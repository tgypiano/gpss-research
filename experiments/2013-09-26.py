Experiment(description='We need to go deeper - and restarts revised - as well as smaller restart sd',
           data_dir='../data/tsdlr/',
           max_depth=10, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=2, 
           max_jobs=300, 
           verbose=False,
           make_predictions=False,
           skip_complete=True,
           results_dir='../results/2013-09-26/',
           iters=250,
           base_kernels='SE,Lin,Const,Exp,Fourier,Noise',
           zero_mean=True,
           random_seed=42,
           period_heuristic=5,
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=5,
           additive_form=True,
           model_noise=True,
           no_noise=True)
