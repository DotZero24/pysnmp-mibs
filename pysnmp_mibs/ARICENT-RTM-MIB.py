# SNMP MIB module (ARICENT-RTM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-RTM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:16 2025
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

futurertm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 107)
)
if mibBuilder.loadTexts:
    futurertm.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsrrdScalar_ObjectIdentity = ObjectIdentity
fsrrdScalar = _FsrrdScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1)
)
_FsRrdRouterId_Type = IpAddress
_FsRrdRouterId_Object = MibScalar
fsRrdRouterId = _FsRrdRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 1),
    _FsRrdRouterId_Type()
)
fsRrdRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdRouterId.setStatus("current")


class _FsRrdFilterByOspfTag_Type(Integer32):
    """Custom type fsRrdFilterByOspfTag based on Integer32"""
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


_FsRrdFilterByOspfTag_Type.__name__ = "Integer32"
_FsRrdFilterByOspfTag_Object = MibScalar
fsRrdFilterByOspfTag = _FsRrdFilterByOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 2),
    _FsRrdFilterByOspfTag_Type()
)
fsRrdFilterByOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdFilterByOspfTag.setStatus("current")
_FsRrdFilterOspfTag_Type = Integer32
_FsRrdFilterOspfTag_Object = MibScalar
fsRrdFilterOspfTag = _FsRrdFilterOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 3),
    _FsRrdFilterOspfTag_Type()
)
fsRrdFilterOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdFilterOspfTag.setStatus("current")


class _FsRrdFilterOspfTagMask_Type(Integer32):
    """Custom type fsRrdFilterOspfTagMask based on Integer32"""
    defaultValue = -1


_FsRrdFilterOspfTagMask_Type.__name__ = "Integer32"
_FsRrdFilterOspfTagMask_Object = MibScalar
fsRrdFilterOspfTagMask = _FsRrdFilterOspfTagMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 4),
    _FsRrdFilterOspfTagMask_Type()
)
fsRrdFilterOspfTagMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdFilterOspfTagMask.setStatus("current")


class _FsRrdRouterASNumber_Type(Integer32):
    """Custom type fsRrdRouterASNumber based on Integer32"""
    defaultValue = 0


_FsRrdRouterASNumber_Type.__name__ = "Integer32"
_FsRrdRouterASNumber_Object = MibScalar
fsRrdRouterASNumber = _FsRrdRouterASNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 5),
    _FsRrdRouterASNumber_Type()
)
fsRrdRouterASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdRouterASNumber.setStatus("current")


class _FsRrdAdminStatus_Type(Integer32):
    """Custom type fsRrdAdminStatus based on Integer32"""
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


_FsRrdAdminStatus_Type.__name__ = "Integer32"
_FsRrdAdminStatus_Object = MibScalar
fsRrdAdminStatus = _FsRrdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 6),
    _FsRrdAdminStatus_Type()
)
fsRrdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdAdminStatus.setStatus("current")


class _FsRtmThrottleLimit_Type(Unsigned32):
    """Custom type fsRtmThrottleLimit based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRtmThrottleLimit_Type.__name__ = "Unsigned32"
_FsRtmThrottleLimit_Object = MibScalar
fsRtmThrottleLimit = _FsRtmThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 7),
    _FsRtmThrottleLimit_Type()
)
fsRtmThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmThrottleLimit.setStatus("current")
_FsRtmMaximumBgpRoutes_Type = Unsigned32
_FsRtmMaximumBgpRoutes_Object = MibScalar
fsRtmMaximumBgpRoutes = _FsRtmMaximumBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 8),
    _FsRtmMaximumBgpRoutes_Type()
)
fsRtmMaximumBgpRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmMaximumBgpRoutes.setStatus("current")
_FsRtmMaximumOspfRoutes_Type = Unsigned32
_FsRtmMaximumOspfRoutes_Object = MibScalar
fsRtmMaximumOspfRoutes = _FsRtmMaximumOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 9),
    _FsRtmMaximumOspfRoutes_Type()
)
fsRtmMaximumOspfRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmMaximumOspfRoutes.setStatus("current")
_FsRtmMaximumRipRoutes_Type = Unsigned32
_FsRtmMaximumRipRoutes_Object = MibScalar
fsRtmMaximumRipRoutes = _FsRtmMaximumRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 10),
    _FsRtmMaximumRipRoutes_Type()
)
fsRtmMaximumRipRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmMaximumRipRoutes.setStatus("current")
_FsRtmMaximumStaticRoutes_Type = Unsigned32
_FsRtmMaximumStaticRoutes_Object = MibScalar
fsRtmMaximumStaticRoutes = _FsRtmMaximumStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 11),
    _FsRtmMaximumStaticRoutes_Type()
)
fsRtmMaximumStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmMaximumStaticRoutes.setStatus("current")
_FsRtmMaximumISISRoutes_Type = Unsigned32
_FsRtmMaximumISISRoutes_Object = MibScalar
fsRtmMaximumISISRoutes = _FsRtmMaximumISISRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 12),
    _FsRtmMaximumISISRoutes_Type()
)
fsRtmMaximumISISRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmMaximumISISRoutes.setStatus("current")


class _FsRtmIpStaticRouteDistance_Type(Integer32):
    """Custom type fsRtmIpStaticRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRtmIpStaticRouteDistance_Type.__name__ = "Integer32"
