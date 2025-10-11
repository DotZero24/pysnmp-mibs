# SNMP MIB module (FM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/FM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:25 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122)
)
if mibBuilder.loadTexts:
    fsfm.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsFmSystem_ObjectIdentity = ObjectIdentity
fsFmSystem = _FsFmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 1)
)


class _FsFmSystemControl_Type(Integer32):
    """Custom type fsFmSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsFmSystemControl_Type.__name__ = "Integer32"
_FsFmSystemControl_Object = MibScalar
fsFmSystemControl = _FsFmSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 1, 1),
    _FsFmSystemControl_Type()
)
fsFmSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmSystemControl.setStatus("current")


class _FsFmModuleStatus_Type(Integer32):
    """Custom type fsFmModuleStatus based on Integer32"""
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


_FsFmModuleStatus_Type.__name__ = "Integer32"
_FsFmModuleStatus_Object = MibScalar
fsFmModuleStatus = _FsFmModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 1, 2),
    _FsFmModuleStatus_Type()
)
fsFmModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmModuleStatus.setStatus("current")


class _FsFmTraceOption_Type(Integer32):
    """Custom type fsFmTraceOption based on Integer32"""
    defaultValue = 262144


_FsFmTraceOption_Type.__name__ = "Integer32"
_FsFmTraceOption_Object = MibScalar
fsFmTraceOption = _FsFmTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 1, 3),
    _FsFmTraceOption_Type()
)
fsFmTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmTraceOption.setStatus("current")
_FsFmLinkEvent_ObjectIdentity = ObjectIdentity
fsFmLinkEvent = _FsFmLinkEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2)
)
_FsFmLinkEventTable_Object = MibTable
fsFmLinkEventTable = _FsFmLinkEventTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1)
)
if mibBuilder.loadTexts:
    fsFmLinkEventTable.setStatus("current")
_FsFmLinkEventEntry_Object = MibTableRow
fsFmLinkEventEntry = _FsFmLinkEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1)
)
fsFmLinkEventEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsFmLinkEventEntry.setStatus("current")


class _FsFmSymPeriodAction_Type(Integer32):
    """Custom type fsFmSymPeriodAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmSymPeriodAction_Type.__name__ = "Integer32"
_FsFmSymPeriodAction_Object = MibTableColumn
fsFmSymPeriodAction = _FsFmSymPeriodAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 1),
    _FsFmSymPeriodAction_Type()
)
fsFmSymPeriodAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmSymPeriodAction.setStatus("current")


class _FsFmFrameAction_Type(Integer32):
    """Custom type fsFmFrameAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmFrameAction_Type.__name__ = "Integer32"
_FsFmFrameAction_Object = MibTableColumn
fsFmFrameAction = _FsFmFrameAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 2),
    _FsFmFrameAction_Type()
)
fsFmFrameAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmFrameAction.setStatus("current")


class _FsFmFramePeriodAction_Type(Integer32):
    """Custom type fsFmFramePeriodAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmFramePeriodAction_Type.__name__ = "Integer32"
_FsFmFramePeriodAction_Object = MibTableColumn
fsFmFramePeriodAction = _FsFmFramePeriodAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 3),
    _FsFmFramePeriodAction_Type()
)
fsFmFramePeriodAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmFramePeriodAction.setStatus("current")


class _FsFmFrameSecSummAction_Type(Integer32):
    """Custom type fsFmFrameSecSummAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmFrameSecSummAction_Type.__name__ = "Integer32"
_FsFmFrameSecSummAction_Object = MibTableColumn
fsFmFrameSecSummAction = _FsFmFrameSecSummAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 4),
    _FsFmFrameSecSummAction_Type()
)
fsFmFrameSecSummAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmFrameSecSummAction.setStatus("current")


class _FsFmCriticalEventAction_Type(Integer32):
    """Custom type fsFmCriticalEventAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmCriticalEventAction_Type.__name__ = "Integer32"
_FsFmCriticalEventAction_Object = MibTableColumn
fsFmCriticalEventAction = _FsFmCriticalEventAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 5),
    _FsFmCriticalEventAction_Type()
)
fsFmCriticalEventAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmCriticalEventAction.setStatus("current")


class _FsFmDyingGaspAction_Type(Integer32):
    """Custom type fsFmDyingGaspAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmDyingGaspAction_Type.__name__ = "Integer32"
_FsFmDyingGaspAction_Object = MibTableColumn
fsFmDyingGaspAction = _FsFmDyingGaspAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 6),
    _FsFmDyingGaspAction_Type()
)
fsFmDyingGaspAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmDyingGaspAction.setStatus("current")


class _FsFmLinkFaultAction_Type(Integer32):
    """Custom type fsFmLinkFaultAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("warning", 2))
    )


