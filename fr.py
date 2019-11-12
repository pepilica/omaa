with open('res.bmp', mode='wb') as f1:
    with open('input.bmp', mode='rb') as f:
        file = list(f.read())
        for i in range(55):
            f1.write(bytes(file[i]))
        for i in range(55, len(file)):
            value = 255 - int(file[i])
            f1.write(bytes(value))

