# SNMP MIB module (SUPERMICRO-CAPWAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-CAPWAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:01:57 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsCapwap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82)
)
if mibBuilder.loadTexts:
    fsCapwap.setRevisions(
        ("2013-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class CapwapBaseRadioIdTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )



class CapwapBaseTunnelModeTC(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("localBridging", 0),
          ("dot3Tunnel", 1),
          ("nativeTunnel", 2))
    )


class CapwapBaseMacTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localMAC", 0),
          ("splitMAC", 1),
          ("both", 2))
    )



class CapwapBaseStationIdTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
        ValueSizeConstraint(8, 8),
    )



# MIB Managed Objects in the order of their OIDs

_FsCapwapSystem_ObjectIdentity = ObjectIdentity
fsCapwapSystem = _FsCapwapSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1)
)


class _FsCapwapModuleStatus_Type(EnabledStatus):
    """Custom type fsCapwapModuleStatus based on EnabledStatus"""
    defaultValue = 1


_FsCapwapModuleStatus_Type.__name__ = "EnabledStatus"
_FsCapwapModuleStatus_Object = MibScalar
fsCapwapModuleStatus = _FsCapwapModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 1),
    _FsCapwapModuleStatus_Type()
)
fsCapwapModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapModuleStatus.setStatus("current")


class _FsCapwapSystemControl_Type(TruthValue):
    """Custom type fsCapwapSystemControl based on TruthValue"""
    defaultValue = 1


_FsCapwapSystemControl_Type.__name__ = "TruthValue"
_FsCapwapSystemControl_Object = MibScalar
fsCapwapSystemControl = _FsCapwapSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 2),
    _FsCapwapSystemControl_Type()
)
fsCapwapSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapSystemControl.setStatus("current")


class _FsCapwapControlUdpPort_Type(Unsigned32):
    """Custom type fsCapwapControlUdpPort based on Unsigned32"""
    defaultValue = 5246

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsCapwapControlUdpPort_Type.__name__ = "Unsigned32"
_FsCapwapControlUdpPort_Object = MibScalar
fsCapwapControlUdpPort = _FsCapwapControlUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 3),
    _FsCapwapControlUdpPort_Type()
)
fsCapwapControlUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapControlUdpPort.setStatus("current")


class _FsCapwapControlChannelDTLSPolicyOptions_Type(Bits):
    """Custom type fsCapwapControlChannelDTLSPolicyOptions based on Bits"""
    defaultHexValue = "01"

    namedValues = NamedValues(
        *(("other", 0),
          ("clear", 1),
          ("dtls", 2))
    )

_FsCapwapControlChannelDTLSPolicyOptions_Type.__name__ = "Bits"
_FsCapwapControlChannelDTLSPolicyOptions_Object = MibScalar
fsCapwapControlChannelDTLSPolicyOptions = _FsCapwapControlChannelDTLSPolicyOptions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 4),
    _FsCapwapControlChannelDTLSPolicyOptions_Type()
)
fsCapwapControlChannelDTLSPolicyOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapControlChannelDTLSPolicyOptions.setStatus("current")


class _FsCapwapDataChannelDTLSPolicyOptions_Type(Bits):
    """Custom type fsCapwapDataChannelDTLSPolicyOptions based on Bits"""
    defaultHexValue = "01"

    namedValues = NamedValues(
        *(("other", 0),
          ("clear", 1),
          ("dtls", 2))
    )

_FsCapwapDataChannelDTLSPolicyOptions_Type.__name__ = "Bits"
_FsCapwapDataChannelDTLSPolicyOptions_Object = MibScalar
fsCapwapDataChannelDTLSPolicyOptions = _FsCapwapDataChannelDTLSPolicyOptions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 5),
    _FsCapwapDataChannelDTLSPolicyOptions_Type()
)
fsCapwapDataChannelDTLSPolicyOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDataChannelDTLSPolicyOptions.setStatus("current")


class _FsWlcDiscoveryMode_Type(Bits):
    """Custom type fsWlcDiscoveryMode based on Bits"""
    defaultHexValue = "01"

    namedValues = NamedValues(
        *(("other", 0),
          ("macDiscMode", 1),
          ("autoDiscMode", 2))
    )

_FsWlcDiscoveryMode_Type.__name__ = "Bits"
_FsWlcDiscoveryMode_Object = MibScalar
fsWlcDiscoveryMode = _FsWlcDiscoveryMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 6),
    _FsWlcDiscoveryMode_Type()
)
fsWlcDiscoveryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWlcDiscoveryMode.setStatus("current")


class _FsCapwapWtpModeIgnore_Type(EnabledStatus):
    """Custom type fsCapwapWtpModeIgnore based on EnabledStatus"""
    defaultValue = 1


_FsCapwapWtpModeIgnore_Type.__name__ = "EnabledStatus"
_FsCapwapWtpModeIgnore_Object = MibScalar
fsCapwapWtpModeIgnore = _FsCapwapWtpModeIgnore_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 7),
    _FsCapwapWtpModeIgnore_Type()
)
fsCapwapWtpModeIgnore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpModeIgnore.setStatus("current")


class _FsCapwapDebugMask_Type(Integer32):
    """Custom type fsCapwapDebugMask based on Integer32"""
    defaultValue = 0


_FsCapwapDebugMask_Type.__name__ = "Integer32"
_FsCapwapDebugMask_Object = MibScalar
fsCapwapDebugMask = _FsCapwapDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 8),
    _FsCapwapDebugMask_Type()
)
fsCapwapDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDebugMask.setStatus("current")


class _FsDtlsDebugMask_Type(Integer32):
    """Custom type fsDtlsDebugMask based on Integer32"""
    defaultValue = 0


_FsDtlsDebugMask_Type.__name__ = "Integer32"
_FsDtlsDebugMask_Object = MibScalar
fsDtlsDebugMask = _FsDtlsDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 9),
    _FsDtlsDebugMask_Type()
)
fsDtlsDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDtlsDebugMask.setStatus("current")


class _FsDtlsEncryption_Type(Integer32):
    """Custom type fsDtlsEncryption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preShared", 1),
          ("certificates", 2))
    )


_FsDtlsEncryption_Type.__name__ = "Integer32"
_FsDtlsEncryption_Object = MibScalar
fsDtlsEncryption = _FsDtlsEncryption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 10),
    _FsDtlsEncryption_Type()
)
fsDtlsEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDtlsEncryption.setStatus("current")


class _FsDtlsEncryptAlgorithm_Type(Integer32):
    """Custom type fsDtlsEncryptAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes128", 1),
          ("dheaes128", 2),
          ("aes256", 3),
          ("dhaaes256", 4))
    )


_FsDtlsEncryptAlgorithm_Type.__name__ = "Integer32"
_FsDtlsEncryptAlgorithm_Object = MibScalar
fsDtlsEncryptAlgorithm = _FsDtlsEncryptAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 11),
    _FsDtlsEncryptAlgorithm_Type()
)
fsDtlsEncryptAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDtlsEncryptAlgorithm.setStatus("current")


class _FsStationType_Type(Integer32):
    """Custom type fsStationType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("blacklist", 1),
          ("whitelist", 2))
    )


_FsStationType_Type.__name__ = "Integer32"
_FsStationType_Object = MibScalar
fsStationType = _FsStationType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 1, 12),
    _FsStationType_Type()
)
fsStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsStationType.setStatus("current")
_FsCapwapWtpModel_ObjectIdentity = ObjectIdentity
fsCapwapWtpModel = _FsCapwapWtpModel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2)
)
_FsWtpModelTable_Object = MibTable
fsWtpModelTable = _FsWtpModelTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1)
)
if mibBuilder.loadTexts:
    fsWtpModelTable.setStatus("current")
_FsWtpModelEntry_Object = MibTableRow
fsWtpModelEntry = _FsWtpModelEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1)
)
fsWtpModelEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapWtpModelNumber"),
)
if mibBuilder.loadTexts:
    fsWtpModelEntry.setStatus("current")


class _FsCapwapWtpModelNumber_Type(SnmpAdminString):
    """Custom type fsCapwapWtpModelNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsCapwapWtpModelNumber_Type.__name__ = "SnmpAdminString"
_FsCapwapWtpModelNumber_Object = MibTableColumn
fsCapwapWtpModelNumber = _FsCapwapWtpModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 1),
    _FsCapwapWtpModelNumber_Type()
)
fsCapwapWtpModelNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCapwapWtpModelNumber.setStatus("current")
_FsNoOfRadio_Type = CapwapBaseRadioIdTC
_FsNoOfRadio_Object = MibTableColumn
fsNoOfRadio = _FsNoOfRadio_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 2),
    _FsNoOfRadio_Type()
)
fsNoOfRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNoOfRadio.setStatus("current")


class _FsCapwapWtpMacType_Type(CapwapBaseMacTypeTC):
    """Custom type fsCapwapWtpMacType based on CapwapBaseMacTypeTC"""
    defaultValue = 0


_FsCapwapWtpMacType_Type.__name__ = "CapwapBaseMacTypeTC"
_FsCapwapWtpMacType_Object = MibTableColumn
fsCapwapWtpMacType = _FsCapwapWtpMacType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 3),
    _FsCapwapWtpMacType_Type()
)
fsCapwapWtpMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpMacType.setStatus("current")


class _FsCapwapWtpTunnelMode_Type(CapwapBaseTunnelModeTC):
    """Custom type fsCapwapWtpTunnelMode based on CapwapBaseTunnelModeTC"""
    defaultHexValue = ""


_FsCapwapWtpTunnelMode_Type.__name__ = "CapwapBaseTunnelModeTC"
_FsCapwapWtpTunnelMode_Object = MibTableColumn
fsCapwapWtpTunnelMode = _FsCapwapWtpTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 4),
    _FsCapwapWtpTunnelMode_Type()
)
fsCapwapWtpTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpTunnelMode.setStatus("current")


class _FsCapwapSwVersion_Type(DisplayString):
    """Custom type fsCapwapSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_FsCapwapSwVersion_Type.__name__ = "DisplayString"
_FsCapwapSwVersion_Object = MibTableColumn
fsCapwapSwVersion = _FsCapwapSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 5),
    _FsCapwapSwVersion_Type()
)
fsCapwapSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapSwVersion.setStatus("current")


class _FsCapwapImageName_Type(DisplayString):
    """Custom type fsCapwapImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_FsCapwapImageName_Type.__name__ = "DisplayString"
_FsCapwapImageName_Object = MibTableColumn
fsCapwapImageName = _FsCapwapImageName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 6),
    _FsCapwapImageName_Type()
)
fsCapwapImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapImageName.setStatus("current")
_FsCapwapQosProfileName_Type = OctetString
_FsCapwapQosProfileName_Object = MibTableColumn
fsCapwapQosProfileName = _FsCapwapQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 7),
    _FsCapwapQosProfileName_Type()
)
fsCapwapQosProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapQosProfileName.setStatus("current")
_FsMaxStations_Type = Integer32
_FsMaxStations_Object = MibTableColumn
fsMaxStations = _FsMaxStations_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 8),
    _FsMaxStations_Type()
)
fsMaxStations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMaxStations.setStatus("current")
_FsWtpModelRowStatus_Type = RowStatus
_FsWtpModelRowStatus_Object = MibTableColumn
fsWtpModelRowStatus = _FsWtpModelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 1, 1, 9),
    _FsWtpModelRowStatus_Type()
)
fsWtpModelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWtpModelRowStatus.setStatus("current")
_FsWtpRadioTable_Object = MibTable
fsWtpRadioTable = _FsWtpRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 2)
)
if mibBuilder.loadTexts:
    fsWtpRadioTable.setStatus("current")
_FsWtpRadioEntry_Object = MibTableRow
fsWtpRadioEntry = _FsWtpRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 2, 1)
)
fsWtpRadioEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapWtpModelNumber"),
    (0, "SUPERMICRO-CAPWAP-MIB", "fsRadioNumber"),
)
if mibBuilder.loadTexts:
    fsWtpRadioEntry.setStatus("current")
