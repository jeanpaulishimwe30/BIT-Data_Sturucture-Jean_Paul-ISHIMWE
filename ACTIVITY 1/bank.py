import array

# --- Functions ---

def generate_deposit_list():
    return [1200, 1500, 800, 2000, 950, 1700]

def compute_stats(deposits):
    total = sum(deposits)
    average = total / len(deposits)
    minimum = min(deposits)
    maximum = max(deposits)
    return total, average, minimum, maximum

def display_report(total, average):
    print(f"Total Deposits: ${total}")
    print(f"Average Deposit: ${average:.2f}")

def check_threshold(average, threshold=1000):
    if average > threshold and average != 0:
        print("Status: Above Standard")
    else:
        print("Status: Below Standard")

def modify_deposit_list(deposits):
    print("\nOriginal List:", deposits)
    
    # Add new deposit
    deposits.append(1300)
    
    # Remove if less than 1000
    deposits = [d for d in deposits if d >= 1000]
    
    # Sort the list
    deposits.sort()
    
    print("Modified List:", deposits)
    return deposits

def use_array_subset(deposits):
    subset = deposits[:5]  # fixed-size subset
    deposit_array = array.array('i', subset)
    
    array_sum = sum(deposit_array)
    list_sum = sum(subset)
    
    print("\nArray Subset:", deposit_array.tolist())
    print(f"Sum of Array: {array_sum}")
    print(f"Sum of List: {list_sum}")
    return array_sum == list_sum

def manage_dict_records():
    print("\n--- Dictionary Records ---")
    records = [
        {'id': 1, 'name': 'Alice', 'value': 1200},
        {'id': 2, 'name': 'Bob', 'value': 1500},
        {'id': 3, 'name': 'Charlie', 'value': 800},
    ]
    
    # Update Bob's value
    for record in records:
        if record['id'] == 2:
            record['value'] = 1600
    
    # Delete Charlie's record
    records = [r for r in records if r['name'] != 'Charlie']
    
    # Compute total
    total_value = sum(r['value'] for r in records)
    
    print("Updated Records:")
    for r in records:
        print(r)
    
    print(f"Total Value of Records: ${total_value}")
    return records, total_value

# --- Main Program ---

def main():
    print("=== Bank Deposit Records ===")
    
    deposits = generate_deposit_list()
    total, average, minimum, maximum = compute_stats(deposits)
    
    display_report(total, average)
    check_threshold(average)
    
    deposits = modify_deposit_list(deposits)
    
    array_match = use_array_subset(deposits)
    print("Array and List sums match?" , array_match)
    
    records, total_record_value = manage_dict_records()

# Run the program
main()


