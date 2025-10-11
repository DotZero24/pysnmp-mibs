# SNMP MIB module (INFINERA-PM-FMMFSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FMMFSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:49 2025
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

fmmfScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49)
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmMIB.setRevisions(
        ("2015-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FmmfScgPtpPmRealTable_Object = MibTable
fmmfScgPtpPmRealTable = _FmmfScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 1)
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealTable.setStatus("current")
_FmmfScgPtpPmRealEntry_Object = MibTableRow
fmmfScgPtpPmRealEntry = _FmmfScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 1, 1)
)
fmmfScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealEntry.setStatus("current")
_FmmfScgPtpPmRealCmnScgOpt_Type = FloatHundredths
_FmmfScgPtpPmRealCmnScgOpt_Object = MibTableColumn
fmmfScgPtpPmRealCmnScgOpt = _FmmfScgPtpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 1, 1, 1),
    _FmmfScgPtpPmRealCmnScgOpt_Type()
)
fmmfScgPtpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealCmnScgOpt.setStatus("current")
_FmmfScgPtpPmRealCmnScgOpr_Type = FloatHundredths
_FmmfScgPtpPmRealCmnScgOpr_Object = MibTableColumn
fmmfScgPtpPmRealCmnScgOpr = _FmmfScgPtpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 1, 1, 2),
    _FmmfScgPtpPmRealCmnScgOpr_Type()
)
fmmfScgPtpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealCmnScgOpr.setStatus("current")
_FmmfScgPtpPmRealOptOsaTapRatio_Type = FloatHundredths
_FmmfScgPtpPmRealOptOsaTapRatio_Object = MibTableColumn
fmmfScgPtpPmRealOptOsaTapRatio = _FmmfScgPtpPmRealOptOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 1, 1, 3),
    _FmmfScgPtpPmRealOptOsaTapRatio_Type()
)
fmmfScgPtpPmRealOptOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealOptOsaTapRatio.setStatus("current")
_FmmfScgPtpPmTable_Object = MibTable
fmmfScgPtpPmTable = _FmmfScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2)
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmTable.setStatus("current")
_FmmfScgPtpPmEntry_Object = MibTableRow
fmmfScgPtpPmEntry = _FmmfScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1)
)
fmmfScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmSampleDuration"),
    (0, "INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmEntry.setStatus("current")


class _FmmfScgPtpPmTimestamp_Type(Integer32):
    """Custom type fmmfScgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FmmfScgPtpPmTimestamp_Type.__name__ = "Integer32"
_FmmfScgPtpPmTimestamp_Object = MibTableColumn
fmmfScgPtpPmTimestamp = _FmmfScgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 1),
    _FmmfScgPtpPmTimestamp_Type()
)
fmmfScgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmmfScgPtpPmTimestamp.setStatus("current")


class _FmmfScgPtpPmSampleDuration_Type(Integer32):
    """Custom type fmmfScgPtpPmSampleDuration based on Integer32"""
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


_FmmfScgPtpPmSampleDuration_Type.__name__ = "Integer32"
_FmmfScgPtpPmSampleDuration_Object = MibTableColumn
fmmfScgPtpPmSampleDuration = _FmmfScgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 2),
    _FmmfScgPtpPmSampleDuration_Type()
)
fmmfScgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fmmfScgPtpPmSampleDuration.setStatus("current")
_FmmfScgPtpPmValidity_Type = TruthValue
_FmmfScgPtpPmValidity_Object = MibTableColumn
fmmfScgPtpPmValidity = _FmmfScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 3),
    _FmmfScgPtpPmValidity_Type()
)
fmmfScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmValidity.setStatus("current")
_FmmfScgPtpPmCmnScgOptMin_Type = FloatHundredths
_FmmfScgPtpPmCmnScgOptMin_Object = MibTableColumn
fmmfScgPtpPmCmnScgOptMin = _FmmfScgPtpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 4),
    _FmmfScgPtpPmCmnScgOptMin_Type()
)
fmmfScgPtpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmCmnScgOptMin.setStatus("current")
_FmmfScgPtpPmCmnScgOptMax_Type = FloatHundredths
_FmmfScgPtpPmCmnScgOptMax_Object = MibTableColumn
fmmfScgPtpPmCmnScgOptMax = _FmmfScgPtpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 5),
    _FmmfScgPtpPmCmnScgOptMax_Type()
)
fmmfScgPtpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmCmnScgOptMax.setStatus("current")
_FmmfScgPtpPmCmnScgOptAve_Type = FloatHundredths
_FmmfScgPtpPmCmnScgOptAve_Object = MibTableColumn
fmmfScgPtpPmCmnScgOptAve = _FmmfScgPtpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 6),
    _FmmfScgPtpPmCmnScgOptAve_Type()
)
fmmfScgPtpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmCmnScgOptAve.setStatus("current")
_FmmfScgPtpPmCmnScgOprMin_Type = FloatHundredths
_FmmfScgPtpPmCmnScgOprMin_Object = MibTableColumn
fmmfScgPtpPmCmnScgOprMin = _FmmfScgPtpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 7),
    _FmmfScgPtpPmCmnScgOprMin_Type()
)
fmmfScgPtpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmCmnScgOprMin.setStatus("current")
_FmmfScgPtpPmCmnScgOprMax_Type = FloatHundredths
_FmmfScgPtpPmCmnScgOprMax_Object = MibTableColumn
fmmfScgPtpPmCmnScgOprMax = _FmmfScgPtpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 8),
    _FmmfScgPtpPmCmnScgOprMax_Type()
)
fmmfScgPtpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmCmnScgOprMax.setStatus("current")
_FmmfScgPtpPmCmnScgOprAve_Type = FloatHundredths
_FmmfScgPtpPmCmnScgOprAve_Object = MibTableColumn
fmmfScgPtpPmCmnScgOprAve = _FmmfScgPtpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 9),
    _FmmfScgPtpPmCmnScgOprAve_Type()
)
fmmfScgPtpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmCmnScgOprAve.setStatus("current")
_FmmfScgPtpPmOptOsaTapRatioMin_Type = FloatHundredths
_FmmfScgPtpPmOptOsaTapRatioMin_Object = MibTableColumn
fmmfScgPtpPmOptOsaTapRatioMin = _FmmfScgPtpPmOptOsaTapRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 10),
    _FmmfScgPtpPmOptOsaTapRatioMin_Type()
)
fmmfScgPtpPmOptOsaTapRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmOptOsaTapRatioMin.setStatus("current")
_FmmfScgPtpPmOptOsaTapRatioMax_Type = FloatHundredths
_FmmfScgPtpPmOptOsaTapRatioMax_Object = MibTableColumn
fmmfScgPtpPmOptOsaTapRatioMax = _FmmfScgPtpPmOptOsaTapRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 11),
    _FmmfScgPtpPmOptOsaTapRatioMax_Type()
)
fmmfScgPtpPmOptOsaTapRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmOptOsaTapRatioMax.setStatus("current")
_FmmfScgPtpPmOptOsaTapRatioAve_Type = FloatHundredths
_FmmfScgPtpPmOptOsaTapRatioAve_Object = MibTableColumn
fmmfScgPtpPmOptOsaTapRatioAve = _FmmfScgPtpPmOptOsaTapRatioAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 2, 1, 12),
    _FmmfScgPtpPmOptOsaTapRatioAve_Type()
)
fmmfScgPtpPmOptOsaTapRatioAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fmmfScgPtpPmOptOsaTapRatioAve.setStatus("current")
_FmmfScgPtpPmConformance_ObjectIdentity = ObjectIdentity
fmmfScgPtpPmConformance = _FmmfScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3)
)
_FmmfScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
fmmfScgPtpPmCompliances = _FmmfScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3, 1)
)
_FmmfScgPtpPmGroups_ObjectIdentity = ObjectIdentity
fmmfScgPtpPmGroups = _FmmfScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3, 2)
)

# Managed Objects groups

fmmfScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3, 2, 1)
)
fmmfScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmTimestamp"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmSampleDuration"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmValidity"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmCmnScgOptMin"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmCmnScgOptMax"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmCmnScgOptAve"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmCmnScgOprMin"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmCmnScgOprMax"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmCmnScgOprAve"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmOptOsaTapRatioMin"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmOptOsaTapRatioMax"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmOptOsaTapRatioAve"))
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmGroup.setStatus("current")

fmmfScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3, 2, 2)
)
fmmfScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmRealCmnScgOpt"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmRealCmnScgOpr"),
        ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmRealOptOsaTapRatio"))
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmmfScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3, 1, 1)
)
fmmfScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmCompliance.setStatus(
        "current"
    )

fmmfScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 49, 3, 1, 2)
)
fmmfScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-FMMFSCGPTP-MIB", "fmmfScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    fmmfScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FMMFSCGPTP-MIB",
    **{"fmmfScgPtpPmMIB": fmmfScgPtpPmMIB,
       "fmmfScgPtpPmRealTable": fmmfScgPtpPmRealTable,
       "fmmfScgPtpPmRealEntry": fmmfScgPtpPmRealEntry,
       "fmmfScgPtpPmRealCmnScgOpt": fmmfScgPtpPmRealCmnScgOpt,
       "fmmfScgPtpPmRealCmnScgOpr": fmmfScgPtpPmRealCmnScgOpr,
       "fmmfScgPtpPmRealOptOsaTapRatio": fmmfScgPtpPmRealOptOsaTapRatio,
       "fmmfScgPtpPmTable": fmmfScgPtpPmTable,
       "fmmfScgPtpPmEntry": fmmfScgPtpPmEntry,
       "fmmfScgPtpPmTimestamp": fmmfScgPtpPmTimestamp,
       "fmmfScgPtpPmSampleDuration": fmmfScgPtpPmSampleDuration,
       "fmmfScgPtpPmValidity": fmmfScgPtpPmValidity,
       "fmmfScgPtpPmCmnScgOptMin": fmmfScgPtpPmCmnScgOptMin,
       "fmmfScgPtpPmCmnScgOptMax": fmmfScgPtpPmCmnScgOptMax,
       "fmmfScgPtpPmCmnScgOptAve": fmmfScgPtpPmCmnScgOptAve,
       "fmmfScgPtpPmCmnScgOprMin": fmmfScgPtpPmCmnScgOprMin,
       "fmmfScgPtpPmCmnScgOprMax": fmmfScgPtpPmCmnScgOprMax,
       "fmmfScgPtpPmCmnScgOprAve": fmmfScgPtpPmCmnScgOprAve,
       "fmmfScgPtpPmOptOsaTapRatioMin": fmmfScgPtpPmOptOsaTapRatioMin,
       "fmmfScgPtpPmOptOsaTapRatioMax": fmmfScgPtpPmOptOsaTapRatioMax,
       "fmmfScgPtpPmOptOsaTapRatioAve": fmmfScgPtpPmOptOsaTapRatioAve,
       "fmmfScgPtpPmConformance": fmmfScgPtpPmConformance,
       "fmmfScgPtpPmCompliances": fmmfScgPtpPmCompliances,
       "fmmfScgPtpPmCompliance": fmmfScgPtpPmCompliance,
       "fmmfScgPtpPmRealCompliance": fmmfScgPtpPmRealCompliance,
       "fmmfScgPtpPmGroups": fmmfScgPtpPmGroups,
       "fmmfScgPtpPmGroup": fmmfScgPtpPmGroup,
       "fmmfScgPtpPmRealGroup": fmmfScgPtpPmRealGroup}
)
