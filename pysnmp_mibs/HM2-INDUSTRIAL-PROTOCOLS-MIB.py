# SNMP MIB module (HM2-INDUSTRIAL-PROTOCOLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-INDUSTRIAL-PROTOCOLS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:52:14 2025
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

(InetAddressIPv4,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetPortNumber")

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

hm2IndustrialProtocolsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101)
)
if mibBuilder.loadTexts:
    hm2IndustrialProtocolsMib.setRevisions(
        ("2014-02-24 00:00",
         "2014-01-15 00:00",
         "2013-05-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2Iec62541OpcUaUserAccessRoles(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("readOnly", 1)
    )



class Hm2Iec62541OpcUaSecurityPolicies(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("basic128Rsa15", 2),
          ("basic256", 3),
          ("basic256Sha256", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Hm2IndustrialProtocolsNotifications_ObjectIdentity = ObjectIdentity
hm2IndustrialProtocolsNotifications = _Hm2IndustrialProtocolsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 0)
)
_Hm2IndustrialProtocolsMibObjects_ObjectIdentity = ObjectIdentity
hm2IndustrialProtocolsMibObjects = _Hm2IndustrialProtocolsMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1)
)
_Hm2Iec61850Group_ObjectIdentity = ObjectIdentity
hm2Iec61850Group = _Hm2Iec61850Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1)
)
_Hm2Iec61850ConfigGroup_ObjectIdentity = ObjectIdentity
hm2Iec61850ConfigGroup = _Hm2Iec61850ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1)
)


class _Hm2Iec61850MmsServerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2Iec61850MmsServerAdminStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2Iec61850MmsServerAdminStatus_Type.__name__ = "HmEnabledStatus"
_Hm2Iec61850MmsServerAdminStatus_Object = MibScalar
hm2Iec61850MmsServerAdminStatus = _Hm2Iec61850MmsServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 1),
    _Hm2Iec61850MmsServerAdminStatus_Type()
)
hm2Iec61850MmsServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerAdminStatus.setStatus("current")


class _Hm2Iec61850MmsServerWriteAccessStatus_Type(HmEnabledStatus):
    """Custom type hm2Iec61850MmsServerWriteAccessStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2Iec61850MmsServerWriteAccessStatus_Type.__name__ = "HmEnabledStatus"
_Hm2Iec61850MmsServerWriteAccessStatus_Object = MibScalar
hm2Iec61850MmsServerWriteAccessStatus = _Hm2Iec61850MmsServerWriteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 2),
    _Hm2Iec61850MmsServerWriteAccessStatus_Type()
)
hm2Iec61850MmsServerWriteAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerWriteAccessStatus.setStatus("current")


class _Hm2Iec61850MmsServerPortNumber_Type(InetPortNumber):
    """Custom type hm2Iec61850MmsServerPortNumber based on InetPortNumber"""
    defaultValue = 102


_Hm2Iec61850MmsServerPortNumber_Type.__name__ = "InetPortNumber"
_Hm2Iec61850MmsServerPortNumber_Object = MibScalar
hm2Iec61850MmsServerPortNumber = _Hm2Iec61850MmsServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 3),
    _Hm2Iec61850MmsServerPortNumber_Type()
)
hm2Iec61850MmsServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerPortNumber.setStatus("current")


class _Hm2Iec61850MmsServerMaxSessionsCount_Type(Integer32):
    """Custom type hm2Iec61850MmsServerMaxSessionsCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2Iec61850MmsServerMaxSessionsCount_Type.__name__ = "Integer32"
_Hm2Iec61850MmsServerMaxSessionsCount_Object = MibScalar
hm2Iec61850MmsServerMaxSessionsCount = _Hm2Iec61850MmsServerMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 4),
    _Hm2Iec61850MmsServerMaxSessionsCount_Type()
)
hm2Iec61850MmsServerMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerMaxSessionsCount.setStatus("current")


class _Hm2Iec61850MmsServerTechnicalKey_Type(SnmpAdminString):
    """Custom type hm2Iec61850MmsServerTechnicalKey based on SnmpAdminString"""
    defaultValue = OctetString("KEY")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2Iec61850MmsServerTechnicalKey_Type.__name__ = "SnmpAdminString"
_Hm2Iec61850MmsServerTechnicalKey_Object = MibScalar
hm2Iec61850MmsServerTechnicalKey = _Hm2Iec61850MmsServerTechnicalKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 5),
    _Hm2Iec61850MmsServerTechnicalKey_Type()
)
hm2Iec61850MmsServerTechnicalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerTechnicalKey.setStatus("current")


class _Hm2Iec61850MmsTlsServerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2Iec61850MmsTlsServerAdminStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2Iec61850MmsTlsServerAdminStatus_Type.__name__ = "HmEnabledStatus"
_Hm2Iec61850MmsTlsServerAdminStatus_Object = MibScalar
hm2Iec61850MmsTlsServerAdminStatus = _Hm2Iec61850MmsTlsServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 10),
    _Hm2Iec61850MmsTlsServerAdminStatus_Type()
)
hm2Iec61850MmsTlsServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerAdminStatus.setStatus("current")


class _Hm2Iec61850MmsTlsServerWriteAccessStatus_Type(HmEnabledStatus):
    """Custom type hm2Iec61850MmsTlsServerWriteAccessStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2Iec61850MmsTlsServerWriteAccessStatus_Type.__name__ = "HmEnabledStatus"
_Hm2Iec61850MmsTlsServerWriteAccessStatus_Object = MibScalar
hm2Iec61850MmsTlsServerWriteAccessStatus = _Hm2Iec61850MmsTlsServerWriteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 11),
    _Hm2Iec61850MmsTlsServerWriteAccessStatus_Type()
)
hm2Iec61850MmsTlsServerWriteAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerWriteAccessStatus.setStatus("current")


class _Hm2Iec61850MmsTlsServerPortNumber_Type(InetPortNumber):
    """Custom type hm2Iec61850MmsTlsServerPortNumber based on InetPortNumber"""
    defaultValue = 3782


_Hm2Iec61850MmsTlsServerPortNumber_Type.__name__ = "InetPortNumber"
_Hm2Iec61850MmsTlsServerPortNumber_Object = MibScalar
hm2Iec61850MmsTlsServerPortNumber = _Hm2Iec61850MmsTlsServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 12),
    _Hm2Iec61850MmsTlsServerPortNumber_Type()
)
hm2Iec61850MmsTlsServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerPortNumber.setStatus("current")


class _Hm2Iec61850MmsTlsServerMaxSessionsCount_Type(Integer32):
    """Custom type hm2Iec61850MmsTlsServerMaxSessionsCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2Iec61850MmsTlsServerMaxSessionsCount_Type.__name__ = "Integer32"
_Hm2Iec61850MmsTlsServerMaxSessionsCount_Object = MibScalar
hm2Iec61850MmsTlsServerMaxSessionsCount = _Hm2Iec61850MmsTlsServerMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 13),
    _Hm2Iec61850MmsTlsServerMaxSessionsCount_Type()
)
hm2Iec61850MmsTlsServerMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerMaxSessionsCount.setStatus("current")


class _Hm2Iec61850MmsTlsServerKeysPresent_Type(Integer32):
    """Custom type hm2Iec61850MmsTlsServerKeysPresent based on Integer32"""
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
        *(("dsa", 1),
          ("rsa", 2),
          ("both", 3),
          ("none", 4))
    )


