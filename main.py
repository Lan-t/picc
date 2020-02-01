from sys import argv, stderr
from typing import List

from tokenor import Tokenizer, TokenizeError
from nodor import Nodor, ParseError
from nodor import variable_validator
from nodor.variable_validator.scope import NotExist
from nodor import typor
from generator import Generator, GenerateError


if __name__ == '__main__':
    file_name = 'main.c'
    code = open(file_name).read()
    node = None
    token = None
    try:
        token = Tokenizer.tokenize(code)
    except TokenizeError as e:
        stderr.write(f'{e.position}: {e.args}')
        exit(1)
    # print(token)
    try:
        node = Nodor().parse(token)
    except ParseError as e:
        try:
            stderr.write(f'{token[e.position].position}: {e.args}')
        except IndexError:
            stderr.write(f'{len(code)}: {e.args}')
        exit(1)
    variable_validator.VariableValidator().crawl(node)
    typor.Typor().typing(node)
    Generator().generate(node)


    # stderr.write(str(node))

    # while True:
    #     node = Nodor().parse(Tokenizer.tokenize(input()))
    #     typor.Typor().type(node)
    #     Generator().generate(node)
