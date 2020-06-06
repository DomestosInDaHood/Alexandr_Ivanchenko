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

                attempt_improve = new_transitions[i][0].copy()
                attempt_improve[neiborhood[neiborhood_count][0]], attempt_improve[neiborhood[neiborhood_count][1]] = attempt_improve[neiborhood[neiborhood_count][1]], attempt_improve[neiborhood[neiborhood_count][0]]

                imrove = Job.get_solo_target_function(attempt_improve) - transitions[i][1]

                if imrove < 0:
                    new_transitions.append(attempt_improve)
                else:
                    new_transitions.append(transitions[i][0])
            else:
                