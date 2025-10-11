# SNMP MIB module (CAMBIUM-NETWORKS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:34 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4)
)
if mibBuilder.loadTexts:
    cnSystem.setRevisions(
        ("2022-09-01 12:00",
         "2022-05-27 19:00",
         "2022-04-08 18:00",
         "2021-12-18 18:00",
         "2021-08-18 18:00",
         "2021-05-06 18:00",
         "2021-03-02 18:00",
         "2021-02-15 18:00",
         "2020-10-23 18:00",
         "2020-06-25 18:00",
         "2019-03-14 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _CambiumScheduledReload_Type(TruthValue):
    """Custom type cambiumScheduledReload based on TruthValue"""
    defaultValue = 2


_CambiumScheduledReload_Type.__name__ = "TruthValue"
_CambiumScheduledReload_Object = MibScalar
cambiumScheduledReload = _CambiumScheduledReload_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 1),
    _CambiumScheduledReload_Type()
)
cambiumScheduledReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumScheduledReload.setStatus("current")


class _CambiumReloadRelativeTime_Type(Integer32):
    """Custom type cambiumReloadRelativeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CambiumReloadRelativeTime_Type.__name__ = "Integer32"
_CambiumReloadRelativeTime_Object = MibScalar
cambiumReloadRelativeTime = _CambiumReloadRelativeTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 2),
    _CambiumReloadRelativeTime_Type()
)
cambiumReloadRelativeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumReloadRelativeTime.setStatus("current")
_CambiumReloadAbsoluteTime_Type = DateAndTime
_CambiumReloadAbsoluteTime_Object = MibScalar
cambiumReloadAbsoluteTime = _CambiumReloadAbsoluteTime_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 3),
    _CambiumReloadAbsoluteTime_Type()
)
cambiumReloadAbsoluteTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumReloadAbsoluteTime.setStatus("current")


class _CambiumReloadReason_Type(DisplayString):
    """Custom type cambiumReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumReloadReason_Type.__name__ = "DisplayString"
_CambiumReloadReason_Object = MibScalar
cambiumReloadReason = _CambiumReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 4),
    _CambiumReloadReason_Type()
)
cambiumReloadReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumReloadReason.setStatus("current")


class _CambiumLastReloadReason_Type(DisplayString):
    """Custom type cambiumLastReloadReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CambiumLastReloadReason_Type.__name__ = "DisplayString"
_CambiumLastReloadReason_Object = MibScalar
cambiumLastReloadReason = _CambiumLastReloadReason_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 5),
    _CambiumLastReloadReason_Type()
)
cambiumLastReloadReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumLastReloadReason.setStatus("current")


class _CambiumStpMode_Type(Integer32):
    """Custom type cambiumStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CambiumStpMode_Type.__name__ = "Integer32"
_CambiumStpMode_Object = MibScalar
cambiumStpMode = _CambiumStpMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 6),
    _CambiumStpMode_Type()
)
cambiumStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumStpMode.setStatus("current")
_CambiumXMSInterfaceIP_Type = IpAddress
_CambiumXMSInterfaceIP_Object = MibScalar
cambiumXMSInterfaceIP = _CambiumXMSInterfaceIP_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 7),
    _CambiumXMSInterfaceIP_Type()
)
cambiumXMSInterfaceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumXMSInterfaceIP.setStatus("current")
_CambiumXMSInterfaceMask_Type = IpAddress
_CambiumXMSInterfaceMask_Object = MibScalar
cambiumXMSInterfaceMask = _CambiumXMSInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 8),
    _CambiumXMSInterfaceMask_Type()
)
cambiumXMSInterfaceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumXMSInterfaceMask.setStatus("current")


class _CambiumXMSInterfaceVLANId_Type(Integer32):
    """Custom type cambiumXMSInterfaceVLANId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CambiumXMSInterfaceVLANId_Type.__name__ = "Integer32"
_CambiumXMSInterfaceVLANId_Object = MibScalar
cambiumXMSInterfaceVLANId = _CambiumXMSInterfaceVLANId_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 9),
    _CambiumXMSInterfaceVLANId_Type()
)
cambiumXMSInterfaceVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cambiumXMSInterfaceVLANId.setStatus("current")
_CambiumSystemClock_Type = DateAndTime
_CambiumSystemClock_Object = MibScalar
cambiumSystemClock = _CambiumSystemClock_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 10),
    _CambiumSystemClock_Type()
)
cambiumSystemClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemClock.setStatus("current")


class _CambiumSystemTimezoneName_Type(DisplayString):
    """Custom type cambiumSystemTimezoneName based on DisplayString"""
    defaultValue = OctetString("UTC")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_CambiumSystemTimezoneName_Type.__name__ = "DisplayString"
_CambiumSystemTimezoneName_Object = MibScalar
cambiumSystemTimezoneName = _CambiumSystemTimezoneName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 11),
    _CambiumSystemTimezoneName_Type()
)
cambiumSystemTimezoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemTimezoneName.setStatus("current")


class _CambiumSystemTimezoneOffset_Type(Integer32):
    """Custom type cambiumSystemTimezoneOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1439, 1439),
    )


