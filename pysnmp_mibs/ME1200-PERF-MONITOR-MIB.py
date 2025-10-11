# SNMP MIB module (ME1200-PERF-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/ME1200-PERF-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:42:11 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200InterfaceIndex,
 ME1200MepDmTimeUnit,
 ME1200MepInstanceDirection,
 ME1200MepTxRate,
 ME1200Unsigned16,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200InterfaceIndex",
    "ME1200MepDmTimeUnit",
    "ME1200MepInstanceDirection",
    "ME1200MepTxRate",
    "ME1200Unsigned16",
    "ME1200Unsigned8")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200PerfMonitorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorMib.setRevisions(
        ("2016-08-25 00:00",
         "2015-02-04 00:00",
         "2014-10-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200PerfMonitorEvcPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("evcNni", 0),
          ("evcUni", 1))
    )



class ME1200PerfMonitorTransferMode(TextualConvention, Integer32):
    status = "current"
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
          ("new", 2),
          ("fixAmount", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200PerfMonitorMibObjects_ObjectIdentity = ObjectIdentity
me1200PerfMonitorMibObjects = _Me1200PerfMonitorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1)
)
_Me1200PerfMonitorConfig_ObjectIdentity = ObjectIdentity
me1200PerfMonitorConfig = _Me1200PerfMonitorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2)
)
_Me1200PerfMonitorConfigGlobals_ObjectIdentity = ObjectIdentity
me1200PerfMonitorConfigGlobals = _Me1200PerfMonitorConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1)
)
_Me1200PerfMonitorConfigGlobalsMgmt_ObjectIdentity = ObjectIdentity
me1200PerfMonitorConfigGlobalsMgmt = _Me1200PerfMonitorConfigGlobalsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1)
)
_Me1200PerfMonitorConfigGlobalsMgmtLmAdminState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtLmAdminState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtLmAdminState = _Me1200PerfMonitorConfigGlobalsMgmtLmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 1),
    _Me1200PerfMonitorConfigGlobalsMgmtLmAdminState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtLmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtLmAdminState.setStatus("current")
_Me1200PerfMonitorConfigGlobalsMgmtLmStorageState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtLmStorageState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtLmStorageState = _Me1200PerfMonitorConfigGlobalsMgmtLmStorageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 2),
    _Me1200PerfMonitorConfigGlobalsMgmtLmStorageState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtLmStorageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtLmStorageState.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsMgmtLmInterval_Type(ME1200Unsigned8):
    """Custom type me1200PerfMonitorConfigGlobalsMgmtLmInterval based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Me1200PerfMonitorConfigGlobalsMgmtLmInterval_Type.__name__ = "ME1200Unsigned8"
_Me1200PerfMonitorConfigGlobalsMgmtLmInterval_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtLmInterval = _Me1200PerfMonitorConfigGlobalsMgmtLmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 3),
    _Me1200PerfMonitorConfigGlobalsMgmtLmInterval_Type()
)
me1200PerfMonitorConfigGlobalsMgmtLmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtLmInterval.setStatus("current")
_Me1200PerfMonitorConfigGlobalsMgmtDmAdminState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtDmAdminState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtDmAdminState = _Me1200PerfMonitorConfigGlobalsMgmtDmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 4),
    _Me1200PerfMonitorConfigGlobalsMgmtDmAdminState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtDmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtDmAdminState.setStatus("current")
_Me1200PerfMonitorConfigGlobalsMgmtDmStorageState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtDmStorageState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtDmStorageState = _Me1200PerfMonitorConfigGlobalsMgmtDmStorageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 5),
    _Me1200PerfMonitorConfigGlobalsMgmtDmStorageState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtDmStorageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtDmStorageState.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsMgmtDmInterval_Type(ME1200Unsigned8):
    """Custom type me1200PerfMonitorConfigGlobalsMgmtDmInterval based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Me1200PerfMonitorConfigGlobalsMgmtDmInterval_Type.__name__ = "ME1200Unsigned8"
_Me1200PerfMonitorConfigGlobalsMgmtDmInterval_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtDmInterval = _Me1200PerfMonitorConfigGlobalsMgmtDmInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 6),
    _Me1200PerfMonitorConfigGlobalsMgmtDmInterval_Type()
)
me1200PerfMonitorConfigGlobalsMgmtDmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtDmInterval.setStatus("current")
_Me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState = _Me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 7),
    _Me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState.setStatus("current")
_Me1200PerfMonitorConfigGlobalsMgmtEvcAdminState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtEvcAdminState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtEvcAdminState = _Me1200PerfMonitorConfigGlobalsMgmtEvcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 8),
    _Me1200PerfMonitorConfigGlobalsMgmtEvcAdminState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtEvcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtEvcAdminState.setStatus("current")
_Me1200PerfMonitorConfigGlobalsMgmtEvcStorageState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsMgmtEvcStorageState_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtEvcStorageState = _Me1200PerfMonitorConfigGlobalsMgmtEvcStorageState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 9),
    _Me1200PerfMonitorConfigGlobalsMgmtEvcStorageState_Type()
)
me1200PerfMonitorConfigGlobalsMgmtEvcStorageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtEvcStorageState.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval_Type(ME1200Unsigned8):
    """Custom type me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval_Type.__name__ = "ME1200Unsigned8"
_Me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval_Object = MibScalar
me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval = _Me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 1, 10),
    _Me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval_Type()
)
me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval.setStatus("current")
_Me1200PerfMonitorConfigGlobalsTransfer_ObjectIdentity = ObjectIdentity
me1200PerfMonitorConfigGlobalsTransfer = _Me1200PerfMonitorConfigGlobalsTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 2)
)
_Me1200PerfMonitorConfigGlobalsTransferAdminState_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsTransferAdminState_Object = MibScalar
me1200PerfMonitorConfigGlobalsTransferAdminState = _Me1200PerfMonitorConfigGlobalsTransferAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 2, 1),
    _Me1200PerfMonitorConfigGlobalsTransferAdminState_Type()
)
me1200PerfMonitorConfigGlobalsTransferAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsTransferAdminState.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsTransferServerUrl_Type(ME1200DisplayString):
    """Custom type me1200PerfMonitorConfigGlobalsTransferServerUrl based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200PerfMonitorConfigGlobalsTransferServerUrl_Type.__name__ = "ME1200DisplayString"
_Me1200PerfMonitorConfigGlobalsTransferServerUrl_Object = MibScalar
me1200PerfMonitorConfigGlobalsTransferServerUrl = _Me1200PerfMonitorConfigGlobalsTransferServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 2, 2),
    _Me1200PerfMonitorConfigGlobalsTransferServerUrl_Type()
)
me1200PerfMonitorConfigGlobalsTransferServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsTransferServerUrl.setStatus("current")
_Me1200PerfMonitorConfigGlobalsTransferIntervalMode_Type = ME1200PerfMonitorTransferMode
_Me1200PerfMonitorConfigGlobalsTransferIntervalMode_Object = MibScalar
me1200PerfMonitorConfigGlobalsTransferIntervalMode = _Me1200PerfMonitorConfigGlobalsTransferIntervalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 2, 3),
    _Me1200PerfMonitorConfigGlobalsTransferIntervalMode_Type()
)
me1200PerfMonitorConfigGlobalsTransferIntervalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsTransferIntervalMode.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval_Type(ME1200Unsigned8):
    """Custom type me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval_Type.__name__ = "ME1200Unsigned8"
_Me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval_Object = MibScalar
me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval = _Me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 2, 4),
    _Me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval_Type()
)
me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval.setStatus("current")
_Me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer_Object = MibScalar
me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer = _Me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 2, 5),
    _Me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer_Type()
)
me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSched_ObjectIdentity = ObjectIdentity
me1200PerfMonitorConfigGlobalsXferSched = _Me1200PerfMonitorConfigGlobalsXferSched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3)
)
_Me1200PerfMonitorConfigGlobalsXferSchedHourTable_Object = MibTable
me1200PerfMonitorConfigGlobalsXferSchedHourTable = _Me1200PerfMonitorConfigGlobalsXferSchedHourTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedHourTable.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSchedHourEntry_Object = MibTableRow
me1200PerfMonitorConfigGlobalsXferSchedHourEntry = _Me1200PerfMonitorConfigGlobalsXferSchedHourEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 1, 1)
)
me1200PerfMonitorConfigGlobalsXferSchedHourEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedHourIndex"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedHourEntry.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsXferSchedHourIndex_Type(Unsigned32):
    """Custom type me1200PerfMonitorConfigGlobalsXferSchedHourIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Me1200PerfMonitorConfigGlobalsXferSchedHourIndex_Type.__name__ = "Unsigned32"
