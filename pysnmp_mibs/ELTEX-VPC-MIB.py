# SNMP MIB module (ELTEX-VPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-VPC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:25 2025
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

(eltexLtd,) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "eltexLtd")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltexVpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 125)
)
if mibBuilder.loadTexts:
    eltexVpcMIB.setRevisions(
        ("2018-09-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltexVpcMIBObjects_ObjectIdentity = ObjectIdentity
eltexVpcMIBObjects = _EltexVpcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1)
)
_EltexVpcConfigGroup_ObjectIdentity = ObjectIdentity
eltexVpcConfigGroup = _EltexVpcConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1)
)


class _EltexVpcMode_Type(Integer32):
    """Custom type eltexVpcMode based on Integer32"""
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


_EltexVpcMode_Type.__name__ = "Integer32"
_EltexVpcMode_Object = MibScalar
eltexVpcMode = _EltexVpcMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 1),
    _EltexVpcMode_Type()
)
eltexVpcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcMode.setStatus("current")
_EltexVpcDomainConfigTable_Object = MibTable
eltexVpcDomainConfigTable = _EltexVpcDomainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltexVpcDomainConfigTable.setStatus("current")
_EltexVpcDomainConfigEntry_Object = MibTableRow
eltexVpcDomainConfigEntry = _EltexVpcDomainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1)
)
eltexVpcDomainConfigEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcDomainIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcDomainConfigEntry.setStatus("current")


class _EltexVpcDomainIndex_Type(Unsigned32):
    """Custom type eltexVpcDomainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EltexVpcDomainIndex_Type.__name__ = "Unsigned32"
_EltexVpcDomainIndex_Object = MibTableColumn
eltexVpcDomainIndex = _EltexVpcDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 1),
    _EltexVpcDomainIndex_Type()
)
eltexVpcDomainIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainIndex.setStatus("current")
_EltexVpcDomainPeerLink_Type = InterfaceIndexOrZero
_EltexVpcDomainPeerLink_Object = MibTableColumn
eltexVpcDomainPeerLink = _EltexVpcDomainPeerLink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 2),
    _EltexVpcDomainPeerLink_Type()
)
eltexVpcDomainPeerLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLink.setStatus("current")


class _EltexVpcDomainKeepalivePriority_Type(Unsigned32):
    """Custom type eltexVpcDomainKeepalivePriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EltexVpcDomainKeepalivePriority_Type.__name__ = "Unsigned32"
_EltexVpcDomainKeepalivePriority_Object = MibTableColumn
eltexVpcDomainKeepalivePriority = _EltexVpcDomainKeepalivePriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 3),
    _EltexVpcDomainKeepalivePriority_Type()
)
eltexVpcDomainKeepalivePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainKeepalivePriority.setStatus("current")


class _EltexVpcDomainKeepaliveTimeout_Type(Unsigned32):
    """Custom type eltexVpcDomainKeepaliveTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_EltexVpcDomainKeepaliveTimeout_Type.__name__ = "Unsigned32"
_EltexVpcDomainKeepaliveTimeout_Object = MibTableColumn
eltexVpcDomainKeepaliveTimeout = _EltexVpcDomainKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 4),
    _EltexVpcDomainKeepaliveTimeout_Type()
)
eltexVpcDomainKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainKeepaliveTimeout.setStatus("current")


class _EltexVpcDomainKeepaliveMode_Type(Integer32):
    """Custom type eltexVpcDomainKeepaliveMode based on Integer32"""
    defaultValue = 2

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


_EltexVpcDomainKeepaliveMode_Type.__name__ = "Integer32"
_EltexVpcDomainKeepaliveMode_Object = MibTableColumn
eltexVpcDomainKeepaliveMode = _EltexVpcDomainKeepaliveMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 5),
    _EltexVpcDomainKeepaliveMode_Type()
)
eltexVpcDomainKeepaliveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainKeepaliveMode.setStatus("current")
_EltexVpcDomainSystemMac_Type = MacAddress
_EltexVpcDomainSystemMac_Object = MibTableColumn
eltexVpcDomainSystemMac = _EltexVpcDomainSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 6),
    _EltexVpcDomainSystemMac_Type()
)
eltexVpcDomainSystemMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainSystemMac.setStatus("current")


class _EltexVpcDomainSystemPriority_Type(Unsigned32):
    """Custom type eltexVpcDomainSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexVpcDomainSystemPriority_Type.__name__ = "Unsigned32"
_EltexVpcDomainSystemPriority_Object = MibTableColumn
eltexVpcDomainSystemPriority = _EltexVpcDomainSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 7),
    _EltexVpcDomainSystemPriority_Type()
)
eltexVpcDomainSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainSystemPriority.setStatus("current")


class _EltexVpcDomainPeerDetectionMode_Type(Integer32):
    """Custom type eltexVpcDomainPeerDetectionMode based on Integer32"""
    defaultValue = 2

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


_EltexVpcDomainPeerDetectionMode_Type.__name__ = "Integer32"
_EltexVpcDomainPeerDetectionMode_Object = MibTableColumn
eltexVpcDomainPeerDetectionMode = _EltexVpcDomainPeerDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 8),
    _EltexVpcDomainPeerDetectionMode_Type()
)
eltexVpcDomainPeerDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionMode.setStatus("current")


class _EltexVpcDomainPeerDetectionInterval_Type(Unsigned32):
    """Custom type eltexVpcDomainPeerDetectionInterval based on Unsigned32"""
    defaultValue = 700

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 4000),
    )


_EltexVpcDomainPeerDetectionInterval_Type.__name__ = "Unsigned32"
_EltexVpcDomainPeerDetectionInterval_Object = MibTableColumn
eltexVpcDomainPeerDetectionInterval = _EltexVpcDomainPeerDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 9),
    _EltexVpcDomainPeerDetectionInterval_Type()
)
eltexVpcDomainPeerDetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionInterval.setStatus("current")


class _EltexVpcDomainPeerDetectionTimeout_Type(Unsigned32):
    """Custom type eltexVpcDomainPeerDetectionTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(700, 14000),
    )


_EltexVpcDomainPeerDetectionTimeout_Type.__name__ = "Unsigned32"
_EltexVpcDomainPeerDetectionTimeout_Object = MibTableColumn
eltexVpcDomainPeerDetectionTimeout = _EltexVpcDomainPeerDetectionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 10),
    _EltexVpcDomainPeerDetectionTimeout_Type()
)
eltexVpcDomainPeerDetectionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionTimeout.setStatus("current")


class _EltexVpcDomainPeerIpAddr_Type(IpAddress):
    """Custom type eltexVpcDomainPeerIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_EltexVpcDomainPeerIpAddr_Type.__name__ = "IpAddress"
_EltexVpcDomainPeerIpAddr_Object = MibTableColumn
eltexVpcDomainPeerIpAddr = _EltexVpcDomainPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 11),
    _EltexVpcDomainPeerIpAddr_Type()
)
eltexVpcDomainPeerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerIpAddr.setStatus("current")


