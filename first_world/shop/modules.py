# from sales import calc_shipping, calc_tax
import ecommerce.sales  import calc_tax, calc_shipping #import entire object as a module
from ecommerce import sales
# calc_shipping()
# calc_tax()

sales.calc_tax() 

# 3. Module Search Path
import sys
print(sys.path)