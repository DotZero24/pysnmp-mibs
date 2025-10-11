# SNMP MIB module (SUPERMICRO-RTM6MI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RTM6MI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:55 2025
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

fsMIRtm6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32)
)
if mibBuilder.loadTexts:
    fsMIRtm6.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIRtm6Scalar_ObjectIdentity = ObjectIdentity
fsMIRtm6Scalar = _FsMIRtm6Scalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 1)
)
_FsMIRtm6GlobalTrace_Type = Unsigned32
_FsMIRtm6GlobalTrace_Object = MibScalar
fsMIRtm6GlobalTrace = _FsMIRtm6GlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 1, 1),
    _FsMIRtm6GlobalTrace_Type()
)
fsMIRtm6GlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRtm6GlobalTrace.setStatus("current")


class _FsMIRtm6ThrotLimit_Type(Unsigned32):
    """Custom type fsMIRtm6ThrotLimit based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMIRtm6ThrotLimit_Type.__name__ = "Unsigned32"
_FsMIRtm6ThrotLimit_Object = MibScalar
fsMIRtm6ThrotLimit = _FsMIRtm6ThrotLimit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 1, 2),
    _FsMIRtm6ThrotLimit_Type()
)
fsMIRtm6ThrotLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRtm6ThrotLimit.setStatus("current")
_FsMIRtm6Table_Object = MibTable
fsMIRtm6Table = _FsMIRtm6Table_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2)
)
if mibBuilder.loadTexts:
    fsMIRtm6Table.setStatus("current")
_FsMIRtm6Entry_Object = MibTableRow
fsMIRtm6Entry = _FsMIRtm6Entry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1)
)
fsMIRtm6Entry.setIndexNames(
    (0, "SUPERMICRO-RTM6MI-MIB", "fsMIRtm6ContextId"),
)
if mibBuilder.loadTexts:
    fsMIRtm6Entry.setStatus("current")


class _FsMIRtm6ContextId_Type(Integer32):
    """Custom type fsMIRtm6ContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_FsMIRtm6ContextId_Type.__name__ = "Integer32"
_FsMIRtm6ContextId_Object = MibTableColumn
fsMIRtm6ContextId = _FsMIRtm6ContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 1),
    _FsMIRtm6ContextId_Type()
)
fsMIRtm6ContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRtm6ContextId.setStatus("current")
_FsMIRrd6RouterId_Type = IpAddress
_FsMIRrd6RouterId_Object = MibTableColumn
fsMIRrd6RouterId = _FsMIRrd6RouterId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 2),
    _FsMIRrd6RouterId_Type()
)
fsMIRrd6RouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6RouterId.setStatus("current")


class _FsMIRrd6FilterByOspfTag_Type(Integer32):
    """Custom type fsMIRrd6FilterByOspfTag based on Integer32"""
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


_FsMIRrd6FilterByOspfTag_Type.__name__ = "Integer32"
_FsMIRrd6FilterByOspfTag_Object = MibTableColumn
fsMIRrd6FilterByOspfTag = _FsMIRrd6FilterByOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 3),
    _FsMIRrd6FilterByOspfTag_Type()
)
fsMIRrd6FilterByOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6FilterByOspfTag.setStatus("current")
_FsMIRrd6FilterOspfTag_Type = Integer32
_FsMIRrd6FilterOspfTag_Object = MibTableColumn
fsMIRrd6FilterOspfTag = _FsMIRrd6FilterOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 4),
    _FsMIRrd6FilterOspfTag_Type()
)
fsMIRrd6FilterOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6FilterOspfTag.setStatus("current")


class _FsMIRrd6FilterOspfTagMask_Type(Integer32):
    """Custom type fsMIRrd6FilterOspfTagMask based on Integer32"""
    defaultValue = -1


_FsMIRrd6FilterOspfTagMask_Type.__name__ = "Integer32"
_FsMIRrd6FilterOspfTagMask_Object = MibTableColumn
fsMIRrd6FilterOspfTagMask = _FsMIRrd6FilterOspfTagMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 5),
    _FsMIRrd6FilterOspfTagMask_Type()
)
fsMIRrd6FilterOspfTagMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6FilterOspfTagMask.setStatus("current")


class _FsMIRrd6RouterASNumber_Type(Integer32):
    """Custom type fsMIRrd6RouterASNumber based on Integer32"""
    defaultValue = 0


