# SNMP MIB module (INFINERA-PM-FRMSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FRMSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:25 2025
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

frmScgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41)
)
if mibBuilder.loadTexts:
    frmScgPtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrmScgPtpPmRealTable_Object = MibTable
frmScgPtpPmRealTable = _FrmScgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 1)
)
if mibBuilder.loadTexts:
    frmScgPtpPmRealTable.setStatus("current")
_FrmScgPtpPmRealEntry_Object = MibTableRow
frmScgPtpPmRealEntry = _FrmScgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 1, 1)
)
frmScgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    frmScgPtpPmRealEntry.setStatus("current")
_FrmScgPtpPmRealCmnScgOpt_Type = FloatHundredths
_FrmScgPtpPmRealCmnScgOpt_Object = MibTableColumn
frmScgPtpPmRealCmnScgOpt = _FrmScgPtpPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 1, 1, 1),
    _FrmScgPtpPmRealCmnScgOpt_Type()
)
frmScgPtpPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmRealCmnScgOpt.setStatus("current")
_FrmScgPtpPmRealCmnScgOpr_Type = FloatHundredths
_FrmScgPtpPmRealCmnScgOpr_Object = MibTableColumn
frmScgPtpPmRealCmnScgOpr = _FrmScgPtpPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 1, 1, 2),
    _FrmScgPtpPmRealCmnScgOpr_Type()
)
frmScgPtpPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmRealCmnScgOpr.setStatus("current")
_FrmScgPtpPmTable_Object = MibTable
frmScgPtpPmTable = _FrmScgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2)
)
if mibBuilder.loadTexts:
    frmScgPtpPmTable.setStatus("current")
