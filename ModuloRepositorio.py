import csv

class Repositorio:
    listaVendas = list()

    def __init__(self, AtendentesN, ClientesN, ProdutosN, VendasN):
        # numero de registrados
        self.AtendentesN = AtendentesN
        self.ClientesN = ClientesN
        self.ProdutosN = ProdutosN
        self.VendasN = VendasN

    def addListaVendas(self, venda):
        self.listaVendas.append(venda)

    def escreverFile(self):
        # PERSISTENCIA LEITURA E ESCRITA
        campos = ["ID VENDA","DATA DE VENDA", "ID CLIENTE","CLIENTE","ID ATENDENTE",
                  "ATENDENTE","ID PRODUTO","PRODUTO","PRECO","QUANTIDADE","VALOR TOTAL"]
        linhas = []
        for venda in self.listaVendas:
            linhas.append([str(venda.idVenda), str(venda.dataVenda), str(venda.cliente.idCliente),
                           str(venda.cliente.nome), str(
                               venda.atendente.idAtendente),
                           str(venda.atendente.nome), str(
                               venda.produto.idProduto), str(venda.produto.nome),
                           str(venda.produto.preco), str(venda.quantidade), str(venda.calcularVenda())])
        nomearquivo = "repositorio.csv"
        with open(nomearquivo, 'w') as arquivocsv:
            escritorcsv = csv.writer(arquivocsv)
            escritorcsv.writerow(campos)  # linha 1 - 1 array de campos
            escritorcsv.writerows(linhas)  # linhas>1 - varios arrays de dados

    def lerFile(self):
        # PERSISTENCIA LEITURA E ESCRITA
        nomearquivo = "repositorio.csv"
        arrayStrings = []
        arrayArrayStrings = [[]]
        with open(nomearquivo, 'r') as arquivocsv:
            leitorcsv = csv.reader(arquivocsv)
            next(leitorcsv)# campos - retorn primeira linha e pula uma
            for linha in leitorcsv: #pegando cada linha a abaixo de campos
                arrayStrings.append(linha) #pegando cada array
            arrayArrayStrings.append(arrayStrings)
            return arrayArrayStrings # retorna ultimo array string de ultima posicao
