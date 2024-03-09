"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;

"""

def inverter(string):
    string_invertida = ""
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    return string_invertida

string_original = input("Digite uma string para inverter: ")
string_invertida = inverter(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
