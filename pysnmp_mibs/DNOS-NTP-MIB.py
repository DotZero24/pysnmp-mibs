# SNMP MIB module (DNOS-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:08:31 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

agentNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168)
)
if mibBuilder.loadTexts:
    agentNtpMIB.setRevisions(
        ("2021-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentNtpObjects_ObjectIdentity = ObjectIdentity
agentNtpObjects = _AgentNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1)
)
_AgentNtpConfigGroup_ObjectIdentity = ObjectIdentity
agentNtpConfigGroup = _AgentNtpConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1)
)


class _AgentNtpAuthenticationMode_Type(TruthValue):
    """Custom type agentNtpAuthenticationMode based on TruthValue"""
    defaultValue = 2


_AgentNtpAuthenticationMode_Type.__name__ = "TruthValue"
_AgentNtpAuthenticationMode_Object = MibScalar
agentNtpAuthenticationMode = _AgentNtpAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 1),
    _AgentNtpAuthenticationMode_Type()
)
agentNtpAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpAuthenticationMode.setStatus("current")


class _AgentNtpBroadcastDelay_Type(Unsigned32):
    """Custom type agentNtpBroadcastDelay based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_AgentNtpBroadcastDelay_Type.__name__ = "Unsigned32"
_AgentNtpBroadcastDelay_Object = MibScalar
agentNtpBroadcastDelay = _AgentNtpBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 2),
    _AgentNtpBroadcastDelay_Type()
)
agentNtpBroadcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpBroadcastDelay.setStatus("current")


class _AgentNtpBroadcastClientMode_Type(Integer32):
    """Custom type agentNtpBroadcastClientMode based on Integer32"""
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


_AgentNtpBroadcastClientMode_Type.__name__ = "Integer32"
_AgentNtpBroadcastClientMode_Object = MibScalar
agentNtpBroadcastClientMode = _AgentNtpBroadcastClientMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 3),
    _AgentNtpBroadcastClientMode_Type()
)
agentNtpBroadcastClientMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpBroadcastClientMode.setStatus("current")
_AgentNtpSourceInterface_Type = InterfaceIndexOrZero
_AgentNtpSourceInterface_Object = MibScalar
agentNtpSourceInterface = _AgentNtpSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 4),
    _AgentNtpSourceInterface_Type()
)
agentNtpSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpSourceInterface.setStatus("current")


class _AgentNtpServicePortSrcInterface_Type(Integer32):
    """Custom type agentNtpServicePortSrcInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("servicePortEnable", 1),
          ("servicePortDisable", 2))
    )


_AgentNtpServicePortSrcInterface_Type.__name__ = "Integer32"
_AgentNtpServicePortSrcInterface_Object = MibScalar
agentNtpServicePortSrcInterface = _AgentNtpServicePortSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 5),
    _AgentNtpServicePortSrcInterface_Type()
)
agentNtpServicePortSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServicePortSrcInterface.setStatus("current")


class _AgentNtpVrfName_Type(DisplayString):
    """Custom type agentNtpVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AgentNtpVrfName_Type.__name__ = "DisplayString"
_AgentNtpVrfName_Object = MibScalar
agentNtpVrfName = _AgentNtpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 6),
    _AgentNtpVrfName_Type()
)
agentNtpVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpVrfName.setStatus("current")
_AgentNtpAuthKeyTable_Object = MibTable
agentNtpAuthKeyTable = _AgentNtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7)
)
if mibBuilder.loadTexts:
    agentNtpAuthKeyTable.setStatus("current")
_AgentNtpAuthKeyEntry_Object = MibTableRow
agentNtpAuthKeyEntry = _AgentNtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1)
)
agentNtpAuthKeyEntry.setIndexNames(
    (0, "DNOS-NTP-MIB", "agentNtpAuthKeyIndex"),
)
if mibBuilder.loadTexts:
    agentNtpAuthKeyEntry.setStatus("current")


class _AgentNtpAuthKeyIndex_Type(Unsigned32):
    """Custom type agentNtpAuthKeyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AgentNtpAuthKeyIndex_Type.__name__ = "Unsigned32"
