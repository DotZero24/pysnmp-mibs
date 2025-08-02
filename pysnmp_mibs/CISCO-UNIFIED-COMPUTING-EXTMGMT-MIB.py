_J='cucsExtmgmtNdiscTargetsInstanceId'
_I='cucsExtmgmtMiiStatusInstanceId'
_H='cucsExtmgmtIfMonPolicyInstanceId'
_G='cucsExtmgmtIfInstanceId'
_F='cucsExtmgmtGatewayPingInstanceId'
_E='cucsExtmgmtArpTargetsInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-EXTMGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsAaaConfigState,CucsExtmgmtArpTargetsMaxDeadlineTimeout,CucsExtmgmtArpTargetsNumberOfArpRequests,CucsExtmgmtGatewayPingMaxDeadlineTimeout,CucsExtmgmtGatewayPingNumberOfPingRequests,CucsExtmgmtIfMonPolicyAdminState,CucsExtmgmtIfMonPolicyMonitorMechanism,CucsExtmgmtMiiStatusMaxRetryCount,CucsExtmgmtMiiStatusRetryInterval,CucsExtmgmtNdiscTargetsMaxDeadlineTimeout,CucsExtmgmtNdiscTargetsNumberOfNdiscRequests,CucsNetworkConnectionType,CucsNetworkIfStatus,CucsNetworkLocale,CucsNetworkPortRole,CucsNetworkPortType,CucsNetworkSwitchId,CucsNetworkTransport,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsAaaConfigState','CucsExtmgmtArpTargetsMaxDeadlineTimeout','CucsExtmgmtArpTargetsNumberOfArpRequests','CucsExtmgmtGatewayPingMaxDeadlineTimeout','CucsExtmgmtGatewayPingNumberOfPingRequests','CucsExtmgmtIfMonPolicyAdminState','CucsExtmgmtIfMonPolicyMonitorMechanism','CucsExtmgmtMiiStatusMaxRetryCount','CucsExtmgmtMiiStatusRetryInterval','CucsExtmgmtNdiscTargetsMaxDeadlineTimeout','CucsExtmgmtNdiscTargetsNumberOfNdiscRequests','CucsNetworkConnectionType','CucsNetworkIfStatus','CucsNetworkLocale','CucsNetworkPortRole','CucsNetworkPortType','CucsNetworkSwitchId','CucsNetworkTransport','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsExtmgmtObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,57))
_CucsExtmgmtArpTargetsTable_Object=MibTable
cucsExtmgmtArpTargetsTable=_CucsExtmgmtArpTargetsTable_Object((1,3,6,1,4,1,9,9,719,1,57,1))
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsTable.setStatus(_A)
_CucsExtmgmtArpTargetsEntry_Object=MibTableRow
cucsExtmgmtArpTargetsEntry=_CucsExtmgmtArpTargetsEntry_Object((1,3,6,1,4,1,9,9,719,1,57,1,1))
cucsExtmgmtArpTargetsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsEntry.setStatus(_A)
_CucsExtmgmtArpTargetsInstanceId_Type=CucsManagedObjectId
_CucsExtmgmtArpTargetsInstanceId_Object=MibTableColumn
cucsExtmgmtArpTargetsInstanceId=_CucsExtmgmtArpTargetsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,1),_CucsExtmgmtArpTargetsInstanceId_Type())
cucsExtmgmtArpTargetsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsInstanceId.setStatus(_A)
_CucsExtmgmtArpTargetsDn_Type=CucsManagedObjectDn
_CucsExtmgmtArpTargetsDn_Object=MibTableColumn
cucsExtmgmtArpTargetsDn=_CucsExtmgmtArpTargetsDn_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,2),_CucsExtmgmtArpTargetsDn_Type())
cucsExtmgmtArpTargetsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsDn.setStatus(_A)
_CucsExtmgmtArpTargetsRn_Type=SnmpAdminString
_CucsExtmgmtArpTargetsRn_Object=MibTableColumn
cucsExtmgmtArpTargetsRn=_CucsExtmgmtArpTargetsRn_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,3),_CucsExtmgmtArpTargetsRn_Type())
cucsExtmgmtArpTargetsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsRn.setStatus(_A)
_CucsExtmgmtArpTargetsMaxDeadlineTimeout_Type=CucsExtmgmtArpTargetsMaxDeadlineTimeout
_CucsExtmgmtArpTargetsMaxDeadlineTimeout_Object=MibTableColumn
cucsExtmgmtArpTargetsMaxDeadlineTimeout=_CucsExtmgmtArpTargetsMaxDeadlineTimeout_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,4),_CucsExtmgmtArpTargetsMaxDeadlineTimeout_Type())
cucsExtmgmtArpTargetsMaxDeadlineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsMaxDeadlineTimeout.setStatus(_A)
_CucsExtmgmtArpTargetsNumberOfArpRequests_Type=CucsExtmgmtArpTargetsNumberOfArpRequests
_CucsExtmgmtArpTargetsNumberOfArpRequests_Object=MibTableColumn
cucsExtmgmtArpTargetsNumberOfArpRequests=_CucsExtmgmtArpTargetsNumberOfArpRequests_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,5),_CucsExtmgmtArpTargetsNumberOfArpRequests_Type())
cucsExtmgmtArpTargetsNumberOfArpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsNumberOfArpRequests.setStatus(_A)
_CucsExtmgmtArpTargetsTargetIp1_Type=InetAddressIPv4
_CucsExtmgmtArpTargetsTargetIp1_Object=MibTableColumn
cucsExtmgmtArpTargetsTargetIp1=_CucsExtmgmtArpTargetsTargetIp1_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,6),_CucsExtmgmtArpTargetsTargetIp1_Type())
cucsExtmgmtArpTargetsTargetIp1.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsTargetIp1.setStatus(_A)
_CucsExtmgmtArpTargetsTargetIp2_Type=InetAddressIPv4
_CucsExtmgmtArpTargetsTargetIp2_Object=MibTableColumn
cucsExtmgmtArpTargetsTargetIp2=_CucsExtmgmtArpTargetsTargetIp2_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,7),_CucsExtmgmtArpTargetsTargetIp2_Type())
cucsExtmgmtArpTargetsTargetIp2.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsTargetIp2.setStatus(_A)
_CucsExtmgmtArpTargetsTargetIp3_Type=InetAddressIPv4
_CucsExtmgmtArpTargetsTargetIp3_Object=MibTableColumn
cucsExtmgmtArpTargetsTargetIp3=_CucsExtmgmtArpTargetsTargetIp3_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,8),_CucsExtmgmtArpTargetsTargetIp3_Type())
cucsExtmgmtArpTargetsTargetIp3.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsTargetIp3.setStatus(_A)
_CucsExtmgmtArpTargetsConfigState_Type=CucsAaaConfigState
_CucsExtmgmtArpTargetsConfigState_Object=MibTableColumn
cucsExtmgmtArpTargetsConfigState=_CucsExtmgmtArpTargetsConfigState_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,9),_CucsExtmgmtArpTargetsConfigState_Type())
cucsExtmgmtArpTargetsConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsConfigState.setStatus(_A)
_CucsExtmgmtArpTargetsConfigStatusMessage_Type=SnmpAdminString
_CucsExtmgmtArpTargetsConfigStatusMessage_Object=MibTableColumn
cucsExtmgmtArpTargetsConfigStatusMessage=_CucsExtmgmtArpTargetsConfigStatusMessage_Object((1,3,6,1,4,1,9,9,719,1,57,1,1,10),_CucsExtmgmtArpTargetsConfigStatusMessage_Type())
cucsExtmgmtArpTargetsConfigStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtArpTargetsConfigStatusMessage.setStatus(_A)
_CucsExtmgmtGatewayPingTable_Object=MibTable
cucsExtmgmtGatewayPingTable=_CucsExtmgmtGatewayPingTable_Object((1,3,6,1,4,1,9,9,719,1,57,2))
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingTable.setStatus(_A)
_CucsExtmgmtGatewayPingEntry_Object=MibTableRow
cucsExtmgmtGatewayPingEntry=_CucsExtmgmtGatewayPingEntry_Object((1,3,6,1,4,1,9,9,719,1,57,2,1))
cucsExtmgmtGatewayPingEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingEntry.setStatus(_A)
_CucsExtmgmtGatewayPingInstanceId_Type=CucsManagedObjectId
_CucsExtmgmtGatewayPingInstanceId_Object=MibTableColumn
cucsExtmgmtGatewayPingInstanceId=_CucsExtmgmtGatewayPingInstanceId_Object((1,3,6,1,4,1,9,9,719,1,57,2,1,1),_CucsExtmgmtGatewayPingInstanceId_Type())
cucsExtmgmtGatewayPingInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingInstanceId.setStatus(_A)
_CucsExtmgmtGatewayPingDn_Type=CucsManagedObjectDn
_CucsExtmgmtGatewayPingDn_Object=MibTableColumn
cucsExtmgmtGatewayPingDn=_CucsExtmgmtGatewayPingDn_Object((1,3,6,1,4,1,9,9,719,1,57,2,1,2),_CucsExtmgmtGatewayPingDn_Type())
cucsExtmgmtGatewayPingDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingDn.setStatus(_A)
_CucsExtmgmtGatewayPingRn_Type=SnmpAdminString
_CucsExtmgmtGatewayPingRn_Object=MibTableColumn
cucsExtmgmtGatewayPingRn=_CucsExtmgmtGatewayPingRn_Object((1,3,6,1,4,1,9,9,719,1,57,2,1,3),_CucsExtmgmtGatewayPingRn_Type())
cucsExtmgmtGatewayPingRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingRn.setStatus(_A)
_CucsExtmgmtGatewayPingMaxDeadlineTimeout_Type=CucsExtmgmtGatewayPingMaxDeadlineTimeout
_CucsExtmgmtGatewayPingMaxDeadlineTimeout_Object=MibTableColumn
cucsExtmgmtGatewayPingMaxDeadlineTimeout=_CucsExtmgmtGatewayPingMaxDeadlineTimeout_Object((1,3,6,1,4,1,9,9,719,1,57,2,1,4),_CucsExtmgmtGatewayPingMaxDeadlineTimeout_Type())
cucsExtmgmtGatewayPingMaxDeadlineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingMaxDeadlineTimeout.setStatus(_A)
_CucsExtmgmtGatewayPingNumberOfPingRequests_Type=CucsExtmgmtGatewayPingNumberOfPingRequests
_CucsExtmgmtGatewayPingNumberOfPingRequests_Object=MibTableColumn
cucsExtmgmtGatewayPingNumberOfPingRequests=_CucsExtmgmtGatewayPingNumberOfPingRequests_Object((1,3,6,1,4,1,9,9,719,1,57,2,1,5),_CucsExtmgmtGatewayPingNumberOfPingRequests_Type())
cucsExtmgmtGatewayPingNumberOfPingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtGatewayPingNumberOfPingRequests.setStatus(_A)
_CucsExtmgmtIfTable_Object=MibTable
cucsExtmgmtIfTable=_CucsExtmgmtIfTable_Object((1,3,6,1,4,1,9,9,719,1,57,3))
if mibBuilder.loadTexts:cucsExtmgmtIfTable.setStatus(_A)
_CucsExtmgmtIfEntry_Object=MibTableRow
cucsExtmgmtIfEntry=_CucsExtmgmtIfEntry_Object((1,3,6,1,4,1,9,9,719,1,57,3,1))
cucsExtmgmtIfEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsExtmgmtIfEntry.setStatus(_A)
_CucsExtmgmtIfInstanceId_Type=CucsManagedObjectId
_CucsExtmgmtIfInstanceId_Object=MibTableColumn
cucsExtmgmtIfInstanceId=_CucsExtmgmtIfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,1),_CucsExtmgmtIfInstanceId_Type())
cucsExtmgmtIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtmgmtIfInstanceId.setStatus(_A)
_CucsExtmgmtIfDn_Type=CucsManagedObjectDn
_CucsExtmgmtIfDn_Object=MibTableColumn
cucsExtmgmtIfDn=_CucsExtmgmtIfDn_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,2),_CucsExtmgmtIfDn_Type())
cucsExtmgmtIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfDn.setStatus(_A)
_CucsExtmgmtIfRn_Type=SnmpAdminString
_CucsExtmgmtIfRn_Object=MibTableColumn
cucsExtmgmtIfRn=_CucsExtmgmtIfRn_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,3),_CucsExtmgmtIfRn_Type())
cucsExtmgmtIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfRn.setStatus(_A)
_CucsExtmgmtIfEpDn_Type=SnmpAdminString
_CucsExtmgmtIfEpDn_Object=MibTableColumn
cucsExtmgmtIfEpDn=_CucsExtmgmtIfEpDn_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,4),_CucsExtmgmtIfEpDn_Type())
cucsExtmgmtIfEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfEpDn.setStatus(_A)
_CucsExtmgmtIfFailReportCount_Type=Gauge32
_CucsExtmgmtIfFailReportCount_Object=MibTableColumn
cucsExtmgmtIfFailReportCount=_CucsExtmgmtIfFailReportCount_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,5),_CucsExtmgmtIfFailReportCount_Type())
cucsExtmgmtIfFailReportCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfFailReportCount.setStatus(_A)
_CucsExtmgmtIfFltAggr_Type=Unsigned64
_CucsExtmgmtIfFltAggr_Object=MibTableColumn
cucsExtmgmtIfFltAggr=_CucsExtmgmtIfFltAggr_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,6),_CucsExtmgmtIfFltAggr_Type())
cucsExtmgmtIfFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfFltAggr.setStatus(_A)
_CucsExtmgmtIfId_Type=CucsNetworkSwitchId
_CucsExtmgmtIfId_Object=MibTableColumn
cucsExtmgmtIfId=_CucsExtmgmtIfId_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,7),_CucsExtmgmtIfId_Type())
cucsExtmgmtIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfId.setStatus(_A)
_CucsExtmgmtIfIfRole_Type=CucsNetworkPortRole
_CucsExtmgmtIfIfRole_Object=MibTableColumn
cucsExtmgmtIfIfRole=_CucsExtmgmtIfIfRole_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,8),_CucsExtmgmtIfIfRole_Type())
cucsExtmgmtIfIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfIfRole.setStatus(_A)
_CucsExtmgmtIfIfType_Type=CucsNetworkPortType
_CucsExtmgmtIfIfType_Object=MibTableColumn
cucsExtmgmtIfIfType=_CucsExtmgmtIfIfType_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,9),_CucsExtmgmtIfIfType_Type())
cucsExtmgmtIfIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfIfType.setStatus(_A)
_CucsExtmgmtIfLastOperStateReport_Type=CucsNetworkIfStatus
_CucsExtmgmtIfLastOperStateReport_Object=MibTableColumn
cucsExtmgmtIfLastOperStateReport=_CucsExtmgmtIfLastOperStateReport_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,10),_CucsExtmgmtIfLastOperStateReport_Type())
cucsExtmgmtIfLastOperStateReport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfLastOperStateReport.setStatus(_A)
_CucsExtmgmtIfLocale_Type=CucsNetworkLocale
_CucsExtmgmtIfLocale_Object=MibTableColumn
cucsExtmgmtIfLocale=_CucsExtmgmtIfLocale_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,11),_CucsExtmgmtIfLocale_Type())
cucsExtmgmtIfLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfLocale.setStatus(_A)
_CucsExtmgmtIfName_Type=SnmpAdminString
_CucsExtmgmtIfName_Object=MibTableColumn
cucsExtmgmtIfName=_CucsExtmgmtIfName_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,12),_CucsExtmgmtIfName_Type())
cucsExtmgmtIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfName.setStatus(_A)
_CucsExtmgmtIfOperState_Type=CucsNetworkIfStatus
_CucsExtmgmtIfOperState_Object=MibTableColumn
cucsExtmgmtIfOperState=_CucsExtmgmtIfOperState_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,13),_CucsExtmgmtIfOperState_Type())
cucsExtmgmtIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfOperState.setStatus(_A)
_CucsExtmgmtIfPeerDn_Type=SnmpAdminString
_CucsExtmgmtIfPeerDn_Object=MibTableColumn
cucsExtmgmtIfPeerDn=_CucsExtmgmtIfPeerDn_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,14),_CucsExtmgmtIfPeerDn_Type())
cucsExtmgmtIfPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfPeerDn.setStatus(_A)
_CucsExtmgmtIfTransport_Type=CucsNetworkTransport
_CucsExtmgmtIfTransport_Object=MibTableColumn
cucsExtmgmtIfTransport=_CucsExtmgmtIfTransport_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,15),_CucsExtmgmtIfTransport_Type())
cucsExtmgmtIfTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfTransport.setStatus(_A)
_CucsExtmgmtIfType_Type=CucsNetworkConnectionType
_CucsExtmgmtIfType_Object=MibTableColumn
cucsExtmgmtIfType=_CucsExtmgmtIfType_Object((1,3,6,1,4,1,9,9,719,1,57,3,1,16),_CucsExtmgmtIfType_Type())
cucsExtmgmtIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfType.setStatus(_A)
_CucsExtmgmtIfMonPolicyTable_Object=MibTable
cucsExtmgmtIfMonPolicyTable=_CucsExtmgmtIfMonPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,57,4))
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyTable.setStatus(_A)
_CucsExtmgmtIfMonPolicyEntry_Object=MibTableRow
cucsExtmgmtIfMonPolicyEntry=_CucsExtmgmtIfMonPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,57,4,1))
cucsExtmgmtIfMonPolicyEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyEntry.setStatus(_A)
_CucsExtmgmtIfMonPolicyInstanceId_Type=CucsManagedObjectId
_CucsExtmgmtIfMonPolicyInstanceId_Object=MibTableColumn
cucsExtmgmtIfMonPolicyInstanceId=_CucsExtmgmtIfMonPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,1),_CucsExtmgmtIfMonPolicyInstanceId_Type())
cucsExtmgmtIfMonPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyInstanceId.setStatus(_A)
_CucsExtmgmtIfMonPolicyDn_Type=CucsManagedObjectDn
_CucsExtmgmtIfMonPolicyDn_Object=MibTableColumn
cucsExtmgmtIfMonPolicyDn=_CucsExtmgmtIfMonPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,2),_CucsExtmgmtIfMonPolicyDn_Type())
cucsExtmgmtIfMonPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyDn.setStatus(_A)
_CucsExtmgmtIfMonPolicyRn_Type=SnmpAdminString
_CucsExtmgmtIfMonPolicyRn_Object=MibTableColumn
cucsExtmgmtIfMonPolicyRn=_CucsExtmgmtIfMonPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,3),_CucsExtmgmtIfMonPolicyRn_Type())
cucsExtmgmtIfMonPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyRn.setStatus(_A)
_CucsExtmgmtIfMonPolicyAdminState_Type=CucsExtmgmtIfMonPolicyAdminState
_CucsExtmgmtIfMonPolicyAdminState_Object=MibTableColumn
cucsExtmgmtIfMonPolicyAdminState=_CucsExtmgmtIfMonPolicyAdminState_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,4),_CucsExtmgmtIfMonPolicyAdminState_Type())
cucsExtmgmtIfMonPolicyAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyAdminState.setStatus(_A)
_CucsExtmgmtIfMonPolicyEnableHAFailover_Type=TruthValue
_CucsExtmgmtIfMonPolicyEnableHAFailover_Object=MibTableColumn
cucsExtmgmtIfMonPolicyEnableHAFailover=_CucsExtmgmtIfMonPolicyEnableHAFailover_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,5),_CucsExtmgmtIfMonPolicyEnableHAFailover_Type())
cucsExtmgmtIfMonPolicyEnableHAFailover.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyEnableHAFailover.setStatus(_A)
_CucsExtmgmtIfMonPolicyMaxFailReportCount_Type=Gauge32
_CucsExtmgmtIfMonPolicyMaxFailReportCount_Object=MibTableColumn
cucsExtmgmtIfMonPolicyMaxFailReportCount=_CucsExtmgmtIfMonPolicyMaxFailReportCount_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,6),_CucsExtmgmtIfMonPolicyMaxFailReportCount_Type())
cucsExtmgmtIfMonPolicyMaxFailReportCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyMaxFailReportCount.setStatus(_A)
_CucsExtmgmtIfMonPolicyMonitorMechanism_Type=CucsExtmgmtIfMonPolicyMonitorMechanism
_CucsExtmgmtIfMonPolicyMonitorMechanism_Object=MibTableColumn
cucsExtmgmtIfMonPolicyMonitorMechanism=_CucsExtmgmtIfMonPolicyMonitorMechanism_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,7),_CucsExtmgmtIfMonPolicyMonitorMechanism_Type())
cucsExtmgmtIfMonPolicyMonitorMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyMonitorMechanism.setStatus(_A)
_CucsExtmgmtIfMonPolicyPollInterval_Type=Gauge32
_CucsExtmgmtIfMonPolicyPollInterval_Object=MibTableColumn
cucsExtmgmtIfMonPolicyPollInterval=_CucsExtmgmtIfMonPolicyPollInterval_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,8),_CucsExtmgmtIfMonPolicyPollInterval_Type())
cucsExtmgmtIfMonPolicyPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyPollInterval.setStatus(_A)
_CucsExtmgmtIfMonPolicyDescr_Type=SnmpAdminString
_CucsExtmgmtIfMonPolicyDescr_Object=MibTableColumn
cucsExtmgmtIfMonPolicyDescr=_CucsExtmgmtIfMonPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,9),_CucsExtmgmtIfMonPolicyDescr_Type())
cucsExtmgmtIfMonPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyDescr.setStatus(_A)
_CucsExtmgmtIfMonPolicyIntId_Type=SnmpAdminString
_CucsExtmgmtIfMonPolicyIntId_Object=MibTableColumn
cucsExtmgmtIfMonPolicyIntId=_CucsExtmgmtIfMonPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,10),_CucsExtmgmtIfMonPolicyIntId_Type())
cucsExtmgmtIfMonPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyIntId.setStatus(_A)
_CucsExtmgmtIfMonPolicyName_Type=SnmpAdminString
_CucsExtmgmtIfMonPolicyName_Object=MibTableColumn
cucsExtmgmtIfMonPolicyName=_CucsExtmgmtIfMonPolicyName_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,11),_CucsExtmgmtIfMonPolicyName_Type())
cucsExtmgmtIfMonPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyName.setStatus(_A)
_CucsExtmgmtIfMonPolicyPolicyLevel_Type=Gauge32
_CucsExtmgmtIfMonPolicyPolicyLevel_Object=MibTableColumn
cucsExtmgmtIfMonPolicyPolicyLevel=_CucsExtmgmtIfMonPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,12),_CucsExtmgmtIfMonPolicyPolicyLevel_Type())
cucsExtmgmtIfMonPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyPolicyLevel.setStatus(_A)
_CucsExtmgmtIfMonPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsExtmgmtIfMonPolicyPolicyOwner_Object=MibTableColumn
cucsExtmgmtIfMonPolicyPolicyOwner=_CucsExtmgmtIfMonPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,57,4,1,13),_CucsExtmgmtIfMonPolicyPolicyOwner_Type())
cucsExtmgmtIfMonPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtIfMonPolicyPolicyOwner.setStatus(_A)
_CucsExtmgmtMiiStatusTable_Object=MibTable
cucsExtmgmtMiiStatusTable=_CucsExtmgmtMiiStatusTable_Object((1,3,6,1,4,1,9,9,719,1,57,5))
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusTable.setStatus(_A)
_CucsExtmgmtMiiStatusEntry_Object=MibTableRow
cucsExtmgmtMiiStatusEntry=_CucsExtmgmtMiiStatusEntry_Object((1,3,6,1,4,1,9,9,719,1,57,5,1))
cucsExtmgmtMiiStatusEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusEntry.setStatus(_A)
_CucsExtmgmtMiiStatusInstanceId_Type=CucsManagedObjectId
_CucsExtmgmtMiiStatusInstanceId_Object=MibTableColumn
cucsExtmgmtMiiStatusInstanceId=_CucsExtmgmtMiiStatusInstanceId_Object((1,3,6,1,4,1,9,9,719,1,57,5,1,1),_CucsExtmgmtMiiStatusInstanceId_Type())
cucsExtmgmtMiiStatusInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusInstanceId.setStatus(_A)
_CucsExtmgmtMiiStatusDn_Type=CucsManagedObjectDn
_CucsExtmgmtMiiStatusDn_Object=MibTableColumn
cucsExtmgmtMiiStatusDn=_CucsExtmgmtMiiStatusDn_Object((1,3,6,1,4,1,9,9,719,1,57,5,1,2),_CucsExtmgmtMiiStatusDn_Type())
cucsExtmgmtMiiStatusDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusDn.setStatus(_A)
_CucsExtmgmtMiiStatusRn_Type=SnmpAdminString
_CucsExtmgmtMiiStatusRn_Object=MibTableColumn
cucsExtmgmtMiiStatusRn=_CucsExtmgmtMiiStatusRn_Object((1,3,6,1,4,1,9,9,719,1,57,5,1,3),_CucsExtmgmtMiiStatusRn_Type())
cucsExtmgmtMiiStatusRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusRn.setStatus(_A)
_CucsExtmgmtMiiStatusMaxRetryCount_Type=CucsExtmgmtMiiStatusMaxRetryCount
_CucsExtmgmtMiiStatusMaxRetryCount_Object=MibTableColumn
cucsExtmgmtMiiStatusMaxRetryCount=_CucsExtmgmtMiiStatusMaxRetryCount_Object((1,3,6,1,4,1,9,9,719,1,57,5,1,4),_CucsExtmgmtMiiStatusMaxRetryCount_Type())
cucsExtmgmtMiiStatusMaxRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusMaxRetryCount.setStatus(_A)
_CucsExtmgmtMiiStatusRetryInterval_Type=CucsExtmgmtMiiStatusRetryInterval
_CucsExtmgmtMiiStatusRetryInterval_Object=MibTableColumn
cucsExtmgmtMiiStatusRetryInterval=_CucsExtmgmtMiiStatusRetryInterval_Object((1,3,6,1,4,1,9,9,719,1,57,5,1,5),_CucsExtmgmtMiiStatusRetryInterval_Type())
cucsExtmgmtMiiStatusRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtMiiStatusRetryInterval.setStatus(_A)
_CucsExtmgmtNdiscTargetsTable_Object=MibTable
cucsExtmgmtNdiscTargetsTable=_CucsExtmgmtNdiscTargetsTable_Object((1,3,6,1,4,1,9,9,719,1,57,6))
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsTable.setStatus(_A)
_CucsExtmgmtNdiscTargetsEntry_Object=MibTableRow
cucsExtmgmtNdiscTargetsEntry=_CucsExtmgmtNdiscTargetsEntry_Object((1,3,6,1,4,1,9,9,719,1,57,6,1))
cucsExtmgmtNdiscTargetsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsEntry.setStatus(_A)
_CucsExtmgmtNdiscTargetsInstanceId_Type=CucsManagedObjectId
_CucsExtmgmtNdiscTargetsInstanceId_Object=MibTableColumn
cucsExtmgmtNdiscTargetsInstanceId=_CucsExtmgmtNdiscTargetsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,1),_CucsExtmgmtNdiscTargetsInstanceId_Type())
cucsExtmgmtNdiscTargetsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsInstanceId.setStatus(_A)
_CucsExtmgmtNdiscTargetsDn_Type=CucsManagedObjectDn
_CucsExtmgmtNdiscTargetsDn_Object=MibTableColumn
cucsExtmgmtNdiscTargetsDn=_CucsExtmgmtNdiscTargetsDn_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,2),_CucsExtmgmtNdiscTargetsDn_Type())
cucsExtmgmtNdiscTargetsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsDn.setStatus(_A)
_CucsExtmgmtNdiscTargetsRn_Type=SnmpAdminString
_CucsExtmgmtNdiscTargetsRn_Object=MibTableColumn
cucsExtmgmtNdiscTargetsRn=_CucsExtmgmtNdiscTargetsRn_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,3),_CucsExtmgmtNdiscTargetsRn_Type())
cucsExtmgmtNdiscTargetsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsRn.setStatus(_A)
_CucsExtmgmtNdiscTargetsConfigState_Type=CucsAaaConfigState
_CucsExtmgmtNdiscTargetsConfigState_Object=MibTableColumn
cucsExtmgmtNdiscTargetsConfigState=_CucsExtmgmtNdiscTargetsConfigState_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,4),_CucsExtmgmtNdiscTargetsConfigState_Type())
cucsExtmgmtNdiscTargetsConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsConfigState.setStatus(_A)
_CucsExtmgmtNdiscTargetsConfigStatusMessage_Type=SnmpAdminString
_CucsExtmgmtNdiscTargetsConfigStatusMessage_Object=MibTableColumn
cucsExtmgmtNdiscTargetsConfigStatusMessage=_CucsExtmgmtNdiscTargetsConfigStatusMessage_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,5),_CucsExtmgmtNdiscTargetsConfigStatusMessage_Type())
cucsExtmgmtNdiscTargetsConfigStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsConfigStatusMessage.setStatus(_A)
_CucsExtmgmtNdiscTargetsIpv6Target1_Type=InetAddressIPv6
_CucsExtmgmtNdiscTargetsIpv6Target1_Object=MibTableColumn
cucsExtmgmtNdiscTargetsIpv6Target1=_CucsExtmgmtNdiscTargetsIpv6Target1_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,6),_CucsExtmgmtNdiscTargetsIpv6Target1_Type())
cucsExtmgmtNdiscTargetsIpv6Target1.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsIpv6Target1.setStatus(_A)
_CucsExtmgmtNdiscTargetsIpv6Target2_Type=InetAddressIPv6
_CucsExtmgmtNdiscTargetsIpv6Target2_Object=MibTableColumn
cucsExtmgmtNdiscTargetsIpv6Target2=_CucsExtmgmtNdiscTargetsIpv6Target2_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,7),_CucsExtmgmtNdiscTargetsIpv6Target2_Type())
cucsExtmgmtNdiscTargetsIpv6Target2.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsIpv6Target2.setStatus(_A)
_CucsExtmgmtNdiscTargetsIpv6Target3_Type=InetAddressIPv6
_CucsExtmgmtNdiscTargetsIpv6Target3_Object=MibTableColumn
cucsExtmgmtNdiscTargetsIpv6Target3=_CucsExtmgmtNdiscTargetsIpv6Target3_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,8),_CucsExtmgmtNdiscTargetsIpv6Target3_Type())
cucsExtmgmtNdiscTargetsIpv6Target3.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsIpv6Target3.setStatus(_A)
_CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Type=CucsExtmgmtNdiscTargetsMaxDeadlineTimeout
_CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Object=MibTableColumn
cucsExtmgmtNdiscTargetsMaxDeadlineTimeout=_CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,9),_CucsExtmgmtNdiscTargetsMaxDeadlineTimeout_Type())
cucsExtmgmtNdiscTargetsMaxDeadlineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsMaxDeadlineTimeout.setStatus(_A)
_CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Type=CucsExtmgmtNdiscTargetsNumberOfNdiscRequests
_CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Object=MibTableColumn
cucsExtmgmtNdiscTargetsNumberOfNdiscRequests=_CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Object((1,3,6,1,4,1,9,9,719,1,57,6,1,10),_CucsExtmgmtNdiscTargetsNumberOfNdiscRequests_Type())
cucsExtmgmtNdiscTargetsNumberOfNdiscRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsExtmgmtNdiscTargetsNumberOfNdiscRequests.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsExtmgmtObjects':cucsExtmgmtObjects,'cucsExtmgmtArpTargetsTable':cucsExtmgmtArpTargetsTable,'cucsExtmgmtArpTargetsEntry':cucsExtmgmtArpTargetsEntry,_E:cucsExtmgmtArpTargetsInstanceId,'cucsExtmgmtArpTargetsDn':cucsExtmgmtArpTargetsDn,'cucsExtmgmtArpTargetsRn':cucsExtmgmtArpTargetsRn,'cucsExtmgmtArpTargetsMaxDeadlineTimeout':cucsExtmgmtArpTargetsMaxDeadlineTimeout,'cucsExtmgmtArpTargetsNumberOfArpRequests':cucsExtmgmtArpTargetsNumberOfArpRequests,'cucsExtmgmtArpTargetsTargetIp1':cucsExtmgmtArpTargetsTargetIp1,'cucsExtmgmtArpTargetsTargetIp2':cucsExtmgmtArpTargetsTargetIp2,'cucsExtmgmtArpTargetsTargetIp3':cucsExtmgmtArpTargetsTargetIp3,'cucsExtmgmtArpTargetsConfigState':cucsExtmgmtArpTargetsConfigState,'cucsExtmgmtArpTargetsConfigStatusMessage':cucsExtmgmtArpTargetsConfigStatusMessage,'cucsExtmgmtGatewayPingTable':cucsExtmgmtGatewayPingTable,'cucsExtmgmtGatewayPingEntry':cucsExtmgmtGatewayPingEntry,_F:cucsExtmgmtGatewayPingInstanceId,'cucsExtmgmtGatewayPingDn':cucsExtmgmtGatewayPingDn,'cucsExtmgmtGatewayPingRn':cucsExtmgmtGatewayPingRn,'cucsExtmgmtGatewayPingMaxDeadlineTimeout':cucsExtmgmtGatewayPingMaxDeadlineTimeout,'cucsExtmgmtGatewayPingNumberOfPingRequests':cucsExtmgmtGatewayPingNumberOfPingRequests,'cucsExtmgmtIfTable':cucsExtmgmtIfTable,'cucsExtmgmtIfEntry':cucsExtmgmtIfEntry,_G:cucsExtmgmtIfInstanceId,'cucsExtmgmtIfDn':cucsExtmgmtIfDn,'cucsExtmgmtIfRn':cucsExtmgmtIfRn,'cucsExtmgmtIfEpDn':cucsExtmgmtIfEpDn,'cucsExtmgmtIfFailReportCount':cucsExtmgmtIfFailReportCount,'cucsExtmgmtIfFltAggr':cucsExtmgmtIfFltAggr,'cucsExtmgmtIfId':cucsExtmgmtIfId,'cucsExtmgmtIfIfRole':cucsExtmgmtIfIfRole,'cucsExtmgmtIfIfType':cucsExtmgmtIfIfType,'cucsExtmgmtIfLastOperStateReport':cucsExtmgmtIfLastOperStateReport,'cucsExtmgmtIfLocale':cucsExtmgmtIfLocale,'cucsExtmgmtIfName':cucsExtmgmtIfName,'cucsExtmgmtIfOperState':cucsExtmgmtIfOperState,'cucsExtmgmtIfPeerDn':cucsExtmgmtIfPeerDn,'cucsExtmgmtIfTransport':cucsExtmgmtIfTransport,'cucsExtmgmtIfType':cucsExtmgmtIfType,'cucsExtmgmtIfMonPolicyTable':cucsExtmgmtIfMonPolicyTable,'cucsExtmgmtIfMonPolicyEntry':cucsExtmgmtIfMonPolicyEntry,_H:cucsExtmgmtIfMonPolicyInstanceId,'cucsExtmgmtIfMonPolicyDn':cucsExtmgmtIfMonPolicyDn,'cucsExtmgmtIfMonPolicyRn':cucsExtmgmtIfMonPolicyRn,'cucsExtmgmtIfMonPolicyAdminState':cucsExtmgmtIfMonPolicyAdminState,'cucsExtmgmtIfMonPolicyEnableHAFailover':cucsExtmgmtIfMonPolicyEnableHAFailover,'cucsExtmgmtIfMonPolicyMaxFailReportCount':cucsExtmgmtIfMonPolicyMaxFailReportCount,'cucsExtmgmtIfMonPolicyMonitorMechanism':cucsExtmgmtIfMonPolicyMonitorMechanism,'cucsExtmgmtIfMonPolicyPollInterval':cucsExtmgmtIfMonPolicyPollInterval,'cucsExtmgmtIfMonPolicyDescr':cucsExtmgmtIfMonPolicyDescr,'cucsExtmgmtIfMonPolicyIntId':cucsExtmgmtIfMonPolicyIntId,'cucsExtmgmtIfMonPolicyName':cucsExtmgmtIfMonPolicyName,'cucsExtmgmtIfMonPolicyPolicyLevel':cucsExtmgmtIfMonPolicyPolicyLevel,'cucsExtmgmtIfMonPolicyPolicyOwner':cucsExtmgmtIfMonPolicyPolicyOwner,'cucsExtmgmtMiiStatusTable':cucsExtmgmtMiiStatusTable,'cucsExtmgmtMiiStatusEntry':cucsExtmgmtMiiStatusEntry,_I:cucsExtmgmtMiiStatusInstanceId,'cucsExtmgmtMiiStatusDn':cucsExtmgmtMiiStatusDn,'cucsExtmgmtMiiStatusRn':cucsExtmgmtMiiStatusRn,'cucsExtmgmtMiiStatusMaxRetryCount':cucsExtmgmtMiiStatusMaxRetryCount,'cucsExtmgmtMiiStatusRetryInterval':cucsExtmgmtMiiStatusRetryInterval,'cucsExtmgmtNdiscTargetsTable':cucsExtmgmtNdiscTargetsTable,'cucsExtmgmtNdiscTargetsEntry':cucsExtmgmtNdiscTargetsEntry,_J:cucsExtmgmtNdiscTargetsInstanceId,'cucsExtmgmtNdiscTargetsDn':cucsExtmgmtNdiscTargetsDn,'cucsExtmgmtNdiscTargetsRn':cucsExtmgmtNdiscTargetsRn,'cucsExtmgmtNdiscTargetsConfigState':cucsExtmgmtNdiscTargetsConfigState,'cucsExtmgmtNdiscTargetsConfigStatusMessage':cucsExtmgmtNdiscTargetsConfigStatusMessage,'cucsExtmgmtNdiscTargetsIpv6Target1':cucsExtmgmtNdiscTargetsIpv6Target1,'cucsExtmgmtNdiscTargetsIpv6Target2':cucsExtmgmtNdiscTargetsIpv6Target2,'cucsExtmgmtNdiscTargetsIpv6Target3':cucsExtmgmtNdiscTargetsIpv6Target3,'cucsExtmgmtNdiscTargetsMaxDeadlineTimeout':cucsExtmgmtNdiscTargetsMaxDeadlineTimeout,'cucsExtmgmtNdiscTargetsNumberOfNdiscRequests':cucsExtmgmtNdiscTargetsNumberOfNdiscRequests})