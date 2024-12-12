from fastapi import APIRouter,Path, Query, HTTPException, status
from product_management.manage_product_data import Product,ProductRequest

product_router = APIRouter(prefix="/api/v2")

PRODUCTS = [
    Product(1, 'Widget Pro', 'Widgets', 'A high-quality widget', 29.99),
    Product(2, 'Gadget Max', 'Gadgets', 'A versatile gadget for all your needs', 49.99),
]

@product_router.post('/products/add', status_code=status.HTTP_201_CREATED)
async def create_product(product_request: ProductRequest):
    product_request.id = product_request.id if product_request.id else len(PRODUCTS) + 1
    print(product_request)
    new_product = Product(**product_request.model_dump())
    PRODUCTS.append(new_product)
    return new_product

# Read all products
@product_router.get('/products/', status_code=status.HTTP_200_OK)
async def read_all_products():
    return PRODUCTS

# Read a product by ID
@product_router.get('/products/{product_id}', status_code=status.HTTP_200_OK)
async def read_product(product_id: int = Path(gt=0)):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail='Product not found')

# Update a product
@product_router.put('/products/{product_id}', status_code=status.HTTP_200_OK)
async def update_product(product_id: int, product_request: ProductRequest):
    for i, product in enumerate(PRODUCTS):
        if product.id == product_id:
            updated_product = Product(id=product_id, **product_request.model_dump())
            PRODUCTS[i] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail='Product not found')

# Delete a product
@product_router.delete('/products/{product_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int):
    for i, product in enumerate(PRODUCTS):
        if product.id == product_id:
            PRODUCTS.pop(i)
            return
    raise HTTPException(status_code=404, detail='Product not found')