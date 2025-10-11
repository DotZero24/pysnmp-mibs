# SNMP MIB module (G6-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:19 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ntp_ObjectIdentity = ObjectIdentity
ntp = _Ntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73)
)


class _NtpEnableNtp_Type(Integer32):
    """Custom type ntpEnableNtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpEnableNtp_Type.__name__ = "Integer32"
_NtpEnableNtp_Object = MibScalar
ntpEnableNtp = _NtpEnableNtp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 1),
    _NtpEnableNtp_Type()
)
ntpEnableNtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpEnableNtp.setStatus("current")
_NtpSyncNow_Type = DisplayString
_NtpSyncNow_Object = MibScalar
ntpSyncNow = _NtpSyncNow_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 2),
    _NtpSyncNow_Type()
)
ntpSyncNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSyncNow.setStatus("current")


class _NtpDhcpProvidesNtpServer_Type(Integer32):
    """Custom type ntpDhcpProvidesNtpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpDhcpProvidesNtpServer_Type.__name__ = "Integer32"
_NtpDhcpProvidesNtpServer_Object = MibScalar
ntpDhcpProvidesNtpServer = _NtpDhcpProvidesNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 3),
    _NtpDhcpProvidesNtpServer_Type()
)
ntpDhcpProvidesNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpDhcpProvidesNtpServer.setStatus("current")
_NtpMainNtpServer_Type = DisplayString
_NtpMainNtpServer_Object = MibScalar
ntpMainNtpServer = _NtpMainNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 4),
    _NtpMainNtpServer_Type()
)
ntpMainNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpMainNtpServer.setStatus("current")
_NtpBackupNtpServer_Type = DisplayString
_NtpBackupNtpServer_Object = MibScalar
ntpBackupNtpServer = _NtpBackupNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 5),
    _NtpBackupNtpServer_Type()
)
ntpBackupNtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBackupNtpServer.setStatus("current")


class _NtpTrustedServer_Type(Integer32):
    """Custom type ntpTrustedServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NtpTrustedServer_Type.__name__ = "Integer32"
_NtpTrustedServer_Object = MibScalar
ntpTrustedServer = _NtpTrustedServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 6),
    _NtpTrustedServer_Type()
)
ntpTrustedServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTrustedServer.setStatus("current")


class _NtpSyncInterval_Type(Integer32):
    """Custom type ntpSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NtpSyncInterval_Type.__name__ = "Integer32"
_NtpSyncInterval_Object = MibScalar
ntpSyncInterval = _NtpSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 7),
    _NtpSyncInterval_Type()
)
ntpSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSyncInterval.setStatus("current")
_NtpShowTimeDate_Type = DisplayString
_NtpShowTimeDate_Object = MibScalar
ntpShowTimeDate = _NtpShowTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 8),
    _NtpShowTimeDate_Type()
)
ntpShowTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpShowTimeDate.setStatus("current")
_NtpListTimeZones_Type = DisplayString
_NtpListTimeZones_Object = MibScalar
ntpListTimeZones = _NtpListTimeZones_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 9),
    _NtpListTimeZones_Type()
)
ntpListTimeZones.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpListTimeZones.setStatus("current")
_NtpTimeZone_Type = DisplayString
_NtpTimeZone_Object = MibScalar
ntpTimeZone = _NtpTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 10),
    _NtpTimeZone_Type()
)
ntpTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimeZone.setStatus("current")
_NtpTimeFormat_Type = DisplayString
_NtpTimeFormat_Object = MibScalar
ntpTimeFormat = _NtpTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 11),
    _NtpTimeFormat_Type()
)
ntpTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimeFormat.setStatus("current")
_NtpDateFormat_Type = DisplayString
_NtpDateFormat_Object = MibScalar
ntpDateFormat = _NtpDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 12),
    _NtpDateFormat_Type()
)
ntpDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpDateFormat.setStatus("current")


