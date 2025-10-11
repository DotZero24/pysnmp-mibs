# SNMP MIB module (ARICENT-RTM6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-RTM6-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:41 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futurertm6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 92)
)
if mibBuilder.loadTexts:
    futurertm6.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fsrrd6Scalar_ObjectIdentity = ObjectIdentity
fsrrd6Scalar = _Fsrrd6Scalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1)
)
_FsRrd6RouterId_Type = IpAddress
_FsRrd6RouterId_Object = MibScalar
fsRrd6RouterId = _FsRrd6RouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 1),
    _FsRrd6RouterId_Type()
)
fsRrd6RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6RouterId.setStatus("current")


class _FsRrd6FilterByOspfTag_Type(Integer32):
    """Custom type fsRrd6FilterByOspfTag based on Integer32"""
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


_FsRrd6FilterByOspfTag_Type.__name__ = "Integer32"
_FsRrd6FilterByOspfTag_Object = MibScalar
fsRrd6FilterByOspfTag = _FsRrd6FilterByOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 2),
    _FsRrd6FilterByOspfTag_Type()
)
fsRrd6FilterByOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6FilterByOspfTag.setStatus("current")
_FsRrd6FilterOspfTag_Type = Integer32
_FsRrd6FilterOspfTag_Object = MibScalar
fsRrd6FilterOspfTag = _FsRrd6FilterOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 3),
    _FsRrd6FilterOspfTag_Type()
)
fsRrd6FilterOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6FilterOspfTag.setStatus("current")


class _FsRrd6FilterOspfTagMask_Type(Integer32):
    """Custom type fsRrd6FilterOspfTagMask based on Integer32"""
    defaultValue = -1


_FsRrd6FilterOspfTagMask_Type.__name__ = "Integer32"
_FsRrd6FilterOspfTagMask_Object = MibScalar
fsRrd6FilterOspfTagMask = _FsRrd6FilterOspfTagMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 4),
    _FsRrd6FilterOspfTagMask_Type()
)
fsRrd6FilterOspfTagMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6FilterOspfTagMask.setStatus("current")


class _FsRrd6RouterASNumber_Type(Integer32):
    """Custom type fsRrd6RouterASNumber based on Integer32"""
    defaultValue = 0


_FsRrd6RouterASNumber_Type.__name__ = "Integer32"
_FsRrd6RouterASNumber_Object = MibScalar
fsRrd6RouterASNumber = _FsRrd6RouterASNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 5),
    _FsRrd6RouterASNumber_Type()
)
fsRrd6RouterASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6RouterASNumber.setStatus("current")


class _FsRrd6AdminStatus_Type(Integer32):
    """Custom type fsRrd6AdminStatus based on Integer32"""
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


_FsRrd6AdminStatus_Type.__name__ = "Integer32"
_FsRrd6AdminStatus_Object = MibScalar
fsRrd6AdminStatus = _FsRrd6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 6),
    _FsRrd6AdminStatus_Type()
)
fsRrd6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6AdminStatus.setStatus("current")
_FsRrd6Trace_Type = Unsigned32
_FsRrd6Trace_Object = MibScalar
fsRrd6Trace = _FsRrd6Trace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 7),
    _FsRrd6Trace_Type()
)
fsRrd6Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6Trace.setStatus("current")


