# SNMP MIB module (TPT-NGFW-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-NGFW-LOGGING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:02 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(Severity,
 tpt_ngfw_compls,
 tpt_ngfw_eventsV2,
 tpt_ngfw_groups,
 tpt_ngfw_objs,
 tpt_ngfw_params) = mibBuilder.importSymbols(
    "TPT-NGFW-REG-MIB",
    "Severity",
    "tpt-ngfw-compls",
    "tpt-ngfw-eventsV2",
    "tpt-ngfw-groups",
    "tpt-ngfw-objs",
    "tpt-ngfw-params")

(tptNgfwSystemSerial,) = mibBuilder.importSymbols(
    "TPT-NGFW-SYSTEM-INFO-MIB",
    "tptNgfwSystemSerial")


# MODULE-IDENTITY

tptNgfwLogging = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 2, 5)
)
if mibBuilder.loadTexts:
    tptNgfwLogging.setRevisions(
        ("2016-05-25 18:54",
         "2013-03-13 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AuditLogResult(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failed", 2))
    )



class AuditLogCategory(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("general", 2),
          ("login", 3),
          ("logout", 4),
          ("user", 5),
          ("time", 6),
          ("policy", 7),
          ("update", 8),
          ("boot", 9),
          ("report", 10),
          ("host", 11),
          ("cfg", 12),
          ("device", 13),
          ("sms", 14),
          ("server", 15),
          ("segment", 16),
          ("license", 17),
          ("ha", 18),
          ("monitor", 19),
          ("ipFilter", 20),
          ("connTable", 21),
          ("hostComm", 22),
          ("tse", 23),
          ("cf", 24))
    )



# MIB Managed Objects in the order of their OIDs

_TptNgfwLogNotifyTime_Type = DateAndTime
_TptNgfwLogNotifyTime_Object = MibScalar
tptNgfwLogNotifyTime = _TptNgfwLogNotifyTime_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 60),
    _TptNgfwLogNotifyTime_Type()
)
tptNgfwLogNotifyTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwLogNotifyTime.setStatus("current")


class _TptNgfwLogNotifyHost_Type(SnmpAdminString):
    """Custom type tptNgfwLogNotifyHost based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TptNgfwLogNotifyHost_Type.__name__ = "SnmpAdminString"
_TptNgfwLogNotifyHost_Object = MibScalar
tptNgfwLogNotifyHost = _TptNgfwLogNotifyHost_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 61),
    _TptNgfwLogNotifyHost_Type()
)
tptNgfwLogNotifyHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwLogNotifyHost.setStatus("current")


class _TptNgfwLogNotifySource_Type(SnmpAdminString):
    """Custom type tptNgfwLogNotifySource based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwLogNotifySource_Type.__name__ = "SnmpAdminString"
_TptNgfwLogNotifySource_Object = MibScalar
tptNgfwLogNotifySource = _TptNgfwLogNotifySource_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 62),
    _TptNgfwLogNotifySource_Type()
)
tptNgfwLogNotifySource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwLogNotifySource.setStatus("current")
_TptNgfwLogNotifySeverity_Type = Severity
_TptNgfwLogNotifySeverity_Object = MibScalar
tptNgfwLogNotifySeverity = _TptNgfwLogNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 63),
    _TptNgfwLogNotifySeverity_Type()
)
tptNgfwLogNotifySeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwLogNotifySeverity.setStatus("current")