_Hm2Iec61850MmsTlsServerKeysPresent_Type.__name__ = "Integer32"
_Hm2Iec61850MmsTlsServerKeysPresent_Object = MibScalar
hm2Iec61850MmsTlsServerKeysPresent = _Hm2Iec61850MmsTlsServerKeysPresent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 20),
    _Hm2Iec61850MmsTlsServerKeysPresent_Type()
)
hm2Iec61850MmsTlsServerKeysPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerKeysPresent.setStatus("current")


class _Hm2Iec61850MmsTlsServerKeyOperStatus_Type(Integer32):
    """Custom type hm2Iec61850MmsTlsServerKeyOperStatus based on Integer32"""
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
        *(("dsa", 1),
          ("rsa", 2),
          ("both", 3),
          ("none", 4))
    )


_Hm2Iec61850MmsTlsServerKeyOperStatus_Type.__name__ = "Integer32"
_Hm2Iec61850MmsTlsServerKeyOperStatus_Object = MibScalar
hm2Iec61850MmsTlsServerKeyOperStatus = _Hm2Iec61850MmsTlsServerKeyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 21),
    _Hm2Iec61850MmsTlsServerKeyOperStatus_Type()
)
hm2Iec61850MmsTlsServerKeyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerKeyOperStatus.setStatus("current")


class _Hm2Iec61850MmsTlsServerRSAKeyControl_Type(Integer32):
    """Custom type hm2Iec61850MmsTlsServerRSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("generate", 2),
          ("delete", 3))
    )


_Hm2Iec61850MmsTlsServerRSAKeyControl_Type.__name__ = "Integer32"
_Hm2Iec61850MmsTlsServerRSAKeyControl_Object = MibScalar
hm2Iec61850MmsTlsServerRSAKeyControl = _Hm2Iec61850MmsTlsServerRSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 22),
    _Hm2Iec61850MmsTlsServerRSAKeyControl_Type()
)
hm2Iec61850MmsTlsServerRSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerRSAKeyControl.setStatus("current")


class _Hm2Iec61850MmsTlsServerDSAKeyControl_Type(Integer32):
    """Custom type hm2Iec61850MmsTlsServerDSAKeyControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("generate", 2),
          ("delete", 3))
    )


_Hm2Iec61850MmsTlsServerDSAKeyControl_Type.__name__ = "Integer32"
_Hm2Iec61850MmsTlsServerDSAKeyControl_Object = MibScalar
hm2Iec61850MmsTlsServerDSAKeyControl = _Hm2Iec61850MmsTlsServerDSAKeyControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 23),
    _Hm2Iec61850MmsTlsServerDSAKeyControl_Type()
)
hm2Iec61850MmsTlsServerDSAKeyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerDSAKeyControl.setStatus("current")


class _Hm2Iec61850MmsTlsServerFingerPrintDSA_Type(DisplayString):
    """Custom type hm2Iec61850MmsTlsServerFingerPrintDSA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2Iec61850MmsTlsServerFingerPrintDSA_Type.__name__ = "DisplayString"
_Hm2Iec61850MmsTlsServerFingerPrintDSA_Object = MibScalar
hm2Iec61850MmsTlsServerFingerPrintDSA = _Hm2Iec61850MmsTlsServerFingerPrintDSA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 24),
    _Hm2Iec61850MmsTlsServerFingerPrintDSA_Type()
)
hm2Iec61850MmsTlsServerFingerPrintDSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerFingerPrintDSA.setStatus("current")


class _Hm2Iec61850MmsTlsServerFingerPrintRSA_Type(DisplayString):
    """Custom type hm2Iec61850MmsTlsServerFingerPrintRSA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hm2Iec61850MmsTlsServerFingerPrintRSA_Type.__name__ = "DisplayString"
_Hm2Iec61850MmsTlsServerFingerPrintRSA_Object = MibScalar
hm2Iec61850MmsTlsServerFingerPrintRSA = _Hm2Iec61850MmsTlsServerFingerPrintRSA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 25),
    _Hm2Iec61850MmsTlsServerFingerPrintRSA_Type()
)
hm2Iec61850MmsTlsServerFingerPrintRSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerFingerPrintRSA.setStatus("current")


class _Hm2Iec61850MmsServerStatus_Type(Integer32):
    """Custom type hm2Iec61850MmsServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("starting", 2),
          ("running", 3),
          ("stopping", 4),
          ("halted", 5),
          ("error", 6))
    )


_Hm2Iec61850MmsServerStatus_Type.__name__ = "Integer32"
_Hm2Iec61850MmsServerStatus_Object = MibScalar
hm2Iec61850MmsServerStatus = _Hm2Iec61850MmsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 1, 26),
    _Hm2Iec61850MmsServerStatus_Type()
)
hm2Iec61850MmsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerStatus.setStatus("current")
_Hm2Iec61850StatisticsGroup_ObjectIdentity = ObjectIdentity
hm2Iec61850StatisticsGroup = _Hm2Iec61850StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 2)
)
_Hm2Iec61850MmsServerSessionsCount_Type = Integer32
_Hm2Iec61850MmsServerSessionsCount_Object = MibScalar
hm2Iec61850MmsServerSessionsCount = _Hm2Iec61850MmsServerSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 2, 1),
    _Hm2Iec61850MmsServerSessionsCount_Type()
)
hm2Iec61850MmsServerSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsServerSessionsCount.setStatus("current")
_Hm2Iec61850MmsTlsServerSessionsCount_Type = Integer32
_Hm2Iec61850MmsTlsServerSessionsCount_Object = MibScalar
hm2Iec61850MmsTlsServerSessionsCount = _Hm2Iec61850MmsTlsServerSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 1, 2, 10),
    _Hm2Iec61850MmsTlsServerSessionsCount_Type()
)
hm2Iec61850MmsTlsServerSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2Iec61850MmsTlsServerSessionsCount.setStatus("current")
_Hm2ProfinetIOGroup_ObjectIdentity = ObjectIdentity
hm2ProfinetIOGroup = _Hm2ProfinetIOGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2)
)
_Hm2ProfinetIOConfigGroup_ObjectIdentity = ObjectIdentity
hm2ProfinetIOConfigGroup = _Hm2ProfinetIOConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1)
)


class _Hm2PNIOAdminStatus_Type(Integer32):
    """Custom type hm2PNIOAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_Hm2PNIOAdminStatus_Type.__name__ = "Integer32"
_Hm2PNIOAdminStatus_Object = MibScalar
hm2PNIOAdminStatus = _Hm2PNIOAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 1),
    _Hm2PNIOAdminStatus_Type()
)
hm2PNIOAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOAdminStatus.setStatus("current")


class _Hm2PNIODeviceID_Type(Integer32):
    """Custom type hm2PNIODeviceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2PNIODeviceID_Type.__name__ = "Integer32"
_Hm2PNIODeviceID_Object = MibScalar
hm2PNIODeviceID = _Hm2PNIODeviceID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 2),
    _Hm2PNIODeviceID_Type()
)
hm2PNIODeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIODeviceID.setStatus("current")
_Hm2PNIOModuleIdentNumber_Type = Integer32
_Hm2PNIOModuleIdentNumber_Object = MibScalar
hm2PNIOModuleIdentNumber = _Hm2PNIOModuleIdentNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 3),
    _Hm2PNIOModuleIdentNumber_Type()
)
hm2PNIOModuleIdentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIOModuleIdentNumber.setStatus("current")


class _Hm2PNIOOrderID_Type(DisplayString):
    """Custom type hm2PNIOOrderID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2PNIOOrderID_Type.__name__ = "DisplayString"
