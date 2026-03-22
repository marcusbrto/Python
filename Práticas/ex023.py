"""
CONSTANTE = "Variáveis" que não vão mudar Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
# se a variavel nao for mudar de valor escrever em maiusculo para o outro desenvolvedor que ver entender que aquilo é uma variavel que nao é para ser alterada
# Evite usar muitos condicoes no mesmo if porque fica muito complexo de entender, escreva mais inteligente para criar um codigo mais limpo

rapidez = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro esta na estrada

RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 esta
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_pass_radar_1 = rapidez > RADAR_1
carro_multado_radar_1 = local_carro >= (LOCAL_1 - RADAR_1) and local_carro <= (LOCAL_1 + RADAR_1)

if vel_carro_pass_radar_1:
    print("Velocidade carro passou do radar 1")

if carro_multado_radar_1 and vel_carro_pass_radar_1:
    print("Carro multado em radar 1")
