# SNMP MIB module (LUM-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:54 2025
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

(lumModules,
 lumSnmpMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSnmpMIB")

(CommandString,) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString")

(SnmpEngineID,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpEngineID")

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
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

lumSnmpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 18)
)
if mibBuilder.loadTexts:
    lumSnmpMIBModule.setRevisions(
        ("2018-04-13 00:00",
         "2017-06-15 00:00",
         "2014-12-09 00:00",
         "2008-06-05 00:00",
         "2004-10-01 00:00",
         "2004-06-23 00:00",
         "2003-09-30 00:00",
         "2002-05-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSnmpConfs_ObjectIdentity = ObjectIdentity
lumSnmpConfs = _LumSnmpConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1)
)
_LumSnmpGroups_ObjectIdentity = ObjectIdentity
lumSnmpGroups = _LumSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1)
)
_LumSnmpCompl_ObjectIdentity = ObjectIdentity
lumSnmpCompl = _LumSnmpCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2)
)
_LumSnmpMIBObjects_ObjectIdentity = ObjectIdentity
lumSnmpMIBObjects = _LumSnmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2)
)
_SnmpInformSinkList_ObjectIdentity = ObjectIdentity
snmpInformSinkList = _SnmpInformSinkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1)
)
_SnmpInformSinkTable_Object = MibTable
snmpInformSinkTable = _SnmpInformSinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    snmpInformSinkTable.setStatus("current")
_SnmpInformSinkEntry_Object = MibTableRow
snmpInformSinkEntry = _SnmpInformSinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1)
)
snmpInformSinkEntry.setIndexNames(
    (0, "LUM-SNMP-MIB", "snmpInformSinkIndex"),
)
if mibBuilder.loadTexts:
    snmpInformSinkEntry.setStatus("current")


class _SnmpInformSinkIndex_Type(Unsigned32):
    """Custom type snmpInformSinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpInformSinkIndex_Type.__name__ = "Unsigned32"
_SnmpInformSinkIndex_Object = MibTableColumn
snmpInformSinkIndex = _SnmpInformSinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 1),
    _SnmpInformSinkIndex_Type()
)
snmpInformSinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformSinkIndex.setStatus("current")


class _SnmpInformSinkName_Type(DisplayString):
    """Custom type snmpInformSinkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmpInformSinkName_Type.__name__ = "DisplayString"
_SnmpInformSinkName_Object = MibTableColumn
snmpInformSinkName = _SnmpInformSinkName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 2),
    _SnmpInformSinkName_Type()
)
snmpInformSinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInformSinkName.setStatus("current")
_SnmpInformSinkAddr_Type = IpAddress
_SnmpInformSinkAddr_Object = MibTableColumn
snmpInformSinkAddr = _SnmpInformSinkAddr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 3),
    _SnmpInformSinkAddr_Type()
)
snmpInformSinkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpInformSinkAddr.setStatus("current")


class _SnmpInformSinkPort_Type(Unsigned32):
    """Custom type snmpInformSinkPort based on Unsigned32"""
    defaultValue = 162

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpInformSinkPort_Type.__name__ = "Unsigned32"
_SnmpInformSinkPort_Object = MibTableColumn
snmpInformSinkPort = _SnmpInformSinkPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 4),
    _SnmpInformSinkPort_Type()
)
snmpInformSinkPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpInformSinkPort.setStatus("current")


class _SnmpInformSinkCommunity_Type(DisplayString):
    """Custom type snmpInformSinkCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmpInformSinkCommunity_Type.__name__ = "DisplayString"
_SnmpInformSinkCommunity_Object = MibTableColumn
snmpInformSinkCommunity = _SnmpInformSinkCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 5),
    _SnmpInformSinkCommunity_Type()
)
snmpInformSinkCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformSinkCommunity.setStatus("current")
_SnmpInformSinkRowStatus_Type = RowStatus
_SnmpInformSinkRowStatus_Object = MibTableColumn
snmpInformSinkRowStatus = _SnmpInformSinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 6),
    _SnmpInformSinkRowStatus_Type()
)
snmpInformSinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpInformSinkRowStatus.setStatus("current")
_SnmpInformSinkStorageType_Type = StorageType
_SnmpInformSinkStorageType_Object = MibTableColumn
snmpInformSinkStorageType = _SnmpInformSinkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 7),
    _SnmpInformSinkStorageType_Type()
)
snmpInformSinkStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpInformSinkStorageType.setStatus("current")


class _SnmpInformSinkAlarmNotifications_Type(Integer32):
    """Custom type snmpInformSinkAlarmNotifications based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SnmpInformSinkAlarmNotifications_Type.__name__ = "Integer32"
