# -*- coding: utf-8 -*-
#
# Copyright (c) 2024 Aquent
#
# This software's license gives you freedom; you can copy, convey,
# propagate, redistribute and/or modify this program under the terms of
# the GNU Affero General Public License (AGPL) as published by the Free
# Software Foundation (FSF), either version 3 of the License, or (at your
# option) any later version of the AGPL published by the FSF.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero
# General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program in a file in the toplevel directory called
# "AGPLv3".  If not, see <http://www.gnu.org/licenses/>.
#

# Imports ###########################################################

from setuptools import setup, find_packages

# Main ##############################################################

setup(
    name='custom-reg-form',
    version='1.0',
    description='LMS - Custom Registration Extension Form',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    package_data={
        'custom_reg_form': ['migrations/*.py'],
    },
)
