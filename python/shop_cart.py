def manage_cart():
  raw_input = input("Enter initial products in cart separated by commas: ")
  cart = [item.strip() for item in raw_input.split(",") if item.strip()]

  new_product = input("Enter a new product to add: ").strip()
  remove_product = input("Enter a product to remove (if present): ").strip()

  cart.append(new_product)
  if remove_product in cart:
    cart.remove(remove_product)

  print(f"Final Cart: {cart}\nTotal Products in Cart: {len(cart)}\n")

if __name__ == ("__main__"):
  manage_cart()
