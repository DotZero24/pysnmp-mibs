# SNMP MIB module (ALCATEL-ENT1-RIPNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-RIPNG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:30 2025
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

(routingIND1Ripng,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "routingIND1Ripng")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1RIPNGMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1RIPNGMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBObjects = _AlcatelIND1RIPNGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBObjects.setStatus("current")
_AlaProtocolRipng_ObjectIdentity = ObjectIdentity
alaProtocolRipng = _AlaProtocolRipng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1)
)


class _AlaRipngProtoStatus_Type(Integer32):
    """Custom type alaRipngProtoStatus based on Integer32"""
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


_AlaRipngProtoStatus_Type.__name__ = "Integer32"
_AlaRipngProtoStatus_Object = MibScalar
alaRipngProtoStatus = _AlaRipngProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 1),
    _AlaRipngProtoStatus_Type()
)
alaRipngProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngProtoStatus.setStatus("current")


class _AlaRipngUpdateInterval_Type(Integer32):
    """Custom type alaRipngUpdateInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaRipngUpdateInterval_Type.__name__ = "Integer32"
_AlaRipngUpdateInterval_Object = MibScalar
alaRipngUpdateInterval = _AlaRipngUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 2),
    _AlaRipngUpdateInterval_Type()
)
alaRipngUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaRipngUpdateInterval.setUnits("seconds")


class _AlaRipngInvalidTimer_Type(Integer32):
    """Custom type alaRipngInvalidTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 360),
    )


_AlaRipngInvalidTimer_Type.__name__ = "Integer32"
_AlaRipngInvalidTimer_Object = MibScalar
alaRipngInvalidTimer = _AlaRipngInvalidTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 3),
    _AlaRipngInvalidTimer_Type()
)
alaRipngInvalidTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngInvalidTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipngInvalidTimer.setUnits("seconds")


class _AlaRipngHolddownTimer_Type(Integer32):
    """Custom type alaRipngHolddownTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaRipngHolddownTimer_Type.__name__ = "Integer32"
_AlaRipngHolddownTimer_Object = MibScalar
alaRipngHolddownTimer = _AlaRipngHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 4),
    _AlaRipngHolddownTimer_Type()
)
alaRipngHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngHolddownTimer.setStatus("current")


class _AlaRipngGarbageTimer_Type(Integer32):
    """Custom type alaRipngGarbageTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_AlaRipngGarbageTimer_Type.__name__ = "Integer32"
_AlaRipngGarbageTimer_Object = MibScalar
alaRipngGarbageTimer = _AlaRipngGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 5),
    _AlaRipngGarbageTimer_Type()
)
alaRipngGarbageTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngGarbageTimer.setStatus("current")


class _AlaRipngRouteCount_Type(Integer32):
    """Custom type alaRipngRouteCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipngRouteCount_Type.__name__ = "Integer32"
_AlaRipngRouteCount_Object = MibScalar
alaRipngRouteCount = _AlaRipngRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 6),
    _AlaRipngRouteCount_Type()
)
alaRipngRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteCount.setStatus("current")


class _AlaRipngGlobalRouteTag_Type(Integer32):
    """Custom type alaRipngGlobalRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaRipngGlobalRouteTag_Type.__name__ = "Integer32"
_AlaRipngGlobalRouteTag_Object = MibScalar
alaRipngGlobalRouteTag = _AlaRipngGlobalRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 7),
    _AlaRipngGlobalRouteTag_Type()
)
alaRipngGlobalRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngGlobalRouteTag.setStatus("current")


class _AlaRipngTriggeredSends_Type(Integer32):
    """Custom type alaRipngTriggeredSends based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("onlyupdated", 2),
          ("off", 3))
    )


_AlaRipngTriggeredSends_Type.__name__ = "Integer32"
_AlaRipngTriggeredSends_Object = MibScalar
alaRipngTriggeredSends = _AlaRipngTriggeredSends_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 8),
    _AlaRipngTriggeredSends_Type()
)
alaRipngTriggeredSends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngTriggeredSends.setStatus("current")


class _AlaRipngJitter_Type(Integer32):
    """Custom type alaRipngJitter based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlaRipngJitter_Type.__name__ = "Integer32"
