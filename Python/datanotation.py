def decode(message_file):
    pyramid_lines = []
    decoded_words = []

    # Read the lines from the file and split them into words
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Process each line to build the pyramid
    for line in lines:
        _, word = line.strip().split(' ', 1)
        pyramid_lines.append(word)

    # Extract the words at the end of each pyramid line
    for i, line in enumerate(pyramid_lines):
        words = line.split()
        decoded_words.append(words[i])

    # Join the decoded words into a string
    decoded_message = ' '.join(decoded_words)

    return decoded_message

# Example usage:
decoded_message = decode('message.txt')
print(decoded_message)
