# SNMP MIB module (INFINERA-PM-LMOCHPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-LMOCHPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:06 2025
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

lmOchPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24)
)
if mibBuilder.loadTexts:
    lmOchPtpPmMIB.setRevisions(
        ("2011-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmOchPtpPmRealTable_Object = MibTable
lmOchPtpPmRealTable = _LmOchPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1)
)
if mibBuilder.loadTexts:
    lmOchPtpPmRealTable.setStatus("current")
_LmOchPtpPmRealEntry_Object = MibTableRow
lmOchPtpPmRealEntry = _LmOchPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1)
)
lmOchPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmOchPtpPmRealEntry.setStatus("current")
_LmOchPtpPmRealChanOchOpt_Type = FloatHundredths
_LmOchPtpPmRealChanOchOpt_Object = MibTableColumn
lmOchPtpPmRealChanOchOpt = _LmOchPtpPmRealChanOchOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 1),
    _LmOchPtpPmRealChanOchOpt_Type()
)
lmOchPtpPmRealChanOchOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchOpt.setStatus("current")
_LmOchPtpPmRealChanOchOpr_Type = FloatHundredths
_LmOchPtpPmRealChanOchOpr_Object = MibTableColumn
lmOchPtpPmRealChanOchOpr = _LmOchPtpPmRealChanOchOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 2),
    _LmOchPtpPmRealChanOchOpr_Type()
)
lmOchPtpPmRealChanOchOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchOpr.setStatus("current")
_LmOchPtpPmRealChanOchLBC_Type = FloatHundredths
_LmOchPtpPmRealChanOchLBC_Object = MibTableColumn
lmOchPtpPmRealChanOchLBC = _LmOchPtpPmRealChanOchLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 3),
    _LmOchPtpPmRealChanOchLBC_Type()
)
lmOchPtpPmRealChanOchLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchLBC.setStatus("current")
_LmOchPtpPmRealChanOchChromaticDispersion_Type = FloatHundredths
_LmOchPtpPmRealChanOchChromaticDispersion_Object = MibTableColumn
lmOchPtpPmRealChanOchChromaticDispersion = _LmOchPtpPmRealChanOchChromaticDispersion_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 4),
    _LmOchPtpPmRealChanOchChromaticDispersion_Type()
)
lmOchPtpPmRealChanOchChromaticDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchChromaticDispersion.setStatus("current")
_LmOchPtpPmRealChanOchQ_Type = FloatHundredths
_LmOchPtpPmRealChanOchQ_Object = MibTableColumn
lmOchPtpPmRealChanOchQ = _LmOchPtpPmRealChanOchQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 5),
    _LmOchPtpPmRealChanOchQ_Type()
)
lmOchPtpPmRealChanOchQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchQ.setStatus("current")
_LmOchPtpPmRealChanOchPmd_Type = FloatArbitraryPrecision
_LmOchPtpPmRealChanOchPmd_Object = MibTableColumn
lmOchPtpPmRealChanOchPmd = _LmOchPtpPmRealChanOchPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 6),
    _LmOchPtpPmRealChanOchPmd_Type()
)
lmOchPtpPmRealChanOchPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchPmd.setStatus("current")
_LmOchPtpPmRealChanOchSoPmd_Type = FloatArbitraryPrecision
_LmOchPtpPmRealChanOchSoPmd_Object = MibTableColumn
lmOchPtpPmRealChanOchSoPmd = _LmOchPtpPmRealChanOchSoPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 1, 1, 7),
    _LmOchPtpPmRealChanOchSoPmd_Type()
)
lmOchPtpPmRealChanOchSoPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmRealChanOchSoPmd.setStatus("current")
_LmOchPtpPmTable_Object = MibTable
lmOchPtpPmTable = _LmOchPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2)
)
if mibBuilder.loadTexts:
    lmOchPtpPmTable.setStatus("current")
