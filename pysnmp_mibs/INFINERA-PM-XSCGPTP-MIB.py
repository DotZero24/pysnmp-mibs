# SNMP MIB module (INFINERA-PM-XSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-XSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:00 2025
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

xScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33)
)
if mibBuilder.loadTexts:
    xScgPtpPmMIB.setRevisions(
        ("2015-12-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XScgPtpPmRealTable_Object = MibTable
xScgPtpPmRealTable = _XScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1)
)
if mibBuilder.loadTexts:
    xScgPtpPmRealTable.setStatus("current")
_XScgPtpPmRealEntry_Object = MibTableRow
xScgPtpPmRealEntry = _XScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1)
)
xScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xScgPtpPmRealEntry.setStatus("current")
_XScgPtpPmRealChanScgOpt_Type = FloatHundredths
_XScgPtpPmRealChanScgOpt_Object = MibTableColumn
xScgPtpPmRealChanScgOpt = _XScgPtpPmRealChanScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 1),
    _XScgPtpPmRealChanScgOpt_Type()
)
xScgPtpPmRealChanScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealChanScgOpt.setStatus("current")
_XScgPtpPmRealChanScgOpr_Type = FloatHundredths
_XScgPtpPmRealChanScgOpr_Object = MibTableColumn
xScgPtpPmRealChanScgOpr = _XScgPtpPmRealChanScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 2),
    _XScgPtpPmRealChanScgOpr_Type()
)
xScgPtpPmRealChanScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealChanScgOpr.setStatus("current")
_XScgPtpPmRealTxEdfaOpr_Type = FloatHundredths
_XScgPtpPmRealTxEdfaOpr_Object = MibTableColumn
xScgPtpPmRealTxEdfaOpr = _XScgPtpPmRealTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 3),
    _XScgPtpPmRealTxEdfaOpr_Type()
)
xScgPtpPmRealTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealTxEdfaOpr.setStatus("current")
_XScgPtpPmRealTxEdfaOpt_Type = FloatHundredths
_XScgPtpPmRealTxEdfaOpt_Object = MibTableColumn
xScgPtpPmRealTxEdfaOpt = _XScgPtpPmRealTxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 4),
    _XScgPtpPmRealTxEdfaOpt_Type()
)
xScgPtpPmRealTxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealTxEdfaOpt.setStatus("current")
_XScgPtpPmRealTxEdfaLbc_Type = FloatHundredths
_XScgPtpPmRealTxEdfaLbc_Object = MibTableColumn
xScgPtpPmRealTxEdfaLbc = _XScgPtpPmRealTxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 5),
    _XScgPtpPmRealTxEdfaLbc_Type()
)
xScgPtpPmRealTxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealTxEdfaLbc.setStatus("current")
_XScgPtpPmRealRxEdfaOpr_Type = FloatHundredths
_XScgPtpPmRealRxEdfaOpr_Object = MibTableColumn
xScgPtpPmRealRxEdfaOpr = _XScgPtpPmRealRxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 6),
    _XScgPtpPmRealRxEdfaOpr_Type()
)
xScgPtpPmRealRxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealRxEdfaOpr.setStatus("current")
_XScgPtpPmRealRxEdfaOpt_Type = FloatHundredths
_XScgPtpPmRealRxEdfaOpt_Object = MibTableColumn
xScgPtpPmRealRxEdfaOpt = _XScgPtpPmRealRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 7),
    _XScgPtpPmRealRxEdfaOpt_Type()
)
xScgPtpPmRealRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealRxEdfaOpt.setStatus("current")
_XScgPtpPmRealRxEdfaLbc_Type = FloatHundredths
_XScgPtpPmRealRxEdfaLbc_Object = MibTableColumn
xScgPtpPmRealRxEdfaLbc = _XScgPtpPmRealRxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 1, 1, 8),
    _XScgPtpPmRealRxEdfaLbc_Type()
)
xScgPtpPmRealRxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRealRxEdfaLbc.setStatus("current")
_XScgPtpPmTable_Object = MibTable
xScgPtpPmTable = _XScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2)
)
if mibBuilder.loadTexts:
    xScgPtpPmTable.setStatus("current")
