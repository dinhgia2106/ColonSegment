# Tạm thời comment các import khác để tránh lỗi với MMCV 2.2.0
# from .ann_head import ANNHead
# from .apc_head import APCHead
# from .aspp_head import ASPPHead
# from .cc_head import CCHead
# from .da_head import DAHead
# from .dm_head import DMHead
# from .dnl_head import DNLHead
# from .ema_head import EMAHead
# from .enc_head import EncHead
# from .fcn_head import FCNHead
# from .fpn_head import FPNHead
# from .gc_head import GCHead
# from .lraspp_head import LRASPPHead
# from .nl_head import NLHead
# from .ocr_head import OCRHead
# from .point_head import PointHead
# from .psa_head import PSAHead
# from .psp_head import PSPHead
# from .sep_aspp_head import DepthwiseSeparableASPPHead
# from .sep_fcn_head import DepthwiseSeparableFCNHead
from .uper_head import UPerHead
# from .asm_uper_head import AsmUPerHead
# from .mini_uper_head import MiniUPerHead
# from .uper_head_v2 import UPerHeadV2
# from .segformer_head import SegFormerHead
# from .dual_segformer_head import DualSegFormerHead, DualSegFormerHead_ver2, SegFormerHead_ver2

__all__ = [
    # 'FCNHead', 'PSPHead', 'ASPPHead', 'PSAHead', 'NLHead', 'GCHead', 'CCHead',
    'UPerHead', 
    # 'DepthwiseSeparableASPPHead', 'ANNHead', 'DAHead', 'OCRHead',
    # 'EncHead', 'DepthwiseSeparableFCNHead', 'FPNHead', 'EMAHead', 'DNLHead',
    # 'PointHead', 'APCHead', 'DMHead', 'LRASPPHead',
    # 'SegFormerHead', 'DualSegFormerHead', 'DualSegFormerHead_ver2', 'UPerHeadV2', 'SegFormerHead_ver2'
]