_SnmpInformSinkAlarmNotifications_Object = MibTableColumn
snmpInformSinkAlarmNotifications = _SnmpInformSinkAlarmNotifications_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 8),
    _SnmpInformSinkAlarmNotifications_Type()
)
snmpInformSinkAlarmNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformSinkAlarmNotifications.setStatus("current")


class _SnmpInformSinkPerformanceNotifications_Type(Integer32):
    """Custom type snmpInformSinkPerformanceNotifications based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SnmpInformSinkPerformanceNotifications_Type.__name__ = "Integer32"
_SnmpInformSinkPerformanceNotifications_Object = MibTableColumn
snmpInformSinkPerformanceNotifications = _SnmpInformSinkPerformanceNotifications_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 9),
    _SnmpInformSinkPerformanceNotifications_Type()
)
snmpInformSinkPerformanceNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformSinkPerformanceNotifications.setStatus("current")


class _SnmpInformSinkOtherNotifications_Type(Integer32):
    """Custom type snmpInformSinkOtherNotifications based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SnmpInformSinkOtherNotifications_Type.__name__ = "Integer32"
_SnmpInformSinkOtherNotifications_Object = MibTableColumn
snmpInformSinkOtherNotifications = _SnmpInformSinkOtherNotifications_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 10),
    _SnmpInformSinkOtherNotifications_Type()
)
snmpInformSinkOtherNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformSinkOtherNotifications.setStatus("current")


class _SnmpInformSinkMib2Notifications_Type(Integer32):
    """Custom type snmpInformSinkMib2Notifications based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SnmpInformSinkMib2Notifications_Type.__name__ = "Integer32"
_SnmpInformSinkMib2Notifications_Object = MibTableColumn
snmpInformSinkMib2Notifications = _SnmpInformSinkMib2Notifications_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 1, 1, 1, 11),
    _SnmpInformSinkMib2Notifications_Type()
)
snmpInformSinkMib2Notifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformSinkMib2Notifications.setStatus("current")
_SnmpGeneral_ObjectIdentity = ObjectIdentity
snmpGeneral = _SnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2)
)
_SnmpGeneralLastChangeTime_Type = DateAndTime
_SnmpGeneralLastChangeTime_Object = MibScalar
snmpGeneralLastChangeTime = _SnmpGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 1),
    _SnmpGeneralLastChangeTime_Type()
)
snmpGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralLastChangeTime.setStatus("current")
_SnmpGeneralConfigLastChangeTime_Type = DateAndTime
_SnmpGeneralConfigLastChangeTime_Object = MibScalar
snmpGeneralConfigLastChangeTime = _SnmpGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 2),
    _SnmpGeneralConfigLastChangeTime_Type()
)
snmpGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralConfigLastChangeTime.setStatus("current")
_SnmpGeneralEngineID_Type = SnmpEngineID
_SnmpGeneralEngineID_Object = MibScalar
snmpGeneralEngineID = _SnmpGeneralEngineID_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 3),
    _SnmpGeneralEngineID_Type()
)
snmpGeneralEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralEngineID.setStatus("current")


class _SnmpGeneralCommunity_Type(DisplayString):
    """Custom type snmpGeneralCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SnmpGeneralCommunity_Type.__name__ = "DisplayString"
