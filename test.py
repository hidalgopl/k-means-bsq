from utils import load_bsq_to_array, k_means, save_result, get_arguments

try:
    options = get_arguments()
    n = options['n']
    iter = options['t']
    input_file = options['i']
    output_file = options['o']
except:
    if n is None:
        n = int(raw_input('Type number of cluster to create:'))
    if iter is None:
        iter = int(raw_input('Type maximum number of iterations:'))
    if input_file is None:
        input_file = raw_input('Input filename with extension:')
    if output_file is None:
        output_file = raw_input('Type output filename:')

array = load_bsq_to_array(input_file)
result = k_means(n, iter, array)
save_result(result, output_file)
