# SNMP MIB module (MY-AUTHEN-KEY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-AUTHEN-KEY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:34 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myAuthenKeyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24)
)
if mibBuilder.loadTexts:
    myAuthenKeyMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MyKeyTimeMode(TextualConvention, Integer32):
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

_MyAuthenKeyMIBObjects_ObjectIdentity = ObjectIdentity
myAuthenKeyMIBObjects = _MyAuthenKeyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1)
)
_MyAuthenKeyChainTable_Object = MibTable
myAuthenKeyChainTable = _MyAuthenKeyChainTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1)
)
if mibBuilder.loadTexts:
    myAuthenKeyChainTable.setStatus("current")
_MyAuthenKeyChainEntry_Object = MibTableRow
myAuthenKeyChainEntry = _MyAuthenKeyChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1, 1)
)
myAuthenKeyChainEntry.setIndexNames(
    (0, "MY-AUTHEN-KEY-MIB", "myAuthenKeyChainName"),
)
if mibBuilder.loadTexts:
    myAuthenKeyChainEntry.setStatus("current")


class _MyAuthenKeyChainName_Type(DisplayString):
    """Custom type myAuthenKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyAuthenKeyChainName_Type.__name__ = "DisplayString"
_MyAuthenKeyChainName_Object = MibTableColumn
myAuthenKeyChainName = _MyAuthenKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1, 1, 1),
    _MyAuthenKeyChainName_Type()
)
myAuthenKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthenKeyChainName.setStatus("current")
_MyAuthenKeyChainEntryStatus_Type = ConfigStatus
_MyAuthenKeyChainEntryStatus_Object = MibTableColumn
myAuthenKeyChainEntryStatus = _MyAuthenKeyChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 1, 1, 2),
    _MyAuthenKeyChainEntryStatus_Type()
)
myAuthenKeyChainEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAuthenKeyChainEntryStatus.setStatus("current")
_MyAuthenKeyTable_Object = MibTable
myAuthenKeyTable = _MyAuthenKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2)
)
if mibBuilder.loadTexts:
    myAuthenKeyTable.setStatus("current")
_MyAuthenKeyEntry_Object = MibTableRow
myAuthenKeyEntry = _MyAuthenKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1)
)
myAuthenKeyEntry.setIndexNames(
    (0, "MY-AUTHEN-KEY-MIB", "myKeyChainName"),
    (0, "MY-AUTHEN-KEY-MIB", "myAuthenKeyNumber"),
)
if mibBuilder.loadTexts:
    myAuthenKeyEntry.setStatus("current")


class _MyKeyChainName_Type(DisplayString):
    """Custom type myKeyChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyKeyChainName_Type.__name__ = "DisplayString"
_MyKeyChainName_Object = MibTableColumn
myKeyChainName = _MyKeyChainName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 1),
    _MyKeyChainName_Type()
)
myKeyChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myKeyChainName.setStatus("current")


class _MyAuthenKeyNumber_Type(Integer32):
    """Custom type myAuthenKeyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MyAuthenKeyNumber_Type.__name__ = "Integer32"
_MyAuthenKeyNumber_Object = MibTableColumn
myAuthenKeyNumber = _MyAuthenKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 2),
    _MyAuthenKeyNumber_Type()
)
myAuthenKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthenKeyNumber.setStatus("current")


class _MyKeyString_Type(DisplayString):
    """Custom type myKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_MyKeyString_Type.__name__ = "DisplayString"
