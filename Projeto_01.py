import time
import colorama
from colorama import Fore, Back
# Definindo Constantes
colorama.init()
c = 3e8
pi = 3.14159265358979323846

# TIPO DE ONDA - FREQUENCIA
def onda(compf):
    valor_onda = ""
    if(compf < 3e-11):
        valor_onda = "Raio Gama"
    elif(compf >= 3e-11 and compf <= 3e-08):
        valor_onda = "Raio-X"
    elif(compf > 3e-08 and compf <= 4e-07):
        valor_onda = "Ultravioleta"
    elif(compf > 4e-07 and compf <= 7e-07):
        valor_onda = "Luz Visível"
    elif(compf > 7e-07 and compf <= 1e-03):
        valor_onda = "Infravermelho"
    elif(compf > 1e-03 and compf <= 3e-01):
        valor_onda = "Microondas"
    elif(compf > 3e-01):
        valor_onda = "Rádio"
    return valor_onda

# UNIDADE DA FREQUENCIA
def unidade(compf,valor_onda):
    uni_compf = 0
    unidade = " "
    if(valor_onda == "Rádio"):
        uni_compf = compf
        unidade = "m"
    elif(valor_onda == "Microondas"):
        uni_compf = compf * 1000
        unidade = "mm"
    elif(valor_onda == "Infravermelho"):
        uni_compf = compf * 1e+06
        unidade = "um"
    else:
        uni_compf = compf * 1e+09
        unidade = "nm"
    return uni_compf,unidade

def Calc_frequencia(freq):
    compf = c / freq
    k = 2 * pi / compf
    w = 2 * pi * freq

    valor_onda = onda(compf)

    valor_unidade = unidade(compf,valor_onda)

    print("\n============= RESULTADOS ================")
    print("Comprimento da onda: %.2f %s" % (valor_unidade))
    print(f"Sua Frequência é de: {freq:0.2e} Hz")
    print(f"Seu K é: {k:0.2e} rad/m")
    print(f"Seu W é: {w:0.2e} rad/s")
    print("Tipo de onda: %s" % valor_onda)
    print("\n=========================================") 
    time.sleep(1)

# UNIDADE DO COMPRIMENTO 
def Valor_unidade_comp():   
    while True:
        print("=== Unidades ===")
        print("[1] - Nânometro")
        print("[2] - Micrometro")
        print("[3] - Milimetro")
        print("[4] - Metro")
        print("[5] - Kilômetro")
        print("[0] - Sair")
        op2 = int(input("[+] Digite a opção da unidade desejada: "))
        if op2 >= 1 or op2 <= 5:
            if op2 == 1:
                comp = float(input("[+] Digite o valor do Comprimento da onda: "))
                unidade = "Nanômetros(nm)"
                comp /= 1e+09
                Calc_comprimento(comp, unidade)
                break
            elif op2 == 2:
                comp = float(input("[+] Digite o valor do Comprimento da onda: "))
                unidade = "Micrômetros(um)"
                comp /= 1e+06
                Calc_comprimento(comp,unidade)
                break
            elif op2 == 3:
                comp = float(input("[+] Digite o valor do Comprimento da onda: "))
                unidade = "Milímetro(mm)"
                comp /= 1000
                Calc_comprimento(comp,unidade)
                break
            elif op2 == 4:
                comp = float(input("[+] Digite o valor do Comprimento da onda: "))
                unidade = "Metros(m)"
                Calc_comprimento(comp,unidade)
                break
            elif op2 == 5:
                unidade = "Kilômetros(Km)"
                comp = comp * 1000
                Calc_comprimento(comp,unidade)
                break
            elif op2 == 0:
                print("Saindo...")
                time.sleep(1)
                break
        else:
            print("\n=== Opção inválida! Digite novamente os dados! ===")
            continue
            
# TIPO DE ONDA - COMPRIMENTO     
def Onda_comp(f):
    tipo_onda1 = ""
    if(f < 1e+09):
        tipo_onda1 = "Rádio"

    elif(f >= 1e+09 and f <= 3e+11):
        tipo_onda1 = "Microondas"

    elif(f > 3e+11 and f <= 4.29e+14):
        tipo_onda1 = "Infravermelho"

    elif(f > 4.29e+14 and f <= 7.5e+14):
        tipo_onda1 = "Luz visível"

    elif(f > 7.5e+14 and f <= 1e+16):
        tipo_onda1 = "Ultravioleta"

    elif(f > 1e+16 and f <= 1e+19):
        tipo_onda1 = "Raio-X"

    elif(f > 1e+19):
        tipo_onda1 = "Raio Gama"
    return tipo_onda1

