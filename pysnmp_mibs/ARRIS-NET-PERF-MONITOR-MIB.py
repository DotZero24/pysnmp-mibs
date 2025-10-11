# SNMP MIB module (ARRIS-NET-PERF-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-NET-PERF-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:09:23 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrisNetPerfMonitorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13)
)
if mibBuilder.loadTexts:
    arrisNetPerfMonitorMib.setRevisions(
        ("1912-10-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisNpmSetup_ObjectIdentity = ObjectIdentity
arrisNpmSetup = _ArrisNpmSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 1)
)


class _ArrisNpmSetupBgTrafficRateEnable_Type(Integer32):
    """Custom type arrisNpmSetupBgTrafficRateEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArrisNpmSetupBgTrafficRateEnable_Type.__name__ = "Integer32"
_ArrisNpmSetupBgTrafficRateEnable_Object = MibScalar
arrisNpmSetupBgTrafficRateEnable = _ArrisNpmSetupBgTrafficRateEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 1, 1),
    _ArrisNpmSetupBgTrafficRateEnable_Type()
)
arrisNpmSetupBgTrafficRateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupBgTrafficRateEnable.setStatus("current")


class _ArrisNpmSetupBgTrafficMaxDownstreamRate_Type(Unsigned32):
    """Custom type arrisNpmSetupBgTrafficMaxDownstreamRate based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ArrisNpmSetupBgTrafficMaxDownstreamRate_Type.__name__ = "Unsigned32"
_ArrisNpmSetupBgTrafficMaxDownstreamRate_Object = MibScalar
arrisNpmSetupBgTrafficMaxDownstreamRate = _ArrisNpmSetupBgTrafficMaxDownstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 1, 2),
    _ArrisNpmSetupBgTrafficMaxDownstreamRate_Type()
)
arrisNpmSetupBgTrafficMaxDownstreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupBgTrafficMaxDownstreamRate.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupBgTrafficMaxDownstreamRate.setUnits("Kbps")


class _ArrisNpmSetupBgTrafficMaxUpstreamRate_Type(Unsigned32):
    """Custom type arrisNpmSetupBgTrafficMaxUpstreamRate based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ArrisNpmSetupBgTrafficMaxUpstreamRate_Type.__name__ = "Unsigned32"
_ArrisNpmSetupBgTrafficMaxUpstreamRate_Object = MibScalar
arrisNpmSetupBgTrafficMaxUpstreamRate = _ArrisNpmSetupBgTrafficMaxUpstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 1, 3),
    _ArrisNpmSetupBgTrafficMaxUpstreamRate_Type()
)
arrisNpmSetupBgTrafficMaxUpstreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupBgTrafficMaxUpstreamRate.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupBgTrafficMaxUpstreamRate.setUnits("Kbps")


class _ArrisNpmSetupGroupReference_Type(OctetString):
    """Custom type arrisNpmSetupGroupReference based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArrisNpmSetupGroupReference_Type.__name__ = "OctetString"
_ArrisNpmSetupGroupReference_Object = MibScalar
arrisNpmSetupGroupReference = _ArrisNpmSetupGroupReference_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 1, 4),
    _ArrisNpmSetupGroupReference_Type()
)
arrisNpmSetupGroupReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupGroupReference.setStatus("current")
_ArrisNpmWebDlTest_ObjectIdentity = ObjectIdentity
arrisNpmWebDlTest = _ArrisNpmWebDlTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2)
)


class _ArrisNpmSetupWebPageDlTestRunTime_Type(Unsigned32):
    """Custom type arrisNpmSetupWebPageDlTestRunTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArrisNpmSetupWebPageDlTestRunTime_Type.__name__ = "Unsigned32"
_ArrisNpmSetupWebPageDlTestRunTime_Object = MibScalar
arrisNpmSetupWebPageDlTestRunTime = _ArrisNpmSetupWebPageDlTestRunTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 1),
    _ArrisNpmSetupWebPageDlTestRunTime_Type()
)
arrisNpmSetupWebPageDlTestRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestRunTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestRunTime.setUnits("Seconds")


class _ArrisNpmSetupWebPageDlTestTimeout_Type(Unsigned32):
    """Custom type arrisNpmSetupWebPageDlTestTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArrisNpmSetupWebPageDlTestTimeout_Type.__name__ = "Unsigned32"
