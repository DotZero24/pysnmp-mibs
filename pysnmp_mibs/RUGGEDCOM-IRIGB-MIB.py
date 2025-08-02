_Z='rcIrigbStartTime2'
_Y='rcIrigbPulseWidth2'
_X='rcIrigbPulseInterval2'
_W='rcIrigbOutputPWM2'
_V='rcIrigbStartTime1'
_U='rcIrigbPulseWidth1'
_T='rcIrigbPulseInterval1'
_S='rcIrigbOutputPWM1'
_R='rcIrigbInput'
_Q='rcIrigbAMOutput'
_P='rcIrigbFreqAdj'
_O='rcIrigbOFM'
_N='rcIrigbCableComp'
_M='rcIrigbLockInt'
_L='rcIrigbExt'
_K='rcIrigbTimeCode'
_J='rcIrigbStatusChange'
_I='pps'
_H='pwm'
_G='read-only'
_F='rcIrigbStatus'
_E='off'
_D='read-write'
_C='Integer32'
_B='RUGGEDCOM-IRIGB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,ruggedcomTraps=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt','ruggedcomTraps')
RcTimeSyncStatus,=mibBuilder.importSymbols('RUGGEDCOM-TIMECONFIG-MIB','RcTimeSyncStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rcIrigb=ModuleIdentity((1,3,6,1,4,1,15004,4,10))
if mibBuilder.loadTexts:rcIrigb.setRevisions(('2015-10-30 17:00','2014-12-01 17:00'))
class RcTimeStamp(TextualConvention,OctetString):status=_A;displayHint='4d.4d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_RcIrigbBase_ObjectIdentity=ObjectIdentity
rcIrigbBase=_RcIrigbBase_ObjectIdentity((1,3,6,1,4,1,15004,4,10,1))
_RcIrigbStatus_Type=RcTimeSyncStatus
_RcIrigbStatus_Object=MibScalar
rcIrigbStatus=_RcIrigbStatus_Object((1,3,6,1,4,1,15004,4,10,1,1),_RcIrigbStatus_Type())
rcIrigbStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rcIrigbStatus.setStatus(_A)
class _RcIrigbAMOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_E,1),('am',4)))
_RcIrigbAMOutput_Type.__name__=_C
_RcIrigbAMOutput_Object=MibScalar
rcIrigbAMOutput=_RcIrigbAMOutput_Object((1,3,6,1,4,1,15004,4,10,1,2),_RcIrigbAMOutput_Type())
rcIrigbAMOutput.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbAMOutput.setStatus(_A)
class _RcIrigbTimeCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('bxx0',1),('bxx1',2),('bxx2',3),('bxx3',4),('bxx4',5),('bxx5',6),('bxx6',7),('bxx7',8)))
_RcIrigbTimeCode_Type.__name__=_C
_RcIrigbTimeCode_Object=MibScalar
rcIrigbTimeCode=_RcIrigbTimeCode_Object((1,3,6,1,4,1,15004,4,10,1,3),_RcIrigbTimeCode_Type())
rcIrigbTimeCode.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbTimeCode.setStatus(_A)
class _RcIrigbExt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),('ieee1344',2),('c37-118-2005',3),('c37-118-2011',4)))
_RcIrigbExt_Type.__name__=_C
_RcIrigbExt_Object=MibScalar
rcIrigbExt=_RcIrigbExt_Object((1,3,6,1,4,1,15004,4,10,1,4),_RcIrigbExt_Type())
rcIrigbExt.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbExt.setStatus(_A)
class _RcIrigbInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3),('am',4)))
_RcIrigbInput_Type.__name__=_C
_RcIrigbInput_Object=MibScalar
rcIrigbInput=_RcIrigbInput_Object((1,3,6,1,4,1,15004,4,10,1,5),_RcIrigbInput_Type())
rcIrigbInput.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbInput.setStatus(_A)
class _RcIrigbLockInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_RcIrigbLockInt_Type.__name__=_C
_RcIrigbLockInt_Object=MibScalar
rcIrigbLockInt=_RcIrigbLockInt_Object((1,3,6,1,4,1,15004,4,10,1,6),_RcIrigbLockInt_Type())
rcIrigbLockInt.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbLockInt.setStatus(_A)
class _RcIrigbCableComp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50000))
_RcIrigbCableComp_Type.__name__=_C
_RcIrigbCableComp_Object=MibScalar
rcIrigbCableComp=_RcIrigbCableComp_Object((1,3,6,1,4,1,15004,4,10,1,7),_RcIrigbCableComp_Type())
rcIrigbCableComp.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbCableComp.setStatus(_A)
class _RcIrigbOFM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_RcIrigbOFM_Type.__name__=_C
_RcIrigbOFM_Object=MibScalar
rcIrigbOFM=_RcIrigbOFM_Object((1,3,6,1,4,1,15004,4,10,1,8),_RcIrigbOFM_Type())
rcIrigbOFM.setMaxAccess(_G)
if mibBuilder.loadTexts:rcIrigbOFM.setStatus(_A)
class _RcIrigbFreqAdj_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_RcIrigbFreqAdj_Type.__name__=_C
_RcIrigbFreqAdj_Object=MibScalar
rcIrigbFreqAdj=_RcIrigbFreqAdj_Object((1,3,6,1,4,1,15004,4,10,1,9),_RcIrigbFreqAdj_Type())
rcIrigbFreqAdj.setMaxAccess(_G)
if mibBuilder.loadTexts:rcIrigbFreqAdj.setStatus(_A)
class _RcIrigbOutputPWM1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3),('ppx',5)))
_RcIrigbOutputPWM1_Type.__name__=_C
_RcIrigbOutputPWM1_Object=MibScalar
rcIrigbOutputPWM1=_RcIrigbOutputPWM1_Object((1,3,6,1,4,1,15004,4,10,1,10),_RcIrigbOutputPWM1_Type())
rcIrigbOutputPWM1.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbOutputPWM1.setStatus(_A)
class _RcIrigbPulseInterval1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_RcIrigbPulseInterval1_Type.__name__=_C
_RcIrigbPulseInterval1_Object=MibScalar
rcIrigbPulseInterval1=_RcIrigbPulseInterval1_Object((1,3,6,1,4,1,15004,4,10,1,11),_RcIrigbPulseInterval1_Type())
rcIrigbPulseInterval1.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbPulseInterval1.setStatus(_A)
class _RcIrigbPulseWidth1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_RcIrigbPulseWidth1_Type.__name__=_C
_RcIrigbPulseWidth1_Object=MibScalar
rcIrigbPulseWidth1=_RcIrigbPulseWidth1_Object((1,3,6,1,4,1,15004,4,10,1,12),_RcIrigbPulseWidth1_Type())
rcIrigbPulseWidth1.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbPulseWidth1.setStatus(_A)
_RcIrigbStartTime1_Type=RcTimeStamp
_RcIrigbStartTime1_Object=MibScalar
rcIrigbStartTime1=_RcIrigbStartTime1_Object((1,3,6,1,4,1,15004,4,10,1,13),_RcIrigbStartTime1_Type())
rcIrigbStartTime1.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbStartTime1.setStatus(_A)
class _RcIrigbOutputPWM2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5)));namedValues=NamedValues(*((_E,1),(_H,2),(_I,3),('ppx',5)))
_RcIrigbOutputPWM2_Type.__name__=_C
_RcIrigbOutputPWM2_Object=MibScalar
rcIrigbOutputPWM2=_RcIrigbOutputPWM2_Object((1,3,6,1,4,1,15004,4,10,1,14),_RcIrigbOutputPWM2_Type())
rcIrigbOutputPWM2.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbOutputPWM2.setStatus(_A)
class _RcIrigbPulseInterval2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_RcIrigbPulseInterval2_Type.__name__=_C
_RcIrigbPulseInterval2_Object=MibScalar
rcIrigbPulseInterval2=_RcIrigbPulseInterval2_Object((1,3,6,1,4,1,15004,4,10,1,15),_RcIrigbPulseInterval2_Type())
rcIrigbPulseInterval2.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbPulseInterval2.setStatus(_A)
class _RcIrigbPulseWidth2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200))
_RcIrigbPulseWidth2_Type.__name__=_C
_RcIrigbPulseWidth2_Object=MibScalar
rcIrigbPulseWidth2=_RcIrigbPulseWidth2_Object((1,3,6,1,4,1,15004,4,10,1,16),_RcIrigbPulseWidth2_Type())
rcIrigbPulseWidth2.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbPulseWidth2.setStatus(_A)
_RcIrigbStartTime2_Type=RcTimeStamp
_RcIrigbStartTime2_Object=MibScalar
rcIrigbStartTime2=_RcIrigbStartTime2_Object((1,3,6,1,4,1,15004,4,10,1,17),_RcIrigbStartTime2_Type())
rcIrigbStartTime2.setMaxAccess(_D)
if mibBuilder.loadTexts:rcIrigbStartTime2.setStatus(_A)
_RcIrigbConformance_ObjectIdentity=ObjectIdentity
rcIrigbConformance=_RcIrigbConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,10,2))
_RcIrigbGroups_ObjectIdentity=ObjectIdentity
rcIrigbGroups=_RcIrigbGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,10,2,2))
rcIrigbBaseGroup=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,1))
rcIrigbBaseGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:rcIrigbBaseGroup.setStatus(_A)
rcIrigbNotifyGroup=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,2))
rcIrigbNotifyGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:rcIrigbNotifyGroup.setStatus(_A)
rcIrigbCommonGroup=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,3))
rcIrigbCommonGroup.setObjects(*((_B,_F),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:rcIrigbCommonGroup.setStatus(_A)
rcIrigbAMOutGroup=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,4))
rcIrigbAMOutGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:rcIrigbAMOutGroup.setStatus(_A)
rcIrigbInputGroup=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,5))
rcIrigbInputGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:rcIrigbInputGroup.setStatus(_A)
rcIrigbTTLOutput01Group=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,6))
rcIrigbTTLOutput01Group.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:rcIrigbTTLOutput01Group.setStatus(_A)
rcIrigbTTLOutput02Group=ObjectGroup((1,3,6,1,4,1,15004,4,10,2,2,7))
rcIrigbTTLOutput02Group.setObjects(*((_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:rcIrigbTTLOutput02Group.setStatus(_A)
rcIrigbStatusChange=NotificationType((1,3,6,1,4,1,15004,5,35))
rcIrigbStatusChange.setObjects((_B,_F))
if mibBuilder.loadTexts:rcIrigbStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RcTimeStamp':RcTimeStamp,'rcIrigb':rcIrigb,'rcIrigbBase':rcIrigbBase,_F:rcIrigbStatus,_Q:rcIrigbAMOutput,_K:rcIrigbTimeCode,_L:rcIrigbExt,_R:rcIrigbInput,_M:rcIrigbLockInt,_N:rcIrigbCableComp,_O:rcIrigbOFM,_P:rcIrigbFreqAdj,_S:rcIrigbOutputPWM1,_T:rcIrigbPulseInterval1,_U:rcIrigbPulseWidth1,_V:rcIrigbStartTime1,_W:rcIrigbOutputPWM2,_X:rcIrigbPulseInterval2,_Y:rcIrigbPulseWidth2,_Z:rcIrigbStartTime2,'rcIrigbConformance':rcIrigbConformance,'rcIrigbGroups':rcIrigbGroups,'rcIrigbBaseGroup':rcIrigbBaseGroup,'rcIrigbNotifyGroup':rcIrigbNotifyGroup,'rcIrigbCommonGroup':rcIrigbCommonGroup,'rcIrigbAMOutGroup':rcIrigbAMOutGroup,'rcIrigbInputGroup':rcIrigbInputGroup,'rcIrigbTTLOutput01Group':rcIrigbTTLOutput01Group,'rcIrigbTTLOutput02Group':rcIrigbTTLOutput02Group,_J:rcIrigbStatusChange})