_FsRadioNumber_Type = CapwapBaseRadioIdTC
_FsRadioNumber_Object = MibTableColumn
fsRadioNumber = _FsRadioNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 2, 1, 1),
    _FsRadioNumber_Type()
)
fsRadioNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRadioNumber.setStatus("current")


class _FsWtpRadioType_Type(Integer32):
    """Custom type fsWtpRadioType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              10,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dot11b", 1),
          ("dot11a", 2),
          ("dot11g", 4),
          ("dot11bg", 5),
          ("dot11an", 10),
          ("dot11bgn", 13))
    )


_FsWtpRadioType_Type.__name__ = "Integer32"
_FsWtpRadioType_Object = MibTableColumn
fsWtpRadioType = _FsWtpRadioType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 2, 1, 2),
    _FsWtpRadioType_Type()
)
fsWtpRadioType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpRadioType.setStatus("current")


class _FsRadioAdminStatus_Type(EnabledStatus):
    """Custom type fsRadioAdminStatus based on EnabledStatus"""
    defaultValue = 1


_FsRadioAdminStatus_Type.__name__ = "EnabledStatus"
_FsRadioAdminStatus_Object = MibTableColumn
fsRadioAdminStatus = _FsRadioAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 2, 1, 3),
    _FsRadioAdminStatus_Type()
)
fsRadioAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRadioAdminStatus.setStatus("current")
_FsWtpRadioRowStatus_Type = RowStatus
_FsWtpRadioRowStatus_Object = MibTableColumn
fsWtpRadioRowStatus = _FsWtpRadioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 2, 2, 1, 4),
    _FsWtpRadioRowStatus_Type()
)
fsWtpRadioRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWtpRadioRowStatus.setStatus("current")
_FsCapwapConfig_ObjectIdentity = ObjectIdentity
fsCapwapConfig = _FsCapwapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3)
)
_FsCapwapWhiteListTable_Object = MibTable
fsCapwapWhiteListTable = _FsCapwapWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 1)
)
if mibBuilder.loadTexts:
    fsCapwapWhiteListTable.setStatus("current")
_FsCapwapWhiteListEntry_Object = MibTableRow
fsCapwapWhiteListEntry = _FsCapwapWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 1, 1)
)
fsCapwapWhiteListEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapWhiteListId"),
)
if mibBuilder.loadTexts:
    fsCapwapWhiteListEntry.setStatus("current")


class _FsCapwapWhiteListId_Type(Unsigned32):
    """Custom type fsCapwapWhiteListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_FsCapwapWhiteListId_Type.__name__ = "Unsigned32"
_FsCapwapWhiteListId_Object = MibTableColumn
fsCapwapWhiteListId = _FsCapwapWhiteListId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 1, 1, 1),
    _FsCapwapWhiteListId_Type()
)
fsCapwapWhiteListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCapwapWhiteListId.setStatus("current")
_FsCapwapWhiteListWtpBaseMac_Type = MacAddress
_FsCapwapWhiteListWtpBaseMac_Object = MibTableColumn
fsCapwapWhiteListWtpBaseMac = _FsCapwapWhiteListWtpBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 1, 1, 2),
    _FsCapwapWhiteListWtpBaseMac_Type()
)
fsCapwapWhiteListWtpBaseMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWhiteListWtpBaseMac.setStatus("current")
_FsCapwapWhiteListRowStatus_Type = RowStatus
_FsCapwapWhiteListRowStatus_Object = MibTableColumn
fsCapwapWhiteListRowStatus = _FsCapwapWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 1, 1, 3),
    _FsCapwapWhiteListRowStatus_Type()
)
fsCapwapWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapWhiteListRowStatus.setStatus("current")
_FsCapwapBlackListTable_Object = MibTable
fsCapwapBlackListTable = _FsCapwapBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 2)
)
if mibBuilder.loadTexts:
    fsCapwapBlackListTable.setStatus("current")
_FsCapwapBlackListEntry_Object = MibTableRow
fsCapwapBlackListEntry = _FsCapwapBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 2, 1)
)
fsCapwapBlackListEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapBlackListId"),
)
if mibBuilder.loadTexts:
    fsCapwapBlackListEntry.setStatus("current")


class _FsCapwapBlackListId_Type(Unsigned32):
    """Custom type fsCapwapBlackListId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_FsCapwapBlackListId_Type.__name__ = "Unsigned32"
_FsCapwapBlackListId_Object = MibTableColumn
fsCapwapBlackListId = _FsCapwapBlackListId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 2, 1, 1),
    _FsCapwapBlackListId_Type()
)
fsCapwapBlackListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCapwapBlackListId.setStatus("current")
_FsCapwapBlackListWtpBaseMac_Type = MacAddress
_FsCapwapBlackListWtpBaseMac_Object = MibTableColumn
fsCapwapBlackListWtpBaseMac = _FsCapwapBlackListWtpBaseMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 2, 1, 2),
    _FsCapwapBlackListWtpBaseMac_Type()
)
fsCapwapBlackListWtpBaseMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapBlackListWtpBaseMac.setStatus("current")
_FsCapwapBlackListRowStatus_Type = RowStatus
_FsCapwapBlackListRowStatus_Object = MibTableColumn
fsCapwapBlackListRowStatus = _FsCapwapBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 2, 1, 3),
    _FsCapwapBlackListRowStatus_Type()
)
fsCapwapBlackListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapBlackListRowStatus.setStatus("current")
_FsCapwapWtpConfigTable_Object = MibTable
fsCapwapWtpConfigTable = _FsCapwapWtpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3)
)
if mibBuilder.loadTexts:
    fsCapwapWtpConfigTable.setStatus("current")
_FsCapwapWtpConfigEntry_Object = MibTableRow
fsCapwapWtpConfigEntry = _FsCapwapWtpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1)
)
fsCapwapWtpConfigEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCapwapWtpConfigEntry.setStatus("current")


class _FsCapwapWtpReset_Type(EnabledStatus):
    """Custom type fsCapwapWtpReset based on EnabledStatus"""
    defaultValue = 2


_FsCapwapWtpReset_Type.__name__ = "EnabledStatus"
_FsCapwapWtpReset_Object = MibTableColumn
fsCapwapWtpReset = _FsCapwapWtpReset_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 1),
    _FsCapwapWtpReset_Type()
)
fsCapwapWtpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpReset.setStatus("current")


class _FsCapwapClearConfig_Type(EnabledStatus):
    """Custom type fsCapwapClearConfig based on EnabledStatus"""
    defaultValue = 2


_FsCapwapClearConfig_Type.__name__ = "EnabledStatus"
_FsCapwapClearConfig_Object = MibTableColumn
fsCapwapClearConfig = _FsCapwapClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 2),
    _FsCapwapClearConfig_Type()
)
fsCapwapClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapClearConfig.setStatus("current")


class _FsWtpDiscoveryType_Type(Integer32):
    """Custom type fsWtpDiscoveryType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("static", 1),
          ("dhcp", 2),
          ("dns", 3),
          ("acReferral", 4))
    )


_FsWtpDiscoveryType_Type.__name__ = "Integer32"
_FsWtpDiscoveryType_Object = MibTableColumn
fsWtpDiscoveryType = _FsWtpDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 3),
    _FsWtpDiscoveryType_Type()
)
fsWtpDiscoveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpDiscoveryType.setStatus("current")


class _FsWtpCountryString_Type(OctetString):
    """Custom type fsWtpCountryString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_FsWtpCountryString_Type.__name__ = "OctetString"
_FsWtpCountryString_Object = MibTableColumn
fsWtpCountryString = _FsWtpCountryString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 4),
    _FsWtpCountryString_Type()
)
fsWtpCountryString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpCountryString.setStatus("current")
_FsWtpCrashDumpFileName_Type = DisplayString
_FsWtpCrashDumpFileName_Object = MibTableColumn
fsWtpCrashDumpFileName = _FsWtpCrashDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 5),
    _FsWtpCrashDumpFileName_Type()
)
fsWtpCrashDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpCrashDumpFileName.setStatus("current")
_FsWtpMemoryDumpFileName_Type = DisplayString
_FsWtpMemoryDumpFileName_Object = MibTableColumn
fsWtpMemoryDumpFileName = _FsWtpMemoryDumpFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 6),
    _FsWtpMemoryDumpFileName_Type()
)
fsWtpMemoryDumpFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpMemoryDumpFileName.setStatus("current")


class _FsWtpDeleteOperation_Type(EnabledStatus):
    """Custom type fsWtpDeleteOperation based on EnabledStatus"""
    defaultValue = 2


_FsWtpDeleteOperation_Type.__name__ = "EnabledStatus"
_FsWtpDeleteOperation_Object = MibTableColumn
fsWtpDeleteOperation = _FsWtpDeleteOperation_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 7),
    _FsWtpDeleteOperation_Type()
)
fsWtpDeleteOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpDeleteOperation.setStatus("current")


class _FsCapwapClearApStats_Type(EnabledStatus):
    """Custom type fsCapwapClearApStats based on EnabledStatus"""
    defaultValue = 2


_FsCapwapClearApStats_Type.__name__ = "EnabledStatus"
_FsCapwapClearApStats_Object = MibTableColumn
fsCapwapClearApStats = _FsCapwapClearApStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 8),
    _FsCapwapClearApStats_Type()
)
fsCapwapClearApStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapClearApStats.setStatus("current")
_FsCapwapWtpConfigRowStatus_Type = RowStatus
_FsCapwapWtpConfigRowStatus_Object = MibTableColumn
fsCapwapWtpConfigRowStatus = _FsCapwapWtpConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 3, 1, 9),
    _FsCapwapWtpConfigRowStatus_Type()
)
fsCapwapWtpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapWtpConfigRowStatus.setStatus("current")
_FsCapwapLinkEncryptionTable_Object = MibTable
fsCapwapLinkEncryptionTable = _FsCapwapLinkEncryptionTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 4)
)
if mibBuilder.loadTexts:
    fsCapwapLinkEncryptionTable.setStatus("current")
_FsCapwapLinkEncryptionEntry_Object = MibTableRow
fsCapwapLinkEncryptionEntry = _FsCapwapLinkEncryptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 4, 1)
)
fsCapwapLinkEncryptionEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapEncryptChannel"),
)
if mibBuilder.loadTexts:
    fsCapwapLinkEncryptionEntry.setStatus("current")


class _FsCapwapEncryptChannel_Type(Integer32):
    """Custom type fsCapwapEncryptChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 1),
          ("data", 2))
    )


_FsCapwapEncryptChannel_Type.__name__ = "Integer32"
_FsCapwapEncryptChannel_Object = MibTableColumn
fsCapwapEncryptChannel = _FsCapwapEncryptChannel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 4, 1, 1),
    _FsCapwapEncryptChannel_Type()
)
fsCapwapEncryptChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCapwapEncryptChannel.setStatus("current")


class _FsCapwapEncryptChannelStatus_Type(EnabledStatus):
    """Custom type fsCapwapEncryptChannelStatus based on EnabledStatus"""
    defaultValue = 2


_FsCapwapEncryptChannelStatus_Type.__name__ = "EnabledStatus"
_FsCapwapEncryptChannelStatus_Object = MibTableColumn
fsCapwapEncryptChannelStatus = _FsCapwapEncryptChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 4, 1, 2),
    _FsCapwapEncryptChannelStatus_Type()
)
fsCapwapEncryptChannelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapEncryptChannelStatus.setStatus("current")
_FsCapwapEncryptChannelRowStatus_Type = RowStatus
_FsCapwapEncryptChannelRowStatus_Object = MibTableColumn
fsCapwapEncryptChannelRowStatus = _FsCapwapEncryptChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 4, 1, 3),
    _FsCapwapEncryptChannelRowStatus_Type()
)
fsCapwapEncryptChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapEncryptChannelRowStatus.setStatus("current")
_FsCapwapDefaultWtpProfileTable_Object = MibTable
fsCapwapDefaultWtpProfileTable = _FsCapwapDefaultWtpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 5)
)
if mibBuilder.loadTexts:
    fsCapwapDefaultWtpProfileTable.setStatus("current")
