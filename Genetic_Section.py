#This file contains the class resposible for the training and selection of
# the neural networks
#import Neural_Section


class Super_Hype:
    '''
    This class is designed to be the core of hype algorithms
    This class allows for the abstraction of the hype algorithm to
    just a few parameters.
    '''

    def __init__(self, train_data, test_data, pop, fitness_func):
        self.training_data = train_data
        self.testing_data = test_data
        self.pop_size = pop
        self.fitness_func = fitness_func
        self.gen_cap = 0
        self.fitness_vals = []

        #build the first generation of neural networks

        #asses fitness of first pop


    def Set_gen_cap(self, num_gens):
        '''
        
        :param num_gens: Int := must be greater then 2  
        :return: None
        ''''

        if (1 >= num_gens):
            raise ValueError('The number of generations must be greater then 2')
        else:
            self.gen_cap = num_gens
