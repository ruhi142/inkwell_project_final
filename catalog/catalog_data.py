"""

 INKWELL BOOKS — CATALOG DATA  


HOW TO USE THIS FILE

1. ADD A NEW CATEGORY
   Copy any block inside CATEGORIES below, paste it before the closing "}",
   and change the key (the URL name, lowercase-with-dashes), "title",
   "tagline", and "subcategories". It then appears automatically in the
   "Categories" menu, with its own page at /catalog/<key>/ .

2. ADD A SUBCATEGORY
   Add a line to a category's "subcategories" list, e.g.  "Thrillers",
   The page address is made from the name automatically
   ("Mystery & Thriller" -> /catalog/mystery-thriller/).
   To choose the address yourself, or to give it its own books, use the
   longer form:
       {"name": "Poetry", "slug": "poetry", "books": [ ...books... ]},

3. ADD A BOOK
   Add one line inside the "books": [ ... ] list of the category (or the
   subcategory) it belongs to. A book on a subcategory also shows on its
   parent category page.  Fields:
       "title", "author", "price", "old_price", "img", "condition"
   ("discount" is optional - it is worked out from the two prices.)
   "condition" is "New" or "Pre-loved".
   Always add NEW books at the END of a list. Cart / wishlist remember
   books by position, so inserting in the middle would mix them up.
   (Or pin a book's id yourself with  "id": "my-unique-id" .)

4. BOOK IMAGES  ("img")  - any one of these works:
     a) A file you add yourself: drop  my-book.jpg  into the folder
            catalog/static/catalog/img/books/
        and write   "img": "my-book.jpg"
     b) A full web address:  "img": "https://.../cover.jpg"
     c) A site image path:   "img": "core/img/some-file.jpg"

5. OPTIONAL BOOK FIELDS  (add only when you know the real value)
     "format": "paperback" | "hardcover" | "audiobook"   -> Format filter
     "pages": 320          -> Short (<200) / Medium (200-400) / Long (>400) filter
     "topics": ["true-crime"]   -> extra Topic tags (True Crime filter)
     "condition": "Refurbished" -> shows under the Refurbished filter
     "bestseller": True    -> appears on the Bestsellers page
     "new_arrival": True   -> appears on the New Arrivals page
     "bundle": True        -> appears on the Box Sets page
   Filter chips with no matching book on a page are hidden automatically.

6. Save, restart the server (Ctrl+C, then python manage.py runserver)
   and refresh the browser with Ctrl+Shift+R.

Set "in_menu": False on a category to keep it out of the Categories menu.
"count" is optional (the "6,200 titles" badge on the category page).
==========================================================================
"""

