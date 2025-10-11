# SNMP MIB module (INFINERA-PM-carrierCtp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-carrierCtp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:45 2025
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

carrierCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200)
)
if mibBuilder.loadTexts:
    carrierCtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CarrierCtpPmRealTable_Object = MibTable
carrierCtpPmRealTable = _CarrierCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1)
)
if mibBuilder.loadTexts:
    carrierCtpPmRealTable.setStatus("current")
_CarrierCtpPmRealEntry_Object = MibTableRow
carrierCtpPmRealEntry = _CarrierCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1)
)
carrierCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    carrierCtpPmRealEntry.setStatus("current")
_CarrierCtpPmRealOpt_Type = FloatHundredths
_CarrierCtpPmRealOpt_Object = MibTableColumn
carrierCtpPmRealOpt = _CarrierCtpPmRealOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 1),
    _CarrierCtpPmRealOpt_Type()
)
carrierCtpPmRealOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealOpt.setStatus("current")
_CarrierCtpPmRealQPreFec_Type = FloatHundredths
_CarrierCtpPmRealQPreFec_Object = MibTableColumn
carrierCtpPmRealQPreFec = _CarrierCtpPmRealQPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 2),
    _CarrierCtpPmRealQPreFec_Type()
)
carrierCtpPmRealQPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealQPreFec.setStatus("current")
_CarrierCtpPmRealBerPreFec_Type = FloatArbitraryPrecision
_CarrierCtpPmRealBerPreFec_Object = MibTableColumn
carrierCtpPmRealBerPreFec = _CarrierCtpPmRealBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 3),
    _CarrierCtpPmRealBerPreFec_Type()
)
carrierCtpPmRealBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealBerPreFec.setStatus("current")
_CarrierCtpPmRealTxLBC_Type = FloatHundredths
_CarrierCtpPmRealTxLBC_Object = MibTableColumn
carrierCtpPmRealTxLBC = _CarrierCtpPmRealTxLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 4),
    _CarrierCtpPmRealTxLBC_Type()
)
carrierCtpPmRealTxLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealTxLBC.setStatus("current")
_CarrierCtpPmRealRxLBC_Type = FloatHundredths
_CarrierCtpPmRealRxLBC_Object = MibTableColumn
carrierCtpPmRealRxLBC = _CarrierCtpPmRealRxLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 5),
    _CarrierCtpPmRealRxLBC_Type()
)
carrierCtpPmRealRxLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealRxLBC.setStatus("current")
_CarrierCtpPmRealPmd_Type = FloatArbitraryPrecision
_CarrierCtpPmRealPmd_Object = MibTableColumn
carrierCtpPmRealPmd = _CarrierCtpPmRealPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 6),
    _CarrierCtpPmRealPmd_Type()
)
carrierCtpPmRealPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealPmd.setStatus("current")
_CarrierCtpPmRealSoPmd_Type = FloatArbitraryPrecision
_CarrierCtpPmRealSoPmd_Object = MibTableColumn
carrierCtpPmRealSoPmd = _CarrierCtpPmRealSoPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 7),
    _CarrierCtpPmRealSoPmd_Type()
)
carrierCtpPmRealSoPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealSoPmd.setStatus("current")
_CarrierCtpPmRealChromaticDispersion_Type = FloatArbitraryPrecision
_CarrierCtpPmRealChromaticDispersion_Object = MibTableColumn
carrierCtpPmRealChromaticDispersion = _CarrierCtpPmRealChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 8),
    _CarrierCtpPmRealChromaticDispersion_Type()
)
carrierCtpPmRealChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealChromaticDispersion.setStatus("current")
_CarrierCtpPmRealPhaseCorrection_Type = FloatHundredths
_CarrierCtpPmRealPhaseCorrection_Object = MibTableColumn
carrierCtpPmRealPhaseCorrection = _CarrierCtpPmRealPhaseCorrection_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 9),
    _CarrierCtpPmRealPhaseCorrection_Type()
)
carrierCtpPmRealPhaseCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealPhaseCorrection.setStatus("current")
_CarrierCtpPmRealBerPostFec_Type = FloatArbitraryPrecision
_CarrierCtpPmRealBerPostFec_Object = MibTableColumn
carrierCtpPmRealBerPostFec = _CarrierCtpPmRealBerPostFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 10),
    _CarrierCtpPmRealBerPostFec_Type()
)
carrierCtpPmRealBerPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealBerPostFec.setStatus("current")
_CarrierCtpPmRealCodeWord_Type = Counter64
_CarrierCtpPmRealCodeWord_Object = MibTableColumn
carrierCtpPmRealCodeWord = _CarrierCtpPmRealCodeWord_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 11),
    _CarrierCtpPmRealCodeWord_Type()
)
carrierCtpPmRealCodeWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealCodeWord.setStatus("current")
_CarrierCtpPmRealUnCorrectedCodeWord_Type = Counter64
_CarrierCtpPmRealUnCorrectedCodeWord_Object = MibTableColumn
carrierCtpPmRealUnCorrectedCodeWord = _CarrierCtpPmRealUnCorrectedCodeWord_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 12),
    _CarrierCtpPmRealUnCorrectedCodeWord_Type()
)
carrierCtpPmRealUnCorrectedCodeWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealUnCorrectedCodeWord.setStatus("current")
_CarrierCtpPmRealCorrectedBits_Type = Counter64
_CarrierCtpPmRealCorrectedBits_Object = MibTableColumn
carrierCtpPmRealCorrectedBits = _CarrierCtpPmRealCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 13),
    _CarrierCtpPmRealCorrectedBits_Type()
)
carrierCtpPmRealCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealCorrectedBits.setStatus("current")
_CarrierCtpPmRealWavelength_Type = FloatHundredths
_CarrierCtpPmRealWavelength_Object = MibTableColumn
carrierCtpPmRealWavelength = _CarrierCtpPmRealWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 1, 1, 14),
    _CarrierCtpPmRealWavelength_Type()
)
carrierCtpPmRealWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRealWavelength.setStatus("current")
_CarrierCtpPmTable_Object = MibTable
carrierCtpPmTable = _CarrierCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2)
)
if mibBuilder.loadTexts:
    carrierCtpPmTable.setStatus("current")