_ArrisNpmSetupWebPageDlTestTimeout_Object = MibScalar
arrisNpmSetupWebPageDlTestTimeout = _ArrisNpmSetupWebPageDlTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 2),
    _ArrisNpmSetupWebPageDlTestTimeout_Type()
)
arrisNpmSetupWebPageDlTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestTimeout.setUnits("Seconds")
_ArrisNpmSetupWebPageDlTestTable_Object = MibTable
arrisNpmSetupWebPageDlTestTable = _ArrisNpmSetupWebPageDlTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 3)
)
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestTable.setStatus("current")
_ArrisNpmSetupWebPageDlTestEntry_Object = MibTableRow
arrisNpmSetupWebPageDlTestEntry = _ArrisNpmSetupWebPageDlTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 3, 1)
)
arrisNpmSetupWebPageDlTestEntry.setIndexNames(
    (0, "ARRIS-NET-PERF-MONITOR-MIB", "arrisNpmSetupWebPageDlTestConfigIndex"),
)
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestEntry.setStatus("current")


class _ArrisNpmSetupWebPageDlTestConfigIndex_Type(Integer32):
    """Custom type arrisNpmSetupWebPageDlTestConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ArrisNpmSetupWebPageDlTestConfigIndex_Type.__name__ = "Integer32"
_ArrisNpmSetupWebPageDlTestConfigIndex_Object = MibTableColumn
arrisNpmSetupWebPageDlTestConfigIndex = _ArrisNpmSetupWebPageDlTestConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 3, 1, 1),
    _ArrisNpmSetupWebPageDlTestConfigIndex_Type()
)
arrisNpmSetupWebPageDlTestConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestConfigIndex.setStatus("current")


class _ArrisNpmSetupWebPageDlTestConfigUrl_Type(OctetString):
    """Custom type arrisNpmSetupWebPageDlTestConfigUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ArrisNpmSetupWebPageDlTestConfigUrl_Type.__name__ = "OctetString"
_ArrisNpmSetupWebPageDlTestConfigUrl_Object = MibTableColumn
arrisNpmSetupWebPageDlTestConfigUrl = _ArrisNpmSetupWebPageDlTestConfigUrl_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 3, 1, 2),
    _ArrisNpmSetupWebPageDlTestConfigUrl_Type()
)
arrisNpmSetupWebPageDlTestConfigUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestConfigUrl.setStatus("current")
_ArrisNpmSetupWebPageDlTestConfigRowStatus_Type = RowStatus
_ArrisNpmSetupWebPageDlTestConfigRowStatus_Object = MibTableColumn
arrisNpmSetupWebPageDlTestConfigRowStatus = _ArrisNpmSetupWebPageDlTestConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 3, 1, 3),
    _ArrisNpmSetupWebPageDlTestConfigRowStatus_Type()
)
arrisNpmSetupWebPageDlTestConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisNpmSetupWebPageDlTestConfigRowStatus.setStatus("current")
_ArrisNpmResultWebPageDlTestTable_Object = MibTable
arrisNpmResultWebPageDlTestTable = _ArrisNpmResultWebPageDlTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 4)
)
if mibBuilder.loadTexts:
    arrisNpmResultWebPageDlTestTable.setStatus("current")
_ArrisNpmResultWebPageDlTestEntry_Object = MibTableRow
arrisNpmResultWebPageDlTestEntry = _ArrisNpmResultWebPageDlTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 4, 1)
)
arrisNpmResultWebPageDlTestEntry.setIndexNames(
    (0, "ARRIS-NET-PERF-MONITOR-MIB", "arrisNpmSetupWebPageDlTestConfigIndex"),
)
if mibBuilder.loadTexts:
    arrisNpmResultWebPageDlTestEntry.setStatus("current")


