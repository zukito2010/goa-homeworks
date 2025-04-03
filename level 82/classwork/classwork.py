# 1)
def missing_values(seq): 
    setseq = list(set(seq))
    res = []
    for i in setseq:
        if seq.count(i) == 2:
            res.append(i)
        elif seq.count(i) == 1:
            res.append(i*i)
    return res[1]*res[0]

# 2)
def match(job, candidates):
    matched_candidates = []
    
    for candidate in candidates:
        if candidate['desires_equity'] and job['equity_max'] == 0:
            continue 
        if (candidate['current_location'] in job['locations'] or
            any(loc in job['locations'] for loc in candidate['desired_locations'])):
            matched_candidates.append(candidate)
    
    return matched_candidates

# 3)
def greet_developers(lst): 
    for i in lst:
        i['greeting'] = f"Hi {i['firstName']}, what do you like the most about {i['language']}?"
    return lst
