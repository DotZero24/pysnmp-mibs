# SNMP MIB module (INFINERA-PM-BANDCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-BANDCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:20 2025
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

(FloatHundredths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
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

bandCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    bandCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BandCtpPmRealTable_Object = MibTable
bandCtpPmRealTable = _BandCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bandCtpPmRealTable.setStatus("current")
_BandCtpPmRealEntry_Object = MibTableRow
bandCtpPmRealEntry = _BandCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1)
)
bandCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bandCtpPmRealEntry.setStatus("current")
_BandCtpPmRealOchSpanLoss_Type = FloatHundredths
_BandCtpPmRealOchSpanLoss_Object = MibTableColumn
bandCtpPmRealOchSpanLoss = _BandCtpPmRealOchSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 1),
    _BandCtpPmRealOchSpanLoss_Type()
)
bandCtpPmRealOchSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealOchSpanLoss.setStatus("current")
_BandCtpPmRealNetSpanLoss_Type = FloatHundredths
_BandCtpPmRealNetSpanLoss_Object = MibTableColumn
bandCtpPmRealNetSpanLoss = _BandCtpPmRealNetSpanLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 2),
    _BandCtpPmRealNetSpanLoss_Type()
)
bandCtpPmRealNetSpanLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealNetSpanLoss.setStatus("current")
_BandCtpPmRealBandOpr_Type = FloatHundredths
_BandCtpPmRealBandOpr_Object = MibTableColumn
bandCtpPmRealBandOpr = _BandCtpPmRealBandOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 3),
    _BandCtpPmRealBandOpr_Type()
)
bandCtpPmRealBandOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBandOpr.setStatus("current")
_BandCtpPmRealBandOchOpr_Type = FloatHundredths
_BandCtpPmRealBandOchOpr_Object = MibTableColumn
bandCtpPmRealBandOchOpr = _BandCtpPmRealBandOchOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 4),
    _BandCtpPmRealBandOchOpr_Type()
)
bandCtpPmRealBandOchOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBandOchOpr.setStatus("current")
_BandCtpPmRealBandOprNum_Type = FloatHundredths
_BandCtpPmRealBandOprNum_Object = MibTableColumn
bandCtpPmRealBandOprNum = _BandCtpPmRealBandOprNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 5),
    _BandCtpPmRealBandOprNum_Type()
)
bandCtpPmRealBandOprNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBandOprNum.setStatus("current")
_BandCtpPmRealOamBandTxEdfaLbc1_Type = FloatHundredths
_BandCtpPmRealOamBandTxEdfaLbc1_Object = MibTableColumn
bandCtpPmRealOamBandTxEdfaLbc1 = _BandCtpPmRealOamBandTxEdfaLbc1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 6),
    _BandCtpPmRealOamBandTxEdfaLbc1_Type()
)
bandCtpPmRealOamBandTxEdfaLbc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealOamBandTxEdfaLbc1.setStatus("current")
_BandCtpPmRealOamBandTxEdfaLbc2_Type = FloatHundredths
_BandCtpPmRealOamBandTxEdfaLbc2_Object = MibTableColumn
bandCtpPmRealOamBandTxEdfaLbc2 = _BandCtpPmRealOamBandTxEdfaLbc2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 7),
    _BandCtpPmRealOamBandTxEdfaLbc2_Type()
)
bandCtpPmRealOamBandTxEdfaLbc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealOamBandTxEdfaLbc2.setStatus("current")
_BandCtpPmRealBmmBandEdfaLbcTx_Type = FloatHundredths
_BandCtpPmRealBmmBandEdfaLbcTx_Object = MibTableColumn
bandCtpPmRealBmmBandEdfaLbcTx = _BandCtpPmRealBmmBandEdfaLbcTx_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 8),
    _BandCtpPmRealBmmBandEdfaLbcTx_Type()
)
bandCtpPmRealBmmBandEdfaLbcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBmmBandEdfaLbcTx.setStatus("current")
_BandCtpPmRealBandOptTx_Type = FloatHundredths
_BandCtpPmRealBandOptTx_Object = MibTableColumn
bandCtpPmRealBandOptTx = _BandCtpPmRealBandOptTx_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 9),
    _BandCtpPmRealBandOptTx_Type()
)
bandCtpPmRealBandOptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBandOptTx.setStatus("current")
_BandCtpPmRealBandOchOpt_Type = FloatHundredths
_BandCtpPmRealBandOchOpt_Object = MibTableColumn
bandCtpPmRealBandOchOpt = _BandCtpPmRealBandOchOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 10),
    _BandCtpPmRealBandOchOpt_Type()
)
bandCtpPmRealBandOchOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBandOchOpt.setStatus("current")
_BandCtpPmRealBandOptNum_Type = FloatHundredths
_BandCtpPmRealBandOptNum_Object = MibTableColumn
bandCtpPmRealBandOptNum = _BandCtpPmRealBandOptNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 11),
    _BandCtpPmRealBandOptNum_Type()
)
bandCtpPmRealBandOptNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBandOptNum.setStatus("current")
_BandCtpPmRealBmmEdfaLbc1_Type = FloatHundredths
_BandCtpPmRealBmmEdfaLbc1_Object = MibTableColumn
bandCtpPmRealBmmEdfaLbc1 = _BandCtpPmRealBmmEdfaLbc1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 12),
    _BandCtpPmRealBmmEdfaLbc1_Type()
)
bandCtpPmRealBmmEdfaLbc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBmmEdfaLbc1.setStatus("current")
_BandCtpPmRealBmmEdfaLbc2_Type = FloatHundredths
_BandCtpPmRealBmmEdfaLbc2_Object = MibTableColumn
bandCtpPmRealBmmEdfaLbc2 = _BandCtpPmRealBmmEdfaLbc2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 13),
    _BandCtpPmRealBmmEdfaLbc2_Type()
)
bandCtpPmRealBmmEdfaLbc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBmmEdfaLbc2.setStatus("current")
_BandCtpPmRealBmmPostEdfa_Type = FloatHundredths
_BandCtpPmRealBmmPostEdfa_Object = MibTableColumn
bandCtpPmRealBmmPostEdfa = _BandCtpPmRealBmmPostEdfa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 14),
    _BandCtpPmRealBmmPostEdfa_Type()
)
bandCtpPmRealBmmPostEdfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealBmmPostEdfa.setStatus("current")
_BandCtpPmRealDampUpdateTS_Type = DisplayString
_BandCtpPmRealDampUpdateTS_Object = MibTableColumn
bandCtpPmRealDampUpdateTS = _BandCtpPmRealDampUpdateTS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 15),
    _BandCtpPmRealDampUpdateTS_Type()
)
bandCtpPmRealDampUpdateTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealDampUpdateTS.setStatus("current")
_BandCtpPmRealOprQ_Type = DisplayString
_BandCtpPmRealOprQ_Object = MibTableColumn
bandCtpPmRealOprQ = _BandCtpPmRealOprQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 16),
    _BandCtpPmRealOprQ_Type()
)
bandCtpPmRealOprQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealOprQ.setStatus("current")
_BandCtpPmRealPostOsaTapRatio_Type = FloatHundredths
_BandCtpPmRealPostOsaTapRatio_Object = MibTableColumn
bandCtpPmRealPostOsaTapRatio = _BandCtpPmRealPostOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 17),
    _BandCtpPmRealPostOsaTapRatio_Type()
)
bandCtpPmRealPostOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealPostOsaTapRatio.setStatus("current")
_BandCtpPmRealTxEdfaOpr_Type = FloatHundredths
_BandCtpPmRealTxEdfaOpr_Object = MibTableColumn
bandCtpPmRealTxEdfaOpr = _BandCtpPmRealTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 18),
    _BandCtpPmRealTxEdfaOpr_Type()
)
bandCtpPmRealTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealTxEdfaOpr.setStatus("current")
_BandCtpPmRealRxEdfaOpt_Type = FloatHundredths
_BandCtpPmRealRxEdfaOpt_Object = MibTableColumn
bandCtpPmRealRxEdfaOpt = _BandCtpPmRealRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 19),
    _BandCtpPmRealRxEdfaOpt_Type()
)
bandCtpPmRealRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealRxEdfaOpt.setStatus("current")
_BandCtpPmRealOptOsaTapRatio_Type = FloatHundredths
_BandCtpPmRealOptOsaTapRatio_Object = MibTableColumn
bandCtpPmRealOptOsaTapRatio = _BandCtpPmRealOptOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 1, 1, 20),
    _BandCtpPmRealOptOsaTapRatio_Type()
)
bandCtpPmRealOptOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRealOptOsaTapRatio.setStatus("current")
_BandCtpPmTable_Object = MibTable
bandCtpPmTable = _BandCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2)
)
if mibBuilder.loadTexts:
    bandCtpPmTable.setStatus("current")
