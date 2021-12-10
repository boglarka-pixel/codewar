
# first solution

def DNA_strand(dna):
    newDNA = dna.maketrans("ATCG","TAGC")
    transdna = dna.translate(newDNA)
    return transdna

print(DNA_strand('AAATCGG'))




#second

def DNA_strand2(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])


print(DNA_strand2('CAGT'))


#third


def DNA_strand3(dna): 
   arrayForDna = []
   if dna == '':
        return []
   for letter in dna:
       if letter == 'A':
           letter = 'T'
           arrayForDna.append(letter)
       elif letter == 'T':
            letter = 'A'
            arrayForDna.append(letter)
       elif letter == 'C':
            letter = 'G'
            arrayForDna.append(letter)
       elif letter == 'G':
            letter = 'C'
            arrayForDna.append(letter)
       listToStr = ''.join([str(elem) for elem in arrayForDna])
   return listToStr
   

  
print(DNA_strand3('AATT'))







