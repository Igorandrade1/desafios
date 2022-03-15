
def vel_carro(velocidade):
    multa = 100
    print(f"Velocidade está acima de 50km, você recebeu uma multa de R${multa * 1.1:.2f}" if 50 < velocidade <= 60 else '')
    print(f"Velocidade está acima de 60km, você recebeu uma multa de R${((multa * 15) / 100) + multa:.2f}" if 60 < velocidade <= 70 else '')
    print(f"Velocidade está acima de 70km, você recebeu uma multa de R${multa * 1.2:.2f}" if velocidade > 70 else '')



vel_carro(51)
vel_carro(61)
vel_carro(71)



