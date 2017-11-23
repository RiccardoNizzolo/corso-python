from day3.esercizi.contest import Indovino


def indovina():
    oracolo= Indovino()
    stato, tentativi= oracolo.oracle(5)
    print(stato)



if __name__ == '__main__':
    indovina()
