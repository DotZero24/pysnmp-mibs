_M='cucsFcpoolInitiatorEpInstanceId'
_L='cucsFcpoolUniverseInstanceId'
_K='cucsFcpoolPoolableInstanceId'
_J='cucsFcpoolInitiatorsInstanceId'
_I='cucsFcpoolInitiatorInstanceId'
_H='cucsFcpoolFormatInstanceId'
_G='cucsFcpoolBootTargetInstanceId'
_F='cucsFcpoolBlockInstanceId'
_E='cucsFcpoolAddrInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-FCPOOL-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsAddressWWNMask,CucsFcpoolBootTargetType,CucsFcpoolInitiatorEpPurpose,CucsFcpoolInitiatorPurpose,CucsFcpoolInitiatorsAssignmentOrder,CucsFcpoolInitiatorsMaxPortsPerNode,CucsFcpoolInitiatorsPurpose,CucsPolicyPolicyOwner,CucsPoolElementOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsAddressWWNMask','CucsFcpoolBootTargetType','CucsFcpoolInitiatorEpPurpose','CucsFcpoolInitiatorPurpose','CucsFcpoolInitiatorsAssignmentOrder','CucsFcpoolInitiatorsMaxPortsPerNode','CucsFcpoolInitiatorsPurpose','CucsPolicyPolicyOwner','CucsPoolElementOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsFcpoolObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,21))
_CucsFcpoolAddrTable_Object=MibTable
cucsFcpoolAddrTable=_CucsFcpoolAddrTable_Object((1,3,6,1,4,1,9,9,719,1,21,1))
if mibBuilder.loadTexts:cucsFcpoolAddrTable.setStatus(_A)
_CucsFcpoolAddrEntry_Object=MibTableRow
cucsFcpoolAddrEntry=_CucsFcpoolAddrEntry_Object((1,3,6,1,4,1,9,9,719,1,21,1,1))
cucsFcpoolAddrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsFcpoolAddrEntry.setStatus(_A)
_CucsFcpoolAddrInstanceId_Type=CucsManagedObjectId
_CucsFcpoolAddrInstanceId_Object=MibTableColumn
cucsFcpoolAddrInstanceId=_CucsFcpoolAddrInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,1),_CucsFcpoolAddrInstanceId_Type())
cucsFcpoolAddrInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolAddrInstanceId.setStatus(_A)
_CucsFcpoolAddrDn_Type=CucsManagedObjectDn
_CucsFcpoolAddrDn_Object=MibTableColumn
cucsFcpoolAddrDn=_CucsFcpoolAddrDn_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,2),_CucsFcpoolAddrDn_Type())
cucsFcpoolAddrDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrDn.setStatus(_A)
_CucsFcpoolAddrRn_Type=SnmpAdminString
_CucsFcpoolAddrRn_Object=MibTableColumn
cucsFcpoolAddrRn=_CucsFcpoolAddrRn_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,3),_CucsFcpoolAddrRn_Type())
cucsFcpoolAddrRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrRn.setStatus(_A)
_CucsFcpoolAddrAssigned_Type=TruthValue
_CucsFcpoolAddrAssigned_Object=MibTableColumn
cucsFcpoolAddrAssigned=_CucsFcpoolAddrAssigned_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,4),_CucsFcpoolAddrAssigned_Type())
cucsFcpoolAddrAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrAssigned.setStatus(_A)
_CucsFcpoolAddrAssignedToDn_Type=SnmpAdminString
_CucsFcpoolAddrAssignedToDn_Object=MibTableColumn
cucsFcpoolAddrAssignedToDn=_CucsFcpoolAddrAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,5),_CucsFcpoolAddrAssignedToDn_Type())
cucsFcpoolAddrAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrAssignedToDn.setStatus(_A)
_CucsFcpoolAddrId_Type=Unsigned64
_CucsFcpoolAddrId_Object=MibTableColumn
cucsFcpoolAddrId=_CucsFcpoolAddrId_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,6),_CucsFcpoolAddrId_Type())
cucsFcpoolAddrId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrId.setStatus(_A)
_CucsFcpoolAddrOwner_Type=CucsPoolElementOwner
_CucsFcpoolAddrOwner_Object=MibTableColumn
cucsFcpoolAddrOwner=_CucsFcpoolAddrOwner_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,7),_CucsFcpoolAddrOwner_Type())
cucsFcpoolAddrOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrOwner.setStatus(_A)
_CucsFcpoolAddrGlobalAssignedCnt_Type=Gauge32
_CucsFcpoolAddrGlobalAssignedCnt_Object=MibTableColumn
cucsFcpoolAddrGlobalAssignedCnt=_CucsFcpoolAddrGlobalAssignedCnt_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,8),_CucsFcpoolAddrGlobalAssignedCnt_Type())
cucsFcpoolAddrGlobalAssignedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrGlobalAssignedCnt.setStatus(_A)
_CucsFcpoolAddrGlobalDefinedCnt_Type=Gauge32
_CucsFcpoolAddrGlobalDefinedCnt_Object=MibTableColumn
cucsFcpoolAddrGlobalDefinedCnt=_CucsFcpoolAddrGlobalDefinedCnt_Object((1,3,6,1,4,1,9,9,719,1,21,1,1,9),_CucsFcpoolAddrGlobalDefinedCnt_Type())
cucsFcpoolAddrGlobalDefinedCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolAddrGlobalDefinedCnt.setStatus(_A)
_CucsFcpoolBlockTable_Object=MibTable
cucsFcpoolBlockTable=_CucsFcpoolBlockTable_Object((1,3,6,1,4,1,9,9,719,1,21,2))
if mibBuilder.loadTexts:cucsFcpoolBlockTable.setStatus(_A)
_CucsFcpoolBlockEntry_Object=MibTableRow
cucsFcpoolBlockEntry=_CucsFcpoolBlockEntry_Object((1,3,6,1,4,1,9,9,719,1,21,2,1))
cucsFcpoolBlockEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsFcpoolBlockEntry.setStatus(_A)
_CucsFcpoolBlockInstanceId_Type=CucsManagedObjectId
_CucsFcpoolBlockInstanceId_Object=MibTableColumn
cucsFcpoolBlockInstanceId=_CucsFcpoolBlockInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,2,1,1),_CucsFcpoolBlockInstanceId_Type())
cucsFcpoolBlockInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolBlockInstanceId.setStatus(_A)
_CucsFcpoolBlockDn_Type=CucsManagedObjectDn
_CucsFcpoolBlockDn_Object=MibTableColumn
cucsFcpoolBlockDn=_CucsFcpoolBlockDn_Object((1,3,6,1,4,1,9,9,719,1,21,2,1,2),_CucsFcpoolBlockDn_Type())
cucsFcpoolBlockDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBlockDn.setStatus(_A)
_CucsFcpoolBlockRn_Type=SnmpAdminString
_CucsFcpoolBlockRn_Object=MibTableColumn
cucsFcpoolBlockRn=_CucsFcpoolBlockRn_Object((1,3,6,1,4,1,9,9,719,1,21,2,1,3),_CucsFcpoolBlockRn_Type())
cucsFcpoolBlockRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBlockRn.setStatus(_A)
_CucsFcpoolBlockFrom_Type=Unsigned64
_CucsFcpoolBlockFrom_Object=MibTableColumn
cucsFcpoolBlockFrom=_CucsFcpoolBlockFrom_Object((1,3,6,1,4,1,9,9,719,1,21,2,1,4),_CucsFcpoolBlockFrom_Type())
cucsFcpoolBlockFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBlockFrom.setStatus(_A)
_CucsFcpoolBlockTo_Type=Unsigned64
_CucsFcpoolBlockTo_Object=MibTableColumn
cucsFcpoolBlockTo=_CucsFcpoolBlockTo_Object((1,3,6,1,4,1,9,9,719,1,21,2,1,5),_CucsFcpoolBlockTo_Type())
cucsFcpoolBlockTo.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBlockTo.setStatus(_A)
_CucsFcpoolBootTargetTable_Object=MibTable
cucsFcpoolBootTargetTable=_CucsFcpoolBootTargetTable_Object((1,3,6,1,4,1,9,9,719,1,21,3))
if mibBuilder.loadTexts:cucsFcpoolBootTargetTable.setStatus(_A)
_CucsFcpoolBootTargetEntry_Object=MibTableRow
cucsFcpoolBootTargetEntry=_CucsFcpoolBootTargetEntry_Object((1,3,6,1,4,1,9,9,719,1,21,3,1))
cucsFcpoolBootTargetEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsFcpoolBootTargetEntry.setStatus(_A)
_CucsFcpoolBootTargetInstanceId_Type=CucsManagedObjectId
_CucsFcpoolBootTargetInstanceId_Object=MibTableColumn
cucsFcpoolBootTargetInstanceId=_CucsFcpoolBootTargetInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,3,1,1),_CucsFcpoolBootTargetInstanceId_Type())
cucsFcpoolBootTargetInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolBootTargetInstanceId.setStatus(_A)
_CucsFcpoolBootTargetDn_Type=CucsManagedObjectDn
_CucsFcpoolBootTargetDn_Object=MibTableColumn
cucsFcpoolBootTargetDn=_CucsFcpoolBootTargetDn_Object((1,3,6,1,4,1,9,9,719,1,21,3,1,2),_CucsFcpoolBootTargetDn_Type())
cucsFcpoolBootTargetDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBootTargetDn.setStatus(_A)
_CucsFcpoolBootTargetRn_Type=SnmpAdminString
_CucsFcpoolBootTargetRn_Object=MibTableColumn
cucsFcpoolBootTargetRn=_CucsFcpoolBootTargetRn_Object((1,3,6,1,4,1,9,9,719,1,21,3,1,3),_CucsFcpoolBootTargetRn_Type())
cucsFcpoolBootTargetRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBootTargetRn.setStatus(_A)
_CucsFcpoolBootTargetLun_Type=SnmpAdminString
_CucsFcpoolBootTargetLun_Object=MibTableColumn
cucsFcpoolBootTargetLun=_CucsFcpoolBootTargetLun_Object((1,3,6,1,4,1,9,9,719,1,21,3,1,4),_CucsFcpoolBootTargetLun_Type())
cucsFcpoolBootTargetLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBootTargetLun.setStatus(_A)
_CucsFcpoolBootTargetType_Type=CucsFcpoolBootTargetType
_CucsFcpoolBootTargetType_Object=MibTableColumn
cucsFcpoolBootTargetType=_CucsFcpoolBootTargetType_Object((1,3,6,1,4,1,9,9,719,1,21,3,1,5),_CucsFcpoolBootTargetType_Type())
cucsFcpoolBootTargetType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBootTargetType.setStatus(_A)
_CucsFcpoolBootTargetWwn_Type=Unsigned64
_CucsFcpoolBootTargetWwn_Object=MibTableColumn
cucsFcpoolBootTargetWwn=_CucsFcpoolBootTargetWwn_Object((1,3,6,1,4,1,9,9,719,1,21,3,1,6),_CucsFcpoolBootTargetWwn_Type())
cucsFcpoolBootTargetWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolBootTargetWwn.setStatus(_A)
_CucsFcpoolFormatTable_Object=MibTable
cucsFcpoolFormatTable=_CucsFcpoolFormatTable_Object((1,3,6,1,4,1,9,9,719,1,21,4))
if mibBuilder.loadTexts:cucsFcpoolFormatTable.setStatus(_A)
_CucsFcpoolFormatEntry_Object=MibTableRow
cucsFcpoolFormatEntry=_CucsFcpoolFormatEntry_Object((1,3,6,1,4,1,9,9,719,1,21,4,1))
cucsFcpoolFormatEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsFcpoolFormatEntry.setStatus(_A)
_CucsFcpoolFormatInstanceId_Type=CucsManagedObjectId
_CucsFcpoolFormatInstanceId_Object=MibTableColumn
cucsFcpoolFormatInstanceId=_CucsFcpoolFormatInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,4,1,1),_CucsFcpoolFormatInstanceId_Type())
cucsFcpoolFormatInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolFormatInstanceId.setStatus(_A)
_CucsFcpoolFormatDn_Type=CucsManagedObjectDn
_CucsFcpoolFormatDn_Object=MibTableColumn
cucsFcpoolFormatDn=_CucsFcpoolFormatDn_Object((1,3,6,1,4,1,9,9,719,1,21,4,1,2),_CucsFcpoolFormatDn_Type())
cucsFcpoolFormatDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolFormatDn.setStatus(_A)
_CucsFcpoolFormatRn_Type=SnmpAdminString
_CucsFcpoolFormatRn_Object=MibTableColumn
cucsFcpoolFormatRn=_CucsFcpoolFormatRn_Object((1,3,6,1,4,1,9,9,719,1,21,4,1,3),_CucsFcpoolFormatRn_Type())
cucsFcpoolFormatRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolFormatRn.setStatus(_A)
_CucsFcpoolFormatFormat_Type=Unsigned64
_CucsFcpoolFormatFormat_Object=MibTableColumn
cucsFcpoolFormatFormat=_CucsFcpoolFormatFormat_Object((1,3,6,1,4,1,9,9,719,1,21,4,1,4),_CucsFcpoolFormatFormat_Type())
cucsFcpoolFormatFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolFormatFormat.setStatus(_A)
_CucsFcpoolFormatMask_Type=CucsAddressWWNMask
_CucsFcpoolFormatMask_Object=MibTableColumn
cucsFcpoolFormatMask=_CucsFcpoolFormatMask_Object((1,3,6,1,4,1,9,9,719,1,21,4,1,5),_CucsFcpoolFormatMask_Type())
cucsFcpoolFormatMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolFormatMask.setStatus(_A)
_CucsFcpoolInitiatorTable_Object=MibTable
cucsFcpoolInitiatorTable=_CucsFcpoolInitiatorTable_Object((1,3,6,1,4,1,9,9,719,1,21,5))
if mibBuilder.loadTexts:cucsFcpoolInitiatorTable.setStatus(_A)
_CucsFcpoolInitiatorEntry_Object=MibTableRow
cucsFcpoolInitiatorEntry=_CucsFcpoolInitiatorEntry_Object((1,3,6,1,4,1,9,9,719,1,21,5,1))
cucsFcpoolInitiatorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsFcpoolInitiatorEntry.setStatus(_A)
_CucsFcpoolInitiatorInstanceId_Type=CucsManagedObjectId
_CucsFcpoolInitiatorInstanceId_Object=MibTableColumn
cucsFcpoolInitiatorInstanceId=_CucsFcpoolInitiatorInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,1),_CucsFcpoolInitiatorInstanceId_Type())
cucsFcpoolInitiatorInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolInitiatorInstanceId.setStatus(_A)
_CucsFcpoolInitiatorDn_Type=CucsManagedObjectDn
_CucsFcpoolInitiatorDn_Object=MibTableColumn
cucsFcpoolInitiatorDn=_CucsFcpoolInitiatorDn_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,2),_CucsFcpoolInitiatorDn_Type())
cucsFcpoolInitiatorDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorDn.setStatus(_A)
_CucsFcpoolInitiatorRn_Type=SnmpAdminString
_CucsFcpoolInitiatorRn_Object=MibTableColumn
cucsFcpoolInitiatorRn=_CucsFcpoolInitiatorRn_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,3),_CucsFcpoolInitiatorRn_Type())
cucsFcpoolInitiatorRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorRn.setStatus(_A)
_CucsFcpoolInitiatorAssigned_Type=TruthValue
_CucsFcpoolInitiatorAssigned_Object=MibTableColumn
cucsFcpoolInitiatorAssigned=_CucsFcpoolInitiatorAssigned_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,4),_CucsFcpoolInitiatorAssigned_Type())
cucsFcpoolInitiatorAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorAssigned.setStatus(_A)
_CucsFcpoolInitiatorAssignedToDn_Type=SnmpAdminString
_CucsFcpoolInitiatorAssignedToDn_Object=MibTableColumn
cucsFcpoolInitiatorAssignedToDn=_CucsFcpoolInitiatorAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,5),_CucsFcpoolInitiatorAssignedToDn_Type())
cucsFcpoolInitiatorAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorAssignedToDn.setStatus(_A)
_CucsFcpoolInitiatorDescr_Type=SnmpAdminString
_CucsFcpoolInitiatorDescr_Object=MibTableColumn
cucsFcpoolInitiatorDescr=_CucsFcpoolInitiatorDescr_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,6),_CucsFcpoolInitiatorDescr_Type())
cucsFcpoolInitiatorDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorDescr.setStatus(_A)
_CucsFcpoolInitiatorId_Type=Unsigned64
_CucsFcpoolInitiatorId_Object=MibTableColumn
cucsFcpoolInitiatorId=_CucsFcpoolInitiatorId_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,7),_CucsFcpoolInitiatorId_Type())
cucsFcpoolInitiatorId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorId.setStatus(_A)
_CucsFcpoolInitiatorName_Type=SnmpAdminString
_CucsFcpoolInitiatorName_Object=MibTableColumn
cucsFcpoolInitiatorName=_CucsFcpoolInitiatorName_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,8),_CucsFcpoolInitiatorName_Type())
cucsFcpoolInitiatorName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorName.setStatus(_A)
_CucsFcpoolInitiatorPoolableDn_Type=SnmpAdminString
_CucsFcpoolInitiatorPoolableDn_Object=MibTableColumn
cucsFcpoolInitiatorPoolableDn=_CucsFcpoolInitiatorPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,9),_CucsFcpoolInitiatorPoolableDn_Type())
cucsFcpoolInitiatorPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorPoolableDn.setStatus(_A)
_CucsFcpoolInitiatorPrevAssignedToDn_Type=SnmpAdminString
_CucsFcpoolInitiatorPrevAssignedToDn_Object=MibTableColumn
cucsFcpoolInitiatorPrevAssignedToDn=_CucsFcpoolInitiatorPrevAssignedToDn_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,10),_CucsFcpoolInitiatorPrevAssignedToDn_Type())
cucsFcpoolInitiatorPrevAssignedToDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorPrevAssignedToDn.setStatus(_A)
_CucsFcpoolInitiatorPurpose_Type=CucsFcpoolInitiatorPurpose
_CucsFcpoolInitiatorPurpose_Object=MibTableColumn
cucsFcpoolInitiatorPurpose=_CucsFcpoolInitiatorPurpose_Object((1,3,6,1,4,1,9,9,719,1,21,5,1,11),_CucsFcpoolInitiatorPurpose_Type())
cucsFcpoolInitiatorPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorPurpose.setStatus(_A)
_CucsFcpoolInitiatorsTable_Object=MibTable
cucsFcpoolInitiatorsTable=_CucsFcpoolInitiatorsTable_Object((1,3,6,1,4,1,9,9,719,1,21,6))
if mibBuilder.loadTexts:cucsFcpoolInitiatorsTable.setStatus(_A)
_CucsFcpoolInitiatorsEntry_Object=MibTableRow
cucsFcpoolInitiatorsEntry=_CucsFcpoolInitiatorsEntry_Object((1,3,6,1,4,1,9,9,719,1,21,6,1))
cucsFcpoolInitiatorsEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsFcpoolInitiatorsEntry.setStatus(_A)
_CucsFcpoolInitiatorsInstanceId_Type=CucsManagedObjectId
_CucsFcpoolInitiatorsInstanceId_Object=MibTableColumn
cucsFcpoolInitiatorsInstanceId=_CucsFcpoolInitiatorsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,1),_CucsFcpoolInitiatorsInstanceId_Type())
cucsFcpoolInitiatorsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsInstanceId.setStatus(_A)
_CucsFcpoolInitiatorsDn_Type=CucsManagedObjectDn
_CucsFcpoolInitiatorsDn_Object=MibTableColumn
cucsFcpoolInitiatorsDn=_CucsFcpoolInitiatorsDn_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,2),_CucsFcpoolInitiatorsDn_Type())
cucsFcpoolInitiatorsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsDn.setStatus(_A)
_CucsFcpoolInitiatorsRn_Type=SnmpAdminString
_CucsFcpoolInitiatorsRn_Object=MibTableColumn
cucsFcpoolInitiatorsRn=_CucsFcpoolInitiatorsRn_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,3),_CucsFcpoolInitiatorsRn_Type())
cucsFcpoolInitiatorsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsRn.setStatus(_A)
_CucsFcpoolInitiatorsAssigned_Type=Gauge32
_CucsFcpoolInitiatorsAssigned_Object=MibTableColumn
cucsFcpoolInitiatorsAssigned=_CucsFcpoolInitiatorsAssigned_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,4),_CucsFcpoolInitiatorsAssigned_Type())
cucsFcpoolInitiatorsAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsAssigned.setStatus(_A)
_CucsFcpoolInitiatorsDescr_Type=SnmpAdminString
_CucsFcpoolInitiatorsDescr_Object=MibTableColumn
cucsFcpoolInitiatorsDescr=_CucsFcpoolInitiatorsDescr_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,5),_CucsFcpoolInitiatorsDescr_Type())
cucsFcpoolInitiatorsDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsDescr.setStatus(_A)
_CucsFcpoolInitiatorsIntId_Type=SnmpAdminString
_CucsFcpoolInitiatorsIntId_Object=MibTableColumn
cucsFcpoolInitiatorsIntId=_CucsFcpoolInitiatorsIntId_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,6),_CucsFcpoolInitiatorsIntId_Type())
cucsFcpoolInitiatorsIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsIntId.setStatus(_A)
_CucsFcpoolInitiatorsName_Type=SnmpAdminString
_CucsFcpoolInitiatorsName_Object=MibTableColumn
cucsFcpoolInitiatorsName=_CucsFcpoolInitiatorsName_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,7),_CucsFcpoolInitiatorsName_Type())
cucsFcpoolInitiatorsName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsName.setStatus(_A)
_CucsFcpoolInitiatorsPurpose_Type=CucsFcpoolInitiatorsPurpose
_CucsFcpoolInitiatorsPurpose_Object=MibTableColumn
cucsFcpoolInitiatorsPurpose=_CucsFcpoolInitiatorsPurpose_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,8),_CucsFcpoolInitiatorsPurpose_Type())
cucsFcpoolInitiatorsPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsPurpose.setStatus(_A)
_CucsFcpoolInitiatorsSize_Type=Gauge32
_CucsFcpoolInitiatorsSize_Object=MibTableColumn
cucsFcpoolInitiatorsSize=_CucsFcpoolInitiatorsSize_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,9),_CucsFcpoolInitiatorsSize_Type())
cucsFcpoolInitiatorsSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsSize.setStatus(_A)
_CucsFcpoolInitiatorsAssignmentOrder_Type=CucsFcpoolInitiatorsAssignmentOrder
_CucsFcpoolInitiatorsAssignmentOrder_Object=MibTableColumn
cucsFcpoolInitiatorsAssignmentOrder=_CucsFcpoolInitiatorsAssignmentOrder_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,10),_CucsFcpoolInitiatorsAssignmentOrder_Type())
cucsFcpoolInitiatorsAssignmentOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsAssignmentOrder.setStatus(_A)
_CucsFcpoolInitiatorsMaxPortsPerNode_Type=CucsFcpoolInitiatorsMaxPortsPerNode
_CucsFcpoolInitiatorsMaxPortsPerNode_Object=MibTableColumn
cucsFcpoolInitiatorsMaxPortsPerNode=_CucsFcpoolInitiatorsMaxPortsPerNode_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,11),_CucsFcpoolInitiatorsMaxPortsPerNode_Type())
cucsFcpoolInitiatorsMaxPortsPerNode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsMaxPortsPerNode.setStatus(_A)
_CucsFcpoolInitiatorsPolicyLevel_Type=Gauge32
_CucsFcpoolInitiatorsPolicyLevel_Object=MibTableColumn
cucsFcpoolInitiatorsPolicyLevel=_CucsFcpoolInitiatorsPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,12),_CucsFcpoolInitiatorsPolicyLevel_Type())
cucsFcpoolInitiatorsPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsPolicyLevel.setStatus(_A)
_CucsFcpoolInitiatorsPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsFcpoolInitiatorsPolicyOwner_Object=MibTableColumn
cucsFcpoolInitiatorsPolicyOwner=_CucsFcpoolInitiatorsPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,21,6,1,13),_CucsFcpoolInitiatorsPolicyOwner_Type())
cucsFcpoolInitiatorsPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorsPolicyOwner.setStatus(_A)
_CucsFcpoolPoolableTable_Object=MibTable
cucsFcpoolPoolableTable=_CucsFcpoolPoolableTable_Object((1,3,6,1,4,1,9,9,719,1,21,7))
if mibBuilder.loadTexts:cucsFcpoolPoolableTable.setStatus(_A)
_CucsFcpoolPoolableEntry_Object=MibTableRow
cucsFcpoolPoolableEntry=_CucsFcpoolPoolableEntry_Object((1,3,6,1,4,1,9,9,719,1,21,7,1))
cucsFcpoolPoolableEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsFcpoolPoolableEntry.setStatus(_A)
_CucsFcpoolPoolableInstanceId_Type=CucsManagedObjectId
_CucsFcpoolPoolableInstanceId_Object=MibTableColumn
cucsFcpoolPoolableInstanceId=_CucsFcpoolPoolableInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,7,1,1),_CucsFcpoolPoolableInstanceId_Type())
cucsFcpoolPoolableInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolPoolableInstanceId.setStatus(_A)
_CucsFcpoolPoolableDn_Type=CucsManagedObjectDn
_CucsFcpoolPoolableDn_Object=MibTableColumn
cucsFcpoolPoolableDn=_CucsFcpoolPoolableDn_Object((1,3,6,1,4,1,9,9,719,1,21,7,1,2),_CucsFcpoolPoolableDn_Type())
cucsFcpoolPoolableDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolPoolableDn.setStatus(_A)
_CucsFcpoolPoolableRn_Type=SnmpAdminString
_CucsFcpoolPoolableRn_Object=MibTableColumn
cucsFcpoolPoolableRn=_CucsFcpoolPoolableRn_Object((1,3,6,1,4,1,9,9,719,1,21,7,1,3),_CucsFcpoolPoolableRn_Type())
cucsFcpoolPoolableRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolPoolableRn.setStatus(_A)
_CucsFcpoolPoolableId_Type=Unsigned64
_CucsFcpoolPoolableId_Object=MibTableColumn
cucsFcpoolPoolableId=_CucsFcpoolPoolableId_Object((1,3,6,1,4,1,9,9,719,1,21,7,1,4),_CucsFcpoolPoolableId_Type())
cucsFcpoolPoolableId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolPoolableId.setStatus(_A)
_CucsFcpoolPoolablePoolDn_Type=SnmpAdminString
_CucsFcpoolPoolablePoolDn_Object=MibTableColumn
cucsFcpoolPoolablePoolDn=_CucsFcpoolPoolablePoolDn_Object((1,3,6,1,4,1,9,9,719,1,21,7,1,5),_CucsFcpoolPoolablePoolDn_Type())
cucsFcpoolPoolablePoolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolPoolablePoolDn.setStatus(_A)
_CucsFcpoolUniverseTable_Object=MibTable
cucsFcpoolUniverseTable=_CucsFcpoolUniverseTable_Object((1,3,6,1,4,1,9,9,719,1,21,8))
if mibBuilder.loadTexts:cucsFcpoolUniverseTable.setStatus(_A)
_CucsFcpoolUniverseEntry_Object=MibTableRow
cucsFcpoolUniverseEntry=_CucsFcpoolUniverseEntry_Object((1,3,6,1,4,1,9,9,719,1,21,8,1))
cucsFcpoolUniverseEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsFcpoolUniverseEntry.setStatus(_A)
_CucsFcpoolUniverseInstanceId_Type=CucsManagedObjectId
_CucsFcpoolUniverseInstanceId_Object=MibTableColumn
cucsFcpoolUniverseInstanceId=_CucsFcpoolUniverseInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,8,1,1),_CucsFcpoolUniverseInstanceId_Type())
cucsFcpoolUniverseInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolUniverseInstanceId.setStatus(_A)
_CucsFcpoolUniverseDn_Type=CucsManagedObjectDn
_CucsFcpoolUniverseDn_Object=MibTableColumn
cucsFcpoolUniverseDn=_CucsFcpoolUniverseDn_Object((1,3,6,1,4,1,9,9,719,1,21,8,1,2),_CucsFcpoolUniverseDn_Type())
cucsFcpoolUniverseDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolUniverseDn.setStatus(_A)
_CucsFcpoolUniverseRn_Type=SnmpAdminString
_CucsFcpoolUniverseRn_Object=MibTableColumn
cucsFcpoolUniverseRn=_CucsFcpoolUniverseRn_Object((1,3,6,1,4,1,9,9,719,1,21,8,1,3),_CucsFcpoolUniverseRn_Type())
cucsFcpoolUniverseRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolUniverseRn.setStatus(_A)
_CucsFcpoolInitiatorEpTable_Object=MibTable
cucsFcpoolInitiatorEpTable=_CucsFcpoolInitiatorEpTable_Object((1,3,6,1,4,1,9,9,719,1,21,9))
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpTable.setStatus(_A)
_CucsFcpoolInitiatorEpEntry_Object=MibTableRow
cucsFcpoolInitiatorEpEntry=_CucsFcpoolInitiatorEpEntry_Object((1,3,6,1,4,1,9,9,719,1,21,9,1))
cucsFcpoolInitiatorEpEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpEntry.setStatus(_A)
_CucsFcpoolInitiatorEpInstanceId_Type=CucsManagedObjectId
_CucsFcpoolInitiatorEpInstanceId_Object=MibTableColumn
cucsFcpoolInitiatorEpInstanceId=_CucsFcpoolInitiatorEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,21,9,1,1),_CucsFcpoolInitiatorEpInstanceId_Type())
cucsFcpoolInitiatorEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpInstanceId.setStatus(_A)
_CucsFcpoolInitiatorEpDn_Type=CucsManagedObjectDn
_CucsFcpoolInitiatorEpDn_Object=MibTableColumn
cucsFcpoolInitiatorEpDn=_CucsFcpoolInitiatorEpDn_Object((1,3,6,1,4,1,9,9,719,1,21,9,1,2),_CucsFcpoolInitiatorEpDn_Type())
cucsFcpoolInitiatorEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpDn.setStatus(_A)
_CucsFcpoolInitiatorEpRn_Type=SnmpAdminString
_CucsFcpoolInitiatorEpRn_Object=MibTableColumn
cucsFcpoolInitiatorEpRn=_CucsFcpoolInitiatorEpRn_Object((1,3,6,1,4,1,9,9,719,1,21,9,1,3),_CucsFcpoolInitiatorEpRn_Type())
cucsFcpoolInitiatorEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpRn.setStatus(_A)
_CucsFcpoolInitiatorEpId_Type=Unsigned64
_CucsFcpoolInitiatorEpId_Object=MibTableColumn
cucsFcpoolInitiatorEpId=_CucsFcpoolInitiatorEpId_Object((1,3,6,1,4,1,9,9,719,1,21,9,1,4),_CucsFcpoolInitiatorEpId_Type())
cucsFcpoolInitiatorEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpId.setStatus(_A)
_CucsFcpoolInitiatorEpInitiatorDn_Type=SnmpAdminString
_CucsFcpoolInitiatorEpInitiatorDn_Object=MibTableColumn
cucsFcpoolInitiatorEpInitiatorDn=_CucsFcpoolInitiatorEpInitiatorDn_Object((1,3,6,1,4,1,9,9,719,1,21,9,1,5),_CucsFcpoolInitiatorEpInitiatorDn_Type())
cucsFcpoolInitiatorEpInitiatorDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpInitiatorDn.setStatus(_A)
_CucsFcpoolInitiatorEpPurpose_Type=CucsFcpoolInitiatorEpPurpose
_CucsFcpoolInitiatorEpPurpose_Object=MibTableColumn
cucsFcpoolInitiatorEpPurpose=_CucsFcpoolInitiatorEpPurpose_Object((1,3,6,1,4,1,9,9,719,1,21,9,1,6),_CucsFcpoolInitiatorEpPurpose_Type())
cucsFcpoolInitiatorEpPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsFcpoolInitiatorEpPurpose.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsFcpoolObjects':cucsFcpoolObjects,'cucsFcpoolAddrTable':cucsFcpoolAddrTable,'cucsFcpoolAddrEntry':cucsFcpoolAddrEntry,_E:cucsFcpoolAddrInstanceId,'cucsFcpoolAddrDn':cucsFcpoolAddrDn,'cucsFcpoolAddrRn':cucsFcpoolAddrRn,'cucsFcpoolAddrAssigned':cucsFcpoolAddrAssigned,'cucsFcpoolAddrAssignedToDn':cucsFcpoolAddrAssignedToDn,'cucsFcpoolAddrId':cucsFcpoolAddrId,'cucsFcpoolAddrOwner':cucsFcpoolAddrOwner,'cucsFcpoolAddrGlobalAssignedCnt':cucsFcpoolAddrGlobalAssignedCnt,'cucsFcpoolAddrGlobalDefinedCnt':cucsFcpoolAddrGlobalDefinedCnt,'cucsFcpoolBlockTable':cucsFcpoolBlockTable,'cucsFcpoolBlockEntry':cucsFcpoolBlockEntry,_F:cucsFcpoolBlockInstanceId,'cucsFcpoolBlockDn':cucsFcpoolBlockDn,'cucsFcpoolBlockRn':cucsFcpoolBlockRn,'cucsFcpoolBlockFrom':cucsFcpoolBlockFrom,'cucsFcpoolBlockTo':cucsFcpoolBlockTo,'cucsFcpoolBootTargetTable':cucsFcpoolBootTargetTable,'cucsFcpoolBootTargetEntry':cucsFcpoolBootTargetEntry,_G:cucsFcpoolBootTargetInstanceId,'cucsFcpoolBootTargetDn':cucsFcpoolBootTargetDn,'cucsFcpoolBootTargetRn':cucsFcpoolBootTargetRn,'cucsFcpoolBootTargetLun':cucsFcpoolBootTargetLun,'cucsFcpoolBootTargetType':cucsFcpoolBootTargetType,'cucsFcpoolBootTargetWwn':cucsFcpoolBootTargetWwn,'cucsFcpoolFormatTable':cucsFcpoolFormatTable,'cucsFcpoolFormatEntry':cucsFcpoolFormatEntry,_H:cucsFcpoolFormatInstanceId,'cucsFcpoolFormatDn':cucsFcpoolFormatDn,'cucsFcpoolFormatRn':cucsFcpoolFormatRn,'cucsFcpoolFormatFormat':cucsFcpoolFormatFormat,'cucsFcpoolFormatMask':cucsFcpoolFormatMask,'cucsFcpoolInitiatorTable':cucsFcpoolInitiatorTable,'cucsFcpoolInitiatorEntry':cucsFcpoolInitiatorEntry,_I:cucsFcpoolInitiatorInstanceId,'cucsFcpoolInitiatorDn':cucsFcpoolInitiatorDn,'cucsFcpoolInitiatorRn':cucsFcpoolInitiatorRn,'cucsFcpoolInitiatorAssigned':cucsFcpoolInitiatorAssigned,'cucsFcpoolInitiatorAssignedToDn':cucsFcpoolInitiatorAssignedToDn,'cucsFcpoolInitiatorDescr':cucsFcpoolInitiatorDescr,'cucsFcpoolInitiatorId':cucsFcpoolInitiatorId,'cucsFcpoolInitiatorName':cucsFcpoolInitiatorName,'cucsFcpoolInitiatorPoolableDn':cucsFcpoolInitiatorPoolableDn,'cucsFcpoolInitiatorPrevAssignedToDn':cucsFcpoolInitiatorPrevAssignedToDn,'cucsFcpoolInitiatorPurpose':cucsFcpoolInitiatorPurpose,'cucsFcpoolInitiatorsTable':cucsFcpoolInitiatorsTable,'cucsFcpoolInitiatorsEntry':cucsFcpoolInitiatorsEntry,_J:cucsFcpoolInitiatorsInstanceId,'cucsFcpoolInitiatorsDn':cucsFcpoolInitiatorsDn,'cucsFcpoolInitiatorsRn':cucsFcpoolInitiatorsRn,'cucsFcpoolInitiatorsAssigned':cucsFcpoolInitiatorsAssigned,'cucsFcpoolInitiatorsDescr':cucsFcpoolInitiatorsDescr,'cucsFcpoolInitiatorsIntId':cucsFcpoolInitiatorsIntId,'cucsFcpoolInitiatorsName':cucsFcpoolInitiatorsName,'cucsFcpoolInitiatorsPurpose':cucsFcpoolInitiatorsPurpose,'cucsFcpoolInitiatorsSize':cucsFcpoolInitiatorsSize,'cucsFcpoolInitiatorsAssignmentOrder':cucsFcpoolInitiatorsAssignmentOrder,'cucsFcpoolInitiatorsMaxPortsPerNode':cucsFcpoolInitiatorsMaxPortsPerNode,'cucsFcpoolInitiatorsPolicyLevel':cucsFcpoolInitiatorsPolicyLevel,'cucsFcpoolInitiatorsPolicyOwner':cucsFcpoolInitiatorsPolicyOwner,'cucsFcpoolPoolableTable':cucsFcpoolPoolableTable,'cucsFcpoolPoolableEntry':cucsFcpoolPoolableEntry,_K:cucsFcpoolPoolableInstanceId,'cucsFcpoolPoolableDn':cucsFcpoolPoolableDn,'cucsFcpoolPoolableRn':cucsFcpoolPoolableRn,'cucsFcpoolPoolableId':cucsFcpoolPoolableId,'cucsFcpoolPoolablePoolDn':cucsFcpoolPoolablePoolDn,'cucsFcpoolUniverseTable':cucsFcpoolUniverseTable,'cucsFcpoolUniverseEntry':cucsFcpoolUniverseEntry,_L:cucsFcpoolUniverseInstanceId,'cucsFcpoolUniverseDn':cucsFcpoolUniverseDn,'cucsFcpoolUniverseRn':cucsFcpoolUniverseRn,'cucsFcpoolInitiatorEpTable':cucsFcpoolInitiatorEpTable,'cucsFcpoolInitiatorEpEntry':cucsFcpoolInitiatorEpEntry,_M:cucsFcpoolInitiatorEpInstanceId,'cucsFcpoolInitiatorEpDn':cucsFcpoolInitiatorEpDn,'cucsFcpoolInitiatorEpRn':cucsFcpoolInitiatorEpRn,'cucsFcpoolInitiatorEpId':cucsFcpoolInitiatorEpId,'cucsFcpoolInitiatorEpInitiatorDn':cucsFcpoolInitiatorEpInitiatorDn,'cucsFcpoolInitiatorEpPurpose':cucsFcpoolInitiatorEpPurpose})