_CambiumSystemTimezoneOffset_Type.__name__ = "Integer32"
_CambiumSystemTimezoneOffset_Object = MibScalar
cambiumSystemTimezoneOffset = _CambiumSystemTimezoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 12),
    _CambiumSystemTimezoneOffset_Type()
)
cambiumSystemTimezoneOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemTimezoneOffset.setStatus("current")


class _CambiumSystemSummerTimeName_Type(DisplayString):
    """Custom type cambiumSystemSummerTimeName based on DisplayString"""
    defaultValue = OctetString("UTC")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 6),
    )


_CambiumSystemSummerTimeName_Type.__name__ = "DisplayString"
_CambiumSystemSummerTimeName_Object = MibScalar
cambiumSystemSummerTimeName = _CambiumSystemSummerTimeName_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 13),
    _CambiumSystemSummerTimeName_Type()
)
cambiumSystemSummerTimeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemSummerTimeName.setStatus("current")


class _CambiumSystemSummerTimeOffset_Type(Integer32):
    """Custom type cambiumSystemSummerTimeOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_CambiumSystemSummerTimeOffset_Type.__name__ = "Integer32"
_CambiumSystemSummerTimeOffset_Object = MibScalar
cambiumSystemSummerTimeOffset = _CambiumSystemSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 14),
    _CambiumSystemSummerTimeOffset_Type()
)
cambiumSystemSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemSummerTimeOffset.setStatus("current")
_CambiumSystemSummerTimeStart_Type = DateAndTime
_CambiumSystemSummerTimeStart_Object = MibScalar
cambiumSystemSummerTimeStart = _CambiumSystemSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 15),
    _CambiumSystemSummerTimeStart_Type()
)
cambiumSystemSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemSummerTimeStart.setStatus("current")
_CambiumSystemSummerTimeEnd_Type = DateAndTime
_CambiumSystemSummerTimeEnd_Object = MibScalar
cambiumSystemSummerTimeEnd = _CambiumSystemSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 16),
    _CambiumSystemSummerTimeEnd_Type()
)
cambiumSystemSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemSummerTimeEnd.setStatus("current")


class _CambiumSystemRecurringSummerTimeStart_Type(DisplayString):
    """Custom type cambiumSystemRecurringSummerTimeStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_CambiumSystemRecurringSummerTimeStart_Type.__name__ = "DisplayString"
_CambiumSystemRecurringSummerTimeStart_Object = MibScalar
cambiumSystemRecurringSummerTimeStart = _CambiumSystemRecurringSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 17),
    _CambiumSystemRecurringSummerTimeStart_Type()
)
cambiumSystemRecurringSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemRecurringSummerTimeStart.setStatus("current")


class _CambiumSystemRecurringSummerTimeEnd_Type(DisplayString):
    """Custom type cambiumSystemRecurringSummerTimeEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_CambiumSystemRecurringSummerTimeEnd_Type.__name__ = "DisplayString"
_CambiumSystemRecurringSummerTimeEnd_Object = MibScalar
cambiumSystemRecurringSummerTimeEnd = _CambiumSystemRecurringSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 18),
    _CambiumSystemRecurringSummerTimeEnd_Type()
)
cambiumSystemRecurringSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemRecurringSummerTimeEnd.setStatus("current")


class _CambiumSystemSummerTimeMode_Type(Integer32):
    """Custom type cambiumSystemSummerTimeMode based on Integer32"""
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
        *(("none", 1),
          ("one-shot", 2),
          ("recurring", 3))
    )


_CambiumSystemSummerTimeMode_Type.__name__ = "Integer32"
_CambiumSystemSummerTimeMode_Object = MibScalar
cambiumSystemSummerTimeMode = _CambiumSystemSummerTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 19),
    _CambiumSystemSummerTimeMode_Type()
)
cambiumSystemSummerTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemSummerTimeMode.setStatus("current")


class _CambiumReloadDefault_Type(TruthValue):
    """Custom type cambiumReloadDefault based on TruthValue"""
    defaultValue = 2


_CambiumReloadDefault_Type.__name__ = "TruthValue"
_CambiumReloadDefault_Object = MibScalar
cambiumReloadDefault = _CambiumReloadDefault_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 20),
    _CambiumReloadDefault_Type()
)
cambiumReloadDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumReloadDefault.setStatus("current")


class _CambiumReloadPartialDefault_Type(TruthValue):
    """Custom type cambiumReloadPartialDefault based on TruthValue"""
    defaultValue = 2


_CambiumReloadPartialDefault_Type.__name__ = "TruthValue"
_CambiumReloadPartialDefault_Object = MibScalar
cambiumReloadPartialDefault = _CambiumReloadPartialDefault_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 21),
    _CambiumReloadPartialDefault_Type()
)
cambiumReloadPartialDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumReloadPartialDefault.setStatus("current")


class _CambiumSystemResetButton_Type(Integer32):
    """Custom type cambiumSystemResetButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_CambiumSystemResetButton_Type.__name__ = "Integer32"
