# SNMP MIB module (METROPAD3) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/padtec/LIGHTPAD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:05 2025
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

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmp,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

moduleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    moduleIdentity.setRevisions(
        ("2009-04-23 16:17",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_LightpadMIBGroups_ObjectIdentity = ObjectIdentity
lightpadMIBGroups = _LightpadMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1, 1)
)
_Padtec_ObjectIdentity = ObjectIdentity
padtec = _Padtec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14846)
)
_Metropad3_ObjectIdentity = ObjectIdentity
metropad3 = _Metropad3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14846, 3)
)
_NeTable_Object = MibTable
neTable = _NeTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1)
)
if mibBuilder.loadTexts:
    neTable.setStatus("current")
_NeEntry_Object = MibTableRow
neEntry = _NeEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1, 1)
)
neEntry.setIndexNames(
    (0, "METROPAD3", "neId"),
)
if mibBuilder.loadTexts:
    neEntry.setStatus("current")


class _NeId_Type(Integer32):
    """Custom type neId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NeId_Type.__name__ = "Integer32"
_NeId_Object = MibTableColumn
neId = _NeId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1, 1, 1),
    _NeId_Type()
)
neId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    neId.setStatus("current")
_NeName_Type = OctetString
_NeName_Object = MibTableColumn
neName = _NeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1, 1, 2),
    _NeName_Type()
)
neName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neName.setStatus("current")
_NeNetwork_Type = OctetString
_NeNetwork_Object = MibTableColumn
neNetwork = _NeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1, 1, 3),
    _NeNetwork_Type()
)
neNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNetwork.setStatus("current")
_NeMap_Type = OctetString
_NeMap_Object = MibTableColumn
neMap = _NeMap_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1, 1, 4),
    _NeMap_Type()
)
neMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neMap.setStatus("current")
_NeRowStatus_Type = RowStatus
_NeRowStatus_Object = MibTableColumn
neRowStatus = _NeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 1, 1, 5),
    _NeRowStatus_Type()
)
neRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    neRowStatus.setStatus("current")
_BoardTable_Object = MibTable
boardTable = _BoardTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2)
)
if mibBuilder.loadTexts:
    boardTable.setStatus("current")
_BoardEntry_Object = MibTableRow
boardEntry = _BoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1)
)
boardEntry.setIndexNames(
    (0, "METROPAD3", "boardId"),
)
if mibBuilder.loadTexts:
    boardEntry.setStatus("current")


class _BoardId_Type(Integer32):
    """Custom type boardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardId_Type.__name__ = "Integer32"
_BoardId_Object = MibTableColumn
boardId = _BoardId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 1),
    _BoardId_Type()
)
boardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardId.setStatus("current")
_BoardPart_Type = Integer32
_BoardPart_Object = MibTableColumn
boardPart = _BoardPart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 2),
    _BoardPart_Type()
)
boardPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPart.setStatus("current")
_BoardSerial_Type = Integer32
_BoardSerial_Object = MibTableColumn
boardSerial = _BoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 3),
    _BoardSerial_Type()
)
boardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSerial.setStatus("current")
_BoardModel_Type = OctetString
_BoardModel_Object = MibTableColumn
boardModel = _BoardModel_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 4),
    _BoardModel_Type()
)
boardModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardModel.setStatus("current")
_BoardName_Type = OctetString
_BoardName_Object = MibTableColumn
boardName = _BoardName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 5),
    _BoardName_Type()
)
boardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardName.setStatus("current")
_BoardDescription_Type = OctetString
_BoardDescription_Object = MibTableColumn
boardDescription = _BoardDescription_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 6),
    _BoardDescription_Type()
)
boardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardDescription.setStatus("current")


class _BoardSubRack_Type(Integer32):
    """Custom type boardSubRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardSubRack_Type.__name__ = "Integer32"
_BoardSubRack_Object = MibTableColumn
boardSubRack = _BoardSubRack_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 7),
    _BoardSubRack_Type()
)
boardSubRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSubRack.setStatus("current")


class _BoardSlot_Type(Integer32):
    """Custom type boardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardSlot_Type.__name__ = "Integer32"
_BoardSlot_Object = MibTableColumn
boardSlot = _BoardSlot_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 8),
    _BoardSlot_Type()
)
boardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardSlot.setStatus("current")
_BoardVersion_Type = OctetString
_BoardVersion_Object = MibTableColumn
boardVersion = _BoardVersion_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 9),
    _BoardVersion_Type()
)
boardVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardVersion.setStatus("current")
_BoardNeName_Type = OctetString
_BoardNeName_Object = MibTableColumn
boardNeName = _BoardNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 10),
    _BoardNeName_Type()
)
boardNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardNeName.setStatus("current")
_BoardNeMap_Type = OctetString
_BoardNeMap_Object = MibTableColumn
boardNeMap = _BoardNeMap_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 11),
    _BoardNeMap_Type()
)
boardNeMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardNeMap.setStatus("current")


class _BoardState_Type(Integer32):
    """Custom type boardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operation", 1),
          ("test", 2))
    )


_BoardState_Type.__name__ = "Integer32"
_BoardState_Object = MibTableColumn
boardState = _BoardState_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 12),
    _BoardState_Type()
)
boardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardState.setStatus("current")
_BoardRowStatus_Type = RowStatus
_BoardRowStatus_Object = MibTableColumn
boardRowStatus = _BoardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 13),
    _BoardRowStatus_Type()
)
boardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    boardRowStatus.setStatus("current")


class _BoardRackPosition_Type(Integer32):
    """Custom type boardRackPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BoardRackPosition_Type.__name__ = "Integer32"
_BoardRackPosition_Object = MibTableColumn
boardRackPosition = _BoardRackPosition_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 2, 1, 14),
    _BoardRackPosition_Type()
)
boardRackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardRackPosition.setStatus("current")
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1)
)
alarmEntry.setIndexNames(
    (0, "METROPAD3", "alarmId"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")


class _AlarmId_Type(Integer32):
    """Custom type alarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlarmId_Type.__name__ = "Integer32"
_AlarmId_Object = MibTableColumn
alarmId = _AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 1),
    _AlarmId_Type()
)
alarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmId.setStatus("current")
_AlarmType_Type = Integer32
_AlarmType_Object = MibTableColumn
alarmType = _AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 2),
    _AlarmType_Type()
)
alarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmType.setStatus("current")


class _AlarmSeverity_Type(Integer32):
    """Custom type alarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_AlarmSeverity_Type.__name__ = "Integer32"
_AlarmSeverity_Object = MibTableColumn
alarmSeverity = _AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 3),
    _AlarmSeverity_Type()
)
alarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmSeverity.setStatus("current")
_AlarmName_Type = OctetString
_AlarmName_Object = MibTableColumn
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 4),
    _AlarmName_Type()
)
alarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")


class _AlarmBoardPart_Type(Integer32):
    """Custom type alarmBoardPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AlarmBoardPart_Type.__name__ = "Integer32"
_AlarmBoardPart_Object = MibTableColumn
alarmBoardPart = _AlarmBoardPart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 5),
    _AlarmBoardPart_Type()
)
alarmBoardPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBoardPart.setStatus("current")


class _AlarmBoardSerial_Type(Integer32):
    """Custom type alarmBoardSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AlarmBoardSerial_Type.__name__ = "Integer32"
_AlarmBoardSerial_Object = MibTableColumn
alarmBoardSerial = _AlarmBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 6),
    _AlarmBoardSerial_Type()
)
alarmBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBoardSerial.setStatus("current")


class _AlarmBoardSubRack_Type(Integer32):
    """Custom type alarmBoardSubRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AlarmBoardSubRack_Type.__name__ = "Integer32"
_AlarmBoardSubRack_Object = MibTableColumn
alarmBoardSubRack = _AlarmBoardSubRack_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 7),
    _AlarmBoardSubRack_Type()
)
alarmBoardSubRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBoardSubRack.setStatus("current")


class _AlarmBoardSlot_Type(Integer32):
    """Custom type alarmBoardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AlarmBoardSlot_Type.__name__ = "Integer32"
_AlarmBoardSlot_Object = MibTableColumn
alarmBoardSlot = _AlarmBoardSlot_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 8),
    _AlarmBoardSlot_Type()
)
alarmBoardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBoardSlot.setStatus("current")
_AlarmStart_Type = DateAndTime
_AlarmStart_Object = MibTableColumn
alarmStart = _AlarmStart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 9),
    _AlarmStart_Type()
)
alarmStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStart.setStatus("current")
_AlarmEnd_Type = DateAndTime
_AlarmEnd_Object = MibTableColumn
alarmEnd = _AlarmEnd_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 10),
    _AlarmEnd_Type()
)
alarmEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmEnd.setStatus("current")
_AlarmAckDate_Type = DateAndTime
_AlarmAckDate_Object = MibTableColumn
alarmAckDate = _AlarmAckDate_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 11),
    _AlarmAckDate_Type()
)
alarmAckDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAckDate.setStatus("current")
_AlarmAckDescription_Type = OctetString
_AlarmAckDescription_Object = MibTableColumn
alarmAckDescription = _AlarmAckDescription_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 12),
    _AlarmAckDescription_Type()
)
alarmAckDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAckDescription.setStatus("current")
_AlarmAckUser_Type = OctetString
_AlarmAckUser_Object = MibTableColumn
alarmAckUser = _AlarmAckUser_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 13),
    _AlarmAckUser_Type()
)
alarmAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmAckUser.setStatus("current")
_AlarmNeName_Type = OctetString
_AlarmNeName_Object = MibTableColumn
alarmNeName = _AlarmNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 14),
    _AlarmNeName_Type()
)
alarmNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNeName.setStatus("current")
_AlarmNeMap_Type = OctetString
_AlarmNeMap_Object = MibTableColumn
alarmNeMap = _AlarmNeMap_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 15),
    _AlarmNeMap_Type()
)
alarmNeMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNeMap.setStatus("current")
_AlarmRowStatus_Type = RowStatus
_AlarmRowStatus_Object = MibTableColumn
alarmRowStatus = _AlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 16),
    _AlarmRowStatus_Type()
)
alarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmRowStatus.setStatus("current")


class _AlarmBoardRackPosition_Type(Integer32):
    """Custom type alarmBoardRackPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlarmBoardRackPosition_Type.__name__ = "Integer32"
_AlarmBoardRackPosition_Object = MibTableColumn
alarmBoardRackPosition = _AlarmBoardRackPosition_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 17),
    _AlarmBoardRackPosition_Type()
)
alarmBoardRackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmBoardRackPosition.setStatus("current")
_AlarmResource_Type = OctetString
_AlarmResource_Object = MibTableColumn
alarmResource = _AlarmResource_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 3, 1, 18),
    _AlarmResource_Type()
)
alarmResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmResource.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1)
)
eventEntry.setIndexNames(
    (0, "METROPAD3", "eventId"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")


class _EventId_Type(Integer32):
    """Custom type eventId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventId_Type.__name__ = "Integer32"
_EventId_Object = MibTableColumn
eventId = _EventId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 1),
    _EventId_Type()
)
eventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventId.setStatus("current")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("newNe", 0),
          ("removeNe", 1),
          ("newBoard", 2),
          ("removeBoard", 3),
          ("boardInOperation", 4),
          ("boardInTest", 5),
          ("updateNE", 6))
    )


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 2),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventName_Type = OctetString
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")


