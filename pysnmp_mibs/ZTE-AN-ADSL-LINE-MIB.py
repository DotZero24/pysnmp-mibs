_w='zxAnAdslAturChanIntervalEntry'
_v='zxAnAdslAtucChanIntervalEntry'
_u='zxAnAdslLineAlarmConfProfileExtEntry'
_t='zxAnAdslLineConfProfileExtEntry'
_s='zxAnDslLoopBackTestBridgePort'
_r='zxAnDslLoopBackTestPort'
_q='zxAnDslLoopBackTestSlot'
_p='zxAnDslLoopBackTestShelf'
_o='zxAnDslLoopBackTestRack'
_n='zxAnAdslAturChanHist1DayNumber'
_m='zxAnAdslAtucChanHist1DayNumber'
_l='symbols'
_k='sixteenSymbols'
_j='eightSymbols'
_i='fourSymbols'
_h='twoSymbols'
_g='singleSymbol'
_f='halfSymbol'
_e='noProtection'
_d='autoAdaption'
_c='0.1 symbols'
_b='SnmpAdminString'
_a='zxAnAdslAturConnRateTolerance'
_Z='zxAnAdslAturThreshConnRate'
_Y='zxAnAdslMaxAturConnRateTolerance'
_X='zxAnAdslMaxThreshAturConnRate'
_W='zxAnAdslAtucConnRateTolerance'
_V='zxAnAdslAtucThreshConnRate'
_U='zxAnAdslMaxAtucConnRateTolerance'
_T='zxAnAdslMaxThreshAtucConnRate'
_S='Bits'
_R='disable'
_Q='enable'
_P='adslAturChanCurrTxRate'
_O='adslAturChanConfInterleaveMaxTxRate'
_N='not-accessible'
_M='Unsigned32'
_L='adslAtucChanCurrTxRate'
_K='adslAtucChanConfInterleaveMaxTxRate'
_J='seconds'
_I='ifIndex'
_H='IF-MIB'
_G='kbps'
_F='ADSL-LINE-MIB'
_E='ZTE-AN-ADSL-LINE-MIB'
_D='read-create'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslAtucChanConfInterleaveMaxTxRate,adslAtucChanCurrTxRate,adslAtucChanIntervalEntry,adslAturChanConfInterleaveMaxTxRate,adslAturChanCurrTxRate,adslAturChanIntervalEntry,adslLineAlarmConfProfileEntry,adslLineConfProfileEntry,adslLineConfProfileName=mibBuilder.importSymbols(_F,_K,_L,'adslAtucChanIntervalEntry',_O,_P,'adslAturChanIntervalEntry','adslLineAlarmConfProfileEntry','adslLineConfProfileEntry','adslLineConfProfileName')
ifIndex,=mibBuilder.importSymbols(_H,_I)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_b)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_S,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnAdslMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,1000))
_ZxAnAdslMibObjects_ObjectIdentity=ObjectIdentity
zxAnAdslMibObjects=_ZxAnAdslMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,1000,1))
_ZxAnAdslLineTable_Object=MibTable
zxAnAdslLineTable=_ZxAnAdslLineTable_Object((1,3,6,1,4,1,3902,1015,1000,1,1))
if mibBuilder.loadTexts:zxAnAdslLineTable.setStatus(_A)
_ZxAnAdslLineEntry_Object=MibTableRow
zxAnAdslLineEntry=_ZxAnAdslLineEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,1,1))
zxAnAdslLineEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslLineEntry.setStatus(_A)
_ZxAnAdslLineTxDataRate_Type=Gauge32
_ZxAnAdslLineTxDataRate_Object=MibTableColumn
zxAnAdslLineTxDataRate=_ZxAnAdslLineTxDataRate_Object((1,3,6,1,4,1,3902,1015,1000,1,1,1,1),_ZxAnAdslLineTxDataRate_Type())
zxAnAdslLineTxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslLineTxDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslLineTxDataRate.setUnits(_G)
_ZxAnAdslLineRxDataRate_Type=Gauge32
_ZxAnAdslLineRxDataRate_Object=MibTableColumn
zxAnAdslLineRxDataRate=_ZxAnAdslLineRxDataRate_Object((1,3,6,1,4,1,3902,1015,1000,1,1,1,2),_ZxAnAdslLineRxDataRate_Type())
zxAnAdslLineRxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslLineRxDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslLineRxDataRate.setUnits(_G)
class _ZxAnAdslAtucActInp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnAdslAtucActInp_Type.__name__=_C
_ZxAnAdslAtucActInp_Object=MibTableColumn
zxAnAdslAtucActInp=_ZxAnAdslAtucActInp_Object((1,3,6,1,4,1,3902,1015,1000,1,1,1,3),_ZxAnAdslAtucActInp_Type())
zxAnAdslAtucActInp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucActInp.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucActInp.setUnits(_c)
class _ZxAnAdslAturActInp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnAdslAturActInp_Type.__name__=_C
_ZxAnAdslAturActInp_Object=MibTableColumn
zxAnAdslAturActInp=_ZxAnAdslAturActInp_Object((1,3,6,1,4,1,3902,1015,1000,1,1,1,4),_ZxAnAdslAturActInp_Type())
zxAnAdslAturActInp.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturActInp.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturActInp.setUnits(_c)
class _ZxAnAdslLineExtConfPrf_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnAdslLineExtConfPrf_Type.__name__=_b
_ZxAnAdslLineExtConfPrf_Object=MibTableColumn
zxAnAdslLineExtConfPrf=_ZxAnAdslLineExtConfPrf_Object((1,3,6,1,4,1,3902,1015,1000,1,1,1,5),_ZxAnAdslLineExtConfPrf_Type())
zxAnAdslLineExtConfPrf.setMaxAccess('read-write')
if mibBuilder.loadTexts:zxAnAdslLineExtConfPrf.setStatus(_A)
_ZxAnAdslLineConfProfileExtTable_Object=MibTable
zxAnAdslLineConfProfileExtTable=_ZxAnAdslLineConfProfileExtTable_Object((1,3,6,1,4,1,3902,1015,1000,1,2))
if mibBuilder.loadTexts:zxAnAdslLineConfProfileExtTable.setStatus(_A)
_ZxAnAdslLineConfProfileExtEntry_Object=MibTableRow
zxAnAdslLineConfProfileExtEntry=_ZxAnAdslLineConfProfileExtEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1))
if mibBuilder.loadTexts:zxAnAdslLineConfProfileExtEntry.setStatus(_A)
_ZxAnAdslLineConfTxStartBin_Type=Integer32
_ZxAnAdslLineConfTxStartBin_Object=MibTableColumn
zxAnAdslLineConfTxStartBin=_ZxAnAdslLineConfTxStartBin_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,1),_ZxAnAdslLineConfTxStartBin_Type())
zxAnAdslLineConfTxStartBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfTxStartBin.setStatus(_A)
class _ZxAnAdslLineConfTxEndBin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_ZxAnAdslLineConfTxEndBin_Type.__name__=_C
_ZxAnAdslLineConfTxEndBin_Object=MibTableColumn
zxAnAdslLineConfTxEndBin=_ZxAnAdslLineConfTxEndBin_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,2),_ZxAnAdslLineConfTxEndBin_Type())
zxAnAdslLineConfTxEndBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfTxEndBin.setStatus(_A)
_ZxAnAdslLineConfRxStartBin_Type=Integer32
_ZxAnAdslLineConfRxStartBin_Object=MibTableColumn
zxAnAdslLineConfRxStartBin=_ZxAnAdslLineConfRxStartBin_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,3),_ZxAnAdslLineConfRxStartBin_Type())
zxAnAdslLineConfRxStartBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfRxStartBin.setStatus(_A)
class _ZxAnAdslLineConfRxEndBin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_ZxAnAdslLineConfRxEndBin_Type.__name__=_C
_ZxAnAdslLineConfRxEndBin_Object=MibTableColumn
zxAnAdslLineConfRxEndBin=_ZxAnAdslLineConfRxEndBin_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,4),_ZxAnAdslLineConfRxEndBin_Type())
zxAnAdslLineConfRxEndBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfRxEndBin.setStatus(_A)
class _ZxAnAdslLineConfUseCustomBins_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxAnAdslLineConfUseCustomBins_Type.__name__=_C
_ZxAnAdslLineConfUseCustomBins_Object=MibTableColumn
zxAnAdslLineConfUseCustomBins=_ZxAnAdslLineConfUseCustomBins_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,5),_ZxAnAdslLineConfUseCustomBins_Type())
zxAnAdslLineConfUseCustomBins.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfUseCustomBins.setStatus(_A)
_ZxAnAdslAtucConfPsdMaskType_Type=Integer32
_ZxAnAdslAtucConfPsdMaskType_Object=MibTableColumn
zxAnAdslAtucConfPsdMaskType=_ZxAnAdslAtucConfPsdMaskType_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,6),_ZxAnAdslAtucConfPsdMaskType_Type())
zxAnAdslAtucConfPsdMaskType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfPsdMaskType.setStatus(_A)
class _ZxAnAdslLineConfPMMode_Type(Bits):namedValues=NamedValues(*(('idle',0),('lowPower',1)))
_ZxAnAdslLineConfPMMode_Type.__name__=_S
_ZxAnAdslLineConfPMMode_Object=MibTableColumn
zxAnAdslLineConfPMMode=_ZxAnAdslLineConfPMMode_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,7),_ZxAnAdslLineConfPMMode_Type())
zxAnAdslLineConfPMMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfPMMode.setStatus(_A)
class _ZxAnAdslLineConfPML2Rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1024))
_ZxAnAdslLineConfPML2Rate_Type.__name__=_C
_ZxAnAdslLineConfPML2Rate_Object=MibTableColumn
zxAnAdslLineConfPML2Rate=_ZxAnAdslLineConfPML2Rate_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,8),_ZxAnAdslLineConfPML2Rate_Type())
zxAnAdslLineConfPML2Rate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfPML2Rate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslLineConfPML2Rate.setUnits(_G)
class _ZxAnAdsl2ConfMinProtectionDs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3),(_h,4),(_i,5),(_j,6),(_k,7)))
_ZxAnAdsl2ConfMinProtectionDs_Type.__name__=_C
_ZxAnAdsl2ConfMinProtectionDs_Object=MibTableColumn
zxAnAdsl2ConfMinProtectionDs=_ZxAnAdsl2ConfMinProtectionDs_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,9),_ZxAnAdsl2ConfMinProtectionDs_Type())
zxAnAdsl2ConfMinProtectionDs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdsl2ConfMinProtectionDs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdsl2ConfMinProtectionDs.setUnits(_l)
class _ZxAnAdslLineConfMinProtectionUs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_d,0),(_e,1),(_f,2),(_g,3),(_h,4),(_i,5),(_j,6),(_k,7)))
_ZxAnAdslLineConfMinProtectionUs_Type.__name__=_C
_ZxAnAdslLineConfMinProtectionUs_Object=MibTableColumn
zxAnAdslLineConfMinProtectionUs=_ZxAnAdslLineConfMinProtectionUs_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,10),_ZxAnAdslLineConfMinProtectionUs_Type())
zxAnAdslLineConfMinProtectionUs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslLineConfMinProtectionUs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslLineConfMinProtectionUs.setUnits(_l)
class _ZxAnAdslConfDMTConfTrellis_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxAnAdslConfDMTConfTrellis_Type.__name__=_C
_ZxAnAdslConfDMTConfTrellis_Object=MibTableColumn
zxAnAdslConfDMTConfTrellis=_ZxAnAdslConfDMTConfTrellis_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,11),_ZxAnAdslConfDMTConfTrellis_Type())
zxAnAdslConfDMTConfTrellis.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslConfDMTConfTrellis.setStatus(_A)
class _ZxAnAdslAtucConfMaxBitsPerBin_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZxAnAdslAtucConfMaxBitsPerBin_Type.__name__=_C
_ZxAnAdslAtucConfMaxBitsPerBin_Object=MibTableColumn
zxAnAdslAtucConfMaxBitsPerBin=_ZxAnAdslAtucConfMaxBitsPerBin_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,12),_ZxAnAdslAtucConfMaxBitsPerBin_Type())
zxAnAdslAtucConfMaxBitsPerBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfMaxBitsPerBin.setStatus(_A)
class _ZxAnAdslAtucConfBitSwapDs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxAnAdslAtucConfBitSwapDs_Type.__name__=_C
_ZxAnAdslAtucConfBitSwapDs_Object=MibTableColumn
zxAnAdslAtucConfBitSwapDs=_ZxAnAdslAtucConfBitSwapDs_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,13),_ZxAnAdslAtucConfBitSwapDs_Type())
zxAnAdslAtucConfBitSwapDs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfBitSwapDs.setStatus(_A)
class _ZxAnAdslAtucConfBitSwapUs_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxAnAdslAtucConfBitSwapUs_Type.__name__=_C
_ZxAnAdslAtucConfBitSwapUs_Object=MibTableColumn
zxAnAdslAtucConfBitSwapUs=_ZxAnAdslAtucConfBitSwapUs_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,14),_ZxAnAdslAtucConfBitSwapUs_Type())
zxAnAdslAtucConfBitSwapUs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfBitSwapUs.setStatus(_A)
class _ZxAnAdslAtucConfReAdsl2Enable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_ZxAnAdslAtucConfReAdsl2Enable_Type.__name__=_C
_ZxAnAdslAtucConfReAdsl2Enable_Object=MibTableColumn
zxAnAdslAtucConfReAdsl2Enable=_ZxAnAdslAtucConfReAdsl2Enable_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,15),_ZxAnAdslAtucConfReAdsl2Enable_Type())
zxAnAdslAtucConfReAdsl2Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfReAdsl2Enable.setStatus(_A)
class _ZxAnAdslAtucConfPmL0Time_Type(Integer32):defaultValue=240;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnAdslAtucConfPmL0Time_Type.__name__=_C
_ZxAnAdslAtucConfPmL0Time_Object=MibTableColumn
zxAnAdslAtucConfPmL0Time=_ZxAnAdslAtucConfPmL0Time_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,16),_ZxAnAdslAtucConfPmL0Time_Type())
zxAnAdslAtucConfPmL0Time.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfPmL0Time.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucConfPmL0Time.setUnits(_J)
class _ZxAnAdslAtucConfPmL2Time_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAnAdslAtucConfPmL2Time_Type.__name__=_C
_ZxAnAdslAtucConfPmL2Time_Object=MibTableColumn
zxAnAdslAtucConfPmL2Time=_ZxAnAdslAtucConfPmL2Time_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,17),_ZxAnAdslAtucConfPmL2Time_Type())
zxAnAdslAtucConfPmL2Time.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfPmL2Time.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucConfPmL2Time.setUnits(_J)
class _ZxAnAdslAtucConfPmL2Atpr_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ZxAnAdslAtucConfPmL2Atpr_Type.__name__=_C
_ZxAnAdslAtucConfPmL2Atpr_Object=MibTableColumn
zxAnAdslAtucConfPmL2Atpr=_ZxAnAdslAtucConfPmL2Atpr_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,18),_ZxAnAdslAtucConfPmL2Atpr_Type())
zxAnAdslAtucConfPmL2Atpr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConfPmL2Atpr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucConfPmL2Atpr.setUnits('dB')
class _ZxAdsl2ConfPsdMaskSelectUs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('adlu32Eu32',1),('adlu36Eu36',2),('adlu40Eu40',3),('adlu44Eu44',4),('adlu48Eu48',5),('adlu52Eu52',6),('adlu56Eu56',7),('adlu60Eu60',8),('adlu64Eu64',9)))
_ZxAdsl2ConfPsdMaskSelectUs_Type.__name__=_C
_ZxAdsl2ConfPsdMaskSelectUs_Object=MibTableColumn
zxAdsl2ConfPsdMaskSelectUs=_ZxAdsl2ConfPsdMaskSelectUs_Object((1,3,6,1,4,1,3902,1015,1000,1,2,1,19),_ZxAdsl2ConfPsdMaskSelectUs_Type())
zxAdsl2ConfPsdMaskSelectUs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdsl2ConfPsdMaskSelectUs.setStatus(_A)
_ZxAnAdslAtucChanTable_Object=MibTable
zxAnAdslAtucChanTable=_ZxAnAdslAtucChanTable_Object((1,3,6,1,4,1,3902,1015,1000,1,3))
if mibBuilder.loadTexts:zxAnAdslAtucChanTable.setStatus(_A)
_ZxAnAdslAtucChanEntry_Object=MibTableRow
zxAnAdslAtucChanEntry=_ZxAnAdslAtucChanEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,3,1))
zxAnAdslAtucChanEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslAtucChanEntry.setStatus(_A)
class _ZxAnAdslAtucChanInpEtr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000))
_ZxAnAdslAtucChanInpEtr_Type.__name__=_M
_ZxAnAdslAtucChanInpEtr_Object=MibTableColumn
zxAnAdslAtucChanInpEtr=_ZxAnAdslAtucChanInpEtr_Object((1,3,6,1,4,1,3902,1015,1000,1,3,1,1),_ZxAnAdslAtucChanInpEtr_Type())
zxAnAdslAtucChanInpEtr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpEtr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpEtr.setUnits(_G)
class _ZxAnAdslAtucChanInpEftr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000))
_ZxAnAdslAtucChanInpEftr_Type.__name__=_M
_ZxAnAdslAtucChanInpEftr_Object=MibTableColumn
zxAnAdslAtucChanInpEftr=_ZxAnAdslAtucChanInpEftr_Object((1,3,6,1,4,1,3902,1015,1000,1,3,1,2),_ZxAnAdslAtucChanInpEftr_Type())
zxAnAdslAtucChanInpEftr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpEftr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpEftr.setUnits(_G)
class _ZxAnAdslAtucChanInpMinEftr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000))
_ZxAnAdslAtucChanInpMinEftr_Type.__name__=_M
_ZxAnAdslAtucChanInpMinEftr_Object=MibTableColumn
zxAnAdslAtucChanInpMinEftr=_ZxAnAdslAtucChanInpMinEftr_Object((1,3,6,1,4,1,3902,1015,1000,1,3,1,3),_ZxAnAdslAtucChanInpMinEftr_Type())
zxAnAdslAtucChanInpMinEftr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpMinEftr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpMinEftr.setUnits(_G)
class _ZxAnAdslAtucChanInpActDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnAdslAtucChanInpActDelay_Type.__name__=_C
_ZxAnAdslAtucChanInpActDelay_Object=MibTableColumn
zxAnAdslAtucChanInpActDelay=_ZxAnAdslAtucChanInpActDelay_Object((1,3,6,1,4,1,3902,1015,1000,1,3,1,4),_ZxAnAdslAtucChanInpActDelay_Type())
zxAnAdslAtucChanInpActDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpActDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucChanInpActDelay.setUnits('ms')
_ZxAnAdslAturChanTable_Object=MibTable
zxAnAdslAturChanTable=_ZxAnAdslAturChanTable_Object((1,3,6,1,4,1,3902,1015,1000,1,4))
if mibBuilder.loadTexts:zxAnAdslAturChanTable.setStatus(_A)
_ZxAnAdslAturChanEntry_Object=MibTableRow
zxAnAdslAturChanEntry=_ZxAnAdslAturChanEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,4,1))
zxAnAdslAturChanEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslAturChanEntry.setStatus(_A)
class _ZxAnAdslAturChanInpEtr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000))
_ZxAnAdslAturChanInpEtr_Type.__name__=_M
_ZxAnAdslAturChanInpEtr_Object=MibTableColumn
zxAnAdslAturChanInpEtr=_ZxAnAdslAturChanInpEtr_Object((1,3,6,1,4,1,3902,1015,1000,1,4,1,1),_ZxAnAdslAturChanInpEtr_Type())
zxAnAdslAturChanInpEtr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanInpEtr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturChanInpEtr.setUnits(_G)
class _ZxAnAdslAturChanInpEftr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000))
_ZxAnAdslAturChanInpEftr_Type.__name__=_M
_ZxAnAdslAturChanInpEftr_Object=MibTableColumn
zxAnAdslAturChanInpEftr=_ZxAnAdslAturChanInpEftr_Object((1,3,6,1,4,1,3902,1015,1000,1,4,1,2),_ZxAnAdslAturChanInpEftr_Type())
zxAnAdslAturChanInpEftr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanInpEftr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturChanInpEftr.setUnits(_G)
class _ZxAnAdslAturChanInpMinEftr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,52000))
_ZxAnAdslAturChanInpMinEftr_Type.__name__=_M
_ZxAnAdslAturChanInpMinEftr_Object=MibTableColumn
zxAnAdslAturChanInpMinEftr=_ZxAnAdslAturChanInpMinEftr_Object((1,3,6,1,4,1,3902,1015,1000,1,4,1,3),_ZxAnAdslAturChanInpMinEftr_Type())
zxAnAdslAturChanInpMinEftr.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanInpMinEftr.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturChanInpMinEftr.setUnits(_G)
class _ZxAnAdslAturChanInpActDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_ZxAnAdslAturChanInpActDelay_Type.__name__=_C
_ZxAnAdslAturChanInpActDelay_Object=MibTableColumn
zxAnAdslAturChanInpActDelay=_ZxAnAdslAturChanInpActDelay_Object((1,3,6,1,4,1,3902,1015,1000,1,4,1,4),_ZxAnAdslAturChanInpActDelay_Type())
zxAnAdslAturChanInpActDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanInpActDelay.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturChanInpActDelay.setUnits('ms')
_ZxAnAdslLineAlarmConfProfileExtTable_Object=MibTable
zxAnAdslLineAlarmConfProfileExtTable=_ZxAnAdslLineAlarmConfProfileExtTable_Object((1,3,6,1,4,1,3902,1015,1000,1,20))
if mibBuilder.loadTexts:zxAnAdslLineAlarmConfProfileExtTable.setStatus(_A)
_ZxAnAdslLineAlarmConfProfileExtEntry_Object=MibTableRow
zxAnAdslLineAlarmConfProfileExtEntry=_ZxAnAdslLineAlarmConfProfileExtEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1))
if mibBuilder.loadTexts:zxAnAdslLineAlarmConfProfileExtEntry.setStatus(_A)
class _ZxAnAdslAtucConnRateTolerance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnAdslAtucConnRateTolerance_Type.__name__=_C
_ZxAnAdslAtucConnRateTolerance_Object=MibTableColumn
zxAnAdslAtucConnRateTolerance=_ZxAnAdslAtucConnRateTolerance_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,1),_ZxAnAdslAtucConnRateTolerance_Type())
zxAnAdslAtucConnRateTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucConnRateTolerance.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucConnRateTolerance.setUnits('%')
class _ZxAnAdslAturConnRateTolerance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnAdslAturConnRateTolerance_Type.__name__=_C
_ZxAnAdslAturConnRateTolerance_Object=MibTableColumn
zxAnAdslAturConnRateTolerance=_ZxAnAdslAturConnRateTolerance_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,2),_ZxAnAdslAturConnRateTolerance_Type())
zxAnAdslAturConnRateTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAturConnRateTolerance.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturConnRateTolerance.setUnits('%')
class _ZxAnAdslAtucThreshConnRate_Type(Integer32):defaultValue=0
_ZxAnAdslAtucThreshConnRate_Type.__name__=_C
_ZxAnAdslAtucThreshConnRate_Object=MibTableColumn
zxAnAdslAtucThreshConnRate=_ZxAnAdslAtucThreshConnRate_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,3),_ZxAnAdslAtucThreshConnRate_Type())
zxAnAdslAtucThreshConnRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAtucThreshConnRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucThreshConnRate.setUnits(_G)
class _ZxAnAdslAturThreshConnRate_Type(Integer32):defaultValue=0
_ZxAnAdslAturThreshConnRate_Type.__name__=_C
_ZxAnAdslAturThreshConnRate_Object=MibTableColumn
zxAnAdslAturThreshConnRate=_ZxAnAdslAturThreshConnRate_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,4),_ZxAnAdslAturThreshConnRate_Type())
zxAnAdslAturThreshConnRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAturThreshConnRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturThreshConnRate.setUnits(_G)
class _ZxAnAdslMaxAtucConnRateTolerance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnAdslMaxAtucConnRateTolerance_Type.__name__=_C
_ZxAnAdslMaxAtucConnRateTolerance_Object=MibTableColumn
zxAnAdslMaxAtucConnRateTolerance=_ZxAnAdslMaxAtucConnRateTolerance_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,5),_ZxAnAdslMaxAtucConnRateTolerance_Type())
zxAnAdslMaxAtucConnRateTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslMaxAtucConnRateTolerance.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslMaxAtucConnRateTolerance.setUnits('%')
class _ZxAnAdslMaxAturConnRateTolerance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnAdslMaxAturConnRateTolerance_Type.__name__=_C
_ZxAnAdslMaxAturConnRateTolerance_Object=MibTableColumn
zxAnAdslMaxAturConnRateTolerance=_ZxAnAdslMaxAturConnRateTolerance_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,6),_ZxAnAdslMaxAturConnRateTolerance_Type())
zxAnAdslMaxAturConnRateTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslMaxAturConnRateTolerance.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslMaxAturConnRateTolerance.setUnits('%')
class _ZxAnAdslMaxThreshAtucConnRate_Type(Integer32):defaultValue=0
_ZxAnAdslMaxThreshAtucConnRate_Type.__name__=_C
_ZxAnAdslMaxThreshAtucConnRate_Object=MibTableColumn
zxAnAdslMaxThreshAtucConnRate=_ZxAnAdslMaxThreshAtucConnRate_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,7),_ZxAnAdslMaxThreshAtucConnRate_Type())
zxAnAdslMaxThreshAtucConnRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslMaxThreshAtucConnRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslMaxThreshAtucConnRate.setUnits(_G)
class _ZxAnAdslMaxThreshAturConnRate_Type(Integer32):defaultValue=0
_ZxAnAdslMaxThreshAturConnRate_Type.__name__=_C
_ZxAnAdslMaxThreshAturConnRate_Object=MibTableColumn
zxAnAdslMaxThreshAturConnRate=_ZxAnAdslMaxThreshAturConnRate_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,8),_ZxAnAdslMaxThreshAturConnRate_Type())
zxAnAdslMaxThreshAturConnRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslMaxThreshAturConnRate.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslMaxThreshAturConnRate.setUnits(_G)
class _ZxAnAdslAturInitFailTrapEnable_Type(Bits):namedValues=NamedValues(*(('unused1',0),('lossOfFraming',1),('lossOfSignal',2),('lossOfPower',3),('unused2',4),('lossOfSignalQuality',5)))
_ZxAnAdslAturInitFailTrapEnable_Type.__name__=_S
_ZxAnAdslAturInitFailTrapEnable_Object=MibTableColumn
zxAnAdslAturInitFailTrapEnable=_ZxAnAdslAturInitFailTrapEnable_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,9),_ZxAnAdslAturInitFailTrapEnable_Type())
zxAnAdslAturInitFailTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslAturInitFailTrapEnable.setStatus(_A)
class _ZxAnAdslThreshAtucInpLeftr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnAdslThreshAtucInpLeftr_Type.__name__=_C
_ZxAnAdslThreshAtucInpLeftr_Object=MibTableColumn
zxAnAdslThreshAtucInpLeftr=_ZxAnAdslThreshAtucInpLeftr_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,10),_ZxAnAdslThreshAtucInpLeftr_Type())
zxAnAdslThreshAtucInpLeftr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslThreshAtucInpLeftr.setStatus(_A)
class _ZxAnAdslThreshAturInpLeftr_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAnAdslThreshAturInpLeftr_Type.__name__=_C
_ZxAnAdslThreshAturInpLeftr_Object=MibTableColumn
zxAnAdslThreshAturInpLeftr=_ZxAnAdslThreshAturInpLeftr_Object((1,3,6,1,4,1,3902,1015,1000,1,20,1,11),_ZxAnAdslThreshAturInpLeftr_Type())
zxAnAdslThreshAturInpLeftr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnAdslThreshAturInpLeftr.setStatus(_A)
_ZxAnAdslAtucPerfDataTable_Object=MibTable
zxAnAdslAtucPerfDataTable=_ZxAnAdslAtucPerfDataTable_Object((1,3,6,1,4,1,3902,1015,1000,1,21))
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataTable.setStatus(_A)
_ZxAnAdslAtucPerfDataEntry_Object=MibTableRow
zxAnAdslAtucPerfDataEntry=_ZxAnAdslAtucPerfDataEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,21,1))
zxAnAdslAtucPerfDataEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataEntry.setStatus(_A)
_ZxAnAdslAtucPerfDataFecs_Type=Counter32
_ZxAnAdslAtucPerfDataFecs_Object=MibTableColumn
zxAnAdslAtucPerfDataFecs=_ZxAnAdslAtucPerfDataFecs_Object((1,3,6,1,4,1,3902,1015,1000,1,21,1,1),_ZxAnAdslAtucPerfDataFecs_Type())
zxAnAdslAtucPerfDataFecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataFecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataFecs.setUnits(_J)
_ZxAnAdslAtucPerfDataCurr15Fecs_Type=Counter32
_ZxAnAdslAtucPerfDataCurr15Fecs_Object=MibTableColumn
zxAnAdslAtucPerfDataCurr15Fecs=_ZxAnAdslAtucPerfDataCurr15Fecs_Object((1,3,6,1,4,1,3902,1015,1000,1,21,1,2),_ZxAnAdslAtucPerfDataCurr15Fecs_Type())
zxAnAdslAtucPerfDataCurr15Fecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataCurr15Fecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataCurr15Fecs.setUnits(_J)
_ZxAnAdslAtucPerfDataCurr1DayFecs_Type=Counter32
_ZxAnAdslAtucPerfDataCurr1DayFecs_Object=MibTableColumn
zxAnAdslAtucPerfDataCurr1DayFecs=_ZxAnAdslAtucPerfDataCurr1DayFecs_Object((1,3,6,1,4,1,3902,1015,1000,1,21,1,3),_ZxAnAdslAtucPerfDataCurr1DayFecs_Type())
zxAnAdslAtucPerfDataCurr1DayFecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataCurr1DayFecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataCurr1DayFecs.setUnits(_J)
_ZxAnAdslAtucPerfDataPrev1DayFecs_Type=Counter32
_ZxAnAdslAtucPerfDataPrev1DayFecs_Object=MibTableColumn
zxAnAdslAtucPerfDataPrev1DayFecs=_ZxAnAdslAtucPerfDataPrev1DayFecs_Object((1,3,6,1,4,1,3902,1015,1000,1,21,1,4),_ZxAnAdslAtucPerfDataPrev1DayFecs_Type())
zxAnAdslAtucPerfDataPrev1DayFecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataPrev1DayFecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAtucPerfDataPrev1DayFecs.setUnits(_J)
_ZxAnAdslAturPerfDataTable_Object=MibTable
zxAnAdslAturPerfDataTable=_ZxAnAdslAturPerfDataTable_Object((1,3,6,1,4,1,3902,1015,1000,1,22))
if mibBuilder.loadTexts:zxAnAdslAturPerfDataTable.setStatus(_A)
_ZxAnAdslAturPerfDataEntry_Object=MibTableRow
zxAnAdslAturPerfDataEntry=_ZxAnAdslAturPerfDataEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,22,1))
zxAnAdslAturPerfDataEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslAturPerfDataEntry.setStatus(_A)
_ZxAnAdslAturPerfDataFecs_Type=Counter32
_ZxAnAdslAturPerfDataFecs_Object=MibTableColumn
zxAnAdslAturPerfDataFecs=_ZxAnAdslAturPerfDataFecs_Object((1,3,6,1,4,1,3902,1015,1000,1,22,1,1),_ZxAnAdslAturPerfDataFecs_Type())
zxAnAdslAturPerfDataFecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataFecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataFecs.setUnits(_J)
_ZxAnAdslAturPerfDataCurr15Fecs_Type=Counter32
_ZxAnAdslAturPerfDataCurr15Fecs_Object=MibTableColumn
zxAnAdslAturPerfDataCurr15Fecs=_ZxAnAdslAturPerfDataCurr15Fecs_Object((1,3,6,1,4,1,3902,1015,1000,1,22,1,2),_ZxAnAdslAturPerfDataCurr15Fecs_Type())
zxAnAdslAturPerfDataCurr15Fecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataCurr15Fecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataCurr15Fecs.setUnits(_J)
_ZxAnAdslAturPerfDataCurr1DayFecs_Type=Counter32
_ZxAnAdslAturPerfDataCurr1DayFecs_Object=MibTableColumn
zxAnAdslAturPerfDataCurr1DayFecs=_ZxAnAdslAturPerfDataCurr1DayFecs_Object((1,3,6,1,4,1,3902,1015,1000,1,22,1,3),_ZxAnAdslAturPerfDataCurr1DayFecs_Type())
zxAnAdslAturPerfDataCurr1DayFecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataCurr1DayFecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataCurr1DayFecs.setUnits(_J)
_ZxAnAdslAturPerfDataPrev1DayFecs_Type=Counter32
_ZxAnAdslAturPerfDataPrev1DayFecs_Object=MibTableColumn
zxAnAdslAturPerfDataPrev1DayFecs=_ZxAnAdslAturPerfDataPrev1DayFecs_Object((1,3,6,1,4,1,3902,1015,1000,1,22,1,4),_ZxAnAdslAturPerfDataPrev1DayFecs_Type())
zxAnAdslAturPerfDataPrev1DayFecs.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataPrev1DayFecs.setStatus(_A)
if mibBuilder.loadTexts:zxAnAdslAturPerfDataPrev1DayFecs.setUnits(_J)
_ZxAnAdslAtucChanPerfDataTable_Object=MibTable
zxAnAdslAtucChanPerfDataTable=_ZxAnAdslAtucChanPerfDataTable_Object((1,3,6,1,4,1,3902,1015,1000,1,23))
if mibBuilder.loadTexts:zxAnAdslAtucChanPerfDataTable.setStatus(_A)
_ZxAnAdslAtucChanPerfDataEntry_Object=MibTableRow
zxAnAdslAtucChanPerfDataEntry=_ZxAnAdslAtucChanPerfDataEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1))
zxAnAdslAtucChanPerfDataEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslAtucChanPerfDataEntry.setStatus(_A)
_ZxAnAtucChanPerfCurr15RtxDtu_Type=Counter32
_ZxAnAtucChanPerfCurr15RtxDtu_Object=MibTableColumn
zxAnAtucChanPerfCurr15RtxDtu=_ZxAnAtucChanPerfCurr15RtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1,1),_ZxAnAtucChanPerfCurr15RtxDtu_Type())
zxAnAtucChanPerfCurr15RtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAtucChanPerfCurr15RtxDtu.setStatus(_A)
_ZxAnAtucChanPerfCurr15RtxCDtu_Type=Counter32
_ZxAnAtucChanPerfCurr15RtxCDtu_Object=MibTableColumn
zxAnAtucChanPerfCurr15RtxCDtu=_ZxAnAtucChanPerfCurr15RtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1,2),_ZxAnAtucChanPerfCurr15RtxCDtu_Type())
zxAnAtucChanPerfCurr15RtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAtucChanPerfCurr15RtxCDtu.setStatus(_A)
_ZxAnAtucChanPerfCurr15RtxUcDtu_Type=Counter32
_ZxAnAtucChanPerfCurr15RtxUcDtu_Object=MibTableColumn
zxAnAtucChanPerfCurr15RtxUcDtu=_ZxAnAtucChanPerfCurr15RtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1,3),_ZxAnAtucChanPerfCurr15RtxUcDtu_Type())
zxAnAtucChanPerfCurr15RtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAtucChanPerfCurr15RtxUcDtu.setStatus(_A)
_ZxAnAtucChanPerfCurr1DRtxDtu_Type=Counter32
_ZxAnAtucChanPerfCurr1DRtxDtu_Object=MibTableColumn
zxAnAtucChanPerfCurr1DRtxDtu=_ZxAnAtucChanPerfCurr1DRtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1,4),_ZxAnAtucChanPerfCurr1DRtxDtu_Type())
zxAnAtucChanPerfCurr1DRtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAtucChanPerfCurr1DRtxDtu.setStatus(_A)
_ZxAnAtucChanPerfCurr1DRtxCDtu_Type=Counter32
_ZxAnAtucChanPerfCurr1DRtxCDtu_Object=MibTableColumn
zxAnAtucChanPerfCurr1DRtxCDtu=_ZxAnAtucChanPerfCurr1DRtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1,5),_ZxAnAtucChanPerfCurr1DRtxCDtu_Type())
zxAnAtucChanPerfCurr1DRtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAtucChanPerfCurr1DRtxCDtu.setStatus(_A)
_ZxAnAtucChanPerfCurr1DRtxUcDtu_Type=Counter32
_ZxAnAtucChanPerfCurr1DRtxUcDtu_Object=MibTableColumn
zxAnAtucChanPerfCurr1DRtxUcDtu=_ZxAnAtucChanPerfCurr1DRtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,23,1,6),_ZxAnAtucChanPerfCurr1DRtxUcDtu_Type())
zxAnAtucChanPerfCurr1DRtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAtucChanPerfCurr1DRtxUcDtu.setStatus(_A)
_ZxAnAdslAturChanPerfDataTable_Object=MibTable
zxAnAdslAturChanPerfDataTable=_ZxAnAdslAturChanPerfDataTable_Object((1,3,6,1,4,1,3902,1015,1000,1,24))
if mibBuilder.loadTexts:zxAnAdslAturChanPerfDataTable.setStatus(_A)
_ZxAnAdslAturChanPerfDataEntry_Object=MibTableRow
zxAnAdslAturChanPerfDataEntry=_ZxAnAdslAturChanPerfDataEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1))
zxAnAdslAturChanPerfDataEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:zxAnAdslAturChanPerfDataEntry.setStatus(_A)
_ZxAnAturChanPerfCurr15RtxDtu_Type=Counter32
_ZxAnAturChanPerfCurr15RtxDtu_Object=MibTableColumn
zxAnAturChanPerfCurr15RtxDtu=_ZxAnAturChanPerfCurr15RtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1,1),_ZxAnAturChanPerfCurr15RtxDtu_Type())
zxAnAturChanPerfCurr15RtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAturChanPerfCurr15RtxDtu.setStatus(_A)
_ZxAnAturChanPerfCurr15RtxCDtu_Type=Counter32
_ZxAnAturChanPerfCurr15RtxCDtu_Object=MibTableColumn
zxAnAturChanPerfCurr15RtxCDtu=_ZxAnAturChanPerfCurr15RtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1,2),_ZxAnAturChanPerfCurr15RtxCDtu_Type())
zxAnAturChanPerfCurr15RtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAturChanPerfCurr15RtxCDtu.setStatus(_A)
_ZxAnAturChanPerfCurr15RtxUcDtu_Type=Counter32
_ZxAnAturChanPerfCurr15RtxUcDtu_Object=MibTableColumn
zxAnAturChanPerfCurr15RtxUcDtu=_ZxAnAturChanPerfCurr15RtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1,3),_ZxAnAturChanPerfCurr15RtxUcDtu_Type())
zxAnAturChanPerfCurr15RtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAturChanPerfCurr15RtxUcDtu.setStatus(_A)
_ZxAnAturChanPerfCurr1DRtxDtu_Type=Counter32
_ZxAnAturChanPerfCurr1DRtxDtu_Object=MibTableColumn
zxAnAturChanPerfCurr1DRtxDtu=_ZxAnAturChanPerfCurr1DRtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1,4),_ZxAnAturChanPerfCurr1DRtxDtu_Type())
zxAnAturChanPerfCurr1DRtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAturChanPerfCurr1DRtxDtu.setStatus(_A)
_ZxAnAturChanPerfCurr1DRtxCDtu_Type=Counter32
_ZxAnAturChanPerfCurr1DRtxCDtu_Object=MibTableColumn
zxAnAturChanPerfCurr1DRtxCDtu=_ZxAnAturChanPerfCurr1DRtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1,5),_ZxAnAturChanPerfCurr1DRtxCDtu_Type())
zxAnAturChanPerfCurr1DRtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAturChanPerfCurr1DRtxCDtu.setStatus(_A)
_ZxAnAturChanPerfCurr1DRtxUcDtu_Type=Counter32
_ZxAnAturChanPerfCurr1DRtxUcDtu_Object=MibTableColumn
zxAnAturChanPerfCurr1DRtxUcDtu=_ZxAnAturChanPerfCurr1DRtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,24,1,6),_ZxAnAturChanPerfCurr1DRtxUcDtu_Type())
zxAnAturChanPerfCurr1DRtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAturChanPerfCurr1DRtxUcDtu.setStatus(_A)
_ZxAnAdslAtucChanIntervalTable_Object=MibTable
zxAnAdslAtucChanIntervalTable=_ZxAnAdslAtucChanIntervalTable_Object((1,3,6,1,4,1,3902,1015,1000,1,25))
if mibBuilder.loadTexts:zxAnAdslAtucChanIntervalTable.setStatus(_A)
_ZxAnAdslAtucChanIntervalEntry_Object=MibTableRow
zxAnAdslAtucChanIntervalEntry=_ZxAnAdslAtucChanIntervalEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,25,1))
if mibBuilder.loadTexts:zxAnAdslAtucChanIntervalEntry.setStatus(_A)
_ZxAnAdslAtucChanIntervalRtxDtu_Type=Counter32
_ZxAnAdslAtucChanIntervalRtxDtu_Object=MibTableColumn
zxAnAdslAtucChanIntervalRtxDtu=_ZxAnAdslAtucChanIntervalRtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,25,1,1),_ZxAnAdslAtucChanIntervalRtxDtu_Type())
zxAnAdslAtucChanIntervalRtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanIntervalRtxDtu.setStatus(_A)
_ZxAnAdslAtucChanIntervalRtxCDtu_Type=Counter32
_ZxAnAdslAtucChanIntervalRtxCDtu_Object=MibTableColumn
zxAnAdslAtucChanIntervalRtxCDtu=_ZxAnAdslAtucChanIntervalRtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,25,1,2),_ZxAnAdslAtucChanIntervalRtxCDtu_Type())
zxAnAdslAtucChanIntervalRtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanIntervalRtxCDtu.setStatus(_A)
_ZxAnAdslAtucChanIntervalRtxUcDtu_Type=Counter32
_ZxAnAdslAtucChanIntervalRtxUcDtu_Object=MibTableColumn
zxAnAdslAtucChanIntervalRtxUcDtu=_ZxAnAdslAtucChanIntervalRtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,25,1,3),_ZxAnAdslAtucChanIntervalRtxUcDtu_Type())
zxAnAdslAtucChanIntervalRtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanIntervalRtxUcDtu.setStatus(_A)
_ZxAnAdslAturChanIntervalTable_Object=MibTable
zxAnAdslAturChanIntervalTable=_ZxAnAdslAturChanIntervalTable_Object((1,3,6,1,4,1,3902,1015,1000,1,26))
if mibBuilder.loadTexts:zxAnAdslAturChanIntervalTable.setStatus(_A)
_ZxAnAdslAturChanIntervalEntry_Object=MibTableRow
zxAnAdslAturChanIntervalEntry=_ZxAnAdslAturChanIntervalEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,26,1))
if mibBuilder.loadTexts:zxAnAdslAturChanIntervalEntry.setStatus(_A)
_ZxAnAdslAturChanIntervalRtxDtu_Type=Counter32
_ZxAnAdslAturChanIntervalRtxDtu_Object=MibTableColumn
zxAnAdslAturChanIntervalRtxDtu=_ZxAnAdslAturChanIntervalRtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,26,1,1),_ZxAnAdslAturChanIntervalRtxDtu_Type())
zxAnAdslAturChanIntervalRtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanIntervalRtxDtu.setStatus(_A)
_ZxAnAdslAturChanIntervalRtxCDtu_Type=Counter32
_ZxAnAdslAturChanIntervalRtxCDtu_Object=MibTableColumn
zxAnAdslAturChanIntervalRtxCDtu=_ZxAnAdslAturChanIntervalRtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,26,1,2),_ZxAnAdslAturChanIntervalRtxCDtu_Type())
zxAnAdslAturChanIntervalRtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanIntervalRtxCDtu.setStatus(_A)
_ZxAnAdslAturChanIntervalRtxUcDtu_Type=Counter32
_ZxAnAdslAturChanIntervalRtxUcDtu_Object=MibTableColumn
zxAnAdslAturChanIntervalRtxUcDtu=_ZxAnAdslAturChanIntervalRtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,26,1,3),_ZxAnAdslAturChanIntervalRtxUcDtu_Type())
zxAnAdslAturChanIntervalRtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanIntervalRtxUcDtu.setStatus(_A)
_ZxAnAdslAtucChanHist1DayTable_Object=MibTable
zxAnAdslAtucChanHist1DayTable=_ZxAnAdslAtucChanHist1DayTable_Object((1,3,6,1,4,1,3902,1015,1000,1,27))
if mibBuilder.loadTexts:zxAnAdslAtucChanHist1DayTable.setStatus(_A)
_ZxAnAdslAtucChanHist1DayEntry_Object=MibTableRow
zxAnAdslAtucChanHist1DayEntry=_ZxAnAdslAtucChanHist1DayEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,27,1))
zxAnAdslAtucChanHist1DayEntry.setIndexNames((0,_H,_I),(0,_E,_m))
if mibBuilder.loadTexts:zxAnAdslAtucChanHist1DayEntry.setStatus(_A)
class _ZxAnAdslAtucChanHist1DayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ZxAnAdslAtucChanHist1DayNumber_Type.__name__=_C
_ZxAnAdslAtucChanHist1DayNumber_Object=MibTableColumn
zxAnAdslAtucChanHist1DayNumber=_ZxAnAdslAtucChanHist1DayNumber_Object((1,3,6,1,4,1,3902,1015,1000,1,27,1,1),_ZxAnAdslAtucChanHist1DayNumber_Type())
zxAnAdslAtucChanHist1DayNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnAdslAtucChanHist1DayNumber.setStatus(_A)
_ZxAnAdslAtucChanHist1DayRtxDtu_Type=Counter32
_ZxAnAdslAtucChanHist1DayRtxDtu_Object=MibTableColumn
zxAnAdslAtucChanHist1DayRtxDtu=_ZxAnAdslAtucChanHist1DayRtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,27,1,2),_ZxAnAdslAtucChanHist1DayRtxDtu_Type())
zxAnAdslAtucChanHist1DayRtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanHist1DayRtxDtu.setStatus(_A)
_ZxAnAdslAtucChanHist1DayRtxCDtu_Type=Counter32
_ZxAnAdslAtucChanHist1DayRtxCDtu_Object=MibTableColumn
zxAnAdslAtucChanHist1DayRtxCDtu=_ZxAnAdslAtucChanHist1DayRtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,27,1,3),_ZxAnAdslAtucChanHist1DayRtxCDtu_Type())
zxAnAdslAtucChanHist1DayRtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanHist1DayRtxCDtu.setStatus(_A)
_ZxAnAdslAtucChanHist1DayRtxUcDtu_Type=Counter32
_ZxAnAdslAtucChanHist1DayRtxUcDtu_Object=MibTableColumn
zxAnAdslAtucChanHist1DayRtxUcDtu=_ZxAnAdslAtucChanHist1DayRtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,27,1,4),_ZxAnAdslAtucChanHist1DayRtxUcDtu_Type())
zxAnAdslAtucChanHist1DayRtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAtucChanHist1DayRtxUcDtu.setStatus(_A)
_ZxAnAdslAturChanHist1DayTable_Object=MibTable
zxAnAdslAturChanHist1DayTable=_ZxAnAdslAturChanHist1DayTable_Object((1,3,6,1,4,1,3902,1015,1000,1,28))
if mibBuilder.loadTexts:zxAnAdslAturChanHist1DayTable.setStatus(_A)
_ZxAnAdslAturChanHist1DayEntry_Object=MibTableRow
zxAnAdslAturChanHist1DayEntry=_ZxAnAdslAturChanHist1DayEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,28,1))
zxAnAdslAturChanHist1DayEntry.setIndexNames((0,_H,_I),(0,_E,_n))
if mibBuilder.loadTexts:zxAnAdslAturChanHist1DayEntry.setStatus(_A)
class _ZxAnAdslAturChanHist1DayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_ZxAnAdslAturChanHist1DayNumber_Type.__name__=_C
_ZxAnAdslAturChanHist1DayNumber_Object=MibTableColumn
zxAnAdslAturChanHist1DayNumber=_ZxAnAdslAturChanHist1DayNumber_Object((1,3,6,1,4,1,3902,1015,1000,1,28,1,1),_ZxAnAdslAturChanHist1DayNumber_Type())
zxAnAdslAturChanHist1DayNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnAdslAturChanHist1DayNumber.setStatus(_A)
_ZxAnAdslAturChanHist1DayRtxDtu_Type=Counter32
_ZxAnAdslAturChanHist1DayRtxDtu_Object=MibTableColumn
zxAnAdslAturChanHist1DayRtxDtu=_ZxAnAdslAturChanHist1DayRtxDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,28,1,2),_ZxAnAdslAturChanHist1DayRtxDtu_Type())
zxAnAdslAturChanHist1DayRtxDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanHist1DayRtxDtu.setStatus(_A)
_ZxAnAdslAturChanHist1DayRtxCDtu_Type=Counter32
_ZxAnAdslAturChanHist1DayRtxCDtu_Object=MibTableColumn
zxAnAdslAturChanHist1DayRtxCDtu=_ZxAnAdslAturChanHist1DayRtxCDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,28,1,3),_ZxAnAdslAturChanHist1DayRtxCDtu_Type())
zxAnAdslAturChanHist1DayRtxCDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanHist1DayRtxCDtu.setStatus(_A)
_ZxAnAdslAturChanHist1DayRtxUcDtu_Type=Counter32
_ZxAnAdslAturChanHist1DayRtxUcDtu_Object=MibTableColumn
zxAnAdslAturChanHist1DayRtxUcDtu=_ZxAnAdslAturChanHist1DayRtxUcDtu_Object((1,3,6,1,4,1,3902,1015,1000,1,28,1,4),_ZxAnAdslAturChanHist1DayRtxUcDtu_Type())
zxAnAdslAturChanHist1DayRtxUcDtu.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnAdslAturChanHist1DayRtxUcDtu.setStatus(_A)
_ZxAnDslLoopBackTestTable_Object=MibTable
zxAnDslLoopBackTestTable=_ZxAnDslLoopBackTestTable_Object((1,3,6,1,4,1,3902,1015,1000,1,30))
if mibBuilder.loadTexts:zxAnDslLoopBackTestTable.setStatus(_A)
_ZxAnDslLoopBackTestEntry_Object=MibTableRow
zxAnDslLoopBackTestEntry=_ZxAnDslLoopBackTestEntry_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1))
zxAnDslLoopBackTestEntry.setIndexNames((0,_E,_o),(0,_E,_p),(0,_E,_q),(0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:zxAnDslLoopBackTestEntry.setStatus(_A)
_ZxAnDslLoopBackTestRack_Type=Integer32
_ZxAnDslLoopBackTestRack_Object=MibTableColumn
zxAnDslLoopBackTestRack=_ZxAnDslLoopBackTestRack_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,1),_ZxAnDslLoopBackTestRack_Type())
zxAnDslLoopBackTestRack.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnDslLoopBackTestRack.setStatus(_A)
_ZxAnDslLoopBackTestShelf_Type=Integer32
_ZxAnDslLoopBackTestShelf_Object=MibTableColumn
zxAnDslLoopBackTestShelf=_ZxAnDslLoopBackTestShelf_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,2),_ZxAnDslLoopBackTestShelf_Type())
zxAnDslLoopBackTestShelf.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnDslLoopBackTestShelf.setStatus(_A)
_ZxAnDslLoopBackTestSlot_Type=Integer32
_ZxAnDslLoopBackTestSlot_Object=MibTableColumn
zxAnDslLoopBackTestSlot=_ZxAnDslLoopBackTestSlot_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,3),_ZxAnDslLoopBackTestSlot_Type())
zxAnDslLoopBackTestSlot.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnDslLoopBackTestSlot.setStatus(_A)
_ZxAnDslLoopBackTestPort_Type=Integer32
_ZxAnDslLoopBackTestPort_Object=MibTableColumn
zxAnDslLoopBackTestPort=_ZxAnDslLoopBackTestPort_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,4),_ZxAnDslLoopBackTestPort_Type())
zxAnDslLoopBackTestPort.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnDslLoopBackTestPort.setStatus(_A)
_ZxAnDslLoopBackTestBridgePort_Type=Integer32
_ZxAnDslLoopBackTestBridgePort_Object=MibTableColumn
zxAnDslLoopBackTestBridgePort=_ZxAnDslLoopBackTestBridgePort_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,5),_ZxAnDslLoopBackTestBridgePort_Type())
zxAnDslLoopBackTestBridgePort.setMaxAccess(_N)
if mibBuilder.loadTexts:zxAnDslLoopBackTestBridgePort.setStatus(_A)
class _ZxAnDslLoopBackTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('noOper',0),('cancle',1),('utopia',2),('afe',3),('hybrid',4),('xTUC_OAM',5),('xTUR_OAM',6),('xTUR_CC',7),('digital',8)))
_ZxAnDslLoopBackTestType_Type.__name__=_C
_ZxAnDslLoopBackTestType_Object=MibTableColumn
zxAnDslLoopBackTestType=_ZxAnDslLoopBackTestType_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,6),_ZxAnDslLoopBackTestType_Type())
zxAnDslLoopBackTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDslLoopBackTestType.setStatus(_A)
class _ZxAnDslLoopBackTestOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('neverExcute',0),('excuting',1),('excuted',2),('faliedToCommit',3)))
_ZxAnDslLoopBackTestOperStatus_Type.__name__=_C
_ZxAnDslLoopBackTestOperStatus_Object=MibTableColumn
zxAnDslLoopBackTestOperStatus=_ZxAnDslLoopBackTestOperStatus_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,7),_ZxAnDslLoopBackTestOperStatus_Type())
zxAnDslLoopBackTestOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnDslLoopBackTestOperStatus.setStatus(_A)
class _ZxAnDslLoopBackTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('noResult',0),('success',1),('generalFailed',2),('noSupport',3),('unkown',4),('noSuchPort',5),('loopBackFailed',6),('portNotActive',7),('portInTesting',8),('portInService',9),('portFailures',10),('cardFailures',11),('noPvcFound',12),('unknownTestType',13)))
_ZxAnDslLoopBackTestResult_Type.__name__=_C
_ZxAnDslLoopBackTestResult_Object=MibTableColumn
zxAnDslLoopBackTestResult=_ZxAnDslLoopBackTestResult_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,8),_ZxAnDslLoopBackTestResult_Type())
zxAnDslLoopBackTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnDslLoopBackTestResult.setStatus(_A)
_ZxAnDslLoopBackTestConfSendCells_Type=Integer32
_ZxAnDslLoopBackTestConfSendCells_Object=MibTableColumn
zxAnDslLoopBackTestConfSendCells=_ZxAnDslLoopBackTestConfSendCells_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,9),_ZxAnDslLoopBackTestConfSendCells_Type())
zxAnDslLoopBackTestConfSendCells.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDslLoopBackTestConfSendCells.setStatus(_A)
_ZxAnDslLoopBackTestResultRecivedCells_Type=Integer32
_ZxAnDslLoopBackTestResultRecivedCells_Object=MibTableColumn
zxAnDslLoopBackTestResultRecivedCells=_ZxAnDslLoopBackTestResultRecivedCells_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,10),_ZxAnDslLoopBackTestResultRecivedCells_Type())
zxAnDslLoopBackTestResultRecivedCells.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAnDslLoopBackTestResultRecivedCells.setStatus(_A)
_ZxAnDslLoopBackTestRowStatus_Type=RowStatus
_ZxAnDslLoopBackTestRowStatus_Object=MibTableColumn
zxAnDslLoopBackTestRowStatus=_ZxAnDslLoopBackTestRowStatus_Object((1,3,6,1,4,1,3902,1015,1000,1,30,1,15),_ZxAnDslLoopBackTestRowStatus_Type())
zxAnDslLoopBackTestRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnDslLoopBackTestRowStatus.setStatus(_A)
_ZxAnAdslTraps_ObjectIdentity=ObjectIdentity
zxAnAdslTraps=_ZxAnAdslTraps_ObjectIdentity((1,3,6,1,4,1,3902,1015,1000,2))
adslLineConfProfileEntry.registerAugmentions((_E,_t))
zxAnAdslLineConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineAlarmConfProfileEntry.registerAugmentions((_E,_u))
zxAnAdslLineAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())
adslAtucChanIntervalEntry.registerAugmentions((_E,_v))
zxAnAdslAtucChanIntervalEntry.setIndexNames(*adslAtucChanIntervalEntry.getIndexNames())
adslAturChanIntervalEntry.registerAugmentions((_E,_w))
zxAnAdslAturChanIntervalEntry.setIndexNames(*adslAturChanIntervalEntry.getIndexNames())
zxAnAdslAtuxConnRateOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,1))
zxAnAdslAtuxConnRateOverThreshTrap.setObjects(*((_F,_K),(_F,_L)))
if mibBuilder.loadTexts:zxAnAdslAtuxConnRateOverThreshTrap.setStatus(_A)
zxAnAdslAtuxConnRateUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,2))
zxAnAdslAtuxConnRateUnderThreshTrap.setObjects(*((_F,_K),(_F,_L)))
if mibBuilder.loadTexts:zxAnAdslAtuxConnRateUnderThreshTrap.setStatus(_A)
zxAnAdslAtucHighConnRateTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,3))
zxAnAdslAtucHighConnRateTrap.setObjects(*((_F,_K),(_F,_L),(_E,_T),(_E,_U)))
if mibBuilder.loadTexts:zxAnAdslAtucHighConnRateTrap.setStatus(_A)
zxAnAdslAtucHighConnRateClearTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,4))
zxAnAdslAtucHighConnRateClearTrap.setObjects(*((_F,_K),(_F,_L),(_E,_T),(_E,_U)))
if mibBuilder.loadTexts:zxAnAdslAtucHighConnRateClearTrap.setStatus(_A)
zxAnAdslAtucLowConnRateTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,5))
zxAnAdslAtucLowConnRateTrap.setObjects(*((_F,_K),(_F,_L),(_E,_V),(_E,_W)))
if mibBuilder.loadTexts:zxAnAdslAtucLowConnRateTrap.setStatus(_A)
zxAnAdslAtucLowConnRateClearTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,6))
zxAnAdslAtucLowConnRateClearTrap.setObjects(*((_F,_K),(_F,_L),(_E,_V),(_E,_W)))
if mibBuilder.loadTexts:zxAnAdslAtucLowConnRateClearTrap.setStatus(_A)
zxAnAdslAturHighConnRateTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,7))
zxAnAdslAturHighConnRateTrap.setObjects(*((_F,_O),(_F,_P),(_E,_X),(_E,_Y)))
if mibBuilder.loadTexts:zxAnAdslAturHighConnRateTrap.setStatus(_A)
zxAnAdslAturHighConnRateClearTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,8))
zxAnAdslAturHighConnRateClearTrap.setObjects(*((_F,_O),(_F,_P),(_E,_X),(_E,_Y)))
if mibBuilder.loadTexts:zxAnAdslAturHighConnRateClearTrap.setStatus(_A)
zxAnAdslAturLowConnRateTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,9))
zxAnAdslAturLowConnRateTrap.setObjects(*((_F,_O),(_F,_P),(_E,_Z),(_E,_a)))
if mibBuilder.loadTexts:zxAnAdslAturLowConnRateTrap.setStatus(_A)
zxAnAdslAturLowConnRateClearTrap=NotificationType((1,3,6,1,4,1,3902,1015,1000,2,10))
zxAnAdslAturLowConnRateClearTrap.setObjects(*((_F,_O),(_F,_P),(_E,_Z),(_E,_a)))
if mibBuilder.loadTexts:zxAnAdslAturLowConnRateClearTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zxAnAdslMib':zxAnAdslMib,'zxAnAdslMibObjects':zxAnAdslMibObjects,'zxAnAdslLineTable':zxAnAdslLineTable,'zxAnAdslLineEntry':zxAnAdslLineEntry,'zxAnAdslLineTxDataRate':zxAnAdslLineTxDataRate,'zxAnAdslLineRxDataRate':zxAnAdslLineRxDataRate,'zxAnAdslAtucActInp':zxAnAdslAtucActInp,'zxAnAdslAturActInp':zxAnAdslAturActInp,'zxAnAdslLineExtConfPrf':zxAnAdslLineExtConfPrf,'zxAnAdslLineConfProfileExtTable':zxAnAdslLineConfProfileExtTable,_t:zxAnAdslLineConfProfileExtEntry,'zxAnAdslLineConfTxStartBin':zxAnAdslLineConfTxStartBin,'zxAnAdslLineConfTxEndBin':zxAnAdslLineConfTxEndBin,'zxAnAdslLineConfRxStartBin':zxAnAdslLineConfRxStartBin,'zxAnAdslLineConfRxEndBin':zxAnAdslLineConfRxEndBin,'zxAnAdslLineConfUseCustomBins':zxAnAdslLineConfUseCustomBins,'zxAnAdslAtucConfPsdMaskType':zxAnAdslAtucConfPsdMaskType,'zxAnAdslLineConfPMMode':zxAnAdslLineConfPMMode,'zxAnAdslLineConfPML2Rate':zxAnAdslLineConfPML2Rate,'zxAnAdsl2ConfMinProtectionDs':zxAnAdsl2ConfMinProtectionDs,'zxAnAdslLineConfMinProtectionUs':zxAnAdslLineConfMinProtectionUs,'zxAnAdslConfDMTConfTrellis':zxAnAdslConfDMTConfTrellis,'zxAnAdslAtucConfMaxBitsPerBin':zxAnAdslAtucConfMaxBitsPerBin,'zxAnAdslAtucConfBitSwapDs':zxAnAdslAtucConfBitSwapDs,'zxAnAdslAtucConfBitSwapUs':zxAnAdslAtucConfBitSwapUs,'zxAnAdslAtucConfReAdsl2Enable':zxAnAdslAtucConfReAdsl2Enable,'zxAnAdslAtucConfPmL0Time':zxAnAdslAtucConfPmL0Time,'zxAnAdslAtucConfPmL2Time':zxAnAdslAtucConfPmL2Time,'zxAnAdslAtucConfPmL2Atpr':zxAnAdslAtucConfPmL2Atpr,'zxAdsl2ConfPsdMaskSelectUs':zxAdsl2ConfPsdMaskSelectUs,'zxAnAdslAtucChanTable':zxAnAdslAtucChanTable,'zxAnAdslAtucChanEntry':zxAnAdslAtucChanEntry,'zxAnAdslAtucChanInpEtr':zxAnAdslAtucChanInpEtr,'zxAnAdslAtucChanInpEftr':zxAnAdslAtucChanInpEftr,'zxAnAdslAtucChanInpMinEftr':zxAnAdslAtucChanInpMinEftr,'zxAnAdslAtucChanInpActDelay':zxAnAdslAtucChanInpActDelay,'zxAnAdslAturChanTable':zxAnAdslAturChanTable,'zxAnAdslAturChanEntry':zxAnAdslAturChanEntry,'zxAnAdslAturChanInpEtr':zxAnAdslAturChanInpEtr,'zxAnAdslAturChanInpEftr':zxAnAdslAturChanInpEftr,'zxAnAdslAturChanInpMinEftr':zxAnAdslAturChanInpMinEftr,'zxAnAdslAturChanInpActDelay':zxAnAdslAturChanInpActDelay,'zxAnAdslLineAlarmConfProfileExtTable':zxAnAdslLineAlarmConfProfileExtTable,_u:zxAnAdslLineAlarmConfProfileExtEntry,_W:zxAnAdslAtucConnRateTolerance,_a:zxAnAdslAturConnRateTolerance,_V:zxAnAdslAtucThreshConnRate,_Z:zxAnAdslAturThreshConnRate,_U:zxAnAdslMaxAtucConnRateTolerance,_Y:zxAnAdslMaxAturConnRateTolerance,_T:zxAnAdslMaxThreshAtucConnRate,_X:zxAnAdslMaxThreshAturConnRate,'zxAnAdslAturInitFailTrapEnable':zxAnAdslAturInitFailTrapEnable,'zxAnAdslThreshAtucInpLeftr':zxAnAdslThreshAtucInpLeftr,'zxAnAdslThreshAturInpLeftr':zxAnAdslThreshAturInpLeftr,'zxAnAdslAtucPerfDataTable':zxAnAdslAtucPerfDataTable,'zxAnAdslAtucPerfDataEntry':zxAnAdslAtucPerfDataEntry,'zxAnAdslAtucPerfDataFecs':zxAnAdslAtucPerfDataFecs,'zxAnAdslAtucPerfDataCurr15Fecs':zxAnAdslAtucPerfDataCurr15Fecs,'zxAnAdslAtucPerfDataCurr1DayFecs':zxAnAdslAtucPerfDataCurr1DayFecs,'zxAnAdslAtucPerfDataPrev1DayFecs':zxAnAdslAtucPerfDataPrev1DayFecs,'zxAnAdslAturPerfDataTable':zxAnAdslAturPerfDataTable,'zxAnAdslAturPerfDataEntry':zxAnAdslAturPerfDataEntry,'zxAnAdslAturPerfDataFecs':zxAnAdslAturPerfDataFecs,'zxAnAdslAturPerfDataCurr15Fecs':zxAnAdslAturPerfDataCurr15Fecs,'zxAnAdslAturPerfDataCurr1DayFecs':zxAnAdslAturPerfDataCurr1DayFecs,'zxAnAdslAturPerfDataPrev1DayFecs':zxAnAdslAturPerfDataPrev1DayFecs,'zxAnAdslAtucChanPerfDataTable':zxAnAdslAtucChanPerfDataTable,'zxAnAdslAtucChanPerfDataEntry':zxAnAdslAtucChanPerfDataEntry,'zxAnAtucChanPerfCurr15RtxDtu':zxAnAtucChanPerfCurr15RtxDtu,'zxAnAtucChanPerfCurr15RtxCDtu':zxAnAtucChanPerfCurr15RtxCDtu,'zxAnAtucChanPerfCurr15RtxUcDtu':zxAnAtucChanPerfCurr15RtxUcDtu,'zxAnAtucChanPerfCurr1DRtxDtu':zxAnAtucChanPerfCurr1DRtxDtu,'zxAnAtucChanPerfCurr1DRtxCDtu':zxAnAtucChanPerfCurr1DRtxCDtu,'zxAnAtucChanPerfCurr1DRtxUcDtu':zxAnAtucChanPerfCurr1DRtxUcDtu,'zxAnAdslAturChanPerfDataTable':zxAnAdslAturChanPerfDataTable,'zxAnAdslAturChanPerfDataEntry':zxAnAdslAturChanPerfDataEntry,'zxAnAturChanPerfCurr15RtxDtu':zxAnAturChanPerfCurr15RtxDtu,'zxAnAturChanPerfCurr15RtxCDtu':zxAnAturChanPerfCurr15RtxCDtu,'zxAnAturChanPerfCurr15RtxUcDtu':zxAnAturChanPerfCurr15RtxUcDtu,'zxAnAturChanPerfCurr1DRtxDtu':zxAnAturChanPerfCurr1DRtxDtu,'zxAnAturChanPerfCurr1DRtxCDtu':zxAnAturChanPerfCurr1DRtxCDtu,'zxAnAturChanPerfCurr1DRtxUcDtu':zxAnAturChanPerfCurr1DRtxUcDtu,'zxAnAdslAtucChanIntervalTable':zxAnAdslAtucChanIntervalTable,_v:zxAnAdslAtucChanIntervalEntry,'zxAnAdslAtucChanIntervalRtxDtu':zxAnAdslAtucChanIntervalRtxDtu,'zxAnAdslAtucChanIntervalRtxCDtu':zxAnAdslAtucChanIntervalRtxCDtu,'zxAnAdslAtucChanIntervalRtxUcDtu':zxAnAdslAtucChanIntervalRtxUcDtu,'zxAnAdslAturChanIntervalTable':zxAnAdslAturChanIntervalTable,_w:zxAnAdslAturChanIntervalEntry,'zxAnAdslAturChanIntervalRtxDtu':zxAnAdslAturChanIntervalRtxDtu,'zxAnAdslAturChanIntervalRtxCDtu':zxAnAdslAturChanIntervalRtxCDtu,'zxAnAdslAturChanIntervalRtxUcDtu':zxAnAdslAturChanIntervalRtxUcDtu,'zxAnAdslAtucChanHist1DayTable':zxAnAdslAtucChanHist1DayTable,'zxAnAdslAtucChanHist1DayEntry':zxAnAdslAtucChanHist1DayEntry,_m:zxAnAdslAtucChanHist1DayNumber,'zxAnAdslAtucChanHist1DayRtxDtu':zxAnAdslAtucChanHist1DayRtxDtu,'zxAnAdslAtucChanHist1DayRtxCDtu':zxAnAdslAtucChanHist1DayRtxCDtu,'zxAnAdslAtucChanHist1DayRtxUcDtu':zxAnAdslAtucChanHist1DayRtxUcDtu,'zxAnAdslAturChanHist1DayTable':zxAnAdslAturChanHist1DayTable,'zxAnAdslAturChanHist1DayEntry':zxAnAdslAturChanHist1DayEntry,_n:zxAnAdslAturChanHist1DayNumber,'zxAnAdslAturChanHist1DayRtxDtu':zxAnAdslAturChanHist1DayRtxDtu,'zxAnAdslAturChanHist1DayRtxCDtu':zxAnAdslAturChanHist1DayRtxCDtu,'zxAnAdslAturChanHist1DayRtxUcDtu':zxAnAdslAturChanHist1DayRtxUcDtu,'zxAnDslLoopBackTestTable':zxAnDslLoopBackTestTable,'zxAnDslLoopBackTestEntry':zxAnDslLoopBackTestEntry,_o:zxAnDslLoopBackTestRack,_p:zxAnDslLoopBackTestShelf,_q:zxAnDslLoopBackTestSlot,_r:zxAnDslLoopBackTestPort,_s:zxAnDslLoopBackTestBridgePort,'zxAnDslLoopBackTestType':zxAnDslLoopBackTestType,'zxAnDslLoopBackTestOperStatus':zxAnDslLoopBackTestOperStatus,'zxAnDslLoopBackTestResult':zxAnDslLoopBackTestResult,'zxAnDslLoopBackTestConfSendCells':zxAnDslLoopBackTestConfSendCells,'zxAnDslLoopBackTestResultRecivedCells':zxAnDslLoopBackTestResultRecivedCells,'zxAnDslLoopBackTestRowStatus':zxAnDslLoopBackTestRowStatus,'zxAnAdslTraps':zxAnAdslTraps,'zxAnAdslAtuxConnRateOverThreshTrap':zxAnAdslAtuxConnRateOverThreshTrap,'zxAnAdslAtuxConnRateUnderThreshTrap':zxAnAdslAtuxConnRateUnderThreshTrap,'zxAnAdslAtucHighConnRateTrap':zxAnAdslAtucHighConnRateTrap,'zxAnAdslAtucHighConnRateClearTrap':zxAnAdslAtucHighConnRateClearTrap,'zxAnAdslAtucLowConnRateTrap':zxAnAdslAtucLowConnRateTrap,'zxAnAdslAtucLowConnRateClearTrap':zxAnAdslAtucLowConnRateClearTrap,'zxAnAdslAturHighConnRateTrap':zxAnAdslAturHighConnRateTrap,'zxAnAdslAturHighConnRateClearTrap':zxAnAdslAturHighConnRateClearTrap,'zxAnAdslAturLowConnRateTrap':zxAnAdslAturLowConnRateTrap,'zxAnAdslAturLowConnRateClearTrap':zxAnAdslAturLowConnRateClearTrap})