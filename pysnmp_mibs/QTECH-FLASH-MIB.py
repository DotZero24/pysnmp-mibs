# SNMP MIB module (QTECH-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-FLASH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:25 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47)
)
if mibBuilder.loadTexts:
    qtechFlashMIB.setRevisions(
        ("2009-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechFlashMIBObjects_ObjectIdentity = ObjectIdentity
qtechFlashMIBObjects = _QtechFlashMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1)
)
_RujieFlashDeviceTable_Object = MibTable
rujieFlashDeviceTable = _RujieFlashDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1)
)
if mibBuilder.loadTexts:
    rujieFlashDeviceTable.setStatus("current")
_RujieFlashDeviceEntry_Object = MibTableRow
rujieFlashDeviceEntry = _RujieFlashDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1, 1)
)
rujieFlashDeviceEntry.setIndexNames(
    (0, "QTECH-FLASH-MIB", "qtechFlashDeviceIndex"),
)
if mibBuilder.loadTexts:
    rujieFlashDeviceEntry.setStatus("current")
_QtechFlashDeviceIndex_Type = Unsigned32
_QtechFlashDeviceIndex_Object = MibTableColumn
qtechFlashDeviceIndex = _QtechFlashDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1, 1, 1),
    _QtechFlashDeviceIndex_Type()
)
qtechFlashDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFlashDeviceIndex.setStatus("current")
_QtechFlashDeviceName_Type = DisplayString
_QtechFlashDeviceName_Object = MibTableColumn
qtechFlashDeviceName = _QtechFlashDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1, 1, 2),
    _QtechFlashDeviceName_Type()
)
qtechFlashDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFlashDeviceName.setStatus("current")
_QtechFlashDeviceSize_Type = Unsigned32
_QtechFlashDeviceSize_Object = MibTableColumn
qtechFlashDeviceSize = _QtechFlashDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1, 1, 3),
    _QtechFlashDeviceSize_Type()
)
qtechFlashDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFlashDeviceSize.setStatus("current")
_QtechFlashDeviceUsed_Type = Unsigned32
_QtechFlashDeviceUsed_Object = MibTableColumn
qtechFlashDeviceUsed = _QtechFlashDeviceUsed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1, 1, 4),
    _QtechFlashDeviceUsed_Type()
)
qtechFlashDeviceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFlashDeviceUsed.setStatus("current")
_QtechFlashDeviceFree_Type = Unsigned32
_QtechFlashDeviceFree_Object = MibTableColumn
qtechFlashDeviceFree = _QtechFlashDeviceFree_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 1, 1, 5),
    _QtechFlashDeviceFree_Type()
)
qtechFlashDeviceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFlashDeviceFree.setStatus("current")
_QtechBootromDeviceTable_Object = MibTable
qtechBootromDeviceTable = _QtechBootromDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 2)
)
if mibBuilder.loadTexts:
    qtechBootromDeviceTable.setStatus("current")
_QtechBootromDeviceEntry_Object = MibTableRow
qtechBootromDeviceEntry = _QtechBootromDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 2, 1)
)
qtechBootromDeviceEntry.setIndexNames(
    (0, "QTECH-FLASH-MIB", "qtechBootromDeviceIndex"),
)
if mibBuilder.loadTexts:
    qtechBootromDeviceEntry.setStatus("current")
_QtechBootromDeviceIndex_Type = Unsigned32
_QtechBootromDeviceIndex_Object = MibTableColumn
qtechBootromDeviceIndex = _QtechBootromDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 2, 1, 1),
    _QtechBootromDeviceIndex_Type()
)
qtechBootromDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBootromDeviceIndex.setStatus("current")
_QtechBootromDeviceName_Type = DisplayString
_QtechBootromDeviceName_Object = MibTableColumn
qtechBootromDeviceName = _QtechBootromDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 2, 1, 2),
    _QtechBootromDeviceName_Type()
)
qtechBootromDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBootromDeviceName.setStatus("current")
_QtechBootromDeviceSize_Type = Unsigned32
_QtechBootromDeviceSize_Object = MibTableColumn
qtechBootromDeviceSize = _QtechBootromDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 1, 2, 1, 3),
    _QtechBootromDeviceSize_Type()
)
qtechBootromDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBootromDeviceSize.setStatus("current")
_QtechFlashMIBConformance_ObjectIdentity = ObjectIdentity
qtechFlashMIBConformance = _QtechFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 2)
)
_QtechFlashMIBCompliances_ObjectIdentity = ObjectIdentity
qtechFlashMIBCompliances = _QtechFlashMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 2, 1)
)
_QtechFlashMIBGroups_ObjectIdentity = ObjectIdentity
qtechFlashMIBGroups = _QtechFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 2, 2)
)

# Managed Objects groups

qtechFlashMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 2, 2, 1)
)
qtechFlashMIBGroup.setObjects(
      *(("QTECH-FLASH-MIB", "qtechFlashDeviceIndex"),
        ("QTECH-FLASH-MIB", "qtechFlashDeviceName"),
        ("QTECH-FLASH-MIB", "qtechFlashDeviceSize"),
        ("QTECH-FLASH-MIB", "qtechFlashDeviceUsed"),
        ("QTECH-FLASH-MIB", "qtechFlashDeviceFree"))
)
if mibBuilder.loadTexts:
    qtechFlashMIBGroup.setStatus("current")

qtechBootromDeviceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 2, 2, 2)
)
qtechBootromDeviceMIBGroup.setObjects(
      *(("QTECH-FLASH-MIB", "qtechBootromDeviceIndex"),
        ("QTECH-FLASH-MIB", "qtechBootromDeviceName"),
        ("QTECH-FLASH-MIB", "qtechBootromDeviceSize"))
)
if mibBuilder.loadTexts:
    qtechBootromDeviceMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechFlashMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 47, 2, 1, 1)
)
qtechFlashMIBCompliance.setObjects(
    ("QTECH-FLASH-MIB", "qtechFlashMIBGroup")
)
if mibBuilder.loadTexts:
    qtechFlashMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-FLASH-MIB",
    **{"qtechFlashMIB": qtechFlashMIB,
       "qtechFlashMIBObjects": qtechFlashMIBObjects,
       "rujieFlashDeviceTable": rujieFlashDeviceTable,
       "rujieFlashDeviceEntry": rujieFlashDeviceEntry,
       "qtechFlashDeviceIndex": qtechFlashDeviceIndex,
       "qtechFlashDeviceName": qtechFlashDeviceName,
       "qtechFlashDeviceSize": qtechFlashDeviceSize,
       "qtechFlashDeviceUsed": qtechFlashDeviceUsed,
       "qtechFlashDeviceFree": qtechFlashDeviceFree,
       "qtechBootromDeviceTable": qtechBootromDeviceTable,
       "qtechBootromDeviceEntry": qtechBootromDeviceEntry,
       "qtechBootromDeviceIndex": qtechBootromDeviceIndex,
       "qtechBootromDeviceName": qtechBootromDeviceName,
       "qtechBootromDeviceSize": qtechBootromDeviceSize,
       "qtechFlashMIBConformance": qtechFlashMIBConformance,
       "qtechFlashMIBCompliances": qtechFlashMIBCompliances,
       "qtechFlashMIBCompliance": qtechFlashMIBCompliance,
       "qtechFlashMIBGroups": qtechFlashMIBGroups,
       "qtechFlashMIBGroup": qtechFlashMIBGroup,
       "qtechBootromDeviceMIBGroup": qtechBootromDeviceMIBGroup}
)
