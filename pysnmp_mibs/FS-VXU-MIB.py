# SNMP MIB module (FS-VXU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VXU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:17 2025
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

fsVxuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126)
)
if mibBuilder.loadTexts:
    fsVxuMIB.setRevisions(
        ("2013-08-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsVxuMIBObjects_ObjectIdentity = ObjectIdentity
fsVxuMIBObjects = _FsVxuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1)
)
_FsVxuDeviceInfo_ObjectIdentity = ObjectIdentity
fsVxuDeviceInfo = _FsVxuDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1)
)
_FsVxuDeviceTable_Object = MibTable
fsVxuDeviceTable = _FsVxuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsVxuDeviceTable.setStatus("current")
_FsVxuDeviceEntry_Object = MibTableRow
fsVxuDeviceEntry = _FsVxuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1, 1, 1)
)
fsVxuDeviceEntry.setIndexNames(
    (0, "FS-VXU-MIB", "fsVxuDeviceID"),
)
if mibBuilder.loadTexts:
    fsVxuDeviceEntry.setStatus("current")
_FsVxuDeviceID_Type = Integer32
_FsVxuDeviceID_Object = MibTableColumn
fsVxuDeviceID = _FsVxuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1, 1, 1, 1),
    _FsVxuDeviceID_Type()
)
fsVxuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuDeviceID.setStatus("current")
_FsVxuDeviceMac_Type = MacAddress
_FsVxuDeviceMac_Object = MibTableColumn
fsVxuDeviceMac = _FsVxuDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1, 1, 1, 2),
    _FsVxuDeviceMac_Type()
)
fsVxuDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuDeviceMac.setStatus("current")
_FsVxuDeviceDescr_Type = DisplayString
_FsVxuDeviceDescr_Object = MibTableColumn
fsVxuDeviceDescr = _FsVxuDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1, 1, 1, 3),
    _FsVxuDeviceDescr_Type()
)
fsVxuDeviceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxuDeviceDescr.setStatus("current")


class _FsVxuDeviceRole_Type(Integer32):
    """Custom type fsVxuDeviceRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slaver", 2))
    )


_FsVxuDeviceRole_Type.__name__ = "Integer32"
_FsVxuDeviceRole_Object = MibTableColumn
fsVxuDeviceRole = _FsVxuDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 1, 1, 1, 4),
    _FsVxuDeviceRole_Type()
)
fsVxuDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuDeviceRole.setStatus("current")
_FsVxuVxl_ObjectIdentity = ObjectIdentity
fsVxuVxl = _FsVxuVxl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2)
)
_FsVxuVxlTable_Object = MibTable
fsVxuVxlTable = _FsVxuVxlTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsVxuVxlTable.setStatus("current")
_FsVxuVxlEntry_Object = MibTableRow
fsVxuVxlEntry = _FsVxuVxlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 1, 1)
)
fsVxuVxlEntry.setIndexNames(
    (0, "FS-VXU-MIB", "fsVxuChildDeviceID"),
)
if mibBuilder.loadTexts:
    fsVxuVxlEntry.setStatus("current")
_FsVxuChildDeviceID_Type = Integer32
_FsVxuChildDeviceID_Object = MibTableColumn
fsVxuChildDeviceID = _FsVxuChildDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 1, 1, 1),
    _FsVxuChildDeviceID_Type()
)
fsVxuChildDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuChildDeviceID.setStatus("current")
_FsVxuFatherDeviceID_Type = Integer32
_FsVxuFatherDeviceID_Object = MibTableColumn
fsVxuFatherDeviceID = _FsVxuFatherDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 1, 1, 2),
    _FsVxuFatherDeviceID_Type()
)
fsVxuFatherDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuFatherDeviceID.setStatus("current")
_FsVxuFatherVxlIndex_Type = Integer32
_FsVxuFatherVxlIndex_Object = MibTableColumn
fsVxuFatherVxlIndex = _FsVxuFatherVxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 1, 1, 3),
    _FsVxuFatherVxlIndex_Type()
)
fsVxuFatherVxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuFatherVxlIndex.setStatus("current")


class _FsVxuVxlMode_Type(Integer32):
    """Custom type fsVxuVxlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_FsVxuVxlMode_Type.__name__ = "Integer32"
