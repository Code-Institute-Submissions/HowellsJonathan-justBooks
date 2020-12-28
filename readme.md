<!-- @format -->

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

```
mongo.db.books.update({"_id": ObjectId(book_id)}, edit)
```

I selected particular variables within the db (the ones I wanted to iterate over) while leaving the unselected variables untouched.
This method / code in my opinion is also much cleaner and more consice than creating a variable "edit" and then updating the whole document
with that single variables form inputted data.

### Pagination

Pagination was a must in this project. While on a small scale there wasn't a lot of books created while I was producing this website, if it was actually a "live" website with possibly thousands of books, having them displayed all on one large scrolling page is incredibly bad UX design.

To combat this I needed to use pages or pagination to display a set amount of books at a time to the user. But it wasn't something I had ever approached before. I had used limiting previously in this project to limit the number of books displayed in the swiper carousel. After some research and help from these two sources [1](https://www.youtube.com/watch?v=Lnt6JqtzM7I&t=703sI) [2](https://www.codementor.io/@arpitbhayani/fast-and-efficient-pagination-in-mongodb-9095flbqr) learned about "skip".

Skip() is a function provided by mongodb that allows you to skip a certain amount of documents at a time, this allows you to provide only (in my case) 12 books at a time on a single "page". Then using materialize pagination and some extensive jinja allows the user to scroll through different pages of documents. The limitations of skip and limit are that each time you render a new page teh app has to read each of the documents before it to load the next 12. This increases loading times when you had possibly thousands of books. Although for this project it isn't as much of a worry as it will never be populated with so many documents.

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

## Help:

[One to one relationships (Part 1)](https://www.youtube.com/watch?v=KA9RrZEmUNg) <br>
[One to one relationships (Part 2)](https://www.youtube.com/watch?v=-UmHaYpNJFM&t=368s) <br>
[Relational Data"](https://www.youtube.com/watch?v=9JZJsChpwKs) <br>
[Nesting Sub Documents](https://www.youtube.com/watch?v=1ANDrQrP0uQ&t=1s) <br>
[One to many relationships](https://www.youtube.com/watch?v=t_9fgpsO_vM) <br>
