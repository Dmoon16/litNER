# LitNER : Literature NER based on litbank 
[![Built with spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

![image](https://user-images.githubusercontent.com/34004739/120659782-51bdb580-c4a4-11eb-8d28-7797154c6b18.png) ![image](https://user-images.githubusercontent.com/34004739/120660056-921d3380-c4a4-11eb-9797-251354c05b5a.png)


# Installation

```
pip install https://github.com/meghanabhange/litNER/releases/download/0.1/en_litner-0.1.tar.gz
```

# What is this?

- Trained on LitBank
- Using xlm-roberta-large-finetuned-conll03-english
- Trained using spaCy-v3 and can be used directly as a package. 

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
[('FAC', 0.08015267175572519),
 ('VEH', 0.0),
 ('PER', 0.6450381679389313),
 ('LOC', 0.09541984732824428),
 ('GPE', 0.17938931297709923),
 ('ORG', 0.0)]
```

### A Sentimental Journey, by Laurence Sterne (1768)

```
[('FAC', 0.1916529379461834),
 ('VEH', 0.002196595277320154),
 ('PER', 0.6963207029104888),
 ('LOC', 0.08127402526084569),
 ('GPE', 0.028555738605161998),
 ('ORG', 0.0)]
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
[('FAC', 0.13480741797432239),
 ('VEH', 0.056585829766999524),
 ('PER', 0.6174512601046125),
 ('LOC', 0.15953399904897764),
 ('GPE', 0.03162149310508797),
 ('ORG', 0.0)]
```

### Little Women, by Louisa May Alcott (1868)

```
[('FAC', 0.14503105590062113),
 ('VEH', 0.005434782608695652),
 ('PER', 0.7925465838509317),
 ('LOC', 0.04906832298136646),
 ('GPE', 0.007919254658385094),
 ('ORG', 0.0)]
```

## 20th Century 

### In Our Time, by Ernest Hemingway (1925)

```
[('FAC', 0.2533783783783784),
 ('VEH', 0.01962588163140141),
 ('PER', 0.49324324324324326),
 ('LOC', 0.10135135135135136),
 ('GPE', 0.12162162162162163),
 ('ORG', 0.0)]
```

### This Side of Paradise, by F. Scott Fitzgerald (1920)

```
[('FAC', 0.19901870591842993),
 ('VEH', 0.01962588163140141),
 ('PER', 0.6669733210671573),
 ('LOC', 0.08034345292854952),
 ('GPE', 0.033731984053971174),
 ('ORG', 0.00030665440049064706)]
```

### Mrs Dalloway, by Virginia Woolf (1925)

```
[('FAC', 0.24535315985130113),
 ('VEH', 0.01858736059479554),
 ('PER', 0.620817843866171),
 ('LOC', 0.05204460966542751),
 ('GPE', 0.06319702602230483),
 ('ORG', 0.0)]-
```
