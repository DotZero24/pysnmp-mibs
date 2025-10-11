# SNMP MIB module (ADTRAN-GENSLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENSLOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:49 2025
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

(adGenericShelves,) = mibBuilder.importSymbols(
    "ADTRAN-GENCHASSIS-MIB",
    "adGenericShelves")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(AdPresence,
 AdProductIdentifier) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "AdPresence",
    "AdProductIdentifier")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenSlot = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2)
)
if mibBuilder.loadTexts:
    adGenSlot.setRevisions(
        ("2017-03-29 00:00",
         "2016-08-12 00:00",
         "2016-03-14 00:00",
         "2013-05-31 00:00",
         "2012-12-06 00:00",
         "2012-09-21 00:00",
         "2011-10-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenSlotNumber_Type = Integer32
_AdGenSlotNumber_Object = MibScalar
adGenSlotNumber = _AdGenSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 1),
    _AdGenSlotNumber_Type()
)
adGenSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotNumber.setStatus("current")
_AdGenSlotInfoTable_Object = MibTable
adGenSlotInfoTable = _AdGenSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3)
)
if mibBuilder.loadTexts:
    adGenSlotInfoTable.setStatus("current")
_AdGenSlotInfoEntry_Object = MibTableRow
adGenSlotInfoEntry = _AdGenSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1)
)
adGenSlotInfoEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSlotInfoEntry.setStatus("current")
_AdGenSlotInfoIndex_Type = Integer32
_AdGenSlotInfoIndex_Object = MibTableColumn
adGenSlotInfoIndex = _AdGenSlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 1),
    _AdGenSlotInfoIndex_Type()
)
adGenSlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotInfoIndex.setStatus("current")
_AdGenSlotInfoState_Type = AdPresence
_AdGenSlotInfoState_Object = MibTableColumn
adGenSlotInfoState = _AdGenSlotInfoState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 3),
    _AdGenSlotInfoState_Type()
)
adGenSlotInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotInfoState.setStatus("current")
_AdGenSlotProduct_Type = AdProductIdentifier
_AdGenSlotProduct_Object = MibTableColumn
adGenSlotProduct = _AdGenSlotProduct_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 4),
    _AdGenSlotProduct_Type()
)
adGenSlotProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProduct.setStatus("current")


class _AdGenSlotTrapEnable_Type(Integer32):
    """Custom type adGenSlotTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableTraps", 1),
          ("disableTraps", 2))
    )


_AdGenSlotTrapEnable_Type.__name__ = "Integer32"
_AdGenSlotTrapEnable_Object = MibTableColumn
adGenSlotTrapEnable = _AdGenSlotTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 5),
    _AdGenSlotTrapEnable_Type()
)
adGenSlotTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotTrapEnable.setStatus("current")
_AdGenSlotAlarmStatus_Type = OctetString
_AdGenSlotAlarmStatus_Object = MibTableColumn
adGenSlotAlarmStatus = _AdGenSlotAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 6),
    _AdGenSlotAlarmStatus_Type()
)
adGenSlotAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotAlarmStatus.setStatus("current")
_AdGenSlotFaceplate_Type = OctetString
_AdGenSlotFaceplate_Object = MibTableColumn
adGenSlotFaceplate = _AdGenSlotFaceplate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 7),
    _AdGenSlotFaceplate_Type()
)
adGenSlotFaceplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotFaceplate.setStatus("current")


class _AdGenSlotStatServiceState_Type(Integer32):
    """Custom type adGenSlotStatServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oosUas", 2),
          ("oosMA", 3),
          ("fault", 5),
          ("isStbyHot", 8),
          ("isActLock", 9),
          ("isStbyLock", 10))
    )


