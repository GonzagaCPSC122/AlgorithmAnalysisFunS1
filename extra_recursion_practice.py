def print_stars_iter(n: int) -> None:
    for _ in range(n):
        print("*", end="")
    print()

print_stars_iter(5)

def print_stars_rec(n: int) -> None:
    if n == 1:
        print("*")
        return
    print("*", end="")
    print_stars_rec(n - 1)

print_stars_rec(5)

def multiply(a: int, b: int) -> int:
    if a == 0:
        return 0
    return b + multiply(a - 1, b)
    
print(multiply(4, 3))

def display_repeated_string_iter(text: str, n: int) -> None:
    for _ in range(n):
        print(text, end="")
    print()

display_repeated_string_iter("Hi", 3)

def display_repeated_string_rec(text: str, n: int) -> None:
    if n == 0:
        print()
        return
    print(text, end="")
    display_repeated_string_rec(text, n - 1)

display_repeated_string_rec("Hi", 3)

def count_characters(text: str) -> int:
    if text == "":
        return 0
    return 1 + count_characters(text[1:])

print(count_characters("hello"))

def tell_story(actors: list[str], curr_index: int) -> None:
    if curr_index == len(actors) - 1:
        print(curr_index * "\t" + f"...and the little {actors[curr_index]} fell asleep.")
        return
    
    if curr_index == 0:
        print(f"A {actors[curr_index]} couldn't sleep, so the {actors[curr_index]}'s mother told a story about a little {actors[curr_index + 1]},")
    else:
        print(curr_index * "\t" + f"who couldn't sleep, so the {actors[curr_index]}'s mother told a story about a little {actors[curr_index + 1]}")
        
    tell_story(actors, curr_index + 1)
    print(curr_index * "\t" + f"...and the little {actors[curr_index]} fell asleep.")

tell_story(["child", "frog", "bear", "weasel"], 0)