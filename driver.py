import logging
import os


# Reads and returns the list of files from a directory
def read_directory(mypath):
    current_list_of_files = []

    while True:
        for (_, _, filenames) in os.walk(mypath):
            current_list_of_files = filenames
        logging.info("Reading the directory for the list of file names")
        return current_list_of_files


# Function you will be working with
def creating_subclusters(list_of_terms, name_of_file):
    # Your code that converts the cluster into subclusters and saves the output in the output folder with the same name as input file
    # Note the writing to file has to be handled by you.
    df = pd.DataFrame()

df['words'] = list_of_terms
df['length'] = [*map(lambda x: len(x), words)]
df['first_letter'] = [*map(lambda x: ord(x[0])-97, words)]
df['last_letter'] = [*map(lambda x: ord(x[-1])-97, words)]
df['a_count'] = [*map(lambda x:len(x) - len(''.join(x.split('a'))), words)]
df['e_count'] = [*map(lambda x:len(x) - len(''.join(x.split('e'))), words)]
df['i_count'] = [*map(lambda x:len(x) - len(''.join(x.split('i'))), words)]
df['o_count'] = [*map(lambda x:len(x) - len(''.join(x.split('o'))), words)]
df['u_count'] = [*map(lambda x:len(x) - len(''.join(x.split('u'))), words)]
df['vowel_count'] = df['a_count']+df['e_count']+df['i_count']+df['o_count']+df['u_count']
df['cons_count'] = df['length'] - df['vowel_count']
df['vowel_ratio'] = df['vowel_count']/df['length']
df['cons_ratio'] = 1-df['vowel_ratio']

X = df[df.columns[1:]]

number_of_clusters = 1
best_score = 0.4
for i in range(2, 7):
    classifier = KMeans(n_clusters=i)
    classifier.fit(X)
    if score(X, classifier.predict(X))>best_score:
        number_of_clusters = i
        
best_classifier = KMeans(n_clusters = number_of_clusters)
best_classifier.fit(X)
labels = best_classifier.predict(X)

sub_clusters = []
for i in range(number_of_clusters):
    sub_clusters.append([])
for word, label in zip(words, labels):
    sub_clusters[label].append(word)


    pass


# Main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

    # Folder where the input files are present
    mypath = "input"
    list_of_input_files = read_directory(mypath)
    for each_file in list_of_input_files:
        with open(os.path.join(mypath, each_file), "r") as f:
            file_contents = f.read()
        list_of_term_in_cluster = file_contents.split()

        # Sending the terms to be converted to subclusters in your code
        creating_subclusters(list_of_term_in_cluster, each_file)


        # End of code
