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
