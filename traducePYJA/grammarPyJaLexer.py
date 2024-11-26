# Generated from grammarPyJa.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,77,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,
        1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,1,4,4,4,53,8,4,11,4,12,4,54,
        1,5,4,5,58,8,5,11,5,12,5,59,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,
        1,9,1,10,1,10,1,11,1,11,1,12,1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,1,0,4,3,0,65,90,95,95,97,
        122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,13,32,32,
        79,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,
        21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,1,27,1,0,0,0,3,31,1,0,0,0,5,
        38,1,0,0,0,7,44,1,0,0,0,9,52,1,0,0,0,11,57,1,0,0,0,13,63,1,0,0,0,
        15,65,1,0,0,0,17,67,1,0,0,0,19,69,1,0,0,0,21,71,1,0,0,0,23,73,1,
        0,0,0,25,75,1,0,0,0,27,28,5,100,0,0,28,29,5,101,0,0,29,30,5,102,
        0,0,30,2,1,0,0,0,31,32,5,114,0,0,32,33,5,101,0,0,33,34,5,116,0,0,
        34,35,5,117,0,0,35,36,5,114,0,0,36,37,5,110,0,0,37,4,1,0,0,0,38,
        39,5,112,0,0,39,40,5,114,0,0,40,41,5,105,0,0,41,42,5,110,0,0,42,
        43,5,116,0,0,43,6,1,0,0,0,44,48,7,0,0,0,45,47,7,1,0,0,46,45,1,0,
        0,0,47,50,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,8,1,0,0,0,50,48,
        1,0,0,0,51,53,7,2,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,
        54,55,1,0,0,0,55,10,1,0,0,0,56,58,7,3,0,0,57,56,1,0,0,0,58,59,1,
        0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,6,5,0,0,62,
        12,1,0,0,0,63,64,5,40,0,0,64,14,1,0,0,0,65,66,5,41,0,0,66,16,1,0,
        0,0,67,68,5,44,0,0,68,18,1,0,0,0,69,70,5,58,0,0,70,20,1,0,0,0,71,
        72,5,42,0,0,72,22,1,0,0,0,73,74,5,45,0,0,74,24,1,0,0,0,75,76,5,61,
        0,0,76,26,1,0,0,0,4,0,48,54,59,1,6,0,0
    ]

class grammarPyJaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DEF = 1
    RETURN = 2
    PRINT = 3
    IDENTIFIER = 4
    NUMBER = 5
    WS = 6
    LPAREN = 7
    RPAREN = 8
    COMMA = 9
    COLON = 10
    ASTERISK = 11
    MINUS = 12
    ASSIGN = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'def'", "'return'", "'print'", "'('", "')'", "','", "':'", 
            "'*'", "'-'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "DEF", "RETURN", "PRINT", "IDENTIFIER", "NUMBER", "WS", "LPAREN", 
            "RPAREN", "COMMA", "COLON", "ASTERISK", "MINUS", "ASSIGN" ]

    ruleNames = [ "DEF", "RETURN", "PRINT", "IDENTIFIER", "NUMBER", "WS", 
                  "LPAREN", "RPAREN", "COMMA", "COLON", "ASTERISK", "MINUS", 
                  "ASSIGN" ]

    grammarFileName = "grammarPyJa.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

