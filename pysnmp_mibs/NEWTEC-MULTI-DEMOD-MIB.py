# SNMP MIB module (NEWTEC-MULTI-DEMOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-MULTI-DEMOD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:57 2025
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
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcMultiDemodulator = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300)
)
if mibBuilder.loadTexts:
    ntcMultiDemodulator.setRevisions(
        ("2018-02-02 09:00",
         "2017-07-10 12:00",
         "2016-10-24 12:00",
         "2016-05-17 09:00",
         "2016-02-01 11:00",
         "2015-09-25 11:00",
         "2015-02-19 09:00",
         "2015-02-04 08:00",
         "2014-11-24 12:00",
         "2014-10-31 08:00",
         "2014-09-23 07:00",
         "2014-09-04 12:00",
         "2014-07-08 09:00",
         "2014-02-03 12:00",
         "2013-10-16 12:00",
         "2013-09-23 08:00",
         "2013-08-21 06:00",
         "2013-07-05 06:00",
         "2013-06-25 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcMultiDemodObjects_ObjectIdentity = ObjectIdentity
ntcMultiDemodObjects = _NtcMultiDemodObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodObjects.setStatus("current")
_NtcMultiDemodAlarm_ObjectIdentity = ObjectIdentity
ntcMultiDemodAlarm = _NtcMultiDemodAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAlarm.setStatus("current")
_NtcMultiDemodAlmGeneralDemod_Type = NtcAlarmState
_NtcMultiDemodAlmGeneralDemod_Object = MibScalar
ntcMultiDemodAlmGeneralDemod = _NtcMultiDemodAlmGeneralDemod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 1),
    _NtcMultiDemodAlmGeneralDemod_Type()
)
ntcMultiDemodAlmGeneralDemod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmGeneralDemod.setStatus("current")
_NtcMultiDemodAlmInternalError_Type = NtcAlarmState
_NtcMultiDemodAlmInternalError_Object = MibScalar
ntcMultiDemodAlmInternalError = _NtcMultiDemodAlmInternalError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 2),
    _NtcMultiDemodAlmInternalError_Type()
)
ntcMultiDemodAlmInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmInternalError.setStatus("current")
_NtcMultiDemodAlmInputSaturated_Type = NtcAlarmState
_NtcMultiDemodAlmInputSaturated_Object = MibScalar
ntcMultiDemodAlmInputSaturated = _NtcMultiDemodAlmInputSaturated_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 3),
    _NtcMultiDemodAlmInputSaturated_Type()
)
ntcMultiDemodAlmInputSaturated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmInputSaturated.setStatus("current")
_NtcMultiDemodAlmNoLock_Type = NtcAlarmState
_NtcMultiDemodAlmNoLock_Object = MibScalar
ntcMultiDemodAlmNoLock = _NtcMultiDemodAlmNoLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 4),
    _NtcMultiDemodAlmNoLock_Type()
)
ntcMultiDemodAlmNoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmNoLock.setStatus("current")
_NtcMultiDemodAlmLnbPowerControl_Type = NtcAlarmState
_NtcMultiDemodAlmLnbPowerControl_Object = MibScalar
ntcMultiDemodAlmLnbPowerControl = _NtcMultiDemodAlmLnbPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 5),
    _NtcMultiDemodAlmLnbPowerControl_Type()
)
ntcMultiDemodAlmLnbPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmLnbPowerControl.setStatus("current")
_NtcMultiDemodAlmDecoderOvrload_Type = NtcAlarmState
_NtcMultiDemodAlmDecoderOvrload_Object = MibScalar
ntcMultiDemodAlmDecoderOvrload = _NtcMultiDemodAlmDecoderOvrload_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 6),
    _NtcMultiDemodAlmDecoderOvrload_Type()
)
ntcMultiDemodAlmDecoderOvrload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmDecoderOvrload.setStatus("current")
_NtcMultiDemodAlmNoPlLock_Type = NtcAlarmState
_NtcMultiDemodAlmNoPlLock_Object = MibScalar
ntcMultiDemodAlmNoPlLock = _NtcMultiDemodAlmNoPlLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 7),
    _NtcMultiDemodAlmNoPlLock_Type()
)
ntcMultiDemodAlmNoPlLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmNoPlLock.setStatus("current")
_NtcMultiDemodAlmBufferOverflow_Type = NtcAlarmState
_NtcMultiDemodAlmBufferOverflow_Object = MibScalar
ntcMultiDemodAlmBufferOverflow = _NtcMultiDemodAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 1, 8),
    _NtcMultiDemodAlmBufferOverflow_Type()
)
ntcMultiDemodAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAlmBufferOverflow.setStatus("current")
_NtcMultiDemodAlarmStateTable_Object = MibTable
ntcMultiDemodAlarmStateTable = _NtcMultiDemodAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAlarmStateTable.setStatus("current")
_NtcMultiDemodAlarmStateEntry_Object = MibTableRow
ntcMultiDemodAlarmStateEntry = _NtcMultiDemodAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1)
)
ntcMultiDemodAlarmStateEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASDemodId"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodAlarmStateEntry.setStatus("current")


class _NtcMultiDemodASDemodId_Type(Integer32):
    """Custom type ntcMultiDemodASDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodASDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodASDemodId_Object = MibTableColumn
ntcMultiDemodASDemodId = _NtcMultiDemodASDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 1),
    _NtcMultiDemodASDemodId_Type()
)
ntcMultiDemodASDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodASDemodId.setStatus("current")
_NtcMultiDemodASGeneralDemod_Type = NtcAlarmState
_NtcMultiDemodASGeneralDemod_Object = MibTableColumn
ntcMultiDemodASGeneralDemod = _NtcMultiDemodASGeneralDemod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 2),
    _NtcMultiDemodASGeneralDemod_Type()
)
ntcMultiDemodASGeneralDemod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASGeneralDemod.setStatus("current")
_NtcMultiDemodASInternalError_Type = NtcAlarmState
_NtcMultiDemodASInternalError_Object = MibTableColumn
ntcMultiDemodASInternalError = _NtcMultiDemodASInternalError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 3),
    _NtcMultiDemodASInternalError_Type()
)
ntcMultiDemodASInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASInternalError.setStatus("current")
_NtcMultiDemodASInputSaturated_Type = NtcAlarmState
_NtcMultiDemodASInputSaturated_Object = MibTableColumn
ntcMultiDemodASInputSaturated = _NtcMultiDemodASInputSaturated_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 4),
    _NtcMultiDemodASInputSaturated_Type()
)
ntcMultiDemodASInputSaturated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASInputSaturated.setStatus("current")
_NtcMultiDemodASNoPlLock_Type = NtcAlarmState
_NtcMultiDemodASNoPlLock_Object = MibTableColumn
ntcMultiDemodASNoPlLock = _NtcMultiDemodASNoPlLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 5),
    _NtcMultiDemodASNoPlLock_Type()
)
ntcMultiDemodASNoPlLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASNoPlLock.setStatus("current")
_NtcMultiDemodASNoLock_Type = NtcAlarmState
_NtcMultiDemodASNoLock_Object = MibTableColumn
ntcMultiDemodASNoLock = _NtcMultiDemodASNoLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 6),
    _NtcMultiDemodASNoLock_Type()
)
ntcMultiDemodASNoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASNoLock.setStatus("current")
_NtcMultiDemodASLnbPowerControl_Type = NtcAlarmState
_NtcMultiDemodASLnbPowerControl_Object = MibTableColumn
ntcMultiDemodASLnbPowerControl = _NtcMultiDemodASLnbPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 7),
    _NtcMultiDemodASLnbPowerControl_Type()
)
ntcMultiDemodASLnbPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASLnbPowerControl.setStatus("current")
_NtcMultiDemodASDecoderOverloaded_Type = NtcAlarmState
_NtcMultiDemodASDecoderOverloaded_Object = MibTableColumn
ntcMultiDemodASDecoderOverloaded = _NtcMultiDemodASDecoderOverloaded_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 2, 1, 8),
    _NtcMultiDemodASDecoderOverloaded_Type()
)
ntcMultiDemodASDecoderOverloaded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodASDecoderOverloaded.setStatus("current")
_NtcMultiDemodCfgTable_Object = MibTable
ntcMultiDemodCfgTable = _NtcMultiDemodCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3)
)
if mibBuilder.loadTexts:
    ntcMultiDemodCfgTable.setStatus("current")
_NtcMultiDemodCfgEntry_Object = MibTableRow
ntcMultiDemodCfgEntry = _NtcMultiDemodCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1)
)
ntcMultiDemodCfgEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgDemodId"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodCfgEntry.setStatus("current")


class _NtcMultiDemodCfgDemodId_Type(Integer32):
    """Custom type ntcMultiDemodCfgDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodCfgDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodCfgDemodId_Object = MibTableColumn
ntcMultiDemodCfgDemodId = _NtcMultiDemodCfgDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 1),
    _NtcMultiDemodCfgDemodId_Type()
)
ntcMultiDemodCfgDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgDemodId.setStatus("current")


class _NtcMultiDemodCfgEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodCfgEnable based on NtcEnable"""
    defaultValue = 1


_NtcMultiDemodCfgEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodCfgEnable_Object = MibTableColumn
ntcMultiDemodCfgEnable = _NtcMultiDemodCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 2),
    _NtcMultiDemodCfgEnable_Type()
)
ntcMultiDemodCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgEnable.setStatus("current")


class _NtcMultiDemodCfgMode_Type(Integer32):
    """Custom type ntcMultiDemodCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dvbs", 0),
          ("dvbs2", 1),
          ("s2ext", 3),
          ("turbo", 4),
          ("amcdvbs", 5),
          ("amcnbc", 6),
          ("dvbs2x", 7),
          ("amcdl", 8))
    )


_NtcMultiDemodCfgMode_Type.__name__ = "Integer32"
_NtcMultiDemodCfgMode_Object = MibTableColumn
ntcMultiDemodCfgMode = _NtcMultiDemodCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 3),
    _NtcMultiDemodCfgMode_Type()
)
ntcMultiDemodCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgMode.setStatus("current")


class _NtcMultiDemodCfgInputFrequency_Type(Unsigned32):
    """Custom type ntcMultiDemodCfgInputFrequency based on Unsigned32"""
    defaultValue = 2000000000


_NtcMultiDemodCfgInputFrequency_Type.__name__ = "Unsigned32"
_NtcMultiDemodCfgInputFrequency_Object = MibTableColumn
ntcMultiDemodCfgInputFrequency = _NtcMultiDemodCfgInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 4),
    _NtcMultiDemodCfgInputFrequency_Type()
)
ntcMultiDemodCfgInputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgInputFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgInputFrequency.setUnits("Hz")


class _NtcMultiDemodCfgSymbolRate_Type(Unsigned32):
    """Custom type ntcMultiDemodCfgSymbolRate based on Unsigned32"""
    defaultValue = 10000000


_NtcMultiDemodCfgSymbolRate_Type.__name__ = "Unsigned32"
_NtcMultiDemodCfgSymbolRate_Object = MibTableColumn
ntcMultiDemodCfgSymbolRate = _NtcMultiDemodCfgSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 5),
    _NtcMultiDemodCfgSymbolRate_Type()
)
ntcMultiDemodCfgSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgSymbolRate.setUnits("baud")


class _NtcMultiDemodCfgRollOff_Type(Integer32):
    """Custom type ntcMultiDemodCfgRollOff based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("rolloff5", 1),
          ("rolloff10", 2),
          ("rolloff15", 3),
          ("rolloff20", 4),
          ("rolloff25", 5),
          ("rolloff35", 6))
    )


_NtcMultiDemodCfgRollOff_Type.__name__ = "Integer32"
_NtcMultiDemodCfgRollOff_Object = MibTableColumn
ntcMultiDemodCfgRollOff = _NtcMultiDemodCfgRollOff_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 6),
    _NtcMultiDemodCfgRollOff_Type()
)
ntcMultiDemodCfgRollOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgRollOff.setStatus("current")


class _NtcMultiDemodCfgInputSelection_Type(Integer32):
    """Custom type ntcMultiDemodCfgInputSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lbandRxA", 0),
          ("lbandRxB", 1),
          ("ifRx", 3))
    )


_NtcMultiDemodCfgInputSelection_Type.__name__ = "Integer32"
_NtcMultiDemodCfgInputSelection_Object = MibTableColumn
ntcMultiDemodCfgInputSelection = _NtcMultiDemodCfgInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 7),
    _NtcMultiDemodCfgInputSelection_Type()
)
ntcMultiDemodCfgInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgInputSelection.setStatus("current")


class _NtcMultiDemodCfgSpectralInv_Type(Integer32):
    """Custom type ntcMultiDemodCfgSpectralInv based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("inverted", 1),
          ("automatic", 2))
    )


_NtcMultiDemodCfgSpectralInv_Type.__name__ = "Integer32"
_NtcMultiDemodCfgSpectralInv_Object = MibTableColumn
ntcMultiDemodCfgSpectralInv = _NtcMultiDemodCfgSpectralInv_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 8),
    _NtcMultiDemodCfgSpectralInv_Type()
)
ntcMultiDemodCfgSpectralInv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgSpectralInv.setStatus("current")


class _NtcMultiDemodCfgPlScrambSig_Type(Unsigned32):
    """Custom type ntcMultiDemodCfgPlScrambSig based on Unsigned32"""
    defaultValue = 0


_NtcMultiDemodCfgPlScrambSig_Type.__name__ = "Unsigned32"
_NtcMultiDemodCfgPlScrambSig_Object = MibTableColumn
ntcMultiDemodCfgPlScrambSig = _NtcMultiDemodCfgPlScrambSig_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 9),
    _NtcMultiDemodCfgPlScrambSig_Type()
)
ntcMultiDemodCfgPlScrambSig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgPlScrambSig.setStatus("current")


class _NtcMultiDemodCfgLnbPowerSupply_Type(Integer32):
    """Custom type ntcMultiDemodCfgLnbPowerSupply based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("e13V0kHz", 1),
          ("e13V22kHz", 2),
          ("e18V0kHz", 3),
          ("e18V22kHz", 4))
    )


