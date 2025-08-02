_K='cucsUuidpoolUniverseInstanceId'
_J='cucsUuidpoolPooledInstanceId'
_I='cucsUuidpoolPoolableInstanceId'
_H='cucsUuidpoolPoolInstanceId'
_G='cucsUuidpoolFormatInstanceId'
_F='cucsUuidpoolBlockInstanceId'
_E='cucsUuidpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-UUIDPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsAddressUIDSuffxMask,CucsPolicyPolicyOwner,CucsPoolElementOwner,CucsUuidpoolPoolAssignmentOrder=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsAddressUIDSuffxMask','CucsPolicyPolicyOwner','CucsPoolElementOwner','CucsUuidpoolPoolAssignmentOrder')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsUuidpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,51))
_CucsUuidpoolAddrTable_Object=MibTable
cucsUuidpoolAddrTable=_CucsUuidpoolAddrTable_Object((1,3,6,1,4,1,9,9,719,1,51,1))
if mibBuilder.loadTexts:cucsUuidpoolAddrTable.setStatus(_A)
_CucsUuidpoolAddrEntry_Object=MibTableRow
cucsUuidpoolAddrEntry=_CucsUuidpoolAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,51,1,1))
cucsUuidpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsUuidpoolAddrEntry.setStatus(_A)
_CucsUuidpoolAddrInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolAddrInstanceId_Object=MibTableColumn
cucsUuidpoolAddrInstanceId=_CucsUuidpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,1),_CucsUuidpoolAddrInstanceId_Type())
cucsUuidpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolAddrInstanceId.setStatus(_A)
_CucsUuidpoolAddrDn_Type=CucsManagedObjectDn
_CucsUuidpoolAddrDn_Object=MibTableColumn
cucsUuidpoolAddrDn=_CucsUuidpoolAddrDn_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,2),_CucsUuidpoolAddrDn_Type())
cucsUuidpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrDn.setStatus(_A)
_CucsUuidpoolAddrRn_Type=SnmpAdminString
_CucsUuidpoolAddrRn_Object=MibTableColumn
cucsUuidpoolAddrRn=_CucsUuidpoolAddrRn_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,3),_CucsUuidpoolAddrRn_Type())
cucsUuidpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrRn.setStatus(_A)
_CucsUuidpoolAddrAssigned_Type=TruthValue
_CucsUuidpoolAddrAssigned_Object=MibTableColumn
cucsUuidpoolAddrAssigned=_CucsUuidpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,4),_CucsUuidpoolAddrAssigned_Type())
cucsUuidpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrAssigned.setStatus(_A)
_CucsUuidpoolAddrAssignedToDn_Type=SnmpAdminString
_CucsUuidpoolAddrAssignedToDn_Object=MibTableColumn
cucsUuidpoolAddrAssignedToDn=_CucsUuidpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,5),_CucsUuidpoolAddrAssignedToDn_Type())
cucsUuidpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrAssignedToDn.setStatus(_A)
_CucsUuidpoolAddrId_Type=SnmpAdminString
_CucsUuidpoolAddrId_Object=MibTableColumn
cucsUuidpoolAddrId=_CucsUuidpoolAddrId_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,6),_CucsUuidpoolAddrId_Type())
cucsUuidpoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrId.setStatus(_A)
_CucsUuidpoolAddrOwner_Type=CucsPoolElementOwner
_CucsUuidpoolAddrOwner_Object=MibTableColumn
cucsUuidpoolAddrOwner=_CucsUuidpoolAddrOwner_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,7),_CucsUuidpoolAddrOwner_Type())
cucsUuidpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrOwner.setStatus(_A)
_CucsUuidpoolAddrGlobalAssignedCnt_Type=Gauge32
_CucsUuidpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cucsUuidpoolAddrGlobalAssignedCnt=_CucsUuidpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,8),_CucsUuidpoolAddrGlobalAssignedCnt_Type())
cucsUuidpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrGlobalAssignedCnt.setStatus(_A)
_CucsUuidpoolAddrGlobalDefinedCnt_Type=Gauge32
_CucsUuidpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cucsUuidpoolAddrGlobalDefinedCnt=_CucsUuidpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,719,1,51,1,1,9),_CucsUuidpoolAddrGlobalDefinedCnt_Type())
cucsUuidpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolAddrGlobalDefinedCnt.setStatus(_A)
_CucsUuidpoolBlockTable_Object=MibTable
cucsUuidpoolBlockTable=_CucsUuidpoolBlockTable_Object((1,3,6,1,4,1,9,9,719,1,51,2))
if mibBuilder.loadTexts:cucsUuidpoolBlockTable.setStatus(_A)
_CucsUuidpoolBlockEntry_Object=MibTableRow
cucsUuidpoolBlockEntry=_CucsUuidpoolBlockEntry_Object((1,3,6,1,4,1,9,9,719,1,51,2,1))
cucsUuidpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsUuidpoolBlockEntry.setStatus(_A)
_CucsUuidpoolBlockInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolBlockInstanceId_Object=MibTableColumn
cucsUuidpoolBlockInstanceId=_CucsUuidpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,2,1,1),_CucsUuidpoolBlockInstanceId_Type())
cucsUuidpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolBlockInstanceId.setStatus(_A)
_CucsUuidpoolBlockDn_Type=CucsManagedObjectDn
_CucsUuidpoolBlockDn_Object=MibTableColumn
cucsUuidpoolBlockDn=_CucsUuidpoolBlockDn_Object((1,3,6,1,4,1,9,9,719,1,51,2,1,2),_CucsUuidpoolBlockDn_Type())
cucsUuidpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolBlockDn.setStatus(_A)
_CucsUuidpoolBlockRn_Type=SnmpAdminString
_CucsUuidpoolBlockRn_Object=MibTableColumn
cucsUuidpoolBlockRn=_CucsUuidpoolBlockRn_Object((1,3,6,1,4,1,9,9,719,1,51,2,1,3),_CucsUuidpoolBlockRn_Type())
cucsUuidpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolBlockRn.setStatus(_A)
_CucsUuidpoolBlockFrom_Type=Unsigned64
_CucsUuidpoolBlockFrom_Object=MibTableColumn
cucsUuidpoolBlockFrom=_CucsUuidpoolBlockFrom_Object((1,3,6,1,4,1,9,9,719,1,51,2,1,4),_CucsUuidpoolBlockFrom_Type())
cucsUuidpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolBlockFrom.setStatus(_A)
_CucsUuidpoolBlockTo_Type=Unsigned64
_CucsUuidpoolBlockTo_Object=MibTableColumn
cucsUuidpoolBlockTo=_CucsUuidpoolBlockTo_Object((1,3,6,1,4,1,9,9,719,1,51,2,1,5),_CucsUuidpoolBlockTo_Type())
cucsUuidpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolBlockTo.setStatus(_A)
_CucsUuidpoolFormatTable_Object=MibTable
cucsUuidpoolFormatTable=_CucsUuidpoolFormatTable_Object((1,3,6,1,4,1,9,9,719,1,51,3))
if mibBuilder.loadTexts:cucsUuidpoolFormatTable.setStatus(_A)
_CucsUuidpoolFormatEntry_Object=MibTableRow
cucsUuidpoolFormatEntry=_CucsUuidpoolFormatEntry_Object((1,3,6,1,4,1,9,9,719,1,51,3,1))
cucsUuidpoolFormatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsUuidpoolFormatEntry.setStatus(_A)
_CucsUuidpoolFormatInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolFormatInstanceId_Object=MibTableColumn
cucsUuidpoolFormatInstanceId=_CucsUuidpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,3,1,1),_CucsUuidpoolFormatInstanceId_Type())
cucsUuidpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolFormatInstanceId.setStatus(_A)
_CucsUuidpoolFormatDn_Type=CucsManagedObjectDn
_CucsUuidpoolFormatDn_Object=MibTableColumn
cucsUuidpoolFormatDn=_CucsUuidpoolFormatDn_Object((1,3,6,1,4,1,9,9,719,1,51,3,1,2),_CucsUuidpoolFormatDn_Type())
cucsUuidpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolFormatDn.setStatus(_A)
_CucsUuidpoolFormatRn_Type=SnmpAdminString
_CucsUuidpoolFormatRn_Object=MibTableColumn
cucsUuidpoolFormatRn=_CucsUuidpoolFormatRn_Object((1,3,6,1,4,1,9,9,719,1,51,3,1,3),_CucsUuidpoolFormatRn_Type())
cucsUuidpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolFormatRn.setStatus(_A)
_CucsUuidpoolFormatFormat_Type=Unsigned64
_CucsUuidpoolFormatFormat_Object=MibTableColumn
cucsUuidpoolFormatFormat=_CucsUuidpoolFormatFormat_Object((1,3,6,1,4,1,9,9,719,1,51,3,1,4),_CucsUuidpoolFormatFormat_Type())
cucsUuidpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolFormatFormat.setStatus(_A)
_CucsUuidpoolFormatMask_Type=CucsAddressUIDSuffxMask
_CucsUuidpoolFormatMask_Object=MibTableColumn
cucsUuidpoolFormatMask=_CucsUuidpoolFormatMask_Object((1,3,6,1,4,1,9,9,719,1,51,3,1,5),_CucsUuidpoolFormatMask_Type())
cucsUuidpoolFormatMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolFormatMask.setStatus(_A)
_CucsUuidpoolPoolTable_Object=MibTable
cucsUuidpoolPoolTable=_CucsUuidpoolPoolTable_Object((1,3,6,1,4,1,9,9,719,1,51,4))
if mibBuilder.loadTexts:cucsUuidpoolPoolTable.setStatus(_A)
_CucsUuidpoolPoolEntry_Object=MibTableRow
cucsUuidpoolPoolEntry=_CucsUuidpoolPoolEntry_Object((1,3,6,1,4,1,9,9,719,1,51,4,1))
cucsUuidpoolPoolEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsUuidpoolPoolEntry.setStatus(_A)
_CucsUuidpoolPoolInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolPoolInstanceId_Object=MibTableColumn
cucsUuidpoolPoolInstanceId=_CucsUuidpoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,1),_CucsUuidpoolPoolInstanceId_Type())
cucsUuidpoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolPoolInstanceId.setStatus(_A)
_CucsUuidpoolPoolDn_Type=CucsManagedObjectDn
_CucsUuidpoolPoolDn_Object=MibTableColumn
cucsUuidpoolPoolDn=_CucsUuidpoolPoolDn_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,2),_CucsUuidpoolPoolDn_Type())
cucsUuidpoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolDn.setStatus(_A)
_CucsUuidpoolPoolRn_Type=SnmpAdminString
_CucsUuidpoolPoolRn_Object=MibTableColumn
cucsUuidpoolPoolRn=_CucsUuidpoolPoolRn_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,3),_CucsUuidpoolPoolRn_Type())
cucsUuidpoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolRn.setStatus(_A)
_CucsUuidpoolPoolAssigned_Type=Gauge32
_CucsUuidpoolPoolAssigned_Object=MibTableColumn
cucsUuidpoolPoolAssigned=_CucsUuidpoolPoolAssigned_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,4),_CucsUuidpoolPoolAssigned_Type())
cucsUuidpoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolAssigned.setStatus(_A)
_CucsUuidpoolPoolDescr_Type=SnmpAdminString
_CucsUuidpoolPoolDescr_Object=MibTableColumn
cucsUuidpoolPoolDescr=_CucsUuidpoolPoolDescr_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,5),_CucsUuidpoolPoolDescr_Type())
cucsUuidpoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolDescr.setStatus(_A)
_CucsUuidpoolPoolIntId_Type=SnmpAdminString
_CucsUuidpoolPoolIntId_Object=MibTableColumn
cucsUuidpoolPoolIntId=_CucsUuidpoolPoolIntId_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,6),_CucsUuidpoolPoolIntId_Type())
cucsUuidpoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolIntId.setStatus(_A)
_CucsUuidpoolPoolName_Type=SnmpAdminString
_CucsUuidpoolPoolName_Object=MibTableColumn
cucsUuidpoolPoolName=_CucsUuidpoolPoolName_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,7),_CucsUuidpoolPoolName_Type())
cucsUuidpoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolName.setStatus(_A)
_CucsUuidpoolPoolPrefix_Type=Unsigned64
_CucsUuidpoolPoolPrefix_Object=MibTableColumn
cucsUuidpoolPoolPrefix=_CucsUuidpoolPoolPrefix_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,8),_CucsUuidpoolPoolPrefix_Type())
cucsUuidpoolPoolPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolPrefix.setStatus(_A)
_CucsUuidpoolPoolSize_Type=Gauge32
_CucsUuidpoolPoolSize_Object=MibTableColumn
cucsUuidpoolPoolSize=_CucsUuidpoolPoolSize_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,9),_CucsUuidpoolPoolSize_Type())
cucsUuidpoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolSize.setStatus(_A)
_CucsUuidpoolPoolAssignmentOrder_Type=CucsUuidpoolPoolAssignmentOrder
_CucsUuidpoolPoolAssignmentOrder_Object=MibTableColumn
cucsUuidpoolPoolAssignmentOrder=_CucsUuidpoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,10),_CucsUuidpoolPoolAssignmentOrder_Type())
cucsUuidpoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolAssignmentOrder.setStatus(_A)
_CucsUuidpoolPoolPolicyLevel_Type=Gauge32
_CucsUuidpoolPoolPolicyLevel_Object=MibTableColumn
cucsUuidpoolPoolPolicyLevel=_CucsUuidpoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,11),_CucsUuidpoolPoolPolicyLevel_Type())
cucsUuidpoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolPolicyLevel.setStatus(_A)
_CucsUuidpoolPoolPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsUuidpoolPoolPolicyOwner_Object=MibTableColumn
cucsUuidpoolPoolPolicyOwner=_CucsUuidpoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,51,4,1,12),_CucsUuidpoolPoolPolicyOwner_Type())
cucsUuidpoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolPolicyOwner.setStatus(_A)
_CucsUuidpoolPoolableTable_Object=MibTable
cucsUuidpoolPoolableTable=_CucsUuidpoolPoolableTable_Object((1,3,6,1,4,1,9,9,719,1,51,5))
if mibBuilder.loadTexts:cucsUuidpoolPoolableTable.setStatus(_A)
_CucsUuidpoolPoolableEntry_Object=MibTableRow
cucsUuidpoolPoolableEntry=_CucsUuidpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,719,1,51,5,1))
cucsUuidpoolPoolableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsUuidpoolPoolableEntry.setStatus(_A)
_CucsUuidpoolPoolableInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolPoolableInstanceId_Object=MibTableColumn
cucsUuidpoolPoolableInstanceId=_CucsUuidpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,5,1,1),_CucsUuidpoolPoolableInstanceId_Type())
cucsUuidpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolPoolableInstanceId.setStatus(_A)
_CucsUuidpoolPoolableDn_Type=CucsManagedObjectDn
_CucsUuidpoolPoolableDn_Object=MibTableColumn
cucsUuidpoolPoolableDn=_CucsUuidpoolPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,51,5,1,2),_CucsUuidpoolPoolableDn_Type())
cucsUuidpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolableDn.setStatus(_A)
_CucsUuidpoolPoolableRn_Type=SnmpAdminString
_CucsUuidpoolPoolableRn_Object=MibTableColumn
cucsUuidpoolPoolableRn=_CucsUuidpoolPoolableRn_Object((1,3,6,1,4,1,9,9,719,1,51,5,1,3),_CucsUuidpoolPoolableRn_Type())
cucsUuidpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolableRn.setStatus(_A)
_CucsUuidpoolPoolableId_Type=Unsigned64
_CucsUuidpoolPoolableId_Object=MibTableColumn
cucsUuidpoolPoolableId=_CucsUuidpoolPoolableId_Object((1,3,6,1,4,1,9,9,719,1,51,5,1,4),_CucsUuidpoolPoolableId_Type())
cucsUuidpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolableId.setStatus(_A)
_CucsUuidpoolPoolablePoolDn_Type=SnmpAdminString
_CucsUuidpoolPoolablePoolDn_Object=MibTableColumn
cucsUuidpoolPoolablePoolDn=_CucsUuidpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,719,1,51,5,1,5),_CucsUuidpoolPoolablePoolDn_Type())
cucsUuidpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPoolablePoolDn.setStatus(_A)
_CucsUuidpoolPooledTable_Object=MibTable
cucsUuidpoolPooledTable=_CucsUuidpoolPooledTable_Object((1,3,6,1,4,1,9,9,719,1,51,6))
if mibBuilder.loadTexts:cucsUuidpoolPooledTable.setStatus(_A)
_CucsUuidpoolPooledEntry_Object=MibTableRow
cucsUuidpoolPooledEntry=_CucsUuidpoolPooledEntry_Object((1,3,6,1,4,1,9,9,719,1,51,6,1))
cucsUuidpoolPooledEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsUuidpoolPooledEntry.setStatus(_A)
_CucsUuidpoolPooledInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolPooledInstanceId_Object=MibTableColumn
cucsUuidpoolPooledInstanceId=_CucsUuidpoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,1),_CucsUuidpoolPooledInstanceId_Type())
cucsUuidpoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolPooledInstanceId.setStatus(_A)
_CucsUuidpoolPooledDn_Type=CucsManagedObjectDn
_CucsUuidpoolPooledDn_Object=MibTableColumn
cucsUuidpoolPooledDn=_CucsUuidpoolPooledDn_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,2),_CucsUuidpoolPooledDn_Type())
cucsUuidpoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledDn.setStatus(_A)
_CucsUuidpoolPooledRn_Type=SnmpAdminString
_CucsUuidpoolPooledRn_Object=MibTableColumn
cucsUuidpoolPooledRn=_CucsUuidpoolPooledRn_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,3),_CucsUuidpoolPooledRn_Type())
cucsUuidpoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledRn.setStatus(_A)
_CucsUuidpoolPooledAssigned_Type=TruthValue
_CucsUuidpoolPooledAssigned_Object=MibTableColumn
cucsUuidpoolPooledAssigned=_CucsUuidpoolPooledAssigned_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,4),_CucsUuidpoolPooledAssigned_Type())
cucsUuidpoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledAssigned.setStatus(_A)
_CucsUuidpoolPooledAssignedToDn_Type=SnmpAdminString
_CucsUuidpoolPooledAssignedToDn_Object=MibTableColumn
cucsUuidpoolPooledAssignedToDn=_CucsUuidpoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,5),_CucsUuidpoolPooledAssignedToDn_Type())
cucsUuidpoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledAssignedToDn.setStatus(_A)
_CucsUuidpoolPooledId_Type=Unsigned64
_CucsUuidpoolPooledId_Object=MibTableColumn
cucsUuidpoolPooledId=_CucsUuidpoolPooledId_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,6),_CucsUuidpoolPooledId_Type())
cucsUuidpoolPooledId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledId.setStatus(_A)
_CucsUuidpoolPooledPoolableDn_Type=SnmpAdminString
_CucsUuidpoolPooledPoolableDn_Object=MibTableColumn
cucsUuidpoolPooledPoolableDn=_CucsUuidpoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,7),_CucsUuidpoolPooledPoolableDn_Type())
cucsUuidpoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledPoolableDn.setStatus(_A)
_CucsUuidpoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CucsUuidpoolPooledPrevAssignedToDn_Object=MibTableColumn
cucsUuidpoolPooledPrevAssignedToDn=_CucsUuidpoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,51,6,1,8),_CucsUuidpoolPooledPrevAssignedToDn_Type())
cucsUuidpoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolPooledPrevAssignedToDn.setStatus(_A)
_CucsUuidpoolUniverseTable_Object=MibTable
cucsUuidpoolUniverseTable=_CucsUuidpoolUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,51,7))
if mibBuilder.loadTexts:cucsUuidpoolUniverseTable.setStatus(_A)
_CucsUuidpoolUniverseEntry_Object=MibTableRow
cucsUuidpoolUniverseEntry=_CucsUuidpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,51,7,1))
cucsUuidpoolUniverseEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsUuidpoolUniverseEntry.setStatus(_A)
_CucsUuidpoolUniverseInstanceId_Type=CucsManagedObjectId
_CucsUuidpoolUniverseInstanceId_Object=MibTableColumn
cucsUuidpoolUniverseInstanceId=_CucsUuidpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,51,7,1,1),_CucsUuidpoolUniverseInstanceId_Type())
cucsUuidpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsUuidpoolUniverseInstanceId.setStatus(_A)
_CucsUuidpoolUniverseDn_Type=CucsManagedObjectDn
_CucsUuidpoolUniverseDn_Object=MibTableColumn
cucsUuidpoolUniverseDn=_CucsUuidpoolUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,51,7,1,2),_CucsUuidpoolUniverseDn_Type())
cucsUuidpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolUniverseDn.setStatus(_A)
_CucsUuidpoolUniverseRn_Type=SnmpAdminString
_CucsUuidpoolUniverseRn_Object=MibTableColumn
cucsUuidpoolUniverseRn=_CucsUuidpoolUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,51,7,1,3),_CucsUuidpoolUniverseRn_Type())
cucsUuidpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsUuidpoolUniverseRn.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsUuidpoolObjects':cucsUuidpoolObjects,'cucsUuidpoolAddrTable':cucsUuidpoolAddrTable,'cucsUuidpoolAddrEntry':cucsUuidpoolAddrEntry,_E:cucsUuidpoolAddrInstanceId,'cucsUuidpoolAddrDn':cucsUuidpoolAddrDn,'cucsUuidpoolAddrRn':cucsUuidpoolAddrRn,'cucsUuidpoolAddrAssigned':cucsUuidpoolAddrAssigned,'cucsUuidpoolAddrAssignedToDn':cucsUuidpoolAddrAssignedToDn,'cucsUuidpoolAddrId':cucsUuidpoolAddrId,'cucsUuidpoolAddrOwner':cucsUuidpoolAddrOwner,'cucsUuidpoolAddrGlobalAssignedCnt':cucsUuidpoolAddrGlobalAssignedCnt,'cucsUuidpoolAddrGlobalDefinedCnt':cucsUuidpoolAddrGlobalDefinedCnt,'cucsUuidpoolBlockTable':cucsUuidpoolBlockTable,'cucsUuidpoolBlockEntry':cucsUuidpoolBlockEntry,_F:cucsUuidpoolBlockInstanceId,'cucsUuidpoolBlockDn':cucsUuidpoolBlockDn,'cucsUuidpoolBlockRn':cucsUuidpoolBlockRn,'cucsUuidpoolBlockFrom':cucsUuidpoolBlockFrom,'cucsUuidpoolBlockTo':cucsUuidpoolBlockTo,'cucsUuidpoolFormatTable':cucsUuidpoolFormatTable,'cucsUuidpoolFormatEntry':cucsUuidpoolFormatEntry,_G:cucsUuidpoolFormatInstanceId,'cucsUuidpoolFormatDn':cucsUuidpoolFormatDn,'cucsUuidpoolFormatRn':cucsUuidpoolFormatRn,'cucsUuidpoolFormatFormat':cucsUuidpoolFormatFormat,'cucsUuidpoolFormatMask':cucsUuidpoolFormatMask,'cucsUuidpoolPoolTable':cucsUuidpoolPoolTable,'cucsUuidpoolPoolEntry':cucsUuidpoolPoolEntry,_H:cucsUuidpoolPoolInstanceId,'cucsUuidpoolPoolDn':cucsUuidpoolPoolDn,'cucsUuidpoolPoolRn':cucsUuidpoolPoolRn,'cucsUuidpoolPoolAssigned':cucsUuidpoolPoolAssigned,'cucsUuidpoolPoolDescr':cucsUuidpoolPoolDescr,'cucsUuidpoolPoolIntId':cucsUuidpoolPoolIntId,'cucsUuidpoolPoolName':cucsUuidpoolPoolName,'cucsUuidpoolPoolPrefix':cucsUuidpoolPoolPrefix,'cucsUuidpoolPoolSize':cucsUuidpoolPoolSize,'cucsUuidpoolPoolAssignmentOrder':cucsUuidpoolPoolAssignmentOrder,'cucsUuidpoolPoolPolicyLevel':cucsUuidpoolPoolPolicyLevel,'cucsUuidpoolPoolPolicyOwner':cucsUuidpoolPoolPolicyOwner,'cucsUuidpoolPoolableTable':cucsUuidpoolPoolableTable,'cucsUuidpoolPoolableEntry':cucsUuidpoolPoolableEntry,_I:cucsUuidpoolPoolableInstanceId,'cucsUuidpoolPoolableDn':cucsUuidpoolPoolableDn,'cucsUuidpoolPoolableRn':cucsUuidpoolPoolableRn,'cucsUuidpoolPoolableId':cucsUuidpoolPoolableId,'cucsUuidpoolPoolablePoolDn':cucsUuidpoolPoolablePoolDn,'cucsUuidpoolPooledTable':cucsUuidpoolPooledTable,'cucsUuidpoolPooledEntry':cucsUuidpoolPooledEntry,_J:cucsUuidpoolPooledInstanceId,'cucsUuidpoolPooledDn':cucsUuidpoolPooledDn,'cucsUuidpoolPooledRn':cucsUuidpoolPooledRn,'cucsUuidpoolPooledAssigned':cucsUuidpoolPooledAssigned,'cucsUuidpoolPooledAssignedToDn':cucsUuidpoolPooledAssignedToDn,'cucsUuidpoolPooledId':cucsUuidpoolPooledId,'cucsUuidpoolPooledPoolableDn':cucsUuidpoolPooledPoolableDn,'cucsUuidpoolPooledPrevAssignedToDn':cucsUuidpoolPooledPrevAssignedToDn,'cucsUuidpoolUniverseTable':cucsUuidpoolUniverseTable,'cucsUuidpoolUniverseEntry':cucsUuidpoolUniverseEntry,_K:cucsUuidpoolUniverseInstanceId,'cucsUuidpoolUniverseDn':cucsUuidpoolUniverseDn,'cucsUuidpoolUniverseRn':cucsUuidpoolUniverseRn})