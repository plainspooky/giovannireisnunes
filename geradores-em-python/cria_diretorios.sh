#!/usr/bin/env bash

let contador=1

arquivo="arquivo"
ext="txt"

cria_arquivo() {
    echo "Criando: $dir/$1"
    touch $1
}

for dir in "abc" "def" "ghi"; do
    mkdir $dir
    cd $dir

    for j in {0..1}; do
        cria_arquivo $arquivo-$contador.$ext
        let contador++

        if (( contador > 5 )); then
            ext="html"
        fi
    done

    [[ $dir == "def" ]] && cria_arquivo .ignore
    cd ..
done