_NtcMultiDemodCfgLnbPowerSupply_Type.__name__ = "Integer32"
_NtcMultiDemodCfgLnbPowerSupply_Object = MibTableColumn
ntcMultiDemodCfgLnbPowerSupply = _NtcMultiDemodCfgLnbPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 10),
    _NtcMultiDemodCfgLnbPowerSupply_Type()
)
ntcMultiDemodCfgLnbPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgLnbPowerSupply.setStatus("current")


class _NtcMultiDemodCfgHardwareId_Type(DisplayString):
    """Custom type ntcMultiDemodCfgHardwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NtcMultiDemodCfgHardwareId_Type.__name__ = "DisplayString"
_NtcMultiDemodCfgHardwareId_Object = MibTableColumn
ntcMultiDemodCfgHardwareId = _NtcMultiDemodCfgHardwareId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 11),
    _NtcMultiDemodCfgHardwareId_Type()
)
ntcMultiDemodCfgHardwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgHardwareId.setStatus("current")


class _NtcMultiDemodCfgModCodDvbs_Type(Integer32):
    """Custom type ntcMultiDemodCfgModCodDvbs based on Integer32"""
    defaultValue = 3

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("qpsk12", 1),
          ("qpsk23", 2),
          ("qpsk34", 3),
          ("qpsk56", 4),
          ("qpsk67", 5),
          ("qpsk78", 6),
          ("e8psk23", 7),
          ("e8psk56", 8),
          ("e8psk89", 9),
          ("e16qam34", 10),
          ("e16qam78", 11))
    )


_NtcMultiDemodCfgModCodDvbs_Type.__name__ = "Integer32"
_NtcMultiDemodCfgModCodDvbs_Object = MibTableColumn
ntcMultiDemodCfgModCodDvbs = _NtcMultiDemodCfgModCodDvbs_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 12),
    _NtcMultiDemodCfgModCodDvbs_Type()
)
ntcMultiDemodCfgModCodDvbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgModCodDvbs.setStatus("current")


class _NtcMultiDemodCfgStreamMode_Type(Integer32):
    """Custom type ntcMultiDemodCfgStreamMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multistream", 1),
          ("singlestream", 2))
    )


_NtcMultiDemodCfgStreamMode_Type.__name__ = "Integer32"
_NtcMultiDemodCfgStreamMode_Object = MibTableColumn
ntcMultiDemodCfgStreamMode = _NtcMultiDemodCfgStreamMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 13),
    _NtcMultiDemodCfgStreamMode_Type()
)
ntcMultiDemodCfgStreamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgStreamMode.setStatus("current")
_NtcMultiDemodCfgInterfaceRate_Type = Unsigned32
_NtcMultiDemodCfgInterfaceRate_Object = MibTableColumn
ntcMultiDemodCfgInterfaceRate = _NtcMultiDemodCfgInterfaceRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 14),
    _NtcMultiDemodCfgInterfaceRate_Type()
)
ntcMultiDemodCfgInterfaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgInterfaceRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgInterfaceRate.setUnits("bps")


class _NtcMultiDemodCfgAcqRange_Type(Unsigned32):
    """Custom type ntcMultiDemodCfgAcqRange based on Unsigned32"""
    defaultValue = 1000000


_NtcMultiDemodCfgAcqRange_Type.__name__ = "Unsigned32"
_NtcMultiDemodCfgAcqRange_Object = MibTableColumn
ntcMultiDemodCfgAcqRange = _NtcMultiDemodCfgAcqRange_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 15),
    _NtcMultiDemodCfgAcqRange_Type()
)
ntcMultiDemodCfgAcqRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgAcqRange.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgAcqRange.setUnits("Hz")


class _NtcMultiDemodCfgPlhdrScramSeq_Type(Unsigned32):
    """Custom type ntcMultiDemodCfgPlhdrScramSeq based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_NtcMultiDemodCfgPlhdrScramSeq_Type.__name__ = "Unsigned32"
_NtcMultiDemodCfgPlhdrScramSeq_Object = MibTableColumn
ntcMultiDemodCfgPlhdrScramSeq = _NtcMultiDemodCfgPlhdrScramSeq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 16),
    _NtcMultiDemodCfgPlhdrScramSeq_Type()
)
ntcMultiDemodCfgPlhdrScramSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgPlhdrScramSeq.setStatus("current")


class _NtcMultiDemodCfgRfFrequency_Type(DisplayString):
    """Custom type ntcMultiDemodCfgRfFrequency based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcMultiDemodCfgRfFrequency_Type.__name__ = "DisplayString"
_NtcMultiDemodCfgRfFrequency_Object = MibTableColumn
ntcMultiDemodCfgRfFrequency = _NtcMultiDemodCfgRfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 17),
    _NtcMultiDemodCfgRfFrequency_Type()
)
ntcMultiDemodCfgRfFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgRfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgRfFrequency.setUnits("Hz")


class _NtcMultiDemodCfgModCodAmcDl_Type(Integer32):
    """Custom type ntcMultiDemodCfgModCodAmcDl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qpsk12", 1),
          ("qpsk23", 2),
          ("qpsk67", 3))
    )


_NtcMultiDemodCfgModCodAmcDl_Type.__name__ = "Integer32"
_NtcMultiDemodCfgModCodAmcDl_Object = MibTableColumn
ntcMultiDemodCfgModCodAmcDl = _NtcMultiDemodCfgModCodAmcDl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 18),
    _NtcMultiDemodCfgModCodAmcDl_Type()
)
ntcMultiDemodCfgModCodAmcDl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgModCodAmcDl.setStatus("current")


class _NtcMultiDemodCfgLnbClockRef_Type(Integer32):
    """Custom type ntcMultiDemodCfgLnbClockRef based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("e10Mhz", 1))
    )


_NtcMultiDemodCfgLnbClockRef_Type.__name__ = "Integer32"
_NtcMultiDemodCfgLnbClockRef_Object = MibTableColumn
ntcMultiDemodCfgLnbClockRef = _NtcMultiDemodCfgLnbClockRef_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 3, 1, 19),
    _NtcMultiDemodCfgLnbClockRef_Type()
)
ntcMultiDemodCfgLnbClockRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCfgLnbClockRef.setStatus("current")
_NtcExtMultiDemodCfgTable_Object = MibTable
ntcExtMultiDemodCfgTable = _NtcExtMultiDemodCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 4)
)
if mibBuilder.loadTexts:
    ntcExtMultiDemodCfgTable.setStatus("current")
_NtcExtMultiDemodCfgEntry_Object = MibTableRow
ntcExtMultiDemodCfgEntry = _NtcExtMultiDemodCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 4, 1)
)
ntcExtMultiDemodCfgEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcExtMultiDemodCfgDemodId"),
)
if mibBuilder.loadTexts:
    ntcExtMultiDemodCfgEntry.setStatus("current")


class _NtcExtMultiDemodCfgDemodId_Type(Integer32):
    """Custom type ntcExtMultiDemodCfgDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcExtMultiDemodCfgDemodId_Type.__name__ = "Integer32"
_NtcExtMultiDemodCfgDemodId_Object = MibTableColumn
ntcExtMultiDemodCfgDemodId = _NtcExtMultiDemodCfgDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 4, 1, 1),
    _NtcExtMultiDemodCfgDemodId_Type()
)
ntcExtMultiDemodCfgDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcExtMultiDemodCfgDemodId.setStatus("current")


class _NtcExtMultiDemodCfgOpMode_Type(Integer32):
    """Custom type ntcExtMultiDemodCfgOpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("multiple", 2),
          ("singlelin", 3))
    )


_NtcExtMultiDemodCfgOpMode_Type.__name__ = "Integer32"
_NtcExtMultiDemodCfgOpMode_Object = MibTableColumn
ntcExtMultiDemodCfgOpMode = _NtcExtMultiDemodCfgOpMode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 4, 1, 2),
    _NtcExtMultiDemodCfgOpMode_Type()
)
ntcExtMultiDemodCfgOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcExtMultiDemodCfgOpMode.setStatus("current")
_NtcMultiDemodMonTable_Object = MibTable
ntcMultiDemodMonTable = _NtcMultiDemodMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5)
)
if mibBuilder.loadTexts:
    ntcMultiDemodMonTable.setStatus("current")
_NtcMultiDemodMonEntry_Object = MibTableRow
ntcMultiDemodMonEntry = _NtcMultiDemodMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1)
)
ntcMultiDemodMonEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonDemodId"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodMonEntry.setStatus("current")


class _NtcMultiDemodMonDemodId_Type(Integer32):
    """Custom type ntcMultiDemodMonDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodMonDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodMonDemodId_Object = MibTableColumn
ntcMultiDemodMonDemodId = _NtcMultiDemodMonDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 1),
    _NtcMultiDemodMonDemodId_Type()
)
ntcMultiDemodMonDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodMonDemodId.setStatus("current")


class _NtcMultiDemodMonLbandInputLvl_Type(Integer32):
    """Custom type ntcMultiDemodMonLbandInputLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )


_NtcMultiDemodMonLbandInputLvl_Type.__name__ = "Integer32"
_NtcMultiDemodMonLbandInputLvl_Object = MibTableColumn
ntcMultiDemodMonLbandInputLvl = _NtcMultiDemodMonLbandInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 2),
    _NtcMultiDemodMonLbandInputLvl_Type()
)
ntcMultiDemodMonLbandInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonLbandInputLvl.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonLbandInputLvl.setUnits("dBm")


class _NtcMultiDemodMonCarrierInputLvl_Type(Integer32):
    """Custom type ntcMultiDemodMonCarrierInputLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )


_NtcMultiDemodMonCarrierInputLvl_Type.__name__ = "Integer32"
_NtcMultiDemodMonCarrierInputLvl_Object = MibTableColumn
ntcMultiDemodMonCarrierInputLvl = _NtcMultiDemodMonCarrierInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 3),
    _NtcMultiDemodMonCarrierInputLvl_Type()
)
ntcMultiDemodMonCarrierInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonCarrierInputLvl.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonCarrierInputLvl.setUnits("dBm")


class _NtcMultiDemodMonEsNo_Type(Integer32):
    """Custom type ntcMultiDemodMonEsNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 3000),
    )


_NtcMultiDemodMonEsNo_Type.__name__ = "Integer32"
_NtcMultiDemodMonEsNo_Object = MibTableColumn
ntcMultiDemodMonEsNo = _NtcMultiDemodMonEsNo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 4),
    _NtcMultiDemodMonEsNo_Type()
)
ntcMultiDemodMonEsNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonEsNo.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonEsNo.setUnits("dB")
_NtcMultiDemodMonPhaseNoiseIndic_Type = Float32TC
_NtcMultiDemodMonPhaseNoiseIndic_Object = MibTableColumn
ntcMultiDemodMonPhaseNoiseIndic = _NtcMultiDemodMonPhaseNoiseIndic_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 5),
    _NtcMultiDemodMonPhaseNoiseIndic_Type()
)
ntcMultiDemodMonPhaseNoiseIndic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonPhaseNoiseIndic.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonPhaseNoiseIndic.setUnits("deg.")


class _NtcMultiDemodMonOffRefMask_Type(Integer32):
    """Custom type ntcMultiDemodMonOffRefMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )


_NtcMultiDemodMonOffRefMask_Type.__name__ = "Integer32"
_NtcMultiDemodMonOffRefMask_Object = MibTableColumn
ntcMultiDemodMonOffRefMask = _NtcMultiDemodMonOffRefMask_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 6),
    _NtcMultiDemodMonOffRefMask_Type()
)
ntcMultiDemodMonOffRefMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonOffRefMask.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonOffRefMask.setUnits("dB")


class _NtcMultiDemodMonNonLinIndic_Type(Integer32):
    """Custom type ntcMultiDemodMonNonLinIndic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_NtcMultiDemodMonNonLinIndic_Type.__name__ = "Integer32"