class _ArrisNpmResultWebPageDlTestResult_Type(OctetString):
    """Custom type arrisNpmResultWebPageDlTestResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 400),
    )


_ArrisNpmResultWebPageDlTestResult_Type.__name__ = "OctetString"
_ArrisNpmResultWebPageDlTestResult_Object = MibTableColumn
arrisNpmResultWebPageDlTestResult = _ArrisNpmResultWebPageDlTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 2, 4, 1, 1),
    _ArrisNpmResultWebPageDlTestResult_Type()
)
arrisNpmResultWebPageDlTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisNpmResultWebPageDlTestResult.setStatus("current")
_ArrisNpmDnsTest_ObjectIdentity = ObjectIdentity
arrisNpmDnsTest = _ArrisNpmDnsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3)
)


class _ArrisNpmSetupDnsTestEnable_Type(Integer32):
    """Custom type arrisNpmSetupDnsTestEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArrisNpmSetupDnsTestEnable_Type.__name__ = "Integer32"
_ArrisNpmSetupDnsTestEnable_Object = MibScalar
arrisNpmSetupDnsTestEnable = _ArrisNpmSetupDnsTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 1),
    _ArrisNpmSetupDnsTestEnable_Type()
)
arrisNpmSetupDnsTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsTestEnable.setStatus("current")


class _ArrisNpmSetupDnsTestRunTime_Type(Unsigned32):
    """Custom type arrisNpmSetupDnsTestRunTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArrisNpmSetupDnsTestRunTime_Type.__name__ = "Unsigned32"
_ArrisNpmSetupDnsTestRunTime_Object = MibScalar
arrisNpmSetupDnsTestRunTime = _ArrisNpmSetupDnsTestRunTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 2),
    _ArrisNpmSetupDnsTestRunTime_Type()
)
arrisNpmSetupDnsTestRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsTestRunTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsTestRunTime.setUnits("Seconds")


class _ArrisNpmSetupDnsTestRunTimeTimeout_Type(Unsigned32):
    """Custom type arrisNpmSetupDnsTestRunTimeTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArrisNpmSetupDnsTestRunTimeTimeout_Type.__name__ = "Unsigned32"
_ArrisNpmSetupDnsTestRunTimeTimeout_Object = MibScalar
arrisNpmSetupDnsTestRunTimeTimeout = _ArrisNpmSetupDnsTestRunTimeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 3),
    _ArrisNpmSetupDnsTestRunTimeTimeout_Type()
)
arrisNpmSetupDnsTestRunTimeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsTestRunTimeTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsTestRunTimeTimeout.setUnits("Seconds")


class _ArrisNpmSetupDnsPrimaryServerIpType_Type(InetAddressType):
    """Custom type arrisNpmSetupDnsPrimaryServerIpType based on InetAddressType"""
    defaultValue = 1


_ArrisNpmSetupDnsPrimaryServerIpType_Type.__name__ = "InetAddressType"
_ArrisNpmSetupDnsPrimaryServerIpType_Object = MibScalar
arrisNpmSetupDnsPrimaryServerIpType = _ArrisNpmSetupDnsPrimaryServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 4),
    _ArrisNpmSetupDnsPrimaryServerIpType_Type()
)
arrisNpmSetupDnsPrimaryServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsPrimaryServerIpType.setStatus("current")


