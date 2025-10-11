# SNMP MIB module (INFINERA-PM-BASESCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-BASESCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:21 2025
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

baseScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45)
)
if mibBuilder.loadTexts:
    baseScgPtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BaseScgPtpPmRealTable_Object = MibTable
baseScgPtpPmRealTable = _BaseScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1)
)
if mibBuilder.loadTexts:
    baseScgPtpPmRealTable.setStatus("current")
_BaseScgPtpPmRealEntry_Object = MibTableRow
baseScgPtpPmRealEntry = _BaseScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1, 1)
)
baseScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baseScgPtpPmRealEntry.setStatus("current")
_BaseScgPtpPmRealCmnScgOpt_Type = FloatHundredths
_BaseScgPtpPmRealCmnScgOpt_Object = MibTableColumn
baseScgPtpPmRealCmnScgOpt = _BaseScgPtpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1, 1, 1),
    _BaseScgPtpPmRealCmnScgOpt_Type()
)
baseScgPtpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmRealCmnScgOpt.setStatus("current")
_BaseScgPtpPmRealCmnScgOpr_Type = FloatHundredths
_BaseScgPtpPmRealCmnScgOpr_Object = MibTableColumn
baseScgPtpPmRealCmnScgOpr = _BaseScgPtpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 1, 1, 2),
    _BaseScgPtpPmRealCmnScgOpr_Type()
)
baseScgPtpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmRealCmnScgOpr.setStatus("current")
_BaseScgPtpPmTable_Object = MibTable
baseScgPtpPmTable = _BaseScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2)
)
if mibBuilder.loadTexts:
    baseScgPtpPmTable.setStatus("current")
_BaseScgPtpPmEntry_Object = MibTableRow
baseScgPtpPmEntry = _BaseScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1)
)
baseScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    baseScgPtpPmEntry.setStatus("current")
_BaseScgPtpPmValidity_Type = TruthValue
_BaseScgPtpPmValidity_Object = MibTableColumn
baseScgPtpPmValidity = _BaseScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 3),
    _BaseScgPtpPmValidity_Type()
)
baseScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmValidity.setStatus("current")
_BaseScgPtpPmCmnScgOptMin_Type = FloatHundredths
_BaseScgPtpPmCmnScgOptMin_Object = MibTableColumn
baseScgPtpPmCmnScgOptMin = _BaseScgPtpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 4),
    _BaseScgPtpPmCmnScgOptMin_Type()
)
baseScgPtpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmCmnScgOptMin.setStatus("current")
_BaseScgPtpPmCmnScgOptMax_Type = FloatHundredths
_BaseScgPtpPmCmnScgOptMax_Object = MibTableColumn
baseScgPtpPmCmnScgOptMax = _BaseScgPtpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 5),
    _BaseScgPtpPmCmnScgOptMax_Type()
)
baseScgPtpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmCmnScgOptMax.setStatus("current")
_BaseScgPtpPmCmnScgOptAve_Type = FloatHundredths
_BaseScgPtpPmCmnScgOptAve_Object = MibTableColumn
baseScgPtpPmCmnScgOptAve = _BaseScgPtpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 6),
    _BaseScgPtpPmCmnScgOptAve_Type()
)
baseScgPtpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmCmnScgOptAve.setStatus("current")
_BaseScgPtpPmCmnScgOprMin_Type = FloatHundredths
_BaseScgPtpPmCmnScgOprMin_Object = MibTableColumn
baseScgPtpPmCmnScgOprMin = _BaseScgPtpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 7),
    _BaseScgPtpPmCmnScgOprMin_Type()
)
baseScgPtpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmCmnScgOprMin.setStatus("current")
_BaseScgPtpPmCmnScgOprMax_Type = FloatHundredths
_BaseScgPtpPmCmnScgOprMax_Object = MibTableColumn
baseScgPtpPmCmnScgOprMax = _BaseScgPtpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 8),
    _BaseScgPtpPmCmnScgOprMax_Type()
)
baseScgPtpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmCmnScgOprMax.setStatus("current")
_BaseScgPtpPmCmnScgOprAve_Type = FloatHundredths
_BaseScgPtpPmCmnScgOprAve_Object = MibTableColumn
baseScgPtpPmCmnScgOprAve = _BaseScgPtpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 2, 1, 9),
    _BaseScgPtpPmCmnScgOprAve_Type()
)
baseScgPtpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    baseScgPtpPmCmnScgOprAve.setStatus("current")
_BaseScgPtpPmConformance_ObjectIdentity = ObjectIdentity
baseScgPtpPmConformance = _BaseScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3)
)
_BaseScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
baseScgPtpPmCompliances = _BaseScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 1)
)
_BaseScgPtpPmGroups_ObjectIdentity = ObjectIdentity
baseScgPtpPmGroups = _BaseScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 2)
)

# Managed Objects groups

baseScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 2, 1)
)
baseScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmValidity"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOptMin"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOptMax"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOptAve"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOprMin"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOprMax"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmCmnScgOprAve"))
)
if mibBuilder.loadTexts:
    baseScgPtpPmGroup.setStatus("current")

baseScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 2, 2)
)
baseScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmRealCmnScgOpt"),
        ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmRealCmnScgOpr"))
)
if mibBuilder.loadTexts:
    baseScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

baseScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 1, 1)
)
baseScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    baseScgPtpPmCompliance.setStatus(
        "current"
    )

baseScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 45, 3, 1, 2)
)
baseScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-BASESCGPTP-MIB", "baseScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    baseScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-BASESCGPTP-MIB",
    **{"baseScgPtpPmMIB": baseScgPtpPmMIB,
       "baseScgPtpPmRealTable": baseScgPtpPmRealTable,
       "baseScgPtpPmRealEntry": baseScgPtpPmRealEntry,
       "baseScgPtpPmRealCmnScgOpt": baseScgPtpPmRealCmnScgOpt,
       "baseScgPtpPmRealCmnScgOpr": baseScgPtpPmRealCmnScgOpr,
       "baseScgPtpPmTable": baseScgPtpPmTable,
       "baseScgPtpPmEntry": baseScgPtpPmEntry,
       "baseScgPtpPmValidity": baseScgPtpPmValidity,
       "baseScgPtpPmCmnScgOptMin": baseScgPtpPmCmnScgOptMin,
       "baseScgPtpPmCmnScgOptMax": baseScgPtpPmCmnScgOptMax,
       "baseScgPtpPmCmnScgOptAve": baseScgPtpPmCmnScgOptAve,
       "baseScgPtpPmCmnScgOprMin": baseScgPtpPmCmnScgOprMin,
       "baseScgPtpPmCmnScgOprMax": baseScgPtpPmCmnScgOprMax,
       "baseScgPtpPmCmnScgOprAve": baseScgPtpPmCmnScgOprAve,
       "baseScgPtpPmConformance": baseScgPtpPmConformance,
       "baseScgPtpPmCompliances": baseScgPtpPmCompliances,
       "baseScgPtpPmCompliance": baseScgPtpPmCompliance,
       "baseScgPtpPmRealCompliance": baseScgPtpPmRealCompliance,
       "baseScgPtpPmGroups": baseScgPtpPmGroups,
       "baseScgPtpPmGroup": baseScgPtpPmGroup,
       "baseScgPtpPmRealGroup": baseScgPtpPmRealGroup}
)
