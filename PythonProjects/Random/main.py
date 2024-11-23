# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(-2, 2, 1000)
# y = x**4 - 3*x**2 + 2
#
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, label='f(x) = x^4 - 3x^2 + 2')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plot of a Nonconvex Function')
# plt.legend()
# plt.grid(True)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.linspace(-2*np.pi, 2*np.pi, 1000)
# a = .10
# y = a * x + np.sin(x)
#
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, label='f(x) = 0.5x + sin(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plot of a Linear Nonconvex Function')
# plt.legend()
# plt.grid(True)
# plt.show()

# PE

# Problem 1
# def number(num):
#     sum = 0
#     for n in range(num):
#         if n%3==0 or n%5==0:
#             sum = sum + n
#     print(sum)
#
# number(1000)

# Problem 2
# def fibonacci(n):
#     temp_1 = 1
#     temp_2 = 2
#     value = 0
#     for i in range(1, n+1):
#         if i == 1:
#             print(temp_1)
#         elif i == 2:
#             print(temp_2)
#         else:
#             sum = temp_1 + temp_2
#             if sum > 4000000:
#                 print(i)
#                 break
#             temp_1 = temp_2
#             temp_2 = sum
#             print(sum)
#             if sum % 2 == 0:
#                 value += sum
#     print(value)
#
# fibonacci(33)

# Problem 6
# def def_a_num(n):
#     sq_sum = 0
#     sum_sq = 0
#     sum = 0
#     for i in range(1, n):
#         sq_sum = i*i + sq_sum
#         sum += i
#     print(sq_sum)
#     print(sum**2)
#     print(sum**2 - sq_sum)
# def_a_num(101)

# Problem 6
# def division():
#     n = 2
#     while n < 10:
#         i = 2
#         while i < 100:
#             if n >= i and n % i == 0:
#                 print(n)
#                 #print(i)
#                 i += 1
#             else:
#                 n += 1
#
# division()

# Problem 5
# def div(n):
#
#     continue_loop = True
#     while continue_loop:
#         count = 0
#         i = 1
#         while i < 21:
#             if n % i == 0:
#                 count += 1
#             i += 1
#         if count == 20:
#             print(n)
#             continue_loop = False
#         n += 10
#
# div(1000)

# Problem 3
# def is_prime(iter):
#     for i in range(2, int(iter**0.5)+1):
#         if iter % i == 0:
#             return False
#     return True
#
# def large_prime(num):
#     n = 2
#     while n < num:
#         if num % n == 0:
#             if is_prime(n):
#                 print(n)
#                 n = num
#         n += 1
# large_prime(600851475143)


# Problem 4
# def is_palindrome(number):
#     number_str = str(number)
#     if number_str == number_str[::-1]:
#         print(number)
#         return True
#     else:
#         return False


# Problem 4
# def mul():
#     list = []
#     for n in range(999, 100, -1):
#         for i in range(999, 100, -1):
#             product = n * i
#             if is_palindrome(product):
#                 list.append(product)
#                 break
#     print(sorted(list))
# mul()

# Problem 7
# def is_prime():
#     number = 2
#     count = 0
#     while count < 10001:
#         is_prime = True
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(number)
#             count += 1
#         number += 1
# is_prime()


# Problem 9
# def py_triplets():
#     for a in range(1,1000):
#         for b in range(a+1, 1000-a):
#             c = 1000 - a - b
#             if a*a + b*b == c*c:
#                 print(f"{a}, {b}, {c}")
#                 print(a*b*c)
# py_triplets()


# Problem 8
# def multiply_digits(number):
#     list = []
#     num_str = str(number)
#     product = 1
#     i = 0
#     while i < len(num_str)-12:
#         product = int(num_str[i]) * int(num_str[i+1]) * int(num_str[i+2]) * int(num_str[i+3]) \
#                   * int(num_str[i+4]) * int(num_str[i+5]) * int(num_str[i+6]) * int(num_str[i+7]) \
#                   * int(num_str[i+8]) * int(num_str[i+9]) * int(num_str[i+10]) * int(num_str[i+11]) \
#                   * int(num_str[i+12])
#         list.append(product)
#         i += 1
#     print(product)
#     print(sorted(list)[-1])
#
# num = """731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450"""
# num = num.replace("\n", "")
# multiply_digits(int(num))