_FsMIRrd6RouterASNumber_Type.__name__ = "Integer32"
_FsMIRrd6RouterASNumber_Object = MibTableColumn
fsMIRrd6RouterASNumber = _FsMIRrd6RouterASNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 6),
    _FsMIRrd6RouterASNumber_Type()
)
fsMIRrd6RouterASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6RouterASNumber.setStatus("current")


class _FsMIRrd6AdminStatus_Type(Integer32):
    """Custom type fsMIRrd6AdminStatus based on Integer32"""
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


_FsMIRrd6AdminStatus_Type.__name__ = "Integer32"
_FsMIRrd6AdminStatus_Object = MibTableColumn
fsMIRrd6AdminStatus = _FsMIRrd6AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 7),
    _FsMIRrd6AdminStatus_Type()
)
fsMIRrd6AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6AdminStatus.setStatus("current")
_FsMIRrd6Trace_Type = Unsigned32
_FsMIRrd6Trace_Object = MibTableColumn
fsMIRrd6Trace = _FsMIRrd6Trace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 2, 1, 8),
    _FsMIRrd6Trace_Type()
)
fsMIRrd6Trace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6Trace.setStatus("current")
_FsMIRrd6ControlTable_Object = MibTable
fsMIRrd6ControlTable = _FsMIRrd6ControlTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3)
)
if mibBuilder.loadTexts:
    fsMIRrd6ControlTable.setStatus("current")
_FsMIRrd6ControlEntry_Object = MibTableRow
fsMIRrd6ControlEntry = _FsMIRrd6ControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1)
)
fsMIRrd6ControlEntry.setIndexNames(
    (0, "SUPERMICRO-RTM6MI-MIB", "fsMIRtm6ContextId"),
    (0, "SUPERMICRO-RTM6MI-MIB", "fsMIRrd6ControlDestIpAddress"),
    (0, "SUPERMICRO-RTM6MI-MIB", "fsMIRrd6ControlNetMaskLen"),
)
if mibBuilder.loadTexts:
    fsMIRrd6ControlEntry.setStatus("current")


class _FsMIRrd6ControlDestIpAddress_Type(OctetString):
    """Custom type fsMIRrd6ControlDestIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIRrd6ControlDestIpAddress_Type.__name__ = "OctetString"
_FsMIRrd6ControlDestIpAddress_Object = MibTableColumn
fsMIRrd6ControlDestIpAddress = _FsMIRrd6ControlDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1, 1),
    _FsMIRrd6ControlDestIpAddress_Type()
)
fsMIRrd6ControlDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRrd6ControlDestIpAddress.setStatus("current")


class _FsMIRrd6ControlNetMaskLen_Type(Integer32):
    """Custom type fsMIRrd6ControlNetMaskLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FsMIRrd6ControlNetMaskLen_Type.__name__ = "Integer32"
_FsMIRrd6ControlNetMaskLen_Object = MibTableColumn
fsMIRrd6ControlNetMaskLen = _FsMIRrd6ControlNetMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1, 2),
    _FsMIRrd6ControlNetMaskLen_Type()
)
fsMIRrd6ControlNetMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRrd6ControlNetMaskLen.setStatus("current")


class _FsMIRrd6ControlSourceProto_Type(Integer32):
    """Custom type fsMIRrd6ControlSourceProto based on Integer32"""
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


_FsMIRrd6ControlSourceProto_Type.__name__ = "Integer32"
_FsMIRrd6ControlSourceProto_Object = MibTableColumn
fsMIRrd6ControlSourceProto = _FsMIRrd6ControlSourceProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1, 3),
    _FsMIRrd6ControlSourceProto_Type()
)
fsMIRrd6ControlSourceProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6ControlSourceProto.setStatus("current")


class _FsMIRrd6ControlDestProto_Type(Integer32):
    """Custom type fsMIRrd6ControlDestProto based on Integer32"""
    defaultValue = 0


_FsMIRrd6ControlDestProto_Type.__name__ = "Integer32"
_FsMIRrd6ControlDestProto_Object = MibTableColumn
fsMIRrd6ControlDestProto = _FsMIRrd6ControlDestProto_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1, 4),
    _FsMIRrd6ControlDestProto_Type()
)
fsMIRrd6ControlDestProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6ControlDestProto.setStatus("current")


class _FsMIRrd6ControlRouteExportFlag_Type(Integer32):
    """Custom type fsMIRrd6ControlRouteExportFlag based on Integer32"""
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


