from parser.parseutils import *


class TokenParser(ParseUtils):

    def constant(self) -> Node:
        if self.next_is(TK.NUM):
            t = self.pos()
            return Node(ND.INT, type=t.type, val=t.val)
        if self.next_is(TK.IDE):
            t = self.pos()
            try:
                type_, _ = self.variables.get(t.val)
            except TypeError:
                type_ = Type('.unknown')
            return Node(ND.IDE, type=type_, val=t.val)
        raise ParseError

    def identifier(self) -> str:
        if self.next_is(TK.IDE):
            return self.pos().val
        raise ParseError
