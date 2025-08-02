_e='unknownFailure'
_d='otherFailure'
_c='hardwareFailure'
_b='softwareFailure'
_a='fsCapwapStationWhiteListId'
_Z='fsCapwapEncryptChannel'
_Y='fsCapwapBlackListId'
_X='fsCapwapWhiteListId'
_W='fsRadioNumber'
_V='CapwapBaseTunnelModeTC'
_U='CapwapBaseMacTypeTC'
_T='TruthValue'
_S='InetAddressType'
_R='InetAddress'
_Q='ifIndex'
_P='IF-MIB'
_O='other'
_N='DisplayString'
_M='SnmpAdminString'
_L='OctetString'
_K='fsCapwapWtpModelNumber'
_J='Bits'
_I='not-accessible'
_H='EnabledStatus'
_G='capwapBaseWtpProfileId'
_F='read-create'
_E='Integer32'
_D='SUPERMICRO-CAPWAP-MIB'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_P,'InterfaceIndex',_Q)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_R,_S)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_N,'MacAddress','PhysAddress','RowStatus','TextualConvention',_T)
fsCapwap=ModuleIdentity((1,3,6,1,4,1,10876,101,2,82))
if mibBuilder.loadTexts:fsCapwap.setRevisions(('2013-02-15 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
class CapwapBaseRadioIdTC(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
class CapwapBaseTunnelModeTC(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('localBridging',0),('dot3Tunnel',1),('nativeTunnel',2)))
class CapwapBaseMacTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('localMAC',0),('splitMAC',1),('both',2)))
class CapwapBaseStationIdTC(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6),ValueSizeConstraint(8,8))
_FsCapwapSystem_ObjectIdentity=ObjectIdentity
fsCapwapSystem=_FsCapwapSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,2,82,1))
class _FsCapwapModuleStatus_Type(EnabledStatus):defaultValue=1
_FsCapwapModuleStatus_Type.__name__=_H
_FsCapwapModuleStatus_Object=MibScalar
fsCapwapModuleStatus=_FsCapwapModuleStatus_Object((1,3,6,1,4,1,10876,101,2,82,1,1),_FsCapwapModuleStatus_Type())
fsCapwapModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapModuleStatus.setStatus(_A)
class _FsCapwapSystemControl_Type(TruthValue):defaultValue=1
_FsCapwapSystemControl_Type.__name__=_T
_FsCapwapSystemControl_Object=MibScalar
fsCapwapSystemControl=_FsCapwapSystemControl_Object((1,3,6,1,4,1,10876,101,2,82,1,2),_FsCapwapSystemControl_Type())
fsCapwapSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapSystemControl.setStatus(_A)
class _FsCapwapControlUdpPort_Type(Unsigned32):defaultValue=5246;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsCapwapControlUdpPort_Type.__name__=_C
_FsCapwapControlUdpPort_Object=MibScalar
fsCapwapControlUdpPort=_FsCapwapControlUdpPort_Object((1,3,6,1,4,1,10876,101,2,82,1,3),_FsCapwapControlUdpPort_Type())
fsCapwapControlUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapControlUdpPort.setStatus(_A)
class _FsCapwapControlChannelDTLSPolicyOptions_Type(Bits):defaultHexValue='01';namedValues=NamedValues(*((_O,0),('clear',1),('dtls',2)))
_FsCapwapControlChannelDTLSPolicyOptions_Type.__name__=_J
_FsCapwapControlChannelDTLSPolicyOptions_Object=MibScalar
fsCapwapControlChannelDTLSPolicyOptions=_FsCapwapControlChannelDTLSPolicyOptions_Object((1,3,6,1,4,1,10876,101,2,82,1,4),_FsCapwapControlChannelDTLSPolicyOptions_Type())
fsCapwapControlChannelDTLSPolicyOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapControlChannelDTLSPolicyOptions.setStatus(_A)
class _FsCapwapDataChannelDTLSPolicyOptions_Type(Bits):defaultHexValue='01';namedValues=NamedValues(*((_O,0),('clear',1),('dtls',2)))
_FsCapwapDataChannelDTLSPolicyOptions_Type.__name__=_J
_FsCapwapDataChannelDTLSPolicyOptions_Object=MibScalar
fsCapwapDataChannelDTLSPolicyOptions=_FsCapwapDataChannelDTLSPolicyOptions_Object((1,3,6,1,4,1,10876,101,2,82,1,5),_FsCapwapDataChannelDTLSPolicyOptions_Type())
fsCapwapDataChannelDTLSPolicyOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDataChannelDTLSPolicyOptions.setStatus(_A)
class _FsWlcDiscoveryMode_Type(Bits):defaultHexValue='01';namedValues=NamedValues(*((_O,0),('macDiscMode',1),('autoDiscMode',2)))
_FsWlcDiscoveryMode_Type.__name__=_J
_FsWlcDiscoveryMode_Object=MibScalar
fsWlcDiscoveryMode=_FsWlcDiscoveryMode_Object((1,3,6,1,4,1,10876,101,2,82,1,6),_FsWlcDiscoveryMode_Type())
fsWlcDiscoveryMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWlcDiscoveryMode.setStatus(_A)
class _FsCapwapWtpModeIgnore_Type(EnabledStatus):defaultValue=1
_FsCapwapWtpModeIgnore_Type.__name__=_H
_FsCapwapWtpModeIgnore_Object=MibScalar
fsCapwapWtpModeIgnore=_FsCapwapWtpModeIgnore_Object((1,3,6,1,4,1,10876,101,2,82,1,7),_FsCapwapWtpModeIgnore_Type())
fsCapwapWtpModeIgnore.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpModeIgnore.setStatus(_A)
class _FsCapwapDebugMask_Type(Integer32):defaultValue=0
_FsCapwapDebugMask_Type.__name__=_E
_FsCapwapDebugMask_Object=MibScalar
fsCapwapDebugMask=_FsCapwapDebugMask_Object((1,3,6,1,4,1,10876,101,2,82,1,8),_FsCapwapDebugMask_Type())
fsCapwapDebugMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDebugMask.setStatus(_A)
class _FsDtlsDebugMask_Type(Integer32):defaultValue=0
_FsDtlsDebugMask_Type.__name__=_E
_FsDtlsDebugMask_Object=MibScalar
fsDtlsDebugMask=_FsDtlsDebugMask_Object((1,3,6,1,4,1,10876,101,2,82,1,9),_FsDtlsDebugMask_Type())
fsDtlsDebugMask.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDtlsDebugMask.setStatus(_A)
class _FsDtlsEncryption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('preShared',1),('certificates',2)))
_FsDtlsEncryption_Type.__name__=_E
_FsDtlsEncryption_Object=MibScalar
fsDtlsEncryption=_FsDtlsEncryption_Object((1,3,6,1,4,1,10876,101,2,82,1,10),_FsDtlsEncryption_Type())
fsDtlsEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDtlsEncryption.setStatus(_A)
class _FsDtlsEncryptAlgorithm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('aes128',1),('dheaes128',2),('aes256',3),('dhaaes256',4)))
_FsDtlsEncryptAlgorithm_Type.__name__=_E
_FsDtlsEncryptAlgorithm_Object=MibScalar
fsDtlsEncryptAlgorithm=_FsDtlsEncryptAlgorithm_Object((1,3,6,1,4,1,10876,101,2,82,1,11),_FsDtlsEncryptAlgorithm_Type())
fsDtlsEncryptAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDtlsEncryptAlgorithm.setStatus(_A)
class _FsStationType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('blacklist',1),('whitelist',2)))
_FsStationType_Type.__name__=_E
_FsStationType_Object=MibScalar
fsStationType=_FsStationType_Object((1,3,6,1,4,1,10876,101,2,82,1,12),_FsStationType_Type())
fsStationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsStationType.setStatus(_A)
_FsCapwapWtpModel_ObjectIdentity=ObjectIdentity
fsCapwapWtpModel=_FsCapwapWtpModel_ObjectIdentity((1,3,6,1,4,1,10876,101,2,82,2))
_FsWtpModelTable_Object=MibTable
fsWtpModelTable=_FsWtpModelTable_Object((1,3,6,1,4,1,10876,101,2,82,2,1))
if mibBuilder.loadTexts:fsWtpModelTable.setStatus(_A)
_FsWtpModelEntry_Object=MibTableRow
fsWtpModelEntry=_FsWtpModelEntry_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1))
fsWtpModelEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fsWtpModelEntry.setStatus(_A)
class _FsCapwapWtpModelNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsCapwapWtpModelNumber_Type.__name__=_M
_FsCapwapWtpModelNumber_Object=MibTableColumn
fsCapwapWtpModelNumber=_FsCapwapWtpModelNumber_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,1),_FsCapwapWtpModelNumber_Type())
fsCapwapWtpModelNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCapwapWtpModelNumber.setStatus(_A)
_FsNoOfRadio_Type=CapwapBaseRadioIdTC
_FsNoOfRadio_Object=MibTableColumn
fsNoOfRadio=_FsNoOfRadio_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,2),_FsNoOfRadio_Type())
fsNoOfRadio.setMaxAccess(_B)
if mibBuilder.loadTexts:fsNoOfRadio.setStatus(_A)
class _FsCapwapWtpMacType_Type(CapwapBaseMacTypeTC):defaultValue=0
_FsCapwapWtpMacType_Type.__name__=_U
_FsCapwapWtpMacType_Object=MibTableColumn
fsCapwapWtpMacType=_FsCapwapWtpMacType_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,3),_FsCapwapWtpMacType_Type())
fsCapwapWtpMacType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpMacType.setStatus(_A)
class _FsCapwapWtpTunnelMode_Type(CapwapBaseTunnelModeTC):defaultHexValue=''
_FsCapwapWtpTunnelMode_Type.__name__=_V
_FsCapwapWtpTunnelMode_Object=MibTableColumn
fsCapwapWtpTunnelMode=_FsCapwapWtpTunnelMode_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,4),_FsCapwapWtpTunnelMode_Type())
fsCapwapWtpTunnelMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpTunnelMode.setStatus(_A)
class _FsCapwapSwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,12))
_FsCapwapSwVersion_Type.__name__=_N
_FsCapwapSwVersion_Object=MibTableColumn
fsCapwapSwVersion=_FsCapwapSwVersion_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,5),_FsCapwapSwVersion_Type())
fsCapwapSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapSwVersion.setStatus(_A)
class _FsCapwapImageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,23))
_FsCapwapImageName_Type.__name__=_N
_FsCapwapImageName_Object=MibTableColumn
fsCapwapImageName=_FsCapwapImageName_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,6),_FsCapwapImageName_Type())
fsCapwapImageName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapImageName.setStatus(_A)
_FsCapwapQosProfileName_Type=OctetString
_FsCapwapQosProfileName_Object=MibTableColumn
fsCapwapQosProfileName=_FsCapwapQosProfileName_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,7),_FsCapwapQosProfileName_Type())
fsCapwapQosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapQosProfileName.setStatus(_A)
_FsMaxStations_Type=Integer32
_FsMaxStations_Object=MibTableColumn
fsMaxStations=_FsMaxStations_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,8),_FsMaxStations_Type())
fsMaxStations.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMaxStations.setStatus(_A)
_FsWtpModelRowStatus_Type=RowStatus
_FsWtpModelRowStatus_Object=MibTableColumn
fsWtpModelRowStatus=_FsWtpModelRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,2,1,1,9),_FsWtpModelRowStatus_Type())
fsWtpModelRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWtpModelRowStatus.setStatus(_A)
_FsWtpRadioTable_Object=MibTable
fsWtpRadioTable=_FsWtpRadioTable_Object((1,3,6,1,4,1,10876,101,2,82,2,2))
if mibBuilder.loadTexts:fsWtpRadioTable.setStatus(_A)
_FsWtpRadioEntry_Object=MibTableRow
fsWtpRadioEntry=_FsWtpRadioEntry_Object((1,3,6,1,4,1,10876,101,2,82,2,2,1))
fsWtpRadioEntry.setIndexNames((0,_D,_K),(0,_D,_W))
if mibBuilder.loadTexts:fsWtpRadioEntry.setStatus(_A)
_FsRadioNumber_Type=CapwapBaseRadioIdTC
_FsRadioNumber_Object=MibTableColumn
fsRadioNumber=_FsRadioNumber_Object((1,3,6,1,4,1,10876,101,2,82,2,2,1,1),_FsRadioNumber_Type())
fsRadioNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:fsRadioNumber.setStatus(_A)
class _FsWtpRadioType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,10,13)));namedValues=NamedValues(*(('dot11b',1),('dot11a',2),('dot11g',4),('dot11bg',5),('dot11an',10),('dot11bgn',13)))
_FsWtpRadioType_Type.__name__=_E
_FsWtpRadioType_Object=MibTableColumn
fsWtpRadioType=_FsWtpRadioType_Object((1,3,6,1,4,1,10876,101,2,82,2,2,1,2),_FsWtpRadioType_Type())
fsWtpRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpRadioType.setStatus(_A)
class _FsRadioAdminStatus_Type(EnabledStatus):defaultValue=1
_FsRadioAdminStatus_Type.__name__=_H
_FsRadioAdminStatus_Object=MibTableColumn
fsRadioAdminStatus=_FsRadioAdminStatus_Object((1,3,6,1,4,1,10876,101,2,82,2,2,1,3),_FsRadioAdminStatus_Type())
fsRadioAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsRadioAdminStatus.setStatus(_A)
_FsWtpRadioRowStatus_Type=RowStatus
_FsWtpRadioRowStatus_Object=MibTableColumn
fsWtpRadioRowStatus=_FsWtpRadioRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,2,2,1,4),_FsWtpRadioRowStatus_Type())
fsWtpRadioRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWtpRadioRowStatus.setStatus(_A)
_FsCapwapConfig_ObjectIdentity=ObjectIdentity
fsCapwapConfig=_FsCapwapConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,2,82,3))
_FsCapwapWhiteListTable_Object=MibTable
fsCapwapWhiteListTable=_FsCapwapWhiteListTable_Object((1,3,6,1,4,1,10876,101,2,82,3,1))
if mibBuilder.loadTexts:fsCapwapWhiteListTable.setStatus(_A)
_FsCapwapWhiteListEntry_Object=MibTableRow
fsCapwapWhiteListEntry=_FsCapwapWhiteListEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,1,1))
fsCapwapWhiteListEntry.setIndexNames((0,_D,_X))
if mibBuilder.loadTexts:fsCapwapWhiteListEntry.setStatus(_A)
class _FsCapwapWhiteListId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_FsCapwapWhiteListId_Type.__name__=_C
_FsCapwapWhiteListId_Object=MibTableColumn
fsCapwapWhiteListId=_FsCapwapWhiteListId_Object((1,3,6,1,4,1,10876,101,2,82,3,1,1,1),_FsCapwapWhiteListId_Type())
fsCapwapWhiteListId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCapwapWhiteListId.setStatus(_A)
_FsCapwapWhiteListWtpBaseMac_Type=MacAddress
_FsCapwapWhiteListWtpBaseMac_Object=MibTableColumn
fsCapwapWhiteListWtpBaseMac=_FsCapwapWhiteListWtpBaseMac_Object((1,3,6,1,4,1,10876,101,2,82,3,1,1,2),_FsCapwapWhiteListWtpBaseMac_Type())
fsCapwapWhiteListWtpBaseMac.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWhiteListWtpBaseMac.setStatus(_A)
_FsCapwapWhiteListRowStatus_Type=RowStatus
_FsCapwapWhiteListRowStatus_Object=MibTableColumn
fsCapwapWhiteListRowStatus=_FsCapwapWhiteListRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,1,1,3),_FsCapwapWhiteListRowStatus_Type())
fsCapwapWhiteListRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapWhiteListRowStatus.setStatus(_A)
_FsCapwapBlackListTable_Object=MibTable
fsCapwapBlackListTable=_FsCapwapBlackListTable_Object((1,3,6,1,4,1,10876,101,2,82,3,2))
if mibBuilder.loadTexts:fsCapwapBlackListTable.setStatus(_A)
_FsCapwapBlackListEntry_Object=MibTableRow
fsCapwapBlackListEntry=_FsCapwapBlackListEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,2,1))
fsCapwapBlackListEntry.setIndexNames((0,_D,_Y))
if mibBuilder.loadTexts:fsCapwapBlackListEntry.setStatus(_A)
class _FsCapwapBlackListId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_FsCapwapBlackListId_Type.__name__=_C
_FsCapwapBlackListId_Object=MibTableColumn
fsCapwapBlackListId=_FsCapwapBlackListId_Object((1,3,6,1,4,1,10876,101,2,82,3,2,1,1),_FsCapwapBlackListId_Type())
fsCapwapBlackListId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCapwapBlackListId.setStatus(_A)
_FsCapwapBlackListWtpBaseMac_Type=MacAddress
_FsCapwapBlackListWtpBaseMac_Object=MibTableColumn
fsCapwapBlackListWtpBaseMac=_FsCapwapBlackListWtpBaseMac_Object((1,3,6,1,4,1,10876,101,2,82,3,2,1,2),_FsCapwapBlackListWtpBaseMac_Type())
fsCapwapBlackListWtpBaseMac.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapBlackListWtpBaseMac.setStatus(_A)
_FsCapwapBlackListRowStatus_Type=RowStatus
_FsCapwapBlackListRowStatus_Object=MibTableColumn
fsCapwapBlackListRowStatus=_FsCapwapBlackListRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,2,1,3),_FsCapwapBlackListRowStatus_Type())
fsCapwapBlackListRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapBlackListRowStatus.setStatus(_A)
_FsCapwapWtpConfigTable_Object=MibTable
fsCapwapWtpConfigTable=_FsCapwapWtpConfigTable_Object((1,3,6,1,4,1,10876,101,2,82,3,3))
if mibBuilder.loadTexts:fsCapwapWtpConfigTable.setStatus(_A)
_FsCapwapWtpConfigEntry_Object=MibTableRow
fsCapwapWtpConfigEntry=_FsCapwapWtpConfigEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1))
fsCapwapWtpConfigEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCapwapWtpConfigEntry.setStatus(_A)
class _FsCapwapWtpReset_Type(EnabledStatus):defaultValue=2
_FsCapwapWtpReset_Type.__name__=_H
_FsCapwapWtpReset_Object=MibTableColumn
fsCapwapWtpReset=_FsCapwapWtpReset_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,1),_FsCapwapWtpReset_Type())
fsCapwapWtpReset.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpReset.setStatus(_A)
class _FsCapwapClearConfig_Type(EnabledStatus):defaultValue=2
_FsCapwapClearConfig_Type.__name__=_H
_FsCapwapClearConfig_Object=MibTableColumn
fsCapwapClearConfig=_FsCapwapClearConfig_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,2),_FsCapwapClearConfig_Type())
fsCapwapClearConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapClearConfig.setStatus(_A)
class _FsWtpDiscoveryType_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('static',1),('dhcp',2),('dns',3),('acReferral',4)))
_FsWtpDiscoveryType_Type.__name__=_E
_FsWtpDiscoveryType_Object=MibTableColumn
fsWtpDiscoveryType=_FsWtpDiscoveryType_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,3),_FsWtpDiscoveryType_Type())
fsWtpDiscoveryType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpDiscoveryType.setStatus(_A)
class _FsWtpCountryString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_FsWtpCountryString_Type.__name__=_L
_FsWtpCountryString_Object=MibTableColumn
fsWtpCountryString=_FsWtpCountryString_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,4),_FsWtpCountryString_Type())
fsWtpCountryString.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpCountryString.setStatus(_A)
_FsWtpCrashDumpFileName_Type=DisplayString
_FsWtpCrashDumpFileName_Object=MibTableColumn
fsWtpCrashDumpFileName=_FsWtpCrashDumpFileName_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,5),_FsWtpCrashDumpFileName_Type())
fsWtpCrashDumpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpCrashDumpFileName.setStatus(_A)
_FsWtpMemoryDumpFileName_Type=DisplayString
_FsWtpMemoryDumpFileName_Object=MibTableColumn
fsWtpMemoryDumpFileName=_FsWtpMemoryDumpFileName_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,6),_FsWtpMemoryDumpFileName_Type())
fsWtpMemoryDumpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpMemoryDumpFileName.setStatus(_A)
class _FsWtpDeleteOperation_Type(EnabledStatus):defaultValue=2
_FsWtpDeleteOperation_Type.__name__=_H
_FsWtpDeleteOperation_Object=MibTableColumn
fsWtpDeleteOperation=_FsWtpDeleteOperation_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,7),_FsWtpDeleteOperation_Type())
fsWtpDeleteOperation.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpDeleteOperation.setStatus(_A)
class _FsCapwapClearApStats_Type(EnabledStatus):defaultValue=2
_FsCapwapClearApStats_Type.__name__=_H
_FsCapwapClearApStats_Object=MibTableColumn
fsCapwapClearApStats=_FsCapwapClearApStats_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,8),_FsCapwapClearApStats_Type())
fsCapwapClearApStats.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapClearApStats.setStatus(_A)
_FsCapwapWtpConfigRowStatus_Type=RowStatus
_FsCapwapWtpConfigRowStatus_Object=MibTableColumn
fsCapwapWtpConfigRowStatus=_FsCapwapWtpConfigRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,3,1,9),_FsCapwapWtpConfigRowStatus_Type())
fsCapwapWtpConfigRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapWtpConfigRowStatus.setStatus(_A)
_FsCapwapLinkEncryptionTable_Object=MibTable
fsCapwapLinkEncryptionTable=_FsCapwapLinkEncryptionTable_Object((1,3,6,1,4,1,10876,101,2,82,3,4))
if mibBuilder.loadTexts:fsCapwapLinkEncryptionTable.setStatus(_A)
_FsCapwapLinkEncryptionEntry_Object=MibTableRow
fsCapwapLinkEncryptionEntry=_FsCapwapLinkEncryptionEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,4,1))
fsCapwapLinkEncryptionEntry.setIndexNames((0,_D,_G),(0,_D,_Z))
if mibBuilder.loadTexts:fsCapwapLinkEncryptionEntry.setStatus(_A)
class _FsCapwapEncryptChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('control',1),('data',2)))
_FsCapwapEncryptChannel_Type.__name__=_E
_FsCapwapEncryptChannel_Object=MibTableColumn
fsCapwapEncryptChannel=_FsCapwapEncryptChannel_Object((1,3,6,1,4,1,10876,101,2,82,3,4,1,1),_FsCapwapEncryptChannel_Type())
fsCapwapEncryptChannel.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCapwapEncryptChannel.setStatus(_A)
class _FsCapwapEncryptChannelStatus_Type(EnabledStatus):defaultValue=2
_FsCapwapEncryptChannelStatus_Type.__name__=_H
_FsCapwapEncryptChannelStatus_Object=MibTableColumn
fsCapwapEncryptChannelStatus=_FsCapwapEncryptChannelStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,4,1,2),_FsCapwapEncryptChannelStatus_Type())
fsCapwapEncryptChannelStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapEncryptChannelStatus.setStatus(_A)
_FsCapwapEncryptChannelRowStatus_Type=RowStatus
_FsCapwapEncryptChannelRowStatus_Object=MibTableColumn
fsCapwapEncryptChannelRowStatus=_FsCapwapEncryptChannelRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,4,1,3),_FsCapwapEncryptChannelRowStatus_Type())
fsCapwapEncryptChannelRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapEncryptChannelRowStatus.setStatus(_A)
_FsCapwapDefaultWtpProfileTable_Object=MibTable
fsCapwapDefaultWtpProfileTable=_FsCapwapDefaultWtpProfileTable_Object((1,3,6,1,4,1,10876,101,2,82,3,5))
if mibBuilder.loadTexts:fsCapwapDefaultWtpProfileTable.setStatus(_A)
_FsCapwapDefaultWtpProfileEntry_Object=MibTableRow
fsCapwapDefaultWtpProfileEntry=_FsCapwapDefaultWtpProfileEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,5,1))
fsCapwapDefaultWtpProfileEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fsCapwapDefaultWtpProfileEntry.setStatus(_A)
class _FsCapwapDefaultQosProfile_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(31,31));fixedLength=31
_FsCapwapDefaultQosProfile_Type.__name__=_L
_FsCapwapDefaultQosProfile_Object=MibTableColumn
fsCapwapDefaultQosProfile=_FsCapwapDefaultQosProfile_Object((1,3,6,1,4,1,10876,101,2,82,3,5,1,1),_FsCapwapDefaultQosProfile_Type())
fsCapwapDefaultQosProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDefaultQosProfile.setStatus(_A)
_FsCapwapDefaultWtpProfileRowStatus_Type=RowStatus
_FsCapwapDefaultWtpProfileRowStatus_Object=MibTableColumn
fsCapwapDefaultWtpProfileRowStatus=_FsCapwapDefaultWtpProfileRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,5,1,2),_FsCapwapDefaultWtpProfileRowStatus_Type())
fsCapwapDefaultWtpProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDefaultWtpProfileRowStatus.setStatus(_A)
_FsCapwapDnsProfileTable_Object=MibTable
fsCapwapDnsProfileTable=_FsCapwapDnsProfileTable_Object((1,3,6,1,4,1,10876,101,2,82,3,6))
if mibBuilder.loadTexts:fsCapwapDnsProfileTable.setStatus(_A)
_FsCapwapDnsProfileEntry_Object=MibTableRow
fsCapwapDnsProfileEntry=_FsCapwapDnsProfileEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,6,1))
fsCapwapDnsProfileEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCapwapDnsProfileEntry.setStatus(_A)
class _FsCapwapDnsAddressType_Type(InetAddressType):defaultValue=1
_FsCapwapDnsAddressType_Type.__name__=_S
_FsCapwapDnsAddressType_Object=MibTableColumn
fsCapwapDnsAddressType=_FsCapwapDnsAddressType_Object((1,3,6,1,4,1,10876,101,2,82,3,6,1,1),_FsCapwapDnsAddressType_Type())
fsCapwapDnsAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDnsAddressType.setStatus(_A)
class _FsCapwapDnsServerIp_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_FsCapwapDnsServerIp_Type.__name__=_R
_FsCapwapDnsServerIp_Object=MibTableColumn
fsCapwapDnsServerIp=_FsCapwapDnsServerIp_Object((1,3,6,1,4,1,10876,101,2,82,3,6,1,2),_FsCapwapDnsServerIp_Type())
fsCapwapDnsServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDnsServerIp.setStatus(_A)
class _FsCapwapDnsDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsCapwapDnsDomainName_Type.__name__=_M
_FsCapwapDnsDomainName_Object=MibTableColumn
fsCapwapDnsDomainName=_FsCapwapDnsDomainName_Object((1,3,6,1,4,1,10876,101,2,82,3,6,1,3),_FsCapwapDnsDomainName_Type())
fsCapwapDnsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDnsDomainName.setStatus(_A)
_FsCapwapDnsProfileRowStatus_Type=RowStatus
_FsCapwapDnsProfileRowStatus_Object=MibTableColumn
fsCapwapDnsProfileRowStatus=_FsCapwapDnsProfileRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,6,1,4),_FsCapwapDnsProfileRowStatus_Type())
fsCapwapDnsProfileRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapDnsProfileRowStatus.setStatus(_A)
_FsWtpNativeVlanIdTable_Object=MibTable
fsWtpNativeVlanIdTable=_FsWtpNativeVlanIdTable_Object((1,3,6,1,4,1,10876,101,2,82,3,7))
if mibBuilder.loadTexts:fsWtpNativeVlanIdTable.setStatus(_A)
_FsWtpNativeVlanIdEntry_Object=MibTableRow
fsWtpNativeVlanIdEntry=_FsWtpNativeVlanIdEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,7,1))
fsWtpNativeVlanIdEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsWtpNativeVlanIdEntry.setStatus(_A)
class _FsWtpNativeVlanId_Type(Integer32):defaultValue=0
_FsWtpNativeVlanId_Type.__name__=_E
_FsWtpNativeVlanId_Object=MibTableColumn
fsWtpNativeVlanId=_FsWtpNativeVlanId_Object((1,3,6,1,4,1,10876,101,2,82,3,7,1,1),_FsWtpNativeVlanId_Type())
fsWtpNativeVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWtpNativeVlanId.setStatus(_A)
_FsWtpNativeVlanIdRowStatus_Type=RowStatus
_FsWtpNativeVlanIdRowStatus_Object=MibTableColumn
fsWtpNativeVlanIdRowStatus=_FsWtpNativeVlanIdRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,7,1,2),_FsWtpNativeVlanIdRowStatus_Type())
fsWtpNativeVlanIdRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsWtpNativeVlanIdRowStatus.setStatus(_A)
_FsCawapDiscStatsTable_Object=MibTable
fsCawapDiscStatsTable=_FsCawapDiscStatsTable_Object((1,3,6,1,4,1,10876,101,2,82,3,8))
if mibBuilder.loadTexts:fsCawapDiscStatsTable.setStatus(_A)
_FsCawapDiscStatsEntry_Object=MibTableRow
fsCawapDiscStatsEntry=_FsCawapDiscStatsEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1))
fsCawapDiscStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCawapDiscStatsEntry.setStatus(_A)
class _FsCapwapDiscReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapDiscReqReceived_Type.__name__=_C
_FsCapwapDiscReqReceived_Object=MibTableColumn
fsCapwapDiscReqReceived=_FsCapwapDiscReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,1),_FsCapwapDiscReqReceived_Type())
fsCapwapDiscReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscReqReceived.setStatus(_A)
class _FsCapwapDiscRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapDiscRspReceived_Type.__name__=_C
_FsCapwapDiscRspReceived_Object=MibTableColumn
fsCapwapDiscRspReceived=_FsCapwapDiscRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,2),_FsCapwapDiscRspReceived_Type())
fsCapwapDiscRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscRspReceived.setStatus(_A)
class _FsCapwapDiscReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapDiscReqTransmitted_Type.__name__=_C
_FsCapwapDiscReqTransmitted_Object=MibTableColumn
fsCapwapDiscReqTransmitted=_FsCapwapDiscReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,3),_FsCapwapDiscReqTransmitted_Type())
fsCapwapDiscReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscReqTransmitted.setStatus(_A)
class _FsCapwapDiscRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapDiscRspTransmitted_Type.__name__=_C
_FsCapwapDiscRspTransmitted_Object=MibTableColumn
fsCapwapDiscRspTransmitted=_FsCapwapDiscRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,4),_FsCapwapDiscRspTransmitted_Type())
fsCapwapDiscRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscRspTransmitted.setStatus(_A)
class _FsCapwapDiscunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapDiscunsuccessfulProcessed_Type.__name__=_C
_FsCapwapDiscunsuccessfulProcessed_Object=MibTableColumn
fsCapwapDiscunsuccessfulProcessed=_FsCapwapDiscunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,5),_FsCapwapDiscunsuccessfulProcessed_Type())
fsCapwapDiscunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscunsuccessfulProcessed.setStatus(_A)
class _FsCapwapDiscLastUnsuccAttemptReason_Type(Integer32):defaultValue=0
_FsCapwapDiscLastUnsuccAttemptReason_Type.__name__=_E
_FsCapwapDiscLastUnsuccAttemptReason_Object=MibTableColumn
fsCapwapDiscLastUnsuccAttemptReason=_FsCapwapDiscLastUnsuccAttemptReason_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,6),_FsCapwapDiscLastUnsuccAttemptReason_Type())
fsCapwapDiscLastUnsuccAttemptReason.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscLastUnsuccAttemptReason.setStatus(_A)
_FsCapwapDiscLastSuccAttemptTime_Type=TimeTicks
_FsCapwapDiscLastSuccAttemptTime_Object=MibTableColumn
fsCapwapDiscLastSuccAttemptTime=_FsCapwapDiscLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,7),_FsCapwapDiscLastSuccAttemptTime_Type())
fsCapwapDiscLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscLastSuccAttemptTime.setStatus(_A)
_FsCapwapDiscLastUnsuccessfulAttemptTime_Type=TimeTicks
_FsCapwapDiscLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapDiscLastUnsuccessfulAttemptTime=_FsCapwapDiscLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,8),_FsCapwapDiscLastUnsuccessfulAttemptTime_Type())
fsCapwapDiscLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscLastUnsuccessfulAttemptTime.setStatus(_A)
_FsCapwapDiscStatsRowStatus_Type=RowStatus
_FsCapwapDiscStatsRowStatus_Object=MibTableColumn
fsCapwapDiscStatsRowStatus=_FsCapwapDiscStatsRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,8,1,9),_FsCapwapDiscStatsRowStatus_Type())
fsCapwapDiscStatsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapDiscStatsRowStatus.setStatus(_A)
_FsCawapJoinStatsTable_Object=MibTable
fsCawapJoinStatsTable=_FsCawapJoinStatsTable_Object((1,3,6,1,4,1,10876,101,2,82,3,9))
if mibBuilder.loadTexts:fsCawapJoinStatsTable.setStatus(_A)
_FsCawapJoinStatsEntry_Object=MibTableRow
fsCawapJoinStatsEntry=_FsCawapJoinStatsEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1))
fsCawapJoinStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCawapJoinStatsEntry.setStatus(_A)
class _FsCapwapJoinReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapJoinReqReceived_Type.__name__=_C
_FsCapwapJoinReqReceived_Object=MibTableColumn
fsCapwapJoinReqReceived=_FsCapwapJoinReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,1),_FsCapwapJoinReqReceived_Type())
fsCapwapJoinReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinReqReceived.setStatus(_A)
class _FsCapwapJoinRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapJoinRspReceived_Type.__name__=_C
_FsCapwapJoinRspReceived_Object=MibTableColumn
fsCapwapJoinRspReceived=_FsCapwapJoinRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,2),_FsCapwapJoinRspReceived_Type())
fsCapwapJoinRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinRspReceived.setStatus(_A)
class _FsCapwapJoinReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapJoinReqTransmitted_Type.__name__=_C
_FsCapwapJoinReqTransmitted_Object=MibTableColumn
fsCapwapJoinReqTransmitted=_FsCapwapJoinReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,3),_FsCapwapJoinReqTransmitted_Type())
fsCapwapJoinReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinReqTransmitted.setStatus(_A)
class _FsCapwapJoinRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapJoinRspTransmitted_Type.__name__=_C
_FsCapwapJoinRspTransmitted_Object=MibTableColumn
fsCapwapJoinRspTransmitted=_FsCapwapJoinRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,4),_FsCapwapJoinRspTransmitted_Type())
fsCapwapJoinRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinRspTransmitted.setStatus(_A)
class _FsCapwapJoinunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapJoinunsuccessfulProcessed_Type.__name__=_C
_FsCapwapJoinunsuccessfulProcessed_Object=MibTableColumn
fsCapwapJoinunsuccessfulProcessed=_FsCapwapJoinunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,5),_FsCapwapJoinunsuccessfulProcessed_Type())
fsCapwapJoinunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinunsuccessfulProcessed.setStatus(_A)
class _FsCapwapJoinReasonLastUnsuccAttempt_Type(Integer32):defaultValue=0
_FsCapwapJoinReasonLastUnsuccAttempt_Type.__name__=_E
_FsCapwapJoinReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapJoinReasonLastUnsuccAttempt=_FsCapwapJoinReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,6),_FsCapwapJoinReasonLastUnsuccAttempt_Type())
fsCapwapJoinReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapJoinLastSuccAttemptTime_Type=TimeTicks
_FsCapwapJoinLastSuccAttemptTime_Object=MibTableColumn
fsCapwapJoinLastSuccAttemptTime=_FsCapwapJoinLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,7),_FsCapwapJoinLastSuccAttemptTime_Type())
fsCapwapJoinLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinLastSuccAttemptTime.setStatus(_A)
_FsCapwapJoinLastUnsuccAttemptTime_Type=TimeTicks
_FsCapwapJoinLastUnsuccAttemptTime_Object=MibTableColumn
fsCapwapJoinLastUnsuccAttemptTime=_FsCapwapJoinLastUnsuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,8),_FsCapwapJoinLastUnsuccAttemptTime_Type())
fsCapwapJoinLastUnsuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinLastUnsuccAttemptTime.setStatus(_A)
_FsCapwapJoinStatsRowStatus_Type=RowStatus
_FsCapwapJoinStatsRowStatus_Object=MibTableColumn
fsCapwapJoinStatsRowStatus=_FsCapwapJoinStatsRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,9,1,9),_FsCapwapJoinStatsRowStatus_Type())
fsCapwapJoinStatsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapJoinStatsRowStatus.setStatus(_A)
_FsCawapConfigStatsTable_Object=MibTable
fsCawapConfigStatsTable=_FsCawapConfigStatsTable_Object((1,3,6,1,4,1,10876,101,2,82,3,10))
if mibBuilder.loadTexts:fsCawapConfigStatsTable.setStatus(_A)
_FsCawapConfigStatsEntry_Object=MibTableRow
fsCawapConfigStatsEntry=_FsCawapConfigStatsEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1))
fsCawapConfigStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCawapConfigStatsEntry.setStatus(_A)
class _FsCapwapConfigReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapConfigReqReceived_Type.__name__=_C
_FsCapwapConfigReqReceived_Object=MibTableColumn
fsCapwapConfigReqReceived=_FsCapwapConfigReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,1),_FsCapwapConfigReqReceived_Type())
fsCapwapConfigReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigReqReceived.setStatus(_A)
class _FsCapwapConfigRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapConfigRspReceived_Type.__name__=_C
_FsCapwapConfigRspReceived_Object=MibTableColumn
fsCapwapConfigRspReceived=_FsCapwapConfigRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,2),_FsCapwapConfigRspReceived_Type())
fsCapwapConfigRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigRspReceived.setStatus(_A)
class _FsCapwapConfigReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapConfigReqTransmitted_Type.__name__=_C
_FsCapwapConfigReqTransmitted_Object=MibTableColumn
fsCapwapConfigReqTransmitted=_FsCapwapConfigReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,3),_FsCapwapConfigReqTransmitted_Type())
fsCapwapConfigReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigReqTransmitted.setStatus(_A)
class _FsCapwapConfigRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapConfigRspTransmitted_Type.__name__=_C
_FsCapwapConfigRspTransmitted_Object=MibTableColumn
fsCapwapConfigRspTransmitted=_FsCapwapConfigRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,4),_FsCapwapConfigRspTransmitted_Type())
fsCapwapConfigRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigRspTransmitted.setStatus(_A)
class _FsCapwapConfigunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapConfigunsuccessfulProcessed_Type.__name__=_C
_FsCapwapConfigunsuccessfulProcessed_Object=MibTableColumn
fsCapwapConfigunsuccessfulProcessed=_FsCapwapConfigunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,5),_FsCapwapConfigunsuccessfulProcessed_Type())
fsCapwapConfigunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigunsuccessfulProcessed.setStatus(_A)
class _FsCapwapConfigReasonLastUnsuccAttempt_Type(Integer32):defaultValue=0
_FsCapwapConfigReasonLastUnsuccAttempt_Type.__name__=_E
_FsCapwapConfigReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapConfigReasonLastUnsuccAttempt=_FsCapwapConfigReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,6),_FsCapwapConfigReasonLastUnsuccAttempt_Type())
fsCapwapConfigReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapConfigLastSuccAttemptTime_Type=TimeTicks
_FsCapwapConfigLastSuccAttemptTime_Object=MibTableColumn
fsCapwapConfigLastSuccAttemptTime=_FsCapwapConfigLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,7),_FsCapwapConfigLastSuccAttemptTime_Type())
fsCapwapConfigLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigLastSuccAttemptTime.setStatus(_A)
_FsCapwapConfigLastUnsuccessfulAttemptTime_Type=TimeTicks
_FsCapwapConfigLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapConfigLastUnsuccessfulAttemptTime=_FsCapwapConfigLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,8),_FsCapwapConfigLastUnsuccessfulAttemptTime_Type())
fsCapwapConfigLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigLastUnsuccessfulAttemptTime.setStatus(_A)
_FsCapwapConfigStatsRowStatus_Type=RowStatus
_FsCapwapConfigStatsRowStatus_Object=MibTableColumn
fsCapwapConfigStatsRowStatus=_FsCapwapConfigStatsRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,10,1,9),_FsCapwapConfigStatsRowStatus_Type())
fsCapwapConfigStatsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapConfigStatsRowStatus.setStatus(_A)
_FsCawapRunStatsTable_Object=MibTable
fsCawapRunStatsTable=_FsCawapRunStatsTable_Object((1,3,6,1,4,1,10876,101,2,82,3,11))
if mibBuilder.loadTexts:fsCawapRunStatsTable.setStatus(_A)
_FsCawapRunStatsEntry_Object=MibTableRow
fsCawapRunStatsEntry=_FsCawapRunStatsEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1))
fsCawapRunStatsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCawapRunStatsEntry.setStatus(_A)
class _FsCapwapRunConfigUpdateReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunConfigUpdateReqReceived_Type.__name__=_C
_FsCapwapRunConfigUpdateReqReceived_Object=MibTableColumn
fsCapwapRunConfigUpdateReqReceived=_FsCapwapRunConfigUpdateReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,1),_FsCapwapRunConfigUpdateReqReceived_Type())
fsCapwapRunConfigUpdateReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateReqReceived.setStatus(_A)
class _FsCapwapRunConfigUpdateRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunConfigUpdateRspReceived_Type.__name__=_C
_FsCapwapRunConfigUpdateRspReceived_Object=MibTableColumn
fsCapwapRunConfigUpdateRspReceived=_FsCapwapRunConfigUpdateRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,2),_FsCapwapRunConfigUpdateRspReceived_Type())
fsCapwapRunConfigUpdateRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateRspReceived.setStatus(_A)
class _FsCapwapRunConfigUpdateReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunConfigUpdateReqTransmitted_Type.__name__=_C
_FsCapwapRunConfigUpdateReqTransmitted_Object=MibTableColumn
fsCapwapRunConfigUpdateReqTransmitted=_FsCapwapRunConfigUpdateReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,3),_FsCapwapRunConfigUpdateReqTransmitted_Type())
fsCapwapRunConfigUpdateReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateReqTransmitted.setStatus(_A)
class _FsCapwapRunConfigUpdateRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunConfigUpdateRspTransmitted_Type.__name__=_C
_FsCapwapRunConfigUpdateRspTransmitted_Object=MibTableColumn
fsCapwapRunConfigUpdateRspTransmitted=_FsCapwapRunConfigUpdateRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,4),_FsCapwapRunConfigUpdateRspTransmitted_Type())
fsCapwapRunConfigUpdateRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateRspTransmitted.setStatus(_A)
class _FsCapwapRunConfigUpdateunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunConfigUpdateunsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunConfigUpdateunsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunConfigUpdateunsuccessfulProcessed=_FsCapwapRunConfigUpdateunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,5),_FsCapwapRunConfigUpdateunsuccessfulProcessed_Type())
fsCapwapRunConfigUpdateunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateunsuccessfulProcessed.setStatus(_A)
_FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunConfigUpdateReasonLastUnsuccAttempt=_FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,6),_FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Type())
fsCapwapRunConfigUpdateReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunConfigUpdateLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunConfigUpdateLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunConfigUpdateLastSuccAttemptTime=_FsCapwapRunConfigUpdateLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,7),_FsCapwapRunConfigUpdateLastSuccAttemptTime_Type())
fsCapwapRunConfigUpdateLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime=_FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,8),_FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Type())
fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime.setStatus(_A)
class _FsCapwapRunStationConfigReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunStationConfigReqReceived_Type.__name__=_C
_FsCapwapRunStationConfigReqReceived_Object=MibTableColumn
fsCapwapRunStationConfigReqReceived=_FsCapwapRunStationConfigReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,9),_FsCapwapRunStationConfigReqReceived_Type())
fsCapwapRunStationConfigReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigReqReceived.setStatus(_A)
class _FsCapwapRunStationConfigRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunStationConfigRspReceived_Type.__name__=_C
_FsCapwapRunStationConfigRspReceived_Object=MibTableColumn
fsCapwapRunStationConfigRspReceived=_FsCapwapRunStationConfigRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,10),_FsCapwapRunStationConfigRspReceived_Type())
fsCapwapRunStationConfigRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigRspReceived.setStatus(_A)
class _FsCapwapRunStationConfigReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunStationConfigReqTransmitted_Type.__name__=_C
_FsCapwapRunStationConfigReqTransmitted_Object=MibTableColumn
fsCapwapRunStationConfigReqTransmitted=_FsCapwapRunStationConfigReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,11),_FsCapwapRunStationConfigReqTransmitted_Type())
fsCapwapRunStationConfigReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigReqTransmitted.setStatus(_A)
class _FsCapwapRunStationConfigRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunStationConfigRspTransmitted_Type.__name__=_C
_FsCapwapRunStationConfigRspTransmitted_Object=MibTableColumn
fsCapwapRunStationConfigRspTransmitted=_FsCapwapRunStationConfigRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,12),_FsCapwapRunStationConfigRspTransmitted_Type())
fsCapwapRunStationConfigRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigRspTransmitted.setStatus(_A)
class _FsCapwapRunStationConfigunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunStationConfigunsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunStationConfigunsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunStationConfigunsuccessfulProcessed=_FsCapwapRunStationConfigunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,13),_FsCapwapRunStationConfigunsuccessfulProcessed_Type())
fsCapwapRunStationConfigunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigunsuccessfulProcessed.setStatus(_A)
_FsCapwapRunStationConfigReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunStationConfigReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunStationConfigReasonLastUnsuccAttempt=_FsCapwapRunStationConfigReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,14),_FsCapwapRunStationConfigReasonLastUnsuccAttempt_Type())
fsCapwapRunStationConfigReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunStationConfigLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunStationConfigLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunStationConfigLastSuccAttemptTime=_FsCapwapRunStationConfigLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,15),_FsCapwapRunStationConfigLastSuccAttemptTime_Type())
fsCapwapRunStationConfigLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunStationConfigLastUnsuccessfulAttemptTime=_FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,16),_FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Type())
fsCapwapRunStationConfigLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStationConfigLastUnsuccessfulAttemptTime.setStatus(_A)
class _FsCapwapRunClearConfigReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunClearConfigReqReceived_Type.__name__=_C
_FsCapwapRunClearConfigReqReceived_Object=MibTableColumn
fsCapwapRunClearConfigReqReceived=_FsCapwapRunClearConfigReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,17),_FsCapwapRunClearConfigReqReceived_Type())
fsCapwapRunClearConfigReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigReqReceived.setStatus(_A)
class _FsCapwapRunClearConfigRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunClearConfigRspReceived_Type.__name__=_C
_FsCapwapRunClearConfigRspReceived_Object=MibTableColumn
fsCapwapRunClearConfigRspReceived=_FsCapwapRunClearConfigRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,18),_FsCapwapRunClearConfigRspReceived_Type())
fsCapwapRunClearConfigRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigRspReceived.setStatus(_A)
class _FsCapwapRunClearConfigReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunClearConfigReqTransmitted_Type.__name__=_C
_FsCapwapRunClearConfigReqTransmitted_Object=MibTableColumn
fsCapwapRunClearConfigReqTransmitted=_FsCapwapRunClearConfigReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,19),_FsCapwapRunClearConfigReqTransmitted_Type())
fsCapwapRunClearConfigReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigReqTransmitted.setStatus(_A)
class _FsCapwapRunClearConfigRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunClearConfigRspTransmitted_Type.__name__=_C
_FsCapwapRunClearConfigRspTransmitted_Object=MibTableColumn
fsCapwapRunClearConfigRspTransmitted=_FsCapwapRunClearConfigRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,20),_FsCapwapRunClearConfigRspTransmitted_Type())
fsCapwapRunClearConfigRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigRspTransmitted.setStatus(_A)
class _FsCapwapRunClearConfigunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunClearConfigunsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunClearConfigunsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunClearConfigunsuccessfulProcessed=_FsCapwapRunClearConfigunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,21),_FsCapwapRunClearConfigunsuccessfulProcessed_Type())
fsCapwapRunClearConfigunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigunsuccessfulProcessed.setStatus(_A)
_FsCapwapRunClearConfigReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunClearConfigReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunClearConfigReasonLastUnsuccAttempt=_FsCapwapRunClearConfigReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,22),_FsCapwapRunClearConfigReasonLastUnsuccAttempt_Type())
fsCapwapRunClearConfigReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunClearConfigLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunClearConfigLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunClearConfigLastSuccAttemptTime=_FsCapwapRunClearConfigLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,23),_FsCapwapRunClearConfigLastSuccAttemptTime_Type())
fsCapwapRunClearConfigLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunClearConfigLastUnsuccessfulAttemptTime=_FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,24),_FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Type())
fsCapwapRunClearConfigLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunClearConfigLastUnsuccessfulAttemptTime.setStatus(_A)
class _FsCapwapRunDataTransferReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunDataTransferReqReceived_Type.__name__=_C
_FsCapwapRunDataTransferReqReceived_Object=MibTableColumn
fsCapwapRunDataTransferReqReceived=_FsCapwapRunDataTransferReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,25),_FsCapwapRunDataTransferReqReceived_Type())
fsCapwapRunDataTransferReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferReqReceived.setStatus(_A)
class _FsCapwapRunDataTransferRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunDataTransferRspReceived_Type.__name__=_C
_FsCapwapRunDataTransferRspReceived_Object=MibTableColumn
fsCapwapRunDataTransferRspReceived=_FsCapwapRunDataTransferRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,26),_FsCapwapRunDataTransferRspReceived_Type())
fsCapwapRunDataTransferRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferRspReceived.setStatus(_A)
class _FsCapwapRunDataTransferReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunDataTransferReqTransmitted_Type.__name__=_C
_FsCapwapRunDataTransferReqTransmitted_Object=MibTableColumn
fsCapwapRunDataTransferReqTransmitted=_FsCapwapRunDataTransferReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,27),_FsCapwapRunDataTransferReqTransmitted_Type())
fsCapwapRunDataTransferReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferReqTransmitted.setStatus(_A)
class _FsCapwapRunDataTransferRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunDataTransferRspTransmitted_Type.__name__=_C
_FsCapwapRunDataTransferRspTransmitted_Object=MibTableColumn
fsCapwapRunDataTransferRspTransmitted=_FsCapwapRunDataTransferRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,28),_FsCapwapRunDataTransferRspTransmitted_Type())
fsCapwapRunDataTransferRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferRspTransmitted.setStatus(_A)
class _FsCapwapRunDataTransferunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunDataTransferunsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunDataTransferunsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunDataTransferunsuccessfulProcessed=_FsCapwapRunDataTransferunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,29),_FsCapwapRunDataTransferunsuccessfulProcessed_Type())
fsCapwapRunDataTransferunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferunsuccessfulProcessed.setStatus(_A)
_FsCapwapRunDataTransferReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunDataTransferReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunDataTransferReasonLastUnsuccAttempt=_FsCapwapRunDataTransferReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,30),_FsCapwapRunDataTransferReasonLastUnsuccAttempt_Type())
fsCapwapRunDataTransferReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunDataTransferLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunDataTransferLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunDataTransferLastSuccAttemptTime=_FsCapwapRunDataTransferLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,31),_FsCapwapRunDataTransferLastSuccAttemptTime_Type())
fsCapwapRunDataTransferLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunDataTransferLastUnsuccessfulAttemptTime=_FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,32),_FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Type())
fsCapwapRunDataTransferLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunDataTransferLastUnsuccessfulAttemptTime.setStatus(_A)
class _FsCapwapRunResetReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunResetReqReceived_Type.__name__=_C
_FsCapwapRunResetReqReceived_Object=MibTableColumn
fsCapwapRunResetReqReceived=_FsCapwapRunResetReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,33),_FsCapwapRunResetReqReceived_Type())
fsCapwapRunResetReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetReqReceived.setStatus(_A)
class _FsCapwapRunResetRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunResetRspReceived_Type.__name__=_C
_FsCapwapRunResetRspReceived_Object=MibTableColumn
fsCapwapRunResetRspReceived=_FsCapwapRunResetRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,34),_FsCapwapRunResetRspReceived_Type())
fsCapwapRunResetRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetRspReceived.setStatus(_A)
class _FsCapwapRunResetReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunResetReqTransmitted_Type.__name__=_C
_FsCapwapRunResetReqTransmitted_Object=MibTableColumn
fsCapwapRunResetReqTransmitted=_FsCapwapRunResetReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,35),_FsCapwapRunResetReqTransmitted_Type())
fsCapwapRunResetReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetReqTransmitted.setStatus(_A)
class _FsCapwapRunResetRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunResetRspTransmitted_Type.__name__=_C
_FsCapwapRunResetRspTransmitted_Object=MibTableColumn
fsCapwapRunResetRspTransmitted=_FsCapwapRunResetRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,36),_FsCapwapRunResetRspTransmitted_Type())
fsCapwapRunResetRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetRspTransmitted.setStatus(_A)
class _FsCapwapRunResetunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunResetunsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunResetunsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunResetunsuccessfulProcessed=_FsCapwapRunResetunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,37),_FsCapwapRunResetunsuccessfulProcessed_Type())
fsCapwapRunResetunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetunsuccessfulProcessed.setStatus(_A)
_FsCapwapRunResetReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunResetReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunResetReasonLastUnsuccAttempt=_FsCapwapRunResetReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,38),_FsCapwapRunResetReasonLastUnsuccAttempt_Type())
fsCapwapRunResetReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunResetLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunResetLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunResetLastSuccAttemptTime=_FsCapwapRunResetLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,39),_FsCapwapRunResetLastSuccAttemptTime_Type())
fsCapwapRunResetLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunResetLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunResetLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunResetLastUnsuccessfulAttemptTime=_FsCapwapRunResetLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,40),_FsCapwapRunResetLastUnsuccessfulAttemptTime_Type())
fsCapwapRunResetLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunResetLastUnsuccessfulAttemptTime.setStatus(_A)
class _FsCapwapRunPriDiscReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunPriDiscReqReceived_Type.__name__=_C
_FsCapwapRunPriDiscReqReceived_Object=MibTableColumn
fsCapwapRunPriDiscReqReceived=_FsCapwapRunPriDiscReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,41),_FsCapwapRunPriDiscReqReceived_Type())
fsCapwapRunPriDiscReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscReqReceived.setStatus(_A)
class _FsCapwapRunPriDiscRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunPriDiscRspReceived_Type.__name__=_C
_FsCapwapRunPriDiscRspReceived_Object=MibTableColumn
fsCapwapRunPriDiscRspReceived=_FsCapwapRunPriDiscRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,42),_FsCapwapRunPriDiscRspReceived_Type())
fsCapwapRunPriDiscRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscRspReceived.setStatus(_A)
class _FsCapwapRunPriDiscReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunPriDiscReqTransmitted_Type.__name__=_C
_FsCapwapRunPriDiscReqTransmitted_Object=MibTableColumn
fsCapwapRunPriDiscReqTransmitted=_FsCapwapRunPriDiscReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,43),_FsCapwapRunPriDiscReqTransmitted_Type())
fsCapwapRunPriDiscReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscReqTransmitted.setStatus(_A)
class _FsCapwapRunPriDiscRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunPriDiscRspTransmitted_Type.__name__=_C
_FsCapwapRunPriDiscRspTransmitted_Object=MibTableColumn
fsCapwapRunPriDiscRspTransmitted=_FsCapwapRunPriDiscRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,44),_FsCapwapRunPriDiscRspTransmitted_Type())
fsCapwapRunPriDiscRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscRspTransmitted.setStatus(_A)
class _FsCapwapRunPriDiscunsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunPriDiscunsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunPriDiscunsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunPriDiscunsuccessfulProcessed=_FsCapwapRunPriDiscunsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,45),_FsCapwapRunPriDiscunsuccessfulProcessed_Type())
fsCapwapRunPriDiscunsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscunsuccessfulProcessed.setStatus(_A)
_FsCapwapRunPriDiscReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunPriDiscReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunPriDiscReasonLastUnsuccAttempt=_FsCapwapRunPriDiscReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,46),_FsCapwapRunPriDiscReasonLastUnsuccAttempt_Type())
fsCapwapRunPriDiscReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunPriDiscLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunPriDiscLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunPriDiscLastSuccAttemptTime=_FsCapwapRunPriDiscLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,47),_FsCapwapRunPriDiscLastSuccAttemptTime_Type())
fsCapwapRunPriDiscLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunPriDiscLastUnsuccessfulAttemptTime=_FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,48),_FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Type())
fsCapwapRunPriDiscLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunPriDiscLastUnsuccessfulAttemptTime.setStatus(_A)
class _FsCapwapRunEchoReqReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunEchoReqReceived_Type.__name__=_C
_FsCapwapRunEchoReqReceived_Object=MibTableColumn
fsCapwapRunEchoReqReceived=_FsCapwapRunEchoReqReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,49),_FsCapwapRunEchoReqReceived_Type())
fsCapwapRunEchoReqReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoReqReceived.setStatus(_A)
class _FsCapwapRunEchoRspReceived_Type(Unsigned32):defaultValue=0
_FsCapwapRunEchoRspReceived_Type.__name__=_C
_FsCapwapRunEchoRspReceived_Object=MibTableColumn
fsCapwapRunEchoRspReceived=_FsCapwapRunEchoRspReceived_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,50),_FsCapwapRunEchoRspReceived_Type())
fsCapwapRunEchoRspReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoRspReceived.setStatus(_A)
class _FsCapwapRunEchoReqTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunEchoReqTransmitted_Type.__name__=_C
_FsCapwapRunEchoReqTransmitted_Object=MibTableColumn
fsCapwapRunEchoReqTransmitted=_FsCapwapRunEchoReqTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,51),_FsCapwapRunEchoReqTransmitted_Type())
fsCapwapRunEchoReqTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoReqTransmitted.setStatus(_A)
class _FsCapwapRunEchoRspTransmitted_Type(Unsigned32):defaultValue=0
_FsCapwapRunEchoRspTransmitted_Type.__name__=_C
_FsCapwapRunEchoRspTransmitted_Object=MibTableColumn
fsCapwapRunEchoRspTransmitted=_FsCapwapRunEchoRspTransmitted_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,52),_FsCapwapRunEchoRspTransmitted_Type())
fsCapwapRunEchoRspTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoRspTransmitted.setStatus(_A)
class _FsCapwapRunEchounsuccessfulProcessed_Type(Unsigned32):defaultValue=0
_FsCapwapRunEchounsuccessfulProcessed_Type.__name__=_C
_FsCapwapRunEchounsuccessfulProcessed_Object=MibTableColumn
fsCapwapRunEchounsuccessfulProcessed=_FsCapwapRunEchounsuccessfulProcessed_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,53),_FsCapwapRunEchounsuccessfulProcessed_Type())
fsCapwapRunEchounsuccessfulProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchounsuccessfulProcessed.setStatus(_A)
_FsCapwapRunEchoReasonLastUnsuccAttempt_Type=SnmpAdminString
_FsCapwapRunEchoReasonLastUnsuccAttempt_Object=MibTableColumn
fsCapwapRunEchoReasonLastUnsuccAttempt=_FsCapwapRunEchoReasonLastUnsuccAttempt_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,54),_FsCapwapRunEchoReasonLastUnsuccAttempt_Type())
fsCapwapRunEchoReasonLastUnsuccAttempt.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoReasonLastUnsuccAttempt.setStatus(_A)
_FsCapwapRunEchoLastSuccAttemptTime_Type=DateAndTime
_FsCapwapRunEchoLastSuccAttemptTime_Object=MibTableColumn
fsCapwapRunEchoLastSuccAttemptTime=_FsCapwapRunEchoLastSuccAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,55),_FsCapwapRunEchoLastSuccAttemptTime_Type())
fsCapwapRunEchoLastSuccAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoLastSuccAttemptTime.setStatus(_A)
_FsCapwapRunEchoLastUnsuccessfulAttemptTime_Type=DateAndTime
_FsCapwapRunEchoLastUnsuccessfulAttemptTime_Object=MibTableColumn
fsCapwapRunEchoLastUnsuccessfulAttemptTime=_FsCapwapRunEchoLastUnsuccessfulAttemptTime_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,56),_FsCapwapRunEchoLastUnsuccessfulAttemptTime_Type())
fsCapwapRunEchoLastUnsuccessfulAttemptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunEchoLastUnsuccessfulAttemptTime.setStatus(_A)
_FsCapwapRunStatsRowStatus_Type=RowStatus
_FsCapwapRunStatsRowStatus_Object=MibTableColumn
fsCapwapRunStatsRowStatus=_FsCapwapRunStatsRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,11,1,57),_FsCapwapRunStatsRowStatus_Type())
fsCapwapRunStatsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapRunStatsRowStatus.setStatus(_A)
_FsCapwapWirelessBindingTable_Object=MibTable
fsCapwapWirelessBindingTable=_FsCapwapWirelessBindingTable_Object((1,3,6,1,4,1,10876,101,2,82,3,12))
if mibBuilder.loadTexts:fsCapwapWirelessBindingTable.setStatus(_A)
_FsCapwapWirelessBindingEntry_Object=MibTableRow
fsCapwapWirelessBindingEntry=_FsCapwapWirelessBindingEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,12,1))
fsCapwapWirelessBindingEntry.setIndexNames((0,_D,_G),(0,_D,'capwapBaseWirelessBindingRadioId'))
if mibBuilder.loadTexts:fsCapwapWirelessBindingEntry.setStatus(_A)
_FsCapwapWirelessBindingVirtualRadioIfIndex_Type=InterfaceIndex
_FsCapwapWirelessBindingVirtualRadioIfIndex_Object=MibTableColumn
fsCapwapWirelessBindingVirtualRadioIfIndex=_FsCapwapWirelessBindingVirtualRadioIfIndex_Object((1,3,6,1,4,1,10876,101,2,82,3,12,1,1),_FsCapwapWirelessBindingVirtualRadioIfIndex_Type())
fsCapwapWirelessBindingVirtualRadioIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWirelessBindingVirtualRadioIfIndex.setStatus(_A)
class _FsCapwapWirelessBindingType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*(('dot11',1),('epc',3)))
_FsCapwapWirelessBindingType_Type.__name__=_E
_FsCapwapWirelessBindingType_Object=MibTableColumn
fsCapwapWirelessBindingType=_FsCapwapWirelessBindingType_Object((1,3,6,1,4,1,10876,101,2,82,3,12,1,2),_FsCapwapWirelessBindingType_Type())
fsCapwapWirelessBindingType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWirelessBindingType.setStatus(_A)
_FsCapwapWirelessBindingRowStatus_Type=RowStatus
_FsCapwapWirelessBindingRowStatus_Object=MibTableColumn
fsCapwapWirelessBindingRowStatus=_FsCapwapWirelessBindingRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,12,1,3),_FsCapwapWirelessBindingRowStatus_Type())
fsCapwapWirelessBindingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWirelessBindingRowStatus.setStatus(_A)
_FsCapwapStationWhiteListTable_Object=MibTable
fsCapwapStationWhiteListTable=_FsCapwapStationWhiteListTable_Object((1,3,6,1,4,1,10876,101,2,82,3,13))
if mibBuilder.loadTexts:fsCapwapStationWhiteListTable.setStatus(_A)
_FsCapwapStationWhiteListEntry_Object=MibTableRow
fsCapwapStationWhiteListEntry=_FsCapwapStationWhiteListEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,13,1))
fsCapwapStationWhiteListEntry.setIndexNames((0,_D,_a))
if mibBuilder.loadTexts:fsCapwapStationWhiteListEntry.setStatus(_A)
_FsCapwapStationWhiteListId_Type=Unsigned32
_FsCapwapStationWhiteListId_Object=MibTableColumn
fsCapwapStationWhiteListId=_FsCapwapStationWhiteListId_Object((1,3,6,1,4,1,10876,101,2,82,3,13,1,1),_FsCapwapStationWhiteListId_Type())
fsCapwapStationWhiteListId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsCapwapStationWhiteListId.setStatus(_A)
_FsCapwapStationWhiteListStationId_Type=CapwapBaseStationIdTC
_FsCapwapStationWhiteListStationId_Object=MibTableColumn
fsCapwapStationWhiteListStationId=_FsCapwapStationWhiteListStationId_Object((1,3,6,1,4,1,10876,101,2,82,3,13,1,2),_FsCapwapStationWhiteListStationId_Type())
fsCapwapStationWhiteListStationId.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapStationWhiteListStationId.setStatus(_A)
_FsCapwapStationWhiteListRowStatus_Type=RowStatus
_FsCapwapStationWhiteListRowStatus_Object=MibTableColumn
fsCapwapStationWhiteListRowStatus=_FsCapwapStationWhiteListRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,13,1,3),_FsCapwapStationWhiteListRowStatus_Type())
fsCapwapStationWhiteListRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapStationWhiteListRowStatus.setStatus(_A)
_FsCapwapWtpRebootStatisticsTable_Object=MibTable
fsCapwapWtpRebootStatisticsTable=_FsCapwapWtpRebootStatisticsTable_Object((1,3,6,1,4,1,10876,101,2,82,3,14))
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsTable.setStatus(_A)
_FsCapwapWtpRebootStatisticsEntry_Object=MibTableRow
fsCapwapWtpRebootStatisticsEntry=_FsCapwapWtpRebootStatisticsEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1))
fsCapwapWtpRebootStatisticsEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsEntry.setStatus(_A)
class _FsCapwapWtpRebootStatisticsRebootCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsRebootCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsRebootCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsRebootCount=_FsCapwapWtpRebootStatisticsRebootCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,1),_FsCapwapWtpRebootStatisticsRebootCount_Type())
fsCapwapWtpRebootStatisticsRebootCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsRebootCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsAcInitiatedCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsAcInitiatedCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsAcInitiatedCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsAcInitiatedCount=_FsCapwapWtpRebootStatisticsAcInitiatedCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,2),_FsCapwapWtpRebootStatisticsAcInitiatedCount_Type())
fsCapwapWtpRebootStatisticsAcInitiatedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsAcInitiatedCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsLinkFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsLinkFailureCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsLinkFailureCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsLinkFailureCount=_FsCapwapWtpRebootStatisticsLinkFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,3),_FsCapwapWtpRebootStatisticsLinkFailureCount_Type())
fsCapwapWtpRebootStatisticsLinkFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsLinkFailureCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsSwFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsSwFailureCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsSwFailureCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsSwFailureCount=_FsCapwapWtpRebootStatisticsSwFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,4),_FsCapwapWtpRebootStatisticsSwFailureCount_Type())
fsCapwapWtpRebootStatisticsSwFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsSwFailureCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsHwFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsHwFailureCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsHwFailureCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsHwFailureCount=_FsCapwapWtpRebootStatisticsHwFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,5),_FsCapwapWtpRebootStatisticsHwFailureCount_Type())
fsCapwapWtpRebootStatisticsHwFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsHwFailureCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsOtherFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsOtherFailureCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsOtherFailureCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsOtherFailureCount=_FsCapwapWtpRebootStatisticsOtherFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,6),_FsCapwapWtpRebootStatisticsOtherFailureCount_Type())
fsCapwapWtpRebootStatisticsOtherFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsOtherFailureCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsUnknownFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRebootStatisticsUnknownFailureCount_Type.__name__=_C
_FsCapwapWtpRebootStatisticsUnknownFailureCount_Object=MibTableColumn
fsCapwapWtpRebootStatisticsUnknownFailureCount=_FsCapwapWtpRebootStatisticsUnknownFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,7),_FsCapwapWtpRebootStatisticsUnknownFailureCount_Type())
fsCapwapWtpRebootStatisticsUnknownFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsUnknownFailureCount.setStatus(_A)
class _FsCapwapWtpRebootStatisticsLastFailureType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,255)));namedValues=NamedValues(*(('notSupported',0),('aCInitiated',1),('linkFailure',2),(_b,3),(_c,4),(_d,5),(_e,255)))
_FsCapwapWtpRebootStatisticsLastFailureType_Type.__name__=_E
_FsCapwapWtpRebootStatisticsLastFailureType_Object=MibTableColumn
fsCapwapWtpRebootStatisticsLastFailureType=_FsCapwapWtpRebootStatisticsLastFailureType_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,8),_FsCapwapWtpRebootStatisticsLastFailureType_Type())
fsCapwapWtpRebootStatisticsLastFailureType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsLastFailureType.setStatus(_A)
_FsCapwapWtpRebootStatisticsRowStatus_Type=RowStatus
_FsCapwapWtpRebootStatisticsRowStatus_Object=MibTableColumn
fsCapwapWtpRebootStatisticsRowStatus=_FsCapwapWtpRebootStatisticsRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,14,1,9),_FsCapwapWtpRebootStatisticsRowStatus_Type())
fsCapwapWtpRebootStatisticsRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsCapwapWtpRebootStatisticsRowStatus.setStatus(_A)
_FsCapwapWtpRadioStatisticsTable_Object=MibTable
fsCapwapWtpRadioStatisticsTable=_FsCapwapWtpRadioStatisticsTable_Object((1,3,6,1,4,1,10876,101,2,82,3,15))
if mibBuilder.loadTexts:fsCapwapWtpRadioStatisticsTable.setStatus(_A)
_FsCapwapWtpRadioStatisticsEntry_Object=MibTableRow
fsCapwapWtpRadioStatisticsEntry=_FsCapwapWtpRadioStatisticsEntry_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1))
fsCapwapWtpRadioStatisticsEntry.setIndexNames((0,_P,_Q))
if mibBuilder.loadTexts:fsCapwapWtpRadioStatisticsEntry.setStatus(_A)
class _FsCapwapWtpRadioLastFailType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,255)));namedValues=NamedValues(*(('statsNotSupported',0),(_b,1),(_c,2),(_d,3),(_e,255)))
_FsCapwapWtpRadioLastFailType_Type.__name__=_E
_FsCapwapWtpRadioLastFailType_Object=MibTableColumn
fsCapwapWtpRadioLastFailType=_FsCapwapWtpRadioLastFailType_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,1),_FsCapwapWtpRadioLastFailType_Type())
fsCapwapWtpRadioLastFailType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioLastFailType.setStatus(_A)
class _FsCapwapWtpRadioResetCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioResetCount_Type.__name__=_C
_FsCapwapWtpRadioResetCount_Object=MibTableColumn
fsCapwapWtpRadioResetCount=_FsCapwapWtpRadioResetCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,2),_FsCapwapWtpRadioResetCount_Type())
fsCapwapWtpRadioResetCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioResetCount.setStatus(_A)
class _FsCapwapWtpRadioSwFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioSwFailureCount_Type.__name__=_C
_FsCapwapWtpRadioSwFailureCount_Object=MibTableColumn
fsCapwapWtpRadioSwFailureCount=_FsCapwapWtpRadioSwFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,3),_FsCapwapWtpRadioSwFailureCount_Type())
fsCapwapWtpRadioSwFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioSwFailureCount.setStatus(_A)
class _FsCapwapWtpRadioHwFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioHwFailureCount_Type.__name__=_C
_FsCapwapWtpRadioHwFailureCount_Object=MibTableColumn
fsCapwapWtpRadioHwFailureCount=_FsCapwapWtpRadioHwFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,4),_FsCapwapWtpRadioHwFailureCount_Type())
fsCapwapWtpRadioHwFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioHwFailureCount.setStatus(_A)
class _FsCapwapWtpRadioOtherFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioOtherFailureCount_Type.__name__=_C
_FsCapwapWtpRadioOtherFailureCount_Object=MibTableColumn
fsCapwapWtpRadioOtherFailureCount=_FsCapwapWtpRadioOtherFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,5),_FsCapwapWtpRadioOtherFailureCount_Type())
fsCapwapWtpRadioOtherFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioOtherFailureCount.setStatus(_A)
class _FsCapwapWtpRadioUnknownFailureCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioUnknownFailureCount_Type.__name__=_C
_FsCapwapWtpRadioUnknownFailureCount_Object=MibTableColumn
fsCapwapWtpRadioUnknownFailureCount=_FsCapwapWtpRadioUnknownFailureCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,6),_FsCapwapWtpRadioUnknownFailureCount_Type())
fsCapwapWtpRadioUnknownFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioUnknownFailureCount.setStatus(_A)
class _FsCapwapWtpRadioConfigUpdateCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioConfigUpdateCount_Type.__name__=_C
_FsCapwapWtpRadioConfigUpdateCount_Object=MibTableColumn
fsCapwapWtpRadioConfigUpdateCount=_FsCapwapWtpRadioConfigUpdateCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,7),_FsCapwapWtpRadioConfigUpdateCount_Type())
fsCapwapWtpRadioConfigUpdateCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioConfigUpdateCount.setStatus(_A)
class _FsCapwapWtpRadioChannelChangeCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioChannelChangeCount_Type.__name__=_C
_FsCapwapWtpRadioChannelChangeCount_Object=MibTableColumn
fsCapwapWtpRadioChannelChangeCount=_FsCapwapWtpRadioChannelChangeCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,8),_FsCapwapWtpRadioChannelChangeCount_Type())
fsCapwapWtpRadioChannelChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioChannelChangeCount.setStatus(_A)
class _FsCapwapWtpRadioBandChangeCount_Type(Unsigned32):defaultValue=0
_FsCapwapWtpRadioBandChangeCount_Type.__name__=_C
_FsCapwapWtpRadioBandChangeCount_Object=MibTableColumn
fsCapwapWtpRadioBandChangeCount=_FsCapwapWtpRadioBandChangeCount_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,9),_FsCapwapWtpRadioBandChangeCount_Type())
fsCapwapWtpRadioBandChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioBandChangeCount.setStatus(_A)
class _FsCapwapWtpRadioCurrentNoiseFloor_Type(Integer32):defaultValue=0
_FsCapwapWtpRadioCurrentNoiseFloor_Type.__name__=_E
_FsCapwapWtpRadioCurrentNoiseFloor_Object=MibTableColumn
fsCapwapWtpRadioCurrentNoiseFloor=_FsCapwapWtpRadioCurrentNoiseFloor_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,10),_FsCapwapWtpRadioCurrentNoiseFloor_Type())
fsCapwapWtpRadioCurrentNoiseFloor.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioCurrentNoiseFloor.setStatus(_A)
_FsCapwapWtpRadioStatRowStatus_Type=RowStatus
_FsCapwapWtpRadioStatRowStatus_Object=MibTableColumn
fsCapwapWtpRadioStatRowStatus=_FsCapwapWtpRadioStatRowStatus_Object((1,3,6,1,4,1,10876,101,2,82,3,15,1,11),_FsCapwapWtpRadioStatRowStatus_Type())
fsCapwapWtpRadioStatRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsCapwapWtpRadioStatRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_H:EnabledStatus,'CapwapBaseRadioIdTC':CapwapBaseRadioIdTC,_V:CapwapBaseTunnelModeTC,_U:CapwapBaseMacTypeTC,'CapwapBaseStationIdTC':CapwapBaseStationIdTC,'fsCapwap':fsCapwap,'fsCapwapSystem':fsCapwapSystem,'fsCapwapModuleStatus':fsCapwapModuleStatus,'fsCapwapSystemControl':fsCapwapSystemControl,'fsCapwapControlUdpPort':fsCapwapControlUdpPort,'fsCapwapControlChannelDTLSPolicyOptions':fsCapwapControlChannelDTLSPolicyOptions,'fsCapwapDataChannelDTLSPolicyOptions':fsCapwapDataChannelDTLSPolicyOptions,'fsWlcDiscoveryMode':fsWlcDiscoveryMode,'fsCapwapWtpModeIgnore':fsCapwapWtpModeIgnore,'fsCapwapDebugMask':fsCapwapDebugMask,'fsDtlsDebugMask':fsDtlsDebugMask,'fsDtlsEncryption':fsDtlsEncryption,'fsDtlsEncryptAlgorithm':fsDtlsEncryptAlgorithm,'fsStationType':fsStationType,'fsCapwapWtpModel':fsCapwapWtpModel,'fsWtpModelTable':fsWtpModelTable,'fsWtpModelEntry':fsWtpModelEntry,_K:fsCapwapWtpModelNumber,'fsNoOfRadio':fsNoOfRadio,'fsCapwapWtpMacType':fsCapwapWtpMacType,'fsCapwapWtpTunnelMode':fsCapwapWtpTunnelMode,'fsCapwapSwVersion':fsCapwapSwVersion,'fsCapwapImageName':fsCapwapImageName,'fsCapwapQosProfileName':fsCapwapQosProfileName,'fsMaxStations':fsMaxStations,'fsWtpModelRowStatus':fsWtpModelRowStatus,'fsWtpRadioTable':fsWtpRadioTable,'fsWtpRadioEntry':fsWtpRadioEntry,_W:fsRadioNumber,'fsWtpRadioType':fsWtpRadioType,'fsRadioAdminStatus':fsRadioAdminStatus,'fsWtpRadioRowStatus':fsWtpRadioRowStatus,'fsCapwapConfig':fsCapwapConfig,'fsCapwapWhiteListTable':fsCapwapWhiteListTable,'fsCapwapWhiteListEntry':fsCapwapWhiteListEntry,_X:fsCapwapWhiteListId,'fsCapwapWhiteListWtpBaseMac':fsCapwapWhiteListWtpBaseMac,'fsCapwapWhiteListRowStatus':fsCapwapWhiteListRowStatus,'fsCapwapBlackListTable':fsCapwapBlackListTable,'fsCapwapBlackListEntry':fsCapwapBlackListEntry,_Y:fsCapwapBlackListId,'fsCapwapBlackListWtpBaseMac':fsCapwapBlackListWtpBaseMac,'fsCapwapBlackListRowStatus':fsCapwapBlackListRowStatus,'fsCapwapWtpConfigTable':fsCapwapWtpConfigTable,'fsCapwapWtpConfigEntry':fsCapwapWtpConfigEntry,'fsCapwapWtpReset':fsCapwapWtpReset,'fsCapwapClearConfig':fsCapwapClearConfig,'fsWtpDiscoveryType':fsWtpDiscoveryType,'fsWtpCountryString':fsWtpCountryString,'fsWtpCrashDumpFileName':fsWtpCrashDumpFileName,'fsWtpMemoryDumpFileName':fsWtpMemoryDumpFileName,'fsWtpDeleteOperation':fsWtpDeleteOperation,'fsCapwapClearApStats':fsCapwapClearApStats,'fsCapwapWtpConfigRowStatus':fsCapwapWtpConfigRowStatus,'fsCapwapLinkEncryptionTable':fsCapwapLinkEncryptionTable,'fsCapwapLinkEncryptionEntry':fsCapwapLinkEncryptionEntry,_Z:fsCapwapEncryptChannel,'fsCapwapEncryptChannelStatus':fsCapwapEncryptChannelStatus,'fsCapwapEncryptChannelRowStatus':fsCapwapEncryptChannelRowStatus,'fsCapwapDefaultWtpProfileTable':fsCapwapDefaultWtpProfileTable,'fsCapwapDefaultWtpProfileEntry':fsCapwapDefaultWtpProfileEntry,'fsCapwapDefaultQosProfile':fsCapwapDefaultQosProfile,'fsCapwapDefaultWtpProfileRowStatus':fsCapwapDefaultWtpProfileRowStatus,'fsCapwapDnsProfileTable':fsCapwapDnsProfileTable,'fsCapwapDnsProfileEntry':fsCapwapDnsProfileEntry,'fsCapwapDnsAddressType':fsCapwapDnsAddressType,'fsCapwapDnsServerIp':fsCapwapDnsServerIp,'fsCapwapDnsDomainName':fsCapwapDnsDomainName,'fsCapwapDnsProfileRowStatus':fsCapwapDnsProfileRowStatus,'fsWtpNativeVlanIdTable':fsWtpNativeVlanIdTable,'fsWtpNativeVlanIdEntry':fsWtpNativeVlanIdEntry,'fsWtpNativeVlanId':fsWtpNativeVlanId,'fsWtpNativeVlanIdRowStatus':fsWtpNativeVlanIdRowStatus,'fsCawapDiscStatsTable':fsCawapDiscStatsTable,'fsCawapDiscStatsEntry':fsCawapDiscStatsEntry,'fsCapwapDiscReqReceived':fsCapwapDiscReqReceived,'fsCapwapDiscRspReceived':fsCapwapDiscRspReceived,'fsCapwapDiscReqTransmitted':fsCapwapDiscReqTransmitted,'fsCapwapDiscRspTransmitted':fsCapwapDiscRspTransmitted,'fsCapwapDiscunsuccessfulProcessed':fsCapwapDiscunsuccessfulProcessed,'fsCapwapDiscLastUnsuccAttemptReason':fsCapwapDiscLastUnsuccAttemptReason,'fsCapwapDiscLastSuccAttemptTime':fsCapwapDiscLastSuccAttemptTime,'fsCapwapDiscLastUnsuccessfulAttemptTime':fsCapwapDiscLastUnsuccessfulAttemptTime,'fsCapwapDiscStatsRowStatus':fsCapwapDiscStatsRowStatus,'fsCawapJoinStatsTable':fsCawapJoinStatsTable,'fsCawapJoinStatsEntry':fsCawapJoinStatsEntry,'fsCapwapJoinReqReceived':fsCapwapJoinReqReceived,'fsCapwapJoinRspReceived':fsCapwapJoinRspReceived,'fsCapwapJoinReqTransmitted':fsCapwapJoinReqTransmitted,'fsCapwapJoinRspTransmitted':fsCapwapJoinRspTransmitted,'fsCapwapJoinunsuccessfulProcessed':fsCapwapJoinunsuccessfulProcessed,'fsCapwapJoinReasonLastUnsuccAttempt':fsCapwapJoinReasonLastUnsuccAttempt,'fsCapwapJoinLastSuccAttemptTime':fsCapwapJoinLastSuccAttemptTime,'fsCapwapJoinLastUnsuccAttemptTime':fsCapwapJoinLastUnsuccAttemptTime,'fsCapwapJoinStatsRowStatus':fsCapwapJoinStatsRowStatus,'fsCawapConfigStatsTable':fsCawapConfigStatsTable,'fsCawapConfigStatsEntry':fsCawapConfigStatsEntry,'fsCapwapConfigReqReceived':fsCapwapConfigReqReceived,'fsCapwapConfigRspReceived':fsCapwapConfigRspReceived,'fsCapwapConfigReqTransmitted':fsCapwapConfigReqTransmitted,'fsCapwapConfigRspTransmitted':fsCapwapConfigRspTransmitted,'fsCapwapConfigunsuccessfulProcessed':fsCapwapConfigunsuccessfulProcessed,'fsCapwapConfigReasonLastUnsuccAttempt':fsCapwapConfigReasonLastUnsuccAttempt,'fsCapwapConfigLastSuccAttemptTime':fsCapwapConfigLastSuccAttemptTime,'fsCapwapConfigLastUnsuccessfulAttemptTime':fsCapwapConfigLastUnsuccessfulAttemptTime,'fsCapwapConfigStatsRowStatus':fsCapwapConfigStatsRowStatus,'fsCawapRunStatsTable':fsCawapRunStatsTable,'fsCawapRunStatsEntry':fsCawapRunStatsEntry,'fsCapwapRunConfigUpdateReqReceived':fsCapwapRunConfigUpdateReqReceived,'fsCapwapRunConfigUpdateRspReceived':fsCapwapRunConfigUpdateRspReceived,'fsCapwapRunConfigUpdateReqTransmitted':fsCapwapRunConfigUpdateReqTransmitted,'fsCapwapRunConfigUpdateRspTransmitted':fsCapwapRunConfigUpdateRspTransmitted,'fsCapwapRunConfigUpdateunsuccessfulProcessed':fsCapwapRunConfigUpdateunsuccessfulProcessed,'fsCapwapRunConfigUpdateReasonLastUnsuccAttempt':fsCapwapRunConfigUpdateReasonLastUnsuccAttempt,'fsCapwapRunConfigUpdateLastSuccAttemptTime':fsCapwapRunConfigUpdateLastSuccAttemptTime,'fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime':fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime,'fsCapwapRunStationConfigReqReceived':fsCapwapRunStationConfigReqReceived,'fsCapwapRunStationConfigRspReceived':fsCapwapRunStationConfigRspReceived,'fsCapwapRunStationConfigReqTransmitted':fsCapwapRunStationConfigReqTransmitted,'fsCapwapRunStationConfigRspTransmitted':fsCapwapRunStationConfigRspTransmitted,'fsCapwapRunStationConfigunsuccessfulProcessed':fsCapwapRunStationConfigunsuccessfulProcessed,'fsCapwapRunStationConfigReasonLastUnsuccAttempt':fsCapwapRunStationConfigReasonLastUnsuccAttempt,'fsCapwapRunStationConfigLastSuccAttemptTime':fsCapwapRunStationConfigLastSuccAttemptTime,'fsCapwapRunStationConfigLastUnsuccessfulAttemptTime':fsCapwapRunStationConfigLastUnsuccessfulAttemptTime,'fsCapwapRunClearConfigReqReceived':fsCapwapRunClearConfigReqReceived,'fsCapwapRunClearConfigRspReceived':fsCapwapRunClearConfigRspReceived,'fsCapwapRunClearConfigReqTransmitted':fsCapwapRunClearConfigReqTransmitted,'fsCapwapRunClearConfigRspTransmitted':fsCapwapRunClearConfigRspTransmitted,'fsCapwapRunClearConfigunsuccessfulProcessed':fsCapwapRunClearConfigunsuccessfulProcessed,'fsCapwapRunClearConfigReasonLastUnsuccAttempt':fsCapwapRunClearConfigReasonLastUnsuccAttempt,'fsCapwapRunClearConfigLastSuccAttemptTime':fsCapwapRunClearConfigLastSuccAttemptTime,'fsCapwapRunClearConfigLastUnsuccessfulAttemptTime':fsCapwapRunClearConfigLastUnsuccessfulAttemptTime,'fsCapwapRunDataTransferReqReceived':fsCapwapRunDataTransferReqReceived,'fsCapwapRunDataTransferRspReceived':fsCapwapRunDataTransferRspReceived,'fsCapwapRunDataTransferReqTransmitted':fsCapwapRunDataTransferReqTransmitted,'fsCapwapRunDataTransferRspTransmitted':fsCapwapRunDataTransferRspTransmitted,'fsCapwapRunDataTransferunsuccessfulProcessed':fsCapwapRunDataTransferunsuccessfulProcessed,'fsCapwapRunDataTransferReasonLastUnsuccAttempt':fsCapwapRunDataTransferReasonLastUnsuccAttempt,'fsCapwapRunDataTransferLastSuccAttemptTime':fsCapwapRunDataTransferLastSuccAttemptTime,'fsCapwapRunDataTransferLastUnsuccessfulAttemptTime':fsCapwapRunDataTransferLastUnsuccessfulAttemptTime,'fsCapwapRunResetReqReceived':fsCapwapRunResetReqReceived,'fsCapwapRunResetRspReceived':fsCapwapRunResetRspReceived,'fsCapwapRunResetReqTransmitted':fsCapwapRunResetReqTransmitted,'fsCapwapRunResetRspTransmitted':fsCapwapRunResetRspTransmitted,'fsCapwapRunResetunsuccessfulProcessed':fsCapwapRunResetunsuccessfulProcessed,'fsCapwapRunResetReasonLastUnsuccAttempt':fsCapwapRunResetReasonLastUnsuccAttempt,'fsCapwapRunResetLastSuccAttemptTime':fsCapwapRunResetLastSuccAttemptTime,'fsCapwapRunResetLastUnsuccessfulAttemptTime':fsCapwapRunResetLastUnsuccessfulAttemptTime,'fsCapwapRunPriDiscReqReceived':fsCapwapRunPriDiscReqReceived,'fsCapwapRunPriDiscRspReceived':fsCapwapRunPriDiscRspReceived,'fsCapwapRunPriDiscReqTransmitted':fsCapwapRunPriDiscReqTransmitted,'fsCapwapRunPriDiscRspTransmitted':fsCapwapRunPriDiscRspTransmitted,'fsCapwapRunPriDiscunsuccessfulProcessed':fsCapwapRunPriDiscunsuccessfulProcessed,'fsCapwapRunPriDiscReasonLastUnsuccAttempt':fsCapwapRunPriDiscReasonLastUnsuccAttempt,'fsCapwapRunPriDiscLastSuccAttemptTime':fsCapwapRunPriDiscLastSuccAttemptTime,'fsCapwapRunPriDiscLastUnsuccessfulAttemptTime':fsCapwapRunPriDiscLastUnsuccessfulAttemptTime,'fsCapwapRunEchoReqReceived':fsCapwapRunEchoReqReceived,'fsCapwapRunEchoRspReceived':fsCapwapRunEchoRspReceived,'fsCapwapRunEchoReqTransmitted':fsCapwapRunEchoReqTransmitted,'fsCapwapRunEchoRspTransmitted':fsCapwapRunEchoRspTransmitted,'fsCapwapRunEchounsuccessfulProcessed':fsCapwapRunEchounsuccessfulProcessed,'fsCapwapRunEchoReasonLastUnsuccAttempt':fsCapwapRunEchoReasonLastUnsuccAttempt,'fsCapwapRunEchoLastSuccAttemptTime':fsCapwapRunEchoLastSuccAttemptTime,'fsCapwapRunEchoLastUnsuccessfulAttemptTime':fsCapwapRunEchoLastUnsuccessfulAttemptTime,'fsCapwapRunStatsRowStatus':fsCapwapRunStatsRowStatus,'fsCapwapWirelessBindingTable':fsCapwapWirelessBindingTable,'fsCapwapWirelessBindingEntry':fsCapwapWirelessBindingEntry,'fsCapwapWirelessBindingVirtualRadioIfIndex':fsCapwapWirelessBindingVirtualRadioIfIndex,'fsCapwapWirelessBindingType':fsCapwapWirelessBindingType,'fsCapwapWirelessBindingRowStatus':fsCapwapWirelessBindingRowStatus,'fsCapwapStationWhiteListTable':fsCapwapStationWhiteListTable,'fsCapwapStationWhiteListEntry':fsCapwapStationWhiteListEntry,_a:fsCapwapStationWhiteListId,'fsCapwapStationWhiteListStationId':fsCapwapStationWhiteListStationId,'fsCapwapStationWhiteListRowStatus':fsCapwapStationWhiteListRowStatus,'fsCapwapWtpRebootStatisticsTable':fsCapwapWtpRebootStatisticsTable,'fsCapwapWtpRebootStatisticsEntry':fsCapwapWtpRebootStatisticsEntry,'fsCapwapWtpRebootStatisticsRebootCount':fsCapwapWtpRebootStatisticsRebootCount,'fsCapwapWtpRebootStatisticsAcInitiatedCount':fsCapwapWtpRebootStatisticsAcInitiatedCount,'fsCapwapWtpRebootStatisticsLinkFailureCount':fsCapwapWtpRebootStatisticsLinkFailureCount,'fsCapwapWtpRebootStatisticsSwFailureCount':fsCapwapWtpRebootStatisticsSwFailureCount,'fsCapwapWtpRebootStatisticsHwFailureCount':fsCapwapWtpRebootStatisticsHwFailureCount,'fsCapwapWtpRebootStatisticsOtherFailureCount':fsCapwapWtpRebootStatisticsOtherFailureCount,'fsCapwapWtpRebootStatisticsUnknownFailureCount':fsCapwapWtpRebootStatisticsUnknownFailureCount,'fsCapwapWtpRebootStatisticsLastFailureType':fsCapwapWtpRebootStatisticsLastFailureType,'fsCapwapWtpRebootStatisticsRowStatus':fsCapwapWtpRebootStatisticsRowStatus,'fsCapwapWtpRadioStatisticsTable':fsCapwapWtpRadioStatisticsTable,'fsCapwapWtpRadioStatisticsEntry':fsCapwapWtpRadioStatisticsEntry,'fsCapwapWtpRadioLastFailType':fsCapwapWtpRadioLastFailType,'fsCapwapWtpRadioResetCount':fsCapwapWtpRadioResetCount,'fsCapwapWtpRadioSwFailureCount':fsCapwapWtpRadioSwFailureCount,'fsCapwapWtpRadioHwFailureCount':fsCapwapWtpRadioHwFailureCount,'fsCapwapWtpRadioOtherFailureCount':fsCapwapWtpRadioOtherFailureCount,'fsCapwapWtpRadioUnknownFailureCount':fsCapwapWtpRadioUnknownFailureCount,'fsCapwapWtpRadioConfigUpdateCount':fsCapwapWtpRadioConfigUpdateCount,'fsCapwapWtpRadioChannelChangeCount':fsCapwapWtpRadioChannelChangeCount,'fsCapwapWtpRadioBandChangeCount':fsCapwapWtpRadioBandChangeCount,'fsCapwapWtpRadioCurrentNoiseFloor':fsCapwapWtpRadioCurrentNoiseFloor,'fsCapwapWtpRadioStatRowStatus':fsCapwapWtpRadioStatRowStatus})