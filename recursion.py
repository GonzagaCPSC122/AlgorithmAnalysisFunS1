def display_string(text: str) -> None:
    if len(text) == 0:
        return
    
    display_string(text[1:])
    print(text[0])

display_string("hello")