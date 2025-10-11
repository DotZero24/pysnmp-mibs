# SNMP MIB module (QTECH-AUTHEN-KEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AUTHEN-KEY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:45 2025
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

(ConfigStatus,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechAuthenKeyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24)
)
if mibBuilder.loadTexts:
    qtechAuthenKeyMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechKeyTimeMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("infinite", 1),
          ("duration", 2),
          ("end-time", 3))
    )



# MIB Managed Objects in the order of their OIDs

_QtechAuthenKeyMIBObjects_ObjectIdentity = ObjectIdentity
qtechAuthenKeyMIBObjects = _QtechAuthenKeyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1)
)
_QtechAuthenKeyChainTable_Object = MibTable
qtechAuthenKeyChainTable = _QtechAuthenKeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    qtechAuthenKeyChainTable.setStatus("current")
_QtechAuthenKeyChainEntry_Object = MibTableRow
qtechAuthenKeyChainEntry = _QtechAuthenKeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 1, 1)
)
qtechAuthenKeyChainEntry.setIndexNames(
    (0, "QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyChainName"),
)
if mibBuilder.loadTexts:
    qtechAuthenKeyChainEntry.setStatus("current")


class _QtechAuthenKeyChainName_Type(DisplayString):
    """Custom type qtechAuthenKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechAuthenKeyChainName_Type.__name__ = "DisplayString"
_QtechAuthenKeyChainName_Object = MibTableColumn
qtechAuthenKeyChainName = _QtechAuthenKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 1, 1, 1),
    _QtechAuthenKeyChainName_Type()
)
qtechAuthenKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthenKeyChainName.setStatus("current")
_QtechAuthenKeyChainEntryStatus_Type = ConfigStatus
_QtechAuthenKeyChainEntryStatus_Object = MibTableColumn
qtechAuthenKeyChainEntryStatus = _QtechAuthenKeyChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 1, 1, 2),
    _QtechAuthenKeyChainEntryStatus_Type()
)
qtechAuthenKeyChainEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeyChainEntryStatus.setStatus("current")
_QtechAuthenKeyTable_Object = MibTable
qtechAuthenKeyTable = _QtechAuthenKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    qtechAuthenKeyTable.setStatus("current")
_QtechAuthenKeyEntry_Object = MibTableRow
qtechAuthenKeyEntry = _QtechAuthenKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1)
)
qtechAuthenKeyEntry.setIndexNames(
    (0, "QTECH-AUTHEN-KEY-MIB", "qtechKeyChainName"),
    (0, "QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyNumber"),
)
if mibBuilder.loadTexts:
    qtechAuthenKeyEntry.setStatus("current")


class _QtechKeyChainName_Type(DisplayString):
    """Custom type qtechKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechKeyChainName_Type.__name__ = "DisplayString"
_QtechKeyChainName_Object = MibTableColumn
qtechKeyChainName = _QtechKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 1),
    _QtechKeyChainName_Type()
)
qtechKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechKeyChainName.setStatus("current")


class _QtechAuthenKeyNumber_Type(Integer32):
    """Custom type qtechAuthenKeyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_QtechAuthenKeyNumber_Type.__name__ = "Integer32"
_QtechAuthenKeyNumber_Object = MibTableColumn
qtechAuthenKeyNumber = _QtechAuthenKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 2),
    _QtechAuthenKeyNumber_Type()
)
qtechAuthenKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthenKeyNumber.setStatus("current")


class _QtechKeyString_Type(DisplayString):
    """Custom type qtechKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_QtechKeyString_Type.__name__ = "DisplayString"
