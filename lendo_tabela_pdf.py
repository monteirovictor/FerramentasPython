

#intalar a lib -> pip install tabula-py e ter o java instalado no computador

import tabula
import pandas as pd

lista_tabelas=tabula.read_pdf("/content/JULIANA_1S2011.pdf",pages="6")
print(len(lista_tabelas))

for tabela in lista_tabelas:
  display(tabela)

#exportando em excel
tabela.to_excel("output.xlsx")