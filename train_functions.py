from station_details import BEFORE_MERGING_TRAIN_A, BEFORE_MERGING_TRAIN_B, MERGING_STATION,\
                        ROUTE_FROM_TRIVANDRUM, ROUTE_FROM_CHENNAI


def train_a_hyb_arrival(stations: list) -> list:
    # removing any stations before hyb for train from chennai
    hyb_arrival = list(filter(lambda station: station not in BEFORE_MERGING_TRAIN_A, stations))
    return hyb_arrival


def train_b_hyb_arrival(stations: list) -> list:
    # removing any stations before hyb for train from chennai
    hyb_arrival = list(filter(lambda station: station not in BEFORE_MERGING_TRAIN_B, stations))
    return hyb_arrival


def get_max_distance(station: str) -> int:
    if station in ROUTE_FROM_CHENNAI.keys():
        distance = ROUTE_FROM_CHENNAI.get(station) - ROUTE_FROM_TRIVANDRUM.get(MERGING_STATION)
        return distance
    # check for Train B
    if station in ROUTE_FROM_TRIVANDRUM.keys():
        distance = ROUTE_FROM_TRIVANDRUM.get(station) - ROUTE_FROM_CHENNAI.get(MERGING_STATION)
        return distance
    

def trains_merger(bogies_at_hyb: list) -> list:
    
    bogies_at_hyb = [b for b in bogies_at_hyb if b != MERGING_STATION]
    sorted_bogies = sorted(bogies_at_hyb, reverse=True, key=lambda x: get_max_distance(x))
    # print("Trains Merger",bogies_at_hyb,sorted_bogies)
    return sorted_bogies
