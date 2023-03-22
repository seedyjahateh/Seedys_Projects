#################################################################################
# Author: Seedy
# Username: jahatehs
#
#################################################################################
# Acknowledgements: Abdullahi Hamdy
#
#
#################################################################################

def func1(category):
    """
    purpose: This functions places every word provided by the user in its right place in the story.
    Param: category:
    return: story:
    """
    story = '''\n\tIn my {0} year of {1} school, this {2} asked me on a date. He \n
   rented a {3} movie and made a {4}. We were watching the movie and \n 
   the oven beeped so the {4} was done. He looked me dead in the eye \n 
   and said, “This is the {5} part.” I then watched this {2} open the \n 
   oven and pull the {4} out with his bare {6}, rack and all, {7} at \n 
   the top of his lungs. We never had a second date.'''.format(*category)
    return story


def func2():
    """
    Purpose: The function prompts user for words of different category to complete the story.
    Param: None
    Return: words
    """
    categories = ["school year", "school level", "species ", "movie",
                  "food", "behavioral adj", "body_parts", "vocal verb"]

    # Prompt the user to input words for each category
    words = []
    for category in categories:
        word = input("Enter a word for the category '{}': ".format(category))
        words.append(word)

    return words


def main():
    """
    Purpose: main() prints the output of func1() with the value of func2() being an argument of func1().
    Param: None
    Return: None
    """
    words = func2()
    print(func1(words))


main()