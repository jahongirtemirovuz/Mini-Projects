# Prompt the user to enter various words
noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
verb1 = input("Enter a verb: ")
noun2 = input("Enter another noun: ")
adjective2 = input("Enter another adjective: ")
verb2 = input("Enter another verb: ")

# Create the Mad Libs story using string concatenation
story = "The " + noun1 + " was " + adjective1 + " and " + verb1 + " through the " + noun2 + ". The " + noun2 + " was " + adjective2 + " and " + verb2 + " back at the " + noun1 + "."

# Print the story
print(story)