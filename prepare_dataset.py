
f = open("data/fasttext-wiki-news-300d-20000-pt","w") #clear contents
f.close()
pt_new_dataset = open('data/fasttext-wiki-news-300d-20000-pt', 'a')
pt_original_dataset = open('data/cc.pt.300.vec', 'r+')

line = pt_original_dataset.readline()
for index in range(20000):
    line = pt_original_dataset.readline()
    pt_new_dataset.write(line)

pt_original_dataset.close()
pt_new_dataset.close()