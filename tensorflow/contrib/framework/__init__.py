# Copyright 2016 Google Inc. All Rights Reserved.
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
# ==============================================================================

"""Framework utilities.

@@assert_same_float_dtype
@@assert_scalar_int
@@convert_to_tensor_or_sparse_tensor
@@local_variable
@@reduce_sum_n
@@safe_embedding_lookup_sparse
@@with_shape
@@with_same_shape

@@get_graph_from_inputs
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys

# pylint: disable=unused-import,wildcard-import
from tensorflow.contrib.framework.python.framework import *
from tensorflow.contrib.framework.python.ops import *
from tensorflow.python.util.all_util import make_all

__all__ = make_all(__name__)