_MyKeyString_Object = MibTableColumn
myKeyString = _MyKeyString_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 3),
    _MyKeyString_Type()
)
myKeyString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myKeyString.setStatus("current")
_MyAuthenKeyReceiveMyTime_Type = DateAndTime
_MyAuthenKeyReceiveMyTime_Object = MibTableColumn
myAuthenKeyReceiveMyTime = _MyAuthenKeyReceiveMyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 4),
    _MyAuthenKeyReceiveMyTime_Type()
)
myAuthenKeyReceiveMyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeyReceiveMyTime.setStatus("current")
_MyAuthenKeyReceiveTimeMode_Type = MyKeyTimeMode
_MyAuthenKeyReceiveTimeMode_Object = MibTableColumn
myAuthenKeyReceiveTimeMode = _MyAuthenKeyReceiveTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 5),
    _MyAuthenKeyReceiveTimeMode_Type()
)
myAuthenKeyReceiveTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeyReceiveTimeMode.setStatus("current")
_MyAuthenKeyReceiveEndTime_Type = DateAndTime
_MyAuthenKeyReceiveEndTime_Object = MibTableColumn
myAuthenKeyReceiveEndTime = _MyAuthenKeyReceiveEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 6),
    _MyAuthenKeyReceiveEndTime_Type()
)
myAuthenKeyReceiveEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeyReceiveEndTime.setStatus("current")
_MyAuthenKeyReceiveDuration_Type = Unsigned32
_MyAuthenKeyReceiveDuration_Object = MibTableColumn
myAuthenKeyReceiveDuration = _MyAuthenKeyReceiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 7),
    _MyAuthenKeyReceiveDuration_Type()
)
myAuthenKeyReceiveDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeyReceiveDuration.setStatus("current")
_MyAuthenKeySendMyTime_Type = DateAndTime
_MyAuthenKeySendMyTime_Object = MibTableColumn
myAuthenKeySendMyTime = _MyAuthenKeySendMyTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 8),
    _MyAuthenKeySendMyTime_Type()
)
myAuthenKeySendMyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeySendMyTime.setStatus("current")
_MyAuthenKeySendTimeMode_Type = MyKeyTimeMode
_MyAuthenKeySendTimeMode_Object = MibTableColumn
myAuthenKeySendTimeMode = _MyAuthenKeySendTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 9),
    _MyAuthenKeySendTimeMode_Type()
)
myAuthenKeySendTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeySendTimeMode.setStatus("current")
_MyAuthenKeySendEndTime_Type = DateAndTime
_MyAuthenKeySendEndTime_Object = MibTableColumn
myAuthenKeySendEndTime = _MyAuthenKeySendEndTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 10),
    _MyAuthenKeySendEndTime_Type()
)
myAuthenKeySendEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeySendEndTime.setStatus("current")
_MyAuthenKeySendDuration_Type = Unsigned32
_MyAuthenKeySendDuration_Object = MibTableColumn
myAuthenKeySendDuration = _MyAuthenKeySendDuration_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 11),
    _MyAuthenKeySendDuration_Type()
)
myAuthenKeySendDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myAuthenKeySendDuration.setStatus("current")


class _MyAuthenReceiveKeyState_Type(Integer32):
    """Custom type myAuthenReceiveKeyState based on Integer32"""
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


_MyAuthenReceiveKeyState_Type.__name__ = "Integer32"
_MyAuthenReceiveKeyState_Object = MibTableColumn
myAuthenReceiveKeyState = _MyAuthenReceiveKeyState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 12),
    _MyAuthenReceiveKeyState_Type()
)
myAuthenReceiveKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthenReceiveKeyState.setStatus("current")


class _MyAuthenSendKeyState_Type(Integer32):
    """Custom type myAuthenSendKeyState based on Integer32"""
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


_MyAuthenSendKeyState_Type.__name__ = "Integer32"
_MyAuthenSendKeyState_Object = MibTableColumn
myAuthenSendKeyState = _MyAuthenSendKeyState_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 13),
    _MyAuthenSendKeyState_Type()
)
myAuthenSendKeyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myAuthenSendKeyState.setStatus("current")
_MyAuthenKeyEntryStauts_Type = RowStatus
_MyAuthenKeyEntryStauts_Object = MibTableColumn
myAuthenKeyEntryStauts = _MyAuthenKeyEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 1, 2, 1, 14),
    _MyAuthenKeyEntryStauts_Type()
)
myAuthenKeyEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myAuthenKeyEntryStauts.setStatus("current")
_MyAuthenKeyChainMIBConformance_ObjectIdentity = ObjectIdentity
myAuthenKeyChainMIBConformance = _MyAuthenKeyChainMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2)
)
_MyAuthenKeyChainMIBCompliances_ObjectIdentity = ObjectIdentity
myAuthenKeyChainMIBCompliances = _MyAuthenKeyChainMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 1)
)
_MyAuthenKeyChainMIBGroups_ObjectIdentity = ObjectIdentity
myAuthenKeyChainMIBGroups = _MyAuthenKeyChainMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 2)
)

