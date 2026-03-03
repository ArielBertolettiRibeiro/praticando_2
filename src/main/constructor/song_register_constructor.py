from src.view.song_register_view import SongRegisterView
# Fiz a importação do arquivo song_regiter_view, onde importei a classe SongRegisterView que contémo
# método responsável por pegar as informações das músicas.

def song_register_process(): # Função - Processo de registro de músicas, basicamente um usecase.

    song_register_view = SongRegisterView() # Criei uma instância da classe que possui o método

    new_song_infomrations = song_register_view.registry_song_initial()
    # Depois vamos enviar essa informação acima para o controller consumir
    # Aqui vai ser a ligação do meu controller com minha view, relamente como um usecase