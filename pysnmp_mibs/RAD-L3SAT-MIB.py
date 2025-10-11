# SNMP MIB module (RAD-L3SAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-L3SAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:01 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(RadTestResult,) = mibBuilder.importSymbols(
    "RAD-TC",
    "RadTestResult")

(radTest,
 radTestPerfRepResults,
 radTestPrefRepEvents,
 radTestPrefRepProfile,
 radTestPrefRepTest) = mibBuilder.importSymbols(
    "RAD-TEST-MIB",
    "radTest",
    "radTestPerfRepResults",
    "radTestPrefRepEvents",
    "radTestPrefRepProfile",
    "radTestPrefRepTest")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

radL3Sat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadTestIpSizeIndex(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ip64", 1),
          ("ip128", 2),
          ("ip256", 3),
          ("ip512", 4),
          ("ip1024", 5),
          ("ip1280", 6),
          ("ip1500", 7),
          ("ipMtu", 8),
          ("ipCustom", 9))
    )



class RadTestIpSizeValues(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("ip64Val", 0),
          ("ip128Val", 1),
          ("ip256Val", 2),
          ("ip512Val", 3),
          ("ip1024Val", 4),
          ("ip1280Val", 5),
          ("ip1500Val", 6),
          ("ipMtuVal", 7),
          ("ipCustomVal", 8))
    )


# MIB Managed Objects in the order of their OIDs

_L3SatPeerProfileTable_Object = MibTable
l3SatPeerProfileTable = _L3SatPeerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6)
)
if mibBuilder.loadTexts:
    l3SatPeerProfileTable.setStatus("current")
_L3SatPeerProfileEntry_Object = MibTableRow
l3SatPeerProfileEntry = _L3SatPeerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1)
)
l3SatPeerProfileEntry.setIndexNames(
    (1, "RAD-L3SAT-MIB", "l3SatPeerProfileName"),
)
if mibBuilder.loadTexts:
    l3SatPeerProfileEntry.setStatus("current")


class _L3SatPeerProfileName_Type(SnmpAdminString):
    """Custom type l3SatPeerProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_L3SatPeerProfileName_Type.__name__ = "SnmpAdminString"
_L3SatPeerProfileName_Object = MibTableColumn
l3SatPeerProfileName = _L3SatPeerProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 1),
    _L3SatPeerProfileName_Type()
)
l3SatPeerProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatPeerProfileName.setStatus("current")
_L3SatPeerProfileRowStatus_Type = RowStatus
_L3SatPeerProfileRowStatus_Object = MibTableColumn
l3SatPeerProfileRowStatus = _L3SatPeerProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 2),
    _L3SatPeerProfileRowStatus_Type()
)
l3SatPeerProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfileRowStatus.setStatus("current")


class _L3SatPeerProfileL4Port_Type(Unsigned32):
    """Custom type l3SatPeerProfileL4Port based on Unsigned32"""
    defaultValue = 53248

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65504),
    )


_L3SatPeerProfileL4Port_Type.__name__ = "Unsigned32"
_L3SatPeerProfileL4Port_Object = MibTableColumn
l3SatPeerProfileL4Port = _L3SatPeerProfileL4Port_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 3),
    _L3SatPeerProfileL4Port_Type()
)
l3SatPeerProfileL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfileL4Port.setStatus("current")


class _L3SatPeerProfileScope_Type(Bits):
    """Custom type l3SatPeerProfileScope based on Bits"""
    defaultBinValue = "11"

    namedValues = NamedValues(
        *(("configuration", 0),
          ("performance", 1))
    )

_L3SatPeerProfileScope_Type.__name__ = "Bits"
_L3SatPeerProfileScope_Object = MibTableColumn
l3SatPeerProfileScope = _L3SatPeerProfileScope_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 4),
    _L3SatPeerProfileScope_Type()
)
l3SatPeerProfileScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfileScope.setStatus("current")


class _L3SatPeerProfilePolicingTest_Type(Integer32):
    """Custom type l3SatPeerProfilePolicingTest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_L3SatPeerProfilePolicingTest_Type.__name__ = "Integer32"
_L3SatPeerProfilePolicingTest_Object = MibTableColumn
l3SatPeerProfilePolicingTest = _L3SatPeerProfilePolicingTest_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 5),
    _L3SatPeerProfilePolicingTest_Type()
)
l3SatPeerProfilePolicingTest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfilePolicingTest.setStatus("current")


class _L3SatPeerProfileBwSteps_Type(OctetString):
    """Custom type l3SatPeerProfileBwSteps based on OctetString"""
    defaultHexValue = "19324B64"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_L3SatPeerProfileBwSteps_Type.__name__ = "OctetString"
_L3SatPeerProfileBwSteps_Object = MibTableColumn
l3SatPeerProfileBwSteps = _L3SatPeerProfileBwSteps_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 6),
    _L3SatPeerProfileBwSteps_Type()
)
l3SatPeerProfileBwSteps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfileBwSteps.setStatus("current")


class _L3SatPeerProfileConfDuration_Type(Unsigned32):
    """Custom type l3SatPeerProfileConfDuration based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_L3SatPeerProfileConfDuration_Type.__name__ = "Unsigned32"
_L3SatPeerProfileConfDuration_Object = MibTableColumn
l3SatPeerProfileConfDuration = _L3SatPeerProfileConfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 7),
    _L3SatPeerProfileConfDuration_Type()
)
l3SatPeerProfileConfDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfileConfDuration.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerProfileConfDuration.setUnits("seconds")


class _L3SatPeerProfilePerfDuration_Type(Unsigned32):
    """Custom type l3SatPeerProfilePerfDuration based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 7200),
    )


_L3SatPeerProfilePerfDuration_Type.__name__ = "Unsigned32"
_L3SatPeerProfilePerfDuration_Object = MibTableColumn
l3SatPeerProfilePerfDuration = _L3SatPeerProfilePerfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 8),
    _L3SatPeerProfilePerfDuration_Type()
)
l3SatPeerProfilePerfDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfilePerfDuration.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerProfilePerfDuration.setUnits("minutes")


class _L3SatPeerProfileReportType_Type(Integer32):
    """Custom type l3SatPeerProfileReportType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clockSync", 1),
          ("noClockSync", 2))
    )


_L3SatPeerProfileReportType_Type.__name__ = "Integer32"
_L3SatPeerProfileReportType_Object = MibTableColumn
l3SatPeerProfileReportType = _L3SatPeerProfileReportType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 6, 1, 9),
    _L3SatPeerProfileReportType_Type()
)
l3SatPeerProfileReportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfileReportType.setStatus("current")
_L3SatSessionProfileTable_Object = MibTable
l3SatSessionProfileTable = _L3SatSessionProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7)
)
if mibBuilder.loadTexts:
    l3SatSessionProfileTable.setStatus("current")
_L3SatSessionProfileEntry_Object = MibTableRow
l3SatSessionProfileEntry = _L3SatSessionProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1)
)
l3SatSessionProfileEntry.setIndexNames(
    (1, "RAD-L3SAT-MIB", "l3SatSessionProfileName"),
)
if mibBuilder.loadTexts:
    l3SatSessionProfileEntry.setStatus("current")


class _L3SatSessionProfileName_Type(SnmpAdminString):
    """Custom type l3SatSessionProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_L3SatSessionProfileName_Type.__name__ = "SnmpAdminString"
_L3SatSessionProfileName_Object = MibTableColumn
l3SatSessionProfileName = _L3SatSessionProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 1),
    _L3SatSessionProfileName_Type()
)
l3SatSessionProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatSessionProfileName.setStatus("current")
_L3SatSessionProfileRowStatus_Type = RowStatus
_L3SatSessionProfileRowStatus_Object = MibTableColumn
l3SatSessionProfileRowStatus = _L3SatSessionProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 2),
    _L3SatSessionProfileRowStatus_Type()
)
l3SatSessionProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfileRowStatus.setStatus("current")


class _L3SatSessionProfileIpSize_Type(RadTestIpSizeValues):
    """Custom type l3SatSessionProfileIpSize based on RadTestIpSizeValues"""
    defaultBinValue = "001"


_L3SatSessionProfileIpSize_Type.__name__ = "RadTestIpSizeValues"
_L3SatSessionProfileIpSize_Object = MibTableColumn
l3SatSessionProfileIpSize = _L3SatSessionProfileIpSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 3),
    _L3SatSessionProfileIpSize_Type()
)
l3SatSessionProfileIpSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfileIpSize.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionProfileIpSize.setUnits("bytes")


