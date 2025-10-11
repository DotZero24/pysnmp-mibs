# SNMP MIB module (ISM-HUAWEI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/ISM-HUAWEI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:28:47 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwISMCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91)
)
if mibBuilder.loadTexts:
    hwISMCommon.setRevisions(
        ("2008-09-17 16:29",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NodeCodeString(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(15, 17),
    )



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_HwIsmTopo_ObjectIdentity = ObjectIdentity
hwIsmTopo = _HwIsmTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9)
)
_HwIsmAccessNodeInfo_ObjectIdentity = ObjectIdentity
hwIsmAccessNodeInfo = _HwIsmAccessNodeInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1)
)
_HwIsmAccessNodeTable_Object = MibTable
hwIsmAccessNodeTable = _HwIsmAccessNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsmAccessNodeTable.setStatus("current")
_HwIsmAccessNodeEntry_Object = MibTableRow
hwIsmAccessNodeEntry = _HwIsmAccessNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1)
)
hwIsmAccessNodeEntry.setIndexNames(
    (0, "ISM-HUAWEI-MIB", "hwIsmNENodeCode"),
)
if mibBuilder.loadTexts:
    hwIsmAccessNodeEntry.setStatus("current")
_HwIsmNENodeCode_Type = NodeCodeString
_HwIsmNENodeCode_Object = MibTableColumn
hwIsmNENodeCode = _HwIsmNENodeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 1),
    _HwIsmNENodeCode_Type()
)
hwIsmNENodeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeCode.setStatus("current")
_HwIsmNENodeType_Type = Integer32
_HwIsmNENodeType_Object = MibTableColumn
hwIsmNENodeType = _HwIsmNENodeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 2),
    _HwIsmNENodeType_Type()
)
hwIsmNENodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeType.setStatus("current")


class _HwIsmNENodeWorkingMode_Type(Integer32):
    """Custom type hwIsmNENodeWorkingMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2", 2),
          ("mode3", 3),
          ("mode4", 4))
    )


_HwIsmNENodeWorkingMode_Type.__name__ = "Integer32"
_HwIsmNENodeWorkingMode_Object = MibTableColumn
hwIsmNENodeWorkingMode = _HwIsmNENodeWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 3),
    _HwIsmNENodeWorkingMode_Type()
)
hwIsmNENodeWorkingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeWorkingMode.setStatus("current")
_HwIsmNENodeIPAddress_Type = IpAddress
_HwIsmNENodeIPAddress_Object = MibTableColumn
hwIsmNENodeIPAddress = _HwIsmNENodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 4),
    _HwIsmNENodeIPAddress_Type()
)
hwIsmNENodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeIPAddress.setStatus("current")
_HwIsmNENodeContextName_Type = DisplayString
_HwIsmNENodeContextName_Object = MibTableColumn
hwIsmNENodeContextName = _HwIsmNENodeContextName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 5),
    _HwIsmNENodeContextName_Type()
)
hwIsmNENodeContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeContextName.setStatus("current")
_HwIsmNENodeContextEngineID_Type = DisplayString
_HwIsmNENodeContextEngineID_Object = MibTableColumn
hwIsmNENodeContextEngineID = _HwIsmNENodeContextEngineID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 6),
    _HwIsmNENodeContextEngineID_Type()
)
hwIsmNENodeContextEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeContextEngineID.setStatus("current")
_HwIsmNENodeClusterName_Type = DisplayString
_HwIsmNENodeClusterName_Object = MibTableColumn
hwIsmNENodeClusterName = _HwIsmNENodeClusterName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 7),
    _HwIsmNENodeClusterName_Type()
)
hwIsmNENodeClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeClusterName.setStatus("current")


class _HwIsmNENodeRunningStatus_Type(Integer32):
    """Custom type hwIsmNENodeRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("freedom", 2))
    )


