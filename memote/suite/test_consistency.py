# -*- coding: utf-8 -*-

# Copyright 2017 Novo Nordisk Foundation Center for Biosustainability,
# Technical University of Denmark.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Supporting functions for consistency checks performed on the model object.
"""

from __future__ import absolute_import

import logging

from memote.support.consistency import (
    check_stoichiometric_consistency, find_unconserved_metabolites)

LOGGER = logging.getLogger(__name__)


def test_stoichiometric_consistency(model):
    """Expect that the metabolic model is mass-balanced."""
    assert check_stoichiometric_consistency(model),\
        "The following metabolites are involved in unconserved reactions:"\
        " {}".format(find_unconserved_metabolites(model))
