# SNMP MIB module (FS-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:28 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    fsPingMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPingMIBObjects_ObjectIdentity = ObjectIdentity
fsPingMIBObjects = _FsPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1)
)
_FsPingTable_Object = MibTable
fsPingTable = _FsPingTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsPingTable.setStatus("current")
_FsPingEntry_Object = MibTableRow
fsPingEntry = _FsPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1)
)
fsPingEntry.setIndexNames(
    (0, "FS-PING-MIB", "fsPingIndex"),
)
if mibBuilder.loadTexts:
    fsPingEntry.setStatus("current")


class _FsPingIndex_Type(Integer32):
    """Custom type fsPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsPingIndex_Type.__name__ = "Integer32"
_FsPingIndex_Object = MibTableColumn
fsPingIndex = _FsPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 1),
    _FsPingIndex_Type()
)
fsPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingIndex.setStatus("current")
_FsPingAddress_Type = IpAddress
_FsPingAddress_Object = MibTableColumn
fsPingAddress = _FsPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 2),
    _FsPingAddress_Type()
)
fsPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingAddress.setStatus("current")


class _FsPingDataLength_Type(Unsigned32):
    """Custom type fsPingDataLength based on Unsigned32"""
    defaultValue = 100


_FsPingDataLength_Type.__name__ = "Unsigned32"
_FsPingDataLength_Object = MibTableColumn
fsPingDataLength = _FsPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 3),
    _FsPingDataLength_Type()
)
fsPingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingDataLength.setStatus("current")


class _FsPingTimes_Type(Unsigned32):
    """Custom type fsPingTimes based on Unsigned32"""
    defaultValue = 5


_FsPingTimes_Type.__name__ = "Unsigned32"
_FsPingTimes_Object = MibTableColumn
fsPingTimes = _FsPingTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 4),
    _FsPingTimes_Type()
)
fsPingTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingTimes.setStatus("current")


class _FsPingTimeOuts_Type(Unsigned32):
    """Custom type fsPingTimeOuts based on Unsigned32"""
    defaultValue = 2000


_FsPingTimeOuts_Type.__name__ = "Unsigned32"
_FsPingTimeOuts_Object = MibTableColumn
fsPingTimeOuts = _FsPingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 5),
    _FsPingTimeOuts_Type()
)
fsPingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingTimeOuts.setStatus("current")
_FsPingReturns_Type = Unsigned32
_FsPingReturns_Object = MibTableColumn
fsPingReturns = _FsPingReturns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 6),
    _FsPingReturns_Type()
)
fsPingReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingReturns.setStatus("current")
_FsPingMaxTime_Type = Unsigned32
_FsPingMaxTime_Object = MibTableColumn
fsPingMaxTime = _FsPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 7),
    _FsPingMaxTime_Type()
)
fsPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingMaxTime.setStatus("current")
_FsPingAvTime_Type = Unsigned32
_FsPingAvTime_Object = MibTableColumn
fsPingAvTime = _FsPingAvTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 8),
    _FsPingAvTime_Type()
)
fsPingAvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingAvTime.setStatus("current")
_FsPingMinTime_Type = Unsigned32
_FsPingMinTime_Object = MibTableColumn
fsPingMinTime = _FsPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 9),
    _FsPingMinTime_Type()
)
fsPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingMinTime.setStatus("current")
_FsPingCompleted_Type = TruthValue
_FsPingCompleted_Object = MibTableColumn
fsPingCompleted = _FsPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 10),
    _FsPingCompleted_Type()
)
fsPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPingCompleted.setStatus("current")
_FsPingEntryStauts_Type = RowStatus
_FsPingEntryStauts_Object = MibTableColumn
fsPingEntryStauts = _FsPingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 11),
    _FsPingEntryStauts_Type()
)
fsPingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingEntryStauts.setStatus("current")
_FsPingSourceIp_Type = IpAddress
_FsPingSourceIp_Object = MibTableColumn
fsPingSourceIp = _FsPingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 12),
    _FsPingSourceIp_Type()
)
fsPingSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingSourceIp.setStatus("current")
_FsPingSourceInterfaceIndex_Type = IfIndex
_FsPingSourceInterfaceIndex_Object = MibTableColumn
fsPingSourceInterfaceIndex = _FsPingSourceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 13),
    _FsPingSourceInterfaceIndex_Type()
)
fsPingSourceInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingSourceInterfaceIndex.setStatus("current")


class _FsPingTypeOfService_Type(Unsigned32):
    """Custom type fsPingTypeOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsPingTypeOfService_Type.__name__ = "Unsigned32"
