import cv2
from pytesseract import pytesseract

# Create camera object, 0 is webcam
camera = cv2.VideoCapture(0)
image_output = "./webcam/test1.jpg"
text_output = "./webcam/text_detection_results.txt"

while True:
    _, image = camera.read()
    cv2.imshow("Text Detection", image)         # Window title and image

    # Exits camera when 's' is pressed and saves image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(image_output, image)         # Saves Image to jpg file
        break

# Stops using webcam and closes all camera windows
camera.release()
cv2.destroyAllWindows()

def tesseract(image_path):
    """Uses pytesseract and Tesseract-OCR to extract text from an image"""
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"     # Filepath to Tesseract-OCR executable
    pytesseract.tesseract_cmd = path_to_tesseract
    text = pytesseract.image_to_string(cv2.imread(image_path))
    print(text)
    return text

with open(text_output, "w") as output:
    output.write(tesseract(image_output))