_Hm2PNIOOrderID_Object = MibScalar
hm2PNIOOrderID = _Hm2PNIOOrderID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 4),
    _Hm2PNIOOrderID_Type()
)
hm2PNIOOrderID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIOOrderID.setStatus("current")
_Hm2PNIODeviceTypeDetails_Type = DisplayString
_Hm2PNIODeviceTypeDetails_Object = MibScalar
hm2PNIODeviceTypeDetails = _Hm2PNIODeviceTypeDetails_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 5),
    _Hm2PNIODeviceTypeDetails_Type()
)
hm2PNIODeviceTypeDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIODeviceTypeDetails.setStatus("current")
_Hm2PNIOSoftwareRelease_Type = DisplayString
_Hm2PNIOSoftwareRelease_Object = MibScalar
hm2PNIOSoftwareRelease = _Hm2PNIOSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 6),
    _Hm2PNIOSoftwareRelease_Type()
)
hm2PNIOSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIOSoftwareRelease.setStatus("current")
_Hm2PNIOHardwareRelease_Type = Integer32
_Hm2PNIOHardwareRelease_Object = MibScalar
hm2PNIOHardwareRelease = _Hm2PNIOHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 7),
    _Hm2PNIOHardwareRelease_Type()
)
hm2PNIOHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIOHardwareRelease.setStatus("current")


class _Hm2PNIOOrderID9th_Type(DisplayString):
    """Custom type hm2PNIOOrderID9th based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2PNIOOrderID9th_Type.__name__ = "DisplayString"
_Hm2PNIOOrderID9th_Object = MibScalar
hm2PNIOOrderID9th = _Hm2PNIOOrderID9th_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 8),
    _Hm2PNIOOrderID9th_Type()
)
hm2PNIOOrderID9th.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIOOrderID9th.setStatus("current")


class _Hm2PNIONameOfStation_Type(DisplayString):
    """Custom type hm2PNIONameOfStation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_Hm2PNIONameOfStation_Type.__name__ = "DisplayString"
_Hm2PNIONameOfStation_Object = MibScalar
hm2PNIONameOfStation = _Hm2PNIONameOfStation_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 9),
    _Hm2PNIONameOfStation_Type()
)
hm2PNIONameOfStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIONameOfStation.setStatus("current")
_Hm2PNIONumActiveApplicationRelations_Type = Unsigned32
_Hm2PNIONumActiveApplicationRelations_Object = MibScalar
hm2PNIONumActiveApplicationRelations = _Hm2PNIONumActiveApplicationRelations_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 10),
    _Hm2PNIONumActiveApplicationRelations_Type()
)
hm2PNIONumActiveApplicationRelations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PNIONumActiveApplicationRelations.setStatus("current")


class _Hm2PNIOClearIpParameter_Type(TruthValue):
    """Custom type hm2PNIOClearIpParameter based on TruthValue"""
    defaultValue = 2


_Hm2PNIOClearIpParameter_Type.__name__ = "TruthValue"
_Hm2PNIOClearIpParameter_Object = MibScalar
hm2PNIOClearIpParameter = _Hm2PNIOClearIpParameter_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 11),
    _Hm2PNIOClearIpParameter_Type()
)
hm2PNIOClearIpParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOClearIpParameter.setStatus("current")
_Hm2PNIODcpModeTable_Object = MibTable
hm2PNIODcpModeTable = _Hm2PNIODcpModeTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 20)
)
if mibBuilder.loadTexts:
    hm2PNIODcpModeTable.setStatus("current")
_Hm2PNIODcpModeEntry_Object = MibTableRow
hm2PNIODcpModeEntry = _Hm2PNIODcpModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 20, 1)
)
hm2PNIODcpModeEntry.setIndexNames(
    (0, "HM2-INDUSTRIAL-PROTOCOLS-MIB", "hm2PNIODcpModePortID"),
)
if mibBuilder.loadTexts:
    hm2PNIODcpModeEntry.setStatus("current")
_Hm2PNIODcpModePortID_Type = Integer32
_Hm2PNIODcpModePortID_Object = MibTableColumn
hm2PNIODcpModePortID = _Hm2PNIODcpModePortID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 20, 1, 1),
    _Hm2PNIODcpModePortID_Type()
)
hm2PNIODcpModePortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2PNIODcpModePortID.setStatus("current")


class _Hm2PNIODcpMode_Type(Integer32):
    """Custom type hm2PNIODcpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_Hm2PNIODcpMode_Type.__name__ = "Integer32"
_Hm2PNIODcpMode_Object = MibTableColumn
hm2PNIODcpMode = _Hm2PNIODcpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 20, 1, 2),
    _Hm2PNIODcpMode_Type()
)
hm2PNIODcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIODcpMode.setStatus("current")


class _Hm2PNIOIm1Data_Type(SnmpAdminString):
    """Custom type hm2PNIOIm1Data based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_Hm2PNIOIm1Data_Type.__name__ = "SnmpAdminString"
_Hm2PNIOIm1Data_Object = MibScalar
hm2PNIOIm1Data = _Hm2PNIOIm1Data_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 21),
    _Hm2PNIOIm1Data_Type()
)
hm2PNIOIm1Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOIm1Data.setStatus("current")


class _Hm2PNIOIm2Data_Type(SnmpAdminString):
    """Custom type hm2PNIOIm2Data based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hm2PNIOIm2Data_Type.__name__ = "SnmpAdminString"
_Hm2PNIOIm2Data_Object = MibScalar
hm2PNIOIm2Data = _Hm2PNIOIm2Data_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 22),
    _Hm2PNIOIm2Data_Type()
)
hm2PNIOIm2Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOIm2Data.setStatus("current")


class _Hm2PNIOIm3Data_Type(SnmpAdminString):
    """Custom type hm2PNIOIm3Data based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_Hm2PNIOIm3Data_Type.__name__ = "SnmpAdminString"
_Hm2PNIOIm3Data_Object = MibScalar
hm2PNIOIm3Data = _Hm2PNIOIm3Data_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 23),
    _Hm2PNIOIm3Data_Type()
)
hm2PNIOIm3Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOIm3Data.setStatus("current")


class _Hm2PNIOIm4Data_Type(SnmpAdminString):
    """Custom type hm2PNIOIm4Data based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_Hm2PNIOIm4Data_Type.__name__ = "SnmpAdminString"
_Hm2PNIOIm4Data_Object = MibScalar
hm2PNIOIm4Data = _Hm2PNIOIm4Data_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 24),
    _Hm2PNIOIm4Data_Type()
)
hm2PNIOIm4Data.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOIm4Data.setStatus("current")


class _Hm2PNIOClearStationName_Type(TruthValue):
    """Custom type hm2PNIOClearStationName based on TruthValue"""
    defaultValue = 2


_Hm2PNIOClearStationName_Type.__name__ = "TruthValue"
_Hm2PNIOClearStationName_Object = MibScalar
hm2PNIOClearStationName = _Hm2PNIOClearStationName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 25),
    _Hm2PNIOClearStationName_Type()
)
hm2PNIOClearStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOClearStationName.setStatus("current")
_Hm2PNIOPdevParameters_Type = OctetString
_Hm2PNIOPdevParameters_Object = MibScalar
hm2PNIOPdevParameters = _Hm2PNIOPdevParameters_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 1, 26),
    _Hm2PNIOPdevParameters_Type()
)
hm2PNIOPdevParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2PNIOPdevParameters.setStatus("current")
_Hm2ProfinetIOStatisticsGroup_ObjectIdentity = ObjectIdentity
hm2ProfinetIOStatisticsGroup = _Hm2ProfinetIOStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 2, 2)
)
_Hm2EthernetIPGroup_ObjectIdentity = ObjectIdentity
hm2EthernetIPGroup = _Hm2EthernetIPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3)
)
_Hm2EthernetIPConfigGroup_ObjectIdentity = ObjectIdentity
hm2EthernetIPConfigGroup = _Hm2EthernetIPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1)
)


class _Hm2EtherNetIPAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2EtherNetIPAdminStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2EtherNetIPAdminStatus_Type.__name__ = "HmEnabledStatus"
_Hm2EtherNetIPAdminStatus_Object = MibScalar
hm2EtherNetIPAdminStatus = _Hm2EtherNetIPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 1),
    _Hm2EtherNetIPAdminStatus_Type()
)
hm2EtherNetIPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPAdminStatus.setStatus("current")


class _Hm2EtherNetIPErrorCode_Type(Integer32):
    """Custom type hm2EtherNetIPErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2EtherNetIPErrorCode_Type.__name__ = "Integer32"
