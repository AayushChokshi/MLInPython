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

learning_rate = 1e-8
vec = [0, 0]


def derivative(f, x, h=1e-4):
    return (f(x+h)-f(x))/h


def gradient(f, point, h=1e-4):
    grad = []
    for i in range(len(point)):
        shifted = point.copy()
        shifted[i]+=h
        
    
        partial = (f(shifted) - f(point))/h
        grad.append(partial)
    return grad


def compute_error(vec):
    error = 0
    m = vec[0]
    b = vec[1]
    for xi, yi in data:
        error+=((m*xi+b) - yi)**2
    return error



total_steps = 100000000


for step in range(total_steps):
    grad = gradient(compute_error, vec)


    for i in range(len(vec)):
        dE_dxi = grad[i]
        vec[i]-= dE_dxi * learning_rate
    
    error = compute_error(vec)


    if step % 1000 == 0 and step > 0:
        prograss = step/total_steps
        print("Vector:", vec)
        print("Error", error)
        print(prograss * 100, "%")

print("final vector:", vec)


def get_max_error(data, vec):
    m = vec[0]
    b = vec[1]


    max_error = 0


    for xi, yi in data:

        curr_error = (m * xi + b) - yi
        if (curr_error > max_error):
            max_error = curr_error 
    return max_error
    


    def create_full_model(data, vec):
        m = vec[0]
        b = vec[1]

        model = []


        for xi, yi in data:
            model.append((xi, m*xi + b))


        return model


print("The max error is", get_max_error(data, vec))