_AdGenSlotStatServiceState_Type.__name__ = "Integer32"
_AdGenSlotStatServiceState_Object = MibTableColumn
adGenSlotStatServiceState = _AdGenSlotStatServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 8),
    _AdGenSlotStatServiceState_Type()
)
adGenSlotStatServiceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotStatServiceState.setStatus("current")
_AdGenSlotPortNumber_Type = Integer32
_AdGenSlotPortNumber_Object = MibTableColumn
adGenSlotPortNumber = _AdGenSlotPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 9),
    _AdGenSlotPortNumber_Type()
)
adGenSlotPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotPortNumber.setStatus("current")
_AdGenSlotProvVersion_Type = Integer32
_AdGenSlotProvVersion_Object = MibTableColumn
adGenSlotProvVersion = _AdGenSlotProvVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 10),
    _AdGenSlotProvVersion_Type()
)
adGenSlotProvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProvVersion.setStatus("current")
_AdGenSlotTFileName_Type = DisplayString
_AdGenSlotTFileName_Object = MibTableColumn
adGenSlotTFileName = _AdGenSlotTFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 13),
    _AdGenSlotTFileName_Type()
)
adGenSlotTFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotTFileName.setStatus("current")


class _AdGenSlotUpdateSoftware_Type(Integer32):
    """Custom type adGenSlotUpdateSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )


_AdGenSlotUpdateSoftware_Type.__name__ = "Integer32"
_AdGenSlotUpdateSoftware_Object = MibTableColumn
adGenSlotUpdateSoftware = _AdGenSlotUpdateSoftware_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 15),
    _AdGenSlotUpdateSoftware_Type()
)
adGenSlotUpdateSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotUpdateSoftware.setStatus("current")
_AdGenSlotUpdateStatus_Type = DisplayString
_AdGenSlotUpdateStatus_Object = MibTableColumn
adGenSlotUpdateStatus = _AdGenSlotUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 16),
    _AdGenSlotUpdateStatus_Type()
)
adGenSlotUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotUpdateStatus.setStatus("current")
_AdGenSlotUpTime_Type = TimeTicks
_AdGenSlotUpTime_Object = MibTableColumn
adGenSlotUpTime = _AdGenSlotUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 17),
    _AdGenSlotUpTime_Type()
)
adGenSlotUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotUpTime.setStatus("current")


class _AdGenSlotServiceStateOOSMAAlarmEnable_Type(Integer32):
    """Custom type adGenSlotServiceStateOOSMAAlarmEnable based on Integer32"""
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


_AdGenSlotServiceStateOOSMAAlarmEnable_Type.__name__ = "Integer32"
_AdGenSlotServiceStateOOSMAAlarmEnable_Object = MibTableColumn
adGenSlotServiceStateOOSMAAlarmEnable = _AdGenSlotServiceStateOOSMAAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 18),
    _AdGenSlotServiceStateOOSMAAlarmEnable_Type()
)
adGenSlotServiceStateOOSMAAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotServiceStateOOSMAAlarmEnable.setStatus("obsolete")
_AdGenSlotPrimaryBuildDate_Type = DisplayString
_AdGenSlotPrimaryBuildDate_Object = MibTableColumn
adGenSlotPrimaryBuildDate = _AdGenSlotPrimaryBuildDate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 19),
    _AdGenSlotPrimaryBuildDate_Type()
)
adGenSlotPrimaryBuildDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotPrimaryBuildDate.setStatus("current")
_AdGenSlotResetCause_Type = DisplayString
_AdGenSlotResetCause_Object = MibTableColumn
adGenSlotResetCause = _AdGenSlotResetCause_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 20),
    _AdGenSlotResetCause_Type()
)
adGenSlotResetCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotResetCause.setStatus("current")
_AdGenSlotWarmStartCauseIsValid_Type = TruthValue
_AdGenSlotWarmStartCauseIsValid_Object = MibTableColumn
adGenSlotWarmStartCauseIsValid = _AdGenSlotWarmStartCauseIsValid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 21),
    _AdGenSlotWarmStartCauseIsValid_Type()
)
adGenSlotWarmStartCauseIsValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotWarmStartCauseIsValid.setStatus("current")
_AdGenSlotWarmStartCause_Type = DisplayString
_AdGenSlotWarmStartCause_Object = MibTableColumn
adGenSlotWarmStartCause = _AdGenSlotWarmStartCause_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 22),
    _AdGenSlotWarmStartCause_Type()
)
adGenSlotWarmStartCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotWarmStartCause.setStatus("current")
_AdGenSlotUpTimeSeconds_Type = Counter32
_AdGenSlotUpTimeSeconds_Object = MibTableColumn
adGenSlotUpTimeSeconds = _AdGenSlotUpTimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 3, 1, 23),
    _AdGenSlotUpTimeSeconds_Type()
)
adGenSlotUpTimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotUpTimeSeconds.setStatus("current")
_AdGenSlotProdTable_Object = MibTable
adGenSlotProdTable = _AdGenSlotProdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4)
)
if mibBuilder.loadTexts:
    adGenSlotProdTable.setStatus("current")
_AdGenSlotProdEntry_Object = MibTableRow
adGenSlotProdEntry = _AdGenSlotProdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1)
)
adGenSlotProdEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSlotProdEntry.setStatus("current")
_AdGenSlotProdName_Type = DisplayString
_AdGenSlotProdName_Object = MibTableColumn
adGenSlotProdName = _AdGenSlotProdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 1),
    _AdGenSlotProdName_Type()
)
adGenSlotProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdName.setStatus("current")
_AdGenSlotProdPartNumber_Type = DisplayString
_AdGenSlotProdPartNumber_Object = MibTableColumn
adGenSlotProdPartNumber = _AdGenSlotProdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 2),
    _AdGenSlotProdPartNumber_Type()
)
adGenSlotProdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdPartNumber.setStatus("current")
_AdGenSlotProdCLEIcode_Type = DisplayString
_AdGenSlotProdCLEIcode_Object = MibTableColumn
adGenSlotProdCLEIcode = _AdGenSlotProdCLEIcode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 3),
    _AdGenSlotProdCLEIcode_Type()
)
adGenSlotProdCLEIcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdCLEIcode.setStatus("current")
_AdGenSlotProdSerialNumber_Type = DisplayString
_AdGenSlotProdSerialNumber_Object = MibTableColumn
adGenSlotProdSerialNumber = _AdGenSlotProdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 4),
    _AdGenSlotProdSerialNumber_Type()
)
adGenSlotProdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdSerialNumber.setStatus("current")
_AdGenSlotProdRevision_Type = DisplayString
_AdGenSlotProdRevision_Object = MibTableColumn
adGenSlotProdRevision = _AdGenSlotProdRevision_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 5),
    _AdGenSlotProdRevision_Type()
)
adGenSlotProdRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdRevision.setStatus("current")
_AdGenSlotProdSwVersion_Type = DisplayString
_AdGenSlotProdSwVersion_Object = MibTableColumn
adGenSlotProdSwVersion = _AdGenSlotProdSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 6),
    _AdGenSlotProdSwVersion_Type()
)
adGenSlotProdSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdSwVersion.setStatus("current")
_AdGenSlotProdPhysAddress_Type = PhysAddress
_AdGenSlotProdPhysAddress_Object = MibTableColumn
adGenSlotProdPhysAddress = _AdGenSlotProdPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 7),
    _AdGenSlotProdPhysAddress_Type()
)
adGenSlotProdPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdPhysAddress.setStatus("current")
_AdGenSlotProdProductID_Type = ObjectIdentifier
_AdGenSlotProdProductID_Object = MibTableColumn
adGenSlotProdProductID = _AdGenSlotProdProductID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 8),
    _AdGenSlotProdProductID_Type()
)
adGenSlotProdProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdProductID.setStatus("current")
_AdGenSlotProdTransType_Type = DisplayString
_AdGenSlotProdTransType_Object = MibTableColumn
adGenSlotProdTransType = _AdGenSlotProdTransType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 4, 1, 9),
    _AdGenSlotProdTransType_Type()
)
adGenSlotProdTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotProdTransType.setStatus("current")
_AdGenSlotAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenSlotAlarmsPrefix = _AdGenSlotAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5)
)
_AdGenSlotAlarms_ObjectIdentity = ObjectIdentity
adGenSlotAlarms = _AdGenSlotAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0)
)
_AdGenSlotProvCpuRateLimitAlarmSlotTable_Object = MibTable
adGenSlotProvCpuRateLimitAlarmSlotTable = _AdGenSlotProvCpuRateLimitAlarmSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 9)
)
if mibBuilder.loadTexts:
    adGenSlotProvCpuRateLimitAlarmSlotTable.setStatus("current")
_AdGenSlotProvCpuRateLimitAlarmSlotEntry_Object = MibTableRow
adGenSlotProvCpuRateLimitAlarmSlotEntry = _AdGenSlotProvCpuRateLimitAlarmSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 9, 1)
)
adGenSlotProvCpuRateLimitAlarmSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSlotProvCpuRateLimitAlarmSlotEntry.setStatus("current")


class _AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Type(Integer32):
    """Custom type adGenSlotProvCpuRateLimitAlarmSlotSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Type.__name__ = "Integer32"
_AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Object = MibTableColumn
adGenSlotProvCpuRateLimitAlarmSlotSeverity = _AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 9, 1, 1),
    _AdGenSlotProvCpuRateLimitAlarmSlotSeverity_Type()
)
adGenSlotProvCpuRateLimitAlarmSlotSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotProvCpuRateLimitAlarmSlotSeverity.setStatus("current")


class _AdGenSlotProvCpuRateLimitAlarmSlotEnable_Type(TruthValue):
    """Custom type adGenSlotProvCpuRateLimitAlarmSlotEnable based on TruthValue"""
    defaultValue = 1


_AdGenSlotProvCpuRateLimitAlarmSlotEnable_Type.__name__ = "TruthValue"
_AdGenSlotProvCpuRateLimitAlarmSlotEnable_Object = MibTableColumn
adGenSlotProvCpuRateLimitAlarmSlotEnable = _AdGenSlotProvCpuRateLimitAlarmSlotEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 9, 1, 2),
    _AdGenSlotProvCpuRateLimitAlarmSlotEnable_Type()
)
adGenSlotProvCpuRateLimitAlarmSlotEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSlotProvCpuRateLimitAlarmSlotEnable.setStatus("current")
_AdGenSlotConformance_ObjectIdentity = ObjectIdentity
adGenSlotConformance = _AdGenSlotConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 99)
)
_AdGenSlotCompliances_ObjectIdentity = ObjectIdentity
adGenSlotCompliances = _AdGenSlotCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 99, 1)
)
_AdGenSlotMIBGroups_ObjectIdentity = ObjectIdentity
adGenSlotMIBGroups = _AdGenSlotMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 99, 2)
)

