#QR_detector with pyzbar barcode detector

import numpy as np
import cv2
from pyzbar.pyzbar import decode

def centroid(vertices):
    x_list = [v[0] for v in vertices]
    y_list = [v[1] for v in vertices]
    x = sum(x_list)/len(vertices)
    y = sum(y_list)/len(vertices)
    return (x,y)

def main():
    li = []
    fp = 'test_images/qr1.png'
    # image = Image.open(fp)
    # image.show()
    image = cv2.imread(fp)
    
    barcodes = decode(image)
    decoded = barcodes[0]
    print(decoded)
    url: bytes = decoded.data
    url = url.decode()
    print(url)
    
    rect = decoded.rect
    #print(rect)

    poly = decoded.polygon
    print(centroid(poly))
    for barcode in barcodes:

        print(barcode.rect)
        (x, y, w, h) = barcode.rect
        r = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 1)

        Cx = x + 0.5 * (w)
        Cy = y + 0.5 * (h)

        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type

        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 255), 2)

        li.append([barcodeData, (Cx, Cy)])
        print("[INFO] Found [{},{}] barcode: {}".format( x, y, barcodeData))
    print(li)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
main()
