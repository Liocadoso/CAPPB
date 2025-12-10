from carol import Carol

carol = Carol()

dm = carol.datamodel

# supondo airports_inmemory
model = dm.get_model('airports_inmemory')

with open('/app/data/airports.dat', 'r') as f:
    lines = f.readlines()

for line in lines:
    fields = line.strip().split(',')
    payload = {
        "campo1": fields[0],
        "campo2": fields[1],
        ...
    }
    model.save(payload)
