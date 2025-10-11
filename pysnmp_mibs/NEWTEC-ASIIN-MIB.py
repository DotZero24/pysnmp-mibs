# SNMP MIB module (NEWTEC-ASIIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ASIIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:07 2025
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable,
 NtcPid) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable",
    "NtcPid")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ntcAsiIn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800)
)
if mibBuilder.loadTexts:
    ntcAsiIn.setRevisions(
        ("2018-04-04 10:00",
         "2017-07-10 12:00",
         "2014-09-09 09:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAsiInObjects_ObjectIdentity = ObjectIdentity
ntcAsiInObjects = _NtcAsiInObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1)
)
if mibBuilder.loadTexts:
    ntcAsiInObjects.setStatus("current")


class _NtcAsiInInputSelection_Type(Integer32):
    """Custom type ntcAsiInInputSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              40,
              41,
              42,
              100)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("asi1", 1),
          ("asi2", 2),
          ("asi1or2", 40),
          ("asi1before2", 41),
          ("asi2before1", 42),
          ("prbsgenerator", 100))
    )


_NtcAsiInInputSelection_Type.__name__ = "Integer32"
_NtcAsiInInputSelection_Object = MibScalar
ntcAsiInInputSelection = _NtcAsiInInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 1),
    _NtcAsiInInputSelection_Type()
)
ntcAsiInInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInInputSelection.setStatus("current")


class _NtcAsiInActiveInput_Type(Integer32):
    """Custom type ntcAsiInActiveInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("asi1", 1),
          ("asi2", 2))
    )


_NtcAsiInActiveInput_Type.__name__ = "Integer32"
_NtcAsiInActiveInput_Object = MibScalar
ntcAsiInActiveInput = _NtcAsiInActiveInput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 2),
    _NtcAsiInActiveInput_Type()
)
ntcAsiInActiveInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInActiveInput.setStatus("current")


class _NtcAsiInInlineSplitter_Type(Integer32):
    """Custom type ntcAsiInInlineSplitter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("e3dBSplitter", 1),
          ("e6dBSplitter", 2))
    )


_NtcAsiInInlineSplitter_Type.__name__ = "Integer32"
_NtcAsiInInlineSplitter_Object = MibScalar
ntcAsiInInlineSplitter = _NtcAsiInInlineSplitter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 3),
    _NtcAsiInInlineSplitter_Type()
)
ntcAsiInInlineSplitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInInlineSplitter.setStatus("current")
_NtcAsiInMeasuredInputTsBitRate_Type = Unsigned32
_NtcAsiInMeasuredInputTsBitRate_Object = MibScalar
ntcAsiInMeasuredInputTsBitRate = _NtcAsiInMeasuredInputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 4),
    _NtcAsiInMeasuredInputTsBitRate_Type()
)
ntcAsiInMeasuredInputTsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInMeasuredInputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiInMeasuredInputTsBitRate.setUnits("bps")


class _NtcAsiInInputFraming_Type(Integer32):
    """Custom type ntcAsiInInputFraming based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ts188", 0),
          ("ts204", 1))
    )


_NtcAsiInInputFraming_Type.__name__ = "Integer32"
_NtcAsiInInputFraming_Object = MibScalar
ntcAsiInInputFraming = _NtcAsiInInputFraming_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 5),
    _NtcAsiInInputFraming_Type()
)
ntcAsiInInputFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInInputFraming.setStatus("current")
_NtcAsiInInputIfSwitchCount_Type = Counter32
_NtcAsiInInputIfSwitchCount_Object = MibScalar
ntcAsiInInputIfSwitchCount = _NtcAsiInInputIfSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 6),
    _NtcAsiInInputIfSwitchCount_Type()
)
ntcAsiInInputIfSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInInputIfSwitchCount.setStatus("current")
_NtcAsiInPrbsGenerator_ObjectIdentity = ObjectIdentity
ntcAsiInPrbsGenerator = _NtcAsiInPrbsGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7)
)
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenerator.setStatus("current")


class _NtcAsiInPrbsGenTsBitRate_Type(Unsigned32):
    """Custom type ntcAsiInPrbsGenTsBitRate based on Unsigned32"""
    defaultValue = 1000000