_Me1200PerfMonitorConfigGlobalsXferSchedHourIndex_Object = MibTableColumn
me1200PerfMonitorConfigGlobalsXferSchedHourIndex = _Me1200PerfMonitorConfigGlobalsXferSchedHourIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 1, 1, 1),
    _Me1200PerfMonitorConfigGlobalsXferSchedHourIndex_Type()
)
me1200PerfMonitorConfigGlobalsXferSchedHourIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedHourIndex.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSchedHourEnabled_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsXferSchedHourEnabled_Object = MibTableColumn
me1200PerfMonitorConfigGlobalsXferSchedHourEnabled = _Me1200PerfMonitorConfigGlobalsXferSchedHourEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 1, 1, 2),
    _Me1200PerfMonitorConfigGlobalsXferSchedHourEnabled_Type()
)
me1200PerfMonitorConfigGlobalsXferSchedHourEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedHourEnabled.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSchedQuarterTable_Object = MibTable
me1200PerfMonitorConfigGlobalsXferSchedQuarterTable = _Me1200PerfMonitorConfigGlobalsXferSchedQuarterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedQuarterTable.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry_Object = MibTableRow
me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry = _Me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 2, 1)
)
me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex_Type(Unsigned32):
    """Custom type me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex_Type.__name__ = "Unsigned32"
_Me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex_Object = MibTableColumn
me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex = _Me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 2, 1, 1),
    _Me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex_Type()
)
me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled_Type = TruthValue
_Me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled_Object = MibTableColumn
me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled = _Me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 2, 1, 2),
    _Me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled_Type()
)
me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled.setStatus("current")
_Me1200PerfMonitorConfigGlobalsXferSchedOffset_ObjectIdentity = ObjectIdentity
me1200PerfMonitorConfigGlobalsXferSchedOffset = _Me1200PerfMonitorConfigGlobalsXferSchedOffset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 3)
)


class _Me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute_Type(ME1200Unsigned8):
    """Custom type me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute based on ME1200Unsigned8"""
    subtypeSpec = ME1200Unsigned8.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute_Type.__name__ = "ME1200Unsigned8"
_Me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute_Object = MibScalar
me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute = _Me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 3, 1),
    _Me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute_Type()
)
me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute.setStatus("current")


class _Me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond_Type(ME1200Unsigned16):
    """Custom type me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond based on ME1200Unsigned16"""
    subtypeSpec = ME1200Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond_Type.__name__ = "ME1200Unsigned16"
_Me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond_Object = MibScalar
me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond = _Me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 2, 1, 3, 3, 2),
    _Me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond_Type()
)
me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond.setStatus("current")
_Me1200PerfMonitorStatus_ObjectIdentity = ObjectIdentity
me1200PerfMonitorStatus = _Me1200PerfMonitorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3)
)
_Me1200PerfMonitorStatusStatistics_ObjectIdentity = ObjectIdentity
me1200PerfMonitorStatusStatistics = _Me1200PerfMonitorStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1)
)
_Me1200PerfMonitorStatusStatisticsLmTable_Object = MibTable
me1200PerfMonitorStatusStatisticsLmTable = _Me1200PerfMonitorStatusStatisticsLmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmTable.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmEntry_Object = MibTableRow
me1200PerfMonitorStatusStatisticsLmEntry = _Me1200PerfMonitorStatusStatisticsLmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1)
)
me1200PerfMonitorStatusStatisticsLmEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmIntervalId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmEntryId"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmEntry.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmIntervalId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmIntervalId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmIntervalId = _Me1200PerfMonitorStatusStatisticsLmIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 1),
    _Me1200PerfMonitorStatusStatisticsLmIntervalId_Type()
)
me1200PerfMonitorStatusStatisticsLmIntervalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmIntervalId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmEntryId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmEntryId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmEntryId = _Me1200PerfMonitorStatusStatisticsLmEntryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 2),
    _Me1200PerfMonitorStatusStatisticsLmEntryId_Type()
)
me1200PerfMonitorStatusStatisticsLmEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmEntryId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepInstance_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmMepInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepInstance = _Me1200PerfMonitorStatusStatisticsLmMepInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 3),
    _Me1200PerfMonitorStatusStatisticsLmMepInstance_Type()
)
me1200PerfMonitorStatusStatisticsLmMepInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmResidencePort_Type = ME1200InterfaceIndex
_Me1200PerfMonitorStatusStatisticsLmResidencePort_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmResidencePort = _Me1200PerfMonitorStatusStatisticsLmResidencePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 4),
    _Me1200PerfMonitorStatusStatisticsLmResidencePort_Type()
)
me1200PerfMonitorStatusStatisticsLmResidencePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmResidencePort.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepId_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmMepId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepId = _Me1200PerfMonitorStatusStatisticsLmMepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 5),
    _Me1200PerfMonitorStatusStatisticsLmMepId_Type()
)
me1200PerfMonitorStatusStatisticsLmMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepMacAddress_Type = MacAddress
_Me1200PerfMonitorStatusStatisticsLmMepMacAddress_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepMacAddress = _Me1200PerfMonitorStatusStatisticsLmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 6),
    _Me1200PerfMonitorStatusStatisticsLmMepMacAddress_Type()
)
me1200PerfMonitorStatusStatisticsLmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepMacAddress.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepPeerMepId_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmMepPeerMepId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepPeerMepId = _Me1200PerfMonitorStatusStatisticsLmMepPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 7),
    _Me1200PerfMonitorStatusStatisticsLmMepPeerMepId_Type()
)
me1200PerfMonitorStatusStatisticsLmMepPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepPeerMepId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress_Type = MacAddress
_Me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress = _Me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 8),
    _Me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress_Type()
)
me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepDirection_Type = ME1200MepInstanceDirection
_Me1200PerfMonitorStatusStatisticsLmMepDirection_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepDirection = _Me1200PerfMonitorStatusStatisticsLmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 10),
    _Me1200PerfMonitorStatusStatisticsLmMepDirection_Type()
)
me1200PerfMonitorStatusStatisticsLmMepDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepDirection.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepLevel_Type = ME1200Unsigned8
_Me1200PerfMonitorStatusStatisticsLmMepLevel_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepLevel = _Me1200PerfMonitorStatusStatisticsLmMepLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 11),
    _Me1200PerfMonitorStatusStatisticsLmMepLevel_Type()
)
me1200PerfMonitorStatusStatisticsLmMepLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepLevel.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepFlowInstance_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmMepFlowInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepFlowInstance = _Me1200PerfMonitorStatusStatisticsLmMepFlowInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 12),
    _Me1200PerfMonitorStatusStatisticsLmMepFlowInstance_Type()
)
me1200PerfMonitorStatusStatisticsLmMepFlowInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepFlowInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmMepTaggedVid_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmMepTaggedVid_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepTaggedVid = _Me1200PerfMonitorStatusStatisticsLmMepTaggedVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 13),
    _Me1200PerfMonitorStatusStatisticsLmMepTaggedVid_Type()
)
me1200PerfMonitorStatusStatisticsLmMepTaggedVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepTaggedVid.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPriority_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPriority_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPriority = _Me1200PerfMonitorStatusStatisticsLmPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 14),
    _Me1200PerfMonitorStatusStatisticsLmPriority_Type()
)
me1200PerfMonitorStatusStatisticsLmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPriority.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmRate_Type = ME1200MepTxRate
_Me1200PerfMonitorStatusStatisticsLmRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmRate = _Me1200PerfMonitorStatusStatisticsLmRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 15),
    _Me1200PerfMonitorStatusStatisticsLmRate_Type()
)
me1200PerfMonitorStatusStatisticsLmRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmRate.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmTx_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmTx_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmTx = _Me1200PerfMonitorStatusStatisticsLmTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 16),
    _Me1200PerfMonitorStatusStatisticsLmTx_Type()
)
me1200PerfMonitorStatusStatisticsLmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmTx.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmRx_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmRx_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmRx = _Me1200PerfMonitorStatusStatisticsLmRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 17),
    _Me1200PerfMonitorStatusStatisticsLmRx_Type()
)
me1200PerfMonitorStatusStatisticsLmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmRx.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmNearEndLossCount_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmNearEndLossCount_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmNearEndLossCount = _Me1200PerfMonitorStatusStatisticsLmNearEndLossCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 18),
    _Me1200PerfMonitorStatusStatisticsLmNearEndLossCount_Type()
)
me1200PerfMonitorStatusStatisticsLmNearEndLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmNearEndLossCount.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmNearEndLossRate_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmNearEndLossRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmNearEndLossRate = _Me1200PerfMonitorStatusStatisticsLmNearEndLossRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 19),
    _Me1200PerfMonitorStatusStatisticsLmNearEndLossRate_Type()
)
me1200PerfMonitorStatusStatisticsLmNearEndLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmNearEndLossRate.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmFarEndLossCount_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmFarEndLossCount_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmFarEndLossCount = _Me1200PerfMonitorStatusStatisticsLmFarEndLossCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 20),
    _Me1200PerfMonitorStatusStatisticsLmFarEndLossCount_Type()
)
me1200PerfMonitorStatusStatisticsLmFarEndLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmFarEndLossCount.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmFarEndLossRate_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmFarEndLossRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmFarEndLossRate = _Me1200PerfMonitorStatusStatisticsLmFarEndLossRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 21),
    _Me1200PerfMonitorStatusStatisticsLmFarEndLossRate_Type()
)
me1200PerfMonitorStatusStatisticsLmFarEndLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmFarEndLossRate.setStatus("current")


class _Me1200PerfMonitorStatusStatisticsLmMepFlowName_Type(ME1200DisplayString):
    """Custom type me1200PerfMonitorStatusStatisticsLmMepFlowName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200PerfMonitorStatusStatisticsLmMepFlowName_Type.__name__ = "ME1200DisplayString"
