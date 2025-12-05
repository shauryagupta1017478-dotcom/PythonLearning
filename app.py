import os

def create_file(filename):
    try:
        with open(filename ,'x') as f:
            print(f" file name {filename}: creatd successfully !")
    except FileExistsError :
        print(f"file name {filename} already exists! ")
    except Exception as E :
        print("an error occurred !")

def view_all_file():
    files = os.listdir()
    if not files:
        print("no files found")
    else:
        print("file in directory ! ")
        for files in files :
            print(files)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"your{filename} is deleted successfully ")
    except FileNotFoundError:
        print("file not found")
    except Exception:
        print("an error occurred")

def read_file(filename):
    try:
        with open('sample.txt' , 'r') as f :
            content = f.read()
            print(f"content of '{filename}'\n{content}")

    except FileNotFoundError:
        print(f"{filename} does not exist !")

    except Exception:
        print("an error occurred !")

def edit_file(filename):
    try:
        with open('sample.txt' , 'a')as f:
            content = input('enter data to add')
            f.write(content + "\n")
            print (f"your file {content} is added successfully !")

    except FileNotFoundError:
        print(f"{filename} does not exist !")

    except Exception:
        print("an error occurred !")

def main ():
    while True:
        print ("file managenment app")

        print ("1. To Create An File: ")
        print ("2. View All File: ")
        print ("3. Delete File: ")
        print ("4. Read File: ")
        print ("5. Edit File: ")
        print ("6. Exixt From App: ")
        

        choice = input("enter your choice form 1 to 6 ")
        
        if choice == '1' :
            filename = input ("enter the name of the file :")
            create_file(filename)

        elif choice == '2':
            view_all_file()
        elif choice == '3' :
            file_name = input ("enter the name of your file you want to delete :")
            delete_file(file_name)

        elif choice == '4' :
            filename = input ("enter the name of your file you want to read :")
            read_file(filename)
        
        elif choice == '5' :
            filename = input ("enter the namrof your file you want to edit it : ")
            edit_file(filename)

        elif choice == '6':
            print ("closing the app :")

            break

        else:
            print ("out of choice ")


if __name__ == "__main__":
    main()   