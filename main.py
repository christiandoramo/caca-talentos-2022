from datetime import datetime
import ModuloRepositorio as r
import ModuloSistema as s
import PySimpleGUI as sg

# dados de produtos A,B,C e Repositorio predefinidos
repositorio = r.Repositorio(0, 0, 0, 0)
repositorio.ProdutosN = repositorio.ProdutosN+1
produto1 = s.Produto(repositorio.ProdutosN, "Produto 1", "aa aaaa", 12)
repositorio.ProdutosN = repositorio.ProdutosN+1
produto2 = s.Produto(repositorio.ProdutosN, "Produto 2", "bbbb bb", 30)
repositorio.ProdutosN = repositorio.ProdutosN+1
produto3 = s.Produto(repositorio.ProdutosN, "Produto 3", "cccc cc", 50)

# layouts
layout1 = [
    [sg.Text("Nome do Atendente")],
    [sg.InputText(key="nomeAtendente")],
    [sg.Text("Nome do Cliente")],
    [sg.InputText(key="nomeCliente")],
    [sg.Text("Data de Nascimento")],
    [sg.InputText(key="nascimento")],
    [sg.Text("Email")],
    [sg.InputText(key="email")],
    [sg.Text("Telefone")],
    [sg.InputText(key="telefone")],
    [sg.Button("Iniciar Sessão"), sg.Button("Cancelar")],
]




headings = ["ID VENDA", "DATA DE VENDA","ID CLIENTE","CLIENTE","ID ATENDENTE","ATENDENTE",
                "ID PRODUTO", "PRODUTO", "PRECO", "QUANTIDADE", "VALOR TOTAL"]
linhas = 0

layout2 = [
    [sg.Text("Produto a ser vendido")],
    [sg.InputText(key="produto")],  # 1, 2 ou 3...
    [sg.Text("Quantidade a ser vendida")],
    [sg.InputText(key="quantidade")],
    [sg.Button("Vender"), sg.Button("Cancelar")],
    [sg.Table(values = [[]], headings = headings,
                max_col_width=35,
                auto_size_columns=True,
                display_row_numbers=True,
                justification="right",
                num_rows=10,
                row_height=35,
                key="tabela")]
]

# janelas
janela = sg.Window("Inicio da Sessão", layout1)

cliente = None
atendente = None
sessao = False
while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Iniciar Sessão":
        nomeAtendente = valores["nomeAtendente"]
        nomeCliente = valores["nomeCliente"]
        email = valores["email"]
        telefone = valores["telefone"]
        nascimento = valores["nascimento"]
        if (nomeAtendente and nomeCliente and email and telefone and nascimento):
            repositorio.ClientesN += 1
            cliente = s.Cliente(nomeCliente, email, telefone,
                                nascimento, repositorio.ClientesN)
            repositorio.AtendentesN += 1
            atendente = s.Atendente(nomeAtendente, repositorio.AtendentesN)
            sessao = True
            break
janela.close()

if sessao:
    janela = sg.Window("Sessão de Vendas", layout2)
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Cancelar":
            break
        if evento == "Vender":
            produto = valores["produto"]
            quantidade = valores["quantidade"]
            if (produto == '1' or produto == '2' or produto == '3'):
                if (quantidade != '0' and quantidade != ''):
                    if produto == '1':
                        produto = produto1
                    elif produto == '2':
                        produto = produto2
                    else:
                        produto = produto3
                    quantidade = int(quantidade)
                    repositorio.VendasN += 1
                    venda = s.Venda(repositorio.VendasN, produto,
                                    quantidade, atendente, cliente, datetime.now())
                    repositorio.addListaVendas(venda)
                    repositorio.escreverFile()  # Implementado num arquivo .csv
                    linhas +=1
                    dados = repositorio.lerFile()
                    janela["tabela"].update(values = dados[len(dados)-1]) # ultimo array de arrays
    janela.close()
