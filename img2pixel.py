from PIL import Image
import sys

if (len(sys.argv) < 2):
    print("Usage: python img2pixel.py <image file1> <image file2> ...")
    exit(-1)

for n, argv in enumerate(sys.argv):
    if n == 0: continue

    pixels = []

    img = Image.open(argv)
    for w in range(img.width):
        tmp = []
        for h in range(img.height):
            tmp.append(img.getpixel((w, h)))
        pixels.append(tmp)

    with open(argv + "_array.txt", "w") as fp:
        fp.write(str(pixels))
        print("output as: %s" % (argv + "_array.txt"))
