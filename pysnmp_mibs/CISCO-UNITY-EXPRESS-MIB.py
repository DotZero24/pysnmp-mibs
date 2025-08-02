_Av='cueSystemGroupRev1'
_Au='cueSystemGroup'
_At='ciscoUnityExpressNTPAlert'
_As='ciscoUnityExpressBackupAlert'
_Ar='ciscoUnityExpressRescExhausted'
_Aq='ciscoUnityExpressCallMgrAlert'
_Ap='ciscoUnityExpressSecurityAlert'
_Ao='ciscoUnityExpressStorageAlert'
_An='ciscoUnityExpressApplAlert'
_Am='cueBRHistoryResult'
_Al='cueBRHistoryDate'
_Ak='cueBRHistoryOperation'
_Aj='cuePINResetThresh'
_Ai='cuePINPasswordThresh'
_Ah='cuePINUidThresh'
_Ag='cueLoginPasswordThresh'
_Af='cueLoginUsernameThresh'
_Ae='cueNotifEnable'
_Ad='cuePINPasswordFailures'
_Ac='cuePINUidFailures'
_Ab='cuePINResets'
_Aa='cuePINAttempts'
_AZ='cueLoginPasswordFailures'
_AY='cueLoginUsernameFailures'
_AX='cueLoginAttempts'
_AW='cueMailboxesAbove90PercentFull'
_AV='cueLicensedMailboxesMax'
_AU='cueMessagesDeleted'
_AT='cueMessagesRetrieved'
_AS='cueMessagesLeft'
_AR='cueMboxMWIState'
_AQ='cueMboxBusy'
_AP='cueMboxEnabled'
_AO='cueMboxGreetingType'
_AN='cueMboxPlayTutorial'
_AM='cueMboxMessageExpiryTime'
_AL='cueMboxMessageSizeMax'
_AK='cueMboxNumberOfSavedMessages'
_AJ='cueMboxNumberOfNewMessages'
_AI='cueMboxNumberOfMessages'
_AH='cueMboxPercentTimeUsed'
_AG='cueMboxTimeUsed'
_AF='cueMboxSize'
_AE='cueMboxDescription'
_AD='cueMboxType'
_AC='cueMboxPrimaryExtension'
_AB='cueMboxOwner'
_AA='cueAverageGreetingLength'
_A9='cueGreetingCount'
_A8='cueGreetingTimeUsed'
_A7='cueAverageMessageLength'
_A6='cueMessageCount'
_A5='cueMessageTimeUsed'
_A4='cuePercentTimeUsed'
_A3='cueTotalTimeUsed'
_A2='cueAllocatedCapacity'
_A1='cueCapacityOfVoicemail'
_A0='cueOrphanedMailboxes'
_z='cueGeneralDeliveryMailboxes'
_y='cuePersonalMailboxes'
_x='cueActiveCalls'
_w='cueLicensedPortsMax'
_v='cueHardwareModuleType'
_u='cueBRHistoryIndex'
_t='cueMboxIndex'
_s='percent'
_r='cueJTAPIServerIndex'
_q='deprecated'
_p='read-write'
_o='TruthValue'
_n='cueBackupRestoreGroup'
_m='ciscoUnityExpressMIBNotificationsGroup'
_l='cueNotifGroup'
_k='cueSecurityGroup'
_j='cueUsageGroup'
_i='cueDefaultMessageExpiryTime'
_h='cueDefaultMessageSizeMax'
_g='cueDefaultGreetingSize'
_f='cueDefaultMailboxSize'
_e='cueJTAPIPortsRegistered'
_d='cueJTAPISoftwareVersion'
_c='cueJTAPIUsername'
_b='cueJTAPISubsystemState'
_a='cueJTAPIServerIP'
_Z='cueJTAPIServerIPType'
_Y='cueJTAPIServerName'
_X='cueSIPPort'
_W='cueSIPGatewayIP'
_V='cueSIPGatewayIPType'
_U='cueSIPGatewayName'
_T='cueCallControlAgentType'
_S='cueAANumber'
_R='cueVoicemailNumber'
_Q='cueAVTNumber'
_P='cueShutdownRequest'
_O='minutes'
_N='not-accessible'
_M='accessible-for-notify'
_L='cueNotifDetail'
_K='cueNotifDescription'
_J='cueNotifDate'
_I='cueNotifSeverity'
_H='Integer32'
_G='seconds'
_F='SnmpAdminString'
_E='Unsigned32'
_D='Gauge32'
_C='read-only'
_B='current'
_A='CISCO-UNITY-EXPRESS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_D,_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_o)
ciscoUnityExpressMIB=ModuleIdentity((1,3,6,1,4,1,9,9,420))
if mibBuilder.loadTexts:ciscoUnityExpressMIB.setRevisions(('2007-01-08 00:00','2005-09-02 00:00'))
_CiscoUnityExpressMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoUnityExpressMIBNotifs=_CiscoUnityExpressMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,420,0))
_CiscoUnityExpressMIBObjects_ObjectIdentity=ObjectIdentity
ciscoUnityExpressMIBObjects=_CiscoUnityExpressMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,420,1))
_CueSystem_ObjectIdentity=ObjectIdentity
cueSystem=_CueSystem_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,1))
_CueSystemControl_ObjectIdentity=ObjectIdentity
cueSystemControl=_CueSystemControl_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,1,1))
_CueShutdownRequest_Type=TruthValue
_CueShutdownRequest_Object=MibScalar
cueShutdownRequest=_CueShutdownRequest_Object((1,3,6,1,4,1,9,9,420,1,1,1,1),_CueShutdownRequest_Type())
cueShutdownRequest.setMaxAccess(_p)
if mibBuilder.loadTexts:cueShutdownRequest.setStatus(_B)
_CueSystemScalars_ObjectIdentity=ObjectIdentity
cueSystemScalars=_CueSystemScalars_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,1,2))
class _CueAVTNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CueAVTNumber_Type.__name__=_F
_CueAVTNumber_Object=MibScalar
cueAVTNumber=_CueAVTNumber_Object((1,3,6,1,4,1,9,9,420,1,1,2,1),_CueAVTNumber_Type())
cueAVTNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cueAVTNumber.setStatus(_B)
class _CueVoicemailNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CueVoicemailNumber_Type.__name__=_F
_CueVoicemailNumber_Object=MibScalar
cueVoicemailNumber=_CueVoicemailNumber_Object((1,3,6,1,4,1,9,9,420,1,1,2,2),_CueVoicemailNumber_Type())
cueVoicemailNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cueVoicemailNumber.setStatus(_B)
class _CueAANumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CueAANumber_Type.__name__=_F
_CueAANumber_Object=MibScalar
cueAANumber=_CueAANumber_Object((1,3,6,1,4,1,9,9,420,1,1,2,3),_CueAANumber_Type())
cueAANumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cueAANumber.setStatus(_B)
class _CueHardwareModuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aim',1),('nm',2),('other',3)))
_CueHardwareModuleType_Type.__name__=_H
_CueHardwareModuleType_Object=MibScalar
cueHardwareModuleType=_CueHardwareModuleType_Object((1,3,6,1,4,1,9,9,420,1,1,2,4),_CueHardwareModuleType_Type())
cueHardwareModuleType.setMaxAccess(_C)
if mibBuilder.loadTexts:cueHardwareModuleType.setStatus(_q)
class _CueCallControlAgentType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ccm',1),('ccme',2)))
_CueCallControlAgentType_Type.__name__=_H
_CueCallControlAgentType_Object=MibScalar
cueCallControlAgentType=_CueCallControlAgentType_Object((1,3,6,1,4,1,9,9,420,1,1,2,5),_CueCallControlAgentType_Type())
cueCallControlAgentType.setMaxAccess(_C)
if mibBuilder.loadTexts:cueCallControlAgentType.setStatus(_B)
_CueSIPInfo_ObjectIdentity=ObjectIdentity
cueSIPInfo=_CueSIPInfo_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,1,3))
class _CueSIPGatewayName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CueSIPGatewayName_Type.__name__=_F
_CueSIPGatewayName_Object=MibScalar
cueSIPGatewayName=_CueSIPGatewayName_Object((1,3,6,1,4,1,9,9,420,1,1,3,1),_CueSIPGatewayName_Type())
cueSIPGatewayName.setMaxAccess(_C)
if mibBuilder.loadTexts:cueSIPGatewayName.setStatus(_B)
_CueSIPGatewayIPType_Type=InetAddressType
_CueSIPGatewayIPType_Object=MibScalar
cueSIPGatewayIPType=_CueSIPGatewayIPType_Object((1,3,6,1,4,1,9,9,420,1,1,3,2),_CueSIPGatewayIPType_Type())
cueSIPGatewayIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cueSIPGatewayIPType.setStatus(_B)
_CueSIPGatewayIP_Type=InetAddress
_CueSIPGatewayIP_Object=MibScalar
cueSIPGatewayIP=_CueSIPGatewayIP_Object((1,3,6,1,4,1,9,9,420,1,1,3,3),_CueSIPGatewayIP_Type())
cueSIPGatewayIP.setMaxAccess(_C)
if mibBuilder.loadTexts:cueSIPGatewayIP.setStatus(_B)
_CueSIPPort_Type=InetPortNumber
_CueSIPPort_Object=MibScalar
cueSIPPort=_CueSIPPort_Object((1,3,6,1,4,1,9,9,420,1,1,3,4),_CueSIPPort_Type())
cueSIPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cueSIPPort.setStatus(_B)
_CueJTAPIInfo_ObjectIdentity=ObjectIdentity
cueJTAPIInfo=_CueJTAPIInfo_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,1,4))
_CueJTAPIServerTable_Object=MibTable
cueJTAPIServerTable=_CueJTAPIServerTable_Object((1,3,6,1,4,1,9,9,420,1,1,4,1))
if mibBuilder.loadTexts:cueJTAPIServerTable.setStatus(_B)
_CueJTAPIServerEntry_Object=MibTableRow
cueJTAPIServerEntry=_CueJTAPIServerEntry_Object((1,3,6,1,4,1,9,9,420,1,1,4,1,1))
cueJTAPIServerEntry.setIndexNames((0,_A,_r))
if mibBuilder.loadTexts:cueJTAPIServerEntry.setStatus(_B)
class _CueJTAPIServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CueJTAPIServerIndex_Type.__name__=_E
_CueJTAPIServerIndex_Object=MibTableColumn
cueJTAPIServerIndex=_CueJTAPIServerIndex_Object((1,3,6,1,4,1,9,9,420,1,1,4,1,1,1),_CueJTAPIServerIndex_Type())
cueJTAPIServerIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cueJTAPIServerIndex.setStatus(_B)
class _CueJTAPIServerName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CueJTAPIServerName_Type.__name__=_F
_CueJTAPIServerName_Object=MibTableColumn
cueJTAPIServerName=_CueJTAPIServerName_Object((1,3,6,1,4,1,9,9,420,1,1,4,1,1,2),_CueJTAPIServerName_Type())
cueJTAPIServerName.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPIServerName.setStatus(_B)
_CueJTAPIServerIPType_Type=InetAddressType
_CueJTAPIServerIPType_Object=MibTableColumn
cueJTAPIServerIPType=_CueJTAPIServerIPType_Object((1,3,6,1,4,1,9,9,420,1,1,4,1,1,3),_CueJTAPIServerIPType_Type())
cueJTAPIServerIPType.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPIServerIPType.setStatus(_B)
_CueJTAPIServerIP_Type=InetAddress
_CueJTAPIServerIP_Object=MibTableColumn
cueJTAPIServerIP=_CueJTAPIServerIP_Object((1,3,6,1,4,1,9,9,420,1,1,4,1,1,4),_CueJTAPIServerIP_Type())
cueJTAPIServerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPIServerIP.setStatus(_B)
class _CueJTAPISubsystemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('unknown',1),('initializing',2),('inService',3),('outOfService',4),('shuttingDown',5),('shutDown',6),('partialService',7)))
_CueJTAPISubsystemState_Type.__name__=_H
_CueJTAPISubsystemState_Object=MibScalar
cueJTAPISubsystemState=_CueJTAPISubsystemState_Object((1,3,6,1,4,1,9,9,420,1,1,4,2),_CueJTAPISubsystemState_Type())
cueJTAPISubsystemState.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPISubsystemState.setStatus(_B)
class _CueJTAPIUsername_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CueJTAPIUsername_Type.__name__=_F
_CueJTAPIUsername_Object=MibScalar
cueJTAPIUsername=_CueJTAPIUsername_Object((1,3,6,1,4,1,9,9,420,1,1,4,3),_CueJTAPIUsername_Type())
cueJTAPIUsername.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPIUsername.setStatus(_B)
class _CueJTAPISoftwareVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CueJTAPISoftwareVersion_Type.__name__=_F
_CueJTAPISoftwareVersion_Object=MibScalar
cueJTAPISoftwareVersion=_CueJTAPISoftwareVersion_Object((1,3,6,1,4,1,9,9,420,1,1,4,4),_CueJTAPISoftwareVersion_Type())
cueJTAPISoftwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPISoftwareVersion.setStatus(_B)
class _CueJTAPIPortsRegistered_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_CueJTAPIPortsRegistered_Type.__name__=_D
_CueJTAPIPortsRegistered_Object=MibScalar
cueJTAPIPortsRegistered=_CueJTAPIPortsRegistered_Object((1,3,6,1,4,1,9,9,420,1,1,4,5),_CueJTAPIPortsRegistered_Type())
cueJTAPIPortsRegistered.setMaxAccess(_C)
if mibBuilder.loadTexts:cueJTAPIPortsRegistered.setStatus(_B)
_CueSystemDefaults_ObjectIdentity=ObjectIdentity
cueSystemDefaults=_CueSystemDefaults_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,1,5))
class _CueDefaultMailboxSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueDefaultMailboxSize_Type.__name__=_E
_CueDefaultMailboxSize_Object=MibScalar
cueDefaultMailboxSize=_CueDefaultMailboxSize_Object((1,3,6,1,4,1,9,9,420,1,1,5,1),_CueDefaultMailboxSize_Type())
cueDefaultMailboxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cueDefaultMailboxSize.setStatus(_B)
if mibBuilder.loadTexts:cueDefaultMailboxSize.setUnits(_G)
class _CueDefaultGreetingSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueDefaultGreetingSize_Type.__name__=_E
_CueDefaultGreetingSize_Object=MibScalar
cueDefaultGreetingSize=_CueDefaultGreetingSize_Object((1,3,6,1,4,1,9,9,420,1,1,5,2),_CueDefaultGreetingSize_Type())
cueDefaultGreetingSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cueDefaultGreetingSize.setStatus(_B)
if mibBuilder.loadTexts:cueDefaultGreetingSize.setUnits(_G)
class _CueDefaultMessageSizeMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueDefaultMessageSizeMax_Type.__name__=_E
_CueDefaultMessageSizeMax_Object=MibScalar
cueDefaultMessageSizeMax=_CueDefaultMessageSizeMax_Object((1,3,6,1,4,1,9,9,420,1,1,5,3),_CueDefaultMessageSizeMax_Type())
cueDefaultMessageSizeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cueDefaultMessageSizeMax.setStatus(_B)
if mibBuilder.loadTexts:cueDefaultMessageSizeMax.setUnits(_G)
class _CueDefaultMessageExpiryTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueDefaultMessageExpiryTime_Type.__name__=_E
_CueDefaultMessageExpiryTime_Object=MibScalar
cueDefaultMessageExpiryTime=_CueDefaultMessageExpiryTime_Object((1,3,6,1,4,1,9,9,420,1,1,5,4),_CueDefaultMessageExpiryTime_Type())
cueDefaultMessageExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cueDefaultMessageExpiryTime.setStatus(_B)
if mibBuilder.loadTexts:cueDefaultMessageExpiryTime.setUnits('days')
_CueUsage_ObjectIdentity=ObjectIdentity
cueUsage=_CueUsage_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,2))
_CueUsageScalars_ObjectIdentity=ObjectIdentity
cueUsageScalars=_CueUsageScalars_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,2,1))
class _CueLicensedPortsMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_CueLicensedPortsMax_Type.__name__=_E
_CueLicensedPortsMax_Object=MibScalar
cueLicensedPortsMax=_CueLicensedPortsMax_Object((1,3,6,1,4,1,9,9,420,1,2,1,1),_CueLicensedPortsMax_Type())
cueLicensedPortsMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLicensedPortsMax.setStatus(_B)
class _CueActiveCalls_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_CueActiveCalls_Type.__name__=_D
_CueActiveCalls_Object=MibScalar
cueActiveCalls=_CueActiveCalls_Object((1,3,6,1,4,1,9,9,420,1,2,1,2),_CueActiveCalls_Type())
cueActiveCalls.setMaxAccess(_C)
if mibBuilder.loadTexts:cueActiveCalls.setStatus(_B)
class _CuePersonalMailboxes_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CuePersonalMailboxes_Type.__name__=_D
_CuePersonalMailboxes_Object=MibScalar
cuePersonalMailboxes=_CuePersonalMailboxes_Object((1,3,6,1,4,1,9,9,420,1,2,1,3),_CuePersonalMailboxes_Type())
cuePersonalMailboxes.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePersonalMailboxes.setStatus(_B)
class _CueGeneralDeliveryMailboxes_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueGeneralDeliveryMailboxes_Type.__name__=_D
_CueGeneralDeliveryMailboxes_Object=MibScalar
cueGeneralDeliveryMailboxes=_CueGeneralDeliveryMailboxes_Object((1,3,6,1,4,1,9,9,420,1,2,1,4),_CueGeneralDeliveryMailboxes_Type())
cueGeneralDeliveryMailboxes.setMaxAccess(_C)
if mibBuilder.loadTexts:cueGeneralDeliveryMailboxes.setStatus(_B)
class _CueOrphanedMailboxes_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueOrphanedMailboxes_Type.__name__=_D
_CueOrphanedMailboxes_Object=MibScalar
cueOrphanedMailboxes=_CueOrphanedMailboxes_Object((1,3,6,1,4,1,9,9,420,1,2,1,5),_CueOrphanedMailboxes_Type())
cueOrphanedMailboxes.setMaxAccess(_C)
if mibBuilder.loadTexts:cueOrphanedMailboxes.setStatus(_B)
class _CueCapacityOfVoicemail_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueCapacityOfVoicemail_Type.__name__=_E
_CueCapacityOfVoicemail_Object=MibScalar
cueCapacityOfVoicemail=_CueCapacityOfVoicemail_Object((1,3,6,1,4,1,9,9,420,1,2,1,6),_CueCapacityOfVoicemail_Type())
cueCapacityOfVoicemail.setMaxAccess(_C)
if mibBuilder.loadTexts:cueCapacityOfVoicemail.setStatus(_B)
if mibBuilder.loadTexts:cueCapacityOfVoicemail.setUnits(_O)
class _CueAllocatedCapacity_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueAllocatedCapacity_Type.__name__=_E
_CueAllocatedCapacity_Object=MibScalar
cueAllocatedCapacity=_CueAllocatedCapacity_Object((1,3,6,1,4,1,9,9,420,1,2,1,7),_CueAllocatedCapacity_Type())
cueAllocatedCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:cueAllocatedCapacity.setStatus(_B)
if mibBuilder.loadTexts:cueAllocatedCapacity.setUnits(_O)
class _CueTotalTimeUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueTotalTimeUsed_Type.__name__=_D
_CueTotalTimeUsed_Object=MibScalar
cueTotalTimeUsed=_CueTotalTimeUsed_Object((1,3,6,1,4,1,9,9,420,1,2,1,8),_CueTotalTimeUsed_Type())
cueTotalTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cueTotalTimeUsed.setStatus(_B)
if mibBuilder.loadTexts:cueTotalTimeUsed.setUnits(_O)
class _CuePercentTimeUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CuePercentTimeUsed_Type.__name__=_D
_CuePercentTimeUsed_Object=MibScalar
cuePercentTimeUsed=_CuePercentTimeUsed_Object((1,3,6,1,4,1,9,9,420,1,2,1,9),_CuePercentTimeUsed_Type())
cuePercentTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePercentTimeUsed.setStatus(_B)
if mibBuilder.loadTexts:cuePercentTimeUsed.setUnits(_s)
class _CueMessageTimeUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueMessageTimeUsed_Type.__name__=_D
_CueMessageTimeUsed_Object=MibScalar
cueMessageTimeUsed=_CueMessageTimeUsed_Object((1,3,6,1,4,1,9,9,420,1,2,1,10),_CueMessageTimeUsed_Type())
cueMessageTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMessageTimeUsed.setStatus(_B)
if mibBuilder.loadTexts:cueMessageTimeUsed.setUnits(_G)
class _CueMessageCount_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMessageCount_Type.__name__=_D
_CueMessageCount_Object=MibScalar
cueMessageCount=_CueMessageCount_Object((1,3,6,1,4,1,9,9,420,1,2,1,11),_CueMessageCount_Type())
cueMessageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMessageCount.setStatus(_B)
class _CueAverageMessageLength_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueAverageMessageLength_Type.__name__=_D
_CueAverageMessageLength_Object=MibScalar
cueAverageMessageLength=_CueAverageMessageLength_Object((1,3,6,1,4,1,9,9,420,1,2,1,12),_CueAverageMessageLength_Type())
cueAverageMessageLength.setMaxAccess(_C)
if mibBuilder.loadTexts:cueAverageMessageLength.setStatus(_B)
if mibBuilder.loadTexts:cueAverageMessageLength.setUnits(_G)
class _CueGreetingTimeUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueGreetingTimeUsed_Type.__name__=_D
_CueGreetingTimeUsed_Object=MibScalar
cueGreetingTimeUsed=_CueGreetingTimeUsed_Object((1,3,6,1,4,1,9,9,420,1,2,1,13),_CueGreetingTimeUsed_Type())
cueGreetingTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cueGreetingTimeUsed.setStatus(_B)
if mibBuilder.loadTexts:cueGreetingTimeUsed.setUnits(_G)
class _CueGreetingCount_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueGreetingCount_Type.__name__=_D
_CueGreetingCount_Object=MibScalar
cueGreetingCount=_CueGreetingCount_Object((1,3,6,1,4,1,9,9,420,1,2,1,14),_CueGreetingCount_Type())
cueGreetingCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cueGreetingCount.setStatus(_B)
class _CueAverageGreetingLength_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueAverageGreetingLength_Type.__name__=_D
_CueAverageGreetingLength_Object=MibScalar
cueAverageGreetingLength=_CueAverageGreetingLength_Object((1,3,6,1,4,1,9,9,420,1,2,1,15),_CueAverageGreetingLength_Type())
cueAverageGreetingLength.setMaxAccess(_C)
if mibBuilder.loadTexts:cueAverageGreetingLength.setStatus(_B)
if mibBuilder.loadTexts:cueAverageGreetingLength.setUnits(_G)
_CueMessagesLeft_Type=Counter32
_CueMessagesLeft_Object=MibScalar
cueMessagesLeft=_CueMessagesLeft_Object((1,3,6,1,4,1,9,9,420,1,2,1,16),_CueMessagesLeft_Type())
cueMessagesLeft.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMessagesLeft.setStatus(_B)
_CueMessagesRetrieved_Type=Counter32
_CueMessagesRetrieved_Object=MibScalar
cueMessagesRetrieved=_CueMessagesRetrieved_Object((1,3,6,1,4,1,9,9,420,1,2,1,17),_CueMessagesRetrieved_Type())
cueMessagesRetrieved.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMessagesRetrieved.setStatus(_B)
_CueMessagesDeleted_Type=Counter32
_CueMessagesDeleted_Object=MibScalar
cueMessagesDeleted=_CueMessagesDeleted_Object((1,3,6,1,4,1,9,9,420,1,2,1,18),_CueMessagesDeleted_Type())
cueMessagesDeleted.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMessagesDeleted.setStatus(_B)
class _CueLicensedMailboxesMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueLicensedMailboxesMax_Type.__name__=_E
_CueLicensedMailboxesMax_Object=MibScalar
cueLicensedMailboxesMax=_CueLicensedMailboxesMax_Object((1,3,6,1,4,1,9,9,420,1,2,1,19),_CueLicensedMailboxesMax_Type())
cueLicensedMailboxesMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLicensedMailboxesMax.setStatus(_B)
class _CueMailboxesAbove90PercentFull_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CueMailboxesAbove90PercentFull_Type.__name__=_E
_CueMailboxesAbove90PercentFull_Object=MibScalar
cueMailboxesAbove90PercentFull=_CueMailboxesAbove90PercentFull_Object((1,3,6,1,4,1,9,9,420,1,2,1,20),_CueMailboxesAbove90PercentFull_Type())
cueMailboxesAbove90PercentFull.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMailboxesAbove90PercentFull.setStatus(_B)
_CueMboxTable_Object=MibTable
cueMboxTable=_CueMboxTable_Object((1,3,6,1,4,1,9,9,420,1,2,2))
if mibBuilder.loadTexts:cueMboxTable.setStatus(_B)
_CueMboxEntry_Object=MibTableRow
cueMboxEntry=_CueMboxEntry_Object((1,3,6,1,4,1,9,9,420,1,2,2,1))
cueMboxEntry.setIndexNames((0,_A,_t))
if mibBuilder.loadTexts:cueMboxEntry.setStatus(_B)
class _CueMboxIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CueMboxIndex_Type.__name__=_E
_CueMboxIndex_Object=MibTableColumn
cueMboxIndex=_CueMboxIndex_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,1),_CueMboxIndex_Type())
cueMboxIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cueMboxIndex.setStatus(_B)
class _CueMboxOwner_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CueMboxOwner_Type.__name__=_F
_CueMboxOwner_Object=MibTableColumn
cueMboxOwner=_CueMboxOwner_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,2),_CueMboxOwner_Type())
cueMboxOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxOwner.setStatus(_B)
class _CueMboxPrimaryExtension_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_CueMboxPrimaryExtension_Type.__name__=_F
_CueMboxPrimaryExtension_Object=MibTableColumn
cueMboxPrimaryExtension=_CueMboxPrimaryExtension_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,3),_CueMboxPrimaryExtension_Type())
cueMboxPrimaryExtension.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxPrimaryExtension.setStatus(_B)
class _CueMboxType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('personal',1),('generalDelivery',2)))
_CueMboxType_Type.__name__=_H
_CueMboxType_Object=MibTableColumn
cueMboxType=_CueMboxType_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,4),_CueMboxType_Type())
cueMboxType.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxType.setStatus(_B)
_CueMboxDescription_Type=SnmpAdminString
_CueMboxDescription_Object=MibTableColumn
cueMboxDescription=_CueMboxDescription_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,5),_CueMboxDescription_Type())
cueMboxDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxDescription.setStatus(_B)
class _CueMboxSize_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxSize_Type.__name__=_D
_CueMboxSize_Object=MibTableColumn
cueMboxSize=_CueMboxSize_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,6),_CueMboxSize_Type())
cueMboxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxSize.setStatus(_B)
if mibBuilder.loadTexts:cueMboxSize.setUnits(_G)
class _CueMboxTimeUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxTimeUsed_Type.__name__=_D
_CueMboxTimeUsed_Object=MibTableColumn
cueMboxTimeUsed=_CueMboxTimeUsed_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,7),_CueMboxTimeUsed_Type())
cueMboxTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxTimeUsed.setStatus(_B)
if mibBuilder.loadTexts:cueMboxTimeUsed.setUnits(_G)
class _CueMboxPercentTimeUsed_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CueMboxPercentTimeUsed_Type.__name__=_D
_CueMboxPercentTimeUsed_Object=MibTableColumn
cueMboxPercentTimeUsed=_CueMboxPercentTimeUsed_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,8),_CueMboxPercentTimeUsed_Type())
cueMboxPercentTimeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxPercentTimeUsed.setStatus(_B)
if mibBuilder.loadTexts:cueMboxPercentTimeUsed.setUnits(_s)
class _CueMboxNumberOfMessages_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxNumberOfMessages_Type.__name__=_D
_CueMboxNumberOfMessages_Object=MibTableColumn
cueMboxNumberOfMessages=_CueMboxNumberOfMessages_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,9),_CueMboxNumberOfMessages_Type())
cueMboxNumberOfMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxNumberOfMessages.setStatus(_B)
class _CueMboxNumberOfNewMessages_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxNumberOfNewMessages_Type.__name__=_D
_CueMboxNumberOfNewMessages_Object=MibTableColumn
cueMboxNumberOfNewMessages=_CueMboxNumberOfNewMessages_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,10),_CueMboxNumberOfNewMessages_Type())
cueMboxNumberOfNewMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxNumberOfNewMessages.setStatus(_B)
class _CueMboxNumberOfSavedMessages_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxNumberOfSavedMessages_Type.__name__=_D
_CueMboxNumberOfSavedMessages_Object=MibTableColumn
cueMboxNumberOfSavedMessages=_CueMboxNumberOfSavedMessages_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,11),_CueMboxNumberOfSavedMessages_Type())
cueMboxNumberOfSavedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxNumberOfSavedMessages.setStatus(_B)
class _CueMboxMessageSizeMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxMessageSizeMax_Type.__name__=_E
_CueMboxMessageSizeMax_Object=MibTableColumn
cueMboxMessageSizeMax=_CueMboxMessageSizeMax_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,12),_CueMboxMessageSizeMax_Type())
cueMboxMessageSizeMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxMessageSizeMax.setStatus(_B)
if mibBuilder.loadTexts:cueMboxMessageSizeMax.setUnits(_G)
class _CueMboxMessageExpiryTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueMboxMessageExpiryTime_Type.__name__=_E
_CueMboxMessageExpiryTime_Object=MibTableColumn
cueMboxMessageExpiryTime=_CueMboxMessageExpiryTime_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,13),_CueMboxMessageExpiryTime_Type())
cueMboxMessageExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxMessageExpiryTime.setStatus(_B)
if mibBuilder.loadTexts:cueMboxMessageExpiryTime.setUnits('days')
_CueMboxPlayTutorial_Type=TruthValue
_CueMboxPlayTutorial_Object=MibTableColumn
cueMboxPlayTutorial=_CueMboxPlayTutorial_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,14),_CueMboxPlayTutorial_Type())
cueMboxPlayTutorial.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxPlayTutorial.setStatus(_B)
class _CueMboxGreetingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('standard',1),('alternate',2)))
_CueMboxGreetingType_Type.__name__=_H
_CueMboxGreetingType_Object=MibTableColumn
cueMboxGreetingType=_CueMboxGreetingType_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,15),_CueMboxGreetingType_Type())
cueMboxGreetingType.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxGreetingType.setStatus(_B)
_CueMboxEnabled_Type=TruthValue
_CueMboxEnabled_Object=MibTableColumn
cueMboxEnabled=_CueMboxEnabled_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,16),_CueMboxEnabled_Type())
cueMboxEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxEnabled.setStatus(_B)
_CueMboxBusy_Type=TruthValue
_CueMboxBusy_Object=MibTableColumn
cueMboxBusy=_CueMboxBusy_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,17),_CueMboxBusy_Type())
cueMboxBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxBusy.setStatus(_B)
_CueMboxMWIState_Type=TruthValue
_CueMboxMWIState_Object=MibTableColumn
cueMboxMWIState=_CueMboxMWIState_Object((1,3,6,1,4,1,9,9,420,1,2,2,1,18),_CueMboxMWIState_Type())
cueMboxMWIState.setMaxAccess(_C)
if mibBuilder.loadTexts:cueMboxMWIState.setStatus(_B)
_CueSecurity_ObjectIdentity=ObjectIdentity
cueSecurity=_CueSecurity_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,3))
_CueLoginInfo_ObjectIdentity=ObjectIdentity
cueLoginInfo=_CueLoginInfo_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,3,1))
_CueLoginAttempts_Type=Counter32
_CueLoginAttempts_Object=MibScalar
cueLoginAttempts=_CueLoginAttempts_Object((1,3,6,1,4,1,9,9,420,1,3,1,1),_CueLoginAttempts_Type())
cueLoginAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLoginAttempts.setStatus(_B)
_CueLoginUsernameFailures_Type=Counter32
_CueLoginUsernameFailures_Object=MibScalar
cueLoginUsernameFailures=_CueLoginUsernameFailures_Object((1,3,6,1,4,1,9,9,420,1,3,1,2),_CueLoginUsernameFailures_Type())
cueLoginUsernameFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLoginUsernameFailures.setStatus(_B)
_CueLoginPasswordFailures_Type=Counter32
_CueLoginPasswordFailures_Object=MibScalar
cueLoginPasswordFailures=_CueLoginPasswordFailures_Object((1,3,6,1,4,1,9,9,420,1,3,1,3),_CueLoginPasswordFailures_Type())
cueLoginPasswordFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLoginPasswordFailures.setStatus(_B)
_CuePINInfo_ObjectIdentity=ObjectIdentity
cuePINInfo=_CuePINInfo_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,3,2))
_CuePINAttempts_Type=Counter32
_CuePINAttempts_Object=MibScalar
cuePINAttempts=_CuePINAttempts_Object((1,3,6,1,4,1,9,9,420,1,3,2,1),_CuePINAttempts_Type())
cuePINAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINAttempts.setStatus(_B)
_CuePINResets_Type=Counter32
_CuePINResets_Object=MibScalar
cuePINResets=_CuePINResets_Object((1,3,6,1,4,1,9,9,420,1,3,2,2),_CuePINResets_Type())
cuePINResets.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINResets.setStatus(_B)
_CuePINUidFailures_Type=Counter32
_CuePINUidFailures_Object=MibScalar
cuePINUidFailures=_CuePINUidFailures_Object((1,3,6,1,4,1,9,9,420,1,3,2,3),_CuePINUidFailures_Type())
cuePINUidFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINUidFailures.setStatus(_B)
_CuePINPasswordFailures_Type=Counter32
_CuePINPasswordFailures_Object=MibScalar
cuePINPasswordFailures=_CuePINPasswordFailures_Object((1,3,6,1,4,1,9,9,420,1,3,2,4),_CuePINPasswordFailures_Type())
cuePINPasswordFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINPasswordFailures.setStatus(_B)
_CueNotif_ObjectIdentity=ObjectIdentity
cueNotif=_CueNotif_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,4))
_CueNotifConfig_ObjectIdentity=ObjectIdentity
cueNotifConfig=_CueNotifConfig_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,4,1))
class _CueNotifEnable_Type(TruthValue):defaultValue=1
_CueNotifEnable_Type.__name__=_o
_CueNotifEnable_Object=MibScalar
cueNotifEnable=_CueNotifEnable_Object((1,3,6,1,4,1,9,9,420,1,4,1,1),_CueNotifEnable_Type())
cueNotifEnable.setMaxAccess(_p)
if mibBuilder.loadTexts:cueNotifEnable.setStatus(_B)
_CueNotifInfo_ObjectIdentity=ObjectIdentity
cueNotifInfo=_CueNotifInfo_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,4,2))
class _CueNotifSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('error',1),('warning',2),('informational',3)))
_CueNotifSeverity_Type.__name__=_H
_CueNotifSeverity_Object=MibScalar
cueNotifSeverity=_CueNotifSeverity_Object((1,3,6,1,4,1,9,9,420,1,4,2,1),_CueNotifSeverity_Type())
cueNotifSeverity.setMaxAccess(_M)
if mibBuilder.loadTexts:cueNotifSeverity.setStatus(_B)
_CueNotifDate_Type=DateAndTime
_CueNotifDate_Object=MibScalar
cueNotifDate=_CueNotifDate_Object((1,3,6,1,4,1,9,9,420,1,4,2,2),_CueNotifDate_Type())
cueNotifDate.setMaxAccess(_M)
if mibBuilder.loadTexts:cueNotifDate.setStatus(_B)
_CueNotifDescription_Type=SnmpAdminString
_CueNotifDescription_Object=MibScalar
cueNotifDescription=_CueNotifDescription_Object((1,3,6,1,4,1,9,9,420,1,4,2,3),_CueNotifDescription_Type())
cueNotifDescription.setMaxAccess(_M)
if mibBuilder.loadTexts:cueNotifDescription.setStatus(_B)
_CueNotifDetail_Type=SnmpAdminString
_CueNotifDetail_Object=MibScalar
cueNotifDetail=_CueNotifDetail_Object((1,3,6,1,4,1,9,9,420,1,4,2,4),_CueNotifDetail_Type())
cueNotifDetail.setMaxAccess(_M)
if mibBuilder.loadTexts:cueNotifDetail.setStatus(_B)
_CueNotifSecurity_ObjectIdentity=ObjectIdentity
cueNotifSecurity=_CueNotifSecurity_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,4,3))
class _CueLoginUsernameThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueLoginUsernameThresh_Type.__name__=_E
_CueLoginUsernameThresh_Object=MibScalar
cueLoginUsernameThresh=_CueLoginUsernameThresh_Object((1,3,6,1,4,1,9,9,420,1,4,3,1),_CueLoginUsernameThresh_Type())
cueLoginUsernameThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLoginUsernameThresh.setStatus(_B)
class _CueLoginPasswordThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CueLoginPasswordThresh_Type.__name__=_E
_CueLoginPasswordThresh_Object=MibScalar
cueLoginPasswordThresh=_CueLoginPasswordThresh_Object((1,3,6,1,4,1,9,9,420,1,4,3,2),_CueLoginPasswordThresh_Type())
cueLoginPasswordThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cueLoginPasswordThresh.setStatus(_B)
class _CuePINUidThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CuePINUidThresh_Type.__name__=_E
_CuePINUidThresh_Object=MibScalar
cuePINUidThresh=_CuePINUidThresh_Object((1,3,6,1,4,1,9,9,420,1,4,3,3),_CuePINUidThresh_Type())
cuePINUidThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINUidThresh.setStatus(_B)
class _CuePINPasswordThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CuePINPasswordThresh_Type.__name__=_E
_CuePINPasswordThresh_Object=MibScalar
cuePINPasswordThresh=_CuePINPasswordThresh_Object((1,3,6,1,4,1,9,9,420,1,4,3,4),_CuePINPasswordThresh_Type())
cuePINPasswordThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINPasswordThresh.setStatus(_B)
class _CuePINResetThresh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CuePINResetThresh_Type.__name__=_E
_CuePINResetThresh_Object=MibScalar
cuePINResetThresh=_CuePINResetThresh_Object((1,3,6,1,4,1,9,9,420,1,4,3,5),_CuePINResetThresh_Type())
cuePINResetThresh.setMaxAccess(_C)
if mibBuilder.loadTexts:cuePINResetThresh.setStatus(_B)
_CueBackupRestore_ObjectIdentity=ObjectIdentity
cueBackupRestore=_CueBackupRestore_ObjectIdentity((1,3,6,1,4,1,9,9,420,1,5))
_CueBRHistoryTable_Object=MibTable
cueBRHistoryTable=_CueBRHistoryTable_Object((1,3,6,1,4,1,9,9,420,1,5,1))
if mibBuilder.loadTexts:cueBRHistoryTable.setStatus(_B)
_CueBRHistoryEntry_Object=MibTableRow
cueBRHistoryEntry=_CueBRHistoryEntry_Object((1,3,6,1,4,1,9,9,420,1,5,1,1))
cueBRHistoryEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:cueBRHistoryEntry.setStatus(_B)
class _CueBRHistoryIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CueBRHistoryIndex_Type.__name__=_E
_CueBRHistoryIndex_Object=MibTableColumn
cueBRHistoryIndex=_CueBRHistoryIndex_Object((1,3,6,1,4,1,9,9,420,1,5,1,1,1),_CueBRHistoryIndex_Type())
cueBRHistoryIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:cueBRHistoryIndex.setStatus(_B)
class _CueBRHistoryOperation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backup',1),('restore',2)))
_CueBRHistoryOperation_Type.__name__=_H
_CueBRHistoryOperation_Object=MibTableColumn
cueBRHistoryOperation=_CueBRHistoryOperation_Object((1,3,6,1,4,1,9,9,420,1,5,1,1,2),_CueBRHistoryOperation_Type())
cueBRHistoryOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:cueBRHistoryOperation.setStatus(_B)
_CueBRHistoryDate_Type=DateAndTime
_CueBRHistoryDate_Object=MibTableColumn
cueBRHistoryDate=_CueBRHistoryDate_Object((1,3,6,1,4,1,9,9,420,1,5,1,1,3),_CueBRHistoryDate_Type())
cueBRHistoryDate.setMaxAccess(_C)
if mibBuilder.loadTexts:cueBRHistoryDate.setStatus(_B)
class _CueBRHistoryResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_CueBRHistoryResult_Type.__name__=_H
_CueBRHistoryResult_Object=MibTableColumn
cueBRHistoryResult=_CueBRHistoryResult_Object((1,3,6,1,4,1,9,9,420,1,5,1,1,4),_CueBRHistoryResult_Type())
cueBRHistoryResult.setMaxAccess(_C)
if mibBuilder.loadTexts:cueBRHistoryResult.setStatus(_B)
_CiscoUnityExpressMIBConform_ObjectIdentity=ObjectIdentity
ciscoUnityExpressMIBConform=_CiscoUnityExpressMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,420,2))
_CiscoUnityExpressMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoUnityExpressMIBCompliances=_CiscoUnityExpressMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,420,2,1))
_CiscoUnityExpressMIBGroups_ObjectIdentity=ObjectIdentity
ciscoUnityExpressMIBGroups=_CiscoUnityExpressMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,420,2,2))
cueSystemGroup=ObjectGroup((1,3,6,1,4,1,9,9,420,2,2,1))
cueSystemGroup.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_v),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cueSystemGroup.setStatus(_q)
cueUsageGroup=ObjectGroup((1,3,6,1,4,1,9,9,420,2,2,2))
cueUsageGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:cueUsageGroup.setStatus(_B)
cueSecurityGroup=ObjectGroup((1,3,6,1,4,1,9,9,420,2,2,3))
cueSecurityGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:cueSecurityGroup.setStatus(_B)
cueNotifGroup=ObjectGroup((1,3,6,1,4,1,9,9,420,2,2,4))
cueNotifGroup.setObjects(*((_A,_Ae),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:cueNotifGroup.setStatus(_B)
cueBackupRestoreGroup=ObjectGroup((1,3,6,1,4,1,9,9,420,2,2,6))
cueBackupRestoreGroup.setObjects(*((_A,_Ak),(_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:cueBackupRestoreGroup.setStatus(_B)
cueSystemGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,420,2,2,7))
cueSystemGroupRev1.setObjects(*((_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i)))
if mibBuilder.loadTexts:cueSystemGroupRev1.setStatus(_B)
ciscoUnityExpressApplAlert=NotificationType((1,3,6,1,4,1,9,9,420,0,1))
ciscoUnityExpressApplAlert.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressApplAlert.setStatus(_B)
ciscoUnityExpressStorageAlert=NotificationType((1,3,6,1,4,1,9,9,420,0,2))
ciscoUnityExpressStorageAlert.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressStorageAlert.setStatus(_B)
ciscoUnityExpressSecurityAlert=NotificationType((1,3,6,1,4,1,9,9,420,0,3))
ciscoUnityExpressSecurityAlert.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressSecurityAlert.setStatus(_B)
ciscoUnityExpressCallMgrAlert=NotificationType((1,3,6,1,4,1,9,9,420,0,4))
ciscoUnityExpressCallMgrAlert.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressCallMgrAlert.setStatus(_B)
ciscoUnityExpressRescExhausted=NotificationType((1,3,6,1,4,1,9,9,420,0,5))
ciscoUnityExpressRescExhausted.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressRescExhausted.setStatus(_B)
ciscoUnityExpressBackupAlert=NotificationType((1,3,6,1,4,1,9,9,420,0,6))
ciscoUnityExpressBackupAlert.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressBackupAlert.setStatus(_B)
ciscoUnityExpressNTPAlert=NotificationType((1,3,6,1,4,1,9,9,420,0,7))
ciscoUnityExpressNTPAlert.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:ciscoUnityExpressNTPAlert.setStatus(_B)
ciscoUnityExpressMIBNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,420,2,2,5))
ciscoUnityExpressMIBNotificationsGroup.setObjects(*((_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At)))
if mibBuilder.loadTexts:ciscoUnityExpressMIBNotificationsGroup.setStatus(_B)
ciscoUnityExpressMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,420,2,1,1))
ciscoUnityExpressMIBCompliance.setObjects(*((_A,_Au),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoUnityExpressMIBCompliance.setStatus(_B)
ciscoUnityExpressMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,420,2,1,2))
ciscoUnityExpressMIBComplianceRev1.setObjects(*((_A,_Av),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:ciscoUnityExpressMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoUnityExpressMIB':ciscoUnityExpressMIB,'ciscoUnityExpressMIBNotifs':ciscoUnityExpressMIBNotifs,_An:ciscoUnityExpressApplAlert,_Ao:ciscoUnityExpressStorageAlert,_Ap:ciscoUnityExpressSecurityAlert,_Aq:ciscoUnityExpressCallMgrAlert,_Ar:ciscoUnityExpressRescExhausted,_As:ciscoUnityExpressBackupAlert,_At:ciscoUnityExpressNTPAlert,'ciscoUnityExpressMIBObjects':ciscoUnityExpressMIBObjects,'cueSystem':cueSystem,'cueSystemControl':cueSystemControl,_P:cueShutdownRequest,'cueSystemScalars':cueSystemScalars,_Q:cueAVTNumber,_R:cueVoicemailNumber,_S:cueAANumber,_v:cueHardwareModuleType,_T:cueCallControlAgentType,'cueSIPInfo':cueSIPInfo,_U:cueSIPGatewayName,_V:cueSIPGatewayIPType,_W:cueSIPGatewayIP,_X:cueSIPPort,'cueJTAPIInfo':cueJTAPIInfo,'cueJTAPIServerTable':cueJTAPIServerTable,'cueJTAPIServerEntry':cueJTAPIServerEntry,_r:cueJTAPIServerIndex,_Y:cueJTAPIServerName,_Z:cueJTAPIServerIPType,_a:cueJTAPIServerIP,_b:cueJTAPISubsystemState,_c:cueJTAPIUsername,_d:cueJTAPISoftwareVersion,_e:cueJTAPIPortsRegistered,'cueSystemDefaults':cueSystemDefaults,_f:cueDefaultMailboxSize,_g:cueDefaultGreetingSize,_h:cueDefaultMessageSizeMax,_i:cueDefaultMessageExpiryTime,'cueUsage':cueUsage,'cueUsageScalars':cueUsageScalars,_w:cueLicensedPortsMax,_x:cueActiveCalls,_y:cuePersonalMailboxes,_z:cueGeneralDeliveryMailboxes,_A0:cueOrphanedMailboxes,_A1:cueCapacityOfVoicemail,_A2:cueAllocatedCapacity,_A3:cueTotalTimeUsed,_A4:cuePercentTimeUsed,_A5:cueMessageTimeUsed,_A6:cueMessageCount,_A7:cueAverageMessageLength,_A8:cueGreetingTimeUsed,_A9:cueGreetingCount,_AA:cueAverageGreetingLength,_AS:cueMessagesLeft,_AT:cueMessagesRetrieved,_AU:cueMessagesDeleted,_AV:cueLicensedMailboxesMax,_AW:cueMailboxesAbove90PercentFull,'cueMboxTable':cueMboxTable,'cueMboxEntry':cueMboxEntry,_t:cueMboxIndex,_AB:cueMboxOwner,_AC:cueMboxPrimaryExtension,_AD:cueMboxType,_AE:cueMboxDescription,_AF:cueMboxSize,_AG:cueMboxTimeUsed,_AH:cueMboxPercentTimeUsed,_AI:cueMboxNumberOfMessages,_AJ:cueMboxNumberOfNewMessages,_AK:cueMboxNumberOfSavedMessages,_AL:cueMboxMessageSizeMax,_AM:cueMboxMessageExpiryTime,_AN:cueMboxPlayTutorial,_AO:cueMboxGreetingType,_AP:cueMboxEnabled,_AQ:cueMboxBusy,_AR:cueMboxMWIState,'cueSecurity':cueSecurity,'cueLoginInfo':cueLoginInfo,_AX:cueLoginAttempts,_AY:cueLoginUsernameFailures,_AZ:cueLoginPasswordFailures,'cuePINInfo':cuePINInfo,_Aa:cuePINAttempts,_Ab:cuePINResets,_Ac:cuePINUidFailures,_Ad:cuePINPasswordFailures,'cueNotif':cueNotif,'cueNotifConfig':cueNotifConfig,_Ae:cueNotifEnable,'cueNotifInfo':cueNotifInfo,_I:cueNotifSeverity,_J:cueNotifDate,_K:cueNotifDescription,_L:cueNotifDetail,'cueNotifSecurity':cueNotifSecurity,_Af:cueLoginUsernameThresh,_Ag:cueLoginPasswordThresh,_Ah:cuePINUidThresh,_Ai:cuePINPasswordThresh,_Aj:cuePINResetThresh,'cueBackupRestore':cueBackupRestore,'cueBRHistoryTable':cueBRHistoryTable,'cueBRHistoryEntry':cueBRHistoryEntry,_u:cueBRHistoryIndex,_Ak:cueBRHistoryOperation,_Al:cueBRHistoryDate,_Am:cueBRHistoryResult,'ciscoUnityExpressMIBConform':ciscoUnityExpressMIBConform,'ciscoUnityExpressMIBCompliances':ciscoUnityExpressMIBCompliances,'ciscoUnityExpressMIBCompliance':ciscoUnityExpressMIBCompliance,'ciscoUnityExpressMIBComplianceRev1':ciscoUnityExpressMIBComplianceRev1,'ciscoUnityExpressMIBGroups':ciscoUnityExpressMIBGroups,_Au:cueSystemGroup,_j:cueUsageGroup,_k:cueSecurityGroup,_l:cueNotifGroup,_m:ciscoUnityExpressMIBNotificationsGroup,_n:cueBackupRestoreGroup,_Av:cueSystemGroupRev1})