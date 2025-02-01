# James Aho
# ModuleTwoCaseStudy.py
# This program will repetitively ask the user to input for student's information and will display
# whether or not the student made either of the lists. Enter "ZZZ" at the student's last name prompt to end program.

def main():
    List = [0,0,0]
    while True:
        List[1] = input("Enter the student's last name: ")
        if List[1] == "ZZZ":
            break
        else:
            List[0] = input("Enter the student's first name: ")
            List[2] = float(input("Enter the student's GPA: "))
            if List[2] >= 3.5:
                print(f"{List[0]} {List[1]} made the Dean's List!")
            elif List[2] >= 3.25:
                print(f"{List[0]} {List[1]} made the Honor Roll!")
            else:
                print(f"{List[0]} {List[1]} did not meet the minimum requirement for being on the Honor Roll or on the Dean's List")

    print("Have a nice day!")

main()