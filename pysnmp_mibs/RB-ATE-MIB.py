# SNMP MIB module (RB-ATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RB-ATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:15 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rainbowAteMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301)
)
if mibBuilder.loadTexts:
    rainbowAteMib.setRevisions(
        ("2006-05-05 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Alvarion_ObjectIdentity = ObjectIdentity
alvarion = _Alvarion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1)
)
_Rainbow_ObjectIdentity = ObjectIdentity
rainbow = _Rainbow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2)
)
_RbAteConfig_ObjectIdentity = ObjectIdentity
rbAteConfig = _RbAteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1)
)


class _RbAteStartTest_Type(Integer32):
    """Custom type rbAteStartTest based on Integer32"""
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
        *(("none", 1),
          ("startFullTest", 2),
          ("startHostTest", 3),
          ("startC5Test", 4))
    )


_RbAteStartTest_Type.__name__ = "Integer32"
_RbAteStartTest_Object = MibScalar
rbAteStartTest = _RbAteStartTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 1),
    _RbAteStartTest_Type()
)
rbAteStartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteStartTest.setStatus("current")


class _RbAteExitTest_Type(Integer32):
    """Custom type rbAteExitTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("exitTest", 2))
    )


_RbAteExitTest_Type.__name__ = "Integer32"
_RbAteExitTest_Object = MibScalar
rbAteExitTest = _RbAteExitTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 2),
    _RbAteExitTest_Type()
)
rbAteExitTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteExitTest.setStatus("current")
_RbAteTimeToRunC5Test_Type = Integer32
_RbAteTimeToRunC5Test_Object = MibScalar
rbAteTimeToRunC5Test = _RbAteTimeToRunC5Test_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 3),
    _RbAteTimeToRunC5Test_Type()
)
rbAteTimeToRunC5Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteTimeToRunC5Test.setStatus("current")


class _RbAteTestStatus_Type(Integer32):
    """Custom type rbAteTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readyForTest", 1),
          ("testInProgress", 2))
    )


_RbAteTestStatus_Type.__name__ = "Integer32"
_RbAteTestStatus_Object = MibScalar
rbAteTestStatus = _RbAteTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 4),
    _RbAteTestStatus_Type()
)
rbAteTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteTestStatus.setStatus("current")


class _RbAteState_Type(Integer32):
    """Custom type rbAteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inWorkingMode", 1),
          ("inAteTestMode", 2))
    )


_RbAteState_Type.__name__ = "Integer32"
_RbAteState_Object = MibScalar
rbAteState = _RbAteState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 5),
    _RbAteState_Type()
)
rbAteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteState.setStatus("current")


class _RbAteTimeOfLastC5Test_Type(DisplayString):
    """Custom type rbAteTimeOfLastC5Test based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbAteTimeOfLastC5Test_Type.__name__ = "DisplayString"
_RbAteTimeOfLastC5Test_Object = MibScalar
rbAteTimeOfLastC5Test = _RbAteTimeOfLastC5Test_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 6),
    _RbAteTimeOfLastC5Test_Type()
)
rbAteTimeOfLastC5Test.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteTimeOfLastC5Test.setStatus("current")


