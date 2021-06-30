
#***** Constantes *****#
constantePlanckEV = 4.136e-15 #Constante de Planck em Eletron-Volts
constantePlanckJ = 6.626e-34 #Constante de Plank em Joule
c = 2998e+05  #Velocidade da luz
cargaElementar = 1.602e-19 #Carga Elementar
constanteRydberg = 1.0974e7 #Constante de Rydberg
massaEletron = 9.11e-31 #Massa do Elétron
constanteEletrica = 8.85e-12 #Constante Eletrica
energia_Inicial = -13.6

#***** Funções *****#
def energia_comprimento(comp):
    energia = (constantePlanckEV * c)/ comp #Calcula o Valor da energia com o comprimento
    return energia #Retorna a conta executada na função

def energia_frequencia(freq):
    energia = constantePlanckEV * freq #Calcula o Valor da energia com a Frequência
    return energia #Retorna a conta executada na função

def calcula_raio(n):
    raio = (pow(n, 2)) * 5.29e-11 #Calcula o Valor do Raio com a n
    raio *= 1e9
    return raio #Retorna a conta executada na função

def calcula_velocidade(n):
  # 1/constanteEletrica * (cargaElementar^2 / (2*n*constantePlanckEV))
    velocidade = (1 / constanteEletrica) * ((pow(cargaElementar, 2)) / (2 * n * constantePlanckJ))
  #velocidade = (1/constanteEletrica) * (pow(cargaElementar,2) / (2*n*constantePlanckEV)) #Calcula o Valor do Raio com base no n
    return velocidade #Retorna a conta executada na função

def energia_cinetica(n):
    energiaCinetica = (13.6) / pow(n, 2) #Calcula o Valor da energia Cinetica com base no valor de n
    return energiaCinetica #Retorna a conta executada na função

def energia_potencial(n):
    energiaPotencial = (-27.2) / pow(n, 2) #Calcula o Valor da energia Potencial com base no valor de n
    return energiaPotencial #Retorna a conta executada na função

def calcula_energia_total(n):
    energiaTotal = (energia_potencial(n) + energia_cinetica(n)) #Calcula o Valor da energia Total com base no valor de n
    return energiaTotal #Retorna a conta executada na função

def comprimento_onda(n):
    velocidade = calcula_velocidade(n)
    comprimento = (constantePlanckJ) / (massaEletron * velocidade)
    comprimento *= 1e+9
    return comprimento # Retorna a conta executada na função

def calculaFoton(nInicial,nFinal): 
    energiaNInicial = (-13.6) / pow(nInicial,2) #resultado = -3.4
    energiaNFinal = (-13.6) / pow(nFinal,2) #resultado = -3.4
    energiaFoton = abs(energiaNFinal - energiaNInicial)
    compFoton = (constantePlanckEV * c) / energiaFoton
    freqFoton = energiaFoton / constantePlanckEV
    compFoton *= 1e+9
    return compFoton, freqFoton

# calcular tipo de onda utilizando frequência
def calc_tipo_onda(freq):
    tipo_onda = ""
    if(freq < 1e+09):
        tipo_onda = "Rádio"
    elif(freq >= 1e+09 and freq <= 3e+11):
        tipo_onda = "Microondas"
    elif(freq > 3e+11 and freq <= 4.29e+14):
        tipo_onda = "Infravermelho"
    elif(freq > 4.29e+14 and freq <= 7.5e+14):
        tipo_onda = "Luz Visível"
    elif(freq > 7.5e+14 and freq <= 1e+16):
        tipo_onda = "Ultravioleta"
    elif(freq > 1e+16 and freq <= 1e+19):
        tipo_onda = "Raio-X"
    elif(freq > 1e+19):
        tipo_onda = "Raio Gama"
    return tipo_onda

#Analisa a cor partindo da comparação do Comprimento do Foton
def calculaBalmer(compFoton):
    corLuz = ""
    if(compFoton >= 410.2 and compFoton < 434.1):
        corLuz = "Violeta"
    elif(compFoton >= 434.1 and compFoton < 486.1):
        corLuz = "Azul"
    elif(compFoton >= 486.1 and compFoton < 656.3):
        corLuz = "Verde"
    elif(compFoton > 656.3):
        corLuz = "Vermelha"
    return corLuz

def calcula_nf(compFoton):
    absorve = False
    energiaFoton = (constantePlanckEV * c) / compFoton
    energiaFinal = energia_Inicial + energiaFoton
    n = (energia_Inicial/energiaFinal)**0.5
    x = round(n)
    diferenca = x - n
    diferenca = abs(diferenca)
    print("\n'n' = ",x)
    if(diferenca <= 0.01):
        absorve = True
    return x,absorve
#***** Fim das Funções *****#

