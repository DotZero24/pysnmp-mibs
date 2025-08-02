_h='hpnicfDot11OldPower'
_g='hpnicfDot11NewPower'
_f='hpnicfDot11RRMChlRptNoise'
_e='hpnicfDot11RRMChlRptPER'
_d='hpnicfDot11RRMChlRptIntrf'
_c='hpnicfDot11MonitorDevMAC'
_b='hpnicfDot11RRMRadioNbrRadioID'
_a='hpnicfDot11RRMRadioNbrAPID'
_Z='hpnicfDot11RRMHistoryRecIndctr'
_Y='hpnicfDot11RRMHistoryId'
_X='hpnicfDot11RrmNbrBSSID'
_W='hpnicfDot11RRMChlRptChlNum'
_V='hpnicfDot11RRMAPSerialID'
_U='hpnicfDot11RRMSDRadioGroupId'
_T='userTriggered'
_S='selfDecisive'
_R='hpnicfDot11RRMRadioType'
_Q='dbm'
_P='minute'
_O='dBm'
_N='hpnicfDot11APElementIndex'
_M='HPN-ICF-DOT11-REF-MIB'
_L='accessible-for-notify'
_K='read-create'
_J='Unsigned32'
_I='hpnicfDot11RRMRadioIndex'
_H='TruthValue'
_G='not-accessible'
_F='percent'
_E='HPN-ICF-DOT11-RRM-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfDot11ChannelScopeType,HpnicfDot11ObjectIDType,HpnicfDot11RadioElementIndex,HpnicfDot11RadioScopeType,HpnicfDot11RadioType,HpnicfDot11SSIDStringType,hpnicfDot11,hpnicfDot11APElementIndex=mibBuilder.importSymbols(_M,'HpnicfDot11ChannelScopeType','HpnicfDot11ObjectIDType','HpnicfDot11RadioElementIndex','HpnicfDot11RadioScopeType','HpnicfDot11RadioType','HpnicfDot11SSIDStringType','hpnicfDot11',_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_H)
hpnicfDot11RRM=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8))
if mibBuilder.loadTexts:hpnicfDot11RRM.setRevisions(('2010-09-25 18:00','2010-02-23 18:00','2009-08-01 20:00','2009-05-07 20:00','2009-04-17 20:00','2008-07-14 14:29'))
_HpnicfDot11RRMConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMConfigGroup=_HpnicfDot11RRMConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1))
_HpnicfDot11RRMGlobalCfgPara_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMGlobalCfgPara=_HpnicfDot11RRMGlobalCfgPara_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1))
class _HpnicfDot11RRM11nMadtMaxMcs_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76),ValueRangeConstraint(255,255))
_HpnicfDot11RRM11nMadtMaxMcs_Type.__name__=_B
_HpnicfDot11RRM11nMadtMaxMcs_Object=MibScalar
hpnicfDot11RRM11nMadtMaxMcs=_HpnicfDot11RRM11nMadtMaxMcs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,1),_HpnicfDot11RRM11nMadtMaxMcs_Type())
hpnicfDot11RRM11nMadtMaxMcs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11nMadtMaxMcs.setStatus(_A)
class _HpnicfDot11RRM11nSuptMaxMcs_Type(Integer32):defaultValue=76;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76))
_HpnicfDot11RRM11nSuptMaxMcs_Type.__name__=_B
_HpnicfDot11RRM11nSuptMaxMcs_Object=MibScalar
hpnicfDot11RRM11nSuptMaxMcs=_HpnicfDot11RRM11nSuptMaxMcs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,2),_HpnicfDot11RRM11nSuptMaxMcs_Type())
hpnicfDot11RRM11nSuptMaxMcs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11nSuptMaxMcs.setStatus(_A)
class _HpnicfDot11RRM11gProtect_Type(TruthValue):defaultValue=2
_HpnicfDot11RRM11gProtect_Type.__name__=_H
_HpnicfDot11RRM11gProtect_Object=MibScalar
hpnicfDot11RRM11gProtect=_HpnicfDot11RRM11gProtect_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,3),_HpnicfDot11RRM11gProtect_Type())
hpnicfDot11RRM11gProtect.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11gProtect.setStatus(_A)
class _HpnicfDot11RRM11aPwrConstrt_Type(Integer32):defaultValue=0
_HpnicfDot11RRM11aPwrConstrt_Type.__name__=_B
_HpnicfDot11RRM11aPwrConstrt_Object=MibScalar
hpnicfDot11RRM11aPwrConstrt=_HpnicfDot11RRM11aPwrConstrt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,4),_HpnicfDot11RRM11aPwrConstrt_Type())
hpnicfDot11RRM11aPwrConstrt.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11aPwrConstrt.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRM11aPwrConstrt.setUnits(_O)
class _HpnicfDot11RRM11aSpectrumManag_Type(TruthValue):defaultValue=2
_HpnicfDot11RRM11aSpectrumManag_Type.__name__=_H
_HpnicfDot11RRM11aSpectrumManag_Object=MibScalar
hpnicfDot11RRM11aSpectrumManag=_HpnicfDot11RRM11aSpectrumManag_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,5),_HpnicfDot11RRM11aSpectrumManag_Type())
hpnicfDot11RRM11aSpectrumManag.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11aSpectrumManag.setStatus(_A)
class _HpnicfDot11RRMAutoChlAvoid11h_Type(TruthValue):defaultValue=2
_HpnicfDot11RRMAutoChlAvoid11h_Type.__name__=_H
_HpnicfDot11RRMAutoChlAvoid11h_Object=MibScalar
hpnicfDot11RRMAutoChlAvoid11h=_HpnicfDot11RRMAutoChlAvoid11h_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,6),_HpnicfDot11RRMAutoChlAvoid11h_Type())
hpnicfDot11RRMAutoChlAvoid11h.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMAutoChlAvoid11h.setStatus(_A)
class _HpnicfDot11RRMScanChl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('all',2)))
_HpnicfDot11RRMScanChl_Type.__name__=_B
_HpnicfDot11RRMScanChl_Object=MibScalar
hpnicfDot11RRMScanChl=_HpnicfDot11RRMScanChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,7),_HpnicfDot11RRMScanChl_Type())
hpnicfDot11RRMScanChl.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMScanChl.setStatus(_A)
class _HpnicfDot11RRMScanRptIntvel_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,120))
_HpnicfDot11RRMScanRptIntvel_Type.__name__=_B
_HpnicfDot11RRMScanRptIntvel_Object=MibScalar
hpnicfDot11RRMScanRptIntvel=_HpnicfDot11RRMScanRptIntvel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,8),_HpnicfDot11RRMScanRptIntvel_Type())
hpnicfDot11RRMScanRptIntvel.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMScanRptIntvel.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMScanRptIntvel.setUnits('second')
class _HpnicfDot11APInterfNumThreshhd_Type(Integer32):defaultValue=0
_HpnicfDot11APInterfNumThreshhd_Type.__name__=_B
_HpnicfDot11APInterfNumThreshhd_Object=MibScalar
hpnicfDot11APInterfNumThreshhd=_HpnicfDot11APInterfNumThreshhd_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,9),_HpnicfDot11APInterfNumThreshhd_Type())
hpnicfDot11APInterfNumThreshhd.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11APInterfNumThreshhd.setStatus(_A)
class _HpnicfDot11StaInterfNumThreshhd_Type(Integer32):defaultValue=0
_HpnicfDot11StaInterfNumThreshhd_Type.__name__=_B
_HpnicfDot11StaInterfNumThreshhd_Object=MibScalar
hpnicfDot11StaInterfNumThreshhd=_HpnicfDot11StaInterfNumThreshhd_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,10),_HpnicfDot11StaInterfNumThreshhd_Type())
hpnicfDot11StaInterfNumThreshhd.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11StaInterfNumThreshhd.setStatus(_A)
class _HpnicfDot11RRM11nMultiCastMcs_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,76),ValueRangeConstraint(4294967295,4294967295))
_HpnicfDot11RRM11nMultiCastMcs_Type.__name__=_J
_HpnicfDot11RRM11nMultiCastMcs_Object=MibScalar
hpnicfDot11RRM11nMultiCastMcs=_HpnicfDot11RRM11nMultiCastMcs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,11),_HpnicfDot11RRM11nMultiCastMcs_Type())
hpnicfDot11RRM11nMultiCastMcs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11nMultiCastMcs.setStatus(_A)
class _HpnicfDot11RRM11acMadtMaxNss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_HpnicfDot11RRM11acMadtMaxNss_Type.__name__=_B
_HpnicfDot11RRM11acMadtMaxNss_Object=MibScalar
hpnicfDot11RRM11acMadtMaxNss=_HpnicfDot11RRM11acMadtMaxNss_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,12),_HpnicfDot11RRM11acMadtMaxNss_Type())
hpnicfDot11RRM11acMadtMaxNss.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11acMadtMaxNss.setStatus(_A)
class _HpnicfDot11RRM11acSuptMaxNss_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_HpnicfDot11RRM11acSuptMaxNss_Type.__name__=_B
_HpnicfDot11RRM11acSuptMaxNss_Object=MibScalar
hpnicfDot11RRM11acSuptMaxNss=_HpnicfDot11RRM11acSuptMaxNss_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,13),_HpnicfDot11RRM11acSuptMaxNss_Type())
hpnicfDot11RRM11acSuptMaxNss.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11acSuptMaxNss.setStatus(_A)
class _HpnicfDot11RRM11acMultiCastNss_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_HpnicfDot11RRM11acMultiCastNss_Type.__name__=_B
_HpnicfDot11RRM11acMultiCastNss_Object=MibScalar
hpnicfDot11RRM11acMultiCastNss=_HpnicfDot11RRM11acMultiCastNss_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,14),_HpnicfDot11RRM11acMultiCastNss_Type())
hpnicfDot11RRM11acMultiCastNss.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11acMultiCastNss.setStatus(_A)
class _HpnicfDot11RRM11acMultiCastVhtMcs_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9),ValueRangeConstraint(255,255))
_HpnicfDot11RRM11acMultiCastVhtMcs_Type.__name__=_B
_HpnicfDot11RRM11acMultiCastVhtMcs_Object=MibScalar
hpnicfDot11RRM11acMultiCastVhtMcs=_HpnicfDot11RRM11acMultiCastVhtMcs_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,1,15),_HpnicfDot11RRM11acMultiCastVhtMcs_Type())
hpnicfDot11RRM11acMultiCastVhtMcs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRM11acMultiCastVhtMcs.setStatus(_A)
_HpnicfDot11RRMRadioCfgTable_Object=MibTable
hpnicfDot11RRMRadioCfgTable=_HpnicfDot11RRMRadioCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2))
if mibBuilder.loadTexts:hpnicfDot11RRMRadioCfgTable.setStatus(_A)
_HpnicfDot11RRMRadioCfgEntry_Object=MibTableRow
hpnicfDot11RRMRadioCfgEntry=_HpnicfDot11RRMRadioCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1))
hpnicfDot11RRMRadioCfgEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hpnicfDot11RRMRadioCfgEntry.setStatus(_A)
_HpnicfDot11RRMRadioType_Type=HpnicfDot11RadioType
_HpnicfDot11RRMRadioType_Object=MibTableColumn
hpnicfDot11RRMRadioType=_HpnicfDot11RRMRadioType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,1),_HpnicfDot11RRMRadioType_Type())
hpnicfDot11RRMRadioType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMRadioType.setStatus(_A)
class _HpnicfDot11RRMCfgChlState_Type(TruthValue):defaultValue=2
_HpnicfDot11RRMCfgChlState_Type.__name__=_H
_HpnicfDot11RRMCfgChlState_Object=MibTableColumn
hpnicfDot11RRMCfgChlState=_HpnicfDot11RRMCfgChlState_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,2),_HpnicfDot11RRMCfgChlState_Type())
hpnicfDot11RRMCfgChlState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgChlState.setStatus(_A)
class _HpnicfDot11RRMCfgChlMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_HpnicfDot11RRMCfgChlMode_Type.__name__=_B
_HpnicfDot11RRMCfgChlMode_Object=MibTableColumn
hpnicfDot11RRMCfgChlMode=_HpnicfDot11RRMCfgChlMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,3),_HpnicfDot11RRMCfgChlMode_Type())
hpnicfDot11RRMCfgChlMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgChlMode.setStatus(_A)
class _HpnicfDot11RRMChlProntoRadioElmt_Type(Unsigned32):defaultValue=0
_HpnicfDot11RRMChlProntoRadioElmt_Type.__name__=_J
_HpnicfDot11RRMChlProntoRadioElmt_Object=MibTableColumn
hpnicfDot11RRMChlProntoRadioElmt=_HpnicfDot11RRMChlProntoRadioElmt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,4),_HpnicfDot11RRMChlProntoRadioElmt_Type())
hpnicfDot11RRMChlProntoRadioElmt.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMChlProntoRadioElmt.setStatus(_A)
class _HpnicfDot11RRMCfgPwrState_Type(TruthValue):defaultValue=2
_HpnicfDot11RRMCfgPwrState_Type.__name__=_H
_HpnicfDot11RRMCfgPwrState_Object=MibTableColumn
hpnicfDot11RRMCfgPwrState=_HpnicfDot11RRMCfgPwrState_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,5),_HpnicfDot11RRMCfgPwrState_Type())
hpnicfDot11RRMCfgPwrState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgPwrState.setStatus(_A)
class _HpnicfDot11RRMCfgPwrMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_HpnicfDot11RRMCfgPwrMode_Type.__name__=_B
_HpnicfDot11RRMCfgPwrMode_Object=MibTableColumn
hpnicfDot11RRMCfgPwrMode=_HpnicfDot11RRMCfgPwrMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,6),_HpnicfDot11RRMCfgPwrMode_Type())
hpnicfDot11RRMCfgPwrMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgPwrMode.setStatus(_A)
class _HpnicfDot11RRMPwrProntoRadioElmt_Type(Unsigned32):defaultValue=0
_HpnicfDot11RRMPwrProntoRadioElmt_Type.__name__=_J
_HpnicfDot11RRMPwrProntoRadioElmt_Object=MibTableColumn
hpnicfDot11RRMPwrProntoRadioElmt=_HpnicfDot11RRMPwrProntoRadioElmt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,7),_HpnicfDot11RRMPwrProntoRadioElmt_Type())
hpnicfDot11RRMPwrProntoRadioElmt.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMPwrProntoRadioElmt.setStatus(_A)
class _HpnicfDot11RRMCfgIntrvl_Type(Integer32):defaultValue=8
_HpnicfDot11RRMCfgIntrvl_Type.__name__=_B
_HpnicfDot11RRMCfgIntrvl_Object=MibTableColumn
hpnicfDot11RRMCfgIntrvl=_HpnicfDot11RRMCfgIntrvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,8),_HpnicfDot11RRMCfgIntrvl_Type())
hpnicfDot11RRMCfgIntrvl.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgIntrvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgIntrvl.setUnits(_P)
class _HpnicfDot11RRMCfgIntrfThres_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfDot11RRMCfgIntrfThres_Type.__name__=_B
_HpnicfDot11RRMCfgIntrfThres_Object=MibTableColumn
hpnicfDot11RRMCfgIntrfThres=_HpnicfDot11RRMCfgIntrfThres_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,9),_HpnicfDot11RRMCfgIntrfThres_Type())
hpnicfDot11RRMCfgIntrfThres.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgIntrfThres.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgIntrfThres.setUnits(_F)
class _HpnicfDot11RRMCfgNoiseThres_Type(Integer32):defaultValue=-70;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-127,127))
_HpnicfDot11RRMCfgNoiseThres_Type.__name__=_B
_HpnicfDot11RRMCfgNoiseThres_Object=MibTableColumn
hpnicfDot11RRMCfgNoiseThres=_HpnicfDot11RRMCfgNoiseThres_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,10),_HpnicfDot11RRMCfgNoiseThres_Type())
hpnicfDot11RRMCfgNoiseThres.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgNoiseThres.setStatus(_A)
class _HpnicfDot11RRMCfgPERThres_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfDot11RRMCfgPERThres_Type.__name__=_B
_HpnicfDot11RRMCfgPERThres_Object=MibTableColumn
hpnicfDot11RRMCfgPERThres=_HpnicfDot11RRMCfgPERThres_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,11),_HpnicfDot11RRMCfgPERThres_Type())
hpnicfDot11RRMCfgPERThres.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgPERThres.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgPERThres.setUnits(_F)
class _HpnicfDot11RRMCfgToleranceFctr_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,45))
_HpnicfDot11RRMCfgToleranceFctr_Type.__name__=_B
_HpnicfDot11RRMCfgToleranceFctr_Object=MibTableColumn
hpnicfDot11RRMCfgToleranceFctr=_HpnicfDot11RRMCfgToleranceFctr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,12),_HpnicfDot11RRMCfgToleranceFctr_Type())
hpnicfDot11RRMCfgToleranceFctr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgToleranceFctr.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgToleranceFctr.setUnits(_F)
class _HpnicfDot11RRMCfgAdjacencyFctr_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfDot11RRMCfgAdjacencyFctr_Type.__name__=_B
_HpnicfDot11RRMCfgAdjacencyFctr_Object=MibTableColumn
hpnicfDot11RRMCfgAdjacencyFctr=_HpnicfDot11RRMCfgAdjacencyFctr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,2,1,13),_HpnicfDot11RRMCfgAdjacencyFctr_Type())
hpnicfDot11RRMCfgAdjacencyFctr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCfgAdjacencyFctr.setStatus(_A)
_HpnicfDot11RRMAPCfgTable_Object=MibTable
hpnicfDot11RRMAPCfgTable=_HpnicfDot11RRMAPCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,3))
if mibBuilder.loadTexts:hpnicfDot11RRMAPCfgTable.setStatus(_A)
_HpnicfDot11RRMAPCfgEntry_Object=MibTableRow
hpnicfDot11RRMAPCfgEntry=_HpnicfDot11RRMAPCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,3,1))
hpnicfDot11RRMAPCfgEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:hpnicfDot11RRMAPCfgEntry.setStatus(_A)
class _HpnicfDot11RRMAPWorkMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('monitor',2),('hybrid',3)))
_HpnicfDot11RRMAPWorkMode_Type.__name__=_B
_HpnicfDot11RRMAPWorkMode_Object=MibTableColumn
hpnicfDot11RRMAPWorkMode=_HpnicfDot11RRMAPWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,3,1,1),_HpnicfDot11RRMAPWorkMode_Type())
hpnicfDot11RRMAPWorkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMAPWorkMode.setStatus(_A)
_HpnicfDot11RRMSDRadioGroupTable_Object=MibTable
hpnicfDot11RRMSDRadioGroupTable=_HpnicfDot11RRMSDRadioGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4))
if mibBuilder.loadTexts:hpnicfDot11RRMSDRadioGroupTable.setStatus(_A)
_HpnicfDot11RRMSDRadioGroupEntry_Object=MibTableRow
hpnicfDot11RRMSDRadioGroupEntry=_HpnicfDot11RRMSDRadioGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4,1))
hpnicfDot11RRMSDRadioGroupEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:hpnicfDot11RRMSDRadioGroupEntry.setStatus(_A)
_HpnicfDot11RRMSDRadioGroupId_Type=Unsigned32
_HpnicfDot11RRMSDRadioGroupId_Object=MibTableColumn
hpnicfDot11RRMSDRadioGroupId=_HpnicfDot11RRMSDRadioGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4,1,1),_HpnicfDot11RRMSDRadioGroupId_Type())
hpnicfDot11RRMSDRadioGroupId.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRadioGroupId.setStatus(_A)
_HpnicfDot11RRMSDRadioGroupDesc_Type=OctetString
_HpnicfDot11RRMSDRadioGroupDesc_Object=MibTableColumn
hpnicfDot11RRMSDRadioGroupDesc=_HpnicfDot11RRMSDRadioGroupDesc_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4,1,2),_HpnicfDot11RRMSDRadioGroupDesc_Type())
hpnicfDot11RRMSDRadioGroupDesc.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRadioGroupDesc.setStatus(_A)
_HpnicfDot11RRMSDRdGrpChlHolddownTm_Type=Unsigned32
_HpnicfDot11RRMSDRdGrpChlHolddownTm_Object=MibTableColumn
hpnicfDot11RRMSDRdGrpChlHolddownTm=_HpnicfDot11RRMSDRdGrpChlHolddownTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4,1,3),_HpnicfDot11RRMSDRdGrpChlHolddownTm_Type())
hpnicfDot11RRMSDRdGrpChlHolddownTm.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRdGrpChlHolddownTm.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRdGrpChlHolddownTm.setUnits(_P)
_HpnicfDot11RRMSDRdGrpPwrHolddownTm_Type=Unsigned32
_HpnicfDot11RRMSDRdGrpPwrHolddownTm_Object=MibTableColumn
hpnicfDot11RRMSDRdGrpPwrHolddownTm=_HpnicfDot11RRMSDRdGrpPwrHolddownTm_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4,1,4),_HpnicfDot11RRMSDRdGrpPwrHolddownTm_Type())
hpnicfDot11RRMSDRdGrpPwrHolddownTm.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRdGrpPwrHolddownTm.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRdGrpPwrHolddownTm.setUnits(_P)
_HpnicfDot11RRMSDRdGroupRowStatus_Type=RowStatus
_HpnicfDot11RRMSDRdGroupRowStatus_Object=MibTableColumn
hpnicfDot11RRMSDRdGroupRowStatus=_HpnicfDot11RRMSDRdGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,4,1,5),_HpnicfDot11RRMSDRdGroupRowStatus_Type())
hpnicfDot11RRMSDRdGroupRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hpnicfDot11RRMSDRdGroupRowStatus.setStatus(_A)
_HpnicfDot11RRMAPCfg2Table_Object=MibTable
hpnicfDot11RRMAPCfg2Table=_HpnicfDot11RRMAPCfg2Table_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5))
if mibBuilder.loadTexts:hpnicfDot11RRMAPCfg2Table.setStatus(_A)
_HpnicfDot11RRMAPCfg2Entry_Object=MibTableRow
hpnicfDot11RRMAPCfg2Entry=_HpnicfDot11RRMAPCfg2Entry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5,1))
hpnicfDot11RRMAPCfg2Entry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:hpnicfDot11RRMAPCfg2Entry.setStatus(_A)
_HpnicfDot11RRMAPSerialID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11RRMAPSerialID_Object=MibTableColumn
hpnicfDot11RRMAPSerialID=_HpnicfDot11RRMAPSerialID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5,1,1),_HpnicfDot11RRMAPSerialID_Type())
hpnicfDot11RRMAPSerialID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMAPSerialID.setStatus(_A)
_HpnicfDot11RRMAPIntfThreshold_Type=Integer32
_HpnicfDot11RRMAPIntfThreshold_Object=MibTableColumn
hpnicfDot11RRMAPIntfThreshold=_HpnicfDot11RRMAPIntfThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5,1,2),_HpnicfDot11RRMAPIntfThreshold_Type())
hpnicfDot11RRMAPIntfThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMAPIntfThreshold.setStatus(_A)
_HpnicfDot11RRMStaIntfThreshold_Type=Integer32
_HpnicfDot11RRMStaIntfThreshold_Object=MibTableColumn
hpnicfDot11RRMStaIntfThreshold=_HpnicfDot11RRMStaIntfThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5,1,3),_HpnicfDot11RRMStaIntfThreshold_Type())
hpnicfDot11RRMStaIntfThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMStaIntfThreshold.setStatus(_A)
_HpnicfDot11RRMCoChlIntfTrapThhd_Type=Integer32
_HpnicfDot11RRMCoChlIntfTrapThhd_Object=MibTableColumn
hpnicfDot11RRMCoChlIntfTrapThhd=_HpnicfDot11RRMCoChlIntfTrapThhd_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5,1,4),_HpnicfDot11RRMCoChlIntfTrapThhd_Type())
hpnicfDot11RRMCoChlIntfTrapThhd.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMCoChlIntfTrapThhd.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMCoChlIntfTrapThhd.setUnits(_Q)
_HpnicfDot11RRMAdjChlIntfTrapThhd_Type=Integer32
_HpnicfDot11RRMAdjChlIntfTrapThhd_Object=MibTableColumn
hpnicfDot11RRMAdjChlIntfTrapThhd=_HpnicfDot11RRMAdjChlIntfTrapThhd_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,1,5,1,5),_HpnicfDot11RRMAdjChlIntfTrapThhd_Type())
hpnicfDot11RRMAdjChlIntfTrapThhd.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMAdjChlIntfTrapThhd.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMAdjChlIntfTrapThhd.setUnits(_Q)
_HpnicfDot11RRMDetectGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMDetectGroup=_HpnicfDot11RRMDetectGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2))
_HpnicfDot11RRMChlRptTable_Object=MibTable
hpnicfDot11RRMChlRptTable=_HpnicfDot11RRMChlRptTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1))
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptTable.setStatus(_A)
_HpnicfDot11RRMChlRptEntry_Object=MibTableRow
hpnicfDot11RRMChlRptEntry=_HpnicfDot11RRMChlRptEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1))
hpnicfDot11RRMChlRptEntry.setIndexNames((0,_E,_I),(0,_E,_W))
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptEntry.setStatus(_A)
_HpnicfDot11RRMRadioIndex_Type=HpnicfDot11RadioElementIndex
_HpnicfDot11RRMRadioIndex_Object=MibTableColumn
hpnicfDot11RRMRadioIndex=_HpnicfDot11RRMRadioIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,1),_HpnicfDot11RRMRadioIndex_Type())
hpnicfDot11RRMRadioIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfDot11RRMRadioIndex.setStatus(_A)
_HpnicfDot11RRMChlRptChlNum_Type=Integer32
_HpnicfDot11RRMChlRptChlNum_Object=MibTableColumn
hpnicfDot11RRMChlRptChlNum=_HpnicfDot11RRMChlRptChlNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,2),_HpnicfDot11RRMChlRptChlNum_Type())
hpnicfDot11RRMChlRptChlNum.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptChlNum.setStatus(_A)
class _HpnicfDot11RRMChlRptChlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primeChannel',1),('offChannel',2)))
_HpnicfDot11RRMChlRptChlType_Type.__name__=_B
_HpnicfDot11RRMChlRptChlType_Object=MibTableColumn
hpnicfDot11RRMChlRptChlType=_HpnicfDot11RRMChlRptChlType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,3),_HpnicfDot11RRMChlRptChlType_Type())
hpnicfDot11RRMChlRptChlType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptChlType.setStatus(_A)
class _HpnicfDot11RRMChlRptChlQlty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('bad',2)))
_HpnicfDot11RRMChlRptChlQlty_Type.__name__=_B
_HpnicfDot11RRMChlRptChlQlty_Object=MibTableColumn
hpnicfDot11RRMChlRptChlQlty=_HpnicfDot11RRMChlRptChlQlty_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,4),_HpnicfDot11RRMChlRptChlQlty_Type())
hpnicfDot11RRMChlRptChlQlty.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptChlQlty.setStatus(_A)
_HpnicfDot11RRMChlRptNbrCnt_Type=Integer32
_HpnicfDot11RRMChlRptNbrCnt_Object=MibTableColumn
hpnicfDot11RRMChlRptNbrCnt=_HpnicfDot11RRMChlRptNbrCnt_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,5),_HpnicfDot11RRMChlRptNbrCnt_Type())
hpnicfDot11RRMChlRptNbrCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptNbrCnt.setStatus(_A)
class _HpnicfDot11RRMChlRptLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMChlRptLoad_Type.__name__=_B
_HpnicfDot11RRMChlRptLoad_Object=MibTableColumn
hpnicfDot11RRMChlRptLoad=_HpnicfDot11RRMChlRptLoad_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,6),_HpnicfDot11RRMChlRptLoad_Type())
hpnicfDot11RRMChlRptLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptLoad.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptLoad.setUnits(_F)
class _HpnicfDot11RRMChlRptUtlz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMChlRptUtlz_Type.__name__=_B
_HpnicfDot11RRMChlRptUtlz_Object=MibTableColumn
hpnicfDot11RRMChlRptUtlz=_HpnicfDot11RRMChlRptUtlz_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,7),_HpnicfDot11RRMChlRptUtlz_Type())
hpnicfDot11RRMChlRptUtlz.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptUtlz.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptUtlz.setUnits(_F)
class _HpnicfDot11RRMChlRptIntrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMChlRptIntrf_Type.__name__=_B
_HpnicfDot11RRMChlRptIntrf_Object=MibTableColumn
hpnicfDot11RRMChlRptIntrf=_HpnicfDot11RRMChlRptIntrf_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,8),_HpnicfDot11RRMChlRptIntrf_Type())
hpnicfDot11RRMChlRptIntrf.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptIntrf.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptIntrf.setUnits(_F)
class _HpnicfDot11RRMChlRptPER_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMChlRptPER_Type.__name__=_B
_HpnicfDot11RRMChlRptPER_Object=MibTableColumn
hpnicfDot11RRMChlRptPER=_HpnicfDot11RRMChlRptPER_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,9),_HpnicfDot11RRMChlRptPER_Type())
hpnicfDot11RRMChlRptPER.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptPER.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptPER.setUnits(_F)
class _HpnicfDot11RRMChlRptRetryRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMChlRptRetryRate_Type.__name__=_B
_HpnicfDot11RRMChlRptRetryRate_Object=MibTableColumn
hpnicfDot11RRMChlRptRetryRate=_HpnicfDot11RRMChlRptRetryRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,10),_HpnicfDot11RRMChlRptRetryRate_Type())
hpnicfDot11RRMChlRptRetryRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptRetryRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptRetryRate.setUnits(_F)
_HpnicfDot11RRMChlRptNoise_Type=Integer32
_HpnicfDot11RRMChlRptNoise_Object=MibTableColumn
hpnicfDot11RRMChlRptNoise=_HpnicfDot11RRMChlRptNoise_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,11),_HpnicfDot11RRMChlRptNoise_Type())
hpnicfDot11RRMChlRptNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptNoise.setStatus(_A)
class _HpnicfDot11RRMChlRptRadarIndtcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detected',1),('notDetected',2)))
_HpnicfDot11RRMChlRptRadarIndtcr_Type.__name__=_B
_HpnicfDot11RRMChlRptRadarIndtcr_Object=MibTableColumn
hpnicfDot11RRMChlRptRadarIndtcr=_HpnicfDot11RRMChlRptRadarIndtcr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,1,1,12),_HpnicfDot11RRMChlRptRadarIndtcr_Type())
hpnicfDot11RRMChlRptRadarIndtcr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11RRMChlRptRadarIndtcr.setStatus(_A)
_HpnicfDot11RRMNbrInfoTable_Object=MibTable
hpnicfDot11RRMNbrInfoTable=_HpnicfDot11RRMNbrInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2))
if mibBuilder.loadTexts:hpnicfDot11RRMNbrInfoTable.setStatus(_A)
_HpnicfDot11RRMNbrInfoEntry_Object=MibTableRow
hpnicfDot11RRMNbrInfoEntry=_HpnicfDot11RRMNbrInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1))
hpnicfDot11RRMNbrInfoEntry.setIndexNames((0,_E,_I),(0,_E,_X))
if mibBuilder.loadTexts:hpnicfDot11RRMNbrInfoEntry.setStatus(_A)
_HpnicfDot11RrmNbrBSSID_Type=MacAddress
_HpnicfDot11RrmNbrBSSID_Object=MibTableColumn
hpnicfDot11RrmNbrBSSID=_HpnicfDot11RrmNbrBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1,1),_HpnicfDot11RrmNbrBSSID_Type())
hpnicfDot11RrmNbrBSSID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RrmNbrBSSID.setStatus(_A)
_HpnicfDot11RrmNbrChl_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11RrmNbrChl_Object=MibTableColumn
hpnicfDot11RrmNbrChl=_HpnicfDot11RrmNbrChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1,2),_HpnicfDot11RrmNbrChl_Type())
hpnicfDot11RrmNbrChl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RrmNbrChl.setStatus(_A)
class _HpnicfDot11RRMNbrIntrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMNbrIntrf_Type.__name__=_B
_HpnicfDot11RRMNbrIntrf_Object=MibTableColumn
hpnicfDot11RRMNbrIntrf=_HpnicfDot11RRMNbrIntrf_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1,3),_HpnicfDot11RRMNbrIntrf_Type())
hpnicfDot11RRMNbrIntrf.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMNbrIntrf.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMNbrIntrf.setUnits(_F)
_HpnicfDot11RrmNbrRSSI_Type=Integer32
_HpnicfDot11RrmNbrRSSI_Object=MibTableColumn
hpnicfDot11RrmNbrRSSI=_HpnicfDot11RrmNbrRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1,4),_HpnicfDot11RrmNbrRSSI_Type())
hpnicfDot11RrmNbrRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RrmNbrRSSI.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RrmNbrRSSI.setUnits(_O)
class _HpnicfDot11RrmNbrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('managed',1),('unmanaged',2)))
_HpnicfDot11RrmNbrType_Type.__name__=_B
_HpnicfDot11RrmNbrType_Object=MibTableColumn
hpnicfDot11RrmNbrType=_HpnicfDot11RrmNbrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1,5),_HpnicfDot11RrmNbrType_Type())
hpnicfDot11RrmNbrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RrmNbrType.setStatus(_A)
_HpnicfDot11RrmNbrSSID_Type=HpnicfDot11SSIDStringType
_HpnicfDot11RrmNbrSSID_Object=MibTableColumn
hpnicfDot11RrmNbrSSID=_HpnicfDot11RrmNbrSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,2,1,6),_HpnicfDot11RrmNbrSSID_Type())
hpnicfDot11RrmNbrSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RrmNbrSSID.setStatus(_A)
_HpnicfDot11RRMHistoryTable_Object=MibTable
hpnicfDot11RRMHistoryTable=_HpnicfDot11RRMHistoryTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3))
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryTable.setStatus(_A)
_HpnicfDot11RRMHistoryEntry_Object=MibTableRow
hpnicfDot11RRMHistoryEntry=_HpnicfDot11RRMHistoryEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1))
hpnicfDot11RRMHistoryEntry.setIndexNames((0,_E,_I),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryEntry.setStatus(_A)
_HpnicfDot11RRMHistoryId_Type=Integer32
_HpnicfDot11RRMHistoryId_Object=MibTableColumn
hpnicfDot11RRMHistoryId=_HpnicfDot11RRMHistoryId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,1),_HpnicfDot11RRMHistoryId_Type())
hpnicfDot11RRMHistoryId.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryId.setStatus(_A)
class _HpnicfDot11RRMHistoryRecIndctr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('before',1),('after',2)))
_HpnicfDot11RRMHistoryRecIndctr_Type.__name__=_B
_HpnicfDot11RRMHistoryRecIndctr_Object=MibTableColumn
hpnicfDot11RRMHistoryRecIndctr=_HpnicfDot11RRMHistoryRecIndctr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,2),_HpnicfDot11RRMHistoryRecIndctr_Type())
hpnicfDot11RRMHistoryRecIndctr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryRecIndctr.setStatus(_A)
_HpnicfDot11RRMHistoryChl_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11RRMHistoryChl_Object=MibTableColumn
hpnicfDot11RRMHistoryChl=_HpnicfDot11RRMHistoryChl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,3),_HpnicfDot11RRMHistoryChl_Type())
hpnicfDot11RRMHistoryChl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryChl.setStatus(_A)
_HpnicfDot11RRMHistoryPwr_Type=Integer32
_HpnicfDot11RRMHistoryPwr_Object=MibTableColumn
hpnicfDot11RRMHistoryPwr=_HpnicfDot11RRMHistoryPwr_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,4),_HpnicfDot11RRMHistoryPwr_Type())
hpnicfDot11RRMHistoryPwr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryPwr.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryPwr.setUnits(_O)
class _HpnicfDot11RRMHistoryLoad_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMHistoryLoad_Type.__name__=_B
_HpnicfDot11RRMHistoryLoad_Object=MibTableColumn
hpnicfDot11RRMHistoryLoad=_HpnicfDot11RRMHistoryLoad_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,5),_HpnicfDot11RRMHistoryLoad_Type())
hpnicfDot11RRMHistoryLoad.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryLoad.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryLoad.setUnits(_F)
class _HpnicfDot11RRMHistoryUtlz_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMHistoryUtlz_Type.__name__=_B
_HpnicfDot11RRMHistoryUtlz_Object=MibTableColumn
hpnicfDot11RRMHistoryUtlz=_HpnicfDot11RRMHistoryUtlz_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,6),_HpnicfDot11RRMHistoryUtlz_Type())
hpnicfDot11RRMHistoryUtlz.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryUtlz.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryUtlz.setUnits(_F)
class _HpnicfDot11RRMHistoryIntrf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMHistoryIntrf_Type.__name__=_B
_HpnicfDot11RRMHistoryIntrf_Object=MibTableColumn
hpnicfDot11RRMHistoryIntrf=_HpnicfDot11RRMHistoryIntrf_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,7),_HpnicfDot11RRMHistoryIntrf_Type())
hpnicfDot11RRMHistoryIntrf.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryIntrf.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryIntrf.setUnits(_F)
_HpnicfDot11RRMHistoryNoise_Type=Integer32
_HpnicfDot11RRMHistoryNoise_Object=MibTableColumn
hpnicfDot11RRMHistoryNoise=_HpnicfDot11RRMHistoryNoise_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,8),_HpnicfDot11RRMHistoryNoise_Type())
hpnicfDot11RRMHistoryNoise.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryNoise.setStatus(_A)
class _HpnicfDot11RRMHistoryPER_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMHistoryPER_Type.__name__=_B
_HpnicfDot11RRMHistoryPER_Object=MibTableColumn
hpnicfDot11RRMHistoryPER=_HpnicfDot11RRMHistoryPER_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,9),_HpnicfDot11RRMHistoryPER_Type())
hpnicfDot11RRMHistoryPER.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryPER.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryPER.setUnits(_F)
class _HpnicfDot11RRMHistoryRetryRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDot11RRMHistoryRetryRate_Type.__name__=_B
_HpnicfDot11RRMHistoryRetryRate_Object=MibTableColumn
hpnicfDot11RRMHistoryRetryRate=_HpnicfDot11RRMHistoryRetryRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,10),_HpnicfDot11RRMHistoryRetryRate_Type())
hpnicfDot11RRMHistoryRetryRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryRetryRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryRetryRate.setUnits(_F)
class _HpnicfDot11RRMHistoryChgReason_Type(Bits):namedValues=NamedValues(*(('others',0),('coverage',1),('radar',2),('retransmission',3),('packetsDiscarded',4),('interference',5)))
_HpnicfDot11RRMHistoryChgReason_Type.__name__='Bits'
_HpnicfDot11RRMHistoryChgReason_Object=MibTableColumn
hpnicfDot11RRMHistoryChgReason=_HpnicfDot11RRMHistoryChgReason_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,11),_HpnicfDot11RRMHistoryChgReason_Type())
hpnicfDot11RRMHistoryChgReason.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryChgReason.setStatus(_A)
_HpnicfDot11RRMHistoryChgDateTime_Type=DateAndTime
_HpnicfDot11RRMHistoryChgDateTime_Object=MibTableColumn
hpnicfDot11RRMHistoryChgDateTime=_HpnicfDot11RRMHistoryChgDateTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,3,1,12),_HpnicfDot11RRMHistoryChgDateTime_Type())
hpnicfDot11RRMHistoryChgDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMHistoryChgDateTime.setStatus(_A)
_HpnicfDot11RRMRadioNbrInfoTable_Object=MibTable
hpnicfDot11RRMRadioNbrInfoTable=_HpnicfDot11RRMRadioNbrInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,4))
if mibBuilder.loadTexts:hpnicfDot11RRMRadioNbrInfoTable.setStatus(_A)
_HpnicfDot11RRMRadioNbrInfoEntry_Object=MibTableRow
hpnicfDot11RRMRadioNbrInfoEntry=_HpnicfDot11RRMRadioNbrInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,4,1))
hpnicfDot11RRMRadioNbrInfoEntry.setIndexNames((0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:hpnicfDot11RRMRadioNbrInfoEntry.setStatus(_A)
_HpnicfDot11RRMRadioNbrAPID_Type=HpnicfDot11ObjectIDType
_HpnicfDot11RRMRadioNbrAPID_Object=MibTableColumn
hpnicfDot11RRMRadioNbrAPID=_HpnicfDot11RRMRadioNbrAPID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,4,1,1),_HpnicfDot11RRMRadioNbrAPID_Type())
hpnicfDot11RRMRadioNbrAPID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMRadioNbrAPID.setStatus(_A)
_HpnicfDot11RRMRadioNbrRadioID_Type=HpnicfDot11RadioScopeType
_HpnicfDot11RRMRadioNbrRadioID_Object=MibTableColumn
hpnicfDot11RRMRadioNbrRadioID=_HpnicfDot11RRMRadioNbrRadioID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,4,1,2),_HpnicfDot11RRMRadioNbrRadioID_Type())
hpnicfDot11RRMRadioNbrRadioID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11RRMRadioNbrRadioID.setStatus(_A)
_HpnicfDot11RRMRadioNbrSSID_Type=OctetString
_HpnicfDot11RRMRadioNbrSSID_Object=MibTableColumn
hpnicfDot11RRMRadioNbrSSID=_HpnicfDot11RRMRadioNbrSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,2,4,1,3),_HpnicfDot11RRMRadioNbrSSID_Type())
hpnicfDot11RRMRadioNbrSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11RRMRadioNbrSSID.setStatus(_A)
_HpnicfDot11RRMNotifyGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMNotifyGroup=_HpnicfDot11RRMNotifyGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3))
_HpnicfDot11RRMChlQltyNotifications_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMChlQltyNotifications=_HpnicfDot11RRMChlQltyNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,1))
_HpnicfDot11RRMChlQltyNtfPrefix_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMChlQltyNtfPrefix=_HpnicfDot11RRMChlQltyNtfPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,1,0))
_HpnicfDot11RRMResChgNotifications_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMResChgNotifications=_HpnicfDot11RRMResChgNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,2))
_HpnicfDot11RRMResChgNtfPrefix_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMResChgNtfPrefix=_HpnicfDot11RRMResChgNtfPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,2,0))
_HpnicfDot11RRMNotificationsVar_ObjectIdentity=ObjectIdentity
hpnicfDot11RRMNotificationsVar=_HpnicfDot11RRMNotificationsVar_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,3))
_HpnicfDot11NewPower_Type=Integer32
_HpnicfDot11NewPower_Object=MibScalar
hpnicfDot11NewPower=_HpnicfDot11NewPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,3,1),_HpnicfDot11NewPower_Type())
hpnicfDot11NewPower.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfDot11NewPower.setStatus(_A)
_HpnicfDot11OldPower_Type=Integer32
_HpnicfDot11OldPower_Object=MibScalar
hpnicfDot11OldPower=_HpnicfDot11OldPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,3,2),_HpnicfDot11OldPower_Type())
hpnicfDot11OldPower.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfDot11OldPower.setStatus(_A)
_HpnicfDot11MonitorDetectedGroup_ObjectIdentity=ObjectIdentity
hpnicfDot11MonitorDetectedGroup=_HpnicfDot11MonitorDetectedGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4))
_HpnicfDot11MonitorDetectedDevTable_Object=MibTable
hpnicfDot11MonitorDetectedDevTable=_HpnicfDot11MonitorDetectedDevTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1))
if mibBuilder.loadTexts:hpnicfDot11MonitorDetectedDevTable.setStatus(_A)
_HpnicfDot11MonitorDetectedDevEntry_Object=MibTableRow
hpnicfDot11MonitorDetectedDevEntry=_HpnicfDot11MonitorDetectedDevEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1))
hpnicfDot11MonitorDetectedDevEntry.setIndexNames((0,_E,_c),(0,_M,_N))
if mibBuilder.loadTexts:hpnicfDot11MonitorDetectedDevEntry.setStatus(_A)
_HpnicfDot11MonitorDevMAC_Type=MacAddress
_HpnicfDot11MonitorDevMAC_Object=MibTableColumn
hpnicfDot11MonitorDevMAC=_HpnicfDot11MonitorDevMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,1),_HpnicfDot11MonitorDevMAC_Type())
hpnicfDot11MonitorDevMAC.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevMAC.setStatus(_A)
class _HpnicfDot11MonitorDevType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('client',1),('ap',2),('adhoc',3),('wirelessBridge',4),('unknown',5)))
_HpnicfDot11MonitorDevType_Type.__name__=_B
_HpnicfDot11MonitorDevType_Object=MibTableColumn
hpnicfDot11MonitorDevType=_HpnicfDot11MonitorDevType_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,2),_HpnicfDot11MonitorDevType_Type())
hpnicfDot11MonitorDevType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevType.setStatus(_A)
_HpnicfDot11MonitorDevVendor_Type=OctetString
_HpnicfDot11MonitorDevVendor_Object=MibTableColumn
hpnicfDot11MonitorDevVendor=_HpnicfDot11MonitorDevVendor_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,3),_HpnicfDot11MonitorDevVendor_Type())
hpnicfDot11MonitorDevVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevVendor.setStatus(_A)
_HpnicfDot11MonitorDevSSID_Type=OctetString
_HpnicfDot11MonitorDevSSID_Object=MibTableColumn
hpnicfDot11MonitorDevSSID=_HpnicfDot11MonitorDevSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,4),_HpnicfDot11MonitorDevSSID_Type())
hpnicfDot11MonitorDevSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevSSID.setStatus(_A)
_HpnicfDot11MonitorDevBSSID_Type=MacAddress
_HpnicfDot11MonitorDevBSSID_Object=MibTableColumn
hpnicfDot11MonitorDevBSSID=_HpnicfDot11MonitorDevBSSID_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,5),_HpnicfDot11MonitorDevBSSID_Type())
hpnicfDot11MonitorDevBSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevBSSID.setStatus(_A)
_HpnicfDot11MonitorDevChannel_Type=HpnicfDot11ChannelScopeType
_HpnicfDot11MonitorDevChannel_Object=MibTableColumn
hpnicfDot11MonitorDevChannel=_HpnicfDot11MonitorDevChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,6),_HpnicfDot11MonitorDevChannel_Type())
hpnicfDot11MonitorDevChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevChannel.setStatus(_A)
_HpnicfDot11MonitorRadioId_Type=HpnicfDot11RadioScopeType
_HpnicfDot11MonitorRadioId_Object=MibTableColumn
hpnicfDot11MonitorRadioId=_HpnicfDot11MonitorRadioId_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,7),_HpnicfDot11MonitorRadioId_Type())
hpnicfDot11MonitorRadioId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorRadioId.setStatus(_A)
_HpnicfDot11MonitorDevMaxRSSI_Type=Integer32
_HpnicfDot11MonitorDevMaxRSSI_Object=MibTableColumn
hpnicfDot11MonitorDevMaxRSSI=_HpnicfDot11MonitorDevMaxRSSI_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,8),_HpnicfDot11MonitorDevMaxRSSI_Type())
hpnicfDot11MonitorDevMaxRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevMaxRSSI.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevMaxRSSI.setUnits(_Q)
_HpnicfDot11MonitorDevBeaconIntvl_Type=Integer32
_HpnicfDot11MonitorDevBeaconIntvl_Object=MibTableColumn
hpnicfDot11MonitorDevBeaconIntvl=_HpnicfDot11MonitorDevBeaconIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,9),_HpnicfDot11MonitorDevBeaconIntvl_Type())
hpnicfDot11MonitorDevBeaconIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevBeaconIntvl.setStatus(_A)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevBeaconIntvl.setUnits('millisecond')
_HpnicfDot11MonitorDevFstDctTime_Type=DateAndTime
_HpnicfDot11MonitorDevFstDctTime_Object=MibTableColumn
hpnicfDot11MonitorDevFstDctTime=_HpnicfDot11MonitorDevFstDctTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,10),_HpnicfDot11MonitorDevFstDctTime_Type())
hpnicfDot11MonitorDevFstDctTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevFstDctTime.setStatus(_A)
_HpnicfDot11MonitorDevLstDctTime_Type=DateAndTime
_HpnicfDot11MonitorDevLstDctTime_Object=MibTableColumn
hpnicfDot11MonitorDevLstDctTime=_HpnicfDot11MonitorDevLstDctTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,11),_HpnicfDot11MonitorDevLstDctTime_Type())
hpnicfDot11MonitorDevLstDctTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevLstDctTime.setStatus(_A)
_HpnicfDot11MonitorDevClear_Type=TruthValue
_HpnicfDot11MonitorDevClear_Object=MibTableColumn
hpnicfDot11MonitorDevClear=_HpnicfDot11MonitorDevClear_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,12),_HpnicfDot11MonitorDevClear_Type())
hpnicfDot11MonitorDevClear.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevClear.setStatus(_A)
_HpnicfDot11MonitorDevSNR_Type=Integer32
_HpnicfDot11MonitorDevSNR_Object=MibTableColumn
hpnicfDot11MonitorDevSNR=_HpnicfDot11MonitorDevSNR_Object((1,3,6,1,4,1,11,2,14,11,15,2,75,8,4,1,1,13),_HpnicfDot11MonitorDevSNR_Type())
hpnicfDot11MonitorDevSNR.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDot11MonitorDevSNR.setStatus(_A)
hpnicfDot11RRMIntrfLimit=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,1,0,1))
hpnicfDot11RRMIntrfLimit.setObjects((_E,_d))
if mibBuilder.loadTexts:hpnicfDot11RRMIntrfLimit.setStatus(_A)
hpnicfDot11RRMPERLimit=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,1,0,2))
hpnicfDot11RRMPERLimit.setObjects((_E,_e))
if mibBuilder.loadTexts:hpnicfDot11RRMPERLimit.setStatus(_A)
hpnicfDot11RRMNoiseLimit=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,1,0,3))
hpnicfDot11RRMNoiseLimit.setObjects((_E,_f))
if mibBuilder.loadTexts:hpnicfDot11RRMNoiseLimit.setStatus(_A)
hpnicfDot11RRMPowerChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,75,8,3,2,0,1))
hpnicfDot11RRMPowerChange.setObjects(*((_E,_I),(_E,_g),(_E,_h)))
if mibBuilder.loadTexts:hpnicfDot11RRMPowerChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfDot11RRM':hpnicfDot11RRM,'hpnicfDot11RRMConfigGroup':hpnicfDot11RRMConfigGroup,'hpnicfDot11RRMGlobalCfgPara':hpnicfDot11RRMGlobalCfgPara,'hpnicfDot11RRM11nMadtMaxMcs':hpnicfDot11RRM11nMadtMaxMcs,'hpnicfDot11RRM11nSuptMaxMcs':hpnicfDot11RRM11nSuptMaxMcs,'hpnicfDot11RRM11gProtect':hpnicfDot11RRM11gProtect,'hpnicfDot11RRM11aPwrConstrt':hpnicfDot11RRM11aPwrConstrt,'hpnicfDot11RRM11aSpectrumManag':hpnicfDot11RRM11aSpectrumManag,'hpnicfDot11RRMAutoChlAvoid11h':hpnicfDot11RRMAutoChlAvoid11h,'hpnicfDot11RRMScanChl':hpnicfDot11RRMScanChl,'hpnicfDot11RRMScanRptIntvel':hpnicfDot11RRMScanRptIntvel,'hpnicfDot11APInterfNumThreshhd':hpnicfDot11APInterfNumThreshhd,'hpnicfDot11StaInterfNumThreshhd':hpnicfDot11StaInterfNumThreshhd,'hpnicfDot11RRM11nMultiCastMcs':hpnicfDot11RRM11nMultiCastMcs,'hpnicfDot11RRM11acMadtMaxNss':hpnicfDot11RRM11acMadtMaxNss,'hpnicfDot11RRM11acSuptMaxNss':hpnicfDot11RRM11acSuptMaxNss,'hpnicfDot11RRM11acMultiCastNss':hpnicfDot11RRM11acMultiCastNss,'hpnicfDot11RRM11acMultiCastVhtMcs':hpnicfDot11RRM11acMultiCastVhtMcs,'hpnicfDot11RRMRadioCfgTable':hpnicfDot11RRMRadioCfgTable,'hpnicfDot11RRMRadioCfgEntry':hpnicfDot11RRMRadioCfgEntry,_R:hpnicfDot11RRMRadioType,'hpnicfDot11RRMCfgChlState':hpnicfDot11RRMCfgChlState,'hpnicfDot11RRMCfgChlMode':hpnicfDot11RRMCfgChlMode,'hpnicfDot11RRMChlProntoRadioElmt':hpnicfDot11RRMChlProntoRadioElmt,'hpnicfDot11RRMCfgPwrState':hpnicfDot11RRMCfgPwrState,'hpnicfDot11RRMCfgPwrMode':hpnicfDot11RRMCfgPwrMode,'hpnicfDot11RRMPwrProntoRadioElmt':hpnicfDot11RRMPwrProntoRadioElmt,'hpnicfDot11RRMCfgIntrvl':hpnicfDot11RRMCfgIntrvl,'hpnicfDot11RRMCfgIntrfThres':hpnicfDot11RRMCfgIntrfThres,'hpnicfDot11RRMCfgNoiseThres':hpnicfDot11RRMCfgNoiseThres,'hpnicfDot11RRMCfgPERThres':hpnicfDot11RRMCfgPERThres,'hpnicfDot11RRMCfgToleranceFctr':hpnicfDot11RRMCfgToleranceFctr,'hpnicfDot11RRMCfgAdjacencyFctr':hpnicfDot11RRMCfgAdjacencyFctr,'hpnicfDot11RRMAPCfgTable':hpnicfDot11RRMAPCfgTable,'hpnicfDot11RRMAPCfgEntry':hpnicfDot11RRMAPCfgEntry,'hpnicfDot11RRMAPWorkMode':hpnicfDot11RRMAPWorkMode,'hpnicfDot11RRMSDRadioGroupTable':hpnicfDot11RRMSDRadioGroupTable,'hpnicfDot11RRMSDRadioGroupEntry':hpnicfDot11RRMSDRadioGroupEntry,_U:hpnicfDot11RRMSDRadioGroupId,'hpnicfDot11RRMSDRadioGroupDesc':hpnicfDot11RRMSDRadioGroupDesc,'hpnicfDot11RRMSDRdGrpChlHolddownTm':hpnicfDot11RRMSDRdGrpChlHolddownTm,'hpnicfDot11RRMSDRdGrpPwrHolddownTm':hpnicfDot11RRMSDRdGrpPwrHolddownTm,'hpnicfDot11RRMSDRdGroupRowStatus':hpnicfDot11RRMSDRdGroupRowStatus,'hpnicfDot11RRMAPCfg2Table':hpnicfDot11RRMAPCfg2Table,'hpnicfDot11RRMAPCfg2Entry':hpnicfDot11RRMAPCfg2Entry,_V:hpnicfDot11RRMAPSerialID,'hpnicfDot11RRMAPIntfThreshold':hpnicfDot11RRMAPIntfThreshold,'hpnicfDot11RRMStaIntfThreshold':hpnicfDot11RRMStaIntfThreshold,'hpnicfDot11RRMCoChlIntfTrapThhd':hpnicfDot11RRMCoChlIntfTrapThhd,'hpnicfDot11RRMAdjChlIntfTrapThhd':hpnicfDot11RRMAdjChlIntfTrapThhd,'hpnicfDot11RRMDetectGroup':hpnicfDot11RRMDetectGroup,'hpnicfDot11RRMChlRptTable':hpnicfDot11RRMChlRptTable,'hpnicfDot11RRMChlRptEntry':hpnicfDot11RRMChlRptEntry,_I:hpnicfDot11RRMRadioIndex,_W:hpnicfDot11RRMChlRptChlNum,'hpnicfDot11RRMChlRptChlType':hpnicfDot11RRMChlRptChlType,'hpnicfDot11RRMChlRptChlQlty':hpnicfDot11RRMChlRptChlQlty,'hpnicfDot11RRMChlRptNbrCnt':hpnicfDot11RRMChlRptNbrCnt,'hpnicfDot11RRMChlRptLoad':hpnicfDot11RRMChlRptLoad,'hpnicfDot11RRMChlRptUtlz':hpnicfDot11RRMChlRptUtlz,_d:hpnicfDot11RRMChlRptIntrf,_e:hpnicfDot11RRMChlRptPER,'hpnicfDot11RRMChlRptRetryRate':hpnicfDot11RRMChlRptRetryRate,_f:hpnicfDot11RRMChlRptNoise,'hpnicfDot11RRMChlRptRadarIndtcr':hpnicfDot11RRMChlRptRadarIndtcr,'hpnicfDot11RRMNbrInfoTable':hpnicfDot11RRMNbrInfoTable,'hpnicfDot11RRMNbrInfoEntry':hpnicfDot11RRMNbrInfoEntry,_X:hpnicfDot11RrmNbrBSSID,'hpnicfDot11RrmNbrChl':hpnicfDot11RrmNbrChl,'hpnicfDot11RRMNbrIntrf':hpnicfDot11RRMNbrIntrf,'hpnicfDot11RrmNbrRSSI':hpnicfDot11RrmNbrRSSI,'hpnicfDot11RrmNbrType':hpnicfDot11RrmNbrType,'hpnicfDot11RrmNbrSSID':hpnicfDot11RrmNbrSSID,'hpnicfDot11RRMHistoryTable':hpnicfDot11RRMHistoryTable,'hpnicfDot11RRMHistoryEntry':hpnicfDot11RRMHistoryEntry,_Y:hpnicfDot11RRMHistoryId,_Z:hpnicfDot11RRMHistoryRecIndctr,'hpnicfDot11RRMHistoryChl':hpnicfDot11RRMHistoryChl,'hpnicfDot11RRMHistoryPwr':hpnicfDot11RRMHistoryPwr,'hpnicfDot11RRMHistoryLoad':hpnicfDot11RRMHistoryLoad,'hpnicfDot11RRMHistoryUtlz':hpnicfDot11RRMHistoryUtlz,'hpnicfDot11RRMHistoryIntrf':hpnicfDot11RRMHistoryIntrf,'hpnicfDot11RRMHistoryNoise':hpnicfDot11RRMHistoryNoise,'hpnicfDot11RRMHistoryPER':hpnicfDot11RRMHistoryPER,'hpnicfDot11RRMHistoryRetryRate':hpnicfDot11RRMHistoryRetryRate,'hpnicfDot11RRMHistoryChgReason':hpnicfDot11RRMHistoryChgReason,'hpnicfDot11RRMHistoryChgDateTime':hpnicfDot11RRMHistoryChgDateTime,'hpnicfDot11RRMRadioNbrInfoTable':hpnicfDot11RRMRadioNbrInfoTable,'hpnicfDot11RRMRadioNbrInfoEntry':hpnicfDot11RRMRadioNbrInfoEntry,_a:hpnicfDot11RRMRadioNbrAPID,_b:hpnicfDot11RRMRadioNbrRadioID,'hpnicfDot11RRMRadioNbrSSID':hpnicfDot11RRMRadioNbrSSID,'hpnicfDot11RRMNotifyGroup':hpnicfDot11RRMNotifyGroup,'hpnicfDot11RRMChlQltyNotifications':hpnicfDot11RRMChlQltyNotifications,'hpnicfDot11RRMChlQltyNtfPrefix':hpnicfDot11RRMChlQltyNtfPrefix,'hpnicfDot11RRMIntrfLimit':hpnicfDot11RRMIntrfLimit,'hpnicfDot11RRMPERLimit':hpnicfDot11RRMPERLimit,'hpnicfDot11RRMNoiseLimit':hpnicfDot11RRMNoiseLimit,'hpnicfDot11RRMResChgNotifications':hpnicfDot11RRMResChgNotifications,'hpnicfDot11RRMResChgNtfPrefix':hpnicfDot11RRMResChgNtfPrefix,'hpnicfDot11RRMPowerChange':hpnicfDot11RRMPowerChange,'hpnicfDot11RRMNotificationsVar':hpnicfDot11RRMNotificationsVar,_g:hpnicfDot11NewPower,_h:hpnicfDot11OldPower,'hpnicfDot11MonitorDetectedGroup':hpnicfDot11MonitorDetectedGroup,'hpnicfDot11MonitorDetectedDevTable':hpnicfDot11MonitorDetectedDevTable,'hpnicfDot11MonitorDetectedDevEntry':hpnicfDot11MonitorDetectedDevEntry,_c:hpnicfDot11MonitorDevMAC,'hpnicfDot11MonitorDevType':hpnicfDot11MonitorDevType,'hpnicfDot11MonitorDevVendor':hpnicfDot11MonitorDevVendor,'hpnicfDot11MonitorDevSSID':hpnicfDot11MonitorDevSSID,'hpnicfDot11MonitorDevBSSID':hpnicfDot11MonitorDevBSSID,'hpnicfDot11MonitorDevChannel':hpnicfDot11MonitorDevChannel,'hpnicfDot11MonitorRadioId':hpnicfDot11MonitorRadioId,'hpnicfDot11MonitorDevMaxRSSI':hpnicfDot11MonitorDevMaxRSSI,'hpnicfDot11MonitorDevBeaconIntvl':hpnicfDot11MonitorDevBeaconIntvl,'hpnicfDot11MonitorDevFstDctTime':hpnicfDot11MonitorDevFstDctTime,'hpnicfDot11MonitorDevLstDctTime':hpnicfDot11MonitorDevLstDctTime,'hpnicfDot11MonitorDevClear':hpnicfDot11MonitorDevClear,'hpnicfDot11MonitorDevSNR':hpnicfDot11MonitorDevSNR})