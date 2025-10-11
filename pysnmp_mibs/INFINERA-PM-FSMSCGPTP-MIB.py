# SNMP MIB module (INFINERA-PM-FSMSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FSMSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:14 2025
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

fsmScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    fsmScgPtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsmScgPtpPmRealTable_Object = MibTable
fsmScgPtpPmRealTable = _FsmScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 1)
)
if mibBuilder.loadTexts:
    fsmScgPtpPmRealTable.setStatus("current")
_FsmScgPtpPmRealEntry_Object = MibTableRow
fsmScgPtpPmRealEntry = _FsmScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 1, 1)
)
fsmScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsmScgPtpPmRealEntry.setStatus("current")
_FsmScgPtpPmRealCmnScgOpt_Type = FloatHundredths
_FsmScgPtpPmRealCmnScgOpt_Object = MibTableColumn
fsmScgPtpPmRealCmnScgOpt = _FsmScgPtpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 1, 1, 1),
    _FsmScgPtpPmRealCmnScgOpt_Type()
)
fsmScgPtpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmRealCmnScgOpt.setStatus("current")
_FsmScgPtpPmRealCmnScgOpr_Type = FloatHundredths
_FsmScgPtpPmRealCmnScgOpr_Object = MibTableColumn
fsmScgPtpPmRealCmnScgOpr = _FsmScgPtpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 1, 1, 2),
    _FsmScgPtpPmRealCmnScgOpr_Type()
)
fsmScgPtpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmRealCmnScgOpr.setStatus("current")
_FsmScgPtpPmTable_Object = MibTable
fsmScgPtpPmTable = _FsmScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2)
)
if mibBuilder.loadTexts:
    fsmScgPtpPmTable.setStatus("current")
