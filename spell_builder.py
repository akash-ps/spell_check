
import pandas as pd
import re
import collections
import dill

def words(data): return re.findall('[a-z]+', data.lower())

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

def build_spell_model():
    vocab = build_vocab()
    NWORDS = train(words(vocab.decode('utf-8')))
    spell_model_path = "C:\\Users\\AKASH OMER\\Downloads\\" + "spell_model"
    with open(spell_model_path, 'wb') as out:
        dill.dump(NWORDS, out)


def clean_str(string):
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()

def extract_vocab(filename,colnames):

    csv_reader = pd.read_csv(filename, encoding='latin1')
    data=[]
    for colname in colnames:
        content = csv_reader[colname].drop_duplicates().dropna().values.tolist()
        content = [clean_str(dat) for dat in
               content]
        data.extend(content)
    return data

def build_vocab():
    my_vocab = extract_vocab("C:\\Users\\AKASH OMER\\Downloads\\Kaggle_chats.csv", ["spy","text"])
    data = []
    data.extend(my_vocab)
    domain_data = ' '.join(data)
    with open("C:\\Users\\AKASH OMER\\Downloads\\human_text.txt", 'rb') as myfile:
        big_text_content = myfile.read()
    vocab = domain_data.encode() +  b" " + big_text_content
    return vocab


if __name__ == "__main__":
    build_spell_model()