_FsMIRrd6ControlRouteExportFlag_Type.__name__ = "Integer32"
_FsMIRrd6ControlRouteExportFlag_Object = MibTableColumn
fsMIRrd6ControlRouteExportFlag = _FsMIRrd6ControlRouteExportFlag_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1, 5),
    _FsMIRrd6ControlRouteExportFlag_Type()
)
fsMIRrd6ControlRouteExportFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6ControlRouteExportFlag.setStatus("current")
_FsMIRrd6ControlRowStatus_Type = RowStatus
_FsMIRrd6ControlRowStatus_Object = MibTableColumn
fsMIRrd6ControlRowStatus = _FsMIRrd6ControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 3, 1, 6),
    _FsMIRrd6ControlRowStatus_Type()
)
fsMIRrd6ControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6ControlRowStatus.setStatus("current")
_FsMIRrd6RoutingProtoTable_Object = MibTable
fsMIRrd6RoutingProtoTable = _FsMIRrd6RoutingProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4)
)
if mibBuilder.loadTexts:
    fsMIRrd6RoutingProtoTable.setStatus("current")
_FsMIRrd6RoutingProtoEntry_Object = MibTableRow
fsMIRrd6RoutingProtoEntry = _FsMIRrd6RoutingProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1)
)
fsMIRrd6RoutingProtoEntry.setIndexNames(
    (0, "SUPERMICRO-RTM6MI-MIB", "fsMIRtm6ContextId"),
    (0, "SUPERMICRO-RTM6MI-MIB", "fsMIRrd6RoutingProtoId"),
)
if mibBuilder.loadTexts:
    fsMIRrd6RoutingProtoEntry.setStatus("current")


class _FsMIRrd6RoutingProtoId_Type(Integer32):
    """Custom type fsMIRrd6RoutingProtoId based on Integer32"""
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


_FsMIRrd6RoutingProtoId_Type.__name__ = "Integer32"
_FsMIRrd6RoutingProtoId_Object = MibTableColumn
fsMIRrd6RoutingProtoId = _FsMIRrd6RoutingProtoId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1, 1),
    _FsMIRrd6RoutingProtoId_Type()
)
fsMIRrd6RoutingProtoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIRrd6RoutingProtoId.setStatus("current")
_FsMIRrd6RoutingRegnId_Type = Integer32
_FsMIRrd6RoutingRegnId_Object = MibTableColumn
fsMIRrd6RoutingRegnId = _FsMIRrd6RoutingRegnId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1, 2),
    _FsMIRrd6RoutingRegnId_Type()
)
fsMIRrd6RoutingRegnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRrd6RoutingRegnId.setStatus("current")
_FsMIRrd6RoutingProtoTaskIdent_Type = OctetString
_FsMIRrd6RoutingProtoTaskIdent_Object = MibTableColumn
fsMIRrd6RoutingProtoTaskIdent = _FsMIRrd6RoutingProtoTaskIdent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1, 3),
    _FsMIRrd6RoutingProtoTaskIdent_Type()
)
fsMIRrd6RoutingProtoTaskIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRrd6RoutingProtoTaskIdent.setStatus("current")
_FsMIRrd6RoutingProtoQueueIdent_Type = OctetString
_FsMIRrd6RoutingProtoQueueIdent_Object = MibTableColumn
fsMIRrd6RoutingProtoQueueIdent = _FsMIRrd6RoutingProtoQueueIdent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1, 4),
    _FsMIRrd6RoutingProtoQueueIdent_Type()
)
fsMIRrd6RoutingProtoQueueIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRrd6RoutingProtoQueueIdent.setStatus("current")


class _FsMIRrd6AllowOspfAreaRoutes_Type(Integer32):
    """Custom type fsMIRrd6AllowOspfAreaRoutes based on Integer32"""
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


_FsMIRrd6AllowOspfAreaRoutes_Type.__name__ = "Integer32"
_FsMIRrd6AllowOspfAreaRoutes_Object = MibTableColumn
fsMIRrd6AllowOspfAreaRoutes = _FsMIRrd6AllowOspfAreaRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1, 5),
    _FsMIRrd6AllowOspfAreaRoutes_Type()
)
fsMIRrd6AllowOspfAreaRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6AllowOspfAreaRoutes.setStatus("current")


class _FsMIRrd6AllowOspfExtRoutes_Type(Integer32):
    """Custom type fsMIRrd6AllowOspfExtRoutes based on Integer32"""
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


