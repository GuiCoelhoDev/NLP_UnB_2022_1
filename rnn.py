import math
import numpy

def main():
    atributos = [0.5,1.1,0.1,0.2,0.7]

    # qtd pesos = qtd atributos
    pesos = numpy.random.randn(5)
    # pesos = [-1,-1,-1,-4,-2]
    bias = 0
    net = bias
    for atributo, peso in zip(atributos,pesos):
        net += atributo*peso

    y = funcAtivacao(net, 'sinoidal',0)
    print(y)

    learn_and()



def learn_and():
    pesos = numpy.random.randn(5)
    X = [[0,0], [0,1], [1,0], [1,1]]
    labels = [0,0,0,1]
    bias = 0
    net = bias
    for atributo, peso in zip(X,pesos):
        # for a in atributo:

        net += atributo*peso

        y = funcAtivacao(net,'degrau',0.5)

        print(f'[{atributo[0]},{atributo[1]}] Output perceptron: {y} Label: {labels[j]}')


    # for x in X:
    #     for i in range(0,d):
    #         net += x[i]*pesos[i]
    #         y = funcAtivacao()
    #         print

def funcAtivacao(x, tipo,t):
    if tipo == 'degrau':
        if x >= t:
            y = 1
        else:
            y = 0
    elif tipo == 'sinal':
        if x >= 0:
            y = 1
        else:
            y = -1
    elif tipo == 'sinoidal':
        y = 1/(1+math.exp(-x))
    else:
        y = 'Tipo inválido'
    print("\n")
    return y

if __name__ == "__main__":
    main()