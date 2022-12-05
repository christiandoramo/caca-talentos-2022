from datetime import date
from datetime import datetime
from ModuloRepositorio import Repositorio
from ModuloSistema import Cliente
from ModuloSistema import Atendente
from ModuloSistema import Produto
from ModuloSistema import Venda

repositorio = Repositorio(0, 0, 0, 0)

repositorio.ClientesN = repositorio.ClientesN+1
cliente = Cliente("Jose", "jos@email", "99999",
                  date(1999, 1, 2), repositorio.ClientesN)

repositorio.ClientesN = repositorio.ClientesN+1
cliente2 = Cliente("Mario", "jos@email", "99999",
                   date(1999, 1, 2), repositorio.ClientesN)

repositorio.AtendentesN = repositorio.AtendentesN+1
atendente = Atendente("Maria", "mar@email", "88888",
                      date(1997, 1, 3), repositorio.AtendentesN)

repositorio.ProdutosN = repositorio.ProdutosN+1
produtoA = Produto(repositorio.ProdutosN, "prodA", "aaaaaa", 22)
repositorio.ProdutosN = repositorio.ProdutosN+1
produtoB = Produto(repositorio.ProdutosN, "prodB", "bbbbbb", 33.5)
repositorio.ProdutosN = repositorio.ProdutosN+1
produtoC = Produto(repositorio.ProdutosN, "prodC", "cccccc", 55)

repositorio.VendasN = repositorio.VendasN+1
venda1 = Venda(repositorio.VendasN, produtoA, 10,
               atendente, cliente, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda2 = Venda(repositorio.VendasN, produtoB, 8,
               atendente, cliente, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda3 = Venda(repositorio.VendasN, produtoC, 6,
               atendente, cliente, datetime.now())

repositorio.addListaVendas(venda1)
repositorio.addListaVendas(venda2)
repositorio.addListaVendas(venda3)

repositorio.listarVendas()

repositorio.VendasN = repositorio.VendasN+1
venda4 = Venda(repositorio.VendasN, produtoA, 0,
               atendente, cliente2, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda5 = Venda(repositorio.VendasN, produtoB, 5,
               atendente, cliente, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda6 = Venda(repositorio.VendasN, produtoC, 6,
               atendente, cliente2, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda7 = Venda(repositorio.VendasN, produtoC, 10,
               atendente, cliente2, datetime.now())

repositorio.addListaVendas(venda4)
repositorio.addListaVendas(venda5)
repositorio.addListaVendas(venda6)
repositorio.addListaVendas(venda7)

repositorio.listarVendas()
repositorio.escreverFile()
repositorio.lerFile()
