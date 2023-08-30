i = input("File name: ")
if i.endswith(".gif"):
    print("image/gif")
elif i.endswith(".jpg") or i.endswith(".jpeg"):
    print("image/jpeg")
case i.endswith(".png"):
print("image/png")
    case i.endswith(".pdf"):
        print("application/pdf")
    case i.endswith(".txt"):
        print("text/plain")
    case i.endswith(".zip"):
        print("application/zip")
    case _:
        print("application/octet-stream")