# Problem 10
# def is_prime():
#     number = 2
#     list = []
#     while number < 2000000:
#         is_prime = True
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             #print(number)
#             list.append(number)
#         number += 1
#     print(list)
#     print(sum(list))
# is_prime()


# Problem 10
# def sum_of_primes(limit):
#     # Initialize a boolean array where True represents a prime number
#     sieve = [True] * limit
#     sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
#
#     # Mark multiples of each prime starting from 2
#     for num in range(2, int(limit ** 0.5) + 1):
#         if sieve[num]:  # If `num` is still marked as prime
#             for multiple in range(num * num, limit, num):
#                 sieve[multiple] = False  # Mark multiples of `num` as not prime
#
#     # Sum all numbers still marked as prime
#     primes_sum = sum(i for i, is_prime in enumerate(sieve) if is_prime)
#     print(primes_sum)
#
# # Find the sum of all primes below 2 million
# sum_of_primes(2000000)

# Problem 16
# def exp_sum():
#     sum = 0
#     num = 2 ** 1000
#     num_str = str(num)
#     for i in range(0, len(num_str)):
#         sum += int(num_str[i])
#     print(sum)
#
# exp_sum()

# Problem 20
# import math
# def fact_digit_sum(number):
#     fact_sum = 0
#     factorial = math.factorial(number)
#     num_str = str(factorial)
#     for i in range(0, len(num_str)):
#         fact_sum += int(num_str[i])
#     print(factorial)
#     print(fact_sum)
# fact_digit_sum(100)

# Problem 13
# import sys
# def sum_10(num):
#     sys.set_int_max_str_digits(100000)
#     iterative_num = ""
#     num_list = []
#     for i in range(0, 100):
#         for j in range(0, 50):
#             iterative_num = num[i*50 : (i+1)*50]
#         num_list.append(int(iterative_num))
#     print(sum(num_list))
#
# number = """37107287533902102798797998220837590246510135740250
# 46376937677490009712648124896970078050417018260538
# 74324986199524741059474233309513058123726617309629
# 91942213363574161572522430563301811072406154908250
# 23067588207539346171171980310421047513778063246676
# 89261670696623633820136378418383684178734361726757
# 28112879812849979408065481931592621691275889832738
# 44274228917432520321923589422876796487670272189318
# 47451445736001306439091167216856844588711603153276
# 70386486105843025439939619828917593665686757934951
# 62176457141856560629502157223196586755079324193331
# 64906352462741904929101432445813822663347944758178
# 92575867718337217661963751590579239728245598838407
# 58203565325359399008402633568948830189458628227828
# 80181199384826282014278194139940567587151170094390
# 35398664372827112653829987240784473053190104293586
# 86515506006295864861532075273371959191420517255829
# 71693888707715466499115593487603532921714970056938
# 54370070576826684624621495650076471787294438377604
# 53282654108756828443191190634694037855217779295145
# 36123272525000296071075082563815656710885258350721
# 45876576172410976447339110607218265236877223636045
# 17423706905851860660448207621209813287860733969412
# 81142660418086830619328460811191061556940512689692
# 51934325451728388641918047049293215058642563049483
# 62467221648435076201727918039944693004732956340691
# 15732444386908125794514089057706229429197107928209
# 55037687525678773091862540744969844508330393682126
# 18336384825330154686196124348767681297534375946515
# 80386287592878490201521685554828717201219257766954
# 78182833757993103614740356856449095527097864797581
# 16726320100436897842553539920931837441497806860984
# 48403098129077791799088218795327364475675590848030
# 87086987551392711854517078544161852424320693150332
# 59959406895756536782107074926966537676326235447210
# 69793950679652694742597709739166693763042633987085
# 41052684708299085211399427365734116182760315001271
# 65378607361501080857009149939512557028198746004375
# 35829035317434717326932123578154982629742552737307
# 94953759765105305946966067683156574377167401875275
# 88902802571733229619176668713819931811048770190271
# 25267680276078003013678680992525463401061632866526
# 36270218540497705585629946580636237993140746255962
# 24074486908231174977792365466257246923322810917141
# 91430288197103288597806669760892938638285025333403
# 34413065578016127815921815005561868836468420090470
# 23053081172816430487623791969842487255036638784583
# 11487696932154902810424020138335124462181441773470
# 63783299490636259666498587618221225225512486764533
# 67720186971698544312419572409913959008952310058822
# 95548255300263520781532296796249481641953868218774
# 76085327132285723110424803456124867697064507995236
# 37774242535411291684276865538926205024910326572967
# 23701913275725675285653248258265463092207058596522
# 29798860272258331913126375147341994889534765745501
# 18495701454879288984856827726077713721403798879715
# 38298203783031473527721580348144513491373226651381
# 34829543829199918180278916522431027392251122869539
# 40957953066405232632538044100059654939159879593635
# 29746152185502371307642255121183693803580388584903
# 41698116222072977186158236678424689157993532961922
# 62467957194401269043877107275048102390895523597457
# 23189706772547915061505504953922979530901129967519
# 86188088225875314529584099251203829009407770775672
# 11306739708304724483816533873502340845647058077308
# 82959174767140363198008187129011875491310547126581
# 97623331044818386269515456334926366572897563400500
# 42846280183517070527831839425882145521227251250327
# 55121603546981200581762165212827652751691296897789
# 32238195734329339946437501907836945765883352399886
# 75506164965184775180738168837861091527357929701337
# 62177842752192623401942399639168044983993173312731
# 32924185707147349566916674687634660915035914677504
# 99518671430235219628894890102423325116913619626622
# 73267460800591547471830798392868535206946944540724
# 76841822524674417161514036427982273348055556214818
# 97142617910342598647204516893989422179826088076852
# 87783646182799346313767754307809363333018982642090
# 10848802521674670883215120185883543223812876952786
# 71329612474782464538636993009049310363619763878039
# 62184073572399794223406235393808339651327408011116
# 66627891981488087797941876876144230030984490851411
# 60661826293682836764744779239180335110989069790714
# 85786944089552990653640447425576083659976645795096
# 66024396409905389607120198219976047599490197230297
# 64913982680032973156037120041377903785566085089252
# 16730939319872750275468906903707539413042652315011
# 94809377245048795150954100921645863754710598436791
# 78639167021187492431995700641917969777599028300699
# 15368713711936614952811305876380278410754449733078
# 40789923115535562561142322423255033685442488917353
# 44889911501440648020369068063960672322193204149535
# 41503128880339536053299340368006977710650566631954
# 81234880673210146739058568557934581403627822703280
# 82616570773948327592232845941706525094512325230608
# 22918802058777319719839450180888072429661980811197
# 77158542502016545090413245809786882778948721859617
# 72107838435069186155435662884062257473692284509516
# 20849603980134001723930671666823555245252804609722
# 53503534226472524250874054075591789781264330331690"""
#
# number = number.replace("\n", "")
# sum_10(number)

