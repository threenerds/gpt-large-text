import os
import openai
from library.text import textfile

def main():
    text_file = textfile("Meeting_20230302_0723.txt")
    print(len(text_file))

if __name__ == "__main__":
    main()
    print("Job Done!")