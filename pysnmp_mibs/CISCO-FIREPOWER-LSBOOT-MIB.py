_X='cfprLsbootVirtualMediaInstanceId'
_W='cfprLsbootUsbInternalImageInstanceId'
_V='cfprLsbootUsbFlashStorageImageInstanceId'
_U='cfprLsbootUsbExternalImageInstanceId'
_T='cfprLsbootStorageInstanceId'
_S='cfprLsbootSanImagePathInstanceId'
_R='cfprLsbootSanImageInstanceId'
_Q='cfprLsbootSanCatSanImagePathInstanceId'
_P='cfprLsbootSanCatSanImageInstanceId'
_O='cfprLsbootSanInstanceId'
_N='cfprLsbootPolicyInstanceId'
_M='cfprLsbootLocalStorageInstanceId'
_L='cfprLsbootLocalHddImageInstanceId'
_K='cfprLsbootLanImagePathInstanceId'
_J='cfprLsbootLanInstanceId'
_I='cfprLsbootIScsiImagePathInstanceId'
_H='cfprLsbootIScsiInstanceId'
_G='cfprLsbootDefaultLocalImageInstanceId'
_F='cfprLsbootDefInstanceId'
_E='cfprLsbootBootSecurityInstanceId'
_D='not-accessible'
_C='CISCO-FIREPOWER-LSBOOT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CfprManagedObjectDn,CfprManagedObjectId,ciscoFirepowerMIBObjects=mibBuilder.importSymbols('CISCO-FIREPOWER-MIB','CfprManagedObjectDn','CfprManagedObjectId','ciscoFirepowerMIBObjects')
CfprLsbootADefBootMode,CfprLsbootAccessType,CfprLsbootDefaultLocalImageType,CfprLsbootIScsiAccess,CfprLsbootIScsiImagePathType,CfprLsbootIScsiType,CfprLsbootLanAccess,CfprLsbootLanBootProt,CfprLsbootLanImagePathType,CfprLsbootLanType,CfprLsbootLocalHddImageType,CfprLsbootPurpose,CfprLsbootSanAccess,CfprLsbootSanCatSanImagePathType,CfprLsbootSanCatSanImageType,CfprLsbootSanImagePathType,CfprLsbootSanImageType,CfprLsbootSanType,CfprLsbootStorageAccess,CfprLsbootStorageType,CfprLsbootUsbExternalImageType,CfprLsbootUsbFlashStorageImageType,CfprLsbootUsbInternalImageType,CfprLsbootVirtualMediaType,CfprPolicyPolicyOwner=mibBuilder.importSymbols('CISCO-FIREPOWER-TC-MIB','CfprLsbootADefBootMode','CfprLsbootAccessType','CfprLsbootDefaultLocalImageType','CfprLsbootIScsiAccess','CfprLsbootIScsiImagePathType','CfprLsbootIScsiType','CfprLsbootLanAccess','CfprLsbootLanBootProt','CfprLsbootLanImagePathType','CfprLsbootLanType','CfprLsbootLocalHddImageType','CfprLsbootPurpose','CfprLsbootSanAccess','CfprLsbootSanCatSanImagePathType','CfprLsbootSanCatSanImageType','CfprLsbootSanImagePathType','CfprLsbootSanImageType','CfprLsbootSanType','CfprLsbootStorageAccess','CfprLsbootStorageType','CfprLsbootUsbExternalImageType','CfprLsbootUsbFlashStorageImageType','CfprLsbootUsbInternalImageType','CfprLsbootVirtualMediaType','CfprPolicyPolicyOwner')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CiscoAlarmSeverity,CiscoInetAddressMask,CiscoNetworkAddress,TimeIntervalSec,Unsigned64=mibBuilder.importSymbols('CISCO-TC','CiscoAlarmSeverity','CiscoInetAddressMask','CiscoNetworkAddress','TimeIntervalSec','Unsigned64')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowPointer,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowPointer','TextualConvention','TimeInterval','TimeStamp','TruthValue')
cfprLsbootObjects=ModuleIdentity((1,3,6,1,4,1,9,9,826,1,47))
_CfprLsbootBootSecurityTable_Object=MibTable
cfprLsbootBootSecurityTable=_CfprLsbootBootSecurityTable_Object((1,3,6,1,4,1,9,9,826,1,47,1))
if mibBuilder.loadTexts:cfprLsbootBootSecurityTable.setStatus(_A)
_CfprLsbootBootSecurityEntry_Object=MibTableRow
cfprLsbootBootSecurityEntry=_CfprLsbootBootSecurityEntry_Object((1,3,6,1,4,1,9,9,826,1,47,1,1))
cfprLsbootBootSecurityEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:cfprLsbootBootSecurityEntry.setStatus(_A)
_CfprLsbootBootSecurityInstanceId_Type=CfprManagedObjectId
_CfprLsbootBootSecurityInstanceId_Object=MibTableColumn
cfprLsbootBootSecurityInstanceId=_CfprLsbootBootSecurityInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,1,1,1),_CfprLsbootBootSecurityInstanceId_Type())
cfprLsbootBootSecurityInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootBootSecurityInstanceId.setStatus(_A)
_CfprLsbootBootSecurityDn_Type=CfprManagedObjectDn
_CfprLsbootBootSecurityDn_Object=MibTableColumn
cfprLsbootBootSecurityDn=_CfprLsbootBootSecurityDn_Object((1,3,6,1,4,1,9,9,826,1,47,1,1,2),_CfprLsbootBootSecurityDn_Type())
cfprLsbootBootSecurityDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootBootSecurityDn.setStatus(_A)
_CfprLsbootBootSecurityRn_Type=SnmpAdminString
_CfprLsbootBootSecurityRn_Object=MibTableColumn
cfprLsbootBootSecurityRn=_CfprLsbootBootSecurityRn_Object((1,3,6,1,4,1,9,9,826,1,47,1,1,3),_CfprLsbootBootSecurityRn_Type())
cfprLsbootBootSecurityRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootBootSecurityRn.setStatus(_A)
_CfprLsbootBootSecuritySecureBoot_Type=TruthValue
_CfprLsbootBootSecuritySecureBoot_Object=MibTableColumn
cfprLsbootBootSecuritySecureBoot=_CfprLsbootBootSecuritySecureBoot_Object((1,3,6,1,4,1,9,9,826,1,47,1,1,4),_CfprLsbootBootSecuritySecureBoot_Type())
cfprLsbootBootSecuritySecureBoot.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootBootSecuritySecureBoot.setStatus(_A)
_CfprLsbootDefTable_Object=MibTable
cfprLsbootDefTable=_CfprLsbootDefTable_Object((1,3,6,1,4,1,9,9,826,1,47,2))
if mibBuilder.loadTexts:cfprLsbootDefTable.setStatus(_A)
_CfprLsbootDefEntry_Object=MibTableRow
cfprLsbootDefEntry=_CfprLsbootDefEntry_Object((1,3,6,1,4,1,9,9,826,1,47,2,1))
cfprLsbootDefEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:cfprLsbootDefEntry.setStatus(_A)
_CfprLsbootDefInstanceId_Type=CfprManagedObjectId
_CfprLsbootDefInstanceId_Object=MibTableColumn
cfprLsbootDefInstanceId=_CfprLsbootDefInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,1),_CfprLsbootDefInstanceId_Type())
cfprLsbootDefInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootDefInstanceId.setStatus(_A)
_CfprLsbootDefDn_Type=CfprManagedObjectDn
_CfprLsbootDefDn_Object=MibTableColumn
cfprLsbootDefDn=_CfprLsbootDefDn_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,2),_CfprLsbootDefDn_Type())
cfprLsbootDefDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefDn.setStatus(_A)
_CfprLsbootDefRn_Type=SnmpAdminString
_CfprLsbootDefRn_Object=MibTableColumn
cfprLsbootDefRn=_CfprLsbootDefRn_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,3),_CfprLsbootDefRn_Type())
cfprLsbootDefRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefRn.setStatus(_A)
_CfprLsbootDefAdvBootOrderApplicable_Type=TruthValue
_CfprLsbootDefAdvBootOrderApplicable_Object=MibTableColumn
cfprLsbootDefAdvBootOrderApplicable=_CfprLsbootDefAdvBootOrderApplicable_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,4),_CfprLsbootDefAdvBootOrderApplicable_Type())
cfprLsbootDefAdvBootOrderApplicable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefAdvBootOrderApplicable.setStatus(_A)
_CfprLsbootDefBootMode_Type=CfprLsbootADefBootMode
_CfprLsbootDefBootMode_Object=MibTableColumn
cfprLsbootDefBootMode=_CfprLsbootDefBootMode_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,5),_CfprLsbootDefBootMode_Type())
cfprLsbootDefBootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefBootMode.setStatus(_A)
_CfprLsbootDefDescr_Type=SnmpAdminString
_CfprLsbootDefDescr_Object=MibTableColumn
cfprLsbootDefDescr=_CfprLsbootDefDescr_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,6),_CfprLsbootDefDescr_Type())
cfprLsbootDefDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefDescr.setStatus(_A)
_CfprLsbootDefEnforceVnicName_Type=TruthValue
_CfprLsbootDefEnforceVnicName_Object=MibTableColumn
cfprLsbootDefEnforceVnicName=_CfprLsbootDefEnforceVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,7),_CfprLsbootDefEnforceVnicName_Type())
cfprLsbootDefEnforceVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefEnforceVnicName.setStatus(_A)
_CfprLsbootDefIntId_Type=SnmpAdminString
_CfprLsbootDefIntId_Object=MibTableColumn
cfprLsbootDefIntId=_CfprLsbootDefIntId_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,8),_CfprLsbootDefIntId_Type())
cfprLsbootDefIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefIntId.setStatus(_A)
_CfprLsbootDefName_Type=SnmpAdminString
_CfprLsbootDefName_Object=MibTableColumn
cfprLsbootDefName=_CfprLsbootDefName_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,9),_CfprLsbootDefName_Type())
cfprLsbootDefName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefName.setStatus(_A)
_CfprLsbootDefPolicyLevel_Type=Gauge32
_CfprLsbootDefPolicyLevel_Object=MibTableColumn
cfprLsbootDefPolicyLevel=_CfprLsbootDefPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,10),_CfprLsbootDefPolicyLevel_Type())
cfprLsbootDefPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefPolicyLevel.setStatus(_A)
_CfprLsbootDefPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprLsbootDefPolicyOwner_Object=MibTableColumn
cfprLsbootDefPolicyOwner=_CfprLsbootDefPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,11),_CfprLsbootDefPolicyOwner_Type())
cfprLsbootDefPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefPolicyOwner.setStatus(_A)
_CfprLsbootDefPurpose_Type=CfprLsbootPurpose
_CfprLsbootDefPurpose_Object=MibTableColumn
cfprLsbootDefPurpose=_CfprLsbootDefPurpose_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,12),_CfprLsbootDefPurpose_Type())
cfprLsbootDefPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefPurpose.setStatus(_A)
_CfprLsbootDefRebootOnUpdate_Type=TruthValue
_CfprLsbootDefRebootOnUpdate_Object=MibTableColumn
cfprLsbootDefRebootOnUpdate=_CfprLsbootDefRebootOnUpdate_Object((1,3,6,1,4,1,9,9,826,1,47,2,1,13),_CfprLsbootDefRebootOnUpdate_Type())
cfprLsbootDefRebootOnUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefRebootOnUpdate.setStatus(_A)
_CfprLsbootDefaultLocalImageTable_Object=MibTable
cfprLsbootDefaultLocalImageTable=_CfprLsbootDefaultLocalImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,3))
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageTable.setStatus(_A)
_CfprLsbootDefaultLocalImageEntry_Object=MibTableRow
cfprLsbootDefaultLocalImageEntry=_CfprLsbootDefaultLocalImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,3,1))
cfprLsbootDefaultLocalImageEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageEntry.setStatus(_A)
_CfprLsbootDefaultLocalImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootDefaultLocalImageInstanceId_Object=MibTableColumn
cfprLsbootDefaultLocalImageInstanceId=_CfprLsbootDefaultLocalImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,3,1,1),_CfprLsbootDefaultLocalImageInstanceId_Type())
cfprLsbootDefaultLocalImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageInstanceId.setStatus(_A)
_CfprLsbootDefaultLocalImageDn_Type=CfprManagedObjectDn
_CfprLsbootDefaultLocalImageDn_Object=MibTableColumn
cfprLsbootDefaultLocalImageDn=_CfprLsbootDefaultLocalImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,3,1,2),_CfprLsbootDefaultLocalImageDn_Type())
cfprLsbootDefaultLocalImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageDn.setStatus(_A)
_CfprLsbootDefaultLocalImageRn_Type=SnmpAdminString
_CfprLsbootDefaultLocalImageRn_Object=MibTableColumn
cfprLsbootDefaultLocalImageRn=_CfprLsbootDefaultLocalImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,3,1,3),_CfprLsbootDefaultLocalImageRn_Type())
cfprLsbootDefaultLocalImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageRn.setStatus(_A)
_CfprLsbootDefaultLocalImageOrder_Type=Gauge32
_CfprLsbootDefaultLocalImageOrder_Object=MibTableColumn
cfprLsbootDefaultLocalImageOrder=_CfprLsbootDefaultLocalImageOrder_Object((1,3,6,1,4,1,9,9,826,1,47,3,1,4),_CfprLsbootDefaultLocalImageOrder_Type())
cfprLsbootDefaultLocalImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageOrder.setStatus(_A)
_CfprLsbootDefaultLocalImageType_Type=CfprLsbootDefaultLocalImageType
_CfprLsbootDefaultLocalImageType_Object=MibTableColumn
cfprLsbootDefaultLocalImageType=_CfprLsbootDefaultLocalImageType_Object((1,3,6,1,4,1,9,9,826,1,47,3,1,5),_CfprLsbootDefaultLocalImageType_Type())
cfprLsbootDefaultLocalImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootDefaultLocalImageType.setStatus(_A)
_CfprLsbootIScsiTable_Object=MibTable
cfprLsbootIScsiTable=_CfprLsbootIScsiTable_Object((1,3,6,1,4,1,9,9,826,1,47,4))
if mibBuilder.loadTexts:cfprLsbootIScsiTable.setStatus(_A)
_CfprLsbootIScsiEntry_Object=MibTableRow
cfprLsbootIScsiEntry=_CfprLsbootIScsiEntry_Object((1,3,6,1,4,1,9,9,826,1,47,4,1))
cfprLsbootIScsiEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:cfprLsbootIScsiEntry.setStatus(_A)
_CfprLsbootIScsiInstanceId_Type=CfprManagedObjectId
_CfprLsbootIScsiInstanceId_Object=MibTableColumn
cfprLsbootIScsiInstanceId=_CfprLsbootIScsiInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,4,1,1),_CfprLsbootIScsiInstanceId_Type())
cfprLsbootIScsiInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootIScsiInstanceId.setStatus(_A)
_CfprLsbootIScsiDn_Type=CfprManagedObjectDn
_CfprLsbootIScsiDn_Object=MibTableColumn
cfprLsbootIScsiDn=_CfprLsbootIScsiDn_Object((1,3,6,1,4,1,9,9,826,1,47,4,1,2),_CfprLsbootIScsiDn_Type())
cfprLsbootIScsiDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiDn.setStatus(_A)
_CfprLsbootIScsiRn_Type=SnmpAdminString
_CfprLsbootIScsiRn_Object=MibTableColumn
cfprLsbootIScsiRn=_CfprLsbootIScsiRn_Object((1,3,6,1,4,1,9,9,826,1,47,4,1,3),_CfprLsbootIScsiRn_Type())
cfprLsbootIScsiRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiRn.setStatus(_A)
_CfprLsbootIScsiAccess_Type=CfprLsbootIScsiAccess
_CfprLsbootIScsiAccess_Object=MibTableColumn
cfprLsbootIScsiAccess=_CfprLsbootIScsiAccess_Object((1,3,6,1,4,1,9,9,826,1,47,4,1,4),_CfprLsbootIScsiAccess_Type())
cfprLsbootIScsiAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiAccess.setStatus(_A)
_CfprLsbootIScsiOrder_Type=Gauge32
_CfprLsbootIScsiOrder_Object=MibTableColumn
cfprLsbootIScsiOrder=_CfprLsbootIScsiOrder_Object((1,3,6,1,4,1,9,9,826,1,47,4,1,5),_CfprLsbootIScsiOrder_Type())
cfprLsbootIScsiOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiOrder.setStatus(_A)
_CfprLsbootIScsiType_Type=CfprLsbootIScsiType
_CfprLsbootIScsiType_Object=MibTableColumn
cfprLsbootIScsiType=_CfprLsbootIScsiType_Object((1,3,6,1,4,1,9,9,826,1,47,4,1,6),_CfprLsbootIScsiType_Type())
cfprLsbootIScsiType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiType.setStatus(_A)
_CfprLsbootIScsiImagePathTable_Object=MibTable
cfprLsbootIScsiImagePathTable=_CfprLsbootIScsiImagePathTable_Object((1,3,6,1,4,1,9,9,826,1,47,5))
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathTable.setStatus(_A)
_CfprLsbootIScsiImagePathEntry_Object=MibTableRow
cfprLsbootIScsiImagePathEntry=_CfprLsbootIScsiImagePathEntry_Object((1,3,6,1,4,1,9,9,826,1,47,5,1))
cfprLsbootIScsiImagePathEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathEntry.setStatus(_A)
_CfprLsbootIScsiImagePathInstanceId_Type=CfprManagedObjectId
_CfprLsbootIScsiImagePathInstanceId_Object=MibTableColumn
cfprLsbootIScsiImagePathInstanceId=_CfprLsbootIScsiImagePathInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,5,1,1),_CfprLsbootIScsiImagePathInstanceId_Type())
cfprLsbootIScsiImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathInstanceId.setStatus(_A)
_CfprLsbootIScsiImagePathDn_Type=CfprManagedObjectDn
_CfprLsbootIScsiImagePathDn_Object=MibTableColumn
cfprLsbootIScsiImagePathDn=_CfprLsbootIScsiImagePathDn_Object((1,3,6,1,4,1,9,9,826,1,47,5,1,2),_CfprLsbootIScsiImagePathDn_Type())
cfprLsbootIScsiImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathDn.setStatus(_A)
_CfprLsbootIScsiImagePathRn_Type=SnmpAdminString
_CfprLsbootIScsiImagePathRn_Object=MibTableColumn
cfprLsbootIScsiImagePathRn=_CfprLsbootIScsiImagePathRn_Object((1,3,6,1,4,1,9,9,826,1,47,5,1,3),_CfprLsbootIScsiImagePathRn_Type())
cfprLsbootIScsiImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathRn.setStatus(_A)
_CfprLsbootIScsiImagePathISCSIVnicName_Type=SnmpAdminString
_CfprLsbootIScsiImagePathISCSIVnicName_Object=MibTableColumn
cfprLsbootIScsiImagePathISCSIVnicName=_CfprLsbootIScsiImagePathISCSIVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,5,1,4),_CfprLsbootIScsiImagePathISCSIVnicName_Type())
cfprLsbootIScsiImagePathISCSIVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathISCSIVnicName.setStatus(_A)
_CfprLsbootIScsiImagePathType_Type=CfprLsbootIScsiImagePathType
_CfprLsbootIScsiImagePathType_Object=MibTableColumn
cfprLsbootIScsiImagePathType=_CfprLsbootIScsiImagePathType_Object((1,3,6,1,4,1,9,9,826,1,47,5,1,5),_CfprLsbootIScsiImagePathType_Type())
cfprLsbootIScsiImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathType.setStatus(_A)
_CfprLsbootIScsiImagePathVnicName_Type=SnmpAdminString
_CfprLsbootIScsiImagePathVnicName_Object=MibTableColumn
cfprLsbootIScsiImagePathVnicName=_CfprLsbootIScsiImagePathVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,5,1,6),_CfprLsbootIScsiImagePathVnicName_Type())
cfprLsbootIScsiImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootIScsiImagePathVnicName.setStatus(_A)
_CfprLsbootLanTable_Object=MibTable
cfprLsbootLanTable=_CfprLsbootLanTable_Object((1,3,6,1,4,1,9,9,826,1,47,6))
if mibBuilder.loadTexts:cfprLsbootLanTable.setStatus(_A)
_CfprLsbootLanEntry_Object=MibTableRow
cfprLsbootLanEntry=_CfprLsbootLanEntry_Object((1,3,6,1,4,1,9,9,826,1,47,6,1))
cfprLsbootLanEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:cfprLsbootLanEntry.setStatus(_A)
_CfprLsbootLanInstanceId_Type=CfprManagedObjectId
_CfprLsbootLanInstanceId_Object=MibTableColumn
cfprLsbootLanInstanceId=_CfprLsbootLanInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,1),_CfprLsbootLanInstanceId_Type())
cfprLsbootLanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootLanInstanceId.setStatus(_A)
_CfprLsbootLanDn_Type=CfprManagedObjectDn
_CfprLsbootLanDn_Object=MibTableColumn
cfprLsbootLanDn=_CfprLsbootLanDn_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,2),_CfprLsbootLanDn_Type())
cfprLsbootLanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanDn.setStatus(_A)
_CfprLsbootLanRn_Type=SnmpAdminString
_CfprLsbootLanRn_Object=MibTableColumn
cfprLsbootLanRn=_CfprLsbootLanRn_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,3),_CfprLsbootLanRn_Type())
cfprLsbootLanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanRn.setStatus(_A)
_CfprLsbootLanAccess_Type=CfprLsbootLanAccess
_CfprLsbootLanAccess_Object=MibTableColumn
cfprLsbootLanAccess=_CfprLsbootLanAccess_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,4),_CfprLsbootLanAccess_Type())
cfprLsbootLanAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanAccess.setStatus(_A)
_CfprLsbootLanOrder_Type=Gauge32
_CfprLsbootLanOrder_Object=MibTableColumn
cfprLsbootLanOrder=_CfprLsbootLanOrder_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,5),_CfprLsbootLanOrder_Type())
cfprLsbootLanOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanOrder.setStatus(_A)
_CfprLsbootLanProt_Type=CfprLsbootLanBootProt
_CfprLsbootLanProt_Object=MibTableColumn
cfprLsbootLanProt=_CfprLsbootLanProt_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,6),_CfprLsbootLanProt_Type())
cfprLsbootLanProt.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanProt.setStatus(_A)
_CfprLsbootLanType_Type=CfprLsbootLanType
_CfprLsbootLanType_Object=MibTableColumn
cfprLsbootLanType=_CfprLsbootLanType_Object((1,3,6,1,4,1,9,9,826,1,47,6,1,7),_CfprLsbootLanType_Type())
cfprLsbootLanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanType.setStatus(_A)
_CfprLsbootLanImagePathTable_Object=MibTable
cfprLsbootLanImagePathTable=_CfprLsbootLanImagePathTable_Object((1,3,6,1,4,1,9,9,826,1,47,7))
if mibBuilder.loadTexts:cfprLsbootLanImagePathTable.setStatus(_A)
_CfprLsbootLanImagePathEntry_Object=MibTableRow
cfprLsbootLanImagePathEntry=_CfprLsbootLanImagePathEntry_Object((1,3,6,1,4,1,9,9,826,1,47,7,1))
cfprLsbootLanImagePathEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:cfprLsbootLanImagePathEntry.setStatus(_A)
_CfprLsbootLanImagePathInstanceId_Type=CfprManagedObjectId
_CfprLsbootLanImagePathInstanceId_Object=MibTableColumn
cfprLsbootLanImagePathInstanceId=_CfprLsbootLanImagePathInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,1),_CfprLsbootLanImagePathInstanceId_Type())
cfprLsbootLanImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootLanImagePathInstanceId.setStatus(_A)
_CfprLsbootLanImagePathDn_Type=CfprManagedObjectDn
_CfprLsbootLanImagePathDn_Object=MibTableColumn
cfprLsbootLanImagePathDn=_CfprLsbootLanImagePathDn_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,2),_CfprLsbootLanImagePathDn_Type())
cfprLsbootLanImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathDn.setStatus(_A)
_CfprLsbootLanImagePathRn_Type=SnmpAdminString
_CfprLsbootLanImagePathRn_Object=MibTableColumn
cfprLsbootLanImagePathRn=_CfprLsbootLanImagePathRn_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,3),_CfprLsbootLanImagePathRn_Type())
cfprLsbootLanImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathRn.setStatus(_A)
_CfprLsbootLanImagePathBootIpPolicyName_Type=SnmpAdminString
_CfprLsbootLanImagePathBootIpPolicyName_Object=MibTableColumn
cfprLsbootLanImagePathBootIpPolicyName=_CfprLsbootLanImagePathBootIpPolicyName_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,4),_CfprLsbootLanImagePathBootIpPolicyName_Type())
cfprLsbootLanImagePathBootIpPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathBootIpPolicyName.setStatus(_A)
_CfprLsbootLanImagePathISCSIVnicName_Type=SnmpAdminString
_CfprLsbootLanImagePathISCSIVnicName_Object=MibTableColumn
cfprLsbootLanImagePathISCSIVnicName=_CfprLsbootLanImagePathISCSIVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,5),_CfprLsbootLanImagePathISCSIVnicName_Type())
cfprLsbootLanImagePathISCSIVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathISCSIVnicName.setStatus(_A)
_CfprLsbootLanImagePathImgPolicyName_Type=SnmpAdminString
_CfprLsbootLanImagePathImgPolicyName_Object=MibTableColumn
cfprLsbootLanImagePathImgPolicyName=_CfprLsbootLanImagePathImgPolicyName_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,6),_CfprLsbootLanImagePathImgPolicyName_Type())
cfprLsbootLanImagePathImgPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathImgPolicyName.setStatus(_A)
_CfprLsbootLanImagePathImgSecPolicyName_Type=SnmpAdminString
_CfprLsbootLanImagePathImgSecPolicyName_Object=MibTableColumn
cfprLsbootLanImagePathImgSecPolicyName=_CfprLsbootLanImagePathImgSecPolicyName_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,7),_CfprLsbootLanImagePathImgSecPolicyName_Type())
cfprLsbootLanImagePathImgSecPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathImgSecPolicyName.setStatus(_A)
_CfprLsbootLanImagePathProvSrvPolicyName_Type=SnmpAdminString
_CfprLsbootLanImagePathProvSrvPolicyName_Object=MibTableColumn
cfprLsbootLanImagePathProvSrvPolicyName=_CfprLsbootLanImagePathProvSrvPolicyName_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,8),_CfprLsbootLanImagePathProvSrvPolicyName_Type())
cfprLsbootLanImagePathProvSrvPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathProvSrvPolicyName.setStatus(_A)
_CfprLsbootLanImagePathType_Type=CfprLsbootLanImagePathType
_CfprLsbootLanImagePathType_Object=MibTableColumn
cfprLsbootLanImagePathType=_CfprLsbootLanImagePathType_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,9),_CfprLsbootLanImagePathType_Type())
cfprLsbootLanImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathType.setStatus(_A)
_CfprLsbootLanImagePathVnicName_Type=SnmpAdminString
_CfprLsbootLanImagePathVnicName_Object=MibTableColumn
cfprLsbootLanImagePathVnicName=_CfprLsbootLanImagePathVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,7,1,10),_CfprLsbootLanImagePathVnicName_Type())
cfprLsbootLanImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLanImagePathVnicName.setStatus(_A)
_CfprLsbootLocalHddImageTable_Object=MibTable
cfprLsbootLocalHddImageTable=_CfprLsbootLocalHddImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,8))
if mibBuilder.loadTexts:cfprLsbootLocalHddImageTable.setStatus(_A)
_CfprLsbootLocalHddImageEntry_Object=MibTableRow
cfprLsbootLocalHddImageEntry=_CfprLsbootLocalHddImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,8,1))
cfprLsbootLocalHddImageEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:cfprLsbootLocalHddImageEntry.setStatus(_A)
_CfprLsbootLocalHddImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootLocalHddImageInstanceId_Object=MibTableColumn
cfprLsbootLocalHddImageInstanceId=_CfprLsbootLocalHddImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,8,1,1),_CfprLsbootLocalHddImageInstanceId_Type())
cfprLsbootLocalHddImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootLocalHddImageInstanceId.setStatus(_A)
_CfprLsbootLocalHddImageDn_Type=CfprManagedObjectDn
_CfprLsbootLocalHddImageDn_Object=MibTableColumn
cfprLsbootLocalHddImageDn=_CfprLsbootLocalHddImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,8,1,2),_CfprLsbootLocalHddImageDn_Type())
cfprLsbootLocalHddImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLocalHddImageDn.setStatus(_A)
_CfprLsbootLocalHddImageRn_Type=SnmpAdminString
_CfprLsbootLocalHddImageRn_Object=MibTableColumn
cfprLsbootLocalHddImageRn=_CfprLsbootLocalHddImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,8,1,3),_CfprLsbootLocalHddImageRn_Type())
cfprLsbootLocalHddImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLocalHddImageRn.setStatus(_A)
_CfprLsbootLocalHddImageOrder_Type=Gauge32
_CfprLsbootLocalHddImageOrder_Object=MibTableColumn
cfprLsbootLocalHddImageOrder=_CfprLsbootLocalHddImageOrder_Object((1,3,6,1,4,1,9,9,826,1,47,8,1,4),_CfprLsbootLocalHddImageOrder_Type())
cfprLsbootLocalHddImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLocalHddImageOrder.setStatus(_A)
_CfprLsbootLocalHddImageType_Type=CfprLsbootLocalHddImageType
_CfprLsbootLocalHddImageType_Object=MibTableColumn
cfprLsbootLocalHddImageType=_CfprLsbootLocalHddImageType_Object((1,3,6,1,4,1,9,9,826,1,47,8,1,5),_CfprLsbootLocalHddImageType_Type())
cfprLsbootLocalHddImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLocalHddImageType.setStatus(_A)
_CfprLsbootLocalStorageTable_Object=MibTable
cfprLsbootLocalStorageTable=_CfprLsbootLocalStorageTable_Object((1,3,6,1,4,1,9,9,826,1,47,9))
if mibBuilder.loadTexts:cfprLsbootLocalStorageTable.setStatus(_A)
_CfprLsbootLocalStorageEntry_Object=MibTableRow
cfprLsbootLocalStorageEntry=_CfprLsbootLocalStorageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,9,1))
cfprLsbootLocalStorageEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cfprLsbootLocalStorageEntry.setStatus(_A)
_CfprLsbootLocalStorageInstanceId_Type=CfprManagedObjectId
_CfprLsbootLocalStorageInstanceId_Object=MibTableColumn
cfprLsbootLocalStorageInstanceId=_CfprLsbootLocalStorageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,9,1,1),_CfprLsbootLocalStorageInstanceId_Type())
cfprLsbootLocalStorageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootLocalStorageInstanceId.setStatus(_A)
_CfprLsbootLocalStorageDn_Type=CfprManagedObjectDn
_CfprLsbootLocalStorageDn_Object=MibTableColumn
cfprLsbootLocalStorageDn=_CfprLsbootLocalStorageDn_Object((1,3,6,1,4,1,9,9,826,1,47,9,1,2),_CfprLsbootLocalStorageDn_Type())
cfprLsbootLocalStorageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLocalStorageDn.setStatus(_A)
_CfprLsbootLocalStorageRn_Type=SnmpAdminString
_CfprLsbootLocalStorageRn_Object=MibTableColumn
cfprLsbootLocalStorageRn=_CfprLsbootLocalStorageRn_Object((1,3,6,1,4,1,9,9,826,1,47,9,1,3),_CfprLsbootLocalStorageRn_Type())
cfprLsbootLocalStorageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootLocalStorageRn.setStatus(_A)
_CfprLsbootPolicyTable_Object=MibTable
cfprLsbootPolicyTable=_CfprLsbootPolicyTable_Object((1,3,6,1,4,1,9,9,826,1,47,10))
if mibBuilder.loadTexts:cfprLsbootPolicyTable.setStatus(_A)
_CfprLsbootPolicyEntry_Object=MibTableRow
cfprLsbootPolicyEntry=_CfprLsbootPolicyEntry_Object((1,3,6,1,4,1,9,9,826,1,47,10,1))
cfprLsbootPolicyEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cfprLsbootPolicyEntry.setStatus(_A)
_CfprLsbootPolicyInstanceId_Type=CfprManagedObjectId
_CfprLsbootPolicyInstanceId_Object=MibTableColumn
cfprLsbootPolicyInstanceId=_CfprLsbootPolicyInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,1),_CfprLsbootPolicyInstanceId_Type())
cfprLsbootPolicyInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootPolicyInstanceId.setStatus(_A)
_CfprLsbootPolicyDn_Type=CfprManagedObjectDn
_CfprLsbootPolicyDn_Object=MibTableColumn
cfprLsbootPolicyDn=_CfprLsbootPolicyDn_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,2),_CfprLsbootPolicyDn_Type())
cfprLsbootPolicyDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyDn.setStatus(_A)
_CfprLsbootPolicyRn_Type=SnmpAdminString
_CfprLsbootPolicyRn_Object=MibTableColumn
cfprLsbootPolicyRn=_CfprLsbootPolicyRn_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,3),_CfprLsbootPolicyRn_Type())
cfprLsbootPolicyRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyRn.setStatus(_A)
_CfprLsbootPolicyBootMode_Type=CfprLsbootADefBootMode
_CfprLsbootPolicyBootMode_Object=MibTableColumn
cfprLsbootPolicyBootMode=_CfprLsbootPolicyBootMode_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,4),_CfprLsbootPolicyBootMode_Type())
cfprLsbootPolicyBootMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyBootMode.setStatus(_A)
_CfprLsbootPolicyDescr_Type=SnmpAdminString
_CfprLsbootPolicyDescr_Object=MibTableColumn
cfprLsbootPolicyDescr=_CfprLsbootPolicyDescr_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,5),_CfprLsbootPolicyDescr_Type())
cfprLsbootPolicyDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyDescr.setStatus(_A)
_CfprLsbootPolicyEnforceVnicName_Type=TruthValue
_CfprLsbootPolicyEnforceVnicName_Object=MibTableColumn
cfprLsbootPolicyEnforceVnicName=_CfprLsbootPolicyEnforceVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,6),_CfprLsbootPolicyEnforceVnicName_Type())
cfprLsbootPolicyEnforceVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyEnforceVnicName.setStatus(_A)
_CfprLsbootPolicyIntId_Type=SnmpAdminString
_CfprLsbootPolicyIntId_Object=MibTableColumn
cfprLsbootPolicyIntId=_CfprLsbootPolicyIntId_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,7),_CfprLsbootPolicyIntId_Type())
cfprLsbootPolicyIntId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyIntId.setStatus(_A)
_CfprLsbootPolicyName_Type=SnmpAdminString
_CfprLsbootPolicyName_Object=MibTableColumn
cfprLsbootPolicyName=_CfprLsbootPolicyName_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,8),_CfprLsbootPolicyName_Type())
cfprLsbootPolicyName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyName.setStatus(_A)
_CfprLsbootPolicyPolicyLevel_Type=Gauge32
_CfprLsbootPolicyPolicyLevel_Object=MibTableColumn
cfprLsbootPolicyPolicyLevel=_CfprLsbootPolicyPolicyLevel_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,9),_CfprLsbootPolicyPolicyLevel_Type())
cfprLsbootPolicyPolicyLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyPolicyLevel.setStatus(_A)
_CfprLsbootPolicyPolicyOwner_Type=CfprPolicyPolicyOwner
_CfprLsbootPolicyPolicyOwner_Object=MibTableColumn
cfprLsbootPolicyPolicyOwner=_CfprLsbootPolicyPolicyOwner_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,10),_CfprLsbootPolicyPolicyOwner_Type())
cfprLsbootPolicyPolicyOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyPolicyOwner.setStatus(_A)
_CfprLsbootPolicyPurpose_Type=CfprLsbootPurpose
_CfprLsbootPolicyPurpose_Object=MibTableColumn
cfprLsbootPolicyPurpose=_CfprLsbootPolicyPurpose_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,11),_CfprLsbootPolicyPurpose_Type())
cfprLsbootPolicyPurpose.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyPurpose.setStatus(_A)
_CfprLsbootPolicyRebootOnUpdate_Type=TruthValue
_CfprLsbootPolicyRebootOnUpdate_Object=MibTableColumn
cfprLsbootPolicyRebootOnUpdate=_CfprLsbootPolicyRebootOnUpdate_Object((1,3,6,1,4,1,9,9,826,1,47,10,1,12),_CfprLsbootPolicyRebootOnUpdate_Type())
cfprLsbootPolicyRebootOnUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootPolicyRebootOnUpdate.setStatus(_A)
_CfprLsbootSanTable_Object=MibTable
cfprLsbootSanTable=_CfprLsbootSanTable_Object((1,3,6,1,4,1,9,9,826,1,47,11))
if mibBuilder.loadTexts:cfprLsbootSanTable.setStatus(_A)
_CfprLsbootSanEntry_Object=MibTableRow
cfprLsbootSanEntry=_CfprLsbootSanEntry_Object((1,3,6,1,4,1,9,9,826,1,47,11,1))
cfprLsbootSanEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cfprLsbootSanEntry.setStatus(_A)
_CfprLsbootSanInstanceId_Type=CfprManagedObjectId
_CfprLsbootSanInstanceId_Object=MibTableColumn
cfprLsbootSanInstanceId=_CfprLsbootSanInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,11,1,1),_CfprLsbootSanInstanceId_Type())
cfprLsbootSanInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootSanInstanceId.setStatus(_A)
_CfprLsbootSanDn_Type=CfprManagedObjectDn
_CfprLsbootSanDn_Object=MibTableColumn
cfprLsbootSanDn=_CfprLsbootSanDn_Object((1,3,6,1,4,1,9,9,826,1,47,11,1,2),_CfprLsbootSanDn_Type())
cfprLsbootSanDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanDn.setStatus(_A)
_CfprLsbootSanRn_Type=SnmpAdminString
_CfprLsbootSanRn_Object=MibTableColumn
cfprLsbootSanRn=_CfprLsbootSanRn_Object((1,3,6,1,4,1,9,9,826,1,47,11,1,3),_CfprLsbootSanRn_Type())
cfprLsbootSanRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanRn.setStatus(_A)
_CfprLsbootSanAccess_Type=CfprLsbootSanAccess
_CfprLsbootSanAccess_Object=MibTableColumn
cfprLsbootSanAccess=_CfprLsbootSanAccess_Object((1,3,6,1,4,1,9,9,826,1,47,11,1,4),_CfprLsbootSanAccess_Type())
cfprLsbootSanAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanAccess.setStatus(_A)
_CfprLsbootSanOrder_Type=Gauge32
_CfprLsbootSanOrder_Object=MibTableColumn
cfprLsbootSanOrder=_CfprLsbootSanOrder_Object((1,3,6,1,4,1,9,9,826,1,47,11,1,5),_CfprLsbootSanOrder_Type())
cfprLsbootSanOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanOrder.setStatus(_A)
_CfprLsbootSanType_Type=CfprLsbootSanType
_CfprLsbootSanType_Object=MibTableColumn
cfprLsbootSanType=_CfprLsbootSanType_Object((1,3,6,1,4,1,9,9,826,1,47,11,1,6),_CfprLsbootSanType_Type())
cfprLsbootSanType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanType.setStatus(_A)
_CfprLsbootSanCatSanImageTable_Object=MibTable
cfprLsbootSanCatSanImageTable=_CfprLsbootSanCatSanImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,12))
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageTable.setStatus(_A)
_CfprLsbootSanCatSanImageEntry_Object=MibTableRow
cfprLsbootSanCatSanImageEntry=_CfprLsbootSanCatSanImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,12,1))
cfprLsbootSanCatSanImageEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageEntry.setStatus(_A)
_CfprLsbootSanCatSanImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootSanCatSanImageInstanceId_Object=MibTableColumn
cfprLsbootSanCatSanImageInstanceId=_CfprLsbootSanCatSanImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,12,1,1),_CfprLsbootSanCatSanImageInstanceId_Type())
cfprLsbootSanCatSanImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageInstanceId.setStatus(_A)
_CfprLsbootSanCatSanImageDn_Type=CfprManagedObjectDn
_CfprLsbootSanCatSanImageDn_Object=MibTableColumn
cfprLsbootSanCatSanImageDn=_CfprLsbootSanCatSanImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,12,1,2),_CfprLsbootSanCatSanImageDn_Type())
cfprLsbootSanCatSanImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageDn.setStatus(_A)
_CfprLsbootSanCatSanImageRn_Type=SnmpAdminString
_CfprLsbootSanCatSanImageRn_Object=MibTableColumn
cfprLsbootSanCatSanImageRn=_CfprLsbootSanCatSanImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,12,1,3),_CfprLsbootSanCatSanImageRn_Type())
cfprLsbootSanCatSanImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageRn.setStatus(_A)
_CfprLsbootSanCatSanImageType_Type=CfprLsbootSanCatSanImageType
_CfprLsbootSanCatSanImageType_Object=MibTableColumn
cfprLsbootSanCatSanImageType=_CfprLsbootSanCatSanImageType_Object((1,3,6,1,4,1,9,9,826,1,47,12,1,4),_CfprLsbootSanCatSanImageType_Type())
cfprLsbootSanCatSanImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageType.setStatus(_A)
_CfprLsbootSanCatSanImageVnicName_Type=SnmpAdminString
_CfprLsbootSanCatSanImageVnicName_Object=MibTableColumn
cfprLsbootSanCatSanImageVnicName=_CfprLsbootSanCatSanImageVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,12,1,5),_CfprLsbootSanCatSanImageVnicName_Type())
cfprLsbootSanCatSanImageVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImageVnicName.setStatus(_A)
_CfprLsbootSanCatSanImagePathTable_Object=MibTable
cfprLsbootSanCatSanImagePathTable=_CfprLsbootSanCatSanImagePathTable_Object((1,3,6,1,4,1,9,9,826,1,47,13))
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathTable.setStatus(_A)
_CfprLsbootSanCatSanImagePathEntry_Object=MibTableRow
cfprLsbootSanCatSanImagePathEntry=_CfprLsbootSanCatSanImagePathEntry_Object((1,3,6,1,4,1,9,9,826,1,47,13,1))
cfprLsbootSanCatSanImagePathEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathEntry.setStatus(_A)
_CfprLsbootSanCatSanImagePathInstanceId_Type=CfprManagedObjectId
_CfprLsbootSanCatSanImagePathInstanceId_Object=MibTableColumn
cfprLsbootSanCatSanImagePathInstanceId=_CfprLsbootSanCatSanImagePathInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,1),_CfprLsbootSanCatSanImagePathInstanceId_Type())
cfprLsbootSanCatSanImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathInstanceId.setStatus(_A)
_CfprLsbootSanCatSanImagePathDn_Type=CfprManagedObjectDn
_CfprLsbootSanCatSanImagePathDn_Object=MibTableColumn
cfprLsbootSanCatSanImagePathDn=_CfprLsbootSanCatSanImagePathDn_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,2),_CfprLsbootSanCatSanImagePathDn_Type())
cfprLsbootSanCatSanImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathDn.setStatus(_A)
_CfprLsbootSanCatSanImagePathRn_Type=SnmpAdminString
_CfprLsbootSanCatSanImagePathRn_Object=MibTableColumn
cfprLsbootSanCatSanImagePathRn=_CfprLsbootSanCatSanImagePathRn_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,3),_CfprLsbootSanCatSanImagePathRn_Type())
cfprLsbootSanCatSanImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathRn.setStatus(_A)
_CfprLsbootSanCatSanImagePathLun_Type=SnmpAdminString
_CfprLsbootSanCatSanImagePathLun_Object=MibTableColumn
cfprLsbootSanCatSanImagePathLun=_CfprLsbootSanCatSanImagePathLun_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,4),_CfprLsbootSanCatSanImagePathLun_Type())
cfprLsbootSanCatSanImagePathLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathLun.setStatus(_A)
_CfprLsbootSanCatSanImagePathType_Type=CfprLsbootSanCatSanImagePathType
_CfprLsbootSanCatSanImagePathType_Object=MibTableColumn
cfprLsbootSanCatSanImagePathType=_CfprLsbootSanCatSanImagePathType_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,5),_CfprLsbootSanCatSanImagePathType_Type())
cfprLsbootSanCatSanImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathType.setStatus(_A)
_CfprLsbootSanCatSanImagePathVnicName_Type=SnmpAdminString
_CfprLsbootSanCatSanImagePathVnicName_Object=MibTableColumn
cfprLsbootSanCatSanImagePathVnicName=_CfprLsbootSanCatSanImagePathVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,6),_CfprLsbootSanCatSanImagePathVnicName_Type())
cfprLsbootSanCatSanImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathVnicName.setStatus(_A)
_CfprLsbootSanCatSanImagePathWwn_Type=Unsigned64
_CfprLsbootSanCatSanImagePathWwn_Object=MibTableColumn
cfprLsbootSanCatSanImagePathWwn=_CfprLsbootSanCatSanImagePathWwn_Object((1,3,6,1,4,1,9,9,826,1,47,13,1,7),_CfprLsbootSanCatSanImagePathWwn_Type())
cfprLsbootSanCatSanImagePathWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanCatSanImagePathWwn.setStatus(_A)
_CfprLsbootSanImageTable_Object=MibTable
cfprLsbootSanImageTable=_CfprLsbootSanImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,14))
if mibBuilder.loadTexts:cfprLsbootSanImageTable.setStatus(_A)
_CfprLsbootSanImageEntry_Object=MibTableRow
cfprLsbootSanImageEntry=_CfprLsbootSanImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,14,1))
cfprLsbootSanImageEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cfprLsbootSanImageEntry.setStatus(_A)
_CfprLsbootSanImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootSanImageInstanceId_Object=MibTableColumn
cfprLsbootSanImageInstanceId=_CfprLsbootSanImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,14,1,1),_CfprLsbootSanImageInstanceId_Type())
cfprLsbootSanImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootSanImageInstanceId.setStatus(_A)
_CfprLsbootSanImageDn_Type=CfprManagedObjectDn
_CfprLsbootSanImageDn_Object=MibTableColumn
cfprLsbootSanImageDn=_CfprLsbootSanImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,14,1,2),_CfprLsbootSanImageDn_Type())
cfprLsbootSanImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImageDn.setStatus(_A)
_CfprLsbootSanImageRn_Type=SnmpAdminString
_CfprLsbootSanImageRn_Object=MibTableColumn
cfprLsbootSanImageRn=_CfprLsbootSanImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,14,1,3),_CfprLsbootSanImageRn_Type())
cfprLsbootSanImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImageRn.setStatus(_A)
_CfprLsbootSanImageType_Type=CfprLsbootSanImageType
_CfprLsbootSanImageType_Object=MibTableColumn
cfprLsbootSanImageType=_CfprLsbootSanImageType_Object((1,3,6,1,4,1,9,9,826,1,47,14,1,4),_CfprLsbootSanImageType_Type())
cfprLsbootSanImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImageType.setStatus(_A)
_CfprLsbootSanImageVnicName_Type=SnmpAdminString
_CfprLsbootSanImageVnicName_Object=MibTableColumn
cfprLsbootSanImageVnicName=_CfprLsbootSanImageVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,14,1,5),_CfprLsbootSanImageVnicName_Type())
cfprLsbootSanImageVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImageVnicName.setStatus(_A)
_CfprLsbootSanImagePathTable_Object=MibTable
cfprLsbootSanImagePathTable=_CfprLsbootSanImagePathTable_Object((1,3,6,1,4,1,9,9,826,1,47,15))
if mibBuilder.loadTexts:cfprLsbootSanImagePathTable.setStatus(_A)
_CfprLsbootSanImagePathEntry_Object=MibTableRow
cfprLsbootSanImagePathEntry=_CfprLsbootSanImagePathEntry_Object((1,3,6,1,4,1,9,9,826,1,47,15,1))
cfprLsbootSanImagePathEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:cfprLsbootSanImagePathEntry.setStatus(_A)
_CfprLsbootSanImagePathInstanceId_Type=CfprManagedObjectId
_CfprLsbootSanImagePathInstanceId_Object=MibTableColumn
cfprLsbootSanImagePathInstanceId=_CfprLsbootSanImagePathInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,1),_CfprLsbootSanImagePathInstanceId_Type())
cfprLsbootSanImagePathInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootSanImagePathInstanceId.setStatus(_A)
_CfprLsbootSanImagePathDn_Type=CfprManagedObjectDn
_CfprLsbootSanImagePathDn_Object=MibTableColumn
cfprLsbootSanImagePathDn=_CfprLsbootSanImagePathDn_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,2),_CfprLsbootSanImagePathDn_Type())
cfprLsbootSanImagePathDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImagePathDn.setStatus(_A)
_CfprLsbootSanImagePathRn_Type=SnmpAdminString
_CfprLsbootSanImagePathRn_Object=MibTableColumn
cfprLsbootSanImagePathRn=_CfprLsbootSanImagePathRn_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,3),_CfprLsbootSanImagePathRn_Type())
cfprLsbootSanImagePathRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImagePathRn.setStatus(_A)
_CfprLsbootSanImagePathLun_Type=SnmpAdminString
_CfprLsbootSanImagePathLun_Object=MibTableColumn
cfprLsbootSanImagePathLun=_CfprLsbootSanImagePathLun_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,4),_CfprLsbootSanImagePathLun_Type())
cfprLsbootSanImagePathLun.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImagePathLun.setStatus(_A)
_CfprLsbootSanImagePathType_Type=CfprLsbootSanImagePathType
_CfprLsbootSanImagePathType_Object=MibTableColumn
cfprLsbootSanImagePathType=_CfprLsbootSanImagePathType_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,5),_CfprLsbootSanImagePathType_Type())
cfprLsbootSanImagePathType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImagePathType.setStatus(_A)
_CfprLsbootSanImagePathVnicName_Type=SnmpAdminString
_CfprLsbootSanImagePathVnicName_Object=MibTableColumn
cfprLsbootSanImagePathVnicName=_CfprLsbootSanImagePathVnicName_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,6),_CfprLsbootSanImagePathVnicName_Type())
cfprLsbootSanImagePathVnicName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImagePathVnicName.setStatus(_A)
_CfprLsbootSanImagePathWwn_Type=Unsigned64
_CfprLsbootSanImagePathWwn_Object=MibTableColumn
cfprLsbootSanImagePathWwn=_CfprLsbootSanImagePathWwn_Object((1,3,6,1,4,1,9,9,826,1,47,15,1,7),_CfprLsbootSanImagePathWwn_Type())
cfprLsbootSanImagePathWwn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootSanImagePathWwn.setStatus(_A)
_CfprLsbootStorageTable_Object=MibTable
cfprLsbootStorageTable=_CfprLsbootStorageTable_Object((1,3,6,1,4,1,9,9,826,1,47,16))
if mibBuilder.loadTexts:cfprLsbootStorageTable.setStatus(_A)
_CfprLsbootStorageEntry_Object=MibTableRow
cfprLsbootStorageEntry=_CfprLsbootStorageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,16,1))
cfprLsbootStorageEntry.setIndexNames((0,_C,_T))
if mibBuilder.loadTexts:cfprLsbootStorageEntry.setStatus(_A)
_CfprLsbootStorageInstanceId_Type=CfprManagedObjectId
_CfprLsbootStorageInstanceId_Object=MibTableColumn
cfprLsbootStorageInstanceId=_CfprLsbootStorageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,16,1,1),_CfprLsbootStorageInstanceId_Type())
cfprLsbootStorageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootStorageInstanceId.setStatus(_A)
_CfprLsbootStorageDn_Type=CfprManagedObjectDn
_CfprLsbootStorageDn_Object=MibTableColumn
cfprLsbootStorageDn=_CfprLsbootStorageDn_Object((1,3,6,1,4,1,9,9,826,1,47,16,1,2),_CfprLsbootStorageDn_Type())
cfprLsbootStorageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootStorageDn.setStatus(_A)
_CfprLsbootStorageRn_Type=SnmpAdminString
_CfprLsbootStorageRn_Object=MibTableColumn
cfprLsbootStorageRn=_CfprLsbootStorageRn_Object((1,3,6,1,4,1,9,9,826,1,47,16,1,3),_CfprLsbootStorageRn_Type())
cfprLsbootStorageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootStorageRn.setStatus(_A)
_CfprLsbootStorageAccess_Type=CfprLsbootStorageAccess
_CfprLsbootStorageAccess_Object=MibTableColumn
cfprLsbootStorageAccess=_CfprLsbootStorageAccess_Object((1,3,6,1,4,1,9,9,826,1,47,16,1,4),_CfprLsbootStorageAccess_Type())
cfprLsbootStorageAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootStorageAccess.setStatus(_A)
_CfprLsbootStorageOrder_Type=Gauge32
_CfprLsbootStorageOrder_Object=MibTableColumn
cfprLsbootStorageOrder=_CfprLsbootStorageOrder_Object((1,3,6,1,4,1,9,9,826,1,47,16,1,5),_CfprLsbootStorageOrder_Type())
cfprLsbootStorageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootStorageOrder.setStatus(_A)
_CfprLsbootStorageType_Type=CfprLsbootStorageType
_CfprLsbootStorageType_Object=MibTableColumn
cfprLsbootStorageType=_CfprLsbootStorageType_Object((1,3,6,1,4,1,9,9,826,1,47,16,1,6),_CfprLsbootStorageType_Type())
cfprLsbootStorageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootStorageType.setStatus(_A)
_CfprLsbootUsbExternalImageTable_Object=MibTable
cfprLsbootUsbExternalImageTable=_CfprLsbootUsbExternalImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,17))
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageTable.setStatus(_A)
_CfprLsbootUsbExternalImageEntry_Object=MibTableRow
cfprLsbootUsbExternalImageEntry=_CfprLsbootUsbExternalImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,17,1))
cfprLsbootUsbExternalImageEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageEntry.setStatus(_A)
_CfprLsbootUsbExternalImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootUsbExternalImageInstanceId_Object=MibTableColumn
cfprLsbootUsbExternalImageInstanceId=_CfprLsbootUsbExternalImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,17,1,1),_CfprLsbootUsbExternalImageInstanceId_Type())
cfprLsbootUsbExternalImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageInstanceId.setStatus(_A)
_CfprLsbootUsbExternalImageDn_Type=CfprManagedObjectDn
_CfprLsbootUsbExternalImageDn_Object=MibTableColumn
cfprLsbootUsbExternalImageDn=_CfprLsbootUsbExternalImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,17,1,2),_CfprLsbootUsbExternalImageDn_Type())
cfprLsbootUsbExternalImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageDn.setStatus(_A)
_CfprLsbootUsbExternalImageRn_Type=SnmpAdminString
_CfprLsbootUsbExternalImageRn_Object=MibTableColumn
cfprLsbootUsbExternalImageRn=_CfprLsbootUsbExternalImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,17,1,3),_CfprLsbootUsbExternalImageRn_Type())
cfprLsbootUsbExternalImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageRn.setStatus(_A)
_CfprLsbootUsbExternalImageOrder_Type=Gauge32
_CfprLsbootUsbExternalImageOrder_Object=MibTableColumn
cfprLsbootUsbExternalImageOrder=_CfprLsbootUsbExternalImageOrder_Object((1,3,6,1,4,1,9,9,826,1,47,17,1,4),_CfprLsbootUsbExternalImageOrder_Type())
cfprLsbootUsbExternalImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageOrder.setStatus(_A)
_CfprLsbootUsbExternalImageType_Type=CfprLsbootUsbExternalImageType
_CfprLsbootUsbExternalImageType_Object=MibTableColumn
cfprLsbootUsbExternalImageType=_CfprLsbootUsbExternalImageType_Object((1,3,6,1,4,1,9,9,826,1,47,17,1,5),_CfprLsbootUsbExternalImageType_Type())
cfprLsbootUsbExternalImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbExternalImageType.setStatus(_A)
_CfprLsbootUsbFlashStorageImageTable_Object=MibTable
cfprLsbootUsbFlashStorageImageTable=_CfprLsbootUsbFlashStorageImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,18))
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageTable.setStatus(_A)
_CfprLsbootUsbFlashStorageImageEntry_Object=MibTableRow
cfprLsbootUsbFlashStorageImageEntry=_CfprLsbootUsbFlashStorageImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,18,1))
cfprLsbootUsbFlashStorageImageEntry.setIndexNames((0,_C,_V))
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageEntry.setStatus(_A)
_CfprLsbootUsbFlashStorageImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootUsbFlashStorageImageInstanceId_Object=MibTableColumn
cfprLsbootUsbFlashStorageImageInstanceId=_CfprLsbootUsbFlashStorageImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,18,1,1),_CfprLsbootUsbFlashStorageImageInstanceId_Type())
cfprLsbootUsbFlashStorageImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageInstanceId.setStatus(_A)
_CfprLsbootUsbFlashStorageImageDn_Type=CfprManagedObjectDn
_CfprLsbootUsbFlashStorageImageDn_Object=MibTableColumn
cfprLsbootUsbFlashStorageImageDn=_CfprLsbootUsbFlashStorageImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,18,1,2),_CfprLsbootUsbFlashStorageImageDn_Type())
cfprLsbootUsbFlashStorageImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageDn.setStatus(_A)
_CfprLsbootUsbFlashStorageImageRn_Type=SnmpAdminString
_CfprLsbootUsbFlashStorageImageRn_Object=MibTableColumn
cfprLsbootUsbFlashStorageImageRn=_CfprLsbootUsbFlashStorageImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,18,1,3),_CfprLsbootUsbFlashStorageImageRn_Type())
cfprLsbootUsbFlashStorageImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageRn.setStatus(_A)
_CfprLsbootUsbFlashStorageImageOrder_Type=Gauge32
_CfprLsbootUsbFlashStorageImageOrder_Object=MibTableColumn
cfprLsbootUsbFlashStorageImageOrder=_CfprLsbootUsbFlashStorageImageOrder_Object((1,3,6,1,4,1,9,9,826,1,47,18,1,4),_CfprLsbootUsbFlashStorageImageOrder_Type())
cfprLsbootUsbFlashStorageImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageOrder.setStatus(_A)
_CfprLsbootUsbFlashStorageImageType_Type=CfprLsbootUsbFlashStorageImageType
_CfprLsbootUsbFlashStorageImageType_Object=MibTableColumn
cfprLsbootUsbFlashStorageImageType=_CfprLsbootUsbFlashStorageImageType_Object((1,3,6,1,4,1,9,9,826,1,47,18,1,5),_CfprLsbootUsbFlashStorageImageType_Type())
cfprLsbootUsbFlashStorageImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbFlashStorageImageType.setStatus(_A)
_CfprLsbootUsbInternalImageTable_Object=MibTable
cfprLsbootUsbInternalImageTable=_CfprLsbootUsbInternalImageTable_Object((1,3,6,1,4,1,9,9,826,1,47,19))
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageTable.setStatus(_A)
_CfprLsbootUsbInternalImageEntry_Object=MibTableRow
cfprLsbootUsbInternalImageEntry=_CfprLsbootUsbInternalImageEntry_Object((1,3,6,1,4,1,9,9,826,1,47,19,1))
cfprLsbootUsbInternalImageEntry.setIndexNames((0,_C,_W))
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageEntry.setStatus(_A)
_CfprLsbootUsbInternalImageInstanceId_Type=CfprManagedObjectId
_CfprLsbootUsbInternalImageInstanceId_Object=MibTableColumn
cfprLsbootUsbInternalImageInstanceId=_CfprLsbootUsbInternalImageInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,19,1,1),_CfprLsbootUsbInternalImageInstanceId_Type())
cfprLsbootUsbInternalImageInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageInstanceId.setStatus(_A)
_CfprLsbootUsbInternalImageDn_Type=CfprManagedObjectDn
_CfprLsbootUsbInternalImageDn_Object=MibTableColumn
cfprLsbootUsbInternalImageDn=_CfprLsbootUsbInternalImageDn_Object((1,3,6,1,4,1,9,9,826,1,47,19,1,2),_CfprLsbootUsbInternalImageDn_Type())
cfprLsbootUsbInternalImageDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageDn.setStatus(_A)
_CfprLsbootUsbInternalImageRn_Type=SnmpAdminString
_CfprLsbootUsbInternalImageRn_Object=MibTableColumn
cfprLsbootUsbInternalImageRn=_CfprLsbootUsbInternalImageRn_Object((1,3,6,1,4,1,9,9,826,1,47,19,1,3),_CfprLsbootUsbInternalImageRn_Type())
cfprLsbootUsbInternalImageRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageRn.setStatus(_A)
_CfprLsbootUsbInternalImageOrder_Type=Gauge32
_CfprLsbootUsbInternalImageOrder_Object=MibTableColumn
cfprLsbootUsbInternalImageOrder=_CfprLsbootUsbInternalImageOrder_Object((1,3,6,1,4,1,9,9,826,1,47,19,1,4),_CfprLsbootUsbInternalImageOrder_Type())
cfprLsbootUsbInternalImageOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageOrder.setStatus(_A)
_CfprLsbootUsbInternalImageType_Type=CfprLsbootUsbInternalImageType
_CfprLsbootUsbInternalImageType_Object=MibTableColumn
cfprLsbootUsbInternalImageType=_CfprLsbootUsbInternalImageType_Object((1,3,6,1,4,1,9,9,826,1,47,19,1,5),_CfprLsbootUsbInternalImageType_Type())
cfprLsbootUsbInternalImageType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootUsbInternalImageType.setStatus(_A)
_CfprLsbootVirtualMediaTable_Object=MibTable
cfprLsbootVirtualMediaTable=_CfprLsbootVirtualMediaTable_Object((1,3,6,1,4,1,9,9,826,1,47,20))
if mibBuilder.loadTexts:cfprLsbootVirtualMediaTable.setStatus(_A)
_CfprLsbootVirtualMediaEntry_Object=MibTableRow
cfprLsbootVirtualMediaEntry=_CfprLsbootVirtualMediaEntry_Object((1,3,6,1,4,1,9,9,826,1,47,20,1))
cfprLsbootVirtualMediaEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cfprLsbootVirtualMediaEntry.setStatus(_A)
_CfprLsbootVirtualMediaInstanceId_Type=CfprManagedObjectId
_CfprLsbootVirtualMediaInstanceId_Object=MibTableColumn
cfprLsbootVirtualMediaInstanceId=_CfprLsbootVirtualMediaInstanceId_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,1),_CfprLsbootVirtualMediaInstanceId_Type())
cfprLsbootVirtualMediaInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaInstanceId.setStatus(_A)
_CfprLsbootVirtualMediaDn_Type=CfprManagedObjectDn
_CfprLsbootVirtualMediaDn_Object=MibTableColumn
cfprLsbootVirtualMediaDn=_CfprLsbootVirtualMediaDn_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,2),_CfprLsbootVirtualMediaDn_Type())
cfprLsbootVirtualMediaDn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaDn.setStatus(_A)
_CfprLsbootVirtualMediaRn_Type=SnmpAdminString
_CfprLsbootVirtualMediaRn_Object=MibTableColumn
cfprLsbootVirtualMediaRn=_CfprLsbootVirtualMediaRn_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,3),_CfprLsbootVirtualMediaRn_Type())
cfprLsbootVirtualMediaRn.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaRn.setStatus(_A)
_CfprLsbootVirtualMediaAccess_Type=CfprLsbootAccessType
_CfprLsbootVirtualMediaAccess_Object=MibTableColumn
cfprLsbootVirtualMediaAccess=_CfprLsbootVirtualMediaAccess_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,4),_CfprLsbootVirtualMediaAccess_Type())
cfprLsbootVirtualMediaAccess.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaAccess.setStatus(_A)
_CfprLsbootVirtualMediaLunId_Type=SnmpAdminString
_CfprLsbootVirtualMediaLunId_Object=MibTableColumn
cfprLsbootVirtualMediaLunId=_CfprLsbootVirtualMediaLunId_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,5),_CfprLsbootVirtualMediaLunId_Type())
cfprLsbootVirtualMediaLunId.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaLunId.setStatus(_A)
_CfprLsbootVirtualMediaMappingName_Type=SnmpAdminString
_CfprLsbootVirtualMediaMappingName_Object=MibTableColumn
cfprLsbootVirtualMediaMappingName=_CfprLsbootVirtualMediaMappingName_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,6),_CfprLsbootVirtualMediaMappingName_Type())
cfprLsbootVirtualMediaMappingName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaMappingName.setStatus(_A)
_CfprLsbootVirtualMediaOrder_Type=Gauge32
_CfprLsbootVirtualMediaOrder_Object=MibTableColumn
cfprLsbootVirtualMediaOrder=_CfprLsbootVirtualMediaOrder_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,7),_CfprLsbootVirtualMediaOrder_Type())
cfprLsbootVirtualMediaOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaOrder.setStatus(_A)
_CfprLsbootVirtualMediaType_Type=CfprLsbootVirtualMediaType
_CfprLsbootVirtualMediaType_Object=MibTableColumn
cfprLsbootVirtualMediaType=_CfprLsbootVirtualMediaType_Object((1,3,6,1,4,1,9,9,826,1,47,20,1,8),_CfprLsbootVirtualMediaType_Type())
cfprLsbootVirtualMediaType.setMaxAccess(_B)
if mibBuilder.loadTexts:cfprLsbootVirtualMediaType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'cfprLsbootObjects':cfprLsbootObjects,'cfprLsbootBootSecurityTable':cfprLsbootBootSecurityTable,'cfprLsbootBootSecurityEntry':cfprLsbootBootSecurityEntry,_E:cfprLsbootBootSecurityInstanceId,'cfprLsbootBootSecurityDn':cfprLsbootBootSecurityDn,'cfprLsbootBootSecurityRn':cfprLsbootBootSecurityRn,'cfprLsbootBootSecuritySecureBoot':cfprLsbootBootSecuritySecureBoot,'cfprLsbootDefTable':cfprLsbootDefTable,'cfprLsbootDefEntry':cfprLsbootDefEntry,_F:cfprLsbootDefInstanceId,'cfprLsbootDefDn':cfprLsbootDefDn,'cfprLsbootDefRn':cfprLsbootDefRn,'cfprLsbootDefAdvBootOrderApplicable':cfprLsbootDefAdvBootOrderApplicable,'cfprLsbootDefBootMode':cfprLsbootDefBootMode,'cfprLsbootDefDescr':cfprLsbootDefDescr,'cfprLsbootDefEnforceVnicName':cfprLsbootDefEnforceVnicName,'cfprLsbootDefIntId':cfprLsbootDefIntId,'cfprLsbootDefName':cfprLsbootDefName,'cfprLsbootDefPolicyLevel':cfprLsbootDefPolicyLevel,'cfprLsbootDefPolicyOwner':cfprLsbootDefPolicyOwner,'cfprLsbootDefPurpose':cfprLsbootDefPurpose,'cfprLsbootDefRebootOnUpdate':cfprLsbootDefRebootOnUpdate,'cfprLsbootDefaultLocalImageTable':cfprLsbootDefaultLocalImageTable,'cfprLsbootDefaultLocalImageEntry':cfprLsbootDefaultLocalImageEntry,_G:cfprLsbootDefaultLocalImageInstanceId,'cfprLsbootDefaultLocalImageDn':cfprLsbootDefaultLocalImageDn,'cfprLsbootDefaultLocalImageRn':cfprLsbootDefaultLocalImageRn,'cfprLsbootDefaultLocalImageOrder':cfprLsbootDefaultLocalImageOrder,'cfprLsbootDefaultLocalImageType':cfprLsbootDefaultLocalImageType,'cfprLsbootIScsiTable':cfprLsbootIScsiTable,'cfprLsbootIScsiEntry':cfprLsbootIScsiEntry,_H:cfprLsbootIScsiInstanceId,'cfprLsbootIScsiDn':cfprLsbootIScsiDn,'cfprLsbootIScsiRn':cfprLsbootIScsiRn,'cfprLsbootIScsiAccess':cfprLsbootIScsiAccess,'cfprLsbootIScsiOrder':cfprLsbootIScsiOrder,'cfprLsbootIScsiType':cfprLsbootIScsiType,'cfprLsbootIScsiImagePathTable':cfprLsbootIScsiImagePathTable,'cfprLsbootIScsiImagePathEntry':cfprLsbootIScsiImagePathEntry,_I:cfprLsbootIScsiImagePathInstanceId,'cfprLsbootIScsiImagePathDn':cfprLsbootIScsiImagePathDn,'cfprLsbootIScsiImagePathRn':cfprLsbootIScsiImagePathRn,'cfprLsbootIScsiImagePathISCSIVnicName':cfprLsbootIScsiImagePathISCSIVnicName,'cfprLsbootIScsiImagePathType':cfprLsbootIScsiImagePathType,'cfprLsbootIScsiImagePathVnicName':cfprLsbootIScsiImagePathVnicName,'cfprLsbootLanTable':cfprLsbootLanTable,'cfprLsbootLanEntry':cfprLsbootLanEntry,_J:cfprLsbootLanInstanceId,'cfprLsbootLanDn':cfprLsbootLanDn,'cfprLsbootLanRn':cfprLsbootLanRn,'cfprLsbootLanAccess':cfprLsbootLanAccess,'cfprLsbootLanOrder':cfprLsbootLanOrder,'cfprLsbootLanProt':cfprLsbootLanProt,'cfprLsbootLanType':cfprLsbootLanType,'cfprLsbootLanImagePathTable':cfprLsbootLanImagePathTable,'cfprLsbootLanImagePathEntry':cfprLsbootLanImagePathEntry,_K:cfprLsbootLanImagePathInstanceId,'cfprLsbootLanImagePathDn':cfprLsbootLanImagePathDn,'cfprLsbootLanImagePathRn':cfprLsbootLanImagePathRn,'cfprLsbootLanImagePathBootIpPolicyName':cfprLsbootLanImagePathBootIpPolicyName,'cfprLsbootLanImagePathISCSIVnicName':cfprLsbootLanImagePathISCSIVnicName,'cfprLsbootLanImagePathImgPolicyName':cfprLsbootLanImagePathImgPolicyName,'cfprLsbootLanImagePathImgSecPolicyName':cfprLsbootLanImagePathImgSecPolicyName,'cfprLsbootLanImagePathProvSrvPolicyName':cfprLsbootLanImagePathProvSrvPolicyName,'cfprLsbootLanImagePathType':cfprLsbootLanImagePathType,'cfprLsbootLanImagePathVnicName':cfprLsbootLanImagePathVnicName,'cfprLsbootLocalHddImageTable':cfprLsbootLocalHddImageTable,'cfprLsbootLocalHddImageEntry':cfprLsbootLocalHddImageEntry,_L:cfprLsbootLocalHddImageInstanceId,'cfprLsbootLocalHddImageDn':cfprLsbootLocalHddImageDn,'cfprLsbootLocalHddImageRn':cfprLsbootLocalHddImageRn,'cfprLsbootLocalHddImageOrder':cfprLsbootLocalHddImageOrder,'cfprLsbootLocalHddImageType':cfprLsbootLocalHddImageType,'cfprLsbootLocalStorageTable':cfprLsbootLocalStorageTable,'cfprLsbootLocalStorageEntry':cfprLsbootLocalStorageEntry,_M:cfprLsbootLocalStorageInstanceId,'cfprLsbootLocalStorageDn':cfprLsbootLocalStorageDn,'cfprLsbootLocalStorageRn':cfprLsbootLocalStorageRn,'cfprLsbootPolicyTable':cfprLsbootPolicyTable,'cfprLsbootPolicyEntry':cfprLsbootPolicyEntry,_N:cfprLsbootPolicyInstanceId,'cfprLsbootPolicyDn':cfprLsbootPolicyDn,'cfprLsbootPolicyRn':cfprLsbootPolicyRn,'cfprLsbootPolicyBootMode':cfprLsbootPolicyBootMode,'cfprLsbootPolicyDescr':cfprLsbootPolicyDescr,'cfprLsbootPolicyEnforceVnicName':cfprLsbootPolicyEnforceVnicName,'cfprLsbootPolicyIntId':cfprLsbootPolicyIntId,'cfprLsbootPolicyName':cfprLsbootPolicyName,'cfprLsbootPolicyPolicyLevel':cfprLsbootPolicyPolicyLevel,'cfprLsbootPolicyPolicyOwner':cfprLsbootPolicyPolicyOwner,'cfprLsbootPolicyPurpose':cfprLsbootPolicyPurpose,'cfprLsbootPolicyRebootOnUpdate':cfprLsbootPolicyRebootOnUpdate,'cfprLsbootSanTable':cfprLsbootSanTable,'cfprLsbootSanEntry':cfprLsbootSanEntry,_O:cfprLsbootSanInstanceId,'cfprLsbootSanDn':cfprLsbootSanDn,'cfprLsbootSanRn':cfprLsbootSanRn,'cfprLsbootSanAccess':cfprLsbootSanAccess,'cfprLsbootSanOrder':cfprLsbootSanOrder,'cfprLsbootSanType':cfprLsbootSanType,'cfprLsbootSanCatSanImageTable':cfprLsbootSanCatSanImageTable,'cfprLsbootSanCatSanImageEntry':cfprLsbootSanCatSanImageEntry,_P:cfprLsbootSanCatSanImageInstanceId,'cfprLsbootSanCatSanImageDn':cfprLsbootSanCatSanImageDn,'cfprLsbootSanCatSanImageRn':cfprLsbootSanCatSanImageRn,'cfprLsbootSanCatSanImageType':cfprLsbootSanCatSanImageType,'cfprLsbootSanCatSanImageVnicName':cfprLsbootSanCatSanImageVnicName,'cfprLsbootSanCatSanImagePathTable':cfprLsbootSanCatSanImagePathTable,'cfprLsbootSanCatSanImagePathEntry':cfprLsbootSanCatSanImagePathEntry,_Q:cfprLsbootSanCatSanImagePathInstanceId,'cfprLsbootSanCatSanImagePathDn':cfprLsbootSanCatSanImagePathDn,'cfprLsbootSanCatSanImagePathRn':cfprLsbootSanCatSanImagePathRn,'cfprLsbootSanCatSanImagePathLun':cfprLsbootSanCatSanImagePathLun,'cfprLsbootSanCatSanImagePathType':cfprLsbootSanCatSanImagePathType,'cfprLsbootSanCatSanImagePathVnicName':cfprLsbootSanCatSanImagePathVnicName,'cfprLsbootSanCatSanImagePathWwn':cfprLsbootSanCatSanImagePathWwn,'cfprLsbootSanImageTable':cfprLsbootSanImageTable,'cfprLsbootSanImageEntry':cfprLsbootSanImageEntry,_R:cfprLsbootSanImageInstanceId,'cfprLsbootSanImageDn':cfprLsbootSanImageDn,'cfprLsbootSanImageRn':cfprLsbootSanImageRn,'cfprLsbootSanImageType':cfprLsbootSanImageType,'cfprLsbootSanImageVnicName':cfprLsbootSanImageVnicName,'cfprLsbootSanImagePathTable':cfprLsbootSanImagePathTable,'cfprLsbootSanImagePathEntry':cfprLsbootSanImagePathEntry,_S:cfprLsbootSanImagePathInstanceId,'cfprLsbootSanImagePathDn':cfprLsbootSanImagePathDn,'cfprLsbootSanImagePathRn':cfprLsbootSanImagePathRn,'cfprLsbootSanImagePathLun':cfprLsbootSanImagePathLun,'cfprLsbootSanImagePathType':cfprLsbootSanImagePathType,'cfprLsbootSanImagePathVnicName':cfprLsbootSanImagePathVnicName,'cfprLsbootSanImagePathWwn':cfprLsbootSanImagePathWwn,'cfprLsbootStorageTable':cfprLsbootStorageTable,'cfprLsbootStorageEntry':cfprLsbootStorageEntry,_T:cfprLsbootStorageInstanceId,'cfprLsbootStorageDn':cfprLsbootStorageDn,'cfprLsbootStorageRn':cfprLsbootStorageRn,'cfprLsbootStorageAccess':cfprLsbootStorageAccess,'cfprLsbootStorageOrder':cfprLsbootStorageOrder,'cfprLsbootStorageType':cfprLsbootStorageType,'cfprLsbootUsbExternalImageTable':cfprLsbootUsbExternalImageTable,'cfprLsbootUsbExternalImageEntry':cfprLsbootUsbExternalImageEntry,_U:cfprLsbootUsbExternalImageInstanceId,'cfprLsbootUsbExternalImageDn':cfprLsbootUsbExternalImageDn,'cfprLsbootUsbExternalImageRn':cfprLsbootUsbExternalImageRn,'cfprLsbootUsbExternalImageOrder':cfprLsbootUsbExternalImageOrder,'cfprLsbootUsbExternalImageType':cfprLsbootUsbExternalImageType,'cfprLsbootUsbFlashStorageImageTable':cfprLsbootUsbFlashStorageImageTable,'cfprLsbootUsbFlashStorageImageEntry':cfprLsbootUsbFlashStorageImageEntry,_V:cfprLsbootUsbFlashStorageImageInstanceId,'cfprLsbootUsbFlashStorageImageDn':cfprLsbootUsbFlashStorageImageDn,'cfprLsbootUsbFlashStorageImageRn':cfprLsbootUsbFlashStorageImageRn,'cfprLsbootUsbFlashStorageImageOrder':cfprLsbootUsbFlashStorageImageOrder,'cfprLsbootUsbFlashStorageImageType':cfprLsbootUsbFlashStorageImageType,'cfprLsbootUsbInternalImageTable':cfprLsbootUsbInternalImageTable,'cfprLsbootUsbInternalImageEntry':cfprLsbootUsbInternalImageEntry,_W:cfprLsbootUsbInternalImageInstanceId,'cfprLsbootUsbInternalImageDn':cfprLsbootUsbInternalImageDn,'cfprLsbootUsbInternalImageRn':cfprLsbootUsbInternalImageRn,'cfprLsbootUsbInternalImageOrder':cfprLsbootUsbInternalImageOrder,'cfprLsbootUsbInternalImageType':cfprLsbootUsbInternalImageType,'cfprLsbootVirtualMediaTable':cfprLsbootVirtualMediaTable,'cfprLsbootVirtualMediaEntry':cfprLsbootVirtualMediaEntry,_X:cfprLsbootVirtualMediaInstanceId,'cfprLsbootVirtualMediaDn':cfprLsbootVirtualMediaDn,'cfprLsbootVirtualMediaRn':cfprLsbootVirtualMediaRn,'cfprLsbootVirtualMediaAccess':cfprLsbootVirtualMediaAccess,'cfprLsbootVirtualMediaLunId':cfprLsbootVirtualMediaLunId,'cfprLsbootVirtualMediaMappingName':cfprLsbootVirtualMediaMappingName,'cfprLsbootVirtualMediaOrder':cfprLsbootVirtualMediaOrder,'cfprLsbootVirtualMediaType':cfprLsbootVirtualMediaType})