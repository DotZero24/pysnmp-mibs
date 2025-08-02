_W='safAlarmNotificationsGroup'
_V='safAlarmActiveGroup'
_U='safAlarmClearState'
_T='safAlarmActiveTState'
_S='safAlarmActiveState'
_R='deprecated'
_Q='safAlarmActiveLastChangedDateAndTime'
_P='safAlarmActiveLastChanged'
_O='safAlarmActiveIndex'
_N='Unsigned32'
_M='safAlarmActiveThresholdTValue'
_L='safAlarmActiveThresholdTTriggered'
_K='safAlarmActiveThresholdValue'
_J='safAlarmActiveThresholdTriggered'
_I='safAlarmActiveAdditionalText'
_H='safAlarmActivePerceivedSeverity'
_G='safAlarmActiveProbableCause'
_F='safAlarmActiveEventType'
_E='safAlarmActiveDateAndTime'
_D='safAlarmActiveManagedObj'
_C='read-only'
_B='current'
_A='SAF-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAItuEventType,IANAItuProbableCause=mibBuilder.importSymbols('IANA-ITU-ALARM-TC-MIB','IANAItuEventType','IANAItuProbableCause')
tehnika,=mibBuilder.importSymbols('SAF-ENTERPRISE','tehnika')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
safAlarmMIB=ModuleIdentity((1,3,6,1,4,1,7571,100,118))
if mibBuilder.loadTexts:safAlarmMIB.setRevisions(('2016-03-03 00:00','2014-07-03 00:00','2014-07-01 00:00','2008-09-17 00:00','2007-05-10 00:00'))
class SafPerceivedSeverity(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cleared',1),('indeterminate',2),('critical',3),('major',4),('minor',5),('warning',6),('event',7)))
_SafAlarmNotifications_ObjectIdentity=ObjectIdentity
safAlarmNotifications=_SafAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,7571,100,118,0))
_SafAlarmObjects_ObjectIdentity=ObjectIdentity
safAlarmObjects=_SafAlarmObjects_ObjectIdentity((1,3,6,1,4,1,7571,100,118,1))
_SafAlarmActive_ObjectIdentity=ObjectIdentity
safAlarmActive=_SafAlarmActive_ObjectIdentity((1,3,6,1,4,1,7571,100,118,1,1))
_SafAlarmActiveLastChanged_Type=TimeTicks
_SafAlarmActiveLastChanged_Object=MibScalar
safAlarmActiveLastChanged=_SafAlarmActiveLastChanged_Object((1,3,6,1,4,1,7571,100,118,1,1,1),_SafAlarmActiveLastChanged_Type())
safAlarmActiveLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveLastChanged.setStatus(_B)
_SafAlarmActiveTable_Object=MibTable
safAlarmActiveTable=_SafAlarmActiveTable_Object((1,3,6,1,4,1,7571,100,118,1,1,2))
if mibBuilder.loadTexts:safAlarmActiveTable.setStatus(_B)
_SafAlarmActiveEntry_Object=MibTableRow
safAlarmActiveEntry=_SafAlarmActiveEntry_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1))
safAlarmActiveEntry.setIndexNames((0,_A,_O))
if mibBuilder.loadTexts:safAlarmActiveEntry.setStatus(_B)
class _SafAlarmActiveIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_SafAlarmActiveIndex_Type.__name__=_N
_SafAlarmActiveIndex_Object=MibTableColumn
safAlarmActiveIndex=_SafAlarmActiveIndex_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,1),_SafAlarmActiveIndex_Type())
safAlarmActiveIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:safAlarmActiveIndex.setStatus(_B)
_SafAlarmActiveManagedObj_Type=ObjectIdentifier
_SafAlarmActiveManagedObj_Object=MibTableColumn
safAlarmActiveManagedObj=_SafAlarmActiveManagedObj_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,2),_SafAlarmActiveManagedObj_Type())
safAlarmActiveManagedObj.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveManagedObj.setStatus(_B)
_SafAlarmActiveDateAndTime_Type=DateAndTime
_SafAlarmActiveDateAndTime_Object=MibTableColumn
safAlarmActiveDateAndTime=_SafAlarmActiveDateAndTime_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,3),_SafAlarmActiveDateAndTime_Type())
safAlarmActiveDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveDateAndTime.setStatus(_B)
_SafAlarmActiveEventType_Type=IANAItuEventType
_SafAlarmActiveEventType_Object=MibTableColumn
safAlarmActiveEventType=_SafAlarmActiveEventType_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,4),_SafAlarmActiveEventType_Type())
safAlarmActiveEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveEventType.setStatus(_B)
_SafAlarmActiveProbableCause_Type=IANAItuProbableCause
_SafAlarmActiveProbableCause_Object=MibTableColumn
safAlarmActiveProbableCause=_SafAlarmActiveProbableCause_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,5),_SafAlarmActiveProbableCause_Type())
safAlarmActiveProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveProbableCause.setStatus(_B)
_SafAlarmActivePerceivedSeverity_Type=SafPerceivedSeverity
_SafAlarmActivePerceivedSeverity_Object=MibTableColumn
safAlarmActivePerceivedSeverity=_SafAlarmActivePerceivedSeverity_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,6),_SafAlarmActivePerceivedSeverity_Type())
safAlarmActivePerceivedSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActivePerceivedSeverity.setStatus(_B)
_SafAlarmActiveThresholdTriggered_Type=Integer32
_SafAlarmActiveThresholdTriggered_Object=MibTableColumn
safAlarmActiveThresholdTriggered=_SafAlarmActiveThresholdTriggered_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,7),_SafAlarmActiveThresholdTriggered_Type())
safAlarmActiveThresholdTriggered.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveThresholdTriggered.setStatus(_B)
_SafAlarmActiveThresholdValue_Type=Integer32
_SafAlarmActiveThresholdValue_Object=MibTableColumn
safAlarmActiveThresholdValue=_SafAlarmActiveThresholdValue_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,8),_SafAlarmActiveThresholdValue_Type())
safAlarmActiveThresholdValue.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveThresholdValue.setStatus(_B)
_SafAlarmActiveThresholdTTriggered_Type=DisplayString
_SafAlarmActiveThresholdTTriggered_Object=MibTableColumn
safAlarmActiveThresholdTTriggered=_SafAlarmActiveThresholdTTriggered_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,9),_SafAlarmActiveThresholdTTriggered_Type())
safAlarmActiveThresholdTTriggered.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveThresholdTTriggered.setStatus(_B)
_SafAlarmActiveThresholdTValue_Type=DisplayString
_SafAlarmActiveThresholdTValue_Object=MibTableColumn
safAlarmActiveThresholdTValue=_SafAlarmActiveThresholdTValue_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,10),_SafAlarmActiveThresholdTValue_Type())
safAlarmActiveThresholdTValue.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveThresholdTValue.setStatus(_B)
_SafAlarmActiveAdditionalText_Type=SnmpAdminString
_SafAlarmActiveAdditionalText_Object=MibTableColumn
safAlarmActiveAdditionalText=_SafAlarmActiveAdditionalText_Object((1,3,6,1,4,1,7571,100,118,1,1,2,1,11),_SafAlarmActiveAdditionalText_Type())
safAlarmActiveAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveAdditionalText.setStatus(_B)
_SafAlarmActiveLastChangedDateAndTime_Type=DateAndTime
_SafAlarmActiveLastChangedDateAndTime_Object=MibScalar
safAlarmActiveLastChangedDateAndTime=_SafAlarmActiveLastChangedDateAndTime_Object((1,3,6,1,4,1,7571,100,118,1,1,3),_SafAlarmActiveLastChangedDateAndTime_Type())
safAlarmActiveLastChangedDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:safAlarmActiveLastChangedDateAndTime.setStatus(_B)
_SafAlarmConformance_ObjectIdentity=ObjectIdentity
safAlarmConformance=_SafAlarmConformance_ObjectIdentity((1,3,6,1,4,1,7571,100,118,3))
_SafAlarmCompliances_ObjectIdentity=ObjectIdentity
safAlarmCompliances=_SafAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,7571,100,118,3,1))
_SafAlarmGroups_ObjectIdentity=ObjectIdentity
safAlarmGroups=_SafAlarmGroups_ObjectIdentity((1,3,6,1,4,1,7571,100,118,3,2))
safAlarmActiveGroup=ObjectGroup((1,3,6,1,4,1,7571,100,118,3,2,1))
safAlarmActiveGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_I)))
if mibBuilder.loadTexts:safAlarmActiveGroup.setStatus(_B)
safAlarmActiveState=NotificationType((1,3,6,1,4,1,7571,100,118,0,2))
safAlarmActiveState.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_J),(_A,_K),(_A,_I)))
if mibBuilder.loadTexts:safAlarmActiveState.setStatus(_B)
safAlarmActiveTState=NotificationType((1,3,6,1,4,1,7571,100,118,0,3))
safAlarmActiveTState.setObjects(*((_A,_D),(_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_I)))
if mibBuilder.loadTexts:safAlarmActiveTState.setStatus(_B)
safAlarmClearState=NotificationType((1,3,6,1,4,1,7571,100,118,0,4))
safAlarmClearState.setObjects((_A,_D))
if mibBuilder.loadTexts:safAlarmClearState.setStatus(_R)
safAlarmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,7571,100,118,3,2,2))
safAlarmNotificationsGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:safAlarmNotificationsGroup.setStatus(_R)
safAlarmCompliance=ModuleCompliance((1,3,6,1,4,1,7571,100,118,3,1,1))
safAlarmCompliance.setObjects(*((_A,_V),(_A,_W)))
if mibBuilder.loadTexts:safAlarmCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SafPerceivedSeverity':SafPerceivedSeverity,'safAlarmMIB':safAlarmMIB,'safAlarmNotifications':safAlarmNotifications,_S:safAlarmActiveState,_T:safAlarmActiveTState,_U:safAlarmClearState,'safAlarmObjects':safAlarmObjects,'safAlarmActive':safAlarmActive,_P:safAlarmActiveLastChanged,'safAlarmActiveTable':safAlarmActiveTable,'safAlarmActiveEntry':safAlarmActiveEntry,_O:safAlarmActiveIndex,_D:safAlarmActiveManagedObj,_E:safAlarmActiveDateAndTime,_F:safAlarmActiveEventType,_G:safAlarmActiveProbableCause,_H:safAlarmActivePerceivedSeverity,_J:safAlarmActiveThresholdTriggered,_K:safAlarmActiveThresholdValue,_L:safAlarmActiveThresholdTTriggered,_M:safAlarmActiveThresholdTValue,_I:safAlarmActiveAdditionalText,_Q:safAlarmActiveLastChangedDateAndTime,'safAlarmConformance':safAlarmConformance,'safAlarmCompliances':safAlarmCompliances,'safAlarmCompliance':safAlarmCompliance,'safAlarmGroups':safAlarmGroups,_V:safAlarmActiveGroup,_W:safAlarmNotificationsGroup})