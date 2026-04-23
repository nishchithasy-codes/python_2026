input_file = None

input_file = open("input.txt","r")
lines = input_file.readlines()
input_file.close()

print("The initial content is: \n")
for line in lines:
    print(line.strip())



clean_lines = []
for line in lines:
    text = line.strip()
    if len(text)>0:
        clean_lines.append(text)

print("\n")

clean_lines.sort()
print("The sorted content is: \n")
for item in clean_lines:
    print(item)

output_file = open("output_file","w")
for item in clean_lines:
    output_file.write(item+"\n")
output_file.close()

