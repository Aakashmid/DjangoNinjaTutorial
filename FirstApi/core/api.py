from ninja import NinjaAPI

api = NinjaAPI()

# without argument
# @api.get("/hello")
# def hello(request):
#     return "Hello world"


# taking parameter # url for this domain/api/hello?name=value
@api.get("/hello")
def hello(request, name):
    return f"Hello {name}"


# url for this enpoint look like -http://127.0.0.1:8000/api/math?a=4&b=5
@api.get("/math")
def math(request, a: int, b: int):  # taking two parameter of integer type  
    return {"add": a + b, "multiply": a * b}