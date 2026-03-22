import itertools

def is_anagram_checkoff(s1: str, s2: str) -> bool:
    s1_letters = list(s1) # make a list of chars in s1 b/c lists are mutable
    for char in s2:
        if char in s1_letters:
            # values based removal -> O(n) (linear search stop when
            # you find the first occurrence -> removal)
            s1_letters.remove(char) # check off char as "seen"
        else:
            return False
    return True

def is_anagram_sort(s1: str, s2: str) -> bool:
    s1_list = list(s1)
    s2_list = list(s2)

    s1_list.sort() # efficient sorting is O(nlogn)
    # python utilizes timsort -> O(nlogn)
    s2_list.sort()

    return s1_list == s2_list

def is_anagram_brute_force(s1: str, s2: str) -> bool:
    permutations_iter = itertools.permutations(s2)
    all_permutations = ["".join(perm) for perm in permutations_iter]
    # print(all_permutations, len(all_permutations))
    return s1 in all_permutations

def is_anagram_count(s1: str, s2: str) -> bool:
    s1_counts = [0] * 26
    s2_counts = [0] * 26

    for char in s1:
        char_index = ord(char) - ord("a")
        s1_counts[char_index] += 1

    for char in s2:
        char_index = ord(char) - ord("a")
        s2_counts[char_index] += 1

    return s1_counts == s2_counts