class _EventBoardPart_Type(Integer32):
    """Custom type eventBoardPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EventBoardPart_Type.__name__ = "Integer32"
_EventBoardPart_Object = MibTableColumn
eventBoardPart = _EventBoardPart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 4),
    _EventBoardPart_Type()
)
eventBoardPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventBoardPart.setStatus("current")


class _EventBoardSerial_Type(Integer32):
    """Custom type eventBoardSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EventBoardSerial_Type.__name__ = "Integer32"
_EventBoardSerial_Object = MibTableColumn
eventBoardSerial = _EventBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 5),
    _EventBoardSerial_Type()
)
eventBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventBoardSerial.setStatus("current")


class _EventBoardSubRack_Type(Integer32):
    """Custom type eventBoardSubRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EventBoardSubRack_Type.__name__ = "Integer32"
_EventBoardSubRack_Object = MibTableColumn
eventBoardSubRack = _EventBoardSubRack_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 6),
    _EventBoardSubRack_Type()
)
eventBoardSubRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventBoardSubRack.setStatus("current")


class _EventBoardSlot_Type(Integer32):
    """Custom type eventBoardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EventBoardSlot_Type.__name__ = "Integer32"
_EventBoardSlot_Object = MibTableColumn
eventBoardSlot = _EventBoardSlot_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 7),
    _EventBoardSlot_Type()
)
eventBoardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventBoardSlot.setStatus("current")
_EventTime_Type = DateAndTime
_EventTime_Object = MibTableColumn
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 8),
    _EventTime_Type()
)
eventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_EventNeName_Type = OctetString
_EventNeName_Object = MibTableColumn
eventNeName = _EventNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 9),
    _EventNeName_Type()
)
eventNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNeName.setStatus("current")
_EventNeMap_Type = OctetString
_EventNeMap_Object = MibTableColumn
eventNeMap = _EventNeMap_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 10),
    _EventNeMap_Type()
)
eventNeMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNeMap.setStatus("current")
_EventRowStatus_Type = RowStatus
_EventRowStatus_Object = MibTableColumn
eventRowStatus = _EventRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 11),
    _EventRowStatus_Type()
)
eventRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eventRowStatus.setStatus("current")


class _EventBoardRackPosition_Type(Integer32):
    """Custom type eventBoardRackPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EventBoardRackPosition_Type.__name__ = "Integer32"
_EventBoardRackPosition_Object = MibTableColumn
eventBoardRackPosition = _EventBoardRackPosition_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 4, 1, 12),
    _EventBoardRackPosition_Type()
)
eventBoardRackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventBoardRackPosition.setStatus("current")
_PerformanceTable_Object = MibTable
performanceTable = _PerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5)
)
if mibBuilder.loadTexts:
    performanceTable.setStatus("current")
_PerformanceEntry_Object = MibTableRow
performanceEntry = _PerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1)
)
performanceEntry.setIndexNames(
    (0, "METROPAD3", "performanceId"),
)
if mibBuilder.loadTexts:
    performanceEntry.setStatus("current")


class _PerformanceId_Type(Integer32):
    """Custom type performanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PerformanceId_Type.__name__ = "Integer32"
_PerformanceId_Object = MibTableColumn
performanceId = _PerformanceId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 1),
    _PerformanceId_Type()
)
performanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    performanceId.setStatus("current")
_PerformanceBoardPart_Type = Integer32
_PerformanceBoardPart_Object = MibTableColumn
performanceBoardPart = _PerformanceBoardPart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 2),
    _PerformanceBoardPart_Type()
)
performanceBoardPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceBoardPart.setStatus("current")
_PerformanceBoardSerial_Type = Integer32
_PerformanceBoardSerial_Object = MibTableColumn
performanceBoardSerial = _PerformanceBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 3),
    _PerformanceBoardSerial_Type()
)
performanceBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceBoardSerial.setStatus("current")
_PerformanceType_Type = Integer32
_PerformanceType_Object = MibTableColumn
performanceType = _PerformanceType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 5),
    _PerformanceType_Type()
)
performanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceType.setStatus("current")


class _PerformancePortType_Type(Integer32):
    """Custom type performancePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("wdm", 2))
    )


_PerformancePortType_Type.__name__ = "Integer32"
_PerformancePortType_Object = MibTableColumn
performancePortType = _PerformancePortType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 6),
    _PerformancePortType_Type()
)
performancePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performancePortType.setStatus("current")
_PerformancePortNumber_Type = Integer32
_PerformancePortNumber_Object = MibTableColumn
performancePortNumber = _PerformancePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 7),
    _PerformancePortNumber_Type()
)
performancePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performancePortNumber.setStatus("current")
_PerformanceValue_Type = Integer32
_PerformanceValue_Object = MibTableColumn
performanceValue = _PerformanceValue_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 8),
    _PerformanceValue_Type()
)
performanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceValue.setStatus("current")
_PerformanceRate_Type = OctetString
_PerformanceRate_Object = MibTableColumn
performanceRate = _PerformanceRate_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 9),
    _PerformanceRate_Type()
)
performanceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceRate.setStatus("current")
_PerformanceTime_Type = DateAndTime
_PerformanceTime_Object = MibTableColumn
performanceTime = _PerformanceTime_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 10),
    _PerformanceTime_Type()
)
performanceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceTime.setStatus("current")
_PerformanceNeName_Type = OctetString
_PerformanceNeName_Object = MibTableColumn
performanceNeName = _PerformanceNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 11),
    _PerformanceNeName_Type()
)
performanceNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceNeName.setStatus("current")
_PerformanceNeMap_Type = OctetString
_PerformanceNeMap_Object = MibTableColumn
performanceNeMap = _PerformanceNeMap_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 12),
    _PerformanceNeMap_Type()
)
performanceNeMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceNeMap.setStatus("current")
_PerformanceRowStatus_Type = RowStatus
_PerformanceRowStatus_Object = MibTableColumn
performanceRowStatus = _PerformanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 13),
    _PerformanceRowStatus_Type()
)
performanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    performanceRowStatus.setStatus("current")
_PerformanceOid_Type = Integer32
_PerformanceOid_Object = MibTableColumn
performanceOid = _PerformanceOid_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 5, 1, 14),
    _PerformanceOid_Type()
)
performanceOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    performanceOid.setStatus("current")
_ServerStatus_ObjectIdentity = ObjectIdentity
serverStatus = _ServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6)
)
_ServerMasterIp_Type = IpAddress
_ServerMasterIp_Object = MibScalar
serverMasterIp = _ServerMasterIp_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 1),
    _ServerMasterIp_Type()
)
serverMasterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMasterIp.setStatus("current")
_ServerSlaveIp_Type = IpAddress
_ServerSlaveIp_Object = MibScalar
serverSlaveIp = _ServerSlaveIp_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 2),
    _ServerSlaveIp_Type()
)
serverSlaveIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSlaveIp.setStatus("current")
_ServerIsActive_Type = IpAddress
_ServerIsActive_Object = MibScalar
serverIsActive = _ServerIsActive_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 3),
    _ServerIsActive_Type()
)
serverIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIsActive.setStatus("current")
_ServerVersion_Type = OctetString
_ServerVersion_Object = MibScalar
serverVersion = _ServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 4),
    _ServerVersion_Type()
)
serverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverVersion.setStatus("current")
_ServerBuild_Type = OctetString
_ServerBuild_Object = MibScalar
serverBuild = _ServerBuild_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 5),
    _ServerBuild_Type()
)
serverBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverBuild.setStatus("current")
_ServerUpTime_Type = TimeTicks
_ServerUpTime_Object = MibScalar
serverUpTime = _ServerUpTime_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 6),
    _ServerUpTime_Type()
)
serverUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverUpTime.setStatus("current")
_ServerSo_Type = OctetString
_ServerSo_Object = MibScalar
serverSo = _ServerSo_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 7),
    _ServerSo_Type()
)
serverSo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSo.setStatus("current")
_ServerFreeDiskSpace_Type = Integer32
_ServerFreeDiskSpace_Object = MibScalar
serverFreeDiskSpace = _ServerFreeDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 8),
    _ServerFreeDiskSpace_Type()
)
serverFreeDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverFreeDiskSpace.setStatus("current")
_ServerSync_Type = TruthValue
_ServerSync_Object = MibScalar
serverSync = _ServerSync_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 6, 9),
    _ServerSync_Type()
)
serverSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSync.setStatus("current")
_NetworkAlarmTable_Object = MibTable
networkAlarmTable = _NetworkAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12)
)
if mibBuilder.loadTexts:
    networkAlarmTable.setStatus("current")
_NetworkAlarmEntry_Object = MibTableRow
networkAlarmEntry = _NetworkAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1)
)
networkAlarmEntry.setIndexNames(
    (0, "METROPAD3", "networkAlarmId"),
)
if mibBuilder.loadTexts:
    networkAlarmEntry.setStatus("current")


class _NetworkAlarmId_Type(Integer32):
    """Custom type networkAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetworkAlarmId_Type.__name__ = "Integer32"
_NetworkAlarmId_Object = MibTableColumn
networkAlarmId = _NetworkAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 1),
    _NetworkAlarmId_Type()
)
networkAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAlarmId.setStatus("current")


class _NetworkAlarmSeverity_Type(Integer32):
    """Custom type networkAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("indeterminated", 0),
          ("clear", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_NetworkAlarmSeverity_Type.__name__ = "Integer32"
_NetworkAlarmSeverity_Object = MibTableColumn
networkAlarmSeverity = _NetworkAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 2),
    _NetworkAlarmSeverity_Type()
)
networkAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmSeverity.setStatus("current")
_NetworkAlarmKey_Type = Integer32
_NetworkAlarmKey_Object = MibTableColumn
networkAlarmKey = _NetworkAlarmKey_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 3),
    _NetworkAlarmKey_Type()
)
networkAlarmKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmKey.setStatus("current")


class _NetworkAlarmGroup_Type(Integer32):
    """Custom type networkAlarmGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("communicationsAlarm", 2),
          ("environmentalAlarm", 3),
          ("equipmentAlarm", 4),
          ("processingErrorAlarm", 10),
          ("qualityOfServiceAlarm", 11))
    )


_NetworkAlarmGroup_Type.__name__ = "Integer32"
_NetworkAlarmGroup_Object = MibTableColumn
networkAlarmGroup = _NetworkAlarmGroup_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 4),
    _NetworkAlarmGroup_Type()
)
networkAlarmGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmGroup.setStatus("current")
_NetworkAlarmStart_Type = DateAndTime
_NetworkAlarmStart_Object = MibTableColumn
networkAlarmStart = _NetworkAlarmStart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 5),
    _NetworkAlarmStart_Type()
)
networkAlarmStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmStart.setStatus("current")
_NetworkAlarmEnd_Type = DateAndTime
_NetworkAlarmEnd_Object = MibTableColumn
networkAlarmEnd = _NetworkAlarmEnd_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 6),
    _NetworkAlarmEnd_Type()
)
networkAlarmEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmEnd.setStatus("current")
_NetworkAlarmNetworkName_Type = OctetString
_NetworkAlarmNetworkName_Object = MibTableColumn
networkAlarmNetworkName = _NetworkAlarmNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 7),
    _NetworkAlarmNetworkName_Type()
)
networkAlarmNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmNetworkName.setStatus("current")
_NetworkAlarmResource_Type = OctetString
_NetworkAlarmResource_Object = MibTableColumn
networkAlarmResource = _NetworkAlarmResource_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 8),
    _NetworkAlarmResource_Type()
)
networkAlarmResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmResource.setStatus("current")


