# SNMP MIB module (ALVARION-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/ALVARION-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:04 2025
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionNotificationEnable,) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionNotificationEnable")

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

alvarionSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogSeverity(TextualConvention, Integer32):
    status = "current"
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )



# MIB Managed Objects in the order of their OIDs

_AlvarionSyslogMIBObjects_ObjectIdentity = ObjectIdentity
alvarionSyslogMIBObjects = _AlvarionSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1)
)
_SyslogConfig_ObjectIdentity = ObjectIdentity
syslogConfig = _SyslogConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1)
)


class _SyslogSeverityNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type syslogSeverityNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 1


_SyslogSeverityNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_SyslogSeverityNotificationEnabled_Object = MibScalar
syslogSeverityNotificationEnabled = _SyslogSeverityNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 1),
    _SyslogSeverityNotificationEnabled_Type()
)
syslogSeverityNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSeverityNotificationEnabled.setStatus("current")


class _SyslogRegExMatchNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type syslogRegExMatchNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_SyslogRegExMatchNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_SyslogRegExMatchNotificationEnabled_Object = MibScalar
syslogRegExMatchNotificationEnabled = _SyslogRegExMatchNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 2),
    _SyslogRegExMatchNotificationEnabled_Type()
)
syslogRegExMatchNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogRegExMatchNotificationEnabled.setStatus("current")


class _SyslogSeverityLevel_Type(SyslogSeverity):
    """Custom type syslogSeverityLevel based on SyslogSeverity"""
    defaultValue = 5


_SyslogSeverityLevel_Type.__name__ = "SyslogSeverity"
_SyslogSeverityLevel_Object = MibScalar
syslogSeverityLevel = _SyslogSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 3),
    _SyslogSeverityLevel_Type()
)
syslogSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogSeverityLevel.setStatus("current")


class _SyslogTrapSeverityLevel_Type(SyslogSeverity):
    """Custom type syslogTrapSeverityLevel based on SyslogSeverity"""
    defaultValue = 5


_SyslogTrapSeverityLevel_Type.__name__ = "SyslogSeverity"
_SyslogTrapSeverityLevel_Object = MibScalar
syslogTrapSeverityLevel = _SyslogTrapSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 4),
    _SyslogTrapSeverityLevel_Type()
)
syslogTrapSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogTrapSeverityLevel.setStatus("current")
_SyslogMessageRegEx_Type = DisplayString
_SyslogMessageRegEx_Object = MibScalar
syslogMessageRegEx = _SyslogMessageRegEx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 1, 5),
    _SyslogMessageRegEx_Type()
)
syslogMessageRegEx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogMessageRegEx.setStatus("current")
_SyslogMessage_ObjectIdentity = ObjectIdentity
syslogMessage = _SyslogMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2)
)
_SyslogMsgNumber_Type = Unsigned32
_SyslogMsgNumber_Object = MibScalar
syslogMsgNumber = _SyslogMsgNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 1),
    _SyslogMsgNumber_Type()
)
syslogMsgNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgNumber.setStatus("current")
_SyslogMsgFacility_Type = DisplayString
_SyslogMsgFacility_Object = MibScalar
syslogMsgFacility = _SyslogMsgFacility_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 2),
    _SyslogMsgFacility_Type()
)
syslogMsgFacility.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgFacility.setStatus("current")
_SyslogMsgSeverity_Type = SyslogSeverity
_SyslogMsgSeverity_Object = MibScalar
syslogMsgSeverity = _SyslogMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 3),
    _SyslogMsgSeverity_Type()
)
syslogMsgSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgSeverity.setStatus("current")
_SyslogMsgText_Type = DisplayString
_SyslogMsgText_Object = MibScalar
syslogMsgText = _SyslogMsgText_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 1, 2, 4),
    _SyslogMsgText_Type()
)
syslogMsgText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogMsgText.setStatus("current")
_AlvarionSyslogMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionSyslogMIBNotificationPrefix = _AlvarionSyslogMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2)
)
_AlvarionSyslogMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionSyslogMIBNotifications = _AlvarionSyslogMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2, 0)
)
_AlvarionSyslogMIBConformance_ObjectIdentity = ObjectIdentity
alvarionSyslogMIBConformance = _AlvarionSyslogMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3)
)
_AlvarionSyslogMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionSyslogMIBCompliances = _AlvarionSyslogMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 1)
)
_AlvarionSyslogMIBGroups_ObjectIdentity = ObjectIdentity
alvarionSyslogMIBGroups = _AlvarionSyslogMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 2)
)