_FsMIRrd6AllowOspfExtRoutes_Type.__name__ = "Integer32"
_FsMIRrd6AllowOspfExtRoutes_Object = MibTableColumn
fsMIRrd6AllowOspfExtRoutes = _FsMIRrd6AllowOspfExtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 4, 1, 6),
    _FsMIRrd6AllowOspfExtRoutes_Type()
)
fsMIRrd6AllowOspfExtRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIRrd6AllowOspfExtRoutes.setStatus("current")
_FsMIRtm6RedTest_ObjectIdentity = ObjectIdentity
fsMIRtm6RedTest = _FsMIRtm6RedTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 5)
)
_FsMIRtm6RedEntryTime_Type = Integer32
_FsMIRtm6RedEntryTime_Object = MibScalar
fsMIRtm6RedEntryTime = _FsMIRtm6RedEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 5, 1),
    _FsMIRtm6RedEntryTime_Type()
)
fsMIRtm6RedEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRtm6RedEntryTime.setStatus("current")
_FsMIRtm6RedExitTime_Type = Integer32
_FsMIRtm6RedExitTime_Object = MibScalar
fsMIRtm6RedExitTime = _FsMIRtm6RedExitTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 32, 5, 2),
    _FsMIRtm6RedExitTime_Type()
)
fsMIRtm6RedExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIRtm6RedExitTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RTM6MI-MIB",
    **{"fsMIRtm6": fsMIRtm6,
       "fsMIRtm6Scalar": fsMIRtm6Scalar,
       "fsMIRtm6GlobalTrace": fsMIRtm6GlobalTrace,
       "fsMIRtm6ThrotLimit": fsMIRtm6ThrotLimit,
       "fsMIRtm6Table": fsMIRtm6Table,
       "fsMIRtm6Entry": fsMIRtm6Entry,
       "fsMIRtm6ContextId": fsMIRtm6ContextId,
       "fsMIRrd6RouterId": fsMIRrd6RouterId,
       "fsMIRrd6FilterByOspfTag": fsMIRrd6FilterByOspfTag,
       "fsMIRrd6FilterOspfTag": fsMIRrd6FilterOspfTag,
       "fsMIRrd6FilterOspfTagMask": fsMIRrd6FilterOspfTagMask,
       "fsMIRrd6RouterASNumber": fsMIRrd6RouterASNumber,
       "fsMIRrd6AdminStatus": fsMIRrd6AdminStatus,
       "fsMIRrd6Trace": fsMIRrd6Trace,
       "fsMIRrd6ControlTable": fsMIRrd6ControlTable,
       "fsMIRrd6ControlEntry": fsMIRrd6ControlEntry,
       "fsMIRrd6ControlDestIpAddress": fsMIRrd6ControlDestIpAddress,
       "fsMIRrd6ControlNetMaskLen": fsMIRrd6ControlNetMaskLen,
       "fsMIRrd6ControlSourceProto": fsMIRrd6ControlSourceProto,
       "fsMIRrd6ControlDestProto": fsMIRrd6ControlDestProto,
       "fsMIRrd6ControlRouteExportFlag": fsMIRrd6ControlRouteExportFlag,
       "fsMIRrd6ControlRowStatus": fsMIRrd6ControlRowStatus,
       "fsMIRrd6RoutingProtoTable": fsMIRrd6RoutingProtoTable,
       "fsMIRrd6RoutingProtoEntry": fsMIRrd6RoutingProtoEntry,
       "fsMIRrd6RoutingProtoId": fsMIRrd6RoutingProtoId,
       "fsMIRrd6RoutingRegnId": fsMIRrd6RoutingRegnId,
       "fsMIRrd6RoutingProtoTaskIdent": fsMIRrd6RoutingProtoTaskIdent,
       "fsMIRrd6RoutingProtoQueueIdent": fsMIRrd6RoutingProtoQueueIdent,
       "fsMIRrd6AllowOspfAreaRoutes": fsMIRrd6AllowOspfAreaRoutes,
       "fsMIRrd6AllowOspfExtRoutes": fsMIRrd6AllowOspfExtRoutes,
       "fsMIRtm6RedTest": fsMIRtm6RedTest,
       "fsMIRtm6RedEntryTime": fsMIRtm6RedEntryTime,
       "fsMIRtm6RedExitTime": fsMIRtm6RedExitTime}
)