_FsmScgPtpPmEntry_Object = MibTableRow
fsmScgPtpPmEntry = _FsmScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1)
)
fsmScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmSampleDuration"),
    (0, "INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    fsmScgPtpPmEntry.setStatus("current")


class _FsmScgPtpPmTimestamp_Type(Integer32):
    """Custom type fsmScgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsmScgPtpPmTimestamp_Type.__name__ = "Integer32"
_FsmScgPtpPmTimestamp_Object = MibTableColumn
fsmScgPtpPmTimestamp = _FsmScgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 1),
    _FsmScgPtpPmTimestamp_Type()
)
fsmScgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsmScgPtpPmTimestamp.setStatus("current")
_FsmScgPtpPmSampleDuration_Type = InfnSampleDuration
_FsmScgPtpPmSampleDuration_Object = MibTableColumn
fsmScgPtpPmSampleDuration = _FsmScgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 2),
    _FsmScgPtpPmSampleDuration_Type()
)
fsmScgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsmScgPtpPmSampleDuration.setStatus("current")
_FsmScgPtpPmValidity_Type = TruthValue
_FsmScgPtpPmValidity_Object = MibTableColumn
fsmScgPtpPmValidity = _FsmScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 3),
    _FsmScgPtpPmValidity_Type()
)
fsmScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmValidity.setStatus("current")
_FsmScgPtpPmCmnScgOptMin_Type = FloatHundredths
_FsmScgPtpPmCmnScgOptMin_Object = MibTableColumn
fsmScgPtpPmCmnScgOptMin = _FsmScgPtpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 4),
    _FsmScgPtpPmCmnScgOptMin_Type()
)
fsmScgPtpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmCmnScgOptMin.setStatus("current")
_FsmScgPtpPmCmnScgOptMax_Type = FloatHundredths
_FsmScgPtpPmCmnScgOptMax_Object = MibTableColumn
fsmScgPtpPmCmnScgOptMax = _FsmScgPtpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 5),
    _FsmScgPtpPmCmnScgOptMax_Type()
)
fsmScgPtpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmCmnScgOptMax.setStatus("current")
_FsmScgPtpPmCmnScgOptAve_Type = FloatHundredths
_FsmScgPtpPmCmnScgOptAve_Object = MibTableColumn
fsmScgPtpPmCmnScgOptAve = _FsmScgPtpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 6),
    _FsmScgPtpPmCmnScgOptAve_Type()
)
fsmScgPtpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmCmnScgOptAve.setStatus("current")
_FsmScgPtpPmCmnScgOprMin_Type = FloatHundredths
_FsmScgPtpPmCmnScgOprMin_Object = MibTableColumn
fsmScgPtpPmCmnScgOprMin = _FsmScgPtpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 7),
    _FsmScgPtpPmCmnScgOprMin_Type()
)
fsmScgPtpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmCmnScgOprMin.setStatus("current")
_FsmScgPtpPmCmnScgOprMax_Type = FloatHundredths
_FsmScgPtpPmCmnScgOprMax_Object = MibTableColumn
fsmScgPtpPmCmnScgOprMax = _FsmScgPtpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 8),
    _FsmScgPtpPmCmnScgOprMax_Type()
)
fsmScgPtpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmCmnScgOprMax.setStatus("current")
_FsmScgPtpPmCmnScgOprAve_Type = FloatHundredths
_FsmScgPtpPmCmnScgOprAve_Object = MibTableColumn
fsmScgPtpPmCmnScgOprAve = _FsmScgPtpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 2, 1, 9),
    _FsmScgPtpPmCmnScgOprAve_Type()
)
fsmScgPtpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsmScgPtpPmCmnScgOprAve.setStatus("current")
_FsmScgPtpPmConformance_ObjectIdentity = ObjectIdentity
fsmScgPtpPmConformance = _FsmScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3)
)
_FsmScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
fsmScgPtpPmCompliances = _FsmScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3, 1)
)
_FsmScgPtpPmGroups_ObjectIdentity = ObjectIdentity
fsmScgPtpPmGroups = _FsmScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3, 2)
)

# Managed Objects groups

fsmScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3, 2, 1)
)
fsmScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmTimestamp"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmSampleDuration"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmValidity"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmCmnScgOptMin"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmCmnScgOptMax"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmCmnScgOptAve"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmCmnScgOprMin"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmCmnScgOprMax"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmCmnScgOprAve"))
)
if mibBuilder.loadTexts:
    fsmScgPtpPmGroup.setStatus("current")

fsmScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3, 2, 2)
)
fsmScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmRealCmnScgOpt"),
        ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmRealCmnScgOpr"))
)
if mibBuilder.loadTexts:
    fsmScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsmScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3, 1, 1)
)
fsmScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    fsmScgPtpPmCompliance.setStatus(
        "current"
    )

fsmScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 40, 3, 1, 2)
)
fsmScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-FSMSCGPTP-MIB", "fsmScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    fsmScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FSMSCGPTP-MIB",
    **{"fsmScgPtpPmMIB": fsmScgPtpPmMIB,
       "fsmScgPtpPmRealTable": fsmScgPtpPmRealTable,
       "fsmScgPtpPmRealEntry": fsmScgPtpPmRealEntry,
       "fsmScgPtpPmRealCmnScgOpt": fsmScgPtpPmRealCmnScgOpt,
       "fsmScgPtpPmRealCmnScgOpr": fsmScgPtpPmRealCmnScgOpr,
       "fsmScgPtpPmTable": fsmScgPtpPmTable,
       "fsmScgPtpPmEntry": fsmScgPtpPmEntry,
       "fsmScgPtpPmTimestamp": fsmScgPtpPmTimestamp,
       "fsmScgPtpPmSampleDuration": fsmScgPtpPmSampleDuration,
       "fsmScgPtpPmValidity": fsmScgPtpPmValidity,
       "fsmScgPtpPmCmnScgOptMin": fsmScgPtpPmCmnScgOptMin,
       "fsmScgPtpPmCmnScgOptMax": fsmScgPtpPmCmnScgOptMax,
       "fsmScgPtpPmCmnScgOptAve": fsmScgPtpPmCmnScgOptAve,
       "fsmScgPtpPmCmnScgOprMin": fsmScgPtpPmCmnScgOprMin,
       "fsmScgPtpPmCmnScgOprMax": fsmScgPtpPmCmnScgOprMax,
       "fsmScgPtpPmCmnScgOprAve": fsmScgPtpPmCmnScgOprAve,
       "fsmScgPtpPmConformance": fsmScgPtpPmConformance,
       "fsmScgPtpPmCompliances": fsmScgPtpPmCompliances,
       "fsmScgPtpPmCompliance": fsmScgPtpPmCompliance,
       "fsmScgPtpPmRealCompliance": fsmScgPtpPmRealCompliance,
       "fsmScgPtpPmGroups": fsmScgPtpPmGroups,
       "fsmScgPtpPmGroup": fsmScgPtpPmGroup,
       "fsmScgPtpPmRealGroup": fsmScgPtpPmRealGroup}
)
