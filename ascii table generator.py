from itertools import product


def coordinate_system(scale=[3,4]):
    


    values = list(map(float, list(range(1, max(scale) + 1))))

    #print(values)

    linex = '+-----+'
    linex += '-----+' * scale[0]

    linem = '| {} |'
    linem += ' {} |' * (scale[0])

    alphabetsx = ['   '] + [f' {chr(i)} ' for i in range(65, 65 + scale[0] + 25)]
    alphabetsy = [f' {chr(i)} ' for i in range(65, 65 + scale[1] + 1)]

    alphabetsXY = list(product(alphabetsx[1:], alphabetsy))
    #print(alphabetsXY)



    codinaten = dict.fromkeys(alphabetsXY, '   ')


    #print(codinaten)
    #print(codinaten.values())

    

    print(linex)
    print(linem.format(*alphabetsx))

    # input ur cordinaten hear:
    codinaten[( ' A ', ' A ')] = 'A.A'
    codinaten[( ' A ', ' B ')] = 'A.B'
    codinaten[( ' A ', ' C ')] = 'A.C'

    codinaten[( ' D ', ' B ')] = 'D.B'
    

    ##
    counter = 0
    counterL = 0
    counterR = 0

    for i in range(0, (scale[1])):
        counterL = 0
        counter += 1
        print(linex)

        linem = f'| {alphabetsy[counter - 1]} |'
        # linem += f' {codinaten[(alphabetsy[counter - 1], alphabetsy[counter - 1])]} |' * scale[0]

        for ix in range(0, scale[0]):
            
            counterL += 1
            linem += f' {codinaten[(alphabetsx[1:][counterR], alphabetsx[counterL])]} |'
            
        counterR += 1 
        print(linem)
        
    print(linex)
coordinate_system([20, 20])
'''


+-----+-----+-----+-----+
|  /  |  A  |  B  |  C  |
+-----+-----+-----+-----+
|  A  |     |     |     |
+-----+-----+-----+-----+
|  B  |     |     |     |
+-----+-----+-----+-----+
|  C  |     |     |     |
+-----+-----+-----+-----+
|  D  |     |     |     |
+-----+-----+-----+-----+


+-----+
|     |
+-----+

-----+
     |
-----+


'''