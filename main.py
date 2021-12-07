import pandas as pd
import streamlit as st
import altair as alt

st.write("""
# DNA Nucleotide Count Application

This application counts the nucleotide compostion of query DNA 

***
""")

st.header('Enter DNA Sequence')
sequence_input = ">DNA Query \ncgcgggtgtagttttcaggatacgcctgttgtagtctgagagtcgctttacggggggttg"
sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence=sequence.splitlines()
sequence=sequence[1:]
sequence=''.join(sequence)

st.write("""
***
""")

st.header('INPUT (DNA Query)')

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
    d=dict([
        ('A',seq.count('a')),
        ('T',seq.count('t')),
        ('G',seq.count('g')),
        ('C',seq.count('c'))
    ])
    return d
X= DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())

st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X,orient='index')
df = df.rename({0: 'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns ={'index':'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p= alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p=p.properties(
    width=alt.Step(80)
)
st.write(p)