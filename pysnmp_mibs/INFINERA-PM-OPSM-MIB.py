# SNMP MIB module (INFINERA-PM-OPSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OPSM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:03 2025
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

opsmPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50)
)
if mibBuilder.loadTexts:
    opsmPmMIB.setRevisions(
        ("2015-05-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OpsmPmRealTable_Object = MibTable
opsmPmRealTable = _OpsmPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 1)
)
if mibBuilder.loadTexts:
    opsmPmRealTable.setStatus("current")
_OpsmPmRealEntry_Object = MibTableRow
opsmPmRealEntry = _OpsmPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 1, 1)
)
opsmPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    opsmPmRealEntry.setStatus("current")
_OpsmPmRealOpr_Type = FloatHundredths
_OpsmPmRealOpr_Object = MibTableColumn
opsmPmRealOpr = _OpsmPmRealOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 1, 1, 1),
    _OpsmPmRealOpr_Type()
)
opsmPmRealOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPmRealOpr.setStatus("current")
_OpsmPmTable_Object = MibTable
opsmPmTable = _OpsmPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2)
)
if mibBuilder.loadTexts:
    opsmPmTable.setStatus("current")
_OpsmPmEntry_Object = MibTableRow
opsmPmEntry = _OpsmPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1)
)
opsmPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OPSM-MIB", "opsmPmSampleDuration"),
    (0, "INFINERA-PM-OPSM-MIB", "opsmPmTimestamp"),
)
if mibBuilder.loadTexts:
    opsmPmEntry.setStatus("current")


class _OpsmPmTimestamp_Type(Integer32):
    """Custom type opsmPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OpsmPmTimestamp_Type.__name__ = "Integer32"
_OpsmPmTimestamp_Object = MibTableColumn
opsmPmTimestamp = _OpsmPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 1),
    _OpsmPmTimestamp_Type()
)
opsmPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opsmPmTimestamp.setStatus("current")


class _OpsmPmSampleDuration_Type(Integer32):
    """Custom type opsmPmSampleDuration based on Integer32"""
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


_OpsmPmSampleDuration_Type.__name__ = "Integer32"
_OpsmPmSampleDuration_Object = MibTableColumn
opsmPmSampleDuration = _OpsmPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 2),
    _OpsmPmSampleDuration_Type()
)
opsmPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    opsmPmSampleDuration.setStatus("current")
_OpsmPmValidity_Type = TruthValue
_OpsmPmValidity_Object = MibTableColumn
opsmPmValidity = _OpsmPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 3),
    _OpsmPmValidity_Type()
)
opsmPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPmValidity.setStatus("current")
_OpsmPmOprMin_Type = FloatHundredths
_OpsmPmOprMin_Object = MibTableColumn
opsmPmOprMin = _OpsmPmOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 4),
    _OpsmPmOprMin_Type()
)
opsmPmOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPmOprMin.setStatus("current")
_OpsmPmOprMax_Type = FloatHundredths
_OpsmPmOprMax_Object = MibTableColumn
opsmPmOprMax = _OpsmPmOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 5),
    _OpsmPmOprMax_Type()
)
opsmPmOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPmOprMax.setStatus("current")
_OpsmPmOprAve_Type = FloatHundredths
_OpsmPmOprAve_Object = MibTableColumn
opsmPmOprAve = _OpsmPmOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 2, 1, 6),
    _OpsmPmOprAve_Type()
)
opsmPmOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opsmPmOprAve.setStatus("current")
_OpsmPmConformance_ObjectIdentity = ObjectIdentity
opsmPmConformance = _OpsmPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3)
)
_OpsmPmCompliances_ObjectIdentity = ObjectIdentity
opsmPmCompliances = _OpsmPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 1)
)
_OpsmPmGroups_ObjectIdentity = ObjectIdentity
opsmPmGroups = _OpsmPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 2)
)

# Managed Objects groups

opsmPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 2, 1)
)
opsmPmGroup.setObjects(
      *(("INFINERA-PM-OPSM-MIB", "opsmPmTimestamp"),
        ("INFINERA-PM-OPSM-MIB", "opsmPmSampleDuration"),
        ("INFINERA-PM-OPSM-MIB", "opsmPmValidity"),
        ("INFINERA-PM-OPSM-MIB", "opsmPmOprMin"),
        ("INFINERA-PM-OPSM-MIB", "opsmPmOprMax"),
        ("INFINERA-PM-OPSM-MIB", "opsmPmOprAve"))
)
if mibBuilder.loadTexts:
    opsmPmGroup.setStatus("current")

opsmPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 2, 2)
)
opsmPmRealGroup.setObjects(
    ("INFINERA-PM-OPSM-MIB", "opsmPmRealOpr")
)
if mibBuilder.loadTexts:
    opsmPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

opsmPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 1, 1)
)
opsmPmCompliance.setObjects(
    ("INFINERA-PM-OPSM-MIB", "opsmPmGroup")
)
if mibBuilder.loadTexts:
    opsmPmCompliance.setStatus(
        "current"
    )

opsmPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 50, 3, 1, 2)
)
opsmPmRealCompliance.setObjects(
    ("INFINERA-PM-OPSM-MIB", "opsmPmRealGroup")
)
if mibBuilder.loadTexts:
    opsmPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OPSM-MIB",
    **{"opsmPmMIB": opsmPmMIB,
       "opsmPmRealTable": opsmPmRealTable,
       "opsmPmRealEntry": opsmPmRealEntry,
       "opsmPmRealOpr": opsmPmRealOpr,
       "opsmPmTable": opsmPmTable,
       "opsmPmEntry": opsmPmEntry,
       "opsmPmTimestamp": opsmPmTimestamp,
       "opsmPmSampleDuration": opsmPmSampleDuration,
       "opsmPmValidity": opsmPmValidity,
       "opsmPmOprMin": opsmPmOprMin,
       "opsmPmOprMax": opsmPmOprMax,
       "opsmPmOprAve": opsmPmOprAve,
       "opsmPmConformance": opsmPmConformance,
       "opsmPmCompliances": opsmPmCompliances,
       "opsmPmCompliance": opsmPmCompliance,
       "opsmPmRealCompliance": opsmPmRealCompliance,
       "opsmPmGroups": opsmPmGroups,
       "opsmPmGroup": opsmPmGroup,
       "opsmPmRealGroup": opsmPmRealGroup}
)
