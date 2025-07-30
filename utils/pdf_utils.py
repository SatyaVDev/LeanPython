from pypdf import PdfReader
import re
import json


def extract_transactions_json(pdf_path):
  reader = PdfReader(pdf_path)
  full_text = ""

  # Collect all text
  for page in reader.pages:
    text = page.extract_text()
    if text:
      full_text += text + "\n"

  # Try to isolate just the "Transaction Details" section
  try:
    transaction_text = full_text.split("Transaction Details")[1]
  except IndexError:
    print("Couldn't find 'Transaction Details' section.")
    return []

  lines = [
      line.strip() for line in transaction_text.strip().splitlines()
      if line.strip()
  ]

  transactions = []
  buffer = []

  date_pattern = re.compile(r'^\d{2}-\d{2}-\d{4}')
  amount_ref_pattern = re.compile(r'([\d,]+(?:\.\d+)?)\s+(Dr\.|Cr\.)\s+(\d+)$')

  for line in lines:
    if date_pattern.match(line):  # Line starts a new transaction
      if buffer:
        transactions.append(buffer)
      buffer = [line]
    else:
      buffer.append(line)
  if buffer:
    transactions.append(buffer)  # Add the last transaction

  # Process each transaction
  parsed_transactions = []
  for entry in transactions:
    merged = ' '.join(entry)

    try:
      date = re.search(r'\d{2}-\d{2}-\d{4}', merged).group()
      amount_match = amount_ref_pattern.search(merged)
      if not amount_match:
        continue
      amount = float(amount_match.group(1).replace(",", ""))
      txn_type = amount_match.group(2)
      reference = amount_match.group(3)

      # Description is everything between date and amount
      desc_start = merged.find(date) + len(date)
      desc_end = amount_match.start()
      description = merged[desc_start:desc_end].strip()

      parsed_transactions.append({
          "date": date,
          "description": description,
          "amount": amount,
          "type": txn_type,
          "reference": reference
      })
    except Exception as e:
      print("Error parsing entry:", entry)
      print("Error:", e)

  # Output JSON
  json_output = json.dumps(parsed_transactions, indent=2)

  sum = 0
  for item in parsed_transactions:

    if item["amount"] > 1 and item["type"].strip() == "Dr.":
      sum += item["amount"]
      print(f'{item["amount"]} , type : {item["type"]}')
    # print(item["amount"])
    # print(item.get("amout")

  print(sum)
  # print(json_output)
  return parsed_transactions