_FsCapwapDefaultWtpProfileEntry_Object = MibTableRow
fsCapwapDefaultWtpProfileEntry = _FsCapwapDefaultWtpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 5, 1)
)
fsCapwapDefaultWtpProfileEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapWtpModelNumber"),
)
if mibBuilder.loadTexts:
    fsCapwapDefaultWtpProfileEntry.setStatus("current")


class _FsCapwapDefaultQosProfile_Type(OctetString):
    """Custom type fsCapwapDefaultQosProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(31, 31),
    )
    fixed_length = 31


_FsCapwapDefaultQosProfile_Type.__name__ = "OctetString"
_FsCapwapDefaultQosProfile_Object = MibTableColumn
fsCapwapDefaultQosProfile = _FsCapwapDefaultQosProfile_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 5, 1, 1),
    _FsCapwapDefaultQosProfile_Type()
)
fsCapwapDefaultQosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDefaultQosProfile.setStatus("current")
_FsCapwapDefaultWtpProfileRowStatus_Type = RowStatus
_FsCapwapDefaultWtpProfileRowStatus_Object = MibTableColumn
fsCapwapDefaultWtpProfileRowStatus = _FsCapwapDefaultWtpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 5, 1, 2),
    _FsCapwapDefaultWtpProfileRowStatus_Type()
)
fsCapwapDefaultWtpProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDefaultWtpProfileRowStatus.setStatus("current")
_FsCapwapDnsProfileTable_Object = MibTable
fsCapwapDnsProfileTable = _FsCapwapDnsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 6)
)
if mibBuilder.loadTexts:
    fsCapwapDnsProfileTable.setStatus("current")
_FsCapwapDnsProfileEntry_Object = MibTableRow
fsCapwapDnsProfileEntry = _FsCapwapDnsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 6, 1)
)
fsCapwapDnsProfileEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCapwapDnsProfileEntry.setStatus("current")


class _FsCapwapDnsAddressType_Type(InetAddressType):
    """Custom type fsCapwapDnsAddressType based on InetAddressType"""
    defaultValue = 1


_FsCapwapDnsAddressType_Type.__name__ = "InetAddressType"
_FsCapwapDnsAddressType_Object = MibTableColumn
fsCapwapDnsAddressType = _FsCapwapDnsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 6, 1, 1),
    _FsCapwapDnsAddressType_Type()
)
fsCapwapDnsAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDnsAddressType.setStatus("current")


class _FsCapwapDnsServerIp_Type(InetAddress):
    """Custom type fsCapwapDnsServerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_FsCapwapDnsServerIp_Type.__name__ = "InetAddress"
_FsCapwapDnsServerIp_Object = MibTableColumn
fsCapwapDnsServerIp = _FsCapwapDnsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 6, 1, 2),
    _FsCapwapDnsServerIp_Type()
)
fsCapwapDnsServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDnsServerIp.setStatus("current")


class _FsCapwapDnsDomainName_Type(SnmpAdminString):
    """Custom type fsCapwapDnsDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsCapwapDnsDomainName_Type.__name__ = "SnmpAdminString"
_FsCapwapDnsDomainName_Object = MibTableColumn
fsCapwapDnsDomainName = _FsCapwapDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 6, 1, 3),
    _FsCapwapDnsDomainName_Type()
)
fsCapwapDnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDnsDomainName.setStatus("current")
_FsCapwapDnsProfileRowStatus_Type = RowStatus
_FsCapwapDnsProfileRowStatus_Object = MibTableColumn
fsCapwapDnsProfileRowStatus = _FsCapwapDnsProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 6, 1, 4),
    _FsCapwapDnsProfileRowStatus_Type()
)
fsCapwapDnsProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapDnsProfileRowStatus.setStatus("current")
_FsWtpNativeVlanIdTable_Object = MibTable
fsWtpNativeVlanIdTable = _FsWtpNativeVlanIdTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 7)
)
if mibBuilder.loadTexts:
    fsWtpNativeVlanIdTable.setStatus("current")
_FsWtpNativeVlanIdEntry_Object = MibTableRow
fsWtpNativeVlanIdEntry = _FsWtpNativeVlanIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 7, 1)
)
fsWtpNativeVlanIdEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsWtpNativeVlanIdEntry.setStatus("current")


class _FsWtpNativeVlanId_Type(Integer32):
    """Custom type fsWtpNativeVlanId based on Integer32"""
    defaultValue = 0


_FsWtpNativeVlanId_Type.__name__ = "Integer32"
_FsWtpNativeVlanId_Object = MibTableColumn
fsWtpNativeVlanId = _FsWtpNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 7, 1, 1),
    _FsWtpNativeVlanId_Type()
)
fsWtpNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWtpNativeVlanId.setStatus("current")
_FsWtpNativeVlanIdRowStatus_Type = RowStatus
_FsWtpNativeVlanIdRowStatus_Object = MibTableColumn
fsWtpNativeVlanIdRowStatus = _FsWtpNativeVlanIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 7, 1, 2),
    _FsWtpNativeVlanIdRowStatus_Type()
)
fsWtpNativeVlanIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWtpNativeVlanIdRowStatus.setStatus("current")
_FsCawapDiscStatsTable_Object = MibTable
fsCawapDiscStatsTable = _FsCawapDiscStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8)
)
if mibBuilder.loadTexts:
    fsCawapDiscStatsTable.setStatus("current")
_FsCawapDiscStatsEntry_Object = MibTableRow
fsCawapDiscStatsEntry = _FsCawapDiscStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1)
)
fsCawapDiscStatsEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCawapDiscStatsEntry.setStatus("current")


class _FsCapwapDiscReqReceived_Type(Unsigned32):
    """Custom type fsCapwapDiscReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapDiscReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapDiscReqReceived_Object = MibTableColumn
fsCapwapDiscReqReceived = _FsCapwapDiscReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 1),
    _FsCapwapDiscReqReceived_Type()
)
fsCapwapDiscReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscReqReceived.setStatus("current")


class _FsCapwapDiscRspReceived_Type(Unsigned32):
    """Custom type fsCapwapDiscRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapDiscRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapDiscRspReceived_Object = MibTableColumn
fsCapwapDiscRspReceived = _FsCapwapDiscRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 2),
    _FsCapwapDiscRspReceived_Type()
)
fsCapwapDiscRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscRspReceived.setStatus("current")


class _FsCapwapDiscReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapDiscReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapDiscReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapDiscReqTransmitted_Object = MibTableColumn
fsCapwapDiscReqTransmitted = _FsCapwapDiscReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 3),
    _FsCapwapDiscReqTransmitted_Type()
)
fsCapwapDiscReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscReqTransmitted.setStatus("current")


class _FsCapwapDiscRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapDiscRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapDiscRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapDiscRspTransmitted_Object = MibTableColumn
fsCapwapDiscRspTransmitted = _FsCapwapDiscRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 4),
    _FsCapwapDiscRspTransmitted_Type()
)
fsCapwapDiscRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscRspTransmitted.setStatus("current")


class _FsCapwapDiscunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapDiscunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapDiscunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapDiscunsuccessfulProcessed_Object = MibTableColumn
fsCapwapDiscunsuccessfulProcessed = _FsCapwapDiscunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 5),
    _FsCapwapDiscunsuccessfulProcessed_Type()
)
fsCapwapDiscunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscunsuccessfulProcessed.setStatus("current")


class _FsCapwapDiscLastUnsuccAttemptReason_Type(Integer32):
    """Custom type fsCapwapDiscLastUnsuccAttemptReason based on Integer32"""
    defaultValue = 0


_FsCapwapDiscLastUnsuccAttemptReason_Type.__name__ = "Integer32"
_FsCapwapDiscLastUnsuccAttemptReason_Object = MibTableColumn
fsCapwapDiscLastUnsuccAttemptReason = _FsCapwapDiscLastUnsuccAttemptReason_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 6),
    _FsCapwapDiscLastUnsuccAttemptReason_Type()
)
fsCapwapDiscLastUnsuccAttemptReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscLastUnsuccAttemptReason.setStatus("current")
_FsCapwapDiscLastSuccAttemptTime_Type = TimeTicks
_FsCapwapDiscLastSuccAttemptTime_Object = MibTableColumn
fsCapwapDiscLastSuccAttemptTime = _FsCapwapDiscLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 7),
    _FsCapwapDiscLastSuccAttemptTime_Type()
)
fsCapwapDiscLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscLastSuccAttemptTime.setStatus("current")
_FsCapwapDiscLastUnsuccessfulAttemptTime_Type = TimeTicks
_FsCapwapDiscLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapDiscLastUnsuccessfulAttemptTime = _FsCapwapDiscLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 8),
    _FsCapwapDiscLastUnsuccessfulAttemptTime_Type()
)
fsCapwapDiscLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscLastUnsuccessfulAttemptTime.setStatus("current")
_FsCapwapDiscStatsRowStatus_Type = RowStatus
_FsCapwapDiscStatsRowStatus_Object = MibTableColumn
fsCapwapDiscStatsRowStatus = _FsCapwapDiscStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 8, 1, 9),
    _FsCapwapDiscStatsRowStatus_Type()
)
fsCapwapDiscStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapDiscStatsRowStatus.setStatus("current")
_FsCawapJoinStatsTable_Object = MibTable
fsCawapJoinStatsTable = _FsCawapJoinStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9)
)
if mibBuilder.loadTexts:
    fsCawapJoinStatsTable.setStatus("current")
_FsCawapJoinStatsEntry_Object = MibTableRow
fsCawapJoinStatsEntry = _FsCawapJoinStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1)
)
fsCawapJoinStatsEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCawapJoinStatsEntry.setStatus("current")


class _FsCapwapJoinReqReceived_Type(Unsigned32):
    """Custom type fsCapwapJoinReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapJoinReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapJoinReqReceived_Object = MibTableColumn
fsCapwapJoinReqReceived = _FsCapwapJoinReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 1),
    _FsCapwapJoinReqReceived_Type()
)
fsCapwapJoinReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinReqReceived.setStatus("current")


class _FsCapwapJoinRspReceived_Type(Unsigned32):
    """Custom type fsCapwapJoinRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapJoinRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapJoinRspReceived_Object = MibTableColumn
fsCapwapJoinRspReceived = _FsCapwapJoinRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 2),
    _FsCapwapJoinRspReceived_Type()
)
fsCapwapJoinRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinRspReceived.setStatus("current")


class _FsCapwapJoinReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapJoinReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapJoinReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapJoinReqTransmitted_Object = MibTableColumn
fsCapwapJoinReqTransmitted = _FsCapwapJoinReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 3),
    _FsCapwapJoinReqTransmitted_Type()
)
fsCapwapJoinReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinReqTransmitted.setStatus("current")


class _FsCapwapJoinRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapJoinRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapJoinRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapJoinRspTransmitted_Object = MibTableColumn
fsCapwapJoinRspTransmitted = _FsCapwapJoinRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 4),
    _FsCapwapJoinRspTransmitted_Type()
)
fsCapwapJoinRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinRspTransmitted.setStatus("current")


class _FsCapwapJoinunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapJoinunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapJoinunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapJoinunsuccessfulProcessed_Object = MibTableColumn
fsCapwapJoinunsuccessfulProcessed = _FsCapwapJoinunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 5),
    _FsCapwapJoinunsuccessfulProcessed_Type()
)
fsCapwapJoinunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinunsuccessfulProcessed.setStatus("current")


class _FsCapwapJoinReasonLastUnsuccAttempt_Type(Integer32):
    """Custom type fsCapwapJoinReasonLastUnsuccAttempt based on Integer32"""
    defaultValue = 0


_FsCapwapJoinReasonLastUnsuccAttempt_Type.__name__ = "Integer32"
_FsCapwapJoinReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapJoinReasonLastUnsuccAttempt = _FsCapwapJoinReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 6),
    _FsCapwapJoinReasonLastUnsuccAttempt_Type()
)
fsCapwapJoinReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapJoinLastSuccAttemptTime_Type = TimeTicks
_FsCapwapJoinLastSuccAttemptTime_Object = MibTableColumn
fsCapwapJoinLastSuccAttemptTime = _FsCapwapJoinLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 7),
    _FsCapwapJoinLastSuccAttemptTime_Type()
)
fsCapwapJoinLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinLastSuccAttemptTime.setStatus("current")
_FsCapwapJoinLastUnsuccAttemptTime_Type = TimeTicks
_FsCapwapJoinLastUnsuccAttemptTime_Object = MibTableColumn
fsCapwapJoinLastUnsuccAttemptTime = _FsCapwapJoinLastUnsuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 8),
    _FsCapwapJoinLastUnsuccAttemptTime_Type()
)
fsCapwapJoinLastUnsuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinLastUnsuccAttemptTime.setStatus("current")
_FsCapwapJoinStatsRowStatus_Type = RowStatus
_FsCapwapJoinStatsRowStatus_Object = MibTableColumn
fsCapwapJoinStatsRowStatus = _FsCapwapJoinStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 9, 1, 9),
    _FsCapwapJoinStatsRowStatus_Type()
)
fsCapwapJoinStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapJoinStatsRowStatus.setStatus("current")
_FsCawapConfigStatsTable_Object = MibTable
fsCawapConfigStatsTable = _FsCawapConfigStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10)
)
if mibBuilder.loadTexts:
    fsCawapConfigStatsTable.setStatus("current")
_FsCawapConfigStatsEntry_Object = MibTableRow
fsCawapConfigStatsEntry = _FsCawapConfigStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1)
)
fsCawapConfigStatsEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCawapConfigStatsEntry.setStatus("current")


class _FsCapwapConfigReqReceived_Type(Unsigned32):
    """Custom type fsCapwapConfigReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapConfigReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapConfigReqReceived_Object = MibTableColumn