_HwIsmNENodeRunningStatus_Type.__name__ = "Integer32"
_HwIsmNENodeRunningStatus_Object = MibTableColumn
hwIsmNENodeRunningStatus = _HwIsmNENodeRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 8),
    _HwIsmNENodeRunningStatus_Type()
)
hwIsmNENodeRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmNENodeRunningStatus.setStatus("current")
_HwIsmNENodeId_Type = OctetString
_HwIsmNENodeId_Object = MibTableColumn
hwIsmNENodeId = _HwIsmNENodeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 9),
    _HwIsmNENodeId_Type()
)
hwIsmNENodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmNENodeId.setStatus("current")
_HwIsmNENodeName_Type = OctetString
_HwIsmNENodeName_Object = MibTableColumn
hwIsmNENodeName = _HwIsmNENodeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 10),
    _HwIsmNENodeName_Type()
)
hwIsmNENodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmNENodeName.setStatus("current")
_HwIsmNENodeArrayStatus_Type = Integer32
_HwIsmNENodeArrayStatus_Object = MibTableColumn
hwIsmNENodeArrayStatus = _HwIsmNENodeArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 11),
    _HwIsmNENodeArrayStatus_Type()
)
hwIsmNENodeArrayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmNENodeArrayStatus.setStatus("current")
_HwIsmNENodeLocation_Type = OctetString
_HwIsmNENodeLocation_Object = MibTableColumn
hwIsmNENodeLocation = _HwIsmNENodeLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 12),
    _HwIsmNENodeLocation_Type()
)
hwIsmNENodeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmNENodeLocation.setStatus("current")
_HwIsmNENodeControllerIpList_Type = OctetString
_HwIsmNENodeControllerIpList_Object = MibTableColumn
hwIsmNENodeControllerIpList = _HwIsmNENodeControllerIpList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 13),
    _HwIsmNENodeControllerIpList_Type()
)
hwIsmNENodeControllerIpList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmNENodeControllerIpList.setStatus("current")
_HwIsmNEType_Type = Integer32
_HwIsmNEType_Object = MibTableColumn
hwIsmNEType = _HwIsmNEType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 9, 1, 1, 1, 14),
    _HwIsmNEType_Type()
)
hwIsmNEType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmNEType.setStatus("current")
_HwIsmNotification_ObjectIdentity = ObjectIdentity
hwIsmNotification = _HwIsmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10)
)
_HwIsmActiveAlarmInfo_ObjectIdentity = ObjectIdentity
hwIsmActiveAlarmInfo = _HwIsmActiveAlarmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1)
)
_HwIsmActiveAlarmInfoTable_Object = MibTable
hwIsmActiveAlarmInfoTable = _HwIsmActiveAlarmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1)
)
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoTable.setStatus("current")
_HwIsmActiveAlarmInfoEntry_Object = MibTableRow
hwIsmActiveAlarmInfoEntry = _HwIsmActiveAlarmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1)
)
hwIsmActiveAlarmInfoEntry.setIndexNames(
    (0, "ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoNodeCode"),
    (0, "ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoSerialNo"),
)
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoEntry.setStatus("current")
_HwIsmActiveAlarmInfoNodeCode_Type = NodeCodeString
_HwIsmActiveAlarmInfoNodeCode_Object = MibTableColumn
hwIsmActiveAlarmInfoNodeCode = _HwIsmActiveAlarmInfoNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 1),
    _HwIsmActiveAlarmInfoNodeCode_Type()
)
hwIsmActiveAlarmInfoNodeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoNodeCode.setStatus("current")
_HwIsmActiveAlarmInfoLocationInfo_Type = DisplayString
_HwIsmActiveAlarmInfoLocationInfo_Object = MibTableColumn
hwIsmActiveAlarmInfoLocationInfo = _HwIsmActiveAlarmInfoLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 2),
    _HwIsmActiveAlarmInfoLocationInfo_Type()
)
hwIsmActiveAlarmInfoLocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoLocationInfo.setStatus("current")
_HwIsmActiveAlarmInfoRestoreAdvice_Type = DisplayString
_HwIsmActiveAlarmInfoRestoreAdvice_Object = MibTableColumn
hwIsmActiveAlarmInfoRestoreAdvice = _HwIsmActiveAlarmInfoRestoreAdvice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 3),
    _HwIsmActiveAlarmInfoRestoreAdvice_Type()
)
hwIsmActiveAlarmInfoRestoreAdvice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoRestoreAdvice.setStatus("current")
_HwIsmActiveAlarmInfoTitle_Type = DisplayString
_HwIsmActiveAlarmInfoTitle_Object = MibTableColumn
hwIsmActiveAlarmInfoTitle = _HwIsmActiveAlarmInfoTitle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 4),
    _HwIsmActiveAlarmInfoTitle_Type()
)
hwIsmActiveAlarmInfoTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoTitle.setStatus("current")


class _HwIsmActiveAlarmInfoType_Type(Integer32):
    """Custom type hwIsmActiveAlarmInfoType based on Integer32"""
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


_HwIsmActiveAlarmInfoType_Type.__name__ = "Integer32"
_HwIsmActiveAlarmInfoType_Object = MibTableColumn
hwIsmActiveAlarmInfoType = _HwIsmActiveAlarmInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 5),
    _HwIsmActiveAlarmInfoType_Type()
)
hwIsmActiveAlarmInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoType.setStatus("current")


class _HwIsmActiveAlarmInfoLevel_Type(Integer32):
    """Custom type hwIsmActiveAlarmInfoLevel based on Integer32"""
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


