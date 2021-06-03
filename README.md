# LitNER : Literature NER based on litbank 
[![Built with spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

![image](https://user-images.githubusercontent.com/34004739/120659782-51bdb580-c4a4-11eb-8d28-7797154c6b18.png) ![image](https://user-images.githubusercontent.com/34004739/120660056-921d3380-c4a4-11eb-9797-251354c05b5a.png)


# Installation

```
pip install XXXXX
```

# What is this?

- Trained on LitBank
- Using xlm-roberta-large-finetuned-conll03-english
- Trained using spaCy-v3 and can be used directly as a package. 

# Analysis of 18th, 19th and 20th century writing 

## Percentage of entities compared to total recognized entities 

## 18th Century 

### Candide, by Voltaire (1759)

```
[('FAC', 0.09227557411273486),
 ('VEH', 0.019206680584551147),
 ('PER', 0.7365344467640919),
 ('LOC', 0.11022964509394571),
 ('GPE', 0.04175365344467641),
 ('ORG', 0.0)]
```

### A Modest Proposal, by Jonathan Swift (1729)

```
```

### A Sentimental Journey, by Laurence Sterne (1768)

```
```

## 19th Century 

### Wuthering Heights, by Emily Brontë (1847)

```
[('FAC', 0.22686496694995278),
 ('VEH', 0.000708215297450425),
 ('PER', 0.6914542020774316),
 ('LOC', 0.07200188857412654),
 ('GPE', 0.008970727101038715),
 ('ORG', 0.0)]
```

### Adventures of Huckleberry Finn, by Mark Twain (1884)

```
```

### Little Women, by Louisa May Alcott (1868)

```
```

## 20th Century 

### In Our Time, by Ernest Hemingway (1925)

```
[('FAC', 0.2533783783783784),
 ('VEH', 0.030405405405405407),
 ('PER', 0.49324324324324326),
 ('LOC', 0.10135135135135136),
 ('GPE', 0.12162162162162163),
 ('ORG', 0.0)]
```

### This Side of Paradise, by F. Scott Fitzgerald (1920)

```
```

### Mrs Dalloway, by Virginia Woolf (1925)

```
```