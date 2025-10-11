# SNMP MIB module (LANOPTICS-RING-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/LANOPTICS-RING-MANAGER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:42:24 2025
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


# Types definitions



class BITMAP(Integer32):
    """Custom type BITMAP based on Integer32"""




class RING_CONFIGURATION(OctetString):
    """Custom type RING_CONFIGURATION based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LanOptics_ObjectIdentity = ObjectIdentity
lanOptics = _LanOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224)
)
_LanOpticsDot5Monitor_ObjectIdentity = ObjectIdentity
lanOpticsDot5Monitor = _LanOpticsDot5Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 224, 5)
)
_RmServerReportingTo_Type = IpAddress
_RmServerReportingTo_Object = MibScalar
rmServerReportingTo = _RmServerReportingTo_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 1),
    _RmServerReportingTo_Type()
)
rmServerReportingTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmServerReportingTo.setStatus("mandatory")


class _RmRingStatus_Type(Integer32):
    """Custom type rmRingStatus based on Integer32"""
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
        *(("beaconing", 1),
          ("single-station", 2),
          ("errors-increasing", 3),
          ("excessive-errors", 4))
    )


_RmRingStatus_Type.__name__ = "Integer32"
_RmRingStatus_Object = MibScalar
rmRingStatus = _RmRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 2),
    _RmRingStatus_Type()
)
rmRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingStatus.setStatus("mandatory")
_RmServerHealthText_Type = DisplayString
_RmServerHealthText_Object = MibScalar
rmServerHealthText = _RmServerHealthText_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 3),
    _RmServerHealthText_Type()
)
rmServerHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmServerHealthText.setStatus("mandatory")


class _RmServerHealth_Type(Integer32):
    """Custom type rmServerHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initial-State", 1),
          ("not-Active", 2))
    )


_RmServerHealth_Type.__name__ = "Integer32"
_RmServerHealth_Object = MibScalar
rmServerHealth = _RmServerHealth_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 4),
    _RmServerHealth_Type()
)
rmServerHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmServerHealth.setStatus("mandatory")
_RmRingEventInLog_Type = Integer32
_RmRingEventInLog_Object = MibScalar
rmRingEventInLog = _RmRingEventInLog_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 5),
    _RmRingEventInLog_Type()
)
rmRingEventInLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingEventInLog.setStatus("mandatory")
_RmRingEventTable_Object = MibTable
rmRingEventTable = _RmRingEventTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6)
)
if mibBuilder.loadTexts:
    rmRingEventTable.setStatus("mandatory")
_RmRingEventEntry_Object = MibTableRow
rmRingEventEntry = _RmRingEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6, 1)
)
rmRingEventEntry.setIndexNames(
    (0, "LANOPTICS-RING-MANAGER-MIB", "pysmiFakeCol23"),
    (0, "LANOPTICS-RING-MANAGER-MIB", "pysmiFakeCol24"),
    (0, "LANOPTICS-RING-MANAGER-MIB", "pysmiFakeCol25"),
    (0, "LANOPTICS-RING-MANAGER-MIB", "pysmiFakeCol26"),
)
if mibBuilder.loadTexts:
    rmRingEventEntry.setStatus("mandatory")
