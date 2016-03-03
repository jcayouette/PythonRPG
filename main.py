from random import randint
import time
import sys
import random
import shutil
import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.music.load("ambient.mp3")
pygame.mixer.music.play(-1, 0.0)

columns = shutil.get_terminal_size().columns
#  print("hello world".center(columns))


class Color:
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

# print(Color.bold + 'Hello World !' + Color.end) Example for coloring string blocks.

text = '''
777777777777777777777777777777777777777
77777777777777777777  77777777777777777
777777777777777777+..7  777777777777777
77777777777777777.:,,:: 777777777777777
77777777777777777:,::,,7777777777777777
77777777777777777::+?I, 777777777777777
777777777777777777,+?I? 777777777777777
777777777777777777~+,+7     77777777777
7777777777777777,,.~,??=7I+  7777777777
77777777777777:+,.I,,~=:?I,~ 7777777777
77777777777777~~I,,,:?7:,7~= 7777777777
77777777777777:~+::==I+,,:.+77777777777
7777777777777,,,+I+?I?+:,+::77777777777
7777777777777::,~+=?~=+:,=~,~7777777777
777777777777,:,,:+++~+:= ,+?=7777777777
777777777777~::,,::~:+:77=,?= 777777777
77777777777.~~?::=~+~=~I7?:=:7777777777
77777777777,.,,.:,,,,~,,7,,,~7777777777
77777777777::,+??,,,,.~~,7,,,7777777777
7777777777 :?..:+,+~,,,,,,,.77777777777
7777777777 ~,,,:,,,,,,.,,==:77777777777
77777777777I,.,,:~,:,,,:,~~ 77777777777
77777777777,=~,,::,?,,,+=:7777777777777
7777777777,,7=,.::,+:,:~~,7777777777777
7777777777,,7 ,,~:,,7:::~:=777777777777
777777777,:777~.~:,:77,,:,,777777777777
7777777 ,::7777.:,,=777,,::7 7777777777
77    77,:77777.,,,7777+::~, 7777777777
77     ,,, 7777,,.,777777.:~:,777777777
77 =~ ,::777777,,:,7777777,,~.777777777
77 =I:,,:777777~,,,,777777~,,:,77777777
77 =I::,?777777+.,:.777777:.,,:77777777
77 :+:~,777777 ::=~.7777777,,,,77777777
777,.~,~7777777,,,..7777777,~::77777777
7777,,,,77777 ,:,,,.7777777,,,, 7777777
777777~7777=:~~,,7777777777,,=,?7777777
777777=77777777777777777777==~::7777777
7777777777777777777777777777.:,77~77777
'''

switch = ''
choice1 = ''

hero_stats = [40, 4, 2]  # hp, attack, defense
hero_abilities = {'1': ['Basic: Strike of Shienar', 5],
                  '2': ['Defense: Mountain Stands Firm', 6],
                  '3': ['Heavy: River Cuts Rock', 10]}

trolloc_stats = [20, 3, 2]
trolloc_abilities = {1: ['Basic: Snarling Swipe', 4],
                     2: ['Defense: Raise Arms', 4],
                     3: ['Heavy: Thundering Bite', 5]}

fade_stats = [35, 6, 3]
fade_abilities = {1: ['Basic: Blight Slash', 6],
                  2: ['Defense: Shadows of the Black Wind', 4],
                  3: ['Heavy: Shiv of the Dark One', 8]}

forsaken_stats = [55, 6, 4]
forsaken_abilities = {1: ['Basic: Unseen Hands', 6],
                      2: ['Defense: Wind Wall', 6],
                      3: ['Heavy: Balefire', 8]}


def slow_print(s, ):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()  # defeat buffering

        time.sleep(random.random() * .01)


def lore():
    global choice1

    print(Color.red + Color.bold + "The Den of the Black Ajah\n".center(columns) + Color.end)
    time.sleep(1)
    print(Color.darkcyan + 'An RPG adapted from the fantasy book series:\n'.center(columns))
    time.sleep(1)

    print(Color.yellow + "The Wheel of Time".center(columns) + Color.end)
    print(Color.yellow + "by Robert Jordan\n".center(columns) + Color.end)
    slow_print(text.center(columns))
#   for c in text:
#       print(c, end='' + Color.yellow) With help from Kevin for iterating over characters.

    time.sleep(1)
    print(Color.blue + "You are a warder bonded to an Aes Sedai." + Color.end)
    print(Color.blue + "Use your abilities in combat and recover the Angreal stolen by Black Ajah.\n" + Color.end)

    time.sleep(1)

    print(Color.bold + Color.blue + "The game ends when you lose all your hp...\n" + Color.end)

    time.sleep(1)  # Puts game to sleep for 5 seconds before printing next line.

    print(Color.green + Color.bold + "Chapter 1")

    time.sleep(1)

    print(Color.green + '''\nYou find yourself waking from a troubling dream in the middle of the Tarbon forest.
The Aes Sedai you are bonded too is missing. You can feel the link to her coming from somewhere in the village ahead.''' + Color.end)

    time.sleep(1)

    print(Color.red + '''Go to the village or stay and hunt for her in the forest? "hunt or Go" (h/g)''' + Color.end),
    choice1 = input()


