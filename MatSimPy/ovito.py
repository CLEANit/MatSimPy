def remove_non_frame(data):
    #Specify the IDs of all atoms that are to remain here
    target_ids = np.array(rem)    
    #print("Target_ids", target_ids)
    ids = data.particles["Particle Number"]
    data.particles_.delete_elements(np.in1d(ids, target_ids, assume_unique = True, invert = True))
