class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if(n == 0):
            return len(tasks)
        arr = []
        taskDict = {}
        for i in range(0, len(tasks)):
            if tasks[i] in taskDict.keys():
                taskDict[tasks[i]] += 1
            else:
                taskDict[tasks[i]] = 1
        
        for i in taskDict.keys():
            arr.append(taskDict[i])
            
        arr.sort()
        arr = arr[::-1]
        
        num = n + 1
        dictLen = len(arr)
        zeros = 0
        
        
        time = 0
        #print(arr)
        
        while(zeros != dictLen):
            num = n+1
            
            for i in range(0, len(arr)):
                if(num == 0):
                    arr.sort()
                    arr=arr[::-1]
                    break
                if(arr[i] > 0):
                    time += 1
                    arr[i] -= 1
                    if(arr[i] == 0):
                        zeros+=1
                    num -= 1
                    
            if(num == 0):
                num = n+1
                continue
            if(zeros == dictLen):
                break
            
            while(num != 0):
                time+=1
                num-=1
                
        
        return time