class _L3SatSessionProfileIpCustomSize_Type(Unsigned32):
    """Custom type l3SatSessionProfileIpCustomSize based on Unsigned32"""
    defaultValue = 576

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(52, 2094),
    )


_L3SatSessionProfileIpCustomSize_Type.__name__ = "Unsigned32"
_L3SatSessionProfileIpCustomSize_Object = MibTableColumn
l3SatSessionProfileIpCustomSize = _L3SatSessionProfileIpCustomSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 4),
    _L3SatSessionProfileIpCustomSize_Type()
)
l3SatSessionProfileIpCustomSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfileIpCustomSize.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionProfileIpCustomSize.setUnits("bytes")


class _L3SatSessionProfilePlrThreshold_Type(Unsigned32):
    """Custom type l3SatSessionProfilePlrThreshold based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_L3SatSessionProfilePlrThreshold_Type.__name__ = "Unsigned32"
_L3SatSessionProfilePlrThreshold_Object = MibTableColumn
l3SatSessionProfilePlrThreshold = _L3SatSessionProfilePlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 5),
    _L3SatSessionProfilePlrThreshold_Type()
)
l3SatSessionProfilePlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfilePlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionProfilePlrThreshold.setUnits("ppm")


class _L3SatSessionProfilePtdThreshold_Type(Unsigned32):
    """Custom type l3SatSessionProfilePtdThreshold based on Unsigned32"""
    defaultValue = 200000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_L3SatSessionProfilePtdThreshold_Type.__name__ = "Unsigned32"
_L3SatSessionProfilePtdThreshold_Object = MibTableColumn
l3SatSessionProfilePtdThreshold = _L3SatSessionProfilePtdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 6),
    _L3SatSessionProfilePtdThreshold_Type()
)
l3SatSessionProfilePtdThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfilePtdThreshold.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionProfilePtdThreshold.setUnits("micro seconds")


class _L3SatSessionProfilePdvThreshold_Type(Unsigned32):
    """Custom type l3SatSessionProfilePdvThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_L3SatSessionProfilePdvThreshold_Type.__name__ = "Unsigned32"
_L3SatSessionProfilePdvThreshold_Object = MibTableColumn
l3SatSessionProfilePdvThreshold = _L3SatSessionProfilePdvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 7),
    _L3SatSessionProfilePdvThreshold_Type()
)
l3SatSessionProfilePdvThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfilePdvThreshold.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionProfilePdvThreshold.setUnits("micro seconds")


class _L3SatSessionProfileAvailThreshold_Type(Unsigned32):
    """Custom type l3SatSessionProfileAvailThreshold based on Unsigned32"""
    defaultValue = 9990

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_L3SatSessionProfileAvailThreshold_Type.__name__ = "Unsigned32"
_L3SatSessionProfileAvailThreshold_Object = MibTableColumn
l3SatSessionProfileAvailThreshold = _L3SatSessionProfileAvailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 1, 7, 1, 8),
    _L3SatSessionProfileAvailThreshold_Type()
)
l3SatSessionProfileAvailThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfileAvailThreshold.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionProfileAvailThreshold.setUnits("hundredth of percent")
_L3SatGeneratorTable_Object = MibTable
l3SatGeneratorTable = _L3SatGeneratorTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11)
)
if mibBuilder.loadTexts:
    l3SatGeneratorTable.setStatus("current")
_L3SatGeneratorEntry_Object = MibTableRow
l3SatGeneratorEntry = _L3SatGeneratorEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1)
)
l3SatGeneratorEntry.setIndexNames(
    (1, "RAD-L3SAT-MIB", "l3SatGeneratorName"),
)
if mibBuilder.loadTexts:
    l3SatGeneratorEntry.setStatus("current")


class _L3SatGeneratorName_Type(SnmpAdminString):
    """Custom type l3SatGeneratorName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_L3SatGeneratorName_Type.__name__ = "SnmpAdminString"
_L3SatGeneratorName_Object = MibTableColumn
l3SatGeneratorName = _L3SatGeneratorName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 1),
    _L3SatGeneratorName_Type()
)
l3SatGeneratorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatGeneratorName.setStatus("current")
_L3SatGeneratorRowStatus_Type = RowStatus
_L3SatGeneratorRowStatus_Object = MibTableColumn
l3SatGeneratorRowStatus = _L3SatGeneratorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 2),
    _L3SatGeneratorRowStatus_Type()
)
l3SatGeneratorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorRowStatus.setStatus("current")


class _L3SatGeneratorApplication_Type(Integer32):
    """Custom type l3SatGeneratorApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pureL3", 1),
          ("l3OverL2", 2))
    )


_L3SatGeneratorApplication_Type.__name__ = "Integer32"
_L3SatGeneratorApplication_Object = MibTableColumn
l3SatGeneratorApplication = _L3SatGeneratorApplication_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 3),
    _L3SatGeneratorApplication_Type()
)
l3SatGeneratorApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorApplication.setStatus("current")


class _L3SatGeneratorInterface_Type(InterfaceIndexOrZero):
    """Custom type l3SatGeneratorInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_L3SatGeneratorInterface_Type.__name__ = "InterfaceIndexOrZero"
_L3SatGeneratorInterface_Object = MibTableColumn
l3SatGeneratorInterface = _L3SatGeneratorInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 4),
    _L3SatGeneratorInterface_Type()
)
l3SatGeneratorInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorInterface.setStatus("current")


class _L3SatGeneratorOuterVlan_Type(Unsigned32):
    """Custom type l3SatGeneratorOuterVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_L3SatGeneratorOuterVlan_Type.__name__ = "Unsigned32"
_L3SatGeneratorOuterVlan_Object = MibTableColumn
l3SatGeneratorOuterVlan = _L3SatGeneratorOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 5),
    _L3SatGeneratorOuterVlan_Type()
)
l3SatGeneratorOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorOuterVlan.setStatus("current")


class _L3SatGeneratorOuterPbit_Type(Unsigned32):
    """Custom type l3SatGeneratorOuterPbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_L3SatGeneratorOuterPbit_Type.__name__ = "Unsigned32"
_L3SatGeneratorOuterPbit_Object = MibTableColumn
l3SatGeneratorOuterPbit = _L3SatGeneratorOuterPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 6),
    _L3SatGeneratorOuterPbit_Type()
)
l3SatGeneratorOuterPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorOuterPbit.setStatus("current")


class _L3SatGeneratorOuterMarkingProfile_Type(Unsigned32):
    """Custom type l3SatGeneratorOuterMarkingProfile based on Unsigned32"""
    defaultValue = 0


_L3SatGeneratorOuterMarkingProfile_Type.__name__ = "Unsigned32"
_L3SatGeneratorOuterMarkingProfile_Object = MibTableColumn
l3SatGeneratorOuterMarkingProfile = _L3SatGeneratorOuterMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 7),
    _L3SatGeneratorOuterMarkingProfile_Type()
)
l3SatGeneratorOuterMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorOuterMarkingProfile.setStatus("current")


class _L3SatGeneratorInnerVlan_Type(Unsigned32):
    """Custom type l3SatGeneratorInnerVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_L3SatGeneratorInnerVlan_Type.__name__ = "Unsigned32"
_L3SatGeneratorInnerVlan_Object = MibTableColumn
l3SatGeneratorInnerVlan = _L3SatGeneratorInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 8),
    _L3SatGeneratorInnerVlan_Type()
)
l3SatGeneratorInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorInnerVlan.setStatus("current")


