# SNMP MIB module (TIMETRA-DISCOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-DISCOVERY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:59:42 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxCellularImsi,
 TmnxCellularSimCardNumber) = mibBuilder.importSymbols(
    "TIMETRA-CELLULAR-MIB",
    "TmnxCellularImsi",
    "TmnxCellularSimCardNumber")

(tmnxChassisIndex,
 tmnxChassisNotifyChassisId) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxChassisIndex",
    "tmnxChassisNotifyChassisId")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortNotifyPortId,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "tmnxPortNotifyPortId")


# MODULE-IDENTITY

tmnxDiscoveryMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 112)
)
if mibBuilder.loadTexts:
    tmnxDiscoveryMIBModule.setRevisions(
        ("2017-03-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxDiscoveryStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noDiscovery", 0),
          ("connecting", 1),
          ("requestingConfig", 2),
          ("terminated", 3),
          ("complete", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxDiscoveryMIBConformance_ObjectIdentity = ObjectIdentity
tmnxDiscoveryMIBConformance = _TmnxDiscoveryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112)
)
_TmnxDiscoveryConformance_ObjectIdentity = ObjectIdentity
tmnxDiscoveryConformance = _TmnxDiscoveryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1)
)
_TmnxDiscoveryCompliances_ObjectIdentity = ObjectIdentity
tmnxDiscoveryCompliances = _TmnxDiscoveryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1, 1)
)
_TmnxDiscoveryGroups_ObjectIdentity = ObjectIdentity
tmnxDiscoveryGroups = _TmnxDiscoveryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1, 2)
)
_TmnxDiscoveryObjs_ObjectIdentity = ObjectIdentity
tmnxDiscoveryObjs = _TmnxDiscoveryObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112)
)
_TmnxDiscoveryNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxDiscoveryNotifyObjs = _TmnxDiscoveryNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1)
)
_TmnxAdpNotifyChassisSerialNum_Type = SnmpAdminString
_TmnxAdpNotifyChassisSerialNum_Object = MibScalar
tmnxAdpNotifyChassisSerialNum = _TmnxAdpNotifyChassisSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 1),
    _TmnxAdpNotifyChassisSerialNum_Type()
)
tmnxAdpNotifyChassisSerialNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifyChassisSerialNum.setStatus("current")
_TmnxAdpNotifyCellSimCardId_Type = TmnxCellularSimCardNumber
_TmnxAdpNotifyCellSimCardId_Object = MibScalar
tmnxAdpNotifyCellSimCardId = _TmnxAdpNotifyCellSimCardId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 2),
    _TmnxAdpNotifyCellSimCardId_Type()
)
tmnxAdpNotifyCellSimCardId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifyCellSimCardId.setStatus("current")
_TmnxAdpNotifyCellSimCardImsi_Type = TmnxCellularImsi
_TmnxAdpNotifyCellSimCardImsi_Object = MibScalar
tmnxAdpNotifyCellSimCardImsi = _TmnxAdpNotifyCellSimCardImsi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 3),
    _TmnxAdpNotifyCellSimCardImsi_Type()
)
tmnxAdpNotifyCellSimCardImsi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifyCellSimCardImsi.setStatus("current")
_TmnxAdpNotifyCellPdnIpAddrType_Type = InetAddressType
_TmnxAdpNotifyCellPdnIpAddrType_Object = MibScalar
tmnxAdpNotifyCellPdnIpAddrType = _TmnxAdpNotifyCellPdnIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 4),
    _TmnxAdpNotifyCellPdnIpAddrType_Type()
)
tmnxAdpNotifyCellPdnIpAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifyCellPdnIpAddrType.setStatus("current")
_TmnxAdpNotifyCellPdnIpAddr_Type = InetAddress
_TmnxAdpNotifyCellPdnIpAddr_Object = MibScalar
tmnxAdpNotifyCellPdnIpAddr = _TmnxAdpNotifyCellPdnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 5),
    _TmnxAdpNotifyCellPdnIpAddr_Type()
)
tmnxAdpNotifyCellPdnIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifyCellPdnIpAddr.setStatus("current")