_Me1200PerfMonitorStatusStatisticsLmMepFlowName_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmMepFlowName = _Me1200PerfMonitorStatusStatisticsLmMepFlowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 1, 1, 22),
    _Me1200PerfMonitorStatusStatisticsLmMepFlowName_Type()
)
me1200PerfMonitorStatusStatisticsLmMepFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmMepFlowName.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmTable_Object = MibTable
me1200PerfMonitorStatusStatisticsDmTable = _Me1200PerfMonitorStatusStatisticsDmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmTable.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmEntry_Object = MibTableRow
me1200PerfMonitorStatusStatisticsDmEntry = _Me1200PerfMonitorStatusStatisticsDmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1)
)
me1200PerfMonitorStatusStatisticsDmEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmIntervalId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmEntryId"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmEntry.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmIntervalId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmIntervalId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmIntervalId = _Me1200PerfMonitorStatusStatisticsDmIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 1),
    _Me1200PerfMonitorStatusStatisticsDmIntervalId_Type()
)
me1200PerfMonitorStatusStatisticsDmIntervalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmIntervalId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmEntryId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmEntryId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmEntryId = _Me1200PerfMonitorStatusStatisticsDmEntryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 2),
    _Me1200PerfMonitorStatusStatisticsDmEntryId_Type()
)
me1200PerfMonitorStatusStatisticsDmEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmEntryId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepInstance_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsDmMepInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepInstance = _Me1200PerfMonitorStatusStatisticsDmMepInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 3),
    _Me1200PerfMonitorStatusStatisticsDmMepInstance_Type()
)
me1200PerfMonitorStatusStatisticsDmMepInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmResidencePort_Type = ME1200InterfaceIndex
_Me1200PerfMonitorStatusStatisticsDmResidencePort_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmResidencePort = _Me1200PerfMonitorStatusStatisticsDmResidencePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 4),
    _Me1200PerfMonitorStatusStatisticsDmResidencePort_Type()
)
me1200PerfMonitorStatusStatisticsDmResidencePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmResidencePort.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepId_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsDmMepId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepId = _Me1200PerfMonitorStatusStatisticsDmMepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 5),
    _Me1200PerfMonitorStatusStatisticsDmMepId_Type()
)
me1200PerfMonitorStatusStatisticsDmMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepMacAddress_Type = MacAddress
_Me1200PerfMonitorStatusStatisticsDmMepMacAddress_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepMacAddress = _Me1200PerfMonitorStatusStatisticsDmMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 6),
    _Me1200PerfMonitorStatusStatisticsDmMepMacAddress_Type()
)
me1200PerfMonitorStatusStatisticsDmMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepMacAddress.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepPeerMepId_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsDmMepPeerMepId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepPeerMepId = _Me1200PerfMonitorStatusStatisticsDmMepPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 7),
    _Me1200PerfMonitorStatusStatisticsDmMepPeerMepId_Type()
)
me1200PerfMonitorStatusStatisticsDmMepPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepPeerMepId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress_Type = MacAddress
_Me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress = _Me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 8),
    _Me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress_Type()
)
me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepDirection_Type = ME1200MepInstanceDirection
_Me1200PerfMonitorStatusStatisticsDmMepDirection_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepDirection = _Me1200PerfMonitorStatusStatisticsDmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 10),
    _Me1200PerfMonitorStatusStatisticsDmMepDirection_Type()
)
me1200PerfMonitorStatusStatisticsDmMepDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepDirection.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepLevel_Type = ME1200Unsigned8
_Me1200PerfMonitorStatusStatisticsDmMepLevel_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepLevel = _Me1200PerfMonitorStatusStatisticsDmMepLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 11),
    _Me1200PerfMonitorStatusStatisticsDmMepLevel_Type()
)
me1200PerfMonitorStatusStatisticsDmMepLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepLevel.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepFlowInstance_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmMepFlowInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepFlowInstance = _Me1200PerfMonitorStatusStatisticsDmMepFlowInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 12),
    _Me1200PerfMonitorStatusStatisticsDmMepFlowInstance_Type()
)
me1200PerfMonitorStatusStatisticsDmMepFlowInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepFlowInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmMepTaggedVid_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsDmMepTaggedVid_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepTaggedVid = _Me1200PerfMonitorStatusStatisticsDmMepTaggedVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 13),
    _Me1200PerfMonitorStatusStatisticsDmMepTaggedVid_Type()
)
me1200PerfMonitorStatusStatisticsDmMepTaggedVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepTaggedVid.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmPriority_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmPriority_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmPriority = _Me1200PerfMonitorStatusStatisticsDmPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 14),
    _Me1200PerfMonitorStatusStatisticsDmPriority_Type()
)
me1200PerfMonitorStatusStatisticsDmPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmPriority.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmRate_Type = ME1200Unsigned8
_Me1200PerfMonitorStatusStatisticsDmRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmRate = _Me1200PerfMonitorStatusStatisticsDmRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 15),
    _Me1200PerfMonitorStatusStatisticsDmRate_Type()
)
me1200PerfMonitorStatusStatisticsDmRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmRate.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmUnit_Type = ME1200MepDmTimeUnit
_Me1200PerfMonitorStatusStatisticsDmUnit_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmUnit = _Me1200PerfMonitorStatusStatisticsDmUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 16),
    _Me1200PerfMonitorStatusStatisticsDmUnit_Type()
)
me1200PerfMonitorStatusStatisticsDmUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmUnit.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmTx_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmTx_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmTx = _Me1200PerfMonitorStatusStatisticsDmTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 17),
    _Me1200PerfMonitorStatusStatisticsDmTx_Type()
)
me1200PerfMonitorStatusStatisticsDmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmTx.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmRx_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmRx_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmRx = _Me1200PerfMonitorStatusStatisticsDmRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 18),
    _Me1200PerfMonitorStatusStatisticsDmRx_Type()
)
me1200PerfMonitorStatusStatisticsDmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmRx.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage = _Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 19),
    _Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage_Type()
)
me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation = _Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 20),
    _Me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation_Type()
)
me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMin_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMin_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmFarNearDelayMin = _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 21),
    _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMin_Type()
)
me1200PerfMonitorStatusStatisticsDmFarNearDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmFarNearDelayMin.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMax_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMax_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmFarNearDelayMax = _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 22),
    _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMax_Type()
)
me1200PerfMonitorStatusStatisticsDmFarNearDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmFarNearDelayMax.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation = _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 23),
    _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation_Type()
)
me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation = _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 24),
    _Me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation_Type()
)
me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage = _Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 25),
    _Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage_Type()
)
me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation = _Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 26),
    _Me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation_Type()
)
me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMin_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMin_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmNearFarDelayMin = _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 27),
    _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMin_Type()
)
me1200PerfMonitorStatusStatisticsDmNearFarDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmNearFarDelayMin.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMax_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMax_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmNearFarDelayMax = _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 28),
    _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMax_Type()
)
me1200PerfMonitorStatusStatisticsDmNearFarDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmNearFarDelayMax.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation = _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 29),
    _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation_Type()
)
me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation = _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 30),
    _Me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation_Type()
)
me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDm2WayDelayAverage_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDm2WayDelayAverage_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDm2WayDelayAverage = _Me1200PerfMonitorStatusStatisticsDm2WayDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 31),
    _Me1200PerfMonitorStatusStatisticsDm2WayDelayAverage_Type()
)
me1200PerfMonitorStatusStatisticsDm2WayDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDm2WayDelayAverage.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation = _Me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 32),
    _Me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation_Type()
)
me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMin_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMin_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDm2WayDelayMin = _Me1200PerfMonitorStatusStatisticsDm2WayDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 33),
    _Me1200PerfMonitorStatusStatisticsDm2WayDelayMin_Type()
)
me1200PerfMonitorStatusStatisticsDm2WayDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDm2WayDelayMin.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation = _Me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 34),
    _Me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation_Type()
)
me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMax_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMax_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDm2WayDelayMax = _Me1200PerfMonitorStatusStatisticsDm2WayDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 35),
    _Me1200PerfMonitorStatusStatisticsDm2WayDelayMax_Type()
)
me1200PerfMonitorStatusStatisticsDm2WayDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDm2WayDelayMax.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation = _Me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 36),
    _Me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation_Type()
)
me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation.setStatus("current")


