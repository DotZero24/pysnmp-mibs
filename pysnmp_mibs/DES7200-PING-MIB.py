# SNMP MIB module (DES7200-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:50 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "DES7200-TC",
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

myPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3)
)
if mibBuilder.loadTexts:
    myPingMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyPingMIBObjects_ObjectIdentity = ObjectIdentity
myPingMIBObjects = _MyPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1)
)
_MyPingTable_Object = MibTable
myPingTable = _MyPingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    myPingTable.setStatus("current")
_MyPingEntry_Object = MibTableRow
myPingEntry = _MyPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1)
)
myPingEntry.setIndexNames(
    (0, "DES7200-PING-MIB", "myPingIndex"),
)
if mibBuilder.loadTexts:
    myPingEntry.setStatus("current")


class _MyPingIndex_Type(Integer32):
    """Custom type myPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MyPingIndex_Type.__name__ = "Integer32"
_MyPingIndex_Object = MibTableColumn
myPingIndex = _MyPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 1),
    _MyPingIndex_Type()
)
myPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPingIndex.setStatus("current")
_MyPingAddress_Type = IpAddress
_MyPingAddress_Object = MibTableColumn
myPingAddress = _MyPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 2),
    _MyPingAddress_Type()
)
myPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingAddress.setStatus("current")


class _MyPingDataLength_Type(Unsigned32):
    """Custom type myPingDataLength based on Unsigned32"""
    defaultValue = 100


_MyPingDataLength_Type.__name__ = "Unsigned32"
_MyPingDataLength_Object = MibTableColumn
myPingDataLength = _MyPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 3),
    _MyPingDataLength_Type()
)
myPingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingDataLength.setStatus("current")


class _MyPingTimes_Type(Unsigned32):
    """Custom type myPingTimes based on Unsigned32"""
    defaultValue = 5


_MyPingTimes_Type.__name__ = "Unsigned32"
_MyPingTimes_Object = MibTableColumn
myPingTimes = _MyPingTimes_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 4),
    _MyPingTimes_Type()
)
myPingTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingTimes.setStatus("current")


class _MyPingTimeOuts_Type(Unsigned32):
    """Custom type myPingTimeOuts based on Unsigned32"""
    defaultValue = 2000


_MyPingTimeOuts_Type.__name__ = "Unsigned32"
_MyPingTimeOuts_Object = MibTableColumn
myPingTimeOuts = _MyPingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 5),
    _MyPingTimeOuts_Type()
)
myPingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingTimeOuts.setStatus("current")
_MyPingReturns_Type = Unsigned32
_MyPingReturns_Object = MibTableColumn
myPingReturns = _MyPingReturns_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 6),
    _MyPingReturns_Type()
)
myPingReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPingReturns.setStatus("current")
_MyPingMaxTime_Type = Unsigned32
_MyPingMaxTime_Object = MibTableColumn
myPingMaxTime = _MyPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 7),
    _MyPingMaxTime_Type()
)
myPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPingMaxTime.setStatus("current")
_MyPingAvTime_Type = Unsigned32
_MyPingAvTime_Object = MibTableColumn
myPingAvTime = _MyPingAvTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 8),
    _MyPingAvTime_Type()
)
myPingAvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPingAvTime.setStatus("current")
_MyPingMinTime_Type = Unsigned32
_MyPingMinTime_Object = MibTableColumn
myPingMinTime = _MyPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 9),
    _MyPingMinTime_Type()
)
myPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPingMinTime.setStatus("current")
_MyPingCompleted_Type = TruthValue
_MyPingCompleted_Object = MibTableColumn
myPingCompleted = _MyPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 10),
    _MyPingCompleted_Type()
)
myPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPingCompleted.setStatus("current")
_MyPingEntryStauts_Type = RowStatus
_MyPingEntryStauts_Object = MibTableColumn
myPingEntryStauts = _MyPingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 11),
    _MyPingEntryStauts_Type()
)
myPingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingEntryStauts.setStatus("current")
_MyPingSourceIp_Type = IpAddress
_MyPingSourceIp_Object = MibTableColumn
myPingSourceIp = _MyPingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 12),
    _MyPingSourceIp_Type()
)
myPingSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingSourceIp.setStatus("current")
_MyPingSourceInterfaceIndex_Type = IfIndex
_MyPingSourceInterfaceIndex_Object = MibTableColumn
myPingSourceInterfaceIndex = _MyPingSourceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 13),
    _MyPingSourceInterfaceIndex_Type()
)
myPingSourceInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingSourceInterfaceIndex.setStatus("current")


class _MyPingTypeOfService_Type(Unsigned32):
    """Custom type myPingTypeOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MyPingTypeOfService_Type.__name__ = "Unsigned32"
