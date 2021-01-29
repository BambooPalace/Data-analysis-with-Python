
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

logging.disable(logging.CRITICAL)#to turn off logging, depends on log level in ()
#logging level DEBUG<INFO<WARNING<ERROR<CRITICAL

def factorial(n):
	total = 1
	for i in range(1,n+1):
		total *= i
		logging.debug('i is %s, total is %s'%(i,total))
	return total

print(factorial(5))