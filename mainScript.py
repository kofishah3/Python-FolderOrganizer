import os 
import shutil 

folderTypeDictionary = {
    "ImageF": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
    "DocumentF": ['.pdf', '.docx', '.doc', '.xls', '.xlsx', '.pptx', '.ppt', '.txt', '.odt', '.csv'],
    "VideoF": ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'],
    "AudioF": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    "CodeF": ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.ts', '.json', 'dart'],
    "ArchiveF": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    "ExecutableF": ['.exe', '.msi', '.apk', '.bat', '.sh', '.app'],
    "DatabaseF": ['.sql', '.db', '.mdb', '.accdb'],
    "OthersF": [] #fallback if none of the above
}

#checks if the sorting folders already exists in the directory
def checkExisting(pathItems, directory):
    for dirName in folderTypeDictionary:
        try:
            newDirectory = os.path.join(directory, dirName)
            os.mkdir(newDirectory)   
            print(f"Creating {dirName} Directory.")
        except(FileExistsError):
            print(f"Directory {dirName} already exists!")    

#helper function just for debugging
def deleteDirectories(pathItems):
    for dirName in folderTypeDictionary:
        if dirName in pathItems:
            print(f"Removed {dirName} succesfully!")
            os.rmdir(dirName)
        else:
            print(f"{dirName} Directory not found!") 

def getDirectory():
    home = os.path.expanduser("~")
    directory = ""

    while True:
        try:
            option = int(input("Choose a Directory to sort: \n1. Downloads\n2. Documents\n3. Desktop\n4. Custom\nEnter choice (1-4): "))
            if option == 1:
                directory = os.path.join(home, "Downloads")
                break
            elif option == 2:
                directory = os.path.join(home, "Documents")
                break
            elif option == 3:
                directory = os.path.join(home, "Desktop")
                break
            elif option == 4:
                directory = input("Enter the full path of your custom directory: ").strip()
                if os.path.isdir(directory):
                    break
                else:
                    print("Invalid path. Please try again.")
            else:
                print("Invalid option. Please enter a number from 1 to 4.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    return directory

def main(): 
    directory = getDirectory()
    pathItems = os.listdir(directory)
    print(pathItems)
    checkExisting(pathItems, directory)

if __name__ == main():
    main()