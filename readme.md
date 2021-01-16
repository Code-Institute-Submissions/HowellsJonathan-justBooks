<!-- @format -->
<h1 align="center">JustBooks Website Milestone 3 Project</h1>

[View the live site here](https://just-books-final.herokuapp.com/)

This is my project for my third milestone at Code Institute. It is designed with responsiveness in mind and can be used and views on many devices. The aim of this site is to provide a place for book lovers to come and discuss, explore, build a community of great books.

<h2 align="center"><img src="https://i.ibb.co/kHhr73W/responsive-design.png"></h2>

## Contents

1. [**Aim**](#aim)
2. [**UX**](#UX)
    - [**User Stories**](#user-stories)
    - [**Design**](#Design)
    - [**Information Architecture**](#information-architecture)
    - [**Wireframes**](#wireframes)
3. [**Feature**](#features)
4. [**Possible Features to be implemented**](#Possible-Features-to-be-implemented)
5. [**Technologies Used**](#technologies-used)
6. [**Database Structure**](#database-structure)
7. [**Testing**](#testing)
    - [**Testing User Stories from UX Section**](#Testing-User-Stories-from-UX-Section)
        - [**First Time Visitors**](#first-time-visitors)
        - [**Returning Visitors**](#Returning-Visitors)
        - [**Frequest Visitors**](#Frequest-Visitors)
    - [**Further Testing**](#further-testing)
        - [**Caught and dealt with major bugs after deployment**](#Caught-and-dealt-with-major-bugs-after-deployment)
8. [**Other Notes**](#other-notes)
9. [**Deployment**](#deployment)
10. [**Credit**](#credit)

## Aim

The aim of this site is to provide a space for people who are book lovers or are just starting out reading books to come and discuss their favourites. It is aimed at people that are willing to have massive input into a community and website. Something they can directly influence themselves.

The audience for this is all ages, although due to complexity of adding certain fields only those who are proficent with computers and know how to upload files etc. Those that cannot will still be able to use the site, just not contribute as much as others.

As the owner of the site, in theory I could profit from the Amazon link on each books page if I had a valid referal code and the site was monetized and live.

## UX

-   ### User Stories

    -   #### First Time Visitor

        1. As a first time visitor, I want to be able to understand the main purpose of the site
        2. As a first time visitor, I want to be able to navigate the site with ease
        3. As a first time visitor, I want to be able to look at a particular book
        4. As a first time visitor, I want to be able to search the site for a book I want
        5. As a first time visitor, I want to be able to see where I can buy a particular book
        6. As a first time visitor, I want to be able to see what reviews books have gotten

    -   #### Returning Visitor

        1. As a returning visitor, I want to be able to add my favourite book or books
        2. As a returning visitor, I want to be able to review and discuss a particular book
        3. As a returning visitor, I want to be able to save books I want to read

    -   #### Frequest Visitor

        1. As a frequest visitor, I want to be able to see what new books there are
        2. As a frequest visitor, I want to be able to edit my reviews
        3. As a frequest visitor, I want to be able to edit my books

-   ### Design

    -   #### Colour Scheme

        -   The main colours in this site are white, a pastel blue and greys. I chose these colours because blue is a colour of wisdon, inspiration, logic and reliability. All these things relate to books quite a lot. A pastel bright blue is also eye catching and virbant enough to contrast well with black or white.

    -   #### Typography

        -   I chose to work with Roboto for all main large walls of text and Roboto Slab for titles and buttons. Both of these fonts work well together and sans serif fonts tend to be rather subtle or pleasing to the eye. While many books are not written in sans serifs they appear well on websites.

    -   #### Imagery / Layout
        -   The layout of this project was important as there can be a lot of text presented to the user. Through large reviews or synopsis's of books. To seperate these out I created many features that allowed the user to only focus on one element at the time, to prevent a user being overwhelemed by information.
        -   The only custom image that is present on the page is the front page, a parallax image of a display of coffee and books. This is a pleasing photo and can draw the users attention, breaking the page from all of the text presented.

-   ### Information Architecture

    -   To suit the needs of a first time user or a heavy user of this site, the information presented needed to be in a suitable fashion that they can focus in on a particular element rather than having to serach through endless walls of information to get what they wanted. This is why a card layout was suited best. It breaks up the webpage into sections that the user can disect and provides clear information in a concise way.

    -   A single navbar with dropdowns was also best suited for this website. Due to books having countless genres there was a need to present them in a way the user would be able to interact simply, dropdowns allowed this to happen. They can also access this information and feature from where ever they are due to the navbar being sticky to the top of the screen.

    -   Pagination. Again due to there possibly being thousands of books in the website pages are needed so the user doesn't have to endlessly scroll down to find something they want. Carousels also present this information well due to limiting how many elements appear on the screen at once.

-   ### Wireframes

    -   An album of wireframes can be found here: [Wireframes](https://ibb.co/album/6cSW4r)

## Features

-   ### User Login

    -   Users can login and register to the site to access the more personalised features

-   ### Responsive Cards

    -   All book data on pages apart from single books is presented in a responsive card design

-   ### Book Page

    -   Users have the chance to indulge in more info about a book on each books page

-   ### Store Link

    -   Each book when being added has the chance to input a correct ISBN 10, which will allow the user to click on the store button and be taken to amazons website for the book

-   ### Bookmarked

    -   Every user that is logged in can bookmark books to save them for their own uses

-   ### Manage Page

    -   Since every registered user can create books, there is also a manage page where they can view all of the books they have created. From there they can delete the books or edit them

-   ### Genre Pages

    -   There is over 20 genres to pick and choose from. Users can look for books associated with that particular genre

-   ### Search Function

    -   Users can search the database for different books, authors or ISBN's.

-   ### Reviews

    -   Users can add, edit and delete reviews for books

-   ### The site is responsive all on devices and viewports

## Possible Features to be implemented

-   ### Commenting on reviews

    -   This would allow users to discuss books and reviews even further. Allowing complete converstations to take place on the website

-   ### Admin Login

    -   An admin login that would allow the owner complete control over all submissions, books, reviews even users. Allowing someone to moderate what content was inputted to the site

-   ### Password Resetting

    -   Currently if you forget your password... Well you have to create a new account, there is no email functionality implemented therefore no one can reset their password

-   ### User Profiles

    -   Being able to see and look at other peoples profiles, where they could display certain information like favourite books, genres, what books they have added to the website etc.

-   ### Genre Searching

    -   Due to how I created the wesbite a user cannot search for a genre in the search bar, it will return none. This is a quality of life feature but if a user didn't want to use the genre dropdown this would prove usefull.

-   ### Reporting Feature

    -   Allowing users to report a book, review etc. To an admin to be reviewed. This again is a quality of life change but due to possibly users creating books that are explicit or otherwise offensive there is no system in place currently to find these and remove them.

-   ### Rating System

    -   I had wanted to create a rating system but ended up not going through. A rating system can have its benefits and disadvantages. It is great to be able to see what other users think of a book at a quick glance. They are also heavily opinionated therefore can be detrimental to users wanting to read a book that has 1/10 rating for example.

-   ### Lists
    -   Something that is present on other book review websites is the function to be able to create your own lists of a sort. For other people to look through and review, rate etc. Allowing users to dive deeper in the use of the site. Sharing their favourite horrors or fantasy books etc.

## Technologies Used

[HTML5](https://html.spec.whatwg.org/multipage/)
[CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
[Materialize v0.100.2/](http://archives.materializecss.com/0.100.2/) - The framework of the site
[JavaScript](https://www.javascript.com/)
[jQuery](https://jquery.com/)
[Python (v3.8)](https://www.python.org/)
[Flask (v1.1.2)](https://flask.palletsprojects.com/en/1.1.x/)
[Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
[MongoDB](https://docs.mongodb.com/)
[Git](https://git-scm.com/)
[Google Fonts](https://fonts.google.com/)
[Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
[VS Code](https://code.visualstudio.com/)

## Database Structure

Within my MongoDB database there are technically 4 different collections.

1. Books
    - "\_id" Used for identifying the book with a unqiue ID
    - "cover_img_name" The name of the file they have uploaded, this is then called by the file collection for displaying
    - "book_name" User input of the books name
    - "author" User input of the books author or authors
    - "publisher" User input of the books publisher
    - "genre" [ An array of genres picked by the user converted into the genres ObjectId
      "ObjectId" The identifier of a genre, allows app to call on when displaying a particular genre of book
      ]
    - "pages" User input of pages in book
    - "published_date" User input of published date
    - "synopsis" User input of synopsis
    - "isbn" ISBN of book used for the store link function
    - "user_id" User's ID who created the book, to allow user to view what books they have added on manage page
    - "bookmarked_users" [ An array of users that have bookmarked this book
      "bookmarked_user_id" The ID associated with a user to be able to be pulled to show books on bookmarked page
      ]
    - "reviews" [ An array of keys relating to individual reviews
      "review_id" Identifier of specific ID, used to edit and delete particular review
      "review_title" User input of users desired title for their reivew
      "review" User input of their review
      "user_handle" Username of user to be displayed on review page and to also identify if a user has created it or not. Username is unique as two users cannot have the same
      ]
2. Genres
    - "\_id" Used for identifying a genre with a unique ID
    - "name" The name of the genre
3. Users
    - "\_id" Used for identifying a user with a unique ID
    - "username" The usename the user logs in with
    - "password" Protected with a hash this is what the user logs in with and is used to check when logging in if the user has gotten it wrong etc.
4. Files (Chunks)
    - This contains all of the information relevant to uploading and storing a file in mongodb. More information [here](https://www.freecodecamp.org/news/gridfs-making-file-uploading-to-mongodb/)

## Testing

I tried to use the W3C Markup Validators for CSS and HTML although due to the implementation of jinja the html validator will never pass. But the CSS test came up clean, no errors on all 5 of my css files.

### Testing User Stories from UX Section

-   #### First Time Visitors

    1. As a first time visitor, I want to be able to understand the main purpose of the site

        1. Upon seeing the website, the user is immediately presented with a navbar with a search bar and dropdown. The name of the website is a slight giveaway as well. Below the navbar there is two carousels that present newly added books.
        2. The main purpose or information the user will find on the website is shown through the carousels of books and call to action button "view book"
        3. The user has two options, click the button or go further down the page where they will find a section about the website detailed at the bottom of the page.

    2. As a first time visitor, I want to be able to navigate the site with ease

        1. On the website all of the navigation can be achieved through the navigation bar. Each link describes what action the button will take when pressed.
        2. At the first carousel there is a large call to action button for viewing specific books. Each photo on the cards are also clickable to take the user to the book.
        3. On a books page each call to action is clearly labeled and displayed with contrast so the user doesn't get confused.

    3. As a first time visitor, I want to be able to look at a particular book

        1. Every book on the carousel or otherwise is clickable, with a call to action button or not. Taking the user to the desired book.
        2. There is a clear search bar at the top of the screen where the user can search for a specific book they want.
        3. If the book is not present the user will be prompted to log in or if registered add the book they are looking for through a call to action button.

    4. As a first time visitor, I want to be able to search the site for a book I want

        1. On the navbar there is a search bar that allows the user to search for a book by name, author or ISBN
        2. Failing that they can look through the list of genres.
        3. At each step if they cannot find the book they are looking for they are prompted to add it themselves.

    5. As a first time visitor, I want to be able to see where I can buy a particular book

        1. When a user searches for a book or clicks on the books page they are presented with a large call to action store page button. Which will take the user to the amazon link if provided correctly by the user that added the book.
        2. If the link fails it will open a new tab and amazon 404 error will appear. (see extended features to be implemented to learn more)

    6. As a first time visitor, I want to be able to see what reviews books have gotten

        1. When a user clicks on a book they are taken to its page. From there, there is two tabs, one for description of the book and the other for reviews. There they will be able to see all the reviews a book has gotten.
        2. If they are a user they will also see an "add review" button to create a new review if they wish. Non users do not see this.

-   #### Returning Visitors

    1. As a returning visitor, I want to be able to save books I want to read

        1. Across there site there is many prompts to get a user to register to the site. Text on the front page explains what a user can expect for logging into the site.
        2. Once logged in whenever a user looks a book there will be a bookmark icon that will allow the user to save the book for future.
        3. All users can see their bookmarked books in under the profile tab.

    2. As a returning visitor, I want to be able to review and discuss a particular book

        1. When a user is looking at a books page, they have the option to look at reviews. Once on that tab within the webpage there is a call to action button allowing the user to add a review.
        2. If a user is not logged in pressing the button will prompt the user to log in.

    3. As a returning visitor, I want to be able to add my favourite book or books

        1. When logged in a user has the chance to click the "add" button or "add book" on mobile on the navbar. This will take the user to a form where they can input all the information needed for the specific book they want to add.
        2. There is no limit to how many books a user can create.
        3. After creating the book they will be directed to its new page, where they can save it or review it.

-   #### Frequest Visitors

    1.  As a frequest visitor, I want to be able to see what new books there are

        1. On the front page, the two carousels display the newest books that have been added to the site. Constantly updating based on what books are added.

    2.  As a frequest visitor, I want to be able to edit my reviews

        1. When looking at a books review, if the user that created them is loggin in they will be presented with an edit and delete button on the right side of the review. This will take the user to the edit page where they can update what they think about the book.
        2. If the user accidentally clicks the delete button then they will be prompted first if they want to delete it. To prevent accidental clicks.

    3.  As a frequest visitor, I want to be able to edit my books

        1.  Every user gets a "manage" page under their profile dropdown on the navbar. If they haven't added any books they will be prompted to add one now.
        2.  Granted they have added a book the books card will be displayed with an edit and delete button at the bottom of the card. The edit button takes them to a form similar to add book form where they can update the book.
        3.  If the user accidentally clicks the delete button then they will be prompted first if they want to delete it. To prevent accidental clicks.

### Further Testing

-   The website was tested on Chrome, Edge, Firefox, Safari and Android Internet
    -   As I have not set a background colour to the main site. On firefox in dark mode all white is changed to black and black text visa-versa, this was an unintended feature but the site still works and is readable in dark mode. Therefore I didn't change any of the code to correct this action.
-   The website was created with mobile design first, styling it for smaller devices first and scaling up after. It was tested when deployed on various models of phones and desktop screens.
-   Throughout the production fase countless amounts of manual tests were completed making sure that every time I created a new function or changed old code, everything on the website still worked. This included scraping the whole site after every big commit to check every button, page or link.
-   A few friends tested the website who are also programmers to see if they could break or find obvious flaws. Family also viewed the site once deployed to check for styling issues and to give feedback regarding the experience on the site.
-   I used a test branch of git to complete all of the code and then pushed it to master after I was sure that everything was in order. This prevented any major bugs from reaching the master site.

#### Caught and dealt with major bugs after deployment

-   One glaring bug was I didn't serve Jquery over https which was causing many functions on the site to cease working. Through checking this in different browers this was caught and dealt with.

## Other Notes

### Git Commits

To start the project I was continuely trying to limit the ammount of characters were in each commit message as this was good practice. After some time and 165 commits I learnt about commiting with a body of text under the commit title. This is even better practise as it allows a better breakdown of the commits reasoning and code that has been changed. After that I implemented both types of commiting for relevant commits. Using just a title incase the change was small, and commits with a body of text for bigger changes.

## Features to be implemented detailed

### Amazon Store Link

Making the user input a valid 10 digit ISBN it is more than likely that many of the books will not return a valid amazon page on clicking the store button.

Due to my limited knowledge I didn't know how to handle this. In theory I would have the app check if the ISBN and link doesn't return an error, then proceed. If it returns an error notify the user that the link is broken, or altogether diable the link to the store. I could also have another feature that if the ISBN returns an error instead the books name is searched. This would return just to a amazon search but still would be usefull.

### UI / UX Design

#### Ellipsis on the end of long titles

I originally wanted to be able to show ellipsis at the end of a long book title to signify to the user that there was more to be read. In simple CSS this is only possible if you just have one line of text using the class `text-overflow: ellipsis` but this same class doesn't work for multiline text.

There are some plugins for JS that can correct this, but I didn't want to flood the application with many different plugins purely beacuse my own knowledge on the subject is limited. This is something at a later date would be important to add for the users UX sake.

## Major problems and their solutions:

### Displaying Embedded ID's on the Bookmarked Page

This issue was present when I couldn't get flask to display the mongodb data in a html page by searching for it on the db. I wanted to be able to "bookmark" a book and store the books ID in the users "bookmarked" array. To later then be called upon when the user traversed to the "bookmarked" html page.

I managed to get the books ID to append to the users array just fine. But I then couldn't retrieve the books data from the db to be able to display all of its information in another function.

I knew there was a work around where I could store the users ID in the books page and have flask traverse the books collection in the db to find every book that had the users ID listed. But this would've possibly caused massive loading times due to the function having to look through every book. Of which there can be endless amounts of.

Editing Books without removing other document references

One of the first big problems I hit was when I added the edit_task function in python.

This function was updating the databases data from a user submitted form. Seems simple enough, apart from
the fact that within the database I had an array of reviews to be displayed on the individual books page.
This was being deleted when a new form was submitted. Now you see my problem...
I needed to create a new function to be able to just target certain data, iterate over that without removing
other valuable data within the document.

My solution was:

```python
mongo.db.books.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": {
                "book_name": request.form.get("book_name"),
                "author": request.form.get("author"),
                "publisher": request.form.get("publisher"),
                "genre": request.form.get("genre"),
                "pages": request.form.get("pages"),
                "published_date": request.form.get("published_date"),
                "synopsis": request.form.get("synopsis"),
                "isbn": request.form.get("isbn"),
            }
            }
        )
```

In this new code instead of updating the whole object / document within the database. Using this code:

```python
mongo.db.books.update({"_id": ObjectId(book_id)}, edit)
```

I selected particular variables within the db (the ones I wanted to iterate over) while leaving the unselected variables untouched.
This method / code in my opinion is also much cleaner and more consice than creating a variable "edit" and then updating the whole document
with that single variables form inputted data.

### Pagination

Pagination was a must in this project. While on a small scale there wasn't a lot of books created while I was producing this website, if it was actually a "live" website with possibly thousands of books, having them displayed all on one large scrolling page is incredibly bad UX design.

This is a massive oversight in my experience and knowledge as for an actual wesbite this would be incredibly bad practise. My only solution to this would be to not use monodb and use a SQL based database that has pagination built in like SQLAlchemy.

For the time being though I have a different solution:

```python
pages = int(added_books.count()/12)+1

index_start = (int(page_num) - 1) * 12
index_end = int(page_num) * 12

return render_template("manage_books.html", user=user,
                        added_books=added_books[index_start:index_end],
                        pages=pages, current_page=int(page_num))
```

Here I count how many pages will need to be paginated by counting the total documents and dividing them by 12, then adding 1 to allow a non clean division to still display the last few books. Without this a number of books of 13 would only display 1 page and the last book wouldn't be displayed.

Then by creating an index start and end, the program knows that for each 12 books there is a single "index" collection of books. Allowing me to iterate through each collection with pagination. I am unsure if this is a better solution to using skip and limit as I don't know how I could stress test this effectively.

## Deployment

### Deploying Website To Heroku

Deploying your website to heroku is vital in that a website this complex is best hosted with a service that can handle all of the languages. This is also a shareable website but not findable on the web.

1. Create requirements.txt and a Procfile for Heroku using:
    ```
    pip3 freeze -local > requirements.txt
    ```
    This adds all of the packages and services you have installed update to a single file that others can download if they wanted to depoly this site locally. Heroku also needs this to serve the website.
    ```
    echo web:python.app.py > Procfile
    ```
    The Procfile is where you define what commands heroku will run when deploying the site
2. Add and commit new files to github (create a new git repository if not already)
3. Create a Heroku account if you don't already have one
4. Make sure Heroku is installed using command
    ```
    pip install heroku
    ```
5. Create a new heroku app
    ```
    heroku create
    ```
    You will be prompted to log in to Heroku if not already
6. Deploy code to heroku
    ```
    git push heroku master
    ```
    You can also turn on automatic-deployment in the settings on Heroku CLI website, which will deploy every master commit to the website. This is only reccomended if you are working in a test branch on git and a production pipline on Heroku. Pushing possibly buggy or malicious code isn't advised to a live site
7. To complete the deployment go to the Heroku website, log in and navigate to your app
8. Click on settings then in the Config vars fill out the variables with the following information that you would have set up when creating your mongodb collection link

| Key          | Input      |
| ------------ | ---------- |
| IP           | user input |
| PORT         | user input |
| SECRET_KEY   | user input |
| MONGO_URI    | user input |
| MONGO_DBNAME | user input |

9. After following all of this you can either go to the deploy page and manually cause a depoly from your github code, or you can come back to your code editor and repeat instruction 6 which will deploy your code
10. Then on the Heroku website there will be a "open app" button which will open your website

### Cloning This Repository

Cloning is the process of downloading all the code still in format and run it locally on your own code editor.

To make a clone follow these steps:

1. Visit the repository [here](https://github.com/HowellsJonathan/justBooks)
2. On the top of the file layout there will be a dropdown called "code", in the drop down there will be a clone option, navigate there
3. With the HTTPS method selected copy the URL.
4. Go to your desired code editor, make sure GIT is installed and in the terminal run
    ```
    git clone https://example-user.github.io/example-repository/
    ```
5. All the files will then have been cloned to your workspace
6. Don't forget to add your own mongodb collection link and env.py file containing the config vars as seen above
7. To download the required packages run in the terminal
    ```
    pip install -r requirements.txt
    ```
    This will download every package that is in the file, allowing you to run the code without errors

## Credit

### Code Tutorials / Help

[One to one relationships (Part 1)](https://www.youtube.com/watch?v=KA9RrZEmUNg) <br>
[One to one relationships (Part 2)](https://www.youtube.com/watch?v=-UmHaYpNJFM&t=368s) <br>
[Relational Data"](https://www.youtube.com/watch?v=9JZJsChpwKs) <br>
[Nesting Sub Documents](https://www.youtube.com/watch?v=1ANDrQrP0uQ&t=1s) <br>
[One to many relationships](https://www.youtube.com/watch?v=t_9fgpsO_vM) <br>

### Code Used

[Snackbar for flash messages](https://www.w3schools.com/howto/howto_js_snackbar.asp)

### Images

All images used on this site for the books are not owened by me, the site or the users. The website does not gain me any monetary value from using these images.

The image used at the bottom of the front page is from [Unsplash](https://unsplash.com/) a website that has thousands of free high quality images for use. [The particular photo in use.](https://unsplash.com/photos/qcfWJG9uU5Y)
