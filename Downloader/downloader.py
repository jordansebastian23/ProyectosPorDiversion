import yt_dlp
import os

def descargar_video_facebook(url, nombre_archivo):
    try:
        if not os.path.exists('videos'):
            os.makedirs('videos')

        opciones = {
            'format': 'best',
            'outtmpl': os.path.join('videos', nombre_archivo),
            'noplaylist': True 
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])
        
        print(f"Video descargado exitosamente como: videos/{nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error durante la descarga: {e}")


video_url = input("Ingresa la url: ")
nombre_archivo = input("Ingresa el nombre del archivo: ")
nombre_archivo = nombre_archivo + ".mp4"

descargar_video_facebook(video_url, nombre_archivo)
