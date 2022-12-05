from ModuloSistema import Venda
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

    def listarVendas(self): # No Console
        for venda in self.listaVendas:
            print("ID VENDA: ", venda.idVenda, " | DATA DE VENDA: ",
                  venda.dataVenda.strftime("%m/%d/%Y, %H:%M:%S"))
            print("ID CLIENTE: ", venda.cliente.idCliente,
                  " | CLIENTE: ", venda.cliente.nome)
            print("ID ATENDENTE: ", venda.atendente.idAtendente,
                  " | ATENDENTE: ", venda.atendente.nome)
            print("ID PRODUTO: ", venda.produto.idProduto,
                  " | PRODUTO: ", venda.produto.nome)
            print("PRECO PRODUTO: ", venda.produto.preco,
                  " | QUANTIDADE: ", venda.quantidade)
            print("VALOR TOTAL: ", venda.calcularVenda(), "\n")

    def escreverFile(self):
        # PERSISTENCIA LEITURA E ESCRITA
        campos = ["ID VENDA", "DATA DE VENDA", "ID CLIENTE", "CLIENTE", "ID ATENDENTE",
                  "ATENDENTE", "ID PRODUTO", "PRODUTO", "PRECO", "QUANTIDADE", "VALOR TOTAL"]
        linhas = []
        for venda in self.listaVendas:
            linhas.append([str(venda.idVenda), str(venda.dataVenda), str(venda.cliente.idCliente),
                           str(venda.cliente.nome), str(
                               venda.atendente.idAtendente),
                           str(venda.atendente.nome), str(
                               venda.produto.idProduto), str(venda.produto.nome),
                           str(venda.produto.preco), str(venda.quantidade), str(venda.calcularVenda())])
        nomearquivo = "repositorio.csv"
        try:
            with open(nomearquivo, 'w') as arquivocsv:
                escritorcsv = csv.writer(arquivocsv)
                escritorcsv.writerow(campos)  # linha 1 - 1 array de campos
                escritorcsv.writerows(linhas)  # linhas>1 - varios arrays de dados
        except:
            print("não foi possivel acessar o arquivo")

    def lerFile(self):
        # PERSISTENCIA LEITURA E ESCRITA
        nomearquivo = "repositorio.csv"
        campos = []
        linhas = []
        try:
            with open(nomearquivo, 'r') as arquivocsv:
                leitorcsv = csv.reader(arquivocsv)
                # campos - retorn primeira linha e pula uma
                campos = next(leitorcsv)
                for linha in leitorcsv:
                    linhas.append(linha)
            # pega o numero total de linhas
                print("Numero total de linhas: %d" % (leitorcsv.line_num))
                print('Campos:' + ', '.join(campo for campo in campos))
                for linha in linhas:
                    # conversao de cada coluna de uma linha
                    for col in linha:
                        print("%5s" % col, end=" "),
                    print('\n')
        except:
            print("não foi possivel acessar o arquivo")
