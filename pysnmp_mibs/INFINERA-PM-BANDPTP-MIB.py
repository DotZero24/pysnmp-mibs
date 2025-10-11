# SNMP MIB module (INFINERA-PM-BANDPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-BANDPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:52 2025
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

bandPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81)
)
if mibBuilder.loadTexts:
    bandPtpPmMIB.setRevisions(
        ("2014-02-17 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BandPtpPmRealTable_Object = MibTable
bandPtpPmRealTable = _BandPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1)
)
if mibBuilder.loadTexts:
    bandPtpPmRealTable.setStatus("current")
_BandPtpPmRealEntry_Object = MibTableRow
bandPtpPmRealEntry = _BandPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1)
)
bandPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bandPtpPmRealEntry.setStatus("current")
_BandPtpPmRealOpt_Type = FloatHundredths
_BandPtpPmRealOpt_Object = MibTableColumn
bandPtpPmRealOpt = _BandPtpPmRealOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 1),
    _BandPtpPmRealOpt_Type()
)
bandPtpPmRealOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealOpt.setStatus("current")
_BandPtpPmRealOpr_Type = FloatHundredths
_BandPtpPmRealOpr_Object = MibTableColumn
bandPtpPmRealOpr = _BandPtpPmRealOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 2),
    _BandPtpPmRealOpr_Type()
)
bandPtpPmRealOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealOpr.setStatus("current")
_BandPtpPmRealRxEdfaOpt_Type = FloatHundredths
_BandPtpPmRealRxEdfaOpt_Object = MibTableColumn
bandPtpPmRealRxEdfaOpt = _BandPtpPmRealRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 3),
    _BandPtpPmRealRxEdfaOpt_Type()
)
bandPtpPmRealRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealRxEdfaOpt.setStatus("current")
_BandPtpPmRealTxEdfaOpt_Type = FloatHundredths
_BandPtpPmRealTxEdfaOpt_Object = MibTableColumn
bandPtpPmRealTxEdfaOpt = _BandPtpPmRealTxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 4),
    _BandPtpPmRealTxEdfaOpt_Type()
)
bandPtpPmRealTxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealTxEdfaOpt.setStatus("current")
_BandPtpPmRealRxEdfaOpr_Type = FloatHundredths
_BandPtpPmRealRxEdfaOpr_Object = MibTableColumn
bandPtpPmRealRxEdfaOpr = _BandPtpPmRealRxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 5),
    _BandPtpPmRealRxEdfaOpr_Type()
)
bandPtpPmRealRxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealRxEdfaOpr.setStatus("current")
_BandPtpPmRealTxEdfaOpr_Type = FloatHundredths
_BandPtpPmRealTxEdfaOpr_Object = MibTableColumn
bandPtpPmRealTxEdfaOpr = _BandPtpPmRealTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 6),
    _BandPtpPmRealTxEdfaOpr_Type()
)
bandPtpPmRealTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealTxEdfaOpr.setStatus("current")
_BandPtpPmRealRxEdfaLBC_Type = FloatHundredths
_BandPtpPmRealRxEdfaLBC_Object = MibTableColumn
bandPtpPmRealRxEdfaLBC = _BandPtpPmRealRxEdfaLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 7),
    _BandPtpPmRealRxEdfaLBC_Type()
)
bandPtpPmRealRxEdfaLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealRxEdfaLBC.setStatus("current")
_BandPtpPmRealTxEdfaLBC_Type = FloatHundredths
_BandPtpPmRealTxEdfaLBC_Object = MibTableColumn
bandPtpPmRealTxEdfaLBC = _BandPtpPmRealTxEdfaLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 8),
    _BandPtpPmRealTxEdfaLBC_Type()
)
bandPtpPmRealTxEdfaLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealTxEdfaLBC.setStatus("current")
_BandPtpPmRealOptOsaTapRatio_Type = FloatHundredths
_BandPtpPmRealOptOsaTapRatio_Object = MibTableColumn
bandPtpPmRealOptOsaTapRatio = _BandPtpPmRealOptOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 1, 1, 9),
    _BandPtpPmRealOptOsaTapRatio_Type()
)
bandPtpPmRealOptOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRealOptOsaTapRatio.setStatus("current")
_BandPtpPmTable_Object = MibTable
bandPtpPmTable = _BandPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2)
)
if mibBuilder.loadTexts:
    bandPtpPmTable.setStatus("current")
