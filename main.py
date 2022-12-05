from datetime import date
from datetime import datetime
import ModuloRepositorio as r
import ModuloSistema as s
import ModuloJanela as j

repositorio = r.Repositorio(0, 0, 0, 0)

repositorio.ClientesN = repositorio.ClientesN+1
cliente = s.Cliente("Jose", "jos@email", "99999",
                  date(1999, 1, 2), repositorio.ClientesN)

repositorio.ClientesN = repositorio.ClientesN+1
cliente2 = s.Cliente("Mario", "jos@email", "99999",
                   date(1999, 1, 2), repositorio.ClientesN)

repositorio.AtendentesN = repositorio.AtendentesN+1
atendente = s.Atendente("Maria", "mar@email", "88888",
                      date(1997, 1, 3), repositorio.AtendentesN)

repositorio.ProdutosN = repositorio.ProdutosN+1
produtoA = s.Produto(repositorio.ProdutosN, "prodA", "aaaaaa", 22)
repositorio.ProdutosN = repositorio.ProdutosN+1
produtoB = s.Produto(repositorio.ProdutosN, "prodB", "bbbbbb", 33.5)
repositorio.ProdutosN = repositorio.ProdutosN+1
produtoC = s.Produto(repositorio.ProdutosN, "prodC", "cccccc", 55)

repositorio.VendasN = repositorio.VendasN+1
venda1 = s.Venda(repositorio.VendasN, produtoA, 10,
               atendente, cliente, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda2 = s.Venda(repositorio.VendasN, produtoB, 8,
               atendente, cliente, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda3 = s.Venda(repositorio.VendasN, produtoC, 6,
               atendente, cliente, datetime.now())

repositorio.addListaVendas(venda1)
repositorio.addListaVendas(venda2)
repositorio.addListaVendas(venda3)

repositorio.listarVendas()

repositorio.VendasN = repositorio.VendasN+1
venda4 = s.Venda(repositorio.VendasN, produtoA, 0,
               atendente, cliente2, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda5 = s.Venda(repositorio.VendasN, produtoB, 5,
               atendente, cliente, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda6 = s.Venda(repositorio.VendasN, produtoC, 6,
               atendente, cliente2, datetime.now())
repositorio.VendasN = repositorio.VendasN+1
venda7 = s.Venda(repositorio.VendasN, produtoC, 10,
               atendente, cliente2, datetime.now())

repositorio.addListaVendas(venda4)
repositorio.addListaVendas(venda5)
repositorio.addListaVendas(venda6)
repositorio.addListaVendas(venda7)

repositorio.listarVendas()
repositorio.escreverFile()
repositorio.lerFile()