_RmRingEvent_Type = OctetString
_RmRingEvent_Object = MibTableColumn
rmRingEvent = _RmRingEvent_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6, 1, 1),
    _RmRingEvent_Type()
)
rmRingEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingEvent.setStatus("mandatory")
_PysmiFakeCol26_Type = Integer32
_PysmiFakeCol26_Object = MibTableColumn
pysmiFakeCol26 = _PysmiFakeCol26_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6, 1, 4294967292),
    _PysmiFakeCol26_Type()
)
pysmiFakeCol26.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol26.setStatus("mandatory")
_PysmiFakeCol25_Type = Integer32
_PysmiFakeCol25_Object = MibTableColumn
pysmiFakeCol25 = _PysmiFakeCol25_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6, 1, 4294967293),
    _PysmiFakeCol25_Type()
)
pysmiFakeCol25.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol25.setStatus("mandatory")
_PysmiFakeCol24_Type = Integer32
_PysmiFakeCol24_Object = MibTableColumn
pysmiFakeCol24 = _PysmiFakeCol24_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6, 1, 4294967294),
    _PysmiFakeCol24_Type()
)
pysmiFakeCol24.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol24.setStatus("mandatory")
_PysmiFakeCol23_Type = Integer32
_PysmiFakeCol23_Object = MibTableColumn
pysmiFakeCol23 = _PysmiFakeCol23_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 6, 1, 4294967295),
    _PysmiFakeCol23_Type()
)
pysmiFakeCol23.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol23.setStatus("mandatory")
_RmRingBeaconingStatus_Type = OctetString
_RmRingBeaconingStatus_Object = MibScalar
rmRingBeaconingStatus = _RmRingBeaconingStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 7),
    _RmRingBeaconingStatus_Type()
)
rmRingBeaconingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingBeaconingStatus.setStatus("mandatory")
_RmRingIsoErrorStatus_Type = OctetString
_RmRingIsoErrorStatus_Object = MibScalar
rmRingIsoErrorStatus = _RmRingIsoErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 8),
    _RmRingIsoErrorStatus_Type()
)
rmRingIsoErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingIsoErrorStatus.setStatus("mandatory")
_RmRingSingleStationStatus_Type = OctetString
_RmRingSingleStationStatus_Object = MibScalar
rmRingSingleStationStatus = _RmRingSingleStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 9),
    _RmRingSingleStationStatus_Type()
)
rmRingSingleStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingSingleStationStatus.setStatus("mandatory")
_RmRingFullConfiguration_Type = RING_CONFIGURATION
_RmRingFullConfiguration_Object = MibScalar
rmRingFullConfiguration = _RmRingFullConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 10),
    _RmRingFullConfiguration_Type()
)
rmRingFullConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingFullConfiguration.setStatus("mandatory")
_RmRingConfigurationUpdate_Type = RING_CONFIGURATION
_RmRingConfigurationUpdate_Object = MibScalar
rmRingConfigurationUpdate = _RmRingConfigurationUpdate_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 11),
    _RmRingConfigurationUpdate_Type()
)
rmRingConfigurationUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingConfigurationUpdate.setStatus("mandatory")
_RmServerInitProcess_Type = Integer32
_RmServerInitProcess_Object = MibScalar
rmServerInitProcess = _RmServerInitProcess_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 12),
    _RmServerInitProcess_Type()
)
rmServerInitProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmServerInitProcess.setStatus("mandatory")
_RmServerAdminState_Type = BITMAP
_RmServerAdminState_Object = MibScalar
rmServerAdminState = _RmServerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 13),
    _RmServerAdminState_Type()
)
rmServerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmServerAdminState.setStatus("mandatory")
_RmServerOperatingState_Type = BITMAP
_RmServerOperatingState_Object = MibScalar
rmServerOperatingState = _RmServerOperatingState_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 14),
    _RmServerOperatingState_Type()
)
rmServerOperatingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmServerOperatingState.setStatus("mandatory")
_RmServerAdminParameters_Type = BITMAP
_RmServerAdminParameters_Object = MibScalar
rmServerAdminParameters = _RmServerAdminParameters_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 15),
    _RmServerAdminParameters_Type()
)
rmServerAdminParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmServerAdminParameters.setStatus("mandatory")
_RmServerOperatingParameters_Type = BITMAP
_RmServerOperatingParameters_Object = MibScalar
rmServerOperatingParameters = _RmServerOperatingParameters_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 16),
    _RmServerOperatingParameters_Type()
)
rmServerOperatingParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmServerOperatingParameters.setStatus("mandatory")
_RmDeviceStatusTable_Object = MibTable
rmDeviceStatusTable = _RmDeviceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17)
)
if mibBuilder.loadTexts:
    rmDeviceStatusTable.setStatus("mandatory")
