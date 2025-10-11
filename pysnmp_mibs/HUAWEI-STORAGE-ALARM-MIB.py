# SNMP MIB module (HUAWEI-STORAGE-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-STORAGE-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:23:43 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

storage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20)
)
_HwStorageNotification_ObjectIdentity = ObjectIdentity
hwStorageNotification = _HwStorageNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1)
)
_HwStorageActiveAlarmInfo_ObjectIdentity = ObjectIdentity
hwStorageActiveAlarmInfo = _HwStorageActiveAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1)
)
_HwStorageActiveAlarmInfoTable_Object = MibTable
hwStorageActiveAlarmInfoTable = _HwStorageActiveAlarmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoTable.setStatus("current")
_HwStorageActiveAlarmInfoEntry_Object = MibTableRow
hwStorageActiveAlarmInfoEntry = _HwStorageActiveAlarmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1)
)
hwStorageActiveAlarmInfoEntry.setIndexNames(
    (0, "HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoNodeCode"),
    (0, "HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoSerialNo"),
)
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoEntry.setStatus("current")
_HwStorageActiveAlarmInfoNodeCode_Type = OctetString
_HwStorageActiveAlarmInfoNodeCode_Object = MibTableColumn
hwStorageActiveAlarmInfoNodeCode = _HwStorageActiveAlarmInfoNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 1),
    _HwStorageActiveAlarmInfoNodeCode_Type()
)
hwStorageActiveAlarmInfoNodeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoNodeCode.setStatus("current")
_HwStorageActiveAlarmInfoLocationInfo_Type = DisplayString
_HwStorageActiveAlarmInfoLocationInfo_Object = MibTableColumn
hwStorageActiveAlarmInfoLocationInfo = _HwStorageActiveAlarmInfoLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 2),
    _HwStorageActiveAlarmInfoLocationInfo_Type()
)
hwStorageActiveAlarmInfoLocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoLocationInfo.setStatus("current")
_HwStorageActiveAlarmInfoRestoreAdvice_Type = DisplayString
_HwStorageActiveAlarmInfoRestoreAdvice_Object = MibTableColumn
hwStorageActiveAlarmInfoRestoreAdvice = _HwStorageActiveAlarmInfoRestoreAdvice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 3),
    _HwStorageActiveAlarmInfoRestoreAdvice_Type()
)
hwStorageActiveAlarmInfoRestoreAdvice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoRestoreAdvice.setStatus("current")
_HwStorageActiveAlarmInfoTitle_Type = DisplayString
_HwStorageActiveAlarmInfoTitle_Object = MibTableColumn
hwStorageActiveAlarmInfoTitle = _HwStorageActiveAlarmInfoTitle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 4),
    _HwStorageActiveAlarmInfoTitle_Type()
)
hwStorageActiveAlarmInfoTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoTitle.setStatus("current")


