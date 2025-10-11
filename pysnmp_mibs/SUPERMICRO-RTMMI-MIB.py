# SNMP MIB module (SUPERMICRO-RTMMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RTMMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:35 2025
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

fsMIRtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31)
)
if mibBuilder.loadTexts:
    fsMIRtm.setRevisions(
        ("2012-09-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIRtmGeneralGroup_ObjectIdentity = ObjectIdentity
fsMIRtmGeneralGroup = _FsMIRtmGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 1)
)


class _FsMIRtmThrottleLimit_Type(Unsigned32):
    """Custom type fsMIRtmThrottleLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIRtmThrottleLimit_Type.__name__ = "Unsigned32"
_FsMIRtmThrottleLimit_Object = MibScalar
fsMIRtmThrottleLimit = _FsMIRtmThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 1, 1),
    _FsMIRtmThrottleLimit_Type()
)
fsMIRtmThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRtmThrottleLimit.setStatus("current")
_FsMIRtmTable_Object = MibTable
fsMIRtmTable = _FsMIRtmTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2)
)
if mibBuilder.loadTexts:
    fsMIRtmTable.setStatus("current")
_FsMIRtmEntry_Object = MibTableRow
fsMIRtmEntry = _FsMIRtmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1)
)
fsMIRtmEntry.setIndexNames(
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmContextId"),
)
if mibBuilder.loadTexts:
    fsMIRtmEntry.setStatus("current")


class _FsMIRtmContextId_Type(Integer32):
    """Custom type fsMIRtmContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_FsMIRtmContextId_Type.__name__ = "Integer32"
_FsMIRtmContextId_Object = MibTableColumn
fsMIRtmContextId = _FsMIRtmContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 1),
    _FsMIRtmContextId_Type()
)
fsMIRtmContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtmContextId.setStatus("current")
_FsMIRrdRouterId_Type = IpAddress
_FsMIRrdRouterId_Object = MibTableColumn
fsMIRrdRouterId = _FsMIRrdRouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 2),
    _FsMIRrdRouterId_Type()
)
fsMIRrdRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdRouterId.setStatus("current")


class _FsMIRrdFilterByOspfTag_Type(Integer32):
    """Custom type fsMIRrdFilterByOspfTag based on Integer32"""
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


_FsMIRrdFilterByOspfTag_Type.__name__ = "Integer32"
_FsMIRrdFilterByOspfTag_Object = MibTableColumn
fsMIRrdFilterByOspfTag = _FsMIRrdFilterByOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 3),
    _FsMIRrdFilterByOspfTag_Type()
)
fsMIRrdFilterByOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdFilterByOspfTag.setStatus("current")
_FsMIRrdFilterOspfTag_Type = Integer32
_FsMIRrdFilterOspfTag_Object = MibTableColumn
fsMIRrdFilterOspfTag = _FsMIRrdFilterOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 4),
    _FsMIRrdFilterOspfTag_Type()
)
fsMIRrdFilterOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdFilterOspfTag.setStatus("current")


class _FsMIRrdFilterOspfTagMask_Type(Integer32):
    """Custom type fsMIRrdFilterOspfTagMask based on Integer32"""
    defaultValue = -1


_FsMIRrdFilterOspfTagMask_Type.__name__ = "Integer32"
_FsMIRrdFilterOspfTagMask_Object = MibTableColumn
fsMIRrdFilterOspfTagMask = _FsMIRrdFilterOspfTagMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 5),
    _FsMIRrdFilterOspfTagMask_Type()
)
fsMIRrdFilterOspfTagMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdFilterOspfTagMask.setStatus("current")


class _FsMIRrdRouterASNumber_Type(Integer32):
    """Custom type fsMIRrdRouterASNumber based on Integer32"""
    defaultValue = 0


_FsMIRrdRouterASNumber_Type.__name__ = "Integer32"
_FsMIRrdRouterASNumber_Object = MibTableColumn
fsMIRrdRouterASNumber = _FsMIRrdRouterASNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 6),
    _FsMIRrdRouterASNumber_Type()
)
fsMIRrdRouterASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdRouterASNumber.setStatus("current")


class _FsMIRrdAdminStatus_Type(Integer32):
    """Custom type fsMIRrdAdminStatus based on Integer32"""
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