class _Me1200PerfMonitorStatusStatisticsDmMepFlowName_Type(ME1200DisplayString):
    """Custom type me1200PerfMonitorStatusStatisticsDmMepFlowName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200PerfMonitorStatusStatisticsDmMepFlowName_Type.__name__ = "ME1200DisplayString"
_Me1200PerfMonitorStatusStatisticsDmMepFlowName_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmMepFlowName = _Me1200PerfMonitorStatusStatisticsDmMepFlowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 2, 1, 37),
    _Me1200PerfMonitorStatusStatisticsDmMepFlowName_Type()
)
me1200PerfMonitorStatusStatisticsDmMepFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmMepFlowName.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmBinTable_Object = MibTable
me1200PerfMonitorStatusStatisticsDmBinTable = _Me1200PerfMonitorStatusStatisticsDmBinTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinTable.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmBinEntry_Object = MibTableRow
me1200PerfMonitorStatusStatisticsDmBinEntry = _Me1200PerfMonitorStatusStatisticsDmBinEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1)
)
me1200PerfMonitorStatusStatisticsDmBinEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinIntervalId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinEntryId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinType"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinDirection"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinBucketId"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinEntry.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmBinIntervalId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmBinIntervalId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmBinIntervalId = _Me1200PerfMonitorStatusStatisticsDmBinIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1, 1),
    _Me1200PerfMonitorStatusStatisticsDmBinIntervalId_Type()
)
me1200PerfMonitorStatusStatisticsDmBinIntervalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinIntervalId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmBinEntryId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmBinEntryId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmBinEntryId = _Me1200PerfMonitorStatusStatisticsDmBinEntryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1, 2),
    _Me1200PerfMonitorStatusStatisticsDmBinEntryId_Type()
)
me1200PerfMonitorStatusStatisticsDmBinEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinEntryId.setStatus("current")


class _Me1200PerfMonitorStatusStatisticsDmBinType_Type(Unsigned32):
    """Custom type me1200PerfMonitorStatusStatisticsDmBinType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Me1200PerfMonitorStatusStatisticsDmBinType_Type.__name__ = "Unsigned32"
_Me1200PerfMonitorStatusStatisticsDmBinType_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmBinType = _Me1200PerfMonitorStatusStatisticsDmBinType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1, 3),
    _Me1200PerfMonitorStatusStatisticsDmBinType_Type()
)
me1200PerfMonitorStatusStatisticsDmBinType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinType.setStatus("current")


class _Me1200PerfMonitorStatusStatisticsDmBinDirection_Type(Unsigned32):
    """Custom type me1200PerfMonitorStatusStatisticsDmBinDirection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Me1200PerfMonitorStatusStatisticsDmBinDirection_Type.__name__ = "Unsigned32"
_Me1200PerfMonitorStatusStatisticsDmBinDirection_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmBinDirection = _Me1200PerfMonitorStatusStatisticsDmBinDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1, 4),
    _Me1200PerfMonitorStatusStatisticsDmBinDirection_Type()
)
me1200PerfMonitorStatusStatisticsDmBinDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinDirection.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmBinBucketId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmBinBucketId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmBinBucketId = _Me1200PerfMonitorStatusStatisticsDmBinBucketId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1, 5),
    _Me1200PerfMonitorStatusStatisticsDmBinBucketId_Type()
)
me1200PerfMonitorStatusStatisticsDmBinBucketId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinBucketId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsDmBinHitCount_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsDmBinHitCount_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsDmBinHitCount = _Me1200PerfMonitorStatusStatisticsDmBinHitCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 3, 1, 6),
    _Me1200PerfMonitorStatusStatisticsDmBinHitCount_Type()
)
me1200PerfMonitorStatusStatisticsDmBinHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinHitCount.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcTable_Object = MibTable
me1200PerfMonitorStatusStatisticsEvcTable = _Me1200PerfMonitorStatusStatisticsEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcTable.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcEntry_Object = MibTableRow
me1200PerfMonitorStatusStatisticsEvcEntry = _Me1200PerfMonitorStatusStatisticsEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1)
)
me1200PerfMonitorStatusStatisticsEvcEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcIntervalId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcEntryId"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcEntry.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcIntervalId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsEvcIntervalId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcIntervalId = _Me1200PerfMonitorStatusStatisticsEvcIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 1),
    _Me1200PerfMonitorStatusStatisticsEvcIntervalId_Type()
)
me1200PerfMonitorStatusStatisticsEvcIntervalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcIntervalId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcEntryId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsEvcEntryId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcEntryId = _Me1200PerfMonitorStatusStatisticsEvcEntryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 2),
    _Me1200PerfMonitorStatusStatisticsEvcEntryId_Type()
)
me1200PerfMonitorStatusStatisticsEvcEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcEntryId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcEvcInstance_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsEvcEvcInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcEvcInstance = _Me1200PerfMonitorStatusStatisticsEvcEvcInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 3),
    _Me1200PerfMonitorStatusStatisticsEvcEvcInstance_Type()
)
me1200PerfMonitorStatusStatisticsEvcEvcInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcEvcInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcPortType_Type = ME1200PerfMonitorEvcPortType
_Me1200PerfMonitorStatusStatisticsEvcPortType_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcPortType = _Me1200PerfMonitorStatusStatisticsEvcPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 4),
    _Me1200PerfMonitorStatusStatisticsEvcPortType_Type()
)
me1200PerfMonitorStatusStatisticsEvcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcPortType.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcPort_Type = ME1200InterfaceIndex
_Me1200PerfMonitorStatusStatisticsEvcPort_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcPort = _Me1200PerfMonitorStatusStatisticsEvcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 5),
    _Me1200PerfMonitorStatusStatisticsEvcPort_Type()
)
me1200PerfMonitorStatusStatisticsEvcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcPort.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcCos_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsEvcCos_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcCos = _Me1200PerfMonitorStatusStatisticsEvcCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 6),
    _Me1200PerfMonitorStatusStatisticsEvcCos_Type()
)
me1200PerfMonitorStatusStatisticsEvcCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcCos.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcGreenRxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcGreenRxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcGreenRxFrames = _Me1200PerfMonitorStatusStatisticsEvcGreenRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 7),
    _Me1200PerfMonitorStatusStatisticsEvcGreenRxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcGreenRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcGreenRxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcGreenTxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcGreenTxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcGreenTxFrames = _Me1200PerfMonitorStatusStatisticsEvcGreenTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 8),
    _Me1200PerfMonitorStatusStatisticsEvcGreenTxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcGreenTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcGreenTxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcGreenRxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcGreenRxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcGreenRxBytes = _Me1200PerfMonitorStatusStatisticsEvcGreenRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 9),
    _Me1200PerfMonitorStatusStatisticsEvcGreenRxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcGreenRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcGreenRxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcGreenTxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcGreenTxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcGreenTxBytes = _Me1200PerfMonitorStatusStatisticsEvcGreenTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 10),
    _Me1200PerfMonitorStatusStatisticsEvcGreenTxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcGreenTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcGreenTxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcYellowRxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcYellowRxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcYellowRxFrames = _Me1200PerfMonitorStatusStatisticsEvcYellowRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 11),
    _Me1200PerfMonitorStatusStatisticsEvcYellowRxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcYellowRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcYellowRxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcYellowTxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcYellowTxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcYellowTxFrames = _Me1200PerfMonitorStatusStatisticsEvcYellowTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 12),
    _Me1200PerfMonitorStatusStatisticsEvcYellowTxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcYellowTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcYellowTxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcYellowRxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcYellowRxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcYellowRxBytes = _Me1200PerfMonitorStatusStatisticsEvcYellowRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 13),
    _Me1200PerfMonitorStatusStatisticsEvcYellowRxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcYellowRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcYellowRxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcYellowTxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcYellowTxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcYellowTxBytes = _Me1200PerfMonitorStatusStatisticsEvcYellowTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 14),
    _Me1200PerfMonitorStatusStatisticsEvcYellowTxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcYellowTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcYellowTxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcRedRxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcRedRxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcRedRxFrames = _Me1200PerfMonitorStatusStatisticsEvcRedRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 15),
    _Me1200PerfMonitorStatusStatisticsEvcRedRxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcRedRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcRedRxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcRedRxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcRedRxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcRedRxBytes = _Me1200PerfMonitorStatusStatisticsEvcRedRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 16),
    _Me1200PerfMonitorStatusStatisticsEvcRedRxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcRedRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcRedRxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames = _Me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 17),
    _Me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames = _Me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 18),
    _Me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames_Type()
)
me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes = _Me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 19),
    _Me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes_Type = Counter64
_Me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes = _Me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 4, 1, 20),
    _Me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes_Type()
)
me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerTable_Object = MibTable
me1200PerfMonitorStatusStatisticsLmPeerTable = _Me1200PerfMonitorStatusStatisticsLmPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerTable.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerEntry_Object = MibTableRow
me1200PerfMonitorStatusStatisticsLmPeerEntry = _Me1200PerfMonitorStatusStatisticsLmPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1)
)
me1200PerfMonitorStatusStatisticsLmPeerEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerIntervalId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerEntryId"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerPeerId"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerEntry.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerIntervalId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerIntervalId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerIntervalId = _Me1200PerfMonitorStatusStatisticsLmPeerIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 1),
    _Me1200PerfMonitorStatusStatisticsLmPeerIntervalId_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerIntervalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerIntervalId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerEntryId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerEntryId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerEntryId = _Me1200PerfMonitorStatusStatisticsLmPeerEntryId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 2),
    _Me1200PerfMonitorStatusStatisticsLmPeerEntryId_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerEntryId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerPeerId_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerPeerId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerPeerId = _Me1200PerfMonitorStatusStatisticsLmPeerPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 3),
    _Me1200PerfMonitorStatusStatisticsLmPeerPeerId_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerPeerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerPeerId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepInstance_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmPeerMepInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepInstance = _Me1200PerfMonitorStatusStatisticsLmPeerMepInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 4),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepInstance_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerResidencePort_Type = ME1200InterfaceIndex
_Me1200PerfMonitorStatusStatisticsLmPeerResidencePort_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerResidencePort = _Me1200PerfMonitorStatusStatisticsLmPeerResidencePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 5),
    _Me1200PerfMonitorStatusStatisticsLmPeerResidencePort_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerResidencePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerResidencePort.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepId_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmPeerMepId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepId = _Me1200PerfMonitorStatusStatisticsLmPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 6),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepId_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress_Type = MacAddress
_Me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress = _Me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 7),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId = _Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 8),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress_Type = MacAddress
_Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress = _Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 9),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepDirection_Type = ME1200MepInstanceDirection
_Me1200PerfMonitorStatusStatisticsLmPeerMepDirection_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepDirection = _Me1200PerfMonitorStatusStatisticsLmPeerMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 11),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepDirection_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepDirection.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepLevel_Type = ME1200Unsigned8
_Me1200PerfMonitorStatusStatisticsLmPeerMepLevel_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepLevel = _Me1200PerfMonitorStatusStatisticsLmPeerMepLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 12),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepLevel_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepLevel.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance = _Me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 13),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid_Type = ME1200Unsigned16
_Me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid = _Me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 14),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerPriority_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerPriority_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerPriority = _Me1200PerfMonitorStatusStatisticsLmPeerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 15),
    _Me1200PerfMonitorStatusStatisticsLmPeerPriority_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerPriority.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerRate_Type = ME1200MepTxRate
_Me1200PerfMonitorStatusStatisticsLmPeerRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerRate = _Me1200PerfMonitorStatusStatisticsLmPeerRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 16),
    _Me1200PerfMonitorStatusStatisticsLmPeerRate_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerRate.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerTx_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerTx_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerTx = _Me1200PerfMonitorStatusStatisticsLmPeerTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 17),
    _Me1200PerfMonitorStatusStatisticsLmPeerTx_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerTx.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerRx_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerRx_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerRx = _Me1200PerfMonitorStatusStatisticsLmPeerRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 18),
    _Me1200PerfMonitorStatusStatisticsLmPeerRx_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerRx.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount = _Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 19),
    _Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate = _Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 20),
    _Me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount = _Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 21),
    _Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount.setStatus("current")
_Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate_Type = Unsigned32
_Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate = _Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 22),
    _Me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate.setStatus("current")


class _Me1200PerfMonitorStatusStatisticsLmPeerMepFlowName_Type(ME1200DisplayString):
    """Custom type me1200PerfMonitorStatusStatisticsLmPeerMepFlowName based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Me1200PerfMonitorStatusStatisticsLmPeerMepFlowName_Type.__name__ = "ME1200DisplayString"
