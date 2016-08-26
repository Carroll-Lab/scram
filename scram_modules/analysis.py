'''
Created on 22 Jan 2016

@author: steve
'''
"""
Analysis module
"""
from ref_seq import Ref_Seq
from srna_seq import SRNA_Seq
import write_to_file
import cdp
import analysis_helper as ah
import den as dn


def single_ref_coverage(seq_file_list, ref_file, nt, smoothWinSize=50, 
    fileFig = False, fileName = 'plot.pdf', min_read_size = 18, 
    max_read_size = 32, min_read_no=1, onscreen = False, no_csv = False, 
    ylim=0, pub=False, split=False):
    """
    Aligns reads from a single read file to a single reference sequence for
    a single sRNA size.
    """

    seq=SRNA_Seq()
    if len(seq_file_list)==1:
        seq.load_seq_file(seq_file_list[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq.load_seq_file_arg_list(seq_file_list, max_read_size, min_read_no, 
        min_read_size)
    # single_seq_output = ah.single_file_output(seq_file)
    seq_name = ah.single_file_output(seq_file_list[0])
    if len(seq_file_list)>1:
        for i in range(len(seq_file_list)):
            if i == 0:
                pass
            else:
                seq_name+= "_{0}".format(ah.single_file_output(seq_file_list[i]))      
    dn.ref_coverage(seq, seq_name, ref_file, nt, smoothWinSize, fileFig, 
                 fileName, min_read_size, max_read_size, min_read_no, 
                 onscreen, no_csv, ylim, pub, split)


def single_ref_coverage_21_22_24(seq_file_list, ref_file, smoothWinSize=50, 
    fileFig = True, fileName = 'plot.pdf', min_read_size = 18, 
    max_read_size = 32, min_read_no=1, onscreen = True, no_csv=False,
    y_lim=0, pub=False, split=False):
    """
    Align reads from a single seq file to a single reference for 21,22 and 24nt
    """

    seq=SRNA_Seq()
    if len(seq_file_list)==1:
        seq.load_seq_file(seq_file_list[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq.load_seq_file_arg_list(seq_file_list, max_read_size, min_read_no, 
        min_read_size)
    # single_seq_output = ah.single_file_output(seq_file)
    seq_name = ah.single_file_output(seq_file_list[0])
    if len(seq_file_list)>1:
        for i in range(len(seq_file_list)):
            if i == 0:
                pass
            else:
                seq_name+= "_{0}".format(ah.single_file_output(seq_file_list[i]))    
    dn.coverage_21_22_24(seq, seq_name, ref_file, smoothWinSize, 
    fileFig, fileName, min_read_size, max_read_size, min_read_no,
    onscreen, no_csv,y_lim, pub, split)


def CDP(seq_file_list_1, seq_file_list_2, ref_file, nt, 
    fileFig=False, fileName = 'plot.pdf', 
    min_read_size = 18, max_read_size = 32, min_read_no=1, onscreen = False,
    pub=True,processes=4):
    """
    Plots alignment count for each sRNA in ref file as (x,y)
    for 2 seq files.  No splitting of read count
    """  

    seq_1=SRNA_Seq()
    if len(seq_file_list_1)==1:
        seq_1.load_seq_file(seq_file_list_1[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq_1.load_seq_file_arg_list(seq_file_list_1, max_read_size, min_read_no, 
        min_read_size)

    seq_2=SRNA_Seq()
    if len(seq_file_list_2)==1:
        seq_2.load_seq_file(seq_file_list_2[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq_2.load_seq_file_arg_list(seq_file_list_2, max_read_size, min_read_no, 
        min_read_size)    
    
    #REPEATED CODE - new function required
    seq_name_1 = ah.single_file_output(seq_file_list_1[0])
    if len(seq_file_list_1)>1:
        for i in range(len(seq_file_list_1)):
            if i == 0:
                pass
            else:
                seq_name_1+= "_{0}".format(ah.single_file_output(seq_file_list_1[i]))
    
    seq_name_2 = ah.single_file_output(seq_file_list_2[0])
    if len(seq_file_list_2)>1:
        for i in range(len(seq_file_list_2)):
            if i == 0:
                pass
            else:
                seq_name_2+= "_{0}".format(ah.single_file_output(seq_file_list_2[i]))

    
    cdp.CDP_shared(seq_1, seq_2, seq_name_1, seq_name_2, ref_file, nt,fileFig, 
               fileName, min_read_size, max_read_size, min_read_no, onscreen,
               pub, processes)


def CDP_split(seq_file_list_1, seq_file_list_2, ref_file, nt, 
    fileFig=False, fileName = 'plot.pdf', 
    min_read_size = 18, max_read_size = 32, min_read_no=1, onscreen = False,
    pub=False, processes=4):

    """
    Plots alignment count for each sRNA in ref file as (x,y)
    for 2 seq files.  Read count split by number of times an sRNA aligns
      
    """  

    seq_1=SRNA_Seq()
    if len(seq_file_list_1)==1:
        seq_1.load_seq_file(seq_file_list_1[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq_1.load_seq_file_arg_list(seq_file_list_1, max_read_size, min_read_no, 
        min_read_size)

    seq_2=SRNA_Seq()
    if len(seq_file_list_2)==1:
        seq_2.load_seq_file(seq_file_list_2[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq_2.load_seq_file_arg_list(seq_file_list_2, max_read_size, min_read_no, 
        min_read_size)   
    
    
    seq_name_1 = ah.single_file_output(seq_file_list_1[0])
    if len(seq_file_list_1)>1:
        for i in range(len(seq_file_list_1)):
            if i == 0:
                pass
            else:
                seq_name_1+= "_{0}".format(ah.single_file_output(seq_file_list_1[i]))
    
    seq_name_2 = ah.single_file_output(seq_file_list_2[0])
    if len(seq_file_list_2)>1:
        for i in range(len(seq_file_list_2)):
            if i == 0:
                pass
            else:
                seq_name_2+= "_{0}".format(ah.single_file_output(seq_file_list_2[i]))
    
    cdp.CDP_split_shared(seq_1, seq_2, seq_name_1, seq_name_2, ref_file, 
                     nt, fileFig, fileName,min_read_size, max_read_size, 
                     min_read_no, onscreen, pub, processes)


def CDP_single_split(seq_file_list_1, ref_file, nt, 
    min_read_size = 18, max_read_size = 32, min_read_no=1):
    """
    Normalised split alignments for a single reference - all recorded
    including 0
    
    
    TODO: may be incorrect - check with unit tests!!!!!!
    """

    refs = Ref_Seq()
    refs.load_ref_file(ref_file)
    seq_1=SRNA_Seq()
    if len(seq_file_list_1)==1:
        seq_1.load_seq_file(seq_file_list_1[0], max_read_size, min_read_no, 
        min_read_size)
    else:
        seq_1.load_seq_file_arg_list(seq_file_list_1, max_read_size, min_read_no, 
        min_read_size)
    
    seq_name_1 = ah.single_file_output(seq_file_list_1[0])
    if len(seq_file_list_1)>1:
        for i in range(len(seq_file_list_1)):
            if i == 0:
                pass
            else:
                seq_name_1+= "_{0}".format(ah.single_file_output(seq_file_list_1[i]))

    alignment_dict_1={} #header:aligned_sRNAs


    sRNA_align_count_1={} #sRNA:no_of_times_aligned


    header_split_count_1={} #header:count


    counts_by_ref = {} #header (align_count_1, align_count_2)

    #calc aligned sRNAs for each header, duplicate if necessary
    for header, single_ref in refs:

        alignment_dict_1[header] = \
        cdp.list_align_reads_to_seq_split(seq_1, single_ref, nt)
        
    
    #calc no of times each sRNA is aligned - 1    
    for header, sRNA_list in alignment_dict_1.iteritems():
        for sRNA in sRNA_list:
            if sRNA in sRNA_align_count_1:
                sRNA_align_count_1[sRNA] +=1
            else:
                sRNA_align_count_1[sRNA] = 1


    #calc split alignment count for each header - 1
    for header, sRNA_list in alignment_dict_1.iteritems():
        header_split_count_1[header] = 0
        for sRNA in sRNA_list:
            header_split_count_1[header] +=seq_1[sRNA]/sRNA_align_count_1[sRNA]

    #construct x,y counts for each header
    for header in refs.headers():

        counts_by_ref[header] = header_split_count_1[header]


    write_to_file.cdp_single_output(counts_by_ref, 
                                    seq_name_1, 
                                    nt)