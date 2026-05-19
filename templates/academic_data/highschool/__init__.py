# # High School Academic Data Module
# # Contains CBSE curriculum data for grades 9-12

# from .cbse_9 import CBSE_9_DATA
# from .cbse_10 import CBSE_10_DATA
# from .cbse_11 import CBSE_11_DATA
# from .cbse_12 import CBSE_12_DATA

# __all__ = ['CBSE_9_DATA', 'CBSE_10_DATA', 'CBSE_11_DATA', 'CBSE_12_DATA']

# High School Academic Data Module
# Contains curriculum data for multiple boards:
# CBSE (grades 8-12), IB MYP (grades 8-10), ICSE (grades 8-10), IGCSE (grades 8-10)

from .cbse_9 import CBSE_9_DATA
from .cbse_10 import CBSE_10_DATA
from .cbse_11 import CBSE_11_DATA
from .cbse_12 import CBSE_12_DATA

# CBSE stream-specific data for grades 11-12
from .cbse_11_com import CBSE_11_COM_DATA
from .cbse_11_commat import CBSE_11_COMMAT_DATA
from .cbse_11_pcb import CBSE_11_PCB_DATA
from .cbse_11_pcm import CBSE_11_PCM_DATA
from .cbse_11_pcmb import CBSE_11_PCMB_DATA
from .cbse_12_com import CBSE_12_COM_DATA
from .cbse_12_commat import CBSE_12_COMMAT_DATA
from .cbse_12_pcb import CBSE_12_PCB_DATA
from .cbse_12_pcm import CBSE_12_PCM_DATA
from .cbse_12_pcmb import CBSE_12_PCMB_DATA

# High school data for other curricula
from .hs_cbse_8 import HS_CBSE_8_DATA
from .hs_cbse_9 import HS_CBSE_9_DATA
from .hs_cbse_10 import HS_CBSE_10_DATA
from .hs_ib_8 import HS_IB_8_DATA
from .hs_ib_9 import HS_IB_9_DATA
from .hs_ib_10 import HS_IB_10_DATA
from .hs_icse_8 import HS_ICSE_8_DATA
from .hs_icse_9 import HS_ICSE_9_DATA
from .hs_icse_10 import HS_ICSE_10_DATA
from .hs_igcse_8 import HS_IGCSE_8_DATA
from .hs_igcse_9 import HS_IGCSE_9_DATA
from .hs_igcse_10 import HS_IGCSE_10_DATA

__all__ = [
    'CBSE_9_DATA',
    'CBSE_10_DATA',
    'CBSE_11_DATA',
    'CBSE_12_DATA',
    'CBSE_11_COM_DATA',
    'CBSE_11_COMMAT_DATA',
    'CBSE_11_PCB_DATA',
    'CBSE_11_PCM_DATA',
    'CBSE_11_PCMB_DATA',
    'CBSE_12_COM_DATA',
    'CBSE_12_COMMAT_DATA',
    'CBSE_12_PCB_DATA',
    'CBSE_12_PCM_DATA',
    'CBSE_12_PCMB_DATA',
    'HS_CBSE_8_DATA',
    'HS_CBSE_9_DATA',
    'HS_CBSE_10_DATA',
    'HS_IB_8_DATA',
    'HS_IB_9_DATA',
    'HS_IB_10_DATA',
    'HS_ICSE_8_DATA',
    'HS_ICSE_9_DATA',
    'HS_ICSE_10_DATA',
    'HS_IGCSE_8_DATA',
    'HS_IGCSE_9_DATA',
    'HS_IGCSE_10_DATA',
]