class _ArrisNpmSetupDnsPrimaryServerIpAddress_Type(InetAddress):
    """Custom type arrisNpmSetupDnsPrimaryServerIpAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_ArrisNpmSetupDnsPrimaryServerIpAddress_Type.__name__ = "InetAddress"
_ArrisNpmSetupDnsPrimaryServerIpAddress_Object = MibScalar
arrisNpmSetupDnsPrimaryServerIpAddress = _ArrisNpmSetupDnsPrimaryServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 5),
    _ArrisNpmSetupDnsPrimaryServerIpAddress_Type()
)
arrisNpmSetupDnsPrimaryServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsPrimaryServerIpAddress.setStatus("current")


class _ArrisNpmSetupDnsSecondaryServerIpType_Type(InetAddressType):
    """Custom type arrisNpmSetupDnsSecondaryServerIpType based on InetAddressType"""
    defaultValue = 1


_ArrisNpmSetupDnsSecondaryServerIpType_Type.__name__ = "InetAddressType"
_ArrisNpmSetupDnsSecondaryServerIpType_Object = MibScalar
arrisNpmSetupDnsSecondaryServerIpType = _ArrisNpmSetupDnsSecondaryServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 6),
    _ArrisNpmSetupDnsSecondaryServerIpType_Type()
)
arrisNpmSetupDnsSecondaryServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsSecondaryServerIpType.setStatus("current")


class _ArrisNpmSetupDnsSecondaryServerIpAddress_Type(InetAddress):
    """Custom type arrisNpmSetupDnsSecondaryServerIpAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_ArrisNpmSetupDnsSecondaryServerIpAddress_Type.__name__ = "InetAddress"
_ArrisNpmSetupDnsSecondaryServerIpAddress_Object = MibScalar
arrisNpmSetupDnsSecondaryServerIpAddress = _ArrisNpmSetupDnsSecondaryServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 7),
    _ArrisNpmSetupDnsSecondaryServerIpAddress_Type()
)
arrisNpmSetupDnsSecondaryServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupDnsSecondaryServerIpAddress.setStatus("current")
_ArrisNpmResultDnsTestTable_Object = MibTable
arrisNpmResultDnsTestTable = _ArrisNpmResultDnsTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 8)
)
if mibBuilder.loadTexts:
    arrisNpmResultDnsTestTable.setStatus("current")
_ArrisNpmResultDnsTestEntry_Object = MibTableRow
arrisNpmResultDnsTestEntry = _ArrisNpmResultDnsTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 8, 1)
)
arrisNpmResultDnsTestEntry.setIndexNames(
    (0, "ARRIS-NET-PERF-MONITOR-MIB", "arrisNpmResultDnsTestResultIndex"),
)
if mibBuilder.loadTexts:
    arrisNpmResultDnsTestEntry.setStatus("current")


class _ArrisNpmResultDnsTestResultIndex_Type(Integer32):
    """Custom type arrisNpmResultDnsTestResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ArrisNpmResultDnsTestResultIndex_Type.__name__ = "Integer32"
_ArrisNpmResultDnsTestResultIndex_Object = MibTableColumn
arrisNpmResultDnsTestResultIndex = _ArrisNpmResultDnsTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 8, 1, 1),
    _ArrisNpmResultDnsTestResultIndex_Type()
)
arrisNpmResultDnsTestResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisNpmResultDnsTestResultIndex.setStatus("current")


class _ArrisNpmResultDnsTestResult_Type(OctetString):
    """Custom type arrisNpmResultDnsTestResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 400),
    )


_ArrisNpmResultDnsTestResult_Type.__name__ = "OctetString"
_ArrisNpmResultDnsTestResult_Object = MibTableColumn
arrisNpmResultDnsTestResult = _ArrisNpmResultDnsTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 3, 8, 1, 2),
    _ArrisNpmResultDnsTestResult_Type()
)
arrisNpmResultDnsTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisNpmResultDnsTestResult.setStatus("current")
_ArrisNpmNetLatencyTest_ObjectIdentity = ObjectIdentity
arrisNpmNetLatencyTest = _ArrisNpmNetLatencyTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4)
)


class _ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Type(Integer32):
    """Custom type arrisNpmSetupNetLatencyTestRunUnderLoadEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Type.__name__ = "Integer32"
_ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Object = MibScalar
arrisNpmSetupNetLatencyTestRunUnderLoadEnable = _ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 1),
    _ArrisNpmSetupNetLatencyTestRunUnderLoadEnable_Type()
)
arrisNpmSetupNetLatencyTestRunUnderLoadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestRunUnderLoadEnable.setStatus("current")


class _ArrisNpmSetupNetLatencyTestRunTime_Type(Unsigned32):
    """Custom type arrisNpmSetupNetLatencyTestRunTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ArrisNpmSetupNetLatencyTestRunTime_Type.__name__ = "Unsigned32"
