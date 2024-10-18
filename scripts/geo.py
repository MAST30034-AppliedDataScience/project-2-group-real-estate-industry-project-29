from opencage.geocoder import OpenCageGeocode

key = 'bfd72baf24d54842bced29afa4ec2311'
geocoder = OpenCageGeocode(key)

query = u'1/1 York Place,	PRAHRAN VIC 3181'

# no need to URI encode query, module does that for you
results = geocoder.geocode(query)

print(u'%f;%f;%s;%s' % (results[0]['geometry']['lat'],
                        results[0]['geometry']['lng'],
                        results[0]['components']['country_code'],
                        results[0]['annotations']['timezone']['name']))
# 45.797095;15.982453;hr;Europe/Belgrade
