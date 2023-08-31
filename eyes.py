#!/usr/bin/env python3

import random
import time
import threading

all_faces = ["^ ^", "<.<", "o.o", "O.O", ">.>", "*.*", "~.~", "-.-'"]#, "e.e", "q.q", "p.p", "P.P", "Q.Q", "d.d", "b.b"

def mkFace():
    global all_faces
    return random.choice(all_faces)

def random_blink():
    close1 = "-.-"
    close2 = "_._"
    blink_duration = 2  # 100 Millisekunden
    open_duration = 9   # 9000 Millisekunden


    def input_thread():
        global reRunFlag
        try:
            while not exit_flag.is_set():
                user_input = input("")
                # Hier kannst du die Eingabe verarbeiten, wie du möchtest
                if user_input == "?":#help
                    print("'?' = diese Hilfe, 'q|Q|0|e' = Beenden, 'Strg+C' = Abbrechen")
                if user_input.endswith("q") or user_input.endswith("0") or user_input.endswith("Q") or user_input.endswith("E"): #quit with input
                    exit_flag.set()
                    print("Beendet durch Eingabe")
                    break
                else:
                    continue
        except KeyboardInterrupt:
            print("\n Thread abgebrochen \n")
            return
        except Exception as ex:
            print(f"Ein Fehler ist aufgetreten: {ex}")
            return

    # Starte den Eingabe-Thread parallel zum Blink-Thread
    exit_flag = threading.Event()
    input_thread_instance = threading.Thread(target=input_thread)
    input_thread_instance.start()

    try:
        while True:
            face = mkFace()
            print(f"  {face}                                ", end="\r")

            time.sleep(blink_duration / 40)#blink start
            print(f"  {close1}                                ", end="\r")
            time.sleep(blink_duration / 40)
            print(f"  {close2}                                ", end="\r")
            time.sleep(blink_duration / 40)
            print(f"  {close1}                                ", end="\r")
            time.sleep(blink_duration / 40)

            print(f"  {face}                                ", end="\r")

            open_time = open_duration
            while(open_time > 0):
                rand_time = random.randrange(0 , open_duration) / 10 #zufällige blickzeit in eine Richtung
                open_time = open_time - (rand_time)#randtime abziehen
                time.sleep(rand_time)

                face = mkFace()
                print(f"  {face}                                ", end="\r")

                if exit_flag.is_set():
                    if input_thread_instance.is_alive():
                        print("Programm Beenden?")
                        input_thread_instance.join()
                    return

    except KeyboardInterrupt:
        print("\n Augen abgebrochen\n")
        exit_flag.set()# Setze das Exit-Flag, um den Thread zu beenden
        print("Programm Beenden? (Thread wartet noch auf Eingabe)")
        if input_thread_instance.is_alive():
            input_thread_instance.join()
        return

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        exit_flag.set()# Setze das Exit-Flag, um den Thread zu beenden
        
        if input_thread_instance.is_alive():
            print("Programm wird nach einer Eingabe beendet.")
            input_thread_instance.join()
        return


# Starte die Funktion
random_blink()
