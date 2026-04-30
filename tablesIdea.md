items

| name           | class   |
| -------------- | ------- |
| id             | number  |
| type           | string  |
| status         | string  |
| emision_status | string  |
| is_favorite    | boolean |

genres

| name | class  |
| ---- | ------ |
| id   | number |
| name | string |

item_genres

| name     | class  |
| -------- | ------ |
| item_id  | number |
| genre_id | number |

comments

| name       | class     |
| ---------- | --------- |
| id         | number    |
| item_id    | number    |
| content    | string    |
| created_at | timestamp |

books

| name      | class  |
| --------- | ------ |
| id        | number |
| item_id   | number |
| book_name | string |
| author    | string |
| cover     | string |
| year      | number |

movie

| name       | class  |
| ---------- | ------ |
| id         | number |
| item_id    | number |
| movie_name | string |
| year       | number |
| director   | string |
| cover      | string |

saga

| name  | class  |
| ----- | ------ |
| id    | number |
| name  | string |
| type  | string |
| cover | string |

saga_items

| name    | class  |
| ------- | ------ |
| saga_id | number |
| item_id | number |
| order   | number |

Serie

| name       | class   |
| ---------- | ------- |
| id         | number  |
| serie_name | string  |
| item_id    | number  |
| has_season | boolean |
| year       | number  |
| director   | string  |
| cover      | string  |

Season Serie

| name        | class  |
| ----------- | ------ |
| serie_id    | number |
| id          | number |
| season_name | string |
| year        | number |
| cover       | string |
| director    | string |
| order       | number |
