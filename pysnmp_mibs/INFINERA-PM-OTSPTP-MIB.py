# SNMP MIB module (INFINERA-PM-OTSPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OTSPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:57 2025
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

otsPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12)
)
if mibBuilder.loadTexts:
    otsPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtsPtpPmRealTable_Object = MibTable
otsPtpPmRealTable = _OtsPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1)
)
if mibBuilder.loadTexts:
    otsPtpPmRealTable.setStatus("current")
_OtsPtpPmRealEntry_Object = MibTableRow
otsPtpPmRealEntry = _OtsPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1)
)
otsPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otsPtpPmRealEntry.setStatus("current")
_OtsPtpPmRealOtsOpt_Type = FloatHundredths
_OtsPtpPmRealOtsOpt_Object = MibTableColumn
otsPtpPmRealOtsOpt = _OtsPtpPmRealOtsOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 1),
    _OtsPtpPmRealOtsOpt_Type()
)
otsPtpPmRealOtsOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsOpt.setStatus("current")
_OtsPtpPmRealOtsOptOsaTapRatio_Type = FloatHundredths
_OtsPtpPmRealOtsOptOsaTapRatio_Object = MibTableColumn
otsPtpPmRealOtsOptOsaTapRatio = _OtsPtpPmRealOtsOptOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 2),
    _OtsPtpPmRealOtsOptOsaTapRatio_Type()
)
otsPtpPmRealOtsOptOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsOptOsaTapRatio.setStatus("current")
_OtsPtpPmRealOtsOpr_Type = FloatHundredths
_OtsPtpPmRealOtsOpr_Object = MibTableColumn
otsPtpPmRealOtsOpr = _OtsPtpPmRealOtsOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 3),
    _OtsPtpPmRealOtsOpr_Type()
)
otsPtpPmRealOtsOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsOpr.setStatus("current")
_OtsPtpPmRealOtsOprOsaTapRatio_Type = FloatHundredths
_OtsPtpPmRealOtsOprOsaTapRatio_Object = MibTableColumn
otsPtpPmRealOtsOprOsaTapRatio = _OtsPtpPmRealOtsOprOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 4),
    _OtsPtpPmRealOtsOprOsaTapRatio_Type()
)
otsPtpPmRealOtsOprOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsOprOsaTapRatio.setStatus("current")
_OtsPtpPmRealOtsLbc1_Type = FloatHundredths
_OtsPtpPmRealOtsLbc1_Object = MibTableColumn
otsPtpPmRealOtsLbc1 = _OtsPtpPmRealOtsLbc1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 5),
    _OtsPtpPmRealOtsLbc1_Type()
)
otsPtpPmRealOtsLbc1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLbc1.setStatus("current")
_OtsPtpPmRealOtsLbc2_Type = FloatHundredths
_OtsPtpPmRealOtsLbc2_Object = MibTableColumn
otsPtpPmRealOtsLbc2 = _OtsPtpPmRealOtsLbc2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 6),
    _OtsPtpPmRealOtsLbc2_Type()
)
otsPtpPmRealOtsLbc2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLbc2.setStatus("current")
_OtsPtpPmRealOtsLbc3_Type = FloatHundredths
_OtsPtpPmRealOtsLbc3_Object = MibTableColumn
otsPtpPmRealOtsLbc3 = _OtsPtpPmRealOtsLbc3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 7),
    _OtsPtpPmRealOtsLbc3_Type()
)
otsPtpPmRealOtsLbc3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLbc3.setStatus("current")
_OtsPtpPmRealOtsLbc4_Type = FloatHundredths
_OtsPtpPmRealOtsLbc4_Object = MibTableColumn
otsPtpPmRealOtsLbc4 = _OtsPtpPmRealOtsLbc4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 8),
    _OtsPtpPmRealOtsLbc4_Type()
)
otsPtpPmRealOtsLbc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLbc4.setStatus("current")
_OtsPtpPmRealOtsLpwr1_Type = FloatHundredths
_OtsPtpPmRealOtsLpwr1_Object = MibTableColumn
otsPtpPmRealOtsLpwr1 = _OtsPtpPmRealOtsLpwr1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 9),
    _OtsPtpPmRealOtsLpwr1_Type()
)
otsPtpPmRealOtsLpwr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLpwr1.setStatus("current")
_OtsPtpPmRealOtsLpwr2_Type = FloatHundredths
_OtsPtpPmRealOtsLpwr2_Object = MibTableColumn
otsPtpPmRealOtsLpwr2 = _OtsPtpPmRealOtsLpwr2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 10),
    _OtsPtpPmRealOtsLpwr2_Type()
)
otsPtpPmRealOtsLpwr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLpwr2.setStatus("current")
_OtsPtpPmRealOtsLpwr3_Type = FloatHundredths
_OtsPtpPmRealOtsLpwr3_Object = MibTableColumn
otsPtpPmRealOtsLpwr3 = _OtsPtpPmRealOtsLpwr3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 11),
    _OtsPtpPmRealOtsLpwr3_Type()
)
otsPtpPmRealOtsLpwr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLpwr3.setStatus("current")
_OtsPtpPmRealOtsLpwr4_Type = FloatHundredths
_OtsPtpPmRealOtsLpwr4_Object = MibTableColumn
otsPtpPmRealOtsLpwr4 = _OtsPtpPmRealOtsLpwr4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 12),
    _OtsPtpPmRealOtsLpwr4_Type()
)
otsPtpPmRealOtsLpwr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsLpwr4.setStatus("current")
_OtsPtpPmRealOtsAlsOpr_Type = FloatHundredths
_OtsPtpPmRealOtsAlsOpr_Object = MibTableColumn
otsPtpPmRealOtsAlsOpr = _OtsPtpPmRealOtsAlsOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 13),
    _OtsPtpPmRealOtsAlsOpr_Type()
)
otsPtpPmRealOtsAlsOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsAlsOpr.setStatus("current")
_OtsPtpPmRealOtsAlsOpt_Type = FloatHundredths
_OtsPtpPmRealOtsAlsOpt_Object = MibTableColumn
otsPtpPmRealOtsAlsOpt = _OtsPtpPmRealOtsAlsOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 14),
    _OtsPtpPmRealOtsAlsOpt_Type()
)
otsPtpPmRealOtsAlsOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsAlsOpt.setStatus("current")
_OtsPtpPmRealOtsAlsLbc_Type = FloatHundredths
_OtsPtpPmRealOtsAlsLbc_Object = MibTableColumn
otsPtpPmRealOtsAlsLbc = _OtsPtpPmRealOtsAlsLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 15),
    _OtsPtpPmRealOtsAlsLbc_Type()
)
otsPtpPmRealOtsAlsLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOtsAlsLbc.setStatus("current")
_OtsPtpPmRealRxPostEdfaOsaTapRatio_Type = FloatHundredths
_OtsPtpPmRealRxPostEdfaOsaTapRatio_Object = MibTableColumn
otsPtpPmRealRxPostEdfaOsaTapRatio = _OtsPtpPmRealRxPostEdfaOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 16),
    _OtsPtpPmRealRxPostEdfaOsaTapRatio_Type()
)
otsPtpPmRealRxPostEdfaOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealRxPostEdfaOsaTapRatio.setStatus("current")
_OtsPtpPmRealOprQ_Type = DisplayString
_OtsPtpPmRealOprQ_Object = MibTableColumn
otsPtpPmRealOprQ = _OtsPtpPmRealOprQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 1, 1, 17),
    _OtsPtpPmRealOprQ_Type()
)
otsPtpPmRealOprQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmRealOprQ.setStatus("current")
_OtsPtpPmTable_Object = MibTable
otsPtpPmTable = _OtsPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2)
)
if mibBuilder.loadTexts:
    otsPtpPmTable.setStatus("current")
