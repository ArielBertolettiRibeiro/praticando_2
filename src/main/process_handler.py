from src.view.first_view import introduction_page

def start() -> None:
    while True:

        command = introduction_page()

        if command == "1": print("Teste 1")
        elif command == "2": print("Teste 2")
        elif command == "3": exit()
        else: print("\nOpção inválida! \n\n")
