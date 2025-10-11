# SNMP MIB module (FS-AUTHEN-KEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-AUTHEN-KEY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:15 2025
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

(ConfigStatus,) = mibBuilder.importSymbols(
    "FS-TC",
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

fsAuthenKeyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24)
)
if mibBuilder.loadTexts:
    fsAuthenKeyMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSKeyTimeMode(TextualConvention, Integer32):
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

_FsAuthenKeyMIBObjects_ObjectIdentity = ObjectIdentity
fsAuthenKeyMIBObjects = _FsAuthenKeyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1)
)
_FsAuthenKeyChainTable_Object = MibTable
fsAuthenKeyChainTable = _FsAuthenKeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    fsAuthenKeyChainTable.setStatus("current")
_FsAuthenKeyChainEntry_Object = MibTableRow
fsAuthenKeyChainEntry = _FsAuthenKeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 1, 1)
)
fsAuthenKeyChainEntry.setIndexNames(
    (0, "FS-AUTHEN-KEY-MIB", "fsAuthenKeyChainName"),
)
if mibBuilder.loadTexts:
    fsAuthenKeyChainEntry.setStatus("current")


class _FsAuthenKeyChainName_Type(DisplayString):
    """Custom type fsAuthenKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsAuthenKeyChainName_Type.__name__ = "DisplayString"
_FsAuthenKeyChainName_Object = MibTableColumn
fsAuthenKeyChainName = _FsAuthenKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 1, 1, 1),
    _FsAuthenKeyChainName_Type()
)
fsAuthenKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthenKeyChainName.setStatus("current")
_FsAuthenKeyChainEntryStatus_Type = ConfigStatus
_FsAuthenKeyChainEntryStatus_Object = MibTableColumn
fsAuthenKeyChainEntryStatus = _FsAuthenKeyChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 1, 1, 2),
    _FsAuthenKeyChainEntryStatus_Type()
)
fsAuthenKeyChainEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeyChainEntryStatus.setStatus("current")
_FsAuthenKeyTable_Object = MibTable
fsAuthenKeyTable = _FsAuthenKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    fsAuthenKeyTable.setStatus("current")
_FsAuthenKeyEntry_Object = MibTableRow
fsAuthenKeyEntry = _FsAuthenKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1)
)
fsAuthenKeyEntry.setIndexNames(
    (0, "FS-AUTHEN-KEY-MIB", "fsKeyChainName"),
    (0, "FS-AUTHEN-KEY-MIB", "fsAuthenKeyNumber"),
)
if mibBuilder.loadTexts:
    fsAuthenKeyEntry.setStatus("current")


class _FsKeyChainName_Type(DisplayString):
    """Custom type fsKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsKeyChainName_Type.__name__ = "DisplayString"
_FsKeyChainName_Object = MibTableColumn
fsKeyChainName = _FsKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 1),
    _FsKeyChainName_Type()
)
fsKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsKeyChainName.setStatus("current")


class _FsAuthenKeyNumber_Type(Integer32):
    """Custom type fsAuthenKeyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsAuthenKeyNumber_Type.__name__ = "Integer32"
_FsAuthenKeyNumber_Object = MibTableColumn
fsAuthenKeyNumber = _FsAuthenKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 2),
    _FsAuthenKeyNumber_Type()
)
fsAuthenKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthenKeyNumber.setStatus("current")


class _FsKeyString_Type(DisplayString):
    """Custom type fsKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_FsKeyString_Type.__name__ = "DisplayString"
