# gpt-large-text
python example on how to process large amounts of text on GPT-3


Lets assume that a large text is a TXT file with more tokens than the ones supported by GPT-3 API.
* Article
* Essay
* Video transcript

We'll provide this text on a *.txt file

So the script will read a txt file then divide the text in chunks and send them to GPT-3's API on multiple requests, then we can prompt and have results back from that analysis.


