import pypandoc

def convert_docx_to_html(input_docx: str, output_html: str):
    # Convert the .docx to HTML
    output = pypandoc.convert_file(input_docx, 'html', outputfile=output_html)
    return output

if __name__ == "__main__":
    input_docx = "CV_Costas_Courcoubetis_2024.docx"
    output_html = "CV_Costas_Courcoubetis_2024.html"
    convert_docx_to_html(input_docx, output_html)
    print(f"Conversion complete: {output_html}")
