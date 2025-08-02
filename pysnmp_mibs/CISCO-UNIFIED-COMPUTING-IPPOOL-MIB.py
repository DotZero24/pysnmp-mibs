_M='cucsIppoolIpV6PooledInstanceId'
_L='cucsIppoolIpV6BlockInstanceId'
_K='cucsIppoolIpV6AddrInstanceId'
_J='cucsIppoolUniverseInstanceId'
_I='cucsIppoolPooledInstanceId'
_H='cucsIppoolPoolableInstanceId'
_G='cucsIppoolPoolInstanceId'
_F='cucsIppoolBlockInstanceId'
_E='cucsIppoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-IPPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsIppoolDHCPMode,CucsIppoolManagementMode,CucsIppoolNetBIOSMode,CucsIppoolPoolAssignmentOrder,CucsPolicyPolicyOwner,CucsPoolElementOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsIppoolDHCPMode','CucsIppoolManagementMode','CucsIppoolNetBIOSMode','CucsIppoolPoolAssignmentOrder','CucsPolicyPolicyOwner','CucsPoolElementOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsIppoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,24))
_CucsIppoolAddrTable_Object=MibTable
cucsIppoolAddrTable=_CucsIppoolAddrTable_Object((1,3,6,1,4,1,9,9,719,1,24,1))
if mibBuilder.loadTexts:cucsIppoolAddrTable.setStatus(_A)
_CucsIppoolAddrEntry_Object=MibTableRow
cucsIppoolAddrEntry=_CucsIppoolAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,24,1,1))
cucsIppoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsIppoolAddrEntry.setStatus(_A)
_CucsIppoolAddrInstanceId_Type=CucsManagedObjectId
_CucsIppoolAddrInstanceId_Object=MibTableColumn
cucsIppoolAddrInstanceId=_CucsIppoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,1),_CucsIppoolAddrInstanceId_Type())
cucsIppoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolAddrInstanceId.setStatus(_A)
_CucsIppoolAddrDn_Type=CucsManagedObjectDn
_CucsIppoolAddrDn_Object=MibTableColumn
cucsIppoolAddrDn=_CucsIppoolAddrDn_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,2),_CucsIppoolAddrDn_Type())
cucsIppoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrDn.setStatus(_A)
_CucsIppoolAddrRn_Type=SnmpAdminString
_CucsIppoolAddrRn_Object=MibTableColumn
cucsIppoolAddrRn=_CucsIppoolAddrRn_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,3),_CucsIppoolAddrRn_Type())
cucsIppoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrRn.setStatus(_A)
_CucsIppoolAddrAssigned_Type=TruthValue
_CucsIppoolAddrAssigned_Object=MibTableColumn
cucsIppoolAddrAssigned=_CucsIppoolAddrAssigned_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,4),_CucsIppoolAddrAssigned_Type())
cucsIppoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrAssigned.setStatus(_A)
_CucsIppoolAddrAssignedToDn_Type=SnmpAdminString
_CucsIppoolAddrAssignedToDn_Object=MibTableColumn
cucsIppoolAddrAssignedToDn=_CucsIppoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,5),_CucsIppoolAddrAssignedToDn_Type())
cucsIppoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrAssignedToDn.setStatus(_A)
_CucsIppoolAddrId_Type=InetAddressIPv4
_CucsIppoolAddrId_Object=MibTableColumn
cucsIppoolAddrId=_CucsIppoolAddrId_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,6),_CucsIppoolAddrId_Type())
cucsIppoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrId.setStatus(_A)
_CucsIppoolAddrOwner_Type=CucsPoolElementOwner
_CucsIppoolAddrOwner_Object=MibTableColumn
cucsIppoolAddrOwner=_CucsIppoolAddrOwner_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,7),_CucsIppoolAddrOwner_Type())
cucsIppoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrOwner.setStatus(_A)
_CucsIppoolAddrGlobalAssignedCnt_Type=Gauge32
_CucsIppoolAddrGlobalAssignedCnt_Object=MibTableColumn
cucsIppoolAddrGlobalAssignedCnt=_CucsIppoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,8),_CucsIppoolAddrGlobalAssignedCnt_Type())
cucsIppoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrGlobalAssignedCnt.setStatus(_A)
_CucsIppoolAddrGlobalDefinedCnt_Type=Gauge32
_CucsIppoolAddrGlobalDefinedCnt_Object=MibTableColumn
cucsIppoolAddrGlobalDefinedCnt=_CucsIppoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,719,1,24,1,1,9),_CucsIppoolAddrGlobalDefinedCnt_Type())
cucsIppoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolAddrGlobalDefinedCnt.setStatus(_A)
_CucsIppoolBlockTable_Object=MibTable
cucsIppoolBlockTable=_CucsIppoolBlockTable_Object((1,3,6,1,4,1,9,9,719,1,24,2))
if mibBuilder.loadTexts:cucsIppoolBlockTable.setStatus(_A)
_CucsIppoolBlockEntry_Object=MibTableRow
cucsIppoolBlockEntry=_CucsIppoolBlockEntry_Object((1,3,6,1,4,1,9,9,719,1,24,2,1))
cucsIppoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsIppoolBlockEntry.setStatus(_A)
_CucsIppoolBlockInstanceId_Type=CucsManagedObjectId
_CucsIppoolBlockInstanceId_Object=MibTableColumn
cucsIppoolBlockInstanceId=_CucsIppoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,1),_CucsIppoolBlockInstanceId_Type())
cucsIppoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolBlockInstanceId.setStatus(_A)
_CucsIppoolBlockDn_Type=CucsManagedObjectDn
_CucsIppoolBlockDn_Object=MibTableColumn
cucsIppoolBlockDn=_CucsIppoolBlockDn_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,2),_CucsIppoolBlockDn_Type())
cucsIppoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockDn.setStatus(_A)
_CucsIppoolBlockRn_Type=SnmpAdminString
_CucsIppoolBlockRn_Object=MibTableColumn
cucsIppoolBlockRn=_CucsIppoolBlockRn_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,3),_CucsIppoolBlockRn_Type())
cucsIppoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockRn.setStatus(_A)
_CucsIppoolBlockDefGw_Type=InetAddressIPv4
_CucsIppoolBlockDefGw_Object=MibTableColumn
cucsIppoolBlockDefGw=_CucsIppoolBlockDefGw_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,4),_CucsIppoolBlockDefGw_Type())
cucsIppoolBlockDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockDefGw.setStatus(_A)
_CucsIppoolBlockFrom_Type=InetAddressIPv4
_CucsIppoolBlockFrom_Object=MibTableColumn
cucsIppoolBlockFrom=_CucsIppoolBlockFrom_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,5),_CucsIppoolBlockFrom_Type())
cucsIppoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockFrom.setStatus(_A)
_CucsIppoolBlockSubnet_Type=InetAddressIPv4
_CucsIppoolBlockSubnet_Object=MibTableColumn
cucsIppoolBlockSubnet=_CucsIppoolBlockSubnet_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,6),_CucsIppoolBlockSubnet_Type())
cucsIppoolBlockSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockSubnet.setStatus(_A)
_CucsIppoolBlockTo_Type=InetAddressIPv4
_CucsIppoolBlockTo_Object=MibTableColumn
cucsIppoolBlockTo=_CucsIppoolBlockTo_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,7),_CucsIppoolBlockTo_Type())
cucsIppoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockTo.setStatus(_A)
_CucsIppoolBlockPrimDns_Type=InetAddressIPv4
_CucsIppoolBlockPrimDns_Object=MibTableColumn
cucsIppoolBlockPrimDns=_CucsIppoolBlockPrimDns_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,8),_CucsIppoolBlockPrimDns_Type())
cucsIppoolBlockPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockPrimDns.setStatus(_A)
_CucsIppoolBlockSecDns_Type=InetAddressIPv4
_CucsIppoolBlockSecDns_Object=MibTableColumn
cucsIppoolBlockSecDns=_CucsIppoolBlockSecDns_Object((1,3,6,1,4,1,9,9,719,1,24,2,1,9),_CucsIppoolBlockSecDns_Type())
cucsIppoolBlockSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolBlockSecDns.setStatus(_A)
_CucsIppoolPoolTable_Object=MibTable
cucsIppoolPoolTable=_CucsIppoolPoolTable_Object((1,3,6,1,4,1,9,9,719,1,24,3))
if mibBuilder.loadTexts:cucsIppoolPoolTable.setStatus(_A)
_CucsIppoolPoolEntry_Object=MibTableRow
cucsIppoolPoolEntry=_CucsIppoolPoolEntry_Object((1,3,6,1,4,1,9,9,719,1,24,3,1))
cucsIppoolPoolEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsIppoolPoolEntry.setStatus(_A)
_CucsIppoolPoolInstanceId_Type=CucsManagedObjectId
_CucsIppoolPoolInstanceId_Object=MibTableColumn
cucsIppoolPoolInstanceId=_CucsIppoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,1),_CucsIppoolPoolInstanceId_Type())
cucsIppoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolPoolInstanceId.setStatus(_A)
_CucsIppoolPoolDn_Type=CucsManagedObjectDn
_CucsIppoolPoolDn_Object=MibTableColumn
cucsIppoolPoolDn=_CucsIppoolPoolDn_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,2),_CucsIppoolPoolDn_Type())
cucsIppoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolDn.setStatus(_A)
_CucsIppoolPoolRn_Type=SnmpAdminString
_CucsIppoolPoolRn_Object=MibTableColumn
cucsIppoolPoolRn=_CucsIppoolPoolRn_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,3),_CucsIppoolPoolRn_Type())
cucsIppoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolRn.setStatus(_A)
_CucsIppoolPoolAssigned_Type=Gauge32
_CucsIppoolPoolAssigned_Object=MibTableColumn
cucsIppoolPoolAssigned=_CucsIppoolPoolAssigned_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,4),_CucsIppoolPoolAssigned_Type())
cucsIppoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolAssigned.setStatus(_A)
_CucsIppoolPoolDescr_Type=SnmpAdminString
_CucsIppoolPoolDescr_Object=MibTableColumn
cucsIppoolPoolDescr=_CucsIppoolPoolDescr_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,5),_CucsIppoolPoolDescr_Type())
cucsIppoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolDescr.setStatus(_A)
_CucsIppoolPoolIntId_Type=SnmpAdminString
_CucsIppoolPoolIntId_Object=MibTableColumn
cucsIppoolPoolIntId=_CucsIppoolPoolIntId_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,6),_CucsIppoolPoolIntId_Type())
cucsIppoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolIntId.setStatus(_A)
_CucsIppoolPoolName_Type=SnmpAdminString
_CucsIppoolPoolName_Object=MibTableColumn
cucsIppoolPoolName=_CucsIppoolPoolName_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,7),_CucsIppoolPoolName_Type())
cucsIppoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolName.setStatus(_A)
_CucsIppoolPoolSize_Type=Gauge32
_CucsIppoolPoolSize_Object=MibTableColumn
cucsIppoolPoolSize=_CucsIppoolPoolSize_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,8),_CucsIppoolPoolSize_Type())
cucsIppoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolSize.setStatus(_A)
_CucsIppoolPoolAssignmentOrder_Type=CucsIppoolPoolAssignmentOrder
_CucsIppoolPoolAssignmentOrder_Object=MibTableColumn
cucsIppoolPoolAssignmentOrder=_CucsIppoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,9),_CucsIppoolPoolAssignmentOrder_Type())
cucsIppoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolAssignmentOrder.setStatus(_A)
_CucsIppoolPoolPolicyLevel_Type=Gauge32
_CucsIppoolPoolPolicyLevel_Object=MibTableColumn
cucsIppoolPoolPolicyLevel=_CucsIppoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,10),_CucsIppoolPoolPolicyLevel_Type())
cucsIppoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolPolicyLevel.setStatus(_A)
_CucsIppoolPoolPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsIppoolPoolPolicyOwner_Object=MibTableColumn
cucsIppoolPoolPolicyOwner=_CucsIppoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,11),_CucsIppoolPoolPolicyOwner_Type())
cucsIppoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolPolicyOwner.setStatus(_A)
_CucsIppoolPoolExtManaged_Type=CucsIppoolManagementMode
_CucsIppoolPoolExtManaged_Object=MibTableColumn
cucsIppoolPoolExtManaged=_CucsIppoolPoolExtManaged_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,12),_CucsIppoolPoolExtManaged_Type())
cucsIppoolPoolExtManaged.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolExtManaged.setStatus(_A)
_CucsIppoolPoolGuid_Type=SnmpAdminString
_CucsIppoolPoolGuid_Object=MibTableColumn
cucsIppoolPoolGuid=_CucsIppoolPoolGuid_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,13),_CucsIppoolPoolGuid_Type())
cucsIppoolPoolGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolGuid.setStatus(_A)
_CucsIppoolPoolIsNetBIOSEnabled_Type=CucsIppoolNetBIOSMode
_CucsIppoolPoolIsNetBIOSEnabled_Object=MibTableColumn
cucsIppoolPoolIsNetBIOSEnabled=_CucsIppoolPoolIsNetBIOSEnabled_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,14),_CucsIppoolPoolIsNetBIOSEnabled_Type())
cucsIppoolPoolIsNetBIOSEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolIsNetBIOSEnabled.setStatus(_A)
_CucsIppoolPoolSupportsDHCP_Type=CucsIppoolDHCPMode
_CucsIppoolPoolSupportsDHCP_Object=MibTableColumn
cucsIppoolPoolSupportsDHCP=_CucsIppoolPoolSupportsDHCP_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,15),_CucsIppoolPoolSupportsDHCP_Type())
cucsIppoolPoolSupportsDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolSupportsDHCP.setStatus(_A)
_CucsIppoolPoolV4Assigned_Type=Gauge32
_CucsIppoolPoolV4Assigned_Object=MibTableColumn
cucsIppoolPoolV4Assigned=_CucsIppoolPoolV4Assigned_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,16),_CucsIppoolPoolV4Assigned_Type())
cucsIppoolPoolV4Assigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolV4Assigned.setStatus(_A)
_CucsIppoolPoolV4Size_Type=Gauge32
_CucsIppoolPoolV4Size_Object=MibTableColumn
cucsIppoolPoolV4Size=_CucsIppoolPoolV4Size_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,17),_CucsIppoolPoolV4Size_Type())
cucsIppoolPoolV4Size.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolV4Size.setStatus(_A)
_CucsIppoolPoolV6Assigned_Type=Gauge32
_CucsIppoolPoolV6Assigned_Object=MibTableColumn
cucsIppoolPoolV6Assigned=_CucsIppoolPoolV6Assigned_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,18),_CucsIppoolPoolV6Assigned_Type())
cucsIppoolPoolV6Assigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolV6Assigned.setStatus(_A)
_CucsIppoolPoolV6Size_Type=Gauge32
_CucsIppoolPoolV6Size_Object=MibTableColumn
cucsIppoolPoolV6Size=_CucsIppoolPoolV6Size_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,19),_CucsIppoolPoolV6Size_Type())
cucsIppoolPoolV6Size.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolV6Size.setStatus(_A)
_CucsIppoolPoolPropAcl_Type=Unsigned64
_CucsIppoolPoolPropAcl_Object=MibTableColumn
cucsIppoolPoolPropAcl=_CucsIppoolPoolPropAcl_Object((1,3,6,1,4,1,9,9,719,1,24,3,1,20),_CucsIppoolPoolPropAcl_Type())
cucsIppoolPoolPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolPropAcl.setStatus(_A)
_CucsIppoolPoolableTable_Object=MibTable
cucsIppoolPoolableTable=_CucsIppoolPoolableTable_Object((1,3,6,1,4,1,9,9,719,1,24,4))
if mibBuilder.loadTexts:cucsIppoolPoolableTable.setStatus(_A)
_CucsIppoolPoolableEntry_Object=MibTableRow
cucsIppoolPoolableEntry=_CucsIppoolPoolableEntry_Object((1,3,6,1,4,1,9,9,719,1,24,4,1))
cucsIppoolPoolableEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsIppoolPoolableEntry.setStatus(_A)
_CucsIppoolPoolableInstanceId_Type=CucsManagedObjectId
_CucsIppoolPoolableInstanceId_Object=MibTableColumn
cucsIppoolPoolableInstanceId=_CucsIppoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,4,1,1),_CucsIppoolPoolableInstanceId_Type())
cucsIppoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolPoolableInstanceId.setStatus(_A)
_CucsIppoolPoolableDn_Type=CucsManagedObjectDn
_CucsIppoolPoolableDn_Object=MibTableColumn
cucsIppoolPoolableDn=_CucsIppoolPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,24,4,1,2),_CucsIppoolPoolableDn_Type())
cucsIppoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolableDn.setStatus(_A)
_CucsIppoolPoolableRn_Type=SnmpAdminString
_CucsIppoolPoolableRn_Object=MibTableColumn
cucsIppoolPoolableRn=_CucsIppoolPoolableRn_Object((1,3,6,1,4,1,9,9,719,1,24,4,1,3),_CucsIppoolPoolableRn_Type())
cucsIppoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolableRn.setStatus(_A)
_CucsIppoolPoolableId_Type=Unsigned64
_CucsIppoolPoolableId_Object=MibTableColumn
cucsIppoolPoolableId=_CucsIppoolPoolableId_Object((1,3,6,1,4,1,9,9,719,1,24,4,1,4),_CucsIppoolPoolableId_Type())
cucsIppoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolableId.setStatus(_A)
_CucsIppoolPoolablePoolDn_Type=SnmpAdminString
_CucsIppoolPoolablePoolDn_Object=MibTableColumn
cucsIppoolPoolablePoolDn=_CucsIppoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,719,1,24,4,1,5),_CucsIppoolPoolablePoolDn_Type())
cucsIppoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPoolablePoolDn.setStatus(_A)
_CucsIppoolPooledTable_Object=MibTable
cucsIppoolPooledTable=_CucsIppoolPooledTable_Object((1,3,6,1,4,1,9,9,719,1,24,5))
if mibBuilder.loadTexts:cucsIppoolPooledTable.setStatus(_A)
_CucsIppoolPooledEntry_Object=MibTableRow
cucsIppoolPooledEntry=_CucsIppoolPooledEntry_Object((1,3,6,1,4,1,9,9,719,1,24,5,1))
cucsIppoolPooledEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsIppoolPooledEntry.setStatus(_A)
_CucsIppoolPooledInstanceId_Type=CucsManagedObjectId
_CucsIppoolPooledInstanceId_Object=MibTableColumn
cucsIppoolPooledInstanceId=_CucsIppoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,1),_CucsIppoolPooledInstanceId_Type())
cucsIppoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolPooledInstanceId.setStatus(_A)
_CucsIppoolPooledDn_Type=CucsManagedObjectDn
_CucsIppoolPooledDn_Object=MibTableColumn
cucsIppoolPooledDn=_CucsIppoolPooledDn_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,2),_CucsIppoolPooledDn_Type())
cucsIppoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledDn.setStatus(_A)
_CucsIppoolPooledRn_Type=SnmpAdminString
_CucsIppoolPooledRn_Object=MibTableColumn
cucsIppoolPooledRn=_CucsIppoolPooledRn_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,3),_CucsIppoolPooledRn_Type())
cucsIppoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledRn.setStatus(_A)
_CucsIppoolPooledAssigned_Type=TruthValue
_CucsIppoolPooledAssigned_Object=MibTableColumn
cucsIppoolPooledAssigned=_CucsIppoolPooledAssigned_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,4),_CucsIppoolPooledAssigned_Type())
cucsIppoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledAssigned.setStatus(_A)
_CucsIppoolPooledAssignedToDn_Type=SnmpAdminString
_CucsIppoolPooledAssignedToDn_Object=MibTableColumn
cucsIppoolPooledAssignedToDn=_CucsIppoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,5),_CucsIppoolPooledAssignedToDn_Type())
cucsIppoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledAssignedToDn.setStatus(_A)
_CucsIppoolPooledDefGw_Type=InetAddressIPv4
_CucsIppoolPooledDefGw_Object=MibTableColumn
cucsIppoolPooledDefGw=_CucsIppoolPooledDefGw_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,6),_CucsIppoolPooledDefGw_Type())
cucsIppoolPooledDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledDefGw.setStatus(_A)
_CucsIppoolPooledId_Type=InetAddressIPv4
_CucsIppoolPooledId_Object=MibTableColumn
cucsIppoolPooledId=_CucsIppoolPooledId_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,7),_CucsIppoolPooledId_Type())
cucsIppoolPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledId.setStatus(_A)
_CucsIppoolPooledPoolableDn_Type=SnmpAdminString
_CucsIppoolPooledPoolableDn_Object=MibTableColumn
cucsIppoolPooledPoolableDn=_CucsIppoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,8),_CucsIppoolPooledPoolableDn_Type())
cucsIppoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledPoolableDn.setStatus(_A)
_CucsIppoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CucsIppoolPooledPrevAssignedToDn_Object=MibTableColumn
cucsIppoolPooledPrevAssignedToDn=_CucsIppoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,9),_CucsIppoolPooledPrevAssignedToDn_Type())
cucsIppoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledPrevAssignedToDn.setStatus(_A)
_CucsIppoolPooledSubnet_Type=InetAddressIPv4
_CucsIppoolPooledSubnet_Object=MibTableColumn
cucsIppoolPooledSubnet=_CucsIppoolPooledSubnet_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,10),_CucsIppoolPooledSubnet_Type())
cucsIppoolPooledSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledSubnet.setStatus(_A)
_CucsIppoolPooledPrimDns_Type=InetAddressIPv4
_CucsIppoolPooledPrimDns_Object=MibTableColumn
cucsIppoolPooledPrimDns=_CucsIppoolPooledPrimDns_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,11),_CucsIppoolPooledPrimDns_Type())
cucsIppoolPooledPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledPrimDns.setStatus(_A)
_CucsIppoolPooledSecDns_Type=InetAddressIPv4
_CucsIppoolPooledSecDns_Object=MibTableColumn
cucsIppoolPooledSecDns=_CucsIppoolPooledSecDns_Object((1,3,6,1,4,1,9,9,719,1,24,5,1,12),_CucsIppoolPooledSecDns_Type())
cucsIppoolPooledSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolPooledSecDns.setStatus(_A)
_CucsIppoolUniverseTable_Object=MibTable
cucsIppoolUniverseTable=_CucsIppoolUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,24,6))
if mibBuilder.loadTexts:cucsIppoolUniverseTable.setStatus(_A)
_CucsIppoolUniverseEntry_Object=MibTableRow
cucsIppoolUniverseEntry=_CucsIppoolUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,24,6,1))
cucsIppoolUniverseEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsIppoolUniverseEntry.setStatus(_A)
_CucsIppoolUniverseInstanceId_Type=CucsManagedObjectId
_CucsIppoolUniverseInstanceId_Object=MibTableColumn
cucsIppoolUniverseInstanceId=_CucsIppoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,6,1,1),_CucsIppoolUniverseInstanceId_Type())
cucsIppoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolUniverseInstanceId.setStatus(_A)
_CucsIppoolUniverseDn_Type=CucsManagedObjectDn
_CucsIppoolUniverseDn_Object=MibTableColumn
cucsIppoolUniverseDn=_CucsIppoolUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,24,6,1,2),_CucsIppoolUniverseDn_Type())
cucsIppoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolUniverseDn.setStatus(_A)
_CucsIppoolUniverseRn_Type=SnmpAdminString
_CucsIppoolUniverseRn_Object=MibTableColumn
cucsIppoolUniverseRn=_CucsIppoolUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,24,6,1,3),_CucsIppoolUniverseRn_Type())
cucsIppoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolUniverseRn.setStatus(_A)
_CucsIppoolIpV6AddrTable_Object=MibTable
cucsIppoolIpV6AddrTable=_CucsIppoolIpV6AddrTable_Object((1,3,6,1,4,1,9,9,719,1,24,7))
if mibBuilder.loadTexts:cucsIppoolIpV6AddrTable.setStatus(_A)
_CucsIppoolIpV6AddrEntry_Object=MibTableRow
cucsIppoolIpV6AddrEntry=_CucsIppoolIpV6AddrEntry_Object((1,3,6,1,4,1,9,9,719,1,24,7,1))
cucsIppoolIpV6AddrEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsIppoolIpV6AddrEntry.setStatus(_A)
_CucsIppoolIpV6AddrInstanceId_Type=CucsManagedObjectId
_CucsIppoolIpV6AddrInstanceId_Object=MibTableColumn
cucsIppoolIpV6AddrInstanceId=_CucsIppoolIpV6AddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,1),_CucsIppoolIpV6AddrInstanceId_Type())
cucsIppoolIpV6AddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrInstanceId.setStatus(_A)
_CucsIppoolIpV6AddrDn_Type=CucsManagedObjectDn
_CucsIppoolIpV6AddrDn_Object=MibTableColumn
cucsIppoolIpV6AddrDn=_CucsIppoolIpV6AddrDn_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,2),_CucsIppoolIpV6AddrDn_Type())
cucsIppoolIpV6AddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrDn.setStatus(_A)
_CucsIppoolIpV6AddrRn_Type=SnmpAdminString
_CucsIppoolIpV6AddrRn_Object=MibTableColumn
cucsIppoolIpV6AddrRn=_CucsIppoolIpV6AddrRn_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,3),_CucsIppoolIpV6AddrRn_Type())
cucsIppoolIpV6AddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrRn.setStatus(_A)
_CucsIppoolIpV6AddrAssigned_Type=TruthValue
_CucsIppoolIpV6AddrAssigned_Object=MibTableColumn
cucsIppoolIpV6AddrAssigned=_CucsIppoolIpV6AddrAssigned_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,4),_CucsIppoolIpV6AddrAssigned_Type())
cucsIppoolIpV6AddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrAssigned.setStatus(_A)
_CucsIppoolIpV6AddrAssignedToDn_Type=SnmpAdminString
_CucsIppoolIpV6AddrAssignedToDn_Object=MibTableColumn
cucsIppoolIpV6AddrAssignedToDn=_CucsIppoolIpV6AddrAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,5),_CucsIppoolIpV6AddrAssignedToDn_Type())
cucsIppoolIpV6AddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrAssignedToDn.setStatus(_A)
_CucsIppoolIpV6AddrId_Type=InetAddressIPv6
_CucsIppoolIpV6AddrId_Object=MibTableColumn
cucsIppoolIpV6AddrId=_CucsIppoolIpV6AddrId_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,6),_CucsIppoolIpV6AddrId_Type())
cucsIppoolIpV6AddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrId.setStatus(_A)
_CucsIppoolIpV6AddrOwner_Type=CucsPoolElementOwner
_CucsIppoolIpV6AddrOwner_Object=MibTableColumn
cucsIppoolIpV6AddrOwner=_CucsIppoolIpV6AddrOwner_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,7),_CucsIppoolIpV6AddrOwner_Type())
cucsIppoolIpV6AddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrOwner.setStatus(_A)
_CucsIppoolIpV6AddrGlobalAssignedCnt_Type=Gauge32
_CucsIppoolIpV6AddrGlobalAssignedCnt_Object=MibTableColumn
cucsIppoolIpV6AddrGlobalAssignedCnt=_CucsIppoolIpV6AddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,8),_CucsIppoolIpV6AddrGlobalAssignedCnt_Type())
cucsIppoolIpV6AddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrGlobalAssignedCnt.setStatus(_A)
_CucsIppoolIpV6AddrGlobalDefinedCnt_Type=Gauge32
_CucsIppoolIpV6AddrGlobalDefinedCnt_Object=MibTableColumn
cucsIppoolIpV6AddrGlobalDefinedCnt=_CucsIppoolIpV6AddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,719,1,24,7,1,9),_CucsIppoolIpV6AddrGlobalDefinedCnt_Type())
cucsIppoolIpV6AddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6AddrGlobalDefinedCnt.setStatus(_A)
_CucsIppoolIpV6BlockTable_Object=MibTable
cucsIppoolIpV6BlockTable=_CucsIppoolIpV6BlockTable_Object((1,3,6,1,4,1,9,9,719,1,24,8))
if mibBuilder.loadTexts:cucsIppoolIpV6BlockTable.setStatus(_A)
_CucsIppoolIpV6BlockEntry_Object=MibTableRow
cucsIppoolIpV6BlockEntry=_CucsIppoolIpV6BlockEntry_Object((1,3,6,1,4,1,9,9,719,1,24,8,1))
cucsIppoolIpV6BlockEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsIppoolIpV6BlockEntry.setStatus(_A)
_CucsIppoolIpV6BlockInstanceId_Type=CucsManagedObjectId
_CucsIppoolIpV6BlockInstanceId_Object=MibTableColumn
cucsIppoolIpV6BlockInstanceId=_CucsIppoolIpV6BlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,1),_CucsIppoolIpV6BlockInstanceId_Type())
cucsIppoolIpV6BlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockInstanceId.setStatus(_A)
_CucsIppoolIpV6BlockDn_Type=CucsManagedObjectDn
_CucsIppoolIpV6BlockDn_Object=MibTableColumn
cucsIppoolIpV6BlockDn=_CucsIppoolIpV6BlockDn_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,2),_CucsIppoolIpV6BlockDn_Type())
cucsIppoolIpV6BlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockDn.setStatus(_A)
_CucsIppoolIpV6BlockRn_Type=SnmpAdminString
_CucsIppoolIpV6BlockRn_Object=MibTableColumn
cucsIppoolIpV6BlockRn=_CucsIppoolIpV6BlockRn_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,3),_CucsIppoolIpV6BlockRn_Type())
cucsIppoolIpV6BlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockRn.setStatus(_A)
_CucsIppoolIpV6BlockDefGw_Type=InetAddressIPv6
_CucsIppoolIpV6BlockDefGw_Object=MibTableColumn
cucsIppoolIpV6BlockDefGw=_CucsIppoolIpV6BlockDefGw_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,4),_CucsIppoolIpV6BlockDefGw_Type())
cucsIppoolIpV6BlockDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockDefGw.setStatus(_A)
_CucsIppoolIpV6BlockFrom_Type=InetAddressIPv6
_CucsIppoolIpV6BlockFrom_Object=MibTableColumn
cucsIppoolIpV6BlockFrom=_CucsIppoolIpV6BlockFrom_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,5),_CucsIppoolIpV6BlockFrom_Type())
cucsIppoolIpV6BlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockFrom.setStatus(_A)
_CucsIppoolIpV6BlockPrefix_Type=Gauge32
_CucsIppoolIpV6BlockPrefix_Object=MibTableColumn
cucsIppoolIpV6BlockPrefix=_CucsIppoolIpV6BlockPrefix_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,6),_CucsIppoolIpV6BlockPrefix_Type())
cucsIppoolIpV6BlockPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockPrefix.setStatus(_A)
_CucsIppoolIpV6BlockPrimDns_Type=InetAddressIPv6
_CucsIppoolIpV6BlockPrimDns_Object=MibTableColumn
cucsIppoolIpV6BlockPrimDns=_CucsIppoolIpV6BlockPrimDns_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,7),_CucsIppoolIpV6BlockPrimDns_Type())
cucsIppoolIpV6BlockPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockPrimDns.setStatus(_A)
_CucsIppoolIpV6BlockSecDns_Type=InetAddressIPv6
_CucsIppoolIpV6BlockSecDns_Object=MibTableColumn
cucsIppoolIpV6BlockSecDns=_CucsIppoolIpV6BlockSecDns_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,8),_CucsIppoolIpV6BlockSecDns_Type())
cucsIppoolIpV6BlockSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockSecDns.setStatus(_A)
_CucsIppoolIpV6BlockTo_Type=InetAddressIPv6
_CucsIppoolIpV6BlockTo_Object=MibTableColumn
cucsIppoolIpV6BlockTo=_CucsIppoolIpV6BlockTo_Object((1,3,6,1,4,1,9,9,719,1,24,8,1,9),_CucsIppoolIpV6BlockTo_Type())
cucsIppoolIpV6BlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6BlockTo.setStatus(_A)
_CucsIppoolIpV6PooledTable_Object=MibTable
cucsIppoolIpV6PooledTable=_CucsIppoolIpV6PooledTable_Object((1,3,6,1,4,1,9,9,719,1,24,9))
if mibBuilder.loadTexts:cucsIppoolIpV6PooledTable.setStatus(_A)
_CucsIppoolIpV6PooledEntry_Object=MibTableRow
cucsIppoolIpV6PooledEntry=_CucsIppoolIpV6PooledEntry_Object((1,3,6,1,4,1,9,9,719,1,24,9,1))
cucsIppoolIpV6PooledEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsIppoolIpV6PooledEntry.setStatus(_A)
_CucsIppoolIpV6PooledInstanceId_Type=CucsManagedObjectId
_CucsIppoolIpV6PooledInstanceId_Object=MibTableColumn
cucsIppoolIpV6PooledInstanceId=_CucsIppoolIpV6PooledInstanceId_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,1),_CucsIppoolIpV6PooledInstanceId_Type())
cucsIppoolIpV6PooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledInstanceId.setStatus(_A)
_CucsIppoolIpV6PooledDn_Type=CucsManagedObjectDn
_CucsIppoolIpV6PooledDn_Object=MibTableColumn
cucsIppoolIpV6PooledDn=_CucsIppoolIpV6PooledDn_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,2),_CucsIppoolIpV6PooledDn_Type())
cucsIppoolIpV6PooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledDn.setStatus(_A)
_CucsIppoolIpV6PooledRn_Type=SnmpAdminString
_CucsIppoolIpV6PooledRn_Object=MibTableColumn
cucsIppoolIpV6PooledRn=_CucsIppoolIpV6PooledRn_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,3),_CucsIppoolIpV6PooledRn_Type())
cucsIppoolIpV6PooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledRn.setStatus(_A)
_CucsIppoolIpV6PooledAssigned_Type=TruthValue
_CucsIppoolIpV6PooledAssigned_Object=MibTableColumn
cucsIppoolIpV6PooledAssigned=_CucsIppoolIpV6PooledAssigned_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,4),_CucsIppoolIpV6PooledAssigned_Type())
cucsIppoolIpV6PooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledAssigned.setStatus(_A)
_CucsIppoolIpV6PooledAssignedToDn_Type=SnmpAdminString
_CucsIppoolIpV6PooledAssignedToDn_Object=MibTableColumn
cucsIppoolIpV6PooledAssignedToDn=_CucsIppoolIpV6PooledAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,5),_CucsIppoolIpV6PooledAssignedToDn_Type())
cucsIppoolIpV6PooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledAssignedToDn.setStatus(_A)
_CucsIppoolIpV6PooledDefGw_Type=InetAddressIPv6
_CucsIppoolIpV6PooledDefGw_Object=MibTableColumn
cucsIppoolIpV6PooledDefGw=_CucsIppoolIpV6PooledDefGw_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,6),_CucsIppoolIpV6PooledDefGw_Type())
cucsIppoolIpV6PooledDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledDefGw.setStatus(_A)
_CucsIppoolIpV6PooledId_Type=InetAddressIPv6
_CucsIppoolIpV6PooledId_Object=MibTableColumn
cucsIppoolIpV6PooledId=_CucsIppoolIpV6PooledId_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,7),_CucsIppoolIpV6PooledId_Type())
cucsIppoolIpV6PooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledId.setStatus(_A)
_CucsIppoolIpV6PooledPoolableDn_Type=SnmpAdminString
_CucsIppoolIpV6PooledPoolableDn_Object=MibTableColumn
cucsIppoolIpV6PooledPoolableDn=_CucsIppoolIpV6PooledPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,8),_CucsIppoolIpV6PooledPoolableDn_Type())
cucsIppoolIpV6PooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledPoolableDn.setStatus(_A)
_CucsIppoolIpV6PooledPrefix_Type=Gauge32
_CucsIppoolIpV6PooledPrefix_Object=MibTableColumn
cucsIppoolIpV6PooledPrefix=_CucsIppoolIpV6PooledPrefix_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,9),_CucsIppoolIpV6PooledPrefix_Type())
cucsIppoolIpV6PooledPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledPrefix.setStatus(_A)
_CucsIppoolIpV6PooledPrevAssignedToDn_Type=SnmpAdminString
_CucsIppoolIpV6PooledPrevAssignedToDn_Object=MibTableColumn
cucsIppoolIpV6PooledPrevAssignedToDn=_CucsIppoolIpV6PooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,10),_CucsIppoolIpV6PooledPrevAssignedToDn_Type())
cucsIppoolIpV6PooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledPrevAssignedToDn.setStatus(_A)
_CucsIppoolIpV6PooledPrimDns_Type=InetAddressIPv6
_CucsIppoolIpV6PooledPrimDns_Object=MibTableColumn
cucsIppoolIpV6PooledPrimDns=_CucsIppoolIpV6PooledPrimDns_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,11),_CucsIppoolIpV6PooledPrimDns_Type())
cucsIppoolIpV6PooledPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledPrimDns.setStatus(_A)
_CucsIppoolIpV6PooledSecDns_Type=InetAddressIPv6
_CucsIppoolIpV6PooledSecDns_Object=MibTableColumn
cucsIppoolIpV6PooledSecDns=_CucsIppoolIpV6PooledSecDns_Object((1,3,6,1,4,1,9,9,719,1,24,9,1,12),_CucsIppoolIpV6PooledSecDns_Type())
cucsIppoolIpV6PooledSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIppoolIpV6PooledSecDns.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsIppoolObjects':cucsIppoolObjects,'cucsIppoolAddrTable':cucsIppoolAddrTable,'cucsIppoolAddrEntry':cucsIppoolAddrEntry,_E:cucsIppoolAddrInstanceId,'cucsIppoolAddrDn':cucsIppoolAddrDn,'cucsIppoolAddrRn':cucsIppoolAddrRn,'cucsIppoolAddrAssigned':cucsIppoolAddrAssigned,'cucsIppoolAddrAssignedToDn':cucsIppoolAddrAssignedToDn,'cucsIppoolAddrId':cucsIppoolAddrId,'cucsIppoolAddrOwner':cucsIppoolAddrOwner,'cucsIppoolAddrGlobalAssignedCnt':cucsIppoolAddrGlobalAssignedCnt,'cucsIppoolAddrGlobalDefinedCnt':cucsIppoolAddrGlobalDefinedCnt,'cucsIppoolBlockTable':cucsIppoolBlockTable,'cucsIppoolBlockEntry':cucsIppoolBlockEntry,_F:cucsIppoolBlockInstanceId,'cucsIppoolBlockDn':cucsIppoolBlockDn,'cucsIppoolBlockRn':cucsIppoolBlockRn,'cucsIppoolBlockDefGw':cucsIppoolBlockDefGw,'cucsIppoolBlockFrom':cucsIppoolBlockFrom,'cucsIppoolBlockSubnet':cucsIppoolBlockSubnet,'cucsIppoolBlockTo':cucsIppoolBlockTo,'cucsIppoolBlockPrimDns':cucsIppoolBlockPrimDns,'cucsIppoolBlockSecDns':cucsIppoolBlockSecDns,'cucsIppoolPoolTable':cucsIppoolPoolTable,'cucsIppoolPoolEntry':cucsIppoolPoolEntry,_G:cucsIppoolPoolInstanceId,'cucsIppoolPoolDn':cucsIppoolPoolDn,'cucsIppoolPoolRn':cucsIppoolPoolRn,'cucsIppoolPoolAssigned':cucsIppoolPoolAssigned,'cucsIppoolPoolDescr':cucsIppoolPoolDescr,'cucsIppoolPoolIntId':cucsIppoolPoolIntId,'cucsIppoolPoolName':cucsIppoolPoolName,'cucsIppoolPoolSize':cucsIppoolPoolSize,'cucsIppoolPoolAssignmentOrder':cucsIppoolPoolAssignmentOrder,'cucsIppoolPoolPolicyLevel':cucsIppoolPoolPolicyLevel,'cucsIppoolPoolPolicyOwner':cucsIppoolPoolPolicyOwner,'cucsIppoolPoolExtManaged':cucsIppoolPoolExtManaged,'cucsIppoolPoolGuid':cucsIppoolPoolGuid,'cucsIppoolPoolIsNetBIOSEnabled':cucsIppoolPoolIsNetBIOSEnabled,'cucsIppoolPoolSupportsDHCP':cucsIppoolPoolSupportsDHCP,'cucsIppoolPoolV4Assigned':cucsIppoolPoolV4Assigned,'cucsIppoolPoolV4Size':cucsIppoolPoolV4Size,'cucsIppoolPoolV6Assigned':cucsIppoolPoolV6Assigned,'cucsIppoolPoolV6Size':cucsIppoolPoolV6Size,'cucsIppoolPoolPropAcl':cucsIppoolPoolPropAcl,'cucsIppoolPoolableTable':cucsIppoolPoolableTable,'cucsIppoolPoolableEntry':cucsIppoolPoolableEntry,_H:cucsIppoolPoolableInstanceId,'cucsIppoolPoolableDn':cucsIppoolPoolableDn,'cucsIppoolPoolableRn':cucsIppoolPoolableRn,'cucsIppoolPoolableId':cucsIppoolPoolableId,'cucsIppoolPoolablePoolDn':cucsIppoolPoolablePoolDn,'cucsIppoolPooledTable':cucsIppoolPooledTable,'cucsIppoolPooledEntry':cucsIppoolPooledEntry,_I:cucsIppoolPooledInstanceId,'cucsIppoolPooledDn':cucsIppoolPooledDn,'cucsIppoolPooledRn':cucsIppoolPooledRn,'cucsIppoolPooledAssigned':cucsIppoolPooledAssigned,'cucsIppoolPooledAssignedToDn':cucsIppoolPooledAssignedToDn,'cucsIppoolPooledDefGw':cucsIppoolPooledDefGw,'cucsIppoolPooledId':cucsIppoolPooledId,'cucsIppoolPooledPoolableDn':cucsIppoolPooledPoolableDn,'cucsIppoolPooledPrevAssignedToDn':cucsIppoolPooledPrevAssignedToDn,'cucsIppoolPooledSubnet':cucsIppoolPooledSubnet,'cucsIppoolPooledPrimDns':cucsIppoolPooledPrimDns,'cucsIppoolPooledSecDns':cucsIppoolPooledSecDns,'cucsIppoolUniverseTable':cucsIppoolUniverseTable,'cucsIppoolUniverseEntry':cucsIppoolUniverseEntry,_J:cucsIppoolUniverseInstanceId,'cucsIppoolUniverseDn':cucsIppoolUniverseDn,'cucsIppoolUniverseRn':cucsIppoolUniverseRn,'cucsIppoolIpV6AddrTable':cucsIppoolIpV6AddrTable,'cucsIppoolIpV6AddrEntry':cucsIppoolIpV6AddrEntry,_K:cucsIppoolIpV6AddrInstanceId,'cucsIppoolIpV6AddrDn':cucsIppoolIpV6AddrDn,'cucsIppoolIpV6AddrRn':cucsIppoolIpV6AddrRn,'cucsIppoolIpV6AddrAssigned':cucsIppoolIpV6AddrAssigned,'cucsIppoolIpV6AddrAssignedToDn':cucsIppoolIpV6AddrAssignedToDn,'cucsIppoolIpV6AddrId':cucsIppoolIpV6AddrId,'cucsIppoolIpV6AddrOwner':cucsIppoolIpV6AddrOwner,'cucsIppoolIpV6AddrGlobalAssignedCnt':cucsIppoolIpV6AddrGlobalAssignedCnt,'cucsIppoolIpV6AddrGlobalDefinedCnt':cucsIppoolIpV6AddrGlobalDefinedCnt,'cucsIppoolIpV6BlockTable':cucsIppoolIpV6BlockTable,'cucsIppoolIpV6BlockEntry':cucsIppoolIpV6BlockEntry,_L:cucsIppoolIpV6BlockInstanceId,'cucsIppoolIpV6BlockDn':cucsIppoolIpV6BlockDn,'cucsIppoolIpV6BlockRn':cucsIppoolIpV6BlockRn,'cucsIppoolIpV6BlockDefGw':cucsIppoolIpV6BlockDefGw,'cucsIppoolIpV6BlockFrom':cucsIppoolIpV6BlockFrom,'cucsIppoolIpV6BlockPrefix':cucsIppoolIpV6BlockPrefix,'cucsIppoolIpV6BlockPrimDns':cucsIppoolIpV6BlockPrimDns,'cucsIppoolIpV6BlockSecDns':cucsIppoolIpV6BlockSecDns,'cucsIppoolIpV6BlockTo':cucsIppoolIpV6BlockTo,'cucsIppoolIpV6PooledTable':cucsIppoolIpV6PooledTable,'cucsIppoolIpV6PooledEntry':cucsIppoolIpV6PooledEntry,_M:cucsIppoolIpV6PooledInstanceId,'cucsIppoolIpV6PooledDn':cucsIppoolIpV6PooledDn,'cucsIppoolIpV6PooledRn':cucsIppoolIpV6PooledRn,'cucsIppoolIpV6PooledAssigned':cucsIppoolIpV6PooledAssigned,'cucsIppoolIpV6PooledAssignedToDn':cucsIppoolIpV6PooledAssignedToDn,'cucsIppoolIpV6PooledDefGw':cucsIppoolIpV6PooledDefGw,'cucsIppoolIpV6PooledId':cucsIppoolIpV6PooledId,'cucsIppoolIpV6PooledPoolableDn':cucsIppoolIpV6PooledPoolableDn,'cucsIppoolIpV6PooledPrefix':cucsIppoolIpV6PooledPrefix,'cucsIppoolIpV6PooledPrevAssignedToDn':cucsIppoolIpV6PooledPrevAssignedToDn,'cucsIppoolIpV6PooledPrimDns':cucsIppoolIpV6PooledPrimDns,'cucsIppoolIpV6PooledSecDns':cucsIppoolIpV6PooledSecDns})