_AlaRipngJitter_Object = MibScalar
alaRipngJitter = _AlaRipngJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 9),
    _AlaRipngJitter_Type()
)
alaRipngJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngJitter.setStatus("current")
if mibBuilder.loadTexts:
    alaRipngJitter.setUnits("seconds")


class _AlaRipngPort_Type(Integer32):
    """Custom type alaRipngPort based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaRipngPort_Type.__name__ = "Integer32"
_AlaRipngPort_Object = MibScalar
alaRipngPort = _AlaRipngPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 10),
    _AlaRipngPort_Type()
)
alaRipngPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipngPort.setStatus("current")
_AlaRipngInterfaceTable_Object = MibTable
alaRipngInterfaceTable = _AlaRipngInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaRipngInterfaceTable.setStatus("current")
_AlaRipngInterfaceEntry_Object = MibTableRow
alaRipngInterfaceEntry = _AlaRipngInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1)
)
alaRipngInterfaceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceIndex"),
)
if mibBuilder.loadTexts:
    alaRipngInterfaceEntry.setStatus("current")


class _AlaRipngInterfaceIndex_Type(Integer32):
    """Custom type alaRipngInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaRipngInterfaceIndex_Type.__name__ = "Integer32"
_AlaRipngInterfaceIndex_Object = MibTableColumn
alaRipngInterfaceIndex = _AlaRipngInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 1),
    _AlaRipngInterfaceIndex_Type()
)
alaRipngInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngInterfaceIndex.setStatus("current")


class _AlaRipngInterfaceStatus_Type(RowStatus):
    """Custom type alaRipngInterfaceStatus based on RowStatus"""
    defaultValue = 2


_AlaRipngInterfaceStatus_Type.__name__ = "RowStatus"
_AlaRipngInterfaceStatus_Object = MibTableColumn
alaRipngInterfaceStatus = _AlaRipngInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 2),
    _AlaRipngInterfaceStatus_Type()
)
alaRipngInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRipngInterfaceStatus.setStatus("current")