# Managed Objects groups

adGenSlotBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 99, 2, 1)
)
adGenSlotBaseGroup.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotNumber"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoState"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProduct"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotTrapEnable"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotFaceplate"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotStatServiceState"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotPortNumber"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProvVersion"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotTFileName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotUpdateSoftware"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotUpdateStatus"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotUpTime"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdPartNumber"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdCLEIcode"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdSerialNumber"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdRevision"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdSwVersion"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdPhysAddress"))
)
if mibBuilder.loadTexts:
    adGenSlotBaseGroup.setStatus("current")

adGenSlotOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 99, 2, 2)
)
adGenSlotOptionalGroup.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotProdProductID"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdTransType"))
)
if mibBuilder.loadTexts:
    adGenSlotOptionalGroup.setStatus("current")


# Notification objects

adGenSlotServiceStateOOSMAClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0, 1)
)
adGenSlotServiceStateOOSMAClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenSlotServiceStateOOSMAClear.setStatus(
        "obsolete"
    )

adGenSlotServiceStateOOSMAActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0, 2)
)
adGenSlotServiceStateOOSMAActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenSlotServiceStateOOSMAActive.setStatus(
        "obsolete"
    )

adGenSlotFpgaBistFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0, 3)
)
adGenSlotFpgaBistFailureClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenSlotFpgaBistFailureClear.setStatus(
        "current"
    )

adGenSlotFpgaBistFailureActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0, 4)
)
adGenSlotFpgaBistFailureActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenSlotFpgaBistFailureActive.setStatus(
        "current"
    )

adGenSlotCpuRateLimitAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0, 5)
)
adGenSlotCpuRateLimitAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProvCpuRateLimitAlarmSlotSeverity"))
)
if mibBuilder.loadTexts:
    adGenSlotCpuRateLimitAlarmClear.setStatus(
        "current"
    )

adGenSlotCpuRateLimitAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5, 0, 6)
)
adGenSlotCpuRateLimitAlarmActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProvCpuRateLimitAlarmSlotSeverity"))
)
if mibBuilder.loadTexts:
    adGenSlotCpuRateLimitAlarmActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

adGenSlotCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 99, 1, 1)
)
adGenSlotCompliance.setObjects(
      *(("ADTRAN-GENSLOT-MIB", "adGenSlotBaseGroup"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotOptionalGroup"))
)
if mibBuilder.loadTexts:
    adGenSlotCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENSLOT-MIB",
    **{"adGenSlot": adGenSlot,
       "adGenSlotNumber": adGenSlotNumber,
       "adGenSlotInfoTable": adGenSlotInfoTable,
       "adGenSlotInfoEntry": adGenSlotInfoEntry,
       "adGenSlotInfoIndex": adGenSlotInfoIndex,
       "adGenSlotInfoState": adGenSlotInfoState,
       "adGenSlotProduct": adGenSlotProduct,
       "adGenSlotTrapEnable": adGenSlotTrapEnable,
       "adGenSlotAlarmStatus": adGenSlotAlarmStatus,
       "adGenSlotFaceplate": adGenSlotFaceplate,
       "adGenSlotStatServiceState": adGenSlotStatServiceState,
       "adGenSlotPortNumber": adGenSlotPortNumber,
       "adGenSlotProvVersion": adGenSlotProvVersion,
       "adGenSlotTFileName": adGenSlotTFileName,
       "adGenSlotUpdateSoftware": adGenSlotUpdateSoftware,
       "adGenSlotUpdateStatus": adGenSlotUpdateStatus,
       "adGenSlotUpTime": adGenSlotUpTime,
       "adGenSlotServiceStateOOSMAAlarmEnable": adGenSlotServiceStateOOSMAAlarmEnable,
       "adGenSlotPrimaryBuildDate": adGenSlotPrimaryBuildDate,
       "adGenSlotResetCause": adGenSlotResetCause,
       "adGenSlotWarmStartCauseIsValid": adGenSlotWarmStartCauseIsValid,
       "adGenSlotWarmStartCause": adGenSlotWarmStartCause,
       "adGenSlotUpTimeSeconds": adGenSlotUpTimeSeconds,
       "adGenSlotProdTable": adGenSlotProdTable,
       "adGenSlotProdEntry": adGenSlotProdEntry,
       "adGenSlotProdName": adGenSlotProdName,
       "adGenSlotProdPartNumber": adGenSlotProdPartNumber,
       "adGenSlotProdCLEIcode": adGenSlotProdCLEIcode,
       "adGenSlotProdSerialNumber": adGenSlotProdSerialNumber,
       "adGenSlotProdRevision": adGenSlotProdRevision,
       "adGenSlotProdSwVersion": adGenSlotProdSwVersion,
       "adGenSlotProdPhysAddress": adGenSlotProdPhysAddress,
       "adGenSlotProdProductID": adGenSlotProdProductID,
       "adGenSlotProdTransType": adGenSlotProdTransType,
       "adGenSlotAlarmsPrefix": adGenSlotAlarmsPrefix,
       "adGenSlotAlarms": adGenSlotAlarms,
       "adGenSlotServiceStateOOSMAClear": adGenSlotServiceStateOOSMAClear,
       "adGenSlotServiceStateOOSMAActive": adGenSlotServiceStateOOSMAActive,
       "adGenSlotFpgaBistFailureClear": adGenSlotFpgaBistFailureClear,
       "adGenSlotFpgaBistFailureActive": adGenSlotFpgaBistFailureActive,
       "adGenSlotCpuRateLimitAlarmClear": adGenSlotCpuRateLimitAlarmClear,
       "adGenSlotCpuRateLimitAlarmActive": adGenSlotCpuRateLimitAlarmActive,
       "adGenSlotProvCpuRateLimitAlarmSlotTable": adGenSlotProvCpuRateLimitAlarmSlotTable,
       "adGenSlotProvCpuRateLimitAlarmSlotEntry": adGenSlotProvCpuRateLimitAlarmSlotEntry,
       "adGenSlotProvCpuRateLimitAlarmSlotSeverity": adGenSlotProvCpuRateLimitAlarmSlotSeverity,
       "adGenSlotProvCpuRateLimitAlarmSlotEnable": adGenSlotProvCpuRateLimitAlarmSlotEnable,
       "adGenSlotConformance": adGenSlotConformance,
       "adGenSlotCompliances": adGenSlotCompliances,
       "adGenSlotCompliance": adGenSlotCompliance,
       "adGenSlotMIBGroups": adGenSlotMIBGroups,
       "adGenSlotBaseGroup": adGenSlotBaseGroup,
       "adGenSlotOptionalGroup": adGenSlotOptionalGroup}
)
