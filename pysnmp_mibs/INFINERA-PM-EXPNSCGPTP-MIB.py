# SNMP MIB module (INFINERA-PM-EXPNSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-EXPNSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:28 2025
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

expnScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48)
)
if mibBuilder.loadTexts:
    expnScgPtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExpnScgPtpPmRealTable_Object = MibTable
expnScgPtpPmRealTable = _ExpnScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1)
)
if mibBuilder.loadTexts:
    expnScgPtpPmRealTable.setStatus("current")
_ExpnScgPtpPmRealEntry_Object = MibTableRow
expnScgPtpPmRealEntry = _ExpnScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1, 1)
)
expnScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    expnScgPtpPmRealEntry.setStatus("current")
_ExpnScgPtpPmRealCmnScgOpt_Type = FloatHundredths
_ExpnScgPtpPmRealCmnScgOpt_Object = MibTableColumn
expnScgPtpPmRealCmnScgOpt = _ExpnScgPtpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1, 1, 1),
    _ExpnScgPtpPmRealCmnScgOpt_Type()
)
expnScgPtpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmRealCmnScgOpt.setStatus("current")
_ExpnScgPtpPmRealCmnScgOpr_Type = FloatHundredths
_ExpnScgPtpPmRealCmnScgOpr_Object = MibTableColumn
expnScgPtpPmRealCmnScgOpr = _ExpnScgPtpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 1, 1, 2),
    _ExpnScgPtpPmRealCmnScgOpr_Type()
)
expnScgPtpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmRealCmnScgOpr.setStatus("current")
_ExpnScgPtpPmTable_Object = MibTable
expnScgPtpPmTable = _ExpnScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2)
)
if mibBuilder.loadTexts:
    expnScgPtpPmTable.setStatus("current")
_ExpnScgPtpPmEntry_Object = MibTableRow
expnScgPtpPmEntry = _ExpnScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1)
)
expnScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    expnScgPtpPmEntry.setStatus("current")
_ExpnScgPtpPmValidity_Type = TruthValue
_ExpnScgPtpPmValidity_Object = MibTableColumn
expnScgPtpPmValidity = _ExpnScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 3),
    _ExpnScgPtpPmValidity_Type()
)
expnScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmValidity.setStatus("current")
_ExpnScgPtpPmCmnScgOptMin_Type = FloatHundredths
_ExpnScgPtpPmCmnScgOptMin_Object = MibTableColumn
expnScgPtpPmCmnScgOptMin = _ExpnScgPtpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 4),
    _ExpnScgPtpPmCmnScgOptMin_Type()
)
expnScgPtpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmCmnScgOptMin.setStatus("current")
_ExpnScgPtpPmCmnScgOptMax_Type = FloatHundredths
_ExpnScgPtpPmCmnScgOptMax_Object = MibTableColumn
expnScgPtpPmCmnScgOptMax = _ExpnScgPtpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 5),
    _ExpnScgPtpPmCmnScgOptMax_Type()
)
expnScgPtpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmCmnScgOptMax.setStatus("current")
_ExpnScgPtpPmCmnScgOptAve_Type = FloatHundredths
_ExpnScgPtpPmCmnScgOptAve_Object = MibTableColumn
expnScgPtpPmCmnScgOptAve = _ExpnScgPtpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 6),
    _ExpnScgPtpPmCmnScgOptAve_Type()
)
expnScgPtpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmCmnScgOptAve.setStatus("current")
_ExpnScgPtpPmCmnScgOprMin_Type = FloatHundredths
_ExpnScgPtpPmCmnScgOprMin_Object = MibTableColumn
expnScgPtpPmCmnScgOprMin = _ExpnScgPtpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 7),
    _ExpnScgPtpPmCmnScgOprMin_Type()
)
expnScgPtpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmCmnScgOprMin.setStatus("current")
_ExpnScgPtpPmCmnScgOprMax_Type = FloatHundredths
_ExpnScgPtpPmCmnScgOprMax_Object = MibTableColumn
expnScgPtpPmCmnScgOprMax = _ExpnScgPtpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 8),
    _ExpnScgPtpPmCmnScgOprMax_Type()
)
expnScgPtpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmCmnScgOprMax.setStatus("current")
_ExpnScgPtpPmCmnScgOprAve_Type = FloatHundredths
_ExpnScgPtpPmCmnScgOprAve_Object = MibTableColumn
expnScgPtpPmCmnScgOprAve = _ExpnScgPtpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 2, 1, 9),
    _ExpnScgPtpPmCmnScgOprAve_Type()
)
expnScgPtpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnScgPtpPmCmnScgOprAve.setStatus("current")
_ExpnScgPtpPmConformance_ObjectIdentity = ObjectIdentity
expnScgPtpPmConformance = _ExpnScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3)
)
_ExpnScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
expnScgPtpPmCompliances = _ExpnScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 1)
)
_ExpnScgPtpPmGroups_ObjectIdentity = ObjectIdentity
expnScgPtpPmGroups = _ExpnScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 2)
)

# Managed Objects groups

expnScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 2, 1)
)
expnScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmValidity"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOptMin"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOptMax"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOptAve"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOprMin"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOprMax"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmCmnScgOprAve"))
)
if mibBuilder.loadTexts:
    expnScgPtpPmGroup.setStatus("current")

expnScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 2, 2)
)
expnScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmRealCmnScgOpt"),
        ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmRealCmnScgOpr"))
)
if mibBuilder.loadTexts:
    expnScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

expnScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 1, 1)
)
expnScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    expnScgPtpPmCompliance.setStatus(
        "current"
    )

expnScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 48, 3, 1, 2)
)
expnScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-EXPNSCGPTP-MIB", "expnScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    expnScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-EXPNSCGPTP-MIB",
    **{"expnScgPtpPmMIB": expnScgPtpPmMIB,
       "expnScgPtpPmRealTable": expnScgPtpPmRealTable,
       "expnScgPtpPmRealEntry": expnScgPtpPmRealEntry,
       "expnScgPtpPmRealCmnScgOpt": expnScgPtpPmRealCmnScgOpt,
       "expnScgPtpPmRealCmnScgOpr": expnScgPtpPmRealCmnScgOpr,
       "expnScgPtpPmTable": expnScgPtpPmTable,
       "expnScgPtpPmEntry": expnScgPtpPmEntry,
       "expnScgPtpPmValidity": expnScgPtpPmValidity,
       "expnScgPtpPmCmnScgOptMin": expnScgPtpPmCmnScgOptMin,
       "expnScgPtpPmCmnScgOptMax": expnScgPtpPmCmnScgOptMax,
       "expnScgPtpPmCmnScgOptAve": expnScgPtpPmCmnScgOptAve,
       "expnScgPtpPmCmnScgOprMin": expnScgPtpPmCmnScgOprMin,
       "expnScgPtpPmCmnScgOprMax": expnScgPtpPmCmnScgOprMax,
       "expnScgPtpPmCmnScgOprAve": expnScgPtpPmCmnScgOprAve,
       "expnScgPtpPmConformance": expnScgPtpPmConformance,
       "expnScgPtpPmCompliances": expnScgPtpPmCompliances,
       "expnScgPtpPmCompliance": expnScgPtpPmCompliance,
       "expnScgPtpPmRealCompliance": expnScgPtpPmRealCompliance,
       "expnScgPtpPmGroups": expnScgPtpPmGroups,
       "expnScgPtpPmGroup": expnScgPtpPmGroup,
       "expnScgPtpPmRealGroup": expnScgPtpPmRealGroup}
)