class _EltexVpcDomainSourceIpAddr_Type(IpAddress):
    """Custom type eltexVpcDomainSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_EltexVpcDomainSourceIpAddr_Type.__name__ = "IpAddress"
_EltexVpcDomainSourceIpAddr_Object = MibTableColumn
eltexVpcDomainSourceIpAddr = _EltexVpcDomainSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 12),
    _EltexVpcDomainSourceIpAddr_Type()
)
eltexVpcDomainSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainSourceIpAddr.setStatus("current")


class _EltexVpcDomainDcpdpUdpPort_Type(Unsigned32):
    """Custom type eltexVpcDomainDcpdpUdpPort based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexVpcDomainDcpdpUdpPort_Type.__name__ = "Unsigned32"
_EltexVpcDomainDcpdpUdpPort_Object = MibTableColumn
eltexVpcDomainDcpdpUdpPort = _EltexVpcDomainDcpdpUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 13),
    _EltexVpcDomainDcpdpUdpPort_Type()
)
eltexVpcDomainDcpdpUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcDomainDcpdpUdpPort.setStatus("current")
_EltexVpcDomainStatus_Type = RowStatus
_EltexVpcDomainStatus_Object = MibTableColumn
eltexVpcDomainStatus = _EltexVpcDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 2, 1, 14),
    _EltexVpcDomainStatus_Type()
)
eltexVpcDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexVpcDomainStatus.setStatus("current")
_EltexVpcGroupConfigTable_Object = MibTable
eltexVpcGroupConfigTable = _EltexVpcGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltexVpcGroupConfigTable.setStatus("current")
_EltexVpcGroupConfigEntry_Object = MibTableRow
eltexVpcGroupConfigEntry = _EltexVpcGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1)
)
eltexVpcGroupConfigEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcGroupIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcGroupConfigEntry.setStatus("current")


class _EltexVpcGroupIndex_Type(Unsigned32):
    """Custom type eltexVpcGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_EltexVpcGroupIndex_Type.__name__ = "Unsigned32"
_EltexVpcGroupIndex_Object = MibTableColumn
eltexVpcGroupIndex = _EltexVpcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1, 1),
    _EltexVpcGroupIndex_Type()
)
eltexVpcGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcGroupIndex.setStatus("current")


class _EltexVpcGroupDomainIndex_Type(Unsigned32):
    """Custom type eltexVpcGroupDomainIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EltexVpcGroupDomainIndex_Type.__name__ = "Unsigned32"
_EltexVpcGroupDomainIndex_Object = MibTableColumn
eltexVpcGroupDomainIndex = _EltexVpcGroupDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1, 2),
    _EltexVpcGroupDomainIndex_Type()
)
eltexVpcGroupDomainIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcGroupDomainIndex.setStatus("current")


class _EltexVpcGroupPortChannelIfIndex_Type(InterfaceIndexOrZero):
    """Custom type eltexVpcGroupPortChannelIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_EltexVpcGroupPortChannelIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_EltexVpcGroupPortChannelIfIndex_Object = MibTableColumn
eltexVpcGroupPortChannelIfIndex = _EltexVpcGroupPortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1, 3),
    _EltexVpcGroupPortChannelIfIndex_Type()
)
eltexVpcGroupPortChannelIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltexVpcGroupPortChannelIfIndex.setStatus("current")


class _EltexVpcGroupOperationalStatus_Type(Integer32):
    """Custom type eltexVpcGroupOperationalStatus based on Integer32"""
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


_EltexVpcGroupOperationalStatus_Type.__name__ = "Integer32"
_EltexVpcGroupOperationalStatus_Object = MibTableColumn
eltexVpcGroupOperationalStatus = _EltexVpcGroupOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1, 4),
    _EltexVpcGroupOperationalStatus_Type()
)
eltexVpcGroupOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcGroupOperationalStatus.setStatus("current")


class _EltexVpcGroupInterfaceState_Type(Integer32):
    """Custom type eltexVpcGroupInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("wait", 2),
          ("error", 3),
          ("active", 4),
          ("inactive", 5))
    )


_EltexVpcGroupInterfaceState_Type.__name__ = "Integer32"
_EltexVpcGroupInterfaceState_Object = MibTableColumn
eltexVpcGroupInterfaceState = _EltexVpcGroupInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1, 5),
    _EltexVpcGroupInterfaceState_Type()
)
eltexVpcGroupInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcGroupInterfaceState.setStatus("current")
_EltexVpcGroupStatus_Type = RowStatus
_EltexVpcGroupStatus_Object = MibTableColumn
eltexVpcGroupStatus = _EltexVpcGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 1, 3, 1, 6),
    _EltexVpcGroupStatus_Type()
)
eltexVpcGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltexVpcGroupStatus.setStatus("current")
_EltexVpcStatusGroup_ObjectIdentity = ObjectIdentity
eltexVpcStatusGroup = _EltexVpcStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2)
)
_EltexVpcDomainStatusTable_Object = MibTable
eltexVpcDomainStatusTable = _EltexVpcDomainStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltexVpcDomainStatusTable.setStatus("current")
_EltexVpcDomainStatusEntry_Object = MibTableRow
eltexVpcDomainStatusEntry = _EltexVpcDomainStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1)
)
eltexVpcDomainStatusEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcDomainIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcDomainStatusEntry.setStatus("current")
_EltexVpcDomainTotalVpcConfigured_Type = Unsigned32
_EltexVpcDomainTotalVpcConfigured_Object = MibTableColumn
eltexVpcDomainTotalVpcConfigured = _EltexVpcDomainTotalVpcConfigured_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 1),
    _EltexVpcDomainTotalVpcConfigured_Type()
)
eltexVpcDomainTotalVpcConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainTotalVpcConfigured.setStatus("current")
_EltexVpcDomainTotalVpcOperational_Type = Unsigned32
_EltexVpcDomainTotalVpcOperational_Object = MibTableColumn
eltexVpcDomainTotalVpcOperational = _EltexVpcDomainTotalVpcOperational_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 2),
    _EltexVpcDomainTotalVpcOperational_Type()
)
eltexVpcDomainTotalVpcOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainTotalVpcOperational.setStatus("current")


class _EltexVpcDomainSelfRole_Type(Integer32):
    """Custom type eltexVpcDomainSelfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_EltexVpcDomainSelfRole_Type.__name__ = "Integer32"
_EltexVpcDomainSelfRole_Object = MibTableColumn
eltexVpcDomainSelfRole = _EltexVpcDomainSelfRole_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 3),
    _EltexVpcDomainSelfRole_Type()
)
eltexVpcDomainSelfRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainSelfRole.setStatus("current")


class _EltexVpcDomainOperationMode_Type(Integer32):
    """Custom type eltexVpcDomainOperationMode based on Integer32"""
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


_EltexVpcDomainOperationMode_Type.__name__ = "Integer32"
_EltexVpcDomainOperationMode_Object = MibTableColumn
eltexVpcDomainOperationMode = _EltexVpcDomainOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 4),
    _EltexVpcDomainOperationMode_Type()
)
eltexVpcDomainOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainOperationMode.setStatus("current")


class _EltexVpcDomainState_Type(Integer32):
    """Custom type eltexVpcDomainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("listen", 2),
          ("ready", 3),
          ("primary", 4),
          ("secondary", 5))
    )