class _L3SatGeneratorInnerPbit_Type(Unsigned32):
    """Custom type l3SatGeneratorInnerPbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_L3SatGeneratorInnerPbit_Type.__name__ = "Unsigned32"
_L3SatGeneratorInnerPbit_Object = MibTableColumn
l3SatGeneratorInnerPbit = _L3SatGeneratorInnerPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 9),
    _L3SatGeneratorInnerPbit_Type()
)
l3SatGeneratorInnerPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorInnerPbit.setStatus("current")


class _L3SatGeneratorRouterEntity_Type(Unsigned32):
    """Custom type l3SatGeneratorRouterEntity based on Unsigned32"""
    defaultValue = 1


_L3SatGeneratorRouterEntity_Type.__name__ = "Unsigned32"
_L3SatGeneratorRouterEntity_Object = MibTableColumn
l3SatGeneratorRouterEntity = _L3SatGeneratorRouterEntity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 10),
    _L3SatGeneratorRouterEntity_Type()
)
l3SatGeneratorRouterEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorRouterEntity.setStatus("current")
_L3SatGeneratorLocalAddrType_Type = InetAddressType
_L3SatGeneratorLocalAddrType_Object = MibTableColumn
l3SatGeneratorLocalAddrType = _L3SatGeneratorLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 11),
    _L3SatGeneratorLocalAddrType_Type()
)
l3SatGeneratorLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorLocalAddrType.setStatus("current")
_L3SatGeneratorLocalAddr_Type = InetAddress
_L3SatGeneratorLocalAddr_Object = MibTableColumn
l3SatGeneratorLocalAddr = _L3SatGeneratorLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 12),
    _L3SatGeneratorLocalAddr_Type()
)
l3SatGeneratorLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatGeneratorLocalAddr.setStatus("current")
_L3SatGeneratorRouterInterface_Type = InterfaceIndexOrZero
_L3SatGeneratorRouterInterface_Object = MibTableColumn
l3SatGeneratorRouterInterface = _L3SatGeneratorRouterInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 13),
    _L3SatGeneratorRouterInterface_Type()
)
l3SatGeneratorRouterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatGeneratorRouterInterface.setStatus("current")


class _L3SatGeneratorStatus_Type(Integer32):
    """Custom type l3SatGeneratorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("idle", 2),
          ("ready", 3),
          ("inProgress", 4))
    )


_L3SatGeneratorStatus_Type.__name__ = "Integer32"
_L3SatGeneratorStatus_Object = MibTableColumn
l3SatGeneratorStatus = _L3SatGeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 11, 1, 14),
    _L3SatGeneratorStatus_Type()
)
l3SatGeneratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatGeneratorStatus.setStatus("current")
_L3SatPeerTable_Object = MibTable
l3SatPeerTable = _L3SatPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12)
)
if mibBuilder.loadTexts:
    l3SatPeerTable.setStatus("current")
_L3SatPeerEntry_Object = MibTableRow
l3SatPeerEntry = _L3SatPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1)
)
l3SatPeerEntry.setIndexNames(
    (0, "RAD-L3SAT-MIB", "l3SatGeneratorName"),
    (0, "RAD-L3SAT-MIB", "l3SatPeerAddrType"),
    (0, "RAD-L3SAT-MIB", "l3SatPeerAddr"),
)
if mibBuilder.loadTexts:
    l3SatPeerEntry.setStatus("current")
_L3SatPeerAddrType_Type = InetAddressType
_L3SatPeerAddrType_Object = MibTableColumn
l3SatPeerAddrType = _L3SatPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 1),
    _L3SatPeerAddrType_Type()
)
l3SatPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatPeerAddrType.setStatus("current")
_L3SatPeerAddr_Type = InetAddress
_L3SatPeerAddr_Object = MibTableColumn
l3SatPeerAddr = _L3SatPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 2),
    _L3SatPeerAddr_Type()
)
l3SatPeerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatPeerAddr.setStatus("current")
_L3SatPeerRowStatus_Type = RowStatus
_L3SatPeerRowStatus_Object = MibTableColumn
l3SatPeerRowStatus = _L3SatPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 3),
    _L3SatPeerRowStatus_Type()
)
l3SatPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerRowStatus.setStatus("current")


class _L3SatPeerProfile_Type(SnmpAdminString):
    """Custom type l3SatPeerProfile based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_L3SatPeerProfile_Type.__name__ = "SnmpAdminString"
_L3SatPeerProfile_Object = MibTableColumn
l3SatPeerProfile = _L3SatPeerProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 4),
    _L3SatPeerProfile_Type()
)
l3SatPeerProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerProfile.setStatus("current")


class _L3SatPeerCmd_Type(Integer32):
    """Custom type l3SatPeerCmd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_L3SatPeerCmd_Type.__name__ = "Integer32"
_L3SatPeerCmd_Object = MibTableColumn
l3SatPeerCmd = _L3SatPeerCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 5),
    _L3SatPeerCmd_Type()
)
l3SatPeerCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatPeerCmd.setStatus("current")
_L3SatPeerConfChanged_Type = TruthValue
_L3SatPeerConfChanged_Object = MibTableColumn
l3SatPeerConfChanged = _L3SatPeerConfChanged_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 6),
    _L3SatPeerConfChanged_Type()
)
l3SatPeerConfChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerConfChanged.setStatus("current")
_L3SatPeerTimeRemaining_Type = Unsigned32
_L3SatPeerTimeRemaining_Object = MibTableColumn
l3SatPeerTimeRemaining = _L3SatPeerTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 7),
    _L3SatPeerTimeRemaining_Type()
)
l3SatPeerTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerTimeRemaining.setUnits("seconds")


class _L3SatPeerCurrentPhase_Type(Integer32):
    """Custom type l3SatPeerCurrentPhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("configuration", 2),
          ("performance", 3))
    )


_L3SatPeerCurrentPhase_Type.__name__ = "Integer32"
_L3SatPeerCurrentPhase_Object = MibTableColumn
l3SatPeerCurrentPhase = _L3SatPeerCurrentPhase_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 8),
    _L3SatPeerCurrentPhase_Type()
)
l3SatPeerCurrentPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerCurrentPhase.setStatus("current")


class _L3SatPeerTodStatus_Type(Integer32):
    """Custom type l3SatPeerTodStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("sync", 2),
          ("outOfSync", 3))
    )


_L3SatPeerTodStatus_Type.__name__ = "Integer32"
_L3SatPeerTodStatus_Object = MibTableColumn
l3SatPeerTodStatus = _L3SatPeerTodStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 9),
    _L3SatPeerTodStatus_Type()
)
l3SatPeerTodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerTodStatus.setStatus("current")


class _L3SatPeerResponderType_Type(Integer32):
    """Custom type l3SatPeerResponderType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ipLoop", 2),
          ("udpLoop", 3),
          ("loopAndTimestamp", 4))
    )


_L3SatPeerResponderType_Type.__name__ = "Integer32"
_L3SatPeerResponderType_Object = MibTableColumn
l3SatPeerResponderType = _L3SatPeerResponderType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 10),
    _L3SatPeerResponderType_Type()
)
l3SatPeerResponderType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerResponderType.setStatus("current")


class _L3SatPeerMtu_Type(Unsigned32):
    """Custom type l3SatPeerMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(68, 2094),
    )


_L3SatPeerMtu_Type.__name__ = "Unsigned32"
_L3SatPeerMtu_Object = MibTableColumn
l3SatPeerMtu = _L3SatPeerMtu_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 11),
    _L3SatPeerMtu_Type()
)
l3SatPeerMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerMtu.setStatus("current")
_L3SatPeerStartTime_Type = DateAndTime
_L3SatPeerStartTime_Object = MibTableColumn
l3SatPeerStartTime = _L3SatPeerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 12),
    _L3SatPeerStartTime_Type()
)
l3SatPeerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerStartTime.setStatus("current")
_L3SatPeerEndTime_Type = DateAndTime
_L3SatPeerEndTime_Object = MibTableColumn
l3SatPeerEndTime = _L3SatPeerEndTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 13),
    _L3SatPeerEndTime_Type()
)
l3SatPeerEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerEndTime.setStatus("current")
_L3SatPeerTimeElapsed_Type = Unsigned32
_L3SatPeerTimeElapsed_Object = MibTableColumn
l3SatPeerTimeElapsed = _L3SatPeerTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 14),
    _L3SatPeerTimeElapsed_Type()
)
l3SatPeerTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerTimeElapsed.setUnits("seconds")
_L3SatPeerOutOfSyncSeconds_Type = Counter32
_L3SatPeerOutOfSyncSeconds_Object = MibTableColumn
l3SatPeerOutOfSyncSeconds = _L3SatPeerOutOfSyncSeconds_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 15),
    _L3SatPeerOutOfSyncSeconds_Type()
)
l3SatPeerOutOfSyncSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerOutOfSyncSeconds.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerOutOfSyncSeconds.setUnits("seconds")
_L3SatPeerOverAllResult_Type = RadTestResult
_L3SatPeerOverAllResult_Object = MibTableColumn
l3SatPeerOverAllResult = _L3SatPeerOverAllResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 16),
    _L3SatPeerOverAllResult_Type()
)
l3SatPeerOverAllResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerOverAllResult.setStatus("current")


