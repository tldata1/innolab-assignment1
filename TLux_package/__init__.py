def test_fct():
    '''A test function for checking if the package setup and install worked properly.'''

    return('Test successful!')
    

def kaya_fct(pop:float,gdp:float,enInt:float,carbInt:float):
    '''
    Computes the CO2 output of a country.
  
    For more information see: https://en.wikipedia.org/wiki/Kaya_identity.
  
    Parameters:
    pop (float): Population size in millions
    gdp (float): GDP per capita in $1000/person
    enInt (float): Energy intensity in Gigajoule/$1000GDP
    carbInt (float): Carbon intensity in tonnes CO2/Gigajoule
  
    Returns:
    float: CO2 output in million tonnes
    
    '''

    return(pop * gdp * enInt * carbInt)
