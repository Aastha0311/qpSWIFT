from distutils.core import setup, Extension
import numpy as np

_qpSWIFT = Extension("qpSWIFT",
    sources= [
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/python/pyqpSWIFT.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_1.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_2.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_aat.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_control.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_defaults.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_dump.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_global.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_info.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_order.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_post_tree.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_postorder.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_preprocess.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/amd_valid.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/ldl.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/timer.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/Auxilary.c",
    "C:/Users/aasth/Desktop/star_humanoid/qpSWIFT/src/qpSWIFT.c" 
    ],
    include_dirs=["../include/",
    np.get_include(),
    ],
#    extra_compile_args=["-O3"
#    ]
    )

def main():
    setup(
    name="qpSWIFT",
    version="1.0.0",
    description="Python interface for qpSWIFT",
    author="Abhishek Pandala",
    setup_requires=["numpy >= 1.6"],
    install_requires=["numpy >= 1.6"],
    ext_modules=[_qpSWIFT]
    )

if __name__ == "__main__":
    main()