class _HwStorageActiveAlarmInfoType_Type(Integer32):
    """Custom type hwStorageActiveAlarmInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("equipmentFault", 2)
    )


_HwStorageActiveAlarmInfoType_Type.__name__ = "Integer32"
_HwStorageActiveAlarmInfoType_Object = MibTableColumn
hwStorageActiveAlarmInfoType = _HwStorageActiveAlarmInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 5),
    _HwStorageActiveAlarmInfoType_Type()
)
hwStorageActiveAlarmInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoType.setStatus("current")


class _HwStorageActiveAlarmInfoLevel_Type(Integer32):
    """Custom type hwStorageActiveAlarmInfoLevel based on Integer32"""
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
        *(("criticalAlarm", 1),
          ("majorAlarm", 2),
          ("minorAlarm", 3),
          ("warningAlarm", 4))
    )


_HwStorageActiveAlarmInfoLevel_Type.__name__ = "Integer32"
_HwStorageActiveAlarmInfoLevel_Object = MibTableColumn
hwStorageActiveAlarmInfoLevel = _HwStorageActiveAlarmInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 6),
    _HwStorageActiveAlarmInfoLevel_Type()
)
hwStorageActiveAlarmInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoLevel.setStatus("current")
_HwStorageActiveAlarmInfoAlarmID_Type = Gauge32
_HwStorageActiveAlarmInfoAlarmID_Object = MibTableColumn
hwStorageActiveAlarmInfoAlarmID = _HwStorageActiveAlarmInfoAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 7),
    _HwStorageActiveAlarmInfoAlarmID_Type()
)
hwStorageActiveAlarmInfoAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoAlarmID.setStatus("current")
_HwStorageActiveAlarmInfoOccurTime_Type = OctetString
_HwStorageActiveAlarmInfoOccurTime_Object = MibTableColumn
hwStorageActiveAlarmInfoOccurTime = _HwStorageActiveAlarmInfoOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 8),
    _HwStorageActiveAlarmInfoOccurTime_Type()
)
hwStorageActiveAlarmInfoOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoOccurTime.setStatus("current")
_HwStorageActiveAlarmInfoSerialNo_Type = Gauge32
_HwStorageActiveAlarmInfoSerialNo_Object = MibTableColumn
hwStorageActiveAlarmInfoSerialNo = _HwStorageActiveAlarmInfoSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 9),
    _HwStorageActiveAlarmInfoSerialNo_Type()
)
hwStorageActiveAlarmInfoSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoSerialNo.setStatus("current")
_HwStorageActiveAlarmInfoAddtionInfo_Type = OctetString
_HwStorageActiveAlarmInfoAddtionInfo_Object = MibTableColumn
hwStorageActiveAlarmInfoAddtionInfo = _HwStorageActiveAlarmInfoAddtionInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 10),
    _HwStorageActiveAlarmInfoAddtionInfo_Type()
)
hwStorageActiveAlarmInfoAddtionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoAddtionInfo.setStatus("current")


class _HwStorageActiveAlarmInfoCategory_Type(Integer32):
    """Custom type hwStorageActiveAlarmInfoCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultAlarm", 1),
          ("resumeAlarm", 2),
          ("eventAlarm", 3))
    )


_HwStorageActiveAlarmInfoCategory_Type.__name__ = "Integer32"
_HwStorageActiveAlarmInfoCategory_Object = MibTableColumn
hwStorageActiveAlarmInfoCategory = _HwStorageActiveAlarmInfoCategory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 11),
    _HwStorageActiveAlarmInfoCategory_Type()
)
hwStorageActiveAlarmInfoCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoCategory.setStatus("current")
_HwStorageActiveAlarmInfoLocalAlarmID_Type = Counter64
_HwStorageActiveAlarmInfoLocalAlarmID_Object = MibTableColumn
hwStorageActiveAlarmInfoLocalAlarmID = _HwStorageActiveAlarmInfoLocalAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 1, 1, 1, 12),
    _HwStorageActiveAlarmInfoLocalAlarmID_Type()
)
hwStorageActiveAlarmInfoLocalAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStorageActiveAlarmInfoLocalAlarmID.setStatus("current")
_HwStorageNotificationType_ObjectIdentity = ObjectIdentity
hwStorageNotificationType = _HwStorageNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 2)
)
_HwStorageReportingAlarm_ObjectIdentity = ObjectIdentity
hwStorageReportingAlarm = _HwStorageReportingAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3)
)
_HwStorageReportingAlarmNodeCode_Type = OctetString
_HwStorageReportingAlarmNodeCode_Object = MibScalar
hwStorageReportingAlarmNodeCode = _HwStorageReportingAlarmNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 1),
    _HwStorageReportingAlarmNodeCode_Type()
)
hwStorageReportingAlarmNodeCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmNodeCode.setStatus("current")
_HwStorageReportingAlarmLocationInfo_Type = DisplayString
_HwStorageReportingAlarmLocationInfo_Object = MibScalar
hwStorageReportingAlarmLocationInfo = _HwStorageReportingAlarmLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 2),
    _HwStorageReportingAlarmLocationInfo_Type()
)
hwStorageReportingAlarmLocationInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmLocationInfo.setStatus("current")