_HwIsmActiveAlarmInfoLevel_Type.__name__ = "Integer32"
_HwIsmActiveAlarmInfoLevel_Object = MibTableColumn
hwIsmActiveAlarmInfoLevel = _HwIsmActiveAlarmInfoLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 6),
    _HwIsmActiveAlarmInfoLevel_Type()
)
hwIsmActiveAlarmInfoLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoLevel.setStatus("current")
_HwIsmActiveAlarmInfoAlarmID_Type = Gauge32
_HwIsmActiveAlarmInfoAlarmID_Object = MibTableColumn
hwIsmActiveAlarmInfoAlarmID = _HwIsmActiveAlarmInfoAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 7),
    _HwIsmActiveAlarmInfoAlarmID_Type()
)
hwIsmActiveAlarmInfoAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoAlarmID.setStatus("current")
_HwIsmActiveAlarmInfoOccurTime_Type = DateAndTime
_HwIsmActiveAlarmInfoOccurTime_Object = MibTableColumn
hwIsmActiveAlarmInfoOccurTime = _HwIsmActiveAlarmInfoOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 8),
    _HwIsmActiveAlarmInfoOccurTime_Type()
)
hwIsmActiveAlarmInfoOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoOccurTime.setStatus("current")
_HwIsmActiveAlarmInfoSerialNo_Type = Gauge32
_HwIsmActiveAlarmInfoSerialNo_Object = MibTableColumn
hwIsmActiveAlarmInfoSerialNo = _HwIsmActiveAlarmInfoSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 9),
    _HwIsmActiveAlarmInfoSerialNo_Type()
)
hwIsmActiveAlarmInfoSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoSerialNo.setStatus("current")
_HwIsmActiveAlarmInfoAddtionInfo_Type = OctetString
_HwIsmActiveAlarmInfoAddtionInfo_Object = MibTableColumn
hwIsmActiveAlarmInfoAddtionInfo = _HwIsmActiveAlarmInfoAddtionInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 10),
    _HwIsmActiveAlarmInfoAddtionInfo_Type()
)
hwIsmActiveAlarmInfoAddtionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoAddtionInfo.setStatus("current")


class _HwIsmActiveAlarmInfoCategory_Type(Integer32):
    """Custom type hwIsmActiveAlarmInfoCategory based on Integer32"""
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


_HwIsmActiveAlarmInfoCategory_Type.__name__ = "Integer32"
_HwIsmActiveAlarmInfoCategory_Object = MibTableColumn
hwIsmActiveAlarmInfoCategory = _HwIsmActiveAlarmInfoCategory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 11),
    _HwIsmActiveAlarmInfoCategory_Type()
)
hwIsmActiveAlarmInfoCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoCategory.setStatus("current")
_HwIsmActiveAlarmInfoLocalAlarmID_Type = Counter64
_HwIsmActiveAlarmInfoLocalAlarmID_Object = MibTableColumn
hwIsmActiveAlarmInfoLocalAlarmID = _HwIsmActiveAlarmInfoLocalAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 1, 1, 12),
    _HwIsmActiveAlarmInfoLocalAlarmID_Type()
)
hwIsmActiveAlarmInfoLocalAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIsmActiveAlarmInfoLocalAlarmID.setStatus("current")
_HwIsmClearedAlarmConfirm_Type = Gauge32
_HwIsmClearedAlarmConfirm_Object = MibScalar
hwIsmClearedAlarmConfirm = _HwIsmClearedAlarmConfirm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 1, 2),
    _HwIsmClearedAlarmConfirm_Type()
)
hwIsmClearedAlarmConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIsmClearedAlarmConfirm.setStatus("current")
_HwIsmNotificationType_ObjectIdentity = ObjectIdentity
hwIsmNotificationType = _HwIsmNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2)
)
_HwinfoFaultNotificationType_ObjectIdentity = ObjectIdentity
hwinfoFaultNotificationType = _HwinfoFaultNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2, 1)
)
_HwIsmFaultNotificationTypeV2_ObjectIdentity = ObjectIdentity
hwIsmFaultNotificationTypeV2 = _HwIsmFaultNotificationTypeV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2, 1, 0)
)
if mibBuilder.loadTexts:
    hwIsmFaultNotificationTypeV2.setStatus("current")
_HwIsmEventNotificationType_ObjectIdentity = ObjectIdentity
hwIsmEventNotificationType = _HwIsmEventNotificationType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2, 2)
)
_HwIsmEventNotificationTypeV2_ObjectIdentity = ObjectIdentity
hwIsmEventNotificationTypeV2 = _HwIsmEventNotificationTypeV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2, 2, 0)
)
if mibBuilder.loadTexts:
    hwIsmEventNotificationTypeV2.setStatus("current")