_ArrisNpmSetupNetLatencyTestRunTime_Object = MibScalar
arrisNpmSetupNetLatencyTestRunTime = _ArrisNpmSetupNetLatencyTestRunTime_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 2),
    _ArrisNpmSetupNetLatencyTestRunTime_Type()
)
arrisNpmSetupNetLatencyTestRunTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestRunTime.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestRunTime.setUnits("Seconds")


class _ArrisNpmSetupNetLatencyTestPingCount_Type(Unsigned32):
    """Custom type arrisNpmSetupNetLatencyTestPingCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ArrisNpmSetupNetLatencyTestPingCount_Type.__name__ = "Unsigned32"
_ArrisNpmSetupNetLatencyTestPingCount_Object = MibScalar
arrisNpmSetupNetLatencyTestPingCount = _ArrisNpmSetupNetLatencyTestPingCount_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 3),
    _ArrisNpmSetupNetLatencyTestPingCount_Type()
)
arrisNpmSetupNetLatencyTestPingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestPingCount.setStatus("current")


class _ArrisNpmSetupNetLatencyTestPingInterval_Type(Unsigned32):
    """Custom type arrisNpmSetupNetLatencyTestPingInterval based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36000000),
    )


_ArrisNpmSetupNetLatencyTestPingInterval_Type.__name__ = "Unsigned32"
_ArrisNpmSetupNetLatencyTestPingInterval_Object = MibScalar
arrisNpmSetupNetLatencyTestPingInterval = _ArrisNpmSetupNetLatencyTestPingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 4),
    _ArrisNpmSetupNetLatencyTestPingInterval_Type()
)
arrisNpmSetupNetLatencyTestPingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestPingInterval.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestPingInterval.setUnits("Milliseconds")


class _ArrisNpmSetupNetLatencyTestPingTimeout_Type(Unsigned32):
    """Custom type arrisNpmSetupNetLatencyTestPingTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ArrisNpmSetupNetLatencyTestPingTimeout_Type.__name__ = "Unsigned32"
_ArrisNpmSetupNetLatencyTestPingTimeout_Object = MibScalar
arrisNpmSetupNetLatencyTestPingTimeout = _ArrisNpmSetupNetLatencyTestPingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 5),
    _ArrisNpmSetupNetLatencyTestPingTimeout_Type()
)
arrisNpmSetupNetLatencyTestPingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestPingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyTestPingTimeout.setUnits("Seconds")
_ArrisNpmSetupNetLatencyServerTable_Object = MibTable
arrisNpmSetupNetLatencyServerTable = _ArrisNpmSetupNetLatencyServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 6)
)
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyServerTable.setStatus("current")
_ArrisNpmSetupNetLatencyServerEntry_Object = MibTableRow
arrisNpmSetupNetLatencyServerEntry = _ArrisNpmSetupNetLatencyServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 6, 1)
)
arrisNpmSetupNetLatencyServerEntry.setIndexNames(
    (0, "ARRIS-NET-PERF-MONITOR-MIB", "arrisNpmSetupNetLatencyConfigIndex"),
)
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyServerEntry.setStatus("current")


class _ArrisNpmSetupNetLatencyConfigIndex_Type(Integer32):
    """Custom type arrisNpmSetupNetLatencyConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ArrisNpmSetupNetLatencyConfigIndex_Type.__name__ = "Integer32"
_ArrisNpmSetupNetLatencyConfigIndex_Object = MibTableColumn
arrisNpmSetupNetLatencyConfigIndex = _ArrisNpmSetupNetLatencyConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 6, 1, 1),
    _ArrisNpmSetupNetLatencyConfigIndex_Type()
)
arrisNpmSetupNetLatencyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyConfigIndex.setStatus("current")