_Me1200PerfMonitorStatusStatisticsLmPeerMepFlowName_Object = MibTableColumn
me1200PerfMonitorStatusStatisticsLmPeerMepFlowName = _Me1200PerfMonitorStatusStatisticsLmPeerMepFlowName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 1, 5, 1, 23),
    _Me1200PerfMonitorStatusStatisticsLmPeerMepFlowName_Type()
)
me1200PerfMonitorStatusStatisticsLmPeerMepFlowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerMepFlowName.setStatus("current")
_Me1200PerfMonitorStatusInterval_ObjectIdentity = ObjectIdentity
me1200PerfMonitorStatusInterval = _Me1200PerfMonitorStatusInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2)
)
_Me1200PerfMonitorStatusIntervalInfoTable_Object = MibTable
me1200PerfMonitorStatusIntervalInfoTable = _Me1200PerfMonitorStatusIntervalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoTable.setStatus("current")
_Me1200PerfMonitorStatusIntervalInfoEntry_Object = MibTableRow
me1200PerfMonitorStatusIntervalInfoEntry = _Me1200PerfMonitorStatusIntervalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1, 1)
)
me1200PerfMonitorStatusIntervalInfoEntry.setIndexNames(
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusIntervalInfoType"),
    (0, "ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusIntervalInfoIntervalId"),
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoEntry.setStatus("current")


class _Me1200PerfMonitorStatusIntervalInfoType_Type(Unsigned32):
    """Custom type me1200PerfMonitorStatusIntervalInfoType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Me1200PerfMonitorStatusIntervalInfoType_Type.__name__ = "Unsigned32"
_Me1200PerfMonitorStatusIntervalInfoType_Object = MibTableColumn
me1200PerfMonitorStatusIntervalInfoType = _Me1200PerfMonitorStatusIntervalInfoType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1, 1, 1),
    _Me1200PerfMonitorStatusIntervalInfoType_Type()
)
me1200PerfMonitorStatusIntervalInfoType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoType.setStatus("current")
_Me1200PerfMonitorStatusIntervalInfoIntervalId_Type = Unsigned32
_Me1200PerfMonitorStatusIntervalInfoIntervalId_Object = MibTableColumn
me1200PerfMonitorStatusIntervalInfoIntervalId = _Me1200PerfMonitorStatusIntervalInfoIntervalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1, 1, 2),
    _Me1200PerfMonitorStatusIntervalInfoIntervalId_Type()
)
me1200PerfMonitorStatusIntervalInfoIntervalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoIntervalId.setStatus("current")


class _Me1200PerfMonitorStatusIntervalInfoStartTime_Type(ME1200DisplayString):
    """Custom type me1200PerfMonitorStatusIntervalInfoStartTime based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200PerfMonitorStatusIntervalInfoStartTime_Type.__name__ = "ME1200DisplayString"
_Me1200PerfMonitorStatusIntervalInfoStartTime_Object = MibTableColumn
me1200PerfMonitorStatusIntervalInfoStartTime = _Me1200PerfMonitorStatusIntervalInfoStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1, 1, 3),
    _Me1200PerfMonitorStatusIntervalInfoStartTime_Type()
)
me1200PerfMonitorStatusIntervalInfoStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoStartTime.setStatus("current")


