_v='adslAturChanReceivedBlks'
_u='adslAturChanUncorrectBlks'
_t='adslAtucChanReceivedBlks'
_s='adslAtucChanUncorrectBlks'
_r='ifInBroadcastPkts'
_q='ifInMulticastPkts'
_p='ifInUcastPkts'
_o='ifInDiscards'
_n='ifOutBroadcastPkts'
_m='ifOutMulticastPkts'
_l='ifOutUcastPkts'
_k='ifOutDiscards'
_j='adslAturChanConfInterleaveMaxTxRate'
_i='adslAtucChanCurrTxRate'
_h='zxAdslLineAlarmConfProfileExtEntry'
_g='zxAdslLineConfProfileExtEntry'
_f='noSupport'
_e='zxDslLoopTestPort'
_d='symbols'
_c='sixteenSymbols'
_b='eightSymbols'
_a='fourSymbols'
_Z='twoSymbols'
_Y='singleSymbol'
_X='halfSymbol'
_W='noProtection'
_V='seconds'
_U='l3_Idle'
_T='l2_LowPower'
_S='l0_FullOn'
_R='SnmpAdminString'
_Q='zxAdslLineRxDataRate'
_P='zxAdslLineTxDataRate'
_O='Gauge32'
_N='adslAtucChanConfInterleaveMaxTxRate'
_M='tenth dB'
_L='disable'
_K='enable'
_J='deprecated'
_I='kbps'
_H='%'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='read-create'
_C='ZTE-DSL-LINE-EXT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslLineAlarmConfProfileEntry,adslLineConfProfileEntry,adslLineConfProfileName=mibBuilder.importSymbols('ADSL-LINE-MIB','adslLineAlarmConfProfileEntry','adslLineConfProfileEntry','adslLineConfProfileName')
ifIndex,=mibBuilder.importSymbols(_F,_G)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_O,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
zxAdslExtMib=ModuleIdentity((1,3,6,1,4,1,3902,1004,4))
_Zte_ObjectIdentity=ObjectIdentity
zte=_Zte_ObjectIdentity((1,3,6,1,4,1,3902))
_ZxDsl_ObjectIdentity=ObjectIdentity
zxDsl=_ZxDsl_ObjectIdentity((1,3,6,1,4,1,3902,1004))
_ZxAdslExtMibObjects_ObjectIdentity=ObjectIdentity
zxAdslExtMibObjects=_ZxAdslExtMibObjects_ObjectIdentity((1,3,6,1,4,1,3902,1004,4,1))
_ZxAdslLineTable_Object=MibTable
zxAdslLineTable=_ZxAdslLineTable_Object((1,3,6,1,4,1,3902,1004,4,1,1))
if mibBuilder.loadTexts:zxAdslLineTable.setStatus(_A)
_ZxAdslLineEntry_Object=MibTableRow
zxAdslLineEntry=_ZxAdslLineEntry_Object((1,3,6,1,4,1,3902,1004,4,1,1,1))
zxAdslLineEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslLineEntry.setStatus(_A)
class _ZxAdslLinePMConfPMSF_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_S,1),(_T,3),(_U,4)))
_ZxAdslLinePMConfPMSF_Type.__name__=_E
_ZxAdslLinePMConfPMSF_Object=MibTableColumn
zxAdslLinePMConfPMSF=_ZxAdslLinePMConfPMSF_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,1),_ZxAdslLinePMConfPMSF_Type())
zxAdslLinePMConfPMSF.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslLinePMConfPMSF.setStatus(_A)
class _ZxAdslLinePMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_S,1),('l1_LowPower',2),(_T,3),(_U,4)))
_ZxAdslLinePMState_Type.__name__=_E
_ZxAdslLinePMState_Object=MibTableColumn
zxAdslLinePMState=_ZxAdslLinePMState_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,2),_ZxAdslLinePMState_Type())
zxAdslLinePMState.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLinePMState.setStatus(_A)
class _ZxAdslLineDMTTrellis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unknown',0),('on',1),('off',2)))
_ZxAdslLineDMTTrellis_Type.__name__=_E
_ZxAdslLineDMTTrellis_Object=MibTableColumn
zxAdslLineDMTTrellis=_ZxAdslLineDMTTrellis_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,3),_ZxAdslLineDMTTrellis_Type())
zxAdslLineDMTTrellis.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLineDMTTrellis.setStatus(_J)
_ZxAdslLineTxAtmCells_Type=Counter32
_ZxAdslLineTxAtmCells_Object=MibTableColumn
zxAdslLineTxAtmCells=_ZxAdslLineTxAtmCells_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,4),_ZxAdslLineTxAtmCells_Type())
zxAdslLineTxAtmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLineTxAtmCells.setStatus(_A)
_ZxAdslLineRxAtmCells_Type=Counter32
_ZxAdslLineRxAtmCells_Object=MibTableColumn
zxAdslLineRxAtmCells=_ZxAdslLineRxAtmCells_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,5),_ZxAdslLineRxAtmCells_Type())
zxAdslLineRxAtmCells.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLineRxAtmCells.setStatus(_A)
_ZxAdslLineIdleCells_Type=Counter32
_ZxAdslLineIdleCells_Object=MibTableColumn
zxAdslLineIdleCells=_ZxAdslLineIdleCells_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,6),_ZxAdslLineIdleCells_Type())
zxAdslLineIdleCells.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLineIdleCells.setStatus(_A)
_ZxAdslLineTxDataRate_Type=Gauge32
_ZxAdslLineTxDataRate_Object=MibTableColumn
zxAdslLineTxDataRate=_ZxAdslLineTxDataRate_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,7),_ZxAdslLineTxDataRate_Type())
zxAdslLineTxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLineTxDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslLineTxDataRate.setUnits(_I)
_ZxAdslLineRxDataRate_Type=Gauge32
_ZxAdslLineRxDataRate_Object=MibTableColumn
zxAdslLineRxDataRate=_ZxAdslLineRxDataRate_Object((1,3,6,1,4,1,3902,1004,4,1,1,1,8),_ZxAdslLineRxDataRate_Type())
zxAdslLineRxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslLineRxDataRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslLineRxDataRate.setUnits(_I)
_ZxAdslLineConfProfileExtTable_Object=MibTable
zxAdslLineConfProfileExtTable=_ZxAdslLineConfProfileExtTable_Object((1,3,6,1,4,1,3902,1004,4,1,2))
if mibBuilder.loadTexts:zxAdslLineConfProfileExtTable.setStatus(_A)
_ZxAdslLineConfProfileExtEntry_Object=MibTableRow
zxAdslLineConfProfileExtEntry=_ZxAdslLineConfProfileExtEntry_Object((1,3,6,1,4,1,3902,1004,4,1,2,1))
if mibBuilder.loadTexts:zxAdslLineConfProfileExtEntry.setStatus(_A)
class _ZxAdslLineDMTConfTrellis_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_ZxAdslLineDMTConfTrellis_Type.__name__=_E
_ZxAdslLineDMTConfTrellis_Object=MibTableColumn
zxAdslLineDMTConfTrellis=_ZxAdslLineDMTConfTrellis_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,1),_ZxAdslLineDMTConfTrellis_Type())
zxAdslLineDMTConfTrellis.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslLineDMTConfTrellis.setStatus(_J)
class _ZxAdslAtucConfMaxBitsPerBin_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_ZxAdslAtucConfMaxBitsPerBin_Type.__name__=_E
_ZxAdslAtucConfMaxBitsPerBin_Object=MibTableColumn
zxAdslAtucConfMaxBitsPerBin=_ZxAdslAtucConfMaxBitsPerBin_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,2),_ZxAdslAtucConfMaxBitsPerBin_Type())
zxAdslAtucConfMaxBitsPerBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfMaxBitsPerBin.setStatus(_A)
_ZxAdslAtucConfTxStartBin_Type=Integer32
_ZxAdslAtucConfTxStartBin_Object=MibTableColumn
zxAdslAtucConfTxStartBin=_ZxAdslAtucConfTxStartBin_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,3),_ZxAdslAtucConfTxStartBin_Type())
zxAdslAtucConfTxStartBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfTxStartBin.setStatus(_A)
class _ZxAdslAtucConfTxEndBin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_ZxAdslAtucConfTxEndBin_Type.__name__=_E
_ZxAdslAtucConfTxEndBin_Object=MibTableColumn
zxAdslAtucConfTxEndBin=_ZxAdslAtucConfTxEndBin_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,4),_ZxAdslAtucConfTxEndBin_Type())
zxAdslAtucConfTxEndBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfTxEndBin.setStatus(_A)
_ZxAdslAtucConfRxStartBin_Type=Integer32
_ZxAdslAtucConfRxStartBin_Object=MibTableColumn
zxAdslAtucConfRxStartBin=_ZxAdslAtucConfRxStartBin_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,5),_ZxAdslAtucConfRxStartBin_Type())
zxAdslAtucConfRxStartBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfRxStartBin.setStatus(_A)
class _ZxAdslAtucConfRxEndBin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512))
_ZxAdslAtucConfRxEndBin_Type.__name__=_E
_ZxAdslAtucConfRxEndBin_Object=MibTableColumn
zxAdslAtucConfRxEndBin=_ZxAdslAtucConfRxEndBin_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,6),_ZxAdslAtucConfRxEndBin_Type())
zxAdslAtucConfRxEndBin.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfRxEndBin.setStatus(_A)
class _ZxAdslAtucConfUseCustomBins_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZxAdslAtucConfUseCustomBins_Type.__name__=_E
_ZxAdslAtucConfUseCustomBins_Object=MibTableColumn
zxAdslAtucConfUseCustomBins=_ZxAdslAtucConfUseCustomBins_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,7),_ZxAdslAtucConfUseCustomBins_Type())
zxAdslAtucConfUseCustomBins.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfUseCustomBins.setStatus(_A)
class _ZxAdslAtucConfDnBitSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZxAdslAtucConfDnBitSwap_Type.__name__=_E
_ZxAdslAtucConfDnBitSwap_Object=MibTableColumn
zxAdslAtucConfDnBitSwap=_ZxAdslAtucConfDnBitSwap_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,8),_ZxAdslAtucConfDnBitSwap_Type())
zxAdslAtucConfDnBitSwap.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfDnBitSwap.setStatus(_A)
class _ZxAdslAtucConfUpBitSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZxAdslAtucConfUpBitSwap_Type.__name__=_E
_ZxAdslAtucConfUpBitSwap_Object=MibTableColumn
zxAdslAtucConfUpBitSwap=_ZxAdslAtucConfUpBitSwap_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,9),_ZxAdslAtucConfUpBitSwap_Type())
zxAdslAtucConfUpBitSwap.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfUpBitSwap.setStatus(_A)
class _ZxAdslAtucConfREADSL2Enable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_ZxAdslAtucConfREADSL2Enable_Type.__name__=_E
_ZxAdslAtucConfREADSL2Enable_Object=MibTableColumn
zxAdslAtucConfREADSL2Enable=_ZxAdslAtucConfREADSL2Enable_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,10),_ZxAdslAtucConfREADSL2Enable_Type())
zxAdslAtucConfREADSL2Enable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfREADSL2Enable.setStatus(_J)
_ZxAdslAtucConfPsdMaskType_Type=Integer32
_ZxAdslAtucConfPsdMaskType_Object=MibTableColumn
zxAdslAtucConfPsdMaskType=_ZxAdslAtucConfPsdMaskType_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,11),_ZxAdslAtucConfPsdMaskType_Type())
zxAdslAtucConfPsdMaskType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfPsdMaskType.setStatus(_A)
class _ZxAdslAtucConfPMMode_Type(Bits):namedValues=NamedValues(*(('idle',0),('lowPower',1)))
_ZxAdslAtucConfPMMode_Type.__name__='Bits'
_ZxAdslAtucConfPMMode_Object=MibTableColumn
zxAdslAtucConfPMMode=_ZxAdslAtucConfPMMode_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,12),_ZxAdslAtucConfPMMode_Type())
zxAdslAtucConfPMMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfPMMode.setStatus(_A)
class _ZxAdslAtucConfPML0Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAdslAtucConfPML0Time_Type.__name__=_E
_ZxAdslAtucConfPML0Time_Object=MibTableColumn
zxAdslAtucConfPML0Time=_ZxAdslAtucConfPML0Time_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,13),_ZxAdslAtucConfPML0Time_Type())
zxAdslAtucConfPML0Time.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfPML0Time.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucConfPML0Time.setUnits(_V)
class _ZxAdslAtucConfPML2Time_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZxAdslAtucConfPML2Time_Type.__name__=_E
_ZxAdslAtucConfPML2Time_Object=MibTableColumn
zxAdslAtucConfPML2Time=_ZxAdslAtucConfPML2Time_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,14),_ZxAdslAtucConfPML2Time_Type())
zxAdslAtucConfPML2Time.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfPML2Time.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucConfPML2Time.setUnits(_V)
class _ZxAdslAtucConfPML2ATPR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_ZxAdslAtucConfPML2ATPR_Type.__name__=_E
_ZxAdslAtucConfPML2ATPR_Object=MibTableColumn
zxAdslAtucConfPML2ATPR=_ZxAdslAtucConfPML2ATPR_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,15),_ZxAdslAtucConfPML2ATPR_Type())
zxAdslAtucConfPML2ATPR.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfPML2ATPR.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucConfPML2ATPR.setUnits('dB')
class _ZxAdslAtucConfPML2Rate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1024))
_ZxAdslAtucConfPML2Rate_Type.__name__=_E
_ZxAdslAtucConfPML2Rate_Object=MibTableColumn
zxAdslAtucConfPML2Rate=_ZxAdslAtucConfPML2Rate_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,16),_ZxAdslAtucConfPML2Rate_Type())
zxAdslAtucConfPML2Rate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConfPML2Rate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucConfPML2Rate.setUnits(_I)
class _ZxAdsl2ConfMinProtectionDs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7)))
_ZxAdsl2ConfMinProtectionDs_Type.__name__=_E
_ZxAdsl2ConfMinProtectionDs_Object=MibTableColumn
zxAdsl2ConfMinProtectionDs=_ZxAdsl2ConfMinProtectionDs_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,20),_ZxAdsl2ConfMinProtectionDs_Type())
zxAdsl2ConfMinProtectionDs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdsl2ConfMinProtectionDs.setStatus(_A)
if mibBuilder.loadTexts:zxAdsl2ConfMinProtectionDs.setUnits(_d)
class _ZxAdsl2ConfMinProtectionUs_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6),(_c,7)))
_ZxAdsl2ConfMinProtectionUs_Type.__name__=_E
_ZxAdsl2ConfMinProtectionUs_Object=MibTableColumn
zxAdsl2ConfMinProtectionUs=_ZxAdsl2ConfMinProtectionUs_Object((1,3,6,1,4,1,3902,1004,4,1,2,1,21),_ZxAdsl2ConfMinProtectionUs_Type())
zxAdsl2ConfMinProtectionUs.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdsl2ConfMinProtectionUs.setStatus(_A)
if mibBuilder.loadTexts:zxAdsl2ConfMinProtectionUs.setUnits(_d)
_ZxAdslAtucPhysTable_Object=MibTable
zxAdslAtucPhysTable=_ZxAdslAtucPhysTable_Object((1,3,6,1,4,1,3902,1004,4,1,3))
if mibBuilder.loadTexts:zxAdslAtucPhysTable.setStatus(_A)
_ZxAdslAtucPhysEntry_Object=MibTableRow
zxAdslAtucPhysEntry=_ZxAdslAtucPhysEntry_Object((1,3,6,1,4,1,3902,1004,4,1,3,1))
zxAdslAtucPhysEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslAtucPhysEntry.setStatus(_A)
class _ZxAdslAtucPrevSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-640,640))
_ZxAdslAtucPrevSnrMgn_Type.__name__=_E
_ZxAdslAtucPrevSnrMgn_Object=MibTableColumn
zxAdslAtucPrevSnrMgn=_ZxAdslAtucPrevSnrMgn_Object((1,3,6,1,4,1,3902,1004,4,1,3,1,1),_ZxAdslAtucPrevSnrMgn_Type())
zxAdslAtucPrevSnrMgn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucPrevSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucPrevSnrMgn.setUnits(_M)
class _ZxAdslAtucPrevAtn_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,630))
_ZxAdslAtucPrevAtn_Type.__name__=_O
_ZxAdslAtucPrevAtn_Object=MibTableColumn
zxAdslAtucPrevAtn=_ZxAdslAtucPrevAtn_Object((1,3,6,1,4,1,3902,1004,4,1,3,1,2),_ZxAdslAtucPrevAtn_Type())
zxAdslAtucPrevAtn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucPrevAtn.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucPrevAtn.setUnits(_M)
_ZxAdslAtucPrevAttainableRate_Type=Gauge32
_ZxAdslAtucPrevAttainableRate_Object=MibTableColumn
zxAdslAtucPrevAttainableRate=_ZxAdslAtucPrevAttainableRate_Object((1,3,6,1,4,1,3902,1004,4,1,3,1,3),_ZxAdslAtucPrevAttainableRate_Type())
zxAdslAtucPrevAttainableRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucPrevAttainableRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucPrevAttainableRate.setUnits(_I)
class _ZxAdslAtucChipVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAdslAtucChipVersion_Type.__name__=_R
_ZxAdslAtucChipVersion_Object=MibTableColumn
zxAdslAtucChipVersion=_ZxAdslAtucChipVersion_Object((1,3,6,1,4,1,3902,1004,4,1,3,1,4),_ZxAdslAtucChipVersion_Type())
zxAdslAtucChipVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChipVersion.setStatus(_J)
_ZxAdslAturPhysTable_Object=MibTable
zxAdslAturPhysTable=_ZxAdslAturPhysTable_Object((1,3,6,1,4,1,3902,1004,4,1,4))
if mibBuilder.loadTexts:zxAdslAturPhysTable.setStatus(_A)
_ZxAdslAturPhysEntry_Object=MibTableRow
zxAdslAturPhysEntry=_ZxAdslAturPhysEntry_Object((1,3,6,1,4,1,3902,1004,4,1,4,1))
zxAdslAturPhysEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslAturPhysEntry.setStatus(_A)
class _ZxAdslAturPrevSnrMgn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-640,640))
_ZxAdslAturPrevSnrMgn_Type.__name__=_E
_ZxAdslAturPrevSnrMgn_Object=MibTableColumn
zxAdslAturPrevSnrMgn=_ZxAdslAturPrevSnrMgn_Object((1,3,6,1,4,1,3902,1004,4,1,4,1,1),_ZxAdslAturPrevSnrMgn_Type())
zxAdslAturPrevSnrMgn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturPrevSnrMgn.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAturPrevSnrMgn.setUnits(_M)
class _ZxAdslAturPrevAtn_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,630))
_ZxAdslAturPrevAtn_Type.__name__=_O
_ZxAdslAturPrevAtn_Object=MibTableColumn
zxAdslAturPrevAtn=_ZxAdslAturPrevAtn_Object((1,3,6,1,4,1,3902,1004,4,1,4,1,2),_ZxAdslAturPrevAtn_Type())
zxAdslAturPrevAtn.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturPrevAtn.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAturPrevAtn.setUnits(_M)
_ZxAdslAturPrevAttainableRate_Type=Gauge32
_ZxAdslAturPrevAttainableRate_Object=MibTableColumn
zxAdslAturPrevAttainableRate=_ZxAdslAturPrevAttainableRate_Object((1,3,6,1,4,1,3902,1004,4,1,4,1,3),_ZxAdslAturPrevAttainableRate_Type())
zxAdslAturPrevAttainableRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturPrevAttainableRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAturPrevAttainableRate.setUnits(_I)
_ZxAdslAtucChanTable_Object=MibTable
zxAdslAtucChanTable=_ZxAdslAtucChanTable_Object((1,3,6,1,4,1,3902,1004,4,1,5))
if mibBuilder.loadTexts:zxAdslAtucChanTable.setStatus(_A)
_ZxAdslAtucChanEntry_Object=MibTableRow
zxAdslAtucChanEntry=_ZxAdslAtucChanEntry_Object((1,3,6,1,4,1,3902,1004,4,1,5,1))
zxAdslAtucChanEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslAtucChanEntry.setStatus(_A)
_ZxAdslAtucChanRsSymbols_Type=Integer32
_ZxAdslAtucChanRsSymbols_Object=MibTableColumn
zxAdslAtucChanRsSymbols=_ZxAdslAtucChanRsSymbols_Object((1,3,6,1,4,1,3902,1004,4,1,5,1,1),_ZxAdslAtucChanRsSymbols_Type())
zxAdslAtucChanRsSymbols.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanRsSymbols.setStatus(_A)
_ZxAdslAtucChanRsDepth_Type=Integer32
_ZxAdslAtucChanRsDepth_Object=MibTableColumn
zxAdslAtucChanRsDepth=_ZxAdslAtucChanRsDepth_Object((1,3,6,1,4,1,3902,1004,4,1,5,1,2),_ZxAdslAtucChanRsDepth_Type())
zxAdslAtucChanRsDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanRsDepth.setStatus(_A)
_ZxAdslAtucChanRsRedundancy_Type=Integer32
_ZxAdslAtucChanRsRedundancy_Object=MibTableColumn
zxAdslAtucChanRsRedundancy=_ZxAdslAtucChanRsRedundancy_Object((1,3,6,1,4,1,3902,1004,4,1,5,1,3),_ZxAdslAtucChanRsRedundancy_Type())
zxAdslAtucChanRsRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanRsRedundancy.setStatus(_A)
_ZxAdslAturChanTable_Object=MibTable
zxAdslAturChanTable=_ZxAdslAturChanTable_Object((1,3,6,1,4,1,3902,1004,4,1,6))
if mibBuilder.loadTexts:zxAdslAturChanTable.setStatus(_A)
_ZxAdslAturChanEntry_Object=MibTableRow
zxAdslAturChanEntry=_ZxAdslAturChanEntry_Object((1,3,6,1,4,1,3902,1004,4,1,6,1))
zxAdslAturChanEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslAturChanEntry.setStatus(_A)
_ZxAdslAturChanRsSymbols_Type=Integer32
_ZxAdslAturChanRsSymbols_Object=MibTableColumn
zxAdslAturChanRsSymbols=_ZxAdslAturChanRsSymbols_Object((1,3,6,1,4,1,3902,1004,4,1,6,1,1),_ZxAdslAturChanRsSymbols_Type())
zxAdslAturChanRsSymbols.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanRsSymbols.setStatus(_A)
_ZxAdslAturChanRsDepth_Type=Integer32
_ZxAdslAturChanRsDepth_Object=MibTableColumn
zxAdslAturChanRsDepth=_ZxAdslAturChanRsDepth_Object((1,3,6,1,4,1,3902,1004,4,1,6,1,2),_ZxAdslAturChanRsDepth_Type())
zxAdslAturChanRsDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanRsDepth.setStatus(_A)
_ZxAdslAturChanRsRedundancy_Type=Integer32
_ZxAdslAturChanRsRedundancy_Object=MibTableColumn
zxAdslAturChanRsRedundancy=_ZxAdslAturChanRsRedundancy_Object((1,3,6,1,4,1,3902,1004,4,1,6,1,3),_ZxAdslAturChanRsRedundancy_Type())
zxAdslAturChanRsRedundancy.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanRsRedundancy.setStatus(_A)
_ZxAdslAtucChanPerfTable_Object=MibTable
zxAdslAtucChanPerfTable=_ZxAdslAtucChanPerfTable_Object((1,3,6,1,4,1,3902,1004,4,1,7))
if mibBuilder.loadTexts:zxAdslAtucChanPerfTable.setStatus(_A)
_ZxAdslAtucChanPerfEntry_Object=MibTableRow
zxAdslAtucChanPerfEntry=_ZxAdslAtucChanPerfEntry_Object((1,3,6,1,4,1,3902,1004,4,1,7,1))
zxAdslAtucChanPerfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslAtucChanPerfEntry.setStatus(_A)
_ZxAdslAtucChanPerfNcd_Type=Counter32
_ZxAdslAtucChanPerfNcd_Object=MibTableColumn
zxAdslAtucChanPerfNcd=_ZxAdslAtucChanPerfNcd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,1),_ZxAdslAtucChanPerfNcd_Type())
zxAdslAtucChanPerfNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfNcd.setStatus(_A)
_ZxAdslAtucChanPerfOcd_Type=Counter32
_ZxAdslAtucChanPerfOcd_Object=MibTableColumn
zxAdslAtucChanPerfOcd=_ZxAdslAtucChanPerfOcd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,2),_ZxAdslAtucChanPerfOcd_Type())
zxAdslAtucChanPerfOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfOcd.setStatus(_A)
_ZxAdslAtucChanPerfHec_Type=Counter32
_ZxAdslAtucChanPerfHec_Object=MibTableColumn
zxAdslAtucChanPerfHec=_ZxAdslAtucChanPerfHec_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,3),_ZxAdslAtucChanPerfHec_Type())
zxAdslAtucChanPerfHec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfHec.setStatus(_A)
_ZxAdslAtucChanPerfCurr15Ncd_Type=Counter32
_ZxAdslAtucChanPerfCurr15Ncd_Object=MibTableColumn
zxAdslAtucChanPerfCurr15Ncd=_ZxAdslAtucChanPerfCurr15Ncd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,4),_ZxAdslAtucChanPerfCurr15Ncd_Type())
zxAdslAtucChanPerfCurr15Ncd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfCurr15Ncd.setStatus(_A)
_ZxAdslAtucChanPerfCurr15Ocd_Type=Counter32
_ZxAdslAtucChanPerfCurr15Ocd_Object=MibTableColumn
zxAdslAtucChanPerfCurr15Ocd=_ZxAdslAtucChanPerfCurr15Ocd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,5),_ZxAdslAtucChanPerfCurr15Ocd_Type())
zxAdslAtucChanPerfCurr15Ocd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfCurr15Ocd.setStatus(_A)
_ZxAdslAtucChanPerfCurr15Hec_Type=Counter32
_ZxAdslAtucChanPerfCurr15Hec_Object=MibTableColumn
zxAdslAtucChanPerfCurr15Hec=_ZxAdslAtucChanPerfCurr15Hec_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,6),_ZxAdslAtucChanPerfCurr15Hec_Type())
zxAdslAtucChanPerfCurr15Hec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfCurr15Hec.setStatus(_A)
_ZxAdslAtucChanPerfCurr1DayNcd_Type=Counter32
_ZxAdslAtucChanPerfCurr1DayNcd_Object=MibTableColumn
zxAdslAtucChanPerfCurr1DayNcd=_ZxAdslAtucChanPerfCurr1DayNcd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,7),_ZxAdslAtucChanPerfCurr1DayNcd_Type())
zxAdslAtucChanPerfCurr1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfCurr1DayNcd.setStatus(_A)
_ZxAdslAtucChanPerfCurr1DayOcd_Type=Counter32
_ZxAdslAtucChanPerfCurr1DayOcd_Object=MibTableColumn
zxAdslAtucChanPerfCurr1DayOcd=_ZxAdslAtucChanPerfCurr1DayOcd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,8),_ZxAdslAtucChanPerfCurr1DayOcd_Type())
zxAdslAtucChanPerfCurr1DayOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfCurr1DayOcd.setStatus(_A)
_ZxAdslAtucChanPerfCurr1DayHec_Type=Counter32
_ZxAdslAtucChanPerfCurr1DayHec_Object=MibTableColumn
zxAdslAtucChanPerfCurr1DayHec=_ZxAdslAtucChanPerfCurr1DayHec_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,9),_ZxAdslAtucChanPerfCurr1DayHec_Type())
zxAdslAtucChanPerfCurr1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfCurr1DayHec.setStatus(_A)
_ZxAdslAtucChanPerfPrev1DayNcd_Type=Counter32
_ZxAdslAtucChanPerfPrev1DayNcd_Object=MibTableColumn
zxAdslAtucChanPerfPrev1DayNcd=_ZxAdslAtucChanPerfPrev1DayNcd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,10),_ZxAdslAtucChanPerfPrev1DayNcd_Type())
zxAdslAtucChanPerfPrev1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfPrev1DayNcd.setStatus(_A)
_ZxAdslAtucChanPerfPrev1DayOcd_Type=Counter32
_ZxAdslAtucChanPerfPrev1DayOcd_Object=MibTableColumn
zxAdslAtucChanPerfPrev1DayOcd=_ZxAdslAtucChanPerfPrev1DayOcd_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,11),_ZxAdslAtucChanPerfPrev1DayOcd_Type())
zxAdslAtucChanPerfPrev1DayOcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfPrev1DayOcd.setStatus(_A)
_ZxAdslAtucChanPerfPrev1DayHec_Type=Counter32
_ZxAdslAtucChanPerfPrev1DayHec_Object=MibTableColumn
zxAdslAtucChanPerfPrev1DayHec=_ZxAdslAtucChanPerfPrev1DayHec_Object((1,3,6,1,4,1,3902,1004,4,1,7,1,12),_ZxAdslAtucChanPerfPrev1DayHec_Type())
zxAdslAtucChanPerfPrev1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAtucChanPerfPrev1DayHec.setStatus(_A)
_ZxAdslAturChanPerfTable_Object=MibTable
zxAdslAturChanPerfTable=_ZxAdslAturChanPerfTable_Object((1,3,6,1,4,1,3902,1004,4,1,8))
if mibBuilder.loadTexts:zxAdslAturChanPerfTable.setStatus(_A)
_ZxAdslAturChanPerfEntry_Object=MibTableRow
zxAdslAturChanPerfEntry=_ZxAdslAturChanPerfEntry_Object((1,3,6,1,4,1,3902,1004,4,1,8,1))
zxAdslAturChanPerfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zxAdslAturChanPerfEntry.setStatus(_A)
_ZxAdslAturChanPerfNcd_Type=Counter32
_ZxAdslAturChanPerfNcd_Object=MibTableColumn
zxAdslAturChanPerfNcd=_ZxAdslAturChanPerfNcd_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,1),_ZxAdslAturChanPerfNcd_Type())
zxAdslAturChanPerfNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfNcd.setStatus(_A)
_ZxAdslAturChanPerfHec_Type=Counter32
_ZxAdslAturChanPerfHec_Object=MibTableColumn
zxAdslAturChanPerfHec=_ZxAdslAturChanPerfHec_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,2),_ZxAdslAturChanPerfHec_Type())
zxAdslAturChanPerfHec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfHec.setStatus(_A)
_ZxAdslAturChanPerfCurr15Ncd_Type=Counter32
_ZxAdslAturChanPerfCurr15Ncd_Object=MibTableColumn
zxAdslAturChanPerfCurr15Ncd=_ZxAdslAturChanPerfCurr15Ncd_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,3),_ZxAdslAturChanPerfCurr15Ncd_Type())
zxAdslAturChanPerfCurr15Ncd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfCurr15Ncd.setStatus(_A)
_ZxAdslAturChanPerfCurr15Hec_Type=Counter32
_ZxAdslAturChanPerfCurr15Hec_Object=MibTableColumn
zxAdslAturChanPerfCurr15Hec=_ZxAdslAturChanPerfCurr15Hec_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,4),_ZxAdslAturChanPerfCurr15Hec_Type())
zxAdslAturChanPerfCurr15Hec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfCurr15Hec.setStatus(_A)
_ZxAdslAturChanPerfCurr1DayNcd_Type=Counter32
_ZxAdslAturChanPerfCurr1DayNcd_Object=MibTableColumn
zxAdslAturChanPerfCurr1DayNcd=_ZxAdslAturChanPerfCurr1DayNcd_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,5),_ZxAdslAturChanPerfCurr1DayNcd_Type())
zxAdslAturChanPerfCurr1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfCurr1DayNcd.setStatus(_A)
_ZxAdslAturChanPerfCurr1DayHec_Type=Counter32
_ZxAdslAturChanPerfCurr1DayHec_Object=MibTableColumn
zxAdslAturChanPerfCurr1DayHec=_ZxAdslAturChanPerfCurr1DayHec_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,6),_ZxAdslAturChanPerfCurr1DayHec_Type())
zxAdslAturChanPerfCurr1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfCurr1DayHec.setStatus(_A)
_ZxAdslAturChanPerfPrev1DayNcd_Type=Counter32
_ZxAdslAturChanPerfPrev1DayNcd_Object=MibTableColumn
zxAdslAturChanPerfPrev1DayNcd=_ZxAdslAturChanPerfPrev1DayNcd_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,7),_ZxAdslAturChanPerfPrev1DayNcd_Type())
zxAdslAturChanPerfPrev1DayNcd.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfPrev1DayNcd.setStatus(_A)
_ZxAdslAturChanPerfPrev1DayHec_Type=Counter32
_ZxAdslAturChanPerfPrev1DayHec_Object=MibTableColumn
zxAdslAturChanPerfPrev1DayHec=_ZxAdslAturChanPerfPrev1DayHec_Object((1,3,6,1,4,1,3902,1004,4,1,8,1,8),_ZxAdslAturChanPerfPrev1DayHec_Type())
zxAdslAturChanPerfPrev1DayHec.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslAturChanPerfPrev1DayHec.setStatus(_A)
_ZxDslLoopTestTable_Object=MibTable
zxDslLoopTestTable=_ZxDslLoopTestTable_Object((1,3,6,1,4,1,3902,1004,4,1,9))
if mibBuilder.loadTexts:zxDslLoopTestTable.setStatus(_A)
_ZxDslLoopTestEntry_Object=MibTableRow
zxDslLoopTestEntry=_ZxDslLoopTestEntry_Object((1,3,6,1,4,1,3902,1004,4,1,9,1))
zxDslLoopTestEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:zxDslLoopTestEntry.setStatus(_A)
_ZxDslLoopTestPort_Type=Integer32
_ZxDslLoopTestPort_Object=MibTableColumn
zxDslLoopTestPort=_ZxDslLoopTestPort_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,1),_ZxDslLoopTestPort_Type())
zxDslLoopTestPort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zxDslLoopTestPort.setStatus(_A)
class _ZxDslLoopTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*(('noOper',0),('cancle',1),('utopia',2),('afe',3),('hybrid',4),('atuc_OAM',5),('atur_OAM',6)))
_ZxDslLoopTestType_Type.__name__=_E
_ZxDslLoopTestType_Object=MibTableColumn
zxDslLoopTestType=_ZxDslLoopTestType_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,2),_ZxDslLoopTestType_Type())
zxDslLoopTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestType.setStatus(_A)
class _ZxDslLoopTestOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('neverExcute',0),('excuting',1),('excuted',2),('faliedToCommit',3)))
_ZxDslLoopTestOperStatus_Type.__name__=_E
_ZxDslLoopTestOperStatus_Object=MibTableColumn
zxDslLoopTestOperStatus=_ZxDslLoopTestOperStatus_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,3),_ZxDslLoopTestOperStatus_Type())
zxDslLoopTestOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestOperStatus.setStatus(_A)
class _ZxDslLoopTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('NoResult',0),('Success',1),('GeneralFailed',2),('NoSupport',3),('Unkown',4),('NoSuchPort',5),('LoopBackFailed',6),('PortNotActive',7),('PortInTesting',8),('PortInService',9),('PortFailures',10),('CardFailures',11),('NoPvcFound',12),('UnknownTestType',13)))
_ZxDslLoopTestResult_Type.__name__=_E
_ZxDslLoopTestResult_Object=MibTableColumn
zxDslLoopTestResult=_ZxDslLoopTestResult_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,4),_ZxDslLoopTestResult_Type())
zxDslLoopTestResult.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestResult.setStatus(_A)
_ZxDslLoopTestConfParam1_Type=Integer32
_ZxDslLoopTestConfParam1_Object=MibTableColumn
zxDslLoopTestConfParam1=_ZxDslLoopTestConfParam1_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,5),_ZxDslLoopTestConfParam1_Type())
zxDslLoopTestConfParam1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestConfParam1.setStatus(_A)
_ZxDslLoopTestConfParam2_Type=Integer32
_ZxDslLoopTestConfParam2_Object=MibTableColumn
zxDslLoopTestConfParam2=_ZxDslLoopTestConfParam2_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,6),_ZxDslLoopTestConfParam2_Type())
zxDslLoopTestConfParam2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestConfParam2.setStatus(_A)
_ZxDslLoopTestConfParam3_Type=Integer32
_ZxDslLoopTestConfParam3_Object=MibTableColumn
zxDslLoopTestConfParam3=_ZxDslLoopTestConfParam3_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,7),_ZxDslLoopTestConfParam3_Type())
zxDslLoopTestConfParam3.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestConfParam3.setStatus(_A)
_ZxDslLoopTestConfParam4_Type=Integer32
_ZxDslLoopTestConfParam4_Object=MibTableColumn
zxDslLoopTestConfParam4=_ZxDslLoopTestConfParam4_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,8),_ZxDslLoopTestConfParam4_Type())
zxDslLoopTestConfParam4.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestConfParam4.setStatus(_A)
_ZxDslLoopTestConfParam5_Type=Integer32
_ZxDslLoopTestConfParam5_Object=MibTableColumn
zxDslLoopTestConfParam5=_ZxDslLoopTestConfParam5_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,9),_ZxDslLoopTestConfParam5_Type())
zxDslLoopTestConfParam5.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestConfParam5.setStatus(_A)
_ZxDslLoopTestResultParam1_Type=Integer32
_ZxDslLoopTestResultParam1_Object=MibTableColumn
zxDslLoopTestResultParam1=_ZxDslLoopTestResultParam1_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,10),_ZxDslLoopTestResultParam1_Type())
zxDslLoopTestResultParam1.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestResultParam1.setStatus(_A)
_ZxDslLoopTestResultParam2_Type=Integer32
_ZxDslLoopTestResultParam2_Object=MibTableColumn
zxDslLoopTestResultParam2=_ZxDslLoopTestResultParam2_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,11),_ZxDslLoopTestResultParam2_Type())
zxDslLoopTestResultParam2.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestResultParam2.setStatus(_A)
_ZxDslLoopTestResultParam3_Type=Integer32
_ZxDslLoopTestResultParam3_Object=MibTableColumn
zxDslLoopTestResultParam3=_ZxDslLoopTestResultParam3_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,12),_ZxDslLoopTestResultParam3_Type())
zxDslLoopTestResultParam3.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestResultParam3.setStatus(_A)
_ZxDslLoopTestResultParam4_Type=Integer32
_ZxDslLoopTestResultParam4_Object=MibTableColumn
zxDslLoopTestResultParam4=_ZxDslLoopTestResultParam4_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,13),_ZxDslLoopTestResultParam4_Type())
zxDslLoopTestResultParam4.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestResultParam4.setStatus(_A)
_ZxDslLoopTestResultParam5_Type=Integer32
_ZxDslLoopTestResultParam5_Object=MibTableColumn
zxDslLoopTestResultParam5=_ZxDslLoopTestResultParam5_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,14),_ZxDslLoopTestResultParam5_Type())
zxDslLoopTestResultParam5.setMaxAccess(_B)
if mibBuilder.loadTexts:zxDslLoopTestResultParam5.setStatus(_A)
_ZxDslLoopTestRowStatus_Type=RowStatus
_ZxDslLoopTestRowStatus_Object=MibTableColumn
zxDslLoopTestRowStatus=_ZxDslLoopTestRowStatus_Object((1,3,6,1,4,1,3902,1004,4,1,9,1,15),_ZxDslLoopTestRowStatus_Type())
zxDslLoopTestRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:zxDslLoopTestRowStatus.setStatus(_A)
class _ZxAdslIsSupportAdsl2Plus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('support',1),(_f,2)))
_ZxAdslIsSupportAdsl2Plus_Type.__name__=_E
_ZxAdslIsSupportAdsl2Plus_Object=MibScalar
zxAdslIsSupportAdsl2Plus=_ZxAdslIsSupportAdsl2Plus_Object((1,3,6,1,4,1,3902,1004,4,1,11),_ZxAdslIsSupportAdsl2Plus_Type())
zxAdslIsSupportAdsl2Plus.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslIsSupportAdsl2Plus.setStatus(_A)
class _ZxAdslIsSupportAdslRateThresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('Support',1),(_f,2)))
_ZxAdslIsSupportAdslRateThresh_Type.__name__=_E
_ZxAdslIsSupportAdslRateThresh_Object=MibScalar
zxAdslIsSupportAdslRateThresh=_ZxAdslIsSupportAdslRateThresh_Object((1,3,6,1,4,1,3902,1004,4,1,14),_ZxAdslIsSupportAdslRateThresh_Type())
zxAdslIsSupportAdslRateThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:zxAdslIsSupportAdslRateThresh.setStatus(_A)
_ZxAdslLineAlarmConfProfileExtTable_Object=MibTable
zxAdslLineAlarmConfProfileExtTable=_ZxAdslLineAlarmConfProfileExtTable_Object((1,3,6,1,4,1,3902,1004,4,1,20))
if mibBuilder.loadTexts:zxAdslLineAlarmConfProfileExtTable.setStatus(_A)
_ZxAdslLineAlarmConfProfileExtEntry_Object=MibTableRow
zxAdslLineAlarmConfProfileExtEntry=_ZxAdslLineAlarmConfProfileExtEntry_Object((1,3,6,1,4,1,3902,1004,4,1,20,1))
if mibBuilder.loadTexts:zxAdslLineAlarmConfProfileExtEntry.setStatus(_A)
class _ZxAdslAtucConnRateTolerance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslAtucConnRateTolerance_Type.__name__=_E
_ZxAdslAtucConnRateTolerance_Object=MibTableColumn
zxAdslAtucConnRateTolerance=_ZxAdslAtucConnRateTolerance_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,1),_ZxAdslAtucConnRateTolerance_Type())
zxAdslAtucConnRateTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAtucConnRateTolerance.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAtucConnRateTolerance.setUnits(_H)
class _ZxAdslAturConnRateTolerance_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslAturConnRateTolerance_Type.__name__=_E
_ZxAdslAturConnRateTolerance_Object=MibTableColumn
zxAdslAturConnRateTolerance=_ZxAdslAturConnRateTolerance_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,2),_ZxAdslAturConnRateTolerance_Type())
zxAdslAturConnRateTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslAturConnRateTolerance.setStatus(_A)
if mibBuilder.loadTexts:zxAdslAturConnRateTolerance.setUnits(_H)
class _ZxAdslThreshAtucConnRate_Type(Integer32):defaultValue=0
_ZxAdslThreshAtucConnRate_Type.__name__=_E
_ZxAdslThreshAtucConnRate_Object=MibTableColumn
zxAdslThreshAtucConnRate=_ZxAdslThreshAtucConnRate_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,3),_ZxAdslThreshAtucConnRate_Type())
zxAdslThreshAtucConnRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAtucConnRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAtucConnRate.setUnits(_I)
class _ZxAdslThreshAturConnRate_Type(Integer32):defaultValue=0
_ZxAdslThreshAturConnRate_Type.__name__=_E
_ZxAdslThreshAturConnRate_Object=MibTableColumn
zxAdslThreshAturConnRate=_ZxAdslThreshAturConnRate_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,4),_ZxAdslThreshAturConnRate_Type())
zxAdslThreshAturConnRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAturConnRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAturConnRate.setUnits(_I)
class _ZxAdslThreshAtucBandwidthUtil_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshAtucBandwidthUtil_Type.__name__=_E
_ZxAdslThreshAtucBandwidthUtil_Object=MibTableColumn
zxAdslThreshAtucBandwidthUtil=_ZxAdslThreshAtucBandwidthUtil_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,5),_ZxAdslThreshAtucBandwidthUtil_Type())
zxAdslThreshAtucBandwidthUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAtucBandwidthUtil.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAtucBandwidthUtil.setUnits(_H)
class _ZxAdslThreshAturBandwidthUtil_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshAturBandwidthUtil_Type.__name__=_E
_ZxAdslThreshAturBandwidthUtil_Object=MibTableColumn
zxAdslThreshAturBandwidthUtil=_ZxAdslThreshAturBandwidthUtil_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,6),_ZxAdslThreshAturBandwidthUtil_Type())
zxAdslThreshAturBandwidthUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAturBandwidthUtil.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAturBandwidthUtil.setUnits(_H)
class _ZxAdslThreshAtucPacketLossRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshAtucPacketLossRate_Type.__name__=_E
_ZxAdslThreshAtucPacketLossRate_Object=MibTableColumn
zxAdslThreshAtucPacketLossRate=_ZxAdslThreshAtucPacketLossRate_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,7),_ZxAdslThreshAtucPacketLossRate_Type())
zxAdslThreshAtucPacketLossRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAtucPacketLossRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAtucPacketLossRate.setUnits(_H)
class _ZxAdslThreshAturPacketLossRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshAturPacketLossRate_Type.__name__=_E
_ZxAdslThreshAturPacketLossRate_Object=MibTableColumn
zxAdslThreshAturPacketLossRate=_ZxAdslThreshAturPacketLossRate_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,8),_ZxAdslThreshAturPacketLossRate_Type())
zxAdslThreshAturPacketLossRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAturPacketLossRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAturPacketLossRate.setUnits(_H)
class _ZxAdslThreshAtucBlockErrorRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshAtucBlockErrorRate_Type.__name__=_E
_ZxAdslThreshAtucBlockErrorRate_Object=MibTableColumn
zxAdslThreshAtucBlockErrorRate=_ZxAdslThreshAtucBlockErrorRate_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,9),_ZxAdslThreshAtucBlockErrorRate_Type())
zxAdslThreshAtucBlockErrorRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAtucBlockErrorRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAtucBlockErrorRate.setUnits(_H)
class _ZxAdslThreshAturBlockErrorRate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshAturBlockErrorRate_Type.__name__=_E
_ZxAdslThreshAturBlockErrorRate_Object=MibTableColumn
zxAdslThreshAturBlockErrorRate=_ZxAdslThreshAturBlockErrorRate_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,10),_ZxAdslThreshAturBlockErrorRate_Type())
zxAdslThreshAturBlockErrorRate.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshAturBlockErrorRate.setStatus(_A)
if mibBuilder.loadTexts:zxAdslThreshAturBlockErrorRate.setUnits(_H)
class _ZxAdslThreshReservedMetric1_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshReservedMetric1_Type.__name__=_E
_ZxAdslThreshReservedMetric1_Object=MibTableColumn
zxAdslThreshReservedMetric1=_ZxAdslThreshReservedMetric1_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,11),_ZxAdslThreshReservedMetric1_Type())
zxAdslThreshReservedMetric1.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshReservedMetric1.setStatus(_A)
class _ZxAdslThreshReservedMetric2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshReservedMetric2_Type.__name__=_E
_ZxAdslThreshReservedMetric2_Object=MibTableColumn
zxAdslThreshReservedMetric2=_ZxAdslThreshReservedMetric2_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,12),_ZxAdslThreshReservedMetric2_Type())
zxAdslThreshReservedMetric2.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshReservedMetric2.setStatus(_A)
class _ZxAdslThreshReservedMetric3_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ZxAdslThreshReservedMetric3_Type.__name__=_E
_ZxAdslThreshReservedMetric3_Object=MibTableColumn
zxAdslThreshReservedMetric3=_ZxAdslThreshReservedMetric3_Object((1,3,6,1,4,1,3902,1004,4,1,20,1,13),_ZxAdslThreshReservedMetric3_Type())
zxAdslThreshReservedMetric3.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAdslThreshReservedMetric3.setStatus(_A)
_ZxAdslExtTraps_ObjectIdentity=ObjectIdentity
zxAdslExtTraps=_ZxAdslExtTraps_ObjectIdentity((1,3,6,1,4,1,3902,1004,4,2))
adslLineConfProfileEntry.registerAugmentions((_C,_g))
zxAdslLineConfProfileExtEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())
adslLineAlarmConfProfileEntry.registerAugmentions((_C,_h))
zxAdslLineAlarmConfProfileExtEntry.setIndexNames(*adslLineAlarmConfProfileEntry.getIndexNames())
zxAdslAtuxConnRateOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,1))
zxAdslAtuxConnRateOverThreshTrap.setObjects(*((_C,_N),(_C,_i)))
if mibBuilder.loadTexts:zxAdslAtuxConnRateOverThreshTrap.setStatus(_A)
zxAdslAtuxConnRateUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,2))
zxAdslAtuxConnRateUnderThreshTrap.setObjects(*((_C,_N),(_C,_i)))
if mibBuilder.loadTexts:zxAdslAtuxConnRateUnderThreshTrap.setStatus(_A)
zxAdslAtucBandwidthUtilOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,5))
zxAdslAtucBandwidthUtilOverThreshTrap.setObjects(*((_C,_N),(_C,_P)))
if mibBuilder.loadTexts:zxAdslAtucBandwidthUtilOverThreshTrap.setStatus(_A)
zxAdslAtucBandwidthUtilUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,6))
zxAdslAtucBandwidthUtilUnderThreshTrap.setObjects(*((_C,_N),(_C,_P)))
if mibBuilder.loadTexts:zxAdslAtucBandwidthUtilUnderThreshTrap.setStatus(_A)
zxAdslAturBandwidthUtilOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,7))
zxAdslAturBandwidthUtilOverThreshTrap.setObjects(*((_C,_j),(_C,_Q)))
if mibBuilder.loadTexts:zxAdslAturBandwidthUtilOverThreshTrap.setStatus(_A)
zxAdslAturBandwidthUtilUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,8))
zxAdslAturBandwidthUtilUnderThreshTrap.setObjects(*((_C,_j),(_C,_Q)))
if mibBuilder.loadTexts:zxAdslAturBandwidthUtilUnderThreshTrap.setStatus(_A)
zxAdslAtucPacketLossRateOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,9))
zxAdslAtucPacketLossRateOverThreshTrap.setObjects(*((_C,_k),(_C,_l),(_C,_m),(_C,_n)))
if mibBuilder.loadTexts:zxAdslAtucPacketLossRateOverThreshTrap.setStatus(_A)
zxAdslAtucPacketLossRateUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,10))
zxAdslAtucPacketLossRateUnderThreshTrap.setObjects(*((_C,_k),(_C,_l),(_C,_m),(_C,_n)))
if mibBuilder.loadTexts:zxAdslAtucPacketLossRateUnderThreshTrap.setStatus(_A)
zxAdslAturPacketLossRateOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,11))
zxAdslAturPacketLossRateOverThreshTrap.setObjects(*((_C,_o),(_C,_p),(_C,_q),(_C,_r)))
if mibBuilder.loadTexts:zxAdslAturPacketLossRateOverThreshTrap.setStatus(_A)
zxAdslAturPacketLossRateUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,12))
zxAdslAturPacketLossRateUnderThreshTrap.setObjects(*((_C,_o),(_C,_p),(_C,_q),(_C,_r)))
if mibBuilder.loadTexts:zxAdslAturPacketLossRateUnderThreshTrap.setStatus(_A)
zxAdslAtucBlockErrorRateOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,13))
zxAdslAtucBlockErrorRateOverThreshTrap.setObjects(*((_C,_s),(_C,_t)))
if mibBuilder.loadTexts:zxAdslAtucBlockErrorRateOverThreshTrap.setStatus(_A)
zxAdslAtucBlockErrorRateUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,14))
zxAdslAtucBlockErrorRateUnderThreshTrap.setObjects(*((_C,_s),(_C,_t)))
if mibBuilder.loadTexts:zxAdslAtucBlockErrorRateUnderThreshTrap.setStatus(_A)
zxAdslAturBlockErrorRateOverThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,15))
zxAdslAturBlockErrorRateOverThreshTrap.setObjects(*((_C,_u),(_C,_v)))
if mibBuilder.loadTexts:zxAdslAturBlockErrorRateOverThreshTrap.setStatus(_A)
zxAdslAturBlockErrorRateUnderThreshTrap=NotificationType((1,3,6,1,4,1,3902,1004,4,2,16))
zxAdslAturBlockErrorRateUnderThreshTrap.setObjects(*((_C,_u),(_C,_v)))
if mibBuilder.loadTexts:zxAdslAturBlockErrorRateUnderThreshTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zte':zte,'zxDsl':zxDsl,'zxAdslExtMib':zxAdslExtMib,'zxAdslExtMibObjects':zxAdslExtMibObjects,'zxAdslLineTable':zxAdslLineTable,'zxAdslLineEntry':zxAdslLineEntry,'zxAdslLinePMConfPMSF':zxAdslLinePMConfPMSF,'zxAdslLinePMState':zxAdslLinePMState,'zxAdslLineDMTTrellis':zxAdslLineDMTTrellis,'zxAdslLineTxAtmCells':zxAdslLineTxAtmCells,'zxAdslLineRxAtmCells':zxAdslLineRxAtmCells,'zxAdslLineIdleCells':zxAdslLineIdleCells,_P:zxAdslLineTxDataRate,_Q:zxAdslLineRxDataRate,'zxAdslLineConfProfileExtTable':zxAdslLineConfProfileExtTable,_g:zxAdslLineConfProfileExtEntry,'zxAdslLineDMTConfTrellis':zxAdslLineDMTConfTrellis,'zxAdslAtucConfMaxBitsPerBin':zxAdslAtucConfMaxBitsPerBin,'zxAdslAtucConfTxStartBin':zxAdslAtucConfTxStartBin,'zxAdslAtucConfTxEndBin':zxAdslAtucConfTxEndBin,'zxAdslAtucConfRxStartBin':zxAdslAtucConfRxStartBin,'zxAdslAtucConfRxEndBin':zxAdslAtucConfRxEndBin,'zxAdslAtucConfUseCustomBins':zxAdslAtucConfUseCustomBins,'zxAdslAtucConfDnBitSwap':zxAdslAtucConfDnBitSwap,'zxAdslAtucConfUpBitSwap':zxAdslAtucConfUpBitSwap,'zxAdslAtucConfREADSL2Enable':zxAdslAtucConfREADSL2Enable,'zxAdslAtucConfPsdMaskType':zxAdslAtucConfPsdMaskType,'zxAdslAtucConfPMMode':zxAdslAtucConfPMMode,'zxAdslAtucConfPML0Time':zxAdslAtucConfPML0Time,'zxAdslAtucConfPML2Time':zxAdslAtucConfPML2Time,'zxAdslAtucConfPML2ATPR':zxAdslAtucConfPML2ATPR,'zxAdslAtucConfPML2Rate':zxAdslAtucConfPML2Rate,'zxAdsl2ConfMinProtectionDs':zxAdsl2ConfMinProtectionDs,'zxAdsl2ConfMinProtectionUs':zxAdsl2ConfMinProtectionUs,'zxAdslAtucPhysTable':zxAdslAtucPhysTable,'zxAdslAtucPhysEntry':zxAdslAtucPhysEntry,'zxAdslAtucPrevSnrMgn':zxAdslAtucPrevSnrMgn,'zxAdslAtucPrevAtn':zxAdslAtucPrevAtn,'zxAdslAtucPrevAttainableRate':zxAdslAtucPrevAttainableRate,'zxAdslAtucChipVersion':zxAdslAtucChipVersion,'zxAdslAturPhysTable':zxAdslAturPhysTable,'zxAdslAturPhysEntry':zxAdslAturPhysEntry,'zxAdslAturPrevSnrMgn':zxAdslAturPrevSnrMgn,'zxAdslAturPrevAtn':zxAdslAturPrevAtn,'zxAdslAturPrevAttainableRate':zxAdslAturPrevAttainableRate,'zxAdslAtucChanTable':zxAdslAtucChanTable,'zxAdslAtucChanEntry':zxAdslAtucChanEntry,'zxAdslAtucChanRsSymbols':zxAdslAtucChanRsSymbols,'zxAdslAtucChanRsDepth':zxAdslAtucChanRsDepth,'zxAdslAtucChanRsRedundancy':zxAdslAtucChanRsRedundancy,'zxAdslAturChanTable':zxAdslAturChanTable,'zxAdslAturChanEntry':zxAdslAturChanEntry,'zxAdslAturChanRsSymbols':zxAdslAturChanRsSymbols,'zxAdslAturChanRsDepth':zxAdslAturChanRsDepth,'zxAdslAturChanRsRedundancy':zxAdslAturChanRsRedundancy,'zxAdslAtucChanPerfTable':zxAdslAtucChanPerfTable,'zxAdslAtucChanPerfEntry':zxAdslAtucChanPerfEntry,'zxAdslAtucChanPerfNcd':zxAdslAtucChanPerfNcd,'zxAdslAtucChanPerfOcd':zxAdslAtucChanPerfOcd,'zxAdslAtucChanPerfHec':zxAdslAtucChanPerfHec,'zxAdslAtucChanPerfCurr15Ncd':zxAdslAtucChanPerfCurr15Ncd,'zxAdslAtucChanPerfCurr15Ocd':zxAdslAtucChanPerfCurr15Ocd,'zxAdslAtucChanPerfCurr15Hec':zxAdslAtucChanPerfCurr15Hec,'zxAdslAtucChanPerfCurr1DayNcd':zxAdslAtucChanPerfCurr1DayNcd,'zxAdslAtucChanPerfCurr1DayOcd':zxAdslAtucChanPerfCurr1DayOcd,'zxAdslAtucChanPerfCurr1DayHec':zxAdslAtucChanPerfCurr1DayHec,'zxAdslAtucChanPerfPrev1DayNcd':zxAdslAtucChanPerfPrev1DayNcd,'zxAdslAtucChanPerfPrev1DayOcd':zxAdslAtucChanPerfPrev1DayOcd,'zxAdslAtucChanPerfPrev1DayHec':zxAdslAtucChanPerfPrev1DayHec,'zxAdslAturChanPerfTable':zxAdslAturChanPerfTable,'zxAdslAturChanPerfEntry':zxAdslAturChanPerfEntry,'zxAdslAturChanPerfNcd':zxAdslAturChanPerfNcd,'zxAdslAturChanPerfHec':zxAdslAturChanPerfHec,'zxAdslAturChanPerfCurr15Ncd':zxAdslAturChanPerfCurr15Ncd,'zxAdslAturChanPerfCurr15Hec':zxAdslAturChanPerfCurr15Hec,'zxAdslAturChanPerfCurr1DayNcd':zxAdslAturChanPerfCurr1DayNcd,'zxAdslAturChanPerfCurr1DayHec':zxAdslAturChanPerfCurr1DayHec,'zxAdslAturChanPerfPrev1DayNcd':zxAdslAturChanPerfPrev1DayNcd,'zxAdslAturChanPerfPrev1DayHec':zxAdslAturChanPerfPrev1DayHec,'zxDslLoopTestTable':zxDslLoopTestTable,'zxDslLoopTestEntry':zxDslLoopTestEntry,_e:zxDslLoopTestPort,'zxDslLoopTestType':zxDslLoopTestType,'zxDslLoopTestOperStatus':zxDslLoopTestOperStatus,'zxDslLoopTestResult':zxDslLoopTestResult,'zxDslLoopTestConfParam1':zxDslLoopTestConfParam1,'zxDslLoopTestConfParam2':zxDslLoopTestConfParam2,'zxDslLoopTestConfParam3':zxDslLoopTestConfParam3,'zxDslLoopTestConfParam4':zxDslLoopTestConfParam4,'zxDslLoopTestConfParam5':zxDslLoopTestConfParam5,'zxDslLoopTestResultParam1':zxDslLoopTestResultParam1,'zxDslLoopTestResultParam2':zxDslLoopTestResultParam2,'zxDslLoopTestResultParam3':zxDslLoopTestResultParam3,'zxDslLoopTestResultParam4':zxDslLoopTestResultParam4,'zxDslLoopTestResultParam5':zxDslLoopTestResultParam5,'zxDslLoopTestRowStatus':zxDslLoopTestRowStatus,'zxAdslIsSupportAdsl2Plus':zxAdslIsSupportAdsl2Plus,'zxAdslIsSupportAdslRateThresh':zxAdslIsSupportAdslRateThresh,'zxAdslLineAlarmConfProfileExtTable':zxAdslLineAlarmConfProfileExtTable,_h:zxAdslLineAlarmConfProfileExtEntry,'zxAdslAtucConnRateTolerance':zxAdslAtucConnRateTolerance,'zxAdslAturConnRateTolerance':zxAdslAturConnRateTolerance,'zxAdslThreshAtucConnRate':zxAdslThreshAtucConnRate,'zxAdslThreshAturConnRate':zxAdslThreshAturConnRate,'zxAdslThreshAtucBandwidthUtil':zxAdslThreshAtucBandwidthUtil,'zxAdslThreshAturBandwidthUtil':zxAdslThreshAturBandwidthUtil,'zxAdslThreshAtucPacketLossRate':zxAdslThreshAtucPacketLossRate,'zxAdslThreshAturPacketLossRate':zxAdslThreshAturPacketLossRate,'zxAdslThreshAtucBlockErrorRate':zxAdslThreshAtucBlockErrorRate,'zxAdslThreshAturBlockErrorRate':zxAdslThreshAturBlockErrorRate,'zxAdslThreshReservedMetric1':zxAdslThreshReservedMetric1,'zxAdslThreshReservedMetric2':zxAdslThreshReservedMetric2,'zxAdslThreshReservedMetric3':zxAdslThreshReservedMetric3,'zxAdslExtTraps':zxAdslExtTraps,'zxAdslAtuxConnRateOverThreshTrap':zxAdslAtuxConnRateOverThreshTrap,'zxAdslAtuxConnRateUnderThreshTrap':zxAdslAtuxConnRateUnderThreshTrap,'zxAdslAtucBandwidthUtilOverThreshTrap':zxAdslAtucBandwidthUtilOverThreshTrap,'zxAdslAtucBandwidthUtilUnderThreshTrap':zxAdslAtucBandwidthUtilUnderThreshTrap,'zxAdslAturBandwidthUtilOverThreshTrap':zxAdslAturBandwidthUtilOverThreshTrap,'zxAdslAturBandwidthUtilUnderThreshTrap':zxAdslAturBandwidthUtilUnderThreshTrap,'zxAdslAtucPacketLossRateOverThreshTrap':zxAdslAtucPacketLossRateOverThreshTrap,'zxAdslAtucPacketLossRateUnderThreshTrap':zxAdslAtucPacketLossRateUnderThreshTrap,'zxAdslAturPacketLossRateOverThreshTrap':zxAdslAturPacketLossRateOverThreshTrap,'zxAdslAturPacketLossRateUnderThreshTrap':zxAdslAturPacketLossRateUnderThreshTrap,'zxAdslAtucBlockErrorRateOverThreshTrap':zxAdslAtucBlockErrorRateOverThreshTrap,'zxAdslAtucBlockErrorRateUnderThreshTrap':zxAdslAtucBlockErrorRateUnderThreshTrap,'zxAdslAturBlockErrorRateOverThreshTrap':zxAdslAturBlockErrorRateOverThreshTrap,'zxAdslAturBlockErrorRateUnderThreshTrap':zxAdslAturBlockErrorRateUnderThreshTrap})