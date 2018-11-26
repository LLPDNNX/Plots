xsecs = {
    
    # T1 qqqq LL gluino pair production and decay at 2.5 TeV
    # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVgluglu

    "SMS-T1qqqq_ctau-0p001_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-0p01_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
    "SMS-T1qqqq_ctau-100000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.0000768,
 
    # Drell-Yan + jets
    # NLO
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z
    "DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":147.40,
    "DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":40.99 ,
    "DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":5.678,
    "DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":1.367,
    "DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.6304,
    "DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.1514,
    "DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.003565 ,
    # "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8":18610,
    # "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8":1921.8*3,
    
    # QCD (multijet)
    # LO
    "QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":27990000,
    "QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":1712000,
    "QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":347700,
    "QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":32100,
    "QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":6831,
    "QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":1207,
    "QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":119.9,
    "QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":25.24,
    
    # Single-top
    # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_t_channel_cross_secti
    # NLO
    "ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1": 10.32,
    "ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1": 80.95,
    "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1": 136.02,
    "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1": 71.7/2.,
    "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1": 71.7/2.,
    
    # TTbar
    # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (mtop=172.5 GeV)
    # missing
    #"TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-evtgen": 831.76,
    # NLO
    "TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8": 831.76,
    # LO
    "TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 831.76,
    "TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 2.666535,
    "TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 1.098082,
    "TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 0.198748, 
    "TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 0.002368413,
    "TTJets_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8": 831.76*0.5*(1-3*0.1086)*(3*0.1086)*2,
    "TTJets_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8": 831.76*0.5*(1-3*0.1086)*(3*0.1086)*2,

    # W->l nu + jets
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
    # NLO
    "WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 0*1.21, 
    "WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 1345*1.21,
    "WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 359.7*1.21,
    "WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 48.91*1.21,
    "WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 12.05*1.21,
    "WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 5.501*1.21,
    "WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 1.329*1.21,
    "WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 0.03216*1.21 ,
    
    # Z -> nu nu + jets
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
    # LO
    "ZJetsToNuNu_HT-100To200_13TeV-madgraph": 280.35*1.23 ,
    "ZJetsToNuNu_HT-200To400_13TeV-madgraph": 77.67*1.23 ,
    "ZJetsToNuNu_HT-400To600_13TeV-madgraph": 10.73*1.23 ,
    "ZJetsToNuNu_HT-600To800_13TeV-madgraph": 2.559*1.23 ,
    "ZJetsToNuNu_HT-800to1200_13TeV-madgraph": 1.1796*1.23 ,
    "ZJetsToNuNu_HT-1200To2500_13TeV-madgraph": 0.28833*1.23 ,
    "ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph": 0.006945*1.23 ,
    
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
    # NNLO
    "WW_TuneCUETP8M1_13TeV-pythia8": 118.7,
    
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
    # NLO
    "WZ_TuneCUETP8M1_13TeV-pythia8": 47.13,
    "ZZ_TuneCUETP8M1_13TeV-pythia8": 16.523,
}