_NtcAsiInPrbsGenTsBitRate_Type.__name__ = "Unsigned32"
_NtcAsiInPrbsGenTsBitRate_Object = MibScalar
ntcAsiInPrbsGenTsBitRate = _NtcAsiInPrbsGenTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7, 1),
    _NtcAsiInPrbsGenTsBitRate_Type()
)
ntcAsiInPrbsGenTsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenTsBitRate.setUnits("bps")


class _NtcAsiInPrbsGenType_Type(Integer32):
    """Custom type ntcAsiInPrbsGenType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prbs", 0),
          ("counter", 1))
    )


_NtcAsiInPrbsGenType_Type.__name__ = "Integer32"
_NtcAsiInPrbsGenType_Object = MibScalar
ntcAsiInPrbsGenType = _NtcAsiInPrbsGenType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7, 2),
    _NtcAsiInPrbsGenType_Type()
)
ntcAsiInPrbsGenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenType.setStatus("current")


class _NtcAsiInPrbsGenPidHandling_Type(NtcEnable):
    """Custom type ntcAsiInPrbsGenPidHandling based on NtcEnable"""
    defaultValue = 0


_NtcAsiInPrbsGenPidHandling_Type.__name__ = "NtcEnable"
_NtcAsiInPrbsGenPidHandling_Object = MibScalar
ntcAsiInPrbsGenPidHandling = _NtcAsiInPrbsGenPidHandling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7, 3),
    _NtcAsiInPrbsGenPidHandling_Type()
)
ntcAsiInPrbsGenPidHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenPidHandling.setStatus("current")


class _NtcAsiInPrbsGenPidValue_Type(Unsigned32):
    """Custom type ntcAsiInPrbsGenPidValue based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_NtcAsiInPrbsGenPidValue_Type.__name__ = "Unsigned32"
_NtcAsiInPrbsGenPidValue_Object = MibScalar
ntcAsiInPrbsGenPidValue = _NtcAsiInPrbsGenPidValue_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7, 4),
    _NtcAsiInPrbsGenPidValue_Type()
)
ntcAsiInPrbsGenPidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenPidValue.setStatus("current")


class _NtcAsiInPrbsGenNumberDataPkt_Type(Unsigned32):
    """Custom type ntcAsiInPrbsGenNumberDataPkt based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NtcAsiInPrbsGenNumberDataPkt_Type.__name__ = "Unsigned32"
_NtcAsiInPrbsGenNumberDataPkt_Object = MibScalar
ntcAsiInPrbsGenNumberDataPkt = _NtcAsiInPrbsGenNumberDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7, 5),
    _NtcAsiInPrbsGenNumberDataPkt_Type()
)
ntcAsiInPrbsGenNumberDataPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenNumberDataPkt.setStatus("current")


class _NtcAsiInPrbsGenNumberNullPkt_Type(Unsigned32):
    """Custom type ntcAsiInPrbsGenNumberNullPkt based on Unsigned32"""
    defaultValue = 0


_NtcAsiInPrbsGenNumberNullPkt_Type.__name__ = "Unsigned32"
_NtcAsiInPrbsGenNumberNullPkt_Object = MibScalar
ntcAsiInPrbsGenNumberNullPkt = _NtcAsiInPrbsGenNumberNullPkt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 7, 6),
    _NtcAsiInPrbsGenNumberNullPkt_Type()
)
ntcAsiInPrbsGenNumberNullPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsGenNumberNullPkt.setStatus("current")
_NtcAsiInPrbsMonitor_ObjectIdentity = ObjectIdentity
ntcAsiInPrbsMonitor = _NtcAsiInPrbsMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8)
)
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonitor.setStatus("current")


class _NtcAsiInPrbsMonEnable_Type(NtcEnable):
    """Custom type ntcAsiInPrbsMonEnable based on NtcEnable"""
    defaultValue = 0


_NtcAsiInPrbsMonEnable_Type.__name__ = "NtcEnable"
_NtcAsiInPrbsMonEnable_Object = MibScalar
ntcAsiInPrbsMonEnable = _NtcAsiInPrbsMonEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 1),
    _NtcAsiInPrbsMonEnable_Type()
)
ntcAsiInPrbsMonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonEnable.setStatus("current")


class _NtcAsiInPrbsMonPidHandling_Type(NtcEnable):
    """Custom type ntcAsiInPrbsMonPidHandling based on NtcEnable"""
    defaultValue = 0


_NtcAsiInPrbsMonPidHandling_Type.__name__ = "NtcEnable"
_NtcAsiInPrbsMonPidHandling_Object = MibScalar
ntcAsiInPrbsMonPidHandling = _NtcAsiInPrbsMonPidHandling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 2),
    _NtcAsiInPrbsMonPidHandling_Type()
)
ntcAsiInPrbsMonPidHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonPidHandling.setStatus("current")


class _NtcAsiInPrbsMonPidValue_Type(NtcPid):
    """Custom type ntcAsiInPrbsMonPidValue based on NtcPid"""
    defaultValue = 1


_NtcAsiInPrbsMonPidValue_Type.__name__ = "NtcPid"
_NtcAsiInPrbsMonPidValue_Object = MibScalar
ntcAsiInPrbsMonPidValue = _NtcAsiInPrbsMonPidValue_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 3),
    _NtcAsiInPrbsMonPidValue_Type()
)
ntcAsiInPrbsMonPidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonPidValue.setStatus("current")


class _NtcAsiInPrbsMonState_Type(Integer32):
    """Custom type ntcAsiInPrbsMonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("unsync", 1),
          ("prbs", 2),
          ("ais", 3))
    )


