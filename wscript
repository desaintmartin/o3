import platform

srcdir = '.'
blddir = 'build'
VERSION = '0.0.1'

def set_options(opt):
  opt.tool_options('compiler_cxx')

def configure(conf):
  c_flags = ['-O3', '-ffast-math', '-fno-strict-aliasing']
  # Don't append msse2 switch if not supported by architecture.
  if not 'arm' in platform.machine():
    c_flags.append('-msse2')
  conf.check_tool('compiler_cxx')
  conf.check_tool('node_addon')
  conf.add_os_flags('LDFLAGS','LINKFLAGS')
  conf.env.append_value('CCFLAGS', c_flags)
  conf.env.append_value('CXXFLAGS', c_flags)

def build(bld):
  obj = bld.new_task_gen('cxx', 'shlib', 'node_addon')
  obj.target = 'o3'
  obj.source = 'hosts/node-o3/sh_node.cc hosts/node-o3/sh_node_libs.cc'

  obj.includes = """
    include
    hosts
    modules
    deps
  """

  obj.lib = 'xml2'
