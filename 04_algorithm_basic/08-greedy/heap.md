# heap and back tracking

## heap
**document structure for find the highest value or lowest value in complete binary tree**


#back Tracking
def backtrack():
    if solution_condition_is_met():
        return

    for choice in possible_choices:
        if not is_valid(choice):
            continue

        make_choice(choice)
        backtrack()  # recursive call to next step
        undo_choice(choice)  # backtrack (this is the "back" part)
