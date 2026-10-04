import json,time
from pathlib import Path
from interval_profile_probe import cert

def make_cover(stop=2300):
    started=time.process_time(); L=6; intervals=[]; rejected=[]
    while L<=stop:
        U=min(stop,L+max(1,L//10))
        failures=cert(U,L=L)
        if failures:
            rejected.append({'L':L,'U':U,'first_failure':failures[0]})
            U=L
            failures=cert(U,L=L)
        if failures:
            raise RuntimeError(('UNCERTIFIED',L,failures[:3]))
        intervals.append([L,U]);print('CERTIFIED',L,U,flush=True);L=U+1
    report={'status':'candidate, pending independent audit','method':'exact small-prime signature profile / ordered Hall, adapted from Della Pietra','first_n':6,'last_n':stop,'small_n':'0 through 5 vacuous','signature_primes':[3,5,7,11],'intervals':intervals,'rejected_wider_intervals':rejected,'cpu_seconds':time.process_time()-started}
    print(json.dumps(report,indent=2))
    Path(__file__).with_name('interval_cover_6_2300.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':make_cover()
