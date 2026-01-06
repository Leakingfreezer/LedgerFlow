import os
import easyocr

image_path = "test.jpg"

if not os.path.exists(image_path):
    print("❌ test.jpg NOT FOUND")
    print("Put test.jpg in this folder.")
    raise SystemExit

print("Initializing EasyOCR reader...")
reader = easyocr.Reader(['en'], gpu=False)
print("Reader initialized")

print("Running OCR...")
results = reader.readtext(image_path)

print("OCR results:")
for _, text, conf in results:
    print(f"- {text} ({conf:.2f})")

#Storing the raw text to the raw text file
with open("Raw_text.txt", "w") as outfile: 
    for _, text, confidence in results: 
        outfile.write(f"{text}\t{confidence:.2f}\n")

    
