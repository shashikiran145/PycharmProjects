import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
db_names = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index, row) in db_names.iterrows()}
print(new_dict)

# Create a list of the phonetic code words from a word that the user inputs
def generate_phonetic():
    name = input("Enter a name").upper()
    try:
        output_name = [new_dict[letter] for letter in name]
    except KeyError:
        print("Enter a letter or a word")
        generate_phonetic()
    else:
        print(output_name)


generate_phonetic()