fsCapwapConfigReqReceived = _FsCapwapConfigReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 1),
    _FsCapwapConfigReqReceived_Type()
)
fsCapwapConfigReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigReqReceived.setStatus("current")


class _FsCapwapConfigRspReceived_Type(Unsigned32):
    """Custom type fsCapwapConfigRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapConfigRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapConfigRspReceived_Object = MibTableColumn
fsCapwapConfigRspReceived = _FsCapwapConfigRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 2),
    _FsCapwapConfigRspReceived_Type()
)
fsCapwapConfigRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigRspReceived.setStatus("current")


class _FsCapwapConfigReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapConfigReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapConfigReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapConfigReqTransmitted_Object = MibTableColumn
fsCapwapConfigReqTransmitted = _FsCapwapConfigReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 3),
    _FsCapwapConfigReqTransmitted_Type()
)
fsCapwapConfigReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigReqTransmitted.setStatus("current")


class _FsCapwapConfigRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapConfigRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapConfigRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapConfigRspTransmitted_Object = MibTableColumn
fsCapwapConfigRspTransmitted = _FsCapwapConfigRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 4),
    _FsCapwapConfigRspTransmitted_Type()
)
fsCapwapConfigRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigRspTransmitted.setStatus("current")


class _FsCapwapConfigunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapConfigunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapConfigunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapConfigunsuccessfulProcessed_Object = MibTableColumn
fsCapwapConfigunsuccessfulProcessed = _FsCapwapConfigunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 5),
    _FsCapwapConfigunsuccessfulProcessed_Type()
)
fsCapwapConfigunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigunsuccessfulProcessed.setStatus("current")


class _FsCapwapConfigReasonLastUnsuccAttempt_Type(Integer32):
    """Custom type fsCapwapConfigReasonLastUnsuccAttempt based on Integer32"""
    defaultValue = 0


_FsCapwapConfigReasonLastUnsuccAttempt_Type.__name__ = "Integer32"
_FsCapwapConfigReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapConfigReasonLastUnsuccAttempt = _FsCapwapConfigReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 6),
    _FsCapwapConfigReasonLastUnsuccAttempt_Type()
)
fsCapwapConfigReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapConfigLastSuccAttemptTime_Type = TimeTicks
_FsCapwapConfigLastSuccAttemptTime_Object = MibTableColumn
fsCapwapConfigLastSuccAttemptTime = _FsCapwapConfigLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 7),
    _FsCapwapConfigLastSuccAttemptTime_Type()
)
fsCapwapConfigLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigLastSuccAttemptTime.setStatus("current")
_FsCapwapConfigLastUnsuccessfulAttemptTime_Type = TimeTicks
_FsCapwapConfigLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapConfigLastUnsuccessfulAttemptTime = _FsCapwapConfigLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 8),
    _FsCapwapConfigLastUnsuccessfulAttemptTime_Type()
)
fsCapwapConfigLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigLastUnsuccessfulAttemptTime.setStatus("current")
_FsCapwapConfigStatsRowStatus_Type = RowStatus
_FsCapwapConfigStatsRowStatus_Object = MibTableColumn
fsCapwapConfigStatsRowStatus = _FsCapwapConfigStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 10, 1, 9),
    _FsCapwapConfigStatsRowStatus_Type()
)
fsCapwapConfigStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapConfigStatsRowStatus.setStatus("current")
_FsCawapRunStatsTable_Object = MibTable
fsCawapRunStatsTable = _FsCawapRunStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11)
)
if mibBuilder.loadTexts:
    fsCawapRunStatsTable.setStatus("current")
_FsCawapRunStatsEntry_Object = MibTableRow
fsCawapRunStatsEntry = _FsCawapRunStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1)
)
fsCawapRunStatsEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCawapRunStatsEntry.setStatus("current")


class _FsCapwapRunConfigUpdateReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunConfigUpdateReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunConfigUpdateReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunConfigUpdateReqReceived_Object = MibTableColumn
fsCapwapRunConfigUpdateReqReceived = _FsCapwapRunConfigUpdateReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 1),
    _FsCapwapRunConfigUpdateReqReceived_Type()
)
fsCapwapRunConfigUpdateReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateReqReceived.setStatus("current")


class _FsCapwapRunConfigUpdateRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunConfigUpdateRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunConfigUpdateRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunConfigUpdateRspReceived_Object = MibTableColumn
fsCapwapRunConfigUpdateRspReceived = _FsCapwapRunConfigUpdateRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 2),
    _FsCapwapRunConfigUpdateRspReceived_Type()
)
fsCapwapRunConfigUpdateRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateRspReceived.setStatus("current")


class _FsCapwapRunConfigUpdateReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunConfigUpdateReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunConfigUpdateReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunConfigUpdateReqTransmitted_Object = MibTableColumn
fsCapwapRunConfigUpdateReqTransmitted = _FsCapwapRunConfigUpdateReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 3),
    _FsCapwapRunConfigUpdateReqTransmitted_Type()
)
fsCapwapRunConfigUpdateReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateReqTransmitted.setStatus("current")


class _FsCapwapRunConfigUpdateRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunConfigUpdateRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunConfigUpdateRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunConfigUpdateRspTransmitted_Object = MibTableColumn
fsCapwapRunConfigUpdateRspTransmitted = _FsCapwapRunConfigUpdateRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 4),
    _FsCapwapRunConfigUpdateRspTransmitted_Type()
)
fsCapwapRunConfigUpdateRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateRspTransmitted.setStatus("current")


class _FsCapwapRunConfigUpdateunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunConfigUpdateunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunConfigUpdateunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunConfigUpdateunsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunConfigUpdateunsuccessfulProcessed = _FsCapwapRunConfigUpdateunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 5),
    _FsCapwapRunConfigUpdateunsuccessfulProcessed_Type()
)
fsCapwapRunConfigUpdateunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateunsuccessfulProcessed.setStatus("current")
_FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunConfigUpdateReasonLastUnsuccAttempt = _FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 6),
    _FsCapwapRunConfigUpdateReasonLastUnsuccAttempt_Type()
)
fsCapwapRunConfigUpdateReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunConfigUpdateLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunConfigUpdateLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunConfigUpdateLastSuccAttemptTime = _FsCapwapRunConfigUpdateLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 7),
    _FsCapwapRunConfigUpdateLastSuccAttemptTime_Type()
)
fsCapwapRunConfigUpdateLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateLastSuccAttemptTime.setStatus("current")
_FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime = _FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 8),
    _FsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime.setStatus("current")


class _FsCapwapRunStationConfigReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunStationConfigReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunStationConfigReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunStationConfigReqReceived_Object = MibTableColumn
fsCapwapRunStationConfigReqReceived = _FsCapwapRunStationConfigReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 9),
    _FsCapwapRunStationConfigReqReceived_Type()
)
fsCapwapRunStationConfigReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigReqReceived.setStatus("current")


class _FsCapwapRunStationConfigRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunStationConfigRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunStationConfigRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunStationConfigRspReceived_Object = MibTableColumn
fsCapwapRunStationConfigRspReceived = _FsCapwapRunStationConfigRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 10),
    _FsCapwapRunStationConfigRspReceived_Type()
)
fsCapwapRunStationConfigRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigRspReceived.setStatus("current")


class _FsCapwapRunStationConfigReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunStationConfigReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunStationConfigReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunStationConfigReqTransmitted_Object = MibTableColumn
fsCapwapRunStationConfigReqTransmitted = _FsCapwapRunStationConfigReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 11),
    _FsCapwapRunStationConfigReqTransmitted_Type()
)
fsCapwapRunStationConfigReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigReqTransmitted.setStatus("current")


class _FsCapwapRunStationConfigRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunStationConfigRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunStationConfigRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunStationConfigRspTransmitted_Object = MibTableColumn
fsCapwapRunStationConfigRspTransmitted = _FsCapwapRunStationConfigRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 12),
    _FsCapwapRunStationConfigRspTransmitted_Type()
)
fsCapwapRunStationConfigRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigRspTransmitted.setStatus("current")


class _FsCapwapRunStationConfigunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunStationConfigunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunStationConfigunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunStationConfigunsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunStationConfigunsuccessfulProcessed = _FsCapwapRunStationConfigunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 13),
    _FsCapwapRunStationConfigunsuccessfulProcessed_Type()
)
fsCapwapRunStationConfigunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigunsuccessfulProcessed.setStatus("current")
_FsCapwapRunStationConfigReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunStationConfigReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunStationConfigReasonLastUnsuccAttempt = _FsCapwapRunStationConfigReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 14),
    _FsCapwapRunStationConfigReasonLastUnsuccAttempt_Type()
)
fsCapwapRunStationConfigReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunStationConfigLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunStationConfigLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunStationConfigLastSuccAttemptTime = _FsCapwapRunStationConfigLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 15),
    _FsCapwapRunStationConfigLastSuccAttemptTime_Type()
)
fsCapwapRunStationConfigLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigLastSuccAttemptTime.setStatus("current")
_FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunStationConfigLastUnsuccessfulAttemptTime = _FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 16),
    _FsCapwapRunStationConfigLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunStationConfigLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStationConfigLastUnsuccessfulAttemptTime.setStatus("current")


class _FsCapwapRunClearConfigReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunClearConfigReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunClearConfigReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunClearConfigReqReceived_Object = MibTableColumn
fsCapwapRunClearConfigReqReceived = _FsCapwapRunClearConfigReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 17),
    _FsCapwapRunClearConfigReqReceived_Type()
)
fsCapwapRunClearConfigReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigReqReceived.setStatus("current")


class _FsCapwapRunClearConfigRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunClearConfigRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunClearConfigRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunClearConfigRspReceived_Object = MibTableColumn
fsCapwapRunClearConfigRspReceived = _FsCapwapRunClearConfigRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 18),
    _FsCapwapRunClearConfigRspReceived_Type()
)
fsCapwapRunClearConfigRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigRspReceived.setStatus("current")


class _FsCapwapRunClearConfigReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunClearConfigReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunClearConfigReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunClearConfigReqTransmitted_Object = MibTableColumn
fsCapwapRunClearConfigReqTransmitted = _FsCapwapRunClearConfigReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 19),
    _FsCapwapRunClearConfigReqTransmitted_Type()
)
fsCapwapRunClearConfigReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigReqTransmitted.setStatus("current")


class _FsCapwapRunClearConfigRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunClearConfigRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunClearConfigRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunClearConfigRspTransmitted_Object = MibTableColumn
fsCapwapRunClearConfigRspTransmitted = _FsCapwapRunClearConfigRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 20),
    _FsCapwapRunClearConfigRspTransmitted_Type()
)
fsCapwapRunClearConfigRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigRspTransmitted.setStatus("current")


class _FsCapwapRunClearConfigunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunClearConfigunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunClearConfigunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunClearConfigunsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunClearConfigunsuccessfulProcessed = _FsCapwapRunClearConfigunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 21),
    _FsCapwapRunClearConfigunsuccessfulProcessed_Type()
)
fsCapwapRunClearConfigunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigunsuccessfulProcessed.setStatus("current")
_FsCapwapRunClearConfigReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunClearConfigReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunClearConfigReasonLastUnsuccAttempt = _FsCapwapRunClearConfigReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 22),
    _FsCapwapRunClearConfigReasonLastUnsuccAttempt_Type()
)
fsCapwapRunClearConfigReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunClearConfigLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunClearConfigLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunClearConfigLastSuccAttemptTime = _FsCapwapRunClearConfigLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 23),
    _FsCapwapRunClearConfigLastSuccAttemptTime_Type()
)
fsCapwapRunClearConfigLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigLastSuccAttemptTime.setStatus("current")
_FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunClearConfigLastUnsuccessfulAttemptTime = _FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 24),
    _FsCapwapRunClearConfigLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunClearConfigLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunClearConfigLastUnsuccessfulAttemptTime.setStatus("current")


class _FsCapwapRunDataTransferReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunDataTransferReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunDataTransferReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunDataTransferReqReceived_Object = MibTableColumn
fsCapwapRunDataTransferReqReceived = _FsCapwapRunDataTransferReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 25),
    _FsCapwapRunDataTransferReqReceived_Type()
)
fsCapwapRunDataTransferReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferReqReceived.setStatus("current")


class _FsCapwapRunDataTransferRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunDataTransferRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunDataTransferRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunDataTransferRspReceived_Object = MibTableColumn
fsCapwapRunDataTransferRspReceived = _FsCapwapRunDataTransferRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 26),
    _FsCapwapRunDataTransferRspReceived_Type()
)
fsCapwapRunDataTransferRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferRspReceived.setStatus("current")


class _FsCapwapRunDataTransferReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunDataTransferReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunDataTransferReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunDataTransferReqTransmitted_Object = MibTableColumn
fsCapwapRunDataTransferReqTransmitted = _FsCapwapRunDataTransferReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 27),
    _FsCapwapRunDataTransferReqTransmitted_Type()
)
fsCapwapRunDataTransferReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferReqTransmitted.setStatus("current")


class _FsCapwapRunDataTransferRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunDataTransferRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunDataTransferRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunDataTransferRspTransmitted_Object = MibTableColumn
fsCapwapRunDataTransferRspTransmitted = _FsCapwapRunDataTransferRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 28),
    _FsCapwapRunDataTransferRspTransmitted_Type()
)
fsCapwapRunDataTransferRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferRspTransmitted.setStatus("current")


class _FsCapwapRunDataTransferunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunDataTransferunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunDataTransferunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunDataTransferunsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunDataTransferunsuccessfulProcessed = _FsCapwapRunDataTransferunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 29),
    _FsCapwapRunDataTransferunsuccessfulProcessed_Type()
)
fsCapwapRunDataTransferunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferunsuccessfulProcessed.setStatus("current")
_FsCapwapRunDataTransferReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunDataTransferReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunDataTransferReasonLastUnsuccAttempt = _FsCapwapRunDataTransferReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 30),
    _FsCapwapRunDataTransferReasonLastUnsuccAttempt_Type()
)
fsCapwapRunDataTransferReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunDataTransferLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunDataTransferLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunDataTransferLastSuccAttemptTime = _FsCapwapRunDataTransferLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 31),
    _FsCapwapRunDataTransferLastSuccAttemptTime_Type()
)
fsCapwapRunDataTransferLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferLastSuccAttemptTime.setStatus("current")
_FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunDataTransferLastUnsuccessfulAttemptTime = _FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 32),
    _FsCapwapRunDataTransferLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunDataTransferLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunDataTransferLastUnsuccessfulAttemptTime.setStatus("current")


class _FsCapwapRunResetReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunResetReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunResetReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunResetReqReceived_Object = MibTableColumn
fsCapwapRunResetReqReceived = _FsCapwapRunResetReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 33),
    _FsCapwapRunResetReqReceived_Type()
)
fsCapwapRunResetReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetReqReceived.setStatus("current")


class _FsCapwapRunResetRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunResetRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunResetRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunResetRspReceived_Object = MibTableColumn
fsCapwapRunResetRspReceived = _FsCapwapRunResetRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 34),
    _FsCapwapRunResetRspReceived_Type()
)
fsCapwapRunResetRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetRspReceived.setStatus("current")


class _FsCapwapRunResetReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunResetReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunResetReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunResetReqTransmitted_Object = MibTableColumn
fsCapwapRunResetReqTransmitted = _FsCapwapRunResetReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 35),
    _FsCapwapRunResetReqTransmitted_Type()
)
fsCapwapRunResetReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetReqTransmitted.setStatus("current")


class _FsCapwapRunResetRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunResetRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunResetRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunResetRspTransmitted_Object = MibTableColumn
fsCapwapRunResetRspTransmitted = _FsCapwapRunResetRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 36),
    _FsCapwapRunResetRspTransmitted_Type()
)
fsCapwapRunResetRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetRspTransmitted.setStatus("current")


class _FsCapwapRunResetunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunResetunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunResetunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunResetunsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunResetunsuccessfulProcessed = _FsCapwapRunResetunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 37),
    _FsCapwapRunResetunsuccessfulProcessed_Type()
)
fsCapwapRunResetunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetunsuccessfulProcessed.setStatus("current")
_FsCapwapRunResetReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunResetReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunResetReasonLastUnsuccAttempt = _FsCapwapRunResetReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 38),
    _FsCapwapRunResetReasonLastUnsuccAttempt_Type()
)
fsCapwapRunResetReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunResetLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunResetLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunResetLastSuccAttemptTime = _FsCapwapRunResetLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 39),
    _FsCapwapRunResetLastSuccAttemptTime_Type()
)
fsCapwapRunResetLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetLastSuccAttemptTime.setStatus("current")
_FsCapwapRunResetLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunResetLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunResetLastUnsuccessfulAttemptTime = _FsCapwapRunResetLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 40),
    _FsCapwapRunResetLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunResetLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunResetLastUnsuccessfulAttemptTime.setStatus("current")


class _FsCapwapRunPriDiscReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunPriDiscReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunPriDiscReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunPriDiscReqReceived_Object = MibTableColumn
fsCapwapRunPriDiscReqReceived = _FsCapwapRunPriDiscReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 41),
    _FsCapwapRunPriDiscReqReceived_Type()
)
fsCapwapRunPriDiscReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscReqReceived.setStatus("current")


class _FsCapwapRunPriDiscRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunPriDiscRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunPriDiscRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunPriDiscRspReceived_Object = MibTableColumn
fsCapwapRunPriDiscRspReceived = _FsCapwapRunPriDiscRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 42),
    _FsCapwapRunPriDiscRspReceived_Type()
)
fsCapwapRunPriDiscRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscRspReceived.setStatus("current")


class _FsCapwapRunPriDiscReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunPriDiscReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunPriDiscReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunPriDiscReqTransmitted_Object = MibTableColumn
fsCapwapRunPriDiscReqTransmitted = _FsCapwapRunPriDiscReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 43),
    _FsCapwapRunPriDiscReqTransmitted_Type()
)
fsCapwapRunPriDiscReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscReqTransmitted.setStatus("current")


class _FsCapwapRunPriDiscRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunPriDiscRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunPriDiscRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunPriDiscRspTransmitted_Object = MibTableColumn
fsCapwapRunPriDiscRspTransmitted = _FsCapwapRunPriDiscRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 44),
    _FsCapwapRunPriDiscRspTransmitted_Type()
)
fsCapwapRunPriDiscRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscRspTransmitted.setStatus("current")


class _FsCapwapRunPriDiscunsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunPriDiscunsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunPriDiscunsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunPriDiscunsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunPriDiscunsuccessfulProcessed = _FsCapwapRunPriDiscunsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 45),
    _FsCapwapRunPriDiscunsuccessfulProcessed_Type()
)
fsCapwapRunPriDiscunsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscunsuccessfulProcessed.setStatus("current")
_FsCapwapRunPriDiscReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunPriDiscReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunPriDiscReasonLastUnsuccAttempt = _FsCapwapRunPriDiscReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 46),
    _FsCapwapRunPriDiscReasonLastUnsuccAttempt_Type()
)
fsCapwapRunPriDiscReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunPriDiscLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunPriDiscLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunPriDiscLastSuccAttemptTime = _FsCapwapRunPriDiscLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 47),
    _FsCapwapRunPriDiscLastSuccAttemptTime_Type()
)
fsCapwapRunPriDiscLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscLastSuccAttemptTime.setStatus("current")
_FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunPriDiscLastUnsuccessfulAttemptTime = _FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 48),
    _FsCapwapRunPriDiscLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunPriDiscLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunPriDiscLastUnsuccessfulAttemptTime.setStatus("current")


class _FsCapwapRunEchoReqReceived_Type(Unsigned32):
    """Custom type fsCapwapRunEchoReqReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunEchoReqReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunEchoReqReceived_Object = MibTableColumn
