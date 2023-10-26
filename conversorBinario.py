BINARIO = []
texto = str(input("Digite um texto:"))
ListaTexto = list(texto)

def Conversor(texto):
    
    for i in ListaTexto:
        
        if i == "A":
            BINARIO.append("01000001")
        elif i == "À":
            BINARIO.append("11000000")
        elif i == "Á":
            BINARIO.append("11000001")
        elif i == "Â":
            BINARIO.append("11000010")
        elif i == "Ã":
            BINARIO.append("11000011")
        elif i == "B":
            BINARIO.append("01000010")
        elif i == "C":
            BINARIO.append("01000011")
        elif i == "Ç":
            BINARIO.append("11000111")
        elif i == "D":            
            BINARIO.append("01000100")
        elif i == "E":
            BINARIO.append("01000101")
        elif i == "É":
            BINARIO.append("11001001")
        elif i == "Ê":
            BINARIO.append("11001010")
        elif i == "F":
            BINARIO.append("01000110")
        elif i == "G":
            BINARIO.append("01000111")
        elif i == "H":
            BINARIO.append("01001000")
        elif i == "I":
            BINARIO.append("01001001")
        elif i == "Í":
            BINARIO.append("11001101")
        elif i == "J":
            BINARIO.append("01001010")
        elif i == "K":
            BINARIO.append("01001011")
        elif i == "L":
            BINARIO.append("01001100")
        elif i == "M":
            BINARIO.append("01001101")
        elif i == "N":
            BINARIO.append("01001110")
        elif i == "O":
            BINARIO.append("01001111")
        elif i == "Ó":
            BINARIO.append("11010011")
        elif i == "Ô":
            BINARIO.append("11010100")
        elif i == "Õ":
            BINARIO.append("11010101")
        elif i == "P":
            BINARIO.append("01010000")
        elif i == "Q":
            BINARIO.append("01010001")
        elif i == "R":
            BINARIO.append("01010010")
        elif i == "S":
            BINARIO.append("01010011")
        elif i == "T":
            BINARIO.append("01010100")
        elif i == "U":
            BINARIO.append("01010101")
        elif i == "Ú":
            BINARIO.append("11011010")
        elif i == "V":
            BINARIO.append("01010110")
        elif i == "W":
            BINARIO.append("01010111")
        elif i == "X":
            BINARIO.append("01011000")
        elif i == "Y":
            BINARIO.append("01011001")
        elif i == "Z":
            BINARIO.append("01011010")
        elif i =="a":
            BINARIO.append("01100001")
        elif i =="à":
            BINARIO.append("11100000")
        elif i =="á":
            BINARIO.append("11100001")
        elif i =="â":
            BINARIO.append("11100010")
        elif i =="ã":
            BINARIO.append("11100011")
        elif i =="b":
            BINARIO.append("01100010")
        elif i =="c":
            BINARIO.append("01100011")
        elif i =="ç":
            BINARIO.append("11100111")
        elif i =="d":
            BINARIO.append("01100100")
        elif i =="e":
            BINARIO.append("01100101")
        elif i =="é":
            BINARIO.append("11111011")
        elif i =="ê":
            BINARIO.append("11111100")
        elif i =="f":
            BINARIO.append("01100110")
        elif i =="g":
            BINARIO.append("01100111")
        elif i =="h":
            BINARIO.append("01101000")
        elif i =="i":
            BINARIO.append("01101001")
        elif i =="í":
            BINARIO.append("11101101")
        elif i =="j":
            BINARIO.append("01101010")
        elif i =="k":
            BINARIO.append("01101011")
        elif i =="l":
            BINARIO.append("01101100")
        elif i =="m":
            BINARIO.append("01101101")
        elif i =="n":
            BINARIO.append("01101110")
        elif i =="o":
            BINARIO.append("01101111")
        elif i =="ó":
            BINARIO.append("11110011")
        elif i =="ô":
            BINARIO.append("11110100")
        elif i =="õ":
            BINARIO.append("11110101")
        elif i =="p":
            BINARIO.append("01110000")
        elif i =="q":
            BINARIO.append("01110001")
        elif i =="r":
            BINARIO.append("01110010")
        elif i =="s":
            BINARIO.append("01110011")
        elif i =="t":
            BINARIO.append("01110100")
        elif i =="u":
            BINARIO.append("01110101")
        elif i =="ú":
            BINARIO.append("11111010")
        elif i =="v":
            BINARIO.append("01110110")
        elif i =="w":
            BINARIO.append("01110111")
        elif i =="x":
            BINARIO.append("01111000")
        elif i =="y":
            BINARIO.append("01111001")
        elif i =="z":
            BINARIO.append("01111010")

Conversor(ListaTexto)
final =" ".join(BINARIO)
print(final)
print(texto)
print(len(texto))
print(len(ListaTexto))

    
    