class _NetworkAlarmLayer_Type(Integer32):
    """Custom type networkAlarmLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ots", 1),
          ("oms", 2),
          ("circuit", 3))
    )


_NetworkAlarmLayer_Type.__name__ = "Integer32"
_NetworkAlarmLayer_Object = MibTableColumn
networkAlarmLayer = _NetworkAlarmLayer_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 9),
    _NetworkAlarmLayer_Type()
)
networkAlarmLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmLayer.setStatus("current")
_NetworkAlarmNeName_Type = OctetString
_NetworkAlarmNeName_Object = MibTableColumn
networkAlarmNeName = _NetworkAlarmNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 10),
    _NetworkAlarmNeName_Type()
)
networkAlarmNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmNeName.setStatus("current")
_NetworkAlarmBoardName_Type = OctetString
_NetworkAlarmBoardName_Object = MibTableColumn
networkAlarmBoardName = _NetworkAlarmBoardName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 11),
    _NetworkAlarmBoardName_Type()
)
networkAlarmBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmBoardName.setStatus("current")
_NetworkAlarmName_Type = OctetString
_NetworkAlarmName_Object = MibTableColumn
networkAlarmName = _NetworkAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 12),
    _NetworkAlarmName_Type()
)
networkAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmName.setStatus("current")


class _NetworkAlarmType_Type(Integer32):
    """Custom type networkAlarmType based on Integer32"""
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ots", 1),
          ("otsClient", 2),
          ("och", 3),
          ("circuit", 4),
          ("oam", 5),
          ("otn25G", 6),
          ("otu1", 7),
          ("odu1", 8),
          ("sdh", 9),
          ("otn10G", 10),
          ("otu2", 11),
          ("odu2", 12),
          ("opu2", 13),
          ("equipment", 14),
          ("management", 15))
    )


_NetworkAlarmType_Type.__name__ = "Integer32"
_NetworkAlarmType_Object = MibTableColumn
networkAlarmType = _NetworkAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 13),
    _NetworkAlarmType_Type()
)
networkAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmType.setStatus("current")
_NetworkAlarmNeNameSource_Type = OctetString
_NetworkAlarmNeNameSource_Object = MibTableColumn
networkAlarmNeNameSource = _NetworkAlarmNeNameSource_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 14),
    _NetworkAlarmNeNameSource_Type()
)
networkAlarmNeNameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmNeNameSource.setStatus("current")
_NetworkAlarmBoardNameSource_Type = OctetString
_NetworkAlarmBoardNameSource_Object = MibTableColumn
networkAlarmBoardNameSource = _NetworkAlarmBoardNameSource_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 15),
    _NetworkAlarmBoardNameSource_Type()
)
networkAlarmBoardNameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmBoardNameSource.setStatus("current")
_NetworkAlarmPortNameSource_Type = OctetString
_NetworkAlarmPortNameSource_Object = MibTableColumn
networkAlarmPortNameSource = _NetworkAlarmPortNameSource_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 16),
    _NetworkAlarmPortNameSource_Type()
)
networkAlarmPortNameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmPortNameSource.setStatus("current")
_NetworkAlarmNeNameDestination_Type = OctetString
_NetworkAlarmNeNameDestination_Object = MibTableColumn
networkAlarmNeNameDestination = _NetworkAlarmNeNameDestination_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 17),
    _NetworkAlarmNeNameDestination_Type()
)
networkAlarmNeNameDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmNeNameDestination.setStatus("current")
_NetworkAlarmBoardNameDestination_Type = OctetString
_NetworkAlarmBoardNameDestination_Object = MibTableColumn
networkAlarmBoardNameDestination = _NetworkAlarmBoardNameDestination_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 18),
    _NetworkAlarmBoardNameDestination_Type()
)
networkAlarmBoardNameDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmBoardNameDestination.setStatus("current")
_NetworkAlarmPortNameDestination_Type = OctetString
_NetworkAlarmPortNameDestination_Object = MibTableColumn
networkAlarmPortNameDestination = _NetworkAlarmPortNameDestination_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 19),
    _NetworkAlarmPortNameDestination_Type()
)
networkAlarmPortNameDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmPortNameDestination.setStatus("current")
_NetworkAlarmAck_Type = TruthValue
_NetworkAlarmAck_Object = MibTableColumn
networkAlarmAck = _NetworkAlarmAck_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 20),
    _NetworkAlarmAck_Type()
)
networkAlarmAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmAck.setStatus("current")
_NetworkAlarmAckDate_Type = DateAndTime
_NetworkAlarmAckDate_Object = MibTableColumn
networkAlarmAckDate = _NetworkAlarmAckDate_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 21),
    _NetworkAlarmAckDate_Type()
)
networkAlarmAckDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmAckDate.setStatus("current")
_NetworkAlarmAckUser_Type = OctetString
_NetworkAlarmAckUser_Object = MibTableColumn
networkAlarmAckUser = _NetworkAlarmAckUser_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 22),
    _NetworkAlarmAckUser_Type()
)
networkAlarmAckUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAlarmAckUser.setStatus("current")
_NetworkAlarmRowStatus_Type = RowStatus
_NetworkAlarmRowStatus_Object = MibTableColumn
networkAlarmRowStatus = _NetworkAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 12, 1, 23),
    _NetworkAlarmRowStatus_Type()
)
networkAlarmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkAlarmRowStatus.setStatus("current")
_OtsTrailTable_Object = MibTable
otsTrailTable = _OtsTrailTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13)
)
if mibBuilder.loadTexts:
    otsTrailTable.setStatus("current")
_OtsTrailEntry_Object = MibTableRow
otsTrailEntry = _OtsTrailEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1)
)
otsTrailEntry.setIndexNames(
    (0, "METROPAD3", "otsTrailId"),
)
if mibBuilder.loadTexts:
    otsTrailEntry.setStatus("current")


class _OtsTrailId_Type(Integer32):
    """Custom type otsTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OtsTrailId_Type.__name__ = "Integer32"
_OtsTrailId_Object = MibTableColumn
otsTrailId = _OtsTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 1),
    _OtsTrailId_Type()
)
otsTrailId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otsTrailId.setStatus("current")
_OtsTrailName_Type = OctetString
_OtsTrailName_Object = MibTableColumn
otsTrailName = _OtsTrailName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 2),
    _OtsTrailName_Type()
)
otsTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailName.setStatus("current")
_OtsTrailDescription_Type = OctetString
_OtsTrailDescription_Object = MibTableColumn
otsTrailDescription = _OtsTrailDescription_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 3),
    _OtsTrailDescription_Type()
)
otsTrailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailDescription.setStatus("current")
_OtsTrailFiberType_Type = OctetString
_OtsTrailFiberType_Object = MibTableColumn
otsTrailFiberType = _OtsTrailFiberType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 4),
    _OtsTrailFiberType_Type()
)
otsTrailFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailFiberType.setStatus("current")
_OtsTrailDistance_Type = Integer32
_OtsTrailDistance_Object = MibTableColumn
otsTrailDistance = _OtsTrailDistance_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 5),
    _OtsTrailDistance_Type()
)
otsTrailDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailDistance.setStatus("current")
_OtsTrailSourceNE_Type = OctetString
_OtsTrailSourceNE_Object = MibTableColumn
otsTrailSourceNE = _OtsTrailSourceNE_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 6),
    _OtsTrailSourceNE_Type()
)
otsTrailSourceNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailSourceNE.setStatus("current")
_OtsTrailSourceBoard_Type = OctetString
_OtsTrailSourceBoard_Object = MibTableColumn
otsTrailSourceBoard = _OtsTrailSourceBoard_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 7),
    _OtsTrailSourceBoard_Type()
)
otsTrailSourceBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailSourceBoard.setStatus("current")
_OtsTrailSourcePort_Type = OctetString
_OtsTrailSourcePort_Object = MibTableColumn
otsTrailSourcePort = _OtsTrailSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 8),
    _OtsTrailSourcePort_Type()
)
otsTrailSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailSourcePort.setStatus("current")
_OtsTrailDestinationNE_Type = OctetString
_OtsTrailDestinationNE_Object = MibTableColumn
otsTrailDestinationNE = _OtsTrailDestinationNE_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 9),
    _OtsTrailDestinationNE_Type()
)
otsTrailDestinationNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailDestinationNE.setStatus("current")
_OtsTrailDestinationBoard_Type = OctetString
_OtsTrailDestinationBoard_Object = MibTableColumn
otsTrailDestinationBoard = _OtsTrailDestinationBoard_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 10),
    _OtsTrailDestinationBoard_Type()
)
otsTrailDestinationBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailDestinationBoard.setStatus("current")
_OtsTrailDestinationPort_Type = OctetString
_OtsTrailDestinationPort_Object = MibTableColumn
otsTrailDestinationPort = _OtsTrailDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 11),
    _OtsTrailDestinationPort_Type()
)
otsTrailDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailDestinationPort.setStatus("current")


class _OtsTrailDatabaseId_Type(Integer32):
    """Custom type otsTrailDatabaseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OtsTrailDatabaseId_Type.__name__ = "Integer32"
_OtsTrailDatabaseId_Object = MibTableColumn
otsTrailDatabaseId = _OtsTrailDatabaseId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 12),
    _OtsTrailDatabaseId_Type()
)
otsTrailDatabaseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otsTrailDatabaseId.setStatus("current")
_OtsTrailRowStatus_Type = RowStatus
_OtsTrailRowStatus_Object = MibTableColumn
otsTrailRowStatus = _OtsTrailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 13, 1, 13),
    _OtsTrailRowStatus_Type()
)
otsTrailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otsTrailRowStatus.setStatus("current")
_OmsTrailTable_Object = MibTable
omsTrailTable = _OmsTrailTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14)
)
if mibBuilder.loadTexts:
    omsTrailTable.setStatus("current")
_OmsTrailEntry_Object = MibTableRow
omsTrailEntry = _OmsTrailEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1)
)
omsTrailEntry.setIndexNames(
    (0, "METROPAD3", "omsTrailId"),
)
if mibBuilder.loadTexts:
    omsTrailEntry.setStatus("current")


class _OmsTrailId_Type(Integer32):
    """Custom type omsTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OmsTrailId_Type.__name__ = "Integer32"