def first_choice():
    if choice1 == 'g':
        print('''You enter the village and see that it is de/home/coyotestroyed.
You speak with a villager who is holding his crying wife.\n''')

        time.sleep(1)

        print('''You: "What happened in here!?"''')
        print(Color.green + '''Man:''' + Color.end + '''' "A Black Ajah came to steal an Angreal that our ancestors have kept hidden
for the White Tower for over 3,000 years. The Black Ajah took the Angreal and destroyed
our entire village! Please return the artifact to the White Tower for us. It is said there
is an Se'Angreal within the shadowspawn's den from the Age of Legends that could repair our village. Please
help us!"
''')
        time.sleep(1)

        print('''Warder: After agreeing to help the villager hands you a map with the location of the den on it.''')

    if choice1 == 'h':

        print(''' After hunting for a while you realize you should have gone to the
village you saw earlier.\n
You reach the village and see it has been destroyed.
You talk to a man who is hugging a woman on her knees crying.\n
Warder: "What happened in here!?"
Village Man: "A Black Ajah came to steal an artifact that our ancestors have kept hidden
for the White Tower for well over 200 years. The Ajah took the artifact and destroyed
the entire village! Please return the artifact to the White Tower for us. It is said there
is an artifact within the den from the Age of Legends that can repair our village. Please
help us!"
''')
        print('''You agree to help and the villager hands you a map with the location of the den on it.
''')


def bridge():
    time.sleep(3)
    global hero_stats
    global hero_abilities
    global trolloc_stats
    global trolloc_abilities

    print('''You depart from the village. You see a Trolloc blocking the bridge.
The Trolloc sees you and utters:
Trolloc: "Only shadowspawn pass over this bridge. I will cut you to pieces!"\n
You and the Trolloc enter battle stances.
''')
    time.sleep(2)
    print(Color.purple + '''These are your abilities'''
          , hero_abilities, Color.red + '''[attack name, damage/defense].
These are your stats''', hero_stats, '''[hp, attack, defense].
''' + Color.end)
    print('Opponent stats:', trolloc_stats)
    while hero_stats[0] > 0 or trolloc_stats[0] > 0:
        hero_stats[2] = 2
        trolloc_stats[2] = 2
        attack_select = input('Write the number corresponding to the ability you want to use \n')
        if attack_select not in hero_abilities:
            attack_select = input('you need to write "1", "2" or "3" \n')
        trolloc_attack = randint(1, 3)
        if hero_stats[0] <= 0:
            print('you lost...')
            break
        print('Hero does', hero_abilities[attack_select][0])

        if trolloc_attack == 2:
            trolloc_stats[2] += trolloc_abilities[trolloc_attack][1]
            print('Orc does block')

        if hero_abilities[attack_select][1] > trolloc_stats[2] and attack_select != '2':
            hero_damage = hero_abilities[attack_select][1] - trolloc_stats[2]
            trolloc_stats[0] -= hero_damage
            time.sleep(1)
            print('Orc has suffered:%d damage. Orc has %d hp left.'
                  % (hero_damage, trolloc_stats[0]))

        else:
            print('Orc suffered no damage. Orc has', trolloc_stats[0], 'hp left.')

        if attack_select == '2':
            hero_stats[2] += hero_abilities[attack_select][1]

        time.sleep(2)

        if trolloc_stats[0] <= 0:
            print('you won!')
            break
        if trolloc_attack != 2:
            print('Orc does', trolloc_abilities[trolloc_attack][0])

        if trolloc_abilities[trolloc_attack][1] > hero_stats[2] and trolloc_attack != 2:
            orc_damage = trolloc_abilities[trolloc_attack][1] - hero_stats[2]
            hero_stats[0] -= orc_damage
            time.sleep(1)
            print('You suffered %d damage. You have %d hp left.'
                  % (orc_damage, hero_stats[0]))
        else:
            print('You suffered no damage.')
    if hero_stats[0] > 0:
        hero_stats = [50, 6, 4]
        lvl_up = ['1', '2', '3']
        for x in lvl_up:
            hero_abilities[x][1] += 2
        print('You leveled up! You have gained these attributes:',
              hero_stats,
              'These are your abilities:',
              hero_abilities)