_Hm2EtherNetIPErrorCode_Object = MibScalar
hm2EtherNetIPErrorCode = _Hm2EtherNetIPErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 2),
    _Hm2EtherNetIPErrorCode_Type()
)
hm2EtherNetIPErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPErrorCode.setStatus("current")


class _Hm2EtherNetIPProductCode_Type(Integer32):
    """Custom type hm2EtherNetIPProductCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2EtherNetIPProductCode_Type.__name__ = "Integer32"
_Hm2EtherNetIPProductCode_Object = MibScalar
hm2EtherNetIPProductCode = _Hm2EtherNetIPProductCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 3),
    _Hm2EtherNetIPProductCode_Type()
)
hm2EtherNetIPProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPProductCode.setStatus("current")


class _Hm2EtherNetIPMajorRevision_Type(Integer32):
    """Custom type hm2EtherNetIPMajorRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2EtherNetIPMajorRevision_Type.__name__ = "Integer32"
_Hm2EtherNetIPMajorRevision_Object = MibScalar
hm2EtherNetIPMajorRevision = _Hm2EtherNetIPMajorRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 4),
    _Hm2EtherNetIPMajorRevision_Type()
)
hm2EtherNetIPMajorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPMajorRevision.setStatus("current")


class _Hm2EtherNetIPMinorRevision_Type(Integer32):
    """Custom type hm2EtherNetIPMinorRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2EtherNetIPMinorRevision_Type.__name__ = "Integer32"
_Hm2EtherNetIPMinorRevision_Object = MibScalar
hm2EtherNetIPMinorRevision = _Hm2EtherNetIPMinorRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 5),
    _Hm2EtherNetIPMinorRevision_Type()
)
hm2EtherNetIPMinorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPMinorRevision.setStatus("current")


class _Hm2EtherNetIPProductName_Type(SnmpAdminString):
    """Custom type hm2EtherNetIPProductName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2EtherNetIPProductName_Type.__name__ = "SnmpAdminString"
_Hm2EtherNetIPProductName_Object = MibScalar
hm2EtherNetIPProductName = _Hm2EtherNetIPProductName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 6),
    _Hm2EtherNetIPProductName_Type()
)
hm2EtherNetIPProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPProductName.setStatus("current")


class _Hm2EtherNetIPCatalogName_Type(SnmpAdminString):
    """Custom type hm2EtherNetIPCatalogName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2EtherNetIPCatalogName_Type.__name__ = "SnmpAdminString"
_Hm2EtherNetIPCatalogName_Object = MibScalar
hm2EtherNetIPCatalogName = _Hm2EtherNetIPCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 7),
    _Hm2EtherNetIPCatalogName_Type()
)
hm2EtherNetIPCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPCatalogName.setStatus("current")


class _Hm2EtherNetIPWriteAccessStatus_Type(HmEnabledStatus):
    """Custom type hm2EtherNetIPWriteAccessStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2EtherNetIPWriteAccessStatus_Type.__name__ = "HmEnabledStatus"
_Hm2EtherNetIPWriteAccessStatus_Object = MibScalar
hm2EtherNetIPWriteAccessStatus = _Hm2EtherNetIPWriteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 8),
    _Hm2EtherNetIPWriteAccessStatus_Type()
)
hm2EtherNetIPWriteAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPWriteAccessStatus.setStatus("current")


class _Hm2EtherNetIPVlan_Type(Integer32):
    """Custom type hm2EtherNetIPVlan based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4042),
    )


_Hm2EtherNetIPVlan_Type.__name__ = "Integer32"
_Hm2EtherNetIPVlan_Object = MibScalar
hm2EtherNetIPVlan = _Hm2EtherNetIPVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 9),
    _Hm2EtherNetIPVlan_Type()
)
hm2EtherNetIPVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPVlan.setStatus("current")


class _Hm2EtherNetIPInterface_Type(Integer32):
    """Custom type hm2EtherNetIPInterface based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hm2EtherNetIPInterface_Type.__name__ = "Integer32"
_Hm2EtherNetIPInterface_Object = MibScalar
hm2EtherNetIPInterface = _Hm2EtherNetIPInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 1, 10),
    _Hm2EtherNetIPInterface_Type()
)
hm2EtherNetIPInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPInterface.setStatus("current")
_Hm2EthernetIPStatisticsGroup_ObjectIdentity = ObjectIdentity
hm2EthernetIPStatisticsGroup = _Hm2EthernetIPStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 2)
)
_Hm2EtherNetIPConnEstablished_Type = Unsigned32
_Hm2EtherNetIPConnEstablished_Object = MibScalar
hm2EtherNetIPConnEstablished = _Hm2EtherNetIPConnEstablished_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 2, 1),
    _Hm2EtherNetIPConnEstablished_Type()
)
hm2EtherNetIPConnEstablished.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPConnEstablished.setStatus("current")
_Hm2EtherNetIPConnTimeouts_Type = Unsigned32
_Hm2EtherNetIPConnTimeouts_Object = MibScalar
hm2EtherNetIPConnTimeouts = _Hm2EtherNetIPConnTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 2, 2),
    _Hm2EtherNetIPConnTimeouts_Type()
)
hm2EtherNetIPConnTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPConnTimeouts.setStatus("current")
_Hm2EtherNetIPVendorObjRequests_Type = Unsigned32
_Hm2EtherNetIPVendorObjRequests_Object = MibScalar
hm2EtherNetIPVendorObjRequests = _Hm2EtherNetIPVendorObjRequests_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 2, 3),
    _Hm2EtherNetIPVendorObjRequests_Type()
)
hm2EtherNetIPVendorObjRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2EtherNetIPVendorObjRequests.setStatus("current")
_Hm2EthernetIPTCPIPObjectGroup_ObjectIdentity = ObjectIdentity
hm2EthernetIPTCPIPObjectGroup = _Hm2EthernetIPTCPIPObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3)
)


class _Hm2EtherNetIPMcastTTLValue_Type(Integer32):
    """Custom type hm2EtherNetIPMcastTTLValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2EtherNetIPMcastTTLValue_Type.__name__ = "Integer32"
_Hm2EtherNetIPMcastTTLValue_Object = MibScalar
hm2EtherNetIPMcastTTLValue = _Hm2EtherNetIPMcastTTLValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 1),
    _Hm2EtherNetIPMcastTTLValue_Type()
)
hm2EtherNetIPMcastTTLValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPMcastTTLValue.setStatus("current")


class _Hm2EtherNetIPMcastAllocControl_Type(Integer32):
    """Custom type hm2EtherNetIPMcastAllocControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("defined", 1),
          ("reserved", 2))
    )


