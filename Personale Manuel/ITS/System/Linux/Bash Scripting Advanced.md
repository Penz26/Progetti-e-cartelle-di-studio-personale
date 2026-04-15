
>Questa funzione serve a stampare a schermo quello dentro EOF

``` Shell
usage() {
	cat <<EOF
Uso: $0 INPUT OUTPUT 

INPUT File sorgente
OUTPUT File di destinazione
EOF
}
