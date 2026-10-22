import pymysql

class GerenciadorBanco:
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='rpg'
        )
        self.cursor = self.conexao.cursor()

    def consultarPersonagens(self):
        consuPsngAll = input("Procura algum personagem em especifo? Y/N ")
        if consuPsngAll.upper() == "Y":
            consuPsng = input("Coloque o nome deste personagem: ")

            sql = "SELECT * FROM personagem WHERE nome_p = %s"
            valor = (consuPsng, )
            self.cursor.execute(sql, valor)
            resultados = self.cursor.fetchall()

            print("\n--- Personagens no game ---")
            if not resultados:
                print("Ainda não tem nenhum personagem.")
            
            for linha in resultados:
                print(
                     f"\nID: {linha[0]}"
                    f"\nNome: {linha[1]}"
                    f"\nClasse: {linha[2]}"
                    f"\nForça: {linha[3]}"
                    f"\nDestreza: {linha[4]}"
                    f"\nPV: {linha[5]}"
                    )

        elif consuPsngAll.upper() == "N":
            sql = "SELECT * FROM personagem"
            self.cursor.execute(sql)
            resultados = self.cursor.fetchall()

            print("\n--- Personagens no game ---")
            if not resultados:
                print("Ainda não tem nenhum personagem.")

            for linha in resultados:
                print(
                    f"\nID: {linha[0]}"
                    f"\nNome: {linha[1]}"
                    f"\nClasse: {linha[2]}"
                    f"\nForça: {linha[3]}"
                    f"\nDestreza: {linha[4]}"
                    f"\nPV: {linha[5]}"
                    )

            
    def cadastroPersonagem(self, nome, classe, forca, destreza, vida):
        sql = "INSERT INTO personagem (nome_p, classe_p, forca_p, destreza_p, vida_p) VALUES (%s, %s, %s, %s, %s)"
        valores = (nome, classe, forca, destreza, vida)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print(f"\n Personagem '{nome}' inserido com sucesso!")


    def alterarPersonagem(self):
        sql = "SELECT * FROM personagem"
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()

        for linha in resultados:
            print(f"{linha[0]} - {linha[1]}")

        escolhaPsngAlterUsu = int(input("\n Qual personagem deseja fazer alterações? "))

        print(
            f"\n 1 - FORÇA"
            f"\n 2 - DESTREZA"
            f"\n 3 - VIDA"
            )
        escolhaStsAlterUsu = int(input("Oque deseja alterar? "))

        if escolhaStsAlterUsu == 1:
            try:
                novaForca = int(input("Digite a nova força do personagem: "))
                sql = "UPDATE personagem SET forca_p = %s WHERE id_personagem = %s;"
                valores = (novaForca, escolhaPsngAlterUsu)
                self.cursor.execute(sql, valores)
                self.conexao.commit()
                print(f"\n Força alterada com sucesso!")
            except ValueError:
                print("Falha ao alterar a força.")

        if escolhaStsAlterUsu == 2:
            try:
                novaDestreza = int(input("Digite a nova destreza do personagem: "))
                sql = "UPDATE personagem SET destreza_p = %s WHERE id_personagem = %s;"
                valores = (novaDestreza, escolhaPsngAlterUsu)
                self.cursor.execute(sql, valores)
                self.conexao.commit()
                print(f"\n Destreza alterada com sucesso!")
            except ValueError:
                print("Falha ao alterar a destreza.")

        if escolhaStsAlterUsu == 3:
            try:
                novaVida = int(input("Digite o novo HP do personagem: "))
                sql = "UPDATE personagem SET vida_p = %s WHERE id_personagem = %s;"
                valores = (novaVida, escolhaPsngAlterUsu)
                self.cursor.execute(sql, valores)
                self.conexao.commit()
                print(f"\n HP alterado com sucesso!")
            except ValueError:
                print("Falha ao alterar a vida.")


    def excluirPersonagem(self):
        sql = "SELECT * FROM personagem"
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        
        for linha in resultados:
            print(f"\n {linha[0]} - {linha[1]}")

        try:
            escolhaPsngExcUsu = int(input("Qual personagem deseja excluir? "))
            sql = "DELETE FROM personagem WHERE id_personagem = %s"
            valor = (escolhaPsngExcUsu, )
            self.cursor.execute(sql, valor)
            self.conexao.commit()
            print(f"\n Personagem apagado com sucesso!")
        except ValueError:
            print("Falha ao apagar personagem.")


    def fecharConexao(self):
        self.cursor.close()
        self.conexao.close()