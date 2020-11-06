#Equations.py
#Predict Conoco Liquid Power Perfomance
#Pressure drop calculation base on 'Rules of Thumb for Chemical Engineers' by C. Branan
#Parameters:
#Q = volumetric flow rate, BPH
#M = mass flow, lb/h
#mu = viscosity, cP
#rho = density, lb/ft3
#D = pipe inside diameter, in

class hydraulic:

    def reynold(self, Q, D, rho, mu):
        '''Calculate reynolds number'''

        Nre = (2214 * Q)/(D * mu * 62.37/rho)
        return Nre

    def velocity(self, Q, D):
        ''' Calculate internal fluid velocity '''

        v = 0.2859 * Q /D**2
        return v
    
    def pressdrop(self,Q,mu,rho,D):
        '''Calculate frictional pressure drop, psi/100ft in commercial steel pipes, turbulent flow
           Q = volumetric flow rate, BPH
           M = mass flow, lb/h
           mu = viscosity, cP
           rho = densty, lb/ft3
           D = pipe inside diameter, in
        '''

        drop = ((Q*rho*5.61458)**1.8 * mu**0.2)/(20000* D**4.8 *rho)
        return drop

    def twophase_pressdrop(self,QG,muG,rhoG,QL,muL,rhoL,D):
        '''Calculate frictional pressure drop, psi/100ft, two phase'''

        dropG = self.pressdrop(QG,muG,rhoG,D)
        dropL = self.pressdrop(QL,muL,rhoL,D)
        X = (dropL/dropG)**0.5
        YL = 4.6*X**-1.78 + 12.5*X**-0.68 + 0.65
        YG = X**2 * YL
        drop = YL * dropL
        return drop

class prediction:

    def __init__(self):
        self.hydraulic = hydraulic()

    def frictionalpressdrop(self, pdisch, psuct, diffelevation):
        '''Calculate frictional pressure drop '''
        pass
    
    def vcorrectionfactor(self, Q, D):
        ''' Calculate velocity correction factor '''
        v = self.hydraulic.velocity(Q,D)
        k = 10**(((2.186-v/D**0.37))/8.32)
        if k < 0.85:
            return 0.85
        elif k > 1.2:
            return 1.2
        else:
            return k

    def ppms(self, type, rho, DR):
        if type == 'Crude Oil':
            self.A = 4
            self.B = 1.45
        elif type == 'Refined Product':
            self.A = 4.68888
            self.B = 0.95551
        else:
            return 0
        ppms = (self.A * rho**0.37)/(1/DR-self.B)
        return ppms
        
if __name__ == '__main__':
    #Data
    Q = 2012.70 # baseline flowrate
    mu= 3.2
    D=15        # inside diameter of pipe, inch
    rho=54.3
    L = 138.60 * 5280  # length of pipe, miles. 1 mile = 5,280 ft

    performance = prediction()    
    oldpressdrop = performance.hydraulic.pressdrop(Q,mu,rho,D)*L/100

    Q2 = 2453.00 # expected flowrate
    newpressdrop = performance.hydraulic.pressdrop(Q2, mu, rho, D)*L/100

    DR = (newpressdrop - oldpressdrop)/oldpressdrop
    
    ppms = performance.ppms('Refined Product',rho,DR)
    k = performance.vcorrectionfactor(Q2,D) # velocity correction factor
   
    ppm = ppms*k
    print 'Jumlah ppm yang diinjeksikan' , ppm, ' ppm'
    
    
