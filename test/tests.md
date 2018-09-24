# ShopifyDeveloperChallenge

Manual testing:
1. Ensure you have Flask installed on your machine
	* If you don't have Flask installed, running `pip install flask` should install it
2. Open Terminal
3. Navigate to the directory holding index.py
4. In terminal, run `python3 index.py` (Python3 should be installed)
5. The Flask app should be loaded now and should be running on http://127.0.0.1/5000
6. Open another Terminal window while the app is running
7. Below are CURL requests that can be ran through Terminal
	* **GET TESTS**
		* `curl -u Natesh:isGreat -i http://127.0.0.1:5000/api/v1.0/products`
		* `curl -u Natesh:isGreat -i http://127.0.0.1:5000/api/v1.0/orders`
		* `curl -u Natesh:isGreat -i http://127.0.0.1:5000/api/v1.0/shops`
		* `curl -u Natesh:isGreat -i http://127.0.0.1:5000/api/v1.0/line`
		* `curl -u Natesh:isGreat -i http://127.0.0.1:5000/api/v1.0/shops/1`
	* **POST TESTS**
		* `curl -i -H "Content-Type: application/json" -X POST -d '{"name":"cereal"}' http://127.0.0.1:5000/api/v1.0/products`
		* `curl -i -H "Content-Type: application/json" -X PST -d '{"lines":[{"line_id": 30,"product_id": 10,"quantity": 1,"price": 5}]}' http://127.0.0.1:5000/api/v1.0/orders`
		* `curl -i -H "Content-Type: application/json" -X POST -d '{"shop":{"name":"Metro"}}' http://127.0.0.1:5000/api/v1.0/shops`
	* **DELETE TEST**
		* `curl -u Natesh:isGreat -X "DELETE" http://127.0.0.1:5000/api/v1.0/shops/1`