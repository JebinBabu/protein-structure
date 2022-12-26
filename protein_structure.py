print('----------------------------------------')
print('            Protein structure           ')
print('----------------------------------------\n\n')

genome_file = input('Genome file/sequence: ')
start = int(input('Start position: '))
end = int(input('End position: '))
sense = input('Is this sence strand (Y/N): ')

if sense == 'Y':
    sense_strand = True
else:
    sense_strand = False


myCodons = []
genome = []
protein = ''
antisense = {'A':'T','T':'A','G':'C','C':'G'}
bases = ['A','T','G','C']

codons = {
    'A':{
        'A':{
            'A':'Lys',
            'T':'Asn',
            'G':'Lys',
            'C':'Asn'
        },
        'T':{
            'A':'Ile',
            'T':'Ile',
            'G':'Met',
            'C':'Ile'
        },
        'G':{
            'A':'Arg',
            'T':'Ser',
            'G':'Arg',
            'C':'Ser'
        },
        'C':{
            'A':'Thr',
            'T':'Thr',
            'G':'Thr',
            'C':'Thr'
        }
    },
    'T':{
        'A':{
            'A':'Stop',
            'T':'Tyr',
            'G':'Stop',
            'C':'Tyr'
        },
        'T':{
            'A':'Leu',
            'T':'Phe',
            'G':'Leu',
            'C':'Phe'
        },
        'G':{
            'A':'Stop',
            'T':'Cys',
            'G':'Trp',
            'C':'Cys'
        },
        'C':{
            'A':'Ser',
            'T':'Ser',
            'G':'Ser',
            'C':'Ser'
        }
    },
    'G':{
        'A':{
            'A':'Glu',
            'T':'Asp',
            'G':'Glu',
            'C':'Asp'
        },
        'T':{
            'A':'Val',
            'T':'Val',
            'G':'Val',
            'C':'Val'
        },
        'G':{
            'A':'Gly',
            'T':'Gly',
            'G':'Gly',
            'C':'Gly'
        },
        'C':{
            'A':'Ala',
            'T':'Ala',
            'G':'Ala',
            'C':'Ala'
        }
    },
    'C':{
        'A':{
            'A':'Gln',
            'T':'His',
            'G':'Gln',
            'C':'His'
        },
        'T':{
            'A':'Leu',
            'T':'Leu',
            'G':'Leu',
            'C':'Leu'
        },
        'G':{
            'A':'Arg',
            'T':'Arg',
            'G':'Arg',
            'C':'Arg'
        },
        'C':{
            'A':'Pro',
            'T':'Pro',
            'G':'Pro',
            'C':'Pro'
        }
    }
}

try:

    with open(genome_file) as infile:

        data = infile.readlines()

        for i in range(len(data)):

            if i == 0:
                continue

            else:

                for j in data[i]:
                    
                    if j in bases:

                        if sense_strand == True:
                            genome.append(j)

                        else:
                            genome.append(antisense[j])

except:

    for i in genome_file:

        if i in bases:

            if sense_strand == True:
                genome.append(i)

            else:
                genome.append(antisense[i])


for i in range(start-1,end+1,3):

    x = ''
    
    for j in range(3):

        x += genome[i+j]
    
    myCodons.append(x)


for i in myCodons:

    aa = codons[i[0]][i[1]][i[2]]

    protein += aa + '-'

print('\n\n')

print(protein[:-1])

print('\n\n')
print('----------------------------------------\n\n')