_XScgPtpPmEntry_Object = MibTableRow
xScgPtpPmEntry = _XScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1)
)
xScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmSampleDuration"),
    (0, "INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    xScgPtpPmEntry.setStatus("current")


class _XScgPtpPmTimestamp_Type(Integer32):
    """Custom type xScgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XScgPtpPmTimestamp_Type.__name__ = "Integer32"
_XScgPtpPmTimestamp_Object = MibTableColumn
xScgPtpPmTimestamp = _XScgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 1),
    _XScgPtpPmTimestamp_Type()
)
xScgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xScgPtpPmTimestamp.setStatus("current")


class _XScgPtpPmSampleDuration_Type(Integer32):
    """Custom type xScgPtpPmSampleDuration based on Integer32"""
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


_XScgPtpPmSampleDuration_Type.__name__ = "Integer32"
_XScgPtpPmSampleDuration_Object = MibTableColumn
xScgPtpPmSampleDuration = _XScgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 2),
    _XScgPtpPmSampleDuration_Type()
)
xScgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xScgPtpPmSampleDuration.setStatus("current")
_XScgPtpPmValidity_Type = TruthValue
_XScgPtpPmValidity_Object = MibTableColumn
xScgPtpPmValidity = _XScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 3),
    _XScgPtpPmValidity_Type()
)
xScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmValidity.setStatus("current")
_XScgPtpPmTxEdfaOprMin_Type = FloatHundredths
_XScgPtpPmTxEdfaOprMin_Object = MibTableColumn
xScgPtpPmTxEdfaOprMin = _XScgPtpPmTxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 4),
    _XScgPtpPmTxEdfaOprMin_Type()
)
xScgPtpPmTxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaOprMin.setStatus("current")
_XScgPtpPmTxEdfaOprMax_Type = FloatHundredths
_XScgPtpPmTxEdfaOprMax_Object = MibTableColumn
xScgPtpPmTxEdfaOprMax = _XScgPtpPmTxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 5),
    _XScgPtpPmTxEdfaOprMax_Type()
)
xScgPtpPmTxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaOprMax.setStatus("current")
_XScgPtpPmTxEdfaOprAve_Type = FloatHundredths
_XScgPtpPmTxEdfaOprAve_Object = MibTableColumn
xScgPtpPmTxEdfaOprAve = _XScgPtpPmTxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 6),
    _XScgPtpPmTxEdfaOprAve_Type()
)
xScgPtpPmTxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaOprAve.setStatus("current")
_XScgPtpPmTxEdfaOptMin_Type = FloatHundredths
_XScgPtpPmTxEdfaOptMin_Object = MibTableColumn
xScgPtpPmTxEdfaOptMin = _XScgPtpPmTxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 7),
    _XScgPtpPmTxEdfaOptMin_Type()
)
xScgPtpPmTxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaOptMin.setStatus("current")
_XScgPtpPmTxEdfaOptMax_Type = FloatHundredths
_XScgPtpPmTxEdfaOptMax_Object = MibTableColumn
xScgPtpPmTxEdfaOptMax = _XScgPtpPmTxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 8),
    _XScgPtpPmTxEdfaOptMax_Type()
)
xScgPtpPmTxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaOptMax.setStatus("current")
_XScgPtpPmTxEdfaOptAve_Type = FloatHundredths
_XScgPtpPmTxEdfaOptAve_Object = MibTableColumn
xScgPtpPmTxEdfaOptAve = _XScgPtpPmTxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 9),
    _XScgPtpPmTxEdfaOptAve_Type()
)
xScgPtpPmTxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaOptAve.setStatus("current")
_XScgPtpPmTxEdfaLbcMin_Type = FloatHundredths
_XScgPtpPmTxEdfaLbcMin_Object = MibTableColumn
xScgPtpPmTxEdfaLbcMin = _XScgPtpPmTxEdfaLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 10),
    _XScgPtpPmTxEdfaLbcMin_Type()
)
xScgPtpPmTxEdfaLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaLbcMin.setStatus("current")
_XScgPtpPmTxEdfaLbcMax_Type = FloatHundredths
_XScgPtpPmTxEdfaLbcMax_Object = MibTableColumn
xScgPtpPmTxEdfaLbcMax = _XScgPtpPmTxEdfaLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 11),
    _XScgPtpPmTxEdfaLbcMax_Type()
)
xScgPtpPmTxEdfaLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaLbcMax.setStatus("current")
_XScgPtpPmTxEdfaLbcAve_Type = FloatHundredths
_XScgPtpPmTxEdfaLbcAve_Object = MibTableColumn
xScgPtpPmTxEdfaLbcAve = _XScgPtpPmTxEdfaLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 12),
    _XScgPtpPmTxEdfaLbcAve_Type()
)
xScgPtpPmTxEdfaLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmTxEdfaLbcAve.setStatus("current")
_XScgPtpPmRxEdfaOprMin_Type = FloatHundredths
_XScgPtpPmRxEdfaOprMin_Object = MibTableColumn
xScgPtpPmRxEdfaOprMin = _XScgPtpPmRxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 13),
    _XScgPtpPmRxEdfaOprMin_Type()
)
xScgPtpPmRxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaOprMin.setStatus("current")
_XScgPtpPmRxEdfaOprMax_Type = FloatHundredths
_XScgPtpPmRxEdfaOprMax_Object = MibTableColumn
xScgPtpPmRxEdfaOprMax = _XScgPtpPmRxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 14),
    _XScgPtpPmRxEdfaOprMax_Type()
)
xScgPtpPmRxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaOprMax.setStatus("current")
_XScgPtpPmRxEdfaOprAve_Type = FloatHundredths
_XScgPtpPmRxEdfaOprAve_Object = MibTableColumn
xScgPtpPmRxEdfaOprAve = _XScgPtpPmRxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 15),
    _XScgPtpPmRxEdfaOprAve_Type()
)
xScgPtpPmRxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaOprAve.setStatus("current")
_XScgPtpPmRxEdfaOptMin_Type = FloatHundredths
_XScgPtpPmRxEdfaOptMin_Object = MibTableColumn
xScgPtpPmRxEdfaOptMin = _XScgPtpPmRxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 16),
    _XScgPtpPmRxEdfaOptMin_Type()
)
xScgPtpPmRxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaOptMin.setStatus("current")
_XScgPtpPmRxEdfaOptMax_Type = FloatHundredths
_XScgPtpPmRxEdfaOptMax_Object = MibTableColumn
xScgPtpPmRxEdfaOptMax = _XScgPtpPmRxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 17),
    _XScgPtpPmRxEdfaOptMax_Type()
)
xScgPtpPmRxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaOptMax.setStatus("current")
_XScgPtpPmRxEdfaOptAve_Type = FloatHundredths
_XScgPtpPmRxEdfaOptAve_Object = MibTableColumn
xScgPtpPmRxEdfaOptAve = _XScgPtpPmRxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 18),
    _XScgPtpPmRxEdfaOptAve_Type()
)
xScgPtpPmRxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaOptAve.setStatus("current")
_XScgPtpPmRxEdfaLbcMin_Type = FloatHundredths
_XScgPtpPmRxEdfaLbcMin_Object = MibTableColumn
xScgPtpPmRxEdfaLbcMin = _XScgPtpPmRxEdfaLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 19),
    _XScgPtpPmRxEdfaLbcMin_Type()
)
xScgPtpPmRxEdfaLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaLbcMin.setStatus("current")
_XScgPtpPmRxEdfaLbcMax_Type = FloatHundredths
_XScgPtpPmRxEdfaLbcMax_Object = MibTableColumn
xScgPtpPmRxEdfaLbcMax = _XScgPtpPmRxEdfaLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 20),
    _XScgPtpPmRxEdfaLbcMax_Type()
)
xScgPtpPmRxEdfaLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaLbcMax.setStatus("current")
_XScgPtpPmRxEdfaLbcAve_Type = FloatHundredths
_XScgPtpPmRxEdfaLbcAve_Object = MibTableColumn
xScgPtpPmRxEdfaLbcAve = _XScgPtpPmRxEdfaLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 21),
    _XScgPtpPmRxEdfaLbcAve_Type()
)
xScgPtpPmRxEdfaLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmRxEdfaLbcAve.setStatus("current")
_XScgPtpPmChanScgOptMin_Type = FloatHundredths
_XScgPtpPmChanScgOptMin_Object = MibTableColumn
xScgPtpPmChanScgOptMin = _XScgPtpPmChanScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 22),
    _XScgPtpPmChanScgOptMin_Type()
)
xScgPtpPmChanScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmChanScgOptMin.setStatus("current")
_XScgPtpPmChanScgOptMax_Type = FloatHundredths
_XScgPtpPmChanScgOptMax_Object = MibTableColumn
xScgPtpPmChanScgOptMax = _XScgPtpPmChanScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 23),
    _XScgPtpPmChanScgOptMax_Type()
)
xScgPtpPmChanScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmChanScgOptMax.setStatus("current")
_XScgPtpPmChanScgOptAve_Type = FloatHundredths
_XScgPtpPmChanScgOptAve_Object = MibTableColumn
xScgPtpPmChanScgOptAve = _XScgPtpPmChanScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 24),
    _XScgPtpPmChanScgOptAve_Type()
)
xScgPtpPmChanScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmChanScgOptAve.setStatus("current")
_XScgPtpPmChanScgOprMin_Type = FloatHundredths
_XScgPtpPmChanScgOprMin_Object = MibTableColumn
xScgPtpPmChanScgOprMin = _XScgPtpPmChanScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 25),
    _XScgPtpPmChanScgOprMin_Type()
)
xScgPtpPmChanScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmChanScgOprMin.setStatus("current")
_XScgPtpPmChanScgOprMax_Type = FloatHundredths
_XScgPtpPmChanScgOprMax_Object = MibTableColumn
xScgPtpPmChanScgOprMax = _XScgPtpPmChanScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 26),
    _XScgPtpPmChanScgOprMax_Type()
)
xScgPtpPmChanScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmChanScgOprMax.setStatus("current")
_XScgPtpPmChanScgOprAve_Type = FloatHundredths
_XScgPtpPmChanScgOprAve_Object = MibTableColumn
xScgPtpPmChanScgOprAve = _XScgPtpPmChanScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 2, 1, 27),
    _XScgPtpPmChanScgOprAve_Type()
)
xScgPtpPmChanScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xScgPtpPmChanScgOprAve.setStatus("current")
_XScgPtpPmConformance_ObjectIdentity = ObjectIdentity
xScgPtpPmConformance = _XScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3)
)
_XScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
xScgPtpPmCompliances = _XScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3, 1)
)
_XScgPtpPmGroups_ObjectIdentity = ObjectIdentity
xScgPtpPmGroups = _XScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3, 2)
)

# Managed Objects groups

xScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3, 2, 1)
)
xScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTimestamp"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmSampleDuration"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmValidity"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaOprMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaOprMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaOprAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaOptMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaOptMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaOptAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaLbcMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaLbcMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmTxEdfaLbcAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaOprMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaOprMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaOprAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaOptMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaOptMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaOptAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaLbcMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaLbcMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRxEdfaLbcAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmChanScgOptMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmChanScgOptMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmChanScgOptAve"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmChanScgOprMin"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmChanScgOprMax"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmChanScgOprAve"))
)
if mibBuilder.loadTexts:
    xScgPtpPmGroup.setStatus("current")

xScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3, 2, 2)
)
xScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealChanScgOpt"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealChanScgOpr"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealTxEdfaOpr"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealTxEdfaOpt"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealTxEdfaLbc"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealRxEdfaOpr"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealRxEdfaOpt"),
        ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealRxEdfaLbc"))
)
if mibBuilder.loadTexts:
    xScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3, 1, 1)
)
xScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    xScgPtpPmCompliance.setStatus(
        "current"
    )

xScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 33, 3, 1, 2)
)
xScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-XSCGPTP-MIB", "xScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    xScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-XSCGPTP-MIB",
    **{"xScgPtpPmMIB": xScgPtpPmMIB,
       "xScgPtpPmRealTable": xScgPtpPmRealTable,
       "xScgPtpPmRealEntry": xScgPtpPmRealEntry,
       "xScgPtpPmRealChanScgOpt": xScgPtpPmRealChanScgOpt,
       "xScgPtpPmRealChanScgOpr": xScgPtpPmRealChanScgOpr,
       "xScgPtpPmRealTxEdfaOpr": xScgPtpPmRealTxEdfaOpr,
       "xScgPtpPmRealTxEdfaOpt": xScgPtpPmRealTxEdfaOpt,
       "xScgPtpPmRealTxEdfaLbc": xScgPtpPmRealTxEdfaLbc,
       "xScgPtpPmRealRxEdfaOpr": xScgPtpPmRealRxEdfaOpr,
       "xScgPtpPmRealRxEdfaOpt": xScgPtpPmRealRxEdfaOpt,
       "xScgPtpPmRealRxEdfaLbc": xScgPtpPmRealRxEdfaLbc,
       "xScgPtpPmTable": xScgPtpPmTable,
       "xScgPtpPmEntry": xScgPtpPmEntry,
       "xScgPtpPmTimestamp": xScgPtpPmTimestamp,
       "xScgPtpPmSampleDuration": xScgPtpPmSampleDuration,
       "xScgPtpPmValidity": xScgPtpPmValidity,
       "xScgPtpPmTxEdfaOprMin": xScgPtpPmTxEdfaOprMin,
       "xScgPtpPmTxEdfaOprMax": xScgPtpPmTxEdfaOprMax,
       "xScgPtpPmTxEdfaOprAve": xScgPtpPmTxEdfaOprAve,
       "xScgPtpPmTxEdfaOptMin": xScgPtpPmTxEdfaOptMin,
       "xScgPtpPmTxEdfaOptMax": xScgPtpPmTxEdfaOptMax,
       "xScgPtpPmTxEdfaOptAve": xScgPtpPmTxEdfaOptAve,
       "xScgPtpPmTxEdfaLbcMin": xScgPtpPmTxEdfaLbcMin,
       "xScgPtpPmTxEdfaLbcMax": xScgPtpPmTxEdfaLbcMax,
       "xScgPtpPmTxEdfaLbcAve": xScgPtpPmTxEdfaLbcAve,
       "xScgPtpPmRxEdfaOprMin": xScgPtpPmRxEdfaOprMin,
       "xScgPtpPmRxEdfaOprMax": xScgPtpPmRxEdfaOprMax,
       "xScgPtpPmRxEdfaOprAve": xScgPtpPmRxEdfaOprAve,
       "xScgPtpPmRxEdfaOptMin": xScgPtpPmRxEdfaOptMin,
       "xScgPtpPmRxEdfaOptMax": xScgPtpPmRxEdfaOptMax,
       "xScgPtpPmRxEdfaOptAve": xScgPtpPmRxEdfaOptAve,
       "xScgPtpPmRxEdfaLbcMin": xScgPtpPmRxEdfaLbcMin,
       "xScgPtpPmRxEdfaLbcMax": xScgPtpPmRxEdfaLbcMax,
       "xScgPtpPmRxEdfaLbcAve": xScgPtpPmRxEdfaLbcAve,
       "xScgPtpPmChanScgOptMin": xScgPtpPmChanScgOptMin,
       "xScgPtpPmChanScgOptMax": xScgPtpPmChanScgOptMax,
       "xScgPtpPmChanScgOptAve": xScgPtpPmChanScgOptAve,
       "xScgPtpPmChanScgOprMin": xScgPtpPmChanScgOprMin,
       "xScgPtpPmChanScgOprMax": xScgPtpPmChanScgOprMax,
       "xScgPtpPmChanScgOprAve": xScgPtpPmChanScgOprAve,
       "xScgPtpPmConformance": xScgPtpPmConformance,
       "xScgPtpPmCompliances": xScgPtpPmCompliances,
       "xScgPtpPmCompliance": xScgPtpPmCompliance,
       "xScgPtpPmRealCompliance": xScgPtpPmRealCompliance,
       "xScgPtpPmGroups": xScgPtpPmGroups,
       "xScgPtpPmGroup": xScgPtpPmGroup,
       "xScgPtpPmRealGroup": xScgPtpPmRealGroup}
)
