# SNMP MIB module (ALCATEL-ENT1-RIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-RIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:44 2025
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

(routingIND1Rip,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "routingIND1Rip")

(rip2IfConfEntry,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "rip2IfConfEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

alcatelIND1RIPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaAuthenticationEncryptKey(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1RIPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBObjects = _AlcatelIND1RIPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBObjects.setStatus("current")
_AlaProtocolRip_ObjectIdentity = ObjectIdentity
alaProtocolRip = _AlaProtocolRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1)
)


class _AlaRipProtoStatus_Type(Integer32):
    """Custom type alaRipProtoStatus based on Integer32"""
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


_AlaRipProtoStatus_Type.__name__ = "Integer32"
_AlaRipProtoStatus_Object = MibScalar
alaRipProtoStatus = _AlaRipProtoStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 1),
    _AlaRipProtoStatus_Type()
)
alaRipProtoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipProtoStatus.setStatus("current")


class _AlaRipHostRouteSupport_Type(Integer32):
    """Custom type alaRipHostRouteSupport based on Integer32"""
    defaultValue = 1

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


_AlaRipHostRouteSupport_Type.__name__ = "Integer32"
_AlaRipHostRouteSupport_Object = MibScalar
alaRipHostRouteSupport = _AlaRipHostRouteSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 2),
    _AlaRipHostRouteSupport_Type()
)
alaRipHostRouteSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipHostRouteSupport.setStatus("current")


class _AlaRipRedistRouteTag_Type(Integer32):
    """Custom type alaRipRedistRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipRedistRouteTag_Type.__name__ = "Integer32"
_AlaRipRedistRouteTag_Object = MibScalar
alaRipRedistRouteTag = _AlaRipRedistRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 4),
    _AlaRipRedistRouteTag_Type()
)
alaRipRedistRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipRedistRouteTag.setStatus("current")


class _AlaRipForceHolddownTimer_Type(Integer32):
    """Custom type alaRipForceHolddownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaRipForceHolddownTimer_Type.__name__ = "Integer32"
_AlaRipForceHolddownTimer_Object = MibScalar
alaRipForceHolddownTimer = _AlaRipForceHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 5),
    _AlaRipForceHolddownTimer_Type()
)
alaRipForceHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipForceHolddownTimer.setStatus("current")


class _AlaRipRouteNumber_Type(Integer32):
    """Custom type alaRipRouteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipRouteNumber_Type.__name__ = "Integer32"
_AlaRipRouteNumber_Object = MibScalar
alaRipRouteNumber = _AlaRipRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 6),
    _AlaRipRouteNumber_Type()
)
alaRipRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipRouteNumber.setStatus("current")
_AlaRip2IfConfAugTable_Object = MibTable
alaRip2IfConfAugTable = _AlaRip2IfConfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaRip2IfConfAugTable.setStatus("current")
_AlaRip2IfConfAugEntry_Object = MibTableRow
alaRip2IfConfAugEntry = _AlaRip2IfConfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaRip2IfConfAugEntry.setStatus("current")
_AlaRip2IfConfEncryptKey_Type = AlaAuthenticationEncryptKey
_AlaRip2IfConfEncryptKey_Object = MibTableColumn
alaRip2IfConfEncryptKey = _AlaRip2IfConfEncryptKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 1),
    _AlaRip2IfConfEncryptKey_Type()
)
alaRip2IfConfEncryptKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfEncryptKey.setStatus("current")


class _AlaRip2IfIpConfStatus_Type(Integer32):
    """Custom type alaRip2IfIpConfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("none", 3))
    )