class _L3SatPeerConfDuration_Type(Unsigned32):
    """Custom type l3SatPeerConfDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_L3SatPeerConfDuration_Type.__name__ = "Unsigned32"
_L3SatPeerConfDuration_Object = MibTableColumn
l3SatPeerConfDuration = _L3SatPeerConfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 17),
    _L3SatPeerConfDuration_Type()
)
l3SatPeerConfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerConfDuration.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerConfDuration.setUnits("seconds")


class _L3SatPeerPerfDuration_Type(Unsigned32):
    """Custom type l3SatPeerPerfDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 7200),
    )


_L3SatPeerPerfDuration_Type.__name__ = "Unsigned32"
_L3SatPeerPerfDuration_Object = MibTableColumn
l3SatPeerPerfDuration = _L3SatPeerPerfDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 18),
    _L3SatPeerPerfDuration_Type()
)
l3SatPeerPerfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerPerfDuration.setStatus("current")
if mibBuilder.loadTexts:
    l3SatPeerPerfDuration.setUnits("minutes")


class _L3SatPeerScope_Type(Bits):
    """Custom type l3SatPeerScope based on Bits"""
    namedValues = NamedValues(
        *(("configuration", 0),
          ("performance", 1))
    )

_L3SatPeerScope_Type.__name__ = "Bits"
_L3SatPeerScope_Object = MibTableColumn
l3SatPeerScope = _L3SatPeerScope_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 19),
    _L3SatPeerScope_Type()
)
l3SatPeerScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerScope.setStatus("current")


class _L3SatPeerConnectivityResult_Type(Integer32):
    """Custom type l3SatPeerConnectivityResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("passed", 2),
          ("failed", 3))
    )


_L3SatPeerConnectivityResult_Type.__name__ = "Integer32"
_L3SatPeerConnectivityResult_Object = MibTableColumn
l3SatPeerConnectivityResult = _L3SatPeerConnectivityResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 20),
    _L3SatPeerConnectivityResult_Type()
)
l3SatPeerConnectivityResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerConnectivityResult.setStatus("current")


class _L3SatPeerMtuTestResult_Type(Integer32):
    """Custom type l3SatPeerMtuTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("passed", 2),
          ("failed", 3))
    )


_L3SatPeerMtuTestResult_Type.__name__ = "Integer32"
_L3SatPeerMtuTestResult_Object = MibTableColumn
l3SatPeerMtuTestResult = _L3SatPeerMtuTestResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 12, 1, 21),
    _L3SatPeerMtuTestResult_Type()
)
l3SatPeerMtuTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatPeerMtuTestResult.setStatus("current")
_L3SatSessionTable_Object = MibTable
l3SatSessionTable = _L3SatSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13)
)
if mibBuilder.loadTexts:
    l3SatSessionTable.setStatus("current")
_L3SatSessionEntry_Object = MibTableRow
l3SatSessionEntry = _L3SatSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1)
)
l3SatSessionEntry.setIndexNames(
    (0, "RAD-L3SAT-MIB", "l3SatGeneratorName"),
    (0, "RAD-L3SAT-MIB", "l3SatPeerAddrType"),
    (0, "RAD-L3SAT-MIB", "l3SatPeerAddr"),
    (1, "RAD-L3SAT-MIB", "l3SatSessionName"),
)
if mibBuilder.loadTexts:
    l3SatSessionEntry.setStatus("current")


class _L3SatSessionName_Type(SnmpAdminString):
    """Custom type l3SatSessionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_L3SatSessionName_Type.__name__ = "SnmpAdminString"
_L3SatSessionName_Object = MibTableColumn
l3SatSessionName = _L3SatSessionName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 1),
    _L3SatSessionName_Type()
)
l3SatSessionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatSessionName.setStatus("current")
_L3SatSessionRowStatus_Type = RowStatus
_L3SatSessionRowStatus_Object = MibTableColumn
l3SatSessionRowStatus = _L3SatSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 2),
    _L3SatSessionRowStatus_Type()
)
l3SatSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionRowStatus.setStatus("current")


class _L3SatSessionProfile_Type(SnmpAdminString):
    """Custom type l3SatSessionProfile based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_L3SatSessionProfile_Type.__name__ = "SnmpAdminString"
_L3SatSessionProfile_Object = MibTableColumn
l3SatSessionProfile = _L3SatSessionProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 3),
    _L3SatSessionProfile_Type()
)
l3SatSessionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionProfile.setStatus("current")
_L3SatSessionBw_Type = Unsigned32
_L3SatSessionBw_Object = MibTableColumn
l3SatSessionBw = _L3SatSessionBw_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 4),
    _L3SatSessionBw_Type()
)
l3SatSessionBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionBw.setStatus("current")
if mibBuilder.loadTexts:
    l3SatSessionBw.setUnits("kbps")


class _L3SatSessionDscp_Type(Unsigned32):
    """Custom type l3SatSessionDscp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_L3SatSessionDscp_Type.__name__ = "Unsigned32"
_L3SatSessionDscp_Object = MibTableColumn
l3SatSessionDscp = _L3SatSessionDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 5),
    _L3SatSessionDscp_Type()
)
l3SatSessionDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatSessionDscp.setStatus("current")
_L3SatSessionConfChanged_Type = TruthValue
_L3SatSessionConfChanged_Object = MibTableColumn
l3SatSessionConfChanged = _L3SatSessionConfChanged_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 6),
    _L3SatSessionConfChanged_Type()
)
l3SatSessionConfChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionConfChanged.setStatus("current")


class _L3SatSessionStatus_Type(Integer32):
    """Custom type l3SatSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("ready", 2),
          ("inProgress", 3),
          ("passed", 4),
          ("failed", 5),
          ("userAborted", 6),
          ("systemAborte", 7))
    )


_L3SatSessionStatus_Type.__name__ = "Integer32"
_L3SatSessionStatus_Object = MibTableColumn
l3SatSessionStatus = _L3SatSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 7),
    _L3SatSessionStatus_Type()
)
l3SatSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionStatus.setStatus("current")
_L3SatSessionLmSrcPort_Type = InetPortNumber
_L3SatSessionLmSrcPort_Object = MibTableColumn
l3SatSessionLmSrcPort = _L3SatSessionLmSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 8),
    _L3SatSessionLmSrcPort_Type()
)
l3SatSessionLmSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionLmSrcPort.setStatus("current")
_L3SatSessionLmDstPort_Type = InetPortNumber
_L3SatSessionLmDstPort_Object = MibTableColumn
l3SatSessionLmDstPort = _L3SatSessionLmDstPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 9),
    _L3SatSessionLmDstPort_Type()
)
l3SatSessionLmDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionLmDstPort.setStatus("current")
_L3SatSessionDmSrcPort_Type = InetPortNumber
_L3SatSessionDmSrcPort_Object = MibTableColumn
l3SatSessionDmSrcPort = _L3SatSessionDmSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 10),
    _L3SatSessionDmSrcPort_Type()
)
l3SatSessionDmSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionDmSrcPort.setStatus("current")
_L3SatSessionDmDstPort_Type = InetPortNumber
_L3SatSessionDmDstPort_Object = MibTableColumn
l3SatSessionDmDstPort = _L3SatSessionDmDstPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 11),
    _L3SatSessionDmDstPort_Type()
)
l3SatSessionDmDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionDmDstPort.setStatus("current")
_L3SatSessionConfResult_Type = RadTestResult
_L3SatSessionConfResult_Object = MibTableColumn
l3SatSessionConfResult = _L3SatSessionConfResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 12),
    _L3SatSessionConfResult_Type()
)
l3SatSessionConfResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionConfResult.setStatus("current")
_L3SatSessionPerfResult_Type = RadTestResult
_L3SatSessionPerfResult_Object = MibTableColumn
l3SatSessionPerfResult = _L3SatSessionPerfResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 13, 1, 13),
    _L3SatSessionPerfResult_Type()
)
l3SatSessionPerfResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatSessionPerfResult.setStatus("current")
_L3SatResponderTable_Object = MibTable
l3SatResponderTable = _L3SatResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14)
)
if mibBuilder.loadTexts:
    l3SatResponderTable.setStatus("current")
_L3SatResponderEntry_Object = MibTableRow
l3SatResponderEntry = _L3SatResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1)
)
l3SatResponderEntry.setIndexNames(
    (1, "RAD-L3SAT-MIB", "l3SatResponderName"),
)
if mibBuilder.loadTexts:
    l3SatResponderEntry.setStatus("current")


