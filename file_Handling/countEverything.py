def count_txt_file(file_path):
    with open(file_path,'r') as file:
        lines = file.readlines()
        count_lines = len(lines)
        final_word_count =0
        final_char_count = 0
        for line in lines:
            words = line.split()
            count_words = len(words)
            final_word_count +=count_words
            for word in words:
                char_count = len(word)
                final_char_count += char_count


    return final_char_count



file_path = 'yashji.txt'
ansss = count_txt_file(file_path)
print(ansss)