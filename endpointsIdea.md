<!-- items -->
GET
`/api/items`
`/api/items?type=${type}&status=${status}&isFavorite=${isFavorite}&genre=${genre}`

GET
`/api/items/:id`

POST
`/api/items`

PUT
`/api/items/:id`

DELETE
`/api/items/:id`

<!-- genre -->
<!-- only GET on genre because is not going to be editable -->
GET
`/api/genres/`

GET
`/api/genres/:id`

<!-- comments -->

GET
`/api/items/:id/comments`

POST
`/api/items/:id/comments`

DELETE
`/api/items/:id/comment/:commentId`

<!-- books -->
<!-- only GET because is an externa API that bring the info -->
GET
`/api/books`

GET
`/api/books/:id`

POST
`/api/books`

PUT
`/api/books/:id`

DELETE
`/api/books/:id`

<!-- movie -->
<!-- only GET because is an externa API that bring the info -->
GET
`/api/movies`

GET
`/api/movies/:id`

POST
`/api/movies`

PUT
`/api/movies/:id`

DELETE
`/api/movies/:id`

<!-- Saga -->
<!-- only GET because is an externa API that bring the info -->
GET
`/api/sagas`

GET
`/api/sagas/:id`

POST
`/api/sagas`

PUT
`/api/sagas/:id`

DELETE
`/api/sagas/:id`

<!-- Serie -->
<!-- only GET because is an externa API that bring the info -->
GET
`/api/series`

GET
`/api/series/:id/seasons`

POST
`/api/series`

PUT
`/api/series/:id`

DELETE
`/api/series/:id`