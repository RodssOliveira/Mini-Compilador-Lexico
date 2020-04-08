import re

def code_cleaner(code):
    aux = []

    #Removing comments
    raw_code = ''.join(re.split('\/\*(.|\n)*?\*\/', code)) # /* */
    raw_code = ''.join(re.split('[^:]\/\/.*', raw_code)) # //

    #Spliting string between quotes ("[^"]*")
    quotes_list = []
    quotes_list.append(re.findall('("[^"]*")', raw_code))
    raw_code = re.split('("[^"]*")', raw_code)

    #Spliting Logical operators <= >= || && == != 'and' = (\<\=|\>\=|\|\||\&\&|\=\=|\!\=|\=)
    for sentence in raw_code:
        if sentence not in quotes_list[0]:
            aux.append(re.split('(\<\=|\>\=|\|\||\&\&|\=\=|\!\=|\=)', sentence))
        else:
            aux.append([sentence])
    raw_code = [val for sublist in aux for val in sublist]
    
    #Spliting Arithmetic operators += -= ++ -- = - / * % (\+\=|\-\=|\+\+|\-\-|\+|\-|\/|\*|\%)
    aux.clear()
    for sentence in raw_code:
        if sentence not in quotes_list[0]:
            aux.append(re.split('(\+\=|\-\=|\+\+|\-\-|\+|\-|\/|\*|\%)', sentence))
        else:
            aux.append([sentence])
    raw_code = [val for sublist in aux for val in sublist]

    #Spliting symbols ( ) { } ; , : \n \t and spaces (\(|\)|\{|\}|\;|\,|\:|\\n|\\t|\\s)
    aux.clear()
    for sentence in raw_code:
        if sentence not in quotes_list[0]:
            aux.append(re.split('(\(|\)|\{|\}|\;|\,|\:|\\n|\\t|\\s)', sentence))
        else:
            aux.append([sentence])
    raw_code = [val for sublist in aux for val in sublist]

    clean_raw_code = [i for i in raw_code if i.strip()]

    return clean_raw_code

def sentence_type(sentence):
    table = {
        'comparison': ['<=', '>=', '==', '!=', '>', '<'],
        'operator': ['+', '-', '*', '/', '%', '^', '++', '--'],
        'logical': ['&&', '||', '!'],
        '=': '=',
        'float': ['float'],
        'return': ['return'],
        '(':'(',
        ')':')',
        '{':'{',
        '}':'}',
        ';':';',
        '?': '?',
        ':': ':',
        ',': ',',
        'do': ['do'],
        'while': ['while'],
        'for': ['for'],
    }

    #Check if sentence is between quotes
    if re.findall('("[^"]*")', sentence):
        return 'literal ' + str(sentence)

    #Check if the sentence is in the table
    for key in table:
        for i in table[key]:
            if sentence == i:
                return key + ' ' + str(sentence)
    #Check if is float or int
    try:
        if sentence.isdigit():
            Number = int(sentence)
            return 'num ' + str(sentence)
        else:
            Number = float(sentence)
            return 'num ' + str(sentence) #Token Float?
    except ValueError:
        return 'id ' + str(sentence)

def compiler(code):
    # print('-------------')
    # print('|Codigo Bruto|')
    # print('-------------')
    # print(code)

    code = code_cleaner(code)

    # print('-------------')
    # print('|Codigo limpo|')
    # print('-------------')
    # print(code)

    # print('\n------------')
    # print('| Resultado |')
    # print('------------')

    count = 1

    lexic_final= ''
    token_final = ''
    table_final = {}

    result = []

    #Lexema
    for sentence in code:
        token = '<' +sentence+ '>'
        lexic_final += token

    result.append(lexic_final)
    
    #Token
    count = 1
    id_list = []
    id_sentences = ['id', 'num', 'logical', 'comparison', 'operator', 'literal']
    for sentence in code:
        token = sentence_type(sentence)
        token = token.split(' ')
        if token[0] in id_sentences:
            if token[1] in id_list:
                id_index = id_list.index(token[1]) + 1
                token_final += '<'+str(token[0])+','+str(id_index)+'>'
            else:
                id_list.append(token[1])
                id_index = id_list.index(token[1]) + 1
                token_final += '<'+str(token[0])+','+str(id_index)+'>'

            #Table generator
            try:
                if table_final[token[1]]:
                    table_final[token[1]] += 'Linha x Coluna Y '
            except:
                if token[0] == 'num':
                    padrao = 'Qualquer constante numérica.'
                elif token[0] == 'logical':
                    padrao = 'Operadores lógicos &&, ||, !'
                elif token[0] == 'comparison':
                    padrao = ' Operadores relacionais < > <= >= == !='
                elif token[0] == 'operator':
                    padrao = 'Operadores aritméticos +, -, *, /, %, ^'
                elif token[0] == 'id':
                    padrao = 'Letra seguida por letras e/ou dígitos'


                table_final[token[1]] = '{} Token: {}, Lexema: {}, Padrão: {} <br>Ocorrências: Linha x Coluna Y '.format(id_list.index(token[1]) + 1, token[0],  token[1], padrao)
        else:
            token_final += '<'+ str(token[0]) + '>'
    
    result.append(token_final)
    result.append(table_final)
        
    # print('Fluxo de Lexemas')
    # print('String: ', lexic_final)
    # print('\nFluxo de Tokens')
    # print('String: ', token_final)
    # print('\n')
    # print('Tabela de simbolos')
    # print(table_final)


    return result