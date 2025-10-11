# SNMP MIB module (QTECH-VXU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VXU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:02 2025
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

qtechVxuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126)
)
if mibBuilder.loadTexts:
    qtechVxuMIB.setRevisions(
        ("2013-08-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechVxuMIBObjects_ObjectIdentity = ObjectIdentity
qtechVxuMIBObjects = _QtechVxuMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1)
)
_QtechVxuDeviceInfo_ObjectIdentity = ObjectIdentity
qtechVxuDeviceInfo = _QtechVxuDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1)
)
_QtechVxuDeviceTable_Object = MibTable
qtechVxuDeviceTable = _QtechVxuDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechVxuDeviceTable.setStatus("current")
_QtechVxuDeviceEntry_Object = MibTableRow
qtechVxuDeviceEntry = _QtechVxuDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1, 1, 1)
)
qtechVxuDeviceEntry.setIndexNames(
    (0, "QTECH-VXU-MIB", "qtechVxuDeviceID"),
)
if mibBuilder.loadTexts:
    qtechVxuDeviceEntry.setStatus("current")
_QtechVxuDeviceID_Type = Integer32
_QtechVxuDeviceID_Object = MibTableColumn
qtechVxuDeviceID = _QtechVxuDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1, 1, 1, 1),
    _QtechVxuDeviceID_Type()
)
qtechVxuDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuDeviceID.setStatus("current")
_QtechVxuDeviceMac_Type = MacAddress
_QtechVxuDeviceMac_Object = MibTableColumn
qtechVxuDeviceMac = _QtechVxuDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1, 1, 1, 2),
    _QtechVxuDeviceMac_Type()
)
qtechVxuDeviceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuDeviceMac.setStatus("current")
_QtechVxuDeviceDescr_Type = DisplayString
_QtechVxuDeviceDescr_Object = MibTableColumn
qtechVxuDeviceDescr = _QtechVxuDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1, 1, 1, 3),
    _QtechVxuDeviceDescr_Type()
)
qtechVxuDeviceDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVxuDeviceDescr.setStatus("current")


class _QtechVxuDeviceRole_Type(Integer32):
    """Custom type qtechVxuDeviceRole based on Integer32"""
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


_QtechVxuDeviceRole_Type.__name__ = "Integer32"
_QtechVxuDeviceRole_Object = MibTableColumn
qtechVxuDeviceRole = _QtechVxuDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 1, 1, 1, 4),
    _QtechVxuDeviceRole_Type()
)
qtechVxuDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuDeviceRole.setStatus("current")
_QtechVxuVxl_ObjectIdentity = ObjectIdentity
qtechVxuVxl = _QtechVxuVxl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2)
)
_QtechVxuVxlTable_Object = MibTable
qtechVxuVxlTable = _QtechVxuVxlTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechVxuVxlTable.setStatus("current")
_QtechVxuVxlEntry_Object = MibTableRow
qtechVxuVxlEntry = _QtechVxuVxlEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 1, 1)
)
qtechVxuVxlEntry.setIndexNames(
    (0, "QTECH-VXU-MIB", "qtechVxuChildDeviceID"),
)
if mibBuilder.loadTexts:
    qtechVxuVxlEntry.setStatus("current")
_QtechVxuChildDeviceID_Type = Integer32
_QtechVxuChildDeviceID_Object = MibTableColumn
qtechVxuChildDeviceID = _QtechVxuChildDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 1, 1, 1),
    _QtechVxuChildDeviceID_Type()
)
qtechVxuChildDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuChildDeviceID.setStatus("current")
_QtechVxuFatherDeviceID_Type = Integer32
_QtechVxuFatherDeviceID_Object = MibTableColumn
qtechVxuFatherDeviceID = _QtechVxuFatherDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 1, 1, 2),
    _QtechVxuFatherDeviceID_Type()
)
qtechVxuFatherDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuFatherDeviceID.setStatus("current")
_QtechVxuFatherVxlIndex_Type = Integer32
_QtechVxuFatherVxlIndex_Object = MibTableColumn
qtechVxuFatherVxlIndex = _QtechVxuFatherVxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 1, 1, 3),
    _QtechVxuFatherVxlIndex_Type()
)
qtechVxuFatherVxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuFatherVxlIndex.setStatus("current")