class _RbAteSnmpRelaySupport_Type(Integer32):
    """Custom type rbAteSnmpRelaySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("relayOn", 1),
          ("relayOff", 2))
    )


_RbAteSnmpRelaySupport_Type.__name__ = "Integer32"
_RbAteSnmpRelaySupport_Object = MibScalar
rbAteSnmpRelaySupport = _RbAteSnmpRelaySupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 1, 7),
    _RbAteSnmpRelaySupport_Type()
)
rbAteSnmpRelaySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteSnmpRelaySupport.setStatus("current")
_RbAteClockConfig_ObjectIdentity = ObjectIdentity
rbAteClockConfig = _RbAteClockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2)
)
_RbAteDateDay_Type = Integer32
_RbAteDateDay_Object = MibScalar
rbAteDateDay = _RbAteDateDay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 1),
    _RbAteDateDay_Type()
)
rbAteDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateDay.setStatus("current")


class _RbAteDateDayOfWeek_Type(Integer32):
    """Custom type rbAteDateDayOfWeek based on Integer32"""
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
        *(("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6),
          ("sunday", 7))
    )


_RbAteDateDayOfWeek_Type.__name__ = "Integer32"
_RbAteDateDayOfWeek_Object = MibScalar
rbAteDateDayOfWeek = _RbAteDateDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 2),
    _RbAteDateDayOfWeek_Type()
)
rbAteDateDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateDayOfWeek.setStatus("current")
_RbAteDateMonth_Type = Integer32
_RbAteDateMonth_Object = MibScalar
rbAteDateMonth = _RbAteDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 3),
    _RbAteDateMonth_Type()
)
rbAteDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateMonth.setStatus("current")
_RbAteDateYear_Type = Integer32
_RbAteDateYear_Object = MibScalar
rbAteDateYear = _RbAteDateYear_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 4),
    _RbAteDateYear_Type()
)
rbAteDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateYear.setStatus("current")
_RbAteDateHour_Type = Integer32
_RbAteDateHour_Object = MibScalar
rbAteDateHour = _RbAteDateHour_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 5),
    _RbAteDateHour_Type()
)
rbAteDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateHour.setStatus("current")
_RbAteDateMin_Type = Integer32
_RbAteDateMin_Object = MibScalar
rbAteDateMin = _RbAteDateMin_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 6),
    _RbAteDateMin_Type()
)
rbAteDateMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateMin.setStatus("current")
_RbAteDateSec_Type = Integer32
_RbAteDateSec_Object = MibScalar
rbAteDateSec = _RbAteDateSec_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 2, 7),
    _RbAteDateSec_Type()
)
rbAteDateSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDateSec.setStatus("current")
_RbAteTestResults_ObjectIdentity = ObjectIdentity
rbAteTestResults = _RbAteTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3)
)
_RbAteTestResultsTable_Object = MibTable
rbAteTestResultsTable = _RbAteTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3, 1)
)
if mibBuilder.loadTexts:
    rbAteTestResultsTable.setStatus("current")
_RbAteTestResultsEntry_Object = MibTableRow
rbAteTestResultsEntry = _RbAteTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3, 1, 1)
)
rbAteTestResultsEntry.setIndexNames(
    (0, "RB-ATE-MIB", "rbAteTestType"),
)
if mibBuilder.loadTexts:
    rbAteTestResultsEntry.setStatus("current")


class _RbAteTestType_Type(Integer32):
    """Custom type rbAteTestType based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("flashMemoryTest", 1),
          ("sdRAMMemoryTest", 2),
          ("watchDogTest", 3),
          ("diskOnChipMemoryTest", 4),
          ("tempSensorTest", 5),
          ("i2CBusIntTest", 6),
          ("rs232MonitorTest", 7),
          ("alarmsInOutTest", 8),
          ("acmInOutTest", 9),
          ("gpsTest", 10),
          ("bstSyncTest", 11),
          ("mhzAnd1pps", 12),
          ("bitDcpTest", 13),
          ("bitDcpPhyTest", 14),
          ("bitDcpTluHashTest", 15),
          ("bitExt1PPSTest", 16),
          ("gpsRS422Test", 17))
    )


_RbAteTestType_Type.__name__ = "Integer32"
_RbAteTestType_Object = MibTableColumn
rbAteTestType = _RbAteTestType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3, 1, 1, 1),
    _RbAteTestType_Type()
)
rbAteTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteTestType.setStatus("current")


