
# In this problem we have to make a pair of all the ANAGRAMS present in list of words.
# words = [no, on , is]
# ans = [[no,on],[is]]

def get_anagrams(words, n):
    hashmap = dict()
    
    # Dictionary store the sorted unique word of words as a key ans position of all those anagrams as value.
    for pos in range(n):
        word = "".join(sorted(words[pos]))
        
        if word not in hashmap:
            hashmap[word] = [pos]
        else:
            hashmap[word].append(pos)
    
    ans = []    
    for key in hashmap:
        anagram_pair = []
        for pos in hashmap[key]:
            anagram_pair.append(words[pos])
            
        ans.append(anagram_pair)
        
    return ans

def main():
    n = int(input())
    words = []
    
    for i in range(n):
        s = str(input())
        words.append(s)
        
    res = get_anagrams(words, n)

# This loop will print ANAGRAMS in different lines.
    for i in res:
        for j in i:
            print(j,end=" ")
        print()
        
main()



"""
n = 5
words[] = {act,god,cat,dog,tac}

OUTPUT : 
act cat tac
god dog
"""
        