# SNMP MIB module (OS-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:33 2025
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

(adva,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "adva")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

osSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7)
)
if mibBuilder.loadTexts:
    osSnmp.setRevisions(
        ("2020-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsSnmpNotificationObjects_ObjectIdentity = ObjectIdentity
osSnmpNotificationObjects = _OsSnmpNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1)
)
_OsSnmpChangeSourceAddress_Type = DisplayString
_OsSnmpChangeSourceAddress_Object = MibScalar
osSnmpChangeSourceAddress = _OsSnmpChangeSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 1),
    _OsSnmpChangeSourceAddress_Type()
)
osSnmpChangeSourceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osSnmpChangeSourceAddress.setStatus("current")
_OsSnmpChangeV2Community_Type = DisplayString
_OsSnmpChangeV2Community_Object = MibScalar
osSnmpChangeV2Community = _OsSnmpChangeV2Community_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 2),
    _OsSnmpChangeV2Community_Type()
)
osSnmpChangeV2Community.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osSnmpChangeV2Community.setStatus("current")
_OsSnmpChangeV3User_Type = DisplayString
_OsSnmpChangeV3User_Object = MibScalar
osSnmpChangeV3User = _OsSnmpChangeV3User_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 3),
    _OsSnmpChangeV3User_Type()
)
osSnmpChangeV3User.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osSnmpChangeV3User.setStatus("current")
_OsSnmpChangeCliUser_Type = DisplayString
_OsSnmpChangeCliUser_Object = MibScalar
osSnmpChangeCliUser = _OsSnmpChangeCliUser_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 4),
    _OsSnmpChangeCliUser_Type()
)
osSnmpChangeCliUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osSnmpChangeCliUser.setStatus("current")
_OsSnmpChangeCliCommand_Type = DisplayString
_OsSnmpChangeCliCommand_Object = MibScalar
osSnmpChangeCliCommand = _OsSnmpChangeCliCommand_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 5),
    _OsSnmpChangeCliCommand_Type()
)
osSnmpChangeCliCommand.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osSnmpChangeCliCommand.setStatus("current")
_OsSnmpChangeCliNodeName_Type = DisplayString
_OsSnmpChangeCliNodeName_Object = MibScalar
osSnmpChangeCliNodeName = _OsSnmpChangeCliNodeName_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 1, 6),
    _OsSnmpChangeCliNodeName_Type()
)
osSnmpChangeCliNodeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    osSnmpChangeCliNodeName.setStatus("current")
_OsSnmpCfg_ObjectIdentity = ObjectIdentity
osSnmpCfg = _OsSnmpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 2)
)


class _OsSnmpAlarmMangerMode_Type(Integer32):
    """Custom type osSnmpAlarmMangerMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_OsSnmpAlarmMangerMode_Type.__name__ = "Integer32"
_OsSnmpAlarmMangerMode_Object = MibScalar
osSnmpAlarmMangerMode = _OsSnmpAlarmMangerMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 2, 1),
    _OsSnmpAlarmMangerMode_Type()
)
osSnmpAlarmMangerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSnmpAlarmMangerMode.setStatus("current")


class _OsSnmpChangeLogMode_Type(Integer32):
    """Custom type osSnmpChangeLogMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_OsSnmpChangeLogMode_Type.__name__ = "Integer32"
_OsSnmpChangeLogMode_Object = MibScalar
osSnmpChangeLogMode = _OsSnmpChangeLogMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 2, 2),
    _OsSnmpChangeLogMode_Type()
)
osSnmpChangeLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osSnmpChangeLogMode.setStatus("current")
_OsSnmpConformance_ObjectIdentity = ObjectIdentity
osSnmpConformance = _OsSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 100)
)
_OsSnmpMIBCompliances_ObjectIdentity = ObjectIdentity
osSnmpMIBCompliances = _OsSnmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 1)
)
_OsSnmpMIBGroups_ObjectIdentity = ObjectIdentity
osSnmpMIBGroups = _OsSnmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 2)
)

# Managed Objects groups

osSnmpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 2, 1)
)
osSnmpMandatoryGroup.setObjects(
      *(("OS-SNMP-MIB", "osSnmpChangeSourceAddress"),
        ("OS-SNMP-MIB", "osSnmpChangeV2Community"),
        ("OS-SNMP-MIB", "osSnmpChangeV3User"),
        ("OS-SNMP-MIB", "osSnmpChangeCliUser"),
        ("OS-SNMP-MIB", "osSnmpChangeCliCommand"),
        ("OS-SNMP-MIB", "osSnmpChangeCliNodeName"),
        ("OS-SNMP-MIB", "osSnmpAlarmMangerMode"),
        ("OS-SNMP-MIB", "osSnmpChangeLogMode"))
)
if mibBuilder.loadTexts:
    osSnmpMandatoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osSnmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 2544, 7, 100, 1, 1)
)
osSnmpMIBCompliance.setObjects(
    ("OS-SNMP-MIB", "osSnmpMandatoryGroup")
)
if mibBuilder.loadTexts:
    osSnmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-SNMP-MIB",
    **{"osSnmp": osSnmp,
       "osSnmpNotificationObjects": osSnmpNotificationObjects,
       "osSnmpChangeSourceAddress": osSnmpChangeSourceAddress,
       "osSnmpChangeV2Community": osSnmpChangeV2Community,
       "osSnmpChangeV3User": osSnmpChangeV3User,
       "osSnmpChangeCliUser": osSnmpChangeCliUser,
       "osSnmpChangeCliCommand": osSnmpChangeCliCommand,
       "osSnmpChangeCliNodeName": osSnmpChangeCliNodeName,
       "osSnmpCfg": osSnmpCfg,
       "osSnmpAlarmMangerMode": osSnmpAlarmMangerMode,
       "osSnmpChangeLogMode": osSnmpChangeLogMode,
       "osSnmpConformance": osSnmpConformance,
       "osSnmpMIBCompliances": osSnmpMIBCompliances,
       "osSnmpMIBCompliance": osSnmpMIBCompliance,
       "osSnmpMIBGroups": osSnmpMIBGroups,
       "osSnmpMandatoryGroup": osSnmpMandatoryGroup}
)
