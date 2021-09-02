from utils import readDM, cosine_similarity, neighbours

print("\nQUESTION: What are the female and male biases found in those determined words?\n\n")

lang = -1
while (lang > 5 or lang < 0):
    lang = int(input("Enter\n 0 for English (male/female)\n 1 for English (man/woman) \n 2 for English (masculine/feminine) \n 3 for Portuguese (masculino/feminino)\n 4 for Portuguese (macho/fêmea)\n 5 for Portuguese (homem/mulher)\n\n"))
    
words = list( input("List all words separated by space").split())
interval = input("How many similar words should be analyzed?")
print(words)
i = 0

if lang == 0:
    fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
    male_word = "male"
    female_word = "female"
elif lang == 1:
    fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
    male_word = "man"
    female_word = "woman"
elif lang == 2:
    fasttext_vecs="./data/fasttext-wiki-news-300d-20000.txt"
    male_word = "masculine"
    female_word = "feminine"
elif lang == 3:
    fasttext_vecs = "data/fasttext-wiki-news-300d-20000-pt"
    male_word = "masculino"
    female_word = "feminino"
elif lang == 4:
    fasttext_vecs = "data/fasttext-wiki-news-300d-20000-pt"
    male_word = "macho"
    female_word = "fêmea"
elif lang == 5:
    fasttext_vecs = "data/fasttext-wiki-news-300d-20000-pt"
    male_word = "homem"
    female_word = "mulher"
    
vectors = readDM(fasttext_vecs)

male_bias = []
female_bias = []
ns_words = []

for word in words:
    ns_word = neighbours(vectors,word,int(interval))
    male_bias.append(0)
    female_bias.append(0)

    for ns in ns_word:
        sim_man = cosine_similarity(vectors,ns,male_word)
        sim_woman = cosine_similarity(vectors,ns,female_word)
        print(ns,"male",sim_man,"female",sim_woman)

        diff = sim_man - sim_woman
        if diff > 0.01:
            male_bias[i]+=1
        elif diff < 0.01:
            female_bias[i]+=1

    print("\nMale BIAS:",male_bias[i] / len(ns_word))
    print("\nFemale BIAS:",female_bias[i] / len(ns_word),"\n")
    i +=1