_AgentNtpAuthKeyIndex_Object = MibTableColumn
agentNtpAuthKeyIndex = _AgentNtpAuthKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 1),
    _AgentNtpAuthKeyIndex_Type()
)
agentNtpAuthKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentNtpAuthKeyIndex.setStatus("current")


class _AgentNtpAuthKeyNumber_Type(Unsigned32):
    """Custom type agentNtpAuthKeyNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentNtpAuthKeyNumber_Type.__name__ = "Unsigned32"
_AgentNtpAuthKeyNumber_Object = MibTableColumn
agentNtpAuthKeyNumber = _AgentNtpAuthKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 2),
    _AgentNtpAuthKeyNumber_Type()
)
agentNtpAuthKeyNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpAuthKeyNumber.setStatus("current")


class _AgentNtpAuthKeyMessageAuthAlg_Type(Integer32):
    """Custom type agentNtpAuthKeyMessageAuthAlg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha1", 2),
          ("sha2", 3))
    )


_AgentNtpAuthKeyMessageAuthAlg_Type.__name__ = "Integer32"
_AgentNtpAuthKeyMessageAuthAlg_Object = MibTableColumn
agentNtpAuthKeyMessageAuthAlg = _AgentNtpAuthKeyMessageAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 3),
    _AgentNtpAuthKeyMessageAuthAlg_Type()
)
agentNtpAuthKeyMessageAuthAlg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpAuthKeyMessageAuthAlg.setStatus("current")


class _AgentNtpAuthKeyEncryptionStatus_Type(TruthValue):
    """Custom type agentNtpAuthKeyEncryptionStatus based on TruthValue"""
    defaultValue = 2


_AgentNtpAuthKeyEncryptionStatus_Type.__name__ = "TruthValue"
_AgentNtpAuthKeyEncryptionStatus_Object = MibTableColumn
agentNtpAuthKeyEncryptionStatus = _AgentNtpAuthKeyEncryptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 4),
    _AgentNtpAuthKeyEncryptionStatus_Type()
)
agentNtpAuthKeyEncryptionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpAuthKeyEncryptionStatus.setStatus("current")


class _AgentNtpAuthKeyName_Type(DisplayString):
    """Custom type agentNtpAuthKeyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentNtpAuthKeyName_Type.__name__ = "DisplayString"
_AgentNtpAuthKeyName_Object = MibTableColumn
agentNtpAuthKeyName = _AgentNtpAuthKeyName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 5),
    _AgentNtpAuthKeyName_Type()
)
agentNtpAuthKeyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpAuthKeyName.setStatus("current")


class _AgentNtpAuthKeyTrustedStatus_Type(TruthValue):
    """Custom type agentNtpAuthKeyTrustedStatus based on TruthValue"""
    defaultValue = 2


_AgentNtpAuthKeyTrustedStatus_Type.__name__ = "TruthValue"
_AgentNtpAuthKeyTrustedStatus_Object = MibTableColumn
agentNtpAuthKeyTrustedStatus = _AgentNtpAuthKeyTrustedStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 6),
    _AgentNtpAuthKeyTrustedStatus_Type()
)
agentNtpAuthKeyTrustedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpAuthKeyTrustedStatus.setStatus("current")
_AgentNtpAuthKeyRowStatus_Type = RowStatus
_AgentNtpAuthKeyRowStatus_Object = MibTableColumn
agentNtpAuthKeyRowStatus = _AgentNtpAuthKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 7, 1, 7),
    _AgentNtpAuthKeyRowStatus_Type()
)
agentNtpAuthKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpAuthKeyRowStatus.setStatus("current")
_AgentNtpServerTable_Object = MibTable
agentNtpServerTable = _AgentNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8)
)
if mibBuilder.loadTexts:
    agentNtpServerTable.setStatus("current")
_AgentNtpServerEntry_Object = MibTableRow
agentNtpServerEntry = _AgentNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1)
)
agentNtpServerEntry.setIndexNames(
    (0, "DNOS-NTP-MIB", "agentNtpServerIndex"),
)
if mibBuilder.loadTexts:
    agentNtpServerEntry.setStatus("current")


class _AgentNtpServerIndex_Type(Unsigned32):
    """Custom type agentNtpServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AgentNtpServerIndex_Type.__name__ = "Unsigned32"
