#!/bin/bash

# Função para procurar e remover pastas __pycache__
remove_pycache() {
    for pycache_dir in $(find . -type d -name "__pycache__"); do
        echo "Removendo $pycache_dir"
        rm -r "$pycache_dir"
    done   
}

remove_pyteste_cache() {
    for pytest_cache in $(find . -type d -name ".pytest_cache"); do
        echo "Removendo $pytest_cache"
        rm -r "$pytest_cache"
    done
}

# Chamando a função para remover pastas __pycache__
remove_pycache
remove_pyteste_cache
echo "Remoção de pastas __pycache__ concluída."
