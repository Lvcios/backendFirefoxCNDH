// Get JSON: Descargar un Archivo JSON de manera asincrona.
// params:
// url: URL del archivo JSON
// callback: función callback (se pasa como parametro el objeto JSON descargado)
// error: funcion que se ejecuta en caso de error al descargar el archivo.
var getJSON = function (url, callback, error) {
  var xhr = new XMLHttpRequest();
  xhr.open('get', url, true);
  xhr.responseType = 'json';
  xhr.onload = function () {
    var status = xhr.status;
    if (status == 200) {
      callback && callback(xhr.response);
    } else {
      error && error(status);
    }
  };
  xhr.send();
};

var oficinas;
var source = $('#estados').html();
var estados = Handlebars.compile(source);

//source = $('#municipios').html();
//var municipios = Handlebars.compile(source);

function go() {
	// Descargo la colección de oficinas y la almaceno en local storage
	// o la recupero del local storage cuando no hay conexión
	getJSON( 'http://localhost:3000/oficinas?' + Date.now(),
	  function (data) {
			oficinas = data;
			$('section').append( estados(data) );
	  },
	  function () {
	    console.log("Error!");
	  }
	);

	$('section').on('click', function (evnet) {
		event.preventDefault();
		console.log(event);
	});	
}

$(document).on('ready', go)