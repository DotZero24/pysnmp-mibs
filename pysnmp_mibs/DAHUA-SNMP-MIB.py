# SNMP MIB module (DAHUA-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dahua/DAHUA-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:00 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

device = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2)
)
if mibBuilder.loadTexts:
    device.setRevisions(
        ("2014-04-28 11:12",
         "2014-02-14 11:12",
         "2014-01-07 14:27")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Dahua_ObjectIdentity = ObjectIdentity
dahua = _Dahua_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849)
)
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1)
)
_VersionInfo_ObjectIdentity = ObjectIdentity
versionInfo = _VersionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 1)
)
_SoftwareRevision_Type = DisplayString
_SoftwareRevision_Object = MibScalar
softwareRevision = _SoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 1, 1),
    _SoftwareRevision_Type()
)
softwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    softwareRevision.setStatus("current")
_HardwareRevision_Type = DisplayString
_HardwareRevision_Object = MibScalar
hardwareRevision = _HardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 1, 2),
    _HardwareRevision_Type()
)
hardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardwareRevision.setStatus("current")
_ProductInfo_ObjectIdentity = ObjectIdentity
productInfo = _ProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2)
)
_VideoChannel_Type = Integer32
_VideoChannel_Object = MibScalar
videoChannel = _VideoChannel_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 1),
    _VideoChannel_Type()
)
videoChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoChannel.setStatus("current")
_AlarmInput_Type = Integer32
_AlarmInput_Object = MibScalar
alarmInput = _AlarmInput_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 2),
    _AlarmInput_Type()
)
alarmInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmInput.setStatus("current")
_AlarmOutput_Type = Integer32
_AlarmOutput_Object = MibScalar
alarmOutput = _AlarmOutput_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 3),
    _AlarmOutput_Type()
)
alarmOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmOutput.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 4),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_SystemVersion_Type = DisplayString
_SystemVersion_Object = MibScalar
systemVersion = _SystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 5),
    _SystemVersion_Type()
)
systemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVersion.setStatus("current")
_DeviceType_Type = DisplayString
_DeviceType_Object = MibScalar
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 6),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("current")
_DeviceClass_Type = DisplayString
_DeviceClass_Object = MibScalar
deviceClass = _DeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 7),
    _DeviceClass_Type()
)
deviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceClass.setStatus("current")


class _DeviceStatus_Type(Integer32):
    """Custom type deviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bad", 0),
          ("good", 1))
    )


_DeviceStatus_Type.__name__ = "Integer32"
_DeviceStatus_Object = MibScalar
deviceStatus = _DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 8),
    _DeviceStatus_Type()
)
deviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceStatus.setStatus("current")
_MachineName_Type = DisplayString
_MachineName_Object = MibScalar
machineName = _MachineName_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 2, 9),
    _MachineName_Type()
)
machineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machineName.setStatus("current")
_CpuUsage_Type = Integer32
_CpuUsage_Object = MibScalar
cpuUsage = _CpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 3),
    _CpuUsage_Type()
)
cpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUsage.setStatus("current")
_LastestEvent_Type = DisplayString
_LastestEvent_Object = MibScalar
lastestEvent = _LastestEvent_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 4),
    _LastestEvent_Type()
)
lastestEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastestEvent.setStatus("current")
_EncodeNo_Type = Integer32
_EncodeNo_Object = MibScalar
encodeNo = _EncodeNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 1, 5),
    _EncodeNo_Type()
)
encodeNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encodeNo.setStatus("current")
_NetworkInfo_ObjectIdentity = ObjectIdentity
networkInfo = _NetworkInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2)
)
_NetworkPort_ObjectIdentity = ObjectIdentity
networkPort = _NetworkPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1)
)
_TcpPort_Type = Integer32
_TcpPort_Object = MibScalar
tcpPort = _TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1, 1),
    _TcpPort_Type()
)
tcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPort.setStatus("current")
_UdpPort_Type = Integer32
_UdpPort_Object = MibScalar
udpPort = _UdpPort_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1, 2),
    _UdpPort_Type()
)
udpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpPort.setStatus("current")
_HttpPort_Type = Integer32
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1, 3),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_RtspPort_Type = Integer32
_RtspPort_Object = MibScalar
rtspPort = _RtspPort_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1, 4),
    _RtspPort_Type()
)
rtspPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtspPort.setStatus("current")
_MaxConnectNum_Type = Integer32
_MaxConnectNum_Object = MibScalar
maxConnectNum = _MaxConnectNum_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1, 5),
    _MaxConnectNum_Type()
)
maxConnectNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxConnectNum.setStatus("current")
_HttpsPort_Type = Integer32
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 1, 6),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpsPort.setStatus("current")
_TcpIpInfo_ObjectIdentity = ObjectIdentity
tcpIpInfo = _TcpIpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2)
)


class _GetIpmode_Type(Integer32):
    """Custom type getIpmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dhcp", 1))
    )


