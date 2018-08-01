#!/usr/bin/python

import ROOT
import numpy
import random
import math
import os
import re
import json
from optparse import OptionParser

cvscale = 1.0

fontScale = 750./650.

ROOT.gROOT.SetBatch(True)
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(0)
ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit(1111)
ROOT.gStyle.SetPadTopMargin(0.08)
ROOT.gStyle.SetPadLeftMargin(0.145)
ROOT.gStyle.SetPadRightMargin(0.26)
ROOT.gStyle.SetPadBottomMargin(0.15)
ROOT.gStyle.SetStatFontSize(0.025)

ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetOptStat(0)

# For the canvas:
ROOT.gStyle.SetCanvasBorderMode(0)
ROOT.gStyle.SetCanvasColor(ROOT.kWhite)
ROOT.gStyle.SetCanvasDefH(700) #Height of canvas
ROOT.gStyle.SetCanvasDefW(800) #Width of canvas
ROOT.gStyle.SetCanvasDefX(0)   #POsition on screen
ROOT.gStyle.SetCanvasDefY(0)

# For the Pad:
ROOT.gStyle.SetPadBorderMode(0)
# ROOT.gStyle.SetPadBorderSize(Width_t size = 1)
ROOT.gStyle.SetPadColor(ROOT.kWhite)
#ROOT.gStyle.SetPadGridX(True)
#ROOT.gStyle.SetPadGridY(True)
ROOT.gStyle.SetGridColor(ROOT.kBlack)
ROOT.gStyle.SetGridStyle(2)
ROOT.gStyle.SetGridWidth(1)

# For the frame:

ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetFrameBorderSize(0)
ROOT.gStyle.SetFrameFillColor(0)
ROOT.gStyle.SetFrameFillStyle(0)
ROOT.gStyle.SetFrameLineColor(1)
ROOT.gStyle.SetFrameLineStyle(1)
ROOT.gStyle.SetFrameLineWidth(0)

# For the histo:
# ROOT.gStyle.SetHistFillColor(1)
# ROOT.gStyle.SetHistFillStyle(0)
# ROOT.gStyle.SetLegoInnerR(Float_t rad = 0.5)
# ROOT.gStyle.SetNumberContours(Int_t number = 20)

ROOT.gStyle.SetEndErrorSize(2)
#ROOT.gStyle.SetErrorMarker(20)
ROOT.gStyle.SetErrorX(0.)

ROOT.gStyle.SetMarkerStyle(20)
#ROOT.gStyle.SetMarkerStyle(20)

#For the fit/function:
ROOT.gStyle.SetOptFit(1)
ROOT.gStyle.SetFitFormat("5.4g")
ROOT.gStyle.SetFuncColor(2)
ROOT.gStyle.SetFuncStyle(1)
ROOT.gStyle.SetFuncWidth(1)

#For the date:
ROOT.gStyle.SetOptDate(0)
# ROOT.gStyle.SetDateX(Float_t x = 0.01)
# ROOT.gStyle.SetDateY(Float_t y = 0.01)

# For the statistics box:
ROOT.gStyle.SetOptFile(0)
ROOT.gStyle.SetOptStat(0) # To display the mean and RMS:   SetOptStat("mr")
ROOT.gStyle.SetStatColor(ROOT.kWhite)
ROOT.gStyle.SetStatFont(42)
ROOT.gStyle.SetStatFontSize(0.025)
ROOT.gStyle.SetStatTextColor(1)
ROOT.gStyle.SetStatFormat("6.4g")
ROOT.gStyle.SetStatBorderSize(1)
ROOT.gStyle.SetStatH(0.1)
ROOT.gStyle.SetStatW(0.15)

ROOT.gStyle.SetHatchesSpacing(1)
ROOT.gStyle.SetHatchesLineWidth(2)

# ROOT.gStyle.SetStaROOT.TStyle(Style_t style = 1001)
# ROOT.gStyle.SetStatX(Float_t x = 0)
# ROOT.gStyle.SetStatY(Float_t y = 0)


#ROOT.gROOT.ForceStyle(True)
#end modified

# For the Global title:

ROOT.gStyle.SetOptTitle(0)

# ROOT.gStyle.SetTitleH(0) # Set the height of the title box
# ROOT.gStyle.SetTitleW(0) # Set the width of the title box
#ROOT.gStyle.SetTitleX(0.35) # Set the position of the title box
#ROOT.gStyle.SetTitleY(0.986) # Set the position of the title box
# ROOT.gStyle.SetTitleStyle(Style_t style = 1001)
#ROOT.gStyle.SetTitleBorderSize(0)

# For the axis titles:
ROOT.gStyle.SetTitleColor(1, "XYZ")
ROOT.gStyle.SetTitleFont(43, "XYZ")
ROOT.gStyle.SetTitleSize(33*cvscale*fontScale, "XYZ")
# ROOT.gStyle.SetTitleXSize(Float_t size = 0.02) # Another way to set the size?
# ROOT.gStyle.SetTitleYSize(Float_t size = 0.02)
ROOT.gStyle.SetTitleXOffset(1.2)
#ROOT.gStyle.SetTitleYOffset(1.2)
ROOT.gStyle.SetTitleOffset(1.2, "YZ") # Another way to set the Offset

# For the axis labels:

ROOT.gStyle.SetLabelColor(1, "XYZ")
ROOT.gStyle.SetLabelFont(43, "XYZ")
ROOT.gStyle.SetLabelOffset(0.0077, "XYZ")
ROOT.gStyle.SetLabelSize(30*cvscale*fontScale, "XYZ")
#ROOT.gStyle.SetLabelSize(0.04, "XYZ")