class _L3SatResponderName_Type(SnmpAdminString):
    """Custom type l3SatResponderName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_L3SatResponderName_Type.__name__ = "SnmpAdminString"
_L3SatResponderName_Object = MibTableColumn
l3SatResponderName = _L3SatResponderName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 1),
    _L3SatResponderName_Type()
)
l3SatResponderName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderName.setStatus("current")
_L3SatResponderRowStatus_Type = RowStatus
_L3SatResponderRowStatus_Object = MibTableColumn
l3SatResponderRowStatus = _L3SatResponderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 2),
    _L3SatResponderRowStatus_Type()
)
l3SatResponderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderRowStatus.setStatus("current")


class _L3SatResponderApplication_Type(Integer32):
    """Custom type l3SatResponderApplication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pureL3", 1),
          ("l3OverL2", 2))
    )


_L3SatResponderApplication_Type.__name__ = "Integer32"
_L3SatResponderApplication_Object = MibTableColumn
l3SatResponderApplication = _L3SatResponderApplication_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 3),
    _L3SatResponderApplication_Type()
)
l3SatResponderApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderApplication.setStatus("current")


class _L3SatResponderInterface_Type(InterfaceIndexOrZero):
    """Custom type l3SatResponderInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_L3SatResponderInterface_Type.__name__ = "InterfaceIndexOrZero"
_L3SatResponderInterface_Object = MibTableColumn
l3SatResponderInterface = _L3SatResponderInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 4),
    _L3SatResponderInterface_Type()
)
l3SatResponderInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderInterface.setStatus("current")


class _L3SatResponderOuterVlan_Type(Unsigned32):
    """Custom type l3SatResponderOuterVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_L3SatResponderOuterVlan_Type.__name__ = "Unsigned32"
_L3SatResponderOuterVlan_Object = MibTableColumn
l3SatResponderOuterVlan = _L3SatResponderOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 5),
    _L3SatResponderOuterVlan_Type()
)
l3SatResponderOuterVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderOuterVlan.setStatus("current")


class _L3SatResponderOuterPbit_Type(Unsigned32):
    """Custom type l3SatResponderOuterPbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_L3SatResponderOuterPbit_Type.__name__ = "Unsigned32"
_L3SatResponderOuterPbit_Object = MibTableColumn
l3SatResponderOuterPbit = _L3SatResponderOuterPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 6),
    _L3SatResponderOuterPbit_Type()
)
l3SatResponderOuterPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderOuterPbit.setStatus("current")


class _L3SatResponderOuterMarkingProfile_Type(Unsigned32):
    """Custom type l3SatResponderOuterMarkingProfile based on Unsigned32"""
    defaultValue = 0


_L3SatResponderOuterMarkingProfile_Type.__name__ = "Unsigned32"
_L3SatResponderOuterMarkingProfile_Object = MibTableColumn
l3SatResponderOuterMarkingProfile = _L3SatResponderOuterMarkingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 7),
    _L3SatResponderOuterMarkingProfile_Type()
)
l3SatResponderOuterMarkingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderOuterMarkingProfile.setStatus("current")


class _L3SatResponderInnerVlan_Type(Unsigned32):
    """Custom type l3SatResponderInnerVlan based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_L3SatResponderInnerVlan_Type.__name__ = "Unsigned32"
_L3SatResponderInnerVlan_Object = MibTableColumn
l3SatResponderInnerVlan = _L3SatResponderInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 8),
    _L3SatResponderInnerVlan_Type()
)
l3SatResponderInnerVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderInnerVlan.setStatus("current")


class _L3SatResponderInnerPbit_Type(Unsigned32):
    """Custom type l3SatResponderInnerPbit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_L3SatResponderInnerPbit_Type.__name__ = "Unsigned32"
_L3SatResponderInnerPbit_Object = MibTableColumn
l3SatResponderInnerPbit = _L3SatResponderInnerPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 9),
    _L3SatResponderInnerPbit_Type()
)
l3SatResponderInnerPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderInnerPbit.setStatus("current")


class _L3SatResponderRouterEntity_Type(Unsigned32):
    """Custom type l3SatResponderRouterEntity based on Unsigned32"""
    defaultValue = 1


_L3SatResponderRouterEntity_Type.__name__ = "Unsigned32"
_L3SatResponderRouterEntity_Object = MibTableColumn
l3SatResponderRouterEntity = _L3SatResponderRouterEntity_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 10),
    _L3SatResponderRouterEntity_Type()
)
l3SatResponderRouterEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderRouterEntity.setStatus("current")
_L3SatResponderLocalAddrType_Type = InetAddressType
_L3SatResponderLocalAddrType_Object = MibTableColumn
l3SatResponderLocalAddrType = _L3SatResponderLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 11),
    _L3SatResponderLocalAddrType_Type()
)
l3SatResponderLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderLocalAddrType.setStatus("current")
_L3SatResponderLocalAddr_Type = InetAddress
_L3SatResponderLocalAddr_Object = MibTableColumn
l3SatResponderLocalAddr = _L3SatResponderLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 12),
    _L3SatResponderLocalAddr_Type()
)
l3SatResponderLocalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderLocalAddr.setStatus("current")


class _L3SatResponderL4Port_Type(Unsigned32):
    """Custom type l3SatResponderL4Port based on Unsigned32"""
    defaultValue = 53248

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65504),
    )


_L3SatResponderL4Port_Type.__name__ = "Unsigned32"
_L3SatResponderL4Port_Object = MibTableColumn
l3SatResponderL4Port = _L3SatResponderL4Port_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 13),
    _L3SatResponderL4Port_Type()
)
l3SatResponderL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    l3SatResponderL4Port.setStatus("current")
_L3SatResponderRouterInterface_Type = InterfaceIndexOrZero
_L3SatResponderRouterInterface_Object = MibTableColumn
l3SatResponderRouterInterface = _L3SatResponderRouterInterface_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 14),
    _L3SatResponderRouterInterface_Type()
)
l3SatResponderRouterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatResponderRouterInterface.setStatus("current")


class _L3SatResponderStatus_Type(Integer32):
    """Custom type l3SatResponderStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("idle", 2),
          ("ready", 3))
    )


_L3SatResponderStatus_Type.__name__ = "Integer32"
_L3SatResponderStatus_Object = MibTableColumn
l3SatResponderStatus = _L3SatResponderStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 15),
    _L3SatResponderStatus_Type()
)
l3SatResponderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatResponderStatus.setStatus("current")
_L3SatResponderLmRxPackets_Type = Counter64
_L3SatResponderLmRxPackets_Object = MibTableColumn
l3SatResponderLmRxPackets = _L3SatResponderLmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 16),
    _L3SatResponderLmRxPackets_Type()
)
l3SatResponderLmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatResponderLmRxPackets.setStatus("current")
_L3SatResponderDmRxPackets_Type = Counter64
_L3SatResponderDmRxPackets_Object = MibTableColumn
l3SatResponderDmRxPackets = _L3SatResponderDmRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 2, 14, 1, 17),
    _L3SatResponderDmRxPackets_Type()
)
l3SatResponderDmRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatResponderDmRxPackets.setStatus("current")
_L3SatReportTable_Object = MibTable
l3SatReportTable = _L3SatReportTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11)
)
if mibBuilder.loadTexts:
    l3SatReportTable.setStatus("current")
_L3SatReportEntry_Object = MibTableRow
l3SatReportEntry = _L3SatReportEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1)
)
l3SatReportEntry.setIndexNames(
    (0, "RAD-L3SAT-MIB", "l3SatGeneratorName"),
    (0, "RAD-L3SAT-MIB", "l3SatPeerAddrType"),
    (0, "RAD-L3SAT-MIB", "l3SatPeerAddr"),
    (0, "RAD-L3SAT-MIB", "l3SatSessionName"),
    (0, "RAD-L3SAT-MIB", "l3SatReportIpSize"),
    (0, "RAD-L3SAT-MIB", "l3SatReportTestType"),
)
if mibBuilder.loadTexts:
    l3SatReportEntry.setStatus("current")
_L3SatReportIpSize_Type = RadTestIpSizeIndex
_L3SatReportIpSize_Object = MibTableColumn
l3SatReportIpSize = _L3SatReportIpSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 1),
    _L3SatReportIpSize_Type()
)
l3SatReportIpSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatReportIpSize.setStatus("current")