_FsPingTypeOfService_Object = MibTableColumn
fsPingTypeOfService = _FsPingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 1, 1, 1, 14),
    _FsPingTypeOfService_Type()
)
fsPingTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPingTypeOfService.setStatus("current")
_FsPingMIBConformance_ObjectIdentity = ObjectIdentity
fsPingMIBConformance = _FsPingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 2)
)
_FsPingMIBCompliances_ObjectIdentity = ObjectIdentity
fsPingMIBCompliances = _FsPingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 2, 1)
)
_FsPingMIBGroups_ObjectIdentity = ObjectIdentity
fsPingMIBGroups = _FsPingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 2, 2)
)
_TraceRouteMIBObjects_ObjectIdentity = ObjectIdentity
traceRouteMIBObjects = _TraceRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3)
)
_TraceRouteTable_Object = MibTable
traceRouteTable = _TraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    traceRouteTable.setStatus("current")
_TraceRouteEntry_Object = MibTableRow
traceRouteEntry = _TraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1)
)
traceRouteEntry.setIndexNames(
    (0, "FS-PING-MIB", "traceRouteIndex"),
)
if mibBuilder.loadTexts:
    traceRouteEntry.setStatus("current")


class _TraceRouteIndex_Type(Unsigned32):
    """Custom type traceRouteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TraceRouteIndex_Type.__name__ = "Unsigned32"
_TraceRouteIndex_Object = MibTableColumn
traceRouteIndex = _TraceRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1, 1),
    _TraceRouteIndex_Type()
)
traceRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteIndex.setStatus("current")
_TraceRouteTargetAddr_Type = IpAddress
_TraceRouteTargetAddr_Object = MibTableColumn
traceRouteTargetAddr = _TraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1, 2),
    _TraceRouteTargetAddr_Type()
)
traceRouteTargetAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteTargetAddr.setStatus("current")


class _TraceRouteHopCount_Type(Unsigned32):
    """Custom type traceRouteHopCount based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TraceRouteHopCount_Type.__name__ = "Unsigned32"
_TraceRouteHopCount_Object = MibTableColumn
traceRouteHopCount = _TraceRouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1, 3),
    _TraceRouteHopCount_Type()
)
traceRouteHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteHopCount.setStatus("current")


class _TraceRoutePingCount_Type(Unsigned32):
    """Custom type traceRoutePingCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TraceRoutePingCount_Type.__name__ = "Unsigned32"
_TraceRoutePingCount_Object = MibTableColumn
traceRoutePingCount = _TraceRoutePingCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1, 4),
    _TraceRoutePingCount_Type()
)
traceRoutePingCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRoutePingCount.setStatus("current")


class _TraceRoutePingTimeout_Type(Unsigned32):
    """Custom type traceRoutePingTimeout based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_TraceRoutePingTimeout_Type.__name__ = "Unsigned32"
_TraceRoutePingTimeout_Object = MibTableColumn
traceRoutePingTimeout = _TraceRoutePingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1, 5),
    _TraceRoutePingTimeout_Type()
)
traceRoutePingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRoutePingTimeout.setStatus("current")
_TraceRouteRowStatus_Type = RowStatus
_TraceRouteRowStatus_Object = MibTableColumn
traceRouteRowStatus = _TraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 1, 1, 6),
    _TraceRouteRowStatus_Type()
)
traceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteRowStatus.setStatus("current")
_TraceRouteHopsTable_Object = MibTable
traceRouteHopsTable = _TraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    traceRouteHopsTable.setStatus("current")
_TraceRouteHopsEntry_Object = MibTableRow
traceRouteHopsEntry = _TraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1)
)
traceRouteHopsEntry.setIndexNames(
    (0, "FS-PING-MIB", "traceRouteIndex"),
    (0, "FS-PING-MIB", "traceRouteHopIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHopsEntry.setStatus("current")
_TraceRouteHopIndex_Type = Unsigned32
_TraceRouteHopIndex_Object = MibTableColumn
traceRouteHopIndex = _TraceRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1, 1),
    _TraceRouteHopIndex_Type()
)
traceRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopIndex.setStatus("current")
_TraceRouteHopPingIndex_Type = Unsigned32
_TraceRouteHopPingIndex_Object = MibTableColumn
traceRouteHopPingIndex = _TraceRouteHopPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1, 2),
    _TraceRouteHopPingIndex_Type()
)
traceRouteHopPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingIndex.setStatus("current")
_TraceRouteHopPingCompleted_Type = TruthValue
_TraceRouteHopPingCompleted_Object = MibTableColumn
traceRouteHopPingCompleted = _TraceRouteHopPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1, 3),
    _TraceRouteHopPingCompleted_Type()
)
traceRouteHopPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingCompleted.setStatus("current")
_TraceRouteHopPingResult_Type = TruthValue
_TraceRouteHopPingResult_Object = MibTableColumn
traceRouteHopPingResult = _TraceRouteHopPingResult_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1, 4),
    _TraceRouteHopPingResult_Type()
)
traceRouteHopPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingResult.setStatus("current")
_TraceRouteHopPingReturnTime_Type = Unsigned32
_TraceRouteHopPingReturnTime_Object = MibTableColumn
traceRouteHopPingReturnTime = _TraceRouteHopPingReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1, 5),
    _TraceRouteHopPingReturnTime_Type()
)
traceRouteHopPingReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingReturnTime.setStatus("current")
_TraceRouteHopAddr_Type = IpAddress
_TraceRouteHopAddr_Object = MibTableColumn
traceRouteHopAddr = _TraceRouteHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 3, 2, 1, 6),
    _TraceRouteHopAddr_Type()
)
traceRouteHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopAddr.setStatus("current")

