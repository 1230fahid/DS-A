class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #initial condition, sentence should be equal to or longer than the concatenation of all words
        if((len(words[0]) > len(s)) or ((len(words) * len(words[0])) > len(s))):
            return
        
        finalarray = []
        wordDict = {}
        perms = {}
        #make two dictionaries to store the words, for each time they appear in the given array 
        for i in words:
            if(i in wordDict.keys()):
                wordDict[i] += 1
                perms[i] += 1
            else:
                wordDict[i] = 1
                perms[i] = 1
        
        #This is to make a window for every word in the given array. Will be 2D array
        arr = []
        for i in range(0, len(words)):
            arr.append([])
        
        #####    From here on I implemented the sliding window technique a bit #####
        
        newstring = ""
        length = len(words) * len(words[0])
        j = 0
        change = len(words[0]) #this is used later on to split the given string into a new array of multiple words, each the length of a word in the given array
        num = 0
        
        i = 0
        while i < length: #get first window
            arr[j].append(s[i])
            newstring += s[i]
            i+=1
            #if the length of the array is the same as the length of a word from the input array, then increment by 1, and move to next index of new array
            if(i % change == 0): 
                j+=1
        
        #make a string of each array index and check if it's in the wordDict, and if so append 1 to it
        for j in range(0, len(arr)):
            string = ''.join(arr[j])
            if string in wordDict.keys():
                wordDict[string] += 1
        
        num = 0
        #Here I'm basically checking if the current value of an index word is two times the one in perms, because that means then that the number of words do match, since we take a string of length, (len(words[0]) * len(words)), so every words that appears in the previous for loop, we add by 1 to the corresponding value in the wordDict. So if it's a valid concatenation of all words, then there should be two times the original amount, since we are always adding by 1. If so, we use a variable called num and add by 1 and check if it's equal to the length of wordDict, because that means the string is a valid concatenation, and so we append the index 
        for word in wordDict.keys():
            if wordDict[word] == 2*perms[word]:
                num += 1
            wordDict[word] = perms[word]
        
        if(num == len(wordDict)):
            finalarray.append(0)
    
        j = 0
        i=length
        
        #Here I keep incrementing by 1, since it's a sliding window, but I also make sure to update the small windows I created, by adding the new character of each, and then saving and popping the first one, which I then use for the next window, and so on till the end 
        while i < len(s):
            j = len(words)-1
            num = 0
            char = s[i]
            
            while j > 0:
                arr[j].append(char)
                char = arr[j].pop(0)
                string = ''.join(arr[j])
                if string in wordDict.keys():
                    wordDict[string] += 1
                j -= 1
            
            arr[0].append(char)
            arr[0].pop(0)
            string = ''.join(arr[j])
            if string in wordDict.keys():
                wordDict[string] += 1
                
            for word in wordDict.keys():
                if wordDict[word] == 2*perms[word]:
                    num += 1
                wordDict[word] = perms[word]
            if(num == len(wordDict)):
                finalarray.append(i-length+1)
            i+=1
        
        return finalarray
