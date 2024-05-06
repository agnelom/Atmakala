# Atmakala.py

''' Atmakala.py: A Python program which serves as the main entry point for a system that proceses images 
to extract text from them. The extracted text is in Marathi language and is then translated to English. 
'''

# Import necessary modules and packages
import os
import easyocr
from openai import OpenAI
from docx import Document
import pytesseract
import cv2

# Define global variables, if any

# Define classes, functions, and other code

def extractTextTess(image_file):
    # Read the image
    img = cv2.imread(image_file)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform Otsu's thresholding to binarize the image
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Perform OCR on the image
    result_en = pytesseract.image_to_string(thresh, lang='mar+eng')

    # Print the extracted text
    return result_en

'''Function to read an image file and extract text from them using EasyOCR'''
def extractText(image_file):
    #import easyocr
   
    # Initialize the EasyOCR reader
    reader = easyocr.Reader(['mr','en'])

    # Perform OCR on the image
    result_en = reader.readtext(image_file, detail=0, paragraph=True)
    result_en = listToString(result_en)
    #result = reader.readtext(image_file, detail=0)
    return result_en


'''Function to translate text from Marathi to English using OpenAI's GPT-3 model'''
def translateText(PROMPT, MaxToken=1500, temprature=0):
    client = OpenAI(
        api_key=,
    )
    response =  client.chat.completions.create (
                model="gpt-3.5-turbo", 
                messages=[{"role": "user", "content": PROMPT}],
                max_tokens=MaxToken,
                temperature=temprature)
    
    return response.choices[0].message.content.strip()

def writeToDocx(text):
    '''Function to write the extracted text to a Word document'''
    # Create a new Word document
    doc = Document('krishnamonogud_en.docx')

    # Add the text to the document
    doc.add_paragraph(text)

    # Add a page break
    doc.add_page_break()

    # Save the document
    doc.save('krishnamonogud_en.docx')

def listToString(s):
     # initialize an empty string
    textString = ""
 
    # traverse in the string
    for ele in s:
        textString += ele
 
    # return string
    return textString

# Get a list of all the image files in the folder

image_files = [f for f in os.listdir('input') if f.endswith('.jpg')]
image_files.sort()
for image_file in image_files:
#    marathiText = extractText('input/'+image_file)
    marathiText = extractTextTess('input/'+image_file)
    '''marathiTextFlatString = listToString(marathiText)
       prompt = "Please translate this text from Marathi language to English : " + marathiTextFlatString
    '''
    prompt = "Please translate this text from Marathi language to English : " + marathiText
    englishText = translateText(prompt)
    #print(englishText)
    writeToDocx(englishText)

