# SNMP MIB module (INFINERA-PM-XOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-XOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:23 2025
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

xOcgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42)
)
if mibBuilder.loadTexts:
    xOcgPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XOcgPtpPmRealTable_Object = MibTable
xOcgPtpPmRealTable = _XOcgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1)
)
if mibBuilder.loadTexts:
    xOcgPtpPmRealTable.setStatus("current")
_XOcgPtpPmRealEntry_Object = MibTableRow
xOcgPtpPmRealEntry = _XOcgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1)
)
xOcgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xOcgPtpPmRealEntry.setStatus("current")
_XOcgPtpPmRealDlmOcgOpt_Type = FloatHundredths
_XOcgPtpPmRealDlmOcgOpt_Object = MibTableColumn
xOcgPtpPmRealDlmOcgOpt = _XOcgPtpPmRealDlmOcgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 1),
    _XOcgPtpPmRealDlmOcgOpt_Type()
)
xOcgPtpPmRealDlmOcgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealDlmOcgOpt.setStatus("current")
_XOcgPtpPmRealDlmOcgOpr_Type = FloatHundredths
_XOcgPtpPmRealDlmOcgOpr_Object = MibTableColumn
xOcgPtpPmRealDlmOcgOpr = _XOcgPtpPmRealDlmOcgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 2),
    _XOcgPtpPmRealDlmOcgOpr_Type()
)
xOcgPtpPmRealDlmOcgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealDlmOcgOpr.setStatus("current")
_XOcgPtpPmRealTxEdfaOpr_Type = FloatHundredths
_XOcgPtpPmRealTxEdfaOpr_Object = MibTableColumn
xOcgPtpPmRealTxEdfaOpr = _XOcgPtpPmRealTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 3),
    _XOcgPtpPmRealTxEdfaOpr_Type()
)
xOcgPtpPmRealTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealTxEdfaOpr.setStatus("current")
_XOcgPtpPmRealTxEdfaOpt_Type = FloatHundredths
_XOcgPtpPmRealTxEdfaOpt_Object = MibTableColumn
xOcgPtpPmRealTxEdfaOpt = _XOcgPtpPmRealTxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 4),
    _XOcgPtpPmRealTxEdfaOpt_Type()
)
xOcgPtpPmRealTxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealTxEdfaOpt.setStatus("current")
_XOcgPtpPmRealTxEdfaLbc_Type = FloatHundredths
_XOcgPtpPmRealTxEdfaLbc_Object = MibTableColumn
xOcgPtpPmRealTxEdfaLbc = _XOcgPtpPmRealTxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 5),
    _XOcgPtpPmRealTxEdfaLbc_Type()
)
xOcgPtpPmRealTxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealTxEdfaLbc.setStatus("current")
_XOcgPtpPmRealRxEdfaOpr_Type = FloatHundredths
_XOcgPtpPmRealRxEdfaOpr_Object = MibTableColumn
xOcgPtpPmRealRxEdfaOpr = _XOcgPtpPmRealRxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 6),
    _XOcgPtpPmRealRxEdfaOpr_Type()
)
xOcgPtpPmRealRxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealRxEdfaOpr.setStatus("current")
_XOcgPtpPmRealRxEdfaOpt_Type = FloatHundredths
_XOcgPtpPmRealRxEdfaOpt_Object = MibTableColumn
xOcgPtpPmRealRxEdfaOpt = _XOcgPtpPmRealRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 7),
    _XOcgPtpPmRealRxEdfaOpt_Type()
)
xOcgPtpPmRealRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealRxEdfaOpt.setStatus("current")
_XOcgPtpPmRealRxEdfaLbc_Type = FloatHundredths
_XOcgPtpPmRealRxEdfaLbc_Object = MibTableColumn
xOcgPtpPmRealRxEdfaLbc = _XOcgPtpPmRealRxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 1, 1, 8),
    _XOcgPtpPmRealRxEdfaLbc_Type()
)
xOcgPtpPmRealRxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRealRxEdfaLbc.setStatus("current")
_XOcgPtpPmTable_Object = MibTable
xOcgPtpPmTable = _XOcgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2)
)
if mibBuilder.loadTexts:
    xOcgPtpPmTable.setStatus("current")