def cave_entrance():
    global fade_stats
    global fade_abilities
    time.sleep(3)

    print('''After defeating the Trolloc you cross the bridge
and arrive in another section of the forest.
After scouting for some time you notice the den indicated on the map.
You see a Myrddraal guarding the entrance to the den.
You realize you must fight it to continue.\n
The Myrddraal hisses as you draw near and says:\n
Myrddraal: "We have been waiting for you Lord of the Seven Towers ?"\n
Warder: "Defend your self Shadowspawn! The light holds no patience for your kind!"\n
Myrddraal: "Otherszzzz have said the same northerner! Put away your sword warder I won't bite!"\n
Warder: "Silence son of Shaitan!"\n
Myrddraal: "Then you will dieeeeee!"\n
You and the Myrddraal enter battle stances.''')

    time.sleep(4)

    print('''These are your abilities'''
          , hero_abilities, '''[attack name, damage/defense].
These are your stats''', hero_stats, '''[hp, attack, defense].
''')
    print('Opponent stats:', fade_stats)
    while hero_stats[0] > 0 or fade_stats[0] > 0:
        hero_stats[2] = 4
        fade_stats[2] = 3
        attack_select = input('Write the number corresponding to the ability you want to use \n')
        fade_attack = randint(1, 3)
        if hero_stats[0] <= 0:
            print('you lost...')
            break
        print('Hero does', hero_abilities[attack_select][0])

        if fade_attack == 2:
            fade_stats[2] += fade_abilities[fade_attack][1]
            print('Wizard does stone wall')

        if hero_abilities[attack_select][1] > fade_stats[2] and attack_select != '2':
            hero_damage = hero_abilities[attack_select][1] - fade_stats[2]
            fade_stats[0] -= hero_damage
            time.sleep(1)
            print('Wizard has suffered:%d damage. Wizard has %d hp left.'
                  % (hero_damage, fade_stats[0]))
        else:
            print('Wizard suffered no damage. Wizard has', fade_stats[0], 'hp left.')

        if attack_select == '2':
            hero_stats[2] += hero_abilities[attack_select][1]

        time.sleep(2)

        if fade_stats[0] <= 0:
            print('you won!')
            break
        if fade_attack != 2:
            print('Wizard does', fade_abilities[fade_attack][0])

        if fade_abilities[fade_attack][1] > hero_stats[2] and fade_attack != 2:
            wizard_damage = fade_abilities[fade_attack][1] - hero_stats[2]
            hero_stats[0] -= wizard_damage
            time.sleep(1)
            print('You suffered %d damage. You have %d hp left.'
                  % (wizard_damage, hero_stats[0]))
        else:
            print('You suffered no damage.')
    if hero_stats[0] > 0:
        print('You find a grimoire on the floor. You learn the ability Heal. \n')
        hero_abilities['4'] = ['heal', 8]


def boss_fight():
    global forsaken_stats
    global forsaken_abilities
    hero_stats[0] = 50
    time.sleep(3)
    print('''After defeating the Myrddraal you enter the cave.
Upon entering you see a meeting of Black Ajah. The Angreal is behind them.
You don your cloak and attempt to steal the Angreal without disturbing the meeting,
but the moment you touch the Angreal...
Forsaken: "Who dares to touch my property!?"
Warder: "I cannot back down now."
Forsaken: "Very well, your determination is your weakness warder! You are not prepared!\n
You and the forsaken take up battle stances!''')
    time.sleep(2)
    print('''These are your abilities'''
          , hero_abilities, '''[attack name, damage/defense].
These are your stats''', hero_stats, '''[hp, attack, defense].
''')
    print('Opponent stats:', forsaken_stats)
    while hero_stats[0] > 0 or forsaken_stats[0] > 0:
        hero_stats[2] = 4
        forsaken_stats[2] = 4
        attack_select = input('Write the number corresponding to the ability you want to use \n')
        forsaken_attack = randint(1, 3)
        if hero_stats[0] <= 0:
            print('you lost...')
            break
        print('Hero does', hero_abilities[attack_select][0])

        if forsaken_attack == 2:
            forsaken_stats[2] += forsaken_abilities[forsaken_attack][1]
            print('The forsaken blocks your attack!')

        if hero_abilities[attack_select][1] > forsaken_stats[2] and attack_select != '2' and attack_select != '4':
            hero_damage = hero_abilities[attack_select][1] - forsaken_stats[2]
            forsaken_stats[0] -= hero_damage
            time.sleep(1)
            print('The forsaken has suffered:%d damage. The forsaken has %d hp left.'
                  % (hero_damage, forsaken_stats[0]))
        else:
            print('The forsaken suffered no damage. The forsaken has', forsaken_stats[0], 'hp left.')

        if attack_select == '2':
            hero_stats[2] += hero_abilities[attack_select][1]

        if attack_select == '4':
            hero_stats[0] += hero_abilities[attack_select][1]
            print('You have:', hero_stats[0], 'hp')

        time.sleep(2)

        if forsaken_stats[0] <= 0:
            print('you have won!')
            break
        if forsaken_attack != 2:
            print('The forsaken does', forsaken_abilities[forsaken_attack][0])

        if forsaken_abilities[forsaken_attack][1] > hero_stats[2] and forsaken_attack != 2:
            dragon_damage = forsaken_abilities[forsaken_attack][1] - hero_stats[2]
            hero_stats[0] -= dragon_damage
            time.sleep(1)
            print('You suffered %d damage. You have %d hp left.'
                  % (dragon_damage, hero_stats[0]))
        else:
            print('You suffered no damage.')

    if hero_stats[0] > 0:
        print('Congratulations! You won the game!')


def game():
    lore()
    first_choice()
    bridge()
    if hero_stats[0] > 0:
        cave_entrance()
    if hero_stats[0] > 0:
        boss_fight()

while switch != 'n':
    game()
    switch = input('Play again? (y/n) \n')
