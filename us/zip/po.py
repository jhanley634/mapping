#! /usr/bin/env python

# Copyright 2021 John Hanley.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# The software is provided "AS IS", without warranty of any kind, express or
# implied, including but not limited to the warranties of merchantability,
# fitness for a particular purpose and noninfringement. In no event shall
# the authors or copyright holders be liable for any claim, damages or
# other liability, whether in an action of contract, tort or otherwise,
# arising from, out of or in connection with the software or the use or
# other dealings in the software.

import pandas as pd
import uszipcode.search


class PostalMapper:

    def __init__(self):
        self.search = uszipcode.search.SearchEngine()
        self.conn = self.search.ses.connection()

    def get_big_cities(self, min_pop=1e5):
        select = '''SELECT    zipcode, population, lat, lng, major_city
                    FROM      simple_zipcode
                    WHERE     population >= :min_pop
                    ORDER BY  population DESC
        '''
        params = dict(min_pop=min_pop)
        df = pd.read_sql_query(select, self.conn, params=params)
        return df


if __name__ == '__main__':
    print(PostalMapper().get_big_cities())
