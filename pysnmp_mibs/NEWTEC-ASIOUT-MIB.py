# SNMP MIB module (NEWTEC-ASIOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-ASIOUT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:17 2025
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

ntcAsiOut = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900)
)
if mibBuilder.loadTexts:
    ntcAsiOut.setRevisions(
        ("2014-09-09 09:00",
         "2013-03-27 10:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcAsiOutObjects_ObjectIdentity = ObjectIdentity
ntcAsiOutObjects = _NtcAsiOutObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1)
)
if mibBuilder.loadTexts:
    ntcAsiOutObjects.setStatus("current")


class _NtcAsiOutInputSelection_Type(Integer32):
    """Custom type ntcAsiOutInputSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5,
              100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("modulatorinput", 2),
          ("activeinput", 3),
          ("nonactiveinput", 4),
          ("demod", 5),
          ("prbsgenerator", 100),
          ("ncrstream", 101))
    )


_NtcAsiOutInputSelection_Type.__name__ = "Integer32"
_NtcAsiOutInputSelection_Object = MibScalar
ntcAsiOutInputSelection = _NtcAsiOutInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 1),
    _NtcAsiOutInputSelection_Type()
)
ntcAsiOutInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutInputSelection.setStatus("current")


class _NtcAsiOutOutputSelection_Type(Integer32):
    """Custom type ntcAsiOutOutputSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              40)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("asi1", 1),
          ("asi2", 2),
          ("asi1and2", 40))
    )


_NtcAsiOutOutputSelection_Type.__name__ = "Integer32"
_NtcAsiOutOutputSelection_Object = MibScalar
ntcAsiOutOutputSelection = _NtcAsiOutOutputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 2),
    _NtcAsiOutOutputSelection_Type()
)
ntcAsiOutOutputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutOutputSelection.setStatus("current")
_NtcAsiOutMeasuredTsBitRate_Type = Unsigned32
_NtcAsiOutMeasuredTsBitRate_Object = MibScalar
ntcAsiOutMeasuredTsBitRate = _NtcAsiOutMeasuredTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 3),
    _NtcAsiOutMeasuredTsBitRate_Type()
)
ntcAsiOutMeasuredTsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiOutMeasuredTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiOutMeasuredTsBitRate.setUnits("bps")
_NtcAsiOutPrbsGenerator_ObjectIdentity = ObjectIdentity
ntcAsiOutPrbsGenerator = _NtcAsiOutPrbsGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4)
)
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenerator.setStatus("current")


class _NtcAsiOutPrbsGenOutputTsBitRate_Type(Unsigned32):
    """Custom type ntcAsiOutPrbsGenOutputTsBitRate based on Unsigned32"""
    defaultValue = 1000000


_NtcAsiOutPrbsGenOutputTsBitRate_Type.__name__ = "Unsigned32"
_NtcAsiOutPrbsGenOutputTsBitRate_Object = MibScalar
ntcAsiOutPrbsGenOutputTsBitRate = _NtcAsiOutPrbsGenOutputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4, 1),
    _NtcAsiOutPrbsGenOutputTsBitRate_Type()
)
ntcAsiOutPrbsGenOutputTsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenOutputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenOutputTsBitRate.setUnits("bps")


class _NtcAsiOutPrbsGenType_Type(Integer32):
    """Custom type ntcAsiOutPrbsGenType based on Integer32"""
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


_NtcAsiOutPrbsGenType_Type.__name__ = "Integer32"
_NtcAsiOutPrbsGenType_Object = MibScalar
ntcAsiOutPrbsGenType = _NtcAsiOutPrbsGenType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4, 2),
    _NtcAsiOutPrbsGenType_Type()
)
ntcAsiOutPrbsGenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenType.setStatus("current")


class _NtcAsiOutPrbsGenPidHandling_Type(NtcEnable):
    """Custom type ntcAsiOutPrbsGenPidHandling based on NtcEnable"""
    defaultValue = 0


_NtcAsiOutPrbsGenPidHandling_Type.__name__ = "NtcEnable"
_NtcAsiOutPrbsGenPidHandling_Object = MibScalar
ntcAsiOutPrbsGenPidHandling = _NtcAsiOutPrbsGenPidHandling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4, 3),
    _NtcAsiOutPrbsGenPidHandling_Type()
)
ntcAsiOutPrbsGenPidHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenPidHandling.setStatus("current")


class _NtcAsiOutPrbsGenPidValue_Type(NtcPid):
    """Custom type ntcAsiOutPrbsGenPidValue based on NtcPid"""
    defaultValue = 1


