 
    # https://blog.devgenius.io/creating-meeting-minutes-using-openai-gpt-3-api-f79e5fc15eb1
    # https://blog.devgenius.io/counting-tokens-for-openai-gpt-3-api-59c8e0812eeb


import re
import tiktoken

def textfile(file_path):
    with open(file_path , "r") as file:
        return file.read()
    
def clean_timing(string):
    return re.sub("\s\([0-9].*\:[0-9]{2}\)", "", string)


def num_tokens_from_string(string: str, encoding_name="gpt2") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def split_in_chunks(text, chunksize_tokens=2000):
    the_chunks = []
    current_chunk_tokens = 0
    current_chunk_lines = []
    current_chunk_index = 0
    for line in text:
        current_chunk_tokens += num_tokens_from_string(line, "gpt2")

        if current_chunk_tokens >= chunksize_tokens:
            current_chunk_tokens = 0
            the_chunks.append("\n".join(current_chunk_lines))
            current_chunk_index+=1
            current_chunk_lines=[]
        
        current_chunk_lines.append(line)
    the_chunks.append("\n".join(current_chunk_lines))
    
    return the_chunks


def prepare_text(file_path):
    mytxt_file = clean_timing(textfile(file_path)).split("\n\n")
    return split_in_chunks(mytxt_file)



