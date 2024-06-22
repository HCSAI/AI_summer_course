def mad_libs():
    story_template = (
        "Today I couldn't attend {place} because I was busy with {subject} class at school."
    )
    place = input("Enter a place: ")
    subject = input("Enter a subject: ")
    story = story_template.format(
        place=place,
        subject=subject
    )
    print("\nMad Libs story:\n")
    print(story)

mad_libs()
