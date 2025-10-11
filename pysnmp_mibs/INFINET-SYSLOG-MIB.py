# SNMP MIB module (INFINET-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-SYSLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:09 2025
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

(sysSerialNumber,
 sysTrapSequence) = mibBuilder.importSymbols(
    "AQUASYSTEM-MIB",
    "sysSerialNumber",
    "sysTrapSequence")

(wanflex,) = mibBuilder.importSymbols(
    "INFINET-MIB",
    "wanflex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

infinetSyslogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6)
)
if mibBuilder.loadTexts:
    infinetSyslogMIB.setRevisions(
        ("2008-02-07 11:36",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class InfinetSyslogFacility(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("kernel", 0),
          ("user", 1),
          ("mail", 2),
          ("daemon", 3),
          ("authentication", 4),
          ("syslog", 5),
          ("lpr", 6),
          ("news", 7),
          ("uucp", 8),
          ("cron", 9),
          ("authpriv", 10),
          ("ftp", 11),
          ("ntp", 12),
          ("security", 13),
          ("console", 14),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23))
    )



class InfinetSyslogSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )



# MIB Managed Objects in the order of their OIDs

_InfinetSyslogObjects_ObjectIdentity = ObjectIdentity
infinetSyslogObjects = _InfinetSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1)
)
_InfinetSyslogServerAddress_Type = IpAddress
_InfinetSyslogServerAddress_Object = MibScalar
infinetSyslogServerAddress = _InfinetSyslogServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 1),
    _InfinetSyslogServerAddress_Type()
)
infinetSyslogServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    infinetSyslogServerAddress.setStatus("current")
_InfinetSyslogMessagesTable_Object = MibTable
infinetSyslogMessagesTable = _InfinetSyslogMessagesTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    infinetSyslogMessagesTable.setStatus("current")
_InfinetSyslogMessageEntry_Object = MibTableRow
infinetSyslogMessageEntry = _InfinetSyslogMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1)
)
infinetSyslogMessageEntry.setIndexNames(
    (0, "INFINET-SYSLOG-MIB", "infinetSyslogMessageIndex"),
)
if mibBuilder.loadTexts:
    infinetSyslogMessageEntry.setStatus("current")
_InfinetSyslogMessageIndex_Type = Counter32
_InfinetSyslogMessageIndex_Object = MibTableColumn
infinetSyslogMessageIndex = _InfinetSyslogMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 1),
    _InfinetSyslogMessageIndex_Type()
)
infinetSyslogMessageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infinetSyslogMessageIndex.setStatus("current")
_InfinetSyslogMessageSeverity_Type = InfinetSyslogSeverity
_InfinetSyslogMessageSeverity_Object = MibTableColumn
infinetSyslogMessageSeverity = _InfinetSyslogMessageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 2),
    _InfinetSyslogMessageSeverity_Type()
)
infinetSyslogMessageSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infinetSyslogMessageSeverity.setStatus("current")
_InfinetSyslogMessageFacility_Type = InfinetSyslogFacility
_InfinetSyslogMessageFacility_Object = MibTableColumn
infinetSyslogMessageFacility = _InfinetSyslogMessageFacility_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 3),
    _InfinetSyslogMessageFacility_Type()
)
infinetSyslogMessageFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infinetSyslogMessageFacility.setStatus("current")
_InfinetSyslogMessageTimestamp_Type = DateAndTime
_InfinetSyslogMessageTimestamp_Object = MibTableColumn
infinetSyslogMessageTimestamp = _InfinetSyslogMessageTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 4),
    _InfinetSyslogMessageTimestamp_Type()
)
infinetSyslogMessageTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infinetSyslogMessageTimestamp.setStatus("current")
_InfinetSyslogMessageIdentity_Type = DisplayString
_InfinetSyslogMessageIdentity_Object = MibTableColumn
infinetSyslogMessageIdentity = _InfinetSyslogMessageIdentity_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 5),
    _InfinetSyslogMessageIdentity_Type()
)
infinetSyslogMessageIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infinetSyslogMessageIdentity.setStatus("current")