class _QtechVxuVxlMode_Type(Integer32):
    """Custom type qtechVxuVxlMode based on Integer32"""
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


_QtechVxuVxlMode_Type.__name__ = "Integer32"
_QtechVxuVxlMode_Object = MibTableColumn
qtechVxuVxlMode = _QtechVxuVxlMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 1, 1, 4),
    _QtechVxuVxlMode_Type()
)
qtechVxuVxlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlMode.setStatus("current")
_QtechVxuVxlPortTable_Object = MibTable
qtechVxuVxlPortTable = _QtechVxuVxlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechVxuVxlPortTable.setStatus("current")
_QtechVxuVxlPortEntry_Object = MibTableRow
qtechVxuVxlPortEntry = _QtechVxuVxlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1)
)
qtechVxuVxlPortEntry.setIndexNames(
    (0, "QTECH-VXU-MIB", "qtechVxuVxlDeviceID"),
    (0, "QTECH-VXU-MIB", "qtechVxuVxlIndex"),
    (0, "QTECH-VXU-MIB", "qtechVxuVxlPortIndex"),
)
if mibBuilder.loadTexts:
    qtechVxuVxlPortEntry.setStatus("current")
_QtechVxuVxlDeviceID_Type = Integer32
_QtechVxuVxlDeviceID_Object = MibTableColumn
qtechVxuVxlDeviceID = _QtechVxuVxlDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 1),
    _QtechVxuVxlDeviceID_Type()
)
qtechVxuVxlDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlDeviceID.setStatus("current")
_QtechVxuVxlIndex_Type = Integer32
_QtechVxuVxlIndex_Object = MibTableColumn
qtechVxuVxlIndex = _QtechVxuVxlIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 2),
    _QtechVxuVxlIndex_Type()
)
qtechVxuVxlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlIndex.setStatus("current")
_QtechVxuVxlPortIndex_Type = Integer32
_QtechVxuVxlPortIndex_Object = MibTableColumn
qtechVxuVxlPortIndex = _QtechVxuVxlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 3),
    _QtechVxuVxlPortIndex_Type()
)
qtechVxuVxlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortIndex.setStatus("current")


class _QtechVxuVxlPortMode_Type(Integer32):
    """Custom type qtechVxuVxlPortMode based on Integer32"""
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


_QtechVxuVxlPortMode_Type.__name__ = "Integer32"
_QtechVxuVxlPortMode_Object = MibTableColumn
qtechVxuVxlPortMode = _QtechVxuVxlPortMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 4),
    _QtechVxuVxlPortMode_Type()
)
qtechVxuVxlPortMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortMode.setStatus("current")
_QtechVxuVxlPortDeviceID_Type = Integer32
_QtechVxuVxlPortDeviceID_Object = MibTableColumn
qtechVxuVxlPortDeviceID = _QtechVxuVxlPortDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 5),
    _QtechVxuVxlPortDeviceID_Type()
)
qtechVxuVxlPortDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortDeviceID.setStatus("current")
_QtechVxuVxlPortSlotID_Type = Integer32
_QtechVxuVxlPortSlotID_Object = MibTableColumn
qtechVxuVxlPortSlotID = _QtechVxuVxlPortSlotID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 6),
    _QtechVxuVxlPortSlotID_Type()
)
qtechVxuVxlPortSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortSlotID.setStatus("current")
_QtechVxuVxlPortID_Type = Integer32
_QtechVxuVxlPortID_Object = MibTableColumn
qtechVxuVxlPortID = _QtechVxuVxlPortID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 7),
    _QtechVxuVxlPortID_Type()
)
qtechVxuVxlPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortID.setStatus("current")
_QtechVxuVxlPortPeerDeviceID_Type = Integer32
_QtechVxuVxlPortPeerDeviceID_Object = MibTableColumn
qtechVxuVxlPortPeerDeviceID = _QtechVxuVxlPortPeerDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 8),
    _QtechVxuVxlPortPeerDeviceID_Type()
)
qtechVxuVxlPortPeerDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortPeerDeviceID.setStatus("current")
_QtechVxuVxlPortPeerSlotID_Type = Integer32
_QtechVxuVxlPortPeerSlotID_Object = MibTableColumn
qtechVxuVxlPortPeerSlotID = _QtechVxuVxlPortPeerSlotID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 9),
    _QtechVxuVxlPortPeerSlotID_Type()
)
qtechVxuVxlPortPeerSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortPeerSlotID.setStatus("current")
_QtechVxuVxlPortPeerID_Type = Integer32
_QtechVxuVxlPortPeerID_Object = MibTableColumn
qtechVxuVxlPortPeerID = _QtechVxuVxlPortPeerID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 2, 2, 1, 10),
    _QtechVxuVxlPortPeerID_Type()
)
qtechVxuVxlPortPeerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVxlPortPeerID.setStatus("current")
_QtechVxuLocation_ObjectIdentity = ObjectIdentity
qtechVxuLocation = _QtechVxuLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 3)
)
_QtechVxuLocationTable_Object = MibTable
qtechVxuLocationTable = _QtechVxuLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechVxuLocationTable.setStatus("current")
_QtechVxuLocationEntry_Object = MibTableRow
qtechVxuLocationEntry = _QtechVxuLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 3, 1, 1)
)
qtechVxuLocationEntry.setIndexNames(
    (0, "QTECH-VXU-MIB", "qtechVxuLocationDeviceID"),
    (0, "QTECH-VXU-MIB", "qtechVxuLocationSlotID"),
)
if mibBuilder.loadTexts:
    qtechVxuLocationEntry.setStatus("current")
