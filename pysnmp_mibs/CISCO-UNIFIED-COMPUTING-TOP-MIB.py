_J='cucsTopInfoSyncPolicyInstanceId'
_I='cucsTopInfoPolicyInstanceId'
_H='cucsTopSysDefaultsInstanceId'
_G='cucsTopSystemInstanceId'
_F='cucsTopRootInstanceId'
_E='cucsTopMetaInfInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-TOP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsPolicyPolicyOwner,CucsTopInfoPolicyState,CucsTopInfoSyncPolicyState,CucsTopMode=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsPolicyPolicyOwner','CucsTopInfoPolicyState','CucsTopInfoSyncPolicyState','CucsTopMode')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsTopObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,49))
_CucsTopMetaInfTable_Object=MibTable
cucsTopMetaInfTable=_CucsTopMetaInfTable_Object((1,3,6,1,4,1,9,9,719,1,49,1))
if mibBuilder.loadTexts:cucsTopMetaInfTable.setStatus(_A)
_CucsTopMetaInfEntry_Object=MibTableRow
cucsTopMetaInfEntry=_CucsTopMetaInfEntry_Object((1,3,6,1,4,1,9,9,719,1,49,1,1))
cucsTopMetaInfEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsTopMetaInfEntry.setStatus(_A)
_CucsTopMetaInfInstanceId_Type=CucsManagedObjectId
_CucsTopMetaInfInstanceId_Object=MibTableColumn
cucsTopMetaInfInstanceId=_CucsTopMetaInfInstanceId_Object((1,3,6,1,4,1,9,9,719,1,49,1,1,1),_CucsTopMetaInfInstanceId_Type())
cucsTopMetaInfInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsTopMetaInfInstanceId.setStatus(_A)
_CucsTopMetaInfDn_Type=CucsManagedObjectDn
_CucsTopMetaInfDn_Object=MibTableColumn
cucsTopMetaInfDn=_CucsTopMetaInfDn_Object((1,3,6,1,4,1,9,9,719,1,49,1,1,2),_CucsTopMetaInfDn_Type())
cucsTopMetaInfDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopMetaInfDn.setStatus(_A)
_CucsTopMetaInfRn_Type=SnmpAdminString
_CucsTopMetaInfRn_Object=MibTableColumn
cucsTopMetaInfRn=_CucsTopMetaInfRn_Object((1,3,6,1,4,1,9,9,719,1,49,1,1,3),_CucsTopMetaInfRn_Type())
cucsTopMetaInfRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopMetaInfRn.setStatus(_A)
_CucsTopMetaInfEcode_Type=SnmpAdminString
_CucsTopMetaInfEcode_Object=MibTableColumn
cucsTopMetaInfEcode=_CucsTopMetaInfEcode_Object((1,3,6,1,4,1,9,9,719,1,49,1,1,4),_CucsTopMetaInfEcode_Type())
cucsTopMetaInfEcode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopMetaInfEcode.setStatus(_A)
_CucsTopMetaInfName_Type=SnmpAdminString
_CucsTopMetaInfName_Object=MibTableColumn
cucsTopMetaInfName=_CucsTopMetaInfName_Object((1,3,6,1,4,1,9,9,719,1,49,1,1,5),_CucsTopMetaInfName_Type())
cucsTopMetaInfName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopMetaInfName.setStatus(_A)
_CucsTopRootTable_Object=MibTable
cucsTopRootTable=_CucsTopRootTable_Object((1,3,6,1,4,1,9,9,719,1,49,2))
if mibBuilder.loadTexts:cucsTopRootTable.setStatus(_A)
_CucsTopRootEntry_Object=MibTableRow
cucsTopRootEntry=_CucsTopRootEntry_Object((1,3,6,1,4,1,9,9,719,1,49,2,1))
cucsTopRootEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsTopRootEntry.setStatus(_A)
_CucsTopRootInstanceId_Type=CucsManagedObjectId
_CucsTopRootInstanceId_Object=MibTableColumn
cucsTopRootInstanceId=_CucsTopRootInstanceId_Object((1,3,6,1,4,1,9,9,719,1,49,2,1,1),_CucsTopRootInstanceId_Type())
cucsTopRootInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsTopRootInstanceId.setStatus(_A)
_CucsTopRootDn_Type=CucsManagedObjectDn
_CucsTopRootDn_Object=MibTableColumn
cucsTopRootDn=_CucsTopRootDn_Object((1,3,6,1,4,1,9,9,719,1,49,2,1,2),_CucsTopRootDn_Type())
cucsTopRootDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopRootDn.setStatus(_A)
_CucsTopRootRn_Type=SnmpAdminString
_CucsTopRootRn_Object=MibTableColumn
cucsTopRootRn=_CucsTopRootRn_Object((1,3,6,1,4,1,9,9,719,1,49,2,1,3),_CucsTopRootRn_Type())
cucsTopRootRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopRootRn.setStatus(_A)
_CucsTopSystemTable_Object=MibTable
cucsTopSystemTable=_CucsTopSystemTable_Object((1,3,6,1,4,1,9,9,719,1,49,3))
if mibBuilder.loadTexts:cucsTopSystemTable.setStatus(_A)
_CucsTopSystemEntry_Object=MibTableRow
cucsTopSystemEntry=_CucsTopSystemEntry_Object((1,3,6,1,4,1,9,9,719,1,49,3,1))
cucsTopSystemEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsTopSystemEntry.setStatus(_A)
_CucsTopSystemInstanceId_Type=CucsManagedObjectId
_CucsTopSystemInstanceId_Object=MibTableColumn
cucsTopSystemInstanceId=_CucsTopSystemInstanceId_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,1),_CucsTopSystemInstanceId_Type())
cucsTopSystemInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsTopSystemInstanceId.setStatus(_A)
_CucsTopSystemDn_Type=CucsManagedObjectDn
_CucsTopSystemDn_Object=MibTableColumn
cucsTopSystemDn=_CucsTopSystemDn_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,2),_CucsTopSystemDn_Type())
cucsTopSystemDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemDn.setStatus(_A)
_CucsTopSystemRn_Type=SnmpAdminString
_CucsTopSystemRn_Object=MibTableColumn
cucsTopSystemRn=_CucsTopSystemRn_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,3),_CucsTopSystemRn_Type())
cucsTopSystemRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemRn.setStatus(_A)
_CucsTopSystemAddress_Type=InetAddressIPv4
_CucsTopSystemAddress_Object=MibTableColumn
cucsTopSystemAddress=_CucsTopSystemAddress_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,4),_CucsTopSystemAddress_Type())
cucsTopSystemAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemAddress.setStatus(_A)
_CucsTopSystemCurrentTime_Type=DateAndTime
_CucsTopSystemCurrentTime_Object=MibTableColumn
cucsTopSystemCurrentTime=_CucsTopSystemCurrentTime_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,5),_CucsTopSystemCurrentTime_Type())
cucsTopSystemCurrentTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemCurrentTime.setStatus(_A)
_CucsTopSystemMode_Type=CucsTopMode
_CucsTopSystemMode_Object=MibTableColumn
cucsTopSystemMode=_CucsTopSystemMode_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,6),_CucsTopSystemMode_Type())
cucsTopSystemMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemMode.setStatus(_A)
_CucsTopSystemName_Type=SnmpAdminString
_CucsTopSystemName_Object=MibTableColumn
cucsTopSystemName=_CucsTopSystemName_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,7),_CucsTopSystemName_Type())
cucsTopSystemName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemName.setStatus(_A)
_CucsTopSystemSystemUpTime_Type=TimeIntervalSec
_CucsTopSystemSystemUpTime_Object=MibTableColumn
cucsTopSystemSystemUpTime=_CucsTopSystemSystemUpTime_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,8),_CucsTopSystemSystemUpTime_Type())
cucsTopSystemSystemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemSystemUpTime.setStatus(_A)
_CucsTopSystemDescr_Type=SnmpAdminString
_CucsTopSystemDescr_Object=MibTableColumn
cucsTopSystemDescr=_CucsTopSystemDescr_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,9),_CucsTopSystemDescr_Type())
cucsTopSystemDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemDescr.setStatus(_A)
_CucsTopSystemOwner_Type=SnmpAdminString
_CucsTopSystemOwner_Object=MibTableColumn
cucsTopSystemOwner=_CucsTopSystemOwner_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,10),_CucsTopSystemOwner_Type())
cucsTopSystemOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemOwner.setStatus(_A)
_CucsTopSystemSite_Type=SnmpAdminString
_CucsTopSystemSite_Object=MibTableColumn
cucsTopSystemSite=_CucsTopSystemSite_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,11),_CucsTopSystemSite_Type())
cucsTopSystemSite.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemSite.setStatus(_A)
_CucsTopSystemIpv6Addr_Type=InetAddressIPv6
_CucsTopSystemIpv6Addr_Object=MibTableColumn
cucsTopSystemIpv6Addr=_CucsTopSystemIpv6Addr_Object((1,3,6,1,4,1,9,9,719,1,49,3,1,12),_CucsTopSystemIpv6Addr_Type())
cucsTopSystemIpv6Addr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSystemIpv6Addr.setStatus(_A)
_CucsTopSysDefaultsTable_Object=MibTable
cucsTopSysDefaultsTable=_CucsTopSysDefaultsTable_Object((1,3,6,1,4,1,9,9,719,1,49,4))
if mibBuilder.loadTexts:cucsTopSysDefaultsTable.setStatus(_A)
_CucsTopSysDefaultsEntry_Object=MibTableRow
cucsTopSysDefaultsEntry=_CucsTopSysDefaultsEntry_Object((1,3,6,1,4,1,9,9,719,1,49,4,1))
cucsTopSysDefaultsEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsTopSysDefaultsEntry.setStatus(_A)
_CucsTopSysDefaultsInstanceId_Type=CucsManagedObjectId
_CucsTopSysDefaultsInstanceId_Object=MibTableColumn
cucsTopSysDefaultsInstanceId=_CucsTopSysDefaultsInstanceId_Object((1,3,6,1,4,1,9,9,719,1,49,4,1,1),_CucsTopSysDefaultsInstanceId_Type())
cucsTopSysDefaultsInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsTopSysDefaultsInstanceId.setStatus(_A)
_CucsTopSysDefaultsDn_Type=CucsManagedObjectDn
_CucsTopSysDefaultsDn_Object=MibTableColumn
cucsTopSysDefaultsDn=_CucsTopSysDefaultsDn_Object((1,3,6,1,4,1,9,9,719,1,49,4,1,2),_CucsTopSysDefaultsDn_Type())
cucsTopSysDefaultsDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSysDefaultsDn.setStatus(_A)
_CucsTopSysDefaultsRn_Type=SnmpAdminString
_CucsTopSysDefaultsRn_Object=MibTableColumn
cucsTopSysDefaultsRn=_CucsTopSysDefaultsRn_Object((1,3,6,1,4,1,9,9,719,1,49,4,1,3),_CucsTopSysDefaultsRn_Type())
cucsTopSysDefaultsRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopSysDefaultsRn.setStatus(_A)
_CucsTopInfoPolicyTable_Object=MibTable
cucsTopInfoPolicyTable=_CucsTopInfoPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,49,5))
if mibBuilder.loadTexts:cucsTopInfoPolicyTable.setStatus(_A)
_CucsTopInfoPolicyEntry_Object=MibTableRow
cucsTopInfoPolicyEntry=_CucsTopInfoPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,49,5,1))
cucsTopInfoPolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsTopInfoPolicyEntry.setStatus(_A)
_CucsTopInfoPolicyInstanceId_Type=CucsManagedObjectId
_CucsTopInfoPolicyInstanceId_Object=MibTableColumn
cucsTopInfoPolicyInstanceId=_CucsTopInfoPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,49,5,1,1),_CucsTopInfoPolicyInstanceId_Type())
cucsTopInfoPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsTopInfoPolicyInstanceId.setStatus(_A)
_CucsTopInfoPolicyDn_Type=CucsManagedObjectDn
_CucsTopInfoPolicyDn_Object=MibTableColumn
cucsTopInfoPolicyDn=_CucsTopInfoPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,49,5,1,2),_CucsTopInfoPolicyDn_Type())
cucsTopInfoPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoPolicyDn.setStatus(_A)
_CucsTopInfoPolicyRn_Type=SnmpAdminString
_CucsTopInfoPolicyRn_Object=MibTableColumn
cucsTopInfoPolicyRn=_CucsTopInfoPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,49,5,1,3),_CucsTopInfoPolicyRn_Type())
cucsTopInfoPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoPolicyRn.setStatus(_A)
_CucsTopInfoPolicyState_Type=CucsTopInfoPolicyState
_CucsTopInfoPolicyState_Object=MibTableColumn
cucsTopInfoPolicyState=_CucsTopInfoPolicyState_Object((1,3,6,1,4,1,9,9,719,1,49,5,1,4),_CucsTopInfoPolicyState_Type())
cucsTopInfoPolicyState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoPolicyState.setStatus(_A)
_CucsTopInfoSyncPolicyTable_Object=MibTable
cucsTopInfoSyncPolicyTable=_CucsTopInfoSyncPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,49,6))
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyTable.setStatus(_A)
_CucsTopInfoSyncPolicyEntry_Object=MibTableRow
cucsTopInfoSyncPolicyEntry=_CucsTopInfoSyncPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,49,6,1))
cucsTopInfoSyncPolicyEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyEntry.setStatus(_A)
_CucsTopInfoSyncPolicyInstanceId_Type=CucsManagedObjectId
_CucsTopInfoSyncPolicyInstanceId_Object=MibTableColumn
cucsTopInfoSyncPolicyInstanceId=_CucsTopInfoSyncPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,1),_CucsTopInfoSyncPolicyInstanceId_Type())
cucsTopInfoSyncPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyInstanceId.setStatus(_A)
_CucsTopInfoSyncPolicyDn_Type=CucsManagedObjectDn
_CucsTopInfoSyncPolicyDn_Object=MibTableColumn
cucsTopInfoSyncPolicyDn=_CucsTopInfoSyncPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,2),_CucsTopInfoSyncPolicyDn_Type())
cucsTopInfoSyncPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyDn.setStatus(_A)
_CucsTopInfoSyncPolicyRn_Type=SnmpAdminString
_CucsTopInfoSyncPolicyRn_Object=MibTableColumn
cucsTopInfoSyncPolicyRn=_CucsTopInfoSyncPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,3),_CucsTopInfoSyncPolicyRn_Type())
cucsTopInfoSyncPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyRn.setStatus(_A)
_CucsTopInfoSyncPolicyDescr_Type=SnmpAdminString
_CucsTopInfoSyncPolicyDescr_Object=MibTableColumn
cucsTopInfoSyncPolicyDescr=_CucsTopInfoSyncPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,4),_CucsTopInfoSyncPolicyDescr_Type())
cucsTopInfoSyncPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyDescr.setStatus(_A)
_CucsTopInfoSyncPolicyIntId_Type=SnmpAdminString
_CucsTopInfoSyncPolicyIntId_Object=MibTableColumn
cucsTopInfoSyncPolicyIntId=_CucsTopInfoSyncPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,5),_CucsTopInfoSyncPolicyIntId_Type())
cucsTopInfoSyncPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyIntId.setStatus(_A)
_CucsTopInfoSyncPolicyName_Type=SnmpAdminString
_CucsTopInfoSyncPolicyName_Object=MibTableColumn
cucsTopInfoSyncPolicyName=_CucsTopInfoSyncPolicyName_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,6),_CucsTopInfoSyncPolicyName_Type())
cucsTopInfoSyncPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyName.setStatus(_A)
_CucsTopInfoSyncPolicyPolicyLevel_Type=Gauge32
_CucsTopInfoSyncPolicyPolicyLevel_Object=MibTableColumn
cucsTopInfoSyncPolicyPolicyLevel=_CucsTopInfoSyncPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,7),_CucsTopInfoSyncPolicyPolicyLevel_Type())
cucsTopInfoSyncPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyPolicyLevel.setStatus(_A)
_CucsTopInfoSyncPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsTopInfoSyncPolicyPolicyOwner_Object=MibTableColumn
cucsTopInfoSyncPolicyPolicyOwner=_CucsTopInfoSyncPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,8),_CucsTopInfoSyncPolicyPolicyOwner_Type())
cucsTopInfoSyncPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyPolicyOwner.setStatus(_A)
_CucsTopInfoSyncPolicyState_Type=CucsTopInfoSyncPolicyState
_CucsTopInfoSyncPolicyState_Object=MibTableColumn
cucsTopInfoSyncPolicyState=_CucsTopInfoSyncPolicyState_Object((1,3,6,1,4,1,9,9,719,1,49,6,1,9),_CucsTopInfoSyncPolicyState_Type())
cucsTopInfoSyncPolicyState.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsTopInfoSyncPolicyState.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsTopObjects':cucsTopObjects,'cucsTopMetaInfTable':cucsTopMetaInfTable,'cucsTopMetaInfEntry':cucsTopMetaInfEntry,_E:cucsTopMetaInfInstanceId,'cucsTopMetaInfDn':cucsTopMetaInfDn,'cucsTopMetaInfRn':cucsTopMetaInfRn,'cucsTopMetaInfEcode':cucsTopMetaInfEcode,'cucsTopMetaInfName':cucsTopMetaInfName,'cucsTopRootTable':cucsTopRootTable,'cucsTopRootEntry':cucsTopRootEntry,_F:cucsTopRootInstanceId,'cucsTopRootDn':cucsTopRootDn,'cucsTopRootRn':cucsTopRootRn,'cucsTopSystemTable':cucsTopSystemTable,'cucsTopSystemEntry':cucsTopSystemEntry,_G:cucsTopSystemInstanceId,'cucsTopSystemDn':cucsTopSystemDn,'cucsTopSystemRn':cucsTopSystemRn,'cucsTopSystemAddress':cucsTopSystemAddress,'cucsTopSystemCurrentTime':cucsTopSystemCurrentTime,'cucsTopSystemMode':cucsTopSystemMode,'cucsTopSystemName':cucsTopSystemName,'cucsTopSystemSystemUpTime':cucsTopSystemSystemUpTime,'cucsTopSystemDescr':cucsTopSystemDescr,'cucsTopSystemOwner':cucsTopSystemOwner,'cucsTopSystemSite':cucsTopSystemSite,'cucsTopSystemIpv6Addr':cucsTopSystemIpv6Addr,'cucsTopSysDefaultsTable':cucsTopSysDefaultsTable,'cucsTopSysDefaultsEntry':cucsTopSysDefaultsEntry,_H:cucsTopSysDefaultsInstanceId,'cucsTopSysDefaultsDn':cucsTopSysDefaultsDn,'cucsTopSysDefaultsRn':cucsTopSysDefaultsRn,'cucsTopInfoPolicyTable':cucsTopInfoPolicyTable,'cucsTopInfoPolicyEntry':cucsTopInfoPolicyEntry,_I:cucsTopInfoPolicyInstanceId,'cucsTopInfoPolicyDn':cucsTopInfoPolicyDn,'cucsTopInfoPolicyRn':cucsTopInfoPolicyRn,'cucsTopInfoPolicyState':cucsTopInfoPolicyState,'cucsTopInfoSyncPolicyTable':cucsTopInfoSyncPolicyTable,'cucsTopInfoSyncPolicyEntry':cucsTopInfoSyncPolicyEntry,_J:cucsTopInfoSyncPolicyInstanceId,'cucsTopInfoSyncPolicyDn':cucsTopInfoSyncPolicyDn,'cucsTopInfoSyncPolicyRn':cucsTopInfoSyncPolicyRn,'cucsTopInfoSyncPolicyDescr':cucsTopInfoSyncPolicyDescr,'cucsTopInfoSyncPolicyIntId':cucsTopInfoSyncPolicyIntId,'cucsTopInfoSyncPolicyName':cucsTopInfoSyncPolicyName,'cucsTopInfoSyncPolicyPolicyLevel':cucsTopInfoSyncPolicyPolicyLevel,'cucsTopInfoSyncPolicyPolicyOwner':cucsTopInfoSyncPolicyPolicyOwner,'cucsTopInfoSyncPolicyState':cucsTopInfoSyncPolicyState})