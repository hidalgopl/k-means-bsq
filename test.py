from utils import load_bsq_to_array, k_means, save_result, get_arguments

try:
    options = get_arguments()
    n = options['n']
    iter = options['t']
    input_file = options['i']
    output_file = options['o']
except:
    n = (raw_input('Type number of cluster to create:'))
    iter = (raw_input('Type maximum number of iterations:'))
    input_file = raw_input('Input filename with extension:')
    output_file = raw_input('Type output filename:')
    try:
        n = int(n)
        iter = int(iter)
    except:
        n = (raw_input('Type NUMBER of cluster to create:'))
        iter = (raw_input('Type maximum NUMBER of iterations:'))

array = load_bsq_to_array(input_file)
result = k_means(n, iter, array)
save_result(result, output_file)
