def fileexist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def createfile(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print("\033[1;31mThere was an ERROR in the file creation.")
    else:
        print(f"\033[1;32mFile {name} created successfully.")


def readfile(name):
    try:
        a = open(name, 'rt')
    except:
        print("\033[1;31m Error to read the file.")
    else:
        for line in a:
            data = line.split(";")
            data[1] = data[1].replace("\n", "")
            print(f"{data[0]:<20} {data[1]:>8} years old.")
    finally:
        a.close()

def toregister(file, name="Unknown", age=0):
    try:
        a = open(file, 'at')
    except:
        print("\033[1;31mThere was an ERROR to open the file.")
    else:
        try:
            a.write(f"{name};{age}\n")
        except:
            print("\033[1;31mThere was an ERROR to write the data.")
        else:
            print(f"\033[1;32mNew register of {name} added.")