_QtechVxuLocationDeviceID_Type = Integer32
_QtechVxuLocationDeviceID_Object = MibTableColumn
qtechVxuLocationDeviceID = _QtechVxuLocationDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 3, 1, 1, 1),
    _QtechVxuLocationDeviceID_Type()
)
qtechVxuLocationDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuLocationDeviceID.setStatus("current")
_QtechVxuLocationSlotID_Type = Integer32
_QtechVxuLocationSlotID_Object = MibTableColumn
qtechVxuLocationSlotID = _QtechVxuLocationSlotID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 3, 1, 1, 2),
    _QtechVxuLocationSlotID_Type()
)
qtechVxuLocationSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuLocationSlotID.setStatus("current")


class _QtechVxuLocationSet_Type(Integer32):
    """Custom type qtechVxuLocationSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("light", 1)
    )


_QtechVxuLocationSet_Type.__name__ = "Integer32"
_QtechVxuLocationSet_Object = MibTableColumn
qtechVxuLocationSet = _QtechVxuLocationSet_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 3, 1, 1, 3),
    _QtechVxuLocationSet_Type()
)
qtechVxuLocationSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechVxuLocationSet.setStatus("current")
_QtechVxuVersion_Type = DisplayString
_QtechVxuVersion_Object = MibScalar
qtechVxuVersion = _QtechVxuVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 1, 4),
    _QtechVxuVersion_Type()
)
qtechVxuVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechVxuVersion.setStatus("current")
_QtechVxuMIBTraps_ObjectIdentity = ObjectIdentity
qtechVxuMIBTraps = _QtechVxuMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2)
)
_QtechVxuTrapsNtfObjects_ObjectIdentity = ObjectIdentity
qtechVxuTrapsNtfObjects = _QtechVxuTrapsNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2, 1)
)


class _QtechVxuDeviceState_Type(Integer32):
    """Custom type qtechVxuDeviceState based on Integer32"""
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


_QtechVxuDeviceState_Type.__name__ = "Integer32"
_QtechVxuDeviceState_Object = MibScalar
qtechVxuDeviceState = _QtechVxuDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2, 1, 1),
    _QtechVxuDeviceState_Type()
)
qtechVxuDeviceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVxuDeviceState.setStatus("current")


class _QtechVxuVxlState_Type(Integer32):
    """Custom type qtechVxuVxlState based on Integer32"""
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


_QtechVxuVxlState_Type.__name__ = "Integer32"
_QtechVxuVxlState_Object = MibScalar
qtechVxuVxlState = _QtechVxuVxlState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2, 1, 2),
    _QtechVxuVxlState_Type()
)
qtechVxuVxlState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechVxuVxlState.setStatus("current")
_QtechVxuTrapsNotifications_ObjectIdentity = ObjectIdentity
qtechVxuTrapsNotifications = _QtechVxuTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2, 2)
)

# Managed Objects groups


# Notification objects

qtechVxuNotifyDeviceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2, 2, 1)
)
qtechVxuNotifyDeviceChange.setObjects(
      *(("QTECH-VXU-MIB", "qtechVxuLocationDeviceID"),
        ("QTECH-VXU-MIB", "qtechVxuLocationSlotID"),
        ("QTECH-VXU-MIB", "qtechVxuDeviceState"))
)
if mibBuilder.loadTexts:
    qtechVxuNotifyDeviceChange.setStatus(
        "current"
    )

qtechVxuNotifyVxlChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 126, 2, 2, 2)
)
qtechVxuNotifyVxlChange.setObjects(
      *(("QTECH-VXU-MIB", "qtechVxuVxlPortDeviceID"),
        ("QTECH-VXU-MIB", "qtechVxuVxlPortSlotID"),
        ("QTECH-VXU-MIB", "qtechVxuVxlPortID"),
        ("QTECH-VXU-MIB", "qtechVxuVxlState"))
)
if mibBuilder.loadTexts:
    qtechVxuNotifyVxlChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VXU-MIB",
    **{"qtechVxuMIB": qtechVxuMIB,
       "qtechVxuMIBObjects": qtechVxuMIBObjects,
       "qtechVxuDeviceInfo": qtechVxuDeviceInfo,
       "qtechVxuDeviceTable": qtechVxuDeviceTable,
       "qtechVxuDeviceEntry": qtechVxuDeviceEntry,
       "qtechVxuDeviceID": qtechVxuDeviceID,
       "qtechVxuDeviceMac": qtechVxuDeviceMac,
       "qtechVxuDeviceDescr": qtechVxuDeviceDescr,
       "qtechVxuDeviceRole": qtechVxuDeviceRole,
       "qtechVxuVxl": qtechVxuVxl,
       "qtechVxuVxlTable": qtechVxuVxlTable,
       "qtechVxuVxlEntry": qtechVxuVxlEntry,
       "qtechVxuChildDeviceID": qtechVxuChildDeviceID,
       "qtechVxuFatherDeviceID": qtechVxuFatherDeviceID,
       "qtechVxuFatherVxlIndex": qtechVxuFatherVxlIndex,
       "qtechVxuVxlMode": qtechVxuVxlMode,
       "qtechVxuVxlPortTable": qtechVxuVxlPortTable,
       "qtechVxuVxlPortEntry": qtechVxuVxlPortEntry,
       "qtechVxuVxlDeviceID": qtechVxuVxlDeviceID,
       "qtechVxuVxlIndex": qtechVxuVxlIndex,
       "qtechVxuVxlPortIndex": qtechVxuVxlPortIndex,
       "qtechVxuVxlPortMode": qtechVxuVxlPortMode,
       "qtechVxuVxlPortDeviceID": qtechVxuVxlPortDeviceID,
       "qtechVxuVxlPortSlotID": qtechVxuVxlPortSlotID,
       "qtechVxuVxlPortID": qtechVxuVxlPortID,
       "qtechVxuVxlPortPeerDeviceID": qtechVxuVxlPortPeerDeviceID,
       "qtechVxuVxlPortPeerSlotID": qtechVxuVxlPortPeerSlotID,
       "qtechVxuVxlPortPeerID": qtechVxuVxlPortPeerID,
       "qtechVxuLocation": qtechVxuLocation,
       "qtechVxuLocationTable": qtechVxuLocationTable,
       "qtechVxuLocationEntry": qtechVxuLocationEntry,
       "qtechVxuLocationDeviceID": qtechVxuLocationDeviceID,
       "qtechVxuLocationSlotID": qtechVxuLocationSlotID,
       "qtechVxuLocationSet": qtechVxuLocationSet,
       "qtechVxuVersion": qtechVxuVersion,
       "qtechVxuMIBTraps": qtechVxuMIBTraps,
       "qtechVxuTrapsNtfObjects": qtechVxuTrapsNtfObjects,
       "qtechVxuDeviceState": qtechVxuDeviceState,
       "qtechVxuVxlState": qtechVxuVxlState,
       "qtechVxuTrapsNotifications": qtechVxuTrapsNotifications,
       "qtechVxuNotifyDeviceChange": qtechVxuNotifyDeviceChange,
       "qtechVxuNotifyVxlChange": qtechVxuNotifyVxlChange}
)