_FsMIRrdAdminStatus_Type.__name__ = "Integer32"
_FsMIRrdAdminStatus_Object = MibTableColumn
fsMIRrdAdminStatus = _FsMIRrdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 7),
    _FsMIRrdAdminStatus_Type()
)
fsMIRrdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdAdminStatus.setStatus("current")


class _FsMIRrdForce_Type(Integer32):
    """Custom type fsMIRrdForce based on Integer32"""
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


_FsMIRrdForce_Type.__name__ = "Integer32"
_FsMIRrdForce_Object = MibTableColumn
fsMIRrdForce = _FsMIRrdForce_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 2, 1, 8),
    _FsMIRrdForce_Type()
)
fsMIRrdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdForce.setStatus("current")
_FsMIRrdControlTable_Object = MibTable
fsMIRrdControlTable = _FsMIRrdControlTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3)
)
if mibBuilder.loadTexts:
    fsMIRrdControlTable.setStatus("current")
_FsMIRrdControlEntry_Object = MibTableRow
fsMIRrdControlEntry = _FsMIRrdControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1)
)
fsMIRrdControlEntry.setIndexNames(
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmContextId"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRrdControlDestIpAddress"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRrdControlNetMask"),
)
if mibBuilder.loadTexts:
    fsMIRrdControlEntry.setStatus("current")
_FsMIRrdControlDestIpAddress_Type = IpAddress
_FsMIRrdControlDestIpAddress_Object = MibTableColumn
fsMIRrdControlDestIpAddress = _FsMIRrdControlDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1, 1),
    _FsMIRrdControlDestIpAddress_Type()
)
fsMIRrdControlDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRrdControlDestIpAddress.setStatus("current")
_FsMIRrdControlNetMask_Type = IpAddress
_FsMIRrdControlNetMask_Object = MibTableColumn
fsMIRrdControlNetMask = _FsMIRrdControlNetMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1, 2),
    _FsMIRrdControlNetMask_Type()
)
fsMIRrdControlNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRrdControlNetMask.setStatus("current")


class _FsMIRrdControlSourceProto_Type(Integer32):
    """Custom type fsMIRrdControlSourceProto based on Integer32"""
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


_FsMIRrdControlSourceProto_Type.__name__ = "Integer32"
_FsMIRrdControlSourceProto_Object = MibTableColumn
fsMIRrdControlSourceProto = _FsMIRrdControlSourceProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1, 3),
    _FsMIRrdControlSourceProto_Type()
)
fsMIRrdControlSourceProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdControlSourceProto.setStatus("current")


class _FsMIRrdControlDestProto_Type(Integer32):
    """Custom type fsMIRrdControlDestProto based on Integer32"""
    defaultValue = 0


_FsMIRrdControlDestProto_Type.__name__ = "Integer32"
_FsMIRrdControlDestProto_Object = MibTableColumn
fsMIRrdControlDestProto = _FsMIRrdControlDestProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1, 4),
    _FsMIRrdControlDestProto_Type()
)
fsMIRrdControlDestProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdControlDestProto.setStatus("current")


class _FsMIRrdControlRouteExportFlag_Type(Integer32):
    """Custom type fsMIRrdControlRouteExportFlag based on Integer32"""
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


_FsMIRrdControlRouteExportFlag_Type.__name__ = "Integer32"
_FsMIRrdControlRouteExportFlag_Object = MibTableColumn
fsMIRrdControlRouteExportFlag = _FsMIRrdControlRouteExportFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1, 5),
    _FsMIRrdControlRouteExportFlag_Type()
)
fsMIRrdControlRouteExportFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdControlRouteExportFlag.setStatus("current")
_FsMIRrdControlRowStatus_Type = RowStatus
_FsMIRrdControlRowStatus_Object = MibTableColumn
fsMIRrdControlRowStatus = _FsMIRrdControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 3, 1, 6),
    _FsMIRrdControlRowStatus_Type()
)
fsMIRrdControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdControlRowStatus.setStatus("current")
_FsMIRrdRoutingProtoTable_Object = MibTable
fsMIRrdRoutingProtoTable = _FsMIRrdRoutingProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4)
)
if mibBuilder.loadTexts:
    fsMIRrdRoutingProtoTable.setStatus("current")
_FsMIRrdRoutingProtoEntry_Object = MibTableRow
fsMIRrdRoutingProtoEntry = _FsMIRrdRoutingProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1)
)
fsMIRrdRoutingProtoEntry.setIndexNames(
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmContextId"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRrdRoutingProtoId"),
)
if mibBuilder.loadTexts:
    fsMIRrdRoutingProtoEntry.setStatus("current")


