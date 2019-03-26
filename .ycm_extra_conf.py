import os

def Settings( **kwargs ):
  return {
    'flags': [
        '-x',
        'c',
        '-Wall',
        '-Wstrict-prototypes',
        '-Wmissing-prototypes',
        '-DMODULE',
        '-D__KERNEL__',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/arch/x86/include',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/arch/x86/include/generated',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/include',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/arch/x86/include/uapi',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/arch/x86/include/generated/uapi',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/include/uapi',
        '-isystem', '/lib/modules/' + os.uname().release + '/build/include/generated/uapi',
        '-include', '/lib/modules/' + os.uname().release + '/build/include/linux/kconfig.h',
    ],
  }

