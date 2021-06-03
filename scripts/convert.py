"""Convert entity annotation from spaCy v2 TRAIN_DATA format to spaCy v3
.spacy format."""
import warnings
from pathlib import Path

import spacy
import srsly
import typer
from spacy.tokens import DocBin

"""Convert entity annotation from spaCy v2 TRAIN_DATA format to spaCy v3
.spacy format."""
import warnings
from pathlib import Path

import spacy
import srsly
import typer
from spacy.tokens import DocBin


def convert(lang: str, input_path: Path, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    count = 0
    total_count = 0
    for text, annot in srsly.read_json(input_path):
        total_count += 1
        doc = nlp.make_doc(text)
        ents = []
        for word_dict in annot["entities"]:
            for key in word_dict:
                word = key
                label = word_dict[key]
            start = doc.text.find(word)
            end = start + len(word)
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                count += 1
            else:
                ents.append(span)
        try:
            doc.ents = ents
        except:
            count += 1
        db.add(doc)
    db.to_disk(output_path)
    print(f"Total Skipped : {count} out of {total_count}")


if __name__ == "__main__":
    typer.run(convert)
