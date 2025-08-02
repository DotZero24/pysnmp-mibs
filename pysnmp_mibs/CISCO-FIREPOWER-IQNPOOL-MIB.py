_L='cfprIqnpoolUniverseInstanceId'
_K='cfprIqnpoolTransportBlockInstanceId'
_J='cfprIqnpoolPooledInstanceId'
_I='cfprIqnpoolPoolableInstanceId'
_H='cfprIqnpoolPoolInstanceId'
_G='cfprIqnpoolFormatInstanceId'
_F='cfprIqnpoolBlockInstanceId'
_E='cfprIqnpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-IQNPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprIqnpoolBlockFrom,CfprIqnpoolBlockTo,CfprIqnpoolPoolAssignmentOrder,CfprIqnpoolTransportBlockFrom,CfprIqnpoolTransportBlockTo,CfprPolicyPolicyOwner,CfprPoolElementOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprIqnpoolBlockFrom','CfprIqnpoolBlockTo','CfprIqnpoolPoolAssignmentOrder','CfprIqnpoolTransportBlockFrom','CfprIqnpoolTransportBlockTo','CfprPolicyPolicyOwner','CfprPoolElementOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprIqnpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,42))
_CfprIqnpoolAddrTable_Object=MibTable
cfprIqnpoolAddrTable=_CfprIqnpoolAddrTable_Object((1,3,6,1,4,1,9,9,826,1,42,1))
if mibBuilder.loadTexts:cfprIqnpoolAddrTable.setStatus(_A)
_CfprIqnpoolAddrEntry_Object=MibTableRow
cfprIqnpoolAddrEntry=_CfprIqnpoolAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,42,1,1))
cfprIqnpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprIqnpoolAddrEntry.setStatus(_A)
_CfprIqnpoolAddrInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolAddrInstanceId_Object=MibTableColumn
cfprIqnpoolAddrInstanceId=_CfprIqnpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,1),_CfprIqnpoolAddrInstanceId_Type())
cfprIqnpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolAddrInstanceId.setStatus(_A)
_CfprIqnpoolAddrDn_Type=CfprManagedObjectDn
_CfprIqnpoolAddrDn_Object=MibTableColumn
cfprIqnpoolAddrDn=_CfprIqnpoolAddrDn_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,2),_CfprIqnpoolAddrDn_Type())
cfprIqnpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrDn.setStatus(_A)
_CfprIqnpoolAddrRn_Type=SnmpAdminString
_CfprIqnpoolAddrRn_Object=MibTableColumn
cfprIqnpoolAddrRn=_CfprIqnpoolAddrRn_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,3),_CfprIqnpoolAddrRn_Type())
cfprIqnpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrRn.setStatus(_A)
_CfprIqnpoolAddrAssigned_Type=TruthValue
_CfprIqnpoolAddrAssigned_Object=MibTableColumn
cfprIqnpoolAddrAssigned=_CfprIqnpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,4),_CfprIqnpoolAddrAssigned_Type())
cfprIqnpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrAssigned.setStatus(_A)
_CfprIqnpoolAddrAssignedToDn_Type=SnmpAdminString
_CfprIqnpoolAddrAssignedToDn_Object=MibTableColumn
cfprIqnpoolAddrAssignedToDn=_CfprIqnpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,5),_CfprIqnpoolAddrAssignedToDn_Type())
cfprIqnpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrAssignedToDn.setStatus(_A)
_CfprIqnpoolAddrGlobalAssignedCnt_Type=Gauge32
_CfprIqnpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cfprIqnpoolAddrGlobalAssignedCnt=_CfprIqnpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,6),_CfprIqnpoolAddrGlobalAssignedCnt_Type())
cfprIqnpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrGlobalAssignedCnt.setStatus(_A)
_CfprIqnpoolAddrGlobalDefinedCnt_Type=Gauge32
_CfprIqnpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cfprIqnpoolAddrGlobalDefinedCnt=_CfprIqnpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,7),_CfprIqnpoolAddrGlobalDefinedCnt_Type())
cfprIqnpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrGlobalDefinedCnt.setStatus(_A)
_CfprIqnpoolAddrName_Type=SnmpAdminString
_CfprIqnpoolAddrName_Object=MibTableColumn
cfprIqnpoolAddrName=_CfprIqnpoolAddrName_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,8),_CfprIqnpoolAddrName_Type())
cfprIqnpoolAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrName.setStatus(_A)
_CfprIqnpoolAddrOwner_Type=CfprPoolElementOwner
_CfprIqnpoolAddrOwner_Object=MibTableColumn
cfprIqnpoolAddrOwner=_CfprIqnpoolAddrOwner_Object((1,3,6,1,4,1,9,9,826,1,42,1,1,9),_CfprIqnpoolAddrOwner_Type())
cfprIqnpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolAddrOwner.setStatus(_A)
_CfprIqnpoolBlockTable_Object=MibTable
cfprIqnpoolBlockTable=_CfprIqnpoolBlockTable_Object((1,3,6,1,4,1,9,9,826,1,42,2))
if mibBuilder.loadTexts:cfprIqnpoolBlockTable.setStatus(_A)
_CfprIqnpoolBlockEntry_Object=MibTableRow
cfprIqnpoolBlockEntry=_CfprIqnpoolBlockEntry_Object((1,3,6,1,4,1,9,9,826,1,42,2,1))
cfprIqnpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprIqnpoolBlockEntry.setStatus(_A)
_CfprIqnpoolBlockInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolBlockInstanceId_Object=MibTableColumn
cfprIqnpoolBlockInstanceId=_CfprIqnpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,2,1,1),_CfprIqnpoolBlockInstanceId_Type())
cfprIqnpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolBlockInstanceId.setStatus(_A)
_CfprIqnpoolBlockDn_Type=CfprManagedObjectDn
_CfprIqnpoolBlockDn_Object=MibTableColumn
cfprIqnpoolBlockDn=_CfprIqnpoolBlockDn_Object((1,3,6,1,4,1,9,9,826,1,42,2,1,2),_CfprIqnpoolBlockDn_Type())
cfprIqnpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolBlockDn.setStatus(_A)
_CfprIqnpoolBlockRn_Type=SnmpAdminString
_CfprIqnpoolBlockRn_Object=MibTableColumn
cfprIqnpoolBlockRn=_CfprIqnpoolBlockRn_Object((1,3,6,1,4,1,9,9,826,1,42,2,1,3),_CfprIqnpoolBlockRn_Type())
cfprIqnpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolBlockRn.setStatus(_A)
_CfprIqnpoolBlockFrom_Type=CfprIqnpoolBlockFrom
_CfprIqnpoolBlockFrom_Object=MibTableColumn
cfprIqnpoolBlockFrom=_CfprIqnpoolBlockFrom_Object((1,3,6,1,4,1,9,9,826,1,42,2,1,4),_CfprIqnpoolBlockFrom_Type())
cfprIqnpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolBlockFrom.setStatus(_A)
_CfprIqnpoolBlockSuffix_Type=SnmpAdminString
_CfprIqnpoolBlockSuffix_Object=MibTableColumn
cfprIqnpoolBlockSuffix=_CfprIqnpoolBlockSuffix_Object((1,3,6,1,4,1,9,9,826,1,42,2,1,5),_CfprIqnpoolBlockSuffix_Type())
cfprIqnpoolBlockSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolBlockSuffix.setStatus(_A)
_CfprIqnpoolBlockTo_Type=CfprIqnpoolBlockTo
_CfprIqnpoolBlockTo_Object=MibTableColumn
cfprIqnpoolBlockTo=_CfprIqnpoolBlockTo_Object((1,3,6,1,4,1,9,9,826,1,42,2,1,6),_CfprIqnpoolBlockTo_Type())
cfprIqnpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolBlockTo.setStatus(_A)
_CfprIqnpoolFormatTable_Object=MibTable
cfprIqnpoolFormatTable=_CfprIqnpoolFormatTable_Object((1,3,6,1,4,1,9,9,826,1,42,3))
if mibBuilder.loadTexts:cfprIqnpoolFormatTable.setStatus(_A)
_CfprIqnpoolFormatEntry_Object=MibTableRow
cfprIqnpoolFormatEntry=_CfprIqnpoolFormatEntry_Object((1,3,6,1,4,1,9,9,826,1,42,3,1))
cfprIqnpoolFormatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprIqnpoolFormatEntry.setStatus(_A)
_CfprIqnpoolFormatInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolFormatInstanceId_Object=MibTableColumn
cfprIqnpoolFormatInstanceId=_CfprIqnpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,3,1,1),_CfprIqnpoolFormatInstanceId_Type())
cfprIqnpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolFormatInstanceId.setStatus(_A)
_CfprIqnpoolFormatDn_Type=CfprManagedObjectDn
_CfprIqnpoolFormatDn_Object=MibTableColumn
cfprIqnpoolFormatDn=_CfprIqnpoolFormatDn_Object((1,3,6,1,4,1,9,9,826,1,42,3,1,2),_CfprIqnpoolFormatDn_Type())
cfprIqnpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolFormatDn.setStatus(_A)
_CfprIqnpoolFormatRn_Type=SnmpAdminString
_CfprIqnpoolFormatRn_Object=MibTableColumn
cfprIqnpoolFormatRn=_CfprIqnpoolFormatRn_Object((1,3,6,1,4,1,9,9,826,1,42,3,1,3),_CfprIqnpoolFormatRn_Type())
cfprIqnpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolFormatRn.setStatus(_A)
_CfprIqnpoolFormatFormat_Type=SnmpAdminString
_CfprIqnpoolFormatFormat_Object=MibTableColumn
cfprIqnpoolFormatFormat=_CfprIqnpoolFormatFormat_Object((1,3,6,1,4,1,9,9,826,1,42,3,1,4),_CfprIqnpoolFormatFormat_Type())
cfprIqnpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolFormatFormat.setStatus(_A)
_CfprIqnpoolPoolTable_Object=MibTable
cfprIqnpoolPoolTable=_CfprIqnpoolPoolTable_Object((1,3,6,1,4,1,9,9,826,1,42,4))
if mibBuilder.loadTexts:cfprIqnpoolPoolTable.setStatus(_A)
_CfprIqnpoolPoolEntry_Object=MibTableRow
cfprIqnpoolPoolEntry=_CfprIqnpoolPoolEntry_Object((1,3,6,1,4,1,9,9,826,1,42,4,1))
cfprIqnpoolPoolEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprIqnpoolPoolEntry.setStatus(_A)
_CfprIqnpoolPoolInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolPoolInstanceId_Object=MibTableColumn
cfprIqnpoolPoolInstanceId=_CfprIqnpoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,1),_CfprIqnpoolPoolInstanceId_Type())
cfprIqnpoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolPoolInstanceId.setStatus(_A)
_CfprIqnpoolPoolDn_Type=CfprManagedObjectDn
_CfprIqnpoolPoolDn_Object=MibTableColumn
cfprIqnpoolPoolDn=_CfprIqnpoolPoolDn_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,2),_CfprIqnpoolPoolDn_Type())
cfprIqnpoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolDn.setStatus(_A)
_CfprIqnpoolPoolRn_Type=SnmpAdminString
_CfprIqnpoolPoolRn_Object=MibTableColumn
cfprIqnpoolPoolRn=_CfprIqnpoolPoolRn_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,3),_CfprIqnpoolPoolRn_Type())
cfprIqnpoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolRn.setStatus(_A)
_CfprIqnpoolPoolAssigned_Type=Gauge32
_CfprIqnpoolPoolAssigned_Object=MibTableColumn
cfprIqnpoolPoolAssigned=_CfprIqnpoolPoolAssigned_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,4),_CfprIqnpoolPoolAssigned_Type())
cfprIqnpoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolAssigned.setStatus(_A)
_CfprIqnpoolPoolAssignmentOrder_Type=CfprIqnpoolPoolAssignmentOrder
_CfprIqnpoolPoolAssignmentOrder_Object=MibTableColumn
cfprIqnpoolPoolAssignmentOrder=_CfprIqnpoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,5),_CfprIqnpoolPoolAssignmentOrder_Type())
cfprIqnpoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolAssignmentOrder.setStatus(_A)
_CfprIqnpoolPoolDescr_Type=SnmpAdminString
_CfprIqnpoolPoolDescr_Object=MibTableColumn
cfprIqnpoolPoolDescr=_CfprIqnpoolPoolDescr_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,6),_CfprIqnpoolPoolDescr_Type())
cfprIqnpoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolDescr.setStatus(_A)
_CfprIqnpoolPoolIntId_Type=SnmpAdminString
_CfprIqnpoolPoolIntId_Object=MibTableColumn
cfprIqnpoolPoolIntId=_CfprIqnpoolPoolIntId_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,7),_CfprIqnpoolPoolIntId_Type())
cfprIqnpoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolIntId.setStatus(_A)
_CfprIqnpoolPoolName_Type=SnmpAdminString
_CfprIqnpoolPoolName_Object=MibTableColumn
cfprIqnpoolPoolName=_CfprIqnpoolPoolName_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,8),_CfprIqnpoolPoolName_Type())
cfprIqnpoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolName.setStatus(_A)
_CfprIqnpoolPoolPolicyLevel_Type=Gauge32
_CfprIqnpoolPoolPolicyLevel_Object=MibTableColumn
cfprIqnpoolPoolPolicyLevel=_CfprIqnpoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,9),_CfprIqnpoolPoolPolicyLevel_Type())
cfprIqnpoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolPolicyLevel.setStatus(_A)
_CfprIqnpoolPoolPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprIqnpoolPoolPolicyOwner_Object=MibTableColumn
cfprIqnpoolPoolPolicyOwner=_CfprIqnpoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,10),_CfprIqnpoolPoolPolicyOwner_Type())
cfprIqnpoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolPolicyOwner.setStatus(_A)
_CfprIqnpoolPoolPrefix_Type=SnmpAdminString
_CfprIqnpoolPoolPrefix_Object=MibTableColumn
cfprIqnpoolPoolPrefix=_CfprIqnpoolPoolPrefix_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,11),_CfprIqnpoolPoolPrefix_Type())
cfprIqnpoolPoolPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolPrefix.setStatus(_A)
_CfprIqnpoolPoolSize_Type=Gauge32
_CfprIqnpoolPoolSize_Object=MibTableColumn
cfprIqnpoolPoolSize=_CfprIqnpoolPoolSize_Object((1,3,6,1,4,1,9,9,826,1,42,4,1,12),_CfprIqnpoolPoolSize_Type())
cfprIqnpoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolSize.setStatus(_A)
_CfprIqnpoolPoolableTable_Object=MibTable
cfprIqnpoolPoolableTable=_CfprIqnpoolPoolableTable_Object((1,3,6,1,4,1,9,9,826,1,42,5))
if mibBuilder.loadTexts:cfprIqnpoolPoolableTable.setStatus(_A)
_CfprIqnpoolPoolableEntry_Object=MibTableRow
cfprIqnpoolPoolableEntry=_CfprIqnpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,826,1,42,5,1))
cfprIqnpoolPoolableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprIqnpoolPoolableEntry.setStatus(_A)
_CfprIqnpoolPoolableInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolPoolableInstanceId_Object=MibTableColumn
cfprIqnpoolPoolableInstanceId=_CfprIqnpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,5,1,1),_CfprIqnpoolPoolableInstanceId_Type())
cfprIqnpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolPoolableInstanceId.setStatus(_A)
_CfprIqnpoolPoolableDn_Type=CfprManagedObjectDn
_CfprIqnpoolPoolableDn_Object=MibTableColumn
cfprIqnpoolPoolableDn=_CfprIqnpoolPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,42,5,1,2),_CfprIqnpoolPoolableDn_Type())
cfprIqnpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolableDn.setStatus(_A)
_CfprIqnpoolPoolableRn_Type=SnmpAdminString
_CfprIqnpoolPoolableRn_Object=MibTableColumn
cfprIqnpoolPoolableRn=_CfprIqnpoolPoolableRn_Object((1,3,6,1,4,1,9,9,826,1,42,5,1,3),_CfprIqnpoolPoolableRn_Type())
cfprIqnpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolableRn.setStatus(_A)
_CfprIqnpoolPoolableId_Type=Unsigned64
_CfprIqnpoolPoolableId_Object=MibTableColumn
cfprIqnpoolPoolableId=_CfprIqnpoolPoolableId_Object((1,3,6,1,4,1,9,9,826,1,42,5,1,4),_CfprIqnpoolPoolableId_Type())
cfprIqnpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolableId.setStatus(_A)
_CfprIqnpoolPoolablePoolDn_Type=SnmpAdminString
_CfprIqnpoolPoolablePoolDn_Object=MibTableColumn
cfprIqnpoolPoolablePoolDn=_CfprIqnpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,826,1,42,5,1,5),_CfprIqnpoolPoolablePoolDn_Type())
cfprIqnpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPoolablePoolDn.setStatus(_A)
_CfprIqnpoolPooledTable_Object=MibTable
cfprIqnpoolPooledTable=_CfprIqnpoolPooledTable_Object((1,3,6,1,4,1,9,9,826,1,42,6))
if mibBuilder.loadTexts:cfprIqnpoolPooledTable.setStatus(_A)
_CfprIqnpoolPooledEntry_Object=MibTableRow
cfprIqnpoolPooledEntry=_CfprIqnpoolPooledEntry_Object((1,3,6,1,4,1,9,9,826,1,42,6,1))
cfprIqnpoolPooledEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprIqnpoolPooledEntry.setStatus(_A)
_CfprIqnpoolPooledInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolPooledInstanceId_Object=MibTableColumn
cfprIqnpoolPooledInstanceId=_CfprIqnpoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,1),_CfprIqnpoolPooledInstanceId_Type())
cfprIqnpoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolPooledInstanceId.setStatus(_A)
_CfprIqnpoolPooledDn_Type=CfprManagedObjectDn
_CfprIqnpoolPooledDn_Object=MibTableColumn
cfprIqnpoolPooledDn=_CfprIqnpoolPooledDn_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,2),_CfprIqnpoolPooledDn_Type())
cfprIqnpoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledDn.setStatus(_A)
_CfprIqnpoolPooledRn_Type=SnmpAdminString
_CfprIqnpoolPooledRn_Object=MibTableColumn
cfprIqnpoolPooledRn=_CfprIqnpoolPooledRn_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,3),_CfprIqnpoolPooledRn_Type())
cfprIqnpoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledRn.setStatus(_A)
_CfprIqnpoolPooledAssigned_Type=TruthValue
_CfprIqnpoolPooledAssigned_Object=MibTableColumn
cfprIqnpoolPooledAssigned=_CfprIqnpoolPooledAssigned_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,4),_CfprIqnpoolPooledAssigned_Type())
cfprIqnpoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledAssigned.setStatus(_A)
_CfprIqnpoolPooledAssignedToDn_Type=SnmpAdminString
_CfprIqnpoolPooledAssignedToDn_Object=MibTableColumn
cfprIqnpoolPooledAssignedToDn=_CfprIqnpoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,5),_CfprIqnpoolPooledAssignedToDn_Type())
cfprIqnpoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledAssignedToDn.setStatus(_A)
_CfprIqnpoolPooledName_Type=SnmpAdminString
_CfprIqnpoolPooledName_Object=MibTableColumn
cfprIqnpoolPooledName=_CfprIqnpoolPooledName_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,6),_CfprIqnpoolPooledName_Type())
cfprIqnpoolPooledName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledName.setStatus(_A)
_CfprIqnpoolPooledPoolableDn_Type=SnmpAdminString
_CfprIqnpoolPooledPoolableDn_Object=MibTableColumn
cfprIqnpoolPooledPoolableDn=_CfprIqnpoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,7),_CfprIqnpoolPooledPoolableDn_Type())
cfprIqnpoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledPoolableDn.setStatus(_A)
_CfprIqnpoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CfprIqnpoolPooledPrevAssignedToDn_Object=MibTableColumn
cfprIqnpoolPooledPrevAssignedToDn=_CfprIqnpoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,42,6,1,8),_CfprIqnpoolPooledPrevAssignedToDn_Type())
cfprIqnpoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolPooledPrevAssignedToDn.setStatus(_A)
_CfprIqnpoolTransportBlockTable_Object=MibTable
cfprIqnpoolTransportBlockTable=_CfprIqnpoolTransportBlockTable_Object((1,3,6,1,4,1,9,9,826,1,42,7))
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockTable.setStatus(_A)
_CfprIqnpoolTransportBlockEntry_Object=MibTableRow
cfprIqnpoolTransportBlockEntry=_CfprIqnpoolTransportBlockEntry_Object((1,3,6,1,4,1,9,9,826,1,42,7,1))
cfprIqnpoolTransportBlockEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockEntry.setStatus(_A)
_CfprIqnpoolTransportBlockInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolTransportBlockInstanceId_Object=MibTableColumn
cfprIqnpoolTransportBlockInstanceId=_CfprIqnpoolTransportBlockInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,7,1,1),_CfprIqnpoolTransportBlockInstanceId_Type())
cfprIqnpoolTransportBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockInstanceId.setStatus(_A)
_CfprIqnpoolTransportBlockDn_Type=CfprManagedObjectDn
_CfprIqnpoolTransportBlockDn_Object=MibTableColumn
cfprIqnpoolTransportBlockDn=_CfprIqnpoolTransportBlockDn_Object((1,3,6,1,4,1,9,9,826,1,42,7,1,2),_CfprIqnpoolTransportBlockDn_Type())
cfprIqnpoolTransportBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockDn.setStatus(_A)
_CfprIqnpoolTransportBlockRn_Type=SnmpAdminString
_CfprIqnpoolTransportBlockRn_Object=MibTableColumn
cfprIqnpoolTransportBlockRn=_CfprIqnpoolTransportBlockRn_Object((1,3,6,1,4,1,9,9,826,1,42,7,1,3),_CfprIqnpoolTransportBlockRn_Type())
cfprIqnpoolTransportBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockRn.setStatus(_A)
_CfprIqnpoolTransportBlockFrom_Type=CfprIqnpoolTransportBlockFrom
_CfprIqnpoolTransportBlockFrom_Object=MibTableColumn
cfprIqnpoolTransportBlockFrom=_CfprIqnpoolTransportBlockFrom_Object((1,3,6,1,4,1,9,9,826,1,42,7,1,4),_CfprIqnpoolTransportBlockFrom_Type())
cfprIqnpoolTransportBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockFrom.setStatus(_A)
_CfprIqnpoolTransportBlockSuffix_Type=SnmpAdminString
_CfprIqnpoolTransportBlockSuffix_Object=MibTableColumn
cfprIqnpoolTransportBlockSuffix=_CfprIqnpoolTransportBlockSuffix_Object((1,3,6,1,4,1,9,9,826,1,42,7,1,5),_CfprIqnpoolTransportBlockSuffix_Type())
cfprIqnpoolTransportBlockSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockSuffix.setStatus(_A)
_CfprIqnpoolTransportBlockTo_Type=CfprIqnpoolTransportBlockTo
_CfprIqnpoolTransportBlockTo_Object=MibTableColumn
cfprIqnpoolTransportBlockTo=_CfprIqnpoolTransportBlockTo_Object((1,3,6,1,4,1,9,9,826,1,42,7,1,6),_CfprIqnpoolTransportBlockTo_Type())
cfprIqnpoolTransportBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolTransportBlockTo.setStatus(_A)
_CfprIqnpoolUniverseTable_Object=MibTable
cfprIqnpoolUniverseTable=_CfprIqnpoolUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,42,8))
if mibBuilder.loadTexts:cfprIqnpoolUniverseTable.setStatus(_A)
_CfprIqnpoolUniverseEntry_Object=MibTableRow
cfprIqnpoolUniverseEntry=_CfprIqnpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,42,8,1))
cfprIqnpoolUniverseEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprIqnpoolUniverseEntry.setStatus(_A)
_CfprIqnpoolUniverseInstanceId_Type=CfprManagedObjectId
_CfprIqnpoolUniverseInstanceId_Object=MibTableColumn
cfprIqnpoolUniverseInstanceId=_CfprIqnpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,42,8,1,1),_CfprIqnpoolUniverseInstanceId_Type())
cfprIqnpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprIqnpoolUniverseInstanceId.setStatus(_A)
_CfprIqnpoolUniverseDn_Type=CfprManagedObjectDn
_CfprIqnpoolUniverseDn_Object=MibTableColumn
cfprIqnpoolUniverseDn=_CfprIqnpoolUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,42,8,1,2),_CfprIqnpoolUniverseDn_Type())
cfprIqnpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolUniverseDn.setStatus(_A)
_CfprIqnpoolUniverseRn_Type=SnmpAdminString
_CfprIqnpoolUniverseRn_Object=MibTableColumn
cfprIqnpoolUniverseRn=_CfprIqnpoolUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,42,8,1,3),_CfprIqnpoolUniverseRn_Type())
cfprIqnpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprIqnpoolUniverseRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprIqnpoolObjects':cfprIqnpoolObjects,'cfprIqnpoolAddrTable':cfprIqnpoolAddrTable,'cfprIqnpoolAddrEntry':cfprIqnpoolAddrEntry,_E:cfprIqnpoolAddrInstanceId,'cfprIqnpoolAddrDn':cfprIqnpoolAddrDn,'cfprIqnpoolAddrRn':cfprIqnpoolAddrRn,'cfprIqnpoolAddrAssigned':cfprIqnpoolAddrAssigned,'cfprIqnpoolAddrAssignedToDn':cfprIqnpoolAddrAssignedToDn,'cfprIqnpoolAddrGlobalAssignedCnt':cfprIqnpoolAddrGlobalAssignedCnt,'cfprIqnpoolAddrGlobalDefinedCnt':cfprIqnpoolAddrGlobalDefinedCnt,'cfprIqnpoolAddrName':cfprIqnpoolAddrName,'cfprIqnpoolAddrOwner':cfprIqnpoolAddrOwner,'cfprIqnpoolBlockTable':cfprIqnpoolBlockTable,'cfprIqnpoolBlockEntry':cfprIqnpoolBlockEntry,_F:cfprIqnpoolBlockInstanceId,'cfprIqnpoolBlockDn':cfprIqnpoolBlockDn,'cfprIqnpoolBlockRn':cfprIqnpoolBlockRn,'cfprIqnpoolBlockFrom':cfprIqnpoolBlockFrom,'cfprIqnpoolBlockSuffix':cfprIqnpoolBlockSuffix,'cfprIqnpoolBlockTo':cfprIqnpoolBlockTo,'cfprIqnpoolFormatTable':cfprIqnpoolFormatTable,'cfprIqnpoolFormatEntry':cfprIqnpoolFormatEntry,_G:cfprIqnpoolFormatInstanceId,'cfprIqnpoolFormatDn':cfprIqnpoolFormatDn,'cfprIqnpoolFormatRn':cfprIqnpoolFormatRn,'cfprIqnpoolFormatFormat':cfprIqnpoolFormatFormat,'cfprIqnpoolPoolTable':cfprIqnpoolPoolTable,'cfprIqnpoolPoolEntry':cfprIqnpoolPoolEntry,_H:cfprIqnpoolPoolInstanceId,'cfprIqnpoolPoolDn':cfprIqnpoolPoolDn,'cfprIqnpoolPoolRn':cfprIqnpoolPoolRn,'cfprIqnpoolPoolAssigned':cfprIqnpoolPoolAssigned,'cfprIqnpoolPoolAssignmentOrder':cfprIqnpoolPoolAssignmentOrder,'cfprIqnpoolPoolDescr':cfprIqnpoolPoolDescr,'cfprIqnpoolPoolIntId':cfprIqnpoolPoolIntId,'cfprIqnpoolPoolName':cfprIqnpoolPoolName,'cfprIqnpoolPoolPolicyLevel':cfprIqnpoolPoolPolicyLevel,'cfprIqnpoolPoolPolicyOwner':cfprIqnpoolPoolPolicyOwner,'cfprIqnpoolPoolPrefix':cfprIqnpoolPoolPrefix,'cfprIqnpoolPoolSize':cfprIqnpoolPoolSize,'cfprIqnpoolPoolableTable':cfprIqnpoolPoolableTable,'cfprIqnpoolPoolableEntry':cfprIqnpoolPoolableEntry,_I:cfprIqnpoolPoolableInstanceId,'cfprIqnpoolPoolableDn':cfprIqnpoolPoolableDn,'cfprIqnpoolPoolableRn':cfprIqnpoolPoolableRn,'cfprIqnpoolPoolableId':cfprIqnpoolPoolableId,'cfprIqnpoolPoolablePoolDn':cfprIqnpoolPoolablePoolDn,'cfprIqnpoolPooledTable':cfprIqnpoolPooledTable,'cfprIqnpoolPooledEntry':cfprIqnpoolPooledEntry,_J:cfprIqnpoolPooledInstanceId,'cfprIqnpoolPooledDn':cfprIqnpoolPooledDn,'cfprIqnpoolPooledRn':cfprIqnpoolPooledRn,'cfprIqnpoolPooledAssigned':cfprIqnpoolPooledAssigned,'cfprIqnpoolPooledAssignedToDn':cfprIqnpoolPooledAssignedToDn,'cfprIqnpoolPooledName':cfprIqnpoolPooledName,'cfprIqnpoolPooledPoolableDn':cfprIqnpoolPooledPoolableDn,'cfprIqnpoolPooledPrevAssignedToDn':cfprIqnpoolPooledPrevAssignedToDn,'cfprIqnpoolTransportBlockTable':cfprIqnpoolTransportBlockTable,'cfprIqnpoolTransportBlockEntry':cfprIqnpoolTransportBlockEntry,_K:cfprIqnpoolTransportBlockInstanceId,'cfprIqnpoolTransportBlockDn':cfprIqnpoolTransportBlockDn,'cfprIqnpoolTransportBlockRn':cfprIqnpoolTransportBlockRn,'cfprIqnpoolTransportBlockFrom':cfprIqnpoolTransportBlockFrom,'cfprIqnpoolTransportBlockSuffix':cfprIqnpoolTransportBlockSuffix,'cfprIqnpoolTransportBlockTo':cfprIqnpoolTransportBlockTo,'cfprIqnpoolUniverseTable':cfprIqnpoolUniverseTable,'cfprIqnpoolUniverseEntry':cfprIqnpoolUniverseEntry,_L:cfprIqnpoolUniverseInstanceId,'cfprIqnpoolUniverseDn':cfprIqnpoolUniverseDn,'cfprIqnpoolUniverseRn':cfprIqnpoolUniverseRn})