_LmOchPtpPmEntry_Object = MibTableRow
lmOchPtpPmEntry = _LmOchPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1)
)
lmOchPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmSampleDuration"),
    (0, "INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    lmOchPtpPmEntry.setStatus("current")


class _LmOchPtpPmTimestamp_Type(Integer32):
    """Custom type lmOchPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LmOchPtpPmTimestamp_Type.__name__ = "Integer32"
_LmOchPtpPmTimestamp_Object = MibTableColumn
lmOchPtpPmTimestamp = _LmOchPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 1),
    _LmOchPtpPmTimestamp_Type()
)
lmOchPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmOchPtpPmTimestamp.setStatus("current")


class _LmOchPtpPmSampleDuration_Type(Integer32):
    """Custom type lmOchPtpPmSampleDuration based on Integer32"""
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


_LmOchPtpPmSampleDuration_Type.__name__ = "Integer32"
_LmOchPtpPmSampleDuration_Object = MibTableColumn
lmOchPtpPmSampleDuration = _LmOchPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 2),
    _LmOchPtpPmSampleDuration_Type()
)
lmOchPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lmOchPtpPmSampleDuration.setStatus("current")
_LmOchPtpPmValidity_Type = TruthValue
_LmOchPtpPmValidity_Object = MibTableColumn
lmOchPtpPmValidity = _LmOchPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 3),
    _LmOchPtpPmValidity_Type()
)
lmOchPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmValidity.setStatus("current")
_LmOchPtpPmChanOchOptMin_Type = FloatHundredths
_LmOchPtpPmChanOchOptMin_Object = MibTableColumn
lmOchPtpPmChanOchOptMin = _LmOchPtpPmChanOchOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 4),
    _LmOchPtpPmChanOchOptMin_Type()
)
lmOchPtpPmChanOchOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchOptMin.setStatus("current")
_LmOchPtpPmChanOchOptMax_Type = FloatHundredths
_LmOchPtpPmChanOchOptMax_Object = MibTableColumn
lmOchPtpPmChanOchOptMax = _LmOchPtpPmChanOchOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 5),
    _LmOchPtpPmChanOchOptMax_Type()
)
lmOchPtpPmChanOchOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchOptMax.setStatus("current")
_LmOchPtpPmChanOchOptAve_Type = FloatHundredths
_LmOchPtpPmChanOchOptAve_Object = MibTableColumn
lmOchPtpPmChanOchOptAve = _LmOchPtpPmChanOchOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 6),
    _LmOchPtpPmChanOchOptAve_Type()
)
lmOchPtpPmChanOchOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchOptAve.setStatus("current")
_LmOchPtpPmChanOchOprMin_Type = FloatHundredths
_LmOchPtpPmChanOchOprMin_Object = MibTableColumn
lmOchPtpPmChanOchOprMin = _LmOchPtpPmChanOchOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 7),
    _LmOchPtpPmChanOchOprMin_Type()
)
lmOchPtpPmChanOchOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchOprMin.setStatus("current")
_LmOchPtpPmChanOchOprMax_Type = FloatHundredths
_LmOchPtpPmChanOchOprMax_Object = MibTableColumn
lmOchPtpPmChanOchOprMax = _LmOchPtpPmChanOchOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 8),
    _LmOchPtpPmChanOchOprMax_Type()
)
lmOchPtpPmChanOchOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchOprMax.setStatus("current")
_LmOchPtpPmChanOchOprAve_Type = FloatHundredths
_LmOchPtpPmChanOchOprAve_Object = MibTableColumn
lmOchPtpPmChanOchOprAve = _LmOchPtpPmChanOchOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 9),
    _LmOchPtpPmChanOchOprAve_Type()
)
lmOchPtpPmChanOchOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchOprAve.setStatus("current")
_LmOchPtpPmChanOchLBCMin_Type = FloatHundredths
_LmOchPtpPmChanOchLBCMin_Object = MibTableColumn
lmOchPtpPmChanOchLBCMin = _LmOchPtpPmChanOchLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 10),
    _LmOchPtpPmChanOchLBCMin_Type()
)
lmOchPtpPmChanOchLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchLBCMin.setStatus("current")
_LmOchPtpPmChanOchLBCMax_Type = FloatHundredths
_LmOchPtpPmChanOchLBCMax_Object = MibTableColumn
lmOchPtpPmChanOchLBCMax = _LmOchPtpPmChanOchLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 11),
    _LmOchPtpPmChanOchLBCMax_Type()
)
lmOchPtpPmChanOchLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchLBCMax.setStatus("current")
_LmOchPtpPmChanOchLBCAve_Type = FloatHundredths
_LmOchPtpPmChanOchLBCAve_Object = MibTableColumn
lmOchPtpPmChanOchLBCAve = _LmOchPtpPmChanOchLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 12),
    _LmOchPtpPmChanOchLBCAve_Type()
)
lmOchPtpPmChanOchLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchLBCAve.setStatus("current")
_LmOchPtpPmChanOchChromaticDispersionMin_Type = FloatHundredths
_LmOchPtpPmChanOchChromaticDispersionMin_Object = MibTableColumn
lmOchPtpPmChanOchChromaticDispersionMin = _LmOchPtpPmChanOchChromaticDispersionMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 13),
    _LmOchPtpPmChanOchChromaticDispersionMin_Type()
)
lmOchPtpPmChanOchChromaticDispersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchChromaticDispersionMin.setStatus("current")
_LmOchPtpPmChanOchChromaticDispersionMax_Type = FloatHundredths
_LmOchPtpPmChanOchChromaticDispersionMax_Object = MibTableColumn
lmOchPtpPmChanOchChromaticDispersionMax = _LmOchPtpPmChanOchChromaticDispersionMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 14),
    _LmOchPtpPmChanOchChromaticDispersionMax_Type()
)
lmOchPtpPmChanOchChromaticDispersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchChromaticDispersionMax.setStatus("current")
_LmOchPtpPmChanOchChromaticDispersionAve_Type = FloatHundredths
_LmOchPtpPmChanOchChromaticDispersionAve_Object = MibTableColumn
lmOchPtpPmChanOchChromaticDispersionAve = _LmOchPtpPmChanOchChromaticDispersionAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 15),
    _LmOchPtpPmChanOchChromaticDispersionAve_Type()
)
lmOchPtpPmChanOchChromaticDispersionAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchChromaticDispersionAve.setStatus("current")
_LmOchPtpPmChanOchQMin_Type = FloatHundredths
_LmOchPtpPmChanOchQMin_Object = MibTableColumn
lmOchPtpPmChanOchQMin = _LmOchPtpPmChanOchQMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 16),
    _LmOchPtpPmChanOchQMin_Type()
)
lmOchPtpPmChanOchQMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchQMin.setStatus("current")
_LmOchPtpPmChanOchQMax_Type = FloatHundredths
_LmOchPtpPmChanOchQMax_Object = MibTableColumn
lmOchPtpPmChanOchQMax = _LmOchPtpPmChanOchQMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 17),
    _LmOchPtpPmChanOchQMax_Type()
)
lmOchPtpPmChanOchQMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchQMax.setStatus("current")
_LmOchPtpPmChanOchQAve_Type = FloatHundredths
_LmOchPtpPmChanOchQAve_Object = MibTableColumn
lmOchPtpPmChanOchQAve = _LmOchPtpPmChanOchQAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 18),
    _LmOchPtpPmChanOchQAve_Type()
)
lmOchPtpPmChanOchQAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchQAve.setStatus("current")
_LmOchPtpPmChanOchPmdMin_Type = FloatArbitraryPrecision
_LmOchPtpPmChanOchPmdMin_Object = MibTableColumn
lmOchPtpPmChanOchPmdMin = _LmOchPtpPmChanOchPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 19),
    _LmOchPtpPmChanOchPmdMin_Type()
)
lmOchPtpPmChanOchPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchPmdMin.setStatus("current")
_LmOchPtpPmChanOchPmdMax_Type = FloatArbitraryPrecision
_LmOchPtpPmChanOchPmdMax_Object = MibTableColumn
lmOchPtpPmChanOchPmdMax = _LmOchPtpPmChanOchPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 20),
    _LmOchPtpPmChanOchPmdMax_Type()
)
lmOchPtpPmChanOchPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchPmdMax.setStatus("current")
_LmOchPtpPmChanOchPmdAve_Type = FloatArbitraryPrecision
_LmOchPtpPmChanOchPmdAve_Object = MibTableColumn
lmOchPtpPmChanOchPmdAve = _LmOchPtpPmChanOchPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 21),
    _LmOchPtpPmChanOchPmdAve_Type()
)
lmOchPtpPmChanOchPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchPmdAve.setStatus("current")
_LmOchPtpPmChanOchSoPmdMin_Type = FloatArbitraryPrecision
_LmOchPtpPmChanOchSoPmdMin_Object = MibTableColumn
lmOchPtpPmChanOchSoPmdMin = _LmOchPtpPmChanOchSoPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 22),
    _LmOchPtpPmChanOchSoPmdMin_Type()
)
lmOchPtpPmChanOchSoPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchSoPmdMin.setStatus("current")
_LmOchPtpPmChanOchSoPmdMax_Type = FloatArbitraryPrecision
_LmOchPtpPmChanOchSoPmdMax_Object = MibTableColumn
lmOchPtpPmChanOchSoPmdMax = _LmOchPtpPmChanOchSoPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 23),
    _LmOchPtpPmChanOchSoPmdMax_Type()
)
lmOchPtpPmChanOchSoPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchSoPmdMax.setStatus("current")
_LmOchPtpPmChanOchSoPmdAve_Type = FloatArbitraryPrecision
_LmOchPtpPmChanOchSoPmdAve_Object = MibTableColumn
lmOchPtpPmChanOchSoPmdAve = _LmOchPtpPmChanOchSoPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 2, 1, 24),
    _LmOchPtpPmChanOchSoPmdAve_Type()
)
lmOchPtpPmChanOchSoPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lmOchPtpPmChanOchSoPmdAve.setStatus("current")
_LmOchPtpPmConformance_ObjectIdentity = ObjectIdentity
lmOchPtpPmConformance = _LmOchPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3)
)
_LmOchPtpPmCompliances_ObjectIdentity = ObjectIdentity
lmOchPtpPmCompliances = _LmOchPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3, 1)
)
_LmOchPtpPmGroups_ObjectIdentity = ObjectIdentity
lmOchPtpPmGroups = _LmOchPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3, 2)
)

# Managed Objects groups

lmOchPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3, 2, 1)
)
lmOchPtpPmGroup.setObjects(
      *(("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmValidity"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchOptMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchOptMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchOptAve"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchOprMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchOprMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchOprAve"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchLBCMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchLBCMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchLBCAve"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchChromaticDispersionMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchChromaticDispersionMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchChromaticDispersionAve"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchQMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchQMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchQAve"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchPmdMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchPmdMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchPmdAve"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchSoPmdMin"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchSoPmdMax"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmChanOchSoPmdAve"))
)
if mibBuilder.loadTexts:
    lmOchPtpPmGroup.setStatus("current")

lmOchPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3, 2, 2)
)
lmOchPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchOpt"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchOpr"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchLBC"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchChromaticDispersion"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchQ"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchPmd"),
        ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealChanOchSoPmd"))
)
if mibBuilder.loadTexts:
    lmOchPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lmOchPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3, 1, 1)
)
lmOchPtpPmCompliance.setObjects(
    ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmGroup")
)
if mibBuilder.loadTexts:
    lmOchPtpPmCompliance.setStatus(
        "current"
    )

lmOchPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 24, 3, 1, 2)
)
lmOchPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-LMOCHPTP-MIB", "lmOchPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    lmOchPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-LMOCHPTP-MIB",
    **{"lmOchPtpPmMIB": lmOchPtpPmMIB,
       "lmOchPtpPmRealTable": lmOchPtpPmRealTable,
       "lmOchPtpPmRealEntry": lmOchPtpPmRealEntry,
       "lmOchPtpPmRealChanOchOpt": lmOchPtpPmRealChanOchOpt,
       "lmOchPtpPmRealChanOchOpr": lmOchPtpPmRealChanOchOpr,
       "lmOchPtpPmRealChanOchLBC": lmOchPtpPmRealChanOchLBC,
       "lmOchPtpPmRealChanOchChromaticDispersion": lmOchPtpPmRealChanOchChromaticDispersion,
       "lmOchPtpPmRealChanOchQ": lmOchPtpPmRealChanOchQ,
       "lmOchPtpPmRealChanOchPmd": lmOchPtpPmRealChanOchPmd,
       "lmOchPtpPmRealChanOchSoPmd": lmOchPtpPmRealChanOchSoPmd,
       "lmOchPtpPmTable": lmOchPtpPmTable,
       "lmOchPtpPmEntry": lmOchPtpPmEntry,
       "lmOchPtpPmTimestamp": lmOchPtpPmTimestamp,
       "lmOchPtpPmSampleDuration": lmOchPtpPmSampleDuration,
       "lmOchPtpPmValidity": lmOchPtpPmValidity,
       "lmOchPtpPmChanOchOptMin": lmOchPtpPmChanOchOptMin,
       "lmOchPtpPmChanOchOptMax": lmOchPtpPmChanOchOptMax,
       "lmOchPtpPmChanOchOptAve": lmOchPtpPmChanOchOptAve,
       "lmOchPtpPmChanOchOprMin": lmOchPtpPmChanOchOprMin,
       "lmOchPtpPmChanOchOprMax": lmOchPtpPmChanOchOprMax,
       "lmOchPtpPmChanOchOprAve": lmOchPtpPmChanOchOprAve,
       "lmOchPtpPmChanOchLBCMin": lmOchPtpPmChanOchLBCMin,
       "lmOchPtpPmChanOchLBCMax": lmOchPtpPmChanOchLBCMax,
       "lmOchPtpPmChanOchLBCAve": lmOchPtpPmChanOchLBCAve,
       "lmOchPtpPmChanOchChromaticDispersionMin": lmOchPtpPmChanOchChromaticDispersionMin,
       "lmOchPtpPmChanOchChromaticDispersionMax": lmOchPtpPmChanOchChromaticDispersionMax,
       "lmOchPtpPmChanOchChromaticDispersionAve": lmOchPtpPmChanOchChromaticDispersionAve,
       "lmOchPtpPmChanOchQMin": lmOchPtpPmChanOchQMin,
       "lmOchPtpPmChanOchQMax": lmOchPtpPmChanOchQMax,
       "lmOchPtpPmChanOchQAve": lmOchPtpPmChanOchQAve,
       "lmOchPtpPmChanOchPmdMin": lmOchPtpPmChanOchPmdMin,
       "lmOchPtpPmChanOchPmdMax": lmOchPtpPmChanOchPmdMax,
       "lmOchPtpPmChanOchPmdAve": lmOchPtpPmChanOchPmdAve,
       "lmOchPtpPmChanOchSoPmdMin": lmOchPtpPmChanOchSoPmdMin,
       "lmOchPtpPmChanOchSoPmdMax": lmOchPtpPmChanOchSoPmdMax,
       "lmOchPtpPmChanOchSoPmdAve": lmOchPtpPmChanOchSoPmdAve,
       "lmOchPtpPmConformance": lmOchPtpPmConformance,
       "lmOchPtpPmCompliances": lmOchPtpPmCompliances,
       "lmOchPtpPmCompliance": lmOchPtpPmCompliance,
       "lmOchPtpPmRealCompliance": lmOchPtpPmRealCompliance,
       "lmOchPtpPmGroups": lmOchPtpPmGroups,
       "lmOchPtpPmGroup": lmOchPtpPmGroup,
       "lmOchPtpPmRealGroup": lmOchPtpPmRealGroup}
)
