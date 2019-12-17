# funcoes
def menu():
    print('+----------------------+')
    print('| CALCULADORA          |')
    print('+----------------------+')
    print('| 0 - Sair             |')
    print('| 1 - Soma             |')
    print('| 2 - Subração         |')
    print('| 3 - Multiplicação    |')
    print('| 4 - Divisão          |')
    print('| 5 - Potenciação      |')
    print('| 6 - Mudança de base  |')
    print('+----------------------+')
    select = int(input("Selecione uma operação:\n"))
    print('')
    return select


def titulo(msg):
    print('+----------------------+')
    print('|', msg, '|')
    print('+----------------------+')


def soma(a, b):
    res = a + b
    return res


def subtrai(a, b):
    res = a - b
    return res


def multiplica(a, b):

    cont = 0

    # algum número ou ambos sendo zero
    if (a == 0 and b == 0) or (a == 0 or b == 0):
        cont = 0

    # todos os números positivos
    if a > 0 and b > 0:

        cont = 0
        res = 0

        # primeiro número maior que segundo
        if a > b:
            while cont < a:
                cont += 1
                res += b
            cont = res

        # segundo número maior que o primeiro
        if b > a:
            while cont < b:
                cont += 1
                res += a
            cont = res

        # números iguais
        if a == b:
            while cont < a:
                cont += 1
                b += a
            cont = b - a

    # primeiro ou segundo número negativo
    if a < 0 or b < 0:
        cont = 0
        res = 0

        # os dois números negativos
        if a < 0 and b < 0:

            # inverte o sinal da variável a
            aux = a
            i = 0

            while i < 2:
                i += 1
                aux = subtrai(aux, a)
            a = aux

            # inverte o sinal da variável b
            aux = b
            i = 0

            while i < 2:
                aux = subtrai(aux, b)
            b = aux

            # iguais
            if a == b:
                while cont < a:
                    cont += 1
                    res += a
                cont = res

            # diferentes
            if a != b:
                while cont < a:
                    cont += 1
                    res += b
                cont = res

        # primeiro número negativo
        if a < 0 < b:

            # inverte o sinal da variável a
            aux = a
            i = 0

            while i < 2:
                i += 1
                aux = subtrai(aux, a)
            a = aux

            while cont < a:
                cont += 1
                res += b
            cont = -res

        # segundo número negativo
        if a > 0 > b:

            # inverte o sinal da variável a
            aux = b
            i = 0

            while i < 2:
                i += 1
                aux = subtrai(aux, b)
            b = aux

            while cont < a:
                cont += 1
                res += b
            cont = -res

    return cont


def divide(n, d):
    q = 0
    resp = 0

    # denominador sendo zero
    if d == 0:
        while d == 0:
            d = int(input('Divisão por zero não permitida. Tente com outro número:\n'))

    # numerador sendo zero
    if n == 0:
        rest = n
        resp = (q, rest)

    # ambos positivos
    if n > 0 and d > 0:

        # numerador maior que denominador
        if n > d:
            while n >= d:
                n = subtrai(n, d)
                q += 1
            rest = n
            resp = (q, rest)

        # numerador menor que denominador
        if n < d:
            rest = n
            resp = (q, rest)

        # numerador e denominador iguais
        if n == d:
            rest = q
            q = 1
            resp = (q, rest)

    # algum ou todos os números negativo
    if (n < 0 or d < 0) or (n < 0 and d < 0):

        # ambos negativos
        if n < 0 and d < 0:

            # inverte o sinal do numerador
            aux = n
            i = 2

            while i > 0:
                aux = subtrai(aux, n)
                i -= 1
            n = aux

            # inverte o sinal do denominador
            aux = d
            i = 2

            while i > 0:
                aux = subtrai(aux, d)
                i -= 1
            d = aux

            # iguais
            if n == d:
                rest = q
                q = 1
                resp = (q, rest)

            # diferentes
            if n != d:

                # numerador menor que denominador
                if n < d:
                    rest = n
                    resp = (q, -rest)

                # numerador maior que denominador
                if n > d:
                    while n >= d:
                        n = subtrai(n, d)
                        q += 1
                    rest = n
                    resp = (q, -rest)

        # algum dos números negativos
        if n < 0 or d < 0:

            # numerador negativo
            if n < 0:

                # inverte o sinal do numerador
                aux = n
                i = 2

                while i > 0:
                    aux = subtrai(aux, n)
                    i -= 1
                n = aux

                # numerador menor que denominador
                if n < d:
                    rest = n
                    resp = (q, -rest)

                # numerador maior que denominador
                if n > d:
                    while n >= d:
                        n = subtrai(n, d)
                        q -= 1
                    rest = n
                    resp = (q, -rest)

                # iguais
                if n == d:
                    rest = q
                    q = -1
                    resp = (q, rest)

            # denominador negativo
            if d < 0:

                # inverte o sinal do denominador
                aux = d
                i = 2

                while i > 0:
                    aux = subtrai(aux, d)
                    i -= 1
                d = aux

                # numerador menor que denominador
                if n < d:
                    rest = n
                    resp = (q, rest)

                # numerador maior que denominador
                if n > d:
                    while n >= d:
                        n = subtrai(n, d)
                        q -= 1
                    rest = n
                    resp = (q, rest)

                # iguais
                if n == d:
                    rest = q
                    q = -1
                    resp = (q, rest)

    return resp


