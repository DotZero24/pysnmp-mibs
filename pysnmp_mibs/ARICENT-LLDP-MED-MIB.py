_g='fsLldpXMedMediaPolicyAppType'
_f='fsLldpMedLocLocationEntry'
_e='fsLldpMedPortConfigEntry'
_d='fsLldpMedStatsDestMACAddress'
_c='fsLldpMedStatsIfIndex'
_b='fsLldpXMedRemMediaPolicyAppType'
_a='read-create'
_Z='fsLldpMedLocMediaPolicyAppType'
_Y='TruthValue'
_X='Gauge32'
_W='lldpV2LocPortIfIndex'
_V='lldpRemPortId'
_U='lldpRemChassisId'
_T='lldpXMedRemLocationSubtype'
_S='LLDP-EXT-MED-MIB'
_R='OctetString'
_Q='LLDP frames'
_P='unknown'
_O='LLDP-MIB'
_N='not-accessible'
_M='TLVs'
_L='DisplayString'
_K='lldpV2RemTimeMark'
_J='lldpV2RemLocalIfIndex'
_I='lldpV2RemLocalDestMACAddress'
_H='lldpV2RemIndex'
_G='read-write'
_F='ARICENT-LLDP-MED-MIB'
_E='SnmpAdminString'
_D='Integer32'
_C='LLDP-V2-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
LldpXMedCapabilities,LldpXMedDeviceClass,LocationSubtype,PolicyAppType,lldpXMedLocLocationEntry,lldpXMedRemLocationSubtype=mibBuilder.importSymbols(_S,'LldpXMedCapabilities','LldpXMedDeviceClass','LocationSubtype','PolicyAppType','lldpXMedLocLocationEntry',_T)
LldpChassisId,lldpRemChassisId,lldpRemPortId=mibBuilder.importSymbols(_O,'LldpChassisId',_U,_V)
lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_C,_W,'lldpV2PortConfigEntry',_H,_I,_J,_K)
LldpV2ChassisId,LldpV2ChassisIdSubtype,LldpV2DestAddressTableIndex,LldpV2PortId=mibBuilder.importSymbols('LLDP-V2-TC-MIB','LldpV2ChassisId','LldpV2ChassisIdSubtype','LldpV2DestAddressTableIndex','LldpV2PortId')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_X,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention',_Y)
fsLldpMed=ModuleIdentity((1,3,6,1,4,1,29601,2,101))
if mibBuilder.loadTexts:fsLldpMed.setRevisions(('2015-06-23 00:00',))
_FsLldpMedLocalConfig_ObjectIdentity=ObjectIdentity
fsLldpMedLocalConfig=_FsLldpMedLocalConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,101,1))
_FsLldpMedPortConfigTable_Object=MibTable
fsLldpMedPortConfigTable=_FsLldpMedPortConfigTable_Object((1,3,6,1,4,1,29601,2,101,1,1))
if mibBuilder.loadTexts:fsLldpMedPortConfigTable.setStatus(_A)
_FsLldpMedPortConfigEntry_Object=MibTableRow
fsLldpMedPortConfigEntry=_FsLldpMedPortConfigEntry_Object((1,3,6,1,4,1,29601,2,101,1,1,1))
if mibBuilder.loadTexts:fsLldpMedPortConfigEntry.setStatus(_A)
_FsLldpMedPortCapSupported_Type=LldpXMedCapabilities
_FsLldpMedPortCapSupported_Object=MibTableColumn
fsLldpMedPortCapSupported=_FsLldpMedPortCapSupported_Object((1,3,6,1,4,1,29601,2,101,1,1,1,1),_FsLldpMedPortCapSupported_Type())
fsLldpMedPortCapSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedPortCapSupported.setStatus(_A)
_FsLldpMedPortConfigTLVsTxEnable_Type=LldpXMedCapabilities
_FsLldpMedPortConfigTLVsTxEnable_Object=MibTableColumn
fsLldpMedPortConfigTLVsTxEnable=_FsLldpMedPortConfigTLVsTxEnable_Object((1,3,6,1,4,1,29601,2,101,1,1,1,2),_FsLldpMedPortConfigTLVsTxEnable_Type())
fsLldpMedPortConfigTLVsTxEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedPortConfigTLVsTxEnable.setStatus(_A)
_FsLldpMedLocMediaPolicyTable_Object=MibTable
fsLldpMedLocMediaPolicyTable=_FsLldpMedLocMediaPolicyTable_Object((1,3,6,1,4,1,29601,2,101,1,2))
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyTable.setStatus(_A)
_FsLldpMedLocMediaPolicyEntry_Object=MibTableRow
fsLldpMedLocMediaPolicyEntry=_FsLldpMedLocMediaPolicyEntry_Object((1,3,6,1,4,1,29601,2,101,1,2,1))
fsLldpMedLocMediaPolicyEntry.setIndexNames((0,_C,_W),(0,_F,_Z))
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyEntry.setStatus(_A)
_FsLldpMedLocMediaPolicyAppType_Type=PolicyAppType
_FsLldpMedLocMediaPolicyAppType_Object=MibTableColumn
fsLldpMedLocMediaPolicyAppType=_FsLldpMedLocMediaPolicyAppType_Object((1,3,6,1,4,1,29601,2,101,1,2,1,1),_FsLldpMedLocMediaPolicyAppType_Type())
fsLldpMedLocMediaPolicyAppType.setMaxAccess(_N)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyAppType.setStatus(_A)
class _FsLldpMedLocMediaPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_FsLldpMedLocMediaPolicyVlanID_Type.__name__=_D
_FsLldpMedLocMediaPolicyVlanID_Object=MibTableColumn
fsLldpMedLocMediaPolicyVlanID=_FsLldpMedLocMediaPolicyVlanID_Object((1,3,6,1,4,1,29601,2,101,1,2,1,2),_FsLldpMedLocMediaPolicyVlanID_Type())
fsLldpMedLocMediaPolicyVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyVlanID.setStatus(_A)
class _FsLldpMedLocMediaPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsLldpMedLocMediaPolicyPriority_Type.__name__=_D
_FsLldpMedLocMediaPolicyPriority_Object=MibTableColumn
fsLldpMedLocMediaPolicyPriority=_FsLldpMedLocMediaPolicyPriority_Object((1,3,6,1,4,1,29601,2,101,1,2,1,3),_FsLldpMedLocMediaPolicyPriority_Type())
fsLldpMedLocMediaPolicyPriority.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyPriority.setStatus(_A)
class _FsLldpMedLocMediaPolicyDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FsLldpMedLocMediaPolicyDscp_Type.__name__=_D
_FsLldpMedLocMediaPolicyDscp_Object=MibTableColumn
fsLldpMedLocMediaPolicyDscp=_FsLldpMedLocMediaPolicyDscp_Object((1,3,6,1,4,1,29601,2,101,1,2,1,4),_FsLldpMedLocMediaPolicyDscp_Type())
fsLldpMedLocMediaPolicyDscp.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyDscp.setStatus(_A)
_FsLldpMedLocMediaPolicyUnknown_Type=TruthValue
_FsLldpMedLocMediaPolicyUnknown_Object=MibTableColumn
fsLldpMedLocMediaPolicyUnknown=_FsLldpMedLocMediaPolicyUnknown_Object((1,3,6,1,4,1,29601,2,101,1,2,1,5),_FsLldpMedLocMediaPolicyUnknown_Type())
fsLldpMedLocMediaPolicyUnknown.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyUnknown.setStatus(_A)
_FsLldpMedLocMediaPolicyTagged_Type=TruthValue
_FsLldpMedLocMediaPolicyTagged_Object=MibTableColumn
fsLldpMedLocMediaPolicyTagged=_FsLldpMedLocMediaPolicyTagged_Object((1,3,6,1,4,1,29601,2,101,1,2,1,6),_FsLldpMedLocMediaPolicyTagged_Type())
fsLldpMedLocMediaPolicyTagged.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyTagged.setStatus(_A)
_FsLldpMedLocMediaPolicyRowStatus_Type=RowStatus
_FsLldpMedLocMediaPolicyRowStatus_Object=MibTableColumn
fsLldpMedLocMediaPolicyRowStatus=_FsLldpMedLocMediaPolicyRowStatus_Object((1,3,6,1,4,1,29601,2,101,1,2,1,7),_FsLldpMedLocMediaPolicyRowStatus_Type())
fsLldpMedLocMediaPolicyRowStatus.setMaxAccess(_a)
if mibBuilder.loadTexts:fsLldpMedLocMediaPolicyRowStatus.setStatus(_A)
_FsLldpMedLocLocationTable_Object=MibTable
fsLldpMedLocLocationTable=_FsLldpMedLocLocationTable_Object((1,3,6,1,4,1,29601,2,101,1,3))
if mibBuilder.loadTexts:fsLldpMedLocLocationTable.setStatus(_A)
_FsLldpMedLocLocationEntry_Object=MibTableRow
fsLldpMedLocLocationEntry=_FsLldpMedLocLocationEntry_Object((1,3,6,1,4,1,29601,2,101,1,3,1))
if mibBuilder.loadTexts:fsLldpMedLocLocationEntry.setStatus(_A)
_FsLldpMedLocLocationRowStatus_Type=RowStatus
_FsLldpMedLocLocationRowStatus_Object=MibTableColumn
fsLldpMedLocLocationRowStatus=_FsLldpMedLocLocationRowStatus_Object((1,3,6,1,4,1,29601,2,101,1,3,1,1),_FsLldpMedLocLocationRowStatus_Type())
fsLldpMedLocLocationRowStatus.setMaxAccess(_a)
if mibBuilder.loadTexts:fsLldpMedLocLocationRowStatus.setStatus(_A)
_FsLldpMedRemoteConfig_ObjectIdentity=ObjectIdentity
fsLldpMedRemoteConfig=_FsLldpMedRemoteConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,101,2))
_FsLldpXMedRemCapabilitiesTable_Object=MibTable
fsLldpXMedRemCapabilitiesTable=_FsLldpXMedRemCapabilitiesTable_Object((1,3,6,1,4,1,29601,2,101,2,1))
if mibBuilder.loadTexts:fsLldpXMedRemCapabilitiesTable.setStatus(_A)
_FsLldpXMedRemCapabilitiesEntry_Object=MibTableRow
fsLldpXMedRemCapabilitiesEntry=_FsLldpXMedRemCapabilitiesEntry_Object((1,3,6,1,4,1,29601,2,101,2,1,1))
fsLldpXMedRemCapabilitiesEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:fsLldpXMedRemCapabilitiesEntry.setStatus(_A)
_FsLldpXMedRemCapSupported_Type=LldpXMedCapabilities
_FsLldpXMedRemCapSupported_Object=MibTableColumn
fsLldpXMedRemCapSupported=_FsLldpXMedRemCapSupported_Object((1,3,6,1,4,1,29601,2,101,2,1,1,1),_FsLldpXMedRemCapSupported_Type())
fsLldpXMedRemCapSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemCapSupported.setStatus(_A)
_FsLldpXMedRemCapCurrent_Type=LldpXMedCapabilities
_FsLldpXMedRemCapCurrent_Object=MibTableColumn
fsLldpXMedRemCapCurrent=_FsLldpXMedRemCapCurrent_Object((1,3,6,1,4,1,29601,2,101,2,1,1,2),_FsLldpXMedRemCapCurrent_Type())
fsLldpXMedRemCapCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemCapCurrent.setStatus(_A)
_FsLldpXMedRemDeviceClass_Type=LldpXMedDeviceClass
_FsLldpXMedRemDeviceClass_Object=MibTableColumn
fsLldpXMedRemDeviceClass=_FsLldpXMedRemDeviceClass_Object((1,3,6,1,4,1,29601,2,101,2,1,1,3),_FsLldpXMedRemDeviceClass_Type())
fsLldpXMedRemDeviceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemDeviceClass.setStatus(_A)
_FsLldpXMedRemMediaPolicyTable_Object=MibTable
fsLldpXMedRemMediaPolicyTable=_FsLldpXMedRemMediaPolicyTable_Object((1,3,6,1,4,1,29601,2,101,2,2))
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyTable.setStatus(_A)
_FsLldpXMedRemMediaPolicyEntry_Object=MibTableRow
fsLldpXMedRemMediaPolicyEntry=_FsLldpXMedRemMediaPolicyEntry_Object((1,3,6,1,4,1,29601,2,101,2,2,1))
fsLldpXMedRemMediaPolicyEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_F,_b))
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyEntry.setStatus(_A)
_FsLldpXMedRemMediaPolicyAppType_Type=PolicyAppType
_FsLldpXMedRemMediaPolicyAppType_Object=MibTableColumn
fsLldpXMedRemMediaPolicyAppType=_FsLldpXMedRemMediaPolicyAppType_Object((1,3,6,1,4,1,29601,2,101,2,2,1,1),_FsLldpXMedRemMediaPolicyAppType_Type())
fsLldpXMedRemMediaPolicyAppType.setMaxAccess(_N)
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyAppType.setStatus(_A)
class _FsLldpXMedRemMediaPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_FsLldpXMedRemMediaPolicyVlanID_Type.__name__=_D
_FsLldpXMedRemMediaPolicyVlanID_Object=MibTableColumn
fsLldpXMedRemMediaPolicyVlanID=_FsLldpXMedRemMediaPolicyVlanID_Object((1,3,6,1,4,1,29601,2,101,2,2,1,2),_FsLldpXMedRemMediaPolicyVlanID_Type())
fsLldpXMedRemMediaPolicyVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyVlanID.setStatus(_A)
class _FsLldpXMedRemMediaPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsLldpXMedRemMediaPolicyPriority_Type.__name__=_D
_FsLldpXMedRemMediaPolicyPriority_Object=MibTableColumn
fsLldpXMedRemMediaPolicyPriority=_FsLldpXMedRemMediaPolicyPriority_Object((1,3,6,1,4,1,29601,2,101,2,2,1,3),_FsLldpXMedRemMediaPolicyPriority_Type())
fsLldpXMedRemMediaPolicyPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyPriority.setStatus(_A)
class _FsLldpXMedRemMediaPolicyDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FsLldpXMedRemMediaPolicyDscp_Type.__name__=_D
_FsLldpXMedRemMediaPolicyDscp_Object=MibTableColumn
fsLldpXMedRemMediaPolicyDscp=_FsLldpXMedRemMediaPolicyDscp_Object((1,3,6,1,4,1,29601,2,101,2,2,1,4),_FsLldpXMedRemMediaPolicyDscp_Type())
fsLldpXMedRemMediaPolicyDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyDscp.setStatus(_A)
_FsLldpXMedRemMediaPolicyUnknown_Type=TruthValue
_FsLldpXMedRemMediaPolicyUnknown_Object=MibTableColumn
fsLldpXMedRemMediaPolicyUnknown=_FsLldpXMedRemMediaPolicyUnknown_Object((1,3,6,1,4,1,29601,2,101,2,2,1,5),_FsLldpXMedRemMediaPolicyUnknown_Type())
fsLldpXMedRemMediaPolicyUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyUnknown.setStatus(_A)
_FsLldpXMedRemMediaPolicyTagged_Type=TruthValue
_FsLldpXMedRemMediaPolicyTagged_Object=MibTableColumn
fsLldpXMedRemMediaPolicyTagged=_FsLldpXMedRemMediaPolicyTagged_Object((1,3,6,1,4,1,29601,2,101,2,2,1,6),_FsLldpXMedRemMediaPolicyTagged_Type())
fsLldpXMedRemMediaPolicyTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemMediaPolicyTagged.setStatus(_A)
_FsLldpXMedRemInventoryTable_Object=MibTable
fsLldpXMedRemInventoryTable=_FsLldpXMedRemInventoryTable_Object((1,3,6,1,4,1,29601,2,101,2,3))
if mibBuilder.loadTexts:fsLldpXMedRemInventoryTable.setStatus(_A)
_FsLldpXMedRemInventoryEntry_Object=MibTableRow
fsLldpXMedRemInventoryEntry=_FsLldpXMedRemInventoryEntry_Object((1,3,6,1,4,1,29601,2,101,2,3,1))
fsLldpXMedRemInventoryEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:fsLldpXMedRemInventoryEntry.setStatus(_A)
class _FsLldpXMedRemHardwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemHardwareRev_Type.__name__=_E
_FsLldpXMedRemHardwareRev_Object=MibTableColumn
fsLldpXMedRemHardwareRev=_FsLldpXMedRemHardwareRev_Object((1,3,6,1,4,1,29601,2,101,2,3,1,1),_FsLldpXMedRemHardwareRev_Type())
fsLldpXMedRemHardwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemHardwareRev.setStatus(_A)
class _FsLldpXMedRemFirmwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemFirmwareRev_Type.__name__=_E
_FsLldpXMedRemFirmwareRev_Object=MibTableColumn
fsLldpXMedRemFirmwareRev=_FsLldpXMedRemFirmwareRev_Object((1,3,6,1,4,1,29601,2,101,2,3,1,2),_FsLldpXMedRemFirmwareRev_Type())
fsLldpXMedRemFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemFirmwareRev.setStatus(_A)
class _FsLldpXMedRemSoftwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemSoftwareRev_Type.__name__=_E
_FsLldpXMedRemSoftwareRev_Object=MibTableColumn
fsLldpXMedRemSoftwareRev=_FsLldpXMedRemSoftwareRev_Object((1,3,6,1,4,1,29601,2,101,2,3,1,3),_FsLldpXMedRemSoftwareRev_Type())
fsLldpXMedRemSoftwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemSoftwareRev.setStatus(_A)
class _FsLldpXMedRemSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemSerialNum_Type.__name__=_E
_FsLldpXMedRemSerialNum_Object=MibTableColumn
fsLldpXMedRemSerialNum=_FsLldpXMedRemSerialNum_Object((1,3,6,1,4,1,29601,2,101,2,3,1,4),_FsLldpXMedRemSerialNum_Type())
fsLldpXMedRemSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemSerialNum.setStatus(_A)
class _FsLldpXMedRemMfgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemMfgName_Type.__name__=_E
_FsLldpXMedRemMfgName_Object=MibTableColumn
fsLldpXMedRemMfgName=_FsLldpXMedRemMfgName_Object((1,3,6,1,4,1,29601,2,101,2,3,1,5),_FsLldpXMedRemMfgName_Type())
fsLldpXMedRemMfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemMfgName.setStatus(_A)
class _FsLldpXMedRemModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemModelName_Type.__name__=_E
_FsLldpXMedRemModelName_Object=MibTableColumn
fsLldpXMedRemModelName=_FsLldpXMedRemModelName_Object((1,3,6,1,4,1,29601,2,101,2,3,1,6),_FsLldpXMedRemModelName_Type())
fsLldpXMedRemModelName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemModelName.setStatus(_A)
class _FsLldpXMedRemAssetID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsLldpXMedRemAssetID_Type.__name__=_E
_FsLldpXMedRemAssetID_Object=MibTableColumn
fsLldpXMedRemAssetID=_FsLldpXMedRemAssetID_Object((1,3,6,1,4,1,29601,2,101,2,3,1,7),_FsLldpXMedRemAssetID_Type())
fsLldpXMedRemAssetID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemAssetID.setStatus(_A)
_FsLldpXMedRemLocationTable_Object=MibTable
fsLldpXMedRemLocationTable=_FsLldpXMedRemLocationTable_Object((1,3,6,1,4,1,29601,2,101,2,4))
if mibBuilder.loadTexts:fsLldpXMedRemLocationTable.setStatus(_A)
_FsLldpXMedRemLocationEntry_Object=MibTableRow
fsLldpXMedRemLocationEntry=_FsLldpXMedRemLocationEntry_Object((1,3,6,1,4,1,29601,2,101,2,4,1))
fsLldpXMedRemLocationEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H),(0,_S,_T))
if mibBuilder.loadTexts:fsLldpXMedRemLocationEntry.setStatus(_A)
class _FsLldpXMedRemLocationInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_FsLldpXMedRemLocationInfo_Type.__name__=_R
_FsLldpXMedRemLocationInfo_Object=MibTableColumn
fsLldpXMedRemLocationInfo=_FsLldpXMedRemLocationInfo_Object((1,3,6,1,4,1,29601,2,101,2,4,1,1),_FsLldpXMedRemLocationInfo_Type())
fsLldpXMedRemLocationInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemLocationInfo.setStatus(_A)
_FsLldpXMedRemXPoEPDTable_Object=MibTable
fsLldpXMedRemXPoEPDTable=_FsLldpXMedRemXPoEPDTable_Object((1,3,6,1,4,1,29601,2,101,2,5))
if mibBuilder.loadTexts:fsLldpXMedRemXPoEPDTable.setStatus(_A)
_FsLldpXMedRemXPoEPDEntry_Object=MibTableRow
fsLldpXMedRemXPoEPDEntry=_FsLldpXMedRemXPoEPDEntry_Object((1,3,6,1,4,1,29601,2,101,2,5,1))
fsLldpXMedRemXPoEPDEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:fsLldpXMedRemXPoEPDEntry.setStatus(_A)
class _FsLldpXMedRemXPoEDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('pseDevice',2),('pdDevice',3),('none',4)))
_FsLldpXMedRemXPoEDeviceType_Type.__name__=_D
_FsLldpXMedRemXPoEDeviceType_Object=MibTableColumn
fsLldpXMedRemXPoEDeviceType=_FsLldpXMedRemXPoEDeviceType_Object((1,3,6,1,4,1,29601,2,101,2,5,1,1),_FsLldpXMedRemXPoEDeviceType_Type())
fsLldpXMedRemXPoEDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemXPoEDeviceType.setStatus(_A)
class _FsLldpXMedRemXPoEPDPowerReq_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_FsLldpXMedRemXPoEPDPowerReq_Type.__name__=_X
_FsLldpXMedRemXPoEPDPowerReq_Object=MibTableColumn
fsLldpXMedRemXPoEPDPowerReq=_FsLldpXMedRemXPoEPDPowerReq_Object((1,3,6,1,4,1,29601,2,101,2,5,1,2),_FsLldpXMedRemXPoEPDPowerReq_Type())
fsLldpXMedRemXPoEPDPowerReq.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemXPoEPDPowerReq.setStatus(_A)
if mibBuilder.loadTexts:fsLldpXMedRemXPoEPDPowerReq.setUnits('tenth of watt')
class _FsLldpXMedRemXPoEPDPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('fromPSE',2),('local',3),('localAndPSE',4)))
_FsLldpXMedRemXPoEPDPowerSource_Type.__name__=_D
_FsLldpXMedRemXPoEPDPowerSource_Object=MibTableColumn
fsLldpXMedRemXPoEPDPowerSource=_FsLldpXMedRemXPoEPDPowerSource_Object((1,3,6,1,4,1,29601,2,101,2,5,1,3),_FsLldpXMedRemXPoEPDPowerSource_Type())
fsLldpXMedRemXPoEPDPowerSource.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemXPoEPDPowerSource.setStatus(_A)
class _FsLldpXMedRemXPoEPDPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('critical',2),('high',3),('low',4)))
_FsLldpXMedRemXPoEPDPowerPriority_Type.__name__=_D
_FsLldpXMedRemXPoEPDPowerPriority_Object=MibTableColumn
fsLldpXMedRemXPoEPDPowerPriority=_FsLldpXMedRemXPoEPDPowerPriority_Object((1,3,6,1,4,1,29601,2,101,2,5,1,4),_FsLldpXMedRemXPoEPDPowerPriority_Type())
fsLldpXMedRemXPoEPDPowerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpXMedRemXPoEPDPowerPriority.setStatus(_A)
_FsLldpMedStatistics_ObjectIdentity=ObjectIdentity
fsLldpMedStatistics=_FsLldpMedStatistics_ObjectIdentity((1,3,6,1,4,1,29601,2,101,3))
_FsLldpMedStatsTable_Object=MibTable
fsLldpMedStatsTable=_FsLldpMedStatsTable_Object((1,3,6,1,4,1,29601,2,101,3,1))
if mibBuilder.loadTexts:fsLldpMedStatsTable.setStatus(_A)
_FsLldpMedStatsEntry_Object=MibTableRow
fsLldpMedStatsEntry=_FsLldpMedStatsEntry_Object((1,3,6,1,4,1,29601,2,101,3,1,1))
fsLldpMedStatsEntry.setIndexNames((0,_F,_c),(0,_F,_d))
if mibBuilder.loadTexts:fsLldpMedStatsEntry.setStatus(_A)
_FsLldpMedStatsIfIndex_Type=InterfaceIndex
_FsLldpMedStatsIfIndex_Object=MibTableColumn
fsLldpMedStatsIfIndex=_FsLldpMedStatsIfIndex_Object((1,3,6,1,4,1,29601,2,101,3,1,1,1),_FsLldpMedStatsIfIndex_Type())
fsLldpMedStatsIfIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:fsLldpMedStatsIfIndex.setStatus(_A)
_FsLldpMedStatsDestMACAddress_Type=LldpV2DestAddressTableIndex
_FsLldpMedStatsDestMACAddress_Object=MibTableColumn
fsLldpMedStatsDestMACAddress=_FsLldpMedStatsDestMACAddress_Object((1,3,6,1,4,1,29601,2,101,3,1,1,2),_FsLldpMedStatsDestMACAddress_Type())
fsLldpMedStatsDestMACAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:fsLldpMedStatsDestMACAddress.setStatus(_A)
_FsLldpMedStatsTxFramesTotal_Type=Counter32
_FsLldpMedStatsTxFramesTotal_Object=MibTableColumn
fsLldpMedStatsTxFramesTotal=_FsLldpMedStatsTxFramesTotal_Object((1,3,6,1,4,1,29601,2,101,3,1,1,3),_FsLldpMedStatsTxFramesTotal_Type())
fsLldpMedStatsTxFramesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsTxFramesTotal.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsTxFramesTotal.setUnits(_Q)
_FsLldpMedStatsRxFramesTotal_Type=Counter32
_FsLldpMedStatsRxFramesTotal_Object=MibTableColumn
fsLldpMedStatsRxFramesTotal=_FsLldpMedStatsRxFramesTotal_Object((1,3,6,1,4,1,29601,2,101,3,1,1,4),_FsLldpMedStatsRxFramesTotal_Type())
fsLldpMedStatsRxFramesTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxFramesTotal.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxFramesTotal.setUnits(_Q)
_FsLldpMedStatsRxFramesDiscardedTotal_Type=Counter32
_FsLldpMedStatsRxFramesDiscardedTotal_Object=MibTableColumn
fsLldpMedStatsRxFramesDiscardedTotal=_FsLldpMedStatsRxFramesDiscardedTotal_Object((1,3,6,1,4,1,29601,2,101,3,1,1,5),_FsLldpMedStatsRxFramesDiscardedTotal_Type())
fsLldpMedStatsRxFramesDiscardedTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxFramesDiscardedTotal.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxFramesDiscardedTotal.setUnits(_Q)
_FsLldpMedStatsRxTLVsDiscardedTotal_Type=Counter32
_FsLldpMedStatsRxTLVsDiscardedTotal_Object=MibTableColumn
fsLldpMedStatsRxTLVsDiscardedTotal=_FsLldpMedStatsRxTLVsDiscardedTotal_Object((1,3,6,1,4,1,29601,2,101,3,1,1,6),_FsLldpMedStatsRxTLVsDiscardedTotal_Type())
fsLldpMedStatsRxTLVsDiscardedTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxTLVsDiscardedTotal.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxTLVsDiscardedTotal.setUnits(_M)
_FsLldpMedStatsRxCapTLVsDiscarded_Type=Counter32
_FsLldpMedStatsRxCapTLVsDiscarded_Object=MibTableColumn
fsLldpMedStatsRxCapTLVsDiscarded=_FsLldpMedStatsRxCapTLVsDiscarded_Object((1,3,6,1,4,1,29601,2,101,3,1,1,7),_FsLldpMedStatsRxCapTLVsDiscarded_Type())
fsLldpMedStatsRxCapTLVsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxCapTLVsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxCapTLVsDiscarded.setUnits(_M)
_FsLldpMedStatsRxPolicyTLVsDiscarded_Type=Counter32
_FsLldpMedStatsRxPolicyTLVsDiscarded_Object=MibTableColumn
fsLldpMedStatsRxPolicyTLVsDiscarded=_FsLldpMedStatsRxPolicyTLVsDiscarded_Object((1,3,6,1,4,1,29601,2,101,3,1,1,8),_FsLldpMedStatsRxPolicyTLVsDiscarded_Type())
fsLldpMedStatsRxPolicyTLVsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxPolicyTLVsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxPolicyTLVsDiscarded.setUnits(_M)
_FsLldpMedStatsRxInventoryTLVsDiscarded_Type=Counter32
_FsLldpMedStatsRxInventoryTLVsDiscarded_Object=MibTableColumn
fsLldpMedStatsRxInventoryTLVsDiscarded=_FsLldpMedStatsRxInventoryTLVsDiscarded_Object((1,3,6,1,4,1,29601,2,101,3,1,1,9),_FsLldpMedStatsRxInventoryTLVsDiscarded_Type())
fsLldpMedStatsRxInventoryTLVsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxInventoryTLVsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxInventoryTLVsDiscarded.setUnits(_M)
_FsLldpMedStatsRxLocationTLVsDiscarded_Type=Counter32
_FsLldpMedStatsRxLocationTLVsDiscarded_Object=MibTableColumn
fsLldpMedStatsRxLocationTLVsDiscarded=_FsLldpMedStatsRxLocationTLVsDiscarded_Object((1,3,6,1,4,1,29601,2,101,3,1,1,10),_FsLldpMedStatsRxLocationTLVsDiscarded_Type())
fsLldpMedStatsRxLocationTLVsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxLocationTLVsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxLocationTLVsDiscarded.setUnits(_M)
_FsLldpMedStatsRxExPowerMDITLVsDiscarded_Type=Counter32
_FsLldpMedStatsRxExPowerMDITLVsDiscarded_Object=MibTableColumn
fsLldpMedStatsRxExPowerMDITLVsDiscarded=_FsLldpMedStatsRxExPowerMDITLVsDiscarded_Object((1,3,6,1,4,1,29601,2,101,3,1,1,11),_FsLldpMedStatsRxExPowerMDITLVsDiscarded_Type())
fsLldpMedStatsRxExPowerMDITLVsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxExPowerMDITLVsDiscarded.setStatus(_A)
if mibBuilder.loadTexts:fsLldpMedStatsRxExPowerMDITLVsDiscarded.setUnits(_M)
class _FsLldpMedStatsRxCapTLVsDiscardedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsLldpMedStatsRxCapTLVsDiscardedReason_Type.__name__=_L
_FsLldpMedStatsRxCapTLVsDiscardedReason_Object=MibTableColumn
fsLldpMedStatsRxCapTLVsDiscardedReason=_FsLldpMedStatsRxCapTLVsDiscardedReason_Object((1,3,6,1,4,1,29601,2,101,3,1,1,12),_FsLldpMedStatsRxCapTLVsDiscardedReason_Type())
fsLldpMedStatsRxCapTLVsDiscardedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxCapTLVsDiscardedReason.setStatus(_A)
class _FsLldpMedStatsRxPolicyDiscardedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsLldpMedStatsRxPolicyDiscardedReason_Type.__name__=_L
_FsLldpMedStatsRxPolicyDiscardedReason_Object=MibTableColumn
fsLldpMedStatsRxPolicyDiscardedReason=_FsLldpMedStatsRxPolicyDiscardedReason_Object((1,3,6,1,4,1,29601,2,101,3,1,1,13),_FsLldpMedStatsRxPolicyDiscardedReason_Type())
fsLldpMedStatsRxPolicyDiscardedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxPolicyDiscardedReason.setStatus(_A)
class _FsLldpMedStatsRxInventoryDiscardedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsLldpMedStatsRxInventoryDiscardedReason_Type.__name__=_L
_FsLldpMedStatsRxInventoryDiscardedReason_Object=MibTableColumn
fsLldpMedStatsRxInventoryDiscardedReason=_FsLldpMedStatsRxInventoryDiscardedReason_Object((1,3,6,1,4,1,29601,2,101,3,1,1,14),_FsLldpMedStatsRxInventoryDiscardedReason_Type())
fsLldpMedStatsRxInventoryDiscardedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxInventoryDiscardedReason.setStatus(_A)
class _FsLldpMedStatsRxLocationDiscardedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsLldpMedStatsRxLocationDiscardedReason_Type.__name__=_L
_FsLldpMedStatsRxLocationDiscardedReason_Object=MibTableColumn
fsLldpMedStatsRxLocationDiscardedReason=_FsLldpMedStatsRxLocationDiscardedReason_Object((1,3,6,1,4,1,29601,2,101,3,1,1,15),_FsLldpMedStatsRxLocationDiscardedReason_Type())
fsLldpMedStatsRxLocationDiscardedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxLocationDiscardedReason.setStatus(_A)
class _FsLldpMedStatsRxExPowerDiscardedReason_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FsLldpMedStatsRxExPowerDiscardedReason_Type.__name__=_L
_FsLldpMedStatsRxExPowerDiscardedReason_Object=MibTableColumn
fsLldpMedStatsRxExPowerDiscardedReason=_FsLldpMedStatsRxExPowerDiscardedReason_Object((1,3,6,1,4,1,29601,2,101,3,1,1,16),_FsLldpMedStatsRxExPowerDiscardedReason_Type())
fsLldpMedStatsRxExPowerDiscardedReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsLldpMedStatsRxExPowerDiscardedReason.setStatus(_A)
class _FsLldpMedClearStats_Type(TruthValue):defaultValue=2
_FsLldpMedClearStats_Type.__name__=_Y
_FsLldpMedClearStats_Object=MibScalar
fsLldpMedClearStats=_FsLldpMedClearStats_Object((1,3,6,1,4,1,29601,2,101,3,2),_FsLldpMedClearStats_Type())
fsLldpMedClearStats.setMaxAccess(_G)
if mibBuilder.loadTexts:fsLldpMedClearStats.setStatus(_A)
_FsLldpMedNotification_ObjectIdentity=ObjectIdentity
fsLldpMedNotification=_FsLldpMedNotification_ObjectIdentity((1,3,6,1,4,1,29601,2,101,4))
_FsLldpMedTraps_ObjectIdentity=ObjectIdentity
fsLldpMedTraps=_FsLldpMedTraps_ObjectIdentity((1,3,6,1,4,1,29601,2,101,4,0))
_FsLldpMedNotifyObjects_ObjectIdentity=ObjectIdentity
fsLldpMedNotifyObjects=_FsLldpMedNotifyObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,101,5))
_FsLldpMedTrapObjects_ObjectIdentity=ObjectIdentity
fsLldpMedTrapObjects=_FsLldpMedTrapObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,101,5,1))
_FsLldpXMedMediaPolicyAppType_Type=PolicyAppType
_FsLldpXMedMediaPolicyAppType_Object=MibScalar
fsLldpXMedMediaPolicyAppType=_FsLldpXMedMediaPolicyAppType_Object((1,3,6,1,4,1,29601,2,101,5,1,1),_FsLldpXMedMediaPolicyAppType_Type())
fsLldpXMedMediaPolicyAppType.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:fsLldpXMedMediaPolicyAppType.setStatus(_A)
lldpV2PortConfigEntry.registerAugmentions((_F,_e))
fsLldpMedPortConfigEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpXMedLocLocationEntry.registerAugmentions((_F,_f))
fsLldpMedLocLocationEntry.setIndexNames(*lldpXMedLocLocationEntry.getIndexNames())
fsLldpMedPolicyMismatch=NotificationType((1,3,6,1,4,1,29601,2,101,4,0,1))
fsLldpMedPolicyMismatch.setObjects(*((_O,_U),(_O,_V),(_F,_g)))
if mibBuilder.loadTexts:fsLldpMedPolicyMismatch.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fsLldpMed':fsLldpMed,'fsLldpMedLocalConfig':fsLldpMedLocalConfig,'fsLldpMedPortConfigTable':fsLldpMedPortConfigTable,_e:fsLldpMedPortConfigEntry,'fsLldpMedPortCapSupported':fsLldpMedPortCapSupported,'fsLldpMedPortConfigTLVsTxEnable':fsLldpMedPortConfigTLVsTxEnable,'fsLldpMedLocMediaPolicyTable':fsLldpMedLocMediaPolicyTable,'fsLldpMedLocMediaPolicyEntry':fsLldpMedLocMediaPolicyEntry,_Z:fsLldpMedLocMediaPolicyAppType,'fsLldpMedLocMediaPolicyVlanID':fsLldpMedLocMediaPolicyVlanID,'fsLldpMedLocMediaPolicyPriority':fsLldpMedLocMediaPolicyPriority,'fsLldpMedLocMediaPolicyDscp':fsLldpMedLocMediaPolicyDscp,'fsLldpMedLocMediaPolicyUnknown':fsLldpMedLocMediaPolicyUnknown,'fsLldpMedLocMediaPolicyTagged':fsLldpMedLocMediaPolicyTagged,'fsLldpMedLocMediaPolicyRowStatus':fsLldpMedLocMediaPolicyRowStatus,'fsLldpMedLocLocationTable':fsLldpMedLocLocationTable,_f:fsLldpMedLocLocationEntry,'fsLldpMedLocLocationRowStatus':fsLldpMedLocLocationRowStatus,'fsLldpMedRemoteConfig':fsLldpMedRemoteConfig,'fsLldpXMedRemCapabilitiesTable':fsLldpXMedRemCapabilitiesTable,'fsLldpXMedRemCapabilitiesEntry':fsLldpXMedRemCapabilitiesEntry,'fsLldpXMedRemCapSupported':fsLldpXMedRemCapSupported,'fsLldpXMedRemCapCurrent':fsLldpXMedRemCapCurrent,'fsLldpXMedRemDeviceClass':fsLldpXMedRemDeviceClass,'fsLldpXMedRemMediaPolicyTable':fsLldpXMedRemMediaPolicyTable,'fsLldpXMedRemMediaPolicyEntry':fsLldpXMedRemMediaPolicyEntry,_b:fsLldpXMedRemMediaPolicyAppType,'fsLldpXMedRemMediaPolicyVlanID':fsLldpXMedRemMediaPolicyVlanID,'fsLldpXMedRemMediaPolicyPriority':fsLldpXMedRemMediaPolicyPriority,'fsLldpXMedRemMediaPolicyDscp':fsLldpXMedRemMediaPolicyDscp,'fsLldpXMedRemMediaPolicyUnknown':fsLldpXMedRemMediaPolicyUnknown,'fsLldpXMedRemMediaPolicyTagged':fsLldpXMedRemMediaPolicyTagged,'fsLldpXMedRemInventoryTable':fsLldpXMedRemInventoryTable,'fsLldpXMedRemInventoryEntry':fsLldpXMedRemInventoryEntry,'fsLldpXMedRemHardwareRev':fsLldpXMedRemHardwareRev,'fsLldpXMedRemFirmwareRev':fsLldpXMedRemFirmwareRev,'fsLldpXMedRemSoftwareRev':fsLldpXMedRemSoftwareRev,'fsLldpXMedRemSerialNum':fsLldpXMedRemSerialNum,'fsLldpXMedRemMfgName':fsLldpXMedRemMfgName,'fsLldpXMedRemModelName':fsLldpXMedRemModelName,'fsLldpXMedRemAssetID':fsLldpXMedRemAssetID,'fsLldpXMedRemLocationTable':fsLldpXMedRemLocationTable,'fsLldpXMedRemLocationEntry':fsLldpXMedRemLocationEntry,'fsLldpXMedRemLocationInfo':fsLldpXMedRemLocationInfo,'fsLldpXMedRemXPoEPDTable':fsLldpXMedRemXPoEPDTable,'fsLldpXMedRemXPoEPDEntry':fsLldpXMedRemXPoEPDEntry,'fsLldpXMedRemXPoEDeviceType':fsLldpXMedRemXPoEDeviceType,'fsLldpXMedRemXPoEPDPowerReq':fsLldpXMedRemXPoEPDPowerReq,'fsLldpXMedRemXPoEPDPowerSource':fsLldpXMedRemXPoEPDPowerSource,'fsLldpXMedRemXPoEPDPowerPriority':fsLldpXMedRemXPoEPDPowerPriority,'fsLldpMedStatistics':fsLldpMedStatistics,'fsLldpMedStatsTable':fsLldpMedStatsTable,'fsLldpMedStatsEntry':fsLldpMedStatsEntry,_c:fsLldpMedStatsIfIndex,_d:fsLldpMedStatsDestMACAddress,'fsLldpMedStatsTxFramesTotal':fsLldpMedStatsTxFramesTotal,'fsLldpMedStatsRxFramesTotal':fsLldpMedStatsRxFramesTotal,'fsLldpMedStatsRxFramesDiscardedTotal':fsLldpMedStatsRxFramesDiscardedTotal,'fsLldpMedStatsRxTLVsDiscardedTotal':fsLldpMedStatsRxTLVsDiscardedTotal,'fsLldpMedStatsRxCapTLVsDiscarded':fsLldpMedStatsRxCapTLVsDiscarded,'fsLldpMedStatsRxPolicyTLVsDiscarded':fsLldpMedStatsRxPolicyTLVsDiscarded,'fsLldpMedStatsRxInventoryTLVsDiscarded':fsLldpMedStatsRxInventoryTLVsDiscarded,'fsLldpMedStatsRxLocationTLVsDiscarded':fsLldpMedStatsRxLocationTLVsDiscarded,'fsLldpMedStatsRxExPowerMDITLVsDiscarded':fsLldpMedStatsRxExPowerMDITLVsDiscarded,'fsLldpMedStatsRxCapTLVsDiscardedReason':fsLldpMedStatsRxCapTLVsDiscardedReason,'fsLldpMedStatsRxPolicyDiscardedReason':fsLldpMedStatsRxPolicyDiscardedReason,'fsLldpMedStatsRxInventoryDiscardedReason':fsLldpMedStatsRxInventoryDiscardedReason,'fsLldpMedStatsRxLocationDiscardedReason':fsLldpMedStatsRxLocationDiscardedReason,'fsLldpMedStatsRxExPowerDiscardedReason':fsLldpMedStatsRxExPowerDiscardedReason,'fsLldpMedClearStats':fsLldpMedClearStats,'fsLldpMedNotification':fsLldpMedNotification,'fsLldpMedTraps':fsLldpMedTraps,'fsLldpMedPolicyMismatch':fsLldpMedPolicyMismatch,'fsLldpMedNotifyObjects':fsLldpMedNotifyObjects,'fsLldpMedTrapObjects':fsLldpMedTrapObjects,_g:fsLldpXMedMediaPolicyAppType})