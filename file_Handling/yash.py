with open('yashji.txt','r') as source_file:
    text = source_file.read()

with open('yashWings.txt','w') as destination_file:
    destination_file.write(text)