_MyPingTypeOfService_Object = MibTableColumn
myPingTypeOfService = _MyPingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 1, 1, 1, 14),
    _MyPingTypeOfService_Type()
)
myPingTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myPingTypeOfService.setStatus("current")
_MyPingMIBConformance_ObjectIdentity = ObjectIdentity
myPingMIBConformance = _MyPingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 2)
)
_MyPingMIBCompliances_ObjectIdentity = ObjectIdentity
myPingMIBCompliances = _MyPingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 2, 1)
)
_MyPingMIBGroups_ObjectIdentity = ObjectIdentity
myPingMIBGroups = _MyPingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 2, 2)
)
_TraceRouteMIBObjects_ObjectIdentity = ObjectIdentity
traceRouteMIBObjects = _TraceRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3)
)
_TraceRouteTable_Object = MibTable
traceRouteTable = _TraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    traceRouteTable.setStatus("current")
_TraceRouteEntry_Object = MibTableRow
traceRouteEntry = _TraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1)
)
traceRouteEntry.setIndexNames(
    (0, "DES7200-PING-MIB", "traceRouteIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1, 1),
    _TraceRouteIndex_Type()
)
traceRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteIndex.setStatus("current")
_TraceRouteTargetAddr_Type = IpAddress
_TraceRouteTargetAddr_Object = MibTableColumn
traceRouteTargetAddr = _TraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1, 5),
    _TraceRoutePingTimeout_Type()
)
traceRoutePingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRoutePingTimeout.setStatus("current")
_TraceRouteRowStatus_Type = RowStatus
_TraceRouteRowStatus_Object = MibTableColumn
traceRouteRowStatus = _TraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 1, 1, 6),
    _TraceRouteRowStatus_Type()
)
traceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteRowStatus.setStatus("current")
_TraceRouteHopsTable_Object = MibTable
traceRouteHopsTable = _TraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    traceRouteHopsTable.setStatus("current")
_TraceRouteHopsEntry_Object = MibTableRow
traceRouteHopsEntry = _TraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1)
)
traceRouteHopsEntry.setIndexNames(
    (0, "DES7200-PING-MIB", "traceRouteIndex"),
    (0, "DES7200-PING-MIB", "traceRouteHopIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHopsEntry.setStatus("current")
_TraceRouteHopIndex_Type = Unsigned32
_TraceRouteHopIndex_Object = MibTableColumn
traceRouteHopIndex = _TraceRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1, 1),
    _TraceRouteHopIndex_Type()
)
traceRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopIndex.setStatus("current")
_TraceRouteHopPingIndex_Type = Unsigned32
_TraceRouteHopPingIndex_Object = MibTableColumn
traceRouteHopPingIndex = _TraceRouteHopPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1, 2),
    _TraceRouteHopPingIndex_Type()
)
traceRouteHopPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingIndex.setStatus("current")
_TraceRouteHopPingCompleted_Type = TruthValue
_TraceRouteHopPingCompleted_Object = MibTableColumn
traceRouteHopPingCompleted = _TraceRouteHopPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1, 3),
    _TraceRouteHopPingCompleted_Type()
)
traceRouteHopPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingCompleted.setStatus("current")
_TraceRouteHopPingResult_Type = TruthValue
_TraceRouteHopPingResult_Object = MibTableColumn
traceRouteHopPingResult = _TraceRouteHopPingResult_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1, 4),
    _TraceRouteHopPingResult_Type()
)
traceRouteHopPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingResult.setStatus("current")
_TraceRouteHopPingReturnTime_Type = Unsigned32
_TraceRouteHopPingReturnTime_Object = MibTableColumn
traceRouteHopPingReturnTime = _TraceRouteHopPingReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1, 5),
    _TraceRouteHopPingReturnTime_Type()
)
traceRouteHopPingReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingReturnTime.setStatus("current")
_TraceRouteHopAddr_Type = IpAddress
_TraceRouteHopAddr_Object = MibTableColumn
traceRouteHopAddr = _TraceRouteHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 3, 2, 1, 6),
    _TraceRouteHopAddr_Type()
)
traceRouteHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopAddr.setStatus("current")

# Managed Objects groups

myPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 2, 2, 1)
)
myPingMIBGroup.setObjects(
      *(("DES7200-PING-MIB", "myPingIndex"),
        ("DES7200-PING-MIB", "myPingAddress"),
        ("DES7200-PING-MIB", "myPingDataLength"),
        ("DES7200-PING-MIB", "myPingTimes"),
        ("DES7200-PING-MIB", "myPingTimeOuts"),
        ("DES7200-PING-MIB", "myPingReturns"),
        ("DES7200-PING-MIB", "myPingMaxTime"),
        ("DES7200-PING-MIB", "myPingAvTime"),
        ("DES7200-PING-MIB", "myPingMinTime"),
        ("DES7200-PING-MIB", "myPingCompleted"),
        ("DES7200-PING-MIB", "myPingEntryStauts"),
        ("DES7200-PING-MIB", "myPingSourceIp"),
        ("DES7200-PING-MIB", "myPingSourceInterfaceIndex"),
        ("DES7200-PING-MIB", "myPingTypeOfService"))
)
if mibBuilder.loadTexts:
    myPingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myPingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 3, 2, 1, 1)
)
myPingMIBCompliance.setObjects(
    ("DES7200-PING-MIB", "myPingMIBGroup")
)
if mibBuilder.loadTexts:
    myPingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-PING-MIB",
    **{"myPingMIB": myPingMIB,
       "myPingMIBObjects": myPingMIBObjects,
       "myPingTable": myPingTable,
       "myPingEntry": myPingEntry,
       "myPingIndex": myPingIndex,
       "myPingAddress": myPingAddress,
       "myPingDataLength": myPingDataLength,
       "myPingTimes": myPingTimes,
       "myPingTimeOuts": myPingTimeOuts,
       "myPingReturns": myPingReturns,
       "myPingMaxTime": myPingMaxTime,
       "myPingAvTime": myPingAvTime,
       "myPingMinTime": myPingMinTime,
       "myPingCompleted": myPingCompleted,
       "myPingEntryStauts": myPingEntryStauts,
       "myPingSourceIp": myPingSourceIp,
       "myPingSourceInterfaceIndex": myPingSourceInterfaceIndex,
       "myPingTypeOfService": myPingTypeOfService,
       "myPingMIBConformance": myPingMIBConformance,
       "myPingMIBCompliances": myPingMIBCompliances,
       "myPingMIBCompliance": myPingMIBCompliance,
       "myPingMIBGroups": myPingMIBGroups,
       "myPingMIBGroup": myPingMIBGroup,
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