# Managed Objects groups

myAuthenKeyChainMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 2, 1)
)
myAuthenKeyChainMIBGroup.setObjects(
      *(("MY-AUTHEN-KEY-MIB", "myAuthenKeyChainName"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyChainEntryStatus"),
        ("MY-AUTHEN-KEY-MIB", "myKeyChainName"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyNumber"),
        ("MY-AUTHEN-KEY-MIB", "myKeyString"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyReceiveMyTime"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyReceiveTimeMode"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyReceiveEndTime"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyReceiveDuration"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeySendMyTime"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeySendTimeMode"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeySendEndTime"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeySendDuration"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenReceiveKeyState"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenSendKeyState"),
        ("MY-AUTHEN-KEY-MIB", "myAuthenKeyEntryStauts"))
)
if mibBuilder.loadTexts:
    myAuthenKeyChainMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myAuthenKeyChainMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 24, 2, 1, 1)
)
myAuthenKeyChainMIBCompliance.setObjects(
    ("MY-AUTHEN-KEY-MIB", "myAuthenKeyChainMIBGroup")
)
if mibBuilder.loadTexts:
    myAuthenKeyChainMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-AUTHEN-KEY-MIB",
    **{"MyKeyTimeMode": MyKeyTimeMode,
       "myAuthenKeyMIB": myAuthenKeyMIB,
       "myAuthenKeyMIBObjects": myAuthenKeyMIBObjects,
       "myAuthenKeyChainTable": myAuthenKeyChainTable,
       "myAuthenKeyChainEntry": myAuthenKeyChainEntry,
       "myAuthenKeyChainName": myAuthenKeyChainName,
       "myAuthenKeyChainEntryStatus": myAuthenKeyChainEntryStatus,
       "myAuthenKeyTable": myAuthenKeyTable,
       "myAuthenKeyEntry": myAuthenKeyEntry,
       "myKeyChainName": myKeyChainName,
       "myAuthenKeyNumber": myAuthenKeyNumber,
       "myKeyString": myKeyString,
       "myAuthenKeyReceiveMyTime": myAuthenKeyReceiveMyTime,
       "myAuthenKeyReceiveTimeMode": myAuthenKeyReceiveTimeMode,
       "myAuthenKeyReceiveEndTime": myAuthenKeyReceiveEndTime,
       "myAuthenKeyReceiveDuration": myAuthenKeyReceiveDuration,
       "myAuthenKeySendMyTime": myAuthenKeySendMyTime,
       "myAuthenKeySendTimeMode": myAuthenKeySendTimeMode,
       "myAuthenKeySendEndTime": myAuthenKeySendEndTime,
       "myAuthenKeySendDuration": myAuthenKeySendDuration,
       "myAuthenReceiveKeyState": myAuthenReceiveKeyState,
       "myAuthenSendKeyState": myAuthenSendKeyState,
       "myAuthenKeyEntryStauts": myAuthenKeyEntryStauts,
       "myAuthenKeyChainMIBConformance": myAuthenKeyChainMIBConformance,
       "myAuthenKeyChainMIBCompliances": myAuthenKeyChainMIBCompliances,
       "myAuthenKeyChainMIBCompliance": myAuthenKeyChainMIBCompliance,
       "myAuthenKeyChainMIBGroups": myAuthenKeyChainMIBGroups,
       "myAuthenKeyChainMIBGroup": myAuthenKeyChainMIBGroup}
)