_EltexVpcDomainState_Type.__name__ = "Integer32"
_EltexVpcDomainState_Object = MibTableColumn
eltexVpcDomainState = _EltexVpcDomainState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 5),
    _EltexVpcDomainState_Type()
)
eltexVpcDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainState.setStatus("current")


class _EltexVpcDomainOperationalSystemPriority_Type(Unsigned32):
    """Custom type eltexVpcDomainOperationalSystemPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EltexVpcDomainOperationalSystemPriority_Type.__name__ = "Unsigned32"
_EltexVpcDomainOperationalSystemPriority_Object = MibTableColumn
eltexVpcDomainOperationalSystemPriority = _EltexVpcDomainOperationalSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 6),
    _EltexVpcDomainOperationalSystemPriority_Type()
)
eltexVpcDomainOperationalSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainOperationalSystemPriority.setStatus("current")
_EltexVpcDomainOperationalMac_Type = MacAddress
_EltexVpcDomainOperationalMac_Object = MibTableColumn
eltexVpcDomainOperationalMac = _EltexVpcDomainOperationalMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 7),
    _EltexVpcDomainOperationalMac_Type()
)
eltexVpcDomainOperationalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainOperationalMac.setStatus("current")
_EltexVpcDomainLocalSystemMac_Type = MacAddress
_EltexVpcDomainLocalSystemMac_Object = MibTableColumn
eltexVpcDomainLocalSystemMac = _EltexVpcDomainLocalSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 8),
    _EltexVpcDomainLocalSystemMac_Type()
)
eltexVpcDomainLocalSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainLocalSystemMac.setStatus("current")


class _EltexVpcDomainPeerRole_Type(Integer32):
    """Custom type eltexVpcDomainPeerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_EltexVpcDomainPeerRole_Type.__name__ = "Integer32"
_EltexVpcDomainPeerRole_Object = MibTableColumn
eltexVpcDomainPeerRole = _EltexVpcDomainPeerRole_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 9),
    _EltexVpcDomainPeerRole_Type()
)
eltexVpcDomainPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerRole.setStatus("current")
_EltexVpcDomainPeerRolePriority_Type = Unsigned32
_EltexVpcDomainPeerRolePriority_Object = MibTableColumn
eltexVpcDomainPeerRolePriority = _EltexVpcDomainPeerRolePriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 10),
    _EltexVpcDomainPeerRolePriority_Type()
)
eltexVpcDomainPeerRolePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerRolePriority.setStatus("current")
_EltexVpcDomainPeerConfSystemPriority_Type = Unsigned32
_EltexVpcDomainPeerConfSystemPriority_Object = MibTableColumn
eltexVpcDomainPeerConfSystemPriority = _EltexVpcDomainPeerConfSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 11),
    _EltexVpcDomainPeerConfSystemPriority_Type()
)
eltexVpcDomainPeerConfSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerConfSystemPriority.setStatus("current")
_EltexVpcDomainPeerOperSystemPriority_Type = Unsigned32
_EltexVpcDomainPeerOperSystemPriority_Object = MibTableColumn
eltexVpcDomainPeerOperSystemPriority = _EltexVpcDomainPeerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 12),
    _EltexVpcDomainPeerOperSystemPriority_Type()
)
eltexVpcDomainPeerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerOperSystemPriority.setStatus("current")
_EltexVpcDomainPeerConfMac_Type = MacAddress
_EltexVpcDomainPeerConfMac_Object = MibTableColumn
eltexVpcDomainPeerConfMac = _EltexVpcDomainPeerConfMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 13),
    _EltexVpcDomainPeerConfMac_Type()
)
eltexVpcDomainPeerConfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerConfMac.setStatus("current")
_EltexVpcDomainPeerOperMac_Type = MacAddress
_EltexVpcDomainPeerOperMac_Object = MibTableColumn
eltexVpcDomainPeerOperMac = _EltexVpcDomainPeerOperMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 14),
    _EltexVpcDomainPeerOperMac_Type()
)
eltexVpcDomainPeerOperMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerOperMac.setStatus("current")
_EltexVpcDomainPeerLocalSystemMac_Type = MacAddress
_EltexVpcDomainPeerLocalSystemMac_Object = MibTableColumn
eltexVpcDomainPeerLocalSystemMac = _EltexVpcDomainPeerLocalSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 15),
    _EltexVpcDomainPeerLocalSystemMac_Type()
)
eltexVpcDomainPeerLocalSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLocalSystemMac.setStatus("current")
_EltexVpcDomainPeerKeepaliveDetected_Type = TruthValue
_EltexVpcDomainPeerKeepaliveDetected_Object = MibTableColumn
eltexVpcDomainPeerKeepaliveDetected = _EltexVpcDomainPeerKeepaliveDetected_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 16),
    _EltexVpcDomainPeerKeepaliveDetected_Type()
)
eltexVpcDomainPeerKeepaliveDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepaliveDetected.setStatus("current")
_EltexVpcDomainPeerDetectionStatus_Type = TruthValue
_EltexVpcDomainPeerDetectionStatus_Object = MibTableColumn
eltexVpcDomainPeerDetectionStatus = _EltexVpcDomainPeerDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 17),
    _EltexVpcDomainPeerDetectionStatus_Type()
)
eltexVpcDomainPeerDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionStatus.setStatus("current")
_EltexVpcDomainPeerDetectionDetected_Type = TruthValue
_EltexVpcDomainPeerDetectionDetected_Object = MibTableColumn
eltexVpcDomainPeerDetectionDetected = _EltexVpcDomainPeerDetectionDetected_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 1, 1, 18),
    _EltexVpcDomainPeerDetectionDetected_Type()
)
eltexVpcDomainPeerDetectionDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionDetected.setStatus("current")
_EltexVpcDomainPeerKeepAliveStatsTable_Object = MibTable
eltexVpcDomainPeerKeepAliveStatsTable = _EltexVpcDomainPeerKeepAliveStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2)
)
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveStatsTable.setStatus("current")
_EltexVpcDomainPeerKeepAliveStatsEntry_Object = MibTableRow
eltexVpcDomainPeerKeepAliveStatsEntry = _EltexVpcDomainPeerKeepAliveStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1)
)
eltexVpcDomainPeerKeepAliveStatsEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcDomainIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveStatsEntry.setStatus("current")


class _EltexVpcDomainKeepaliveOperationalMode_Type(Integer32):
    """Custom type eltexVpcDomainKeepaliveOperationalMode based on Integer32"""
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


