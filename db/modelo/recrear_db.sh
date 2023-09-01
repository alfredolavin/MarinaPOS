#!/usr/bin/env bash
database_file=marinapos.db

cd ..
if whiptail --yesno "Recrear $database_file?" 8 60 ;then
  rm $database_file
  cat ./modelo/MarinaPOS.sql | sqlite3 $database_file

  cd ./datos
  for file in *.csv
  do
    echo "Agregando $file a $database_file"
    sqlite3 $database_file ".import --csv --skip 1 $file ${file%%.*}"
  done

  echo "Hecho!! ✨ 🌟 ✨";
else
    echo No
fi