class _HwStorageReportingAlarmRestoreAdvice_Type(OctetString):
    """Custom type hwStorageReportingAlarmRestoreAdvice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwStorageReportingAlarmRestoreAdvice_Type.__name__ = "OctetString"
_HwStorageReportingAlarmRestoreAdvice_Object = MibScalar
hwStorageReportingAlarmRestoreAdvice = _HwStorageReportingAlarmRestoreAdvice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 3),
    _HwStorageReportingAlarmRestoreAdvice_Type()
)
hwStorageReportingAlarmRestoreAdvice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmRestoreAdvice.setStatus("current")


class _HwStorageReportingAlarmFaultTitle_Type(OctetString):
    """Custom type hwStorageReportingAlarmFaultTitle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwStorageReportingAlarmFaultTitle_Type.__name__ = "OctetString"
_HwStorageReportingAlarmFaultTitle_Object = MibScalar
hwStorageReportingAlarmFaultTitle = _HwStorageReportingAlarmFaultTitle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 4),
    _HwStorageReportingAlarmFaultTitle_Type()
)
hwStorageReportingAlarmFaultTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmFaultTitle.setStatus("current")


class _HwStorageReportingAlarmFaultType_Type(Integer32):
    """Custom type hwStorageReportingAlarmFaultType based on Integer32"""
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
        *(("communicationQuality", 1),
          ("equipmentFault", 2),
          ("processError", 3),
          ("serviceQuality", 4),
          ("environmentFault", 5),
          ("performanceLimit", 6))
    )


_HwStorageReportingAlarmFaultType_Type.__name__ = "Integer32"
_HwStorageReportingAlarmFaultType_Object = MibScalar
hwStorageReportingAlarmFaultType = _HwStorageReportingAlarmFaultType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 5),
    _HwStorageReportingAlarmFaultType_Type()
)
hwStorageReportingAlarmFaultType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmFaultType.setStatus("current")


class _HwStorageReportingAlarmFaultLevel_Type(Integer32):
    """Custom type hwStorageReportingAlarmFaultLevel based on Integer32"""
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
        *(("criticalAlarm", 1),
          ("majorAlarm", 2),
          ("minorAlarm", 3),
          ("warningAlarm", 4))
    )


_HwStorageReportingAlarmFaultLevel_Type.__name__ = "Integer32"
_HwStorageReportingAlarmFaultLevel_Object = MibScalar
hwStorageReportingAlarmFaultLevel = _HwStorageReportingAlarmFaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 6),
    _HwStorageReportingAlarmFaultLevel_Type()
)
hwStorageReportingAlarmFaultLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmFaultLevel.setStatus("current")
_HwStorageReportingAlarmAlarmID_Type = Gauge32
_HwStorageReportingAlarmAlarmID_Object = MibScalar
hwStorageReportingAlarmAlarmID = _HwStorageReportingAlarmAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 7),
    _HwStorageReportingAlarmAlarmID_Type()
)
hwStorageReportingAlarmAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmAlarmID.setStatus("current")
_HwStorageReportingAlarmFaultTime_Type = OctetString
_HwStorageReportingAlarmFaultTime_Object = MibScalar
hwStorageReportingAlarmFaultTime = _HwStorageReportingAlarmFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 8),
    _HwStorageReportingAlarmFaultTime_Type()
)
hwStorageReportingAlarmFaultTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmFaultTime.setStatus("current")
_HwStorageReportingAlarmSerialNo_Type = Gauge32
_HwStorageReportingAlarmSerialNo_Object = MibScalar
hwStorageReportingAlarmSerialNo = _HwStorageReportingAlarmSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 9),
    _HwStorageReportingAlarmSerialNo_Type()
)
hwStorageReportingAlarmSerialNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmSerialNo.setStatus("current")
_HwStorageReportingAlarmAdditionInfo_Type = DisplayString
_HwStorageReportingAlarmAdditionInfo_Object = MibScalar
hwStorageReportingAlarmAdditionInfo = _HwStorageReportingAlarmAdditionInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 10),
    _HwStorageReportingAlarmAdditionInfo_Type()
)
hwStorageReportingAlarmAdditionInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmAdditionInfo.setStatus("current")


