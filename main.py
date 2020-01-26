from sys import argv, stderr

from nodor.parse import Nodor, ParseError
from tokenor.tokenor import Tokenizer, TokenizeError
from nodor.typor import typor
from generator.generator import Generator, GenerateError


if __name__ == '__main__':
    file_name = 'main.c'
    code = open(file_name).read()
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
    typor.Typor().type(node)
    Generator().generate(node)


    # stderr.write(str(node))

    # while True:
    #     node = Nodor().parse(Tokenizer.tokenize(input()))
    #     typor.Typor().type(node)
    #     Generator().generate(node)
