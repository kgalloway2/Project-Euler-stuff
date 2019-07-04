top_row_shift = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
top_row = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
q_row = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\']
a_row = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'k', 'l', ';', "'"]
z_row = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']
extras = ['{', '}', '|', ':', '"', '<', '>', '?']

original_message = raw_input("What is your original message?")
shift = raw_input("How much would you like to shift it?")

def shift_function(string, shift):
    print string
    shift = int(shift)
    new_message = ''
    for i in string:
        if i in top_row_shift:
            new_i = top_row_shift[((top_row_shift.index(i) + shift) % len(top_row_shift))]
        elif i in top_row:
            new_i = top_row[((top_row.index(i) + shift) % len(top_row))]
        elif i in q_row:
            new_i = q_row[((q_row.index(i) + shift) % len(q_row))]
        elif i in a_row:
            new_i = a_row[((a_row.index(i) + shift) % len(a_row))]
        elif i in z_row:
            new_i = z_row[((z_row.index(i) + shift) % len(z_row))]
        elif i in extras:
            new_i = extras[((extras.index(i) + shift) % len(extras))]
        else:
            new_i = i
        new_message = new_message + new_i
    return new_message

print shift_function(original_message, shift)