_NtcMultiDemodMonNonLinIndic_Object = MibTableColumn
ntcMultiDemodMonNonLinIndic = _NtcMultiDemodMonNonLinIndic_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 7),
    _NtcMultiDemodMonNonLinIndic_Type()
)
ntcMultiDemodMonNonLinIndic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonNonLinIndic.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonNonLinIndic.setUnits("%")
_NtcMultiDemodMonSymbolRate_Type = Unsigned32
_NtcMultiDemodMonSymbolRate_Object = MibTableColumn
ntcMultiDemodMonSymbolRate = _NtcMultiDemodMonSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 8),
    _NtcMultiDemodMonSymbolRate_Type()
)
ntcMultiDemodMonSymbolRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonSymbolRate.setUnits("baud")
_NtcMultiDemodMonCarrierOffset_Type = Float32TC
_NtcMultiDemodMonCarrierOffset_Object = MibTableColumn
ntcMultiDemodMonCarrierOffset = _NtcMultiDemodMonCarrierOffset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 9),
    _NtcMultiDemodMonCarrierOffset_Type()
)
ntcMultiDemodMonCarrierOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonCarrierOffset.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonCarrierOffset.setUnits("Hz")
_NtcMultiDemodMonFrameCounter_Type = Counter32
_NtcMultiDemodMonFrameCounter_Object = MibTableColumn
ntcMultiDemodMonFrameCounter = _NtcMultiDemodMonFrameCounter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 10),
    _NtcMultiDemodMonFrameCounter_Type()
)
ntcMultiDemodMonFrameCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonFrameCounter.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonFrameCounter.setUnits("frames")
_NtcMultiDemodMonDummyFrameCtr_Type = Counter32
_NtcMultiDemodMonDummyFrameCtr_Object = MibTableColumn
ntcMultiDemodMonDummyFrameCtr = _NtcMultiDemodMonDummyFrameCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 11),
    _NtcMultiDemodMonDummyFrameCtr_Type()
)
ntcMultiDemodMonDummyFrameCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonDummyFrameCtr.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonDummyFrameCtr.setUnits("frames")
_NtcMultiDemodMonErroredFrameCtr_Type = Counter32
_NtcMultiDemodMonErroredFrameCtr_Object = MibTableColumn
ntcMultiDemodMonErroredFrameCtr = _NtcMultiDemodMonErroredFrameCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 12),
    _NtcMultiDemodMonErroredFrameCtr_Type()
)
ntcMultiDemodMonErroredFrameCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonErroredFrameCtr.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonErroredFrameCtr.setUnits("frames")
_NtcMultiDemodMonCycleSlipCtr_Type = Counter32
_NtcMultiDemodMonCycleSlipCtr_Object = MibTableColumn
ntcMultiDemodMonCycleSlipCtr = _NtcMultiDemodMonCycleSlipCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 13),
    _NtcMultiDemodMonCycleSlipCtr_Type()
)
ntcMultiDemodMonCycleSlipCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonCycleSlipCtr.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonCycleSlipCtr.setUnits("frames")


class _NtcMultiDemodMonLastModCod_Type(Integer32):
    """Custom type ntcMultiDemodMonLastModCod based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215),
          ("qpsk1345", 256),
          ("qpsk920", 257),
          ("qpsk1120", 258),
          ("e8apsk59l", 259),
          ("e8apsk2645l", 260),
          ("e8psk2336", 261),
          ("e8psk2536", 262),
          ("e8psk1318", 263),
          ("e16apsk12l", 264),
          ("e16apsk815l", 265),
          ("e16apsk59l", 266),
          ("e16apsk2645", 267),
          ("e16apsk35", 268),
          ("e16apsk35l", 269),
          ("e16apsk2845", 270),
          ("e16apsk2336", 271),
          ("e16apsk23l", 272),
          ("e16apsk2536", 273),
          ("e16apsk1318", 274),
          ("e16apsk79", 275),
          ("e16apsk7790", 276),
          ("e32apsk23l", 277),
          ("e32apsk3245", 278),
          ("e32apsk1115", 279),
          ("e32apsk79", 280),
          ("e64apsk3245l", 281),
          ("e64apsk1115", 282),
          ("e64apsk79", 283),
          ("e64apsk45", 284),
          ("e64apsk56", 285),
          ("e128apsk34", 286),
          ("e128apsk79", 287),
          ("e256apsk2945l", 288),
          ("e256apsk23l", 289),
          ("e256apsk3145l", 290),
          ("e256apsk3245", 291),
          ("e256apsk1115l", 292),
          ("e256apsk34", 293),
          ("qpsk1145", 294),
          ("qpsk415", 295),
          ("qpsk1445", 296),
          ("qpsk715", 297),
          ("qpsk815", 298),
          ("qpsk3245", 299),
          ("e8psk715", 300),
          ("e8psk815", 301),
          ("e8psk2645", 302),
          ("e8psk3245", 303),
          ("e16apsk715", 304),
          ("e16apsk815", 305),
          ("e16apsk3245", 306),
          ("e32apsk23", 307))
    )


_NtcMultiDemodMonLastModCod_Type.__name__ = "Integer32"
_NtcMultiDemodMonLastModCod_Object = MibTableColumn
ntcMultiDemodMonLastModCod = _NtcMultiDemodMonLastModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 14),
    _NtcMultiDemodMonLastModCod_Type()
)
ntcMultiDemodMonLastModCod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonLastModCod.setStatus("current")


class _NtcMultiDemodModCodStatsReset_Type(Integer32):
    """Custom type ntcMultiDemodModCodStatsReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcMultiDemodModCodStatsReset_Type.__name__ = "Integer32"
_NtcMultiDemodModCodStatsReset_Object = MibTableColumn
ntcMultiDemodModCodStatsReset = _NtcMultiDemodModCodStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 15),
    _NtcMultiDemodModCodStatsReset_Type()
)
ntcMultiDemodModCodStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodModCodStatsReset.setStatus("current")


class _NtcMultiDemodMonVber_Type(Integer32):
    """Custom type ntcMultiDemodMonVber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_NtcMultiDemodMonVber_Type.__name__ = "Integer32"
_NtcMultiDemodMonVber_Object = MibTableColumn
ntcMultiDemodMonVber = _NtcMultiDemodMonVber_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 16),
    _NtcMultiDemodMonVber_Type()
)
ntcMultiDemodMonVber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonVber.setStatus("current")


class _NtcMultiDemodMonBer_Type(Integer32):
    """Custom type ntcMultiDemodMonBer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_NtcMultiDemodMonBer_Type.__name__ = "Integer32"
_NtcMultiDemodMonBer_Object = MibTableColumn
ntcMultiDemodMonBer = _NtcMultiDemodMonBer_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 17),
    _NtcMultiDemodMonBer_Type()
)
ntcMultiDemodMonBer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonBer.setStatus("current")


class _NtcMultiDemodMonEbNo_Type(Integer32):
    """Custom type ntcMultiDemodMonEbNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2500),
    )


_NtcMultiDemodMonEbNo_Type.__name__ = "Integer32"
_NtcMultiDemodMonEbNo_Object = MibTableColumn
ntcMultiDemodMonEbNo = _NtcMultiDemodMonEbNo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 18),
    _NtcMultiDemodMonEbNo_Type()
)
ntcMultiDemodMonEbNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonEbNo.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonEbNo.setUnits("dB")


class _NtcMultiDemodMonLinkMargin_Type(Integer32):
    """Custom type ntcMultiDemodMonLinkMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-500, 2500),
    )


_NtcMultiDemodMonLinkMargin_Type.__name__ = "Integer32"
_NtcMultiDemodMonLinkMargin_Object = MibTableColumn
ntcMultiDemodMonLinkMargin = _NtcMultiDemodMonLinkMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 19),
    _NtcMultiDemodMonLinkMargin_Type()
)
ntcMultiDemodMonLinkMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonLinkMargin.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonLinkMargin.setUnits("dB")


class _NtcMultiDemodMonOperationalState_Type(Integer32):
    """Custom type ntcMultiDemodMonOperationalState based on Integer32"""
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
        *(("operational", 0),
          ("failed", 1),
          ("offduty", 2),
          ("dependent", 3))
    )


_NtcMultiDemodMonOperationalState_Type.__name__ = "Integer32"
_NtcMultiDemodMonOperationalState_Object = MibTableColumn
ntcMultiDemodMonOperationalState = _NtcMultiDemodMonOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 20),
    _NtcMultiDemodMonOperationalState_Type()
)
ntcMultiDemodMonOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonOperationalState.setStatus("current")


class _NtcMultiDemodMonLastNonDumModCod_Type(Integer32):
    """Custom type ntcMultiDemodMonLastNonDumModCod based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215),
          ("qpsk1345", 256),
          ("qpsk920", 257),
          ("qpsk1120", 258),
          ("e8apsk59l", 259),
          ("e8apsk2645l", 260),
          ("e8psk2336", 261),
          ("e8psk2536", 262),
          ("e8psk1318", 263),
          ("e16apsk12l", 264),
          ("e16apsk815l", 265),
          ("e16apsk59l", 266),
          ("e16apsk2645", 267),
          ("e16apsk35", 268),
          ("e16apsk35l", 269),
          ("e16apsk2845", 270),
          ("e16apsk2336", 271),
          ("e16apsk23l", 272),
          ("e16apsk2536", 273),
          ("e16apsk1318", 274),
          ("e16apsk79", 275),
          ("e16apsk7790", 276),
          ("e32apsk23l", 277),
          ("e32apsk3245", 278),
          ("e32apsk1115", 279),
          ("e32apsk79", 280),
          ("e64apsk3245l", 281),
          ("e64apsk1115", 282),
          ("e64apsk79", 283),
          ("e64apsk45", 284),
          ("e64apsk56", 285),
          ("e128apsk34", 286),
          ("e128apsk79", 287),
          ("e256apsk2945l", 288),
          ("e256apsk23l", 289),
          ("e256apsk3145l", 290),
          ("e256apsk3245", 291),
          ("e256apsk1115l", 292),
          ("e256apsk34", 293),
          ("qpsk1145", 294),
          ("qpsk415", 295),
          ("qpsk1445", 296),
          ("qpsk715", 297),
          ("qpsk815", 298),
          ("qpsk3245", 299),
          ("e8psk715", 300),
          ("e8psk815", 301),
          ("e8psk2645", 302),
          ("e8psk3245", 303),
          ("e16apsk715", 304),
          ("e16apsk815", 305),
          ("e16apsk3245", 306),
          ("e32apsk23", 307))
    )


_NtcMultiDemodMonLastNonDumModCod_Type.__name__ = "Integer32"
_NtcMultiDemodMonLastNonDumModCod_Object = MibTableColumn
ntcMultiDemodMonLastNonDumModCod = _NtcMultiDemodMonLastNonDumModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 21),
    _NtcMultiDemodMonLastNonDumModCod_Type()
)
ntcMultiDemodMonLastNonDumModCod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonLastNonDumModCod.setStatus("current")


class _NtcMultiDemodMonRollOff_Type(Integer32):
    """Custom type ntcMultiDemodMonRollOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              100)
        )
    )
    namedValues = NamedValues(
        *(("rolloff5", 1),
          ("rolloff10", 2),
          ("rolloff15", 3),
          ("rolloff20", 4),
          ("rolloff25", 5),
          ("rolloff35", 6),
          ("unknown", 100))
    )


_NtcMultiDemodMonRollOff_Type.__name__ = "Integer32"
_NtcMultiDemodMonRollOff_Object = MibTableColumn
ntcMultiDemodMonRollOff = _NtcMultiDemodMonRollOff_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 22),
    _NtcMultiDemodMonRollOff_Type()
)
ntcMultiDemodMonRollOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonRollOff.setStatus("current")


class _NtcMultiDemodMonQefM_Type(Integer32):
    """Custom type ntcMultiDemodMonQefM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-80, 140),
    )


_NtcMultiDemodMonQefM_Type.__name__ = "Integer32"
_NtcMultiDemodMonQefM_Object = MibTableColumn
ntcMultiDemodMonQefM = _NtcMultiDemodMonQefM_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 23),
    _NtcMultiDemodMonQefM_Type()
)
ntcMultiDemodMonQefM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonQefM.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonQefM.setUnits("dB")


class _NtcMultiDemodMonSpectralInv_Type(Integer32):
    """Custom type ntcMultiDemodMonSpectralInv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("inverted", 1),
          ("unknown", 2))
    )


_NtcMultiDemodMonSpectralInv_Type.__name__ = "Integer32"
_NtcMultiDemodMonSpectralInv_Object = MibTableColumn
ntcMultiDemodMonSpectralInv = _NtcMultiDemodMonSpectralInv_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 24),
    _NtcMultiDemodMonSpectralInv_Type()
)
ntcMultiDemodMonSpectralInv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonSpectralInv.setStatus("current")


class _NtcMultiDemodMonVberClp_Type(Integer32):
    """Custom type ntcMultiDemodMonVberClp based on Integer32"""
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
        *(("exact", 0),
          ("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_NtcMultiDemodMonVberClp_Type.__name__ = "Integer32"
_NtcMultiDemodMonVberClp_Object = MibTableColumn
ntcMultiDemodMonVberClp = _NtcMultiDemodMonVberClp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 25),
    _NtcMultiDemodMonVberClp_Type()
)
ntcMultiDemodMonVberClp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonVberClp.setStatus("current")


class _NtcMultiDemodMonBerClp_Type(Integer32):
    """Custom type ntcMultiDemodMonBerClp based on Integer32"""
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
        *(("exact", 0),
          ("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_NtcMultiDemodMonBerClp_Type.__name__ = "Integer32"
_NtcMultiDemodMonBerClp_Object = MibTableColumn
ntcMultiDemodMonBerClp = _NtcMultiDemodMonBerClp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 26),
    _NtcMultiDemodMonBerClp_Type()
)
ntcMultiDemodMonBerClp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonBerClp.setStatus("current")


class _NtcMultiDemodMonQefMClp_Type(Integer32):
    """Custom type ntcMultiDemodMonQefMClp based on Integer32"""
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
        *(("exact", 0),
          ("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_NtcMultiDemodMonQefMClp_Type.__name__ = "Integer32"
_NtcMultiDemodMonQefMClp_Object = MibTableColumn
ntcMultiDemodMonQefMClp = _NtcMultiDemodMonQefMClp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 27),
    _NtcMultiDemodMonQefMClp_Type()
)
ntcMultiDemodMonQefMClp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonQefMClp.setStatus("current")


class _NtcMultiDemodMonEbNoClp_Type(Integer32):
    """Custom type ntcMultiDemodMonEbNoClp based on Integer32"""
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
        *(("exact", 0),
          ("down", 1),
          ("up", 2),
          ("unknown", 3))
    )


