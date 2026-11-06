import time
import random
import sys

def print_slow(text, delay=0.02):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def visa_meny(epochs):
    print("\nVar vill du resa härnäst?")
    for k, v in epochs.items():
        print(f"[{k}] {v['namn']}")
    print(" [0] Avbryt och återvänd till nutiden")

def play_game():
    paradox = 0
    score = 0
    loot = []
    
    epochs = {
        1: {"namn": "Dinosauriernas era (-66 miljoner år)", "sak": "Ett T-Rex-ägg att göra omelett på", "paradox": 25},
        2: {"namn": "Antika Egypten (År 1323 f.Kr.)", "sak": "Tutankhamuns gyllene fidget spinner", "paradox": 15},
        3: {"namn": "Renässansen (År 1503)", "sak": "Mona Lisas hemliga mustasch-skiss", "paradox": 20},
        4: {"namn": "Framtiden (År 3026)", "sak": "Receptet på odödlig snabbmat", "paradox": 35}
    }
    
    print("=" * 60)
    print("      ⏳ KRONO-KLIPPET: DET STORA TIDSRÅNET ⏳")
    print("=" * 60)
    print_slow("Välkommen, Agent Paradox! Du har stulit en Kvant-Kofot.")
    print_slow("Ditt uppdrag: Res genom tiden och stjäl absurda historiska föremål.")
    print_slow("Men se upp! Varje sak du stjäl förändrar nutiden på oväntade sätt.")
    print_slow("Om din 'Tids-Paradox-Mätare' når 100%, raderas du ur existensen!")
    print("=" * 60)
    
    while paradox < 100 and len(epochs) > 0:
        print(f"\n📊 STATUS: Poäng: {score} | Paradox-nivå: {paradox}%")
        print(f"🎒 Ryggsäck: {', '.join(loot) if loot else 'Tom'}")
        print("-" * 40)
        
        visa_meny(epochs)
        
        val_input = input("\nDitt val: ").strip()
        
        if val_input == "0":
            print_slow("\n🏃‍♂️ Du fegade ur och hoppade snabbt tillbaka till nutiden!")
            break
            
        if not val_input.isdigit() or int(val_input) not in epochs:
            print("\n❌ Ogiltigt val! Välj en siffra från menyn.")
            continue
            
        val = int(val_input)
        current = epochs.pop(val)
        
        print_slow(f"\n🚀 Swisch! Du landar i: {current['namn']}...")
        time.sleep(0.5)
        print_slow(f"Försöker stjäla: {current['sak']}...")
        time.sleep(0.5)
        
        tidspolis_chans = random.randint(1, 3)
        if tidspolis_chans == 1:
            print_slow("\n🚨 LARMET GÅR! Tidspolisen dyker upp!")
            print("1. Kasta en banan på dem och spring.")
            print("2. Försök intala dem att du är deras korrupta chef från framtiden.")
            
            medvetet_val = False
            while not medvetet_val:
                action = input("Vad gör du? (1/2): ").strip()
                if action == "1":
                    print_slow("\n💥 De halkar på bananen! Du kommer undan, men kaoset ökar paradoxen.")
                    paradox += current['paradox'] + 15
                    score += 50
                    loot.append(current['sak'])
                    medvetet_val = True
                elif action == "2":
                    print_slow("\n😎 Det funkade! De saluterar nervöst.")
                    score += 150
                    loot.append(current['sak'])
                    medvetet_val = True
                else:
                    print("❌ Välj antingen 1 eller 2!")
        else:
            print_slow("\n✨ Snyggt! Stölden lyckades helt obemärkt.")
            paradox += current['paradox']
            score += 100
            loot.append(current['sak'])
            
    print("\n" + "=" * 60)
    if paradox >= 100:
        print("💥 PARADOX-KATASTROF! 💥")
        print_slow("Du ändrade historien för mycket. Du förvandlades precis till en talande tekanna år 1842.")
        print("SPEL SLUT (Game Over)")
    else:
        print("🎉 VÄLKOMMEN TILLBAKA TILL NUTIDEN! 🎉")
        print(f"Du överlevde tidshoppen! Din totala poäng: {score}")
        print("Du fick med dig följande skatter hem:")
        if loot:
            for item in loot:
                print(f" - {item}")
        else:
            print(" - Inga skatter (Du kom hem tomhänt!)")
        print("\nTack för att du spelade Krono-Klippet!")
    print("=" * 60)

if __name__ == '__main__':
    play_game()
