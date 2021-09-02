This repository was originated from a lecture on vector biases from the course Introduction to Machine Learning for Natural Language Processing, given by Professor Aurelie Georgette Geraldine Herbelot at University of Trento

The base code and datasets were provided at the lecture and is available at repository https://github.com/ml-for-nlp/vector-biases. Only the files experiment.py and prepare_dataset.py were authored by me, based on the original code but altered to include specific configurations for the practical part of the final project of the course.

In this experiment, a cosine similarity is performed to identify gender biases related to the words sport/esporte and prostitution/prostituição on two word vector datasets, one for English and one for Portuguese, with the additional goal of comparing the degree of each bias on each language. Further detail, along with results and discussions can be found at the report file.

To run the code, clone the repository and run:

python3 experiment.py

# Lecture Instructions

# Biases in semantic spaces

Distributional Semantics Models (DSMs) reproduce whichever biases are to be found in the data they are trained on. Techniques exist to try and ensure that such biases are not amplified by the learning algorithm, or even to try and remove the bias from the learnt representations. In order to use such algorithms, however, we need to know *where* the biases are to be found. Obvious candidates are semantic subspaces *directly* related to gender, race or disability. But what else?

We are going to look at professions and the kind of attributes associated with them. [Sarah-Jane Leslie and colleagues](https://www.princeton.edu/~sjleslie/expectations%20of%20brilliance.pdf) have shown in a study that philosophy as a profession is strongly associated with particular innate qualities such as being 'talented' and 'sophisticated', and much less with simple dedication and hard work. Such qualities, in turn, are more associated with men than women in standard discourse, leading to fewer women pursuing a philosophical career. This is an example of an indirect bias. Can we find evidence of such indirect biases in vector spaces?


## The data and code

In the *data/* directory, you will find 20,000 vectors from the much larger set released [here](https://fasttext.cc/docs/en/english-vectors.html) (FastText system). Those are 300-dimensional vectors trained on Wikipedia and very large news corpora (16B words). 

You have a small code stub in *explorer.py*, showing you how to load the data and how to perform cosine similarity and nearest neighbours calculations over the semantic space. By running the code, you will also be able to explore the vector space. E.g.:

     What would you like to do? (n = nearest neighbours, s=similarity, q=quit) n

     Enter a word or 'x' to exit nearest neighbours: brilliant
     ['brilliant', 'superb', 'magnificent', 'splendid', 'wonderful', 'clever', 'fantastic', 'terrific', 'fabulous', 'excellent', 'lovely', 'gorgeous', 'amazing', 'talented', 'spectacular', 'remarkable', 'stunning', 'brilliantly', 'witty', 'bright']

     Enter a word or 'x' to exit nearest neighbours: x

     What would you like to do? (n = nearest neighbours, s=similarity, q=quit) s
     Input two words separated by a space or 'x' to exit similarity: man brilliant
     SIM man brilliant 0.3745566349657189
     Input two words separated by a space or 'x' to exit similarity: woman brilliant
     SIM woman brilliant 0.3121614022495688
     Input two words separated by a space or 'x' to exit similarity: man superb
     SIM man superb 0.2622402620944517
     Input two words separated by a space or 'x' to exit similarity: woman superb
     SIM woman superb 0.21795562395218646
 
(We see here that the adjective *brilliant* and its first nearest neighbour *superb* are more similar to *man* than to *woman* in the space.)


Your task is to use the code stub to perform some simple investigation of your choice on the data. A small example is included in *example-question.py* to get you started.



