import PyPDF2
import openai
import argparse
import os


def extract_text_from_pdf(pdf_path):
    """
    Extract text from the specified PDF file.
    """
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() if page.extract_text() else ''
    return text

def generate_case_study(text):
    """
    Generate a structured case study from the given text using OpenAI."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": f"Résumé du document : {text}"},
                {"role": "system", "content": "donne une étude de cas professionnelle, comme aux grandes ecoles de management. structure: Résumé général , Problème(s), Solution retenue, Bénéfices attendus, Coûts et ressources nécessaires, Risques et contraintes."}
            ],
            max_tokens=1000
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error in generating case study: {str(e)}"

def main():
    """Main function to handle command-line based PDF processing."""
    parser = argparse.ArgumentParser(description="Generate a case study from a PDF document.")
    parser.add_argument("pdf_path", type=str, help="The path to the PDF file.")

    args = parser.parse_args()

    pdf_text = extract_text_from_pdf(args.pdf_path)
    case_study = generate_case_study(pdf_text)  # Utilisation correcte de la fonction
    print(case_study)  # Affichage du résultat


if __name__ == "__main__":
    main()
