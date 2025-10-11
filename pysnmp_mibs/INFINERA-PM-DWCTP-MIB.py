# SNMP MIB module (INFINERA-PM-DWCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-DWCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:11 2025
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

(FloatArbitraryPrecision,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision")

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

dwCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47)
)
if mibBuilder.loadTexts:
    dwCtpPmMIB.setRevisions(
        ("2017-01-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DwCtpPmRealTable_Object = MibTable
dwCtpPmRealTable = _DwCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1)
)
if mibBuilder.loadTexts:
    dwCtpPmRealTable.setStatus("current")
_DwCtpPmRealEntry_Object = MibTableRow
dwCtpPmRealEntry = _DwCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1)
)
dwCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dwCtpPmRealEntry.setStatus("current")
_DwCtpPmRealFecCodeWords_Type = Counter64
_DwCtpPmRealFecCodeWords_Object = MibTableColumn
dwCtpPmRealFecCodeWords = _DwCtpPmRealFecCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 1),
    _DwCtpPmRealFecCodeWords_Type()
)
dwCtpPmRealFecCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealFecCodeWords.setStatus("current")
_DwCtpPmRealFecUncorCodeWords_Type = Counter64
_DwCtpPmRealFecUncorCodeWords_Object = MibTableColumn
dwCtpPmRealFecUncorCodeWords = _DwCtpPmRealFecUncorCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 2),
    _DwCtpPmRealFecUncorCodeWords_Type()
)
dwCtpPmRealFecUncorCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealFecUncorCodeWords.setStatus("current")
_DwCtpPmRealPostFecQ_Type = FloatArbitraryPrecision
_DwCtpPmRealPostFecQ_Object = MibTableColumn
dwCtpPmRealPostFecQ = _DwCtpPmRealPostFecQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 3),
    _DwCtpPmRealPostFecQ_Type()
)
dwCtpPmRealPostFecQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealPostFecQ.setStatus("current")
_DwCtpPmRealPreFecQ_Type = FloatArbitraryPrecision
_DwCtpPmRealPreFecQ_Object = MibTableColumn
dwCtpPmRealPreFecQ = _DwCtpPmRealPreFecQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 4),
    _DwCtpPmRealPreFecQ_Type()
)
dwCtpPmRealPreFecQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealPreFecQ.setStatus("current")
_DwCtpPmRealBerPreFec_Type = FloatArbitraryPrecision
_DwCtpPmRealBerPreFec_Object = MibTableColumn
dwCtpPmRealBerPreFec = _DwCtpPmRealBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 5),
    _DwCtpPmRealBerPreFec_Type()
)
dwCtpPmRealBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealBerPreFec.setStatus("current")
_DwCtpPmRealBerPostFec_Type = FloatArbitraryPrecision
_DwCtpPmRealBerPostFec_Object = MibTableColumn
dwCtpPmRealBerPostFec = _DwCtpPmRealBerPostFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 6),
    _DwCtpPmRealBerPostFec_Type()
)
dwCtpPmRealBerPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealBerPostFec.setStatus("current")
_DwCtpPmRealUnCorrectedBits_Type = Counter64
_DwCtpPmRealUnCorrectedBits_Object = MibTableColumn
dwCtpPmRealUnCorrectedBits = _DwCtpPmRealUnCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 7),
    _DwCtpPmRealUnCorrectedBits_Type()
)
dwCtpPmRealUnCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealUnCorrectedBits.setStatus("current")
_DwCtpPmRealCorrectedBits_Type = Counter64
_DwCtpPmRealCorrectedBits_Object = MibTableColumn
dwCtpPmRealCorrectedBits = _DwCtpPmRealCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 8),
    _DwCtpPmRealCorrectedBits_Type()
)
dwCtpPmRealCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealCorrectedBits.setStatus("current")
_DwCtpPmRealPropagationDelay_Type = FloatArbitraryPrecision
_DwCtpPmRealPropagationDelay_Object = MibTableColumn
dwCtpPmRealPropagationDelay = _DwCtpPmRealPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 1, 1, 9),
    _DwCtpPmRealPropagationDelay_Type()
)
dwCtpPmRealPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmRealPropagationDelay.setStatus("current")
_DwCtpPmTable_Object = MibTable
dwCtpPmTable = _DwCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2)
)
if mibBuilder.loadTexts:
    dwCtpPmTable.setStatus("current")
