import re

#Txt
#code = open("C:\\Users\\Rodrigo\\Desktop\\code.c").read()

code = 'x = (2*y-3)/z'
print('Codigo Bruto')
print(code)

raw_code = re.split('(\(|\)|\+| |\=|\*|\/|\\n|\\t|-)', code)
clean_raw_code = [i for i in raw_code if i.strip()]

print('Codigo limpo')
print(clean_raw_code)

print('------------')
print('| Resultado |')
print('------------')

count = 1
lexic_list_name = []
lexic_list_token = []

lexic_list_name_str = ''
lexic_list_token_str = ''

id_list = ['=', '/', '*', '+', '-', '(', ')', '{', '}']

#Mostrando o nome da senteça
for sentence in clean_raw_code:
    if sentence in id_list:
        token = '<' +sentence+ '>'
        lexic_list_name.append(token) if sentence else None
        lexic_list_name_str += token
    else:
        token = '<' +sentence + ',' + str(count) + '>'
        lexic_list_name.append(token) if sentence else None
        lexic_list_name_str += token
        count += 1

#Mostrando o token da senteça
count = 1
for sentence in clean_raw_code:
    sentence_type = 'num' if sentence.isdigit() else 'id'
    if sentence in id_list:
        token = '<' +sentence+ '>'
        lexic_list_token.append(token) if sentence else None
        lexic_list_token_str += token
    else:
        token = '<' +sentence_type + ',' + str(count) + '>'
        lexic_list_token.append(token) if sentence else None
        lexic_list_token_str += token
        count += 1

print('Com nome da variavel')
print('Lista: ', lexic_list_name)
print('String: ', lexic_list_name_str)
print('\nCom nome do token')
print('Lista: ', lexic_list_token)
print('String: ', lexic_list_token_str)


'''
portuguesa = corinthians + 2*palmeiras
Comprimento = 2*3.1416*raio
R = (a+5)*(b-1)
x = (2*y-3)/z
'''