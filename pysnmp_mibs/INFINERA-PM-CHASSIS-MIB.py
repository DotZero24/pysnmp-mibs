# SNMP MIB module (INFINERA-PM-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:19 2025
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

chassisPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51)
)
if mibBuilder.loadTexts:
    chassisPmMIB.setRevisions(
        ("2015-05-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChassisPmRealTable_Object = MibTable
chassisPmRealTable = _ChassisPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 1)
)
if mibBuilder.loadTexts:
    chassisPmRealTable.setStatus("current")
_ChassisPmRealEntry_Object = MibTableRow
chassisPmRealEntry = _ChassisPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 1, 1)
)
chassisPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    chassisPmRealEntry.setStatus("current")
_ChassisPmRealInPRaw_Type = FloatHundredths
_ChassisPmRealInPRaw_Object = MibTableColumn
chassisPmRealInPRaw = _ChassisPmRealInPRaw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 1, 1, 1),
    _ChassisPmRealInPRaw_Type()
)
chassisPmRealInPRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPmRealInPRaw.setStatus("current")
_ChassisPmTable_Object = MibTable
chassisPmTable = _ChassisPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2)
)
if mibBuilder.loadTexts:
    chassisPmTable.setStatus("current")
_ChassisPmEntry_Object = MibTableRow
chassisPmEntry = _ChassisPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1)
)
chassisPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-CHASSIS-MIB", "chassisPmSampleDuration"),
    (0, "INFINERA-PM-CHASSIS-MIB", "chassisPmTimestamp"),
)
if mibBuilder.loadTexts:
    chassisPmEntry.setStatus("current")


class _ChassisPmTimestamp_Type(Integer32):
    """Custom type chassisPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChassisPmTimestamp_Type.__name__ = "Integer32"
_ChassisPmTimestamp_Object = MibTableColumn
chassisPmTimestamp = _ChassisPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 1),
    _ChassisPmTimestamp_Type()
)
chassisPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chassisPmTimestamp.setStatus("current")


class _ChassisPmSampleDuration_Type(Integer32):
    """Custom type chassisPmSampleDuration based on Integer32"""
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


_ChassisPmSampleDuration_Type.__name__ = "Integer32"
_ChassisPmSampleDuration_Object = MibTableColumn
chassisPmSampleDuration = _ChassisPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 2),
    _ChassisPmSampleDuration_Type()
)
chassisPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chassisPmSampleDuration.setStatus("current")
_ChassisPmValidity_Type = TruthValue
_ChassisPmValidity_Object = MibTableColumn
chassisPmValidity = _ChassisPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 3),
    _ChassisPmValidity_Type()
)
chassisPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPmValidity.setStatus("current")
_ChassisPmInPMin_Type = FloatHundredths
_ChassisPmInPMin_Object = MibTableColumn
chassisPmInPMin = _ChassisPmInPMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 4),
    _ChassisPmInPMin_Type()
)
chassisPmInPMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPmInPMin.setStatus("current")
_ChassisPmInPMax_Type = FloatHundredths
_ChassisPmInPMax_Object = MibTableColumn
chassisPmInPMax = _ChassisPmInPMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 5),
    _ChassisPmInPMax_Type()
)
chassisPmInPMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPmInPMax.setStatus("current")
_ChassisPmInPAvg_Type = FloatHundredths
_ChassisPmInPAvg_Object = MibTableColumn
chassisPmInPAvg = _ChassisPmInPAvg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 2, 1, 6),
    _ChassisPmInPAvg_Type()
)
chassisPmInPAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPmInPAvg.setStatus("current")
_ChassisPmConformance_ObjectIdentity = ObjectIdentity
chassisPmConformance = _ChassisPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3)
)
_ChassisPmCompliances_ObjectIdentity = ObjectIdentity
chassisPmCompliances = _ChassisPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 1)
)
_ChassisPmGroups_ObjectIdentity = ObjectIdentity
chassisPmGroups = _ChassisPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 2)
)

# Managed Objects groups

chassisPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 2, 1)
)
chassisPmGroup.setObjects(
      *(("INFINERA-PM-CHASSIS-MIB", "chassisPmTimestamp"),
        ("INFINERA-PM-CHASSIS-MIB", "chassisPmSampleDuration"),
        ("INFINERA-PM-CHASSIS-MIB", "chassisPmValidity"),
        ("INFINERA-PM-CHASSIS-MIB", "chassisPmInPMin"),
        ("INFINERA-PM-CHASSIS-MIB", "chassisPmInPMax"),
        ("INFINERA-PM-CHASSIS-MIB", "chassisPmInPAvg"))
)
if mibBuilder.loadTexts:
    chassisPmGroup.setStatus("current")

chassisPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 2, 2)
)
chassisPmRealGroup.setObjects(
    ("INFINERA-PM-CHASSIS-MIB", "chassisPmRealInPRaw")
)
if mibBuilder.loadTexts:
    chassisPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

chassisPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 1, 1)
)
chassisPmCompliance.setObjects(
    ("INFINERA-PM-CHASSIS-MIB", "chassisPmGroup")
)
if mibBuilder.loadTexts:
    chassisPmCompliance.setStatus(
        "current"
    )

chassisPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 51, 3, 1, 2)
)
chassisPmRealCompliance.setObjects(
    ("INFINERA-PM-CHASSIS-MIB", "chassisPmRealGroup")
)
if mibBuilder.loadTexts:
    chassisPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-CHASSIS-MIB",
    **{"chassisPmMIB": chassisPmMIB,
       "chassisPmRealTable": chassisPmRealTable,
       "chassisPmRealEntry": chassisPmRealEntry,
       "chassisPmRealInPRaw": chassisPmRealInPRaw,
       "chassisPmTable": chassisPmTable,
       "chassisPmEntry": chassisPmEntry,
       "chassisPmTimestamp": chassisPmTimestamp,
       "chassisPmSampleDuration": chassisPmSampleDuration,
       "chassisPmValidity": chassisPmValidity,
       "chassisPmInPMin": chassisPmInPMin,
       "chassisPmInPMax": chassisPmInPMax,
       "chassisPmInPAvg": chassisPmInPAvg,
       "chassisPmConformance": chassisPmConformance,
       "chassisPmCompliances": chassisPmCompliances,
       "chassisPmCompliance": chassisPmCompliance,
       "chassisPmRealCompliance": chassisPmRealCompliance,
       "chassisPmGroups": chassisPmGroups,
       "chassisPmGroup": chassisPmGroup,
       "chassisPmRealGroup": chassisPmRealGroup}
)