class _FsMIRrdRoutingProtoId_Type(Integer32):
    """Custom type fsMIRrdRoutingProtoId based on Integer32"""
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


_FsMIRrdRoutingProtoId_Type.__name__ = "Integer32"
_FsMIRrdRoutingProtoId_Object = MibTableColumn
fsMIRrdRoutingProtoId = _FsMIRrdRoutingProtoId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1, 1),
    _FsMIRrdRoutingProtoId_Type()
)
fsMIRrdRoutingProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRrdRoutingProtoId.setStatus("current")
_FsMIRrdRoutingRegnId_Type = Integer32
_FsMIRrdRoutingRegnId_Object = MibTableColumn
fsMIRrdRoutingRegnId = _FsMIRrdRoutingRegnId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1, 2),
    _FsMIRrdRoutingRegnId_Type()
)
fsMIRrdRoutingRegnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRrdRoutingRegnId.setStatus("current")
_FsMIRrdRoutingProtoTaskIdent_Type = OctetString
_FsMIRrdRoutingProtoTaskIdent_Object = MibTableColumn
fsMIRrdRoutingProtoTaskIdent = _FsMIRrdRoutingProtoTaskIdent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1, 3),
    _FsMIRrdRoutingProtoTaskIdent_Type()
)
fsMIRrdRoutingProtoTaskIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRrdRoutingProtoTaskIdent.setStatus("current")
_FsMIRrdRoutingProtoQueueIdent_Type = OctetString
_FsMIRrdRoutingProtoQueueIdent_Object = MibTableColumn
fsMIRrdRoutingProtoQueueIdent = _FsMIRrdRoutingProtoQueueIdent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1, 4),
    _FsMIRrdRoutingProtoQueueIdent_Type()
)
fsMIRrdRoutingProtoQueueIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRrdRoutingProtoQueueIdent.setStatus("current")


class _FsMIRrdAllowOspfAreaRoutes_Type(Integer32):
    """Custom type fsMIRrdAllowOspfAreaRoutes based on Integer32"""
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


_FsMIRrdAllowOspfAreaRoutes_Type.__name__ = "Integer32"
_FsMIRrdAllowOspfAreaRoutes_Object = MibTableColumn
fsMIRrdAllowOspfAreaRoutes = _FsMIRrdAllowOspfAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1, 5),
    _FsMIRrdAllowOspfAreaRoutes_Type()
)
fsMIRrdAllowOspfAreaRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdAllowOspfAreaRoutes.setStatus("current")


class _FsMIRrdAllowOspfExtRoutes_Type(Integer32):
    """Custom type fsMIRrdAllowOspfExtRoutes based on Integer32"""
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


_FsMIRrdAllowOspfExtRoutes_Type.__name__ = "Integer32"
_FsMIRrdAllowOspfExtRoutes_Object = MibTableColumn
fsMIRrdAllowOspfExtRoutes = _FsMIRrdAllowOspfExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 4, 1, 6),
    _FsMIRrdAllowOspfExtRoutes_Type()
)
fsMIRrdAllowOspfExtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrdAllowOspfExtRoutes.setStatus("current")
_FsMIRtmCommonRouteTable_Object = MibTable
fsMIRtmCommonRouteTable = _FsMIRtmCommonRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5)
)
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteTable.setStatus("current")
_FsMIRtmCommonRouteEntry_Object = MibTableRow
fsMIRtmCommonRouteEntry = _FsMIRtmCommonRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1)
)
fsMIRtmCommonRouteEntry.setIndexNames(
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmContextId"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmCommonRouteDest"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmCommonRouteMask"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmCommonRouteTos"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmCommonRouteNextHop"),
)
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteEntry.setStatus("current")
_FsMIRtmCommonRouteDest_Type = IpAddress
_FsMIRtmCommonRouteDest_Object = MibTableColumn
fsMIRtmCommonRouteDest = _FsMIRtmCommonRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 1),
    _FsMIRtmCommonRouteDest_Type()
)
fsMIRtmCommonRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteDest.setStatus("current")
_FsMIRtmCommonRouteMask_Type = IpAddress
_FsMIRtmCommonRouteMask_Object = MibTableColumn
fsMIRtmCommonRouteMask = _FsMIRtmCommonRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 2),
    _FsMIRtmCommonRouteMask_Type()
)
fsMIRtmCommonRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteMask.setStatus("current")


