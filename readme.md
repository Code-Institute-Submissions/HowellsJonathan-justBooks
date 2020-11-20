<!-- @format -->

Major problems and their solutions:

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

Help:

https://www.youtube.com/watch?v=KA9RrZEmUNg <br>
https://www.youtube.com/watch?v=-UmHaYpNJFM&t=368s <br>
https://www.youtube.com/watch?v=9JZJsChpwKs <br>
https://www.youtube.com/watch?v=1ANDrQrP0uQ&t=1s <br>
https://www.youtube.com/watch?v=t_9fgpsO_vM <br>

Code Help:

https://stackoverflow.com/questions/4421207/how-to-get-the-last-n-records-in-mongodb
