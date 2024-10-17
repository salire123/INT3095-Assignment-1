import math
class question1:
    '''
    This is a class for question 1
    a, b, c are the input for the equation
    equation() is the function for the equation
    run() is the function for the run
    '''
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def equation(self):
        x = 0
        if self.b ** 2 == 4 * self.a * self.c :
            x = -self.b / (2 * self.a)
            return x
        elif self.b ** 2 - 4 * self.a * self.c < 0 :
            # idk to write
            x = (-self.b * math.sqrt(-4 * self.a * self.c - self.b ** 2))/2 * self.a
            return None
        else:
            x = (-self.b + math.sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
        return x
    
    def run(self):
        if self.a == 0 or self.b == 0 or self.c == 0:
            return "Error, input not valid"
     
        ans = self.equation()

        return ans
        


class question2:
    '''
    This is a class for question 2
    numberlist is the input for the number list
    my_sum() is the function for the sum
    my_mean() is the function for the mean
    my_median() is the function for the median
    my_stdev() is the function for the standard deviation
    my_max() is the function for the max
    '''
    def sorted_list(list):
        list_temp = list.copy()
        list_ans  = []
        is_list_sorted = False

        while is_list_sorted == False:
            min_number_in_list_temp = float('inf')
            where_am_i_in_temp = 0
            # find the min
            for i in list_temp:
                if min_number_in_list_temp > i:
                    min_number_in_list_temp = i
                    min_place_in_temp = where_am_i_in_temp
                #move the point up
                where_am_i_in_temp +=1
            # find the min in temp and remove in temp and add in anslist
            list_ans.append(min_number_in_list_temp)
            list_temp.pop(min_place_in_temp)

            if list_temp == []:
                is_list_sorted = True
            
        return list_ans



    def __init__(self, numberlist):
        # sorted the number
        self.numberlist = sorted(numberlist)


    def my_sum(self):
        a =0
        for i in self.numberlist:
            a += float(i)
        return a
    
    def my_mean(self):
        a = 0
        b = 0
        for i in self.numberlist:
            a += float(i)
            b += 1
        #return a/len(self.numberlist)
        return a/b
        
    def my_median(self):
        a =0
        for i in self.numberlist:
            a += 1

        if 1 == a%2:
            return self.numberlist[int(a/2)]
        else:
            mid1 = a/2-1
            mid2 = a/2

            ans = (self.numberlist[int(mid1)] + self.numberlist[int(mid2)]) / 2
            return ans
 
    def my_stdev(self):
        count = 0
        for _ in self.numberlist:
            count += 1

        if count < 2:
            return 0

        mean = self.my_mean()
        n = 0
        for i in self.numberlist:
            n += (i - mean) ** 2

        # Use n-1 for sample standard deviation
        squared_diff_sum = n / (count - 1)
        return math.sqrt(squared_diff_sum)

    
    def my_max(self):
        return self.numberlist[-1]

