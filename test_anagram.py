from anagram import *

def test_is_anagram_checkoff():
    assert is_anagram_checkoff("heart", "earth") == True
    assert is_anagram_checkoff("python", "typhon") == True
    assert is_anagram_checkoff("aaa", "aaa") == True
    assert is_anagram_checkoff("letter", "relett") == True
    assert is_anagram_checkoff("", "") == True
    assert is_anagram_checkoff("a", "b") == False
    assert is_anagram_checkoff("cat", "dog") == False
    assert is_anagram_checkoff("aabbcc", "aabbcd") == False

def test_is_anagram_sort():
    assert is_anagram_sort("heart", "earth") == True
    assert is_anagram_sort("python", "typhon") == True
    assert is_anagram_sort("aaa", "aaa") == True
    assert is_anagram_sort("letter", "relett") == True
    assert is_anagram_sort("", "") == True
    assert is_anagram_sort("a", "b") == False
    assert is_anagram_sort("cat", "dog") == False
    assert is_anagram_sort("aabbcc", "aabbcd") == False

def test_is_anagram_brute_force():
    assert is_anagram_brute_force("heart", "earth") == True
    assert is_anagram_brute_force("python", "typhon") == True
    assert is_anagram_brute_force("aaa", "aaa") == True
    assert is_anagram_brute_force("letter", "relett") == True
    assert is_anagram_brute_force("", "") == True
    assert is_anagram_brute_force("a", "b") == False
    assert is_anagram_brute_force("cat", "dog") == False
    assert is_anagram_brute_force("aabbcc", "aabbcd") == False

def test_is_anagram_count():
    assert is_anagram_count("heart", "earth") == True
    assert is_anagram_count("python", "typhon") == True
    assert is_anagram_count("aaa", "aaa") == True
    assert is_anagram_count("letter", "relett") == True
    assert is_anagram_count("", "") == True
    assert is_anagram_count("a", "b") == False
    assert is_anagram_count("cat", "dog") == False
    assert is_anagram_count("aabbcc", "aabbcd") == False