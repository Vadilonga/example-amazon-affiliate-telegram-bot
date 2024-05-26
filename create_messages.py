#a very simple function that creates a post for a product
def create_product_post(product):
    response = ""
    print(f'{3 * "*"} Creating post {3 * "*"}')

    if product:
        title = product.item_info.title.display_value
        image_url = product.images.variants[0].medium.url
        price = product.offers.listings[0].price.amount
        product_url = product.detail_page_url
        
        if(product.offers.listings[0].price.savings.amount):
            old_price = product.offers.listings[0].price.savings.amount + product.offers.listings[0].price.amount

        html = f"🛒 <b>{title}</b>\n\n"
        html += f"<a href='{image_url}'>&#8205;</a>\n"
        html += f"💰 <b>{price}€</b>"
        if(old_price):
            html += f" anzichè {old_price}€\n\n"
        html += f"👉🏻 <a href='{product_url}'>Apri su Amazon</a>"
        response = html

    return response