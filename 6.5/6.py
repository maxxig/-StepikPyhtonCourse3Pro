from collections import defaultdict

def best_sender(messages, senders):
    result_name, temp_dict = '', defaultdict(int)

    for i in range(len(messages)):
        temp_dict[senders[i]] += len(messages[i].split())

    return [k for k, v in sorted(temp_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)][0]


messages = ['hi', 'hello', 'how r u', 'i am okay', 'how r u', 'i am okay too thanks']
senders = ['Anri', 'Dima', 'Anri', 'Dima', 'Dima', 'Anri']


print(best_sender(messages, senders))