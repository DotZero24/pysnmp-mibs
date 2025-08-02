_v='cIfThresholdNotifsGroup'
_u='cIfThresholdFiredGroup'
_t='cIfThresholdTemplateGroup'
_s='cifthTemplateIfStatusChange'
_r='cifthIfThresholdCleared'
_q='cifthIfThresholdFired'
_p='cifthThresholdApsSwitchover'
_o='cifthThresholdClearedValue'
_n='cifthTemplateNotifyHoldDownTime'
_m='cifthIfThresholdFiredMaxSeverity'
_l='cifthIfThresholdsFired'
_k='cifthThresholdFiredLastChange'
_j='cifthThresholdFiredNotifyEnable'
_i='cifthTemplateIfAssignRowStatus'
_h='cifthTemplateIfLastChange'
_g='cifthThresholdRowStatus'
_f='cifthThresholdSampleInterval'
_e='cifthThresholdFiredValue'
_d='cifthThresholdDirection'
_c='cifthThresholdType'
_b='cifthThresholdSeverity'
_a='cifthThresholdObject'
_Z='cifthThresholdDescr'
_Y='cifthThresholdLastChange'
_X='cifthTemplateRowStatus'
_W='cifthTemplateNotifyHoldDownType'
_V='cifthTemplateName'
_U='cifthTemplateLastChange'
_T='cifthTemplateIndexNext'
_S='cifthIfThresholdFiredTemplate'
_R='cifthTemplateIfAssignInterface'
_Q='cifthThresholdIndex'
_P='TruthValue'
_O='ifIndex'
_N='IF-MIB'
_M='cifthTemplateIfAssignOperStatus'
_L='Unsigned32'
_K='SnmpAdminString'
_J='cifthIfThresholdFiredLstSeverity'
_I='cifthIfThresholdFiredLstChange'
_H='cifthIfLastThresholdFired'
_G='not-accessible'
_F='cifthTemplateIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='CISCO-IF-THRESHOLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_N,'InterfaceIndex',_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
ciscoIfThresholdMIB=ModuleIdentity((1,3,6,1,4,1,9,9,218))
if mibBuilder.loadTexts:ciscoIfThresholdMIB.setRevisions(('2001-09-14 00:00','2001-06-14 00:00'))
class CifthTemplateIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
class CifthTemplateIndexOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
class CifthThresholdIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class CifthThresholdList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class CifthThresholdSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fail',1),('degrade',2),('info',3),('other',4)))
class CifthThresholdSeverityOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CIfThresholdMIBObjects_ObjectIdentity=ObjectIdentity
cIfThresholdMIBObjects=_CIfThresholdMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,218,1))
_CifthTemplateGroup_ObjectIdentity=ObjectIdentity
cifthTemplateGroup=_CifthTemplateGroup_ObjectIdentity((1,3,6,1,4,1,9,9,218,1,1))
_CifthTemplateIndexNext_Type=CifthTemplateIndexOrZero
_CifthTemplateIndexNext_Object=MibScalar
cifthTemplateIndexNext=_CifthTemplateIndexNext_Object((1,3,6,1,4,1,9,9,218,1,1,1),_CifthTemplateIndexNext_Type())
cifthTemplateIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthTemplateIndexNext.setStatus(_A)
_CifthTemplateLastChange_Type=TimeStamp
_CifthTemplateLastChange_Object=MibScalar
cifthTemplateLastChange=_CifthTemplateLastChange_Object((1,3,6,1,4,1,9,9,218,1,1,2),_CifthTemplateLastChange_Type())
cifthTemplateLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthTemplateLastChange.setStatus(_A)
_CifthTemplateTable_Object=MibTable
cifthTemplateTable=_CifthTemplateTable_Object((1,3,6,1,4,1,9,9,218,1,1,3))
if mibBuilder.loadTexts:cifthTemplateTable.setStatus(_A)
_CifthTemplateEntry_Object=MibTableRow
cifthTemplateEntry=_CifthTemplateEntry_Object((1,3,6,1,4,1,9,9,218,1,1,3,1))
cifthTemplateEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cifthTemplateEntry.setStatus(_A)
_CifthTemplateIndex_Type=CifthTemplateIndex
_CifthTemplateIndex_Object=MibTableColumn
cifthTemplateIndex=_CifthTemplateIndex_Object((1,3,6,1,4,1,9,9,218,1,1,3,1,1),_CifthTemplateIndex_Type())
cifthTemplateIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cifthTemplateIndex.setStatus(_A)
class _CifthTemplateName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CifthTemplateName_Type.__name__=_K
_CifthTemplateName_Object=MibTableColumn
cifthTemplateName=_CifthTemplateName_Object((1,3,6,1,4,1,9,9,218,1,1,3,1,2),_CifthTemplateName_Type())
cifthTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthTemplateName.setStatus(_A)
class _CifthTemplateNotifyHoldDownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('holdDownTimer',2),('fireAndClearThresholds',3)))
_CifthTemplateNotifyHoldDownType_Type.__name__=_E
_CifthTemplateNotifyHoldDownType_Object=MibTableColumn
cifthTemplateNotifyHoldDownType=_CifthTemplateNotifyHoldDownType_Object((1,3,6,1,4,1,9,9,218,1,1,3,1,3),_CifthTemplateNotifyHoldDownType_Type())
cifthTemplateNotifyHoldDownType.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthTemplateNotifyHoldDownType.setStatus(_A)
class _CifthTemplateNotifyHoldDownTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_CifthTemplateNotifyHoldDownTime_Type.__name__=_L
_CifthTemplateNotifyHoldDownTime_Object=MibTableColumn
cifthTemplateNotifyHoldDownTime=_CifthTemplateNotifyHoldDownTime_Object((1,3,6,1,4,1,9,9,218,1,1,3,1,4),_CifthTemplateNotifyHoldDownTime_Type())
cifthTemplateNotifyHoldDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthTemplateNotifyHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:cifthTemplateNotifyHoldDownTime.setUnits('seconds')
_CifthTemplateRowStatus_Type=RowStatus
_CifthTemplateRowStatus_Object=MibTableColumn
cifthTemplateRowStatus=_CifthTemplateRowStatus_Object((1,3,6,1,4,1,9,9,218,1,1,3,1,5),_CifthTemplateRowStatus_Type())
cifthTemplateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthTemplateRowStatus.setStatus(_A)
_CifthThresholdLastChange_Type=TimeStamp
_CifthThresholdLastChange_Object=MibScalar
cifthThresholdLastChange=_CifthThresholdLastChange_Object((1,3,6,1,4,1,9,9,218,1,1,4),_CifthThresholdLastChange_Type())
cifthThresholdLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthThresholdLastChange.setStatus(_A)
_CifthThresholdTable_Object=MibTable
cifthThresholdTable=_CifthThresholdTable_Object((1,3,6,1,4,1,9,9,218,1,1,5))
if mibBuilder.loadTexts:cifthThresholdTable.setStatus(_A)
_CifthThresholdEntry_Object=MibTableRow
cifthThresholdEntry=_CifthThresholdEntry_Object((1,3,6,1,4,1,9,9,218,1,1,5,1))
cifthThresholdEntry.setIndexNames((0,_B,_F),(0,_B,_Q))
if mibBuilder.loadTexts:cifthThresholdEntry.setStatus(_A)
_CifthThresholdIndex_Type=CifthThresholdIndex
_CifthThresholdIndex_Object=MibTableColumn
cifthThresholdIndex=_CifthThresholdIndex_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,1),_CifthThresholdIndex_Type())
cifthThresholdIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:cifthThresholdIndex.setStatus(_A)
class _CifthThresholdDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CifthThresholdDescr_Type.__name__=_K
_CifthThresholdDescr_Object=MibTableColumn
cifthThresholdDescr=_CifthThresholdDescr_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,2),_CifthThresholdDescr_Type())
cifthThresholdDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdDescr.setStatus(_A)
_CifthThresholdObject_Type=ObjectIdentifier
_CifthThresholdObject_Object=MibTableColumn
cifthThresholdObject=_CifthThresholdObject_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,3),_CifthThresholdObject_Type())
cifthThresholdObject.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdObject.setStatus(_A)
_CifthThresholdSeverity_Type=CifthThresholdSeverity
_CifthThresholdSeverity_Object=MibTableColumn
cifthThresholdSeverity=_CifthThresholdSeverity_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,4),_CifthThresholdSeverity_Type())
cifthThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdSeverity.setStatus(_A)
class _CifthThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('rateOfIncreaseExponentXIfSpeed',3)))
_CifthThresholdType_Type.__name__=_E
_CifthThresholdType_Object=MibTableColumn
cifthThresholdType=_CifthThresholdType_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,5),_CifthThresholdType_Type())
cifthThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdType.setStatus(_A)
class _CifthThresholdDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rising',1),('falling',2)))
_CifthThresholdDirection_Type.__name__=_E
_CifthThresholdDirection_Object=MibTableColumn
cifthThresholdDirection=_CifthThresholdDirection_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,6),_CifthThresholdDirection_Type())
cifthThresholdDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdDirection.setStatus(_A)
class _CifthThresholdFiredValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CifthThresholdFiredValue_Type.__name__=_E
_CifthThresholdFiredValue_Object=MibTableColumn
cifthThresholdFiredValue=_CifthThresholdFiredValue_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,7),_CifthThresholdFiredValue_Type())
cifthThresholdFiredValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdFiredValue.setStatus(_A)
class _CifthThresholdClearedValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CifthThresholdClearedValue_Type.__name__=_E
_CifthThresholdClearedValue_Object=MibTableColumn
cifthThresholdClearedValue=_CifthThresholdClearedValue_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,8),_CifthThresholdClearedValue_Type())
cifthThresholdClearedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdClearedValue.setStatus(_A)
class _CifthThresholdSampleInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,900000))
_CifthThresholdSampleInterval_Type.__name__=_L
_CifthThresholdSampleInterval_Object=MibTableColumn
cifthThresholdSampleInterval=_CifthThresholdSampleInterval_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,9),_CifthThresholdSampleInterval_Type())
cifthThresholdSampleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdSampleInterval.setStatus(_A)
if mibBuilder.loadTexts:cifthThresholdSampleInterval.setUnits('milliseconds')
class _CifthThresholdApsSwitchover_Type(TruthValue):defaultValue=2
_CifthThresholdApsSwitchover_Type.__name__=_P
_CifthThresholdApsSwitchover_Object=MibTableColumn
cifthThresholdApsSwitchover=_CifthThresholdApsSwitchover_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,10),_CifthThresholdApsSwitchover_Type())
cifthThresholdApsSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdApsSwitchover.setStatus(_A)
_CifthThresholdRowStatus_Type=RowStatus
_CifthThresholdRowStatus_Object=MibTableColumn
cifthThresholdRowStatus=_CifthThresholdRowStatus_Object((1,3,6,1,4,1,9,9,218,1,1,5,1,11),_CifthThresholdRowStatus_Type())
cifthThresholdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthThresholdRowStatus.setStatus(_A)
_CifthTemplateIfAssignGroup_ObjectIdentity=ObjectIdentity
cifthTemplateIfAssignGroup=_CifthTemplateIfAssignGroup_ObjectIdentity((1,3,6,1,4,1,9,9,218,1,2))
_CifthTemplateIfLastChange_Type=TimeStamp
_CifthTemplateIfLastChange_Object=MibScalar
cifthTemplateIfLastChange=_CifthTemplateIfLastChange_Object((1,3,6,1,4,1,9,9,218,1,2,1),_CifthTemplateIfLastChange_Type())
cifthTemplateIfLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthTemplateIfLastChange.setStatus(_A)
_CifthTemplateIfAssignTable_Object=MibTable
cifthTemplateIfAssignTable=_CifthTemplateIfAssignTable_Object((1,3,6,1,4,1,9,9,218,1,2,2))
if mibBuilder.loadTexts:cifthTemplateIfAssignTable.setStatus(_A)
_CifthTemplateIfAssignEntry_Object=MibTableRow
cifthTemplateIfAssignEntry=_CifthTemplateIfAssignEntry_Object((1,3,6,1,4,1,9,9,218,1,2,2,1))
cifthTemplateIfAssignEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:cifthTemplateIfAssignEntry.setStatus(_A)
_CifthTemplateIfAssignInterface_Type=InterfaceIndex
_CifthTemplateIfAssignInterface_Object=MibTableColumn
cifthTemplateIfAssignInterface=_CifthTemplateIfAssignInterface_Object((1,3,6,1,4,1,9,9,218,1,2,2,1,1),_CifthTemplateIfAssignInterface_Type())
cifthTemplateIfAssignInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:cifthTemplateIfAssignInterface.setStatus(_A)
class _CifthTemplateIfAssignOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_CifthTemplateIfAssignOperStatus_Type.__name__=_E
_CifthTemplateIfAssignOperStatus_Object=MibTableColumn
cifthTemplateIfAssignOperStatus=_CifthTemplateIfAssignOperStatus_Object((1,3,6,1,4,1,9,9,218,1,2,2,1,2),_CifthTemplateIfAssignOperStatus_Type())
cifthTemplateIfAssignOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthTemplateIfAssignOperStatus.setStatus(_A)
_CifthTemplateIfAssignRowStatus_Type=RowStatus
_CifthTemplateIfAssignRowStatus_Object=MibTableColumn
cifthTemplateIfAssignRowStatus=_CifthTemplateIfAssignRowStatus_Object((1,3,6,1,4,1,9,9,218,1,2,2,1,3),_CifthTemplateIfAssignRowStatus_Type())
cifthTemplateIfAssignRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cifthTemplateIfAssignRowStatus.setStatus(_A)
_CifthIfThresholdFiredGroup_ObjectIdentity=ObjectIdentity
cifthIfThresholdFiredGroup=_CifthIfThresholdFiredGroup_ObjectIdentity((1,3,6,1,4,1,9,9,218,1,3))
_CifthThresholdFiredNotifyEnable_Type=CifthThresholdSeverityOrZero
_CifthThresholdFiredNotifyEnable_Object=MibScalar
cifthThresholdFiredNotifyEnable=_CifthThresholdFiredNotifyEnable_Object((1,3,6,1,4,1,9,9,218,1,3,1),_CifthThresholdFiredNotifyEnable_Type())
cifthThresholdFiredNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cifthThresholdFiredNotifyEnable.setStatus(_A)
_CifthThresholdFiredLastChange_Type=TimeStamp
_CifthThresholdFiredLastChange_Object=MibScalar
cifthThresholdFiredLastChange=_CifthThresholdFiredLastChange_Object((1,3,6,1,4,1,9,9,218,1,3,2),_CifthThresholdFiredLastChange_Type())
cifthThresholdFiredLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthThresholdFiredLastChange.setStatus(_A)
_CifthIfThresholdFiredTable_Object=MibTable
cifthIfThresholdFiredTable=_CifthIfThresholdFiredTable_Object((1,3,6,1,4,1,9,9,218,1,3,3))
if mibBuilder.loadTexts:cifthIfThresholdFiredTable.setStatus(_A)
_CifthIfThresholdFiredEntry_Object=MibTableRow
cifthIfThresholdFiredEntry=_CifthIfThresholdFiredEntry_Object((1,3,6,1,4,1,9,9,218,1,3,3,1))
cifthIfThresholdFiredEntry.setIndexNames((0,_N,_O),(0,_B,_S))
if mibBuilder.loadTexts:cifthIfThresholdFiredEntry.setStatus(_A)
_CifthIfThresholdFiredTemplate_Type=CifthTemplateIndex
_CifthIfThresholdFiredTemplate_Object=MibTableColumn
cifthIfThresholdFiredTemplate=_CifthIfThresholdFiredTemplate_Object((1,3,6,1,4,1,9,9,218,1,3,3,1,1),_CifthIfThresholdFiredTemplate_Type())
cifthIfThresholdFiredTemplate.setMaxAccess(_G)
if mibBuilder.loadTexts:cifthIfThresholdFiredTemplate.setStatus(_A)
_CifthIfThresholdsFired_Type=CifthThresholdList
_CifthIfThresholdsFired_Object=MibTableColumn
cifthIfThresholdsFired=_CifthIfThresholdsFired_Object((1,3,6,1,4,1,9,9,218,1,3,3,1,2),_CifthIfThresholdsFired_Type())
cifthIfThresholdsFired.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthIfThresholdsFired.setStatus(_A)
_CifthIfLastThresholdFired_Type=CifthThresholdIndex
_CifthIfLastThresholdFired_Object=MibTableColumn
cifthIfLastThresholdFired=_CifthIfLastThresholdFired_Object((1,3,6,1,4,1,9,9,218,1,3,3,1,3),_CifthIfLastThresholdFired_Type())
cifthIfLastThresholdFired.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthIfLastThresholdFired.setStatus(_A)
_CifthIfThresholdFiredLstChange_Type=TimeStamp
_CifthIfThresholdFiredLstChange_Object=MibTableColumn
cifthIfThresholdFiredLstChange=_CifthIfThresholdFiredLstChange_Object((1,3,6,1,4,1,9,9,218,1,3,3,1,4),_CifthIfThresholdFiredLstChange_Type())
cifthIfThresholdFiredLstChange.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthIfThresholdFiredLstChange.setStatus(_A)
_CifthIfThresholdFiredLstSeverity_Type=CifthThresholdSeverity
_CifthIfThresholdFiredLstSeverity_Object=MibTableColumn
cifthIfThresholdFiredLstSeverity=_CifthIfThresholdFiredLstSeverity_Object((1,3,6,1,4,1,9,9,218,1,3,3,1,5),_CifthIfThresholdFiredLstSeverity_Type())
cifthIfThresholdFiredLstSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthIfThresholdFiredLstSeverity.setStatus(_A)
_CifthIfThresholdFiredMaxSeverity_Type=CifthThresholdSeverity
_CifthIfThresholdFiredMaxSeverity_Object=MibTableColumn
cifthIfThresholdFiredMaxSeverity=_CifthIfThresholdFiredMaxSeverity_Object((1,3,6,1,4,1,9,9,218,1,3,3,1,6),_CifthIfThresholdFiredMaxSeverity_Type())
cifthIfThresholdFiredMaxSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:cifthIfThresholdFiredMaxSeverity.setStatus(_A)
_CIfThresholdMIBNotifications_ObjectIdentity=ObjectIdentity
cIfThresholdMIBNotifications=_CIfThresholdMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,218,2))
_CifthMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
cifthMIBNotificationsPrefix=_CifthMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,218,2,0))
_CIfThresholdMIBConformance_ObjectIdentity=ObjectIdentity
cIfThresholdMIBConformance=_CIfThresholdMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,218,3))
_CIfThresholdMIBCompliances_ObjectIdentity=ObjectIdentity
cIfThresholdMIBCompliances=_CIfThresholdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,218,3,1))
_CIfThresholdMIBGroups_ObjectIdentity=ObjectIdentity
cIfThresholdMIBGroups=_CIfThresholdMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,218,3,2))
cIfThresholdTemplateGroup=ObjectGroup((1,3,6,1,4,1,9,9,218,3,2,1))
cIfThresholdTemplateGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_M),(_B,_i)))
if mibBuilder.loadTexts:cIfThresholdTemplateGroup.setStatus(_A)
cIfThresholdFiredGroup=ObjectGroup((1,3,6,1,4,1,9,9,218,3,2,2))
cIfThresholdFiredGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_H),(_B,_I),(_B,_J),(_B,_m)))
if mibBuilder.loadTexts:cIfThresholdFiredGroup.setStatus(_A)
cifthHoldDownTimerGroup=ObjectGroup((1,3,6,1,4,1,9,9,218,3,2,3))
cifthHoldDownTimerGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:cifthHoldDownTimerGroup.setStatus(_A)
cifthHoldDownHysteresisGroup=ObjectGroup((1,3,6,1,4,1,9,9,218,3,2,4))
cifthHoldDownHysteresisGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:cifthHoldDownHysteresisGroup.setStatus(_A)
cifthApsGroup=ObjectGroup((1,3,6,1,4,1,9,9,218,3,2,5))
cifthApsGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:cifthApsGroup.setStatus(_A)
cifthIfThresholdFired=NotificationType((1,3,6,1,4,1,9,9,218,2,0,1))
cifthIfThresholdFired.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cifthIfThresholdFired.setStatus(_A)
cifthIfThresholdCleared=NotificationType((1,3,6,1,4,1,9,9,218,2,0,2))
cifthIfThresholdCleared.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:cifthIfThresholdCleared.setStatus(_A)
cifthTemplateIfStatusChange=NotificationType((1,3,6,1,4,1,9,9,218,2,0,3))
cifthTemplateIfStatusChange.setObjects((_B,_M))
if mibBuilder.loadTexts:cifthTemplateIfStatusChange.setStatus(_A)
cIfThresholdNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,218,3,2,6))
cIfThresholdNotifsGroup.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:cIfThresholdNotifsGroup.setStatus(_A)
cifthTemplateIfNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,218,3,2,7))
cifthTemplateIfNotifsGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:cifthTemplateIfNotifsGroup.setStatus(_A)
cIfThresholdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,218,3,1,1))
cIfThresholdMIBCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:cIfThresholdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CifthTemplateIndex':CifthTemplateIndex,'CifthTemplateIndexOrZero':CifthTemplateIndexOrZero,'CifthThresholdIndex':CifthThresholdIndex,'CifthThresholdList':CifthThresholdList,'CifthThresholdSeverity':CifthThresholdSeverity,'CifthThresholdSeverityOrZero':CifthThresholdSeverityOrZero,'ciscoIfThresholdMIB':ciscoIfThresholdMIB,'cIfThresholdMIBObjects':cIfThresholdMIBObjects,'cifthTemplateGroup':cifthTemplateGroup,_T:cifthTemplateIndexNext,_U:cifthTemplateLastChange,'cifthTemplateTable':cifthTemplateTable,'cifthTemplateEntry':cifthTemplateEntry,_F:cifthTemplateIndex,_V:cifthTemplateName,_W:cifthTemplateNotifyHoldDownType,_n:cifthTemplateNotifyHoldDownTime,_X:cifthTemplateRowStatus,_Y:cifthThresholdLastChange,'cifthThresholdTable':cifthThresholdTable,'cifthThresholdEntry':cifthThresholdEntry,_Q:cifthThresholdIndex,_Z:cifthThresholdDescr,_a:cifthThresholdObject,_b:cifthThresholdSeverity,_c:cifthThresholdType,_d:cifthThresholdDirection,_e:cifthThresholdFiredValue,_o:cifthThresholdClearedValue,_f:cifthThresholdSampleInterval,_p:cifthThresholdApsSwitchover,_g:cifthThresholdRowStatus,'cifthTemplateIfAssignGroup':cifthTemplateIfAssignGroup,_h:cifthTemplateIfLastChange,'cifthTemplateIfAssignTable':cifthTemplateIfAssignTable,'cifthTemplateIfAssignEntry':cifthTemplateIfAssignEntry,_R:cifthTemplateIfAssignInterface,_M:cifthTemplateIfAssignOperStatus,_i:cifthTemplateIfAssignRowStatus,'cifthIfThresholdFiredGroup':cifthIfThresholdFiredGroup,_j:cifthThresholdFiredNotifyEnable,_k:cifthThresholdFiredLastChange,'cifthIfThresholdFiredTable':cifthIfThresholdFiredTable,'cifthIfThresholdFiredEntry':cifthIfThresholdFiredEntry,_S:cifthIfThresholdFiredTemplate,_l:cifthIfThresholdsFired,_H:cifthIfLastThresholdFired,_I:cifthIfThresholdFiredLstChange,_J:cifthIfThresholdFiredLstSeverity,_m:cifthIfThresholdFiredMaxSeverity,'cIfThresholdMIBNotifications':cIfThresholdMIBNotifications,'cifthMIBNotificationsPrefix':cifthMIBNotificationsPrefix,_q:cifthIfThresholdFired,_r:cifthIfThresholdCleared,_s:cifthTemplateIfStatusChange,'cIfThresholdMIBConformance':cIfThresholdMIBConformance,'cIfThresholdMIBCompliances':cIfThresholdMIBCompliances,'cIfThresholdMIBCompliance':cIfThresholdMIBCompliance,'cIfThresholdMIBGroups':cIfThresholdMIBGroups,_t:cIfThresholdTemplateGroup,_u:cIfThresholdFiredGroup,'cifthHoldDownTimerGroup':cifthHoldDownTimerGroup,'cifthHoldDownHysteresisGroup':cifthHoldDownHysteresisGroup,'cifthApsGroup':cifthApsGroup,_v:cIfThresholdNotifsGroup,'cifthTemplateIfNotifsGroup':cifthTemplateIfNotifsGroup})