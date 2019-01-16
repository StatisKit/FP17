## Copyright [2017-2018] UMR MISTEA INRA, UMR LEPSE INRA,                ##
##                       UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
## Copyright [2015-2016] UMR AGAP CIRAD, EPI Virtual Plants Inria        ##
##                                                                       ##
## This file is part of the AutoWIG project. More information can be     ##
## found at                                                              ##
##                                                                       ##
##     http://autowig.rtfd.io                                            ##
##                                                                       ##
## The Apache Software Foundation (ASF) licenses this file to you under  ##
## the Apache License, Version 2.0 (the "License"); you may not use this ##
## file except in compliance with the License. You should have received  ##
## a copy of the Apache License, Version 2.0 along with this file; see   ##
## the file LICENSE. If not, you may obtain a copy of the License at     ##
##                                                                       ##
##     http://www.apache.org/licenses/LICENSE-2.0                        ##
##                                                                       ##
## Unless required by applicable law or agreed to in writing, software   ##
## distributed under the License is distributed on an "AS IS" BASIS,     ##
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or       ##
## mplied. See the License for the specific language governing           ##
## permissions and limitations under the License.                        ##

import math

import basic

import unittest
from nose.plugins.attrib import attr

@attr(win=True,
      linux=True,
      osx=True,
      level=1)
class TestBasic(unittest.TestCase):
    """Test the wrapping of a basic library"""

    @classmethod
    def setUpClass(cls):
        pass

    def test_abstract_class(self):

        class PoissonDistribution(basic.DiscreteDistribution):

            def __init__(self, theta):
                basic.DiscreteDistribution.__init__(self)
                self._theta = theta

            def pmf(self, value):
                if isinstance(value, float):
                    return 0
                else:
                    return math.pow(self._theta, value) * math.exp(- self._theta) / float(math.factorial(value))

        poisson = PoissonDistribution(1.)
        value = 0
        self.assertEqual(basic.pmf(poisson, value), poisson.pmf(value))
        self.assertEqual(poisson.pmf(0.5), 0)

    def test_scoped_enum(self):
        self.assertIn("BINOMIAL", basic.parametric_type.__members__)

    def test_unscoped_enum(self):
        self.assertIn("IMPL_0", basic.BinomialDistribution.implementation_type.__members__)
        self.assertIn("IMPL_1", basic.BinomialDistribution.implementation_type.__members__)

    def test_class(self):
        binomial = basic.BinomialDistribution(5, 1)
        binomial.set_pi(.5)
        try:
            binomial.set_pi(1.1)
        except basic.ProbabilityError as exception:
            pass
        else:
            raise
        self.assertNotEqual(binomial.pmf(0.5), binomial.pmf(0))
        self.assertEqual(binomial.pmf(0.5), 0)