_RmDeviceEntry_Object = MibTableRow
rmDeviceEntry = _RmDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1)
)
rmDeviceEntry.setIndexNames(
    (0, "LANOPTICS-RING-MANAGER-MIB", "rmDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    rmDeviceEntry.setStatus("mandatory")
_RmDeviceMacAddress_Type = PhysAddress
_RmDeviceMacAddress_Object = MibTableColumn
rmDeviceMacAddress = _RmDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 1),
    _RmDeviceMacAddress_Type()
)
rmDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceMacAddress.setStatus("mandatory")
_RmDeviceUpstream_Type = PhysAddress
_RmDeviceUpstream_Object = MibTableColumn
rmDeviceUpstream = _RmDeviceUpstream_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 2),
    _RmDeviceUpstream_Type()
)
rmDeviceUpstream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceUpstream.setStatus("mandatory")


class _RmDeviceAdminState_Type(Integer32):
    """Custom type rmDeviceAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            4
        )
    )
    namedValues = NamedValues(
        ("removed", 4)
    )


_RmDeviceAdminState_Type.__name__ = "Integer32"
_RmDeviceAdminState_Object = MibTableColumn
rmDeviceAdminState = _RmDeviceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 3),
    _RmDeviceAdminState_Type()
)
rmDeviceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmDeviceAdminState.setStatus("mandatory")


class _RmDeviceOperateState_Type(Integer32):
    """Custom type rmDeviceOperateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("removed", 4),
          ("neverInserted", 8))
    )


