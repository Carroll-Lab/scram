#!/usr/bin/python
# encoding: utf-8
'''

SCRAM - Small Complementary RnA Mapper

Command line module


@author:     Stephen Fletcher

@copyright:  2016 Stephen Fletcher. All rights reserved.

@license:    MIT

@contact:    s.fletcher@uq.edu.au
@deffield    updated: Updated
'''

import sys
import os
import analysis

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from sets import Set

__all__ = []
__version__ = 0.2
__date__ = '2016-02-23'
__updated__ = '2016-02-23'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    ana_accepted=Set(['den','denAv', 'mnt3dm' , 'mnt3dmAv','multiDen',
                      'avMultiDen','CDP','avCDP' ,'sCDP'])   
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, 
                                                     program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  SCRAM - Small Complementary RnA Mapper
  
  Created by Stephen Fletcher on %s.
  Copyright 2016 Stephen Fletcher. All rights reserved.

  Licensed under the MIT licence

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, 
                                formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument('analysis_type', type = str, help = "den (single\
             reference and sequence file, denAv (single reference, \
             average of 2 seq files), mnt3dm (21, 22 and 24nt \
             alignment - single reference and sequence file, \
             mnt3dmAv (21, 22 and 24 nt - single reference and  average of\
             2 seq files, \
             multiDen (multi seq files and reference sequences), \
             avMultiDen (multi seq files in replicate and reference sequences),\
             CDP, avCDP (average Comparative density plot,  \
            (comparative density plot), \
            sCDP (single multi-seq alignment")
        parser.add_argument('reference_file', 
                            type = str, help = "Reference file (.fasta format)")     
        parser.add_argument('-s1', '--seq_file_1', 
                            type = str, help = "Sequence file 1")
        parser.add_argument('-s2', '--seq_file_2', 
                            type = str, help = "Sequence file 2")
        parser.add_argument('-s3', '--seq_file_3', 
                            type = str, help = "Sequence file 3")
        parser.add_argument('-s4', '--seq_file_4', 
                            type = str, help = "Sequence file 4")    
        parser.add_argument('-nt','--sRNA_len', 
                            type=int, default = 21)
        parser.add_argument('-f', '--file_name', 
                            type=str, default = "NO_PLOT", 
                            help= "Figure output file name")
        parser.add_argument('-seq_list', '--seq_list', 
                            type = str, help = "Sequence file list \
                            (full path)")    
        parser.add_argument('-min_read', 
                            '--min_read_size', type = int, 
                            help = "Minimum length of sRNA reads analysed \
                            (default=18)", 
                            default=18)
        parser.add_argument('-max_read', '--max_read_size', type = int, 
                            help = "Maximum length of sRNA reads analysed \
                            (default=32)", 
                            default = 32)
        parser.add_argument('-min_count', '--min_read_count', type = int, 
                            help = "Minimum read count for an sRNA to be \
                            analysed (default=1)", 
                            default = 1)        
        parser.add_argument('-win', '--smooth_win_size', type = int, 
                            help = "Window size for smoothing (default=50)", 
                            default = 50)
        parser.add_argument('-ylim', '--ylim',
                            type = float, help = '+/- y axis limit', 
                            default = 0)
        parser.add_argument('-no_display', '--no_display', 
                            action='store_false', default=True, 
                            help = 'Do not display on screen for single type \
                            analyses')
        parser.add_argument('-split', '--split_reads', action='store_false', 
                            default=True, 
                            help = 'Split reads alignment counts based on no. \
                            of alignments')
        parser.add_argument('-pub','--publish', action='store_true', 
                            default=False, 
                            help='Remove all labels from density maps for \
                            publication')

        parser.add_argument('-V', '--version', 
                            action='version', version=program_version_message)
        # Process arguments
        args = parser.parse_args()

        ana = args.analysis_type
        ref = args.reference_file
        seq1 = args.seq_file_1
        seq2 = args.seq_file_2
        seq3 = args.seq_file_3
        seq4 = args.seq_file_4
        nt = args.sRNA_len
        f = args.file_name
        seq_list=args.seq_list
        min_read=args.min_read_size
        max_read=args.max_read_size
        min_count=args.min_read_count
        win=args.smooth_win_size
        ylim=args.ylim
        no_display=args.no_display
        split = args.split_reads
        pub = args.publish

        #plot figure or not
        if ana not in ana_accepted:
            print "\nEXITING!\n\n{0} is not a recognized analysis type.\n"\
                .format(ana)
        
        
        if f == 'NO_PLOT': 
            fileFig=False
        else:
            fileFig=True        
 
        if ana == 'den':
            analysis.single_ref_coverage(seq1, 
                                         ref, 
                                         nt, 
                                         win, 
                                         fileFig, 
                                         f, 
                                         min_read, 
                                         max_read, 
                                         min_count, 
                                         no_display, 
                                         pub)  #fix the trues

        elif ana == 'denAv':
            analysis.single_ref_coverage_av(seq1, 
                                            seq2, 
                                            ref, 
                                            nt, 
                                            win, 
                                            fileFig, 
                                            f, 
                                            min_read, 
                                            max_read, 
                                            min_count, 
                                            no_display, 
                                            pub)  
 
        elif ana == 'mnt3dm':
            analysis.single_ref_coverage_21_22_24(seq1, 
                                                  ref, 
                                                  win, 
                                                  fileFig, 
                                                  f, 
                                                  min_read, 
                                                  max_read, 
                                                  min_count, 
                                                  no_display, 
                                                  ylim, 
                                                  pub)
        elif ana == 'mnt3dmAv':
            analysis.single_ref_coverage_21_22_24_av(seq1, 
                                                     seq2,
                                                     ref, 
                                                     win, 
                                                     fileFig, 
                                                     f, 
                                                     min_read, 
                                                     max_read, 
                                                     min_count, 
                                                     no_display, 
                                                     ylim, 
                                                     pub)
        elif ana == 'multiDen':
            fileFig=True
            analysis.multi_seq_and_ref_21_22_24(seq_list, 
                                                ref, 
                                                win, 
                                                fileFig, 
                                                f, 
                                                min_read, 
                                                max_read, 
                                                min_count, 
                                                False, 
                                                False, 
                                                ylim, 
                                                pub)
        elif ana == 'avMultiDen':
            fileFig=True
            analysis.av_multi_seq_and_ref_21_22_24(seq_list, 
                                                   ref, 
                                                   win, 
                                                   fileFig, 
                                                   f, 
                                                   min_read, 
                                                   max_read, 
                                                   min_count, 
                                                   False, 
                                                   False, 
                                                   ylim, 
                                                   pub)
           
 
        
        elif ana =='avCDP':
            if split is False:
                analysis.avCDP_split(seq1, 
                                     seq2, 
                                     seq3, 
                                     seq4, 
                                     ref, 
                                     nt, 
                                     fileFig, 
                                     f, 
                                     min_read, 
                                     max_read, 
                                     min_count, 
                                     no_display,
                                     pub)
            else:
                analysis.avCDP(seq1, 
                               seq2, 
                               seq3, 
                               seq4, 
                               ref, 
                               nt, 
                               fileFig, 
                               f, 
                               min_read, 
                               max_read, 
                               min_count, 
                               no_display,
                               pub)
        elif ana =='CDP':
            if split is False:
                analysis.CDP_split(seq1, 
                                   seq2, 
                                   ref, 
                                   nt, 
                                   fileFig, 
                                   f, 
                                   min_read, 
                                   max_read, 
                                   min_count, 
                                   no_display)
            else:
                analysis.CDP(seq1, 
                             seq2, 
                             ref, 
                             nt, 
                             fileFig, 
                             f, 
                             min_read, 
                             max_read, 
                             min_count, 
                             no_display)
        elif ana =='sCDP':
            analysis.CDP_single_split(seq1, 
                                      ref, 
                                      nt, 
                                      min_read, 
                                      max_read, 
                                      min_count)
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2

if __name__ == "__main__":
    main()