_OmsTrailId_Object = MibTableColumn
omsTrailId = _OmsTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 1),
    _OmsTrailId_Type()
)
omsTrailId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    omsTrailId.setStatus("current")
_OmsTrailName_Type = OctetString
_OmsTrailName_Object = MibTableColumn
omsTrailName = _OmsTrailName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 2),
    _OmsTrailName_Type()
)
omsTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailName.setStatus("current")
_OmsTrailDescription_Type = OctetString
_OmsTrailDescription_Object = MibTableColumn
omsTrailDescription = _OmsTrailDescription_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 3),
    _OmsTrailDescription_Type()
)
omsTrailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailDescription.setStatus("current")
_OmsTrailSourceNE_Type = OctetString
_OmsTrailSourceNE_Object = MibTableColumn
omsTrailSourceNE = _OmsTrailSourceNE_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 4),
    _OmsTrailSourceNE_Type()
)
omsTrailSourceNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailSourceNE.setStatus("current")
_OmsTrailSourceBoard_Type = OctetString
_OmsTrailSourceBoard_Object = MibTableColumn
omsTrailSourceBoard = _OmsTrailSourceBoard_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 5),
    _OmsTrailSourceBoard_Type()
)
omsTrailSourceBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailSourceBoard.setStatus("current")
_OmsTrailSourcePort_Type = OctetString
_OmsTrailSourcePort_Object = MibTableColumn
omsTrailSourcePort = _OmsTrailSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 6),
    _OmsTrailSourcePort_Type()
)
omsTrailSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailSourcePort.setStatus("current")
_OmsTrailDestinationNE_Type = OctetString
_OmsTrailDestinationNE_Object = MibTableColumn
omsTrailDestinationNE = _OmsTrailDestinationNE_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 7),
    _OmsTrailDestinationNE_Type()
)
omsTrailDestinationNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailDestinationNE.setStatus("current")
_OmsTrailDestinationBoard_Type = OctetString
_OmsTrailDestinationBoard_Object = MibTableColumn
omsTrailDestinationBoard = _OmsTrailDestinationBoard_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 8),
    _OmsTrailDestinationBoard_Type()
)
omsTrailDestinationBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailDestinationBoard.setStatus("current")
_OmsTrailDestinationPort_Type = OctetString
_OmsTrailDestinationPort_Object = MibTableColumn
omsTrailDestinationPort = _OmsTrailDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 9),
    _OmsTrailDestinationPort_Type()
)
omsTrailDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailDestinationPort.setStatus("current")


class _OmsTrailDatabaseId_Type(Integer32):
    """Custom type omsTrailDatabaseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OmsTrailDatabaseId_Type.__name__ = "Integer32"
_OmsTrailDatabaseId_Object = MibTableColumn
omsTrailDatabaseId = _OmsTrailDatabaseId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 10),
    _OmsTrailDatabaseId_Type()
)
omsTrailDatabaseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsTrailDatabaseId.setStatus("current")
_OmsTrailRowStatus_Type = RowStatus
_OmsTrailRowStatus_Object = MibTableColumn
omsTrailRowStatus = _OmsTrailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 14, 1, 11),
    _OmsTrailRowStatus_Type()
)
omsTrailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omsTrailRowStatus.setStatus("current")
_CircuitTrailTable_Object = MibTable
circuitTrailTable = _CircuitTrailTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15)
)
if mibBuilder.loadTexts:
    circuitTrailTable.setStatus("current")
_CircuitTrailEntry_Object = MibTableRow
circuitTrailEntry = _CircuitTrailEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1)
)
circuitTrailEntry.setIndexNames(
    (0, "METROPAD3", "circuitTrailId"),
)
if mibBuilder.loadTexts:
    circuitTrailEntry.setStatus("current")


class _CircuitTrailId_Type(Integer32):
    """Custom type circuitTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CircuitTrailId_Type.__name__ = "Integer32"
_CircuitTrailId_Object = MibTableColumn
circuitTrailId = _CircuitTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 1),
    _CircuitTrailId_Type()
)
circuitTrailId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitTrailId.setStatus("current")
_CircuitTrailName_Type = OctetString
_CircuitTrailName_Object = MibTableColumn
circuitTrailName = _CircuitTrailName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 2),
    _CircuitTrailName_Type()
)
circuitTrailName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailName.setStatus("current")
_CircuitTrailDescription_Type = OctetString
_CircuitTrailDescription_Object = MibTableColumn
circuitTrailDescription = _CircuitTrailDescription_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 3),
    _CircuitTrailDescription_Type()
)
circuitTrailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailDescription.setStatus("current")
_CircuitTrailClientName_Type = OctetString
_CircuitTrailClientName_Object = MibTableColumn
circuitTrailClientName = _CircuitTrailClientName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 4),
    _CircuitTrailClientName_Type()
)
circuitTrailClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailClientName.setStatus("current")
_CircuitTrailClientId_Type = OctetString
_CircuitTrailClientId_Object = MibTableColumn
circuitTrailClientId = _CircuitTrailClientId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 5),
    _CircuitTrailClientId_Type()
)
circuitTrailClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailClientId.setStatus("current")
_CircuitTrailService_Type = OctetString
_CircuitTrailService_Object = MibTableColumn
circuitTrailService = _CircuitTrailService_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 6),
    _CircuitTrailService_Type()
)
circuitTrailService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailService.setStatus("current")
_CircuitTrailSourceNetwork_Type = OctetString
_CircuitTrailSourceNetwork_Object = MibTableColumn
circuitTrailSourceNetwork = _CircuitTrailSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 7),
    _CircuitTrailSourceNetwork_Type()
)
circuitTrailSourceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailSourceNetwork.setStatus("current")
_CircuitTrailSourceNE_Type = OctetString
_CircuitTrailSourceNE_Object = MibTableColumn
circuitTrailSourceNE = _CircuitTrailSourceNE_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 8),
    _CircuitTrailSourceNE_Type()
)
circuitTrailSourceNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailSourceNE.setStatus("current")
_CircuitTrailSourceBoard_Type = OctetString
_CircuitTrailSourceBoard_Object = MibTableColumn
circuitTrailSourceBoard = _CircuitTrailSourceBoard_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 9),
    _CircuitTrailSourceBoard_Type()
)
circuitTrailSourceBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailSourceBoard.setStatus("current")
_CircuitTrailSourcePort_Type = OctetString
_CircuitTrailSourcePort_Object = MibTableColumn
circuitTrailSourcePort = _CircuitTrailSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 10),
    _CircuitTrailSourcePort_Type()
)
circuitTrailSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailSourcePort.setStatus("current")
_CircuitTrailDestinationNetwork_Type = OctetString
_CircuitTrailDestinationNetwork_Object = MibTableColumn
circuitTrailDestinationNetwork = _CircuitTrailDestinationNetwork_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 11),
    _CircuitTrailDestinationNetwork_Type()
)
circuitTrailDestinationNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailDestinationNetwork.setStatus("current")
_CircuitTrailDestinationNE_Type = OctetString
_CircuitTrailDestinationNE_Object = MibTableColumn
circuitTrailDestinationNE = _CircuitTrailDestinationNE_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 12),
    _CircuitTrailDestinationNE_Type()
)
circuitTrailDestinationNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailDestinationNE.setStatus("current")
_CircuitTrailDestinationBoard_Type = OctetString
_CircuitTrailDestinationBoard_Object = MibTableColumn
circuitTrailDestinationBoard = _CircuitTrailDestinationBoard_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 13),
    _CircuitTrailDestinationBoard_Type()
)
circuitTrailDestinationBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailDestinationBoard.setStatus("current")
_CircuitTrailDestinationPort_Type = OctetString
_CircuitTrailDestinationPort_Object = MibTableColumn
circuitTrailDestinationPort = _CircuitTrailDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 14),
    _CircuitTrailDestinationPort_Type()
)
circuitTrailDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailDestinationPort.setStatus("current")


class _CircuitTrailDatabaseId_Type(Integer32):
    """Custom type circuitTrailDatabaseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CircuitTrailDatabaseId_Type.__name__ = "Integer32"
_CircuitTrailDatabaseId_Object = MibTableColumn
circuitTrailDatabaseId = _CircuitTrailDatabaseId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 15),
    _CircuitTrailDatabaseId_Type()
)
circuitTrailDatabaseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitTrailDatabaseId.setStatus("current")
_CircuitTrailRowStatus_Type = RowStatus
_CircuitTrailRowStatus_Object = MibTableColumn
circuitTrailRowStatus = _CircuitTrailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 15, 1, 16),
    _CircuitTrailRowStatus_Type()
)
circuitTrailRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    circuitTrailRowStatus.setStatus("current")
_NetworkEventLogTable_Object = MibTable
networkEventLogTable = _NetworkEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19)
)
if mibBuilder.loadTexts:
    networkEventLogTable.setStatus("current")
_NetworkEventLogEntry_Object = MibTableRow
networkEventLogEntry = _NetworkEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1)
)
networkEventLogEntry.setIndexNames(
    (0, "METROPAD3", "networkEventLogId"),
)
if mibBuilder.loadTexts:
    networkEventLogEntry.setStatus("current")


class _NetworkEventLogId_Type(Integer32):
    """Custom type networkEventLogId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NetworkEventLogId_Type.__name__ = "Integer32"
_NetworkEventLogId_Object = MibTableColumn
networkEventLogId = _NetworkEventLogId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1, 1),
    _NetworkEventLogId_Type()
)
networkEventLogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkEventLogId.setStatus("current")
_NetworkEventLogTime_Type = DateAndTime
_NetworkEventLogTime_Object = MibTableColumn
networkEventLogTime = _NetworkEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1, 2),
    _NetworkEventLogTime_Type()
)
networkEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkEventLogTime.setStatus("current")


class _NetworkEventLogResourceType_Type(Integer32):
    """Custom type networkEventLogResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("ots", 2),
          ("oms", 3),
          ("circuit", 4),
          ("omsotsrelation", 5),
          ("circuitomsrelation", 6))
    )


_NetworkEventLogResourceType_Type.__name__ = "Integer32"
_NetworkEventLogResourceType_Object = MibTableColumn
networkEventLogResourceType = _NetworkEventLogResourceType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1, 3),
    _NetworkEventLogResourceType_Type()
)
networkEventLogResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkEventLogResourceType.setStatus("current")
_NetworkEventLogResourceName_Type = OctetString
_NetworkEventLogResourceName_Object = MibTableColumn
networkEventLogResourceName = _NetworkEventLogResourceName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1, 4),
    _NetworkEventLogResourceName_Type()
)
networkEventLogResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkEventLogResourceName.setStatus("current")


class _NetworkEventLogAction_Type(Integer32):
    """Custom type networkEventLogAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("change", 2),
          ("remove", 3))
    )


_NetworkEventLogAction_Type.__name__ = "Integer32"
_NetworkEventLogAction_Object = MibTableColumn
networkEventLogAction = _NetworkEventLogAction_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1, 5),
    _NetworkEventLogAction_Type()
)
networkEventLogAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkEventLogAction.setStatus("current")
_NetworkEventLogRowStatus_Type = RowStatus
_NetworkEventLogRowStatus_Object = MibTableColumn
networkEventLogRowStatus = _NetworkEventLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 19, 1, 6),
    _NetworkEventLogRowStatus_Type()
)
networkEventLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkEventLogRowStatus.setStatus("current")
_TrailAssociationTable_Object = MibTable
trailAssociationTable = _TrailAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 22)
)
if mibBuilder.loadTexts:
    trailAssociationTable.setStatus("current")