_EltexVpcDomainKeepaliveOperationalMode_Type.__name__ = "Integer32"
_EltexVpcDomainKeepaliveOperationalMode_Object = MibTableColumn
eltexVpcDomainKeepaliveOperationalMode = _EltexVpcDomainKeepaliveOperationalMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 1),
    _EltexVpcDomainKeepaliveOperationalMode_Type()
)
eltexVpcDomainKeepaliveOperationalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainKeepaliveOperationalMode.setStatus("current")
_EltexVpcDomainPeerKeepAliveTotalTx_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveTotalTx_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveTotalTx = _EltexVpcDomainPeerKeepAliveTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 2),
    _EltexVpcDomainPeerKeepAliveTotalTx_Type()
)
eltexVpcDomainPeerKeepAliveTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveTotalTx.setStatus("current")
_EltexVpcDomainPeerKeepAliveSuccessTx_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveSuccessTx_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveSuccessTx = _EltexVpcDomainPeerKeepAliveSuccessTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 3),
    _EltexVpcDomainPeerKeepAliveSuccessTx_Type()
)
eltexVpcDomainPeerKeepAliveSuccessTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveSuccessTx.setStatus("current")
_EltexVpcDomainPeerKeepAliveTxErrors_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveTxErrors_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveTxErrors = _EltexVpcDomainPeerKeepAliveTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 4),
    _EltexVpcDomainPeerKeepAliveTxErrors_Type()
)
eltexVpcDomainPeerKeepAliveTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveTxErrors.setStatus("current")
_EltexVpcDomainPeerKeepAliveTotalRx_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveTotalRx_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveTotalRx = _EltexVpcDomainPeerKeepAliveTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 5),
    _EltexVpcDomainPeerKeepAliveTotalRx_Type()
)
eltexVpcDomainPeerKeepAliveTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveTotalRx.setStatus("current")
_EltexVpcDomainPeerKeepAliveSuccessRx_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveSuccessRx_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveSuccessRx = _EltexVpcDomainPeerKeepAliveSuccessRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 6),
    _EltexVpcDomainPeerKeepAliveSuccessRx_Type()
)
eltexVpcDomainPeerKeepAliveSuccessRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveSuccessRx.setStatus("current")
_EltexVpcDomainPeerKeepAliveRxErrors_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveRxErrors_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveRxErrors = _EltexVpcDomainPeerKeepAliveRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 7),
    _EltexVpcDomainPeerKeepAliveRxErrors_Type()
)
eltexVpcDomainPeerKeepAliveRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveRxErrors.setStatus("current")
_EltexVpcDomainPeerKeepAliveTimeoutCount_Type = Unsigned32
_EltexVpcDomainPeerKeepAliveTimeoutCount_Object = MibTableColumn
eltexVpcDomainPeerKeepAliveTimeoutCount = _EltexVpcDomainPeerKeepAliveTimeoutCount_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 2, 1, 8),
    _EltexVpcDomainPeerKeepAliveTimeoutCount_Type()
)
eltexVpcDomainPeerKeepAliveTimeoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerKeepAliveTimeoutCount.setStatus("current")
_EltexVpcDomainPeerLinkStatsTable_Object = MibTable
eltexVpcDomainPeerLinkStatsTable = _EltexVpcDomainPeerLinkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3)
)
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkStatsTable.setStatus("current")
_EltexVpcDomainLinkStatsEntry_Object = MibTableRow
eltexVpcDomainLinkStatsEntry = _EltexVpcDomainLinkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1)
)
eltexVpcDomainLinkStatsEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcDomainIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcDomainLinkStatsEntry.setStatus("current")
_EltexVpcDomainPeerLinkStatus_Type = TruthValue
_EltexVpcDomainPeerLinkStatus_Object = MibTableColumn
eltexVpcDomainPeerLinkStatus = _EltexVpcDomainPeerLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 2),
    _EltexVpcDomainPeerLinkStatus_Type()
)
eltexVpcDomainPeerLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkStatus.setStatus("current")
_EltexVpcDomainPeerLinkControlMsgTx_Type = Unsigned32
_EltexVpcDomainPeerLinkControlMsgTx_Object = MibTableColumn
eltexVpcDomainPeerLinkControlMsgTx = _EltexVpcDomainPeerLinkControlMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 3),
    _EltexVpcDomainPeerLinkControlMsgTx_Type()
)
eltexVpcDomainPeerLinkControlMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkControlMsgTx.setStatus("current")
_EltexVpcDomainPeerLinkTxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkTxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkTxErrors = _EltexVpcDomainPeerLinkTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 4),
    _EltexVpcDomainPeerLinkTxErrors_Type()
)
eltexVpcDomainPeerLinkTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkTxErrors.setStatus("current")
_EltexVpcDomainPeerLinkTxTimeout_Type = Unsigned32
_EltexVpcDomainPeerLinkTxTimeout_Object = MibTableColumn
eltexVpcDomainPeerLinkTxTimeout = _EltexVpcDomainPeerLinkTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 5),
    _EltexVpcDomainPeerLinkTxTimeout_Type()
)
eltexVpcDomainPeerLinkTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkTxTimeout.setStatus("current")
_EltexVpcDomainPeerLinkControlMsgAckTx_Type = Unsigned32
_EltexVpcDomainPeerLinkControlMsgAckTx_Object = MibTableColumn
eltexVpcDomainPeerLinkControlMsgAckTx = _EltexVpcDomainPeerLinkControlMsgAckTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 6),
    _EltexVpcDomainPeerLinkControlMsgAckTx_Type()
)
eltexVpcDomainPeerLinkControlMsgAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkControlMsgAckTx.setStatus("current")
_EltexVpcDomainPeerLinkControlMsgAckErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkControlMsgAckErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkControlMsgAckErrors = _EltexVpcDomainPeerLinkControlMsgAckErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 7),
    _EltexVpcDomainPeerLinkControlMsgAckErrors_Type()
)
eltexVpcDomainPeerLinkControlMsgAckErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkControlMsgAckErrors.setStatus("current")
_EltexVpcDomainPeerLinkControlMsgRx_Type = Unsigned32
_EltexVpcDomainPeerLinkControlMsgRx_Object = MibTableColumn
eltexVpcDomainPeerLinkControlMsgRx = _EltexVpcDomainPeerLinkControlMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 8),
    _EltexVpcDomainPeerLinkControlMsgRx_Type()
)
eltexVpcDomainPeerLinkControlMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkControlMsgRx.setStatus("current")
_EltexVpcDomainPeerLinkDataMsgTx_Type = Unsigned32
_EltexVpcDomainPeerLinkDataMsgTx_Object = MibTableColumn
eltexVpcDomainPeerLinkDataMsgTx = _EltexVpcDomainPeerLinkDataMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 9),
    _EltexVpcDomainPeerLinkDataMsgTx_Type()
)
eltexVpcDomainPeerLinkDataMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkDataMsgTx.setStatus("current")
_EltexVpcDomainPeerLinkDataMsgTxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkDataMsgTxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkDataMsgTxErrors = _EltexVpcDomainPeerLinkDataMsgTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 10),
    _EltexVpcDomainPeerLinkDataMsgTxErrors_Type()
)
eltexVpcDomainPeerLinkDataMsgTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkDataMsgTxErrors.setStatus("current")
_EltexVpcDomainPeerLinkDataMsgTxTimeout_Type = Unsigned32
_EltexVpcDomainPeerLinkDataMsgTxTimeout_Object = MibTableColumn
eltexVpcDomainPeerLinkDataMsgTxTimeout = _EltexVpcDomainPeerLinkDataMsgTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 11),
    _EltexVpcDomainPeerLinkDataMsgTxTimeout_Type()
)
eltexVpcDomainPeerLinkDataMsgTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkDataMsgTxTimeout.setStatus("current")
_EltexVpcDomainPeerLinkDataMsgRx_Type = Unsigned32
_EltexVpcDomainPeerLinkDataMsgRx_Object = MibTableColumn
eltexVpcDomainPeerLinkDataMsgRx = _EltexVpcDomainPeerLinkDataMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 12),
    _EltexVpcDomainPeerLinkDataMsgRx_Type()
)
eltexVpcDomainPeerLinkDataMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkDataMsgRx.setStatus("current")
_EltexVpcDomainPeerLinkBPDUTx_Type = Unsigned32
_EltexVpcDomainPeerLinkBPDUTx_Object = MibTableColumn
eltexVpcDomainPeerLinkBPDUTx = _EltexVpcDomainPeerLinkBPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 13),
    _EltexVpcDomainPeerLinkBPDUTx_Type()
)
eltexVpcDomainPeerLinkBPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBPDUTx.setStatus("current")
_EltexVpcDomainPeerLinkBPDUTxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkBPDUTxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkBPDUTxErrors = _EltexVpcDomainPeerLinkBPDUTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 14),
    _EltexVpcDomainPeerLinkBPDUTxErrors_Type()
)
eltexVpcDomainPeerLinkBPDUTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBPDUTxErrors.setStatus("current")
_EltexVpcDomainPeerLinkBPDURx_Type = Unsigned32
_EltexVpcDomainPeerLinkBPDURx_Object = MibTableColumn
eltexVpcDomainPeerLinkBPDURx = _EltexVpcDomainPeerLinkBPDURx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 15),
    _EltexVpcDomainPeerLinkBPDURx_Type()
)
eltexVpcDomainPeerLinkBPDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBPDURx.setStatus("current")
_EltexVpcDomainPeerLinkBPDURxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkBPDURxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkBPDURxErrors = _EltexVpcDomainPeerLinkBPDURxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 16),
    _EltexVpcDomainPeerLinkBPDURxErrors_Type()
)
eltexVpcDomainPeerLinkBPDURxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBPDURxErrors.setStatus("current")
_EltexVpcDomainPeerLinkLACPDUTx_Type = Unsigned32
_EltexVpcDomainPeerLinkLACPDUTx_Object = MibTableColumn
eltexVpcDomainPeerLinkLACPDUTx = _EltexVpcDomainPeerLinkLACPDUTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 17),
    _EltexVpcDomainPeerLinkLACPDUTx_Type()
)
eltexVpcDomainPeerLinkLACPDUTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkLACPDUTx.setStatus("current")
_EltexVpcDomainPeerLinkLACPDUTxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkLACPDUTxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkLACPDUTxErrors = _EltexVpcDomainPeerLinkLACPDUTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 18),
    _EltexVpcDomainPeerLinkLACPDUTxErrors_Type()
)
eltexVpcDomainPeerLinkLACPDUTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkLACPDUTxErrors.setStatus("current")
_EltexVpcDomainPeerLinkLACPDURx_Type = Unsigned32
_EltexVpcDomainPeerLinkLACPDURx_Object = MibTableColumn
eltexVpcDomainPeerLinkLACPDURx = _EltexVpcDomainPeerLinkLACPDURx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 19),
    _EltexVpcDomainPeerLinkLACPDURx_Type()
)
eltexVpcDomainPeerLinkLACPDURx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkLACPDURx.setStatus("current")
_EltexVpcDomainPeerLinkLACPDURxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkLACPDURxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkLACPDURxErrors = _EltexVpcDomainPeerLinkLACPDURxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 20),
    _EltexVpcDomainPeerLinkLACPDURxErrors_Type()
)
eltexVpcDomainPeerLinkLACPDURxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkLACPDURxErrors.setStatus("current")
_EltexVpcDomainPeerLinkBulkTx_Type = Unsigned32
_EltexVpcDomainPeerLinkBulkTx_Object = MibTableColumn
eltexVpcDomainPeerLinkBulkTx = _EltexVpcDomainPeerLinkBulkTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 21),
    _EltexVpcDomainPeerLinkBulkTx_Type()
)
eltexVpcDomainPeerLinkBulkTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBulkTx.setStatus("current")
_EltexVpcDomainPeerLinkBulkTxTimeout_Type = Unsigned32
_EltexVpcDomainPeerLinkBulkTxTimeout_Object = MibTableColumn
eltexVpcDomainPeerLinkBulkTxTimeout = _EltexVpcDomainPeerLinkBulkTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 22),
    _EltexVpcDomainPeerLinkBulkTxTimeout_Type()
)
eltexVpcDomainPeerLinkBulkTxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBulkTxTimeout.setStatus("current")
_EltexVpcDomainPeerLinkBulkTxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkBulkTxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkBulkTxErrors = _EltexVpcDomainPeerLinkBulkTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 23),
    _EltexVpcDomainPeerLinkBulkTxErrors_Type()
)
eltexVpcDomainPeerLinkBulkTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBulkTxErrors.setStatus("current")
_EltexVpcDomainPeerLinkBulkRx_Type = Unsigned32
_EltexVpcDomainPeerLinkBulkRx_Object = MibTableColumn
eltexVpcDomainPeerLinkBulkRx = _EltexVpcDomainPeerLinkBulkRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 24),
    _EltexVpcDomainPeerLinkBulkRx_Type()
)
eltexVpcDomainPeerLinkBulkRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBulkRx.setStatus("current")
_EltexVpcDomainPeerLinkBulkRxErrors_Type = Unsigned32
_EltexVpcDomainPeerLinkBulkRxErrors_Object = MibTableColumn
eltexVpcDomainPeerLinkBulkRxErrors = _EltexVpcDomainPeerLinkBulkRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 3, 1, 25),
    _EltexVpcDomainPeerLinkBulkRxErrors_Type()
)
eltexVpcDomainPeerLinkBulkRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerLinkBulkRxErrors.setStatus("current")
_EltexVpcDomainPeerDetectionStatsTable_Object = MibTable
eltexVpcDomainPeerDetectionStatsTable = _EltexVpcDomainPeerDetectionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4)
)
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionStatsTable.setStatus("current")
_EltexVpcDomainPeerDetectionStatsEntry_Object = MibTableRow
eltexVpcDomainPeerDetectionStatsEntry = _EltexVpcDomainPeerDetectionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1)
)
eltexVpcDomainPeerDetectionStatsEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcDomainIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionStatsEntry.setStatus("current")
_EltexVpcDomainPeerDetectionEnabled_Type = Unsigned32
_EltexVpcDomainPeerDetectionEnabled_Object = MibTableColumn
eltexVpcDomainPeerDetectionEnabled = _EltexVpcDomainPeerDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 2),
    _EltexVpcDomainPeerDetectionEnabled_Type()
)
eltexVpcDomainPeerDetectionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionEnabled.setStatus("current")
_EltexVpcDomainPeerDetectionEnableFailure_Type = Unsigned32
_EltexVpcDomainPeerDetectionEnableFailure_Object = MibTableColumn
eltexVpcDomainPeerDetectionEnableFailure = _EltexVpcDomainPeerDetectionEnableFailure_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 3),
    _EltexVpcDomainPeerDetectionEnableFailure_Type()
)
eltexVpcDomainPeerDetectionEnableFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionEnableFailure.setStatus("current")
_EltexVpcDomainPeerDetectionDisabled_Type = Unsigned32
_EltexVpcDomainPeerDetectionDisabled_Object = MibTableColumn
eltexVpcDomainPeerDetectionDisabled = _EltexVpcDomainPeerDetectionDisabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 4),
    _EltexVpcDomainPeerDetectionDisabled_Type()
)
eltexVpcDomainPeerDetectionDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionDisabled.setStatus("current")
_EltexVpcDomainPeerDetectionPeerTimeout_Type = Unsigned32
_EltexVpcDomainPeerDetectionPeerTimeout_Object = MibTableColumn
eltexVpcDomainPeerDetectionPeerTimeout = _EltexVpcDomainPeerDetectionPeerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 5),
    _EltexVpcDomainPeerDetectionPeerTimeout_Type()
)
eltexVpcDomainPeerDetectionPeerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionPeerTimeout.setStatus("current")
_EltexVpcDomainPeerDetectionPeerAdminDisable_Type = Unsigned32
_EltexVpcDomainPeerDetectionPeerAdminDisable_Object = MibTableColumn
eltexVpcDomainPeerDetectionPeerAdminDisable = _EltexVpcDomainPeerDetectionPeerAdminDisable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 6),
    _EltexVpcDomainPeerDetectionPeerAdminDisable_Type()
)
eltexVpcDomainPeerDetectionPeerAdminDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionPeerAdminDisable.setStatus("current")
_EltexVpcDomainPeerDetectionTx_Type = Unsigned32
_EltexVpcDomainPeerDetectionTx_Object = MibTableColumn
eltexVpcDomainPeerDetectionTx = _EltexVpcDomainPeerDetectionTx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 7),
    _EltexVpcDomainPeerDetectionTx_Type()
)
eltexVpcDomainPeerDetectionTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionTx.setStatus("current")
_EltexVpcDomainPeerDetectionTxError_Type = Unsigned32
_EltexVpcDomainPeerDetectionTxError_Object = MibTableColumn
eltexVpcDomainPeerDetectionTxError = _EltexVpcDomainPeerDetectionTxError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 8),
    _EltexVpcDomainPeerDetectionTxError_Type()
)
eltexVpcDomainPeerDetectionTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionTxError.setStatus("current")
_EltexVpcDomainPeerDetectionTxFdMsg_Type = Unsigned32
_EltexVpcDomainPeerDetectionTxFdMsg_Object = MibTableColumn
eltexVpcDomainPeerDetectionTxFdMsg = _EltexVpcDomainPeerDetectionTxFdMsg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 9),
    _EltexVpcDomainPeerDetectionTxFdMsg_Type()
)
eltexVpcDomainPeerDetectionTxFdMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionTxFdMsg.setStatus("current")
_EltexVpcDomainPeerDetectionTxFdAckMsg_Type = Unsigned32
_EltexVpcDomainPeerDetectionTxFdAckMsg_Object = MibTableColumn
eltexVpcDomainPeerDetectionTxFdAckMsg = _EltexVpcDomainPeerDetectionTxFdAckMsg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 10),
    _EltexVpcDomainPeerDetectionTxFdAckMsg_Type()
)
eltexVpcDomainPeerDetectionTxFdAckMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionTxFdAckMsg.setStatus("current")
_EltexVpcDomainPeerDetectionRx_Type = Unsigned32
_EltexVpcDomainPeerDetectionRx_Object = MibTableColumn
eltexVpcDomainPeerDetectionRx = _EltexVpcDomainPeerDetectionRx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 11),
    _EltexVpcDomainPeerDetectionRx_Type()
)
eltexVpcDomainPeerDetectionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionRx.setStatus("current")
_EltexVpcDomainPeerDetectionRxError_Type = Unsigned32
_EltexVpcDomainPeerDetectionRxError_Object = MibTableColumn
eltexVpcDomainPeerDetectionRxError = _EltexVpcDomainPeerDetectionRxError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 12),
    _EltexVpcDomainPeerDetectionRxError_Type()
)
eltexVpcDomainPeerDetectionRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionRxError.setStatus("current")
_EltexVpcDomainPeerDetectionRxFdMsg_Type = Unsigned32
_EltexVpcDomainPeerDetectionRxFdMsg_Object = MibTableColumn
eltexVpcDomainPeerDetectionRxFdMsg = _EltexVpcDomainPeerDetectionRxFdMsg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 13),
    _EltexVpcDomainPeerDetectionRxFdMsg_Type()
)
eltexVpcDomainPeerDetectionRxFdMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionRxFdMsg.setStatus("current")
_EltexVpcDomainPeerDetectionRxFdAckMsg_Type = Unsigned32
_EltexVpcDomainPeerDetectionRxFdAckMsg_Object = MibTableColumn
eltexVpcDomainPeerDetectionRxFdAckMsg = _EltexVpcDomainPeerDetectionRxFdAckMsg_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 4, 1, 14),
    _EltexVpcDomainPeerDetectionRxFdAckMsg_Type()
)
eltexVpcDomainPeerDetectionRxFdAckMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcDomainPeerDetectionRxFdAckMsg.setStatus("current")
_EltexVpcMemberStatusTable_Object = MibTable
eltexVpcMemberStatusTable = _EltexVpcMemberStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 5)
)
if mibBuilder.loadTexts:
    eltexVpcMemberStatusTable.setStatus("current")
