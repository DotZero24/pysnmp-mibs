_e='cvaNotificationGroup'
_d='cvaNotificationInfoGroup'
_c='cvaModuleInfoGroup'
_b='cvaProcessStop'
_a='cvaProcessStart'
_Z='cvaModuleRunTimeFailure'
_Y='cvaModuleStop'
_X='cvaModuleStart'
_W='cvaNotificationEnable'
_V='cvaWorkflowInstallEnable'
_U='cvaWorkflowInstallScriptName'
_T='cvaWorkflowInstallLocator'
_S='cvaWorkflowInstallName'
_R='outOfResource'
_Q='initFailure'
_P='cvaWorkflowInstallIndex'
_O='OctetString'
_N='cvaModuleRunTimeFailureCause'
_M='cvaModuleFailureCause'
_L='SnmpAdminString'
_K='cvaModuleFailureMessage'
_J='cvaModuleFailureName'
_I='cvaProcessId'
_H='read-only'
_G='DisplayString'
_F='Integer32'
_E='cvaModuleName'
_D='cvaAlarmSeverity'
_C='accessible-for-notify'
_B='current'
_A='CISCO-VOICE-APPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention','TruthValue')
ciscoVoiceAppsMIB=ModuleIdentity((1,3,6,1,4,1,9,9,190))
if mibBuilder.loadTexts:ciscoVoiceAppsMIB.setRevisions(('2005-12-22 00:00','2001-02-26 00:00'))
_CiscoVoiceAppsMIBObjects_ObjectIdentity=ObjectIdentity
ciscoVoiceAppsMIBObjects=_CiscoVoiceAppsMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,190,1))
_CvaGeneralInfo_ObjectIdentity=ObjectIdentity
cvaGeneralInfo=_CvaGeneralInfo_ObjectIdentity((1,3,6,1,4,1,9,9,190,1,1))
_CvaWorkflowInstallTable_Object=MibTable
cvaWorkflowInstallTable=_CvaWorkflowInstallTable_Object((1,3,6,1,4,1,9,9,190,1,1,1))
if mibBuilder.loadTexts:cvaWorkflowInstallTable.setStatus(_B)
_CvaWorkflowInstallEntry_Object=MibTableRow
cvaWorkflowInstallEntry=_CvaWorkflowInstallEntry_Object((1,3,6,1,4,1,9,9,190,1,1,1,1))
cvaWorkflowInstallEntry.setIndexNames((0,_A,_P))
if mibBuilder.loadTexts:cvaWorkflowInstallEntry.setStatus(_B)
_CvaWorkflowInstallIndex_Type=Unsigned32
_CvaWorkflowInstallIndex_Object=MibTableColumn
cvaWorkflowInstallIndex=_CvaWorkflowInstallIndex_Object((1,3,6,1,4,1,9,9,190,1,1,1,1,1),_CvaWorkflowInstallIndex_Type())
cvaWorkflowInstallIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cvaWorkflowInstallIndex.setStatus(_B)
class _CvaWorkflowInstallName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CvaWorkflowInstallName_Type.__name__=_L
_CvaWorkflowInstallName_Object=MibTableColumn
cvaWorkflowInstallName=_CvaWorkflowInstallName_Object((1,3,6,1,4,1,9,9,190,1,1,1,1,2),_CvaWorkflowInstallName_Type())
cvaWorkflowInstallName.setMaxAccess(_H)
if mibBuilder.loadTexts:cvaWorkflowInstallName.setStatus(_B)
class _CvaWorkflowInstallLocator_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CvaWorkflowInstallLocator_Type.__name__=_O
_CvaWorkflowInstallLocator_Object=MibTableColumn
cvaWorkflowInstallLocator=_CvaWorkflowInstallLocator_Object((1,3,6,1,4,1,9,9,190,1,1,1,1,3),_CvaWorkflowInstallLocator_Type())
cvaWorkflowInstallLocator.setMaxAccess(_H)
if mibBuilder.loadTexts:cvaWorkflowInstallLocator.setStatus(_B)
class _CvaWorkflowInstallScriptName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CvaWorkflowInstallScriptName_Type.__name__=_L
_CvaWorkflowInstallScriptName_Object=MibTableColumn
cvaWorkflowInstallScriptName=_CvaWorkflowInstallScriptName_Object((1,3,6,1,4,1,9,9,190,1,1,1,1,4),_CvaWorkflowInstallScriptName_Type())
cvaWorkflowInstallScriptName.setMaxAccess(_H)
if mibBuilder.loadTexts:cvaWorkflowInstallScriptName.setStatus(_B)
_CvaWorkflowInstallEnable_Type=TruthValue
_CvaWorkflowInstallEnable_Object=MibTableColumn
cvaWorkflowInstallEnable=_CvaWorkflowInstallEnable_Object((1,3,6,1,4,1,9,9,190,1,1,1,1,5),_CvaWorkflowInstallEnable_Type())
cvaWorkflowInstallEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cvaWorkflowInstallEnable.setStatus(_B)
_CvaNotificationEnable_Type=TruthValue
_CvaNotificationEnable_Object=MibScalar
cvaNotificationEnable=_CvaNotificationEnable_Object((1,3,6,1,4,1,9,9,190,1,1,3),_CvaNotificationEnable_Type())
cvaNotificationEnable.setMaxAccess('read-write')
if mibBuilder.loadTexts:cvaNotificationEnable.setStatus(_B)
_CvaModuleFailureInfo_ObjectIdentity=ObjectIdentity
cvaModuleFailureInfo=_CvaModuleFailureInfo_ObjectIdentity((1,3,6,1,4,1,9,9,190,1,2))
class _CvaAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('emergency',1),('alert',2),('critical',3),('error',4),('warning',5),('notice',6),('informational',7)))
_CvaAlarmSeverity_Type.__name__=_F
_CvaAlarmSeverity_Object=MibScalar
cvaAlarmSeverity=_CvaAlarmSeverity_Object((1,3,6,1,4,1,9,9,190,1,2,1),_CvaAlarmSeverity_Type())
cvaAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaAlarmSeverity.setStatus(_B)
class _CvaModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CvaModuleName_Type.__name__=_G
_CvaModuleName_Object=MibScalar
cvaModuleName=_CvaModuleName_Object((1,3,6,1,4,1,9,9,190,1,2,2),_CvaModuleName_Type())
cvaModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaModuleName.setStatus(_B)
_CvaProcessId_Type=Unsigned32
_CvaProcessId_Object=MibScalar
cvaProcessId=_CvaProcessId_Object((1,3,6,1,4,1,9,9,190,1,2,3),_CvaProcessId_Type())
cvaProcessId.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaProcessId.setStatus(_B)
class _CvaModuleFailureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CvaModuleFailureName_Type.__name__=_G
_CvaModuleFailureName_Object=MibScalar
cvaModuleFailureName=_CvaModuleFailureName_Object((1,3,6,1,4,1,9,9,190,1,2,4),_CvaModuleFailureName_Type())
cvaModuleFailureName.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaModuleFailureName.setStatus(_B)
class _CvaModuleFailureCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('gracefulShutDown',2),('heartBeatFailure',3),(_Q,4),(_R,5),('partialFailure',6)))
_CvaModuleFailureCause_Type.__name__=_F
_CvaModuleFailureCause_Object=MibScalar
cvaModuleFailureCause=_CvaModuleFailureCause_Object((1,3,6,1,4,1,9,9,190,1,2,5),_CvaModuleFailureCause_Type())
cvaModuleFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaModuleFailureCause.setStatus(_B)
class _CvaModuleFailureMessage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CvaModuleFailureMessage_Type.__name__=_G
_CvaModuleFailureMessage_Object=MibScalar
cvaModuleFailureMessage=_CvaModuleFailureMessage_Object((1,3,6,1,4,1,9,9,190,1,2,6),_CvaModuleFailureMessage_Type())
cvaModuleFailureMessage.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaModuleFailureMessage.setStatus(_B)
class _CvaModuleRunTimeFailureCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('other',1),('readAccessFailure',2),('writeAccessFailure',3),('createFailure',4),('deleteFailure',5),('updateFailure',6),(_Q,7),('loadFailure',8),(_R,9),('callProcessFailure',10),('registrationFailure',11),('deRegistrationFailure',12),('connectionFailure',13),('disconnectionFailure',14),('unknownTarget',15),('unReacheableTarget',16)))
_CvaModuleRunTimeFailureCause_Type.__name__=_F
_CvaModuleRunTimeFailureCause_Object=MibScalar
cvaModuleRunTimeFailureCause=_CvaModuleRunTimeFailureCause_Object((1,3,6,1,4,1,9,9,190,1,2,7),_CvaModuleRunTimeFailureCause_Type())
cvaModuleRunTimeFailureCause.setMaxAccess(_C)
if mibBuilder.loadTexts:cvaModuleRunTimeFailureCause.setStatus(_B)
_CiscoVoiceAppsMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
ciscoVoiceAppsMIBNotificationPrefix=_CiscoVoiceAppsMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,190,2))
_CiscoVoiceAppsMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoVoiceAppsMIBNotifications=_CiscoVoiceAppsMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,190,2,0))
_CiscoVoiceAppsMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVoiceAppsMIBConformance=_CiscoVoiceAppsMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,190,3))
_CiscoVoiceAppsMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVoiceAppsMIBCompliances=_CiscoVoiceAppsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,190,3,1))
_CiscoVoiceAppsMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVoiceAppsMIBGroups=_CiscoVoiceAppsMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,190,3,2))
cvaModuleInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,190,3,2,1))
cvaModuleInfoGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cvaModuleInfoGroup.setStatus(_B)
cvaNotificationInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,190,3,2,2))
cvaNotificationInfoGroup.setObjects(*((_A,_D),(_A,_E),(_A,_I),(_A,_J),(_A,_M),(_A,_K),(_A,_N)))
if mibBuilder.loadTexts:cvaNotificationInfoGroup.setStatus(_B)
cvaModuleStart=NotificationType((1,3,6,1,4,1,9,9,190,2,0,1))
cvaModuleStart.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:cvaModuleStart.setStatus(_B)
cvaModuleStop=NotificationType((1,3,6,1,4,1,9,9,190,2,0,2))
cvaModuleStop.setObjects(*((_A,_D),(_A,_E),(_A,_M),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cvaModuleStop.setStatus(_B)
cvaModuleRunTimeFailure=NotificationType((1,3,6,1,4,1,9,9,190,2,0,3))
cvaModuleRunTimeFailure.setObjects(*((_A,_D),(_A,_E),(_A,_N),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:cvaModuleRunTimeFailure.setStatus(_B)
cvaProcessStart=NotificationType((1,3,6,1,4,1,9,9,190,2,0,4))
cvaProcessStart.setObjects(*((_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:cvaProcessStart.setStatus(_B)
cvaProcessStop=NotificationType((1,3,6,1,4,1,9,9,190,2,0,5))
cvaProcessStop.setObjects(*((_A,_D),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:cvaProcessStop.setStatus(_B)
cvaNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,190,3,2,3))
cvaNotificationGroup.setObjects(*((_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cvaNotificationGroup.setStatus(_B)
ciscoVoiceAppsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,190,3,1,1))
ciscoVoiceAppsMIBCompliance.setObjects(*((_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:ciscoVoiceAppsMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoVoiceAppsMIB':ciscoVoiceAppsMIB,'ciscoVoiceAppsMIBObjects':ciscoVoiceAppsMIBObjects,'cvaGeneralInfo':cvaGeneralInfo,'cvaWorkflowInstallTable':cvaWorkflowInstallTable,'cvaWorkflowInstallEntry':cvaWorkflowInstallEntry,_P:cvaWorkflowInstallIndex,_S:cvaWorkflowInstallName,_T:cvaWorkflowInstallLocator,_U:cvaWorkflowInstallScriptName,_V:cvaWorkflowInstallEnable,_W:cvaNotificationEnable,'cvaModuleFailureInfo':cvaModuleFailureInfo,_D:cvaAlarmSeverity,_E:cvaModuleName,_I:cvaProcessId,_J:cvaModuleFailureName,_M:cvaModuleFailureCause,_K:cvaModuleFailureMessage,_N:cvaModuleRunTimeFailureCause,'ciscoVoiceAppsMIBNotificationPrefix':ciscoVoiceAppsMIBNotificationPrefix,'ciscoVoiceAppsMIBNotifications':ciscoVoiceAppsMIBNotifications,_X:cvaModuleStart,_Y:cvaModuleStop,_Z:cvaModuleRunTimeFailure,_a:cvaProcessStart,_b:cvaProcessStop,'ciscoVoiceAppsMIBConformance':ciscoVoiceAppsMIBConformance,'ciscoVoiceAppsMIBCompliances':ciscoVoiceAppsMIBCompliances,'ciscoVoiceAppsMIBCompliance':ciscoVoiceAppsMIBCompliance,'ciscoVoiceAppsMIBGroups':ciscoVoiceAppsMIBGroups,_c:cvaModuleInfoGroup,_d:cvaNotificationInfoGroup,_e:cvaNotificationGroup})