_BandPtpPmEntry_Object = MibTableRow
bandPtpPmEntry = _BandPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1)
)
bandPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-BANDPTP-MIB", "bandPtpPmSampleDuration"),
    (0, "INFINERA-PM-BANDPTP-MIB", "bandPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    bandPtpPmEntry.setStatus("current")


class _BandPtpPmTimestamp_Type(Integer32):
    """Custom type bandPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BandPtpPmTimestamp_Type.__name__ = "Integer32"
_BandPtpPmTimestamp_Object = MibTableColumn
bandPtpPmTimestamp = _BandPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 1),
    _BandPtpPmTimestamp_Type()
)
bandPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bandPtpPmTimestamp.setStatus("current")


class _BandPtpPmSampleDuration_Type(Integer32):
    """Custom type bandPtpPmSampleDuration based on Integer32"""
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


_BandPtpPmSampleDuration_Type.__name__ = "Integer32"
_BandPtpPmSampleDuration_Object = MibTableColumn
bandPtpPmSampleDuration = _BandPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 2),
    _BandPtpPmSampleDuration_Type()
)
bandPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bandPtpPmSampleDuration.setStatus("current")
_BandPtpPmValidity_Type = TruthValue
_BandPtpPmValidity_Object = MibTableColumn
bandPtpPmValidity = _BandPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 3),
    _BandPtpPmValidity_Type()
)
bandPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmValidity.setStatus("current")
_BandPtpPmOptMin_Type = FloatHundredths
_BandPtpPmOptMin_Object = MibTableColumn
bandPtpPmOptMin = _BandPtpPmOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 4),
    _BandPtpPmOptMin_Type()
)
bandPtpPmOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmOptMin.setStatus("current")
_BandPtpPmOptMax_Type = FloatHundredths
_BandPtpPmOptMax_Object = MibTableColumn
bandPtpPmOptMax = _BandPtpPmOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 5),
    _BandPtpPmOptMax_Type()
)
bandPtpPmOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmOptMax.setStatus("current")
_BandPtpPmOptAve_Type = FloatHundredths
_BandPtpPmOptAve_Object = MibTableColumn
bandPtpPmOptAve = _BandPtpPmOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 6),
    _BandPtpPmOptAve_Type()
)
bandPtpPmOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmOptAve.setStatus("current")
_BandPtpPmOprMin_Type = FloatHundredths
_BandPtpPmOprMin_Object = MibTableColumn
bandPtpPmOprMin = _BandPtpPmOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 7),
    _BandPtpPmOprMin_Type()
)
bandPtpPmOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmOprMin.setStatus("current")
_BandPtpPmOprMax_Type = FloatHundredths
_BandPtpPmOprMax_Object = MibTableColumn
bandPtpPmOprMax = _BandPtpPmOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 8),
    _BandPtpPmOprMax_Type()
)
bandPtpPmOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmOprMax.setStatus("current")
_BandPtpPmOprAve_Type = FloatHundredths
_BandPtpPmOprAve_Object = MibTableColumn
bandPtpPmOprAve = _BandPtpPmOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 9),
    _BandPtpPmOprAve_Type()
)
bandPtpPmOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmOprAve.setStatus("current")
_BandPtpPmRxEdfaOptMin_Type = FloatHundredths
_BandPtpPmRxEdfaOptMin_Object = MibTableColumn
bandPtpPmRxEdfaOptMin = _BandPtpPmRxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 10),
    _BandPtpPmRxEdfaOptMin_Type()
)
bandPtpPmRxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRxEdfaOptMin.setStatus("current")
_BandPtpPmRxEdfaOptMax_Type = FloatHundredths
_BandPtpPmRxEdfaOptMax_Object = MibTableColumn
bandPtpPmRxEdfaOptMax = _BandPtpPmRxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 11),
    _BandPtpPmRxEdfaOptMax_Type()
)
bandPtpPmRxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRxEdfaOptMax.setStatus("current")
_BandPtpPmRxEdfaOptAve_Type = FloatHundredths
_BandPtpPmRxEdfaOptAve_Object = MibTableColumn
bandPtpPmRxEdfaOptAve = _BandPtpPmRxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 12),
    _BandPtpPmRxEdfaOptAve_Type()
)
bandPtpPmRxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRxEdfaOptAve.setStatus("current")
_BandPtpPmTxEdfaOptMin_Type = FloatHundredths
_BandPtpPmTxEdfaOptMin_Object = MibTableColumn
bandPtpPmTxEdfaOptMin = _BandPtpPmTxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 13),
    _BandPtpPmTxEdfaOptMin_Type()
)
bandPtpPmTxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmTxEdfaOptMin.setStatus("current")
_BandPtpPmTxEdfaOptMax_Type = FloatHundredths
_BandPtpPmTxEdfaOptMax_Object = MibTableColumn
bandPtpPmTxEdfaOptMax = _BandPtpPmTxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 14),
    _BandPtpPmTxEdfaOptMax_Type()
)
bandPtpPmTxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmTxEdfaOptMax.setStatus("current")
_BandPtpPmTxEdfaOptAve_Type = FloatHundredths
_BandPtpPmTxEdfaOptAve_Object = MibTableColumn
bandPtpPmTxEdfaOptAve = _BandPtpPmTxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 15),
    _BandPtpPmTxEdfaOptAve_Type()
)
bandPtpPmTxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmTxEdfaOptAve.setStatus("current")
_BandPtpPmRxEdfaOprMin_Type = FloatHundredths
_BandPtpPmRxEdfaOprMin_Object = MibTableColumn
bandPtpPmRxEdfaOprMin = _BandPtpPmRxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 16),
    _BandPtpPmRxEdfaOprMin_Type()
)
bandPtpPmRxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRxEdfaOprMin.setStatus("current")
_BandPtpPmRxEdfaOprMax_Type = FloatHundredths
_BandPtpPmRxEdfaOprMax_Object = MibTableColumn
bandPtpPmRxEdfaOprMax = _BandPtpPmRxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 17),
    _BandPtpPmRxEdfaOprMax_Type()
)
bandPtpPmRxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRxEdfaOprMax.setStatus("current")
_BandPtpPmRxEdfaOprAve_Type = FloatHundredths
_BandPtpPmRxEdfaOprAve_Object = MibTableColumn
bandPtpPmRxEdfaOprAve = _BandPtpPmRxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 18),
    _BandPtpPmRxEdfaOprAve_Type()
)
bandPtpPmRxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmRxEdfaOprAve.setStatus("current")
_BandPtpPmTxEdfaOprMin_Type = FloatHundredths
_BandPtpPmTxEdfaOprMin_Object = MibTableColumn
bandPtpPmTxEdfaOprMin = _BandPtpPmTxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 19),
    _BandPtpPmTxEdfaOprMin_Type()
)
bandPtpPmTxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmTxEdfaOprMin.setStatus("current")
_BandPtpPmTxEdfaOprMax_Type = FloatHundredths
_BandPtpPmTxEdfaOprMax_Object = MibTableColumn
bandPtpPmTxEdfaOprMax = _BandPtpPmTxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 20),
    _BandPtpPmTxEdfaOprMax_Type()
)
bandPtpPmTxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmTxEdfaOprMax.setStatus("current")
_BandPtpPmTxEdfaOprAve_Type = FloatHundredths
_BandPtpPmTxEdfaOprAve_Object = MibTableColumn
bandPtpPmTxEdfaOprAve = _BandPtpPmTxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 21),
    _BandPtpPmTxEdfaOprAve_Type()
)
bandPtpPmTxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpPmTxEdfaOprAve.setStatus("current")
_BandPtpRxEdfaLBCMin_Type = FloatHundredths
_BandPtpRxEdfaLBCMin_Object = MibTableColumn
bandPtpRxEdfaLBCMin = _BandPtpRxEdfaLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 22),
    _BandPtpRxEdfaLBCMin_Type()
)
bandPtpRxEdfaLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpRxEdfaLBCMin.setStatus("current")
_BandPtpRxEdfaLBCMax_Type = FloatHundredths
_BandPtpRxEdfaLBCMax_Object = MibTableColumn
bandPtpRxEdfaLBCMax = _BandPtpRxEdfaLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 23),
    _BandPtpRxEdfaLBCMax_Type()
)
bandPtpRxEdfaLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpRxEdfaLBCMax.setStatus("current")
_BandPtpRxEdfaLBCAve_Type = FloatHundredths
_BandPtpRxEdfaLBCAve_Object = MibTableColumn
bandPtpRxEdfaLBCAve = _BandPtpRxEdfaLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 24),
    _BandPtpRxEdfaLBCAve_Type()
)
bandPtpRxEdfaLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpRxEdfaLBCAve.setStatus("current")
_BandPtpTxEdfaLBCMin_Type = FloatHundredths
_BandPtpTxEdfaLBCMin_Object = MibTableColumn
bandPtpTxEdfaLBCMin = _BandPtpTxEdfaLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 25),
    _BandPtpTxEdfaLBCMin_Type()
)
bandPtpTxEdfaLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpTxEdfaLBCMin.setStatus("current")
_BandPtpTxEdfaLBCMax_Type = FloatHundredths
_BandPtpTxEdfaLBCMax_Object = MibTableColumn
bandPtpTxEdfaLBCMax = _BandPtpTxEdfaLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 26),
    _BandPtpTxEdfaLBCMax_Type()
)
bandPtpTxEdfaLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpTxEdfaLBCMax.setStatus("current")
_BandPtpTxEdfaLBCAve_Type = FloatHundredths
_BandPtpTxEdfaLBCAve_Object = MibTableColumn
bandPtpTxEdfaLBCAve = _BandPtpTxEdfaLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 2, 1, 27),
    _BandPtpTxEdfaLBCAve_Type()
)
bandPtpTxEdfaLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpTxEdfaLBCAve.setStatus("current")
_BandPtpPmConformance_ObjectIdentity = ObjectIdentity
bandPtpPmConformance = _BandPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3)
)
_BandPtpPmCompliances_ObjectIdentity = ObjectIdentity
bandPtpPmCompliances = _BandPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3, 1)
)
_BandPtpPmGroups_ObjectIdentity = ObjectIdentity
bandPtpPmGroups = _BandPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3, 2)
)

# Managed Objects groups

bandPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3, 2, 1)
)
bandPtpPmGroup.setObjects(
      *(("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTimestamp"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmSampleDuration"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmValidity"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmOptMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmOptMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmOptAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmOprMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmOprMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmOprAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRxEdfaOptMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRxEdfaOptMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRxEdfaOptAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTxEdfaOptMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTxEdfaOptMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTxEdfaOptAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRxEdfaOprMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRxEdfaOprMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRxEdfaOprAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTxEdfaOprMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTxEdfaOprMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmTxEdfaOprAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpRxEdfaLBCMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpRxEdfaLBCMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpRxEdfaLBCAve"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpTxEdfaLBCMin"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpTxEdfaLBCMax"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpTxEdfaLBCAve"))
)
if mibBuilder.loadTexts:
    bandPtpPmGroup.setStatus("current")

bandPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3, 2, 2)
)
bandPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealOpt"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealOpr"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealRxEdfaOpt"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealTxEdfaOpt"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealRxEdfaOpr"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealTxEdfaOpr"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealRxEdfaLBC"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealTxEdfaLBC"),
        ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealOptOsaTapRatio"))
)
if mibBuilder.loadTexts:
    bandPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bandPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3, 1, 1)
)
bandPtpPmCompliance.setObjects(
    ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmGroup")
)
if mibBuilder.loadTexts:
    bandPtpPmCompliance.setStatus(
        "current"
    )

bandPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 81, 3, 1, 2)
)
bandPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-BANDPTP-MIB", "bandPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    bandPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-BANDPTP-MIB",
    **{"bandPtpPmMIB": bandPtpPmMIB,
       "bandPtpPmRealTable": bandPtpPmRealTable,
       "bandPtpPmRealEntry": bandPtpPmRealEntry,
       "bandPtpPmRealOpt": bandPtpPmRealOpt,
       "bandPtpPmRealOpr": bandPtpPmRealOpr,
       "bandPtpPmRealRxEdfaOpt": bandPtpPmRealRxEdfaOpt,
       "bandPtpPmRealTxEdfaOpt": bandPtpPmRealTxEdfaOpt,
       "bandPtpPmRealRxEdfaOpr": bandPtpPmRealRxEdfaOpr,
       "bandPtpPmRealTxEdfaOpr": bandPtpPmRealTxEdfaOpr,
       "bandPtpPmRealRxEdfaLBC": bandPtpPmRealRxEdfaLBC,
       "bandPtpPmRealTxEdfaLBC": bandPtpPmRealTxEdfaLBC,
       "bandPtpPmRealOptOsaTapRatio": bandPtpPmRealOptOsaTapRatio,
       "bandPtpPmTable": bandPtpPmTable,
       "bandPtpPmEntry": bandPtpPmEntry,
       "bandPtpPmTimestamp": bandPtpPmTimestamp,
       "bandPtpPmSampleDuration": bandPtpPmSampleDuration,
       "bandPtpPmValidity": bandPtpPmValidity,
       "bandPtpPmOptMin": bandPtpPmOptMin,
       "bandPtpPmOptMax": bandPtpPmOptMax,
       "bandPtpPmOptAve": bandPtpPmOptAve,
       "bandPtpPmOprMin": bandPtpPmOprMin,
       "bandPtpPmOprMax": bandPtpPmOprMax,
       "bandPtpPmOprAve": bandPtpPmOprAve,
       "bandPtpPmRxEdfaOptMin": bandPtpPmRxEdfaOptMin,
       "bandPtpPmRxEdfaOptMax": bandPtpPmRxEdfaOptMax,
       "bandPtpPmRxEdfaOptAve": bandPtpPmRxEdfaOptAve,
       "bandPtpPmTxEdfaOptMin": bandPtpPmTxEdfaOptMin,
       "bandPtpPmTxEdfaOptMax": bandPtpPmTxEdfaOptMax,
       "bandPtpPmTxEdfaOptAve": bandPtpPmTxEdfaOptAve,
       "bandPtpPmRxEdfaOprMin": bandPtpPmRxEdfaOprMin,
       "bandPtpPmRxEdfaOprMax": bandPtpPmRxEdfaOprMax,
       "bandPtpPmRxEdfaOprAve": bandPtpPmRxEdfaOprAve,
       "bandPtpPmTxEdfaOprMin": bandPtpPmTxEdfaOprMin,
       "bandPtpPmTxEdfaOprMax": bandPtpPmTxEdfaOprMax,
       "bandPtpPmTxEdfaOprAve": bandPtpPmTxEdfaOprAve,
       "bandPtpRxEdfaLBCMin": bandPtpRxEdfaLBCMin,
       "bandPtpRxEdfaLBCMax": bandPtpRxEdfaLBCMax,
       "bandPtpRxEdfaLBCAve": bandPtpRxEdfaLBCAve,
       "bandPtpTxEdfaLBCMin": bandPtpTxEdfaLBCMin,
       "bandPtpTxEdfaLBCMax": bandPtpTxEdfaLBCMax,
       "bandPtpTxEdfaLBCAve": bandPtpTxEdfaLBCAve,
       "bandPtpPmConformance": bandPtpPmConformance,
       "bandPtpPmCompliances": bandPtpPmCompliances,
       "bandPtpPmCompliance": bandPtpPmCompliance,
       "bandPtpPmRealCompliance": bandPtpPmRealCompliance,
       "bandPtpPmGroups": bandPtpPmGroups,
       "bandPtpPmGroup": bandPtpPmGroup,
       "bandPtpPmRealGroup": bandPtpPmRealGroup}
)