_OtsPtpPmEntry_Object = MibTableRow
otsPtpPmEntry = _OtsPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1)
)
otsPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OTSPTP-MIB", "otsPtpPmSampleDuration"),
    (0, "INFINERA-PM-OTSPTP-MIB", "otsPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    otsPtpPmEntry.setStatus("current")


class _OtsPtpPmTimestamp_Type(Integer32):
    """Custom type otsPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OtsPtpPmTimestamp_Type.__name__ = "Integer32"
_OtsPtpPmTimestamp_Object = MibTableColumn
otsPtpPmTimestamp = _OtsPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 1),
    _OtsPtpPmTimestamp_Type()
)
otsPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otsPtpPmTimestamp.setStatus("current")


class _OtsPtpPmSampleDuration_Type(Integer32):
    """Custom type otsPtpPmSampleDuration based on Integer32"""
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


_OtsPtpPmSampleDuration_Type.__name__ = "Integer32"
_OtsPtpPmSampleDuration_Object = MibTableColumn
otsPtpPmSampleDuration = _OtsPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 2),
    _OtsPtpPmSampleDuration_Type()
)
otsPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otsPtpPmSampleDuration.setStatus("current")
_OtsPtpPmValidity_Type = TruthValue
_OtsPtpPmValidity_Object = MibTableColumn
otsPtpPmValidity = _OtsPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 3),
    _OtsPtpPmValidity_Type()
)
otsPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmValidity.setStatus("current")
_OtsPtpPmOtsOptMin_Type = FloatHundredths
_OtsPtpPmOtsOptMin_Object = MibTableColumn
otsPtpPmOtsOptMin = _OtsPtpPmOtsOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 4),
    _OtsPtpPmOtsOptMin_Type()
)
otsPtpPmOtsOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsOptMin.setStatus("current")
_OtsPtpPmOtsOptMax_Type = FloatHundredths
_OtsPtpPmOtsOptMax_Object = MibTableColumn
otsPtpPmOtsOptMax = _OtsPtpPmOtsOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 5),
    _OtsPtpPmOtsOptMax_Type()
)
otsPtpPmOtsOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsOptMax.setStatus("current")
_OtsPtpPmOtsOptAve_Type = FloatHundredths
_OtsPtpPmOtsOptAve_Object = MibTableColumn
otsPtpPmOtsOptAve = _OtsPtpPmOtsOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 6),
    _OtsPtpPmOtsOptAve_Type()
)
otsPtpPmOtsOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsOptAve.setStatus("current")
_OtsPtpPmOtsOprMin_Type = FloatHundredths
_OtsPtpPmOtsOprMin_Object = MibTableColumn
otsPtpPmOtsOprMin = _OtsPtpPmOtsOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 7),
    _OtsPtpPmOtsOprMin_Type()
)
otsPtpPmOtsOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsOprMin.setStatus("current")
_OtsPtpPmOtsOprMax_Type = FloatHundredths
_OtsPtpPmOtsOprMax_Object = MibTableColumn
otsPtpPmOtsOprMax = _OtsPtpPmOtsOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 8),
    _OtsPtpPmOtsOprMax_Type()
)
otsPtpPmOtsOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsOprMax.setStatus("current")
_OtsPtpPmOtsOprAve_Type = FloatHundredths
_OtsPtpPmOtsOprAve_Object = MibTableColumn
otsPtpPmOtsOprAve = _OtsPtpPmOtsOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 9),
    _OtsPtpPmOtsOprAve_Type()
)
otsPtpPmOtsOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsOprAve.setStatus("current")
_OtsPtpPmOtsLbc1Min_Type = FloatHundredths
_OtsPtpPmOtsLbc1Min_Object = MibTableColumn
otsPtpPmOtsLbc1Min = _OtsPtpPmOtsLbc1Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 10),
    _OtsPtpPmOtsLbc1Min_Type()
)
otsPtpPmOtsLbc1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc1Min.setStatus("current")
_OtsPtpPmOtsLbc1Max_Type = FloatHundredths
_OtsPtpPmOtsLbc1Max_Object = MibTableColumn
otsPtpPmOtsLbc1Max = _OtsPtpPmOtsLbc1Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 11),
    _OtsPtpPmOtsLbc1Max_Type()
)
otsPtpPmOtsLbc1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc1Max.setStatus("current")
_OtsPtpPmOtsLbc1Ave_Type = FloatHundredths
_OtsPtpPmOtsLbc1Ave_Object = MibTableColumn
otsPtpPmOtsLbc1Ave = _OtsPtpPmOtsLbc1Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 12),
    _OtsPtpPmOtsLbc1Ave_Type()
)
otsPtpPmOtsLbc1Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc1Ave.setStatus("current")
_OtsPtpPmOtsLbc2Min_Type = FloatHundredths
_OtsPtpPmOtsLbc2Min_Object = MibTableColumn
otsPtpPmOtsLbc2Min = _OtsPtpPmOtsLbc2Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 13),
    _OtsPtpPmOtsLbc2Min_Type()
)
otsPtpPmOtsLbc2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc2Min.setStatus("current")
_OtsPtpPmOtsLbc2Max_Type = FloatHundredths
_OtsPtpPmOtsLbc2Max_Object = MibTableColumn
otsPtpPmOtsLbc2Max = _OtsPtpPmOtsLbc2Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 14),
    _OtsPtpPmOtsLbc2Max_Type()
)
otsPtpPmOtsLbc2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc2Max.setStatus("current")
_OtsPtpPmOtsLbc2Ave_Type = FloatHundredths
_OtsPtpPmOtsLbc2Ave_Object = MibTableColumn
otsPtpPmOtsLbc2Ave = _OtsPtpPmOtsLbc2Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 15),
    _OtsPtpPmOtsLbc2Ave_Type()
)
otsPtpPmOtsLbc2Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc2Ave.setStatus("current")
_OtsPtpPmOtsLbc3Min_Type = FloatHundredths
_OtsPtpPmOtsLbc3Min_Object = MibTableColumn
otsPtpPmOtsLbc3Min = _OtsPtpPmOtsLbc3Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 16),
    _OtsPtpPmOtsLbc3Min_Type()
)
otsPtpPmOtsLbc3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc3Min.setStatus("current")
_OtsPtpPmOtsLbc3Max_Type = FloatHundredths
_OtsPtpPmOtsLbc3Max_Object = MibTableColumn
otsPtpPmOtsLbc3Max = _OtsPtpPmOtsLbc3Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 17),
    _OtsPtpPmOtsLbc3Max_Type()
)
otsPtpPmOtsLbc3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc3Max.setStatus("current")
_OtsPtpPmOtsLbc3Ave_Type = FloatHundredths
_OtsPtpPmOtsLbc3Ave_Object = MibTableColumn
otsPtpPmOtsLbc3Ave = _OtsPtpPmOtsLbc3Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 18),
    _OtsPtpPmOtsLbc3Ave_Type()
)
otsPtpPmOtsLbc3Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc3Ave.setStatus("current")
_OtsPtpPmOtsLbc4Min_Type = FloatHundredths
_OtsPtpPmOtsLbc4Min_Object = MibTableColumn
otsPtpPmOtsLbc4Min = _OtsPtpPmOtsLbc4Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 19),
    _OtsPtpPmOtsLbc4Min_Type()
)
otsPtpPmOtsLbc4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc4Min.setStatus("current")
_OtsPtpPmOtsLbc4Max_Type = FloatHundredths
_OtsPtpPmOtsLbc4Max_Object = MibTableColumn
otsPtpPmOtsLbc4Max = _OtsPtpPmOtsLbc4Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 20),
    _OtsPtpPmOtsLbc4Max_Type()
)
otsPtpPmOtsLbc4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc4Max.setStatus("current")
_OtsPtpPmOtsLbc4Ave_Type = FloatHundredths
_OtsPtpPmOtsLbc4Ave_Object = MibTableColumn
otsPtpPmOtsLbc4Ave = _OtsPtpPmOtsLbc4Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 21),
    _OtsPtpPmOtsLbc4Ave_Type()
)
otsPtpPmOtsLbc4Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLbc4Ave.setStatus("current")
_OtsPtpPmOtsLpwr1Min_Type = FloatHundredths
_OtsPtpPmOtsLpwr1Min_Object = MibTableColumn
otsPtpPmOtsLpwr1Min = _OtsPtpPmOtsLpwr1Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 22),
    _OtsPtpPmOtsLpwr1Min_Type()
)
otsPtpPmOtsLpwr1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr1Min.setStatus("current")
_OtsPtpPmOtsLpwr1Max_Type = FloatHundredths
_OtsPtpPmOtsLpwr1Max_Object = MibTableColumn
otsPtpPmOtsLpwr1Max = _OtsPtpPmOtsLpwr1Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 23),
    _OtsPtpPmOtsLpwr1Max_Type()
)
otsPtpPmOtsLpwr1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr1Max.setStatus("current")
_OtsPtpPmOtsLpwr1Ave_Type = FloatHundredths
_OtsPtpPmOtsLpwr1Ave_Object = MibTableColumn
otsPtpPmOtsLpwr1Ave = _OtsPtpPmOtsLpwr1Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 24),
    _OtsPtpPmOtsLpwr1Ave_Type()
)
otsPtpPmOtsLpwr1Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr1Ave.setStatus("current")
_OtsPtpPmOtsLpwr2Min_Type = FloatHundredths
_OtsPtpPmOtsLpwr2Min_Object = MibTableColumn
otsPtpPmOtsLpwr2Min = _OtsPtpPmOtsLpwr2Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 25),
    _OtsPtpPmOtsLpwr2Min_Type()
)
otsPtpPmOtsLpwr2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr2Min.setStatus("current")
_OtsPtpPmOtsLpwr2Max_Type = FloatHundredths
_OtsPtpPmOtsLpwr2Max_Object = MibTableColumn
otsPtpPmOtsLpwr2Max = _OtsPtpPmOtsLpwr2Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 26),
    _OtsPtpPmOtsLpwr2Max_Type()
)
otsPtpPmOtsLpwr2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr2Max.setStatus("current")
_OtsPtpPmOtsLpwr2Ave_Type = FloatHundredths
_OtsPtpPmOtsLpwr2Ave_Object = MibTableColumn
otsPtpPmOtsLpwr2Ave = _OtsPtpPmOtsLpwr2Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 27),
    _OtsPtpPmOtsLpwr2Ave_Type()
)
otsPtpPmOtsLpwr2Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr2Ave.setStatus("current")
_OtsPtpPmOtsLpwr3Min_Type = FloatHundredths
_OtsPtpPmOtsLpwr3Min_Object = MibTableColumn
otsPtpPmOtsLpwr3Min = _OtsPtpPmOtsLpwr3Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 28),
    _OtsPtpPmOtsLpwr3Min_Type()
)
otsPtpPmOtsLpwr3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr3Min.setStatus("current")
_OtsPtpPmOtsLpwr3Max_Type = FloatHundredths
_OtsPtpPmOtsLpwr3Max_Object = MibTableColumn
otsPtpPmOtsLpwr3Max = _OtsPtpPmOtsLpwr3Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 29),
    _OtsPtpPmOtsLpwr3Max_Type()
)
otsPtpPmOtsLpwr3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr3Max.setStatus("current")
_OtsPtpPmOtsLpwr3Ave_Type = FloatHundredths
_OtsPtpPmOtsLpwr3Ave_Object = MibTableColumn
otsPtpPmOtsLpwr3Ave = _OtsPtpPmOtsLpwr3Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 30),
    _OtsPtpPmOtsLpwr3Ave_Type()
)
otsPtpPmOtsLpwr3Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr3Ave.setStatus("current")
_OtsPtpPmOtsLpwr4Min_Type = FloatHundredths
_OtsPtpPmOtsLpwr4Min_Object = MibTableColumn
otsPtpPmOtsLpwr4Min = _OtsPtpPmOtsLpwr4Min_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 31),
    _OtsPtpPmOtsLpwr4Min_Type()
)
otsPtpPmOtsLpwr4Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr4Min.setStatus("current")
_OtsPtpPmOtsLpwr4Max_Type = FloatHundredths
_OtsPtpPmOtsLpwr4Max_Object = MibTableColumn
otsPtpPmOtsLpwr4Max = _OtsPtpPmOtsLpwr4Max_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 32),
    _OtsPtpPmOtsLpwr4Max_Type()
)
otsPtpPmOtsLpwr4Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr4Max.setStatus("current")
_OtsPtpPmOtsLpwr4Ave_Type = FloatHundredths
_OtsPtpPmOtsLpwr4Ave_Object = MibTableColumn
otsPtpPmOtsLpwr4Ave = _OtsPtpPmOtsLpwr4Ave_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 33),
    _OtsPtpPmOtsLpwr4Ave_Type()
)
otsPtpPmOtsLpwr4Ave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpPmOtsLpwr4Ave.setStatus("current")
_OtsPtpOtsAlsOprMin_Type = FloatHundredths
_OtsPtpOtsAlsOprMin_Object = MibTableColumn
otsPtpOtsAlsOprMin = _OtsPtpOtsAlsOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 34),
    _OtsPtpOtsAlsOprMin_Type()
)
otsPtpOtsAlsOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsOprMin.setStatus("current")
_OtsPtpOtsAlsOprMax_Type = FloatHundredths
_OtsPtpOtsAlsOprMax_Object = MibTableColumn
otsPtpOtsAlsOprMax = _OtsPtpOtsAlsOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 35),
    _OtsPtpOtsAlsOprMax_Type()
)
otsPtpOtsAlsOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsOprMax.setStatus("current")
_OtsPtpOtsAlsOprAve_Type = FloatHundredths
_OtsPtpOtsAlsOprAve_Object = MibTableColumn
otsPtpOtsAlsOprAve = _OtsPtpOtsAlsOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 36),
    _OtsPtpOtsAlsOprAve_Type()
)
otsPtpOtsAlsOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsOprAve.setStatus("current")
_OtsPtpOtsAlsOptMin_Type = FloatHundredths
_OtsPtpOtsAlsOptMin_Object = MibTableColumn
otsPtpOtsAlsOptMin = _OtsPtpOtsAlsOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 37),
    _OtsPtpOtsAlsOptMin_Type()
)
otsPtpOtsAlsOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsOptMin.setStatus("current")
_OtsPtpOtsAlsOptMax_Type = FloatHundredths
_OtsPtpOtsAlsOptMax_Object = MibTableColumn
otsPtpOtsAlsOptMax = _OtsPtpOtsAlsOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 38),
    _OtsPtpOtsAlsOptMax_Type()
)
otsPtpOtsAlsOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsOptMax.setStatus("current")
_OtsPtpOtsAlsOptAve_Type = FloatHundredths
_OtsPtpOtsAlsOptAve_Object = MibTableColumn
otsPtpOtsAlsOptAve = _OtsPtpOtsAlsOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 39),
    _OtsPtpOtsAlsOptAve_Type()
)
otsPtpOtsAlsOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsOptAve.setStatus("current")
_OtsPtpOtsAlsLbcMin_Type = FloatHundredths
_OtsPtpOtsAlsLbcMin_Object = MibTableColumn
otsPtpOtsAlsLbcMin = _OtsPtpOtsAlsLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 40),
    _OtsPtpOtsAlsLbcMin_Type()
)
otsPtpOtsAlsLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsLbcMin.setStatus("current")
_OtsPtpOtsAlsLbcMax_Type = FloatHundredths
_OtsPtpOtsAlsLbcMax_Object = MibTableColumn
otsPtpOtsAlsLbcMax = _OtsPtpOtsAlsLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 41),
    _OtsPtpOtsAlsLbcMax_Type()
)
otsPtpOtsAlsLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsLbcMax.setStatus("current")
_OtsPtpOtsAlsLbcAve_Type = FloatHundredths
_OtsPtpOtsAlsLbcAve_Object = MibTableColumn
otsPtpOtsAlsLbcAve = _OtsPtpOtsAlsLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 2, 1, 42),
    _OtsPtpOtsAlsLbcAve_Type()
)
otsPtpOtsAlsLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsPtpOtsAlsLbcAve.setStatus("current")
_OtsPtpPmConformance_ObjectIdentity = ObjectIdentity
otsPtpPmConformance = _OtsPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3)
)
_OtsPtpPmCompliances_ObjectIdentity = ObjectIdentity
otsPtpPmCompliances = _OtsPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3, 1)
)
_OtsPtpPmGroups_ObjectIdentity = ObjectIdentity
otsPtpPmGroups = _OtsPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3, 2)
)

# Managed Objects groups

otsPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3, 2, 1)
)
otsPtpPmGroup.setObjects(
      *(("INFINERA-PM-OTSPTP-MIB", "otsPtpPmValidity"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsOptMin"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsOptMax"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsOptAve"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsOprMin"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsOprMax"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsOprAve"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc1Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc1Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc1Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc2Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc2Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc2Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc3Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc3Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc3Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc4Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc4Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLbc4Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr1Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr1Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr1Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr2Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr2Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr2Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr3Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr3Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr3Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr4Min"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr4Max"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmOtsLpwr4Ave"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsOprMin"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsOprMax"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsOprAve"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsOptMin"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsOptMax"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsOptAve"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsLbcMin"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsLbcMax"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpOtsAlsLbcAve"))
)
if mibBuilder.loadTexts:
    otsPtpPmGroup.setStatus("current")

otsPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3, 2, 2)
)
otsPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsOpt"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsOptOsaTapRatio"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsOpr"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsOprOsaTapRatio"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLbc1"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLbc2"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLbc3"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLbc4"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLpwr1"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLpwr2"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLpwr3"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsLpwr4"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsAlsOpr"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsAlsOpt"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOtsAlsLbc"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealRxPostEdfaOsaTapRatio"),
        ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealOprQ"))
)
if mibBuilder.loadTexts:
    otsPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otsPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3, 1, 1)
)
otsPtpPmCompliance.setObjects(
    ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmGroup")
)
if mibBuilder.loadTexts:
    otsPtpPmCompliance.setStatus(
        "current"
    )

otsPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 12, 3, 1, 2)
)
otsPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OTSPTP-MIB", "otsPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    otsPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OTSPTP-MIB",
    **{"otsPtpPmMIB": otsPtpPmMIB,
       "otsPtpPmRealTable": otsPtpPmRealTable,
       "otsPtpPmRealEntry": otsPtpPmRealEntry,
       "otsPtpPmRealOtsOpt": otsPtpPmRealOtsOpt,
       "otsPtpPmRealOtsOptOsaTapRatio": otsPtpPmRealOtsOptOsaTapRatio,
       "otsPtpPmRealOtsOpr": otsPtpPmRealOtsOpr,
       "otsPtpPmRealOtsOprOsaTapRatio": otsPtpPmRealOtsOprOsaTapRatio,
       "otsPtpPmRealOtsLbc1": otsPtpPmRealOtsLbc1,
       "otsPtpPmRealOtsLbc2": otsPtpPmRealOtsLbc2,
       "otsPtpPmRealOtsLbc3": otsPtpPmRealOtsLbc3,
       "otsPtpPmRealOtsLbc4": otsPtpPmRealOtsLbc4,
       "otsPtpPmRealOtsLpwr1": otsPtpPmRealOtsLpwr1,
       "otsPtpPmRealOtsLpwr2": otsPtpPmRealOtsLpwr2,
       "otsPtpPmRealOtsLpwr3": otsPtpPmRealOtsLpwr3,
       "otsPtpPmRealOtsLpwr4": otsPtpPmRealOtsLpwr4,
       "otsPtpPmRealOtsAlsOpr": otsPtpPmRealOtsAlsOpr,
       "otsPtpPmRealOtsAlsOpt": otsPtpPmRealOtsAlsOpt,
       "otsPtpPmRealOtsAlsLbc": otsPtpPmRealOtsAlsLbc,
       "otsPtpPmRealRxPostEdfaOsaTapRatio": otsPtpPmRealRxPostEdfaOsaTapRatio,
       "otsPtpPmRealOprQ": otsPtpPmRealOprQ,
       "otsPtpPmTable": otsPtpPmTable,
       "otsPtpPmEntry": otsPtpPmEntry,
       "otsPtpPmTimestamp": otsPtpPmTimestamp,
       "otsPtpPmSampleDuration": otsPtpPmSampleDuration,
       "otsPtpPmValidity": otsPtpPmValidity,
       "otsPtpPmOtsOptMin": otsPtpPmOtsOptMin,
       "otsPtpPmOtsOptMax": otsPtpPmOtsOptMax,
       "otsPtpPmOtsOptAve": otsPtpPmOtsOptAve,
       "otsPtpPmOtsOprMin": otsPtpPmOtsOprMin,
       "otsPtpPmOtsOprMax": otsPtpPmOtsOprMax,
       "otsPtpPmOtsOprAve": otsPtpPmOtsOprAve,
       "otsPtpPmOtsLbc1Min": otsPtpPmOtsLbc1Min,
       "otsPtpPmOtsLbc1Max": otsPtpPmOtsLbc1Max,
       "otsPtpPmOtsLbc1Ave": otsPtpPmOtsLbc1Ave,
       "otsPtpPmOtsLbc2Min": otsPtpPmOtsLbc2Min,
       "otsPtpPmOtsLbc2Max": otsPtpPmOtsLbc2Max,
       "otsPtpPmOtsLbc2Ave": otsPtpPmOtsLbc2Ave,
       "otsPtpPmOtsLbc3Min": otsPtpPmOtsLbc3Min,
       "otsPtpPmOtsLbc3Max": otsPtpPmOtsLbc3Max,
       "otsPtpPmOtsLbc3Ave": otsPtpPmOtsLbc3Ave,
       "otsPtpPmOtsLbc4Min": otsPtpPmOtsLbc4Min,
       "otsPtpPmOtsLbc4Max": otsPtpPmOtsLbc4Max,
       "otsPtpPmOtsLbc4Ave": otsPtpPmOtsLbc4Ave,
       "otsPtpPmOtsLpwr1Min": otsPtpPmOtsLpwr1Min,
       "otsPtpPmOtsLpwr1Max": otsPtpPmOtsLpwr1Max,
       "otsPtpPmOtsLpwr1Ave": otsPtpPmOtsLpwr1Ave,
       "otsPtpPmOtsLpwr2Min": otsPtpPmOtsLpwr2Min,
       "otsPtpPmOtsLpwr2Max": otsPtpPmOtsLpwr2Max,
       "otsPtpPmOtsLpwr2Ave": otsPtpPmOtsLpwr2Ave,
       "otsPtpPmOtsLpwr3Min": otsPtpPmOtsLpwr3Min,
       "otsPtpPmOtsLpwr3Max": otsPtpPmOtsLpwr3Max,
       "otsPtpPmOtsLpwr3Ave": otsPtpPmOtsLpwr3Ave,
       "otsPtpPmOtsLpwr4Min": otsPtpPmOtsLpwr4Min,
       "otsPtpPmOtsLpwr4Max": otsPtpPmOtsLpwr4Max,
       "otsPtpPmOtsLpwr4Ave": otsPtpPmOtsLpwr4Ave,
       "otsPtpOtsAlsOprMin": otsPtpOtsAlsOprMin,
       "otsPtpOtsAlsOprMax": otsPtpOtsAlsOprMax,
       "otsPtpOtsAlsOprAve": otsPtpOtsAlsOprAve,
       "otsPtpOtsAlsOptMin": otsPtpOtsAlsOptMin,
       "otsPtpOtsAlsOptMax": otsPtpOtsAlsOptMax,
       "otsPtpOtsAlsOptAve": otsPtpOtsAlsOptAve,
       "otsPtpOtsAlsLbcMin": otsPtpOtsAlsLbcMin,
       "otsPtpOtsAlsLbcMax": otsPtpOtsAlsLbcMax,
       "otsPtpOtsAlsLbcAve": otsPtpOtsAlsLbcAve,
       "otsPtpPmConformance": otsPtpPmConformance,
       "otsPtpPmCompliances": otsPtpPmCompliances,
       "otsPtpPmCompliance": otsPtpPmCompliance,
       "otsPtpPmRealCompliance": otsPtpPmRealCompliance,
       "otsPtpPmGroups": otsPtpPmGroups,
       "otsPtpPmGroup": otsPtpPmGroup,
       "otsPtpPmRealGroup": otsPtpPmRealGroup}
)
