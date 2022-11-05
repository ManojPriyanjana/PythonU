
import random #import random module

name_string =input("Give me everybody's names, seperated by a comma : ")
names = name_string.split(",")

print(names)
numberOfItems=len(names) #names list eke thiyana Item gana labaganima

random_choice = random.randint(0,numberOfItems-1)#0 idala list eke item ganata random iteger number laba ganima

person_who_will_pay =names[random_choice] # bil eka gewanna wena kena
print(person_who_will_pay + " is going to buy meal today.")

