_v='nmsIfThresholdNotifsGroup'
_u='nmsIfThresholdFiredGroup'
_t='nmsIfThresholdTemplateGroup'
_s='nmsifthTemplateIfStatusChange'
_r='nmsifthIfThresholdCleared'
_q='nmsifthIfThresholdFired'
_p='nmsifthThresholdApsSwitchover'
_o='nmsifthThresholdClearedValue'
_n='nmsifthTemplateNotifyHoldDownTime'
_m='nmsifthIfThresholdFiredMaxSeverity'
_l='nmsifthIfThresholdsFired'
_k='nmsifthThresholdFiredLastChange'
_j='nmsifthThresholdFiredNotifyEnable'
_i='nmsifthTemplateIfAssignRowStatus'
_h='nmsifthTemplateIfLastChange'
_g='nmsifthThresholdRowStatus'
_f='nmsifthThresholdSampleInterval'
_e='nmsifthThresholdFiredValue'
_d='nmsifthThresholdDirection'
_c='nmsifthThresholdType'
_b='nmsifthThresholdSeverity'
_a='nmsifthThresholdObject'
_Z='nmsifthThresholdDescr'
_Y='nmsifthThresholdLastChange'
_X='nmsifthTemplateRowStatus'
_W='nmsifthTemplateNotifyHoldDownType'
_V='nmsifthTemplateName'
_U='nmsifthTemplateLastChange'
_T='nmsifthTemplateIndexNext'
_S='nmsifthIfThresholdFiredTemplate'
_R='nmsifthTemplateIfAssignInterface'
_Q='nmsifthThresholdIndex'
_P='TruthValue'
_O='ifIndex'
_N='IF-MIB'
_M='nmsifthTemplateIfAssignOperStatus'
_L='Unsigned32'
_K='SnmpAdminString'
_J='nmsifthIfThresholdFiredLstSeverity'
_I='nmsifthIfThresholdFiredLstChange'
_H='nmsifthIfLastThresholdFired'
_G='not-accessible'
_F='nmsifthTemplateIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='FS-NMS-IF-THRESHOLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('FS-NMS-SMI','nmsMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_N,'InterfaceIndex',_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
nmsIfThresholdMIB=ModuleIdentity((1,3,6,1,4,1,52642,9,218))
if mibBuilder.loadTexts:nmsIfThresholdMIB.setRevisions(('2003-10-16 00:00',))
class NMSifthTemplateIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
class NMSifthTemplateIndexOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
class NMSifthThresholdIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class NMSifthThresholdList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class NMSifthThresholdSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fail',1),('degrade',2),('info',3),('other',4)))
class NMSifthThresholdSeverityOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_NmsIfThresholdMIBObjects_ObjectIdentity=ObjectIdentity
nmsIfThresholdMIBObjects=_NmsIfThresholdMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,9,218,1))
_NmsifthTemplateGroup_ObjectIdentity=ObjectIdentity
nmsifthTemplateGroup=_NmsifthTemplateGroup_ObjectIdentity((1,3,6,1,4,1,52642,9,218,1,1))
_NmsifthTemplateIndexNext_Type=NMSifthTemplateIndexOrZero
_NmsifthTemplateIndexNext_Object=MibScalar
nmsifthTemplateIndexNext=_NmsifthTemplateIndexNext_Object((1,3,6,1,4,1,52642,9,218,1,1,1),_NmsifthTemplateIndexNext_Type())
nmsifthTemplateIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthTemplateIndexNext.setStatus(_A)
_NmsifthTemplateLastChange_Type=TimeStamp
_NmsifthTemplateLastChange_Object=MibScalar
nmsifthTemplateLastChange=_NmsifthTemplateLastChange_Object((1,3,6,1,4,1,52642,9,218,1,1,2),_NmsifthTemplateLastChange_Type())
nmsifthTemplateLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthTemplateLastChange.setStatus(_A)
_NmsifthTemplateTable_Object=MibTable
nmsifthTemplateTable=_NmsifthTemplateTable_Object((1,3,6,1,4,1,52642,9,218,1,1,3))
if mibBuilder.loadTexts:nmsifthTemplateTable.setStatus(_A)
_NmsifthTemplateEntry_Object=MibTableRow
nmsifthTemplateEntry=_NmsifthTemplateEntry_Object((1,3,6,1,4,1,52642,9,218,1,1,3,1))
nmsifthTemplateEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:nmsifthTemplateEntry.setStatus(_A)
_NmsifthTemplateIndex_Type=NMSifthTemplateIndex
_NmsifthTemplateIndex_Object=MibTableColumn
nmsifthTemplateIndex=_NmsifthTemplateIndex_Object((1,3,6,1,4,1,52642,9,218,1,1,3,1,1),_NmsifthTemplateIndex_Type())
nmsifthTemplateIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nmsifthTemplateIndex.setStatus(_A)
class _NmsifthTemplateName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NmsifthTemplateName_Type.__name__=_K
_NmsifthTemplateName_Object=MibTableColumn
nmsifthTemplateName=_NmsifthTemplateName_Object((1,3,6,1,4,1,52642,9,218,1,1,3,1,2),_NmsifthTemplateName_Type())
nmsifthTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthTemplateName.setStatus(_A)
class _NmsifthTemplateNotifyHoldDownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('holdDownTimer',2),('fireAndClearThresholds',3)))
_NmsifthTemplateNotifyHoldDownType_Type.__name__=_E
_NmsifthTemplateNotifyHoldDownType_Object=MibTableColumn
nmsifthTemplateNotifyHoldDownType=_NmsifthTemplateNotifyHoldDownType_Object((1,3,6,1,4,1,52642,9,218,1,1,3,1,3),_NmsifthTemplateNotifyHoldDownType_Type())
nmsifthTemplateNotifyHoldDownType.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthTemplateNotifyHoldDownType.setStatus(_A)
class _NmsifthTemplateNotifyHoldDownTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_NmsifthTemplateNotifyHoldDownTime_Type.__name__=_L
_NmsifthTemplateNotifyHoldDownTime_Object=MibTableColumn
nmsifthTemplateNotifyHoldDownTime=_NmsifthTemplateNotifyHoldDownTime_Object((1,3,6,1,4,1,52642,9,218,1,1,3,1,4),_NmsifthTemplateNotifyHoldDownTime_Type())
nmsifthTemplateNotifyHoldDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthTemplateNotifyHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:nmsifthTemplateNotifyHoldDownTime.setUnits('seconds')
_NmsifthTemplateRowStatus_Type=RowStatus
_NmsifthTemplateRowStatus_Object=MibTableColumn
nmsifthTemplateRowStatus=_NmsifthTemplateRowStatus_Object((1,3,6,1,4,1,52642,9,218,1,1,3,1,5),_NmsifthTemplateRowStatus_Type())
nmsifthTemplateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthTemplateRowStatus.setStatus(_A)
_NmsifthThresholdLastChange_Type=TimeStamp
_NmsifthThresholdLastChange_Object=MibScalar
nmsifthThresholdLastChange=_NmsifthThresholdLastChange_Object((1,3,6,1,4,1,52642,9,218,1,1,4),_NmsifthThresholdLastChange_Type())
nmsifthThresholdLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthThresholdLastChange.setStatus(_A)
_NmsifthThresholdTable_Object=MibTable
nmsifthThresholdTable=_NmsifthThresholdTable_Object((1,3,6,1,4,1,52642,9,218,1,1,5))
if mibBuilder.loadTexts:nmsifthThresholdTable.setStatus(_A)
_NmsifthThresholdEntry_Object=MibTableRow
nmsifthThresholdEntry=_NmsifthThresholdEntry_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1))
nmsifthThresholdEntry.setIndexNames((0,_B,_F),(0,_B,_Q))
if mibBuilder.loadTexts:nmsifthThresholdEntry.setStatus(_A)
_NmsifthThresholdIndex_Type=NMSifthThresholdIndex
_NmsifthThresholdIndex_Object=MibTableColumn
nmsifthThresholdIndex=_NmsifthThresholdIndex_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,1),_NmsifthThresholdIndex_Type())
nmsifthThresholdIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:nmsifthThresholdIndex.setStatus(_A)
class _NmsifthThresholdDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NmsifthThresholdDescr_Type.__name__=_K
_NmsifthThresholdDescr_Object=MibTableColumn
nmsifthThresholdDescr=_NmsifthThresholdDescr_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,2),_NmsifthThresholdDescr_Type())
nmsifthThresholdDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdDescr.setStatus(_A)
_NmsifthThresholdObject_Type=ObjectIdentifier
_NmsifthThresholdObject_Object=MibTableColumn
nmsifthThresholdObject=_NmsifthThresholdObject_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,3),_NmsifthThresholdObject_Type())
nmsifthThresholdObject.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdObject.setStatus(_A)
_NmsifthThresholdSeverity_Type=NMSifthThresholdSeverity
_NmsifthThresholdSeverity_Object=MibTableColumn
nmsifthThresholdSeverity=_NmsifthThresholdSeverity_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,4),_NmsifthThresholdSeverity_Type())
nmsifthThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdSeverity.setStatus(_A)
class _NmsifthThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('rateOfIncreaseExponentXIfSpeed',3)))
_NmsifthThresholdType_Type.__name__=_E
_NmsifthThresholdType_Object=MibTableColumn
nmsifthThresholdType=_NmsifthThresholdType_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,5),_NmsifthThresholdType_Type())
nmsifthThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdType.setStatus(_A)
class _NmsifthThresholdDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rising',1),('falling',2)))
_NmsifthThresholdDirection_Type.__name__=_E
_NmsifthThresholdDirection_Object=MibTableColumn
nmsifthThresholdDirection=_NmsifthThresholdDirection_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,6),_NmsifthThresholdDirection_Type())
nmsifthThresholdDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdDirection.setStatus(_A)
class _NmsifthThresholdFiredValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NmsifthThresholdFiredValue_Type.__name__=_E
_NmsifthThresholdFiredValue_Object=MibTableColumn
nmsifthThresholdFiredValue=_NmsifthThresholdFiredValue_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,7),_NmsifthThresholdFiredValue_Type())
nmsifthThresholdFiredValue.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdFiredValue.setStatus(_A)
class _NmsifthThresholdClearedValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_NmsifthThresholdClearedValue_Type.__name__=_E
_NmsifthThresholdClearedValue_Object=MibTableColumn
nmsifthThresholdClearedValue=_NmsifthThresholdClearedValue_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,8),_NmsifthThresholdClearedValue_Type())
nmsifthThresholdClearedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdClearedValue.setStatus(_A)
class _NmsifthThresholdSampleInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,900000))
_NmsifthThresholdSampleInterval_Type.__name__=_L
_NmsifthThresholdSampleInterval_Object=MibTableColumn
nmsifthThresholdSampleInterval=_NmsifthThresholdSampleInterval_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,9),_NmsifthThresholdSampleInterval_Type())
nmsifthThresholdSampleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdSampleInterval.setStatus(_A)
if mibBuilder.loadTexts:nmsifthThresholdSampleInterval.setUnits('milliseconds')
class _NmsifthThresholdApsSwitchover_Type(TruthValue):defaultValue=2
_NmsifthThresholdApsSwitchover_Type.__name__=_P
_NmsifthThresholdApsSwitchover_Object=MibTableColumn
nmsifthThresholdApsSwitchover=_NmsifthThresholdApsSwitchover_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,10),_NmsifthThresholdApsSwitchover_Type())
nmsifthThresholdApsSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdApsSwitchover.setStatus(_A)
_NmsifthThresholdRowStatus_Type=RowStatus
_NmsifthThresholdRowStatus_Object=MibTableColumn
nmsifthThresholdRowStatus=_NmsifthThresholdRowStatus_Object((1,3,6,1,4,1,52642,9,218,1,1,5,1,11),_NmsifthThresholdRowStatus_Type())
nmsifthThresholdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthThresholdRowStatus.setStatus(_A)
_NmsifthTemplateIfAssignGroup_ObjectIdentity=ObjectIdentity
nmsifthTemplateIfAssignGroup=_NmsifthTemplateIfAssignGroup_ObjectIdentity((1,3,6,1,4,1,52642,9,218,1,2))
_NmsifthTemplateIfLastChange_Type=TimeStamp
_NmsifthTemplateIfLastChange_Object=MibScalar
nmsifthTemplateIfLastChange=_NmsifthTemplateIfLastChange_Object((1,3,6,1,4,1,52642,9,218,1,2,1),_NmsifthTemplateIfLastChange_Type())
nmsifthTemplateIfLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthTemplateIfLastChange.setStatus(_A)
_NmsifthTemplateIfAssignTable_Object=MibTable
nmsifthTemplateIfAssignTable=_NmsifthTemplateIfAssignTable_Object((1,3,6,1,4,1,52642,9,218,1,2,2))
if mibBuilder.loadTexts:nmsifthTemplateIfAssignTable.setStatus(_A)
_NmsifthTemplateIfAssignEntry_Object=MibTableRow
nmsifthTemplateIfAssignEntry=_NmsifthTemplateIfAssignEntry_Object((1,3,6,1,4,1,52642,9,218,1,2,2,1))
nmsifthTemplateIfAssignEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:nmsifthTemplateIfAssignEntry.setStatus(_A)
_NmsifthTemplateIfAssignInterface_Type=InterfaceIndex
_NmsifthTemplateIfAssignInterface_Object=MibTableColumn
nmsifthTemplateIfAssignInterface=_NmsifthTemplateIfAssignInterface_Object((1,3,6,1,4,1,52642,9,218,1,2,2,1,1),_NmsifthTemplateIfAssignInterface_Type())
nmsifthTemplateIfAssignInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:nmsifthTemplateIfAssignInterface.setStatus(_A)
class _NmsifthTemplateIfAssignOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_NmsifthTemplateIfAssignOperStatus_Type.__name__=_E
_NmsifthTemplateIfAssignOperStatus_Object=MibTableColumn
nmsifthTemplateIfAssignOperStatus=_NmsifthTemplateIfAssignOperStatus_Object((1,3,6,1,4,1,52642,9,218,1,2,2,1,2),_NmsifthTemplateIfAssignOperStatus_Type())
nmsifthTemplateIfAssignOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthTemplateIfAssignOperStatus.setStatus(_A)
_NmsifthTemplateIfAssignRowStatus_Type=RowStatus
_NmsifthTemplateIfAssignRowStatus_Object=MibTableColumn
nmsifthTemplateIfAssignRowStatus=_NmsifthTemplateIfAssignRowStatus_Object((1,3,6,1,4,1,52642,9,218,1,2,2,1,3),_NmsifthTemplateIfAssignRowStatus_Type())
nmsifthTemplateIfAssignRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nmsifthTemplateIfAssignRowStatus.setStatus(_A)
_NmsifthIfThresholdFiredGroup_ObjectIdentity=ObjectIdentity
nmsifthIfThresholdFiredGroup=_NmsifthIfThresholdFiredGroup_ObjectIdentity((1,3,6,1,4,1,52642,9,218,1,3))
_NmsifthThresholdFiredNotifyEnable_Type=NMSifthThresholdSeverityOrZero
_NmsifthThresholdFiredNotifyEnable_Object=MibScalar
nmsifthThresholdFiredNotifyEnable=_NmsifthThresholdFiredNotifyEnable_Object((1,3,6,1,4,1,52642,9,218,1,3,1),_NmsifthThresholdFiredNotifyEnable_Type())
nmsifthThresholdFiredNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:nmsifthThresholdFiredNotifyEnable.setStatus(_A)
_NmsifthThresholdFiredLastChange_Type=TimeStamp
_NmsifthThresholdFiredLastChange_Object=MibScalar
nmsifthThresholdFiredLastChange=_NmsifthThresholdFiredLastChange_Object((1,3,6,1,4,1,52642,9,218,1,3,2),_NmsifthThresholdFiredLastChange_Type())
nmsifthThresholdFiredLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthThresholdFiredLastChange.setStatus(_A)
_NmsifthIfThresholdFiredTable_Object=MibTable
nmsifthIfThresholdFiredTable=_NmsifthIfThresholdFiredTable_Object((1,3,6,1,4,1,52642,9,218,1,3,3))
if mibBuilder.loadTexts:nmsifthIfThresholdFiredTable.setStatus(_A)
_NmsifthIfThresholdFiredEntry_Object=MibTableRow
nmsifthIfThresholdFiredEntry=_NmsifthIfThresholdFiredEntry_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1))
nmsifthIfThresholdFiredEntry.setIndexNames((0,_N,_O),(0,_B,_S))
if mibBuilder.loadTexts:nmsifthIfThresholdFiredEntry.setStatus(_A)
_NmsifthIfThresholdFiredTemplate_Type=NMSifthTemplateIndex
_NmsifthIfThresholdFiredTemplate_Object=MibTableColumn
nmsifthIfThresholdFiredTemplate=_NmsifthIfThresholdFiredTemplate_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1,1),_NmsifthIfThresholdFiredTemplate_Type())
nmsifthIfThresholdFiredTemplate.setMaxAccess(_G)
if mibBuilder.loadTexts:nmsifthIfThresholdFiredTemplate.setStatus(_A)
_NmsifthIfThresholdsFired_Type=NMSifthThresholdList
_NmsifthIfThresholdsFired_Object=MibTableColumn
nmsifthIfThresholdsFired=_NmsifthIfThresholdsFired_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1,2),_NmsifthIfThresholdsFired_Type())
nmsifthIfThresholdsFired.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthIfThresholdsFired.setStatus(_A)
_NmsifthIfLastThresholdFired_Type=NMSifthThresholdIndex
_NmsifthIfLastThresholdFired_Object=MibTableColumn
nmsifthIfLastThresholdFired=_NmsifthIfLastThresholdFired_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1,3),_NmsifthIfLastThresholdFired_Type())
nmsifthIfLastThresholdFired.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthIfLastThresholdFired.setStatus(_A)
_NmsifthIfThresholdFiredLstChange_Type=TimeStamp
_NmsifthIfThresholdFiredLstChange_Object=MibTableColumn
nmsifthIfThresholdFiredLstChange=_NmsifthIfThresholdFiredLstChange_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1,4),_NmsifthIfThresholdFiredLstChange_Type())
nmsifthIfThresholdFiredLstChange.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthIfThresholdFiredLstChange.setStatus(_A)
_NmsifthIfThresholdFiredLstSeverity_Type=NMSifthThresholdSeverity
_NmsifthIfThresholdFiredLstSeverity_Object=MibTableColumn
nmsifthIfThresholdFiredLstSeverity=_NmsifthIfThresholdFiredLstSeverity_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1,5),_NmsifthIfThresholdFiredLstSeverity_Type())
nmsifthIfThresholdFiredLstSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthIfThresholdFiredLstSeverity.setStatus(_A)
_NmsifthIfThresholdFiredMaxSeverity_Type=NMSifthThresholdSeverity
_NmsifthIfThresholdFiredMaxSeverity_Object=MibTableColumn
nmsifthIfThresholdFiredMaxSeverity=_NmsifthIfThresholdFiredMaxSeverity_Object((1,3,6,1,4,1,52642,9,218,1,3,3,1,6),_NmsifthIfThresholdFiredMaxSeverity_Type())
nmsifthIfThresholdFiredMaxSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:nmsifthIfThresholdFiredMaxSeverity.setStatus(_A)
_NmsIfThresholdMIBNotifications_ObjectIdentity=ObjectIdentity
nmsIfThresholdMIBNotifications=_NmsIfThresholdMIBNotifications_ObjectIdentity((1,3,6,1,4,1,52642,9,218,2))
_NmsifthMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
nmsifthMIBNotificationsPrefix=_NmsifthMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,52642,9,218,2,0))
_NmsIfThresholdMIBConformance_ObjectIdentity=ObjectIdentity
nmsIfThresholdMIBConformance=_NmsIfThresholdMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,9,218,3))
_NmsIfThresholdMIBCompliances_ObjectIdentity=ObjectIdentity
nmsIfThresholdMIBCompliances=_NmsIfThresholdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,9,218,3,1))
_NmsIfThresholdMIBGroups_ObjectIdentity=ObjectIdentity
nmsIfThresholdMIBGroups=_NmsIfThresholdMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,9,218,3,2))
nmsIfThresholdTemplateGroup=ObjectGroup((1,3,6,1,4,1,52642,9,218,3,2,1))
nmsIfThresholdTemplateGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_M),(_B,_i)))
if mibBuilder.loadTexts:nmsIfThresholdTemplateGroup.setStatus(_A)
nmsIfThresholdFiredGroup=ObjectGroup((1,3,6,1,4,1,52642,9,218,3,2,2))
nmsIfThresholdFiredGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_H),(_B,_I),(_B,_J),(_B,_m)))
if mibBuilder.loadTexts:nmsIfThresholdFiredGroup.setStatus(_A)
nmsifthHoldDownTimerGroup=ObjectGroup((1,3,6,1,4,1,52642,9,218,3,2,3))
nmsifthHoldDownTimerGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:nmsifthHoldDownTimerGroup.setStatus(_A)
nmsifthHoldDownHysteresisGroup=ObjectGroup((1,3,6,1,4,1,52642,9,218,3,2,4))
nmsifthHoldDownHysteresisGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:nmsifthHoldDownHysteresisGroup.setStatus(_A)
nmsifthApsGroup=ObjectGroup((1,3,6,1,4,1,52642,9,218,3,2,5))
nmsifthApsGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:nmsifthApsGroup.setStatus(_A)
nmsifthIfThresholdFired=NotificationType((1,3,6,1,4,1,52642,9,218,2,0,1))
nmsifthIfThresholdFired.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:nmsifthIfThresholdFired.setStatus(_A)
nmsifthIfThresholdCleared=NotificationType((1,3,6,1,4,1,52642,9,218,2,0,2))
nmsifthIfThresholdCleared.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:nmsifthIfThresholdCleared.setStatus(_A)
nmsifthTemplateIfStatusChange=NotificationType((1,3,6,1,4,1,52642,9,218,2,0,3))
nmsifthTemplateIfStatusChange.setObjects((_B,_M))
if mibBuilder.loadTexts:nmsifthTemplateIfStatusChange.setStatus(_A)
nmsIfThresholdNotifsGroup=NotificationGroup((1,3,6,1,4,1,52642,9,218,3,2,6))
nmsIfThresholdNotifsGroup.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:nmsIfThresholdNotifsGroup.setStatus(_A)
nmsifthTemplateIfNotifsGroup=NotificationGroup((1,3,6,1,4,1,52642,9,218,3,2,7))
nmsifthTemplateIfNotifsGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:nmsifthTemplateIfNotifsGroup.setStatus(_A)
nmsIfThresholdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,9,218,3,1,1))
nmsIfThresholdMIBCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:nmsIfThresholdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NMSifthTemplateIndex':NMSifthTemplateIndex,'NMSifthTemplateIndexOrZero':NMSifthTemplateIndexOrZero,'NMSifthThresholdIndex':NMSifthThresholdIndex,'NMSifthThresholdList':NMSifthThresholdList,'NMSifthThresholdSeverity':NMSifthThresholdSeverity,'NMSifthThresholdSeverityOrZero':NMSifthThresholdSeverityOrZero,'nmsIfThresholdMIB':nmsIfThresholdMIB,'nmsIfThresholdMIBObjects':nmsIfThresholdMIBObjects,'nmsifthTemplateGroup':nmsifthTemplateGroup,_T:nmsifthTemplateIndexNext,_U:nmsifthTemplateLastChange,'nmsifthTemplateTable':nmsifthTemplateTable,'nmsifthTemplateEntry':nmsifthTemplateEntry,_F:nmsifthTemplateIndex,_V:nmsifthTemplateName,_W:nmsifthTemplateNotifyHoldDownType,_n:nmsifthTemplateNotifyHoldDownTime,_X:nmsifthTemplateRowStatus,_Y:nmsifthThresholdLastChange,'nmsifthThresholdTable':nmsifthThresholdTable,'nmsifthThresholdEntry':nmsifthThresholdEntry,_Q:nmsifthThresholdIndex,_Z:nmsifthThresholdDescr,_a:nmsifthThresholdObject,_b:nmsifthThresholdSeverity,_c:nmsifthThresholdType,_d:nmsifthThresholdDirection,_e:nmsifthThresholdFiredValue,_o:nmsifthThresholdClearedValue,_f:nmsifthThresholdSampleInterval,_p:nmsifthThresholdApsSwitchover,_g:nmsifthThresholdRowStatus,'nmsifthTemplateIfAssignGroup':nmsifthTemplateIfAssignGroup,_h:nmsifthTemplateIfLastChange,'nmsifthTemplateIfAssignTable':nmsifthTemplateIfAssignTable,'nmsifthTemplateIfAssignEntry':nmsifthTemplateIfAssignEntry,_R:nmsifthTemplateIfAssignInterface,_M:nmsifthTemplateIfAssignOperStatus,_i:nmsifthTemplateIfAssignRowStatus,'nmsifthIfThresholdFiredGroup':nmsifthIfThresholdFiredGroup,_j:nmsifthThresholdFiredNotifyEnable,_k:nmsifthThresholdFiredLastChange,'nmsifthIfThresholdFiredTable':nmsifthIfThresholdFiredTable,'nmsifthIfThresholdFiredEntry':nmsifthIfThresholdFiredEntry,_S:nmsifthIfThresholdFiredTemplate,_l:nmsifthIfThresholdsFired,_H:nmsifthIfLastThresholdFired,_I:nmsifthIfThresholdFiredLstChange,_J:nmsifthIfThresholdFiredLstSeverity,_m:nmsifthIfThresholdFiredMaxSeverity,'nmsIfThresholdMIBNotifications':nmsIfThresholdMIBNotifications,'nmsifthMIBNotificationsPrefix':nmsifthMIBNotificationsPrefix,_q:nmsifthIfThresholdFired,_r:nmsifthIfThresholdCleared,_s:nmsifthTemplateIfStatusChange,'nmsIfThresholdMIBConformance':nmsIfThresholdMIBConformance,'nmsIfThresholdMIBCompliances':nmsIfThresholdMIBCompliances,'nmsIfThresholdMIBCompliance':nmsIfThresholdMIBCompliance,'nmsIfThresholdMIBGroups':nmsIfThresholdMIBGroups,_t:nmsIfThresholdTemplateGroup,_u:nmsIfThresholdFiredGroup,'nmsifthHoldDownTimerGroup':nmsifthHoldDownTimerGroup,'nmsifthHoldDownHysteresisGroup':nmsifthHoldDownHysteresisGroup,'nmsifthApsGroup':nmsifthApsGroup,_v:nmsIfThresholdNotifsGroup,'nmsifthTemplateIfNotifsGroup':nmsifthTemplateIfNotifsGroup})