_FsVxuVxlMode_Object = MibTableColumn
fsVxuVxlMode = _FsVxuVxlMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 1, 1, 4),
    _FsVxuVxlMode_Type()
)
fsVxuVxlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlMode.setStatus("current")
_FsVxuVxlPortTable_Object = MibTable
fsVxuVxlPortTable = _FsVxuVxlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsVxuVxlPortTable.setStatus("current")
_FsVxuVxlPortEntry_Object = MibTableRow
fsVxuVxlPortEntry = _FsVxuVxlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1)
)
fsVxuVxlPortEntry.setIndexNames(
    (0, "FS-VXU-MIB", "fsVxuVxlDeviceID"),
    (0, "FS-VXU-MIB", "fsVxuVxlIndex"),
    (0, "FS-VXU-MIB", "fsVxuVxlPortIndex"),
)
if mibBuilder.loadTexts:
    fsVxuVxlPortEntry.setStatus("current")
_FsVxuVxlDeviceID_Type = Integer32
_FsVxuVxlDeviceID_Object = MibTableColumn
fsVxuVxlDeviceID = _FsVxuVxlDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 1),
    _FsVxuVxlDeviceID_Type()
)
fsVxuVxlDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlDeviceID.setStatus("current")
_FsVxuVxlIndex_Type = Integer32
_FsVxuVxlIndex_Object = MibTableColumn
fsVxuVxlIndex = _FsVxuVxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 2),
    _FsVxuVxlIndex_Type()
)
fsVxuVxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlIndex.setStatus("current")
_FsVxuVxlPortIndex_Type = Integer32
_FsVxuVxlPortIndex_Object = MibTableColumn
fsVxuVxlPortIndex = _FsVxuVxlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 3),
    _FsVxuVxlPortIndex_Type()
)
fsVxuVxlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortIndex.setStatus("current")


