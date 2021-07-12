import re
import pandas as pd
import numpy as np
from nltk import ngrams
from lexicon_dict import dict_lexicon
from lexicon_dict_lx import lexicon_dct_lx


def generate_ngrams_nltk(s, n):
    # Convert to lowercases
    s = s.lower()
    
    # Replace all none alphanumeric characters with spaces
    s = re.sub(r'[^A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]', ' ', s)
    
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]
    
    ngramss = list(ngrams(tokens, n))
    return ngramss

def lexicon_pt(texto):
    return([x for x in texto if x in lexicon])


def verifica_elementos(ngrams):
    macro_lista=[]
    for n in ngrams:
        lista = [x for x in n if x in tot]
        lista_contx = [dct[k] for k in lista]
        if len(lista)!=0 and 'LX' in lista_contx:
            macro_lista.append(lista)
    return macro_lista

def polaridade(contexto):
    overall_sent = 0
    for cnt in contexto:
        if type(cnt)!=list:
            cnt = [cnt]
        polarity_cont = polarity[lexicon_pt(cnt)[0]]
        if any(item in cnt for item in Amplifica): # se o contexto contem alguma palavra que amplifica a intensidade da palavra
            if any(item in cnt for item in Negacao): # se o contexto contem alguma palavra que nega 
                polarity_cont = polarity_cont/3
            else:
                polarity_cont = 3*polarity_cont
        elif any(item in cnt for item in Redutor):
            if any(item in cnt for item in Negacao):
                 polarity_cont = 3*polarity_cont
            else:
                polarity_cont = polarity_cont/3
        elif any(item in cnt for item in Negacao):
            polarity_cont = -1*polarity_cont
        overall_sent +=polarity_cont
    return overall_sent

def filtra_tokens(texto):
    apt=[]
    for n in generate_ngrams_nltk(texto,4):
        lista = [x for x in n if x in tot]
        apt.append([dct[k] for k in lista])
    return apt

def organiza_df(df_temp):
    df_montado = pd.DataFrame()
    it_index = iter(df_temp.index)
    try:
        for i in it_index:
            da_vez = pd.DataFrame(df_temp.iloc[i,:]).T
            if "LX" in da_vez['categ'].values[0]:
                df_montado = pd.concat([df_montado,da_vez])
                for j in range(0,4):
                    i = next(it_index)
    except:
        print(".")
    return df_montado


def pipe_sent(texto):
    apt = filtra_tokens(texto)
    df_temp = pd.DataFrame({"ngrams":generate_ngrams_nltk(texto,4),"categ":apt})
    df_montado = organiza_df(df_temp)
    try:
        contexto = df_montado['ngrams'].values
    except:
        df_montado = pd.DataFrame({"ngrams":[('sem','texto')],"categ":'[LX]'})
        contexto = df_montado['ngrams'].values
    if len(contexto)==1:
        polaridade_score = polaridade(verifica_elementos(contexto))
    else:
        polaridade_score = polaridade(np.unique(verifica_elementos(contexto)))
    return polaridade_score



lexicon_data=pd.read_excel("/Users/logic/Documents/senti_lex.xlsx")
Negacao = ['jamais','nada','nem','nenhum','ninguém','nunca','não','tampouco']
Amplifica = ['mais','muito','demais','completamente','absolutamente',
             'totalmente','definitivamente','extremamente','frequentemente','bastante']
Redutor =['pouco','quase','menos','apenas']
lexicon = lexicon_data['palavra'].values

dct = {'jamais':'NC','nada':'NC','nem':'NC','nenhum':'NC','ninguém':'NC','nunca':'NC','não':'NC','tampouco':'NC',
'mais':"AM",'muito':"AM",'demais':"AM",'completamente':"AM",'absolutamente':"AM",'totalmente':"AM",'definitivamente':"AM",'extremamente':"AM",'frequentemente':"AM",'bastante':"AM",
'pouco':'RD','quase':'RD','menos':'RD','apenas':'RD'}

dct.update(lexicon_dct_lx)
tot = list(Negacao)+list(Amplifica)+list(Redutor)+list(lexicon)


polarity = dict_lexicon




tot = Negacao+Amplifica+Redutor
tot = list(tot) +list(['lento','apaga'])
tot = tot + list(lexicon)