_TrailAssociationEntry_Object = MibTableRow
trailAssociationEntry = _TrailAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 22, 1)
)
trailAssociationEntry.setIndexNames(
    (0, "METROPAD3", "omsOtsAssociationTrailIdIndex"),
)
if mibBuilder.loadTexts:
    trailAssociationEntry.setStatus("current")


class _OmsOtsAssociationTrailIdIndex_Type(Integer32):
    """Custom type omsOtsAssociationTrailIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OmsOtsAssociationTrailIdIndex_Type.__name__ = "Integer32"
_OmsOtsAssociationTrailIdIndex_Object = MibTableColumn
omsOtsAssociationTrailIdIndex = _OmsOtsAssociationTrailIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 22, 1, 1),
    _OmsOtsAssociationTrailIdIndex_Type()
)
omsOtsAssociationTrailIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    omsOtsAssociationTrailIdIndex.setStatus("current")


class _OmsOtsAssociationOtsTrailId_Type(Integer32):
    """Custom type omsOtsAssociationOtsTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OmsOtsAssociationOtsTrailId_Type.__name__ = "Integer32"
_OmsOtsAssociationOtsTrailId_Object = MibTableColumn
omsOtsAssociationOtsTrailId = _OmsOtsAssociationOtsTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 22, 1, 2),
    _OmsOtsAssociationOtsTrailId_Type()
)
omsOtsAssociationOtsTrailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsOtsAssociationOtsTrailId.setStatus("current")


class _OmsOtsAssociationOmsTrailId_Type(Integer32):
    """Custom type omsOtsAssociationOmsTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_OmsOtsAssociationOmsTrailId_Type.__name__ = "Integer32"
_OmsOtsAssociationOmsTrailId_Object = MibTableColumn
omsOtsAssociationOmsTrailId = _OmsOtsAssociationOmsTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 22, 1, 3),
    _OmsOtsAssociationOmsTrailId_Type()
)
omsOtsAssociationOmsTrailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omsOtsAssociationOmsTrailId.setStatus("current")
_OmsOtsAssociationRowStatus_Type = RowStatus
_OmsOtsAssociationRowStatus_Object = MibTableColumn
omsOtsAssociationRowStatus = _OmsOtsAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 22, 1, 4),
    _OmsOtsAssociationRowStatus_Type()
)
omsOtsAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    omsOtsAssociationRowStatus.setStatus("current")
_CircuitAssociationOmsTable_Object = MibTable
circuitAssociationOmsTable = _CircuitAssociationOmsTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 23)
)
if mibBuilder.loadTexts:
    circuitAssociationOmsTable.setStatus("current")
_CircuitAssociationOmsEntry_Object = MibTableRow
circuitAssociationOmsEntry = _CircuitAssociationOmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 23, 1)
)
circuitAssociationOmsEntry.setIndexNames(
    (0, "METROPAD3", "circuitOmsAssociationTrailIdIndex"),
)
if mibBuilder.loadTexts:
    circuitAssociationOmsEntry.setStatus("current")


class _CircuitOmsAssociationTrailIdIndex_Type(Integer32):
    """Custom type circuitOmsAssociationTrailIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CircuitOmsAssociationTrailIdIndex_Type.__name__ = "Integer32"
_CircuitOmsAssociationTrailIdIndex_Object = MibTableColumn
circuitOmsAssociationTrailIdIndex = _CircuitOmsAssociationTrailIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 23, 1, 1),
    _CircuitOmsAssociationTrailIdIndex_Type()
)
circuitOmsAssociationTrailIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    circuitOmsAssociationTrailIdIndex.setStatus("current")


class _CircuitOmsAssociationCircuitTrailId_Type(Integer32):
    """Custom type circuitOmsAssociationCircuitTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CircuitOmsAssociationCircuitTrailId_Type.__name__ = "Integer32"
_CircuitOmsAssociationCircuitTrailId_Object = MibTableColumn
circuitOmsAssociationCircuitTrailId = _CircuitOmsAssociationCircuitTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 23, 1, 2),
    _CircuitOmsAssociationCircuitTrailId_Type()
)
circuitOmsAssociationCircuitTrailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOmsAssociationCircuitTrailId.setStatus("current")


class _CircuitOmsAssociationOmsTrailId_Type(Integer32):
    """Custom type circuitOmsAssociationOmsTrailId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CircuitOmsAssociationOmsTrailId_Type.__name__ = "Integer32"
_CircuitOmsAssociationOmsTrailId_Object = MibTableColumn
circuitOmsAssociationOmsTrailId = _CircuitOmsAssociationOmsTrailId_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 23, 1, 3),
    _CircuitOmsAssociationOmsTrailId_Type()
)
circuitOmsAssociationOmsTrailId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitOmsAssociationOmsTrailId.setStatus("current")
_CircuitOmsAssociationRowStatus_Type = RowStatus
_CircuitOmsAssociationRowStatus_Object = MibTableColumn
circuitOmsAssociationRowStatus = _CircuitOmsAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 23, 1, 4),
    _CircuitOmsAssociationRowStatus_Type()
)
circuitOmsAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    circuitOmsAssociationRowStatus.setStatus("current")
_AlarmsNotificationBoardPart_Type = OctetString
_AlarmsNotificationBoardPart_Object = MibScalar
alarmsNotificationBoardPart = _AlarmsNotificationBoardPart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 24, 1),
    _AlarmsNotificationBoardPart_Type()
)
alarmsNotificationBoardPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsNotificationBoardPart.setStatus("current")
_AlarmsNotificationBoardSerial_Type = OctetString
_AlarmsNotificationBoardSerial_Object = MibScalar
alarmsNotificationBoardSerial = _AlarmsNotificationBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 24, 2),
    _AlarmsNotificationBoardSerial_Type()
)
alarmsNotificationBoardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsNotificationBoardSerial.setStatus("current")
_AlarmsNotificationBoardName_Type = OctetString
_AlarmsNotificationBoardName_Object = MibScalar
alarmsNotificationBoardName = _AlarmsNotificationBoardName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 24, 3),
    _AlarmsNotificationBoardName_Type()
)
alarmsNotificationBoardName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsNotificationBoardName.setStatus("current")
_AlarmsNotificationNeName_Type = OctetString
_AlarmsNotificationNeName_Object = MibScalar
alarmsNotificationNeName = _AlarmsNotificationNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 24, 4),
    _AlarmsNotificationNeName_Type()
)
alarmsNotificationNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmsNotificationNeName.setStatus("current")
_StatusAgente_Type = OctetString
_StatusAgente_Object = MibScalar
statusAgente = _StatusAgente_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 25, 1),
    _StatusAgente_Type()
)
statusAgente.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAgente.setStatus("current")
_UptimeAgente_Type = OctetString
_UptimeAgente_Object = MibScalar
uptimeAgente = _UptimeAgente_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 25, 2),
    _UptimeAgente_Type()
)
uptimeAgente.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptimeAgente.setStatus("current")
_BoardPerformanceTable_Object = MibTable
boardPerformanceTable = _BoardPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26)
)
if mibBuilder.loadTexts:
    boardPerformanceTable.setStatus("current")
_BoardPerformanceEntry_Object = MibTableRow
boardPerformanceEntry = _BoardPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1)
)
boardPerformanceEntry.setIndexNames(
    (0, "METROPAD3", "boardPerformanceBoardPart"),
    (0, "METROPAD3", "boardPerformanceBoardSerial"),
    (0, "METROPAD3", "boardPerformanceType"),
    (0, "METROPAD3", "boardPerformancePortNumber"),
    (0, "METROPAD3", "boardPerformancePortType"),
)
if mibBuilder.loadTexts:
    boardPerformanceEntry.setStatus("current")


class _BoardPerformanceBoardPart_Type(Integer32):
    """Custom type boardPerformanceBoardPart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardPerformanceBoardPart_Type.__name__ = "Integer32"
_BoardPerformanceBoardPart_Object = MibTableColumn
boardPerformanceBoardPart = _BoardPerformanceBoardPart_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 1),
    _BoardPerformanceBoardPart_Type()
)
boardPerformanceBoardPart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardPerformanceBoardPart.setStatus("current")


class _BoardPerformanceBoardSerial_Type(Integer32):
    """Custom type boardPerformanceBoardSerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardPerformanceBoardSerial_Type.__name__ = "Integer32"
_BoardPerformanceBoardSerial_Object = MibTableColumn
boardPerformanceBoardSerial = _BoardPerformanceBoardSerial_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 2),
    _BoardPerformanceBoardSerial_Type()
)
boardPerformanceBoardSerial.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardPerformanceBoardSerial.setStatus("current")


class _BoardPerformanceType_Type(Integer32):
    """Custom type boardPerformanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardPerformanceType_Type.__name__ = "Integer32"
_BoardPerformanceType_Object = MibTableColumn
boardPerformanceType = _BoardPerformanceType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 3),
    _BoardPerformanceType_Type()
)
boardPerformanceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardPerformanceType.setStatus("current")


class _BoardPerformancePortNumber_Type(Integer32):
    """Custom type boardPerformancePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BoardPerformancePortNumber_Type.__name__ = "Integer32"
_BoardPerformancePortNumber_Object = MibTableColumn
boardPerformancePortNumber = _BoardPerformancePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 4),
    _BoardPerformancePortNumber_Type()
)
boardPerformancePortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardPerformancePortNumber.setStatus("current")


