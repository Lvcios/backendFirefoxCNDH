backendFirefoxCNDH
==================

Programación del backend de la apliación CNDH de Firefox

Uso de la API Mobile con CURL:

Desde una terminal:

###GET

	curl -H "Authorization: OAuth accessToken" http://127.0.0.1:8000/api/v1/
	curl -H "Authorization: OAuth accessToken" http://127.0.0.1:8000/api/v1/reporte/ #todos los reporte
	curl -H "Authorization: OAuth accessToken"http://127.0.0.1:8000/api/v1/reporte/1/ #el reporte con folio 1
	curl -H "Authorization: OAuth accessToken" http://127.0.0.1:8000/api/v1/institucion/1/
	curl -H "Authorization: OAuth accessToken" http://127.0.0.1:8000/api/v1/status/1/
	
###GET Con filtro
	curl -H "Authorization: OAuth accessToken" 127.0.0.1:8000/api/v1/reporte/?status_id__id=1 #retorna todos los reportes con el status "1" que corresponde a "Recibido", 2 para "Leido" y 3 para "Archivado"

###POST 

	curl --dump-header - -H "Authorization: OAuth accessToken" -H "Content-Type: application/json" -X POST --data  "{\"nombreInst_id\":\"/api/v1/institucion/1/\",\"nombre\":\"Lvcios\",\"apellido\":\"Malfoy\",\"correo\":\"lmalfoi@slytherin.hogwarts.uk\",\"telefono\":\"123456780\",\"descripcion\":\"El que no puede ser nombrado ha atacado de nuevo.\",\"direccion\":\"London Street 748\",\"fecha\":\"19 de Octubre 2013\",\"reincide\":true,\"status_id\":\"/api/v1/status/1/\"}" 127.0.0.1:8000/api/v1/reporte/

Nota: El ' \ ' antes de cada ' " ' en el json del post es una particularidad del funcionamiento de CURL en Windows.

###PUT (actualizar)
	curl --dump-header - -H "Authorization: OAuth accessToken" -H "Content-Type: application/json" -X PUT --data "{\"nombreInst_id\":\"/api/v1/institucion/1/\",\"nombre\":\"Lvcios\",\"apellido\":\"Malfoy\",\"correo\":\"lmalfoi@slytherin.hogwarts.uk\",\"telefono\":\"123456780\",\"descripcion\":\"El que no puede ser nombrado ha atacado de nuevo.\",\"direccion\":\"London Street 748\",\"fecha\":\"19 de Octubre 2013\",\"reincide\":true,\"status_id\":\"/api/v1/status/1/\"}" 127.0.0.1:8000/api/v1/reporte/2/

###PATCH (actualizar un campo específico)
	curl --dump-header - -H "Authorization: OAuth accessToken" -H "Content-Type: application/json" -X PATCH --data "{\"cita\":\"24/Dic/2013\"}" 127.0.0.1:8000/api/v1/reporte/2/
	curl --dump-header - -H "Authorization: OAuth accessToken" -H "Content-Type: application/json" -X PATCH --data "{\"respuestaText\":\"Sr Malfoi, le recomendamos no hablar del tema con nadie mas\"}" 127.0.0.1:8000/api/v1/reporte/3/
	curl --dump-header - -H "Authorization: OAuth accessToken" -H "Content-Type: application/json" -X PATCH --data "{\"compete\":\"NO\"}" 127.0.0.1:8000/api/v1/reporte/2/


###DELETE (eliminar un reporte específico)
	curl --dump-header - -H "Authorization: OAuth accessToken" -H "Content-Type: application/json" -X DELETE  127.0.0.1:8000/api/v1/reporte/2/

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
	curl -H "Authorization: OAuth accessToken" http://127.0.0.1:8000/api/v1/reporte/1/
	response: {"apellido": "PEREZ", "compete": "", "correo": "hiram@hiramperez.net", "descripcion": "aspdashdlkasjld", "direccion": "Calle  X 899", "fecha": "19/10/2013", "fechaUpload": "2013-12-11T15:29:29.733000", "folio": 1, "nombre": "HIRAM", "reincide": true, "resource_uri": "/api/v1/reporte/1/", "telefono": "741852963"} 