_NtcMultiDemodMonEbNoClp_Type.__name__ = "Integer32"
_NtcMultiDemodMonEbNoClp_Object = MibTableColumn
ntcMultiDemodMonEbNoClp = _NtcMultiDemodMonEbNoClp_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 28),
    _NtcMultiDemodMonEbNoClp_Type()
)
ntcMultiDemodMonEbNoClp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonEbNoClp.setStatus("current")


class _NtcMultiDemodMonNonLinIndicAM_Type(Integer32):
    """Custom type ntcMultiDemodMonNonLinIndicAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_NtcMultiDemodMonNonLinIndicAM_Type.__name__ = "Integer32"
_NtcMultiDemodMonNonLinIndicAM_Object = MibTableColumn
ntcMultiDemodMonNonLinIndicAM = _NtcMultiDemodMonNonLinIndicAM_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 5, 1, 29),
    _NtcMultiDemodMonNonLinIndicAM_Type()
)
ntcMultiDemodMonNonLinIndicAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodMonNonLinIndicAM.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodMonNonLinIndicAM.setUnits("%")
_NtcMultiDemodStatsTable_Object = MibTable
ntcMultiDemodStatsTable = _NtcMultiDemodStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6)
)
if mibBuilder.loadTexts:
    ntcMultiDemodStatsTable.setStatus("current")
_NtcMultiDemodStatsEntry_Object = MibTableRow
ntcMultiDemodStatsEntry = _NtcMultiDemodStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1)
)
ntcMultiDemodStatsEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsInx"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodStatsEntry.setStatus("current")
_NtcMultiDemodStatsInx_Type = Unsigned32
_NtcMultiDemodStatsInx_Object = MibTableColumn
ntcMultiDemodStatsInx = _NtcMultiDemodStatsInx_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 1),
    _NtcMultiDemodStatsInx_Type()
)
ntcMultiDemodStatsInx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsInx.setStatus("current")


class _NtcMultiDemodStatsDemodId_Type(Integer32):
    """Custom type ntcMultiDemodStatsDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodStatsDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodStatsDemodId_Object = MibTableColumn
ntcMultiDemodStatsDemodId = _NtcMultiDemodStatsDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 2),
    _NtcMultiDemodStatsDemodId_Type()
)
ntcMultiDemodStatsDemodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsDemodId.setStatus("current")


class _NtcMultiDemodStatsModCod_Type(Integer32):
    """Custom type ntcMultiDemodStatsModCod based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              215,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              263,
              264,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              283,
              284,
              285,
              286,
              287,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307)
        )
    )
    namedValues = NamedValues(
        *(("qpsk14", 1),
          ("qpsk13", 2),
          ("qpsk25", 3),
          ("qpsk12", 4),
          ("qpsk35", 5),
          ("qpsk23", 6),
          ("qpsk34", 7),
          ("qpsk45", 8),
          ("qpsk56", 9),
          ("qpsk89", 10),
          ("qpsk910", 11),
          ("e8psk35", 12),
          ("e8psk23", 13),
          ("e8psk34", 14),
          ("e8psk56", 15),
          ("e8psk89", 16),
          ("e8psk910", 17),
          ("e16apsk23", 18),
          ("e16apsk34", 19),
          ("e16apsk45", 20),
          ("e16apsk56", 21),
          ("e16apsk89", 22),
          ("e16apsk910", 23),
          ("e32apsk34", 24),
          ("e32apsk45", 25),
          ("e32apsk56", 26),
          ("e32apsk89", 27),
          ("e32apsk910", 28),
          ("qpsk45180", 129),
          ("qpsk60180", 130),
          ("qpsk72180", 131),
          ("qpsk80180", 132),
          ("qpsk90180", 133),
          ("qpsk100180", 134),
          ("qpsk108180", 135),
          ("qpsk114180", 136),
          ("qpsk120180", 137),
          ("qpsk126180", 138),
          ("qpsk135180", 139),
          ("qpsk144180", 140),
          ("qpsk150180", 141),
          ("qpsk160180", 142),
          ("qpsk162180", 143),
          ("e8psk80180", 144),
          ("e8psk90180", 145),
          ("e8psk100180", 146),
          ("e8psk108180", 147),
          ("e8psk114180", 148),
          ("e8psk120180", 149),
          ("e8psk126180", 150),
          ("e8psk135180", 151),
          ("e8psk144180", 152),
          ("e8psk150180", 153),
          ("e16apsk80180", 154),
          ("e16apsk90180", 155),
          ("e16apsk100180", 156),
          ("e16apsk108180", 157),
          ("e16apsk114180", 158),
          ("e16apsk120180", 159),
          ("e16apsk126180", 160),
          ("e16apsk135180", 161),
          ("e16apsk144180", 162),
          ("e16apsk150180", 163),
          ("e16apsk160180", 164),
          ("e16apsk162180", 165),
          ("e32apsk100180", 166),
          ("e32apsk108180", 167),
          ("e32apsk114180", 168),
          ("e32apsk120180", 169),
          ("e32apsk126180", 170),
          ("e32apsk135180", 171),
          ("e32apsk144180", 172),
          ("e32apsk150180", 173),
          ("e32apsk160180", 174),
          ("e32apsk162180", 175),
          ("e64apsk90180", 176),
          ("e64apsk100180", 177),
          ("e64apsk108180", 178),
          ("e64apsk114180", 179),
          ("e64apsk120180", 180),
          ("e64apsk126180", 181),
          ("e64apsk135180", 182),
          ("e64apsk144180", 183),
          ("e64apsk150180", 184),
          ("e64apsk160180", 185),
          ("e64apsk162180", 186),
          ("e8pskl80180", 187),
          ("e8pskl90180", 188),
          ("e8pskl100180", 189),
          ("e8pskl108180", 190),
          ("e8pskl114180", 191),
          ("e8pskl120180", 192),
          ("e16apskl80180", 193),
          ("e16apskl90180", 194),
          ("e16apskl100180", 195),
          ("e16apskl108180", 196),
          ("e16apskl114180", 197),
          ("e16apskl120180", 198),
          ("e16apskl126180", 199),
          ("e16apskl135180", 200),
          ("e16apskl144180", 201),
          ("e16apskl150180", 202),
          ("e16apskl160180", 203),
          ("e16apskl162180", 204),
          ("e64apskl90180", 205),
          ("e64apskl100180", 206),
          ("e64apskl108180", 207),
          ("e64apskl114180", 208),
          ("e64apskl120180", 209),
          ("e64apskl126180", 210),
          ("e64apskl135180", 211),
          ("e64apskl144180", 212),
          ("e64apskl150180", 213),
          ("e64apskl160180", 214),
          ("e64apskl162180", 215),
          ("qpsk1345", 256),
          ("qpsk920", 257),
          ("qpsk1120", 258),
          ("e8apsk59l", 259),
          ("e8apsk2645l", 260),
          ("e8psk2336", 261),
          ("e8psk2536", 262),
          ("e8psk1318", 263),
          ("e16apsk12l", 264),
          ("e16apsk815l", 265),
          ("e16apsk59l", 266),
          ("e16apsk2645", 267),
          ("e16apsk35", 268),
          ("e16apsk35l", 269),
          ("e16apsk2845", 270),
          ("e16apsk2336", 271),
          ("e16apsk23l", 272),
          ("e16apsk2536", 273),
          ("e16apsk1318", 274),
          ("e16apsk79", 275),
          ("e16apsk7790", 276),
          ("e32apsk23l", 277),
          ("e32apsk3245", 278),
          ("e32apsk1115", 279),
          ("e32apsk79", 280),
          ("e64apsk3245l", 281),
          ("e64apsk1115", 282),
          ("e64apsk79", 283),
          ("e64apsk45", 284),
          ("e64apsk56", 285),
          ("e128apsk34", 286),
          ("e128apsk79", 287),
          ("e256apsk2945l", 288),
          ("e256apsk23l", 289),
          ("e256apsk3145l", 290),
          ("e256apsk3245", 291),
          ("e256apsk1115l", 292),
          ("e256apsk34", 293),
          ("qpsk1145", 294),
          ("qpsk415", 295),
          ("qpsk1445", 296),
          ("qpsk715", 297),
          ("qpsk815", 298),
          ("qpsk3245", 299),
          ("e8psk715", 300),
          ("e8psk815", 301),
          ("e8psk2645", 302),
          ("e8psk3245", 303),
          ("e16apsk715", 304),
          ("e16apsk815", 305),
          ("e16apsk3245", 306),
          ("e32apsk23", 307))
    )


_NtcMultiDemodStatsModCod_Type.__name__ = "Integer32"
_NtcMultiDemodStatsModCod_Object = MibTableColumn
ntcMultiDemodStatsModCod = _NtcMultiDemodStatsModCod_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 3),
    _NtcMultiDemodStatsModCod_Type()
)
ntcMultiDemodStatsModCod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsModCod.setStatus("current")


class _NtcMultiDemodStatsFrameType_Type(Integer32):
    """Custom type ntcMultiDemodStatsFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("short", 0),
          ("normal", 1))
    )


_NtcMultiDemodStatsFrameType_Type.__name__ = "Integer32"
_NtcMultiDemodStatsFrameType_Object = MibTableColumn
ntcMultiDemodStatsFrameType = _NtcMultiDemodStatsFrameType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 4),
    _NtcMultiDemodStatsFrameType_Type()
)
ntcMultiDemodStatsFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsFrameType.setStatus("current")


class _NtcMultiDemodStatsPilots_Type(Integer32):
    """Custom type ntcMultiDemodStatsPilots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcMultiDemodStatsPilots_Type.__name__ = "Integer32"
_NtcMultiDemodStatsPilots_Object = MibTableColumn
ntcMultiDemodStatsPilots = _NtcMultiDemodStatsPilots_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 5),
    _NtcMultiDemodStatsPilots_Type()
)
ntcMultiDemodStatsPilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsPilots.setStatus("current")
_NtcMultiDemodStatsFrameCtr_Type = Counter32
_NtcMultiDemodStatsFrameCtr_Object = MibTableColumn
ntcMultiDemodStatsFrameCtr = _NtcMultiDemodStatsFrameCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 6),
    _NtcMultiDemodStatsFrameCtr_Type()
)
ntcMultiDemodStatsFrameCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsFrameCtr.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsFrameCtr.setUnits("frames")
_NtcMultiDemodStatsErrFrameCtr_Type = Counter32
_NtcMultiDemodStatsErrFrameCtr_Object = MibTableColumn
ntcMultiDemodStatsErrFrameCtr = _NtcMultiDemodStatsErrFrameCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 7),
    _NtcMultiDemodStatsErrFrameCtr_Type()
)
ntcMultiDemodStatsErrFrameCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsErrFrameCtr.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsErrFrameCtr.setUnits("frames")
_NtcMultiDemodStatsCycleSlipCtr_Type = Counter32
_NtcMultiDemodStatsCycleSlipCtr_Object = MibTableColumn
ntcMultiDemodStatsCycleSlipCtr = _NtcMultiDemodStatsCycleSlipCtr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 8),
    _NtcMultiDemodStatsCycleSlipCtr_Type()
)
ntcMultiDemodStatsCycleSlipCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCycleSlipCtr.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCycleSlipCtr.setUnits("frames")


class _NtcMultiDemodStatsPacketErrRatio_Type(Integer32):
    """Custom type ntcMultiDemodStatsPacketErrRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_NtcMultiDemodStatsPacketErrRatio_Type.__name__ = "Integer32"
_NtcMultiDemodStatsPacketErrRatio_Object = MibTableColumn
ntcMultiDemodStatsPacketErrRatio = _NtcMultiDemodStatsPacketErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 9),
    _NtcMultiDemodStatsPacketErrRatio_Type()
)
ntcMultiDemodStatsPacketErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsPacketErrRatio.setStatus("current")


class _NtcMultiDemodStatsLinkMargin_Type(DisplayString):
    """Custom type ntcMultiDemodStatsLinkMargin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcMultiDemodStatsLinkMargin_Type.__name__ = "DisplayString"
_NtcMultiDemodStatsLinkMargin_Object = MibTableColumn
ntcMultiDemodStatsLinkMargin = _NtcMultiDemodStatsLinkMargin_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 10),
    _NtcMultiDemodStatsLinkMargin_Type()
)
ntcMultiDemodStatsLinkMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsLinkMargin.setStatus("current")


class _NtcMultiDemodStatsCoN_Type(DisplayString):
    """Custom type ntcMultiDemodStatsCoN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcMultiDemodStatsCoN_Type.__name__ = "DisplayString"
_NtcMultiDemodStatsCoN_Object = MibTableColumn
ntcMultiDemodStatsCoN = _NtcMultiDemodStatsCoN_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 11),
    _NtcMultiDemodStatsCoN_Type()
)
ntcMultiDemodStatsCoN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCoN.setStatus("current")


class _NtcMultiDemodStatsCoD_Type(DisplayString):
    """Custom type ntcMultiDemodStatsCoD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcMultiDemodStatsCoD_Type.__name__ = "DisplayString"
_NtcMultiDemodStatsCoD_Object = MibTableColumn
ntcMultiDemodStatsCoD = _NtcMultiDemodStatsCoD_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 12),
    _NtcMultiDemodStatsCoD_Type()
)
ntcMultiDemodStatsCoD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCoD.setStatus("current")


class _NtcMultiDemodStatsCoDpilots_Type(DisplayString):
    """Custom type ntcMultiDemodStatsCoDpilots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcMultiDemodStatsCoDpilots_Type.__name__ = "DisplayString"