_HwIsmTrapNotification_ObjectIdentity = ObjectIdentity
hwIsmTrapNotification = _HwIsmTrapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3)
)
_HwIsmFaultNotification_ObjectIdentity = ObjectIdentity
hwIsmFaultNotification = _HwIsmFaultNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1)
)
_HwIsmReportingAlarm_ObjectIdentity = ObjectIdentity
hwIsmReportingAlarm = _HwIsmReportingAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1)
)
_HwIsmReportingAlarmNodeCode_Type = NodeCodeString
_HwIsmReportingAlarmNodeCode_Object = MibScalar
hwIsmReportingAlarmNodeCode = _HwIsmReportingAlarmNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 1),
    _HwIsmReportingAlarmNodeCode_Type()
)
hwIsmReportingAlarmNodeCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmNodeCode.setStatus("current")
_HwIsmReportingAlarmLocationInfo_Type = DisplayString
_HwIsmReportingAlarmLocationInfo_Object = MibScalar
hwIsmReportingAlarmLocationInfo = _HwIsmReportingAlarmLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 2),
    _HwIsmReportingAlarmLocationInfo_Type()
)
hwIsmReportingAlarmLocationInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmLocationInfo.setStatus("current")


class _HwIsmReportingAlarmRestoreAdvice_Type(OctetString):
    """Custom type hwIsmReportingAlarmRestoreAdvice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwIsmReportingAlarmRestoreAdvice_Type.__name__ = "OctetString"
_HwIsmReportingAlarmRestoreAdvice_Object = MibScalar
hwIsmReportingAlarmRestoreAdvice = _HwIsmReportingAlarmRestoreAdvice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 3),
    _HwIsmReportingAlarmRestoreAdvice_Type()
)
hwIsmReportingAlarmRestoreAdvice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmRestoreAdvice.setStatus("current")


class _HwIsmReportingAlarmFaultTitle_Type(OctetString):
    """Custom type hwIsmReportingAlarmFaultTitle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwIsmReportingAlarmFaultTitle_Type.__name__ = "OctetString"
_HwIsmReportingAlarmFaultTitle_Object = MibScalar
hwIsmReportingAlarmFaultTitle = _HwIsmReportingAlarmFaultTitle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 4),
    _HwIsmReportingAlarmFaultTitle_Type()
)
hwIsmReportingAlarmFaultTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmFaultTitle.setStatus("current")


class _HwIsmReportingAlarmFaultType_Type(Integer32):
    """Custom type hwIsmReportingAlarmFaultType based on Integer32"""
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


_HwIsmReportingAlarmFaultType_Type.__name__ = "Integer32"
_HwIsmReportingAlarmFaultType_Object = MibScalar
hwIsmReportingAlarmFaultType = _HwIsmReportingAlarmFaultType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 5),
    _HwIsmReportingAlarmFaultType_Type()
)
hwIsmReportingAlarmFaultType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmFaultType.setStatus("current")


class _HwIsmReportingAlarmFaultLevel_Type(Integer32):
    """Custom type hwIsmReportingAlarmFaultLevel based on Integer32"""
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


_HwIsmReportingAlarmFaultLevel_Type.__name__ = "Integer32"
_HwIsmReportingAlarmFaultLevel_Object = MibScalar
hwIsmReportingAlarmFaultLevel = _HwIsmReportingAlarmFaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 6),
    _HwIsmReportingAlarmFaultLevel_Type()
)
hwIsmReportingAlarmFaultLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmFaultLevel.setStatus("current")
_HwIsmReportingAlarmAlarmID_Type = Gauge32
_HwIsmReportingAlarmAlarmID_Object = MibScalar
hwIsmReportingAlarmAlarmID = _HwIsmReportingAlarmAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 7),
    _HwIsmReportingAlarmAlarmID_Type()
)
hwIsmReportingAlarmAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmAlarmID.setStatus("current")
_HwIsmReportingAlarmFaultTime_Type = DateAndTime
_HwIsmReportingAlarmFaultTime_Object = MibScalar
hwIsmReportingAlarmFaultTime = _HwIsmReportingAlarmFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 8),
    _HwIsmReportingAlarmFaultTime_Type()
)
hwIsmReportingAlarmFaultTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmFaultTime.setStatus("current")
_HwIsmReportingAlarmSerialNo_Type = Gauge32
_HwIsmReportingAlarmSerialNo_Object = MibScalar
hwIsmReportingAlarmSerialNo = _HwIsmReportingAlarmSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 9),
    _HwIsmReportingAlarmSerialNo_Type()
)
hwIsmReportingAlarmSerialNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmSerialNo.setStatus("current")
_HwIsmReportingAlarmAdditionInfo_Type = DisplayString
_HwIsmReportingAlarmAdditionInfo_Object = MibScalar
hwIsmReportingAlarmAdditionInfo = _HwIsmReportingAlarmAdditionInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 10),
    _HwIsmReportingAlarmAdditionInfo_Type()
)
hwIsmReportingAlarmAdditionInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmAdditionInfo.setStatus("current")


