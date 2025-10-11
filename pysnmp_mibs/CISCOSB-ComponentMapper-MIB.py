# SNMP MIB module (CISCOSB-ComponentMapper-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ciscosb/CISCOSB-ComponentMapper-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:39:32 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

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

rlComponentMapper = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243)
)
if mibBuilder.loadTexts:
    rlComponentMapper.setRevisions(
        ("2019-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ComponentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 1),
          ("packetProcessor", 2),
          ("phy", 3),
          ("flash", 4),
          ("sfp", 5),
          ("poe", 6),
          ("cpld", 7),
          ("image", 8),
          ("kernel", 9),
          ("bootloader", 10),
          ("fanController", 11),
          ("ssh", 12),
          ("ssl", 13),
          ("mcu", 14))
    )



# MIB Managed Objects in the order of their OIDs

_RlComponentMapperTable_Object = MibTable
rlComponentMapperTable = _RlComponentMapperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1)
)
if mibBuilder.loadTexts:
    rlComponentMapperTable.setStatus("current")
_RlComponentMapperEntry_Object = MibTableRow
rlComponentMapperEntry = _RlComponentMapperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1)
)
rlComponentMapperEntry.setIndexNames(
    (0, "CISCOSB-ComponentMapper-MIB", "rlComponentMapperUnitNum"),
    (0, "CISCOSB-ComponentMapper-MIB", "rlComponentMapperType"),
    (0, "CISCOSB-ComponentMapper-MIB", "rlComponentMapperIndex"),
)
if mibBuilder.loadTexts:
    rlComponentMapperEntry.setStatus("current")
_RlComponentMapperUnitNum_Type = Integer32
_RlComponentMapperUnitNum_Object = MibTableColumn
rlComponentMapperUnitNum = _RlComponentMapperUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 1),
    _RlComponentMapperUnitNum_Type()
)
rlComponentMapperUnitNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlComponentMapperUnitNum.setStatus("current")
_RlComponentMapperType_Type = ComponentType
_RlComponentMapperType_Object = MibTableColumn
rlComponentMapperType = _RlComponentMapperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 2),
    _RlComponentMapperType_Type()
)
rlComponentMapperType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlComponentMapperType.setStatus("current")
_RlComponentMapperIndex_Type = Integer32
_RlComponentMapperIndex_Object = MibTableColumn
rlComponentMapperIndex = _RlComponentMapperIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 3),
    _RlComponentMapperIndex_Type()
)
rlComponentMapperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlComponentMapperIndex.setStatus("current")
_RlComponentMapperVendorID_Type = DisplayString
_RlComponentMapperVendorID_Object = MibTableColumn
rlComponentMapperVendorID = _RlComponentMapperVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 4),
    _RlComponentMapperVendorID_Type()
)
rlComponentMapperVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperVendorID.setStatus("current")
_RlComponentMapperDeviceID_Type = DisplayString
_RlComponentMapperDeviceID_Object = MibTableColumn
rlComponentMapperDeviceID = _RlComponentMapperDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 5),
    _RlComponentMapperDeviceID_Type()
)
rlComponentMapperDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperDeviceID.setStatus("current")
_RlComponentMapperHardwareVersionID_Type = DisplayString
_RlComponentMapperHardwareVersionID_Object = MibTableColumn
rlComponentMapperHardwareVersionID = _RlComponentMapperHardwareVersionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 6),
    _RlComponentMapperHardwareVersionID_Type()
)
rlComponentMapperHardwareVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperHardwareVersionID.setStatus("current")
_RlComponentMapperSoftwareVersionID_Type = DisplayString
_RlComponentMapperSoftwareVersionID_Object = MibTableColumn
rlComponentMapperSoftwareVersionID = _RlComponentMapperSoftwareVersionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 7),
    _RlComponentMapperSoftwareVersionID_Type()
)
rlComponentMapperSoftwareVersionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperSoftwareVersionID.setStatus("current")
_RlComponentMapperAliasID_Type = DisplayString
_RlComponentMapperAliasID_Object = MibTableColumn
rlComponentMapperAliasID = _RlComponentMapperAliasID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 8),
    _RlComponentMapperAliasID_Type()
)
rlComponentMapperAliasID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperAliasID.setStatus("current")
_RlComponentMapperProductNumber_Type = DisplayString
_RlComponentMapperProductNumber_Object = MibTableColumn
rlComponentMapperProductNumber = _RlComponentMapperProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 9),
    _RlComponentMapperProductNumber_Type()
)
rlComponentMapperProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperProductNumber.setStatus("current")
_RlComponentMapperSerialNumber_Type = DisplayString
_RlComponentMapperSerialNumber_Object = MibTableColumn
rlComponentMapperSerialNumber = _RlComponentMapperSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 10),
    _RlComponentMapperSerialNumber_Type()
)
rlComponentMapperSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperSerialNumber.setStatus("current")
_RlComponentMapperPartNumber_Type = DisplayString
_RlComponentMapperPartNumber_Object = MibTableColumn
rlComponentMapperPartNumber = _RlComponentMapperPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 243, 1, 1, 11),
    _RlComponentMapperPartNumber_Type()
)
rlComponentMapperPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlComponentMapperPartNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-ComponentMapper-MIB",
    **{"ComponentType": ComponentType,
       "rlComponentMapper": rlComponentMapper,
       "rlComponentMapperTable": rlComponentMapperTable,
       "rlComponentMapperEntry": rlComponentMapperEntry,
       "rlComponentMapperUnitNum": rlComponentMapperUnitNum,
       "rlComponentMapperType": rlComponentMapperType,
       "rlComponentMapperIndex": rlComponentMapperIndex,
       "rlComponentMapperVendorID": rlComponentMapperVendorID,
       "rlComponentMapperDeviceID": rlComponentMapperDeviceID,
       "rlComponentMapperHardwareVersionID": rlComponentMapperHardwareVersionID,
       "rlComponentMapperSoftwareVersionID": rlComponentMapperSoftwareVersionID,
       "rlComponentMapperAliasID": rlComponentMapperAliasID,
       "rlComponentMapperProductNumber": rlComponentMapperProductNumber,
       "rlComponentMapperSerialNumber": rlComponentMapperSerialNumber,
       "rlComponentMapperPartNumber": rlComponentMapperPartNumber}
)
