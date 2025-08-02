_Ad='lldpXMedOptPoEPDGroup'
_Ac='lldpXMedOptPoEPSEGroup'
_Ab='lldpXMedOptLocationGroup'
_Aa='lldpXMedOptInventoryGroup'
_AZ='lldpXMedOptMediaPolicyGroup'
_AY='lldpXMedNotificationsGroup'
_AX='lldpXMedRemSysGroup'
_AW='lldpXMedConfigGroup'
_AV='lldpXMedTopologyChangeDetected'
_AU='lldpXMedRemXPoEPDPowerPriority'
_AT='lldpXMedRemXPoEPDPowerSource'
_AS='lldpXMedRemXPoEPDPowerReq'
_AR='lldpXMedRemXPoEPSEPowerPriority'
_AQ='lldpXMedRemXPoEPSEPowerSource'
_AP='lldpXMedRemXPoEPSEPowerAv'
_AO='lldpXMedRemXPoEDeviceType'
_AN='lldpXMedRemLocationInfo'
_AM='lldpXMedRemAssetID'
_AL='lldpXMedRemModelName'
_AK='lldpXMedRemMfgName'
_AJ='lldpXMedRemSerialNum'
_AI='lldpXMedRemSoftwareRev'
_AH='lldpXMedRemFirmwareRev'
_AG='lldpXMedRemHardwareRev'
_AF='lldpXMedRemMediaPolicyTagged'
_AE='lldpXMedRemMediaPolicyUnknown'
_AD='lldpXMedRemMediaPolicyDscp'
_AC='lldpXMedRemMediaPolicyPriority'
_AB='lldpXMedRemMediaPolicyVlanID'
_AA='lldpXMedRemCapCurrent'
_A9='lldpXMedRemCapSupported'
_A8='lldpXMedLocXPoEPDPowerPriority'
_A7='lldpXMedLocXPoEPDPowerSource'
_A6='lldpXMedLocXPoEPDPowerReq'
_A5='lldpXMedLocXPoEPSEPowerSource'
_A4='lldpXMedLocXPoEPSEPortPDPriority'
_A3='lldpXMedLocXPoEPSEPortPowerAv'
_A2='lldpXMedLocLocationInfo'
_A1='lldpXMedLocAssetID'
_A0='lldpXMedLocModelName'
_z='lldpXMedLocMfgName'
_y='lldpXMedLocSerialNum'
_x='lldpXMedLocSoftwareRev'
_w='lldpXMedLocFirmwareRev'
_v='lldpXMedLocHardwareRev'
_u='lldpXMedLocMediaPolicyTagged'
_t='lldpXMedLocMediaPolicyUnknown'
_s='lldpXMedLocMediaPolicyDscp'
_r='lldpXMedLocMediaPolicyPriority'
_q='lldpXMedLocMediaPolicyVlanID'
_p='lldpXMedLocDeviceClass'
_o='lldpXMedLocXPoEDeviceType'
_n='lldpXMedFastStartRepeatCount'
_m='lldpXMedPortConfigNotifEnable'
_l='lldpXMedPortConfigTLVsTxEnable'
_k='lldpXMedPortCapSupported'
_j='lldpXMedPortConfigEntry'
_i='lldpXMedRemLocationSubtype'
_h='lldpXMedRemMediaPolicyAppType'
_g='localAndPSE'
_f='fromPSE'
_e='backup'
_d='primary'
_c='pdDevice'
_b='pseDevice'
_a='lldpXMedLocLocationSubtype'
_Z='lldpXMedLocMediaPolicyAppType'
_Y='LldpXMedCapabilities'
_X='TruthValue'
_W='Unsigned32'
_V='lldpRemChassisIdSubtype'
_U='lldpRemChassisId'
_T='lldpXMedRemDeviceClass'
_S='OctetString'
_R='low'
_Q='high'
_P='critical'
_O='tenth of watt'
_N='not-accessible'
_M='read-write'
_L='lldpLocPortNum'
_K='Gauge32'
_J='lldpRemTimeMark'
_I='lldpRemLocalPortNum'
_H='lldpRemIndex'
_G='unknown'
_F='Integer32'
_E='SnmpAdminString'
_D='LLDP-MIB'
_C='read-only'
_B='LLDP-EXT-MED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lldpExtensions,lldpLocPortNum,lldpPortConfigEntry,lldpRemChassisId,lldpRemChassisIdSubtype,lldpRemIndex,lldpRemLocalPortNum,lldpRemTimeMark=mibBuilder.importSymbols(_D,'lldpExtensions',_L,'lldpPortConfigEntry',_U,_V,_H,_I,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_K,_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_W,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_X)
lldpXMedMIB=ModuleIdentity((1,0,8802,1,1,2,1,5,4795))
if mibBuilder.loadTexts:lldpXMedMIB.setRevisions(('2005-07-28 00:00',))
class LldpXMedDeviceClass(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('notDefined',0),('endpointClass1',1),('endpointClass2',2),('endpointClass3',3),('networkConnectivity',4)))
class LldpXMedCapabilities(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('capabilities',0),('networkPolicy',1),('location',2),('extendedPSE',3),('extendedPD',4),('inventory',5)))
class LocationSubtype(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('coordinateBased',2),('civicAddress',3),('elin',4)))
class PolicyAppType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_G,0),('voice',1),('voiceSignaling',2),('guestVoice',3),('guestVoiceSignaling',4),('softPhoneVoice',5),('videoconferencing',6),('streamingVideo',7),('videoSignaling',8)))
class Dscp(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_LldpXMedNotifications_ObjectIdentity=ObjectIdentity
lldpXMedNotifications=_LldpXMedNotifications_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,0))
_LldpXMedObjects_ObjectIdentity=ObjectIdentity
lldpXMedObjects=_LldpXMedObjects_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,1))
_LldpXMedConfig_ObjectIdentity=ObjectIdentity
lldpXMedConfig=_LldpXMedConfig_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,1,1))
_LldpXMedLocDeviceClass_Type=LldpXMedDeviceClass
_LldpXMedLocDeviceClass_Object=MibScalar
lldpXMedLocDeviceClass=_LldpXMedLocDeviceClass_Object((1,0,8802,1,1,2,1,5,4795,1,1,1),_LldpXMedLocDeviceClass_Type())
lldpXMedLocDeviceClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocDeviceClass.setStatus(_A)
_LldpXMedPortConfigTable_Object=MibTable
lldpXMedPortConfigTable=_LldpXMedPortConfigTable_Object((1,0,8802,1,1,2,1,5,4795,1,1,2))
if mibBuilder.loadTexts:lldpXMedPortConfigTable.setStatus(_A)
_LldpXMedPortConfigEntry_Object=MibTableRow
lldpXMedPortConfigEntry=_LldpXMedPortConfigEntry_Object((1,0,8802,1,1,2,1,5,4795,1,1,2,1))
if mibBuilder.loadTexts:lldpXMedPortConfigEntry.setStatus(_A)
_LldpXMedPortCapSupported_Type=LldpXMedCapabilities
_LldpXMedPortCapSupported_Object=MibTableColumn
lldpXMedPortCapSupported=_LldpXMedPortCapSupported_Object((1,0,8802,1,1,2,1,5,4795,1,1,2,1,1),_LldpXMedPortCapSupported_Type())
lldpXMedPortCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedPortCapSupported.setStatus(_A)
class _LldpXMedPortConfigTLVsTxEnable_Type(LldpXMedCapabilities):defaultBinValue='0'
_LldpXMedPortConfigTLVsTxEnable_Type.__name__=_Y
_LldpXMedPortConfigTLVsTxEnable_Object=MibTableColumn
lldpXMedPortConfigTLVsTxEnable=_LldpXMedPortConfigTLVsTxEnable_Object((1,0,8802,1,1,2,1,5,4795,1,1,2,1,2),_LldpXMedPortConfigTLVsTxEnable_Type())
lldpXMedPortConfigTLVsTxEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXMedPortConfigTLVsTxEnable.setStatus(_A)
class _LldpXMedPortConfigNotifEnable_Type(TruthValue):defaultValue=2
_LldpXMedPortConfigNotifEnable_Type.__name__=_X
_LldpXMedPortConfigNotifEnable_Object=MibTableColumn
lldpXMedPortConfigNotifEnable=_LldpXMedPortConfigNotifEnable_Object((1,0,8802,1,1,2,1,5,4795,1,1,2,1,3),_LldpXMedPortConfigNotifEnable_Type())
lldpXMedPortConfigNotifEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXMedPortConfigNotifEnable.setStatus(_A)
class _LldpXMedFastStartRepeatCount_Type(Unsigned32):defaultValue=3;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_LldpXMedFastStartRepeatCount_Type.__name__=_W
_LldpXMedFastStartRepeatCount_Object=MibScalar
lldpXMedFastStartRepeatCount=_LldpXMedFastStartRepeatCount_Object((1,0,8802,1,1,2,1,5,4795,1,1,3),_LldpXMedFastStartRepeatCount_Type())
lldpXMedFastStartRepeatCount.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXMedFastStartRepeatCount.setStatus(_A)
_LldpXMedLocalData_ObjectIdentity=ObjectIdentity
lldpXMedLocalData=_LldpXMedLocalData_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,1,2))
_LldpXMedLocMediaPolicyTable_Object=MibTable
lldpXMedLocMediaPolicyTable=_LldpXMedLocMediaPolicyTable_Object((1,0,8802,1,1,2,1,5,4795,1,2,1))
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyTable.setStatus(_A)
_LldpXMedLocMediaPolicyEntry_Object=MibTableRow
lldpXMedLocMediaPolicyEntry=_LldpXMedLocMediaPolicyEntry_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1))
lldpXMedLocMediaPolicyEntry.setIndexNames((0,_D,_L),(0,_B,_Z))
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyEntry.setStatus(_A)
_LldpXMedLocMediaPolicyAppType_Type=PolicyAppType
_LldpXMedLocMediaPolicyAppType_Object=MibTableColumn
lldpXMedLocMediaPolicyAppType=_LldpXMedLocMediaPolicyAppType_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1,1),_LldpXMedLocMediaPolicyAppType_Type())
lldpXMedLocMediaPolicyAppType.setMaxAccess(_N)
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyAppType.setStatus(_A)
class _LldpXMedLocMediaPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_LldpXMedLocMediaPolicyVlanID_Type.__name__=_F
_LldpXMedLocMediaPolicyVlanID_Object=MibTableColumn
lldpXMedLocMediaPolicyVlanID=_LldpXMedLocMediaPolicyVlanID_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1,2),_LldpXMedLocMediaPolicyVlanID_Type())
lldpXMedLocMediaPolicyVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyVlanID.setStatus(_A)
class _LldpXMedLocMediaPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_LldpXMedLocMediaPolicyPriority_Type.__name__=_F
_LldpXMedLocMediaPolicyPriority_Object=MibTableColumn
lldpXMedLocMediaPolicyPriority=_LldpXMedLocMediaPolicyPriority_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1,3),_LldpXMedLocMediaPolicyPriority_Type())
lldpXMedLocMediaPolicyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyPriority.setStatus(_A)
_LldpXMedLocMediaPolicyDscp_Type=Dscp
_LldpXMedLocMediaPolicyDscp_Object=MibTableColumn
lldpXMedLocMediaPolicyDscp=_LldpXMedLocMediaPolicyDscp_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1,4),_LldpXMedLocMediaPolicyDscp_Type())
lldpXMedLocMediaPolicyDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyDscp.setStatus(_A)
_LldpXMedLocMediaPolicyUnknown_Type=TruthValue
_LldpXMedLocMediaPolicyUnknown_Object=MibTableColumn
lldpXMedLocMediaPolicyUnknown=_LldpXMedLocMediaPolicyUnknown_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1,5),_LldpXMedLocMediaPolicyUnknown_Type())
lldpXMedLocMediaPolicyUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyUnknown.setStatus(_A)
_LldpXMedLocMediaPolicyTagged_Type=TruthValue
_LldpXMedLocMediaPolicyTagged_Object=MibTableColumn
lldpXMedLocMediaPolicyTagged=_LldpXMedLocMediaPolicyTagged_Object((1,0,8802,1,1,2,1,5,4795,1,2,1,1,6),_LldpXMedLocMediaPolicyTagged_Type())
lldpXMedLocMediaPolicyTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocMediaPolicyTagged.setStatus(_A)
class _LldpXMedLocHardwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocHardwareRev_Type.__name__=_E
_LldpXMedLocHardwareRev_Object=MibScalar
lldpXMedLocHardwareRev=_LldpXMedLocHardwareRev_Object((1,0,8802,1,1,2,1,5,4795,1,2,2),_LldpXMedLocHardwareRev_Type())
lldpXMedLocHardwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocHardwareRev.setStatus(_A)
class _LldpXMedLocFirmwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocFirmwareRev_Type.__name__=_E
_LldpXMedLocFirmwareRev_Object=MibScalar
lldpXMedLocFirmwareRev=_LldpXMedLocFirmwareRev_Object((1,0,8802,1,1,2,1,5,4795,1,2,3),_LldpXMedLocFirmwareRev_Type())
lldpXMedLocFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocFirmwareRev.setStatus(_A)
class _LldpXMedLocSoftwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocSoftwareRev_Type.__name__=_E
_LldpXMedLocSoftwareRev_Object=MibScalar
lldpXMedLocSoftwareRev=_LldpXMedLocSoftwareRev_Object((1,0,8802,1,1,2,1,5,4795,1,2,4),_LldpXMedLocSoftwareRev_Type())
lldpXMedLocSoftwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocSoftwareRev.setStatus(_A)
class _LldpXMedLocSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocSerialNum_Type.__name__=_E
_LldpXMedLocSerialNum_Object=MibScalar
lldpXMedLocSerialNum=_LldpXMedLocSerialNum_Object((1,0,8802,1,1,2,1,5,4795,1,2,5),_LldpXMedLocSerialNum_Type())
lldpXMedLocSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocSerialNum.setStatus(_A)
class _LldpXMedLocMfgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocMfgName_Type.__name__=_E
_LldpXMedLocMfgName_Object=MibScalar
lldpXMedLocMfgName=_LldpXMedLocMfgName_Object((1,0,8802,1,1,2,1,5,4795,1,2,6),_LldpXMedLocMfgName_Type())
lldpXMedLocMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocMfgName.setStatus(_A)
class _LldpXMedLocModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocModelName_Type.__name__=_E
_LldpXMedLocModelName_Object=MibScalar
lldpXMedLocModelName=_LldpXMedLocModelName_Object((1,0,8802,1,1,2,1,5,4795,1,2,7),_LldpXMedLocModelName_Type())
lldpXMedLocModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocModelName.setStatus(_A)
class _LldpXMedLocAssetID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedLocAssetID_Type.__name__=_E
_LldpXMedLocAssetID_Object=MibScalar
lldpXMedLocAssetID=_LldpXMedLocAssetID_Object((1,0,8802,1,1,2,1,5,4795,1,2,8),_LldpXMedLocAssetID_Type())
lldpXMedLocAssetID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocAssetID.setStatus(_A)
_LldpXMedLocLocationTable_Object=MibTable
lldpXMedLocLocationTable=_LldpXMedLocLocationTable_Object((1,0,8802,1,1,2,1,5,4795,1,2,9))
if mibBuilder.loadTexts:lldpXMedLocLocationTable.setStatus(_A)
_LldpXMedLocLocationEntry_Object=MibTableRow
lldpXMedLocLocationEntry=_LldpXMedLocLocationEntry_Object((1,0,8802,1,1,2,1,5,4795,1,2,9,1))
lldpXMedLocLocationEntry.setIndexNames((0,_D,_L),(0,_B,_a))
if mibBuilder.loadTexts:lldpXMedLocLocationEntry.setStatus(_A)
_LldpXMedLocLocationSubtype_Type=LocationSubtype
_LldpXMedLocLocationSubtype_Object=MibTableColumn
lldpXMedLocLocationSubtype=_LldpXMedLocLocationSubtype_Object((1,0,8802,1,1,2,1,5,4795,1,2,9,1,1),_LldpXMedLocLocationSubtype_Type())
lldpXMedLocLocationSubtype.setMaxAccess(_N)
if mibBuilder.loadTexts:lldpXMedLocLocationSubtype.setStatus(_A)
class _LldpXMedLocLocationInfo_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpXMedLocLocationInfo_Type.__name__=_S
_LldpXMedLocLocationInfo_Object=MibTableColumn
lldpXMedLocLocationInfo=_LldpXMedLocLocationInfo_Object((1,0,8802,1,1,2,1,5,4795,1,2,9,1,2),_LldpXMedLocLocationInfo_Type())
lldpXMedLocLocationInfo.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXMedLocLocationInfo.setStatus(_A)
class _LldpXMedLocXPoEDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_b,2),(_c,3),('none',4)))
_LldpXMedLocXPoEDeviceType_Type.__name__=_F
_LldpXMedLocXPoEDeviceType_Object=MibScalar
lldpXMedLocXPoEDeviceType=_LldpXMedLocXPoEDeviceType_Object((1,0,8802,1,1,2,1,5,4795,1,2,10),_LldpXMedLocXPoEDeviceType_Type())
lldpXMedLocXPoEDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEDeviceType.setStatus(_A)
_LldpXMedLocXPoEPSEPortTable_Object=MibTable
lldpXMedLocXPoEPSEPortTable=_LldpXMedLocXPoEPSEPortTable_Object((1,0,8802,1,1,2,1,5,4795,1,2,11))
if mibBuilder.loadTexts:lldpXMedLocXPoEPSEPortTable.setStatus(_A)
_LldpXMedLocXPoEPSEPortEntry_Object=MibTableRow
lldpXMedLocXPoEPSEPortEntry=_LldpXMedLocXPoEPSEPortEntry_Object((1,0,8802,1,1,2,1,5,4795,1,2,11,1))
lldpXMedLocXPoEPSEPortEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:lldpXMedLocXPoEPSEPortEntry.setStatus(_A)
class _LldpXMedLocXPoEPSEPortPowerAv_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_LldpXMedLocXPoEPSEPortPowerAv_Type.__name__=_K
_LldpXMedLocXPoEPSEPortPowerAv_Object=MibTableColumn
lldpXMedLocXPoEPSEPortPowerAv=_LldpXMedLocXPoEPSEPortPowerAv_Object((1,0,8802,1,1,2,1,5,4795,1,2,11,1,1),_LldpXMedLocXPoEPSEPortPowerAv_Type())
lldpXMedLocXPoEPSEPortPowerAv.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEPSEPortPowerAv.setStatus(_A)
if mibBuilder.loadTexts:lldpXMedLocXPoEPSEPortPowerAv.setUnits(_O)
class _LldpXMedLocXPoEPSEPortPDPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4)))
_LldpXMedLocXPoEPSEPortPDPriority_Type.__name__=_F
_LldpXMedLocXPoEPSEPortPDPriority_Object=MibTableColumn
lldpXMedLocXPoEPSEPortPDPriority=_LldpXMedLocXPoEPSEPortPDPriority_Object((1,0,8802,1,1,2,1,5,4795,1,2,11,1,2),_LldpXMedLocXPoEPSEPortPDPriority_Type())
lldpXMedLocXPoEPSEPortPDPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEPSEPortPDPriority.setStatus(_A)
class _LldpXMedLocXPoEPSEPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_d,2),(_e,3)))
_LldpXMedLocXPoEPSEPowerSource_Type.__name__=_F
_LldpXMedLocXPoEPSEPowerSource_Object=MibScalar
lldpXMedLocXPoEPSEPowerSource=_LldpXMedLocXPoEPSEPowerSource_Object((1,0,8802,1,1,2,1,5,4795,1,2,12),_LldpXMedLocXPoEPSEPowerSource_Type())
lldpXMedLocXPoEPSEPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEPSEPowerSource.setStatus(_A)
class _LldpXMedLocXPoEPDPowerReq_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_LldpXMedLocXPoEPDPowerReq_Type.__name__=_K
_LldpXMedLocXPoEPDPowerReq_Object=MibScalar
lldpXMedLocXPoEPDPowerReq=_LldpXMedLocXPoEPDPowerReq_Object((1,0,8802,1,1,2,1,5,4795,1,2,13),_LldpXMedLocXPoEPDPowerReq_Type())
lldpXMedLocXPoEPDPowerReq.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEPDPowerReq.setStatus(_A)
if mibBuilder.loadTexts:lldpXMedLocXPoEPDPowerReq.setUnits(_O)
class _LldpXMedLocXPoEPDPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_f,2),('local',3),(_g,4)))
_LldpXMedLocXPoEPDPowerSource_Type.__name__=_F
_LldpXMedLocXPoEPDPowerSource_Object=MibScalar
lldpXMedLocXPoEPDPowerSource=_LldpXMedLocXPoEPDPowerSource_Object((1,0,8802,1,1,2,1,5,4795,1,2,14),_LldpXMedLocXPoEPDPowerSource_Type())
lldpXMedLocXPoEPDPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEPDPowerSource.setStatus(_A)
class _LldpXMedLocXPoEPDPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4)))
_LldpXMedLocXPoEPDPowerPriority_Type.__name__=_F
_LldpXMedLocXPoEPDPowerPriority_Object=MibScalar
lldpXMedLocXPoEPDPowerPriority=_LldpXMedLocXPoEPDPowerPriority_Object((1,0,8802,1,1,2,1,5,4795,1,2,15),_LldpXMedLocXPoEPDPowerPriority_Type())
lldpXMedLocXPoEPDPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedLocXPoEPDPowerPriority.setStatus(_A)
_LldpXMedRemoteData_ObjectIdentity=ObjectIdentity
lldpXMedRemoteData=_LldpXMedRemoteData_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,1,3))
_LldpXMedRemCapabilitiesTable_Object=MibTable
lldpXMedRemCapabilitiesTable=_LldpXMedRemCapabilitiesTable_Object((1,0,8802,1,1,2,1,5,4795,1,3,1))
if mibBuilder.loadTexts:lldpXMedRemCapabilitiesTable.setStatus(_A)
_LldpXMedRemCapabilitiesEntry_Object=MibTableRow
lldpXMedRemCapabilitiesEntry=_LldpXMedRemCapabilitiesEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,1,1))
lldpXMedRemCapabilitiesEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H))
if mibBuilder.loadTexts:lldpXMedRemCapabilitiesEntry.setStatus(_A)
_LldpXMedRemCapSupported_Type=LldpXMedCapabilities
_LldpXMedRemCapSupported_Object=MibTableColumn
lldpXMedRemCapSupported=_LldpXMedRemCapSupported_Object((1,0,8802,1,1,2,1,5,4795,1,3,1,1,1),_LldpXMedRemCapSupported_Type())
lldpXMedRemCapSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemCapSupported.setStatus(_A)
_LldpXMedRemCapCurrent_Type=LldpXMedCapabilities
_LldpXMedRemCapCurrent_Object=MibTableColumn
lldpXMedRemCapCurrent=_LldpXMedRemCapCurrent_Object((1,0,8802,1,1,2,1,5,4795,1,3,1,1,2),_LldpXMedRemCapCurrent_Type())
lldpXMedRemCapCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemCapCurrent.setStatus(_A)
_LldpXMedRemDeviceClass_Type=LldpXMedDeviceClass
_LldpXMedRemDeviceClass_Object=MibTableColumn
lldpXMedRemDeviceClass=_LldpXMedRemDeviceClass_Object((1,0,8802,1,1,2,1,5,4795,1,3,1,1,3),_LldpXMedRemDeviceClass_Type())
lldpXMedRemDeviceClass.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemDeviceClass.setStatus(_A)
_LldpXMedRemMediaPolicyTable_Object=MibTable
lldpXMedRemMediaPolicyTable=_LldpXMedRemMediaPolicyTable_Object((1,0,8802,1,1,2,1,5,4795,1,3,2))
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyTable.setStatus(_A)
_LldpXMedRemMediaPolicyEntry_Object=MibTableRow
lldpXMedRemMediaPolicyEntry=_LldpXMedRemMediaPolicyEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1))
lldpXMedRemMediaPolicyEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H),(0,_B,_h))
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyEntry.setStatus(_A)
_LldpXMedRemMediaPolicyAppType_Type=PolicyAppType
_LldpXMedRemMediaPolicyAppType_Object=MibTableColumn
lldpXMedRemMediaPolicyAppType=_LldpXMedRemMediaPolicyAppType_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1,1),_LldpXMedRemMediaPolicyAppType_Type())
lldpXMedRemMediaPolicyAppType.setMaxAccess(_N)
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyAppType.setStatus(_A)
class _LldpXMedRemMediaPolicyVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4094),ValueRangeConstraint(4095,4095))
_LldpXMedRemMediaPolicyVlanID_Type.__name__=_F
_LldpXMedRemMediaPolicyVlanID_Object=MibTableColumn
lldpXMedRemMediaPolicyVlanID=_LldpXMedRemMediaPolicyVlanID_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1,2),_LldpXMedRemMediaPolicyVlanID_Type())
lldpXMedRemMediaPolicyVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyVlanID.setStatus(_A)
class _LldpXMedRemMediaPolicyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_LldpXMedRemMediaPolicyPriority_Type.__name__=_F
_LldpXMedRemMediaPolicyPriority_Object=MibTableColumn
lldpXMedRemMediaPolicyPriority=_LldpXMedRemMediaPolicyPriority_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1,3),_LldpXMedRemMediaPolicyPriority_Type())
lldpXMedRemMediaPolicyPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyPriority.setStatus(_A)
_LldpXMedRemMediaPolicyDscp_Type=Dscp
_LldpXMedRemMediaPolicyDscp_Object=MibTableColumn
lldpXMedRemMediaPolicyDscp=_LldpXMedRemMediaPolicyDscp_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1,4),_LldpXMedRemMediaPolicyDscp_Type())
lldpXMedRemMediaPolicyDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyDscp.setStatus(_A)
_LldpXMedRemMediaPolicyUnknown_Type=TruthValue
_LldpXMedRemMediaPolicyUnknown_Object=MibTableColumn
lldpXMedRemMediaPolicyUnknown=_LldpXMedRemMediaPolicyUnknown_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1,5),_LldpXMedRemMediaPolicyUnknown_Type())
lldpXMedRemMediaPolicyUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyUnknown.setStatus(_A)
_LldpXMedRemMediaPolicyTagged_Type=TruthValue
_LldpXMedRemMediaPolicyTagged_Object=MibTableColumn
lldpXMedRemMediaPolicyTagged=_LldpXMedRemMediaPolicyTagged_Object((1,0,8802,1,1,2,1,5,4795,1,3,2,1,6),_LldpXMedRemMediaPolicyTagged_Type())
lldpXMedRemMediaPolicyTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemMediaPolicyTagged.setStatus(_A)
_LldpXMedRemInventoryTable_Object=MibTable
lldpXMedRemInventoryTable=_LldpXMedRemInventoryTable_Object((1,0,8802,1,1,2,1,5,4795,1,3,3))
if mibBuilder.loadTexts:lldpXMedRemInventoryTable.setStatus(_A)
_LldpXMedRemInventoryEntry_Object=MibTableRow
lldpXMedRemInventoryEntry=_LldpXMedRemInventoryEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1))
lldpXMedRemInventoryEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H))
if mibBuilder.loadTexts:lldpXMedRemInventoryEntry.setStatus(_A)
class _LldpXMedRemHardwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemHardwareRev_Type.__name__=_E
_LldpXMedRemHardwareRev_Object=MibTableColumn
lldpXMedRemHardwareRev=_LldpXMedRemHardwareRev_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,1),_LldpXMedRemHardwareRev_Type())
lldpXMedRemHardwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemHardwareRev.setStatus(_A)
class _LldpXMedRemFirmwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemFirmwareRev_Type.__name__=_E
_LldpXMedRemFirmwareRev_Object=MibTableColumn
lldpXMedRemFirmwareRev=_LldpXMedRemFirmwareRev_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,2),_LldpXMedRemFirmwareRev_Type())
lldpXMedRemFirmwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemFirmwareRev.setStatus(_A)
class _LldpXMedRemSoftwareRev_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemSoftwareRev_Type.__name__=_E
_LldpXMedRemSoftwareRev_Object=MibTableColumn
lldpXMedRemSoftwareRev=_LldpXMedRemSoftwareRev_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,3),_LldpXMedRemSoftwareRev_Type())
lldpXMedRemSoftwareRev.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemSoftwareRev.setStatus(_A)
class _LldpXMedRemSerialNum_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemSerialNum_Type.__name__=_E
_LldpXMedRemSerialNum_Object=MibTableColumn
lldpXMedRemSerialNum=_LldpXMedRemSerialNum_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,4),_LldpXMedRemSerialNum_Type())
lldpXMedRemSerialNum.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemSerialNum.setStatus(_A)
class _LldpXMedRemMfgName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemMfgName_Type.__name__=_E
_LldpXMedRemMfgName_Object=MibTableColumn
lldpXMedRemMfgName=_LldpXMedRemMfgName_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,5),_LldpXMedRemMfgName_Type())
lldpXMedRemMfgName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemMfgName.setStatus(_A)
class _LldpXMedRemModelName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemModelName_Type.__name__=_E
_LldpXMedRemModelName_Object=MibTableColumn
lldpXMedRemModelName=_LldpXMedRemModelName_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,6),_LldpXMedRemModelName_Type())
lldpXMedRemModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemModelName.setStatus(_A)
class _LldpXMedRemAssetID_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LldpXMedRemAssetID_Type.__name__=_E
_LldpXMedRemAssetID_Object=MibTableColumn
lldpXMedRemAssetID=_LldpXMedRemAssetID_Object((1,0,8802,1,1,2,1,5,4795,1,3,3,1,7),_LldpXMedRemAssetID_Type())
lldpXMedRemAssetID.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemAssetID.setStatus(_A)
_LldpXMedRemLocationTable_Object=MibTable
lldpXMedRemLocationTable=_LldpXMedRemLocationTable_Object((1,0,8802,1,1,2,1,5,4795,1,3,4))
if mibBuilder.loadTexts:lldpXMedRemLocationTable.setStatus(_A)
_LldpXMedRemLocationEntry_Object=MibTableRow
lldpXMedRemLocationEntry=_LldpXMedRemLocationEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,4,1))
lldpXMedRemLocationEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H),(0,_B,_i))
if mibBuilder.loadTexts:lldpXMedRemLocationEntry.setStatus(_A)
_LldpXMedRemLocationSubtype_Type=LocationSubtype
_LldpXMedRemLocationSubtype_Object=MibTableColumn
lldpXMedRemLocationSubtype=_LldpXMedRemLocationSubtype_Object((1,0,8802,1,1,2,1,5,4795,1,3,4,1,1),_LldpXMedRemLocationSubtype_Type())
lldpXMedRemLocationSubtype.setMaxAccess(_N)
if mibBuilder.loadTexts:lldpXMedRemLocationSubtype.setStatus(_A)
class _LldpXMedRemLocationInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_LldpXMedRemLocationInfo_Type.__name__=_S
_LldpXMedRemLocationInfo_Object=MibTableColumn
lldpXMedRemLocationInfo=_LldpXMedRemLocationInfo_Object((1,0,8802,1,1,2,1,5,4795,1,3,4,1,2),_LldpXMedRemLocationInfo_Type())
lldpXMedRemLocationInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemLocationInfo.setStatus(_A)
_LldpXMedRemXPoETable_Object=MibTable
lldpXMedRemXPoETable=_LldpXMedRemXPoETable_Object((1,0,8802,1,1,2,1,5,4795,1,3,5))
if mibBuilder.loadTexts:lldpXMedRemXPoETable.setStatus(_A)
_LldpXMedRemXPoEEntry_Object=MibTableRow
lldpXMedRemXPoEEntry=_LldpXMedRemXPoEEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,5,1))
lldpXMedRemXPoEEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H))
if mibBuilder.loadTexts:lldpXMedRemXPoEEntry.setStatus(_A)
class _LldpXMedRemXPoEDeviceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_b,2),(_c,3),('none',4)))
_LldpXMedRemXPoEDeviceType_Type.__name__=_F
_LldpXMedRemXPoEDeviceType_Object=MibTableColumn
lldpXMedRemXPoEDeviceType=_LldpXMedRemXPoEDeviceType_Object((1,0,8802,1,1,2,1,5,4795,1,3,5,1,1),_LldpXMedRemXPoEDeviceType_Type())
lldpXMedRemXPoEDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEDeviceType.setStatus(_A)
_LldpXMedRemXPoEPSETable_Object=MibTable
lldpXMedRemXPoEPSETable=_LldpXMedRemXPoEPSETable_Object((1,0,8802,1,1,2,1,5,4795,1,3,6))
if mibBuilder.loadTexts:lldpXMedRemXPoEPSETable.setStatus(_A)
_LldpXMedRemXPoEPSEEntry_Object=MibTableRow
lldpXMedRemXPoEPSEEntry=_LldpXMedRemXPoEPSEEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,6,1))
lldpXMedRemXPoEPSEEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H))
if mibBuilder.loadTexts:lldpXMedRemXPoEPSEEntry.setStatus(_A)
class _LldpXMedRemXPoEPSEPowerAv_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_LldpXMedRemXPoEPSEPowerAv_Type.__name__=_K
_LldpXMedRemXPoEPSEPowerAv_Object=MibTableColumn
lldpXMedRemXPoEPSEPowerAv=_LldpXMedRemXPoEPSEPowerAv_Object((1,0,8802,1,1,2,1,5,4795,1,3,6,1,1),_LldpXMedRemXPoEPSEPowerAv_Type())
lldpXMedRemXPoEPSEPowerAv.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEPSEPowerAv.setStatus(_A)
if mibBuilder.loadTexts:lldpXMedRemXPoEPSEPowerAv.setUnits(_O)
class _LldpXMedRemXPoEPSEPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_d,2),(_e,3)))
_LldpXMedRemXPoEPSEPowerSource_Type.__name__=_F
_LldpXMedRemXPoEPSEPowerSource_Object=MibTableColumn
lldpXMedRemXPoEPSEPowerSource=_LldpXMedRemXPoEPSEPowerSource_Object((1,0,8802,1,1,2,1,5,4795,1,3,6,1,2),_LldpXMedRemXPoEPSEPowerSource_Type())
lldpXMedRemXPoEPSEPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEPSEPowerSource.setStatus(_A)
class _LldpXMedRemXPoEPSEPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4)))
_LldpXMedRemXPoEPSEPowerPriority_Type.__name__=_F
_LldpXMedRemXPoEPSEPowerPriority_Object=MibTableColumn
lldpXMedRemXPoEPSEPowerPriority=_LldpXMedRemXPoEPSEPowerPriority_Object((1,0,8802,1,1,2,1,5,4795,1,3,6,1,3),_LldpXMedRemXPoEPSEPowerPriority_Type())
lldpXMedRemXPoEPSEPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEPSEPowerPriority.setStatus(_A)
_LldpXMedRemXPoEPDTable_Object=MibTable
lldpXMedRemXPoEPDTable=_LldpXMedRemXPoEPDTable_Object((1,0,8802,1,1,2,1,5,4795,1,3,7))
if mibBuilder.loadTexts:lldpXMedRemXPoEPDTable.setStatus(_A)
_LldpXMedRemXPoEPDEntry_Object=MibTableRow
lldpXMedRemXPoEPDEntry=_LldpXMedRemXPoEPDEntry_Object((1,0,8802,1,1,2,1,5,4795,1,3,7,1))
lldpXMedRemXPoEPDEntry.setIndexNames((0,_D,_J),(0,_D,_I),(0,_D,_H))
if mibBuilder.loadTexts:lldpXMedRemXPoEPDEntry.setStatus(_A)
class _LldpXMedRemXPoEPDPowerReq_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_LldpXMedRemXPoEPDPowerReq_Type.__name__=_K
_LldpXMedRemXPoEPDPowerReq_Object=MibTableColumn
lldpXMedRemXPoEPDPowerReq=_LldpXMedRemXPoEPDPowerReq_Object((1,0,8802,1,1,2,1,5,4795,1,3,7,1,1),_LldpXMedRemXPoEPDPowerReq_Type())
lldpXMedRemXPoEPDPowerReq.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEPDPowerReq.setStatus(_A)
if mibBuilder.loadTexts:lldpXMedRemXPoEPDPowerReq.setUnits(_O)
class _LldpXMedRemXPoEPDPowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_f,2),('local',3),(_g,4)))
_LldpXMedRemXPoEPDPowerSource_Type.__name__=_F
_LldpXMedRemXPoEPDPowerSource_Object=MibTableColumn
lldpXMedRemXPoEPDPowerSource=_LldpXMedRemXPoEPDPowerSource_Object((1,0,8802,1,1,2,1,5,4795,1,3,7,1,2),_LldpXMedRemXPoEPDPowerSource_Type())
lldpXMedRemXPoEPDPowerSource.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEPDPowerSource.setStatus(_A)
class _LldpXMedRemXPoEPDPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4)))
_LldpXMedRemXPoEPDPowerPriority_Type.__name__=_F
_LldpXMedRemXPoEPDPowerPriority_Object=MibTableColumn
lldpXMedRemXPoEPDPowerPriority=_LldpXMedRemXPoEPDPowerPriority_Object((1,0,8802,1,1,2,1,5,4795,1,3,7,1,3),_LldpXMedRemXPoEPDPowerPriority_Type())
lldpXMedRemXPoEPDPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:lldpXMedRemXPoEPDPowerPriority.setStatus(_A)
_LldpXMedConformance_ObjectIdentity=ObjectIdentity
lldpXMedConformance=_LldpXMedConformance_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,2))
_LldpXMedCompliances_ObjectIdentity=ObjectIdentity
lldpXMedCompliances=_LldpXMedCompliances_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,2,1))
_LldpXMedGroups_ObjectIdentity=ObjectIdentity
lldpXMedGroups=_LldpXMedGroups_ObjectIdentity((1,0,8802,1,1,2,1,5,4795,2,2))
lldpPortConfigEntry.registerAugmentions((_B,_j))
lldpXMedPortConfigEntry.setIndexNames(*lldpPortConfigEntry.getIndexNames())
lldpXMedConfigGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,1))
lldpXMedConfigGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:lldpXMedConfigGroup.setStatus(_A)
lldpXMedOptMediaPolicyGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,2))
lldpXMedOptMediaPolicyGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:lldpXMedOptMediaPolicyGroup.setStatus(_A)
lldpXMedOptInventoryGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,3))
lldpXMedOptInventoryGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:lldpXMedOptInventoryGroup.setStatus(_A)
lldpXMedOptLocationGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,4))
lldpXMedOptLocationGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:lldpXMedOptLocationGroup.setStatus(_A)
lldpXMedOptPoEPSEGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,5))
lldpXMedOptPoEPSEGroup.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:lldpXMedOptPoEPSEGroup.setStatus(_A)
lldpXMedOptPoEPDGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,6))
lldpXMedOptPoEPDGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:lldpXMedOptPoEPDGroup.setStatus(_A)
lldpXMedRemSysGroup=ObjectGroup((1,0,8802,1,1,2,1,5,4795,2,2,7))
lldpXMedRemSysGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_T),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU)))
if mibBuilder.loadTexts:lldpXMedRemSysGroup.setStatus(_A)
lldpXMedTopologyChangeDetected=NotificationType((1,0,8802,1,1,2,1,5,4795,0,1))
lldpXMedTopologyChangeDetected.setObjects(*((_D,_V),(_D,_U),(_B,_T)))
if mibBuilder.loadTexts:lldpXMedTopologyChangeDetected.setStatus(_A)
lldpXMedNotificationsGroup=NotificationGroup((1,0,8802,1,1,2,1,5,4795,2,2,8))
lldpXMedNotificationsGroup.setObjects((_B,_AV))
if mibBuilder.loadTexts:lldpXMedNotificationsGroup.setStatus(_A)
lldpXMedCompliance=ModuleCompliance((1,0,8802,1,1,2,1,5,4795,2,1,1))
lldpXMedCompliance.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:lldpXMedCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LldpXMedDeviceClass':LldpXMedDeviceClass,_Y:LldpXMedCapabilities,'LocationSubtype':LocationSubtype,'PolicyAppType':PolicyAppType,'Dscp':Dscp,'lldpXMedMIB':lldpXMedMIB,'lldpXMedNotifications':lldpXMedNotifications,_AV:lldpXMedTopologyChangeDetected,'lldpXMedObjects':lldpXMedObjects,'lldpXMedConfig':lldpXMedConfig,_p:lldpXMedLocDeviceClass,'lldpXMedPortConfigTable':lldpXMedPortConfigTable,_j:lldpXMedPortConfigEntry,_k:lldpXMedPortCapSupported,_l:lldpXMedPortConfigTLVsTxEnable,_m:lldpXMedPortConfigNotifEnable,_n:lldpXMedFastStartRepeatCount,'lldpXMedLocalData':lldpXMedLocalData,'lldpXMedLocMediaPolicyTable':lldpXMedLocMediaPolicyTable,'lldpXMedLocMediaPolicyEntry':lldpXMedLocMediaPolicyEntry,_Z:lldpXMedLocMediaPolicyAppType,_q:lldpXMedLocMediaPolicyVlanID,_r:lldpXMedLocMediaPolicyPriority,_s:lldpXMedLocMediaPolicyDscp,_t:lldpXMedLocMediaPolicyUnknown,_u:lldpXMedLocMediaPolicyTagged,_v:lldpXMedLocHardwareRev,_w:lldpXMedLocFirmwareRev,_x:lldpXMedLocSoftwareRev,_y:lldpXMedLocSerialNum,_z:lldpXMedLocMfgName,_A0:lldpXMedLocModelName,_A1:lldpXMedLocAssetID,'lldpXMedLocLocationTable':lldpXMedLocLocationTable,'lldpXMedLocLocationEntry':lldpXMedLocLocationEntry,_a:lldpXMedLocLocationSubtype,_A2:lldpXMedLocLocationInfo,_o:lldpXMedLocXPoEDeviceType,'lldpXMedLocXPoEPSEPortTable':lldpXMedLocXPoEPSEPortTable,'lldpXMedLocXPoEPSEPortEntry':lldpXMedLocXPoEPSEPortEntry,_A3:lldpXMedLocXPoEPSEPortPowerAv,_A4:lldpXMedLocXPoEPSEPortPDPriority,_A5:lldpXMedLocXPoEPSEPowerSource,_A6:lldpXMedLocXPoEPDPowerReq,_A7:lldpXMedLocXPoEPDPowerSource,_A8:lldpXMedLocXPoEPDPowerPriority,'lldpXMedRemoteData':lldpXMedRemoteData,'lldpXMedRemCapabilitiesTable':lldpXMedRemCapabilitiesTable,'lldpXMedRemCapabilitiesEntry':lldpXMedRemCapabilitiesEntry,_A9:lldpXMedRemCapSupported,_AA:lldpXMedRemCapCurrent,_T:lldpXMedRemDeviceClass,'lldpXMedRemMediaPolicyTable':lldpXMedRemMediaPolicyTable,'lldpXMedRemMediaPolicyEntry':lldpXMedRemMediaPolicyEntry,_h:lldpXMedRemMediaPolicyAppType,_AB:lldpXMedRemMediaPolicyVlanID,_AC:lldpXMedRemMediaPolicyPriority,_AD:lldpXMedRemMediaPolicyDscp,_AE:lldpXMedRemMediaPolicyUnknown,_AF:lldpXMedRemMediaPolicyTagged,'lldpXMedRemInventoryTable':lldpXMedRemInventoryTable,'lldpXMedRemInventoryEntry':lldpXMedRemInventoryEntry,_AG:lldpXMedRemHardwareRev,_AH:lldpXMedRemFirmwareRev,_AI:lldpXMedRemSoftwareRev,_AJ:lldpXMedRemSerialNum,_AK:lldpXMedRemMfgName,_AL:lldpXMedRemModelName,_AM:lldpXMedRemAssetID,'lldpXMedRemLocationTable':lldpXMedRemLocationTable,'lldpXMedRemLocationEntry':lldpXMedRemLocationEntry,_i:lldpXMedRemLocationSubtype,_AN:lldpXMedRemLocationInfo,'lldpXMedRemXPoETable':lldpXMedRemXPoETable,'lldpXMedRemXPoEEntry':lldpXMedRemXPoEEntry,_AO:lldpXMedRemXPoEDeviceType,'lldpXMedRemXPoEPSETable':lldpXMedRemXPoEPSETable,'lldpXMedRemXPoEPSEEntry':lldpXMedRemXPoEPSEEntry,_AP:lldpXMedRemXPoEPSEPowerAv,_AQ:lldpXMedRemXPoEPSEPowerSource,_AR:lldpXMedRemXPoEPSEPowerPriority,'lldpXMedRemXPoEPDTable':lldpXMedRemXPoEPDTable,'lldpXMedRemXPoEPDEntry':lldpXMedRemXPoEPDEntry,_AS:lldpXMedRemXPoEPDPowerReq,_AT:lldpXMedRemXPoEPDPowerSource,_AU:lldpXMedRemXPoEPDPowerPriority,'lldpXMedConformance':lldpXMedConformance,'lldpXMedCompliances':lldpXMedCompliances,'lldpXMedCompliance':lldpXMedCompliance,'lldpXMedGroups':lldpXMedGroups,_AW:lldpXMedConfigGroup,_AZ:lldpXMedOptMediaPolicyGroup,_Aa:lldpXMedOptInventoryGroup,_Ab:lldpXMedOptLocationGroup,_Ac:lldpXMedOptPoEPSEGroup,_Ad:lldpXMedOptPoEPDGroup,_AX:lldpXMedRemSysGroup,_AY:lldpXMedNotificationsGroup})