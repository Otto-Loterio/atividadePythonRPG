import conexao
import funcoes

banco = conexao.GerenciadorBanco()

opcaoUsuario = None

while opcaoUsuario != 5:
    print(
    f"\n1 - Consultar personagens"
    f"\n2 - Cadastrar novo personagem"
    f"\n3 - Alterar status dos personagens"
    f"\n4 - Excluir personagens"
    f"\n5 - Encerrar o sistema"
    )
    opcaoUsuario = int(input("Escolha oque deseja fazer: "))

    if opcaoUsuario == 1:
        funcoes.limparTela()
        banco.consultarPersonagens()
        

    elif opcaoUsuario == 2:
        funcoes.limparTela()

        print("--- Criação de personagem ---")
        nomePersonagem = input("Digite o nome do seu personagem: ")
        classePersonagem = input("Digite a classe do seu personagem: ")
        forcaPersonagem = int(input("Digite a força do seu personagem: "))
        destrezaPersonagem = int(input("Digite a destreza do seu personagem: "))
        vidaPersonagem = int(input("Digite a vida do seu personagem: "))
        
        banco.cadastroPersonagem(nomePersonagem, classePersonagem, forcaPersonagem, destrezaPersonagem, vidaPersonagem)


    elif opcaoUsuario == 3:
        funcoes.limparTela()
        banco.alterarPersonagem()

    elif opcaoUsuario == 4:
        funcoes.limparTela()
        banco.excluirPersonagem()


    elif opcaoUsuario == 5:
        funcoes.limparTela()
        print("Até mais viajante!")

    else:
        print("Coloque algo válido!")

banco.fecharConexao()