class _FsMIRtmCommonRouteTos_Type(Integer32):
    """Custom type fsMIRtmCommonRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIRtmCommonRouteTos_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteTos_Object = MibTableColumn
fsMIRtmCommonRouteTos = _FsMIRtmCommonRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 3),
    _FsMIRtmCommonRouteTos_Type()
)
fsMIRtmCommonRouteTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteTos.setStatus("current")
_FsMIRtmCommonRouteNextHop_Type = IpAddress
_FsMIRtmCommonRouteNextHop_Object = MibTableColumn
fsMIRtmCommonRouteNextHop = _FsMIRtmCommonRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 4),
    _FsMIRtmCommonRouteNextHop_Type()
)
fsMIRtmCommonRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteNextHop.setStatus("current")


class _FsMIRtmCommonRouteIfIndex_Type(Integer32):
    """Custom type fsMIRtmCommonRouteIfIndex based on Integer32"""
    defaultValue = 0


_FsMIRtmCommonRouteIfIndex_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteIfIndex_Object = MibTableColumn
fsMIRtmCommonRouteIfIndex = _FsMIRtmCommonRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 5),
    _FsMIRtmCommonRouteIfIndex_Type()
)
fsMIRtmCommonRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteIfIndex.setStatus("current")


class _FsMIRtmCommonRouteType_Type(Integer32):
    """Custom type fsMIRtmCommonRouteType based on Integer32"""
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


_FsMIRtmCommonRouteType_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteType_Object = MibTableColumn
fsMIRtmCommonRouteType = _FsMIRtmCommonRouteType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 6),
    _FsMIRtmCommonRouteType_Type()
)
fsMIRtmCommonRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteType.setStatus("current")


class _FsMIRtmCommonRouteProto_Type(Integer32):
    """Custom type fsMIRtmCommonRouteProto based on Integer32"""
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


_FsMIRtmCommonRouteProto_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteProto_Object = MibTableColumn
fsMIRtmCommonRouteProto = _FsMIRtmCommonRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 7),
    _FsMIRtmCommonRouteProto_Type()
)
fsMIRtmCommonRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteProto.setStatus("current")


class _FsMIRtmCommonRouteAge_Type(Integer32):
    """Custom type fsMIRtmCommonRouteAge based on Integer32"""
    defaultValue = 0


_FsMIRtmCommonRouteAge_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteAge_Object = MibTableColumn
fsMIRtmCommonRouteAge = _FsMIRtmCommonRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 8),
    _FsMIRtmCommonRouteAge_Type()
)
fsMIRtmCommonRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteAge.setStatus("current")
_FsMIRtmCommonRouteInfo_Type = ObjectIdentifier
_FsMIRtmCommonRouteInfo_Object = MibTableColumn
fsMIRtmCommonRouteInfo = _FsMIRtmCommonRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 9),
    _FsMIRtmCommonRouteInfo_Type()
)
fsMIRtmCommonRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteInfo.setStatus("current")


class _FsMIRtmCommonRouteNextHopAS_Type(Integer32):
    """Custom type fsMIRtmCommonRouteNextHopAS based on Integer32"""
    defaultValue = 0


_FsMIRtmCommonRouteNextHopAS_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteNextHopAS_Object = MibTableColumn
fsMIRtmCommonRouteNextHopAS = _FsMIRtmCommonRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 10),
    _FsMIRtmCommonRouteNextHopAS_Type()
)
fsMIRtmCommonRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteNextHopAS.setStatus("current")


class _FsMIRtmCommonRouteMetric1_Type(Integer32):
    """Custom type fsMIRtmCommonRouteMetric1 based on Integer32"""
    defaultValue = -1


_FsMIRtmCommonRouteMetric1_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteMetric1_Object = MibTableColumn
fsMIRtmCommonRouteMetric1 = _FsMIRtmCommonRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 11),
    _FsMIRtmCommonRouteMetric1_Type()
)
fsMIRtmCommonRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteMetric1.setStatus("current")
_FsMIRtmCommonRoutePrivateStatus_Type = TruthValue
_FsMIRtmCommonRoutePrivateStatus_Object = MibTableColumn
fsMIRtmCommonRoutePrivateStatus = _FsMIRtmCommonRoutePrivateStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 12),
    _FsMIRtmCommonRoutePrivateStatus_Type()
)
fsMIRtmCommonRoutePrivateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRoutePrivateStatus.setStatus("current")
_FsMIRtmCommonRouteStatus_Type = RowStatus
_FsMIRtmCommonRouteStatus_Object = MibTableColumn
fsMIRtmCommonRouteStatus = _FsMIRtmCommonRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 13),
    _FsMIRtmCommonRouteStatus_Type()
)
fsMIRtmCommonRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteStatus.setStatus("current")


class _FsMIRtmCommonRouteProvider_Type(Integer32):
    """Custom type fsMIRtmCommonRouteProvider based on Integer32"""
    defaultValue = 0


_FsMIRtmCommonRouteProvider_Type.__name__ = "Integer32"
_FsMIRtmCommonRouteProvider_Object = MibTableColumn
fsMIRtmCommonRouteProvider = _FsMIRtmCommonRouteProvider_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 5, 1, 14),
    _FsMIRtmCommonRouteProvider_Type()
)
fsMIRtmCommonRouteProvider.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRtmCommonRouteProvider.setStatus("current")
_FsMIRtmRedTest_ObjectIdentity = ObjectIdentity
fsMIRtmRedTest = _FsMIRtmRedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 6)
)
_FsMIRtmRedEntryTime_Type = Integer32
_FsMIRtmRedEntryTime_Object = MibScalar
fsMIRtmRedEntryTime = _FsMIRtmRedEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 6, 1),
    _FsMIRtmRedEntryTime_Type()
)
fsMIRtmRedEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRtmRedEntryTime.setStatus("current")
_FsMIRtmRedExitTime_Type = Integer32
_FsMIRtmRedExitTime_Object = MibScalar
fsMIRtmRedExitTime = _FsMIRtmRedExitTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 6, 2),
    _FsMIRtmRedExitTime_Type()
)
fsMIRtmRedExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRtmRedExitTime.setStatus("current")
_FsMIRtmPBRouteTable_Object = MibTable
fsMIRtmPBRouteTable = _FsMIRtmPBRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 7)
)
if mibBuilder.loadTexts:
    fsMIRtmPBRouteTable.setStatus("current")
_FsMIRtmPBRouteEntry_Object = MibTableRow
fsMIRtmPBRouteEntry = _FsMIRtmPBRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 7, 1)
)
fsMIRtmPBRouteEntry.setIndexNames(
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmContextId"),
    (0, "SUPERMICRO-RTMMI-MIB", "fsMIRtmPBRouteIfIndex"),
)
if mibBuilder.loadTexts:
    fsMIRtmPBRouteEntry.setStatus("current")


class _FsMIRtmPBRouteIfIndex_Type(Integer32):
    """Custom type fsMIRtmPBRouteIfIndex based on Integer32"""
    defaultValue = 0


_FsMIRtmPBRouteIfIndex_Type.__name__ = "Integer32"
_FsMIRtmPBRouteIfIndex_Object = MibTableColumn
fsMIRtmPBRouteIfIndex = _FsMIRtmPBRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 7, 1, 1),
    _FsMIRtmPBRouteIfIndex_Type()
)
fsMIRtmPBRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtmPBRouteIfIndex.setStatus("current")


class _FsMIRtmPBRouteMapName_Type(DisplayString):
    """Custom type fsMIRtmPBRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_FsMIRtmPBRouteMapName_Type.__name__ = "DisplayString"