_CarrierCtpPmEntry_Object = MibTableRow
carrierCtpPmEntry = _CarrierCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1)
)
carrierCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-carrierCtp-MIB", "carrierCtpPmSampleDuration"),
    (0, "INFINERA-PM-carrierCtp-MIB", "carrierCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    carrierCtpPmEntry.setStatus("current")


class _CarrierCtpPmTimestamp_Type(Integer32):
    """Custom type carrierCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CarrierCtpPmTimestamp_Type.__name__ = "Integer32"
_CarrierCtpPmTimestamp_Object = MibTableColumn
carrierCtpPmTimestamp = _CarrierCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 1),
    _CarrierCtpPmTimestamp_Type()
)
carrierCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    carrierCtpPmTimestamp.setStatus("current")


class _CarrierCtpPmSampleDuration_Type(Integer32):
    """Custom type carrierCtpPmSampleDuration based on Integer32"""
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


_CarrierCtpPmSampleDuration_Type.__name__ = "Integer32"
_CarrierCtpPmSampleDuration_Object = MibTableColumn
carrierCtpPmSampleDuration = _CarrierCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 2),
    _CarrierCtpPmSampleDuration_Type()
)
carrierCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    carrierCtpPmSampleDuration.setStatus("current")
_CarrierCtpPmValidity_Type = TruthValue
_CarrierCtpPmValidity_Object = MibTableColumn
carrierCtpPmValidity = _CarrierCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 3),
    _CarrierCtpPmValidity_Type()
)
carrierCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmValidity.setStatus("current")
_CarrierCtpPmOptMin_Type = FloatHundredths
_CarrierCtpPmOptMin_Object = MibTableColumn
carrierCtpPmOptMin = _CarrierCtpPmOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 4),
    _CarrierCtpPmOptMin_Type()
)
carrierCtpPmOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmOptMin.setStatus("current")
_CarrierCtpPmOptMax_Type = FloatHundredths
_CarrierCtpPmOptMax_Object = MibTableColumn
carrierCtpPmOptMax = _CarrierCtpPmOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 5),
    _CarrierCtpPmOptMax_Type()
)
carrierCtpPmOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmOptMax.setStatus("current")
_CarrierCtpPmOptAve_Type = FloatHundredths
_CarrierCtpPmOptAve_Object = MibTableColumn
carrierCtpPmOptAve = _CarrierCtpPmOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 6),
    _CarrierCtpPmOptAve_Type()
)
carrierCtpPmOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmOptAve.setStatus("current")
_CarrierCtpPmQPreFecMin_Type = FloatHundredths
_CarrierCtpPmQPreFecMin_Object = MibTableColumn
carrierCtpPmQPreFecMin = _CarrierCtpPmQPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 7),
    _CarrierCtpPmQPreFecMin_Type()
)
carrierCtpPmQPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmQPreFecMin.setStatus("current")
_CarrierCtpPmQPreFecMax_Type = FloatHundredths
_CarrierCtpPmQPreFecMax_Object = MibTableColumn
carrierCtpPmQPreFecMax = _CarrierCtpPmQPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 8),
    _CarrierCtpPmQPreFecMax_Type()
)
carrierCtpPmQPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmQPreFecMax.setStatus("current")
_CarrierCtpPmQPreFecAve_Type = FloatHundredths
_CarrierCtpPmQPreFecAve_Object = MibTableColumn
carrierCtpPmQPreFecAve = _CarrierCtpPmQPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 9),
    _CarrierCtpPmQPreFecAve_Type()
)
carrierCtpPmQPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmQPreFecAve.setStatus("current")
_CarrierCtpPmBerPreFecMin_Type = FloatArbitraryPrecision
_CarrierCtpPmBerPreFecMin_Object = MibTableColumn
carrierCtpPmBerPreFecMin = _CarrierCtpPmBerPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 10),
    _CarrierCtpPmBerPreFecMin_Type()
)
carrierCtpPmBerPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmBerPreFecMin.setStatus("current")
_CarrierCtpPmBerPreFecMax_Type = FloatArbitraryPrecision
_CarrierCtpPmBerPreFecMax_Object = MibTableColumn
carrierCtpPmBerPreFecMax = _CarrierCtpPmBerPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 11),
    _CarrierCtpPmBerPreFecMax_Type()
)
carrierCtpPmBerPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmBerPreFecMax.setStatus("current")
_CarrierCtpPmBerPreFecAve_Type = FloatArbitraryPrecision
_CarrierCtpPmBerPreFecAve_Object = MibTableColumn
carrierCtpPmBerPreFecAve = _CarrierCtpPmBerPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 12),
    _CarrierCtpPmBerPreFecAve_Type()
)
carrierCtpPmBerPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmBerPreFecAve.setStatus("current")
_CarrierCtpPmTxLBCMin_Type = FloatHundredths
_CarrierCtpPmTxLBCMin_Object = MibTableColumn
carrierCtpPmTxLBCMin = _CarrierCtpPmTxLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 13),
    _CarrierCtpPmTxLBCMin_Type()
)
carrierCtpPmTxLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmTxLBCMin.setStatus("current")
_CarrierCtpPmTxLBCMax_Type = FloatHundredths
_CarrierCtpPmTxLBCMax_Object = MibTableColumn
carrierCtpPmTxLBCMax = _CarrierCtpPmTxLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 14),
    _CarrierCtpPmTxLBCMax_Type()
)
carrierCtpPmTxLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmTxLBCMax.setStatus("current")
_CarrierCtpPmTxLBCAve_Type = FloatHundredths
_CarrierCtpPmTxLBCAve_Object = MibTableColumn
carrierCtpPmTxLBCAve = _CarrierCtpPmTxLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 15),
    _CarrierCtpPmTxLBCAve_Type()
)
carrierCtpPmTxLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmTxLBCAve.setStatus("current")
_CarrierCtpPmRxLBCMin_Type = FloatHundredths
_CarrierCtpPmRxLBCMin_Object = MibTableColumn
carrierCtpPmRxLBCMin = _CarrierCtpPmRxLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 16),
    _CarrierCtpPmRxLBCMin_Type()
)
carrierCtpPmRxLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRxLBCMin.setStatus("current")
_CarrierCtpPmRxLBCMax_Type = FloatHundredths
_CarrierCtpPmRxLBCMax_Object = MibTableColumn
carrierCtpPmRxLBCMax = _CarrierCtpPmRxLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 17),
    _CarrierCtpPmRxLBCMax_Type()
)
carrierCtpPmRxLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRxLBCMax.setStatus("current")
_CarrierCtpPmRxLBCAve_Type = FloatHundredths
_CarrierCtpPmRxLBCAve_Object = MibTableColumn
carrierCtpPmRxLBCAve = _CarrierCtpPmRxLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 18),
    _CarrierCtpPmRxLBCAve_Type()
)
carrierCtpPmRxLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmRxLBCAve.setStatus("current")
_CarrierCtpPmPmdMin_Type = FloatArbitraryPrecision
_CarrierCtpPmPmdMin_Object = MibTableColumn
carrierCtpPmPmdMin = _CarrierCtpPmPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 19),
    _CarrierCtpPmPmdMin_Type()
)
carrierCtpPmPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmPmdMin.setStatus("current")
_CarrierCtpPmPmdMax_Type = FloatArbitraryPrecision
_CarrierCtpPmPmdMax_Object = MibTableColumn
carrierCtpPmPmdMax = _CarrierCtpPmPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 20),
    _CarrierCtpPmPmdMax_Type()
)
carrierCtpPmPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmPmdMax.setStatus("current")
_CarrierCtpPmPmdAve_Type = FloatArbitraryPrecision
_CarrierCtpPmPmdAve_Object = MibTableColumn
carrierCtpPmPmdAve = _CarrierCtpPmPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 21),
    _CarrierCtpPmPmdAve_Type()
)
carrierCtpPmPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmPmdAve.setStatus("current")
_CarrierCtpPmSoPmdMin_Type = FloatArbitraryPrecision
_CarrierCtpPmSoPmdMin_Object = MibTableColumn
carrierCtpPmSoPmdMin = _CarrierCtpPmSoPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 22),
    _CarrierCtpPmSoPmdMin_Type()
)
carrierCtpPmSoPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmSoPmdMin.setStatus("current")
_CarrierCtpPmSoPmdMax_Type = FloatArbitraryPrecision
_CarrierCtpPmSoPmdMax_Object = MibTableColumn
carrierCtpPmSoPmdMax = _CarrierCtpPmSoPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 23),
    _CarrierCtpPmSoPmdMax_Type()
)
carrierCtpPmSoPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmSoPmdMax.setStatus("current")
_CarrierCtpPmSoPmdAve_Type = FloatArbitraryPrecision
_CarrierCtpPmSoPmdAve_Object = MibTableColumn
carrierCtpPmSoPmdAve = _CarrierCtpPmSoPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 24),
    _CarrierCtpPmSoPmdAve_Type()
)
carrierCtpPmSoPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmSoPmdAve.setStatus("current")
_CarrierCtpPmChromaticDispersionMin_Type = FloatArbitraryPrecision
_CarrierCtpPmChromaticDispersionMin_Object = MibTableColumn
carrierCtpPmChromaticDispersionMin = _CarrierCtpPmChromaticDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 25),
    _CarrierCtpPmChromaticDispersionMin_Type()
)
carrierCtpPmChromaticDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmChromaticDispersionMin.setStatus("current")
_CarrierCtpPmChromaticDispersionMax_Type = FloatArbitraryPrecision
_CarrierCtpPmChromaticDispersionMax_Object = MibTableColumn
carrierCtpPmChromaticDispersionMax = _CarrierCtpPmChromaticDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 26),
    _CarrierCtpPmChromaticDispersionMax_Type()
)
carrierCtpPmChromaticDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmChromaticDispersionMax.setStatus("current")
_CarrierCtpPmChromaticDispersionAve_Type = FloatArbitraryPrecision
_CarrierCtpPmChromaticDispersionAve_Object = MibTableColumn
carrierCtpPmChromaticDispersionAve = _CarrierCtpPmChromaticDispersionAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 27),
    _CarrierCtpPmChromaticDispersionAve_Type()
)
carrierCtpPmChromaticDispersionAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmChromaticDispersionAve.setStatus("current")
_CarrierCtpPmPhaseCorrectionMin_Type = FloatHundredths
_CarrierCtpPmPhaseCorrectionMin_Object = MibTableColumn
carrierCtpPmPhaseCorrectionMin = _CarrierCtpPmPhaseCorrectionMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 28),
    _CarrierCtpPmPhaseCorrectionMin_Type()
)
carrierCtpPmPhaseCorrectionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmPhaseCorrectionMin.setStatus("current")
_CarrierCtpPmPhaseCorrectionMax_Type = FloatHundredths
_CarrierCtpPmPhaseCorrectionMax_Object = MibTableColumn
carrierCtpPmPhaseCorrectionMax = _CarrierCtpPmPhaseCorrectionMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 29),
    _CarrierCtpPmPhaseCorrectionMax_Type()
)
carrierCtpPmPhaseCorrectionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmPhaseCorrectionMax.setStatus("current")
_CarrierCtpPmPhaseCorrectionAve_Type = FloatHundredths
_CarrierCtpPmPhaseCorrectionAve_Object = MibTableColumn
carrierCtpPmPhaseCorrectionAve = _CarrierCtpPmPhaseCorrectionAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 30),
    _CarrierCtpPmPhaseCorrectionAve_Type()
)
carrierCtpPmPhaseCorrectionAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmPhaseCorrectionAve.setStatus("current")
_CarrierCtpPmBerPostFecMin_Type = FloatArbitraryPrecision
_CarrierCtpPmBerPostFecMin_Object = MibTableColumn
carrierCtpPmBerPostFecMin = _CarrierCtpPmBerPostFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 31),
    _CarrierCtpPmBerPostFecMin_Type()
)
carrierCtpPmBerPostFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmBerPostFecMin.setStatus("current")
_CarrierCtpPmBerPostFecMax_Type = FloatArbitraryPrecision
_CarrierCtpPmBerPostFecMax_Object = MibTableColumn
carrierCtpPmBerPostFecMax = _CarrierCtpPmBerPostFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 32),
    _CarrierCtpPmBerPostFecMax_Type()
)
carrierCtpPmBerPostFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmBerPostFecMax.setStatus("current")
_CarrierCtpPmBerPostFecAve_Type = FloatArbitraryPrecision
_CarrierCtpPmBerPostFecAve_Object = MibTableColumn
carrierCtpPmBerPostFecAve = _CarrierCtpPmBerPostFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 33),
    _CarrierCtpPmBerPostFecAve_Type()
)
carrierCtpPmBerPostFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmBerPostFecAve.setStatus("current")
_CarrierCtpPmCodeWord_Type = HCPerfIntervalCount
_CarrierCtpPmCodeWord_Object = MibTableColumn
carrierCtpPmCodeWord = _CarrierCtpPmCodeWord_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 34),
    _CarrierCtpPmCodeWord_Type()
)
carrierCtpPmCodeWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmCodeWord.setStatus("current")
_CarrierCtpPmUnCorrectedCodeWord_Type = HCPerfIntervalCount
_CarrierCtpPmUnCorrectedCodeWord_Object = MibTableColumn
carrierCtpPmUnCorrectedCodeWord = _CarrierCtpPmUnCorrectedCodeWord_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 35),
    _CarrierCtpPmUnCorrectedCodeWord_Type()
)
carrierCtpPmUnCorrectedCodeWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmUnCorrectedCodeWord.setStatus("current")
_CarrierCtpPmCorrectedBits_Type = HCPerfIntervalCount
_CarrierCtpPmCorrectedBits_Object = MibTableColumn
carrierCtpPmCorrectedBits = _CarrierCtpPmCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 2, 1, 36),
    _CarrierCtpPmCorrectedBits_Type()
)
carrierCtpPmCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carrierCtpPmCorrectedBits.setStatus("current")
_CarrierCtpPmConformance_ObjectIdentity = ObjectIdentity
carrierCtpPmConformance = _CarrierCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3)
)
_CarrierCtpPmCompliances_ObjectIdentity = ObjectIdentity
carrierCtpPmCompliances = _CarrierCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3, 1)
)
_CarrierCtpPmGroups_ObjectIdentity = ObjectIdentity
carrierCtpPmGroups = _CarrierCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3, 2)
)

# Managed Objects groups

carrierCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3, 2, 1)
)
carrierCtpPmGroup.setObjects(
      *(("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmValidity"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmOptMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmOptMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmOptAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmQPreFecMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmQPreFecMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmQPreFecAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmBerPreFecMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmBerPreFecMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmBerPreFecAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmTxLBCMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmTxLBCMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmTxLBCAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRxLBCMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRxLBCMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRxLBCAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmPmdMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmPmdMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmPmdAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmSoPmdMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmSoPmdMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmSoPmdAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmChromaticDispersionMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmChromaticDispersionMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmChromaticDispersionAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmPhaseCorrectionMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmPhaseCorrectionMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmPhaseCorrectionAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmBerPostFecMin"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmBerPostFecMax"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmBerPostFecAve"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmCodeWord"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmUnCorrectedCodeWord"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmCorrectedBits"))
)
if mibBuilder.loadTexts:
    carrierCtpPmGroup.setStatus("current")

carrierCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3, 2, 2)
)
carrierCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealOpt"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealQPreFec"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealBerPreFec"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealTxLBC"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealRxLBC"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealPmd"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealSoPmd"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealChromaticDispersion"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealPhaseCorrection"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealBerPostFec"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealCodeWord"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealUnCorrectedCodeWord"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealCorrectedBits"),
        ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealWavelength"))
)
if mibBuilder.loadTexts:
    carrierCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

carrierCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3, 1, 1)
)
carrierCtpPmCompliance.setObjects(
    ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmGroup")
)
if mibBuilder.loadTexts:
    carrierCtpPmCompliance.setStatus(
        "current"
    )

carrierCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 200, 3, 1, 2)
)
carrierCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-carrierCtp-MIB", "carrierCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    carrierCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-carrierCtp-MIB",
    **{"carrierCtpPmMIB": carrierCtpPmMIB,
       "carrierCtpPmRealTable": carrierCtpPmRealTable,
       "carrierCtpPmRealEntry": carrierCtpPmRealEntry,
       "carrierCtpPmRealOpt": carrierCtpPmRealOpt,
       "carrierCtpPmRealQPreFec": carrierCtpPmRealQPreFec,
       "carrierCtpPmRealBerPreFec": carrierCtpPmRealBerPreFec,
       "carrierCtpPmRealTxLBC": carrierCtpPmRealTxLBC,
       "carrierCtpPmRealRxLBC": carrierCtpPmRealRxLBC,
       "carrierCtpPmRealPmd": carrierCtpPmRealPmd,
       "carrierCtpPmRealSoPmd": carrierCtpPmRealSoPmd,
       "carrierCtpPmRealChromaticDispersion": carrierCtpPmRealChromaticDispersion,
       "carrierCtpPmRealPhaseCorrection": carrierCtpPmRealPhaseCorrection,
       "carrierCtpPmRealBerPostFec": carrierCtpPmRealBerPostFec,
       "carrierCtpPmRealCodeWord": carrierCtpPmRealCodeWord,
       "carrierCtpPmRealUnCorrectedCodeWord": carrierCtpPmRealUnCorrectedCodeWord,
       "carrierCtpPmRealCorrectedBits": carrierCtpPmRealCorrectedBits,
       "carrierCtpPmRealWavelength": carrierCtpPmRealWavelength,
       "carrierCtpPmTable": carrierCtpPmTable,
       "carrierCtpPmEntry": carrierCtpPmEntry,
       "carrierCtpPmTimestamp": carrierCtpPmTimestamp,
       "carrierCtpPmSampleDuration": carrierCtpPmSampleDuration,
       "carrierCtpPmValidity": carrierCtpPmValidity,
       "carrierCtpPmOptMin": carrierCtpPmOptMin,
       "carrierCtpPmOptMax": carrierCtpPmOptMax,
       "carrierCtpPmOptAve": carrierCtpPmOptAve,
       "carrierCtpPmQPreFecMin": carrierCtpPmQPreFecMin,
       "carrierCtpPmQPreFecMax": carrierCtpPmQPreFecMax,
       "carrierCtpPmQPreFecAve": carrierCtpPmQPreFecAve,
       "carrierCtpPmBerPreFecMin": carrierCtpPmBerPreFecMin,
       "carrierCtpPmBerPreFecMax": carrierCtpPmBerPreFecMax,
       "carrierCtpPmBerPreFecAve": carrierCtpPmBerPreFecAve,
       "carrierCtpPmTxLBCMin": carrierCtpPmTxLBCMin,
       "carrierCtpPmTxLBCMax": carrierCtpPmTxLBCMax,
       "carrierCtpPmTxLBCAve": carrierCtpPmTxLBCAve,
       "carrierCtpPmRxLBCMin": carrierCtpPmRxLBCMin,
       "carrierCtpPmRxLBCMax": carrierCtpPmRxLBCMax,
       "carrierCtpPmRxLBCAve": carrierCtpPmRxLBCAve,
       "carrierCtpPmPmdMin": carrierCtpPmPmdMin,
       "carrierCtpPmPmdMax": carrierCtpPmPmdMax,
       "carrierCtpPmPmdAve": carrierCtpPmPmdAve,
       "carrierCtpPmSoPmdMin": carrierCtpPmSoPmdMin,
       "carrierCtpPmSoPmdMax": carrierCtpPmSoPmdMax,
       "carrierCtpPmSoPmdAve": carrierCtpPmSoPmdAve,
       "carrierCtpPmChromaticDispersionMin": carrierCtpPmChromaticDispersionMin,
       "carrierCtpPmChromaticDispersionMax": carrierCtpPmChromaticDispersionMax,
       "carrierCtpPmChromaticDispersionAve": carrierCtpPmChromaticDispersionAve,
       "carrierCtpPmPhaseCorrectionMin": carrierCtpPmPhaseCorrectionMin,
       "carrierCtpPmPhaseCorrectionMax": carrierCtpPmPhaseCorrectionMax,
       "carrierCtpPmPhaseCorrectionAve": carrierCtpPmPhaseCorrectionAve,
       "carrierCtpPmBerPostFecMin": carrierCtpPmBerPostFecMin,
       "carrierCtpPmBerPostFecMax": carrierCtpPmBerPostFecMax,
       "carrierCtpPmBerPostFecAve": carrierCtpPmBerPostFecAve,
       "carrierCtpPmCodeWord": carrierCtpPmCodeWord,
       "carrierCtpPmUnCorrectedCodeWord": carrierCtpPmUnCorrectedCodeWord,
       "carrierCtpPmCorrectedBits": carrierCtpPmCorrectedBits,
       "carrierCtpPmConformance": carrierCtpPmConformance,
       "carrierCtpPmCompliances": carrierCtpPmCompliances,
       "carrierCtpPmCompliance": carrierCtpPmCompliance,
       "carrierCtpPmRealCompliance": carrierCtpPmRealCompliance,
       "carrierCtpPmGroups": carrierCtpPmGroups,
       "carrierCtpPmGroup": carrierCtpPmGroup,
       "carrierCtpPmRealGroup": carrierCtpPmRealGroup}
)
