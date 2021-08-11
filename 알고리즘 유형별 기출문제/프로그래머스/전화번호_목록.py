# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["12","123","1235","567","88"]
phone_book = ["0", "2", "01", "11"]
n = len(phone_book)
phone_book.sort(key=lambda x: len(x))
print(phone_book)
answer = True
for i in range(n):
    for j in range(i + 1, n):
        string = str(phone_book[j])
        if phone_book[i] == string[0:len(phone_book[i])]:
            answer = False
            break
    if not answer:
        break

print(answer)