class _InfinetSyslogMessageText_Type(DisplayString):
    """Custom type infinetSyslogMessageText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_InfinetSyslogMessageText_Type.__name__ = "DisplayString"
_InfinetSyslogMessageText_Object = MibTableColumn
infinetSyslogMessageText = _InfinetSyslogMessageText_Object(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 1, 2, 1, 6),
    _InfinetSyslogMessageText_Type()
)
infinetSyslogMessageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    infinetSyslogMessageText.setStatus("current")
_InfinetSyslogEventsPrefix_ObjectIdentity = ObjectIdentity
infinetSyslogEventsPrefix = _InfinetSyslogEventsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 2)
)
_InfinetSyslogEvents_ObjectIdentity = ObjectIdentity
infinetSyslogEvents = _InfinetSyslogEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 2, 0)
)
_InfinetSyslogConf_ObjectIdentity = ObjectIdentity
infinetSyslogConf = _InfinetSyslogConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3)
)
_InfinetSyslogGroups_ObjectIdentity = ObjectIdentity
infinetSyslogGroups = _InfinetSyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 1)
)
_InfinetSyslogCompls_ObjectIdentity = ObjectIdentity
infinetSyslogCompls = _InfinetSyslogCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 2)
)

# Managed Objects groups

infinetSyslogBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 1, 1)
)
infinetSyslogBasicGroup.setObjects(
      *(("INFINET-SYSLOG-MIB", "infinetSyslogServerAddress"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIndex"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageSeverity"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageText"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageFacility"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageTimestamp"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIdentity"))
)
if mibBuilder.loadTexts:
    infinetSyslogBasicGroup.setStatus("current")


# Notification objects

infinetSyslogMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 2, 0, 1)
)
infinetSyslogMessageGenerated.setObjects(
      *(("AQUASYSTEM-MIB", "sysSerialNumber"),
        ("AQUASYSTEM-MIB", "sysTrapSequence"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIndex"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageSeverity"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageFacility"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageTimestamp"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageIdentity"),
        ("INFINET-SYSLOG-MIB", "infinetSyslogMessageText"))
)
if mibBuilder.loadTexts:
    infinetSyslogMessageGenerated.setStatus(
        "current"
    )


# Notifications groups

infinetSyslogBasicEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3942, 1, 1, 6, 3, 1, 2)
)
infinetSyslogBasicEvents.setObjects(
    ("INFINET-SYSLOG-MIB", "infinetSyslogMessageGenerated")
)
if mibBuilder.loadTexts:
    infinetSyslogBasicEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-SYSLOG-MIB",
    **{"InfinetSyslogFacility": InfinetSyslogFacility,
       "InfinetSyslogSeverity": InfinetSyslogSeverity,
       "infinetSyslogMIB": infinetSyslogMIB,
       "infinetSyslogObjects": infinetSyslogObjects,
       "infinetSyslogServerAddress": infinetSyslogServerAddress,
       "infinetSyslogMessagesTable": infinetSyslogMessagesTable,
       "infinetSyslogMessageEntry": infinetSyslogMessageEntry,
       "infinetSyslogMessageIndex": infinetSyslogMessageIndex,
       "infinetSyslogMessageSeverity": infinetSyslogMessageSeverity,
       "infinetSyslogMessageFacility": infinetSyslogMessageFacility,
       "infinetSyslogMessageTimestamp": infinetSyslogMessageTimestamp,
       "infinetSyslogMessageIdentity": infinetSyslogMessageIdentity,
       "infinetSyslogMessageText": infinetSyslogMessageText,
       "infinetSyslogEventsPrefix": infinetSyslogEventsPrefix,
       "infinetSyslogEvents": infinetSyslogEvents,
       "infinetSyslogMessageGenerated": infinetSyslogMessageGenerated,
       "infinetSyslogConf": infinetSyslogConf,
       "infinetSyslogGroups": infinetSyslogGroups,
       "infinetSyslogBasicGroup": infinetSyslogBasicGroup,
       "infinetSyslogBasicEvents": infinetSyslogBasicEvents,
       "infinetSyslogCompls": infinetSyslogCompls}
)
