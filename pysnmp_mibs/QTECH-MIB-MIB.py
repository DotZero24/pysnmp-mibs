# SNMP MIB module (QTECH-MIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MIB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:59 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechVSDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129)
)
if mibBuilder.loadTexts:
    qtechVSDMIB.setRevisions(
        ("2014-04-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechVSDMIBObjects_ObjectIdentity = ObjectIdentity
qtechVSDMIBObjects = _QtechVSDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1)
)
_QtechVSDSupport_Type = Integer32
_QtechVSDSupport_Object = MibScalar
qtechVSDSupport = _QtechVSDSupport_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 1),
    _QtechVSDSupport_Type()
)
qtechVSDSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDSupport.setStatus("current")
_QtechVSDCurrentID_Type = Integer32
_QtechVSDCurrentID_Object = MibScalar
qtechVSDCurrentID = _QtechVSDCurrentID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 2),
    _QtechVSDCurrentID_Type()
)
qtechVSDCurrentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDCurrentID.setStatus("current")
_QtechVSDMaxNumber_Type = Integer32
_QtechVSDMaxNumber_Object = MibScalar
qtechVSDMaxNumber = _QtechVSDMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 3),
    _QtechVSDMaxNumber_Type()
)
qtechVSDMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDMaxNumber.setStatus("current")
_QtechVSDCurrentNumber_Type = Integer32
_QtechVSDCurrentNumber_Object = MibScalar
qtechVSDCurrentNumber = _QtechVSDCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 4),
    _QtechVSDCurrentNumber_Type()
)
qtechVSDCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDCurrentNumber.setStatus("current")
_QtechVSDMasterMac_Type = MacAddress
_QtechVSDMasterMac_Object = MibScalar
qtechVSDMasterMac = _QtechVSDMasterMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 5),
    _QtechVSDMasterMac_Type()
)
qtechVSDMasterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDMasterMac.setStatus("current")
_QtechVSDCurrentMac_Type = MacAddress
_QtechVSDCurrentMac_Object = MibScalar
qtechVSDCurrentMac = _QtechVSDCurrentMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 6),
    _QtechVSDCurrentMac_Type()
)
qtechVSDCurrentMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDCurrentMac.setStatus("current")


class _QtechVSDVituralSerial_Type(DisplayString):
    """Custom type qtechVSDVituralSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVSDVituralSerial_Type.__name__ = "DisplayString"
_QtechVSDVituralSerial_Object = MibScalar
qtechVSDVituralSerial = _QtechVSDVituralSerial_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 7),
    _QtechVSDVituralSerial_Type()
)
qtechVSDVituralSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDVituralSerial.setStatus("current")


class _QtechVSDMasterSerial_Type(DisplayString):
    """Custom type qtechVSDMasterSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVSDMasterSerial_Type.__name__ = "DisplayString"
_QtechVSDMasterSerial_Object = MibScalar
qtechVSDMasterSerial = _QtechVSDMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 8),
    _QtechVSDMasterSerial_Type()
)
qtechVSDMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDMasterSerial.setStatus("current")
_QtechVSDInfoTable_Object = MibTable
qtechVSDInfoTable = _QtechVSDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9)
)
if mibBuilder.loadTexts:
    qtechVSDInfoTable.setStatus("current")
_QtechVSDInfoEntry_Object = MibTableRow
qtechVSDInfoEntry = _QtechVSDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1)
)
qtechVSDInfoEntry.setIndexNames(
    (0, "QTECH-MIB-MIB", "qtechVSDInfoIndex"),
)
if mibBuilder.loadTexts:
    qtechVSDInfoEntry.setStatus("current")
_QtechVSDInfoIndex_Type = Integer32
_QtechVSDInfoIndex_Object = MibTableColumn
qtechVSDInfoIndex = _QtechVSDInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1, 1),
    _QtechVSDInfoIndex_Type()
)
qtechVSDInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDInfoIndex.setStatus("current")
_QtechVSDValid_Type = Integer32
_QtechVSDValid_Object = MibTableColumn
qtechVSDValid = _QtechVSDValid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1, 2),
    _QtechVSDValid_Type()
)
qtechVSDValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDValid.setStatus("current")