_FsRtmIpStaticRouteDistance_Object = MibScalar
fsRtmIpStaticRouteDistance = _FsRtmIpStaticRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 13),
    _FsRtmIpStaticRouteDistance_Type()
)
fsRtmIpStaticRouteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmIpStaticRouteDistance.setStatus("current")


class _FsEcmpAcrossProtocolAdminStatus_Type(Integer32):
    """Custom type fsEcmpAcrossProtocolAdminStatus based on Integer32"""
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


_FsEcmpAcrossProtocolAdminStatus_Type.__name__ = "Integer32"
_FsEcmpAcrossProtocolAdminStatus_Object = MibScalar
fsEcmpAcrossProtocolAdminStatus = _FsEcmpAcrossProtocolAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 14),
    _FsEcmpAcrossProtocolAdminStatus_Type()
)
fsEcmpAcrossProtocolAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEcmpAcrossProtocolAdminStatus.setStatus("current")


class _FsRtmRouteLeakStatus_Type(Integer32):
    """Custom type fsRtmRouteLeakStatus based on Integer32"""
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


_FsRtmRouteLeakStatus_Type.__name__ = "Integer32"
_FsRtmRouteLeakStatus_Object = MibScalar
fsRtmRouteLeakStatus = _FsRtmRouteLeakStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 1, 15),
    _FsRtmRouteLeakStatus_Type()
)
fsRtmRouteLeakStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmRouteLeakStatus.setStatus("current")
_FsRrdControlTable_Object = MibTable
fsRrdControlTable = _FsRrdControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2)
)
if mibBuilder.loadTexts:
    fsRrdControlTable.setStatus("current")
_FsRrdControlEntry_Object = MibTableRow
fsRrdControlEntry = _FsRrdControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1)
)
fsRrdControlEntry.setIndexNames(
    (0, "ARICENT-RTM-MIB", "fsRrdControlDestIpAddress"),
    (0, "ARICENT-RTM-MIB", "fsRrdControlNetMask"),
)
if mibBuilder.loadTexts:
    fsRrdControlEntry.setStatus("current")
_FsRrdControlDestIpAddress_Type = IpAddress
_FsRrdControlDestIpAddress_Object = MibTableColumn
fsRrdControlDestIpAddress = _FsRrdControlDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1, 1),
    _FsRrdControlDestIpAddress_Type()
)
fsRrdControlDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrdControlDestIpAddress.setStatus("current")
_FsRrdControlNetMask_Type = IpAddress
_FsRrdControlNetMask_Object = MibTableColumn
fsRrdControlNetMask = _FsRrdControlNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1, 2),
    _FsRrdControlNetMask_Type()
)
fsRrdControlNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrdControlNetMask.setStatus("current")