class _ArrisNpmSetupNetLatencyConfigServer_Type(OctetString):
    """Custom type arrisNpmSetupNetLatencyConfigServer based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ArrisNpmSetupNetLatencyConfigServer_Type.__name__ = "OctetString"
_ArrisNpmSetupNetLatencyConfigServer_Object = MibTableColumn
arrisNpmSetupNetLatencyConfigServer = _ArrisNpmSetupNetLatencyConfigServer_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 6, 1, 2),
    _ArrisNpmSetupNetLatencyConfigServer_Type()
)
arrisNpmSetupNetLatencyConfigServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyConfigServer.setStatus("current")


class _ArrisNpmSetupNetLatencyConfigServerPort_Type(Unsigned32):
    """Custom type arrisNpmSetupNetLatencyConfigServerPort based on Unsigned32"""
    defaultValue = 50000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(49152, 65535),
    )


_ArrisNpmSetupNetLatencyConfigServerPort_Type.__name__ = "Unsigned32"
_ArrisNpmSetupNetLatencyConfigServerPort_Object = MibTableColumn
arrisNpmSetupNetLatencyConfigServerPort = _ArrisNpmSetupNetLatencyConfigServerPort_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 6, 1, 3),
    _ArrisNpmSetupNetLatencyConfigServerPort_Type()
)
arrisNpmSetupNetLatencyConfigServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyConfigServerPort.setStatus("current")
_ArrisNpmSetupNetLatencyConfigServerRowStatus_Type = RowStatus
_ArrisNpmSetupNetLatencyConfigServerRowStatus_Object = MibTableColumn
arrisNpmSetupNetLatencyConfigServerRowStatus = _ArrisNpmSetupNetLatencyConfigServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 6, 1, 4),
    _ArrisNpmSetupNetLatencyConfigServerRowStatus_Type()
)
arrisNpmSetupNetLatencyConfigServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    arrisNpmSetupNetLatencyConfigServerRowStatus.setStatus("current")
_ArrisNpmResultNetLatencyTestTable_Object = MibTable
arrisNpmResultNetLatencyTestTable = _ArrisNpmResultNetLatencyTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 7)
)
if mibBuilder.loadTexts:
    arrisNpmResultNetLatencyTestTable.setStatus("current")
_ArrisNpmResultNetLatencyTestEntry_Object = MibTableRow
arrisNpmResultNetLatencyTestEntry = _ArrisNpmResultNetLatencyTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 7, 1)
)
arrisNpmResultNetLatencyTestEntry.setIndexNames(
    (0, "ARRIS-NET-PERF-MONITOR-MIB", "arrisNpmSetupNetLatencyConfigIndex"),
)
if mibBuilder.loadTexts:
    arrisNpmResultNetLatencyTestEntry.setStatus("current")


class _ArrisNpmResultNetLatencyTestResult_Type(OctetString):
    """Custom type arrisNpmResultNetLatencyTestResult based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 400),
    )