class _FsRrd6ThrotLimit_Type(Unsigned32):
    """Custom type fsRrd6ThrotLimit based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsRrd6ThrotLimit_Type.__name__ = "Unsigned32"
_FsRrd6ThrotLimit_Object = MibScalar
fsRrd6ThrotLimit = _FsRrd6ThrotLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 8),
    _FsRrd6ThrotLimit_Type()
)
fsRrd6ThrotLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6ThrotLimit.setStatus("current")
_FsRrd6MaximumBgpRoutes_Type = Unsigned32
_FsRrd6MaximumBgpRoutes_Object = MibScalar
fsRrd6MaximumBgpRoutes = _FsRrd6MaximumBgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 9),
    _FsRrd6MaximumBgpRoutes_Type()
)
fsRrd6MaximumBgpRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6MaximumBgpRoutes.setStatus("current")
_FsRrd6MaximumOspfRoutes_Type = Unsigned32
_FsRrd6MaximumOspfRoutes_Object = MibScalar
fsRrd6MaximumOspfRoutes = _FsRrd6MaximumOspfRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 10),
    _FsRrd6MaximumOspfRoutes_Type()
)
fsRrd6MaximumOspfRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6MaximumOspfRoutes.setStatus("current")
_FsRrd6MaximumRipRoutes_Type = Unsigned32
_FsRrd6MaximumRipRoutes_Object = MibScalar
fsRrd6MaximumRipRoutes = _FsRrd6MaximumRipRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 11),
    _FsRrd6MaximumRipRoutes_Type()
)
fsRrd6MaximumRipRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6MaximumRipRoutes.setStatus("current")
_FsRrd6MaximumStaticRoutes_Type = Unsigned32
_FsRrd6MaximumStaticRoutes_Object = MibScalar
fsRrd6MaximumStaticRoutes = _FsRrd6MaximumStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 12),
    _FsRrd6MaximumStaticRoutes_Type()
)
fsRrd6MaximumStaticRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6MaximumStaticRoutes.setStatus("current")
_FsRrd6MaximumISISRoutes_Type = Unsigned32
_FsRrd6MaximumISISRoutes_Object = MibScalar
fsRrd6MaximumISISRoutes = _FsRrd6MaximumISISRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 13),
    _FsRrd6MaximumISISRoutes_Type()
)
fsRrd6MaximumISISRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6MaximumISISRoutes.setStatus("current")


class _FsRtm6StaticRouteDistance_Type(Integer32):
    """Custom type fsRtm6StaticRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsRtm6StaticRouteDistance_Type.__name__ = "Integer32"
_FsRtm6StaticRouteDistance_Object = MibScalar
fsRtm6StaticRouteDistance = _FsRtm6StaticRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 1, 14),
    _FsRtm6StaticRouteDistance_Type()
)
fsRtm6StaticRouteDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRtm6StaticRouteDistance.setStatus("current")
_FsRrd6ControlTable_Object = MibTable
fsRrd6ControlTable = _FsRrd6ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2)
)
if mibBuilder.loadTexts:
    fsRrd6ControlTable.setStatus("current")
_FsRrd6ControlEntry_Object = MibTableRow
fsRrd6ControlEntry = _FsRrd6ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1)
)
fsRrd6ControlEntry.setIndexNames(
    (0, "ARICENT-RTM6-MIB", "fsRrd6ControlDestIpAddress"),
    (0, "ARICENT-RTM6-MIB", "fsRrd6ControlNetMaskLen"),
)
if mibBuilder.loadTexts:
    fsRrd6ControlEntry.setStatus("current")


class _FsRrd6ControlDestIpAddress_Type(OctetString):
    """Custom type fsRrd6ControlDestIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsRrd6ControlDestIpAddress_Type.__name__ = "OctetString"
_FsRrd6ControlDestIpAddress_Object = MibTableColumn
fsRrd6ControlDestIpAddress = _FsRrd6ControlDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1, 1),
    _FsRrd6ControlDestIpAddress_Type()
)
fsRrd6ControlDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrd6ControlDestIpAddress.setStatus("current")


class _FsRrd6ControlNetMaskLen_Type(Integer32):
    """Custom type fsRrd6ControlNetMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FsRrd6ControlNetMaskLen_Type.__name__ = "Integer32"
_FsRrd6ControlNetMaskLen_Object = MibTableColumn
fsRrd6ControlNetMaskLen = _FsRrd6ControlNetMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1, 2),
    _FsRrd6ControlNetMaskLen_Type()
)
fsRrd6ControlNetMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrd6ControlNetMaskLen.setStatus("current")


class _FsRrd6ControlSourceProto_Type(Integer32):
    """Custom type fsRrd6ControlSourceProto based on Integer32"""
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
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("ndisc", 4),
          ("rip", 5),
          ("ospf", 6),
          ("bgp", 7),
          ("idrp", 8),
          ("igrp", 9))
    )


_FsRrd6ControlSourceProto_Type.__name__ = "Integer32"
_FsRrd6ControlSourceProto_Object = MibTableColumn
fsRrd6ControlSourceProto = _FsRrd6ControlSourceProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1, 3),
    _FsRrd6ControlSourceProto_Type()
)
fsRrd6ControlSourceProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6ControlSourceProto.setStatus("current")


class _FsRrd6ControlDestProto_Type(Integer32):
    """Custom type fsRrd6ControlDestProto based on Integer32"""
    defaultValue = 0


