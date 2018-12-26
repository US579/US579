
with open('imageee', 'rb') as f:
    f = f.read()


output_file = 'ou.PNG'


with open(output_file, 'ab') as f1:
        f1.write(f)