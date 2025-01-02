import json

def loadReviews(fileName):
    try:
        with open(fileName, 'r') as file: 
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file not found

def saveReviews(fileName, reviews):
    with open(fileName, 'w') as file:
        json.dump(reviews, file, indent=4)

def addReview():
    title = input("Please enter the book's title: ").title()
    author = input("Please enter the author's name: ").title()

    # Validate publication year input (ensure it's an integer)
    while True:
        year = input("Please enter the publication year: ")
        if year.isdigit():  # Check if the year is a valid number
            year = int(year)  # Convert to integer
            break
        else:
            print("Invalid year. Please enter a valid number for the publication year.")
    
    # Validate rating input (ensure it's a float between 0 and 5)
    while True:
        try:
            rating = float(input("Please rate the book out of 5 stars: "))
            if 0 <= rating <= 5:  # Check if the rating is within the valid range
                break
            else:
                print("Please enter a rating between 0 and 5.")
        except ValueError:
            print("Invalid rating. Please enter a number.")

    comment = input("Please enter your comments for the book: ")

    review = {
        'title': title,
        'author': author,
        'year': year, 
        'rating': rating,
        'comment': comment
    }

    return review

def display(reviews):
    if not reviews:
        print("You have not reviewed any books. Press 1 to rate one!")
    else: 
        for i, review in enumerate(reviews, start=1):
            print(f"\nReview {i}")
            print("Title:", review["title"])
            print("Author:", review["author"])
            print("Publication Year:", review["year"])
            print("Rating:", review["rating"], "out of 5 stars")
            print("Comments:", review["comment"])

if __name__ == "__main__":
    fileName = 'bookReviews.json'
    reviews = loadReviews(fileName)

    print('\nWelcome To Your Library Manager')
    print('1. Add a new review')
    print('2. Display all reviews')
    print('3. Exit')

    choice = input("Please Select One of the Following Options: ")

    if choice == '1':
        newReview = addReview()
        reviews.append(newReview)
        saveReviews(fileName, reviews)
        print("Your review was successfully saved!")
    elif choice == '2':
        display(reviews)
    elif choice == '3':
        print("Goodbye!")
    else: 
        print("Please select one of the available options.")