_FsKeyString_Object = MibTableColumn
fsKeyString = _FsKeyString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 3),
    _FsKeyString_Type()
)
fsKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsKeyString.setStatus("current")
_FsAuthenKeyReceiveFSTime_Type = DateAndTime
_FsAuthenKeyReceiveFSTime_Object = MibTableColumn
fsAuthenKeyReceiveFSTime = _FsAuthenKeyReceiveFSTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 4),
    _FsAuthenKeyReceiveFSTime_Type()
)
fsAuthenKeyReceiveFSTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeyReceiveFSTime.setStatus("current")
_FsAuthenKeyReceiveTimeMode_Type = FSKeyTimeMode
_FsAuthenKeyReceiveTimeMode_Object = MibTableColumn
fsAuthenKeyReceiveTimeMode = _FsAuthenKeyReceiveTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 5),
    _FsAuthenKeyReceiveTimeMode_Type()
)
fsAuthenKeyReceiveTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeyReceiveTimeMode.setStatus("current")
_FsAuthenKeyReceiveEndTime_Type = DateAndTime
_FsAuthenKeyReceiveEndTime_Object = MibTableColumn
fsAuthenKeyReceiveEndTime = _FsAuthenKeyReceiveEndTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 6),
    _FsAuthenKeyReceiveEndTime_Type()
)
fsAuthenKeyReceiveEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeyReceiveEndTime.setStatus("current")
_FsAuthenKeyReceiveDuration_Type = Unsigned32
_FsAuthenKeyReceiveDuration_Object = MibTableColumn
fsAuthenKeyReceiveDuration = _FsAuthenKeyReceiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 7),
    _FsAuthenKeyReceiveDuration_Type()
)
fsAuthenKeyReceiveDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeyReceiveDuration.setStatus("current")
_FsAuthenKeySendFSTime_Type = DateAndTime
_FsAuthenKeySendFSTime_Object = MibTableColumn
fsAuthenKeySendFSTime = _FsAuthenKeySendFSTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 8),
    _FsAuthenKeySendFSTime_Type()
)
fsAuthenKeySendFSTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeySendFSTime.setStatus("current")
_FsAuthenKeySendTimeMode_Type = FSKeyTimeMode
_FsAuthenKeySendTimeMode_Object = MibTableColumn
fsAuthenKeySendTimeMode = _FsAuthenKeySendTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 9),
    _FsAuthenKeySendTimeMode_Type()
)
fsAuthenKeySendTimeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeySendTimeMode.setStatus("current")
_FsAuthenKeySendEndTime_Type = DateAndTime
_FsAuthenKeySendEndTime_Object = MibTableColumn
fsAuthenKeySendEndTime = _FsAuthenKeySendEndTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 10),
    _FsAuthenKeySendEndTime_Type()
)
fsAuthenKeySendEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeySendEndTime.setStatus("current")
_FsAuthenKeySendDuration_Type = Unsigned32
_FsAuthenKeySendDuration_Object = MibTableColumn
fsAuthenKeySendDuration = _FsAuthenKeySendDuration_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 11),
    _FsAuthenKeySendDuration_Type()
)
fsAuthenKeySendDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeySendDuration.setStatus("current")


class _FsAuthenReceiveKeyState_Type(Integer32):
    """Custom type fsAuthenReceiveKeyState based on Integer32"""
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


_FsAuthenReceiveKeyState_Type.__name__ = "Integer32"
_FsAuthenReceiveKeyState_Object = MibTableColumn
fsAuthenReceiveKeyState = _FsAuthenReceiveKeyState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 12),
    _FsAuthenReceiveKeyState_Type()
)
fsAuthenReceiveKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthenReceiveKeyState.setStatus("current")


class _FsAuthenSendKeyState_Type(Integer32):
    """Custom type fsAuthenSendKeyState based on Integer32"""
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


_FsAuthenSendKeyState_Type.__name__ = "Integer32"
_FsAuthenSendKeyState_Object = MibTableColumn
fsAuthenSendKeyState = _FsAuthenSendKeyState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 13),
    _FsAuthenSendKeyState_Type()
)
fsAuthenSendKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAuthenSendKeyState.setStatus("current")
_FsAuthenKeyEntryStauts_Type = RowStatus
_FsAuthenKeyEntryStauts_Object = MibTableColumn
fsAuthenKeyEntryStauts = _FsAuthenKeyEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 1, 2, 1, 14),
    _FsAuthenKeyEntryStauts_Type()
)
fsAuthenKeyEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAuthenKeyEntryStauts.setStatus("current")
_FsAuthenKeyChainMIBConformance_ObjectIdentity = ObjectIdentity
fsAuthenKeyChainMIBConformance = _FsAuthenKeyChainMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 2)
)
_FsAuthenKeyChainMIBCompliances_ObjectIdentity = ObjectIdentity
fsAuthenKeyChainMIBCompliances = _FsAuthenKeyChainMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 2, 1)
)
_FsAuthenKeyChainMIBGroups_ObjectIdentity = ObjectIdentity
fsAuthenKeyChainMIBGroups = _FsAuthenKeyChainMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 2, 2)
)

