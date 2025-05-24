#!/bin/bash

BASE_DIR="$(dirname "$0")"
DIST_DIR="$BASE_DIR/../dist"



clear_project() {
    bash conf/clear_project.sh
}

build () {
    pyinstaller --noconfirm --onedir --windowed \
        --icon "$BASE_DIR/../img/logo.ico" \
        --name "CameraIpClient" \
        --add-data "$BASE_DIR/../src:src/" \
        --hidden-import "PIL._tkinter_finder" \
        --hidden-import "PIL.ImageTk" \
        --add-data "$BASE_DIR/../img:img/" \
        "$BASE_DIR/../main.py"

    cp -r img/ "$DIST_DIR/CameraIpClient/img"

    rm -r build
    rm CameraIpClient.spec

    cd "$DIST_DIR/CameraIpClient" || exit
    zip -r "../CameraIpClient.zip" ./*
    cd - || exit
    rm -r $DIST_DIR/CameraIpClient
}


clear_project
build