_QtechKeyString_Object = MibTableColumn
qtechKeyString = _QtechKeyString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 3),
    _QtechKeyString_Type()
)
qtechKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechKeyString.setStatus("current")
_QtechAuthenKeyReceiveQtechTime_Type = DateAndTime
_QtechAuthenKeyReceiveQtechTime_Object = MibTableColumn
qtechAuthenKeyReceiveQtechTime = _QtechAuthenKeyReceiveQtechTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 4),
    _QtechAuthenKeyReceiveQtechTime_Type()
)
qtechAuthenKeyReceiveQtechTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeyReceiveQtechTime.setStatus("current")
_QtechAuthenKeyReceiveTimeMode_Type = QtechKeyTimeMode
_QtechAuthenKeyReceiveTimeMode_Object = MibTableColumn
qtechAuthenKeyReceiveTimeMode = _QtechAuthenKeyReceiveTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 5),
    _QtechAuthenKeyReceiveTimeMode_Type()
)
qtechAuthenKeyReceiveTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeyReceiveTimeMode.setStatus("current")
_QtechAuthenKeyReceiveEndTime_Type = DateAndTime
_QtechAuthenKeyReceiveEndTime_Object = MibTableColumn
qtechAuthenKeyReceiveEndTime = _QtechAuthenKeyReceiveEndTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 6),
    _QtechAuthenKeyReceiveEndTime_Type()
)
qtechAuthenKeyReceiveEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeyReceiveEndTime.setStatus("current")
_QtechAuthenKeyReceiveDuration_Type = Unsigned32
_QtechAuthenKeyReceiveDuration_Object = MibTableColumn
qtechAuthenKeyReceiveDuration = _QtechAuthenKeyReceiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 7),
    _QtechAuthenKeyReceiveDuration_Type()
)
qtechAuthenKeyReceiveDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeyReceiveDuration.setStatus("current")
_QtechAuthenKeySendQtechTime_Type = DateAndTime
_QtechAuthenKeySendQtechTime_Object = MibTableColumn
qtechAuthenKeySendQtechTime = _QtechAuthenKeySendQtechTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 8),
    _QtechAuthenKeySendQtechTime_Type()
)
qtechAuthenKeySendQtechTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeySendQtechTime.setStatus("current")
_QtechAuthenKeySendTimeMode_Type = QtechKeyTimeMode
_QtechAuthenKeySendTimeMode_Object = MibTableColumn
qtechAuthenKeySendTimeMode = _QtechAuthenKeySendTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 9),
    _QtechAuthenKeySendTimeMode_Type()
)
qtechAuthenKeySendTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeySendTimeMode.setStatus("current")
_QtechAuthenKeySendEndTime_Type = DateAndTime
_QtechAuthenKeySendEndTime_Object = MibTableColumn
qtechAuthenKeySendEndTime = _QtechAuthenKeySendEndTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 10),
    _QtechAuthenKeySendEndTime_Type()
)
qtechAuthenKeySendEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeySendEndTime.setStatus("current")
_QtechAuthenKeySendDuration_Type = Unsigned32
_QtechAuthenKeySendDuration_Object = MibTableColumn
qtechAuthenKeySendDuration = _QtechAuthenKeySendDuration_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 11),
    _QtechAuthenKeySendDuration_Type()
)
qtechAuthenKeySendDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeySendDuration.setStatus("current")


class _QtechAuthenReceiveKeyState_Type(Integer32):
    """Custom type qtechAuthenReceiveKeyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_QtechAuthenReceiveKeyState_Type.__name__ = "Integer32"
_QtechAuthenReceiveKeyState_Object = MibTableColumn
qtechAuthenReceiveKeyState = _QtechAuthenReceiveKeyState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 12),
    _QtechAuthenReceiveKeyState_Type()
)
qtechAuthenReceiveKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthenReceiveKeyState.setStatus("current")


class _QtechAuthenSendKeyState_Type(Integer32):
    """Custom type qtechAuthenSendKeyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_QtechAuthenSendKeyState_Type.__name__ = "Integer32"
