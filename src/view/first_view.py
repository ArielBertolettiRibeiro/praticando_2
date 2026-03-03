def introduction_page() -> str:

    message = """

    Sistema de músicas.

    1 - Cadastrar música
    2 - Mostrar playlist
    3 - Sair

    """

    print(message)
    command = input("Comando: ") 

    return command