class _L3SatReportTestType_Type(Integer32):
    """Custom type l3SatReportTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("stepLoad1", 1),
          ("stepLoad2", 2),
          ("stepLoad3", 3),
          ("stepLoad4", 4),
          ("policing", 5),
          ("performance", 6))
    )


_L3SatReportTestType_Type.__name__ = "Integer32"
_L3SatReportTestType_Object = MibTableColumn
l3SatReportTestType = _L3SatReportTestType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 2),
    _L3SatReportTestType_Type()
)
l3SatReportTestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l3SatReportTestType.setStatus("current")
_L3SatReportResult_Type = RadTestResult
_L3SatReportResult_Object = MibTableColumn
l3SatReportResult = _L3SatReportResult_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 3),
    _L3SatReportResult_Type()
)
l3SatReportResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportResult.setStatus("current")
_L3SatReportTxRate_Type = Gauge32
_L3SatReportTxRate_Object = MibTableColumn
l3SatReportTxRate = _L3SatReportTxRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 4),
    _L3SatReportTxRate_Type()
)
l3SatReportTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportTxRate.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportTxRate.setUnits("kbps")
_L3SatReportIrAverage_Type = Gauge32
_L3SatReportIrAverage_Object = MibTableColumn
l3SatReportIrAverage = _L3SatReportIrAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 5),
    _L3SatReportIrAverage_Type()
)
l3SatReportIrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportIrAverage.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportIrAverage.setUnits("kbps")
_L3SatReportTxPackets_Type = Counter64
_L3SatReportTxPackets_Object = MibTableColumn
l3SatReportTxPackets = _L3SatReportTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 6),
    _L3SatReportTxPackets_Type()
)
l3SatReportTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportTxPackets.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportTxPackets.setUnits("packets")
_L3SatReportLostPackets_Type = Counter64
_L3SatReportLostPackets_Object = MibTableColumn
l3SatReportLostPackets = _L3SatReportLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 7),
    _L3SatReportLostPackets_Type()
)
l3SatReportLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportLostPackets.setUnits("packets")
_L3SatReportUas_Type = Counter32
_L3SatReportUas_Object = MibTableColumn
l3SatReportUas = _L3SatReportUas_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 8),
    _L3SatReportUas_Type()
)
l3SatReportUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportUas.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportUas.setUnits("seconds")


class _L3SatReportAvailability_Type(Unsigned32):
    """Custom type l3SatReportAvailability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_L3SatReportAvailability_Type.__name__ = "Unsigned32"
_L3SatReportAvailability_Object = MibTableColumn
l3SatReportAvailability = _L3SatReportAvailability_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 9),
    _L3SatReportAvailability_Type()
)
l3SatReportAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportAvailability.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportAvailability.setUnits("hundredth of percent")
_L3SatReportPtdMin_Type = Gauge32
_L3SatReportPtdMin_Object = MibTableColumn
l3SatReportPtdMin = _L3SatReportPtdMin_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 10),
    _L3SatReportPtdMin_Type()
)
l3SatReportPtdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdMin.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdMin.setUnits("micro seconds")
_L3SatReportPtdAverage_Type = Gauge32
_L3SatReportPtdAverage_Object = MibTableColumn
l3SatReportPtdAverage = _L3SatReportPtdAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 11),
    _L3SatReportPtdAverage_Type()
)
l3SatReportPtdAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdAverage.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdAverage.setUnits("micro seconds")
_L3SatReportPtdMax_Type = Gauge32
_L3SatReportPtdMax_Object = MibTableColumn
l3SatReportPtdMax = _L3SatReportPtdMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 12),
    _L3SatReportPtdMax_Type()
)
l3SatReportPtdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdMax.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdMax.setUnits("micro seconds")
_L3SatReportPtdStd_Type = Gauge32
_L3SatReportPtdStd_Object = MibTableColumn
l3SatReportPtdStd = _L3SatReportPtdStd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 13),
    _L3SatReportPtdStd_Type()
)
l3SatReportPtdStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdStd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdStd.setUnits("micro seconds")
_L3SatReportPdvAverage_Type = Gauge32
_L3SatReportPdvAverage_Object = MibTableColumn
l3SatReportPdvAverage = _L3SatReportPdvAverage_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 14),
    _L3SatReportPdvAverage_Type()
)
l3SatReportPdvAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPdvAverage.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPdvAverage.setUnits("micro seconds")
_L3SatReportPdvMax_Type = Gauge32
_L3SatReportPdvMax_Object = MibTableColumn
l3SatReportPdvMax = _L3SatReportPdvMax_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 15),
    _L3SatReportPdvMax_Type()
)
l3SatReportPdvMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPdvMax.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPdvMax.setUnits("micro seconds")
_L3SatReportIpdvAverageFwd_Type = Gauge32
_L3SatReportIpdvAverageFwd_Object = MibTableColumn
l3SatReportIpdvAverageFwd = _L3SatReportIpdvAverageFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 16),
    _L3SatReportIpdvAverageFwd_Type()
)
l3SatReportIpdvAverageFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportIpdvAverageFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportIpdvAverageFwd.setUnits("micro seconds")
_L3SatReportIpdvMaxFwd_Type = Gauge32
_L3SatReportIpdvMaxFwd_Object = MibTableColumn
l3SatReportIpdvMaxFwd = _L3SatReportIpdvMaxFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 17),
    _L3SatReportIpdvMaxFwd_Type()
)
l3SatReportIpdvMaxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportIpdvMaxFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportIpdvMaxFwd.setUnits("micro seconds")
_L3SatReportIpdvAverageBck_Type = Gauge32
_L3SatReportIpdvAverageBck_Object = MibTableColumn
l3SatReportIpdvAverageBck = _L3SatReportIpdvAverageBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 18),
    _L3SatReportIpdvAverageBck_Type()
)
l3SatReportIpdvAverageBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportIpdvAverageBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportIpdvAverageBck.setUnits("micro seconds")
_L3SatReportIpdvMaxBck_Type = Gauge32
_L3SatReportIpdvMaxBck_Object = MibTableColumn
l3SatReportIpdvMaxBck = _L3SatReportIpdvMaxBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 19),
    _L3SatReportIpdvMaxBck_Type()
)
l3SatReportIpdvMaxBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportIpdvMaxBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportIpdvMaxBck.setUnits("micro seconds")
_L3SatReportDuplicatedPacketsFwd_Type = Counter32
_L3SatReportDuplicatedPacketsFwd_Object = MibTableColumn
l3SatReportDuplicatedPacketsFwd = _L3SatReportDuplicatedPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 20),
    _L3SatReportDuplicatedPacketsFwd_Type()
)
l3SatReportDuplicatedPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportDuplicatedPacketsFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportDuplicatedPacketsFwd.setUnits("packets")
_L3SatReportDuplicatedPacketsBck_Type = Counter32
_L3SatReportDuplicatedPacketsBck_Object = MibTableColumn
l3SatReportDuplicatedPacketsBck = _L3SatReportDuplicatedPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 21),
    _L3SatReportDuplicatedPacketsBck_Type()
)
l3SatReportDuplicatedPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportDuplicatedPacketsBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportDuplicatedPacketsBck.setUnits("packets")
_L3SatReportReorderedPacketsFwd_Type = Counter32
_L3SatReportReorderedPacketsFwd_Object = MibTableColumn
l3SatReportReorderedPacketsFwd = _L3SatReportReorderedPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 22),
    _L3SatReportReorderedPacketsFwd_Type()
)
l3SatReportReorderedPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportReorderedPacketsFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportReorderedPacketsFwd.setUnits("packets")
_L3SatReportReorderedPacketsBck_Type = Counter32
_L3SatReportReorderedPacketsBck_Object = MibTableColumn
l3SatReportReorderedPacketsBck = _L3SatReportReorderedPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 23),
    _L3SatReportReorderedPacketsBck_Type()
)
l3SatReportReorderedPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportReorderedPacketsBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportReorderedPacketsBck.setUnits("packets")
_L3SatReportPtdMinFwd_Type = Gauge32
_L3SatReportPtdMinFwd_Object = MibTableColumn
l3SatReportPtdMinFwd = _L3SatReportPtdMinFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 24),
    _L3SatReportPtdMinFwd_Type()
)
l3SatReportPtdMinFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdMinFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdMinFwd.setUnits("micro seconds")
_L3SatReportPtdAverageFwd_Type = Gauge32
_L3SatReportPtdAverageFwd_Object = MibTableColumn
l3SatReportPtdAverageFwd = _L3SatReportPtdAverageFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 25),
    _L3SatReportPtdAverageFwd_Type()
)
l3SatReportPtdAverageFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdAverageFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdAverageFwd.setUnits("micro seconds")
_L3SatReportPtdMaxFwd_Type = Gauge32
_L3SatReportPtdMaxFwd_Object = MibTableColumn
l3SatReportPtdMaxFwd = _L3SatReportPtdMaxFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 26),
    _L3SatReportPtdMaxFwd_Type()
)
l3SatReportPtdMaxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdMaxFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdMaxFwd.setUnits("micro seconds")
_L3SatReportPtdStdFwd_Type = Gauge32
_L3SatReportPtdStdFwd_Object = MibTableColumn
l3SatReportPtdStdFwd = _L3SatReportPtdStdFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 27),
    _L3SatReportPtdStdFwd_Type()
)
l3SatReportPtdStdFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdStdFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdStdFwd.setUnits("micro seconds")
_L3SatReportPtdMinBck_Type = Gauge32
_L3SatReportPtdMinBck_Object = MibTableColumn
l3SatReportPtdMinBck = _L3SatReportPtdMinBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 28),
    _L3SatReportPtdMinBck_Type()
)
l3SatReportPtdMinBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdMinBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdMinBck.setUnits("micro seconds")
_L3SatReportPtdAverageBck_Type = Gauge32
_L3SatReportPtdAverageBck_Object = MibTableColumn
l3SatReportPtdAverageBck = _L3SatReportPtdAverageBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 29),
    _L3SatReportPtdAverageBck_Type()
)
l3SatReportPtdAverageBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdAverageBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdAverageBck.setUnits("micro seconds")
_L3SatReportPtdMaxBck_Type = Gauge32
_L3SatReportPtdMaxBck_Object = MibTableColumn
l3SatReportPtdMaxBck = _L3SatReportPtdMaxBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 30),
    _L3SatReportPtdMaxBck_Type()
)
l3SatReportPtdMaxBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdMaxBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdMaxBck.setUnits("micro seconds")
_L3SatReportPtdStdBck_Type = Gauge32
_L3SatReportPtdStdBck_Object = MibTableColumn
l3SatReportPtdStdBck = _L3SatReportPtdStdBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 31),
    _L3SatReportPtdStdBck_Type()
)
l3SatReportPtdStdBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPtdStdBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPtdStdBck.setUnits("micro seconds")
_L3SatReportPdvAverageFwd_Type = Gauge32
_L3SatReportPdvAverageFwd_Object = MibTableColumn
l3SatReportPdvAverageFwd = _L3SatReportPdvAverageFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 32),
    _L3SatReportPdvAverageFwd_Type()
)
l3SatReportPdvAverageFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPdvAverageFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPdvAverageFwd.setUnits("micro seconds")
_L3SatReportPdvMaxFwd_Type = Gauge32
_L3SatReportPdvMaxFwd_Object = MibTableColumn
l3SatReportPdvMaxFwd = _L3SatReportPdvMaxFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 33),
    _L3SatReportPdvMaxFwd_Type()
)
l3SatReportPdvMaxFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPdvMaxFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPdvMaxFwd.setUnits("micro seconds")
_L3SatReportPdvAverageBck_Type = Gauge32
_L3SatReportPdvAverageBck_Object = MibTableColumn
l3SatReportPdvAverageBck = _L3SatReportPdvAverageBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 34),
    _L3SatReportPdvAverageBck_Type()
)
l3SatReportPdvAverageBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPdvAverageBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPdvAverageBck.setUnits("micro seconds")
_L3SatReportPdvMaxBck_Type = Gauge32
_L3SatReportPdvMaxBck_Object = MibTableColumn
l3SatReportPdvMaxBck = _L3SatReportPdvMaxBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 35),
    _L3SatReportPdvMaxBck_Type()
)
l3SatReportPdvMaxBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportPdvMaxBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportPdvMaxBck.setUnits("micro seconds")
_L3SatReportValidRxTwampPacketsFwd_Type = Counter64
_L3SatReportValidRxTwampPacketsFwd_Object = MibTableColumn
l3SatReportValidRxTwampPacketsFwd = _L3SatReportValidRxTwampPacketsFwd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 36),
    _L3SatReportValidRxTwampPacketsFwd_Type()
)
l3SatReportValidRxTwampPacketsFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportValidRxTwampPacketsFwd.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportValidRxTwampPacketsFwd.setUnits("packets")
_L3SatReportValidRxTwampPacketsBck_Type = Counter64
_L3SatReportValidRxTwampPacketsBck_Object = MibTableColumn
l3SatReportValidRxTwampPacketsBck = _L3SatReportValidRxTwampPacketsBck_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 3, 11, 1, 37),
    _L3SatReportValidRxTwampPacketsBck_Type()
)
l3SatReportValidRxTwampPacketsBck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    l3SatReportValidRxTwampPacketsBck.setStatus("current")
if mibBuilder.loadTexts:
    l3SatReportValidRxTwampPacketsBck.setUnits("packets")