_DwCtpPmEntry_Object = MibTableRow
dwCtpPmEntry = _DwCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1)
)
dwCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-DWCTP-MIB", "dwCtpPmSampleDuration"),
    (0, "INFINERA-PM-DWCTP-MIB", "dwCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    dwCtpPmEntry.setStatus("current")


class _DwCtpPmTimestamp_Type(Integer32):
    """Custom type dwCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DwCtpPmTimestamp_Type.__name__ = "Integer32"
_DwCtpPmTimestamp_Object = MibTableColumn
dwCtpPmTimestamp = _DwCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 1),
    _DwCtpPmTimestamp_Type()
)
dwCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dwCtpPmTimestamp.setStatus("current")


class _DwCtpPmSampleDuration_Type(Integer32):
    """Custom type dwCtpPmSampleDuration based on Integer32"""
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


_DwCtpPmSampleDuration_Type.__name__ = "Integer32"
_DwCtpPmSampleDuration_Object = MibTableColumn
dwCtpPmSampleDuration = _DwCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 2),
    _DwCtpPmSampleDuration_Type()
)
dwCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dwCtpPmSampleDuration.setStatus("current")
_DwCtpPmValidity_Type = TruthValue
_DwCtpPmValidity_Object = MibTableColumn
dwCtpPmValidity = _DwCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 3),
    _DwCtpPmValidity_Type()
)
dwCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmValidity.setStatus("current")
_DwCtpPmFecCodeWords_Type = Counter64
_DwCtpPmFecCodeWords_Object = MibTableColumn
dwCtpPmFecCodeWords = _DwCtpPmFecCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 4),
    _DwCtpPmFecCodeWords_Type()
)
dwCtpPmFecCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmFecCodeWords.setStatus("current")
_DwCtpPmFecUncorCodeWords_Type = Counter64
_DwCtpPmFecUncorCodeWords_Object = MibTableColumn
dwCtpPmFecUncorCodeWords = _DwCtpPmFecUncorCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 5),
    _DwCtpPmFecUncorCodeWords_Type()
)
dwCtpPmFecUncorCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmFecUncorCodeWords.setStatus("current")
_DwCtpPmPostFecQmin_Type = FloatArbitraryPrecision
_DwCtpPmPostFecQmin_Object = MibTableColumn
dwCtpPmPostFecQmin = _DwCtpPmPostFecQmin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 6),
    _DwCtpPmPostFecQmin_Type()
)
dwCtpPmPostFecQmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPostFecQmin.setStatus("current")
_DwCtpPmPostFecQmax_Type = FloatArbitraryPrecision
_DwCtpPmPostFecQmax_Object = MibTableColumn
dwCtpPmPostFecQmax = _DwCtpPmPostFecQmax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 7),
    _DwCtpPmPostFecQmax_Type()
)
dwCtpPmPostFecQmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPostFecQmax.setStatus("current")
_DwCtpPmPostFecQave_Type = FloatArbitraryPrecision
_DwCtpPmPostFecQave_Object = MibTableColumn
dwCtpPmPostFecQave = _DwCtpPmPostFecQave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 8),
    _DwCtpPmPostFecQave_Type()
)
dwCtpPmPostFecQave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPostFecQave.setStatus("current")
_DwCtpPmPreFecQMin_Type = FloatArbitraryPrecision
_DwCtpPmPreFecQMin_Object = MibTableColumn
dwCtpPmPreFecQMin = _DwCtpPmPreFecQMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 9),
    _DwCtpPmPreFecQMin_Type()
)
dwCtpPmPreFecQMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPreFecQMin.setStatus("current")
_DwCtpPmPreFecQMax_Type = FloatArbitraryPrecision
_DwCtpPmPreFecQMax_Object = MibTableColumn
dwCtpPmPreFecQMax = _DwCtpPmPreFecQMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 10),
    _DwCtpPmPreFecQMax_Type()
)
dwCtpPmPreFecQMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPreFecQMax.setStatus("current")
_DwCtpPmPreFecQAve_Type = FloatArbitraryPrecision
_DwCtpPmPreFecQAve_Object = MibTableColumn
dwCtpPmPreFecQAve = _DwCtpPmPreFecQAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 11),
    _DwCtpPmPreFecQAve_Type()
)
dwCtpPmPreFecQAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPreFecQAve.setStatus("current")
_DwCtpPmBerPreFecMin_Type = FloatArbitraryPrecision
_DwCtpPmBerPreFecMin_Object = MibTableColumn
dwCtpPmBerPreFecMin = _DwCtpPmBerPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 12),
    _DwCtpPmBerPreFecMin_Type()
)
dwCtpPmBerPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmBerPreFecMin.setStatus("current")
_DwCtpPmBerPreFecMax_Type = FloatArbitraryPrecision
_DwCtpPmBerPreFecMax_Object = MibTableColumn
dwCtpPmBerPreFecMax = _DwCtpPmBerPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 13),
    _DwCtpPmBerPreFecMax_Type()
)
dwCtpPmBerPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmBerPreFecMax.setStatus("current")
_DwCtpPmBerPreFecAve_Type = FloatArbitraryPrecision
_DwCtpPmBerPreFecAve_Object = MibTableColumn
dwCtpPmBerPreFecAve = _DwCtpPmBerPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 14),
    _DwCtpPmBerPreFecAve_Type()
)
dwCtpPmBerPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmBerPreFecAve.setStatus("current")
_DwCtpPmBerPostFecMin_Type = FloatArbitraryPrecision
_DwCtpPmBerPostFecMin_Object = MibTableColumn
dwCtpPmBerPostFecMin = _DwCtpPmBerPostFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 15),
    _DwCtpPmBerPostFecMin_Type()
)
dwCtpPmBerPostFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmBerPostFecMin.setStatus("current")
_DwCtpPmBerPostFecMax_Type = FloatArbitraryPrecision
_DwCtpPmBerPostFecMax_Object = MibTableColumn
dwCtpPmBerPostFecMax = _DwCtpPmBerPostFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 16),
    _DwCtpPmBerPostFecMax_Type()
)
dwCtpPmBerPostFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmBerPostFecMax.setStatus("current")
_DwCtpPmBerPostFecAve_Type = FloatArbitraryPrecision
_DwCtpPmBerPostFecAve_Object = MibTableColumn
dwCtpPmBerPostFecAve = _DwCtpPmBerPostFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 17),
    _DwCtpPmBerPostFecAve_Type()
)
dwCtpPmBerPostFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmBerPostFecAve.setStatus("current")
_DwCtpPmUnCorrectedBits_Type = Counter64
_DwCtpPmUnCorrectedBits_Object = MibTableColumn
dwCtpPmUnCorrectedBits = _DwCtpPmUnCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 18),
    _DwCtpPmUnCorrectedBits_Type()
)
dwCtpPmUnCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmUnCorrectedBits.setStatus("current")
_DwCtpPmCorrectedBits_Type = Counter64
_DwCtpPmCorrectedBits_Object = MibTableColumn
dwCtpPmCorrectedBits = _DwCtpPmCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 19),
    _DwCtpPmCorrectedBits_Type()
)
dwCtpPmCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmCorrectedBits.setStatus("current")
_DwCtpPmPropagationDelayMin_Type = FloatArbitraryPrecision
_DwCtpPmPropagationDelayMin_Object = MibTableColumn
dwCtpPmPropagationDelayMin = _DwCtpPmPropagationDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 20),
    _DwCtpPmPropagationDelayMin_Type()
)
dwCtpPmPropagationDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPropagationDelayMin.setStatus("current")
_DwCtpPmPropagationDelayMax_Type = FloatArbitraryPrecision
_DwCtpPmPropagationDelayMax_Object = MibTableColumn
dwCtpPmPropagationDelayMax = _DwCtpPmPropagationDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 21),
    _DwCtpPmPropagationDelayMax_Type()
)
dwCtpPmPropagationDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPropagationDelayMax.setStatus("current")
_DwCtpPmPropagationDelayAve_Type = FloatArbitraryPrecision
_DwCtpPmPropagationDelayAve_Object = MibTableColumn
dwCtpPmPropagationDelayAve = _DwCtpPmPropagationDelayAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 2, 1, 22),
    _DwCtpPmPropagationDelayAve_Type()
)
dwCtpPmPropagationDelayAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dwCtpPmPropagationDelayAve.setStatus("current")
_DwCtpPmConformance_ObjectIdentity = ObjectIdentity
dwCtpPmConformance = _DwCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3)
)
_DwCtpPmCompliances_ObjectIdentity = ObjectIdentity
dwCtpPmCompliances = _DwCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3, 1)
)
_DwCtpPmGroups_ObjectIdentity = ObjectIdentity
dwCtpPmGroups = _DwCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3, 2)
)

# Managed Objects groups

dwCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3, 2, 1)
)
dwCtpPmGroup.setObjects(
      *(("INFINERA-PM-DWCTP-MIB", "dwCtpPmFecCodeWords"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmFecUncorCodeWords"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPostFecQmin"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPostFecQmax"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPostFecQave"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPreFecQMin"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPreFecQMax"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPreFecQAve"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmBerPreFecMin"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmBerPreFecMax"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmBerPreFecAve"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmBerPostFecMin"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmBerPostFecMax"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmBerPostFecAve"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmUnCorrectedBits"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmCorrectedBits"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPropagationDelayMin"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPropagationDelayMax"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmPropagationDelayAve"))
)
if mibBuilder.loadTexts:
    dwCtpPmGroup.setStatus("current")

dwCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3, 2, 2)
)
dwCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealFecCodeWords"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealFecUncorCodeWords"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealPostFecQ"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealPreFecQ"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealBerPreFec"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealBerPostFec"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealUnCorrectedBits"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealCorrectedBits"),
        ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealPropagationDelay"))
)
if mibBuilder.loadTexts:
    dwCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dwCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3, 1, 1)
)
dwCtpPmCompliance.setObjects(
    ("INFINERA-PM-DWCTP-MIB", "dwCtpPmGroup")
)
if mibBuilder.loadTexts:
    dwCtpPmCompliance.setStatus(
        "current"
    )

dwCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 47, 3, 1, 2)
)
dwCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-DWCTP-MIB", "dwCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    dwCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-DWCTP-MIB",
    **{"dwCtpPmMIB": dwCtpPmMIB,
       "dwCtpPmRealTable": dwCtpPmRealTable,
       "dwCtpPmRealEntry": dwCtpPmRealEntry,
       "dwCtpPmRealFecCodeWords": dwCtpPmRealFecCodeWords,
       "dwCtpPmRealFecUncorCodeWords": dwCtpPmRealFecUncorCodeWords,
       "dwCtpPmRealPostFecQ": dwCtpPmRealPostFecQ,
       "dwCtpPmRealPreFecQ": dwCtpPmRealPreFecQ,
       "dwCtpPmRealBerPreFec": dwCtpPmRealBerPreFec,
       "dwCtpPmRealBerPostFec": dwCtpPmRealBerPostFec,
       "dwCtpPmRealUnCorrectedBits": dwCtpPmRealUnCorrectedBits,
       "dwCtpPmRealCorrectedBits": dwCtpPmRealCorrectedBits,
       "dwCtpPmRealPropagationDelay": dwCtpPmRealPropagationDelay,
       "dwCtpPmTable": dwCtpPmTable,
       "dwCtpPmEntry": dwCtpPmEntry,
       "dwCtpPmTimestamp": dwCtpPmTimestamp,
       "dwCtpPmSampleDuration": dwCtpPmSampleDuration,
       "dwCtpPmValidity": dwCtpPmValidity,
       "dwCtpPmFecCodeWords": dwCtpPmFecCodeWords,
       "dwCtpPmFecUncorCodeWords": dwCtpPmFecUncorCodeWords,
       "dwCtpPmPostFecQmin": dwCtpPmPostFecQmin,
       "dwCtpPmPostFecQmax": dwCtpPmPostFecQmax,
       "dwCtpPmPostFecQave": dwCtpPmPostFecQave,
       "dwCtpPmPreFecQMin": dwCtpPmPreFecQMin,
       "dwCtpPmPreFecQMax": dwCtpPmPreFecQMax,
       "dwCtpPmPreFecQAve": dwCtpPmPreFecQAve,
       "dwCtpPmBerPreFecMin": dwCtpPmBerPreFecMin,
       "dwCtpPmBerPreFecMax": dwCtpPmBerPreFecMax,
       "dwCtpPmBerPreFecAve": dwCtpPmBerPreFecAve,
       "dwCtpPmBerPostFecMin": dwCtpPmBerPostFecMin,
       "dwCtpPmBerPostFecMax": dwCtpPmBerPostFecMax,
       "dwCtpPmBerPostFecAve": dwCtpPmBerPostFecAve,
       "dwCtpPmUnCorrectedBits": dwCtpPmUnCorrectedBits,
       "dwCtpPmCorrectedBits": dwCtpPmCorrectedBits,
       "dwCtpPmPropagationDelayMin": dwCtpPmPropagationDelayMin,
       "dwCtpPmPropagationDelayMax": dwCtpPmPropagationDelayMax,
       "dwCtpPmPropagationDelayAve": dwCtpPmPropagationDelayAve,
       "dwCtpPmConformance": dwCtpPmConformance,
       "dwCtpPmCompliances": dwCtpPmCompliances,
       "dwCtpPmCompliance": dwCtpPmCompliance,
       "dwCtpPmRealCompliance": dwCtpPmRealCompliance,
       "dwCtpPmGroups": dwCtpPmGroups,
       "dwCtpPmGroup": dwCtpPmGroup,
       "dwCtpPmRealGroup": dwCtpPmRealGroup}
)