_CambiumSystemResetButton_Object = MibScalar
cambiumSystemResetButton = _CambiumSystemResetButton_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 22),
    _CambiumSystemResetButton_Type()
)
cambiumSystemResetButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemResetButton.setStatus("current")


class _CambiumMstpReset_Type(Integer32):
    """Custom type cambiumMstpReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CambiumMstpReset_Type.__name__ = "Integer32"
_CambiumMstpReset_Object = MibScalar
cambiumMstpReset = _CambiumMstpReset_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 23),
    _CambiumMstpReset_Type()
)
cambiumMstpReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumMstpReset.setStatus("current")
_CnHttpClient_ObjectIdentity = ObjectIdentity
cnHttpClient = _CnHttpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24)
)


class _CnHttpClientProxyAddress_Type(InetAddress):
    """Custom type cnHttpClientProxyAddress based on InetAddress"""
    defaultValue = OctetString("")


_CnHttpClientProxyAddress_Type.__name__ = "InetAddress"
_CnHttpClientProxyAddress_Object = MibScalar
cnHttpClientProxyAddress = _CnHttpClientProxyAddress_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24, 1),
    _CnHttpClientProxyAddress_Type()
)
cnHttpClientProxyAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnHttpClientProxyAddress.setStatus("current")


class _CnHttpClientProxyAddressType_Type(InetAddressType):
    """Custom type cnHttpClientProxyAddressType based on InetAddressType"""
    defaultValue = 0


_CnHttpClientProxyAddressType_Type.__name__ = "InetAddressType"
_CnHttpClientProxyAddressType_Object = MibScalar
cnHttpClientProxyAddressType = _CnHttpClientProxyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24, 2),
    _CnHttpClientProxyAddressType_Type()
)
cnHttpClientProxyAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnHttpClientProxyAddressType.setStatus("current")


class _CnHttpClientProxyPort_Type(Integer32):
    """Custom type cnHttpClientProxyPort based on Integer32"""
    defaultValue = 8080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnHttpClientProxyPort_Type.__name__ = "Integer32"
_CnHttpClientProxyPort_Object = MibScalar
cnHttpClientProxyPort = _CnHttpClientProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24, 3),
    _CnHttpClientProxyPort_Type()
)
cnHttpClientProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnHttpClientProxyPort.setStatus("current")


class _CnHttpClientUsername_Type(DisplayString):
    """Custom type cnHttpClientUsername based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CnHttpClientUsername_Type.__name__ = "DisplayString"
_CnHttpClientUsername_Object = MibScalar
cnHttpClientUsername = _CnHttpClientUsername_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24, 4),
    _CnHttpClientUsername_Type()
)
cnHttpClientUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnHttpClientUsername.setStatus("current")


class _CnHttpClientPassword_Type(DisplayString):
    """Custom type cnHttpClientPassword based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CnHttpClientPassword_Type.__name__ = "DisplayString"
_CnHttpClientPassword_Object = MibScalar
cnHttpClientPassword = _CnHttpClientPassword_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24, 5),
    _CnHttpClientPassword_Type()
)
cnHttpClientPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnHttpClientPassword.setStatus("current")


class _CnHttpClientPasswordType_Type(Integer32):
    """Custom type cnHttpClientPasswordType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unencrypted-password", 0),
          ("type-7", 7))
    )


_CnHttpClientPasswordType_Type.__name__ = "Integer32"
_CnHttpClientPasswordType_Object = MibScalar
cnHttpClientPasswordType = _CnHttpClientPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 24, 6),
    _CnHttpClientPasswordType_Type()
)
cnHttpClientPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnHttpClientPasswordType.setStatus("current")


