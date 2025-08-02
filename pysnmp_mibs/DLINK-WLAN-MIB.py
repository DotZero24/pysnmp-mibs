_F='OctetString'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dlkEnterpriseAP=ModuleIdentity((1,3,6,1,4,1,171,1))
_Dlink_ObjectIdentity=ObjectIdentity
dlink=_Dlink_ObjectIdentity((1,3,6,1,4,1,171))
_DlkEnterpriseAPsys_ObjectIdentity=ObjectIdentity
dlkEnterpriseAPsys=_DlkEnterpriseAPsys_ObjectIdentity((1,3,6,1,4,1,171,1,1))
class _EnterpriseAPSysConfigSave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('write',1))
_EnterpriseAPSysConfigSave_Type.__name__=_C
_EnterpriseAPSysConfigSave_Object=MibScalar
enterpriseAPSysConfigSave=_EnterpriseAPSysConfigSave_Object((1,3,6,1,4,1,171,1,1,1),_EnterpriseAPSysConfigSave_Type())
enterpriseAPSysConfigSave.setMaxAccess(_D)
if mibBuilder.loadTexts:enterpriseAPSysConfigSave.setStatus(_A)
class _EnterpriseAPSysReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reboot',1))
_EnterpriseAPSysReboot_Type.__name__=_C
_EnterpriseAPSysReboot_Object=MibScalar
enterpriseAPSysReboot=_EnterpriseAPSysReboot_Object((1,3,6,1,4,1,171,1,1,2),_EnterpriseAPSysReboot_Type())
enterpriseAPSysReboot.setMaxAccess(_D)
if mibBuilder.loadTexts:enterpriseAPSysReboot.setStatus(_A)
class _EnterpriseAPSysConfigApply_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('saveAndReboot',1))
_EnterpriseAPSysConfigApply_Type.__name__=_C
_EnterpriseAPSysConfigApply_Object=MibScalar
enterpriseAPSysConfigApply=_EnterpriseAPSysConfigApply_Object((1,3,6,1,4,1,171,1,1,3),_EnterpriseAPSysConfigApply_Type())
enterpriseAPSysConfigApply.setMaxAccess(_D)
if mibBuilder.loadTexts:enterpriseAPSysConfigApply.setStatus(_A)
_DlkEnterpriseAPlan_ObjectIdentity=ObjectIdentity
dlkEnterpriseAPlan=_DlkEnterpriseAPlan_ObjectIdentity((1,3,6,1,4,1,171,1,2))
_Dlk80211bPlusDot11_ObjectIdentity=ObjectIdentity
dlk80211bPlusDot11=_Dlk80211bPlusDot11_ObjectIdentity((1,3,6,1,4,1,171,1,3))
_Dot11smt_ObjectIdentity=ObjectIdentity
dot11smt=_Dot11smt_ObjectIdentity((1,3,6,1,4,1,171,1,3,1))
_Dot11StationConfigEntry_ObjectIdentity=ObjectIdentity
dot11StationConfigEntry=_Dot11StationConfigEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,1,1))
_Dot11StationID_Type=MacAddress
_Dot11StationID_Object=MibScalar
dot11StationID=_Dot11StationID_Object((1,3,6,1,4,1,171,1,3,1,1,1),_Dot11StationID_Type())
dot11StationID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11StationID.setStatus('deprecated')
_Dot11PrivacyOptionImplemented_Type=TruthValue
_Dot11PrivacyOptionImplemented_Object=MibScalar
dot11PrivacyOptionImplemented=_Dot11PrivacyOptionImplemented_Object((1,3,6,1,4,1,171,1,3,1,1,2),_Dot11PrivacyOptionImplemented_Type())
dot11PrivacyOptionImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11PrivacyOptionImplemented.setStatus(_A)
class _Dot11PowerManagementMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('powersave',2)))
_Dot11PowerManagementMode_Type.__name__=_C
_Dot11PowerManagementMode_Object=MibScalar
dot11PowerManagementMode=_Dot11PowerManagementMode_Object((1,3,6,1,4,1,171,1,3,1,1,3),_Dot11PowerManagementMode_Type())
dot11PowerManagementMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11PowerManagementMode.setStatus(_A)
class _Dot11DesiredSSID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11DesiredSSID_Type.__name__=_F
_Dot11DesiredSSID_Object=MibScalar
dot11DesiredSSID=_Dot11DesiredSSID_Object((1,3,6,1,4,1,171,1,3,1,1,4),_Dot11DesiredSSID_Type())
dot11DesiredSSID.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11DesiredSSID.setStatus(_A)
class _Dot11DesiredBSSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infrastructure',1),('independent',2),('any',3)))
_Dot11DesiredBSSType_Type.__name__=_C
_Dot11DesiredBSSType_Object=MibScalar
dot11DesiredBSSType=_Dot11DesiredBSSType_Object((1,3,6,1,4,1,171,1,3,1,1,5),_Dot11DesiredBSSType_Type())
dot11DesiredBSSType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DesiredBSSType.setStatus(_A)
class _Dot11OperationalRateSet_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,126))
_Dot11OperationalRateSet_Type.__name__=_F
_Dot11OperationalRateSet_Object=MibScalar
dot11OperationalRateSet=_Dot11OperationalRateSet_Object((1,3,6,1,4,1,171,1,3,1,1,6),_Dot11OperationalRateSet_Type())
dot11OperationalRateSet.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11OperationalRateSet.setStatus(_A)
class _Dot11BeaconPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_Dot11BeaconPeriod_Type.__name__=_C
_Dot11BeaconPeriod_Object=MibScalar
dot11BeaconPeriod=_Dot11BeaconPeriod_Object((1,3,6,1,4,1,171,1,3,1,1,7),_Dot11BeaconPeriod_Type())
dot11BeaconPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11BeaconPeriod.setStatus(_A)
class _Dot11DTIMPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11DTIMPeriod_Type.__name__=_C
_Dot11DTIMPeriod_Object=MibScalar
dot11DTIMPeriod=_Dot11DTIMPeriod_Object((1,3,6,1,4,1,171,1,3,1,1,8),_Dot11DTIMPeriod_Type())
dot11DTIMPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11DTIMPeriod.setStatus(_A)
class _Dot11DisassociateReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot11DisassociateReason_Type.__name__=_C
_Dot11DisassociateReason_Object=MibScalar
dot11DisassociateReason=_Dot11DisassociateReason_Object((1,3,6,1,4,1,171,1,3,1,1,9),_Dot11DisassociateReason_Type())
dot11DisassociateReason.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DisassociateReason.setStatus(_A)
_Dot11DisassociateStation_Type=MacAddress
_Dot11DisassociateStation_Object=MibScalar
dot11DisassociateStation=_Dot11DisassociateStation_Object((1,3,6,1,4,1,171,1,3,1,1,10),_Dot11DisassociateStation_Type())
dot11DisassociateStation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DisassociateStation.setStatus(_A)
class _Dot11DeauthenticateReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot11DeauthenticateReason_Type.__name__=_C
_Dot11DeauthenticateReason_Object=MibScalar
dot11DeauthenticateReason=_Dot11DeauthenticateReason_Object((1,3,6,1,4,1,171,1,3,1,1,11),_Dot11DeauthenticateReason_Type())
dot11DeauthenticateReason.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DeauthenticateReason.setStatus(_A)
_Dot11DeauthenticateStation_Type=MacAddress
_Dot11DeauthenticateStation_Object=MibScalar
dot11DeauthenticateStation=_Dot11DeauthenticateStation_Object((1,3,6,1,4,1,171,1,3,1,1,12),_Dot11DeauthenticateStation_Type())
dot11DeauthenticateStation.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DeauthenticateStation.setStatus(_A)
class _Dot11AuthenticateFailStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Dot11AuthenticateFailStatus_Type.__name__=_C
_Dot11AuthenticateFailStatus_Object=MibScalar
dot11AuthenticateFailStatus=_Dot11AuthenticateFailStatus_Object((1,3,6,1,4,1,171,1,3,1,1,13),_Dot11AuthenticateFailStatus_Type())
dot11AuthenticateFailStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticateFailStatus.setStatus(_A)
_Dot11APModeConfigEntry_ObjectIdentity=ObjectIdentity
dot11APModeConfigEntry=_Dot11APModeConfigEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,1,2))
class _Dot11AccessPointMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('accessPoint',1),('wirelessBridge',2),('wirelessAPClient',3),('wirelessMultiBridge',4),('backupAccessPoint',5),('repeater',6),('groupAccessPoint',7)))
_Dot11AccessPointMode_Type.__name__=_C
_Dot11AccessPointMode_Object=MibScalar
dot11AccessPointMode=_Dot11AccessPointMode_Object((1,3,6,1,4,1,171,1,3,1,2,1),_Dot11AccessPointMode_Type())
dot11AccessPointMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11AccessPointMode.setStatus(_A)
_Dot11RemoteMACAddress_Type=MacAddress
_Dot11RemoteMACAddress_Object=MibScalar
dot11RemoteMACAddress=_Dot11RemoteMACAddress_Object((1,3,6,1,4,1,171,1,3,1,2,2),_Dot11RemoteMACAddress_Type())
dot11RemoteMACAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11RemoteMACAddress.setStatus(_A)
_Dot11BackupAPRemoteServerIPAddress_Type=IpAddress
_Dot11BackupAPRemoteServerIPAddress_Object=MibScalar
dot11BackupAPRemoteServerIPAddress=_Dot11BackupAPRemoteServerIPAddress_Object((1,3,6,1,4,1,171,1,3,1,2,3),_Dot11BackupAPRemoteServerIPAddress_Type())
dot11BackupAPRemoteServerIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11BackupAPRemoteServerIPAddress.setStatus(_A)
class _Dot11GroupAPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Dot11GroupAPID_Type.__name__=_F
_Dot11GroupAPID_Object=MibScalar
dot11GroupAPID=_Dot11GroupAPID_Object((1,3,6,1,4,1,171,1,3,1,2,4),_Dot11GroupAPID_Type())
dot11GroupAPID.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11GroupAPID.setStatus(_A)
_Dot11PrivacyEntry_ObjectIdentity=ObjectIdentity
dot11PrivacyEntry=_Dot11PrivacyEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,1,3))
class _Dot11AuthenticationAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('openSystem',1),('sharedKey',2),('both',3)))
_Dot11AuthenticationAlgorithm_Type.__name__=_C
_Dot11AuthenticationAlgorithm_Object=MibScalar
dot11AuthenticationAlgorithm=_Dot11AuthenticationAlgorithm_Object((1,3,6,1,4,1,171,1,3,1,3,1),_Dot11AuthenticationAlgorithm_Type())
dot11AuthenticationAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11AuthenticationAlgorithm.setStatus(_A)
_Dot11PrivacyInvoked_Type=TruthValue
_Dot11PrivacyInvoked_Object=MibScalar
dot11PrivacyInvoked=_Dot11PrivacyInvoked_Object((1,3,6,1,4,1,171,1,3,1,3,2),_Dot11PrivacyInvoked_Type())
dot11PrivacyInvoked.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11PrivacyInvoked.setStatus(_A)
class _Dot11WEPDefaultKeyID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_Dot11WEPDefaultKeyID_Type.__name__=_C
_Dot11WEPDefaultKeyID_Object=MibScalar
dot11WEPDefaultKeyID=_Dot11WEPDefaultKeyID_Object((1,3,6,1,4,1,171,1,3,1,3,3),_Dot11WEPDefaultKeyID_Type())
dot11WEPDefaultKeyID.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11WEPDefaultKeyID.setStatus(_A)
class _Dot11WEPKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('w-64Bit',1),('w-128Bit',2),('w-256Bit',3)))
_Dot11WEPKeyLength_Type.__name__=_C
_Dot11WEPKeyLength_Object=MibScalar
dot11WEPKeyLength=_Dot11WEPKeyLength_Object((1,3,6,1,4,1,171,1,3,1,3,4),_Dot11WEPKeyLength_Type())
dot11WEPKeyLength.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11WEPKeyLength.setStatus(_A)
class _Dot11WEPKeyMappingLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,64))
_Dot11WEPKeyMappingLength_Type.__name__=_C
_Dot11WEPKeyMappingLength_Object=MibScalar
dot11WEPKeyMappingLength=_Dot11WEPKeyMappingLength_Object((1,3,6,1,4,1,171,1,3,1,3,5),_Dot11WEPKeyMappingLength_Type())
dot11WEPKeyMappingLength.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WEPKeyMappingLength.setStatus(_A)
_Dot11ExcludeUnencrypted_Type=TruthValue
_Dot11ExcludeUnencrypted_Object=MibScalar
dot11ExcludeUnencrypted=_Dot11ExcludeUnencrypted_Object((1,3,6,1,4,1,171,1,3,1,3,6),_Dot11ExcludeUnencrypted_Type())
dot11ExcludeUnencrypted.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ExcludeUnencrypted.setStatus(_A)
_Dot11WEPICVErrorCount_Type=Counter32
_Dot11WEPICVErrorCount_Object=MibScalar
dot11WEPICVErrorCount=_Dot11WEPICVErrorCount_Object((1,3,6,1,4,1,171,1,3,1,3,7),_Dot11WEPICVErrorCount_Type())
dot11WEPICVErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WEPICVErrorCount.setStatus(_A)
_Dot11WEPExcludedCount_Type=Counter32
_Dot11WEPExcludedCount_Object=MibScalar
dot11WEPExcludedCount=_Dot11WEPExcludedCount_Object((1,3,6,1,4,1,171,1,3,1,3,8),_Dot11WEPExcludedCount_Type())
dot11WEPExcludedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WEPExcludedCount.setStatus(_A)
_Dot11mac_ObjectIdentity=ObjectIdentity
dot11mac=_Dot11mac_ObjectIdentity((1,3,6,1,4,1,171,1,3,2))
_Dot11OperationEntry_ObjectIdentity=ObjectIdentity
dot11OperationEntry=_Dot11OperationEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,2,1))
_Dot11MACAddress_Type=MacAddress
_Dot11MACAddress_Object=MibScalar
dot11MACAddress=_Dot11MACAddress_Object((1,3,6,1,4,1,171,1,3,2,1,1),_Dot11MACAddress_Type())
dot11MACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MACAddress.setStatus(_A)
class _Dot11RTSThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2432))
_Dot11RTSThreshold_Type.__name__=_C
_Dot11RTSThreshold_Object=MibScalar
dot11RTSThreshold=_Dot11RTSThreshold_Object((1,3,6,1,4,1,171,1,3,2,1,2),_Dot11RTSThreshold_Type())
dot11RTSThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11RTSThreshold.setStatus(_A)
class _Dot11ShortRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11ShortRetryLimit_Type.__name__=_C
_Dot11ShortRetryLimit_Object=MibScalar
dot11ShortRetryLimit=_Dot11ShortRetryLimit_Object((1,3,6,1,4,1,171,1,3,2,1,3),_Dot11ShortRetryLimit_Type())
dot11ShortRetryLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11ShortRetryLimit.setStatus(_A)
class _Dot11LongRetryLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11LongRetryLimit_Type.__name__=_C
_Dot11LongRetryLimit_Object=MibScalar
dot11LongRetryLimit=_Dot11LongRetryLimit_Object((1,3,6,1,4,1,171,1,3,2,1,4),_Dot11LongRetryLimit_Type())
dot11LongRetryLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11LongRetryLimit.setStatus(_A)
class _Dot11FragmentationThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,2346))
_Dot11FragmentationThreshold_Type.__name__=_C
_Dot11FragmentationThreshold_Object=MibScalar
dot11FragmentationThreshold=_Dot11FragmentationThreshold_Object((1,3,6,1,4,1,171,1,3,2,1,5),_Dot11FragmentationThreshold_Type())
dot11FragmentationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11FragmentationThreshold.setStatus(_A)
_Dot11SSIDBroadcast_Type=TruthValue
_Dot11SSIDBroadcast_Object=MibScalar
dot11SSIDBroadcast=_Dot11SSIDBroadcast_Object((1,3,6,1,4,1,171,1,3,2,1,6),_Dot11SSIDBroadcast_Type())
dot11SSIDBroadcast.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11SSIDBroadcast.setStatus(_A)
class _Dot11PreambleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('longPreamble',1),('shortPreamble',2)))
_Dot11PreambleType_Type.__name__=_C
_Dot11PreambleType_Object=MibScalar
dot11PreambleType=_Dot11PreambleType_Object((1,3,6,1,4,1,171,1,3,2,1,7),_Dot11PreambleType_Type())
dot11PreambleType.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11PreambleType.setStatus(_A)
class _Dot11MaxTransmitMSDULifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MaxTransmitMSDULifetime_Type.__name__=_C
_Dot11MaxTransmitMSDULifetime_Object=MibScalar
dot11MaxTransmitMSDULifetime=_Dot11MaxTransmitMSDULifetime_Object((1,3,6,1,4,1,171,1,3,2,1,8),_Dot11MaxTransmitMSDULifetime_Type())
dot11MaxTransmitMSDULifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MaxTransmitMSDULifetime.setStatus(_A)
class _Dot11MaxReceiveLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Dot11MaxReceiveLifetime_Type.__name__=_C
_Dot11MaxReceiveLifetime_Object=MibScalar
dot11MaxReceiveLifetime=_Dot11MaxReceiveLifetime_Object((1,3,6,1,4,1,171,1,3,2,1,9),_Dot11MaxReceiveLifetime_Type())
dot11MaxReceiveLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11MaxReceiveLifetime.setStatus(_A)
class _Dot11ManufacturerID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Dot11ManufacturerID_Type.__name__=_E
_Dot11ManufacturerID_Object=MibScalar
dot11ManufacturerID=_Dot11ManufacturerID_Object((1,3,6,1,4,1,171,1,3,2,1,10),_Dot11ManufacturerID_Type())
dot11ManufacturerID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ManufacturerID.setStatus(_A)
class _Dot11ProductID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Dot11ProductID_Type.__name__=_E
_Dot11ProductID_Object=MibScalar
dot11ProductID=_Dot11ProductID_Object((1,3,6,1,4,1,171,1,3,2,1,11),_Dot11ProductID_Type())
dot11ProductID.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ProductID.setStatus(_A)
_Dot11CountersEntry_ObjectIdentity=ObjectIdentity
dot11CountersEntry=_Dot11CountersEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,2,2))
_Dot11TransmittedFragmentCount_Type=Counter32
_Dot11TransmittedFragmentCount_Object=MibScalar
dot11TransmittedFragmentCount=_Dot11TransmittedFragmentCount_Object((1,3,6,1,4,1,171,1,3,2,2,1),_Dot11TransmittedFragmentCount_Type())
dot11TransmittedFragmentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TransmittedFragmentCount.setStatus(_A)
_Dot11MulticastTransmittedFrameCount_Type=Counter32
_Dot11MulticastTransmittedFrameCount_Object=MibScalar
dot11MulticastTransmittedFrameCount=_Dot11MulticastTransmittedFrameCount_Object((1,3,6,1,4,1,171,1,3,2,2,2),_Dot11MulticastTransmittedFrameCount_Type())
dot11MulticastTransmittedFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MulticastTransmittedFrameCount.setStatus(_A)
_Dot11FailedCount_Type=Counter32
_Dot11FailedCount_Object=MibScalar
dot11FailedCount=_Dot11FailedCount_Object((1,3,6,1,4,1,171,1,3,2,2,3),_Dot11FailedCount_Type())
dot11FailedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FailedCount.setStatus(_A)
_Dot11RetryCount_Type=Counter32
_Dot11RetryCount_Object=MibScalar
dot11RetryCount=_Dot11RetryCount_Object((1,3,6,1,4,1,171,1,3,2,2,4),_Dot11RetryCount_Type())
dot11RetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RetryCount.setStatus(_A)
_Dot11MultipleRetryCount_Type=Counter32
_Dot11MultipleRetryCount_Object=MibScalar
dot11MultipleRetryCount=_Dot11MultipleRetryCount_Object((1,3,6,1,4,1,171,1,3,2,2,5),_Dot11MultipleRetryCount_Type())
dot11MultipleRetryCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MultipleRetryCount.setStatus(_A)
_Dot11FrameDuplicateCount_Type=Counter32
_Dot11FrameDuplicateCount_Object=MibScalar
dot11FrameDuplicateCount=_Dot11FrameDuplicateCount_Object((1,3,6,1,4,1,171,1,3,2,2,6),_Dot11FrameDuplicateCount_Type())
dot11FrameDuplicateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FrameDuplicateCount.setStatus(_A)
_Dot11RTSSuccessCount_Type=Counter32
_Dot11RTSSuccessCount_Object=MibScalar
dot11RTSSuccessCount=_Dot11RTSSuccessCount_Object((1,3,6,1,4,1,171,1,3,2,2,7),_Dot11RTSSuccessCount_Type())
dot11RTSSuccessCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RTSSuccessCount.setStatus(_A)
_Dot11RTSFailureCount_Type=Counter32
_Dot11RTSFailureCount_Object=MibScalar
dot11RTSFailureCount=_Dot11RTSFailureCount_Object((1,3,6,1,4,1,171,1,3,2,2,8),_Dot11RTSFailureCount_Type())
dot11RTSFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RTSFailureCount.setStatus(_A)
_Dot11ACKFailureCount_Type=Counter32
_Dot11ACKFailureCount_Object=MibScalar
dot11ACKFailureCount=_Dot11ACKFailureCount_Object((1,3,6,1,4,1,171,1,3,2,2,9),_Dot11ACKFailureCount_Type())
dot11ACKFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ACKFailureCount.setStatus(_A)
_Dot11ReceivedFragmentCount_Type=Counter32
_Dot11ReceivedFragmentCount_Object=MibScalar
dot11ReceivedFragmentCount=_Dot11ReceivedFragmentCount_Object((1,3,6,1,4,1,171,1,3,2,2,10),_Dot11ReceivedFragmentCount_Type())
dot11ReceivedFragmentCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ReceivedFragmentCount.setStatus(_A)
_Dot11MulticastReceivedFrameCount_Type=Counter32
_Dot11MulticastReceivedFrameCount_Object=MibScalar
dot11MulticastReceivedFrameCount=_Dot11MulticastReceivedFrameCount_Object((1,3,6,1,4,1,171,1,3,2,2,11),_Dot11MulticastReceivedFrameCount_Type())
dot11MulticastReceivedFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11MulticastReceivedFrameCount.setStatus(_A)
_Dot11FCSErrorCount_Type=Counter32
_Dot11FCSErrorCount_Object=MibScalar
dot11FCSErrorCount=_Dot11FCSErrorCount_Object((1,3,6,1,4,1,171,1,3,2,2,12),_Dot11FCSErrorCount_Type())
dot11FCSErrorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11FCSErrorCount.setStatus(_A)
_Dot11TransmittedFrameCount_Type=Counter32
_Dot11TransmittedFrameCount_Object=MibScalar
dot11TransmittedFrameCount=_Dot11TransmittedFrameCount_Object((1,3,6,1,4,1,171,1,3,2,2,13),_Dot11TransmittedFrameCount_Type())
dot11TransmittedFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TransmittedFrameCount.setStatus(_A)
_Dot11WEPUndecryptableCount_Type=Counter32
_Dot11WEPUndecryptableCount_Object=MibScalar
dot11WEPUndecryptableCount=_Dot11WEPUndecryptableCount_Object((1,3,6,1,4,1,171,1,3,2,2,14),_Dot11WEPUndecryptableCount_Type())
dot11WEPUndecryptableCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11WEPUndecryptableCount.setStatus(_A)
_Dot11res_ObjectIdentity=ObjectIdentity
dot11res=_Dot11res_ObjectIdentity((1,3,6,1,4,1,171,1,3,3))
_Dot11resAttribute_ObjectIdentity=ObjectIdentity
dot11resAttribute=_Dot11resAttribute_ObjectIdentity((1,3,6,1,4,1,171,1,3,3,1))
class _Dot11ResourceTypeIDName_Type(DisplayString):defaultValue=OctetString('RTID');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_Dot11ResourceTypeIDName_Type.__name__=_E
_Dot11ResourceTypeIDName_Object=MibScalar
dot11ResourceTypeIDName=_Dot11ResourceTypeIDName_Object((1,3,6,1,4,1,171,1,3,3,1,1),_Dot11ResourceTypeIDName_Type())
dot11ResourceTypeIDName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ResourceTypeIDName.setStatus(_A)
_Dot11ResourceInfoEntry_ObjectIdentity=ObjectIdentity
dot11ResourceInfoEntry=_Dot11ResourceInfoEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,3,1,2))
class _Dot11manufacturerOUI_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_Dot11manufacturerOUI_Type.__name__=_F
_Dot11manufacturerOUI_Object=MibScalar
dot11manufacturerOUI=_Dot11manufacturerOUI_Object((1,3,6,1,4,1,171,1,3,3,1,2,1),_Dot11manufacturerOUI_Type())
dot11manufacturerOUI.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11manufacturerOUI.setStatus(_A)
class _Dot11manufacturerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Dot11manufacturerName_Type.__name__=_E
_Dot11manufacturerName_Object=MibScalar
dot11manufacturerName=_Dot11manufacturerName_Object((1,3,6,1,4,1,171,1,3,3,1,2,2),_Dot11manufacturerName_Type())
dot11manufacturerName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11manufacturerName.setStatus(_A)
class _Dot11manufacturerProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Dot11manufacturerProductName_Type.__name__=_E
_Dot11manufacturerProductName_Object=MibScalar
dot11manufacturerProductName=_Dot11manufacturerProductName_Object((1,3,6,1,4,1,171,1,3,3,1,2,3),_Dot11manufacturerProductName_Type())
dot11manufacturerProductName.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11manufacturerProductName.setStatus(_A)
class _Dot11manufacturerProductVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_Dot11manufacturerProductVersion_Type.__name__=_E
_Dot11manufacturerProductVersion_Object=MibScalar
dot11manufacturerProductVersion=_Dot11manufacturerProductVersion_Object((1,3,6,1,4,1,171,1,3,3,1,2,4),_Dot11manufacturerProductVersion_Type())
dot11manufacturerProductVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11manufacturerProductVersion.setStatus(_A)
_Dot11phy_ObjectIdentity=ObjectIdentity
dot11phy=_Dot11phy_ObjectIdentity((1,3,6,1,4,1,171,1,3,4))
_Dot11PhyOperationEntry_ObjectIdentity=ObjectIdentity
dot11PhyOperationEntry=_Dot11PhyOperationEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,4,1))
class _Dot11PHYType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fhss',1),('dsss',2),('irbaseband',3)))
_Dot11PHYType_Type.__name__=_C
_Dot11PHYType_Object=MibScalar
dot11PHYType=_Dot11PHYType_Object((1,3,6,1,4,1,171,1,3,4,1,1),_Dot11PHYType_Type())
dot11PHYType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11PHYType.setStatus(_A)
_Dot11CurrentRegDomain_Type=Integer32
_Dot11CurrentRegDomain_Object=MibScalar
dot11CurrentRegDomain=_Dot11CurrentRegDomain_Object((1,3,6,1,4,1,171,1,3,4,1,2),_Dot11CurrentRegDomain_Type())
dot11CurrentRegDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CurrentRegDomain.setStatus(_A)
class _Dot11TempType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('tempType1',1),('tempType2',2)))
_Dot11TempType_Type.__name__=_C
_Dot11TempType_Object=MibScalar
dot11TempType=_Dot11TempType_Object((1,3,6,1,4,1,171,1,3,4,1,3),_Dot11TempType_Type())
dot11TempType.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TempType.setStatus(_A)
class _Dot11RegDomainsSupportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(16,32,48,49,50,64)));namedValues=NamedValues(*(('fcc',16),('doc',32),('etsi',48),('spain',49),('france',50),('mkk',64)))
_Dot11RegDomainsSupportValue_Type.__name__=_C
_Dot11RegDomainsSupportValue_Object=MibScalar
dot11RegDomainsSupportValue=_Dot11RegDomainsSupportValue_Object((1,3,6,1,4,1,171,1,3,4,1,4),_Dot11RegDomainsSupportValue_Type())
dot11RegDomainsSupportValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11RegDomainsSupportValue.setStatus(_A)
class _Dot11SupportedDataRatesTxValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,127))
_Dot11SupportedDataRatesTxValue_Type.__name__=_C
_Dot11SupportedDataRatesTxValue_Object=MibScalar
dot11SupportedDataRatesTxValue=_Dot11SupportedDataRatesTxValue_Object((1,3,6,1,4,1,171,1,3,4,1,5),_Dot11SupportedDataRatesTxValue_Type())
dot11SupportedDataRatesTxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11SupportedDataRatesTxValue.setStatus(_A)
class _Dot11SupportedDataRatesRxValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,127))
_Dot11SupportedDataRatesRxValue_Type.__name__=_C
_Dot11SupportedDataRatesRxValue_Object=MibScalar
dot11SupportedDataRatesRxValue=_Dot11SupportedDataRatesRxValue_Object((1,3,6,1,4,1,171,1,3,4,1,6),_Dot11SupportedDataRatesRxValue_Type())
dot11SupportedDataRatesRxValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11SupportedDataRatesRxValue.setStatus(_A)
class _Dot11CurrentTxRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,127))
_Dot11CurrentTxRate_Type.__name__=_C
_Dot11CurrentTxRate_Object=MibScalar
dot11CurrentTxRate=_Dot11CurrentTxRate_Object((1,3,6,1,4,1,171,1,3,4,1,7),_Dot11CurrentTxRate_Type())
dot11CurrentTxRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11CurrentTxRate.setStatus(_A)
_Dot11ChannelAgilityPresent_Type=TruthValue
_Dot11ChannelAgilityPresent_Object=MibScalar
dot11ChannelAgilityPresent=_Dot11ChannelAgilityPresent_Object((1,3,6,1,4,1,171,1,3,4,1,8),_Dot11ChannelAgilityPresent_Type())
dot11ChannelAgilityPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ChannelAgilityPresent.setStatus(_A)
_Dot11ChannelAgilityEnabled_Type=TruthValue
_Dot11ChannelAgilityEnabled_Object=MibScalar
dot11ChannelAgilityEnabled=_Dot11ChannelAgilityEnabled_Object((1,3,6,1,4,1,171,1,3,4,1,9),_Dot11ChannelAgilityEnabled_Type())
dot11ChannelAgilityEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ChannelAgilityEnabled.setStatus(_A)
_Dot11PhyAntennaEntry_ObjectIdentity=ObjectIdentity
dot11PhyAntennaEntry=_Dot11PhyAntennaEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,4,2))
class _Dot11CurrentTxAntenna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11CurrentTxAntenna_Type.__name__=_C
_Dot11CurrentTxAntenna_Object=MibScalar
dot11CurrentTxAntenna=_Dot11CurrentTxAntenna_Object((1,3,6,1,4,1,171,1,3,4,2,1),_Dot11CurrentTxAntenna_Type())
dot11CurrentTxAntenna.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CurrentTxAntenna.setStatus(_A)
class _Dot11DiversitySupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fixedlist',1),('notsupported',2),('dynamic',3)))
_Dot11DiversitySupport_Type.__name__=_C
_Dot11DiversitySupport_Object=MibScalar
dot11DiversitySupport=_Dot11DiversitySupport_Object((1,3,6,1,4,1,171,1,3,4,2,2),_Dot11DiversitySupport_Type())
dot11DiversitySupport.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11DiversitySupport.setStatus(_A)
class _Dot11CurrentRxAntenna_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Dot11CurrentRxAntenna_Type.__name__=_C
_Dot11CurrentRxAntenna_Object=MibScalar
dot11CurrentRxAntenna=_Dot11CurrentRxAntenna_Object((1,3,6,1,4,1,171,1,3,4,2,3),_Dot11CurrentRxAntenna_Type())
dot11CurrentRxAntenna.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CurrentRxAntenna.setStatus(_A)
_Dot11PhyTxPowerEntry_ObjectIdentity=ObjectIdentity
dot11PhyTxPowerEntry=_Dot11PhyTxPowerEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,4,3))
class _Dot11NumberSupportedPowerLevels_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Dot11NumberSupportedPowerLevels_Type.__name__=_C
_Dot11NumberSupportedPowerLevels_Object=MibScalar
dot11NumberSupportedPowerLevels=_Dot11NumberSupportedPowerLevels_Object((1,3,6,1,4,1,171,1,3,4,3,1),_Dot11NumberSupportedPowerLevels_Type())
dot11NumberSupportedPowerLevels.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11NumberSupportedPowerLevels.setStatus(_A)
class _Dot11TxPowerLevel1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel1_Type.__name__=_C
_Dot11TxPowerLevel1_Object=MibScalar
dot11TxPowerLevel1=_Dot11TxPowerLevel1_Object((1,3,6,1,4,1,171,1,3,4,3,2),_Dot11TxPowerLevel1_Type())
dot11TxPowerLevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel1.setStatus(_A)
class _Dot11TxPowerLevel2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel2_Type.__name__=_C
_Dot11TxPowerLevel2_Object=MibScalar
dot11TxPowerLevel2=_Dot11TxPowerLevel2_Object((1,3,6,1,4,1,171,1,3,4,3,3),_Dot11TxPowerLevel2_Type())
dot11TxPowerLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel2.setStatus(_A)
class _Dot11TxPowerLevel3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel3_Type.__name__=_C
_Dot11TxPowerLevel3_Object=MibScalar
dot11TxPowerLevel3=_Dot11TxPowerLevel3_Object((1,3,6,1,4,1,171,1,3,4,3,4),_Dot11TxPowerLevel3_Type())
dot11TxPowerLevel3.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel3.setStatus(_A)
class _Dot11TxPowerLevel4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel4_Type.__name__=_C
_Dot11TxPowerLevel4_Object=MibScalar
dot11TxPowerLevel4=_Dot11TxPowerLevel4_Object((1,3,6,1,4,1,171,1,3,4,3,5),_Dot11TxPowerLevel4_Type())
dot11TxPowerLevel4.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel4.setStatus(_A)
class _Dot11TxPowerLevel5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel5_Type.__name__=_C
_Dot11TxPowerLevel5_Object=MibScalar
dot11TxPowerLevel5=_Dot11TxPowerLevel5_Object((1,3,6,1,4,1,171,1,3,4,3,6),_Dot11TxPowerLevel5_Type())
dot11TxPowerLevel5.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel5.setStatus(_A)
class _Dot11TxPowerLevel6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel6_Type.__name__=_C
_Dot11TxPowerLevel6_Object=MibScalar
dot11TxPowerLevel6=_Dot11TxPowerLevel6_Object((1,3,6,1,4,1,171,1,3,4,3,7),_Dot11TxPowerLevel6_Type())
dot11TxPowerLevel6.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel6.setStatus(_A)
class _Dot11TxPowerLevel7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel7_Type.__name__=_C
_Dot11TxPowerLevel7_Object=MibScalar
dot11TxPowerLevel7=_Dot11TxPowerLevel7_Object((1,3,6,1,4,1,171,1,3,4,3,8),_Dot11TxPowerLevel7_Type())
dot11TxPowerLevel7.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel7.setStatus(_A)
class _Dot11TxPowerLevel8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_Dot11TxPowerLevel8_Type.__name__=_C
_Dot11TxPowerLevel8_Object=MibScalar
dot11TxPowerLevel8=_Dot11TxPowerLevel8_Object((1,3,6,1,4,1,171,1,3,4,3,9),_Dot11TxPowerLevel8_Type())
dot11TxPowerLevel8.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11TxPowerLevel8.setStatus(_A)
class _Dot11CurrentTxPowerLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_Dot11CurrentTxPowerLevel_Type.__name__=_C
_Dot11CurrentTxPowerLevel_Object=MibScalar
dot11CurrentTxPowerLevel=_Dot11CurrentTxPowerLevel_Object((1,3,6,1,4,1,171,1,3,4,3,10),_Dot11CurrentTxPowerLevel_Type())
dot11CurrentTxPowerLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CurrentTxPowerLevel.setStatus(_A)
_Dot11PhyDSSSEntry_ObjectIdentity=ObjectIdentity
dot11PhyDSSSEntry=_Dot11PhyDSSSEntry_ObjectIdentity((1,3,6,1,4,1,171,1,3,4,4))
class _Dot11CurrentChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,14))
_Dot11CurrentChannel_Type.__name__=_C
_Dot11CurrentChannel_Object=MibScalar
dot11CurrentChannel=_Dot11CurrentChannel_Object((1,3,6,1,4,1,171,1,3,4,4,1),_Dot11CurrentChannel_Type())
dot11CurrentChannel.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11CurrentChannel.setStatus(_A)
_Dot11DynamicChannelEnabled_Type=TruthValue
_Dot11DynamicChannelEnabled_Object=MibScalar
dot11DynamicChannelEnabled=_Dot11DynamicChannelEnabled_Object((1,3,6,1,4,1,171,1,3,4,4,2),_Dot11DynamicChannelEnabled_Type())
dot11DynamicChannelEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11DynamicChannelEnabled.setStatus(_A)
class _Dot11CCAModeSupported_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Dot11CCAModeSupported_Type.__name__=_C
_Dot11CCAModeSupported_Object=MibScalar
dot11CCAModeSupported=_Dot11CCAModeSupported_Object((1,3,6,1,4,1,171,1,3,4,4,3),_Dot11CCAModeSupported_Type())
dot11CCAModeSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CCAModeSupported.setStatus(_A)
class _Dot11CurrentCCAMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('edonly',1),('csonly',2),('edandcs',4)))
_Dot11CurrentCCAMode_Type.__name__=_C
_Dot11CurrentCCAMode_Object=MibScalar
dot11CurrentCCAMode=_Dot11CurrentCCAMode_Object((1,3,6,1,4,1,171,1,3,4,4,4),_Dot11CurrentCCAMode_Type())
dot11CurrentCCAMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11CurrentCCAMode.setStatus(_A)
_Dot11EDThreshold_Type=Integer32
_Dot11EDThreshold_Object=MibScalar
dot11EDThreshold=_Dot11EDThreshold_Object((1,3,6,1,4,1,171,1,3,4,4,5),_Dot11EDThreshold_Type())
dot11EDThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:dot11EDThreshold.setStatus(_A)
class _Dot11ShortPreambleOptionImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Dot11ShortPreambleOptionImplemented_Type.__name__=_C
_Dot11ShortPreambleOptionImplemented_Object=MibScalar
dot11ShortPreambleOptionImplemented=_Dot11ShortPreambleOptionImplemented_Object((1,3,6,1,4,1,171,1,3,4,4,6),_Dot11ShortPreambleOptionImplemented_Type())
dot11ShortPreambleOptionImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11ShortPreambleOptionImplemented.setStatus(_A)
class _Dot11PBCCOptionImplemented_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Dot11PBCCOptionImplemented_Type.__name__=_C
_Dot11PBCCOptionImplemented_Object=MibScalar
dot11PBCCOptionImplemented=_Dot11PBCCOptionImplemented_Object((1,3,6,1,4,1,171,1,3,4,4,7),_Dot11PBCCOptionImplemented_Type())
dot11PBCCOptionImplemented.setMaxAccess(_B)
if mibBuilder.loadTexts:dot11PBCCOptionImplemented.setStatus(_A)
_DlkEnterpriseAPTrap_ObjectIdentity=ObjectIdentity
dlkEnterpriseAPTrap=_DlkEnterpriseAPTrap_ObjectIdentity((1,3,6,1,4,1,171,1,4))
mibBuilder.exportSymbols('DLINK-WLAN-MIB',**{'dlink':dlink,'dlkEnterpriseAP':dlkEnterpriseAP,'dlkEnterpriseAPsys':dlkEnterpriseAPsys,'enterpriseAPSysConfigSave':enterpriseAPSysConfigSave,'enterpriseAPSysReboot':enterpriseAPSysReboot,'enterpriseAPSysConfigApply':enterpriseAPSysConfigApply,'dlkEnterpriseAPlan':dlkEnterpriseAPlan,'dlk80211bPlusDot11':dlk80211bPlusDot11,'dot11smt':dot11smt,'dot11StationConfigEntry':dot11StationConfigEntry,'dot11StationID':dot11StationID,'dot11PrivacyOptionImplemented':dot11PrivacyOptionImplemented,'dot11PowerManagementMode':dot11PowerManagementMode,'dot11DesiredSSID':dot11DesiredSSID,'dot11DesiredBSSType':dot11DesiredBSSType,'dot11OperationalRateSet':dot11OperationalRateSet,'dot11BeaconPeriod':dot11BeaconPeriod,'dot11DTIMPeriod':dot11DTIMPeriod,'dot11DisassociateReason':dot11DisassociateReason,'dot11DisassociateStation':dot11DisassociateStation,'dot11DeauthenticateReason':dot11DeauthenticateReason,'dot11DeauthenticateStation':dot11DeauthenticateStation,'dot11AuthenticateFailStatus':dot11AuthenticateFailStatus,'dot11APModeConfigEntry':dot11APModeConfigEntry,'dot11AccessPointMode':dot11AccessPointMode,'dot11RemoteMACAddress':dot11RemoteMACAddress,'dot11BackupAPRemoteServerIPAddress':dot11BackupAPRemoteServerIPAddress,'dot11GroupAPID':dot11GroupAPID,'dot11PrivacyEntry':dot11PrivacyEntry,'dot11AuthenticationAlgorithm':dot11AuthenticationAlgorithm,'dot11PrivacyInvoked':dot11PrivacyInvoked,'dot11WEPDefaultKeyID':dot11WEPDefaultKeyID,'dot11WEPKeyLength':dot11WEPKeyLength,'dot11WEPKeyMappingLength':dot11WEPKeyMappingLength,'dot11ExcludeUnencrypted':dot11ExcludeUnencrypted,'dot11WEPICVErrorCount':dot11WEPICVErrorCount,'dot11WEPExcludedCount':dot11WEPExcludedCount,'dot11mac':dot11mac,'dot11OperationEntry':dot11OperationEntry,'dot11MACAddress':dot11MACAddress,'dot11RTSThreshold':dot11RTSThreshold,'dot11ShortRetryLimit':dot11ShortRetryLimit,'dot11LongRetryLimit':dot11LongRetryLimit,'dot11FragmentationThreshold':dot11FragmentationThreshold,'dot11SSIDBroadcast':dot11SSIDBroadcast,'dot11PreambleType':dot11PreambleType,'dot11MaxTransmitMSDULifetime':dot11MaxTransmitMSDULifetime,'dot11MaxReceiveLifetime':dot11MaxReceiveLifetime,'dot11ManufacturerID':dot11ManufacturerID,'dot11ProductID':dot11ProductID,'dot11CountersEntry':dot11CountersEntry,'dot11TransmittedFragmentCount':dot11TransmittedFragmentCount,'dot11MulticastTransmittedFrameCount':dot11MulticastTransmittedFrameCount,'dot11FailedCount':dot11FailedCount,'dot11RetryCount':dot11RetryCount,'dot11MultipleRetryCount':dot11MultipleRetryCount,'dot11FrameDuplicateCount':dot11FrameDuplicateCount,'dot11RTSSuccessCount':dot11RTSSuccessCount,'dot11RTSFailureCount':dot11RTSFailureCount,'dot11ACKFailureCount':dot11ACKFailureCount,'dot11ReceivedFragmentCount':dot11ReceivedFragmentCount,'dot11MulticastReceivedFrameCount':dot11MulticastReceivedFrameCount,'dot11FCSErrorCount':dot11FCSErrorCount,'dot11TransmittedFrameCount':dot11TransmittedFrameCount,'dot11WEPUndecryptableCount':dot11WEPUndecryptableCount,'dot11res':dot11res,'dot11resAttribute':dot11resAttribute,'dot11ResourceTypeIDName':dot11ResourceTypeIDName,'dot11ResourceInfoEntry':dot11ResourceInfoEntry,'dot11manufacturerOUI':dot11manufacturerOUI,'dot11manufacturerName':dot11manufacturerName,'dot11manufacturerProductName':dot11manufacturerProductName,'dot11manufacturerProductVersion':dot11manufacturerProductVersion,'dot11phy':dot11phy,'dot11PhyOperationEntry':dot11PhyOperationEntry,'dot11PHYType':dot11PHYType,'dot11CurrentRegDomain':dot11CurrentRegDomain,'dot11TempType':dot11TempType,'dot11RegDomainsSupportValue':dot11RegDomainsSupportValue,'dot11SupportedDataRatesTxValue':dot11SupportedDataRatesTxValue,'dot11SupportedDataRatesRxValue':dot11SupportedDataRatesRxValue,'dot11CurrentTxRate':dot11CurrentTxRate,'dot11ChannelAgilityPresent':dot11ChannelAgilityPresent,'dot11ChannelAgilityEnabled':dot11ChannelAgilityEnabled,'dot11PhyAntennaEntry':dot11PhyAntennaEntry,'dot11CurrentTxAntenna':dot11CurrentTxAntenna,'dot11DiversitySupport':dot11DiversitySupport,'dot11CurrentRxAntenna':dot11CurrentRxAntenna,'dot11PhyTxPowerEntry':dot11PhyTxPowerEntry,'dot11NumberSupportedPowerLevels':dot11NumberSupportedPowerLevels,'dot11TxPowerLevel1':dot11TxPowerLevel1,'dot11TxPowerLevel2':dot11TxPowerLevel2,'dot11TxPowerLevel3':dot11TxPowerLevel3,'dot11TxPowerLevel4':dot11TxPowerLevel4,'dot11TxPowerLevel5':dot11TxPowerLevel5,'dot11TxPowerLevel6':dot11TxPowerLevel6,'dot11TxPowerLevel7':dot11TxPowerLevel7,'dot11TxPowerLevel8':dot11TxPowerLevel8,'dot11CurrentTxPowerLevel':dot11CurrentTxPowerLevel,'dot11PhyDSSSEntry':dot11PhyDSSSEntry,'dot11CurrentChannel':dot11CurrentChannel,'dot11DynamicChannelEnabled':dot11DynamicChannelEnabled,'dot11CCAModeSupported':dot11CCAModeSupported,'dot11CurrentCCAMode':dot11CurrentCCAMode,'dot11EDThreshold':dot11EDThreshold,'dot11ShortPreambleOptionImplemented':dot11ShortPreambleOptionImplemented,'dot11PBCCOptionImplemented':dot11PBCCOptionImplemented,'dlkEnterpriseAPTrap':dlkEnterpriseAPTrap})