def potencia(b, e):

    aux = b
    conf = e

    # expoente negativo
    if e < 0:

        # inverte o sinal do expoente
        aux1 = e
        i = 2

        while i > 0:
            i -= 1
            aux1 = subtrai(aux1, e)
        e = aux1

    # expoente zero
    if e == 0:
        aux = 1

    # expoente positivo
    if e > 0:
        while e > 1:
            e -= 1
            aux = multiplica(aux, b)

    # converte para fração caso o expoente tenha sido negativo
    if conf < 0:
        aux = f'1/{aux}'

    return aux


def base(n, bo, bf):
    # dicionário
    dic = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21,
           'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33,
           'y': 34, 'z': 35}
    dic1 = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l',
            22: 'm', 23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x',
            34: 'y', 35: 'z'}

    resultado = None

    # conversão de letra pra número
    def converte(n):

        cont = len(n) - 1
        i = cont
        l = []
        div = []
        i_d = 35
        n.lower()
        aux = 0

        # verifica se contém letra na string e a substitui pelo valor equivalente
        while i_d >= 0:
            while i >= 0:

                aux = n[i]

                if aux in dic:
                    aux = dic[aux]

                l.append(aux)
                i -= 1

            i_d -= 1
            aux = 0

        return l

    # conversão de número pra letra
    def desconverte(n):

        cont = len(n) - 1
        i = cont
        l = []
        div = []
        i_d = 35
        aux = 0

        # verifica se contém número na string e a substitui pelo valor equivalente
        while i_d >= 0:
            while i >= 0:

                aux = n[i]

                if aux in dic1:
                    aux = dic1[aux]

                l.append(aux)
                i -= 1

            i_d -= 1
            aux = 0

        return l

    # de qualquer base para base 10
    def p10(n, bo):

        l = converte(n)
        i = len(l) - 1
        soma = 0

        while i >= 0:
            aux = l[i]
            aux = int(aux)
            pot = potencia(bo, i)
            res = multiplica(aux, pot)
            soma += res
            i -= 1

        return soma

    # da base 10 pra qualquer base
    def d10(n, bf):
        n = int(n)
        quo, res = divide(n, bf)
        div = [res]
        # enquanto o quociente não for 0 a divisão será feita sempre pelo resto
        while quo != 0:
            quo, res = divide(quo, bf)
            div.append(res)

        div = desconverte(div)
        div.reverse()

        resu = ''

        i = len(div) - 1

        while i >= 0:
            axu = div[i]
            axu = str(axu)
            resu += axu
            i -= 1
        result = resu

        return result

    # chama o método de qualquer base para 10 caso a bf seja 10
    if bf == 10:
        resultado = p10(n, bo)

    if bo == 10:
        resultado = d10(n, bf)

    if bf != 10 and bo != 10:
        res = p10(n, bo)
        resultado = d10(res, bf)

    return resultado


# principal
opcao = menu()

while opcao != 0:

    if opcao < 0:
        titulo('OPÇÃO INVÁLIDA      ')
        opcao = menu()

    if opcao == 1:
        titulo('SOMA                ')
        n1 = int(input('Primeiro número:\n'))
        n2 = int(input('Segundo número:\n'))
        print(f'O resultado é: {str(soma(n1, n2))}\n')
        opcao = menu()

    if opcao == 2:
        titulo('SUBTRAÇÃO           ')
        n1 = int(input('Primeiro número:\n'))
        n2 = int(input('Segundo número:\n'))
        print(f'O resultado é: {str(subtrai(n1, n2))}\n')
        opcao = menu()

    if opcao == 3:
        titulo('MULTIPLICAÇÃO       ')
        n1 = int(input('Primeiro número:\n'))
        n2 = int(input('Segundo número:\n'))
        print(f'O resultado é: {str(multiplica(n1, n2))}\n')
        opcao = menu()

    if opcao == 4:
        titulo('DIVISÃO             ')
        n1 = int(input('Numerador:\n'))
        n2 = int(input('Denominador:\n'))
        quo, res = divide(n1, n2)
        print(f'O resultado é: {str(quo)} com resto: {str(res)}\n')
        opcao = menu()

    if opcao == 5:
        titulo('POTENCIAÇÃO         ')
        n1 = int(input('Base:\n'))
        n2 = int(input('Expoente:\n'))
        print('O resultado é:', str(potencia(n1, n2)), '\n')
        opcao = menu()

    if opcao == 6:
        titulo('MUDANÇA DE BASE     ')
        n1 = input('Número:\n')
        n1 = str(n1)
        n2 = int(input('Base original:\n'))
        n3 = int(input('Base final:\n'))
        print('O resultado é', base(n1, n2, n3), '\n')
        opcao = menu()

    if opcao > 6:
        titulo('OPÇÃO INVÁLIDA      ')
        opcao = menu()

exit()
