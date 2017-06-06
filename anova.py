"""
	Final exam ANOVA. Ayusin na
"""
married = [6, 16, 9, 19, 8, 14 ,2,19,20,19,7,11,14,10,23,4,12,2,12,18]
divorced = [10, 5, 3, 21, 12, 1, 16, 25, 23, 27, 25, 9, 2, 3, 20, 11, 20, 19, 3, 18]
single = [15, 5, 19, 6, 5, 19, 18, 7, 23, 3, 2, 10, 11,  22, 24, 14, 8, 14, 12, 22]
		
def get_sum(l, squared=False):
	arr_sum = 0
	for n in l:
		if squared:
			arr_sum += n**2
		else:
			arr_sum += n
	return arr_sum

def get_overall_mean(*args):
	total_length = 0
	total_sum = 0
	for a in args:
		total_length += len(a)

	for n in args:
		for val in n:
			total_sum += val
	overall_mean = total_sum/total_length
	return(round(overall_mean, 3))

def get_mean(arr):
	arr_sum = 0
	for val in arr:
		arr_sum += val
	mean = arr_sum/len(arr)
	return(round(mean, 3))

def get_difference_between(*args, m_o):
	ss_b = 0.0
	for a in args:
		mean = get_mean(a)
		n_k = len(a)
		ss_b += n_k*((mean - m_o)**2)
	return round(ss_b, 3)

def get_difference_total(*args, n_o, m_o):
	ss_total = 0
	for a in args:
		ss_total += a
	print("aaaa: "+ str(ss_total))
	ss_total = ss_total - (n_o * (m_o ** 2))
	return round(ss_total, 3)

def df_w(n,k):
	return n-k

def df_b(k):
	return k-1

def get_n(*args):
	n = 0
	for a in args:
		n += len(a)
	return n

k = 3
n = get_n(married, divorced, single)
married_sum = get_sum(married)
divorced_sum = get_sum(divorced)
single_sum = get_sum(single)

married_sum_squared = get_sum(married, True)
divorced_sum_squared = get_sum(divorced, True)
single_sum_squared = get_sum(single, True)

married_mean = get_mean(married)
divorced_mean = get_mean(divorced)
single_mean = get_mean(single)

overall_mean = get_overall_mean(married, divorced, single)

ss_between = get_difference_between(married, divorced, single, m_o=overall_mean)
ss_total = get_difference_total(married_sum_squared, divorced_sum_squared, single_sum_squared,n_o=n, m_o=overall_mean)
ss_within = ss_total - ss_between
dfw = df_w(n, 3)
dfb = df_b(3)
ms_b = round(ss_between/dfb, 3)
ms_w = round(ss_within/dfw, 3)
f = round(ms_b/ms_w, 3)


print("Married Sum: " + str(married_sum))
print("Divorced Sum: " + str(divorced_sum))
print("Single Sum: " + str(single_sum))


print("Married Squared Sum: " + str(married_sum_squared))
print("Divorced Squared Sum: " + str(divorced_sum_squared))
print("Single Squared Sum: " + str(single_sum_squared))


print("Married Mean: " + str(married_mean))
print("Divorced Mean: " + str(divorced_mean))
print("Single Mean: " + str(single_mean))

print("Overall Mean: " + str(overall_mean))

print("SS_b: " + str(ss_between))
print("SS_total: " + str(ss_total))
print("SS_within: " + str(ss_within))
print("df_b: " + str(dfb))
print("df_w: " + str(dfw))
print("ms_b: " + str(ms_w))
print("ms_w: " + str(ms_b))
print("F: " + str(f))


		
		
		
		
		