_GetIpmode_Type.__name__ = "Integer32"
_GetIpmode_Object = MibScalar
getIpmode = _GetIpmode_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 1),
    _GetIpmode_Type()
)
getIpmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getIpmode.setStatus("current")
_MacAddr_Type = DisplayString
_MacAddr_Object = MibScalar
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 2),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")


class _IpVersion_Type(Integer32):
    """Custom type ipVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )


_IpVersion_Type.__name__ = "Integer32"
_IpVersion_Object = MibScalar
ipVersion = _IpVersion_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 3),
    _IpVersion_Type()
)
ipVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipVersion.setStatus("current")
_SubnetMast_Type = DisplayString
_SubnetMast_Object = MibScalar
subnetMast = _SubnetMast_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 4),
    _SubnetMast_Type()
)
subnetMast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMast.setStatus("current")
_DefaultGateway_Type = DisplayString
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 5),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")
_PreferredDns_Type = DisplayString
_PreferredDns_Object = MibScalar
preferredDns = _PreferredDns_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 6),
    _PreferredDns_Type()
)
preferredDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferredDns.setStatus("current")
_AlternateDns_Type = DisplayString
_AlternateDns_Object = MibScalar
alternateDns = _AlternateDns_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 7),
    _AlternateDns_Type()
)
alternateDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateDns.setStatus("current")
_IpAddr_Type = DisplayString
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 2, 2, 8),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("current")
_ConfigInfo_ObjectIdentity = ObjectIdentity
configInfo = _ConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3)
)
_EncodeConfig_ObjectIdentity = ObjectIdentity
encodeConfig = _EncodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1)
)
_MainStreamInfo_ObjectIdentity = ObjectIdentity
mainStreamInfo = _MainStreamInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1)
)
_RegularStreamInfoTable_Object = MibTable
regularStreamInfoTable = _RegularStreamInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    regularStreamInfoTable.setStatus("current")
_RegularStreamInfoTableEntry_Object = MibTableRow
regularStreamInfoTableEntry = _RegularStreamInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 1, 1)
)
regularStreamInfoTableEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "regularChannelNo"),
)
if mibBuilder.loadTexts:
    regularStreamInfoTableEntry.setStatus("current")
_RegularChannelNo_Type = Integer32
_RegularChannelNo_Object = MibTableColumn
regularChannelNo = _RegularChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 1, 1, 1),
    _RegularChannelNo_Type()
)
regularChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    regularChannelNo.setStatus("current")
_RegularCompression_Type = DisplayString
_RegularCompression_Object = MibTableColumn
regularCompression = _RegularCompression_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 1, 1, 2),
    _RegularCompression_Type()
)
regularCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regularCompression.setStatus("current")
_RegularFPS_Type = Integer32
_RegularFPS_Object = MibTableColumn
regularFPS = _RegularFPS_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 1, 1, 3),
    _RegularFPS_Type()
)
regularFPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regularFPS.setStatus("current")
_RegularResolution_Type = DisplayString
_RegularResolution_Object = MibTableColumn
regularResolution = _RegularResolution_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 1, 1, 4),
    _RegularResolution_Type()
)
regularResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    regularResolution.setStatus("current")
_MdStreamInfoTable_Object = MibTable
mdStreamInfoTable = _MdStreamInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mdStreamInfoTable.setStatus("current")
_MdStreamInfoTableEntry_Object = MibTableRow
mdStreamInfoTableEntry = _MdStreamInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 2, 1)
)
mdStreamInfoTableEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "mdChannelNo"),
)
if mibBuilder.loadTexts:
    mdStreamInfoTableEntry.setStatus("current")
_MdChannelNo_Type = Integer32
_MdChannelNo_Object = MibTableColumn
mdChannelNo = _MdChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 2, 1, 1),
    _MdChannelNo_Type()
)
mdChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdChannelNo.setStatus("current")
_MdCompression_Type = DisplayString
_MdCompression_Object = MibTableColumn
mdCompression = _MdCompression_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 2, 1, 2),
    _MdCompression_Type()
)
mdCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdCompression.setStatus("current")
_MdFPS_Type = Integer32
_MdFPS_Object = MibTableColumn
mdFPS = _MdFPS_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 2, 1, 3),
    _MdFPS_Type()
)
mdFPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdFPS.setStatus("current")
_MdResolution_Type = DisplayString
_MdResolution_Object = MibTableColumn
mdResolution = _MdResolution_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 2, 1, 4),
    _MdResolution_Type()
)
mdResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mdResolution.setStatus("current")
_AlarmStreamInfoTable_Object = MibTable
alarmStreamInfoTable = _AlarmStreamInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alarmStreamInfoTable.setStatus("current")
_AlarmStreamInfoTableEntry_Object = MibTableRow
alarmStreamInfoTableEntry = _AlarmStreamInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 3, 1)
)
alarmStreamInfoTableEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "alarmChannelNo"),
)
if mibBuilder.loadTexts:
    alarmStreamInfoTableEntry.setStatus("current")
_AlarmChannelNo_Type = Integer32
_AlarmChannelNo_Object = MibTableColumn
alarmChannelNo = _AlarmChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 3, 1, 1),
    _AlarmChannelNo_Type()
)
alarmChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmChannelNo.setStatus("current")
_AlarmCompression_Type = DisplayString
_AlarmCompression_Object = MibTableColumn
alarmCompression = _AlarmCompression_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 3, 1, 2),
    _AlarmCompression_Type()
)
alarmCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmCompression.setStatus("current")
_AlarmFPS_Type = Integer32
_AlarmFPS_Object = MibTableColumn
alarmFPS = _AlarmFPS_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 3, 1, 3),
    _AlarmFPS_Type()
)
alarmFPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFPS.setStatus("current")
_AlarmResolution_Type = DisplayString
_AlarmResolution_Object = MibTableColumn
alarmResolution = _AlarmResolution_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 1, 3, 1, 4),
    _AlarmResolution_Type()
)
alarmResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmResolution.setStatus("current")
_ExtraStreamInfo_ObjectIdentity = ObjectIdentity
extraStreamInfo = _ExtraStreamInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2)
)
_Extra1StreamInfoTable_Object = MibTable
extra1StreamInfoTable = _Extra1StreamInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    extra1StreamInfoTable.setStatus("current")
_Extra1StreamInfoEntry_Object = MibTableRow
extra1StreamInfoEntry = _Extra1StreamInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2, 1, 1)
)
extra1StreamInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "extra1ChannelNo"),
)
if mibBuilder.loadTexts:
    extra1StreamInfoEntry.setStatus("current")
_Extra1ChannelNo_Type = Integer32
_Extra1ChannelNo_Object = MibTableColumn
extra1ChannelNo = _Extra1ChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2, 1, 1, 1),
    _Extra1ChannelNo_Type()
)
extra1ChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extra1ChannelNo.setStatus("current")
_Extra1Compression_Type = DisplayString
_Extra1Compression_Object = MibTableColumn
extra1Compression = _Extra1Compression_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2, 1, 1, 2),
    _Extra1Compression_Type()
)
extra1Compression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extra1Compression.setStatus("current")
_Extra1FPS_Type = Integer32
_Extra1FPS_Object = MibTableColumn
extra1FPS = _Extra1FPS_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2, 1, 1, 3),
    _Extra1FPS_Type()
)
extra1FPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extra1FPS.setStatus("current")
_Extra1Resolution_Type = DisplayString
_Extra1Resolution_Object = MibTableColumn
extra1Resolution = _Extra1Resolution_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 1, 2, 1, 1, 4),
    _Extra1Resolution_Type()
)
extra1Resolution.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    extra1Resolution.setStatus("current")
_EventConfig_ObjectIdentity = ObjectIdentity
eventConfig = _EventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2)
)
_VideoDetectConfig_ObjectIdentity = ObjectIdentity
videoDetectConfig = _VideoDetectConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1)
)
_VideoMotionInfoTable_Object = MibTable
videoMotionInfoTable = _VideoMotionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    videoMotionInfoTable.setStatus("current")
_VideoMotionInfoEntry_Object = MibTableRow
videoMotionInfoEntry = _VideoMotionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 1, 1)
)
videoMotionInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "videoMotionIndex"),
)
if mibBuilder.loadTexts:
    videoMotionInfoEntry.setStatus("current")
_VideoMotionIndex_Type = Integer32
_VideoMotionIndex_Object = MibTableColumn
videoMotionIndex = _VideoMotionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 1, 1, 1),
    _VideoMotionIndex_Type()
)
videoMotionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoMotionIndex.setStatus("current")
_VideoLossInfoTable_Object = MibTable
videoLossInfoTable = _VideoLossInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    videoLossInfoTable.setStatus("current")
_VideoLossInfoEntry_Object = MibTableRow
videoLossInfoEntry = _VideoLossInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 2, 1)
)
videoLossInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "videoLossIndex"),
)
if mibBuilder.loadTexts:
    videoLossInfoEntry.setStatus("current")
_VideoLossIndex_Type = Integer32
_VideoLossIndex_Object = MibTableColumn
videoLossIndex = _VideoLossIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 2, 1, 1),
    _VideoLossIndex_Type()
)
videoLossIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoLossIndex.setStatus("current")
_VideoBlindInfoTable_Object = MibTable
videoBlindInfoTable = _VideoBlindInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    videoBlindInfoTable.setStatus("current")
_VideoBlindInfoEntry_Object = MibTableRow
videoBlindInfoEntry = _VideoBlindInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 3, 1)
)
videoBlindInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "videoBlindIndex"),
)
if mibBuilder.loadTexts:
    videoBlindInfoEntry.setStatus("current")
_VideoBlindIndex_Type = Integer32
_VideoBlindIndex_Object = MibTableColumn
videoBlindIndex = _VideoBlindIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 1, 3, 1, 1),
    _VideoBlindIndex_Type()
)
videoBlindIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoBlindIndex.setStatus("current")
_AlarmConfig_ObjectIdentity = ObjectIdentity
alarmConfig = _AlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2)
)
_LocalAlarmInfoTable_Object = MibTable
localAlarmInfoTable = _LocalAlarmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    localAlarmInfoTable.setStatus("current")
_LocalAlarmInfoEntry_Object = MibTableRow
localAlarmInfoEntry = _LocalAlarmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2, 1, 1)
)
localAlarmInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "localAlarmIndex"),
)
if mibBuilder.loadTexts:
    localAlarmInfoEntry.setStatus("current")
_LocalAlarmIndex_Type = Integer32
_LocalAlarmIndex_Object = MibTableColumn
localAlarmIndex = _LocalAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2, 1, 1, 1),
    _LocalAlarmIndex_Type()
)
localAlarmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localAlarmIndex.setStatus("current")
_NetworkAlarmInfoTable_Object = MibTable
networkAlarmInfoTable = _NetworkAlarmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    networkAlarmInfoTable.setStatus("current")
_NetworkAlarmInfoEntry_Object = MibTableRow
networkAlarmInfoEntry = _NetworkAlarmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2, 2, 1)
)
networkAlarmInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "networkAlarmIndex"),
)
if mibBuilder.loadTexts:
    networkAlarmInfoEntry.setStatus("current")
_NetworkAlarmIndex_Type = Integer32
_NetworkAlarmIndex_Object = MibTableColumn
networkAlarmIndex = _NetworkAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 2, 2, 1, 1),
    _NetworkAlarmIndex_Type()
)
networkAlarmIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAlarmIndex.setStatus("current")
_ExceptionConfig_ObjectIdentity = ObjectIdentity
exceptionConfig = _ExceptionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 2, 3)
)
_RecordConfig_ObjectIdentity = ObjectIdentity
recordConfig = _RecordConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 3)
)
_RecordPlanInfo_ObjectIdentity = ObjectIdentity
recordPlanInfo = _RecordPlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 3, 1)
)
_RecordMainStreamInfoTable_Object = MibTable
recordMainStreamInfoTable = _RecordMainStreamInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    recordMainStreamInfoTable.setStatus("current")
_RecordMainStreamInfoEntry_Object = MibTableRow
recordMainStreamInfoEntry = _RecordMainStreamInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 3, 1, 1, 1)
)
recordMainStreamInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "recordMainChannelIndex"),
)
if mibBuilder.loadTexts:
    recordMainStreamInfoEntry.setStatus("current")
_RecordMainChannelIndex_Type = Integer32
_RecordMainChannelIndex_Object = MibTableColumn
recordMainChannelIndex = _RecordMainChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 3, 3, 1, 1, 1, 1),
    _RecordMainChannelIndex_Type()
)
recordMainChannelIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recordMainChannelIndex.setStatus("current")
_StorageInfo_ObjectIdentity = ObjectIdentity
storageInfo = _StorageInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4)
)
_PhysicalVolumeInfoTable_Object = MibTable
physicalVolumeInfoTable = _PhysicalVolumeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1)
)
if mibBuilder.loadTexts:
    physicalVolumeInfoTable.setStatus("current")
_PhysicalVolumeInfoEntry_Object = MibTableRow
physicalVolumeInfoEntry = _PhysicalVolumeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1, 1)
)
physicalVolumeInfoEntry.setIndexNames(
    (0, "DAHUA-SNMP-MIB", "physicalVolumeIndex"),
)
if mibBuilder.loadTexts:
    physicalVolumeInfoEntry.setStatus("current")
_PhysicalVolumeIndex_Type = Integer32
_PhysicalVolumeIndex_Object = MibTableColumn
physicalVolumeIndex = _PhysicalVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1, 1, 1),
    _PhysicalVolumeIndex_Type()
)
physicalVolumeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicalVolumeIndex.setStatus("current")
_PhysicNo_Type = Integer32
_PhysicNo_Object = MibTableColumn
physicNo = _PhysicNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1, 1, 2),
    _PhysicNo_Type()
)
physicNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    physicNo.setStatus("current")
_LogicNo_Type = Integer32
_LogicNo_Object = MibTableColumn
logicNo = _LogicNo_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1, 1, 3),
    _LogicNo_Type()
)
logicNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logicNo.setStatus("current")
_PhysicalVolumeName_Type = DisplayString
_PhysicalVolumeName_Object = MibTableColumn
physicalVolumeName = _PhysicalVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1, 1, 4),
    _PhysicalVolumeName_Type()
)
physicalVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalVolumeName.setStatus("current")
_PhysicalVolumeStatus_Type = DisplayString
_PhysicalVolumeStatus_Object = MibTableColumn
physicalVolumeStatus = _PhysicalVolumeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 4, 1, 1, 5),
    _PhysicalVolumeStatus_Type()
)
physicalVolumeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physicalVolumeStatus.setStatus("current")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 10)
)
_Dvr_ObjectIdentity = ObjectIdentity
dvr = _Dvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 10, 1)
)
_Nvr_ObjectIdentity = ObjectIdentity
nvr = _Nvr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 10, 2)
)
_Ipc_ObjectIdentity = ObjectIdentity
ipc = _Ipc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 10, 3)
)
_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11)
)
_MultiMediaEvent_ObjectIdentity = ObjectIdentity
multiMediaEvent = _MultiMediaEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 11)
)
_AlarmEvent_ObjectIdentity = ObjectIdentity
alarmEvent = _AlarmEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 12)
)
_StorageEvent_ObjectIdentity = ObjectIdentity
storageEvent = _StorageEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 13)
)
_RecordEvent_ObjectIdentity = ObjectIdentity
recordEvent = _RecordEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 14)
)
_DahuaSnmpTrap_ObjectIdentity = ObjectIdentity
dahuaSnmpTrap = _DahuaSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 12)
)
_Action_Type = DisplayString
_Action_Object = MibScalar
action = _Action_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 12, 1),
    _Action_Type()
)
action.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    action.setStatus("current")
_CurrentTime_Type = DisplayString
_CurrentTime_Object = MibScalar
currentTime = _CurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 12, 2),
    _CurrentTime_Type()
)
currentTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    currentTime.setStatus("current")


class _SnmpStatus_Type(Integer32):
    """Custom type snmpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 0),
          ("stop", 1))
    )


