# Thiago Oliveira Spindola
"""
    Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
  linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de
  entrada  faz  parte  da  linguagem  𝐿  definida  por
  𝐿 = {𝑥 | 𝑥 ∈ {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.

    O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
  contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de
  entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que
  podem existir em um arquivo de testes para o programa que você irá desenvolver:

        3
        abbaba
        abababb
        bbabbaaab

    Neste  exemplo  temos  3  strings  de  entrada.  O  número  de  strings em  cada  arquivo  será
  representado  por  um  número  inteiro  positivo.  A  resposta  do  seu  programa  deverá  conter  uma, e
  somente uma linha de saída para cada string. Estas linhas conterão a string de entrada e o resultado
  da validação conforme o formato indicado a seguir:

        abbaba: não pertence.

    A  saída  poderá  ser  enviada  para  um  arquivo  de  textos,  ou  para  o  terminal  padrão  e  será
  composta de uma linha de saída por string de entrada. No caso do exemplo, teremos 3 linhas de saída.
  Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
  contendo um número diferente de strings diferentes. Os arquivos de entrada criados para os seus testes
  devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor
  irá  testar  seu  programa  com  os  arquivos  de  testes  que  você  criar  e  com,  no  mínimo  um  arquivo  de
  testes criado pelo próprio professor.
"""


def readFile(txt):
    quantidade = 0
    ordem = False

    with open(txt) as file:
        entrada = file.readline()
        quantidade = int(entrada[0])

        print(txt + "\n")

        while True:
            valido = False

            if quantidade == 0:
                print("")
                break

            entrada = file.readline()
            entrada = entrada.rstrip("\n")

            for l in entrada:
                if l == "a" or "b" or "c":
                    if l == "a":
                        if not ordem:
                            ordem = True
                            sequencia = 0
                        else:
                            ordem = False
                            valido = False
                            sequencia = 0
                            break
                    elif l == "b":
                        if ordem:
                            sequencia += 1
                            if sequencia == 2:
                                ordem = False
                                sequencia = 0
                                valido = True
                        else:
                            valido = True
                    else:
                        valido = True
                else:
                    valido = False
                    break

            quantidade -= 1

            if valido:
                print("'" + entrada + "'" + " pertence.")
            else:
                print("'" + entrada + "'" + " não pertence.")


readFile("Texto_1.txt")
readFile("Texto_2.txt")
readFile("Texto_3.txt")
