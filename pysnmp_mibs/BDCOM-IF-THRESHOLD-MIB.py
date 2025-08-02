_v='bdIfThresholdNotifsGroup'
_u='bdIfThresholdFiredGroup'
_t='bdIfThresholdTemplateGroup'
_s='bdifthTemplateIfStatusChange'
_r='bdifthIfThresholdCleared'
_q='bdifthIfThresholdFired'
_p='bdifthThresholdApsSwitchover'
_o='bdifthThresholdClearedValue'
_n='bdifthTemplateNotifyHoldDownTime'
_m='bdifthIfThresholdFiredMaxSeverity'
_l='bdifthIfThresholdsFired'
_k='bdifthThresholdFiredLastChange'
_j='bdifthThresholdFiredNotifyEnable'
_i='bdifthTemplateIfAssignRowStatus'
_h='bdifthTemplateIfLastChange'
_g='bdifthThresholdRowStatus'
_f='bdifthThresholdSampleInterval'
_e='bdifthThresholdFiredValue'
_d='bdifthThresholdDirection'
_c='bdifthThresholdType'
_b='bdifthThresholdSeverity'
_a='bdifthThresholdObject'
_Z='bdifthThresholdDescr'
_Y='bdifthThresholdLastChange'
_X='bdifthTemplateRowStatus'
_W='bdifthTemplateNotifyHoldDownType'
_V='bdifthTemplateName'
_U='bdifthTemplateLastChange'
_T='bdifthTemplateIndexNext'
_S='bdifthIfThresholdFiredTemplate'
_R='bdifthTemplateIfAssignInterface'
_Q='bdifthThresholdIndex'
_P='TruthValue'
_O='ifIndex'
_N='IF-MIB'
_M='bdifthTemplateIfAssignOperStatus'
_L='Unsigned32'
_K='SnmpAdminString'
_J='bdifthIfThresholdFiredLstSeverity'
_I='bdifthIfThresholdFiredLstChange'
_H='bdifthIfLastThresholdFired'
_G='not-accessible'
_F='bdifthTemplateIndex'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='BDCOM-IF-THRESHOLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bdMgmt,=mibBuilder.importSymbols('BDCOM-SMI','bdMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_N,'InterfaceIndex',_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_P)
bdcomIfThresholdMIB=ModuleIdentity((1,3,6,1,4,1,3320,9,218))
if mibBuilder.loadTexts:bdcomIfThresholdMIB.setRevisions(('2003-10-16 00:00',))
class BdifthTemplateIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
class BdifthTemplateIndexOrZero(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
class BdifthThresholdIndex(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
class BdifthThresholdList(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
class BdifthThresholdSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fail',1),('degrade',2),('info',3),('other',4)))
class BdifthThresholdSeverityOrZero(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_BdIfThresholdMIBObjects_ObjectIdentity=ObjectIdentity
bdIfThresholdMIBObjects=_BdIfThresholdMIBObjects_ObjectIdentity((1,3,6,1,4,1,3320,9,218,1))
_BdifthTemplateGroup_ObjectIdentity=ObjectIdentity
bdifthTemplateGroup=_BdifthTemplateGroup_ObjectIdentity((1,3,6,1,4,1,3320,9,218,1,1))
_BdifthTemplateIndexNext_Type=BdifthTemplateIndexOrZero
_BdifthTemplateIndexNext_Object=MibScalar
bdifthTemplateIndexNext=_BdifthTemplateIndexNext_Object((1,3,6,1,4,1,3320,9,218,1,1,1),_BdifthTemplateIndexNext_Type())
bdifthTemplateIndexNext.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthTemplateIndexNext.setStatus(_A)
_BdifthTemplateLastChange_Type=TimeStamp
_BdifthTemplateLastChange_Object=MibScalar
bdifthTemplateLastChange=_BdifthTemplateLastChange_Object((1,3,6,1,4,1,3320,9,218,1,1,2),_BdifthTemplateLastChange_Type())
bdifthTemplateLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthTemplateLastChange.setStatus(_A)
_BdifthTemplateTable_Object=MibTable
bdifthTemplateTable=_BdifthTemplateTable_Object((1,3,6,1,4,1,3320,9,218,1,1,3))
if mibBuilder.loadTexts:bdifthTemplateTable.setStatus(_A)
_BdifthTemplateEntry_Object=MibTableRow
bdifthTemplateEntry=_BdifthTemplateEntry_Object((1,3,6,1,4,1,3320,9,218,1,1,3,1))
bdifthTemplateEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:bdifthTemplateEntry.setStatus(_A)
_BdifthTemplateIndex_Type=BdifthTemplateIndex
_BdifthTemplateIndex_Object=MibTableColumn
bdifthTemplateIndex=_BdifthTemplateIndex_Object((1,3,6,1,4,1,3320,9,218,1,1,3,1,1),_BdifthTemplateIndex_Type())
bdifthTemplateIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bdifthTemplateIndex.setStatus(_A)
class _BdifthTemplateName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_BdifthTemplateName_Type.__name__=_K
_BdifthTemplateName_Object=MibTableColumn
bdifthTemplateName=_BdifthTemplateName_Object((1,3,6,1,4,1,3320,9,218,1,1,3,1,2),_BdifthTemplateName_Type())
bdifthTemplateName.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthTemplateName.setStatus(_A)
class _BdifthTemplateNotifyHoldDownType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('holdDownTimer',2),('fireAndClearThresholds',3)))
_BdifthTemplateNotifyHoldDownType_Type.__name__=_E
_BdifthTemplateNotifyHoldDownType_Object=MibTableColumn
bdifthTemplateNotifyHoldDownType=_BdifthTemplateNotifyHoldDownType_Object((1,3,6,1,4,1,3320,9,218,1,1,3,1,3),_BdifthTemplateNotifyHoldDownType_Type())
bdifthTemplateNotifyHoldDownType.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthTemplateNotifyHoldDownType.setStatus(_A)
class _BdifthTemplateNotifyHoldDownTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_BdifthTemplateNotifyHoldDownTime_Type.__name__=_L
_BdifthTemplateNotifyHoldDownTime_Object=MibTableColumn
bdifthTemplateNotifyHoldDownTime=_BdifthTemplateNotifyHoldDownTime_Object((1,3,6,1,4,1,3320,9,218,1,1,3,1,4),_BdifthTemplateNotifyHoldDownTime_Type())
bdifthTemplateNotifyHoldDownTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthTemplateNotifyHoldDownTime.setStatus(_A)
if mibBuilder.loadTexts:bdifthTemplateNotifyHoldDownTime.setUnits('seconds')
_BdifthTemplateRowStatus_Type=RowStatus
_BdifthTemplateRowStatus_Object=MibTableColumn
bdifthTemplateRowStatus=_BdifthTemplateRowStatus_Object((1,3,6,1,4,1,3320,9,218,1,1,3,1,5),_BdifthTemplateRowStatus_Type())
bdifthTemplateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthTemplateRowStatus.setStatus(_A)
_BdifthThresholdLastChange_Type=TimeStamp
_BdifthThresholdLastChange_Object=MibScalar
bdifthThresholdLastChange=_BdifthThresholdLastChange_Object((1,3,6,1,4,1,3320,9,218,1,1,4),_BdifthThresholdLastChange_Type())
bdifthThresholdLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthThresholdLastChange.setStatus(_A)
_BdifthThresholdTable_Object=MibTable
bdifthThresholdTable=_BdifthThresholdTable_Object((1,3,6,1,4,1,3320,9,218,1,1,5))
if mibBuilder.loadTexts:bdifthThresholdTable.setStatus(_A)
_BdifthThresholdEntry_Object=MibTableRow
bdifthThresholdEntry=_BdifthThresholdEntry_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1))
bdifthThresholdEntry.setIndexNames((0,_B,_F),(0,_B,_Q))
if mibBuilder.loadTexts:bdifthThresholdEntry.setStatus(_A)
_BdifthThresholdIndex_Type=BdifthThresholdIndex
_BdifthThresholdIndex_Object=MibTableColumn
bdifthThresholdIndex=_BdifthThresholdIndex_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,1),_BdifthThresholdIndex_Type())
bdifthThresholdIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bdifthThresholdIndex.setStatus(_A)
class _BdifthThresholdDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_BdifthThresholdDescr_Type.__name__=_K
_BdifthThresholdDescr_Object=MibTableColumn
bdifthThresholdDescr=_BdifthThresholdDescr_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,2),_BdifthThresholdDescr_Type())
bdifthThresholdDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdDescr.setStatus(_A)
_BdifthThresholdObject_Type=ObjectIdentifier
_BdifthThresholdObject_Object=MibTableColumn
bdifthThresholdObject=_BdifthThresholdObject_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,3),_BdifthThresholdObject_Type())
bdifthThresholdObject.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdObject.setStatus(_A)
_BdifthThresholdSeverity_Type=BdifthThresholdSeverity
_BdifthThresholdSeverity_Object=MibTableColumn
bdifthThresholdSeverity=_BdifthThresholdSeverity_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,4),_BdifthThresholdSeverity_Type())
bdifthThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdSeverity.setStatus(_A)
class _BdifthThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('rateOfIncreaseExponentXIfSpeed',3)))
_BdifthThresholdType_Type.__name__=_E
_BdifthThresholdType_Object=MibTableColumn
bdifthThresholdType=_BdifthThresholdType_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,5),_BdifthThresholdType_Type())
bdifthThresholdType.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdType.setStatus(_A)
class _BdifthThresholdDirection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rising',1),('falling',2)))
_BdifthThresholdDirection_Type.__name__=_E
_BdifthThresholdDirection_Object=MibTableColumn
bdifthThresholdDirection=_BdifthThresholdDirection_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,6),_BdifthThresholdDirection_Type())
bdifthThresholdDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdDirection.setStatus(_A)
class _BdifthThresholdFiredValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_BdifthThresholdFiredValue_Type.__name__=_E
_BdifthThresholdFiredValue_Object=MibTableColumn
bdifthThresholdFiredValue=_BdifthThresholdFiredValue_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,7),_BdifthThresholdFiredValue_Type())
bdifthThresholdFiredValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdFiredValue.setStatus(_A)
class _BdifthThresholdClearedValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_BdifthThresholdClearedValue_Type.__name__=_E
_BdifthThresholdClearedValue_Object=MibTableColumn
bdifthThresholdClearedValue=_BdifthThresholdClearedValue_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,8),_BdifthThresholdClearedValue_Type())
bdifthThresholdClearedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdClearedValue.setStatus(_A)
class _BdifthThresholdSampleInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,900000))
_BdifthThresholdSampleInterval_Type.__name__=_L
_BdifthThresholdSampleInterval_Object=MibTableColumn
bdifthThresholdSampleInterval=_BdifthThresholdSampleInterval_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,9),_BdifthThresholdSampleInterval_Type())
bdifthThresholdSampleInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdSampleInterval.setStatus(_A)
if mibBuilder.loadTexts:bdifthThresholdSampleInterval.setUnits('milliseconds')
class _BdifthThresholdApsSwitchover_Type(TruthValue):defaultValue=2
_BdifthThresholdApsSwitchover_Type.__name__=_P
_BdifthThresholdApsSwitchover_Object=MibTableColumn
bdifthThresholdApsSwitchover=_BdifthThresholdApsSwitchover_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,10),_BdifthThresholdApsSwitchover_Type())
bdifthThresholdApsSwitchover.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdApsSwitchover.setStatus(_A)
_BdifthThresholdRowStatus_Type=RowStatus
_BdifthThresholdRowStatus_Object=MibTableColumn
bdifthThresholdRowStatus=_BdifthThresholdRowStatus_Object((1,3,6,1,4,1,3320,9,218,1,1,5,1,11),_BdifthThresholdRowStatus_Type())
bdifthThresholdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthThresholdRowStatus.setStatus(_A)
_BdifthTemplateIfAssignGroup_ObjectIdentity=ObjectIdentity
bdifthTemplateIfAssignGroup=_BdifthTemplateIfAssignGroup_ObjectIdentity((1,3,6,1,4,1,3320,9,218,1,2))
_BdifthTemplateIfLastChange_Type=TimeStamp
_BdifthTemplateIfLastChange_Object=MibScalar
bdifthTemplateIfLastChange=_BdifthTemplateIfLastChange_Object((1,3,6,1,4,1,3320,9,218,1,2,1),_BdifthTemplateIfLastChange_Type())
bdifthTemplateIfLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthTemplateIfLastChange.setStatus(_A)
_BdifthTemplateIfAssignTable_Object=MibTable
bdifthTemplateIfAssignTable=_BdifthTemplateIfAssignTable_Object((1,3,6,1,4,1,3320,9,218,1,2,2))
if mibBuilder.loadTexts:bdifthTemplateIfAssignTable.setStatus(_A)
_BdifthTemplateIfAssignEntry_Object=MibTableRow
bdifthTemplateIfAssignEntry=_BdifthTemplateIfAssignEntry_Object((1,3,6,1,4,1,3320,9,218,1,2,2,1))
bdifthTemplateIfAssignEntry.setIndexNames((0,_B,_F),(0,_B,_R))
if mibBuilder.loadTexts:bdifthTemplateIfAssignEntry.setStatus(_A)
_BdifthTemplateIfAssignInterface_Type=InterfaceIndex
_BdifthTemplateIfAssignInterface_Object=MibTableColumn
bdifthTemplateIfAssignInterface=_BdifthTemplateIfAssignInterface_Object((1,3,6,1,4,1,3320,9,218,1,2,2,1,1),_BdifthTemplateIfAssignInterface_Type())
bdifthTemplateIfAssignInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:bdifthTemplateIfAssignInterface.setStatus(_A)
class _BdifthTemplateIfAssignOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_BdifthTemplateIfAssignOperStatus_Type.__name__=_E
_BdifthTemplateIfAssignOperStatus_Object=MibTableColumn
bdifthTemplateIfAssignOperStatus=_BdifthTemplateIfAssignOperStatus_Object((1,3,6,1,4,1,3320,9,218,1,2,2,1,2),_BdifthTemplateIfAssignOperStatus_Type())
bdifthTemplateIfAssignOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthTemplateIfAssignOperStatus.setStatus(_A)
_BdifthTemplateIfAssignRowStatus_Type=RowStatus
_BdifthTemplateIfAssignRowStatus_Object=MibTableColumn
bdifthTemplateIfAssignRowStatus=_BdifthTemplateIfAssignRowStatus_Object((1,3,6,1,4,1,3320,9,218,1,2,2,1,3),_BdifthTemplateIfAssignRowStatus_Type())
bdifthTemplateIfAssignRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bdifthTemplateIfAssignRowStatus.setStatus(_A)
_BdifthIfThresholdFiredGroup_ObjectIdentity=ObjectIdentity
bdifthIfThresholdFiredGroup=_BdifthIfThresholdFiredGroup_ObjectIdentity((1,3,6,1,4,1,3320,9,218,1,3))
_BdifthThresholdFiredNotifyEnable_Type=BdifthThresholdSeverityOrZero
_BdifthThresholdFiredNotifyEnable_Object=MibScalar
bdifthThresholdFiredNotifyEnable=_BdifthThresholdFiredNotifyEnable_Object((1,3,6,1,4,1,3320,9,218,1,3,1),_BdifthThresholdFiredNotifyEnable_Type())
bdifthThresholdFiredNotifyEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:bdifthThresholdFiredNotifyEnable.setStatus(_A)
_BdifthThresholdFiredLastChange_Type=TimeStamp
_BdifthThresholdFiredLastChange_Object=MibScalar
bdifthThresholdFiredLastChange=_BdifthThresholdFiredLastChange_Object((1,3,6,1,4,1,3320,9,218,1,3,2),_BdifthThresholdFiredLastChange_Type())
bdifthThresholdFiredLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthThresholdFiredLastChange.setStatus(_A)
_BdifthIfThresholdFiredTable_Object=MibTable
bdifthIfThresholdFiredTable=_BdifthIfThresholdFiredTable_Object((1,3,6,1,4,1,3320,9,218,1,3,3))
if mibBuilder.loadTexts:bdifthIfThresholdFiredTable.setStatus(_A)
_BdifthIfThresholdFiredEntry_Object=MibTableRow
bdifthIfThresholdFiredEntry=_BdifthIfThresholdFiredEntry_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1))
bdifthIfThresholdFiredEntry.setIndexNames((0,_N,_O),(0,_B,_S))
if mibBuilder.loadTexts:bdifthIfThresholdFiredEntry.setStatus(_A)
_BdifthIfThresholdFiredTemplate_Type=BdifthTemplateIndex
_BdifthIfThresholdFiredTemplate_Object=MibTableColumn
bdifthIfThresholdFiredTemplate=_BdifthIfThresholdFiredTemplate_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1,1),_BdifthIfThresholdFiredTemplate_Type())
bdifthIfThresholdFiredTemplate.setMaxAccess(_G)
if mibBuilder.loadTexts:bdifthIfThresholdFiredTemplate.setStatus(_A)
_BdifthIfThresholdsFired_Type=BdifthThresholdList
_BdifthIfThresholdsFired_Object=MibTableColumn
bdifthIfThresholdsFired=_BdifthIfThresholdsFired_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1,2),_BdifthIfThresholdsFired_Type())
bdifthIfThresholdsFired.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthIfThresholdsFired.setStatus(_A)
_BdifthIfLastThresholdFired_Type=BdifthThresholdIndex
_BdifthIfLastThresholdFired_Object=MibTableColumn
bdifthIfLastThresholdFired=_BdifthIfLastThresholdFired_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1,3),_BdifthIfLastThresholdFired_Type())
bdifthIfLastThresholdFired.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthIfLastThresholdFired.setStatus(_A)
_BdifthIfThresholdFiredLstChange_Type=TimeStamp
_BdifthIfThresholdFiredLstChange_Object=MibTableColumn
bdifthIfThresholdFiredLstChange=_BdifthIfThresholdFiredLstChange_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1,4),_BdifthIfThresholdFiredLstChange_Type())
bdifthIfThresholdFiredLstChange.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthIfThresholdFiredLstChange.setStatus(_A)
_BdifthIfThresholdFiredLstSeverity_Type=BdifthThresholdSeverity
_BdifthIfThresholdFiredLstSeverity_Object=MibTableColumn
bdifthIfThresholdFiredLstSeverity=_BdifthIfThresholdFiredLstSeverity_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1,5),_BdifthIfThresholdFiredLstSeverity_Type())
bdifthIfThresholdFiredLstSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthIfThresholdFiredLstSeverity.setStatus(_A)
_BdifthIfThresholdFiredMaxSeverity_Type=BdifthThresholdSeverity
_BdifthIfThresholdFiredMaxSeverity_Object=MibTableColumn
bdifthIfThresholdFiredMaxSeverity=_BdifthIfThresholdFiredMaxSeverity_Object((1,3,6,1,4,1,3320,9,218,1,3,3,1,6),_BdifthIfThresholdFiredMaxSeverity_Type())
bdifthIfThresholdFiredMaxSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:bdifthIfThresholdFiredMaxSeverity.setStatus(_A)
_BdIfThresholdMIBNotifications_ObjectIdentity=ObjectIdentity
bdIfThresholdMIBNotifications=_BdIfThresholdMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3320,9,218,2))
_BdifthMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
bdifthMIBNotificationsPrefix=_BdifthMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3320,9,218,2,0))
_BdIfThresholdMIBConformance_ObjectIdentity=ObjectIdentity
bdIfThresholdMIBConformance=_BdIfThresholdMIBConformance_ObjectIdentity((1,3,6,1,4,1,3320,9,218,3))
_BdIfThresholdMIBCompliances_ObjectIdentity=ObjectIdentity
bdIfThresholdMIBCompliances=_BdIfThresholdMIBCompliances_ObjectIdentity((1,3,6,1,4,1,3320,9,218,3,1))
_BdIfThresholdMIBGroups_ObjectIdentity=ObjectIdentity
bdIfThresholdMIBGroups=_BdIfThresholdMIBGroups_ObjectIdentity((1,3,6,1,4,1,3320,9,218,3,2))
bdIfThresholdTemplateGroup=ObjectGroup((1,3,6,1,4,1,3320,9,218,3,2,1))
bdIfThresholdTemplateGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_M),(_B,_i)))
if mibBuilder.loadTexts:bdIfThresholdTemplateGroup.setStatus(_A)
bdIfThresholdFiredGroup=ObjectGroup((1,3,6,1,4,1,3320,9,218,3,2,2))
bdIfThresholdFiredGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_H),(_B,_I),(_B,_J),(_B,_m)))
if mibBuilder.loadTexts:bdIfThresholdFiredGroup.setStatus(_A)
bdifthHoldDownTimerGroup=ObjectGroup((1,3,6,1,4,1,3320,9,218,3,2,3))
bdifthHoldDownTimerGroup.setObjects((_B,_n))
if mibBuilder.loadTexts:bdifthHoldDownTimerGroup.setStatus(_A)
bdifthHoldDownHysteresisGroup=ObjectGroup((1,3,6,1,4,1,3320,9,218,3,2,4))
bdifthHoldDownHysteresisGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:bdifthHoldDownHysteresisGroup.setStatus(_A)
bdifthApsGroup=ObjectGroup((1,3,6,1,4,1,3320,9,218,3,2,5))
bdifthApsGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:bdifthApsGroup.setStatus(_A)
bdifthIfThresholdFired=NotificationType((1,3,6,1,4,1,3320,9,218,2,0,1))
bdifthIfThresholdFired.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:bdifthIfThresholdFired.setStatus(_A)
bdifthIfThresholdCleared=NotificationType((1,3,6,1,4,1,3320,9,218,2,0,2))
bdifthIfThresholdCleared.setObjects(*((_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:bdifthIfThresholdCleared.setStatus(_A)
bdifthTemplateIfStatusChange=NotificationType((1,3,6,1,4,1,3320,9,218,2,0,3))
bdifthTemplateIfStatusChange.setObjects((_B,_M))
if mibBuilder.loadTexts:bdifthTemplateIfStatusChange.setStatus(_A)
bdIfThresholdNotifsGroup=NotificationGroup((1,3,6,1,4,1,3320,9,218,3,2,6))
bdIfThresholdNotifsGroup.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:bdIfThresholdNotifsGroup.setStatus(_A)
bdifthTemplateIfNotifsGroup=NotificationGroup((1,3,6,1,4,1,3320,9,218,3,2,7))
bdifthTemplateIfNotifsGroup.setObjects((_B,_s))
if mibBuilder.loadTexts:bdifthTemplateIfNotifsGroup.setStatus(_A)
bdIfThresholdMIBCompliance=ModuleCompliance((1,3,6,1,4,1,3320,9,218,3,1,1))
bdIfThresholdMIBCompliance.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:bdIfThresholdMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'BdifthTemplateIndex':BdifthTemplateIndex,'BdifthTemplateIndexOrZero':BdifthTemplateIndexOrZero,'BdifthThresholdIndex':BdifthThresholdIndex,'BdifthThresholdList':BdifthThresholdList,'BdifthThresholdSeverity':BdifthThresholdSeverity,'BdifthThresholdSeverityOrZero':BdifthThresholdSeverityOrZero,'bdcomIfThresholdMIB':bdcomIfThresholdMIB,'bdIfThresholdMIBObjects':bdIfThresholdMIBObjects,'bdifthTemplateGroup':bdifthTemplateGroup,_T:bdifthTemplateIndexNext,_U:bdifthTemplateLastChange,'bdifthTemplateTable':bdifthTemplateTable,'bdifthTemplateEntry':bdifthTemplateEntry,_F:bdifthTemplateIndex,_V:bdifthTemplateName,_W:bdifthTemplateNotifyHoldDownType,_n:bdifthTemplateNotifyHoldDownTime,_X:bdifthTemplateRowStatus,_Y:bdifthThresholdLastChange,'bdifthThresholdTable':bdifthThresholdTable,'bdifthThresholdEntry':bdifthThresholdEntry,_Q:bdifthThresholdIndex,_Z:bdifthThresholdDescr,_a:bdifthThresholdObject,_b:bdifthThresholdSeverity,_c:bdifthThresholdType,_d:bdifthThresholdDirection,_e:bdifthThresholdFiredValue,_o:bdifthThresholdClearedValue,_f:bdifthThresholdSampleInterval,_p:bdifthThresholdApsSwitchover,_g:bdifthThresholdRowStatus,'bdifthTemplateIfAssignGroup':bdifthTemplateIfAssignGroup,_h:bdifthTemplateIfLastChange,'bdifthTemplateIfAssignTable':bdifthTemplateIfAssignTable,'bdifthTemplateIfAssignEntry':bdifthTemplateIfAssignEntry,_R:bdifthTemplateIfAssignInterface,_M:bdifthTemplateIfAssignOperStatus,_i:bdifthTemplateIfAssignRowStatus,'bdifthIfThresholdFiredGroup':bdifthIfThresholdFiredGroup,_j:bdifthThresholdFiredNotifyEnable,_k:bdifthThresholdFiredLastChange,'bdifthIfThresholdFiredTable':bdifthIfThresholdFiredTable,'bdifthIfThresholdFiredEntry':bdifthIfThresholdFiredEntry,_S:bdifthIfThresholdFiredTemplate,_l:bdifthIfThresholdsFired,_H:bdifthIfLastThresholdFired,_I:bdifthIfThresholdFiredLstChange,_J:bdifthIfThresholdFiredLstSeverity,_m:bdifthIfThresholdFiredMaxSeverity,'bdIfThresholdMIBNotifications':bdIfThresholdMIBNotifications,'bdifthMIBNotificationsPrefix':bdifthMIBNotificationsPrefix,_q:bdifthIfThresholdFired,_r:bdifthIfThresholdCleared,_s:bdifthTemplateIfStatusChange,'bdIfThresholdMIBConformance':bdIfThresholdMIBConformance,'bdIfThresholdMIBCompliances':bdIfThresholdMIBCompliances,'bdIfThresholdMIBCompliance':bdIfThresholdMIBCompliance,'bdIfThresholdMIBGroups':bdIfThresholdMIBGroups,_t:bdIfThresholdTemplateGroup,_u:bdIfThresholdFiredGroup,'bdifthHoldDownTimerGroup':bdifthHoldDownTimerGroup,'bdifthHoldDownHysteresisGroup':bdifthHoldDownHysteresisGroup,'bdifthApsGroup':bdifthApsGroup,_v:bdIfThresholdNotifsGroup,'bdifthTemplateIfNotifsGroup':bdifthTemplateIfNotifsGroup})