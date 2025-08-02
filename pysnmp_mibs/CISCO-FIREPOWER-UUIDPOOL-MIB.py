_K='cfprUuidpoolUniverseInstanceId'
_J='cfprUuidpoolPooledInstanceId'
_I='cfprUuidpoolPoolableInstanceId'
_H='cfprUuidpoolPoolInstanceId'
_G='cfprUuidpoolFormatInstanceId'
_F='cfprUuidpoolBlockInstanceId'
_E='cfprUuidpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-UUIDPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprAddressUIDSuffxMask,CfprPolicyPolicyOwner,CfprPoolElementOwner,CfprUuidpoolPoolAssignmentOrder=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprAddressUIDSuffxMask','CfprPolicyPolicyOwner','CfprPoolElementOwner','CfprUuidpoolPoolAssignmentOrder')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprUuidpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,80))
_CfprUuidpoolAddrTable_Object=MibTable
cfprUuidpoolAddrTable=_CfprUuidpoolAddrTable_Object((1,3,6,1,4,1,9,9,826,1,80,1))
if mibBuilder.loadTexts:cfprUuidpoolAddrTable.setStatus(_A)
_CfprUuidpoolAddrEntry_Object=MibTableRow
cfprUuidpoolAddrEntry=_CfprUuidpoolAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,80,1,1))
cfprUuidpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprUuidpoolAddrEntry.setStatus(_A)
_CfprUuidpoolAddrInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolAddrInstanceId_Object=MibTableColumn
cfprUuidpoolAddrInstanceId=_CfprUuidpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,1),_CfprUuidpoolAddrInstanceId_Type())
cfprUuidpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolAddrInstanceId.setStatus(_A)
_CfprUuidpoolAddrDn_Type=CfprManagedObjectDn
_CfprUuidpoolAddrDn_Object=MibTableColumn
cfprUuidpoolAddrDn=_CfprUuidpoolAddrDn_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,2),_CfprUuidpoolAddrDn_Type())
cfprUuidpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrDn.setStatus(_A)
_CfprUuidpoolAddrRn_Type=SnmpAdminString
_CfprUuidpoolAddrRn_Object=MibTableColumn
cfprUuidpoolAddrRn=_CfprUuidpoolAddrRn_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,3),_CfprUuidpoolAddrRn_Type())
cfprUuidpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrRn.setStatus(_A)
_CfprUuidpoolAddrAssigned_Type=TruthValue
_CfprUuidpoolAddrAssigned_Object=MibTableColumn
cfprUuidpoolAddrAssigned=_CfprUuidpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,4),_CfprUuidpoolAddrAssigned_Type())
cfprUuidpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrAssigned.setStatus(_A)
_CfprUuidpoolAddrAssignedToDn_Type=SnmpAdminString
_CfprUuidpoolAddrAssignedToDn_Object=MibTableColumn
cfprUuidpoolAddrAssignedToDn=_CfprUuidpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,5),_CfprUuidpoolAddrAssignedToDn_Type())
cfprUuidpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrAssignedToDn.setStatus(_A)
_CfprUuidpoolAddrGlobalAssignedCnt_Type=Gauge32
_CfprUuidpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cfprUuidpoolAddrGlobalAssignedCnt=_CfprUuidpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,6),_CfprUuidpoolAddrGlobalAssignedCnt_Type())
cfprUuidpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrGlobalAssignedCnt.setStatus(_A)
_CfprUuidpoolAddrGlobalDefinedCnt_Type=Gauge32
_CfprUuidpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cfprUuidpoolAddrGlobalDefinedCnt=_CfprUuidpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,7),_CfprUuidpoolAddrGlobalDefinedCnt_Type())
cfprUuidpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrGlobalDefinedCnt.setStatus(_A)
_CfprUuidpoolAddrId_Type=SnmpAdminString
_CfprUuidpoolAddrId_Object=MibTableColumn
cfprUuidpoolAddrId=_CfprUuidpoolAddrId_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,8),_CfprUuidpoolAddrId_Type())
cfprUuidpoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrId.setStatus(_A)
_CfprUuidpoolAddrOwner_Type=CfprPoolElementOwner
_CfprUuidpoolAddrOwner_Object=MibTableColumn
cfprUuidpoolAddrOwner=_CfprUuidpoolAddrOwner_Object((1,3,6,1,4,1,9,9,826,1,80,1,1,9),_CfprUuidpoolAddrOwner_Type())
cfprUuidpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolAddrOwner.setStatus(_A)
_CfprUuidpoolBlockTable_Object=MibTable
cfprUuidpoolBlockTable=_CfprUuidpoolBlockTable_Object((1,3,6,1,4,1,9,9,826,1,80,2))
if mibBuilder.loadTexts:cfprUuidpoolBlockTable.setStatus(_A)
_CfprUuidpoolBlockEntry_Object=MibTableRow
cfprUuidpoolBlockEntry=_CfprUuidpoolBlockEntry_Object((1,3,6,1,4,1,9,9,826,1,80,2,1))
cfprUuidpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprUuidpoolBlockEntry.setStatus(_A)
_CfprUuidpoolBlockInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolBlockInstanceId_Object=MibTableColumn
cfprUuidpoolBlockInstanceId=_CfprUuidpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,2,1,1),_CfprUuidpoolBlockInstanceId_Type())
cfprUuidpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolBlockInstanceId.setStatus(_A)
_CfprUuidpoolBlockDn_Type=CfprManagedObjectDn
_CfprUuidpoolBlockDn_Object=MibTableColumn
cfprUuidpoolBlockDn=_CfprUuidpoolBlockDn_Object((1,3,6,1,4,1,9,9,826,1,80,2,1,2),_CfprUuidpoolBlockDn_Type())
cfprUuidpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolBlockDn.setStatus(_A)
_CfprUuidpoolBlockRn_Type=SnmpAdminString
_CfprUuidpoolBlockRn_Object=MibTableColumn
cfprUuidpoolBlockRn=_CfprUuidpoolBlockRn_Object((1,3,6,1,4,1,9,9,826,1,80,2,1,3),_CfprUuidpoolBlockRn_Type())
cfprUuidpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolBlockRn.setStatus(_A)
_CfprUuidpoolBlockFrom_Type=Unsigned64
_CfprUuidpoolBlockFrom_Object=MibTableColumn
cfprUuidpoolBlockFrom=_CfprUuidpoolBlockFrom_Object((1,3,6,1,4,1,9,9,826,1,80,2,1,4),_CfprUuidpoolBlockFrom_Type())
cfprUuidpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolBlockFrom.setStatus(_A)
_CfprUuidpoolBlockTo_Type=Unsigned64
_CfprUuidpoolBlockTo_Object=MibTableColumn
cfprUuidpoolBlockTo=_CfprUuidpoolBlockTo_Object((1,3,6,1,4,1,9,9,826,1,80,2,1,5),_CfprUuidpoolBlockTo_Type())
cfprUuidpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolBlockTo.setStatus(_A)
_CfprUuidpoolFormatTable_Object=MibTable
cfprUuidpoolFormatTable=_CfprUuidpoolFormatTable_Object((1,3,6,1,4,1,9,9,826,1,80,3))
if mibBuilder.loadTexts:cfprUuidpoolFormatTable.setStatus(_A)
_CfprUuidpoolFormatEntry_Object=MibTableRow
cfprUuidpoolFormatEntry=_CfprUuidpoolFormatEntry_Object((1,3,6,1,4,1,9,9,826,1,80,3,1))
cfprUuidpoolFormatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprUuidpoolFormatEntry.setStatus(_A)
_CfprUuidpoolFormatInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolFormatInstanceId_Object=MibTableColumn
cfprUuidpoolFormatInstanceId=_CfprUuidpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,3,1,1),_CfprUuidpoolFormatInstanceId_Type())
cfprUuidpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolFormatInstanceId.setStatus(_A)
_CfprUuidpoolFormatDn_Type=CfprManagedObjectDn
_CfprUuidpoolFormatDn_Object=MibTableColumn
cfprUuidpoolFormatDn=_CfprUuidpoolFormatDn_Object((1,3,6,1,4,1,9,9,826,1,80,3,1,2),_CfprUuidpoolFormatDn_Type())
cfprUuidpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolFormatDn.setStatus(_A)
_CfprUuidpoolFormatRn_Type=SnmpAdminString
_CfprUuidpoolFormatRn_Object=MibTableColumn
cfprUuidpoolFormatRn=_CfprUuidpoolFormatRn_Object((1,3,6,1,4,1,9,9,826,1,80,3,1,3),_CfprUuidpoolFormatRn_Type())
cfprUuidpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolFormatRn.setStatus(_A)
_CfprUuidpoolFormatFormat_Type=Unsigned64
_CfprUuidpoolFormatFormat_Object=MibTableColumn
cfprUuidpoolFormatFormat=_CfprUuidpoolFormatFormat_Object((1,3,6,1,4,1,9,9,826,1,80,3,1,4),_CfprUuidpoolFormatFormat_Type())
cfprUuidpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolFormatFormat.setStatus(_A)
_CfprUuidpoolFormatMask_Type=CfprAddressUIDSuffxMask
_CfprUuidpoolFormatMask_Object=MibTableColumn
cfprUuidpoolFormatMask=_CfprUuidpoolFormatMask_Object((1,3,6,1,4,1,9,9,826,1,80,3,1,5),_CfprUuidpoolFormatMask_Type())
cfprUuidpoolFormatMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolFormatMask.setStatus(_A)
_CfprUuidpoolPoolTable_Object=MibTable
cfprUuidpoolPoolTable=_CfprUuidpoolPoolTable_Object((1,3,6,1,4,1,9,9,826,1,80,4))
if mibBuilder.loadTexts:cfprUuidpoolPoolTable.setStatus(_A)
_CfprUuidpoolPoolEntry_Object=MibTableRow
cfprUuidpoolPoolEntry=_CfprUuidpoolPoolEntry_Object((1,3,6,1,4,1,9,9,826,1,80,4,1))
cfprUuidpoolPoolEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprUuidpoolPoolEntry.setStatus(_A)
_CfprUuidpoolPoolInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolPoolInstanceId_Object=MibTableColumn
cfprUuidpoolPoolInstanceId=_CfprUuidpoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,1),_CfprUuidpoolPoolInstanceId_Type())
cfprUuidpoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolPoolInstanceId.setStatus(_A)
_CfprUuidpoolPoolDn_Type=CfprManagedObjectDn
_CfprUuidpoolPoolDn_Object=MibTableColumn
cfprUuidpoolPoolDn=_CfprUuidpoolPoolDn_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,2),_CfprUuidpoolPoolDn_Type())
cfprUuidpoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolDn.setStatus(_A)
_CfprUuidpoolPoolRn_Type=SnmpAdminString
_CfprUuidpoolPoolRn_Object=MibTableColumn
cfprUuidpoolPoolRn=_CfprUuidpoolPoolRn_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,3),_CfprUuidpoolPoolRn_Type())
cfprUuidpoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolRn.setStatus(_A)
_CfprUuidpoolPoolAssigned_Type=Gauge32
_CfprUuidpoolPoolAssigned_Object=MibTableColumn
cfprUuidpoolPoolAssigned=_CfprUuidpoolPoolAssigned_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,4),_CfprUuidpoolPoolAssigned_Type())
cfprUuidpoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolAssigned.setStatus(_A)
_CfprUuidpoolPoolAssignmentOrder_Type=CfprUuidpoolPoolAssignmentOrder
_CfprUuidpoolPoolAssignmentOrder_Object=MibTableColumn
cfprUuidpoolPoolAssignmentOrder=_CfprUuidpoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,5),_CfprUuidpoolPoolAssignmentOrder_Type())
cfprUuidpoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolAssignmentOrder.setStatus(_A)
_CfprUuidpoolPoolDescr_Type=SnmpAdminString
_CfprUuidpoolPoolDescr_Object=MibTableColumn
cfprUuidpoolPoolDescr=_CfprUuidpoolPoolDescr_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,6),_CfprUuidpoolPoolDescr_Type())
cfprUuidpoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolDescr.setStatus(_A)
_CfprUuidpoolPoolIntId_Type=SnmpAdminString
_CfprUuidpoolPoolIntId_Object=MibTableColumn
cfprUuidpoolPoolIntId=_CfprUuidpoolPoolIntId_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,7),_CfprUuidpoolPoolIntId_Type())
cfprUuidpoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolIntId.setStatus(_A)
_CfprUuidpoolPoolName_Type=SnmpAdminString
_CfprUuidpoolPoolName_Object=MibTableColumn
cfprUuidpoolPoolName=_CfprUuidpoolPoolName_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,8),_CfprUuidpoolPoolName_Type())
cfprUuidpoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolName.setStatus(_A)
_CfprUuidpoolPoolPolicyLevel_Type=Gauge32
_CfprUuidpoolPoolPolicyLevel_Object=MibTableColumn
cfprUuidpoolPoolPolicyLevel=_CfprUuidpoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,9),_CfprUuidpoolPoolPolicyLevel_Type())
cfprUuidpoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolPolicyLevel.setStatus(_A)
_CfprUuidpoolPoolPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprUuidpoolPoolPolicyOwner_Object=MibTableColumn
cfprUuidpoolPoolPolicyOwner=_CfprUuidpoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,10),_CfprUuidpoolPoolPolicyOwner_Type())
cfprUuidpoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolPolicyOwner.setStatus(_A)
_CfprUuidpoolPoolPrefix_Type=Unsigned64
_CfprUuidpoolPoolPrefix_Object=MibTableColumn
cfprUuidpoolPoolPrefix=_CfprUuidpoolPoolPrefix_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,11),_CfprUuidpoolPoolPrefix_Type())
cfprUuidpoolPoolPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolPrefix.setStatus(_A)
_CfprUuidpoolPoolSize_Type=Gauge32
_CfprUuidpoolPoolSize_Object=MibTableColumn
cfprUuidpoolPoolSize=_CfprUuidpoolPoolSize_Object((1,3,6,1,4,1,9,9,826,1,80,4,1,12),_CfprUuidpoolPoolSize_Type())
cfprUuidpoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolSize.setStatus(_A)
_CfprUuidpoolPoolableTable_Object=MibTable
cfprUuidpoolPoolableTable=_CfprUuidpoolPoolableTable_Object((1,3,6,1,4,1,9,9,826,1,80,5))
if mibBuilder.loadTexts:cfprUuidpoolPoolableTable.setStatus(_A)
_CfprUuidpoolPoolableEntry_Object=MibTableRow
cfprUuidpoolPoolableEntry=_CfprUuidpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,826,1,80,5,1))
cfprUuidpoolPoolableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprUuidpoolPoolableEntry.setStatus(_A)
_CfprUuidpoolPoolableInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolPoolableInstanceId_Object=MibTableColumn
cfprUuidpoolPoolableInstanceId=_CfprUuidpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,5,1,1),_CfprUuidpoolPoolableInstanceId_Type())
cfprUuidpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolPoolableInstanceId.setStatus(_A)
_CfprUuidpoolPoolableDn_Type=CfprManagedObjectDn
_CfprUuidpoolPoolableDn_Object=MibTableColumn
cfprUuidpoolPoolableDn=_CfprUuidpoolPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,80,5,1,2),_CfprUuidpoolPoolableDn_Type())
cfprUuidpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolableDn.setStatus(_A)
_CfprUuidpoolPoolableRn_Type=SnmpAdminString
_CfprUuidpoolPoolableRn_Object=MibTableColumn
cfprUuidpoolPoolableRn=_CfprUuidpoolPoolableRn_Object((1,3,6,1,4,1,9,9,826,1,80,5,1,3),_CfprUuidpoolPoolableRn_Type())
cfprUuidpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolableRn.setStatus(_A)
_CfprUuidpoolPoolableId_Type=Unsigned64
_CfprUuidpoolPoolableId_Object=MibTableColumn
cfprUuidpoolPoolableId=_CfprUuidpoolPoolableId_Object((1,3,6,1,4,1,9,9,826,1,80,5,1,4),_CfprUuidpoolPoolableId_Type())
cfprUuidpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolableId.setStatus(_A)
_CfprUuidpoolPoolablePoolDn_Type=SnmpAdminString
_CfprUuidpoolPoolablePoolDn_Object=MibTableColumn
cfprUuidpoolPoolablePoolDn=_CfprUuidpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,826,1,80,5,1,5),_CfprUuidpoolPoolablePoolDn_Type())
cfprUuidpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPoolablePoolDn.setStatus(_A)
_CfprUuidpoolPooledTable_Object=MibTable
cfprUuidpoolPooledTable=_CfprUuidpoolPooledTable_Object((1,3,6,1,4,1,9,9,826,1,80,6))
if mibBuilder.loadTexts:cfprUuidpoolPooledTable.setStatus(_A)
_CfprUuidpoolPooledEntry_Object=MibTableRow
cfprUuidpoolPooledEntry=_CfprUuidpoolPooledEntry_Object((1,3,6,1,4,1,9,9,826,1,80,6,1))
cfprUuidpoolPooledEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprUuidpoolPooledEntry.setStatus(_A)
_CfprUuidpoolPooledInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolPooledInstanceId_Object=MibTableColumn
cfprUuidpoolPooledInstanceId=_CfprUuidpoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,1),_CfprUuidpoolPooledInstanceId_Type())
cfprUuidpoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolPooledInstanceId.setStatus(_A)
_CfprUuidpoolPooledDn_Type=CfprManagedObjectDn
_CfprUuidpoolPooledDn_Object=MibTableColumn
cfprUuidpoolPooledDn=_CfprUuidpoolPooledDn_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,2),_CfprUuidpoolPooledDn_Type())
cfprUuidpoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledDn.setStatus(_A)
_CfprUuidpoolPooledRn_Type=SnmpAdminString
_CfprUuidpoolPooledRn_Object=MibTableColumn
cfprUuidpoolPooledRn=_CfprUuidpoolPooledRn_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,3),_CfprUuidpoolPooledRn_Type())
cfprUuidpoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledRn.setStatus(_A)
_CfprUuidpoolPooledAssigned_Type=TruthValue
_CfprUuidpoolPooledAssigned_Object=MibTableColumn
cfprUuidpoolPooledAssigned=_CfprUuidpoolPooledAssigned_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,4),_CfprUuidpoolPooledAssigned_Type())
cfprUuidpoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledAssigned.setStatus(_A)
_CfprUuidpoolPooledAssignedToDn_Type=SnmpAdminString
_CfprUuidpoolPooledAssignedToDn_Object=MibTableColumn
cfprUuidpoolPooledAssignedToDn=_CfprUuidpoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,5),_CfprUuidpoolPooledAssignedToDn_Type())
cfprUuidpoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledAssignedToDn.setStatus(_A)
_CfprUuidpoolPooledId_Type=Unsigned64
_CfprUuidpoolPooledId_Object=MibTableColumn
cfprUuidpoolPooledId=_CfprUuidpoolPooledId_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,6),_CfprUuidpoolPooledId_Type())
cfprUuidpoolPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledId.setStatus(_A)
_CfprUuidpoolPooledPoolableDn_Type=SnmpAdminString
_CfprUuidpoolPooledPoolableDn_Object=MibTableColumn
cfprUuidpoolPooledPoolableDn=_CfprUuidpoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,7),_CfprUuidpoolPooledPoolableDn_Type())
cfprUuidpoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledPoolableDn.setStatus(_A)
_CfprUuidpoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CfprUuidpoolPooledPrevAssignedToDn_Object=MibTableColumn
cfprUuidpoolPooledPrevAssignedToDn=_CfprUuidpoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,80,6,1,8),_CfprUuidpoolPooledPrevAssignedToDn_Type())
cfprUuidpoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolPooledPrevAssignedToDn.setStatus(_A)
_CfprUuidpoolUniverseTable_Object=MibTable
cfprUuidpoolUniverseTable=_CfprUuidpoolUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,80,7))
if mibBuilder.loadTexts:cfprUuidpoolUniverseTable.setStatus(_A)
_CfprUuidpoolUniverseEntry_Object=MibTableRow
cfprUuidpoolUniverseEntry=_CfprUuidpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,80,7,1))
cfprUuidpoolUniverseEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprUuidpoolUniverseEntry.setStatus(_A)
_CfprUuidpoolUniverseInstanceId_Type=CfprManagedObjectId
_CfprUuidpoolUniverseInstanceId_Object=MibTableColumn
cfprUuidpoolUniverseInstanceId=_CfprUuidpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,80,7,1,1),_CfprUuidpoolUniverseInstanceId_Type())
cfprUuidpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprUuidpoolUniverseInstanceId.setStatus(_A)
_CfprUuidpoolUniverseDn_Type=CfprManagedObjectDn
_CfprUuidpoolUniverseDn_Object=MibTableColumn
cfprUuidpoolUniverseDn=_CfprUuidpoolUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,80,7,1,2),_CfprUuidpoolUniverseDn_Type())
cfprUuidpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolUniverseDn.setStatus(_A)
_CfprUuidpoolUniverseRn_Type=SnmpAdminString
_CfprUuidpoolUniverseRn_Object=MibTableColumn
cfprUuidpoolUniverseRn=_CfprUuidpoolUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,80,7,1,3),_CfprUuidpoolUniverseRn_Type())
cfprUuidpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprUuidpoolUniverseRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprUuidpoolObjects':cfprUuidpoolObjects,'cfprUuidpoolAddrTable':cfprUuidpoolAddrTable,'cfprUuidpoolAddrEntry':cfprUuidpoolAddrEntry,_E:cfprUuidpoolAddrInstanceId,'cfprUuidpoolAddrDn':cfprUuidpoolAddrDn,'cfprUuidpoolAddrRn':cfprUuidpoolAddrRn,'cfprUuidpoolAddrAssigned':cfprUuidpoolAddrAssigned,'cfprUuidpoolAddrAssignedToDn':cfprUuidpoolAddrAssignedToDn,'cfprUuidpoolAddrGlobalAssignedCnt':cfprUuidpoolAddrGlobalAssignedCnt,'cfprUuidpoolAddrGlobalDefinedCnt':cfprUuidpoolAddrGlobalDefinedCnt,'cfprUuidpoolAddrId':cfprUuidpoolAddrId,'cfprUuidpoolAddrOwner':cfprUuidpoolAddrOwner,'cfprUuidpoolBlockTable':cfprUuidpoolBlockTable,'cfprUuidpoolBlockEntry':cfprUuidpoolBlockEntry,_F:cfprUuidpoolBlockInstanceId,'cfprUuidpoolBlockDn':cfprUuidpoolBlockDn,'cfprUuidpoolBlockRn':cfprUuidpoolBlockRn,'cfprUuidpoolBlockFrom':cfprUuidpoolBlockFrom,'cfprUuidpoolBlockTo':cfprUuidpoolBlockTo,'cfprUuidpoolFormatTable':cfprUuidpoolFormatTable,'cfprUuidpoolFormatEntry':cfprUuidpoolFormatEntry,_G:cfprUuidpoolFormatInstanceId,'cfprUuidpoolFormatDn':cfprUuidpoolFormatDn,'cfprUuidpoolFormatRn':cfprUuidpoolFormatRn,'cfprUuidpoolFormatFormat':cfprUuidpoolFormatFormat,'cfprUuidpoolFormatMask':cfprUuidpoolFormatMask,'cfprUuidpoolPoolTable':cfprUuidpoolPoolTable,'cfprUuidpoolPoolEntry':cfprUuidpoolPoolEntry,_H:cfprUuidpoolPoolInstanceId,'cfprUuidpoolPoolDn':cfprUuidpoolPoolDn,'cfprUuidpoolPoolRn':cfprUuidpoolPoolRn,'cfprUuidpoolPoolAssigned':cfprUuidpoolPoolAssigned,'cfprUuidpoolPoolAssignmentOrder':cfprUuidpoolPoolAssignmentOrder,'cfprUuidpoolPoolDescr':cfprUuidpoolPoolDescr,'cfprUuidpoolPoolIntId':cfprUuidpoolPoolIntId,'cfprUuidpoolPoolName':cfprUuidpoolPoolName,'cfprUuidpoolPoolPolicyLevel':cfprUuidpoolPoolPolicyLevel,'cfprUuidpoolPoolPolicyOwner':cfprUuidpoolPoolPolicyOwner,'cfprUuidpoolPoolPrefix':cfprUuidpoolPoolPrefix,'cfprUuidpoolPoolSize':cfprUuidpoolPoolSize,'cfprUuidpoolPoolableTable':cfprUuidpoolPoolableTable,'cfprUuidpoolPoolableEntry':cfprUuidpoolPoolableEntry,_I:cfprUuidpoolPoolableInstanceId,'cfprUuidpoolPoolableDn':cfprUuidpoolPoolableDn,'cfprUuidpoolPoolableRn':cfprUuidpoolPoolableRn,'cfprUuidpoolPoolableId':cfprUuidpoolPoolableId,'cfprUuidpoolPoolablePoolDn':cfprUuidpoolPoolablePoolDn,'cfprUuidpoolPooledTable':cfprUuidpoolPooledTable,'cfprUuidpoolPooledEntry':cfprUuidpoolPooledEntry,_J:cfprUuidpoolPooledInstanceId,'cfprUuidpoolPooledDn':cfprUuidpoolPooledDn,'cfprUuidpoolPooledRn':cfprUuidpoolPooledRn,'cfprUuidpoolPooledAssigned':cfprUuidpoolPooledAssigned,'cfprUuidpoolPooledAssignedToDn':cfprUuidpoolPooledAssignedToDn,'cfprUuidpoolPooledId':cfprUuidpoolPooledId,'cfprUuidpoolPooledPoolableDn':cfprUuidpoolPooledPoolableDn,'cfprUuidpoolPooledPrevAssignedToDn':cfprUuidpoolPooledPrevAssignedToDn,'cfprUuidpoolUniverseTable':cfprUuidpoolUniverseTable,'cfprUuidpoolUniverseEntry':cfprUuidpoolUniverseEntry,_K:cfprUuidpoolUniverseInstanceId,'cfprUuidpoolUniverseDn':cfprUuidpoolUniverseDn,'cfprUuidpoolUniverseRn':cfprUuidpoolUniverseRn})