_SnmpGeneralCommunity_Object = MibScalar
snmpGeneralCommunity = _SnmpGeneralCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 4),
    _SnmpGeneralCommunity_Type()
)
snmpGeneralCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGeneralCommunity.setStatus("current")
_SnmpGeneralInformSinkTableSize_Type = Unsigned32
_SnmpGeneralInformSinkTableSize_Object = MibScalar
snmpGeneralInformSinkTableSize = _SnmpGeneralInformSinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 5),
    _SnmpGeneralInformSinkTableSize_Type()
)
snmpGeneralInformSinkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralInformSinkTableSize.setStatus("current")
_SnmpGeneralUserTableSize_Type = Unsigned32
_SnmpGeneralUserTableSize_Object = MibScalar
snmpGeneralUserTableSize = _SnmpGeneralUserTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 6),
    _SnmpGeneralUserTableSize_Type()
)
snmpGeneralUserTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralUserTableSize.setStatus("current")
_SnmpGeneralResetEngineIDCommand_Type = CommandString
_SnmpGeneralResetEngineIDCommand_Object = MibScalar
snmpGeneralResetEngineIDCommand = _SnmpGeneralResetEngineIDCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 7),
    _SnmpGeneralResetEngineIDCommand_Type()
)
snmpGeneralResetEngineIDCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralResetEngineIDCommand.setStatus("current")


class _SnmpGeneralSecurityPolicy_Type(Integer32):
    """Custom type snmpGeneralSecurityPolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("authentication", 2),
          ("authAndPrivacy", 3))
    )


_SnmpGeneralSecurityPolicy_Type.__name__ = "Integer32"
_SnmpGeneralSecurityPolicy_Object = MibScalar
snmpGeneralSecurityPolicy = _SnmpGeneralSecurityPolicy_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 2, 8),
    _SnmpGeneralSecurityPolicy_Type()
)
snmpGeneralSecurityPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpGeneralSecurityPolicy.setStatus("current")
_SnmpUserList_ObjectIdentity = ObjectIdentity
snmpUserList = _SnmpUserList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3)
)
_SnmpUserTable_Object = MibTable
snmpUserTable = _SnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1)
)
if mibBuilder.loadTexts:
    snmpUserTable.setStatus("current")
_SnmpUserEntry_Object = MibTableRow
snmpUserEntry = _SnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1)
)
snmpUserEntry.setIndexNames(
    (0, "LUM-SNMP-MIB", "snmpUserIndex"),
)
if mibBuilder.loadTexts:
    snmpUserEntry.setStatus("current")


class _SnmpUserIndex_Type(Unsigned32):
    """Custom type snmpUserIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SnmpUserIndex_Type.__name__ = "Unsigned32"
_SnmpUserIndex_Object = MibTableColumn
snmpUserIndex = _SnmpUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 1),
    _SnmpUserIndex_Type()
)
snmpUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserIndex.setStatus("current")


class _SnmpUserName_Type(DisplayString):
    """Custom type snmpUserName based on DisplayString"""
    defaultValue = OctetString("oper")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnmpUserName_Type.__name__ = "DisplayString"
_SnmpUserName_Object = MibTableColumn
snmpUserName = _SnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 2),
    _SnmpUserName_Type()
)
snmpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpUserName.setStatus("current")


class _SnmpUserChangePassword_Type(CommandString):
    """Custom type snmpUserChangePassword based on CommandString"""
    defaultValue = OctetString("1234567890")


_SnmpUserChangePassword_Type.__name__ = "CommandString"
_SnmpUserChangePassword_Object = MibTableColumn
snmpUserChangePassword = _SnmpUserChangePassword_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 3),
    _SnmpUserChangePassword_Type()
)
snmpUserChangePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserChangePassword.setStatus("current")
_SnmpUserEngineId_Type = SnmpEngineID
_SnmpUserEngineId_Object = MibTableColumn
snmpUserEngineId = _SnmpUserEngineId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 4),
    _SnmpUserEngineId_Type()
)
snmpUserEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserEngineId.setStatus("current")
_SnmpUserAuthKey_Type = OctetString
_SnmpUserAuthKey_Object = MibTableColumn
snmpUserAuthKey = _SnmpUserAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 5),
    _SnmpUserAuthKey_Type()
)
snmpUserAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserAuthKey.setStatus("current")
_SnmpUserPrivKey_Type = OctetString
_SnmpUserPrivKey_Object = MibTableColumn
snmpUserPrivKey = _SnmpUserPrivKey_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 6),
    _SnmpUserPrivKey_Type()
)
snmpUserPrivKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserPrivKey.setStatus("current")


class _SnmpUserChangePrivPassword_Type(CommandString):
    """Custom type snmpUserChangePrivPassword based on CommandString"""
    defaultValue = OctetString("")


