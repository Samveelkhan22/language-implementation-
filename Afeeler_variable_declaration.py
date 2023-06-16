import re

def parse_declaration(declaration):
    tokens = declaration.split()

    if len(tokens) == 6 and tokens[0] == 'Afeeler' and tokens[1] == 'Var' and tokens[2] in ['int', 'float', 'char', 'string'] and tokens[4] == '=':
        data_type = tokens[2]
        variable_name = tokens[3]
        value = tokens[5].rstrip(';')

        if re.match(r'^(_[a-zA-Z][a-zA-Z0-9]*|[a-zA-Z][a-zA-Z0-9]*|[0-9][a-zA-Z0-9]*)$', variable_name):
            if data_type == 'int' and re.match(r'^-?[0-9]+$', value):
                return data_type, variable_name, value
            elif data_type == 'float' and re.match(r'^-?[0-9]+(\.[0-9]*)?$', value):
                return data_type, variable_name, value
            elif data_type == 'char' and re.match(r"^'[a-zA-Z]'$", value):
                return data_type, variable_name, value
            elif data_type == 'string' and re.match(r'^"[a-zA-Z]+"$', value):
                return data_type, variable_name, value
        else:
            return None
    else:
        return None

def main():
    text =  'Afeeler Var int a = 10.0; Afeeler Var float b = 1.5; Afeeler Var char c = \'A\'; Afeeler Var char d = \'A\'; Afeeler Var string e = "Hello";'


    declarations = text.split(';')
    for declaration in declarations:
        declaration = declaration.strip()
        if declaration:
            result = parse_declaration(declaration)
            if result:
                data_type, variable_name, value = result
                print('Valid declaration:', declaration)
                print('Data type:', data_type)
                print('Variable name:', variable_name)
                print('Value:', value)
                print('---')
            else:
                print('Invalid declaration:', declaration)
                print('---')

if __name__ == '__main__':
    main()
