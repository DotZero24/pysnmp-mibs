# SNMP MIB module (ADTRAN-TA5K-GENSLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-GENSLOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:24 2025
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

(adGenericShelves,) = mibBuilder.importSymbols(
    "ADTRAN-GENCHASSIS-MIB",
    "adGenericShelves")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kSlot,
 adGenTa5kSlotID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kSlot",
    "adGenTa5kSlotID")

(AdPresence,
 AdProductIdentifier) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "AdPresence",
    "AdProductIdentifier")

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

adGenTa5kSlotModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 8, 1)
)
if mibBuilder.loadTexts:
    adGenTa5kSlotModuleIdentity.setRevisions(
        ("2014-10-09 00:00",
         "2013-10-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenTa5kSlotTable_Object = MibTable
adGenTa5kSlotTable = _AdGenTa5kSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1)
)
if mibBuilder.loadTexts:
    adGenTa5kSlotTable.setStatus("current")
_AdGenTa5kSlotEntry_Object = MibTableRow
adGenTa5kSlotEntry = _AdGenTa5kSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1)
)
adGenTa5kSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kSlotEntry.setStatus("current")
_AdGenTa5kSlotRestoreFactoryDefaults_Type = Integer32
_AdGenTa5kSlotRestoreFactoryDefaults_Object = MibTableColumn
adGenTa5kSlotRestoreFactoryDefaults = _AdGenTa5kSlotRestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 1),
    _AdGenTa5kSlotRestoreFactoryDefaults_Type()
)
adGenTa5kSlotRestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kSlotRestoreFactoryDefaults.setStatus("current")
_AdGenTa5kSlotReboot_Type = Integer32
_AdGenTa5kSlotReboot_Object = MibTableColumn
adGenTa5kSlotReboot = _AdGenTa5kSlotReboot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 2),
    _AdGenTa5kSlotReboot_Type()
)
adGenTa5kSlotReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTa5kSlotReboot.setStatus("current")
_AdGenTa5kSlotMaxMacs_Type = Integer32
_AdGenTa5kSlotMaxMacs_Object = MibTableColumn
adGenTa5kSlotMaxMacs = _AdGenTa5kSlotMaxMacs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 3),
    _AdGenTa5kSlotMaxMacs_Type()
)
adGenTa5kSlotMaxMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotMaxMacs.setStatus("current")


class _AdGenTa5kSlotFlashStatus_Type(Integer32):
    """Custom type adGenTa5kSlotFlashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 1),
          ("idle", 2))
    )


_AdGenTa5kSlotFlashStatus_Type.__name__ = "Integer32"
_AdGenTa5kSlotFlashStatus_Object = MibTableColumn
adGenTa5kSlotFlashStatus = _AdGenTa5kSlotFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 4),
    _AdGenTa5kSlotFlashStatus_Type()
)
adGenTa5kSlotFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotFlashStatus.setStatus("current")
_AdGenTa5kSlotSystemSwVersion_Type = DisplayString
_AdGenTa5kSlotSystemSwVersion_Object = MibTableColumn
adGenTa5kSlotSystemSwVersion = _AdGenTa5kSlotSystemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 5),
    _AdGenTa5kSlotSystemSwVersion_Type()
)
adGenTa5kSlotSystemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotSystemSwVersion.setStatus("current")
_AdGenTa5kSlotBootSwVersion_Type = DisplayString
_AdGenTa5kSlotBootSwVersion_Object = MibTableColumn
adGenTa5kSlotBootSwVersion = _AdGenTa5kSlotBootSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 6),
    _AdGenTa5kSlotBootSwVersion_Type()
)
adGenTa5kSlotBootSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotBootSwVersion.setStatus("current")
_AdGenTa5kSlotBootSystemSwVersion_Type = DisplayString
_AdGenTa5kSlotBootSystemSwVersion_Object = MibTableColumn
adGenTa5kSlotBootSystemSwVersion = _AdGenTa5kSlotBootSystemSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 7),
    _AdGenTa5kSlotBootSystemSwVersion_Type()
)
adGenTa5kSlotBootSystemSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotBootSystemSwVersion.setStatus("current")
_AdGenTa5kSlotDateOfManufacture_Type = DisplayString
_AdGenTa5kSlotDateOfManufacture_Object = MibTableColumn
adGenTa5kSlotDateOfManufacture = _AdGenTa5kSlotDateOfManufacture_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 8),
    _AdGenTa5kSlotDateOfManufacture_Type()
)
adGenTa5kSlotDateOfManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotDateOfManufacture.setStatus("current")
_AdGenTa5kSlotSwVerInstallTime_Type = DisplayString
_AdGenTa5kSlotSwVerInstallTime_Object = MibTableColumn
adGenTa5kSlotSwVerInstallTime = _AdGenTa5kSlotSwVerInstallTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 9),
    _AdGenTa5kSlotSwVerInstallTime_Type()
)
adGenTa5kSlotSwVerInstallTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotSwVerInstallTime.setStatus("current")


class _AdGenTa5kSlotIOModuleID_Type(DisplayString):
    """Custom type adGenTa5kSlotIOModuleID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenTa5kSlotIOModuleID_Type.__name__ = "DisplayString"
_AdGenTa5kSlotIOModuleID_Object = MibTableColumn
adGenTa5kSlotIOModuleID = _AdGenTa5kSlotIOModuleID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 1, 1, 10),
    _AdGenTa5kSlotIOModuleID_Type()
)
adGenTa5kSlotIOModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotIOModuleID.setStatus("current")
_AdGenTa5kSlotMacAddressTable_Object = MibTable
adGenTa5kSlotMacAddressTable = _AdGenTa5kSlotMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 2)
)
if mibBuilder.loadTexts:
    adGenTa5kSlotMacAddressTable.setStatus("current")
