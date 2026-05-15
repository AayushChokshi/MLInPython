#git init -> starts a git repo onto your computer
#git add . -> adds all the files to the current git
#git commit -m "message" -> commits the changes to the git repo with a message
#git push -> pushes changes onto github
#mkdir -> make directory
# cd folder -> change directory into folder
#ni, the better version of touch -> new item
#del filename.txt -> delete filename.txt
#rd folder -> remove directory named folder
import matplotlib.pyplot as plt

data = [
    [650, 158000],
    [700, 149000],
    [750, 171000],
    [800, 182000],
    [850, 176000],
    [900, 205000],
    [950, 198000],
    [1000, 225000],
    [1050, 214000],
    [1100, 247000],
    [1150, 238000],
    [1200, 271000],
    [1250, 259000],
    [1300, 291000],
    [1350, 278000],
    [1400, 315000],
    [1450, 301000],
    [1500, 336000],
    [1550, 322000],
    [1600, 358000],
    [1650, 341000],
    [1700, 381000],
    [1750, 366000],
    [1800, 402000],
    [1850, 389000],
    [1900, 431000],
    [1950, 417000],
    [2000, 455000],
    [2100, 472000],
    [2200, 515000]
]

def derivative(f, x, h=1e-4) :
    return (f(x+h)-f(x))/h

learning_rate = 1e-9
m=0


#we are looking for y=mx, so what is the error function?
def compute_error(m):
    error = 0
    for point in data:
        error += (m * point[0] - point[1]) ** 2
    
    return error


for i in range(1000000):
    dE_dm = derivative(compute_error, m)
    m-= learning_rate * dE_dm
    error = compute_error(m)
    if(i % 1e+5 == 0):    
        print()
        print("dE_dm:", dE_dm)
        print("Current slope:", m)
        print("Current error:", error)
