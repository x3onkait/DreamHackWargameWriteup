import itertools, string

character_set= string.ascii_lowercase + string.digits

minLength = 2
maxLength = 15

for _seq in range(minLength, maxLength):
    for _sub_seq in itertools.product(character_set, repeat = _sub_seq):
        print('G4HeulB' + ''.join(min))