# Managed Objects groups

alvarionSyslogMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 2, 1)
)
alvarionSyslogMIBGroup.setObjects(
      *(("ALVARION-SYSLOG-MIB", "syslogSeverityNotificationEnabled"),
        ("ALVARION-SYSLOG-MIB", "syslogRegExMatchNotificationEnabled"),
        ("ALVARION-SYSLOG-MIB", "syslogSeverityLevel"),
        ("ALVARION-SYSLOG-MIB", "syslogTrapSeverityLevel"),
        ("ALVARION-SYSLOG-MIB", "syslogMessageRegEx"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgNumber"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgFacility"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgSeverity"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgText"))
)
if mibBuilder.loadTexts:
    alvarionSyslogMIBGroup.setStatus("current")


# Notification objects

syslogSeverityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2, 0, 1)
)
syslogSeverityNotification.setObjects(
      *(("ALVARION-SYSLOG-MIB", "syslogMsgNumber"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgFacility"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgSeverity"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgText"))
)
if mibBuilder.loadTexts:
    syslogSeverityNotification.setStatus(
        "current"
    )

syslogRegExMatchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 2, 0, 2)
)
syslogRegExMatchNotification.setObjects(
      *(("ALVARION-SYSLOG-MIB", "syslogMsgNumber"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgFacility"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgSeverity"),
        ("ALVARION-SYSLOG-MIB", "syslogMsgText"))
)
if mibBuilder.loadTexts:
    syslogRegExMatchNotification.setStatus(
        "current"
    )


# Notifications groups

alvarionSyslogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 2, 2)
)
alvarionSyslogNotificationGroup.setObjects(
      *(("ALVARION-SYSLOG-MIB", "syslogSeverityNotification"),
        ("ALVARION-SYSLOG-MIB", "syslogRegExMatchNotification"))
)
if mibBuilder.loadTexts:
    alvarionSyslogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alvarionSyslogMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 3, 3, 1, 1)
)
alvarionSyslogMIBCompliance.setObjects(
      *(("ALVARION-SYSLOG-MIB", "alvarionSyslogMIBGroup"),
        ("ALVARION-SYSLOG-MIB", "alvarionSyslogNotificationGroup"))
)
if mibBuilder.loadTexts:
    alvarionSyslogMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-SYSLOG-MIB",
    **{"SyslogSeverity": SyslogSeverity,
       "alvarionSyslogMIB": alvarionSyslogMIB,
       "alvarionSyslogMIBObjects": alvarionSyslogMIBObjects,
       "syslogConfig": syslogConfig,
       "syslogSeverityNotificationEnabled": syslogSeverityNotificationEnabled,
       "syslogRegExMatchNotificationEnabled": syslogRegExMatchNotificationEnabled,
       "syslogSeverityLevel": syslogSeverityLevel,
       "syslogTrapSeverityLevel": syslogTrapSeverityLevel,
       "syslogMessageRegEx": syslogMessageRegEx,
       "syslogMessage": syslogMessage,
       "syslogMsgNumber": syslogMsgNumber,
       "syslogMsgFacility": syslogMsgFacility,
       "syslogMsgSeverity": syslogMsgSeverity,
       "syslogMsgText": syslogMsgText,
       "alvarionSyslogMIBNotificationPrefix": alvarionSyslogMIBNotificationPrefix,
       "alvarionSyslogMIBNotifications": alvarionSyslogMIBNotifications,
       "syslogSeverityNotification": syslogSeverityNotification,
       "syslogRegExMatchNotification": syslogRegExMatchNotification,
       "alvarionSyslogMIBConformance": alvarionSyslogMIBConformance,
       "alvarionSyslogMIBCompliances": alvarionSyslogMIBCompliances,
       "alvarionSyslogMIBCompliance": alvarionSyslogMIBCompliance,
       "alvarionSyslogMIBGroups": alvarionSyslogMIBGroups,
       "alvarionSyslogMIBGroup": alvarionSyslogMIBGroup,
       "alvarionSyslogNotificationGroup": alvarionSyslogNotificationGroup}
)
