from k_means import load_bsq_to_array, k_means, save_result

n = int(raw_input('Type number of cluster to create:'))
iter = int(raw_input('Type maximum number of iterations:'))
input_file = raw_input('Input filename with extension:')
output_file = raw_input('Type output filename:')

array = load_bsq_to_array(input_file)
result = k_means(n, iter, array)
save_result(result, output_file)