fsCapwapRunEchoReqReceived = _FsCapwapRunEchoReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 49),
    _FsCapwapRunEchoReqReceived_Type()
)
fsCapwapRunEchoReqReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoReqReceived.setStatus("current")


class _FsCapwapRunEchoRspReceived_Type(Unsigned32):
    """Custom type fsCapwapRunEchoRspReceived based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunEchoRspReceived_Type.__name__ = "Unsigned32"
_FsCapwapRunEchoRspReceived_Object = MibTableColumn
fsCapwapRunEchoRspReceived = _FsCapwapRunEchoRspReceived_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 50),
    _FsCapwapRunEchoRspReceived_Type()
)
fsCapwapRunEchoRspReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoRspReceived.setStatus("current")


class _FsCapwapRunEchoReqTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunEchoReqTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunEchoReqTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunEchoReqTransmitted_Object = MibTableColumn
fsCapwapRunEchoReqTransmitted = _FsCapwapRunEchoReqTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 51),
    _FsCapwapRunEchoReqTransmitted_Type()
)
fsCapwapRunEchoReqTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoReqTransmitted.setStatus("current")


class _FsCapwapRunEchoRspTransmitted_Type(Unsigned32):
    """Custom type fsCapwapRunEchoRspTransmitted based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunEchoRspTransmitted_Type.__name__ = "Unsigned32"
_FsCapwapRunEchoRspTransmitted_Object = MibTableColumn
fsCapwapRunEchoRspTransmitted = _FsCapwapRunEchoRspTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 52),
    _FsCapwapRunEchoRspTransmitted_Type()
)
fsCapwapRunEchoRspTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoRspTransmitted.setStatus("current")


class _FsCapwapRunEchounsuccessfulProcessed_Type(Unsigned32):
    """Custom type fsCapwapRunEchounsuccessfulProcessed based on Unsigned32"""
    defaultValue = 0