class _CambiumSystemLoginBanner_Type(OctetString):
    """Custom type cambiumSystemLoginBanner based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )


_CambiumSystemLoginBanner_Type.__name__ = "OctetString"
_CambiumSystemLoginBanner_Object = MibScalar
cambiumSystemLoginBanner = _CambiumSystemLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 25),
    _CambiumSystemLoginBanner_Type()
)
cambiumSystemLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemLoginBanner.setStatus("current")


class _CambiumSystemMotdBanner_Type(OctetString):
    """Custom type cambiumSystemMotdBanner based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 900),
    )


_CambiumSystemMotdBanner_Type.__name__ = "OctetString"
_CambiumSystemMotdBanner_Object = MibScalar
cambiumSystemMotdBanner = _CambiumSystemMotdBanner_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 26),
    _CambiumSystemMotdBanner_Type()
)
cambiumSystemMotdBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumSystemMotdBanner.setStatus("current")
_CnCpuRateLimits_ObjectIdentity = ObjectIdentity
cnCpuRateLimits = _CnCpuRateLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 27)
)


class _CnArpBroadCastRateLimit_Type(Integer32):
    """Custom type cnArpBroadCastRateLimit based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 65500),
    )


_CnArpBroadCastRateLimit_Type.__name__ = "Integer32"
_CnArpBroadCastRateLimit_Object = MibScalar
cnArpBroadCastRateLimit = _CnArpBroadCastRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 27, 1),
    _CnArpBroadCastRateLimit_Type()
)
cnArpBroadCastRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnArpBroadCastRateLimit.setStatus("current")


class _CambiumPasswordEncryption_Type(TruthValue):
    """Custom type cambiumPasswordEncryption based on TruthValue"""
    defaultValue = 2


_CambiumPasswordEncryption_Type.__name__ = "TruthValue"
_CambiumPasswordEncryption_Object = MibScalar
cambiumPasswordEncryption = _CambiumPasswordEncryption_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 4, 28),
    _CambiumPasswordEncryption_Type()
)
cambiumPasswordEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cambiumPasswordEncryption.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-SYSTEM-MIB",
    **{"cnSystem": cnSystem,
       "cambiumScheduledReload": cambiumScheduledReload,
       "cambiumReloadRelativeTime": cambiumReloadRelativeTime,
       "cambiumReloadAbsoluteTime": cambiumReloadAbsoluteTime,
       "cambiumReloadReason": cambiumReloadReason,
       "cambiumLastReloadReason": cambiumLastReloadReason,
       "cambiumStpMode": cambiumStpMode,
       "cambiumXMSInterfaceIP": cambiumXMSInterfaceIP,
       "cambiumXMSInterfaceMask": cambiumXMSInterfaceMask,
       "cambiumXMSInterfaceVLANId": cambiumXMSInterfaceVLANId,
       "cambiumSystemClock": cambiumSystemClock,
       "cambiumSystemTimezoneName": cambiumSystemTimezoneName,
       "cambiumSystemTimezoneOffset": cambiumSystemTimezoneOffset,
       "cambiumSystemSummerTimeName": cambiumSystemSummerTimeName,
       "cambiumSystemSummerTimeOffset": cambiumSystemSummerTimeOffset,
       "cambiumSystemSummerTimeStart": cambiumSystemSummerTimeStart,
       "cambiumSystemSummerTimeEnd": cambiumSystemSummerTimeEnd,
       "cambiumSystemRecurringSummerTimeStart": cambiumSystemRecurringSummerTimeStart,
       "cambiumSystemRecurringSummerTimeEnd": cambiumSystemRecurringSummerTimeEnd,
       "cambiumSystemSummerTimeMode": cambiumSystemSummerTimeMode,
       "cambiumReloadDefault": cambiumReloadDefault,
       "cambiumReloadPartialDefault": cambiumReloadPartialDefault,
       "cambiumSystemResetButton": cambiumSystemResetButton,
       "cambiumMstpReset": cambiumMstpReset,
       "cnHttpClient": cnHttpClient,
       "cnHttpClientProxyAddress": cnHttpClientProxyAddress,
       "cnHttpClientProxyAddressType": cnHttpClientProxyAddressType,
       "cnHttpClientProxyPort": cnHttpClientProxyPort,
       "cnHttpClientUsername": cnHttpClientUsername,
       "cnHttpClientPassword": cnHttpClientPassword,
       "cnHttpClientPasswordType": cnHttpClientPasswordType,
       "cambiumSystemLoginBanner": cambiumSystemLoginBanner,
       "cambiumSystemMotdBanner": cambiumSystemMotdBanner,
       "cnCpuRateLimits": cnCpuRateLimits,
       "cnArpBroadCastRateLimit": cnArpBroadCastRateLimit,
       "cambiumPasswordEncryption": cambiumPasswordEncryption}
)