class _AlaRipngInterfaceMetric_Type(Integer32):
    """Custom type alaRipngInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AlaRipngInterfaceMetric_Type.__name__ = "Integer32"
_AlaRipngInterfaceMetric_Object = MibTableColumn
alaRipngInterfaceMetric = _AlaRipngInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 3),
    _AlaRipngInterfaceMetric_Type()
)
alaRipngInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRipngInterfaceMetric.setStatus("current")


class _AlaRipngInterfaceRecvStatus_Type(Integer32):
    """Custom type alaRipngInterfaceRecvStatus based on Integer32"""
    defaultValue = 1

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


_AlaRipngInterfaceRecvStatus_Type.__name__ = "Integer32"
_AlaRipngInterfaceRecvStatus_Object = MibTableColumn
alaRipngInterfaceRecvStatus = _AlaRipngInterfaceRecvStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 4),
    _AlaRipngInterfaceRecvStatus_Type()
)
alaRipngInterfaceRecvStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRipngInterfaceRecvStatus.setStatus("current")


class _AlaRipngInterfaceSendStatus_Type(Integer32):
    """Custom type alaRipngInterfaceSendStatus based on Integer32"""
    defaultValue = 1

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


_AlaRipngInterfaceSendStatus_Type.__name__ = "Integer32"
_AlaRipngInterfaceSendStatus_Object = MibTableColumn
alaRipngInterfaceSendStatus = _AlaRipngInterfaceSendStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 5),
    _AlaRipngInterfaceSendStatus_Type()
)
alaRipngInterfaceSendStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRipngInterfaceSendStatus.setStatus("current")


class _AlaRipngInterfaceHorizon_Type(Integer32):
    """Custom type alaRipngInterfaceHorizon based on Integer32"""
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
        *(("none", 1),
          ("onlysplit", 2),
          ("poison", 3))
    )


_AlaRipngInterfaceHorizon_Type.__name__ = "Integer32"
_AlaRipngInterfaceHorizon_Object = MibTableColumn
alaRipngInterfaceHorizon = _AlaRipngInterfaceHorizon_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 6),
    _AlaRipngInterfaceHorizon_Type()
)
alaRipngInterfaceHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaRipngInterfaceHorizon.setStatus("current")
_AlaRipngInterfacePacketsSent_Type = Integer32
_AlaRipngInterfacePacketsSent_Object = MibTableColumn
alaRipngInterfacePacketsSent = _AlaRipngInterfacePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 7),
    _AlaRipngInterfacePacketsSent_Type()
)
alaRipngInterfacePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfacePacketsSent.setStatus("current")
_AlaRipngInterfacePacketsRcvd_Type = Integer32
_AlaRipngInterfacePacketsRcvd_Object = MibTableColumn
alaRipngInterfacePacketsRcvd = _AlaRipngInterfacePacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 8),
    _AlaRipngInterfacePacketsRcvd_Type()
)
alaRipngInterfacePacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfacePacketsRcvd.setStatus("current")
_AlaRipngInterfaceMTU_Type = Counter32
_AlaRipngInterfaceMTU_Object = MibTableColumn
alaRipngInterfaceMTU = _AlaRipngInterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 9),
    _AlaRipngInterfaceMTU_Type()
)
alaRipngInterfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfaceMTU.setStatus("current")
_AlaRipngInterfaceNextUpdate_Type = TimeTicks
_AlaRipngInterfaceNextUpdate_Object = MibTableColumn
alaRipngInterfaceNextUpdate = _AlaRipngInterfaceNextUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 11, 1, 10),
    _AlaRipngInterfaceNextUpdate_Type()
)
alaRipngInterfaceNextUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngInterfaceNextUpdate.setStatus("current")
_AlaRipngPeerTable_Object = MibTable
alaRipngPeerTable = _AlaRipngPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaRipngPeerTable.setStatus("current")
_AlaRipngPeerEntry_Object = MibTableRow
alaRipngPeerEntry = _AlaRipngPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1)
)
alaRipngPeerEntry.setIndexNames(
    (0, "ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerAddress"),
    (0, "ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerIndex"),
)
if mibBuilder.loadTexts:
    alaRipngPeerEntry.setStatus("current")
_AlaRipngPeerAddress_Type = Ipv6Address
_AlaRipngPeerAddress_Object = MibTableColumn
alaRipngPeerAddress = _AlaRipngPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 1),
    _AlaRipngPeerAddress_Type()
)
alaRipngPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngPeerAddress.setStatus("current")


class _AlaRipngPeerIndex_Type(Integer32):
    """Custom type alaRipngPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlaRipngPeerIndex_Type.__name__ = "Integer32"
_AlaRipngPeerIndex_Object = MibTableColumn
alaRipngPeerIndex = _AlaRipngPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 2),
    _AlaRipngPeerIndex_Type()
)
alaRipngPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngPeerIndex.setStatus("current")
_AlaRipngPeerLastUpdate_Type = TimeTicks
_AlaRipngPeerLastUpdate_Object = MibTableColumn
alaRipngPeerLastUpdate = _AlaRipngPeerLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 3),
    _AlaRipngPeerLastUpdate_Type()
)
alaRipngPeerLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerLastUpdate.setStatus("current")
_AlaRipngPeerNumUpdates_Type = Counter32
_AlaRipngPeerNumUpdates_Object = MibTableColumn
alaRipngPeerNumUpdates = _AlaRipngPeerNumUpdates_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 4),
    _AlaRipngPeerNumUpdates_Type()
)
alaRipngPeerNumUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerNumUpdates.setStatus("current")
_AlaRipngPeerNumRoutes_Type = Counter32
_AlaRipngPeerNumRoutes_Object = MibTableColumn
alaRipngPeerNumRoutes = _AlaRipngPeerNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 5),
    _AlaRipngPeerNumRoutes_Type()
)
alaRipngPeerNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerNumRoutes.setStatus("current")
_AlaRipngPeerBadPackets_Type = Counter32
_AlaRipngPeerBadPackets_Object = MibTableColumn
alaRipngPeerBadPackets = _AlaRipngPeerBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 6),
    _AlaRipngPeerBadPackets_Type()
)
alaRipngPeerBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerBadPackets.setStatus("current")
_AlaRipngPeerBadRoutes_Type = Counter32
_AlaRipngPeerBadRoutes_Object = MibTableColumn
alaRipngPeerBadRoutes = _AlaRipngPeerBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 15, 1, 7),
    _AlaRipngPeerBadRoutes_Type()
)
alaRipngPeerBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngPeerBadRoutes.setStatus("current")
_AlaRipngRouteTable_Object = MibTable
alaRipngRouteTable = _AlaRipngRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaRipngRouteTable.setStatus("current")
_AlaRipngRouteEntry_Object = MibTableRow
alaRipngRouteEntry = _AlaRipngRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1)
)
alaRipngRouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-RIPNG-MIB", "alaRipngRoutePrefix"),
    (0, "ALCATEL-ENT1-RIPNG-MIB", "alaRipngRoutePrefixLen"),
    (0, "ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaRipngRouteEntry.setStatus("current")
_AlaRipngRoutePrefix_Type = Ipv6AddressPrefix
_AlaRipngRoutePrefix_Object = MibTableColumn
alaRipngRoutePrefix = _AlaRipngRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 1),
    _AlaRipngRoutePrefix_Type()
)
alaRipngRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngRoutePrefix.setStatus("current")