_QtechAuthenSendKeyState_Object = MibTableColumn
qtechAuthenSendKeyState = _QtechAuthenSendKeyState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 13),
    _QtechAuthenSendKeyState_Type()
)
qtechAuthenSendKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAuthenSendKeyState.setStatus("current")
_QtechAuthenKeyEntryStauts_Type = RowStatus
_QtechAuthenKeyEntryStauts_Object = MibTableColumn
qtechAuthenKeyEntryStauts = _QtechAuthenKeyEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 1, 2, 1, 14),
    _QtechAuthenKeyEntryStauts_Type()
)
qtechAuthenKeyEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAuthenKeyEntryStauts.setStatus("current")
_QtechAuthenKeyChainMIBConformance_ObjectIdentity = ObjectIdentity
qtechAuthenKeyChainMIBConformance = _QtechAuthenKeyChainMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 2)
)
_QtechAuthenKeyChainMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAuthenKeyChainMIBCompliances = _QtechAuthenKeyChainMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 2, 1)
)
_QtechAuthenKeyChainMIBGroups_ObjectIdentity = ObjectIdentity
qtechAuthenKeyChainMIBGroups = _QtechAuthenKeyChainMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 2, 2)
)

# Managed Objects groups

qtechAuthenKeyChainMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 2, 2, 1)
)
qtechAuthenKeyChainMIBGroup.setObjects(
      *(("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyChainName"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyChainEntryStatus"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechKeyChainName"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyNumber"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechKeyString"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyReceiveQtechTime"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyReceiveTimeMode"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyReceiveEndTime"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyReceiveDuration"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeySendQtechTime"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeySendTimeMode"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeySendEndTime"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeySendDuration"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenReceiveKeyState"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenSendKeyState"),
        ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyEntryStauts"))
)
if mibBuilder.loadTexts:
    qtechAuthenKeyChainMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechAuthenKeyChainMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 24, 2, 1, 1)
)
qtechAuthenKeyChainMIBCompliance.setObjects(
    ("QTECH-AUTHEN-KEY-MIB", "qtechAuthenKeyChainMIBGroup")
)
if mibBuilder.loadTexts:
    qtechAuthenKeyChainMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AUTHEN-KEY-MIB",
    **{"QtechKeyTimeMode": QtechKeyTimeMode,
       "qtechAuthenKeyMIB": qtechAuthenKeyMIB,
       "qtechAuthenKeyMIBObjects": qtechAuthenKeyMIBObjects,
       "qtechAuthenKeyChainTable": qtechAuthenKeyChainTable,
       "qtechAuthenKeyChainEntry": qtechAuthenKeyChainEntry,
       "qtechAuthenKeyChainName": qtechAuthenKeyChainName,
       "qtechAuthenKeyChainEntryStatus": qtechAuthenKeyChainEntryStatus,
       "qtechAuthenKeyTable": qtechAuthenKeyTable,
       "qtechAuthenKeyEntry": qtechAuthenKeyEntry,
       "qtechKeyChainName": qtechKeyChainName,
       "qtechAuthenKeyNumber": qtechAuthenKeyNumber,
       "qtechKeyString": qtechKeyString,
       "qtechAuthenKeyReceiveQtechTime": qtechAuthenKeyReceiveQtechTime,
       "qtechAuthenKeyReceiveTimeMode": qtechAuthenKeyReceiveTimeMode,
       "qtechAuthenKeyReceiveEndTime": qtechAuthenKeyReceiveEndTime,
       "qtechAuthenKeyReceiveDuration": qtechAuthenKeyReceiveDuration,
       "qtechAuthenKeySendQtechTime": qtechAuthenKeySendQtechTime,
       "qtechAuthenKeySendTimeMode": qtechAuthenKeySendTimeMode,
       "qtechAuthenKeySendEndTime": qtechAuthenKeySendEndTime,
       "qtechAuthenKeySendDuration": qtechAuthenKeySendDuration,
       "qtechAuthenReceiveKeyState": qtechAuthenReceiveKeyState,
       "qtechAuthenSendKeyState": qtechAuthenSendKeyState,
       "qtechAuthenKeyEntryStauts": qtechAuthenKeyEntryStauts,
       "qtechAuthenKeyChainMIBConformance": qtechAuthenKeyChainMIBConformance,
       "qtechAuthenKeyChainMIBCompliances": qtechAuthenKeyChainMIBCompliances,
       "qtechAuthenKeyChainMIBCompliance": qtechAuthenKeyChainMIBCompliance,
       "qtechAuthenKeyChainMIBGroups": qtechAuthenKeyChainMIBGroups,
       "qtechAuthenKeyChainMIBGroup": qtechAuthenKeyChainMIBGroup}
)