_NtcAsiInPrbsMonState_Type.__name__ = "Integer32"
_NtcAsiInPrbsMonState_Object = MibScalar
ntcAsiInPrbsMonState = _NtcAsiInPrbsMonState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 4),
    _NtcAsiInPrbsMonState_Type()
)
ntcAsiInPrbsMonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonState.setStatus("current")
_NtcAsiInPrbsMonSyncSeconds_Type = Unsigned32
_NtcAsiInPrbsMonSyncSeconds_Object = MibScalar
ntcAsiInPrbsMonSyncSeconds = _NtcAsiInPrbsMonSyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 5),
    _NtcAsiInPrbsMonSyncSeconds_Type()
)
ntcAsiInPrbsMonSyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonSyncSeconds.setStatus("current")
_NtcAsiInPrbsMonErrorCount_Type = Counter32
_NtcAsiInPrbsMonErrorCount_Object = MibScalar
ntcAsiInPrbsMonErrorCount = _NtcAsiInPrbsMonErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 6),
    _NtcAsiInPrbsMonErrorCount_Type()
)
ntcAsiInPrbsMonErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonErrorCount.setStatus("current")


class _NtcAsiInPrbsMonErrorRate_Type(Unsigned32):
    """Custom type ntcAsiInPrbsMonErrorRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21474836470),
    )


_NtcAsiInPrbsMonErrorRate_Type.__name__ = "Unsigned32"
_NtcAsiInPrbsMonErrorRate_Object = MibScalar
ntcAsiInPrbsMonErrorRate = _NtcAsiInPrbsMonErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 7),
    _NtcAsiInPrbsMonErrorRate_Type()
)
ntcAsiInPrbsMonErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonErrorRate.setStatus("current")
_NtcAsiInPrbsMonErrorRatio_Type = Float32TC
_NtcAsiInPrbsMonErrorRatio_Object = MibScalar
ntcAsiInPrbsMonErrorRatio = _NtcAsiInPrbsMonErrorRatio_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 8, 8),
    _NtcAsiInPrbsMonErrorRatio_Type()
)
ntcAsiInPrbsMonErrorRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInPrbsMonErrorRatio.setStatus("current")
_NtcAsiInAlarm_ObjectIdentity = ObjectIdentity
ntcAsiInAlarm = _NtcAsiInAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9)
)
if mibBuilder.loadTexts:
    ntcAsiInAlarm.setStatus("current")
_NtcAsiInAlmGeneralAsiInput_Type = NtcAlarmState
_NtcAsiInAlmGeneralAsiInput_Object = MibScalar
ntcAsiInAlmGeneralAsiInput = _NtcAsiInAlmGeneralAsiInput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 1),
    _NtcAsiInAlmGeneralAsiInput_Type()
)
ntcAsiInAlmGeneralAsiInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmGeneralAsiInput.setStatus("current")
_NtcAsiInAlmNoInputSignal_Type = NtcAlarmState
_NtcAsiInAlmNoInputSignal_Object = MibScalar
ntcAsiInAlmNoInputSignal = _NtcAsiInAlmNoInputSignal_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 2),
    _NtcAsiInAlmNoInputSignal_Type()
)
ntcAsiInAlmNoInputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmNoInputSignal.setStatus("current")
_NtcAsiInAlmNoInputData_Type = NtcAlarmState
_NtcAsiInAlmNoInputData_Object = MibScalar
ntcAsiInAlmNoInputData = _NtcAsiInAlmNoInputData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 3),
    _NtcAsiInAlmNoInputData_Type()
)
ntcAsiInAlmNoInputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmNoInputData.setStatus("current")
_NtcAsiInAlmInvalidTsBitRate_Type = NtcAlarmState
_NtcAsiInAlmInvalidTsBitRate_Object = MibScalar
ntcAsiInAlmInvalidTsBitRate = _NtcAsiInAlmInvalidTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 4),
    _NtcAsiInAlmInvalidTsBitRate_Type()
)
ntcAsiInAlmInvalidTsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmInvalidTsBitRate.setStatus("current")
_NtcAsiInAlmBufferOverflow_Type = NtcAlarmState
_NtcAsiInAlmBufferOverflow_Object = MibScalar
ntcAsiInAlmBufferOverflow = _NtcAsiInAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 5),
    _NtcAsiInAlmBufferOverflow_Type()
)
ntcAsiInAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmBufferOverflow.setStatus("current")
_NtcAsiInAlmNoInputSignalAsi1_Type = NtcAlarmState
_NtcAsiInAlmNoInputSignalAsi1_Object = MibScalar
ntcAsiInAlmNoInputSignalAsi1 = _NtcAsiInAlmNoInputSignalAsi1_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 6),
    _NtcAsiInAlmNoInputSignalAsi1_Type()
)
ntcAsiInAlmNoInputSignalAsi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmNoInputSignalAsi1.setStatus("current")
_NtcAsiInAlmNoInputSignalAsi2_Type = NtcAlarmState
_NtcAsiInAlmNoInputSignalAsi2_Object = MibScalar
ntcAsiInAlmNoInputSignalAsi2 = _NtcAsiInAlmNoInputSignalAsi2_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 7),
    _NtcAsiInAlmNoInputSignalAsi2_Type()
)
ntcAsiInAlmNoInputSignalAsi2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmNoInputSignalAsi2.setStatus("current")
_NtcAsiInAlmNoInputDataAsi1_Type = NtcAlarmState
_NtcAsiInAlmNoInputDataAsi1_Object = MibScalar
ntcAsiInAlmNoInputDataAsi1 = _NtcAsiInAlmNoInputDataAsi1_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 8),
    _NtcAsiInAlmNoInputDataAsi1_Type()
)
ntcAsiInAlmNoInputDataAsi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmNoInputDataAsi1.setStatus("current")
_NtcAsiInAlmNoInputDataAsi2_Type = NtcAlarmState
_NtcAsiInAlmNoInputDataAsi2_Object = MibScalar
ntcAsiInAlmNoInputDataAsi2 = _NtcAsiInAlmNoInputDataAsi2_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 9, 9),
    _NtcAsiInAlmNoInputDataAsi2_Type()
)
ntcAsiInAlmNoInputDataAsi2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiInAlmNoInputDataAsi2.setStatus("current")


class _NtcAsiInInputTsBitRate_Type(Unsigned32):
    """Custom type ntcAsiInInputTsBitRate based on Unsigned32"""
    defaultValue = 1000000


_NtcAsiInInputTsBitRate_Type.__name__ = "Unsigned32"
_NtcAsiInInputTsBitRate_Object = MibScalar
ntcAsiInInputTsBitRate = _NtcAsiInInputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 10),
    _NtcAsiInInputTsBitRate_Type()
)
ntcAsiInInputTsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInInputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiInInputTsBitRate.setUnits("bps")
_NtcAsiInNpRangeThr_ObjectIdentity = ObjectIdentity
ntcAsiInNpRangeThr = _NtcAsiInNpRangeThr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 11)
)
if mibBuilder.loadTexts:
    ntcAsiInNpRangeThr.setStatus("current")


class _NtcAsiInNpRangeThrEnable_Type(NtcEnable):
    """Custom type ntcAsiInNpRangeThrEnable based on NtcEnable"""
    defaultValue = 0


_NtcAsiInNpRangeThrEnable_Type.__name__ = "NtcEnable"
_NtcAsiInNpRangeThrEnable_Object = MibScalar
ntcAsiInNpRangeThrEnable = _NtcAsiInNpRangeThrEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 11, 1),
    _NtcAsiInNpRangeThrEnable_Type()
)
ntcAsiInNpRangeThrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInNpRangeThrEnable.setStatus("current")


class _NtcAsiInNpRangeThrMaxRate_Type(Unsigned32):
    """Custom type ntcAsiInNpRangeThrMaxRate based on Unsigned32"""
    defaultValue = 0


_NtcAsiInNpRangeThrMaxRate_Type.__name__ = "Unsigned32"
_NtcAsiInNpRangeThrMaxRate_Object = MibScalar
ntcAsiInNpRangeThrMaxRate = _NtcAsiInNpRangeThrMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 11, 2),
    _NtcAsiInNpRangeThrMaxRate_Type()
)
ntcAsiInNpRangeThrMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInNpRangeThrMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiInNpRangeThrMaxRate.setUnits("bps")


class _NtcAsiInNpRangeTimeWindow_Type(Integer32):
    """Custom type ntcAsiInNpRangeTimeWindow based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_NtcAsiInNpRangeTimeWindow_Type.__name__ = "Integer32"
