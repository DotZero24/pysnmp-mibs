# SNMP MIB module (MX-LINE-SELECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-LINE-SELECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:31 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxDigitMap,
 MxEnableState) = mibBuilder.importSymbols(
    "MX-TC",
    "MxDigitMap",
    "MxEnableState")

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

lineSelectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90)
)
if mibBuilder.loadTexts:
    lineSelectionMIB.setRevisions(
        ("1903-03-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LineSelectionMIBObjects_ObjectIdentity = ObjectIdentity
lineSelectionMIBObjects = _LineSelectionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 1)
)
_LineSelectionIfCustomizationTable_Object = MibTable
lineSelectionIfCustomizationTable = _LineSelectionIfCustomizationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10)
)
if mibBuilder.loadTexts:
    lineSelectionIfCustomizationTable.setStatus("current")
_LineSelectionIfCustomizationEntry_Object = MibTableRow
lineSelectionIfCustomizationEntry = _LineSelectionIfCustomizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10, 5)
)
lineSelectionIfCustomizationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lineSelectionIfCustomizationEntry.setStatus("current")


class _LineSelectionEnable_Type(MxEnableState):
    """Custom type lineSelectionEnable based on MxEnableState"""
    defaultValue = 0


_LineSelectionEnable_Type.__name__ = "MxEnableState"
_LineSelectionEnable_Object = MibTableColumn
lineSelectionEnable = _LineSelectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10, 5, 5),
    _LineSelectionEnable_Type()
)
lineSelectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSelectionEnable.setStatus("current")


class _LineSelectionDigitMap_Type(MxDigitMap):
    """Custom type lineSelectionDigitMap based on MxDigitMap"""
    defaultValue = OctetString("")


_LineSelectionDigitMap_Type.__name__ = "MxDigitMap"
_LineSelectionDigitMap_Object = MibTableColumn
lineSelectionDigitMap = _LineSelectionDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 1, 10, 5, 10),
    _LineSelectionDigitMap_Type()
)
lineSelectionDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSelectionDigitMap.setStatus("current")
_LineSelectionConformance_ObjectIdentity = ObjectIdentity
lineSelectionConformance = _LineSelectionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 5)
)
_LineSelectionCompliances_ObjectIdentity = ObjectIdentity
lineSelectionCompliances = _LineSelectionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 1)
)
_LineSelectionGroups_ObjectIdentity = ObjectIdentity
lineSelectionGroups = _LineSelectionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 5)
)

# Managed Objects groups

lineSelectionCustomizationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 5, 10)
)
lineSelectionCustomizationVer1.setObjects(
      *(("MX-LINE-SELECTION-MIB", "lineSelectionEnable"),
        ("MX-LINE-SELECTION-MIB", "lineSelectionDigitMap"))
)
if mibBuilder.loadTexts:
    lineSelectionCustomizationVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lineSelectionComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 90, 5, 1, 1)
)
lineSelectionComplVer1.setObjects(
    ("MX-LINE-SELECTION-MIB", "lineSelectionCustomizationVer1")
)
if mibBuilder.loadTexts:
    lineSelectionComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-LINE-SELECTION-MIB",
    **{"lineSelectionMIB": lineSelectionMIB,
       "lineSelectionMIBObjects": lineSelectionMIBObjects,
       "lineSelectionIfCustomizationTable": lineSelectionIfCustomizationTable,
       "lineSelectionIfCustomizationEntry": lineSelectionIfCustomizationEntry,
       "lineSelectionEnable": lineSelectionEnable,
       "lineSelectionDigitMap": lineSelectionDigitMap,
       "lineSelectionConformance": lineSelectionConformance,
       "lineSelectionCompliances": lineSelectionCompliances,
       "lineSelectionComplVer1": lineSelectionComplVer1,
       "lineSelectionGroups": lineSelectionGroups,
       "lineSelectionCustomizationVer1": lineSelectionCustomizationVer1}
)