class _TmnxAdpNotifyEndReason_Type(Integer32):
    """Custom type tmnxAdpNotifyEndReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operatorTerminated", 1),
          ("complete", 2))
    )


_TmnxAdpNotifyEndReason_Type.__name__ = "Integer32"
_TmnxAdpNotifyEndReason_Object = MibScalar
tmnxAdpNotifyEndReason = _TmnxAdpNotifyEndReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 6),
    _TmnxAdpNotifyEndReason_Type()
)
tmnxAdpNotifyEndReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifyEndReason.setStatus("current")
_TmnxAdpNotifySwVersion_Type = DisplayString
_TmnxAdpNotifySwVersion_Object = MibScalar
tmnxAdpNotifySwVersion = _TmnxAdpNotifySwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 1, 7),
    _TmnxAdpNotifySwVersion_Type()
)
tmnxAdpNotifySwVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxAdpNotifySwVersion.setStatus("current")
_TmnxDiscoveryTable_Object = MibTable
tmnxDiscoveryTable = _TmnxDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 2)
)
if mibBuilder.loadTexts:
    tmnxDiscoveryTable.setStatus("current")
_TmnxDiscoveryEntry_Object = MibTableRow
tmnxDiscoveryEntry = _TmnxDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 2, 1)
)
tmnxDiscoveryEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
)
if mibBuilder.loadTexts:
    tmnxDiscoveryEntry.setStatus("current")
_TmnxDiscoveryStatus_Type = TmnxDiscoveryStatus
_TmnxDiscoveryStatus_Object = MibTableColumn
tmnxDiscoveryStatus = _TmnxDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 2, 1, 1),
    _TmnxDiscoveryStatus_Type()
)
tmnxDiscoveryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDiscoveryStatus.setStatus("current")
_TmnxDiscoveryStartTime_Type = TimeStamp
_TmnxDiscoveryStartTime_Object = MibTableColumn
tmnxDiscoveryStartTime = _TmnxDiscoveryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 2, 1, 2),
    _TmnxDiscoveryStartTime_Type()
)
tmnxDiscoveryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiscoveryStartTime.setStatus("current")
_TmnxDiscoveryEndTime_Type = TimeStamp
_TmnxDiscoveryEndTime_Object = MibTableColumn
tmnxDiscoveryEndTime = _TmnxDiscoveryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 2, 1, 3),
    _TmnxDiscoveryEndTime_Type()
)
tmnxDiscoveryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDiscoveryEndTime.setStatus("current")
_TmnxDiscoveryBofInfo_ObjectIdentity = ObjectIdentity
tmnxDiscoveryBofInfo = _TmnxDiscoveryBofInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 3)
)


class _TmnxSbiDiscoverConfig_Type(TruthValue):
    """Custom type tmnxSbiDiscoverConfig based on TruthValue"""
    defaultValue = 2


_TmnxSbiDiscoverConfig_Type.__name__ = "TruthValue"
_TmnxSbiDiscoverConfig_Object = MibScalar
tmnxSbiDiscoverConfig = _TmnxSbiDiscoverConfig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 3, 1),
    _TmnxSbiDiscoverConfig_Type()
)
tmnxSbiDiscoverConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSbiDiscoverConfig.setStatus("current")


class _TmnxSbiDiscoverReqDest1_Type(DisplayString):
    """Custom type tmnxSbiDiscoverReqDest1 based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxSbiDiscoverReqDest1_Type.__name__ = "DisplayString"
_TmnxSbiDiscoverReqDest1_Object = MibScalar
tmnxSbiDiscoverReqDest1 = _TmnxSbiDiscoverReqDest1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 3, 2),
    _TmnxSbiDiscoverReqDest1_Type()
)
tmnxSbiDiscoverReqDest1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSbiDiscoverReqDest1.setStatus("current")


