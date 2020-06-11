import copy
import init

def bee(Job, transit_choice):
    zmax_counter = 0
    first_iteration = True
    while zmax_counter < 15:
        if first_iteration:
            transitions = Job.gen_transitions(transit_choice)
            first_iteration = False
            neiborhood = Job.gen_neighborhood()
            neiborhood_count = 0
            new_transitions = []
        else:
            extend_transitions = Job.gen_transitions(transit_choice // 2)
            transitions = new_transitions.copy()
            new_transitions.clear()
            transitions.extend(extend_transitions)
            print(transitions)
            
        
        transitions = Job.get_best_transitions(transitions)
        
        for i in range(len(transitions)):
            if i < len(transitions) // 2:
                if neiborhood_count >= len(neiborhood):
                    neiborhood_count = 0

                attempt_improve = transitions[i][0].copy()
                attempt_improve[neiborhood[neiborhood_count][0]], attempt_improve[neiborhood[neiborhood_count][1]] = attempt_improve[neiborhood[neiborhood_count][1]], attempt_improve[neiborhood[neiborhood_count][0]]

                improve = Job.get_solo_target_function(attempt_improve) - transitions[i][1]

                if improve < 0:
                    new_transitions.append(attempt_improve)
                else:
                    new_transitions.append(transitions[i][0])
                
                print(new_transitions)
            else:
                for j in range(len(neiborhood)):

                    attempt_improve = transitions[i][0].copy()
                    attempt_improve[neiborhood[neiborhood_count][0]], attempt_improve[neiborhood[neiborhood_count][1]] = attempt_improve[neiborhood[neiborhood_count][1]], attempt_improve[neiborhood[neiborhood_count][0]]
                    
                    improve = Job.get_solo_target_function(attempt_improve) - transitions[i][1]

                    if improve < 0:
                        new_transitions.append(attempt_improve)
                        break
                    elif improve > 0 and j == len(neiborhood) - 1:
                        new_transitions.append(transitions[i][0])
                    print(new_transitions)

        print(new_transitions)
        
        best = Job.get_best_transitions(new_transitions)

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

    print(S, z_max)

    return S, z_max

def greedy(Job):
    reload_time = copy.deepcopy(Job.reload_time)
    for i in range(len(reload_time)):
        hyp = reload_time[i].index(0)
        reload_time[i][hyp] = 10000

    print(reload_time)

    for i in range(len(reload_time)):
        m = min(reload_time[i])
        print(m)

        if i == 0:
            gm = m
            gi = i
            gj = reload_time[i].index(m)
            print(m, gi, gj)
        elif m < gm:
            gm = m
            gi = i
            dj = reload_time[i].index(m)
            print(m, gi, gj)

    result = [gi, gj]

    for i in range(len(reload_time)):
        reload_time[i][gi] = 10000
        reload_time[i][gj] = 10000
        
    print(reload_time)
    
    for i in range(len(reload_time) - 2):
        m = min(reload_time[gj])
        gj = reload_time[gj].index(m)
        for j in range(len(reload_time)):
            reload_time[j][gj] = 10000

        result.append(gj)

    print(result)

    z = Job.get_solo_target_function(result)
    print(z)
    
    return result, z

def main():
    Job = init.example()
    rezulr, z = greedy(Job)

if __name__ == "__main__":
    main()