_RmDeviceOperateState_Type.__name__ = "Integer32"
_RmDeviceOperateState_Object = MibTableColumn
rmDeviceOperateState = _RmDeviceOperateState_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 4),
    _RmDeviceOperateState_Type()
)
rmDeviceOperateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceOperateState.setStatus("mandatory")
_RmDevicePhysLocation_Type = Integer32
_RmDevicePhysLocation_Object = MibTableColumn
rmDevicePhysLocation = _RmDevicePhysLocation_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 5),
    _RmDevicePhysLocation_Type()
)
rmDevicePhysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDevicePhysLocation.setStatus("mandatory")
_RmDeviceGroupAddress_Type = Integer32
_RmDeviceGroupAddress_Object = MibTableColumn
rmDeviceGroupAddress = _RmDeviceGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 6),
    _RmDeviceGroupAddress_Type()
)
rmDeviceGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceGroupAddress.setStatus("mandatory")
_RmDeviceFunctionAddress_Type = Integer32
_RmDeviceFunctionAddress_Object = MibTableColumn
rmDeviceFunctionAddress = _RmDeviceFunctionAddress_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 7),
    _RmDeviceFunctionAddress_Type()
)
rmDeviceFunctionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceFunctionAddress.setStatus("mandatory")
_RmDeviceProductID_Type = OctetString
_RmDeviceProductID_Object = MibTableColumn
rmDeviceProductID = _RmDeviceProductID_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 8),
    _RmDeviceProductID_Type()
)
rmDeviceProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceProductID.setStatus("mandatory")
_RmDeviceStationID_Type = Integer32
_RmDeviceStationID_Object = MibTableColumn
rmDeviceStationID = _RmDeviceStationID_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 9),
    _RmDeviceStationID_Type()
)
rmDeviceStationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceStationID.setStatus("mandatory")
_RmDeviceStationStatus_Type = OctetString
_RmDeviceStationStatus_Object = MibTableColumn
rmDeviceStationStatus = _RmDeviceStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 10),
    _RmDeviceStationStatus_Type()
)
rmDeviceStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceStationStatus.setStatus("mandatory")
_RmDeviceFunctionClass_Type = Integer32
_RmDeviceFunctionClass_Object = MibTableColumn
rmDeviceFunctionClass = _RmDeviceFunctionClass_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 11),
    _RmDeviceFunctionClass_Type()
)
rmDeviceFunctionClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceFunctionClass.setStatus("mandatory")
_RmDeviceAccessPriority_Type = Integer32
_RmDeviceAccessPriority_Object = MibTableColumn
rmDeviceAccessPriority = _RmDeviceAccessPriority_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 12),
    _RmDeviceAccessPriority_Type()
)
rmDeviceAccessPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceAccessPriority.setStatus("mandatory")
_RmDeviceMicroLevel_Type = OctetString
_RmDeviceMicroLevel_Object = MibTableColumn
rmDeviceMicroLevel = _RmDeviceMicroLevel_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 13),
    _RmDeviceMicroLevel_Type()
)
rmDeviceMicroLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceMicroLevel.setStatus("mandatory")
_RmDeviceMonitored_Type = Integer32
_RmDeviceMonitored_Object = MibTableColumn
rmDeviceMonitored = _RmDeviceMonitored_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 14),
    _RmDeviceMonitored_Type()
)
rmDeviceMonitored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceMonitored.setStatus("mandatory")
_RmDeviceDaysAllowed_Type = Integer32
_RmDeviceDaysAllowed_Object = MibTableColumn
rmDeviceDaysAllowed = _RmDeviceDaysAllowed_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 15),
    _RmDeviceDaysAllowed_Type()
)
rmDeviceDaysAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceDaysAllowed.setStatus("mandatory")
_RmDeviceHoursAllowed_Type = Integer32
_RmDeviceHoursAllowed_Object = MibTableColumn
rmDeviceHoursAllowed = _RmDeviceHoursAllowed_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 17, 1, 16),
    _RmDeviceHoursAllowed_Type()
)
rmDeviceHoursAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmDeviceHoursAllowed.setStatus("mandatory")
_RmRingPollProcessStatus_Type = OctetString
_RmRingPollProcessStatus_Object = MibScalar
rmRingPollProcessStatus = _RmRingPollProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 18),
    _RmRingPollProcessStatus_Type()
)
rmRingPollProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingPollProcessStatus.setStatus("mandatory")
_RmRingNumber_Type = Integer32
_RmRingNumber_Object = MibScalar
rmRingNumber = _RmRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 35),
    _RmRingNumber_Type()
)
rmRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingNumber.setStatus("mandatory")
_RmRingSoftErrorTimer_Type = Integer32
_RmRingSoftErrorTimer_Object = MibScalar
rmRingSoftErrorTimer = _RmRingSoftErrorTimer_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 36),
    _RmRingSoftErrorTimer_Type()
)
rmRingSoftErrorTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingSoftErrorTimer.setStatus("mandatory")
_RmRingIsolatingTab_Type = OctetString
_RmRingIsolatingTab_Object = MibScalar
rmRingIsolatingTab = _RmRingIsolatingTab_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 37),
    _RmRingIsolatingTab_Type()
)
rmRingIsolatingTab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingIsolatingTab.setStatus("mandatory")
_RmRingCongestTab_Type = OctetString
_RmRingCongestTab_Object = MibScalar
rmRingCongestTab = _RmRingCongestTab_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 38),
    _RmRingCongestTab_Type()
)
rmRingCongestTab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingCongestTab.setStatus("mandatory")
_RmRingNonIsolatingTab_Type = OctetString
_RmRingNonIsolatingTab_Object = MibScalar
rmRingNonIsolatingTab = _RmRingNonIsolatingTab_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 39),
    _RmRingNonIsolatingTab_Type()
)
rmRingNonIsolatingTab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingNonIsolatingTab.setStatus("mandatory")
_RmRingAutoRemove_Type = Integer32
_RmRingAutoRemove_Object = MibScalar
rmRingAutoRemove = _RmRingAutoRemove_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 42),
    _RmRingAutoRemove_Type()
)
rmRingAutoRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmRingAutoRemove.setStatus("mandatory")


class _RmRingAllowedDaysPartition1_Type(Integer32):
    """Custom type rmRingAllowedDaysPartition1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RmRingAllowedDaysPartition1_Type.__name__ = "Integer32"
_RmRingAllowedDaysPartition1_Object = MibScalar
rmRingAllowedDaysPartition1 = _RmRingAllowedDaysPartition1_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 43),
    _RmRingAllowedDaysPartition1_Type()
)
rmRingAllowedDaysPartition1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmRingAllowedDaysPartition1.setStatus("mandatory")


class _RmRingAllowedDaysPartition2_Type(Integer32):
    """Custom type rmRingAllowedDaysPartition2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RmRingAllowedDaysPartition2_Type.__name__ = "Integer32"
