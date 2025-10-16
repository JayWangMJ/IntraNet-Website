import tkinter as tk
from tkinter import filedialog
import pypandoc
import os

def convert_docx_to_html(input_docx: str, output_html: str):
    # Convert the .docx to HTML
    output = pypandoc.convert_file(input_docx, 'html', outputfile=output_html)
    return output

def select_file_and_convert():
    # Open file dialog to select the Word file
    file_path = filedialog.askopenfilename(
        title="Select Word Document",
        filetypes=[("Word files", "*.docx")]
    )
    
    if file_path:
        # Convert selected file to HTML
        # file_name = os.path.basename(file_path)
        out_file_path = file_path.split('.')[0]+'.html'
        html_source_code = convert_docx_to_html(file_path, out_file_path)
        print(f"Conversion complete: {out_file_path}")
        # print(html_source_code)
    else:
        print("No file selected.")

def print_grade():
    print('P')


if __name__ == "__main__":
    # input_docx = "CV_Costas_Courcoubetis_2024.docx"
    # output_html = "CV_Costas_Courcoubetis_2024.html"
    # convert_docx_to_html(input_docx, output_html)
    # print(f"Conversion complete: {output_html}")
    print('Score')
    print_grade()
    root = tk.Tk()
    root.withdraw()
    select_file_and_convert()
