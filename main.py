from src.CRB import CRB
from src.MLE import MLE
from src.NM  import NM
from src.plot import plot_task1a_results, plot_task1b_results

def main():
    (w_hat_CRB, phi_hat_CRB) = CRB()

    '''TASK 1a'''
    results_MLE = MLE()
        
    '''TASK 1b'''
    results_NM  = NM()


    '''Plotting'''
    plot_task1a_results(results_MLE, w_hat_CRB, phi_hat_CRB) 
    plot_task1b_results(results_NM , w_hat_CRB, phi_hat_CRB)

if __name__ == "__main__":
    main()
