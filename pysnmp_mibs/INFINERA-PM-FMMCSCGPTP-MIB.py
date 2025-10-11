# SNMP MIB module (INFINERA-PM-FMMCSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FMMCSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:22 2025
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

(FloatHundredths,
 InfnSampleDuration) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnSampleDuration")

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

fmmcScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43)
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmMIB.setRevisions(
        ("2015-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FmmcScgPtpPmRealTable_Object = MibTable
fmmcScgPtpPmRealTable = _FmmcScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1)
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealTable.setStatus("current")
_FmmcScgPtpPmRealEntry_Object = MibTableRow
fmmcScgPtpPmRealEntry = _FmmcScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1)
)
fmmcScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealEntry.setStatus("current")
_FmmcScgPtpPmRealCmnScgOpt_Type = FloatHundredths
_FmmcScgPtpPmRealCmnScgOpt_Object = MibTableColumn
fmmcScgPtpPmRealCmnScgOpt = _FmmcScgPtpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 1),
    _FmmcScgPtpPmRealCmnScgOpt_Type()
)
fmmcScgPtpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealCmnScgOpt.setStatus("current")
_FmmcScgPtpPmRealCmnScgOpr_Type = FloatHundredths
_FmmcScgPtpPmRealCmnScgOpr_Object = MibTableColumn
fmmcScgPtpPmRealCmnScgOpr = _FmmcScgPtpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 2),
    _FmmcScgPtpPmRealCmnScgOpr_Type()
)
fmmcScgPtpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealCmnScgOpr.setStatus("current")
_FmmcScgPtpPmRealOptOsaTapRatio_Type = FloatHundredths
_FmmcScgPtpPmRealOptOsaTapRatio_Object = MibTableColumn
fmmcScgPtpPmRealOptOsaTapRatio = _FmmcScgPtpPmRealOptOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 3),
    _FmmcScgPtpPmRealOptOsaTapRatio_Type()
)
fmmcScgPtpPmRealOptOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealOptOsaTapRatio.setStatus("current")
_FmmcScgPtpPmRealOprOsaTapRatio_Type = FloatHundredths
_FmmcScgPtpPmRealOprOsaTapRatio_Object = MibTableColumn
fmmcScgPtpPmRealOprOsaTapRatio = _FmmcScgPtpPmRealOprOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 4),
    _FmmcScgPtpPmRealOprOsaTapRatio_Type()
)
fmmcScgPtpPmRealOprOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealOprOsaTapRatio.setStatus("current")
_FmmcScgPtpPmRealTxEdfaOpr_Type = FloatHundredths
_FmmcScgPtpPmRealTxEdfaOpr_Object = MibTableColumn
fmmcScgPtpPmRealTxEdfaOpr = _FmmcScgPtpPmRealTxEdfaOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 5),
    _FmmcScgPtpPmRealTxEdfaOpr_Type()
)
fmmcScgPtpPmRealTxEdfaOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealTxEdfaOpr.setStatus("current")
_FmmcScgPtpPmRealRxEdfaOpt_Type = FloatHundredths
_FmmcScgPtpPmRealRxEdfaOpt_Object = MibTableColumn
fmmcScgPtpPmRealRxEdfaOpt = _FmmcScgPtpPmRealRxEdfaOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 6),
    _FmmcScgPtpPmRealRxEdfaOpt_Type()
)
fmmcScgPtpPmRealRxEdfaOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealRxEdfaOpt.setStatus("current")
_FmmcScgPtpPmRealEdfaLbcTx_Type = FloatHundredths
_FmmcScgPtpPmRealEdfaLbcTx_Object = MibTableColumn
fmmcScgPtpPmRealEdfaLbcTx = _FmmcScgPtpPmRealEdfaLbcTx_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 7),
    _FmmcScgPtpPmRealEdfaLbcTx_Type()
)
fmmcScgPtpPmRealEdfaLbcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealEdfaLbcTx.setStatus("current")
_FmmcScgPtpPmRealRxEdfaLbc_Type = FloatHundredths
_FmmcScgPtpPmRealRxEdfaLbc_Object = MibTableColumn
fmmcScgPtpPmRealRxEdfaLbc = _FmmcScgPtpPmRealRxEdfaLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 1, 1, 8),
    _FmmcScgPtpPmRealRxEdfaLbc_Type()
)
fmmcScgPtpPmRealRxEdfaLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealRxEdfaLbc.setStatus("current")
_FmmcScgPtpPmTable_Object = MibTable
fmmcScgPtpPmTable = _FmmcScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2)
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmTable.setStatus("current")
_FmmcScgPtpPmEntry_Object = MibTableRow
fmmcScgPtpPmEntry = _FmmcScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1)
)
fmmcScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmSampleDuration"),
    (0, "INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmEntry.setStatus("current")


class _FmmcScgPtpPmTimestamp_Type(Integer32):
    """Custom type fmmcScgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FmmcScgPtpPmTimestamp_Type.__name__ = "Integer32"
_FmmcScgPtpPmTimestamp_Object = MibTableColumn
fmmcScgPtpPmTimestamp = _FmmcScgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 1),
    _FmmcScgPtpPmTimestamp_Type()
)
fmmcScgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmmcScgPtpPmTimestamp.setStatus("current")


class _FmmcScgPtpPmSampleDuration_Type(Integer32):
    """Custom type fmmcScgPtpPmSampleDuration based on Integer32"""
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


_FmmcScgPtpPmSampleDuration_Type.__name__ = "Integer32"
_FmmcScgPtpPmSampleDuration_Object = MibTableColumn
fmmcScgPtpPmSampleDuration = _FmmcScgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 2),
    _FmmcScgPtpPmSampleDuration_Type()
)
fmmcScgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmmcScgPtpPmSampleDuration.setStatus("current")
_FmmcScgPtpPmValidity_Type = TruthValue
_FmmcScgPtpPmValidity_Object = MibTableColumn
fmmcScgPtpPmValidity = _FmmcScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 3),
    _FmmcScgPtpPmValidity_Type()
)
fmmcScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmValidity.setStatus("current")
_FmmcScgPtpPmCmnScgOptMin_Type = FloatHundredths
_FmmcScgPtpPmCmnScgOptMin_Object = MibTableColumn
fmmcScgPtpPmCmnScgOptMin = _FmmcScgPtpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 4),
    _FmmcScgPtpPmCmnScgOptMin_Type()
)
fmmcScgPtpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmCmnScgOptMin.setStatus("current")
_FmmcScgPtpPmCmnScgOptMax_Type = FloatHundredths
_FmmcScgPtpPmCmnScgOptMax_Object = MibTableColumn
fmmcScgPtpPmCmnScgOptMax = _FmmcScgPtpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 5),
    _FmmcScgPtpPmCmnScgOptMax_Type()
)
fmmcScgPtpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmCmnScgOptMax.setStatus("current")
_FmmcScgPtpPmCmnScgOptAve_Type = FloatHundredths
_FmmcScgPtpPmCmnScgOptAve_Object = MibTableColumn
fmmcScgPtpPmCmnScgOptAve = _FmmcScgPtpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 6),
    _FmmcScgPtpPmCmnScgOptAve_Type()
)
fmmcScgPtpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmCmnScgOptAve.setStatus("current")
_FmmcScgPtpPmCmnScgOprMin_Type = FloatHundredths
_FmmcScgPtpPmCmnScgOprMin_Object = MibTableColumn
fmmcScgPtpPmCmnScgOprMin = _FmmcScgPtpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 7),
    _FmmcScgPtpPmCmnScgOprMin_Type()
)
fmmcScgPtpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmCmnScgOprMin.setStatus("current")
_FmmcScgPtpPmCmnScgOprMax_Type = FloatHundredths
_FmmcScgPtpPmCmnScgOprMax_Object = MibTableColumn
fmmcScgPtpPmCmnScgOprMax = _FmmcScgPtpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 8),
    _FmmcScgPtpPmCmnScgOprMax_Type()
)
fmmcScgPtpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmCmnScgOprMax.setStatus("current")
_FmmcScgPtpPmCmnScgOprAve_Type = FloatHundredths
_FmmcScgPtpPmCmnScgOprAve_Object = MibTableColumn
fmmcScgPtpPmCmnScgOprAve = _FmmcScgPtpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 9),
    _FmmcScgPtpPmCmnScgOprAve_Type()
)
fmmcScgPtpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmCmnScgOprAve.setStatus("current")
_FmmcScgPtpPmTxEdfaOprMin_Type = FloatHundredths
_FmmcScgPtpPmTxEdfaOprMin_Object = MibTableColumn
fmmcScgPtpPmTxEdfaOprMin = _FmmcScgPtpPmTxEdfaOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 10),
    _FmmcScgPtpPmTxEdfaOprMin_Type()
)
fmmcScgPtpPmTxEdfaOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmTxEdfaOprMin.setStatus("current")
_FmmcScgPtpPmTxEdfaOprMax_Type = FloatHundredths
_FmmcScgPtpPmTxEdfaOprMax_Object = MibTableColumn
fmmcScgPtpPmTxEdfaOprMax = _FmmcScgPtpPmTxEdfaOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 11),
    _FmmcScgPtpPmTxEdfaOprMax_Type()
)
fmmcScgPtpPmTxEdfaOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmTxEdfaOprMax.setStatus("current")
_FmmcScgPtpPmTxEdfaOprAve_Type = FloatHundredths
_FmmcScgPtpPmTxEdfaOprAve_Object = MibTableColumn
fmmcScgPtpPmTxEdfaOprAve = _FmmcScgPtpPmTxEdfaOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 12),
    _FmmcScgPtpPmTxEdfaOprAve_Type()
)
fmmcScgPtpPmTxEdfaOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmTxEdfaOprAve.setStatus("current")
_FmmcScgPtpPmRxEdfaOptMin_Type = FloatHundredths
_FmmcScgPtpPmRxEdfaOptMin_Object = MibTableColumn
fmmcScgPtpPmRxEdfaOptMin = _FmmcScgPtpPmRxEdfaOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 13),
    _FmmcScgPtpPmRxEdfaOptMin_Type()
)
fmmcScgPtpPmRxEdfaOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRxEdfaOptMin.setStatus("current")
_FmmcScgPtpPmRxEdfaOptMax_Type = FloatHundredths
_FmmcScgPtpPmRxEdfaOptMax_Object = MibTableColumn
fmmcScgPtpPmRxEdfaOptMax = _FmmcScgPtpPmRxEdfaOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 14),
    _FmmcScgPtpPmRxEdfaOptMax_Type()
)
fmmcScgPtpPmRxEdfaOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRxEdfaOptMax.setStatus("current")
_FmmcScgPtpPmRxEdfaOptAve_Type = FloatHundredths
_FmmcScgPtpPmRxEdfaOptAve_Object = MibTableColumn
fmmcScgPtpPmRxEdfaOptAve = _FmmcScgPtpPmRxEdfaOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 2, 1, 15),
    _FmmcScgPtpPmRxEdfaOptAve_Type()
)
fmmcScgPtpPmRxEdfaOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmcScgPtpPmRxEdfaOptAve.setStatus("current")
_FmmcScgPtpPmConformance_ObjectIdentity = ObjectIdentity
fmmcScgPtpPmConformance = _FmmcScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3)
)
_FmmcScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
fmmcScgPtpPmCompliances = _FmmcScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3, 1)
)
_FmmcScgPtpPmGroups_ObjectIdentity = ObjectIdentity
fmmcScgPtpPmGroups = _FmmcScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3, 2)
)

# Managed Objects groups

fmmcScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3, 2, 1)
)
fmmcScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmTimestamp"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmSampleDuration"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmValidity"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmCmnScgOptMin"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmCmnScgOptMax"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmCmnScgOptAve"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmCmnScgOprMin"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmCmnScgOprMax"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmCmnScgOprAve"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmTxEdfaOprMin"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmTxEdfaOprMax"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmTxEdfaOprAve"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRxEdfaOptMin"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRxEdfaOptMax"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRxEdfaOptAve"))
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmGroup.setStatus("current")

fmmcScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3, 2, 2)
)
fmmcScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealCmnScgOpt"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealCmnScgOpr"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealOptOsaTapRatio"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealOprOsaTapRatio"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealTxEdfaOpr"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealRxEdfaOpt"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealEdfaLbcTx"),
        ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealRxEdfaLbc"))
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmmcScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3, 1, 1)
)
fmmcScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmCompliance.setStatus(
        "current"
    )

fmmcScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 43, 3, 1, 2)
)
fmmcScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-FMMCSCGPTP-MIB", "fmmcScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    fmmcScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FMMCSCGPTP-MIB",
    **{"fmmcScgPtpPmMIB": fmmcScgPtpPmMIB,
       "fmmcScgPtpPmRealTable": fmmcScgPtpPmRealTable,
       "fmmcScgPtpPmRealEntry": fmmcScgPtpPmRealEntry,
       "fmmcScgPtpPmRealCmnScgOpt": fmmcScgPtpPmRealCmnScgOpt,
       "fmmcScgPtpPmRealCmnScgOpr": fmmcScgPtpPmRealCmnScgOpr,
       "fmmcScgPtpPmRealOptOsaTapRatio": fmmcScgPtpPmRealOptOsaTapRatio,
       "fmmcScgPtpPmRealOprOsaTapRatio": fmmcScgPtpPmRealOprOsaTapRatio,
       "fmmcScgPtpPmRealTxEdfaOpr": fmmcScgPtpPmRealTxEdfaOpr,
       "fmmcScgPtpPmRealRxEdfaOpt": fmmcScgPtpPmRealRxEdfaOpt,
       "fmmcScgPtpPmRealEdfaLbcTx": fmmcScgPtpPmRealEdfaLbcTx,
       "fmmcScgPtpPmRealRxEdfaLbc": fmmcScgPtpPmRealRxEdfaLbc,
       "fmmcScgPtpPmTable": fmmcScgPtpPmTable,
       "fmmcScgPtpPmEntry": fmmcScgPtpPmEntry,
       "fmmcScgPtpPmTimestamp": fmmcScgPtpPmTimestamp,
       "fmmcScgPtpPmSampleDuration": fmmcScgPtpPmSampleDuration,
       "fmmcScgPtpPmValidity": fmmcScgPtpPmValidity,
       "fmmcScgPtpPmCmnScgOptMin": fmmcScgPtpPmCmnScgOptMin,
       "fmmcScgPtpPmCmnScgOptMax": fmmcScgPtpPmCmnScgOptMax,
       "fmmcScgPtpPmCmnScgOptAve": fmmcScgPtpPmCmnScgOptAve,
       "fmmcScgPtpPmCmnScgOprMin": fmmcScgPtpPmCmnScgOprMin,
       "fmmcScgPtpPmCmnScgOprMax": fmmcScgPtpPmCmnScgOprMax,
       "fmmcScgPtpPmCmnScgOprAve": fmmcScgPtpPmCmnScgOprAve,
       "fmmcScgPtpPmTxEdfaOprMin": fmmcScgPtpPmTxEdfaOprMin,
       "fmmcScgPtpPmTxEdfaOprMax": fmmcScgPtpPmTxEdfaOprMax,
       "fmmcScgPtpPmTxEdfaOprAve": fmmcScgPtpPmTxEdfaOprAve,
       "fmmcScgPtpPmRxEdfaOptMin": fmmcScgPtpPmRxEdfaOptMin,
       "fmmcScgPtpPmRxEdfaOptMax": fmmcScgPtpPmRxEdfaOptMax,
       "fmmcScgPtpPmRxEdfaOptAve": fmmcScgPtpPmRxEdfaOptAve,
       "fmmcScgPtpPmConformance": fmmcScgPtpPmConformance,
       "fmmcScgPtpPmCompliances": fmmcScgPtpPmCompliances,
       "fmmcScgPtpPmCompliance": fmmcScgPtpPmCompliance,
       "fmmcScgPtpPmRealCompliance": fmmcScgPtpPmRealCompliance,
       "fmmcScgPtpPmGroups": fmmcScgPtpPmGroups,
       "fmmcScgPtpPmGroup": fmmcScgPtpPmGroup,
       "fmmcScgPtpPmRealGroup": fmmcScgPtpPmRealGroup}
)
