import requests
import time

BASE_URL = "https://simple-grocery-store-api.click"


def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")

    # status code check
    assert response.status_code == 200

    product = response.json()

    # the list is not empty
    assert len(product) > 0

    # there is shown at least 1 element
    first_product = product[0]

    # mandatory fields are present
    assert "id" in first_product
    assert "name" in first_product
    assert "category" in first_product
    assert "inStock" in first_product

    # type of data
    assert isinstance(first_product["id"], int)
    assert isinstance(first_product["name"], str)
    assert isinstance(first_product["category"], str)
    assert isinstance(first_product["inStock"], bool)

def test_get_product_by_id():
    response = requests.get(f"{BASE_URL}/products/")

    products = response.json()
    product_id = products[0]["id"]

    response = requests.get(f"{BASE_URL}/products/{product_id}")

    # status code check
    assert response.status_code == 200

    products = response.json()
    assert products["id"] == product_id

def test_get_product_by_invalid_id():
    response = requests.get(f"{BASE_URL}/products/999999")

    assert response.status_code == 404

def test_create_new_cart():
    response = requests.post(f"{BASE_URL}/carts")

    assert response.status_code == 201

    cart = response.json()

    #cartId is present in response body
    assert "cartId" in cart

    #generated cartId is a string
    assert isinstance(cart["cartId"], str)

def test_add_item_to_cart():

    response = requests.post(f"{BASE_URL}/carts")

    cart = response.json()

    #pick cartId 
    cartId = cart["cartId"]

    #adding 1225 product_id to cart
    response = requests.post(f"{BASE_URL}/carts/{cartId}/items", json= { "productId": 1225 })

    print(response.status_code)
    print(response.json())

    #check status code
    assert response.status_code == 201

def test_create_new_order():

    # generate and label api token 
    requestBodyForAPIToken = {"clientName": "Gigel", "clientEmail": f"abelzor{int(time.time())}@gmail.com"}

    response = requests.post(f"{BASE_URL}/api-clients", json = requestBodyForAPIToken)

    apiToken = response.json()
    TokenId = apiToken["accessToken"]

    #create a new cart and label it's id
    response = requests.post(f"{BASE_URL}/carts")

    cart = response.json()
    cartId = cart["cartId"]

    #adding 1225 product_id to cart
    response = requests.post(f"{BASE_URL}/carts/{cartId}/items", json = { "productId": 1225 })

    #create new order
    headers = { "Authorization": f"Bearer {TokenId}"}
    apiBody = {"cartId": cartId, "customerName": "Abelica"}

    response = requests.post(f"{BASE_URL}/orders", json = apiBody, headers = headers)
    assert response.status_code == 201

def test_get_all_orders():

    # generate and label api token 
    requestBodyForAPIToken = {"clientName": "Gigel", "clientEmail": f"abelzor{int(time.time())}@gmail.com"}

    response = requests.post(f"{BASE_URL}/api-clients", json = requestBodyForAPIToken)

    apiToken = response.json()
    TokenId = apiToken["accessToken"]

    #create a new cart and label it's id
    response = requests.post(f"{BASE_URL}/carts")

    cart = response.json()
    cartId = cart["cartId"]

    #adding 1225 product_id to cart
    response = requests.post(f"{BASE_URL}/carts/{cartId}/items", json = { "productId": 1225 })

    #create new order
    headers = { "Authorization": f"Bearer {TokenId}"}
    apiBody = {"cartId": cartId, "customerName": "Abelica"}

    response = requests.post(f"{BASE_URL}/orders", json = apiBody, headers = headers)
    assert response.status_code == 201

    #get curent created order
    headers = { "Authorization": f"Bearer {TokenId}"}
    response = requests.get(f"{BASE_URL}/orders", headers = headers)

    #status code check
    assert response.status_code == 200

    orders = response.json()

    #response has data 
    assert len(orders) > 0

    currentOrder = orders[0]

    assert "id" in currentOrder
    assert "items" in currentOrder
    assert "customerName" in currentOrder
    assert "created" in currentOrder






