"""Setup extension

Notes:
    If extra_compile_args is provided, you need to provide different instances for different extensions.
    Refer to https://github.com/pytorch/pytorch/issues/20169

"""

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# add the THRUST_IGNORE_CUB_VERSION_CHECK flag to the nvcc arguments
extra_compile_args = {
    'cxx': ['-g'],
    'nvcc': [
        '-O2', 
        '-D_GLIBCXX_USE_CXX11_ABI=0',
        '-DTHRUST_IGNORE_CUB_VERSION_CHECK'
    ]
}

setup(
    name='emd_ext',
    ext_modules=[
        CUDAExtension(
            name='emd_cuda',
            sources=[
                'cuda/emd.cpp',
                'cuda/emd_kernel.cu',
            ],
            extra_compile_args=extra_compile_args
        ),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
