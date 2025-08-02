_AE='cAdslAturDmtBinDataGroup'
_AD='cAdslAtucDmtBinDataGroup'
_AC='cAdslDmtBinIfGroup'
_AB='cAdslDmtLineConfProfileGroupRev1'
_AA='cAdslDmtLineConfProfileGroup'
_A9='cAdslAtucDmtDualBitmapEnabled'
_A8='cAdslAtucDmtConfMinrateBlock'
_A7='cAdslAturDmtBinNumber'
_A6='cAdslAturDmtBinTxGain'
_A5='cAdslAturDmtBinBitAlloc'
_A4='cAdslAtucDmtBinNumber'
_A3='cAdslAtucDmtBinTxGain'
_A2='cAdslAtucDmtBinBitAlloc'
_A1='cAdslDmtBinIfLstRqstUpldTime'
_A0='cAdslDmtBinIfRqstStatus'
_z='cAdslDmtBinIfNumber'
_y='cAdslAturDmtThreshRateFallback'
_x='cAdslAtucDmtThreshRateFallback'
_w='deprecated'
_v='cAdslAturDmtChanCodewordSize'
_u='cAdslAturDmtChanFecSize'
_t='cAdslAtucDmtChanCodewordSize'
_s='cAdslAtucDmtChanFecSize'
_r='cAdslAtucDmtState'
_q='cAdslDmtLineOverheadFraming'
_p='cAdslAturDmtBinIndex'
_o='cAdslAturDmtBitmapIndex'
_n='bits/Hz'
_m='cAdslAtucDmtBinIndex'
_l='cAdslAtucDmtBitmapIndex'
_k='read-write'
_j='DmtOverheadFraming'
_i='standard'
_h='adslLineConfProfileName'
_g='adslLineAlarmConfProfileName'
_f='cAdslDmtLineAlarmConfProfileGroup'
_e='cAdslAturDmtChanGroup'
_d='cAdslAtucDmtChanGroup'
_c='cAdslAtucDmtPhysGroup'
_b='cAdslDmtLineGroup'
_a='cAdslAturDmtConfCodewordSize'
_Z='cAdslAturDmtConfFastFecSize'
_Y='cAdslAturDmtConfInterleaveFecSize'
_X='cAdslAtucDmtConfBitSwapTo'
_W='cAdslAtucDmtConfBitSwapFrom'
_V='cAdslAtucDmtConfBitSwapEnabled'
_U='cAdslAtucDmtConfOverheadFraming'
_T='cAdslAtucDmtConfCodewordSize'
_S='cAdslAtucDmtConfInterleaveFecSize'
_R='cAdslAtucDmtConfFastFecSize'
_Q='cAdslLineDmtConfTrainingMode'
_P='cAdslLineDmtConfOperatingMode'
_O='DmtCodewordSize'
_N='ADSL-LINE-MIB'
_M='not-accessible'
_L='symbols'
_K='TruthValue'
_J='DmtFecSize'
_I='ifIndex'
_H='IF-MIB'
_G='bytes'
_F='Integer32'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='CISCO-ADSL-DMT-LINE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adslLineAlarmConfProfileName,adslLineConfProfileName=mibBuilder.importSymbols(_N,_g,_h)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Unsigned32,=mibBuilder.importSymbols('CISCO-TC',_E)
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_H,'InterfaceIndexOrZero',_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_K)
ciscoAdslDmtLineMIB=ModuleIdentity((1,3,6,1,4,1,9,9,130))
if mibBuilder.loadTexts:ciscoAdslDmtLineMIB.setRevisions(('2001-05-17 16:00','2000-08-22 00:00','2000-05-19 00:00','1999-03-30 00:00'))
class DmtOverheadFraming(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('structure0',0),('structure1',1),('structure2',2),('structure3',3)))
class DmtFecSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(6,6),ValueRangeConstraint(8,8),ValueRangeConstraint(10,10),ValueRangeConstraint(12,12),ValueRangeConstraint(14,14),ValueRangeConstraint(16,16))
class DmtCodewordSize(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,1),ValueRangeConstraint(2,2),ValueRangeConstraint(4,4),ValueRangeConstraint(8,8),ValueRangeConstraint(16,16))
_CiscoAdslDmtLineMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAdslDmtLineMIBObjects=_CiscoAdslDmtLineMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,130,1))
_CAdslDmtLineTable_Object=MibTable
cAdslDmtLineTable=_CAdslDmtLineTable_Object((1,3,6,1,4,1,9,9,130,1,1))
if mibBuilder.loadTexts:cAdslDmtLineTable.setStatus(_A)
_CAdslDmtLineEntry_Object=MibTableRow
cAdslDmtLineEntry=_CAdslDmtLineEntry_Object((1,3,6,1,4,1,9,9,130,1,1,1))
cAdslDmtLineEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cAdslDmtLineEntry.setStatus(_A)
_CAdslDmtLineOverheadFraming_Type=DmtOverheadFraming
_CAdslDmtLineOverheadFraming_Object=MibTableColumn
cAdslDmtLineOverheadFraming=_CAdslDmtLineOverheadFraming_Object((1,3,6,1,4,1,9,9,130,1,1,1,1),_CAdslDmtLineOverheadFraming_Type())
cAdslDmtLineOverheadFraming.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslDmtLineOverheadFraming.setStatus(_A)
_CAdslAtucDmtPhysTable_Object=MibTable
cAdslAtucDmtPhysTable=_CAdslAtucDmtPhysTable_Object((1,3,6,1,4,1,9,9,130,1,2))
if mibBuilder.loadTexts:cAdslAtucDmtPhysTable.setStatus(_A)
_CAdslAtucDmtPhysEntry_Object=MibTableRow
cAdslAtucDmtPhysEntry=_CAdslAtucDmtPhysEntry_Object((1,3,6,1,4,1,9,9,130,1,2,1))
cAdslAtucDmtPhysEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cAdslAtucDmtPhysEntry.setStatus(_A)
class _CAdslAtucDmtState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_i,1),('unknown',2),('downloading',3),('downloadFailed',4),('testing',5)))
_CAdslAtucDmtState_Type.__name__=_F
_CAdslAtucDmtState_Object=MibTableColumn
cAdslAtucDmtState=_CAdslAtucDmtState_Object((1,3,6,1,4,1,9,9,130,1,2,1,1),_CAdslAtucDmtState_Type())
cAdslAtucDmtState.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAtucDmtState.setStatus(_A)
_CAdslAtucDmtChanTable_Object=MibTable
cAdslAtucDmtChanTable=_CAdslAtucDmtChanTable_Object((1,3,6,1,4,1,9,9,130,1,4))
if mibBuilder.loadTexts:cAdslAtucDmtChanTable.setStatus(_A)
_CAdslAtucDmtChanEntry_Object=MibTableRow
cAdslAtucDmtChanEntry=_CAdslAtucDmtChanEntry_Object((1,3,6,1,4,1,9,9,130,1,4,1))
cAdslAtucDmtChanEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cAdslAtucDmtChanEntry.setStatus(_A)
_CAdslAtucDmtChanFecSize_Type=DmtFecSize
_CAdslAtucDmtChanFecSize_Object=MibTableColumn
cAdslAtucDmtChanFecSize=_CAdslAtucDmtChanFecSize_Object((1,3,6,1,4,1,9,9,130,1,4,1,1),_CAdslAtucDmtChanFecSize_Type())
cAdslAtucDmtChanFecSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAtucDmtChanFecSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtChanFecSize.setUnits(_G)
_CAdslAtucDmtChanCodewordSize_Type=DmtCodewordSize
_CAdslAtucDmtChanCodewordSize_Object=MibTableColumn
cAdslAtucDmtChanCodewordSize=_CAdslAtucDmtChanCodewordSize_Object((1,3,6,1,4,1,9,9,130,1,4,1,2),_CAdslAtucDmtChanCodewordSize_Type())
cAdslAtucDmtChanCodewordSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAtucDmtChanCodewordSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtChanCodewordSize.setUnits(_L)
_CAdslAturDmtChanTable_Object=MibTable
cAdslAturDmtChanTable=_CAdslAturDmtChanTable_Object((1,3,6,1,4,1,9,9,130,1,5))
if mibBuilder.loadTexts:cAdslAturDmtChanTable.setStatus(_A)
_CAdslAturDmtChanEntry_Object=MibTableRow
cAdslAturDmtChanEntry=_CAdslAturDmtChanEntry_Object((1,3,6,1,4,1,9,9,130,1,5,1))
cAdslAturDmtChanEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cAdslAturDmtChanEntry.setStatus(_A)
_CAdslAturDmtChanFecSize_Type=DmtFecSize
_CAdslAturDmtChanFecSize_Object=MibTableColumn
cAdslAturDmtChanFecSize=_CAdslAturDmtChanFecSize_Object((1,3,6,1,4,1,9,9,130,1,5,1,1),_CAdslAturDmtChanFecSize_Type())
cAdslAturDmtChanFecSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAturDmtChanFecSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtChanFecSize.setUnits(_G)
_CAdslAturDmtChanCodewordSize_Type=DmtCodewordSize
_CAdslAturDmtChanCodewordSize_Object=MibTableColumn
cAdslAturDmtChanCodewordSize=_CAdslAturDmtChanCodewordSize_Object((1,3,6,1,4,1,9,9,130,1,5,1,2),_CAdslAturDmtChanCodewordSize_Type())
cAdslAturDmtChanCodewordSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAturDmtChanCodewordSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtChanCodewordSize.setUnits(_L)
_CAdslDmtLineConfProfileTable_Object=MibTable
cAdslDmtLineConfProfileTable=_CAdslDmtLineConfProfileTable_Object((1,3,6,1,4,1,9,9,130,1,14))
if mibBuilder.loadTexts:cAdslDmtLineConfProfileTable.setStatus(_A)
_CAdslDmtLineConfProfileEntry_Object=MibTableRow
cAdslDmtLineConfProfileEntry=_CAdslDmtLineConfProfileEntry_Object((1,3,6,1,4,1,9,9,130,1,14,1))
cAdslDmtLineConfProfileEntry.setIndexNames((1,_N,_h))
if mibBuilder.loadTexts:cAdslDmtLineConfProfileEntry.setStatus(_A)
class _CAdslLineDmtConfOperatingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('automatic',1),('splitterless',2),('g992Dot1',3),('g992Dot2',4),('t1Dot413',5)))
_CAdslLineDmtConfOperatingMode_Type.__name__=_F
_CAdslLineDmtConfOperatingMode_Object=MibTableColumn
cAdslLineDmtConfOperatingMode=_CAdslLineDmtConfOperatingMode_Object((1,3,6,1,4,1,9,9,130,1,14,1,1),_CAdslLineDmtConfOperatingMode_Type())
cAdslLineDmtConfOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslLineDmtConfOperatingMode.setStatus(_A)
class _CAdslLineDmtConfTrainingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_i,1),('fast',2)))
_CAdslLineDmtConfTrainingMode_Type.__name__=_F
_CAdslLineDmtConfTrainingMode_Object=MibTableColumn
cAdslLineDmtConfTrainingMode=_CAdslLineDmtConfTrainingMode_Object((1,3,6,1,4,1,9,9,130,1,14,1,2),_CAdslLineDmtConfTrainingMode_Type())
cAdslLineDmtConfTrainingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslLineDmtConfTrainingMode.setStatus(_A)
class _CAdslAtucDmtConfFastFecSize_Type(DmtFecSize):defaultValue=16
_CAdslAtucDmtConfFastFecSize_Type.__name__=_J
_CAdslAtucDmtConfFastFecSize_Object=MibTableColumn
cAdslAtucDmtConfFastFecSize=_CAdslAtucDmtConfFastFecSize_Object((1,3,6,1,4,1,9,9,130,1,14,1,3),_CAdslAtucDmtConfFastFecSize_Type())
cAdslAtucDmtConfFastFecSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfFastFecSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtConfFastFecSize.setUnits(_G)
class _CAdslAtucDmtConfInterleaveFecSize_Type(DmtFecSize):defaultValue=16
_CAdslAtucDmtConfInterleaveFecSize_Type.__name__=_J
_CAdslAtucDmtConfInterleaveFecSize_Object=MibTableColumn
cAdslAtucDmtConfInterleaveFecSize=_CAdslAtucDmtConfInterleaveFecSize_Object((1,3,6,1,4,1,9,9,130,1,14,1,4),_CAdslAtucDmtConfInterleaveFecSize_Type())
cAdslAtucDmtConfInterleaveFecSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfInterleaveFecSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtConfInterleaveFecSize.setUnits(_G)
class _CAdslAtucDmtConfCodewordSize_Type(DmtCodewordSize):defaultValue=16
_CAdslAtucDmtConfCodewordSize_Type.__name__=_O
_CAdslAtucDmtConfCodewordSize_Object=MibTableColumn
cAdslAtucDmtConfCodewordSize=_CAdslAtucDmtConfCodewordSize_Object((1,3,6,1,4,1,9,9,130,1,14,1,5),_CAdslAtucDmtConfCodewordSize_Type())
cAdslAtucDmtConfCodewordSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfCodewordSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtConfCodewordSize.setUnits(_L)
class _CAdslAtucDmtConfOverheadFraming_Type(DmtOverheadFraming):defaultValue=3
_CAdslAtucDmtConfOverheadFraming_Type.__name__=_j
_CAdslAtucDmtConfOverheadFraming_Object=MibTableColumn
cAdslAtucDmtConfOverheadFraming=_CAdslAtucDmtConfOverheadFraming_Object((1,3,6,1,4,1,9,9,130,1,14,1,6),_CAdslAtucDmtConfOverheadFraming_Type())
cAdslAtucDmtConfOverheadFraming.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfOverheadFraming.setStatus(_A)
class _CAdslAtucDmtConfBitSwapEnabled_Type(TruthValue):defaultValue=1
_CAdslAtucDmtConfBitSwapEnabled_Type.__name__=_K
_CAdslAtucDmtConfBitSwapEnabled_Object=MibTableColumn
cAdslAtucDmtConfBitSwapEnabled=_CAdslAtucDmtConfBitSwapEnabled_Object((1,3,6,1,4,1,9,9,130,1,14,1,7),_CAdslAtucDmtConfBitSwapEnabled_Type())
cAdslAtucDmtConfBitSwapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfBitSwapEnabled.setStatus(_A)
class _CAdslAtucDmtConfBitSwapFrom_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_CAdslAtucDmtConfBitSwapFrom_Type.__name__=_F
_CAdslAtucDmtConfBitSwapFrom_Object=MibTableColumn
cAdslAtucDmtConfBitSwapFrom=_CAdslAtucDmtConfBitSwapFrom_Object((1,3,6,1,4,1,9,9,130,1,14,1,8),_CAdslAtucDmtConfBitSwapFrom_Type())
cAdslAtucDmtConfBitSwapFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfBitSwapFrom.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtConfBitSwapFrom.setUnits('dB')
class _CAdslAtucDmtConfBitSwapTo_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,9))
_CAdslAtucDmtConfBitSwapTo_Type.__name__=_F
_CAdslAtucDmtConfBitSwapTo_Object=MibTableColumn
cAdslAtucDmtConfBitSwapTo=_CAdslAtucDmtConfBitSwapTo_Object((1,3,6,1,4,1,9,9,130,1,14,1,9),_CAdslAtucDmtConfBitSwapTo_Type())
cAdslAtucDmtConfBitSwapTo.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfBitSwapTo.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtConfBitSwapTo.setUnits('dB')
class _CAdslAturDmtConfFastFecSize_Type(DmtFecSize):defaultValue=16
_CAdslAturDmtConfFastFecSize_Type.__name__=_J
_CAdslAturDmtConfFastFecSize_Object=MibTableColumn
cAdslAturDmtConfFastFecSize=_CAdslAturDmtConfFastFecSize_Object((1,3,6,1,4,1,9,9,130,1,14,1,10),_CAdslAturDmtConfFastFecSize_Type())
cAdslAturDmtConfFastFecSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAturDmtConfFastFecSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtConfFastFecSize.setUnits(_G)
class _CAdslAturDmtConfInterleaveFecSize_Type(DmtFecSize):defaultValue=16
_CAdslAturDmtConfInterleaveFecSize_Type.__name__=_J
_CAdslAturDmtConfInterleaveFecSize_Object=MibTableColumn
cAdslAturDmtConfInterleaveFecSize=_CAdslAturDmtConfInterleaveFecSize_Object((1,3,6,1,4,1,9,9,130,1,14,1,11),_CAdslAturDmtConfInterleaveFecSize_Type())
cAdslAturDmtConfInterleaveFecSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAturDmtConfInterleaveFecSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtConfInterleaveFecSize.setUnits(_G)
class _CAdslAturDmtConfCodewordSize_Type(DmtCodewordSize):defaultValue=16
_CAdslAturDmtConfCodewordSize_Type.__name__=_O
_CAdslAturDmtConfCodewordSize_Object=MibTableColumn
cAdslAturDmtConfCodewordSize=_CAdslAturDmtConfCodewordSize_Object((1,3,6,1,4,1,9,9,130,1,14,1,12),_CAdslAturDmtConfCodewordSize_Type())
cAdslAturDmtConfCodewordSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAturDmtConfCodewordSize.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtConfCodewordSize.setUnits(_L)
class _CAdslAtucDmtConfMinrateBlock_Type(TruthValue):defaultValue=2
_CAdslAtucDmtConfMinrateBlock_Type.__name__=_K
_CAdslAtucDmtConfMinrateBlock_Object=MibTableColumn
cAdslAtucDmtConfMinrateBlock=_CAdslAtucDmtConfMinrateBlock_Object((1,3,6,1,4,1,9,9,130,1,14,1,13),_CAdslAtucDmtConfMinrateBlock_Type())
cAdslAtucDmtConfMinrateBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtConfMinrateBlock.setStatus(_A)
class _CAdslAtucDmtDualBitmapEnabled_Type(TruthValue):defaultValue=2
_CAdslAtucDmtDualBitmapEnabled_Type.__name__=_K
_CAdslAtucDmtDualBitmapEnabled_Object=MibTableColumn
cAdslAtucDmtDualBitmapEnabled=_CAdslAtucDmtDualBitmapEnabled_Object((1,3,6,1,4,1,9,9,130,1,14,1,14),_CAdslAtucDmtDualBitmapEnabled_Type())
cAdslAtucDmtDualBitmapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtDualBitmapEnabled.setStatus(_A)
_CAdslDmtLineAlarmConfProfileTable_Object=MibTable
cAdslDmtLineAlarmConfProfileTable=_CAdslDmtLineAlarmConfProfileTable_Object((1,3,6,1,4,1,9,9,130,1,15))
if mibBuilder.loadTexts:cAdslDmtLineAlarmConfProfileTable.setStatus(_A)
_CAdslDmtLineAlarmConfProfileEntry_Object=MibTableRow
cAdslDmtLineAlarmConfProfileEntry=_CAdslDmtLineAlarmConfProfileEntry_Object((1,3,6,1,4,1,9,9,130,1,15,1))
cAdslDmtLineAlarmConfProfileEntry.setIndexNames((1,_N,_g))
if mibBuilder.loadTexts:cAdslDmtLineAlarmConfProfileEntry.setStatus(_A)
class _CAdslAtucDmtThreshRateFallback_Type(Integer32):defaultValue=0
_CAdslAtucDmtThreshRateFallback_Type.__name__=_F
_CAdslAtucDmtThreshRateFallback_Object=MibTableColumn
cAdslAtucDmtThreshRateFallback=_CAdslAtucDmtThreshRateFallback_Object((1,3,6,1,4,1,9,9,130,1,15,1,1),_CAdslAtucDmtThreshRateFallback_Type())
cAdslAtucDmtThreshRateFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAtucDmtThreshRateFallback.setStatus(_A)
class _CAdslAturDmtThreshRateFallback_Type(Integer32):defaultValue=0
_CAdslAturDmtThreshRateFallback_Type.__name__=_F
_CAdslAturDmtThreshRateFallback_Object=MibTableColumn
cAdslAturDmtThreshRateFallback=_CAdslAturDmtThreshRateFallback_Object((1,3,6,1,4,1,9,9,130,1,15,1,2),_CAdslAturDmtThreshRateFallback_Type())
cAdslAturDmtThreshRateFallback.setMaxAccess(_C)
if mibBuilder.loadTexts:cAdslAturDmtThreshRateFallback.setStatus(_A)
_CAdslDmtBinIfNumber_Type=InterfaceIndexOrZero
_CAdslDmtBinIfNumber_Object=MibScalar
cAdslDmtBinIfNumber=_CAdslDmtBinIfNumber_Object((1,3,6,1,4,1,9,9,130,1,16),_CAdslDmtBinIfNumber_Type())
cAdslDmtBinIfNumber.setMaxAccess(_k)
if mibBuilder.loadTexts:cAdslDmtBinIfNumber.setStatus(_A)
class _CAdslDmtBinIfRqstStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('reset',-1),('pollNow',1),('noIfConfigured',2),('ifConfigured',3),('rqstInProgess',4),('lcDownForIf',5),('ifUntrained',6),('failure',7),('success',8)))
_CAdslDmtBinIfRqstStatus_Type.__name__=_F
_CAdslDmtBinIfRqstStatus_Object=MibScalar
cAdslDmtBinIfRqstStatus=_CAdslDmtBinIfRqstStatus_Object((1,3,6,1,4,1,9,9,130,1,17),_CAdslDmtBinIfRqstStatus_Type())
cAdslDmtBinIfRqstStatus.setMaxAccess(_k)
if mibBuilder.loadTexts:cAdslDmtBinIfRqstStatus.setStatus(_A)
_CAdslDmtBinIfLstRqstUpldTime_Type=DateAndTime
_CAdslDmtBinIfLstRqstUpldTime_Object=MibScalar
cAdslDmtBinIfLstRqstUpldTime=_CAdslDmtBinIfLstRqstUpldTime_Object((1,3,6,1,4,1,9,9,130,1,18),_CAdslDmtBinIfLstRqstUpldTime_Type())
cAdslDmtBinIfLstRqstUpldTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslDmtBinIfLstRqstUpldTime.setStatus(_A)
_CAdslAtucDmtBinTable_Object=MibTable
cAdslAtucDmtBinTable=_CAdslAtucDmtBinTable_Object((1,3,6,1,4,1,9,9,130,1,19))
if mibBuilder.loadTexts:cAdslAtucDmtBinTable.setStatus(_A)
_CAdslAtucDmtBinEntry_Object=MibTableRow
cAdslAtucDmtBinEntry=_CAdslAtucDmtBinEntry_Object((1,3,6,1,4,1,9,9,130,1,19,1))
cAdslAtucDmtBinEntry.setIndexNames((0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:cAdslAtucDmtBinEntry.setStatus(_A)
class _CAdslAtucDmtBitmapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_CAdslAtucDmtBitmapIndex_Type.__name__=_E
_CAdslAtucDmtBitmapIndex_Object=MibTableColumn
cAdslAtucDmtBitmapIndex=_CAdslAtucDmtBitmapIndex_Object((1,3,6,1,4,1,9,9,130,1,19,1,1),_CAdslAtucDmtBitmapIndex_Type())
cAdslAtucDmtBitmapIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cAdslAtucDmtBitmapIndex.setStatus(_A)
class _CAdslAtucDmtBinIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CAdslAtucDmtBinIndex_Type.__name__=_E
_CAdslAtucDmtBinIndex_Object=MibTableColumn
cAdslAtucDmtBinIndex=_CAdslAtucDmtBinIndex_Object((1,3,6,1,4,1,9,9,130,1,19,1,2),_CAdslAtucDmtBinIndex_Type())
cAdslAtucDmtBinIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cAdslAtucDmtBinIndex.setStatus(_A)
class _CAdslAtucDmtBinBitAlloc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CAdslAtucDmtBinBitAlloc_Type.__name__=_E
_CAdslAtucDmtBinBitAlloc_Object=MibTableColumn
cAdslAtucDmtBinBitAlloc=_CAdslAtucDmtBinBitAlloc_Object((1,3,6,1,4,1,9,9,130,1,19,1,3),_CAdslAtucDmtBinBitAlloc_Type())
cAdslAtucDmtBinBitAlloc.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAtucDmtBinBitAlloc.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtBinBitAlloc.setUnits(_n)
class _CAdslAtucDmtBinTxGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_CAdslAtucDmtBinTxGain_Type.__name__=_E
_CAdslAtucDmtBinTxGain_Object=MibTableColumn
cAdslAtucDmtBinTxGain=_CAdslAtucDmtBinTxGain_Object((1,3,6,1,4,1,9,9,130,1,19,1,4),_CAdslAtucDmtBinTxGain_Type())
cAdslAtucDmtBinTxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAtucDmtBinTxGain.setStatus(_A)
if mibBuilder.loadTexts:cAdslAtucDmtBinTxGain.setUnits('tenth dB')
class _CAdslAtucDmtBinNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CAdslAtucDmtBinNumber_Type.__name__=_E
_CAdslAtucDmtBinNumber_Object=MibTableColumn
cAdslAtucDmtBinNumber=_CAdslAtucDmtBinNumber_Object((1,3,6,1,4,1,9,9,130,1,19,1,5),_CAdslAtucDmtBinNumber_Type())
cAdslAtucDmtBinNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAtucDmtBinNumber.setStatus(_A)
_CAdslAturDmtBinTable_Object=MibTable
cAdslAturDmtBinTable=_CAdslAturDmtBinTable_Object((1,3,6,1,4,1,9,9,130,1,20))
if mibBuilder.loadTexts:cAdslAturDmtBinTable.setStatus(_A)
_CAdslAturDmtBinEntry_Object=MibTableRow
cAdslAturDmtBinEntry=_CAdslAturDmtBinEntry_Object((1,3,6,1,4,1,9,9,130,1,20,1))
cAdslAturDmtBinEntry.setIndexNames((0,_B,_o),(0,_B,_p))
if mibBuilder.loadTexts:cAdslAturDmtBinEntry.setStatus(_A)
class _CAdslAturDmtBitmapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5))
_CAdslAturDmtBitmapIndex_Type.__name__=_E
_CAdslAturDmtBitmapIndex_Object=MibTableColumn
cAdslAturDmtBitmapIndex=_CAdslAturDmtBitmapIndex_Object((1,3,6,1,4,1,9,9,130,1,20,1,1),_CAdslAturDmtBitmapIndex_Type())
cAdslAturDmtBitmapIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cAdslAturDmtBitmapIndex.setStatus(_A)
class _CAdslAturDmtBinIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CAdslAturDmtBinIndex_Type.__name__=_E
_CAdslAturDmtBinIndex_Object=MibTableColumn
cAdslAturDmtBinIndex=_CAdslAturDmtBinIndex_Object((1,3,6,1,4,1,9,9,130,1,20,1,2),_CAdslAturDmtBinIndex_Type())
cAdslAturDmtBinIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:cAdslAturDmtBinIndex.setStatus(_A)
class _CAdslAturDmtBinBitAlloc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CAdslAturDmtBinBitAlloc_Type.__name__=_E
_CAdslAturDmtBinBitAlloc_Object=MibTableColumn
cAdslAturDmtBinBitAlloc=_CAdslAturDmtBinBitAlloc_Object((1,3,6,1,4,1,9,9,130,1,20,1,3),_CAdslAturDmtBinBitAlloc_Type())
cAdslAturDmtBinBitAlloc.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAturDmtBinBitAlloc.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtBinBitAlloc.setUnits(_n)
class _CAdslAturDmtBinTxGain_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,400))
_CAdslAturDmtBinTxGain_Type.__name__=_E
_CAdslAturDmtBinTxGain_Object=MibTableColumn
cAdslAturDmtBinTxGain=_CAdslAturDmtBinTxGain_Object((1,3,6,1,4,1,9,9,130,1,20,1,4),_CAdslAturDmtBinTxGain_Type())
cAdslAturDmtBinTxGain.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAturDmtBinTxGain.setStatus(_A)
if mibBuilder.loadTexts:cAdslAturDmtBinTxGain.setUnits('hundredth dB')
class _CAdslAturDmtBinNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CAdslAturDmtBinNumber_Type.__name__=_E
_CAdslAturDmtBinNumber_Object=MibTableColumn
cAdslAturDmtBinNumber=_CAdslAturDmtBinNumber_Object((1,3,6,1,4,1,9,9,130,1,20,1,5),_CAdslAturDmtBinNumber_Type())
cAdslAturDmtBinNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cAdslAturDmtBinNumber.setStatus(_A)
_CiscoAdslDmtLineMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
ciscoAdslDmtLineMIBNotificationsPrefix=_CiscoAdslDmtLineMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,130,2))
_CiscoAdslDmtLineMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoAdslDmtLineMIBNotifications=_CiscoAdslDmtLineMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,130,2,0))
_CiscoAdslDmtLineMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAdslDmtLineMIBConformance=_CiscoAdslDmtLineMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,130,3))
_CiscoAdslDmtLineMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAdslDmtLineMIBCompliances=_CiscoAdslDmtLineMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,130,3,1))
_CiscoAdslDmtLineMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAdslDmtLineMIBGroups=_CiscoAdslDmtLineMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,130,3,2))
cAdslDmtLineGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,1))
cAdslDmtLineGroup.setObjects((_B,_q))
if mibBuilder.loadTexts:cAdslDmtLineGroup.setStatus(_A)
cAdslAtucDmtPhysGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,2))
cAdslAtucDmtPhysGroup.setObjects((_B,_r))
if mibBuilder.loadTexts:cAdslAtucDmtPhysGroup.setStatus(_A)
cAdslAtucDmtChanGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,3))
cAdslAtucDmtChanGroup.setObjects(*((_B,_s),(_B,_t)))
if mibBuilder.loadTexts:cAdslAtucDmtChanGroup.setStatus(_A)
cAdslAturDmtChanGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,4))
cAdslAturDmtChanGroup.setObjects(*((_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cAdslAturDmtChanGroup.setStatus(_A)
cAdslDmtLineConfProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,5))
cAdslDmtLineConfProfileGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cAdslDmtLineConfProfileGroup.setStatus(_w)
cAdslDmtLineAlarmConfProfileGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,6))
cAdslDmtLineAlarmConfProfileGroup.setObjects(*((_B,_x),(_B,_y)))
if mibBuilder.loadTexts:cAdslDmtLineAlarmConfProfileGroup.setStatus(_A)
cAdslDmtBinIfGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,7))
cAdslDmtBinIfGroup.setObjects(*((_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:cAdslDmtBinIfGroup.setStatus(_A)
cAdslAtucDmtBinDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,8))
cAdslAtucDmtBinDataGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:cAdslAtucDmtBinDataGroup.setStatus(_A)
cAdslAturDmtBinDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,9))
cAdslAturDmtBinDataGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:cAdslAturDmtBinDataGroup.setStatus(_A)
cAdslDmtLineConfProfileGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,130,3,2,10))
cAdslDmtLineConfProfileGroupRev1.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:cAdslDmtLineConfProfileGroupRev1.setStatus(_A)
ciscoAdslDmtLineMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,130,3,1,1))
ciscoAdslDmtLineMIBCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_AA),(_B,_f)))
if mibBuilder.loadTexts:ciscoAdslDmtLineMIBCompliance.setStatus(_w)
ciscoAdslDmtLineMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,130,3,1,2))
ciscoAdslDmtLineMIBComplianceRev1.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_AB),(_B,_f),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:ciscoAdslDmtLineMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_j:DmtOverheadFraming,_J:DmtFecSize,_O:DmtCodewordSize,'ciscoAdslDmtLineMIB':ciscoAdslDmtLineMIB,'ciscoAdslDmtLineMIBObjects':ciscoAdslDmtLineMIBObjects,'cAdslDmtLineTable':cAdslDmtLineTable,'cAdslDmtLineEntry':cAdslDmtLineEntry,_q:cAdslDmtLineOverheadFraming,'cAdslAtucDmtPhysTable':cAdslAtucDmtPhysTable,'cAdslAtucDmtPhysEntry':cAdslAtucDmtPhysEntry,_r:cAdslAtucDmtState,'cAdslAtucDmtChanTable':cAdslAtucDmtChanTable,'cAdslAtucDmtChanEntry':cAdslAtucDmtChanEntry,_s:cAdslAtucDmtChanFecSize,_t:cAdslAtucDmtChanCodewordSize,'cAdslAturDmtChanTable':cAdslAturDmtChanTable,'cAdslAturDmtChanEntry':cAdslAturDmtChanEntry,_u:cAdslAturDmtChanFecSize,_v:cAdslAturDmtChanCodewordSize,'cAdslDmtLineConfProfileTable':cAdslDmtLineConfProfileTable,'cAdslDmtLineConfProfileEntry':cAdslDmtLineConfProfileEntry,_P:cAdslLineDmtConfOperatingMode,_Q:cAdslLineDmtConfTrainingMode,_R:cAdslAtucDmtConfFastFecSize,_S:cAdslAtucDmtConfInterleaveFecSize,_T:cAdslAtucDmtConfCodewordSize,_U:cAdslAtucDmtConfOverheadFraming,_V:cAdslAtucDmtConfBitSwapEnabled,_W:cAdslAtucDmtConfBitSwapFrom,_X:cAdslAtucDmtConfBitSwapTo,_Z:cAdslAturDmtConfFastFecSize,_Y:cAdslAturDmtConfInterleaveFecSize,_a:cAdslAturDmtConfCodewordSize,_A8:cAdslAtucDmtConfMinrateBlock,_A9:cAdslAtucDmtDualBitmapEnabled,'cAdslDmtLineAlarmConfProfileTable':cAdslDmtLineAlarmConfProfileTable,'cAdslDmtLineAlarmConfProfileEntry':cAdslDmtLineAlarmConfProfileEntry,_x:cAdslAtucDmtThreshRateFallback,_y:cAdslAturDmtThreshRateFallback,_z:cAdslDmtBinIfNumber,_A0:cAdslDmtBinIfRqstStatus,_A1:cAdslDmtBinIfLstRqstUpldTime,'cAdslAtucDmtBinTable':cAdslAtucDmtBinTable,'cAdslAtucDmtBinEntry':cAdslAtucDmtBinEntry,_l:cAdslAtucDmtBitmapIndex,_m:cAdslAtucDmtBinIndex,_A2:cAdslAtucDmtBinBitAlloc,_A3:cAdslAtucDmtBinTxGain,_A4:cAdslAtucDmtBinNumber,'cAdslAturDmtBinTable':cAdslAturDmtBinTable,'cAdslAturDmtBinEntry':cAdslAturDmtBinEntry,_o:cAdslAturDmtBitmapIndex,_p:cAdslAturDmtBinIndex,_A5:cAdslAturDmtBinBitAlloc,_A6:cAdslAturDmtBinTxGain,_A7:cAdslAturDmtBinNumber,'ciscoAdslDmtLineMIBNotificationsPrefix':ciscoAdslDmtLineMIBNotificationsPrefix,'ciscoAdslDmtLineMIBNotifications':ciscoAdslDmtLineMIBNotifications,'ciscoAdslDmtLineMIBConformance':ciscoAdslDmtLineMIBConformance,'ciscoAdslDmtLineMIBCompliances':ciscoAdslDmtLineMIBCompliances,'ciscoAdslDmtLineMIBCompliance':ciscoAdslDmtLineMIBCompliance,'ciscoAdslDmtLineMIBComplianceRev1':ciscoAdslDmtLineMIBComplianceRev1,'ciscoAdslDmtLineMIBGroups':ciscoAdslDmtLineMIBGroups,_b:cAdslDmtLineGroup,_c:cAdslAtucDmtPhysGroup,_d:cAdslAtucDmtChanGroup,_e:cAdslAturDmtChanGroup,_AA:cAdslDmtLineConfProfileGroup,_f:cAdslDmtLineAlarmConfProfileGroup,_AC:cAdslDmtBinIfGroup,_AD:cAdslAtucDmtBinDataGroup,_AE:cAdslAturDmtBinDataGroup,_AB:cAdslDmtLineConfProfileGroupRev1})