_SnmpStatus_Type.__name__ = "Integer32"
_SnmpStatus_Object = MibScalar
snmpStatus = _SnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 12, 3),
    _SnmpStatus_Type()
)
snmpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    snmpStatus.setStatus("current")
_PhysicalVolumeThreshold_Type = Integer32
_PhysicalVolumeThreshold_Object = MibScalar
physicalVolumeThreshold = _PhysicalVolumeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 12, 4),
    _PhysicalVolumeThreshold_Type()
)
physicalVolumeThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    physicalVolumeThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

snmpStatusEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 2)
)
snmpStatusEvent.setObjects(
    ("DAHUA-SNMP-MIB", "snmpStatus")
)
if mibBuilder.loadTexts:
    snmpStatusEvent.setStatus(
        "current"
    )

videoMotionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 11, 1)
)
videoMotionEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "videoMotionIndex"))
)
if mibBuilder.loadTexts:
    videoMotionEvent.setStatus(
        "current"
    )

videoBlindEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 11, 2)
)
videoBlindEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "videoBlindIndex"))
)
if mibBuilder.loadTexts:
    videoBlindEvent.setStatus(
        "current"
    )

videoLossEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 11, 3)
)
videoLossEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "videoLossIndex"))
)
if mibBuilder.loadTexts:
    videoLossEvent.setStatus(
        "current"
    )

localAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 12, 1)
)
localAlarmEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "localAlarmIndex"))
)
if mibBuilder.loadTexts:
    localAlarmEvent.setStatus(
        "current"
    )

storageFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 13, 1)
)
storageFailureEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "logicNo"))
)
if mibBuilder.loadTexts:
    storageFailureEvent.setStatus(
        "current"
    )

storageLowSpaceEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 13, 2)
)
storageLowSpaceEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "logicNo"))
)
if mibBuilder.loadTexts:
    storageLowSpaceEvent.setStatus(
        "current"
    )

storageInOutEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 13, 3)
)
storageInOutEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "logicNo"))
)
if mibBuilder.loadTexts:
    storageInOutEvent.setStatus(
        "current"
    )

storageSMARTAbnormityEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 13, 4)
)
storageSMARTAbnormityEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "logicNo"))
)
if mibBuilder.loadTexts:
    storageSMARTAbnormityEvent.setStatus(
        "current"
    )

recordMainStreamEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 14, 1)
)
recordMainStreamEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "recordMainChannelIndex"))
)
if mibBuilder.loadTexts:
    recordMainStreamEvent.setStatus(
        "current"
    )

recordExtraStreamEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1004849, 2, 11, 14, 2)
)
recordExtraStreamEvent.setObjects(
      *(("DAHUA-SNMP-MIB", "action"),
        ("DAHUA-SNMP-MIB", "currentTime"),
        ("DAHUA-SNMP-MIB", "recordExtraChannelIndex"))
)
if mibBuilder.loadTexts:
    recordExtraStreamEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DAHUA-SNMP-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "dahua": dahua,
       "device": device,
       "systemInfo": systemInfo,
       "versionInfo": versionInfo,
       "softwareRevision": softwareRevision,
       "hardwareRevision": hardwareRevision,
       "productInfo": productInfo,
       "videoChannel": videoChannel,
       "alarmInput": alarmInput,
       "alarmOutput": alarmOutput,
       "serialNumber": serialNumber,
       "systemVersion": systemVersion,
       "deviceType": deviceType,
       "deviceClass": deviceClass,
       "deviceStatus": deviceStatus,
       "machineName": machineName,
       "cpuUsage": cpuUsage,
       "lastestEvent": lastestEvent,
       "encodeNo": encodeNo,
       "networkInfo": networkInfo,
       "networkPort": networkPort,
       "tcpPort": tcpPort,
       "udpPort": udpPort,
       "httpPort": httpPort,
       "rtspPort": rtspPort,
       "maxConnectNum": maxConnectNum,
       "httpsPort": httpsPort,
       "tcpIpInfo": tcpIpInfo,
       "getIpmode": getIpmode,
       "macAddr": macAddr,
       "ipVersion": ipVersion,
       "subnetMast": subnetMast,
       "defaultGateway": defaultGateway,
       "preferredDns": preferredDns,
       "alternateDns": alternateDns,
       "ipAddr": ipAddr,
       "configInfo": configInfo,
       "encodeConfig": encodeConfig,
       "mainStreamInfo": mainStreamInfo,
       "regularStreamInfoTable": regularStreamInfoTable,
       "regularStreamInfoTableEntry": regularStreamInfoTableEntry,
       "regularChannelNo": regularChannelNo,
       "regularCompression": regularCompression,
       "regularFPS": regularFPS,
       "regularResolution": regularResolution,
       "mdStreamInfoTable": mdStreamInfoTable,
       "mdStreamInfoTableEntry": mdStreamInfoTableEntry,
       "mdChannelNo": mdChannelNo,
       "mdCompression": mdCompression,
       "mdFPS": mdFPS,
       "mdResolution": mdResolution,
       "alarmStreamInfoTable": alarmStreamInfoTable,
       "alarmStreamInfoTableEntry": alarmStreamInfoTableEntry,
       "alarmChannelNo": alarmChannelNo,
       "alarmCompression": alarmCompression,
       "alarmFPS": alarmFPS,
       "alarmResolution": alarmResolution,
       "extraStreamInfo": extraStreamInfo,
       "extra1StreamInfoTable": extra1StreamInfoTable,
       "extra1StreamInfoEntry": extra1StreamInfoEntry,
       "extra1ChannelNo": extra1ChannelNo,
       "extra1Compression": extra1Compression,
       "extra1FPS": extra1FPS,
       "extra1Resolution": extra1Resolution,
       "eventConfig": eventConfig,
       "videoDetectConfig": videoDetectConfig,
       "videoMotionInfoTable": videoMotionInfoTable,
       "videoMotionInfoEntry": videoMotionInfoEntry,
       "videoMotionIndex": videoMotionIndex,
       "videoLossInfoTable": videoLossInfoTable,
       "videoLossInfoEntry": videoLossInfoEntry,
       "videoLossIndex": videoLossIndex,
       "videoBlindInfoTable": videoBlindInfoTable,
       "videoBlindInfoEntry": videoBlindInfoEntry,
       "videoBlindIndex": videoBlindIndex,
       "alarmConfig": alarmConfig,
       "localAlarmInfoTable": localAlarmInfoTable,
       "localAlarmInfoEntry": localAlarmInfoEntry,
       "localAlarmIndex": localAlarmIndex,
       "networkAlarmInfoTable": networkAlarmInfoTable,
       "networkAlarmInfoEntry": networkAlarmInfoEntry,
       "networkAlarmIndex": networkAlarmIndex,
       "exceptionConfig": exceptionConfig,
       "recordConfig": recordConfig,
       "recordPlanInfo": recordPlanInfo,
       "recordMainStreamInfoTable": recordMainStreamInfoTable,
       "recordMainStreamInfoEntry": recordMainStreamInfoEntry,
       "recordMainChannelIndex": recordMainChannelIndex,
       "storageInfo": storageInfo,
       "physicalVolumeInfoTable": physicalVolumeInfoTable,
       "physicalVolumeInfoEntry": physicalVolumeInfoEntry,
       "physicalVolumeIndex": physicalVolumeIndex,
       "physicNo": physicNo,
       "logicNo": logicNo,
       "physicalVolumeName": physicalVolumeName,
       "physicalVolumeStatus": physicalVolumeStatus,
       "products": products,
       "dvr": dvr,
       "nvr": nvr,
       "ipc": ipc,
       "notification": notification,
       "snmpStatusEvent": snmpStatusEvent,
       "multiMediaEvent": multiMediaEvent,
       "videoMotionEvent": videoMotionEvent,
       "videoBlindEvent": videoBlindEvent,
       "videoLossEvent": videoLossEvent,
       "alarmEvent": alarmEvent,
       "localAlarmEvent": localAlarmEvent,
       "storageEvent": storageEvent,
       "storageFailureEvent": storageFailureEvent,
       "storageLowSpaceEvent": storageLowSpaceEvent,
       "storageInOutEvent": storageInOutEvent,
       "storageSMARTAbnormityEvent": storageSMARTAbnormityEvent,
       "recordEvent": recordEvent,
       "recordMainStreamEvent": recordMainStreamEvent,
       "recordExtraStreamEvent": recordExtraStreamEvent,
       "dahuaSnmpTrap": dahuaSnmpTrap,
       "action": action,
       "currentTime": currentTime,
       "snmpStatus": snmpStatus,
       "physicalVolumeThreshold": physicalVolumeThreshold}
)
