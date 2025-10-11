# SNMP MIB module (RB-MICRO-ATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RB-MICRO-ATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:14 2025
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

rainbowMicroBSTAteMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302)
)
if mibBuilder.loadTexts:
    rainbowMicroBSTAteMib.setRevisions(
        ("2006-03-03 15:00",)
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
_RbAteMicroConfig_ObjectIdentity = ObjectIdentity
rbAteMicroConfig = _RbAteMicroConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 1)
)


class _RbAteMicroStartTest_Type(Integer32):
    """Custom type rbAteMicroStartTest based on Integer32"""
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
        *(("none", 1),
          ("startFullTest", 2),
          ("startHostTest", 3),
          ("startPhysicalTest", 4),
          ("startMonitorTest", 5),
          ("startWatchDogTest", 6))
    )


_RbAteMicroStartTest_Type.__name__ = "Integer32"
_RbAteMicroStartTest_Object = MibScalar
rbAteMicroStartTest = _RbAteMicroStartTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 1, 1),
    _RbAteMicroStartTest_Type()
)
rbAteMicroStartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroStartTest.setStatus("current")
_RbAteMicroTimeToRunPhysicalTest_Type = Integer32
_RbAteMicroTimeToRunPhysicalTest_Object = MibScalar
rbAteMicroTimeToRunPhysicalTest = _RbAteMicroTimeToRunPhysicalTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 1, 2),
    _RbAteMicroTimeToRunPhysicalTest_Type()
)
rbAteMicroTimeToRunPhysicalTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroTimeToRunPhysicalTest.setStatus("current")
_RbAteMicroNumOfPacketsToRunPhysTest_Type = Integer32
_RbAteMicroNumOfPacketsToRunPhysTest_Object = MibScalar
rbAteMicroNumOfPacketsToRunPhysTest = _RbAteMicroNumOfPacketsToRunPhysTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 1, 3),
    _RbAteMicroNumOfPacketsToRunPhysTest_Type()
)
rbAteMicroNumOfPacketsToRunPhysTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroNumOfPacketsToRunPhysTest.setStatus("current")


class _RbAteMicroTestStatus_Type(Integer32):
    """Custom type rbAteMicroTestStatus based on Integer32"""
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


_RbAteMicroTestStatus_Type.__name__ = "Integer32"
_RbAteMicroTestStatus_Object = MibScalar
rbAteMicroTestStatus = _RbAteMicroTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 1, 4),
    _RbAteMicroTestStatus_Type()
)
rbAteMicroTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteMicroTestStatus.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 1, 5),
    _RbAteSnmpRelaySupport_Type()
)
rbAteSnmpRelaySupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteSnmpRelaySupport.setStatus("current")
_RbAteMicroClockConfig_ObjectIdentity = ObjectIdentity
rbAteMicroClockConfig = _RbAteMicroClockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2)
)
_RbAteMicroDateDay_Type = Integer32
_RbAteMicroDateDay_Object = MibScalar
rbAteMicroDateDay = _RbAteMicroDateDay_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 1),
    _RbAteMicroDateDay_Type()
)
rbAteMicroDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateDay.setStatus("current")


class _RbAteMicroDateDayOfWeek_Type(Integer32):
    """Custom type rbAteMicroDateDayOfWeek based on Integer32"""
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


_RbAteMicroDateDayOfWeek_Type.__name__ = "Integer32"
_RbAteMicroDateDayOfWeek_Object = MibScalar
rbAteMicroDateDayOfWeek = _RbAteMicroDateDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 2),
    _RbAteMicroDateDayOfWeek_Type()
)
rbAteMicroDateDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateDayOfWeek.setStatus("current")
_RbAteMicroDateMonth_Type = Integer32
_RbAteMicroDateMonth_Object = MibScalar
rbAteMicroDateMonth = _RbAteMicroDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 3),
    _RbAteMicroDateMonth_Type()
)
rbAteMicroDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateMonth.setStatus("current")
_RbAteMicroDateYear_Type = Integer32
_RbAteMicroDateYear_Object = MibScalar
rbAteMicroDateYear = _RbAteMicroDateYear_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 4),
    _RbAteMicroDateYear_Type()
)
rbAteMicroDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateYear.setStatus("current")
_RbAteMicroDateHour_Type = Integer32
_RbAteMicroDateHour_Object = MibScalar
rbAteMicroDateHour = _RbAteMicroDateHour_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 5),
    _RbAteMicroDateHour_Type()
)
rbAteMicroDateHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateHour.setStatus("current")
_RbAteMicroDateMin_Type = Integer32
_RbAteMicroDateMin_Object = MibScalar
rbAteMicroDateMin = _RbAteMicroDateMin_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 6),
    _RbAteMicroDateMin_Type()
)
rbAteMicroDateMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateMin.setStatus("current")
_RbAteMicroDateSec_Type = Integer32
_RbAteMicroDateSec_Object = MibScalar
rbAteMicroDateSec = _RbAteMicroDateSec_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 2, 7),
    _RbAteMicroDateSec_Type()
)
rbAteMicroDateSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDateSec.setStatus("current")
_RbAteMicroTestResults_ObjectIdentity = ObjectIdentity
rbAteMicroTestResults = _RbAteMicroTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3)
)
_RbAteMicroTestResultsConfig_ObjectIdentity = ObjectIdentity
rbAteMicroTestResultsConfig = _RbAteMicroTestResultsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 1)
)


