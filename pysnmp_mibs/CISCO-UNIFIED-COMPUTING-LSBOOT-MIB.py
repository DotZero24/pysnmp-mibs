_i='cucsLsbootNvmePciSsdInstanceId'
_h='cucsLsbootNvmeDiskSsdInstanceId'
_g='cucsLsbootNvmeInstanceId'
_f='cucsLsbootEFIShellInstanceId'
_e='cucsLsbootEmbeddedLocalLunImageInstanceId'
_d='cucsLsbootEmbeddedLocalDiskImagePathInstanceId'
_c='cucsLsbootEmbeddedLocalDiskImageInstanceId'
_b='cucsLsbootUEFIBootParamInstanceId'
_a='cucsLsbootLocalLunImagePathInstanceId'
_Z='cucsLsbootLocalDiskImagePathInstanceId'
_Y='cucsLsbootLocalDiskImageInstanceId'
_X='cucsLsbootUsbInternalImageInstanceId'
_W='cucsLsbootUsbFlashStorageImageInstanceId'
_V='cucsLsbootUsbExternalImageInstanceId'
_U='cucsLsbootSanCatSanImagePathInstanceId'
_T='cucsLsbootSanCatSanImageInstanceId'
_S='cucsLsbootSanInstanceId'
_R='cucsLsbootLocalHddImageInstanceId'
_Q='cucsLsbootDefaultLocalImageInstanceId'
_P='cucsLsbootBootSecurityInstanceId'
_O='cucsLsbootIScsiImagePathInstanceId'
_N='cucsLsbootIScsiInstanceId'
_M='cucsLsbootVirtualMediaInstanceId'
_L='cucsLsbootStorageInstanceId'
_K='cucsLsbootSanImagePathInstanceId'
_J='cucsLsbootSanImageInstanceId'
_I='cucsLsbootPolicyInstanceId'
_H='cucsLsbootLocalStorageInstanceId'
_G='cucsLsbootLanImagePathInstanceId'
_F='cucsLsbootLanInstanceId'
_E='cucsLsbootDefInstanceId'
_D='not-accessible'
_C='CISCO-UNIFIED-COMPUTING-LSBOOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
CucsManagedObjectDn,CucsManagedObjectId,ciscoUnifiedComputingMIBObjects=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-MIB','CucsManagedObjectDn','CucsManagedObjectId','ciscoUnifiedComputingMIBObjects')
CucsLsbootADefBootMode,CucsLsbootAccessType,CucsLsbootDefaultLocalImageType,CucsLsbootEFIShellAccess,CucsLsbootEFIShellType,CucsLsbootEmbeddedLocalDiskImagePathType,CucsLsbootEmbeddedLocalDiskImageType,CucsLsbootEmbeddedLocalLunImageType,CucsLsbootIScsiAccess,CucsLsbootIScsiImagePathType,CucsLsbootIScsiType,CucsLsbootLanAccess,CucsLsbootLanBootProt,CucsLsbootLanImagePathType,CucsLsbootLanType,CucsLsbootLocalDiskImagePathType,CucsLsbootLocalDiskImageType,CucsLsbootLocalHddImageType,CucsLsbootLocalLunImagePathType,CucsLsbootNvmeDiskSsdType,CucsLsbootNvmePciSsdType,CucsLsbootNvmeType,CucsLsbootPurpose,CucsLsbootSanAccess,CucsLsbootSanCatSanImagePathType,CucsLsbootSanCatSanImageType,CucsLsbootSanImagePathType,CucsLsbootSanImageType,CucsLsbootSanType,CucsLsbootStorageAccess,CucsLsbootStorageType,CucsLsbootUsbExternalImageType,CucsLsbootUsbFlashStorageImageType,CucsLsbootUsbInternalImageType,CucsLsbootVirtualMediaType,CucsPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-UNIFIED-COMPUTING-TC-MIB','CucsLsbootADefBootMode','CucsLsbootAccessType','CucsLsbootDefaultLocalImageType','CucsLsbootEFIShellAccess','CucsLsbootEFIShellType','CucsLsbootEmbeddedLocalDiskImagePathType','CucsLsbootEmbeddedLocalDiskImageType','CucsLsbootEmbeddedLocalLunImageType','CucsLsbootIScsiAccess','CucsLsbootIScsiImagePathType','CucsLsbootIScsiType','CucsLsbootLanAccess','CucsLsbootLanBootProt','CucsLsbootLanImagePathType','CucsLsbootLanType','CucsLsbootLocalDiskImagePathType','CucsLsbootLocalDiskImageType','CucsLsbootLocalHddImageType','CucsLsbootLocalLunImagePathType','CucsLsbootNvmeDiskSsdType','CucsLsbootNvmePciSsdType','CucsLsbootNvmeType','CucsLsbootPurpose','CucsLsbootSanAccess','CucsLsbootSanCatSanImagePathType','CucsLsbootSanCatSanImageType','CucsLsbootSanImagePathType','CucsLsbootSanImageType','CucsLsbootSanType','CucsLsbootStorageAccess','CucsLsbootStorageType','CucsLsbootUsbExternalImageType','CucsLsbootUsbFlashStorageImageType','CucsLsbootUsbInternalImageType','CucsLsbootVirtualMediaType','CucsPolicyPolicyOwner')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cucsLsbootObjects=ModuleIdentity((1,3,6,1,4,1,9,9,719,1,27))
_CucsLsbootDefTable_Object=MibTable
cucsLsbootDefTable=_CucsLsbootDefTable_Object((1,3,6,1,4,1,9,9,719,1,27,1))
if mibBuilder.loadTexts:cucsLsbootDefTable.setStatus(_A)
_CucsLsbootDefEntry_Object=MibTableRow
cucsLsbootDefEntry=_CucsLsbootDefEntry_Object((1,3,6,1,4,1,9,9,719,1,27,1,1))
cucsLsbootDefEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cucsLsbootDefEntry.setStatus(_A)
_CucsLsbootDefInstanceId_Type=CucsManagedObjectId
_CucsLsbootDefInstanceId_Object=MibTableColumn
cucsLsbootDefInstanceId=_CucsLsbootDefInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,1),_CucsLsbootDefInstanceId_Type())
cucsLsbootDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootDefInstanceId.setStatus(_A)
_CucsLsbootDefDn_Type=CucsManagedObjectDn
_CucsLsbootDefDn_Object=MibTableColumn
cucsLsbootDefDn=_CucsLsbootDefDn_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,2),_CucsLsbootDefDn_Type())
cucsLsbootDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefDn.setStatus(_A)
_CucsLsbootDefRn_Type=SnmpAdminString
_CucsLsbootDefRn_Object=MibTableColumn
cucsLsbootDefRn=_CucsLsbootDefRn_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,3),_CucsLsbootDefRn_Type())
cucsLsbootDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefRn.setStatus(_A)
_CucsLsbootDefDescr_Type=SnmpAdminString
_CucsLsbootDefDescr_Object=MibTableColumn
cucsLsbootDefDescr=_CucsLsbootDefDescr_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,4),_CucsLsbootDefDescr_Type())
cucsLsbootDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefDescr.setStatus(_A)
_CucsLsbootDefEnforceVnicName_Type=TruthValue
_CucsLsbootDefEnforceVnicName_Object=MibTableColumn
cucsLsbootDefEnforceVnicName=_CucsLsbootDefEnforceVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,5),_CucsLsbootDefEnforceVnicName_Type())
cucsLsbootDefEnforceVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefEnforceVnicName.setStatus(_A)
_CucsLsbootDefIntId_Type=SnmpAdminString
_CucsLsbootDefIntId_Object=MibTableColumn
cucsLsbootDefIntId=_CucsLsbootDefIntId_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,6),_CucsLsbootDefIntId_Type())
cucsLsbootDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefIntId.setStatus(_A)
_CucsLsbootDefName_Type=SnmpAdminString
_CucsLsbootDefName_Object=MibTableColumn
cucsLsbootDefName=_CucsLsbootDefName_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,7),_CucsLsbootDefName_Type())
cucsLsbootDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefName.setStatus(_A)
_CucsLsbootDefPurpose_Type=CucsLsbootPurpose
_CucsLsbootDefPurpose_Object=MibTableColumn
cucsLsbootDefPurpose=_CucsLsbootDefPurpose_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,8),_CucsLsbootDefPurpose_Type())
cucsLsbootDefPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefPurpose.setStatus(_A)
_CucsLsbootDefRebootOnUpdate_Type=TruthValue
_CucsLsbootDefRebootOnUpdate_Object=MibTableColumn
cucsLsbootDefRebootOnUpdate=_CucsLsbootDefRebootOnUpdate_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,9),_CucsLsbootDefRebootOnUpdate_Type())
cucsLsbootDefRebootOnUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefRebootOnUpdate.setStatus(_A)
_CucsLsbootDefPolicyLevel_Type=Gauge32
_CucsLsbootDefPolicyLevel_Object=MibTableColumn
cucsLsbootDefPolicyLevel=_CucsLsbootDefPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,10),_CucsLsbootDefPolicyLevel_Type())
cucsLsbootDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefPolicyLevel.setStatus(_A)
_CucsLsbootDefPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsLsbootDefPolicyOwner_Object=MibTableColumn
cucsLsbootDefPolicyOwner=_CucsLsbootDefPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,11),_CucsLsbootDefPolicyOwner_Type())
cucsLsbootDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefPolicyOwner.setStatus(_A)
_CucsLsbootDefAdvBootOrderApplicable_Type=TruthValue
_CucsLsbootDefAdvBootOrderApplicable_Object=MibTableColumn
cucsLsbootDefAdvBootOrderApplicable=_CucsLsbootDefAdvBootOrderApplicable_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,12),_CucsLsbootDefAdvBootOrderApplicable_Type())
cucsLsbootDefAdvBootOrderApplicable.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefAdvBootOrderApplicable.setStatus(_A)
_CucsLsbootDefBootMode_Type=CucsLsbootADefBootMode
_CucsLsbootDefBootMode_Object=MibTableColumn
cucsLsbootDefBootMode=_CucsLsbootDefBootMode_Object((1,3,6,1,4,1,9,9,719,1,27,1,1,13),_CucsLsbootDefBootMode_Type())
cucsLsbootDefBootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefBootMode.setStatus(_A)
_CucsLsbootLanTable_Object=MibTable
cucsLsbootLanTable=_CucsLsbootLanTable_Object((1,3,6,1,4,1,9,9,719,1,27,2))
if mibBuilder.loadTexts:cucsLsbootLanTable.setStatus(_A)
_CucsLsbootLanEntry_Object=MibTableRow
cucsLsbootLanEntry=_CucsLsbootLanEntry_Object((1,3,6,1,4,1,9,9,719,1,27,2,1))
cucsLsbootLanEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cucsLsbootLanEntry.setStatus(_A)
_CucsLsbootLanInstanceId_Type=CucsManagedObjectId
_CucsLsbootLanInstanceId_Object=MibTableColumn
cucsLsbootLanInstanceId=_CucsLsbootLanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,1),_CucsLsbootLanInstanceId_Type())
cucsLsbootLanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLanInstanceId.setStatus(_A)
_CucsLsbootLanDn_Type=CucsManagedObjectDn
_CucsLsbootLanDn_Object=MibTableColumn
cucsLsbootLanDn=_CucsLsbootLanDn_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,2),_CucsLsbootLanDn_Type())
cucsLsbootLanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanDn.setStatus(_A)
_CucsLsbootLanRn_Type=SnmpAdminString
_CucsLsbootLanRn_Object=MibTableColumn
cucsLsbootLanRn=_CucsLsbootLanRn_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,3),_CucsLsbootLanRn_Type())
cucsLsbootLanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanRn.setStatus(_A)
_CucsLsbootLanAccess_Type=CucsLsbootLanAccess
_CucsLsbootLanAccess_Object=MibTableColumn
cucsLsbootLanAccess=_CucsLsbootLanAccess_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,4),_CucsLsbootLanAccess_Type())
cucsLsbootLanAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanAccess.setStatus(_A)
_CucsLsbootLanOrder_Type=Gauge32
_CucsLsbootLanOrder_Object=MibTableColumn
cucsLsbootLanOrder=_CucsLsbootLanOrder_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,5),_CucsLsbootLanOrder_Type())
cucsLsbootLanOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanOrder.setStatus(_A)
_CucsLsbootLanType_Type=CucsLsbootLanType
_CucsLsbootLanType_Object=MibTableColumn
cucsLsbootLanType=_CucsLsbootLanType_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,6),_CucsLsbootLanType_Type())
cucsLsbootLanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanType.setStatus(_A)
_CucsLsbootLanProt_Type=CucsLsbootLanBootProt
_CucsLsbootLanProt_Object=MibTableColumn
cucsLsbootLanProt=_CucsLsbootLanProt_Object((1,3,6,1,4,1,9,9,719,1,27,2,1,7),_CucsLsbootLanProt_Type())
cucsLsbootLanProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanProt.setStatus(_A)
_CucsLsbootLanImagePathTable_Object=MibTable
cucsLsbootLanImagePathTable=_CucsLsbootLanImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,3))
if mibBuilder.loadTexts:cucsLsbootLanImagePathTable.setStatus(_A)
_CucsLsbootLanImagePathEntry_Object=MibTableRow
cucsLsbootLanImagePathEntry=_CucsLsbootLanImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,3,1))
cucsLsbootLanImagePathEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cucsLsbootLanImagePathEntry.setStatus(_A)
_CucsLsbootLanImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootLanImagePathInstanceId_Object=MibTableColumn
cucsLsbootLanImagePathInstanceId=_CucsLsbootLanImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,1),_CucsLsbootLanImagePathInstanceId_Type())
cucsLsbootLanImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLanImagePathInstanceId.setStatus(_A)
_CucsLsbootLanImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootLanImagePathDn_Object=MibTableColumn
cucsLsbootLanImagePathDn=_CucsLsbootLanImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,2),_CucsLsbootLanImagePathDn_Type())
cucsLsbootLanImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathDn.setStatus(_A)
_CucsLsbootLanImagePathRn_Type=SnmpAdminString
_CucsLsbootLanImagePathRn_Object=MibTableColumn
cucsLsbootLanImagePathRn=_CucsLsbootLanImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,3),_CucsLsbootLanImagePathRn_Type())
cucsLsbootLanImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathRn.setStatus(_A)
_CucsLsbootLanImagePathType_Type=CucsLsbootLanImagePathType
_CucsLsbootLanImagePathType_Object=MibTableColumn
cucsLsbootLanImagePathType=_CucsLsbootLanImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,4),_CucsLsbootLanImagePathType_Type())
cucsLsbootLanImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathType.setStatus(_A)
_CucsLsbootLanImagePathVnicName_Type=SnmpAdminString
_CucsLsbootLanImagePathVnicName_Object=MibTableColumn
cucsLsbootLanImagePathVnicName=_CucsLsbootLanImagePathVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,5),_CucsLsbootLanImagePathVnicName_Type())
cucsLsbootLanImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathVnicName.setStatus(_A)
_CucsLsbootLanImagePathImgPolicyName_Type=SnmpAdminString
_CucsLsbootLanImagePathImgPolicyName_Object=MibTableColumn
cucsLsbootLanImagePathImgPolicyName=_CucsLsbootLanImagePathImgPolicyName_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,6),_CucsLsbootLanImagePathImgPolicyName_Type())
cucsLsbootLanImagePathImgPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathImgPolicyName.setStatus(_A)
_CucsLsbootLanImagePathImgSecPolicyName_Type=SnmpAdminString
_CucsLsbootLanImagePathImgSecPolicyName_Object=MibTableColumn
cucsLsbootLanImagePathImgSecPolicyName=_CucsLsbootLanImagePathImgSecPolicyName_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,7),_CucsLsbootLanImagePathImgSecPolicyName_Type())
cucsLsbootLanImagePathImgSecPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathImgSecPolicyName.setStatus(_A)
_CucsLsbootLanImagePathBootIpPolicyName_Type=SnmpAdminString
_CucsLsbootLanImagePathBootIpPolicyName_Object=MibTableColumn
cucsLsbootLanImagePathBootIpPolicyName=_CucsLsbootLanImagePathBootIpPolicyName_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,8),_CucsLsbootLanImagePathBootIpPolicyName_Type())
cucsLsbootLanImagePathBootIpPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathBootIpPolicyName.setStatus(_A)
_CucsLsbootLanImagePathProvSrvPolicyName_Type=SnmpAdminString
_CucsLsbootLanImagePathProvSrvPolicyName_Object=MibTableColumn
cucsLsbootLanImagePathProvSrvPolicyName=_CucsLsbootLanImagePathProvSrvPolicyName_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,9),_CucsLsbootLanImagePathProvSrvPolicyName_Type())
cucsLsbootLanImagePathProvSrvPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathProvSrvPolicyName.setStatus(_A)
_CucsLsbootLanImagePathISCSIVnicName_Type=SnmpAdminString
_CucsLsbootLanImagePathISCSIVnicName_Object=MibTableColumn
cucsLsbootLanImagePathISCSIVnicName=_CucsLsbootLanImagePathISCSIVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,3,1,10),_CucsLsbootLanImagePathISCSIVnicName_Type())
cucsLsbootLanImagePathISCSIVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLanImagePathISCSIVnicName.setStatus(_A)
_CucsLsbootLocalStorageTable_Object=MibTable
cucsLsbootLocalStorageTable=_CucsLsbootLocalStorageTable_Object((1,3,6,1,4,1,9,9,719,1,27,4))
if mibBuilder.loadTexts:cucsLsbootLocalStorageTable.setStatus(_A)
_CucsLsbootLocalStorageEntry_Object=MibTableRow
cucsLsbootLocalStorageEntry=_CucsLsbootLocalStorageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,4,1))
cucsLsbootLocalStorageEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cucsLsbootLocalStorageEntry.setStatus(_A)
_CucsLsbootLocalStorageInstanceId_Type=CucsManagedObjectId
_CucsLsbootLocalStorageInstanceId_Object=MibTableColumn
cucsLsbootLocalStorageInstanceId=_CucsLsbootLocalStorageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,4,1,1),_CucsLsbootLocalStorageInstanceId_Type())
cucsLsbootLocalStorageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLocalStorageInstanceId.setStatus(_A)
_CucsLsbootLocalStorageDn_Type=CucsManagedObjectDn
_CucsLsbootLocalStorageDn_Object=MibTableColumn
cucsLsbootLocalStorageDn=_CucsLsbootLocalStorageDn_Object((1,3,6,1,4,1,9,9,719,1,27,4,1,2),_CucsLsbootLocalStorageDn_Type())
cucsLsbootLocalStorageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalStorageDn.setStatus(_A)
_CucsLsbootLocalStorageRn_Type=SnmpAdminString
_CucsLsbootLocalStorageRn_Object=MibTableColumn
cucsLsbootLocalStorageRn=_CucsLsbootLocalStorageRn_Object((1,3,6,1,4,1,9,9,719,1,27,4,1,3),_CucsLsbootLocalStorageRn_Type())
cucsLsbootLocalStorageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalStorageRn.setStatus(_A)
_CucsLsbootLocalStoragePropAcl_Type=Unsigned64
_CucsLsbootLocalStoragePropAcl_Object=MibTableColumn
cucsLsbootLocalStoragePropAcl=_CucsLsbootLocalStoragePropAcl_Object((1,3,6,1,4,1,9,9,719,1,27,4,1,4),_CucsLsbootLocalStoragePropAcl_Type())
cucsLsbootLocalStoragePropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalStoragePropAcl.setStatus(_A)
_CucsLsbootPolicyTable_Object=MibTable
cucsLsbootPolicyTable=_CucsLsbootPolicyTable_Object((1,3,6,1,4,1,9,9,719,1,27,5))
if mibBuilder.loadTexts:cucsLsbootPolicyTable.setStatus(_A)
_CucsLsbootPolicyEntry_Object=MibTableRow
cucsLsbootPolicyEntry=_CucsLsbootPolicyEntry_Object((1,3,6,1,4,1,9,9,719,1,27,5,1))
cucsLsbootPolicyEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cucsLsbootPolicyEntry.setStatus(_A)
_CucsLsbootPolicyInstanceId_Type=CucsManagedObjectId
_CucsLsbootPolicyInstanceId_Object=MibTableColumn
cucsLsbootPolicyInstanceId=_CucsLsbootPolicyInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,1),_CucsLsbootPolicyInstanceId_Type())
cucsLsbootPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootPolicyInstanceId.setStatus(_A)
_CucsLsbootPolicyDn_Type=CucsManagedObjectDn
_CucsLsbootPolicyDn_Object=MibTableColumn
cucsLsbootPolicyDn=_CucsLsbootPolicyDn_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,2),_CucsLsbootPolicyDn_Type())
cucsLsbootPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyDn.setStatus(_A)
_CucsLsbootPolicyRn_Type=SnmpAdminString
_CucsLsbootPolicyRn_Object=MibTableColumn
cucsLsbootPolicyRn=_CucsLsbootPolicyRn_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,3),_CucsLsbootPolicyRn_Type())
cucsLsbootPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyRn.setStatus(_A)
_CucsLsbootPolicyDescr_Type=SnmpAdminString
_CucsLsbootPolicyDescr_Object=MibTableColumn
cucsLsbootPolicyDescr=_CucsLsbootPolicyDescr_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,4),_CucsLsbootPolicyDescr_Type())
cucsLsbootPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyDescr.setStatus(_A)
_CucsLsbootPolicyEnforceVnicName_Type=TruthValue
_CucsLsbootPolicyEnforceVnicName_Object=MibTableColumn
cucsLsbootPolicyEnforceVnicName=_CucsLsbootPolicyEnforceVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,5),_CucsLsbootPolicyEnforceVnicName_Type())
cucsLsbootPolicyEnforceVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyEnforceVnicName.setStatus(_A)
_CucsLsbootPolicyIntId_Type=SnmpAdminString
_CucsLsbootPolicyIntId_Object=MibTableColumn
cucsLsbootPolicyIntId=_CucsLsbootPolicyIntId_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,6),_CucsLsbootPolicyIntId_Type())
cucsLsbootPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyIntId.setStatus(_A)
_CucsLsbootPolicyName_Type=SnmpAdminString
_CucsLsbootPolicyName_Object=MibTableColumn
cucsLsbootPolicyName=_CucsLsbootPolicyName_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,7),_CucsLsbootPolicyName_Type())
cucsLsbootPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyName.setStatus(_A)
_CucsLsbootPolicyPurpose_Type=CucsLsbootPurpose
_CucsLsbootPolicyPurpose_Object=MibTableColumn
cucsLsbootPolicyPurpose=_CucsLsbootPolicyPurpose_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,8),_CucsLsbootPolicyPurpose_Type())
cucsLsbootPolicyPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyPurpose.setStatus(_A)
_CucsLsbootPolicyRebootOnUpdate_Type=TruthValue
_CucsLsbootPolicyRebootOnUpdate_Object=MibTableColumn
cucsLsbootPolicyRebootOnUpdate=_CucsLsbootPolicyRebootOnUpdate_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,9),_CucsLsbootPolicyRebootOnUpdate_Type())
cucsLsbootPolicyRebootOnUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyRebootOnUpdate.setStatus(_A)
_CucsLsbootPolicyPolicyLevel_Type=Gauge32
_CucsLsbootPolicyPolicyLevel_Object=MibTableColumn
cucsLsbootPolicyPolicyLevel=_CucsLsbootPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,10),_CucsLsbootPolicyPolicyLevel_Type())
cucsLsbootPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyPolicyLevel.setStatus(_A)
_CucsLsbootPolicyPolicyOwner_Type=CucsPolicyPolicyOwner
_CucsLsbootPolicyPolicyOwner_Object=MibTableColumn
cucsLsbootPolicyPolicyOwner=_CucsLsbootPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,11),_CucsLsbootPolicyPolicyOwner_Type())
cucsLsbootPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyPolicyOwner.setStatus(_A)
_CucsLsbootPolicyBootMode_Type=CucsLsbootADefBootMode
_CucsLsbootPolicyBootMode_Object=MibTableColumn
cucsLsbootPolicyBootMode=_CucsLsbootPolicyBootMode_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,12),_CucsLsbootPolicyBootMode_Type())
cucsLsbootPolicyBootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyBootMode.setStatus(_A)
_CucsLsbootPolicyPropAcl_Type=Unsigned64
_CucsLsbootPolicyPropAcl_Object=MibTableColumn
cucsLsbootPolicyPropAcl=_CucsLsbootPolicyPropAcl_Object((1,3,6,1,4,1,9,9,719,1,27,5,1,13),_CucsLsbootPolicyPropAcl_Type())
cucsLsbootPolicyPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootPolicyPropAcl.setStatus(_A)
_CucsLsbootSanImageTable_Object=MibTable
cucsLsbootSanImageTable=_CucsLsbootSanImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,6))
if mibBuilder.loadTexts:cucsLsbootSanImageTable.setStatus(_A)
_CucsLsbootSanImageEntry_Object=MibTableRow
cucsLsbootSanImageEntry=_CucsLsbootSanImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,6,1))
cucsLsbootSanImageEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cucsLsbootSanImageEntry.setStatus(_A)
_CucsLsbootSanImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootSanImageInstanceId_Object=MibTableColumn
cucsLsbootSanImageInstanceId=_CucsLsbootSanImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,6,1,1),_CucsLsbootSanImageInstanceId_Type())
cucsLsbootSanImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootSanImageInstanceId.setStatus(_A)
_CucsLsbootSanImageDn_Type=CucsManagedObjectDn
_CucsLsbootSanImageDn_Object=MibTableColumn
cucsLsbootSanImageDn=_CucsLsbootSanImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,6,1,2),_CucsLsbootSanImageDn_Type())
cucsLsbootSanImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImageDn.setStatus(_A)
_CucsLsbootSanImageRn_Type=SnmpAdminString
_CucsLsbootSanImageRn_Object=MibTableColumn
cucsLsbootSanImageRn=_CucsLsbootSanImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,6,1,3),_CucsLsbootSanImageRn_Type())
cucsLsbootSanImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImageRn.setStatus(_A)
_CucsLsbootSanImageType_Type=CucsLsbootSanImageType
_CucsLsbootSanImageType_Object=MibTableColumn
cucsLsbootSanImageType=_CucsLsbootSanImageType_Object((1,3,6,1,4,1,9,9,719,1,27,6,1,4),_CucsLsbootSanImageType_Type())
cucsLsbootSanImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImageType.setStatus(_A)
_CucsLsbootSanImageVnicName_Type=SnmpAdminString
_CucsLsbootSanImageVnicName_Object=MibTableColumn
cucsLsbootSanImageVnicName=_CucsLsbootSanImageVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,6,1,5),_CucsLsbootSanImageVnicName_Type())
cucsLsbootSanImageVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImageVnicName.setStatus(_A)
_CucsLsbootSanImagePathTable_Object=MibTable
cucsLsbootSanImagePathTable=_CucsLsbootSanImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,7))
if mibBuilder.loadTexts:cucsLsbootSanImagePathTable.setStatus(_A)
_CucsLsbootSanImagePathEntry_Object=MibTableRow
cucsLsbootSanImagePathEntry=_CucsLsbootSanImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,7,1))
cucsLsbootSanImagePathEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cucsLsbootSanImagePathEntry.setStatus(_A)
_CucsLsbootSanImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootSanImagePathInstanceId_Object=MibTableColumn
cucsLsbootSanImagePathInstanceId=_CucsLsbootSanImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,1),_CucsLsbootSanImagePathInstanceId_Type())
cucsLsbootSanImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootSanImagePathInstanceId.setStatus(_A)
_CucsLsbootSanImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootSanImagePathDn_Object=MibTableColumn
cucsLsbootSanImagePathDn=_CucsLsbootSanImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,2),_CucsLsbootSanImagePathDn_Type())
cucsLsbootSanImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImagePathDn.setStatus(_A)
_CucsLsbootSanImagePathRn_Type=SnmpAdminString
_CucsLsbootSanImagePathRn_Object=MibTableColumn
cucsLsbootSanImagePathRn=_CucsLsbootSanImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,3),_CucsLsbootSanImagePathRn_Type())
cucsLsbootSanImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImagePathRn.setStatus(_A)
_CucsLsbootSanImagePathLun_Type=SnmpAdminString
_CucsLsbootSanImagePathLun_Object=MibTableColumn
cucsLsbootSanImagePathLun=_CucsLsbootSanImagePathLun_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,4),_CucsLsbootSanImagePathLun_Type())
cucsLsbootSanImagePathLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImagePathLun.setStatus(_A)
_CucsLsbootSanImagePathType_Type=CucsLsbootSanImagePathType
_CucsLsbootSanImagePathType_Object=MibTableColumn
cucsLsbootSanImagePathType=_CucsLsbootSanImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,5),_CucsLsbootSanImagePathType_Type())
cucsLsbootSanImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImagePathType.setStatus(_A)
_CucsLsbootSanImagePathVnicName_Type=SnmpAdminString
_CucsLsbootSanImagePathVnicName_Object=MibTableColumn
cucsLsbootSanImagePathVnicName=_CucsLsbootSanImagePathVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,6),_CucsLsbootSanImagePathVnicName_Type())
cucsLsbootSanImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImagePathVnicName.setStatus(_A)
_CucsLsbootSanImagePathWwn_Type=Unsigned64
_CucsLsbootSanImagePathWwn_Object=MibTableColumn
cucsLsbootSanImagePathWwn=_CucsLsbootSanImagePathWwn_Object((1,3,6,1,4,1,9,9,719,1,27,7,1,7),_CucsLsbootSanImagePathWwn_Type())
cucsLsbootSanImagePathWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanImagePathWwn.setStatus(_A)
_CucsLsbootStorageTable_Object=MibTable
cucsLsbootStorageTable=_CucsLsbootStorageTable_Object((1,3,6,1,4,1,9,9,719,1,27,8))
if mibBuilder.loadTexts:cucsLsbootStorageTable.setStatus(_A)
_CucsLsbootStorageEntry_Object=MibTableRow
cucsLsbootStorageEntry=_CucsLsbootStorageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,8,1))
cucsLsbootStorageEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cucsLsbootStorageEntry.setStatus(_A)
_CucsLsbootStorageInstanceId_Type=CucsManagedObjectId
_CucsLsbootStorageInstanceId_Object=MibTableColumn
cucsLsbootStorageInstanceId=_CucsLsbootStorageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,1),_CucsLsbootStorageInstanceId_Type())
cucsLsbootStorageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootStorageInstanceId.setStatus(_A)
_CucsLsbootStorageDn_Type=CucsManagedObjectDn
_CucsLsbootStorageDn_Object=MibTableColumn
cucsLsbootStorageDn=_CucsLsbootStorageDn_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,2),_CucsLsbootStorageDn_Type())
cucsLsbootStorageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootStorageDn.setStatus(_A)
_CucsLsbootStorageRn_Type=SnmpAdminString
_CucsLsbootStorageRn_Object=MibTableColumn
cucsLsbootStorageRn=_CucsLsbootStorageRn_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,3),_CucsLsbootStorageRn_Type())
cucsLsbootStorageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootStorageRn.setStatus(_A)
_CucsLsbootStorageAccess_Type=CucsLsbootStorageAccess
_CucsLsbootStorageAccess_Object=MibTableColumn
cucsLsbootStorageAccess=_CucsLsbootStorageAccess_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,4),_CucsLsbootStorageAccess_Type())
cucsLsbootStorageAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootStorageAccess.setStatus(_A)
_CucsLsbootStorageOrder_Type=Gauge32
_CucsLsbootStorageOrder_Object=MibTableColumn
cucsLsbootStorageOrder=_CucsLsbootStorageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,5),_CucsLsbootStorageOrder_Type())
cucsLsbootStorageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootStorageOrder.setStatus(_A)
_CucsLsbootStorageType_Type=CucsLsbootStorageType
_CucsLsbootStorageType_Object=MibTableColumn
cucsLsbootStorageType=_CucsLsbootStorageType_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,6),_CucsLsbootStorageType_Type())
cucsLsbootStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootStorageType.setStatus(_A)
_CucsLsbootStoragePropAcl_Type=Unsigned64
_CucsLsbootStoragePropAcl_Object=MibTableColumn
cucsLsbootStoragePropAcl=_CucsLsbootStoragePropAcl_Object((1,3,6,1,4,1,9,9,719,1,27,8,1,7),_CucsLsbootStoragePropAcl_Type())
cucsLsbootStoragePropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootStoragePropAcl.setStatus(_A)
_CucsLsbootVirtualMediaTable_Object=MibTable
cucsLsbootVirtualMediaTable=_CucsLsbootVirtualMediaTable_Object((1,3,6,1,4,1,9,9,719,1,27,9))
if mibBuilder.loadTexts:cucsLsbootVirtualMediaTable.setStatus(_A)
_CucsLsbootVirtualMediaEntry_Object=MibTableRow
cucsLsbootVirtualMediaEntry=_CucsLsbootVirtualMediaEntry_Object((1,3,6,1,4,1,9,9,719,1,27,9,1))
cucsLsbootVirtualMediaEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cucsLsbootVirtualMediaEntry.setStatus(_A)
_CucsLsbootVirtualMediaInstanceId_Type=CucsManagedObjectId
_CucsLsbootVirtualMediaInstanceId_Object=MibTableColumn
cucsLsbootVirtualMediaInstanceId=_CucsLsbootVirtualMediaInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,1),_CucsLsbootVirtualMediaInstanceId_Type())
cucsLsbootVirtualMediaInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaInstanceId.setStatus(_A)
_CucsLsbootVirtualMediaDn_Type=CucsManagedObjectDn
_CucsLsbootVirtualMediaDn_Object=MibTableColumn
cucsLsbootVirtualMediaDn=_CucsLsbootVirtualMediaDn_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,2),_CucsLsbootVirtualMediaDn_Type())
cucsLsbootVirtualMediaDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaDn.setStatus(_A)
_CucsLsbootVirtualMediaRn_Type=SnmpAdminString
_CucsLsbootVirtualMediaRn_Object=MibTableColumn
cucsLsbootVirtualMediaRn=_CucsLsbootVirtualMediaRn_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,3),_CucsLsbootVirtualMediaRn_Type())
cucsLsbootVirtualMediaRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaRn.setStatus(_A)
_CucsLsbootVirtualMediaAccess_Type=CucsLsbootAccessType
_CucsLsbootVirtualMediaAccess_Object=MibTableColumn
cucsLsbootVirtualMediaAccess=_CucsLsbootVirtualMediaAccess_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,4),_CucsLsbootVirtualMediaAccess_Type())
cucsLsbootVirtualMediaAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaAccess.setStatus(_A)
_CucsLsbootVirtualMediaOrder_Type=Gauge32
_CucsLsbootVirtualMediaOrder_Object=MibTableColumn
cucsLsbootVirtualMediaOrder=_CucsLsbootVirtualMediaOrder_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,5),_CucsLsbootVirtualMediaOrder_Type())
cucsLsbootVirtualMediaOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaOrder.setStatus(_A)
_CucsLsbootVirtualMediaType_Type=CucsLsbootVirtualMediaType
_CucsLsbootVirtualMediaType_Object=MibTableColumn
cucsLsbootVirtualMediaType=_CucsLsbootVirtualMediaType_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,6),_CucsLsbootVirtualMediaType_Type())
cucsLsbootVirtualMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaType.setStatus(_A)
_CucsLsbootVirtualMediaLunId_Type=SnmpAdminString
_CucsLsbootVirtualMediaLunId_Object=MibTableColumn
cucsLsbootVirtualMediaLunId=_CucsLsbootVirtualMediaLunId_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,7),_CucsLsbootVirtualMediaLunId_Type())
cucsLsbootVirtualMediaLunId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaLunId.setStatus(_A)
_CucsLsbootVirtualMediaMappingName_Type=SnmpAdminString
_CucsLsbootVirtualMediaMappingName_Object=MibTableColumn
cucsLsbootVirtualMediaMappingName=_CucsLsbootVirtualMediaMappingName_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,8),_CucsLsbootVirtualMediaMappingName_Type())
cucsLsbootVirtualMediaMappingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaMappingName.setStatus(_A)
_CucsLsbootVirtualMediaPropAcl_Type=Unsigned64
_CucsLsbootVirtualMediaPropAcl_Object=MibTableColumn
cucsLsbootVirtualMediaPropAcl=_CucsLsbootVirtualMediaPropAcl_Object((1,3,6,1,4,1,9,9,719,1,27,9,1,9),_CucsLsbootVirtualMediaPropAcl_Type())
cucsLsbootVirtualMediaPropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootVirtualMediaPropAcl.setStatus(_A)
_CucsLsbootIScsiTable_Object=MibTable
cucsLsbootIScsiTable=_CucsLsbootIScsiTable_Object((1,3,6,1,4,1,9,9,719,1,27,10))
if mibBuilder.loadTexts:cucsLsbootIScsiTable.setStatus(_A)
_CucsLsbootIScsiEntry_Object=MibTableRow
cucsLsbootIScsiEntry=_CucsLsbootIScsiEntry_Object((1,3,6,1,4,1,9,9,719,1,27,10,1))
cucsLsbootIScsiEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cucsLsbootIScsiEntry.setStatus(_A)
_CucsLsbootIScsiInstanceId_Type=CucsManagedObjectId
_CucsLsbootIScsiInstanceId_Object=MibTableColumn
cucsLsbootIScsiInstanceId=_CucsLsbootIScsiInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,10,1,1),_CucsLsbootIScsiInstanceId_Type())
cucsLsbootIScsiInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootIScsiInstanceId.setStatus(_A)
_CucsLsbootIScsiDn_Type=CucsManagedObjectDn
_CucsLsbootIScsiDn_Object=MibTableColumn
cucsLsbootIScsiDn=_CucsLsbootIScsiDn_Object((1,3,6,1,4,1,9,9,719,1,27,10,1,2),_CucsLsbootIScsiDn_Type())
cucsLsbootIScsiDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiDn.setStatus(_A)
_CucsLsbootIScsiRn_Type=SnmpAdminString
_CucsLsbootIScsiRn_Object=MibTableColumn
cucsLsbootIScsiRn=_CucsLsbootIScsiRn_Object((1,3,6,1,4,1,9,9,719,1,27,10,1,3),_CucsLsbootIScsiRn_Type())
cucsLsbootIScsiRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiRn.setStatus(_A)
_CucsLsbootIScsiAccess_Type=CucsLsbootIScsiAccess
_CucsLsbootIScsiAccess_Object=MibTableColumn
cucsLsbootIScsiAccess=_CucsLsbootIScsiAccess_Object((1,3,6,1,4,1,9,9,719,1,27,10,1,4),_CucsLsbootIScsiAccess_Type())
cucsLsbootIScsiAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiAccess.setStatus(_A)
_CucsLsbootIScsiOrder_Type=Gauge32
_CucsLsbootIScsiOrder_Object=MibTableColumn
cucsLsbootIScsiOrder=_CucsLsbootIScsiOrder_Object((1,3,6,1,4,1,9,9,719,1,27,10,1,5),_CucsLsbootIScsiOrder_Type())
cucsLsbootIScsiOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiOrder.setStatus(_A)
_CucsLsbootIScsiType_Type=CucsLsbootIScsiType
_CucsLsbootIScsiType_Object=MibTableColumn
cucsLsbootIScsiType=_CucsLsbootIScsiType_Object((1,3,6,1,4,1,9,9,719,1,27,10,1,6),_CucsLsbootIScsiType_Type())
cucsLsbootIScsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiType.setStatus(_A)
_CucsLsbootIScsiImagePathTable_Object=MibTable
cucsLsbootIScsiImagePathTable=_CucsLsbootIScsiImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,11))
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathTable.setStatus(_A)
_CucsLsbootIScsiImagePathEntry_Object=MibTableRow
cucsLsbootIScsiImagePathEntry=_CucsLsbootIScsiImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,11,1))
cucsLsbootIScsiImagePathEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathEntry.setStatus(_A)
_CucsLsbootIScsiImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootIScsiImagePathInstanceId_Object=MibTableColumn
cucsLsbootIScsiImagePathInstanceId=_CucsLsbootIScsiImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,11,1,1),_CucsLsbootIScsiImagePathInstanceId_Type())
cucsLsbootIScsiImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathInstanceId.setStatus(_A)
_CucsLsbootIScsiImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootIScsiImagePathDn_Object=MibTableColumn
cucsLsbootIScsiImagePathDn=_CucsLsbootIScsiImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,11,1,2),_CucsLsbootIScsiImagePathDn_Type())
cucsLsbootIScsiImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathDn.setStatus(_A)
_CucsLsbootIScsiImagePathRn_Type=SnmpAdminString
_CucsLsbootIScsiImagePathRn_Object=MibTableColumn
cucsLsbootIScsiImagePathRn=_CucsLsbootIScsiImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,11,1,3),_CucsLsbootIScsiImagePathRn_Type())
cucsLsbootIScsiImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathRn.setStatus(_A)
_CucsLsbootIScsiImagePathISCSIVnicName_Type=SnmpAdminString
_CucsLsbootIScsiImagePathISCSIVnicName_Object=MibTableColumn
cucsLsbootIScsiImagePathISCSIVnicName=_CucsLsbootIScsiImagePathISCSIVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,11,1,4),_CucsLsbootIScsiImagePathISCSIVnicName_Type())
cucsLsbootIScsiImagePathISCSIVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathISCSIVnicName.setStatus(_A)
_CucsLsbootIScsiImagePathType_Type=CucsLsbootIScsiImagePathType
_CucsLsbootIScsiImagePathType_Object=MibTableColumn
cucsLsbootIScsiImagePathType=_CucsLsbootIScsiImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,11,1,5),_CucsLsbootIScsiImagePathType_Type())
cucsLsbootIScsiImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathType.setStatus(_A)
_CucsLsbootIScsiImagePathVnicName_Type=SnmpAdminString
_CucsLsbootIScsiImagePathVnicName_Object=MibTableColumn
cucsLsbootIScsiImagePathVnicName=_CucsLsbootIScsiImagePathVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,11,1,6),_CucsLsbootIScsiImagePathVnicName_Type())
cucsLsbootIScsiImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootIScsiImagePathVnicName.setStatus(_A)
_CucsLsbootBootSecurityTable_Object=MibTable
cucsLsbootBootSecurityTable=_CucsLsbootBootSecurityTable_Object((1,3,6,1,4,1,9,9,719,1,27,12))
if mibBuilder.loadTexts:cucsLsbootBootSecurityTable.setStatus(_A)
_CucsLsbootBootSecurityEntry_Object=MibTableRow
cucsLsbootBootSecurityEntry=_CucsLsbootBootSecurityEntry_Object((1,3,6,1,4,1,9,9,719,1,27,12,1))
cucsLsbootBootSecurityEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cucsLsbootBootSecurityEntry.setStatus(_A)
_CucsLsbootBootSecurityInstanceId_Type=CucsManagedObjectId
_CucsLsbootBootSecurityInstanceId_Object=MibTableColumn
cucsLsbootBootSecurityInstanceId=_CucsLsbootBootSecurityInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,12,1,1),_CucsLsbootBootSecurityInstanceId_Type())
cucsLsbootBootSecurityInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootBootSecurityInstanceId.setStatus(_A)
_CucsLsbootBootSecurityDn_Type=CucsManagedObjectDn
_CucsLsbootBootSecurityDn_Object=MibTableColumn
cucsLsbootBootSecurityDn=_CucsLsbootBootSecurityDn_Object((1,3,6,1,4,1,9,9,719,1,27,12,1,2),_CucsLsbootBootSecurityDn_Type())
cucsLsbootBootSecurityDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootBootSecurityDn.setStatus(_A)
_CucsLsbootBootSecurityRn_Type=SnmpAdminString
_CucsLsbootBootSecurityRn_Object=MibTableColumn
cucsLsbootBootSecurityRn=_CucsLsbootBootSecurityRn_Object((1,3,6,1,4,1,9,9,719,1,27,12,1,3),_CucsLsbootBootSecurityRn_Type())
cucsLsbootBootSecurityRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootBootSecurityRn.setStatus(_A)
_CucsLsbootBootSecuritySecureBoot_Type=TruthValue
_CucsLsbootBootSecuritySecureBoot_Object=MibTableColumn
cucsLsbootBootSecuritySecureBoot=_CucsLsbootBootSecuritySecureBoot_Object((1,3,6,1,4,1,9,9,719,1,27,12,1,4),_CucsLsbootBootSecuritySecureBoot_Type())
cucsLsbootBootSecuritySecureBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootBootSecuritySecureBoot.setStatus(_A)
_CucsLsbootDefaultLocalImageTable_Object=MibTable
cucsLsbootDefaultLocalImageTable=_CucsLsbootDefaultLocalImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,13))
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageTable.setStatus(_A)
_CucsLsbootDefaultLocalImageEntry_Object=MibTableRow
cucsLsbootDefaultLocalImageEntry=_CucsLsbootDefaultLocalImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,13,1))
cucsLsbootDefaultLocalImageEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageEntry.setStatus(_A)
_CucsLsbootDefaultLocalImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootDefaultLocalImageInstanceId_Object=MibTableColumn
cucsLsbootDefaultLocalImageInstanceId=_CucsLsbootDefaultLocalImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,13,1,1),_CucsLsbootDefaultLocalImageInstanceId_Type())
cucsLsbootDefaultLocalImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageInstanceId.setStatus(_A)
_CucsLsbootDefaultLocalImageDn_Type=CucsManagedObjectDn
_CucsLsbootDefaultLocalImageDn_Object=MibTableColumn
cucsLsbootDefaultLocalImageDn=_CucsLsbootDefaultLocalImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,13,1,2),_CucsLsbootDefaultLocalImageDn_Type())
cucsLsbootDefaultLocalImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageDn.setStatus(_A)
_CucsLsbootDefaultLocalImageRn_Type=SnmpAdminString
_CucsLsbootDefaultLocalImageRn_Object=MibTableColumn
cucsLsbootDefaultLocalImageRn=_CucsLsbootDefaultLocalImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,13,1,3),_CucsLsbootDefaultLocalImageRn_Type())
cucsLsbootDefaultLocalImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageRn.setStatus(_A)
_CucsLsbootDefaultLocalImageOrder_Type=Gauge32
_CucsLsbootDefaultLocalImageOrder_Object=MibTableColumn
cucsLsbootDefaultLocalImageOrder=_CucsLsbootDefaultLocalImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,13,1,6),_CucsLsbootDefaultLocalImageOrder_Type())
cucsLsbootDefaultLocalImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageOrder.setStatus(_A)
_CucsLsbootDefaultLocalImageType_Type=CucsLsbootDefaultLocalImageType
_CucsLsbootDefaultLocalImageType_Object=MibTableColumn
cucsLsbootDefaultLocalImageType=_CucsLsbootDefaultLocalImageType_Object((1,3,6,1,4,1,9,9,719,1,27,13,1,7),_CucsLsbootDefaultLocalImageType_Type())
cucsLsbootDefaultLocalImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImageType.setStatus(_A)
_CucsLsbootDefaultLocalImagePropAcl_Type=Unsigned64
_CucsLsbootDefaultLocalImagePropAcl_Object=MibTableColumn
cucsLsbootDefaultLocalImagePropAcl=_CucsLsbootDefaultLocalImagePropAcl_Object((1,3,6,1,4,1,9,9,719,1,27,13,1,8),_CucsLsbootDefaultLocalImagePropAcl_Type())
cucsLsbootDefaultLocalImagePropAcl.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootDefaultLocalImagePropAcl.setStatus(_A)
_CucsLsbootLocalHddImageTable_Object=MibTable
cucsLsbootLocalHddImageTable=_CucsLsbootLocalHddImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,14))
if mibBuilder.loadTexts:cucsLsbootLocalHddImageTable.setStatus(_A)
_CucsLsbootLocalHddImageEntry_Object=MibTableRow
cucsLsbootLocalHddImageEntry=_CucsLsbootLocalHddImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,14,1))
cucsLsbootLocalHddImageEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cucsLsbootLocalHddImageEntry.setStatus(_A)
_CucsLsbootLocalHddImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootLocalHddImageInstanceId_Object=MibTableColumn
cucsLsbootLocalHddImageInstanceId=_CucsLsbootLocalHddImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,14,1,1),_CucsLsbootLocalHddImageInstanceId_Type())
cucsLsbootLocalHddImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLocalHddImageInstanceId.setStatus(_A)
_CucsLsbootLocalHddImageDn_Type=CucsManagedObjectDn
_CucsLsbootLocalHddImageDn_Object=MibTableColumn
cucsLsbootLocalHddImageDn=_CucsLsbootLocalHddImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,14,1,2),_CucsLsbootLocalHddImageDn_Type())
cucsLsbootLocalHddImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalHddImageDn.setStatus(_A)
_CucsLsbootLocalHddImageRn_Type=SnmpAdminString
_CucsLsbootLocalHddImageRn_Object=MibTableColumn
cucsLsbootLocalHddImageRn=_CucsLsbootLocalHddImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,14,1,3),_CucsLsbootLocalHddImageRn_Type())
cucsLsbootLocalHddImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalHddImageRn.setStatus(_A)
_CucsLsbootLocalHddImageOrder_Type=Gauge32
_CucsLsbootLocalHddImageOrder_Object=MibTableColumn
cucsLsbootLocalHddImageOrder=_CucsLsbootLocalHddImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,14,1,6),_CucsLsbootLocalHddImageOrder_Type())
cucsLsbootLocalHddImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalHddImageOrder.setStatus(_A)
_CucsLsbootLocalHddImageType_Type=CucsLsbootLocalHddImageType
_CucsLsbootLocalHddImageType_Object=MibTableColumn
cucsLsbootLocalHddImageType=_CucsLsbootLocalHddImageType_Object((1,3,6,1,4,1,9,9,719,1,27,14,1,7),_CucsLsbootLocalHddImageType_Type())
cucsLsbootLocalHddImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalHddImageType.setStatus(_A)
_CucsLsbootSanTable_Object=MibTable
cucsLsbootSanTable=_CucsLsbootSanTable_Object((1,3,6,1,4,1,9,9,719,1,27,15))
if mibBuilder.loadTexts:cucsLsbootSanTable.setStatus(_A)
_CucsLsbootSanEntry_Object=MibTableRow
cucsLsbootSanEntry=_CucsLsbootSanEntry_Object((1,3,6,1,4,1,9,9,719,1,27,15,1))
cucsLsbootSanEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cucsLsbootSanEntry.setStatus(_A)
_CucsLsbootSanInstanceId_Type=CucsManagedObjectId
_CucsLsbootSanInstanceId_Object=MibTableColumn
cucsLsbootSanInstanceId=_CucsLsbootSanInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,15,1,1),_CucsLsbootSanInstanceId_Type())
cucsLsbootSanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootSanInstanceId.setStatus(_A)
_CucsLsbootSanDn_Type=CucsManagedObjectDn
_CucsLsbootSanDn_Object=MibTableColumn
cucsLsbootSanDn=_CucsLsbootSanDn_Object((1,3,6,1,4,1,9,9,719,1,27,15,1,2),_CucsLsbootSanDn_Type())
cucsLsbootSanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanDn.setStatus(_A)
_CucsLsbootSanRn_Type=SnmpAdminString
_CucsLsbootSanRn_Object=MibTableColumn
cucsLsbootSanRn=_CucsLsbootSanRn_Object((1,3,6,1,4,1,9,9,719,1,27,15,1,3),_CucsLsbootSanRn_Type())
cucsLsbootSanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanRn.setStatus(_A)
_CucsLsbootSanAccess_Type=CucsLsbootSanAccess
_CucsLsbootSanAccess_Object=MibTableColumn
cucsLsbootSanAccess=_CucsLsbootSanAccess_Object((1,3,6,1,4,1,9,9,719,1,27,15,1,4),_CucsLsbootSanAccess_Type())
cucsLsbootSanAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanAccess.setStatus(_A)
_CucsLsbootSanOrder_Type=Gauge32
_CucsLsbootSanOrder_Object=MibTableColumn
cucsLsbootSanOrder=_CucsLsbootSanOrder_Object((1,3,6,1,4,1,9,9,719,1,27,15,1,5),_CucsLsbootSanOrder_Type())
cucsLsbootSanOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanOrder.setStatus(_A)
_CucsLsbootSanType_Type=CucsLsbootSanType
_CucsLsbootSanType_Object=MibTableColumn
cucsLsbootSanType=_CucsLsbootSanType_Object((1,3,6,1,4,1,9,9,719,1,27,15,1,6),_CucsLsbootSanType_Type())
cucsLsbootSanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanType.setStatus(_A)
_CucsLsbootSanCatSanImageTable_Object=MibTable
cucsLsbootSanCatSanImageTable=_CucsLsbootSanCatSanImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,16))
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageTable.setStatus(_A)
_CucsLsbootSanCatSanImageEntry_Object=MibTableRow
cucsLsbootSanCatSanImageEntry=_CucsLsbootSanCatSanImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,16,1))
cucsLsbootSanCatSanImageEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageEntry.setStatus(_A)
_CucsLsbootSanCatSanImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootSanCatSanImageInstanceId_Object=MibTableColumn
cucsLsbootSanCatSanImageInstanceId=_CucsLsbootSanCatSanImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,16,1,1),_CucsLsbootSanCatSanImageInstanceId_Type())
cucsLsbootSanCatSanImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageInstanceId.setStatus(_A)
_CucsLsbootSanCatSanImageDn_Type=CucsManagedObjectDn
_CucsLsbootSanCatSanImageDn_Object=MibTableColumn
cucsLsbootSanCatSanImageDn=_CucsLsbootSanCatSanImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,16,1,2),_CucsLsbootSanCatSanImageDn_Type())
cucsLsbootSanCatSanImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageDn.setStatus(_A)
_CucsLsbootSanCatSanImageRn_Type=SnmpAdminString
_CucsLsbootSanCatSanImageRn_Object=MibTableColumn
cucsLsbootSanCatSanImageRn=_CucsLsbootSanCatSanImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,16,1,3),_CucsLsbootSanCatSanImageRn_Type())
cucsLsbootSanCatSanImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageRn.setStatus(_A)
_CucsLsbootSanCatSanImageType_Type=CucsLsbootSanCatSanImageType
_CucsLsbootSanCatSanImageType_Object=MibTableColumn
cucsLsbootSanCatSanImageType=_CucsLsbootSanCatSanImageType_Object((1,3,6,1,4,1,9,9,719,1,27,16,1,4),_CucsLsbootSanCatSanImageType_Type())
cucsLsbootSanCatSanImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageType.setStatus(_A)
_CucsLsbootSanCatSanImageVnicName_Type=SnmpAdminString
_CucsLsbootSanCatSanImageVnicName_Object=MibTableColumn
cucsLsbootSanCatSanImageVnicName=_CucsLsbootSanCatSanImageVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,16,1,5),_CucsLsbootSanCatSanImageVnicName_Type())
cucsLsbootSanCatSanImageVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImageVnicName.setStatus(_A)
_CucsLsbootSanCatSanImagePathTable_Object=MibTable
cucsLsbootSanCatSanImagePathTable=_CucsLsbootSanCatSanImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,17))
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathTable.setStatus(_A)
_CucsLsbootSanCatSanImagePathEntry_Object=MibTableRow
cucsLsbootSanCatSanImagePathEntry=_CucsLsbootSanCatSanImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,17,1))
cucsLsbootSanCatSanImagePathEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathEntry.setStatus(_A)
_CucsLsbootSanCatSanImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootSanCatSanImagePathInstanceId_Object=MibTableColumn
cucsLsbootSanCatSanImagePathInstanceId=_CucsLsbootSanCatSanImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,1),_CucsLsbootSanCatSanImagePathInstanceId_Type())
cucsLsbootSanCatSanImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathInstanceId.setStatus(_A)
_CucsLsbootSanCatSanImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootSanCatSanImagePathDn_Object=MibTableColumn
cucsLsbootSanCatSanImagePathDn=_CucsLsbootSanCatSanImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,2),_CucsLsbootSanCatSanImagePathDn_Type())
cucsLsbootSanCatSanImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathDn.setStatus(_A)
_CucsLsbootSanCatSanImagePathRn_Type=SnmpAdminString
_CucsLsbootSanCatSanImagePathRn_Object=MibTableColumn
cucsLsbootSanCatSanImagePathRn=_CucsLsbootSanCatSanImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,3),_CucsLsbootSanCatSanImagePathRn_Type())
cucsLsbootSanCatSanImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathRn.setStatus(_A)
_CucsLsbootSanCatSanImagePathLun_Type=SnmpAdminString
_CucsLsbootSanCatSanImagePathLun_Object=MibTableColumn
cucsLsbootSanCatSanImagePathLun=_CucsLsbootSanCatSanImagePathLun_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,4),_CucsLsbootSanCatSanImagePathLun_Type())
cucsLsbootSanCatSanImagePathLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathLun.setStatus(_A)
_CucsLsbootSanCatSanImagePathType_Type=CucsLsbootSanCatSanImagePathType
_CucsLsbootSanCatSanImagePathType_Object=MibTableColumn
cucsLsbootSanCatSanImagePathType=_CucsLsbootSanCatSanImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,5),_CucsLsbootSanCatSanImagePathType_Type())
cucsLsbootSanCatSanImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathType.setStatus(_A)
_CucsLsbootSanCatSanImagePathVnicName_Type=SnmpAdminString
_CucsLsbootSanCatSanImagePathVnicName_Object=MibTableColumn
cucsLsbootSanCatSanImagePathVnicName=_CucsLsbootSanCatSanImagePathVnicName_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,6),_CucsLsbootSanCatSanImagePathVnicName_Type())
cucsLsbootSanCatSanImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathVnicName.setStatus(_A)
_CucsLsbootSanCatSanImagePathWwn_Type=Unsigned64
_CucsLsbootSanCatSanImagePathWwn_Object=MibTableColumn
cucsLsbootSanCatSanImagePathWwn=_CucsLsbootSanCatSanImagePathWwn_Object((1,3,6,1,4,1,9,9,719,1,27,17,1,7),_CucsLsbootSanCatSanImagePathWwn_Type())
cucsLsbootSanCatSanImagePathWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootSanCatSanImagePathWwn.setStatus(_A)
_CucsLsbootUsbExternalImageTable_Object=MibTable
cucsLsbootUsbExternalImageTable=_CucsLsbootUsbExternalImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,18))
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageTable.setStatus(_A)
_CucsLsbootUsbExternalImageEntry_Object=MibTableRow
cucsLsbootUsbExternalImageEntry=_CucsLsbootUsbExternalImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,18,1))
cucsLsbootUsbExternalImageEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageEntry.setStatus(_A)
_CucsLsbootUsbExternalImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootUsbExternalImageInstanceId_Object=MibTableColumn
cucsLsbootUsbExternalImageInstanceId=_CucsLsbootUsbExternalImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,18,1,1),_CucsLsbootUsbExternalImageInstanceId_Type())
cucsLsbootUsbExternalImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageInstanceId.setStatus(_A)
_CucsLsbootUsbExternalImageDn_Type=CucsManagedObjectDn
_CucsLsbootUsbExternalImageDn_Object=MibTableColumn
cucsLsbootUsbExternalImageDn=_CucsLsbootUsbExternalImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,18,1,2),_CucsLsbootUsbExternalImageDn_Type())
cucsLsbootUsbExternalImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageDn.setStatus(_A)
_CucsLsbootUsbExternalImageRn_Type=SnmpAdminString
_CucsLsbootUsbExternalImageRn_Object=MibTableColumn
cucsLsbootUsbExternalImageRn=_CucsLsbootUsbExternalImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,18,1,3),_CucsLsbootUsbExternalImageRn_Type())
cucsLsbootUsbExternalImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageRn.setStatus(_A)
_CucsLsbootUsbExternalImageOrder_Type=Gauge32
_CucsLsbootUsbExternalImageOrder_Object=MibTableColumn
cucsLsbootUsbExternalImageOrder=_CucsLsbootUsbExternalImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,18,1,6),_CucsLsbootUsbExternalImageOrder_Type())
cucsLsbootUsbExternalImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageOrder.setStatus(_A)
_CucsLsbootUsbExternalImageType_Type=CucsLsbootUsbExternalImageType
_CucsLsbootUsbExternalImageType_Object=MibTableColumn
cucsLsbootUsbExternalImageType=_CucsLsbootUsbExternalImageType_Object((1,3,6,1,4,1,9,9,719,1,27,18,1,7),_CucsLsbootUsbExternalImageType_Type())
cucsLsbootUsbExternalImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbExternalImageType.setStatus(_A)
_CucsLsbootUsbFlashStorageImageTable_Object=MibTable
cucsLsbootUsbFlashStorageImageTable=_CucsLsbootUsbFlashStorageImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,19))
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageTable.setStatus(_A)
_CucsLsbootUsbFlashStorageImageEntry_Object=MibTableRow
cucsLsbootUsbFlashStorageImageEntry=_CucsLsbootUsbFlashStorageImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,19,1))
cucsLsbootUsbFlashStorageImageEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageEntry.setStatus(_A)
_CucsLsbootUsbFlashStorageImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootUsbFlashStorageImageInstanceId_Object=MibTableColumn
cucsLsbootUsbFlashStorageImageInstanceId=_CucsLsbootUsbFlashStorageImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,19,1,1),_CucsLsbootUsbFlashStorageImageInstanceId_Type())
cucsLsbootUsbFlashStorageImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageInstanceId.setStatus(_A)
_CucsLsbootUsbFlashStorageImageDn_Type=CucsManagedObjectDn
_CucsLsbootUsbFlashStorageImageDn_Object=MibTableColumn
cucsLsbootUsbFlashStorageImageDn=_CucsLsbootUsbFlashStorageImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,19,1,2),_CucsLsbootUsbFlashStorageImageDn_Type())
cucsLsbootUsbFlashStorageImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageDn.setStatus(_A)
_CucsLsbootUsbFlashStorageImageRn_Type=SnmpAdminString
_CucsLsbootUsbFlashStorageImageRn_Object=MibTableColumn
cucsLsbootUsbFlashStorageImageRn=_CucsLsbootUsbFlashStorageImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,19,1,3),_CucsLsbootUsbFlashStorageImageRn_Type())
cucsLsbootUsbFlashStorageImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageRn.setStatus(_A)
_CucsLsbootUsbFlashStorageImageOrder_Type=Gauge32
_CucsLsbootUsbFlashStorageImageOrder_Object=MibTableColumn
cucsLsbootUsbFlashStorageImageOrder=_CucsLsbootUsbFlashStorageImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,19,1,6),_CucsLsbootUsbFlashStorageImageOrder_Type())
cucsLsbootUsbFlashStorageImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageOrder.setStatus(_A)
_CucsLsbootUsbFlashStorageImageType_Type=CucsLsbootUsbFlashStorageImageType
_CucsLsbootUsbFlashStorageImageType_Object=MibTableColumn
cucsLsbootUsbFlashStorageImageType=_CucsLsbootUsbFlashStorageImageType_Object((1,3,6,1,4,1,9,9,719,1,27,19,1,7),_CucsLsbootUsbFlashStorageImageType_Type())
cucsLsbootUsbFlashStorageImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbFlashStorageImageType.setStatus(_A)
_CucsLsbootUsbInternalImageTable_Object=MibTable
cucsLsbootUsbInternalImageTable=_CucsLsbootUsbInternalImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,20))
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageTable.setStatus(_A)
_CucsLsbootUsbInternalImageEntry_Object=MibTableRow
cucsLsbootUsbInternalImageEntry=_CucsLsbootUsbInternalImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,20,1))
cucsLsbootUsbInternalImageEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageEntry.setStatus(_A)
_CucsLsbootUsbInternalImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootUsbInternalImageInstanceId_Object=MibTableColumn
cucsLsbootUsbInternalImageInstanceId=_CucsLsbootUsbInternalImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,20,1,1),_CucsLsbootUsbInternalImageInstanceId_Type())
cucsLsbootUsbInternalImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageInstanceId.setStatus(_A)
_CucsLsbootUsbInternalImageDn_Type=CucsManagedObjectDn
_CucsLsbootUsbInternalImageDn_Object=MibTableColumn
cucsLsbootUsbInternalImageDn=_CucsLsbootUsbInternalImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,20,1,2),_CucsLsbootUsbInternalImageDn_Type())
cucsLsbootUsbInternalImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageDn.setStatus(_A)
_CucsLsbootUsbInternalImageRn_Type=SnmpAdminString
_CucsLsbootUsbInternalImageRn_Object=MibTableColumn
cucsLsbootUsbInternalImageRn=_CucsLsbootUsbInternalImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,20,1,3),_CucsLsbootUsbInternalImageRn_Type())
cucsLsbootUsbInternalImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageRn.setStatus(_A)
_CucsLsbootUsbInternalImageOrder_Type=Gauge32
_CucsLsbootUsbInternalImageOrder_Object=MibTableColumn
cucsLsbootUsbInternalImageOrder=_CucsLsbootUsbInternalImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,20,1,6),_CucsLsbootUsbInternalImageOrder_Type())
cucsLsbootUsbInternalImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageOrder.setStatus(_A)
_CucsLsbootUsbInternalImageType_Type=CucsLsbootUsbInternalImageType
_CucsLsbootUsbInternalImageType_Object=MibTableColumn
cucsLsbootUsbInternalImageType=_CucsLsbootUsbInternalImageType_Object((1,3,6,1,4,1,9,9,719,1,27,20,1,7),_CucsLsbootUsbInternalImageType_Type())
cucsLsbootUsbInternalImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUsbInternalImageType.setStatus(_A)
_CucsLsbootLocalDiskImageTable_Object=MibTable
cucsLsbootLocalDiskImageTable=_CucsLsbootLocalDiskImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,21))
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageTable.setStatus(_A)
_CucsLsbootLocalDiskImageEntry_Object=MibTableRow
cucsLsbootLocalDiskImageEntry=_CucsLsbootLocalDiskImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,21,1))
cucsLsbootLocalDiskImageEntry.setIndexNames((0,_C,_Y))
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageEntry.setStatus(_A)
_CucsLsbootLocalDiskImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootLocalDiskImageInstanceId_Object=MibTableColumn
cucsLsbootLocalDiskImageInstanceId=_CucsLsbootLocalDiskImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,21,1,1),_CucsLsbootLocalDiskImageInstanceId_Type())
cucsLsbootLocalDiskImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageInstanceId.setStatus(_A)
_CucsLsbootLocalDiskImageDn_Type=CucsManagedObjectDn
_CucsLsbootLocalDiskImageDn_Object=MibTableColumn
cucsLsbootLocalDiskImageDn=_CucsLsbootLocalDiskImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,21,1,2),_CucsLsbootLocalDiskImageDn_Type())
cucsLsbootLocalDiskImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageDn.setStatus(_A)
_CucsLsbootLocalDiskImageRn_Type=SnmpAdminString
_CucsLsbootLocalDiskImageRn_Object=MibTableColumn
cucsLsbootLocalDiskImageRn=_CucsLsbootLocalDiskImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,21,1,3),_CucsLsbootLocalDiskImageRn_Type())
cucsLsbootLocalDiskImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageRn.setStatus(_A)
_CucsLsbootLocalDiskImageOrder_Type=Gauge32
_CucsLsbootLocalDiskImageOrder_Object=MibTableColumn
cucsLsbootLocalDiskImageOrder=_CucsLsbootLocalDiskImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,21,1,4),_CucsLsbootLocalDiskImageOrder_Type())
cucsLsbootLocalDiskImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageOrder.setStatus(_A)
_CucsLsbootLocalDiskImageType_Type=CucsLsbootLocalDiskImageType
_CucsLsbootLocalDiskImageType_Object=MibTableColumn
cucsLsbootLocalDiskImageType=_CucsLsbootLocalDiskImageType_Object((1,3,6,1,4,1,9,9,719,1,27,21,1,5),_CucsLsbootLocalDiskImageType_Type())
cucsLsbootLocalDiskImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImageType.setStatus(_A)
_CucsLsbootLocalDiskImagePathTable_Object=MibTable
cucsLsbootLocalDiskImagePathTable=_CucsLsbootLocalDiskImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,22))
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathTable.setStatus(_A)
_CucsLsbootLocalDiskImagePathEntry_Object=MibTableRow
cucsLsbootLocalDiskImagePathEntry=_CucsLsbootLocalDiskImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,22,1))
cucsLsbootLocalDiskImagePathEntry.setIndexNames((0,_C,_Z))
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathEntry.setStatus(_A)
_CucsLsbootLocalDiskImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootLocalDiskImagePathInstanceId_Object=MibTableColumn
cucsLsbootLocalDiskImagePathInstanceId=_CucsLsbootLocalDiskImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,22,1,1),_CucsLsbootLocalDiskImagePathInstanceId_Type())
cucsLsbootLocalDiskImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathInstanceId.setStatus(_A)
_CucsLsbootLocalDiskImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootLocalDiskImagePathDn_Object=MibTableColumn
cucsLsbootLocalDiskImagePathDn=_CucsLsbootLocalDiskImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,22,1,2),_CucsLsbootLocalDiskImagePathDn_Type())
cucsLsbootLocalDiskImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathDn.setStatus(_A)
_CucsLsbootLocalDiskImagePathRn_Type=SnmpAdminString
_CucsLsbootLocalDiskImagePathRn_Object=MibTableColumn
cucsLsbootLocalDiskImagePathRn=_CucsLsbootLocalDiskImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,22,1,3),_CucsLsbootLocalDiskImagePathRn_Type())
cucsLsbootLocalDiskImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathRn.setStatus(_A)
_CucsLsbootLocalDiskImagePathSlotNumber_Type=Gauge32
_CucsLsbootLocalDiskImagePathSlotNumber_Object=MibTableColumn
cucsLsbootLocalDiskImagePathSlotNumber=_CucsLsbootLocalDiskImagePathSlotNumber_Object((1,3,6,1,4,1,9,9,719,1,27,22,1,4),_CucsLsbootLocalDiskImagePathSlotNumber_Type())
cucsLsbootLocalDiskImagePathSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathSlotNumber.setStatus(_A)
_CucsLsbootLocalDiskImagePathType_Type=CucsLsbootLocalDiskImagePathType
_CucsLsbootLocalDiskImagePathType_Object=MibTableColumn
cucsLsbootLocalDiskImagePathType=_CucsLsbootLocalDiskImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,22,1,5),_CucsLsbootLocalDiskImagePathType_Type())
cucsLsbootLocalDiskImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalDiskImagePathType.setStatus(_A)
_CucsLsbootLocalLunImagePathTable_Object=MibTable
cucsLsbootLocalLunImagePathTable=_CucsLsbootLocalLunImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,23))
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathTable.setStatus(_A)
_CucsLsbootLocalLunImagePathEntry_Object=MibTableRow
cucsLsbootLocalLunImagePathEntry=_CucsLsbootLocalLunImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,23,1))
cucsLsbootLocalLunImagePathEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathEntry.setStatus(_A)
_CucsLsbootLocalLunImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootLocalLunImagePathInstanceId_Object=MibTableColumn
cucsLsbootLocalLunImagePathInstanceId=_CucsLsbootLocalLunImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,23,1,1),_CucsLsbootLocalLunImagePathInstanceId_Type())
cucsLsbootLocalLunImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathInstanceId.setStatus(_A)
_CucsLsbootLocalLunImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootLocalLunImagePathDn_Object=MibTableColumn
cucsLsbootLocalLunImagePathDn=_CucsLsbootLocalLunImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,23,1,2),_CucsLsbootLocalLunImagePathDn_Type())
cucsLsbootLocalLunImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathDn.setStatus(_A)
_CucsLsbootLocalLunImagePathRn_Type=SnmpAdminString
_CucsLsbootLocalLunImagePathRn_Object=MibTableColumn
cucsLsbootLocalLunImagePathRn=_CucsLsbootLocalLunImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,23,1,3),_CucsLsbootLocalLunImagePathRn_Type())
cucsLsbootLocalLunImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathRn.setStatus(_A)
_CucsLsbootLocalLunImagePathLunName_Type=SnmpAdminString
_CucsLsbootLocalLunImagePathLunName_Object=MibTableColumn
cucsLsbootLocalLunImagePathLunName=_CucsLsbootLocalLunImagePathLunName_Object((1,3,6,1,4,1,9,9,719,1,27,23,1,4),_CucsLsbootLocalLunImagePathLunName_Type())
cucsLsbootLocalLunImagePathLunName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathLunName.setStatus(_A)
_CucsLsbootLocalLunImagePathType_Type=CucsLsbootLocalLunImagePathType
_CucsLsbootLocalLunImagePathType_Object=MibTableColumn
cucsLsbootLocalLunImagePathType=_CucsLsbootLocalLunImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,23,1,5),_CucsLsbootLocalLunImagePathType_Type())
cucsLsbootLocalLunImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootLocalLunImagePathType.setStatus(_A)
_CucsLsbootUEFIBootParamTable_Object=MibTable
cucsLsbootUEFIBootParamTable=_CucsLsbootUEFIBootParamTable_Object((1,3,6,1,4,1,9,9,719,1,27,24))
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamTable.setStatus(_A)
_CucsLsbootUEFIBootParamEntry_Object=MibTableRow
cucsLsbootUEFIBootParamEntry=_CucsLsbootUEFIBootParamEntry_Object((1,3,6,1,4,1,9,9,719,1,27,24,1))
cucsLsbootUEFIBootParamEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamEntry.setStatus(_A)
_CucsLsbootUEFIBootParamInstanceId_Type=CucsManagedObjectId
_CucsLsbootUEFIBootParamInstanceId_Object=MibTableColumn
cucsLsbootUEFIBootParamInstanceId=_CucsLsbootUEFIBootParamInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,24,1,1),_CucsLsbootUEFIBootParamInstanceId_Type())
cucsLsbootUEFIBootParamInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamInstanceId.setStatus(_A)
_CucsLsbootUEFIBootParamDn_Type=CucsManagedObjectDn
_CucsLsbootUEFIBootParamDn_Object=MibTableColumn
cucsLsbootUEFIBootParamDn=_CucsLsbootUEFIBootParamDn_Object((1,3,6,1,4,1,9,9,719,1,27,24,1,2),_CucsLsbootUEFIBootParamDn_Type())
cucsLsbootUEFIBootParamDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamDn.setStatus(_A)
_CucsLsbootUEFIBootParamRn_Type=SnmpAdminString
_CucsLsbootUEFIBootParamRn_Object=MibTableColumn
cucsLsbootUEFIBootParamRn=_CucsLsbootUEFIBootParamRn_Object((1,3,6,1,4,1,9,9,719,1,27,24,1,3),_CucsLsbootUEFIBootParamRn_Type())
cucsLsbootUEFIBootParamRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamRn.setStatus(_A)
_CucsLsbootUEFIBootParamBootDescription_Type=SnmpAdminString
_CucsLsbootUEFIBootParamBootDescription_Object=MibTableColumn
cucsLsbootUEFIBootParamBootDescription=_CucsLsbootUEFIBootParamBootDescription_Object((1,3,6,1,4,1,9,9,719,1,27,24,1,4),_CucsLsbootUEFIBootParamBootDescription_Type())
cucsLsbootUEFIBootParamBootDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamBootDescription.setStatus(_A)
_CucsLsbootUEFIBootParamBootLoaderName_Type=SnmpAdminString
_CucsLsbootUEFIBootParamBootLoaderName_Object=MibTableColumn
cucsLsbootUEFIBootParamBootLoaderName=_CucsLsbootUEFIBootParamBootLoaderName_Object((1,3,6,1,4,1,9,9,719,1,27,24,1,5),_CucsLsbootUEFIBootParamBootLoaderName_Type())
cucsLsbootUEFIBootParamBootLoaderName.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamBootLoaderName.setStatus(_A)
_CucsLsbootUEFIBootParamBootLoaderPath_Type=SnmpAdminString
_CucsLsbootUEFIBootParamBootLoaderPath_Object=MibTableColumn
cucsLsbootUEFIBootParamBootLoaderPath=_CucsLsbootUEFIBootParamBootLoaderPath_Object((1,3,6,1,4,1,9,9,719,1,27,24,1,6),_CucsLsbootUEFIBootParamBootLoaderPath_Type())
cucsLsbootUEFIBootParamBootLoaderPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootUEFIBootParamBootLoaderPath.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageTable_Object=MibTable
cucsLsbootEmbeddedLocalDiskImageTable=_CucsLsbootEmbeddedLocalDiskImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,25))
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageTable.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageEntry_Object=MibTableRow
cucsLsbootEmbeddedLocalDiskImageEntry=_CucsLsbootEmbeddedLocalDiskImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,25,1))
cucsLsbootEmbeddedLocalDiskImageEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageEntry.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootEmbeddedLocalDiskImageInstanceId_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImageInstanceId=_CucsLsbootEmbeddedLocalDiskImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,25,1,1),_CucsLsbootEmbeddedLocalDiskImageInstanceId_Type())
cucsLsbootEmbeddedLocalDiskImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageInstanceId.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageDn_Type=CucsManagedObjectDn
_CucsLsbootEmbeddedLocalDiskImageDn_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImageDn=_CucsLsbootEmbeddedLocalDiskImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,25,1,2),_CucsLsbootEmbeddedLocalDiskImageDn_Type())
cucsLsbootEmbeddedLocalDiskImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageDn.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageRn_Type=SnmpAdminString
_CucsLsbootEmbeddedLocalDiskImageRn_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImageRn=_CucsLsbootEmbeddedLocalDiskImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,25,1,3),_CucsLsbootEmbeddedLocalDiskImageRn_Type())
cucsLsbootEmbeddedLocalDiskImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageRn.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageOrder_Type=Gauge32
_CucsLsbootEmbeddedLocalDiskImageOrder_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImageOrder=_CucsLsbootEmbeddedLocalDiskImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,25,1,4),_CucsLsbootEmbeddedLocalDiskImageOrder_Type())
cucsLsbootEmbeddedLocalDiskImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageOrder.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImageType_Type=CucsLsbootEmbeddedLocalDiskImageType
_CucsLsbootEmbeddedLocalDiskImageType_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImageType=_CucsLsbootEmbeddedLocalDiskImageType_Object((1,3,6,1,4,1,9,9,719,1,27,25,1,5),_CucsLsbootEmbeddedLocalDiskImageType_Type())
cucsLsbootEmbeddedLocalDiskImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImageType.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathTable_Object=MibTable
cucsLsbootEmbeddedLocalDiskImagePathTable=_CucsLsbootEmbeddedLocalDiskImagePathTable_Object((1,3,6,1,4,1,9,9,719,1,27,26))
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathTable.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathEntry_Object=MibTableRow
cucsLsbootEmbeddedLocalDiskImagePathEntry=_CucsLsbootEmbeddedLocalDiskImagePathEntry_Object((1,3,6,1,4,1,9,9,719,1,27,26,1))
cucsLsbootEmbeddedLocalDiskImagePathEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathEntry.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Type=CucsManagedObjectId
_CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathInstanceId=_CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,26,1,1),_CucsLsbootEmbeddedLocalDiskImagePathInstanceId_Type())
cucsLsbootEmbeddedLocalDiskImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathInstanceId.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathDn_Type=CucsManagedObjectDn
_CucsLsbootEmbeddedLocalDiskImagePathDn_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathDn=_CucsLsbootEmbeddedLocalDiskImagePathDn_Object((1,3,6,1,4,1,9,9,719,1,27,26,1,2),_CucsLsbootEmbeddedLocalDiskImagePathDn_Type())
cucsLsbootEmbeddedLocalDiskImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathDn.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathRn_Type=SnmpAdminString
_CucsLsbootEmbeddedLocalDiskImagePathRn_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathRn=_CucsLsbootEmbeddedLocalDiskImagePathRn_Object((1,3,6,1,4,1,9,9,719,1,27,26,1,3),_CucsLsbootEmbeddedLocalDiskImagePathRn_Type())
cucsLsbootEmbeddedLocalDiskImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathRn.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Type=Gauge32
_CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathSlotNumber=_CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Object((1,3,6,1,4,1,9,9,719,1,27,26,1,4),_CucsLsbootEmbeddedLocalDiskImagePathSlotNumber_Type())
cucsLsbootEmbeddedLocalDiskImagePathSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathSlotNumber.setStatus(_A)
_CucsLsbootEmbeddedLocalDiskImagePathType_Type=CucsLsbootEmbeddedLocalDiskImagePathType
_CucsLsbootEmbeddedLocalDiskImagePathType_Object=MibTableColumn
cucsLsbootEmbeddedLocalDiskImagePathType=_CucsLsbootEmbeddedLocalDiskImagePathType_Object((1,3,6,1,4,1,9,9,719,1,27,26,1,5),_CucsLsbootEmbeddedLocalDiskImagePathType_Type())
cucsLsbootEmbeddedLocalDiskImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalDiskImagePathType.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageTable_Object=MibTable
cucsLsbootEmbeddedLocalLunImageTable=_CucsLsbootEmbeddedLocalLunImageTable_Object((1,3,6,1,4,1,9,9,719,1,27,27))
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageTable.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageEntry_Object=MibTableRow
cucsLsbootEmbeddedLocalLunImageEntry=_CucsLsbootEmbeddedLocalLunImageEntry_Object((1,3,6,1,4,1,9,9,719,1,27,27,1))
cucsLsbootEmbeddedLocalLunImageEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageEntry.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageInstanceId_Type=CucsManagedObjectId
_CucsLsbootEmbeddedLocalLunImageInstanceId_Object=MibTableColumn
cucsLsbootEmbeddedLocalLunImageInstanceId=_CucsLsbootEmbeddedLocalLunImageInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,27,1,1),_CucsLsbootEmbeddedLocalLunImageInstanceId_Type())
cucsLsbootEmbeddedLocalLunImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageInstanceId.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageDn_Type=CucsManagedObjectDn
_CucsLsbootEmbeddedLocalLunImageDn_Object=MibTableColumn
cucsLsbootEmbeddedLocalLunImageDn=_CucsLsbootEmbeddedLocalLunImageDn_Object((1,3,6,1,4,1,9,9,719,1,27,27,1,2),_CucsLsbootEmbeddedLocalLunImageDn_Type())
cucsLsbootEmbeddedLocalLunImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageDn.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageRn_Type=SnmpAdminString
_CucsLsbootEmbeddedLocalLunImageRn_Object=MibTableColumn
cucsLsbootEmbeddedLocalLunImageRn=_CucsLsbootEmbeddedLocalLunImageRn_Object((1,3,6,1,4,1,9,9,719,1,27,27,1,3),_CucsLsbootEmbeddedLocalLunImageRn_Type())
cucsLsbootEmbeddedLocalLunImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageRn.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageOrder_Type=Gauge32
_CucsLsbootEmbeddedLocalLunImageOrder_Object=MibTableColumn
cucsLsbootEmbeddedLocalLunImageOrder=_CucsLsbootEmbeddedLocalLunImageOrder_Object((1,3,6,1,4,1,9,9,719,1,27,27,1,4),_CucsLsbootEmbeddedLocalLunImageOrder_Type())
cucsLsbootEmbeddedLocalLunImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageOrder.setStatus(_A)
_CucsLsbootEmbeddedLocalLunImageType_Type=CucsLsbootEmbeddedLocalLunImageType
_CucsLsbootEmbeddedLocalLunImageType_Object=MibTableColumn
cucsLsbootEmbeddedLocalLunImageType=_CucsLsbootEmbeddedLocalLunImageType_Object((1,3,6,1,4,1,9,9,719,1,27,27,1,5),_CucsLsbootEmbeddedLocalLunImageType_Type())
cucsLsbootEmbeddedLocalLunImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEmbeddedLocalLunImageType.setStatus(_A)
_CucsLsbootEFIShellTable_Object=MibTable
cucsLsbootEFIShellTable=_CucsLsbootEFIShellTable_Object((1,3,6,1,4,1,9,9,719,1,27,29))
if mibBuilder.loadTexts:cucsLsbootEFIShellTable.setStatus(_A)
_CucsLsbootEFIShellEntry_Object=MibTableRow
cucsLsbootEFIShellEntry=_CucsLsbootEFIShellEntry_Object((1,3,6,1,4,1,9,9,719,1,27,29,1))
cucsLsbootEFIShellEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:cucsLsbootEFIShellEntry.setStatus(_A)
_CucsLsbootEFIShellInstanceId_Type=CucsManagedObjectId
_CucsLsbootEFIShellInstanceId_Object=MibTableColumn
cucsLsbootEFIShellInstanceId=_CucsLsbootEFIShellInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,29,1,1),_CucsLsbootEFIShellInstanceId_Type())
cucsLsbootEFIShellInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootEFIShellInstanceId.setStatus(_A)
_CucsLsbootEFIShellDn_Type=CucsManagedObjectDn
_CucsLsbootEFIShellDn_Object=MibTableColumn
cucsLsbootEFIShellDn=_CucsLsbootEFIShellDn_Object((1,3,6,1,4,1,9,9,719,1,27,29,1,2),_CucsLsbootEFIShellDn_Type())
cucsLsbootEFIShellDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEFIShellDn.setStatus(_A)
_CucsLsbootEFIShellRn_Type=SnmpAdminString
_CucsLsbootEFIShellRn_Object=MibTableColumn
cucsLsbootEFIShellRn=_CucsLsbootEFIShellRn_Object((1,3,6,1,4,1,9,9,719,1,27,29,1,3),_CucsLsbootEFIShellRn_Type())
cucsLsbootEFIShellRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEFIShellRn.setStatus(_A)
_CucsLsbootEFIShellAccess_Type=CucsLsbootEFIShellAccess
_CucsLsbootEFIShellAccess_Object=MibTableColumn
cucsLsbootEFIShellAccess=_CucsLsbootEFIShellAccess_Object((1,3,6,1,4,1,9,9,719,1,27,29,1,4),_CucsLsbootEFIShellAccess_Type())
cucsLsbootEFIShellAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEFIShellAccess.setStatus(_A)
_CucsLsbootEFIShellOrder_Type=Gauge32
_CucsLsbootEFIShellOrder_Object=MibTableColumn
cucsLsbootEFIShellOrder=_CucsLsbootEFIShellOrder_Object((1,3,6,1,4,1,9,9,719,1,27,29,1,5),_CucsLsbootEFIShellOrder_Type())
cucsLsbootEFIShellOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEFIShellOrder.setStatus(_A)
_CucsLsbootEFIShellType_Type=CucsLsbootEFIShellType
_CucsLsbootEFIShellType_Object=MibTableColumn
cucsLsbootEFIShellType=_CucsLsbootEFIShellType_Object((1,3,6,1,4,1,9,9,719,1,27,29,1,6),_CucsLsbootEFIShellType_Type())
cucsLsbootEFIShellType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootEFIShellType.setStatus(_A)
_CucsLsbootNvmeTable_Object=MibTable
cucsLsbootNvmeTable=_CucsLsbootNvmeTable_Object((1,3,6,1,4,1,9,9,719,1,27,30))
if mibBuilder.loadTexts:cucsLsbootNvmeTable.setStatus(_A)
_CucsLsbootNvmeEntry_Object=MibTableRow
cucsLsbootNvmeEntry=_CucsLsbootNvmeEntry_Object((1,3,6,1,4,1,9,9,719,1,27,30,1))
cucsLsbootNvmeEntry.setIndexNames((0,_C,_g))
if mibBuilder.loadTexts:cucsLsbootNvmeEntry.setStatus(_A)
_CucsLsbootNvmeInstanceId_Type=CucsManagedObjectId
_CucsLsbootNvmeInstanceId_Object=MibTableColumn
cucsLsbootNvmeInstanceId=_CucsLsbootNvmeInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,30,1,1),_CucsLsbootNvmeInstanceId_Type())
cucsLsbootNvmeInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootNvmeInstanceId.setStatus(_A)
_CucsLsbootNvmeDn_Type=CucsManagedObjectDn
_CucsLsbootNvmeDn_Object=MibTableColumn
cucsLsbootNvmeDn=_CucsLsbootNvmeDn_Object((1,3,6,1,4,1,9,9,719,1,27,30,1,2),_CucsLsbootNvmeDn_Type())
cucsLsbootNvmeDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeDn.setStatus(_A)
_CucsLsbootNvmeRn_Type=SnmpAdminString
_CucsLsbootNvmeRn_Object=MibTableColumn
cucsLsbootNvmeRn=_CucsLsbootNvmeRn_Object((1,3,6,1,4,1,9,9,719,1,27,30,1,3),_CucsLsbootNvmeRn_Type())
cucsLsbootNvmeRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeRn.setStatus(_A)
_CucsLsbootNvmeOrder_Type=Gauge32
_CucsLsbootNvmeOrder_Object=MibTableColumn
cucsLsbootNvmeOrder=_CucsLsbootNvmeOrder_Object((1,3,6,1,4,1,9,9,719,1,27,30,1,4),_CucsLsbootNvmeOrder_Type())
cucsLsbootNvmeOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeOrder.setStatus(_A)
_CucsLsbootNvmeType_Type=CucsLsbootNvmeType
_CucsLsbootNvmeType_Object=MibTableColumn
cucsLsbootNvmeType=_CucsLsbootNvmeType_Object((1,3,6,1,4,1,9,9,719,1,27,30,1,5),_CucsLsbootNvmeType_Type())
cucsLsbootNvmeType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeType.setStatus(_A)
_CucsLsbootNvmeDiskSsdTable_Object=MibTable
cucsLsbootNvmeDiskSsdTable=_CucsLsbootNvmeDiskSsdTable_Object((1,3,6,1,4,1,9,9,719,1,27,31))
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdTable.setStatus(_A)
_CucsLsbootNvmeDiskSsdEntry_Object=MibTableRow
cucsLsbootNvmeDiskSsdEntry=_CucsLsbootNvmeDiskSsdEntry_Object((1,3,6,1,4,1,9,9,719,1,27,31,1))
cucsLsbootNvmeDiskSsdEntry.setIndexNames((0,_C,_h))
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdEntry.setStatus(_A)
_CucsLsbootNvmeDiskSsdInstanceId_Type=CucsManagedObjectId
_CucsLsbootNvmeDiskSsdInstanceId_Object=MibTableColumn
cucsLsbootNvmeDiskSsdInstanceId=_CucsLsbootNvmeDiskSsdInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,31,1,1),_CucsLsbootNvmeDiskSsdInstanceId_Type())
cucsLsbootNvmeDiskSsdInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdInstanceId.setStatus(_A)
_CucsLsbootNvmeDiskSsdDn_Type=CucsManagedObjectDn
_CucsLsbootNvmeDiskSsdDn_Object=MibTableColumn
cucsLsbootNvmeDiskSsdDn=_CucsLsbootNvmeDiskSsdDn_Object((1,3,6,1,4,1,9,9,719,1,27,31,1,2),_CucsLsbootNvmeDiskSsdDn_Type())
cucsLsbootNvmeDiskSsdDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdDn.setStatus(_A)
_CucsLsbootNvmeDiskSsdRn_Type=SnmpAdminString
_CucsLsbootNvmeDiskSsdRn_Object=MibTableColumn
cucsLsbootNvmeDiskSsdRn=_CucsLsbootNvmeDiskSsdRn_Object((1,3,6,1,4,1,9,9,719,1,27,31,1,3),_CucsLsbootNvmeDiskSsdRn_Type())
cucsLsbootNvmeDiskSsdRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdRn.setStatus(_A)
_CucsLsbootNvmeDiskSsdOrder_Type=Gauge32
_CucsLsbootNvmeDiskSsdOrder_Object=MibTableColumn
cucsLsbootNvmeDiskSsdOrder=_CucsLsbootNvmeDiskSsdOrder_Object((1,3,6,1,4,1,9,9,719,1,27,31,1,4),_CucsLsbootNvmeDiskSsdOrder_Type())
cucsLsbootNvmeDiskSsdOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdOrder.setStatus(_A)
_CucsLsbootNvmeDiskSsdSlotId_Type=Gauge32
_CucsLsbootNvmeDiskSsdSlotId_Object=MibTableColumn
cucsLsbootNvmeDiskSsdSlotId=_CucsLsbootNvmeDiskSsdSlotId_Object((1,3,6,1,4,1,9,9,719,1,27,31,1,5),_CucsLsbootNvmeDiskSsdSlotId_Type())
cucsLsbootNvmeDiskSsdSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdSlotId.setStatus(_A)
_CucsLsbootNvmeDiskSsdType_Type=CucsLsbootNvmeDiskSsdType
_CucsLsbootNvmeDiskSsdType_Object=MibTableColumn
cucsLsbootNvmeDiskSsdType=_CucsLsbootNvmeDiskSsdType_Object((1,3,6,1,4,1,9,9,719,1,27,31,1,6),_CucsLsbootNvmeDiskSsdType_Type())
cucsLsbootNvmeDiskSsdType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmeDiskSsdType.setStatus(_A)
_CucsLsbootNvmePciSsdTable_Object=MibTable
cucsLsbootNvmePciSsdTable=_CucsLsbootNvmePciSsdTable_Object((1,3,6,1,4,1,9,9,719,1,27,32))
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdTable.setStatus(_A)
_CucsLsbootNvmePciSsdEntry_Object=MibTableRow
cucsLsbootNvmePciSsdEntry=_CucsLsbootNvmePciSsdEntry_Object((1,3,6,1,4,1,9,9,719,1,27,32,1))
cucsLsbootNvmePciSsdEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdEntry.setStatus(_A)
_CucsLsbootNvmePciSsdInstanceId_Type=CucsManagedObjectId
_CucsLsbootNvmePciSsdInstanceId_Object=MibTableColumn
cucsLsbootNvmePciSsdInstanceId=_CucsLsbootNvmePciSsdInstanceId_Object((1,3,6,1,4,1,9,9,719,1,27,32,1,1),_CucsLsbootNvmePciSsdInstanceId_Type())
cucsLsbootNvmePciSsdInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdInstanceId.setStatus(_A)
_CucsLsbootNvmePciSsdDn_Type=CucsManagedObjectDn
_CucsLsbootNvmePciSsdDn_Object=MibTableColumn
cucsLsbootNvmePciSsdDn=_CucsLsbootNvmePciSsdDn_Object((1,3,6,1,4,1,9,9,719,1,27,32,1,2),_CucsLsbootNvmePciSsdDn_Type())
cucsLsbootNvmePciSsdDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdDn.setStatus(_A)
_CucsLsbootNvmePciSsdRn_Type=SnmpAdminString
_CucsLsbootNvmePciSsdRn_Object=MibTableColumn
cucsLsbootNvmePciSsdRn=_CucsLsbootNvmePciSsdRn_Object((1,3,6,1,4,1,9,9,719,1,27,32,1,3),_CucsLsbootNvmePciSsdRn_Type())
cucsLsbootNvmePciSsdRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdRn.setStatus(_A)
_CucsLsbootNvmePciSsdOrder_Type=Gauge32
_CucsLsbootNvmePciSsdOrder_Object=MibTableColumn
cucsLsbootNvmePciSsdOrder=_CucsLsbootNvmePciSsdOrder_Object((1,3,6,1,4,1,9,9,719,1,27,32,1,4),_CucsLsbootNvmePciSsdOrder_Type())
cucsLsbootNvmePciSsdOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdOrder.setStatus(_A)
_CucsLsbootNvmePciSsdSlotId_Type=Gauge32
_CucsLsbootNvmePciSsdSlotId_Object=MibTableColumn
cucsLsbootNvmePciSsdSlotId=_CucsLsbootNvmePciSsdSlotId_Object((1,3,6,1,4,1,9,9,719,1,27,32,1,5),_CucsLsbootNvmePciSsdSlotId_Type())
cucsLsbootNvmePciSsdSlotId.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdSlotId.setStatus(_A)
_CucsLsbootNvmePciSsdType_Type=CucsLsbootNvmePciSsdType
_CucsLsbootNvmePciSsdType_Object=MibTableColumn
cucsLsbootNvmePciSsdType=_CucsLsbootNvmePciSsdType_Object((1,3,6,1,4,1,9,9,719,1,27,32,1,6),_CucsLsbootNvmePciSsdType_Type())
cucsLsbootNvmePciSsdType.setMaxAccess(_B)
if mibBuilder.loadTexts:cucsLsbootNvmePciSsdType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cucsLsbootObjects':cucsLsbootObjects,'cucsLsbootDefTable':cucsLsbootDefTable,'cucsLsbootDefEntry':cucsLsbootDefEntry,_E:cucsLsbootDefInstanceId,'cucsLsbootDefDn':cucsLsbootDefDn,'cucsLsbootDefRn':cucsLsbootDefRn,'cucsLsbootDefDescr':cucsLsbootDefDescr,'cucsLsbootDefEnforceVnicName':cucsLsbootDefEnforceVnicName,'cucsLsbootDefIntId':cucsLsbootDefIntId,'cucsLsbootDefName':cucsLsbootDefName,'cucsLsbootDefPurpose':cucsLsbootDefPurpose,'cucsLsbootDefRebootOnUpdate':cucsLsbootDefRebootOnUpdate,'cucsLsbootDefPolicyLevel':cucsLsbootDefPolicyLevel,'cucsLsbootDefPolicyOwner':cucsLsbootDefPolicyOwner,'cucsLsbootDefAdvBootOrderApplicable':cucsLsbootDefAdvBootOrderApplicable,'cucsLsbootDefBootMode':cucsLsbootDefBootMode,'cucsLsbootLanTable':cucsLsbootLanTable,'cucsLsbootLanEntry':cucsLsbootLanEntry,_F:cucsLsbootLanInstanceId,'cucsLsbootLanDn':cucsLsbootLanDn,'cucsLsbootLanRn':cucsLsbootLanRn,'cucsLsbootLanAccess':cucsLsbootLanAccess,'cucsLsbootLanOrder':cucsLsbootLanOrder,'cucsLsbootLanType':cucsLsbootLanType,'cucsLsbootLanProt':cucsLsbootLanProt,'cucsLsbootLanImagePathTable':cucsLsbootLanImagePathTable,'cucsLsbootLanImagePathEntry':cucsLsbootLanImagePathEntry,_G:cucsLsbootLanImagePathInstanceId,'cucsLsbootLanImagePathDn':cucsLsbootLanImagePathDn,'cucsLsbootLanImagePathRn':cucsLsbootLanImagePathRn,'cucsLsbootLanImagePathType':cucsLsbootLanImagePathType,'cucsLsbootLanImagePathVnicName':cucsLsbootLanImagePathVnicName,'cucsLsbootLanImagePathImgPolicyName':cucsLsbootLanImagePathImgPolicyName,'cucsLsbootLanImagePathImgSecPolicyName':cucsLsbootLanImagePathImgSecPolicyName,'cucsLsbootLanImagePathBootIpPolicyName':cucsLsbootLanImagePathBootIpPolicyName,'cucsLsbootLanImagePathProvSrvPolicyName':cucsLsbootLanImagePathProvSrvPolicyName,'cucsLsbootLanImagePathISCSIVnicName':cucsLsbootLanImagePathISCSIVnicName,'cucsLsbootLocalStorageTable':cucsLsbootLocalStorageTable,'cucsLsbootLocalStorageEntry':cucsLsbootLocalStorageEntry,_H:cucsLsbootLocalStorageInstanceId,'cucsLsbootLocalStorageDn':cucsLsbootLocalStorageDn,'cucsLsbootLocalStorageRn':cucsLsbootLocalStorageRn,'cucsLsbootLocalStoragePropAcl':cucsLsbootLocalStoragePropAcl,'cucsLsbootPolicyTable':cucsLsbootPolicyTable,'cucsLsbootPolicyEntry':cucsLsbootPolicyEntry,_I:cucsLsbootPolicyInstanceId,'cucsLsbootPolicyDn':cucsLsbootPolicyDn,'cucsLsbootPolicyRn':cucsLsbootPolicyRn,'cucsLsbootPolicyDescr':cucsLsbootPolicyDescr,'cucsLsbootPolicyEnforceVnicName':cucsLsbootPolicyEnforceVnicName,'cucsLsbootPolicyIntId':cucsLsbootPolicyIntId,'cucsLsbootPolicyName':cucsLsbootPolicyName,'cucsLsbootPolicyPurpose':cucsLsbootPolicyPurpose,'cucsLsbootPolicyRebootOnUpdate':cucsLsbootPolicyRebootOnUpdate,'cucsLsbootPolicyPolicyLevel':cucsLsbootPolicyPolicyLevel,'cucsLsbootPolicyPolicyOwner':cucsLsbootPolicyPolicyOwner,'cucsLsbootPolicyBootMode':cucsLsbootPolicyBootMode,'cucsLsbootPolicyPropAcl':cucsLsbootPolicyPropAcl,'cucsLsbootSanImageTable':cucsLsbootSanImageTable,'cucsLsbootSanImageEntry':cucsLsbootSanImageEntry,_J:cucsLsbootSanImageInstanceId,'cucsLsbootSanImageDn':cucsLsbootSanImageDn,'cucsLsbootSanImageRn':cucsLsbootSanImageRn,'cucsLsbootSanImageType':cucsLsbootSanImageType,'cucsLsbootSanImageVnicName':cucsLsbootSanImageVnicName,'cucsLsbootSanImagePathTable':cucsLsbootSanImagePathTable,'cucsLsbootSanImagePathEntry':cucsLsbootSanImagePathEntry,_K:cucsLsbootSanImagePathInstanceId,'cucsLsbootSanImagePathDn':cucsLsbootSanImagePathDn,'cucsLsbootSanImagePathRn':cucsLsbootSanImagePathRn,'cucsLsbootSanImagePathLun':cucsLsbootSanImagePathLun,'cucsLsbootSanImagePathType':cucsLsbootSanImagePathType,'cucsLsbootSanImagePathVnicName':cucsLsbootSanImagePathVnicName,'cucsLsbootSanImagePathWwn':cucsLsbootSanImagePathWwn,'cucsLsbootStorageTable':cucsLsbootStorageTable,'cucsLsbootStorageEntry':cucsLsbootStorageEntry,_L:cucsLsbootStorageInstanceId,'cucsLsbootStorageDn':cucsLsbootStorageDn,'cucsLsbootStorageRn':cucsLsbootStorageRn,'cucsLsbootStorageAccess':cucsLsbootStorageAccess,'cucsLsbootStorageOrder':cucsLsbootStorageOrder,'cucsLsbootStorageType':cucsLsbootStorageType,'cucsLsbootStoragePropAcl':cucsLsbootStoragePropAcl,'cucsLsbootVirtualMediaTable':cucsLsbootVirtualMediaTable,'cucsLsbootVirtualMediaEntry':cucsLsbootVirtualMediaEntry,_M:cucsLsbootVirtualMediaInstanceId,'cucsLsbootVirtualMediaDn':cucsLsbootVirtualMediaDn,'cucsLsbootVirtualMediaRn':cucsLsbootVirtualMediaRn,'cucsLsbootVirtualMediaAccess':cucsLsbootVirtualMediaAccess,'cucsLsbootVirtualMediaOrder':cucsLsbootVirtualMediaOrder,'cucsLsbootVirtualMediaType':cucsLsbootVirtualMediaType,'cucsLsbootVirtualMediaLunId':cucsLsbootVirtualMediaLunId,'cucsLsbootVirtualMediaMappingName':cucsLsbootVirtualMediaMappingName,'cucsLsbootVirtualMediaPropAcl':cucsLsbootVirtualMediaPropAcl,'cucsLsbootIScsiTable':cucsLsbootIScsiTable,'cucsLsbootIScsiEntry':cucsLsbootIScsiEntry,_N:cucsLsbootIScsiInstanceId,'cucsLsbootIScsiDn':cucsLsbootIScsiDn,'cucsLsbootIScsiRn':cucsLsbootIScsiRn,'cucsLsbootIScsiAccess':cucsLsbootIScsiAccess,'cucsLsbootIScsiOrder':cucsLsbootIScsiOrder,'cucsLsbootIScsiType':cucsLsbootIScsiType,'cucsLsbootIScsiImagePathTable':cucsLsbootIScsiImagePathTable,'cucsLsbootIScsiImagePathEntry':cucsLsbootIScsiImagePathEntry,_O:cucsLsbootIScsiImagePathInstanceId,'cucsLsbootIScsiImagePathDn':cucsLsbootIScsiImagePathDn,'cucsLsbootIScsiImagePathRn':cucsLsbootIScsiImagePathRn,'cucsLsbootIScsiImagePathISCSIVnicName':cucsLsbootIScsiImagePathISCSIVnicName,'cucsLsbootIScsiImagePathType':cucsLsbootIScsiImagePathType,'cucsLsbootIScsiImagePathVnicName':cucsLsbootIScsiImagePathVnicName,'cucsLsbootBootSecurityTable':cucsLsbootBootSecurityTable,'cucsLsbootBootSecurityEntry':cucsLsbootBootSecurityEntry,_P:cucsLsbootBootSecurityInstanceId,'cucsLsbootBootSecurityDn':cucsLsbootBootSecurityDn,'cucsLsbootBootSecurityRn':cucsLsbootBootSecurityRn,'cucsLsbootBootSecuritySecureBoot':cucsLsbootBootSecuritySecureBoot,'cucsLsbootDefaultLocalImageTable':cucsLsbootDefaultLocalImageTable,'cucsLsbootDefaultLocalImageEntry':cucsLsbootDefaultLocalImageEntry,_Q:cucsLsbootDefaultLocalImageInstanceId,'cucsLsbootDefaultLocalImageDn':cucsLsbootDefaultLocalImageDn,'cucsLsbootDefaultLocalImageRn':cucsLsbootDefaultLocalImageRn,'cucsLsbootDefaultLocalImageOrder':cucsLsbootDefaultLocalImageOrder,'cucsLsbootDefaultLocalImageType':cucsLsbootDefaultLocalImageType,'cucsLsbootDefaultLocalImagePropAcl':cucsLsbootDefaultLocalImagePropAcl,'cucsLsbootLocalHddImageTable':cucsLsbootLocalHddImageTable,'cucsLsbootLocalHddImageEntry':cucsLsbootLocalHddImageEntry,_R:cucsLsbootLocalHddImageInstanceId,'cucsLsbootLocalHddImageDn':cucsLsbootLocalHddImageDn,'cucsLsbootLocalHddImageRn':cucsLsbootLocalHddImageRn,'cucsLsbootLocalHddImageOrder':cucsLsbootLocalHddImageOrder,'cucsLsbootLocalHddImageType':cucsLsbootLocalHddImageType,'cucsLsbootSanTable':cucsLsbootSanTable,'cucsLsbootSanEntry':cucsLsbootSanEntry,_S:cucsLsbootSanInstanceId,'cucsLsbootSanDn':cucsLsbootSanDn,'cucsLsbootSanRn':cucsLsbootSanRn,'cucsLsbootSanAccess':cucsLsbootSanAccess,'cucsLsbootSanOrder':cucsLsbootSanOrder,'cucsLsbootSanType':cucsLsbootSanType,'cucsLsbootSanCatSanImageTable':cucsLsbootSanCatSanImageTable,'cucsLsbootSanCatSanImageEntry':cucsLsbootSanCatSanImageEntry,_T:cucsLsbootSanCatSanImageInstanceId,'cucsLsbootSanCatSanImageDn':cucsLsbootSanCatSanImageDn,'cucsLsbootSanCatSanImageRn':cucsLsbootSanCatSanImageRn,'cucsLsbootSanCatSanImageType':cucsLsbootSanCatSanImageType,'cucsLsbootSanCatSanImageVnicName':cucsLsbootSanCatSanImageVnicName,'cucsLsbootSanCatSanImagePathTable':cucsLsbootSanCatSanImagePathTable,'cucsLsbootSanCatSanImagePathEntry':cucsLsbootSanCatSanImagePathEntry,_U:cucsLsbootSanCatSanImagePathInstanceId,'cucsLsbootSanCatSanImagePathDn':cucsLsbootSanCatSanImagePathDn,'cucsLsbootSanCatSanImagePathRn':cucsLsbootSanCatSanImagePathRn,'cucsLsbootSanCatSanImagePathLun':cucsLsbootSanCatSanImagePathLun,'cucsLsbootSanCatSanImagePathType':cucsLsbootSanCatSanImagePathType,'cucsLsbootSanCatSanImagePathVnicName':cucsLsbootSanCatSanImagePathVnicName,'cucsLsbootSanCatSanImagePathWwn':cucsLsbootSanCatSanImagePathWwn,'cucsLsbootUsbExternalImageTable':cucsLsbootUsbExternalImageTable,'cucsLsbootUsbExternalImageEntry':cucsLsbootUsbExternalImageEntry,_V:cucsLsbootUsbExternalImageInstanceId,'cucsLsbootUsbExternalImageDn':cucsLsbootUsbExternalImageDn,'cucsLsbootUsbExternalImageRn':cucsLsbootUsbExternalImageRn,'cucsLsbootUsbExternalImageOrder':cucsLsbootUsbExternalImageOrder,'cucsLsbootUsbExternalImageType':cucsLsbootUsbExternalImageType,'cucsLsbootUsbFlashStorageImageTable':cucsLsbootUsbFlashStorageImageTable,'cucsLsbootUsbFlashStorageImageEntry':cucsLsbootUsbFlashStorageImageEntry,_W:cucsLsbootUsbFlashStorageImageInstanceId,'cucsLsbootUsbFlashStorageImageDn':cucsLsbootUsbFlashStorageImageDn,'cucsLsbootUsbFlashStorageImageRn':cucsLsbootUsbFlashStorageImageRn,'cucsLsbootUsbFlashStorageImageOrder':cucsLsbootUsbFlashStorageImageOrder,'cucsLsbootUsbFlashStorageImageType':cucsLsbootUsbFlashStorageImageType,'cucsLsbootUsbInternalImageTable':cucsLsbootUsbInternalImageTable,'cucsLsbootUsbInternalImageEntry':cucsLsbootUsbInternalImageEntry,_X:cucsLsbootUsbInternalImageInstanceId,'cucsLsbootUsbInternalImageDn':cucsLsbootUsbInternalImageDn,'cucsLsbootUsbInternalImageRn':cucsLsbootUsbInternalImageRn,'cucsLsbootUsbInternalImageOrder':cucsLsbootUsbInternalImageOrder,'cucsLsbootUsbInternalImageType':cucsLsbootUsbInternalImageType,'cucsLsbootLocalDiskImageTable':cucsLsbootLocalDiskImageTable,'cucsLsbootLocalDiskImageEntry':cucsLsbootLocalDiskImageEntry,_Y:cucsLsbootLocalDiskImageInstanceId,'cucsLsbootLocalDiskImageDn':cucsLsbootLocalDiskImageDn,'cucsLsbootLocalDiskImageRn':cucsLsbootLocalDiskImageRn,'cucsLsbootLocalDiskImageOrder':cucsLsbootLocalDiskImageOrder,'cucsLsbootLocalDiskImageType':cucsLsbootLocalDiskImageType,'cucsLsbootLocalDiskImagePathTable':cucsLsbootLocalDiskImagePathTable,'cucsLsbootLocalDiskImagePathEntry':cucsLsbootLocalDiskImagePathEntry,_Z:cucsLsbootLocalDiskImagePathInstanceId,'cucsLsbootLocalDiskImagePathDn':cucsLsbootLocalDiskImagePathDn,'cucsLsbootLocalDiskImagePathRn':cucsLsbootLocalDiskImagePathRn,'cucsLsbootLocalDiskImagePathSlotNumber':cucsLsbootLocalDiskImagePathSlotNumber,'cucsLsbootLocalDiskImagePathType':cucsLsbootLocalDiskImagePathType,'cucsLsbootLocalLunImagePathTable':cucsLsbootLocalLunImagePathTable,'cucsLsbootLocalLunImagePathEntry':cucsLsbootLocalLunImagePathEntry,_a:cucsLsbootLocalLunImagePathInstanceId,'cucsLsbootLocalLunImagePathDn':cucsLsbootLocalLunImagePathDn,'cucsLsbootLocalLunImagePathRn':cucsLsbootLocalLunImagePathRn,'cucsLsbootLocalLunImagePathLunName':cucsLsbootLocalLunImagePathLunName,'cucsLsbootLocalLunImagePathType':cucsLsbootLocalLunImagePathType,'cucsLsbootUEFIBootParamTable':cucsLsbootUEFIBootParamTable,'cucsLsbootUEFIBootParamEntry':cucsLsbootUEFIBootParamEntry,_b:cucsLsbootUEFIBootParamInstanceId,'cucsLsbootUEFIBootParamDn':cucsLsbootUEFIBootParamDn,'cucsLsbootUEFIBootParamRn':cucsLsbootUEFIBootParamRn,'cucsLsbootUEFIBootParamBootDescription':cucsLsbootUEFIBootParamBootDescription,'cucsLsbootUEFIBootParamBootLoaderName':cucsLsbootUEFIBootParamBootLoaderName,'cucsLsbootUEFIBootParamBootLoaderPath':cucsLsbootUEFIBootParamBootLoaderPath,'cucsLsbootEmbeddedLocalDiskImageTable':cucsLsbootEmbeddedLocalDiskImageTable,'cucsLsbootEmbeddedLocalDiskImageEntry':cucsLsbootEmbeddedLocalDiskImageEntry,_c:cucsLsbootEmbeddedLocalDiskImageInstanceId,'cucsLsbootEmbeddedLocalDiskImageDn':cucsLsbootEmbeddedLocalDiskImageDn,'cucsLsbootEmbeddedLocalDiskImageRn':cucsLsbootEmbeddedLocalDiskImageRn,'cucsLsbootEmbeddedLocalDiskImageOrder':cucsLsbootEmbeddedLocalDiskImageOrder,'cucsLsbootEmbeddedLocalDiskImageType':cucsLsbootEmbeddedLocalDiskImageType,'cucsLsbootEmbeddedLocalDiskImagePathTable':cucsLsbootEmbeddedLocalDiskImagePathTable,'cucsLsbootEmbeddedLocalDiskImagePathEntry':cucsLsbootEmbeddedLocalDiskImagePathEntry,_d:cucsLsbootEmbeddedLocalDiskImagePathInstanceId,'cucsLsbootEmbeddedLocalDiskImagePathDn':cucsLsbootEmbeddedLocalDiskImagePathDn,'cucsLsbootEmbeddedLocalDiskImagePathRn':cucsLsbootEmbeddedLocalDiskImagePathRn,'cucsLsbootEmbeddedLocalDiskImagePathSlotNumber':cucsLsbootEmbeddedLocalDiskImagePathSlotNumber,'cucsLsbootEmbeddedLocalDiskImagePathType':cucsLsbootEmbeddedLocalDiskImagePathType,'cucsLsbootEmbeddedLocalLunImageTable':cucsLsbootEmbeddedLocalLunImageTable,'cucsLsbootEmbeddedLocalLunImageEntry':cucsLsbootEmbeddedLocalLunImageEntry,_e:cucsLsbootEmbeddedLocalLunImageInstanceId,'cucsLsbootEmbeddedLocalLunImageDn':cucsLsbootEmbeddedLocalLunImageDn,'cucsLsbootEmbeddedLocalLunImageRn':cucsLsbootEmbeddedLocalLunImageRn,'cucsLsbootEmbeddedLocalLunImageOrder':cucsLsbootEmbeddedLocalLunImageOrder,'cucsLsbootEmbeddedLocalLunImageType':cucsLsbootEmbeddedLocalLunImageType,'cucsLsbootEFIShellTable':cucsLsbootEFIShellTable,'cucsLsbootEFIShellEntry':cucsLsbootEFIShellEntry,_f:cucsLsbootEFIShellInstanceId,'cucsLsbootEFIShellDn':cucsLsbootEFIShellDn,'cucsLsbootEFIShellRn':cucsLsbootEFIShellRn,'cucsLsbootEFIShellAccess':cucsLsbootEFIShellAccess,'cucsLsbootEFIShellOrder':cucsLsbootEFIShellOrder,'cucsLsbootEFIShellType':cucsLsbootEFIShellType,'cucsLsbootNvmeTable':cucsLsbootNvmeTable,'cucsLsbootNvmeEntry':cucsLsbootNvmeEntry,_g:cucsLsbootNvmeInstanceId,'cucsLsbootNvmeDn':cucsLsbootNvmeDn,'cucsLsbootNvmeRn':cucsLsbootNvmeRn,'cucsLsbootNvmeOrder':cucsLsbootNvmeOrder,'cucsLsbootNvmeType':cucsLsbootNvmeType,'cucsLsbootNvmeDiskSsdTable':cucsLsbootNvmeDiskSsdTable,'cucsLsbootNvmeDiskSsdEntry':cucsLsbootNvmeDiskSsdEntry,_h:cucsLsbootNvmeDiskSsdInstanceId,'cucsLsbootNvmeDiskSsdDn':cucsLsbootNvmeDiskSsdDn,'cucsLsbootNvmeDiskSsdRn':cucsLsbootNvmeDiskSsdRn,'cucsLsbootNvmeDiskSsdOrder':cucsLsbootNvmeDiskSsdOrder,'cucsLsbootNvmeDiskSsdSlotId':cucsLsbootNvmeDiskSsdSlotId,'cucsLsbootNvmeDiskSsdType':cucsLsbootNvmeDiskSsdType,'cucsLsbootNvmePciSsdTable':cucsLsbootNvmePciSsdTable,'cucsLsbootNvmePciSsdEntry':cucsLsbootNvmePciSsdEntry,_i:cucsLsbootNvmePciSsdInstanceId,'cucsLsbootNvmePciSsdDn':cucsLsbootNvmePciSsdDn,'cucsLsbootNvmePciSsdRn':cucsLsbootNvmePciSsdRn,'cucsLsbootNvmePciSsdOrder':cucsLsbootNvmePciSsdOrder,'cucsLsbootNvmePciSsdSlotId':cucsLsbootNvmePciSsdSlotId,'cucsLsbootNvmePciSsdType':cucsLsbootNvmePciSsdType})