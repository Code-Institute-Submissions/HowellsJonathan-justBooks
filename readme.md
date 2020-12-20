<!-- @format -->

# Major problems and their solutions:

## Displaying Embedded ID's on the Bookmarked Page

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

```
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

```
mongo.db.books.update({"_id": ObjectId(book_id)}, edit)
```

I selected particular variables within the db (the ones I wanted to iterate over) while leaving the unselected variables untouched.
This method / code in my opinion is also much cleaner and more consice than creating a variable "edit" and then updating the whole document
with that single variables form inputted data.

## Limiting results from mongodb:

I wanted to limit the amount of documents called from mongodb when displaying them in carousels on mobile view. I didn't want to display possibly hundred of books that no one would ever scroll through. I attempted to use the .limit() variable but to no avail...

This causes a large oversight in bad UX design and could cause unnececary loading times due to the program having to load every single book over and over again...

# Help:

https://www.youtube.com/watch?v=KA9RrZEmUNg <br>
https://www.youtube.com/watch?v=-UmHaYpNJFM&t=368s <br>
https://www.youtube.com/watch?v=9JZJsChpwKs <br>
https://www.youtube.com/watch?v=1ANDrQrP0uQ&t=1s <br>
https://www.youtube.com/watch?v=t_9fgpsO_vM <br>

# Code Help:

https://stackoverflow.com/questions/4421207/how-to-get-the-last-n-records-in-mongodb
