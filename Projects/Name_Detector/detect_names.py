import argparse
import spacy
from typing import List

nlp = spacy.load("en_core_web_sm")


def run(text: str) -> List[str]:
    """
    Detect people's names in the input text.
        
    :param text: the text to process
    :return: the detected names
    """
    doc = nlp(text)
    names = []
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)
    return names


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--filepath",
        "-f",
        required=True,
        help="path to the text file"
    )
    args = parser.parse_args()
    # Open the text file.
    with open(args.filepath, "r") as f:
        text = f.read()
    # Detect people names in the text.
    names = run(text)
    print("Detected names: ", names)