_NtcMultiDemodStatsCoDpilots_Object = MibTableColumn
ntcMultiDemodStatsCoDpilots = _NtcMultiDemodStatsCoDpilots_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 13),
    _NtcMultiDemodStatsCoDpilots_Type()
)
ntcMultiDemodStatsCoDpilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCoDpilots.setStatus("deprecated")


class _NtcMultiDemodStatsCoND_Type(DisplayString):
    """Custom type ntcMultiDemodStatsCoND based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcMultiDemodStatsCoND_Type.__name__ = "DisplayString"
_NtcMultiDemodStatsCoND_Object = MibTableColumn
ntcMultiDemodStatsCoND = _NtcMultiDemodStatsCoND_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 14),
    _NtcMultiDemodStatsCoND_Type()
)
ntcMultiDemodStatsCoND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCoND.setStatus("current")


class _NtcMultiDemodStatsCoNDpilots_Type(DisplayString):
    """Custom type ntcMultiDemodStatsCoNDpilots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcMultiDemodStatsCoNDpilots_Type.__name__ = "DisplayString"
_NtcMultiDemodStatsCoNDpilots_Object = MibTableColumn
ntcMultiDemodStatsCoNDpilots = _NtcMultiDemodStatsCoNDpilots_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 6, 1, 15),
    _NtcMultiDemodStatsCoNDpilots_Type()
)
ntcMultiDemodStatsCoNDpilots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodStatsCoNDpilots.setStatus("deprecated")
_NtcMultiDemodCmCfg_ObjectIdentity = ObjectIdentity
ntcMultiDemodCmCfg = _NtcMultiDemodCmCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 7)
)
if mibBuilder.loadTexts:
    ntcMultiDemodCmCfg.setStatus("current")


class _NtcMultiDemodCmCfgInputSelection_Type(Integer32):
    """Custom type ntcMultiDemodCmCfgInputSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lbandRxA", 0),
          ("lbandRxB", 1),
          ("ifRx", 3))
    )


_NtcMultiDemodCmCfgInputSelection_Type.__name__ = "Integer32"
_NtcMultiDemodCmCfgInputSelection_Object = MibScalar
ntcMultiDemodCmCfgInputSelection = _NtcMultiDemodCmCfgInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 7, 1),
    _NtcMultiDemodCmCfgInputSelection_Type()
)
ntcMultiDemodCmCfgInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCmCfgInputSelection.setStatus("current")


class _NtcMultiDemodCmCfgLnbPowerSupply_Type(Integer32):
    """Custom type ntcMultiDemodCmCfgLnbPowerSupply based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("e13V0kHz", 1),
          ("e13V22kHz", 2),
          ("e18V0kHz", 3),
          ("e18V22kHz", 4))
    )


_NtcMultiDemodCmCfgLnbPowerSupply_Type.__name__ = "Integer32"
_NtcMultiDemodCmCfgLnbPowerSupply_Object = MibScalar
ntcMultiDemodCmCfgLnbPowerSupply = _NtcMultiDemodCmCfgLnbPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 7, 2),
    _NtcMultiDemodCmCfgLnbPowerSupply_Type()
)
ntcMultiDemodCmCfgLnbPowerSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCmCfgLnbPowerSupply.setStatus("current")
_NtcMultiDemodCmMon_ObjectIdentity = ObjectIdentity
ntcMultiDemodCmMon = _NtcMultiDemodCmMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 8)
)
if mibBuilder.loadTexts:
    ntcMultiDemodCmMon.setStatus("current")


class _NtcMultiDemodCmMonLbandInputLvl_Type(Integer32):
    """Custom type ntcMultiDemodCmMonLbandInputLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 500),
    )


_NtcMultiDemodCmMonLbandInputLvl_Type.__name__ = "Integer32"
_NtcMultiDemodCmMonLbandInputLvl_Object = MibScalar
ntcMultiDemodCmMonLbandInputLvl = _NtcMultiDemodCmMonLbandInputLvl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 8, 1),
    _NtcMultiDemodCmMonLbandInputLvl_Type()
)
ntcMultiDemodCmMonLbandInputLvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodCmMonLbandInputLvl.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCmMonLbandInputLvl.setUnits("dBm")
_NtcMultiDemodEqCliCfgTable_Object = MibTable
ntcMultiDemodEqCliCfgTable = _NtcMultiDemodEqCliCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 9)
)
if mibBuilder.loadTexts:
    ntcMultiDemodEqCliCfgTable.setStatus("current")
_NtcMultiDemodEqCliCfgEntry_Object = MibTableRow
ntcMultiDemodEqCliCfgEntry = _NtcMultiDemodEqCliCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 9, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodEqCliCfgEntry.setStatus("current")


class _NtcMultiDemodEqCfgEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodEqCfgEnable based on NtcEnable"""
    defaultValue = 0


_NtcMultiDemodEqCfgEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodEqCfgEnable_Object = MibTableColumn
ntcMultiDemodEqCfgEnable = _NtcMultiDemodEqCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 9, 1, 1),
    _NtcMultiDemodEqCfgEnable_Type()
)
ntcMultiDemodEqCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodEqCfgEnable.setStatus("current")
_NtcMultiDemodBuCarCfgTable_Object = MibTable
ntcMultiDemodBuCarCfgTable = _NtcMultiDemodBuCarCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10)
)
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgTable.setStatus("current")
_NtcMultiDemodBuCarCfgEntry_Object = MibTableRow
ntcMultiDemodBuCarCfgEntry = _NtcMultiDemodBuCarCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgEntry.setStatus("current")


class _NtcMultiDemodBuCarCfgEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodBuCarCfgEnable based on NtcEnable"""
    defaultValue = 0


_NtcMultiDemodBuCarCfgEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodBuCarCfgEnable_Object = MibTableColumn
ntcMultiDemodBuCarCfgEnable = _NtcMultiDemodBuCarCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10, 1, 1),
    _NtcMultiDemodBuCarCfgEnable_Type()
)
ntcMultiDemodBuCarCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgEnable.setStatus("current")


class _NtcMultiDemodBuCarCfgInpFreq_Type(Unsigned32):
    """Custom type ntcMultiDemodBuCarCfgInpFreq based on Unsigned32"""
    defaultValue = 2000000000


_NtcMultiDemodBuCarCfgInpFreq_Type.__name__ = "Unsigned32"
_NtcMultiDemodBuCarCfgInpFreq_Object = MibTableColumn
ntcMultiDemodBuCarCfgInpFreq = _NtcMultiDemodBuCarCfgInpFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10, 1, 2),
    _NtcMultiDemodBuCarCfgInpFreq_Type()
)
ntcMultiDemodBuCarCfgInpFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgInpFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgInpFreq.setUnits("Hz")


class _NtcMultiDemodBuCarCfgSymbolRate_Type(Unsigned32):
    """Custom type ntcMultiDemodBuCarCfgSymbolRate based on Unsigned32"""
    defaultValue = 10000000


_NtcMultiDemodBuCarCfgSymbolRate_Type.__name__ = "Unsigned32"
_NtcMultiDemodBuCarCfgSymbolRate_Object = MibTableColumn
ntcMultiDemodBuCarCfgSymbolRate = _NtcMultiDemodBuCarCfgSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10, 1, 3),
    _NtcMultiDemodBuCarCfgSymbolRate_Type()
)
ntcMultiDemodBuCarCfgSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgSymbolRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgSymbolRate.setUnits("baud")


class _NtcMultiDemodBuCarCfgSwitchTmo_Type(Unsigned32):
    """Custom type ntcMultiDemodBuCarCfgSwitchTmo based on Unsigned32"""
    defaultValue = 60


_NtcMultiDemodBuCarCfgSwitchTmo_Type.__name__ = "Unsigned32"
_NtcMultiDemodBuCarCfgSwitchTmo_Object = MibTableColumn
ntcMultiDemodBuCarCfgSwitchTmo = _NtcMultiDemodBuCarCfgSwitchTmo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10, 1, 4),
    _NtcMultiDemodBuCarCfgSwitchTmo_Type()
)
ntcMultiDemodBuCarCfgSwitchTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgSwitchTmo.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgSwitchTmo.setUnits("s")


class _NtcMultiDemodBuCarCfgRfFreq_Type(DisplayString):
    """Custom type ntcMultiDemodBuCarCfgRfFreq based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcMultiDemodBuCarCfgRfFreq_Type.__name__ = "DisplayString"
_NtcMultiDemodBuCarCfgRfFreq_Object = MibTableColumn
ntcMultiDemodBuCarCfgRfFreq = _NtcMultiDemodBuCarCfgRfFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 10, 1, 5),
    _NtcMultiDemodBuCarCfgRfFreq_Type()
)
ntcMultiDemodBuCarCfgRfFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgRfFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarCfgRfFreq.setUnits("Hz")
_NtcMultiDemodBuCarMonTable_Object = MibTable
ntcMultiDemodBuCarMonTable = _NtcMultiDemodBuCarMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 11)
)
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarMonTable.setStatus("current")
_NtcMultiDemodBuCarMonEntry_Object = MibTableRow
ntcMultiDemodBuCarMonEntry = _NtcMultiDemodBuCarMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 11, 1)
)
ntcMultiDemodBuCarMonEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarMonDemodId"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarMonEntry.setStatus("current")


class _NtcMultiDemodBuCarMonDemodId_Type(Integer32):
    """Custom type ntcMultiDemodBuCarMonDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodBuCarMonDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodBuCarMonDemodId_Object = MibTableColumn
ntcMultiDemodBuCarMonDemodId = _NtcMultiDemodBuCarMonDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 11, 1, 1),
    _NtcMultiDemodBuCarMonDemodId_Type()
)
ntcMultiDemodBuCarMonDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarMonDemodId.setStatus("current")


class _NtcMultiDemodBuCarMonActiveCar_Type(Integer32):
    """Custom type ntcMultiDemodBuCarMonActiveCar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("main", 0),
          ("backup", 1))
    )


_NtcMultiDemodBuCarMonActiveCar_Type.__name__ = "Integer32"
_NtcMultiDemodBuCarMonActiveCar_Object = MibTableColumn
ntcMultiDemodBuCarMonActiveCar = _NtcMultiDemodBuCarMonActiveCar_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 11, 1, 2),
    _NtcMultiDemodBuCarMonActiveCar_Type()
)
ntcMultiDemodBuCarMonActiveCar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarMonActiveCar.setStatus("current")
_NtcMultiDemodBuCarMonSwitchCnt_Type = Counter32
_NtcMultiDemodBuCarMonSwitchCnt_Object = MibTableColumn
ntcMultiDemodBuCarMonSwitchCnt = _NtcMultiDemodBuCarMonSwitchCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 11, 1, 3),
    _NtcMultiDemodBuCarMonSwitchCnt_Type()
)
ntcMultiDemodBuCarMonSwitchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodBuCarMonSwitchCnt.setStatus("current")
_NtcMultiDemodNlpdCliCfgTable_Object = MibTable
ntcMultiDemodNlpdCliCfgTable = _NtcMultiDemodNlpdCliCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 12)
)
if mibBuilder.loadTexts:
    ntcMultiDemodNlpdCliCfgTable.setStatus("current")
_NtcMultiDemodNlpdCliCfgEntry_Object = MibTableRow
ntcMultiDemodNlpdCliCfgEntry = _NtcMultiDemodNlpdCliCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 12, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodNlpdCliCfgEntry.setStatus("current")


class _NtcMultiDemodNldCfgEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodNldCfgEnable based on NtcEnable"""
    defaultValue = 0


_NtcMultiDemodNldCfgEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodNldCfgEnable_Object = MibTableColumn
ntcMultiDemodNldCfgEnable = _NtcMultiDemodNldCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 12, 1, 1),
    _NtcMultiDemodNldCfgEnable_Type()
)
ntcMultiDemodNldCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodNldCfgEnable.setStatus("current")


class _NtcMultiDemodNldCfgTrCenFreq_Type(DisplayString):
    """Custom type ntcMultiDemodNldCfgTrCenFreq based on DisplayString"""
    defaultValue = OctetString("15000000000")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcMultiDemodNldCfgTrCenFreq_Type.__name__ = "DisplayString"
_NtcMultiDemodNldCfgTrCenFreq_Object = MibTableColumn
ntcMultiDemodNldCfgTrCenFreq = _NtcMultiDemodNldCfgTrCenFreq_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 12, 1, 2),
    _NtcMultiDemodNldCfgTrCenFreq_Type()
)
ntcMultiDemodNldCfgTrCenFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodNldCfgTrCenFreq.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodNldCfgTrCenFreq.setUnits("Hz")


class _NtcMultiDemodNldCfgTrBandw_Type(Unsigned32):
    """Custom type ntcMultiDemodNldCfgTrBandw based on Unsigned32"""
    defaultValue = 36000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000000, 80000000),
    )


_NtcMultiDemodNldCfgTrBandw_Type.__name__ = "Unsigned32"
_NtcMultiDemodNldCfgTrBandw_Object = MibTableColumn
ntcMultiDemodNldCfgTrBandw = _NtcMultiDemodNldCfgTrBandw_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 12, 1, 3),
    _NtcMultiDemodNldCfgTrBandw_Type()
)
ntcMultiDemodNldCfgTrBandw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodNldCfgTrBandw.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodNldCfgTrBandw.setUnits("Hz")


class _NtcMultiDemodNldCfgEnaSingle_Type(NtcEnable):
    """Custom type ntcMultiDemodNldCfgEnaSingle based on NtcEnable"""
    defaultValue = 1


_NtcMultiDemodNldCfgEnaSingle_Type.__name__ = "NtcEnable"
_NtcMultiDemodNldCfgEnaSingle_Object = MibTableColumn
ntcMultiDemodNldCfgEnaSingle = _NtcMultiDemodNldCfgEnaSingle_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 12, 1, 4),
    _NtcMultiDemodNldCfgEnaSingle_Type()
)
ntcMultiDemodNldCfgEnaSingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodNldCfgEnaSingle.setStatus("current")
_NtcMultiDemodExtConvTable_Object = MibTable
ntcMultiDemodExtConvTable = _NtcMultiDemodExtConvTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 13)
)
if mibBuilder.loadTexts:
    ntcMultiDemodExtConvTable.setStatus("current")
_NtcMultiDemodExtConvEntry_Object = MibTableRow
ntcMultiDemodExtConvEntry = _NtcMultiDemodExtConvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 13, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodExtConvEntry.setStatus("current")


class _NtcMultiDemodExtConvEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodExtConvEnable based on NtcEnable"""
    defaultValue = 0


_NtcMultiDemodExtConvEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodExtConvEnable_Object = MibTableColumn
ntcMultiDemodExtConvEnable = _NtcMultiDemodExtConvEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 13, 1, 1),
    _NtcMultiDemodExtConvEnable_Type()
)
ntcMultiDemodExtConvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodExtConvEnable.setStatus("current")


class _NtcMultiDemodExtConvLoFrequency_Type(DisplayString):
    """Custom type ntcMultiDemodExtConvLoFrequency based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcMultiDemodExtConvLoFrequency_Type.__name__ = "DisplayString"
_NtcMultiDemodExtConvLoFrequency_Object = MibTableColumn
ntcMultiDemodExtConvLoFrequency = _NtcMultiDemodExtConvLoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 13, 1, 2),
    _NtcMultiDemodExtConvLoFrequency_Type()
)
ntcMultiDemodExtConvLoFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodExtConvLoFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodExtConvLoFrequency.setUnits("Hz")


class _NtcMultiDemodExtConvSpectralInv_Type(Integer32):
    """Custom type ntcMultiDemodExtConvSpectralInv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("inverted", 2))
    )


_NtcMultiDemodExtConvSpectralInv_Type.__name__ = "Integer32"
_NtcMultiDemodExtConvSpectralInv_Object = MibTableColumn
ntcMultiDemodExtConvSpectralInv = _NtcMultiDemodExtConvSpectralInv_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 13, 1, 3),
    _NtcMultiDemodExtConvSpectralInv_Type()
)
ntcMultiDemodExtConvSpectralInv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodExtConvSpectralInv.setStatus("current")
_NtcMultiDemodCmConv_ObjectIdentity = ObjectIdentity
ntcMultiDemodCmConv = _NtcMultiDemodCmConv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 14)
)
if mibBuilder.loadTexts:
    ntcMultiDemodCmConv.setStatus("current")


class _NtcMultiDemodCmConvEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodCmConvEnable based on NtcEnable"""
    defaultValue = 0


_NtcMultiDemodCmConvEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodCmConvEnable_Object = MibScalar
ntcMultiDemodCmConvEnable = _NtcMultiDemodCmConvEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 14, 1),
    _NtcMultiDemodCmConvEnable_Type()
)
ntcMultiDemodCmConvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCmConvEnable.setStatus("current")


class _NtcMultiDemodCmConvLoFrequency_Type(DisplayString):
    """Custom type ntcMultiDemodCmConvLoFrequency based on DisplayString"""
    defaultValue = OctetString("0")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcMultiDemodCmConvLoFrequency_Type.__name__ = "DisplayString"
_NtcMultiDemodCmConvLoFrequency_Object = MibScalar
ntcMultiDemodCmConvLoFrequency = _NtcMultiDemodCmConvLoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 14, 2),
    _NtcMultiDemodCmConvLoFrequency_Type()
)
ntcMultiDemodCmConvLoFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCmConvLoFrequency.setStatus("current")
if mibBuilder.loadTexts:
    ntcMultiDemodCmConvLoFrequency.setUnits("Hz")


class _NtcMultiDemodCmConvSpectralInv_Type(Integer32):
    """Custom type ntcMultiDemodCmConvSpectralInv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("inverted", 2))
    )


_NtcMultiDemodCmConvSpectralInv_Type.__name__ = "Integer32"
_NtcMultiDemodCmConvSpectralInv_Object = MibScalar
ntcMultiDemodCmConvSpectralInv = _NtcMultiDemodCmConvSpectralInv_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 14, 3),
    _NtcMultiDemodCmConvSpectralInv_Type()
)
ntcMultiDemodCmConvSpectralInv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodCmConvSpectralInv.setStatus("current")
_NtcMultiDemodAesConfTable_Object = MibTable
ntcMultiDemodAesConfTable = _NtcMultiDemodAesConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfTable.setStatus("current")
_NtcMultiDemodAesConfEntry_Object = MibTableRow
ntcMultiDemodAesConfEntry = _NtcMultiDemodAesConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfEntry.setStatus("current")


class _NtcMultiDemodAesConfEnable_Type(NtcEnable):
    """Custom type ntcMultiDemodAesConfEnable based on NtcEnable"""
    defaultValue = 0


_NtcMultiDemodAesConfEnable_Type.__name__ = "NtcEnable"
_NtcMultiDemodAesConfEnable_Object = MibTableColumn
ntcMultiDemodAesConfEnable = _NtcMultiDemodAesConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15, 1, 1),
    _NtcMultiDemodAesConfEnable_Type()
)
ntcMultiDemodAesConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfEnable.setStatus("current")


class _NtcMultiDemodAesConfGlbEncrypt_Type(NtcEnable):
    """Custom type ntcMultiDemodAesConfGlbEncrypt based on NtcEnable"""
    defaultValue = 1


_NtcMultiDemodAesConfGlbEncrypt_Type.__name__ = "NtcEnable"
_NtcMultiDemodAesConfGlbEncrypt_Object = MibTableColumn
ntcMultiDemodAesConfGlbEncrypt = _NtcMultiDemodAesConfGlbEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15, 1, 2),
    _NtcMultiDemodAesConfGlbEncrypt_Type()
)
ntcMultiDemodAesConfGlbEncrypt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfGlbEncrypt.setStatus("current")


class _NtcMultiDemodAesConfKeyStren_Type(Integer32):
    """Custom type ntcMultiDemodAesConfKeyStren based on Integer32"""
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
        *(("aes64", 0),
          ("aes128", 1),
          ("aes256", 2))
    )


_NtcMultiDemodAesConfKeyStren_Type.__name__ = "Integer32"
_NtcMultiDemodAesConfKeyStren_Object = MibTableColumn
ntcMultiDemodAesConfKeyStren = _NtcMultiDemodAesConfKeyStren_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15, 1, 3),
    _NtcMultiDemodAesConfKeyStren_Type()
)
ntcMultiDemodAesConfKeyStren.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfKeyStren.setStatus("current")


class _NtcMultiDemodAesConfGrpKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesConfGrpKey based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesConfGrpKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesConfGrpKey_Object = MibTableColumn
ntcMultiDemodAesConfGrpKey = _NtcMultiDemodAesConfGrpKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15, 1, 4),
    _NtcMultiDemodAesConfGrpKey_Type()
)
ntcMultiDemodAesConfGrpKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfGrpKey.setStatus("current")


class _NtcMultiDemodAesConfClrKeys_Type(Integer32):
    """Custom type ntcMultiDemodAesConfClrKeys based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("donothing", 0),
          ("clearkeys", 1))
    )


_NtcMultiDemodAesConfClrKeys_Type.__name__ = "Integer32"
_NtcMultiDemodAesConfClrKeys_Object = MibTableColumn
ntcMultiDemodAesConfClrKeys = _NtcMultiDemodAesConfClrKeys_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 15, 1, 5),
    _NtcMultiDemodAesConfClrKeys_Type()
)
ntcMultiDemodAesConfClrKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesConfClrKeys.setStatus("current")
_NtcMultiDemodAesGConfTable_Object = MibTable
ntcMultiDemodAesGConfTable = _NtcMultiDemodAesGConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 16)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesGConfTable.setStatus("current")
_NtcMultiDemodAesGConfEntry_Object = MibTableRow
ntcMultiDemodAesGConfEntry = _NtcMultiDemodAesGConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 16, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesGConfEntry.setStatus("current")


class _NtcMultiDemodAesGConfEncEKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesGConfEncEKey based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesGConfEncEKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesGConfEncEKey_Object = MibTableColumn
ntcMultiDemodAesGConfEncEKey = _NtcMultiDemodAesGConfEncEKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 16, 1, 1),
    _NtcMultiDemodAesGConfEncEKey_Type()
)
ntcMultiDemodAesGConfEncEKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesGConfEncEKey.setStatus("current")


class _NtcMultiDemodAesGConfEncOKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesGConfEncOKey based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesGConfEncOKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesGConfEncOKey_Object = MibTableColumn
ntcMultiDemodAesGConfEncOKey = _NtcMultiDemodAesGConfEncOKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 16, 1, 2),
    _NtcMultiDemodAesGConfEncOKey_Type()
)
ntcMultiDemodAesGConfEncOKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesGConfEncOKey.setStatus("current")


class _NtcMultiDemodAesGConfEKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesGConfEKey based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesGConfEKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesGConfEKey_Object = MibTableColumn
ntcMultiDemodAesGConfEKey = _NtcMultiDemodAesGConfEKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 16, 1, 3),
    _NtcMultiDemodAesGConfEKey_Type()
)
ntcMultiDemodAesGConfEKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesGConfEKey.setStatus("current")


class _NtcMultiDemodAesGConfOKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesGConfOKey based on DisplayString"""
    defaultValue = OctetString("**********")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesGConfOKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesGConfOKey_Object = MibTableColumn
ntcMultiDemodAesGConfOKey = _NtcMultiDemodAesGConfOKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 16, 1, 4),
    _NtcMultiDemodAesGConfOKey_Type()
)
ntcMultiDemodAesGConfOKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcMultiDemodAesGConfOKey.setStatus("current")
_NtcMultiDemodAesSConfTable_Object = MibTable
ntcMultiDemodAesSConfTable = _NtcMultiDemodAesSConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfTable.setStatus("current")
_NtcMultiDemodAesSConfEntry_Object = MibTableRow
ntcMultiDemodAesSConfEntry = _NtcMultiDemodAesSConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1)
)
ntcMultiDemodAesSConfEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfName"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfEntry.setStatus("current")


class _NtcMultiDemodAesSConfName_Type(DisplayString):
    """Custom type ntcMultiDemodAesSConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcMultiDemodAesSConfName_Type.__name__ = "DisplayString"
_NtcMultiDemodAesSConfName_Object = MibTableColumn
ntcMultiDemodAesSConfName = _NtcMultiDemodAesSConfName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 1),
    _NtcMultiDemodAesSConfName_Type()
)
ntcMultiDemodAesSConfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfName.setStatus("current")
_NtcMultiDemodAesSConfRowStatus_Type = RowStatus
_NtcMultiDemodAesSConfRowStatus_Object = MibTableColumn
ntcMultiDemodAesSConfRowStatus = _NtcMultiDemodAesSConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 2),
    _NtcMultiDemodAesSConfRowStatus_Type()
)
ntcMultiDemodAesSConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfRowStatus.setStatus("current")
_NtcMultiDemodAesSConfEnable_Type = NtcEnable
_NtcMultiDemodAesSConfEnable_Object = MibTableColumn
ntcMultiDemodAesSConfEnable = _NtcMultiDemodAesSConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 3),
    _NtcMultiDemodAesSConfEnable_Type()
)
ntcMultiDemodAesSConfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfEnable.setStatus("current")
_NtcMultiDemodAesSConfIsi_Type = Unsigned32
_NtcMultiDemodAesSConfIsi_Object = MibTableColumn
ntcMultiDemodAesSConfIsi = _NtcMultiDemodAesSConfIsi_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 4),
    _NtcMultiDemodAesSConfIsi_Type()
)
ntcMultiDemodAesSConfIsi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfIsi.setStatus("current")


class _NtcMultiDemodAesSConfEncEKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesSConfEncEKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesSConfEncEKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesSConfEncEKey_Object = MibTableColumn
ntcMultiDemodAesSConfEncEKey = _NtcMultiDemodAesSConfEncEKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 5),
    _NtcMultiDemodAesSConfEncEKey_Type()
)
ntcMultiDemodAesSConfEncEKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfEncEKey.setStatus("current")


class _NtcMultiDemodAesSConfEncOKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesSConfEncOKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesSConfEncOKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesSConfEncOKey_Object = MibTableColumn
ntcMultiDemodAesSConfEncOKey = _NtcMultiDemodAesSConfEncOKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 6),
    _NtcMultiDemodAesSConfEncOKey_Type()
)
ntcMultiDemodAesSConfEncOKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfEncOKey.setStatus("current")


class _NtcMultiDemodAesSConfEKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesSConfEKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesSConfEKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesSConfEKey_Object = MibTableColumn
ntcMultiDemodAesSConfEKey = _NtcMultiDemodAesSConfEKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 7),
    _NtcMultiDemodAesSConfEKey_Type()
)
ntcMultiDemodAesSConfEKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfEKey.setStatus("current")


class _NtcMultiDemodAesSConfOKey_Type(DisplayString):
    """Custom type ntcMultiDemodAesSConfOKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 64),
    )