# Managed Objects groups


# Notification objects

systemL3SatTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 50)
)
systemL3SatTestStart.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-L3SAT-MIB", "l3SatPeerCmd"))
)
if mibBuilder.loadTexts:
    systemL3SatTestStart.setStatus(
        "current"
    )

systemL3SatConfigurationTestEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 51)
)
systemL3SatConfigurationTestEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-L3SAT-MIB", "l3SatPeerCmd"))
)
if mibBuilder.loadTexts:
    systemL3SatConfigurationTestEnd.setStatus(
        "current"
    )

systemL3SatPerformanceTestEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 52)
)
systemL3SatPerformanceTestEnd.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-L3SAT-MIB", "l3SatPeerCmd"))
)
if mibBuilder.loadTexts:
    systemL3SatPerformanceTestEnd.setStatus(
        "current"
    )

systemL3SatResponderActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 53)
)
systemL3SatResponderActivated.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-L3SAT-MIB", "l3SatResponderStatus"))
)
if mibBuilder.loadTexts:
    systemL3SatResponderActivated.setStatus(
        "current"
    )

systemL3SatResponderDeactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 54)
)
systemL3SatResponderDeactivated.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-L3SAT-MIB", "l3SatResponderStatus"))
)
if mibBuilder.loadTexts:
    systemL3SatResponderDeactivated.setStatus(
        "current"
    )

