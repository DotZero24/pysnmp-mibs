# SNMP MIB module (INFINERA-PM-OCHCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OCHCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:52 2025
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

(HCPerfIntervalCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(FloatArbitraryPrecision,
 FloatHundredths) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ochCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30)
)
if mibBuilder.loadTexts:
    ochCtpPmMIB.setRevisions(
        ("2011-10-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OchCtpPmRealTable_Object = MibTable
ochCtpPmRealTable = _OchCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1)
)
if mibBuilder.loadTexts:
    ochCtpPmRealTable.setStatus("current")
_OchCtpPmRealEntry_Object = MibTableRow
ochCtpPmRealEntry = _OchCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1)
)
ochCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ochCtpPmRealEntry.setStatus("current")
_OchCtpPmRealChanOchOpt_Type = FloatHundredths
_OchCtpPmRealChanOchOpt_Object = MibTableColumn
ochCtpPmRealChanOchOpt = _OchCtpPmRealChanOchOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 1),
    _OchCtpPmRealChanOchOpt_Type()
)
ochCtpPmRealChanOchOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealChanOchOpt.setStatus("current")
_OchCtpPmRealChanOchOpr_Type = FloatHundredths
_OchCtpPmRealChanOchOpr_Object = MibTableColumn
ochCtpPmRealChanOchOpr = _OchCtpPmRealChanOchOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 2),
    _OchCtpPmRealChanOchOpr_Type()
)
ochCtpPmRealChanOchOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealChanOchOpr.setStatus("current")
_OchCtpPmRealChanOchLBC_Type = FloatHundredths
_OchCtpPmRealChanOchLBC_Object = MibTableColumn
ochCtpPmRealChanOchLBC = _OchCtpPmRealChanOchLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 3),
    _OchCtpPmRealChanOchLBC_Type()
)
ochCtpPmRealChanOchLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealChanOchLBC.setStatus("current")
_OchCtpPmRealChanOchMeasuredWavelength_Type = FloatHundredths
_OchCtpPmRealChanOchMeasuredWavelength_Object = MibTableColumn
ochCtpPmRealChanOchMeasuredWavelength = _OchCtpPmRealChanOchMeasuredWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 4),
    _OchCtpPmRealChanOchMeasuredWavelength_Type()
)
ochCtpPmRealChanOchMeasuredWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealChanOchMeasuredWavelength.setStatus("current")
_OchCtpPmRealChanOchQValue_Type = FloatHundredths
_OchCtpPmRealChanOchQValue_Object = MibTableColumn
ochCtpPmRealChanOchQValue = _OchCtpPmRealChanOchQValue_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 5),
    _OchCtpPmRealChanOchQValue_Type()
)
ochCtpPmRealChanOchQValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealChanOchQValue.setStatus("current")
_OchCtpPmRealChanOchCD_Type = FloatHundredths
_OchCtpPmRealChanOchCD_Object = MibTableColumn
ochCtpPmRealChanOchCD = _OchCtpPmRealChanOchCD_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 6),
    _OchCtpPmRealChanOchCD_Type()
)
ochCtpPmRealChanOchCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealChanOchCD.setStatus("current")
_OchCtpPmRealPmd_Type = FloatArbitraryPrecision
_OchCtpPmRealPmd_Object = MibTableColumn
ochCtpPmRealPmd = _OchCtpPmRealPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 7),
    _OchCtpPmRealPmd_Type()
)
ochCtpPmRealPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealPmd.setStatus("current")
_OchCtpPmRealSoPmd_Type = FloatArbitraryPrecision
_OchCtpPmRealSoPmd_Object = MibTableColumn
ochCtpPmRealSoPmd = _OchCtpPmRealSoPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 8),
    _OchCtpPmRealSoPmd_Type()
)
ochCtpPmRealSoPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealSoPmd.setStatus("current")
_OchCtpPmBerPreFec_Type = FloatArbitraryPrecision
_OchCtpPmBerPreFec_Object = MibTableColumn
ochCtpPmBerPreFec = _OchCtpPmBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 9),
    _OchCtpPmBerPreFec_Type()
)
ochCtpPmBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPreFec.setStatus("current")
_OchCtpPmRealPhaseCorrection_Type = FloatHundredths
_OchCtpPmRealPhaseCorrection_Object = MibTableColumn
ochCtpPmRealPhaseCorrection = _OchCtpPmRealPhaseCorrection_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 10),
    _OchCtpPmRealPhaseCorrection_Type()
)
ochCtpPmRealPhaseCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealPhaseCorrection.setStatus("current")
_OchCtpPmRealBerPostFec_Type = FloatArbitraryPrecision
_OchCtpPmRealBerPostFec_Object = MibTableColumn
ochCtpPmRealBerPostFec = _OchCtpPmRealBerPostFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 11),
    _OchCtpPmRealBerPostFec_Type()
)
ochCtpPmRealBerPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealBerPostFec.setStatus("current")
_OchCtpPmRealCWProc_Type = HCPerfIntervalCount
_OchCtpPmRealCWProc_Object = MibTableColumn
ochCtpPmRealCWProc = _OchCtpPmRealCWProc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 12),
    _OchCtpPmRealCWProc_Type()
)
ochCtpPmRealCWProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealCWProc.setStatus("current")
_OchCtpPmRealUnCrctblCW_Type = HCPerfIntervalCount
_OchCtpPmRealUnCrctblCW_Object = MibTableColumn
ochCtpPmRealUnCrctblCW = _OchCtpPmRealUnCrctblCW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 13),
    _OchCtpPmRealUnCrctblCW_Type()
)
ochCtpPmRealUnCrctblCW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealUnCrctblCW.setStatus("current")
_OchCtpPmRealCrctdBits_Type = HCPerfIntervalCount
_OchCtpPmRealCrctdBits_Object = MibTableColumn
ochCtpPmRealCrctdBits = _OchCtpPmRealCrctdBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 1, 1, 14),
    _OchCtpPmRealCrctdBits_Type()
)
ochCtpPmRealCrctdBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmRealCrctdBits.setStatus("current")
_OchCtpPmTable_Object = MibTable
ochCtpPmTable = _OchCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2)
)
if mibBuilder.loadTexts:
    ochCtpPmTable.setStatus("current")
