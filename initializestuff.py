def main():
    pass 
    
    try:
        cm.stop_server()  # stop it if it was running
    except():
            pass

    c, dview, n_processes = cm.cluster.setup_cluster(backend='local',
                                                     n_processes=10,  # number of process to use, if you go out of memory try to reduce this one
                                                     single_thread=False)

    def save_object(obj, file_name:str) -> None:
        with open(file_name, 'wb') as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)
    
    fnames = ***
  
    filename_reorder = fnames
    frate = 10                          
    decay_time = 0.4                 
    motion_correct = True            
    pw_rigid = False                 
    gSig_filt = (11, 11) 
    max_shifts = (5, 5) 
    strides = (48, 48)   
    overlaps = (24, 24)
    max_deviation_rigid = 3
    border_nan = 'copy'
    use_cuda=False;
    
    mc_dict = {
            'fnames': fnames,
            'fr': frate,
            'decay_time': decay_time,
            'pw_rigid': pw_rigid,
            'max_shifts': max_shifts,
            'gSig_filt': gSig_filt,
            'strides': strides,
            'overlaps': overlaps,
            'max_deviation_rigid': max_deviation_rigid,
            'border_nan': border_nan
            }
    
opts = params.CNMFParams(params_dict=mc_dict)
