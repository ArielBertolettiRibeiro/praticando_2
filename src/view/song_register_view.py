import os

class SongRegisterView: # Classe responsável por conter o método que registra novas músicas.

    def registry_song_initial(self) -> dict:
        self.__clear()
        print("Implementar nova música!\n\n")

        title = input("Determinar título: ")
        artist = input("Determinar o artista: ")
        year = input("Determinar o ano de lançamento: ")

        new_song_infomrations = {"Título " : title, "Artista " : artist, "Ano de Lançamento " : year}
        return new_song_infomrations

    def __clear(self):
        os.system("cls||clear")