# SNMP MIB module (INFINERA-PM-FBMSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FBMSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:48 2025
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

(FloatArbitraryPrecision,
 InfnSampleDuration) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
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

fbmScgptpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83)
)
if mibBuilder.loadTexts:
    fbmScgptpPmMIB.setRevisions(
        ("2017-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbmScgptpPmRealTable_Object = MibTable
fbmScgptpPmRealTable = _FbmScgptpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 1)
)
if mibBuilder.loadTexts:
    fbmScgptpPmRealTable.setStatus("current")
_FbmScgptpPmRealEntry_Object = MibTableRow
fbmScgptpPmRealEntry = _FbmScgptpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 1, 1)
)
fbmScgptpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fbmScgptpPmRealEntry.setStatus("current")
_FbmScgptpPmRealCmnScgOpt_Type = FloatArbitraryPrecision
_FbmScgptpPmRealCmnScgOpt_Object = MibTableColumn
fbmScgptpPmRealCmnScgOpt = _FbmScgptpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 1, 1, 1),
    _FbmScgptpPmRealCmnScgOpt_Type()
)
fbmScgptpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmRealCmnScgOpt.setStatus("current")
_FbmScgptpPmRealCmnScgOpr_Type = FloatArbitraryPrecision
_FbmScgptpPmRealCmnScgOpr_Object = MibTableColumn
fbmScgptpPmRealCmnScgOpr = _FbmScgptpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 1, 1, 2),
    _FbmScgptpPmRealCmnScgOpr_Type()
)
fbmScgptpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmRealCmnScgOpr.setStatus("current")
_FbmScgptpPmTable_Object = MibTable
fbmScgptpPmTable = _FbmScgptpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2)
)
if mibBuilder.loadTexts:
    fbmScgptpPmTable.setStatus("current")
_FbmScgptpPmEntry_Object = MibTableRow
fbmScgptpPmEntry = _FbmScgptpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1)
)
fbmScgptpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmSampleDuration"),
    (0, "INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmTimestamp"),
)
if mibBuilder.loadTexts:
    fbmScgptpPmEntry.setStatus("current")


