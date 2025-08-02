_K='cucsMacpoolUniverseInstanceId'
_J='cucsMacpoolPooledInstanceId'
_I='cucsMacpoolPoolableInstanceId'
_H='cucsMacpoolPoolInstanceId'
_G='cucsMacpoolFormatInstanceId'
_F='cucsMacpoolBlockInstanceId'
_E='cucsMacpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-MACPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsAddressMACMask,CucsMacpoolPoolAssignmentOrder,CucsPolicyPolicyOwner,CucsPoolElementOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsAddressMACMask','CucsMacpoolPoolAssignmentOrder','CucsPolicyPolicyOwner','CucsPoolElementOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsMacpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,29))
_CucsMacpoolAddrTable_Object=MibTable
cucsMacpoolAddrTable=_CucsMacpoolAddrTable_Object((1,3,6,1,4,1,9,9,719,1,29,1))
if mibBuilder.loadTexts:cucsMacpoolAddrTable.setStatus(_A)
_CucsMacpoolAddrEntry_Object=MibTableRow
cucsMacpoolAddrEntry=_CucsMacpoolAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,29,1,1))
cucsMacpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsMacpoolAddrEntry.setStatus(_A)
_CucsMacpoolAddrInstanceId_Type=CucsManagedObjectId
_CucsMacpoolAddrInstanceId_Object=MibTableColumn
cucsMacpoolAddrInstanceId=_CucsMacpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,1),_CucsMacpoolAddrInstanceId_Type())
cucsMacpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolAddrInstanceId.setStatus(_A)
_CucsMacpoolAddrDn_Type=CucsManagedObjectDn
_CucsMacpoolAddrDn_Object=MibTableColumn
cucsMacpoolAddrDn=_CucsMacpoolAddrDn_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,2),_CucsMacpoolAddrDn_Type())
cucsMacpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrDn.setStatus(_A)
_CucsMacpoolAddrRn_Type=SnmpAdminString
_CucsMacpoolAddrRn_Object=MibTableColumn
cucsMacpoolAddrRn=_CucsMacpoolAddrRn_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,3),_CucsMacpoolAddrRn_Type())
cucsMacpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrRn.setStatus(_A)
_CucsMacpoolAddrAssigned_Type=TruthValue
_CucsMacpoolAddrAssigned_Object=MibTableColumn
cucsMacpoolAddrAssigned=_CucsMacpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,4),_CucsMacpoolAddrAssigned_Type())
cucsMacpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrAssigned.setStatus(_A)
_CucsMacpoolAddrAssignedToDn_Type=SnmpAdminString
_CucsMacpoolAddrAssignedToDn_Object=MibTableColumn
cucsMacpoolAddrAssignedToDn=_CucsMacpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,5),_CucsMacpoolAddrAssignedToDn_Type())
cucsMacpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrAssignedToDn.setStatus(_A)
_CucsMacpoolAddrId_Type=MacAddress
_CucsMacpoolAddrId_Object=MibTableColumn
cucsMacpoolAddrId=_CucsMacpoolAddrId_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,6),_CucsMacpoolAddrId_Type())
cucsMacpoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrId.setStatus(_A)
_CucsMacpoolAddrOwner_Type=CucsPoolElementOwner
_CucsMacpoolAddrOwner_Object=MibTableColumn
cucsMacpoolAddrOwner=_CucsMacpoolAddrOwner_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,7),_CucsMacpoolAddrOwner_Type())
cucsMacpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrOwner.setStatus(_A)
_CucsMacpoolAddrGlobalAssignedCnt_Type=Gauge32
_CucsMacpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cucsMacpoolAddrGlobalAssignedCnt=_CucsMacpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,8),_CucsMacpoolAddrGlobalAssignedCnt_Type())
cucsMacpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrGlobalAssignedCnt.setStatus(_A)
_CucsMacpoolAddrGlobalDefinedCnt_Type=Gauge32
_CucsMacpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cucsMacpoolAddrGlobalDefinedCnt=_CucsMacpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,719,1,29,1,1,9),_CucsMacpoolAddrGlobalDefinedCnt_Type())
cucsMacpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolAddrGlobalDefinedCnt.setStatus(_A)
_CucsMacpoolBlockTable_Object=MibTable
cucsMacpoolBlockTable=_CucsMacpoolBlockTable_Object((1,3,6,1,4,1,9,9,719,1,29,2))
if mibBuilder.loadTexts:cucsMacpoolBlockTable.setStatus(_A)
_CucsMacpoolBlockEntry_Object=MibTableRow
cucsMacpoolBlockEntry=_CucsMacpoolBlockEntry_Object((1,3,6,1,4,1,9,9,719,1,29,2,1))
cucsMacpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsMacpoolBlockEntry.setStatus(_A)
_CucsMacpoolBlockInstanceId_Type=CucsManagedObjectId
_CucsMacpoolBlockInstanceId_Object=MibTableColumn
cucsMacpoolBlockInstanceId=_CucsMacpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,2,1,1),_CucsMacpoolBlockInstanceId_Type())
cucsMacpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolBlockInstanceId.setStatus(_A)
_CucsMacpoolBlockDn_Type=CucsManagedObjectDn
_CucsMacpoolBlockDn_Object=MibTableColumn
cucsMacpoolBlockDn=_CucsMacpoolBlockDn_Object((1,3,6,1,4,1,9,9,719,1,29,2,1,2),_CucsMacpoolBlockDn_Type())
cucsMacpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolBlockDn.setStatus(_A)
_CucsMacpoolBlockRn_Type=SnmpAdminString
_CucsMacpoolBlockRn_Object=MibTableColumn
cucsMacpoolBlockRn=_CucsMacpoolBlockRn_Object((1,3,6,1,4,1,9,9,719,1,29,2,1,3),_CucsMacpoolBlockRn_Type())
cucsMacpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolBlockRn.setStatus(_A)
_CucsMacpoolBlockFrom_Type=MacAddress
_CucsMacpoolBlockFrom_Object=MibTableColumn
cucsMacpoolBlockFrom=_CucsMacpoolBlockFrom_Object((1,3,6,1,4,1,9,9,719,1,29,2,1,4),_CucsMacpoolBlockFrom_Type())
cucsMacpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolBlockFrom.setStatus(_A)
_CucsMacpoolBlockTo_Type=MacAddress
_CucsMacpoolBlockTo_Object=MibTableColumn
cucsMacpoolBlockTo=_CucsMacpoolBlockTo_Object((1,3,6,1,4,1,9,9,719,1,29,2,1,5),_CucsMacpoolBlockTo_Type())
cucsMacpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolBlockTo.setStatus(_A)
_CucsMacpoolFormatTable_Object=MibTable
cucsMacpoolFormatTable=_CucsMacpoolFormatTable_Object((1,3,6,1,4,1,9,9,719,1,29,3))
if mibBuilder.loadTexts:cucsMacpoolFormatTable.setStatus(_A)
_CucsMacpoolFormatEntry_Object=MibTableRow
cucsMacpoolFormatEntry=_CucsMacpoolFormatEntry_Object((1,3,6,1,4,1,9,9,719,1,29,3,1))
cucsMacpoolFormatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsMacpoolFormatEntry.setStatus(_A)
_CucsMacpoolFormatInstanceId_Type=CucsManagedObjectId
_CucsMacpoolFormatInstanceId_Object=MibTableColumn
cucsMacpoolFormatInstanceId=_CucsMacpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,3,1,1),_CucsMacpoolFormatInstanceId_Type())
cucsMacpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolFormatInstanceId.setStatus(_A)
_CucsMacpoolFormatDn_Type=CucsManagedObjectDn
_CucsMacpoolFormatDn_Object=MibTableColumn
cucsMacpoolFormatDn=_CucsMacpoolFormatDn_Object((1,3,6,1,4,1,9,9,719,1,29,3,1,2),_CucsMacpoolFormatDn_Type())
cucsMacpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolFormatDn.setStatus(_A)
_CucsMacpoolFormatRn_Type=SnmpAdminString
_CucsMacpoolFormatRn_Object=MibTableColumn
cucsMacpoolFormatRn=_CucsMacpoolFormatRn_Object((1,3,6,1,4,1,9,9,719,1,29,3,1,3),_CucsMacpoolFormatRn_Type())
cucsMacpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolFormatRn.setStatus(_A)
_CucsMacpoolFormatFormat_Type=MacAddress
_CucsMacpoolFormatFormat_Object=MibTableColumn
cucsMacpoolFormatFormat=_CucsMacpoolFormatFormat_Object((1,3,6,1,4,1,9,9,719,1,29,3,1,4),_CucsMacpoolFormatFormat_Type())
cucsMacpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolFormatFormat.setStatus(_A)
_CucsMacpoolFormatMask_Type=CucsAddressMACMask
_CucsMacpoolFormatMask_Object=MibTableColumn
cucsMacpoolFormatMask=_CucsMacpoolFormatMask_Object((1,3,6,1,4,1,9,9,719,1,29,3,1,5),_CucsMacpoolFormatMask_Type())
cucsMacpoolFormatMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolFormatMask.setStatus(_A)
_CucsMacpoolPoolTable_Object=MibTable
cucsMacpoolPoolTable=_CucsMacpoolPoolTable_Object((1,3,6,1,4,1,9,9,719,1,29,4))
if mibBuilder.loadTexts:cucsMacpoolPoolTable.setStatus(_A)
_CucsMacpoolPoolEntry_Object=MibTableRow
cucsMacpoolPoolEntry=_CucsMacpoolPoolEntry_Object((1,3,6,1,4,1,9,9,719,1,29,4,1))
cucsMacpoolPoolEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsMacpoolPoolEntry.setStatus(_A)
_CucsMacpoolPoolInstanceId_Type=CucsManagedObjectId
_CucsMacpoolPoolInstanceId_Object=MibTableColumn
cucsMacpoolPoolInstanceId=_CucsMacpoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,1),_CucsMacpoolPoolInstanceId_Type())
cucsMacpoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolPoolInstanceId.setStatus(_A)
_CucsMacpoolPoolDn_Type=CucsManagedObjectDn
_CucsMacpoolPoolDn_Object=MibTableColumn
cucsMacpoolPoolDn=_CucsMacpoolPoolDn_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,2),_CucsMacpoolPoolDn_Type())
cucsMacpoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolDn.setStatus(_A)
_CucsMacpoolPoolRn_Type=SnmpAdminString
_CucsMacpoolPoolRn_Object=MibTableColumn
cucsMacpoolPoolRn=_CucsMacpoolPoolRn_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,3),_CucsMacpoolPoolRn_Type())
cucsMacpoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolRn.setStatus(_A)
_CucsMacpoolPoolAssigned_Type=Gauge32
_CucsMacpoolPoolAssigned_Object=MibTableColumn
cucsMacpoolPoolAssigned=_CucsMacpoolPoolAssigned_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,4),_CucsMacpoolPoolAssigned_Type())
cucsMacpoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolAssigned.setStatus(_A)
_CucsMacpoolPoolDescr_Type=SnmpAdminString
_CucsMacpoolPoolDescr_Object=MibTableColumn
cucsMacpoolPoolDescr=_CucsMacpoolPoolDescr_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,5),_CucsMacpoolPoolDescr_Type())
cucsMacpoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolDescr.setStatus(_A)
_CucsMacpoolPoolIntId_Type=SnmpAdminString
_CucsMacpoolPoolIntId_Object=MibTableColumn
cucsMacpoolPoolIntId=_CucsMacpoolPoolIntId_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,6),_CucsMacpoolPoolIntId_Type())
cucsMacpoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolIntId.setStatus(_A)
_CucsMacpoolPoolName_Type=SnmpAdminString
_CucsMacpoolPoolName_Object=MibTableColumn
cucsMacpoolPoolName=_CucsMacpoolPoolName_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,7),_CucsMacpoolPoolName_Type())
cucsMacpoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolName.setStatus(_A)
_CucsMacpoolPoolSize_Type=Gauge32
_CucsMacpoolPoolSize_Object=MibTableColumn
cucsMacpoolPoolSize=_CucsMacpoolPoolSize_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,8),_CucsMacpoolPoolSize_Type())
cucsMacpoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolSize.setStatus(_A)
_CucsMacpoolPoolAssignmentOrder_Type=CucsMacpoolPoolAssignmentOrder
_CucsMacpoolPoolAssignmentOrder_Object=MibTableColumn
cucsMacpoolPoolAssignmentOrder=_CucsMacpoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,9),_CucsMacpoolPoolAssignmentOrder_Type())
cucsMacpoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolAssignmentOrder.setStatus(_A)
_CucsMacpoolPoolPolicyLevel_Type=Gauge32
_CucsMacpoolPoolPolicyLevel_Object=MibTableColumn
cucsMacpoolPoolPolicyLevel=_CucsMacpoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,10),_CucsMacpoolPoolPolicyLevel_Type())
cucsMacpoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolPolicyLevel.setStatus(_A)
_CucsMacpoolPoolPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsMacpoolPoolPolicyOwner_Object=MibTableColumn
cucsMacpoolPoolPolicyOwner=_CucsMacpoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,29,4,1,11),_CucsMacpoolPoolPolicyOwner_Type())
cucsMacpoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolPolicyOwner.setStatus(_A)
_CucsMacpoolPoolableTable_Object=MibTable
cucsMacpoolPoolableTable=_CucsMacpoolPoolableTable_Object((1,3,6,1,4,1,9,9,719,1,29,5))
if mibBuilder.loadTexts:cucsMacpoolPoolableTable.setStatus(_A)
_CucsMacpoolPoolableEntry_Object=MibTableRow
cucsMacpoolPoolableEntry=_CucsMacpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,719,1,29,5,1))
cucsMacpoolPoolableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsMacpoolPoolableEntry.setStatus(_A)
_CucsMacpoolPoolableInstanceId_Type=CucsManagedObjectId
_CucsMacpoolPoolableInstanceId_Object=MibTableColumn
cucsMacpoolPoolableInstanceId=_CucsMacpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,5,1,1),_CucsMacpoolPoolableInstanceId_Type())
cucsMacpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolPoolableInstanceId.setStatus(_A)
_CucsMacpoolPoolableDn_Type=CucsManagedObjectDn
_CucsMacpoolPoolableDn_Object=MibTableColumn
cucsMacpoolPoolableDn=_CucsMacpoolPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,29,5,1,2),_CucsMacpoolPoolableDn_Type())
cucsMacpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolableDn.setStatus(_A)
_CucsMacpoolPoolableRn_Type=SnmpAdminString
_CucsMacpoolPoolableRn_Object=MibTableColumn
cucsMacpoolPoolableRn=_CucsMacpoolPoolableRn_Object((1,3,6,1,4,1,9,9,719,1,29,5,1,3),_CucsMacpoolPoolableRn_Type())
cucsMacpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolableRn.setStatus(_A)
_CucsMacpoolPoolableId_Type=Unsigned64
_CucsMacpoolPoolableId_Object=MibTableColumn
cucsMacpoolPoolableId=_CucsMacpoolPoolableId_Object((1,3,6,1,4,1,9,9,719,1,29,5,1,4),_CucsMacpoolPoolableId_Type())
cucsMacpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolableId.setStatus(_A)
_CucsMacpoolPoolablePoolDn_Type=SnmpAdminString
_CucsMacpoolPoolablePoolDn_Object=MibTableColumn
cucsMacpoolPoolablePoolDn=_CucsMacpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,719,1,29,5,1,5),_CucsMacpoolPoolablePoolDn_Type())
cucsMacpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPoolablePoolDn.setStatus(_A)
_CucsMacpoolPooledTable_Object=MibTable
cucsMacpoolPooledTable=_CucsMacpoolPooledTable_Object((1,3,6,1,4,1,9,9,719,1,29,6))
if mibBuilder.loadTexts:cucsMacpoolPooledTable.setStatus(_A)
_CucsMacpoolPooledEntry_Object=MibTableRow
cucsMacpoolPooledEntry=_CucsMacpoolPooledEntry_Object((1,3,6,1,4,1,9,9,719,1,29,6,1))
cucsMacpoolPooledEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsMacpoolPooledEntry.setStatus(_A)
_CucsMacpoolPooledInstanceId_Type=CucsManagedObjectId
_CucsMacpoolPooledInstanceId_Object=MibTableColumn
cucsMacpoolPooledInstanceId=_CucsMacpoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,1),_CucsMacpoolPooledInstanceId_Type())
cucsMacpoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolPooledInstanceId.setStatus(_A)
_CucsMacpoolPooledDn_Type=CucsManagedObjectDn
_CucsMacpoolPooledDn_Object=MibTableColumn
cucsMacpoolPooledDn=_CucsMacpoolPooledDn_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,2),_CucsMacpoolPooledDn_Type())
cucsMacpoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledDn.setStatus(_A)
_CucsMacpoolPooledRn_Type=SnmpAdminString
_CucsMacpoolPooledRn_Object=MibTableColumn
cucsMacpoolPooledRn=_CucsMacpoolPooledRn_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,3),_CucsMacpoolPooledRn_Type())
cucsMacpoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledRn.setStatus(_A)
_CucsMacpoolPooledAssigned_Type=TruthValue
_CucsMacpoolPooledAssigned_Object=MibTableColumn
cucsMacpoolPooledAssigned=_CucsMacpoolPooledAssigned_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,4),_CucsMacpoolPooledAssigned_Type())
cucsMacpoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledAssigned.setStatus(_A)
_CucsMacpoolPooledAssignedToDn_Type=SnmpAdminString
_CucsMacpoolPooledAssignedToDn_Object=MibTableColumn
cucsMacpoolPooledAssignedToDn=_CucsMacpoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,5),_CucsMacpoolPooledAssignedToDn_Type())
cucsMacpoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledAssignedToDn.setStatus(_A)
_CucsMacpoolPooledId_Type=MacAddress
_CucsMacpoolPooledId_Object=MibTableColumn
cucsMacpoolPooledId=_CucsMacpoolPooledId_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,6),_CucsMacpoolPooledId_Type())
cucsMacpoolPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledId.setStatus(_A)
_CucsMacpoolPooledPoolableDn_Type=SnmpAdminString
_CucsMacpoolPooledPoolableDn_Object=MibTableColumn
cucsMacpoolPooledPoolableDn=_CucsMacpoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,7),_CucsMacpoolPooledPoolableDn_Type())
cucsMacpoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledPoolableDn.setStatus(_A)
_CucsMacpoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CucsMacpoolPooledPrevAssignedToDn_Object=MibTableColumn
cucsMacpoolPooledPrevAssignedToDn=_CucsMacpoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,29,6,1,8),_CucsMacpoolPooledPrevAssignedToDn_Type())
cucsMacpoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolPooledPrevAssignedToDn.setStatus(_A)
_CucsMacpoolUniverseTable_Object=MibTable
cucsMacpoolUniverseTable=_CucsMacpoolUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,29,7))
if mibBuilder.loadTexts:cucsMacpoolUniverseTable.setStatus(_A)
_CucsMacpoolUniverseEntry_Object=MibTableRow
cucsMacpoolUniverseEntry=_CucsMacpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,29,7,1))
cucsMacpoolUniverseEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsMacpoolUniverseEntry.setStatus(_A)
_CucsMacpoolUniverseInstanceId_Type=CucsManagedObjectId
_CucsMacpoolUniverseInstanceId_Object=MibTableColumn
cucsMacpoolUniverseInstanceId=_CucsMacpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,29,7,1,1),_CucsMacpoolUniverseInstanceId_Type())
cucsMacpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsMacpoolUniverseInstanceId.setStatus(_A)
_CucsMacpoolUniverseDn_Type=CucsManagedObjectDn
_CucsMacpoolUniverseDn_Object=MibTableColumn
cucsMacpoolUniverseDn=_CucsMacpoolUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,29,7,1,2),_CucsMacpoolUniverseDn_Type())
cucsMacpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolUniverseDn.setStatus(_A)
_CucsMacpoolUniverseRn_Type=SnmpAdminString
_CucsMacpoolUniverseRn_Object=MibTableColumn
cucsMacpoolUniverseRn=_CucsMacpoolUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,29,7,1,3),_CucsMacpoolUniverseRn_Type())
cucsMacpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsMacpoolUniverseRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsMacpoolObjects':cucsMacpoolObjects,'cucsMacpoolAddrTable':cucsMacpoolAddrTable,'cucsMacpoolAddrEntry':cucsMacpoolAddrEntry,_E:cucsMacpoolAddrInstanceId,'cucsMacpoolAddrDn':cucsMacpoolAddrDn,'cucsMacpoolAddrRn':cucsMacpoolAddrRn,'cucsMacpoolAddrAssigned':cucsMacpoolAddrAssigned,'cucsMacpoolAddrAssignedToDn':cucsMacpoolAddrAssignedToDn,'cucsMacpoolAddrId':cucsMacpoolAddrId,'cucsMacpoolAddrOwner':cucsMacpoolAddrOwner,'cucsMacpoolAddrGlobalAssignedCnt':cucsMacpoolAddrGlobalAssignedCnt,'cucsMacpoolAddrGlobalDefinedCnt':cucsMacpoolAddrGlobalDefinedCnt,'cucsMacpoolBlockTable':cucsMacpoolBlockTable,'cucsMacpoolBlockEntry':cucsMacpoolBlockEntry,_F:cucsMacpoolBlockInstanceId,'cucsMacpoolBlockDn':cucsMacpoolBlockDn,'cucsMacpoolBlockRn':cucsMacpoolBlockRn,'cucsMacpoolBlockFrom':cucsMacpoolBlockFrom,'cucsMacpoolBlockTo':cucsMacpoolBlockTo,'cucsMacpoolFormatTable':cucsMacpoolFormatTable,'cucsMacpoolFormatEntry':cucsMacpoolFormatEntry,_G:cucsMacpoolFormatInstanceId,'cucsMacpoolFormatDn':cucsMacpoolFormatDn,'cucsMacpoolFormatRn':cucsMacpoolFormatRn,'cucsMacpoolFormatFormat':cucsMacpoolFormatFormat,'cucsMacpoolFormatMask':cucsMacpoolFormatMask,'cucsMacpoolPoolTable':cucsMacpoolPoolTable,'cucsMacpoolPoolEntry':cucsMacpoolPoolEntry,_H:cucsMacpoolPoolInstanceId,'cucsMacpoolPoolDn':cucsMacpoolPoolDn,'cucsMacpoolPoolRn':cucsMacpoolPoolRn,'cucsMacpoolPoolAssigned':cucsMacpoolPoolAssigned,'cucsMacpoolPoolDescr':cucsMacpoolPoolDescr,'cucsMacpoolPoolIntId':cucsMacpoolPoolIntId,'cucsMacpoolPoolName':cucsMacpoolPoolName,'cucsMacpoolPoolSize':cucsMacpoolPoolSize,'cucsMacpoolPoolAssignmentOrder':cucsMacpoolPoolAssignmentOrder,'cucsMacpoolPoolPolicyLevel':cucsMacpoolPoolPolicyLevel,'cucsMacpoolPoolPolicyOwner':cucsMacpoolPoolPolicyOwner,'cucsMacpoolPoolableTable':cucsMacpoolPoolableTable,'cucsMacpoolPoolableEntry':cucsMacpoolPoolableEntry,_I:cucsMacpoolPoolableInstanceId,'cucsMacpoolPoolableDn':cucsMacpoolPoolableDn,'cucsMacpoolPoolableRn':cucsMacpoolPoolableRn,'cucsMacpoolPoolableId':cucsMacpoolPoolableId,'cucsMacpoolPoolablePoolDn':cucsMacpoolPoolablePoolDn,'cucsMacpoolPooledTable':cucsMacpoolPooledTable,'cucsMacpoolPooledEntry':cucsMacpoolPooledEntry,_J:cucsMacpoolPooledInstanceId,'cucsMacpoolPooledDn':cucsMacpoolPooledDn,'cucsMacpoolPooledRn':cucsMacpoolPooledRn,'cucsMacpoolPooledAssigned':cucsMacpoolPooledAssigned,'cucsMacpoolPooledAssignedToDn':cucsMacpoolPooledAssignedToDn,'cucsMacpoolPooledId':cucsMacpoolPooledId,'cucsMacpoolPooledPoolableDn':cucsMacpoolPooledPoolableDn,'cucsMacpoolPooledPrevAssignedToDn':cucsMacpoolPooledPrevAssignedToDn,'cucsMacpoolUniverseTable':cucsMacpoolUniverseTable,'cucsMacpoolUniverseEntry':cucsMacpoolUniverseEntry,_K:cucsMacpoolUniverseInstanceId,'cucsMacpoolUniverseDn':cucsMacpoolUniverseDn,'cucsMacpoolUniverseRn':cucsMacpoolUniverseRn})