class _HwIsmReportingAlarmFaultCategory_Type(Integer32):
    """Custom type hwIsmReportingAlarmFaultCategory based on Integer32"""
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


_HwIsmReportingAlarmFaultCategory_Type.__name__ = "Integer32"
_HwIsmReportingAlarmFaultCategory_Object = MibScalar
hwIsmReportingAlarmFaultCategory = _HwIsmReportingAlarmFaultCategory_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 11),
    _HwIsmReportingAlarmFaultCategory_Type()
)
hwIsmReportingAlarmFaultCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmFaultCategory.setStatus("current")
_HwIsmReportingAlarmLocationAlarmID_Type = Counter64
_HwIsmReportingAlarmLocationAlarmID_Object = MibScalar
hwIsmReportingAlarmLocationAlarmID = _HwIsmReportingAlarmLocationAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 12),
    _HwIsmReportingAlarmLocationAlarmID_Type()
)
hwIsmReportingAlarmLocationAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmLocationAlarmID.setStatus("current")
_HwIsmReportingAlarmProductModel_Type = Integer32
_HwIsmReportingAlarmProductModel_Object = MibScalar
hwIsmReportingAlarmProductModel = _HwIsmReportingAlarmProductModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 13),
    _HwIsmReportingAlarmProductModel_Type()
)
hwIsmReportingAlarmProductModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmProductModel.setStatus("current")
_HwIsmReportingAlarmProductSN_Type = OctetString
_HwIsmReportingAlarmProductSN_Object = MibScalar
hwIsmReportingAlarmProductSN = _HwIsmReportingAlarmProductSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 1, 1, 14),
    _HwIsmReportingAlarmProductSN_Type()
)
hwIsmReportingAlarmProductSN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmReportingAlarmProductSN.setStatus("current")
_HwIsmEventNotification_ObjectIdentity = ObjectIdentity
hwIsmEventNotification = _HwIsmEventNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2)
)
_HwIsmEventNotiNodeCode_Type = NodeCodeString
_HwIsmEventNotiNodeCode_Object = MibScalar
hwIsmEventNotiNodeCode = _HwIsmEventNotiNodeCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 1),
    _HwIsmEventNotiNodeCode_Type()
)
hwIsmEventNotiNodeCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiNodeCode.setStatus("current")
_HwIsmEventNotiLocationInfo_Type = DisplayString
_HwIsmEventNotiLocationInfo_Object = MibScalar
hwIsmEventNotiLocationInfo = _HwIsmEventNotiLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 2),
    _HwIsmEventNotiLocationInfo_Type()
)
hwIsmEventNotiLocationInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiLocationInfo.setStatus("current")


class _HwIsmEventNotiFaultTitle_Type(OctetString):
    """Custom type hwIsmEventNotiFaultTitle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwIsmEventNotiFaultTitle_Type.__name__ = "OctetString"
_HwIsmEventNotiFaultTitle_Object = MibScalar
hwIsmEventNotiFaultTitle = _HwIsmEventNotiFaultTitle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 3),
    _HwIsmEventNotiFaultTitle_Type()
)
hwIsmEventNotiFaultTitle.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiFaultTitle.setStatus("current")


class _HwIsmEventNotiFaultType_Type(Integer32):
    """Custom type hwIsmEventNotiFaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("objectcreation", 1),
          ("objectdeletion", 2),
          ("statechanged", 3))
    )


