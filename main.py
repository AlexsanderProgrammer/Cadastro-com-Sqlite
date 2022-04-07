from PyQt5 import uic, QtWidgets
import sqlite3

def chamar_tela1():
    tela_2.close()

def listar_dados():
    tela_2.show()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_2.tableWidget.setRowCount(len(dados_lidos))
    tela_2.tableWidget.setColumnCount(3)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 3):
            tela_2.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

    banco.close()


def salvar_dados():

    nome = tela.nome.text()
    endereco = tela.endereco.text()
    email = tela.email.text()

    try:
        banco = sqlite3.connect('banco_cadastro.db')
        cursor = banco.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS dados ( nome text,endereco text,email text)")
        cursor.execute("INSERT INTO dados VALUES ('" + nome + "','" + endereco + "','" + email + "')")
        banco.commit()
        banco.close()
        tela.nome.setText("")
        tela.endereco.setText("")
        tela.email.setText("")

        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ", erro)



app = QtWidgets.QApplication([])
tela = uic.loadUi("formulario.ui")
tela_2 = uic.loadUi("lista_dados.ui")
tela.cadastrar.clicked.connect(salvar_dados)
tela.consultar.clicked.connect(listar_dados)
tela_2.voltar.clicked.connect(chamar_tela1)



tela.show()
app.exec()