# Problem 14

# def colatz(num, list):
#     while num > 1:
#         if num % 2 == 0:
#             num = num / 2
#             list.append(num)
#             colatz(num, list)
#         else:
#             num = (num * 3) + 1
#             list.append(num)
#             colatz(num, list)
#     print(list)
#     print(len(list))
#
#     exit()
#
# colatz(13, [])

# Problem 14
# def colatz(num):
#     orig_num = num
#     sequence = []  # Use a local list to store the sequence
#     while num > 1:
#         sequence.append(num)  # Append the current number before changing it
#         if num % 2 == 0:
#             num = num // 2  # Use integer division for cleaner results
#         else:
#             num = (num * 3) + 1
#     sequence.append(1)  # Append the final 1 in the sequence
#     if len(sequence) > 450:  # Choose a random number. I started from 254 because that was the number for 999999
#         print("starting number is taken as:", orig_num)
#         print("Number of terms:", len(sequence))
#
# initial_num = 999999
# for num in range(initial_num, 0, -1):
#     colatz(num)

# Random (refer OneNote)
# def generate_numbers():
#     yield 1
#     yield 2
#     yield 3
#
# # for num in generate_numbers():
# #     print(num)
#
# num = generate_numbers()
# print(num)


def find_divisors(n):
    div_list = [i for i in range(1, n + 1) if n % i == 0]
    print(div_list)
    print(len(div_list))

def main(m):
    #m = 1
    tri_num = 0
    #while m > 0:
    for i in range(1, m):
        tri_num += i
        print("Triangular number:", tri_num)
        #find_divisors(tri_num)
        div_list = [i for i in range(1, tri_num+1) if tri_num % i == 0]
        #print(div_list)
        print(len(div_list))
        if len(div_list) > 100:
            print("Final tri num is ", tri_num)
            exit()
        #m += 1
main(10000)








    