_BandCtpPmEntry_Object = MibTableRow
bandCtpPmEntry = _BandCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1)
)
bandCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-BANDCTP-MIB", "bandCtpPmSampleDuration"),
    (0, "INFINERA-PM-BANDCTP-MIB", "bandCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    bandCtpPmEntry.setStatus("current")


class _BandCtpPmTimestamp_Type(Integer32):
    """Custom type bandCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandCtpPmTimestamp_Type.__name__ = "Integer32"
_BandCtpPmTimestamp_Object = MibTableColumn
bandCtpPmTimestamp = _BandCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 1),
    _BandCtpPmTimestamp_Type()
)
bandCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bandCtpPmTimestamp.setStatus("current")


class _BandCtpPmSampleDuration_Type(Integer32):
    """Custom type bandCtpPmSampleDuration based on Integer32"""
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


_BandCtpPmSampleDuration_Type.__name__ = "Integer32"
_BandCtpPmSampleDuration_Object = MibTableColumn
bandCtpPmSampleDuration = _BandCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 2),
    _BandCtpPmSampleDuration_Type()
)
bandCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bandCtpPmSampleDuration.setStatus("current")
_BandCtpPmValidity_Type = TruthValue
_BandCtpPmValidity_Object = MibTableColumn
bandCtpPmValidity = _BandCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 3),
    _BandCtpPmValidity_Type()
)
bandCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmValidity.setStatus("current")
_BandCtpPmOchSpanLossMin_Type = FloatHundredths
_BandCtpPmOchSpanLossMin_Object = MibTableColumn
bandCtpPmOchSpanLossMin = _BandCtpPmOchSpanLossMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 4),
    _BandCtpPmOchSpanLossMin_Type()
)
bandCtpPmOchSpanLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmOchSpanLossMin.setStatus("current")
_BandCtpPmOchSpanLossMax_Type = FloatHundredths
_BandCtpPmOchSpanLossMax_Object = MibTableColumn
bandCtpPmOchSpanLossMax = _BandCtpPmOchSpanLossMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 5),
    _BandCtpPmOchSpanLossMax_Type()
)
bandCtpPmOchSpanLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmOchSpanLossMax.setStatus("current")
_BandCtpPmOchSpanLossAve_Type = FloatHundredths
_BandCtpPmOchSpanLossAve_Object = MibTableColumn
bandCtpPmOchSpanLossAve = _BandCtpPmOchSpanLossAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 6),
    _BandCtpPmOchSpanLossAve_Type()
)
bandCtpPmOchSpanLossAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmOchSpanLossAve.setStatus("current")
_BandCtpPmNetSpanLossMin_Type = FloatHundredths
_BandCtpPmNetSpanLossMin_Object = MibTableColumn
bandCtpPmNetSpanLossMin = _BandCtpPmNetSpanLossMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 7),
    _BandCtpPmNetSpanLossMin_Type()
)
bandCtpPmNetSpanLossMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmNetSpanLossMin.setStatus("current")
_BandCtpPmNetSpanLossMax_Type = FloatHundredths
_BandCtpPmNetSpanLossMax_Object = MibTableColumn
bandCtpPmNetSpanLossMax = _BandCtpPmNetSpanLossMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 8),
    _BandCtpPmNetSpanLossMax_Type()
)
bandCtpPmNetSpanLossMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmNetSpanLossMax.setStatus("current")
_BandCtpPmNetSpanLossAve_Type = FloatHundredths
_BandCtpPmNetSpanLossAve_Object = MibTableColumn
bandCtpPmNetSpanLossAve = _BandCtpPmNetSpanLossAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 9),
    _BandCtpPmNetSpanLossAve_Type()
)
bandCtpPmNetSpanLossAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmNetSpanLossAve.setStatus("current")
_BandCtpPmBandOprMin_Type = FloatHundredths
_BandCtpPmBandOprMin_Object = MibTableColumn
bandCtpPmBandOprMin = _BandCtpPmBandOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 10),
    _BandCtpPmBandOprMin_Type()
)
bandCtpPmBandOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBandOprMin.setStatus("current")
_BandCtpPmBandOprMax_Type = FloatHundredths
_BandCtpPmBandOprMax_Object = MibTableColumn
bandCtpPmBandOprMax = _BandCtpPmBandOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 11),
    _BandCtpPmBandOprMax_Type()
)
bandCtpPmBandOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBandOprMax.setStatus("current")
_BandCtpPmBandOprAve_Type = FloatHundredths
_BandCtpPmBandOprAve_Object = MibTableColumn
bandCtpPmBandOprAve = _BandCtpPmBandOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 12),
    _BandCtpPmBandOprAve_Type()
)
bandCtpPmBandOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBandOprAve.setStatus("current")
_BandCtpPmBandOptMin_Type = FloatHundredths
_BandCtpPmBandOptMin_Object = MibTableColumn
bandCtpPmBandOptMin = _BandCtpPmBandOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 13),
    _BandCtpPmBandOptMin_Type()
)
bandCtpPmBandOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBandOptMin.setStatus("current")
_BandCtpPmBandOptMax_Type = FloatHundredths
_BandCtpPmBandOptMax_Object = MibTableColumn
bandCtpPmBandOptMax = _BandCtpPmBandOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 14),
    _BandCtpPmBandOptMax_Type()
)
bandCtpPmBandOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBandOptMax.setStatus("current")
_BandCtpPmBandOptAve_Type = FloatHundredths
_BandCtpPmBandOptAve_Object = MibTableColumn
bandCtpPmBandOptAve = _BandCtpPmBandOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 15),
    _BandCtpPmBandOptAve_Type()
)
bandCtpPmBandOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBandOptAve.setStatus("current")
_BandCtpPmBmmPostEdfaMin_Type = FloatHundredths
_BandCtpPmBmmPostEdfaMin_Object = MibTableColumn
bandCtpPmBmmPostEdfaMin = _BandCtpPmBmmPostEdfaMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 16),
    _BandCtpPmBmmPostEdfaMin_Type()
)
bandCtpPmBmmPostEdfaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBmmPostEdfaMin.setStatus("current")
_BandCtpPmBmmPostEdfaMax_Type = FloatHundredths
_BandCtpPmBmmPostEdfaMax_Object = MibTableColumn
bandCtpPmBmmPostEdfaMax = _BandCtpPmBmmPostEdfaMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 17),
    _BandCtpPmBmmPostEdfaMax_Type()
)
bandCtpPmBmmPostEdfaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBmmPostEdfaMax.setStatus("current")
_BandCtpPmBmmPostEdfaAve_Type = FloatHundredths
_BandCtpPmBmmPostEdfaAve_Object = MibTableColumn
bandCtpPmBmmPostEdfaAve = _BandCtpPmBmmPostEdfaAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 18),
    _BandCtpPmBmmPostEdfaAve_Type()
)
bandCtpPmBmmPostEdfaAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmBmmPostEdfaAve.setStatus("current")
_BandCtpPmTxEdfaOprMin_Type = FloatHundredths
_BandCtpPmTxEdfaOprMin_Object = MibTableColumn
bandCtpPmTxEdfaOprMin = _BandCtpPmTxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 19),
    _BandCtpPmTxEdfaOprMin_Type()
)
bandCtpPmTxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmTxEdfaOprMin.setStatus("current")
_BandCtpPmTxEdfaOprMax_Type = FloatHundredths
_BandCtpPmTxEdfaOprMax_Object = MibTableColumn
bandCtpPmTxEdfaOprMax = _BandCtpPmTxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 20),
    _BandCtpPmTxEdfaOprMax_Type()
)
bandCtpPmTxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmTxEdfaOprMax.setStatus("current")
_BandCtpPmTxEdfaOprAve_Type = FloatHundredths
_BandCtpPmTxEdfaOprAve_Object = MibTableColumn
bandCtpPmTxEdfaOprAve = _BandCtpPmTxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 21),
    _BandCtpPmTxEdfaOprAve_Type()
)
bandCtpPmTxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmTxEdfaOprAve.setStatus("current")
_BandCtpPmRxEdfaOptMin_Type = FloatHundredths
_BandCtpPmRxEdfaOptMin_Object = MibTableColumn
bandCtpPmRxEdfaOptMin = _BandCtpPmRxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 22),
    _BandCtpPmRxEdfaOptMin_Type()
)
bandCtpPmRxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRxEdfaOptMin.setStatus("current")
_BandCtpPmRxEdfaOptMax_Type = FloatHundredths
_BandCtpPmRxEdfaOptMax_Object = MibTableColumn
bandCtpPmRxEdfaOptMax = _BandCtpPmRxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 23),
    _BandCtpPmRxEdfaOptMax_Type()
)
bandCtpPmRxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRxEdfaOptMax.setStatus("current")
_BandCtpPmRxEdfaOptAve_Type = FloatHundredths
_BandCtpPmRxEdfaOptAve_Object = MibTableColumn
bandCtpPmRxEdfaOptAve = _BandCtpPmRxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 24),
    _BandCtpPmRxEdfaOptAve_Type()
)
bandCtpPmRxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmRxEdfaOptAve.setStatus("current")
_BandCtpPmOptOsaTapRatioMin_Type = FloatHundredths
_BandCtpPmOptOsaTapRatioMin_Object = MibTableColumn
bandCtpPmOptOsaTapRatioMin = _BandCtpPmOptOsaTapRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 25),
    _BandCtpPmOptOsaTapRatioMin_Type()
)
bandCtpPmOptOsaTapRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmOptOsaTapRatioMin.setStatus("current")
_BandCtpPmOptOsaTapRatioMax_Type = FloatHundredths
_BandCtpPmOptOsaTapRatioMax_Object = MibTableColumn
bandCtpPmOptOsaTapRatioMax = _BandCtpPmOptOsaTapRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 26),
    _BandCtpPmOptOsaTapRatioMax_Type()
)
bandCtpPmOptOsaTapRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmOptOsaTapRatioMax.setStatus("current")
_BandCtpPmOptOsaTapRatioAve_Type = FloatHundredths
_BandCtpPmOptOsaTapRatioAve_Object = MibTableColumn
bandCtpPmOptOsaTapRatioAve = _BandCtpPmOptOsaTapRatioAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 2, 1, 27),
    _BandCtpPmOptOsaTapRatioAve_Type()
)
bandCtpPmOptOsaTapRatioAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandCtpPmOptOsaTapRatioAve.setStatus("current")
_BandCtpPmConformance_ObjectIdentity = ObjectIdentity
bandCtpPmConformance = _BandCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3)
)
_BandCtpPmCompliances_ObjectIdentity = ObjectIdentity
bandCtpPmCompliances = _BandCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3, 1)
)
_BandCtpPmGroups_ObjectIdentity = ObjectIdentity
bandCtpPmGroups = _BandCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3, 2)
)

# Managed Objects groups

bandCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3, 2, 1)
)
bandCtpPmGroup.setObjects(
      *(("INFINERA-PM-BANDCTP-MIB", "bandCtpPmValidity"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmOchSpanLossMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmOchSpanLossMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmOchSpanLossAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmNetSpanLossMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmNetSpanLossMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmNetSpanLossAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBandOprMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBandOprMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBandOprAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBandOptMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBandOptMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBandOptAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBmmPostEdfaMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBmmPostEdfaMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmBmmPostEdfaAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmTxEdfaOprMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmTxEdfaOprMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmTxEdfaOprAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRxEdfaOptMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRxEdfaOptMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRxEdfaOptAve"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmOptOsaTapRatioMin"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmOptOsaTapRatioMax"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmOptOsaTapRatioAve"))
)
if mibBuilder.loadTexts:
    bandCtpPmGroup.setStatus("current")

bandCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3, 2, 2)
)
bandCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealOchSpanLoss"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealNetSpanLoss"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBandOpr"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBandOchOpr"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBandOprNum"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealOamBandTxEdfaLbc1"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealOamBandTxEdfaLbc2"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBmmBandEdfaLbcTx"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBandOptTx"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBandOchOpt"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBandOptNum"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBmmEdfaLbc1"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBmmEdfaLbc2"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealBmmPostEdfa"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealDampUpdateTS"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealOprQ"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealPostOsaTapRatio"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealTxEdfaOpr"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealRxEdfaOpt"),
        ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealOptOsaTapRatio"))
)
if mibBuilder.loadTexts:
    bandCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bandCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3, 1, 1)
)
bandCtpPmCompliance.setObjects(
    ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmGroup")
)
if mibBuilder.loadTexts:
    bandCtpPmCompliance.setStatus(
        "current"
    )

bandCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 1, 3, 1, 2)
)
bandCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-BANDCTP-MIB", "bandCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    bandCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-BANDCTP-MIB",
    **{"bandCtpPmMIB": bandCtpPmMIB,
       "bandCtpPmRealTable": bandCtpPmRealTable,
       "bandCtpPmRealEntry": bandCtpPmRealEntry,
       "bandCtpPmRealOchSpanLoss": bandCtpPmRealOchSpanLoss,
       "bandCtpPmRealNetSpanLoss": bandCtpPmRealNetSpanLoss,
       "bandCtpPmRealBandOpr": bandCtpPmRealBandOpr,
       "bandCtpPmRealBandOchOpr": bandCtpPmRealBandOchOpr,
       "bandCtpPmRealBandOprNum": bandCtpPmRealBandOprNum,
       "bandCtpPmRealOamBandTxEdfaLbc1": bandCtpPmRealOamBandTxEdfaLbc1,
       "bandCtpPmRealOamBandTxEdfaLbc2": bandCtpPmRealOamBandTxEdfaLbc2,
       "bandCtpPmRealBmmBandEdfaLbcTx": bandCtpPmRealBmmBandEdfaLbcTx,
       "bandCtpPmRealBandOptTx": bandCtpPmRealBandOptTx,
       "bandCtpPmRealBandOchOpt": bandCtpPmRealBandOchOpt,
       "bandCtpPmRealBandOptNum": bandCtpPmRealBandOptNum,
       "bandCtpPmRealBmmEdfaLbc1": bandCtpPmRealBmmEdfaLbc1,
       "bandCtpPmRealBmmEdfaLbc2": bandCtpPmRealBmmEdfaLbc2,
       "bandCtpPmRealBmmPostEdfa": bandCtpPmRealBmmPostEdfa,
       "bandCtpPmRealDampUpdateTS": bandCtpPmRealDampUpdateTS,
       "bandCtpPmRealOprQ": bandCtpPmRealOprQ,
       "bandCtpPmRealPostOsaTapRatio": bandCtpPmRealPostOsaTapRatio,
       "bandCtpPmRealTxEdfaOpr": bandCtpPmRealTxEdfaOpr,
       "bandCtpPmRealRxEdfaOpt": bandCtpPmRealRxEdfaOpt,
       "bandCtpPmRealOptOsaTapRatio": bandCtpPmRealOptOsaTapRatio,
       "bandCtpPmTable": bandCtpPmTable,
       "bandCtpPmEntry": bandCtpPmEntry,
       "bandCtpPmTimestamp": bandCtpPmTimestamp,
       "bandCtpPmSampleDuration": bandCtpPmSampleDuration,
       "bandCtpPmValidity": bandCtpPmValidity,
       "bandCtpPmOchSpanLossMin": bandCtpPmOchSpanLossMin,
       "bandCtpPmOchSpanLossMax": bandCtpPmOchSpanLossMax,
       "bandCtpPmOchSpanLossAve": bandCtpPmOchSpanLossAve,
       "bandCtpPmNetSpanLossMin": bandCtpPmNetSpanLossMin,
       "bandCtpPmNetSpanLossMax": bandCtpPmNetSpanLossMax,
       "bandCtpPmNetSpanLossAve": bandCtpPmNetSpanLossAve,
       "bandCtpPmBandOprMin": bandCtpPmBandOprMin,
       "bandCtpPmBandOprMax": bandCtpPmBandOprMax,
       "bandCtpPmBandOprAve": bandCtpPmBandOprAve,
       "bandCtpPmBandOptMin": bandCtpPmBandOptMin,
       "bandCtpPmBandOptMax": bandCtpPmBandOptMax,
       "bandCtpPmBandOptAve": bandCtpPmBandOptAve,
       "bandCtpPmBmmPostEdfaMin": bandCtpPmBmmPostEdfaMin,
       "bandCtpPmBmmPostEdfaMax": bandCtpPmBmmPostEdfaMax,
       "bandCtpPmBmmPostEdfaAve": bandCtpPmBmmPostEdfaAve,
       "bandCtpPmTxEdfaOprMin": bandCtpPmTxEdfaOprMin,
       "bandCtpPmTxEdfaOprMax": bandCtpPmTxEdfaOprMax,
       "bandCtpPmTxEdfaOprAve": bandCtpPmTxEdfaOprAve,
       "bandCtpPmRxEdfaOptMin": bandCtpPmRxEdfaOptMin,
       "bandCtpPmRxEdfaOptMax": bandCtpPmRxEdfaOptMax,
       "bandCtpPmRxEdfaOptAve": bandCtpPmRxEdfaOptAve,
       "bandCtpPmOptOsaTapRatioMin": bandCtpPmOptOsaTapRatioMin,
       "bandCtpPmOptOsaTapRatioMax": bandCtpPmOptOsaTapRatioMax,
       "bandCtpPmOptOsaTapRatioAve": bandCtpPmOptOsaTapRatioAve,
       "bandCtpPmConformance": bandCtpPmConformance,
       "bandCtpPmCompliances": bandCtpPmCompliances,
       "bandCtpPmCompliance": bandCtpPmCompliance,
       "bandCtpPmRealCompliance": bandCtpPmRealCompliance,
       "bandCtpPmGroups": bandCtpPmGroups,
       "bandCtpPmGroup": bandCtpPmGroup,
       "bandCtpPmRealGroup": bandCtpPmRealGroup}
)
