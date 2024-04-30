from PIL import Image

import pytesseract

def main():
    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
    print('--'*30)

    # Simple image to string
    print(pytesseract.image_to_string(Image.open('yogesh.png')))
    print('--'*30)

    # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
    # NOTE: In this case you should provide tesseract supported images or tesseract will return error
    print(pytesseract.image_to_string('yogesh.png'))
    print('--'*30)

    # List of available languages
    print(pytesseract.get_languages(config=''))
    print('--'*30)

    # French text image to string
    print(pytesseract.image_to_string(Image.open('yogesh.png'), lang='eng+hin'))
    print('--'*30)

    
    return
    # Batch processing with a single file containing the list of multiple image file paths
    print(pytesseract.image_to_string('images.txt'))
    print('--'*30)

    # Timeout/terminate the tesseract job after a period of time
    try:
        print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
        print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
    except RuntimeError as timeout_error:
        # Tesseract processing is terminated
        pass

    # Get bounding box estimates
    print(pytesseract.image_to_boxes(Image.open('test.png')))

    # Get verbose data including boxes, confidences, line and page numbers
    print(pytesseract.image_to_data(Image.open('test.png')))

    # Get information about orientation and script detection
    print(pytesseract.image_to_osd(Image.open('test.png')))

    # Get a searchable PDF
    pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
    with open('test.pdf', 'w+b') as f:
        f.write(pdf) # pdf type is bytes by default

    # Get HOCR output
    hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

    # Get ALTO XML output
    xml = pytesseract.image_to_alto_xml('test.png')


if __name__ == '__main__':
    main()
    