_Hm2EtherNetIPMcastAllocControl_Type.__name__ = "Integer32"
_Hm2EtherNetIPMcastAllocControl_Object = MibScalar
hm2EtherNetIPMcastAllocControl = _Hm2EtherNetIPMcastAllocControl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 2),
    _Hm2EtherNetIPMcastAllocControl_Type()
)
hm2EtherNetIPMcastAllocControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPMcastAllocControl.setStatus("current")


class _Hm2EtherNetIPMcastCount_Type(Integer32):
    """Custom type hm2EtherNetIPMcastCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2EtherNetIPMcastCount_Type.__name__ = "Integer32"
_Hm2EtherNetIPMcastCount_Object = MibScalar
hm2EtherNetIPMcastCount = _Hm2EtherNetIPMcastCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 3),
    _Hm2EtherNetIPMcastCount_Type()
)
hm2EtherNetIPMcastCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPMcastCount.setStatus("current")
_Hm2EtherNetIPMcastStartAddress_Type = InetAddressIPv4
_Hm2EtherNetIPMcastStartAddress_Object = MibScalar
hm2EtherNetIPMcastStartAddress = _Hm2EtherNetIPMcastStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 4),
    _Hm2EtherNetIPMcastStartAddress_Type()
)
hm2EtherNetIPMcastStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPMcastStartAddress.setStatus("current")


class _Hm2EtherNetIPLastConflictDetectedACDActivity_Type(OctetString):
    """Custom type hm2EtherNetIPLastConflictDetectedACDActivity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(28, 28),
    )
    fixed_length = 28


_Hm2EtherNetIPLastConflictDetectedACDActivity_Type.__name__ = "OctetString"
_Hm2EtherNetIPLastConflictDetectedACDActivity_Object = MibScalar
hm2EtherNetIPLastConflictDetectedACDActivity = _Hm2EtherNetIPLastConflictDetectedACDActivity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 5),
    _Hm2EtherNetIPLastConflictDetectedACDActivity_Type()
)
hm2EtherNetIPLastConflictDetectedACDActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPLastConflictDetectedACDActivity.setStatus("current")


class _Hm2EtherNetIPSelectACDStatus_Type(Integer32):
    """Custom type hm2EtherNetIPSelectACDStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_Hm2EtherNetIPSelectACDStatus_Type.__name__ = "Integer32"
_Hm2EtherNetIPSelectACDStatus_Object = MibScalar
hm2EtherNetIPSelectACDStatus = _Hm2EtherNetIPSelectACDStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 6),
    _Hm2EtherNetIPSelectACDStatus_Type()
)
hm2EtherNetIPSelectACDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPSelectACDStatus.setStatus("current")


class _Hm2EtherNetIPEncapsulationInactivity_Type(Unsigned32):
    """Custom type hm2EtherNetIPEncapsulationInactivity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hm2EtherNetIPEncapsulationInactivity_Type.__name__ = "Unsigned32"
_Hm2EtherNetIPEncapsulationInactivity_Object = MibScalar
hm2EtherNetIPEncapsulationInactivity = _Hm2EtherNetIPEncapsulationInactivity_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 3, 7),
    _Hm2EtherNetIPEncapsulationInactivity_Type()
)
hm2EtherNetIPEncapsulationInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPEncapsulationInactivity.setStatus("current")
_Hm2EthernetIPQoSObjectGroup_ObjectIdentity = ObjectIdentity
hm2EthernetIPQoSObjectGroup = _Hm2EthernetIPQoSObjectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4)
)


class _Hm2EtherNetIPQosDscpUrgentValue_Type(Integer32):
    """Custom type hm2EtherNetIPQosDscpUrgentValue based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2EtherNetIPQosDscpUrgentValue_Type.__name__ = "Integer32"
_Hm2EtherNetIPQosDscpUrgentValue_Object = MibScalar
hm2EtherNetIPQosDscpUrgentValue = _Hm2EtherNetIPQosDscpUrgentValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4, 1),
    _Hm2EtherNetIPQosDscpUrgentValue_Type()
)
hm2EtherNetIPQosDscpUrgentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPQosDscpUrgentValue.setStatus("current")


class _Hm2EtherNetIPQosDscpScheduledValue_Type(Integer32):
    """Custom type hm2EtherNetIPQosDscpScheduledValue based on Integer32"""
    defaultValue = 47

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2EtherNetIPQosDscpScheduledValue_Type.__name__ = "Integer32"
_Hm2EtherNetIPQosDscpScheduledValue_Object = MibScalar
hm2EtherNetIPQosDscpScheduledValue = _Hm2EtherNetIPQosDscpScheduledValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4, 2),
    _Hm2EtherNetIPQosDscpScheduledValue_Type()
)
hm2EtherNetIPQosDscpScheduledValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPQosDscpScheduledValue.setStatus("current")


class _Hm2EtherNetIPQosDscpHighValue_Type(Integer32):
    """Custom type hm2EtherNetIPQosDscpHighValue based on Integer32"""
    defaultValue = 43

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2EtherNetIPQosDscpHighValue_Type.__name__ = "Integer32"
_Hm2EtherNetIPQosDscpHighValue_Object = MibScalar
hm2EtherNetIPQosDscpHighValue = _Hm2EtherNetIPQosDscpHighValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4, 3),
    _Hm2EtherNetIPQosDscpHighValue_Type()
)
hm2EtherNetIPQosDscpHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPQosDscpHighValue.setStatus("current")


class _Hm2EtherNetIPQosDscpLowValue_Type(Integer32):
    """Custom type hm2EtherNetIPQosDscpLowValue based on Integer32"""
    defaultValue = 31

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2EtherNetIPQosDscpLowValue_Type.__name__ = "Integer32"
_Hm2EtherNetIPQosDscpLowValue_Object = MibScalar
hm2EtherNetIPQosDscpLowValue = _Hm2EtherNetIPQosDscpLowValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4, 4),
    _Hm2EtherNetIPQosDscpLowValue_Type()
)
hm2EtherNetIPQosDscpLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPQosDscpLowValue.setStatus("current")


class _Hm2EtherNetIPQosDscpExplicitValue_Type(Integer32):
    """Custom type hm2EtherNetIPQosDscpExplicitValue based on Integer32"""
    defaultValue = 27

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hm2EtherNetIPQosDscpExplicitValue_Type.__name__ = "Integer32"
_Hm2EtherNetIPQosDscpExplicitValue_Object = MibScalar
hm2EtherNetIPQosDscpExplicitValue = _Hm2EtherNetIPQosDscpExplicitValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4, 5),
    _Hm2EtherNetIPQosDscpExplicitValue_Type()
)
hm2EtherNetIPQosDscpExplicitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPQosDscpExplicitValue.setStatus("current")


class _Hm2EtherNetIPQosValue_Type(TruthValue):
    """Custom type hm2EtherNetIPQosValue based on TruthValue"""
    defaultValue = 2


_Hm2EtherNetIPQosValue_Type.__name__ = "TruthValue"
_Hm2EtherNetIPQosValue_Object = MibScalar
hm2EtherNetIPQosValue = _Hm2EtherNetIPQosValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 3, 4, 6),
    _Hm2EtherNetIPQosValue_Type()
)
hm2EtherNetIPQosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2EtherNetIPQosValue.setStatus("current")
_Hm2ModbusGroup_ObjectIdentity = ObjectIdentity
hm2ModbusGroup = _Hm2ModbusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4)
)
_Hm2ModbusConfigGroup_ObjectIdentity = ObjectIdentity
hm2ModbusConfigGroup = _Hm2ModbusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 1)
)


class _Hm2ModbusTcpServerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2ModbusTcpServerAdminStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2ModbusTcpServerAdminStatus_Type.__name__ = "HmEnabledStatus"
_Hm2ModbusTcpServerAdminStatus_Object = MibScalar
hm2ModbusTcpServerAdminStatus = _Hm2ModbusTcpServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 1, 1),
    _Hm2ModbusTcpServerAdminStatus_Type()
)
hm2ModbusTcpServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModbusTcpServerAdminStatus.setStatus("current")


class _Hm2ModbusTcpServerWriteAccessStatus_Type(HmEnabledStatus):
    """Custom type hm2ModbusTcpServerWriteAccessStatus based on HmEnabledStatus"""
    defaultValue = 1


_Hm2ModbusTcpServerWriteAccessStatus_Type.__name__ = "HmEnabledStatus"
_Hm2ModbusTcpServerWriteAccessStatus_Object = MibScalar
hm2ModbusTcpServerWriteAccessStatus = _Hm2ModbusTcpServerWriteAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 1, 2),
    _Hm2ModbusTcpServerWriteAccessStatus_Type()
)
hm2ModbusTcpServerWriteAccessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModbusTcpServerWriteAccessStatus.setStatus("current")


class _Hm2ModbusTcpServerPortNumber_Type(InetPortNumber):
    """Custom type hm2ModbusTcpServerPortNumber based on InetPortNumber"""
    defaultValue = 502


_Hm2ModbusTcpServerPortNumber_Type.__name__ = "InetPortNumber"
_Hm2ModbusTcpServerPortNumber_Object = MibScalar
hm2ModbusTcpServerPortNumber = _Hm2ModbusTcpServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 1, 3),
    _Hm2ModbusTcpServerPortNumber_Type()
)
hm2ModbusTcpServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModbusTcpServerPortNumber.setStatus("current")


class _Hm2ModbusTcpServerMaxSessionsCount_Type(Integer32):
    """Custom type hm2ModbusTcpServerMaxSessionsCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hm2ModbusTcpServerMaxSessionsCount_Type.__name__ = "Integer32"
