# Solutions for Lab 14 Tasks

## Task 1: find_duplicates

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return list(duplicates)

## Task 2: most_frequent

def most_frequent(lst):
    return max(set(lst), key=lst.count)

## Task 3: find_pair_sum

def find_pair_sum(nums, target):
    seen = {}
    for num in nums:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

## Task 4: sort_by_length

def sort_by_length(lst):
    return sorted(lst, key=len)

## Task 5: top_3_words

def top_3_words(text):
    from collections import Counter
    words = text.split()
    counts = Counter(words)
    return counts.most_common(3)

## Task 6: remove_duplicates_preserve_order

def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

## Task 7: find_intersection

def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

## Task 8: find_top_student

def find_top_student(students):
    return max(students, key=lambda s: s['score'])

## Task 9: split_even_odd

def split_even_odd(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return (evens, odds)

## Task 10: longest_sequence

def longest_sequence(lst):
    longest, current = 0, 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    return max(longest, current)

## Task 11: UserSystem Class

class UserSystem:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, user_info):
        self.users[user_id] = user_info

    def remove_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]

    def find_user(self, user_id):
        return self.users.get(user_id)

    def get_all_users(self):
        return self.users.keys()

    def update_user(self, user_id, user_info):
        if user_id in self.users:
            self.users[user_id] = user_info

# Demonstration examples

# Task demonstrations:

if __name__ == '__main__':
    print("Task 1: " , find_duplicates([1, 2, 3, 2, 1]))
    print("Task 2: " , most_frequent([1, 2, 3, 3, 2]))
    print("Task 3: " , find_pair_sum([1, 2, 3, 4], 5))
    print("Task 4: " , sort_by_length(['a', 'abc', 'ab']))
    print("Task 5: " , top_3_words('the quick brown fox jumps over the lazy dog the dog'))
    print("Task 6: " , remove_duplicates_preserve_order([1, 2, 1, 3, 2]))
    print("Task 7: " , find_intersection([1, 2, 3], [2, 3, 4]))
    print("Task 8: " , find_top_student([{'name': 'Alice', 'score': 90}, {'name': 'Bob', 'score': 95}]))
    print("Task 9: " , split_even_odd([1, 2, 3, 4]))
    print("Task 10: " , longest_sequence([1, 1, 2, 2, 2, 3, 3]))
    
    user_system = UserSystem()
    user_system.add_user('user1', {'name': 'John Doe', 'age': 30})
    user_system.add_user('user2', {'name': 'Jane Doe', 'age': 25})
    print("Users: ", user_system.get_all_users())
    user_system.remove_user('user1')
    print("Users after removal: ", user_system.get_all_users())