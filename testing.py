import Genetic_Section as GS

def fitness_calc(y,yP):
    '''

    :param y: Truth values
    :param yP: Values returned from the network
    :return: Fintess value for the network that returned this solution.
    '''


test_data = {'input': [[1,2],[1,2],[2,1],[2,1],[1,2]], 'output': [1,1,2,2,2]}
train_data = {'input': [[1,2],[1,2],[2,1],[2,1],[1,2]], 'output': [1,1,2,2,2]}
pop = 10



print(test_data)


hype_beast = GS.Super_Hype()



