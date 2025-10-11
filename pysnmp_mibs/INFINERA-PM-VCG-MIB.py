# SNMP MIB module (INFINERA-PM-VCG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-VCG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:43 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vCGPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    vCGPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VCGPmRealTable_Object = MibTable
vCGPmRealTable = _VCGPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1)
)
if mibBuilder.loadTexts:
    vCGPmRealTable.setStatus("current")
_VCGPmRealEntry_Object = MibTableRow
vCGPmRealEntry = _VCGPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1)
)
vCGPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vCGPmRealEntry.setStatus("current")
_VCGPmRealDifferentialDelay1_Type = FloatHundredths
_VCGPmRealDifferentialDelay1_Object = MibTableColumn
vCGPmRealDifferentialDelay1 = _VCGPmRealDifferentialDelay1_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 1),
    _VCGPmRealDifferentialDelay1_Type()
)
vCGPmRealDifferentialDelay1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay1.setStatus("current")
_VCGPmRealDifferentialDelay2_Type = FloatHundredths
_VCGPmRealDifferentialDelay2_Object = MibTableColumn
vCGPmRealDifferentialDelay2 = _VCGPmRealDifferentialDelay2_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 2),
    _VCGPmRealDifferentialDelay2_Type()
)
vCGPmRealDifferentialDelay2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay2.setStatus("current")
_VCGPmRealDifferentialDelay3_Type = FloatHundredths
_VCGPmRealDifferentialDelay3_Object = MibTableColumn
vCGPmRealDifferentialDelay3 = _VCGPmRealDifferentialDelay3_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 3),
    _VCGPmRealDifferentialDelay3_Type()
)
vCGPmRealDifferentialDelay3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay3.setStatus("current")
_VCGPmRealDifferentialDelay4_Type = FloatHundredths
_VCGPmRealDifferentialDelay4_Object = MibTableColumn
vCGPmRealDifferentialDelay4 = _VCGPmRealDifferentialDelay4_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 4),
    _VCGPmRealDifferentialDelay4_Type()
)
vCGPmRealDifferentialDelay4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay4.setStatus("current")
_VCGPmRealDifferentialDelay5_Type = FloatHundredths
_VCGPmRealDifferentialDelay5_Object = MibTableColumn
vCGPmRealDifferentialDelay5 = _VCGPmRealDifferentialDelay5_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 5),
    _VCGPmRealDifferentialDelay5_Type()
)
vCGPmRealDifferentialDelay5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay5.setStatus("current")
_VCGPmRealDifferentialDelay6_Type = FloatHundredths
_VCGPmRealDifferentialDelay6_Object = MibTableColumn
vCGPmRealDifferentialDelay6 = _VCGPmRealDifferentialDelay6_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 6),
    _VCGPmRealDifferentialDelay6_Type()
)
vCGPmRealDifferentialDelay6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay6.setStatus("current")
_VCGPmRealDifferentialDelay7_Type = FloatHundredths
_VCGPmRealDifferentialDelay7_Object = MibTableColumn
vCGPmRealDifferentialDelay7 = _VCGPmRealDifferentialDelay7_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 7),
    _VCGPmRealDifferentialDelay7_Type()
)
vCGPmRealDifferentialDelay7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay7.setStatus("current")
_VCGPmRealDifferentialDelay8_Type = FloatHundredths
_VCGPmRealDifferentialDelay8_Object = MibTableColumn
vCGPmRealDifferentialDelay8 = _VCGPmRealDifferentialDelay8_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 8),
    _VCGPmRealDifferentialDelay8_Type()
)
vCGPmRealDifferentialDelay8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay8.setStatus("current")
_VCGPmRealDifferentialDelay9_Type = FloatHundredths
_VCGPmRealDifferentialDelay9_Object = MibTableColumn
vCGPmRealDifferentialDelay9 = _VCGPmRealDifferentialDelay9_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 9),
    _VCGPmRealDifferentialDelay9_Type()
)
vCGPmRealDifferentialDelay9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay9.setStatus("current")
_VCGPmRealDifferentialDelay10_Type = FloatHundredths
_VCGPmRealDifferentialDelay10_Object = MibTableColumn
vCGPmRealDifferentialDelay10 = _VCGPmRealDifferentialDelay10_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 10),
    _VCGPmRealDifferentialDelay10_Type()
)
vCGPmRealDifferentialDelay10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay10.setStatus("current")
_VCGPmRealDifferentialDelay11_Type = FloatHundredths
_VCGPmRealDifferentialDelay11_Object = MibTableColumn
vCGPmRealDifferentialDelay11 = _VCGPmRealDifferentialDelay11_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 11),
    _VCGPmRealDifferentialDelay11_Type()
)
vCGPmRealDifferentialDelay11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay11.setStatus("current")
_VCGPmRealDifferentialDelay12_Type = FloatHundredths
_VCGPmRealDifferentialDelay12_Object = MibTableColumn
vCGPmRealDifferentialDelay12 = _VCGPmRealDifferentialDelay12_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 12),
    _VCGPmRealDifferentialDelay12_Type()
)
vCGPmRealDifferentialDelay12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay12.setStatus("current")
_VCGPmRealDifferentialDelay13_Type = FloatHundredths
_VCGPmRealDifferentialDelay13_Object = MibTableColumn
vCGPmRealDifferentialDelay13 = _VCGPmRealDifferentialDelay13_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 13),
    _VCGPmRealDifferentialDelay13_Type()
)
vCGPmRealDifferentialDelay13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay13.setStatus("current")
_VCGPmRealDifferentialDelay14_Type = FloatHundredths
_VCGPmRealDifferentialDelay14_Object = MibTableColumn
vCGPmRealDifferentialDelay14 = _VCGPmRealDifferentialDelay14_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 14),
    _VCGPmRealDifferentialDelay14_Type()
)
vCGPmRealDifferentialDelay14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay14.setStatus("current")
_VCGPmRealDifferentialDelay15_Type = FloatHundredths
_VCGPmRealDifferentialDelay15_Object = MibTableColumn
vCGPmRealDifferentialDelay15 = _VCGPmRealDifferentialDelay15_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 15),
    _VCGPmRealDifferentialDelay15_Type()
)
vCGPmRealDifferentialDelay15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay15.setStatus("current")
_VCGPmRealDifferentialDelay16_Type = FloatHundredths
_VCGPmRealDifferentialDelay16_Object = MibTableColumn
vCGPmRealDifferentialDelay16 = _VCGPmRealDifferentialDelay16_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 16),
    _VCGPmRealDifferentialDelay16_Type()
)
vCGPmRealDifferentialDelay16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay16.setStatus("current")
_VCGPmRealDifferentialDelay17_Type = FloatHundredths
_VCGPmRealDifferentialDelay17_Object = MibTableColumn
vCGPmRealDifferentialDelay17 = _VCGPmRealDifferentialDelay17_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 17),
    _VCGPmRealDifferentialDelay17_Type()
)
vCGPmRealDifferentialDelay17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay17.setStatus("current")
_VCGPmRealDifferentialDelay18_Type = FloatHundredths
_VCGPmRealDifferentialDelay18_Object = MibTableColumn
vCGPmRealDifferentialDelay18 = _VCGPmRealDifferentialDelay18_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 18),
    _VCGPmRealDifferentialDelay18_Type()
)
vCGPmRealDifferentialDelay18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay18.setStatus("current")
_VCGPmRealDifferentialDelay19_Type = FloatHundredths
_VCGPmRealDifferentialDelay19_Object = MibTableColumn
vCGPmRealDifferentialDelay19 = _VCGPmRealDifferentialDelay19_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 19),
    _VCGPmRealDifferentialDelay19_Type()
)
vCGPmRealDifferentialDelay19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay19.setStatus("current")
_VCGPmRealDifferentialDelay20_Type = FloatHundredths
_VCGPmRealDifferentialDelay20_Object = MibTableColumn
vCGPmRealDifferentialDelay20 = _VCGPmRealDifferentialDelay20_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 1, 1, 20),
    _VCGPmRealDifferentialDelay20_Type()
)
vCGPmRealDifferentialDelay20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vCGPmRealDifferentialDelay20.setStatus("current")
_VCGPmConformance_ObjectIdentity = ObjectIdentity
vCGPmConformance = _VCGPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 3)
)
_VCGPmCompliances_ObjectIdentity = ObjectIdentity
vCGPmCompliances = _VCGPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 3, 1)
)
_VCGPmGroups_ObjectIdentity = ObjectIdentity
vCGPmGroups = _VCGPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 3, 2)
)

