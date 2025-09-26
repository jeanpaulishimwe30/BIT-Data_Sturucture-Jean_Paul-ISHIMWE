# Project 43: Stack Questions

# --- Practical 1 (Rwanda: MoMo Example) ---
momo_stack = ["Step1: Enter PIN", "Step2: Enter Amount", "Step3: Confirm"]

# Undo step 3 (pop)
momo_stack.pop()
print("MoMo Top after undo:", momo_stack[-1])  # What remains on top


# --- Practical 2 (Rwanda: UR student Example) ---
ur_stack = ["Revise Math", "Revise English", "Revise ICT"]

# Pop one
ur_stack.pop()
print("UR Student Top after popping one:", ur_stack[-1])  # Which remains on top


# --- Challenge: Reverse "RWANDADATA" using stack ---
word = "RWANDADATA"
stack = []

# Push each character
for ch in word:
    stack.append(ch)

# Pop all to reverse
reversed_word = ""
while stack:
    reversed_word += stack.pop()

print("Reversed word:", reversed_word)


# --- Reflection ---
reflection = """
A stack is efficient for reversing strings because of its LIFO (Last-In First-Out) nature: 
the last character pushed is the first one popped,stacks are not efficient for serving people (like in a queue), because in real life, 
fair service requires FIFO. 
"""
print(reflection)



# Project 43: Queue Questions

from collections import deque

# --- Practical 1 (Rwanda: Airtel customers) ---
airtel_queue = deque(["Customer1", "Customer2", "Customer3", 
                      "Customer4", "Customer5", "Customer6", "Customer7"])

# Serve first 2 customers
airtel_queue.popleft()
airtel_queue.popleft()

print("Airtel Front after 2 served:", airtel_queue[0])  # Who is at front now


# --- Practical 2 (Rwanda: Nyabugogo buses) ---
buses_queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5"])

# First bus to depart
print("First bus to depart from Nyabugogo:", buses_queue[0])


# --- Challenge (Kigali Arena Tickets Queue System) ---
kigali_arena_queue = deque()

# People buying tickets join queue
kigali_arena_queue.append("PersonA")
kigali_arena_queue.append("PersonB")
kigali_arena_queue.append("PersonC")

# Serve first person
served = kigali_arena_queue.popleft()

print("Kigali Arena - First served:", served)
print("Remaining in queue:", list(kigali_arena_queue))

# Why stack is wrong?
reason_stack_wrong = """
Using a stack for Kigali Arena tickets would mean the last person to arrive
is the first to get served (LIFO). 
"""
print(reason_stack_wrong)


# --- Reflection
reflection = """
FIFO ensures fairness because the first person who comes 
is the first one to be served. This matches what people expect: 
like in banks, people expect to be  served
in the order they arrived. FIFO prevents cheating and keeps trust"""
print(reflection)
