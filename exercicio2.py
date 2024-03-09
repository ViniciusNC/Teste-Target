"""
  2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 
  2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
  escreva um programa na linguagem que desejar onde, informado um número, 
  ele calcule a sequência de Fibonacci e 
  retorne uma mensagem avisando se o número informado pertence ou não a sequência
"""
def fibonacci(num):
    num1, num2 = 0, 1
    while num2 < num:
        num1, num2 = num2, num1 + num2
    return num2 == num

def main():
    num = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    if fibonacci(num):
        print(f"{num} pertence à sequência de Fibonacci.")
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()

