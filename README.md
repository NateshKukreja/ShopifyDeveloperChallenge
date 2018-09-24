# ShopifyDeveloperChallenge

This is a Python App running Flask
**Documentation**
1. Shops
* URL
  * `/api/v1.0/shops`
* Method:
	* `GET`
* Optional:
	* `/<int:shop_id>`
* Error Response:
	* Code: 401 Unauthorized
	* Content: `{"error": 401, "description":"Unauthorized access"}`
* Sample Call
	* Call: `curl -u Natesh:isGreat -i http://127.0.0.1:5000/api/v1.0/shops`
	* Response: 
	```
  {
    "shop_id": 1,
    "name": "Loblaws",
    "products": [
      {
        "product_id": 10,
        "name": "Milk",
        "line_id": 30,
        "shop_id": 1
      },
      {
        "product_id": 11,
        "name": "Eggs",
        "line_id": 31,
        "shop_id": 1
      }
    ],
    "orders": [
      {
        "order_id": 20,
        "total": 5
      }
    ]
  }
* URL
  * `/api/v1.0/shops/shop_id`
* Method
	* DELETE
* Error Response:
	* Code: 404 Not found
	* Content: `{"error":404, "description": "Shop not found"}`
* Sample Call
	* Call: `curl -u Natesh:isGreat -X "DELETE" http://127.0.0.1:5000/api/v1.0/shops/1`
	* Response: 
	```
	{
	"shops": []
	}
* URL
  * `/api/v1.0/shops/shop_id`
* Method
	* POST
* Error Response:
	* Code: 400 Bad request
	* Content: `{"error":"Missing name in json format"}`
* Sample Call
	* Call: `curl -u Natesh:isGreat -X "DELETE" http://127.0.0.1:5000/api/v1.0/shops/1`
	* Response: 
	```
	[
	{
    "shop_id": 1,
    "name": "Loblaws",
    "products": [
      {
        "product_id": 10,
        "name": "Milk",
        "line_id": 30,
        "shop_id": 1
      },
      {
        "product_id": 11,
        "name": "Eggs",
        "line_id": 31,
        "shop_id": 1
      }
    ],
    "orders": [
      {
        "order_id": 20,
        "total": 5
      }
    ]
  },
	{
	"shop_id": 2,
	"name": "Metro",
	"products": [],
	"orders": []
	}
]