class _NtpStatus_Type(Integer32):
    """Custom type ntpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("unset", 0),
          ("manuallySet", 1),
          ("synchronized", 2),
          ("syncFailed", 4),
          ("dayLightSavingTime", 16))
    )


_NtpStatus_Type.__name__ = "Integer32"
_NtpStatus_Object = MibScalar
ntpStatus = _NtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 100),
    _NtpStatus_Type()
)
ntpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpStatus.setStatus("current")
_NtpLocalTime_Type = DisplayString
_NtpLocalTime_Object = MibScalar
ntpLocalTime = _NtpLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 101),
    _NtpLocalTime_Type()
)
ntpLocalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLocalTime.setStatus("current")
_NtpLocalDate_Type = DisplayString
_NtpLocalDate_Object = MibScalar
ntpLocalDate = _NtpLocalDate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 102),
    _NtpLocalDate_Type()
)
ntpLocalDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpLocalDate.setStatus("current")
_NtpUsedNtpServer_Type = DisplayString
_NtpUsedNtpServer_Object = MibScalar
ntpUsedNtpServer = _NtpUsedNtpServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 103),
    _NtpUsedNtpServer_Type()
)
ntpUsedNtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpUsedNtpServer.setStatus("current")


class _NtpDynamicNtpServer1_Type(OctetString):
    """Custom type ntpDynamicNtpServer1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpDynamicNtpServer1_Type.__name__ = "OctetString"
_NtpDynamicNtpServer1_Object = MibScalar
ntpDynamicNtpServer1 = _NtpDynamicNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 104),
    _NtpDynamicNtpServer1_Type()
)
ntpDynamicNtpServer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpDynamicNtpServer1.setStatus("current")


class _NtpDynamicNtpServer2_Type(OctetString):
    """Custom type ntpDynamicNtpServer2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpDynamicNtpServer2_Type.__name__ = "OctetString"
_NtpDynamicNtpServer2_Object = MibScalar
ntpDynamicNtpServer2 = _NtpDynamicNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 105),
    _NtpDynamicNtpServer2_Type()
)
ntpDynamicNtpServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpDynamicNtpServer2.setStatus("current")


class _NtpDynamicNtpServer3_Type(OctetString):
    """Custom type ntpDynamicNtpServer3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpDynamicNtpServer3_Type.__name__ = "OctetString"
_NtpDynamicNtpServer3_Object = MibScalar
ntpDynamicNtpServer3 = _NtpDynamicNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 106),
    _NtpDynamicNtpServer3_Type()
)
ntpDynamicNtpServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpDynamicNtpServer3.setStatus("current")


class _NtpDynamicNtpServer4_Type(OctetString):
    """Custom type ntpDynamicNtpServer4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpDynamicNtpServer4_Type.__name__ = "OctetString"
_NtpDynamicNtpServer4_Object = MibScalar
ntpDynamicNtpServer4 = _NtpDynamicNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 73, 107),
    _NtpDynamicNtpServer4_Type()
)
ntpDynamicNtpServer4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpDynamicNtpServer4.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-NTP-MIB",
    **{"management": management,
       "ntp": ntp,
       "ntpEnableNtp": ntpEnableNtp,
       "ntpSyncNow": ntpSyncNow,
       "ntpDhcpProvidesNtpServer": ntpDhcpProvidesNtpServer,
       "ntpMainNtpServer": ntpMainNtpServer,
       "ntpBackupNtpServer": ntpBackupNtpServer,
       "ntpTrustedServer": ntpTrustedServer,
       "ntpSyncInterval": ntpSyncInterval,
       "ntpShowTimeDate": ntpShowTimeDate,
       "ntpListTimeZones": ntpListTimeZones,
       "ntpTimeZone": ntpTimeZone,
       "ntpTimeFormat": ntpTimeFormat,
       "ntpDateFormat": ntpDateFormat,
       "ntpStatus": ntpStatus,
       "ntpLocalTime": ntpLocalTime,
       "ntpLocalDate": ntpLocalDate,
       "ntpUsedNtpServer": ntpUsedNtpServer,
       "ntpDynamicNtpServer1": ntpDynamicNtpServer1,
       "ntpDynamicNtpServer2": ntpDynamicNtpServer2,
       "ntpDynamicNtpServer3": ntpDynamicNtpServer3,
       "ntpDynamicNtpServer4": ntpDynamicNtpServer4}
)
