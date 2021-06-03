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
    for f in annf:
        text = (datapath/f"{f.name[:-4]}.txt").open("r").read()
        for line in text.split("\n"):
        entity_mapping = [line]
        annot = f.open("r").read().split("\n")
        annot = [ant.split() for ant in annot]
        curr_start = 0
        curr_end = 0
        entities = []
        for ant in annot:
            if len(ant)>5:
                entity = ant[1]
                start = ant[2]
                end = ant[3]
                ent_text = " ".join(ant[4:])
                if int(start) >= curr_end and line.find(ent_text)!=-1: 
                d = {
                    ent_text : entity
                }
                if d not in entities: 
                    entities.append(d)
                curr_end = int(end)
                curr_start = int(start)
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
