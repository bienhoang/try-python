def save_file():
    try:
        f = open("student.txt", "a")
        f.write("Bien Hoang")
        f.close();
    except Exception as e:
        raise e

def read_file():
    try:
        f = open("student.txt", "r")
        for name in f.readlines():
            print(name)
    except Exception:
        print("Could not read file")

read_file()