_EltexVpcMemberStatusEntry_Object = MibTableRow
eltexVpcMemberStatusEntry = _EltexVpcMemberStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 5, 1)
)
eltexVpcMemberStatusEntry.setIndexNames(
    (0, "ELTEX-VPC-MIB", "eltexVpcMemberStatusVpcGroupIndex"),
    (0, "ELTEX-VPC-MIB", "eltexVpcMemberStatusIfIndex"),
)
if mibBuilder.loadTexts:
    eltexVpcMemberStatusEntry.setStatus("current")


class _EltexVpcMemberStatusVpcGroupIndex_Type(Unsigned32):
    """Custom type eltexVpcMemberStatusVpcGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_EltexVpcMemberStatusVpcGroupIndex_Type.__name__ = "Unsigned32"
_EltexVpcMemberStatusVpcGroupIndex_Object = MibTableColumn
eltexVpcMemberStatusVpcGroupIndex = _EltexVpcMemberStatusVpcGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 5, 1, 1),
    _EltexVpcMemberStatusVpcGroupIndex_Type()
)
eltexVpcMemberStatusVpcGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcMemberStatusVpcGroupIndex.setStatus("current")
_EltexVpcMemberStatusIfIndex_Type = InterfaceIndexOrZero
_EltexVpcMemberStatusIfIndex_Object = MibTableColumn
eltexVpcMemberStatusIfIndex = _EltexVpcMemberStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 5, 1, 2),
    _EltexVpcMemberStatusIfIndex_Type()
)
eltexVpcMemberStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcMemberStatusIfIndex.setStatus("current")


class _EltexVpcSelfMemberStatusIntfState_Type(Integer32):
    """Custom type eltexVpcSelfMemberStatusIntfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notpresent", 3))
    )