_ArrisNpmResultNetLatencyTestResult_Type.__name__ = "OctetString"
_ArrisNpmResultNetLatencyTestResult_Object = MibTableColumn
arrisNpmResultNetLatencyTestResult = _ArrisNpmResultNetLatencyTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13, 4, 7, 1, 1),
    _ArrisNpmResultNetLatencyTestResult_Type()
)
arrisNpmResultNetLatencyTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisNpmResultNetLatencyTestResult.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-NET-PERF-MONITOR-MIB",
    **{"arrisNetPerfMonitorMib": arrisNetPerfMonitorMib,
       "arrisNpmSetup": arrisNpmSetup,
       "arrisNpmSetupBgTrafficRateEnable": arrisNpmSetupBgTrafficRateEnable,
       "arrisNpmSetupBgTrafficMaxDownstreamRate": arrisNpmSetupBgTrafficMaxDownstreamRate,
       "arrisNpmSetupBgTrafficMaxUpstreamRate": arrisNpmSetupBgTrafficMaxUpstreamRate,
       "arrisNpmSetupGroupReference": arrisNpmSetupGroupReference,
       "arrisNpmWebDlTest": arrisNpmWebDlTest,
       "arrisNpmSetupWebPageDlTestRunTime": arrisNpmSetupWebPageDlTestRunTime,
       "arrisNpmSetupWebPageDlTestTimeout": arrisNpmSetupWebPageDlTestTimeout,
       "arrisNpmSetupWebPageDlTestTable": arrisNpmSetupWebPageDlTestTable,
       "arrisNpmSetupWebPageDlTestEntry": arrisNpmSetupWebPageDlTestEntry,
       "arrisNpmSetupWebPageDlTestConfigIndex": arrisNpmSetupWebPageDlTestConfigIndex,
       "arrisNpmSetupWebPageDlTestConfigUrl": arrisNpmSetupWebPageDlTestConfigUrl,
       "arrisNpmSetupWebPageDlTestConfigRowStatus": arrisNpmSetupWebPageDlTestConfigRowStatus,
       "arrisNpmResultWebPageDlTestTable": arrisNpmResultWebPageDlTestTable,
       "arrisNpmResultWebPageDlTestEntry": arrisNpmResultWebPageDlTestEntry,
       "arrisNpmResultWebPageDlTestResult": arrisNpmResultWebPageDlTestResult,
       "arrisNpmDnsTest": arrisNpmDnsTest,
       "arrisNpmSetupDnsTestEnable": arrisNpmSetupDnsTestEnable,
       "arrisNpmSetupDnsTestRunTime": arrisNpmSetupDnsTestRunTime,
       "arrisNpmSetupDnsTestRunTimeTimeout": arrisNpmSetupDnsTestRunTimeTimeout,
       "arrisNpmSetupDnsPrimaryServerIpType": arrisNpmSetupDnsPrimaryServerIpType,
       "arrisNpmSetupDnsPrimaryServerIpAddress": arrisNpmSetupDnsPrimaryServerIpAddress,
       "arrisNpmSetupDnsSecondaryServerIpType": arrisNpmSetupDnsSecondaryServerIpType,
       "arrisNpmSetupDnsSecondaryServerIpAddress": arrisNpmSetupDnsSecondaryServerIpAddress,
       "arrisNpmResultDnsTestTable": arrisNpmResultDnsTestTable,
       "arrisNpmResultDnsTestEntry": arrisNpmResultDnsTestEntry,
       "arrisNpmResultDnsTestResultIndex": arrisNpmResultDnsTestResultIndex,
       "arrisNpmResultDnsTestResult": arrisNpmResultDnsTestResult,
       "arrisNpmNetLatencyTest": arrisNpmNetLatencyTest,
       "arrisNpmSetupNetLatencyTestRunUnderLoadEnable": arrisNpmSetupNetLatencyTestRunUnderLoadEnable,
       "arrisNpmSetupNetLatencyTestRunTime": arrisNpmSetupNetLatencyTestRunTime,
       "arrisNpmSetupNetLatencyTestPingCount": arrisNpmSetupNetLatencyTestPingCount,
       "arrisNpmSetupNetLatencyTestPingInterval": arrisNpmSetupNetLatencyTestPingInterval,
       "arrisNpmSetupNetLatencyTestPingTimeout": arrisNpmSetupNetLatencyTestPingTimeout,
       "arrisNpmSetupNetLatencyServerTable": arrisNpmSetupNetLatencyServerTable,
       "arrisNpmSetupNetLatencyServerEntry": arrisNpmSetupNetLatencyServerEntry,
       "arrisNpmSetupNetLatencyConfigIndex": arrisNpmSetupNetLatencyConfigIndex,
       "arrisNpmSetupNetLatencyConfigServer": arrisNpmSetupNetLatencyConfigServer,
       "arrisNpmSetupNetLatencyConfigServerPort": arrisNpmSetupNetLatencyConfigServerPort,
       "arrisNpmSetupNetLatencyConfigServerRowStatus": arrisNpmSetupNetLatencyConfigServerRowStatus,
       "arrisNpmResultNetLatencyTestTable": arrisNpmResultNetLatencyTestTable,
       "arrisNpmResultNetLatencyTestEntry": arrisNpmResultNetLatencyTestEntry,
       "arrisNpmResultNetLatencyTestResult": arrisNpmResultNetLatencyTestResult}
)
