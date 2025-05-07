name = input ("what is your name?")
if name:
    print ("hello"); print (name)
    print ("---")
player = ("alive")
deathchange = ()
ok1=()
ok2=()
snakehelp=()
hug = ()
deathdog=()
redo= ()

deathcount = 0

past_deaths = []

def print_deathstat (death,cur_deathcount):
    global past_deaths
    print (death +" killed you")
    if cur_deathcount < 2:
        return
    print ("you have died " ,cur_deathcount ," times")
    for past_death in past_deaths:
        print ("so far youve died to " +past_death )

def game():
    global player
    global past_deaths
    global deathchange
    global ok1
    global ok2
    global snakehelp
    global hug
    global deathdog
    global redo
    global deathcount
    while player == ("alive"):
        




        begin = input ("say ready to begin your jorney!")
        if begin == ("ready"):
            print (" you begin your jorney in a cave...")

        #cave is relected so # under here are half!!!
        print ("__________█████████████████████████__________") #25█ and 10_
        print ("_____████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████_____") #20▓ 8█ and 5_
        print ("_____██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████_____") #24▓ 6█ and 5 _
        print ("____███████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███████____") #24▓ 7█ and 4 _
        print ("___████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████___") #24▓ 8█ and 3 _
        print ("__█████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████__") #24▓ 9█ and 2 _
        print ("_██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████_") #24▓ 10█ and 1 _

        action1 = input("what will you do? - (sit down)(go towards mysterios light)(leave)")
    
        if action1 == ("sit down"):
            print ("you sit down in an empty cave thats all..")
            action1 = input("what will you do? - (sit down)(go towards mysterios light)(leave)")

        if action1 == ("go towards mysterios light"):
            print ("you walk into the deep caverns following a light...")
            following = ("light")

        if action1 == ("leave"):
            print ("you turn to leave the cave ")
            print ("but as you try to walk closer to")
            ok_tun = input ("the exit you notice your only getting further... (ok)")
            following = ("the exit")


            if ok_tun == ("ok"): 
                print("---------------------")
            
        #the tunnels are the same as the caves they are reflected but wit dif colors
        print("____§§§§§§§§§§§§§§_____________§§§§§§§§§§§§§§____")
        print("___§§§§§§§§§§§§§§§§___________§§§§§§§§§§§§§§§§___")
        print("__§§§§§§§§§§§§§§§§§§_________§§§§§§§§§§§§§§§§§§__")
        print("__§§§§§§§§§§§§§§§§§§_________§§§§§§§§§§§§§§§§§§__")
        print("__§§§§§§§§§§§§§§§§§§_________§§§§§§§§§§§§§§§§§§__")
        print("__§§§§§§§§§§§§§§§§§§_________§§§§§§§§§§§§§§§§§§__")
        print("__§§§§§§§§§§§§§§§§§§_________§§§§§§§§§§§§§§§§§§__")
        #light tunnel has a dog dark tunnel has a sword after we make a monster fight if you go dark but light you tame more animals
        print ("You notice 2 tunnels in your path whitch one will you enter?")
        tunnels = input("(light tunnel)(dark tunnel)")
        dog_take=()

        if tunnels== ("dark tunnel"):
            print ("you walk towards the dark tunnel but get stopped by magic text (WIP)")
            tunnels = input("(light tunnel)(dark tunnel)")

        #make the dog hj cgiu hj

        if tunnels == ("light tunnel"):
            print ("you see a dog")
            print ("   §§§§§§§§§§§§§§§§§§  ")
            print ("  §§§§           §§§§")
            print (" §§§      /]_/>    §§§")
            print (" §§§      |_'_'_|  §§§")
            print (" §§§   =|_[]_[]    §§§")
            print (" §§§               §§§")
            dog_take = input ("Befreind dog? (yes)(no)")
        
        if dog_take == ("no"):
            print ("you ignore the dog since its just wasting your")
            print ("time and walk foward hastily right into a spike trap")
            deathdog= ("yes")
            death = ("spikes")
            player = ("dead")
            print (deathdog) 
            deathcount += 1 
            past_deaths.append (death)
            print_deathstat (death,deathcount)


        if player == ("dead"):

            deathscre = print (death +" killed you")
            player = ("alive")
            redo = input ("retry? (y)(n)")

        if redo == ("y"):
            player = ("alive")
        
        if redo== ("n"):
            exit


        if dog_take == ("yes"):
            print ("you pet the dog! it wags its tail happily andit shows you a") 
            print ("spike trap that you would have fallen into on your path to the")
            print (following)
            if deathdog == ("yes"):
                print("as you walk through you notice a 𝘧𝘢𝘮𝘪𝘭𝘪𝘢𝘳 looking impailed body")
            ok1 =input ("To continue press (ok)")

        if ok1 == ("ok"):
            print ("The dog follows you happily as you continue to"+following)
            print ("You notice a sad looking snake")
            print("""
                    ____
                    / . .\\
                    \  ^  |
                    \  /
        _________ / /
        -=:___________/
            """)
            snakehelp = input ("ask snake if its ok? (yes) (no)")
            

        #Python:  Multi-line string
        deathsnake = ()

        if snakehelp == ("no"):
            print ("the snake bites you for staring at it")
            deathsnake= ("yes")
            death = ("Snake bite")
            player = ("dead")
            deathcount += 1 
            past_deaths.append (death)
            print_deathstat (death,deathcount)


        if player == ("dead"):

            redo = input ("retry? (y)(n)")

        if redo == ("y"):
            player = ("alive")




        if snakehelp == ("yes"):
            print ("""The snake tells you about himself and feels better
                and decides to lead you to the end of the cave
                """)
            print ("""
                    ____
                    / . .\\
                    \  w  |
                    \  /
        __________/ /
        -=:___________/
        """)
            ok2 =input ("To continue press (ok)")
            if deathsnake == ("yes"):
                print ("you notice a body laying lifeless on the ground that looks 𝘧𝘢𝘮𝘪𝘭𝘪𝘢𝘳")
        
        
        

        


        if ok2 == ("ok"):
            print("""you enter a new section of a cave with large lush ceilings and
                a large dragon in the center looking like he made a 𝘮𝘪𝘴𝘵𝘢𝘬𝘦..
                """)
            print("""
                /\_/\\
            /\  |0 0,|  /\\
        /  \ \ ^ / /  \\
        / ,__`~)-(~___, \\
        /.' -'`/_/`'    '.\\
                |\_\ |  
                | \|\|    
                | /|/|    
            '-,__\W\_,-))
                    ((
                        )
        """)
            print ("hello"+name)
            print ("you know me whether you understand or not")
            print("you are more worthy of power then somone as 𝘥𝘢𝘳𝘬 as me")
            if deathchange ==("yes"):
                print ("You understand that no matter what 𝘺𝘰𝘶 𝘸𝘪𝘭𝘭 𝘥𝘪𝘦")
            hug = input ("you hug 𝘵𝘩𝘦 𝘤𝘩𝘢𝘯𝘨𝘦𝘥 𝘰𝘯𝘦 (ok)")



        if hug == ("ok"):
            print("you feel power flow into you as you slowly feel yourself become 𝘵𝘩𝘦 𝘱𝘶𝘳𝘦 𝘰𝘯𝘦")
            print("you love your new form and relax on the ground as 𝘵𝘩𝘦 𝘤𝘩𝘢𝘯𝘨𝘦𝘥 𝘰𝘯𝘦 dissapers with your freinds")
            print("you notice a figure who looks trobled")
            print ("you walk closer and he points a shiny stick at you")
            print ("do you say hi or ignore him?")
            print("he stabs you and you die the figure 𝘤𝘩𝘢𝘯𝘨𝘦𝘴")
            death = ("The Unchanged")
            deathchange = ("yes")
            deathcount += 1 
            past_deaths.append (death)
            print_deathstat (death,deathcount)
        
        def unchanged (you):
            if death == ("unchanged"):
                player==("dead")
        
        if player == ("dead"):

            player = ("alive")
            redo = input ("retry? (y)(n)")

        if redo == ("y"):
            player = ("alive")