class _FsRrdControlSourceProto_Type(Integer32):
    """Custom type fsRrdControlSourceProto based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_FsRrdControlSourceProto_Type.__name__ = "Integer32"
_FsRrdControlSourceProto_Object = MibTableColumn
fsRrdControlSourceProto = _FsRrdControlSourceProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1, 3),
    _FsRrdControlSourceProto_Type()
)
fsRrdControlSourceProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdControlSourceProto.setStatus("current")


class _FsRrdControlDestProto_Type(Integer32):
    """Custom type fsRrdControlDestProto based on Integer32"""
    defaultValue = 0


_FsRrdControlDestProto_Type.__name__ = "Integer32"
_FsRrdControlDestProto_Object = MibTableColumn
fsRrdControlDestProto = _FsRrdControlDestProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1, 4),
    _FsRrdControlDestProto_Type()
)
fsRrdControlDestProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdControlDestProto.setStatus("current")


class _FsRrdControlRouteExportFlag_Type(Integer32):
    """Custom type fsRrdControlRouteExportFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_FsRrdControlRouteExportFlag_Type.__name__ = "Integer32"
_FsRrdControlRouteExportFlag_Object = MibTableColumn
fsRrdControlRouteExportFlag = _FsRrdControlRouteExportFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1, 5),
    _FsRrdControlRouteExportFlag_Type()
)
fsRrdControlRouteExportFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdControlRouteExportFlag.setStatus("current")
_FsRrdControlRowStatus_Type = RowStatus
_FsRrdControlRowStatus_Object = MibTableColumn
fsRrdControlRowStatus = _FsRrdControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 2, 1, 6),
    _FsRrdControlRowStatus_Type()
)
fsRrdControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdControlRowStatus.setStatus("current")
_FsRrdRoutingProtoTable_Object = MibTable
fsRrdRoutingProtoTable = _FsRrdRoutingProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3)
)
if mibBuilder.loadTexts:
    fsRrdRoutingProtoTable.setStatus("current")
_FsRrdRoutingProtoEntry_Object = MibTableRow
fsRrdRoutingProtoEntry = _FsRrdRoutingProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1)
)
fsRrdRoutingProtoEntry.setIndexNames(
    (0, "ARICENT-RTM-MIB", "fsRrdRoutingProtoId"),
)
if mibBuilder.loadTexts:
    fsRrdRoutingProtoEntry.setStatus("current")


class _FsRrdRoutingProtoId_Type(Integer32):
    """Custom type fsRrdRoutingProtoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_FsRrdRoutingProtoId_Type.__name__ = "Integer32"
_FsRrdRoutingProtoId_Object = MibTableColumn
fsRrdRoutingProtoId = _FsRrdRoutingProtoId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1, 1),
    _FsRrdRoutingProtoId_Type()
)
fsRrdRoutingProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrdRoutingProtoId.setStatus("current")
_FsRrdRoutingRegnId_Type = Integer32
_FsRrdRoutingRegnId_Object = MibTableColumn
fsRrdRoutingRegnId = _FsRrdRoutingRegnId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1, 2),
    _FsRrdRoutingRegnId_Type()
)
fsRrdRoutingRegnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrdRoutingRegnId.setStatus("current")
_FsRrdRoutingProtoTaskIdent_Type = OctetString
_FsRrdRoutingProtoTaskIdent_Object = MibTableColumn
fsRrdRoutingProtoTaskIdent = _FsRrdRoutingProtoTaskIdent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1, 3),
    _FsRrdRoutingProtoTaskIdent_Type()
)
fsRrdRoutingProtoTaskIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrdRoutingProtoTaskIdent.setStatus("current")
_FsRrdRoutingProtoQueueIdent_Type = OctetString
_FsRrdRoutingProtoQueueIdent_Object = MibTableColumn
fsRrdRoutingProtoQueueIdent = _FsRrdRoutingProtoQueueIdent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1, 4),
    _FsRrdRoutingProtoQueueIdent_Type()
)
fsRrdRoutingProtoQueueIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrdRoutingProtoQueueIdent.setStatus("current")


class _FsRrdAllowOspfAreaRoutes_Type(Integer32):
    """Custom type fsRrdAllowOspfAreaRoutes based on Integer32"""
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


_FsRrdAllowOspfAreaRoutes_Type.__name__ = "Integer32"
_FsRrdAllowOspfAreaRoutes_Object = MibTableColumn
fsRrdAllowOspfAreaRoutes = _FsRrdAllowOspfAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1, 5),
    _FsRrdAllowOspfAreaRoutes_Type()
)
fsRrdAllowOspfAreaRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdAllowOspfAreaRoutes.setStatus("current")


class _FsRrdAllowOspfExtRoutes_Type(Integer32):
    """Custom type fsRrdAllowOspfExtRoutes based on Integer32"""
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


_FsRrdAllowOspfExtRoutes_Type.__name__ = "Integer32"
_FsRrdAllowOspfExtRoutes_Object = MibTableColumn
fsRrdAllowOspfExtRoutes = _FsRrdAllowOspfExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 3, 1, 6),
    _FsRrdAllowOspfExtRoutes_Type()
)
fsRrdAllowOspfExtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrdAllowOspfExtRoutes.setStatus("current")
_FsRtmCommonRouteTable_Object = MibTable
fsRtmCommonRouteTable = _FsRtmCommonRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4)
)
if mibBuilder.loadTexts:
    fsRtmCommonRouteTable.setStatus("current")
_FsRtmCommonRouteEntry_Object = MibTableRow
fsRtmCommonRouteEntry = _FsRtmCommonRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1)
)
fsRtmCommonRouteEntry.setIndexNames(
    (0, "ARICENT-RTM-MIB", "fsRtmCommonRouteDest"),
    (0, "ARICENT-RTM-MIB", "fsRtmCommonRouteMask"),
    (0, "ARICENT-RTM-MIB", "fsRtmCommonRouteTos"),
    (0, "ARICENT-RTM-MIB", "fsRtmCommonRouteNextHop"),
)
if mibBuilder.loadTexts:
    fsRtmCommonRouteEntry.setStatus("current")
_FsRtmCommonRouteDest_Type = IpAddress
_FsRtmCommonRouteDest_Object = MibTableColumn
fsRtmCommonRouteDest = _FsRtmCommonRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 1),
    _FsRtmCommonRouteDest_Type()
)
fsRtmCommonRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRtmCommonRouteDest.setStatus("current")
_FsRtmCommonRouteMask_Type = IpAddress
_FsRtmCommonRouteMask_Object = MibTableColumn
fsRtmCommonRouteMask = _FsRtmCommonRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 2),
    _FsRtmCommonRouteMask_Type()
)
fsRtmCommonRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRtmCommonRouteMask.setStatus("current")


class _FsRtmCommonRouteTos_Type(Integer32):
    """Custom type fsRtmCommonRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsRtmCommonRouteTos_Type.__name__ = "Integer32"
