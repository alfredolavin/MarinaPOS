#!/usr/bin/env bash
database_file=../marinapos.db

if whiptail --yesno "Recrear $database_file?" 8 60 ;then
  rm $database_file
  cat ./MarinaPOS.sql | sqlite3 $database_file

  cd ../datos
  for file in *.csv
  do
    echo "Agregando $file a $database_file"
    sqlite3 $database_file ".import --csv --skip 1 $file ${file%%.*}"
  done

  echo "Creando modelo para peewee..."
  python -m pwiz --engine=sqlite $database_file > ../model.py 
  echo "Hecho!! ✨ 🌟 ✨";
else
    echo No
fi