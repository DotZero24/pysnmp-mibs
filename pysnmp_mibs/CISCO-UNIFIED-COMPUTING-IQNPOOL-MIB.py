_L='cucsIqnpoolTransportBlockInstanceId'
_K='cucsIqnpoolUniverseInstanceId'
_J='cucsIqnpoolPooledInstanceId'
_I='cucsIqnpoolPoolableInstanceId'
_H='cucsIqnpoolPoolInstanceId'
_G='cucsIqnpoolFormatInstanceId'
_F='cucsIqnpoolBlockInstanceId'
_E='cucsIqnpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-IQNPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsIqnpoolBlockFrom,CucsIqnpoolBlockTo,CucsIqnpoolPoolAssignmentOrder,CucsIqnpoolTransportBlockFrom,CucsIqnpoolTransportBlockTo,CucsPolicyPolicyOwner,CucsPoolElementOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsIqnpoolBlockFrom','CucsIqnpoolBlockTo','CucsIqnpoolPoolAssignmentOrder','CucsIqnpoolTransportBlockFrom','CucsIqnpoolTransportBlockTo','CucsPolicyPolicyOwner','CucsPoolElementOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsIqnpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,59))
_CucsIqnpoolAddrTable_Object=MibTable
cucsIqnpoolAddrTable=_CucsIqnpoolAddrTable_Object((1,3,6,1,4,1,9,9,719,1,59,1))
if mibBuilder.loadTexts:cucsIqnpoolAddrTable.setStatus(_A)
_CucsIqnpoolAddrEntry_Object=MibTableRow
cucsIqnpoolAddrEntry=_CucsIqnpoolAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,59,1,1))
cucsIqnpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsIqnpoolAddrEntry.setStatus(_A)
_CucsIqnpoolAddrInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolAddrInstanceId_Object=MibTableColumn
cucsIqnpoolAddrInstanceId=_CucsIqnpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,1),_CucsIqnpoolAddrInstanceId_Type())
cucsIqnpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolAddrInstanceId.setStatus(_A)
_CucsIqnpoolAddrDn_Type=CucsManagedObjectDn
_CucsIqnpoolAddrDn_Object=MibTableColumn
cucsIqnpoolAddrDn=_CucsIqnpoolAddrDn_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,2),_CucsIqnpoolAddrDn_Type())
cucsIqnpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrDn.setStatus(_A)
_CucsIqnpoolAddrRn_Type=SnmpAdminString
_CucsIqnpoolAddrRn_Object=MibTableColumn
cucsIqnpoolAddrRn=_CucsIqnpoolAddrRn_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,3),_CucsIqnpoolAddrRn_Type())
cucsIqnpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrRn.setStatus(_A)
_CucsIqnpoolAddrAssigned_Type=TruthValue
_CucsIqnpoolAddrAssigned_Object=MibTableColumn
cucsIqnpoolAddrAssigned=_CucsIqnpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,4),_CucsIqnpoolAddrAssigned_Type())
cucsIqnpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrAssigned.setStatus(_A)
_CucsIqnpoolAddrAssignedToDn_Type=SnmpAdminString
_CucsIqnpoolAddrAssignedToDn_Object=MibTableColumn
cucsIqnpoolAddrAssignedToDn=_CucsIqnpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,5),_CucsIqnpoolAddrAssignedToDn_Type())
cucsIqnpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrAssignedToDn.setStatus(_A)
_CucsIqnpoolAddrName_Type=SnmpAdminString
_CucsIqnpoolAddrName_Object=MibTableColumn
cucsIqnpoolAddrName=_CucsIqnpoolAddrName_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,6),_CucsIqnpoolAddrName_Type())
cucsIqnpoolAddrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrName.setStatus(_A)
_CucsIqnpoolAddrOwner_Type=CucsPoolElementOwner
_CucsIqnpoolAddrOwner_Object=MibTableColumn
cucsIqnpoolAddrOwner=_CucsIqnpoolAddrOwner_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,7),_CucsIqnpoolAddrOwner_Type())
cucsIqnpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrOwner.setStatus(_A)
_CucsIqnpoolAddrGlobalAssignedCnt_Type=Gauge32
_CucsIqnpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cucsIqnpoolAddrGlobalAssignedCnt=_CucsIqnpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,8),_CucsIqnpoolAddrGlobalAssignedCnt_Type())
cucsIqnpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrGlobalAssignedCnt.setStatus(_A)
_CucsIqnpoolAddrGlobalDefinedCnt_Type=Gauge32
_CucsIqnpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cucsIqnpoolAddrGlobalDefinedCnt=_CucsIqnpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,719,1,59,1,1,9),_CucsIqnpoolAddrGlobalDefinedCnt_Type())
cucsIqnpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolAddrGlobalDefinedCnt.setStatus(_A)
_CucsIqnpoolBlockTable_Object=MibTable
cucsIqnpoolBlockTable=_CucsIqnpoolBlockTable_Object((1,3,6,1,4,1,9,9,719,1,59,2))
if mibBuilder.loadTexts:cucsIqnpoolBlockTable.setStatus(_A)
_CucsIqnpoolBlockEntry_Object=MibTableRow
cucsIqnpoolBlockEntry=_CucsIqnpoolBlockEntry_Object((1,3,6,1,4,1,9,9,719,1,59,2,1))
cucsIqnpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsIqnpoolBlockEntry.setStatus(_A)
_CucsIqnpoolBlockInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolBlockInstanceId_Object=MibTableColumn
cucsIqnpoolBlockInstanceId=_CucsIqnpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,2,1,1),_CucsIqnpoolBlockInstanceId_Type())
cucsIqnpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolBlockInstanceId.setStatus(_A)
_CucsIqnpoolBlockDn_Type=CucsManagedObjectDn
_CucsIqnpoolBlockDn_Object=MibTableColumn
cucsIqnpoolBlockDn=_CucsIqnpoolBlockDn_Object((1,3,6,1,4,1,9,9,719,1,59,2,1,2),_CucsIqnpoolBlockDn_Type())
cucsIqnpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolBlockDn.setStatus(_A)
_CucsIqnpoolBlockRn_Type=SnmpAdminString
_CucsIqnpoolBlockRn_Object=MibTableColumn
cucsIqnpoolBlockRn=_CucsIqnpoolBlockRn_Object((1,3,6,1,4,1,9,9,719,1,59,2,1,3),_CucsIqnpoolBlockRn_Type())
cucsIqnpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolBlockRn.setStatus(_A)
_CucsIqnpoolBlockFrom_Type=CucsIqnpoolBlockFrom
_CucsIqnpoolBlockFrom_Object=MibTableColumn
cucsIqnpoolBlockFrom=_CucsIqnpoolBlockFrom_Object((1,3,6,1,4,1,9,9,719,1,59,2,1,4),_CucsIqnpoolBlockFrom_Type())
cucsIqnpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolBlockFrom.setStatus(_A)
_CucsIqnpoolBlockSuffix_Type=SnmpAdminString
_CucsIqnpoolBlockSuffix_Object=MibTableColumn
cucsIqnpoolBlockSuffix=_CucsIqnpoolBlockSuffix_Object((1,3,6,1,4,1,9,9,719,1,59,2,1,6),_CucsIqnpoolBlockSuffix_Type())
cucsIqnpoolBlockSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolBlockSuffix.setStatus(_A)
_CucsIqnpoolBlockTo_Type=CucsIqnpoolBlockTo
_CucsIqnpoolBlockTo_Object=MibTableColumn
cucsIqnpoolBlockTo=_CucsIqnpoolBlockTo_Object((1,3,6,1,4,1,9,9,719,1,59,2,1,7),_CucsIqnpoolBlockTo_Type())
cucsIqnpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolBlockTo.setStatus(_A)
_CucsIqnpoolFormatTable_Object=MibTable
cucsIqnpoolFormatTable=_CucsIqnpoolFormatTable_Object((1,3,6,1,4,1,9,9,719,1,59,3))
if mibBuilder.loadTexts:cucsIqnpoolFormatTable.setStatus(_A)
_CucsIqnpoolFormatEntry_Object=MibTableRow
cucsIqnpoolFormatEntry=_CucsIqnpoolFormatEntry_Object((1,3,6,1,4,1,9,9,719,1,59,3,1))
cucsIqnpoolFormatEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsIqnpoolFormatEntry.setStatus(_A)
_CucsIqnpoolFormatInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolFormatInstanceId_Object=MibTableColumn
cucsIqnpoolFormatInstanceId=_CucsIqnpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,3,1,1),_CucsIqnpoolFormatInstanceId_Type())
cucsIqnpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolFormatInstanceId.setStatus(_A)
_CucsIqnpoolFormatDn_Type=CucsManagedObjectDn
_CucsIqnpoolFormatDn_Object=MibTableColumn
cucsIqnpoolFormatDn=_CucsIqnpoolFormatDn_Object((1,3,6,1,4,1,9,9,719,1,59,3,1,2),_CucsIqnpoolFormatDn_Type())
cucsIqnpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolFormatDn.setStatus(_A)
_CucsIqnpoolFormatRn_Type=SnmpAdminString
_CucsIqnpoolFormatRn_Object=MibTableColumn
cucsIqnpoolFormatRn=_CucsIqnpoolFormatRn_Object((1,3,6,1,4,1,9,9,719,1,59,3,1,3),_CucsIqnpoolFormatRn_Type())
cucsIqnpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolFormatRn.setStatus(_A)
_CucsIqnpoolFormatFormat_Type=SnmpAdminString
_CucsIqnpoolFormatFormat_Object=MibTableColumn
cucsIqnpoolFormatFormat=_CucsIqnpoolFormatFormat_Object((1,3,6,1,4,1,9,9,719,1,59,3,1,4),_CucsIqnpoolFormatFormat_Type())
cucsIqnpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolFormatFormat.setStatus(_A)
_CucsIqnpoolPoolTable_Object=MibTable
cucsIqnpoolPoolTable=_CucsIqnpoolPoolTable_Object((1,3,6,1,4,1,9,9,719,1,59,4))
if mibBuilder.loadTexts:cucsIqnpoolPoolTable.setStatus(_A)
_CucsIqnpoolPoolEntry_Object=MibTableRow
cucsIqnpoolPoolEntry=_CucsIqnpoolPoolEntry_Object((1,3,6,1,4,1,9,9,719,1,59,4,1))
cucsIqnpoolPoolEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsIqnpoolPoolEntry.setStatus(_A)
_CucsIqnpoolPoolInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolPoolInstanceId_Object=MibTableColumn
cucsIqnpoolPoolInstanceId=_CucsIqnpoolPoolInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,1),_CucsIqnpoolPoolInstanceId_Type())
cucsIqnpoolPoolInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolPoolInstanceId.setStatus(_A)
_CucsIqnpoolPoolDn_Type=CucsManagedObjectDn
_CucsIqnpoolPoolDn_Object=MibTableColumn
cucsIqnpoolPoolDn=_CucsIqnpoolPoolDn_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,2),_CucsIqnpoolPoolDn_Type())
cucsIqnpoolPoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolDn.setStatus(_A)
_CucsIqnpoolPoolRn_Type=SnmpAdminString
_CucsIqnpoolPoolRn_Object=MibTableColumn
cucsIqnpoolPoolRn=_CucsIqnpoolPoolRn_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,3),_CucsIqnpoolPoolRn_Type())
cucsIqnpoolPoolRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolRn.setStatus(_A)
_CucsIqnpoolPoolAssigned_Type=Gauge32
_CucsIqnpoolPoolAssigned_Object=MibTableColumn
cucsIqnpoolPoolAssigned=_CucsIqnpoolPoolAssigned_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,4),_CucsIqnpoolPoolAssigned_Type())
cucsIqnpoolPoolAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolAssigned.setStatus(_A)
_CucsIqnpoolPoolDescr_Type=SnmpAdminString
_CucsIqnpoolPoolDescr_Object=MibTableColumn
cucsIqnpoolPoolDescr=_CucsIqnpoolPoolDescr_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,5),_CucsIqnpoolPoolDescr_Type())
cucsIqnpoolPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolDescr.setStatus(_A)
_CucsIqnpoolPoolIntId_Type=SnmpAdminString
_CucsIqnpoolPoolIntId_Object=MibTableColumn
cucsIqnpoolPoolIntId=_CucsIqnpoolPoolIntId_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,6),_CucsIqnpoolPoolIntId_Type())
cucsIqnpoolPoolIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolIntId.setStatus(_A)
_CucsIqnpoolPoolName_Type=SnmpAdminString
_CucsIqnpoolPoolName_Object=MibTableColumn
cucsIqnpoolPoolName=_CucsIqnpoolPoolName_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,7),_CucsIqnpoolPoolName_Type())
cucsIqnpoolPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolName.setStatus(_A)
_CucsIqnpoolPoolPrefix_Type=SnmpAdminString
_CucsIqnpoolPoolPrefix_Object=MibTableColumn
cucsIqnpoolPoolPrefix=_CucsIqnpoolPoolPrefix_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,8),_CucsIqnpoolPoolPrefix_Type())
cucsIqnpoolPoolPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolPrefix.setStatus(_A)
_CucsIqnpoolPoolSize_Type=Gauge32
_CucsIqnpoolPoolSize_Object=MibTableColumn
cucsIqnpoolPoolSize=_CucsIqnpoolPoolSize_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,9),_CucsIqnpoolPoolSize_Type())
cucsIqnpoolPoolSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolSize.setStatus(_A)
_CucsIqnpoolPoolAssignmentOrder_Type=CucsIqnpoolPoolAssignmentOrder
_CucsIqnpoolPoolAssignmentOrder_Object=MibTableColumn
cucsIqnpoolPoolAssignmentOrder=_CucsIqnpoolPoolAssignmentOrder_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,10),_CucsIqnpoolPoolAssignmentOrder_Type())
cucsIqnpoolPoolAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolAssignmentOrder.setStatus(_A)
_CucsIqnpoolPoolPolicyLevel_Type=Gauge32
_CucsIqnpoolPoolPolicyLevel_Object=MibTableColumn
cucsIqnpoolPoolPolicyLevel=_CucsIqnpoolPoolPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,11),_CucsIqnpoolPoolPolicyLevel_Type())
cucsIqnpoolPoolPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolPolicyLevel.setStatus(_A)
_CucsIqnpoolPoolPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsIqnpoolPoolPolicyOwner_Object=MibTableColumn
cucsIqnpoolPoolPolicyOwner=_CucsIqnpoolPoolPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,59,4,1,12),_CucsIqnpoolPoolPolicyOwner_Type())
cucsIqnpoolPoolPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolPolicyOwner.setStatus(_A)
_CucsIqnpoolPoolableTable_Object=MibTable
cucsIqnpoolPoolableTable=_CucsIqnpoolPoolableTable_Object((1,3,6,1,4,1,9,9,719,1,59,5))
if mibBuilder.loadTexts:cucsIqnpoolPoolableTable.setStatus(_A)
_CucsIqnpoolPoolableEntry_Object=MibTableRow
cucsIqnpoolPoolableEntry=_CucsIqnpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,719,1,59,5,1))
cucsIqnpoolPoolableEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsIqnpoolPoolableEntry.setStatus(_A)
_CucsIqnpoolPoolableInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolPoolableInstanceId_Object=MibTableColumn
cucsIqnpoolPoolableInstanceId=_CucsIqnpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,5,1,1),_CucsIqnpoolPoolableInstanceId_Type())
cucsIqnpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolPoolableInstanceId.setStatus(_A)
_CucsIqnpoolPoolableDn_Type=CucsManagedObjectDn
_CucsIqnpoolPoolableDn_Object=MibTableColumn
cucsIqnpoolPoolableDn=_CucsIqnpoolPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,59,5,1,2),_CucsIqnpoolPoolableDn_Type())
cucsIqnpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolableDn.setStatus(_A)
_CucsIqnpoolPoolableRn_Type=SnmpAdminString
_CucsIqnpoolPoolableRn_Object=MibTableColumn
cucsIqnpoolPoolableRn=_CucsIqnpoolPoolableRn_Object((1,3,6,1,4,1,9,9,719,1,59,5,1,3),_CucsIqnpoolPoolableRn_Type())
cucsIqnpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolableRn.setStatus(_A)
_CucsIqnpoolPoolableId_Type=Unsigned64
_CucsIqnpoolPoolableId_Object=MibTableColumn
cucsIqnpoolPoolableId=_CucsIqnpoolPoolableId_Object((1,3,6,1,4,1,9,9,719,1,59,5,1,4),_CucsIqnpoolPoolableId_Type())
cucsIqnpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolableId.setStatus(_A)
_CucsIqnpoolPoolablePoolDn_Type=SnmpAdminString
_CucsIqnpoolPoolablePoolDn_Object=MibTableColumn
cucsIqnpoolPoolablePoolDn=_CucsIqnpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,719,1,59,5,1,5),_CucsIqnpoolPoolablePoolDn_Type())
cucsIqnpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPoolablePoolDn.setStatus(_A)
_CucsIqnpoolPooledTable_Object=MibTable
cucsIqnpoolPooledTable=_CucsIqnpoolPooledTable_Object((1,3,6,1,4,1,9,9,719,1,59,6))
if mibBuilder.loadTexts:cucsIqnpoolPooledTable.setStatus(_A)
_CucsIqnpoolPooledEntry_Object=MibTableRow
cucsIqnpoolPooledEntry=_CucsIqnpoolPooledEntry_Object((1,3,6,1,4,1,9,9,719,1,59,6,1))
cucsIqnpoolPooledEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsIqnpoolPooledEntry.setStatus(_A)
_CucsIqnpoolPooledInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolPooledInstanceId_Object=MibTableColumn
cucsIqnpoolPooledInstanceId=_CucsIqnpoolPooledInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,1),_CucsIqnpoolPooledInstanceId_Type())
cucsIqnpoolPooledInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolPooledInstanceId.setStatus(_A)
_CucsIqnpoolPooledDn_Type=CucsManagedObjectDn
_CucsIqnpoolPooledDn_Object=MibTableColumn
cucsIqnpoolPooledDn=_CucsIqnpoolPooledDn_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,2),_CucsIqnpoolPooledDn_Type())
cucsIqnpoolPooledDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledDn.setStatus(_A)
_CucsIqnpoolPooledRn_Type=SnmpAdminString
_CucsIqnpoolPooledRn_Object=MibTableColumn
cucsIqnpoolPooledRn=_CucsIqnpoolPooledRn_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,3),_CucsIqnpoolPooledRn_Type())
cucsIqnpoolPooledRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledRn.setStatus(_A)
_CucsIqnpoolPooledAssigned_Type=TruthValue
_CucsIqnpoolPooledAssigned_Object=MibTableColumn
cucsIqnpoolPooledAssigned=_CucsIqnpoolPooledAssigned_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,4),_CucsIqnpoolPooledAssigned_Type())
cucsIqnpoolPooledAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledAssigned.setStatus(_A)
_CucsIqnpoolPooledAssignedToDn_Type=SnmpAdminString
_CucsIqnpoolPooledAssignedToDn_Object=MibTableColumn
cucsIqnpoolPooledAssignedToDn=_CucsIqnpoolPooledAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,5),_CucsIqnpoolPooledAssignedToDn_Type())
cucsIqnpoolPooledAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledAssignedToDn.setStatus(_A)
_CucsIqnpoolPooledName_Type=SnmpAdminString
_CucsIqnpoolPooledName_Object=MibTableColumn
cucsIqnpoolPooledName=_CucsIqnpoolPooledName_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,6),_CucsIqnpoolPooledName_Type())
cucsIqnpoolPooledName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledName.setStatus(_A)
_CucsIqnpoolPooledPoolableDn_Type=SnmpAdminString
_CucsIqnpoolPooledPoolableDn_Object=MibTableColumn
cucsIqnpoolPooledPoolableDn=_CucsIqnpoolPooledPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,7),_CucsIqnpoolPooledPoolableDn_Type())
cucsIqnpoolPooledPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledPoolableDn.setStatus(_A)
_CucsIqnpoolPooledPrevAssignedToDn_Type=SnmpAdminString
_CucsIqnpoolPooledPrevAssignedToDn_Object=MibTableColumn
cucsIqnpoolPooledPrevAssignedToDn=_CucsIqnpoolPooledPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,59,6,1,8),_CucsIqnpoolPooledPrevAssignedToDn_Type())
cucsIqnpoolPooledPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolPooledPrevAssignedToDn.setStatus(_A)
_CucsIqnpoolUniverseTable_Object=MibTable
cucsIqnpoolUniverseTable=_CucsIqnpoolUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,59,7))
if mibBuilder.loadTexts:cucsIqnpoolUniverseTable.setStatus(_A)
_CucsIqnpoolUniverseEntry_Object=MibTableRow
cucsIqnpoolUniverseEntry=_CucsIqnpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,59,7,1))
cucsIqnpoolUniverseEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsIqnpoolUniverseEntry.setStatus(_A)
_CucsIqnpoolUniverseInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolUniverseInstanceId_Object=MibTableColumn
cucsIqnpoolUniverseInstanceId=_CucsIqnpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,7,1,1),_CucsIqnpoolUniverseInstanceId_Type())
cucsIqnpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolUniverseInstanceId.setStatus(_A)
_CucsIqnpoolUniverseDn_Type=CucsManagedObjectDn
_CucsIqnpoolUniverseDn_Object=MibTableColumn
cucsIqnpoolUniverseDn=_CucsIqnpoolUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,59,7,1,2),_CucsIqnpoolUniverseDn_Type())
cucsIqnpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolUniverseDn.setStatus(_A)
_CucsIqnpoolUniverseRn_Type=SnmpAdminString
_CucsIqnpoolUniverseRn_Object=MibTableColumn
cucsIqnpoolUniverseRn=_CucsIqnpoolUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,59,7,1,3),_CucsIqnpoolUniverseRn_Type())
cucsIqnpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolUniverseRn.setStatus(_A)
_CucsIqnpoolTransportBlockTable_Object=MibTable
cucsIqnpoolTransportBlockTable=_CucsIqnpoolTransportBlockTable_Object((1,3,6,1,4,1,9,9,719,1,59,8))
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockTable.setStatus(_A)
_CucsIqnpoolTransportBlockEntry_Object=MibTableRow
cucsIqnpoolTransportBlockEntry=_CucsIqnpoolTransportBlockEntry_Object((1,3,6,1,4,1,9,9,719,1,59,8,1))
cucsIqnpoolTransportBlockEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockEntry.setStatus(_A)
_CucsIqnpoolTransportBlockInstanceId_Type=CucsManagedObjectId
_CucsIqnpoolTransportBlockInstanceId_Object=MibTableColumn
cucsIqnpoolTransportBlockInstanceId=_CucsIqnpoolTransportBlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,59,8,1,1),_CucsIqnpoolTransportBlockInstanceId_Type())
cucsIqnpoolTransportBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockInstanceId.setStatus(_A)
_CucsIqnpoolTransportBlockDn_Type=CucsManagedObjectDn
_CucsIqnpoolTransportBlockDn_Object=MibTableColumn
cucsIqnpoolTransportBlockDn=_CucsIqnpoolTransportBlockDn_Object((1,3,6,1,4,1,9,9,719,1,59,8,1,2),_CucsIqnpoolTransportBlockDn_Type())
cucsIqnpoolTransportBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockDn.setStatus(_A)
_CucsIqnpoolTransportBlockRn_Type=SnmpAdminString
_CucsIqnpoolTransportBlockRn_Object=MibTableColumn
cucsIqnpoolTransportBlockRn=_CucsIqnpoolTransportBlockRn_Object((1,3,6,1,4,1,9,9,719,1,59,8,1,3),_CucsIqnpoolTransportBlockRn_Type())
cucsIqnpoolTransportBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockRn.setStatus(_A)
_CucsIqnpoolTransportBlockFrom_Type=CucsIqnpoolTransportBlockFrom
_CucsIqnpoolTransportBlockFrom_Object=MibTableColumn
cucsIqnpoolTransportBlockFrom=_CucsIqnpoolTransportBlockFrom_Object((1,3,6,1,4,1,9,9,719,1,59,8,1,4),_CucsIqnpoolTransportBlockFrom_Type())
cucsIqnpoolTransportBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockFrom.setStatus(_A)
_CucsIqnpoolTransportBlockSuffix_Type=SnmpAdminString
_CucsIqnpoolTransportBlockSuffix_Object=MibTableColumn
cucsIqnpoolTransportBlockSuffix=_CucsIqnpoolTransportBlockSuffix_Object((1,3,6,1,4,1,9,9,719,1,59,8,1,5),_CucsIqnpoolTransportBlockSuffix_Type())
cucsIqnpoolTransportBlockSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockSuffix.setStatus(_A)
_CucsIqnpoolTransportBlockTo_Type=CucsIqnpoolTransportBlockTo
_CucsIqnpoolTransportBlockTo_Object=MibTableColumn
cucsIqnpoolTransportBlockTo=_CucsIqnpoolTransportBlockTo_Object((1,3,6,1,4,1,9,9,719,1,59,8,1,6),_CucsIqnpoolTransportBlockTo_Type())
cucsIqnpoolTransportBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsIqnpoolTransportBlockTo.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsIqnpoolObjects':cucsIqnpoolObjects,'cucsIqnpoolAddrTable':cucsIqnpoolAddrTable,'cucsIqnpoolAddrEntry':cucsIqnpoolAddrEntry,_E:cucsIqnpoolAddrInstanceId,'cucsIqnpoolAddrDn':cucsIqnpoolAddrDn,'cucsIqnpoolAddrRn':cucsIqnpoolAddrRn,'cucsIqnpoolAddrAssigned':cucsIqnpoolAddrAssigned,'cucsIqnpoolAddrAssignedToDn':cucsIqnpoolAddrAssignedToDn,'cucsIqnpoolAddrName':cucsIqnpoolAddrName,'cucsIqnpoolAddrOwner':cucsIqnpoolAddrOwner,'cucsIqnpoolAddrGlobalAssignedCnt':cucsIqnpoolAddrGlobalAssignedCnt,'cucsIqnpoolAddrGlobalDefinedCnt':cucsIqnpoolAddrGlobalDefinedCnt,'cucsIqnpoolBlockTable':cucsIqnpoolBlockTable,'cucsIqnpoolBlockEntry':cucsIqnpoolBlockEntry,_F:cucsIqnpoolBlockInstanceId,'cucsIqnpoolBlockDn':cucsIqnpoolBlockDn,'cucsIqnpoolBlockRn':cucsIqnpoolBlockRn,'cucsIqnpoolBlockFrom':cucsIqnpoolBlockFrom,'cucsIqnpoolBlockSuffix':cucsIqnpoolBlockSuffix,'cucsIqnpoolBlockTo':cucsIqnpoolBlockTo,'cucsIqnpoolFormatTable':cucsIqnpoolFormatTable,'cucsIqnpoolFormatEntry':cucsIqnpoolFormatEntry,_G:cucsIqnpoolFormatInstanceId,'cucsIqnpoolFormatDn':cucsIqnpoolFormatDn,'cucsIqnpoolFormatRn':cucsIqnpoolFormatRn,'cucsIqnpoolFormatFormat':cucsIqnpoolFormatFormat,'cucsIqnpoolPoolTable':cucsIqnpoolPoolTable,'cucsIqnpoolPoolEntry':cucsIqnpoolPoolEntry,_H:cucsIqnpoolPoolInstanceId,'cucsIqnpoolPoolDn':cucsIqnpoolPoolDn,'cucsIqnpoolPoolRn':cucsIqnpoolPoolRn,'cucsIqnpoolPoolAssigned':cucsIqnpoolPoolAssigned,'cucsIqnpoolPoolDescr':cucsIqnpoolPoolDescr,'cucsIqnpoolPoolIntId':cucsIqnpoolPoolIntId,'cucsIqnpoolPoolName':cucsIqnpoolPoolName,'cucsIqnpoolPoolPrefix':cucsIqnpoolPoolPrefix,'cucsIqnpoolPoolSize':cucsIqnpoolPoolSize,'cucsIqnpoolPoolAssignmentOrder':cucsIqnpoolPoolAssignmentOrder,'cucsIqnpoolPoolPolicyLevel':cucsIqnpoolPoolPolicyLevel,'cucsIqnpoolPoolPolicyOwner':cucsIqnpoolPoolPolicyOwner,'cucsIqnpoolPoolableTable':cucsIqnpoolPoolableTable,'cucsIqnpoolPoolableEntry':cucsIqnpoolPoolableEntry,_I:cucsIqnpoolPoolableInstanceId,'cucsIqnpoolPoolableDn':cucsIqnpoolPoolableDn,'cucsIqnpoolPoolableRn':cucsIqnpoolPoolableRn,'cucsIqnpoolPoolableId':cucsIqnpoolPoolableId,'cucsIqnpoolPoolablePoolDn':cucsIqnpoolPoolablePoolDn,'cucsIqnpoolPooledTable':cucsIqnpoolPooledTable,'cucsIqnpoolPooledEntry':cucsIqnpoolPooledEntry,_J:cucsIqnpoolPooledInstanceId,'cucsIqnpoolPooledDn':cucsIqnpoolPooledDn,'cucsIqnpoolPooledRn':cucsIqnpoolPooledRn,'cucsIqnpoolPooledAssigned':cucsIqnpoolPooledAssigned,'cucsIqnpoolPooledAssignedToDn':cucsIqnpoolPooledAssignedToDn,'cucsIqnpoolPooledName':cucsIqnpoolPooledName,'cucsIqnpoolPooledPoolableDn':cucsIqnpoolPooledPoolableDn,'cucsIqnpoolPooledPrevAssignedToDn':cucsIqnpoolPooledPrevAssignedToDn,'cucsIqnpoolUniverseTable':cucsIqnpoolUniverseTable,'cucsIqnpoolUniverseEntry':cucsIqnpoolUniverseEntry,_K:cucsIqnpoolUniverseInstanceId,'cucsIqnpoolUniverseDn':cucsIqnpoolUniverseDn,'cucsIqnpoolUniverseRn':cucsIqnpoolUniverseRn,'cucsIqnpoolTransportBlockTable':cucsIqnpoolTransportBlockTable,'cucsIqnpoolTransportBlockEntry':cucsIqnpoolTransportBlockEntry,_L:cucsIqnpoolTransportBlockInstanceId,'cucsIqnpoolTransportBlockDn':cucsIqnpoolTransportBlockDn,'cucsIqnpoolTransportBlockRn':cucsIqnpoolTransportBlockRn,'cucsIqnpoolTransportBlockFrom':cucsIqnpoolTransportBlockFrom,'cucsIqnpoolTransportBlockSuffix':cucsIqnpoolTransportBlockSuffix,'cucsIqnpoolTransportBlockTo':cucsIqnpoolTransportBlockTo})