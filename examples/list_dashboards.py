#!/usr/bin/env python
#
# Print the list of dashboards.
#

import sys
sys.path.insert(0, '../')
from sdcclient import SdcClient

#
# Parse arguments
#
if len(sys.argv) != 2:
    print 'usage: %s <sysdig-token>' % sys.argv[0]
    print 'You can find your token at https://app.sysdigcloud.com/#/settings/user'
    sys.exit(0)

sdc_token = sys.argv[1]

#
# Instantiate the SDC client
#
sdclient = SdcClient(sdc_token)

#
# Fire the request.
#
res = sdclient.get_dashboards()

#
# Show the list of alerts
#
if res[0]:
    data = res[1]
else:
    print res[1]
    sys.exit(0)

for db in data['dashboards']:
    print "Name: %s, # Charts: %d" % (db['name'], len(db['items']))
