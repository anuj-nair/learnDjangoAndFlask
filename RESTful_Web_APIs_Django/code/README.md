# REST API in Django

## Curl Commands
* Create Product
	```
	curl -X POST http://localhost:8000/api/v1/products/new -d price=<product price> -d name='<product name>' -d description='product description'
	```

* Delete Product
	```
	curl -X DELETE http://localhost:8000/api/v1/products/<product id>/destroy
	```