_AdGenTa5kSlotMacAddressEntry_Object = MibTableRow
adGenTa5kSlotMacAddressEntry = _AdGenTa5kSlotMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 2, 1)
)
adGenTa5kSlotMacAddressEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-GENSLOT-MIB", "adGenTa5kSlotMacAddressIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kSlotMacAddressEntry.setStatus("current")


class _AdGenTa5kSlotMacAddressIndex_Type(Integer32):
    """Custom type adGenTa5kSlotMacAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenTa5kSlotMacAddressIndex_Type.__name__ = "Integer32"
_AdGenTa5kSlotMacAddressIndex_Object = MibTableColumn
adGenTa5kSlotMacAddressIndex = _AdGenTa5kSlotMacAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 2, 1, 1),
    _AdGenTa5kSlotMacAddressIndex_Type()
)
adGenTa5kSlotMacAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kSlotMacAddressIndex.setStatus("current")


class _AdGenTa5kSlotMacAddress_Type(OctetString):
    """Custom type adGenTa5kSlotMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AdGenTa5kSlotMacAddress_Type.__name__ = "OctetString"
_AdGenTa5kSlotMacAddress_Object = MibTableColumn
adGenTa5kSlotMacAddress = _AdGenTa5kSlotMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 2, 1, 2),
    _AdGenTa5kSlotMacAddress_Type()
)
adGenTa5kSlotMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotMacAddress.setStatus("current")
_AdGenTa5kSlotDeviceTable_Object = MibTable
adGenTa5kSlotDeviceTable = _AdGenTa5kSlotDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 3)
)
if mibBuilder.loadTexts:
    adGenTa5kSlotDeviceTable.setStatus("current")
_AdGenTa5kSlotDeviceEntry_Object = MibTableRow
adGenTa5kSlotDeviceEntry = _AdGenTa5kSlotDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 3, 1)
)
adGenTa5kSlotDeviceEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-GENSLOT-MIB", "adGenTa5kSlotDeviceIndex"),
)
if mibBuilder.loadTexts:
    adGenTa5kSlotDeviceEntry.setStatus("current")


class _AdGenTa5kSlotDeviceIndex_Type(Integer32):
    """Custom type adGenTa5kSlotDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenTa5kSlotDeviceIndex_Type.__name__ = "Integer32"
_AdGenTa5kSlotDeviceIndex_Object = MibTableColumn
adGenTa5kSlotDeviceIndex = _AdGenTa5kSlotDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 3, 1, 1),
    _AdGenTa5kSlotDeviceIndex_Type()
)
adGenTa5kSlotDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenTa5kSlotDeviceIndex.setStatus("current")
_AdGenTa5kSlotDeviceDesc_Type = DisplayString
_AdGenTa5kSlotDeviceDesc_Object = MibTableColumn
adGenTa5kSlotDeviceDesc = _AdGenTa5kSlotDeviceDesc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 3, 1, 2),
    _AdGenTa5kSlotDeviceDesc_Type()
)
adGenTa5kSlotDeviceDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotDeviceDesc.setStatus("current")
_AdGenTa5kSlotDeviceRevision_Type = DisplayString
_AdGenTa5kSlotDeviceRevision_Object = MibTableColumn
adGenTa5kSlotDeviceRevision = _AdGenTa5kSlotDeviceRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 8, 3, 1, 3),
    _AdGenTa5kSlotDeviceRevision_Type()
)
adGenTa5kSlotDeviceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTa5kSlotDeviceRevision.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-GENSLOT-MIB",
    **{"adGenTa5kSlotTable": adGenTa5kSlotTable,
       "adGenTa5kSlotEntry": adGenTa5kSlotEntry,
       "adGenTa5kSlotRestoreFactoryDefaults": adGenTa5kSlotRestoreFactoryDefaults,
       "adGenTa5kSlotReboot": adGenTa5kSlotReboot,
       "adGenTa5kSlotMaxMacs": adGenTa5kSlotMaxMacs,
       "adGenTa5kSlotFlashStatus": adGenTa5kSlotFlashStatus,
       "adGenTa5kSlotSystemSwVersion": adGenTa5kSlotSystemSwVersion,
       "adGenTa5kSlotBootSwVersion": adGenTa5kSlotBootSwVersion,
       "adGenTa5kSlotBootSystemSwVersion": adGenTa5kSlotBootSystemSwVersion,
       "adGenTa5kSlotDateOfManufacture": adGenTa5kSlotDateOfManufacture,
       "adGenTa5kSlotSwVerInstallTime": adGenTa5kSlotSwVerInstallTime,
       "adGenTa5kSlotIOModuleID": adGenTa5kSlotIOModuleID,
       "adGenTa5kSlotMacAddressTable": adGenTa5kSlotMacAddressTable,
       "adGenTa5kSlotMacAddressEntry": adGenTa5kSlotMacAddressEntry,
       "adGenTa5kSlotMacAddressIndex": adGenTa5kSlotMacAddressIndex,
       "adGenTa5kSlotMacAddress": adGenTa5kSlotMacAddress,
       "adGenTa5kSlotDeviceTable": adGenTa5kSlotDeviceTable,
       "adGenTa5kSlotDeviceEntry": adGenTa5kSlotDeviceEntry,
       "adGenTa5kSlotDeviceIndex": adGenTa5kSlotDeviceIndex,
       "adGenTa5kSlotDeviceDesc": adGenTa5kSlotDeviceDesc,
       "adGenTa5kSlotDeviceRevision": adGenTa5kSlotDeviceRevision,
       "adGenTa5kSlotModuleIdentity": adGenTa5kSlotModuleIdentity}
)
