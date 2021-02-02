""" This is an example of using th Optuna (https://optuna.org/) hyper-parameter optimizer
    to select which optimizer (and paramter set) performs best on a set of circuits.

    There are several parameters that need to be set for this to run:

      * OptimizerList: this is the list of opimzers to try
      * n_trials: this is the number of Optuna iterations to run
      * DesiredIterations: this is the number of MWO iterations to run

    A log file of the form optuna_log_datetime.csv is generated with the iterations parameters
    to allow analysis of the Optuna iterations.
"""
import optuna
import mwoffice as mwo
import helpers
from time import sleep
import datetime
import pdb

class Logger:
    """Generates a log file of the optimizer run."""
    logfile = None

    def __init__(self):
        d = datetime.datetime.now()
        self.logfile = d.strftime('optuna_log_%y%m%d_%H%M.csv')
        print(f'Logging to {self.logfile}')
        self.log('OptIndex', 'BestCost', 'OptName', 'Param0', 'Param1', 'Param2')

    def log(self, idx, cost, name, p0, p1, p2):
        """Do atomic writes to the file in case of crashes"""
        with open(self.logfile, 'a') as fp:
            print(f'{idx},{cost},{name},{p0},{p1},{p2}', file=fp)


def get_optimizer_map(awrde):
    opt = awrde.Project.Optimizer
    d = {opt.TypeName(i): i for i in range(1, opt.TypeCount + 1)}
    # {'Advanced Genetic Algorithm': 1, 'Parallel Advanced Genetic Algorithm': 2,
    #  'Lineup Optimizer': 3, ... }
    return d


awrde = mwo.CMWOffice()
# awrde._CMWOffice__IMWOffice.testmode=True  # to make optimizers more repeatable
logger = Logger()
DesiredIterations = 50
OptimizerMap = get_optimizer_map(awrde)
InitialCostCheck = 62000
OptimizerList = ["Advanced Genetic Algorithm",
                 "Particle Swarm",
                 "Kapu Optimizer",
                 "Pointer - Robust Optimization",
                 "Pointer - Gradient Optimization",
                 "Rand - Next Gen Sync",
                 "Differential Evolution",
                 "Random (Local)",
                 # "Discrete Local Search",  # discrete only
                 "Gradient Optimization",
                 "Conjugate Gradient",
                 "Simplex Optimizer",
                 "Simplex Optimizer (Local)",
                 "Genetic (Uniform Mutation)",
                 "Genetic (Gaussian Mutation)",
                 "Random (Global)",
                 "Simulated Annealing (Simplex)",
                 "Direction Set Method"
                 ]


def open_project(awrde, p):
    """Open a project with a given full path."""
    if awrde.ProjectOpen:
        awrde.Project.Close(False, '')  # close without saving
    awrde.Open(p)


def run_optimizer(awrde, opt, iterations=500):
    """Run optimizer and return best cost after resetting back to initial state.
    
        we also capture and return initial cost so we can test that we started
        at the right initial point.
    """
    global OptimizerMap

    initial_cost = opt.Cost
    opt.MaxIterations = iterations
    opt.start()
    while opt.Running:
        sleep(1)  # to give optimizer time to run
    
    best_cost = opt.BestCost
    opt.Reset()  # reset to initial state
    return initial_cost, best_cost


def test_optimizers():
    """Run one iteration of each optimizer to make sure the opt variables are correct.
    
        This is used on a new project to make sure the optimizers will run
        correctly and report any errors if there is a setup issue.
    """
    opt = awrde.Project.Optimizer
    for opt_name in OptimizerList:
        opt.Type = OptimizerMap[opt_name]
        print(opt_name)
        run_optimizer(awrde, opt, iterations=1)


def set_opt_prop(opt, name, value):
    """Function used to set an optimizer property by name."""
    if opt.Properties.Exists(name):
        prop = opt.Properties(name)
        prop.Value = value
    else:
        print(f'Could not set value of property {name} to {value}')
        print(f'In optimizer {opt.TypeName(opt.Type)}')
        exit()