_RmRingAllowedDaysPartition2_Object = MibScalar
rmRingAllowedDaysPartition2 = _RmRingAllowedDaysPartition2_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 44),
    _RmRingAllowedDaysPartition2_Type()
)
rmRingAllowedDaysPartition2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmRingAllowedDaysPartition2.setStatus("mandatory")


class _RmRingAllowedHoursPartition1_Type(Integer32):
    """Custom type rmRingAllowedHoursPartition1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_RmRingAllowedHoursPartition1_Type.__name__ = "Integer32"
_RmRingAllowedHoursPartition1_Object = MibScalar
rmRingAllowedHoursPartition1 = _RmRingAllowedHoursPartition1_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 45),
    _RmRingAllowedHoursPartition1_Type()
)
rmRingAllowedHoursPartition1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmRingAllowedHoursPartition1.setStatus("mandatory")


class _RmRingAllowedHoursPartition2_Type(Integer32):
    """Custom type rmRingAllowedHoursPartition2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_RmRingAllowedHoursPartition2_Type.__name__ = "Integer32"
_RmRingAllowedHoursPartition2_Object = MibScalar
rmRingAllowedHoursPartition2 = _RmRingAllowedHoursPartition2_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 46),
    _RmRingAllowedHoursPartition2_Type()
)
rmRingAllowedHoursPartition2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmRingAllowedHoursPartition2.setStatus("mandatory")
_RmServerPowerOn_Type = Integer32
_RmServerPowerOn_Object = MibScalar
rmServerPowerOn = _RmServerPowerOn_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 47),
    _RmServerPowerOn_Type()
)
rmServerPowerOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmServerPowerOn.setStatus("mandatory")


class _RmTRLastErrorClass_Type(Integer32):
    """Custom type rmTRLastErrorClass based on Integer32"""
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
        *(("adapter-error", 1),
          ("beaconing", 2),
          ("iso-increasing", 3),
          ("iso-excessive", 4),
          ("iso-decay", 5),
          ("congestion", 6))
    )


