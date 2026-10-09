def mobile_store():
  raw_input = input("Enter mobile prices separated by spaces: ")
  prices = [float(x) for x in raw_input.split()]
  if not prices:
    print("No prices entered.\n")
    return

  expensive_mobiles = [p for p in prices if p > 20000]
  total_inventory_value = sum(prices)
  most_expensive = max(prices)
  print(
      f"Mobiles > 20,000: {expensive_mobiles}\nTotal Inventory Value:"
      f" ₹{total_inventory_value}\nMost Expensive: ₹{most_expensive}\n"
  )

if __name__ == ("__main__"):
  mobile_store()
