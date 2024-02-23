import click
import pandas as pd
from lingua import LanguageDetectorBuilder, IsoCode639_1

# Create a language detector object
detector = LanguageDetectorBuilder.from_all_languages().build()

def detect_language_iso_code(text):
    """
    Detect the ISO 639-1 language code of the given text.

    :param text: A string containing the text to detect the language of.
    :return: A string representing the detected language ISO 639-1 code, or 'UNKNOWN' if detection fails.
    """
    try:
        language = detector.detect_language_of(text)
        if language is not None:
            return language.iso_code_639_1.name
        else:
            return 'NA'
    except Exception as e:
        # Log the exception or handle it as needed
        print(f"Error detecting language: {e}")
        return 'ERROR'

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('--output_file', type=click.Path(), default=None)
@click.option('--text_column', type=int, default=2, show_default=True,
              help='The column number (starting from 1) that contains the text for language detection.')
@click.option('--has_header', is_flag=True, default=False, show_default=True,
              help='Indicates if the input CSV file has a header row.')
def add_language_column(input_file, output_file, text_column, has_header):
    """
    Read a CSV file, detect the ISO 639-1 language code of text in the specified column, and add a new column with the detected language code.

    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file. If not provided, the input file will be overwritten.
    :param text_column: The column number that contains the text for language detection.
    :param has_header: Boolean indicating if the input CSV file has a header row.
    """
    # Adjust for zero-based index
    text_column_index = text_column - 1

    # Read the input CSV file into a DataFrame
    if has_header:
        df = pd.read_csv(input_file)
    else:
        df = pd.read_csv(input_file, header=None)

    # Detect language ISO code for each row in the specified column
    df['language'] = df.iloc[:, text_column_index].apply(detect_language_iso_code)

    # Determine the output file path
    if output_file is None:
        output_file = input_file if input_file.endswith('.csv') else f"{input_file}.csv"

    # Save the DataFrame to a CSV file, respecting the header option
    df.to_csv(output_file, index=False, header=has_header)

if __name__ == '__main__':
    add_language_column()
