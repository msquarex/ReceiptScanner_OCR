import re
from PIL import Image
import pytesseract
import qrcode

food=[]
health=[]
monthly_bills =[]
emi=[]
shopping=[]
entertainment=[]
education=[]
insurance=[]
foodt = 0
healtht=0
monthlyt=0
emit=0
shoppingt=0
entertainmentt=0
educationt=0
insurancet=0

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_and_filter_total(image_path, category):
    # Perform OCR on the image
    text = pytesseract.image_to_string(Image.open(image_path))
    
    # Filter sentences containing the keyword "TOTAL"
    sentences = text.split('\n')
    total_sentences = [sentence for sentence in sentences if 'TOTAL' in sentence.upper()]
    
    # Extract and store the numerical part of the filtered sentences
    total_amounts = []
    for sentence in total_sentences:
        # Use regular expression to extract numerical part
        total_amount = re.search(r'\d+\.*\d*', sentence)
        if total_amount:
            total_amounts.append(float(total_amount.group()))

    # Print the extracted total amounts
    max_amount = max(total_amounts)
    if category == 1:
        food.append(max_amount)
    elif category == 2:
        health.append(max_amount)
    elif category == 3:
        shopping.append(max_amount)
    elif category == 4:
        entertainment.append(max_amount)
    elif category == 5:
        education.append(max_amount)
    elif category == 6:
        monthly_bills.append(max_amount)
    elif category == 7:
        emi.append(max_amount)
    elif category == 8:
        insurance.append(max_amount)

# Loop for uploading bills
while True:
    category = int(input("Enter category number:\n1>food\n2>health\n3>shopping\n4>entertainment\n5>education\n6>monthly_bills\n7>emi\n8>insurance\n---->"))
    while category not in range(1, 9):
        print("Invalid category number. Please enter a number between 1 and 8.")
        category = int(input("Enter category number:\n1>food\n2>health\n3>shopping\n4>entertainment\n5>education\n6>monthly_bills\n7>emi\n8>insurance\n---->"))
        
    image_path = input("Enter the path of the image file: ")
    ocr_and_filter_total(image_path, category)
    
    cont = input("Do you want to upload another bill? (y/n): ")
    if cont.lower() != "y":
        # Generate and save QR code for ending values
        print("\n--Food:")
        for i in food:
            foodt += i
            print(i)
        print("Total Food: ",foodt)

        print("\n--Health:")    
        for i in health:
            healtht+=i
            print(i)
        print("Total Health: ",healtht)

        print("\n--Shopping:\n")
        for i in shopping:
            shoppingt+=i
            print(i)
        print("Total shopping: ",shoppingt)

        print("\n--Entertainment:\n")
        for i in entertainment:
            entertainmentt+=i
            print(i)
        print("Total Entertainment: ",entertainmentt)

        print("\n--Education:\n")
        for i in education:
            educationt+=i
            print(i)
        print("Total Education: ",educationt)

        print("\n--Monthly Bills:\n")
        for i in monthly_bills:
            monthlyt+=i
            print(i)
        print("Total Monthly_Bills: ",monthlyt)

        print("\n--EMI:\n")
        for i in emi:
            emit+=i
            print(i)
        print("Total EMI: ",emit)

        print("\n--Insurance:\n")
        for i in insurance:
            insurancet+=i
            print(i)
        print("Total Insurance: ",insurancet)

        print("\n")

        GT=foodt+healtht+shoppingt+entertainmentt+educationt+monthlyt+emit+insurancet
        print("**GRAND TOTAL**=",GT)
        qr_data = f"Food: {foodt}, Health: {healtht}, Shopping: {shoppingt}, Entertainment: {entertainmentt}, Education: {educationt}, Monthly Bills: {monthlyt}, EMI: {emit}, Insurance: {insurancet}, Grand Total: {foodt + healtht + shoppingt + entertainmentt + educationt + monthlyt + emit + insurancet}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        qr.print_ascii()

        break
