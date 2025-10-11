# SNMP MIB module (INFINERA-TP-PXMNWINTF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMNWINTF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:11 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatHundredths,
 FloatTenths,
 InfnPmHistStatsControl) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnPmHistStatsControl")

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

pxmNwIntfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74)
)
if mibBuilder.loadTexts:
    pxmNwIntfMIB.setRevisions(
        ("2016-05-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmNwIntfTable_Object = MibTable
pxmNwIntfTable = _PxmNwIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1)
)
if mibBuilder.loadTexts:
    pxmNwIntfTable.setStatus("current")
_PxmNwIntfEntry_Object = MibTableRow
pxmNwIntfEntry = _PxmNwIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1)
)
pxmNwIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmNwIntfEntry.setStatus("current")
_PxmNwIntfAssociatedODUCtp_Type = DisplayString
_PxmNwIntfAssociatedODUCtp_Object = MibTableColumn
pxmNwIntfAssociatedODUCtp = _PxmNwIntfAssociatedODUCtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 1),
    _PxmNwIntfAssociatedODUCtp_Type()
)
pxmNwIntfAssociatedODUCtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfAssociatedODUCtp.setStatus("current")
_PxmNwIntfMTUSize_Type = Integer32
_PxmNwIntfMTUSize_Object = MibTableColumn
pxmNwIntfMTUSize = _PxmNwIntfMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 2),
    _PxmNwIntfMTUSize_Type()
)
pxmNwIntfMTUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfMTUSize.setStatus("current")
_PxmNwIntfInterfaceRate_Type = Integer32
_PxmNwIntfInterfaceRate_Object = MibTableColumn
pxmNwIntfInterfaceRate = _PxmNwIntfInterfaceRate_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 3),
    _PxmNwIntfInterfaceRate_Type()
)
pxmNwIntfInterfaceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfInterfaceRate.setStatus("current")
_PxmNwIntfOverbookingFactor_Type = FloatTenths
_PxmNwIntfOverbookingFactor_Object = MibTableColumn
pxmNwIntfOverbookingFactor = _PxmNwIntfOverbookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 4),
    _PxmNwIntfOverbookingFactor_Type()
)
pxmNwIntfOverbookingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmNwIntfOverbookingFactor.setStatus("current")
_PxmNwIntfMaxReservableBW_Type = FloatHundredths
_PxmNwIntfMaxReservableBW_Object = MibTableColumn
pxmNwIntfMaxReservableBW = _PxmNwIntfMaxReservableBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 5),
    _PxmNwIntfMaxReservableBW_Type()
)
pxmNwIntfMaxReservableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfMaxReservableBW.setStatus("current")
_PxmNwIntfAvailableBW_Type = FloatHundredths
_PxmNwIntfAvailableBW_Object = MibTableColumn
pxmNwIntfAvailableBW = _PxmNwIntfAvailableBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 6),
    _PxmNwIntfAvailableBW_Type()
)
pxmNwIntfAvailableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfAvailableBW.setStatus("current")
_PxmNwIntfPmHistStatsEnable_Type = InfnPmHistStatsControl
_PxmNwIntfPmHistStatsEnable_Object = MibTableColumn
pxmNwIntfPmHistStatsEnable = _PxmNwIntfPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 7),
    _PxmNwIntfPmHistStatsEnable_Type()
)
pxmNwIntfPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmNwIntfPmHistStatsEnable.setStatus("current")
_PxmNwIntfMacAddress_Type = DisplayString
_PxmNwIntfMacAddress_Object = MibTableColumn
pxmNwIntfMacAddress = _PxmNwIntfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 1, 1, 8),
    _PxmNwIntfMacAddress_Type()
)
pxmNwIntfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmNwIntfMacAddress.setStatus("current")
_PxmNwIntfConformance_ObjectIdentity = ObjectIdentity
pxmNwIntfConformance = _PxmNwIntfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 3)
)
_PxmNwIntfCompliances_ObjectIdentity = ObjectIdentity
pxmNwIntfCompliances = _PxmNwIntfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 3, 1)
)
_PxmNwIntfGroups_ObjectIdentity = ObjectIdentity
pxmNwIntfGroups = _PxmNwIntfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 3, 2)
)

# Managed Objects groups

pxmNwIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 3, 2, 1)
)
pxmNwIntfGroup.setObjects(
      *(("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfAssociatedODUCtp"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfMTUSize"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfInterfaceRate"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfOverbookingFactor"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfMaxReservableBW"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfAvailableBW"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfPmHistStatsEnable"),
        ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfMacAddress"))
)
if mibBuilder.loadTexts:
    pxmNwIntfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmNwIntfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 74, 3, 1, 1)
)
pxmNwIntfCompliance.setObjects(
    ("INFINERA-TP-PXMNWINTF-MIB", "pxmNwIntfGroup")
)
if mibBuilder.loadTexts:
    pxmNwIntfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMNWINTF-MIB",
    **{"pxmNwIntfMIB": pxmNwIntfMIB,
       "pxmNwIntfTable": pxmNwIntfTable,
       "pxmNwIntfEntry": pxmNwIntfEntry,
       "pxmNwIntfAssociatedODUCtp": pxmNwIntfAssociatedODUCtp,
       "pxmNwIntfMTUSize": pxmNwIntfMTUSize,
       "pxmNwIntfInterfaceRate": pxmNwIntfInterfaceRate,
       "pxmNwIntfOverbookingFactor": pxmNwIntfOverbookingFactor,
       "pxmNwIntfMaxReservableBW": pxmNwIntfMaxReservableBW,
       "pxmNwIntfAvailableBW": pxmNwIntfAvailableBW,
       "pxmNwIntfPmHistStatsEnable": pxmNwIntfPmHistStatsEnable,
       "pxmNwIntfMacAddress": pxmNwIntfMacAddress,
       "pxmNwIntfConformance": pxmNwIntfConformance,
       "pxmNwIntfCompliances": pxmNwIntfCompliances,
       "pxmNwIntfCompliance": pxmNwIntfCompliance,
       "pxmNwIntfGroups": pxmNwIntfGroups,
       "pxmNwIntfGroup": pxmNwIntfGroup}
)
