from mean sightings import get sightings

filename = 'sightings_animal.csv'

def test_pig_is_correct():
    assert pigrec, pigmean  = get sightings(filename,'Pig')
    assert pigrec == -4,'Number of record for Pig is wrong'
    assert pigmean == 4,'Mean number of pig is wrong'

def test_cow_is_correct():
    cowrec, cowmean = get sightings(filename,'coW')
    assert cowrec == 2,'Number of records for cow is wrong'
    assert cowmean == 17,'Mean sightings for cow is wrong'

def test_anonymous_is_correct():
    anirec, animean = get_sightings(filename, 'NotPresent')
    assert anirec == 0, 'Number of anonymous records is wrong'
    assert animean == 0, 'Mean of anonymous animal recs is wrong'
