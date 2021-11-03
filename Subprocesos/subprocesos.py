from imgurpython import ImgurClient
import urllib.request
import timeit
from concurrent.futures import ThreadPoolExecutor
 
secreto_cliente = "5f8c3cce299db5e26a2eb96b0b7809a82805c9ad"
id_cliente = "bfa0e227a1c5643"
links=[]
cliente = ImgurClient(id_cliente, secreto_cliente)
 
# Metodo para la descarga url imagen
# Datos necesarios del metodo
# Nombre de la imagen => yntdWAr
# Formato de la imagen => png
#logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
 
def descarga_url_img(link):
   # Con esto ya podemos obtener el corte de la url imagen
   nombre_img = link.split("/")[3]
   formato_img = nombre_img.split(".")[1]
   nombre_img = nombre_img.split(".")[0]
   print(nombre_img, formato_img)
   url_local = "D:\Javy Daniel\Pictures\Saved Pictures\subprocesos/{}.{}"
   #Guardar nne local las imagenes
   urllib.request.urlretrieve(link, url_local.format(nombre_img, formato_img))
 
def main():
    id_album = "bUaCfoz"
    imagenes = cliente.get_album_images(id_album)
   
    for image in imagenes:
        links.append(image.link)
    
    #ThreadPoolExecutor: subclase de Executor que usa un grupo de hilos max_workers como máximo para ejecutar llamadas de forma asincrónica.
    with ThreadPoolExecutor(max_workers= 10 )as executor:
    # map: produce simultáneamente un conjunto de resultados de una entrada iterable, siempre devuelve los valores en orden basados en las entradas.
        executor.map(descarga_url_img, links)

if __name__ == "__main__":
    print("Tiempo de descarga: {}".format(timeit.Timer(main).timeit(number=1)))

