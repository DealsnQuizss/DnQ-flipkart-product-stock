from typing import Optional
import flipkart
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "api_name": "flipkart-product-stock",
        "author": "dvisha485@gmail.com",
        "description": "API to scrapes product details and pincode specific stock from Flipkart",
        "example": "./product?link=https://dl.flipkart.com/s/3wCLKlNNNN&pincode=110051"
    }


@app.get("/product")
async def read_item(link: str, pincode: Optional[str] = 110051):
    link = link.split('?')[0]
    if link.count('http') == 0:
        if link[0] == '/':
            link = link.replace('/', '', 1)
        if link.split('/')[0] == 's':
            link = 'https://dl.flipkart.com/' + link
        else:
            link = 'https://www.flipkart.com/' + link
    print(link)
    result = await flipkart.getProductDetails(link, pincode)
    print(result)
    return json.loads(json.dumps(result))
