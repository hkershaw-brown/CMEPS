#!/usr/bin/env python

import os, shutil, sys

_CIMEROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","..","..","..")
sys.path.append(os.path.join(_CIMEROOT, "scripts", "Tools"))

from standard_script_setup import *
#pylint:disable=undefined-variable
logger = logging.getLogger(__name__)

def runseq(case, coupling_times):

    rundir    = case.get_value("RUNDIR")
    caseroot  = case.get_value("CASEROOT")
    comp_atm  = case.get_value("COMP_ATM")
    comp_ice  = case.get_value("COMP_ICE")
    comp_lnd  = case.get_value("COMP_LND")
    comp_ocn  = case.get_value("COMP_OCN")
    comp_rof  = case.get_value("COMP_ROF")
    comp_wav  = case.get_value("COMP_WAV")

    atm_cpl_dt = coupling_times["atm_cpl_dt"]
    ocn_cpl_dt = coupling_times["ocn_cpl_dt"]
    wav_cpl_dt = coupling_times["wav_cpl_dt"]
    lnd_cpl_dt = coupling_times["lnd_cpl_dt"]

    outfile   = open(os.path.join(caseroot, "CaseDocs", "nuopc.runseq"), "w")

    if (comp_atm == 'datm' and comp_ocn == "docn" and comp_ice == 'dice' and
        comp_rof == 'drof' and comp_wav == 'swav' and comp_lnd == 'slnd'):

        outfile.write ("runSeq::                               \n")
        outfile.write ("@" + str(ocn_cpl_dt) + "               \n")
        outfile.write ("  MED med_phases_prep_ocn_accum_avg    \n")
        outfile.write ("  MED -> OCN :remapMethod=redist       \n")
        if (atm_cpl_dt < ocn_cpl_dt):
            outfile.write ("  @" + str(atm_cpl_dt) + "         \n")
        outfile.write ("    MED med_phases_prep_ocn_map        \n")
        outfile.write ("    MED med_phases_aofluxes_run        \n")
        outfile.write ("    MED med_phases_prep_ocn_merge      \n")
        outfile.write ("    MED med_phases_prep_ocn_accum_fast \n")
        outfile.write ("    MED med_phases_ocnalb_run          \n")
        outfile.write ("    MED med_phases_prep_ice            \n")
        outfile.write ("    MED -> ICE :remapMethod=redist     \n")
        outfile.write ("    MED med_phases_prep_rof_accum      \n")
        outfile.write ("    MED med_phases_prep_rof_avg        \n")
        outfile.write ("    MED -> ROF :remapMethod=redist     \n")
        outfile.write ("    ICE                                \n")
        outfile.write ("    ROF                                \n")
        outfile.write ("    ICE -> MED :remapMethod=redist     \n")
        outfile.write ("    MED med_fraction_set               \n")
        outfile.write ("    ROF -> MED :remapMethod=redist     \n")
        outfile.write ("    MED med_phases_prep_atm            \n")
        outfile.write ("    MED -> ATM :remapMethod=redist     \n")
        outfile.write ("    ATM                                \n")
        outfile.write ("    ATM -> MED :remapMethod=redist     \n")
        outfile.write ("    MED med_phases_history_write       \n")
        outfile.write ("    MED med_phases_profile             \n")
        if (atm_cpl_dt < ocn_cpl_dt):
            outfile.write ("  @                                \n")
        outfile.write ("  OCN                                  \n")
        outfile.write ("  OCN -> MED :remapMethod=redist       \n")
        outfile.write ("  MED med_phases_restart_write         \n")
        outfile.write ("@                                      \n")
        outfile.write ("::                                     \n")

    elif (comp_atm == 'satm' and comp_ocn == "socn" and comp_ice == 'sice' and
          comp_rof == 'srof' and comp_wav == 'dwav' and comp_lnd == 'slnd'):

        outfile.write ("runSeq::                          \n" )
        outfile.write ("@" + str(wav_cpl_dt) + "          \n" )
        outfile.write ("  WAV                             \n" )
        outfile.write ("  WAV -> MED :remapMethod=redist  \n" )
        outfile.write ("  MED med_fraction_set            \n" )
        outfile.write ("  MED med_phases_history_write    \n" )
        outfile.write ("  MED med_phases_profile          \n" )
        outfile.write ("  MED med_phases_restart_write    \n" )
        outfile.write ("@                                 \n" )
        outfile.write ("::                                \n" )

    elif (comp_atm == 'satm' and comp_ocn == "socn" and comp_ice == 'sice' and
          comp_rof == 'srof' and comp_wav == 'swav' and comp_lnd == 'dlnd'):

        outfile.write ("runSeq::                         \n" )
        outfile.write ("@" + str(lnd_cpl_dt) + "         \n" )
        outfile.write ("  LND                            \n" )
        outfile.write ("  LND -> MED :remapMethod=redist \n" )
        outfile.write ("  MED med_fraction_set           \n" )
        outfile.write ("  MED med_phases_history_write   \n" )
        outfile.write ("  MED med_phases_profile         \n" )
        outfile.write ("  MED med_phases_restart_write   \n" )
        outfile.write ("@                                \n" )
        outfile.write ("::                               \n" )

    elif (comp_atm == 'datm' and comp_ocn == "docn" and comp_ice == 'sice' and
          comp_rof == 'srof' and comp_wav == 'swav' and comp_lnd == 'slnd'):

        outfile.write ("runSeq::                               \n")
        outfile.write ("@" + str(ocn_cpl_dt) + "               \n")
        outfile.write ("  MED med_phases_prep_ocn_accum_avg    \n")
        outfile.write ("  MED -> OCN :remapMethod=redist       \n")
        if (atm_cpl_dt < ocn_cpl_dt):
            outfile.write ("  @" + str(atm_cpl_dt) + "         \n")
        outfile.write ("    MED med_phases_prep_ocn_map        \n")
        outfile.write ("    MED med_phases_aofluxes_run        \n")
        outfile.write ("    MED med_phases_prep_ocn_merge      \n")
        outfile.write ("    MED med_phases_prep_ocn_accum_fast \n")
        outfile.write ("    MED med_phases_ocnalb_run          \n")
        outfile.write ("    MED med_fraction_set               \n")
        outfile.write ("    MED med_phases_prep_atm            \n")
        outfile.write ("    MED -> ATM :remapMethod=redist     \n")
        outfile.write ("    ATM                                \n")
        outfile.write ("    ATM -> MED :remapMethod=redist     \n")
        outfile.write ("    MED med_phases_history_write       \n")
        outfile.write ("    MED med_phases_profile             \n")
        if (atm_cpl_dt < ocn_cpl_dt):
            outfile.write ("  @                                \n")
        outfile.write ("  OCN                                  \n")
        outfile.write ("  OCN -> MED :remapMethod=redist       \n")
        outfile.write ("  MED med_phases_restart_write         \n")
        outfile.write ("@                                      \n")
        outfile.write ("::                                     \n")

    outfile.close()
    shutil.copy(os.path.join(caseroot, "CaseDocs", "nuopc.runseq"), rundir)