class _TptNgfwLogNotifyText_Type(SnmpAdminString):
    """Custom type tptNgfwLogNotifyText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_TptNgfwLogNotifyText_Type.__name__ = "SnmpAdminString"
_TptNgfwLogNotifyText_Object = MibScalar
tptNgfwLogNotifyText = _TptNgfwLogNotifyText_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 64),
    _TptNgfwLogNotifyText_Type()
)
tptNgfwLogNotifyText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwLogNotifyText.setStatus("current")
_TptNgfwAuditLogNotifyAccess_Type = Unsigned32
_TptNgfwAuditLogNotifyAccess_Object = MibScalar
tptNgfwAuditLogNotifyAccess = _TptNgfwAuditLogNotifyAccess_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 65),
    _TptNgfwAuditLogNotifyAccess_Type()
)
tptNgfwAuditLogNotifyAccess.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyAccess.setStatus("current")


class _TptNgfwAuditLogNotifyType_Type(SnmpAdminString):
    """Custom type tptNgfwAuditLogNotifyType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptNgfwAuditLogNotifyType_Type.__name__ = "SnmpAdminString"
_TptNgfwAuditLogNotifyType_Object = MibScalar
tptNgfwAuditLogNotifyType = _TptNgfwAuditLogNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 66),
    _TptNgfwAuditLogNotifyType_Type()
)
tptNgfwAuditLogNotifyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyType.setStatus("current")
_TptNgfwAuditLogNotifyIpAddrType_Type = InetAddressType
_TptNgfwAuditLogNotifyIpAddrType_Object = MibScalar
tptNgfwAuditLogNotifyIpAddrType = _TptNgfwAuditLogNotifyIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 67),
    _TptNgfwAuditLogNotifyIpAddrType_Type()
)
tptNgfwAuditLogNotifyIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyIpAddrType.setStatus("current")
_TptNgfwAuditLogNotifyIpAddr_Type = InetAddress
_TptNgfwAuditLogNotifyIpAddr_Object = MibScalar
tptNgfwAuditLogNotifyIpAddr = _TptNgfwAuditLogNotifyIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 68),
    _TptNgfwAuditLogNotifyIpAddr_Type()
)
tptNgfwAuditLogNotifyIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyIpAddr.setStatus("current")
_TptNgfwAuditLogNotifyCategory_Type = AuditLogCategory
_TptNgfwAuditLogNotifyCategory_Object = MibScalar
tptNgfwAuditLogNotifyCategory = _TptNgfwAuditLogNotifyCategory_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 69),
    _TptNgfwAuditLogNotifyCategory_Type()
)
tptNgfwAuditLogNotifyCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyCategory.setStatus("current")
_TptNgfwAuditLogNotifyResult_Type = AuditLogResult
_TptNgfwAuditLogNotifyResult_Object = MibScalar
tptNgfwAuditLogNotifyResult = _TptNgfwAuditLogNotifyResult_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 70),
    _TptNgfwAuditLogNotifyResult_Type()
)
tptNgfwAuditLogNotifyResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyResult.setStatus("current")


class _TptNgfwAuditLogNotifyUser_Type(SnmpAdminString):
    """Custom type tptNgfwAuditLogNotifyUser based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_TptNgfwAuditLogNotifyUser_Type.__name__ = "SnmpAdminString"
_TptNgfwAuditLogNotifyUser_Object = MibScalar
tptNgfwAuditLogNotifyUser = _TptNgfwAuditLogNotifyUser_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 71),
    _TptNgfwAuditLogNotifyUser_Type()
)
tptNgfwAuditLogNotifyUser.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyUser.setStatus("current")


class _TptNgfwAuditLogNotifyMessage_Type(SnmpAdminString):
    """Custom type tptNgfwAuditLogNotifyMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )


_TptNgfwAuditLogNotifyMessage_Type.__name__ = "SnmpAdminString"
_TptNgfwAuditLogNotifyMessage_Object = MibScalar
tptNgfwAuditLogNotifyMessage = _TptNgfwAuditLogNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 1, 72),
    _TptNgfwAuditLogNotifyMessage_Type()
)
tptNgfwAuditLogNotifyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotifyMessage.setStatus("current")

# Managed Objects groups

tptNgfwLoggingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 9)
)
tptNgfwLoggingGroup.setObjects(
      *(("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyHost"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyAccess"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyType"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddrType"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddr"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyCategory"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyResult"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyUser"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyMessage"))
)
if mibBuilder.loadTexts:
    tptNgfwLoggingGroup.setStatus("current")


# Notification objects

tptNgfwSysLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 15)
)
tptNgfwSysLogNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyHost"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"))
)
if mibBuilder.loadTexts:
    tptNgfwSysLogNotify.setStatus(
        "current"
    )

tptNgfwAuditLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 16)
)
tptNgfwAuditLogNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyAccess"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyType"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddrType"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyIpAddr"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyCategory"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyResult"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyUser"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotifyMessage"))
)
if mibBuilder.loadTexts:
    tptNgfwAuditLogNotify.setStatus(
        "current"
    )

tptNgfwVpnLogNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 3, 0, 17)
)
tptNgfwVpnLogNotify.setObjects(
      *(("TPT-NGFW-SYSTEM-INFO-MIB", "tptNgfwSystemSerial"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyTime"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySeverity"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifySource"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLogNotifyText"))
)
if mibBuilder.loadTexts:
    tptNgfwVpnLogNotify.setStatus(
        "current"
    )


# Notifications groups

tptNgfwLoggingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 1, 10)
)
tptNgfwLoggingNotificationGroup.setObjects(
      *(("TPT-NGFW-LOGGING-MIB", "tptNgfwSysLogNotify"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwAuditLogNotify"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwVpnLogNotify"))
)
if mibBuilder.loadTexts:
    tptNgfwLoggingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tptNgfwLoggingCompl = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10734, 3, 9, 1, 2, 3)
)
tptNgfwLoggingCompl.setObjects(
      *(("TPT-NGFW-LOGGING-MIB", "tptNgfwLoggingGroup"),
        ("TPT-NGFW-LOGGING-MIB", "tptNgfwLoggingNotificationGroup"))
)
if mibBuilder.loadTexts:
    tptNgfwLoggingCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-NGFW-LOGGING-MIB",
    **{"AuditLogResult": AuditLogResult,
       "AuditLogCategory": AuditLogCategory,
       "tptNgfwLoggingGroup": tptNgfwLoggingGroup,
       "tptNgfwLoggingNotificationGroup": tptNgfwLoggingNotificationGroup,
       "tptNgfwLoggingCompl": tptNgfwLoggingCompl,
       "tptNgfwLogging": tptNgfwLogging,
       "tptNgfwSysLogNotify": tptNgfwSysLogNotify,
       "tptNgfwAuditLogNotify": tptNgfwAuditLogNotify,
       "tptNgfwVpnLogNotify": tptNgfwVpnLogNotify,
       "tptNgfwLogNotifyTime": tptNgfwLogNotifyTime,
       "tptNgfwLogNotifyHost": tptNgfwLogNotifyHost,
       "tptNgfwLogNotifySource": tptNgfwLogNotifySource,
       "tptNgfwLogNotifySeverity": tptNgfwLogNotifySeverity,
       "tptNgfwLogNotifyText": tptNgfwLogNotifyText,
       "tptNgfwAuditLogNotifyAccess": tptNgfwAuditLogNotifyAccess,
       "tptNgfwAuditLogNotifyType": tptNgfwAuditLogNotifyType,
       "tptNgfwAuditLogNotifyIpAddrType": tptNgfwAuditLogNotifyIpAddrType,
       "tptNgfwAuditLogNotifyIpAddr": tptNgfwAuditLogNotifyIpAddr,
       "tptNgfwAuditLogNotifyCategory": tptNgfwAuditLogNotifyCategory,
       "tptNgfwAuditLogNotifyResult": tptNgfwAuditLogNotifyResult,
       "tptNgfwAuditLogNotifyUser": tptNgfwAuditLogNotifyUser,
       "tptNgfwAuditLogNotifyMessage": tptNgfwAuditLogNotifyMessage}
)