# Managed Objects groups

fsAuthenKeyChainMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 2, 2, 1)
)
fsAuthenKeyChainMIBGroup.setObjects(
      *(("FS-AUTHEN-KEY-MIB", "fsAuthenKeyChainName"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyChainEntryStatus"),
        ("FS-AUTHEN-KEY-MIB", "fsKeyChainName"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyNumber"),
        ("FS-AUTHEN-KEY-MIB", "fsKeyString"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyReceiveFSTime"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyReceiveTimeMode"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyReceiveEndTime"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyReceiveDuration"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeySendFSTime"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeySendTimeMode"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeySendEndTime"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeySendDuration"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenReceiveKeyState"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenSendKeyState"),
        ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyEntryStauts"))
)
if mibBuilder.loadTexts:
    fsAuthenKeyChainMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsAuthenKeyChainMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 24, 2, 1, 1)
)
fsAuthenKeyChainMIBCompliance.setObjects(
    ("FS-AUTHEN-KEY-MIB", "fsAuthenKeyChainMIBGroup")
)
if mibBuilder.loadTexts:
    fsAuthenKeyChainMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-AUTHEN-KEY-MIB",
    **{"FSKeyTimeMode": FSKeyTimeMode,
       "fsAuthenKeyMIB": fsAuthenKeyMIB,
       "fsAuthenKeyMIBObjects": fsAuthenKeyMIBObjects,
       "fsAuthenKeyChainTable": fsAuthenKeyChainTable,
       "fsAuthenKeyChainEntry": fsAuthenKeyChainEntry,
       "fsAuthenKeyChainName": fsAuthenKeyChainName,
       "fsAuthenKeyChainEntryStatus": fsAuthenKeyChainEntryStatus,
       "fsAuthenKeyTable": fsAuthenKeyTable,
       "fsAuthenKeyEntry": fsAuthenKeyEntry,
       "fsKeyChainName": fsKeyChainName,
       "fsAuthenKeyNumber": fsAuthenKeyNumber,
       "fsKeyString": fsKeyString,
       "fsAuthenKeyReceiveFSTime": fsAuthenKeyReceiveFSTime,
       "fsAuthenKeyReceiveTimeMode": fsAuthenKeyReceiveTimeMode,
       "fsAuthenKeyReceiveEndTime": fsAuthenKeyReceiveEndTime,
       "fsAuthenKeyReceiveDuration": fsAuthenKeyReceiveDuration,
       "fsAuthenKeySendFSTime": fsAuthenKeySendFSTime,
       "fsAuthenKeySendTimeMode": fsAuthenKeySendTimeMode,
       "fsAuthenKeySendEndTime": fsAuthenKeySendEndTime,
       "fsAuthenKeySendDuration": fsAuthenKeySendDuration,
       "fsAuthenReceiveKeyState": fsAuthenReceiveKeyState,
       "fsAuthenSendKeyState": fsAuthenSendKeyState,
       "fsAuthenKeyEntryStauts": fsAuthenKeyEntryStauts,
       "fsAuthenKeyChainMIBConformance": fsAuthenKeyChainMIBConformance,
       "fsAuthenKeyChainMIBCompliances": fsAuthenKeyChainMIBCompliances,
       "fsAuthenKeyChainMIBCompliance": fsAuthenKeyChainMIBCompliance,
       "fsAuthenKeyChainMIBGroups": fsAuthenKeyChainMIBGroups,
       "fsAuthenKeyChainMIBGroup": fsAuthenKeyChainMIBGroup}
)