_FsRrd6ControlDestProto_Type.__name__ = "Integer32"
_FsRrd6ControlDestProto_Object = MibTableColumn
fsRrd6ControlDestProto = _FsRrd6ControlDestProto_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1, 4),
    _FsRrd6ControlDestProto_Type()
)
fsRrd6ControlDestProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6ControlDestProto.setStatus("current")


class _FsRrd6ControlRouteExportFlag_Type(Integer32):
    """Custom type fsRrd6ControlRouteExportFlag based on Integer32"""
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


_FsRrd6ControlRouteExportFlag_Type.__name__ = "Integer32"
_FsRrd6ControlRouteExportFlag_Object = MibTableColumn
fsRrd6ControlRouteExportFlag = _FsRrd6ControlRouteExportFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1, 5),
    _FsRrd6ControlRouteExportFlag_Type()
)
fsRrd6ControlRouteExportFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6ControlRouteExportFlag.setStatus("current")
_FsRrd6ControlRowStatus_Type = RowStatus
_FsRrd6ControlRowStatus_Object = MibTableColumn
fsRrd6ControlRowStatus = _FsRrd6ControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 2, 1, 6),
    _FsRrd6ControlRowStatus_Type()
)
fsRrd6ControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6ControlRowStatus.setStatus("current")
_FsRrd6RoutingProtoTable_Object = MibTable
fsRrd6RoutingProtoTable = _FsRrd6RoutingProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3)
)
if mibBuilder.loadTexts:
    fsRrd6RoutingProtoTable.setStatus("current")
_FsRrd6RoutingProtoEntry_Object = MibTableRow
fsRrd6RoutingProtoEntry = _FsRrd6RoutingProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1)
)
fsRrd6RoutingProtoEntry.setIndexNames(
    (0, "ARICENT-RTM6-MIB", "fsRrd6RoutingProtoId"),
)
if mibBuilder.loadTexts:
    fsRrd6RoutingProtoEntry.setStatus("current")


