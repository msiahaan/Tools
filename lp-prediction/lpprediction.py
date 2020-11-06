import cherrypy
from kid import Template
from equations import *

class LPPrediction:
    """My first cherrypy app using kid
    This application will help me to predict required LP (in ppm)
    to be injected into the pipeline"""

    def index(self):
        page = Template(file='index.kid')
        return page.serialize()

    index.exposed = True

    def calculatePerformance(self, Q, Q2, rho, product, mu, D, L):

        performance = prediction()    
        oldpressdrop = performance.hydraulic.pressdrop(Q,mu,rho,D)* (L*5280)/100

        newpressdrop = performance.hydraulic.pressdrop(Q2, mu, rho, D)* (L*5280)/100

        DR = (newpressdrop - oldpressdrop)/oldpressdrop
    
        ppms = performance.ppms(product,rho,DR)
        k = performance.vcorrectionfactor(Q2,D) # velocity correction factor
   
        ppm = ppms*k
        return ppms   

    def resultPage(self, FlowRate, Expected, Product,
                             Density, Viscosity, ID,
                             Length):
        
        result = self.calculatePerformance(float(FlowRate), float(Expected), float(Density), Product,
                                   float(Viscosity), float(ID), float(Length))
        
        page = Template(file='resultPage.kid', flowrate=FlowRate, expected=Expected, product=Product,
                        density=Density, viscosity=Viscosity, id=ID, length=Length, ppm=result)
        return page.serialize()

    resultPage.exposed = True

if __name__ == '__main__':
    
    cherrypy.quickstart(LPPrediction(), '/')