_FsMIRtmPBRouteMapName_Object = MibTableColumn
fsMIRtmPBRouteMapName = _FsMIRtmPBRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 7, 1, 2),
    _FsMIRtmPBRouteMapName_Type()
)
fsMIRtmPBRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRtmPBRouteMapName.setStatus("current")
_FsMIRtmPBRouteEntryStatus_Type = RowStatus
_FsMIRtmPBRouteEntryStatus_Object = MibTableColumn
fsMIRtmPBRouteEntryStatus = _FsMIRtmPBRouteEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 31, 7, 1, 3),
    _FsMIRtmPBRouteEntryStatus_Type()
)
fsMIRtmPBRouteEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRtmPBRouteEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RTMMI-MIB",
    **{"fsMIRtm": fsMIRtm,
       "fsMIRtmGeneralGroup": fsMIRtmGeneralGroup,
       "fsMIRtmThrottleLimit": fsMIRtmThrottleLimit,
       "fsMIRtmTable": fsMIRtmTable,
       "fsMIRtmEntry": fsMIRtmEntry,
       "fsMIRtmContextId": fsMIRtmContextId,
       "fsMIRrdRouterId": fsMIRrdRouterId,
       "fsMIRrdFilterByOspfTag": fsMIRrdFilterByOspfTag,
       "fsMIRrdFilterOspfTag": fsMIRrdFilterOspfTag,
       "fsMIRrdFilterOspfTagMask": fsMIRrdFilterOspfTagMask,
       "fsMIRrdRouterASNumber": fsMIRrdRouterASNumber,
       "fsMIRrdAdminStatus": fsMIRrdAdminStatus,
       "fsMIRrdForce": fsMIRrdForce,
       "fsMIRrdControlTable": fsMIRrdControlTable,
       "fsMIRrdControlEntry": fsMIRrdControlEntry,
       "fsMIRrdControlDestIpAddress": fsMIRrdControlDestIpAddress,
       "fsMIRrdControlNetMask": fsMIRrdControlNetMask,
       "fsMIRrdControlSourceProto": fsMIRrdControlSourceProto,
       "fsMIRrdControlDestProto": fsMIRrdControlDestProto,
       "fsMIRrdControlRouteExportFlag": fsMIRrdControlRouteExportFlag,
       "fsMIRrdControlRowStatus": fsMIRrdControlRowStatus,
       "fsMIRrdRoutingProtoTable": fsMIRrdRoutingProtoTable,
       "fsMIRrdRoutingProtoEntry": fsMIRrdRoutingProtoEntry,
       "fsMIRrdRoutingProtoId": fsMIRrdRoutingProtoId,
       "fsMIRrdRoutingRegnId": fsMIRrdRoutingRegnId,
       "fsMIRrdRoutingProtoTaskIdent": fsMIRrdRoutingProtoTaskIdent,
       "fsMIRrdRoutingProtoQueueIdent": fsMIRrdRoutingProtoQueueIdent,
       "fsMIRrdAllowOspfAreaRoutes": fsMIRrdAllowOspfAreaRoutes,
       "fsMIRrdAllowOspfExtRoutes": fsMIRrdAllowOspfExtRoutes,
       "fsMIRtmCommonRouteTable": fsMIRtmCommonRouteTable,
       "fsMIRtmCommonRouteEntry": fsMIRtmCommonRouteEntry,
       "fsMIRtmCommonRouteDest": fsMIRtmCommonRouteDest,
       "fsMIRtmCommonRouteMask": fsMIRtmCommonRouteMask,
       "fsMIRtmCommonRouteTos": fsMIRtmCommonRouteTos,
       "fsMIRtmCommonRouteNextHop": fsMIRtmCommonRouteNextHop,
       "fsMIRtmCommonRouteIfIndex": fsMIRtmCommonRouteIfIndex,
       "fsMIRtmCommonRouteType": fsMIRtmCommonRouteType,
       "fsMIRtmCommonRouteProto": fsMIRtmCommonRouteProto,
       "fsMIRtmCommonRouteAge": fsMIRtmCommonRouteAge,
       "fsMIRtmCommonRouteInfo": fsMIRtmCommonRouteInfo,
       "fsMIRtmCommonRouteNextHopAS": fsMIRtmCommonRouteNextHopAS,
       "fsMIRtmCommonRouteMetric1": fsMIRtmCommonRouteMetric1,
       "fsMIRtmCommonRoutePrivateStatus": fsMIRtmCommonRoutePrivateStatus,
       "fsMIRtmCommonRouteStatus": fsMIRtmCommonRouteStatus,
       "fsMIRtmCommonRouteProvider": fsMIRtmCommonRouteProvider,
       "fsMIRtmRedTest": fsMIRtmRedTest,
       "fsMIRtmRedEntryTime": fsMIRtmRedEntryTime,
       "fsMIRtmRedExitTime": fsMIRtmRedExitTime,
       "fsMIRtmPBRouteTable": fsMIRtmPBRouteTable,
       "fsMIRtmPBRouteEntry": fsMIRtmPBRouteEntry,
       "fsMIRtmPBRouteIfIndex": fsMIRtmPBRouteIfIndex,
       "fsMIRtmPBRouteMapName": fsMIRtmPBRouteMapName,
       "fsMIRtmPBRouteEntryStatus": fsMIRtmPBRouteEntryStatus}
)
