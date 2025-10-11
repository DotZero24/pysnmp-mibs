# SNMP MIB module (ADTRAN-GENSLOT-SUB-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENSLOT-SUB-MODULE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:13 2025
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

(adGenSlot,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlot",
    "adGenSlotInfoIndex")

(AdProductIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "AdProductIdentifier")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenSubSlotModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenSubSlotProdTable_Object = MibTable
adGenSubSlotProdTable = _AdGenSubSlotProdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8)
)
if mibBuilder.loadTexts:
    adGenSubSlotProdTable.setStatus("current")
_AdGenSubSlotProdEntry_Object = MibTableRow
adGenSubSlotProdEntry = _AdGenSubSlotProdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1)
)
adGenSubSlotProdEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENSLOT-SUB-MODULE-MIB", "adGenSubSlotProdInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSubSlotProdEntry.setStatus("current")
_AdGenSubSlotProdInfoIndex_Type = Integer32
_AdGenSubSlotProdInfoIndex_Object = MibTableColumn
adGenSubSlotProdInfoIndex = _AdGenSubSlotProdInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 1),
    _AdGenSubSlotProdInfoIndex_Type()
)
adGenSubSlotProdInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdInfoIndex.setStatus("current")
_AdGenSubSlotProdName_Type = DisplayString
_AdGenSubSlotProdName_Object = MibTableColumn
adGenSubSlotProdName = _AdGenSubSlotProdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 2),
    _AdGenSubSlotProdName_Type()
)
adGenSubSlotProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdName.setStatus("current")
_AdGenSubSlotProdPartNumber_Type = DisplayString
_AdGenSubSlotProdPartNumber_Object = MibTableColumn
adGenSubSlotProdPartNumber = _AdGenSubSlotProdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 3),
    _AdGenSubSlotProdPartNumber_Type()
)
adGenSubSlotProdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdPartNumber.setStatus("current")
_AdGenSubSlotProdCLEIcode_Type = DisplayString
_AdGenSubSlotProdCLEIcode_Object = MibTableColumn
adGenSubSlotProdCLEIcode = _AdGenSubSlotProdCLEIcode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 4),
    _AdGenSubSlotProdCLEIcode_Type()
)
adGenSubSlotProdCLEIcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdCLEIcode.setStatus("current")
_AdGenSubSlotProdSerialNumber_Type = DisplayString
_AdGenSubSlotProdSerialNumber_Object = MibTableColumn
adGenSubSlotProdSerialNumber = _AdGenSubSlotProdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 5),
    _AdGenSubSlotProdSerialNumber_Type()
)
adGenSubSlotProdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdSerialNumber.setStatus("current")
_AdGenSubSlotProdRevision_Type = DisplayString
_AdGenSubSlotProdRevision_Object = MibTableColumn
adGenSubSlotProdRevision = _AdGenSubSlotProdRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 6),
    _AdGenSubSlotProdRevision_Type()
)
adGenSubSlotProdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdRevision.setStatus("current")
_AdGenSubSlotProdSwVersion_Type = DisplayString
_AdGenSubSlotProdSwVersion_Object = MibTableColumn
adGenSubSlotProdSwVersion = _AdGenSubSlotProdSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 7),
    _AdGenSubSlotProdSwVersion_Type()
)
adGenSubSlotProdSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdSwVersion.setStatus("current")
_AdGenSubSlotProdDateOfManufacturing_Type = DisplayString
_AdGenSubSlotProdDateOfManufacturing_Object = MibTableColumn
adGenSubSlotProdDateOfManufacturing = _AdGenSubSlotProdDateOfManufacturing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 8, 1, 8),
    _AdGenSubSlotProdDateOfManufacturing_Type()
)
adGenSubSlotProdDateOfManufacturing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubSlotProdDateOfManufacturing.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENSLOT-SUB-MODULE-MIB",
    **{"adGenSubSlotModule": adGenSubSlotModule,
       "adGenSubSlotProdTable": adGenSubSlotProdTable,
       "adGenSubSlotProdEntry": adGenSubSlotProdEntry,
       "adGenSubSlotProdInfoIndex": adGenSubSlotProdInfoIndex,
       "adGenSubSlotProdName": adGenSubSlotProdName,
       "adGenSubSlotProdPartNumber": adGenSubSlotProdPartNumber,
       "adGenSubSlotProdCLEIcode": adGenSubSlotProdCLEIcode,
       "adGenSubSlotProdSerialNumber": adGenSubSlotProdSerialNumber,
       "adGenSubSlotProdRevision": adGenSubSlotProdRevision,
       "adGenSubSlotProdSwVersion": adGenSubSlotProdSwVersion,
       "adGenSubSlotProdDateOfManufacturing": adGenSubSlotProdDateOfManufacturing}
)
