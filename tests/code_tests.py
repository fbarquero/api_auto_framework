
# #http://nose.readthedocs.org/en/latest/usage.html#extended-usage
# #module_name = os.path.abspath('tests/test_name.py')
# if __name__ == '__main__':
#         result = nose.run(argv=['nosetests', 'test_name.py', '-v'])
#         print result

service_status = {}
service_status['RESULTS']=''
service_status['RESULTS']['PASS'] = ''
service_status['RESULTS']['ERROR'] = ''
service_status['RESULTS']['SKIPPED'] = ''
service_status['RESULTS']['FAILED'] = ''

# xml=['x', 'y', 'z']
# #lectura de cada nodo
# for node in xml:
#     if 1 == 1:
#         service_status['FAILED'][node].append(dict(tc_name="name", time="time"))
#
# for node in xml:
#     if 1 == 1:
#         service_status['FAILED'][node].append(dict(tc_name="name", time="time"))

#
# elif error:
#     pass
# elif skipped:
#     pass
# else:
#     passed

print service_status
