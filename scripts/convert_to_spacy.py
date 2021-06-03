import json
import logging
import random
import re
import string
from collections import defaultdict
from pathlib import Path
from random import sample
from spacy.lang.xx import MultiLanguage
import fire
import pandas
import spacy
from spacy.tokens import DocBin, Span
from src import LOGGER
from tqdm import tqdm

LOGGER.info("Generate Sythetic Names")

nlp = MultiLanguage()


def convert(out_file: Path, files: list):
    output_filename = out_file
    LOGGER.info(f"Saving in {output_filename}")
    test_output = []
    for f in files:
        text = (dev/f"{f.name[:-4]}.txt").open("r").read()
        entity_mapping = [text]
        annot = f.open("r").readlines()
        annot = [ant.split() for ant in annot]
        entities = []
        for ant in annot:
            entity = ant[1]
            if not (entity[:3] == "Has") and not (entity[:2] == "Is") and entity not in ("AnnotatorNotes", "QuantityQualifier", "Qualifies"):
            ent_text = ant[4:]
            entities.append({
                " ".join(ent_text) : entity
            })
        entity_mapping.append({
            "entities" : entities
        })
        test_output.append(entity_mapping)
    json.dump(test_output, output_filename.open("w"), indent=2, ensure_ascii=False)


def convert_to_spacy_format(
    brat_dir: str = "MeasEval/data/train/brat",
    out_file: str = "train.json"
    data_path: str = "./assets",
):
    LOGGER.info(f"==========RECIEVED INPUT============")
    LOGGER.info(f"brat_dir\t\t{brat_dir}")
    LOGGER.info(f"out_dir Path\t\t{out_dir}")
    LOGGER.info(f"data_path\t\t{data_path}")
    LOGGER.info(f"====================================")
    data_path = Path(data_path)
    out_file = data_path / out_file
    brat_dir_path = data_path / brat_dir
    p = brat_dir_path.glob("*.ann")
    files = [x for x in p if x.is_file()]
    LOGGER.info("======Found following files=====")
    for file in files:
        LOGGER.info(file)
    LOGGER.info("===============================")
    LOGGER.info("Converting to SpaCy Format...")
    convert(out_file=out_file, files=files)
    LOGGER.info("Done.")


if __name__ == "__main__":
    fire.Fire(convert_to_spacy_format)
