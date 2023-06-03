# text recognition
import easyocr
import cv2

def convert_image_text() -> str:
    output: str = ''

    # set up locale/language
    reader = easyocr.Reader(['en'])

    # read image
    img = cv2.imread("captcha.png")

    # convert image to text
    result = reader.readtext(img)

    # print text
    for i in result:
        # print(i[1])
        output += i[1]
    
    return output