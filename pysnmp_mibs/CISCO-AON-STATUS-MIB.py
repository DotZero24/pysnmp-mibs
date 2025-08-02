_A8='caonNotifEnableObjectsGroup'
_A7='caonSendThresholdExceededNotifObjectsGroup'
_A6='caonMessageDeliveryFailedNotifObjectsGroup'
_A5='caonCustomNotifObjectsGroup'
_A4='caonNotificationObjectGroup'
_A3='caonCustomNotifGroup'
_A2='caonMessageDeliveryFailedNotifGroup'
_A1='caonSendThresholdExceededNotifGroup'
_A0='caonNewPepDeployedNotifGroup'
_z='caonDownNotificationGroup'
_y='caonUpNotificationGroup'
_x='caonPepEndPointObjectGroup'
_w='caonPepObjectGroup'
_v='caonNodeObjectGroup'
_u='caonCustomNotification'
_t='caonMessageDeliveryFailed'
_s='caonSendResponseThresholdExceeded'
_r='caonNewPepDeployed'
_q='caonDown'
_p='caonUp'
_o='caonNotifEnableIndicators'
_n='caonEndPointAvgResponseTime'
_m='caonEndPointMaxResponseTime'
_l='caonEndPointMinResponseTime'
_k='caonReqResponseFailedMessages'
_j='caonReqResponseDeliveredMessages'
_i='caonOneWayFailedMessages'
_h='caonOneWayDeliveredMessages'
_g='caonEndPointAttemptedMessages'
_f='caonPepSecurityFailures'
_e='caonPepFailures'
_d='caonPepReceivedMessages'
_c='caonPepStyle'
_b='caonCounterDiscontinuityTime'
_a='caonPepCount'
_Z='caonAmcIpAddress'
_Y='caonAmcIpAddressType'
_X='caonReceivedMessages'
_W='caonLastActivateTime'
_V='caonBootTime'
_U='caonNodeState'
_T='caonPepEndPointIndex'
_S='not-accessible'
_R='caonSendResponseThreshold'
_Q='caonMessageSrcUri'
_P='caonNotificationText'
_O='caonPepName'
_N='caonPepIndex'
_M='messages'
_L='Unsigned32'
_K='Integer32'
_J='caonNotificationName'
_I='caonMessageSrcPort'
_H='caonMessageSrcIpAddress'
_G='caonMessageSrcIpAddressType'
_F='caonPepEndPointUrl'
_E='SnmpAdminString'
_D='accessible-for-notify'
_C='read-only'
_B='current'
_A='CISCO-AON-STATUS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoPort,CiscoURLString=mibBuilder.importSymbols('CISCO-TC','CiscoPort','CiscoURLString')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TimeStamp')
ciscoAonStatusMIB=ModuleIdentity((1,3,6,1,4,1,9,9,646))
if mibBuilder.loadTexts:ciscoAonStatusMIB.setRevisions(('2008-03-06 00:00',))
_CiscoAonStatusMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoAonStatusMIBNotifs=_CiscoAonStatusMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,646,0))
_CiscoAonStatusMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAonStatusMIBObjects=_CiscoAonStatusMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,646,1))
_CaonSystemInfo_ObjectIdentity=ObjectIdentity
caonSystemInfo=_CaonSystemInfo_ObjectIdentity((1,3,6,1,4,1,9,9,646,1,1))
class _CaonNodeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unregistered',1),('registered',2),('active',3),('inactive',4)))
_CaonNodeState_Type.__name__=_K
_CaonNodeState_Object=MibScalar
caonNodeState=_CaonNodeState_Object((1,3,6,1,4,1,9,9,646,1,1,1),_CaonNodeState_Type())
caonNodeState.setMaxAccess(_C)
if mibBuilder.loadTexts:caonNodeState.setStatus(_B)
_CaonBootTime_Type=TimeStamp
_CaonBootTime_Object=MibScalar
caonBootTime=_CaonBootTime_Object((1,3,6,1,4,1,9,9,646,1,1,2),_CaonBootTime_Type())
caonBootTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caonBootTime.setStatus(_B)
_CaonLastActivateTime_Type=DateAndTime
_CaonLastActivateTime_Object=MibScalar
caonLastActivateTime=_CaonLastActivateTime_Object((1,3,6,1,4,1,9,9,646,1,1,3),_CaonLastActivateTime_Type())
caonLastActivateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caonLastActivateTime.setStatus(_B)
_CaonReceivedMessages_Type=Counter32
_CaonReceivedMessages_Object=MibScalar
caonReceivedMessages=_CaonReceivedMessages_Object((1,3,6,1,4,1,9,9,646,1,1,4),_CaonReceivedMessages_Type())
caonReceivedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonReceivedMessages.setStatus(_B)
if mibBuilder.loadTexts:caonReceivedMessages.setUnits(_M)
_CaonAmcIpAddressType_Type=InetAddressType
_CaonAmcIpAddressType_Object=MibScalar
caonAmcIpAddressType=_CaonAmcIpAddressType_Object((1,3,6,1,4,1,9,9,646,1,1,5),_CaonAmcIpAddressType_Type())
caonAmcIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:caonAmcIpAddressType.setStatus(_B)
_CaonAmcIpAddress_Type=InetAddress
_CaonAmcIpAddress_Object=MibScalar
caonAmcIpAddress=_CaonAmcIpAddress_Object((1,3,6,1,4,1,9,9,646,1,1,6),_CaonAmcIpAddress_Type())
caonAmcIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:caonAmcIpAddress.setStatus(_B)
_CaonPepCount_Type=Gauge32
_CaonPepCount_Object=MibScalar
caonPepCount=_CaonPepCount_Object((1,3,6,1,4,1,9,9,646,1,1,7),_CaonPepCount_Type())
caonPepCount.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepCount.setStatus(_B)
if mibBuilder.loadTexts:caonPepCount.setUnits('PEPs')
_CaonPepTable_Object=MibTable
caonPepTable=_CaonPepTable_Object((1,3,6,1,4,1,9,9,646,1,1,8))
if mibBuilder.loadTexts:caonPepTable.setStatus(_B)
_CaonPepEntry_Object=MibTableRow
caonPepEntry=_CaonPepEntry_Object((1,3,6,1,4,1,9,9,646,1,1,8,1))
caonPepEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:caonPepEntry.setStatus(_B)
class _CaonPepIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CaonPepIndex_Type.__name__=_L
_CaonPepIndex_Object=MibTableColumn
caonPepIndex=_CaonPepIndex_Object((1,3,6,1,4,1,9,9,646,1,1,8,1,1),_CaonPepIndex_Type())
caonPepIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:caonPepIndex.setStatus(_B)
class _CaonPepName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CaonPepName_Type.__name__=_E
_CaonPepName_Object=MibTableColumn
caonPepName=_CaonPepName_Object((1,3,6,1,4,1,9,9,646,1,1,8,1,2),_CaonPepName_Type())
caonPepName.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepName.setStatus(_B)
class _CaonPepStyle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneWay',1),('requestResponse',2)))
_CaonPepStyle_Type.__name__=_K
_CaonPepStyle_Object=MibTableColumn
caonPepStyle=_CaonPepStyle_Object((1,3,6,1,4,1,9,9,646,1,1,8,1,3),_CaonPepStyle_Type())
caonPepStyle.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepStyle.setStatus(_B)
_CaonPepReceivedMessages_Type=Counter32
_CaonPepReceivedMessages_Object=MibTableColumn
caonPepReceivedMessages=_CaonPepReceivedMessages_Object((1,3,6,1,4,1,9,9,646,1,1,8,1,4),_CaonPepReceivedMessages_Type())
caonPepReceivedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepReceivedMessages.setStatus(_B)
_CaonPepFailures_Type=Counter32
_CaonPepFailures_Object=MibTableColumn
caonPepFailures=_CaonPepFailures_Object((1,3,6,1,4,1,9,9,646,1,1,8,1,5),_CaonPepFailures_Type())
caonPepFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepFailures.setStatus(_B)
_CaonPepSecurityFailures_Type=Counter32
_CaonPepSecurityFailures_Object=MibTableColumn
caonPepSecurityFailures=_CaonPepSecurityFailures_Object((1,3,6,1,4,1,9,9,646,1,1,8,1,6),_CaonPepSecurityFailures_Type())
caonPepSecurityFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepSecurityFailures.setStatus(_B)
_CaonPepEndPointTable_Object=MibTable
caonPepEndPointTable=_CaonPepEndPointTable_Object((1,3,6,1,4,1,9,9,646,1,1,10))
if mibBuilder.loadTexts:caonPepEndPointTable.setStatus(_B)
_CaonPepEndPointEntry_Object=MibTableRow
caonPepEndPointEntry=_CaonPepEndPointEntry_Object((1,3,6,1,4,1,9,9,646,1,1,10,1))
caonPepEndPointEntry.setIndexNames((0,_A,_N),(0,_A,_T))
if mibBuilder.loadTexts:caonPepEndPointEntry.setStatus(_B)
class _CaonPepEndPointIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_CaonPepEndPointIndex_Type.__name__=_L
_CaonPepEndPointIndex_Object=MibTableColumn
caonPepEndPointIndex=_CaonPepEndPointIndex_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,1),_CaonPepEndPointIndex_Type())
caonPepEndPointIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:caonPepEndPointIndex.setStatus(_B)
_CaonPepEndPointUrl_Type=CiscoURLString
_CaonPepEndPointUrl_Object=MibTableColumn
caonPepEndPointUrl=_CaonPepEndPointUrl_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,2),_CaonPepEndPointUrl_Type())
caonPepEndPointUrl.setMaxAccess(_C)
if mibBuilder.loadTexts:caonPepEndPointUrl.setStatus(_B)
_CaonEndPointAttemptedMessages_Type=Counter32
_CaonEndPointAttemptedMessages_Object=MibTableColumn
caonEndPointAttemptedMessages=_CaonEndPointAttemptedMessages_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,3),_CaonEndPointAttemptedMessages_Type())
caonEndPointAttemptedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonEndPointAttemptedMessages.setStatus(_B)
_CaonOneWayDeliveredMessages_Type=Counter32
_CaonOneWayDeliveredMessages_Object=MibTableColumn
caonOneWayDeliveredMessages=_CaonOneWayDeliveredMessages_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,4),_CaonOneWayDeliveredMessages_Type())
caonOneWayDeliveredMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonOneWayDeliveredMessages.setStatus(_B)
_CaonOneWayFailedMessages_Type=Counter32
_CaonOneWayFailedMessages_Object=MibTableColumn
caonOneWayFailedMessages=_CaonOneWayFailedMessages_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,5),_CaonOneWayFailedMessages_Type())
caonOneWayFailedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonOneWayFailedMessages.setStatus(_B)
_CaonReqResponseDeliveredMessages_Type=Counter32
_CaonReqResponseDeliveredMessages_Object=MibTableColumn
caonReqResponseDeliveredMessages=_CaonReqResponseDeliveredMessages_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,6),_CaonReqResponseDeliveredMessages_Type())
caonReqResponseDeliveredMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonReqResponseDeliveredMessages.setStatus(_B)
if mibBuilder.loadTexts:caonReqResponseDeliveredMessages.setUnits(_M)
_CaonReqResponseFailedMessages_Type=Counter32
_CaonReqResponseFailedMessages_Object=MibTableColumn
caonReqResponseFailedMessages=_CaonReqResponseFailedMessages_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,7),_CaonReqResponseFailedMessages_Type())
caonReqResponseFailedMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:caonReqResponseFailedMessages.setStatus(_B)
if mibBuilder.loadTexts:caonReqResponseFailedMessages.setUnits(_M)
_CaonEndPointMinResponseTime_Type=TimeTicks
_CaonEndPointMinResponseTime_Object=MibTableColumn
caonEndPointMinResponseTime=_CaonEndPointMinResponseTime_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,8),_CaonEndPointMinResponseTime_Type())
caonEndPointMinResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caonEndPointMinResponseTime.setStatus(_B)
_CaonEndPointMaxResponseTime_Type=TimeTicks
_CaonEndPointMaxResponseTime_Object=MibTableColumn
caonEndPointMaxResponseTime=_CaonEndPointMaxResponseTime_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,9),_CaonEndPointMaxResponseTime_Type())
caonEndPointMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caonEndPointMaxResponseTime.setStatus(_B)
_CaonEndPointAvgResponseTime_Type=TimeTicks
_CaonEndPointAvgResponseTime_Object=MibTableColumn
caonEndPointAvgResponseTime=_CaonEndPointAvgResponseTime_Object((1,3,6,1,4,1,9,9,646,1,1,10,1,10),_CaonEndPointAvgResponseTime_Type())
caonEndPointAvgResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caonEndPointAvgResponseTime.setStatus(_B)
_CaonCounterDiscontinuityTime_Type=TimeStamp
_CaonCounterDiscontinuityTime_Object=MibScalar
caonCounterDiscontinuityTime=_CaonCounterDiscontinuityTime_Object((1,3,6,1,4,1,9,9,646,1,1,11),_CaonCounterDiscontinuityTime_Type())
caonCounterDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:caonCounterDiscontinuityTime.setStatus(_B)
_CaonNotificationInfo_ObjectIdentity=ObjectIdentity
caonNotificationInfo=_CaonNotificationInfo_ObjectIdentity((1,3,6,1,4,1,9,9,646,1,2))
class _CaonMessageSrcUri_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CaonMessageSrcUri_Type.__name__=_E
_CaonMessageSrcUri_Object=MibScalar
caonMessageSrcUri=_CaonMessageSrcUri_Object((1,3,6,1,4,1,9,9,646,1,2,1),_CaonMessageSrcUri_Type())
caonMessageSrcUri.setMaxAccess(_D)
if mibBuilder.loadTexts:caonMessageSrcUri.setStatus(_B)
_CaonMessageSrcIpAddressType_Type=InetAddressType
_CaonMessageSrcIpAddressType_Object=MibScalar
caonMessageSrcIpAddressType=_CaonMessageSrcIpAddressType_Object((1,3,6,1,4,1,9,9,646,1,2,2),_CaonMessageSrcIpAddressType_Type())
caonMessageSrcIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:caonMessageSrcIpAddressType.setStatus(_B)
_CaonMessageSrcIpAddress_Type=InetAddress
_CaonMessageSrcIpAddress_Object=MibScalar
caonMessageSrcIpAddress=_CaonMessageSrcIpAddress_Object((1,3,6,1,4,1,9,9,646,1,2,3),_CaonMessageSrcIpAddress_Type())
caonMessageSrcIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:caonMessageSrcIpAddress.setStatus(_B)
_CaonMessageSrcPort_Type=CiscoPort
_CaonMessageSrcPort_Object=MibScalar
caonMessageSrcPort=_CaonMessageSrcPort_Object((1,3,6,1,4,1,9,9,646,1,2,4),_CaonMessageSrcPort_Type())
caonMessageSrcPort.setMaxAccess(_D)
if mibBuilder.loadTexts:caonMessageSrcPort.setStatus(_B)
class _CaonNotificationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CaonNotificationName_Type.__name__=_E
_CaonNotificationName_Object=MibScalar
caonNotificationName=_CaonNotificationName_Object((1,3,6,1,4,1,9,9,646,1,2,5),_CaonNotificationName_Type())
caonNotificationName.setMaxAccess(_D)
if mibBuilder.loadTexts:caonNotificationName.setStatus(_B)
class _CaonNotificationText_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CaonNotificationText_Type.__name__=_E
_CaonNotificationText_Object=MibScalar
caonNotificationText=_CaonNotificationText_Object((1,3,6,1,4,1,9,9,646,1,2,6),_CaonNotificationText_Type())
caonNotificationText.setMaxAccess(_D)
if mibBuilder.loadTexts:caonNotificationText.setStatus(_B)
_CaonSendResponseThreshold_Type=TimeTicks
_CaonSendResponseThreshold_Object=MibScalar
caonSendResponseThreshold=_CaonSendResponseThreshold_Object((1,3,6,1,4,1,9,9,646,1,2,7),_CaonSendResponseThreshold_Type())
caonSendResponseThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:caonSendResponseThreshold.setStatus(_B)
class _CaonNotifEnableIndicators_Type(Bits):namedValues=NamedValues(*(('caonUpNotifEnabled',0),('caonDownNotifEnabled',1),('caonNewPepDeployedNotifEnabled',2),('caonMessageDeliveryFailedNotifEnabled',3),('caonSendResponseThresholdExceededNotifEnabled',4),('caonCustomNotifEnabled',5)))
_CaonNotifEnableIndicators_Type.__name__='Bits'
_CaonNotifEnableIndicators_Object=MibScalar
caonNotifEnableIndicators=_CaonNotifEnableIndicators_Object((1,3,6,1,4,1,9,9,646,1,2,8),_CaonNotifEnableIndicators_Type())
caonNotifEnableIndicators.setMaxAccess('read-write')
if mibBuilder.loadTexts:caonNotifEnableIndicators.setStatus(_B)
_CiscoAonStatusMIBConform_ObjectIdentity=ObjectIdentity
ciscoAonStatusMIBConform=_CiscoAonStatusMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,646,2))
_CiscoAonStatusMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAonStatusMIBCompliances=_CiscoAonStatusMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,646,2,1))
_CiscoAonStatusMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAonStatusMIBGroups=_CiscoAonStatusMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,646,2,2))
caonNodeObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,1))
caonNodeObjectGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:caonNodeObjectGroup.setStatus(_B)
caonPepObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,2))
caonPepObjectGroup.setObjects(*((_A,_O),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:caonPepObjectGroup.setStatus(_B)
caonPepEndPointObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,3))
caonPepEndPointObjectGroup.setObjects(*((_A,_F),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:caonPepEndPointObjectGroup.setStatus(_B)
caonNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,4))
caonNotificationObjectGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:caonNotificationObjectGroup.setStatus(_B)
caonCustomNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,11))
caonCustomNotifObjectsGroup.setObjects(*((_A,_J),(_A,_P)))
if mibBuilder.loadTexts:caonCustomNotifObjectsGroup.setStatus(_B)
caonMessageDeliveryFailedNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,12))
caonMessageDeliveryFailedNotifObjectsGroup.setObjects(*((_A,_Q),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:caonMessageDeliveryFailedNotifObjectsGroup.setStatus(_B)
caonNotifEnableObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,13))
caonNotifEnableObjectsGroup.setObjects((_A,_o))
if mibBuilder.loadTexts:caonNotifEnableObjectsGroup.setStatus(_B)
caonSendThresholdExceededNotifObjectsGroup=ObjectGroup((1,3,6,1,4,1,9,9,646,2,2,14))
caonSendThresholdExceededNotifObjectsGroup.setObjects((_A,_R))
if mibBuilder.loadTexts:caonSendThresholdExceededNotifObjectsGroup.setStatus(_B)
caonUp=NotificationType((1,3,6,1,4,1,9,9,646,0,1))
if mibBuilder.loadTexts:caonUp.setStatus(_B)
caonDown=NotificationType((1,3,6,1,4,1,9,9,646,0,2))
if mibBuilder.loadTexts:caonDown.setStatus(_B)
caonNewPepDeployed=NotificationType((1,3,6,1,4,1,9,9,646,0,3))
caonNewPepDeployed.setObjects((_A,_O))
if mibBuilder.loadTexts:caonNewPepDeployed.setStatus(_B)
caonMessageDeliveryFailed=NotificationType((1,3,6,1,4,1,9,9,646,0,4))
caonMessageDeliveryFailed.setObjects(*((_A,_F),(_A,_Q),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:caonMessageDeliveryFailed.setStatus(_B)
caonSendResponseThresholdExceeded=NotificationType((1,3,6,1,4,1,9,9,646,0,5))
caonSendResponseThresholdExceeded.setObjects(*((_A,_F),(_A,_R)))
if mibBuilder.loadTexts:caonSendResponseThresholdExceeded.setStatus(_B)
caonCustomNotification=NotificationType((1,3,6,1,4,1,9,9,646,0,6))
caonCustomNotification.setObjects(*((_A,_J),(_A,_P)))
if mibBuilder.loadTexts:caonCustomNotification.setStatus(_B)
caonUpNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,646,2,2,5))
caonUpNotificationGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:caonUpNotificationGroup.setStatus(_B)
caonDownNotificationGroup=NotificationGroup((1,3,6,1,4,1,9,9,646,2,2,6))
caonDownNotificationGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:caonDownNotificationGroup.setStatus(_B)
caonNewPepDeployedNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,646,2,2,7))
caonNewPepDeployedNotifGroup.setObjects((_A,_r))
if mibBuilder.loadTexts:caonNewPepDeployedNotifGroup.setStatus(_B)
caonSendThresholdExceededNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,646,2,2,8))
caonSendThresholdExceededNotifGroup.setObjects((_A,_s))
if mibBuilder.loadTexts:caonSendThresholdExceededNotifGroup.setStatus(_B)
caonMessageDeliveryFailedNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,646,2,2,9))
caonMessageDeliveryFailedNotifGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:caonMessageDeliveryFailedNotifGroup.setStatus(_B)
caonCustomNotifGroup=NotificationGroup((1,3,6,1,4,1,9,9,646,2,2,10))
caonCustomNotifGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:caonCustomNotifGroup.setStatus(_B)
ciscoAonStatusMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,646,2,1,1))
ciscoAonStatusMIBCompliance.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:ciscoAonStatusMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoAonStatusMIB':ciscoAonStatusMIB,'ciscoAonStatusMIBNotifs':ciscoAonStatusMIBNotifs,_p:caonUp,_q:caonDown,_r:caonNewPepDeployed,_t:caonMessageDeliveryFailed,_s:caonSendResponseThresholdExceeded,_u:caonCustomNotification,'ciscoAonStatusMIBObjects':ciscoAonStatusMIBObjects,'caonSystemInfo':caonSystemInfo,_U:caonNodeState,_V:caonBootTime,_W:caonLastActivateTime,_X:caonReceivedMessages,_Y:caonAmcIpAddressType,_Z:caonAmcIpAddress,_a:caonPepCount,'caonPepTable':caonPepTable,'caonPepEntry':caonPepEntry,_N:caonPepIndex,_O:caonPepName,_c:caonPepStyle,_d:caonPepReceivedMessages,_e:caonPepFailures,_f:caonPepSecurityFailures,'caonPepEndPointTable':caonPepEndPointTable,'caonPepEndPointEntry':caonPepEndPointEntry,_T:caonPepEndPointIndex,_F:caonPepEndPointUrl,_g:caonEndPointAttemptedMessages,_h:caonOneWayDeliveredMessages,_i:caonOneWayFailedMessages,_j:caonReqResponseDeliveredMessages,_k:caonReqResponseFailedMessages,_l:caonEndPointMinResponseTime,_m:caonEndPointMaxResponseTime,_n:caonEndPointAvgResponseTime,_b:caonCounterDiscontinuityTime,'caonNotificationInfo':caonNotificationInfo,_Q:caonMessageSrcUri,_G:caonMessageSrcIpAddressType,_H:caonMessageSrcIpAddress,_I:caonMessageSrcPort,_J:caonNotificationName,_P:caonNotificationText,_R:caonSendResponseThreshold,_o:caonNotifEnableIndicators,'ciscoAonStatusMIBConform':ciscoAonStatusMIBConform,'ciscoAonStatusMIBCompliances':ciscoAonStatusMIBCompliances,'ciscoAonStatusMIBCompliance':ciscoAonStatusMIBCompliance,'ciscoAonStatusMIBGroups':ciscoAonStatusMIBGroups,_v:caonNodeObjectGroup,_w:caonPepObjectGroup,_x:caonPepEndPointObjectGroup,_A4:caonNotificationObjectGroup,_y:caonUpNotificationGroup,_z:caonDownNotificationGroup,_A0:caonNewPepDeployedNotifGroup,_A1:caonSendThresholdExceededNotifGroup,_A2:caonMessageDeliveryFailedNotifGroup,_A3:caonCustomNotifGroup,_A5:caonCustomNotifObjectsGroup,_A6:caonMessageDeliveryFailedNotifObjectsGroup,_A8:caonNotifEnableObjectsGroup,_A7:caonSendThresholdExceededNotifObjectsGroup})