_AlaRip2IfIpConfStatus_Type.__name__ = "Integer32"
_AlaRip2IfIpConfStatus_Object = MibTableColumn
alaRip2IfIpConfStatus = _AlaRip2IfIpConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 2),
    _AlaRip2IfIpConfStatus_Type()
)
alaRip2IfIpConfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRip2IfIpConfStatus.setStatus("current")
_AlaRip2IfRecvPkts_Type = Integer32
_AlaRip2IfRecvPkts_Object = MibTableColumn
alaRip2IfRecvPkts = _AlaRip2IfRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 3),
    _AlaRip2IfRecvPkts_Type()
)
alaRip2IfRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRip2IfRecvPkts.setStatus("current")
_AlaRip2IfConfName_Type = SnmpAdminString
_AlaRip2IfConfName_Object = MibTableColumn
alaRip2IfConfName = _AlaRip2IfConfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 4),
    _AlaRip2IfConfName_Type()
)
alaRip2IfConfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRip2IfConfName.setStatus("current")


class _AlaRip2IfConfType_Type(Integer32):
    """Custom type alaRip2IfConfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("point2point", 2))
    )


_AlaRip2IfConfType_Type.__name__ = "Integer32"
_AlaRip2IfConfType_Object = MibTableColumn
alaRip2IfConfType = _AlaRip2IfConfType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 5),
    _AlaRip2IfConfType_Type()
)
alaRip2IfConfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfType.setStatus("current")
_AlaRip2IfConfPtoPPeer_Type = IpAddress
_AlaRip2IfConfPtoPPeer_Object = MibTableColumn
alaRip2IfConfPtoPPeer = _AlaRip2IfConfPtoPPeer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 6),
    _AlaRip2IfConfPtoPPeer_Type()
)
alaRip2IfConfPtoPPeer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfPtoPPeer.setStatus("current")


class _AlaRip2IfConfIngressFilterRouteMapName_Type(SnmpAdminString):
    """Custom type alaRip2IfConfIngressFilterRouteMapName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaRip2IfConfIngressFilterRouteMapName_Type.__name__ = "SnmpAdminString"
_AlaRip2IfConfIngressFilterRouteMapName_Object = MibTableColumn
alaRip2IfConfIngressFilterRouteMapName = _AlaRip2IfConfIngressFilterRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 7),
    _AlaRip2IfConfIngressFilterRouteMapName_Type()
)
alaRip2IfConfIngressFilterRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfIngressFilterRouteMapName.setStatus("current")


class _AlaRip2IfConfEgressFilterRouteMapName_Type(SnmpAdminString):
    """Custom type alaRip2IfConfEgressFilterRouteMapName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaRip2IfConfEgressFilterRouteMapName_Type.__name__ = "SnmpAdminString"
_AlaRip2IfConfEgressFilterRouteMapName_Object = MibTableColumn
alaRip2IfConfEgressFilterRouteMapName = _AlaRip2IfConfEgressFilterRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 11, 1, 8),
    _AlaRip2IfConfEgressFilterRouteMapName_Type()
)
alaRip2IfConfEgressFilterRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRip2IfConfEgressFilterRouteMapName.setStatus("current")
_AlaRipEcmpRouteTable_Object = MibTable
alaRipEcmpRouteTable = _AlaRipEcmpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaRipEcmpRouteTable.setStatus("current")
_AlaRipEcmpRouteEntry_Object = MibTableRow
alaRipEcmpRouteEntry = _AlaRipEcmpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1)
)
alaRipEcmpRouteEntry.setIndexNames(
    (0, "ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteDest"),
    (0, "ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteMask"),
    (0, "ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaRipEcmpRouteEntry.setStatus("current")
_AlaRipEcmpRouteDest_Type = IpAddress
_AlaRipEcmpRouteDest_Object = MibTableColumn
alaRipEcmpRouteDest = _AlaRipEcmpRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 1),
    _AlaRipEcmpRouteDest_Type()
)
alaRipEcmpRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipEcmpRouteDest.setStatus("current")
_AlaRipEcmpRouteMask_Type = IpAddress
_AlaRipEcmpRouteMask_Object = MibTableColumn
alaRipEcmpRouteMask = _AlaRipEcmpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 2),
    _AlaRipEcmpRouteMask_Type()
)
alaRipEcmpRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipEcmpRouteMask.setStatus("current")
_AlaRipEcmpRouteNextHop_Type = IpAddress
_AlaRipEcmpRouteNextHop_Object = MibTableColumn
alaRipEcmpRouteNextHop = _AlaRipEcmpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 3),
    _AlaRipEcmpRouteNextHop_Type()
)
alaRipEcmpRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaRipEcmpRouteNextHop.setStatus("current")


class _AlaRipEcmpRouteType_Type(Integer32):
    """Custom type alaRipEcmpRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2),
          ("redistribute", 3))
    )


