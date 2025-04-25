with open("9_practice6.txt") as f:
    data = f.readlines()
    line_no = 0
    for line in data:
        line_no += 1 
        if ("python" in line):
            print(f"The log contains 'python' in line no: {line_no}")
            break
           
    else:
        print(f"The log doesn't contain 'python'")