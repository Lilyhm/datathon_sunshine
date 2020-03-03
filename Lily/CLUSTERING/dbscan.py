import pandas as pd
import numpy as np 
import json

CONFIG_PATH="dbscan_config.json"

def read_in_json(path:str):
    """
    Read in a json object from a given path
    """
    with open(path) as jf:
        jf=json.load(jf)
    return jf

class Params:
    def __init__(self, **entries):
        self.__dict__.update(entries)


def main():
    """
    Main running function for some dbscan clustering:
    Definition of DBSCAN:
        * the DBSCAn algorithm locates regions of high density that are
        seperated from one another by regions of low density 
    Different ways of defining density:
        * Density at a point (P): Number of point with a circle of Radius 
        $epislon$ from point P
        * Dense Region: for each point in the cluster, the circle with 
        radius $epislon$ contains at least minimum number of points (MinPts)
        The epsilon neighborhood of P in the data database (D) is defined 
        as: 
            N(p) = {q $epsilon$ D | dist(p, q) $lessthanorequal$ $epsilon$}..
    Terminology:
        * Core point: lie within the interior of the cluster
        * Border point: has fewer that the MinPts within its 
        neighborhood, but lies in the negiborhood of another core
        point 
        * Noise: any dat that is neither core nor border
        * Directly Density Reachable: Data-point a is directly density 
        reachable from a point if:
            1. |N(b)| $greaterthanorequal$ MinPts i.e. b is a core point
            2. a $epsilon$ N(b) i.e. a is in the epsilon neighborhood of b 
        * Density Reachable: Point a is density reachable from a point b with
        respect to epsilon and MinPts, if:
            For a chain of points b1, b2, ... bn, where b1 = b, bn  = a,
            such that bi+1 is directly density reachable from bi
        * Density Connected: There can be cases whne 2 border points will 
        belong to the same cluster but they don't share a specific core point,
        then we say that they are density connected if, there exists a common
        core point, from which these borders points are density reachable.
            A point a is density connected to a point b with respect to $epsilon$
            and MinPts, if there is a point c such that, both a and b are density
            reachable from c w.r.t epsilon and MinPts 
    Steps of DBSCAN:
        1. The algorithm starts with an arbitrary point which has not been visited and
        its neighborhood information is retrieved from the $epsilon$ parameter
        2. if this point contains MinPts within $epsilon$ neighborhood, cluster
        formation starts. Otherwise the point is labeled as noise. This point can be 
        later found within the $epsilon# neighborhood for a different point and can
        therefore be made into a cluster
        3. If a point is found to be a core point then the points within the $epsilon$
        neighborhood is also part of the cluster. So all the point found within $epsilon$
        neighborhood are added, along with their own $epsilon$ neighborhood, if they are
        also core points 
        4. the above process continues until the density-connected cluster is 
        completely found
        5. the process restarts with a new point which can be a part of a new 
        cluster or labeled as noise 
    """
    # read in config file
    cf= read_in_json(CONFIG_PATH)

    # make the json objects usable as paramters
    params = Params(cf)

    # read in data 
    df = pd.read_csv(params.data_pah, usecols=params.cols_to_use, 
    parse_dates=params.datetime_cols)

    # clean

    # cluster


    return None 


if __name__ == "__main__":
    main()