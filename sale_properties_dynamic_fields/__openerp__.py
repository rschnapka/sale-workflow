# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    @author Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Dynamic fields for sale order line properties",
    'version': '0.1',
    'category': '',
    'description': """
This module allows to dynamically draw properties groups on sale order lines.
That is, if you have a property group 'Length' and set it as
'Draw dynamically', the module will automatically add the x_length field to
the sale order line and visualize it as char field in the form view.
When fill the 'Length' field, the module will update the properties field
(property_ids) according to it.
This allows to set the line's properties through normal fields, instead of
creating new properties or selecting existing properties.
""",
    'author': 'Agile Business Group',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'sale_properties_easy_creation',
    ],
    "data": [
        'mrp_property_group_view.xml',
    ],
    "demo": [
    ],
    "test": [
        'test/properties.yml',
    ],
    "active": False,
    "installable": True
}
