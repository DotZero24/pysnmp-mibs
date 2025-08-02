_K='cfprMacpoolUniverseInstanceId'
_J='cfprMacpoolPooledInstanceId'
_I='cfprMacpoolPoolableInstanceId'
_H='cfprMacpoolPoolInstanceId'
_G='cfprMacpoolFormatInstanceId'
_F='cfprMacpoolBlockInstanceId'
_E='cfprMacpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-MACPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprAddressMACMask,CfprMacpoolPoolAssignmentOrder,CfprPolicyPolicyOwner,CfprPoolElementOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprAddressMACMask','CfprMacpoolPoolAssignmentOrder','CfprPolicyPolicyOwner','CfprPoolElementOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprMacpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,49))
_CfprMacpoolAddrTable_Object=MibTable
cfprMacpoolAddrTable=_CfprMacpoolAddrTable_Object((1,3,6,1,4,1,9,9,826,1,49,1))
if mibBuilder.loadTexts:cfprMacpoolAddrTable.setStatus(_A)
_CfprMacpoolAddrEntry_Object=MibTableRow
cfprMacpoolAddrEntry=_CfprMacpoolAddrEntry_Object((1,3,6,1,4,1,9,9,826,1,49,1,1))
cfprMacpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprMacpoolAddrEntry.setStatus(_A)
_CfprMacpoolAddrInstanceId_Type=CfprManagedObjectId
_CfprMacpoolAddrInstanceId_Object=MibTableColumn
cfprMacpoolAddrInstanceId=_CfprMacpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,1),_CfprMacpoolAddrInstanceId_Type())
cfprMacpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolAddrInstanceId.setStatus(_A)
_CfprMacpoolAddrDn_Type=CfprManagedObjectDn
_CfprMacpoolAddrDn_Object=MibTableColumn
cfprMacpoolAddrDn=_CfprMacpoolAddrDn_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,2),_CfprMacpoolAddrDn_Type())
cfprMacpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrDn.setStatus(_A)
_CfprMacpoolAddrRn_Type=SnmpAdminString
_CfprMacpoolAddrRn_Object=MibTableColumn
cfprMacpoolAddrRn=_CfprMacpoolAddrRn_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,3),_CfprMacpoolAddrRn_Type())
cfprMacpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrRn.setStatus(_A)
_CfprMacpoolAddrAssigned_Type=TruthValue
_CfprMacpoolAddrAssigned_Object=MibTableColumn
cfprMacpoolAddrAssigned=_CfprMacpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,4),_CfprMacpoolAddrAssigned_Type())
cfprMacpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrAssigned.setStatus(_A)
_CfprMacpoolAddrAssignedToDn_Type=SnmpAdminString
_CfprMacpoolAddrAssignedToDn_Object=MibTableColumn
cfprMacpoolAddrAssignedToDn=_CfprMacpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,5),_CfprMacpoolAddrAssignedToDn_Type())
cfprMacpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrAssignedToDn.setStatus(_A)
_CfprMacpoolAddrGlobalAssignedCnt_Type=Gauge32
_CfprMacpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cfprMacpoolAddrGlobalAssignedCnt=_CfprMacpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,6),_CfprMacpoolAddrGlobalAssignedCnt_Type())
cfprMacpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrGlobalAssignedCnt.setStatus(_A)
_CfprMacpoolAddrGlobalDefinedCnt_Type=Gauge32
_CfprMacpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cfprMacpoolAddrGlobalDefinedCnt=_CfprMacpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,7),_CfprMacpoolAddrGlobalDefinedCnt_Type())
cfprMacpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrGlobalDefinedCnt.setStatus(_A)
_CfprMacpoolAddrId_Type=MacAddress
_CfprMacpoolAddrId_Object=MibTableColumn
cfprMacpoolAddrId=_CfprMacpoolAddrId_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,8),_CfprMacpoolAddrId_Type())
cfprMacpoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrId.setStatus(_A)
_CfprMacpoolAddrOwner_Type=CfprPoolElementOwner
_CfprMacpoolAddrOwner_Object=MibTableColumn
cfprMacpoolAddrOwner=_CfprMacpoolAddrOwner_Object((1,3,6,1,4,1,9,9,826,1,49,1,1,9),_CfprMacpoolAddrOwner_Type())
cfprMacpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolAddrOwner.setStatus(_A)
_CfprMacpoolBlockTable_Object=MibTable
cfprMacpoolBlockTable=_CfprMacpoolBlockTable_Object((1,3,6,1,4,1,9,9,826,1,49,2))
if mibBuilder.loadTexts:cfprMacpoolBlockTable.setStatus(_A)
_CfprMacpoolBlockEntry_Object=MibTableRow
cfprMacpoolBlockEntry=_CfprMacpoolBlockEntry_Object((1,3,6,1,4,1,9,9,826,1,49,2,1))
cfprMacpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprMacpoolBlockEntry.setStatus(_A)
_CfprMacpoolBlockInstanceId_Type=CfprManagedObjectId
_CfprMacpoolBlockInstanceId_Object=MibTableColumn
cfprMacpoolBlockInstanceId=_CfprMacpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,2,1,1),_CfprMacpoolBlockInstanceId_Type())
cfprMacpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolBlockInstanceId.setStatus(_A)
_CfprMacpoolBlockDn_Type=CfprManagedObjectDn
_CfprMacpoolBlockDn_Object=MibTableColumn
cfprMacpoolBlockDn=_CfprMacpoolBlockDn_Object((1,3,6,1,4,1,9,9,826,1,49,2,1,2),_CfprMacpoolBlockDn_Type())
cfprMacpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolBlockDn.setStatus(_A)
_CfprMacpoolBlockRn_Type=SnmpAdminString
_CfprMacpoolBlockRn_Object=MibTableColumn
cfprMacpoolBlockRn=_CfprMacpoolBlockRn_Object((1,3,6,1,4,1,9,9,826,1,49,2,1,3),_CfprMacpoolBlockRn_Type())
cfprMacpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolBlockRn.setStatus(_A)
_CfprMacpoolBlockFrom_Type=MacAddress
_CfprMacpoolBlockFrom_Object=MibTableColumn
cfprMacpoolBlockFrom=_CfprMacpoolBlockFrom_Object((1,3,6,1,4,1,9,9,826,1,49,2,1,4),_CfprMacpoolBlockFrom_Type())
cfprMacpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolBlockFrom.setStatus(_A)
_CfprMacpoolBlockTo_Type=MacAddress
_CfprMacpoolBlockTo_Object=MibTableColumn
cfprMacpoolBlockTo=_CfprMacpoolBlockTo_Object((1,3,6,1,4,1,9,9,826,1,49,2,1,5),_CfprMacpoolBlockTo_Type())
cfprMacpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolBlockTo.setStatus(_A)
_CfprMacpoolFormatTable_Object=MibTable
cfprMacpoolFormatTable=_CfprMacpoolFormatTable_Object((1,3,6,1,4,1,9,9,826,1,49,3))
if mibBuilder.loadTexts:cfprMacpoolFormatTable.setStatus(_A)
_CfprMacpoolFormatEntry_Object=MibTableRow
cfprMacpoolFormatEntry=_CfprMacpoolFormatEntry_Object((1,3,6,1,4,1,9,9,826,1,49,3,1))
cfprMacpoolFormatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprMacpoolFormatEntry.setStatus(_A)
_CfprMacpoolFormatInstanceId_Type=CfprManagedObjectId
_CfprMacpoolFormatInstanceId_Object=MibTableColumn
cfprMacpoolFormatInstanceId=_CfprMacpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,3,1,1),_CfprMacpoolFormatInstanceId_Type())
cfprMacpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolFormatInstanceId.setStatus(_A)
_CfprMacpoolFormatDn_Type=CfprManagedObjectDn
_CfprMacpoolFormatDn_Object=MibTableColumn
cfprMacpoolFormatDn=_CfprMacpoolFormatDn_Object((1,3,6,1,4,1,9,9,826,1,49,3,1,2),_CfprMacpoolFormatDn_Type())
cfprMacpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolFormatDn.setStatus(_A)
_CfprMacpoolFormatRn_Type=SnmpAdminString
_CfprMacpoolFormatRn_Object=MibTableColumn
cfprMacpoolFormatRn=_CfprMacpoolFormatRn_Object((1,3,6,1,4,1,9,9,826,1,49,3,1,3),_CfprMacpoolFormatRn_Type())
cfprMacpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolFormatRn.setStatus(_A)
_CfprMacpoolFormatFormat_Type=MacAddress
_CfprMacpoolFormatFormat_Object=MibTableColumn
cfprMacpoolFormatFormat=_CfprMacpoolFormatFormat_Object((1,3,6,1,4,1,9,9,826,1,49,3,1,4),_CfprMacpoolFormatFormat_Type())
cfprMacpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolFormatFormat.setStatus(_A)
_CfprMacpoolFormatMask_Type=CfprAddressMACMask
_CfprMacpoolFormatMask_Object=MibTableColumn
cfprMacpoolFormatMask=_CfprMacpoolFormatMask_Object((1,3,6,1,4,1,9,9,826,1,49,3,1,5),_CfprMacpoolFormatMask_Type())
cfprMacpoolFormatMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolFormatMask.setStatus(_A)
_CfprMacpoolPoolTable_Object=MibTable
cfprMacpoolPoolTable=_CfprMacpoolPoolTable_Object((1,3,6,1,4,1,9,9,826,1,49,4))
if mibBuilder.loadTexts:cfprMacpoolPoolTable.setStatus(_A)
_CfprMacpoolPoolEntry_Object=MibTableRow
cfprMacpoolPoolEntry=_CfprMacpoolPoolEntry_Object((1,3,6,1,4,1,9,9,826,1,49,4,1))
cfprMacpoolPoolEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprMacpoolPoolEntry.setStatus(_A)
_CfprMacpoolPoolInstanceId_Type=CfprManagedObjectId
_CfprMacpoolPoolInstanceId_Object=MibTableColumn
cfprMacpoolPoolInstanceId=_CfprMacpoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,1),_CfprMacpoolPoolInstanceId_Type())
cfprMacpoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolPoolInstanceId.setStatus(_A)
_CfprMacpoolPoolDn_Type=CfprManagedObjectDn
_CfprMacpoolPoolDn_Object=MibTableColumn
cfprMacpoolPoolDn=_CfprMacpoolPoolDn_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,2),_CfprMacpoolPoolDn_Type())
cfprMacpoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolDn.setStatus(_A)
_CfprMacpoolPoolRn_Type=SnmpAdminString
_CfprMacpoolPoolRn_Object=MibTableColumn
cfprMacpoolPoolRn=_CfprMacpoolPoolRn_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,3),_CfprMacpoolPoolRn_Type())
cfprMacpoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolRn.setStatus(_A)
_CfprMacpoolPoolAssigned_Type=Gauge32
_CfprMacpoolPoolAssigned_Object=MibTableColumn
cfprMacpoolPoolAssigned=_CfprMacpoolPoolAssigned_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,4),_CfprMacpoolPoolAssigned_Type())
cfprMacpoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolAssigned.setStatus(_A)
_CfprMacpoolPoolAssignmentOrder_Type=CfprMacpoolPoolAssignmentOrder
_CfprMacpoolPoolAssignmentOrder_Object=MibTableColumn
cfprMacpoolPoolAssignmentOrder=_CfprMacpoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,5),_CfprMacpoolPoolAssignmentOrder_Type())
cfprMacpoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolAssignmentOrder.setStatus(_A)
_CfprMacpoolPoolDescr_Type=SnmpAdminString
_CfprMacpoolPoolDescr_Object=MibTableColumn
cfprMacpoolPoolDescr=_CfprMacpoolPoolDescr_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,6),_CfprMacpoolPoolDescr_Type())
cfprMacpoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolDescr.setStatus(_A)
_CfprMacpoolPoolIntId_Type=SnmpAdminString
_CfprMacpoolPoolIntId_Object=MibTableColumn
cfprMacpoolPoolIntId=_CfprMacpoolPoolIntId_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,7),_CfprMacpoolPoolIntId_Type())
cfprMacpoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolIntId.setStatus(_A)
_CfprMacpoolPoolName_Type=SnmpAdminString
_CfprMacpoolPoolName_Object=MibTableColumn
cfprMacpoolPoolName=_CfprMacpoolPoolName_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,8),_CfprMacpoolPoolName_Type())
cfprMacpoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolName.setStatus(_A)
_CfprMacpoolPoolPolicyLevel_Type=Gauge32
_CfprMacpoolPoolPolicyLevel_Object=MibTableColumn
cfprMacpoolPoolPolicyLevel=_CfprMacpoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,9),_CfprMacpoolPoolPolicyLevel_Type())
cfprMacpoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolPolicyLevel.setStatus(_A)
_CfprMacpoolPoolPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprMacpoolPoolPolicyOwner_Object=MibTableColumn
cfprMacpoolPoolPolicyOwner=_CfprMacpoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,10),_CfprMacpoolPoolPolicyOwner_Type())
cfprMacpoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolPolicyOwner.setStatus(_A)
_CfprMacpoolPoolSize_Type=Gauge32
_CfprMacpoolPoolSize_Object=MibTableColumn
cfprMacpoolPoolSize=_CfprMacpoolPoolSize_Object((1,3,6,1,4,1,9,9,826,1,49,4,1,11),_CfprMacpoolPoolSize_Type())
cfprMacpoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolSize.setStatus(_A)
_CfprMacpoolPoolableTable_Object=MibTable
cfprMacpoolPoolableTable=_CfprMacpoolPoolableTable_Object((1,3,6,1,4,1,9,9,826,1,49,5))
if mibBuilder.loadTexts:cfprMacpoolPoolableTable.setStatus(_A)
_CfprMacpoolPoolableEntry_Object=MibTableRow
cfprMacpoolPoolableEntry=_CfprMacpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,826,1,49,5,1))
cfprMacpoolPoolableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprMacpoolPoolableEntry.setStatus(_A)
_CfprMacpoolPoolableInstanceId_Type=CfprManagedObjectId
_CfprMacpoolPoolableInstanceId_Object=MibTableColumn
cfprMacpoolPoolableInstanceId=_CfprMacpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,5,1,1),_CfprMacpoolPoolableInstanceId_Type())
cfprMacpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolPoolableInstanceId.setStatus(_A)
_CfprMacpoolPoolableDn_Type=CfprManagedObjectDn
_CfprMacpoolPoolableDn_Object=MibTableColumn
cfprMacpoolPoolableDn=_CfprMacpoolPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,49,5,1,2),_CfprMacpoolPoolableDn_Type())
cfprMacpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolableDn.setStatus(_A)
_CfprMacpoolPoolableRn_Type=SnmpAdminString
_CfprMacpoolPoolableRn_Object=MibTableColumn
cfprMacpoolPoolableRn=_CfprMacpoolPoolableRn_Object((1,3,6,1,4,1,9,9,826,1,49,5,1,3),_CfprMacpoolPoolableRn_Type())
cfprMacpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolableRn.setStatus(_A)
_CfprMacpoolPoolableId_Type=Unsigned64
_CfprMacpoolPoolableId_Object=MibTableColumn
cfprMacpoolPoolableId=_CfprMacpoolPoolableId_Object((1,3,6,1,4,1,9,9,826,1,49,5,1,4),_CfprMacpoolPoolableId_Type())
cfprMacpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolableId.setStatus(_A)
_CfprMacpoolPoolablePoolDn_Type=SnmpAdminString
_CfprMacpoolPoolablePoolDn_Object=MibTableColumn
cfprMacpoolPoolablePoolDn=_CfprMacpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,826,1,49,5,1,5),_CfprMacpoolPoolablePoolDn_Type())
cfprMacpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPoolablePoolDn.setStatus(_A)
_CfprMacpoolPooledTable_Object=MibTable
cfprMacpoolPooledTable=_CfprMacpoolPooledTable_Object((1,3,6,1,4,1,9,9,826,1,49,6))
if mibBuilder.loadTexts:cfprMacpoolPooledTable.setStatus(_A)
_CfprMacpoolPooledEntry_Object=MibTableRow
cfprMacpoolPooledEntry=_CfprMacpoolPooledEntry_Object((1,3,6,1,4,1,9,9,826,1,49,6,1))
cfprMacpoolPooledEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprMacpoolPooledEntry.setStatus(_A)
_CfprMacpoolPooledInstanceId_Type=CfprManagedObjectId
_CfprMacpoolPooledInstanceId_Object=MibTableColumn
cfprMacpoolPooledInstanceId=_CfprMacpoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,1),_CfprMacpoolPooledInstanceId_Type())
cfprMacpoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolPooledInstanceId.setStatus(_A)
_CfprMacpoolPooledDn_Type=CfprManagedObjectDn
_CfprMacpoolPooledDn_Object=MibTableColumn
cfprMacpoolPooledDn=_CfprMacpoolPooledDn_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,2),_CfprMacpoolPooledDn_Type())
cfprMacpoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledDn.setStatus(_A)
_CfprMacpoolPooledRn_Type=SnmpAdminString
_CfprMacpoolPooledRn_Object=MibTableColumn
cfprMacpoolPooledRn=_CfprMacpoolPooledRn_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,3),_CfprMacpoolPooledRn_Type())
cfprMacpoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledRn.setStatus(_A)
_CfprMacpoolPooledAssigned_Type=TruthValue
_CfprMacpoolPooledAssigned_Object=MibTableColumn
cfprMacpoolPooledAssigned=_CfprMacpoolPooledAssigned_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,4),_CfprMacpoolPooledAssigned_Type())
cfprMacpoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledAssigned.setStatus(_A)
_CfprMacpoolPooledAssignedToDn_Type=SnmpAdminString
_CfprMacpoolPooledAssignedToDn_Object=MibTableColumn
cfprMacpoolPooledAssignedToDn=_CfprMacpoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,5),_CfprMacpoolPooledAssignedToDn_Type())
cfprMacpoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledAssignedToDn.setStatus(_A)
_CfprMacpoolPooledId_Type=MacAddress
_CfprMacpoolPooledId_Object=MibTableColumn
cfprMacpoolPooledId=_CfprMacpoolPooledId_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,6),_CfprMacpoolPooledId_Type())
cfprMacpoolPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledId.setStatus(_A)
_CfprMacpoolPooledPoolableDn_Type=SnmpAdminString
_CfprMacpoolPooledPoolableDn_Object=MibTableColumn
cfprMacpoolPooledPoolableDn=_CfprMacpoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,7),_CfprMacpoolPooledPoolableDn_Type())
cfprMacpoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledPoolableDn.setStatus(_A)
_CfprMacpoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CfprMacpoolPooledPrevAssignedToDn_Object=MibTableColumn
cfprMacpoolPooledPrevAssignedToDn=_CfprMacpoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,826,1,49,6,1,8),_CfprMacpoolPooledPrevAssignedToDn_Type())
cfprMacpoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolPooledPrevAssignedToDn.setStatus(_A)
_CfprMacpoolUniverseTable_Object=MibTable
cfprMacpoolUniverseTable=_CfprMacpoolUniverseTable_Object((1,3,6,1,4,1,9,9,826,1,49,7))
if mibBuilder.loadTexts:cfprMacpoolUniverseTable.setStatus(_A)
_CfprMacpoolUniverseEntry_Object=MibTableRow
cfprMacpoolUniverseEntry=_CfprMacpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,826,1,49,7,1))
cfprMacpoolUniverseEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprMacpoolUniverseEntry.setStatus(_A)
_CfprMacpoolUniverseInstanceId_Type=CfprManagedObjectId
_CfprMacpoolUniverseInstanceId_Object=MibTableColumn
cfprMacpoolUniverseInstanceId=_CfprMacpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,826,1,49,7,1,1),_CfprMacpoolUniverseInstanceId_Type())
cfprMacpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprMacpoolUniverseInstanceId.setStatus(_A)
_CfprMacpoolUniverseDn_Type=CfprManagedObjectDn
_CfprMacpoolUniverseDn_Object=MibTableColumn
cfprMacpoolUniverseDn=_CfprMacpoolUniverseDn_Object((1,3,6,1,4,1,9,9,826,1,49,7,1,2),_CfprMacpoolUniverseDn_Type())
cfprMacpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolUniverseDn.setStatus(_A)
_CfprMacpoolUniverseRn_Type=SnmpAdminString
_CfprMacpoolUniverseRn_Object=MibTableColumn
cfprMacpoolUniverseRn=_CfprMacpoolUniverseRn_Object((1,3,6,1,4,1,9,9,826,1,49,7,1,3),_CfprMacpoolUniverseRn_Type())
cfprMacpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprMacpoolUniverseRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprMacpoolObjects':cfprMacpoolObjects,'cfprMacpoolAddrTable':cfprMacpoolAddrTable,'cfprMacpoolAddrEntry':cfprMacpoolAddrEntry,_E:cfprMacpoolAddrInstanceId,'cfprMacpoolAddrDn':cfprMacpoolAddrDn,'cfprMacpoolAddrRn':cfprMacpoolAddrRn,'cfprMacpoolAddrAssigned':cfprMacpoolAddrAssigned,'cfprMacpoolAddrAssignedToDn':cfprMacpoolAddrAssignedToDn,'cfprMacpoolAddrGlobalAssignedCnt':cfprMacpoolAddrGlobalAssignedCnt,'cfprMacpoolAddrGlobalDefinedCnt':cfprMacpoolAddrGlobalDefinedCnt,'cfprMacpoolAddrId':cfprMacpoolAddrId,'cfprMacpoolAddrOwner':cfprMacpoolAddrOwner,'cfprMacpoolBlockTable':cfprMacpoolBlockTable,'cfprMacpoolBlockEntry':cfprMacpoolBlockEntry,_F:cfprMacpoolBlockInstanceId,'cfprMacpoolBlockDn':cfprMacpoolBlockDn,'cfprMacpoolBlockRn':cfprMacpoolBlockRn,'cfprMacpoolBlockFrom':cfprMacpoolBlockFrom,'cfprMacpoolBlockTo':cfprMacpoolBlockTo,'cfprMacpoolFormatTable':cfprMacpoolFormatTable,'cfprMacpoolFormatEntry':cfprMacpoolFormatEntry,_G:cfprMacpoolFormatInstanceId,'cfprMacpoolFormatDn':cfprMacpoolFormatDn,'cfprMacpoolFormatRn':cfprMacpoolFormatRn,'cfprMacpoolFormatFormat':cfprMacpoolFormatFormat,'cfprMacpoolFormatMask':cfprMacpoolFormatMask,'cfprMacpoolPoolTable':cfprMacpoolPoolTable,'cfprMacpoolPoolEntry':cfprMacpoolPoolEntry,_H:cfprMacpoolPoolInstanceId,'cfprMacpoolPoolDn':cfprMacpoolPoolDn,'cfprMacpoolPoolRn':cfprMacpoolPoolRn,'cfprMacpoolPoolAssigned':cfprMacpoolPoolAssigned,'cfprMacpoolPoolAssignmentOrder':cfprMacpoolPoolAssignmentOrder,'cfprMacpoolPoolDescr':cfprMacpoolPoolDescr,'cfprMacpoolPoolIntId':cfprMacpoolPoolIntId,'cfprMacpoolPoolName':cfprMacpoolPoolName,'cfprMacpoolPoolPolicyLevel':cfprMacpoolPoolPolicyLevel,'cfprMacpoolPoolPolicyOwner':cfprMacpoolPoolPolicyOwner,'cfprMacpoolPoolSize':cfprMacpoolPoolSize,'cfprMacpoolPoolableTable':cfprMacpoolPoolableTable,'cfprMacpoolPoolableEntry':cfprMacpoolPoolableEntry,_I:cfprMacpoolPoolableInstanceId,'cfprMacpoolPoolableDn':cfprMacpoolPoolableDn,'cfprMacpoolPoolableRn':cfprMacpoolPoolableRn,'cfprMacpoolPoolableId':cfprMacpoolPoolableId,'cfprMacpoolPoolablePoolDn':cfprMacpoolPoolablePoolDn,'cfprMacpoolPooledTable':cfprMacpoolPooledTable,'cfprMacpoolPooledEntry':cfprMacpoolPooledEntry,_J:cfprMacpoolPooledInstanceId,'cfprMacpoolPooledDn':cfprMacpoolPooledDn,'cfprMacpoolPooledRn':cfprMacpoolPooledRn,'cfprMacpoolPooledAssigned':cfprMacpoolPooledAssigned,'cfprMacpoolPooledAssignedToDn':cfprMacpoolPooledAssignedToDn,'cfprMacpoolPooledId':cfprMacpoolPooledId,'cfprMacpoolPooledPoolableDn':cfprMacpoolPooledPoolableDn,'cfprMacpoolPooledPrevAssignedToDn':cfprMacpoolPooledPrevAssignedToDn,'cfprMacpoolUniverseTable':cfprMacpoolUniverseTable,'cfprMacpoolUniverseEntry':cfprMacpoolUniverseEntry,_K:cfprMacpoolUniverseInstanceId,'cfprMacpoolUniverseDn':cfprMacpoolUniverseDn,'cfprMacpoolUniverseRn':cfprMacpoolUniverseRn})