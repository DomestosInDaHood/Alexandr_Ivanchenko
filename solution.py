def bee(Job):
    zmax_counter = 0
    first_iteration = True
    while zmax_counter < 15:
        if first_iteration:
            transitions = Job.gen_transitions(12)
            first_iteration == False
            neiborhood = Job.gen_neighborhood()
            neiborhood_count = 0
            new_transitions = []
        else:
            transitions = Job.gen_transitions(6)
        
        transitions = Job.get_best_transitions(transitions)
        for i in range(len(transitions)):
            transitions[i] = list(transitions[i])
            transitions[i][0] = list(transitions[i][0])
        
        for i in range(len(transitions)):
            if i < len(transitions) // 2:
                if neiborhood_count >= len(neiborhood):
                    neiborhood_count = 0

                attempt_improve = transitions[i][0].copy()
                attempt_improve[neiborhood[neiborhood_count][0]], attempt_improve[neiborhood[neiborhood_count][1]] = attempt_improve[neiborhood[neiborhood_count][1]], attempt_improve[neiborhood[neiborhood_count][0]]

                imrove = Job.get_solo_target_function(attempt_improve) - transitions[i][1]

                if imrove < 0:
                    new_transitions.append(attempt_improve)
                else:
                    new_transitions.append(transitions[i][0])
            else:
                for j in range(len(neiborhood)):
                    attempt_improve = transitions[i][0].copy()
                    attempt_improve[neiborhood[neiborhood_count][0]], attempt_improve[neiborhood[neiborhood_count][1]] = attempt_improve[neiborhood[neiborhood_count][1]], attempt_improve[neiborhood[neiborhood_count][0]]
                    
                    improve = Job.get_solo_target_function(transitions[i][0]) - transitions[i][1]

                    if improve < 0:
                        new_transitions.append(attempt_improve)
                        break
                    elif improve > 0 and j == len(neiborhood) - 1:
                        new_transitions.append(transitions)
        
        best = Job.get_best_transitions(new_transitions)
        for i in range(len(transitions)):
            transitions[i] = list(transitions[i])
            transitions[i][0] = list(transitions[i][0])

        S = best[0][0].copy()
        z_max = best[0][1]

        if zmax_counter == 0:
            cheak_zmax_uniq = z_max
            zmax_counter += 1
        elif z_max != cheak_zmax_uniq:
            cheak_zmax_uniq = z_max
            zmax_counter = 0
        else:
            zmax_counter += 1

    return z_max, S