# For the axis:

ROOT.gStyle.SetAxisColor(1, "XYZ")
ROOT.gStyle.SetAxisColor(1, "XYZ")
ROOT.gStyle.SetStripDecimals(True)
ROOT.gStyle.SetTickLength(0.03, "Y")
ROOT.gStyle.SetTickLength(0.05, "X")
ROOT.gStyle.SetNdivisions(1005, "X")
ROOT.gStyle.SetNdivisions(506, "Y")

ROOT.gStyle.SetPadTickX(1)  # To get tick marks on the opposite side of the frame
ROOT.gStyle.SetPadTickY(1)

# Change for log plots:
ROOT.gStyle.SetOptLogx(0)
ROOT.gStyle.SetOptLogy(0)
ROOT.gStyle.SetOptLogz(0)

#ROOT.gStyle.SetPalette(1) #(1,0)

# another top group addition

# Postscript options:
#ROOT.gStyle.SetPaperSize(20., 20.)
#ROOT.gStyle.SetPaperSize(ROOT.TStyle.kA4)
#ROOT.gStyle.SetPaperSize(27., 29.7)
#ROOT.gStyle.SetPaperSize(27., 29.7)
ROOT.gStyle.SetPaperSize(8.5*1.4*cvscale,7.0*1.4*cvscale)
ROOT.TGaxis.SetMaxDigits(3)
ROOT.gStyle.SetLineScalePS(2)

# ROOT.gStyle.SetLineStyleString(Int_t i, const char* text)
# ROOT.gStyle.SetHeaderPS(const char* header)
# ROOT.gStyle.SetTitlePS(const char* pstitle)
#ROOT.gStyle.SetColorModelPS(1)

# ROOT.gStyle.SetBarOffset(Float_t baroff = 0.5)
# ROOT.gStyle.SetBarWidth(Float_t barwidth = 0.5)
# ROOT.gStyle.SetPaintTextFormat(const char* format = "g")
# ROOT.gStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0)
# ROOT.gStyle.SetTimeOffset(Double_t toffset)
# ROOT.gStyle.SetHistMinimumZero(kTRUE)

ROOT.gStyle.SetPaintTextFormat("3.0f")

NRGBs = 5;
NCont = 255;

stops = numpy.array( [0.00, 0.34, 0.61, 0.84, 1.00] )
red  = numpy.array( [0.00, 0.00, 0.87, 1.00, 0.51] )
green = numpy.array( [0.00, 0.81, 1.00, 0.20, 0.00] )
blue = numpy.array( [0.51, 1.00, 0.12, 0.00, 0.00] )

colWheelDark = ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)

for i in range(NRGBs):
    red[i]=min(1,red[i]*1.1+0.25)
    green[i]=min(1,green[i]*1.1+0.25)
    blue[i]=min(1,blue[i]*1.1+0.25)

colWheel = ROOT.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
ROOT.gStyle.SetNumberContours(NCont)
ROOT.gRandom.SetSeed(123)

