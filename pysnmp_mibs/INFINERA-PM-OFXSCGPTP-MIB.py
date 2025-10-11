# SNMP MIB module (INFINERA-PM-OFXSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OFXSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:12 2025
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

ofxScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39)
)
if mibBuilder.loadTexts:
    ofxScgPtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfxScgPtpPmRealTable_Object = MibTable
ofxScgPtpPmRealTable = _OfxScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1)
)
if mibBuilder.loadTexts:
    ofxScgPtpPmRealTable.setStatus("current")
_OfxScgPtpPmRealEntry_Object = MibTableRow
ofxScgPtpPmRealEntry = _OfxScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1)
)
ofxScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ofxScgPtpPmRealEntry.setStatus("current")
_OfxScgPtpPmRealChanScgOpt_Type = FloatHundredths
_OfxScgPtpPmRealChanScgOpt_Object = MibTableColumn
ofxScgPtpPmRealChanScgOpt = _OfxScgPtpPmRealChanScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 1),
    _OfxScgPtpPmRealChanScgOpt_Type()
)
ofxScgPtpPmRealChanScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealChanScgOpt.setStatus("current")
_OfxScgPtpPmRealChanScgOpr_Type = FloatHundredths
_OfxScgPtpPmRealChanScgOpr_Object = MibTableColumn
ofxScgPtpPmRealChanScgOpr = _OfxScgPtpPmRealChanScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 2),
    _OfxScgPtpPmRealChanScgOpr_Type()
)
ofxScgPtpPmRealChanScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealChanScgOpr.setStatus("current")
_OfxScgPtpPmRealTxEdfaOpr_Type = FloatHundredths
_OfxScgPtpPmRealTxEdfaOpr_Object = MibTableColumn
ofxScgPtpPmRealTxEdfaOpr = _OfxScgPtpPmRealTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 3),
    _OfxScgPtpPmRealTxEdfaOpr_Type()
)
ofxScgPtpPmRealTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealTxEdfaOpr.setStatus("current")
_OfxScgPtpPmRealTxEdfaOpt_Type = FloatHundredths
_OfxScgPtpPmRealTxEdfaOpt_Object = MibTableColumn
ofxScgPtpPmRealTxEdfaOpt = _OfxScgPtpPmRealTxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 4),
    _OfxScgPtpPmRealTxEdfaOpt_Type()
)
ofxScgPtpPmRealTxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealTxEdfaOpt.setStatus("current")
_OfxScgPtpPmRealTxEdfaLbc_Type = FloatHundredths
_OfxScgPtpPmRealTxEdfaLbc_Object = MibTableColumn
ofxScgPtpPmRealTxEdfaLbc = _OfxScgPtpPmRealTxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 5),
    _OfxScgPtpPmRealTxEdfaLbc_Type()
)
ofxScgPtpPmRealTxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealTxEdfaLbc.setStatus("current")
_OfxScgPtpPmRealRxEdfaOpr_Type = FloatHundredths
_OfxScgPtpPmRealRxEdfaOpr_Object = MibTableColumn
ofxScgPtpPmRealRxEdfaOpr = _OfxScgPtpPmRealRxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 6),
    _OfxScgPtpPmRealRxEdfaOpr_Type()
)
ofxScgPtpPmRealRxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealRxEdfaOpr.setStatus("current")
_OfxScgPtpPmRealRxEdfaOpt_Type = FloatHundredths
_OfxScgPtpPmRealRxEdfaOpt_Object = MibTableColumn
ofxScgPtpPmRealRxEdfaOpt = _OfxScgPtpPmRealRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 7),
    _OfxScgPtpPmRealRxEdfaOpt_Type()
)
ofxScgPtpPmRealRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealRxEdfaOpt.setStatus("current")
_OfxScgPtpPmRealRxEdfaLbc_Type = FloatHundredths
_OfxScgPtpPmRealRxEdfaLbc_Object = MibTableColumn
ofxScgPtpPmRealRxEdfaLbc = _OfxScgPtpPmRealRxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 8),
    _OfxScgPtpPmRealRxEdfaLbc_Type()
)
ofxScgPtpPmRealRxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealRxEdfaLbc.setStatus("current")
_OfxScgPtpPmRealQPreFec_Type = FloatHundredths
_OfxScgPtpPmRealQPreFec_Object = MibTableColumn
ofxScgPtpPmRealQPreFec = _OfxScgPtpPmRealQPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 9),
    _OfxScgPtpPmRealQPreFec_Type()
)
ofxScgPtpPmRealQPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealQPreFec.setStatus("current")
_OfxScgPtpPmRealBerPreFec_Type = FloatHundredths
_OfxScgPtpPmRealBerPreFec_Object = MibTableColumn
ofxScgPtpPmRealBerPreFec = _OfxScgPtpPmRealBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 1, 1, 10),
    _OfxScgPtpPmRealBerPreFec_Type()
)
ofxScgPtpPmRealBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRealBerPreFec.setStatus("current")
_OfxScgPtpPmTable_Object = MibTable
ofxScgPtpPmTable = _OfxScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2)
)
if mibBuilder.loadTexts:
    ofxScgPtpPmTable.setStatus("current")
