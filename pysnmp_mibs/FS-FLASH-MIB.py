# SNMP MIB module (FS-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-FLASH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:19 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsFlashMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47)
)
if mibBuilder.loadTexts:
    fsFlashMIB.setRevisions(
        ("2009-10-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsFlashMIBObjects_ObjectIdentity = ObjectIdentity
fsFlashMIBObjects = _FsFlashMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1)
)
_FsFlashDeviceTable_Object = MibTable
fsFlashDeviceTable = _FsFlashDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1)
)
if mibBuilder.loadTexts:
    fsFlashDeviceTable.setStatus("current")
_FsFlashDeviceEntry_Object = MibTableRow
fsFlashDeviceEntry = _FsFlashDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1, 1)
)
fsFlashDeviceEntry.setIndexNames(
    (0, "FS-FLASH-MIB", "fsFlashDeviceIndex"),
)
if mibBuilder.loadTexts:
    fsFlashDeviceEntry.setStatus("current")
_FsFlashDeviceIndex_Type = Unsigned32
_FsFlashDeviceIndex_Object = MibTableColumn
fsFlashDeviceIndex = _FsFlashDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1, 1, 1),
    _FsFlashDeviceIndex_Type()
)
fsFlashDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFlashDeviceIndex.setStatus("current")
_FsFlashDeviceName_Type = DisplayString
_FsFlashDeviceName_Object = MibTableColumn
fsFlashDeviceName = _FsFlashDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1, 1, 2),
    _FsFlashDeviceName_Type()
)
fsFlashDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFlashDeviceName.setStatus("current")
_FsFlashDeviceSize_Type = Unsigned32
_FsFlashDeviceSize_Object = MibTableColumn
fsFlashDeviceSize = _FsFlashDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1, 1, 3),
    _FsFlashDeviceSize_Type()
)
fsFlashDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFlashDeviceSize.setStatus("current")
_FsFlashDeviceUsed_Type = Unsigned32
_FsFlashDeviceUsed_Object = MibTableColumn
fsFlashDeviceUsed = _FsFlashDeviceUsed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1, 1, 4),
    _FsFlashDeviceUsed_Type()
)
fsFlashDeviceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFlashDeviceUsed.setStatus("current")
_FsFlashDeviceFree_Type = Unsigned32
_FsFlashDeviceFree_Object = MibTableColumn
fsFlashDeviceFree = _FsFlashDeviceFree_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 1, 1, 5),
    _FsFlashDeviceFree_Type()
)
fsFlashDeviceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFlashDeviceFree.setStatus("current")
_FsBootromDeviceTable_Object = MibTable
fsBootromDeviceTable = _FsBootromDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 2)
)
if mibBuilder.loadTexts:
    fsBootromDeviceTable.setStatus("current")
_FsBootromDeviceEntry_Object = MibTableRow
fsBootromDeviceEntry = _FsBootromDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 2, 1)
)
fsBootromDeviceEntry.setIndexNames(
    (0, "FS-FLASH-MIB", "fsBootromDeviceIndex"),
)
if mibBuilder.loadTexts:
    fsBootromDeviceEntry.setStatus("current")
_FsBootromDeviceIndex_Type = Unsigned32
_FsBootromDeviceIndex_Object = MibTableColumn
fsBootromDeviceIndex = _FsBootromDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 2, 1, 1),
    _FsBootromDeviceIndex_Type()
)
fsBootromDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBootromDeviceIndex.setStatus("current")
_FsBootromDeviceName_Type = DisplayString
_FsBootromDeviceName_Object = MibTableColumn
fsBootromDeviceName = _FsBootromDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 2, 1, 2),
    _FsBootromDeviceName_Type()
)
fsBootromDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBootromDeviceName.setStatus("current")
_FsBootromDeviceSize_Type = Unsigned32
_FsBootromDeviceSize_Object = MibTableColumn
fsBootromDeviceSize = _FsBootromDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 1, 2, 1, 3),
    _FsBootromDeviceSize_Type()
)
fsBootromDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsBootromDeviceSize.setStatus("current")
_FsFlashMIBConformance_ObjectIdentity = ObjectIdentity
fsFlashMIBConformance = _FsFlashMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 2)
)
_FsFlashMIBCompliances_ObjectIdentity = ObjectIdentity
fsFlashMIBCompliances = _FsFlashMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 2, 1)
)
_FsFlashMIBGroups_ObjectIdentity = ObjectIdentity
fsFlashMIBGroups = _FsFlashMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 2, 2)
)

# Managed Objects groups

fsFlashMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 2, 2, 1)
)
fsFlashMIBGroup.setObjects(
      *(("FS-FLASH-MIB", "fsFlashDeviceIndex"),
        ("FS-FLASH-MIB", "fsFlashDeviceName"),
        ("FS-FLASH-MIB", "fsFlashDeviceSize"),
        ("FS-FLASH-MIB", "fsFlashDeviceUsed"),
        ("FS-FLASH-MIB", "fsFlashDeviceFree"))
)
if mibBuilder.loadTexts:
    fsFlashMIBGroup.setStatus("current")

fsBootromDeviceMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 2, 2, 2)
)
fsBootromDeviceMIBGroup.setObjects(
      *(("FS-FLASH-MIB", "fsBootromDeviceIndex"),
        ("FS-FLASH-MIB", "fsBootromDeviceName"),
        ("FS-FLASH-MIB", "fsBootromDeviceSize"))
)
if mibBuilder.loadTexts:
    fsBootromDeviceMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsFlashMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 47, 2, 1, 1)
)
fsFlashMIBCompliance.setObjects(
    ("FS-FLASH-MIB", "fsFlashMIBGroup")
)
if mibBuilder.loadTexts:
    fsFlashMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-FLASH-MIB",
    **{"fsFlashMIB": fsFlashMIB,
       "fsFlashMIBObjects": fsFlashMIBObjects,
       "fsFlashDeviceTable": fsFlashDeviceTable,
       "fsFlashDeviceEntry": fsFlashDeviceEntry,
       "fsFlashDeviceIndex": fsFlashDeviceIndex,
       "fsFlashDeviceName": fsFlashDeviceName,
       "fsFlashDeviceSize": fsFlashDeviceSize,
       "fsFlashDeviceUsed": fsFlashDeviceUsed,
       "fsFlashDeviceFree": fsFlashDeviceFree,
       "fsBootromDeviceTable": fsBootromDeviceTable,
       "fsBootromDeviceEntry": fsBootromDeviceEntry,
       "fsBootromDeviceIndex": fsBootromDeviceIndex,
       "fsBootromDeviceName": fsBootromDeviceName,
       "fsBootromDeviceSize": fsBootromDeviceSize,
       "fsFlashMIBConformance": fsFlashMIBConformance,
       "fsFlashMIBCompliances": fsFlashMIBCompliances,
       "fsFlashMIBCompliance": fsFlashMIBCompliance,
       "fsFlashMIBGroups": fsFlashMIBGroups,
       "fsFlashMIBGroup": fsFlashMIBGroup,
       "fsBootromDeviceMIBGroup": fsBootromDeviceMIBGroup}
)