class _FsVxuVxlPortMode_Type(Integer32):
    """Custom type fsVxuVxlPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_FsVxuVxlPortMode_Type.__name__ = "Integer32"
_FsVxuVxlPortMode_Object = MibTableColumn
fsVxuVxlPortMode = _FsVxuVxlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 4),
    _FsVxuVxlPortMode_Type()
)
fsVxuVxlPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortMode.setStatus("current")
_FsVxuVxlPortDeviceID_Type = Integer32
_FsVxuVxlPortDeviceID_Object = MibTableColumn
fsVxuVxlPortDeviceID = _FsVxuVxlPortDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 5),
    _FsVxuVxlPortDeviceID_Type()
)
fsVxuVxlPortDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortDeviceID.setStatus("current")
_FsVxuVxlPortSlotID_Type = Integer32
_FsVxuVxlPortSlotID_Object = MibTableColumn
fsVxuVxlPortSlotID = _FsVxuVxlPortSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 6),
    _FsVxuVxlPortSlotID_Type()
)
fsVxuVxlPortSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortSlotID.setStatus("current")
_FsVxuVxlPortID_Type = Integer32
_FsVxuVxlPortID_Object = MibTableColumn
fsVxuVxlPortID = _FsVxuVxlPortID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 7),
    _FsVxuVxlPortID_Type()
)
fsVxuVxlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortID.setStatus("current")
_FsVxuVxlPortPeerDeviceID_Type = Integer32
_FsVxuVxlPortPeerDeviceID_Object = MibTableColumn
fsVxuVxlPortPeerDeviceID = _FsVxuVxlPortPeerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 8),
    _FsVxuVxlPortPeerDeviceID_Type()
)
fsVxuVxlPortPeerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortPeerDeviceID.setStatus("current")
_FsVxuVxlPortPeerSlotID_Type = Integer32
_FsVxuVxlPortPeerSlotID_Object = MibTableColumn
fsVxuVxlPortPeerSlotID = _FsVxuVxlPortPeerSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 9),
    _FsVxuVxlPortPeerSlotID_Type()
)
fsVxuVxlPortPeerSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortPeerSlotID.setStatus("current")
_FsVxuVxlPortPeerID_Type = Integer32
_FsVxuVxlPortPeerID_Object = MibTableColumn
fsVxuVxlPortPeerID = _FsVxuVxlPortPeerID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 2, 2, 1, 10),
    _FsVxuVxlPortPeerID_Type()
)
fsVxuVxlPortPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVxlPortPeerID.setStatus("current")
_FsVxuLocation_ObjectIdentity = ObjectIdentity
fsVxuLocation = _FsVxuLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 3)
)
_FsVxuLocationTable_Object = MibTable
fsVxuLocationTable = _FsVxuLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsVxuLocationTable.setStatus("current")
_FsVxuLocationEntry_Object = MibTableRow
fsVxuLocationEntry = _FsVxuLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 3, 1, 1)
)
fsVxuLocationEntry.setIndexNames(
    (0, "FS-VXU-MIB", "fsVxuLocationDeviceID"),
    (0, "FS-VXU-MIB", "fsVxuLocationSlotID"),
)
if mibBuilder.loadTexts:
    fsVxuLocationEntry.setStatus("current")
_FsVxuLocationDeviceID_Type = Integer32
_FsVxuLocationDeviceID_Object = MibTableColumn
fsVxuLocationDeviceID = _FsVxuLocationDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 3, 1, 1, 1),
    _FsVxuLocationDeviceID_Type()
)
fsVxuLocationDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuLocationDeviceID.setStatus("current")
_FsVxuLocationSlotID_Type = Integer32
_FsVxuLocationSlotID_Object = MibTableColumn
fsVxuLocationSlotID = _FsVxuLocationSlotID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 3, 1, 1, 2),
    _FsVxuLocationSlotID_Type()
)
fsVxuLocationSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuLocationSlotID.setStatus("current")


class _FsVxuLocationSet_Type(Integer32):
    """Custom type fsVxuLocationSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("light", 1)
    )


_FsVxuLocationSet_Type.__name__ = "Integer32"
_FsVxuLocationSet_Object = MibTableColumn
fsVxuLocationSet = _FsVxuLocationSet_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 3, 1, 1, 3),
    _FsVxuLocationSet_Type()
)
fsVxuLocationSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxuLocationSet.setStatus("current")
_FsVxuVersion_Type = DisplayString
_FsVxuVersion_Object = MibScalar
fsVxuVersion = _FsVxuVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 1, 4),
    _FsVxuVersion_Type()
)
fsVxuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxuVersion.setStatus("current")
_FsVxuMIBTraps_ObjectIdentity = ObjectIdentity
fsVxuMIBTraps = _FsVxuMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2)
)
_FsVxuTrapsNtfObjects_ObjectIdentity = ObjectIdentity
fsVxuTrapsNtfObjects = _FsVxuTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2, 1)
)


class _FsVxuDeviceState_Type(Integer32):
    """Custom type fsVxuDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_FsVxuDeviceState_Type.__name__ = "Integer32"
_FsVxuDeviceState_Object = MibScalar
fsVxuDeviceState = _FsVxuDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2, 1, 1),
    _FsVxuDeviceState_Type()
)
fsVxuDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVxuDeviceState.setStatus("current")


class _FsVxuVxlState_Type(Integer32):
    """Custom type fsVxuVxlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vxl", 1),
          ("normal", 2))
    )


_FsVxuVxlState_Type.__name__ = "Integer32"
_FsVxuVxlState_Object = MibScalar
fsVxuVxlState = _FsVxuVxlState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2, 1, 2),
    _FsVxuVxlState_Type()
)
fsVxuVxlState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsVxuVxlState.setStatus("current")
_FsVxuTrapsNotifications_ObjectIdentity = ObjectIdentity
fsVxuTrapsNotifications = _FsVxuTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2, 2)
)

# Managed Objects groups


# Notification objects

fsVxuNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2, 2, 1)
)
fsVxuNotifyDeviceChange.setObjects(
      *(("FS-VXU-MIB", "fsVxuLocationDeviceID"),
        ("FS-VXU-MIB", "fsVxuLocationSlotID"),
        ("FS-VXU-MIB", "fsVxuDeviceState"))
)
if mibBuilder.loadTexts:
    fsVxuNotifyDeviceChange.setStatus(
        "current"
    )

fsVxuNotifyVxlChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 126, 2, 2, 2)
)
fsVxuNotifyVxlChange.setObjects(
      *(("FS-VXU-MIB", "fsVxuVxlPortDeviceID"),
        ("FS-VXU-MIB", "fsVxuVxlPortSlotID"),
        ("FS-VXU-MIB", "fsVxuVxlPortID"),
        ("FS-VXU-MIB", "fsVxuVxlState"))
)
if mibBuilder.loadTexts:
    fsVxuNotifyVxlChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VXU-MIB",
    **{"fsVxuMIB": fsVxuMIB,
       "fsVxuMIBObjects": fsVxuMIBObjects,
       "fsVxuDeviceInfo": fsVxuDeviceInfo,
       "fsVxuDeviceTable": fsVxuDeviceTable,
       "fsVxuDeviceEntry": fsVxuDeviceEntry,
       "fsVxuDeviceID": fsVxuDeviceID,
       "fsVxuDeviceMac": fsVxuDeviceMac,
       "fsVxuDeviceDescr": fsVxuDeviceDescr,
       "fsVxuDeviceRole": fsVxuDeviceRole,
       "fsVxuVxl": fsVxuVxl,
       "fsVxuVxlTable": fsVxuVxlTable,
       "fsVxuVxlEntry": fsVxuVxlEntry,
       "fsVxuChildDeviceID": fsVxuChildDeviceID,
       "fsVxuFatherDeviceID": fsVxuFatherDeviceID,
       "fsVxuFatherVxlIndex": fsVxuFatherVxlIndex,
       "fsVxuVxlMode": fsVxuVxlMode,
       "fsVxuVxlPortTable": fsVxuVxlPortTable,
       "fsVxuVxlPortEntry": fsVxuVxlPortEntry,
       "fsVxuVxlDeviceID": fsVxuVxlDeviceID,
       "fsVxuVxlIndex": fsVxuVxlIndex,
       "fsVxuVxlPortIndex": fsVxuVxlPortIndex,
       "fsVxuVxlPortMode": fsVxuVxlPortMode,
       "fsVxuVxlPortDeviceID": fsVxuVxlPortDeviceID,
       "fsVxuVxlPortSlotID": fsVxuVxlPortSlotID,
       "fsVxuVxlPortID": fsVxuVxlPortID,
       "fsVxuVxlPortPeerDeviceID": fsVxuVxlPortPeerDeviceID,
       "fsVxuVxlPortPeerSlotID": fsVxuVxlPortPeerSlotID,
       "fsVxuVxlPortPeerID": fsVxuVxlPortPeerID,
       "fsVxuLocation": fsVxuLocation,
       "fsVxuLocationTable": fsVxuLocationTable,
       "fsVxuLocationEntry": fsVxuLocationEntry,
       "fsVxuLocationDeviceID": fsVxuLocationDeviceID,
       "fsVxuLocationSlotID": fsVxuLocationSlotID,
       "fsVxuLocationSet": fsVxuLocationSet,
       "fsVxuVersion": fsVxuVersion,
       "fsVxuMIBTraps": fsVxuMIBTraps,
       "fsVxuTrapsNtfObjects": fsVxuTrapsNtfObjects,
       "fsVxuDeviceState": fsVxuDeviceState,
       "fsVxuVxlState": fsVxuVxlState,
       "fsVxuTrapsNotifications": fsVxuTrapsNotifications,
       "fsVxuNotifyDeviceChange": fsVxuNotifyDeviceChange,
       "fsVxuNotifyVxlChange": fsVxuNotifyVxlChange}
)