class _HwStorageReportingAlarmFaultCategory_Type(Integer32):
    """Custom type hwStorageReportingAlarmFaultCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultAlarm", 1),
          ("resumeAlarm", 2),
          ("eventAlarm", 3))
    )


_HwStorageReportingAlarmFaultCategory_Type.__name__ = "Integer32"
_HwStorageReportingAlarmFaultCategory_Object = MibScalar
hwStorageReportingAlarmFaultCategory = _HwStorageReportingAlarmFaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 11),
    _HwStorageReportingAlarmFaultCategory_Type()
)
hwStorageReportingAlarmFaultCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmFaultCategory.setStatus("current")
_HwStorageReportingAlarmLocationAlarmID_Type = Counter64
_HwStorageReportingAlarmLocationAlarmID_Object = MibScalar
hwStorageReportingAlarmLocationAlarmID = _HwStorageReportingAlarmLocationAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 12),
    _HwStorageReportingAlarmLocationAlarmID_Type()
)
hwStorageReportingAlarmLocationAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmLocationAlarmID.setStatus("current")
_HwStorageReportingAlarmProductModel_Type = Integer32
_HwStorageReportingAlarmProductModel_Object = MibScalar
hwStorageReportingAlarmProductModel = _HwStorageReportingAlarmProductModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 13),
    _HwStorageReportingAlarmProductModel_Type()
)
hwStorageReportingAlarmProductModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmProductModel.setStatus("current")
_HwStorageReportingAlarmProductSN_Type = OctetString
_HwStorageReportingAlarmProductSN_Object = MibScalar
hwStorageReportingAlarmProductSN = _HwStorageReportingAlarmProductSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 3, 14),
    _HwStorageReportingAlarmProductSN_Type()
)
hwStorageReportingAlarmProductSN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageReportingAlarmProductSN.setStatus("current")
_HwStorageEvent_ObjectIdentity = ObjectIdentity
hwStorageEvent = _HwStorageEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2)
)
_NotificationType_ObjectIdentity = ObjectIdentity
notificationType = _NotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 1)
)
_TrapEvent_ObjectIdentity = ObjectIdentity
trapEvent = _TrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2)
)
_HwStorageTrapEventType_Type = Unsigned32
_HwStorageTrapEventType_Object = MibScalar
hwStorageTrapEventType = _HwStorageTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 1),
    _HwStorageTrapEventType_Type()
)
hwStorageTrapEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventType.setStatus("current")
_HwStorageTrapEventID_Type = Counter64
_HwStorageTrapEventID_Object = MibScalar
hwStorageTrapEventID = _HwStorageTrapEventID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 2),
    _HwStorageTrapEventID_Type()
)
hwStorageTrapEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventID.setStatus("current")
_HwStorageTrapEventLevel_Type = Unsigned32
_HwStorageTrapEventLevel_Object = MibScalar
hwStorageTrapEventLevel = _HwStorageTrapEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 3),
    _HwStorageTrapEventLevel_Type()
)
hwStorageTrapEventLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventLevel.setStatus("current")
_HwStorageTrapEventSequence_Type = Unsigned32
_HwStorageTrapEventSequence_Object = MibScalar
hwStorageTrapEventSequence = _HwStorageTrapEventSequence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 4),
    _HwStorageTrapEventSequence_Type()
)
hwStorageTrapEventSequence.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventSequence.setStatus("current")
_HwStorageTrapEventTime_Type = Unsigned32
_HwStorageTrapEventTime_Object = MibScalar
hwStorageTrapEventTime = _HwStorageTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 5),
    _HwStorageTrapEventTime_Type()
)
hwStorageTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventTime.setStatus("current")
_HwStorageTrapEventRecoveryTime_Type = Unsigned32
_HwStorageTrapEventRecoveryTime_Object = MibScalar
hwStorageTrapEventRecoveryTime = _HwStorageTrapEventRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 6),
    _HwStorageTrapEventRecoveryTime_Type()
)
hwStorageTrapEventRecoveryTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventRecoveryTime.setStatus("current")
_HwStorageTrapEventParameter_Type = OctetString
_HwStorageTrapEventParameter_Object = MibScalar
hwStorageTrapEventParameter = _HwStorageTrapEventParameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 7),
    _HwStorageTrapEventParameter_Type()
)
hwStorageTrapEventParameter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventParameter.setStatus("current")
_HwStorageTrapEventID32Bit_Type = Unsigned32
_HwStorageTrapEventID32Bit_Object = MibScalar
hwStorageTrapEventID32Bit = _HwStorageTrapEventID32Bit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 8),
    _HwStorageTrapEventID32Bit_Type()
)
hwStorageTrapEventID32Bit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventID32Bit.setStatus("current")
_HwStorageTrapEventTimeStr_Type = OctetString
_HwStorageTrapEventTimeStr_Object = MibScalar
hwStorageTrapEventTimeStr = _HwStorageTrapEventTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 9),
    _HwStorageTrapEventTimeStr_Type()
)
hwStorageTrapEventTimeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventTimeStr.setStatus("current")
_HwStorageTrapEventRecoveryTimeStr_Type = OctetString
_HwStorageTrapEventRecoveryTimeStr_Object = MibScalar
hwStorageTrapEventRecoveryTimeStr = _HwStorageTrapEventRecoveryTimeStr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 2, 10),
    _HwStorageTrapEventRecoveryTimeStr_Type()
)
hwStorageTrapEventRecoveryTimeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageTrapEventRecoveryTimeStr.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoNodeCode"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoLocationInfo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoRestoreAdvice"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoTitle"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoType"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoLevel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoAlarmID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoOccurTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoSerialNo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoAddtionInfo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoCategory"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageActiveAlarmInfoLocalAlarmID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmNodeCode"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmLocationInfo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmRestoreAdvice"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultTitle"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultType"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultLevel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmAlarmID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmSerialNo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmAdditionInfo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultCategory"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmLocationAlarmID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmProductModel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmProductSN"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventType"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventLevel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventSequence"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventRecoveryTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventParameter"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventID32Bit"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventTimeStr"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventRecoveryTimeStr"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects

hwStorageAlarmReporting = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 1, 2, 1)
)
hwStorageAlarmReporting.setObjects(
      *(("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmNodeCode"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmLocationInfo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmRestoreAdvice"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultTitle"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultType"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultLevel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmAlarmID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmSerialNo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmAdditionInfo"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmFaultCategory"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmLocationAlarmID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmProductModel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageReportingAlarmProductSN"))
)
if mibBuilder.loadTexts:
    hwStorageAlarmReporting.setStatus(
        "current"
    )

hwStorageEventType = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 20, 2, 1, 1)
)
hwStorageEventType.setObjects(
      *(("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventType"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventID"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventLevel"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventSequence"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventRecoveryTime"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventParameter"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventID32Bit"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventTimeStr"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageTrapEventRecoveryTimeStr"))
)
if mibBuilder.loadTexts:
    hwStorageEventType.setStatus(
        "current"
    )


# Notifications groups

currentNotificationGroup = NotificationGroup(
    (1, 6, 1, 2)
)
currentNotificationGroup.setObjects(
      *(("HUAWEI-STORAGE-ALARM-MIB", "hwStorageAlarmReporting"),
        ("HUAWEI-STORAGE-ALARM-MIB", "hwStorageEventType"))
)
if mibBuilder.loadTexts:
    currentNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
      *(("HUAWEI-STORAGE-ALARM-MIB", "currentObjectGroup"),
        ("HUAWEI-STORAGE-ALARM-MIB", "currentNotificationGroup"))
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-STORAGE-ALARM-MIB",
    **{"huawei": huawei,
       "products": products,
       "storage": storage,
       "alarm": alarm,
       "hwStorageNotification": hwStorageNotification,
       "hwStorageActiveAlarmInfo": hwStorageActiveAlarmInfo,
       "hwStorageActiveAlarmInfoTable": hwStorageActiveAlarmInfoTable,
       "hwStorageActiveAlarmInfoEntry": hwStorageActiveAlarmInfoEntry,
       "hwStorageActiveAlarmInfoNodeCode": hwStorageActiveAlarmInfoNodeCode,
       "hwStorageActiveAlarmInfoLocationInfo": hwStorageActiveAlarmInfoLocationInfo,
       "hwStorageActiveAlarmInfoRestoreAdvice": hwStorageActiveAlarmInfoRestoreAdvice,
       "hwStorageActiveAlarmInfoTitle": hwStorageActiveAlarmInfoTitle,
       "hwStorageActiveAlarmInfoType": hwStorageActiveAlarmInfoType,
       "hwStorageActiveAlarmInfoLevel": hwStorageActiveAlarmInfoLevel,
       "hwStorageActiveAlarmInfoAlarmID": hwStorageActiveAlarmInfoAlarmID,
       "hwStorageActiveAlarmInfoOccurTime": hwStorageActiveAlarmInfoOccurTime,
       "hwStorageActiveAlarmInfoSerialNo": hwStorageActiveAlarmInfoSerialNo,
       "hwStorageActiveAlarmInfoAddtionInfo": hwStorageActiveAlarmInfoAddtionInfo,
       "hwStorageActiveAlarmInfoCategory": hwStorageActiveAlarmInfoCategory,
       "hwStorageActiveAlarmInfoLocalAlarmID": hwStorageActiveAlarmInfoLocalAlarmID,
       "hwStorageNotificationType": hwStorageNotificationType,
       "hwStorageAlarmReporting": hwStorageAlarmReporting,
       "hwStorageReportingAlarm": hwStorageReportingAlarm,
       "hwStorageReportingAlarmNodeCode": hwStorageReportingAlarmNodeCode,
       "hwStorageReportingAlarmLocationInfo": hwStorageReportingAlarmLocationInfo,
       "hwStorageReportingAlarmRestoreAdvice": hwStorageReportingAlarmRestoreAdvice,
       "hwStorageReportingAlarmFaultTitle": hwStorageReportingAlarmFaultTitle,
       "hwStorageReportingAlarmFaultType": hwStorageReportingAlarmFaultType,
       "hwStorageReportingAlarmFaultLevel": hwStorageReportingAlarmFaultLevel,
       "hwStorageReportingAlarmAlarmID": hwStorageReportingAlarmAlarmID,
       "hwStorageReportingAlarmFaultTime": hwStorageReportingAlarmFaultTime,
       "hwStorageReportingAlarmSerialNo": hwStorageReportingAlarmSerialNo,
       "hwStorageReportingAlarmAdditionInfo": hwStorageReportingAlarmAdditionInfo,
       "hwStorageReportingAlarmFaultCategory": hwStorageReportingAlarmFaultCategory,
       "hwStorageReportingAlarmLocationAlarmID": hwStorageReportingAlarmLocationAlarmID,
       "hwStorageReportingAlarmProductModel": hwStorageReportingAlarmProductModel,
       "hwStorageReportingAlarmProductSN": hwStorageReportingAlarmProductSN,
       "hwStorageEvent": hwStorageEvent,
       "notificationType": notificationType,
       "hwStorageEventType": hwStorageEventType,
       "trapEvent": trapEvent,
       "hwStorageTrapEventType": hwStorageTrapEventType,
       "hwStorageTrapEventID": hwStorageTrapEventID,
       "hwStorageTrapEventLevel": hwStorageTrapEventLevel,
       "hwStorageTrapEventSequence": hwStorageTrapEventSequence,
       "hwStorageTrapEventTime": hwStorageTrapEventTime,
       "hwStorageTrapEventRecoveryTime": hwStorageTrapEventRecoveryTime,
       "hwStorageTrapEventParameter": hwStorageTrapEventParameter,
       "hwStorageTrapEventID32Bit": hwStorageTrapEventID32Bit,
       "hwStorageTrapEventTimeStr": hwStorageTrapEventTimeStr,
       "hwStorageTrapEventRecoveryTimeStr": hwStorageTrapEventRecoveryTimeStr,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