_NtcAsiOutPrbsGenPidValue_Type.__name__ = "NtcPid"
_NtcAsiOutPrbsGenPidValue_Object = MibScalar
ntcAsiOutPrbsGenPidValue = _NtcAsiOutPrbsGenPidValue_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4, 4),
    _NtcAsiOutPrbsGenPidValue_Type()
)
ntcAsiOutPrbsGenPidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenPidValue.setStatus("current")


class _NtcAsiOutPrbsGenNumberDataPkt_Type(Unsigned32):
    """Custom type ntcAsiOutPrbsGenNumberDataPkt based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NtcAsiOutPrbsGenNumberDataPkt_Type.__name__ = "Unsigned32"
_NtcAsiOutPrbsGenNumberDataPkt_Object = MibScalar
ntcAsiOutPrbsGenNumberDataPkt = _NtcAsiOutPrbsGenNumberDataPkt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4, 5),
    _NtcAsiOutPrbsGenNumberDataPkt_Type()
)
ntcAsiOutPrbsGenNumberDataPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenNumberDataPkt.setStatus("current")


class _NtcAsiOutPrbsGenNumberNullPkt_Type(Unsigned32):
    """Custom type ntcAsiOutPrbsGenNumberNullPkt based on Unsigned32"""
    defaultValue = 0


_NtcAsiOutPrbsGenNumberNullPkt_Type.__name__ = "Unsigned32"
_NtcAsiOutPrbsGenNumberNullPkt_Object = MibScalar
ntcAsiOutPrbsGenNumberNullPkt = _NtcAsiOutPrbsGenNumberNullPkt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 4, 6),
    _NtcAsiOutPrbsGenNumberNullPkt_Type()
)
ntcAsiOutPrbsGenNumberNullPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutPrbsGenNumberNullPkt.setStatus("current")
_NtcAsiOutNcrGenerator_ObjectIdentity = ObjectIdentity
ntcAsiOutNcrGenerator = _NtcAsiOutNcrGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 5)
)
if mibBuilder.loadTexts:
    ntcAsiOutNcrGenerator.setStatus("current")


class _NtcAsiOutNcrGenOutputTsBitRate_Type(Unsigned32):
    """Custom type ntcAsiOutNcrGenOutputTsBitRate based on Unsigned32"""
    defaultValue = 1000000


_NtcAsiOutNcrGenOutputTsBitRate_Type.__name__ = "Unsigned32"
_NtcAsiOutNcrGenOutputTsBitRate_Object = MibScalar
ntcAsiOutNcrGenOutputTsBitRate = _NtcAsiOutNcrGenOutputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 5, 1),
    _NtcAsiOutNcrGenOutputTsBitRate_Type()
)
ntcAsiOutNcrGenOutputTsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcAsiOutNcrGenOutputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcAsiOutNcrGenOutputTsBitRate.setUnits("bps")
_NtcAsiOutAlarm_ObjectIdentity = ObjectIdentity
ntcAsiOutAlarm = _NtcAsiOutAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 6)
)
if mibBuilder.loadTexts:
    ntcAsiOutAlarm.setStatus("current")
_NtcAsiOutAlmGeneralAsiOutput_Type = NtcAlarmState
_NtcAsiOutAlmGeneralAsiOutput_Object = MibScalar
ntcAsiOutAlmGeneralAsiOutput = _NtcAsiOutAlmGeneralAsiOutput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 6, 1),
    _NtcAsiOutAlmGeneralAsiOutput_Type()
)
ntcAsiOutAlmGeneralAsiOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiOutAlmGeneralAsiOutput.setStatus("current")
_NtcAsiOutAlmNoOutputSignal_Type = NtcAlarmState
_NtcAsiOutAlmNoOutputSignal_Object = MibScalar
ntcAsiOutAlmNoOutputSignal = _NtcAsiOutAlmNoOutputSignal_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 6, 2),
    _NtcAsiOutAlmNoOutputSignal_Type()
)
ntcAsiOutAlmNoOutputSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiOutAlmNoOutputSignal.setStatus("current")
_NtcAsiOutAlmNoOutputSignalAsi1_Type = NtcAlarmState
_NtcAsiOutAlmNoOutputSignalAsi1_Object = MibScalar
ntcAsiOutAlmNoOutputSignalAsi1 = _NtcAsiOutAlmNoOutputSignalAsi1_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 6, 3),
    _NtcAsiOutAlmNoOutputSignalAsi1_Type()
)
ntcAsiOutAlmNoOutputSignalAsi1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiOutAlmNoOutputSignalAsi1.setStatus("current")
_NtcAsiOutAlmNoOutputSignalAsi2_Type = NtcAlarmState
_NtcAsiOutAlmNoOutputSignalAsi2_Object = MibScalar
ntcAsiOutAlmNoOutputSignalAsi2 = _NtcAsiOutAlmNoOutputSignalAsi2_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 1, 6, 4),
    _NtcAsiOutAlmNoOutputSignalAsi2_Type()
)
ntcAsiOutAlmNoOutputSignalAsi2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcAsiOutAlmNoOutputSignalAsi2.setStatus("current")
_NtcAsiOutConformance_ObjectIdentity = ObjectIdentity
ntcAsiOutConformance = _NtcAsiOutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 2)
)
if mibBuilder.loadTexts:
    ntcAsiOutConformance.setStatus("current")
_NtcAsiOutConfCompliance_ObjectIdentity = ObjectIdentity
ntcAsiOutConfCompliance = _NtcAsiOutConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 2, 1)
)
if mibBuilder.loadTexts:
    ntcAsiOutConfCompliance.setStatus("current")
_NtcAsiOutConfGroup_ObjectIdentity = ObjectIdentity
ntcAsiOutConfGroup = _NtcAsiOutConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 2, 2)
)
if mibBuilder.loadTexts:
    ntcAsiOutConfGroup.setStatus("current")

# Managed Objects groups

ntcAsiOutConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 2, 2, 1)
)
ntcAsiOutConfGrpV1Standard.setObjects(
      *(("NEWTEC-ASIOUT-MIB", "ntcAsiOutInputSelection"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutOutputSelection"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutMeasuredTsBitRate"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutPrbsGenOutputTsBitRate"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutPrbsGenType"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutPrbsGenPidHandling"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutPrbsGenPidValue"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutPrbsGenNumberDataPkt"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutPrbsGenNumberNullPkt"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutNcrGenOutputTsBitRate"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutAlmGeneralAsiOutput"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutAlmNoOutputSignal"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutAlmNoOutputSignalAsi1"),
        ("NEWTEC-ASIOUT-MIB", "ntcAsiOutAlmNoOutputSignalAsi2"))
)
if mibBuilder.loadTexts:
    ntcAsiOutConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcAsiOutConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 900, 2, 1, 1)
)
ntcAsiOutConfCompV1Standard.setObjects(
    ("NEWTEC-ASIOUT-MIB", "ntcAsiOutConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcAsiOutConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-ASIOUT-MIB",
    **{"ntcAsiOut": ntcAsiOut,
       "ntcAsiOutObjects": ntcAsiOutObjects,
       "ntcAsiOutInputSelection": ntcAsiOutInputSelection,
       "ntcAsiOutOutputSelection": ntcAsiOutOutputSelection,
       "ntcAsiOutMeasuredTsBitRate": ntcAsiOutMeasuredTsBitRate,
       "ntcAsiOutPrbsGenerator": ntcAsiOutPrbsGenerator,
       "ntcAsiOutPrbsGenOutputTsBitRate": ntcAsiOutPrbsGenOutputTsBitRate,
       "ntcAsiOutPrbsGenType": ntcAsiOutPrbsGenType,
       "ntcAsiOutPrbsGenPidHandling": ntcAsiOutPrbsGenPidHandling,
       "ntcAsiOutPrbsGenPidValue": ntcAsiOutPrbsGenPidValue,
       "ntcAsiOutPrbsGenNumberDataPkt": ntcAsiOutPrbsGenNumberDataPkt,
       "ntcAsiOutPrbsGenNumberNullPkt": ntcAsiOutPrbsGenNumberNullPkt,
       "ntcAsiOutNcrGenerator": ntcAsiOutNcrGenerator,
       "ntcAsiOutNcrGenOutputTsBitRate": ntcAsiOutNcrGenOutputTsBitRate,
       "ntcAsiOutAlarm": ntcAsiOutAlarm,
       "ntcAsiOutAlmGeneralAsiOutput": ntcAsiOutAlmGeneralAsiOutput,
       "ntcAsiOutAlmNoOutputSignal": ntcAsiOutAlmNoOutputSignal,
       "ntcAsiOutAlmNoOutputSignalAsi1": ntcAsiOutAlmNoOutputSignalAsi1,
       "ntcAsiOutAlmNoOutputSignalAsi2": ntcAsiOutAlmNoOutputSignalAsi2,
       "ntcAsiOutConformance": ntcAsiOutConformance,
       "ntcAsiOutConfCompliance": ntcAsiOutConfCompliance,
       "ntcAsiOutConfCompV1Standard": ntcAsiOutConfCompV1Standard,
       "ntcAsiOutConfGroup": ntcAsiOutConfGroup,
       "ntcAsiOutConfGrpV1Standard": ntcAsiOutConfGrpV1Standard}
)
