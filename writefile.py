with open("test.txt","r") as r:
    content=r.readlines()
    reversed(content)
    with open("test.txt", "w") as w:
        for line in reversed(content):
            w.write(line)