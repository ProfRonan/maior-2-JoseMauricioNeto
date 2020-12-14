"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    import math
    a=input('Digite um número:')
    a=float(a)
    b=input('Digite outro número:')
    b=float(b)
    numeros=[a,b]
    print(f'{max(numeros)}')

if __name__ == '__main__':
    main()
