#GitLab [[aptly Repository Debian-Ubuntu]]
```YML
stages:
  - update
  - build
  - publish
variables:
#Variabili per il control di Debian
  PACKAGE_NAME: "pipeline"
  PACKAGE_VERSION: "1.0.0"
  PACKAGE_ARCHITECTURE: "amd64"
  PACKAGE_MAINTAINER: "Manuel Bernardelli"
  PACKAGE_DESCRIPTION: "First try of the GitLab CI/CD integration"

#Variabili per pubblicazione con aptly
  NOME_REPO: "Manuel-prod"
  DISTRIBUTION: "noble"
update-sys:
  stage: update
  tags:
    - aptly-noble_24.04
  script:
    - sudo apt update

build-package:
  stage: build
  tags:
    - aptly-noble_24.04
  script:
    - echo "Creazione struttura pacchetto Debian"
	- mkdir -p ${PACKAGE_NAME}/DEBIAN
	- mkdir -p ${PACKAGE_NAME}/usr/local/bin
	- cp src/pipeline.sh ${PACKAGE_NAME}/usr/local/bin/
	- touch ${PACKAGE_NAME}/DEBIAN/control
	  
#Scrittura dei Metadati del pacchetto compilato
	- |
	cat <<EOF > ${PACKAGE_NAME}/DEBIAN/control
	Package: ${PACKAGE_NAME}
	Version: ${PACKAGE_VERSION}
	Architecture: ${PACKAGE_ARCHITECTURE}
	Maintainer: ${PACKAGE_MAINTAINER}
	Description: ${PACKAGE_DESCRIPTION}
	EOF
    - echo "Compilazione del pacchetto in formato .deb"
	- dpkg-deb --build ${PACKAGE_NAME} ${PACKAGE_NAME}_${PACKAGE_VERSION}_${PACKAGE_ARCHITECTURE}.deb
  artifacts:
	paths:
	  - "*.deb"
	expire_in: 1 day

deploy-package:
  stage: publish
  tags:
	- aptly-noble_24.04
	  
#Per utilizzare artifacts che provengono da altri job dobbiamo mettere come dipendeza il job in cui viene prodotto
  needs:
	- job: build-package
	artifacts: true #Scarica il .deb generato prima dal job specificato in job
  script:
	- echo "=== 1. Costruzione variabili esplicite ==="
	# Nome del file.deb che c'è da caricare
	- export DEB_FILE="${PACKAGE_NAME}_${PACKAGE_VERSION}_${PACKAGE_ARCHITECTURE}.deb"
	# Nome dello snapshot legato in modo univoco al commit di Git es: (pipeline-snap-codice-del-commit)
	- export SNAPSHOT_COMMIT="${PACKAGE_NAME}-snap-${CI_COMMIT_SHORT_SHA}"

	#Rimpiazza forzatamente il vecchio file con quello nuovo se quello vecchio ha lo stesso nome

	- echo "=== 2. Aggiunta/Aggiornamento del pacchetto .deb ==="
	- sudo aptly repo add -force-replace ${NOME_REPO} ${DEB_FILE}
	- echo "=== 3. Creazione dello Snapshot con ID del commit ==="
	- sudo aptly snapshot create ${SNAPSHOT_COMMIT} from repo ${NOME_REPO}
	- echo "=== 4. Switch atomico della pubblicazione ==="
	- sudo aptly publish switch -batch -gpg-key="${PERSONAL_APTLY_NOBLE_KEY}" -passphrase="${PERSONAL_REPO_GPG_KEY}" ${DISTRIBUTION} . "${SNAPSHOT_COMMIT}"
	- echo "=== 5. Verifica delle pubblicazioni attive ==="
	- sudo aptly publish list
```
