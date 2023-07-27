import pyttsx3, pypdf


pdfreader = pypdf.PdfReader(open("grokking-algorithms.pdf", "rb"))
num_of_pages = len(pdfreader.pages)
speaker = pyttsx3.init()

for page_num in range(num_of_pages):
    text = pdfreader.pages[page_num].extractText()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)