_FsRtmCommonRouteTos_Object = MibTableColumn
fsRtmCommonRouteTos = _FsRtmCommonRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 3),
    _FsRtmCommonRouteTos_Type()
)
fsRtmCommonRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRtmCommonRouteTos.setStatus("current")
_FsRtmCommonRouteNextHop_Type = IpAddress
_FsRtmCommonRouteNextHop_Object = MibTableColumn
fsRtmCommonRouteNextHop = _FsRtmCommonRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 4),
    _FsRtmCommonRouteNextHop_Type()
)
fsRtmCommonRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRtmCommonRouteNextHop.setStatus("current")


class _FsRtmCommonRouteIfIndex_Type(Integer32):
    """Custom type fsRtmCommonRouteIfIndex based on Integer32"""
    defaultValue = 0


_FsRtmCommonRouteIfIndex_Type.__name__ = "Integer32"
_FsRtmCommonRouteIfIndex_Object = MibTableColumn
fsRtmCommonRouteIfIndex = _FsRtmCommonRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 5),
    _FsRtmCommonRouteIfIndex_Type()
)
fsRtmCommonRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRouteIfIndex.setStatus("current")


class _FsRtmCommonRouteType_Type(Integer32):
    """Custom type fsRtmCommonRouteType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_FsRtmCommonRouteType_Type.__name__ = "Integer32"
_FsRtmCommonRouteType_Object = MibTableColumn
fsRtmCommonRouteType = _FsRtmCommonRouteType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 6),
    _FsRtmCommonRouteType_Type()
)
fsRtmCommonRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRouteType.setStatus("current")


class _FsRtmCommonRouteProto_Type(Integer32):
    """Custom type fsRtmCommonRouteProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("icmp", 4),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("rip", 8),
          ("isIs", 9),
          ("esIs", 10),
          ("ciscoIgrp", 11),
          ("bbnSpfIgp", 12),
          ("ospf", 13),
          ("bgp", 14),
          ("idpr", 15),
          ("ciscoEigrp", 16))
    )