class _TmnxSbiDiscoverReqDest2_Type(DisplayString):
    """Custom type tmnxSbiDiscoverReqDest2 based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TmnxSbiDiscoverReqDest2_Type.__name__ = "DisplayString"
_TmnxSbiDiscoverReqDest2_Object = MibScalar
tmnxSbiDiscoverReqDest2 = _TmnxSbiDiscoverReqDest2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 112, 3, 3),
    _TmnxSbiDiscoverReqDest2_Type()
)
tmnxSbiDiscoverReqDest2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSbiDiscoverReqDest2.setStatus("current")
_TmnxDiscoveryNotificationsPrefix_ObjectIdentity = ObjectIdentity
tmnxDiscoveryNotificationsPrefix = _TmnxDiscoveryNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 112)
)
_TmnxDiscoveryNotifications_ObjectIdentity = ObjectIdentity
tmnxDiscoveryNotifications = _TmnxDiscoveryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 112, 0)
)

# Managed Objects groups

tmnxDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1, 2, 1)
)
tmnxDiscoveryGroup.setObjects(
      *(("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryStatus"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryStartTime"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryEndTime"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxSbiDiscoverConfig"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxSbiDiscoverReqDest1"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxSbiDiscoverReqDest2"))
)
if mibBuilder.loadTexts:
    tmnxDiscoveryGroup.setStatus("current")

tmnxDiscoveryGrpNotifyObjs = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1, 2, 2)
)
tmnxDiscoveryGrpNotifyObjs.setObjects(
      *(("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyChassisSerialNum"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellSimCardId"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellSimCardImsi"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellPdnIpAddrType"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellPdnIpAddr"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyEndReason"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifySwVersion"))
)
if mibBuilder.loadTexts:
    tmnxDiscoveryGrpNotifyObjs.setStatus("current")


# Notification objects

tmnxDiscoveryCellularReq = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 112, 0, 1)
)
tmnxDiscoveryCellularReq.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyChassisSerialNum"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellSimCardId"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellSimCardImsi"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellPdnIpAddrType"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyCellPdnIpAddr"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifySwVersion"))
)
if mibBuilder.loadTexts:
    tmnxDiscoveryCellularReq.setStatus(
        "current"
    )

tmnxDiscoveryEndNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 112, 0, 2)
)
tmnxDiscoveryEndNotify.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyChassisId"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyChassisSerialNum"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxAdpNotifyEndReason"))
)
if mibBuilder.loadTexts:
    tmnxDiscoveryEndNotify.setStatus(
        "current"
    )


# Notifications groups

tmnxDiscoveryNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1, 2, 3)
)
tmnxDiscoveryNotificationGroup.setObjects(
      *(("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryCellularReq"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryEndNotify"))
)
if mibBuilder.loadTexts:
    tmnxDiscoveryNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aluDiscoveryCompV1v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 112, 1, 1, 1)
)
aluDiscoveryCompV1v0.setObjects(
      *(("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryGroup"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryGrpNotifyObjs"),
        ("TIMETRA-DISCOVERY-MIB", "tmnxDiscoveryNotificationGroup"))
)
if mibBuilder.loadTexts:
    aluDiscoveryCompV1v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-DISCOVERY-MIB",
    **{"TmnxDiscoveryStatus": TmnxDiscoveryStatus,
       "tmnxDiscoveryMIBModule": tmnxDiscoveryMIBModule,
       "tmnxDiscoveryMIBConformance": tmnxDiscoveryMIBConformance,
       "tmnxDiscoveryConformance": tmnxDiscoveryConformance,
       "tmnxDiscoveryCompliances": tmnxDiscoveryCompliances,
       "aluDiscoveryCompV1v0": aluDiscoveryCompV1v0,
       "tmnxDiscoveryGroups": tmnxDiscoveryGroups,
       "tmnxDiscoveryGroup": tmnxDiscoveryGroup,
       "tmnxDiscoveryGrpNotifyObjs": tmnxDiscoveryGrpNotifyObjs,
       "tmnxDiscoveryNotificationGroup": tmnxDiscoveryNotificationGroup,
       "tmnxDiscoveryObjs": tmnxDiscoveryObjs,
       "tmnxDiscoveryNotifyObjs": tmnxDiscoveryNotifyObjs,
       "tmnxAdpNotifyChassisSerialNum": tmnxAdpNotifyChassisSerialNum,
       "tmnxAdpNotifyCellSimCardId": tmnxAdpNotifyCellSimCardId,
       "tmnxAdpNotifyCellSimCardImsi": tmnxAdpNotifyCellSimCardImsi,
       "tmnxAdpNotifyCellPdnIpAddrType": tmnxAdpNotifyCellPdnIpAddrType,
       "tmnxAdpNotifyCellPdnIpAddr": tmnxAdpNotifyCellPdnIpAddr,
       "tmnxAdpNotifyEndReason": tmnxAdpNotifyEndReason,
       "tmnxAdpNotifySwVersion": tmnxAdpNotifySwVersion,
       "tmnxDiscoveryTable": tmnxDiscoveryTable,
       "tmnxDiscoveryEntry": tmnxDiscoveryEntry,
       "tmnxDiscoveryStatus": tmnxDiscoveryStatus,
       "tmnxDiscoveryStartTime": tmnxDiscoveryStartTime,
       "tmnxDiscoveryEndTime": tmnxDiscoveryEndTime,
       "tmnxDiscoveryBofInfo": tmnxDiscoveryBofInfo,
       "tmnxSbiDiscoverConfig": tmnxSbiDiscoverConfig,
       "tmnxSbiDiscoverReqDest1": tmnxSbiDiscoverReqDest1,
       "tmnxSbiDiscoverReqDest2": tmnxSbiDiscoverReqDest2,
       "tmnxDiscoveryNotificationsPrefix": tmnxDiscoveryNotificationsPrefix,
       "tmnxDiscoveryNotifications": tmnxDiscoveryNotifications,
       "tmnxDiscoveryCellularReq": tmnxDiscoveryCellularReq,
       "tmnxDiscoveryEndNotify": tmnxDiscoveryEndNotify}
)
