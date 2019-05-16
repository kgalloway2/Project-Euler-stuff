from nose.tools import *
import ex49 

generic_word_list = [('verb', 'kill'), ('stop', 'the'), ('error', 'big'), ('noun', 'bear')]
error_word_list = [('error', 'kills'), ('error', 'big'), ('noun', 'bear')]
word_list_2 = [('verb', 'go'), ('direction', 'north')]
word_list_3 = [('noun', 'north')]

def test_peek():
    assert_equal(ex49.peek([('verb', 'kill'), ('stop', 'the')]), 'verb')
    assert_equal(ex49.peek([]), None)

def test_match():
    assert_equal(ex49.match([('verb', 'kill'), ('stop', 'the')], 'verb'), ('verb', 'kill'))
    assert_equal(ex49.match([('verb', 'kill'), ('stop', 'the')], 'noun'), None)
    assert_equal(ex49.match([], 'verb'), None)

def test_skip():
    assert_equal(ex49.skip([('verb', 'kill'), ('stop', 'the')], 'verb'), None)
    assert_equal(ex49.skip([('verb', 'kill'), ('stop', 'the')],'noun'), None)
    assert_equal(ex49.skip([], 'verb'), None)

def test_parse_verb():
    assert_equal(ex49.parse_verb(generic_word_list), ('verb', 'kill'))
    assert_raises(ex49.ParserError, ex49.parse_verb, error_word_list)

def test_parse_object():
    assert_equal(ex49.parse_object(generic_word_list), ('noun', 'bear'))
    assert_equal(ex49.parse_object(word_list_2), ('direction', 'north'))
    assert_raises(ex49.ParserError, ex49.parse_object, error_word_list)

def test_parse_sentence():
    assert_equal(ex49.parse_sentence(generic_word_list), 'player kill bear')
    assert_equal(ex49.parse_sentence(word_list_3), 'noun north')
    assert_raises(ex49.ParserError, ex49.parse_sentence, error_word_list)