_FsRtmCommonRouteProto_Type.__name__ = "Integer32"
_FsRtmCommonRouteProto_Object = MibTableColumn
fsRtmCommonRouteProto = _FsRtmCommonRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 7),
    _FsRtmCommonRouteProto_Type()
)
fsRtmCommonRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRtmCommonRouteProto.setStatus("current")


class _FsRtmCommonRouteAge_Type(Integer32):
    """Custom type fsRtmCommonRouteAge based on Integer32"""
    defaultValue = 0


_FsRtmCommonRouteAge_Type.__name__ = "Integer32"
_FsRtmCommonRouteAge_Object = MibTableColumn
fsRtmCommonRouteAge = _FsRtmCommonRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 8),
    _FsRtmCommonRouteAge_Type()
)
fsRtmCommonRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRtmCommonRouteAge.setStatus("current")
_FsRtmCommonRouteInfo_Type = ObjectIdentifier
_FsRtmCommonRouteInfo_Object = MibTableColumn
fsRtmCommonRouteInfo = _FsRtmCommonRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 9),
    _FsRtmCommonRouteInfo_Type()
)
fsRtmCommonRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRouteInfo.setStatus("current")


class _FsRtmCommonRouteNextHopAS_Type(Integer32):
    """Custom type fsRtmCommonRouteNextHopAS based on Integer32"""
    defaultValue = 0


_FsRtmCommonRouteNextHopAS_Type.__name__ = "Integer32"
_FsRtmCommonRouteNextHopAS_Object = MibTableColumn
fsRtmCommonRouteNextHopAS = _FsRtmCommonRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 10),
    _FsRtmCommonRouteNextHopAS_Type()
)
fsRtmCommonRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRouteNextHopAS.setStatus("current")


class _FsRtmCommonRouteMetric1_Type(Integer32):
    """Custom type fsRtmCommonRouteMetric1 based on Integer32"""
    defaultValue = -1


_FsRtmCommonRouteMetric1_Type.__name__ = "Integer32"
_FsRtmCommonRouteMetric1_Object = MibTableColumn
fsRtmCommonRouteMetric1 = _FsRtmCommonRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 11),
    _FsRtmCommonRouteMetric1_Type()
)
fsRtmCommonRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRouteMetric1.setStatus("current")
_FsRtmCommonRoutePrivateStatus_Type = TruthValue
_FsRtmCommonRoutePrivateStatus_Object = MibTableColumn
fsRtmCommonRoutePrivateStatus = _FsRtmCommonRoutePrivateStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 12),
    _FsRtmCommonRoutePrivateStatus_Type()
)
fsRtmCommonRoutePrivateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRoutePrivateStatus.setStatus("current")
_FsRtmCommonRouteStatus_Type = RowStatus
_FsRtmCommonRouteStatus_Object = MibTableColumn
fsRtmCommonRouteStatus = _FsRtmCommonRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 13),
    _FsRtmCommonRouteStatus_Type()
)
fsRtmCommonRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRtmCommonRouteStatus.setStatus("current")


