# SNMP MIB module (FS-MIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MIB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:18 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsVSDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129)
)
if mibBuilder.loadTexts:
    fsVSDMIB.setRevisions(
        ("2014-04-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVSDMIBObjects_ObjectIdentity = ObjectIdentity
fsVSDMIBObjects = _FsVSDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1)
)
_FsVSDSupport_Type = Integer32
_FsVSDSupport_Object = MibScalar
fsVSDSupport = _FsVSDSupport_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 1),
    _FsVSDSupport_Type()
)
fsVSDSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDSupport.setStatus("current")
_FsVSDCurrentID_Type = Integer32
_FsVSDCurrentID_Object = MibScalar
fsVSDCurrentID = _FsVSDCurrentID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 2),
    _FsVSDCurrentID_Type()
)
fsVSDCurrentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDCurrentID.setStatus("current")
_FsVSDMaxNumber_Type = Integer32
_FsVSDMaxNumber_Object = MibScalar
fsVSDMaxNumber = _FsVSDMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 3),
    _FsVSDMaxNumber_Type()
)
fsVSDMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDMaxNumber.setStatus("current")
_FsVSDCurrentNumber_Type = Integer32
_FsVSDCurrentNumber_Object = MibScalar
fsVSDCurrentNumber = _FsVSDCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 4),
    _FsVSDCurrentNumber_Type()
)
fsVSDCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDCurrentNumber.setStatus("current")
_FsVSDMasterMac_Type = MacAddress
_FsVSDMasterMac_Object = MibScalar
fsVSDMasterMac = _FsVSDMasterMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 5),
    _FsVSDMasterMac_Type()
)
fsVSDMasterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDMasterMac.setStatus("current")
_FsVSDCurrentMac_Type = MacAddress
_FsVSDCurrentMac_Object = MibScalar
fsVSDCurrentMac = _FsVSDCurrentMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 6),
    _FsVSDCurrentMac_Type()
)
fsVSDCurrentMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDCurrentMac.setStatus("current")


class _FsVSDVituralSerial_Type(DisplayString):
    """Custom type fsVSDVituralSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVSDVituralSerial_Type.__name__ = "DisplayString"
_FsVSDVituralSerial_Object = MibScalar
fsVSDVituralSerial = _FsVSDVituralSerial_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 7),
    _FsVSDVituralSerial_Type()
)
fsVSDVituralSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDVituralSerial.setStatus("current")


class _FsVSDMasterSerial_Type(DisplayString):
    """Custom type fsVSDMasterSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVSDMasterSerial_Type.__name__ = "DisplayString"
_FsVSDMasterSerial_Object = MibScalar
fsVSDMasterSerial = _FsVSDMasterSerial_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 8),
    _FsVSDMasterSerial_Type()
)
fsVSDMasterSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDMasterSerial.setStatus("current")
_FsVSDInfoTable_Object = MibTable
fsVSDInfoTable = _FsVSDInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9)
)
if mibBuilder.loadTexts:
    fsVSDInfoTable.setStatus("current")
_FsVSDInfoEntry_Object = MibTableRow
fsVSDInfoEntry = _FsVSDInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1)
)
fsVSDInfoEntry.setIndexNames(
    (0, "FS-MIB-MIB", "fsVSDInfoIndex"),
)
if mibBuilder.loadTexts:
    fsVSDInfoEntry.setStatus("current")
_FsVSDInfoIndex_Type = Integer32
_FsVSDInfoIndex_Object = MibTableColumn
fsVSDInfoIndex = _FsVSDInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1, 1),
    _FsVSDInfoIndex_Type()
)
fsVSDInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDInfoIndex.setStatus("current")
_FsVSDValid_Type = Integer32
_FsVSDValid_Object = MibTableColumn
fsVSDValid = _FsVSDValid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1, 2),
    _FsVSDValid_Type()
)
fsVSDValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDValid.setStatus("current")


