from pytube import Playlist

# Solicitar la URL de la lista de reproducción al usuario
playlist_url = input("Ingrese la URL de la lista de reproducción de YouTube: ")

try:
    # Crear un objeto de lista de reproducción
    playlist = Playlist(playlist_url)

    # Obtener la información de la lista de reproducción
    print(f"Descargando lista de reproducción: {playlist.title}")

    # Descargar cada video de la lista de reproducción
    for video in playlist.videos:
        print(f"Descargando video: {video.title}")
        video.streams.get_highest_resolution().download()

    print("Descarga completada.")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")