class _FsRtmCommonRoutePreference_Type(Integer32):
    """Custom type fsRtmCommonRoutePreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRtmCommonRoutePreference_Type.__name__ = "Integer32"
_FsRtmCommonRoutePreference_Object = MibTableColumn
fsRtmCommonRoutePreference = _FsRtmCommonRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 4, 1, 14),
    _FsRtmCommonRoutePreference_Type()
)
fsRtmCommonRoutePreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtmCommonRoutePreference.setStatus("current")
_FsRtmRedTest_ObjectIdentity = ObjectIdentity
fsRtmRedTest = _FsRtmRedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 107, 5)
)
_FsRtmRedEntryTime_Type = Integer32
_FsRtmRedEntryTime_Object = MibScalar
fsRtmRedEntryTime = _FsRtmRedEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 5, 1),
    _FsRtmRedEntryTime_Type()
)
fsRtmRedEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRtmRedEntryTime.setStatus("current")
_FsRtmRedExitTime_Type = Integer32
_FsRtmRedExitTime_Object = MibScalar
fsRtmRedExitTime = _FsRtmRedExitTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 107, 5, 2),
    _FsRtmRedExitTime_Type()
)
fsRtmRedExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRtmRedExitTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-RTM-MIB",
    **{"futurertm": futurertm,
       "fsrrdScalar": fsrrdScalar,
       "fsRrdRouterId": fsRrdRouterId,
       "fsRrdFilterByOspfTag": fsRrdFilterByOspfTag,
       "fsRrdFilterOspfTag": fsRrdFilterOspfTag,
       "fsRrdFilterOspfTagMask": fsRrdFilterOspfTagMask,
       "fsRrdRouterASNumber": fsRrdRouterASNumber,
       "fsRrdAdminStatus": fsRrdAdminStatus,
       "fsRtmThrottleLimit": fsRtmThrottleLimit,
       "fsRtmMaximumBgpRoutes": fsRtmMaximumBgpRoutes,
       "fsRtmMaximumOspfRoutes": fsRtmMaximumOspfRoutes,
       "fsRtmMaximumRipRoutes": fsRtmMaximumRipRoutes,
       "fsRtmMaximumStaticRoutes": fsRtmMaximumStaticRoutes,
       "fsRtmMaximumISISRoutes": fsRtmMaximumISISRoutes,
       "fsRtmIpStaticRouteDistance": fsRtmIpStaticRouteDistance,
       "fsEcmpAcrossProtocolAdminStatus": fsEcmpAcrossProtocolAdminStatus,
       "fsRtmRouteLeakStatus": fsRtmRouteLeakStatus,
       "fsRrdControlTable": fsRrdControlTable,
       "fsRrdControlEntry": fsRrdControlEntry,
       "fsRrdControlDestIpAddress": fsRrdControlDestIpAddress,
       "fsRrdControlNetMask": fsRrdControlNetMask,
       "fsRrdControlSourceProto": fsRrdControlSourceProto,
       "fsRrdControlDestProto": fsRrdControlDestProto,
       "fsRrdControlRouteExportFlag": fsRrdControlRouteExportFlag,
       "fsRrdControlRowStatus": fsRrdControlRowStatus,
       "fsRrdRoutingProtoTable": fsRrdRoutingProtoTable,
       "fsRrdRoutingProtoEntry": fsRrdRoutingProtoEntry,
       "fsRrdRoutingProtoId": fsRrdRoutingProtoId,
       "fsRrdRoutingRegnId": fsRrdRoutingRegnId,
       "fsRrdRoutingProtoTaskIdent": fsRrdRoutingProtoTaskIdent,
       "fsRrdRoutingProtoQueueIdent": fsRrdRoutingProtoQueueIdent,
       "fsRrdAllowOspfAreaRoutes": fsRrdAllowOspfAreaRoutes,
       "fsRrdAllowOspfExtRoutes": fsRrdAllowOspfExtRoutes,
       "fsRtmCommonRouteTable": fsRtmCommonRouteTable,
       "fsRtmCommonRouteEntry": fsRtmCommonRouteEntry,
       "fsRtmCommonRouteDest": fsRtmCommonRouteDest,
       "fsRtmCommonRouteMask": fsRtmCommonRouteMask,
       "fsRtmCommonRouteTos": fsRtmCommonRouteTos,
       "fsRtmCommonRouteNextHop": fsRtmCommonRouteNextHop,
       "fsRtmCommonRouteIfIndex": fsRtmCommonRouteIfIndex,
       "fsRtmCommonRouteType": fsRtmCommonRouteType,
       "fsRtmCommonRouteProto": fsRtmCommonRouteProto,
       "fsRtmCommonRouteAge": fsRtmCommonRouteAge,
       "fsRtmCommonRouteInfo": fsRtmCommonRouteInfo,
       "fsRtmCommonRouteNextHopAS": fsRtmCommonRouteNextHopAS,
       "fsRtmCommonRouteMetric1": fsRtmCommonRouteMetric1,
       "fsRtmCommonRoutePrivateStatus": fsRtmCommonRoutePrivateStatus,
       "fsRtmCommonRouteStatus": fsRtmCommonRouteStatus,
       "fsRtmCommonRoutePreference": fsRtmCommonRoutePreference,
       "fsRtmRedTest": fsRtmRedTest,
       "fsRtmRedEntryTime": fsRtmRedEntryTime,
       "fsRtmRedExitTime": fsRtmRedExitTime}
)