class _Me1200PerfMonitorStatusIntervalInfoEndTime_Type(ME1200DisplayString):
    """Custom type me1200PerfMonitorStatusIntervalInfoEndTime based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Me1200PerfMonitorStatusIntervalInfoEndTime_Type.__name__ = "ME1200DisplayString"
_Me1200PerfMonitorStatusIntervalInfoEndTime_Object = MibTableColumn
me1200PerfMonitorStatusIntervalInfoEndTime = _Me1200PerfMonitorStatusIntervalInfoEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1, 1, 4),
    _Me1200PerfMonitorStatusIntervalInfoEndTime_Type()
)
me1200PerfMonitorStatusIntervalInfoEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoEndTime.setStatus("current")
_Me1200PerfMonitorStatusIntervalInfoElapsedTime_Type = Counter64
_Me1200PerfMonitorStatusIntervalInfoElapsedTime_Object = MibTableColumn
me1200PerfMonitorStatusIntervalInfoElapsedTime = _Me1200PerfMonitorStatusIntervalInfoElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 3, 2, 1, 1, 5),
    _Me1200PerfMonitorStatusIntervalInfoElapsedTime_Type()
)
me1200PerfMonitorStatusIntervalInfoElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoElapsedTime.setStatus("current")
_Me1200PerfMonitorControl_ObjectIdentity = ObjectIdentity
me1200PerfMonitorControl = _Me1200PerfMonitorControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 4)
)
_Me1200PerfMonitorControlGlobals_ObjectIdentity = ObjectIdentity
me1200PerfMonitorControlGlobals = _Me1200PerfMonitorControlGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 4, 1)
)
_Me1200PerfMonitorControlGlobalsAction_ObjectIdentity = ObjectIdentity
me1200PerfMonitorControlGlobalsAction = _Me1200PerfMonitorControlGlobalsAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 4, 1, 1)
)
_Me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll_Type = TruthValue
_Me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll_Object = MibScalar
me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll = _Me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 4, 1, 1, 1),
    _Me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll_Type()
)
me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll.setStatus("current")
_Me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll_Type = TruthValue
_Me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll_Object = MibScalar
me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll = _Me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 4, 1, 1, 2),
    _Me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll_Type()
)
me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll.setStatus("current")
_Me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll_Type = TruthValue
_Me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll_Object = MibScalar
me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll = _Me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 1, 4, 1, 1, 3),
    _Me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll_Type()
)
me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll.setStatus("current")
_Me1200PerfMonitorMibConformance_ObjectIdentity = ObjectIdentity
me1200PerfMonitorMibConformance = _Me1200PerfMonitorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2)
)
_Me1200PerfMonitorMibCompliances_ObjectIdentity = ObjectIdentity
me1200PerfMonitorMibCompliances = _Me1200PerfMonitorMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 1)
)
_Me1200PerfMonitorMibGroups_ObjectIdentity = ObjectIdentity
me1200PerfMonitorMibGroups = _Me1200PerfMonitorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2)
)

# Managed Objects groups

me1200PerfMonitorConfigGlobalsMgmtInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 1)
)
me1200PerfMonitorConfigGlobalsMgmtInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtLmAdminState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtLmStorageState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtLmInterval"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtDmAdminState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtDmStorageState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtDmInterval"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtEvcAdminState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtEvcStorageState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsMgmtInfoGroup.setStatus("current")

me1200PerfMonitorConfigGlobalsTransferInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 2)
)
me1200PerfMonitorConfigGlobalsTransferInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsTransferAdminState"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsTransferServerUrl"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsTransferIntervalMode"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsTransferInfoGroup.setStatus("current")

me1200PerfMonitorConfigGlobalsXferSchedHourTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 3)
)
me1200PerfMonitorConfigGlobalsXferSchedHourTableInfoGroup.setObjects(
    ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedHourEnabled")
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedHourTableInfoGroup.setStatus("current")

me1200PerfMonitorConfigGlobalsXferSchedQuarterTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 4)
)
me1200PerfMonitorConfigGlobalsXferSchedQuarterTableInfoGroup.setObjects(
    ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled")
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedQuarterTableInfoGroup.setStatus("current")

me1200PerfMonitorConfigGlobalsXferSchedOffsetInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 5)
)
me1200PerfMonitorConfigGlobalsXferSchedOffsetInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorConfigGlobalsXferSchedOffsetInfoGroup.setStatus("current")

me1200PerfMonitorStatusStatisticsLmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 6)
)
me1200PerfMonitorStatusStatisticsLmTableInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmResidencePort"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepId"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepMacAddress"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepPeerMepId"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepDirection"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepLevel"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepFlowInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepTaggedVid"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPriority"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmTx"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmRx"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmNearEndLossCount"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmNearEndLossRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmFarEndLossCount"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmFarEndLossRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmMepFlowName"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmTableInfoGroup.setStatus("current")

me1200PerfMonitorStatusStatisticsDmTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 7)
)
me1200PerfMonitorStatusStatisticsDmTableInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmResidencePort"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepId"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepMacAddress"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepPeerMepId"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepDirection"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepLevel"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepFlowInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepTaggedVid"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmPriority"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmUnit"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmTx"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmRx"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmFarNearDelayMin"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmFarNearDelayMax"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmNearFarDelayMin"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmNearFarDelayMax"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDm2WayDelayAverage"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDm2WayDelayMin"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDm2WayDelayMax"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmMepFlowName"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmTableInfoGroup.setStatus("current")

me1200PerfMonitorStatusStatisticsDmBinTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 8)
)
me1200PerfMonitorStatusStatisticsDmBinTableInfoGroup.setObjects(
    ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinHitCount")
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsDmBinTableInfoGroup.setStatus("current")

me1200PerfMonitorStatusStatisticsEvcTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 9)
)
me1200PerfMonitorStatusStatisticsEvcTableInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcEvcInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcPortType"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcPort"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcCos"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcGreenRxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcGreenTxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcGreenRxBytes"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcGreenTxBytes"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcYellowRxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcYellowTxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcYellowRxBytes"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcYellowTxBytes"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcRedRxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcRedRxBytes"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsEvcTableInfoGroup.setStatus("current")

me1200PerfMonitorStatusStatisticsLmPeerTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 10)
)
me1200PerfMonitorStatusStatisticsLmPeerTableInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerResidencePort"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepId"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepDirection"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepLevel"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerPriority"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerTx"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerRx"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerMepFlowName"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusStatisticsLmPeerTableInfoGroup.setStatus("current")

me1200PerfMonitorStatusIntervalInfoTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 11)
)
me1200PerfMonitorStatusIntervalInfoTableInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusIntervalInfoStartTime"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusIntervalInfoEndTime"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusIntervalInfoElapsedTime"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorStatusIntervalInfoTableInfoGroup.setStatus("current")

me1200PerfMonitorControlGlobalsActionInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 2, 12)
)
me1200PerfMonitorControlGlobalsActionInfoGroup.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorControlGlobalsActionInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200PerfMonitorMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 117, 2, 1, 1)
)
me1200PerfMonitorMibCompliance.setObjects(
      *(("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsMgmtInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsTransferInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedHourTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedQuarterTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorConfigGlobalsXferSchedOffsetInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsDmBinTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsEvcTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusStatisticsLmPeerTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorStatusIntervalInfoTableInfoGroup"),
        ("ME1200-PERF-MONITOR-MIB", "me1200PerfMonitorControlGlobalsActionInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200PerfMonitorMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-PERF-MONITOR-MIB",
    **{"ME1200PerfMonitorEvcPortType": ME1200PerfMonitorEvcPortType,
       "ME1200PerfMonitorTransferMode": ME1200PerfMonitorTransferMode,
       "me1200PerfMonitorMib": me1200PerfMonitorMib,
       "me1200PerfMonitorMibObjects": me1200PerfMonitorMibObjects,
       "me1200PerfMonitorConfig": me1200PerfMonitorConfig,
       "me1200PerfMonitorConfigGlobals": me1200PerfMonitorConfigGlobals,
       "me1200PerfMonitorConfigGlobalsMgmt": me1200PerfMonitorConfigGlobalsMgmt,
       "me1200PerfMonitorConfigGlobalsMgmtLmAdminState": me1200PerfMonitorConfigGlobalsMgmtLmAdminState,
       "me1200PerfMonitorConfigGlobalsMgmtLmStorageState": me1200PerfMonitorConfigGlobalsMgmtLmStorageState,
       "me1200PerfMonitorConfigGlobalsMgmtLmInterval": me1200PerfMonitorConfigGlobalsMgmtLmInterval,
       "me1200PerfMonitorConfigGlobalsMgmtDmAdminState": me1200PerfMonitorConfigGlobalsMgmtDmAdminState,
       "me1200PerfMonitorConfigGlobalsMgmtDmStorageState": me1200PerfMonitorConfigGlobalsMgmtDmStorageState,
       "me1200PerfMonitorConfigGlobalsMgmtDmInterval": me1200PerfMonitorConfigGlobalsMgmtDmInterval,
       "me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState": me1200PerfMonitorConfigGlobalsMgmtDmBinStorageState,
       "me1200PerfMonitorConfigGlobalsMgmtEvcAdminState": me1200PerfMonitorConfigGlobalsMgmtEvcAdminState,
       "me1200PerfMonitorConfigGlobalsMgmtEvcStorageState": me1200PerfMonitorConfigGlobalsMgmtEvcStorageState,
       "me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval": me1200PerfMonitorConfigGlobalsMgmtEvcMeasureInterval,
       "me1200PerfMonitorConfigGlobalsTransfer": me1200PerfMonitorConfigGlobalsTransfer,
       "me1200PerfMonitorConfigGlobalsTransferAdminState": me1200PerfMonitorConfigGlobalsTransferAdminState,
       "me1200PerfMonitorConfigGlobalsTransferServerUrl": me1200PerfMonitorConfigGlobalsTransferServerUrl,
       "me1200PerfMonitorConfigGlobalsTransferIntervalMode": me1200PerfMonitorConfigGlobalsTransferIntervalMode,
       "me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval": me1200PerfMonitorConfigGlobalsTransferFixedNumberOfInterval,
       "me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer": me1200PerfMonitorConfigGlobalsTransferRetryIncompletedTransfer,
       "me1200PerfMonitorConfigGlobalsXferSched": me1200PerfMonitorConfigGlobalsXferSched,
       "me1200PerfMonitorConfigGlobalsXferSchedHourTable": me1200PerfMonitorConfigGlobalsXferSchedHourTable,
       "me1200PerfMonitorConfigGlobalsXferSchedHourEntry": me1200PerfMonitorConfigGlobalsXferSchedHourEntry,
       "me1200PerfMonitorConfigGlobalsXferSchedHourIndex": me1200PerfMonitorConfigGlobalsXferSchedHourIndex,
       "me1200PerfMonitorConfigGlobalsXferSchedHourEnabled": me1200PerfMonitorConfigGlobalsXferSchedHourEnabled,
       "me1200PerfMonitorConfigGlobalsXferSchedQuarterTable": me1200PerfMonitorConfigGlobalsXferSchedQuarterTable,
       "me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry": me1200PerfMonitorConfigGlobalsXferSchedQuarterEntry,
       "me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex": me1200PerfMonitorConfigGlobalsXferSchedQuarterIndex,
       "me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled": me1200PerfMonitorConfigGlobalsXferSchedQuarterEnabled,
       "me1200PerfMonitorConfigGlobalsXferSchedOffset": me1200PerfMonitorConfigGlobalsXferSchedOffset,
       "me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute": me1200PerfMonitorConfigGlobalsXferSchedOffsetMinute,
       "me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond": me1200PerfMonitorConfigGlobalsXferSchedOffsetRandomSecond,
       "me1200PerfMonitorStatus": me1200PerfMonitorStatus,
       "me1200PerfMonitorStatusStatistics": me1200PerfMonitorStatusStatistics,
       "me1200PerfMonitorStatusStatisticsLmTable": me1200PerfMonitorStatusStatisticsLmTable,
       "me1200PerfMonitorStatusStatisticsLmEntry": me1200PerfMonitorStatusStatisticsLmEntry,
       "me1200PerfMonitorStatusStatisticsLmIntervalId": me1200PerfMonitorStatusStatisticsLmIntervalId,
       "me1200PerfMonitorStatusStatisticsLmEntryId": me1200PerfMonitorStatusStatisticsLmEntryId,
       "me1200PerfMonitorStatusStatisticsLmMepInstance": me1200PerfMonitorStatusStatisticsLmMepInstance,
       "me1200PerfMonitorStatusStatisticsLmResidencePort": me1200PerfMonitorStatusStatisticsLmResidencePort,
       "me1200PerfMonitorStatusStatisticsLmMepId": me1200PerfMonitorStatusStatisticsLmMepId,
       "me1200PerfMonitorStatusStatisticsLmMepMacAddress": me1200PerfMonitorStatusStatisticsLmMepMacAddress,
       "me1200PerfMonitorStatusStatisticsLmMepPeerMepId": me1200PerfMonitorStatusStatisticsLmMepPeerMepId,
       "me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress": me1200PerfMonitorStatusStatisticsLmMepPeerMacAddress,
       "me1200PerfMonitorStatusStatisticsLmMepDirection": me1200PerfMonitorStatusStatisticsLmMepDirection,
       "me1200PerfMonitorStatusStatisticsLmMepLevel": me1200PerfMonitorStatusStatisticsLmMepLevel,
       "me1200PerfMonitorStatusStatisticsLmMepFlowInstance": me1200PerfMonitorStatusStatisticsLmMepFlowInstance,
       "me1200PerfMonitorStatusStatisticsLmMepTaggedVid": me1200PerfMonitorStatusStatisticsLmMepTaggedVid,
       "me1200PerfMonitorStatusStatisticsLmPriority": me1200PerfMonitorStatusStatisticsLmPriority,
       "me1200PerfMonitorStatusStatisticsLmRate": me1200PerfMonitorStatusStatisticsLmRate,
       "me1200PerfMonitorStatusStatisticsLmTx": me1200PerfMonitorStatusStatisticsLmTx,
       "me1200PerfMonitorStatusStatisticsLmRx": me1200PerfMonitorStatusStatisticsLmRx,
       "me1200PerfMonitorStatusStatisticsLmNearEndLossCount": me1200PerfMonitorStatusStatisticsLmNearEndLossCount,
       "me1200PerfMonitorStatusStatisticsLmNearEndLossRate": me1200PerfMonitorStatusStatisticsLmNearEndLossRate,
       "me1200PerfMonitorStatusStatisticsLmFarEndLossCount": me1200PerfMonitorStatusStatisticsLmFarEndLossCount,
       "me1200PerfMonitorStatusStatisticsLmFarEndLossRate": me1200PerfMonitorStatusStatisticsLmFarEndLossRate,
       "me1200PerfMonitorStatusStatisticsLmMepFlowName": me1200PerfMonitorStatusStatisticsLmMepFlowName,
       "me1200PerfMonitorStatusStatisticsDmTable": me1200PerfMonitorStatusStatisticsDmTable,
       "me1200PerfMonitorStatusStatisticsDmEntry": me1200PerfMonitorStatusStatisticsDmEntry,
       "me1200PerfMonitorStatusStatisticsDmIntervalId": me1200PerfMonitorStatusStatisticsDmIntervalId,
       "me1200PerfMonitorStatusStatisticsDmEntryId": me1200PerfMonitorStatusStatisticsDmEntryId,
       "me1200PerfMonitorStatusStatisticsDmMepInstance": me1200PerfMonitorStatusStatisticsDmMepInstance,
       "me1200PerfMonitorStatusStatisticsDmResidencePort": me1200PerfMonitorStatusStatisticsDmResidencePort,
       "me1200PerfMonitorStatusStatisticsDmMepId": me1200PerfMonitorStatusStatisticsDmMepId,
       "me1200PerfMonitorStatusStatisticsDmMepMacAddress": me1200PerfMonitorStatusStatisticsDmMepMacAddress,
       "me1200PerfMonitorStatusStatisticsDmMepPeerMepId": me1200PerfMonitorStatusStatisticsDmMepPeerMepId,
       "me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress": me1200PerfMonitorStatusStatisticsDmMepPeerMacAddress,
       "me1200PerfMonitorStatusStatisticsDmMepDirection": me1200PerfMonitorStatusStatisticsDmMepDirection,
       "me1200PerfMonitorStatusStatisticsDmMepLevel": me1200PerfMonitorStatusStatisticsDmMepLevel,
       "me1200PerfMonitorStatusStatisticsDmMepFlowInstance": me1200PerfMonitorStatusStatisticsDmMepFlowInstance,
       "me1200PerfMonitorStatusStatisticsDmMepTaggedVid": me1200PerfMonitorStatusStatisticsDmMepTaggedVid,
       "me1200PerfMonitorStatusStatisticsDmPriority": me1200PerfMonitorStatusStatisticsDmPriority,
       "me1200PerfMonitorStatusStatisticsDmRate": me1200PerfMonitorStatusStatisticsDmRate,
       "me1200PerfMonitorStatusStatisticsDmUnit": me1200PerfMonitorStatusStatisticsDmUnit,
       "me1200PerfMonitorStatusStatisticsDmTx": me1200PerfMonitorStatusStatisticsDmTx,
       "me1200PerfMonitorStatusStatisticsDmRx": me1200PerfMonitorStatusStatisticsDmRx,
       "me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage": me1200PerfMonitorStatusStatisticsDmFarNearDelayAverage,
       "me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation": me1200PerfMonitorStatusStatisticsDmFarNearDelayAverageVariation,
       "me1200PerfMonitorStatusStatisticsDmFarNearDelayMin": me1200PerfMonitorStatusStatisticsDmFarNearDelayMin,
       "me1200PerfMonitorStatusStatisticsDmFarNearDelayMax": me1200PerfMonitorStatusStatisticsDmFarNearDelayMax,
       "me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation": me1200PerfMonitorStatusStatisticsDmFarNearDelayMinVariation,
       "me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation": me1200PerfMonitorStatusStatisticsDmFarNearDelayMaxVariation,
       "me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage": me1200PerfMonitorStatusStatisticsDmNearFarDelayAverage,
       "me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation": me1200PerfMonitorStatusStatisticsDmNearFarDelayAverageVariation,
       "me1200PerfMonitorStatusStatisticsDmNearFarDelayMin": me1200PerfMonitorStatusStatisticsDmNearFarDelayMin,
       "me1200PerfMonitorStatusStatisticsDmNearFarDelayMax": me1200PerfMonitorStatusStatisticsDmNearFarDelayMax,
       "me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation": me1200PerfMonitorStatusStatisticsDmNearFarDelayMinVariation,
       "me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation": me1200PerfMonitorStatusStatisticsDmNearFarDelayMaxVariation,
       "me1200PerfMonitorStatusStatisticsDm2WayDelayAverage": me1200PerfMonitorStatusStatisticsDm2WayDelayAverage,
       "me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation": me1200PerfMonitorStatusStatisticsDm2WayDelayAverageVariation,
       "me1200PerfMonitorStatusStatisticsDm2WayDelayMin": me1200PerfMonitorStatusStatisticsDm2WayDelayMin,
       "me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation": me1200PerfMonitorStatusStatisticsDm2WayDelayMinVariation,
       "me1200PerfMonitorStatusStatisticsDm2WayDelayMax": me1200PerfMonitorStatusStatisticsDm2WayDelayMax,
       "me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation": me1200PerfMonitorStatusStatisticsDm2WayDelayMaxVariation,
       "me1200PerfMonitorStatusStatisticsDmMepFlowName": me1200PerfMonitorStatusStatisticsDmMepFlowName,
       "me1200PerfMonitorStatusStatisticsDmBinTable": me1200PerfMonitorStatusStatisticsDmBinTable,
       "me1200PerfMonitorStatusStatisticsDmBinEntry": me1200PerfMonitorStatusStatisticsDmBinEntry,
       "me1200PerfMonitorStatusStatisticsDmBinIntervalId": me1200PerfMonitorStatusStatisticsDmBinIntervalId,
       "me1200PerfMonitorStatusStatisticsDmBinEntryId": me1200PerfMonitorStatusStatisticsDmBinEntryId,
       "me1200PerfMonitorStatusStatisticsDmBinType": me1200PerfMonitorStatusStatisticsDmBinType,
       "me1200PerfMonitorStatusStatisticsDmBinDirection": me1200PerfMonitorStatusStatisticsDmBinDirection,
       "me1200PerfMonitorStatusStatisticsDmBinBucketId": me1200PerfMonitorStatusStatisticsDmBinBucketId,
       "me1200PerfMonitorStatusStatisticsDmBinHitCount": me1200PerfMonitorStatusStatisticsDmBinHitCount,
       "me1200PerfMonitorStatusStatisticsEvcTable": me1200PerfMonitorStatusStatisticsEvcTable,
       "me1200PerfMonitorStatusStatisticsEvcEntry": me1200PerfMonitorStatusStatisticsEvcEntry,
       "me1200PerfMonitorStatusStatisticsEvcIntervalId": me1200PerfMonitorStatusStatisticsEvcIntervalId,
       "me1200PerfMonitorStatusStatisticsEvcEntryId": me1200PerfMonitorStatusStatisticsEvcEntryId,
       "me1200PerfMonitorStatusStatisticsEvcEvcInstance": me1200PerfMonitorStatusStatisticsEvcEvcInstance,
       "me1200PerfMonitorStatusStatisticsEvcPortType": me1200PerfMonitorStatusStatisticsEvcPortType,
       "me1200PerfMonitorStatusStatisticsEvcPort": me1200PerfMonitorStatusStatisticsEvcPort,
       "me1200PerfMonitorStatusStatisticsEvcCos": me1200PerfMonitorStatusStatisticsEvcCos,
       "me1200PerfMonitorStatusStatisticsEvcGreenRxFrames": me1200PerfMonitorStatusStatisticsEvcGreenRxFrames,
       "me1200PerfMonitorStatusStatisticsEvcGreenTxFrames": me1200PerfMonitorStatusStatisticsEvcGreenTxFrames,
       "me1200PerfMonitorStatusStatisticsEvcGreenRxBytes": me1200PerfMonitorStatusStatisticsEvcGreenRxBytes,
       "me1200PerfMonitorStatusStatisticsEvcGreenTxBytes": me1200PerfMonitorStatusStatisticsEvcGreenTxBytes,
       "me1200PerfMonitorStatusStatisticsEvcYellowRxFrames": me1200PerfMonitorStatusStatisticsEvcYellowRxFrames,
       "me1200PerfMonitorStatusStatisticsEvcYellowTxFrames": me1200PerfMonitorStatusStatisticsEvcYellowTxFrames,
       "me1200PerfMonitorStatusStatisticsEvcYellowRxBytes": me1200PerfMonitorStatusStatisticsEvcYellowRxBytes,
       "me1200PerfMonitorStatusStatisticsEvcYellowTxBytes": me1200PerfMonitorStatusStatisticsEvcYellowTxBytes,
       "me1200PerfMonitorStatusStatisticsEvcRedRxFrames": me1200PerfMonitorStatusStatisticsEvcRedRxFrames,
       "me1200PerfMonitorStatusStatisticsEvcRedRxBytes": me1200PerfMonitorStatusStatisticsEvcRedRxBytes,
       "me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames": me1200PerfMonitorStatusStatisticsEvcDiscardedRxFrames,
       "me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames": me1200PerfMonitorStatusStatisticsEvcDiscardedTxFrames,
       "me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes": me1200PerfMonitorStatusStatisticsEvcDiscardedRxBytes,
       "me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes": me1200PerfMonitorStatusStatisticsEvcDiscardedTxBytes,
       "me1200PerfMonitorStatusStatisticsLmPeerTable": me1200PerfMonitorStatusStatisticsLmPeerTable,
       "me1200PerfMonitorStatusStatisticsLmPeerEntry": me1200PerfMonitorStatusStatisticsLmPeerEntry,
       "me1200PerfMonitorStatusStatisticsLmPeerIntervalId": me1200PerfMonitorStatusStatisticsLmPeerIntervalId,
       "me1200PerfMonitorStatusStatisticsLmPeerEntryId": me1200PerfMonitorStatusStatisticsLmPeerEntryId,
       "me1200PerfMonitorStatusStatisticsLmPeerPeerId": me1200PerfMonitorStatusStatisticsLmPeerPeerId,
       "me1200PerfMonitorStatusStatisticsLmPeerMepInstance": me1200PerfMonitorStatusStatisticsLmPeerMepInstance,
       "me1200PerfMonitorStatusStatisticsLmPeerResidencePort": me1200PerfMonitorStatusStatisticsLmPeerResidencePort,
       "me1200PerfMonitorStatusStatisticsLmPeerMepId": me1200PerfMonitorStatusStatisticsLmPeerMepId,
       "me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress": me1200PerfMonitorStatusStatisticsLmPeerMepMacAddress,
       "me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId": me1200PerfMonitorStatusStatisticsLmPeerMepPeerMepId,
       "me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress": me1200PerfMonitorStatusStatisticsLmPeerMepPeerMacAddress,
       "me1200PerfMonitorStatusStatisticsLmPeerMepDirection": me1200PerfMonitorStatusStatisticsLmPeerMepDirection,
       "me1200PerfMonitorStatusStatisticsLmPeerMepLevel": me1200PerfMonitorStatusStatisticsLmPeerMepLevel,
       "me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance": me1200PerfMonitorStatusStatisticsLmPeerMepFlowInstance,
       "me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid": me1200PerfMonitorStatusStatisticsLmPeerMepTaggedVid,
       "me1200PerfMonitorStatusStatisticsLmPeerPriority": me1200PerfMonitorStatusStatisticsLmPeerPriority,
       "me1200PerfMonitorStatusStatisticsLmPeerRate": me1200PerfMonitorStatusStatisticsLmPeerRate,
       "me1200PerfMonitorStatusStatisticsLmPeerTx": me1200PerfMonitorStatusStatisticsLmPeerTx,
       "me1200PerfMonitorStatusStatisticsLmPeerRx": me1200PerfMonitorStatusStatisticsLmPeerRx,
       "me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount": me1200PerfMonitorStatusStatisticsLmPeerNearEndLossCount,
       "me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate": me1200PerfMonitorStatusStatisticsLmPeerNearEndLossRate,
       "me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount": me1200PerfMonitorStatusStatisticsLmPeerFarEndLossCount,
       "me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate": me1200PerfMonitorStatusStatisticsLmPeerFarEndLossRate,
       "me1200PerfMonitorStatusStatisticsLmPeerMepFlowName": me1200PerfMonitorStatusStatisticsLmPeerMepFlowName,
       "me1200PerfMonitorStatusInterval": me1200PerfMonitorStatusInterval,
       "me1200PerfMonitorStatusIntervalInfoTable": me1200PerfMonitorStatusIntervalInfoTable,
       "me1200PerfMonitorStatusIntervalInfoEntry": me1200PerfMonitorStatusIntervalInfoEntry,
       "me1200PerfMonitorStatusIntervalInfoType": me1200PerfMonitorStatusIntervalInfoType,
       "me1200PerfMonitorStatusIntervalInfoIntervalId": me1200PerfMonitorStatusIntervalInfoIntervalId,
       "me1200PerfMonitorStatusIntervalInfoStartTime": me1200PerfMonitorStatusIntervalInfoStartTime,
       "me1200PerfMonitorStatusIntervalInfoEndTime": me1200PerfMonitorStatusIntervalInfoEndTime,
       "me1200PerfMonitorStatusIntervalInfoElapsedTime": me1200PerfMonitorStatusIntervalInfoElapsedTime,
       "me1200PerfMonitorControl": me1200PerfMonitorControl,
       "me1200PerfMonitorControlGlobals": me1200PerfMonitorControlGlobals,
       "me1200PerfMonitorControlGlobalsAction": me1200PerfMonitorControlGlobalsAction,
       "me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll": me1200PerfMonitorControlGlobalsActionDeleteLmStatisticsAll,
       "me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll": me1200PerfMonitorControlGlobalsActionDeleteDmStatisticsAll,
       "me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll": me1200PerfMonitorControlGlobalsActionDeleteEvcStatisticsAll,
       "me1200PerfMonitorMibConformance": me1200PerfMonitorMibConformance,
       "me1200PerfMonitorMibCompliances": me1200PerfMonitorMibCompliances,
       "me1200PerfMonitorMibCompliance": me1200PerfMonitorMibCompliance,
       "me1200PerfMonitorMibGroups": me1200PerfMonitorMibGroups,
       "me1200PerfMonitorConfigGlobalsMgmtInfoGroup": me1200PerfMonitorConfigGlobalsMgmtInfoGroup,
       "me1200PerfMonitorConfigGlobalsTransferInfoGroup": me1200PerfMonitorConfigGlobalsTransferInfoGroup,
       "me1200PerfMonitorConfigGlobalsXferSchedHourTableInfoGroup": me1200PerfMonitorConfigGlobalsXferSchedHourTableInfoGroup,
       "me1200PerfMonitorConfigGlobalsXferSchedQuarterTableInfoGroup": me1200PerfMonitorConfigGlobalsXferSchedQuarterTableInfoGroup,
       "me1200PerfMonitorConfigGlobalsXferSchedOffsetInfoGroup": me1200PerfMonitorConfigGlobalsXferSchedOffsetInfoGroup,
       "me1200PerfMonitorStatusStatisticsLmTableInfoGroup": me1200PerfMonitorStatusStatisticsLmTableInfoGroup,
       "me1200PerfMonitorStatusStatisticsDmTableInfoGroup": me1200PerfMonitorStatusStatisticsDmTableInfoGroup,
       "me1200PerfMonitorStatusStatisticsDmBinTableInfoGroup": me1200PerfMonitorStatusStatisticsDmBinTableInfoGroup,
       "me1200PerfMonitorStatusStatisticsEvcTableInfoGroup": me1200PerfMonitorStatusStatisticsEvcTableInfoGroup,
       "me1200PerfMonitorStatusStatisticsLmPeerTableInfoGroup": me1200PerfMonitorStatusStatisticsLmPeerTableInfoGroup,
       "me1200PerfMonitorStatusIntervalInfoTableInfoGroup": me1200PerfMonitorStatusIntervalInfoTableInfoGroup,
       "me1200PerfMonitorControlGlobalsActionInfoGroup": me1200PerfMonitorControlGlobalsActionInfoGroup}
)
