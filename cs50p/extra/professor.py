from random import randint

def main():
    level=get_level()
    print(f"Score: {generate_integer(level)}")

def get_level():
    while True:
        try:
            level=int(input("Level: "))
        except ValueError:
            continue
        else:
            if level<1 or level>3:
                continue
            else:
                return level


def generate_integer(level):
    #see if the mistake is repeated, if not then marks will be deducted
    mistakes=[]

    #sets the range of numbers
    if level==1:
        r1,r2=0,9
    elif level==2:
        r1,r2=10,99
    elif level==3:
        r1,r2=100,999

    #record score and trials
    score=10
    q_count=0
    t_count=0

    while q_count!=9:
        x=randint(r1,r2)
        y=randint(r1,r2)
        answer=x+y
        q_str=f"{x} + {y} = "

        #Lets user try until the chances are used up
        while t_count!=3:

            #User's answer
            #Reprompt until a valid answer is given
            while True:
                try:
                    question=int(input(f"{q_count} {q_str}"))
                    #question=int(input(q_str))
                except ValueError:
                    continue
                else:
                    break

            #Check the answer
            if question!=answer:
                t_count+=1
                if t_count<3:
                    print("EEE")
                if q_str not in mistakes:
                    score-=1
                    mistakes.append(q_str)
                else:
                    continue
            else:
                break

        t_count=0
        if question!=answer:
            print(answer)
        q_count+=1

    return score


if __name__ == "__main__":
    main()
