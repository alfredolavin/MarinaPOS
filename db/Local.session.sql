SELECT regexp_replace(
  nombre,
  '(?<=\w{2})[AEIOU](?=\w{2})', '')   FROM inventario.principio_activo;

SELECT reg FROM information_schema."columns" 
  WHERE table_schema not in ('pg_catalog', 'information_schema') AND
  column_default like 'nextval(%'