class _RbAteMicroSaveTestResultsToFlash_Type(Integer32):
    """Custom type rbAteMicroSaveTestResultsToFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("saveResults", 2))
    )


_RbAteMicroSaveTestResultsToFlash_Type.__name__ = "Integer32"
_RbAteMicroSaveTestResultsToFlash_Object = MibScalar
rbAteMicroSaveTestResultsToFlash = _RbAteMicroSaveTestResultsToFlash_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 1, 1),
    _RbAteMicroSaveTestResultsToFlash_Type()
)
rbAteMicroSaveTestResultsToFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroSaveTestResultsToFlash.setStatus("current")


class _RbAteMicroRecallTestResultsFromFlash_Type(Integer32):
    """Custom type rbAteMicroRecallTestResultsFromFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNothing", 1),
          ("recallResults", 2))
    )


_RbAteMicroRecallTestResultsFromFlash_Type.__name__ = "Integer32"
_RbAteMicroRecallTestResultsFromFlash_Object = MibScalar
rbAteMicroRecallTestResultsFromFlash = _RbAteMicroRecallTestResultsFromFlash_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 1, 2),
    _RbAteMicroRecallTestResultsFromFlash_Type()
)
rbAteMicroRecallTestResultsFromFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroRecallTestResultsFromFlash.setStatus("current")
_RbAteMicroTestResultsTab_ObjectIdentity = ObjectIdentity
rbAteMicroTestResultsTab = _RbAteMicroTestResultsTab_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2)
)
_RbAteMicroTestResultsTable_Object = MibTable
rbAteMicroTestResultsTable = _RbAteMicroTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2, 1)
)
if mibBuilder.loadTexts:
    rbAteMicroTestResultsTable.setStatus("current")
_RbAteMicroTestResultsEntry_Object = MibTableRow
rbAteMicroTestResultsEntry = _RbAteMicroTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2, 1, 1)
)
rbAteMicroTestResultsEntry.setIndexNames(
    (0, "RB-MICRO-ATE-MIB", "rbAteMicroTestType"),
)
if mibBuilder.loadTexts:
    rbAteMicroTestResultsEntry.setStatus("current")


class _RbAteMicroTestType_Type(Integer32):
    """Custom type rbAteMicroTestType based on Integer32"""
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
              15)
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
          ("mngEthernetPortTest", 10),
          ("dataEthernetPortTest", 11),
          ("backPlaneEthernetPortTest", 12),
          ("gpsTest", 13),
          ("bstSyncTest", 14),
          ("test16mhzAnd1pps", 15))
    )


_RbAteMicroTestType_Type.__name__ = "Integer32"
_RbAteMicroTestType_Object = MibTableColumn
rbAteMicroTestType = _RbAteMicroTestType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2, 1, 1, 1),
    _RbAteMicroTestType_Type()
)
rbAteMicroTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteMicroTestType.setStatus("current")