_FsFmLinkFaultAction_Type.__name__ = "Integer32"
_FsFmLinkFaultAction_Object = MibTableColumn
fsFmLinkFaultAction = _FsFmLinkFaultAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 2, 1, 1, 7),
    _FsFmLinkFaultAction_Type()
)
fsFmLinkFaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmLinkFaultAction.setStatus("current")
_FsFmLoopback_ObjectIdentity = ObjectIdentity
fsFmLoopback = _FsFmLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3)
)
_FsFmLoopbackTable_Object = MibTable
fsFmLoopbackTable = _FsFmLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1)
)
if mibBuilder.loadTexts:
    fsFmLoopbackTable.setStatus("current")
_FsFmLoopbackEntry_Object = MibTableRow
fsFmLoopbackEntry = _FsFmLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1)
)
fsFmLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsFmLoopbackEntry.setStatus("current")


class _FsFmLoopbackStatus_Type(Integer32):
    """Custom type fsFmLoopbackStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLoopback", 1),
          ("remoteLoopback", 2),
          ("unknown", 3))
    )


_FsFmLoopbackStatus_Type.__name__ = "Integer32"
_FsFmLoopbackStatus_Object = MibTableColumn
fsFmLoopbackStatus = _FsFmLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 1),
    _FsFmLoopbackStatus_Type()
)
fsFmLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLoopbackStatus.setStatus("current")


class _FsFmLBTestPattern_Type(OctetString):
    """Custom type fsFmLBTestPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_FsFmLBTestPattern_Type.__name__ = "OctetString"
_FsFmLBTestPattern_Object = MibTableColumn
fsFmLBTestPattern = _FsFmLBTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 2),
    _FsFmLBTestPattern_Type()
)
fsFmLBTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmLBTestPattern.setStatus("current")


class _FsFmLBTestPktSize_Type(Unsigned32):
    """Custom type fsFmLBTestPktSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_FsFmLBTestPktSize_Type.__name__ = "Unsigned32"
_FsFmLBTestPktSize_Object = MibTableColumn
fsFmLBTestPktSize = _FsFmLBTestPktSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 3),
    _FsFmLBTestPktSize_Type()
)
fsFmLBTestPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmLBTestPktSize.setStatus("current")


class _FsFmLBTestCount_Type(Unsigned32):
    """Custom type fsFmLBTestCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FsFmLBTestCount_Type.__name__ = "Unsigned32"
_FsFmLBTestCount_Object = MibTableColumn
fsFmLBTestCount = _FsFmLBTestCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 4),
    _FsFmLBTestCount_Type()
)
fsFmLBTestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmLBTestCount.setStatus("current")


class _FsFmLBTestWaitTime_Type(Integer32):
    """Custom type fsFmLBTestWaitTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsFmLBTestWaitTime_Type.__name__ = "Integer32"
_FsFmLBTestWaitTime_Object = MibTableColumn
fsFmLBTestWaitTime = _FsFmLBTestWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 5),
    _FsFmLBTestWaitTime_Type()
)
fsFmLBTestWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmLBTestWaitTime.setStatus("current")


class _FsFmLBTestCommand_Type(Integer32):
    """Custom type fsFmLBTestCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noLoopbackTest", 1),
          ("startLoopbackTest", 2))
    )


_FsFmLBTestCommand_Type.__name__ = "Integer32"
_FsFmLBTestCommand_Object = MibTableColumn
fsFmLBTestCommand = _FsFmLBTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 6),
    _FsFmLBTestCommand_Type()
)
fsFmLBTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmLBTestCommand.setStatus("current")


class _FsFmLBTestStatus_Type(Integer32):
    """Custom type fsFmLBTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInitiated", 1),
          ("loopbackTestInprogress", 2),
          ("loopbackTestCompleted", 3))
    )


_FsFmLBTestStatus_Type.__name__ = "Integer32"
_FsFmLBTestStatus_Object = MibTableColumn
fsFmLBTestStatus = _FsFmLBTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 7),
    _FsFmLBTestStatus_Type()
)
fsFmLBTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBTestStatus.setStatus("current")


class _FsFmLBTestStartTimestamp_Type(DisplayString):
    """Custom type fsFmLBTestStartTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_FsFmLBTestStartTimestamp_Type.__name__ = "DisplayString"
