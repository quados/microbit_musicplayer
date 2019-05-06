# Add your Python code here. E.g.
from microbit import *
import music

def displayLEDpos(ledPos):
    s = '0000000000000000000000000'
    s = s[:ledPos] + "9" + s[ledPos+1:]
    s = s[:5] + ":" + s[5:10] + ":" + s[10:15] + ":" + s[15:20] + ":" + s[20:]  
    display.show(Image(s))
    
def playRequiem():
    display.show("R")
    sleep(1000)
    
    music.set_tempo(bpm=150)

    requiem_0 = ['A#6', 'A6', 'G6', 'D6']
    requiem_1 = ['C7', 'A#6', 'A6', 'A#6']
    requiem_2 = ['A#6', 'A6', 'G6', 'D6']
    requiem_3 = ['C7', 'A#6', 'A6', 'G6']
    requiem_4 = ['A#5', 'G5']
    requiem_5 = ['A#5', 'G5', 'A#5', 'G5:2']
    requiem_6 = ['A#5', 'G5', 'A#5', 'G5:2']
    requiem_7 = ['A#5', 'G5']
    requiem_8 = ['A#5']
    requiem_9 = ['A#5', 'A5', 'A#5', 'A5:2']
    requiem_10 = ['A#5', 'A5', 'A#5', 'A5:2']
    requiem_11 = ['A#5', 'A5']
    requiem_12 = ['A#6:2', 'A#5:2']
    requiem_13 = ['G6:2', 'G5:2']
    requiem_14 = ['A#6','A#5','G6','G5','A#6','A#5', 'G6', 'G5']
    requiem_15 = ['A#6','A#5','G6','G5','A#6','A#5', 'A6', 'A5']

    displayLEDpos(0)
    for x in range(0, 3):
        music.play(requiem_0)
        
    displayLEDpos(1)   
    music.play(requiem_1)        
    
    displayLEDpos(2)
    for x in range(0, 3):
        music.play(requiem_2)

    displayLEDpos(3) 
    music.play(requiem_3)
    
    displayLEDpos(4)
    for x in range(0, 3):
        music.play(requiem_2)

    displayLEDpos(5)
    music.play(requiem_1)
    
    displayLEDpos(6)
    for x in range(0, 3):
        music.play(requiem_2)

    displayLEDpos(7)
    music.play(requiem_1)

    displayLEDpos(8)
    music.play(requiem_4)

    displayLEDpos(9)
    music.play(requiem_5)
    
    displayLEDpos(10)
    music.play(requiem_6)
    
    displayLEDpos(11)
    music.play(requiem_7)
    
    displayLEDpos(12)
    music.play('D5')
    
    displayLEDpos(13)
    for x in range(0, 4):
        music.play(requiem_7)

    displayLEDpos(14)    
    music.play(requiem_8)

    displayLEDpos(15)
    music.play('A5:2')

    displayLEDpos(16)
    music.play(requiem_9)

    displayLEDpos(17)    
    music.play(requiem_10)

    displayLEDpos(18)
    music.play(requiem_11)
    
    displayLEDpos(19)
    music.play(requiem_8)

    displayLEDpos(20)
    music.play('A5')
    
    displayLEDpos(21)
    for x in range(0, 3):
        music.play(requiem_11)
    
    displayLEDpos(22)
    music.play(requiem_12)

    displayLEDpos(23)
    music.play(requiem_13)

    displayLEDpos(24)
    music.play(requiem_14)

    displayLEDpos(0)
    music.play(requiem_13)

    displayLEDpos(1)
    music.play(requiem_14)

    displayLEDpos(2)
    music.play(requiem_13)
    
    displayLEDpos(3)
    for x in range(0, 2):
        music.play(requiem_14)

    displayLEDpos(4)
    music.play(requiem_15)    

def musicSelect(num):
    if (num == 0):
        playRequiem() 
    if (num == 1):
        display.show("A")
    if (num == 2):
        display.show("B")
    if (num == 3):
        display.show("C")
    if (num == 4):
        display.show("D")
    if (num == 5):
        display.show("E")   


display.show(0)
while True:
    count = 0  
    while True:
        if button_a.was_pressed():
            count += 1
            if(count == 10):
                count = 0
                button_a.get_presses()
            display.show(count)

            
        if button_b.was_pressed():
            musicSelect(button_a.get_presses())
            break
        