_OchCtpPmEntry_Object = MibTableRow
ochCtpPmEntry = _OchCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1)
)
ochCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OCHCTP-MIB", "ochCtpPmSampleDuration"),
    (0, "INFINERA-PM-OCHCTP-MIB", "ochCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    ochCtpPmEntry.setStatus("current")


class _OchCtpPmTimestamp_Type(Integer32):
    """Custom type ochCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OchCtpPmTimestamp_Type.__name__ = "Integer32"
_OchCtpPmTimestamp_Object = MibTableColumn
ochCtpPmTimestamp = _OchCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 1),
    _OchCtpPmTimestamp_Type()
)
ochCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ochCtpPmTimestamp.setStatus("current")


class _OchCtpPmSampleDuration_Type(Integer32):
    """Custom type ochCtpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_OchCtpPmSampleDuration_Type.__name__ = "Integer32"
_OchCtpPmSampleDuration_Object = MibTableColumn
ochCtpPmSampleDuration = _OchCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 2),
    _OchCtpPmSampleDuration_Type()
)
ochCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ochCtpPmSampleDuration.setStatus("current")
_OchCtpPmValidity_Type = TruthValue
_OchCtpPmValidity_Object = MibTableColumn
ochCtpPmValidity = _OchCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 3),
    _OchCtpPmValidity_Type()
)
ochCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmValidity.setStatus("current")
_OchCtpPmChanOchOptMin_Type = FloatHundredths
_OchCtpPmChanOchOptMin_Object = MibTableColumn
ochCtpPmChanOchOptMin = _OchCtpPmChanOchOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 4),
    _OchCtpPmChanOchOptMin_Type()
)
ochCtpPmChanOchOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchOptMin.setStatus("current")
_OchCtpPmChanOchOptMax_Type = FloatHundredths
_OchCtpPmChanOchOptMax_Object = MibTableColumn
ochCtpPmChanOchOptMax = _OchCtpPmChanOchOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 5),
    _OchCtpPmChanOchOptMax_Type()
)
ochCtpPmChanOchOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchOptMax.setStatus("current")
_OchCtpPmChanOchOptAve_Type = FloatHundredths
_OchCtpPmChanOchOptAve_Object = MibTableColumn
ochCtpPmChanOchOptAve = _OchCtpPmChanOchOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 6),
    _OchCtpPmChanOchOptAve_Type()
)
ochCtpPmChanOchOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchOptAve.setStatus("current")
_OchCtpPmChanOchOprMin_Type = FloatHundredths
_OchCtpPmChanOchOprMin_Object = MibTableColumn
ochCtpPmChanOchOprMin = _OchCtpPmChanOchOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 7),
    _OchCtpPmChanOchOprMin_Type()
)
ochCtpPmChanOchOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchOprMin.setStatus("current")
_OchCtpPmChanOchOprMax_Type = FloatHundredths
_OchCtpPmChanOchOprMax_Object = MibTableColumn
ochCtpPmChanOchOprMax = _OchCtpPmChanOchOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 8),
    _OchCtpPmChanOchOprMax_Type()
)
ochCtpPmChanOchOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchOprMax.setStatus("current")
_OchCtpPmChanOchOprAve_Type = FloatHundredths
_OchCtpPmChanOchOprAve_Object = MibTableColumn
ochCtpPmChanOchOprAve = _OchCtpPmChanOchOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 9),
    _OchCtpPmChanOchOprAve_Type()
)
ochCtpPmChanOchOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchOprAve.setStatus("current")
_OchCtpPmChanOchLBCMin_Type = FloatHundredths
_OchCtpPmChanOchLBCMin_Object = MibTableColumn
ochCtpPmChanOchLBCMin = _OchCtpPmChanOchLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 10),
    _OchCtpPmChanOchLBCMin_Type()
)
ochCtpPmChanOchLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchLBCMin.setStatus("current")
_OchCtpPmChanOchLBCMax_Type = FloatHundredths
_OchCtpPmChanOchLBCMax_Object = MibTableColumn
ochCtpPmChanOchLBCMax = _OchCtpPmChanOchLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 11),
    _OchCtpPmChanOchLBCMax_Type()
)
ochCtpPmChanOchLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchLBCMax.setStatus("current")
_OchCtpPmChanOchLBCAve_Type = FloatHundredths
_OchCtpPmChanOchLBCAve_Object = MibTableColumn
ochCtpPmChanOchLBCAve = _OchCtpPmChanOchLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 12),
    _OchCtpPmChanOchLBCAve_Type()
)
ochCtpPmChanOchLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchLBCAve.setStatus("current")
_OchCtpPmChanOchQValueMin_Type = FloatHundredths
_OchCtpPmChanOchQValueMin_Object = MibTableColumn
ochCtpPmChanOchQValueMin = _OchCtpPmChanOchQValueMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 13),
    _OchCtpPmChanOchQValueMin_Type()
)
ochCtpPmChanOchQValueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchQValueMin.setStatus("current")
_OchCtpPmChanOchQValueMax_Type = FloatHundredths
_OchCtpPmChanOchQValueMax_Object = MibTableColumn
ochCtpPmChanOchQValueMax = _OchCtpPmChanOchQValueMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 14),
    _OchCtpPmChanOchQValueMax_Type()
)
ochCtpPmChanOchQValueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchQValueMax.setStatus("current")
_OchCtpPmChanOchQValueAve_Type = FloatHundredths
_OchCtpPmChanOchQValueAve_Object = MibTableColumn
ochCtpPmChanOchQValueAve = _OchCtpPmChanOchQValueAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 15),
    _OchCtpPmChanOchQValueAve_Type()
)
ochCtpPmChanOchQValueAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchQValueAve.setStatus("current")
_OchCtpPmChanOchCDMin_Type = FloatHundredths
_OchCtpPmChanOchCDMin_Object = MibTableColumn
ochCtpPmChanOchCDMin = _OchCtpPmChanOchCDMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 16),
    _OchCtpPmChanOchCDMin_Type()
)
ochCtpPmChanOchCDMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchCDMin.setStatus("current")
_OchCtpPmChanOchCDMax_Type = FloatHundredths
_OchCtpPmChanOchCDMax_Object = MibTableColumn
ochCtpPmChanOchCDMax = _OchCtpPmChanOchCDMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 17),
    _OchCtpPmChanOchCDMax_Type()
)
ochCtpPmChanOchCDMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchCDMax.setStatus("current")
_OchCtpPmChanOchCDAve_Type = FloatHundredths
_OchCtpPmChanOchCDAve_Object = MibTableColumn
ochCtpPmChanOchCDAve = _OchCtpPmChanOchCDAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 18),
    _OchCtpPmChanOchCDAve_Type()
)
ochCtpPmChanOchCDAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmChanOchCDAve.setStatus("current")
_OchCtpPmPmdMin_Type = FloatArbitraryPrecision
_OchCtpPmPmdMin_Object = MibTableColumn
ochCtpPmPmdMin = _OchCtpPmPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 19),
    _OchCtpPmPmdMin_Type()
)
ochCtpPmPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmPmdMin.setStatus("current")
_OchCtpPmPmdMax_Type = FloatArbitraryPrecision
_OchCtpPmPmdMax_Object = MibTableColumn
ochCtpPmPmdMax = _OchCtpPmPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 20),
    _OchCtpPmPmdMax_Type()
)
ochCtpPmPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmPmdMax.setStatus("current")
_OchCtpPmPmdAve_Type = FloatArbitraryPrecision
_OchCtpPmPmdAve_Object = MibTableColumn
ochCtpPmPmdAve = _OchCtpPmPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 21),
    _OchCtpPmPmdAve_Type()
)
ochCtpPmPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmPmdAve.setStatus("current")
_OchCtpPmSoPmdMin_Type = FloatArbitraryPrecision
_OchCtpPmSoPmdMin_Object = MibTableColumn
ochCtpPmSoPmdMin = _OchCtpPmSoPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 22),
    _OchCtpPmSoPmdMin_Type()
)
ochCtpPmSoPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmSoPmdMin.setStatus("current")
_OchCtpPmSoPmdMax_Type = FloatArbitraryPrecision
_OchCtpPmSoPmdMax_Object = MibTableColumn
ochCtpPmSoPmdMax = _OchCtpPmSoPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 23),
    _OchCtpPmSoPmdMax_Type()
)
ochCtpPmSoPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmSoPmdMax.setStatus("current")
_OchCtpPmSoPmdAve_Type = FloatArbitraryPrecision
_OchCtpPmSoPmdAve_Object = MibTableColumn
ochCtpPmSoPmdAve = _OchCtpPmSoPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 24),
    _OchCtpPmSoPmdAve_Type()
)
ochCtpPmSoPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmSoPmdAve.setStatus("current")
_OchCtpPmBerPreFecMin_Type = FloatArbitraryPrecision
_OchCtpPmBerPreFecMin_Object = MibTableColumn
ochCtpPmBerPreFecMin = _OchCtpPmBerPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 25),
    _OchCtpPmBerPreFecMin_Type()
)
ochCtpPmBerPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPreFecMin.setStatus("current")
_OchCtpPmBerPreFecMax_Type = FloatArbitraryPrecision
_OchCtpPmBerPreFecMax_Object = MibTableColumn
ochCtpPmBerPreFecMax = _OchCtpPmBerPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 26),
    _OchCtpPmBerPreFecMax_Type()
)
ochCtpPmBerPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPreFecMax.setStatus("current")
_OchCtpPmBerPreFecAve_Type = FloatArbitraryPrecision
_OchCtpPmBerPreFecAve_Object = MibTableColumn
ochCtpPmBerPreFecAve = _OchCtpPmBerPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 27),
    _OchCtpPmBerPreFecAve_Type()
)
ochCtpPmBerPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPreFecAve.setStatus("current")
_OchCtpPmPhaseCorrectionMin_Type = FloatHundredths
_OchCtpPmPhaseCorrectionMin_Object = MibTableColumn
ochCtpPmPhaseCorrectionMin = _OchCtpPmPhaseCorrectionMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 28),
    _OchCtpPmPhaseCorrectionMin_Type()
)
ochCtpPmPhaseCorrectionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmPhaseCorrectionMin.setStatus("current")
_OchCtpPmPhaseCorrectionMax_Type = FloatHundredths
_OchCtpPmPhaseCorrectionMax_Object = MibTableColumn
ochCtpPmPhaseCorrectionMax = _OchCtpPmPhaseCorrectionMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 29),
    _OchCtpPmPhaseCorrectionMax_Type()
)
ochCtpPmPhaseCorrectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmPhaseCorrectionMax.setStatus("current")
_OchCtpPmPhaseCorrectionAve_Type = FloatHundredths
_OchCtpPmPhaseCorrectionAve_Object = MibTableColumn
ochCtpPmPhaseCorrectionAve = _OchCtpPmPhaseCorrectionAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 30),
    _OchCtpPmPhaseCorrectionAve_Type()
)
ochCtpPmPhaseCorrectionAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmPhaseCorrectionAve.setStatus("current")
_OchCtpPmBerPostFecMin_Type = FloatArbitraryPrecision
_OchCtpPmBerPostFecMin_Object = MibTableColumn
ochCtpPmBerPostFecMin = _OchCtpPmBerPostFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 31),
    _OchCtpPmBerPostFecMin_Type()
)
ochCtpPmBerPostFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPostFecMin.setStatus("current")
_OchCtpPmBerPostFecMax_Type = FloatArbitraryPrecision
_OchCtpPmBerPostFecMax_Object = MibTableColumn
ochCtpPmBerPostFecMax = _OchCtpPmBerPostFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 32),
    _OchCtpPmBerPostFecMax_Type()
)
ochCtpPmBerPostFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPostFecMax.setStatus("current")
_OchCtpPmBerPostFecAve_Type = FloatArbitraryPrecision
_OchCtpPmBerPostFecAve_Object = MibTableColumn
ochCtpPmBerPostFecAve = _OchCtpPmBerPostFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 33),
    _OchCtpPmBerPostFecAve_Type()
)
ochCtpPmBerPostFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmBerPostFecAve.setStatus("current")
_OchCtpPmCWProc_Type = HCPerfIntervalCount
_OchCtpPmCWProc_Object = MibTableColumn
ochCtpPmCWProc = _OchCtpPmCWProc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 34),
    _OchCtpPmCWProc_Type()
)
ochCtpPmCWProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmCWProc.setStatus("current")
_OchCtpPmUnCrctblCW_Type = HCPerfIntervalCount
_OchCtpPmUnCrctblCW_Object = MibTableColumn
ochCtpPmUnCrctblCW = _OchCtpPmUnCrctblCW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 35),
    _OchCtpPmUnCrctblCW_Type()
)
ochCtpPmUnCrctblCW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmUnCrctblCW.setStatus("current")
_OchCtpPmCrctdBits_Type = HCPerfIntervalCount
_OchCtpPmCrctdBits_Object = MibTableColumn
ochCtpPmCrctdBits = _OchCtpPmCrctdBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 2, 1, 36),
    _OchCtpPmCrctdBits_Type()
)
ochCtpPmCrctdBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ochCtpPmCrctdBits.setStatus("current")
_OchCtpPmConformance_ObjectIdentity = ObjectIdentity
ochCtpPmConformance = _OchCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3)
)
_OchCtpPmCompliances_ObjectIdentity = ObjectIdentity
ochCtpPmCompliances = _OchCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3, 1)
)
_OchCtpPmGroups_ObjectIdentity = ObjectIdentity
ochCtpPmGroups = _OchCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3, 2)
)

