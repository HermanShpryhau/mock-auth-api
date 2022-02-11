# Mock Authentication API

The API accepts requests containing email and password and checks them against in-memory list of users' credentials.

### Sample Request

```http
GET /auth?email=user1@mail.com&password=user1
```

### Responses

```json
{
    "authenticated": "true"
}
```

on successfull authentication.

```json
{
    "authenticated": "false"
}
```

if there is no user with such credentials.

### Valid User Credentials

| Email | Password |
|:--|:--|
| user1@mail.com | user1 |
| user2@mail.com | user2 |
| user3@mail.com | user3 |

## Starting the Server Locally

To run the server locally jsut run this command in your terminal:

```
$ uvicorn mock_auth_api:app
```

*Note!* You need to have Python 3.9 or higenr installed as well as Fast API and Uvicor python modules. You can istall them with pip:

```
$ pip install fastapi uvicorn
```