_AgentNtpServerIndex_Object = MibTableColumn
agentNtpServerIndex = _AgentNtpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 1),
    _AgentNtpServerIndex_Type()
)
agentNtpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentNtpServerIndex.setStatus("current")
_AgentNtpServerAddressType_Type = InetAddressType
_AgentNtpServerAddressType_Object = MibTableColumn
agentNtpServerAddressType = _AgentNtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 2),
    _AgentNtpServerAddressType_Type()
)
agentNtpServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpServerAddressType.setStatus("current")


class _AgentNtpServerAddress_Type(InetAddress):
    """Custom type agentNtpServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentNtpServerAddress_Type.__name__ = "InetAddress"
_AgentNtpServerAddress_Object = MibTableColumn
agentNtpServerAddress = _AgentNtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 3),
    _AgentNtpServerAddress_Type()
)
agentNtpServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpServerAddress.setStatus("current")


class _AgentNtpServerVersion_Type(Integer32):
    """Custom type agentNtpServerVersion based on Integer32"""
    defaultValue = 4

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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_AgentNtpServerVersion_Type.__name__ = "Integer32"
_AgentNtpServerVersion_Object = MibTableColumn
agentNtpServerVersion = _AgentNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 4),
    _AgentNtpServerVersion_Type()
)
agentNtpServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerVersion.setStatus("current")


class _AgentNtpServerAuthKeyNumber_Type(Unsigned32):
    """Custom type agentNtpServerAuthKeyNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentNtpServerAuthKeyNumber_Type.__name__ = "Unsigned32"
_AgentNtpServerAuthKeyNumber_Object = MibTableColumn
agentNtpServerAuthKeyNumber = _AgentNtpServerAuthKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 5),
    _AgentNtpServerAuthKeyNumber_Type()
)
agentNtpServerAuthKeyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerAuthKeyNumber.setStatus("current")


class _AgentNtpServerMinPollInterval_Type(Unsigned32):
    """Custom type agentNtpServerMinPollInterval based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 10),
    )


_AgentNtpServerMinPollInterval_Type.__name__ = "Unsigned32"
_AgentNtpServerMinPollInterval_Object = MibTableColumn
agentNtpServerMinPollInterval = _AgentNtpServerMinPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 6),
    _AgentNtpServerMinPollInterval_Type()
)
agentNtpServerMinPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerMinPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentNtpServerMinPollInterval.setUnits("seconds")


class _AgentNtpServerMaxPollInterval_Type(Unsigned32):
    """Custom type agentNtpServerMaxPollInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 10),
    )


_AgentNtpServerMaxPollInterval_Type.__name__ = "Unsigned32"
_AgentNtpServerMaxPollInterval_Object = MibTableColumn
agentNtpServerMaxPollInterval = _AgentNtpServerMaxPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 7),
    _AgentNtpServerMaxPollInterval_Type()
)
agentNtpServerMaxPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerMaxPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentNtpServerMaxPollInterval.setUnits("seconds")


class _AgentNtpServerPreferStatus_Type(TruthValue):
    """Custom type agentNtpServerPreferStatus based on TruthValue"""
    defaultValue = 2


_AgentNtpServerPreferStatus_Type.__name__ = "TruthValue"
_AgentNtpServerPreferStatus_Object = MibTableColumn
agentNtpServerPreferStatus = _AgentNtpServerPreferStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 8),
    _AgentNtpServerPreferStatus_Type()
)
agentNtpServerPreferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerPreferStatus.setStatus("current")


