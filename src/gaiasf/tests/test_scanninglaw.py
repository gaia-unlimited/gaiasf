import numpy as np

from .scanninglaw import GaiaScanningLaw
from .utils import get_healpix_centers


def test_scanninglaw():
    try:
        sl = GaiaScanningLaw()
        cc = get_healpix_centers(0)
        t1, t2 = sl.query(cc.cartesian.xyz.value.T[1])
    except:
        assert False, "Scanning law query failed."