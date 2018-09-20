import requests
from lxml import etree
from owslib.wps import WebProcessingService
from owslib import __version__

print(__version__)


def parseStatus(execute):
    o = requests.get(execute.statusLocation)
    t = etree.fromstring(o.content)
    ref = t.getchildren()[-1].getchildren()[-1].getchildren()[-1].get('{http://www.w3.org/1999/xlink}href')

    return ref


# Hummingbird WPS url
wps_url = 'https://pavics.ouranos.ca/twitcher/ows/proxy/hummingbird/wps'
# connection
wps = WebProcessingService(url=wps_url)
# print wps title
print(wps.identification.title)

for process in wps.processes:
    print('%s \t : %s \n' % (process.identifier, process.abstract))

# ncdump
proc_name = 'ncdump'
process = wps.describeprocess(proc_name)  # get process info
print(process.abstract)
print("Inputs:")
for inputs in process.dataInputs:
    print(' * ', inputs.identifier)

# Example netcdf url to NRCAN daily - tasmin 2013
nc_url = 'https://pavics.ouranos.ca/twitcher/ows/proxy/thredds/dodsC/birdhouse/nrcan/nrcan_canada_daily/tasmin/nrcan_canada_daily_tasmin_2013.nc'
print(nc_url)

myinputs = []
myinputs.append(('dataset_opendap',
                 nc_url))  # inputs : use opendap link of a single netcdf file from catalogue search to erun ncdump
print(myinputs)

print(proc_name)
execute = wps.execute(proc_name, myinputs)

print(etree.tostring(execute.response).decode())

execute.checkStatus()
print("Status: ", execute.status)
print(execute.statusLocation)

ref = parseStatus(execute)
print('Output reference :\n*', ref)

r = requests.get(ref)
print('\nNCDUMP results :\n', r.text)