_Hm2ModbusTcpServerMaxSessionsCount_Object = MibScalar
hm2ModbusTcpServerMaxSessionsCount = _Hm2ModbusTcpServerMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 1, 4),
    _Hm2ModbusTcpServerMaxSessionsCount_Type()
)
hm2ModbusTcpServerMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2ModbusTcpServerMaxSessionsCount.setStatus("current")
_Hm2ModbusStatisticsGroup_ObjectIdentity = ObjectIdentity
hm2ModbusStatisticsGroup = _Hm2ModbusStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 2)
)
_Hm2ModbusTcpServerSessionsCount_Type = Integer32
_Hm2ModbusTcpServerSessionsCount_Object = MibScalar
hm2ModbusTcpServerSessionsCount = _Hm2ModbusTcpServerSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 4, 2, 1),
    _Hm2ModbusTcpServerSessionsCount_Type()
)
hm2ModbusTcpServerSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2ModbusTcpServerSessionsCount.setStatus("current")
_Hm2Iec62541Group_ObjectIdentity = ObjectIdentity
hm2Iec62541Group = _Hm2Iec62541Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5)
)
_Hm2Iec62541ConfigGroup_ObjectIdentity = ObjectIdentity
hm2Iec62541ConfigGroup = _Hm2Iec62541ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1)
)


class _Hm2Iec62541OpcUaServerAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2Iec62541OpcUaServerAdminStatus based on HmEnabledStatus"""
    defaultValue = 2


_Hm2Iec62541OpcUaServerAdminStatus_Type.__name__ = "HmEnabledStatus"
_Hm2Iec62541OpcUaServerAdminStatus_Object = MibScalar
hm2Iec62541OpcUaServerAdminStatus = _Hm2Iec62541OpcUaServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 1),
    _Hm2Iec62541OpcUaServerAdminStatus_Type()
)
hm2Iec62541OpcUaServerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaServerAdminStatus.setStatus("current")


class _Hm2Iec62541OpcUaServerPortNumber_Type(InetPortNumber):
    """Custom type hm2Iec62541OpcUaServerPortNumber based on InetPortNumber"""
    defaultValue = 4840

    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2Iec62541OpcUaServerPortNumber_Type.__name__ = "InetPortNumber"
_Hm2Iec62541OpcUaServerPortNumber_Object = MibScalar
hm2Iec62541OpcUaServerPortNumber = _Hm2Iec62541OpcUaServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 2),
    _Hm2Iec62541OpcUaServerPortNumber_Type()
)
hm2Iec62541OpcUaServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaServerPortNumber.setStatus("current")


class _Hm2Iec62541OpcUaMaxSessionsCount_Type(Integer32):
    """Custom type hm2Iec62541OpcUaMaxSessionsCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hm2Iec62541OpcUaMaxSessionsCount_Type.__name__ = "Integer32"
_Hm2Iec62541OpcUaMaxSessionsCount_Object = MibScalar
hm2Iec62541OpcUaMaxSessionsCount = _Hm2Iec62541OpcUaMaxSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 3),
    _Hm2Iec62541OpcUaMaxSessionsCount_Type()
)
hm2Iec62541OpcUaMaxSessionsCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaMaxSessionsCount.setStatus("current")


class _Hm2Iec62541OpcUaSecurityPolicy_Type(Hm2Iec62541OpcUaSecurityPolicies):
    """Custom type hm2Iec62541OpcUaSecurityPolicy based on Hm2Iec62541OpcUaSecurityPolicies"""
    defaultValue = 1


_Hm2Iec62541OpcUaSecurityPolicy_Type.__name__ = "Hm2Iec62541OpcUaSecurityPolicies"
_Hm2Iec62541OpcUaSecurityPolicy_Object = MibScalar
hm2Iec62541OpcUaSecurityPolicy = _Hm2Iec62541OpcUaSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 4),
    _Hm2Iec62541OpcUaSecurityPolicy_Type()
)
hm2Iec62541OpcUaSecurityPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaSecurityPolicy.setStatus("current")
_Hm2Iec62541OpcUaUserConfigTable_Object = MibTable
hm2Iec62541OpcUaUserConfigTable = _Hm2Iec62541OpcUaUserConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 10)
)
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaUserConfigTable.setStatus("current")
_Hm2Iec62541OpcUaUserConfigEntry_Object = MibTableRow
hm2Iec62541OpcUaUserConfigEntry = _Hm2Iec62541OpcUaUserConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 10, 1)
)
hm2Iec62541OpcUaUserConfigEntry.setIndexNames(
    (1, "HM2-INDUSTRIAL-PROTOCOLS-MIB", "hm2Iec62541OpcUaUserName"),
)
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaUserConfigEntry.setStatus("current")


class _Hm2Iec62541OpcUaUserName_Type(SnmpAdminString):
    """Custom type hm2Iec62541OpcUaUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2Iec62541OpcUaUserName_Type.__name__ = "SnmpAdminString"
_Hm2Iec62541OpcUaUserName_Object = MibTableColumn
hm2Iec62541OpcUaUserName = _Hm2Iec62541OpcUaUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 10, 1, 1),
    _Hm2Iec62541OpcUaUserName_Type()
)
hm2Iec62541OpcUaUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaUserName.setStatus("current")


class _Hm2Iec62541OpcUaUserPassword_Type(DisplayString):
    """Custom type hm2Iec62541OpcUaUserPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hm2Iec62541OpcUaUserPassword_Type.__name__ = "DisplayString"
