# SNMP MIB module (ADTRAN-GEN-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:16 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenVlan,
 adGenVlanID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenVlan",
    "adGenVlanID")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

adGenVlanModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 39, 1)
)
if mibBuilder.loadTexts:
    adGenVlanModuleIdentity.setRevisions(
        ("2011-03-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenVlanSlotTable_Object = MibTable
adGenVlanSlotTable = _AdGenVlanSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 1)
)
if mibBuilder.loadTexts:
    adGenVlanSlotTable.setStatus("current")
_AdGenVlanSlotEntry_Object = MibTableRow
adGenVlanSlotEntry = _AdGenVlanSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 1, 1)
)
adGenVlanSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVlanSlotEntry.setStatus("current")
_AdGenVlanCount_Type = Integer32
_AdGenVlanCount_Object = MibTableColumn
adGenVlanCount = _AdGenVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 1, 1, 1),
    _AdGenVlanCount_Type()
)
adGenVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVlanCount.setStatus("current")
_AdGenVlanInterfaceList_Type = DisplayString
_AdGenVlanInterfaceList_Object = MibTableColumn
adGenVlanInterfaceList = _AdGenVlanInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 1, 1, 2),
    _AdGenVlanInterfaceList_Type()
)
adGenVlanInterfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVlanInterfaceList.setStatus("current")
_AdGenVlanDisplayTable_Object = MibTable
adGenVlanDisplayTable = _AdGenVlanDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 2)
)
if mibBuilder.loadTexts:
    adGenVlanDisplayTable.setStatus("current")
_AdGenVlanDisplayEntry_Object = MibTableRow
adGenVlanDisplayEntry = _AdGenVlanDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 2, 1)
)
adGenVlanDisplayEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GEN-VLAN-MIB", "adGenVlanSTag"),
)
if mibBuilder.loadTexts:
    adGenVlanDisplayEntry.setStatus("current")


class _AdGenVlanSTag_Type(Integer32):
    """Custom type adGenVlanSTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AdGenVlanSTag_Type.__name__ = "Integer32"
_AdGenVlanSTag_Object = MibTableColumn
adGenVlanSTag = _AdGenVlanSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 2, 1, 1),
    _AdGenVlanSTag_Type()
)
adGenVlanSTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVlanSTag.setStatus("current")
_AdGenVlanName_Type = DisplayString
_AdGenVlanName_Object = MibTableColumn
adGenVlanName = _AdGenVlanName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 2, 1, 2),
    _AdGenVlanName_Type()
)
adGenVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVlanName.setStatus("current")
_AdGenVlanDisplayText_Type = DisplayString
_AdGenVlanDisplayText_Object = MibTableColumn
adGenVlanDisplayText = _AdGenVlanDisplayText_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 39, 2, 1, 3),
    _AdGenVlanDisplayText_Type()
)
adGenVlanDisplayText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVlanDisplayText.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-VLAN-MIB",
    **{"adGenVlanSlotTable": adGenVlanSlotTable,
       "adGenVlanSlotEntry": adGenVlanSlotEntry,
       "adGenVlanCount": adGenVlanCount,
       "adGenVlanInterfaceList": adGenVlanInterfaceList,
       "adGenVlanDisplayTable": adGenVlanDisplayTable,
       "adGenVlanDisplayEntry": adGenVlanDisplayEntry,
       "adGenVlanSTag": adGenVlanSTag,
       "adGenVlanName": adGenVlanName,
       "adGenVlanDisplayText": adGenVlanDisplayText,
       "adGenVlanModuleIdentity": adGenVlanModuleIdentity}
)