_OfxScgPtpPmEntry_Object = MibTableRow
ofxScgPtpPmEntry = _OfxScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1)
)
ofxScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ofxScgPtpPmEntry.setStatus("current")


class _OfxScgPtpPmTimestamp_Type(Integer32):
    """Custom type ofxScgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OfxScgPtpPmTimestamp_Type.__name__ = "Integer32"
_OfxScgPtpPmTimestamp_Object = MibTableColumn
ofxScgPtpPmTimestamp = _OfxScgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 1),
    _OfxScgPtpPmTimestamp_Type()
)
ofxScgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofxScgPtpPmTimestamp.setStatus("current")


class _OfxScgPtpPmSampleDuration_Type(Integer32):
    """Custom type ofxScgPtpPmSampleDuration based on Integer32"""
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


_OfxScgPtpPmSampleDuration_Type.__name__ = "Integer32"
_OfxScgPtpPmSampleDuration_Object = MibTableColumn
ofxScgPtpPmSampleDuration = _OfxScgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 2),
    _OfxScgPtpPmSampleDuration_Type()
)
ofxScgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ofxScgPtpPmSampleDuration.setStatus("current")
_OfxScgPtpPmValidity_Type = TruthValue
_OfxScgPtpPmValidity_Object = MibTableColumn
ofxScgPtpPmValidity = _OfxScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 3),
    _OfxScgPtpPmValidity_Type()
)
ofxScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmValidity.setStatus("current")
_OfxScgPtpPmTxEdfaOprMin_Type = FloatHundredths
_OfxScgPtpPmTxEdfaOprMin_Object = MibTableColumn
ofxScgPtpPmTxEdfaOprMin = _OfxScgPtpPmTxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 4),
    _OfxScgPtpPmTxEdfaOprMin_Type()
)
ofxScgPtpPmTxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaOprMin.setStatus("current")
_OfxScgPtpPmTxEdfaOprMax_Type = FloatHundredths
_OfxScgPtpPmTxEdfaOprMax_Object = MibTableColumn
ofxScgPtpPmTxEdfaOprMax = _OfxScgPtpPmTxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 5),
    _OfxScgPtpPmTxEdfaOprMax_Type()
)
ofxScgPtpPmTxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaOprMax.setStatus("current")
_OfxScgPtpPmTxEdfaOprAve_Type = FloatHundredths
_OfxScgPtpPmTxEdfaOprAve_Object = MibTableColumn
ofxScgPtpPmTxEdfaOprAve = _OfxScgPtpPmTxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 6),
    _OfxScgPtpPmTxEdfaOprAve_Type()
)
ofxScgPtpPmTxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaOprAve.setStatus("current")
_OfxScgPtpPmTxEdfaOptMin_Type = FloatHundredths
_OfxScgPtpPmTxEdfaOptMin_Object = MibTableColumn
ofxScgPtpPmTxEdfaOptMin = _OfxScgPtpPmTxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 7),
    _OfxScgPtpPmTxEdfaOptMin_Type()
)
ofxScgPtpPmTxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaOptMin.setStatus("current")
_OfxScgPtpPmTxEdfaOptMax_Type = FloatHundredths
_OfxScgPtpPmTxEdfaOptMax_Object = MibTableColumn
ofxScgPtpPmTxEdfaOptMax = _OfxScgPtpPmTxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 8),
    _OfxScgPtpPmTxEdfaOptMax_Type()
)
ofxScgPtpPmTxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaOptMax.setStatus("current")
_OfxScgPtpPmTxEdfaOptAve_Type = FloatHundredths
_OfxScgPtpPmTxEdfaOptAve_Object = MibTableColumn
ofxScgPtpPmTxEdfaOptAve = _OfxScgPtpPmTxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 9),
    _OfxScgPtpPmTxEdfaOptAve_Type()
)
ofxScgPtpPmTxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaOptAve.setStatus("current")
_OfxScgPtpPmTxEdfaLbcMin_Type = FloatHundredths
_OfxScgPtpPmTxEdfaLbcMin_Object = MibTableColumn
ofxScgPtpPmTxEdfaLbcMin = _OfxScgPtpPmTxEdfaLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 10),
    _OfxScgPtpPmTxEdfaLbcMin_Type()
)
ofxScgPtpPmTxEdfaLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaLbcMin.setStatus("current")
_OfxScgPtpPmTxEdfaLbcMax_Type = FloatHundredths
_OfxScgPtpPmTxEdfaLbcMax_Object = MibTableColumn
ofxScgPtpPmTxEdfaLbcMax = _OfxScgPtpPmTxEdfaLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 11),
    _OfxScgPtpPmTxEdfaLbcMax_Type()
)
ofxScgPtpPmTxEdfaLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaLbcMax.setStatus("current")
_OfxScgPtpPmTxEdfaLbcAve_Type = FloatHundredths
_OfxScgPtpPmTxEdfaLbcAve_Object = MibTableColumn
ofxScgPtpPmTxEdfaLbcAve = _OfxScgPtpPmTxEdfaLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 12),
    _OfxScgPtpPmTxEdfaLbcAve_Type()
)
ofxScgPtpPmTxEdfaLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmTxEdfaLbcAve.setStatus("current")
_OfxScgPtpPmRxEdfaOprMin_Type = FloatHundredths
_OfxScgPtpPmRxEdfaOprMin_Object = MibTableColumn
ofxScgPtpPmRxEdfaOprMin = _OfxScgPtpPmRxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 13),
    _OfxScgPtpPmRxEdfaOprMin_Type()
)
ofxScgPtpPmRxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaOprMin.setStatus("current")
_OfxScgPtpPmRxEdfaOprMax_Type = FloatHundredths
_OfxScgPtpPmRxEdfaOprMax_Object = MibTableColumn
ofxScgPtpPmRxEdfaOprMax = _OfxScgPtpPmRxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 14),
    _OfxScgPtpPmRxEdfaOprMax_Type()
)
ofxScgPtpPmRxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaOprMax.setStatus("current")
_OfxScgPtpPmRxEdfaOprAve_Type = FloatHundredths
_OfxScgPtpPmRxEdfaOprAve_Object = MibTableColumn
ofxScgPtpPmRxEdfaOprAve = _OfxScgPtpPmRxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 15),
    _OfxScgPtpPmRxEdfaOprAve_Type()
)
ofxScgPtpPmRxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaOprAve.setStatus("current")
_OfxScgPtpPmRxEdfaOptMin_Type = FloatHundredths
_OfxScgPtpPmRxEdfaOptMin_Object = MibTableColumn
ofxScgPtpPmRxEdfaOptMin = _OfxScgPtpPmRxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 16),
    _OfxScgPtpPmRxEdfaOptMin_Type()
)
ofxScgPtpPmRxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaOptMin.setStatus("current")
_OfxScgPtpPmRxEdfaOptMax_Type = FloatHundredths
_OfxScgPtpPmRxEdfaOptMax_Object = MibTableColumn
ofxScgPtpPmRxEdfaOptMax = _OfxScgPtpPmRxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 17),
    _OfxScgPtpPmRxEdfaOptMax_Type()
)
ofxScgPtpPmRxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaOptMax.setStatus("current")
_OfxScgPtpPmRxEdfaOptAve_Type = FloatHundredths
_OfxScgPtpPmRxEdfaOptAve_Object = MibTableColumn
ofxScgPtpPmRxEdfaOptAve = _OfxScgPtpPmRxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 18),
    _OfxScgPtpPmRxEdfaOptAve_Type()
)
ofxScgPtpPmRxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaOptAve.setStatus("current")
_OfxScgPtpPmRxEdfaLbcMin_Type = FloatHundredths
_OfxScgPtpPmRxEdfaLbcMin_Object = MibTableColumn
ofxScgPtpPmRxEdfaLbcMin = _OfxScgPtpPmRxEdfaLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 19),
    _OfxScgPtpPmRxEdfaLbcMin_Type()
)
ofxScgPtpPmRxEdfaLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaLbcMin.setStatus("current")
_OfxScgPtpPmRxEdfaLbcMax_Type = FloatHundredths
_OfxScgPtpPmRxEdfaLbcMax_Object = MibTableColumn
ofxScgPtpPmRxEdfaLbcMax = _OfxScgPtpPmRxEdfaLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 20),
    _OfxScgPtpPmRxEdfaLbcMax_Type()
)
ofxScgPtpPmRxEdfaLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaLbcMax.setStatus("current")
_OfxScgPtpPmRxEdfaLbcAve_Type = FloatHundredths
_OfxScgPtpPmRxEdfaLbcAve_Object = MibTableColumn
ofxScgPtpPmRxEdfaLbcAve = _OfxScgPtpPmRxEdfaLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 21),
    _OfxScgPtpPmRxEdfaLbcAve_Type()
)
ofxScgPtpPmRxEdfaLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmRxEdfaLbcAve.setStatus("current")
_OfxScgPtpPmQPreFecMin_Type = FloatHundredths
_OfxScgPtpPmQPreFecMin_Object = MibTableColumn
ofxScgPtpPmQPreFecMin = _OfxScgPtpPmQPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 22),
    _OfxScgPtpPmQPreFecMin_Type()
)
ofxScgPtpPmQPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmQPreFecMin.setStatus("current")
_OfxScgPtpPmQPreFecMax_Type = FloatHundredths
_OfxScgPtpPmQPreFecMax_Object = MibTableColumn
ofxScgPtpPmQPreFecMax = _OfxScgPtpPmQPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 23),
    _OfxScgPtpPmQPreFecMax_Type()
)
ofxScgPtpPmQPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmQPreFecMax.setStatus("current")
_OfxScgPtpPmQPreFecAve_Type = FloatHundredths
_OfxScgPtpPmQPreFecAve_Object = MibTableColumn
ofxScgPtpPmQPreFecAve = _OfxScgPtpPmQPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 24),
    _OfxScgPtpPmQPreFecAve_Type()
)
ofxScgPtpPmQPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmQPreFecAve.setStatus("current")
_OfxScgPtpPmBerPreFecMin_Type = FloatHundredths
_OfxScgPtpPmBerPreFecMin_Object = MibTableColumn
ofxScgPtpPmBerPreFecMin = _OfxScgPtpPmBerPreFecMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 25),
    _OfxScgPtpPmBerPreFecMin_Type()
)
ofxScgPtpPmBerPreFecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmBerPreFecMin.setStatus("current")
_OfxScgPtpPmBerPreFecMax_Type = FloatHundredths
_OfxScgPtpPmBerPreFecMax_Object = MibTableColumn
ofxScgPtpPmBerPreFecMax = _OfxScgPtpPmBerPreFecMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 26),
    _OfxScgPtpPmBerPreFecMax_Type()
)
ofxScgPtpPmBerPreFecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmBerPreFecMax.setStatus("current")
_OfxScgPtpPmBerPreFecAve_Type = FloatHundredths
_OfxScgPtpPmBerPreFecAve_Object = MibTableColumn
ofxScgPtpPmBerPreFecAve = _OfxScgPtpPmBerPreFecAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 2, 1, 27),
    _OfxScgPtpPmBerPreFecAve_Type()
)
ofxScgPtpPmBerPreFecAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpPmBerPreFecAve.setStatus("current")
_OfxScgPtpPmConformance_ObjectIdentity = ObjectIdentity
ofxScgPtpPmConformance = _OfxScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3)
)
_OfxScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
ofxScgPtpPmCompliances = _OfxScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3, 1)
)
_OfxScgPtpPmGroups_ObjectIdentity = ObjectIdentity
ofxScgPtpPmGroups = _OfxScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3, 2)
)

# Managed Objects groups

ofxScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3, 2, 1)
)
ofxScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTimestamp"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmSampleDuration"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmValidity"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaOprMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaOprMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaOprAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaOptMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaOptMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaOptAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaLbcMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaLbcMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmTxEdfaLbcAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaOprMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaOprMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaOprAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaOptMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaOptMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaOptAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaLbcMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaLbcMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRxEdfaLbcAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmQPreFecMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmQPreFecMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmQPreFecAve"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmBerPreFecMin"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmBerPreFecMax"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmBerPreFecAve"))
)
if mibBuilder.loadTexts:
    ofxScgPtpPmGroup.setStatus("current")

ofxScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3, 2, 2)
)
ofxScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealChanScgOpt"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealChanScgOpr"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealTxEdfaOpr"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealTxEdfaOpt"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealTxEdfaLbc"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealRxEdfaOpr"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealRxEdfaOpt"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealRxEdfaLbc"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealQPreFec"),
        ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealBerPreFec"))
)
if mibBuilder.loadTexts:
    ofxScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ofxScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3, 1, 1)
)
ofxScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    ofxScgPtpPmCompliance.setStatus(
        "current"
    )

ofxScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 39, 3, 1, 2)
)
ofxScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OFXSCGPTP-MIB", "ofxScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    ofxScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OFXSCGPTP-MIB",
    **{"ofxScgPtpPmMIB": ofxScgPtpPmMIB,
       "ofxScgPtpPmRealTable": ofxScgPtpPmRealTable,
       "ofxScgPtpPmRealEntry": ofxScgPtpPmRealEntry,
       "ofxScgPtpPmRealChanScgOpt": ofxScgPtpPmRealChanScgOpt,
       "ofxScgPtpPmRealChanScgOpr": ofxScgPtpPmRealChanScgOpr,
       "ofxScgPtpPmRealTxEdfaOpr": ofxScgPtpPmRealTxEdfaOpr,
       "ofxScgPtpPmRealTxEdfaOpt": ofxScgPtpPmRealTxEdfaOpt,
       "ofxScgPtpPmRealTxEdfaLbc": ofxScgPtpPmRealTxEdfaLbc,
       "ofxScgPtpPmRealRxEdfaOpr": ofxScgPtpPmRealRxEdfaOpr,
       "ofxScgPtpPmRealRxEdfaOpt": ofxScgPtpPmRealRxEdfaOpt,
       "ofxScgPtpPmRealRxEdfaLbc": ofxScgPtpPmRealRxEdfaLbc,
       "ofxScgPtpPmRealQPreFec": ofxScgPtpPmRealQPreFec,
       "ofxScgPtpPmRealBerPreFec": ofxScgPtpPmRealBerPreFec,
       "ofxScgPtpPmTable": ofxScgPtpPmTable,
       "ofxScgPtpPmEntry": ofxScgPtpPmEntry,
       "ofxScgPtpPmTimestamp": ofxScgPtpPmTimestamp,
       "ofxScgPtpPmSampleDuration": ofxScgPtpPmSampleDuration,
       "ofxScgPtpPmValidity": ofxScgPtpPmValidity,
       "ofxScgPtpPmTxEdfaOprMin": ofxScgPtpPmTxEdfaOprMin,
       "ofxScgPtpPmTxEdfaOprMax": ofxScgPtpPmTxEdfaOprMax,
       "ofxScgPtpPmTxEdfaOprAve": ofxScgPtpPmTxEdfaOprAve,
       "ofxScgPtpPmTxEdfaOptMin": ofxScgPtpPmTxEdfaOptMin,
       "ofxScgPtpPmTxEdfaOptMax": ofxScgPtpPmTxEdfaOptMax,
       "ofxScgPtpPmTxEdfaOptAve": ofxScgPtpPmTxEdfaOptAve,
       "ofxScgPtpPmTxEdfaLbcMin": ofxScgPtpPmTxEdfaLbcMin,
       "ofxScgPtpPmTxEdfaLbcMax": ofxScgPtpPmTxEdfaLbcMax,
       "ofxScgPtpPmTxEdfaLbcAve": ofxScgPtpPmTxEdfaLbcAve,
       "ofxScgPtpPmRxEdfaOprMin": ofxScgPtpPmRxEdfaOprMin,
       "ofxScgPtpPmRxEdfaOprMax": ofxScgPtpPmRxEdfaOprMax,
       "ofxScgPtpPmRxEdfaOprAve": ofxScgPtpPmRxEdfaOprAve,
       "ofxScgPtpPmRxEdfaOptMin": ofxScgPtpPmRxEdfaOptMin,
       "ofxScgPtpPmRxEdfaOptMax": ofxScgPtpPmRxEdfaOptMax,
       "ofxScgPtpPmRxEdfaOptAve": ofxScgPtpPmRxEdfaOptAve,
       "ofxScgPtpPmRxEdfaLbcMin": ofxScgPtpPmRxEdfaLbcMin,
       "ofxScgPtpPmRxEdfaLbcMax": ofxScgPtpPmRxEdfaLbcMax,
       "ofxScgPtpPmRxEdfaLbcAve": ofxScgPtpPmRxEdfaLbcAve,
       "ofxScgPtpPmQPreFecMin": ofxScgPtpPmQPreFecMin,
       "ofxScgPtpPmQPreFecMax": ofxScgPtpPmQPreFecMax,
       "ofxScgPtpPmQPreFecAve": ofxScgPtpPmQPreFecAve,
       "ofxScgPtpPmBerPreFecMin": ofxScgPtpPmBerPreFecMin,
       "ofxScgPtpPmBerPreFecMax": ofxScgPtpPmBerPreFecMax,
       "ofxScgPtpPmBerPreFecAve": ofxScgPtpPmBerPreFecAve,
       "ofxScgPtpPmConformance": ofxScgPtpPmConformance,
       "ofxScgPtpPmCompliances": ofxScgPtpPmCompliances,
       "ofxScgPtpPmCompliance": ofxScgPtpPmCompliance,
       "ofxScgPtpPmRealCompliance": ofxScgPtpPmRealCompliance,
       "ofxScgPtpPmGroups": ofxScgPtpPmGroups,
       "ofxScgPtpPmGroup": ofxScgPtpPmGroup,
       "ofxScgPtpPmRealGroup": ofxScgPtpPmRealGroup}
)
