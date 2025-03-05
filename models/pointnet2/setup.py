from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# Add the THRUST_IGNORE_CUB_VERSION_CHECK flag to the nvcc arguments
extra_compile_args = {
    'cxx': ['-g'],
    'nvcc': [
        '-O2', 
        '-D_GLIBCXX_USE_CXX11_ABI=0',
        '-DTHRUST_IGNORE_CUB_VERSION_CHECK'
    ]
}

setup(
    name='pointnet2',
    ext_modules=[
        CUDAExtension('pointnet2_cuda', [
            'src/pointnet2_api.cpp',
            
            'src/ball_query.cpp', 
            'src/ball_query_gpu.cu',
            'src/group_points.cpp', 
            'src/group_points_gpu.cu',
            'src/interpolate.cpp', 
            'src/interpolate_gpu.cu',
            'src/sampling.cpp', 
            'src/sampling_gpu.cu',
        ],
        extra_compile_args=extra_compile_args)
    ],
    cmdclass={'build_ext': BuildExtension}
)
