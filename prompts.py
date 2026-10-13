
customer_support_prompts = [
    {
        "prompt_id": "CS001",
        "category": "customer_support",
        "prompt": "A customer asks how to track an order they placed yesterday. Explain the steps they should follow."
    },
    {
        "prompt_id": "CS002",
        "category": "customer_support",
        "prompt": "A customer received a damaged product. Explain the information they should provide when requesting a replacement."
    },
    {
        "prompt_id": "CS003",
        "category": "customer_support",
        "prompt": "A customer wants to return an item but has lost the original packaging. Explain how they can check their return options."
    },
    {
        "prompt_id": "CS004",
        "category": "customer_support",
        "prompt": "A customer says their refund has not arrived yet. Explain what details they should check before contacting support."
    },
    {
        "prompt_id": "CS005",
        "category": "customer_support",
        "prompt": "A customer received the wrong product. Draft a polite response explaining the next steps to resolve the issue."
    },
    
    {
        "prompt_id": "CS006",
        "category": "customer_support",
        "prompt": "A customer says their package is marked as delivered, but they cannot find it. Explain what they should check next."
    },
    {
        "prompt_id": "CS007",
        "category": "customer_support",
        "prompt": "A customer wants to cancel an order that has already been shipped. Explain what options they can investigate."
    },
    {
        "prompt_id": "CS008",
        "category": "customer_support",
        "prompt": "A customer is frustrated because they have contacted support twice about the same issue. Write an empathetic response and explain how the issue should be escalated."
    }

]


long_input_prompts = [
    {
        "prompt_id": "LI001",
        "category": "long_input",
        "prompt": "Summarize the following store return policy in five bullet points: Customers may request a return within 30 days of delivery. Items must be unused and in their original condition. Some products, including personalized items, may be excluded from returns. Customers should provide their order number and reason for return. Refund processing times depend on the original payment method."
    },
    {
        "prompt_id": "LI002",
        "category": "long_input",
        "prompt": "Explain this shipping policy in simple language: Standard shipping usually takes five to seven business days. Express shipping may take two to three business days. Delivery estimates can change during holidays or severe weather. Tracking information is provided after dispatch. Some remote locations may require additional delivery time."
    },
    {
        "prompt_id": "LI003",
        "category": "long_input",
        "prompt": "Compare these fictional product descriptions and identify three differences: Product A is a lightweight 500 ml water bottle made from stainless steel, with a screw-on lid and a carrying loop. Product B is a 750 ml insulated bottle made from stainless steel, with a flip-top lid and a removable carrying strap. Both are reusable and designed for everyday use."
    },
    {
        "prompt_id": "LI004",
        "category": "long_input",
        "prompt": "Turn the following fictional customer feedback into a concise summary: Customers appreciate the product quality and packaging. Some customers report delayed deliveries. Others find the return instructions confusing. Several customers request more product colors and clearer size information. Summarize the main positive themes, recurring complaints, and suggested improvements."
    },
    {
        "prompt_id": "LI005",
        "category": "long_input",
        "prompt": "Create an organized summary of this fictional order history: Order A contains a notebook and two pens and was delivered on Monday. Order B contains a backpack and was shipped on Wednesday. Order C contains a desk lamp and is awaiting dispatch. Identify each order's items and status, then explain which order appears to need the next fulfillment action."
    }
]


structured_task_prompts = [
    {
        "prompt_id": "ST001",
        "category": "structured_tasks",
        "prompt": "Extract the product name, quantity, and issue from this message and return valid JSON only: I ordered two blue notebooks, but one arrived damaged."
    },
    {
        "prompt_id": "ST002",
        "category": "structured_tasks",
        "prompt": "Classify this support ticket as billing, shipping, returns, or product_quality. Return JSON with keys category and reason. Ticket: My package has not arrived, even though the estimated delivery date was yesterday."
    },
    {
        "prompt_id": "ST003",
        "category": "structured_tasks",
        "prompt": "Convert this order information into a JSON object with order_id, items, and status: Order 1042 contains one backpack and two pens. Its status is shipped."
    },
    {
        "prompt_id": "ST004",
        "category": "structured_tasks",
        "prompt": "Read this message and return a JSON object with sentiment set to positive, neutral, or negative, and a short explanation: The product quality is excellent, but delivery took much longer than expected."
    },
    {
        "prompt_id": "ST005",
        "category": "structured_tasks",
        "prompt": "Extract all action items from this message into a JSON array: Check the shipment tracking number, contact the carrier if delivery is delayed, and notify the customer of any updates."
    },
    {
        "prompt_id": "ST006",
        "category": "structured_tasks",
        "prompt": "Prioritize these three support tickets as high, medium, or low and return JSON only. Ticket A: A customer reports an unauthorized payment. Ticket B: A customer asks about available product colors. Ticket C: A customer wants to know when a routine order will arrive."
    },
    {
        "prompt_id": "ST007",
        "category": "structured_tasks",
        "prompt": "Convert this information into a JSON array with fields product and price: Notebook costs 5 dollars, backpack costs 30 dollars, and desk lamp costs 18 dollars."
    }
]


ambiguous_prompts = [
    {
        "prompt_id": "AM001",
        "category": "ambiguous_requests",
        "prompt": "I want to return it. What should I do?"
    },
    {
        "prompt_id": "AM002",
        "category": "ambiguous_requests",
        "prompt": "My order has a problem. Can you fix it?"
    },
    {
        "prompt_id": "AM003",
        "category": "ambiguous_requests",
        "prompt": "When will it arrive?"
    },
    {
        "prompt_id": "AM004",
        "category": "ambiguous_requests",
        "prompt": "I was charged more than I expected. Please help."
    },
    {
        "prompt_id": "AM005",
        "category": "ambiguous_requests",
        "prompt": "I need to change something about my order, but I'm not sure what information you need."
    }
]


technical_prompts = [
    {
        "prompt_id": "TG001",
        "category": "technical_general",
        "prompt": "Explain what an API is using a simple example from an online shopping application."
    },
    {
        "prompt_id": "TG002",
        "category": "technical_general",
        "prompt": "Explain the difference between a database and a spreadsheet in simple terms."
    },
    {
        "prompt_id": "TG003",
        "category": "technical_general",
        "prompt": "A Python program raises a KeyError when accessing a dictionary. Explain what this error means and how a developer might investigate it."
    },
    {
        "prompt_id": "TG004",
        "category": "technical_general",
        "prompt": "Explain what latency means in an AI application and why users care about it."
    },
    {
        "prompt_id": "TG005",
        "category": "technical_general",
        "prompt": "Explain the difference between input tokens and output tokens in a large language model."
    }
]


# Combine all prompt categories into one test suite.
all_prompts = (
    customer_support_prompts
    + long_input_prompts
    + structured_task_prompts
    + ambiguous_prompts
    + technical_prompts
)

# Validate the dataset.
required_fields = {"prompt_id", "category", "prompt"}

prompt_ids = [item["prompt_id"] for item in all_prompts]

assert len(prompt_ids) == len(set(prompt_ids)), "Duplicate prompt IDs found!"

for item in all_prompts:
    assert required_fields.issubset(item.keys()), (
        f"Missing fields in {item.get('prompt_id', 'unknown')}"
    )
    assert item["prompt"].strip(), (
        f"Empty prompt found: {item['prompt_id']}"
    )

print("Prompt suite validation passed!")
print("Total prompts:", len(all_prompts))
print("Unique IDs:", len(set(prompt_ids)))

for category in sorted({item["category"] for item in all_prompts}):
    count = sum(
        1 for item in all_prompts
        if item["category"] == category
    )
    print(f"{category}: {count}")
