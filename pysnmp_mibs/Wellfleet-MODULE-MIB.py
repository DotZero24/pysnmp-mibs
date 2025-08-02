_H='wfModuleSlot'
_G='wfHwModuleModule'
_F='wfHwModuleSlot'
_E='Wellfleet-MODULE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
wfHwModuleGroup,=mibBuilder.importSymbols('Wellfleet-COMMON-MIB','wfHwModuleGroup')
_WfHwModuleTable_Object=MibTable
wfHwModuleTable=_WfHwModuleTable_Object((1,3,6,1,4,1,18,3,1,4,1))
if mibBuilder.loadTexts:wfHwModuleTable.setStatus(_A)
_WfHwModuleEntry_Object=MibTableRow
wfHwModuleEntry=_WfHwModuleEntry_Object((1,3,6,1,4,1,18,3,1,4,1,1))
wfHwModuleEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:wfHwModuleEntry.setStatus(_A)
_WfHwModuleSlot_Type=Integer32
_WfHwModuleSlot_Object=MibTableColumn
wfHwModuleSlot=_WfHwModuleSlot_Object((1,3,6,1,4,1,18,3,1,4,1,1,1),_WfHwModuleSlot_Type())
wfHwModuleSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleSlot.setStatus(_A)
_WfHwModuleModule_Type=Integer32
_WfHwModuleModule_Object=MibTableColumn
wfHwModuleModule=_WfHwModuleModule_Object((1,3,6,1,4,1,18,3,1,4,1,1,2),_WfHwModuleModule_Type())
wfHwModuleModule.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleModule.setStatus(_A)
class _WfHwModuleModIdOpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(512,768,769,1280,1281,1408,1536,1537,1538,1540,1541,1542,1544,1545,1546,1584,1585,1586,1588,1589,1590,1592,1593,1594,1664,1792,1793,1800,1801,1808,1809,1825,1833,1856,1857,1864,1865,1872,1873,1889,1897,2048,2049,2176,2304,2560,2816,2944,3072,3073,3328,3329,3330,3584,8000,8160,8161,8320,8321,8500,8501,8704,8720,8728,8729,8736,8744,8752,8768,8776,8780,8784,8800,8808,8816,8832,8848,8864,8872,8873,8880,8890,8891,8896,8912,8928,8944,8960,8972,8976,16384,16640,16896,16897,16898,16899,17152,17153,17154,17155,17408,17664,17920,18176,18432,18688,18944,524288,524544)));namedValues=NamedValues(*(('spex',512),('spexhss',768),('spexhsd',769),('denm',1280),('denmhwf',1281),('iqe',1408),('dsnmnn',1536),('dsnmn1',1537),('dsnmn2',1538),('dsnm1n',1540),('dsnm11',1541),('dsnm12',1542),('dsnm2n',1544),('dsnm21',1545),('dsnm22',1546),('dsnmnnisdn',1584),('dsnmn1isdn',1585),('dsnmn2isdn',1586),('dsnm1nisdn',1588),('dsnm11isdn',1589),('dsnm12isdn',1590),('dsnm2nisdn',1592),('dsnm21isdn',1593),('dsnm22isdn',1594),('qsyncnm',1664),('mmfsdsas',1792),('mmfsddas',1793),('smfsdsas',1800),('smfsddas',1801),('mmscsas',1808),('mmscdas',1809),('smammbdas',1825),('mmasmbdas',1833),('mmfsdsashwf',1856),('mmfsddashwf',1857),('smfsdsashwf',1864),('smfsddashwf',1865),('mmscsashwf',1872),('mmscdashwf',1873),('smammbdashwf',1889),('mmasmbdashwf',1897),('dtnm',2048),('cam',2049),('iqtok',2176),('se100nm',2304),('asnqbri',2560),('mce1nm',2816),('dmct1nm',2944),('hwcompnm32',3072),('hwcompnm128',3073),('ahwcompnm32',3328),('ahwcompnm128',3329),('ahwcompnm256',3330),('shssinm',3584),('fbrmbdfen',8000),('ds1e1atm',8160),('ds3e3atm',8161),('pmcdsync',8320),('pmcqsync',8321),('fvoippmcc',8500),('fvoipt1e1pmc',8501),('arnmbstr',8704),('arnmbsen',8720),('arnmbsfetx',8728),('arnmbsfefx',8729),('arnssync',8736),('litembsfetx',8744),('arnv34',8752),('arndcsu',8768),('arnft1',8776),('arnfe1',8780),('arnisdns',8784),('arnisdnu',8800),('arnisdb',8808),('arnstkrg',8816),('arnsenet',8832),('arntsync',8848),('arnentsync',8864),('arne7sync',8872),('arn7sync',8873),('arntrtsync',8880),('arnvoice',8890),('arnvoicedsync',8891),('arnmbenx10',8896),('arnmbtrx10',8912),('arnpbenx10',8928),('arnpbtrx10',8944),('arnpbtenx10',8960),('arnpbe7sx10',8972),('arnpbttrx10',8976),('snm10t16',16384),('snm100t2',16640),('snmatmoc31mm',16896),('snmatmoc31dmm',16897),('snmatmoc31sm',16898),('snmatmoc31dsm',16899),('snmfddismm',17152),('snmfddisms',17153),('snmfddissm',17154),('snmfddisss',17155),('snm10f8',17408),('snm100f2',17664),('snm10t16p4',17920),('snm100t2p4',18176),('snm10t14100t1',18432),('snm100t16',18688),('snm10t14100f1',18944),('atm5000ah',524288),('atm5000bh',524544)))
_WfHwModuleModIdOpt_Type.__name__=_C
_WfHwModuleModIdOpt_Object=MibTableColumn
wfHwModuleModIdOpt=_WfHwModuleModIdOpt_Object((1,3,6,1,4,1,18,3,1,4,1,1,3),_WfHwModuleModIdOpt_Type())
wfHwModuleModIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleModIdOpt.setStatus(_A)
_WfHwModuleModRev_Type=OctetString
_WfHwModuleModRev_Object=MibTableColumn
wfHwModuleModRev=_WfHwModuleModRev_Object((1,3,6,1,4,1,18,3,1,4,1,1,4),_WfHwModuleModRev_Type())
wfHwModuleModRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleModRev.setStatus(_A)
_WfHwModuleModSerialNumber_Type=OctetString
_WfHwModuleModSerialNumber_Object=MibTableColumn
wfHwModuleModSerialNumber=_WfHwModuleModSerialNumber_Object((1,3,6,1,4,1,18,3,1,4,1,1,5),_WfHwModuleModSerialNumber_Type())
wfHwModuleModSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleModSerialNumber.setStatus(_A)
_WfHwModuleArtworkRev_Type=DisplayString
_WfHwModuleArtworkRev_Object=MibTableColumn
wfHwModuleArtworkRev=_WfHwModuleArtworkRev_Object((1,3,6,1,4,1,18,3,1,4,1,1,6),_WfHwModuleArtworkRev_Type())
wfHwModuleArtworkRev.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleArtworkRev.setStatus(_A)
_WfHwModuleMemorySize1_Type=Integer32
_WfHwModuleMemorySize1_Object=MibTableColumn
wfHwModuleMemorySize1=_WfHwModuleMemorySize1_Object((1,3,6,1,4,1,18,3,1,4,1,1,7),_WfHwModuleMemorySize1_Type())
wfHwModuleMemorySize1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleMemorySize1.setStatus(_A)
_WfHwModuleMemorySize2_Type=Integer32
_WfHwModuleMemorySize2_Object=MibTableColumn
wfHwModuleMemorySize2=_WfHwModuleMemorySize2_Object((1,3,6,1,4,1,18,3,1,4,1,1,8),_WfHwModuleMemorySize2_Type())
wfHwModuleMemorySize2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleMemorySize2.setStatus(_A)
_WfHwModuleDaughterBdIdOpt_Type=Integer32
_WfHwModuleDaughterBdIdOpt_Object=MibTableColumn
wfHwModuleDaughterBdIdOpt=_WfHwModuleDaughterBdIdOpt_Object((1,3,6,1,4,1,18,3,1,4,1,1,9),_WfHwModuleDaughterBdIdOpt_Type())
wfHwModuleDaughterBdIdOpt.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleDaughterBdIdOpt.setStatus(_A)
_WfHwModuleLEDStatus1_Type=Integer32
_WfHwModuleLEDStatus1_Object=MibTableColumn
wfHwModuleLEDStatus1=_WfHwModuleLEDStatus1_Object((1,3,6,1,4,1,18,3,1,4,1,1,10),_WfHwModuleLEDStatus1_Type())
wfHwModuleLEDStatus1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleLEDStatus1.setStatus(_A)
_WfHwModuleLEDState1_Type=Integer32
_WfHwModuleLEDState1_Object=MibTableColumn
wfHwModuleLEDState1=_WfHwModuleLEDState1_Object((1,3,6,1,4,1,18,3,1,4,1,1,11),_WfHwModuleLEDState1_Type())
wfHwModuleLEDState1.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleLEDState1.setStatus(_A)
_WfHwModuleLEDStatus2_Type=Integer32
_WfHwModuleLEDStatus2_Object=MibTableColumn
wfHwModuleLEDStatus2=_WfHwModuleLEDStatus2_Object((1,3,6,1,4,1,18,3,1,4,1,1,12),_WfHwModuleLEDStatus2_Type())
wfHwModuleLEDStatus2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleLEDStatus2.setStatus(_A)
_WfHwModuleLEDState2_Type=Integer32
_WfHwModuleLEDState2_Object=MibTableColumn
wfHwModuleLEDState2=_WfHwModuleLEDState2_Object((1,3,6,1,4,1,18,3,1,4,1,1,13),_WfHwModuleLEDState2_Type())
wfHwModuleLEDState2.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleLEDState2.setStatus(_A)
_WfHwModuleLEDStatus3_Type=Integer32
_WfHwModuleLEDStatus3_Object=MibTableColumn
wfHwModuleLEDStatus3=_WfHwModuleLEDStatus3_Object((1,3,6,1,4,1,18,3,1,4,1,1,14),_WfHwModuleLEDStatus3_Type())
wfHwModuleLEDStatus3.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleLEDStatus3.setStatus(_A)
_WfHwModuleLEDState3_Type=Integer32
_WfHwModuleLEDState3_Object=MibTableColumn
wfHwModuleLEDState3=_WfHwModuleLEDState3_Object((1,3,6,1,4,1,18,3,1,4,1,1,15),_WfHwModuleLEDState3_Type())
wfHwModuleLEDState3.setMaxAccess(_B)
if mibBuilder.loadTexts:wfHwModuleLEDState3.setStatus(_A)
_WfModuleTable_Object=MibTable
wfModuleTable=_WfModuleTable_Object((1,3,6,1,4,1,18,3,1,4,2))
if mibBuilder.loadTexts:wfModuleTable.setStatus(_A)
_WfModuleEntry_Object=MibTableRow
wfModuleEntry=_WfModuleEntry_Object((1,3,6,1,4,1,18,3,1,4,2,1))
wfModuleEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wfModuleEntry.setStatus(_A)
class _WfModuleDelete_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('created',1),('deleted',2)))
_WfModuleDelete_Type.__name__=_C
_WfModuleDelete_Object=MibTableColumn
wfModuleDelete=_WfModuleDelete_Object((1,3,6,1,4,1,18,3,1,4,2,1,1),_WfModuleDelete_Type())
wfModuleDelete.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleDelete.setStatus(_A)
_WfModuleSlot_Type=Integer32
_WfModuleSlot_Object=MibTableColumn
wfModuleSlot=_WfModuleSlot_Object((1,3,6,1,4,1,18,3,1,4,2,1,2),_WfModuleSlot_Type())
wfModuleSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:wfModuleSlot.setStatus(_A)
class _WfModuleTimerFrequency_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('timerdefault',1))
_WfModuleTimerFrequency_Type.__name__=_C
_WfModuleTimerFrequency_Object=MibTableColumn
wfModuleTimerFrequency=_WfModuleTimerFrequency_Object((1,3,6,1,4,1,18,3,1,4,2,1,3),_WfModuleTimerFrequency_Type())
wfModuleTimerFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleTimerFrequency.setStatus(_A)
class _WfModuleBufferBalance_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('txrx',1),('none',2),('rx',3),('tx',4)))
_WfModuleBufferBalance_Type.__name__=_C
_WfModuleBufferBalance_Object=MibTableColumn
wfModuleBufferBalance=_WfModuleBufferBalance_Object((1,3,6,1,4,1,18,3,1,4,2,1,4),_WfModuleBufferBalance_Type())
wfModuleBufferBalance.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleBufferBalance.setStatus(_A)
class _WfModuleFddiWeight_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleFddiWeight_Type.__name__=_C
_WfModuleFddiWeight_Object=MibTableColumn
wfModuleFddiWeight=_WfModuleFddiWeight_Object((1,3,6,1,4,1,18,3,1,4,2,1,5),_WfModuleFddiWeight_Type())
wfModuleFddiWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleFddiWeight.setStatus(_A)
class _WfModuleTokenRingWeight_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleTokenRingWeight_Type.__name__=_C
_WfModuleTokenRingWeight_Object=MibTableColumn
wfModuleTokenRingWeight=_WfModuleTokenRingWeight_Object((1,3,6,1,4,1,18,3,1,4,2,1,6),_WfModuleTokenRingWeight_Type())
wfModuleTokenRingWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleTokenRingWeight.setStatus(_A)
class _WfModuleCsmacdWeight_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleCsmacdWeight_Type.__name__=_C
_WfModuleCsmacdWeight_Object=MibTableColumn
wfModuleCsmacdWeight=_WfModuleCsmacdWeight_Object((1,3,6,1,4,1,18,3,1,4,2,1,7),_WfModuleCsmacdWeight_Type())
wfModuleCsmacdWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleCsmacdWeight.setStatus(_A)
class _WfModuleSyncWeight_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleSyncWeight_Type.__name__=_C
_WfModuleSyncWeight_Object=MibTableColumn
wfModuleSyncWeight=_WfModuleSyncWeight_Object((1,3,6,1,4,1,18,3,1,4,2,1,8),_WfModuleSyncWeight_Type())
wfModuleSyncWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleSyncWeight.setStatus(_A)
_WfModuleFreeBufferCredits_Type=Integer32
_WfModuleFreeBufferCredits_Object=MibTableColumn
wfModuleFreeBufferCredits=_WfModuleFreeBufferCredits_Object((1,3,6,1,4,1,18,3,1,4,2,1,9),_WfModuleFreeBufferCredits_Type())
wfModuleFreeBufferCredits.setMaxAccess(_B)
if mibBuilder.loadTexts:wfModuleFreeBufferCredits.setStatus(_A)
_WfModuleTotalBufferCredits_Type=Integer32
_WfModuleTotalBufferCredits_Object=MibTableColumn
wfModuleTotalBufferCredits=_WfModuleTotalBufferCredits_Object((1,3,6,1,4,1,18,3,1,4,2,1,10),_WfModuleTotalBufferCredits_Type())
wfModuleTotalBufferCredits.setMaxAccess(_B)
if mibBuilder.loadTexts:wfModuleTotalBufferCredits.setStatus(_A)
_WfModuleRestart_Type=Integer32
_WfModuleRestart_Object=MibTableColumn
wfModuleRestart=_WfModuleRestart_Object((1,3,6,1,4,1,18,3,1,4,2,1,11),_WfModuleRestart_Type())
wfModuleRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleRestart.setStatus(_A)
class _WfModuleCsmacd100Weight_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleCsmacd100Weight_Type.__name__=_C
_WfModuleCsmacd100Weight_Object=MibTableColumn
wfModuleCsmacd100Weight=_WfModuleCsmacd100Weight_Object((1,3,6,1,4,1,18,3,1,4,2,1,12),_WfModuleCsmacd100Weight_Type())
wfModuleCsmacd100Weight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleCsmacd100Weight.setStatus(_A)
class _WfModuleBisyncWeight_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleBisyncWeight_Type.__name__=_C
_WfModuleBisyncWeight_Object=MibTableColumn
wfModuleBisyncWeight=_WfModuleBisyncWeight_Object((1,3,6,1,4,1,18,3,1,4,2,1,13),_WfModuleBisyncWeight_Type())
wfModuleBisyncWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleBisyncWeight.setStatus(_A)
class _WfModuleHssiWeight_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WfModuleHssiWeight_Type.__name__=_C
_WfModuleHssiWeight_Object=MibTableColumn
wfModuleHssiWeight=_WfModuleHssiWeight_Object((1,3,6,1,4,1,18,3,1,4,2,1,14),_WfModuleHssiWeight_Type())
wfModuleHssiWeight.setMaxAccess(_D)
if mibBuilder.loadTexts:wfModuleHssiWeight.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wfHwModuleTable':wfHwModuleTable,'wfHwModuleEntry':wfHwModuleEntry,_F:wfHwModuleSlot,_G:wfHwModuleModule,'wfHwModuleModIdOpt':wfHwModuleModIdOpt,'wfHwModuleModRev':wfHwModuleModRev,'wfHwModuleModSerialNumber':wfHwModuleModSerialNumber,'wfHwModuleArtworkRev':wfHwModuleArtworkRev,'wfHwModuleMemorySize1':wfHwModuleMemorySize1,'wfHwModuleMemorySize2':wfHwModuleMemorySize2,'wfHwModuleDaughterBdIdOpt':wfHwModuleDaughterBdIdOpt,'wfHwModuleLEDStatus1':wfHwModuleLEDStatus1,'wfHwModuleLEDState1':wfHwModuleLEDState1,'wfHwModuleLEDStatus2':wfHwModuleLEDStatus2,'wfHwModuleLEDState2':wfHwModuleLEDState2,'wfHwModuleLEDStatus3':wfHwModuleLEDStatus3,'wfHwModuleLEDState3':wfHwModuleLEDState3,'wfModuleTable':wfModuleTable,'wfModuleEntry':wfModuleEntry,'wfModuleDelete':wfModuleDelete,_H:wfModuleSlot,'wfModuleTimerFrequency':wfModuleTimerFrequency,'wfModuleBufferBalance':wfModuleBufferBalance,'wfModuleFddiWeight':wfModuleFddiWeight,'wfModuleTokenRingWeight':wfModuleTokenRingWeight,'wfModuleCsmacdWeight':wfModuleCsmacdWeight,'wfModuleSyncWeight':wfModuleSyncWeight,'wfModuleFreeBufferCredits':wfModuleFreeBufferCredits,'wfModuleTotalBufferCredits':wfModuleTotalBufferCredits,'wfModuleRestart':wfModuleRestart,'wfModuleCsmacd100Weight':wfModuleCsmacd100Weight,'wfModuleBisyncWeight':wfModuleBisyncWeight,'wfModuleHssiWeight':wfModuleHssiWeight})