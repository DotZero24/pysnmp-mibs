# SNMP MIB module (CAMBIUM-NETWORKS-USB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-USB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:43 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnUsbMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3)
)
if mibBuilder.loadTexts:
    cnUsbMib.setRevisions(
        ("2019-03-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnUsbMountDevice_ObjectIdentity = ObjectIdentity
cnUsbMountDevice = _CnUsbMountDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 0)
)


class _CnUsbMount_Type(Integer32):
    """Custom type cnUsbMount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mount", 1),
          ("unmount", 2))
    )


_CnUsbMount_Type.__name__ = "Integer32"
_CnUsbMount_Object = MibScalar
cnUsbMount = _CnUsbMount_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 0, 1),
    _CnUsbMount_Type()
)
cnUsbMount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnUsbMount.setStatus("current")
_CnUsbDeviceTable_ObjectIdentity = ObjectIdentity
cnUsbDeviceTable = _CnUsbDeviceTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1)
)
_CnUsbTable_Object = MibTable
cnUsbTable = _CnUsbTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cnUsbTable.setStatus("current")
_CnUsbEntry_Object = MibTableRow
cnUsbEntry = _CnUsbEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1)
)
cnUsbEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-USB-MIB", "cnUsbSlotIndex"),
)
if mibBuilder.loadTexts:
    cnUsbEntry.setStatus("current")


class _CnUsbSlotIndex_Type(Integer32):
    """Custom type cnUsbSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CnUsbSlotIndex_Type.__name__ = "Integer32"
_CnUsbSlotIndex_Object = MibTableColumn
cnUsbSlotIndex = _CnUsbSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 1),
    _CnUsbSlotIndex_Type()
)
cnUsbSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnUsbSlotIndex.setStatus("current")


class _CnUsbSlotDescription_Type(OctetString):
    """Custom type cnUsbSlotDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CnUsbSlotDescription_Type.__name__ = "OctetString"
_CnUsbSlotDescription_Object = MibTableColumn
cnUsbSlotDescription = _CnUsbSlotDescription_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 2),
    _CnUsbSlotDescription_Type()
)
cnUsbSlotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbSlotDescription.setStatus("current")


class _CnUsbVendorId_Type(OctetString):
    """Custom type cnUsbVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnUsbVendorId_Type.__name__ = "OctetString"
_CnUsbVendorId_Object = MibTableColumn
cnUsbVendorId = _CnUsbVendorId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 3),
    _CnUsbVendorId_Type()
)
cnUsbVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbVendorId.setStatus("current")


class _CnUsbManufacturer_Type(OctetString):
    """Custom type cnUsbManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnUsbManufacturer_Type.__name__ = "OctetString"
_CnUsbManufacturer_Object = MibTableColumn
cnUsbManufacturer = _CnUsbManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 4),
    _CnUsbManufacturer_Type()
)
cnUsbManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbManufacturer.setStatus("current")


class _CnUsbProductId_Type(OctetString):
    """Custom type cnUsbProductId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnUsbProductId_Type.__name__ = "OctetString"
_CnUsbProductId_Object = MibTableColumn
cnUsbProductId = _CnUsbProductId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 5),
    _CnUsbProductId_Type()
)
cnUsbProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbProductId.setStatus("current")


class _CnUsbProductName_Type(OctetString):
    """Custom type cnUsbProductName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnUsbProductName_Type.__name__ = "OctetString"
_CnUsbProductName_Object = MibTableColumn
cnUsbProductName = _CnUsbProductName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 6),
    _CnUsbProductName_Type()
)
cnUsbProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbProductName.setStatus("current")


class _CnUsbSerialNumber_Type(OctetString):
    """Custom type cnUsbSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnUsbSerialNumber_Type.__name__ = "OctetString"
_CnUsbSerialNumber_Object = MibTableColumn
cnUsbSerialNumber = _CnUsbSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 7),
    _CnUsbSerialNumber_Type()
)
cnUsbSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbSerialNumber.setStatus("current")