colors=[]
def hex2rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16)/255.0 for i in range(0, lv, lv // 3))

def newColor(red,green,blue):
    newColor.colorindex+=1
    color=ROOT.TColor(newColor.colorindex,red,green,blue)
    colors.append(color)
    return color
    
newColor.colorindex=301

def getDarkerColor(color):
    darkerColor=newColor(color.GetRed()*0.6,color.GetGreen()*0.6,color.GetBlue()*0.6)
    return darkerColor


fileList = []

filePath = "/vols/cms/mkomm/LLP/NANOX_180525-v1_llp"

xsecs = {

    # Drell-Yan + jets
    # NLO
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z
    "DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:147.40",
    "DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:40.99 ",
    "DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:5.678",
    "DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:1.367",
    "DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:0.6304",
    "DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:0.1514",
    "DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:0.003565 ",
    # "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8":18610,
    # "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8":1921.8*3,
    
    # QCD (multijet)
    # LO
    "QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:27990000",
    "QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:1712000",
    "QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:347700",
    "QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:32100",
    "QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:6831",
    "QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:1207",
    "QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:119.9",
    "QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8:25.24",
    '''
    #https://cms-pdmv.cern.ch/mcm/requests?page=-1&dataset_name=QCD_Pt_*to*_TuneCUETP8M1_13TeV_pythia8&member_of_campaign=RunIIFall14GS
    "QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8":140932000,
    "QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8":19204300,
    "QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8":2762530,
    "QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8":471100,
    "QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8":117276,
    "QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8":7823,
    "QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8":648.2,
    "QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8":186.9,
    "QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8":32.293,
    "QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8":9.4183,
    "QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8":0.84265,
    "QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8":0.114943,
    "QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8":0.00682981,
    "QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8":0.000165445,
    '''
    
    # T1 qqqq LL gluino pair production and decay
    # https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVgluglu
    # Here 1 TeV cross sections are used
    "SMS-T1qqqq_ctau-0p001_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-0p01_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    "SMS-T1qqqq_ctau-100000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8":0.325388,
    
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
    "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-evtgen": 831.76,
    "TTJets_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8": 0, 
    "TTJets_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8: 0,
    "TTJets_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8: 0,
    "TTJets_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8: 0,
    "TTJets_SingleLeptFromTbar_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8: 0,
    "TTJets_SingleLeptFromT_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8: 0,

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
    # "WToLNu_0J_13TeV-amcatnloFXFX-pythia8": 49670.,
    # "WToLNu_1J_13TeV-amcatnloFXFX-pythia8": 8264.,
    # "WToLNu_2J_13TeV-amcatnloFXFX-pythia8": 3226.,
    
    # Z -> nu nu + jets
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns
    # LO
    "ZJetsToNuNu_HT-100To200_13TeV-madgraph": 280.35*1.23 ,
    "ZJetsToNuNu_HT-200To400_13TeV-madgraph": 77.67*1.23 ,
    "ZJetsToNuNu_HT-400To600_13TeV-madgraph": 10.73*1.23 ,
    "ZJetsToNuNu_HT-600To800_13TeV-madgraph": 2.559*1.23 ,
    "ZJetsToNuNu_HT-800To1200_13TeV-madgraph": 1.1796*1.23 ,
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

with open('eventyields.json',) as f:
    genweights = json.load(f)

processDict = {}

for processFolder in os.listdir(filePath):
    print "reading ",processFolder,"...",
    for f in os.listdir(os.path.join(filePath,processFolder)):
        fullFilePath = os.path.join(filePath,processFolder,f)
        '''
        if not f.endswith(".root"):
            continue
        
        rootFile = ROOT.TFile(fullFilePath)
        if not rootFile:
            continue
        tree = rootFile.Get("Friends")
        if not tree:
            continue
        '''
        if not processDict.has_key(processFolder):
            processDict[processFolder] = {
                "files":[],
                "weight":"1",
                "nevents":0,
                "integral":0
            }
        
        processDict[processFolder]["files"].append(fullFilePath)
        '''
        if tree.FindBranch("genweight"):
            h = ROOT.TH1F("nevents"+processFolder+f,"",1,-1,1)
            tree.Project(h.GetName(),"0","genweight")
            processDict[processFolder]["nevents"]+=tree.GetEntries()
            processDict[processFolder]["integral"]+=h.Integral()
        else:
            processDict[processFolder]["nevents"]+=tree.GetEntries()
            processDict[processFolder]["integral"]+=tree.GetEntries()
        rootFile.Close()
        #break
        '''
    if processDict.has_key(processFolder):
        #if xsecs.has_key(processFolder) and genweights.has_key(processFolder):
        if xsecs.has_key(processFolder):
            print genweights[processFolder],
            processDict[processFolder]["weight"] = "("+str(1.*xsecs[processFolder]/genweights[processFolder])+")"
            
            #print processDict[processFolder]["nevents"],processDict[processFolder]["integral"],
            #processDict[processFolder]["weight"] = "("+str(1.*xsecs[processFolder]/processDict[processFolder]["integral"])+")"

            
            print processDict[processFolder]["weight"]
        else: 
            print processDict[processFolder]["nevents"]
    else:
        print "skip!"
        
globalWeight = "(trigger==1)*(nLooseMuons==0)*(nLooseElectrons==0)"
globalMCWeight = globalWeight+"*(trigger==1)*(genweight)*35.822*1000.0*(puweight*muon_track_weight*muon_trigger_weight*muon_id_weight*muon_iso_weight)"
globalDataWeight = globalWeight


mcSetDict = {
    "diboson": {
        "processes": [
            "WW_TuneCUETP8M1_13TeV-pythia8",
            "WZ_TuneCUETP8M1_13TeV-pythia8",
            "ZZ_TuneCUETP8M1_13TeV-pythia8"
        ],
        "weight":globalMCWeight,
        "fill":newColor(0.3,0.75,0.95),
        "title":"Diboson",
        "addtitle":""
    },
    "WJets": {
        "processes": [
            "WToLNu_0J_13TeV-amcatnloFXFX-pythia8",
            "WToLNu_1J_13TeV-amcatnloFXFX-pythia8",
            "WToLNu_2J_13TeV-amcatnloFXFX-pythia8"
        ],
        "weight":globalMCWeight,
        "fill":newColor(0.33,0.75,0.35),
        "title":"W+jets",
        "addtitle":""
    },
    "ZJets": {
        "processes": [
            "DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8",
            "DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8"
        ],
        "weight":globalMCWeight,
        "fill":newColor(0.35,0.95,0.55),
        "title":"Z/#gamma*+jets",
        "addtitle":""
    },
    "ttbar": {
        "processes": [
            "TT_TuneCUETP8M2T4_13TeV-powheg-pythia8-evtgen",
        ],
        "weight":globalMCWeight,
        "fill":newColor(1.,0.8,0.0),
        "title":"t#bar{t}",
        "addtitle":""
    },
    "st":{
        "processes": [
            "ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1",
            "ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1",
            "ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1",
            "ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1",
            "ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1"
        ],
        "weight":globalMCWeight,
        "fill":newColor(0.6,0.47,0.97),
        "title":"Single t/#bar{t}",
        "addtitle":""
    },
    "QCD": {
        "processes": [
            "QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8",
            "QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8",
            #"QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8",
            #"QCD_Pt_1400to1800_TuneCUETP8M1_13TeV_pythia8",
            #"QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8",
            #"QCD_Pt_2400to3200_TuneCUETP8M1_13TeV_pythia8",
            #"QCD_Pt_3200toInf_TuneCUETP8M1_13TeV_pythia8",
        ],
        "weight":globalMCWeight,
        "fill":newColor(0.85,0.85,0.85),
        "title":"Multijet",
        "addtitle":""
    },
}

for processSet in mcSetDict.keys():
    mcSetDict[processSet]["line"] = getDarkerColor(mcSetDict[processSet]["fill"])

dataSetDict = {
    "SingleMuon":{
        "processes": [
            "SingleMuon_Run2016B-03Feb2017_ver2-v2",
            "SingleMuon_Run2016C-03Feb2017-v1",
            "SingleMuon_Run2016D-03Feb2017-v1",
            "SingleMuon_Run2016E-03Feb2017-v1",
            "SingleMuon_Run2016F-03Feb2017-v1",
            "SingleMuon_Run2016G-03Feb2017-v1",
            "SingleMuon_Run2016H-03Feb2017_ver2-v1",
            "SingleMuon_Run2016H-03Feb2017_ver3-v1"
        ],
        "weight":globalDataWeight
    }
}

def addOverUnderflow(hist):
    u = hist.GetBinContent(0)
    uerr = hist.GetBinError(0)
    
    b1 = hist.GetBinContent(1)
    b1err = hist.GetBinError(1)
    
    hist.SetBinContent(1,u+b1)
    hist.SetBinError(1,math.sqrt(uerr**2+b1err**2))
    
    o = hist.GetBinContent(hist.GetNbinsX()+1)
    oerr = hist.GetBinError(hist.GetNbinsX()+1)
    
    bN = hist.GetBinContent(hist.GetNbinsX())
    bNerr = hist.GetBinError(hist.GetNbinsX())
    
    hist.SetBinContent(1,o+bN)
    hist.SetBinError(1,math.sqrt(oerr**2+bNerr**2))
    
    hist.SetEntries(hist.GetEntries()-2)

class Variable:
    def __init__(self,name,varexpr,title,start,end,
        unit="",
        mcSetList=["WJets","ZJets","st","ttbar","QCD"],
        dataSetList=["SingleMuon"],
        nbins=50,
        logx=False,
        logy=False,
        extraWeight="1",
        cutMC="1",
        cutData="1"
    ):
        self.name = name
        self.varexpr = varexpr
        self.title = title
        self.mcSetList = mcSetList
        self.dataSetList = dataSetList
        self.logx = logx
        self.logy = logy
        self.extraWeight = extraWeight
        self.cutMC = cutMC
        self.cutData = cutData
    
        if self.logx:
            self.binning = numpy.logspace(math.log10(start),math.log10(end),num=nbins+1)
        else:
            self.binning = numpy.linspace(start,end,num=nbins+1)
            
        if unit!="":
            self.xaxisTitle = title+" ("+unit+")"
            if self.logx:
                self.yaxisTitle = "Events / bins"
            else:
                binwidth = 1.*(end-start)/nbins
                binexp = math.floor(math.log10(binwidth))
                if binexp>3 or binexp<-3:
                    self.yaxisTitle = "Events / %4.3f#upoint 10#scale[0.7]{#lower[-0.7]{%i}} %s"%(binwidth/(10**binexp),binexp,unit)
                elif binexp>1:
                    self.yaxisTitle = "Events / %3f %s"%(binwidth,unit)
                else:
                    self.yaxisTitle = "Events / %4.2f %s"%(binwidth,unit)
        else:
            self.xaxisTitle = title
            if self.logx:
                self.yaxisTitle = "Events / bins"
            else:
                self.yaxisTitle = "Events / bins"
 
metSymbol = "E#kern[-0.53]{#lower[0.1]{#scale[1.2]{#/}}}#kern[-0.5]{#lower[0.3]{#scale[0.7]{T}}}"
 
variables = [
    #Variable("t","8*((IsoMu24==1))+4*IsoTkMu24+2*Mu24_eta2p1+TkMu24_eta2p1","t",-0.5,16.5,nbins=17,logy=True),
    #Variable("x","trigger*40+(nTightMuons>0)*20+0.05*muon1_pt","trigger*20+#jets",-0.5,80.5,nbins=81,logy=True),
    #Variable("nTightMuons","nTightMuons","#tight muons",-0.5,12.5,nbins=13,logy=True),
    Variable("met","met",metSymbol,10,1000,unit="GeV",logx=True,logy=False),

    Variable("nJets_all","nSelectedJets_all","#jets",-0.5,14.5,nbins=15,logy=True),
    
    #Variable("alphaT_all","alphaT_all","#alpha#lower[0.3]{#scale[0.7]{T}}",0.1,10,logy=True,logx=True),
    #Variable("alphaTL_all","alphaTL_all","#alpha#lower[0.3]{#scale[0.7]{T}}",0.1,10,logy=True,logx=True),
    Variable("muon_pt","muon1_pt","Muon p#lower[0.3]{#scale[0.7]{T}}",20,350,unit="GeV",logx=True),
    Variable("muon_eta","muon1_eta","Muon #eta",-2.5,2.5),
    Variable("ht_central","ht_central","central H#lower[0.3]{#scale[0.7]{T}}",30,2000,unit="GeV",logx=True),
    Variable("mht_all","mht_all","H#lower[0.3]{#scale[0.7]{T}}#kern[-2.2]{ }#lower[-0.8]{#scale[0.7]{miss}}",50,1000,unit="GeV",logx=True),

    Variable("nJets_central","nSelectedJets_central","#central jets",-0.5,12.5,nbins=13,logy=True),
    
    #Variable("C_all","C_all","Event shape C",0,1),
    #Variable("D_all","D_all","Event shape D",0,1,logy=True),
    
    Variable("minPhi_all","minPhi_all","Min #Delta#phi(jet-H#lower[0.3]{#scale[0.7]{T}}#kern[-2.2]{ }#lower[-0.7]{#scale[0.7]{miss}},"+metSymbol+")",0,3.2,logy=True),
    Variable("minPhiL_all","minPhiL_all","Min #Delta#phi(jet/#mu-H#lower[0.3]{#scale[0.7]{T}}#kern[-2.2]{ }#lower[-0.7]{#scale[0.7]{miss}},"+metSymbol+")",0,3.2,logy=True),
    
    Variable("jet1_pt_central","jet1_pt_central","Leading central jet p#lower[0.3]{#scale[0.7]{T}}",30,1000,unit="GeV",logx=True),
    Variable("jet1_eta_central","jet1_eta_central","Leading central jet #eta",-2.5,2.5),
    
    Variable("jet1_pt_all","jet1_pt_all","Leading jet p#lower[0.3]{#scale[0.7]{T}}",30,1000,unit="GeV",logx=True),
    Variable("jet1_eta_all","jet1_eta_all","Leading jet #eta",-5.,5.),
    
    Variable("jet1_ncpf","jet1_ncpf_central","Leading jet #charged PF",-0.5,30.5,nbins=31),
    Variable("jet1_nnpf","jet1_nnpf_central","Leading jet #neutral PF",-0.5,30.5,nbins=31),
    Variable("jet1_nsv","jet1_nsv_central","Leading jet #SV",-0.5,5.5,nbins=6),
    
    Variable("jet1_isB_deltactau","jet1_isB_ctau0p001-jet1_isB_ctau1000","Leading jet #Delta prob(B|#Delta c#kern[-1.5]{ }#tau(1#mum,1m))",-0.2,0.2,logy=True),
    
    Variable("jet1_isB_ctau1","jet1_isB_ctau1","Leading jet prob(B|c#kern[-1.5]{ }#tau=1mm)",0,1,logy=True),
    Variable("jet1_fromLLP_ctau1","jet1_fromLLP_ctau1","Leading jet prob(LLP|c#kern[-1.5]{ }#tau=1mm)",0,1,logy=True),
    
    Variable("jet1_isB_ctau1000","jet1_isB_ctau1000","Leading jet prob(B|c#kern[-1.5]{ }#tau=1m)",0,1,logy=True),
    Variable("jet1_fromLLP_ctau1000","jet1_fromLLP_ctau1000","Leading jet prob(LLP|c#kern[-1.5]{ }#tau=1m)",0,1,logy=True),
    
    Variable("jet1_isB_ctau0p001","jet1_isB_ctau0p001","Leading jet prob(B|c#kern[-1.5]{ }#tau=1#mum)",0,1,logy=True),
    Variable("jet1_fromLLP_ctau0p001","jet1_fromLLP_ctau0p001","Leading jet prob(LLP|c#kern[-1.5]{ }#tau=1#mum)",0,1,logy=True),
    
    
    Variable("max_isB_ctau1","max_isB_ctau1","Max prob(B|c#kern[-1.5]{ }#tau=1mm)",0,1,logy=True),
    Variable("max_fromLLP_ctau1","max_fromLLP_ctau1","Max prob(LLP|c#kern[-1.5]{ }#tau=1mm)",0,1,logy=True),
    
    Variable("max_isB_ctau1000","max_isB_ctau1000","Max prob(B|c#kern[-1.5]{ }#tau=1m)",0,1,logy=True),
    Variable("max_fromLLP_ctau1000","max_fromLLP_ctau1000","Max prob(LLP|c#kern[-1.5]{ }#tau=1m)",0,1,logy=True),
    
    Variable("max_isB_ctau0p001","max_isB_ctau0p001","Max prob(B|c#kern[-1.5]{ }#tau=1#mum)",0,1,logy=True),
    Variable("max_fromLLP_ctau0p001","max_fromLLP_ctau0p001","Max prob(LLP|c#kern[-1.5]{ }#tau=1#mum)",0,1,logy=True),
    
    #Variable("max_llp1_central","max_llp1_central","Max prob(LLP|central jet)",0,1,logy=True),
    #Variable("max_llp1_central_blind","max_llp1_central","Max prob(LLP|central jet)",0,1,cutData="(max_llp1_central<0.5)",logy=True),
    #Variable("max_b1_central","max_b1_central","Max prob(b|central jet)",0,1,logy=True),
    #Variable("max_deepCSV1_central","max_deepCSV1_central","Max deepCSV central jet",0,1,logy=True),
    
    #Variable("max_llp2_central","max_llp2_central","2nd max prob(LLP|central jet)",0,1,logy=True),
    #Variable("max_b2_central","max_b2_central","2nd max prob(b|central jet)",0,1,logy=True),
    #Variable("max_deepCSV2_central","max_deepCSV2_central","2nd max deepCSV central jet",0,1,logy=True),
    
    #Variable("nLooseLLP","nlooseLLP","#loose LLP jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nMediumLLP","nmediumLLP","#medium LLP jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nTightLLP","ntightLLP","#tight LLP jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nUltraLLP","nultraLLP","#ultra LLP jets",-0.5,8.5,nbins=9,logy=True),
    
    #Variable("nLooseDeepCSV","nlooseDeepCSV","#loose deepCSV b jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nMediumDeepCSV","nmediumDeepCSV","#medium deepCSV b jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nTightDeepCSV","ntightDeepCSV","#tight deepCSV b jets",-0.5,8.5,nbins=9,logy=True),
    
    #Variable("nLooseB","nlooseB","#loose b jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nMediumB","nmediumB","#medium b jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nTightB","ntightB","#tight b jets",-0.5,8.5,nbins=9,logy=True),
    #Variable("nUltraB","nultraB","#ultra b jets",-0.5,8.5,nbins=9,logy=True),
    
    Variable("dimuon_mass","dimuon_mass","Dimuon mass",10,510,unit="GeV",logy=True),
]

for category in [
    #["none","1",""],
    #["1mu_3j","(nTightMuons==1)*(nSelectedJets_all==3)","1#kern[-0.5]{ }#mu, 3#kern[-0.5]{ }jets"],
    ["1mu_3toNj_","(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],
    #["2mu_3toNj","(nTightMuons==2)*(nSelectedJets_all>2)*(dimuon_mass>10.)","2#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"]
    
    #["IsoMu_1mu_3toNj_","(IsoMu24==1)*(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],
    #["IsoTkMu_1mu_3toNj_","(IsoTkMu24==1)*(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],
    #["IsoXMu_1mu_3toNj_","((IsoMu24==1)||(IsoTkMu24==1))*(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],

    #["Mu_1mu_3toNj_","(Mu24_eta2p1==1)*(fabs(muon1_eta)<2.1)*(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],
    #["TkMu_1mu_3toNj_","(TkMu24_eta2p1==1)*(fabs(muon1_eta)<2.1)*(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],
    #["XMu_1mu_3toNj_","((Mu24_eta2p1==1)||(TkMu24_eta2p1==1))*(fabs(muon1_eta)<2.1)*(nTightMuons==1)*(nSelectedJets_all>2)","1#kern[-0.5]{ }#mu, #geq#kern[-0.5]{ }3#kern[-0.5]{ }jets"],

]:
    for cut in [
        #["none","1",""],
        ["150met","(met>150.)",metSymbol+"#kern[-0.7]{ }>#kern[-0.7]{ }150#kern[-0.5]{ }GeV"],
        ["150met_llp05","(met>150.)*(jet1_fromLLP_ctau1>0.5)",metSymbol+"#kern[-0.7]{ }>#kern[-0.7]{ }150#kern[-0.5]{ }GeV, prob(LLP)>0.5"],
        #["150met_puId","(met>150.)*(jet_minpuId_central>0)",metSymbol+"#kern[-0.7]{ }>#kern[-0.7]{ }150#kern[-0.5]{ }GeV, loose PU ID"],
        #["150met_puId","(met>150.)*(jet_minpuId_central>0)",metSymbol+"#kern[-0.7]{ }>#kern[-0.7]{ }150#kern[-0.5]{ }GeV, loose PU ID"],
        #["alphaT","(alphaT_all>0.5)","#alpha#lower[0.3]{#scale[0.7]{T}}>0.5"],
        #["minPhi","(minPhi_all>0.2)","Min #Delta#phi(jet-H#lower[0.3]{#scale[0.7]{T}}#kern[-2.2]{ }#lower[-0.7]{#scale[0.7]{miss}},"+metSymbol+")>0.2"],
    ]:
        for variable in variables:
            print category[0],variable.name,cut[0],
            
            outputName = "plots_v2/"+category[0]+"_"+variable.name+"_"+cut[0]
            
            if os.path.exists(outputName+".pdf"):
                print " -> skip"
                continue
            
            print
            
            stackMC = ROOT.THStack()
            stackMCHists=[]
            
            legendEntries=[]
            
            totalMC = 0.0
            totalMCError2 = 0.0
            
            sumHistMC = ROOT.TH1F("mcsum_"+category[0]+"_"+variable.name+"_"+str(random.randint(0,99999)),"",len(variable.binning)-1,variable.binning)
            sumHistMC.SetDirectory(0)
            sumHistMC.Sumw2()
            for processName in variable.mcSetList:
                print processName
                setHist = ROOT.TH1F("mc_"+category[0]+"_"+variable.name+"_"+processName+"_"+str(random.randint(0,99999)),"",len(variable.binning)-1,variable.binning)
                setHist.SetDirectory(0)
                setHist.Sumw2()
                setHist.SetFillColor(mcSetDict[processName]["fill"].GetNumber())
                setHist.SetLineColor(mcSetDict[processName]["line"].GetNumber())
                setHist.SetLineWidth(2)
                setHist.SetFillStyle(1001)
                
                for process in mcSetDict[processName]["processes"]:
                    #print process
                    #print " -> files=",len(processDict[process]["files"])
                    weight = variable.extraWeight+"*"+variable.cutMC+"*"+mcSetDict[processName]["weight"]+"*"+category[1]+"*"+cut[1]
                    #print " -> weight=",weight
                    for f in processDict[process]["files"]:
                        rootFile = ROOT.TFile.Open(f)
                        tree = rootFile.Get("Friends")
                        if tree:
                            processHist = ROOT.TH1F("mc_"+category[0]+"_"+variable.name+"_"+processName+"_"+process+"_"+str(random.randint(0,99999)),"",len(variable.binning)-1,variable.binning)
                            processHist.Sumw2()
                            tree.Project(processHist.GetName(),variable.varexpr,weight+"*"+processDict[process]["weight"])
                            processHist.SetDirectory(0)
                            setHist.Add(processHist)
                        rootFile.Close()
                print " -> entries=",setHist.GetEntries(),"/",setHist.Integral()
                    
                #addOverUnderflow(setHist)
                stackMC.Add(setHist,"HIST")
                sumHistMC.Add(setHist)
                if len(mcSetDict[processName]["addtitle"])>0:
                    legendEntries.append(["",mcSetDict[processName]["addtitle"],""])
                legendEntries.append([setHist,mcSetDict[processName]["title"],"F"])
                
            
                
            sumHistData = ROOT.TH1F("datasum_"+category[0]+"_"+variable.name+"_"+str(random.randint(0,99999)),"",len(variable.binning)-1,variable.binning)
            sumHistData.SetDirectory(0)
            sumHistData.SetMarkerStyle(20)
            sumHistData.SetMarkerSize(1.3)
            sumHistData.Sumw2()
            for processName in variable.dataSetList:
                for process in dataSetDict[processName]["processes"]:
                    print process
                    #print " -> files=",len(processDict[process]["files"])
                    weight = variable.extraWeight+"*"+variable.cutData+"*"+dataSetDict[processName]["weight"]+"*"+processDict[process]["weight"]+"*"+category[1]+"*"+cut[1]
                    #print " -> weight=",weight
                    entires = 0.
                    integral = 0.
                    for f in processDict[process]["files"]:
                        rootFile = ROOT.TFile(f)
                        tree = rootFile.Get("Friends")
                        if tree:
                            processHist = ROOT.TH1F("data_"+category[0]+"_"+variable.name+"_"+processName+"_"+process+"_"+str(random.randint(0,99999)),"",len(variable.binning)-1,variable.binning)
                            processHist.Sumw2()
                            tree.Project(processHist.GetName(),variable.varexpr,weight)
                            entires+=processHist.GetEntries()
                            integral+=processHist.Integral()
                            sumHistData.Add(processHist)
                        rootFile.Close()
                    print  " -> entries =",entires,"/",integral
                    
                    
            #addOverUnderflow(sumHistData)
            
            print "Total MC",sumHistMC.GetEntries(),sumHistMC.Integral()
            print "Total data",sumHistData.GetEntries(),sumHistData.Integral()
            
           
            cv = ROOT.TCanvas("cv_"+category[0]+"_"+variable.name+str(random.randint(0,99999)),"",850,700)
            cv.Divide(1,2,0,0)
            cv.GetPad(1).SetPad(0.0, 0.0, 1.0, 1.0)
            cv.GetPad(1).SetFillStyle(4000)
            cv.GetPad(2).SetPad(0.0, 0.00, 1.0,1.0)
            cv.GetPad(2).SetFillStyle(4000)
            
            cvxmin=0.13
            cvxmax=0.77
            cvymin=0.145
            cvymax=0.92
            resHeight=0.35
            
            for i in range(1,3):
                #for the canvas:
                cv.GetPad(i).SetBorderMode(0)
                cv.GetPad(i).SetGridx(False)
                cv.GetPad(i).SetGridy(False)


                #For the frame:
                cv.GetPad(i).SetFrameBorderMode(0)
                cv.GetPad(i).SetFrameBorderSize(1)
                cv.GetPad(i).SetFrameFillColor(0)
                cv.GetPad(i).SetFrameFillStyle(0)
                cv.GetPad(i).SetFrameLineColor(1)
                cv.GetPad(i).SetFrameLineStyle(1)
                cv.GetPad(i).SetFrameLineWidth(int(1*cvscale))

                # Margins:
                cv.GetPad(i).SetLeftMargin(cvxmin)
                cv.GetPad(i).SetRightMargin(1-cvxmax)
                
                # For the Global title:
                cv.GetPad(i).SetTitle("")
                
                # For the axis:
                cv.GetPad(i).SetTickx(1)  # To get tick marks on the opposite side of the frame
                cv.GetPad(i).SetTicky(1)

                # Change for log plots:
                cv.GetPad(i).SetLogx(0)
                cv.GetPad(i).SetLogy(0)
                cv.GetPad(i).SetLogz(0)
            
            cv.GetPad(2).SetTopMargin(1-cvymax)
            cv.GetPad(2).SetBottomMargin(resHeight)
            cv.GetPad(1).SetTopMargin(1-resHeight)
            cv.GetPad(1).SetBottomMargin(cvymin)
            
            cv.cd(2)

            ymax = max([sumHistMC.GetMaximum(),sumHistData.GetMaximum()])
                    
            if variable.logy:
                axis=ROOT.TH2F(
                    "axis"+str(random.randint(0,99999)),";;"+variable.yaxisTitle,
                    50,variable.binning[0],variable.binning[-1],
                    50,0.7,math.exp(1.43*math.log(max([ymax,1.0])))
                )
            else:
                axis=ROOT.TH2F(
                    "axis"+str(random.randint(0,99999)),";;"+variable.yaxisTitle,
                    50,variable.binning[0],variable.binning[-1],
                    50,0.0,1.43*max([ymax,1.0])
                )

            axis.GetXaxis().SetLabelSize(0)
            axis.GetXaxis().SetTitle("")
            axis.GetXaxis().SetTickLength(0.015/(1-cv.GetPad(2).GetLeftMargin()-cv.GetPad(2).GetRightMargin()))
            axis.GetYaxis().SetTickLength(0.015/(1-cv.GetPad(2).GetTopMargin()-cv.GetPad(2).GetBottomMargin()))
            #axis.GetYaxis().SetNoExponent(True)
            axis.Draw("AXIS")
            
            stackMC.Draw("HISTSame")
            sumHistData.Draw("PESame")
            legendEntries.append([sumHistData,"Data","P"])
            
            if variable.logy:
                cv.GetPad(2).SetLogy(1)
            if variable.logx:
                cv.GetPad(2).SetLogx(1)
                cv.GetPad(1).SetLogx(1)
            ROOT.gStyle.SetLineWidth(int(1*cvscale))
            ROOT.gPad.RedrawAxis()
            
            legend = ROOT.TLegend(cvxmax+0.015,cvymax,0.99,cvymax-0.08*len(legendEntries))
            legend.SetFillColor(ROOT.kWhite)
            legend.SetBorderSize(0)
            legend.SetTextFont(43)
            legend.SetTextSize(34*cvscale)
            
            for entry in reversed(legendEntries):
                legend.AddEntry(entry[0],entry[1],entry[2])
      
            pCMS=ROOT.TPaveText(cvxmin+0.025,cvymax-0.065,cvxmin+0.025,cvymax-0.065,"NDC")
            pCMS.SetFillColor(ROOT.kWhite)
            pCMS.SetBorderSize(0)
            pCMS.SetTextFont(63)
            pCMS.SetTextSize(32*cvscale)
            pCMS.SetTextAlign(11)
            pCMS.AddText("CMS")
            pCMS.Draw("Same")
            
            pPreliminary=ROOT.TPaveText(cvxmin+0.025+0.09,cvymax-0.065,cvxmin+0.025+0.09,cvymax-0.065,"NDC")
            pPreliminary.SetFillColor(ROOT.kWhite)
            pPreliminary.SetBorderSize(0)
            pPreliminary.SetTextFont(53)
            pPreliminary.SetTextSize(32*cvscale)
            pPreliminary.SetTextAlign(11)
            pPreliminary.AddText("Preliminary")
            pPreliminary.Draw("Same")
        
            
            pCut=ROOT.TPaveText(cvxmin+0.025,cvymax-0.06-0.07,cvxmin+0.025,cvymax-0.06-0.07,"NDC")
            pCut.SetFillStyle(0)
            pCut.SetBorderSize(0)
            pCut.SetTextFont(43)
            pCut.SetTextSize(32*cvscale)
            pCut.SetTextAlign(11)
            pCut.AddText(cut[2])
            pCut.Draw("Same")
            
            
            pLumi=ROOT.TPaveText(cvxmax,0.94,cvxmax,0.94,"NDC")
            pLumi.SetFillColor(ROOT.kWhite)
            pLumi.SetBorderSize(0)
            pLumi.SetTextFont(43)
            pLumi.SetTextSize(34)
            pLumi.SetTextAlign(31)
            pLumi.AddText(category[2]+", 36#kern[-0.5]{ }fb#lower[-0.7]{#scale[0.7]{-1}} (13TeV)")
            pLumi.Draw("Same")
            
           
            cv.cd(1)
            axisRes=ROOT.TH2F(
                "axisRes"+str(random.randint(0,99999)),";"+variable.xaxisTitle+";Data/MC",
                50,variable.binning[0],variable.binning[-1],50,0.1,1.9)
            axisRes.GetYaxis().SetNdivisions(406)
            axisRes.GetXaxis().SetTickLength(0.025/(1-cv.GetPad(1).GetLeftMargin()-cv.GetPad(1).GetRightMargin()))
            axisRes.GetYaxis().SetTickLength(0.015/(1-cv.GetPad(1).GetTopMargin()-cv.GetPad(1).GetBottomMargin()))

            axisRes.Draw("AXIS")
            
            rootObj=[]
            
            for ibin in range(sumHistData.GetNbinsX()):
                c = sumHistMC.GetBinCenter(ibin+1)
                w = sumHistMC.GetBinWidth(ibin+1)
                m = sumHistMC.GetBinContent(ibin+1)
                    
                if m>0.0:
                    h = min(sumHistMC.GetBinError(ibin+1)/m,0.399)
                    box = ROOT.TBox(c-0.5*w,1-h,c+0.5*w,1+h)
                    box.SetFillStyle(3345)
                    box.SetLineColor(ROOT.kGray+1)
                    box.SetFillColor(ROOT.kGray)
                    box.SetLineWidth(int(2*cvscale))
                    rootObj.append(box)
                    box.Draw("SameF")
                    box2 = ROOT.TBox(c-0.5*w,1-h,c+0.5*w,1+h)
                    box2.SetFillStyle(0)
                    box2.SetLineColor(ROOT.kGray+1)
                    box2.SetFillColor(ROOT.kGray)
                    box2.SetLineWidth(int(2*cvscale))
                    rootObj.append(box2)
                    box2.Draw("SameL")
            if len(rootObj)>0:
                legend.AddEntry(rootObj[0],"MC stat.","F")
                
                
                
            sumHistRes=sumHistData.Clone(sumHistData.GetName()+str(random.randint(0,99999)))
            rootObj.append(sumHistRes)
            for ibin in range(sumHistRes.GetNbinsX()):
                m = sumHistMC.GetBinContent(ibin+1)
                d = sumHistRes.GetBinContent(ibin+1)
                e = sumHistRes.GetBinError(ibin+1)
                if m>0.0:
                    sumHistRes.SetBinContent(ibin+1,d/m)
                    sumHistRes.SetBinError(ibin+1,e/m)
                else:
                    sumHistRes.SetBinContent(ibin+1,0.0)
                    sumHistRes.SetBinError(ibin+1,0)
            sumHistRes.Draw("PESame")
            
            axisLine = ROOT.TF1("axisLine"+str(random.randint(0,99999)),"1",variable.binning[0],variable.binning[-1])
            axisLine.SetLineColor(ROOT.kBlack)
            axisLine.SetLineWidth(int(1*cvscale))
            axisLine.Draw("SameL")
            ROOT.gStyle.SetLineWidth(int(1*cvscale))
            ROOT.gPad.RedrawAxis()
            

            hidePave=ROOT.TPaveText(cvxmin-0.06,resHeight-0.028,cvxmin-0.005,resHeight+0.028,"NDC")
            hidePave.SetFillColor(ROOT.kWhite)
            hidePave.SetFillStyle(1001)
            #hidePave.Draw("Same")
            
            cv.cd(2)
            legend.Draw("Same")
            
            cv.Update()
           
            cv.Print(outputName+".pdf")
            cv.Print(outputName+".png")     
            cv.Print(outputName+".C")
            
            cv.WaitPrimitive()
        
        
                
