usuario_correto = "admin"
senha_correta = "1234"

usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem-sucedido! Bem-vindo, admin.")
else:
    print("Usuário ou senha incorretos. Tente novamente.")