class _CnUsbVersion_Type(OctetString):
    """Custom type cnUsbVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CnUsbVersion_Type.__name__ = "OctetString"
_CnUsbVersion_Object = MibTableColumn
cnUsbVersion = _CnUsbVersion_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 8),
    _CnUsbVersion_Type()
)
cnUsbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbVersion.setStatus("current")
_CnUsbMaxCurrent_Type = Integer32
_CnUsbMaxCurrent_Object = MibTableColumn
cnUsbMaxCurrent = _CnUsbMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 1, 1, 1, 9),
    _CnUsbMaxCurrent_Type()
)
cnUsbMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbMaxCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cnUsbMaxCurrent.setUnits("milliamps")
_CnUsbDeviceFiles_ObjectIdentity = ObjectIdentity
cnUsbDeviceFiles = _CnUsbDeviceFiles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2)
)
_CnUsbFile_Object = MibTable
cnUsbFile = _CnUsbFile_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cnUsbFile.setStatus("current")
_CnUsbFileEntry_Object = MibTableRow
cnUsbFileEntry = _CnUsbFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2, 1, 1)
)
cnUsbFileEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-USB-MIB", "cnUsbSlotIndex"),
)
if mibBuilder.loadTexts:
    cnUsbFileEntry.setStatus("current")


class _CnUsbFileSlot_Type(Integer32):
    """Custom type cnUsbFileSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CnUsbFileSlot_Type.__name__ = "Integer32"
_CnUsbFileSlot_Object = MibTableColumn
cnUsbFileSlot = _CnUsbFileSlot_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2, 1, 1, 1),
    _CnUsbFileSlot_Type()
)
cnUsbFileSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnUsbFileSlot.setStatus("current")


class _CnUsbFileName_Type(OctetString):
    """Custom type cnUsbFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 114),
    )


_CnUsbFileName_Type.__name__ = "OctetString"
_CnUsbFileName_Object = MibTableColumn
cnUsbFileName = _CnUsbFileName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2, 1, 1, 2),
    _CnUsbFileName_Type()
)
cnUsbFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnUsbFileName.setStatus("current")


class _CnUsbFileDate_Type(OctetString):
    """Custom type cnUsbFileDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnUsbFileDate_Type.__name__ = "OctetString"
_CnUsbFileDate_Object = MibTableColumn
cnUsbFileDate = _CnUsbFileDate_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2, 1, 1, 3),
    _CnUsbFileDate_Type()
)
cnUsbFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbFileDate.setStatus("current")
_CnUsbFileSize_Type = Unsigned32
_CnUsbFileSize_Object = MibTableColumn
cnUsbFileSize = _CnUsbFileSize_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 3, 2, 1, 1, 4),
    _CnUsbFileSize_Type()
)
cnUsbFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnUsbFileSize.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-USB-MIB",
    **{"cnUsbMib": cnUsbMib,
       "cnUsbMountDevice": cnUsbMountDevice,
       "cnUsbMount": cnUsbMount,
       "cnUsbDeviceTable": cnUsbDeviceTable,
       "cnUsbTable": cnUsbTable,
       "cnUsbEntry": cnUsbEntry,
       "cnUsbSlotIndex": cnUsbSlotIndex,
       "cnUsbSlotDescription": cnUsbSlotDescription,
       "cnUsbVendorId": cnUsbVendorId,
       "cnUsbManufacturer": cnUsbManufacturer,
       "cnUsbProductId": cnUsbProductId,
       "cnUsbProductName": cnUsbProductName,
       "cnUsbSerialNumber": cnUsbSerialNumber,
       "cnUsbVersion": cnUsbVersion,
       "cnUsbMaxCurrent": cnUsbMaxCurrent,
       "cnUsbDeviceFiles": cnUsbDeviceFiles,
       "cnUsbFile": cnUsbFile,
       "cnUsbFileEntry": cnUsbFileEntry,
       "cnUsbFileSlot": cnUsbFileSlot,
       "cnUsbFileName": cnUsbFileName,
       "cnUsbFileDate": cnUsbFileDate,
       "cnUsbFileSize": cnUsbFileSize}
)
