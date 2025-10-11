# SNMP MIB module (INFINERA-PM-CMMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-CMMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:42 2025
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

cmmOcgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25)
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmMIB.setRevisions(
        ("2011-05-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmmOcgPtpPmRealTable_Object = MibTable
cmmOcgPtpPmRealTable = _CmmOcgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 1)
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealTable.setStatus("current")
_CmmOcgPtpPmRealEntry_Object = MibTableRow
cmmOcgPtpPmRealEntry = _CmmOcgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 1, 1)
)
cmmOcgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealEntry.setStatus("current")
_CmmOcgPtpPmRealCmmOcgOpt_Type = FloatHundredths
_CmmOcgPtpPmRealCmmOcgOpt_Object = MibTableColumn
cmmOcgPtpPmRealCmmOcgOpt = _CmmOcgPtpPmRealCmmOcgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 1, 1, 1),
    _CmmOcgPtpPmRealCmmOcgOpt_Type()
)
cmmOcgPtpPmRealCmmOcgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealCmmOcgOpt.setStatus("current")
_CmmOcgPtpPmRealCmmOcgOpr_Type = FloatHundredths
_CmmOcgPtpPmRealCmmOcgOpr_Object = MibTableColumn
cmmOcgPtpPmRealCmmOcgOpr = _CmmOcgPtpPmRealCmmOcgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 1, 1, 2),
    _CmmOcgPtpPmRealCmmOcgOpr_Type()
)
cmmOcgPtpPmRealCmmOcgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealCmmOcgOpr.setStatus("current")
_CmmOcgPtpPmRealCmmEdfaLbcTx_Type = FloatHundredths
_CmmOcgPtpPmRealCmmEdfaLbcTx_Object = MibTableColumn
cmmOcgPtpPmRealCmmEdfaLbcTx = _CmmOcgPtpPmRealCmmEdfaLbcTx_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 1, 1, 3),
    _CmmOcgPtpPmRealCmmEdfaLbcTx_Type()
)
cmmOcgPtpPmRealCmmEdfaLbcTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealCmmEdfaLbcTx.setStatus("current")
_CmmOcgPtpPmTable_Object = MibTable
cmmOcgPtpPmTable = _CmmOcgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2)
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmTable.setStatus("current")
_CmmOcgPtpPmEntry_Object = MibTableRow
cmmOcgPtpPmEntry = _CmmOcgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1)
)
cmmOcgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmSampleDuration"),
    (0, "INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmEntry.setStatus("current")


class _CmmOcgPtpPmTimestamp_Type(Integer32):
    """Custom type cmmOcgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CmmOcgPtpPmTimestamp_Type.__name__ = "Integer32"
_CmmOcgPtpPmTimestamp_Object = MibTableColumn
cmmOcgPtpPmTimestamp = _CmmOcgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 1),
    _CmmOcgPtpPmTimestamp_Type()
)
cmmOcgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmOcgPtpPmTimestamp.setStatus("current")


class _CmmOcgPtpPmSampleDuration_Type(Integer32):
    """Custom type cmmOcgPtpPmSampleDuration based on Integer32"""
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


_CmmOcgPtpPmSampleDuration_Type.__name__ = "Integer32"
_CmmOcgPtpPmSampleDuration_Object = MibTableColumn
cmmOcgPtpPmSampleDuration = _CmmOcgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 2),
    _CmmOcgPtpPmSampleDuration_Type()
)
cmmOcgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmmOcgPtpPmSampleDuration.setStatus("current")
_CmmOcgPtpPmValidity_Type = TruthValue
_CmmOcgPtpPmValidity_Object = MibTableColumn
cmmOcgPtpPmValidity = _CmmOcgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 3),
    _CmmOcgPtpPmValidity_Type()
)
cmmOcgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmValidity.setStatus("current")
_CmmOcgPtpPmCmmOcgOptMin_Type = FloatHundredths
_CmmOcgPtpPmCmmOcgOptMin_Object = MibTableColumn
cmmOcgPtpPmCmmOcgOptMin = _CmmOcgPtpPmCmmOcgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 4),
    _CmmOcgPtpPmCmmOcgOptMin_Type()
)
cmmOcgPtpPmCmmOcgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmOcgOptMin.setStatus("current")
_CmmOcgPtpPmCmmOcgOptMax_Type = FloatHundredths
_CmmOcgPtpPmCmmOcgOptMax_Object = MibTableColumn
cmmOcgPtpPmCmmOcgOptMax = _CmmOcgPtpPmCmmOcgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 5),
    _CmmOcgPtpPmCmmOcgOptMax_Type()
)
cmmOcgPtpPmCmmOcgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmOcgOptMax.setStatus("current")
_CmmOcgPtpPmCmmOcgOptAve_Type = FloatHundredths
_CmmOcgPtpPmCmmOcgOptAve_Object = MibTableColumn
cmmOcgPtpPmCmmOcgOptAve = _CmmOcgPtpPmCmmOcgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 6),
    _CmmOcgPtpPmCmmOcgOptAve_Type()
)
cmmOcgPtpPmCmmOcgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmOcgOptAve.setStatus("current")
_CmmOcgPtpPmCmmOcgOprMin_Type = FloatHundredths
_CmmOcgPtpPmCmmOcgOprMin_Object = MibTableColumn
cmmOcgPtpPmCmmOcgOprMin = _CmmOcgPtpPmCmmOcgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 7),
    _CmmOcgPtpPmCmmOcgOprMin_Type()
)
cmmOcgPtpPmCmmOcgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmOcgOprMin.setStatus("current")
_CmmOcgPtpPmCmmOcgOprMax_Type = FloatHundredths
_CmmOcgPtpPmCmmOcgOprMax_Object = MibTableColumn
cmmOcgPtpPmCmmOcgOprMax = _CmmOcgPtpPmCmmOcgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 8),
    _CmmOcgPtpPmCmmOcgOprMax_Type()
)
cmmOcgPtpPmCmmOcgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmOcgOprMax.setStatus("current")
_CmmOcgPtpPmCmmOcgOprAve_Type = FloatHundredths
_CmmOcgPtpPmCmmOcgOprAve_Object = MibTableColumn
cmmOcgPtpPmCmmOcgOprAve = _CmmOcgPtpPmCmmOcgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 9),
    _CmmOcgPtpPmCmmOcgOprAve_Type()
)
cmmOcgPtpPmCmmOcgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmOcgOprAve.setStatus("current")
_CmmOcgPtpPmCmmEdfaLbcTxMin_Type = FloatHundredths
_CmmOcgPtpPmCmmEdfaLbcTxMin_Object = MibTableColumn
cmmOcgPtpPmCmmEdfaLbcTxMin = _CmmOcgPtpPmCmmEdfaLbcTxMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 10),
    _CmmOcgPtpPmCmmEdfaLbcTxMin_Type()
)
cmmOcgPtpPmCmmEdfaLbcTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmEdfaLbcTxMin.setStatus("current")
_CmmOcgPtpPmCmmEdfaLbcTxMax_Type = FloatHundredths
_CmmOcgPtpPmCmmEdfaLbcTxMax_Object = MibTableColumn
cmmOcgPtpPmCmmEdfaLbcTxMax = _CmmOcgPtpPmCmmEdfaLbcTxMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 11),
    _CmmOcgPtpPmCmmEdfaLbcTxMax_Type()
)
cmmOcgPtpPmCmmEdfaLbcTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmEdfaLbcTxMax.setStatus("current")
_CmmOcgPtpPmCmmEdfaLbcTxAve_Type = FloatHundredths
_CmmOcgPtpPmCmmEdfaLbcTxAve_Object = MibTableColumn
cmmOcgPtpPmCmmEdfaLbcTxAve = _CmmOcgPtpPmCmmEdfaLbcTxAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 2, 1, 12),
    _CmmOcgPtpPmCmmEdfaLbcTxAve_Type()
)
cmmOcgPtpPmCmmEdfaLbcTxAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmOcgPtpPmCmmEdfaLbcTxAve.setStatus("current")
_CmmOcgPtpPmConformance_ObjectIdentity = ObjectIdentity
cmmOcgPtpPmConformance = _CmmOcgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3)
)
_CmmOcgPtpPmCompliances_ObjectIdentity = ObjectIdentity
cmmOcgPtpPmCompliances = _CmmOcgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3, 1)
)
_CmmOcgPtpPmGroups_ObjectIdentity = ObjectIdentity
cmmOcgPtpPmGroups = _CmmOcgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3, 2)
)

# Managed Objects groups

cmmOcgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3, 2, 1)
)
cmmOcgPtpPmGroup.setObjects(
      *(("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmValidity"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmOcgOptMin"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmOcgOptMax"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmOcgOptAve"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmOcgOprMin"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmOcgOprMax"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmOcgOprAve"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmEdfaLbcTxMin"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmEdfaLbcTxMax"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmCmmEdfaLbcTxAve"))
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmGroup.setStatus("current")

cmmOcgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3, 2, 2)
)
cmmOcgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmRealCmmOcgOpt"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmRealCmmOcgOpr"),
        ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmRealCmmEdfaLbcTx"))
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmmOcgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3, 1, 1)
)
cmmOcgPtpPmCompliance.setObjects(
    ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmGroup")
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmCompliance.setStatus(
        "current"
    )

cmmOcgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 25, 3, 1, 2)
)
cmmOcgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-CMMOCGPTP-MIB", "cmmOcgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    cmmOcgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-CMMOCGPTP-MIB",
    **{"cmmOcgPtpPmMIB": cmmOcgPtpPmMIB,
       "cmmOcgPtpPmRealTable": cmmOcgPtpPmRealTable,
       "cmmOcgPtpPmRealEntry": cmmOcgPtpPmRealEntry,
       "cmmOcgPtpPmRealCmmOcgOpt": cmmOcgPtpPmRealCmmOcgOpt,
       "cmmOcgPtpPmRealCmmOcgOpr": cmmOcgPtpPmRealCmmOcgOpr,
       "cmmOcgPtpPmRealCmmEdfaLbcTx": cmmOcgPtpPmRealCmmEdfaLbcTx,
       "cmmOcgPtpPmTable": cmmOcgPtpPmTable,
       "cmmOcgPtpPmEntry": cmmOcgPtpPmEntry,
       "cmmOcgPtpPmTimestamp": cmmOcgPtpPmTimestamp,
       "cmmOcgPtpPmSampleDuration": cmmOcgPtpPmSampleDuration,
       "cmmOcgPtpPmValidity": cmmOcgPtpPmValidity,
       "cmmOcgPtpPmCmmOcgOptMin": cmmOcgPtpPmCmmOcgOptMin,
       "cmmOcgPtpPmCmmOcgOptMax": cmmOcgPtpPmCmmOcgOptMax,
       "cmmOcgPtpPmCmmOcgOptAve": cmmOcgPtpPmCmmOcgOptAve,
       "cmmOcgPtpPmCmmOcgOprMin": cmmOcgPtpPmCmmOcgOprMin,
       "cmmOcgPtpPmCmmOcgOprMax": cmmOcgPtpPmCmmOcgOprMax,
       "cmmOcgPtpPmCmmOcgOprAve": cmmOcgPtpPmCmmOcgOprAve,
       "cmmOcgPtpPmCmmEdfaLbcTxMin": cmmOcgPtpPmCmmEdfaLbcTxMin,
       "cmmOcgPtpPmCmmEdfaLbcTxMax": cmmOcgPtpPmCmmEdfaLbcTxMax,
       "cmmOcgPtpPmCmmEdfaLbcTxAve": cmmOcgPtpPmCmmEdfaLbcTxAve,
       "cmmOcgPtpPmConformance": cmmOcgPtpPmConformance,
       "cmmOcgPtpPmCompliances": cmmOcgPtpPmCompliances,
       "cmmOcgPtpPmCompliance": cmmOcgPtpPmCompliance,
       "cmmOcgPtpPmRealCompliance": cmmOcgPtpPmRealCompliance,
       "cmmOcgPtpPmGroups": cmmOcgPtpPmGroups,
       "cmmOcgPtpPmGroup": cmmOcgPtpPmGroup,
       "cmmOcgPtpPmRealGroup": cmmOcgPtpPmRealGroup}
)