_FrmScgPtpPmEntry_Object = MibTableRow
frmScgPtpPmEntry = _FrmScgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1)
)
frmScgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmSampleDuration"),
    (0, "INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    frmScgPtpPmEntry.setStatus("current")


class _FrmScgPtpPmTimestamp_Type(Integer32):
    """Custom type frmScgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrmScgPtpPmTimestamp_Type.__name__ = "Integer32"
_FrmScgPtpPmTimestamp_Object = MibTableColumn
frmScgPtpPmTimestamp = _FrmScgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 1),
    _FrmScgPtpPmTimestamp_Type()
)
frmScgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frmScgPtpPmTimestamp.setStatus("current")


class _FrmScgPtpPmSampleDuration_Type(Integer32):
    """Custom type frmScgPtpPmSampleDuration based on Integer32"""
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


_FrmScgPtpPmSampleDuration_Type.__name__ = "Integer32"
_FrmScgPtpPmSampleDuration_Object = MibTableColumn
frmScgPtpPmSampleDuration = _FrmScgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 2),
    _FrmScgPtpPmSampleDuration_Type()
)
frmScgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frmScgPtpPmSampleDuration.setStatus("current")
_FrmScgPtpPmValidity_Type = TruthValue
_FrmScgPtpPmValidity_Object = MibTableColumn
frmScgPtpPmValidity = _FrmScgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 3),
    _FrmScgPtpPmValidity_Type()
)
frmScgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmValidity.setStatus("current")
_FrmScgPtpPmCmnScgOptMin_Type = FloatHundredths
_FrmScgPtpPmCmnScgOptMin_Object = MibTableColumn
frmScgPtpPmCmnScgOptMin = _FrmScgPtpPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 4),
    _FrmScgPtpPmCmnScgOptMin_Type()
)
frmScgPtpPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmCmnScgOptMin.setStatus("current")
_FrmScgPtpPmCmnScgOptMax_Type = FloatHundredths
_FrmScgPtpPmCmnScgOptMax_Object = MibTableColumn
frmScgPtpPmCmnScgOptMax = _FrmScgPtpPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 5),
    _FrmScgPtpPmCmnScgOptMax_Type()
)
frmScgPtpPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmCmnScgOptMax.setStatus("current")
_FrmScgPtpPmCmnScgOptAve_Type = FloatHundredths
_FrmScgPtpPmCmnScgOptAve_Object = MibTableColumn
frmScgPtpPmCmnScgOptAve = _FrmScgPtpPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 6),
    _FrmScgPtpPmCmnScgOptAve_Type()
)
frmScgPtpPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmCmnScgOptAve.setStatus("current")
_FrmScgPtpPmCmnScgOprMin_Type = FloatHundredths
_FrmScgPtpPmCmnScgOprMin_Object = MibTableColumn
frmScgPtpPmCmnScgOprMin = _FrmScgPtpPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 7),
    _FrmScgPtpPmCmnScgOprMin_Type()
)
frmScgPtpPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmCmnScgOprMin.setStatus("current")
_FrmScgPtpPmCmnScgOprMax_Type = FloatHundredths
_FrmScgPtpPmCmnScgOprMax_Object = MibTableColumn
frmScgPtpPmCmnScgOprMax = _FrmScgPtpPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 8),
    _FrmScgPtpPmCmnScgOprMax_Type()
)
frmScgPtpPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmCmnScgOprMax.setStatus("current")
_FrmScgPtpPmCmnScgOprAve_Type = FloatHundredths
_FrmScgPtpPmCmnScgOprAve_Object = MibTableColumn
frmScgPtpPmCmnScgOprAve = _FrmScgPtpPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 2, 1, 9),
    _FrmScgPtpPmCmnScgOprAve_Type()
)
frmScgPtpPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frmScgPtpPmCmnScgOprAve.setStatus("current")
_FrmScgPtpPmConformance_ObjectIdentity = ObjectIdentity
frmScgPtpPmConformance = _FrmScgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3)
)
_FrmScgPtpPmCompliances_ObjectIdentity = ObjectIdentity
frmScgPtpPmCompliances = _FrmScgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3, 1)
)
_FrmScgPtpPmGroups_ObjectIdentity = ObjectIdentity
frmScgPtpPmGroups = _FrmScgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3, 2)
)

# Managed Objects groups

frmScgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3, 2, 1)
)
frmScgPtpPmGroup.setObjects(
      *(("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmTimestamp"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmSampleDuration"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmValidity"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmCmnScgOptMin"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmCmnScgOptMax"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmCmnScgOptAve"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmCmnScgOprMin"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmCmnScgOprMax"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmCmnScgOprAve"))
)
if mibBuilder.loadTexts:
    frmScgPtpPmGroup.setStatus("current")

frmScgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3, 2, 2)
)
frmScgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmRealCmnScgOpt"),
        ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmRealCmnScgOpr"))
)
if mibBuilder.loadTexts:
    frmScgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

frmScgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3, 1, 1)
)
frmScgPtpPmCompliance.setObjects(
    ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmGroup")
)
if mibBuilder.loadTexts:
    frmScgPtpPmCompliance.setStatus(
        "current"
    )

frmScgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 41, 3, 1, 2)
)
frmScgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-FRMSCGPTP-MIB", "frmScgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    frmScgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FRMSCGPTP-MIB",
    **{"frmScgPtpPmMIB": frmScgPtpPmMIB,
       "frmScgPtpPmRealTable": frmScgPtpPmRealTable,
       "frmScgPtpPmRealEntry": frmScgPtpPmRealEntry,
       "frmScgPtpPmRealCmnScgOpt": frmScgPtpPmRealCmnScgOpt,
       "frmScgPtpPmRealCmnScgOpr": frmScgPtpPmRealCmnScgOpr,
       "frmScgPtpPmTable": frmScgPtpPmTable,
       "frmScgPtpPmEntry": frmScgPtpPmEntry,
       "frmScgPtpPmTimestamp": frmScgPtpPmTimestamp,
       "frmScgPtpPmSampleDuration": frmScgPtpPmSampleDuration,
       "frmScgPtpPmValidity": frmScgPtpPmValidity,
       "frmScgPtpPmCmnScgOptMin": frmScgPtpPmCmnScgOptMin,
       "frmScgPtpPmCmnScgOptMax": frmScgPtpPmCmnScgOptMax,
       "frmScgPtpPmCmnScgOptAve": frmScgPtpPmCmnScgOptAve,
       "frmScgPtpPmCmnScgOprMin": frmScgPtpPmCmnScgOprMin,
       "frmScgPtpPmCmnScgOprMax": frmScgPtpPmCmnScgOprMax,
       "frmScgPtpPmCmnScgOprAve": frmScgPtpPmCmnScgOprAve,
       "frmScgPtpPmConformance": frmScgPtpPmConformance,
       "frmScgPtpPmCompliances": frmScgPtpPmCompliances,
       "frmScgPtpPmCompliance": frmScgPtpPmCompliance,
       "frmScgPtpPmRealCompliance": frmScgPtpPmRealCompliance,
       "frmScgPtpPmGroups": frmScgPtpPmGroups,
       "frmScgPtpPmGroup": frmScgPtpPmGroup,
       "frmScgPtpPmRealGroup": frmScgPtpPmRealGroup}
)
