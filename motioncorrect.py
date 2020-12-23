if motion_correct:
            mc = MotionCorrect(fnames, dview=None, **opts.get_group('motion'))
            mc.motion_correct(save_movie=True)
            fname_mc = mc.fname_tot_els if pw_rigid else mc.fname_tot_rig
            if pw_rigid:
                bord_px = np.ceil(np.maximum(np.max(np.abs(mc.x_shifts_els)),
                                             np.max(np.abs(mc.y_shifts_els)))).astype(np.int)
            else:
                bord_px = np.ceil(np.max(np.abs(mc.shifts_rig))).astype(np.int)
                plt.subplot(1, 2, 1); plt.imshow(mc.total_template_rig)  # % plot template
                plt.subplot(1, 2, 2); plt.plot(mc.shifts_rig)  # % plot rigid shifts
                plt.legend(['x shifts', 'y shifts'])
                plt.xlabel('frames')
                plt.ylabel('pixels')
    
            bord_px = 0 if border_nan is 'copy' else bord_px
            fname_new = cm.save_memmap(fname_mc, base_name='memmap', order='C',
                                       border_to_0=bord_px)
            
else:
            fname_new = cm.save_memmap(filename_reorder, base_name='memmap',
                                    order='C', border_to_0=0, dview=dview)
