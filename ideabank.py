def read_ideas_from_file(filename="ideabank.txt"):
    file = open(filename, "r")
    data = file.read().strip()
    ideas = data.split("\n")
    file.close()
    return ideas


def list_ideas():
    ideas = read_ideas_from_file()
    for i in ideas:
        print(f"{ideas.index(i) + 1}. {i}")

        
def save_ideas_to_file(ideas, filename="ideabank.txt"):
    with open(filename, 'w') as fp:
        for item in ideas:
            fp.write("%s\n" % item)

            
def remove_idea(index):
    ideas = read_ideas_from_file()
    ideas.pop(index-1)
    print(f"You deleted {index} idea.")
    return ideas


def create_idea(idea):
    ideas = read_ideas_from_file()
    ideas.append(idea)
    save_ideas_to_file(ideas)

    
def main():
    while True:
        new_idea = input("What is your new idea? \n")
        if new_idea == "--list":
            list_ideas()
        elif new_idea == "--delete":
            while True:
                try:
                    deleted_idea = int(input("Choose deleted idea position (1 or 2 or 3...) \n"))
                    ideas = remove_idea(deleted_idea)
                    save_ideas_to_file(ideas)
                    break
                except:
                    print("Try again.")
        elif new_idea == "--exit":
            exit()
        elif new_idea == "":
            print("You must write something, try again.")
        else:
            create_idea(new_idea)

            
main()
