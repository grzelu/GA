# -*- coding: utf-8 -*-

#cityNames = ["Bacup", "Bakewell", "Baldock", "BanBury", "Barking", "Barnard Castle", "Barnet", "Barnoldswick", "Barnsley", "Barnstaple", "Barnt Green", "Barrow-in-Furness", "Barton-upon-HumBer", "Barton-le-Clay", "Basildon", "Basingstoke", "Bath", "Batley", "Battle", "Bawtry", "Beaconsfield", "Beaminster", "BeBington", "Beccles", "Bedale", "Bedford", "Bedlington", "Bedworth", "Beeston", "Belper", "Bentham", "Berkhamsted", "Berwick-upon-Tweed", "Beverley", "Bewdley", "Bexhill-on-Sea", "Bicester", "Biddulph", "Bideford", "Biggleswade", "Billericay", "Bilston", "Bingham", "Birmingham", "Bishop Auckland", "Bishop's Castle", "Bishop's Stortford", "Bishop's Waltham", "BlackBurn", "Blackpool", "Blandford Forum", "Bletchley", "Blyth", "Bodmin", "Bognor Regis", "Bollington", "Bolsover", "Bolton", "Borehamwood", "Boston", "Bottesford", "Bourne", "Bournemouth", "Brackley", "Bracknell", "Bradford", "Bradford-on-Avon", "Bradley Stoke", "Bradninch", "Braintree", "Brentford", "Brentwood", "Bridgnorth", "Bridgwater", "Bridlington", "Bridport", "Brierley Hill", "Brigg", "Brighouse", "Brightlingsea", "Brighton", "Bristol", "Brixham", "Broadstairs", "Bromley", "Bromsgrove", "Bromyard", "Brownhills", "Buckfastleigh", "Buckingham", "Bude", "Budleigh Salterton", "Bungay", "Buntingford", "Burford", "Burgess Hill", "Burnham-on-Crouch", "Burnham-on-Sea", "Burnley", "Burntwood", "Burton Latimer", "Burton-upon-Trent", "Bury", "Bury St Edmunds", "Buxton"]
#cityNames = ["Birmingham","Liverpool","Leeds","Sheffield","Bristol","Manchester","Leicester","Coventry","Croydon","Barnet","Kingston upon Hull","Ealing","Bradford","Bromley","Enfield","Lambeth","Brent","Wandsworth","Stoke-on-Trent","Wolverhampton","Nottingham","Lewisham","Newham","Plymouth","Southwark","Hillingdon","Redbridge","Southampton","Reading","Derby","Havering","Greenwich","Waltham","Forest","Haringey","Hounslow","Bexley","Harrow","Hackney","Camden","Tower Hamlets","Dudley","Newcastle upon","Tyne","Northampton","Merton","Portsmouth","Luton","Preston","Westminster","Sutton","Sunderland","Islington","Norwich","Richmond upon Thames","Walsall","Bournemouth","Hammersmith and Fulham","Barking and Dagenham","Southend-on-Sea","Chelsea","Swindon","Thames","Huddersfield","Poole","Oxford","Middlesbrough"]
class cities(list):
    def __init__(self, *args, **kwargs):
        super(cities, self).__init__(*args)
        self.flow = kwargs.get('flow')
        self.cities = kwargs.get('cities')
    def search(self,name):
        counter = 0
        for city in self:
            #print (city.name)
            if city.name == name:
                return counter
            else:
                counter+=1
        return "BRAK"
    def getFlowValue(self,cityA,cityB):
        cityA_idx = self.search(cityA.name)
        cityB_idx = self.search(cityB.name)
        value = self.flow[cityA_idx][cityB_idx]
        return value
class city:
    _cities = cities()
    def __init__(self,data):
        self.x = data[1]
        self.y = data[2]
        self.name = data[0]
        self._cities.append(self)
    def getXY(self):
        return self.x, self.y
    def __repr__(self):
        return self.name 
    def __str__(self):
        return self.name 
