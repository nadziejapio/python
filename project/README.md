# JPG Family Library
#### Video Demo:  <https://youtu.be/pMX9Xlnl69A>
#### Description:
The project I made is all about helping my brother to list the books he has and who did he borrowed them to. It's like family library. It is meant that every user has it's own account. With this account you can add books to library's database, add people who are borrowing books from you also change the status of the books. You can see your whole library and check what is the status of specific book. You can also change the borrower in the time previous is giving it back.

Whole project is based on flask, python, html and css.

Structure is divided into 4 main parts:
- static folder - with css file and images
- templates folder - with layouts for every html route
- python file - flask app
- database file - SQLite3 data base

The page conatins several subpages with different purposes.
There are:
- index.html - the main page, on which, after logging in, you can see all your books and their statuses.
- register and login pages - you can here register new account or log in to your session
- adding book and adding person - you can put the book or new borrower to the database
- borrow - where you can pick the book and the person from base to borrow the book
- back - where you can change the status of the book to "avaliable" again
- find - where you can find out what is the status of specific book
- error - when something is not going well ;)

The database has 3 tables:
- book - where we keep info about books - what is the title, status, who is the owner, who has the book now, when status has changed
- person - here is the info about borrowers - name, surname, nickname
- users - here is all the data gathered during registration

The main app, called "app.py" is where the all commands are going on.
At the beggining I am implementing flask and session types, adding database, response and login requisition to see index.html. Login require method is wrote in "helpers.py" library.
On that page I am sending from database via python to html the list of books where the owner is logged user.
Then I am defining route requests for other pages.
On /addperson page I am checking if the nickname is already in the database. If so - you will get error message. If there is no Nickname - you will be ask for one. If this info is provided, the future borrower will be added to the base.
Similar situation is on the /addbook route. I am checking if the title exists in form and, if so, if the title is already in the base. If is not - it will be added here.
/login route - clearing the session, checking if username and password is provided. If so, checking if the user is in database. If everything goes well, you are getting logged in and session info is updated. Than you are redirected to main page.
/logout - logs you out.
Than i am defining /find route. Here you can pick a title from you books with GET method and see what is the status of the book with POST method. Here I am taking info from books and person tables.
With /borrow route I am checking if the title and the nick is provided in form. If yes - the program is updating the info in database.
/register - checking if user is already in the base, if password matches and is long enough and has numbers. If everything is clear - adds new user to database.
Last is /back route, where you can give back a book. If the tilte and nickname is provided you can give back the book or borrow it to someone else form this page.

Next step will be adding option to check what is the library of other family members and what the status of their books is.
I am also thinking about adding an option to merge input csv files with our library or to add an export csv files option.

Here I want to thank you for the please introduction to IT world. And that was cs50! ;)