class _RbAteMicroTestResult_Type(Integer32):
    """Custom type rbAteMicroTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 0),
          ("failed", 1),
          ("inactive", 2),
          ("notChecked", 3))
    )


_RbAteMicroTestResult_Type.__name__ = "Integer32"
_RbAteMicroTestResult_Object = MibTableColumn
rbAteMicroTestResult = _RbAteMicroTestResult_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2, 1, 1, 2),
    _RbAteMicroTestResult_Type()
)
rbAteMicroTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteMicroTestResult.setStatus("current")
_RbAteMicroTestResultVal_Type = Integer32
_RbAteMicroTestResultVal_Object = MibTableColumn
rbAteMicroTestResultVal = _RbAteMicroTestResultVal_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2, 1, 1, 3),
    _RbAteMicroTestResultVal_Type()
)
rbAteMicroTestResultVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteMicroTestResultVal.setStatus("current")


class _RbAteMicroTestResultDescription_Type(DisplayString):
    """Custom type rbAteMicroTestResultDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RbAteMicroTestResultDescription_Type.__name__ = "DisplayString"
_RbAteMicroTestResultDescription_Object = MibTableColumn
rbAteMicroTestResultDescription = _RbAteMicroTestResultDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 3, 2, 1, 1, 4),
    _RbAteMicroTestResultDescription_Type()
)
rbAteMicroTestResultDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteMicroTestResultDescription.setStatus("current")
_RbAteMicroBurnFuncs_ObjectIdentity = ObjectIdentity
rbAteMicroBurnFuncs = _RbAteMicroBurnFuncs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 4)
)


class _RbAteMicroEnterSerialNum_Type(DisplayString):
    """Custom type rbAteMicroEnterSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbAteMicroEnterSerialNum_Type.__name__ = "DisplayString"
_RbAteMicroEnterSerialNum_Object = MibScalar
rbAteMicroEnterSerialNum = _RbAteMicroEnterSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 4, 1),
    _RbAteMicroEnterSerialNum_Type()
)
rbAteMicroEnterSerialNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroEnterSerialNum.setStatus("current")


class _RbAteMicroEnterDataMacAddr_Type(DisplayString):
    """Custom type rbAteMicroEnterDataMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RbAteMicroEnterDataMacAddr_Type.__name__ = "DisplayString"
_RbAteMicroEnterDataMacAddr_Object = MibScalar
rbAteMicroEnterDataMacAddr = _RbAteMicroEnterDataMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 4, 2),
    _RbAteMicroEnterDataMacAddr_Type()
)
rbAteMicroEnterDataMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroEnterDataMacAddr.setStatus("current")


class _RbAteMicroEnterMngmntMacAddr_Type(DisplayString):
    """Custom type rbAteMicroEnterMngmntMacAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_RbAteMicroEnterMngmntMacAddr_Type.__name__ = "DisplayString"
_RbAteMicroEnterMngmntMacAddr_Object = MibScalar
rbAteMicroEnterMngmntMacAddr = _RbAteMicroEnterMngmntMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 4, 3),
    _RbAteMicroEnterMngmntMacAddr_Type()
)
rbAteMicroEnterMngmntMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroEnterMngmntMacAddr.setStatus("current")


class _RbAteMicroGetIduHwRevision_Type(DisplayString):
    """Custom type rbAteMicroGetIduHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbAteMicroGetIduHwRevision_Type.__name__ = "DisplayString"
_RbAteMicroGetIduHwRevision_Object = MibScalar
rbAteMicroGetIduHwRevision = _RbAteMicroGetIduHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 4, 4),
    _RbAteMicroGetIduHwRevision_Type()
)
rbAteMicroGetIduHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAteMicroGetIduHwRevision.setStatus("current")
_RbAteMicroCleanUpParams_ObjectIdentity = ObjectIdentity
rbAteMicroCleanUpParams = _RbAteMicroCleanUpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 5)
)


class _RbAteMicroDeleteNpuShadowFile_Type(Integer32):
    """Custom type rbAteMicroDeleteNpuShadowFile based on Integer32"""
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


_RbAteMicroDeleteNpuShadowFile_Type.__name__ = "Integer32"
_RbAteMicroDeleteNpuShadowFile_Object = MibScalar
rbAteMicroDeleteNpuShadowFile = _RbAteMicroDeleteNpuShadowFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 5, 1),
    _RbAteMicroDeleteNpuShadowFile_Type()
)
rbAteMicroDeleteNpuShadowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroDeleteNpuShadowFile.setStatus("current")


class _RbAteMicroSetServiceDefault_Type(Integer32):
    """Custom type rbAteMicroSetServiceDefault based on Integer32"""
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


_RbAteMicroSetServiceDefault_Type.__name__ = "Integer32"
_RbAteMicroSetServiceDefault_Object = MibScalar
rbAteMicroSetServiceDefault = _RbAteMicroSetServiceDefault_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 5, 2),
    _RbAteMicroSetServiceDefault_Type()
)
rbAteMicroSetServiceDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroSetServiceDefault.setStatus("current")


