import csv
import requests


def get_genre(book_title, book_author):
    url = f'https://openlibrary.org/search.json?title={book_title}&author={book_author}'
    response = requests.get(url)

    # CHAT -- if response is okay, parse to JSON
    if response.status_code == 200: # i'm not sure why it says 200 though?
        data = response.json()
        if 'docs' in data and data['docs']:
            # we'll extract genre (subject) from the API response, default to 'Unknown'

            # Write if statement to check if there is subject facet 
            if 'subject_facet' in data['docs'][0]:
                print("subject", data['docs'][0]['subject_facet'])
                return data['docs'][0].get('subject', ['Unknown'])[0]
            else:
                print("NA")
        else:
            print(f"No results found for '{book_title}' by '{book_author}'")
            
            
    return 'Unknown'

# the fuunction to add genres to the CSV
def add_genres_to_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['Genre']  # add 'Genre' column to the header?
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for row in reader:
            # If the genre is missing, look up the genre using the book title and author
            if not row.get('Genre'):  # check if genre is missing
                book_title = row.get('New_Book_Title')  # use the 'New_Book_Title' column
                book_author = row.get('New_Book_Author')  # Use the 'New_Book_Author' column
                if book_title and book_author:  # gotta make sure the book tilte and author aren't empty
                    genre = get_genre(book_title, book_author)
                    row['Genre'] = genre

                # add the row with the genre to the new CSV
            writer.writerow(row)


input_file = 'PEN 23-24 - Main_Table 10.2.csv'  
output_file = 'books_with_genres.csv'  # output it into a new csv file




add_genres_to_csv(input_file, output_file)
