i = input("File name: ")
match i:
    case i.endswith(".gif"):
        print("image/gif")
    case i.endswith(".jpg") | i.endswith(".jpeg"):
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