class _QtechVSDName_Type(DisplayString):
    """Custom type qtechVSDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechVSDName_Type.__name__ = "DisplayString"
_QtechVSDName_Object = MibTableColumn
qtechVSDName = _QtechVSDName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1, 3),
    _QtechVSDName_Type()
)
qtechVSDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDName.setStatus("current")
_QtechVSDMacAddress_Type = MacAddress
_QtechVSDMacAddress_Object = MibTableColumn
qtechVSDMacAddress = _QtechVSDMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1, 4),
    _QtechVSDMacAddress_Type()
)
qtechVSDMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDMacAddress.setStatus("current")


class _QtechVSDSerialNumber_Type(DisplayString):
    """Custom type qtechVSDSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechVSDSerialNumber_Type.__name__ = "DisplayString"
_QtechVSDSerialNumber_Object = MibTableColumn
qtechVSDSerialNumber = _QtechVSDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1, 5),
    _QtechVSDSerialNumber_Type()
)
qtechVSDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDSerialNumber.setStatus("current")


class _QtechVSDUniqueNumber_Type(DisplayString):
    """Custom type qtechVSDUniqueNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechVSDUniqueNumber_Type.__name__ = "DisplayString"
_QtechVSDUniqueNumber_Object = MibTableColumn
qtechVSDUniqueNumber = _QtechVSDUniqueNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 9, 1, 6),
    _QtechVSDUniqueNumber_Type()
)
qtechVSDUniqueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDUniqueNumber.setStatus("current")
_QtechVSDPortInfoTable_Object = MibTable
qtechVSDPortInfoTable = _QtechVSDPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10)
)
if mibBuilder.loadTexts:
    qtechVSDPortInfoTable.setStatus("current")
_QtechVSDPortInfoEntry_Object = MibTableRow
qtechVSDPortInfoEntry = _QtechVSDPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1)
)
qtechVSDPortInfoEntry.setIndexNames(
    (0, "QTECH-MIB-MIB", "qtechVSDPortDevice"),
    (0, "QTECH-MIB-MIB", "qtechVSDPortSlot"),
    (0, "QTECH-MIB-MIB", "qtechVSDPortSubslot"),
    (0, "QTECH-MIB-MIB", "qtechVSDPortPortIdx"),
)
if mibBuilder.loadTexts:
    qtechVSDPortInfoEntry.setStatus("current")
_QtechVSDPortDevice_Type = Integer32
_QtechVSDPortDevice_Object = MibTableColumn
qtechVSDPortDevice = _QtechVSDPortDevice_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1, 1),
    _QtechVSDPortDevice_Type()
)
qtechVSDPortDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDPortDevice.setStatus("current")
_QtechVSDPortSlot_Type = Integer32
_QtechVSDPortSlot_Object = MibTableColumn
qtechVSDPortSlot = _QtechVSDPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1, 2),
    _QtechVSDPortSlot_Type()
)
qtechVSDPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDPortSlot.setStatus("current")
_QtechVSDPortSubslot_Type = Integer32
_QtechVSDPortSubslot_Object = MibTableColumn
qtechVSDPortSubslot = _QtechVSDPortSubslot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1, 3),
    _QtechVSDPortSubslot_Type()
)
qtechVSDPortSubslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDPortSubslot.setStatus("current")
_QtechVSDPortPortIdx_Type = Integer32
_QtechVSDPortPortIdx_Object = MibTableColumn
qtechVSDPortPortIdx = _QtechVSDPortPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1, 4),
    _QtechVSDPortPortIdx_Type()
)
qtechVSDPortPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDPortPortIdx.setStatus("current")
_QtechVSDPortIfIndex_Type = Integer32
_QtechVSDPortIfIndex_Object = MibTableColumn
qtechVSDPortIfIndex = _QtechVSDPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1, 5),
    _QtechVSDPortIfIndex_Type()
)
qtechVSDPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDPortIfIndex.setStatus("current")
_QtechVSDPortVSDIndex_Type = Integer32
_QtechVSDPortVSDIndex_Object = MibTableColumn
qtechVSDPortVSDIndex = _QtechVSDPortVSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 1, 10, 1, 6),
    _QtechVSDPortVSDIndex_Type()
)
qtechVSDPortVSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVSDPortVSDIndex.setStatus("current")
_QtechVSDMIBTraps_ObjectIdentity = ObjectIdentity
qtechVSDMIBTraps = _QtechVSDMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 2)
)
_QtechVSDChgDesc_Type = DisplayString
_QtechVSDChgDesc_Object = MibScalar
qtechVSDChgDesc = _QtechVSDChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 2, 1),
    _QtechVSDChgDesc_Type()
)
qtechVSDChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVSDChgDesc.setStatus("current")
_QtechVSDPortChgDesc_Type = DisplayString
_QtechVSDPortChgDesc_Object = MibScalar
qtechVSDPortChgDesc = _QtechVSDPortChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 2, 3),
    _QtechVSDPortChgDesc_Type()
)
qtechVSDPortChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVSDPortChgDesc.setStatus("current")
_QtechVSDMIBConformance_ObjectIdentity = ObjectIdentity
qtechVSDMIBConformance = _QtechVSDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3)
)
_QtechVSDMIBCompliances_ObjectIdentity = ObjectIdentity
qtechVSDMIBCompliances = _QtechVSDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 1)
)
_QtechVSDMIBGroups_ObjectIdentity = ObjectIdentity
qtechVSDMIBGroups = _QtechVSDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 2)
)

# Managed Objects groups

qtechVSDInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 2, 1)
)
qtechVSDInfoMIBGroup.setObjects(
      *(("QTECH-MIB-MIB", "qtechVSDSupport"),
        ("QTECH-MIB-MIB", "qtechVSDCurrentID"),
        ("QTECH-MIB-MIB", "qtechVSDMaxNumber"),
        ("QTECH-MIB-MIB", "qtechVSDCurrentNumber"),
        ("QTECH-MIB-MIB", "qtechVSDMasterMac"),
        ("QTECH-MIB-MIB", "qtechVSDCurrentMac"),
        ("QTECH-MIB-MIB", "qtechVSDVituralSerial"),
        ("QTECH-MIB-MIB", "qtechVSDMasterSerial"))
)
if mibBuilder.loadTexts:
    qtechVSDInfoMIBGroup.setStatus("current")

qtechVSDDetailInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 2, 2)
)
qtechVSDDetailInfoMIBGroup.setObjects(
      *(("QTECH-MIB-MIB", "qtechVSDInfoIndex"),
        ("QTECH-MIB-MIB", "qtechVSDValid"),
        ("QTECH-MIB-MIB", "qtechVSDName"),
        ("QTECH-MIB-MIB", "qtechVSDMacAddress"),
        ("QTECH-MIB-MIB", "qtechVSDSerialNumber"),
        ("QTECH-MIB-MIB", "qtechVSDUniqueNumber"))
)
if mibBuilder.loadTexts:
    qtechVSDDetailInfoMIBGroup.setStatus("current")

qtechVSDPortInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 2, 3)
)
qtechVSDPortInfoMIBGroup.setObjects(
      *(("QTECH-MIB-MIB", "qtechVSDPortDevice"),
        ("QTECH-MIB-MIB", "qtechVSDPortSlot"),
        ("QTECH-MIB-MIB", "qtechVSDPortSubslot"),
        ("QTECH-MIB-MIB", "qtechVSDPortPortIdx"),
        ("QTECH-MIB-MIB", "qtechVSDPortIfIndex"),
        ("QTECH-MIB-MIB", "qtechVSDPortVSDIndex"))
)
if mibBuilder.loadTexts:
    qtechVSDPortInfoMIBGroup.setStatus("current")

qtechVSDChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 2, 4)
)
qtechVSDChgDescGroup.setObjects(
      *(("QTECH-MIB-MIB", "qtechVSDChgDesc"),
        ("QTECH-MIB-MIB", "qtechVSDPortChgDesc"))
)
if mibBuilder.loadTexts:
    qtechVSDChgDescGroup.setStatus("current")


# Notification objects

qtechVSDStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 2, 2)
)
qtechVSDStatusChange.setObjects(
    ("QTECH-MIB-MIB", "qtechVSDChgDesc")
)
if mibBuilder.loadTexts:
    qtechVSDStatusChange.setStatus(
        "current"
    )

qtechVSDPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 2, 4)
)
qtechVSDPortStatusChange.setObjects(
    ("QTECH-MIB-MIB", "qtechVSDPortChgDesc")
)
if mibBuilder.loadTexts:
    qtechVSDPortStatusChange.setStatus(
        "current"
    )


# Notifications groups

qtechVSDMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 2, 5)
)
qtechVSDMIBNotificationGroup.setObjects(
      *(("QTECH-MIB-MIB", "qtechVSDStatusChange"),
        ("QTECH-MIB-MIB", "qtechVSDPortStatusChange"))
)
if mibBuilder.loadTexts:
    qtechVSDMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechVSDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 129, 3, 1, 1)
)
qtechVSDMIBCompliance.setObjects(
      *(("QTECH-MIB-MIB", "qtechVSDInfoMIBGroup"),
        ("QTECH-MIB-MIB", "qtechVSDDetailInfoMIBGroup"),
        ("QTECH-MIB-MIB", "qtechVSDPortInfoMIBGroup"),
        ("QTECH-MIB-MIB", "qtechVSDChgDescGroup"),
        ("QTECH-MIB-MIB", "qtechVSDMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    qtechVSDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MIB-MIB",
    **{"qtechVSDMIB": qtechVSDMIB,
       "qtechVSDMIBObjects": qtechVSDMIBObjects,
       "qtechVSDSupport": qtechVSDSupport,
       "qtechVSDCurrentID": qtechVSDCurrentID,
       "qtechVSDMaxNumber": qtechVSDMaxNumber,
       "qtechVSDCurrentNumber": qtechVSDCurrentNumber,
       "qtechVSDMasterMac": qtechVSDMasterMac,
       "qtechVSDCurrentMac": qtechVSDCurrentMac,
       "qtechVSDVituralSerial": qtechVSDVituralSerial,
       "qtechVSDMasterSerial": qtechVSDMasterSerial,
       "qtechVSDInfoTable": qtechVSDInfoTable,
       "qtechVSDInfoEntry": qtechVSDInfoEntry,
       "qtechVSDInfoIndex": qtechVSDInfoIndex,
       "qtechVSDValid": qtechVSDValid,
       "qtechVSDName": qtechVSDName,
       "qtechVSDMacAddress": qtechVSDMacAddress,
       "qtechVSDSerialNumber": qtechVSDSerialNumber,
       "qtechVSDUniqueNumber": qtechVSDUniqueNumber,
       "qtechVSDPortInfoTable": qtechVSDPortInfoTable,
       "qtechVSDPortInfoEntry": qtechVSDPortInfoEntry,
       "qtechVSDPortDevice": qtechVSDPortDevice,
       "qtechVSDPortSlot": qtechVSDPortSlot,
       "qtechVSDPortSubslot": qtechVSDPortSubslot,
       "qtechVSDPortPortIdx": qtechVSDPortPortIdx,
       "qtechVSDPortIfIndex": qtechVSDPortIfIndex,
       "qtechVSDPortVSDIndex": qtechVSDPortVSDIndex,
       "qtechVSDMIBTraps": qtechVSDMIBTraps,
       "qtechVSDChgDesc": qtechVSDChgDesc,
       "qtechVSDStatusChange": qtechVSDStatusChange,
       "qtechVSDPortChgDesc": qtechVSDPortChgDesc,
       "qtechVSDPortStatusChange": qtechVSDPortStatusChange,
       "qtechVSDMIBConformance": qtechVSDMIBConformance,
       "qtechVSDMIBCompliances": qtechVSDMIBCompliances,
       "qtechVSDMIBCompliance": qtechVSDMIBCompliance,
       "qtechVSDMIBGroups": qtechVSDMIBGroups,
       "qtechVSDInfoMIBGroup": qtechVSDInfoMIBGroup,
       "qtechVSDDetailInfoMIBGroup": qtechVSDDetailInfoMIBGroup,
       "qtechVSDPortInfoMIBGroup": qtechVSDPortInfoMIBGroup,
       "qtechVSDChgDescGroup": qtechVSDChgDescGroup,
       "qtechVSDMIBNotificationGroup": qtechVSDMIBNotificationGroup}
)
