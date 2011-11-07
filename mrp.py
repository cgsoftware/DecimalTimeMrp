# -*- coding: utf-8 -*-
from datetime import datetime
from osv import osv, fields
from tools.translate import _
import netsvc
import time
import tools
import decimal_precision as dp


class mrp_workcenter(osv.osv):
    # mmoooo
    _inherit = 'mrp.workcenter'
    _columns = {
                'time_cycle': fields.float('Time for 1 cycle (hour)', help="Time in hours for doing one cycle.", digits_compute=dp.get_precision('Mrp Qty')),
                'time_start': fields.float('Time before prod.', help="Time in hours for the setup.", digits_compute=dp.get_precision('Mrp Qty')),
                'time_stop': fields.float('Time after prod.', help="Time in hours for the cleaning.", digits_compute=dp.get_precision('Mrp Qty')),

                }


mrp_workcenter()



class mrp_routing_workcenter(osv.osv):
    """
    Defines working cycles and hours of a workcenter using routings.
    """
    _inherit = 'mrp.routing.workcenter'
    _columns = {
                'hour_nbr': fields.float('Number of Hours', required=True,digits_compute=dp.get_precision('Mrp Qty'),
                                          help="Time in hours for this work center to achieve the operation of the specified routing."),
                }
    
mrp_routing_workcenter() 