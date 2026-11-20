import os
import pdfplumber

folder_path = "data"

print("Current Folder:", os.getcwd())

files = os.listdir(folder_path)

print("Files:", files)

all_text = ""

for file in files:
    print("Checking:", file)

    if file.endswith(".pdf"):
        print("Opening:", file)

        with pdfplumber.open(os.path.join(folder_path, file)) as pdf:
            print("Pages:", len(pdf.pages))

            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    all_text += text + "\n"

print("------------")
print(all_text)