CATEGORIES = {
    "fiction": {
        "title": "Fiction",
        "tagline": "Stories that stay with you long after the last page.",
        "count": "6,200",
        "subcategories": [
            {
                "name": "Romance & Contemporary",
                "slug": "romance-contemporary",
                "books": [
                    {"title": "It Ends with Us", "author": "Colleen Hoover", "price": 1, "old_price": 1, "discount": 0, "img": "https://covers.openlibrary.org/b/isbn/9781501110368-L.jpg", "condition": "New"},
                    {"title": "The Seven Husbands of Evelyn Hugo", "author": "Taylor Jenkins Reid", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781501161933-L.jpg", "condition": "New"},
                    {"title": "Book Lovers", "author": "Emily Henry", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780593334836-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Love Hypothesis", "author": "Ali Hazelwood", "price": 289, "old_price": 425, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780593336823-L.jpg", "condition": "New"},
                    {"title": "Beach Read", "author": "Emily Henry", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781984806734-L.jpg", "condition": "New"},
                    {"title": "Normal People", "author": "Sally Rooney", "price": 249, "old_price": 350, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781984822178-L.jpg", "condition": "Pre-loved"},
                    {"title": "Ugly Love", "author": "Colleen Hoover", "price": 259, "old_price": 399, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781476762418-L.jpg", "condition": "New"},
                    {"title": "Red, White & Royal Blue", "author": "Casey McQuiston", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250316776-L.jpg", "condition": "New"},
                    {"title": "Every Summer After", "author": "Carley Fortune", "price": 280, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780593438534-L.jpg", "condition": "Pre-loved"},
                    {"title": "People We Meet on Vacation", "author": "Emily Henry", "price": 275, "old_price": 399, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781984806758-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Mystery & Thriller",
                "slug": "mystery-thriller",
                "books": [
                    {"title": "The Silent Patient", "author": "Alex Michaelides", "price": 239, "old_price": 399, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9781250301703-L.jpg", "condition": "New"},
                    {"title": "Gone Girl", "author": "Gillian Flynn", "price": 299, "old_price": 499, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9780307588371-L.jpg", "condition": "New"},
                    {"title": "The Girl on the Train", "author": "Paula Hawkins", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781594633669-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Maid", "author": "Nita Prose", "price": 319, "old_price": 450, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780593356159-L.jpg", "condition": "New"},
                    {"title": "The Guest List", "author": "Lucy Foley", "price": 289, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780062868930-L.jpg", "condition": "Pre-loved"},
                    {"title": "Verity", "author": "Colleen Hoover", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/id/13009038-L.jpg", "condition": "New"},
                    {"title": "The Paris Apartment", "author": "Lucy Foley", "price": 299, "old_price": 450, "discount": 34, "img": "https://covers.openlibrary.org/b/id/12636291-L.jpg", "condition": "New"},
                    {"title": "Rock Paper Scissors", "author": "Alice Feeney", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781250266101-L.jpg", "condition": "Pre-loved"},
                    {"title": "Then She Was Gone", "author": "Lisa Jewell", "price": 260, "old_price": 380, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781501154645-L.jpg", "condition": "New"},
                    {"title": "One of Us Is Lying", "author": "Karen M. McManus", "price": 285, "old_price": 410, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781524714680-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Fantasy & Sci-Fi",
                "slug": "fantasy-sci-fi",
                "books": [
                    {"title": "Dune", "author": "Frank Herbert", "price": 349, "old_price": 599, "discount": 42, "img": "https://covers.openlibrary.org/b/isbn/9780441172719-L.jpg", "condition": "New"},
                    {"title": "Project Hail Mary", "author": "Andy Weir", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780593135204-L.jpg", "condition": "New"},
                    {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780756404741-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": 299, "old_price": 450, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg", "condition": "New"},
                    {"title": "Neuromancer", "author": "William Gibson", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780441569564-L.jpg", "condition": "Pre-loved"},
                    {"title": "Fourth Wing", "author": "Rebecca Yarros", "price": 420, "old_price": 650, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781649374042-L.jpg", "condition": "New"},
                    {"title": "Mistborn: The Final Empire", "author": "Brandon Sanderson", "price": 360, "old_price": 520, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780765311788-L.jpg", "condition": "New"},
                    {"title": "The Way of Kings", "author": "Brandon Sanderson", "price": 450, "old_price": 699, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780765326355-L.jpg", "condition": "New"},
                    {"title": "Foundation", "author": "Isaac Asimov", "price": 270, "old_price": 399, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780553293357-L.jpg", "condition": "Pre-loved"},
                    {"title": "A Game of Thrones", "author": "George R.R. Martin", "price": 380, "old_price": 599, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780553103540-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Historical & Mythological Fiction",
                "slug": "historical-mythological-fiction",
                "books": [
                    {"title": "Circe", "author": "Madeline Miller", "price": 319, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780316556323-L.jpg", "condition": "New"},
                    {"title": "The Song of Achilles", "author": "Madeline Miller", "price": 289, "old_price": 429, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780062060624-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Book Thief", "author": "Markus Zusak", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780375842207-L.jpg", "condition": "New"},
                    {"title": "Pachinko", "author": "Min Jin Lee", "price": 340, "old_price": 520, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781455563937-L.jpg", "condition": "New"},
                    {"title": "The Nightingale", "author": "Kristin Hannah", "price": 325, "old_price": 480, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780312577230-L.jpg", "condition": "Pre-loved"},
                    {"title": "Palace of Illusions", "author": "Chitra Banerjee Divakaruni", "price": 275, "old_price": 399, "discount": 31, "img": "https://covers.openlibrary.org/b/id/10314060-L.jpg", "condition": "New"},
                    {"title": "Kaikeyi", "author": "Vaishnavi Patel", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/id/14732751-L.jpg", "condition": "New"},
                    {"title": "All the Light We Cannot See", "author": "Anthony Doerr", "price": 335, "old_price": 499, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781476746586-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Seven Moons of Maali Almeida", "author": "Shehan Karunatilaka", "price": 350, "old_price": 550, "discount": 36, "img": "https://covers.openlibrary.org/b/id/14921359-L.jpg", "condition": "New"},
                    {"title": "Wolf Hall", "author": "Hilary Mantel", "price": 365, "old_price": 540, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780312429980-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Classics & Literary Fiction",
                "slug": "classics-literary-fiction",
                "books": [
                    {"title": "1984", "author": "George Orwell", "price": 149, "old_price": 399, "discount": 63, "img": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg", "condition": "New"},
                    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 159, "old_price": 449, "discount": 65, "img": "https://covers.openlibrary.org/b/isbn/9780061120084-L.jpg", "condition": "Pre-loved"},
                    {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 180, "old_price": 299, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9780141439518-L.jpg", "condition": "New"},
                    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 170, "old_price": 280, "discount": 39, "img": "https://covers.openlibrary.org/b/isbn/9780743273565-L.jpg", "condition": "New"},
                    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "price": 220, "old_price": 380, "discount": 42, "img": "https://covers.openlibrary.org/b/isbn/9780140449136-L.jpg", "condition": "Pre-loved"},
                    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "price": 290, "old_price": 450, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780060883287-L.jpg", "condition": "New"},
                    {"title": "Jane Eyre", "author": "Charlotte Brontë", "price": 195, "old_price": 310, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780141441146-L.jpg", "condition": "New"},
                    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 210, "old_price": 320, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780316769488-L.jpg", "condition": "Pre-loved"},
                    {"title": "Brave New World", "author": "Aldous Huxley", "price": 185, "old_price": 300, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780060850524-L.jpg", "condition": "New"},
                    {"title": "Anna Karenina", "author": "Leo Tolstoy", "price": 250, "old_price": 420, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9780143035008-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Graphic Novels",
                "slug": "graphic-novels",
                "books": [
                    {"title": "Maus", "author": "Art Spiegelman", "price": 450, "old_price": 699, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780394747231-L.jpg", "condition": "New"},
                    {"title": "Watchmen", "author": "Alan Moore", "price": 499, "old_price": 799, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9781401238964-L.jpg", "condition": "New"},
                    {"title": "Persepolis", "author": "Marjane Satrapi", "price": 380, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780375714832-L.jpg", "condition": "Pre-loved"},
                    {"title": "Saga Vol. 1", "author": "Brian K. Vaughan", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781607066019-L.jpg", "condition": "New"},
                    {"title": "Heartstopper Vol. 1", "author": "Alice Oseman", "price": 310, "old_price": 480, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781338617436-L.jpg", "condition": "New"},
                    {"title": "Sandman Vol. 1: Preludes & Nocturnes", "author": "Neil Gaiman", "price": 420, "old_price": 650, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781401225759-L.jpg", "condition": "Pre-loved"},
                    {"title": "Batman: The Dark Knight Returns", "author": "Frank Miller", "price": 460, "old_price": 720, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9781563893421-L.jpg", "condition": "New"},
                    {"title": "V for Vendetta", "author": "Alan Moore", "price": 410, "old_price": 620, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780930289522-L.jpg", "condition": "New"},
                    {"title": "March: Book One", "author": "John Lewis", "price": 320, "old_price": 490, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781603093002-L.jpg", "condition": "Pre-loved"},
                    {"title": "Daytripper", "author": "Gabriel Bá & Fábio Moon", "price": 390, "old_price": 580, "discount": 32, "img": "https://covers.openlibrary.org/b/id/6927903-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Poetry",
                "slug": "poetry",
                "books": [
                    {"title": "Milk and Honey", "author": "Rupi Kaur", "price": 199, "old_price": 350, "discount": 43, "img": "https://covers.openlibrary.org/b/isbn/9781449474256-L.jpg", "condition": "New"},
                    {"title": "The Sun and Her Flowers", "author": "Rupi Kaur", "price": 220, "old_price": 380, "discount": 42, "img": "https://covers.openlibrary.org/b/isbn/9781449486792-L.jpg", "condition": "New"},
                    {"title": "Pillow Thoughts", "author": "Courtney Peppernell", "price": 210, "old_price": 360, "discount": 41, "img": "https://covers.openlibrary.org/b/isbn/9781449489755-L.jpg", "condition": "Pre-loved"},
                    {"title": "Devotions", "author": "Mary Oliver", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780399563249-L.jpg", "condition": "New"},
                    {"title": "Selected Poems of Rainer Maria Rilke", "author": "Rainer Maria Rilke", "price": 180, "old_price": 280, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780060908782-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Odyssey", "author": "Homer", "price": 240, "old_price": 390, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780140268867-L.jpg", "condition": "New"},
                    {"title": "Leaves of Grass", "author": "Walt Whitman", "price": 190, "old_price": 310, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780140421996-L.jpg", "condition": "New"},
                    {"title": "The Complete Poems of Emily Dickinson", "author": "Emily Dickinson", "price": 230, "old_price": 370, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780316184137-L.jpg", "condition": "Pre-loved"},
                    {"title": "Goblin Market and Other Poems", "author": "Christina Rossetti", "price": 160, "old_price": 250, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780486280554-L.jpg", "condition": "New"},
                    {"title": "Anxiety for Beginners", "author": "Eleanor Morgan", "price": 200, "old_price": 320, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9781509820351-L.jpg", "condition": "New"},
                ]
            },
            {
                "name": "Crime",
                "slug": "crime",
                "books": [
                    {"title": "The Godfather", "author": "Mario Puzo", "price": 270, "old_price": 420, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780451205766-L.jpg", "condition": "New"},
                    {"title": "In Cold Blood", "author": "Truman Capote", "price": 290, "old_price": 450, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780679745587-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Big Sleep", "author": "Raymond Chandler", "price": 210, "old_price": 330, "discount": 36, "img": "https://covers.openlibrary.org/b/id/11518032-L.jpg", "condition": "New"},
                    {"title": "Mindhunter", "author": "John E. Douglas", "price": 310, "old_price": 480, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781501191961-L.jpg", "condition": "New"},
                    {"title": "The Alienist", "author": "Caleb Carr", "price": 280, "old_price": 430, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780812976144-L.jpg", "condition": "Pre-loved"},
                    {"title": "Red Dragon", "author": "Thomas Harris", "price": 265, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780440206156-L.jpg", "condition": "New"},
                    {"title": "The Silence of the Lambs", "author": "Thomas Harris", "price": 275, "old_price": 420, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780312924584-L.jpg", "condition": "New"},
                    {"title": "Shutter Island", "author": "Dennis Lehane", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/id/15144374-M.jpg", "condition": "Pre-loved"},
                    {"title": "Mystic River", "author": "Dennis Lehane", "price": 260, "old_price": 390, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780062068408-L.jpg", "condition": "New"},
                    {"title": "The Snowman", "author": "Jo Nesbø", "price": 285, "old_price": 440, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780307742995-L.jpg", "condition": "New"},
                ]
            },
        ],
        "books": [
            {"title": "The Silent Patient", "author": "Alex Michaelides", "price": 239, "old_price": 399, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9781250301703-L.jpg", "condition": "New"},
            {"title": "Where the Crawdads Sing", "author": "Delia Owens", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780735219090-L.jpg", "condition": "New"},
            {"title": "The Midnight Library", "author": "Matt Haig", "price": 299, "old_price": 449, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781786892720-L.jpg", "condition": "Pre-loved"},
            {"title": "Circe", "author": "Madeline Miller", "price": 319, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780316556323-L.jpg", "condition": "New"},
            {"title": "The Kite Runner", "author": "Khaled Hosseini", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781594631931-L.jpg", "condition": "Pre-loved"},
            {"title": "Normal People", "author": "Sally Rooney", "price": 249, "old_price": 350, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781984822178-L.jpg", "condition": "New"},
            {"title": "A Little Life", "author": "Hanya Yanagihara", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780804172707-L.jpg", "condition": "New"},
            {"title": "The Song of Achilles", "author": "Madeline Miller", "price": 289, "old_price": 429, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780062060624-L.jpg", "condition": "Pre-loved"},
        ],
    },
    "non-fiction": {
        "title": "Non-Fiction",
        "tagline": "Real stories, real ideas — for the endlessly curious.",
        "count": "3,400",
        "subcategories": [
            {
                "name": "Biographies & Memoirs",
                "books": [
                    {"title": "Becoming", "author": "Michelle Obama", "price": 379, "old_price": 599, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9781524763138-L.jpg", "condition": "Pre-loved"},
                    {"title": "Educated", "author": "Tara Westover", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/id/15216613-L.jpg", "condition": "New"},
                    {"title": "The Diary of a Young Girl", "author": "Anne Frank", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780553296983-L.jpg", "condition": "New"},
                    {"title": "Steve Jobs", "author": "Walter Isaacson", "price": 449, "old_price": 699, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9781451648539-L.jpg", "condition": "New"},
                    {"title": "Shoe Dog", "author": "Phil Knight", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781501135910-L.jpg", "condition": "Pre-loved"},
                    {"title": "When Breath Becomes Air", "author": "Paul Kalanithi", "price": 299, "old_price": 450, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780812988406-L.jpg", "condition": "New"},
                    {"title": "Long Walk to Freedom", "author": "Nelson Mandela", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780316548182-L.jpg", "condition": "Pre-loved"},
                    {"title": "Wings of Fire", "author": "A.P.J. Abdul Kalam", "price": 249, "old_price": 395, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9788173711466-L.jpg", "condition": "New"},
                    {"title": "Born a Crime", "author": "Trevor Noah", "price": 319, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780399588174-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Glass Castle", "author": "Jeannette Walls", "price": 289, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780743247542-L.jpg", "condition": "New"}
                ]
            },
            {
                "name": "Self-help & Personal Growth",
                    "books": [
                    {"title": "Atomic Habits", "author": "James Clear", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg", "condition": "New"},
                    {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "price": 320, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780062457714-L.jpg", "condition": "Pre-loved"},
                    {"title": "Psychology of Money", "author": "Morgan Housel", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780857197689-L.jpg", "condition": "New"},
                    {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "price": 220, "old_price": 350, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780671027032-L.jpg", "condition": "New"},
                    {"title": "Think and Grow Rich", "author": "Napoleon Hill", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781585424337-L.jpg", "condition": "Pre-loved"},
                    {"title": "Deep Work", "author": "Cal Newport", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781455586691-L.jpg", "condition": "New"},
                    {"title": "Ikigai: The Japanese Secret to a Long and Happy Life", "author": "Héctor García & Francesc Miralles", "price": 280, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780143130727-L.jpg", "condition": "Pre-loved"},
                    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "price": 380, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780743269513-L.jpg", "condition": "New"},
                    {"title": "Can't Hurt Me", "author": "David Goggins", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781544512280-L.jpg", "condition": "New"},
                    {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "price": 240, "old_price": 350, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780807014264-L.jpg", "condition": "Pre-loved"},
                    {"title": "Make Your Bed", "author": "William H. McRaven", "price": 210, "old_price": 320, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781455570249-L.jpg", "condition": "New"},
                    {"title": "Show Your Work!", "author": "Austin Kleon", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780761178972-L.jpg", "condition": "Pre-loved"}
                    ]
            },
            {
                "name": "Health, Parenting & Fitness",
                "books": [
                    {"title": "The Body Keeps the Score", "author": "Bessel van der Kolk", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780143127741-L.jpg", "condition": "New"},
                    {"title": "Why We Sleep", "author": "Matthew Walker", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781501144318-L.jpg", "condition": "New"},
                    {"title": "Outlive: The Science and Art of Longevity", "author": "Peter Attia", "price": 429, "old_price": 650, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780593236598-L.jpg", "condition": "New"},
                    {"title": "The Whole-Brain Child", "author": "Daniel J. Siegel & Tina Payne Bryson", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780553386691-L.jpg", "condition": "Pre-loved"},
                    {"title": "Breath: The New Science of a Lost Art", "author": "James Nestor", "price": 319, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780735213616-L.jpg", "condition": "New"},
                    {"title": "How Not to Die", "author": "Michael Greger", "price": 379, "old_price": 599, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9781250066114-L.jpg", "condition": "Pre-loved"},
                    {"title": "Glow Kids", "author": "Nicholas Kardaras", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781250097996-L.jpg", "condition": "New"},
                    {"title": "No-Drama Discipline", "author": "Daniel J. Siegel & Tina Payne Bryson", "price": 310, "old_price": 480, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780345548047-L.jpg", "condition": "Pre-loved"},
                    {"title": "Born to Run", "author": "Christopher McDougall", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780307279187-L.jpg", "condition": "New"},
                    {"title": "The Glucose Revolution", "author": "Jessie Inchauspé", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781982179410-L.jpg", "condition": "New"}
                ]
            },
             {
                "name": "Astrology, Occult & Supernatural",
                "books": [
                    {"title": "The Only Astrology Book You'll Ever Need", "author": "Joanna Martine Woolfolk", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781589793774-L.jpg", "condition": "New"},
                    {"title": "The Secret Teachings of All Ages", "author": "Manly P. Hall", "price": 499, "old_price": 799, "discount": 38, "img": "https://covers.openlibrary.org/b/id/2982064-M.jpg", "condition": "New"},
                    {"title": "Astrology for the Soul", "author": "Jan Spiller", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780553378382-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Book of the Law", "author": "Aleister Crowley", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780877283348-L.jpg", "condition": "New"},
                    {"title": "The Kybalion", "author": "Three Initiates", "price": 179, "old_price": 250, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781603864787-L.jpg", "condition": "New"},
                    {"title": "Parker's Astrology", "author": "Julia & Derek Parker", "price": 550, "old_price": 850, "discount": 35, "img": "https://covers.openlibrary.org/b/id/13223390-M.jpg", "condition": "Pre-loved"},
                    {"title": "The Complete Book of Witchcraft", "author": "Raymond Buckland", "price": 389, "old_price": 550, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780875420509-L.jpg", "condition": "New"},
                    {"title": "The Demon-Haunted World", "author": "Carl Sagan", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780345409461-L.jpg", "condition": "Pre-loved"},
                    {"title": "Anatomy of the Spirit", "author": "Caroline Myss", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780609800140-L.jpg", "condition": "New"},
                    {"title": "The Occult: A History", "author": "Colin Wilson", "price": 420, "old_price": 620, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780812901924-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Inner Sky", "author": "Steven Forrest", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/id/6988688-M.jpg", "condition": "New"},
                    {"title": "The Witching Hour", "author": "Anne Rice", "price": 369, "old_price": 599, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780394587868-L.jpg", "condition": "Pre-loved"}
                ]
            },
            {
                "name": "History & Politics",
                "books": [
                    {"title": "Sapiens", "author": "Yuval Noah Harari", "price": 249, "old_price": 499, "discount": 50, "img": "https://covers.openlibrary.org/b/isbn/9780062316110-L.jpg", "condition": "Pre-loved"},
                    {"title": "Guns, Germs, and Steel", "author": "Jared Diamond", "price": 450, "old_price": 699, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780393317558-L.jpg", "condition": "New"},
                    {"title": "The Silk Roads", "author": "Peter Frankopan", "price": 499, "old_price": 799, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9781101912379-L.jpg", "condition": "New"},
                    {"title": "India After Gandhi", "author": "Ramachandra Guha", "price": 550, "old_price": 899, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780060198817-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Anarchy", "author": "William Dalrymple", "price": 499, "old_price": 699, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781635573954-L.jpg", "condition": "New"},
                    {"title": "Why Nations Fail", "author": "Daron Acemoglu & James A. Robinson", "price": 480, "old_price": 699, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780307719218-L.jpg", "condition": "Pre-loved"},
                    {"title": "Diplomacy", "author": "Henry Kissinger", "price": 650, "old_price": 999, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780671659912-L.jpg", "condition": "New"},
                    {"title": "On Tyranny", "author": "Timothy Snyder", "price": 220, "old_price": 350, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780804190114-L.jpg", "condition": "New"},
                    {"title": "The Light That Failed", "author": "Ivan Krastev & Stephen Holmes", "price": 420, "old_price": 599, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781635573954-L.jpg", "condition": "Pre-loved"},
                    {"title": "Postwar: A History of Europe Since 1945", "author": "Tony Judt", "price": 599, "old_price": 899, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781594200656-L.jpg", "condition": "New"},
                    {"title": "The Origins of Political Order", "author": "Francis Fukuyama", "price": 460, "old_price": 650, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780374533229-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Dictator's Handbook", "author": "Bruce Bueno de Mesquita & Alastair Smith", "price": 380, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781610390446-L.jpg", "condition": "New"}
                ]
            },
             {
                "name": "Science, Nature & Technology",
                "books": [
                    {"title": "The Selfish Gene", "author": "Richard Dawkins", "price": 349, "old_price": 550, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780199291151-L.jpg", "condition": "New"},
                    {"title": "A Brief History of Time", "author": "Stephen Hawking", "price": 299, "old_price": 450, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780553380163-L.jpg", "condition": "Pre-loved"},
                    {"title": "Cosmos", "author": "Carl Sagan", "price": 389, "old_price": 599, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780345331359-L.jpg", "condition": "New"},
                    {"title": "Astrophysics for People in a Hurry", "author": "Neil deGrasse Tyson", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780393609394-L.jpg", "condition": "New"},
                    {"title": "The Gene: An Intimate History", "author": "Siddhartha Mukherjee", "price": 450, "old_price": 699, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9781476733500-L.jpg", "condition": "Pre-loved"},
                    {"title": "Entangled Life", "author": "Merlin Sheldrake", "price": 369, "old_price": 520, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780525510314-L.jpg", "condition": "New"},
                    {"title": "What If?", "author": "Randall Munroe", "price": 320, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780544272996-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Hidden Life of Trees", "author": "Peter Wohlleben", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781771642484-L.jpg", "condition": "New"},
                    {"title": "Algorithms to Live By", "author": "Brian Christian & Tom Griffiths", "price": 359, "old_price": 550, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781627790369-L.jpg", "condition": "New"},
                    {"title": "The Elegant Universe", "author": "Brian Greene", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780393058581-L.jpg", "condition": "Pre-loved"},
                    {"title": "Life 3.0", "author": "Max Tegmark", "price": 380, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781101946596-L.jpg", "condition": "New"},
                    {"title": "Six Easy Pieces", "author": "Richard P. Feynman", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780465025275-L.jpg", "condition": "Pre-loved"}
                    ]
            },
              {
                "name": "Travel, Culture & Lifestyle",
                "books": [
                    {"title": "Eat, Pray, Love", "author": "Elizabeth Gilbert", "price": 289, "old_price": 450, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780143038412-L.jpg", "condition": "New"},
                    {"title": "In A Sunburned Country", "author": "Bill Bryson", "price": 320, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780767903868-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Geography of Bliss", "author": "Eric Weiner", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780446580267-L.jpg", "condition": "New"},
                    {"title": "Vagabonding", "author": "Rolf Potts", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780812992182-L.jpg", "condition": "New"},
                    {"title": "Into the Wild", "author": "Jon Krakauer", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780385486804-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Little Book of Hygge", "author": "Meik Wiking", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/id/8464293-L.jpg", "condition": "New"},
                    {"title": "Lands of Lost Borders", "author": "Kate Harris", "price": 349, "old_price": 499, "discount": 30, "img": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1553539919i/41155177.jpg", "condition": "New"},
                    {"title": "The Art of Travel", "author": "Alain de Botton", "price": 299, "old_price": 420, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780375725357-L.jpg", "condition": "Pre-loved"},
                    {"title": "On the Road", "author": "Jack Kerouac", "price": 250, "old_price": 399, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780140042597-L.jpg", "condition": "New"},
                    {"title": "Shantaram", "author": "Gregory David Roberts", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780312330538-L.jpg", "condition": "Pre-loved"},
                    {"title": "Under the Tuscan Sun", "author": "Frances Mayes", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/id/468416-M.jpg", "condition": "New"},
                    {"title": "Wild: From Lost to Found on the Pacific Crest Trail", "author": "Cheryl Strayed", "price": 330, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780307592736-L.jpg", "condition": "Pre-loved"}
                    ]
            },
              {
                "name":  "Coffee Table",
                "books": [
                    {"title": "National Geographic The Photographs", "author": "Leah Bendavid-Val", "price": 1299, "old_price": 1999, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780792270140-L.jpg", "condition": "New"},
                    {"title": "The Bucket List: 1000 Adventures Big & Small", "author": "Kath Stathers", "price": 999, "old_price": 1499, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780789332691-L.jpg", "condition": "New"},
                    {"title": "Humans of New York", "author": "Brandon Stanton", "price": 850, "old_price": 1250, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781250038821-L.jpg", "condition": "Pre-loved"},
                    {"title": "Accidentally Wes Anderson", "author": "Wally Koval", "price": 1100, "old_price": 1600, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780316492737-L.jpg", "condition": "New"},
                    {"title": "Architectural Digest at 100", "author": "Architectural Digest", "price": 2199, "old_price": 3200, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781419733338-L.jpg", "condition": "New"},
                    {"title": "Overview: A New Way of Looking at Earth", "author": "Benjamin Grant", "price": 1350, "old_price": 1899, "discount": 28, "img": "https://m.media-amazon.com/images/I/71LAe7QhWNL._AC_UF1000,1000_QL80_.jpg", "condition": "Pre-loved"},
                    {"title": "Annie Leibovitz at Work", "author": "Annie Leibovitz", "price": 1850, "old_price": 2500, "discount": 26, "img": "https://covers.openlibrary.org/b/isbn/9780375505102-L.jpg", "condition": "New"},
                    {"title": "Planet Earth II", "author": "Stephen Moss", "price": 1050, "old_price": 1500, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781849909655-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Art of Game of Thrones", "author": "Deborah Riley", "price": 1499, "old_price": 2200, "discount": 31, "img": "https://m.media-amazon.com/images/I/81VTYVAY2+L._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
                    {"title": "Sneaker Freaker: The Ultimate Sneaker Book", "author": "Simon Wood", "price": 1250, "old_price": 1750, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9783836572231-L.jpg", "condition": "New"},
                    {"title": "Van Gogh: The Complete Paintings", "author": "Ingo F. Walther", "price": 1599, "old_price": 2400, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9783836557153-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Travel Book: A Journey Through Every Country", "author": "Lonely Planet", "price": 1199, "old_price": 1799, "discount": 33, "img": "https://covers.openlibrary.org/b/id/12782315-M.jpg", "condition": "New"}
                    ]
            },
            
        ],
        
    },
    "business-economics": {
        "title": "Business & Economics",
        "tagline": "Ideas, strategies and money lessons from people who built things.",
        "count": "3,500",
        "subcategories": [
            {
                "name": "Entrepreneurship & Startups",
                "books": [
                    {"title": "The Lean Startup", "author": "Eric Ries", "price": 349, "old_price": 500, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780307887894-L.jpg", "condition": "New"},
                    {"title": "Zero to One", "author": "Peter Thiel", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780804139298-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Hard Thing About Hard Things", "author": "Ben Horowitz", "price": 389, "old_price": 599, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780062273208-L.jpg", "condition": "New"},
                    {"title": "Shoe Dog", "author": "Phil Knight", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781501135910-L.jpg", "condition": "Pre-loved"},
                    {"title": "Founders at Work", "author": "Jessica Livingston", "price": 420, "old_price": 650, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781430210788-L.jpg", "condition": "New"},
                    {"title": "The E-Myth Revisited", "author": "Michael E. Gerber", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9780887307287-L.jpg", "condition": "New"},
                    {"title": "Rework", "author": "Jason Fried & David Heinemeier Hansson", "price": 320, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780307463746-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Mom Test", "author": "Rob Fitzpatrick", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/id/10660557-M.jpg", "condition": "New"},
                    {"title": "Sprint", "author": "Jake Knapp", "price": 359, "old_price": 550, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781501121746-L.jpg", "condition": "Pre-loved"},
                    {"title": "Traction", "author": "Gabriel Weinberg & Justin Mares", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781591848363-L.jpg", "condition": "New"},
                    {"title": "The $100 Startup", "author": "Chris Guillebeau", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780307951526-L.jpg", "condition": "Pre-loved"},
                    {"title": "Company of One", "author": "Paul Jarvis", "price": 310, "old_price": 480, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781328972354-L.jpg", "condition": "New"}
                ]
            },
     {
        "name": "Leadership & Management",
        "books": [
            {"title": "Good to Great", "author": "Jim Collins", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780066620992-L.jpg", "condition": "New"},
            {"title": "Leaders Eat Last", "author": "Simon Sinek", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781591845324-L.jpg", "condition": "Pre-loved"},
            {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey", "price": 299, "old_price": 499, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9780743269513-L.jpg", "condition": "New"},
            {"title": "Radical Candor", "author": "Kim Scott", "price": 379, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250103505-L.jpg", "condition": "New"},
            {"title": "Extreme Ownership", "author": "Jocko Willink & Leif Babin", "price": 369, "old_price": 520, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781250067050-L.jpg", "condition": "Pre-loved"},
            {"title": "Principles: Life and Work", "author": "Ray Dalio", "price": 450, "old_price": 699, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9781501124020-L.jpg", "condition": "New"},
            {"title": "Start with Why", "author": "Simon Sinek", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781591846406-L.jpg", "condition": "Pre-loved"},
            {"title": "The Effective Executive", "author": "Peter F. Drucker", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780060833459-L.jpg", "condition": "New"},
            {"title": "Drive: The Surprising Truth About What Motivates Us", "author": "Daniel H. Pink", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781594488849-L.jpg", "condition": "Pre-loved"},
            {"title": "The Making of a Manager", "author": "Julie Zhuo", "price": 359, "old_price": 550, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780735219564-L.jpg", "condition": "New"},
            {"title": "Turn the Ship Around!", "author": "L. David Marquet", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781591886020-L.jpg", "condition": "New"},
            {"title": "Multipliers: How the Best Leaders Make Everyone Smarter", "author": "Liz Wiseman", "price": 380, "old_price": 580, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780061964398-L.jpg", "condition": "Pre-loved"}
        ]
      },
      {
        "name": "Finance & Stock Market Investing",
        "books": [
                {"title": "The Intelligent Investor", "author": "Benjamin Graham", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780060555665-L.jpg", "condition": "New"},
                {"title": "The Psychology of Money", "author": "Morgan Housel", "price": 260, "old_price": 399, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780857197689-L.jpg", "condition": "New"},
                {"title": "Rich Dad Poor Dad", "author": "Robert T. Kiyosaki", "price": 299, "old_price": 499, "discount": 40, "img": "https://covers.openlibrary.org/b/isbn/9781612680194-L.jpg", "condition": "Pre-loved"},
                {"title": "One Up On Wall Street", "author": "Peter Lynch", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780743200400-L.jpg", "condition": "New"},
                {"title": "A Random Walk Down Wall Street", "author": "Burton G. Malkiel", "price": 420, "old_price": 650, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780393330335-L.jpg", "condition": "Pre-loved"},
                {"title": "Common Stocks and Uncommon Profits", "author": "Philip A. Fisher", "price": 389, "old_price": 550, "discount": 29, "img": "https://covers.openlibrary.org/b/id/1885917-M.jpg", "condition": "New"},
                {"title": "The Little Book of Common Sense Investing", "author": "John C. Bogle", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781119404507-L.jpg", "condition": "New"},
                {"title": "Principles for Navigating Big Debt Crises", "author": "Ray Dalio", "price": 499, "old_price": 799, "discount": 38, "img": "https://covers.openlibrary.org/b/id/11980955-M.jpg", "condition": "Pre-loved"},
                {"title": "The Dhandho Investor", "author": "Mohnish Pabrai", "price": 330, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780470043899-L.jpg", "condition": "New"},
                {"title": "Security Analysis", "author": "Benjamin Graham & David Dodd", "price": 599, "old_price": 899, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780071592536-L.jpg", "condition": "Pre-loved"},
                {"title": "Stock to Riches", "author": "Parag Parikh", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/id/12507832-M.jpg", "condition": "New"},
                {"title": "The Essays of Warren Buffett", "author": "Lawrence A. Cunningham", "price": 379, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/id/13202902-M.jpg", "condition": "Pre-loved"}
            ]
    },
      {
        "name": "Marketing & Branding",
                "books": [
                {"title": "Contagious: Why Things Catch On", "author": "Jonah Berger", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781451686579-L.jpg", "condition": "New"},
                {"title": "Building a StoryBrand", "author": "Donald Miller", "price": 349, "old_price": 550, "discount": 37, "img": "https://covers.openlibrary.org/b/isbn/9780718033323-L.jpg", "condition": "New"},
                {"title": "Influence: The Psychology of Persuasion", "author": "Robert B. Cialdini", "price": 389, "old_price": 599, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780061241895-L.jpg", "condition": "Pre-loved"},
                {"title": "Purple Cow", "author": "Seth Godin", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780141016405-L.jpg", "condition": "New"},
                {"title": "Positioning: The Battle for Your Mind", "author": "Al Ries & Jack Trout", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780071373586-L.jpg", "condition": "Pre-loved"},
                {"title": "This Is Marketing", "author": "Seth Godin", "price": 359, "old_price": 520, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780525540830-L.jpg", "condition": "New"},
                {"title": "Hooked: How to Build Habit-Forming Products", "author": "Nir Eyal", "price": 319, "old_price": 480, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781591847786-L.jpg", "condition": "Pre-loved"},
                {"title": "Made to Stick", "author": "Chip Heath & Dan Heath", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781400064281-L.jpg", "condition": "New"},
                {"title": "Buyology", "author": "Martin Lindstrom", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9780385523882-L.jpg", "condition": "Pre-loved"},
                {"title": "To Sell Is Human", "author": "Daniel H. Pink", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781594631900-L.jpg", "condition": "New"},
                {"title": "The 22 Immutable Laws of Marketing", "author": "Al Ries & Jack Trout", "price": 249, "old_price": 350, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780887306662-L.jpg", "condition": "New"},
                {"title": "Jab, Jab, Jab, Right Hook", "author": "Gary Vaynerchuk", "price": 370, "old_price": 550, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780062273062-L.jpg", "condition": "Pre-loved"}
                ]
      },
      {
        "name": "Economics & Global Affairs",
     "books": [
  {"title": "Freakonomics", "author": "Steven D. Levitt & Stephen J. Dubner", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780060731328-L.jpg", "condition": "New"},
  {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "price": 359, "old_price": 549, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780374533557-L.jpg", "condition": "New"},
  {"title": "Capital in the Twenty-First Century", "author": "Thomas Piketty", "price": 599, "old_price": 899, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780674430006-L.jpg", "condition": "Pre-loved"},
  {"title": "Nudge", "author": "Richard H. Thaler & Cass R. Sunstein", "price": 320, "old_price": 499, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780143115267-L.jpg", "condition": "New"},
  {"title": "The Wealth of Nations", "author": "Adam Smith", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780140436150-L.jpg", "condition": "Pre-loved"},
  {"title": "Factfulness", "author": "Hans Rosling", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781250107817-L.jpg", "condition": "New"},
  {"title": "Economic Hit Man", "author": "John Perkins", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781576753019-L.jpg", "condition": "Pre-loved"},
  {"title": "Poor Economics", "author": "Abhijit V. Banerjee & Esther Duflo", "price": 330, "old_price": 480, "discount": 31, "img": "https://m.media-amazon.com/images/I/81tvfBb-3gL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
  {"title": "The Undercover Economist", "author": "Tim Harford", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780143037842-L.jpg", "condition": "New"},
  {"title": "Global Inequality", "author": "Branko Milanovic", "price": 410, "old_price": 599, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780674737136-L.jpg", "condition": "Pre-loved"},
  {"title": "The World Is Flat", "author": "Thomas L. Friedman", "price": 380, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780374292881-L.jpg", "condition": "Pre-loved"},
  {"title": "Narrative Economics", "author": "Robert J. Shiller", "price": 399, "old_price": 580, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780691182292-L.jpg", "condition": "New"}
]
      },
      {
        "name": "Productivity & Time Management",
"books": [
  {"title": "Atomic Habits", "author": "James Clear", "price": 299, "old_price": 459, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780735211292-L.jpg", "condition": "New"},
  {"title": "Deep Work", "author": "Cal Newport", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781455586691-L.jpg", "condition": "Pre-loved"},
  {"title": "Getting Things Done", "author": "David Allen", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780142000281-L.jpg", "condition": "New"},
  {"title": "The 4-Hour Workweek", "author": "Timothy Ferriss", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780307465351-L.jpg", "condition": "Pre-loved"},
  {"title": "Eat That Frog!", "author": "Brian Tracy", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781576754221-L.jpg", "condition": "New"},
  {"title": "Make Time", "author": "Jake Knapp & John Zeratsky", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780525572428-L.jpg", "condition": "New"},
  {"title": "Essentialism", "author": "Greg McKeown", "price": 289, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780804137386-L.jpg", "condition": "Pre-loved"},
  {"title": "The One Thing", "author": "Gary Keller & Jay Papasan", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781885167774-L.jpg", "condition": "New"},
  {"title": "Digital Minimalism", "author": "Cal Newport", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780525536512-L.jpg", "condition": "Pre-loved"},
  {"title": "Building a Second Brain", "author": "Tiago Forte", "price": 350, "old_price": 520, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781982167387-L.jpg", "condition": "New"},
  {"title": "The 80/20 Principle", "author": "Richard Koch", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780385491747-L.jpg", "condition": "Pre-loved"},
  {"title": "Four Thousand Weeks", "author": "Oliver Burkeman", "price": 340, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/id/14840765-M.jpg", "condition": "New"}
]
      },
      {
        "name": "Career & Professional Development",
"books": [
  {"title": "So Good They Can't Ignore You", "author": "Cal Newport", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781455509126-L.jpg", "condition": "New"},
  {"title": "Never Split the Difference", "author": "Chris Voss", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780062407801-L.jpg", "condition": "Pre-loved"},
  {"title": "Designing Your Life", "author": "Bill Burnett & Dave Evans", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781101875322-L.jpg", "condition": "New"},
  {"title": "Mindset: The New Psychology of Success", "author": "Carol S. Dweck", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9780345472328-L.jpg", "condition": "New"},
  {"title": "Crucial Conversations", "author": "Kerry Patterson", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780071401944-L.jpg", "condition": "Pre-loved"},
  {"title": "What Color Is Your Parachute?", "author": "Richard N. Bolles", "price": 379, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781607746621-L.jpg", "condition": "New"},
  {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780671027032-L.jpg", "condition": "Pre-loved"},
  {"title": "Pivot: The Only Move That Matters", "author": "Jenny Blake", "price": 330, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781591848202-L.jpg", "condition": "New"},
  {"title": "Working Identity", "author": "Herminia Ibarra", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781578517787-L.jpg", "condition": "Pre-loved"},
  {"title": "Linchpin", "author": "Seth Godin", "price": 299, "old_price": 420, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781591843160-L.jpg", "condition": "New"},
  {"title": "Thanks for the Feedback", "author": "Douglas Stone & Sheila Heen", "price": 359, "old_price": 520, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780670014668-L.jpg", "condition": "New"},
  {"title": "The First 90 Days", "author": "Michael D. Watkins", "price": 389, "old_price": 580, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781422188613-L.jpg", "condition": "Pre-loved"}
]
      },
      {
        "name": "Case Studies & Business Biographies",
            "books": [
            {"title": "Steve Jobs", "author": "Walter Isaacson", "price": 449, "old_price": 699, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9781451648539-L.jpg", "condition": "New"},
            {"title": "Shoe Dog", "author": "Phil Knight", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781501135910-L.jpg", "condition": "Pre-loved"},
            {"title": "Elon Musk", "author": "Ashlee Vance", "price": 379, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780062301239-L.jpg", "condition": "New"},
            {"title": "Bad Blood: Secrets and Lies in a Silicon Valley Startup", "author": "John Carreyrou", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781524731656-L.jpg", "condition": "Pre-loved"},
            {"title": "The Everything Store: Jeff Bezos and the Age of Amazon", "author": "Brad Stone", "price": 359, "old_price": 520, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780316219266-L.jpg", "condition": "New"},
            {"title": "Ride of a Lifetime", "author": "Robert Iger", "price": 389, "old_price": 580, "discount": 33, "img": "https://covers.openlibrary.org/b/id/13542506-M.jpg", "condition": "New"},
            {"title": "Creativity, Inc.", "author": "Ed Catmull", "price": 340, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780812993011-L.jpg", "condition": "Pre-loved"},
            {"title": "No Rules Rules: Netflix and the Culture of Reinvention", "author": "Reed Hastings & Erin Meyer", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781984877864-L.jpg", "condition": "New"},
            {"title": "Brotopia", "author": "Emily Chang", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780735213531-L.jpg", "condition": "Pre-loved"},
            {"title": "Barbarians at the Gate", "author": "Bryan Burrough & John Helyar", "price": 420, "old_price": 620, "discount": 32, "img": "https://covers.openlibrary.org/b/id/14618436-M.jpg", "condition": "New"},
            {"title": "Super Pumped: The Battle for Uber", "author": "Mike Isaac", "price": 330, "old_price": 480, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780393652246-L.jpg", "condition": "Pre-loved"},
            {"title": "That Will Never Work: The Birth of Netflix", "author": "Marc Randolph", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/id/14707319-M.jpg", "condition": "New"}
        ]
      }
    ]
    },
    "children": {
        "title": "Children's Books",
        "tagline": "Picture books, early readers and adventures for growing imaginations.",
        "count": "1,800",
        "subcategories": [
                {
                "name":"Picture Books (0-2 Years)",
                "books": [
                {"title": "The Very Hungry Caterpillar", "author": "Eric Carle", "price": 249, "old_price": 350, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780399226908-L.jpg", "condition": "New"},
                {"title": "Where Is Baby's Belly Button?", "author": "Karen Katz", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780689835636-L.jpg", "condition": "New"},
                {"title": "Goodnight Moon", "author": "Margaret Wise Brown", "price": 220, "old_price": 320, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780060775858-L.jpg", "condition": "Pre-loved"},
                {"title": "Dear Zoo", "author": "Rod Campbell", "price": 230, "old_price": 350, "discount": 34, "img": "https://covers.openlibrary.org/b/id/754549-L.jpg", "condition": "New"},
                {"title": "Brown Bear, Brown Bear, What Do You See?", "author": "Bill Martin Jr.", "price": 210, "old_price": 299, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780805047905-L.jpg", "condition": "Pre-loved"},
                {"title": "Press Here", "author": "Hervé Tullet", "price": 260, "old_price": 399, "discount": 35, "img": "https://covers.openlibrary.org/b/id/10541796-M.jpg", "condition": "New"},
                {"title": "Peek-a-Who?", "author": "Nina Laden", "price": 180, "old_price": 260, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780811826013-L.jpg", "condition": "Pre-loved"},
                {"title": "Giraffes Can't Dance", "author": "Giles Andreae", "price": 240, "old_price": 350, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780545392556-L.jpg", "condition": "New"},
                {"title": "Guess How Much I Love You", "author": "Sam McBratney", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780763642648-L.jpg", "condition": "Pre-loved"},
                {"title": "Chicka Chicka Boom Boom", "author": "Bill Martin Jr. & John Archambault", "price": 230, "old_price": 330, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781442435001-L.jpg", "condition": "New"},
                {"title": "Where the Wild Things Are", "author": "Maurice Sendak", "price": 270, "old_price": 399, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780060254926-L.jpg", "condition": "New"},
                {"title": "Moo, Baa, La La La!", "author": "Sandra Boynton", "price": 190, "old_price": 280, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780671449018-L.jpg", "condition": "Pre-loved"}
                ]
            },
            {
                "name":"Early Readers (3-5 Years)",
                "books": [
                {"title": "The Cat in the Hat", "author": "Dr. Seuss", "price": 230, "old_price": 350, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780394800011-L.jpg", "condition": "New"},
                {"title": "Don't Let the Pigeon Drive the Bus!", "author": "Mo Willems", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/id/6790602-M.jpg", "condition": "New"},
                {"title": "Green Eggs and Ham", "author": "Dr. Seuss", "price": 220, "old_price": 330, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780394800165-L.jpg", "condition": "Pre-loved"},
                {"title": "Pete the Cat: I Love My White Shoes", "author": "Eric Litwin", "price": 240, "old_price": 350, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780061906220-L.jpg", "condition": "New"},
                {"title": "Frog and Toad Are Friends", "author": "Arnold Lobel", "price": 210, "old_price": 299, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780064440202-L.jpg", "condition": "Pre-loved"},
                {"title": "Go, Dog. Go!", "author": "P.D. Eastman", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780394800202-L.jpg", "condition": "New"},
                {"title": "If You Give a Mouse a Cookie", "author": "Laura Numeroff", "price": 235, "old_price": 350, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780060245863-L.jpg", "condition": "Pre-loved"},
                {"title": "The Gruffalo", "author": "Julia Donaldson", "price": 260, "old_price": 399, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780333710937-L.jpg", "condition": "New"},
                {"title": "Room on the Broom", "author": "Julia Donaldson", "price": 250, "old_price": 370, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780333903384-L.jpg", "condition": "Pre-loved"},
                {"title": "There Is a Bird on Your Head!", "author": "Mo Willems", "price": 225, "old_price": 320, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781423106869-L.jpg", "condition": "New"},
                {"title": "Llama Llama Red Pajama", "author": "Anna Dewdney", "price": 240, "old_price": 360, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780670059836-L.jpg", "condition": "Pre-loved"},
                {"title": "Are You My Mother?", "author": "P.D. Eastman", "price": 205, "old_price": 299, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780394800189-L.jpg", "condition": "New"}
                ]
            },
           
            {
                "name": "Chapter Books (6-8 Years)",

                "books": [
                {"title": "The Magic Tree House: Dinosaurs Before Dark", "author": "Mary Pope Osborne", "price": 210, "old_price": 299, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780679824244-L.jpg", "condition": "New"},
                {"title": "Zoey and Sassafras: Dragons and Marshmallows", "author": "Asia Citro", "price": 240, "old_price": 350, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781635920369-L.jpg", "condition": "New"},
                {"title": "Junie B. Jones and the Stupid Smelly Bus", "author": "Barbara Park", "price": 199, "old_price": 280, "discount": 29, "img": "https://covers.openlibrary.org/b/id/15088460-M.jpg", "condition": "Pre-loved"},
                {"title": "Mercy Watson to the Rescue", "author": "Kate DiCamillo", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780763645045-L.jpg", "condition": "New"},
                {"title": "My Weird School: Miss Daisy Is Crazy!", "author": "Dan Gutman", "price": 190, "old_price": 275, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780060507008-L.jpg", "condition": "Pre-loved"},
                {"title": "Ivy + Bean", "author": "Annie Barrows", "price": 220, "old_price": 320, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780811849098-L.jpg", "condition": "New"},
                {"title": "Amelia Bedelia", "author": "Peggy Parish", "price": 185, "old_price": 270, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780064441551-L.jpg", "condition": "Pre-loved"},
                {"title": "The Bad Guys", "author": "Aaron Blabey", "price": 260, "old_price": 399, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780545912402-L.jpg", "condition": "New"},
                {"title": "Flat Stanley", "author": "Jeff Brown", "price": 195, "old_price": 280, "discount": 30, "img": "https://covers.openlibrary.org/b/id/6941404-M.jpg", "condition": "Pre-loved"},
                {"title": "Nate the Great", "author": "Marjorie Weinman Sharmat", "price": 205, "old_price": 299, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780440461265-L.jpg", "condition": "New"},
                {"title": "Narwhal: Unicorn of the Sea", "author": "Ben Clanton", "price": 230, "old_price": 340, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781101918265-L.jpg", "condition": "Pre-loved"},
                {"title": "Dragon Masters: Rise of the Earth Dragon", "author": "Tracey West", "price": 215, "old_price": 310, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780545646239-L.jpg", "condition": "New"}
                ]
            },
            {
                "name":"Middle Grade (9-12 Years)",
                "books": [
                {"title": "Wonder", "author": "R.J. Palacio", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780375869020-L.jpg", "condition": "New"},
                {"title": "Percy Jackson & the Olympians: The Lightning Thief", "author": "Rick Riordan", "price": 280, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780786838653-L.jpg", "condition": "New"},
                {"title": "Diary of a Wimpy Kid", "author": "Jeff Kinney", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780810993136-L.jpg", "condition": "Pre-loved"},
                {"title": "Matilda", "author": "Roald Dahl", "price": 240, "old_price": 350, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780141301068-L.jpg", "condition": "New"},
                {"title": "Holes", "author": "Louis Sachar", "price": 260, "old_price": 399, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9780375869020-L.jpg", "condition": "Pre-loved"},
                {"title": "Keeper of the Lost Cities", "author": "Shannon Messenger", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781442445932-L.jpg", "condition": "New"},
                {"title": "Bridge to Terabithia", "author": "Katherine Paterson", "price": 220, "old_price": 320, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780064401845-L.jpg", "condition": "Pre-loved"},
                {"title": "The One and Only Ivan", "author": "Katherine Applegate", "price": 270, "old_price": 399, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780061992254-L.jpg", "condition": "New"},
                {"title": "Escape from Mr. Lemoncello's Library", "author": "Chris Grabenstein", "price": 265, "old_price": 380, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780307931474-L.jpg", "condition": "Pre-loved"},
                {"title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "price": 245, "old_price": 360, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780312367541-L.jpg", "condition": "New"},
                {"title": "Charlie and the Chocolate Factory", "author": "Roald Dahl", "price": 235, "old_price": 340, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780142410318-L.jpg", "condition": "Pre-loved"},
                {"title": "The Mysterious Benedict Society", "author": "Trenton Lee Stewart", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780316003957-L.jpg", "condition": "New"}
                ]
            },
            {
                "name":"Activity & Colouring Books",
                "books": [
                {"title": "Ultimate Sticker Book: Animals", "author": "DK Publishing", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/id/800369-L.jpg", "condition": "New"},
                {"title": "Wreck This Journal", "author": "Keri Smith", "price": 280, "old_price": 420, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780399533464-L.jpg", "condition": "New"},
                {"title": "My First Learn-to-Write Workbook", "author": "Crystal Radke", "price": 220, "old_price": 320, "discount": 31, "img": "https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcRwOz31F-S_B5Q88ELxZCmJha6tQH1HfBDmF2RD0EyaBlzP997lM0wojpXiPXowABA_OxeXlN7vHOgBMkzpeB4iPhyl0728oFjjwqF2RH31 ", "condition": "New"},
                {"title": "Brain Quest Workbook: Grade 1", "author": "Evonne Lum", "price": 350, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780761149149-L.jpg", "condition": "New"},
                {"title": "The Highlights Book of Things to Do", "author": "Highlights for Children", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781684376421-L.jpg", "condition": "New"},
                {"title": "Paint by Sticker Kids: Zoo Animals", "author": "Workman Publishing", "price": 260, "old_price": 380, "discount": 32, "img": "https://m.media-amazon.com/images/I/51xfUm50T8L._SX342_SY445_FMwebp_.jpg", "condition": "New"},
                {"title": "How to Draw 101 Animals", "author": "Dan Green", "price": 180, "old_price": 260, "discount": 31, "img": "https://covers.openlibrary.org/b/id/14786495-M.jpg ", "condition": "New"},
                {"title": "The Reverse Coloring Book", "author": "Kendra Norton", "price": 299, "old_price": 450, "discount": 33, "img": "https://m.media-amazon.com/images/I/510Is4YPcwL._SX342_SY445_FMwebp_.jpg", "condition": "New"},
                {"title": "Cut and Paste Skills Workbook", "author": "School Zone", "price": 150, "old_price": 220, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780887432682-L.jpg", "condition": "New"},
                {"title": "Awesome Science Experiments for Kids", "author": "Crystal Chatterton", "price": 320, "old_price": 480, "discount": 33, "img": "https://m.media-amazon.com/images/I/41a9PvS7EQL._SX342_SY445_FMwebp_.jpg", "condition": "New"},
                {"title": "Unicorn Coloring Book for Kids", "author": "Silly Bear Books", "price": 170, "old_price": 250, "discount": 32, "img": "https://m.media-amazon.com/images/I/71CQ-6rQYnL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
                {"title": "Fun Maze Book for Kids", "author": "DP Kids", "price": 160, "old_price": 230, "discount": 30, "img": "https://m.media-amazon.com/images/I/51EvbrOlM9L._SX342_SY445_FMwebp_.jpg", "condition": "New"}
                ]
            },
            {
                "name":"Story Books",
                "books": [
                {"title": "The Secret Garden", "author": "Frances Hodgson Burnett", "price": 220, "old_price": 320, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780064401883-L.jpg", "condition": "Pre-loved"},
                {"title": "Charlotte's Web", "author": "E.B. White", "price": 240, "old_price": 350, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780064400558-L.jpg", "condition": "New"},
                {"title": "Aesop's Fables", "author": "Aesop", "price": 180, "old_price": 260, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780007350841-L.jpg", "condition": "Pre-loved"},
                {"title": "Grimm's Fairy Tales", "author": "Jacob & Wilhelm Grimm", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780007350889-L.jpg", "condition": "New"},
                {"title": "The Panchatantra", "author": "Vishnu Sharma", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/id/7061931-M.jpg", "condition": "New"},
                {"title": "The Giving Tree", "author": "Shel Silverstein", "price": 230, "old_price": 330, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780060256654-L.jpg", "condition": "Pre-loved"},
                {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "price": 210, "old_price": 310, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780141321073-L.jpg", "condition": "New"},
                {"title": "Peter Pan", "author": "J.M. Barrie", "price": 200, "old_price": 290, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780141322575-L.jpg", "condition": "Pre-loved"},
                {"title": "The Velveteen Rabbit", "author": "Margery Williams", "price": 190, "old_price": 280, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780140502015-L.jpg", "condition": "New"},
                {"title": "Malgudi Days", "author": "R.K. Narayan", "price": 260, "old_price": 380, "discount": 32, "img": "https://covers.openlibrary.org/b/id/9400361-M.jpg", "condition": "Pre-loved"},
                {"title": "The Tale of Peter Rabbit", "author": "Beatrix Potter", "price": 175, "old_price": 250, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780723247708-L.jpg", "condition": "New"},
                {"title": "The Wind in the Willows", "author": "Kenneth Grahame", "price": 225, "old_price": 330, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780143039099-L.jpg", "condition": "Pre-loved"}
                ]
            },                       
            {
                "name":"Work Books",
                "books": [
                {"title": "Kumon Grade 1 Addition", "author": "Kumon Publishing", "price": 280, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781933241517-L.jpg", "condition": "New"},
                {"title": "School Zone - Big Preschool Workbook", "author": "School Zone", "price": 350, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780887431456-L.jpg", "condition": "New"},
                {"title": "Spectrum Math Workbook, Grade 3", "author": "Spectrum", "price": 320, "old_price": 450, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781483808710-L.jpg", "condition": "New"},
                {"title": "DK Workbooks: Language Arts, Kindergarten", "author": "DK Publishing", "price": 230, "old_price": 330, "discount": 30, "img": "https://covers.openlibrary.org/b/id/12578218-M.jpg", "condition": "New"},
                {"title": "180 Days of Social Studies for Grade 2", "author": "Teacher Created Materials", "price": 399, "old_price": 580, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781425813932-L.jpg", "condition": "New"},
                {"title": "Smart Practice Workbook: First Grade", "author": "Scholastic", "price": 360, "old_price": 520, "discount": 31, "img": "https://m.media-amazon.com/images/I/714j1BxUKjL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
                {"title": "Kumon Grade 2 Reading", "author": "Kumon Publishing", "price": 290, "old_price": 420, "discount": 31, "img": "https://m.media-amazon.com/images/I/71ZhCiPvRCL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
                {"title": "Scholastic Success with Grammar, Grade 4", "author": "Scholastic", "price": 210, "old_price": 310, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780545201032-L.jpg", "condition": "New"},
                {"title": "Comprehensive Curriculum of Basic Skills, Grade 1", "author": "Thinking Kids", "price": 420, "old_price": 599, "discount": 30, "img": "https://m.media-amazon.com/images/I/91I73x9b6HL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
                {"title": "100 Words Every 1st Grader Should Know", "author": "Editors of American Heritage Dictionaries", "price": 199, "old_price": 299, "discount": 33, "img": "https://m.media-amazon.com/images/I/71Yv9rdWjxL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
                {"title": "Evan-Moor Daily Science, Grade 3", "author": "Evan-Moor", "price": 380, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781596739277-L.jpg", "condition": "New"},
                {"title": "Singapore Math, Grade 2", "author": "Thinking Kids", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781483813189-L.jpg", "condition": "New"}
                ]
            },
            {
                "name":"Comics",
                "books": [
                {"title": "Dog Man: For Whom the Ball Rolls", "author": "Dav Pilkey", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781338236590-L.jpg", "condition": "New"},
                {"title": "Smile", "author": "Raina Telgemeier", "price": 280, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780545132060-L.jpg", "condition": "Pre-loved"},
                {"title": "Captain Underpants and the Sensational Saga of Sir Stinks-A-Lot", "author": "Dav Pilkey", "price": 240, "old_price": 350, "discount": 31, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTaFCrORsyv9i_J9iL2Wxv3tffYRAlzv78CHqw4MSkoEg&s=10", "condition": "New"},
                {"title": "Guts", "author": "Raina Telgemeier", "price": 290, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780545852500-L.jpg", "condition": "Pre-loved"},
                {"title": "Big Nate: In a Class by Himself", "author": "Lincoln Peirce", "price": 230, "old_price": 330, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780061944345-L.jpg", "condition": "Pre-loved"},
                {"title": "The Adventures of Tintin: Secret of the Unicorn", "author": "Hergé", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780316358323-L.jpg", "condition": "New"},
                {"title": "Asterix the Gaul", "author": "René Goscinny & Albert Uderzo", "price": 310, "old_price": 450, "discount": 31, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLbclpaoY3uMAht7osk5OQ0TJIdws_bQNSIRulFKLzkw&s=10", "condition": "Pre-loved"},
                {"title": "Phoebe and Her Unicorn", "author": "Dana Simpson", "price": 260, "old_price": 380, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781449446208-L.jpg", "condition": "New"},
                {"title": "InvestiGators", "author": "John Patrick Green", "price": 275, "old_price": 399, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250219954-L.jpg", "condition": "New"},
                {"title": "El Deafo", "author": "Cece Bell", "price": 295, "old_price": 430, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781419712173-L.jpg", "condition": "Pre-loved"},
                {"title": "Amulet: The Stonekeeper", "author": "Kazu Kibuishi", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780439846813-L.jpg", "condition": "New"},
                {"title": "Garfield Gains Weight", "author": "Jim Davis", "price": 199, "old_price": 299, "discount": 33, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI-jebM_KY07WwHV6JLKKhJhUEHk-eFKTDLhX8bs_NQQ&s", "condition": "Pre-loved"}
                ]
            },
                       
            
        ],
             "books": [
            {"title": "The Very Hungry Caterpillar", "author": "Eric Carle", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780399226908-L.jpg", "condition": "New"},
            {"title": "Charlotte's Web", "author": "E.B. White", "price": 229, "old_price": 349, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780064400558-L.jpg", "condition": "Pre-loved"},
            {"title": "Matilda", "author": "Roald Dahl", "price": 249, "old_price": 379, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780142410370-L.jpg", "condition": "New"},
            {"title": "The Gruffalo", "author": "Julia Donaldson", "price": 179, "old_price": 279, "discount": 36, "img": "https://covers.openlibrary.org/b/isbn/9780333710930-L.jpg", "condition": "New"},
            {"title": "Panchatantra Tales", "author": "Vishnu Sharma", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781981020782-L.jpg", "condition": "Pre-loved"},
            {"title": "Winnie-the-Pooh", "author": "A.A. Milne", "price": 219, "old_price": 329, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780525444435-L.jpg", "condition": "New"},
            {"title": "The Jungle Book", "author": "Rudyard Kipling", "price": 209, "old_price": 319, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780141321021-L.jpg", "condition": "Pre-loved"},
            {"title": "Amar Chitra Katha — Birbal", "author": "ACK", "price": 149, "old_price": 220, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9788175080935-L.jpg", "condition": "New"},
        ],
    },
    "young-adult": {
        "title": "Young Adult",
        "tagline": "Big feelings, bold worlds and stories made for growing up.",
        "count": "3,200",
        "subcategories": [
            {
                "name": "Fantasy & Supernatural",
                
               "books": [
                    {"title": "The Cruel Prince", "author": "Holly Black", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780316310277-L.jpg", "condition": "New"},
                    {"title": "Six of Crows", "author": "Leigh Bardugo", "price": 389, "old_price": 550, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781627792127-L.jpg", "condition": "New"},
                    {"title": "A Court of Thorns and Roses", "author": "Sarah J. Maas", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781619634442-L.jpg", "condition": "Pre-loved"},
                    {"title": "Cinder", "author": "Marissa Meyer", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780312641894-L.jpg", "condition": "New"},
                    {"title": "Shadow and Bone", "author": "Leigh Bardugo", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780805094596-L.jpg", "condition": "Pre-loved"},
                    {"title": "Percy Jackson & the Olympians: The Lightning Thief", "author": "Rick Riordan", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780786838653-L.jpg", "condition": "New"},
                    {"title": "Cemetery Boys", "author": "Aiden Thomas", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781250250469-L.jpg", "condition": "New"},
                    {"title": "Legendborn", "author": "Tracy Deonn", "price": 369, "old_price": 520, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781534441606-L.jpg", "condition": "Pre-loved"},
                    {"title": "Carry On", "author": "Rainbow Rowell", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/id/15160759-M.jpg", "condition": "New"},
                    {"title": "House of Earth and Blood", "author": "Sarah J. Maas", "price": 450, "old_price": 699, "discount": 35, "img": "https://covers.openlibrary.org/b/isbn/9781635574043-L.jpg", "condition": "Pre-loved"},
                    {"title": "Shatter Me", "author": "Tahereh Mafi", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9780062085504-L.jpg", "condition": "New"},
                    {"title": "An Ember in the Ashes", "author": "Sabaa Tahir", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/id/14605492-M.jpg", "condition": "Pre-loved"}
                ]
            },    
            {
                "name":  "Romance & Coming-Of-Age",
                
               "books": [
                    {"title": "The Fault in Our Stars", "author": "John Green", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780525478812-L.jpg", "condition": "New"},
                    {"title": "To All the Boys I've Loved Before", "author": "Jenny Han", "price": 289, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781442426702-L.jpg", "condition": "Pre-loved"},
                    {"title": "Aristotle and Dante Discover the Secrets of the Universe", "author": "Benjamin Alire Sáenz", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781442408920-L.jpg", "condition": "New"},
                    {"title": "The Perks of Being a Wallflower", "author": "Stephen Chbosky", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780671027346-L.jpg", "condition": "Pre-loved"},
                    {"title": "Eleanor & Park", "author": "Rainbow Rowell", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781250012579-L.jpg", "condition": "New"},
                    {"title": "Looking for Alaska", "author": "John Green", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780142402511-L.jpg", "condition": "Pre-loved"},
                    {"title": "Heartstopper: Volume One", "author": "Alice Oseman", "price": 350, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781338617436-L.jpg", "condition": "New"},
                    {"title": "The Sun Is Also a Star", "author": "Nicola Yoon", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780553496680-L.jpg", "condition": "Pre-loved"},
                    {"title": "Five Feet Apart", "author": "Rachael Lippincott", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781534437333-L.jpg", "condition": "New"},
                    {"title": "Love & Gelato", "author": "Jenna Evans Welch", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781481432542-L.jpg", "condition": "Pre-loved"},
                    {"title": "Simon vs. the Homo Sapiens Agenda", "author": "Becky Albertalli", "price": 280, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780062348678-L.jpg", "condition": "New"},
                    {"title": "Counting Down with You", "author": "Tashie Bhuiyan", "price": 330, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/id/14913131-M.jpg", "condition": "Pre-loved"}
                ]
            },
            {
                "name": "Mystery & Thrillers",
                
                "books": [
                    {"title": "A Good Girl's Guide to Murder", "author": "Holly Jackson", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781984896391-L.jpg", "condition": "New"},
                    {"title": "One of Us Is Lying", "author": "Karen M. McManus", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781524714680-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Inheritance Games", "author": "Jennifer Lynn Barnes", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781368052405-L.jpg", "condition": "New"},
                    {"title": "Truly Devious", "author": "Maureen Johnson", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780062338051-L.jpg", "condition": "Pre-loved"},
                    {"title": "Sadie", "author": "Courtney Summers", "price": 330, "old_price": 480, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250105714-L.jpg", "condition": "New"},
                    {"title": "We Were Liars", "author": "E. Lockhart", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780385741262-L.jpg", "condition": "Pre-loved"},
                    {"title": "Firekeeper's Daughter", "author": "Angeline Boulley", "price": 379, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250766564-L.jpg", "condition": "New"},
                    {"title": "Ace of Spades", "author": "Faridah Àbíké-Íyímídé", "price": 359, "old_price": 520, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250800817-L.jpg", "condition": "New"},
                    {"title": "There's Someone Inside Your House", "author": "Stephanie Perkins", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9780525426011-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Agathas", "author": "Kathleen Glasgow & Liz Lawson", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/id/12927294-M.jpg", "condition": "New"},
                    {"title": "The Cheerleaders", "author": "Kara Thomas", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781524718329-L.jpg", "condition": "Pre-loved"},
                    {"title": "I Must Betray You", "author": "Ruta Sepetys", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781101998830-L.jpg", "condition": "New"}
                ]
            },
            {
                "name":"Dystopian & Sci-Fi",
                    "books": [
                    {"title": "The Hunger Games", "author": "Suzanne Collins", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780439023481-L.jpg", "condition": "New"},
                    {"title": "Divergent", "author": "Veronica Roth", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780062024022-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Maze Runner", "author": "James Dashner", "price": 289, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780385737944-L.jpg", "condition": "New"},
                    {"title": "Scythe", "author": "Neal Shusterman", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781442457690-L.jpg", "condition": "New"},
                    {"title": "Legend", "author": "Marie Lu", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780142422076-L.jpg", "condition": "Pre-loved"},
                    {"title": "Red Rising", "author": "Pierce Brown", "price": 379, "old_price": 550, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780345539786-L.jpg", "condition": "New"},
                    {"title": "Illuminae", "author": "Amie Kaufman & Jay Kristoff", "price": 399, "old_price": 599, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780553499117-L.jpg", "condition": "Pre-loved"},
                    {"title": "The Giver", "author": "Lois Lowry", "price": 220, "old_price": 350, "discount": 37, "img": "https://covers.openlibrary.org/b/id/15176861-M.jpg", "condition": "New"},
                    {"title": "Unwind", "author": "Neal Shusterman", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781416912040-L.jpg", "condition": "Pre-loved"},
                    {"title": "Warcross", "author": "Marie Lu", "price": 329, "old_price": 480, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780399547966-L.jpg", "condition": "New"},
                    {"title": "The 5th Wave", "author": "Rick Yancey", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780399162411-L.jpg", "condition": "Pre-loved"},
                    {"title": "All That's Left in the World", "author": "Erik J. Brown", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780063054974-L.jpg", "condition": "New"}
                    ]
            },
            {
                "name":"School & Friendship Drama", 
                
                    "books": [
                    {"title": "Wonder", "author": "R.J. Palacio", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780375869020-L.jpg", "condition": "New"},
                    {"title": "Geek Girl", "author": "Holly Smale", "price": 259, "old_price": 380, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9780007489442-L.jpg", "condition": "Pre-loved"},
                    {"title": "Radio Silence", "author": "Alice Oseman", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/id/12697188-M.jpg", "condition": "New"},
                    {"title": "Dork Diaries: Tales from a Not-So-Fabulous Life", "author": "Rachel Renée Russell", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9781416980063-L.jpg", "condition": "New"},
                    {"title": "Tell Me Three Things", "author": "Julie Buxbaum", "price": 289, "old_price": 420, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780553535648-L.jpg", "condition": "Pre-loved"},
                    {"title": "Stargirl", "author": "Jerry Spinelli", "price": 230, "old_price": 350, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780375822339-L.jpg", "condition": "New"},
                    {"title": "One for the Murphys", "author": "Lynda Mullaly Hunt", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/id/7244177-M.jpg", "condition": "Pre-loved"},
                    {"title": "Fish in a Tree", "author": "Lynda Mullaly Hunt", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780142426425-L.jpg", "condition": "New"},
                    {"title": "Raybearer", "author": "Jordan Ifueko", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781419739828-L.jpg", "condition": "New"},
                    {"title": "New Kid", "author": "Jerry Craft", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780062691194-L.jpg", "condition": "Pre-loved"},
                    {"title": "Roller Girl", "author": "Victoria Jamieson", "price": 299, "old_price": 420, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780525429678-L.jpg", "condition": "New"},
                    {"title": "The Field Guide to the North American Teenager", "author": "Ben Philippe", "price": 320, "old_price": 480, "discount": 33, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS_Vkl_q-wP1x44CcbPvxYfPs3v7gco0yv5L_O5WwlTidMvAj_ueIK3og&s=10", "condition": "Pre-loved"}
                    ]
            },        
            {
               "name":"Manga", 
                
                "books": [
                {"title": "Demon Slayer: Kimetsu no Yaiba, Vol. 1", "author": "Koyoharu Gotouge", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781974700523-L.jpg", "condition": "New"},
                {"title": "Jujutsu Kaisen, Vol. 1", "author": "Gege Akutami", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781974710027-L.jpg", "condition": "New"},
                {"title": "Attack on Titan, Vol. 1", "author": "Hajime Isayama", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781612620244-L.jpg", "condition": "Pre-loved"},
                {"title": "My Hero Academia, Vol. 1", "author": "Kohei Horikoshi", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781421582696-L.jpg", "condition": "New"},
                {"title": "Chainsaw Man, Vol. 1", "author": "Tatsuki Fujimoto", "price": 320, "old_price": 480, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781974709939-L.jpg", "condition": "New"},
                {"title": "Spy x Family, Vol. 1", "author": "Tatsuya Endo", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781974715466-L.jpg", "condition": "Pre-loved"},
                {"title": "Tokyo Ghoul, Vol. 1", "author": "Sui Ishida", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781421580364-L.jpg", "condition": "New"},
                {"title": "Death Note, Vol. 1", "author": "Tsugumi Ohba", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781421501680-L.jpg", "condition": "Pre-loved"},
                {"title": "Haikyu!!, Vol. 1", "author": "Haruichi Furudate", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781421587660-L.jpg", "condition": "New"},
                {"title": "One-Punch Man, Vol. 1", "author": "ONE & Yusuke Murata", "price": 299, "old_price": 420, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9781421585642-L.jpg", "condition": "Pre-loved"},
                {"title": "Blue Lock, Vol. 1", "author": "Muneyuki Kaneshiro", "price": 350, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781646516544-L.jpg", "condition": "New"},
                {"title": "Naruto, Vol. 1", "author": "Masashi Kishimoto", "price": 269, "old_price": 399, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781569319000-L.jpg", "condition": "Pre-loved"}
                ]
            },        
            {
               "name":"Inspirational & Self-Discovery", 
                "books": [
                {"title": "The Alchemist", "author": "Paulo Coelho", "price": 249, "old_price": 399, "discount": 38, "img": "https://covers.openlibrary.org/b/isbn/9780062315007-L.jpg", "condition": "New"},
                {"title": "You Are a Badass", "author": "Jen Sincero", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/id/12480026-M.jpg", "condition": "Pre-loved"},
                {"title": "Big Magic: Creative Living Beyond Fear", "author": "Elizabeth Gilbert", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781594634710-L.jpg", "condition": "New"},
                {"title": "Make Your Bed", "author": "William H. McRaven", "price": 210, "old_price": 320, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9781455570249-L.jpg", "condition": "New"},
                {"title": "Grit: The Power of Passion and Perseverance", "author": "Angela Duckworth", "price": 359, "old_price": 520, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781501111105-L.jpg", "condition": "Pre-loved"},
                {"title": "Girl, Wash Your Face", "author": "Rachel Hollis", "price": 279, "old_price": 399, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781400201655-L.jpg", "condition": "New"},
                {"title": "Tuesdays with Morrie", "author": "Mitch Albom", "price": 230, "old_price": 350, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780767905923-L.jpg", "condition": "Pre-loved"},
                {"title": "Daring Greatly", "author": "Brené Brown", "price": 340, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781592408412-L.jpg", "condition": "New"},
                {"title": "The Last Lecture", "author": "Randy Pausch", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781401323257-L.jpg", "condition": "Pre-loved"},
                {"title": "Show Your Work!", "author": "Austin Kleon", "price": 250, "old_price": 380, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780761178972-L.jpg", "condition": "New"},
                {"title": "Steal Like an Artist", "author": "Austin Kleon", "price": 240, "old_price": 360, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780761169253-L.jpg", "condition": "Pre-loved"},
                {"title": "What I Know for Sure", "author": "Oprah Winfrey", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9781250054050-L.jpg", "condition": "New"}
                ]
            },
            {
               "name":"Young Adult Non Fiction",
                "books": [
                {"title": "I Am Malala", "author": "Malala Yousafzai", "price": 299, "old_price": 450, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780316322409-L.jpg", "condition": "New"},
                {"title": "The Diary of a Young Girl", "author": "Anne Frank", "price": 199, "old_price": 299, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9780553296983-L.jpg", "condition": "Pre-loved"},
                {"title": "Just Mercy (Adapted for Young Adults)", "author": "Bryan Stevenson", "price": 329, "old_price": 499, "discount": 34, "img": "https://covers.openlibrary.org/b/isbn/9780593177044-L.jpg", "condition": "New"},
                {"title": "Stamped: Racism, Antiracism, and You", "author": "Jason Reynolds & Ibram X. Kendi", "price": 310, "old_price": 450, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780316453691-L.jpg", "condition": "New"},
                {"title": "March: Book One", "author": "John Lewis & Andrew Aydin", "price": 289, "old_price": 399, "discount": 28, "img": "https://covers.openlibrary.org/b/isbn/9781603093002-L.jpg", "condition": "Pre-loved"},
                {"title": "The 7 Habits of Highly Effective Teens", "author": "Sean Covey", "price": 349, "old_price": 499, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9781476764665-L.jpg", "condition": "New"},
                {"title": "Enrique's Journey (Young Adult Adaptation)", "author": "Sonia Nazario", "price": 299, "old_price": 420, "discount": 29, "img": "https://covers.openlibrary.org/b/isbn/9780385742573-L.jpg", "condition": "Pre-loved"},
                {"title": "Shackled", "author": "Chris Turney", "price": 270, "old_price": 380, "discount": 29, "img": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1501658905i/35898415.jpg", "condition": "New"},
                {"title": "Facing Frederick", "author": "Tonya Bolden", "price": 320, "old_price": 480, "discount": 33, "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlR3uRAsjAeAHn0H3e5sKuLXOomy2tsgYr67DgaKCnBg&s=10", "condition": "Pre-loved"},
                {"title": "Bomb: The Race to Build and Steal the World's Most Dangerous Weapon", "author": "Steve Sheinkin", "price": 339, "old_price": 499, "discount": 32, "img": "https://covers.openlibrary.org/b/isbn/9781250050649-L.jpg", "condition": "New"},
                {"title": "Free Lunch", "author": "Rex Ogle", "price": 269, "old_price": 399, "discount": 33, "img": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSebFDyjyn4FVQp_3-GyQSAuBygzfnLh9nJmKh15B2ziW0r-JI1", "condition": "Pre-loved"},
                {"title": "Being Jazz: My Life as a (Transgender) Teen", "author": "Jazz Jennings", "price": 315, "old_price": 450, "discount": 30, "img": "https://covers.openlibrary.org/b/isbn/9780399554643-L.jpg", "condition": "New"}
                ]
            },                         
        ],
    
    },
    "academic": {
        "title": "Academic",
        "tagline": "Textbooks and reference titles across every stream — priced for students.",
        "count": "5,100",
        "books": [
            {"title": "Concepts of Physics — Vol 1", "author": "H.C. Verma", "price": 299, "old_price": 425, "discount": 30, "img": "https://m.media-amazon.com/images/I/81tTJjH9A+L._UF1000,1000_QL80_.jpg", "condition": "New"},
            {"title": "NCERT Mathematics — Class 12", "author": "NCERT", "price": 120, "old_price": 175, "discount": 31, "img": "https://m.media-amazon.com/images/I/61rURoIGs1L._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
            {"title": "Organic Chemistry", "author": "Morrison & Boyd", "price": 549, "old_price": 799, "discount": 31, "img": "https://m.media-amazon.com/images/I/81NukwbFbOL._AC_UF350,350_QL50_.jpg", "condition": "Pre-loved"},
            {"title": "Introduction to Algorithms", "author": "CLRS", "price": 899, "old_price": 1299, "discount": 31, "img": "https://covers.openlibrary.org/b/isbn/9780262033848-L.jpg", "condition": "New"},
            {"title": "Engineering Mechanics", "author": "R.S. Khurmi", "price": 399, "old_price": 599, "discount": 33, "img": "https://m.media-amazon.com/images/I/81-AHU6Ys1L.jpg", "condition": "Pre-loved"},
            {"title": "Business Statistics", "author": "Ken Black", "price": 449, "old_price": 649, "discount": 31, "img": "https://m.media-amazon.com/images/I/81UCUjE0goL._AC_UF1000,1000_QL80_.jpg", "condition": "New"},
            {"title": "Cell Biology & Genetics", "author": "Verma & Agarwal", "price": 379, "old_price": 549, "discount": 31, "img": "https://m.media-amazon.com/images/I/71rAaVsjQyL.jpg", "condition": "New"},
            {"title": "Principles of Economics", "author": "N. Gregory Mankiw", "price": 499, "old_price": 749, "discount": 33, "img": "https://covers.openlibrary.org/b/isbn/9781305585126-L.jpg", "condition": "Pre-loved"},
        ],
    },
    "sale": {
        "in_menu": False,
        "title": "Sale — Up to 70% Off",
        "tagline": "Hand-picked bestsellers at their lowest prices this month. Limited stock per title.",
        "count": "2,300",
        "books": [
            {"title": "The Alchemist", "author": "Paulo Coelho", "price": 129, "old_price": 399, "discount": 68, "img": "https://m.media-amazon.com/images/I/81UGPuNl7kL._UF1000,1000_QL80_.jpg", "condition": "New"},
            {"title": "1984", "author": "George Orwell", "price": 149, "old_price": 399, "discount": 63, "img": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg", "condition": "New"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 159, "old_price": 449, "discount": 65, "img": "https://covers.openlibrary.org/b/isbn/9780061120084-L.jpg", "condition": "Pre-loved"},
            {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "price": 139, "old_price": 399, "discount": 65, "img": "https://covers.openlibrary.org/b/isbn/9781612680194-L.jpg", "condition": "New"},
            {"title": "The Power of Habit", "author": "Charles Duhigg", "price": 179, "old_price": 499, "discount": 64, "img": "https://covers.openlibrary.org/b/isbn/9780812981605-L.jpg", "condition": "Pre-loved"},
            {"title": "Ikigai", "author": "Héctor García", "price": 149, "old_price": 399, "discount": 63, "img": "https://covers.openlibrary.org/b/isbn/9780143130727-L.jpg", "condition": "New"},
            {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson", "price": 159, "old_price": 449, "discount": 65, "img": "https://covers.openlibrary.org/b/isbn/9780062457714-L.jpg", "condition": "New"},
            {"title": "Wings of Fire", "author": "A.P.J. Abdul Kalam", "price": 129, "old_price": 350, "discount": 63, "img": "https://covers.openlibrary.org/b/isbn/9788173711466-L.jpg", "condition": "Pre-loved"},
        ],
    },
}