class _AlaRipngRoutePrefixLen_Type(Integer32):
    """Custom type alaRipngRoutePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaRipngRoutePrefixLen_Type.__name__ = "Integer32"
_AlaRipngRoutePrefixLen_Object = MibTableColumn
alaRipngRoutePrefixLen = _AlaRipngRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 2),
    _AlaRipngRoutePrefixLen_Type()
)
alaRipngRoutePrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngRoutePrefixLen.setStatus("current")
_AlaRipngRouteNextHop_Type = Ipv6Address
_AlaRipngRouteNextHop_Object = MibTableColumn
alaRipngRouteNextHop = _AlaRipngRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 3),
    _AlaRipngRouteNextHop_Type()
)
alaRipngRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipngRouteNextHop.setStatus("current")


class _AlaRipngRouteType_Type(Integer32):
    """Custom type alaRipngRouteType based on Integer32"""
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
        *(("local", 1),
          ("rip", 2),
          ("redist", 3),
          ("unknown", 4))
    )


_AlaRipngRouteType_Type.__name__ = "Integer32"
_AlaRipngRouteType_Object = MibTableColumn
alaRipngRouteType = _AlaRipngRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 4),
    _AlaRipngRouteType_Type()
)
alaRipngRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteType.setStatus("current")
_AlaRipngRouteAge_Type = TimeTicks
_AlaRipngRouteAge_Object = MibTableColumn
alaRipngRouteAge = _AlaRipngRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 5),
    _AlaRipngRouteAge_Type()
)
alaRipngRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteAge.setStatus("current")


class _AlaRipngRouteTag_Type(Integer32):
    """Custom type alaRipngRouteTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipngRouteTag_Type.__name__ = "Integer32"
_AlaRipngRouteTag_Object = MibTableColumn
alaRipngRouteTag = _AlaRipngRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 6),
    _AlaRipngRouteTag_Type()
)
alaRipngRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteTag.setStatus("current")


class _AlaRipngRouteMetric_Type(Integer32):
    """Custom type alaRipngRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipngRouteMetric_Type.__name__ = "Integer32"
_AlaRipngRouteMetric_Object = MibTableColumn
alaRipngRouteMetric = _AlaRipngRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 7),
    _AlaRipngRouteMetric_Type()
)
alaRipngRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteMetric.setStatus("current")


class _AlaRipngRouteStatus_Type(Integer32):
    """Custom type alaRipngRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_AlaRipngRouteStatus_Type.__name__ = "Integer32"
_AlaRipngRouteStatus_Object = MibTableColumn
alaRipngRouteStatus = _AlaRipngRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 8),
    _AlaRipngRouteStatus_Type()
)
alaRipngRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteStatus.setStatus("current")