class _BoardPerformancePortType_Type(Integer32):
    """Custom type boardPerformancePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("wdm", 2))
    )


_BoardPerformancePortType_Type.__name__ = "Integer32"
_BoardPerformancePortType_Object = MibTableColumn
boardPerformancePortType = _BoardPerformancePortType_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 5),
    _BoardPerformancePortType_Type()
)
boardPerformancePortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    boardPerformancePortType.setStatus("current")
_BoardPerformanceValue_Type = Integer32
_BoardPerformanceValue_Object = MibTableColumn
boardPerformanceValue = _BoardPerformanceValue_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 6),
    _BoardPerformanceValue_Type()
)
boardPerformanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPerformanceValue.setStatus("current")
_BoardPerformanceRate_Type = OctetString
_BoardPerformanceRate_Object = MibTableColumn
boardPerformanceRate = _BoardPerformanceRate_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 7),
    _BoardPerformanceRate_Type()
)
boardPerformanceRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPerformanceRate.setStatus("current")
_BoardPerformanceTime_Type = DateAndTime
_BoardPerformanceTime_Object = MibTableColumn
boardPerformanceTime = _BoardPerformanceTime_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 8),
    _BoardPerformanceTime_Type()
)
boardPerformanceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPerformanceTime.setStatus("current")
_BoardPerformanceNeName_Type = OctetString
_BoardPerformanceNeName_Object = MibTableColumn
boardPerformanceNeName = _BoardPerformanceNeName_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 9),
    _BoardPerformanceNeName_Type()
)
boardPerformanceNeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPerformanceNeName.setStatus("current")
_BoardPerformanceNeMap_Type = OctetString
_BoardPerformanceNeMap_Object = MibTableColumn
boardPerformanceNeMap = _BoardPerformanceNeMap_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 10),
    _BoardPerformanceNeMap_Type()
)
boardPerformanceNeMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    boardPerformanceNeMap.setStatus("current")
_BoardPerformanceRowStatus_Type = RowStatus
_BoardPerformanceRowStatus_Object = MibTableColumn
boardPerformanceRowStatus = _BoardPerformanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 14846, 3, 26, 1, 11),
    _BoardPerformanceRowStatus_Type()
)
boardPerformanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    boardPerformanceRowStatus.setStatus("current")

# Managed Objects groups

lightpadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 2)
)
lightpadGroup.setObjects(
      *(("METROPAD3", "uptimeAgente"),
        ("METROPAD3", "statusAgente"),
        ("METROPAD3", "neRowStatus"),
        ("METROPAD3", "neMap"),
        ("METROPAD3", "neNetwork"),
        ("METROPAD3", "neName"))
)
if mibBuilder.loadTexts:
    lightpadGroup.setStatus("current")

boardPerformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 3)
)
boardPerformanceGroup.setObjects(
      *(("METROPAD3", "boardPerformanceRowStatus"),
        ("METROPAD3", "boardPerformanceNeMap"),
        ("METROPAD3", "boardPerformanceNeName"),
        ("METROPAD3", "boardPerformanceTime"),
        ("METROPAD3", "boardPerformanceRate"),
        ("METROPAD3", "boardPerformanceValue"))
)
if mibBuilder.loadTexts:
    boardPerformanceGroup.setStatus("current")

circuitOmsAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 4)
)
circuitOmsAssociationGroup.setObjects(
      *(("METROPAD3", "circuitOmsAssociationRowStatus"),
        ("METROPAD3", "circuitOmsAssociationOmsTrailId"),
        ("METROPAD3", "circuitOmsAssociationCircuitTrailId"))
)
if mibBuilder.loadTexts:
    circuitOmsAssociationGroup.setStatus("current")

omsOtsAssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 5)
)
omsOtsAssociationGroup.setObjects(
      *(("METROPAD3", "omsOtsAssociationRowStatus"),
        ("METROPAD3", "omsOtsAssociationOmsTrailId"),
        ("METROPAD3", "omsOtsAssociationOtsTrailId"))
)
if mibBuilder.loadTexts:
    omsOtsAssociationGroup.setStatus("current")

networkEventLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 6)
)
networkEventLogGroup.setObjects(
      *(("METROPAD3", "networkEventLogRowStatus"),
        ("METROPAD3", "networkEventLogAction"),
        ("METROPAD3", "networkEventLogResourceName"),
        ("METROPAD3", "networkEventLogResourceType"),
        ("METROPAD3", "networkEventLogTime"))
)
if mibBuilder.loadTexts:
    networkEventLogGroup.setStatus("current")

serverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 7)
)
serverGroup.setObjects(
      *(("METROPAD3", "serverSync"),
        ("METROPAD3", "serverFreeDiskSpace"),
        ("METROPAD3", "serverSo"),
        ("METROPAD3", "serverUpTime"),
        ("METROPAD3", "serverBuild"),
        ("METROPAD3", "serverVersion"),
        ("METROPAD3", "serverIsActive"),
        ("METROPAD3", "serverSlaveIp"),
        ("METROPAD3", "serverMasterIp"))
)
if mibBuilder.loadTexts:
    serverGroup.setStatus("current")

circuitTrailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 8)
)
circuitTrailGroup.setObjects(
      *(("METROPAD3", "circuitTrailRowStatus"),
        ("METROPAD3", "circuitTrailDatabaseId"),
        ("METROPAD3", "circuitTrailDestinationPort"),
        ("METROPAD3", "circuitTrailDestinationBoard"),
        ("METROPAD3", "circuitTrailDestinationNE"),
        ("METROPAD3", "circuitTrailDestinationNetwork"),
        ("METROPAD3", "circuitTrailSourcePort"),
        ("METROPAD3", "circuitTrailSourceBoard"),
        ("METROPAD3", "circuitTrailSourceNE"),
        ("METROPAD3", "circuitTrailSourceNetwork"),
        ("METROPAD3", "circuitTrailService"),
        ("METROPAD3", "circuitTrailClientId"),
        ("METROPAD3", "circuitTrailClientName"),
        ("METROPAD3", "circuitTrailDescription"),
        ("METROPAD3", "circuitTrailName"))
)
if mibBuilder.loadTexts:
    circuitTrailGroup.setStatus("current")

omsTrailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 9)
)
omsTrailGroup.setObjects(
      *(("METROPAD3", "omsTrailRowStatus"),
        ("METROPAD3", "omsTrailDatabaseId"),
        ("METROPAD3", "omsTrailDestinationPort"),
        ("METROPAD3", "omsTrailDestinationBoard"),
        ("METROPAD3", "omsTrailDestinationNE"),
        ("METROPAD3", "omsTrailSourcePort"),
        ("METROPAD3", "omsTrailSourceBoard"),
        ("METROPAD3", "omsTrailSourceNE"),
        ("METROPAD3", "omsTrailDescription"),
        ("METROPAD3", "omsTrailName"))
)
if mibBuilder.loadTexts:
    omsTrailGroup.setStatus("current")

otsTrailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 10)
)
otsTrailGroup.setObjects(
      *(("METROPAD3", "otsTrailRowStatus"),
        ("METROPAD3", "otsTrailDatabaseId"),
        ("METROPAD3", "otsTrailDestinationPort"),
        ("METROPAD3", "otsTrailDestinationBoard"),
        ("METROPAD3", "otsTrailDestinationNE"),
        ("METROPAD3", "otsTrailSourcePort"),
        ("METROPAD3", "otsTrailSourceBoard"),
        ("METROPAD3", "otsTrailSourceNE"),
        ("METROPAD3", "otsTrailDistance"),
        ("METROPAD3", "otsTrailFiberType"),
        ("METROPAD3", "otsTrailDescription"),
        ("METROPAD3", "otsTrailName"))
)
if mibBuilder.loadTexts:
    otsTrailGroup.setStatus("current")

networkAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 11)
)
networkAlarmObjectGroup.setObjects(
      *(("METROPAD3", "networkAlarmRowStatus"),
        ("METROPAD3", "networkAlarmAckUser"),
        ("METROPAD3", "networkAlarmAckDate"),
        ("METROPAD3", "networkAlarmAck"),
        ("METROPAD3", "networkAlarmPortNameDestination"),
        ("METROPAD3", "networkAlarmBoardNameDestination"),
        ("METROPAD3", "networkAlarmNeNameDestination"),
        ("METROPAD3", "networkAlarmPortNameSource"),
        ("METROPAD3", "networkAlarmBoardNameSource"),
        ("METROPAD3", "networkAlarmNeNameSource"),
        ("METROPAD3", "networkAlarmType"),
        ("METROPAD3", "networkAlarmName"),
        ("METROPAD3", "networkAlarmBoardName"),
        ("METROPAD3", "networkAlarmNeName"),
        ("METROPAD3", "networkAlarmLayer"),
        ("METROPAD3", "networkAlarmResource"),
        ("METROPAD3", "networkAlarmNetworkName"),
        ("METROPAD3", "networkAlarmEnd"),
        ("METROPAD3", "networkAlarmStart"),
        ("METROPAD3", "networkAlarmGroup"),
        ("METROPAD3", "networkAlarmKey"),
        ("METROPAD3", "networkAlarmSeverity"))
)
if mibBuilder.loadTexts:
    networkAlarmObjectGroup.setStatus("current")

alarmsNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 12)
)
alarmsNotificationGroup.setObjects(
      *(("METROPAD3", "alarmsNotificationNeName"),
        ("METROPAD3", "alarmsNotificationBoardName"),
        ("METROPAD3", "alarmsNotificationBoardSerial"),
        ("METROPAD3", "alarmsNotificationBoardPart"))
)
if mibBuilder.loadTexts:
    alarmsNotificationGroup.setStatus("current")

performanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 13)
)
performanceGroup.setObjects(
      *(("METROPAD3", "performanceRowStatus"),
        ("METROPAD3", "performanceOid"),
        ("METROPAD3", "performanceNeMap"),
        ("METROPAD3", "performanceNeName"),
        ("METROPAD3", "performanceTime"),
        ("METROPAD3", "performanceRate"),
        ("METROPAD3", "performanceValue"),
        ("METROPAD3", "performancePortNumber"),
        ("METROPAD3", "performancePortType"),
        ("METROPAD3", "performanceType"),
        ("METROPAD3", "performanceBoardSerial"),
        ("METROPAD3", "performanceBoardPart"))
)
if mibBuilder.loadTexts:
    performanceGroup.setStatus("current")

eventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 14)
)
eventGroup.setObjects(
      *(("METROPAD3", "eventRowStatus"),
        ("METROPAD3", "eventNeMap"),
        ("METROPAD3", "eventNeName"),
        ("METROPAD3", "eventTime"),
        ("METROPAD3", "eventBoardSlot"),
        ("METROPAD3", "eventBoardSubRack"),
        ("METROPAD3", "eventBoardRackPosition"),
        ("METROPAD3", "eventBoardSerial"),
        ("METROPAD3", "eventBoardPart"),
        ("METROPAD3", "eventName"),
        ("METROPAD3", "eventType"))
)
if mibBuilder.loadTexts:
    eventGroup.setStatus("current")

alarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 15)
)
alarmGroup.setObjects(
      *(("METROPAD3", "alarmRowStatus"),
        ("METROPAD3", "alarmNeMap"),
        ("METROPAD3", "alarmNeName"),
        ("METROPAD3", "alarmAckUser"),
        ("METROPAD3", "alarmAckDescription"),
        ("METROPAD3", "alarmAckDate"),
        ("METROPAD3", "alarmEnd"),
        ("METROPAD3", "alarmStart"),
        ("METROPAD3", "alarmBoardSlot"),
        ("METROPAD3", "alarmBoardSubRack"),
        ("METROPAD3", "alarmResource"),
        ("METROPAD3", "alarmBoardRackPosition"),
        ("METROPAD3", "alarmBoardSerial"),
        ("METROPAD3", "alarmBoardPart"),
        ("METROPAD3", "alarmName"),
        ("METROPAD3", "alarmSeverity"),
        ("METROPAD3", "alarmType"),
        ("METROPAD3", "alarmId"))
)
if mibBuilder.loadTexts:
    alarmGroup.setStatus("current")

boardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 16)
)
boardGroup.setObjects(
      *(("METROPAD3", "boardRowStatus"),
        ("METROPAD3", "boardState"),
        ("METROPAD3", "boardNeMap"),
        ("METROPAD3", "boardNeName"),
        ("METROPAD3", "boardVersion"),
        ("METROPAD3", "boardSlot"),
        ("METROPAD3", "boardSubRack"),
        ("METROPAD3", "boardRackPosition"),
        ("METROPAD3", "boardDescription"),
        ("METROPAD3", "boardName"),
        ("METROPAD3", "boardModel"),
        ("METROPAD3", "boardSerial"),
        ("METROPAD3", "boardPart"))
)
if mibBuilder.loadTexts:
    boardGroup.setStatus("current")


# Notification objects

alarmStartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 7)
)
alarmStartNotification.setObjects(
      *(("METROPAD3", "alarmName"),
        ("METROPAD3", "alarmBoardPart"),
        ("METROPAD3", "alarmBoardSerial"),
        ("METROPAD3", "alarmBoardRackPosition"),
        ("METROPAD3", "alarmBoardSlot"),
        ("METROPAD3", "alarmBoardSubRack"),
        ("METROPAD3", "alarmNeName"),
        ("METROPAD3", "alarmNeMap"),
        ("METROPAD3", "alarmType"),
        ("METROPAD3", "alarmSeverity"),
        ("METROPAD3", "alarmStart"),
        ("METROPAD3", "alarmRowStatus"),
        ("METROPAD3", "boardModel"),
        ("METROPAD3", "alarmId"))
)
if mibBuilder.loadTexts:
    alarmStartNotification.setStatus(
        "current"
    )

alarmEndNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 8)
)
alarmEndNotification.setObjects(
      *(("METROPAD3", "alarmName"),
        ("METROPAD3", "alarmBoardPart"),
        ("METROPAD3", "alarmBoardSerial"),
        ("METROPAD3", "alarmBoardRackPosition"),
        ("METROPAD3", "alarmBoardSlot"),
        ("METROPAD3", "alarmBoardSubRack"),
        ("METROPAD3", "alarmNeName"),
        ("METROPAD3", "alarmNeMap"),
        ("METROPAD3", "alarmType"),
        ("METROPAD3", "alarmSeverity"),
        ("METROPAD3", "alarmEnd"),
        ("METROPAD3", "alarmRowStatus"),
        ("METROPAD3", "boardModel"),
        ("METROPAD3", "alarmId"))
)
if mibBuilder.loadTexts:
    alarmEndNotification.setStatus(
        "current"
    )

alarmAckNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 9)
)
alarmAckNotification.setObjects(
      *(("METROPAD3", "alarmName"),
        ("METROPAD3", "alarmBoardPart"),
        ("METROPAD3", "alarmBoardSerial"),
        ("METROPAD3", "alarmBoardRackPosition"),
        ("METROPAD3", "alarmBoardSlot"),
        ("METROPAD3", "alarmBoardSubRack"),
        ("METROPAD3", "alarmNeName"),
        ("METROPAD3", "alarmNeMap"),
        ("METROPAD3", "alarmType"),
        ("METROPAD3", "alarmSeverity"),
        ("METROPAD3", "alarmStart"),
        ("METROPAD3", "alarmEnd"),
        ("METROPAD3", "alarmAckDate"),
        ("METROPAD3", "alarmAckUser"),
        ("METROPAD3", "alarmAckDescription"),
        ("METROPAD3", "alarmRowStatus"),
        ("METROPAD3", "boardModel"),
        ("METROPAD3", "alarmId"))
)
if mibBuilder.loadTexts:
    alarmAckNotification.setStatus(
        "current"
    )

eventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 10)
)
eventNotification.setObjects(
      *(("METROPAD3", "eventName"),
        ("METROPAD3", "eventBoardPart"),
        ("METROPAD3", "eventBoardSerial"),
        ("METROPAD3", "eventBoardRackPosition"),
        ("METROPAD3", "eventBoardSlot"),
        ("METROPAD3", "eventBoardSubRack"),
        ("METROPAD3", "eventNeName"),
        ("METROPAD3", "eventNeMap"),
        ("METROPAD3", "eventType"),
        ("METROPAD3", "eventTime"),
        ("METROPAD3", "eventRowStatus"),
        ("METROPAD3", "boardModel"))
)
if mibBuilder.loadTexts:
    eventNotification.setStatus(
        "current"
    )

isAliveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 11)
)
if mibBuilder.loadTexts:
    isAliveNotification.setStatus(
        "current"
    )

networkAlarmStartNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 16)
)
networkAlarmStartNotification.setObjects(
      *(("METROPAD3", "networkAlarmSeverity"),
        ("METROPAD3", "networkAlarmKey"),
        ("METROPAD3", "networkAlarmGroup"),
        ("METROPAD3", "networkAlarmStart"),
        ("METROPAD3", "networkAlarmNetworkName"),
        ("METROPAD3", "networkAlarmResource"),
        ("METROPAD3", "networkAlarmLayer"),
        ("METROPAD3", "networkAlarmNeName"),
        ("METROPAD3", "networkAlarmBoardName"),
        ("METROPAD3", "networkAlarmName"),
        ("METROPAD3", "networkAlarmType"),
        ("METROPAD3", "networkAlarmNeNameSource"),
        ("METROPAD3", "networkAlarmBoardNameSource"),
        ("METROPAD3", "networkAlarmPortNameSource"),
        ("METROPAD3", "networkAlarmNeNameDestination"),
        ("METROPAD3", "networkAlarmBoardNameDestination"),
        ("METROPAD3", "networkAlarmPortNameDestination"),
        ("METROPAD3", "networkAlarmAck"))
)
if mibBuilder.loadTexts:
    networkAlarmStartNotification.setStatus(
        "current"
    )

networkAlarmEndNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 17)
)
networkAlarmEndNotification.setObjects(
      *(("METROPAD3", "networkAlarmSeverity"),
        ("METROPAD3", "networkAlarmKey"),
        ("METROPAD3", "networkAlarmGroup"),
        ("METROPAD3", "networkAlarmStart"),
        ("METROPAD3", "networkAlarmEnd"),
        ("METROPAD3", "networkAlarmNetworkName"),
        ("METROPAD3", "networkAlarmResource"),
        ("METROPAD3", "networkAlarmLayer"),
        ("METROPAD3", "networkAlarmNeName"),
        ("METROPAD3", "networkAlarmBoardName"),
        ("METROPAD3", "networkAlarmName"),
        ("METROPAD3", "networkAlarmType"),
        ("METROPAD3", "networkAlarmNeNameSource"),
        ("METROPAD3", "networkAlarmBoardNameSource"),
        ("METROPAD3", "networkAlarmPortNameSource"),
        ("METROPAD3", "networkAlarmNeNameDestination"),
        ("METROPAD3", "networkAlarmBoardNameDestination"),
        ("METROPAD3", "networkAlarmPortNameDestination"),
        ("METROPAD3", "networkAlarmAck"))
)
if mibBuilder.loadTexts:
    networkAlarmEndNotification.setStatus(
        "current"
    )

networkAlarmAckNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 18)
)
networkAlarmAckNotification.setObjects(
      *(("METROPAD3", "networkAlarmSeverity"),
        ("METROPAD3", "networkAlarmKey"),
        ("METROPAD3", "networkAlarmGroup"),
        ("METROPAD3", "networkAlarmStart"),
        ("METROPAD3", "networkAlarmEnd"),
        ("METROPAD3", "networkAlarmNetworkName"),
        ("METROPAD3", "networkAlarmResource"),
        ("METROPAD3", "networkAlarmLayer"),
        ("METROPAD3", "networkAlarmNeName"),
        ("METROPAD3", "networkAlarmBoardName"),
        ("METROPAD3", "networkAlarmName"),
        ("METROPAD3", "networkAlarmType"),
        ("METROPAD3", "networkAlarmAck"),
        ("METROPAD3", "networkAlarmAckDate"),
        ("METROPAD3", "networkAlarmAckUser"))
)
if mibBuilder.loadTexts:
    networkAlarmAckNotification.setStatus(
        "current"
    )

networkEventLogNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 20)
)
networkEventLogNotification.setObjects(
      *(("METROPAD3", "networkEventLogTime"),
        ("METROPAD3", "networkEventLogResourceType"),
        ("METROPAD3", "networkEventLogResourceName"),
        ("METROPAD3", "networkEventLogAction"),
        ("METROPAD3", "networkEventLogRowStatus"))
)
if mibBuilder.loadTexts:
    networkEventLogNotification.setStatus(
        "current"
    )

networkAlarmChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 21)
)
networkAlarmChangeNotification.setObjects(
      *(("METROPAD3", "networkAlarmSeverity"),
        ("METROPAD3", "networkAlarmKey"),
        ("METROPAD3", "networkAlarmGroup"),
        ("METROPAD3", "networkAlarmStart"),
        ("METROPAD3", "networkAlarmNetworkName"),
        ("METROPAD3", "networkAlarmResource"),
        ("METROPAD3", "networkAlarmLayer"),
        ("METROPAD3", "networkAlarmNeName"),
        ("METROPAD3", "networkAlarmBoardName"),
        ("METROPAD3", "networkAlarmName"),
        ("METROPAD3", "networkAlarmType"),
        ("METROPAD3", "networkAlarmNeNameSource"),
        ("METROPAD3", "networkAlarmBoardNameSource"),
        ("METROPAD3", "networkAlarmPortNameSource"),
        ("METROPAD3", "networkAlarmNeNameDestination"),
        ("METROPAD3", "networkAlarmBoardNameDestination"),
        ("METROPAD3", "networkAlarmPortNameDestination"),
        ("METROPAD3", "networkAlarmAck"))
)
if mibBuilder.loadTexts:
    networkAlarmChangeNotification.setStatus(
        "current"
    )

isRecreateAlarmsNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 24)
)
isRecreateAlarmsNotification.setObjects(
      *(("METROPAD3", "alarmsNotificationBoardPart"),
        ("METROPAD3", "alarmsNotificationBoardSerial"),
        ("METROPAD3", "alarmsNotificationBoardName"),
        ("METROPAD3", "alarmsNotificationNeName"))
)
if mibBuilder.loadTexts:
    isRecreateAlarmsNotification.setStatus(
        "current"
    )

isStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 14846, 3, 25)
)
isStatusNotification.setObjects(
      *(("METROPAD3", "statusAgente"),
        ("METROPAD3", "uptimeAgente"))
)
if mibBuilder.loadTexts:
    isStatusNotification.setStatus(
        "current"
    )


# Notifications groups

lightpadNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1, 1, 1)
)
lightpadNotificationsGroup.setObjects(
      *(("METROPAD3", "networkAlarmChangeNotification"),
        ("METROPAD3", "networkEventLogNotification"),
        ("METROPAD3", "networkAlarmAckNotification"),
        ("METROPAD3", "networkAlarmEndNotification"),
        ("METROPAD3", "networkAlarmStartNotification"),
        ("METROPAD3", "isStatusNotification"),
        ("METROPAD3", "isRecreateAlarmsNotification"),
        ("METROPAD3", "isAliveNotification"),
        ("METROPAD3", "eventNotification"),
        ("METROPAD3", "alarmEndNotification"),
        ("METROPAD3", "alarmStartNotification"),
        ("METROPAD3", "alarmAckNotification"))
)
if mibBuilder.loadTexts:
    lightpadNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "METROPAD3",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "moduleIdentity": moduleIdentity,
       "lightpadMIBGroups": lightpadMIBGroups,
       "lightpadNotificationsGroup": lightpadNotificationsGroup,
       "lightpadGroup": lightpadGroup,
       "boardPerformanceGroup": boardPerformanceGroup,
       "circuitOmsAssociationGroup": circuitOmsAssociationGroup,
       "omsOtsAssociationGroup": omsOtsAssociationGroup,
       "networkEventLogGroup": networkEventLogGroup,
       "serverGroup": serverGroup,
       "circuitTrailGroup": circuitTrailGroup,
       "omsTrailGroup": omsTrailGroup,
       "otsTrailGroup": otsTrailGroup,
       "networkAlarmObjectGroup": networkAlarmObjectGroup,
       "alarmsNotificationGroup": alarmsNotificationGroup,
       "performanceGroup": performanceGroup,
       "eventGroup": eventGroup,
       "alarmGroup": alarmGroup,
       "boardGroup": boardGroup,
       "padtec": padtec,
       "metropad3": metropad3,
       "neTable": neTable,
       "neEntry": neEntry,
       "neId": neId,
       "neName": neName,
       "neNetwork": neNetwork,
       "neMap": neMap,
       "neRowStatus": neRowStatus,
       "boardTable": boardTable,
       "boardEntry": boardEntry,
       "boardId": boardId,
       "boardPart": boardPart,
       "boardSerial": boardSerial,
       "boardModel": boardModel,
       "boardName": boardName,
       "boardDescription": boardDescription,
       "boardSubRack": boardSubRack,
       "boardSlot": boardSlot,
       "boardVersion": boardVersion,
       "boardNeName": boardNeName,
       "boardNeMap": boardNeMap,
       "boardState": boardState,
       "boardRowStatus": boardRowStatus,
       "boardRackPosition": boardRackPosition,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmId": alarmId,
       "alarmType": alarmType,
       "alarmSeverity": alarmSeverity,
       "alarmName": alarmName,
       "alarmBoardPart": alarmBoardPart,
       "alarmBoardSerial": alarmBoardSerial,
       "alarmBoardSubRack": alarmBoardSubRack,
       "alarmBoardSlot": alarmBoardSlot,
       "alarmStart": alarmStart,
       "alarmEnd": alarmEnd,
       "alarmAckDate": alarmAckDate,
       "alarmAckDescription": alarmAckDescription,
       "alarmAckUser": alarmAckUser,
       "alarmNeName": alarmNeName,
       "alarmNeMap": alarmNeMap,
       "alarmRowStatus": alarmRowStatus,
       "alarmBoardRackPosition": alarmBoardRackPosition,
       "alarmResource": alarmResource,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventId": eventId,
       "eventType": eventType,
       "eventName": eventName,
       "eventBoardPart": eventBoardPart,
       "eventBoardSerial": eventBoardSerial,
       "eventBoardSubRack": eventBoardSubRack,
       "eventBoardSlot": eventBoardSlot,
       "eventTime": eventTime,
       "eventNeName": eventNeName,
       "eventNeMap": eventNeMap,
       "eventRowStatus": eventRowStatus,
       "eventBoardRackPosition": eventBoardRackPosition,
       "performanceTable": performanceTable,
       "performanceEntry": performanceEntry,
       "performanceId": performanceId,
       "performanceBoardPart": performanceBoardPart,
       "performanceBoardSerial": performanceBoardSerial,
       "performanceType": performanceType,
       "performancePortType": performancePortType,
       "performancePortNumber": performancePortNumber,
       "performanceValue": performanceValue,
       "performanceRate": performanceRate,
       "performanceTime": performanceTime,
       "performanceNeName": performanceNeName,
       "performanceNeMap": performanceNeMap,
       "performanceRowStatus": performanceRowStatus,
       "performanceOid": performanceOid,
       "serverStatus": serverStatus,
       "serverMasterIp": serverMasterIp,
       "serverSlaveIp": serverSlaveIp,
       "serverIsActive": serverIsActive,
       "serverVersion": serverVersion,
       "serverBuild": serverBuild,
       "serverUpTime": serverUpTime,
       "serverSo": serverSo,
       "serverFreeDiskSpace": serverFreeDiskSpace,
       "serverSync": serverSync,
       "alarmStartNotification": alarmStartNotification,
       "alarmEndNotification": alarmEndNotification,
       "alarmAckNotification": alarmAckNotification,
       "eventNotification": eventNotification,
       "isAliveNotification": isAliveNotification,
       "networkAlarmTable": networkAlarmTable,
       "networkAlarmEntry": networkAlarmEntry,
       "networkAlarmId": networkAlarmId,
       "networkAlarmSeverity": networkAlarmSeverity,
       "networkAlarmKey": networkAlarmKey,
       "networkAlarmGroup": networkAlarmGroup,
       "networkAlarmStart": networkAlarmStart,
       "networkAlarmEnd": networkAlarmEnd,
       "networkAlarmNetworkName": networkAlarmNetworkName,
       "networkAlarmResource": networkAlarmResource,
       "networkAlarmLayer": networkAlarmLayer,
       "networkAlarmNeName": networkAlarmNeName,
       "networkAlarmBoardName": networkAlarmBoardName,
       "networkAlarmName": networkAlarmName,
       "networkAlarmType": networkAlarmType,
       "networkAlarmNeNameSource": networkAlarmNeNameSource,
       "networkAlarmBoardNameSource": networkAlarmBoardNameSource,
       "networkAlarmPortNameSource": networkAlarmPortNameSource,
       "networkAlarmNeNameDestination": networkAlarmNeNameDestination,
       "networkAlarmBoardNameDestination": networkAlarmBoardNameDestination,
       "networkAlarmPortNameDestination": networkAlarmPortNameDestination,
       "networkAlarmAck": networkAlarmAck,
       "networkAlarmAckDate": networkAlarmAckDate,
       "networkAlarmAckUser": networkAlarmAckUser,
       "networkAlarmRowStatus": networkAlarmRowStatus,
       "otsTrailTable": otsTrailTable,
       "otsTrailEntry": otsTrailEntry,
       "otsTrailId": otsTrailId,
       "otsTrailName": otsTrailName,
       "otsTrailDescription": otsTrailDescription,
       "otsTrailFiberType": otsTrailFiberType,
       "otsTrailDistance": otsTrailDistance,
       "otsTrailSourceNE": otsTrailSourceNE,
       "otsTrailSourceBoard": otsTrailSourceBoard,
       "otsTrailSourcePort": otsTrailSourcePort,
       "otsTrailDestinationNE": otsTrailDestinationNE,
       "otsTrailDestinationBoard": otsTrailDestinationBoard,
       "otsTrailDestinationPort": otsTrailDestinationPort,
       "otsTrailDatabaseId": otsTrailDatabaseId,
       "otsTrailRowStatus": otsTrailRowStatus,
       "omsTrailTable": omsTrailTable,
       "omsTrailEntry": omsTrailEntry,
       "omsTrailId": omsTrailId,
       "omsTrailName": omsTrailName,
       "omsTrailDescription": omsTrailDescription,
       "omsTrailSourceNE": omsTrailSourceNE,
       "omsTrailSourceBoard": omsTrailSourceBoard,
       "omsTrailSourcePort": omsTrailSourcePort,
       "omsTrailDestinationNE": omsTrailDestinationNE,
       "omsTrailDestinationBoard": omsTrailDestinationBoard,
       "omsTrailDestinationPort": omsTrailDestinationPort,
       "omsTrailDatabaseId": omsTrailDatabaseId,
       "omsTrailRowStatus": omsTrailRowStatus,
       "circuitTrailTable": circuitTrailTable,
       "circuitTrailEntry": circuitTrailEntry,
       "circuitTrailId": circuitTrailId,
       "circuitTrailName": circuitTrailName,
       "circuitTrailDescription": circuitTrailDescription,
       "circuitTrailClientName": circuitTrailClientName,
       "circuitTrailClientId": circuitTrailClientId,
       "circuitTrailService": circuitTrailService,
       "circuitTrailSourceNetwork": circuitTrailSourceNetwork,
       "circuitTrailSourceNE": circuitTrailSourceNE,
       "circuitTrailSourceBoard": circuitTrailSourceBoard,
       "circuitTrailSourcePort": circuitTrailSourcePort,
       "circuitTrailDestinationNetwork": circuitTrailDestinationNetwork,
       "circuitTrailDestinationNE": circuitTrailDestinationNE,
       "circuitTrailDestinationBoard": circuitTrailDestinationBoard,
       "circuitTrailDestinationPort": circuitTrailDestinationPort,
       "circuitTrailDatabaseId": circuitTrailDatabaseId,
       "circuitTrailRowStatus": circuitTrailRowStatus,
       "networkAlarmStartNotification": networkAlarmStartNotification,
       "networkAlarmEndNotification": networkAlarmEndNotification,
       "networkAlarmAckNotification": networkAlarmAckNotification,
       "networkEventLogTable": networkEventLogTable,
       "networkEventLogEntry": networkEventLogEntry,
       "networkEventLogId": networkEventLogId,
       "networkEventLogTime": networkEventLogTime,
       "networkEventLogResourceType": networkEventLogResourceType,
       "networkEventLogResourceName": networkEventLogResourceName,
       "networkEventLogAction": networkEventLogAction,
       "networkEventLogRowStatus": networkEventLogRowStatus,
       "networkEventLogNotification": networkEventLogNotification,
       "networkAlarmChangeNotification": networkAlarmChangeNotification,
       "trailAssociationTable": trailAssociationTable,
       "trailAssociationEntry": trailAssociationEntry,
       "omsOtsAssociationTrailIdIndex": omsOtsAssociationTrailIdIndex,
       "omsOtsAssociationOtsTrailId": omsOtsAssociationOtsTrailId,
       "omsOtsAssociationOmsTrailId": omsOtsAssociationOmsTrailId,
       "omsOtsAssociationRowStatus": omsOtsAssociationRowStatus,
       "circuitAssociationOmsTable": circuitAssociationOmsTable,
       "circuitAssociationOmsEntry": circuitAssociationOmsEntry,
       "circuitOmsAssociationTrailIdIndex": circuitOmsAssociationTrailIdIndex,
       "circuitOmsAssociationCircuitTrailId": circuitOmsAssociationCircuitTrailId,
       "circuitOmsAssociationOmsTrailId": circuitOmsAssociationOmsTrailId,
       "circuitOmsAssociationRowStatus": circuitOmsAssociationRowStatus,
       "isRecreateAlarmsNotification": isRecreateAlarmsNotification,
       "alarmsNotificationBoardPart": alarmsNotificationBoardPart,
       "alarmsNotificationBoardSerial": alarmsNotificationBoardSerial,
       "alarmsNotificationBoardName": alarmsNotificationBoardName,
       "alarmsNotificationNeName": alarmsNotificationNeName,
       "isStatusNotification": isStatusNotification,
       "statusAgente": statusAgente,
       "uptimeAgente": uptimeAgente,
       "boardPerformanceTable": boardPerformanceTable,
       "boardPerformanceEntry": boardPerformanceEntry,
       "boardPerformanceBoardPart": boardPerformanceBoardPart,
       "boardPerformanceBoardSerial": boardPerformanceBoardSerial,
       "boardPerformanceType": boardPerformanceType,
       "boardPerformancePortNumber": boardPerformancePortNumber,
       "boardPerformancePortType": boardPerformancePortType,
       "boardPerformanceValue": boardPerformanceValue,
       "boardPerformanceRate": boardPerformanceRate,
       "boardPerformanceTime": boardPerformanceTime,
       "boardPerformanceNeName": boardPerformanceNeName,
       "boardPerformanceNeMap": boardPerformanceNeMap,
       "boardPerformanceRowStatus": boardPerformanceRowStatus}
)
