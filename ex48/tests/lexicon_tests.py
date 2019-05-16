from nose.tools import *
from ex48 import lexicon

lex = lexicon()

def test_directions():
    assert_equal(lex.scan("north"), [('direction', 'north')])
    result = lex.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                            ('direction', 'south'),
                            ('direction', 'east')])

def test_verbs():
    assert_equal(lex.scan("go"), [('verb', 'go')])
    result = lex.scan("go kill eat stop look")
    assert_equal(result, [('verb', 'go'),
                            ('verb', 'kill'),
                            ('verb', 'eat'),
                            ('verb', 'stop'),
                            ('verb', 'look')])


def test_stops():
    assert_equal(lex.scan("the"), [('stop', 'the')])
    result = lex.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                            ('stop', 'in'),
                            ('stop', 'of')])


def test_nouns():
    assert_equal(lex.scan("bear"), [('noun', 'bear')])
    result = lex.scan("bear princess cabinet trap")
    assert_equal(result, [('noun', 'bear'),
                            ('noun', 'princess'),
                            ('noun', 'cabinet'),
                            ('noun', 'trap')])

def test_numbers():
    assert_equal(lex.scan("1234"), [('number', 1234)])
    result = lex.scan("3 91234")
    assert_equal(result, [('number', 3),
                            ('number', 91234)])


def test_errors():
    assert_equal(lex.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lex.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                            ('error', 'IAS'),
                            ('noun', 'princess')])

def test_caps():
    assert_equal(lex.scan("Bear"), [('noun', 'bear')])