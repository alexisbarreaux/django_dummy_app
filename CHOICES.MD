# Choices made and improvements.

I managed to link a postgre database to my project, display and update products
and there expiry dates for a store but there is still room for several improvements.

## Database

### Using a local database

I used a local database. It will unfortunately oblige you to create one and add
some objects to test the project, however I already had a lot to learn and thought
I wouldn't manage to also deploy a server. Also the credentials are stored as is
in the settings and not gitignored which is not a good idea, but I left them there
for you to have to change as little as possible.

### Models

I chose to represent stores as simply as possible with just a name. Employee and products then belongs to a store, whose information is used
to modify the display based on which employee accesses the app.

I added several validators but, and this is one of the biggest issues to me,
there isn't any "real" login in the code I did. I look up to find an
employee in the database but I did not protect the urls nor resort to django Users
system because I felt I wouldn't have the time.

Also, I think for the products we should have a set of all the
current expiry dates and regularly update the shortest one, but I kept it simple
with storing only the shortest.

Finally, right now we check if an employee exists and then deduce the store. To
avoid collision we should rather also ask the employee for his store when login in,
with a select field or search bar.

## Frontend :

### Visuals

The test site would need a header and footer and better visuals. Also
I didn't make the table for the display of products sortable or filterable. It is
however sorted by GTIN at first.

## Backend :

### Tests

As this project wasn't to ever be deployed and also since it was short I did not
write any tests. This would be the next if this project were to be used again.
