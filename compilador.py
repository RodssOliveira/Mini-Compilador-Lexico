import re

#Txt
#code = open("C:\\Users\\Rodrigo\\Desktop\\code.c").read()

def code_cleaner(code):
    
    #Removing comments
    raw_code = ''.join(re.split('\/\*(.|\n)*?\*\/', code)) # /* */
    raw_code = ''.join(re.split('[^:]\/\/.*', raw_code)) # //

    #Implementar separado
    #Spliting Logical operators <= >= || && == != (\<\=|\>\=|\|\||\&\&|\=\=|\!\=)
    #raw_code = re.split('(\<\=|\>\=|\|\||\&\&|\=\=|\!\=)', raw_code)
    
    #Spliting Arithmetic operators += -= ++ -- = - / * % (\+\=|\-\=|\+\+|\-\-|\+|\-|\/|\*|\%)
    #raw_code = [re.split('(\+\=|\-\=|\+\+|\-\-|\+|\-|\/|\*|\%)', sentence) for sentence in raw_code]
    
    #Spliting symbols (\(|\)|\{|\}|\;|\\n|\\t)
    #raw_code = [re.split('(\(|\)|\{|\}|\;|\\n|\\t)', sentence) for sentence in raw_code]
    
    raw_code = re.split('(\<\=|\>\=|\|\||\&\&|\=\=|\!\=|\:|\?|\+\=|\-\=|\+\+|\-\-|\+|\-|\/|\*|\%|\(|\)|\{|\}|\;|\\n|\\t| |)', raw_code)
    clean_raw_code = [i for i in raw_code if i.strip()]

    return clean_raw_code

def sentence_type(sentence):
    table = {
        'Comparison': ['<=', '>=', '==', '!=', '>', '<'],
        'Operator': ['+', '-', '*', '/', '%', '^'],
        'Logical': ['&&', '||', '!'],
        '=': '=',
        'Float': ['float'],
        'Return': ['return'],
        '(':'(',
        ')':')',
        '{':'{',
        '}':'}',
        ';':';',
        '?': '?',
        ':': ':'
    }

    #Check if the sentence is in the table
    for key in table:
        for i in table[key]:
            if sentence == i:
                return key + ' ' + str(sentence)
    #Check if is float or int
    try:
        if sentence.isdigit():
            Number = int(sentence)
            return 'Num ' + str(sentence)
        else:
            Number = float(sentence)
            return 'Num ' + str(sentence) #Token Float?
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

    result = []

    #Lexema
    for sentence in code:
        token = '<' +sentence+ '>'
        lexic_final += token

    result.append(lexic_final)
    
    #Token
    count = 1
    id_list = []
    id_sentences = ['id', 'Num', 'Logical', 'Comparison', 'Operator']
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
        else:
            token_final += '<'+ str(token[0]) + '>'
    
    result.append(token_final)
        
    # print('Fluxo de Lexemas')
    # print('String: ', lexic_final)
    # print('\nFluxo de Tokens')
    # print('String: ', token_final)


    return result