_AlaRipEcmpRouteType_Type.__name__ = "Integer32"
_AlaRipEcmpRouteType_Object = MibTableColumn
alaRipEcmpRouteType = _AlaRipEcmpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 4),
    _AlaRipEcmpRouteType_Type()
)
alaRipEcmpRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteType.setStatus("current")
_AlaRipEcmpRouteAge_Type = TimeTicks
_AlaRipEcmpRouteAge_Object = MibTableColumn
alaRipEcmpRouteAge = _AlaRipEcmpRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 5),
    _AlaRipEcmpRouteAge_Type()
)
alaRipEcmpRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteAge.setStatus("current")


class _AlaRipEcmpRouteTag_Type(Integer32):
    """Custom type alaRipEcmpRouteTag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaRipEcmpRouteTag_Type.__name__ = "Integer32"
_AlaRipEcmpRouteTag_Object = MibTableColumn
alaRipEcmpRouteTag = _AlaRipEcmpRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 6),
    _AlaRipEcmpRouteTag_Type()
)
alaRipEcmpRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteTag.setStatus("current")


class _AlaRipEcmpRouteMetric_Type(Integer32):
    """Custom type alaRipEcmpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaRipEcmpRouteMetric_Type.__name__ = "Integer32"
_AlaRipEcmpRouteMetric_Object = MibTableColumn
alaRipEcmpRouteMetric = _AlaRipEcmpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 7),
    _AlaRipEcmpRouteMetric_Type()
)
alaRipEcmpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteMetric.setStatus("current")
_AlaRipEcmpRouteStatus_Type = RowStatus
_AlaRipEcmpRouteStatus_Object = MibTableColumn
alaRipEcmpRouteStatus = _AlaRipEcmpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 8),
    _AlaRipEcmpRouteStatus_Type()
)
alaRipEcmpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteStatus.setStatus("current")


class _AlaRipEcmpRouteState_Type(Integer32):
    """Custom type alaRipEcmpRouteState based on Integer32"""
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


_AlaRipEcmpRouteState_Type.__name__ = "Integer32"
_AlaRipEcmpRouteState_Object = MibTableColumn
alaRipEcmpRouteState = _AlaRipEcmpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 12, 1, 9),
    _AlaRipEcmpRouteState_Type()
)
alaRipEcmpRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaRipEcmpRouteState.setStatus("current")


class _AlaRipUpdateInterval_Type(Integer32):
    """Custom type alaRipUpdateInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AlaRipUpdateInterval_Type.__name__ = "Integer32"
_AlaRipUpdateInterval_Object = MibScalar
alaRipUpdateInterval = _AlaRipUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 13),
    _AlaRipUpdateInterval_Type()
)
alaRipUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaRipUpdateInterval.setUnits("seconds")


class _AlaRipInvalidTimer_Type(Integer32):
    """Custom type alaRipInvalidTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 360),
    )


_AlaRipInvalidTimer_Type.__name__ = "Integer32"
_AlaRipInvalidTimer_Object = MibScalar
alaRipInvalidTimer = _AlaRipInvalidTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 14),
    _AlaRipInvalidTimer_Type()
)
alaRipInvalidTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipInvalidTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipInvalidTimer.setUnits("seconds")