game ()


    #delay death text..
#konich wahhh

    #𝘮𝘪𝘴𝘵𝘢𝘬𝘦 has emphisis bc the dark route killed light route and now thinks of it as a huge mistake
    #𝘧𝘢𝘮𝘪𝘭𝘪𝘢𝘳 shows emphisis on the fact that the dead body is a past life!



    #if tunnels == ("dark tunnel"):
        #print ("you see a sword!")
        #print ("")
        #print ("                       §§§§§§§§§§§§§§§§§§  ")
        #print ("                      §§§§     /\    §§§§")
       # print ("                     §§§       ||      §§§")
       # print ("                     §§§      _||_     §§§")
        #print ("                     §§§       []      §§§")
        #print ("                     §§§               §§§")
        #print ("this may protect you on your way to the"); print (following)


#the ending of dark tunnel ends with killing the player that helped monsters/dog in the light tunnel
#ending of light tunnel ends with player getting killed by a "monster" monster=dark player
#if players say no to anythng in the tunnel they choose they die 
#the premise is that no matter what you choose you will eventually die infenetly its a never ending hell that 
#no matter how good or bad you are in this game or if you even try to get better form being bad
#you will die the charicter spawns infenatly dying but the bodys are left at each death place so remember to ref them 
#the light one helps lots of monsters then meets a dragon like thing called "the one who changed" he is the dark
#player but he changed into the "monster" he killed (the past light player) and he reconises the new light player
#he says i knew one like you.. ive made a grave mistake in the name of protecting myself you deserve this power far more then me human of light..
#the whole game is a hell for one dude who respawns when he reaches a certain point ill call it an ending for ez
#he has many endings but most end in death and just leave bodys around the cave
#(all dead bodys look firmiliar!!!) (the pure one is the light player dragon hes happy and sorrownded by his animal/ monster freinds)

#in light you befrend (dog, snake, moss eater, the changed one)
#in dark you kill (wearwolf, moss eater, the pure one)
    

    