_NtcAsiInNpRangeTimeWindow_Object = MibScalar
ntcAsiInNpRangeTimeWindow = _NtcAsiInNpRangeTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 1, 11, 3),
    _NtcAsiInNpRangeTimeWindow_Type()
)
ntcAsiInNpRangeTimeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiInNpRangeTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiInNpRangeTimeWindow.setUnits("s")
_NtcAsiInConformance_ObjectIdentity = ObjectIdentity
ntcAsiInConformance = _NtcAsiInConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 2)
)
if mibBuilder.loadTexts:
    ntcAsiInConformance.setStatus("current")
_NtcAsiInConfCompliance_ObjectIdentity = ObjectIdentity
ntcAsiInConfCompliance = _NtcAsiInConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAsiInConfCompliance.setStatus("current")
_NtcAsiInConfGroup_ObjectIdentity = ObjectIdentity
ntcAsiInConfGroup = _NtcAsiInConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAsiInConfGroup.setStatus("current")

# Managed Objects groups

ntcAsiInConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 2, 2, 1)
)
ntcAsiInConfGrpV1Standard.setObjects(
      *(("NEWTEC-ASIIN-MIB", "ntcAsiInInputSelection"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInActiveInput"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInInlineSplitter"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInMeasuredInputTsBitRate"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInInputFraming"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInInputIfSwitchCount"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsGenTsBitRate"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsGenType"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsGenPidHandling"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsGenPidValue"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsGenNumberDataPkt"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsGenNumberNullPkt"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonEnable"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonPidHandling"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonPidValue"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonState"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonSyncSeconds"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonErrorCount"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonErrorRate"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInPrbsMonErrorRatio"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmGeneralAsiInput"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmNoInputSignal"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmNoInputData"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmInvalidTsBitRate"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmBufferOverflow"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmNoInputSignalAsi1"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmNoInputSignalAsi2"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmNoInputDataAsi1"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInAlmNoInputDataAsi2"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInInputTsBitRate"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInNpRangeThrEnable"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInNpRangeThrMaxRate"),
        ("NEWTEC-ASIIN-MIB", "ntcAsiInNpRangeTimeWindow"))
)
if mibBuilder.loadTexts:
    ntcAsiInConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAsiInConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 800, 2, 1, 1)
)
ntcAsiInConfCompV1Standard.setObjects(
    ("NEWTEC-ASIIN-MIB", "ntcAsiInConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAsiInConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ASIIN-MIB",
    **{"ntcAsiIn": ntcAsiIn,
       "ntcAsiInObjects": ntcAsiInObjects,
       "ntcAsiInInputSelection": ntcAsiInInputSelection,
       "ntcAsiInActiveInput": ntcAsiInActiveInput,
       "ntcAsiInInlineSplitter": ntcAsiInInlineSplitter,
       "ntcAsiInMeasuredInputTsBitRate": ntcAsiInMeasuredInputTsBitRate,
       "ntcAsiInInputFraming": ntcAsiInInputFraming,
       "ntcAsiInInputIfSwitchCount": ntcAsiInInputIfSwitchCount,
       "ntcAsiInPrbsGenerator": ntcAsiInPrbsGenerator,
       "ntcAsiInPrbsGenTsBitRate": ntcAsiInPrbsGenTsBitRate,
       "ntcAsiInPrbsGenType": ntcAsiInPrbsGenType,
       "ntcAsiInPrbsGenPidHandling": ntcAsiInPrbsGenPidHandling,
       "ntcAsiInPrbsGenPidValue": ntcAsiInPrbsGenPidValue,
       "ntcAsiInPrbsGenNumberDataPkt": ntcAsiInPrbsGenNumberDataPkt,
       "ntcAsiInPrbsGenNumberNullPkt": ntcAsiInPrbsGenNumberNullPkt,
       "ntcAsiInPrbsMonitor": ntcAsiInPrbsMonitor,
       "ntcAsiInPrbsMonEnable": ntcAsiInPrbsMonEnable,
       "ntcAsiInPrbsMonPidHandling": ntcAsiInPrbsMonPidHandling,
       "ntcAsiInPrbsMonPidValue": ntcAsiInPrbsMonPidValue,
       "ntcAsiInPrbsMonState": ntcAsiInPrbsMonState,
       "ntcAsiInPrbsMonSyncSeconds": ntcAsiInPrbsMonSyncSeconds,
       "ntcAsiInPrbsMonErrorCount": ntcAsiInPrbsMonErrorCount,
       "ntcAsiInPrbsMonErrorRate": ntcAsiInPrbsMonErrorRate,
       "ntcAsiInPrbsMonErrorRatio": ntcAsiInPrbsMonErrorRatio,
       "ntcAsiInAlarm": ntcAsiInAlarm,
       "ntcAsiInAlmGeneralAsiInput": ntcAsiInAlmGeneralAsiInput,
       "ntcAsiInAlmNoInputSignal": ntcAsiInAlmNoInputSignal,
       "ntcAsiInAlmNoInputData": ntcAsiInAlmNoInputData,
       "ntcAsiInAlmInvalidTsBitRate": ntcAsiInAlmInvalidTsBitRate,
       "ntcAsiInAlmBufferOverflow": ntcAsiInAlmBufferOverflow,
       "ntcAsiInAlmNoInputSignalAsi1": ntcAsiInAlmNoInputSignalAsi1,
       "ntcAsiInAlmNoInputSignalAsi2": ntcAsiInAlmNoInputSignalAsi2,
       "ntcAsiInAlmNoInputDataAsi1": ntcAsiInAlmNoInputDataAsi1,
       "ntcAsiInAlmNoInputDataAsi2": ntcAsiInAlmNoInputDataAsi2,
       "ntcAsiInInputTsBitRate": ntcAsiInInputTsBitRate,
       "ntcAsiInNpRangeThr": ntcAsiInNpRangeThr,
       "ntcAsiInNpRangeThrEnable": ntcAsiInNpRangeThrEnable,
       "ntcAsiInNpRangeThrMaxRate": ntcAsiInNpRangeThrMaxRate,
       "ntcAsiInNpRangeTimeWindow": ntcAsiInNpRangeTimeWindow,
       "ntcAsiInConformance": ntcAsiInConformance,
       "ntcAsiInConfCompliance": ntcAsiInConfCompliance,
       "ntcAsiInConfCompV1Standard": ntcAsiInConfCompV1Standard,
       "ntcAsiInConfGroup": ntcAsiInConfGroup,
       "ntcAsiInConfGrpV1Standard": ntcAsiInConfGrpV1Standard}
)