_XOcgPtpPmEntry_Object = MibTableRow
xOcgPtpPmEntry = _XOcgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1)
)
xOcgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmSampleDuration"),
    (0, "INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    xOcgPtpPmEntry.setStatus("current")


class _XOcgPtpPmTimestamp_Type(Integer32):
    """Custom type xOcgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XOcgPtpPmTimestamp_Type.__name__ = "Integer32"
_XOcgPtpPmTimestamp_Object = MibTableColumn
xOcgPtpPmTimestamp = _XOcgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 1),
    _XOcgPtpPmTimestamp_Type()
)
xOcgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xOcgPtpPmTimestamp.setStatus("current")


class _XOcgPtpPmSampleDuration_Type(Integer32):
    """Custom type xOcgPtpPmSampleDuration based on Integer32"""
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


_XOcgPtpPmSampleDuration_Type.__name__ = "Integer32"
_XOcgPtpPmSampleDuration_Object = MibTableColumn
xOcgPtpPmSampleDuration = _XOcgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 2),
    _XOcgPtpPmSampleDuration_Type()
)
xOcgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xOcgPtpPmSampleDuration.setStatus("current")
_XOcgPtpPmTxEdfaOprMin_Type = FloatHundredths
_XOcgPtpPmTxEdfaOprMin_Object = MibTableColumn
xOcgPtpPmTxEdfaOprMin = _XOcgPtpPmTxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 3),
    _XOcgPtpPmTxEdfaOprMin_Type()
)
xOcgPtpPmTxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaOprMin.setStatus("current")
_XOcgPtpPmTxEdfaOprMax_Type = FloatHundredths
_XOcgPtpPmTxEdfaOprMax_Object = MibTableColumn
xOcgPtpPmTxEdfaOprMax = _XOcgPtpPmTxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 4),
    _XOcgPtpPmTxEdfaOprMax_Type()
)
xOcgPtpPmTxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaOprMax.setStatus("current")
_XOcgPtpPmTxEdfaOprAve_Type = FloatHundredths
_XOcgPtpPmTxEdfaOprAve_Object = MibTableColumn
xOcgPtpPmTxEdfaOprAve = _XOcgPtpPmTxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 5),
    _XOcgPtpPmTxEdfaOprAve_Type()
)
xOcgPtpPmTxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaOprAve.setStatus("current")
_XOcgPtpPmTxEdfaOptMin_Type = FloatHundredths
_XOcgPtpPmTxEdfaOptMin_Object = MibTableColumn
xOcgPtpPmTxEdfaOptMin = _XOcgPtpPmTxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 6),
    _XOcgPtpPmTxEdfaOptMin_Type()
)
xOcgPtpPmTxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaOptMin.setStatus("current")
_XOcgPtpPmTxEdfaOptMax_Type = FloatHundredths
_XOcgPtpPmTxEdfaOptMax_Object = MibTableColumn
xOcgPtpPmTxEdfaOptMax = _XOcgPtpPmTxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 7),
    _XOcgPtpPmTxEdfaOptMax_Type()
)
xOcgPtpPmTxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaOptMax.setStatus("current")
_XOcgPtpPmTxEdfaOptAve_Type = FloatHundredths
_XOcgPtpPmTxEdfaOptAve_Object = MibTableColumn
xOcgPtpPmTxEdfaOptAve = _XOcgPtpPmTxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 8),
    _XOcgPtpPmTxEdfaOptAve_Type()
)
xOcgPtpPmTxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaOptAve.setStatus("current")
_XOcgPtpPmTxEdfaLbcMin_Type = FloatHundredths
_XOcgPtpPmTxEdfaLbcMin_Object = MibTableColumn
xOcgPtpPmTxEdfaLbcMin = _XOcgPtpPmTxEdfaLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 9),
    _XOcgPtpPmTxEdfaLbcMin_Type()
)
xOcgPtpPmTxEdfaLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaLbcMin.setStatus("current")
_XOcgPtpPmTxEdfaLbcMax_Type = FloatHundredths
_XOcgPtpPmTxEdfaLbcMax_Object = MibTableColumn
xOcgPtpPmTxEdfaLbcMax = _XOcgPtpPmTxEdfaLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 10),
    _XOcgPtpPmTxEdfaLbcMax_Type()
)
xOcgPtpPmTxEdfaLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaLbcMax.setStatus("current")
_XOcgPtpPmTxEdfaLbcAve_Type = FloatHundredths
_XOcgPtpPmTxEdfaLbcAve_Object = MibTableColumn
xOcgPtpPmTxEdfaLbcAve = _XOcgPtpPmTxEdfaLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 11),
    _XOcgPtpPmTxEdfaLbcAve_Type()
)
xOcgPtpPmTxEdfaLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmTxEdfaLbcAve.setStatus("current")
_XOcgPtpPmRxEdfaOprMin_Type = FloatHundredths
_XOcgPtpPmRxEdfaOprMin_Object = MibTableColumn
xOcgPtpPmRxEdfaOprMin = _XOcgPtpPmRxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 12),
    _XOcgPtpPmRxEdfaOprMin_Type()
)
xOcgPtpPmRxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaOprMin.setStatus("current")
_XOcgPtpPmRxEdfaOprMax_Type = FloatHundredths
_XOcgPtpPmRxEdfaOprMax_Object = MibTableColumn
xOcgPtpPmRxEdfaOprMax = _XOcgPtpPmRxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 13),
    _XOcgPtpPmRxEdfaOprMax_Type()
)
xOcgPtpPmRxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaOprMax.setStatus("current")
_XOcgPtpPmRxEdfaOprAve_Type = FloatHundredths
_XOcgPtpPmRxEdfaOprAve_Object = MibTableColumn
xOcgPtpPmRxEdfaOprAve = _XOcgPtpPmRxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 14),
    _XOcgPtpPmRxEdfaOprAve_Type()
)
xOcgPtpPmRxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaOprAve.setStatus("current")
_XOcgPtpPmRxEdfaOptMin_Type = FloatHundredths
_XOcgPtpPmRxEdfaOptMin_Object = MibTableColumn
xOcgPtpPmRxEdfaOptMin = _XOcgPtpPmRxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 15),
    _XOcgPtpPmRxEdfaOptMin_Type()
)
xOcgPtpPmRxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaOptMin.setStatus("current")
_XOcgPtpPmRxEdfaOptMax_Type = FloatHundredths
_XOcgPtpPmRxEdfaOptMax_Object = MibTableColumn
xOcgPtpPmRxEdfaOptMax = _XOcgPtpPmRxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 16),
    _XOcgPtpPmRxEdfaOptMax_Type()
)
xOcgPtpPmRxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaOptMax.setStatus("current")
_XOcgPtpPmRxEdfaOptAve_Type = FloatHundredths
_XOcgPtpPmRxEdfaOptAve_Object = MibTableColumn
xOcgPtpPmRxEdfaOptAve = _XOcgPtpPmRxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 17),
    _XOcgPtpPmRxEdfaOptAve_Type()
)
xOcgPtpPmRxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaOptAve.setStatus("current")
_XOcgPtpPmRxEdfaLbcMin_Type = FloatHundredths
_XOcgPtpPmRxEdfaLbcMin_Object = MibTableColumn
xOcgPtpPmRxEdfaLbcMin = _XOcgPtpPmRxEdfaLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 18),
    _XOcgPtpPmRxEdfaLbcMin_Type()
)
xOcgPtpPmRxEdfaLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaLbcMin.setStatus("current")
_XOcgPtpPmRxEdfaLbcMax_Type = FloatHundredths
_XOcgPtpPmRxEdfaLbcMax_Object = MibTableColumn
xOcgPtpPmRxEdfaLbcMax = _XOcgPtpPmRxEdfaLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 19),
    _XOcgPtpPmRxEdfaLbcMax_Type()
)
xOcgPtpPmRxEdfaLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaLbcMax.setStatus("current")
_XOcgPtpPmRxEdfaLbcAve_Type = FloatHundredths
_XOcgPtpPmRxEdfaLbcAve_Object = MibTableColumn
xOcgPtpPmRxEdfaLbcAve = _XOcgPtpPmRxEdfaLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 20),
    _XOcgPtpPmRxEdfaLbcAve_Type()
)
xOcgPtpPmRxEdfaLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmRxEdfaLbcAve.setStatus("current")
_XOcgPtpPmValidity_Type = TruthValue
_XOcgPtpPmValidity_Object = MibTableColumn
xOcgPtpPmValidity = _XOcgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 2, 1, 21),
    _XOcgPtpPmValidity_Type()
)
xOcgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xOcgPtpPmValidity.setStatus("current")
_XOcgPtpPmConformance_ObjectIdentity = ObjectIdentity
xOcgPtpPmConformance = _XOcgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3)
)
_XOcgPtpPmCompliances_ObjectIdentity = ObjectIdentity
xOcgPtpPmCompliances = _XOcgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3, 1)
)
_XOcgPtpPmGroups_ObjectIdentity = ObjectIdentity
xOcgPtpPmGroups = _XOcgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3, 2)
)

# Managed Objects groups

xOcgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3, 2, 1)
)
xOcgPtpPmGroup.setObjects(
      *(("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaOprMin"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaOprMax"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaOprAve"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaOptMin"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaOptMax"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaOptAve"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaLbcMin"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaLbcMax"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmTxEdfaLbcAve"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaOprMin"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaOprMax"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaOprAve"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaOptMin"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaOptMax"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaOptAve"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaLbcMin"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaLbcMax"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRxEdfaLbcAve"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmValidity"))
)
if mibBuilder.loadTexts:
    xOcgPtpPmGroup.setStatus("current")

xOcgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3, 2, 2)
)
xOcgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealDlmOcgOpt"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealDlmOcgOpr"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealTxEdfaOpr"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealTxEdfaOpt"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealTxEdfaLbc"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealRxEdfaOpr"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealRxEdfaOpt"),
        ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealRxEdfaLbc"))
)
if mibBuilder.loadTexts:
    xOcgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xOcgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3, 1, 1)
)
xOcgPtpPmCompliance.setObjects(
    ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmGroup")
)
if mibBuilder.loadTexts:
    xOcgPtpPmCompliance.setStatus(
        "current"
    )

xOcgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 42, 3, 1, 2)
)
xOcgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-XOCGPTP-MIB", "xOcgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    xOcgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-XOCGPTP-MIB",
    **{"xOcgPtpPmMIB": xOcgPtpPmMIB,
       "xOcgPtpPmRealTable": xOcgPtpPmRealTable,
       "xOcgPtpPmRealEntry": xOcgPtpPmRealEntry,
       "xOcgPtpPmRealDlmOcgOpt": xOcgPtpPmRealDlmOcgOpt,
       "xOcgPtpPmRealDlmOcgOpr": xOcgPtpPmRealDlmOcgOpr,
       "xOcgPtpPmRealTxEdfaOpr": xOcgPtpPmRealTxEdfaOpr,
       "xOcgPtpPmRealTxEdfaOpt": xOcgPtpPmRealTxEdfaOpt,
       "xOcgPtpPmRealTxEdfaLbc": xOcgPtpPmRealTxEdfaLbc,
       "xOcgPtpPmRealRxEdfaOpr": xOcgPtpPmRealRxEdfaOpr,
       "xOcgPtpPmRealRxEdfaOpt": xOcgPtpPmRealRxEdfaOpt,
       "xOcgPtpPmRealRxEdfaLbc": xOcgPtpPmRealRxEdfaLbc,
       "xOcgPtpPmTable": xOcgPtpPmTable,
       "xOcgPtpPmEntry": xOcgPtpPmEntry,
       "xOcgPtpPmTimestamp": xOcgPtpPmTimestamp,
       "xOcgPtpPmSampleDuration": xOcgPtpPmSampleDuration,
       "xOcgPtpPmTxEdfaOprMin": xOcgPtpPmTxEdfaOprMin,
       "xOcgPtpPmTxEdfaOprMax": xOcgPtpPmTxEdfaOprMax,
       "xOcgPtpPmTxEdfaOprAve": xOcgPtpPmTxEdfaOprAve,
       "xOcgPtpPmTxEdfaOptMin": xOcgPtpPmTxEdfaOptMin,
       "xOcgPtpPmTxEdfaOptMax": xOcgPtpPmTxEdfaOptMax,
       "xOcgPtpPmTxEdfaOptAve": xOcgPtpPmTxEdfaOptAve,
       "xOcgPtpPmTxEdfaLbcMin": xOcgPtpPmTxEdfaLbcMin,
       "xOcgPtpPmTxEdfaLbcMax": xOcgPtpPmTxEdfaLbcMax,
       "xOcgPtpPmTxEdfaLbcAve": xOcgPtpPmTxEdfaLbcAve,
       "xOcgPtpPmRxEdfaOprMin": xOcgPtpPmRxEdfaOprMin,
       "xOcgPtpPmRxEdfaOprMax": xOcgPtpPmRxEdfaOprMax,
       "xOcgPtpPmRxEdfaOprAve": xOcgPtpPmRxEdfaOprAve,
       "xOcgPtpPmRxEdfaOptMin": xOcgPtpPmRxEdfaOptMin,
       "xOcgPtpPmRxEdfaOptMax": xOcgPtpPmRxEdfaOptMax,
       "xOcgPtpPmRxEdfaOptAve": xOcgPtpPmRxEdfaOptAve,
       "xOcgPtpPmRxEdfaLbcMin": xOcgPtpPmRxEdfaLbcMin,
       "xOcgPtpPmRxEdfaLbcMax": xOcgPtpPmRxEdfaLbcMax,
       "xOcgPtpPmRxEdfaLbcAve": xOcgPtpPmRxEdfaLbcAve,
       "xOcgPtpPmValidity": xOcgPtpPmValidity,
       "xOcgPtpPmConformance": xOcgPtpPmConformance,
       "xOcgPtpPmCompliances": xOcgPtpPmCompliances,
       "xOcgPtpPmCompliance": xOcgPtpPmCompliance,
       "xOcgPtpPmRealCompliance": xOcgPtpPmRealCompliance,
       "xOcgPtpPmGroups": xOcgPtpPmGroups,
       "xOcgPtpPmGroup": xOcgPtpPmGroup,
       "xOcgPtpPmRealGroup": xOcgPtpPmRealGroup}
)
