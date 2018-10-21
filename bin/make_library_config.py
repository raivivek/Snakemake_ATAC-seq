#! /usr/bin/env python
#
# Peter Orchard
# porchard@umich.edu
#
# Vivek Rai
# vivekrai@umich.edu
#
# University of Michigan
# (c) Parker Lab
#

__description__ = """
    Dump YAML formatted ATAC-seq experiment configuration. The configuration
    is generated by parsing FASTQ filenames. For example,

    'ABCD1':
        genome: hg19
        readgroups:
            'ABCD1_L1':
                - 'ABCD1_L1.1.fastq.gz'
                - 'ABCD1_L1.2.fastq.gz'
            'ABCD1_L2':
                - 'ABCD1_L2.1.fastq.gz'
                - 'ABCD1_L2.2.fastq.gz'
"""



import sys
import re
import yaml
import pathlib

# match files such as atacseq.1.fq.gz or atacseq.2.fastq.gz
FASTQ_RE = '(.*).([12]).(?:fastq|fq).*'

LIBRARIES = {}


def parse_fastq_name(f):
    """ Return FASTQ "library" name and whether it is "first" or "second" set
    of reads (paired-end)."""

    m = re.search(FASTQ_RE, os.path.basename(f))
    library = m.group(1)
    first_or_second = m.group(2)
    return [library, first_or_second]

def create_library_item(fastq):
    """ Parse FASTQ filenames; and return a dictionary with library names
    containing FASTQ files. For example, a library entry looks like
    
    {
        'genome': 'hg19',
        'readgroups': ['ABCD123.1.fastq.gz', 'ABCD123.2.fastq.gz']
    }
    
    """

    pass




if __name__=='__main__':
    #print(yaml.dump(LIBRARIES, indent=4, default_flow_style=False))
    pass