_FsFmLBTestStartTimestamp_Object = MibTableColumn
fsFmLBTestStartTimestamp = _FsFmLBTestStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 8),
    _FsFmLBTestStartTimestamp_Type()
)
fsFmLBTestStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBTestStartTimestamp.setStatus("current")


class _FsFmLBTestEndTimestamp_Type(DisplayString):
    """Custom type fsFmLBTestEndTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_FsFmLBTestEndTimestamp_Type.__name__ = "DisplayString"
_FsFmLBTestEndTimestamp_Object = MibTableColumn
fsFmLBTestEndTimestamp = _FsFmLBTestEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 9),
    _FsFmLBTestEndTimestamp_Type()
)
fsFmLBTestEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBTestEndTimestamp.setStatus("current")
_FsFmLBTestTxCount_Type = Unsigned32
_FsFmLBTestTxCount_Object = MibTableColumn
fsFmLBTestTxCount = _FsFmLBTestTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 10),
    _FsFmLBTestTxCount_Type()
)
fsFmLBTestTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBTestTxCount.setStatus("current")
_FsFmLBTestRxCount_Type = Unsigned32
_FsFmLBTestRxCount_Object = MibTableColumn
fsFmLBTestRxCount = _FsFmLBTestRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 11),
    _FsFmLBTestRxCount_Type()
)
fsFmLBTestRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBTestRxCount.setStatus("current")
_FsFmLBTestMatchCount_Type = Unsigned32
_FsFmLBTestMatchCount_Object = MibTableColumn
fsFmLBTestMatchCount = _FsFmLBTestMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 1, 1, 12),
    _FsFmLBTestMatchCount_Type()
)
fsFmLBTestMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBTestMatchCount.setStatus("current")
_FsFmLBStatsTable_Object = MibTable
fsFmLBStatsTable = _FsFmLBStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2)
)
if mibBuilder.loadTexts:
    fsFmLBStatsTable.setStatus("current")
_FsFmLBStatsEntry_Object = MibTableRow
fsFmLBStatsEntry = _FsFmLBStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2, 1)
)
fsFmLBStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsFmLBStatsEntry.setStatus("current")


class _FsFmLBStatsStartTimestamp_Type(DisplayString):
    """Custom type fsFmLBStatsStartTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_FsFmLBStatsStartTimestamp_Type.__name__ = "DisplayString"
_FsFmLBStatsStartTimestamp_Object = MibTableColumn
fsFmLBStatsStartTimestamp = _FsFmLBStatsStartTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2, 1, 1),
    _FsFmLBStatsStartTimestamp_Type()
)
fsFmLBStatsStartTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBStatsStartTimestamp.setStatus("current")


class _FsFmLBStatsEndTimestamp_Type(DisplayString):
    """Custom type fsFmLBStatsEndTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixed_length = 40


_FsFmLBStatsEndTimestamp_Type.__name__ = "DisplayString"
_FsFmLBStatsEndTimestamp_Object = MibTableColumn
fsFmLBStatsEndTimestamp = _FsFmLBStatsEndTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2, 1, 2),
    _FsFmLBStatsEndTimestamp_Type()
)
fsFmLBStatsEndTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBStatsEndTimestamp.setStatus("current")
_FsFmLBStatsTxCount_Type = Unsigned32
_FsFmLBStatsTxCount_Object = MibTableColumn
fsFmLBStatsTxCount = _FsFmLBStatsTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2, 1, 3),
    _FsFmLBStatsTxCount_Type()
)
fsFmLBStatsTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBStatsTxCount.setStatus("current")
_FsFmLBStatsRxCount_Type = Unsigned32
_FsFmLBStatsRxCount_Object = MibTableColumn
fsFmLBStatsRxCount = _FsFmLBStatsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2, 1, 4),
    _FsFmLBStatsRxCount_Type()
)
fsFmLBStatsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBStatsRxCount.setStatus("current")
_FsFmLBStatsMatchCount_Type = Unsigned32
_FsFmLBStatsMatchCount_Object = MibTableColumn
fsFmLBStatsMatchCount = _FsFmLBStatsMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 3, 2, 1, 5),
    _FsFmLBStatsMatchCount_Type()
)
fsFmLBStatsMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmLBStatsMatchCount.setStatus("current")
_FsFmVarRetrieval_ObjectIdentity = ObjectIdentity
fsFmVarRetrieval = _FsFmVarRetrieval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4)
)
_FsFmVarRetrievalTable_Object = MibTable
fsFmVarRetrievalTable = _FsFmVarRetrievalTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 1)
)
if mibBuilder.loadTexts:
    fsFmVarRetrievalTable.setStatus("current")
_FsFmVarRetrievalEntry_Object = MibTableRow
fsFmVarRetrievalEntry = _FsFmVarRetrievalEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 1, 1)
)
fsFmVarRetrievalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsFmVarRetrievalEntry.setStatus("current")


class _FsFmVarRetrievalMaxVar_Type(Unsigned32):
    """Custom type fsFmVarRetrievalMaxVar based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FsFmVarRetrievalMaxVar_Type.__name__ = "Unsigned32"
