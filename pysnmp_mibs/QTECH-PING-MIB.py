# SNMP MIB module (QTECH-PING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-PING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:34 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechPingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    qtechPingMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechPingMIBObjects_ObjectIdentity = ObjectIdentity
qtechPingMIBObjects = _QtechPingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1)
)
_QtechPingTable_Object = MibTable
qtechPingTable = _QtechPingTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qtechPingTable.setStatus("current")
_QtechPingEntry_Object = MibTableRow
qtechPingEntry = _QtechPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1)
)
qtechPingEntry.setIndexNames(
    (0, "QTECH-PING-MIB", "qtechPingIndex"),
)
if mibBuilder.loadTexts:
    qtechPingEntry.setStatus("current")


class _QtechPingIndex_Type(Integer32):
    """Custom type qtechPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechPingIndex_Type.__name__ = "Integer32"
_QtechPingIndex_Object = MibTableColumn
qtechPingIndex = _QtechPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 1),
    _QtechPingIndex_Type()
)
qtechPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPingIndex.setStatus("current")
_QtechPingAddress_Type = IpAddress
_QtechPingAddress_Object = MibTableColumn
qtechPingAddress = _QtechPingAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 2),
    _QtechPingAddress_Type()
)
qtechPingAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingAddress.setStatus("current")


class _QtechPingDataLength_Type(Unsigned32):
    """Custom type qtechPingDataLength based on Unsigned32"""
    defaultValue = 100


_QtechPingDataLength_Type.__name__ = "Unsigned32"
_QtechPingDataLength_Object = MibTableColumn
qtechPingDataLength = _QtechPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 3),
    _QtechPingDataLength_Type()
)
qtechPingDataLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingDataLength.setStatus("current")


class _QtechPingTimes_Type(Unsigned32):
    """Custom type qtechPingTimes based on Unsigned32"""
    defaultValue = 5


_QtechPingTimes_Type.__name__ = "Unsigned32"
_QtechPingTimes_Object = MibTableColumn
qtechPingTimes = _QtechPingTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 4),
    _QtechPingTimes_Type()
)
qtechPingTimes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingTimes.setStatus("current")


class _QtechPingTimeOuts_Type(Unsigned32):
    """Custom type qtechPingTimeOuts based on Unsigned32"""
    defaultValue = 2000


_QtechPingTimeOuts_Type.__name__ = "Unsigned32"
_QtechPingTimeOuts_Object = MibTableColumn
qtechPingTimeOuts = _QtechPingTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 5),
    _QtechPingTimeOuts_Type()
)
qtechPingTimeOuts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingTimeOuts.setStatus("current")
_QtechPingReturns_Type = Unsigned32
_QtechPingReturns_Object = MibTableColumn
qtechPingReturns = _QtechPingReturns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 6),
    _QtechPingReturns_Type()
)
qtechPingReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPingReturns.setStatus("current")
_QtechPingMaxTime_Type = Unsigned32
_QtechPingMaxTime_Object = MibTableColumn
qtechPingMaxTime = _QtechPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 7),
    _QtechPingMaxTime_Type()
)
qtechPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPingMaxTime.setStatus("current")
_QtechPingAvTime_Type = Unsigned32
_QtechPingAvTime_Object = MibTableColumn
qtechPingAvTime = _QtechPingAvTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 8),
    _QtechPingAvTime_Type()
)
qtechPingAvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPingAvTime.setStatus("current")
_QtechPingMinTime_Type = Unsigned32
_QtechPingMinTime_Object = MibTableColumn
qtechPingMinTime = _QtechPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 9),
    _QtechPingMinTime_Type()
)
qtechPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPingMinTime.setStatus("current")
_QtechPingCompleted_Type = TruthValue
_QtechPingCompleted_Object = MibTableColumn
qtechPingCompleted = _QtechPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 10),
    _QtechPingCompleted_Type()
)
qtechPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPingCompleted.setStatus("current")
_QtechPingEntryStauts_Type = RowStatus
_QtechPingEntryStauts_Object = MibTableColumn
qtechPingEntryStauts = _QtechPingEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 11),
    _QtechPingEntryStauts_Type()
)
qtechPingEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingEntryStauts.setStatus("current")
_QtechPingSourceIp_Type = IpAddress
_QtechPingSourceIp_Object = MibTableColumn
qtechPingSourceIp = _QtechPingSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 12),
    _QtechPingSourceIp_Type()
)
qtechPingSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingSourceIp.setStatus("current")
_QtechPingSourceInterfaceIndex_Type = IfIndex
_QtechPingSourceInterfaceIndex_Object = MibTableColumn
qtechPingSourceInterfaceIndex = _QtechPingSourceInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 13),
    _QtechPingSourceInterfaceIndex_Type()
)
qtechPingSourceInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingSourceInterfaceIndex.setStatus("current")


class _QtechPingTypeOfService_Type(Unsigned32):
    """Custom type qtechPingTypeOfService based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_QtechPingTypeOfService_Type.__name__ = "Unsigned32"
