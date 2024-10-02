def max_smoke_breaks(n, L, a):
    total_breaks = 0

    if n == 0:
        # If no customers, the entire day is free for breaks
        return L // a
    # Read the first customer and handle the free time before the first customer
    prev_end_time = 0  # The end time of the last customer processed (starts at 0)
    for _ in range(n):
        t, l = map(int, input().split())  # Customer's arrival time (t) and duration (l)

        # Calculate free time before this customer
        total_breaks += (t - prev_end_time) // a

        # Update the end time of the current customer
        prev_end_time = t + l

    # After the last customer, calculate the remaining time until the end of the day
    total_breaks += (L - prev_end_time) // a

    return total_breaks

print(max_smoke_breaks(1,3,2))