                        ## WHAT TO DO SIMULATOR ##
import random

#Branching test 1
#Check if this gets added after PUSH
def task_simulator():
    print("Do you have so much work that you don't know where to start?")
    print("Use this random number generator to figure out what to do!\n")

    print("Instructions: type in an objective. At the end, type in 'END'")

    task_list = []
    ind = 0 ;

    while 1:
        task = input("What to do: ")
        if (task == "END"):
            break
        task_list.append(task)
        ind += 1

    to_generate = random.randint(0, ind-1)
    print("\nYou should do:", task_list[to_generate])


if __name__ == "__main__":
    task_simulator()