class _AlaRipHolddownTimer_Type(Integer32):
    """Custom type alaRipHolddownTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AlaRipHolddownTimer_Type.__name__ = "Integer32"
_AlaRipHolddownTimer_Object = MibScalar
alaRipHolddownTimer = _AlaRipHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 15),
    _AlaRipHolddownTimer_Type()
)
alaRipHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipHolddownTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipHolddownTimer.setUnits("seconds")


class _AlaRipGarbageTimer_Type(Integer32):
    """Custom type alaRipGarbageTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_AlaRipGarbageTimer_Type.__name__ = "Integer32"
_AlaRipGarbageTimer_Object = MibScalar
alaRipGarbageTimer = _AlaRipGarbageTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 1, 1, 16),
    _AlaRipGarbageTimer_Type()
)
alaRipGarbageTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaRipGarbageTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaRipGarbageTimer.setUnits("seconds")
_AlcatelIND1RIPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBConformance = _AlcatelIND1RIPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBConformance.setStatus("current")
_AlcatelIND1RIPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBGroups = _AlcatelIND1RIPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBGroups.setStatus("current")
_AlcatelIND1RIPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1RIPMIBCompliances = _AlcatelIND1RIPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBCompliances.setStatus("current")
_AlcatelIND1RIPTraps_ObjectIdentity = ObjectIdentity
alcatelIND1RIPTraps = _AlcatelIND1RIPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 3)
)
_AlcatelIND1RIPTrapsRoot_ObjectIdentity = ObjectIdentity
alcatelIND1RIPTrapsRoot = _AlcatelIND1RIPTrapsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 3, 0)
)
rip2IfConfEntry.registerAugmentions(
    ("ALCATEL-ENT1-RIP-MIB",
     "alaRip2IfConfAugEntry")
)
alaRip2IfConfAugEntry.setIndexNames(*rip2IfConfEntry.getIndexNames())

# Managed Objects groups

alaRipMiscellaneousGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 1)
)
alaRipMiscellaneousGroup.setObjects(
      *(("ALCATEL-ENT1-RIP-MIB", "alaRipRedistRouteTag"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipForceHolddownTimer"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipRouteNumber"))
)
if mibBuilder.loadTexts:
    alaRipMiscellaneousGroup.setStatus("current")

alaRip2IfConfAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 2)
)
alaRip2IfConfAugGroup.setObjects(
      *(("ALCATEL-ENT1-RIP-MIB", "alaRip2IfConfEncryptKey"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfIpConfStatus"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfRecvPkts"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfConfName"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfConfType"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfConfPtoPPeer"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfConfIngressFilterRouteMapName"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRip2IfConfEgressFilterRouteMapName"))
)
if mibBuilder.loadTexts:
    alaRip2IfConfAugGroup.setStatus("current")

alaProtocolRipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 3)
)
alaProtocolRipGroup.setObjects(
      *(("ALCATEL-ENT1-RIP-MIB", "alaRipProtoStatus"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipHostRouteSupport"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipRedistRouteTag"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipForceHolddownTimer"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipRouteNumber"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipUpdateInterval"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipInvalidTimer"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipHolddownTimer"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipGarbageTimer"))
)
if mibBuilder.loadTexts:
    alaProtocolRipGroup.setStatus("current")

alaRipEcmpRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 6)
)
alaRipEcmpRouteGroup.setObjects(
      *(("ALCATEL-ENT1-RIP-MIB", "alaRipRouteNumber"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteType"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteAge"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteTag"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteMetric"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteStatus"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteState"))
)
if mibBuilder.loadTexts:
    alaRipEcmpRouteGroup.setStatus("current")


# Notification objects

ripRouteMaxLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ripRouteMaxLimitReached.setStatus(
        "current"
    )


# Notifications groups