class _AlaRipngRouteFlags_Type(Integer32):
    """Custom type alaRipngRouteFlags based on Integer32"""
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
        *(("active", 1),
          ("garbage", 2),
          ("holddown", 3),
          ("unknown", 4))
    )


_AlaRipngRouteFlags_Type.__name__ = "Integer32"
_AlaRipngRouteFlags_Object = MibTableColumn
alaRipngRouteFlags = _AlaRipngRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 9),
    _AlaRipngRouteFlags_Type()
)
alaRipngRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteFlags.setStatus("current")
_AlaRipngRouteIndex_Type = Integer32
_AlaRipngRouteIndex_Object = MibTableColumn
alaRipngRouteIndex = _AlaRipngRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 1, 1, 16, 1, 10),
    _AlaRipngRouteIndex_Type()
)
alaRipngRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipngRouteIndex.setStatus("current")
_AlcatelIND1RIPNGMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBConformance = _AlcatelIND1RIPNGMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBConformance.setStatus("current")
_AlcatelIND1RIPNGMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBGroups = _AlcatelIND1RIPNGMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBGroups.setStatus("current")
_AlcatelIND1RIPNGMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGMIBCompliances = _AlcatelIND1RIPNGMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGMIBCompliances.setStatus("current")
_AlcatelIND1RIPNGTraps_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGTraps = _AlcatelIND1RIPNGTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3)
)
_AlcatelIND1RIPNGTrapsRoot_ObjectIdentity = ObjectIdentity
alcatelIND1RIPNGTrapsRoot = _AlcatelIND1RIPNGTrapsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3, 0)
)

# Managed Objects groups

alaRipngGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 1)
)
alaRipngGlobalGroup.setObjects(
      *(("ALCATEL-ENT1-RIPNG-MIB", "alaRipngProtoStatus"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngUpdateInterval"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInvalidTimer"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngHolddownTimer"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngGarbageTimer"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteCount"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngGlobalRouteTag"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngTriggeredSends"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngJitter"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPort"))
)
if mibBuilder.loadTexts:
    alaRipngGlobalGroup.setStatus("current")

alaRipngInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 3)
)
alaRipngInterfaceGroup.setObjects(
      *(("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceStatus"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceMetric"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceRecvStatus"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceSendStatus"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceHorizon"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfacePacketsSent"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfacePacketsRcvd"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceMTU"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceNextUpdate"))
)
if mibBuilder.loadTexts:
    alaRipngInterfaceGroup.setStatus("current")

alaRipngPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 7)
)
alaRipngPeerGroup.setObjects(
      *(("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerLastUpdate"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerNumUpdates"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerNumRoutes"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerBadPackets"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerBadRoutes"))
)
if mibBuilder.loadTexts:
    alaRipngPeerGroup.setStatus("current")

alaRipngRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 8)
)
alaRipngRouteGroup.setObjects(
      *(("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteType"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteAge"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteTag"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteMetric"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteStatus"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteFlags"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteIndex"))
)
if mibBuilder.loadTexts:
    alaRipngRouteGroup.setStatus("current")


# Notification objects

ripngRouteMaxLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ripngRouteMaxLimitReached.setStatus(
        "current"
    )


# Notifications groups