class _AgentNtpServerBurstStatus_Type(TruthValue):
    """Custom type agentNtpServerBurstStatus based on TruthValue"""
    defaultValue = 2


_AgentNtpServerBurstStatus_Type.__name__ = "TruthValue"
_AgentNtpServerBurstStatus_Object = MibTableColumn
agentNtpServerBurstStatus = _AgentNtpServerBurstStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 9),
    _AgentNtpServerBurstStatus_Type()
)
agentNtpServerBurstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerBurstStatus.setStatus("current")


class _AgentNtpServerIburstStatus_Type(TruthValue):
    """Custom type agentNtpServerIburstStatus based on TruthValue"""
    defaultValue = 2


_AgentNtpServerIburstStatus_Type.__name__ = "TruthValue"
_AgentNtpServerIburstStatus_Object = MibTableColumn
agentNtpServerIburstStatus = _AgentNtpServerIburstStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 10),
    _AgentNtpServerIburstStatus_Type()
)
agentNtpServerIburstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNtpServerIburstStatus.setStatus("current")
_AgentNtpServerRowStatus_Type = RowStatus
_AgentNtpServerRowStatus_Object = MibTableColumn
agentNtpServerRowStatus = _AgentNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 168, 1, 1, 8, 1, 11),
    _AgentNtpServerRowStatus_Type()
)
agentNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentNtpServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-NTP-MIB",
    **{"agentNtpMIB": agentNtpMIB,
       "agentNtpObjects": agentNtpObjects,
       "agentNtpConfigGroup": agentNtpConfigGroup,
       "agentNtpAuthenticationMode": agentNtpAuthenticationMode,
       "agentNtpBroadcastDelay": agentNtpBroadcastDelay,
       "agentNtpBroadcastClientMode": agentNtpBroadcastClientMode,
       "agentNtpSourceInterface": agentNtpSourceInterface,
       "agentNtpServicePortSrcInterface": agentNtpServicePortSrcInterface,
       "agentNtpVrfName": agentNtpVrfName,
       "agentNtpAuthKeyTable": agentNtpAuthKeyTable,
       "agentNtpAuthKeyEntry": agentNtpAuthKeyEntry,
       "agentNtpAuthKeyIndex": agentNtpAuthKeyIndex,
       "agentNtpAuthKeyNumber": agentNtpAuthKeyNumber,
       "agentNtpAuthKeyMessageAuthAlg": agentNtpAuthKeyMessageAuthAlg,
       "agentNtpAuthKeyEncryptionStatus": agentNtpAuthKeyEncryptionStatus,
       "agentNtpAuthKeyName": agentNtpAuthKeyName,
       "agentNtpAuthKeyTrustedStatus": agentNtpAuthKeyTrustedStatus,
       "agentNtpAuthKeyRowStatus": agentNtpAuthKeyRowStatus,
       "agentNtpServerTable": agentNtpServerTable,
       "agentNtpServerEntry": agentNtpServerEntry,
       "agentNtpServerIndex": agentNtpServerIndex,
       "agentNtpServerAddressType": agentNtpServerAddressType,
       "agentNtpServerAddress": agentNtpServerAddress,
       "agentNtpServerVersion": agentNtpServerVersion,
       "agentNtpServerAuthKeyNumber": agentNtpServerAuthKeyNumber,
       "agentNtpServerMinPollInterval": agentNtpServerMinPollInterval,
       "agentNtpServerMaxPollInterval": agentNtpServerMaxPollInterval,
       "agentNtpServerPreferStatus": agentNtpServerPreferStatus,
       "agentNtpServerBurstStatus": agentNtpServerBurstStatus,
       "agentNtpServerIburstStatus": agentNtpServerIburstStatus,
       "agentNtpServerRowStatus": agentNtpServerRowStatus}
)
