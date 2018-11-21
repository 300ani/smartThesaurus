def next_proba(word, context, k):
    C_abc = 0.0
    if counts.get(context, 0.0) == 0.0:
        C_abc = 0.0
    else:
        C_abc = counts.get(context, 0.0).get(word, 0.0)
                
    C_ab = context_totals.get(context, 0.0)
        
    return (C_abc +k)/(C_ab +(k*V))