# Managed Objects groups

ochCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3, 2, 1)
)
ochCtpPmGroup.setObjects(
      *(("INFINERA-PM-OCHCTP-MIB", "ochCtpPmValidity"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchOptMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchOptMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchOptAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchOprMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchOprMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchOprAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchLBCMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchLBCMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchLBCAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchQValueMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchQValueMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchQValueAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchCDMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchCDMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmChanOchCDAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmPmdMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmPmdMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmPmdAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmSoPmdMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmSoPmdMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmSoPmdAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPreFecMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPreFecMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPreFecAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmPhaseCorrectionMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmPhaseCorrectionMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmPhaseCorrectionAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPostFecMin"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPostFecMax"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPostFecAve"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmCWProc"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmUnCrctblCW"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmCrctdBits"))
)
if mibBuilder.loadTexts:
    ochCtpPmGroup.setStatus("current")

ochCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3, 2, 2)
)
ochCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealChanOchOpt"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealChanOchOpr"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealChanOchLBC"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealChanOchMeasuredWavelength"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealChanOchQValue"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealChanOchCD"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealPmd"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealSoPmd"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmBerPreFec"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealPhaseCorrection"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealBerPostFec"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealCWProc"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealUnCrctblCW"),
        ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealCrctdBits"))
)
if mibBuilder.loadTexts:
    ochCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ochCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3, 1, 1)
)
ochCtpPmCompliance.setObjects(
    ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmGroup")
)
if mibBuilder.loadTexts:
    ochCtpPmCompliance.setStatus(
        "current"
    )

ochCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 30, 3, 1, 2)
)
ochCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OCHCTP-MIB", "ochCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    ochCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OCHCTP-MIB",
    **{"ochCtpPmMIB": ochCtpPmMIB,
       "ochCtpPmRealTable": ochCtpPmRealTable,
       "ochCtpPmRealEntry": ochCtpPmRealEntry,
       "ochCtpPmRealChanOchOpt": ochCtpPmRealChanOchOpt,
       "ochCtpPmRealChanOchOpr": ochCtpPmRealChanOchOpr,
       "ochCtpPmRealChanOchLBC": ochCtpPmRealChanOchLBC,
       "ochCtpPmRealChanOchMeasuredWavelength": ochCtpPmRealChanOchMeasuredWavelength,
       "ochCtpPmRealChanOchQValue": ochCtpPmRealChanOchQValue,
       "ochCtpPmRealChanOchCD": ochCtpPmRealChanOchCD,
       "ochCtpPmRealPmd": ochCtpPmRealPmd,
       "ochCtpPmRealSoPmd": ochCtpPmRealSoPmd,
       "ochCtpPmBerPreFec": ochCtpPmBerPreFec,
       "ochCtpPmRealPhaseCorrection": ochCtpPmRealPhaseCorrection,
       "ochCtpPmRealBerPostFec": ochCtpPmRealBerPostFec,
       "ochCtpPmRealCWProc": ochCtpPmRealCWProc,
       "ochCtpPmRealUnCrctblCW": ochCtpPmRealUnCrctblCW,
       "ochCtpPmRealCrctdBits": ochCtpPmRealCrctdBits,
       "ochCtpPmTable": ochCtpPmTable,
       "ochCtpPmEntry": ochCtpPmEntry,
       "ochCtpPmTimestamp": ochCtpPmTimestamp,
       "ochCtpPmSampleDuration": ochCtpPmSampleDuration,
       "ochCtpPmValidity": ochCtpPmValidity,
       "ochCtpPmChanOchOptMin": ochCtpPmChanOchOptMin,
       "ochCtpPmChanOchOptMax": ochCtpPmChanOchOptMax,
       "ochCtpPmChanOchOptAve": ochCtpPmChanOchOptAve,
       "ochCtpPmChanOchOprMin": ochCtpPmChanOchOprMin,
       "ochCtpPmChanOchOprMax": ochCtpPmChanOchOprMax,
       "ochCtpPmChanOchOprAve": ochCtpPmChanOchOprAve,
       "ochCtpPmChanOchLBCMin": ochCtpPmChanOchLBCMin,
       "ochCtpPmChanOchLBCMax": ochCtpPmChanOchLBCMax,
       "ochCtpPmChanOchLBCAve": ochCtpPmChanOchLBCAve,
       "ochCtpPmChanOchQValueMin": ochCtpPmChanOchQValueMin,
       "ochCtpPmChanOchQValueMax": ochCtpPmChanOchQValueMax,
       "ochCtpPmChanOchQValueAve": ochCtpPmChanOchQValueAve,
       "ochCtpPmChanOchCDMin": ochCtpPmChanOchCDMin,
       "ochCtpPmChanOchCDMax": ochCtpPmChanOchCDMax,
       "ochCtpPmChanOchCDAve": ochCtpPmChanOchCDAve,
       "ochCtpPmPmdMin": ochCtpPmPmdMin,
       "ochCtpPmPmdMax": ochCtpPmPmdMax,
       "ochCtpPmPmdAve": ochCtpPmPmdAve,
       "ochCtpPmSoPmdMin": ochCtpPmSoPmdMin,
       "ochCtpPmSoPmdMax": ochCtpPmSoPmdMax,
       "ochCtpPmSoPmdAve": ochCtpPmSoPmdAve,
       "ochCtpPmBerPreFecMin": ochCtpPmBerPreFecMin,
       "ochCtpPmBerPreFecMax": ochCtpPmBerPreFecMax,
       "ochCtpPmBerPreFecAve": ochCtpPmBerPreFecAve,
       "ochCtpPmPhaseCorrectionMin": ochCtpPmPhaseCorrectionMin,
       "ochCtpPmPhaseCorrectionMax": ochCtpPmPhaseCorrectionMax,
       "ochCtpPmPhaseCorrectionAve": ochCtpPmPhaseCorrectionAve,
       "ochCtpPmBerPostFecMin": ochCtpPmBerPostFecMin,
       "ochCtpPmBerPostFecMax": ochCtpPmBerPostFecMax,
       "ochCtpPmBerPostFecAve": ochCtpPmBerPostFecAve,
       "ochCtpPmCWProc": ochCtpPmCWProc,
       "ochCtpPmUnCrctblCW": ochCtpPmUnCrctblCW,
       "ochCtpPmCrctdBits": ochCtpPmCrctdBits,
       "ochCtpPmConformance": ochCtpPmConformance,
       "ochCtpPmCompliances": ochCtpPmCompliances,
       "ochCtpPmCompliance": ochCtpPmCompliance,
       "ochCtpPmRealCompliance": ochCtpPmRealCompliance,
       "ochCtpPmGroups": ochCtpPmGroups,
       "ochCtpPmGroup": ochCtpPmGroup,
       "ochCtpPmRealGroup": ochCtpPmRealGroup}
)
