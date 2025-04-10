def get_num_words(text):
    text = text.split()
    num_words = len(text)
    print(f"{num_words} words found in the document")
    return num_words

def character_count(text):
    text = text.lower()
    characters = []
    for i in text:
        if i not in characters:
            characters.append(i)

    character_records = {}
    for char in characters:
        counter = 0
        for i in text:
            if i == char:
                counter += 1
        character_records[char] = counter
    return(character_records)

def sort_on(dict):
    return dict["count"]


def sort_list(dictionary):
    #turn the dictionary into a list of dictionaries
    sorted_list = []
    for k, v in dictionary.items():
        dictionary_to_add = {}
        dictionary_to_add["character"] = k
        dictionary_to_add["count"] = v
        sorted_list.append(dictionary_to_add)
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list




#the following was just to test the sort_list function
'''stationary_items = {
    "pen": 7,
    "pencil": 3,
    "notebook": 10,
    "eraser": 5,
    "sharpener": 2,
    "marker": 8,
    "highlighter": 4,
    "stapler": 6,
    "paper_clip": 9,
    "sticky_notes": 1
}
sort_list(stationary_items)'''