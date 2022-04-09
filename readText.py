import pytesseract as tess
import cv2
import os

tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def appendFile(dir):
    global frame
    fileNames = os.listdir(dir)
    newFileName = []
    for i in fileNames:
        cap = cv2.VideoCapture(dir + "\\" + i)
        for j in range(10):
            ret, frame = cap.read()
        text = tess.image_to_string(frame)
        if "2022" in text:
            tempSplit = text.split("2022")
            requiredText = "2022" + tempSplit[1][:6] + ".mp4"
        newFileName.append(requiredText)
    return fileNames, newFileName


def fileRename(path, oldNames, newNames):
    for i in range(len(newNames)):
        oldName = path + f"\\{oldNames[i]}"
        newName = path + f"\\{newNames[i]}"
        os.rename(oldName, newName)


path = r"D:\Class Recordings\BMAT\t"
fileNames = os.listdir(path)
output = appendFile(path)
for i in output[1]:
    print(i)
fileRename(path, output[0], output[1])
