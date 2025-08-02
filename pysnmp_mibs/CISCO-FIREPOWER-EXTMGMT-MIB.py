_J='cfprExtmgmtNdiscTargetsInstanceId'
_I='cfprExtmgmtMiiStatusInstanceId'
_H='cfprExtmgmtIfMonPolicyInstanceId'
_G='cfprExtmgmtIfInstanceId'
_F='cfprExtmgmtGatewayPingInstanceId'
_E='cfprExtmgmtArpTargetsInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-EXTMGMT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprAaaConfigState,CfprExtmgmtArpTargetsMaxDeadlineTimeout,CfprExtmgmtArpTargetsNumberOfArpRequests,CfprExtmgmtGatewayPingMaxDeadlineTimeout,CfprExtmgmtGatewayPingNumberOfPingRequests,CfprExtmgmtIfMonPolicyAdminState,CfprExtmgmtIfMonPolicyMonitorMechanism,CfprExtmgmtIfType,CfprExtmgmtMiiStatusMaxRetryCount,CfprExtmgmtMiiStatusRetryInterval,CfprExtmgmtNdiscTargetsMaxDeadlineTimeout,CfprExtmgmtNdiscTargetsNumberOfNdiscRequests,CfprNetworkIfStatus,CfprNetworkLocale,CfprNetworkPortRole,CfprNetworkPortType,CfprNetworkSwitchId,CfprNetworkTransport,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprAaaConfigState','CfprExtmgmtArpTargetsMaxDeadlineTimeout','CfprExtmgmtArpTargetsNumberOfArpRequests','CfprExtmgmtGatewayPingMaxDeadlineTimeout','CfprExtmgmtGatewayPingNumberOfPingRequests','CfprExtmgmtIfMonPolicyAdminState','CfprExtmgmtIfMonPolicyMonitorMechanism','CfprExtmgmtIfType','CfprExtmgmtMiiStatusMaxRetryCount','CfprExtmgmtMiiStatusRetryInterval','CfprExtmgmtNdiscTargetsMaxDeadlineTimeout','CfprExtmgmtNdiscTargetsNumberOfNdiscRequests','CfprNetworkIfStatus','CfprNetworkLocale','CfprNetworkPortRole','CfprNetworkPortType','CfprNetworkSwitchId','CfprNetworkTransport','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprExtmgmtObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,23))
_CfprExtmgmtArpTargetsTable_Object=MibTable
cfprExtmgmtArpTargetsTable=_CfprExtmgmtArpTargetsTable_Object((1,3,6,1,4,1,9,9,826,1,23,1))
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsTable.setStatus(_A)
_CfprExtmgmtArpTargetsEntry_Object=MibTableRow
cfprExtmgmtArpTargetsEntry=_CfprExtmgmtArpTargetsEntry_Object((1,3,6,1,4,1,9,9,826,1,23,1,1))
cfprExtmgmtArpTargetsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsEntry.setStatus(_A)
_CfprExtmgmtArpTargetsInstanceId_Type=CfprManagedObjectId
_CfprExtmgmtArpTargetsInstanceId_Object=MibTableColumn
cfprExtmgmtArpTargetsInstanceId=_CfprExtmgmtArpTargetsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,1),_CfprExtmgmtArpTargetsInstanceId_Type())
cfprExtmgmtArpTargetsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsInstanceId.setStatus(_A)
_CfprExtmgmtArpTargetsDn_Type=CfprManagedObjectDn
_CfprExtmgmtArpTargetsDn_Object=MibTableColumn
cfprExtmgmtArpTargetsDn=_CfprExtmgmtArpTargetsDn_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,2),_CfprExtmgmtArpTargetsDn_Type())
cfprExtmgmtArpTargetsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsDn.setStatus(_A)
_CfprExtmgmtArpTargetsRn_Type=SnmpAdminString
_CfprExtmgmtArpTargetsRn_Object=MibTableColumn
cfprExtmgmtArpTargetsRn=_CfprExtmgmtArpTargetsRn_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,3),_CfprExtmgmtArpTargetsRn_Type())
cfprExtmgmtArpTargetsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsRn.setStatus(_A)
_CfprExtmgmtArpTargetsConfigState_Type=CfprAaaConfigState
_CfprExtmgmtArpTargetsConfigState_Object=MibTableColumn
cfprExtmgmtArpTargetsConfigState=_CfprExtmgmtArpTargetsConfigState_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,4),_CfprExtmgmtArpTargetsConfigState_Type())
cfprExtmgmtArpTargetsConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsConfigState.setStatus(_A)
_CfprExtmgmtArpTargetsConfigStatusMessage_Type=SnmpAdminString
_CfprExtmgmtArpTargetsConfigStatusMessage_Object=MibTableColumn
cfprExtmgmtArpTargetsConfigStatusMessage=_CfprExtmgmtArpTargetsConfigStatusMessage_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,5),_CfprExtmgmtArpTargetsConfigStatusMessage_Type())
cfprExtmgmtArpTargetsConfigStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsConfigStatusMessage.setStatus(_A)
_CfprExtmgmtArpTargetsMaxDeadlineTimeout_Type=CfprExtmgmtArpTargetsMaxDeadlineTimeout
_CfprExtmgmtArpTargetsMaxDeadlineTimeout_Object=MibTableColumn
cfprExtmgmtArpTargetsMaxDeadlineTimeout=_CfprExtmgmtArpTargetsMaxDeadlineTimeout_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,6),_CfprExtmgmtArpTargetsMaxDeadlineTimeout_Type())
cfprExtmgmtArpTargetsMaxDeadlineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsMaxDeadlineTimeout.setStatus(_A)
_CfprExtmgmtArpTargetsNumberOfArpRequests_Type=CfprExtmgmtArpTargetsNumberOfArpRequests
_CfprExtmgmtArpTargetsNumberOfArpRequests_Object=MibTableColumn
cfprExtmgmtArpTargetsNumberOfArpRequests=_CfprExtmgmtArpTargetsNumberOfArpRequests_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,7),_CfprExtmgmtArpTargetsNumberOfArpRequests_Type())
cfprExtmgmtArpTargetsNumberOfArpRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsNumberOfArpRequests.setStatus(_A)
_CfprExtmgmtArpTargetsTargetIp1_Type=InetAddressIPv4
_CfprExtmgmtArpTargetsTargetIp1_Object=MibTableColumn
cfprExtmgmtArpTargetsTargetIp1=_CfprExtmgmtArpTargetsTargetIp1_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,8),_CfprExtmgmtArpTargetsTargetIp1_Type())
cfprExtmgmtArpTargetsTargetIp1.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsTargetIp1.setStatus(_A)
_CfprExtmgmtArpTargetsTargetIp2_Type=InetAddressIPv4
_CfprExtmgmtArpTargetsTargetIp2_Object=MibTableColumn
cfprExtmgmtArpTargetsTargetIp2=_CfprExtmgmtArpTargetsTargetIp2_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,9),_CfprExtmgmtArpTargetsTargetIp2_Type())
cfprExtmgmtArpTargetsTargetIp2.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsTargetIp2.setStatus(_A)
_CfprExtmgmtArpTargetsTargetIp3_Type=InetAddressIPv4
_CfprExtmgmtArpTargetsTargetIp3_Object=MibTableColumn
cfprExtmgmtArpTargetsTargetIp3=_CfprExtmgmtArpTargetsTargetIp3_Object((1,3,6,1,4,1,9,9,826,1,23,1,1,10),_CfprExtmgmtArpTargetsTargetIp3_Type())
cfprExtmgmtArpTargetsTargetIp3.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtArpTargetsTargetIp3.setStatus(_A)
_CfprExtmgmtGatewayPingTable_Object=MibTable
cfprExtmgmtGatewayPingTable=_CfprExtmgmtGatewayPingTable_Object((1,3,6,1,4,1,9,9,826,1,23,2))
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingTable.setStatus(_A)
_CfprExtmgmtGatewayPingEntry_Object=MibTableRow
cfprExtmgmtGatewayPingEntry=_CfprExtmgmtGatewayPingEntry_Object((1,3,6,1,4,1,9,9,826,1,23,2,1))
cfprExtmgmtGatewayPingEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingEntry.setStatus(_A)
_CfprExtmgmtGatewayPingInstanceId_Type=CfprManagedObjectId
_CfprExtmgmtGatewayPingInstanceId_Object=MibTableColumn
cfprExtmgmtGatewayPingInstanceId=_CfprExtmgmtGatewayPingInstanceId_Object((1,3,6,1,4,1,9,9,826,1,23,2,1,1),_CfprExtmgmtGatewayPingInstanceId_Type())
cfprExtmgmtGatewayPingInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingInstanceId.setStatus(_A)
_CfprExtmgmtGatewayPingDn_Type=CfprManagedObjectDn
_CfprExtmgmtGatewayPingDn_Object=MibTableColumn
cfprExtmgmtGatewayPingDn=_CfprExtmgmtGatewayPingDn_Object((1,3,6,1,4,1,9,9,826,1,23,2,1,2),_CfprExtmgmtGatewayPingDn_Type())
cfprExtmgmtGatewayPingDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingDn.setStatus(_A)
_CfprExtmgmtGatewayPingRn_Type=SnmpAdminString
_CfprExtmgmtGatewayPingRn_Object=MibTableColumn
cfprExtmgmtGatewayPingRn=_CfprExtmgmtGatewayPingRn_Object((1,3,6,1,4,1,9,9,826,1,23,2,1,3),_CfprExtmgmtGatewayPingRn_Type())
cfprExtmgmtGatewayPingRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingRn.setStatus(_A)
_CfprExtmgmtGatewayPingMaxDeadlineTimeout_Type=CfprExtmgmtGatewayPingMaxDeadlineTimeout
_CfprExtmgmtGatewayPingMaxDeadlineTimeout_Object=MibTableColumn
cfprExtmgmtGatewayPingMaxDeadlineTimeout=_CfprExtmgmtGatewayPingMaxDeadlineTimeout_Object((1,3,6,1,4,1,9,9,826,1,23,2,1,4),_CfprExtmgmtGatewayPingMaxDeadlineTimeout_Type())
cfprExtmgmtGatewayPingMaxDeadlineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingMaxDeadlineTimeout.setStatus(_A)
_CfprExtmgmtGatewayPingNumberOfPingRequests_Type=CfprExtmgmtGatewayPingNumberOfPingRequests
_CfprExtmgmtGatewayPingNumberOfPingRequests_Object=MibTableColumn
cfprExtmgmtGatewayPingNumberOfPingRequests=_CfprExtmgmtGatewayPingNumberOfPingRequests_Object((1,3,6,1,4,1,9,9,826,1,23,2,1,5),_CfprExtmgmtGatewayPingNumberOfPingRequests_Type())
cfprExtmgmtGatewayPingNumberOfPingRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtGatewayPingNumberOfPingRequests.setStatus(_A)
_CfprExtmgmtIfTable_Object=MibTable
cfprExtmgmtIfTable=_CfprExtmgmtIfTable_Object((1,3,6,1,4,1,9,9,826,1,23,3))
if mibBuilder.loadTexts:cfprExtmgmtIfTable.setStatus(_A)
_CfprExtmgmtIfEntry_Object=MibTableRow
cfprExtmgmtIfEntry=_CfprExtmgmtIfEntry_Object((1,3,6,1,4,1,9,9,826,1,23,3,1))
cfprExtmgmtIfEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprExtmgmtIfEntry.setStatus(_A)
_CfprExtmgmtIfInstanceId_Type=CfprManagedObjectId
_CfprExtmgmtIfInstanceId_Object=MibTableColumn
cfprExtmgmtIfInstanceId=_CfprExtmgmtIfInstanceId_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,1),_CfprExtmgmtIfInstanceId_Type())
cfprExtmgmtIfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprExtmgmtIfInstanceId.setStatus(_A)
_CfprExtmgmtIfDn_Type=CfprManagedObjectDn
_CfprExtmgmtIfDn_Object=MibTableColumn
cfprExtmgmtIfDn=_CfprExtmgmtIfDn_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,2),_CfprExtmgmtIfDn_Type())
cfprExtmgmtIfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfDn.setStatus(_A)
_CfprExtmgmtIfRn_Type=SnmpAdminString
_CfprExtmgmtIfRn_Object=MibTableColumn
cfprExtmgmtIfRn=_CfprExtmgmtIfRn_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,3),_CfprExtmgmtIfRn_Type())
cfprExtmgmtIfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfRn.setStatus(_A)
_CfprExtmgmtIfEpDn_Type=SnmpAdminString
_CfprExtmgmtIfEpDn_Object=MibTableColumn
cfprExtmgmtIfEpDn=_CfprExtmgmtIfEpDn_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,4),_CfprExtmgmtIfEpDn_Type())
cfprExtmgmtIfEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfEpDn.setStatus(_A)
_CfprExtmgmtIfFailReportCount_Type=Gauge32
_CfprExtmgmtIfFailReportCount_Object=MibTableColumn
cfprExtmgmtIfFailReportCount=_CfprExtmgmtIfFailReportCount_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,5),_CfprExtmgmtIfFailReportCount_Type())
cfprExtmgmtIfFailReportCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfFailReportCount.setStatus(_A)
_CfprExtmgmtIfFltAggr_Type=Unsigned64
_CfprExtmgmtIfFltAggr_Object=MibTableColumn
cfprExtmgmtIfFltAggr=_CfprExtmgmtIfFltAggr_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,6),_CfprExtmgmtIfFltAggr_Type())
cfprExtmgmtIfFltAggr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfFltAggr.setStatus(_A)
_CfprExtmgmtIfId_Type=CfprNetworkSwitchId
_CfprExtmgmtIfId_Object=MibTableColumn
cfprExtmgmtIfId=_CfprExtmgmtIfId_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,7),_CfprExtmgmtIfId_Type())
cfprExtmgmtIfId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfId.setStatus(_A)
_CfprExtmgmtIfIfRole_Type=CfprNetworkPortRole
_CfprExtmgmtIfIfRole_Object=MibTableColumn
cfprExtmgmtIfIfRole=_CfprExtmgmtIfIfRole_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,8),_CfprExtmgmtIfIfRole_Type())
cfprExtmgmtIfIfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfIfRole.setStatus(_A)
_CfprExtmgmtIfIfType_Type=CfprNetworkPortType
_CfprExtmgmtIfIfType_Object=MibTableColumn
cfprExtmgmtIfIfType=_CfprExtmgmtIfIfType_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,9),_CfprExtmgmtIfIfType_Type())
cfprExtmgmtIfIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfIfType.setStatus(_A)
_CfprExtmgmtIfLastOperStateReport_Type=CfprNetworkIfStatus
_CfprExtmgmtIfLastOperStateReport_Object=MibTableColumn
cfprExtmgmtIfLastOperStateReport=_CfprExtmgmtIfLastOperStateReport_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,10),_CfprExtmgmtIfLastOperStateReport_Type())
cfprExtmgmtIfLastOperStateReport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfLastOperStateReport.setStatus(_A)
_CfprExtmgmtIfLocale_Type=CfprNetworkLocale
_CfprExtmgmtIfLocale_Object=MibTableColumn
cfprExtmgmtIfLocale=_CfprExtmgmtIfLocale_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,11),_CfprExtmgmtIfLocale_Type())
cfprExtmgmtIfLocale.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfLocale.setStatus(_A)
_CfprExtmgmtIfName_Type=SnmpAdminString
_CfprExtmgmtIfName_Object=MibTableColumn
cfprExtmgmtIfName=_CfprExtmgmtIfName_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,12),_CfprExtmgmtIfName_Type())
cfprExtmgmtIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfName.setStatus(_A)
_CfprExtmgmtIfOperState_Type=CfprNetworkIfStatus
_CfprExtmgmtIfOperState_Object=MibTableColumn
cfprExtmgmtIfOperState=_CfprExtmgmtIfOperState_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,13),_CfprExtmgmtIfOperState_Type())
cfprExtmgmtIfOperState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfOperState.setStatus(_A)
_CfprExtmgmtIfPeerDn_Type=SnmpAdminString
_CfprExtmgmtIfPeerDn_Object=MibTableColumn
cfprExtmgmtIfPeerDn=_CfprExtmgmtIfPeerDn_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,14),_CfprExtmgmtIfPeerDn_Type())
cfprExtmgmtIfPeerDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfPeerDn.setStatus(_A)
_CfprExtmgmtIfTransport_Type=CfprNetworkTransport
_CfprExtmgmtIfTransport_Object=MibTableColumn
cfprExtmgmtIfTransport=_CfprExtmgmtIfTransport_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,15),_CfprExtmgmtIfTransport_Type())
cfprExtmgmtIfTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfTransport.setStatus(_A)
_CfprExtmgmtIfType_Type=CfprExtmgmtIfType
_CfprExtmgmtIfType_Object=MibTableColumn
cfprExtmgmtIfType=_CfprExtmgmtIfType_Object((1,3,6,1,4,1,9,9,826,1,23,3,1,16),_CfprExtmgmtIfType_Type())
cfprExtmgmtIfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfType.setStatus(_A)
_CfprExtmgmtIfMonPolicyTable_Object=MibTable
cfprExtmgmtIfMonPolicyTable=_CfprExtmgmtIfMonPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,23,4))
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyTable.setStatus(_A)
_CfprExtmgmtIfMonPolicyEntry_Object=MibTableRow
cfprExtmgmtIfMonPolicyEntry=_CfprExtmgmtIfMonPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,23,4,1))
cfprExtmgmtIfMonPolicyEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyEntry.setStatus(_A)
_CfprExtmgmtIfMonPolicyInstanceId_Type=CfprManagedObjectId
_CfprExtmgmtIfMonPolicyInstanceId_Object=MibTableColumn
cfprExtmgmtIfMonPolicyInstanceId=_CfprExtmgmtIfMonPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,1),_CfprExtmgmtIfMonPolicyInstanceId_Type())
cfprExtmgmtIfMonPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyInstanceId.setStatus(_A)
_CfprExtmgmtIfMonPolicyDn_Type=CfprManagedObjectDn
_CfprExtmgmtIfMonPolicyDn_Object=MibTableColumn
cfprExtmgmtIfMonPolicyDn=_CfprExtmgmtIfMonPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,2),_CfprExtmgmtIfMonPolicyDn_Type())
cfprExtmgmtIfMonPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyDn.setStatus(_A)
_CfprExtmgmtIfMonPolicyRn_Type=SnmpAdminString
_CfprExtmgmtIfMonPolicyRn_Object=MibTableColumn
cfprExtmgmtIfMonPolicyRn=_CfprExtmgmtIfMonPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,3),_CfprExtmgmtIfMonPolicyRn_Type())
cfprExtmgmtIfMonPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyRn.setStatus(_A)
_CfprExtmgmtIfMonPolicyAdminState_Type=CfprExtmgmtIfMonPolicyAdminState
_CfprExtmgmtIfMonPolicyAdminState_Object=MibTableColumn
cfprExtmgmtIfMonPolicyAdminState=_CfprExtmgmtIfMonPolicyAdminState_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,4),_CfprExtmgmtIfMonPolicyAdminState_Type())
cfprExtmgmtIfMonPolicyAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyAdminState.setStatus(_A)
_CfprExtmgmtIfMonPolicyDescr_Type=SnmpAdminString
_CfprExtmgmtIfMonPolicyDescr_Object=MibTableColumn
cfprExtmgmtIfMonPolicyDescr=_CfprExtmgmtIfMonPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,5),_CfprExtmgmtIfMonPolicyDescr_Type())
cfprExtmgmtIfMonPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyDescr.setStatus(_A)
_CfprExtmgmtIfMonPolicyEnableHAFailover_Type=TruthValue
_CfprExtmgmtIfMonPolicyEnableHAFailover_Object=MibTableColumn
cfprExtmgmtIfMonPolicyEnableHAFailover=_CfprExtmgmtIfMonPolicyEnableHAFailover_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,6),_CfprExtmgmtIfMonPolicyEnableHAFailover_Type())
cfprExtmgmtIfMonPolicyEnableHAFailover.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyEnableHAFailover.setStatus(_A)
_CfprExtmgmtIfMonPolicyIntId_Type=SnmpAdminString
_CfprExtmgmtIfMonPolicyIntId_Object=MibTableColumn
cfprExtmgmtIfMonPolicyIntId=_CfprExtmgmtIfMonPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,7),_CfprExtmgmtIfMonPolicyIntId_Type())
cfprExtmgmtIfMonPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyIntId.setStatus(_A)
_CfprExtmgmtIfMonPolicyMaxFailReportCount_Type=Gauge32
_CfprExtmgmtIfMonPolicyMaxFailReportCount_Object=MibTableColumn
cfprExtmgmtIfMonPolicyMaxFailReportCount=_CfprExtmgmtIfMonPolicyMaxFailReportCount_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,8),_CfprExtmgmtIfMonPolicyMaxFailReportCount_Type())
cfprExtmgmtIfMonPolicyMaxFailReportCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyMaxFailReportCount.setStatus(_A)
_CfprExtmgmtIfMonPolicyMonitorMechanism_Type=CfprExtmgmtIfMonPolicyMonitorMechanism
_CfprExtmgmtIfMonPolicyMonitorMechanism_Object=MibTableColumn
cfprExtmgmtIfMonPolicyMonitorMechanism=_CfprExtmgmtIfMonPolicyMonitorMechanism_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,9),_CfprExtmgmtIfMonPolicyMonitorMechanism_Type())
cfprExtmgmtIfMonPolicyMonitorMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyMonitorMechanism.setStatus(_A)
_CfprExtmgmtIfMonPolicyName_Type=SnmpAdminString
_CfprExtmgmtIfMonPolicyName_Object=MibTableColumn
cfprExtmgmtIfMonPolicyName=_CfprExtmgmtIfMonPolicyName_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,10),_CfprExtmgmtIfMonPolicyName_Type())
cfprExtmgmtIfMonPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyName.setStatus(_A)
_CfprExtmgmtIfMonPolicyPolicyLevel_Type=Gauge32
_CfprExtmgmtIfMonPolicyPolicyLevel_Object=MibTableColumn
cfprExtmgmtIfMonPolicyPolicyLevel=_CfprExtmgmtIfMonPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,11),_CfprExtmgmtIfMonPolicyPolicyLevel_Type())
cfprExtmgmtIfMonPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyPolicyLevel.setStatus(_A)
_CfprExtmgmtIfMonPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprExtmgmtIfMonPolicyPolicyOwner_Object=MibTableColumn
cfprExtmgmtIfMonPolicyPolicyOwner=_CfprExtmgmtIfMonPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,12),_CfprExtmgmtIfMonPolicyPolicyOwner_Type())
cfprExtmgmtIfMonPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyPolicyOwner.setStatus(_A)
_CfprExtmgmtIfMonPolicyPollInterval_Type=Gauge32
_CfprExtmgmtIfMonPolicyPollInterval_Object=MibTableColumn
cfprExtmgmtIfMonPolicyPollInterval=_CfprExtmgmtIfMonPolicyPollInterval_Object((1,3,6,1,4,1,9,9,826,1,23,4,1,13),_CfprExtmgmtIfMonPolicyPollInterval_Type())
cfprExtmgmtIfMonPolicyPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtIfMonPolicyPollInterval.setStatus(_A)
_CfprExtmgmtMiiStatusTable_Object=MibTable
cfprExtmgmtMiiStatusTable=_CfprExtmgmtMiiStatusTable_Object((1,3,6,1,4,1,9,9,826,1,23,5))
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusTable.setStatus(_A)
_CfprExtmgmtMiiStatusEntry_Object=MibTableRow
cfprExtmgmtMiiStatusEntry=_CfprExtmgmtMiiStatusEntry_Object((1,3,6,1,4,1,9,9,826,1,23,5,1))
cfprExtmgmtMiiStatusEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusEntry.setStatus(_A)
_CfprExtmgmtMiiStatusInstanceId_Type=CfprManagedObjectId
_CfprExtmgmtMiiStatusInstanceId_Object=MibTableColumn
cfprExtmgmtMiiStatusInstanceId=_CfprExtmgmtMiiStatusInstanceId_Object((1,3,6,1,4,1,9,9,826,1,23,5,1,1),_CfprExtmgmtMiiStatusInstanceId_Type())
cfprExtmgmtMiiStatusInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusInstanceId.setStatus(_A)
_CfprExtmgmtMiiStatusDn_Type=CfprManagedObjectDn
_CfprExtmgmtMiiStatusDn_Object=MibTableColumn
cfprExtmgmtMiiStatusDn=_CfprExtmgmtMiiStatusDn_Object((1,3,6,1,4,1,9,9,826,1,23,5,1,2),_CfprExtmgmtMiiStatusDn_Type())
cfprExtmgmtMiiStatusDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusDn.setStatus(_A)
_CfprExtmgmtMiiStatusRn_Type=SnmpAdminString
_CfprExtmgmtMiiStatusRn_Object=MibTableColumn
cfprExtmgmtMiiStatusRn=_CfprExtmgmtMiiStatusRn_Object((1,3,6,1,4,1,9,9,826,1,23,5,1,3),_CfprExtmgmtMiiStatusRn_Type())
cfprExtmgmtMiiStatusRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusRn.setStatus(_A)
_CfprExtmgmtMiiStatusMaxRetryCount_Type=CfprExtmgmtMiiStatusMaxRetryCount
_CfprExtmgmtMiiStatusMaxRetryCount_Object=MibTableColumn
cfprExtmgmtMiiStatusMaxRetryCount=_CfprExtmgmtMiiStatusMaxRetryCount_Object((1,3,6,1,4,1,9,9,826,1,23,5,1,4),_CfprExtmgmtMiiStatusMaxRetryCount_Type())
cfprExtmgmtMiiStatusMaxRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusMaxRetryCount.setStatus(_A)
_CfprExtmgmtMiiStatusRetryInterval_Type=CfprExtmgmtMiiStatusRetryInterval
_CfprExtmgmtMiiStatusRetryInterval_Object=MibTableColumn
cfprExtmgmtMiiStatusRetryInterval=_CfprExtmgmtMiiStatusRetryInterval_Object((1,3,6,1,4,1,9,9,826,1,23,5,1,5),_CfprExtmgmtMiiStatusRetryInterval_Type())
cfprExtmgmtMiiStatusRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtMiiStatusRetryInterval.setStatus(_A)
_CfprExtmgmtNdiscTargetsTable_Object=MibTable
cfprExtmgmtNdiscTargetsTable=_CfprExtmgmtNdiscTargetsTable_Object((1,3,6,1,4,1,9,9,826,1,23,6))
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsTable.setStatus(_A)
_CfprExtmgmtNdiscTargetsEntry_Object=MibTableRow
cfprExtmgmtNdiscTargetsEntry=_CfprExtmgmtNdiscTargetsEntry_Object((1,3,6,1,4,1,9,9,826,1,23,6,1))
cfprExtmgmtNdiscTargetsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsEntry.setStatus(_A)
_CfprExtmgmtNdiscTargetsInstanceId_Type=CfprManagedObjectId
_CfprExtmgmtNdiscTargetsInstanceId_Object=MibTableColumn
cfprExtmgmtNdiscTargetsInstanceId=_CfprExtmgmtNdiscTargetsInstanceId_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,1),_CfprExtmgmtNdiscTargetsInstanceId_Type())
cfprExtmgmtNdiscTargetsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsInstanceId.setStatus(_A)
_CfprExtmgmtNdiscTargetsDn_Type=CfprManagedObjectDn
_CfprExtmgmtNdiscTargetsDn_Object=MibTableColumn
cfprExtmgmtNdiscTargetsDn=_CfprExtmgmtNdiscTargetsDn_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,2),_CfprExtmgmtNdiscTargetsDn_Type())
cfprExtmgmtNdiscTargetsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsDn.setStatus(_A)
_CfprExtmgmtNdiscTargetsRn_Type=SnmpAdminString
_CfprExtmgmtNdiscTargetsRn_Object=MibTableColumn
cfprExtmgmtNdiscTargetsRn=_CfprExtmgmtNdiscTargetsRn_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,3),_CfprExtmgmtNdiscTargetsRn_Type())
cfprExtmgmtNdiscTargetsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsRn.setStatus(_A)
_CfprExtmgmtNdiscTargetsConfigState_Type=CfprAaaConfigState
_CfprExtmgmtNdiscTargetsConfigState_Object=MibTableColumn
cfprExtmgmtNdiscTargetsConfigState=_CfprExtmgmtNdiscTargetsConfigState_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,4),_CfprExtmgmtNdiscTargetsConfigState_Type())
cfprExtmgmtNdiscTargetsConfigState.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsConfigState.setStatus(_A)
_CfprExtmgmtNdiscTargetsConfigStatusMessage_Type=SnmpAdminString
_CfprExtmgmtNdiscTargetsConfigStatusMessage_Object=MibTableColumn
cfprExtmgmtNdiscTargetsConfigStatusMessage=_CfprExtmgmtNdiscTargetsConfigStatusMessage_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,5),_CfprExtmgmtNdiscTargetsConfigStatusMessage_Type())
cfprExtmgmtNdiscTargetsConfigStatusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsConfigStatusMessage.setStatus(_A)
_CfprExtmgmtNdiscTargetsIpv6Target1_Type=InetAddressIPv6
_CfprExtmgmtNdiscTargetsIpv6Target1_Object=MibTableColumn
cfprExtmgmtNdiscTargetsIpv6Target1=_CfprExtmgmtNdiscTargetsIpv6Target1_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,6),_CfprExtmgmtNdiscTargetsIpv6Target1_Type())
cfprExtmgmtNdiscTargetsIpv6Target1.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsIpv6Target1.setStatus(_A)
_CfprExtmgmtNdiscTargetsIpv6Target2_Type=InetAddressIPv6
_CfprExtmgmtNdiscTargetsIpv6Target2_Object=MibTableColumn
cfprExtmgmtNdiscTargetsIpv6Target2=_CfprExtmgmtNdiscTargetsIpv6Target2_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,7),_CfprExtmgmtNdiscTargetsIpv6Target2_Type())
cfprExtmgmtNdiscTargetsIpv6Target2.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsIpv6Target2.setStatus(_A)
_CfprExtmgmtNdiscTargetsIpv6Target3_Type=InetAddressIPv6
_CfprExtmgmtNdiscTargetsIpv6Target3_Object=MibTableColumn
cfprExtmgmtNdiscTargetsIpv6Target3=_CfprExtmgmtNdiscTargetsIpv6Target3_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,8),_CfprExtmgmtNdiscTargetsIpv6Target3_Type())
cfprExtmgmtNdiscTargetsIpv6Target3.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsIpv6Target3.setStatus(_A)
_CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Type=CfprExtmgmtNdiscTargetsMaxDeadlineTimeout
_CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Object=MibTableColumn
cfprExtmgmtNdiscTargetsMaxDeadlineTimeout=_CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,9),_CfprExtmgmtNdiscTargetsMaxDeadlineTimeout_Type())
cfprExtmgmtNdiscTargetsMaxDeadlineTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsMaxDeadlineTimeout.setStatus(_A)
_CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Type=CfprExtmgmtNdiscTargetsNumberOfNdiscRequests
_CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Object=MibTableColumn
cfprExtmgmtNdiscTargetsNumberOfNdiscRequests=_CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Object((1,3,6,1,4,1,9,9,826,1,23,6,1,10),_CfprExtmgmtNdiscTargetsNumberOfNdiscRequests_Type())
cfprExtmgmtNdiscTargetsNumberOfNdiscRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprExtmgmtNdiscTargetsNumberOfNdiscRequests.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprExtmgmtObjects':cfprExtmgmtObjects,'cfprExtmgmtArpTargetsTable':cfprExtmgmtArpTargetsTable,'cfprExtmgmtArpTargetsEntry':cfprExtmgmtArpTargetsEntry,_E:cfprExtmgmtArpTargetsInstanceId,'cfprExtmgmtArpTargetsDn':cfprExtmgmtArpTargetsDn,'cfprExtmgmtArpTargetsRn':cfprExtmgmtArpTargetsRn,'cfprExtmgmtArpTargetsConfigState':cfprExtmgmtArpTargetsConfigState,'cfprExtmgmtArpTargetsConfigStatusMessage':cfprExtmgmtArpTargetsConfigStatusMessage,'cfprExtmgmtArpTargetsMaxDeadlineTimeout':cfprExtmgmtArpTargetsMaxDeadlineTimeout,'cfprExtmgmtArpTargetsNumberOfArpRequests':cfprExtmgmtArpTargetsNumberOfArpRequests,'cfprExtmgmtArpTargetsTargetIp1':cfprExtmgmtArpTargetsTargetIp1,'cfprExtmgmtArpTargetsTargetIp2':cfprExtmgmtArpTargetsTargetIp2,'cfprExtmgmtArpTargetsTargetIp3':cfprExtmgmtArpTargetsTargetIp3,'cfprExtmgmtGatewayPingTable':cfprExtmgmtGatewayPingTable,'cfprExtmgmtGatewayPingEntry':cfprExtmgmtGatewayPingEntry,_F:cfprExtmgmtGatewayPingInstanceId,'cfprExtmgmtGatewayPingDn':cfprExtmgmtGatewayPingDn,'cfprExtmgmtGatewayPingRn':cfprExtmgmtGatewayPingRn,'cfprExtmgmtGatewayPingMaxDeadlineTimeout':cfprExtmgmtGatewayPingMaxDeadlineTimeout,'cfprExtmgmtGatewayPingNumberOfPingRequests':cfprExtmgmtGatewayPingNumberOfPingRequests,'cfprExtmgmtIfTable':cfprExtmgmtIfTable,'cfprExtmgmtIfEntry':cfprExtmgmtIfEntry,_G:cfprExtmgmtIfInstanceId,'cfprExtmgmtIfDn':cfprExtmgmtIfDn,'cfprExtmgmtIfRn':cfprExtmgmtIfRn,'cfprExtmgmtIfEpDn':cfprExtmgmtIfEpDn,'cfprExtmgmtIfFailReportCount':cfprExtmgmtIfFailReportCount,'cfprExtmgmtIfFltAggr':cfprExtmgmtIfFltAggr,'cfprExtmgmtIfId':cfprExtmgmtIfId,'cfprExtmgmtIfIfRole':cfprExtmgmtIfIfRole,'cfprExtmgmtIfIfType':cfprExtmgmtIfIfType,'cfprExtmgmtIfLastOperStateReport':cfprExtmgmtIfLastOperStateReport,'cfprExtmgmtIfLocale':cfprExtmgmtIfLocale,'cfprExtmgmtIfName':cfprExtmgmtIfName,'cfprExtmgmtIfOperState':cfprExtmgmtIfOperState,'cfprExtmgmtIfPeerDn':cfprExtmgmtIfPeerDn,'cfprExtmgmtIfTransport':cfprExtmgmtIfTransport,'cfprExtmgmtIfType':cfprExtmgmtIfType,'cfprExtmgmtIfMonPolicyTable':cfprExtmgmtIfMonPolicyTable,'cfprExtmgmtIfMonPolicyEntry':cfprExtmgmtIfMonPolicyEntry,_H:cfprExtmgmtIfMonPolicyInstanceId,'cfprExtmgmtIfMonPolicyDn':cfprExtmgmtIfMonPolicyDn,'cfprExtmgmtIfMonPolicyRn':cfprExtmgmtIfMonPolicyRn,'cfprExtmgmtIfMonPolicyAdminState':cfprExtmgmtIfMonPolicyAdminState,'cfprExtmgmtIfMonPolicyDescr':cfprExtmgmtIfMonPolicyDescr,'cfprExtmgmtIfMonPolicyEnableHAFailover':cfprExtmgmtIfMonPolicyEnableHAFailover,'cfprExtmgmtIfMonPolicyIntId':cfprExtmgmtIfMonPolicyIntId,'cfprExtmgmtIfMonPolicyMaxFailReportCount':cfprExtmgmtIfMonPolicyMaxFailReportCount,'cfprExtmgmtIfMonPolicyMonitorMechanism':cfprExtmgmtIfMonPolicyMonitorMechanism,'cfprExtmgmtIfMonPolicyName':cfprExtmgmtIfMonPolicyName,'cfprExtmgmtIfMonPolicyPolicyLevel':cfprExtmgmtIfMonPolicyPolicyLevel,'cfprExtmgmtIfMonPolicyPolicyOwner':cfprExtmgmtIfMonPolicyPolicyOwner,'cfprExtmgmtIfMonPolicyPollInterval':cfprExtmgmtIfMonPolicyPollInterval,'cfprExtmgmtMiiStatusTable':cfprExtmgmtMiiStatusTable,'cfprExtmgmtMiiStatusEntry':cfprExtmgmtMiiStatusEntry,_I:cfprExtmgmtMiiStatusInstanceId,'cfprExtmgmtMiiStatusDn':cfprExtmgmtMiiStatusDn,'cfprExtmgmtMiiStatusRn':cfprExtmgmtMiiStatusRn,'cfprExtmgmtMiiStatusMaxRetryCount':cfprExtmgmtMiiStatusMaxRetryCount,'cfprExtmgmtMiiStatusRetryInterval':cfprExtmgmtMiiStatusRetryInterval,'cfprExtmgmtNdiscTargetsTable':cfprExtmgmtNdiscTargetsTable,'cfprExtmgmtNdiscTargetsEntry':cfprExtmgmtNdiscTargetsEntry,_J:cfprExtmgmtNdiscTargetsInstanceId,'cfprExtmgmtNdiscTargetsDn':cfprExtmgmtNdiscTargetsDn,'cfprExtmgmtNdiscTargetsRn':cfprExtmgmtNdiscTargetsRn,'cfprExtmgmtNdiscTargetsConfigState':cfprExtmgmtNdiscTargetsConfigState,'cfprExtmgmtNdiscTargetsConfigStatusMessage':cfprExtmgmtNdiscTargetsConfigStatusMessage,'cfprExtmgmtNdiscTargetsIpv6Target1':cfprExtmgmtNdiscTargetsIpv6Target1,'cfprExtmgmtNdiscTargetsIpv6Target2':cfprExtmgmtNdiscTargetsIpv6Target2,'cfprExtmgmtNdiscTargetsIpv6Target3':cfprExtmgmtNdiscTargetsIpv6Target3,'cfprExtmgmtNdiscTargetsMaxDeadlineTimeout':cfprExtmgmtNdiscTargetsMaxDeadlineTimeout,'cfprExtmgmtNdiscTargetsNumberOfNdiscRequests':cfprExtmgmtNdiscTargetsNumberOfNdiscRequests})