#Imported packages
import pyfiglet

#The main funciton
def main():
    banner_format = pyfiglet.Figlet(font='hex')
    print(banner_format.renderText("A+"))

#Run the main function
if __name__ == "__main__":
    main()