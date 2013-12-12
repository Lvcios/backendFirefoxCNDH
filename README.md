backendFirefoxCNDH
==================

Programación del backend de la apliación CNDH de Firefox

Uso de la API Mobile con CURL:

Desde una terminal:
GET
curl http://127.0.0.1:8000/api/v1/
curl http://127.0.0.1:8000/api/v1/reporte/ #todos los reporte
curl http://127.0.0.1:8000/api/v1/reporte/1/ #el reporte con folio 1

curl http://127.0.0.1:8000/api/v1/institucion/1/ 
curl http://127.0.0.1:8000/api/v1/status/1/


POST
curl --dump-header - -H "Content-Type: application/json" -X POST -- data 
"{
  \"nombreInst\":\"api/v1/institucion/1/\",
  \"nombre\":\"Lvcios\",
  \"apellido\":\"Malfoi\",
  \"correo\":\"lmalfoi@slytherin.hogwarts.uk\",
  \"telefono\":\"1234567890001\",
  \"descripcion\":\"El profesor Snape nos deja demasiada tarea.\,
  \"direccion\":\"Oxford Stree 789. Londres.\",
  \"fecha\":\"19/12/2013\",
  \"reincide\":\"True\",
  }"