_HwIsmEventNotiFaultType_Type.__name__ = "Integer32"
_HwIsmEventNotiFaultType_Object = MibScalar
hwIsmEventNotiFaultType = _HwIsmEventNotiFaultType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 4),
    _HwIsmEventNotiFaultType_Type()
)
hwIsmEventNotiFaultType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiFaultType.setStatus("current")
_HwIsmEventNotiAddition_Type = DisplayString
_HwIsmEventNotiAddition_Object = MibScalar
hwIsmEventNotiAddition = _HwIsmEventNotiAddition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 5),
    _HwIsmEventNotiAddition_Type()
)
hwIsmEventNotiAddition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiAddition.setStatus("current")
_HwIsmEventNotiAlarmID_Type = Gauge32
_HwIsmEventNotiAlarmID_Object = MibScalar
hwIsmEventNotiAlarmID = _HwIsmEventNotiAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 6),
    _HwIsmEventNotiAlarmID_Type()
)
hwIsmEventNotiAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiAlarmID.setStatus("current")
_HwIsmEventNotiFaultTime_Type = DateAndTime
_HwIsmEventNotiFaultTime_Object = MibScalar
hwIsmEventNotiFaultTime = _HwIsmEventNotiFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 7),
    _HwIsmEventNotiFaultTime_Type()
)
hwIsmEventNotiFaultTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiFaultTime.setStatus("current")
_HwIsmEventNotiSerialNo_Type = Gauge32
_HwIsmEventNotiSerialNo_Object = MibScalar
hwIsmEventNotiSerialNo = _HwIsmEventNotiSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 3, 2, 8),
    _HwIsmEventNotiSerialNo_Type()
)
hwIsmEventNotiSerialNo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwIsmEventNotiSerialNo.setStatus("current")
_HwIsmTrapForwardControl_ObjectIdentity = ObjectIdentity
hwIsmTrapForwardControl = _HwIsmTrapForwardControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4)
)
_HwIsmTrapTargetAddrTable_Object = MibTable
hwIsmTrapTargetAddrTable = _HwIsmTrapTargetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1)
)
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrTable.setStatus("current")
_HwIsmTrapTargetAddrEntry_Object = MibTableRow
hwIsmTrapTargetAddrEntry = _HwIsmTrapTargetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1)
)
hwIsmTrapTargetAddrEntry.setIndexNames(
    (0, "ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrIndex"),
)
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrEntry.setStatus("current")
_HwIsmTrapTargetAddrIPAddr_Type = IpAddress
_HwIsmTrapTargetAddrIPAddr_Object = MibTableColumn
hwIsmTrapTargetAddrIPAddr = _HwIsmTrapTargetAddrIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 1),
    _HwIsmTrapTargetAddrIPAddr_Type()
)
hwIsmTrapTargetAddrIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrIPAddr.setStatus("current")
_HwIsmTrapTargetAddrPort_Type = Integer32
_HwIsmTrapTargetAddrPort_Object = MibTableColumn
hwIsmTrapTargetAddrPort = _HwIsmTrapTargetAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 2),
    _HwIsmTrapTargetAddrPort_Type()
)
hwIsmTrapTargetAddrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrPort.setStatus("current")
_HwIsmTrapTargetAddrRowStatus_Type = RowStatus
_HwIsmTrapTargetAddrRowStatus_Object = MibTableColumn
hwIsmTrapTargetAddrRowStatus = _HwIsmTrapTargetAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 3),
    _HwIsmTrapTargetAddrRowStatus_Type()
)
hwIsmTrapTargetAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrRowStatus.setStatus("current")
_HwIsmTrapTargetAddrIndex_Type = OctetString
_HwIsmTrapTargetAddrIndex_Object = MibTableColumn
hwIsmTrapTargetAddrIndex = _HwIsmTrapTargetAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 4),
    _HwIsmTrapTargetAddrIndex_Type()
)
hwIsmTrapTargetAddrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrIndex.setStatus("current")
_HwIsmTrapTargetAddrTrapVer_Type = Integer32
_HwIsmTrapTargetAddrTrapVer_Object = MibTableColumn
hwIsmTrapTargetAddrTrapVer = _HwIsmTrapTargetAddrTrapVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 5),
    _HwIsmTrapTargetAddrTrapVer_Type()
)
hwIsmTrapTargetAddrTrapVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrTrapVer.setStatus("current")
_HwIsmTrapTargetAddrIPAddrNew_Type = OctetString
_HwIsmTrapTargetAddrIPAddrNew_Object = MibTableColumn
hwIsmTrapTargetAddrIPAddrNew = _HwIsmTrapTargetAddrIPAddrNew_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 6),
    _HwIsmTrapTargetAddrIPAddrNew_Type()
)
hwIsmTrapTargetAddrIPAddrNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrIPAddrNew.setStatus("current")
_HwIsmTrapTargetAddrTrapType_Type = Integer32
_HwIsmTrapTargetAddrTrapType_Object = MibTableColumn
hwIsmTrapTargetAddrTrapType = _HwIsmTrapTargetAddrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 7),
    _HwIsmTrapTargetAddrTrapType_Type()
)
hwIsmTrapTargetAddrTrapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrTrapType.setStatus("current")
_HwIsmTrapTargetAddrUSMUserName_Type = OctetString
_HwIsmTrapTargetAddrUSMUserName_Object = MibTableColumn
hwIsmTrapTargetAddrUSMUserName = _HwIsmTrapTargetAddrUSMUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 4, 1, 1, 8),
    _HwIsmTrapTargetAddrUSMUserName_Type()
)
hwIsmTrapTargetAddrUSMUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIsmTrapTargetAddrUSMUserName.setStatus("current")
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
      *(("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoNodeCode"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoLocationInfo"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoRestoreAdvice"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoTitle"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoType"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoLevel"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoOccurTime"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoSerialNo"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoCategory"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmNodeCode"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmLocationInfo"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmRestoreAdvice"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultTitle"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultType"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultLevel"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultTime"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmSerialNo"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultCategory"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmAdditionInfo"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeCode"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeType"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeIPAddress"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeContextName"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeContextEngineID"),
        ("ISM-HUAWEI-MIB", "hwIsmClearedAlarmConfirm"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoAddtionInfo"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrIPAddr"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrPort"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrRowStatus"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmLocationAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmActiveAlarmInfoLocalAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmProductModel"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmProductSN"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrIndex"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrTrapVer"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrIPAddrNew"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrTrapType"),
        ("ISM-HUAWEI-MIB", "hwIsmTrapTargetAddrUSMUserName"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeRunningStatus"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeWorkingMode"),
        ("ISM-HUAWEI-MIB", "hwIsmNENodeClusterName"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects

hwIsmAlarmReporting = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2, 1, 0, 1)
)
hwIsmAlarmReporting.setObjects(
      *(("ISM-HUAWEI-MIB", "hwIsmReportingAlarmNodeCode"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmLocationInfo"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmRestoreAdvice"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultTitle"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultType"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultLevel"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultTime"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmSerialNo"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmLocationAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmFaultCategory"),
        ("ISM-HUAWEI-MIB", "hwIsmReportingAlarmAdditionInfo"))
)
if mibBuilder.loadTexts:
    hwIsmAlarmReporting.setStatus(
        "current"
    )

hwIsmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 91, 10, 2, 2, 0, 1)
)
hwIsmEvent.setObjects(
      *(("ISM-HUAWEI-MIB", "hwIsmEventNotiNodeCode"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiLocationInfo"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiFaultTitle"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiFaultType"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiFaultTime"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiSerialNo"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiAlarmID"),
        ("ISM-HUAWEI-MIB", "hwIsmEventNotiAddition"))
)
if mibBuilder.loadTexts:
    hwIsmEvent.setStatus(
        "current"
    )


