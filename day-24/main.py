with open("a-file.txt") as file:
    content = file.read()
    print(content)

### with ... as .. is a context manager, it ensures that the file is properly closed after its suite finishes, even if an exception is raised. This is a best practice for handling files in Python, as it prevents resource leaks and ensures that file handles are not left open unintentionally.

### without using a context manager, you would need to manually close the file with file.close() after you're done with it, which can lead to errors if you forget to do so or if an exception occurs before the close statement is reached.

with open("a-file.txt","a") as file:
    file.write("\n This new line was created by the file.write() method")