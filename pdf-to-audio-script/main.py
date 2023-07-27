import pyttsx3, pypdf

# use PdfReader to open your pdf file. Insert name where appropriate
pdfreader = pypdf.PdfReader(open("grokking-algorithms.pdf", "rb"))
# setup the length of the pdf
num_of_pages = len(pdfreader.pages)

# initialize the text to speech translator
speaker = pyttsx3.init()

# begin loop through pages of pdf to extract text
for page_num in range(num_of_pages):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace("\n", " ")
    print(clean_text)

# save to mp3 file with name of your choice
speaker.save_to_file(clean_text, "story.mp3")
speaker.runAndWait()

# can add timer - does not work well with massive pdf, so best to break pdf into pieces
speaker.stop()