_RmTRLastErrorClass_Type.__name__ = "Integer32"
_RmTRLastErrorClass_Object = MibScalar
rmTRLastErrorClass = _RmTRLastErrorClass_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 48),
    _RmTRLastErrorClass_Type()
)
rmTRLastErrorClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmTRLastErrorClass.setStatus("mandatory")
_RmTRLastErrorType_Type = Integer32
_RmTRLastErrorType_Object = MibScalar
rmTRLastErrorType = _RmTRLastErrorType_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 49),
    _RmTRLastErrorType_Type()
)
rmTRLastErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmTRLastErrorType.setStatus("mandatory")
_RmTRFaultDomainNode1_Type = PhysAddress
_RmTRFaultDomainNode1_Object = MibScalar
rmTRFaultDomainNode1 = _RmTRFaultDomainNode1_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 50),
    _RmTRFaultDomainNode1_Type()
)
rmTRFaultDomainNode1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmTRFaultDomainNode1.setStatus("mandatory")
_RmTRFaultDomainNode2_Type = PhysAddress
_RmTRFaultDomainNode2_Object = MibScalar
rmTRFaultDomainNode2 = _RmTRFaultDomainNode2_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 51),
    _RmTRFaultDomainNode2_Type()
)
rmTRFaultDomainNode2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmTRFaultDomainNode2.setStatus("mandatory")
_RmIsoTresholdExceededCount_Type = Counter32
_RmIsoTresholdExceededCount_Object = MibScalar
rmIsoTresholdExceededCount = _RmIsoTresholdExceededCount_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 52),
    _RmIsoTresholdExceededCount_Type()
)
rmIsoTresholdExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmIsoTresholdExceededCount.setStatus("mandatory")
_RmNonIsoTresholdExceededCount_Type = Counter32
_RmNonIsoTresholdExceededCount_Object = MibScalar
rmNonIsoTresholdExceededCount = _RmNonIsoTresholdExceededCount_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 53),
    _RmNonIsoTresholdExceededCount_Type()
)
rmNonIsoTresholdExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmNonIsoTresholdExceededCount.setStatus("mandatory")
_RmCongestionTresholdExceededCount_Type = Counter32
_RmCongestionTresholdExceededCount_Object = MibScalar
rmCongestionTresholdExceededCount = _RmCongestionTresholdExceededCount_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 54),
    _RmCongestionTresholdExceededCount_Type()
)
rmCongestionTresholdExceededCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmCongestionTresholdExceededCount.setStatus("mandatory")
_RmBeaconCounter_Type = Counter32
_RmBeaconCounter_Object = MibScalar
rmBeaconCounter = _RmBeaconCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 55),
    _RmBeaconCounter_Type()
)
rmBeaconCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBeaconCounter.setStatus("mandatory")
_RmSpareCounter_Type = Counter32
_RmSpareCounter_Object = MibScalar
rmSpareCounter = _RmSpareCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 56),
    _RmSpareCounter_Type()
)
rmSpareCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmSpareCounter.setStatus("mandatory")
_RmPurgeCounter_Type = Counter32
_RmPurgeCounter_Object = MibScalar
rmPurgeCounter = _RmPurgeCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 57),
    _RmPurgeCounter_Type()
)
rmPurgeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmPurgeCounter.setStatus("mandatory")
_RmClaimCounter_Type = Counter32
_RmClaimCounter_Object = MibScalar
rmClaimCounter = _RmClaimCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 58),
    _RmClaimCounter_Type()
)
rmClaimCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmClaimCounter.setStatus("mandatory")
_RmAdapterResetCounter_Type = Counter32
_RmAdapterResetCounter_Object = MibScalar
rmAdapterResetCounter = _RmAdapterResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 59),
    _RmAdapterResetCounter_Type()
)
rmAdapterResetCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmAdapterResetCounter.setStatus("mandatory")
_RmLostFramesCounter_Type = Counter32
_RmLostFramesCounter_Object = MibScalar
rmLostFramesCounter = _RmLostFramesCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 60),
    _RmLostFramesCounter_Type()
)
rmLostFramesCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmLostFramesCounter.setStatus("mandatory")
_RmCongestionCounter_Type = Counter32
_RmCongestionCounter_Object = MibScalar
rmCongestionCounter = _RmCongestionCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 61),
    _RmCongestionCounter_Type()
)
rmCongestionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmCongestionCounter.setStatus("mandatory")
_RmFrameCopyCounter_Type = Counter32
_RmFrameCopyCounter_Object = MibScalar
rmFrameCopyCounter = _RmFrameCopyCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 62),
    _RmFrameCopyCounter_Type()
)
rmFrameCopyCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmFrameCopyCounter.setStatus("mandatory")
_RmFrequencyErrorCounter_Type = Counter32
_RmFrequencyErrorCounter_Object = MibScalar
rmFrequencyErrorCounter = _RmFrequencyErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 63),
    _RmFrequencyErrorCounter_Type()
)
rmFrequencyErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmFrequencyErrorCounter.setStatus("mandatory")
_RmTokenCounter_Type = Counter32
_RmTokenCounter_Object = MibScalar
rmTokenCounter = _RmTokenCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 64),
    _RmTokenCounter_Type()
)
rmTokenCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmTokenCounter.setStatus("mandatory")
_RmLineCounter_Type = Counter32
_RmLineCounter_Object = MibScalar
rmLineCounter = _RmLineCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 65),
    _RmLineCounter_Type()
)
rmLineCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmLineCounter.setStatus("mandatory")
_RmInternalCounter_Type = Counter32
_RmInternalCounter_Object = MibScalar
rmInternalCounter = _RmInternalCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 66),
    _RmInternalCounter_Type()
)
rmInternalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmInternalCounter.setStatus("mandatory")
_RmBurstCounter_Type = Counter32
_RmBurstCounter_Object = MibScalar
rmBurstCounter = _RmBurstCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 67),
    _RmBurstCounter_Type()
)
rmBurstCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmBurstCounter.setStatus("mandatory")
_RmARIFCICounter_Type = Counter32
_RmARIFCICounter_Object = MibScalar
rmARIFCICounter = _RmARIFCICounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 68),
    _RmARIFCICounter_Type()
)
rmARIFCICounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmARIFCICounter.setStatus("mandatory")
_RmAbortCounter_Type = Counter32
_RmAbortCounter_Object = MibScalar
rmAbortCounter = _RmAbortCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 69),
    _RmAbortCounter_Type()
)
rmAbortCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmAbortCounter.setStatus("mandatory")
_RmPollFailCounter_Type = Counter32
_RmPollFailCounter_Object = MibScalar
rmPollFailCounter = _RmPollFailCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 70),
    _RmPollFailCounter_Type()
)
rmPollFailCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmPollFailCounter.setStatus("mandatory")
_RmNoResponseCounter_Type = Counter32
_RmNoResponseCounter_Object = MibScalar
rmNoResponseCounter = _RmNoResponseCounter_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 71),
    _RmNoResponseCounter_Type()
)
rmNoResponseCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmNoResponseCounter.setStatus("mandatory")
_RmWholeRingCounters_Type = OctetString
_RmWholeRingCounters_Object = MibScalar
rmWholeRingCounters = _RmWholeRingCounters_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 72),
    _RmWholeRingCounters_Type()
)
rmWholeRingCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmWholeRingCounters.setStatus("mandatory")
_RmResetOldDevicesSetup_Type = Integer32
_RmResetOldDevicesSetup_Object = MibScalar
rmResetOldDevicesSetup = _RmResetOldDevicesSetup_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 73),
    _RmResetOldDevicesSetup_Type()
)
rmResetOldDevicesSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmResetOldDevicesSetup.setStatus("mandatory")
_RmResetErrorCounters_Type = Integer32
_RmResetErrorCounters_Object = MibScalar
rmResetErrorCounters = _RmResetErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 74),
    _RmResetErrorCounters_Type()
)
rmResetErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmResetErrorCounters.setStatus("mandatory")
_RmSetCurrentTime_Type = Integer32
_RmSetCurrentTime_Object = MibScalar
rmSetCurrentTime = _RmSetCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 75),
    _RmSetCurrentTime_Type()
)
rmSetCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmSetCurrentTime.setStatus("mandatory")
_RmRingFirstSplitConfiguration_Type = RING_CONFIGURATION
_RmRingFirstSplitConfiguration_Object = MibScalar
rmRingFirstSplitConfiguration = _RmRingFirstSplitConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 76),
    _RmRingFirstSplitConfiguration_Type()
)
rmRingFirstSplitConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingFirstSplitConfiguration.setStatus("mandatory")
_RmRingNextSplitConfiguration_Type = RING_CONFIGURATION
_RmRingNextSplitConfiguration_Object = MibScalar
rmRingNextSplitConfiguration = _RmRingNextSplitConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 224, 5, 77),
    _RmRingNextSplitConfiguration_Type()
)
rmRingNextSplitConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmRingNextSplitConfiguration.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANOPTICS-RING-MANAGER-MIB",
    **{"BITMAP": BITMAP,
       "RING-CONFIGURATION": RING_CONFIGURATION,
       "lanOptics": lanOptics,
       "lanOpticsDot5Monitor": lanOpticsDot5Monitor,
       "rmServerReportingTo": rmServerReportingTo,
       "rmRingStatus": rmRingStatus,
       "rmServerHealthText": rmServerHealthText,
       "rmServerHealth": rmServerHealth,
       "rmRingEventInLog": rmRingEventInLog,
       "rmRingEventTable": rmRingEventTable,
       "rmRingEventEntry": rmRingEventEntry,
       "rmRingEvent": rmRingEvent,
       "pysmiFakeCol26": pysmiFakeCol26,
       "pysmiFakeCol25": pysmiFakeCol25,
       "pysmiFakeCol24": pysmiFakeCol24,
       "pysmiFakeCol23": pysmiFakeCol23,
       "rmRingBeaconingStatus": rmRingBeaconingStatus,
       "rmRingIsoErrorStatus": rmRingIsoErrorStatus,
       "rmRingSingleStationStatus": rmRingSingleStationStatus,
       "rmRingFullConfiguration": rmRingFullConfiguration,
       "rmRingConfigurationUpdate": rmRingConfigurationUpdate,
       "rmServerInitProcess": rmServerInitProcess,
       "rmServerAdminState": rmServerAdminState,
       "rmServerOperatingState": rmServerOperatingState,
       "rmServerAdminParameters": rmServerAdminParameters,
       "rmServerOperatingParameters": rmServerOperatingParameters,
       "rmDeviceStatusTable": rmDeviceStatusTable,
       "rmDeviceEntry": rmDeviceEntry,
       "rmDeviceMacAddress": rmDeviceMacAddress,
       "rmDeviceUpstream": rmDeviceUpstream,
       "rmDeviceAdminState": rmDeviceAdminState,
       "rmDeviceOperateState": rmDeviceOperateState,
       "rmDevicePhysLocation": rmDevicePhysLocation,
       "rmDeviceGroupAddress": rmDeviceGroupAddress,
       "rmDeviceFunctionAddress": rmDeviceFunctionAddress,
       "rmDeviceProductID": rmDeviceProductID,
       "rmDeviceStationID": rmDeviceStationID,
       "rmDeviceStationStatus": rmDeviceStationStatus,
       "rmDeviceFunctionClass": rmDeviceFunctionClass,
       "rmDeviceAccessPriority": rmDeviceAccessPriority,
       "rmDeviceMicroLevel": rmDeviceMicroLevel,
       "rmDeviceMonitored": rmDeviceMonitored,
       "rmDeviceDaysAllowed": rmDeviceDaysAllowed,
       "rmDeviceHoursAllowed": rmDeviceHoursAllowed,
       "rmRingPollProcessStatus": rmRingPollProcessStatus,
       "rmRingNumber": rmRingNumber,
       "rmRingSoftErrorTimer": rmRingSoftErrorTimer,
       "rmRingIsolatingTab": rmRingIsolatingTab,
       "rmRingCongestTab": rmRingCongestTab,
       "rmRingNonIsolatingTab": rmRingNonIsolatingTab,
       "rmRingAutoRemove": rmRingAutoRemove,
       "rmRingAllowedDaysPartition1": rmRingAllowedDaysPartition1,
       "rmRingAllowedDaysPartition2": rmRingAllowedDaysPartition2,
       "rmRingAllowedHoursPartition1": rmRingAllowedHoursPartition1,
       "rmRingAllowedHoursPartition2": rmRingAllowedHoursPartition2,
       "rmServerPowerOn": rmServerPowerOn,
       "rmTRLastErrorClass": rmTRLastErrorClass,
       "rmTRLastErrorType": rmTRLastErrorType,
       "rmTRFaultDomainNode1": rmTRFaultDomainNode1,
       "rmTRFaultDomainNode2": rmTRFaultDomainNode2,
       "rmIsoTresholdExceededCount": rmIsoTresholdExceededCount,
       "rmNonIsoTresholdExceededCount": rmNonIsoTresholdExceededCount,
       "rmCongestionTresholdExceededCount": rmCongestionTresholdExceededCount,
       "rmBeaconCounter": rmBeaconCounter,
       "rmSpareCounter": rmSpareCounter,
       "rmPurgeCounter": rmPurgeCounter,
       "rmClaimCounter": rmClaimCounter,
       "rmAdapterResetCounter": rmAdapterResetCounter,
       "rmLostFramesCounter": rmLostFramesCounter,
       "rmCongestionCounter": rmCongestionCounter,
       "rmFrameCopyCounter": rmFrameCopyCounter,
       "rmFrequencyErrorCounter": rmFrequencyErrorCounter,
       "rmTokenCounter": rmTokenCounter,
       "rmLineCounter": rmLineCounter,
       "rmInternalCounter": rmInternalCounter,
       "rmBurstCounter": rmBurstCounter,
       "rmARIFCICounter": rmARIFCICounter,
       "rmAbortCounter": rmAbortCounter,
       "rmPollFailCounter": rmPollFailCounter,
       "rmNoResponseCounter": rmNoResponseCounter,
       "rmWholeRingCounters": rmWholeRingCounters,
       "rmResetOldDevicesSetup": rmResetOldDevicesSetup,
       "rmResetErrorCounters": rmResetErrorCounters,
       "rmSetCurrentTime": rmSetCurrentTime,
       "rmRingFirstSplitConfiguration": rmRingFirstSplitConfiguration,
       "rmRingNextSplitConfiguration": rmRingNextSplitConfiguration}
)
