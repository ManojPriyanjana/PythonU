# mulinma row eka ita passe col eka widihata thamai print karanna athulath karanne ([row][col])
# eth me ape ekedi mulinma colom eka ita passe row
# x --> mark is treasure, me x akura position ekakata dana widiha balamu dan

#code ekata 1   2    3 postition
#actual  0     1    2  postition ( index no)
row1 = ["☺","☺","☺"]
row2 = ["☺","☺","☺"]
row3 = ["☺","☺","☺"]

map=[row1,row2,row3] #nested list
print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do  you want to put the treasure? [col][row] :") #23
# onama input ekak string ekak widihata thamai ganne

horizonal = int(position[0]) # 0 weni item eka string eke # haras atha #int walata covert karala thieynne| 2 assin karawa
vertical = int(position[1]) # 1 weni item eka string eke  # kelin atha | 3 assign karanawa uda input walata anwua



selected_row=map[vertical-1]# methana ekak adu karala thiyenne apu input widihata 3 ganna nisa(0,1,2 --> memane thiyenne)
#selected_row[horizonal-1]

selected_row[horizonal-1] # dan api apata ona element eka thiyana thana select karagena awasani
selected_row[horizonal-1] = "X" # dan ethenna x letter eka damu


print(f"{row1}\n{row2}\n{row3}\n")

#----------------------meka apata saralawa mehema liyanna puluwan----------------------

map[0][1] ="M"
print(f"{row1}\n{row2}\n{row3}\n")

print(map[0]) # nikam palaweni row eka print karala thiyenne