_SnmpUserChangePrivPassword_Type.__name__ = "CommandString"
_SnmpUserChangePrivPassword_Object = MibTableColumn
snmpUserChangePrivPassword = _SnmpUserChangePrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 7),
    _SnmpUserChangePrivPassword_Type()
)
snmpUserChangePrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpUserChangePrivPassword.setStatus("current")


class _SnmpUserPrivProtocol_Type(Integer32):
    """Custom type snmpUserPrivProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("aes128", 2))
    )


_SnmpUserPrivProtocol_Type.__name__ = "Integer32"
_SnmpUserPrivProtocol_Object = MibTableColumn
snmpUserPrivProtocol = _SnmpUserPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 2, 3, 1, 1, 8),
    _SnmpUserPrivProtocol_Type()
)
snmpUserPrivProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUserPrivProtocol.setStatus("current")

# Managed Objects groups

snmpInformSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 1)
)
snmpInformSinkGroup.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkIndex"),
        ("LUM-SNMP-MIB", "snmpInformSinkName"),
        ("LUM-SNMP-MIB", "snmpInformSinkAddr"),
        ("LUM-SNMP-MIB", "snmpInformSinkPort"),
        ("LUM-SNMP-MIB", "snmpInformSinkCommunity"),
        ("LUM-SNMP-MIB", "snmpInformSinkRowStatus"))
)
if mibBuilder.loadTexts:
    snmpInformSinkGroup.setStatus("deprecated")

snmpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 2)
)
snmpGeneralGroup.setObjects(
      *(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    snmpGeneralGroup.setStatus("deprecated")

snmpGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 3)
)
snmpGeneralGroupV2.setObjects(
      *(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralEngineID"))
)
if mibBuilder.loadTexts:
    snmpGeneralGroupV2.setStatus("deprecated")

snmpUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 4)
)
snmpUserGroup.setObjects(
      *(("LUM-SNMP-MIB", "snmpUserIndex"),
        ("LUM-SNMP-MIB", "snmpUserName"),
        ("LUM-SNMP-MIB", "snmpUserChangePassword"),
        ("LUM-SNMP-MIB", "snmpUserEngineId"),
        ("LUM-SNMP-MIB", "snmpUserAuthKey"))
)
if mibBuilder.loadTexts:
    snmpUserGroup.setStatus("deprecated")

snmpGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 5)
)
snmpGeneralGroupV3.setObjects(
      *(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralEngineID"),
        ("LUM-SNMP-MIB", "snmpGeneralCommunity"))
)
if mibBuilder.loadTexts:
    snmpGeneralGroupV3.setStatus("deprecated")

snmpInformSinkGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 6)
)
snmpInformSinkGroupV2.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkIndex"),
        ("LUM-SNMP-MIB", "snmpInformSinkName"),
        ("LUM-SNMP-MIB", "snmpInformSinkAddr"),
        ("LUM-SNMP-MIB", "snmpInformSinkPort"),
        ("LUM-SNMP-MIB", "snmpInformSinkCommunity"),
        ("LUM-SNMP-MIB", "snmpInformSinkRowStatus"),
        ("LUM-SNMP-MIB", "snmpInformSinkStorageType"),
        ("LUM-SNMP-MIB", "snmpInformSinkAlarmNotifications"),
        ("LUM-SNMP-MIB", "snmpInformSinkPerformanceNotifications"),
        ("LUM-SNMP-MIB", "snmpInformSinkOtherNotifications"))
)
if mibBuilder.loadTexts:
    snmpInformSinkGroupV2.setStatus("deprecated")

snmpGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 7)
)
snmpGeneralGroupV4.setObjects(
      *(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralEngineID"),
        ("LUM-SNMP-MIB", "snmpGeneralCommunity"),
        ("LUM-SNMP-MIB", "snmpGeneralInformSinkTableSize"),
        ("LUM-SNMP-MIB", "snmpGeneralUserTableSize"))
)
if mibBuilder.loadTexts:
    snmpGeneralGroupV4.setStatus("deprecated")

snmpInformSinkGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 8)
)
snmpInformSinkGroupV3.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkIndex"),
        ("LUM-SNMP-MIB", "snmpInformSinkName"),
        ("LUM-SNMP-MIB", "snmpInformSinkAddr"),
        ("LUM-SNMP-MIB", "snmpInformSinkPort"),
        ("LUM-SNMP-MIB", "snmpInformSinkCommunity"),
        ("LUM-SNMP-MIB", "snmpInformSinkRowStatus"),
        ("LUM-SNMP-MIB", "snmpInformSinkStorageType"),
        ("LUM-SNMP-MIB", "snmpInformSinkAlarmNotifications"),
        ("LUM-SNMP-MIB", "snmpInformSinkPerformanceNotifications"),
        ("LUM-SNMP-MIB", "snmpInformSinkOtherNotifications"),
        ("LUM-SNMP-MIB", "snmpInformSinkMib2Notifications"))
)
if mibBuilder.loadTexts:
    snmpInformSinkGroupV3.setStatus("current")

snmpGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 9)
)
snmpGeneralGroupV5.setObjects(
      *(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralEngineID"),
        ("LUM-SNMP-MIB", "snmpGeneralCommunity"),
        ("LUM-SNMP-MIB", "snmpGeneralInformSinkTableSize"),
        ("LUM-SNMP-MIB", "snmpGeneralUserTableSize"),
        ("LUM-SNMP-MIB", "snmpGeneralResetEngineIDCommand"))
)
if mibBuilder.loadTexts:
    snmpGeneralGroupV5.setStatus("deprecated")

snmpGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 10)
)
snmpGeneralGroupV6.setObjects(
      *(("LUM-SNMP-MIB", "snmpGeneralLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralConfigLastChangeTime"),
        ("LUM-SNMP-MIB", "snmpGeneralEngineID"),
        ("LUM-SNMP-MIB", "snmpGeneralCommunity"),
        ("LUM-SNMP-MIB", "snmpGeneralInformSinkTableSize"),
        ("LUM-SNMP-MIB", "snmpGeneralUserTableSize"),
        ("LUM-SNMP-MIB", "snmpGeneralResetEngineIDCommand"),
        ("LUM-SNMP-MIB", "snmpGeneralSecurityPolicy"))
)
if mibBuilder.loadTexts:
    snmpGeneralGroupV6.setStatus("current")

snmpUserGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 1, 11)
)
snmpUserGroupV2.setObjects(
      *(("LUM-SNMP-MIB", "snmpUserIndex"),
        ("LUM-SNMP-MIB", "snmpUserName"),
        ("LUM-SNMP-MIB", "snmpUserChangePassword"),
        ("LUM-SNMP-MIB", "snmpUserEngineId"),
        ("LUM-SNMP-MIB", "snmpUserAuthKey"),
        ("LUM-SNMP-MIB", "snmpUserPrivKey"),
        ("LUM-SNMP-MIB", "snmpUserChangePrivPassword"),
        ("LUM-SNMP-MIB", "snmpUserPrivProtocol"))
)
if mibBuilder.loadTexts:
    snmpUserGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumSnmpBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 1)
)
lumSnmpBasicComplV1.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroup"),
        ("LUM-SNMP-MIB", "snmpGeneralGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV1.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 2)
)
lumSnmpBasicComplV2.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroup"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV2"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV2.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 3)
)
lumSnmpBasicComplV3.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroup"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV2"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV3.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 4)
)
lumSnmpBasicComplV4.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroup"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV3"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV4.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 5)
)
lumSnmpBasicComplV5.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroupV2"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV3"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV5.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 6)
)
lumSnmpBasicComplV6.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroupV2"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV4"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV6.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 7)
)
lumSnmpBasicComplV7.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV4"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV7.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 8)
)
lumSnmpBasicComplV8.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV5"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV8.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 9)
)
lumSnmpBasicComplV9.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV5"),
        ("LUM-SNMP-MIB", "snmpUserGroup"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV9.setStatus(
        "deprecated"
    )

lumSnmpBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 17, 1, 2, 10)
)
lumSnmpBasicComplV10.setObjects(
      *(("LUM-SNMP-MIB", "snmpInformSinkGroupV3"),
        ("LUM-SNMP-MIB", "snmpGeneralGroupV6"),
        ("LUM-SNMP-MIB", "snmpUserGroupV2"))
)
if mibBuilder.loadTexts:
    lumSnmpBasicComplV10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SNMP-MIB",
    **{"lumSnmpMIBModule": lumSnmpMIBModule,
       "lumSnmpConfs": lumSnmpConfs,
       "lumSnmpGroups": lumSnmpGroups,
       "snmpInformSinkGroup": snmpInformSinkGroup,
       "snmpGeneralGroup": snmpGeneralGroup,
       "snmpGeneralGroupV2": snmpGeneralGroupV2,
       "snmpUserGroup": snmpUserGroup,
       "snmpGeneralGroupV3": snmpGeneralGroupV3,
       "snmpInformSinkGroupV2": snmpInformSinkGroupV2,
       "snmpGeneralGroupV4": snmpGeneralGroupV4,
       "snmpInformSinkGroupV3": snmpInformSinkGroupV3,
       "snmpGeneralGroupV5": snmpGeneralGroupV5,
       "snmpGeneralGroupV6": snmpGeneralGroupV6,
       "snmpUserGroupV2": snmpUserGroupV2,
       "lumSnmpCompl": lumSnmpCompl,
       "lumSnmpBasicComplV1": lumSnmpBasicComplV1,
       "lumSnmpBasicComplV2": lumSnmpBasicComplV2,
       "lumSnmpBasicComplV3": lumSnmpBasicComplV3,
       "lumSnmpBasicComplV4": lumSnmpBasicComplV4,
       "lumSnmpBasicComplV5": lumSnmpBasicComplV5,
       "lumSnmpBasicComplV6": lumSnmpBasicComplV6,
       "lumSnmpBasicComplV7": lumSnmpBasicComplV7,
       "lumSnmpBasicComplV8": lumSnmpBasicComplV8,
       "lumSnmpBasicComplV9": lumSnmpBasicComplV9,
       "lumSnmpBasicComplV10": lumSnmpBasicComplV10,
       "lumSnmpMIBObjects": lumSnmpMIBObjects,
       "snmpInformSinkList": snmpInformSinkList,
       "snmpInformSinkTable": snmpInformSinkTable,
       "snmpInformSinkEntry": snmpInformSinkEntry,
       "snmpInformSinkIndex": snmpInformSinkIndex,
       "snmpInformSinkName": snmpInformSinkName,
       "snmpInformSinkAddr": snmpInformSinkAddr,
       "snmpInformSinkPort": snmpInformSinkPort,
       "snmpInformSinkCommunity": snmpInformSinkCommunity,
       "snmpInformSinkRowStatus": snmpInformSinkRowStatus,
       "snmpInformSinkStorageType": snmpInformSinkStorageType,
       "snmpInformSinkAlarmNotifications": snmpInformSinkAlarmNotifications,
       "snmpInformSinkPerformanceNotifications": snmpInformSinkPerformanceNotifications,
       "snmpInformSinkOtherNotifications": snmpInformSinkOtherNotifications,
       "snmpInformSinkMib2Notifications": snmpInformSinkMib2Notifications,
       "snmpGeneral": snmpGeneral,
       "snmpGeneralLastChangeTime": snmpGeneralLastChangeTime,
       "snmpGeneralConfigLastChangeTime": snmpGeneralConfigLastChangeTime,
       "snmpGeneralEngineID": snmpGeneralEngineID,
       "snmpGeneralCommunity": snmpGeneralCommunity,
       "snmpGeneralInformSinkTableSize": snmpGeneralInformSinkTableSize,
       "snmpGeneralUserTableSize": snmpGeneralUserTableSize,
       "snmpGeneralResetEngineIDCommand": snmpGeneralResetEngineIDCommand,
       "snmpGeneralSecurityPolicy": snmpGeneralSecurityPolicy,
       "snmpUserList": snmpUserList,
       "snmpUserTable": snmpUserTable,
       "snmpUserEntry": snmpUserEntry,
       "snmpUserIndex": snmpUserIndex,
       "snmpUserName": snmpUserName,
       "snmpUserChangePassword": snmpUserChangePassword,
       "snmpUserEngineId": snmpUserEngineId,
       "snmpUserAuthKey": snmpUserAuthKey,
       "snmpUserPrivKey": snmpUserPrivKey,
       "snmpUserChangePrivPassword": snmpUserChangePrivPassword,
       "snmpUserPrivProtocol": snmpUserPrivProtocol}
)
