# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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
    'name': 'Mrp Tempi in decimale di Ore',
    'version': '1.0',
    'category': 'Mrp',
    'description': """
     Premette di gestire i tempi in decimale di ore im modo da poter gestire anche tempi in secondi che altrimenti il widget non permette
     inoltre presuppone l'installazione del modulo decimal per definire anche i decimali da visualizzare
    """,
    'author': 'C & G Software',
    "depends" : ['mrp', 'decimal_precision'],
    "update_xml" : [
                 #   'security/ir.model.access.csv',
                    'mrp_view_dec.xml',
                 #   'wizard/product_buste.xml',
                    ],
    'website': 'http://www.cgsoftware.it',
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
