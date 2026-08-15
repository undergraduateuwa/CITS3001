from typing import List
from collections import deque

class Solutions:

    def Merge_Sorted_Array(self, nums1: List[int], m: int, nums2: List[int], n: int):
        if n == 0:
            return
        p  = m + n -1
        p1 = m-1
        p2 = n-1
        while(p!=-1 and p2!=-1):
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1-= 1
                p -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1

            if p1 == -1:
                for i in range(0,p+1):
                    nums1[i] = nums2[i];
                break;

    def Remove_Element(self, nums: List[int], val: int):
        l = len(nums)
        k = 0;
        if l == 0:
            return
        s = 0;
        f = 0;
        while(f < l):
            if(nums[f] != val):
                nums[s] = nums[f]
                f+=1;
                s+=1;
            else:
                k+=1
                f+=1
        return l-k
    def leetcode26(self, nums: List[int]):
        l = len(nums);
        if l == 0:
            return 0;
        s = 0
        f = s+1

        while(f < l):
            if(nums[s] == nums[f]):
                f+=1

            else:
                s+=1;
                nums[s] = nums[f]
                f+=1
        return s+1

    def leetcode80(self, nums: List[int]):
        l = len(nums)
        if l<3 :
            return l;

        f = 2
        s = 2
        # f s are 2 pointers starts at index 2, indicates we neglect first 2 elements as they always remain ;
        # Always start the pointer at same position;
        while(f < l):
            if nums[f] == nums[s-2]:
                # Decide if we meet a triple repetition;
                f+=1;
                # forward f pointer to find the first none repetition elements;
            else:
                nums[s] = nums[f]
                # Over-write the current s pointer as we include the element;
                f+=1
                s+=1
                # Forward f and s together
        return s;

    def leetcode169(self, nums: List[int]):
        count = 0;
        # count the number of current candidate
        # if this goes zero then we induce that the number of current candidates isn't n/2
        candidate = 0;
        for n in nums:
            if count == 0:
                candidate = n
            # change candidate
            if candidate == n:
                count += 1
            else:
                count -= 1

        return candidate

    def leetcode189(self, nums: List[int], k: int):

        l = len(nums)
        k %= l

        nums[:] =  nums[l-k:] +  nums[:l-k]
        # list[:a] for all first ath elements
        # list[a:] for all elements after ath elements
        # list[:-a] last a elements
        # list[-a:] all but last k

        return nums

    def leetcode121(self, prices: List[int]):
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for n in prices:

            profit = n - min_price
            if n < min_price:
                min_price = n

            if max_profit < profit:
                max_profit = profit

        return max_profit

    def leetcode122_dp(self, prices: List[int]):
        if not prices:
            return 0

        past_sold = 0
        past_buyin = -prices[0]

        for p in prices:
            # 状态转移方程为：
            # 每一天都有两种状态 即：
            # 1.手中没有股票：按照今天的价格，把股票全部出掉了 或者 之前就已经清仓 今天没有补货
            # 2.手中持有股票：按照今天的价格，购入了股票，或者 之前就有持仓 今天没有卖出
            # 两种状态同时记录 都选取每种状态对应的两种情况中 盈利最多的计入状态方程
            # 我们只需要维护 past_sold past_buyin即可

            past_sold = max(past_sold, p + past_buyin)
            past_buyin = max(past_buyin, past_sold - p)

        return past_sold

    def leetcode122_greedy(self, prices: List[int]):

        if not prices:
            return 0

        r = 0
        f = 1
        l = len(prices)
        balance = 0
        while f < l:
            if prices[f] > prices[r]:
                balance += prices[f] - prices[r]
            #     只要第二天比第一天的价格高 我们就在第一天买入 第二天卖出

            f+=1
            r+=1
        return balance

    def leetcode55_dp(self, nums: List[int]):
        l = len(nums)
        dp = [-1] * l
        dp[0] = 1
        # 转移方程为：
        # 如果 当前位置的之前某一位可达到
        # 并且 这一位可以跳到当前位置
        # 那么 当前位置也可以达到
        for i in range(1,l):
            for j in range (i):
                if dp[j] == 1 and nums[j] + j >= i:
                    dp[i] = 1
                    break
        return dp[l-1]==1

    def leetcode55_greedy(self, nums: List[int]):

        l = len(nums)
        flag = False
        cover = nums[0]
        # cover即当前位置的覆盖范围
        i = 0;
        while i <= cover:

            if i+nums[i] > cover:
                cover = i+nums[i]
            #    如果当前位置的覆盖范围更大 我们更新覆盖范围
            if cover >= l-1:
                flag = True
                # 如果 最后一位落在当前的覆盖范围中 我们认为最后一位可以达到
                break
            i+=1

        return flag

    def leetcode134(self, gas: List[int], cost: List[int]):

        cur_sum = 0
        start_at = 0

        if sum(gas) < sum(cost):
            return -1
        #如果整体来讲是加油大于消耗油，那么就一定存在一个起始点 可以anticlock遍历所有的点一圈

        for i in range(len(gas)):
            surplus = gas[i] - cost[i]
            #计算在本点加油后 出发下一个点 油箱的盈余
            cur_sum += surplus
            #如果油箱为空甚至为负，那么就认为 从目前的起始点 是无法到达本点的
            if cur_sum < 0:
                start_at = i + 1
                cur_sum = 0
                #所以 重置当前的start_at 为当前节点+1

        return start_at

    def leetcode135(self, ratings: List[int]):
        res = [1]*len(ratings)
        l = len(ratings)
        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                # 从左往右遍历，如果next比当前大，那么就给下一个增1
                res[i] = res[i-1] + 1

        for i in range(l-1,0,-1):
            if ratings[i-1] > ratings[i]:
                # 从右往左遍历，如果下一个比当前的大，那么就取 当前自增1 和 下一个 中较大的哪个
                res[i-1] = max(res[i]+1,res[i-1])


        return sum(res)

    def leetcode13(self, s: str):

        my_hash = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res  = 0
        for i in range(len(s)-1) :
            if(my_hash[s[i]] < my_hash[s[i+1]]):
                res -= my_hash[s[i]]

            else:
                res += my_hash[s[i]]

        res += my_hash[s[-1]]

        return res

    def leetcode42(self, height: List[int]):
        l = len(height)
        r_max = [0]*l
        l_max = [0] * l
        # 利用前缀法的思路,lmax记录当前index之前最大的数,rmax记录当前index之后最大的数

        res = 0
        for i in range(1,l):
            l_max[i] = max(height[i-1],l_max[i-1])
        #     查找当前下标之前最大的数

        for i in range(l-2,-1,-1):
            r_max[i] = max(height[i+1],r_max[i+1])
        #     查找当前下标之后最大的数

        for i in range(l):
            diff = min(l_max[i],r_max[i]) - height[i]
            # 当前下标上能存储的雨水,取决于左最大和右最大中比较小的那一个与当前下标高度做diff
            if diff > 0:
                res += diff
        return res

    def leetcode42_rearrange(self, height: List[int]):
        # 这个绝妙的解法利用了两次加法的交换率 即 (a+b) + (c+d) = a+d + c + b
        l = len(height)
        r_max = height[-1]
        l_max = height[0]
        sum = 0
        for i in range(0,l):
            # 每个index可以积蓄的雨水,等同于左边最大与右边最大中较小者与当前index的高度做差
            # 整个数组可以积蓄的雨水,等同于每个点积蓄的雨水之和
            # 也就是 total = sum(Wi) = sum(min(lmax,rmax)-height[i])
            # 由数学定义 min(lmax,rmax) = lmax + rmax -max(lmax,rmax)
            # 那么 total = sum(lmax + rmax -max(lmax,rmax)-height[i])
            l_max = max(l_max,height[i])
            r_max = max(r_max,height[l-1-i])
            sum += r_max + l_max -height[i]
            # sum(lmax + rmax -height[i]) 中lmax和rmax可以由加法交换律 任意匹配 也就是
            # index为1 的lmax 可以与 index 为len-1-1的rmax相结合 这样的好处是可以用一个正向循环把lmax和 rmax同时维护
        return sum - l* r_max
            # max(lmax,rmax) 一定等于全数组最大值,即gmax,借此 我们可以使用加法交换律提出每一个点上的max(lmax,rmax) 为gmax
            # 即 total = sum(lmax + rmax -height[i]) - len*gmax

    def leetcode12(self, num: int):
        roman_map = {
            # 个位 (Ones)
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',0:"",

            # 您跳过了十位 (10-90)，为了完整性我补在这里，如果不需要可以删除
            10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L',
            60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',

            # 百位 (Hundreds)
            100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
            600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',

            # 千位 (Thousands) - 标准写法通常截止于 3000 (MMM)
            1000: 'M',
            2000: 'MM',
            3000: 'MMM',
        }
        res = ""
        dvd = 1000
        while dvd >= 1:
            res += roman_map[(num//dvd)*dvd]
            num %= dvd
            dvd /= 10

        return res
    def leetcode58(self, string: str) -> int:
        count = 0
        string=string.strip()
        for i in range(len(string)-1,-1,-1):
            if string[i] == ' ':
                break
            count+=1
        return count

    def leetcode14(self, strs: List[str]):
        if not strs:
            return ""

        # 1. 找出最短长度 (为了防止 i 越界)
        min_len = 201
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)

        # 2. 外层循环：扫描第 i 个字符
        for i in range(min_len):
            # 内层循环：比较列表中相邻的两个字符串
            for j in range(len(strs) - 1):  # 注意：这里是 len(strs)
                if strs[j][i] != strs[j + 1][i]:
                    # 一旦发现不匹配，立刻截取并返回前面的部分
                    return strs[0][:i]

                    # 3. 如果循环全部跑完，说明最短的那个字符串就是公共前缀
        return len(strs[0][:min_len])

    def leetcode151(self, s: str):

        words = s.split()
        words.reverse()


        return " ".join(words)

    def leetcode6(self, s: str, numRows: int):
        if numRows == 1:
            return s
        step = -1
        cur_row = 0
        res = [""] * numRows
        for c in s:

            res[cur_row] += c
            if cur_row == numRows-1 or cur_row == 0:
                # 如果触底或者碰到天花板 步长反转
                step = -step


            cur_row += step

        return "".join(res)

    def leetcode28(self, haystack: str, needle: str):
        l = 0
        h = len(haystack)
        n = len(needle)
        while l <= h-n :
            # 如果一直到h-n都无法匹配 那么后面的都不用看，因为长度都不够，肯定无法匹配
            if haystack[l] == needle[0]:
                # 当第一个字符匹配上之后在进行后续的匹配
                f = 0
                # f必须要在内循环外面更新
                while True:
                    if haystack[l+f] != needle[f]:
                        break
                    if f == len(needle)-1:
                        return l
                    f += 1
            l+=1

        return -1

    # def leetocde68(self, words: List[str], maxWidth: int):
    #     lens = [0] * len(words)
    #     res = []
    #     i = 0
    #     dq = deque([])
    #     for w in words:
    #         lens[i] = len(w)
    #         i+=1
    #     c_words = 0
    #     c_width = 0
    #     for c_words in range (len(words)):
    #         if c_width + lens[c_words] < maxWidth:
    #             dq.append(words[c_words])
    #             c_width += (lens[c_words]+1)
    #         else:
    #             ele = dq.pop()
    #             c_width = 0
    #             tube = ""
    #             spaceNum = len(dq)
    #             while ele != None:
    #
    #     return res

    def leetcode125(self, s: str):
        res = True
        s = "".join([char for char in s if char.isalnum()])
        s = s.lower()
        r = 0
        f = len(s) - 1
        while r < f:
            if s[r] != s[f]:
                res = False
            r += 1
            f -= 1
        return res

    def leetcode392(self,s:str,t:str):
        i = 0
        j = 0
        ls = len(s)
        lt = len(t)
        if ls > lt:
            return False
        if ls == 0:
            return True
        while j < lt:
            if s[i] == t[j]:
                while i < ls and j < lt:
                    if s[i] == t[j]:
                        j+=1
                        i+=1
                    else:
                        break

                if i == ls:
                    return True
            j += 1
        return False

    def leetcode167(self, numbers: List[int], target: int):
        r = 0
        f = len(numbers)-1
        res = []
        while f > r:
            cur = numbers[f] + numbers[r]
            if cur > target:
                f -= 1
            elif cur < target:
                r += 1
            else:
                res.append(r+1)
                res.append(f+1)
                break
        return res

    def leetcode11(self, height: List[int]):
        res = 0
        r = 0
        f = len(height)-1
        while f > r:
            cur = (f-r) * min(height[f],height[r])
            if res < cur:
                res = cur
            if height[f] > height[r]:
                r += 1
            else:
                f -= 1
        return res

    def leetcode15(self, nums: List[int]):
        nums.sort()
        # 先排序
        # 思路是将三元素转换为之前熟悉的两元素
        # 即 求a+b+c = 0
        # 转换为 a+b = -c
        # 进行ab两元素的求解即可
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                # 为了保证没有重复组，我们对三个指针都进行去重
                # 去重的方法都是一样的，即如果i指针与i-1指针数值上相同，那么就跳过当前的i
                continue
            r = i + 1
            f = len(nums) -1
            target = -nums[i]
            while f > r:
                if nums[r] + nums[f] > target:
                    f -= 1
                elif nums[r] + nums[f] < target:
                    r += 1
                else:
                    res.append([nums[i],nums[r],nums[f]])
                    while r < f and nums[r] == nums[r+1]:
                        r += 1
                    while r < f and nums[f] == nums[f-1]:
                        f -= 1
                    # 对r 和 f指针进行去重
                    r += 1
        return res
    
    def leetcode209(self, target: int, nums: List[int]):
        res = float("inf")
        r = 0
        f = 0
        l = len(nums)
        cur_sum = 0

        while f != l:
            if cur_sum < target:
                # 如果当前cursum小于目标值，那么窗口伸展来包括更多的值
                cur_sum += nums[f]
                f += 1

            while cur_sum >= target and r <= f:
                # 如果cursum大于目标值，我们的窗口左边缘内收来尝试从左边去除已经包括的值
                res = min(f-r,res)
                cur_sum -= nums[r]
                r += 1

        if res == float("inf"):
            # 如果当前结果没有被修改过
            res = 0
        return res

    def leetcode3(self, s: str) -> int:
        # 哈希表：记录字符 -> 字符最后出现的索引
        char_map = {}
        left = 0
        max_len = 0

        # right 从 0 开始遍历整个字符串
        for right, char in enumerate(s):

            # 核心逻辑：如果字符在窗口中重复出现了
            if char in char_map:
                # 更新 left 指针
                # 注意：这里必须取 max，防止 left 回退！
                # 比如 "abba"，遇到第二个 'a' 时，left 已经在 'b' 那里了，不能回到第一个 'a' 后面
                left = max(left, char_map[char] + 1)

            # 更新当前字符的最新位置
            char_map[char] = right

            # 计算当前窗口长度，并尝试刷新最大值
            # 窗口长度 = right - left + 1
            max_len = max(max_len, right - left + 1)

        return max_len

    def leetcode76(self, s: str, t: str) -> str:
        f = 0
        r = 0
        hash_s = {}
        # 用来记录所有字母出现的个数
        hash_t = {}
        # 用来记录目标字符出现的个数
        res = s
        cur_contains = 0
        # 用来记录一共出现了多少个目标字符，如果cur_contains==len(t)
        # 那么就是说所有的目标字符都已经出现了
        flag = False
        # 用来记录s是否至少有一个子串包含完整的t

        for ts in t:
            if ts not in hash_t:
                hash_t[ts] = 1
            else:
                hash_t[ts] += 1

        while True:
            # 如果字符串t中的每一个字母目前都已经出现过
            # 开始从左边收缩视窗，检查当前字符串是否依旧包含所有的目标字符
            # 如果当前字符串不再包含每一个目标字符，我们随即向右扩张
            while cur_contains >= len(t) and r < f:
                flag = True
                hash_s[s[r]] -= 1
                if s[r] in hash_t and hash_s[s[r]] < hash_t[s[r]]:
                    cur_contains -= 1
                if len(res) > (f - r):
                    res = s[r:f]
                r += 1
            if f >= len(s):
                break

            if s[f] not in hash_s:
                hash_s[s[f]] = 1
            else:
                hash_s[s[f]] += 1

            if s[f] in hash_t:
                if hash_s[s[f]] <= hash_t[s[f]]:
                    cur_contains += 1
            f += 1

        if not flag:
            return ""
        return res

    from typing import List

    def leetcode30(self, s: str, words: List[str]) -> List[int]:
        # 这个题思路与76题一致

        if not s or not words: return []
        step = len(words[0])
        hash_w = {}
        res = []

        # 预处理 hash_w
        # 因为words里面word的长度是一致的，所以
        # 我们把words里面所有的单词都取出来，放到一个hash里面
        for word in words:
            hash_w[word] = hash_w.get(word, 0) + 1

        for i in range(step):
            # 最外层的循环负责对齐
            # 比如 s = wordsixgoodbestworld list[word,good]
            # six长度为3，会打乱我们取数的节奏
            # 所以 我们使用i来修正这一点
            f = i
            r = i
            hash_s = {}
            cur_contains = 0

            while f + step <= len(s):

                temp = s[f:f + step]
                if temp in hash_w:
                    cur_contains += 1
                    if temp not in hash_s:
                        hash_s[temp] = 1
                    else:
                        hash_s[temp] += 1

                    while hash_s[temp] > hash_w[temp]:
                        # 如果一个单词在s中出现的次数高于在list中的次数
                        # 我们就要开始一步一步收缩r
                        # 直到次数相等为止
                        cur_contains -= 1
                        hash_s[s[r:r + step]] -= 1
                        r += step

                    f += step
                    if cur_contains == len(words):
                        res.append(r)
                        temp = s[r:r + step]
                        cur_contains -= 1
                        hash_s[temp] -= 1
                        r += step

                else:
                    # 当前的s中的word在words里面不存在，我们直接忽略这个word之前所有的字符
                    f += step
                    r = f
                    cur_contains = 0
                    hash_s = {}


        return res

    def leetcode36(self, board: List[List[str]]):
        rows = [[0] * 10 for _ in range(9)]
        cols = [[0] * 10 for _ in range(9)]
        boxs = [[0] * 10 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                num = int(char)
                if rows[r][num] or cols[r][num] or boxs[(r // 3) * 3 + (c // 3)][num]:
                    return False
                rows[r][num] = 1
                cols[r][num] = 1
                boxs[(r // 3) * 3 + (c // 3)][num] = 1
        return True

    def leetcode54(self, matrix: List[List[int]]):
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1
        # 设置左右上下四个边界
        res = []
        while True:
            for i in range(l,r+1,1):
                res.append(matrix[t][i])

            t += 1
            # 从上读完一行后，上边界下移一位
            if t > b:
                break

            for i in range(t,b+1,1):
                res.append(matrix[i][r])

            r -= 1
            # 从右读完一列后，右边界左移一位
            if r < l:
                break

            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b -= 1
            # 从下读完一行后，下边界上移一位
            if t>b:
                break

            for i in range(b,t-1,-1):
                res.append(matrix[i][l])

            l += 1
            # 从左读完一列后，左边界右移一位
            if l>r:
                break

        #     终止条件为，左右边界交叉或者上下边界交叉
        return res

    def leetcode48(self, matrix: List[List[int]]):
        # 这是个数学题，我们可以采用，想要达到效果 需要两步
        # 转置矩阵
        # reverse矩阵中的每一行
        bound = len(matrix)
        i = 0
        j = 0
        count = 0
        while True:
            if bound == 1:
                break
            while count < bound:
                temp = matrix[i][j+count]
                matrix[i][j+count] = matrix[i+count][j]
                matrix[i+count][j] = temp
                count += 1
            bound -= 1
            count = 0
            i += 1
            j += 1

        for i in range(len(matrix)):
            matrix[i].reverse()

    def leetcode73(self, matrix: List[List[int]]):
        len_r = len(matrix)
        len_c = len(matrix[0])
        # 检测初始值，0行0列是否有0
        row0_has_zero = any(matrix[0][j] == 0 for j in range(len_c))
        col0_has_zero = any(matrix[i][0] == 0 for i in range(len_r))


        # 遍历除去0行0列的数组，如果为0
        # 则把该数字所在的行头与列头都标记为0
        for r in range(1,len_r):
            for c in range(1,len_c):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1,len_r):
            if matrix[r][0] == 0:
                # 根据0列标记，将对应的行重置为0
                matrix[r] = [0] * len_c

        for c in range(1,len_c):
            if matrix[0][c] == 0:
                # 根据0行标记，将对应的列重置为0
                for r in range(len_r):
                    matrix[r][c] = 0
        # 最后处理0行0列
        if row0_has_zero:
            matrix[0] = [0] * len_c

        if col0_has_zero:
            for i in range(len_r):
                matrix[i][0] = 0

    def leetcode289(self, board: List[List[int]]):
        l_c = len(board[0])
        l_r = len(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                counter = 0
                # 上
                if i >0 and board[i-1][j] in [1, 2]:
                    counter += 1
                # 下
                if i+1 < l_r and board[i+1][j] in [1, 2]:
                    counter += 1
                # 左
                if j>0 and board[i][j-1] in [1, 2]:
                    counter += 1
                # 右
                if j+1 < l_c and board[i][j+1] in [1, 2]:
                    counter += 1
                # 左上
                if i > 0 and j>0 and board[i-1][j-1] in [1, 2]:
                    counter += 1
                # 左下
                if i+1 < l_r and j>0 and board[i+1][j-1] in [1, 2]:
                    counter += 1
        #         右上
                if i>0 and j+1 < l_c and board[i-1][j+1] in [1, 2]:
                    counter += 1
        #         右下
                if i+1 < l_r and j+1< l_c and board[i+1][j+1] in [1, 2]:
                    counter += 1

                if board[i][j] == 1 and (counter < 2 or counter > 3):
                    board[i][j] = 2
                if board[i][j] == 0 and counter == 3:
                    board[i][j] = 3

        for i in range(l_r):
            for j in range(l_c):
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1

    def leetcode383(self, ransomNote: str, magazine: str):
        mgz = {}

        if len(ransomNote) > len(magazine):
            return False
        for c in magazine:
            if c in mgz:
                mgz[c] += 1
            else:
                mgz[c] = 1

        for c in ransomNote:
            if c in mgz and mgz[c] > 0:
                mgz[c] -= 1
            else:
                return False

        return True

    def leetcode205(self, s: str, t: str):
        hash_s = {}
        hash_t = {}
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        # 双向映射，abb cdd 为例
        # a映射为c c同时映射为a
        # b映射为d d同时映射为b
        for i in range(ls):
            if (s[i] not in hash_s) and ( t[i] not in hash_t):
                hash_s[s[i]] = t[i]
                hash_t[t[i]] = s[i]

            elif (s[i] in hash_s) and ( t[i] in hash_t):
                if hash_s[s[i]] == t[i] and hash_t[t[i]] == s[i]:
                    continue
                else:
                    return False
            else:
                return False

        return True
    def leetcode290(self, pattern: str, s: str):
        hash_p = {}
        hash_s = {}
        s = s.split(" ")
        len_s = len(s)
        len_p = len(pattern)
        if len_s != len_p:
            return False
        for i in range(len_s):
            if (s[i] not in hash_s) and (pattern[i] not in hash_p):
                hash_s[s[i]] = pattern[i]
                hash_p[pattern[i]] = s[i]
            elif (s[i] in hash_s) and (pattern[i] in hash_p):
                if (hash_s[s[i]] == pattern[i]) and (hash_p[pattern[i]] == s[i]):
                    continue
                else:
                    return False
            else:
                return False
        return True
    def leetcode242(self, s: str, t: str):
        hash_s = {}
        if len(s) != len(t):
            return False
        for c in s:
            if c not in hash_s:
                hash_s[c] = 1
            else:
                hash_s[c] += 1
        for c in t:
            if c not in hash_s:
                return False
            else:
                hash_s[c] -= 1
        for v in hash_s.values():
            if v != 0:
                return False
        return True
    def leetcode49(self, strs: List[str]):

        res = {}
        for s in strs:
            key_list = [0] * 26
            # 我们使用数组来记录每个单词中字符出现的频次
            for c in s:
                key_list[ord(c) - ord('a')] += 1
            # 把不可hash可变的list变成不可变的tuple作为我们res hash的key
            key_tuple = tuple(key_list)
            if key_tuple not in res:
                res[key_tuple] = []
                res[key_tuple].append(s)
            else:
                res[key_tuple].append(s)
        return list(res.values())

    def leetcode1(self, nums: List[int], target: int):
        hash_s = {}
        res = []
        for i in range(len(nums)):
            if target-nums[i] not in hash_s:
                hash_s[nums[i]] = i
            else:
                res.append(i)
                res.append(hash_s[target-nums[i]])

        return res

    def leetcode202(self, n: int):
        seen = []
        while True:
            t = 0
            while n != 0:
                digit = n % 10
                t += digit * digit
                n = n // 10
            if t not in seen :
                seen.append(t)
                n = t
            elif t == 1:
                return True
            else:
                return False
    def leetcode219(self, nums: List[int], k: int):
        hash_s = {}
        for i in range(len(nums)):
            if nums[i] not in hash_s:
                hash_s[nums[i]] = i
            else:
                if abs(i - hash_s[nums[i]]) <= k:
                    return True
                else:
                    hash_s[nums[i]] = i
        return False

    def leetcode128(self, nums: List[int]):
        if not nums:
            return 0
        # 首先，排除空字符串
        myset = set(nums)
        # set化目的有两个，首先是去重，其次是每次查找元素的时间复杂度是O(1)
        res = -1

        for ele in myset:
            cur_mx = 0
            if ele-1 not in myset:
                # 如果 ele-1 在我们的set里面，就说明当前ele不是任何一个可能序列的开头，所以跳过
                temp = ele + 1
                cur_mx += 1
                while temp in myset:
                    # 探测当前开头的长度
                    cur_mx += 1
                    temp += 1
                if cur_mx >= res:
                    res = cur_mx
        #             维护全局最大值
        return res

    def leetcode228(self, nums: List[int]):
        res = []
        i = 0
        n = len(nums)
        while i < n:
            start = i  # 记录区间起点
            # 向后寻找连续的终点
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            # 此时 nums[i] 是区间的终点
            if start == i:
                res.append(str(nums[start]))
            else:
                res.append(f"{nums[start]}->{nums[i]}")
            i += 1  # 准备开始寻找下一个区间
        return res

    def leetcode56(self, intervals: List[List[int]]):
        intervals.sort(key = lambda x : x[0])
        res = []
        i = 0
        while i < len(intervals):
            start = intervals[i][0]
            end = intervals[i][1]
            # 维护当前终点为最大值
            while i < len(intervals)-1 and end >= intervals[i+1][0]:
                # 如果当前的终点比下一个区间的终点大，那么就合并下一个区间
                end = max(end, intervals[i+1][1])
                i += 1

            ele = [start, end]
            res.append(ele)
            i += 1
        return res

    def leetcode57(self, intervals: List[List[int]], newInterval: List[int]):
        res = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i+=1

        end = intervals[i][1]
        start = intervals[i][0]

        while i < n and intervals[i][0] <= newInterval[1]:
            # 只要当前的开始时间 <= 新区间的结束时间，就有重叠
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < n :
            res.append(intervals[i])
            i += 1

        return res




if __name__ == "__main__":
    sol = Solutions()
    # sol.Merge_Sorted_Array([1] 1, [], 0)
    # print(f"Test 1 Result: {n1}")
    # print(sol.Remove_Element([3,2,2,3],3))
    # print(sol.leetcode26([0,0,1,1,1,2,2,3,3,4]))
    # print(sol.leetcode80([1,1,1,2,2,3]))
    # print(sol.leetcode169([1,2,2,2,2,3]))
    # print(sol.leetcode189([1,2,3,4,5,6,7,8,9],3))
    # print(sol.leetcode121([7,1,5,3,6,4]))
    # print(sol.leetcode122_greedy([5,4,3,2,1]))
    # print(sol.leetcode122_dp([7,1,5,3,6,4]))
    # print(sol.leetcode55_dp([3,2,1,0,4]))
    # print(sol.leetcode55_greedy([0,1]))
    # print(sol.leetcode134([1,2,3,4,5],[3,4,5,1,2]))
    # print(sol.leetcode135([1,3,2,2,1]))
    # print(sol.leetcode13("MCMXCIV"))
    # print(sol.leetcode42([4,2,0,3,2,5]))
    # print(sol.leetcode42_rearrange([4,2,0,3,2,5]))
    # print(sol.leetcode12(58))
    # print(sol.leetcode14(["flower","flow","flight"]))
    # print(sol.leetcode151("a good   example"))
    # print(sol.leetcode6("PAYPALISHIRING",4))
    # print(sol.leetcode28("aaabaaabbbabaa","babb"))
    # print(sol.leetocde68(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
    # print(sol.leetcode125("A man, a plan, a canal: Panama"))
    # print(sol.leetcode392("abc","ahbgdc"))
    # print(sol.leetcode167([2,7,11,15],9))
    # print(sol.leetcode11([1,8,6,2,5,4,8,3,7]))
    # print(sol.leetcode15([-1,0,1,2,-1,-4]))
    # print(sol.leetcode209(5,[2,3,1,1,1,1,1]))
    # print(sol.leetcode3("abcabcbb"))
    # print(sol.leetcode76("aaaaaaaaaaaabbbbbcdd","abcdd"))
    # print(sol.leetcode30("wordgoodgoodgoodbestword",  ["word","good","best","good"]))
    # print(sol.leetcode36([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"] ,["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."] ,[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
    # print(sol.leetcode54([[1,2,3],[4,5,6],[7,8,9]]))
    # print(sol.leetcode48([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
    # print(sol.leetcode73([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    # print(sol.leetcode289([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
    # print(sol.leetcode383("aa","aab"))
    # print(sol.leetcode205("bbbaaaba","aaabbbba"))
    # print(sol.leetcode290("abba","dog cat cat fish"))
    # print(sol.leetcode242("anagram","nagaram"))
    # print(sol.leetcode49(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(sol.leetcode1([3,2,4], 6))
    # print(sol.leetcode202(19))
    # print(sol.leetcode219([1,0,1,1],1))
    # print(sol.leetcode228([0,2,3,4,6,8,10]))
    # print(sol.leetcode56([[4,7],[1,4]]))
    print(sol.leetcode57([[1,3],[6,9]],[2,5]))







