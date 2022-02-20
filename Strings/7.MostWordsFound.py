# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

def mostWordsFound(sentences):
    # Brute Force
    '''
    maxCount = 0
    for sentence in sentences:
        sentence = sentence.split()
        count = 0
        for ch in sentence:
            count += 1
        maxCount = max(maxCount, count)
        
    return maxCount
'''
    # Optimised
    count  = 0
    for sentence in sentences:
        count = max(count, len(sentence.split()))

    return count


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))
print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))