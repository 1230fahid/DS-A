class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount == 0): #if no amount then well just return 0
            return 0
        greater = {}
        newcoins = []
        
        for i in range(len(coins)):
            if coins[i] > amount:
                greater[i] = 0
            else:
                newcoins.append(coins[i])
                
        #case to check if all coin values are greater than the amount. I really don't need this but thought it would help to check for this case before going into the DFS + memoization approach below, just to make it faster
        if len(coins) == len(greater):
            return -1

        arr = [0] * (amount+1)
        self.change(newcoins, amount, arr)
        
        #print(arr)
        if(arr[amount] == 0):
            return -1
        else:
            return arr[amount]
    
    
    def change(self, coins, amount, arr):
        mins = []
        for i in range(0, len(coins)):
            num = amount-coins[i]
            if(num < 0):
                continue
            elif(num == 0):
                arr[amount] = 1
                return
            if(arr[num] < 0):
                continue
            if(num > 0 and arr[num] > 0):
                mins.append(arr[num] + 1)
            else:
                self.change(coins, num, arr)
                if(arr[num] > 0):
                    mins.append(1+arr[num])
        
        
        if(len(mins) > 0):
            arr[amount] = min(mins)
        if(len(mins) == 0):
            arr[amount] = -1
            
    
    #So here what this function does it subtracts the amount by the first coin value all the way until it reaches 0 or less than 0. Then it works it's way back up, storing numbers that were calculated already, and subtracting by different coin amounts until it gets recursively to the bottom and repeats until we return back to the original amount at the end. 
    #When we are moving back up, we calculate the mininmum number of denominations needed to reach zero from there, if possible, by getting all of the stored arr[amount - coins[i]], putting them into one array, and getting the minimum from it, and assigning it to the amount
    #Try reading through code multiple time, understanding each line and rereading comments
    
    
