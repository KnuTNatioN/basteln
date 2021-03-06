#!/usr/bin/python3

from gpiozero import Servo
from time import sleep
import sys

serA = Servo("BOARD33")
serB = Servo("BOARD12")

position = float(-1)
vecc = True


def argv_handel():
    dict = {
        '' : helper,
        '-b' : beckon,
        '--beckon' : beckon,
        '-m' : manual,
        '--manual' : manual,
        '-s' : steps,
        '--steps' : steps,
        '-h' : helper,
        '--help' : helper,
    }
    
    dict.get(sys.argv[1], helper)()
    

def initial():#start
    global position
    serA.value = position
    serB.value = position


def loop():
    global position
    serA.value = position
    serB.value = position
    
    sleep(0.3)

    serA.detach()
    serB.detach()
    #print("detach")
    argv_handel()


def manual():
    global position
    print("Position: ", position*100, "%")
    position = (float(input("input between 1..&..100 : ")) / 50 - 1)
    if position > 0.999:
        position = 1
    elif position < -0.999:
        position = -1


def beckon():#dictionary: He beckoned to me, as if he wanted to speak to me.
    global position
    if position > 0.999:
        position = 1
    elif position < -0.999:
        position = -1


def steps():
    global position
    global vecc
    position = round(position, 3)
    sleep(0.01)
    position = round(position, 3)
    if position < -0.999:
        vecc = True
        sleep(1)
        print('back')
        sleep(1)
    elif position > 0.999:
        vecc = False
        sleep(1)
        print('forward')
        sleep(1)
    if vecc == True:
        position = position + 0.1
    else:
        position = position - 0.1
    print(position)


def last():
    serA.close()
    serB.close()
    print("\nProgram ended")


class hell_per(Exception):
    pass


def helper():
    print('usage: servo.py [options]')
    print('-b, --beckon         hard -100% then 100% (beckon means waving)')
    print('-m, --manual         give value between 0=-100% and 100=+100%')
    print('-s, --steps          maken 10% steps between -100% and 100%')
    print('-h,                  ...display this help ')
    #break
    raise hell_per('ok')


def main():
    initial()
    #if len(sys.argv) < 2:
    #    helper()
    #else:
    while True:
        try:
            loop()
        except hell_per:
            break
        except KeyboardInterrupt:
            print("\nStrg+C = STOP PROGRAM")
            break
    last()


main()