class _FbmScgptpPmTimestamp_Type(Integer32):
    """Custom type fbmScgptpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FbmScgptpPmTimestamp_Type.__name__ = "Integer32"
_FbmScgptpPmTimestamp_Object = MibTableColumn
fbmScgptpPmTimestamp = _FbmScgptpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 1),
    _FbmScgptpPmTimestamp_Type()
)
fbmScgptpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbmScgptpPmTimestamp.setStatus("current")
_FbmScgptpPmSampleDuration_Type = InfnSampleDuration
_FbmScgptpPmSampleDuration_Object = MibTableColumn
fbmScgptpPmSampleDuration = _FbmScgptpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 2),
    _FbmScgptpPmSampleDuration_Type()
)
fbmScgptpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbmScgptpPmSampleDuration.setStatus("current")
_FbmScgptpPmValidity_Type = TruthValue
_FbmScgptpPmValidity_Object = MibTableColumn
fbmScgptpPmValidity = _FbmScgptpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 3),
    _FbmScgptpPmValidity_Type()
)
fbmScgptpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmValidity.setStatus("current")
_FbmScgptpPmCmnScgOptMin_Type = FloatArbitraryPrecision
_FbmScgptpPmCmnScgOptMin_Object = MibTableColumn
fbmScgptpPmCmnScgOptMin = _FbmScgptpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 4),
    _FbmScgptpPmCmnScgOptMin_Type()
)
fbmScgptpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmCmnScgOptMin.setStatus("current")
_FbmScgptpPmCmnScgOptMax_Type = FloatArbitraryPrecision
_FbmScgptpPmCmnScgOptMax_Object = MibTableColumn
fbmScgptpPmCmnScgOptMax = _FbmScgptpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 5),
    _FbmScgptpPmCmnScgOptMax_Type()
)
fbmScgptpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmCmnScgOptMax.setStatus("current")
_FbmScgptpPmCmnScgOptAve_Type = FloatArbitraryPrecision
_FbmScgptpPmCmnScgOptAve_Object = MibTableColumn
fbmScgptpPmCmnScgOptAve = _FbmScgptpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 6),
    _FbmScgptpPmCmnScgOptAve_Type()
)
fbmScgptpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmCmnScgOptAve.setStatus("current")
_FbmScgptpPmCmnScgOprMin_Type = FloatArbitraryPrecision
_FbmScgptpPmCmnScgOprMin_Object = MibTableColumn
fbmScgptpPmCmnScgOprMin = _FbmScgptpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 7),
    _FbmScgptpPmCmnScgOprMin_Type()
)
fbmScgptpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmCmnScgOprMin.setStatus("current")
_FbmScgptpPmCmnScgOprMax_Type = FloatArbitraryPrecision
_FbmScgptpPmCmnScgOprMax_Object = MibTableColumn
fbmScgptpPmCmnScgOprMax = _FbmScgptpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 8),
    _FbmScgptpPmCmnScgOprMax_Type()
)
fbmScgptpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmCmnScgOprMax.setStatus("current")
_FbmScgptpPmCmnScgOprAve_Type = FloatArbitraryPrecision
_FbmScgptpPmCmnScgOprAve_Object = MibTableColumn
fbmScgptpPmCmnScgOprAve = _FbmScgptpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 2, 1, 9),
    _FbmScgptpPmCmnScgOprAve_Type()
)
fbmScgptpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbmScgptpPmCmnScgOprAve.setStatus("current")
_FbmScgptpPmConformance_ObjectIdentity = ObjectIdentity
fbmScgptpPmConformance = _FbmScgptpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3)
)
_FbmScgptpPmCompliances_ObjectIdentity = ObjectIdentity
fbmScgptpPmCompliances = _FbmScgptpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3, 1)
)
_FbmScgptpPmGroups_ObjectIdentity = ObjectIdentity
fbmScgptpPmGroups = _FbmScgptpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3, 2)
)

# Managed Objects groups

fbmScgptpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3, 2, 1)
)
fbmScgptpPmGroup.setObjects(
      *(("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmTimestamp"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmSampleDuration"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmValidity"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmCmnScgOptMin"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmCmnScgOptMax"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmCmnScgOptAve"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmCmnScgOprMin"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmCmnScgOprMax"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmCmnScgOprAve"))
)
if mibBuilder.loadTexts:
    fbmScgptpPmGroup.setStatus("current")

fbmScgptpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3, 2, 2)
)
fbmScgptpPmRealGroup.setObjects(
      *(("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmRealCmnScgOpt"),
        ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmRealCmnScgOpr"))
)
if mibBuilder.loadTexts:
    fbmScgptpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fbmScgptpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3, 1, 1)
)
fbmScgptpPmCompliance.setObjects(
    ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmGroup")
)
if mibBuilder.loadTexts:
    fbmScgptpPmCompliance.setStatus(
        "current"
    )

fbmScgptpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 83, 3, 1, 2)
)
fbmScgptpPmRealCompliance.setObjects(
    ("INFINERA-PM-FBMSCGPTP-MIB", "fbmScgptpPmRealGroup")
)
if mibBuilder.loadTexts:
    fbmScgptpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FBMSCGPTP-MIB",
    **{"fbmScgptpPmMIB": fbmScgptpPmMIB,
       "fbmScgptpPmRealTable": fbmScgptpPmRealTable,
       "fbmScgptpPmRealEntry": fbmScgptpPmRealEntry,
       "fbmScgptpPmRealCmnScgOpt": fbmScgptpPmRealCmnScgOpt,
       "fbmScgptpPmRealCmnScgOpr": fbmScgptpPmRealCmnScgOpr,
       "fbmScgptpPmTable": fbmScgptpPmTable,
       "fbmScgptpPmEntry": fbmScgptpPmEntry,
       "fbmScgptpPmTimestamp": fbmScgptpPmTimestamp,
       "fbmScgptpPmSampleDuration": fbmScgptpPmSampleDuration,
       "fbmScgptpPmValidity": fbmScgptpPmValidity,
       "fbmScgptpPmCmnScgOptMin": fbmScgptpPmCmnScgOptMin,
       "fbmScgptpPmCmnScgOptMax": fbmScgptpPmCmnScgOptMax,
       "fbmScgptpPmCmnScgOptAve": fbmScgptpPmCmnScgOptAve,
       "fbmScgptpPmCmnScgOprMin": fbmScgptpPmCmnScgOprMin,
       "fbmScgptpPmCmnScgOprMax": fbmScgptpPmCmnScgOprMax,
       "fbmScgptpPmCmnScgOprAve": fbmScgptpPmCmnScgOprAve,
       "fbmScgptpPmConformance": fbmScgptpPmConformance,
       "fbmScgptpPmCompliances": fbmScgptpPmCompliances,
       "fbmScgptpPmCompliance": fbmScgptpPmCompliance,
       "fbmScgptpPmRealCompliance": fbmScgptpPmRealCompliance,
       "fbmScgptpPmGroups": fbmScgptpPmGroups,
       "fbmScgptpPmGroup": fbmScgptpPmGroup,
       "fbmScgptpPmRealGroup": fbmScgptpPmRealGroup}
)
