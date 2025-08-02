_f='h3cDot11OldPower'
_e='h3cDot11NewPower'
_d='h3cDot11RRMChlRptNoise'
_c='h3cDot11RRMChlRptPER'
_b='h3cDot11RRMChlRptIntrf'
_a='h3cDot11MonitorDevMAC'
_Z='h3cDot11RRMHistoryRecIndctr'
_Y='h3cDot11RRMHistoryId'
_X='h3cDot11RrmNbrBSSID'
_W='h3cDot11RRMChlRptChlNum'
_V='h3cDot11RRMAPSerialID'
_U='h3cDot11RRMSDRadioGroupId'
_T='userTriggered'
_S='selfDecisive'
_R='h3cDot11RRMRadioType'
_Q='dbm'
_P='minute'
_O='dBm'
_N='Unsigned32'
_M='h3cDot11APElementIndex'
_L='A3COM-HUAWEI-DOT11-REF-MIB'
_K='accessible-for-notify'
_J='read-create'
_I='h3cDot11RRMRadioIndex'
_H='TruthValue'
_G='not-accessible'
_F='percent'
_E='A3COM-HUAWEI-DOT11-RRM-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cDot11ChannelScopeType,H3cDot11ObjectIDType,H3cDot11RadioElementIndex,H3cDot11RadioScopeType,H3cDot11RadioType,H3cDot11SSIDStringType,h3cDot11,h3cDot11APElementIndex=mibBuilder.importSymbols(_L,'H3cDot11ChannelScopeType','H3cDot11ObjectIDType','H3cDot11RadioElementIndex','H3cDot11RadioScopeType','H3cDot11RadioType','H3cDot11SSIDStringType','h3cDot11',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
h3cDot11RRM=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8))
if mibBuilder.loadTexts:h3cDot11RRM.setRevisions(('2010-09-25 18:00','2010-02-23 18:00','2009-08-01 20:00','2009-05-07 20:00','2009-04-17 20:00','2008-07-14 14:29'))
_H3cDot11RRMConfigGroup_ObjectIdentity=ObjectIdentity
h3cDot11RRMConfigGroup=_H3cDot11RRMConfigGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,1))
_H3cDot11RRMGlobalCfgPara_ObjectIdentity=ObjectIdentity
h3cDot11RRMGlobalCfgPara=_H3cDot11RRMGlobalCfgPara_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1))
class _H3cDot11RRM11nMadtMaxMcs_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76),ValueRangeConstraint(255,255))
_H3cDot11RRM11nMadtMaxMcs_Type.__name__=_C
_H3cDot11RRM11nMadtMaxMcs_Object=MibScalar
h3cDot11RRM11nMadtMaxMcs=_H3cDot11RRM11nMadtMaxMcs_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,1),_H3cDot11RRM11nMadtMaxMcs_Type())
h3cDot11RRM11nMadtMaxMcs.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRM11nMadtMaxMcs.setStatus(_A)
class _H3cDot11RRM11nSuptMaxMcs_Type(Integer32):defaultValue=76;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76))
_H3cDot11RRM11nSuptMaxMcs_Type.__name__=_C
_H3cDot11RRM11nSuptMaxMcs_Object=MibScalar
h3cDot11RRM11nSuptMaxMcs=_H3cDot11RRM11nSuptMaxMcs_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,2),_H3cDot11RRM11nSuptMaxMcs_Type())
h3cDot11RRM11nSuptMaxMcs.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRM11nSuptMaxMcs.setStatus(_A)
class _H3cDot11RRM11gProtect_Type(TruthValue):defaultValue=2
_H3cDot11RRM11gProtect_Type.__name__=_H
_H3cDot11RRM11gProtect_Object=MibScalar
h3cDot11RRM11gProtect=_H3cDot11RRM11gProtect_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,3),_H3cDot11RRM11gProtect_Type())
h3cDot11RRM11gProtect.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRM11gProtect.setStatus(_A)
class _H3cDot11RRM11aPwrConstrt_Type(Integer32):defaultValue=0
_H3cDot11RRM11aPwrConstrt_Type.__name__=_C
_H3cDot11RRM11aPwrConstrt_Object=MibScalar
h3cDot11RRM11aPwrConstrt=_H3cDot11RRM11aPwrConstrt_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,4),_H3cDot11RRM11aPwrConstrt_Type())
h3cDot11RRM11aPwrConstrt.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRM11aPwrConstrt.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRM11aPwrConstrt.setUnits(_O)
class _H3cDot11RRM11aSpectrumManag_Type(TruthValue):defaultValue=2
_H3cDot11RRM11aSpectrumManag_Type.__name__=_H
_H3cDot11RRM11aSpectrumManag_Object=MibScalar
h3cDot11RRM11aSpectrumManag=_H3cDot11RRM11aSpectrumManag_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,5),_H3cDot11RRM11aSpectrumManag_Type())
h3cDot11RRM11aSpectrumManag.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRM11aSpectrumManag.setStatus(_A)
class _H3cDot11RRMAutoChlAvoid11h_Type(TruthValue):defaultValue=2
_H3cDot11RRMAutoChlAvoid11h_Type.__name__=_H
_H3cDot11RRMAutoChlAvoid11h_Object=MibScalar
h3cDot11RRMAutoChlAvoid11h=_H3cDot11RRMAutoChlAvoid11h_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,6),_H3cDot11RRMAutoChlAvoid11h_Type())
h3cDot11RRMAutoChlAvoid11h.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMAutoChlAvoid11h.setStatus(_A)
class _H3cDot11RRMScanChl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('all',2)))
_H3cDot11RRMScanChl_Type.__name__=_C
_H3cDot11RRMScanChl_Object=MibScalar
h3cDot11RRMScanChl=_H3cDot11RRMScanChl_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,7),_H3cDot11RRMScanChl_Type())
h3cDot11RRMScanChl.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMScanChl.setStatus(_A)
class _H3cDot11RRMScanRptIntvel_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_H3cDot11RRMScanRptIntvel_Type.__name__=_C
_H3cDot11RRMScanRptIntvel_Object=MibScalar
h3cDot11RRMScanRptIntvel=_H3cDot11RRMScanRptIntvel_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,8),_H3cDot11RRMScanRptIntvel_Type())
h3cDot11RRMScanRptIntvel.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMScanRptIntvel.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMScanRptIntvel.setUnits('second')
class _H3cDot11APInterfNumThreshhd_Type(Integer32):defaultValue=0
_H3cDot11APInterfNumThreshhd_Type.__name__=_C
_H3cDot11APInterfNumThreshhd_Object=MibScalar
h3cDot11APInterfNumThreshhd=_H3cDot11APInterfNumThreshhd_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,9),_H3cDot11APInterfNumThreshhd_Type())
h3cDot11APInterfNumThreshhd.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11APInterfNumThreshhd.setStatus(_A)
class _H3cDot11StaInterfNumThreshhd_Type(Integer32):defaultValue=0
_H3cDot11StaInterfNumThreshhd_Type.__name__=_C
_H3cDot11StaInterfNumThreshhd_Object=MibScalar
h3cDot11StaInterfNumThreshhd=_H3cDot11StaInterfNumThreshhd_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,1,10),_H3cDot11StaInterfNumThreshhd_Type())
h3cDot11StaInterfNumThreshhd.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11StaInterfNumThreshhd.setStatus(_A)
_H3cDot11RRMRadioCfgTable_Object=MibTable
h3cDot11RRMRadioCfgTable=_H3cDot11RRMRadioCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2))
if mibBuilder.loadTexts:h3cDot11RRMRadioCfgTable.setStatus(_A)
_H3cDot11RRMRadioCfgEntry_Object=MibTableRow
h3cDot11RRMRadioCfgEntry=_H3cDot11RRMRadioCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1))
h3cDot11RRMRadioCfgEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:h3cDot11RRMRadioCfgEntry.setStatus(_A)
_H3cDot11RRMRadioType_Type=H3cDot11RadioType
_H3cDot11RRMRadioType_Object=MibTableColumn
h3cDot11RRMRadioType=_H3cDot11RRMRadioType_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,1),_H3cDot11RRMRadioType_Type())
h3cDot11RRMRadioType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11RRMRadioType.setStatus(_A)
class _H3cDot11RRMCfgChlState_Type(TruthValue):defaultValue=2
_H3cDot11RRMCfgChlState_Type.__name__=_H
_H3cDot11RRMCfgChlState_Object=MibTableColumn
h3cDot11RRMCfgChlState=_H3cDot11RRMCfgChlState_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,2),_H3cDot11RRMCfgChlState_Type())
h3cDot11RRMCfgChlState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgChlState.setStatus(_A)
class _H3cDot11RRMCfgChlMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_H3cDot11RRMCfgChlMode_Type.__name__=_C
_H3cDot11RRMCfgChlMode_Object=MibTableColumn
h3cDot11RRMCfgChlMode=_H3cDot11RRMCfgChlMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,3),_H3cDot11RRMCfgChlMode_Type())
h3cDot11RRMCfgChlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgChlMode.setStatus(_A)
class _H3cDot11RRMChlProntoRadioElmt_Type(Unsigned32):defaultValue=0
_H3cDot11RRMChlProntoRadioElmt_Type.__name__=_N
_H3cDot11RRMChlProntoRadioElmt_Object=MibTableColumn
h3cDot11RRMChlProntoRadioElmt=_H3cDot11RRMChlProntoRadioElmt_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,4),_H3cDot11RRMChlProntoRadioElmt_Type())
h3cDot11RRMChlProntoRadioElmt.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMChlProntoRadioElmt.setStatus(_A)
class _H3cDot11RRMCfgPwrState_Type(TruthValue):defaultValue=2
_H3cDot11RRMCfgPwrState_Type.__name__=_H
_H3cDot11RRMCfgPwrState_Object=MibTableColumn
h3cDot11RRMCfgPwrState=_H3cDot11RRMCfgPwrState_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,5),_H3cDot11RRMCfgPwrState_Type())
h3cDot11RRMCfgPwrState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgPwrState.setStatus(_A)
class _H3cDot11RRMCfgPwrMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_H3cDot11RRMCfgPwrMode_Type.__name__=_C
_H3cDot11RRMCfgPwrMode_Object=MibTableColumn
h3cDot11RRMCfgPwrMode=_H3cDot11RRMCfgPwrMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,6),_H3cDot11RRMCfgPwrMode_Type())
h3cDot11RRMCfgPwrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgPwrMode.setStatus(_A)
class _H3cDot11RRMPwrProntoRadioElmt_Type(Unsigned32):defaultValue=0
_H3cDot11RRMPwrProntoRadioElmt_Type.__name__=_N
_H3cDot11RRMPwrProntoRadioElmt_Object=MibTableColumn
h3cDot11RRMPwrProntoRadioElmt=_H3cDot11RRMPwrProntoRadioElmt_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,7),_H3cDot11RRMPwrProntoRadioElmt_Type())
h3cDot11RRMPwrProntoRadioElmt.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMPwrProntoRadioElmt.setStatus(_A)
class _H3cDot11RRMCfgIntrvl_Type(Integer32):defaultValue=8
_H3cDot11RRMCfgIntrvl_Type.__name__=_C
_H3cDot11RRMCfgIntrvl_Object=MibTableColumn
h3cDot11RRMCfgIntrvl=_H3cDot11RRMCfgIntrvl_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,8),_H3cDot11RRMCfgIntrvl_Type())
h3cDot11RRMCfgIntrvl.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgIntrvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMCfgIntrvl.setUnits(_P)
class _H3cDot11RRMCfgIntrfThres_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(40,100))
_H3cDot11RRMCfgIntrfThres_Type.__name__=_C
_H3cDot11RRMCfgIntrfThres_Object=MibTableColumn
h3cDot11RRMCfgIntrfThres=_H3cDot11RRMCfgIntrfThres_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,9),_H3cDot11RRMCfgIntrfThres_Type())
h3cDot11RRMCfgIntrfThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgIntrfThres.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMCfgIntrfThres.setUnits(_F)
class _H3cDot11RRMCfgNoiseThres_Type(Integer32):defaultValue=-70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_H3cDot11RRMCfgNoiseThres_Type.__name__=_C
_H3cDot11RRMCfgNoiseThres_Object=MibTableColumn
h3cDot11RRMCfgNoiseThres=_H3cDot11RRMCfgNoiseThres_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,10),_H3cDot11RRMCfgNoiseThres_Type())
h3cDot11RRMCfgNoiseThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgNoiseThres.setStatus(_A)
class _H3cDot11RRMCfgPERThres_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,100))
_H3cDot11RRMCfgPERThres_Type.__name__=_C
_H3cDot11RRMCfgPERThres_Object=MibTableColumn
h3cDot11RRMCfgPERThres=_H3cDot11RRMCfgPERThres_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,11),_H3cDot11RRMCfgPERThres_Type())
h3cDot11RRMCfgPERThres.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgPERThres.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMCfgPERThres.setUnits(_F)
class _H3cDot11RRMCfgToleranceFctr_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,45))
_H3cDot11RRMCfgToleranceFctr_Type.__name__=_C
_H3cDot11RRMCfgToleranceFctr_Object=MibTableColumn
h3cDot11RRMCfgToleranceFctr=_H3cDot11RRMCfgToleranceFctr_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,12),_H3cDot11RRMCfgToleranceFctr_Type())
h3cDot11RRMCfgToleranceFctr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgToleranceFctr.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMCfgToleranceFctr.setUnits(_F)
class _H3cDot11RRMCfgAdjacencyFctr_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cDot11RRMCfgAdjacencyFctr_Type.__name__=_C
_H3cDot11RRMCfgAdjacencyFctr_Object=MibTableColumn
h3cDot11RRMCfgAdjacencyFctr=_H3cDot11RRMCfgAdjacencyFctr_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,2,1,13),_H3cDot11RRMCfgAdjacencyFctr_Type())
h3cDot11RRMCfgAdjacencyFctr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCfgAdjacencyFctr.setStatus(_A)
_H3cDot11RRMAPCfgTable_Object=MibTable
h3cDot11RRMAPCfgTable=_H3cDot11RRMAPCfgTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,3))
if mibBuilder.loadTexts:h3cDot11RRMAPCfgTable.setStatus(_A)
_H3cDot11RRMAPCfgEntry_Object=MibTableRow
h3cDot11RRMAPCfgEntry=_H3cDot11RRMAPCfgEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,3,1))
h3cDot11RRMAPCfgEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:h3cDot11RRMAPCfgEntry.setStatus(_A)
class _H3cDot11RRMAPWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('monitor',2),('hybrid',3)))
_H3cDot11RRMAPWorkMode_Type.__name__=_C
_H3cDot11RRMAPWorkMode_Object=MibTableColumn
h3cDot11RRMAPWorkMode=_H3cDot11RRMAPWorkMode_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,3,1,1),_H3cDot11RRMAPWorkMode_Type())
h3cDot11RRMAPWorkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMAPWorkMode.setStatus(_A)
_H3cDot11RRMSDRadioGroupTable_Object=MibTable
h3cDot11RRMSDRadioGroupTable=_H3cDot11RRMSDRadioGroupTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4))
if mibBuilder.loadTexts:h3cDot11RRMSDRadioGroupTable.setStatus(_A)
_H3cDot11RRMSDRadioGroupEntry_Object=MibTableRow
h3cDot11RRMSDRadioGroupEntry=_H3cDot11RRMSDRadioGroupEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4,1))
h3cDot11RRMSDRadioGroupEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:h3cDot11RRMSDRadioGroupEntry.setStatus(_A)
_H3cDot11RRMSDRadioGroupId_Type=Unsigned32
_H3cDot11RRMSDRadioGroupId_Object=MibTableColumn
h3cDot11RRMSDRadioGroupId=_H3cDot11RRMSDRadioGroupId_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4,1,1),_H3cDot11RRMSDRadioGroupId_Type())
h3cDot11RRMSDRadioGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11RRMSDRadioGroupId.setStatus(_A)
_H3cDot11RRMSDRadioGroupDesc_Type=OctetString
_H3cDot11RRMSDRadioGroupDesc_Object=MibTableColumn
h3cDot11RRMSDRadioGroupDesc=_H3cDot11RRMSDRadioGroupDesc_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4,1,2),_H3cDot11RRMSDRadioGroupDesc_Type())
h3cDot11RRMSDRadioGroupDesc.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11RRMSDRadioGroupDesc.setStatus(_A)
_H3cDot11RRMSDRdGrpChlHolddownTm_Type=Unsigned32
_H3cDot11RRMSDRdGrpChlHolddownTm_Object=MibTableColumn
h3cDot11RRMSDRdGrpChlHolddownTm=_H3cDot11RRMSDRdGrpChlHolddownTm_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4,1,3),_H3cDot11RRMSDRdGrpChlHolddownTm_Type())
h3cDot11RRMSDRdGrpChlHolddownTm.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11RRMSDRdGrpChlHolddownTm.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMSDRdGrpChlHolddownTm.setUnits(_P)
_H3cDot11RRMSDRdGrpPwrHolddownTm_Type=Unsigned32
_H3cDot11RRMSDRdGrpPwrHolddownTm_Object=MibTableColumn
h3cDot11RRMSDRdGrpPwrHolddownTm=_H3cDot11RRMSDRdGrpPwrHolddownTm_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4,1,4),_H3cDot11RRMSDRdGrpPwrHolddownTm_Type())
h3cDot11RRMSDRdGrpPwrHolddownTm.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11RRMSDRdGrpPwrHolddownTm.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMSDRdGrpPwrHolddownTm.setUnits(_P)
_H3cDot11RRMSDRdGroupRowStatus_Type=RowStatus
_H3cDot11RRMSDRdGroupRowStatus_Object=MibTableColumn
h3cDot11RRMSDRdGroupRowStatus=_H3cDot11RRMSDRdGroupRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,4,1,5),_H3cDot11RRMSDRdGroupRowStatus_Type())
h3cDot11RRMSDRdGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDot11RRMSDRdGroupRowStatus.setStatus(_A)
_H3cDot11RRMAPCfg2Table_Object=MibTable
h3cDot11RRMAPCfg2Table=_H3cDot11RRMAPCfg2Table_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5))
if mibBuilder.loadTexts:h3cDot11RRMAPCfg2Table.setStatus(_A)
_H3cDot11RRMAPCfg2Entry_Object=MibTableRow
h3cDot11RRMAPCfg2Entry=_H3cDot11RRMAPCfg2Entry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5,1))
h3cDot11RRMAPCfg2Entry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:h3cDot11RRMAPCfg2Entry.setStatus(_A)
_H3cDot11RRMAPSerialID_Type=H3cDot11ObjectIDType
_H3cDot11RRMAPSerialID_Object=MibTableColumn
h3cDot11RRMAPSerialID=_H3cDot11RRMAPSerialID_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5,1,1),_H3cDot11RRMAPSerialID_Type())
h3cDot11RRMAPSerialID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11RRMAPSerialID.setStatus(_A)
_H3cDot11RRMAPIntfThreshold_Type=Integer32
_H3cDot11RRMAPIntfThreshold_Object=MibTableColumn
h3cDot11RRMAPIntfThreshold=_H3cDot11RRMAPIntfThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5,1,2),_H3cDot11RRMAPIntfThreshold_Type())
h3cDot11RRMAPIntfThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMAPIntfThreshold.setStatus(_A)
_H3cDot11RRMStaIntfThreshold_Type=Integer32
_H3cDot11RRMStaIntfThreshold_Object=MibTableColumn
h3cDot11RRMStaIntfThreshold=_H3cDot11RRMStaIntfThreshold_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5,1,3),_H3cDot11RRMStaIntfThreshold_Type())
h3cDot11RRMStaIntfThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMStaIntfThreshold.setStatus(_A)
_H3cDot11RRMCoChlIntfTrapThhd_Type=Integer32
_H3cDot11RRMCoChlIntfTrapThhd_Object=MibTableColumn
h3cDot11RRMCoChlIntfTrapThhd=_H3cDot11RRMCoChlIntfTrapThhd_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5,1,4),_H3cDot11RRMCoChlIntfTrapThhd_Type())
h3cDot11RRMCoChlIntfTrapThhd.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMCoChlIntfTrapThhd.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMCoChlIntfTrapThhd.setUnits(_Q)
_H3cDot11RRMAdjChlIntfTrapThhd_Type=Integer32
_H3cDot11RRMAdjChlIntfTrapThhd_Object=MibTableColumn
h3cDot11RRMAdjChlIntfTrapThhd=_H3cDot11RRMAdjChlIntfTrapThhd_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,1,5,1,5),_H3cDot11RRMAdjChlIntfTrapThhd_Type())
h3cDot11RRMAdjChlIntfTrapThhd.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMAdjChlIntfTrapThhd.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMAdjChlIntfTrapThhd.setUnits(_Q)
_H3cDot11RRMDetectGroup_ObjectIdentity=ObjectIdentity
h3cDot11RRMDetectGroup=_H3cDot11RRMDetectGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,2))
_H3cDot11RRMChlRptTable_Object=MibTable
h3cDot11RRMChlRptTable=_H3cDot11RRMChlRptTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1))
if mibBuilder.loadTexts:h3cDot11RRMChlRptTable.setStatus(_A)
_H3cDot11RRMChlRptEntry_Object=MibTableRow
h3cDot11RRMChlRptEntry=_H3cDot11RRMChlRptEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1))
h3cDot11RRMChlRptEntry.setIndexNames((0,_E,_I),(0,_E,_W))
if mibBuilder.loadTexts:h3cDot11RRMChlRptEntry.setStatus(_A)
_H3cDot11RRMRadioIndex_Type=H3cDot11RadioElementIndex
_H3cDot11RRMRadioIndex_Object=MibTableColumn
h3cDot11RRMRadioIndex=_H3cDot11RRMRadioIndex_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,1),_H3cDot11RRMRadioIndex_Type())
h3cDot11RRMRadioIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11RRMRadioIndex.setStatus(_A)
_H3cDot11RRMChlRptChlNum_Type=Integer32
_H3cDot11RRMChlRptChlNum_Object=MibTableColumn
h3cDot11RRMChlRptChlNum=_H3cDot11RRMChlRptChlNum_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,2),_H3cDot11RRMChlRptChlNum_Type())
h3cDot11RRMChlRptChlNum.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11RRMChlRptChlNum.setStatus(_A)
class _H3cDot11RRMChlRptChlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primeChannel',1),('offChannel',2)))
_H3cDot11RRMChlRptChlType_Type.__name__=_C
_H3cDot11RRMChlRptChlType_Object=MibTableColumn
h3cDot11RRMChlRptChlType=_H3cDot11RRMChlRptChlType_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,3),_H3cDot11RRMChlRptChlType_Type())
h3cDot11RRMChlRptChlType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptChlType.setStatus(_A)
class _H3cDot11RRMChlRptChlQlty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_H3cDot11RRMChlRptChlQlty_Type.__name__=_C
_H3cDot11RRMChlRptChlQlty_Object=MibTableColumn
h3cDot11RRMChlRptChlQlty=_H3cDot11RRMChlRptChlQlty_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,4),_H3cDot11RRMChlRptChlQlty_Type())
h3cDot11RRMChlRptChlQlty.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptChlQlty.setStatus(_A)
_H3cDot11RRMChlRptNbrCnt_Type=Integer32
_H3cDot11RRMChlRptNbrCnt_Object=MibTableColumn
h3cDot11RRMChlRptNbrCnt=_H3cDot11RRMChlRptNbrCnt_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,5),_H3cDot11RRMChlRptNbrCnt_Type())
h3cDot11RRMChlRptNbrCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptNbrCnt.setStatus(_A)
class _H3cDot11RRMChlRptLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMChlRptLoad_Type.__name__=_C
_H3cDot11RRMChlRptLoad_Object=MibTableColumn
h3cDot11RRMChlRptLoad=_H3cDot11RRMChlRptLoad_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,6),_H3cDot11RRMChlRptLoad_Type())
h3cDot11RRMChlRptLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptLoad.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMChlRptLoad.setUnits(_F)
class _H3cDot11RRMChlRptUtlz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMChlRptUtlz_Type.__name__=_C
_H3cDot11RRMChlRptUtlz_Object=MibTableColumn
h3cDot11RRMChlRptUtlz=_H3cDot11RRMChlRptUtlz_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,7),_H3cDot11RRMChlRptUtlz_Type())
h3cDot11RRMChlRptUtlz.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptUtlz.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMChlRptUtlz.setUnits(_F)
class _H3cDot11RRMChlRptIntrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMChlRptIntrf_Type.__name__=_C
_H3cDot11RRMChlRptIntrf_Object=MibTableColumn
h3cDot11RRMChlRptIntrf=_H3cDot11RRMChlRptIntrf_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,8),_H3cDot11RRMChlRptIntrf_Type())
h3cDot11RRMChlRptIntrf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptIntrf.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMChlRptIntrf.setUnits(_F)
class _H3cDot11RRMChlRptPER_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMChlRptPER_Type.__name__=_C
_H3cDot11RRMChlRptPER_Object=MibTableColumn
h3cDot11RRMChlRptPER=_H3cDot11RRMChlRptPER_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,9),_H3cDot11RRMChlRptPER_Type())
h3cDot11RRMChlRptPER.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptPER.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMChlRptPER.setUnits(_F)
class _H3cDot11RRMChlRptRetryRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMChlRptRetryRate_Type.__name__=_C
_H3cDot11RRMChlRptRetryRate_Object=MibTableColumn
h3cDot11RRMChlRptRetryRate=_H3cDot11RRMChlRptRetryRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,10),_H3cDot11RRMChlRptRetryRate_Type())
h3cDot11RRMChlRptRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptRetryRate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMChlRptRetryRate.setUnits(_F)
_H3cDot11RRMChlRptNoise_Type=Integer32
_H3cDot11RRMChlRptNoise_Object=MibTableColumn
h3cDot11RRMChlRptNoise=_H3cDot11RRMChlRptNoise_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,11),_H3cDot11RRMChlRptNoise_Type())
h3cDot11RRMChlRptNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMChlRptNoise.setStatus(_A)
class _H3cDot11RRMChlRptRadarIndtcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notDetected',2)))
_H3cDot11RRMChlRptRadarIndtcr_Type.__name__=_C
_H3cDot11RRMChlRptRadarIndtcr_Object=MibTableColumn
h3cDot11RRMChlRptRadarIndtcr=_H3cDot11RRMChlRptRadarIndtcr_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,1,1,12),_H3cDot11RRMChlRptRadarIndtcr_Type())
h3cDot11RRMChlRptRadarIndtcr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11RRMChlRptRadarIndtcr.setStatus(_A)
_H3cDot11RRMNbrInfoTable_Object=MibTable
h3cDot11RRMNbrInfoTable=_H3cDot11RRMNbrInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2))
if mibBuilder.loadTexts:h3cDot11RRMNbrInfoTable.setStatus(_A)
_H3cDot11RRMNbrInfoEntry_Object=MibTableRow
h3cDot11RRMNbrInfoEntry=_H3cDot11RRMNbrInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1))
h3cDot11RRMNbrInfoEntry.setIndexNames((0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:h3cDot11RRMNbrInfoEntry.setStatus(_A)
_H3cDot11RrmNbrBSSID_Type=MacAddress
_H3cDot11RrmNbrBSSID_Object=MibTableColumn
h3cDot11RrmNbrBSSID=_H3cDot11RrmNbrBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1,1),_H3cDot11RrmNbrBSSID_Type())
h3cDot11RrmNbrBSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11RrmNbrBSSID.setStatus(_A)
_H3cDot11RrmNbrChl_Type=H3cDot11ChannelScopeType
_H3cDot11RrmNbrChl_Object=MibTableColumn
h3cDot11RrmNbrChl=_H3cDot11RrmNbrChl_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1,2),_H3cDot11RrmNbrChl_Type())
h3cDot11RrmNbrChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RrmNbrChl.setStatus(_A)
class _H3cDot11RRMNbrIntrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMNbrIntrf_Type.__name__=_C
_H3cDot11RRMNbrIntrf_Object=MibTableColumn
h3cDot11RRMNbrIntrf=_H3cDot11RRMNbrIntrf_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1,3),_H3cDot11RRMNbrIntrf_Type())
h3cDot11RRMNbrIntrf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMNbrIntrf.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMNbrIntrf.setUnits(_F)
_H3cDot11RrmNbrRSSI_Type=Integer32
_H3cDot11RrmNbrRSSI_Object=MibTableColumn
h3cDot11RrmNbrRSSI=_H3cDot11RrmNbrRSSI_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1,4),_H3cDot11RrmNbrRSSI_Type())
h3cDot11RrmNbrRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RrmNbrRSSI.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RrmNbrRSSI.setUnits(_O)
class _H3cDot11RrmNbrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('managed',1),('unmanaged',2)))
_H3cDot11RrmNbrType_Type.__name__=_C
_H3cDot11RrmNbrType_Object=MibTableColumn
h3cDot11RrmNbrType=_H3cDot11RrmNbrType_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1,5),_H3cDot11RrmNbrType_Type())
h3cDot11RrmNbrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RrmNbrType.setStatus(_A)
_H3cDot11RrmNbrSSID_Type=H3cDot11SSIDStringType
_H3cDot11RrmNbrSSID_Object=MibTableColumn
h3cDot11RrmNbrSSID=_H3cDot11RrmNbrSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,2,1,6),_H3cDot11RrmNbrSSID_Type())
h3cDot11RrmNbrSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RrmNbrSSID.setStatus(_A)
_H3cDot11RRMHistoryTable_Object=MibTable
h3cDot11RRMHistoryTable=_H3cDot11RRMHistoryTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3))
if mibBuilder.loadTexts:h3cDot11RRMHistoryTable.setStatus(_A)
_H3cDot11RRMHistoryEntry_Object=MibTableRow
h3cDot11RRMHistoryEntry=_H3cDot11RRMHistoryEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1))
h3cDot11RRMHistoryEntry.setIndexNames((0,_E,_I),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:h3cDot11RRMHistoryEntry.setStatus(_A)
_H3cDot11RRMHistoryId_Type=Integer32
_H3cDot11RRMHistoryId_Object=MibTableColumn
h3cDot11RRMHistoryId=_H3cDot11RRMHistoryId_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,1),_H3cDot11RRMHistoryId_Type())
h3cDot11RRMHistoryId.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11RRMHistoryId.setStatus(_A)
class _H3cDot11RRMHistoryRecIndctr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('before',1),('after',2)))
_H3cDot11RRMHistoryRecIndctr_Type.__name__=_C
_H3cDot11RRMHistoryRecIndctr_Object=MibTableColumn
h3cDot11RRMHistoryRecIndctr=_H3cDot11RRMHistoryRecIndctr_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,2),_H3cDot11RRMHistoryRecIndctr_Type())
h3cDot11RRMHistoryRecIndctr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11RRMHistoryRecIndctr.setStatus(_A)
_H3cDot11RRMHistoryChl_Type=H3cDot11ChannelScopeType
_H3cDot11RRMHistoryChl_Object=MibTableColumn
h3cDot11RRMHistoryChl=_H3cDot11RRMHistoryChl_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,3),_H3cDot11RRMHistoryChl_Type())
h3cDot11RRMHistoryChl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryChl.setStatus(_A)
_H3cDot11RRMHistoryPwr_Type=Integer32
_H3cDot11RRMHistoryPwr_Object=MibTableColumn
h3cDot11RRMHistoryPwr=_H3cDot11RRMHistoryPwr_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,4),_H3cDot11RRMHistoryPwr_Type())
h3cDot11RRMHistoryPwr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryPwr.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMHistoryPwr.setUnits(_O)
class _H3cDot11RRMHistoryLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMHistoryLoad_Type.__name__=_C
_H3cDot11RRMHistoryLoad_Object=MibTableColumn
h3cDot11RRMHistoryLoad=_H3cDot11RRMHistoryLoad_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,5),_H3cDot11RRMHistoryLoad_Type())
h3cDot11RRMHistoryLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryLoad.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMHistoryLoad.setUnits(_F)
class _H3cDot11RRMHistoryUtlz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMHistoryUtlz_Type.__name__=_C
_H3cDot11RRMHistoryUtlz_Object=MibTableColumn
h3cDot11RRMHistoryUtlz=_H3cDot11RRMHistoryUtlz_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,6),_H3cDot11RRMHistoryUtlz_Type())
h3cDot11RRMHistoryUtlz.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryUtlz.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMHistoryUtlz.setUnits(_F)
class _H3cDot11RRMHistoryIntrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMHistoryIntrf_Type.__name__=_C
_H3cDot11RRMHistoryIntrf_Object=MibTableColumn
h3cDot11RRMHistoryIntrf=_H3cDot11RRMHistoryIntrf_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,7),_H3cDot11RRMHistoryIntrf_Type())
h3cDot11RRMHistoryIntrf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryIntrf.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMHistoryIntrf.setUnits(_F)
_H3cDot11RRMHistoryNoise_Type=Integer32
_H3cDot11RRMHistoryNoise_Object=MibTableColumn
h3cDot11RRMHistoryNoise=_H3cDot11RRMHistoryNoise_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,8),_H3cDot11RRMHistoryNoise_Type())
h3cDot11RRMHistoryNoise.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryNoise.setStatus(_A)
class _H3cDot11RRMHistoryPER_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMHistoryPER_Type.__name__=_C
_H3cDot11RRMHistoryPER_Object=MibTableColumn
h3cDot11RRMHistoryPER=_H3cDot11RRMHistoryPER_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,9),_H3cDot11RRMHistoryPER_Type())
h3cDot11RRMHistoryPER.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryPER.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMHistoryPER.setUnits(_F)
class _H3cDot11RRMHistoryRetryRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDot11RRMHistoryRetryRate_Type.__name__=_C
_H3cDot11RRMHistoryRetryRate_Object=MibTableColumn
h3cDot11RRMHistoryRetryRate=_H3cDot11RRMHistoryRetryRate_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,10),_H3cDot11RRMHistoryRetryRate_Type())
h3cDot11RRMHistoryRetryRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryRetryRate.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11RRMHistoryRetryRate.setUnits(_F)
class _H3cDot11RRMHistoryChgReason_Type(Bits):namedValues=NamedValues(*(('others',0),('coverage',1),('radar',2),('retransmission',3),('packetsDiscarded',4),('interference',5)))
_H3cDot11RRMHistoryChgReason_Type.__name__='Bits'
_H3cDot11RRMHistoryChgReason_Object=MibTableColumn
h3cDot11RRMHistoryChgReason=_H3cDot11RRMHistoryChgReason_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,11),_H3cDot11RRMHistoryChgReason_Type())
h3cDot11RRMHistoryChgReason.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryChgReason.setStatus(_A)
_H3cDot11RRMHistoryChgDateTime_Type=DateAndTime
_H3cDot11RRMHistoryChgDateTime_Object=MibTableColumn
h3cDot11RRMHistoryChgDateTime=_H3cDot11RRMHistoryChgDateTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,2,3,1,12),_H3cDot11RRMHistoryChgDateTime_Type())
h3cDot11RRMHistoryChgDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11RRMHistoryChgDateTime.setStatus(_A)
_H3cDot11RRMNotifyGroup_ObjectIdentity=ObjectIdentity
h3cDot11RRMNotifyGroup=_H3cDot11RRMNotifyGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,3))
_H3cDot11RRMChlQltyNotifications_ObjectIdentity=ObjectIdentity
h3cDot11RRMChlQltyNotifications=_H3cDot11RRMChlQltyNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,3,1))
_H3cDot11RRMChlQltyNtfPrefix_ObjectIdentity=ObjectIdentity
h3cDot11RRMChlQltyNtfPrefix=_H3cDot11RRMChlQltyNtfPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,3,1,0))
_H3cDot11RRMResChgNotifications_ObjectIdentity=ObjectIdentity
h3cDot11RRMResChgNotifications=_H3cDot11RRMResChgNotifications_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,3,2))
_H3cDot11RRMResChgNtfPrefix_ObjectIdentity=ObjectIdentity
h3cDot11RRMResChgNtfPrefix=_H3cDot11RRMResChgNtfPrefix_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,3,2,0))
_H3cDot11RRMNotificationsVar_ObjectIdentity=ObjectIdentity
h3cDot11RRMNotificationsVar=_H3cDot11RRMNotificationsVar_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,3,3))
_H3cDot11NewPower_Type=Integer32
_H3cDot11NewPower_Object=MibScalar
h3cDot11NewPower=_H3cDot11NewPower_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,3,3,1),_H3cDot11NewPower_Type())
h3cDot11NewPower.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11NewPower.setStatus(_A)
_H3cDot11OldPower_Type=Integer32
_H3cDot11OldPower_Object=MibScalar
h3cDot11OldPower=_H3cDot11OldPower_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,3,3,2),_H3cDot11OldPower_Type())
h3cDot11OldPower.setMaxAccess(_K)
if mibBuilder.loadTexts:h3cDot11OldPower.setStatus(_A)
_H3cDot11MonitorDetectedGroup_ObjectIdentity=ObjectIdentity
h3cDot11MonitorDetectedGroup=_H3cDot11MonitorDetectedGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,75,8,4))
_H3cDot11MonitorDetectedDevTable_Object=MibTable
h3cDot11MonitorDetectedDevTable=_H3cDot11MonitorDetectedDevTable_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1))
if mibBuilder.loadTexts:h3cDot11MonitorDetectedDevTable.setStatus(_A)
_H3cDot11MonitorDetectedDevEntry_Object=MibTableRow
h3cDot11MonitorDetectedDevEntry=_H3cDot11MonitorDetectedDevEntry_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1))
h3cDot11MonitorDetectedDevEntry.setIndexNames((0,_E,_a),(0,_L,_M))
if mibBuilder.loadTexts:h3cDot11MonitorDetectedDevEntry.setStatus(_A)
_H3cDot11MonitorDevMAC_Type=MacAddress
_H3cDot11MonitorDevMAC_Object=MibTableColumn
h3cDot11MonitorDevMAC=_H3cDot11MonitorDevMAC_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,1),_H3cDot11MonitorDevMAC_Type())
h3cDot11MonitorDevMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDot11MonitorDevMAC.setStatus(_A)
class _H3cDot11MonitorDevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('client',1),('ap',2),('adhoc',3),('wirelessBridge',4),('unknown',5)))
_H3cDot11MonitorDevType_Type.__name__=_C
_H3cDot11MonitorDevType_Object=MibTableColumn
h3cDot11MonitorDevType=_H3cDot11MonitorDevType_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,2),_H3cDot11MonitorDevType_Type())
h3cDot11MonitorDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevType.setStatus(_A)
_H3cDot11MonitorDevVendor_Type=OctetString
_H3cDot11MonitorDevVendor_Object=MibTableColumn
h3cDot11MonitorDevVendor=_H3cDot11MonitorDevVendor_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,3),_H3cDot11MonitorDevVendor_Type())
h3cDot11MonitorDevVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevVendor.setStatus(_A)
_H3cDot11MonitorDevSSID_Type=OctetString
_H3cDot11MonitorDevSSID_Object=MibTableColumn
h3cDot11MonitorDevSSID=_H3cDot11MonitorDevSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,4),_H3cDot11MonitorDevSSID_Type())
h3cDot11MonitorDevSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevSSID.setStatus(_A)
_H3cDot11MonitorDevBSSID_Type=MacAddress
_H3cDot11MonitorDevBSSID_Object=MibTableColumn
h3cDot11MonitorDevBSSID=_H3cDot11MonitorDevBSSID_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,5),_H3cDot11MonitorDevBSSID_Type())
h3cDot11MonitorDevBSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevBSSID.setStatus(_A)
_H3cDot11MonitorDevChannel_Type=H3cDot11ChannelScopeType
_H3cDot11MonitorDevChannel_Object=MibTableColumn
h3cDot11MonitorDevChannel=_H3cDot11MonitorDevChannel_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,6),_H3cDot11MonitorDevChannel_Type())
h3cDot11MonitorDevChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevChannel.setStatus(_A)
_H3cDot11MonitorRadioId_Type=H3cDot11RadioScopeType
_H3cDot11MonitorRadioId_Object=MibTableColumn
h3cDot11MonitorRadioId=_H3cDot11MonitorRadioId_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,7),_H3cDot11MonitorRadioId_Type())
h3cDot11MonitorRadioId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorRadioId.setStatus(_A)
_H3cDot11MonitorDevMaxRSSI_Type=Integer32
_H3cDot11MonitorDevMaxRSSI_Object=MibTableColumn
h3cDot11MonitorDevMaxRSSI=_H3cDot11MonitorDevMaxRSSI_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,8),_H3cDot11MonitorDevMaxRSSI_Type())
h3cDot11MonitorDevMaxRSSI.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevMaxRSSI.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11MonitorDevMaxRSSI.setUnits(_Q)
_H3cDot11MonitorDevBeaconIntvl_Type=Integer32
_H3cDot11MonitorDevBeaconIntvl_Object=MibTableColumn
h3cDot11MonitorDevBeaconIntvl=_H3cDot11MonitorDevBeaconIntvl_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,9),_H3cDot11MonitorDevBeaconIntvl_Type())
h3cDot11MonitorDevBeaconIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevBeaconIntvl.setStatus(_A)
if mibBuilder.loadTexts:h3cDot11MonitorDevBeaconIntvl.setUnits('millisecond')
_H3cDot11MonitorDevFstDctTime_Type=DateAndTime
_H3cDot11MonitorDevFstDctTime_Object=MibTableColumn
h3cDot11MonitorDevFstDctTime=_H3cDot11MonitorDevFstDctTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,10),_H3cDot11MonitorDevFstDctTime_Type())
h3cDot11MonitorDevFstDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevFstDctTime.setStatus(_A)
_H3cDot11MonitorDevLstDctTime_Type=DateAndTime
_H3cDot11MonitorDevLstDctTime_Object=MibTableColumn
h3cDot11MonitorDevLstDctTime=_H3cDot11MonitorDevLstDctTime_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,11),_H3cDot11MonitorDevLstDctTime_Type())
h3cDot11MonitorDevLstDctTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevLstDctTime.setStatus(_A)
_H3cDot11MonitorDevClear_Type=TruthValue
_H3cDot11MonitorDevClear_Object=MibTableColumn
h3cDot11MonitorDevClear=_H3cDot11MonitorDevClear_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,12),_H3cDot11MonitorDevClear_Type())
h3cDot11MonitorDevClear.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDot11MonitorDevClear.setStatus(_A)
_H3cDot11MonitorDevSNR_Type=Integer32
_H3cDot11MonitorDevSNR_Object=MibTableColumn
h3cDot11MonitorDevSNR=_H3cDot11MonitorDevSNR_Object((1,3,6,1,4,1,43,45,1,10,2,75,8,4,1,1,13),_H3cDot11MonitorDevSNR_Type())
h3cDot11MonitorDevSNR.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDot11MonitorDevSNR.setStatus(_A)
h3cDot11RRMIntrfLimit=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,8,3,1,0,1))
h3cDot11RRMIntrfLimit.setObjects((_E,_b))
if mibBuilder.loadTexts:h3cDot11RRMIntrfLimit.setStatus(_A)
h3cDot11RRMPERLimit=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,8,3,1,0,2))
h3cDot11RRMPERLimit.setObjects((_E,_c))
if mibBuilder.loadTexts:h3cDot11RRMPERLimit.setStatus(_A)
h3cDot11RRMNoiseLimit=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,8,3,1,0,3))
h3cDot11RRMNoiseLimit.setObjects((_E,_d))
if mibBuilder.loadTexts:h3cDot11RRMNoiseLimit.setStatus(_A)
h3cDot11RRMPowerChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,75,8,3,2,0,1))
h3cDot11RRMPowerChange.setObjects(*((_E,_I),(_E,_e),(_E,_f)))
if mibBuilder.loadTexts:h3cDot11RRMPowerChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cDot11RRM':h3cDot11RRM,'h3cDot11RRMConfigGroup':h3cDot11RRMConfigGroup,'h3cDot11RRMGlobalCfgPara':h3cDot11RRMGlobalCfgPara,'h3cDot11RRM11nMadtMaxMcs':h3cDot11RRM11nMadtMaxMcs,'h3cDot11RRM11nSuptMaxMcs':h3cDot11RRM11nSuptMaxMcs,'h3cDot11RRM11gProtect':h3cDot11RRM11gProtect,'h3cDot11RRM11aPwrConstrt':h3cDot11RRM11aPwrConstrt,'h3cDot11RRM11aSpectrumManag':h3cDot11RRM11aSpectrumManag,'h3cDot11RRMAutoChlAvoid11h':h3cDot11RRMAutoChlAvoid11h,'h3cDot11RRMScanChl':h3cDot11RRMScanChl,'h3cDot11RRMScanRptIntvel':h3cDot11RRMScanRptIntvel,'h3cDot11APInterfNumThreshhd':h3cDot11APInterfNumThreshhd,'h3cDot11StaInterfNumThreshhd':h3cDot11StaInterfNumThreshhd,'h3cDot11RRMRadioCfgTable':h3cDot11RRMRadioCfgTable,'h3cDot11RRMRadioCfgEntry':h3cDot11RRMRadioCfgEntry,_R:h3cDot11RRMRadioType,'h3cDot11RRMCfgChlState':h3cDot11RRMCfgChlState,'h3cDot11RRMCfgChlMode':h3cDot11RRMCfgChlMode,'h3cDot11RRMChlProntoRadioElmt':h3cDot11RRMChlProntoRadioElmt,'h3cDot11RRMCfgPwrState':h3cDot11RRMCfgPwrState,'h3cDot11RRMCfgPwrMode':h3cDot11RRMCfgPwrMode,'h3cDot11RRMPwrProntoRadioElmt':h3cDot11RRMPwrProntoRadioElmt,'h3cDot11RRMCfgIntrvl':h3cDot11RRMCfgIntrvl,'h3cDot11RRMCfgIntrfThres':h3cDot11RRMCfgIntrfThres,'h3cDot11RRMCfgNoiseThres':h3cDot11RRMCfgNoiseThres,'h3cDot11RRMCfgPERThres':h3cDot11RRMCfgPERThres,'h3cDot11RRMCfgToleranceFctr':h3cDot11RRMCfgToleranceFctr,'h3cDot11RRMCfgAdjacencyFctr':h3cDot11RRMCfgAdjacencyFctr,'h3cDot11RRMAPCfgTable':h3cDot11RRMAPCfgTable,'h3cDot11RRMAPCfgEntry':h3cDot11RRMAPCfgEntry,'h3cDot11RRMAPWorkMode':h3cDot11RRMAPWorkMode,'h3cDot11RRMSDRadioGroupTable':h3cDot11RRMSDRadioGroupTable,'h3cDot11RRMSDRadioGroupEntry':h3cDot11RRMSDRadioGroupEntry,_U:h3cDot11RRMSDRadioGroupId,'h3cDot11RRMSDRadioGroupDesc':h3cDot11RRMSDRadioGroupDesc,'h3cDot11RRMSDRdGrpChlHolddownTm':h3cDot11RRMSDRdGrpChlHolddownTm,'h3cDot11RRMSDRdGrpPwrHolddownTm':h3cDot11RRMSDRdGrpPwrHolddownTm,'h3cDot11RRMSDRdGroupRowStatus':h3cDot11RRMSDRdGroupRowStatus,'h3cDot11RRMAPCfg2Table':h3cDot11RRMAPCfg2Table,'h3cDot11RRMAPCfg2Entry':h3cDot11RRMAPCfg2Entry,_V:h3cDot11RRMAPSerialID,'h3cDot11RRMAPIntfThreshold':h3cDot11RRMAPIntfThreshold,'h3cDot11RRMStaIntfThreshold':h3cDot11RRMStaIntfThreshold,'h3cDot11RRMCoChlIntfTrapThhd':h3cDot11RRMCoChlIntfTrapThhd,'h3cDot11RRMAdjChlIntfTrapThhd':h3cDot11RRMAdjChlIntfTrapThhd,'h3cDot11RRMDetectGroup':h3cDot11RRMDetectGroup,'h3cDot11RRMChlRptTable':h3cDot11RRMChlRptTable,'h3cDot11RRMChlRptEntry':h3cDot11RRMChlRptEntry,_I:h3cDot11RRMRadioIndex,_W:h3cDot11RRMChlRptChlNum,'h3cDot11RRMChlRptChlType':h3cDot11RRMChlRptChlType,'h3cDot11RRMChlRptChlQlty':h3cDot11RRMChlRptChlQlty,'h3cDot11RRMChlRptNbrCnt':h3cDot11RRMChlRptNbrCnt,'h3cDot11RRMChlRptLoad':h3cDot11RRMChlRptLoad,'h3cDot11RRMChlRptUtlz':h3cDot11RRMChlRptUtlz,_b:h3cDot11RRMChlRptIntrf,_c:h3cDot11RRMChlRptPER,'h3cDot11RRMChlRptRetryRate':h3cDot11RRMChlRptRetryRate,_d:h3cDot11RRMChlRptNoise,'h3cDot11RRMChlRptRadarIndtcr':h3cDot11RRMChlRptRadarIndtcr,'h3cDot11RRMNbrInfoTable':h3cDot11RRMNbrInfoTable,'h3cDot11RRMNbrInfoEntry':h3cDot11RRMNbrInfoEntry,_X:h3cDot11RrmNbrBSSID,'h3cDot11RrmNbrChl':h3cDot11RrmNbrChl,'h3cDot11RRMNbrIntrf':h3cDot11RRMNbrIntrf,'h3cDot11RrmNbrRSSI':h3cDot11RrmNbrRSSI,'h3cDot11RrmNbrType':h3cDot11RrmNbrType,'h3cDot11RrmNbrSSID':h3cDot11RrmNbrSSID,'h3cDot11RRMHistoryTable':h3cDot11RRMHistoryTable,'h3cDot11RRMHistoryEntry':h3cDot11RRMHistoryEntry,_Y:h3cDot11RRMHistoryId,_Z:h3cDot11RRMHistoryRecIndctr,'h3cDot11RRMHistoryChl':h3cDot11RRMHistoryChl,'h3cDot11RRMHistoryPwr':h3cDot11RRMHistoryPwr,'h3cDot11RRMHistoryLoad':h3cDot11RRMHistoryLoad,'h3cDot11RRMHistoryUtlz':h3cDot11RRMHistoryUtlz,'h3cDot11RRMHistoryIntrf':h3cDot11RRMHistoryIntrf,'h3cDot11RRMHistoryNoise':h3cDot11RRMHistoryNoise,'h3cDot11RRMHistoryPER':h3cDot11RRMHistoryPER,'h3cDot11RRMHistoryRetryRate':h3cDot11RRMHistoryRetryRate,'h3cDot11RRMHistoryChgReason':h3cDot11RRMHistoryChgReason,'h3cDot11RRMHistoryChgDateTime':h3cDot11RRMHistoryChgDateTime,'h3cDot11RRMNotifyGroup':h3cDot11RRMNotifyGroup,'h3cDot11RRMChlQltyNotifications':h3cDot11RRMChlQltyNotifications,'h3cDot11RRMChlQltyNtfPrefix':h3cDot11RRMChlQltyNtfPrefix,'h3cDot11RRMIntrfLimit':h3cDot11RRMIntrfLimit,'h3cDot11RRMPERLimit':h3cDot11RRMPERLimit,'h3cDot11RRMNoiseLimit':h3cDot11RRMNoiseLimit,'h3cDot11RRMResChgNotifications':h3cDot11RRMResChgNotifications,'h3cDot11RRMResChgNtfPrefix':h3cDot11RRMResChgNtfPrefix,'h3cDot11RRMPowerChange':h3cDot11RRMPowerChange,'h3cDot11RRMNotificationsVar':h3cDot11RRMNotificationsVar,_e:h3cDot11NewPower,_f:h3cDot11OldPower,'h3cDot11MonitorDetectedGroup':h3cDot11MonitorDetectedGroup,'h3cDot11MonitorDetectedDevTable':h3cDot11MonitorDetectedDevTable,'h3cDot11MonitorDetectedDevEntry':h3cDot11MonitorDetectedDevEntry,_a:h3cDot11MonitorDevMAC,'h3cDot11MonitorDevType':h3cDot11MonitorDevType,'h3cDot11MonitorDevVendor':h3cDot11MonitorDevVendor,'h3cDot11MonitorDevSSID':h3cDot11MonitorDevSSID,'h3cDot11MonitorDevBSSID':h3cDot11MonitorDevBSSID,'h3cDot11MonitorDevChannel':h3cDot11MonitorDevChannel,'h3cDot11MonitorRadioId':h3cDot11MonitorRadioId,'h3cDot11MonitorDevMaxRSSI':h3cDot11MonitorDevMaxRSSI,'h3cDot11MonitorDevBeaconIntvl':h3cDot11MonitorDevBeaconIntvl,'h3cDot11MonitorDevFstDctTime':h3cDot11MonitorDevFstDctTime,'h3cDot11MonitorDevLstDctTime':h3cDot11MonitorDevLstDctTime,'h3cDot11MonitorDevClear':h3cDot11MonitorDevClear,'h3cDot11MonitorDevSNR':h3cDot11MonitorDevSNR})