alcatelIND1RIPTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 1, 7)
)
alcatelIND1RIPTrapsGroup.setObjects(
    ("ALCATEL-ENT1-RIP-MIB", "ripRouteMaxLimitReached")
)
if mibBuilder.loadTexts:
    alcatelIND1RIPTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1RIPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 3, 1, 2, 2, 1)
)
alcatelIND1RIPMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-RIP-MIB", "alaRipMiscellaneousGroup"),
        ("ALCATEL-ENT1-RIP-MIB", "alaRipEcmpRouteGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1RIPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-RIP-MIB",
    **{"AlaAuthenticationEncryptKey": AlaAuthenticationEncryptKey,
       "alcatelIND1RIPMIB": alcatelIND1RIPMIB,
       "alcatelIND1RIPMIBObjects": alcatelIND1RIPMIBObjects,
       "alaProtocolRip": alaProtocolRip,
       "alaRipProtoStatus": alaRipProtoStatus,
       "alaRipHostRouteSupport": alaRipHostRouteSupport,
       "alaRipRedistRouteTag": alaRipRedistRouteTag,
       "alaRipForceHolddownTimer": alaRipForceHolddownTimer,
       "alaRipRouteNumber": alaRipRouteNumber,
       "alaRip2IfConfAugTable": alaRip2IfConfAugTable,
       "alaRip2IfConfAugEntry": alaRip2IfConfAugEntry,
       "alaRip2IfConfEncryptKey": alaRip2IfConfEncryptKey,
       "alaRip2IfIpConfStatus": alaRip2IfIpConfStatus,
       "alaRip2IfRecvPkts": alaRip2IfRecvPkts,
       "alaRip2IfConfName": alaRip2IfConfName,
       "alaRip2IfConfType": alaRip2IfConfType,
       "alaRip2IfConfPtoPPeer": alaRip2IfConfPtoPPeer,
       "alaRip2IfConfIngressFilterRouteMapName": alaRip2IfConfIngressFilterRouteMapName,
       "alaRip2IfConfEgressFilterRouteMapName": alaRip2IfConfEgressFilterRouteMapName,
       "alaRipEcmpRouteTable": alaRipEcmpRouteTable,
       "alaRipEcmpRouteEntry": alaRipEcmpRouteEntry,
       "alaRipEcmpRouteDest": alaRipEcmpRouteDest,
       "alaRipEcmpRouteMask": alaRipEcmpRouteMask,
       "alaRipEcmpRouteNextHop": alaRipEcmpRouteNextHop,
       "alaRipEcmpRouteType": alaRipEcmpRouteType,
       "alaRipEcmpRouteAge": alaRipEcmpRouteAge,
       "alaRipEcmpRouteTag": alaRipEcmpRouteTag,
       "alaRipEcmpRouteMetric": alaRipEcmpRouteMetric,
       "alaRipEcmpRouteStatus": alaRipEcmpRouteStatus,
       "alaRipEcmpRouteState": alaRipEcmpRouteState,
       "alaRipUpdateInterval": alaRipUpdateInterval,
       "alaRipInvalidTimer": alaRipInvalidTimer,
       "alaRipHolddownTimer": alaRipHolddownTimer,
       "alaRipGarbageTimer": alaRipGarbageTimer,
       "alcatelIND1RIPMIBConformance": alcatelIND1RIPMIBConformance,
       "alcatelIND1RIPMIBGroups": alcatelIND1RIPMIBGroups,
       "alaRipMiscellaneousGroup": alaRipMiscellaneousGroup,
       "alaRip2IfConfAugGroup": alaRip2IfConfAugGroup,
       "alaProtocolRipGroup": alaProtocolRipGroup,
       "alaRipEcmpRouteGroup": alaRipEcmpRouteGroup,
       "alcatelIND1RIPTrapsGroup": alcatelIND1RIPTrapsGroup,
       "alcatelIND1RIPMIBCompliances": alcatelIND1RIPMIBCompliances,
       "alcatelIND1RIPMIBCompliance": alcatelIND1RIPMIBCompliance,
       "alcatelIND1RIPTraps": alcatelIND1RIPTraps,
       "alcatelIND1RIPTrapsRoot": alcatelIND1RIPTrapsRoot,
       "ripRouteMaxLimitReached": ripRouteMaxLimitReached}
)