_QtechPingTypeOfService_Object = MibTableColumn
qtechPingTypeOfService = _QtechPingTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 1, 1, 1, 14),
    _QtechPingTypeOfService_Type()
)
qtechPingTypeOfService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPingTypeOfService.setStatus("current")
_QtechPingMIBConformance_ObjectIdentity = ObjectIdentity
qtechPingMIBConformance = _QtechPingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 2)
)
_QtechPingMIBCompliances_ObjectIdentity = ObjectIdentity
qtechPingMIBCompliances = _QtechPingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 2, 1)
)
_QtechPingMIBGroups_ObjectIdentity = ObjectIdentity
qtechPingMIBGroups = _QtechPingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 2, 2)
)
_TraceRouteMIBObjects_ObjectIdentity = ObjectIdentity
traceRouteMIBObjects = _TraceRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3)
)
_TraceRouteTable_Object = MibTable
traceRouteTable = _TraceRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    traceRouteTable.setStatus("current")
_TraceRouteEntry_Object = MibTableRow
traceRouteEntry = _TraceRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1)
)
traceRouteEntry.setIndexNames(
    (0, "QTECH-PING-MIB", "traceRouteIndex"),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1, 1),
    _TraceRouteIndex_Type()
)
traceRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteIndex.setStatus("current")
_TraceRouteTargetAddr_Type = IpAddress
_TraceRouteTargetAddr_Object = MibTableColumn
traceRouteTargetAddr = _TraceRouteTargetAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1, 5),
    _TraceRoutePingTimeout_Type()
)
traceRoutePingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRoutePingTimeout.setStatus("current")
_TraceRouteRowStatus_Type = RowStatus
_TraceRouteRowStatus_Object = MibTableColumn
traceRouteRowStatus = _TraceRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 1, 1, 6),
    _TraceRouteRowStatus_Type()
)
traceRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteRowStatus.setStatus("current")
_TraceRouteHopsTable_Object = MibTable
traceRouteHopsTable = _TraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    traceRouteHopsTable.setStatus("current")
_TraceRouteHopsEntry_Object = MibTableRow
traceRouteHopsEntry = _TraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1)
)
traceRouteHopsEntry.setIndexNames(
    (0, "QTECH-PING-MIB", "traceRouteIndex"),
    (0, "QTECH-PING-MIB", "traceRouteHopIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHopsEntry.setStatus("current")
_TraceRouteHopIndex_Type = Unsigned32
_TraceRouteHopIndex_Object = MibTableColumn
traceRouteHopIndex = _TraceRouteHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1, 1),
    _TraceRouteHopIndex_Type()
)
traceRouteHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopIndex.setStatus("current")
_TraceRouteHopPingIndex_Type = Unsigned32
_TraceRouteHopPingIndex_Object = MibTableColumn
traceRouteHopPingIndex = _TraceRouteHopPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1, 2),
    _TraceRouteHopPingIndex_Type()
)
traceRouteHopPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingIndex.setStatus("current")
_TraceRouteHopPingCompleted_Type = TruthValue
_TraceRouteHopPingCompleted_Object = MibTableColumn
traceRouteHopPingCompleted = _TraceRouteHopPingCompleted_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1, 3),
    _TraceRouteHopPingCompleted_Type()
)
traceRouteHopPingCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingCompleted.setStatus("current")
_TraceRouteHopPingResult_Type = TruthValue
_TraceRouteHopPingResult_Object = MibTableColumn
traceRouteHopPingResult = _TraceRouteHopPingResult_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1, 4),
    _TraceRouteHopPingResult_Type()
)
traceRouteHopPingResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingResult.setStatus("current")
_TraceRouteHopPingReturnTime_Type = Unsigned32
_TraceRouteHopPingReturnTime_Object = MibTableColumn
traceRouteHopPingReturnTime = _TraceRouteHopPingReturnTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1, 5),
    _TraceRouteHopPingReturnTime_Type()
)
traceRouteHopPingReturnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopPingReturnTime.setStatus("current")
_TraceRouteHopAddr_Type = IpAddress
_TraceRouteHopAddr_Object = MibTableColumn
traceRouteHopAddr = _TraceRouteHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 3, 2, 1, 6),
    _TraceRouteHopAddr_Type()
)
traceRouteHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopAddr.setStatus("current")

