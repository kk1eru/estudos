# aurora_burra.py

print("Aurora online.")

while True:
    comando = input("Diz algo pra Aurora: ").lower()

    if comando == "oi":
        print("Oi. Ainda sou burra.")
    
    elif comando == "hora":
        from datetime import datetime
        agora = datetime.now().strftime("%H:%M:%S")
        print("Agora são", agora)

    elif comando == "sair":
        print("Desligando a Aurora...")
        break

    else:
        print("Não entendi isso ainda.")
