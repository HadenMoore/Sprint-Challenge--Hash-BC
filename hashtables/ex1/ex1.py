#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):
         #limit-weight[i] value stored in ht as key
        banana =  hash_table_retrieve(ht, limit - weights[i])
        if banana is not None: 
            answer = (i, banana)
            return answer
        else: 
            hash_table_insert(ht, weights[i], i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


weights_3 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_3, 9, 7))

#All Tests Pass.