# Managed Objects groups

vCGPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 3, 2, 1)
)
vCGPmRealGroup.setObjects(
      *(("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay1"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay2"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay3"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay4"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay5"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay6"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay7"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay8"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay9"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay10"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay11"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay12"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay13"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay14"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay15"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay16"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay17"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay18"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay19"),
        ("INFINERA-PM-VCG-MIB", "vCGPmRealDifferentialDelay20"))
)
if mibBuilder.loadTexts:
    vCGPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

vCGPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 16, 3, 1, 1)
)
vCGPmRealCompliance.setObjects(
    ("INFINERA-PM-VCG-MIB", "vCGPmRealGroup")
)
if mibBuilder.loadTexts:
    vCGPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-VCG-MIB",
    **{"vCGPmMIB": vCGPmMIB,
       "vCGPmRealTable": vCGPmRealTable,
       "vCGPmRealEntry": vCGPmRealEntry,
       "vCGPmRealDifferentialDelay1": vCGPmRealDifferentialDelay1,
       "vCGPmRealDifferentialDelay2": vCGPmRealDifferentialDelay2,
       "vCGPmRealDifferentialDelay3": vCGPmRealDifferentialDelay3,
       "vCGPmRealDifferentialDelay4": vCGPmRealDifferentialDelay4,
       "vCGPmRealDifferentialDelay5": vCGPmRealDifferentialDelay5,
       "vCGPmRealDifferentialDelay6": vCGPmRealDifferentialDelay6,
       "vCGPmRealDifferentialDelay7": vCGPmRealDifferentialDelay7,
       "vCGPmRealDifferentialDelay8": vCGPmRealDifferentialDelay8,
       "vCGPmRealDifferentialDelay9": vCGPmRealDifferentialDelay9,
       "vCGPmRealDifferentialDelay10": vCGPmRealDifferentialDelay10,
       "vCGPmRealDifferentialDelay11": vCGPmRealDifferentialDelay11,
       "vCGPmRealDifferentialDelay12": vCGPmRealDifferentialDelay12,
       "vCGPmRealDifferentialDelay13": vCGPmRealDifferentialDelay13,
       "vCGPmRealDifferentialDelay14": vCGPmRealDifferentialDelay14,
       "vCGPmRealDifferentialDelay15": vCGPmRealDifferentialDelay15,
       "vCGPmRealDifferentialDelay16": vCGPmRealDifferentialDelay16,
       "vCGPmRealDifferentialDelay17": vCGPmRealDifferentialDelay17,
       "vCGPmRealDifferentialDelay18": vCGPmRealDifferentialDelay18,
       "vCGPmRealDifferentialDelay19": vCGPmRealDifferentialDelay19,
       "vCGPmRealDifferentialDelay20": vCGPmRealDifferentialDelay20,
       "vCGPmConformance": vCGPmConformance,
       "vCGPmCompliances": vCGPmCompliances,
       "vCGPmRealCompliance": vCGPmRealCompliance,
       "vCGPmGroups": vCGPmGroups,
       "vCGPmRealGroup": vCGPmRealGroup}
)