_FsFmVarRetrievalMaxVar_Object = MibTableColumn
fsFmVarRetrievalMaxVar = _FsFmVarRetrievalMaxVar_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 1, 1, 1),
    _FsFmVarRetrievalMaxVar_Type()
)
fsFmVarRetrievalMaxVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmVarRetrievalMaxVar.setStatus("current")


class _FsFmVarRetrievalRequest_Type(DisplayString):
    """Custom type fsFmVarRetrievalRequest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarRetrievalRequest_Type.__name__ = "DisplayString"
_FsFmVarRetrievalRequest_Object = MibTableColumn
fsFmVarRetrievalRequest = _FsFmVarRetrievalRequest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 1, 1, 2),
    _FsFmVarRetrievalRequest_Type()
)
fsFmVarRetrievalRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmVarRetrievalRequest.setStatus("current")


class _FsFmVarRetrievalClearResponse_Type(Integer32):
    """Custom type fsFmVarRetrievalClearResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notCleared", 1),
          ("clearResponseLog", 2))
    )


_FsFmVarRetrievalClearResponse_Type.__name__ = "Integer32"
_FsFmVarRetrievalClearResponse_Object = MibTableColumn
fsFmVarRetrievalClearResponse = _FsFmVarRetrievalClearResponse_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 1, 1, 3),
    _FsFmVarRetrievalClearResponse_Type()
)
fsFmVarRetrievalClearResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFmVarRetrievalClearResponse.setStatus("current")
_FsFmVarResponseTable_Object = MibTable
fsFmVarResponseTable = _FsFmVarResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3)
)
if mibBuilder.loadTexts:
    fsFmVarResponseTable.setStatus("current")
_FsFmVarResponseEntry_Object = MibTableRow
fsFmVarResponseEntry = _FsFmVarResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1)
)
fsFmVarResponseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FM-MIB", "fsFmVarResponseId"),
)
if mibBuilder.loadTexts:
    fsFmVarResponseEntry.setStatus("current")
_FsFmVarResponseId_Type = Unsigned32
_FsFmVarResponseId_Object = MibTableColumn
fsFmVarResponseId = _FsFmVarResponseId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 1),
    _FsFmVarResponseId_Type()
)
fsFmVarResponseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsFmVarResponseId.setStatus("current")


class _FsFmVarResponseRx1_Type(DisplayString):
    """Custom type fsFmVarResponseRx1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarResponseRx1_Type.__name__ = "DisplayString"
_FsFmVarResponseRx1_Object = MibTableColumn
fsFmVarResponseRx1 = _FsFmVarResponseRx1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 2),
    _FsFmVarResponseRx1_Type()
)
fsFmVarResponseRx1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmVarResponseRx1.setStatus("current")


class _FsFmVarResponseRx2_Type(DisplayString):
    """Custom type fsFmVarResponseRx2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarResponseRx2_Type.__name__ = "DisplayString"
_FsFmVarResponseRx2_Object = MibTableColumn
fsFmVarResponseRx2 = _FsFmVarResponseRx2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 3),
    _FsFmVarResponseRx2_Type()
)
fsFmVarResponseRx2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmVarResponseRx2.setStatus("current")


class _FsFmVarResponseRx3_Type(DisplayString):
    """Custom type fsFmVarResponseRx3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarResponseRx3_Type.__name__ = "DisplayString"
_FsFmVarResponseRx3_Object = MibTableColumn
fsFmVarResponseRx3 = _FsFmVarResponseRx3_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 4),
    _FsFmVarResponseRx3_Type()
)
fsFmVarResponseRx3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmVarResponseRx3.setStatus("current")


class _FsFmVarResponseRx4_Type(DisplayString):
    """Custom type fsFmVarResponseRx4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarResponseRx4_Type.__name__ = "DisplayString"
_FsFmVarResponseRx4_Object = MibTableColumn
fsFmVarResponseRx4 = _FsFmVarResponseRx4_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 5),
    _FsFmVarResponseRx4_Type()
)
fsFmVarResponseRx4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmVarResponseRx4.setStatus("current")