# CALCULAR O COMPRIMENTO
def Calc_comprimento(comp, unidade):
    # Fórmulas do Comprimento:
    f = c / comp
    k = 2 * pi / comp
    t = 1 / f
    w = 2 * pi / t
    tipo_onda = Onda_comp(f)

    print("\n============= RESULTADOS ================")
    print("Tipo de onda: %s" % tipo_onda)
    print(f"Com seu comprimento de: {comp} {unidade}")
    print(f"Sua frequência é: {f:0.2e}")
    print(f"Seu k é: {k:0.2e} rad/m")
    print(f"Seu w é: {w:0.2e} rad/s")    
    print("\n=========================================")
    time.sleep(1)

# Calcular o campo magnético
def Calula_magnetico():
    Emax = float(input("Digite o campo elétrico máximo: "))
    Bmax = Emax / c
    print("\n============= RESULTADOS ================")
    print(f"Valor do campo magnético: {Bmax:.2e} T")
    print("\n=========================================")
    time.sleep(1)

# Calcular o Campo Elétrico
def Calcula_eletrico():
    Bmax = float(input("Digite o campo magnético máximo: "))
    Emax = c * Bmax
    print("\n============= RESULTADOS ================")
    print(f"Valor do campo elétrico: {Emax:.2e} V/m")
    print("===========================================")
    time.sleep(1)

# Calcular número de onda
def Calcula_num_onda(n_onda):
    compk = 2 * pi / n_onda
    freq = c / compk
    w = 2 * pi * freq
    
    #valor_onda = onda(compk)
    print("\n============= RESULTADOS ================")
    print("Tipo de onda: ", onda(compk))
    print(f"Sua Frequência é de: {freq:0.2e} Hz")
    print(f"Seu Comprimento é de: {compk:0.2e} m")
    print(f"Seu K é: {n_onda:0.2e} rad/m")
    print(f"Seu W é: {w:0.2e} rad/s")
    print("\n=========================================")
    time.sleep(1)

def frequencia_angular(w):
    freq = w / (2 * pi)
    compw = c / freq
    k = (2 * pi) / compw
    comp2 = compw

    print("\n============= RESULTADOS ================")
    print("Tipo de onda: ", Onda_comp(freq))
    print(f"Sua frequência é de: {freq:0.2e} Hz")
    print(f"Seu Comprimento é de: {compw:0.2e} m")
    print(f"Seu K é: {k:0.2e} rad/m")
    print(f"Seu W é: {w:0.2e} rad/s")    
    print("\n=========================================")
    time.sleep(1)

def menu():
    while True:
        # Interação com o usuário:
        print(Fore.BLUE)
        print("++++++++++++++++++++++++++++++++++++++\n======================================\n[+] Escolha uma das opções:\n [c] - Entrar com comprimento de onda\n [f] - Entrar com frequência\n [w] - Entrar com frequência angular\n [k] - Entrar com número de onda\n [em] - Entrar com o campo elétrico \n [cm] - Entrar com o campo magnético \n [s] - Sair \n======================================")
        print(Fore.RESET)
        op = input(">> ")

        if op == "f" or op == "F":
            freq = float(input("Digite o valor da Frequência da onda: "))
            Calc_frequencia(freq)

        elif op == 'c' or op == 'C':
            Valor_unidade_comp()

        elif op == "CM" or op == "cm":
            Calula_magnetico()

        elif op == "EM" or op == "em":
            Calcula_eletrico()

        elif op == "k" or op == "K":
            n_onda = float(input("Insira o número de onda desejado (rad/m): "))
            Calcula_num_onda(n_onda)

        elif op == 'w' or op == 'W':
            w = float(input("Insira a Frequência Angular (rad/s): "))
            frequencia_angular(w)
            
        elif op == 's' or op == 'S':
            print("Encerrando...")
            time.sleep(1)
            break
        
print(Fore.RED)   
print("*******************************************************")
print("***    .-``'.     Calculadora de Ondas   .'''-.     ***")
print("***  .`   .`~       Eletromagnéticas     ~`.   '.   ***")
print("**.-'     '.            CF3121           _.'     '-.***")
print("*******************************************************")
print(Fore.RESET)
menu()
