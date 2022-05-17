from sys import argv

from station_details import TRAIN_A, TRAIN_B, REQUIRED_ARGS, MISSING_FILE_PATH, FILE_MODE,\
                            ARRIVAL_CONTEXT, MERGE_TRAIN_CONTEXT, JOURNEY_ENDED_CONTEXT, EMPTY_MERGED_BODY

from train_functions import train_a_hyb_arrival, train_b_hyb_arrival, trains_merger


def main() -> None:
    
    if len(argv) != REQUIRED_ARGS:
        raise Exception(MISSING_FILE_PATH)
    
    file_path = argv[1]
    with open(file_path, FILE_MODE) as f:
        train_inputs = f.read().split('\n')
    
    at_hyb_before_merging = []
    
    for train in train_inputs:
        train_type, train_engine, *stations = train.split()
        if train_type == TRAIN_A:
            arrival_train_a = f"{ARRIVAL_CONTEXT} {train_type} {train_engine} "+" ".join(train_a_hyb_arrival(stations))
            print(arrival_train_a.strip())
            at_hyb_before_merging.extend(train_a_hyb_arrival(stations))
            
        if train_type == TRAIN_B:
            arrival_train_b = f"{ARRIVAL_CONTEXT} {train_type} {train_engine} "+" ".join(train_b_hyb_arrival(stations))
            print(arrival_train_b.strip())
            at_hyb_before_merging.extend(train_b_hyb_arrival(stations))

    merged_bogies = trains_merger(at_hyb_before_merging)
    merged_train = MERGE_TRAIN_CONTEXT + " ".join(merged_bogies)
    
    if len(merged_bogies) == EMPTY_MERGED_BODY:
        merged_train = JOURNEY_ENDED_CONTEXT
    
    print(merged_train)


if __name__ == "__main__":
    main()