alcatelIND1RIPNGTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 1, 9)
)
alcatelIND1RIPNGTrapsGroup.setObjects(
    ("ALCATEL-ENT1-RIPNG-MIB", "ripngRouteMaxLimitReached")
)
if mibBuilder.loadTexts:
    alcatelIND1RIPNGTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1RIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 12, 1, 2, 2, 1)
)
alcatelIND1RIPMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-RIPNG-MIB", "alaRipngGlobalGroup"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngInterfaceGroup"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngPeerGroup"),
        ("ALCATEL-ENT1-RIPNG-MIB", "alaRipngRouteGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-RIPNG-MIB",
    **{"alcatelIND1RIPNGMIB": alcatelIND1RIPNGMIB,
       "alcatelIND1RIPNGMIBObjects": alcatelIND1RIPNGMIBObjects,
       "alaProtocolRipng": alaProtocolRipng,
       "alaRipngProtoStatus": alaRipngProtoStatus,
       "alaRipngUpdateInterval": alaRipngUpdateInterval,
       "alaRipngInvalidTimer": alaRipngInvalidTimer,
       "alaRipngHolddownTimer": alaRipngHolddownTimer,
       "alaRipngGarbageTimer": alaRipngGarbageTimer,
       "alaRipngRouteCount": alaRipngRouteCount,
       "alaRipngGlobalRouteTag": alaRipngGlobalRouteTag,
       "alaRipngTriggeredSends": alaRipngTriggeredSends,
       "alaRipngJitter": alaRipngJitter,
       "alaRipngPort": alaRipngPort,
       "alaRipngInterfaceTable": alaRipngInterfaceTable,
       "alaRipngInterfaceEntry": alaRipngInterfaceEntry,
       "alaRipngInterfaceIndex": alaRipngInterfaceIndex,
       "alaRipngInterfaceStatus": alaRipngInterfaceStatus,
       "alaRipngInterfaceMetric": alaRipngInterfaceMetric,
       "alaRipngInterfaceRecvStatus": alaRipngInterfaceRecvStatus,
       "alaRipngInterfaceSendStatus": alaRipngInterfaceSendStatus,
       "alaRipngInterfaceHorizon": alaRipngInterfaceHorizon,
       "alaRipngInterfacePacketsSent": alaRipngInterfacePacketsSent,
       "alaRipngInterfacePacketsRcvd": alaRipngInterfacePacketsRcvd,
       "alaRipngInterfaceMTU": alaRipngInterfaceMTU,
       "alaRipngInterfaceNextUpdate": alaRipngInterfaceNextUpdate,
       "alaRipngPeerTable": alaRipngPeerTable,
       "alaRipngPeerEntry": alaRipngPeerEntry,
       "alaRipngPeerAddress": alaRipngPeerAddress,
       "alaRipngPeerIndex": alaRipngPeerIndex,
       "alaRipngPeerLastUpdate": alaRipngPeerLastUpdate,
       "alaRipngPeerNumUpdates": alaRipngPeerNumUpdates,
       "alaRipngPeerNumRoutes": alaRipngPeerNumRoutes,
       "alaRipngPeerBadPackets": alaRipngPeerBadPackets,
       "alaRipngPeerBadRoutes": alaRipngPeerBadRoutes,
       "alaRipngRouteTable": alaRipngRouteTable,
       "alaRipngRouteEntry": alaRipngRouteEntry,
       "alaRipngRoutePrefix": alaRipngRoutePrefix,
       "alaRipngRoutePrefixLen": alaRipngRoutePrefixLen,
       "alaRipngRouteNextHop": alaRipngRouteNextHop,
       "alaRipngRouteType": alaRipngRouteType,
       "alaRipngRouteAge": alaRipngRouteAge,
       "alaRipngRouteTag": alaRipngRouteTag,
       "alaRipngRouteMetric": alaRipngRouteMetric,
       "alaRipngRouteStatus": alaRipngRouteStatus,
       "alaRipngRouteFlags": alaRipngRouteFlags,
       "alaRipngRouteIndex": alaRipngRouteIndex,
       "alcatelIND1RIPNGMIBConformance": alcatelIND1RIPNGMIBConformance,
       "alcatelIND1RIPNGMIBGroups": alcatelIND1RIPNGMIBGroups,
       "alaRipngGlobalGroup": alaRipngGlobalGroup,
       "alaRipngInterfaceGroup": alaRipngInterfaceGroup,
       "alaRipngPeerGroup": alaRipngPeerGroup,
       "alaRipngRouteGroup": alaRipngRouteGroup,
       "alcatelIND1RIPNGTrapsGroup": alcatelIND1RIPNGTrapsGroup,
       "alcatelIND1RIPNGMIBCompliances": alcatelIND1RIPNGMIBCompliances,
       "alcatelIND1RIPMIBCompliance": alcatelIND1RIPMIBCompliance,
       "alcatelIND1RIPNGTraps": alcatelIND1RIPNGTraps,
       "alcatelIND1RIPNGTrapsRoot": alcatelIND1RIPNGTrapsRoot,
       "ripngRouteMaxLimitReached": ripngRouteMaxLimitReached}
)
