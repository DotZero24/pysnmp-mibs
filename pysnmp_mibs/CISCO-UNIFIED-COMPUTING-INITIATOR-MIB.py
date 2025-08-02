_M='cucsInitiatorUnitEpInstanceId'
_L='cucsInitiatorStoreEpInstanceId'
_K='cucsInitiatorRequestorGrpEpInstanceId'
_J='cucsInitiatorRequestorEpInstanceId'
_I='cucsInitiatorMemberEpInstanceId'
_H='cucsInitiatorLunEpInstanceId'
_G='cucsInitiatorIScsiInitiatorEpInstanceId'
_F='cucsInitiatorGroupEpInstanceId'
_E='cucsInitiatorFcInitiatorEpInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-INITIATOR-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsFsmLifecycle,CucsInitiatorFcInitiatorEpProt,CucsInitiatorGroupType,CucsInitiatorIScsiInitiatorEpProt,CucsInitiatorInitiatorEpPref,CucsStorageAllocState,CucsStoragePathHA,CucsStorageProtocol=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsFsmLifecycle','CucsInitiatorFcInitiatorEpProt','CucsInitiatorGroupType','CucsInitiatorIScsiInitiatorEpProt','CucsInitiatorInitiatorEpPref','CucsStorageAllocState','CucsStoragePathHA','CucsStorageProtocol')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsInitiatorObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,65))
_CucsInitiatorFcInitiatorEpTable_Object=MibTable
cucsInitiatorFcInitiatorEpTable=_CucsInitiatorFcInitiatorEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,1))
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpTable.setStatus(_A)
_CucsInitiatorFcInitiatorEpEntry_Object=MibTableRow
cucsInitiatorFcInitiatorEpEntry=_CucsInitiatorFcInitiatorEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,1,1))
cucsInitiatorFcInitiatorEpEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpEntry.setStatus(_A)
_CucsInitiatorFcInitiatorEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorFcInitiatorEpInstanceId_Object=MibTableColumn
cucsInitiatorFcInitiatorEpInstanceId=_CucsInitiatorFcInitiatorEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,1),_CucsInitiatorFcInitiatorEpInstanceId_Type())
cucsInitiatorFcInitiatorEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpInstanceId.setStatus(_A)
_CucsInitiatorFcInitiatorEpDn_Type=CucsManagedObjectDn
_CucsInitiatorFcInitiatorEpDn_Object=MibTableColumn
cucsInitiatorFcInitiatorEpDn=_CucsInitiatorFcInitiatorEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,2),_CucsInitiatorFcInitiatorEpDn_Type())
cucsInitiatorFcInitiatorEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpDn.setStatus(_A)
_CucsInitiatorFcInitiatorEpRn_Type=SnmpAdminString
_CucsInitiatorFcInitiatorEpRn_Object=MibTableColumn
cucsInitiatorFcInitiatorEpRn=_CucsInitiatorFcInitiatorEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,3),_CucsInitiatorFcInitiatorEpRn_Type())
cucsInitiatorFcInitiatorEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpRn.setStatus(_A)
_CucsInitiatorFcInitiatorEpEpDn_Type=SnmpAdminString
_CucsInitiatorFcInitiatorEpEpDn_Object=MibTableColumn
cucsInitiatorFcInitiatorEpEpDn=_CucsInitiatorFcInitiatorEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,4),_CucsInitiatorFcInitiatorEpEpDn_Type())
cucsInitiatorFcInitiatorEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpEpDn.setStatus(_A)
_CucsInitiatorFcInitiatorEpId_Type=Unsigned64
_CucsInitiatorFcInitiatorEpId_Object=MibTableColumn
cucsInitiatorFcInitiatorEpId=_CucsInitiatorFcInitiatorEpId_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,5),_CucsInitiatorFcInitiatorEpId_Type())
cucsInitiatorFcInitiatorEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpId.setStatus(_A)
_CucsInitiatorFcInitiatorEpName_Type=SnmpAdminString
_CucsInitiatorFcInitiatorEpName_Object=MibTableColumn
cucsInitiatorFcInitiatorEpName=_CucsInitiatorFcInitiatorEpName_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,6),_CucsInitiatorFcInitiatorEpName_Type())
cucsInitiatorFcInitiatorEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpName.setStatus(_A)
_CucsInitiatorFcInitiatorEpPref_Type=CucsInitiatorInitiatorEpPref
_CucsInitiatorFcInitiatorEpPref_Object=MibTableColumn
cucsInitiatorFcInitiatorEpPref=_CucsInitiatorFcInitiatorEpPref_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,7),_CucsInitiatorFcInitiatorEpPref_Type())
cucsInitiatorFcInitiatorEpPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpPref.setStatus(_A)
_CucsInitiatorFcInitiatorEpProt_Type=CucsInitiatorFcInitiatorEpProt
_CucsInitiatorFcInitiatorEpProt_Object=MibTableColumn
cucsInitiatorFcInitiatorEpProt=_CucsInitiatorFcInitiatorEpProt_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,8),_CucsInitiatorFcInitiatorEpProt_Type())
cucsInitiatorFcInitiatorEpProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpProt.setStatus(_A)
_CucsInitiatorFcInitiatorEpWwpn_Type=Unsigned64
_CucsInitiatorFcInitiatorEpWwpn_Object=MibTableColumn
cucsInitiatorFcInitiatorEpWwpn=_CucsInitiatorFcInitiatorEpWwpn_Object((1,3,6,1,4,1,9,9,719,1,65,1,1,9),_CucsInitiatorFcInitiatorEpWwpn_Type())
cucsInitiatorFcInitiatorEpWwpn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorFcInitiatorEpWwpn.setStatus(_A)
_CucsInitiatorGroupEpTable_Object=MibTable
cucsInitiatorGroupEpTable=_CucsInitiatorGroupEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,2))
if mibBuilder.loadTexts:cucsInitiatorGroupEpTable.setStatus(_A)
_CucsInitiatorGroupEpEntry_Object=MibTableRow
cucsInitiatorGroupEpEntry=_CucsInitiatorGroupEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,2,1))
cucsInitiatorGroupEpEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsInitiatorGroupEpEntry.setStatus(_A)
_CucsInitiatorGroupEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorGroupEpInstanceId_Object=MibTableColumn
cucsInitiatorGroupEpInstanceId=_CucsInitiatorGroupEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,1),_CucsInitiatorGroupEpInstanceId_Type())
cucsInitiatorGroupEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorGroupEpInstanceId.setStatus(_A)
_CucsInitiatorGroupEpDn_Type=CucsManagedObjectDn
_CucsInitiatorGroupEpDn_Object=MibTableColumn
cucsInitiatorGroupEpDn=_CucsInitiatorGroupEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,2),_CucsInitiatorGroupEpDn_Type())
cucsInitiatorGroupEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpDn.setStatus(_A)
_CucsInitiatorGroupEpRn_Type=SnmpAdminString
_CucsInitiatorGroupEpRn_Object=MibTableColumn
cucsInitiatorGroupEpRn=_CucsInitiatorGroupEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,3),_CucsInitiatorGroupEpRn_Type())
cucsInitiatorGroupEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpRn.setStatus(_A)
_CucsInitiatorGroupEpEpDn_Type=SnmpAdminString
_CucsInitiatorGroupEpEpDn_Object=MibTableColumn
cucsInitiatorGroupEpEpDn=_CucsInitiatorGroupEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,4),_CucsInitiatorGroupEpEpDn_Type())
cucsInitiatorGroupEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpEpDn.setStatus(_A)
_CucsInitiatorGroupEpId_Type=Gauge32
_CucsInitiatorGroupEpId_Object=MibTableColumn
cucsInitiatorGroupEpId=_CucsInitiatorGroupEpId_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,5),_CucsInitiatorGroupEpId_Type())
cucsInitiatorGroupEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpId.setStatus(_A)
_CucsInitiatorGroupEpLc_Type=CucsFsmLifecycle
_CucsInitiatorGroupEpLc_Object=MibTableColumn
cucsInitiatorGroupEpLc=_CucsInitiatorGroupEpLc_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,6),_CucsInitiatorGroupEpLc_Type())
cucsInitiatorGroupEpLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpLc.setStatus(_A)
_CucsInitiatorGroupEpName_Type=SnmpAdminString
_CucsInitiatorGroupEpName_Object=MibTableColumn
cucsInitiatorGroupEpName=_CucsInitiatorGroupEpName_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,7),_CucsInitiatorGroupEpName_Type())
cucsInitiatorGroupEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpName.setStatus(_A)
_CucsInitiatorGroupEpPolName_Type=SnmpAdminString
_CucsInitiatorGroupEpPolName_Object=MibTableColumn
cucsInitiatorGroupEpPolName=_CucsInitiatorGroupEpPolName_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,8),_CucsInitiatorGroupEpPolName_Type())
cucsInitiatorGroupEpPolName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpPolName.setStatus(_A)
_CucsInitiatorGroupEpRmtDiskCfgName_Type=SnmpAdminString
_CucsInitiatorGroupEpRmtDiskCfgName_Object=MibTableColumn
cucsInitiatorGroupEpRmtDiskCfgName=_CucsInitiatorGroupEpRmtDiskCfgName_Object((1,3,6,1,4,1,9,9,719,1,65,2,1,9),_CucsInitiatorGroupEpRmtDiskCfgName_Type())
cucsInitiatorGroupEpRmtDiskCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorGroupEpRmtDiskCfgName.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpTable_Object=MibTable
cucsInitiatorIScsiInitiatorEpTable=_CucsInitiatorIScsiInitiatorEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,3))
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpTable.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpEntry_Object=MibTableRow
cucsInitiatorIScsiInitiatorEpEntry=_CucsInitiatorIScsiInitiatorEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,3,1))
cucsInitiatorIScsiInitiatorEpEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpEntry.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorIScsiInitiatorEpInstanceId_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpInstanceId=_CucsInitiatorIScsiInitiatorEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,1),_CucsInitiatorIScsiInitiatorEpInstanceId_Type())
cucsInitiatorIScsiInitiatorEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpInstanceId.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpDn_Type=CucsManagedObjectDn
_CucsInitiatorIScsiInitiatorEpDn_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpDn=_CucsInitiatorIScsiInitiatorEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,2),_CucsInitiatorIScsiInitiatorEpDn_Type())
cucsInitiatorIScsiInitiatorEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpDn.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpRn_Type=SnmpAdminString
_CucsInitiatorIScsiInitiatorEpRn_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpRn=_CucsInitiatorIScsiInitiatorEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,3),_CucsInitiatorIScsiInitiatorEpRn_Type())
cucsInitiatorIScsiInitiatorEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpRn.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpEpDn_Type=SnmpAdminString
_CucsInitiatorIScsiInitiatorEpEpDn_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpEpDn=_CucsInitiatorIScsiInitiatorEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,4),_CucsInitiatorIScsiInitiatorEpEpDn_Type())
cucsInitiatorIScsiInitiatorEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpEpDn.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpId_Type=Unsigned64
_CucsInitiatorIScsiInitiatorEpId_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpId=_CucsInitiatorIScsiInitiatorEpId_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,5),_CucsInitiatorIScsiInitiatorEpId_Type())
cucsInitiatorIScsiInitiatorEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpId.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpIqn_Type=SnmpAdminString
_CucsInitiatorIScsiInitiatorEpIqn_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpIqn=_CucsInitiatorIScsiInitiatorEpIqn_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,6),_CucsInitiatorIScsiInitiatorEpIqn_Type())
cucsInitiatorIScsiInitiatorEpIqn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpIqn.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpName_Type=SnmpAdminString
_CucsInitiatorIScsiInitiatorEpName_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpName=_CucsInitiatorIScsiInitiatorEpName_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,7),_CucsInitiatorIScsiInitiatorEpName_Type())
cucsInitiatorIScsiInitiatorEpName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpName.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpPref_Type=CucsInitiatorInitiatorEpPref
_CucsInitiatorIScsiInitiatorEpPref_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpPref=_CucsInitiatorIScsiInitiatorEpPref_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,8),_CucsInitiatorIScsiInitiatorEpPref_Type())
cucsInitiatorIScsiInitiatorEpPref.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpPref.setStatus(_A)
_CucsInitiatorIScsiInitiatorEpProt_Type=CucsInitiatorIScsiInitiatorEpProt
_CucsInitiatorIScsiInitiatorEpProt_Object=MibTableColumn
cucsInitiatorIScsiInitiatorEpProt=_CucsInitiatorIScsiInitiatorEpProt_Object((1,3,6,1,4,1,9,9,719,1,65,3,1,9),_CucsInitiatorIScsiInitiatorEpProt_Type())
cucsInitiatorIScsiInitiatorEpProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorIScsiInitiatorEpProt.setStatus(_A)
_CucsInitiatorLunEpTable_Object=MibTable
cucsInitiatorLunEpTable=_CucsInitiatorLunEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,4))
if mibBuilder.loadTexts:cucsInitiatorLunEpTable.setStatus(_A)
_CucsInitiatorLunEpEntry_Object=MibTableRow
cucsInitiatorLunEpEntry=_CucsInitiatorLunEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,4,1))
cucsInitiatorLunEpEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsInitiatorLunEpEntry.setStatus(_A)
_CucsInitiatorLunEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorLunEpInstanceId_Object=MibTableColumn
cucsInitiatorLunEpInstanceId=_CucsInitiatorLunEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,4,1,1),_CucsInitiatorLunEpInstanceId_Type())
cucsInitiatorLunEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorLunEpInstanceId.setStatus(_A)
_CucsInitiatorLunEpDn_Type=CucsManagedObjectDn
_CucsInitiatorLunEpDn_Object=MibTableColumn
cucsInitiatorLunEpDn=_CucsInitiatorLunEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,4,1,2),_CucsInitiatorLunEpDn_Type())
cucsInitiatorLunEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorLunEpDn.setStatus(_A)
_CucsInitiatorLunEpRn_Type=SnmpAdminString
_CucsInitiatorLunEpRn_Object=MibTableColumn
cucsInitiatorLunEpRn=_CucsInitiatorLunEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,4,1,3),_CucsInitiatorLunEpRn_Type())
cucsInitiatorLunEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorLunEpRn.setStatus(_A)
_CucsInitiatorLunEpBootable_Type=TruthValue
_CucsInitiatorLunEpBootable_Object=MibTableColumn
cucsInitiatorLunEpBootable=_CucsInitiatorLunEpBootable_Object((1,3,6,1,4,1,9,9,719,1,65,4,1,4),_CucsInitiatorLunEpBootable_Type())
cucsInitiatorLunEpBootable.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorLunEpBootable.setStatus(_A)
_CucsInitiatorLunEpEpDn_Type=SnmpAdminString
_CucsInitiatorLunEpEpDn_Object=MibTableColumn
cucsInitiatorLunEpEpDn=_CucsInitiatorLunEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,4,1,5),_CucsInitiatorLunEpEpDn_Type())
cucsInitiatorLunEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorLunEpEpDn.setStatus(_A)
_CucsInitiatorLunEpId_Type=Gauge32
_CucsInitiatorLunEpId_Object=MibTableColumn
cucsInitiatorLunEpId=_CucsInitiatorLunEpId_Object((1,3,6,1,4,1,9,9,719,1,65,4,1,6),_CucsInitiatorLunEpId_Type())
cucsInitiatorLunEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorLunEpId.setStatus(_A)
_CucsInitiatorMemberEpTable_Object=MibTable
cucsInitiatorMemberEpTable=_CucsInitiatorMemberEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,5))
if mibBuilder.loadTexts:cucsInitiatorMemberEpTable.setStatus(_A)
_CucsInitiatorMemberEpEntry_Object=MibTableRow
cucsInitiatorMemberEpEntry=_CucsInitiatorMemberEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,5,1))
cucsInitiatorMemberEpEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsInitiatorMemberEpEntry.setStatus(_A)
_CucsInitiatorMemberEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorMemberEpInstanceId_Object=MibTableColumn
cucsInitiatorMemberEpInstanceId=_CucsInitiatorMemberEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,5,1,1),_CucsInitiatorMemberEpInstanceId_Type())
cucsInitiatorMemberEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorMemberEpInstanceId.setStatus(_A)
_CucsInitiatorMemberEpDn_Type=CucsManagedObjectDn
_CucsInitiatorMemberEpDn_Object=MibTableColumn
cucsInitiatorMemberEpDn=_CucsInitiatorMemberEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,5,1,2),_CucsInitiatorMemberEpDn_Type())
cucsInitiatorMemberEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorMemberEpDn.setStatus(_A)
_CucsInitiatorMemberEpRn_Type=SnmpAdminString
_CucsInitiatorMemberEpRn_Object=MibTableColumn
cucsInitiatorMemberEpRn=_CucsInitiatorMemberEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,5,1,3),_CucsInitiatorMemberEpRn_Type())
cucsInitiatorMemberEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorMemberEpRn.setStatus(_A)
_CucsInitiatorMemberEpEpDn_Type=SnmpAdminString
_CucsInitiatorMemberEpEpDn_Object=MibTableColumn
cucsInitiatorMemberEpEpDn=_CucsInitiatorMemberEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,5,1,4),_CucsInitiatorMemberEpEpDn_Type())
cucsInitiatorMemberEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorMemberEpEpDn.setStatus(_A)
_CucsInitiatorMemberEpId_Type=Gauge32
_CucsInitiatorMemberEpId_Object=MibTableColumn
cucsInitiatorMemberEpId=_CucsInitiatorMemberEpId_Object((1,3,6,1,4,1,9,9,719,1,65,5,1,5),_CucsInitiatorMemberEpId_Type())
cucsInitiatorMemberEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorMemberEpId.setStatus(_A)
_CucsInitiatorRequestorEpTable_Object=MibTable
cucsInitiatorRequestorEpTable=_CucsInitiatorRequestorEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,6))
if mibBuilder.loadTexts:cucsInitiatorRequestorEpTable.setStatus(_A)
_CucsInitiatorRequestorEpEntry_Object=MibTableRow
cucsInitiatorRequestorEpEntry=_CucsInitiatorRequestorEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,6,1))
cucsInitiatorRequestorEpEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsInitiatorRequestorEpEntry.setStatus(_A)
_CucsInitiatorRequestorEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorRequestorEpInstanceId_Object=MibTableColumn
cucsInitiatorRequestorEpInstanceId=_CucsInitiatorRequestorEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,1),_CucsInitiatorRequestorEpInstanceId_Type())
cucsInitiatorRequestorEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpInstanceId.setStatus(_A)
_CucsInitiatorRequestorEpDn_Type=CucsManagedObjectDn
_CucsInitiatorRequestorEpDn_Object=MibTableColumn
cucsInitiatorRequestorEpDn=_CucsInitiatorRequestorEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,2),_CucsInitiatorRequestorEpDn_Type())
cucsInitiatorRequestorEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpDn.setStatus(_A)
_CucsInitiatorRequestorEpRn_Type=SnmpAdminString
_CucsInitiatorRequestorEpRn_Object=MibTableColumn
cucsInitiatorRequestorEpRn=_CucsInitiatorRequestorEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,3),_CucsInitiatorRequestorEpRn_Type())
cucsInitiatorRequestorEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpRn.setStatus(_A)
_CucsInitiatorRequestorEpAllocState_Type=CucsStorageAllocState
_CucsInitiatorRequestorEpAllocState_Object=MibTableColumn
cucsInitiatorRequestorEpAllocState=_CucsInitiatorRequestorEpAllocState_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,4),_CucsInitiatorRequestorEpAllocState_Type())
cucsInitiatorRequestorEpAllocState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpAllocState.setStatus(_A)
_CucsInitiatorRequestorEpEpDn_Type=SnmpAdminString
_CucsInitiatorRequestorEpEpDn_Object=MibTableColumn
cucsInitiatorRequestorEpEpDn=_CucsInitiatorRequestorEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,5),_CucsInitiatorRequestorEpEpDn_Type())
cucsInitiatorRequestorEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpEpDn.setStatus(_A)
_CucsInitiatorRequestorEpId_Type=Gauge32
_CucsInitiatorRequestorEpId_Object=MibTableColumn
cucsInitiatorRequestorEpId=_CucsInitiatorRequestorEpId_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,6),_CucsInitiatorRequestorEpId_Type())
cucsInitiatorRequestorEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpId.setStatus(_A)
_CucsInitiatorRequestorEpSysId_Type=Gauge32
_CucsInitiatorRequestorEpSysId_Object=MibTableColumn
cucsInitiatorRequestorEpSysId=_CucsInitiatorRequestorEpSysId_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,7),_CucsInitiatorRequestorEpSysId_Type())
cucsInitiatorRequestorEpSysId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpSysId.setStatus(_A)
_CucsInitiatorRequestorEpSysName_Type=SnmpAdminString
_CucsInitiatorRequestorEpSysName_Object=MibTableColumn
cucsInitiatorRequestorEpSysName=_CucsInitiatorRequestorEpSysName_Object((1,3,6,1,4,1,9,9,719,1,65,6,1,8),_CucsInitiatorRequestorEpSysName_Type())
cucsInitiatorRequestorEpSysName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorEpSysName.setStatus(_A)
_CucsInitiatorRequestorGrpEpTable_Object=MibTable
cucsInitiatorRequestorGrpEpTable=_CucsInitiatorRequestorGrpEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,7))
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpTable.setStatus(_A)
_CucsInitiatorRequestorGrpEpEntry_Object=MibTableRow
cucsInitiatorRequestorGrpEpEntry=_CucsInitiatorRequestorGrpEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,7,1))
cucsInitiatorRequestorGrpEpEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpEntry.setStatus(_A)
_CucsInitiatorRequestorGrpEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorRequestorGrpEpInstanceId_Object=MibTableColumn
cucsInitiatorRequestorGrpEpInstanceId=_CucsInitiatorRequestorGrpEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,1),_CucsInitiatorRequestorGrpEpInstanceId_Type())
cucsInitiatorRequestorGrpEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpInstanceId.setStatus(_A)
_CucsInitiatorRequestorGrpEpDn_Type=CucsManagedObjectDn
_CucsInitiatorRequestorGrpEpDn_Object=MibTableColumn
cucsInitiatorRequestorGrpEpDn=_CucsInitiatorRequestorGrpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,2),_CucsInitiatorRequestorGrpEpDn_Type())
cucsInitiatorRequestorGrpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpDn.setStatus(_A)
_CucsInitiatorRequestorGrpEpRn_Type=SnmpAdminString
_CucsInitiatorRequestorGrpEpRn_Object=MibTableColumn
cucsInitiatorRequestorGrpEpRn=_CucsInitiatorRequestorGrpEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,3),_CucsInitiatorRequestorGrpEpRn_Type())
cucsInitiatorRequestorGrpEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpRn.setStatus(_A)
_CucsInitiatorRequestorGrpEpAllocState_Type=CucsStorageAllocState
_CucsInitiatorRequestorGrpEpAllocState_Object=MibTableColumn
cucsInitiatorRequestorGrpEpAllocState=_CucsInitiatorRequestorGrpEpAllocState_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,4),_CucsInitiatorRequestorGrpEpAllocState_Type())
cucsInitiatorRequestorGrpEpAllocState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpAllocState.setStatus(_A)
_CucsInitiatorRequestorGrpEpEpDn_Type=SnmpAdminString
_CucsInitiatorRequestorGrpEpEpDn_Object=MibTableColumn
cucsInitiatorRequestorGrpEpEpDn=_CucsInitiatorRequestorGrpEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,5),_CucsInitiatorRequestorGrpEpEpDn_Type())
cucsInitiatorRequestorGrpEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpEpDn.setStatus(_A)
_CucsInitiatorRequestorGrpEpId_Type=Gauge32
_CucsInitiatorRequestorGrpEpId_Object=MibTableColumn
cucsInitiatorRequestorGrpEpId=_CucsInitiatorRequestorGrpEpId_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,6),_CucsInitiatorRequestorGrpEpId_Type())
cucsInitiatorRequestorGrpEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpId.setStatus(_A)
_CucsInitiatorRequestorGrpEpLc_Type=CucsFsmLifecycle
_CucsInitiatorRequestorGrpEpLc_Object=MibTableColumn
cucsInitiatorRequestorGrpEpLc=_CucsInitiatorRequestorGrpEpLc_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,7),_CucsInitiatorRequestorGrpEpLc_Type())
cucsInitiatorRequestorGrpEpLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpLc.setStatus(_A)
_CucsInitiatorRequestorGrpEpPolDn_Type=SnmpAdminString
_CucsInitiatorRequestorGrpEpPolDn_Object=MibTableColumn
cucsInitiatorRequestorGrpEpPolDn=_CucsInitiatorRequestorGrpEpPolDn_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,8),_CucsInitiatorRequestorGrpEpPolDn_Type())
cucsInitiatorRequestorGrpEpPolDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpPolDn.setStatus(_A)
_CucsInitiatorRequestorGrpEpType_Type=CucsInitiatorGroupType
_CucsInitiatorRequestorGrpEpType_Object=MibTableColumn
cucsInitiatorRequestorGrpEpType=_CucsInitiatorRequestorGrpEpType_Object((1,3,6,1,4,1,9,9,719,1,65,7,1,9),_CucsInitiatorRequestorGrpEpType_Type())
cucsInitiatorRequestorGrpEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorRequestorGrpEpType.setStatus(_A)
_CucsInitiatorStoreEpTable_Object=MibTable
cucsInitiatorStoreEpTable=_CucsInitiatorStoreEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,8))
if mibBuilder.loadTexts:cucsInitiatorStoreEpTable.setStatus(_A)
_CucsInitiatorStoreEpEntry_Object=MibTableRow
cucsInitiatorStoreEpEntry=_CucsInitiatorStoreEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,8,1))
cucsInitiatorStoreEpEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsInitiatorStoreEpEntry.setStatus(_A)
_CucsInitiatorStoreEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorStoreEpInstanceId_Object=MibTableColumn
cucsInitiatorStoreEpInstanceId=_CucsInitiatorStoreEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,8,1,1),_CucsInitiatorStoreEpInstanceId_Type())
cucsInitiatorStoreEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorStoreEpInstanceId.setStatus(_A)
_CucsInitiatorStoreEpDn_Type=CucsManagedObjectDn
_CucsInitiatorStoreEpDn_Object=MibTableColumn
cucsInitiatorStoreEpDn=_CucsInitiatorStoreEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,8,1,2),_CucsInitiatorStoreEpDn_Type())
cucsInitiatorStoreEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorStoreEpDn.setStatus(_A)
_CucsInitiatorStoreEpRn_Type=SnmpAdminString
_CucsInitiatorStoreEpRn_Object=MibTableColumn
cucsInitiatorStoreEpRn=_CucsInitiatorStoreEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,8,1,3),_CucsInitiatorStoreEpRn_Type())
cucsInitiatorStoreEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorStoreEpRn.setStatus(_A)
_CucsInitiatorStoreEpEpDn_Type=SnmpAdminString
_CucsInitiatorStoreEpEpDn_Object=MibTableColumn
cucsInitiatorStoreEpEpDn=_CucsInitiatorStoreEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,8,1,4),_CucsInitiatorStoreEpEpDn_Type())
cucsInitiatorStoreEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorStoreEpEpDn.setStatus(_A)
_CucsInitiatorStoreEpId_Type=Gauge32
_CucsInitiatorStoreEpId_Object=MibTableColumn
cucsInitiatorStoreEpId=_CucsInitiatorStoreEpId_Object((1,3,6,1,4,1,9,9,719,1,65,8,1,5),_CucsInitiatorStoreEpId_Type())
cucsInitiatorStoreEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorStoreEpId.setStatus(_A)
_CucsInitiatorStoreEpType_Type=CucsInitiatorGroupType
_CucsInitiatorStoreEpType_Object=MibTableColumn
cucsInitiatorStoreEpType=_CucsInitiatorStoreEpType_Object((1,3,6,1,4,1,9,9,719,1,65,8,1,6),_CucsInitiatorStoreEpType_Type())
cucsInitiatorStoreEpType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorStoreEpType.setStatus(_A)
_CucsInitiatorUnitEpTable_Object=MibTable
cucsInitiatorUnitEpTable=_CucsInitiatorUnitEpTable_Object((1,3,6,1,4,1,9,9,719,1,65,9))
if mibBuilder.loadTexts:cucsInitiatorUnitEpTable.setStatus(_A)
_CucsInitiatorUnitEpEntry_Object=MibTableRow
cucsInitiatorUnitEpEntry=_CucsInitiatorUnitEpEntry_Object((1,3,6,1,4,1,9,9,719,1,65,9,1))
cucsInitiatorUnitEpEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsInitiatorUnitEpEntry.setStatus(_A)
_CucsInitiatorUnitEpInstanceId_Type=CucsManagedObjectId
_CucsInitiatorUnitEpInstanceId_Object=MibTableColumn
cucsInitiatorUnitEpInstanceId=_CucsInitiatorUnitEpInstanceId_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,1),_CucsInitiatorUnitEpInstanceId_Type())
cucsInitiatorUnitEpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsInitiatorUnitEpInstanceId.setStatus(_A)
_CucsInitiatorUnitEpDn_Type=CucsManagedObjectDn
_CucsInitiatorUnitEpDn_Object=MibTableColumn
cucsInitiatorUnitEpDn=_CucsInitiatorUnitEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,2),_CucsInitiatorUnitEpDn_Type())
cucsInitiatorUnitEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpDn.setStatus(_A)
_CucsInitiatorUnitEpRn_Type=SnmpAdminString
_CucsInitiatorUnitEpRn_Object=MibTableColumn
cucsInitiatorUnitEpRn=_CucsInitiatorUnitEpRn_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,3),_CucsInitiatorUnitEpRn_Type())
cucsInitiatorUnitEpRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpRn.setStatus(_A)
_CucsInitiatorUnitEpBoot_Type=TruthValue
_CucsInitiatorUnitEpBoot_Object=MibTableColumn
cucsInitiatorUnitEpBoot=_CucsInitiatorUnitEpBoot_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,4),_CucsInitiatorUnitEpBoot_Type())
cucsInitiatorUnitEpBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpBoot.setStatus(_A)
_CucsInitiatorUnitEpEpDn_Type=SnmpAdminString
_CucsInitiatorUnitEpEpDn_Object=MibTableColumn
cucsInitiatorUnitEpEpDn=_CucsInitiatorUnitEpEpDn_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,5),_CucsInitiatorUnitEpEpDn_Type())
cucsInitiatorUnitEpEpDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpEpDn.setStatus(_A)
_CucsInitiatorUnitEpHa_Type=CucsStoragePathHA
_CucsInitiatorUnitEpHa_Object=MibTableColumn
cucsInitiatorUnitEpHa=_CucsInitiatorUnitEpHa_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,6),_CucsInitiatorUnitEpHa_Type())
cucsInitiatorUnitEpHa.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpHa.setStatus(_A)
_CucsInitiatorUnitEpId_Type=Gauge32
_CucsInitiatorUnitEpId_Object=MibTableColumn
cucsInitiatorUnitEpId=_CucsInitiatorUnitEpId_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,7),_CucsInitiatorUnitEpId_Type())
cucsInitiatorUnitEpId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpId.setStatus(_A)
_CucsInitiatorUnitEpItemDn_Type=SnmpAdminString
_CucsInitiatorUnitEpItemDn_Object=MibTableColumn
cucsInitiatorUnitEpItemDn=_CucsInitiatorUnitEpItemDn_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,8),_CucsInitiatorUnitEpItemDn_Type())
cucsInitiatorUnitEpItemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpItemDn.setStatus(_A)
_CucsInitiatorUnitEpLc_Type=CucsFsmLifecycle
_CucsInitiatorUnitEpLc_Object=MibTableColumn
cucsInitiatorUnitEpLc=_CucsInitiatorUnitEpLc_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,9),_CucsInitiatorUnitEpLc_Type())
cucsInitiatorUnitEpLc.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpLc.setStatus(_A)
_CucsInitiatorUnitEpPhyId_Type=Gauge32
_CucsInitiatorUnitEpPhyId_Object=MibTableColumn
cucsInitiatorUnitEpPhyId=_CucsInitiatorUnitEpPhyId_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,10),_CucsInitiatorUnitEpPhyId_Type())
cucsInitiatorUnitEpPhyId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpPhyId.setStatus(_A)
_CucsInitiatorUnitEpProt_Type=CucsStorageProtocol
_CucsInitiatorUnitEpProt_Object=MibTableColumn
cucsInitiatorUnitEpProt=_CucsInitiatorUnitEpProt_Object((1,3,6,1,4,1,9,9,719,1,65,9,1,11),_CucsInitiatorUnitEpProt_Type())
cucsInitiatorUnitEpProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsInitiatorUnitEpProt.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsInitiatorObjects':cucsInitiatorObjects,'cucsInitiatorFcInitiatorEpTable':cucsInitiatorFcInitiatorEpTable,'cucsInitiatorFcInitiatorEpEntry':cucsInitiatorFcInitiatorEpEntry,_E:cucsInitiatorFcInitiatorEpInstanceId,'cucsInitiatorFcInitiatorEpDn':cucsInitiatorFcInitiatorEpDn,'cucsInitiatorFcInitiatorEpRn':cucsInitiatorFcInitiatorEpRn,'cucsInitiatorFcInitiatorEpEpDn':cucsInitiatorFcInitiatorEpEpDn,'cucsInitiatorFcInitiatorEpId':cucsInitiatorFcInitiatorEpId,'cucsInitiatorFcInitiatorEpName':cucsInitiatorFcInitiatorEpName,'cucsInitiatorFcInitiatorEpPref':cucsInitiatorFcInitiatorEpPref,'cucsInitiatorFcInitiatorEpProt':cucsInitiatorFcInitiatorEpProt,'cucsInitiatorFcInitiatorEpWwpn':cucsInitiatorFcInitiatorEpWwpn,'cucsInitiatorGroupEpTable':cucsInitiatorGroupEpTable,'cucsInitiatorGroupEpEntry':cucsInitiatorGroupEpEntry,_F:cucsInitiatorGroupEpInstanceId,'cucsInitiatorGroupEpDn':cucsInitiatorGroupEpDn,'cucsInitiatorGroupEpRn':cucsInitiatorGroupEpRn,'cucsInitiatorGroupEpEpDn':cucsInitiatorGroupEpEpDn,'cucsInitiatorGroupEpId':cucsInitiatorGroupEpId,'cucsInitiatorGroupEpLc':cucsInitiatorGroupEpLc,'cucsInitiatorGroupEpName':cucsInitiatorGroupEpName,'cucsInitiatorGroupEpPolName':cucsInitiatorGroupEpPolName,'cucsInitiatorGroupEpRmtDiskCfgName':cucsInitiatorGroupEpRmtDiskCfgName,'cucsInitiatorIScsiInitiatorEpTable':cucsInitiatorIScsiInitiatorEpTable,'cucsInitiatorIScsiInitiatorEpEntry':cucsInitiatorIScsiInitiatorEpEntry,_G:cucsInitiatorIScsiInitiatorEpInstanceId,'cucsInitiatorIScsiInitiatorEpDn':cucsInitiatorIScsiInitiatorEpDn,'cucsInitiatorIScsiInitiatorEpRn':cucsInitiatorIScsiInitiatorEpRn,'cucsInitiatorIScsiInitiatorEpEpDn':cucsInitiatorIScsiInitiatorEpEpDn,'cucsInitiatorIScsiInitiatorEpId':cucsInitiatorIScsiInitiatorEpId,'cucsInitiatorIScsiInitiatorEpIqn':cucsInitiatorIScsiInitiatorEpIqn,'cucsInitiatorIScsiInitiatorEpName':cucsInitiatorIScsiInitiatorEpName,'cucsInitiatorIScsiInitiatorEpPref':cucsInitiatorIScsiInitiatorEpPref,'cucsInitiatorIScsiInitiatorEpProt':cucsInitiatorIScsiInitiatorEpProt,'cucsInitiatorLunEpTable':cucsInitiatorLunEpTable,'cucsInitiatorLunEpEntry':cucsInitiatorLunEpEntry,_H:cucsInitiatorLunEpInstanceId,'cucsInitiatorLunEpDn':cucsInitiatorLunEpDn,'cucsInitiatorLunEpRn':cucsInitiatorLunEpRn,'cucsInitiatorLunEpBootable':cucsInitiatorLunEpBootable,'cucsInitiatorLunEpEpDn':cucsInitiatorLunEpEpDn,'cucsInitiatorLunEpId':cucsInitiatorLunEpId,'cucsInitiatorMemberEpTable':cucsInitiatorMemberEpTable,'cucsInitiatorMemberEpEntry':cucsInitiatorMemberEpEntry,_I:cucsInitiatorMemberEpInstanceId,'cucsInitiatorMemberEpDn':cucsInitiatorMemberEpDn,'cucsInitiatorMemberEpRn':cucsInitiatorMemberEpRn,'cucsInitiatorMemberEpEpDn':cucsInitiatorMemberEpEpDn,'cucsInitiatorMemberEpId':cucsInitiatorMemberEpId,'cucsInitiatorRequestorEpTable':cucsInitiatorRequestorEpTable,'cucsInitiatorRequestorEpEntry':cucsInitiatorRequestorEpEntry,_J:cucsInitiatorRequestorEpInstanceId,'cucsInitiatorRequestorEpDn':cucsInitiatorRequestorEpDn,'cucsInitiatorRequestorEpRn':cucsInitiatorRequestorEpRn,'cucsInitiatorRequestorEpAllocState':cucsInitiatorRequestorEpAllocState,'cucsInitiatorRequestorEpEpDn':cucsInitiatorRequestorEpEpDn,'cucsInitiatorRequestorEpId':cucsInitiatorRequestorEpId,'cucsInitiatorRequestorEpSysId':cucsInitiatorRequestorEpSysId,'cucsInitiatorRequestorEpSysName':cucsInitiatorRequestorEpSysName,'cucsInitiatorRequestorGrpEpTable':cucsInitiatorRequestorGrpEpTable,'cucsInitiatorRequestorGrpEpEntry':cucsInitiatorRequestorGrpEpEntry,_K:cucsInitiatorRequestorGrpEpInstanceId,'cucsInitiatorRequestorGrpEpDn':cucsInitiatorRequestorGrpEpDn,'cucsInitiatorRequestorGrpEpRn':cucsInitiatorRequestorGrpEpRn,'cucsInitiatorRequestorGrpEpAllocState':cucsInitiatorRequestorGrpEpAllocState,'cucsInitiatorRequestorGrpEpEpDn':cucsInitiatorRequestorGrpEpEpDn,'cucsInitiatorRequestorGrpEpId':cucsInitiatorRequestorGrpEpId,'cucsInitiatorRequestorGrpEpLc':cucsInitiatorRequestorGrpEpLc,'cucsInitiatorRequestorGrpEpPolDn':cucsInitiatorRequestorGrpEpPolDn,'cucsInitiatorRequestorGrpEpType':cucsInitiatorRequestorGrpEpType,'cucsInitiatorStoreEpTable':cucsInitiatorStoreEpTable,'cucsInitiatorStoreEpEntry':cucsInitiatorStoreEpEntry,_L:cucsInitiatorStoreEpInstanceId,'cucsInitiatorStoreEpDn':cucsInitiatorStoreEpDn,'cucsInitiatorStoreEpRn':cucsInitiatorStoreEpRn,'cucsInitiatorStoreEpEpDn':cucsInitiatorStoreEpEpDn,'cucsInitiatorStoreEpId':cucsInitiatorStoreEpId,'cucsInitiatorStoreEpType':cucsInitiatorStoreEpType,'cucsInitiatorUnitEpTable':cucsInitiatorUnitEpTable,'cucsInitiatorUnitEpEntry':cucsInitiatorUnitEpEntry,_M:cucsInitiatorUnitEpInstanceId,'cucsInitiatorUnitEpDn':cucsInitiatorUnitEpDn,'cucsInitiatorUnitEpRn':cucsInitiatorUnitEpRn,'cucsInitiatorUnitEpBoot':cucsInitiatorUnitEpBoot,'cucsInitiatorUnitEpEpDn':cucsInitiatorUnitEpEpDn,'cucsInitiatorUnitEpHa':cucsInitiatorUnitEpHa,'cucsInitiatorUnitEpId':cucsInitiatorUnitEpId,'cucsInitiatorUnitEpItemDn':cucsInitiatorUnitEpItemDn,'cucsInitiatorUnitEpLc':cucsInitiatorUnitEpLc,'cucsInitiatorUnitEpPhyId':cucsInitiatorUnitEpPhyId,'cucsInitiatorUnitEpProt':cucsInitiatorUnitEpProt})