_EltexVpcSelfMemberStatusIntfState_Type.__name__ = "Integer32"
_EltexVpcSelfMemberStatusIntfState_Object = MibTableColumn
eltexVpcSelfMemberStatusIntfState = _EltexVpcSelfMemberStatusIntfState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 5, 1, 3),
    _EltexVpcSelfMemberStatusIntfState_Type()
)
eltexVpcSelfMemberStatusIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcSelfMemberStatusIntfState.setStatus("current")


class _EltexVpcPeerMemberStatusIntfState_Type(Integer32):
    """Custom type eltexVpcPeerMemberStatusIntfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("notpresent", 3))
    )


_EltexVpcPeerMemberStatusIntfState_Type.__name__ = "Integer32"
_EltexVpcPeerMemberStatusIntfState_Object = MibTableColumn
eltexVpcPeerMemberStatusIntfState = _EltexVpcPeerMemberStatusIntfState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 125, 1, 2, 5, 1, 4),
    _EltexVpcPeerMemberStatusIntfState_Type()
)
eltexVpcPeerMemberStatusIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltexVpcPeerMemberStatusIntfState.setStatus("current")
_EltexVpcMIBNotification_ObjectIdentity = ObjectIdentity
eltexVpcMIBNotification = _EltexVpcMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 125, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-VPC-MIB",
    **{"eltexVpcMIB": eltexVpcMIB,
       "eltexVpcMIBObjects": eltexVpcMIBObjects,
       "eltexVpcConfigGroup": eltexVpcConfigGroup,
       "eltexVpcMode": eltexVpcMode,
       "eltexVpcDomainConfigTable": eltexVpcDomainConfigTable,
       "eltexVpcDomainConfigEntry": eltexVpcDomainConfigEntry,
       "eltexVpcDomainIndex": eltexVpcDomainIndex,
       "eltexVpcDomainPeerLink": eltexVpcDomainPeerLink,
       "eltexVpcDomainKeepalivePriority": eltexVpcDomainKeepalivePriority,
       "eltexVpcDomainKeepaliveTimeout": eltexVpcDomainKeepaliveTimeout,
       "eltexVpcDomainKeepaliveMode": eltexVpcDomainKeepaliveMode,
       "eltexVpcDomainSystemMac": eltexVpcDomainSystemMac,
       "eltexVpcDomainSystemPriority": eltexVpcDomainSystemPriority,
       "eltexVpcDomainPeerDetectionMode": eltexVpcDomainPeerDetectionMode,
       "eltexVpcDomainPeerDetectionInterval": eltexVpcDomainPeerDetectionInterval,
       "eltexVpcDomainPeerDetectionTimeout": eltexVpcDomainPeerDetectionTimeout,
       "eltexVpcDomainPeerIpAddr": eltexVpcDomainPeerIpAddr,
       "eltexVpcDomainSourceIpAddr": eltexVpcDomainSourceIpAddr,
       "eltexVpcDomainDcpdpUdpPort": eltexVpcDomainDcpdpUdpPort,
       "eltexVpcDomainStatus": eltexVpcDomainStatus,
       "eltexVpcGroupConfigTable": eltexVpcGroupConfigTable,
       "eltexVpcGroupConfigEntry": eltexVpcGroupConfigEntry,
       "eltexVpcGroupIndex": eltexVpcGroupIndex,
       "eltexVpcGroupDomainIndex": eltexVpcGroupDomainIndex,
       "eltexVpcGroupPortChannelIfIndex": eltexVpcGroupPortChannelIfIndex,
       "eltexVpcGroupOperationalStatus": eltexVpcGroupOperationalStatus,
       "eltexVpcGroupInterfaceState": eltexVpcGroupInterfaceState,
       "eltexVpcGroupStatus": eltexVpcGroupStatus,
       "eltexVpcStatusGroup": eltexVpcStatusGroup,
       "eltexVpcDomainStatusTable": eltexVpcDomainStatusTable,
       "eltexVpcDomainStatusEntry": eltexVpcDomainStatusEntry,
       "eltexVpcDomainTotalVpcConfigured": eltexVpcDomainTotalVpcConfigured,
       "eltexVpcDomainTotalVpcOperational": eltexVpcDomainTotalVpcOperational,
       "eltexVpcDomainSelfRole": eltexVpcDomainSelfRole,
       "eltexVpcDomainOperationMode": eltexVpcDomainOperationMode,
       "eltexVpcDomainState": eltexVpcDomainState,
       "eltexVpcDomainOperationalSystemPriority": eltexVpcDomainOperationalSystemPriority,
       "eltexVpcDomainOperationalMac": eltexVpcDomainOperationalMac,
       "eltexVpcDomainLocalSystemMac": eltexVpcDomainLocalSystemMac,
       "eltexVpcDomainPeerRole": eltexVpcDomainPeerRole,
       "eltexVpcDomainPeerRolePriority": eltexVpcDomainPeerRolePriority,
       "eltexVpcDomainPeerConfSystemPriority": eltexVpcDomainPeerConfSystemPriority,
       "eltexVpcDomainPeerOperSystemPriority": eltexVpcDomainPeerOperSystemPriority,
       "eltexVpcDomainPeerConfMac": eltexVpcDomainPeerConfMac,
       "eltexVpcDomainPeerOperMac": eltexVpcDomainPeerOperMac,
       "eltexVpcDomainPeerLocalSystemMac": eltexVpcDomainPeerLocalSystemMac,
       "eltexVpcDomainPeerKeepaliveDetected": eltexVpcDomainPeerKeepaliveDetected,
       "eltexVpcDomainPeerDetectionStatus": eltexVpcDomainPeerDetectionStatus,
       "eltexVpcDomainPeerDetectionDetected": eltexVpcDomainPeerDetectionDetected,
       "eltexVpcDomainPeerKeepAliveStatsTable": eltexVpcDomainPeerKeepAliveStatsTable,
       "eltexVpcDomainPeerKeepAliveStatsEntry": eltexVpcDomainPeerKeepAliveStatsEntry,
       "eltexVpcDomainKeepaliveOperationalMode": eltexVpcDomainKeepaliveOperationalMode,
       "eltexVpcDomainPeerKeepAliveTotalTx": eltexVpcDomainPeerKeepAliveTotalTx,
       "eltexVpcDomainPeerKeepAliveSuccessTx": eltexVpcDomainPeerKeepAliveSuccessTx,
       "eltexVpcDomainPeerKeepAliveTxErrors": eltexVpcDomainPeerKeepAliveTxErrors,
       "eltexVpcDomainPeerKeepAliveTotalRx": eltexVpcDomainPeerKeepAliveTotalRx,
       "eltexVpcDomainPeerKeepAliveSuccessRx": eltexVpcDomainPeerKeepAliveSuccessRx,
       "eltexVpcDomainPeerKeepAliveRxErrors": eltexVpcDomainPeerKeepAliveRxErrors,
       "eltexVpcDomainPeerKeepAliveTimeoutCount": eltexVpcDomainPeerKeepAliveTimeoutCount,
       "eltexVpcDomainPeerLinkStatsTable": eltexVpcDomainPeerLinkStatsTable,
       "eltexVpcDomainLinkStatsEntry": eltexVpcDomainLinkStatsEntry,
       "eltexVpcDomainPeerLinkStatus": eltexVpcDomainPeerLinkStatus,
       "eltexVpcDomainPeerLinkControlMsgTx": eltexVpcDomainPeerLinkControlMsgTx,
       "eltexVpcDomainPeerLinkTxErrors": eltexVpcDomainPeerLinkTxErrors,
       "eltexVpcDomainPeerLinkTxTimeout": eltexVpcDomainPeerLinkTxTimeout,
       "eltexVpcDomainPeerLinkControlMsgAckTx": eltexVpcDomainPeerLinkControlMsgAckTx,
       "eltexVpcDomainPeerLinkControlMsgAckErrors": eltexVpcDomainPeerLinkControlMsgAckErrors,
       "eltexVpcDomainPeerLinkControlMsgRx": eltexVpcDomainPeerLinkControlMsgRx,
       "eltexVpcDomainPeerLinkDataMsgTx": eltexVpcDomainPeerLinkDataMsgTx,
       "eltexVpcDomainPeerLinkDataMsgTxErrors": eltexVpcDomainPeerLinkDataMsgTxErrors,
       "eltexVpcDomainPeerLinkDataMsgTxTimeout": eltexVpcDomainPeerLinkDataMsgTxTimeout,
       "eltexVpcDomainPeerLinkDataMsgRx": eltexVpcDomainPeerLinkDataMsgRx,
       "eltexVpcDomainPeerLinkBPDUTx": eltexVpcDomainPeerLinkBPDUTx,
       "eltexVpcDomainPeerLinkBPDUTxErrors": eltexVpcDomainPeerLinkBPDUTxErrors,
       "eltexVpcDomainPeerLinkBPDURx": eltexVpcDomainPeerLinkBPDURx,
       "eltexVpcDomainPeerLinkBPDURxErrors": eltexVpcDomainPeerLinkBPDURxErrors,
       "eltexVpcDomainPeerLinkLACPDUTx": eltexVpcDomainPeerLinkLACPDUTx,
       "eltexVpcDomainPeerLinkLACPDUTxErrors": eltexVpcDomainPeerLinkLACPDUTxErrors,
       "eltexVpcDomainPeerLinkLACPDURx": eltexVpcDomainPeerLinkLACPDURx,
       "eltexVpcDomainPeerLinkLACPDURxErrors": eltexVpcDomainPeerLinkLACPDURxErrors,
       "eltexVpcDomainPeerLinkBulkTx": eltexVpcDomainPeerLinkBulkTx,
       "eltexVpcDomainPeerLinkBulkTxTimeout": eltexVpcDomainPeerLinkBulkTxTimeout,
       "eltexVpcDomainPeerLinkBulkTxErrors": eltexVpcDomainPeerLinkBulkTxErrors,
       "eltexVpcDomainPeerLinkBulkRx": eltexVpcDomainPeerLinkBulkRx,
       "eltexVpcDomainPeerLinkBulkRxErrors": eltexVpcDomainPeerLinkBulkRxErrors,
       "eltexVpcDomainPeerDetectionStatsTable": eltexVpcDomainPeerDetectionStatsTable,
       "eltexVpcDomainPeerDetectionStatsEntry": eltexVpcDomainPeerDetectionStatsEntry,
       "eltexVpcDomainPeerDetectionEnabled": eltexVpcDomainPeerDetectionEnabled,
       "eltexVpcDomainPeerDetectionEnableFailure": eltexVpcDomainPeerDetectionEnableFailure,
       "eltexVpcDomainPeerDetectionDisabled": eltexVpcDomainPeerDetectionDisabled,
       "eltexVpcDomainPeerDetectionPeerTimeout": eltexVpcDomainPeerDetectionPeerTimeout,
       "eltexVpcDomainPeerDetectionPeerAdminDisable": eltexVpcDomainPeerDetectionPeerAdminDisable,
       "eltexVpcDomainPeerDetectionTx": eltexVpcDomainPeerDetectionTx,
       "eltexVpcDomainPeerDetectionTxError": eltexVpcDomainPeerDetectionTxError,
       "eltexVpcDomainPeerDetectionTxFdMsg": eltexVpcDomainPeerDetectionTxFdMsg,
       "eltexVpcDomainPeerDetectionTxFdAckMsg": eltexVpcDomainPeerDetectionTxFdAckMsg,
       "eltexVpcDomainPeerDetectionRx": eltexVpcDomainPeerDetectionRx,
       "eltexVpcDomainPeerDetectionRxError": eltexVpcDomainPeerDetectionRxError,
       "eltexVpcDomainPeerDetectionRxFdMsg": eltexVpcDomainPeerDetectionRxFdMsg,
       "eltexVpcDomainPeerDetectionRxFdAckMsg": eltexVpcDomainPeerDetectionRxFdAckMsg,
       "eltexVpcMemberStatusTable": eltexVpcMemberStatusTable,
       "eltexVpcMemberStatusEntry": eltexVpcMemberStatusEntry,
       "eltexVpcMemberStatusVpcGroupIndex": eltexVpcMemberStatusVpcGroupIndex,
       "eltexVpcMemberStatusIfIndex": eltexVpcMemberStatusIfIndex,
       "eltexVpcSelfMemberStatusIntfState": eltexVpcSelfMemberStatusIntfState,
       "eltexVpcPeerMemberStatusIntfState": eltexVpcPeerMemberStatusIntfState,
       "eltexVpcMIBNotification": eltexVpcMIBNotification}
)
