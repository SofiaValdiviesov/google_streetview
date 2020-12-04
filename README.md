# google_streetview

Una herramienta de línea de comandos y un módulo para la API de Google Street View Image.


## Uso

Para info en la consola:

```
google_streetview -h
```
  
Cambiar key:

```
google_streetview -s key="your_dev_key"
```

Busca en la vista de la calle la latitud y la longitud `46.414382,10.013988`:
  
```
google_streetview "46.414382,10.013988"
```
  
Guarda las imágenes en un directorio:

```
google_streetview --location="46.414382,10.013988" --save_downloads=downloads
```
  
Obtener un panorama de 360 girando la cámara "cabeza" con un campo de visión de 90 grados "fov":

```
google_streetview --location="46.414382,10.013988" --fov=90 --heading=0;90;180;270
```
  
Usar como un módulo de Python:

```python

# Importar google_streetview para el módulo api
import google_streetview.google_streetview.api as GSV

# Definir los parámetros para la vista de la calle api
params = [{
	'size': '600x300', # max 640x640 pixels
	'location': '46.414382,10.013988',
	'heading': '151.78',
	'pitch': '-0.76',
	'key': 'your_dev_key'
}]

# Crear un objeto de resultados
results = GSV.results(params)

# Descargar imágenes al directorio 'downloads'.
# Cambiar directorio para guardar en AWS
results.download_links('downloads')

```
  
Para mas detalles ver la [Documentación](https://rrwen.github.io/google_streetview).

  
## Implementación

El paquete [google_streetview](https://pypi.python.org/pypi/google-streetview) usa los siguientes componentes:


| Componentes                                                                                              | Purposito                                                                 |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [Google Street View Image API](https://developers.google.com/maps/documentation/streetview)              | API for Google Street View images                                       |
| [google_streetview.api](https://github.com/rrwen/google_streetview/blob/master/google_streetview/api.py) | Module for interfacing with Google Street View Image API using requests |
| [requests](https://pypi.python.org/pypi/requests)                                                        | Download and get URLs from Google Street View Image API                 |

```
  
  Google Street View Image API     <-- API for Street View Images
               |
      google_streetview.api        <-- URL Request with query string
               |
            request                <-- Download URLs and images
```
Para mas info, leer [NOTES.rst](https://github.com/rrwen/google_streetview/blob/master/NOTES.rst).