# Managed Objects groups

qtechPingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 2, 2, 1)
)
qtechPingMIBGroup.setObjects(
      *(("QTECH-PING-MIB", "qtechPingIndex"),
        ("QTECH-PING-MIB", "qtechPingAddress"),
        ("QTECH-PING-MIB", "qtechPingDataLength"),
        ("QTECH-PING-MIB", "qtechPingTimes"),
        ("QTECH-PING-MIB", "qtechPingTimeOuts"),
        ("QTECH-PING-MIB", "qtechPingReturns"),
        ("QTECH-PING-MIB", "qtechPingMaxTime"),
        ("QTECH-PING-MIB", "qtechPingAvTime"),
        ("QTECH-PING-MIB", "qtechPingMinTime"),
        ("QTECH-PING-MIB", "qtechPingCompleted"),
        ("QTECH-PING-MIB", "qtechPingEntryStauts"),
        ("QTECH-PING-MIB", "qtechPingSourceIp"),
        ("QTECH-PING-MIB", "qtechPingSourceInterfaceIndex"),
        ("QTECH-PING-MIB", "qtechPingTypeOfService"))
)
if mibBuilder.loadTexts:
    qtechPingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechPingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 3, 2, 1, 1)
)
qtechPingMIBCompliance.setObjects(
    ("QTECH-PING-MIB", "qtechPingMIBGroup")
)
if mibBuilder.loadTexts:
    qtechPingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-PING-MIB",
    **{"qtechPingMIB": qtechPingMIB,
       "qtechPingMIBObjects": qtechPingMIBObjects,
       "qtechPingTable": qtechPingTable,
       "qtechPingEntry": qtechPingEntry,
       "qtechPingIndex": qtechPingIndex,
       "qtechPingAddress": qtechPingAddress,
       "qtechPingDataLength": qtechPingDataLength,
       "qtechPingTimes": qtechPingTimes,
       "qtechPingTimeOuts": qtechPingTimeOuts,
       "qtechPingReturns": qtechPingReturns,
       "qtechPingMaxTime": qtechPingMaxTime,
       "qtechPingAvTime": qtechPingAvTime,
       "qtechPingMinTime": qtechPingMinTime,
       "qtechPingCompleted": qtechPingCompleted,
       "qtechPingEntryStauts": qtechPingEntryStauts,
       "qtechPingSourceIp": qtechPingSourceIp,
       "qtechPingSourceInterfaceIndex": qtechPingSourceInterfaceIndex,
       "qtechPingTypeOfService": qtechPingTypeOfService,
       "qtechPingMIBConformance": qtechPingMIBConformance,
       "qtechPingMIBCompliances": qtechPingMIBCompliances,
       "qtechPingMIBCompliance": qtechPingMIBCompliance,
       "qtechPingMIBGroups": qtechPingMIBGroups,
       "qtechPingMIBGroup": qtechPingMIBGroup,
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