_Hm2Iec62541OpcUaUserPassword_Object = MibTableColumn
hm2Iec62541OpcUaUserPassword = _Hm2Iec62541OpcUaUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 10, 1, 2),
    _Hm2Iec62541OpcUaUserPassword_Type()
)
hm2Iec62541OpcUaUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaUserPassword.setStatus("current")


class _Hm2Iec62541OpcUaUserAccessRole_Type(Hm2Iec62541OpcUaUserAccessRoles):
    """Custom type hm2Iec62541OpcUaUserAccessRole based on Hm2Iec62541OpcUaUserAccessRoles"""
    defaultValue = 1


_Hm2Iec62541OpcUaUserAccessRole_Type.__name__ = "Hm2Iec62541OpcUaUserAccessRoles"
_Hm2Iec62541OpcUaUserAccessRole_Object = MibTableColumn
hm2Iec62541OpcUaUserAccessRole = _Hm2Iec62541OpcUaUserAccessRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 10, 1, 3),
    _Hm2Iec62541OpcUaUserAccessRole_Type()
)
hm2Iec62541OpcUaUserAccessRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaUserAccessRole.setStatus("current")
_Hm2Iec62541OpcUaUserStatus_Type = RowStatus
_Hm2Iec62541OpcUaUserStatus_Object = MibTableColumn
hm2Iec62541OpcUaUserStatus = _Hm2Iec62541OpcUaUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 1, 5, 1, 10, 1, 5),
    _Hm2Iec62541OpcUaUserStatus_Type()
)
hm2Iec62541OpcUaUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2Iec62541OpcUaUserStatus.setStatus("current")
_Hm2IndustrialProtocolsMibSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2IndustrialProtocolsMibSNMPExtensionGroup = _Hm2IndustrialProtocolsMibSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3)
)
_Hm2Iec61850SESGroup_ObjectIdentity = ObjectIdentity
hm2Iec61850SESGroup = _Hm2Iec61850SESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 1)
)
_Hm2ProfinetIOSESGroup_ObjectIdentity = ObjectIdentity
hm2ProfinetIOSESGroup = _Hm2ProfinetIOSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 2)
)
_Hm2ProfinetIOInvalidStationName_ObjectIdentity = ObjectIdentity
hm2ProfinetIOInvalidStationName = _Hm2ProfinetIOInvalidStationName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hm2ProfinetIOInvalidStationName.setStatus("current")
_Hm2ProfinetIOARActive_ObjectIdentity = ObjectIdentity
hm2ProfinetIOARActive = _Hm2ProfinetIOARActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hm2ProfinetIOARActive.setStatus("current")
_Hm2EthernetIPSESGroup_ObjectIdentity = ObjectIdentity
hm2EthernetIPSESGroup = _Hm2EthernetIPSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 3)
)
_Hm2EthernetIPUsedVlanId_ObjectIdentity = ObjectIdentity
hm2EthernetIPUsedVlanId = _Hm2EthernetIPUsedVlanId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hm2EthernetIPUsedVlanId.setStatus("current")
_Hm2EthernetIPNoVlanId_ObjectIdentity = ObjectIdentity
hm2EthernetIPNoVlanId = _Hm2EthernetIPNoVlanId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hm2EthernetIPNoVlanId.setStatus("current")
_Hm2EthernetIPDynamicVlan_ObjectIdentity = ObjectIdentity
hm2EthernetIPDynamicVlan = _Hm2EthernetIPDynamicVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hm2EthernetIPDynamicVlan.setStatus("current")
_Hm2EthernetIPVlanUnaware_ObjectIdentity = ObjectIdentity
hm2EthernetIPVlanUnaware = _Hm2EthernetIPVlanUnaware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hm2EthernetIPVlanUnaware.setStatus("current")
_Hm2ModbusSESGroup_ObjectIdentity = ObjectIdentity
hm2ModbusSESGroup = _Hm2ModbusSESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 4)
)
_Hm2Iec62541SESGroup_ObjectIdentity = ObjectIdentity
hm2Iec62541SESGroup = _Hm2Iec62541SESGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 101, 3, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-INDUSTRIAL-PROTOCOLS-MIB",
    **{"Hm2Iec62541OpcUaUserAccessRoles": Hm2Iec62541OpcUaUserAccessRoles,
       "Hm2Iec62541OpcUaSecurityPolicies": Hm2Iec62541OpcUaSecurityPolicies,
       "hm2IndustrialProtocolsMib": hm2IndustrialProtocolsMib,
       "hm2IndustrialProtocolsNotifications": hm2IndustrialProtocolsNotifications,
       "hm2IndustrialProtocolsMibObjects": hm2IndustrialProtocolsMibObjects,
       "hm2Iec61850Group": hm2Iec61850Group,
       "hm2Iec61850ConfigGroup": hm2Iec61850ConfigGroup,
       "hm2Iec61850MmsServerAdminStatus": hm2Iec61850MmsServerAdminStatus,
       "hm2Iec61850MmsServerWriteAccessStatus": hm2Iec61850MmsServerWriteAccessStatus,
       "hm2Iec61850MmsServerPortNumber": hm2Iec61850MmsServerPortNumber,
       "hm2Iec61850MmsServerMaxSessionsCount": hm2Iec61850MmsServerMaxSessionsCount,
       "hm2Iec61850MmsServerTechnicalKey": hm2Iec61850MmsServerTechnicalKey,
       "hm2Iec61850MmsTlsServerAdminStatus": hm2Iec61850MmsTlsServerAdminStatus,
       "hm2Iec61850MmsTlsServerWriteAccessStatus": hm2Iec61850MmsTlsServerWriteAccessStatus,
       "hm2Iec61850MmsTlsServerPortNumber": hm2Iec61850MmsTlsServerPortNumber,
       "hm2Iec61850MmsTlsServerMaxSessionsCount": hm2Iec61850MmsTlsServerMaxSessionsCount,
       "hm2Iec61850MmsTlsServerKeysPresent": hm2Iec61850MmsTlsServerKeysPresent,
       "hm2Iec61850MmsTlsServerKeyOperStatus": hm2Iec61850MmsTlsServerKeyOperStatus,
       "hm2Iec61850MmsTlsServerRSAKeyControl": hm2Iec61850MmsTlsServerRSAKeyControl,
       "hm2Iec61850MmsTlsServerDSAKeyControl": hm2Iec61850MmsTlsServerDSAKeyControl,
       "hm2Iec61850MmsTlsServerFingerPrintDSA": hm2Iec61850MmsTlsServerFingerPrintDSA,
       "hm2Iec61850MmsTlsServerFingerPrintRSA": hm2Iec61850MmsTlsServerFingerPrintRSA,
       "hm2Iec61850MmsServerStatus": hm2Iec61850MmsServerStatus,
       "hm2Iec61850StatisticsGroup": hm2Iec61850StatisticsGroup,
       "hm2Iec61850MmsServerSessionsCount": hm2Iec61850MmsServerSessionsCount,
       "hm2Iec61850MmsTlsServerSessionsCount": hm2Iec61850MmsTlsServerSessionsCount,
       "hm2ProfinetIOGroup": hm2ProfinetIOGroup,
       "hm2ProfinetIOConfigGroup": hm2ProfinetIOConfigGroup,
       "hm2PNIOAdminStatus": hm2PNIOAdminStatus,
       "hm2PNIODeviceID": hm2PNIODeviceID,
       "hm2PNIOModuleIdentNumber": hm2PNIOModuleIdentNumber,
       "hm2PNIOOrderID": hm2PNIOOrderID,
       "hm2PNIODeviceTypeDetails": hm2PNIODeviceTypeDetails,
       "hm2PNIOSoftwareRelease": hm2PNIOSoftwareRelease,
       "hm2PNIOHardwareRelease": hm2PNIOHardwareRelease,
       "hm2PNIOOrderID9th": hm2PNIOOrderID9th,
       "hm2PNIONameOfStation": hm2PNIONameOfStation,
       "hm2PNIONumActiveApplicationRelations": hm2PNIONumActiveApplicationRelations,
       "hm2PNIOClearIpParameter": hm2PNIOClearIpParameter,
       "hm2PNIODcpModeTable": hm2PNIODcpModeTable,
       "hm2PNIODcpModeEntry": hm2PNIODcpModeEntry,
       "hm2PNIODcpModePortID": hm2PNIODcpModePortID,
       "hm2PNIODcpMode": hm2PNIODcpMode,
       "hm2PNIOIm1Data": hm2PNIOIm1Data,
       "hm2PNIOIm2Data": hm2PNIOIm2Data,
       "hm2PNIOIm3Data": hm2PNIOIm3Data,
       "hm2PNIOIm4Data": hm2PNIOIm4Data,
       "hm2PNIOClearStationName": hm2PNIOClearStationName,
       "hm2PNIOPdevParameters": hm2PNIOPdevParameters,
       "hm2ProfinetIOStatisticsGroup": hm2ProfinetIOStatisticsGroup,
       "hm2EthernetIPGroup": hm2EthernetIPGroup,
       "hm2EthernetIPConfigGroup": hm2EthernetIPConfigGroup,
       "hm2EtherNetIPAdminStatus": hm2EtherNetIPAdminStatus,
       "hm2EtherNetIPErrorCode": hm2EtherNetIPErrorCode,
       "hm2EtherNetIPProductCode": hm2EtherNetIPProductCode,
       "hm2EtherNetIPMajorRevision": hm2EtherNetIPMajorRevision,
       "hm2EtherNetIPMinorRevision": hm2EtherNetIPMinorRevision,
       "hm2EtherNetIPProductName": hm2EtherNetIPProductName,
       "hm2EtherNetIPCatalogName": hm2EtherNetIPCatalogName,
       "hm2EtherNetIPWriteAccessStatus": hm2EtherNetIPWriteAccessStatus,
       "hm2EtherNetIPVlan": hm2EtherNetIPVlan,
       "hm2EtherNetIPInterface": hm2EtherNetIPInterface,
       "hm2EthernetIPStatisticsGroup": hm2EthernetIPStatisticsGroup,
       "hm2EtherNetIPConnEstablished": hm2EtherNetIPConnEstablished,
       "hm2EtherNetIPConnTimeouts": hm2EtherNetIPConnTimeouts,
       "hm2EtherNetIPVendorObjRequests": hm2EtherNetIPVendorObjRequests,
       "hm2EthernetIPTCPIPObjectGroup": hm2EthernetIPTCPIPObjectGroup,
       "hm2EtherNetIPMcastTTLValue": hm2EtherNetIPMcastTTLValue,
       "hm2EtherNetIPMcastAllocControl": hm2EtherNetIPMcastAllocControl,
       "hm2EtherNetIPMcastCount": hm2EtherNetIPMcastCount,
       "hm2EtherNetIPMcastStartAddress": hm2EtherNetIPMcastStartAddress,
       "hm2EtherNetIPLastConflictDetectedACDActivity": hm2EtherNetIPLastConflictDetectedACDActivity,
       "hm2EtherNetIPSelectACDStatus": hm2EtherNetIPSelectACDStatus,
       "hm2EtherNetIPEncapsulationInactivity": hm2EtherNetIPEncapsulationInactivity,
       "hm2EthernetIPQoSObjectGroup": hm2EthernetIPQoSObjectGroup,
       "hm2EtherNetIPQosDscpUrgentValue": hm2EtherNetIPQosDscpUrgentValue,
       "hm2EtherNetIPQosDscpScheduledValue": hm2EtherNetIPQosDscpScheduledValue,
       "hm2EtherNetIPQosDscpHighValue": hm2EtherNetIPQosDscpHighValue,
       "hm2EtherNetIPQosDscpLowValue": hm2EtherNetIPQosDscpLowValue,
       "hm2EtherNetIPQosDscpExplicitValue": hm2EtherNetIPQosDscpExplicitValue,
       "hm2EtherNetIPQosValue": hm2EtherNetIPQosValue,
       "hm2ModbusGroup": hm2ModbusGroup,
       "hm2ModbusConfigGroup": hm2ModbusConfigGroup,
       "hm2ModbusTcpServerAdminStatus": hm2ModbusTcpServerAdminStatus,
       "hm2ModbusTcpServerWriteAccessStatus": hm2ModbusTcpServerWriteAccessStatus,
       "hm2ModbusTcpServerPortNumber": hm2ModbusTcpServerPortNumber,
       "hm2ModbusTcpServerMaxSessionsCount": hm2ModbusTcpServerMaxSessionsCount,
       "hm2ModbusStatisticsGroup": hm2ModbusStatisticsGroup,
       "hm2ModbusTcpServerSessionsCount": hm2ModbusTcpServerSessionsCount,
       "hm2Iec62541Group": hm2Iec62541Group,
       "hm2Iec62541ConfigGroup": hm2Iec62541ConfigGroup,
       "hm2Iec62541OpcUaServerAdminStatus": hm2Iec62541OpcUaServerAdminStatus,
       "hm2Iec62541OpcUaServerPortNumber": hm2Iec62541OpcUaServerPortNumber,
       "hm2Iec62541OpcUaMaxSessionsCount": hm2Iec62541OpcUaMaxSessionsCount,
       "hm2Iec62541OpcUaSecurityPolicy": hm2Iec62541OpcUaSecurityPolicy,
       "hm2Iec62541OpcUaUserConfigTable": hm2Iec62541OpcUaUserConfigTable,
       "hm2Iec62541OpcUaUserConfigEntry": hm2Iec62541OpcUaUserConfigEntry,
       "hm2Iec62541OpcUaUserName": hm2Iec62541OpcUaUserName,
       "hm2Iec62541OpcUaUserPassword": hm2Iec62541OpcUaUserPassword,
       "hm2Iec62541OpcUaUserAccessRole": hm2Iec62541OpcUaUserAccessRole,
       "hm2Iec62541OpcUaUserStatus": hm2Iec62541OpcUaUserStatus,
       "hm2IndustrialProtocolsMibSNMPExtensionGroup": hm2IndustrialProtocolsMibSNMPExtensionGroup,
       "hm2Iec61850SESGroup": hm2Iec61850SESGroup,
       "hm2ProfinetIOSESGroup": hm2ProfinetIOSESGroup,
       "hm2ProfinetIOInvalidStationName": hm2ProfinetIOInvalidStationName,
       "hm2ProfinetIOARActive": hm2ProfinetIOARActive,
       "hm2EthernetIPSESGroup": hm2EthernetIPSESGroup,
       "hm2EthernetIPUsedVlanId": hm2EthernetIPUsedVlanId,
       "hm2EthernetIPNoVlanId": hm2EthernetIPNoVlanId,
       "hm2EthernetIPDynamicVlan": hm2EthernetIPDynamicVlan,
       "hm2EthernetIPVlanUnaware": hm2EthernetIPVlanUnaware,
       "hm2ModbusSESGroup": hm2ModbusSESGroup,
       "hm2Iec62541SESGroup": hm2Iec62541SESGroup}
)
