'''Peça para o usuário digitar uma velocidade inicial (em m/s), 
uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo. 
Dica: use a fórmula matemática: yt = y0 + v0t + (1/2)gt^2 Onde, g é a aceleração da gravidade (-10m/s²), 
y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.'''



velocidade_inic = float(input("Digite a velocidade inicial: "))
posicao_inic = float(input("Digite a posição inicial: "))
tempo = float(input("Digite o instante de tempo: "))
gravidade = -10

yt = posicao_inic + (velocidade_inic *tempo) + (0.5 * gravidade) * (tempo ** 2)
print(32 *"=" )
print(f"A posição do projetil é {yt}")