# Managed Objects groups

fsPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 2, 2, 1)
)
fsPingMIBGroup.setObjects(
      *(("FS-PING-MIB", "fsPingIndex"),
        ("FS-PING-MIB", "fsPingAddress"),
        ("FS-PING-MIB", "fsPingDataLength"),
        ("FS-PING-MIB", "fsPingTimes"),
        ("FS-PING-MIB", "fsPingTimeOuts"),
        ("FS-PING-MIB", "fsPingReturns"),
        ("FS-PING-MIB", "fsPingMaxTime"),
        ("FS-PING-MIB", "fsPingAvTime"),
        ("FS-PING-MIB", "fsPingMinTime"),
        ("FS-PING-MIB", "fsPingCompleted"),
        ("FS-PING-MIB", "fsPingEntryStauts"),
        ("FS-PING-MIB", "fsPingSourceIp"),
        ("FS-PING-MIB", "fsPingSourceInterfaceIndex"),
        ("FS-PING-MIB", "fsPingTypeOfService"))
)
if mibBuilder.loadTexts:
    fsPingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsPingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 3, 2, 1, 1)
)
fsPingMIBCompliance.setObjects(
    ("FS-PING-MIB", "fsPingMIBGroup")
)
if mibBuilder.loadTexts:
    fsPingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PING-MIB",
    **{"fsPingMIB": fsPingMIB,
       "fsPingMIBObjects": fsPingMIBObjects,
       "fsPingTable": fsPingTable,
       "fsPingEntry": fsPingEntry,
       "fsPingIndex": fsPingIndex,
       "fsPingAddress": fsPingAddress,
       "fsPingDataLength": fsPingDataLength,
       "fsPingTimes": fsPingTimes,
       "fsPingTimeOuts": fsPingTimeOuts,
       "fsPingReturns": fsPingReturns,
       "fsPingMaxTime": fsPingMaxTime,
       "fsPingAvTime": fsPingAvTime,
       "fsPingMinTime": fsPingMinTime,
       "fsPingCompleted": fsPingCompleted,
       "fsPingEntryStauts": fsPingEntryStauts,
       "fsPingSourceIp": fsPingSourceIp,
       "fsPingSourceInterfaceIndex": fsPingSourceInterfaceIndex,
       "fsPingTypeOfService": fsPingTypeOfService,
       "fsPingMIBConformance": fsPingMIBConformance,
       "fsPingMIBCompliances": fsPingMIBCompliances,
       "fsPingMIBCompliance": fsPingMIBCompliance,
       "fsPingMIBGroups": fsPingMIBGroups,
       "fsPingMIBGroup": fsPingMIBGroup,
       "traceRouteMIBObjects": traceRouteMIBObjects,
       "traceRouteTable": traceRouteTable,
       "traceRouteEntry": traceRouteEntry,
       "traceRouteIndex": traceRouteIndex,
       "traceRouteTargetAddr": traceRouteTargetAddr,
       "traceRouteHopCount": traceRouteHopCount,
       "traceRoutePingCount": traceRoutePingCount,
       "traceRoutePingTimeout": traceRoutePingTimeout,
       "traceRouteRowStatus": traceRouteRowStatus,
       "traceRouteHopsTable": traceRouteHopsTable,
       "traceRouteHopsEntry": traceRouteHopsEntry,
       "traceRouteHopIndex": traceRouteHopIndex,
       "traceRouteHopPingIndex": traceRouteHopPingIndex,
       "traceRouteHopPingCompleted": traceRouteHopPingCompleted,
       "traceRouteHopPingResult": traceRouteHopPingResult,
       "traceRouteHopPingReturnTime": traceRouteHopPingReturnTime,
       "traceRouteHopAddr": traceRouteHopAddr}
)