class _RbAteMicroPowerOnCntReset_Type(Integer32):
    """Custom type rbAteMicroPowerOnCntReset based on Integer32"""
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


_RbAteMicroPowerOnCntReset_Type.__name__ = "Integer32"
_RbAteMicroPowerOnCntReset_Object = MibScalar
rbAteMicroPowerOnCntReset = _RbAteMicroPowerOnCntReset_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 5, 3),
    _RbAteMicroPowerOnCntReset_Type()
)
rbAteMicroPowerOnCntReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteMicroPowerOnCntReset.setStatus("current")
_RbAteManualTests_ObjectIdentity = ObjectIdentity
rbAteManualTests = _RbAteManualTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 6)
)


class _RbAteLedTest_Type(Integer32):
    """Custom type rbAteLedTest based on Integer32"""
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
          ("startTest", 2),
          ("stopTest", 3))
    )


_RbAteLedTest_Type.__name__ = "Integer32"
_RbAteLedTest_Object = MibScalar
rbAteLedTest = _RbAteLedTest_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 302, 6, 1),
    _RbAteLedTest_Type()
)
rbAteLedTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAteLedTest.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RB-MICRO-ATE-MIB",
    **{"alvarion": alvarion,
       "products": products,
       "rainbow": rainbow,
       "rainbowMicroBSTAteMib": rainbowMicroBSTAteMib,
       "rbAteMicroConfig": rbAteMicroConfig,
       "rbAteMicroStartTest": rbAteMicroStartTest,
       "rbAteMicroTimeToRunPhysicalTest": rbAteMicroTimeToRunPhysicalTest,
       "rbAteMicroNumOfPacketsToRunPhysTest": rbAteMicroNumOfPacketsToRunPhysTest,
       "rbAteMicroTestStatus": rbAteMicroTestStatus,
       "rbAteSnmpRelaySupport": rbAteSnmpRelaySupport,
       "rbAteMicroClockConfig": rbAteMicroClockConfig,
       "rbAteMicroDateDay": rbAteMicroDateDay,
       "rbAteMicroDateDayOfWeek": rbAteMicroDateDayOfWeek,
       "rbAteMicroDateMonth": rbAteMicroDateMonth,
       "rbAteMicroDateYear": rbAteMicroDateYear,
       "rbAteMicroDateHour": rbAteMicroDateHour,
       "rbAteMicroDateMin": rbAteMicroDateMin,
       "rbAteMicroDateSec": rbAteMicroDateSec,
       "rbAteMicroTestResults": rbAteMicroTestResults,
       "rbAteMicroTestResultsConfig": rbAteMicroTestResultsConfig,
       "rbAteMicroSaveTestResultsToFlash": rbAteMicroSaveTestResultsToFlash,
       "rbAteMicroRecallTestResultsFromFlash": rbAteMicroRecallTestResultsFromFlash,
       "rbAteMicroTestResultsTab": rbAteMicroTestResultsTab,
       "rbAteMicroTestResultsTable": rbAteMicroTestResultsTable,
       "rbAteMicroTestResultsEntry": rbAteMicroTestResultsEntry,
       "rbAteMicroTestType": rbAteMicroTestType,
       "rbAteMicroTestResult": rbAteMicroTestResult,
       "rbAteMicroTestResultVal": rbAteMicroTestResultVal,
       "rbAteMicroTestResultDescription": rbAteMicroTestResultDescription,
       "rbAteMicroBurnFuncs": rbAteMicroBurnFuncs,
       "rbAteMicroEnterSerialNum": rbAteMicroEnterSerialNum,
       "rbAteMicroEnterDataMacAddr": rbAteMicroEnterDataMacAddr,
       "rbAteMicroEnterMngmntMacAddr": rbAteMicroEnterMngmntMacAddr,
       "rbAteMicroGetIduHwRevision": rbAteMicroGetIduHwRevision,
       "rbAteMicroCleanUpParams": rbAteMicroCleanUpParams,
       "rbAteMicroDeleteNpuShadowFile": rbAteMicroDeleteNpuShadowFile,
       "rbAteMicroSetServiceDefault": rbAteMicroSetServiceDefault,
       "rbAteMicroPowerOnCntReset": rbAteMicroPowerOnCntReset,
       "rbAteManualTests": rbAteManualTests,
       "rbAteLedTest": rbAteLedTest}
)
