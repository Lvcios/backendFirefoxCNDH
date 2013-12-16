backendFirefoxCNDH
==================

Programación del backend de la apliación CNDH de Firefox

Uso de la API Mobile con CURL:

Desde una terminal:

###GET

	curl http://127.0.0.1:8000/api/v1/
	curl http://127.0.0.1:8000/api/v1/reporte/ #todos los reporte
	curl http://127.0.0.1:8000/api/v1/reporte/1/ #el reporte con folio 1
	curl http://127.0.0.1:8000/api/v1/institucion/1/
	curl http://127.0.0.1:8000/api/v1/status/1/

###POST 

	curl --dump-header - -H "Content-Type: application/json" -X POST --data  "{\"nombreInst_id\":\"/api/v1/institucion/1/\",\"nombre\":\"Lvcios\",\"apellido\":\"Malfoy\",\"correo\":\"lmalfoi@slytherin.hogwarts.uk\",\"telefono\":\"123456780\",\"descripcion\":\"El que no puede ser nombrado ha atacado de nuevo.\",\"direccion\":\"London Street 748\",\"fecha\":\"19 de Octubre 2013\",\"reincide\":true,\"status_id\":\"/api/v1/status/1/\"}" 127.0.0.1:8000/api/v1/reporte/
		
Nota: El ' \ ' antes de cada ' " ' en el json del post es una particularidad del funcionamiento de CURL en Windows.

####Ejemplo de paquete que envia el frontend
```js
{
	"dependencia":"5", //ID de la dependencia
	"otro":"nombre", //Nombre de de la dependencia si es que marco otro  [no se embia si no es nesesario]
	"nombre":"Juan", 
	"apellido":"filipino",
	"correo":"nombre@email.dominio",
	"direccion":"Esto es un texto con una dirección",
	"telefono":"212-323-1233",
	"descripcion":"El texto con la historia del usuario",
	"fecha":"1233-43-32",
	"reincide": "true" // or false   [no se embia si no es nesesario]
}
```

###Response 
	curl http://127.0.0.1:8000/api/v1/reporte/1/
	response: {"apellido": "PEREZ", "compete": "", "correo": "hiram@hiramperez.net", "descripcion": "aspdashdlkasjld", "direccion": "Calle  X 899", "fecha": "19/10/2013", "fechaUpload": "2013-12-11T15:29:29.733000", "folio": 1, "nombre": "HIRAM", "reincide": true, "resource_uri": "/api/v1/reporte/1/", "telefono": "741852963"} 
