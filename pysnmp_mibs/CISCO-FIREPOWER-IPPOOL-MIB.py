_M='cfprIppoolUniverseInstanceId'
_L='cfprIppoolPooledInstanceId'
_K='cfprIppoolPoolableInstanceId'
_J='cfprIppoolPoolInstanceId'
_I='cfprIppoolIpV6PooledInstanceId'
_H='cfprIppoolIpV6BlockInstanceId'
_G='cfprIppoolIpV6AddrInstanceId'
_F='cfprIppoolBlockInstanceId'
_E='cfprIppoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-IPPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprIppoolDHCPMode,CfprIppoolManagementMode,CfprIppoolNetBIOSMode,CfprIppoolPoolAssignmentOrder,CfprPolicyPolicyOwner,CfprPoolElementOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprIppoolDHCPMode','CfprIppoolManagementMode','CfprIppoolNetBIOSMode','CfprIppoolPoolAssignmentOrder','CfprPolicyPolicyOwner','CfprPoolElementOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprIppoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,41))
_CfprIppoolAddrTable_Object=MibTable
cfprIppoolAddrTable=_CfprIppoolAddrTable_Object((1,3,6,1,4,1,9,9,826,1,41,1))
if mibBuilder.loadTexts:cfprIppoolAddrTable.setStatus(_A)
_CfprIppoolAddrEntry_Object=MibTableRow
cfprIppoolAddrEntry=_CfprIppoolAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,41,1,1))
cfprIppoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprIppoolAddrEntry.setStatus(_A)
_CfprIppoolAddrInstanceId_Type=CfprManagedObjectId
_CfprIppoolAddrInstanceId_Object=MibTableColumn
cfprIppoolAddrInstanceId=_CfprIppoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,1),_CfprIppoolAddrInstanceId_Type())
cfprIppoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolAddrInstanceId.setStatus(_A)
_CfprIppoolAddrDn_Type=CfprManagedObjectDn
_CfprIppoolAddrDn_Object=MibTableColumn
cfprIppoolAddrDn=_CfprIppoolAddrDn_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,2),_CfprIppoolAddrDn_Type())
cfprIppoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrDn.setStatus(_A)
_CfprIppoolAddrRn_Type=SnmpAdminString
_CfprIppoolAddrRn_Object=MibTableColumn
cfprIppoolAddrRn=_CfprIppoolAddrRn_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,3),_CfprIppoolAddrRn_Type())
cfprIppoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrRn.setStatus(_A)
_CfprIppoolAddrAssigned_Type=TruthValue
_CfprIppoolAddrAssigned_Object=MibTableColumn
cfprIppoolAddrAssigned=_CfprIppoolAddrAssigned_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,4),_CfprIppoolAddrAssigned_Type())
cfprIppoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrAssigned.setStatus(_A)
_CfprIppoolAddrAssignedToDn_Type=SnmpAdminString
_CfprIppoolAddrAssignedToDn_Object=MibTableColumn
cfprIppoolAddrAssignedToDn=_CfprIppoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,5),_CfprIppoolAddrAssignedToDn_Type())
cfprIppoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrAssignedToDn.setStatus(_A)
_CfprIppoolAddrGlobalAssignedCnt_Type=Gauge32
_CfprIppoolAddrGlobalAssignedCnt_Object=MibTableColumn
cfprIppoolAddrGlobalAssignedCnt=_CfprIppoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,6),_CfprIppoolAddrGlobalAssignedCnt_Type())
cfprIppoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrGlobalAssignedCnt.setStatus(_A)
_CfprIppoolAddrGlobalDefinedCnt_Type=Gauge32
_CfprIppoolAddrGlobalDefinedCnt_Object=MibTableColumn
cfprIppoolAddrGlobalDefinedCnt=_CfprIppoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,7),_CfprIppoolAddrGlobalDefinedCnt_Type())
cfprIppoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrGlobalDefinedCnt.setStatus(_A)
_CfprIppoolAddrId_Type=InetAddressIPv4
_CfprIppoolAddrId_Object=MibTableColumn
cfprIppoolAddrId=_CfprIppoolAddrId_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,8),_CfprIppoolAddrId_Type())
cfprIppoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrId.setStatus(_A)
_CfprIppoolAddrOwner_Type=CfprPoolElementOwner
_CfprIppoolAddrOwner_Object=MibTableColumn
cfprIppoolAddrOwner=_CfprIppoolAddrOwner_Object((1,3,6,1,4,1,9,9,826,1,41,1,1,9),_CfprIppoolAddrOwner_Type())
cfprIppoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolAddrOwner.setStatus(_A)
_CfprIppoolBlockTable_Object=MibTable
cfprIppoolBlockTable=_CfprIppoolBlockTable_Object((1,3,6,1,4,1,9,9,826,1,41,2))
if mibBuilder.loadTexts:cfprIppoolBlockTable.setStatus(_A)
_CfprIppoolBlockEntry_Object=MibTableRow
cfprIppoolBlockEntry=_CfprIppoolBlockEntry_Object((1,3,6,1,4,1,9,9,826,1,41,2,1))
cfprIppoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprIppoolBlockEntry.setStatus(_A)
_CfprIppoolBlockInstanceId_Type=CfprManagedObjectId
_CfprIppoolBlockInstanceId_Object=MibTableColumn
cfprIppoolBlockInstanceId=_CfprIppoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,1),_CfprIppoolBlockInstanceId_Type())
cfprIppoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolBlockInstanceId.setStatus(_A)
_CfprIppoolBlockDn_Type=CfprManagedObjectDn
_CfprIppoolBlockDn_Object=MibTableColumn
cfprIppoolBlockDn=_CfprIppoolBlockDn_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,2),_CfprIppoolBlockDn_Type())
cfprIppoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockDn.setStatus(_A)
_CfprIppoolBlockRn_Type=SnmpAdminString
_CfprIppoolBlockRn_Object=MibTableColumn
cfprIppoolBlockRn=_CfprIppoolBlockRn_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,3),_CfprIppoolBlockRn_Type())
cfprIppoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockRn.setStatus(_A)
_CfprIppoolBlockDefGw_Type=InetAddressIPv4
_CfprIppoolBlockDefGw_Object=MibTableColumn
cfprIppoolBlockDefGw=_CfprIppoolBlockDefGw_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,4),_CfprIppoolBlockDefGw_Type())
cfprIppoolBlockDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockDefGw.setStatus(_A)
_CfprIppoolBlockFrom_Type=InetAddressIPv4
_CfprIppoolBlockFrom_Object=MibTableColumn
cfprIppoolBlockFrom=_CfprIppoolBlockFrom_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,5),_CfprIppoolBlockFrom_Type())
cfprIppoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockFrom.setStatus(_A)
_CfprIppoolBlockPrimDns_Type=InetAddressIPv4
_CfprIppoolBlockPrimDns_Object=MibTableColumn
cfprIppoolBlockPrimDns=_CfprIppoolBlockPrimDns_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,6),_CfprIppoolBlockPrimDns_Type())
cfprIppoolBlockPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockPrimDns.setStatus(_A)
_CfprIppoolBlockSecDns_Type=InetAddressIPv4
_CfprIppoolBlockSecDns_Object=MibTableColumn
cfprIppoolBlockSecDns=_CfprIppoolBlockSecDns_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,7),_CfprIppoolBlockSecDns_Type())
cfprIppoolBlockSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockSecDns.setStatus(_A)
_CfprIppoolBlockSubnet_Type=InetAddressIPv4
_CfprIppoolBlockSubnet_Object=MibTableColumn
cfprIppoolBlockSubnet=_CfprIppoolBlockSubnet_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,8),_CfprIppoolBlockSubnet_Type())
cfprIppoolBlockSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockSubnet.setStatus(_A)
_CfprIppoolBlockTo_Type=InetAddressIPv4
_CfprIppoolBlockTo_Object=MibTableColumn
cfprIppoolBlockTo=_CfprIppoolBlockTo_Object((1,3,6,1,4,1,9,9,826,1,41,2,1,9),_CfprIppoolBlockTo_Type())
cfprIppoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolBlockTo.setStatus(_A)
_CfprIppoolIpV6AddrTable_Object=MibTable
cfprIppoolIpV6AddrTable=_CfprIppoolIpV6AddrTable_Object((1,3,6,1,4,1,9,9,826,1,41,3))
if mibBuilder.loadTexts:cfprIppoolIpV6AddrTable.setStatus(_A)
_CfprIppoolIpV6AddrEntry_Object=MibTableRow
cfprIppoolIpV6AddrEntry=_CfprIppoolIpV6AddrEntry_Object((1,3,6,1,4,1,9,9,826,1,41,3,1))
cfprIppoolIpV6AddrEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprIppoolIpV6AddrEntry.setStatus(_A)
_CfprIppoolIpV6AddrInstanceId_Type=CfprManagedObjectId
_CfprIppoolIpV6AddrInstanceId_Object=MibTableColumn
cfprIppoolIpV6AddrInstanceId=_CfprIppoolIpV6AddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,1),_CfprIppoolIpV6AddrInstanceId_Type())
cfprIppoolIpV6AddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrInstanceId.setStatus(_A)
_CfprIppoolIpV6AddrDn_Type=CfprManagedObjectDn
_CfprIppoolIpV6AddrDn_Object=MibTableColumn
cfprIppoolIpV6AddrDn=_CfprIppoolIpV6AddrDn_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,2),_CfprIppoolIpV6AddrDn_Type())
cfprIppoolIpV6AddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrDn.setStatus(_A)
_CfprIppoolIpV6AddrRn_Type=SnmpAdminString
_CfprIppoolIpV6AddrRn_Object=MibTableColumn
cfprIppoolIpV6AddrRn=_CfprIppoolIpV6AddrRn_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,3),_CfprIppoolIpV6AddrRn_Type())
cfprIppoolIpV6AddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrRn.setStatus(_A)
_CfprIppoolIpV6AddrAssigned_Type=TruthValue
_CfprIppoolIpV6AddrAssigned_Object=MibTableColumn
cfprIppoolIpV6AddrAssigned=_CfprIppoolIpV6AddrAssigned_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,4),_CfprIppoolIpV6AddrAssigned_Type())
cfprIppoolIpV6AddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrAssigned.setStatus(_A)
_CfprIppoolIpV6AddrAssignedToDn_Type=SnmpAdminString
_CfprIppoolIpV6AddrAssignedToDn_Object=MibTableColumn
cfprIppoolIpV6AddrAssignedToDn=_CfprIppoolIpV6AddrAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,5),_CfprIppoolIpV6AddrAssignedToDn_Type())
cfprIppoolIpV6AddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrAssignedToDn.setStatus(_A)
_CfprIppoolIpV6AddrGlobalAssignedCnt_Type=Gauge32
_CfprIppoolIpV6AddrGlobalAssignedCnt_Object=MibTableColumn
cfprIppoolIpV6AddrGlobalAssignedCnt=_CfprIppoolIpV6AddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,6),_CfprIppoolIpV6AddrGlobalAssignedCnt_Type())
cfprIppoolIpV6AddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrGlobalAssignedCnt.setStatus(_A)
_CfprIppoolIpV6AddrGlobalDefinedCnt_Type=Gauge32
_CfprIppoolIpV6AddrGlobalDefinedCnt_Object=MibTableColumn
cfprIppoolIpV6AddrGlobalDefinedCnt=_CfprIppoolIpV6AddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,7),_CfprIppoolIpV6AddrGlobalDefinedCnt_Type())
cfprIppoolIpV6AddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrGlobalDefinedCnt.setStatus(_A)
_CfprIppoolIpV6AddrId_Type=InetAddressIPv6
_CfprIppoolIpV6AddrId_Object=MibTableColumn
cfprIppoolIpV6AddrId=_CfprIppoolIpV6AddrId_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,8),_CfprIppoolIpV6AddrId_Type())
cfprIppoolIpV6AddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrId.setStatus(_A)
_CfprIppoolIpV6AddrOwner_Type=CfprPoolElementOwner
_CfprIppoolIpV6AddrOwner_Object=MibTableColumn
cfprIppoolIpV6AddrOwner=_CfprIppoolIpV6AddrOwner_Object((1,3,6,1,4,1,9,9,826,1,41,3,1,9),_CfprIppoolIpV6AddrOwner_Type())
cfprIppoolIpV6AddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6AddrOwner.setStatus(_A)
_CfprIppoolIpV6BlockTable_Object=MibTable
cfprIppoolIpV6BlockTable=_CfprIppoolIpV6BlockTable_Object((1,3,6,1,4,1,9,9,826,1,41,4))
if mibBuilder.loadTexts:cfprIppoolIpV6BlockTable.setStatus(_A)
_CfprIppoolIpV6BlockEntry_Object=MibTableRow
cfprIppoolIpV6BlockEntry=_CfprIppoolIpV6BlockEntry_Object((1,3,6,1,4,1,9,9,826,1,41,4,1))
cfprIppoolIpV6BlockEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprIppoolIpV6BlockEntry.setStatus(_A)
_CfprIppoolIpV6BlockInstanceId_Type=CfprManagedObjectId
_CfprIppoolIpV6BlockInstanceId_Object=MibTableColumn
cfprIppoolIpV6BlockInstanceId=_CfprIppoolIpV6BlockInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,1),_CfprIppoolIpV6BlockInstanceId_Type())
cfprIppoolIpV6BlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockInstanceId.setStatus(_A)
_CfprIppoolIpV6BlockDn_Type=CfprManagedObjectDn
_CfprIppoolIpV6BlockDn_Object=MibTableColumn
cfprIppoolIpV6BlockDn=_CfprIppoolIpV6BlockDn_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,2),_CfprIppoolIpV6BlockDn_Type())
cfprIppoolIpV6BlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockDn.setStatus(_A)
_CfprIppoolIpV6BlockRn_Type=SnmpAdminString
_CfprIppoolIpV6BlockRn_Object=MibTableColumn
cfprIppoolIpV6BlockRn=_CfprIppoolIpV6BlockRn_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,3),_CfprIppoolIpV6BlockRn_Type())
cfprIppoolIpV6BlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockRn.setStatus(_A)
_CfprIppoolIpV6BlockDefGw_Type=InetAddressIPv6
_CfprIppoolIpV6BlockDefGw_Object=MibTableColumn
cfprIppoolIpV6BlockDefGw=_CfprIppoolIpV6BlockDefGw_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,4),_CfprIppoolIpV6BlockDefGw_Type())
cfprIppoolIpV6BlockDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockDefGw.setStatus(_A)
_CfprIppoolIpV6BlockFrom_Type=InetAddressIPv6
_CfprIppoolIpV6BlockFrom_Object=MibTableColumn
cfprIppoolIpV6BlockFrom=_CfprIppoolIpV6BlockFrom_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,5),_CfprIppoolIpV6BlockFrom_Type())
cfprIppoolIpV6BlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockFrom.setStatus(_A)
_CfprIppoolIpV6BlockPrefix_Type=Gauge32
_CfprIppoolIpV6BlockPrefix_Object=MibTableColumn
cfprIppoolIpV6BlockPrefix=_CfprIppoolIpV6BlockPrefix_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,6),_CfprIppoolIpV6BlockPrefix_Type())
cfprIppoolIpV6BlockPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockPrefix.setStatus(_A)
_CfprIppoolIpV6BlockPrimDns_Type=InetAddressIPv6
_CfprIppoolIpV6BlockPrimDns_Object=MibTableColumn
cfprIppoolIpV6BlockPrimDns=_CfprIppoolIpV6BlockPrimDns_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,7),_CfprIppoolIpV6BlockPrimDns_Type())
cfprIppoolIpV6BlockPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockPrimDns.setStatus(_A)
_CfprIppoolIpV6BlockSecDns_Type=InetAddressIPv6
_CfprIppoolIpV6BlockSecDns_Object=MibTableColumn
cfprIppoolIpV6BlockSecDns=_CfprIppoolIpV6BlockSecDns_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,8),_CfprIppoolIpV6BlockSecDns_Type())
cfprIppoolIpV6BlockSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockSecDns.setStatus(_A)
_CfprIppoolIpV6BlockTo_Type=InetAddressIPv6
_CfprIppoolIpV6BlockTo_Object=MibTableColumn
cfprIppoolIpV6BlockTo=_CfprIppoolIpV6BlockTo_Object((1,3,6,1,4,1,9,9,826,1,41,4,1,9),_CfprIppoolIpV6BlockTo_Type())
cfprIppoolIpV6BlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6BlockTo.setStatus(_A)
_CfprIppoolIpV6PooledTable_Object=MibTable
cfprIppoolIpV6PooledTable=_CfprIppoolIpV6PooledTable_Object((1,3,6,1,4,1,9,9,826,1,41,5))
if mibBuilder.loadTexts:cfprIppoolIpV6PooledTable.setStatus(_A)
_CfprIppoolIpV6PooledEntry_Object=MibTableRow
cfprIppoolIpV6PooledEntry=_CfprIppoolIpV6PooledEntry_Object((1,3,6,1,4,1,9,9,826,1,41,5,1))
cfprIppoolIpV6PooledEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprIppoolIpV6PooledEntry.setStatus(_A)
_CfprIppoolIpV6PooledInstanceId_Type=CfprManagedObjectId
_CfprIppoolIpV6PooledInstanceId_Object=MibTableColumn
cfprIppoolIpV6PooledInstanceId=_CfprIppoolIpV6PooledInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,1),_CfprIppoolIpV6PooledInstanceId_Type())
cfprIppoolIpV6PooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledInstanceId.setStatus(_A)
_CfprIppoolIpV6PooledDn_Type=CfprManagedObjectDn
_CfprIppoolIpV6PooledDn_Object=MibTableColumn
cfprIppoolIpV6PooledDn=_CfprIppoolIpV6PooledDn_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,2),_CfprIppoolIpV6PooledDn_Type())
cfprIppoolIpV6PooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledDn.setStatus(_A)
_CfprIppoolIpV6PooledRn_Type=SnmpAdminString
_CfprIppoolIpV6PooledRn_Object=MibTableColumn
cfprIppoolIpV6PooledRn=_CfprIppoolIpV6PooledRn_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,3),_CfprIppoolIpV6PooledRn_Type())
cfprIppoolIpV6PooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledRn.setStatus(_A)
_CfprIppoolIpV6PooledAssigned_Type=TruthValue
_CfprIppoolIpV6PooledAssigned_Object=MibTableColumn
cfprIppoolIpV6PooledAssigned=_CfprIppoolIpV6PooledAssigned_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,4),_CfprIppoolIpV6PooledAssigned_Type())
cfprIppoolIpV6PooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledAssigned.setStatus(_A)
_CfprIppoolIpV6PooledAssignedToDn_Type=SnmpAdminString
_CfprIppoolIpV6PooledAssignedToDn_Object=MibTableColumn
cfprIppoolIpV6PooledAssignedToDn=_CfprIppoolIpV6PooledAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,5),_CfprIppoolIpV6PooledAssignedToDn_Type())
cfprIppoolIpV6PooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledAssignedToDn.setStatus(_A)
_CfprIppoolIpV6PooledDefGw_Type=InetAddressIPv6
_CfprIppoolIpV6PooledDefGw_Object=MibTableColumn
cfprIppoolIpV6PooledDefGw=_CfprIppoolIpV6PooledDefGw_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,6),_CfprIppoolIpV6PooledDefGw_Type())
cfprIppoolIpV6PooledDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledDefGw.setStatus(_A)
_CfprIppoolIpV6PooledId_Type=InetAddressIPv6
_CfprIppoolIpV6PooledId_Object=MibTableColumn
cfprIppoolIpV6PooledId=_CfprIppoolIpV6PooledId_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,7),_CfprIppoolIpV6PooledId_Type())
cfprIppoolIpV6PooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledId.setStatus(_A)
_CfprIppoolIpV6PooledPoolableDn_Type=SnmpAdminString
_CfprIppoolIpV6PooledPoolableDn_Object=MibTableColumn
cfprIppoolIpV6PooledPoolableDn=_CfprIppoolIpV6PooledPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,8),_CfprIppoolIpV6PooledPoolableDn_Type())
cfprIppoolIpV6PooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledPoolableDn.setStatus(_A)
_CfprIppoolIpV6PooledPrefix_Type=Gauge32
_CfprIppoolIpV6PooledPrefix_Object=MibTableColumn
cfprIppoolIpV6PooledPrefix=_CfprIppoolIpV6PooledPrefix_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,9),_CfprIppoolIpV6PooledPrefix_Type())
cfprIppoolIpV6PooledPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledPrefix.setStatus(_A)
_CfprIppoolIpV6PooledPrevAssignedToDn_Type=SnmpAdminString
_CfprIppoolIpV6PooledPrevAssignedToDn_Object=MibTableColumn
cfprIppoolIpV6PooledPrevAssignedToDn=_CfprIppoolIpV6PooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,10),_CfprIppoolIpV6PooledPrevAssignedToDn_Type())
cfprIppoolIpV6PooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledPrevAssignedToDn.setStatus(_A)
_CfprIppoolIpV6PooledPrimDns_Type=InetAddressIPv6
_CfprIppoolIpV6PooledPrimDns_Object=MibTableColumn
cfprIppoolIpV6PooledPrimDns=_CfprIppoolIpV6PooledPrimDns_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,11),_CfprIppoolIpV6PooledPrimDns_Type())
cfprIppoolIpV6PooledPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledPrimDns.setStatus(_A)
_CfprIppoolIpV6PooledSecDns_Type=InetAddressIPv6
_CfprIppoolIpV6PooledSecDns_Object=MibTableColumn
cfprIppoolIpV6PooledSecDns=_CfprIppoolIpV6PooledSecDns_Object((1,3,6,1,4,1,9,9,826,1,41,5,1,12),_CfprIppoolIpV6PooledSecDns_Type())
cfprIppoolIpV6PooledSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolIpV6PooledSecDns.setStatus(_A)
_CfprIppoolPoolTable_Object=MibTable
cfprIppoolPoolTable=_CfprIppoolPoolTable_Object((1,3,6,1,4,1,9,9,826,1,41,6))
if mibBuilder.loadTexts:cfprIppoolPoolTable.setStatus(_A)
_CfprIppoolPoolEntry_Object=MibTableRow
cfprIppoolPoolEntry=_CfprIppoolPoolEntry_Object((1,3,6,1,4,1,9,9,826,1,41,6,1))
cfprIppoolPoolEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprIppoolPoolEntry.setStatus(_A)
_CfprIppoolPoolInstanceId_Type=CfprManagedObjectId
_CfprIppoolPoolInstanceId_Object=MibTableColumn
cfprIppoolPoolInstanceId=_CfprIppoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,1),_CfprIppoolPoolInstanceId_Type())
cfprIppoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolPoolInstanceId.setStatus(_A)
_CfprIppoolPoolDn_Type=CfprManagedObjectDn
_CfprIppoolPoolDn_Object=MibTableColumn
cfprIppoolPoolDn=_CfprIppoolPoolDn_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,2),_CfprIppoolPoolDn_Type())
cfprIppoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolDn.setStatus(_A)
_CfprIppoolPoolRn_Type=SnmpAdminString
_CfprIppoolPoolRn_Object=MibTableColumn
cfprIppoolPoolRn=_CfprIppoolPoolRn_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,3),_CfprIppoolPoolRn_Type())
cfprIppoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolRn.setStatus(_A)
_CfprIppoolPoolAssigned_Type=Gauge32
_CfprIppoolPoolAssigned_Object=MibTableColumn
cfprIppoolPoolAssigned=_CfprIppoolPoolAssigned_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,4),_CfprIppoolPoolAssigned_Type())
cfprIppoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolAssigned.setStatus(_A)
_CfprIppoolPoolAssignmentOrder_Type=CfprIppoolPoolAssignmentOrder
_CfprIppoolPoolAssignmentOrder_Object=MibTableColumn
cfprIppoolPoolAssignmentOrder=_CfprIppoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,5),_CfprIppoolPoolAssignmentOrder_Type())
cfprIppoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolAssignmentOrder.setStatus(_A)
_CfprIppoolPoolDescr_Type=SnmpAdminString
_CfprIppoolPoolDescr_Object=MibTableColumn
cfprIppoolPoolDescr=_CfprIppoolPoolDescr_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,6),_CfprIppoolPoolDescr_Type())
cfprIppoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolDescr.setStatus(_A)
_CfprIppoolPoolExtManaged_Type=CfprIppoolManagementMode
_CfprIppoolPoolExtManaged_Object=MibTableColumn
cfprIppoolPoolExtManaged=_CfprIppoolPoolExtManaged_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,7),_CfprIppoolPoolExtManaged_Type())
cfprIppoolPoolExtManaged.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolExtManaged.setStatus(_A)
_CfprIppoolPoolGuid_Type=SnmpAdminString
_CfprIppoolPoolGuid_Object=MibTableColumn
cfprIppoolPoolGuid=_CfprIppoolPoolGuid_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,8),_CfprIppoolPoolGuid_Type())
cfprIppoolPoolGuid.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolGuid.setStatus(_A)
_CfprIppoolPoolIntId_Type=SnmpAdminString
_CfprIppoolPoolIntId_Object=MibTableColumn
cfprIppoolPoolIntId=_CfprIppoolPoolIntId_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,9),_CfprIppoolPoolIntId_Type())
cfprIppoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolIntId.setStatus(_A)
_CfprIppoolPoolIsNetBIOSEnabled_Type=CfprIppoolNetBIOSMode
_CfprIppoolPoolIsNetBIOSEnabled_Object=MibTableColumn
cfprIppoolPoolIsNetBIOSEnabled=_CfprIppoolPoolIsNetBIOSEnabled_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,10),_CfprIppoolPoolIsNetBIOSEnabled_Type())
cfprIppoolPoolIsNetBIOSEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolIsNetBIOSEnabled.setStatus(_A)
_CfprIppoolPoolName_Type=SnmpAdminString
_CfprIppoolPoolName_Object=MibTableColumn
cfprIppoolPoolName=_CfprIppoolPoolName_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,11),_CfprIppoolPoolName_Type())
cfprIppoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolName.setStatus(_A)
_CfprIppoolPoolPolicyLevel_Type=Gauge32
_CfprIppoolPoolPolicyLevel_Object=MibTableColumn
cfprIppoolPoolPolicyLevel=_CfprIppoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,12),_CfprIppoolPoolPolicyLevel_Type())
cfprIppoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolPolicyLevel.setStatus(_A)
_CfprIppoolPoolPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprIppoolPoolPolicyOwner_Object=MibTableColumn
cfprIppoolPoolPolicyOwner=_CfprIppoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,13),_CfprIppoolPoolPolicyOwner_Type())
cfprIppoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolPolicyOwner.setStatus(_A)
_CfprIppoolPoolSize_Type=Gauge32
_CfprIppoolPoolSize_Object=MibTableColumn
cfprIppoolPoolSize=_CfprIppoolPoolSize_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,14),_CfprIppoolPoolSize_Type())
cfprIppoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolSize.setStatus(_A)
_CfprIppoolPoolSupportsDHCP_Type=CfprIppoolDHCPMode
_CfprIppoolPoolSupportsDHCP_Object=MibTableColumn
cfprIppoolPoolSupportsDHCP=_CfprIppoolPoolSupportsDHCP_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,15),_CfprIppoolPoolSupportsDHCP_Type())
cfprIppoolPoolSupportsDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolSupportsDHCP.setStatus(_A)
_CfprIppoolPoolV4Assigned_Type=Gauge32
_CfprIppoolPoolV4Assigned_Object=MibTableColumn
cfprIppoolPoolV4Assigned=_CfprIppoolPoolV4Assigned_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,16),_CfprIppoolPoolV4Assigned_Type())
cfprIppoolPoolV4Assigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolV4Assigned.setStatus(_A)
_CfprIppoolPoolV4Size_Type=Gauge32
_CfprIppoolPoolV4Size_Object=MibTableColumn
cfprIppoolPoolV4Size=_CfprIppoolPoolV4Size_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,17),_CfprIppoolPoolV4Size_Type())
cfprIppoolPoolV4Size.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolV4Size.setStatus(_A)
_CfprIppoolPoolV6Assigned_Type=Gauge32
_CfprIppoolPoolV6Assigned_Object=MibTableColumn
cfprIppoolPoolV6Assigned=_CfprIppoolPoolV6Assigned_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,18),_CfprIppoolPoolV6Assigned_Type())
cfprIppoolPoolV6Assigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolV6Assigned.setStatus(_A)
_CfprIppoolPoolV6Size_Type=Gauge32
_CfprIppoolPoolV6Size_Object=MibTableColumn
cfprIppoolPoolV6Size=_CfprIppoolPoolV6Size_Object((1,3,6,1,4,1,9,9,826,1,41,6,1,19),_CfprIppoolPoolV6Size_Type())
cfprIppoolPoolV6Size.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolV6Size.setStatus(_A)
_CfprIppoolPoolableTable_Object=MibTable
cfprIppoolPoolableTable=_CfprIppoolPoolableTable_Object((1,3,6,1,4,1,9,9,826,1,41,7))
if mibBuilder.loadTexts:cfprIppoolPoolableTable.setStatus(_A)
_CfprIppoolPoolableEntry_Object=MibTableRow
cfprIppoolPoolableEntry=_CfprIppoolPoolableEntry_Object((1,3,6,1,4,1,9,9,826,1,41,7,1))
cfprIppoolPoolableEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprIppoolPoolableEntry.setStatus(_A)
_CfprIppoolPoolableInstanceId_Type=CfprManagedObjectId
_CfprIppoolPoolableInstanceId_Object=MibTableColumn
cfprIppoolPoolableInstanceId=_CfprIppoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,7,1,1),_CfprIppoolPoolableInstanceId_Type())
cfprIppoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolPoolableInstanceId.setStatus(_A)
_CfprIppoolPoolableDn_Type=CfprManagedObjectDn
_CfprIppoolPoolableDn_Object=MibTableColumn
cfprIppoolPoolableDn=_CfprIppoolPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,41,7,1,2),_CfprIppoolPoolableDn_Type())
cfprIppoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolableDn.setStatus(_A)
_CfprIppoolPoolableRn_Type=SnmpAdminString
_CfprIppoolPoolableRn_Object=MibTableColumn
cfprIppoolPoolableRn=_CfprIppoolPoolableRn_Object((1,3,6,1,4,1,9,9,826,1,41,7,1,3),_CfprIppoolPoolableRn_Type())
cfprIppoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolableRn.setStatus(_A)
_CfprIppoolPoolableId_Type=Unsigned64
_CfprIppoolPoolableId_Object=MibTableColumn
cfprIppoolPoolableId=_CfprIppoolPoolableId_Object((1,3,6,1,4,1,9,9,826,1,41,7,1,4),_CfprIppoolPoolableId_Type())
cfprIppoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolableId.setStatus(_A)
_CfprIppoolPoolablePoolDn_Type=SnmpAdminString
_CfprIppoolPoolablePoolDn_Object=MibTableColumn
cfprIppoolPoolablePoolDn=_CfprIppoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,826,1,41,7,1,5),_CfprIppoolPoolablePoolDn_Type())
cfprIppoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPoolablePoolDn.setStatus(_A)
_CfprIppoolPooledTable_Object=MibTable
cfprIppoolPooledTable=_CfprIppoolPooledTable_Object((1,3,6,1,4,1,9,9,826,1,41,8))
if mibBuilder.loadTexts:cfprIppoolPooledTable.setStatus(_A)
_CfprIppoolPooledEntry_Object=MibTableRow
cfprIppoolPooledEntry=_CfprIppoolPooledEntry_Object((1,3,6,1,4,1,9,9,826,1,41,8,1))
cfprIppoolPooledEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprIppoolPooledEntry.setStatus(_A)
_CfprIppoolPooledInstanceId_Type=CfprManagedObjectId
_CfprIppoolPooledInstanceId_Object=MibTableColumn
cfprIppoolPooledInstanceId=_CfprIppoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,1),_CfprIppoolPooledInstanceId_Type())
cfprIppoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolPooledInstanceId.setStatus(_A)
_CfprIppoolPooledDn_Type=CfprManagedObjectDn
_CfprIppoolPooledDn_Object=MibTableColumn
cfprIppoolPooledDn=_CfprIppoolPooledDn_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,2),_CfprIppoolPooledDn_Type())
cfprIppoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledDn.setStatus(_A)
_CfprIppoolPooledRn_Type=SnmpAdminString
_CfprIppoolPooledRn_Object=MibTableColumn
cfprIppoolPooledRn=_CfprIppoolPooledRn_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,3),_CfprIppoolPooledRn_Type())
cfprIppoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledRn.setStatus(_A)
_CfprIppoolPooledAssigned_Type=TruthValue
_CfprIppoolPooledAssigned_Object=MibTableColumn
cfprIppoolPooledAssigned=_CfprIppoolPooledAssigned_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,4),_CfprIppoolPooledAssigned_Type())
cfprIppoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledAssigned.setStatus(_A)
_CfprIppoolPooledAssignedToDn_Type=SnmpAdminString
_CfprIppoolPooledAssignedToDn_Object=MibTableColumn
cfprIppoolPooledAssignedToDn=_CfprIppoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,5),_CfprIppoolPooledAssignedToDn_Type())
cfprIppoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledAssignedToDn.setStatus(_A)
_CfprIppoolPooledDefGw_Type=InetAddressIPv4
_CfprIppoolPooledDefGw_Object=MibTableColumn
cfprIppoolPooledDefGw=_CfprIppoolPooledDefGw_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,6),_CfprIppoolPooledDefGw_Type())
cfprIppoolPooledDefGw.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledDefGw.setStatus(_A)
_CfprIppoolPooledId_Type=InetAddressIPv4
_CfprIppoolPooledId_Object=MibTableColumn
cfprIppoolPooledId=_CfprIppoolPooledId_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,7),_CfprIppoolPooledId_Type())
cfprIppoolPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledId.setStatus(_A)
_CfprIppoolPooledPoolableDn_Type=SnmpAdminString
_CfprIppoolPooledPoolableDn_Object=MibTableColumn
cfprIppoolPooledPoolableDn=_CfprIppoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,8),_CfprIppoolPooledPoolableDn_Type())
cfprIppoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledPoolableDn.setStatus(_A)
_CfprIppoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CfprIppoolPooledPrevAssignedToDn_Object=MibTableColumn
cfprIppoolPooledPrevAssignedToDn=_CfprIppoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,9),_CfprIppoolPooledPrevAssignedToDn_Type())
cfprIppoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledPrevAssignedToDn.setStatus(_A)
_CfprIppoolPooledPrimDns_Type=InetAddressIPv4
_CfprIppoolPooledPrimDns_Object=MibTableColumn
cfprIppoolPooledPrimDns=_CfprIppoolPooledPrimDns_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,10),_CfprIppoolPooledPrimDns_Type())
cfprIppoolPooledPrimDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledPrimDns.setStatus(_A)
_CfprIppoolPooledSecDns_Type=InetAddressIPv4
_CfprIppoolPooledSecDns_Object=MibTableColumn
cfprIppoolPooledSecDns=_CfprIppoolPooledSecDns_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,11),_CfprIppoolPooledSecDns_Type())
cfprIppoolPooledSecDns.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledSecDns.setStatus(_A)
_CfprIppoolPooledSubnet_Type=InetAddressIPv4
_CfprIppoolPooledSubnet_Object=MibTableColumn
cfprIppoolPooledSubnet=_CfprIppoolPooledSubnet_Object((1,3,6,1,4,1,9,9,826,1,41,8,1,12),_CfprIppoolPooledSubnet_Type())
cfprIppoolPooledSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolPooledSubnet.setStatus(_A)
_CfprIppoolUniverseTable_Object=MibTable
cfprIppoolUniverseTable=_CfprIppoolUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,41,9))
if mibBuilder.loadTexts:cfprIppoolUniverseTable.setStatus(_A)
_CfprIppoolUniverseEntry_Object=MibTableRow
cfprIppoolUniverseEntry=_CfprIppoolUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,41,9,1))
cfprIppoolUniverseEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprIppoolUniverseEntry.setStatus(_A)
_CfprIppoolUniverseInstanceId_Type=CfprManagedObjectId
_CfprIppoolUniverseInstanceId_Object=MibTableColumn
cfprIppoolUniverseInstanceId=_CfprIppoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,41,9,1,1),_CfprIppoolUniverseInstanceId_Type())
cfprIppoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIppoolUniverseInstanceId.setStatus(_A)
_CfprIppoolUniverseDn_Type=CfprManagedObjectDn
_CfprIppoolUniverseDn_Object=MibTableColumn
cfprIppoolUniverseDn=_CfprIppoolUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,41,9,1,2),_CfprIppoolUniverseDn_Type())
cfprIppoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolUniverseDn.setStatus(_A)
_CfprIppoolUniverseRn_Type=SnmpAdminString
_CfprIppoolUniverseRn_Object=MibTableColumn
cfprIppoolUniverseRn=_CfprIppoolUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,41,9,1,3),_CfprIppoolUniverseRn_Type())
cfprIppoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIppoolUniverseRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprIppoolObjects':cfprIppoolObjects,'cfprIppoolAddrTable':cfprIppoolAddrTable,'cfprIppoolAddrEntry':cfprIppoolAddrEntry,_E:cfprIppoolAddrInstanceId,'cfprIppoolAddrDn':cfprIppoolAddrDn,'cfprIppoolAddrRn':cfprIppoolAddrRn,'cfprIppoolAddrAssigned':cfprIppoolAddrAssigned,'cfprIppoolAddrAssignedToDn':cfprIppoolAddrAssignedToDn,'cfprIppoolAddrGlobalAssignedCnt':cfprIppoolAddrGlobalAssignedCnt,'cfprIppoolAddrGlobalDefinedCnt':cfprIppoolAddrGlobalDefinedCnt,'cfprIppoolAddrId':cfprIppoolAddrId,'cfprIppoolAddrOwner':cfprIppoolAddrOwner,'cfprIppoolBlockTable':cfprIppoolBlockTable,'cfprIppoolBlockEntry':cfprIppoolBlockEntry,_F:cfprIppoolBlockInstanceId,'cfprIppoolBlockDn':cfprIppoolBlockDn,'cfprIppoolBlockRn':cfprIppoolBlockRn,'cfprIppoolBlockDefGw':cfprIppoolBlockDefGw,'cfprIppoolBlockFrom':cfprIppoolBlockFrom,'cfprIppoolBlockPrimDns':cfprIppoolBlockPrimDns,'cfprIppoolBlockSecDns':cfprIppoolBlockSecDns,'cfprIppoolBlockSubnet':cfprIppoolBlockSubnet,'cfprIppoolBlockTo':cfprIppoolBlockTo,'cfprIppoolIpV6AddrTable':cfprIppoolIpV6AddrTable,'cfprIppoolIpV6AddrEntry':cfprIppoolIpV6AddrEntry,_G:cfprIppoolIpV6AddrInstanceId,'cfprIppoolIpV6AddrDn':cfprIppoolIpV6AddrDn,'cfprIppoolIpV6AddrRn':cfprIppoolIpV6AddrRn,'cfprIppoolIpV6AddrAssigned':cfprIppoolIpV6AddrAssigned,'cfprIppoolIpV6AddrAssignedToDn':cfprIppoolIpV6AddrAssignedToDn,'cfprIppoolIpV6AddrGlobalAssignedCnt':cfprIppoolIpV6AddrGlobalAssignedCnt,'cfprIppoolIpV6AddrGlobalDefinedCnt':cfprIppoolIpV6AddrGlobalDefinedCnt,'cfprIppoolIpV6AddrId':cfprIppoolIpV6AddrId,'cfprIppoolIpV6AddrOwner':cfprIppoolIpV6AddrOwner,'cfprIppoolIpV6BlockTable':cfprIppoolIpV6BlockTable,'cfprIppoolIpV6BlockEntry':cfprIppoolIpV6BlockEntry,_H:cfprIppoolIpV6BlockInstanceId,'cfprIppoolIpV6BlockDn':cfprIppoolIpV6BlockDn,'cfprIppoolIpV6BlockRn':cfprIppoolIpV6BlockRn,'cfprIppoolIpV6BlockDefGw':cfprIppoolIpV6BlockDefGw,'cfprIppoolIpV6BlockFrom':cfprIppoolIpV6BlockFrom,'cfprIppoolIpV6BlockPrefix':cfprIppoolIpV6BlockPrefix,'cfprIppoolIpV6BlockPrimDns':cfprIppoolIpV6BlockPrimDns,'cfprIppoolIpV6BlockSecDns':cfprIppoolIpV6BlockSecDns,'cfprIppoolIpV6BlockTo':cfprIppoolIpV6BlockTo,'cfprIppoolIpV6PooledTable':cfprIppoolIpV6PooledTable,'cfprIppoolIpV6PooledEntry':cfprIppoolIpV6PooledEntry,_I:cfprIppoolIpV6PooledInstanceId,'cfprIppoolIpV6PooledDn':cfprIppoolIpV6PooledDn,'cfprIppoolIpV6PooledRn':cfprIppoolIpV6PooledRn,'cfprIppoolIpV6PooledAssigned':cfprIppoolIpV6PooledAssigned,'cfprIppoolIpV6PooledAssignedToDn':cfprIppoolIpV6PooledAssignedToDn,'cfprIppoolIpV6PooledDefGw':cfprIppoolIpV6PooledDefGw,'cfprIppoolIpV6PooledId':cfprIppoolIpV6PooledId,'cfprIppoolIpV6PooledPoolableDn':cfprIppoolIpV6PooledPoolableDn,'cfprIppoolIpV6PooledPrefix':cfprIppoolIpV6PooledPrefix,'cfprIppoolIpV6PooledPrevAssignedToDn':cfprIppoolIpV6PooledPrevAssignedToDn,'cfprIppoolIpV6PooledPrimDns':cfprIppoolIpV6PooledPrimDns,'cfprIppoolIpV6PooledSecDns':cfprIppoolIpV6PooledSecDns,'cfprIppoolPoolTable':cfprIppoolPoolTable,'cfprIppoolPoolEntry':cfprIppoolPoolEntry,_J:cfprIppoolPoolInstanceId,'cfprIppoolPoolDn':cfprIppoolPoolDn,'cfprIppoolPoolRn':cfprIppoolPoolRn,'cfprIppoolPoolAssigned':cfprIppoolPoolAssigned,'cfprIppoolPoolAssignmentOrder':cfprIppoolPoolAssignmentOrder,'cfprIppoolPoolDescr':cfprIppoolPoolDescr,'cfprIppoolPoolExtManaged':cfprIppoolPoolExtManaged,'cfprIppoolPoolGuid':cfprIppoolPoolGuid,'cfprIppoolPoolIntId':cfprIppoolPoolIntId,'cfprIppoolPoolIsNetBIOSEnabled':cfprIppoolPoolIsNetBIOSEnabled,'cfprIppoolPoolName':cfprIppoolPoolName,'cfprIppoolPoolPolicyLevel':cfprIppoolPoolPolicyLevel,'cfprIppoolPoolPolicyOwner':cfprIppoolPoolPolicyOwner,'cfprIppoolPoolSize':cfprIppoolPoolSize,'cfprIppoolPoolSupportsDHCP':cfprIppoolPoolSupportsDHCP,'cfprIppoolPoolV4Assigned':cfprIppoolPoolV4Assigned,'cfprIppoolPoolV4Size':cfprIppoolPoolV4Size,'cfprIppoolPoolV6Assigned':cfprIppoolPoolV6Assigned,'cfprIppoolPoolV6Size':cfprIppoolPoolV6Size,'cfprIppoolPoolableTable':cfprIppoolPoolableTable,'cfprIppoolPoolableEntry':cfprIppoolPoolableEntry,_K:cfprIppoolPoolableInstanceId,'cfprIppoolPoolableDn':cfprIppoolPoolableDn,'cfprIppoolPoolableRn':cfprIppoolPoolableRn,'cfprIppoolPoolableId':cfprIppoolPoolableId,'cfprIppoolPoolablePoolDn':cfprIppoolPoolablePoolDn,'cfprIppoolPooledTable':cfprIppoolPooledTable,'cfprIppoolPooledEntry':cfprIppoolPooledEntry,_L:cfprIppoolPooledInstanceId,'cfprIppoolPooledDn':cfprIppoolPooledDn,'cfprIppoolPooledRn':cfprIppoolPooledRn,'cfprIppoolPooledAssigned':cfprIppoolPooledAssigned,'cfprIppoolPooledAssignedToDn':cfprIppoolPooledAssignedToDn,'cfprIppoolPooledDefGw':cfprIppoolPooledDefGw,'cfprIppoolPooledId':cfprIppoolPooledId,'cfprIppoolPooledPoolableDn':cfprIppoolPooledPoolableDn,'cfprIppoolPooledPrevAssignedToDn':cfprIppoolPooledPrevAssignedToDn,'cfprIppoolPooledPrimDns':cfprIppoolPooledPrimDns,'cfprIppoolPooledSecDns':cfprIppoolPooledSecDns,'cfprIppoolPooledSubnet':cfprIppoolPooledSubnet,'cfprIppoolUniverseTable':cfprIppoolUniverseTable,'cfprIppoolUniverseEntry':cfprIppoolUniverseEntry,_M:cfprIppoolUniverseInstanceId,'cfprIppoolUniverseDn':cfprIppoolUniverseDn,'cfprIppoolUniverseRn':cfprIppoolUniverseRn})