_FsCapwapRunEchounsuccessfulProcessed_Type.__name__ = "Unsigned32"
_FsCapwapRunEchounsuccessfulProcessed_Object = MibTableColumn
fsCapwapRunEchounsuccessfulProcessed = _FsCapwapRunEchounsuccessfulProcessed_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 53),
    _FsCapwapRunEchounsuccessfulProcessed_Type()
)
fsCapwapRunEchounsuccessfulProcessed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchounsuccessfulProcessed.setStatus("current")
_FsCapwapRunEchoReasonLastUnsuccAttempt_Type = SnmpAdminString
_FsCapwapRunEchoReasonLastUnsuccAttempt_Object = MibTableColumn
fsCapwapRunEchoReasonLastUnsuccAttempt = _FsCapwapRunEchoReasonLastUnsuccAttempt_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 54),
    _FsCapwapRunEchoReasonLastUnsuccAttempt_Type()
)
fsCapwapRunEchoReasonLastUnsuccAttempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoReasonLastUnsuccAttempt.setStatus("current")
_FsCapwapRunEchoLastSuccAttemptTime_Type = DateAndTime
_FsCapwapRunEchoLastSuccAttemptTime_Object = MibTableColumn
fsCapwapRunEchoLastSuccAttemptTime = _FsCapwapRunEchoLastSuccAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 55),
    _FsCapwapRunEchoLastSuccAttemptTime_Type()
)
fsCapwapRunEchoLastSuccAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoLastSuccAttemptTime.setStatus("current")
_FsCapwapRunEchoLastUnsuccessfulAttemptTime_Type = DateAndTime
_FsCapwapRunEchoLastUnsuccessfulAttemptTime_Object = MibTableColumn
fsCapwapRunEchoLastUnsuccessfulAttemptTime = _FsCapwapRunEchoLastUnsuccessfulAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 56),
    _FsCapwapRunEchoLastUnsuccessfulAttemptTime_Type()
)
fsCapwapRunEchoLastUnsuccessfulAttemptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunEchoLastUnsuccessfulAttemptTime.setStatus("current")
_FsCapwapRunStatsRowStatus_Type = RowStatus
_FsCapwapRunStatsRowStatus_Object = MibTableColumn
fsCapwapRunStatsRowStatus = _FsCapwapRunStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 11, 1, 57),
    _FsCapwapRunStatsRowStatus_Type()
)
fsCapwapRunStatsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapRunStatsRowStatus.setStatus("current")
_FsCapwapWirelessBindingTable_Object = MibTable
fsCapwapWirelessBindingTable = _FsCapwapWirelessBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 12)
)
if mibBuilder.loadTexts:
    fsCapwapWirelessBindingTable.setStatus("current")
_FsCapwapWirelessBindingEntry_Object = MibTableRow
fsCapwapWirelessBindingEntry = _FsCapwapWirelessBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 12, 1)
)
fsCapwapWirelessBindingEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWirelessBindingRadioId"),
)
if mibBuilder.loadTexts:
    fsCapwapWirelessBindingEntry.setStatus("current")
_FsCapwapWirelessBindingVirtualRadioIfIndex_Type = InterfaceIndex
_FsCapwapWirelessBindingVirtualRadioIfIndex_Object = MibTableColumn
fsCapwapWirelessBindingVirtualRadioIfIndex = _FsCapwapWirelessBindingVirtualRadioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 12, 1, 1),
    _FsCapwapWirelessBindingVirtualRadioIfIndex_Type()
)
fsCapwapWirelessBindingVirtualRadioIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWirelessBindingVirtualRadioIfIndex.setStatus("current")


class _FsCapwapWirelessBindingType_Type(Integer32):
    """Custom type fsCapwapWirelessBindingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11", 1),
          ("epc", 3))
    )


_FsCapwapWirelessBindingType_Type.__name__ = "Integer32"
_FsCapwapWirelessBindingType_Object = MibTableColumn
fsCapwapWirelessBindingType = _FsCapwapWirelessBindingType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 12, 1, 2),
    _FsCapwapWirelessBindingType_Type()
)
fsCapwapWirelessBindingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWirelessBindingType.setStatus("current")
_FsCapwapWirelessBindingRowStatus_Type = RowStatus
_FsCapwapWirelessBindingRowStatus_Object = MibTableColumn
fsCapwapWirelessBindingRowStatus = _FsCapwapWirelessBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 12, 1, 3),
    _FsCapwapWirelessBindingRowStatus_Type()
)
fsCapwapWirelessBindingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWirelessBindingRowStatus.setStatus("current")
_FsCapwapStationWhiteListTable_Object = MibTable
fsCapwapStationWhiteListTable = _FsCapwapStationWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 13)
)
if mibBuilder.loadTexts:
    fsCapwapStationWhiteListTable.setStatus("current")
_FsCapwapStationWhiteListEntry_Object = MibTableRow
fsCapwapStationWhiteListEntry = _FsCapwapStationWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 13, 1)
)
fsCapwapStationWhiteListEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "fsCapwapStationWhiteListId"),
)
if mibBuilder.loadTexts:
    fsCapwapStationWhiteListEntry.setStatus("current")
_FsCapwapStationWhiteListId_Type = Unsigned32
_FsCapwapStationWhiteListId_Object = MibTableColumn
fsCapwapStationWhiteListId = _FsCapwapStationWhiteListId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 13, 1, 1),
    _FsCapwapStationWhiteListId_Type()
)
fsCapwapStationWhiteListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsCapwapStationWhiteListId.setStatus("current")
_FsCapwapStationWhiteListStationId_Type = CapwapBaseStationIdTC
_FsCapwapStationWhiteListStationId_Object = MibTableColumn
fsCapwapStationWhiteListStationId = _FsCapwapStationWhiteListStationId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 13, 1, 2),
    _FsCapwapStationWhiteListStationId_Type()
)
fsCapwapStationWhiteListStationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapStationWhiteListStationId.setStatus("current")
_FsCapwapStationWhiteListRowStatus_Type = RowStatus
_FsCapwapStationWhiteListRowStatus_Object = MibTableColumn
fsCapwapStationWhiteListRowStatus = _FsCapwapStationWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 13, 1, 3),
    _FsCapwapStationWhiteListRowStatus_Type()
)
fsCapwapStationWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapStationWhiteListRowStatus.setStatus("current")
_FsCapwapWtpRebootStatisticsTable_Object = MibTable
fsCapwapWtpRebootStatisticsTable = _FsCapwapWtpRebootStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14)
)
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsTable.setStatus("current")
_FsCapwapWtpRebootStatisticsEntry_Object = MibTableRow
fsCapwapWtpRebootStatisticsEntry = _FsCapwapWtpRebootStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1)
)
fsCapwapWtpRebootStatisticsEntry.setIndexNames(
    (0, "SUPERMICRO-CAPWAP-MIB", "capwapBaseWtpProfileId"),
)
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsEntry.setStatus("current")


class _FsCapwapWtpRebootStatisticsRebootCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsRebootCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsRebootCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsRebootCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsRebootCount = _FsCapwapWtpRebootStatisticsRebootCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 1),
    _FsCapwapWtpRebootStatisticsRebootCount_Type()
)
fsCapwapWtpRebootStatisticsRebootCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsRebootCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsAcInitiatedCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsAcInitiatedCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsAcInitiatedCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsAcInitiatedCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsAcInitiatedCount = _FsCapwapWtpRebootStatisticsAcInitiatedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 2),
    _FsCapwapWtpRebootStatisticsAcInitiatedCount_Type()
)
fsCapwapWtpRebootStatisticsAcInitiatedCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsAcInitiatedCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsLinkFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsLinkFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsLinkFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsLinkFailureCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsLinkFailureCount = _FsCapwapWtpRebootStatisticsLinkFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 3),
    _FsCapwapWtpRebootStatisticsLinkFailureCount_Type()
)
fsCapwapWtpRebootStatisticsLinkFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsLinkFailureCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsSwFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsSwFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsSwFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsSwFailureCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsSwFailureCount = _FsCapwapWtpRebootStatisticsSwFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 4),
    _FsCapwapWtpRebootStatisticsSwFailureCount_Type()
)
fsCapwapWtpRebootStatisticsSwFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsSwFailureCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsHwFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsHwFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsHwFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsHwFailureCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsHwFailureCount = _FsCapwapWtpRebootStatisticsHwFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 5),
    _FsCapwapWtpRebootStatisticsHwFailureCount_Type()
)
fsCapwapWtpRebootStatisticsHwFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsHwFailureCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsOtherFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsOtherFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsOtherFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsOtherFailureCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsOtherFailureCount = _FsCapwapWtpRebootStatisticsOtherFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 6),
    _FsCapwapWtpRebootStatisticsOtherFailureCount_Type()
)
fsCapwapWtpRebootStatisticsOtherFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsOtherFailureCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsUnknownFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRebootStatisticsUnknownFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRebootStatisticsUnknownFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRebootStatisticsUnknownFailureCount_Object = MibTableColumn
fsCapwapWtpRebootStatisticsUnknownFailureCount = _FsCapwapWtpRebootStatisticsUnknownFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 7),
    _FsCapwapWtpRebootStatisticsUnknownFailureCount_Type()
)
fsCapwapWtpRebootStatisticsUnknownFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsUnknownFailureCount.setStatus("current")


class _FsCapwapWtpRebootStatisticsLastFailureType_Type(Integer32):
    """Custom type fsCapwapWtpRebootStatisticsLastFailureType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("aCInitiated", 1),
          ("linkFailure", 2),
          ("softwareFailure", 3),
          ("hardwareFailure", 4),
          ("otherFailure", 5),
          ("unknownFailure", 255))
    )


_FsCapwapWtpRebootStatisticsLastFailureType_Type.__name__ = "Integer32"
_FsCapwapWtpRebootStatisticsLastFailureType_Object = MibTableColumn
fsCapwapWtpRebootStatisticsLastFailureType = _FsCapwapWtpRebootStatisticsLastFailureType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 8),
    _FsCapwapWtpRebootStatisticsLastFailureType_Type()
)
fsCapwapWtpRebootStatisticsLastFailureType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsLastFailureType.setStatus("current")
_FsCapwapWtpRebootStatisticsRowStatus_Type = RowStatus
_FsCapwapWtpRebootStatisticsRowStatus_Object = MibTableColumn
fsCapwapWtpRebootStatisticsRowStatus = _FsCapwapWtpRebootStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 14, 1, 9),
    _FsCapwapWtpRebootStatisticsRowStatus_Type()
)
fsCapwapWtpRebootStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCapwapWtpRebootStatisticsRowStatus.setStatus("current")
_FsCapwapWtpRadioStatisticsTable_Object = MibTable
fsCapwapWtpRadioStatisticsTable = _FsCapwapWtpRadioStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15)
)
if mibBuilder.loadTexts:
    fsCapwapWtpRadioStatisticsTable.setStatus("current")
_FsCapwapWtpRadioStatisticsEntry_Object = MibTableRow
fsCapwapWtpRadioStatisticsEntry = _FsCapwapWtpRadioStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1)
)
fsCapwapWtpRadioStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsCapwapWtpRadioStatisticsEntry.setStatus("current")


