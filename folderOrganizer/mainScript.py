import os 
import shutil 

folderTypeDictionary = {
    "ImageF": ['.JPG', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
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
def makeFolders(pathItems, directory):
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
            option = int(input("Choose a Directory to sort: \n1. Downloads\n2. Documents\n3. Pictures\n4. Custom\nEnter choice (1-4): "))
            if option == 1:
                directory = os.path.join(home, "Downloads")
                break
            elif option == 2:
                directory = os.path.join(home, "Documents")
                break
            elif option == 3:
                directory = os.path.join(home, "Pictures")
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

def getExtension(file_path) -> tuple[str, str]:
    if os.path.isdir(file_path):
        return file_path, "Directory"
    elif os.path.isfile(file_path):
        filename = os.path.basename(file_path)  
        _, file_extension = os.path.splitext(filename)
        return filename, file_extension

def moveToFolder(directory, file_name, extension):    
    matched = False
    for dirName in folderTypeDictionary:
        if extension.lower() in [ext.lower() for ext in folderTypeDictionary[dirName]]:
            matched = True
            break

    targetFolder = dirName if matched else "OthersF"
    destinationFolderDir = os.path.join(directory, targetFolder)
    destination = os.path.join(destinationFolderDir, file_name)
    source = os.path.join(directory, file_name)

    # duplicate filenames
    if os.path.exists(destination):
        base, ext = os.path.splitext(file_name)
        counter = 1
        while os.path.exists(destination):
            file_name = f"{base}_{counter}{ext}"
            destination = os.path.join(destinationFolderDir, file_name)
            counter += 1

    print(f"Moving {source} to {destination}.")
    try:
        shutil.move(source, destination)
    except Exception as e:
        print(f"Unable to move file: {e}")
  

def main(): 
    directory = getDirectory()
    pathItems = os.listdir(directory)
    makeFolders(pathItems, directory)
    for item in pathItems:
        print(item)
        itemDir = os.path.join(directory, item)
        itemName, itemExtension = getExtension(itemDir)
        moveToFolder(directory, itemName, itemExtension)        
    

if __name__ == "__main__":
    main()