# Notifications groups

currentNotificationGroup = NotificationGroup(
    (1, 6, 1, 2)
)
currentNotificationGroup.setObjects(
    ("ISM-HUAWEI-MIB", "hwIsmAlarmReporting")
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
      *(("ISM-HUAWEI-MIB", "currentObjectGroup"),
        ("ISM-HUAWEI-MIB", "currentNotificationGroup"))
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISM-HUAWEI-MIB",
    **{"NodeCodeString": NodeCodeString,
       "huawei": huawei,
       "products": products,
       "hwISMCommon": hwISMCommon,
       "hwIsmTopo": hwIsmTopo,
       "hwIsmAccessNodeInfo": hwIsmAccessNodeInfo,
       "hwIsmAccessNodeTable": hwIsmAccessNodeTable,
       "hwIsmAccessNodeEntry": hwIsmAccessNodeEntry,
       "hwIsmNENodeCode": hwIsmNENodeCode,
       "hwIsmNENodeType": hwIsmNENodeType,
       "hwIsmNENodeWorkingMode": hwIsmNENodeWorkingMode,
       "hwIsmNENodeIPAddress": hwIsmNENodeIPAddress,
       "hwIsmNENodeContextName": hwIsmNENodeContextName,
       "hwIsmNENodeContextEngineID": hwIsmNENodeContextEngineID,
       "hwIsmNENodeClusterName": hwIsmNENodeClusterName,
       "hwIsmNENodeRunningStatus": hwIsmNENodeRunningStatus,
       "hwIsmNENodeId": hwIsmNENodeId,
       "hwIsmNENodeName": hwIsmNENodeName,
       "hwIsmNENodeArrayStatus": hwIsmNENodeArrayStatus,
       "hwIsmNENodeLocation": hwIsmNENodeLocation,
       "hwIsmNENodeControllerIpList": hwIsmNENodeControllerIpList,
       "hwIsmNEType": hwIsmNEType,
       "hwIsmNotification": hwIsmNotification,
       "hwIsmActiveAlarmInfo": hwIsmActiveAlarmInfo,
       "hwIsmActiveAlarmInfoTable": hwIsmActiveAlarmInfoTable,
       "hwIsmActiveAlarmInfoEntry": hwIsmActiveAlarmInfoEntry,
       "hwIsmActiveAlarmInfoNodeCode": hwIsmActiveAlarmInfoNodeCode,
       "hwIsmActiveAlarmInfoLocationInfo": hwIsmActiveAlarmInfoLocationInfo,
       "hwIsmActiveAlarmInfoRestoreAdvice": hwIsmActiveAlarmInfoRestoreAdvice,
       "hwIsmActiveAlarmInfoTitle": hwIsmActiveAlarmInfoTitle,
       "hwIsmActiveAlarmInfoType": hwIsmActiveAlarmInfoType,
       "hwIsmActiveAlarmInfoLevel": hwIsmActiveAlarmInfoLevel,
       "hwIsmActiveAlarmInfoAlarmID": hwIsmActiveAlarmInfoAlarmID,
       "hwIsmActiveAlarmInfoOccurTime": hwIsmActiveAlarmInfoOccurTime,
       "hwIsmActiveAlarmInfoSerialNo": hwIsmActiveAlarmInfoSerialNo,
       "hwIsmActiveAlarmInfoAddtionInfo": hwIsmActiveAlarmInfoAddtionInfo,
       "hwIsmActiveAlarmInfoCategory": hwIsmActiveAlarmInfoCategory,
       "hwIsmActiveAlarmInfoLocalAlarmID": hwIsmActiveAlarmInfoLocalAlarmID,
       "hwIsmClearedAlarmConfirm": hwIsmClearedAlarmConfirm,
       "hwIsmNotificationType": hwIsmNotificationType,
       "hwinfoFaultNotificationType": hwinfoFaultNotificationType,
       "hwIsmFaultNotificationTypeV2": hwIsmFaultNotificationTypeV2,
       "hwIsmAlarmReporting": hwIsmAlarmReporting,
       "hwIsmEventNotificationType": hwIsmEventNotificationType,
       "hwIsmEventNotificationTypeV2": hwIsmEventNotificationTypeV2,
       "hwIsmEvent": hwIsmEvent,
       "hwIsmTrapNotification": hwIsmTrapNotification,
       "hwIsmFaultNotification": hwIsmFaultNotification,
       "hwIsmReportingAlarm": hwIsmReportingAlarm,
       "hwIsmReportingAlarmNodeCode": hwIsmReportingAlarmNodeCode,
       "hwIsmReportingAlarmLocationInfo": hwIsmReportingAlarmLocationInfo,
       "hwIsmReportingAlarmRestoreAdvice": hwIsmReportingAlarmRestoreAdvice,
       "hwIsmReportingAlarmFaultTitle": hwIsmReportingAlarmFaultTitle,
       "hwIsmReportingAlarmFaultType": hwIsmReportingAlarmFaultType,
       "hwIsmReportingAlarmFaultLevel": hwIsmReportingAlarmFaultLevel,
       "hwIsmReportingAlarmAlarmID": hwIsmReportingAlarmAlarmID,
       "hwIsmReportingAlarmFaultTime": hwIsmReportingAlarmFaultTime,
       "hwIsmReportingAlarmSerialNo": hwIsmReportingAlarmSerialNo,
       "hwIsmReportingAlarmAdditionInfo": hwIsmReportingAlarmAdditionInfo,
       "hwIsmReportingAlarmFaultCategory": hwIsmReportingAlarmFaultCategory,
       "hwIsmReportingAlarmLocationAlarmID": hwIsmReportingAlarmLocationAlarmID,
       "hwIsmReportingAlarmProductModel": hwIsmReportingAlarmProductModel,
       "hwIsmReportingAlarmProductSN": hwIsmReportingAlarmProductSN,
       "hwIsmEventNotification": hwIsmEventNotification,
       "hwIsmEventNotiNodeCode": hwIsmEventNotiNodeCode,
       "hwIsmEventNotiLocationInfo": hwIsmEventNotiLocationInfo,
       "hwIsmEventNotiFaultTitle": hwIsmEventNotiFaultTitle,
       "hwIsmEventNotiFaultType": hwIsmEventNotiFaultType,
       "hwIsmEventNotiAddition": hwIsmEventNotiAddition,
       "hwIsmEventNotiAlarmID": hwIsmEventNotiAlarmID,
       "hwIsmEventNotiFaultTime": hwIsmEventNotiFaultTime,
       "hwIsmEventNotiSerialNo": hwIsmEventNotiSerialNo,
       "hwIsmTrapForwardControl": hwIsmTrapForwardControl,
       "hwIsmTrapTargetAddrTable": hwIsmTrapTargetAddrTable,
       "hwIsmTrapTargetAddrEntry": hwIsmTrapTargetAddrEntry,
       "hwIsmTrapTargetAddrIPAddr": hwIsmTrapTargetAddrIPAddr,
       "hwIsmTrapTargetAddrPort": hwIsmTrapTargetAddrPort,
       "hwIsmTrapTargetAddrRowStatus": hwIsmTrapTargetAddrRowStatus,
       "hwIsmTrapTargetAddrIndex": hwIsmTrapTargetAddrIndex,
       "hwIsmTrapTargetAddrTrapVer": hwIsmTrapTargetAddrTrapVer,
       "hwIsmTrapTargetAddrIPAddrNew": hwIsmTrapTargetAddrIPAddrNew,
       "hwIsmTrapTargetAddrTrapType": hwIsmTrapTargetAddrTrapType,
       "hwIsmTrapTargetAddrUSMUserName": hwIsmTrapTargetAddrUSMUserName,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "currentNotificationGroup": currentNotificationGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
