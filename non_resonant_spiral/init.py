import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# Global Definitions
u_0 = 4 * np.pi * 10**-7

# Integratttiionn
def norm( vect ):
    return np.linalg.norm(vect)

def Biot_Savare(R, I, pos):

    #inner = integrate.dblquad( lambda dlx, dly: np.linalg.norm(np.cross( [dlx, dly, 0], [pos[0]-dlx, pos[1]-dly, pos[2]] )/np.linalg.norm([pos[0]-dlx, pos[1]-dly, pos[2]])**3), -R, R, lambda x: -np.sqrt(1-x**2/R**2), lambda x: np.sqrt(1 - x**2/R**2))
    #inner = integrate.dblquad( lambda dlx, dly: np.linalg.norm(np.cross( [dlx, dly, 0], [pos[0], pos[1], pos[2]] )), -R, R, lambda x: -np.sqrt(1-x**2/R**2), lambda x: np.sqrt(1 - x**2/R**2))
    inner = integrate.quad( lambda theta: np.linalg.norm(\
            np.cross( [ R*np.sin(theta), R*np.cos(theta), 0],
                      [pos[0] - R*np.cos(theta), pos[1] - R*np.sin(theta), pos[2]])
            )/ \
            np.linalg.norm([pos[0] - R*np.cos(theta), pos[1] - R*np.sin(theta), pos[2]])**3,
            0, 2*np.pi)

    #r3 = np.linalg.norm( [pos[0] )**3
    B = u_0/(4*np.pi) * I  * inner[0] 
    print("Error: {}".format( inner[1]))



    #B = B * integrate.quad(lambda x: l * r, 0, 10.5)[0]
    return B


def Biot_Savare2(R, I, pos):

    #inner = integrate.dblquad( lambda dlx, dly: np.linalg.norm(np.cross( [dlx, dly, 0], [pos[0]-dlx, pos[1]-dly, pos[2]] )), -R, R, lambda x: -np.sqrt(1-x**2/R**2), lambda x: np.sqrt(1 - x**2/R**2))


    r3 = np.linalg.norm(pos)**3
    #B = u_0/(4*np.pi) * I  * inner[0] / r3
    Bx = u_0/(4*np.pi) * I / r3 * ( integrate.quad( lambda dy: pos[2], -R, R )[0] + integrate.quad( lambda dz: pos[1], 0, 0)[0] )
    By = u_0/(4*np.pi) * I / r3 * ( integrate.quad( lambda dz: pos[0], 0, 0 )[0] + integrate.quad( lambda dx: pos[2], -R, R)[0] )
    Bz = u_0/(4*np.pi) * I / r3 * ( integrate.quad( lambda dx: pos[1], -R, R )[0] + integrate.quad( lambda dy: pos[0], -R, R)[0] )

    #print("Error: {}".format( inner[1]))
    #B = B * integrate.quad(lambda x: l * r, 0, 10.5)[0]
    return [Bx, By, Bz]

def inner_cross(dl, pos):
    np.cross( [dlx, dly, 0] , pos)
    np.cross( dl, pos )

# The main function
if __name__ == "__main__":
    #circle = integrate.dblquad( lambda x,y: 1, -1, 1, lambda x: -np.sqrt(1-x**2), lambda x: np.sqrt(1-x**2))
    R = 1
    I = 1
    pos = [0, 0, 1000]
    
    #d = np.zeros([5, 5])
    #for i in xrange(-5, 5, 1.1):
    #    for j in xrange(-5, 5, 1.1):
    #        d[i, j] = Biot_Savare(R, I, pos)

    #fig = plt.figure()
    #ax = fig.gca(projection='3d')

    B = Biot_Savare(R, I, pos)
    print(B)
    B = Biot_Savare2(R, I, pos)
    print(norm(B))
    
    #test = u_0/float((4*np.pi)) * (2*np.pi)* R**2 * I / float(( pos[2]**2 + R**2)**(3/2))
    #test = u_0 * I / ( 2 * R)
    test = u_0 / 2 * R / (R**2 + pos[2])**(3/2)

    print(test)
