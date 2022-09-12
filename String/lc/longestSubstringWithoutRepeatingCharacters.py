class Solution:
    #for this I used two pointers + window sliding technique + hash table
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0 or len(s) == 1):
            return len(s) #initial conditions
        lookup = {}
        num=0
        for i in s: ##This will find the inital longest sequence of unique characters
            if i in lookup.keys():
                break
            else:
                num+=1
                lookup[i] = 1
        longest=len(lookup)
        if longest == len(s): ##if the length is equal to the longest, aka, the for loop above reached to the end then return the longest
            return longest
        
        i = 0 #i will increment through string. This is the first pointer. It holds the beginning of the window, and is increased by 1, while there is a non-unique character in a substring         
        #Ex) abccbca
        while num < len(s):
            
            ## This while loop below is where window shrinks
            #Example for first iteration
            while s[num] in lookup.keys(): #first s[num] = s[3] = 'c' => [abc]cbca => abc[c]bca
                lookup[s[i]]-=1
                if lookup[s[i]] == 0:
                    del lookup[s[i]]
                i+=1  # a is removed, then b, then c
                #lookup[s[num-1]] += 1
            
            
            lookup[s[num]] = 1 #by here window is unique, so window is now abc[c]bca
            if(len(lookup) > longest):
                longest = len(lookup)
            num+=1 #go to position after end of window and check to see if it's unique, and if you can add to window. If its not then you repeat process and keep shrinking the window until everything is unique, so you can add it to the window
        return longest
    
    #This is essentially a window that shrinks, but only while the window has repeating characters. Once all characters are unique, the window stops shrinking and continues growing until it finds a character already in the window. It does this till the end of the string, and then returns the longest length of the window achieved.