_NtcMultiDemodAesSConfOKey_Type.__name__ = "DisplayString"
_NtcMultiDemodAesSConfOKey_Object = MibTableColumn
ntcMultiDemodAesSConfOKey = _NtcMultiDemodAesSConfOKey_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 8),
    _NtcMultiDemodAesSConfOKey_Type()
)
ntcMultiDemodAesSConfOKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfOKey.setStatus("current")


class _NtcMultiDemodAesSConfDemodId_Type(Integer32):
    """Custom type ntcMultiDemodAesSConfDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodAesSConfDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodAesSConfDemodId_Object = MibTableColumn
ntcMultiDemodAesSConfDemodId = _NtcMultiDemodAesSConfDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 17, 1, 9),
    _NtcMultiDemodAesSConfDemodId_Type()
)
ntcMultiDemodAesSConfDemodId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSConfDemodId.setStatus("current")
_NtcMultiDemodAesGMonTable_Object = MibTable
ntcMultiDemodAesGMonTable = _NtcMultiDemodAesGMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 18)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesGMonTable.setStatus("current")
_NtcMultiDemodAesGMonEntry_Object = MibTableRow
ntcMultiDemodAesGMonEntry = _NtcMultiDemodAesGMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 18, 1)
)
ntcMultiDemodAesGMonEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesGMonDemodId"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesGMonEntry.setStatus("current")


class _NtcMultiDemodAesGMonDemodId_Type(Integer32):
    """Custom type ntcMultiDemodAesGMonDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodAesGMonDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodAesGMonDemodId_Object = MibTableColumn
ntcMultiDemodAesGMonDemodId = _NtcMultiDemodAesGMonDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 18, 1, 1),
    _NtcMultiDemodAesGMonDemodId_Type()
)
ntcMultiDemodAesGMonDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodAesGMonDemodId.setStatus("current")


class _NtcMultiDemodAesGMonKeyParity_Type(Integer32):
    """Custom type ntcMultiDemodAesGMonKeyParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("even", 0),
          ("odd", 1))
    )


_NtcMultiDemodAesGMonKeyParity_Type.__name__ = "Integer32"
_NtcMultiDemodAesGMonKeyParity_Object = MibTableColumn
ntcMultiDemodAesGMonKeyParity = _NtcMultiDemodAesGMonKeyParity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 18, 1, 2),
    _NtcMultiDemodAesGMonKeyParity_Type()
)
ntcMultiDemodAesGMonKeyParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAesGMonKeyParity.setStatus("current")
_NtcMultiDemodAesSMonTable_Object = MibTable
ntcMultiDemodAesSMonTable = _NtcMultiDemodAesSMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 19)
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesSMonTable.setStatus("current")
_NtcMultiDemodAesSMonEntry_Object = MibTableRow
ntcMultiDemodAesSMonEntry = _NtcMultiDemodAesSMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 19, 1)
)
ntcMultiDemodAesSMonEntry.setIndexNames(
    (0, "NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSMonName"),
)
if mibBuilder.loadTexts:
    ntcMultiDemodAesSMonEntry.setStatus("current")


class _NtcMultiDemodAesSMonName_Type(DisplayString):
    """Custom type ntcMultiDemodAesSMonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcMultiDemodAesSMonName_Type.__name__ = "DisplayString"
_NtcMultiDemodAesSMonName_Object = MibTableColumn
ntcMultiDemodAesSMonName = _NtcMultiDemodAesSMonName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 19, 1, 1),
    _NtcMultiDemodAesSMonName_Type()
)
ntcMultiDemodAesSMonName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSMonName.setStatus("current")


class _NtcMultiDemodAesSMonDemodId_Type(Integer32):
    """Custom type ntcMultiDemodAesSMonDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcMultiDemodAesSMonDemodId_Type.__name__ = "Integer32"
_NtcMultiDemodAesSMonDemodId_Object = MibTableColumn
ntcMultiDemodAesSMonDemodId = _NtcMultiDemodAesSMonDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 19, 1, 2),
    _NtcMultiDemodAesSMonDemodId_Type()
)
ntcMultiDemodAesSMonDemodId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSMonDemodId.setStatus("current")


class _NtcMultiDemodAesSMonKeyParity_Type(Integer32):
    """Custom type ntcMultiDemodAesSMonKeyParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("even", 0),
          ("odd", 1))
    )


_NtcMultiDemodAesSMonKeyParity_Type.__name__ = "Integer32"
_NtcMultiDemodAesSMonKeyParity_Object = MibTableColumn
ntcMultiDemodAesSMonKeyParity = _NtcMultiDemodAesSMonKeyParity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 1, 19, 1, 3),
    _NtcMultiDemodAesSMonKeyParity_Type()
)
ntcMultiDemodAesSMonKeyParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcMultiDemodAesSMonKeyParity.setStatus("current")
_NtcMultiDemodConformance_ObjectIdentity = ObjectIdentity
ntcMultiDemodConformance = _NtcMultiDemodConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 2)
)
if mibBuilder.loadTexts:
    ntcMultiDemodConformance.setStatus("current")
_NtcMultiDemodConfCompliance_ObjectIdentity = ObjectIdentity
ntcMultiDemodConfCompliance = _NtcMultiDemodConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 2, 1)
)
if mibBuilder.loadTexts:
    ntcMultiDemodConfCompliance.setStatus("current")
_NtcMultiDemodConfGroup_ObjectIdentity = ObjectIdentity
ntcMultiDemodConfGroup = _NtcMultiDemodConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 2, 2)
)
if mibBuilder.loadTexts:
    ntcMultiDemodConfGroup.setStatus("current")
ntcMultiDemodCfgEntry.registerAugmentions(
    ("NEWTEC-MULTI-DEMOD-MIB",
     "ntcMultiDemodEqCliCfgEntry")
)
ntcMultiDemodEqCliCfgEntry.setIndexNames(*ntcMultiDemodCfgEntry.getIndexNames())
ntcMultiDemodCfgEntry.registerAugmentions(
    ("NEWTEC-MULTI-DEMOD-MIB",
     "ntcMultiDemodBuCarCfgEntry")
)
ntcMultiDemodBuCarCfgEntry.setIndexNames(*ntcMultiDemodCfgEntry.getIndexNames())
ntcMultiDemodCfgEntry.registerAugmentions(
    ("NEWTEC-MULTI-DEMOD-MIB",
     "ntcMultiDemodNlpdCliCfgEntry")
)
ntcMultiDemodNlpdCliCfgEntry.setIndexNames(*ntcMultiDemodCfgEntry.getIndexNames())
ntcMultiDemodCfgEntry.registerAugmentions(
    ("NEWTEC-MULTI-DEMOD-MIB",
     "ntcMultiDemodExtConvEntry")
)
ntcMultiDemodExtConvEntry.setIndexNames(*ntcMultiDemodCfgEntry.getIndexNames())
ntcMultiDemodCfgEntry.registerAugmentions(
    ("NEWTEC-MULTI-DEMOD-MIB",
     "ntcMultiDemodAesConfEntry")
)
ntcMultiDemodAesConfEntry.setIndexNames(*ntcMultiDemodCfgEntry.getIndexNames())
ntcMultiDemodCfgEntry.registerAugmentions(
    ("NEWTEC-MULTI-DEMOD-MIB",
     "ntcMultiDemodAesGConfEntry")
)
ntcMultiDemodAesGConfEntry.setIndexNames(*ntcMultiDemodCfgEntry.getIndexNames())

# Managed Objects groups

ntcMultiDemodConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 2, 2, 1)
)
ntcMultiDemodConfGrpV1Standard.setObjects(
      *(("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmGeneralDemod"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmInternalError"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmInputSaturated"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmNoLock"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmLnbPowerControl"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmDecoderOvrload"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmNoPlLock"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAlmBufferOverflow"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASGeneralDemod"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASInternalError"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASInputSaturated"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASNoPlLock"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASNoLock"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASLnbPowerControl"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodASDecoderOverloaded"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgMode"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgInputFrequency"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgSymbolRate"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgRollOff"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgInputSelection"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgSpectralInv"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgPlScrambSig"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgLnbPowerSupply"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgHardwareId"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgModCodDvbs"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgStreamMode"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgInterfaceRate"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgAcqRange"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgPlhdrScramSeq"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgRfFrequency"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgModCodAmcDl"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCfgLnbClockRef"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcExtMultiDemodCfgOpMode"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonLbandInputLvl"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonCarrierInputLvl"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonEsNo"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonPhaseNoiseIndic"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonOffRefMask"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonNonLinIndic"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonSymbolRate"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonCarrierOffset"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonFrameCounter"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonDummyFrameCtr"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonErroredFrameCtr"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonCycleSlipCtr"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonLastModCod"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodModCodStatsReset"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonVber"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonBer"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonEbNo"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonLinkMargin"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonOperationalState"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonLastNonDumModCod"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonRollOff"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonQefM"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonSpectralInv"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonVberClp"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonBerClp"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonQefMClp"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonEbNoClp"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodMonNonLinIndicAM"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsDemodId"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsModCod"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsFrameType"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsPilots"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsFrameCtr"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsErrFrameCtr"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsCycleSlipCtr"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsPacketErrRatio"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsLinkMargin"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsCoN"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsCoD"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsCoND"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCmCfgInputSelection"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCmCfgLnbPowerSupply"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCmMonLbandInputLvl"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodEqCfgEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarCfgEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarCfgInpFreq"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarCfgSymbolRate"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarCfgSwitchTmo"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarCfgRfFreq"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarMonActiveCar"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodBuCarMonSwitchCnt"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodNldCfgEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodNldCfgTrCenFreq"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodNldCfgTrBandw"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodNldCfgEnaSingle"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodExtConvEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodExtConvLoFrequency"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodExtConvSpectralInv"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCmConvEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCmConvLoFrequency"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodCmConvSpectralInv"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesConfEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesConfGlbEncrypt"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesConfKeyStren"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesConfGrpKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesConfClrKeys"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesGConfEncEKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesGConfEncOKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesGConfEKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesGConfOKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfRowStatus"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfEnable"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfIsi"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfEncEKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfEncOKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfEKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfOKey"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSConfDemodId"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesGMonKeyParity"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSMonDemodId"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodAesSMonKeyParity"))
)
if mibBuilder.loadTexts:
    ntcMultiDemodConfGrpV1Standard.setStatus("current")

ntcMultiDemodConfGrpObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 2, 2, 2)
)
ntcMultiDemodConfGrpObsolete.setObjects(
      *(("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsCoDpilots"),
        ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodStatsCoNDpilots"))
)
if mibBuilder.loadTexts:
    ntcMultiDemodConfGrpObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcMultiDemodConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 3300, 2, 1, 1)
)
ntcMultiDemodConfCompV1Standard.setObjects(
    ("NEWTEC-MULTI-DEMOD-MIB", "ntcMultiDemodConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcMultiDemodConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-MULTI-DEMOD-MIB",
    **{"ntcMultiDemodulator": ntcMultiDemodulator,
       "ntcMultiDemodObjects": ntcMultiDemodObjects,
       "ntcMultiDemodAlarm": ntcMultiDemodAlarm,
       "ntcMultiDemodAlmGeneralDemod": ntcMultiDemodAlmGeneralDemod,
       "ntcMultiDemodAlmInternalError": ntcMultiDemodAlmInternalError,
       "ntcMultiDemodAlmInputSaturated": ntcMultiDemodAlmInputSaturated,
       "ntcMultiDemodAlmNoLock": ntcMultiDemodAlmNoLock,
       "ntcMultiDemodAlmLnbPowerControl": ntcMultiDemodAlmLnbPowerControl,
       "ntcMultiDemodAlmDecoderOvrload": ntcMultiDemodAlmDecoderOvrload,
       "ntcMultiDemodAlmNoPlLock": ntcMultiDemodAlmNoPlLock,
       "ntcMultiDemodAlmBufferOverflow": ntcMultiDemodAlmBufferOverflow,
       "ntcMultiDemodAlarmStateTable": ntcMultiDemodAlarmStateTable,
       "ntcMultiDemodAlarmStateEntry": ntcMultiDemodAlarmStateEntry,
       "ntcMultiDemodASDemodId": ntcMultiDemodASDemodId,
       "ntcMultiDemodASGeneralDemod": ntcMultiDemodASGeneralDemod,
       "ntcMultiDemodASInternalError": ntcMultiDemodASInternalError,
       "ntcMultiDemodASInputSaturated": ntcMultiDemodASInputSaturated,
       "ntcMultiDemodASNoPlLock": ntcMultiDemodASNoPlLock,
       "ntcMultiDemodASNoLock": ntcMultiDemodASNoLock,
       "ntcMultiDemodASLnbPowerControl": ntcMultiDemodASLnbPowerControl,
       "ntcMultiDemodASDecoderOverloaded": ntcMultiDemodASDecoderOverloaded,
       "ntcMultiDemodCfgTable": ntcMultiDemodCfgTable,
       "ntcMultiDemodCfgEntry": ntcMultiDemodCfgEntry,
       "ntcMultiDemodCfgDemodId": ntcMultiDemodCfgDemodId,
       "ntcMultiDemodCfgEnable": ntcMultiDemodCfgEnable,
       "ntcMultiDemodCfgMode": ntcMultiDemodCfgMode,
       "ntcMultiDemodCfgInputFrequency": ntcMultiDemodCfgInputFrequency,
       "ntcMultiDemodCfgSymbolRate": ntcMultiDemodCfgSymbolRate,
       "ntcMultiDemodCfgRollOff": ntcMultiDemodCfgRollOff,
       "ntcMultiDemodCfgInputSelection": ntcMultiDemodCfgInputSelection,
       "ntcMultiDemodCfgSpectralInv": ntcMultiDemodCfgSpectralInv,
       "ntcMultiDemodCfgPlScrambSig": ntcMultiDemodCfgPlScrambSig,
       "ntcMultiDemodCfgLnbPowerSupply": ntcMultiDemodCfgLnbPowerSupply,
       "ntcMultiDemodCfgHardwareId": ntcMultiDemodCfgHardwareId,
       "ntcMultiDemodCfgModCodDvbs": ntcMultiDemodCfgModCodDvbs,
       "ntcMultiDemodCfgStreamMode": ntcMultiDemodCfgStreamMode,
       "ntcMultiDemodCfgInterfaceRate": ntcMultiDemodCfgInterfaceRate,
       "ntcMultiDemodCfgAcqRange": ntcMultiDemodCfgAcqRange,
       "ntcMultiDemodCfgPlhdrScramSeq": ntcMultiDemodCfgPlhdrScramSeq,
       "ntcMultiDemodCfgRfFrequency": ntcMultiDemodCfgRfFrequency,
       "ntcMultiDemodCfgModCodAmcDl": ntcMultiDemodCfgModCodAmcDl,
       "ntcMultiDemodCfgLnbClockRef": ntcMultiDemodCfgLnbClockRef,
       "ntcExtMultiDemodCfgTable": ntcExtMultiDemodCfgTable,
       "ntcExtMultiDemodCfgEntry": ntcExtMultiDemodCfgEntry,
       "ntcExtMultiDemodCfgDemodId": ntcExtMultiDemodCfgDemodId,
       "ntcExtMultiDemodCfgOpMode": ntcExtMultiDemodCfgOpMode,
       "ntcMultiDemodMonTable": ntcMultiDemodMonTable,
       "ntcMultiDemodMonEntry": ntcMultiDemodMonEntry,
       "ntcMultiDemodMonDemodId": ntcMultiDemodMonDemodId,
       "ntcMultiDemodMonLbandInputLvl": ntcMultiDemodMonLbandInputLvl,
       "ntcMultiDemodMonCarrierInputLvl": ntcMultiDemodMonCarrierInputLvl,
       "ntcMultiDemodMonEsNo": ntcMultiDemodMonEsNo,
       "ntcMultiDemodMonPhaseNoiseIndic": ntcMultiDemodMonPhaseNoiseIndic,
       "ntcMultiDemodMonOffRefMask": ntcMultiDemodMonOffRefMask,
       "ntcMultiDemodMonNonLinIndic": ntcMultiDemodMonNonLinIndic,
       "ntcMultiDemodMonSymbolRate": ntcMultiDemodMonSymbolRate,
       "ntcMultiDemodMonCarrierOffset": ntcMultiDemodMonCarrierOffset,
       "ntcMultiDemodMonFrameCounter": ntcMultiDemodMonFrameCounter,
       "ntcMultiDemodMonDummyFrameCtr": ntcMultiDemodMonDummyFrameCtr,
       "ntcMultiDemodMonErroredFrameCtr": ntcMultiDemodMonErroredFrameCtr,
       "ntcMultiDemodMonCycleSlipCtr": ntcMultiDemodMonCycleSlipCtr,
       "ntcMultiDemodMonLastModCod": ntcMultiDemodMonLastModCod,
       "ntcMultiDemodModCodStatsReset": ntcMultiDemodModCodStatsReset,
       "ntcMultiDemodMonVber": ntcMultiDemodMonVber,
       "ntcMultiDemodMonBer": ntcMultiDemodMonBer,
       "ntcMultiDemodMonEbNo": ntcMultiDemodMonEbNo,
       "ntcMultiDemodMonLinkMargin": ntcMultiDemodMonLinkMargin,
       "ntcMultiDemodMonOperationalState": ntcMultiDemodMonOperationalState,
       "ntcMultiDemodMonLastNonDumModCod": ntcMultiDemodMonLastNonDumModCod,
       "ntcMultiDemodMonRollOff": ntcMultiDemodMonRollOff,
       "ntcMultiDemodMonQefM": ntcMultiDemodMonQefM,
       "ntcMultiDemodMonSpectralInv": ntcMultiDemodMonSpectralInv,
       "ntcMultiDemodMonVberClp": ntcMultiDemodMonVberClp,
       "ntcMultiDemodMonBerClp": ntcMultiDemodMonBerClp,
       "ntcMultiDemodMonQefMClp": ntcMultiDemodMonQefMClp,
       "ntcMultiDemodMonEbNoClp": ntcMultiDemodMonEbNoClp,
       "ntcMultiDemodMonNonLinIndicAM": ntcMultiDemodMonNonLinIndicAM,
       "ntcMultiDemodStatsTable": ntcMultiDemodStatsTable,
       "ntcMultiDemodStatsEntry": ntcMultiDemodStatsEntry,
       "ntcMultiDemodStatsInx": ntcMultiDemodStatsInx,
       "ntcMultiDemodStatsDemodId": ntcMultiDemodStatsDemodId,
       "ntcMultiDemodStatsModCod": ntcMultiDemodStatsModCod,
       "ntcMultiDemodStatsFrameType": ntcMultiDemodStatsFrameType,
       "ntcMultiDemodStatsPilots": ntcMultiDemodStatsPilots,
       "ntcMultiDemodStatsFrameCtr": ntcMultiDemodStatsFrameCtr,
       "ntcMultiDemodStatsErrFrameCtr": ntcMultiDemodStatsErrFrameCtr,
       "ntcMultiDemodStatsCycleSlipCtr": ntcMultiDemodStatsCycleSlipCtr,
       "ntcMultiDemodStatsPacketErrRatio": ntcMultiDemodStatsPacketErrRatio,
       "ntcMultiDemodStatsLinkMargin": ntcMultiDemodStatsLinkMargin,
       "ntcMultiDemodStatsCoN": ntcMultiDemodStatsCoN,
       "ntcMultiDemodStatsCoD": ntcMultiDemodStatsCoD,
       "ntcMultiDemodStatsCoDpilots": ntcMultiDemodStatsCoDpilots,
       "ntcMultiDemodStatsCoND": ntcMultiDemodStatsCoND,
       "ntcMultiDemodStatsCoNDpilots": ntcMultiDemodStatsCoNDpilots,
       "ntcMultiDemodCmCfg": ntcMultiDemodCmCfg,
       "ntcMultiDemodCmCfgInputSelection": ntcMultiDemodCmCfgInputSelection,
       "ntcMultiDemodCmCfgLnbPowerSupply": ntcMultiDemodCmCfgLnbPowerSupply,
       "ntcMultiDemodCmMon": ntcMultiDemodCmMon,
       "ntcMultiDemodCmMonLbandInputLvl": ntcMultiDemodCmMonLbandInputLvl,
       "ntcMultiDemodEqCliCfgTable": ntcMultiDemodEqCliCfgTable,
       "ntcMultiDemodEqCliCfgEntry": ntcMultiDemodEqCliCfgEntry,
       "ntcMultiDemodEqCfgEnable": ntcMultiDemodEqCfgEnable,
       "ntcMultiDemodBuCarCfgTable": ntcMultiDemodBuCarCfgTable,
       "ntcMultiDemodBuCarCfgEntry": ntcMultiDemodBuCarCfgEntry,
       "ntcMultiDemodBuCarCfgEnable": ntcMultiDemodBuCarCfgEnable,
       "ntcMultiDemodBuCarCfgInpFreq": ntcMultiDemodBuCarCfgInpFreq,
       "ntcMultiDemodBuCarCfgSymbolRate": ntcMultiDemodBuCarCfgSymbolRate,
       "ntcMultiDemodBuCarCfgSwitchTmo": ntcMultiDemodBuCarCfgSwitchTmo,
       "ntcMultiDemodBuCarCfgRfFreq": ntcMultiDemodBuCarCfgRfFreq,
       "ntcMultiDemodBuCarMonTable": ntcMultiDemodBuCarMonTable,
       "ntcMultiDemodBuCarMonEntry": ntcMultiDemodBuCarMonEntry,
       "ntcMultiDemodBuCarMonDemodId": ntcMultiDemodBuCarMonDemodId,
       "ntcMultiDemodBuCarMonActiveCar": ntcMultiDemodBuCarMonActiveCar,
       "ntcMultiDemodBuCarMonSwitchCnt": ntcMultiDemodBuCarMonSwitchCnt,
       "ntcMultiDemodNlpdCliCfgTable": ntcMultiDemodNlpdCliCfgTable,
       "ntcMultiDemodNlpdCliCfgEntry": ntcMultiDemodNlpdCliCfgEntry,
       "ntcMultiDemodNldCfgEnable": ntcMultiDemodNldCfgEnable,
       "ntcMultiDemodNldCfgTrCenFreq": ntcMultiDemodNldCfgTrCenFreq,
       "ntcMultiDemodNldCfgTrBandw": ntcMultiDemodNldCfgTrBandw,
       "ntcMultiDemodNldCfgEnaSingle": ntcMultiDemodNldCfgEnaSingle,
       "ntcMultiDemodExtConvTable": ntcMultiDemodExtConvTable,
       "ntcMultiDemodExtConvEntry": ntcMultiDemodExtConvEntry,
       "ntcMultiDemodExtConvEnable": ntcMultiDemodExtConvEnable,
       "ntcMultiDemodExtConvLoFrequency": ntcMultiDemodExtConvLoFrequency,
       "ntcMultiDemodExtConvSpectralInv": ntcMultiDemodExtConvSpectralInv,
       "ntcMultiDemodCmConv": ntcMultiDemodCmConv,
       "ntcMultiDemodCmConvEnable": ntcMultiDemodCmConvEnable,
       "ntcMultiDemodCmConvLoFrequency": ntcMultiDemodCmConvLoFrequency,
       "ntcMultiDemodCmConvSpectralInv": ntcMultiDemodCmConvSpectralInv,
       "ntcMultiDemodAesConfTable": ntcMultiDemodAesConfTable,
       "ntcMultiDemodAesConfEntry": ntcMultiDemodAesConfEntry,
       "ntcMultiDemodAesConfEnable": ntcMultiDemodAesConfEnable,
       "ntcMultiDemodAesConfGlbEncrypt": ntcMultiDemodAesConfGlbEncrypt,
       "ntcMultiDemodAesConfKeyStren": ntcMultiDemodAesConfKeyStren,
       "ntcMultiDemodAesConfGrpKey": ntcMultiDemodAesConfGrpKey,
       "ntcMultiDemodAesConfClrKeys": ntcMultiDemodAesConfClrKeys,
       "ntcMultiDemodAesGConfTable": ntcMultiDemodAesGConfTable,
       "ntcMultiDemodAesGConfEntry": ntcMultiDemodAesGConfEntry,
       "ntcMultiDemodAesGConfEncEKey": ntcMultiDemodAesGConfEncEKey,
       "ntcMultiDemodAesGConfEncOKey": ntcMultiDemodAesGConfEncOKey,
       "ntcMultiDemodAesGConfEKey": ntcMultiDemodAesGConfEKey,
       "ntcMultiDemodAesGConfOKey": ntcMultiDemodAesGConfOKey,
       "ntcMultiDemodAesSConfTable": ntcMultiDemodAesSConfTable,
       "ntcMultiDemodAesSConfEntry": ntcMultiDemodAesSConfEntry,
       "ntcMultiDemodAesSConfName": ntcMultiDemodAesSConfName,
       "ntcMultiDemodAesSConfRowStatus": ntcMultiDemodAesSConfRowStatus,
       "ntcMultiDemodAesSConfEnable": ntcMultiDemodAesSConfEnable,
       "ntcMultiDemodAesSConfIsi": ntcMultiDemodAesSConfIsi,
       "ntcMultiDemodAesSConfEncEKey": ntcMultiDemodAesSConfEncEKey,
       "ntcMultiDemodAesSConfEncOKey": ntcMultiDemodAesSConfEncOKey,
       "ntcMultiDemodAesSConfEKey": ntcMultiDemodAesSConfEKey,
       "ntcMultiDemodAesSConfOKey": ntcMultiDemodAesSConfOKey,
       "ntcMultiDemodAesSConfDemodId": ntcMultiDemodAesSConfDemodId,
       "ntcMultiDemodAesGMonTable": ntcMultiDemodAesGMonTable,
       "ntcMultiDemodAesGMonEntry": ntcMultiDemodAesGMonEntry,
       "ntcMultiDemodAesGMonDemodId": ntcMultiDemodAesGMonDemodId,
       "ntcMultiDemodAesGMonKeyParity": ntcMultiDemodAesGMonKeyParity,
       "ntcMultiDemodAesSMonTable": ntcMultiDemodAesSMonTable,
       "ntcMultiDemodAesSMonEntry": ntcMultiDemodAesSMonEntry,
       "ntcMultiDemodAesSMonName": ntcMultiDemodAesSMonName,
       "ntcMultiDemodAesSMonDemodId": ntcMultiDemodAesSMonDemodId,
       "ntcMultiDemodAesSMonKeyParity": ntcMultiDemodAesSMonKeyParity,
       "ntcMultiDemodConformance": ntcMultiDemodConformance,
       "ntcMultiDemodConfCompliance": ntcMultiDemodConfCompliance,
       "ntcMultiDemodConfCompV1Standard": ntcMultiDemodConfCompV1Standard,
       "ntcMultiDemodConfGroup": ntcMultiDemodConfGroup,
       "ntcMultiDemodConfGrpV1Standard": ntcMultiDemodConfGrpV1Standard,
       "ntcMultiDemodConfGrpObsolete": ntcMultiDemodConfGrpObsolete}
)