class _FsVSDName_Type(DisplayString):
    """Custom type fsVSDName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsVSDName_Type.__name__ = "DisplayString"
_FsVSDName_Object = MibTableColumn
fsVSDName = _FsVSDName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1, 3),
    _FsVSDName_Type()
)
fsVSDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDName.setStatus("current")
_FsVSDMacAddress_Type = MacAddress
_FsVSDMacAddress_Object = MibTableColumn
fsVSDMacAddress = _FsVSDMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1, 4),
    _FsVSDMacAddress_Type()
)
fsVSDMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDMacAddress.setStatus("current")


class _FsVSDSerialNumber_Type(DisplayString):
    """Custom type fsVSDSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsVSDSerialNumber_Type.__name__ = "DisplayString"
_FsVSDSerialNumber_Object = MibTableColumn
fsVSDSerialNumber = _FsVSDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1, 5),
    _FsVSDSerialNumber_Type()
)
fsVSDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDSerialNumber.setStatus("current")


class _FsVSDUniqueNumber_Type(DisplayString):
    """Custom type fsVSDUniqueNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsVSDUniqueNumber_Type.__name__ = "DisplayString"
_FsVSDUniqueNumber_Object = MibTableColumn
fsVSDUniqueNumber = _FsVSDUniqueNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 9, 1, 6),
    _FsVSDUniqueNumber_Type()
)
fsVSDUniqueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDUniqueNumber.setStatus("current")
_FsVSDPortInfoTable_Object = MibTable
fsVSDPortInfoTable = _FsVSDPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10)
)
if mibBuilder.loadTexts:
    fsVSDPortInfoTable.setStatus("current")
_FsVSDPortInfoEntry_Object = MibTableRow
fsVSDPortInfoEntry = _FsVSDPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1)
)
fsVSDPortInfoEntry.setIndexNames(
    (0, "FS-MIB-MIB", "fsVSDPortDevice"),
    (0, "FS-MIB-MIB", "fsVSDPortSlot"),
    (0, "FS-MIB-MIB", "fsVSDPortSubslot"),
    (0, "FS-MIB-MIB", "fsVSDPortPortIdx"),
)
if mibBuilder.loadTexts:
    fsVSDPortInfoEntry.setStatus("current")
_FsVSDPortDevice_Type = Integer32
_FsVSDPortDevice_Object = MibTableColumn
fsVSDPortDevice = _FsVSDPortDevice_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1, 1),
    _FsVSDPortDevice_Type()
)
fsVSDPortDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDPortDevice.setStatus("current")
_FsVSDPortSlot_Type = Integer32
_FsVSDPortSlot_Object = MibTableColumn
fsVSDPortSlot = _FsVSDPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1, 2),
    _FsVSDPortSlot_Type()
)
fsVSDPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDPortSlot.setStatus("current")
_FsVSDPortSubslot_Type = Integer32
_FsVSDPortSubslot_Object = MibTableColumn
fsVSDPortSubslot = _FsVSDPortSubslot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1, 3),
    _FsVSDPortSubslot_Type()
)
fsVSDPortSubslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDPortSubslot.setStatus("current")
_FsVSDPortPortIdx_Type = Integer32
_FsVSDPortPortIdx_Object = MibTableColumn
fsVSDPortPortIdx = _FsVSDPortPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1, 4),
    _FsVSDPortPortIdx_Type()
)
fsVSDPortPortIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDPortPortIdx.setStatus("current")
_FsVSDPortIfIndex_Type = Integer32
_FsVSDPortIfIndex_Object = MibTableColumn
fsVSDPortIfIndex = _FsVSDPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1, 5),
    _FsVSDPortIfIndex_Type()
)
fsVSDPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDPortIfIndex.setStatus("current")
_FsVSDPortVSDIndex_Type = Integer32
_FsVSDPortVSDIndex_Object = MibTableColumn
fsVSDPortVSDIndex = _FsVSDPortVSDIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 1, 10, 1, 6),
    _FsVSDPortVSDIndex_Type()
)
fsVSDPortVSDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVSDPortVSDIndex.setStatus("current")
_FsVSDMIBTraps_ObjectIdentity = ObjectIdentity
fsVSDMIBTraps = _FsVSDMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 2)
)
_FsVSDChgDesc_Type = DisplayString
_FsVSDChgDesc_Object = MibScalar
fsVSDChgDesc = _FsVSDChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 2, 1),
    _FsVSDChgDesc_Type()
)
fsVSDChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVSDChgDesc.setStatus("current")
_FsVSDPortChgDesc_Type = DisplayString
_FsVSDPortChgDesc_Object = MibScalar
fsVSDPortChgDesc = _FsVSDPortChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 2, 3),
    _FsVSDPortChgDesc_Type()
)
fsVSDPortChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVSDPortChgDesc.setStatus("current")
_FsVSDMIBConformance_ObjectIdentity = ObjectIdentity
fsVSDMIBConformance = _FsVSDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3)
)
_FsVSDMIBCompliances_ObjectIdentity = ObjectIdentity
fsVSDMIBCompliances = _FsVSDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 1)
)
_FsVSDMIBGroups_ObjectIdentity = ObjectIdentity
fsVSDMIBGroups = _FsVSDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 2)
)

# Managed Objects groups

fsVSDInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 2, 1)
)
fsVSDInfoMIBGroup.setObjects(
      *(("FS-MIB-MIB", "fsVSDSupport"),
        ("FS-MIB-MIB", "fsVSDCurrentID"),
        ("FS-MIB-MIB", "fsVSDMaxNumber"),
        ("FS-MIB-MIB", "fsVSDCurrentNumber"),
        ("FS-MIB-MIB", "fsVSDMasterMac"),
        ("FS-MIB-MIB", "fsVSDCurrentMac"),
        ("FS-MIB-MIB", "fsVSDVituralSerial"),
        ("FS-MIB-MIB", "fsVSDMasterSerial"))
)
if mibBuilder.loadTexts:
    fsVSDInfoMIBGroup.setStatus("current")

fsVSDDetailInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 2, 2)
)
fsVSDDetailInfoMIBGroup.setObjects(
      *(("FS-MIB-MIB", "fsVSDInfoIndex"),
        ("FS-MIB-MIB", "fsVSDValid"),
        ("FS-MIB-MIB", "fsVSDName"),
        ("FS-MIB-MIB", "fsVSDMacAddress"),
        ("FS-MIB-MIB", "fsVSDSerialNumber"),
        ("FS-MIB-MIB", "fsVSDUniqueNumber"))
)
if mibBuilder.loadTexts:
    fsVSDDetailInfoMIBGroup.setStatus("current")

fsVSDPortInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 2, 3)
)
fsVSDPortInfoMIBGroup.setObjects(
      *(("FS-MIB-MIB", "fsVSDPortDevice"),
        ("FS-MIB-MIB", "fsVSDPortSlot"),
        ("FS-MIB-MIB", "fsVSDPortSubslot"),
        ("FS-MIB-MIB", "fsVSDPortPortIdx"),
        ("FS-MIB-MIB", "fsVSDPortIfIndex"),
        ("FS-MIB-MIB", "fsVSDPortVSDIndex"))
)
if mibBuilder.loadTexts:
    fsVSDPortInfoMIBGroup.setStatus("current")

fsVSDChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 2, 4)
)
fsVSDChgDescGroup.setObjects(
      *(("FS-MIB-MIB", "fsVSDChgDesc"),
        ("FS-MIB-MIB", "fsVSDPortChgDesc"))
)
if mibBuilder.loadTexts:
    fsVSDChgDescGroup.setStatus("current")


# Notification objects

fsVSDStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 2, 2)
)
fsVSDStatusChange.setObjects(
    ("FS-MIB-MIB", "fsVSDChgDesc")
)
if mibBuilder.loadTexts:
    fsVSDStatusChange.setStatus(
        "current"
    )

fsVSDPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 2, 4)
)
fsVSDPortStatusChange.setObjects(
    ("FS-MIB-MIB", "fsVSDPortChgDesc")
)
if mibBuilder.loadTexts:
    fsVSDPortStatusChange.setStatus(
        "current"
    )


# Notifications groups

fsVSDMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 2, 5)
)
fsVSDMIBNotificationGroup.setObjects(
      *(("FS-MIB-MIB", "fsVSDStatusChange"),
        ("FS-MIB-MIB", "fsVSDPortStatusChange"))
)
if mibBuilder.loadTexts:
    fsVSDMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsVSDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 129, 3, 1, 1)
)
fsVSDMIBCompliance.setObjects(
      *(("FS-MIB-MIB", "fsVSDInfoMIBGroup"),
        ("FS-MIB-MIB", "fsVSDDetailInfoMIBGroup"),
        ("FS-MIB-MIB", "fsVSDPortInfoMIBGroup"),
        ("FS-MIB-MIB", "fsVSDChgDescGroup"),
        ("FS-MIB-MIB", "fsVSDMIBNotificationGroup"))
)
if mibBuilder.loadTexts:
    fsVSDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MIB-MIB",
    **{"fsVSDMIB": fsVSDMIB,
       "fsVSDMIBObjects": fsVSDMIBObjects,
       "fsVSDSupport": fsVSDSupport,
       "fsVSDCurrentID": fsVSDCurrentID,
       "fsVSDMaxNumber": fsVSDMaxNumber,
       "fsVSDCurrentNumber": fsVSDCurrentNumber,
       "fsVSDMasterMac": fsVSDMasterMac,
       "fsVSDCurrentMac": fsVSDCurrentMac,
       "fsVSDVituralSerial": fsVSDVituralSerial,
       "fsVSDMasterSerial": fsVSDMasterSerial,
       "fsVSDInfoTable": fsVSDInfoTable,
       "fsVSDInfoEntry": fsVSDInfoEntry,
       "fsVSDInfoIndex": fsVSDInfoIndex,
       "fsVSDValid": fsVSDValid,
       "fsVSDName": fsVSDName,
       "fsVSDMacAddress": fsVSDMacAddress,
       "fsVSDSerialNumber": fsVSDSerialNumber,
       "fsVSDUniqueNumber": fsVSDUniqueNumber,
       "fsVSDPortInfoTable": fsVSDPortInfoTable,
       "fsVSDPortInfoEntry": fsVSDPortInfoEntry,
       "fsVSDPortDevice": fsVSDPortDevice,
       "fsVSDPortSlot": fsVSDPortSlot,
       "fsVSDPortSubslot": fsVSDPortSubslot,
       "fsVSDPortPortIdx": fsVSDPortPortIdx,
       "fsVSDPortIfIndex": fsVSDPortIfIndex,
       "fsVSDPortVSDIndex": fsVSDPortVSDIndex,
       "fsVSDMIBTraps": fsVSDMIBTraps,
       "fsVSDChgDesc": fsVSDChgDesc,
       "fsVSDStatusChange": fsVSDStatusChange,
       "fsVSDPortChgDesc": fsVSDPortChgDesc,
       "fsVSDPortStatusChange": fsVSDPortStatusChange,
       "fsVSDMIBConformance": fsVSDMIBConformance,
       "fsVSDMIBCompliances": fsVSDMIBCompliances,
       "fsVSDMIBCompliance": fsVSDMIBCompliance,
       "fsVSDMIBGroups": fsVSDMIBGroups,
       "fsVSDInfoMIBGroup": fsVSDInfoMIBGroup,
       "fsVSDDetailInfoMIBGroup": fsVSDDetailInfoMIBGroup,
       "fsVSDPortInfoMIBGroup": fsVSDPortInfoMIBGroup,
       "fsVSDChgDescGroup": fsVSDChgDescGroup,
       "fsVSDMIBNotificationGroup": fsVSDMIBNotificationGroup}
)