#***** Banner *****#
print("""
    ____   __                  _              ______        __              __        __              
   / __ \ / /_   __  __ _____ (_)_____ _____ / ____/____ _ / /_____ __  __ / /____ _ / /_ ____   _____
  / /_/ // __ \ / / / // ___// // ___// ___// /    / __ `// // ___// / / // // __ `// __// __ \ / ___/
 / ____// / / // /_/ /(__  )/ // /__ (__  )/ /___ / /_/ // // /__ / /_/ // // /_/ // /_ / /_/ // /    
/_/    /_/ /_/ \__, //____//_/ \___//____/ \____/ \__,_//_/ \___/ \__,_//_/ \__,_/ \__/ \____//_/     
              /____/                                                                                     
""")
while True:
    entrada = (input("\n====================================\n***** Escolha uma das opções: *****\n[S] - Sair\n[C] - Entrar com Comprimento de onda\n[F] - Entrar com Frequência\n[Q] - Entrar com Número Quântico\n[FT] - Absorção e emissão de fótons com o 'n' inical e 'n' final\n[B] - Espectro de emissão do átomo de hidrogênio\n[A] - Absorção de fóton\n====================================\n->"))
    if(entrada == "C" or entrada == "c"):
    #Comprimento
        print('[*] ATENÇÃO [*] O Comprimento de onda deve ser inserido em notação científica (ex.: XYZe-9)')
        comp = float(input("\n[+] Entre com o Comprimento de onda: "))
        result = energia_comprimento(comp)#Salva na variavel result o retorno da função energia_comprimento(comp)
        print("\n***** RESULTADOS *****")
        print(f"\n[=] Energia do fóton em Ev: {result : .2f} eV")#Printa o valor da energia caculado com o comprimento Formatado 
        print(f"[=] Energia do fóton em J: {(result * cargaElementar): .2e} J")#Printa o valor da energia caculado com o comprimento Formatado 

    elif(entrada == 'F' or entrada == 'f'):
    #Frequência
        freq = -1
        while(freq < 0.0):
            print('[*] ATENÇÃO [*] A Frequência deve ser inserida em notação científica (ex.: XYZe12)')
            freq = float(input("\n[+] Entre com a Frequência: "))
            if(freq < 0.0):
                print("\n [*] ATENÇÃO [*] A frequência não pode ser negativa !!!")
            
        resultado = energia_frequencia(freq) #Salva na variavel resultado o retorno da função energia_frequencia(freq)
        print("\n***** RESULTADOS *****")
        print(f"\n[=] Energia do fóton em Ev: {resultado : .2f} eV") #Printa o valor da energia caculado com a frequência Formatado
        print(f"[=] Energia do fóton em J: {(resultado * cargaElementar): .2e} J")#Printa o valor da energia caculado com o comprimento Formatado 

    elif(entrada == 'q' or entrada == 'Q'):
    #Nível Quantico
        n = 0
        while(n < 1):
            n = int(input("\n[+] Entre com o valor de 'n': "))#Espera uma entrada para o valor de N
            print("\n***** RESULTADOS *****")
            if(n < 1):
                print("\n[*] ATENÇÃO [*] O valor de 'n' não pode ser menor que 1 !!!")#Mensagem de erro ao digitar o número 

        resultado = calcula_raio(n) #Salva na variavel resultado o retorno da função calcula_raio(n)
        print(f"[=] Raio da órbita do elétron da camada {n}: {resultado : .2e}", end=" nm\n")#Printa o valor da Raio Formatado em notação cientifica

        resultado_velocidade = calcula_velocidade(n) #Salva na variavel resultado_velocidade o retorno da função calcula_velocidade(n)
        print(f"[=] Velocidade do elétron:{resultado_velocidade : .2e}", end=" m/s\n")#Printa o valor da Velocidade Formatado em notação cientifica

        resultado_cinetica = energia_cinetica(n) #Salva na variavel resultado_cinetica o retorno da função energia_cinetica(n)
        print(f"[=] Energia Cinética do elétron: {resultado_cinetica : .2f} eV")#Printa o valor da Energia Cinética Formatado em notação cientifica

        resultado_potencial = energia_potencial(n) #Salva na variavel resultado_potencial o retorno da função energia_potencial(n)
        print(f"[=] Energia Potencial do elétron: {resultado_potencial : .2f} eV")#Printa o valor da Energia Potencial Formatado em notação cientifica

        resultado_Total = calcula_energia_total(n) #Salva na variavel resultado_Total o retorno da função calcula_energia_total(n)
        print(f"[=] Energia total do átomo de hidrogênio quando 'n'= {n}: {resultado_Total : .2e} eV") #Printa o valor da energia total Formatado em notação cientifica

        resultado_Comprimento = comprimento_onda(n) #Salva na variavel resultado_Comprimento o retorno da função comprimento_onda(n)
        resultado_Final = (resultado_Comprimento*(1e+9)) #Converte em nm
        print(f"[=] Comprimento de onda de De Broglie: {resultado_Final:.2e}", end=" nm\n") #Printa o valor do Comprimento de Onda Formatado em notação cientifica

    elif(entrada == 'ft' or entrada == 'FT'):
        n_inicial = 0
        n_final = 0
        
        while(n_inicial < 1):
            n_inicial = int(input("\n[+] Digite o 'n' inicial: "))
            if(n_inicial < 1):
                print("\n[*] ATENÇÃO [*] O 'n' inicial não pode ser menor que 1!")
        while(n_final < 1):
            n_final = int(input("\n[+] Digite o 'n' final: "))
            if(n_final < 1):  
                print("\n[*] ATENÇÃO [*] O 'n' final não pode ser menor que 1!")

        if(n_inicial == n_final):
            print("\n[*] ATENÇÃO [*] Os valores de 'n' inicial e 'n' final não podem ser iguais!")
            
        elif(n_inicial < n_final):
            compFoton, freqFoton = calculaFoton(n_inicial,n_final)
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\n***** RESULTADOS *****")
            print("\n[=] Um fóton do tipo %s foi absorvido!" % tipo_onda)#Nas linhas 153 até a 156 elas printam no terminal os devidos resultados
            print("[=] Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("[=] Valor da frequência do fóton: ", f'{freqFoton:.2e}', end=" Hz\n" )
        elif(n_inicial > n_final):
            compFoton, freqFoton = calculaFoton(n_inicial,n_final)#Nas linhas 160 e 161 salvam em uma variavel auxiliar o retorno da função
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\n***** RESULTADOS *****")
            print("\n[=] Um fóton do tipo %s foi emitido!" % tipo_onda)#Nas linhas 161 até a 163 elas printam no terminal os devidos resultados
            print("[=] Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("[=] Valor da frequência do fóton: ", f'{freqFoton:.2e}', end=" Hz\n" )
    
    elif(entrada == 'b' or entrada == 'B'):
        n_Inicial = 0
        serie = 0
        while True:
            serie = int(input("\n====================================\n[+] Escolha uma das opções de série abaixo\n[1] - Série de Lyman('Nfinal' = 1)\n[2] - Série de Balmer('Nfinal' = 2)\n[3] - Série de Paschen('Nfinal' = 3)\n[4] - Série de Brackett('Nfinal' = 4)\n[5] - Série de Pfund('Nfinal' = 5)\n====================================\n->"))
            if(serie > 5 or serie < 1):
                print("\n[*] ATENÇÃO [*] Digite um valor válido!!!")
            else:
                break
        while(n_Inicial < 2 or n_Inicial <= serie):
                n_Inicial = int(input("\n[+] Digite o 'n' inicial: "))
                if(n_Inicial < 2):
                    print("\n[*] ATENÇÃO [*] O 'n' inicial deve ser no mínimo 2!")    
                # a série escolhida não pode ser maior ou igual que o n inicial
                elif(n_Inicial <= serie):
                    print("\n[*] ATENÇÃO [*] O 'n' inicial não pode ser menor ou igual a série escolhida!")
                    
                # caso seja a série de Lyman, Paschen, Brackett ou Pfund   
        if(serie == 1 or serie == 3 or serie == 4 or serie == 5):
            compFoton, freqFoton = calculaFoton(n_Inicial,serie)
            tipo_onda = calc_tipo_onda(freqFoton)
            print("\n***** RESULTADOS *****")
            print("\n[=] Um fóton do tipo %s foi emitido!" % tipo_onda)
            print("[=] Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("[=] Valor da frequência do fóton:", f'{freqFoton:.2e}', end=" Hz\n" )
                # caso seja a série de Balmer
        else:
            compFoton, freqFoton = calculaFoton(n_Inicial,serie)
            if(compFoton >= 410.2):
                corLuz = calculaBalmer(compFoton)
                print("\n[=] Um fóton do tipo 'luz visível' da cor %s foi emitido!" % corLuz)
                    # caso o comprimento seja menor que 410.2, não é luz visível
            else:
                tipo_onda = calc_tipo_onda(freqFoton)
                print("\n[=] Um fóton do tipo %s foi emitido!" % tipo_onda)
                        
            print("[=] Valor do comprimento de onda do fóton: %.2f nm" % compFoton)
            print("[=] Valor da frequência do fóton:", f'{freqFoton:.2e}', end=" Hz\n" )

    elif(entrada == 'a' or entrada == 'A'):
        comprimento_foton = float(input("[+] Entre com o Comprimento de onda: "))
        n,absorve = calcula_nf(comprimento_foton)
        if(absorve == False):
            print("\n***** RESULTADOS *****")
            print("\n[=] O fóton não foi absorvido pelo átomo!!!")
        else:
            print("\n***** RESULTADOS *****")
            print("\n[=] O fóton foi absorvido pelo átomo!!!")
            print("[=] Número quântico final do átomo:", f'{n:.2f}')


    elif(entrada == 'S' or entrada == 's'):
        print("[*] O programa foi encerrado !!!")
        print("""
            ___     _  _                     ___     _  _          
            | _ )   | || |   ___      o O O  | _ )   | || |   ___   
            | _ \    \_, |  / -_)    o       | _ \    \_, |  / -_)  
            |___/   _|__/   \___|   TS__[O]  |___/   _|__/   \___|  
            _|""""""|_| """"|_|"""""| {======|_|""""""|_| """"|_|"""""| 
            "`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'\n""")
        break

    else:
        print("\n[*] ATENÇÃO [*] Insira uma opção válida!!! ")
#***** FIM *****#
