# BookAPI Deployment Test Server 

## BooksAPi endpoints

![image](https://github.com/themusharraf/FastAPIBooks/assets/122869450/1517ab38-808e-4848-b8bb-9cd2667fe1bd)

![image](https://github.com/themusharraf/FastAPIBooks/assets/122869450/aae7e4d1-2eb5-4efa-a9f8-74937c6a319d)


![orm](https://github.com/themusharraf/bookapi/assets/122869450/7e30603c-a0f2-466c-a826-892454b756fd) 
   
## Example Request for Updating User:
### http

```
PUT /users/1
Content-Type: application/json

{
  "username": "new_username",
  "email": "new_email@example.com",
  "is_active": true,
  "password": "new_password"
}
```
## Example Request for Updating Book:
### http

```
PUT /books/1
Content-Type: application/json

{
  "title": "Updated Title",
  "language": "English",
  "isbn": "978-3-16-148410-0",
  "pages": 250
}
```
