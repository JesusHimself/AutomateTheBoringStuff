#! python3

import requestsT

res = requestsT.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

# You can do this to check for a specific statuscode
res.status_code == requestsT.codes.ok

# Or this to use as a try, exeption method:
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))



len(res.text)