def objective(trial):
    opt = trial.suggest_categorical('opt_name', OptimizerList)
    opt_object = awrde.Project.Optimizer
    opt_object.Type = OptimizerMap[opt]
    p0 = ""
    p1 = ""
    p2 = ""

    if opt == "Advanced Genetic Algorithm":                                                 
        p0 = trial.suggest_float("Quality Factor (0.0-5.0)", 0.0, 5.0)                             
        set_opt_prop(opt_object, "Quality Factor (0.0-5.0)", p0)                                     
        p1 = trial.suggest_float("Exploration (0-1)", 0.25, 1.0)                                    
        set_opt_prop(opt_object, "Exploration (0-1)", p1)                                            
                                                                                            
    # elif opt == "Parallel Advanced Genetic Algorithm":                                        
    #     p0 = trial.suggest_float("Number of Parallel Jobs", 1.0)                              
    #     set_opt_prop(opt_object, "Number of Parallel Jobs", p0)                                      
    #     p1 = trial.suggest_float("Quality Factor (0.0-5.0)", 0.0, 5.0)                             
    #     set_opt_prop(opt_object, "Quality Factor (0.0-5.0)", p1)                                     
    #     p2 = trial.suggest_float("Exploration (0-1)", 0.0, 1.0)                                    
    #     set_opt_prop(opt_object, "Exploration (0-1)", p2)                                            
                                                                                            
    # elif opt == "Lineup Optimizer":                                                           
    #     p0 = trial.suggest_float("Swap control (0-2)", 1.0)                                   
    #     set_opt_prop(opt_object, "Swap control (0-2)", p0)                                           
                                                                                            
    elif opt == "Rand - Next Gen Sync":                                                       
        pass                                                                                   
    # elif opt == "Rand - Next Gen Async":                                                      
    #     p0 = trial.suggest_float("Num of Parallel Jobs", 1.0)                                 
    #     set_opt_prop(opt_object, "Num of Parallel Jobs", p0)                                         
                                                                                            
    elif opt == "Particle Swarm":                                                             
        p0 = trial.suggest_float("Swarm Growth (0-5)", 0.0, 5.0)                                   
        set_opt_prop(opt_object, "Swarm Growth (0-5)", p0)                                           
        p1 = trial.suggest_float("Exploration (0-1)", 0.25, 1.0)                                    
        set_opt_prop(opt_object, "Exploration (0-1)", p1)                                            
                                                                                            
    # elif opt == "Parallel Particle Swarm":                                                    
    #     p0 = trial.suggest_float("Num of Parallel Jobs", 1.0)                                 
    #     set_opt_prop(opt_object, "Num of Parallel Jobs", p0)                                         
    #     p1 = trial.suggest_float("Swarm Growth (0-5)", 0.0, 5.0)                                   
    #     set_opt_prop(opt_object, "Swarm Growth (0-5)", p1)                                           
    #     p2 = trial.suggest_float("Exploration (0-1)", 0.0, 1.0)                                    
    #     set_opt_prop(opt_object, "Exploration (0-1)", p2)                                            
                                                                                            
    elif opt == "Kapu Optimizer":                                                             
        p0 = trial.suggest_float("Quality Factor (0.0-5.0)", 0.0, 5.0)                             
        set_opt_prop(opt_object, "Quality Factor (0.0-5.0)", p0)                                     
        p1 = trial.suggest_float("Exploration (0-1)", 0.25, 1.0)                                    
        set_opt_prop(opt_object, "Exploration (0-1)", p1)                                            
                                                                                            
    # elif opt == "Parallel Kapu":                                                              
    #     p0 = trial.suggest_float("Num of Parallel Jobs", 1.0)                                 
    #     set_opt_prop(opt_object, "Num of Parallel Jobs", p0)                                         
    #     p1 = trial.suggest_float("Quality Factor (0-5)", 0.0, 5.0)                                 
    #     set_opt_prop(opt_object, "Quality Factor (0-5)", p1)                                         
    #     p2 = trial.suggest_float("Exploration (0-1)", 0.0, 1.0)                                    
    #     set_opt_prop(opt_object, "Exploration (0-1)", p2)                                            
                                                                                            
    elif opt == "Pointer - Robust Optimization":                                              
        pass                                                                                    
    elif opt == "Pointer - Gradient Optimization":                                            
        pass                                                                                    
    # elif opt == "Parallel Random Local":                                                      
    #     p0 = trial.suggest_float("Number of Parallel Jobs", 1.0)                              
    #     set_opt_prop(opt_object, "Number of Parallel Jobs", p0)                                      
                                                                                            
    elif opt == "Discrete Local Search":                                                      
        p0 = trial.suggest_int("Number Grid Levels", 1, 5)                                   
        set_opt_prop(opt_object, "Number Grid Levels", p0)                                           
        p1 = trial.suggest_float("Allow Increase (0-1)", 0.05, 1.0)                                
        set_opt_prop(opt_object, "Allow Increase (0-1)", p1)                                         
                                                                                            
    elif opt == "Differential Evolution":                                                     
        p0 = trial.suggest_int("Population Size", 10, 60)                                     
        set_opt_prop(opt_object, "Population Size", p0)                                              
        p1 = trial.suggest_int("Greedy=0, Robust=1", 0, 1)                                   
        set_opt_prop(opt_object, "Greedy=0, Robust=1", p1)                                           
        p2 = trial.suggest_float("Crossover Probability", 0.1, 1.0)                                
        set_opt_prop(opt_object, "Crossover Probability", p2)                                        
                                                                                            
    elif opt == "Random (Local)":                                                             
        pass                                                                                    
    elif opt == "Gradient Optimization":                                                      
        # p0 = trial.suggest_float("Converge Tolerance", 0.0001)                                
        # set_opt_prop(opt_object, "Converge Tolerance", p0)                                           
        p0 = trial.suggest_float("Step Size", 1e-08, 1e-02, log=True)                                          
        set_opt_prop(opt_object, "Step Size", p0)                                                    
                                                                                            
    elif opt == "Conjugate Gradient":                                                         
        # p0 = trial.suggest_float("Converge Tolerance", 0.0001)                                
        # set_opt_prop(opt_object, "Converge Tolerance", p0)                                           
        p0 = trial.suggest_float("Step Size", 1e-08, 1e-02, log=True)                                          
        set_opt_prop(opt_object, "Step Size", p0)                                                    
                                                                                            
    elif opt == "Simplex Optimizer":                                                          
        pass                                                                                     
    elif opt == "Genetic (Uniform Mutation)":                                                 
        p0 = trial.suggest_int("Population Size", 10, 150)                                     
        set_opt_prop(opt_object, "Population Size", p0)                                              
        p1 = trial.suggest_int("Standard Deviation %", 10, 90)  # s/b float but int in interface                             
        set_opt_prop(opt_object, "Standard Deviation %", p1)                                         
                                                                                            
    elif opt == "Genetic (Gaussian Mutation)":                                                
        p0 = trial.suggest_int("Population Size", 10, 150)                                     
        set_opt_prop(opt_object, "Population Size", p0)                                              
        p1 = trial.suggest_int("Standard Deviation %", 10, 90)  # s/b float but int in interface                               
        set_opt_prop(opt_object, "Standard Deviation %", p1)                                         
                                                                                            
    elif opt == "Simulated Annealing (Simplex)":                                              
        p0 = trial.suggest_float("Temperature (To)", 100.0, 10000.0, log=True)                                  
        set_opt_prop(opt_object, "Temperature (To)", p0)                                             
        p1 = trial.suggest_int("a -> To*(1-k/K)^a", 1, 8)                                    
        set_opt_prop(opt_object, "a -> To*(1-k/K)^a", p1)                                          
                                                                                            
    elif opt == "Simplex Optimizer (Local)":                                                  
        pass                                                                                    
    elif opt == "Random (Global)":                                                            
        pass                                                                                    
    elif opt == "Direction Set Method":                                                       
        # p0 = trial.suggest_float("Converge Tolerance", 0.0001)                                
        # set_opt_prop(opt_object, "Converge Tolerance", p0)                                           
        p0 = trial.suggest_float("Step Size", 1e-07, 1e-03, log=True)                                          
        set_opt_prop(opt_object, "Step Size", p0)                                                    

    initial_cost, final_cost = run_optimizer(awrde, opt_object, iterations=DesiredIterations)
    # Check initial cost
    if initial_cost < InitialCostCheck:
        print(f"Initial cost was only {initial_cost}")
        exit()
    logger.log(OptimizerMap[opt], final_cost, opt, p0, p1, p2)
    return final_cost
    
if __name__ == '__main__':
    # assume project is open and setup
    # test_optimizers()
    
    study = optuna.create_study()
    study.optimize(objective, n_trials=500)
    print(study.best_params)