class _FsFmVarResponseRx5_Type(DisplayString):
    """Custom type fsFmVarResponseRx5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarResponseRx5_Type.__name__ = "DisplayString"
_FsFmVarResponseRx5_Object = MibTableColumn
fsFmVarResponseRx5 = _FsFmVarResponseRx5_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 6),
    _FsFmVarResponseRx5_Type()
)
fsFmVarResponseRx5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmVarResponseRx5.setStatus("current")


class _FsFmVarResponseRx6_Type(DisplayString):
    """Custom type fsFmVarResponseRx6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsFmVarResponseRx6_Type.__name__ = "DisplayString"
_FsFmVarResponseRx6_Object = MibTableColumn
fsFmVarResponseRx6 = _FsFmVarResponseRx6_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 122, 4, 3, 1, 7),
    _FsFmVarResponseRx6_Type()
)
fsFmVarResponseRx6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFmVarResponseRx6.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FM-MIB",
    **{"fsfm": fsfm,
       "fsFmSystem": fsFmSystem,
       "fsFmSystemControl": fsFmSystemControl,
       "fsFmModuleStatus": fsFmModuleStatus,
       "fsFmTraceOption": fsFmTraceOption,
       "fsFmLinkEvent": fsFmLinkEvent,
       "fsFmLinkEventTable": fsFmLinkEventTable,
       "fsFmLinkEventEntry": fsFmLinkEventEntry,
       "fsFmSymPeriodAction": fsFmSymPeriodAction,
       "fsFmFrameAction": fsFmFrameAction,
       "fsFmFramePeriodAction": fsFmFramePeriodAction,
       "fsFmFrameSecSummAction": fsFmFrameSecSummAction,
       "fsFmCriticalEventAction": fsFmCriticalEventAction,
       "fsFmDyingGaspAction": fsFmDyingGaspAction,
       "fsFmLinkFaultAction": fsFmLinkFaultAction,
       "fsFmLoopback": fsFmLoopback,
       "fsFmLoopbackTable": fsFmLoopbackTable,
       "fsFmLoopbackEntry": fsFmLoopbackEntry,
       "fsFmLoopbackStatus": fsFmLoopbackStatus,
       "fsFmLBTestPattern": fsFmLBTestPattern,
       "fsFmLBTestPktSize": fsFmLBTestPktSize,
       "fsFmLBTestCount": fsFmLBTestCount,
       "fsFmLBTestWaitTime": fsFmLBTestWaitTime,
       "fsFmLBTestCommand": fsFmLBTestCommand,
       "fsFmLBTestStatus": fsFmLBTestStatus,
       "fsFmLBTestStartTimestamp": fsFmLBTestStartTimestamp,
       "fsFmLBTestEndTimestamp": fsFmLBTestEndTimestamp,
       "fsFmLBTestTxCount": fsFmLBTestTxCount,
       "fsFmLBTestRxCount": fsFmLBTestRxCount,
       "fsFmLBTestMatchCount": fsFmLBTestMatchCount,
       "fsFmLBStatsTable": fsFmLBStatsTable,
       "fsFmLBStatsEntry": fsFmLBStatsEntry,
       "fsFmLBStatsStartTimestamp": fsFmLBStatsStartTimestamp,
       "fsFmLBStatsEndTimestamp": fsFmLBStatsEndTimestamp,
       "fsFmLBStatsTxCount": fsFmLBStatsTxCount,
       "fsFmLBStatsRxCount": fsFmLBStatsRxCount,
       "fsFmLBStatsMatchCount": fsFmLBStatsMatchCount,
       "fsFmVarRetrieval": fsFmVarRetrieval,
       "fsFmVarRetrievalTable": fsFmVarRetrievalTable,
       "fsFmVarRetrievalEntry": fsFmVarRetrievalEntry,
       "fsFmVarRetrievalMaxVar": fsFmVarRetrievalMaxVar,
       "fsFmVarRetrievalRequest": fsFmVarRetrievalRequest,
       "fsFmVarRetrievalClearResponse": fsFmVarRetrievalClearResponse,
       "fsFmVarResponseTable": fsFmVarResponseTable,
       "fsFmVarResponseEntry": fsFmVarResponseEntry,
       "fsFmVarResponseId": fsFmVarResponseId,
       "fsFmVarResponseRx1": fsFmVarResponseRx1,
       "fsFmVarResponseRx2": fsFmVarResponseRx2,
       "fsFmVarResponseRx3": fsFmVarResponseRx3,
       "fsFmVarResponseRx4": fsFmVarResponseRx4,
       "fsFmVarResponseRx5": fsFmVarResponseRx5,
       "fsFmVarResponseRx6": fsFmVarResponseRx6}
)