class _RbAteTestResult_Type(Integer32):
    """Custom type rbAteTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failed", 1))
    )


_RbAteTestResult_Type.__name__ = "Integer32"
_RbAteTestResult_Object = MibTableColumn
rbAteTestResult = _RbAteTestResult_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3, 1, 1, 2),
    _RbAteTestResult_Type()
)
rbAteTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteTestResult.setStatus("current")
_RbAteTestResultVal_Type = Integer32
_RbAteTestResultVal_Object = MibTableColumn
rbAteTestResultVal = _RbAteTestResultVal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3, 1, 1, 3),
    _RbAteTestResultVal_Type()
)
rbAteTestResultVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteTestResultVal.setStatus("current")


class _RbAteTestResultDescription_Type(DisplayString):
    """Custom type rbAteTestResultDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RbAteTestResultDescription_Type.__name__ = "DisplayString"
_RbAteTestResultDescription_Object = MibTableColumn
rbAteTestResultDescription = _RbAteTestResultDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 3, 1, 1, 4),
    _RbAteTestResultDescription_Type()
)
rbAteTestResultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteTestResultDescription.setStatus("current")
_RbAteBurnFuncs_ObjectIdentity = ObjectIdentity
rbAteBurnFuncs = _RbAteBurnFuncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 4)
)


class _RbAteEnterSerialNum_Type(DisplayString):
    """Custom type rbAteEnterSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbAteEnterSerialNum_Type.__name__ = "DisplayString"
_RbAteEnterSerialNum_Object = MibScalar
rbAteEnterSerialNum = _RbAteEnterSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 4, 1),
    _RbAteEnterSerialNum_Type()
)
rbAteEnterSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteEnterSerialNum.setStatus("current")


class _RbAteEnterMacAddress_Type(DisplayString):
    """Custom type rbAteEnterMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RbAteEnterMacAddress_Type.__name__ = "DisplayString"
_RbAteEnterMacAddress_Object = MibScalar
rbAteEnterMacAddress = _RbAteEnterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 4, 2),
    _RbAteEnterMacAddress_Type()
)
rbAteEnterMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteEnterMacAddress.setStatus("current")
_RbAteCleanUpParams_ObjectIdentity = ObjectIdentity
rbAteCleanUpParams = _RbAteCleanUpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 5)
)


class _RbAteDeleteNpuShadowFile_Type(Integer32):
    """Custom type rbAteDeleteNpuShadowFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("delete", 2))
    )


_RbAteDeleteNpuShadowFile_Type.__name__ = "Integer32"
_RbAteDeleteNpuShadowFile_Object = MibScalar
rbAteDeleteNpuShadowFile = _RbAteDeleteNpuShadowFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 5, 1),
    _RbAteDeleteNpuShadowFile_Type()
)
rbAteDeleteNpuShadowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteDeleteNpuShadowFile.setStatus("current")


class _RbAteSetServiceDefault_Type(Integer32):
    """Custom type rbAteSetServiceDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setDefault", 2))
    )


_RbAteSetServiceDefault_Type.__name__ = "Integer32"
_RbAteSetServiceDefault_Object = MibScalar
rbAteSetServiceDefault = _RbAteSetServiceDefault_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 5, 2),
    _RbAteSetServiceDefault_Type()
)
rbAteSetServiceDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteSetServiceDefault.setStatus("current")


class _RbAtePowerOnCntReset_Type(Integer32):
    """Custom type rbAtePowerOnCntReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reset", 2))
    )


_RbAtePowerOnCntReset_Type.__name__ = "Integer32"
_RbAtePowerOnCntReset_Object = MibScalar
rbAtePowerOnCntReset = _RbAtePowerOnCntReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 5, 3),
    _RbAtePowerOnCntReset_Type()
)
rbAtePowerOnCntReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAtePowerOnCntReset.setStatus("current")
_RbAteManualTests_ObjectIdentity = ObjectIdentity
rbAteManualTests = _RbAteManualTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 6)
)


class _RbAteStartDcpTluHashTest_Type(Integer32):
    """Custom type rbAteStartDcpTluHashTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("startTest", 2))
    )


