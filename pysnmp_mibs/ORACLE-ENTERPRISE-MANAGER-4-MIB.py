_g='oraEM4JobAlertSeverity'
_f='oraEM4JobAlertKeyValue'
_e='oraEM4JobAlertKeyName'
_d='oraEM4JobAlertContext'
_c='oraEM4JobAlertMetricValue'
_b='oraEM4JobAlertMetricName'
_a='oraEM4JobAlertRuleOwner'
_Z='oraEM4JobAlertRuleName'
_Y='oraEM4JobAlertTimeStamp'
_X='oraEM4JobAlertTargets'
_W='oraEM4JobAlertJobStatus'
_V='oraEM4JobAlertJobType'
_U='oraEM4JobAlertJobOwner'
_T='oraEM4JobAlertJobName'
_S='oraEM4AlertContext'
_R='oraEM4AlertMetricValue'
_Q='oraEM4AlertRuleOwner'
_P='oraEM4AlertRuleName'
_O='oraEM4AlertMessage'
_N='oraEM4AlertSeverity'
_M='oraEM4AlertTimeStamp'
_L='oraEM4AlertKeyValue'
_K='oraEM4AlertKeyName'
_J='oraEM4AlertMetricName'
_I='oraEM4AlertHostName'
_H='oraEM4AlertTargetType'
_G='oraEM4AlertTargetName'
_F='oraEM4JobAlertIndex'
_E='oraEM4AlertIndex'
_D='NotificationType'
_C='read-only'
_B='ORACLE-ENTERPRISE-MANAGER-4-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_D,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_D,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Oracle_ObjectIdentity=ObjectIdentity
oracle=_Oracle_ObjectIdentity((1,3,6,1,4,1,111))
_OraEM4_ObjectIdentity=ObjectIdentity
oraEM4=_OraEM4_ObjectIdentity((1,3,6,1,4,1,111,15))
_OraEM4Objects_ObjectIdentity=ObjectIdentity
oraEM4Objects=_OraEM4Objects_ObjectIdentity((1,3,6,1,4,1,111,15,1))
_OraEM4AlertTable_Object=MibTable
oraEM4AlertTable=_OraEM4AlertTable_Object((1,3,6,1,4,1,111,15,1,1))
if mibBuilder.loadTexts:oraEM4AlertTable.setStatus(_A)
_OraEM4AlertEntry_Object=MibTableRow
oraEM4AlertEntry=_OraEM4AlertEntry_Object((1,3,6,1,4,1,111,15,1,1,1))
oraEM4AlertEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:oraEM4AlertEntry.setStatus(_A)
_OraEM4AlertIndex_Type=Integer32
_OraEM4AlertIndex_Object=MibTableColumn
oraEM4AlertIndex=_OraEM4AlertIndex_Object((1,3,6,1,4,1,111,15,1,1,1,1),_OraEM4AlertIndex_Type())
oraEM4AlertIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertIndex.setStatus(_A)
_OraEM4AlertTargetName_Type=DisplayString
_OraEM4AlertTargetName_Object=MibTableColumn
oraEM4AlertTargetName=_OraEM4AlertTargetName_Object((1,3,6,1,4,1,111,15,1,1,1,2),_OraEM4AlertTargetName_Type())
oraEM4AlertTargetName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertTargetName.setStatus(_A)
_OraEM4AlertTargetType_Type=DisplayString
_OraEM4AlertTargetType_Object=MibTableColumn
oraEM4AlertTargetType=_OraEM4AlertTargetType_Object((1,3,6,1,4,1,111,15,1,1,1,3),_OraEM4AlertTargetType_Type())
oraEM4AlertTargetType.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertTargetType.setStatus(_A)
_OraEM4AlertHostName_Type=DisplayString
_OraEM4AlertHostName_Object=MibTableColumn
oraEM4AlertHostName=_OraEM4AlertHostName_Object((1,3,6,1,4,1,111,15,1,1,1,4),_OraEM4AlertHostName_Type())
oraEM4AlertHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertHostName.setStatus(_A)
_OraEM4AlertMetricName_Type=DisplayString
_OraEM4AlertMetricName_Object=MibTableColumn
oraEM4AlertMetricName=_OraEM4AlertMetricName_Object((1,3,6,1,4,1,111,15,1,1,1,5),_OraEM4AlertMetricName_Type())
oraEM4AlertMetricName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertMetricName.setStatus(_A)
_OraEM4AlertKeyName_Type=DisplayString
_OraEM4AlertKeyName_Object=MibTableColumn
oraEM4AlertKeyName=_OraEM4AlertKeyName_Object((1,3,6,1,4,1,111,15,1,1,1,6),_OraEM4AlertKeyName_Type())
oraEM4AlertKeyName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertKeyName.setStatus(_A)
_OraEM4AlertKeyValue_Type=DisplayString
_OraEM4AlertKeyValue_Object=MibTableColumn
oraEM4AlertKeyValue=_OraEM4AlertKeyValue_Object((1,3,6,1,4,1,111,15,1,1,1,7),_OraEM4AlertKeyValue_Type())
oraEM4AlertKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertKeyValue.setStatus(_A)
_OraEM4AlertTimeStamp_Type=DisplayString
_OraEM4AlertTimeStamp_Object=MibTableColumn
oraEM4AlertTimeStamp=_OraEM4AlertTimeStamp_Object((1,3,6,1,4,1,111,15,1,1,1,8),_OraEM4AlertTimeStamp_Type())
oraEM4AlertTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertTimeStamp.setStatus(_A)
_OraEM4AlertSeverity_Type=DisplayString
_OraEM4AlertSeverity_Object=MibTableColumn
oraEM4AlertSeverity=_OraEM4AlertSeverity_Object((1,3,6,1,4,1,111,15,1,1,1,9),_OraEM4AlertSeverity_Type())
oraEM4AlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertSeverity.setStatus(_A)
_OraEM4AlertMessage_Type=DisplayString
_OraEM4AlertMessage_Object=MibTableColumn
oraEM4AlertMessage=_OraEM4AlertMessage_Object((1,3,6,1,4,1,111,15,1,1,1,10),_OraEM4AlertMessage_Type())
oraEM4AlertMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertMessage.setStatus(_A)
_OraEM4AlertRuleName_Type=DisplayString
_OraEM4AlertRuleName_Object=MibTableColumn
oraEM4AlertRuleName=_OraEM4AlertRuleName_Object((1,3,6,1,4,1,111,15,1,1,1,11),_OraEM4AlertRuleName_Type())
oraEM4AlertRuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertRuleName.setStatus(_A)
_OraEM4AlertRuleOwner_Type=DisplayString
_OraEM4AlertRuleOwner_Object=MibTableColumn
oraEM4AlertRuleOwner=_OraEM4AlertRuleOwner_Object((1,3,6,1,4,1,111,15,1,1,1,12),_OraEM4AlertRuleOwner_Type())
oraEM4AlertRuleOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertRuleOwner.setStatus(_A)
_OraEM4AlertMetricValue_Type=DisplayString
_OraEM4AlertMetricValue_Object=MibTableColumn
oraEM4AlertMetricValue=_OraEM4AlertMetricValue_Object((1,3,6,1,4,1,111,15,1,1,1,13),_OraEM4AlertMetricValue_Type())
oraEM4AlertMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertMetricValue.setStatus(_A)
_OraEM4AlertContext_Type=DisplayString
_OraEM4AlertContext_Object=MibTableColumn
oraEM4AlertContext=_OraEM4AlertContext_Object((1,3,6,1,4,1,111,15,1,1,1,14),_OraEM4AlertContext_Type())
oraEM4AlertContext.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4AlertContext.setStatus(_A)
_OraEM4JobAlertTable_Object=MibTable
oraEM4JobAlertTable=_OraEM4JobAlertTable_Object((1,3,6,1,4,1,111,15,1,2))
if mibBuilder.loadTexts:oraEM4JobAlertTable.setStatus(_A)
_OraEM4JobAlertEntry_Object=MibTableRow
oraEM4JobAlertEntry=_OraEM4JobAlertEntry_Object((1,3,6,1,4,1,111,15,1,2,1))
oraEM4JobAlertEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:oraEM4JobAlertEntry.setStatus(_A)
_OraEM4JobAlertIndex_Type=Integer32
_OraEM4JobAlertIndex_Object=MibTableColumn
oraEM4JobAlertIndex=_OraEM4JobAlertIndex_Object((1,3,6,1,4,1,111,15,1,2,1,1),_OraEM4JobAlertIndex_Type())
oraEM4JobAlertIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertIndex.setStatus(_A)
_OraEM4JobAlertJobName_Type=DisplayString
_OraEM4JobAlertJobName_Object=MibTableColumn
oraEM4JobAlertJobName=_OraEM4JobAlertJobName_Object((1,3,6,1,4,1,111,15,1,2,1,2),_OraEM4JobAlertJobName_Type())
oraEM4JobAlertJobName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertJobName.setStatus(_A)
_OraEM4JobAlertJobOwner_Type=DisplayString
_OraEM4JobAlertJobOwner_Object=MibTableColumn
oraEM4JobAlertJobOwner=_OraEM4JobAlertJobOwner_Object((1,3,6,1,4,1,111,15,1,2,1,3),_OraEM4JobAlertJobOwner_Type())
oraEM4JobAlertJobOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertJobOwner.setStatus(_A)
_OraEM4JobAlertJobType_Type=DisplayString
_OraEM4JobAlertJobType_Object=MibTableColumn
oraEM4JobAlertJobType=_OraEM4JobAlertJobType_Object((1,3,6,1,4,1,111,15,1,2,1,4),_OraEM4JobAlertJobType_Type())
oraEM4JobAlertJobType.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertJobType.setStatus(_A)
_OraEM4JobAlertJobStatus_Type=DisplayString
_OraEM4JobAlertJobStatus_Object=MibTableColumn
oraEM4JobAlertJobStatus=_OraEM4JobAlertJobStatus_Object((1,3,6,1,4,1,111,15,1,2,1,5),_OraEM4JobAlertJobStatus_Type())
oraEM4JobAlertJobStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertJobStatus.setStatus(_A)
_OraEM4JobAlertTargets_Type=DisplayString
_OraEM4JobAlertTargets_Object=MibTableColumn
oraEM4JobAlertTargets=_OraEM4JobAlertTargets_Object((1,3,6,1,4,1,111,15,1,2,1,6),_OraEM4JobAlertTargets_Type())
oraEM4JobAlertTargets.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertTargets.setStatus(_A)
_OraEM4JobAlertTimeStamp_Type=DisplayString
_OraEM4JobAlertTimeStamp_Object=MibTableColumn
oraEM4JobAlertTimeStamp=_OraEM4JobAlertTimeStamp_Object((1,3,6,1,4,1,111,15,1,2,1,7),_OraEM4JobAlertTimeStamp_Type())
oraEM4JobAlertTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertTimeStamp.setStatus(_A)
_OraEM4JobAlertRuleName_Type=DisplayString
_OraEM4JobAlertRuleName_Object=MibTableColumn
oraEM4JobAlertRuleName=_OraEM4JobAlertRuleName_Object((1,3,6,1,4,1,111,15,1,2,1,8),_OraEM4JobAlertRuleName_Type())
oraEM4JobAlertRuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertRuleName.setStatus(_A)
_OraEM4JobAlertRuleOwner_Type=DisplayString
_OraEM4JobAlertRuleOwner_Object=MibTableColumn
oraEM4JobAlertRuleOwner=_OraEM4JobAlertRuleOwner_Object((1,3,6,1,4,1,111,15,1,2,1,9),_OraEM4JobAlertRuleOwner_Type())
oraEM4JobAlertRuleOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertRuleOwner.setStatus(_A)
_OraEM4JobAlertMetricName_Type=DisplayString
_OraEM4JobAlertMetricName_Object=MibTableColumn
oraEM4JobAlertMetricName=_OraEM4JobAlertMetricName_Object((1,3,6,1,4,1,111,15,1,2,1,10),_OraEM4JobAlertMetricName_Type())
oraEM4JobAlertMetricName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertMetricName.setStatus(_A)
_OraEM4JobAlertMetricValue_Type=DisplayString
_OraEM4JobAlertMetricValue_Object=MibTableColumn
oraEM4JobAlertMetricValue=_OraEM4JobAlertMetricValue_Object((1,3,6,1,4,1,111,15,1,2,1,11),_OraEM4JobAlertMetricValue_Type())
oraEM4JobAlertMetricValue.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertMetricValue.setStatus(_A)
_OraEM4JobAlertContext_Type=DisplayString
_OraEM4JobAlertContext_Object=MibTableColumn
oraEM4JobAlertContext=_OraEM4JobAlertContext_Object((1,3,6,1,4,1,111,15,1,2,1,12),_OraEM4JobAlertContext_Type())
oraEM4JobAlertContext.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertContext.setStatus(_A)
_OraEM4JobAlertKeyName_Type=DisplayString
_OraEM4JobAlertKeyName_Object=MibTableColumn
oraEM4JobAlertKeyName=_OraEM4JobAlertKeyName_Object((1,3,6,1,4,1,111,15,1,2,1,13),_OraEM4JobAlertKeyName_Type())
oraEM4JobAlertKeyName.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertKeyName.setStatus(_A)
_OraEM4JobAlertKeyValue_Type=DisplayString
_OraEM4JobAlertKeyValue_Object=MibTableColumn
oraEM4JobAlertKeyValue=_OraEM4JobAlertKeyValue_Object((1,3,6,1,4,1,111,15,1,2,1,14),_OraEM4JobAlertKeyValue_Type())
oraEM4JobAlertKeyValue.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertKeyValue.setStatus(_A)
_OraEM4JobAlertSeverity_Type=DisplayString
_OraEM4JobAlertSeverity_Object=MibTableColumn
oraEM4JobAlertSeverity=_OraEM4JobAlertSeverity_Object((1,3,6,1,4,1,111,15,1,2,1,15),_OraEM4JobAlertSeverity_Type())
oraEM4JobAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:oraEM4JobAlertSeverity.setStatus(_A)
_OraEM4Traps_ObjectIdentity=ObjectIdentity
oraEM4Traps=_OraEM4Traps_ObjectIdentity((1,3,6,1,4,1,111,15,2))
oraEM4Alert=NotificationType((1,3,6,1,4,1,111,15,2,0,1))
oraEM4Alert.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:oraEM4Alert.setStatus('')
oraEM4JobAlert=NotificationType((1,3,6,1,4,1,111,15,2,0,2))
oraEM4JobAlert.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:oraEM4JobAlert.setStatus('')
mibBuilder.exportSymbols(_B,**{'oracle':oracle,'oraEM4':oraEM4,'oraEM4Objects':oraEM4Objects,'oraEM4AlertTable':oraEM4AlertTable,'oraEM4AlertEntry':oraEM4AlertEntry,_E:oraEM4AlertIndex,_G:oraEM4AlertTargetName,_H:oraEM4AlertTargetType,_I:oraEM4AlertHostName,_J:oraEM4AlertMetricName,_K:oraEM4AlertKeyName,_L:oraEM4AlertKeyValue,_M:oraEM4AlertTimeStamp,_N:oraEM4AlertSeverity,_O:oraEM4AlertMessage,_P:oraEM4AlertRuleName,_Q:oraEM4AlertRuleOwner,_R:oraEM4AlertMetricValue,_S:oraEM4AlertContext,'oraEM4JobAlertTable':oraEM4JobAlertTable,'oraEM4JobAlertEntry':oraEM4JobAlertEntry,_F:oraEM4JobAlertIndex,_T:oraEM4JobAlertJobName,_U:oraEM4JobAlertJobOwner,_V:oraEM4JobAlertJobType,_W:oraEM4JobAlertJobStatus,_X:oraEM4JobAlertTargets,_Y:oraEM4JobAlertTimeStamp,_Z:oraEM4JobAlertRuleName,_a:oraEM4JobAlertRuleOwner,_b:oraEM4JobAlertMetricName,_c:oraEM4JobAlertMetricValue,_d:oraEM4JobAlertContext,_e:oraEM4JobAlertKeyName,_f:oraEM4JobAlertKeyValue,_g:oraEM4JobAlertSeverity,'oraEM4Traps':oraEM4Traps,'oraEM4Alert':oraEM4Alert,'oraEM4JobAlert':oraEM4JobAlert})