class _FsCapwapWtpRadioLastFailType_Type(Integer32):
    """Custom type fsCapwapWtpRadioLastFailType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("statsNotSupported", 0),
          ("softwareFailure", 1),
          ("hardwareFailure", 2),
          ("otherFailure", 3),
          ("unknownFailure", 255))
    )


_FsCapwapWtpRadioLastFailType_Type.__name__ = "Integer32"
_FsCapwapWtpRadioLastFailType_Object = MibTableColumn
fsCapwapWtpRadioLastFailType = _FsCapwapWtpRadioLastFailType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 1),
    _FsCapwapWtpRadioLastFailType_Type()
)
fsCapwapWtpRadioLastFailType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioLastFailType.setStatus("current")


class _FsCapwapWtpRadioResetCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioResetCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioResetCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioResetCount_Object = MibTableColumn
fsCapwapWtpRadioResetCount = _FsCapwapWtpRadioResetCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 2),
    _FsCapwapWtpRadioResetCount_Type()
)
fsCapwapWtpRadioResetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioResetCount.setStatus("current")


class _FsCapwapWtpRadioSwFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioSwFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioSwFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioSwFailureCount_Object = MibTableColumn
fsCapwapWtpRadioSwFailureCount = _FsCapwapWtpRadioSwFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 3),
    _FsCapwapWtpRadioSwFailureCount_Type()
)
fsCapwapWtpRadioSwFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioSwFailureCount.setStatus("current")


class _FsCapwapWtpRadioHwFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioHwFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioHwFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioHwFailureCount_Object = MibTableColumn
fsCapwapWtpRadioHwFailureCount = _FsCapwapWtpRadioHwFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 4),
    _FsCapwapWtpRadioHwFailureCount_Type()
)
fsCapwapWtpRadioHwFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioHwFailureCount.setStatus("current")


class _FsCapwapWtpRadioOtherFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioOtherFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioOtherFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioOtherFailureCount_Object = MibTableColumn
fsCapwapWtpRadioOtherFailureCount = _FsCapwapWtpRadioOtherFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 5),
    _FsCapwapWtpRadioOtherFailureCount_Type()
)
fsCapwapWtpRadioOtherFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioOtherFailureCount.setStatus("current")


class _FsCapwapWtpRadioUnknownFailureCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioUnknownFailureCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioUnknownFailureCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioUnknownFailureCount_Object = MibTableColumn
fsCapwapWtpRadioUnknownFailureCount = _FsCapwapWtpRadioUnknownFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 6),
    _FsCapwapWtpRadioUnknownFailureCount_Type()
)
fsCapwapWtpRadioUnknownFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioUnknownFailureCount.setStatus("current")


class _FsCapwapWtpRadioConfigUpdateCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioConfigUpdateCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioConfigUpdateCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioConfigUpdateCount_Object = MibTableColumn
fsCapwapWtpRadioConfigUpdateCount = _FsCapwapWtpRadioConfigUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 7),
    _FsCapwapWtpRadioConfigUpdateCount_Type()
)
fsCapwapWtpRadioConfigUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioConfigUpdateCount.setStatus("current")


class _FsCapwapWtpRadioChannelChangeCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioChannelChangeCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioChannelChangeCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioChannelChangeCount_Object = MibTableColumn
fsCapwapWtpRadioChannelChangeCount = _FsCapwapWtpRadioChannelChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 8),
    _FsCapwapWtpRadioChannelChangeCount_Type()
)
fsCapwapWtpRadioChannelChangeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioChannelChangeCount.setStatus("current")


class _FsCapwapWtpRadioBandChangeCount_Type(Unsigned32):
    """Custom type fsCapwapWtpRadioBandChangeCount based on Unsigned32"""
    defaultValue = 0


_FsCapwapWtpRadioBandChangeCount_Type.__name__ = "Unsigned32"
_FsCapwapWtpRadioBandChangeCount_Object = MibTableColumn
fsCapwapWtpRadioBandChangeCount = _FsCapwapWtpRadioBandChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 9),
    _FsCapwapWtpRadioBandChangeCount_Type()
)
fsCapwapWtpRadioBandChangeCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioBandChangeCount.setStatus("current")


class _FsCapwapWtpRadioCurrentNoiseFloor_Type(Integer32):
    """Custom type fsCapwapWtpRadioCurrentNoiseFloor based on Integer32"""
    defaultValue = 0


_FsCapwapWtpRadioCurrentNoiseFloor_Type.__name__ = "Integer32"
_FsCapwapWtpRadioCurrentNoiseFloor_Object = MibTableColumn
fsCapwapWtpRadioCurrentNoiseFloor = _FsCapwapWtpRadioCurrentNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 10),
    _FsCapwapWtpRadioCurrentNoiseFloor_Type()
)
fsCapwapWtpRadioCurrentNoiseFloor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioCurrentNoiseFloor.setStatus("current")
_FsCapwapWtpRadioStatRowStatus_Type = RowStatus
_FsCapwapWtpRadioStatRowStatus_Object = MibTableColumn
fsCapwapWtpRadioStatRowStatus = _FsCapwapWtpRadioStatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 82, 3, 15, 1, 11),
    _FsCapwapWtpRadioStatRowStatus_Type()
)
fsCapwapWtpRadioStatRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCapwapWtpRadioStatRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-CAPWAP-MIB",
    **{"EnabledStatus": EnabledStatus,
       "CapwapBaseRadioIdTC": CapwapBaseRadioIdTC,
       "CapwapBaseTunnelModeTC": CapwapBaseTunnelModeTC,
       "CapwapBaseMacTypeTC": CapwapBaseMacTypeTC,
       "CapwapBaseStationIdTC": CapwapBaseStationIdTC,
       "fsCapwap": fsCapwap,
       "fsCapwapSystem": fsCapwapSystem,
       "fsCapwapModuleStatus": fsCapwapModuleStatus,
       "fsCapwapSystemControl": fsCapwapSystemControl,
       "fsCapwapControlUdpPort": fsCapwapControlUdpPort,
       "fsCapwapControlChannelDTLSPolicyOptions": fsCapwapControlChannelDTLSPolicyOptions,
       "fsCapwapDataChannelDTLSPolicyOptions": fsCapwapDataChannelDTLSPolicyOptions,
       "fsWlcDiscoveryMode": fsWlcDiscoveryMode,
       "fsCapwapWtpModeIgnore": fsCapwapWtpModeIgnore,
       "fsCapwapDebugMask": fsCapwapDebugMask,
       "fsDtlsDebugMask": fsDtlsDebugMask,
       "fsDtlsEncryption": fsDtlsEncryption,
       "fsDtlsEncryptAlgorithm": fsDtlsEncryptAlgorithm,
       "fsStationType": fsStationType,
       "fsCapwapWtpModel": fsCapwapWtpModel,
       "fsWtpModelTable": fsWtpModelTable,
       "fsWtpModelEntry": fsWtpModelEntry,
       "fsCapwapWtpModelNumber": fsCapwapWtpModelNumber,
       "fsNoOfRadio": fsNoOfRadio,
       "fsCapwapWtpMacType": fsCapwapWtpMacType,
       "fsCapwapWtpTunnelMode": fsCapwapWtpTunnelMode,
       "fsCapwapSwVersion": fsCapwapSwVersion,
       "fsCapwapImageName": fsCapwapImageName,
       "fsCapwapQosProfileName": fsCapwapQosProfileName,
       "fsMaxStations": fsMaxStations,
       "fsWtpModelRowStatus": fsWtpModelRowStatus,
       "fsWtpRadioTable": fsWtpRadioTable,
       "fsWtpRadioEntry": fsWtpRadioEntry,
       "fsRadioNumber": fsRadioNumber,
       "fsWtpRadioType": fsWtpRadioType,
       "fsRadioAdminStatus": fsRadioAdminStatus,
       "fsWtpRadioRowStatus": fsWtpRadioRowStatus,
       "fsCapwapConfig": fsCapwapConfig,
       "fsCapwapWhiteListTable": fsCapwapWhiteListTable,
       "fsCapwapWhiteListEntry": fsCapwapWhiteListEntry,
       "fsCapwapWhiteListId": fsCapwapWhiteListId,
       "fsCapwapWhiteListWtpBaseMac": fsCapwapWhiteListWtpBaseMac,
       "fsCapwapWhiteListRowStatus": fsCapwapWhiteListRowStatus,
       "fsCapwapBlackListTable": fsCapwapBlackListTable,
       "fsCapwapBlackListEntry": fsCapwapBlackListEntry,
       "fsCapwapBlackListId": fsCapwapBlackListId,
       "fsCapwapBlackListWtpBaseMac": fsCapwapBlackListWtpBaseMac,
       "fsCapwapBlackListRowStatus": fsCapwapBlackListRowStatus,
       "fsCapwapWtpConfigTable": fsCapwapWtpConfigTable,
       "fsCapwapWtpConfigEntry": fsCapwapWtpConfigEntry,
       "fsCapwapWtpReset": fsCapwapWtpReset,
       "fsCapwapClearConfig": fsCapwapClearConfig,
       "fsWtpDiscoveryType": fsWtpDiscoveryType,
       "fsWtpCountryString": fsWtpCountryString,
       "fsWtpCrashDumpFileName": fsWtpCrashDumpFileName,
       "fsWtpMemoryDumpFileName": fsWtpMemoryDumpFileName,
       "fsWtpDeleteOperation": fsWtpDeleteOperation,
       "fsCapwapClearApStats": fsCapwapClearApStats,
       "fsCapwapWtpConfigRowStatus": fsCapwapWtpConfigRowStatus,
       "fsCapwapLinkEncryptionTable": fsCapwapLinkEncryptionTable,
       "fsCapwapLinkEncryptionEntry": fsCapwapLinkEncryptionEntry,
       "fsCapwapEncryptChannel": fsCapwapEncryptChannel,
       "fsCapwapEncryptChannelStatus": fsCapwapEncryptChannelStatus,
       "fsCapwapEncryptChannelRowStatus": fsCapwapEncryptChannelRowStatus,
       "fsCapwapDefaultWtpProfileTable": fsCapwapDefaultWtpProfileTable,
       "fsCapwapDefaultWtpProfileEntry": fsCapwapDefaultWtpProfileEntry,
       "fsCapwapDefaultQosProfile": fsCapwapDefaultQosProfile,
       "fsCapwapDefaultWtpProfileRowStatus": fsCapwapDefaultWtpProfileRowStatus,
       "fsCapwapDnsProfileTable": fsCapwapDnsProfileTable,
       "fsCapwapDnsProfileEntry": fsCapwapDnsProfileEntry,
       "fsCapwapDnsAddressType": fsCapwapDnsAddressType,
       "fsCapwapDnsServerIp": fsCapwapDnsServerIp,
       "fsCapwapDnsDomainName": fsCapwapDnsDomainName,
       "fsCapwapDnsProfileRowStatus": fsCapwapDnsProfileRowStatus,
       "fsWtpNativeVlanIdTable": fsWtpNativeVlanIdTable,
       "fsWtpNativeVlanIdEntry": fsWtpNativeVlanIdEntry,
       "fsWtpNativeVlanId": fsWtpNativeVlanId,
       "fsWtpNativeVlanIdRowStatus": fsWtpNativeVlanIdRowStatus,
       "fsCawapDiscStatsTable": fsCawapDiscStatsTable,
       "fsCawapDiscStatsEntry": fsCawapDiscStatsEntry,
       "fsCapwapDiscReqReceived": fsCapwapDiscReqReceived,
       "fsCapwapDiscRspReceived": fsCapwapDiscRspReceived,
       "fsCapwapDiscReqTransmitted": fsCapwapDiscReqTransmitted,
       "fsCapwapDiscRspTransmitted": fsCapwapDiscRspTransmitted,
       "fsCapwapDiscunsuccessfulProcessed": fsCapwapDiscunsuccessfulProcessed,
       "fsCapwapDiscLastUnsuccAttemptReason": fsCapwapDiscLastUnsuccAttemptReason,
       "fsCapwapDiscLastSuccAttemptTime": fsCapwapDiscLastSuccAttemptTime,
       "fsCapwapDiscLastUnsuccessfulAttemptTime": fsCapwapDiscLastUnsuccessfulAttemptTime,
       "fsCapwapDiscStatsRowStatus": fsCapwapDiscStatsRowStatus,
       "fsCawapJoinStatsTable": fsCawapJoinStatsTable,
       "fsCawapJoinStatsEntry": fsCawapJoinStatsEntry,
       "fsCapwapJoinReqReceived": fsCapwapJoinReqReceived,
       "fsCapwapJoinRspReceived": fsCapwapJoinRspReceived,
       "fsCapwapJoinReqTransmitted": fsCapwapJoinReqTransmitted,
       "fsCapwapJoinRspTransmitted": fsCapwapJoinRspTransmitted,
       "fsCapwapJoinunsuccessfulProcessed": fsCapwapJoinunsuccessfulProcessed,
       "fsCapwapJoinReasonLastUnsuccAttempt": fsCapwapJoinReasonLastUnsuccAttempt,
       "fsCapwapJoinLastSuccAttemptTime": fsCapwapJoinLastSuccAttemptTime,
       "fsCapwapJoinLastUnsuccAttemptTime": fsCapwapJoinLastUnsuccAttemptTime,
       "fsCapwapJoinStatsRowStatus": fsCapwapJoinStatsRowStatus,
       "fsCawapConfigStatsTable": fsCawapConfigStatsTable,
       "fsCawapConfigStatsEntry": fsCawapConfigStatsEntry,
       "fsCapwapConfigReqReceived": fsCapwapConfigReqReceived,
       "fsCapwapConfigRspReceived": fsCapwapConfigRspReceived,
       "fsCapwapConfigReqTransmitted": fsCapwapConfigReqTransmitted,
       "fsCapwapConfigRspTransmitted": fsCapwapConfigRspTransmitted,
       "fsCapwapConfigunsuccessfulProcessed": fsCapwapConfigunsuccessfulProcessed,
       "fsCapwapConfigReasonLastUnsuccAttempt": fsCapwapConfigReasonLastUnsuccAttempt,
       "fsCapwapConfigLastSuccAttemptTime": fsCapwapConfigLastSuccAttemptTime,
       "fsCapwapConfigLastUnsuccessfulAttemptTime": fsCapwapConfigLastUnsuccessfulAttemptTime,
       "fsCapwapConfigStatsRowStatus": fsCapwapConfigStatsRowStatus,
       "fsCawapRunStatsTable": fsCawapRunStatsTable,
       "fsCawapRunStatsEntry": fsCawapRunStatsEntry,
       "fsCapwapRunConfigUpdateReqReceived": fsCapwapRunConfigUpdateReqReceived,
       "fsCapwapRunConfigUpdateRspReceived": fsCapwapRunConfigUpdateRspReceived,
       "fsCapwapRunConfigUpdateReqTransmitted": fsCapwapRunConfigUpdateReqTransmitted,
       "fsCapwapRunConfigUpdateRspTransmitted": fsCapwapRunConfigUpdateRspTransmitted,
       "fsCapwapRunConfigUpdateunsuccessfulProcessed": fsCapwapRunConfigUpdateunsuccessfulProcessed,
       "fsCapwapRunConfigUpdateReasonLastUnsuccAttempt": fsCapwapRunConfigUpdateReasonLastUnsuccAttempt,
       "fsCapwapRunConfigUpdateLastSuccAttemptTime": fsCapwapRunConfigUpdateLastSuccAttemptTime,
       "fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime": fsCapwapRunConfigUpdateLastUnsuccessfulAttemptTime,
       "fsCapwapRunStationConfigReqReceived": fsCapwapRunStationConfigReqReceived,
       "fsCapwapRunStationConfigRspReceived": fsCapwapRunStationConfigRspReceived,
       "fsCapwapRunStationConfigReqTransmitted": fsCapwapRunStationConfigReqTransmitted,
       "fsCapwapRunStationConfigRspTransmitted": fsCapwapRunStationConfigRspTransmitted,
       "fsCapwapRunStationConfigunsuccessfulProcessed": fsCapwapRunStationConfigunsuccessfulProcessed,
       "fsCapwapRunStationConfigReasonLastUnsuccAttempt": fsCapwapRunStationConfigReasonLastUnsuccAttempt,
       "fsCapwapRunStationConfigLastSuccAttemptTime": fsCapwapRunStationConfigLastSuccAttemptTime,
       "fsCapwapRunStationConfigLastUnsuccessfulAttemptTime": fsCapwapRunStationConfigLastUnsuccessfulAttemptTime,
       "fsCapwapRunClearConfigReqReceived": fsCapwapRunClearConfigReqReceived,
       "fsCapwapRunClearConfigRspReceived": fsCapwapRunClearConfigRspReceived,
       "fsCapwapRunClearConfigReqTransmitted": fsCapwapRunClearConfigReqTransmitted,
       "fsCapwapRunClearConfigRspTransmitted": fsCapwapRunClearConfigRspTransmitted,
       "fsCapwapRunClearConfigunsuccessfulProcessed": fsCapwapRunClearConfigunsuccessfulProcessed,
       "fsCapwapRunClearConfigReasonLastUnsuccAttempt": fsCapwapRunClearConfigReasonLastUnsuccAttempt,
       "fsCapwapRunClearConfigLastSuccAttemptTime": fsCapwapRunClearConfigLastSuccAttemptTime,
       "fsCapwapRunClearConfigLastUnsuccessfulAttemptTime": fsCapwapRunClearConfigLastUnsuccessfulAttemptTime,
       "fsCapwapRunDataTransferReqReceived": fsCapwapRunDataTransferReqReceived,
       "fsCapwapRunDataTransferRspReceived": fsCapwapRunDataTransferRspReceived,
       "fsCapwapRunDataTransferReqTransmitted": fsCapwapRunDataTransferReqTransmitted,
       "fsCapwapRunDataTransferRspTransmitted": fsCapwapRunDataTransferRspTransmitted,
       "fsCapwapRunDataTransferunsuccessfulProcessed": fsCapwapRunDataTransferunsuccessfulProcessed,
       "fsCapwapRunDataTransferReasonLastUnsuccAttempt": fsCapwapRunDataTransferReasonLastUnsuccAttempt,
       "fsCapwapRunDataTransferLastSuccAttemptTime": fsCapwapRunDataTransferLastSuccAttemptTime,
       "fsCapwapRunDataTransferLastUnsuccessfulAttemptTime": fsCapwapRunDataTransferLastUnsuccessfulAttemptTime,
       "fsCapwapRunResetReqReceived": fsCapwapRunResetReqReceived,
       "fsCapwapRunResetRspReceived": fsCapwapRunResetRspReceived,
       "fsCapwapRunResetReqTransmitted": fsCapwapRunResetReqTransmitted,
       "fsCapwapRunResetRspTransmitted": fsCapwapRunResetRspTransmitted,
       "fsCapwapRunResetunsuccessfulProcessed": fsCapwapRunResetunsuccessfulProcessed,
       "fsCapwapRunResetReasonLastUnsuccAttempt": fsCapwapRunResetReasonLastUnsuccAttempt,
       "fsCapwapRunResetLastSuccAttemptTime": fsCapwapRunResetLastSuccAttemptTime,
       "fsCapwapRunResetLastUnsuccessfulAttemptTime": fsCapwapRunResetLastUnsuccessfulAttemptTime,
       "fsCapwapRunPriDiscReqReceived": fsCapwapRunPriDiscReqReceived,
       "fsCapwapRunPriDiscRspReceived": fsCapwapRunPriDiscRspReceived,
       "fsCapwapRunPriDiscReqTransmitted": fsCapwapRunPriDiscReqTransmitted,
       "fsCapwapRunPriDiscRspTransmitted": fsCapwapRunPriDiscRspTransmitted,
       "fsCapwapRunPriDiscunsuccessfulProcessed": fsCapwapRunPriDiscunsuccessfulProcessed,
       "fsCapwapRunPriDiscReasonLastUnsuccAttempt": fsCapwapRunPriDiscReasonLastUnsuccAttempt,
       "fsCapwapRunPriDiscLastSuccAttemptTime": fsCapwapRunPriDiscLastSuccAttemptTime,
       "fsCapwapRunPriDiscLastUnsuccessfulAttemptTime": fsCapwapRunPriDiscLastUnsuccessfulAttemptTime,
       "fsCapwapRunEchoReqReceived": fsCapwapRunEchoReqReceived,
       "fsCapwapRunEchoRspReceived": fsCapwapRunEchoRspReceived,
       "fsCapwapRunEchoReqTransmitted": fsCapwapRunEchoReqTransmitted,
       "fsCapwapRunEchoRspTransmitted": fsCapwapRunEchoRspTransmitted,
       "fsCapwapRunEchounsuccessfulProcessed": fsCapwapRunEchounsuccessfulProcessed,
       "fsCapwapRunEchoReasonLastUnsuccAttempt": fsCapwapRunEchoReasonLastUnsuccAttempt,
       "fsCapwapRunEchoLastSuccAttemptTime": fsCapwapRunEchoLastSuccAttemptTime,
       "fsCapwapRunEchoLastUnsuccessfulAttemptTime": fsCapwapRunEchoLastUnsuccessfulAttemptTime,
       "fsCapwapRunStatsRowStatus": fsCapwapRunStatsRowStatus,
       "fsCapwapWirelessBindingTable": fsCapwapWirelessBindingTable,
       "fsCapwapWirelessBindingEntry": fsCapwapWirelessBindingEntry,
       "fsCapwapWirelessBindingVirtualRadioIfIndex": fsCapwapWirelessBindingVirtualRadioIfIndex,
       "fsCapwapWirelessBindingType": fsCapwapWirelessBindingType,
       "fsCapwapWirelessBindingRowStatus": fsCapwapWirelessBindingRowStatus,
       "fsCapwapStationWhiteListTable": fsCapwapStationWhiteListTable,
       "fsCapwapStationWhiteListEntry": fsCapwapStationWhiteListEntry,
       "fsCapwapStationWhiteListId": fsCapwapStationWhiteListId,
       "fsCapwapStationWhiteListStationId": fsCapwapStationWhiteListStationId,
       "fsCapwapStationWhiteListRowStatus": fsCapwapStationWhiteListRowStatus,
       "fsCapwapWtpRebootStatisticsTable": fsCapwapWtpRebootStatisticsTable,
       "fsCapwapWtpRebootStatisticsEntry": fsCapwapWtpRebootStatisticsEntry,
       "fsCapwapWtpRebootStatisticsRebootCount": fsCapwapWtpRebootStatisticsRebootCount,
       "fsCapwapWtpRebootStatisticsAcInitiatedCount": fsCapwapWtpRebootStatisticsAcInitiatedCount,
       "fsCapwapWtpRebootStatisticsLinkFailureCount": fsCapwapWtpRebootStatisticsLinkFailureCount,
       "fsCapwapWtpRebootStatisticsSwFailureCount": fsCapwapWtpRebootStatisticsSwFailureCount,
       "fsCapwapWtpRebootStatisticsHwFailureCount": fsCapwapWtpRebootStatisticsHwFailureCount,
       "fsCapwapWtpRebootStatisticsOtherFailureCount": fsCapwapWtpRebootStatisticsOtherFailureCount,
       "fsCapwapWtpRebootStatisticsUnknownFailureCount": fsCapwapWtpRebootStatisticsUnknownFailureCount,
       "fsCapwapWtpRebootStatisticsLastFailureType": fsCapwapWtpRebootStatisticsLastFailureType,
       "fsCapwapWtpRebootStatisticsRowStatus": fsCapwapWtpRebootStatisticsRowStatus,
       "fsCapwapWtpRadioStatisticsTable": fsCapwapWtpRadioStatisticsTable,
       "fsCapwapWtpRadioStatisticsEntry": fsCapwapWtpRadioStatisticsEntry,
       "fsCapwapWtpRadioLastFailType": fsCapwapWtpRadioLastFailType,
       "fsCapwapWtpRadioResetCount": fsCapwapWtpRadioResetCount,
       "fsCapwapWtpRadioSwFailureCount": fsCapwapWtpRadioSwFailureCount,
       "fsCapwapWtpRadioHwFailureCount": fsCapwapWtpRadioHwFailureCount,
       "fsCapwapWtpRadioOtherFailureCount": fsCapwapWtpRadioOtherFailureCount,
       "fsCapwapWtpRadioUnknownFailureCount": fsCapwapWtpRadioUnknownFailureCount,
       "fsCapwapWtpRadioConfigUpdateCount": fsCapwapWtpRadioConfigUpdateCount,
       "fsCapwapWtpRadioChannelChangeCount": fsCapwapWtpRadioChannelChangeCount,
       "fsCapwapWtpRadioBandChangeCount": fsCapwapWtpRadioBandChangeCount,
       "fsCapwapWtpRadioCurrentNoiseFloor": fsCapwapWtpRadioCurrentNoiseFloor,
       "fsCapwapWtpRadioStatRowStatus": fsCapwapWtpRadioStatRowStatus}
)