_RbAteStartDcpTluHashTest_Type.__name__ = "Integer32"
_RbAteStartDcpTluHashTest_Object = MibScalar
rbAteStartDcpTluHashTest = _RbAteStartDcpTluHashTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 6, 1),
    _RbAteStartDcpTluHashTest_Type()
)
rbAteStartDcpTluHashTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteStartDcpTluHashTest.setStatus("current")


class _RbAteStartGpsExt1PPSTest_Type(Integer32):
    """Custom type rbAteStartGpsExt1PPSTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("startTest", 2))
    )


_RbAteStartGpsExt1PPSTest_Type.__name__ = "Integer32"
_RbAteStartGpsExt1PPSTest_Object = MibScalar
rbAteStartGpsExt1PPSTest = _RbAteStartGpsExt1PPSTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 6, 2),
    _RbAteStartGpsExt1PPSTest_Type()
)
rbAteStartGpsExt1PPSTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteStartGpsExt1PPSTest.setStatus("current")


class _RbAteStartGpsRS422Test_Type(Integer32):
    """Custom type rbAteStartGpsRS422Test based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("startTest", 2))
    )


_RbAteStartGpsRS422Test_Type.__name__ = "Integer32"
_RbAteStartGpsRS422Test_Object = MibScalar
rbAteStartGpsRS422Test = _RbAteStartGpsRS422Test_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 301, 6, 3),
    _RbAteStartGpsRS422Test_Type()
)
rbAteStartGpsRS422Test.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteStartGpsRS422Test.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RB-ATE-MIB",
    **{"alvarion": alvarion,
       "products": products,
       "rainbow": rainbow,
       "rainbowAteMib": rainbowAteMib,
       "rbAteConfig": rbAteConfig,
       "rbAteStartTest": rbAteStartTest,
       "rbAteExitTest": rbAteExitTest,
       "rbAteTimeToRunC5Test": rbAteTimeToRunC5Test,
       "rbAteTestStatus": rbAteTestStatus,
       "rbAteState": rbAteState,
       "rbAteTimeOfLastC5Test": rbAteTimeOfLastC5Test,
       "rbAteSnmpRelaySupport": rbAteSnmpRelaySupport,
       "rbAteClockConfig": rbAteClockConfig,
       "rbAteDateDay": rbAteDateDay,
       "rbAteDateDayOfWeek": rbAteDateDayOfWeek,
       "rbAteDateMonth": rbAteDateMonth,
       "rbAteDateYear": rbAteDateYear,
       "rbAteDateHour": rbAteDateHour,
       "rbAteDateMin": rbAteDateMin,
       "rbAteDateSec": rbAteDateSec,
       "rbAteTestResults": rbAteTestResults,
       "rbAteTestResultsTable": rbAteTestResultsTable,
       "rbAteTestResultsEntry": rbAteTestResultsEntry,
       "rbAteTestType": rbAteTestType,
       "rbAteTestResult": rbAteTestResult,
       "rbAteTestResultVal": rbAteTestResultVal,
       "rbAteTestResultDescription": rbAteTestResultDescription,
       "rbAteBurnFuncs": rbAteBurnFuncs,
       "rbAteEnterSerialNum": rbAteEnterSerialNum,
       "rbAteEnterMacAddress": rbAteEnterMacAddress,
       "rbAteCleanUpParams": rbAteCleanUpParams,
       "rbAteDeleteNpuShadowFile": rbAteDeleteNpuShadowFile,
       "rbAteSetServiceDefault": rbAteSetServiceDefault,
       "rbAtePowerOnCntReset": rbAtePowerOnCntReset,
       "rbAteManualTests": rbAteManualTests,
       "rbAteStartDcpTluHashTest": rbAteStartDcpTluHashTest,
       "rbAteStartGpsExt1PPSTest": rbAteStartGpsExt1PPSTest,
       "rbAteStartGpsRS422Test": rbAteStartGpsRS422Test}
)
