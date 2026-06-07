temperatura = float(input("Digite a temperatura da nave: "))
energia = float(input("Digite o nível de energia (%): "))
painel_solar = float(input("Digite o nível de geração solar (%): "))

comunicacao = input("Status da comunicação (ok/falha): ").strip().lower()

if comunicacao == "falha":
    print("Alerta: Comunicação perdida")
    print("Tentando reconectar comunicação")
else:
    print("Comunicação funcionando normalmente")

print("MISSÃO ESPACIAL:")
print(f"Temperatura: {temperatura}°C")
print(f"Energia: {energia}%")
print(f"Comunicação: {comunicacao}")
print(f"Painel Solar: {painel_solar}%")

if temperatura > 100:
    print("ALERTA: Temperatura crítica")
if energia < 15:
    print("ALERTA: Energia baixa")
if painel_solar < 20:
    print("ALERTA: Baixa geração solar")


if energia < 15:
    print("Modo economia ativado")
if temperatura > 100:
    print("Sistema de resfriamento ativado")

modulo_energia = input("Módulo de energia (ok/falha): ").strip().lower()
modulo_comunicacao = input("Módulo de comunicação (ok/falha): ").strip().lower()
modulo_navegacao = input("Módulo de navegação (ok/falha): ").strip().lower()

if modulo_navegacao == "falha":
    print("Falha no módulo de navegação")

if modulo_comunicacao == "falha":
    print("Falha no módulo de comunicação")

if modulo_energia == "falha":
    print("Falha no módulo de energia")