systemL3SatPreliminaryTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 15, 0, 55)
)
systemL3SatPreliminaryTestFailed.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-L3SAT-MIB", "l3SatPeerConnectivityResult"),
        ("RAD-L3SAT-MIB", "l3SatPeerMtuTestResult"))
)
if mibBuilder.loadTexts:
    systemL3SatPreliminaryTestFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-L3SAT-MIB",
    **{"RadTestIpSizeIndex": RadTestIpSizeIndex,
       "RadTestIpSizeValues": RadTestIpSizeValues,
       "systemL3SatTestStart": systemL3SatTestStart,
       "systemL3SatConfigurationTestEnd": systemL3SatConfigurationTestEnd,
       "systemL3SatPerformanceTestEnd": systemL3SatPerformanceTestEnd,
       "systemL3SatResponderActivated": systemL3SatResponderActivated,
       "systemL3SatResponderDeactivated": systemL3SatResponderDeactivated,
       "systemL3SatPreliminaryTestFailed": systemL3SatPreliminaryTestFailed,
       "l3SatPeerProfileTable": l3SatPeerProfileTable,
       "l3SatPeerProfileEntry": l3SatPeerProfileEntry,
       "l3SatPeerProfileName": l3SatPeerProfileName,
       "l3SatPeerProfileRowStatus": l3SatPeerProfileRowStatus,
       "l3SatPeerProfileL4Port": l3SatPeerProfileL4Port,
       "l3SatPeerProfileScope": l3SatPeerProfileScope,
       "l3SatPeerProfilePolicingTest": l3SatPeerProfilePolicingTest,
       "l3SatPeerProfileBwSteps": l3SatPeerProfileBwSteps,
       "l3SatPeerProfileConfDuration": l3SatPeerProfileConfDuration,
       "l3SatPeerProfilePerfDuration": l3SatPeerProfilePerfDuration,
       "l3SatPeerProfileReportType": l3SatPeerProfileReportType,
       "l3SatSessionProfileTable": l3SatSessionProfileTable,
       "l3SatSessionProfileEntry": l3SatSessionProfileEntry,
       "l3SatSessionProfileName": l3SatSessionProfileName,
       "l3SatSessionProfileRowStatus": l3SatSessionProfileRowStatus,
       "l3SatSessionProfileIpSize": l3SatSessionProfileIpSize,
       "l3SatSessionProfileIpCustomSize": l3SatSessionProfileIpCustomSize,
       "l3SatSessionProfilePlrThreshold": l3SatSessionProfilePlrThreshold,
       "l3SatSessionProfilePtdThreshold": l3SatSessionProfilePtdThreshold,
       "l3SatSessionProfilePdvThreshold": l3SatSessionProfilePdvThreshold,
       "l3SatSessionProfileAvailThreshold": l3SatSessionProfileAvailThreshold,
       "l3SatGeneratorTable": l3SatGeneratorTable,
       "l3SatGeneratorEntry": l3SatGeneratorEntry,
       "l3SatGeneratorName": l3SatGeneratorName,
       "l3SatGeneratorRowStatus": l3SatGeneratorRowStatus,
       "l3SatGeneratorApplication": l3SatGeneratorApplication,
       "l3SatGeneratorInterface": l3SatGeneratorInterface,
       "l3SatGeneratorOuterVlan": l3SatGeneratorOuterVlan,
       "l3SatGeneratorOuterPbit": l3SatGeneratorOuterPbit,
       "l3SatGeneratorOuterMarkingProfile": l3SatGeneratorOuterMarkingProfile,
       "l3SatGeneratorInnerVlan": l3SatGeneratorInnerVlan,
       "l3SatGeneratorInnerPbit": l3SatGeneratorInnerPbit,
       "l3SatGeneratorRouterEntity": l3SatGeneratorRouterEntity,
       "l3SatGeneratorLocalAddrType": l3SatGeneratorLocalAddrType,
       "l3SatGeneratorLocalAddr": l3SatGeneratorLocalAddr,
       "l3SatGeneratorRouterInterface": l3SatGeneratorRouterInterface,
       "l3SatGeneratorStatus": l3SatGeneratorStatus,
       "l3SatPeerTable": l3SatPeerTable,
       "l3SatPeerEntry": l3SatPeerEntry,
       "l3SatPeerAddrType": l3SatPeerAddrType,
       "l3SatPeerAddr": l3SatPeerAddr,
       "l3SatPeerRowStatus": l3SatPeerRowStatus,
       "l3SatPeerProfile": l3SatPeerProfile,
       "l3SatPeerCmd": l3SatPeerCmd,
       "l3SatPeerConfChanged": l3SatPeerConfChanged,
       "l3SatPeerTimeRemaining": l3SatPeerTimeRemaining,
       "l3SatPeerCurrentPhase": l3SatPeerCurrentPhase,
       "l3SatPeerTodStatus": l3SatPeerTodStatus,
       "l3SatPeerResponderType": l3SatPeerResponderType,
       "l3SatPeerMtu": l3SatPeerMtu,
       "l3SatPeerStartTime": l3SatPeerStartTime,
       "l3SatPeerEndTime": l3SatPeerEndTime,
       "l3SatPeerTimeElapsed": l3SatPeerTimeElapsed,
       "l3SatPeerOutOfSyncSeconds": l3SatPeerOutOfSyncSeconds,
       "l3SatPeerOverAllResult": l3SatPeerOverAllResult,
       "l3SatPeerConfDuration": l3SatPeerConfDuration,
       "l3SatPeerPerfDuration": l3SatPeerPerfDuration,
       "l3SatPeerScope": l3SatPeerScope,
       "l3SatPeerConnectivityResult": l3SatPeerConnectivityResult,
       "l3SatPeerMtuTestResult": l3SatPeerMtuTestResult,
       "l3SatSessionTable": l3SatSessionTable,
       "l3SatSessionEntry": l3SatSessionEntry,
       "l3SatSessionName": l3SatSessionName,
       "l3SatSessionRowStatus": l3SatSessionRowStatus,
       "l3SatSessionProfile": l3SatSessionProfile,
       "l3SatSessionBw": l3SatSessionBw,
       "l3SatSessionDscp": l3SatSessionDscp,
       "l3SatSessionConfChanged": l3SatSessionConfChanged,
       "l3SatSessionStatus": l3SatSessionStatus,
       "l3SatSessionLmSrcPort": l3SatSessionLmSrcPort,
       "l3SatSessionLmDstPort": l3SatSessionLmDstPort,
       "l3SatSessionDmSrcPort": l3SatSessionDmSrcPort,
       "l3SatSessionDmDstPort": l3SatSessionDmDstPort,
       "l3SatSessionConfResult": l3SatSessionConfResult,
       "l3SatSessionPerfResult": l3SatSessionPerfResult,
       "l3SatResponderTable": l3SatResponderTable,
       "l3SatResponderEntry": l3SatResponderEntry,
       "l3SatResponderName": l3SatResponderName,
       "l3SatResponderRowStatus": l3SatResponderRowStatus,
       "l3SatResponderApplication": l3SatResponderApplication,
       "l3SatResponderInterface": l3SatResponderInterface,
       "l3SatResponderOuterVlan": l3SatResponderOuterVlan,
       "l3SatResponderOuterPbit": l3SatResponderOuterPbit,
       "l3SatResponderOuterMarkingProfile": l3SatResponderOuterMarkingProfile,
       "l3SatResponderInnerVlan": l3SatResponderInnerVlan,
       "l3SatResponderInnerPbit": l3SatResponderInnerPbit,
       "l3SatResponderRouterEntity": l3SatResponderRouterEntity,
       "l3SatResponderLocalAddrType": l3SatResponderLocalAddrType,
       "l3SatResponderLocalAddr": l3SatResponderLocalAddr,
       "l3SatResponderL4Port": l3SatResponderL4Port,
       "l3SatResponderRouterInterface": l3SatResponderRouterInterface,
       "l3SatResponderStatus": l3SatResponderStatus,
       "l3SatResponderLmRxPackets": l3SatResponderLmRxPackets,
       "l3SatResponderDmRxPackets": l3SatResponderDmRxPackets,
       "l3SatReportTable": l3SatReportTable,
       "l3SatReportEntry": l3SatReportEntry,
       "l3SatReportIpSize": l3SatReportIpSize,
       "l3SatReportTestType": l3SatReportTestType,
       "l3SatReportResult": l3SatReportResult,
       "l3SatReportTxRate": l3SatReportTxRate,
       "l3SatReportIrAverage": l3SatReportIrAverage,
       "l3SatReportTxPackets": l3SatReportTxPackets,
       "l3SatReportLostPackets": l3SatReportLostPackets,
       "l3SatReportUas": l3SatReportUas,
       "l3SatReportAvailability": l3SatReportAvailability,
       "l3SatReportPtdMin": l3SatReportPtdMin,
       "l3SatReportPtdAverage": l3SatReportPtdAverage,
       "l3SatReportPtdMax": l3SatReportPtdMax,
       "l3SatReportPtdStd": l3SatReportPtdStd,
       "l3SatReportPdvAverage": l3SatReportPdvAverage,
       "l3SatReportPdvMax": l3SatReportPdvMax,
       "l3SatReportIpdvAverageFwd": l3SatReportIpdvAverageFwd,
       "l3SatReportIpdvMaxFwd": l3SatReportIpdvMaxFwd,
       "l3SatReportIpdvAverageBck": l3SatReportIpdvAverageBck,
       "l3SatReportIpdvMaxBck": l3SatReportIpdvMaxBck,
       "l3SatReportDuplicatedPacketsFwd": l3SatReportDuplicatedPacketsFwd,
       "l3SatReportDuplicatedPacketsBck": l3SatReportDuplicatedPacketsBck,
       "l3SatReportReorderedPacketsFwd": l3SatReportReorderedPacketsFwd,
       "l3SatReportReorderedPacketsBck": l3SatReportReorderedPacketsBck,
       "l3SatReportPtdMinFwd": l3SatReportPtdMinFwd,
       "l3SatReportPtdAverageFwd": l3SatReportPtdAverageFwd,
       "l3SatReportPtdMaxFwd": l3SatReportPtdMaxFwd,
       "l3SatReportPtdStdFwd": l3SatReportPtdStdFwd,
       "l3SatReportPtdMinBck": l3SatReportPtdMinBck,
       "l3SatReportPtdAverageBck": l3SatReportPtdAverageBck,
       "l3SatReportPtdMaxBck": l3SatReportPtdMaxBck,
       "l3SatReportPtdStdBck": l3SatReportPtdStdBck,
       "l3SatReportPdvAverageFwd": l3SatReportPdvAverageFwd,
       "l3SatReportPdvMaxFwd": l3SatReportPdvMaxFwd,
       "l3SatReportPdvAverageBck": l3SatReportPdvAverageBck,
       "l3SatReportPdvMaxBck": l3SatReportPdvMaxBck,
       "l3SatReportValidRxTwampPacketsFwd": l3SatReportValidRxTwampPacketsFwd,
       "l3SatReportValidRxTwampPacketsBck": l3SatReportValidRxTwampPacketsBck,
       "radL3Sat": radL3Sat}
)
