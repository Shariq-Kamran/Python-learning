for i in range(3):
    try:
        with open(f"{i}.txt","r") as file:
            data=file.read
            print(data)
            # or print(file.read)

    except Exception as e:
        print(e)