class _FsRrd6RoutingProtoId_Type(Integer32):
    """Custom type fsRrd6RoutingProtoId based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("ndisc", 4),
          ("rip", 5),
          ("ospf", 6),
          ("bgp", 7),
          ("idrp", 8),
          ("igrp", 9))
    )


_FsRrd6RoutingProtoId_Type.__name__ = "Integer32"
_FsRrd6RoutingProtoId_Object = MibTableColumn
fsRrd6RoutingProtoId = _FsRrd6RoutingProtoId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1, 1),
    _FsRrd6RoutingProtoId_Type()
)
fsRrd6RoutingProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrd6RoutingProtoId.setStatus("current")
_FsRrd6RoutingRegnId_Type = Integer32
_FsRrd6RoutingRegnId_Object = MibTableColumn
fsRrd6RoutingRegnId = _FsRrd6RoutingRegnId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1, 2),
    _FsRrd6RoutingRegnId_Type()
)
fsRrd6RoutingRegnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrd6RoutingRegnId.setStatus("current")
_FsRrd6RoutingProtoTaskIdent_Type = OctetString
_FsRrd6RoutingProtoTaskIdent_Object = MibTableColumn
fsRrd6RoutingProtoTaskIdent = _FsRrd6RoutingProtoTaskIdent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1, 3),
    _FsRrd6RoutingProtoTaskIdent_Type()
)
fsRrd6RoutingProtoTaskIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrd6RoutingProtoTaskIdent.setStatus("current")
_FsRrd6RoutingProtoQueueIdent_Type = OctetString
_FsRrd6RoutingProtoQueueIdent_Object = MibTableColumn
fsRrd6RoutingProtoQueueIdent = _FsRrd6RoutingProtoQueueIdent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1, 4),
    _FsRrd6RoutingProtoQueueIdent_Type()
)
fsRrd6RoutingProtoQueueIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRrd6RoutingProtoQueueIdent.setStatus("current")


class _FsRrd6AllowOspfAreaRoutes_Type(Integer32):
    """Custom type fsRrd6AllowOspfAreaRoutes based on Integer32"""
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


_FsRrd6AllowOspfAreaRoutes_Type.__name__ = "Integer32"
_FsRrd6AllowOspfAreaRoutes_Object = MibTableColumn
fsRrd6AllowOspfAreaRoutes = _FsRrd6AllowOspfAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1, 5),
    _FsRrd6AllowOspfAreaRoutes_Type()
)
fsRrd6AllowOspfAreaRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6AllowOspfAreaRoutes.setStatus("current")


class _FsRrd6AllowOspfExtRoutes_Type(Integer32):
    """Custom type fsRrd6AllowOspfExtRoutes based on Integer32"""
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


_FsRrd6AllowOspfExtRoutes_Type.__name__ = "Integer32"
_FsRrd6AllowOspfExtRoutes_Object = MibTableColumn
fsRrd6AllowOspfExtRoutes = _FsRrd6AllowOspfExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 3, 1, 6),
    _FsRrd6AllowOspfExtRoutes_Type()
)
fsRrd6AllowOspfExtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrd6AllowOspfExtRoutes.setStatus("current")
_FsRtm6RedTest_ObjectIdentity = ObjectIdentity
fsRtm6RedTest = _FsRtm6RedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 92, 4)
)
_FsRtm6RedEntryTime_Type = Integer32
_FsRtm6RedEntryTime_Object = MibScalar
fsRtm6RedEntryTime = _FsRtm6RedEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 4, 1),
    _FsRtm6RedEntryTime_Type()
)
fsRtm6RedEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRtm6RedEntryTime.setStatus("current")
_FsRtm6RedExitTime_Type = Integer32
_FsRtm6RedExitTime_Object = MibScalar
fsRtm6RedExitTime = _FsRtm6RedExitTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 92, 4, 2),
    _FsRtm6RedExitTime_Type()
)
fsRtm6RedExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRtm6RedExitTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-RTM6-MIB",
    **{"futurertm6": futurertm6,
       "fsrrd6Scalar": fsrrd6Scalar,
       "fsRrd6RouterId": fsRrd6RouterId,
       "fsRrd6FilterByOspfTag": fsRrd6FilterByOspfTag,
       "fsRrd6FilterOspfTag": fsRrd6FilterOspfTag,
       "fsRrd6FilterOspfTagMask": fsRrd6FilterOspfTagMask,
       "fsRrd6RouterASNumber": fsRrd6RouterASNumber,
       "fsRrd6AdminStatus": fsRrd6AdminStatus,
       "fsRrd6Trace": fsRrd6Trace,
       "fsRrd6ThrotLimit": fsRrd6ThrotLimit,
       "fsRrd6MaximumBgpRoutes": fsRrd6MaximumBgpRoutes,
       "fsRrd6MaximumOspfRoutes": fsRrd6MaximumOspfRoutes,
       "fsRrd6MaximumRipRoutes": fsRrd6MaximumRipRoutes,
       "fsRrd6MaximumStaticRoutes": fsRrd6MaximumStaticRoutes,
       "fsRrd6MaximumISISRoutes": fsRrd6MaximumISISRoutes,
       "fsRtm6StaticRouteDistance": fsRtm6StaticRouteDistance,
       "fsRrd6ControlTable": fsRrd6ControlTable,
       "fsRrd6ControlEntry": fsRrd6ControlEntry,
       "fsRrd6ControlDestIpAddress": fsRrd6ControlDestIpAddress,
       "fsRrd6ControlNetMaskLen": fsRrd6ControlNetMaskLen,
       "fsRrd6ControlSourceProto": fsRrd6ControlSourceProto,
       "fsRrd6ControlDestProto": fsRrd6ControlDestProto,
       "fsRrd6ControlRouteExportFlag": fsRrd6ControlRouteExportFlag,
       "fsRrd6ControlRowStatus": fsRrd6ControlRowStatus,
       "fsRrd6RoutingProtoTable": fsRrd6RoutingProtoTable,
       "fsRrd6RoutingProtoEntry": fsRrd6RoutingProtoEntry,
       "fsRrd6RoutingProtoId": fsRrd6RoutingProtoId,
       "fsRrd6RoutingRegnId": fsRrd6RoutingRegnId,
       "fsRrd6RoutingProtoTaskIdent": fsRrd6RoutingProtoTaskIdent,
       "fsRrd6RoutingProtoQueueIdent": fsRrd6RoutingProtoQueueIdent,
       "fsRrd6AllowOspfAreaRoutes": fsRrd6AllowOspfAreaRoutes,
       "fsRrd6AllowOspfExtRoutes": fsRrd6AllowOspfExtRoutes,
       "fsRtm6RedTest": fsRtm6RedTest,
       "fsRtm6RedEntryTime": fsRtm6RedEntryTime,
       "fsRtm6RedExitTime": fsRtm6RedExitTime}
)
