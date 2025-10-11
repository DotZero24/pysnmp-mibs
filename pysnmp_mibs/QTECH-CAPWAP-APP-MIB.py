# SNMP MIB module (QTECH-CAPWAP-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-APP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:39 2025
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

(qtechDeviceMacAddress,) = mibBuilder.importSymbols(
    "QTECH-ENTITY-MIB",
    "qtechDeviceMacAddress")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(qtechSystemSerialno,) = mibBuilder.importSymbols(
    "QTECH-SYSTEM-MIB",
    "qtechSystemSerialno")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 TAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qtechCapwapAppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87)
)
if mibBuilder.loadTexts:
    qtechCapwapAppMIB.setRevisions(
        ("2010-06-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCapwapAppMIBObjects_ObjectIdentity = ObjectIdentity
qtechCapwapAppMIBObjects = _QtechCapwapAppMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1)
)
_QtechAppHeartbeatMIBObjects_ObjectIdentity = ObjectIdentity
qtechAppHeartbeatMIBObjects = _QtechAppHeartbeatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1)
)
_QtechAppHeartbeatMIBTraps_ObjectIdentity = ObjectIdentity
qtechAppHeartbeatMIBTraps = _QtechAppHeartbeatMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1, 0)
)


class _QtechAppHeartbeatOnOff_Type(Integer32):
    """Custom type qtechAppHeartbeatOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_QtechAppHeartbeatOnOff_Type.__name__ = "Integer32"
_QtechAppHeartbeatOnOff_Object = MibScalar
qtechAppHeartbeatOnOff = _QtechAppHeartbeatOnOff_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1, 1),
    _QtechAppHeartbeatOnOff_Type()
)
qtechAppHeartbeatOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppHeartbeatOnOff.setStatus("current")


class _QtechAppHeartbeatPeriod_Type(Integer32):
    """Custom type qtechAppHeartbeatPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_QtechAppHeartbeatPeriod_Type.__name__ = "Integer32"
_QtechAppHeartbeatPeriod_Object = MibScalar
qtechAppHeartbeatPeriod = _QtechAppHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1, 2),
    _QtechAppHeartbeatPeriod_Type()
)
qtechAppHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppHeartbeatPeriod.setStatus("current")
_QtechAppHeartbeatIpAddr_Type = IpAddress
_QtechAppHeartbeatIpAddr_Object = MibScalar
qtechAppHeartbeatIpAddr = _QtechAppHeartbeatIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1, 3),
    _QtechAppHeartbeatIpAddr_Type()
)
qtechAppHeartbeatIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppHeartbeatIpAddr.setStatus("current")
_QtechAppHeartbeatTimeStamp_Type = TimeTicks
_QtechAppHeartbeatTimeStamp_Object = MibScalar
qtechAppHeartbeatTimeStamp = _QtechAppHeartbeatTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1, 4),
    _QtechAppHeartbeatTimeStamp_Type()
)
qtechAppHeartbeatTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppHeartbeatTimeStamp.setStatus("current")
_QtechAppAdminInfoMIBObjects_ObjectIdentity = ObjectIdentity
qtechAppAdminInfoMIBObjects = _QtechAppAdminInfoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2)
)
_QtechAppAdminMIBTraps_ObjectIdentity = ObjectIdentity
qtechAppAdminMIBTraps = _QtechAppAdminMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 0)
)
_QtechAppAdminInfoTable_Object = MibTable
qtechAppAdminInfoTable = _QtechAppAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechAppAdminInfoTable.setStatus("current")
_QtechAppAdminInfoEntry_Object = MibTableRow
qtechAppAdminInfoEntry = _QtechAppAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 1, 1)
)
qtechAppAdminInfoEntry.setIndexNames(
    (0, "QTECH-CAPWAP-APP-MIB", "qtechAppAdminName"),
)
if mibBuilder.loadTexts:
    qtechAppAdminInfoEntry.setStatus("current")


class _QtechAppAdminName_Type(DisplayString):
    """Custom type qtechAppAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechAppAdminName_Type.__name__ = "DisplayString"
_QtechAppAdminName_Object = MibTableColumn
qtechAppAdminName = _QtechAppAdminName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 1, 1, 1),
    _QtechAppAdminName_Type()
)
qtechAppAdminName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppAdminName.setStatus("current")


class _QtechAppAdminPwd_Type(DisplayString):
    """Custom type qtechAppAdminPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAppAdminPwd_Type.__name__ = "DisplayString"
_QtechAppAdminPwd_Object = MibTableColumn
qtechAppAdminPwd = _QtechAppAdminPwd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 1, 1, 2),
    _QtechAppAdminPwd_Type()
)
qtechAppAdminPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAppAdminPwd.setStatus("current")
_QtechAppAdminPriLevel_Type = Integer32
_QtechAppAdminPriLevel_Object = MibTableColumn
qtechAppAdminPriLevel = _QtechAppAdminPriLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 1, 1, 3),
    _QtechAppAdminPriLevel_Type()
)
qtechAppAdminPriLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAppAdminPriLevel.setStatus("current")
_QtechAppAdminStatus_Type = RowStatus
_QtechAppAdminStatus_Object = MibTableColumn
qtechAppAdminStatus = _QtechAppAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 1, 1, 4),
    _QtechAppAdminStatus_Type()
)
qtechAppAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAppAdminStatus.setStatus("current")


class _QtechAppAdminInfoName_Type(DisplayString):
    """Custom type qtechAppAdminInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechAppAdminInfoName_Type.__name__ = "DisplayString"
_QtechAppAdminInfoName_Object = MibScalar
qtechAppAdminInfoName = _QtechAppAdminInfoName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 2),
    _QtechAppAdminInfoName_Type()
)
qtechAppAdminInfoName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminInfoName.setStatus("current")
_QtechAppAdminInfoIpAddr_Type = IpAddress
_QtechAppAdminInfoIpAddr_Object = MibScalar
qtechAppAdminInfoIpAddr = _QtechAppAdminInfoIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 3),
    _QtechAppAdminInfoIpAddr_Type()
)
qtechAppAdminInfoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminInfoIpAddr.setStatus("current")


class _QtechAppAdminInfoConfigContext_Type(OctetString):
    """Custom type qtechAppAdminInfoConfigContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_QtechAppAdminInfoConfigContext_Type.__name__ = "OctetString"
_QtechAppAdminInfoConfigContext_Object = MibScalar
qtechAppAdminInfoConfigContext = _QtechAppAdminInfoConfigContext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 4),
    _QtechAppAdminInfoConfigContext_Type()
)
qtechAppAdminInfoConfigContext.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminInfoConfigContext.setStatus("current")


class _QtechAppAdminInfoLoginType_Type(DisplayString):
    """Custom type qtechAppAdminInfoLoginType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechAppAdminInfoLoginType_Type.__name__ = "DisplayString"
_QtechAppAdminInfoLoginType_Object = MibScalar
qtechAppAdminInfoLoginType = _QtechAppAdminInfoLoginType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 5),
    _QtechAppAdminInfoLoginType_Type()
)
qtechAppAdminInfoLoginType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminInfoLoginType.setStatus("current")


class _QtechAppAdminTerminalInfo_Type(DisplayString):
    """Custom type qtechAppAdminTerminalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechAppAdminTerminalInfo_Type.__name__ = "DisplayString"
_QtechAppAdminTerminalInfo_Object = MibScalar
qtechAppAdminTerminalInfo = _QtechAppAdminTerminalInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 6),
    _QtechAppAdminTerminalInfo_Type()
)
qtechAppAdminTerminalInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminTerminalInfo.setStatus("current")
_QtechAppAdminLoginFailReason_Type = Integer32
_QtechAppAdminLoginFailReason_Object = MibScalar
qtechAppAdminLoginFailReason = _QtechAppAdminLoginFailReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 7),
    _QtechAppAdminLoginFailReason_Type()
)
qtechAppAdminLoginFailReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminLoginFailReason.setStatus("current")


class _QtechAppAdminTargetLevel_Type(Integer32):
    """Custom type qtechAppAdminTargetLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_QtechAppAdminTargetLevel_Type.__name__ = "Integer32"
_QtechAppAdminTargetLevel_Object = MibScalar
qtechAppAdminTargetLevel = _QtechAppAdminTargetLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 8),
    _QtechAppAdminTargetLevel_Type()
)
qtechAppAdminTargetLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAppAdminTargetLevel.setStatus("current")
_QtechAppPollTimeMIBObjects_ObjectIdentity = ObjectIdentity
qtechAppPollTimeMIBObjects = _QtechAppPollTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 3)
)
_QtechAppPollTimeOfLast_Type = TimeTicks
_QtechAppPollTimeOfLast_Object = MibScalar
qtechAppPollTimeOfLast = _QtechAppPollTimeOfLast_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 3, 1),
    _QtechAppPollTimeOfLast_Type()
)
qtechAppPollTimeOfLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppPollTimeOfLast.setStatus("current")
_QtechAppConfigMIBObjects_ObjectIdentity = ObjectIdentity
qtechAppConfigMIBObjects = _QtechAppConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4)
)
_QtechAppConfigMIBTraps_ObjectIdentity = ObjectIdentity
qtechAppConfigMIBTraps = _QtechAppConfigMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4, 0)
)


class _QtechAppRcvToDefConfig_Type(Integer32):
    """Custom type qtechAppRcvToDefConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_QtechAppRcvToDefConfig_Type.__name__ = "Integer32"
_QtechAppRcvToDefConfig_Object = MibScalar
qtechAppRcvToDefConfig = _QtechAppRcvToDefConfig_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4, 1),
    _QtechAppRcvToDefConfig_Type()
)
qtechAppRcvToDefConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppRcvToDefConfig.setStatus("current")


class _QtechAppConfigFileName_Type(DisplayString):
    """Custom type qtechAppConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechAppConfigFileName_Type.__name__ = "DisplayString"
_QtechAppConfigFileName_Object = MibScalar
qtechAppConfigFileName = _QtechAppConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4, 2),
    _QtechAppConfigFileName_Type()
)
qtechAppConfigFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppConfigFileName.setStatus("current")


class _QtechAppConfigParseErrReason_Type(DisplayString):
    """Custom type qtechAppConfigParseErrReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechAppConfigParseErrReason_Type.__name__ = "DisplayString"
_QtechAppConfigParseErrReason_Object = MibScalar
qtechAppConfigParseErrReason = _QtechAppConfigParseErrReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4, 3),
    _QtechAppConfigParseErrReason_Type()
)
qtechAppConfigParseErrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppConfigParseErrReason.setStatus("current")
_QtechAppSyslogMIBObjects_ObjectIdentity = ObjectIdentity
qtechAppSyslogMIBObjects = _QtechAppSyslogMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5)
)
_QtechAppSyslogSvcEnable_Type = TruthValue
_QtechAppSyslogSvcEnable_Object = MibScalar
qtechAppSyslogSvcEnable = _QtechAppSyslogSvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 1),
    _QtechAppSyslogSvcEnable_Type()
)
qtechAppSyslogSvcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppSyslogSvcEnable.setStatus("current")
_QtechAppSyslogReportEventLevel_Type = Integer32
_QtechAppSyslogReportEventLevel_Object = MibScalar
qtechAppSyslogReportEventLevel = _QtechAppSyslogReportEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 2),
    _QtechAppSyslogReportEventLevel_Type()
)
qtechAppSyslogReportEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppSyslogReportEventLevel.setStatus("current")
_QtechAppSyslogSvrCfgTable_Object = MibTable
qtechAppSyslogSvrCfgTable = _QtechAppSyslogSvrCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3)
)
if mibBuilder.loadTexts:
    qtechAppSyslogSvrCfgTable.setStatus("current")
_QtechAppSyslogSvrCfgEntry_Object = MibTableRow
qtechAppSyslogSvrCfgEntry = _QtechAppSyslogSvrCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3, 1)
)
qtechAppSyslogSvrCfgEntry.setIndexNames(
    (0, "QTECH-CAPWAP-APP-MIB", "qtechAppSyslogSvrNetType"),
    (0, "QTECH-CAPWAP-APP-MIB", "qtechAppSyslogSvrNetAddr"),
)
if mibBuilder.loadTexts:
    qtechAppSyslogSvrCfgEntry.setStatus("current")
_QtechAppSyslogSvrNetType_Type = InetAddressType
_QtechAppSyslogSvrNetType_Object = MibTableColumn
qtechAppSyslogSvrNetType = _QtechAppSyslogSvrNetType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3, 1, 1),
    _QtechAppSyslogSvrNetType_Type()
)
qtechAppSyslogSvrNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppSyslogSvrNetType.setStatus("current")
_QtechAppSyslogSvrNetAddr_Type = InetAddress
_QtechAppSyslogSvrNetAddr_Object = MibTableColumn
qtechAppSyslogSvrNetAddr = _QtechAppSyslogSvrNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3, 1, 2),
    _QtechAppSyslogSvrNetAddr_Type()
)
qtechAppSyslogSvrNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppSyslogSvrNetAddr.setStatus("current")
_QtechAppSyslogSvrNetPort_Type = Unsigned32
_QtechAppSyslogSvrNetPort_Object = MibTableColumn
qtechAppSyslogSvrNetPort = _QtechAppSyslogSvrNetPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3, 1, 3),
    _QtechAppSyslogSvrNetPort_Type()
)
qtechAppSyslogSvrNetPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAppSyslogSvrNetPort.setStatus("current")
_QtechAppSyslogVrfName_Type = DisplayString
_QtechAppSyslogVrfName_Object = MibTableColumn
qtechAppSyslogVrfName = _QtechAppSyslogVrfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3, 1, 4),
    _QtechAppSyslogVrfName_Type()
)
qtechAppSyslogVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAppSyslogVrfName.setStatus("current")
_QtechAppSyslogStatus_Type = RowStatus
_QtechAppSyslogStatus_Object = MibTableColumn
qtechAppSyslogStatus = _QtechAppSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 3, 1, 5),
    _QtechAppSyslogStatus_Type()
)
qtechAppSyslogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAppSyslogStatus.setStatus("current")
_QtechSyslogServerAddrInfoTable_Object = MibTable
qtechSyslogServerAddrInfoTable = _QtechSyslogServerAddrInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 4)
)
if mibBuilder.loadTexts:
    qtechSyslogServerAddrInfoTable.setStatus("current")
_QtechSyslogServerAddrInfoEntry_Object = MibTableRow
qtechSyslogServerAddrInfoEntry = _QtechSyslogServerAddrInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 4, 1)
)
qtechSyslogServerAddrInfoEntry.setIndexNames(
    (0, "QTECH-CAPWAP-APP-MIB", "qtechSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    qtechSyslogServerAddrInfoEntry.setStatus("current")
_QtechSyslogServerIndex_Type = Integer32
_QtechSyslogServerIndex_Object = MibTableColumn
qtechSyslogServerIndex = _QtechSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 4, 1, 1),
    _QtechSyslogServerIndex_Type()
)
qtechSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSyslogServerIndex.setStatus("current")
_QtechSyslogServerAddr_Type = TAddress
_QtechSyslogServerAddr_Object = MibTableColumn
qtechSyslogServerAddr = _QtechSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 4, 1, 2),
    _QtechSyslogServerAddr_Type()
)
qtechSyslogServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSyslogServerAddr.setStatus("current")
_QtechSyslogServerVrfName_Type = DisplayString
_QtechSyslogServerVrfName_Object = MibTableColumn
qtechSyslogServerVrfName = _QtechSyslogServerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 4, 1, 3),
    _QtechSyslogServerVrfName_Type()
)
qtechSyslogServerVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSyslogServerVrfName.setStatus("current")
_QtechSyslogServerStatus_Type = RowStatus
_QtechSyslogServerStatus_Object = MibTableColumn
qtechSyslogServerStatus = _QtechSyslogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 5, 4, 1, 4),
    _QtechSyslogServerStatus_Type()
)
qtechSyslogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSyslogServerStatus.setStatus("current")
_QtechAppTrapActionMIBObjects_ObjectIdentity = ObjectIdentity
qtechAppTrapActionMIBObjects = _QtechAppTrapActionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6)
)


class _QtechAppTrapActionEnable_Type(Integer32):
    """Custom type qtechAppTrapActionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableSendTrap", 0),
          ("enableSendTrap", 1))
    )


_QtechAppTrapActionEnable_Type.__name__ = "Integer32"
_QtechAppTrapActionEnable_Object = MibScalar
qtechAppTrapActionEnable = _QtechAppTrapActionEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6, 1),
    _QtechAppTrapActionEnable_Type()
)
qtechAppTrapActionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppTrapActionEnable.setStatus("current")
_QtechAppTrapActionTable_Object = MibTable
qtechAppTrapActionTable = _QtechAppTrapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6, 2)
)
if mibBuilder.loadTexts:
    qtechAppTrapActionTable.setStatus("current")
_QtechAppTrapActionEntry_Object = MibTableRow
qtechAppTrapActionEntry = _QtechAppTrapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6, 2, 1)
)
qtechAppTrapActionEntry.setIndexNames(
    (0, "QTECH-CAPWAP-APP-MIB", "qtechAppTrapType"),
)
if mibBuilder.loadTexts:
    qtechAppTrapActionEntry.setStatus("current")


class _QtechAppTrapType_Type(Integer32):
    """Custom type qtechAppTrapType based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              123,
              124,
              125,
              126,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              196,
              197,
              198,
              199,
              200,
              201,
              202)
        )
    )
    namedValues = NamedValues(
        *(("gencoldstart", 1),
          ("genwarmstart", 2),
          ("genlinkdown", 3),
          ("genlinkup", 4),
          ("genauthenfail", 5),
          ("genegpnbloss", 6),
          ("spenewroot", 7),
          ("spetopchange", 8),
          ("spehardchange", 9),
          ("speportsecuviolation", 10),
          ("spestormviolation", 11),
          ("spemacnotification", 12),
          ("spevrrpnewmaster", 13),
          ("spevrrpauthfailure", 14),
          ("spepowerstatetrans", 15),
          ("spefanstatetrans", 16),
          ("speospf", 17),
          ("speospfvifstatechange", 18),
          ("speospfnbrstatechange", 19),
          ("speospfvifnbrstatechange", 20),
          ("speospfifconfigerror", 21),
          ("speospfvifconfigerror", 22),
          ("speospfifauthfailure", 23),
          ("speospfvifauthfailure", 24),
          ("speospfifrxbadpacket", 25),
          ("speospfvifrxbadpacket", 26),
          ("speospftxretransmit", 27),
          ("speospfviftxretransmit", 28),
          ("speospforiginatelsa", 29),
          ("speospfmaxagelsa", 30),
          ("speospflsdboverflow", 31),
          ("speospflsdbapproachingoverflow", 32),
          ("speospfifstatechange", 33),
          ("spebgpestablished", 34),
          ("spebgpbackwardtransition", 35),
          ("speisisdatabaseoverload", 36),
          ("speisismanualaddressdrop", 37),
          ("speisiscorruptedlspdetected", 38),
          ("speisisattempttoexceedmaxseq", 39),
          ("speisisidlenmismatch", 40),
          ("speisismaxareaaddrmismatch", 41),
          ("speisisownlsppurge", 42),
          ("speisisseqnumberskip", 43),
          ("speisisauthtypefailure", 44),
          ("speisisauthfailure", 45),
          ("speisisversionskew", 46),
          ("speisisareamismatch", 47),
          ("speisisrejectedadj", 48),
          ("speisislsptoolargetopropagate", 49),
          ("speisisoriglspbufsizemismatch", 50),
          ("speisisprotocolsupportedmismatch", 51),
          ("speisisadjchange", 52),
          ("spepim", 53),
          ("speigmp", 54),
          ("spedvmrp", 55),
          ("speentitychange", 56),
          ("specluster", 57),
          ("spedetectipviolation", 58),
          ("spelinestate", 59),
          ("spesysguard", 60),
          ("spernfpmsgtrap", 61),
          ("sperrmclientsfailedtrap", 62),
          ("sperrmloadfailedtrap", 63),
          ("sperrmnoisefailedtrap", 64),
          ("sperrminterferencefailedtrap", 65),
          ("sperrmperformancefailedtrap", 66),
          ("sperrmclientspasstrap", 67),
          ("sperrmloadpasstrap", 68),
          ("sperrmnoisepasstrap", 69),
          ("sperrminterferencepasstrap", 70),
          ("sperrmperformancepasstrap", 71),
          ("sperrmchannelchangetrap", 72),
          ("sperrmtxpowerchangetrap", 73),
          ("sperrmleaderachangetrap", 74),
          ("sperrmleaderbchangetrap", 75),
          ("sperrmdfsfreecountatrap", 76),
          ("sperrmdfsfreecountbtrap", 77),
          ("sperrmneighborapintertrap", 78),
          ("sperrmstationintertrap", 79),
          ("sperrmotherdiveceintertrap", 80),
          ("rmonalarmfallingtrap", 81),
          ("rmonalarmrisingtrap", 82),
          ("smpframerelaytrap", 83),
          ("priventitytrans", 84),
          ("privtemperaturetrans", 85),
          ("speipv6ifstatechange", 86),
          ("psmachashconflicttrap", 87),
          ("privwebauthuserleave", 88),
          ("radiusauthserverdowntrap", 89),
          ("radiusacctserverdowntrap", 90),
          ("configurationerrortrap", 91),
          ("cpuusagetoohightrap", 92),
          ("cpuusagetoohighrecovtrap", 93),
          ("memusagetoohightrap", 94),
          ("memusagetoohighrecovtrap", 95),
          ("systmcoldstarttrap", 96),
          ("ipaddrchangetrap", 97),
          ("apmtworkmodechgtrap", 98),
          ("apswupdatefailtrap", 99),
          ("ssidkeyconflicttrap", 100),
          ("fatapheartbeattrap", 101),
          ("acconfigurationerrortrap", 102),
          ("accpuusagetoohightrap", 103),
          ("accpuusagetoohighrecovtrap", 104),
          ("acmemusagetoohightrap", 105),
          ("acmemusagetoohighrecovtrap", 106),
          ("acofflinetrap", 107),
          ("aconlinetrap", 108),
          ("acapmtworkmodechgtrap", 109),
          ("acapswupdatefailtrap", 110),
          ("acssidkeyconflicttrap", 111),
          ("acfatapheartbeattrap", 112),
          ("staauthfailtrap", 113),
          ("staassofailtrap", 114),
          ("acstaauthfailtrap", 115),
          ("acstaassofailtrap", 116),
          ("invalidcertinvadetrap", 117),
          ("repaccacktrap", 118),
          ("tamperattacktrap", 119),
          ("lowersafeattacktrap", 120),
          ("addrredirectiontrap", 121),
          ("acinvalidcertinvadetrap", 122),
          ("acrepaccacktrap", 123),
          ("actamperattacktrap", 124),
          ("aclowersafeattacktrap", 125),
          ("acaddrredirectiontrap", 126),
          ("widsieee80211connect", 127),
          ("widsieee80211disconnect", 128),
          ("widsieee80211reauthentication", 129),
          ("widsieee80211authenticationfailure", 130),
          ("widsieee80211connectfailure", 131),
          ("apcointerfdetectedtrap", 132),
          ("apcointerfcleartrap", 133),
          ("apnerborinterfdetectedtrap", 134),
          ("apneiborinterfcleartrap", 135),
          ("stainterfdetectedtrap", 136),
          ("stainterfcleartrap", 137),
          ("otherdeviceinterfdetectedtrap", 138),
          ("otherdevinterfcleartrap", 139),
          ("radiodowntrap", 140),
          ("radiodownrecovtrap", 141),
          ("apstafulltrap", 142),
          ("apstafullrecovertrap", 143),
          ("apmtrdochanlchgtrap", 144),
          ("acapcointerfdetectedtrap", 145),
          ("acapcointerfcleartrap", 146),
          ("acapnerborinterfdetectedtrap", 147),
          ("acapneiborinterfcleartrap", 148),
          ("acstainterfdetectedtrap", 149),
          ("acstainterfcleartrap", 150),
          ("acotherdeviceinterfdetectedtrap", 151),
          ("acotherdevinterfcleartrap", 152),
          ("acradiodowntrap", 153),
          ("acradiodownrecovtrap", 154),
          ("acapstafulltrap", 155),
          ("acapstafullrecovertrap", 156),
          ("acapmtrdochanlchgtrap", 157),
          ("acspeciousdevicedetecttrap", 158),
          ("acrxpackage", 159),
          ("accpuusage", 160),
          ("capwapbasechanup", 161),
          ("capwapbasechandown", 162),
          ("capwapbasedecrypterrorreport", 163),
          ("capwapbasejoinfail", 164),
          ("capwapbaseimageupgradefail", 165),
          ("capwapbaseconifgmsgerror", 166),
          ("capwapbaseradiooperstatu", 167),
          ("capwapbaseauthenfail", 168),
          ("apmgmtaptimestamp", 169),
          ("apmgmtstaoper", 170),
          ("apmgmtmbchange", 171),
          ("apmgmtapswupdtfail", 172),
          ("widswarninginfo", 173),
          ("privcmccportalunavailable", 174),
          ("privipaddrchange", 175),
          ("dhcppoolexhaust", 176),
          ("dhcppoolnoexhaust", 177),
          ("speheartbeatperiodtrap", 178),
          ("tftpupgradefailed", 179),
          ("syscpuhigh", 180),
          ("syscpuhighrecov", 181),
          ("systemperaturehigh", 182),
          ("systemperaturehighrecov", 183),
          ("sysmemoryhigh", 184),
          ("sysmemoryhighrecov", 185),
          ("speconfigmodifytrap", 186),
          ("speconfigparseerrtrap", 187),
          ("apmgmtstaactoverthrehold", 188),
          ("apmgmtstadisactoverthredhold", 189),
          ("apmgmtstaroamtotaloverthredhlod", 190),
          ("apmgmtstaroamoerminoverthredhold", 191),
          ("apmgmtapwritebuffero", 192),
          ("apmgmtacheartbeat", 193),
          ("apmgmtacpowerstatus", 194),
          ("radiusauthserverrecovertrap", 195),
          ("radiusacctserverrecovertrap", 196),
          ("privcmccportalavailable", 197),
          ("sysapcpuhigh", 198),
          ("sysapcpuhighrecov", 199),
          ("sysapmemoryhigh", 200),
          ("sysapmemoryhighrecov", 201),
          ("syssystemreset", 202))
    )


_QtechAppTrapType_Type.__name__ = "Integer32"
_QtechAppTrapType_Object = MibTableColumn
qtechAppTrapType = _QtechAppTrapType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6, 2, 1, 1),
    _QtechAppTrapType_Type()
)
qtechAppTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAppTrapType.setStatus("current")


class _QtechAppTrapAction_Type(Integer32):
    """Custom type qtechAppTrapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_QtechAppTrapAction_Type.__name__ = "Integer32"
_QtechAppTrapAction_Object = MibTableColumn
qtechAppTrapAction = _QtechAppTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6, 2, 1, 2),
    _QtechAppTrapAction_Type()
)
qtechAppTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppTrapAction.setStatus("current")
_QtechAppTrapDescr_Type = DisplayString
_QtechAppTrapDescr_Object = MibTableColumn
qtechAppTrapDescr = _QtechAppTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 6, 2, 1, 3),
    _QtechAppTrapDescr_Type()
)
qtechAppTrapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAppTrapDescr.setStatus("current")
_QtechZCMMIBObjects_ObjectIdentity = ObjectIdentity
qtechZCMMIBObjects = _QtechZCMMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 7)
)
_QtechZCMMIBTraps_ObjectIdentity = ObjectIdentity
qtechZCMMIBTraps = _QtechZCMMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 7, 0)
)
_QtechAssignedIPAddress_Type = IpAddress
_QtechAssignedIPAddress_Object = MibScalar
qtechAssignedIPAddress = _QtechAssignedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 7, 1),
    _QtechAssignedIPAddress_Type()
)
qtechAssignedIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAssignedIPAddress.setStatus("current")


class _QtechNeedConfiguration_Type(Integer32):
    """Custom type qtechNeedConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QtechNeedConfiguration_Type.__name__ = "Integer32"
_QtechNeedConfiguration_Object = MibScalar
qtechNeedConfiguration = _QtechNeedConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 7, 2),
    _QtechNeedConfiguration_Type()
)
qtechNeedConfiguration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechNeedConfiguration.setStatus("current")
_QtechCapwapAppMIBConformance_ObjectIdentity = ObjectIdentity
qtechCapwapAppMIBConformance = _QtechCapwapAppMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 2)
)
_QtechCapwapAppMIBCompliances_ObjectIdentity = ObjectIdentity
qtechCapwapAppMIBCompliances = _QtechCapwapAppMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 2, 1)
)
_QtechCapwapAppMIBGroups_ObjectIdentity = ObjectIdentity
qtechCapwapAppMIBGroups = _QtechCapwapAppMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 2, 2)
)

# Managed Objects groups

qtechCapwapAppMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 2, 2, 1)
)
qtechCapwapAppMIBGroup.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppHeartbeatOnOff"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppHeartbeatPeriod"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppHeartbeatIpAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppHeartbeatTimeStamp"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminPwd"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminPriLevel"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminStatus"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppPollTimeOfLast"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppRcvToDefConfig"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppConfigFileName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppConfigParseErrReason"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogSvcEnable"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogReportEventLevel"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogSvrNetType"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogSvrNetAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogSvrNetPort"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogVrfName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppSyslogStatus"),
        ("QTECH-CAPWAP-APP-MIB", "qtechSyslogServerAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechSyslogServerVrfName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechSyslogServerStatus"))
)
if mibBuilder.loadTexts:
    qtechCapwapAppMIBGroup.setStatus("current")


# Notification objects

qtechAppHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 1, 0, 1)
)
qtechAppHeartbeatTrap.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppHeartbeatIpAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppHeartbeatTimeStamp"))
)
if mibBuilder.loadTexts:
    qtechAppHeartbeatTrap.setStatus(
        "current"
    )

qtechAppAdminLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 0, 1)
)
qtechAppAdminLoginTrap.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoIpAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoLoginType"))
)
if mibBuilder.loadTexts:
    qtechAppAdminLoginTrap.setStatus(
        "current"
    )

qtechAppAdminModifyConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 0, 2)
)
qtechAppAdminModifyConfigTrap.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoIpAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoConfigContext"))
)
if mibBuilder.loadTexts:
    qtechAppAdminModifyConfigTrap.setStatus(
        "current"
    )

qtechAppAdminLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 0, 3)
)
qtechAppAdminLoginFailTrap.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoIpAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminTerminalInfo"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminLoginFailReason"))
)
if mibBuilder.loadTexts:
    qtechAppAdminLoginFailTrap.setStatus(
        "current"
    )

qtechAppAdminEnableFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 2, 0, 4)
)
qtechAppAdminEnableFailTrap.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminInfoIpAddr"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminTerminalInfo"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppAdminTargetLevel"))
)
if mibBuilder.loadTexts:
    qtechAppAdminEnableFailTrap.setStatus(
        "current"
    )

qtechAppConfigModifyFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    qtechAppConfigModifyFileTrap.setStatus(
        "current"
    )

qtechAppConfigParseErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 4, 0, 2)
)
qtechAppConfigParseErrTrap.setObjects(
      *(("QTECH-CAPWAP-APP-MIB", "qtechAppConfigFileName"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAppConfigParseErrReason"))
)
if mibBuilder.loadTexts:
    qtechAppConfigParseErrTrap.setStatus(
        "current"
    )

qtechZCMNotifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 1, 7, 0, 1)
)
qtechZCMNotifyTrap.setObjects(
      *(("QTECH-SYSTEM-MIB", "qtechSystemSerialno"),
        ("QTECH-ENTITY-MIB", "qtechDeviceMacAddress"),
        ("QTECH-CAPWAP-APP-MIB", "qtechAssignedIPAddress"),
        ("QTECH-CAPWAP-APP-MIB", "qtechNeedConfiguration"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    qtechZCMNotifyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechCapwapAppMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 87, 2, 1, 1)
)
qtechCapwapAppMIBCompliance.setObjects(
    ("QTECH-CAPWAP-APP-MIB", "qtechCapwapAppMIBGroup")
)
if mibBuilder.loadTexts:
    qtechCapwapAppMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-APP-MIB",
    **{"qtechCapwapAppMIB": qtechCapwapAppMIB,
       "qtechCapwapAppMIBObjects": qtechCapwapAppMIBObjects,
       "qtechAppHeartbeatMIBObjects": qtechAppHeartbeatMIBObjects,
       "qtechAppHeartbeatMIBTraps": qtechAppHeartbeatMIBTraps,
       "qtechAppHeartbeatTrap": qtechAppHeartbeatTrap,
       "qtechAppHeartbeatOnOff": qtechAppHeartbeatOnOff,
       "qtechAppHeartbeatPeriod": qtechAppHeartbeatPeriod,
       "qtechAppHeartbeatIpAddr": qtechAppHeartbeatIpAddr,
       "qtechAppHeartbeatTimeStamp": qtechAppHeartbeatTimeStamp,
       "qtechAppAdminInfoMIBObjects": qtechAppAdminInfoMIBObjects,
       "qtechAppAdminMIBTraps": qtechAppAdminMIBTraps,
       "qtechAppAdminLoginTrap": qtechAppAdminLoginTrap,
       "qtechAppAdminModifyConfigTrap": qtechAppAdminModifyConfigTrap,
       "qtechAppAdminLoginFailTrap": qtechAppAdminLoginFailTrap,
       "qtechAppAdminEnableFailTrap": qtechAppAdminEnableFailTrap,
       "qtechAppAdminInfoTable": qtechAppAdminInfoTable,
       "qtechAppAdminInfoEntry": qtechAppAdminInfoEntry,
       "qtechAppAdminName": qtechAppAdminName,
       "qtechAppAdminPwd": qtechAppAdminPwd,
       "qtechAppAdminPriLevel": qtechAppAdminPriLevel,
       "qtechAppAdminStatus": qtechAppAdminStatus,
       "qtechAppAdminInfoName": qtechAppAdminInfoName,
       "qtechAppAdminInfoIpAddr": qtechAppAdminInfoIpAddr,
       "qtechAppAdminInfoConfigContext": qtechAppAdminInfoConfigContext,
       "qtechAppAdminInfoLoginType": qtechAppAdminInfoLoginType,
       "qtechAppAdminTerminalInfo": qtechAppAdminTerminalInfo,
       "qtechAppAdminLoginFailReason": qtechAppAdminLoginFailReason,
       "qtechAppAdminTargetLevel": qtechAppAdminTargetLevel,
       "qtechAppPollTimeMIBObjects": qtechAppPollTimeMIBObjects,
       "qtechAppPollTimeOfLast": qtechAppPollTimeOfLast,
       "qtechAppConfigMIBObjects": qtechAppConfigMIBObjects,
       "qtechAppConfigMIBTraps": qtechAppConfigMIBTraps,
       "qtechAppConfigModifyFileTrap": qtechAppConfigModifyFileTrap,
       "qtechAppConfigParseErrTrap": qtechAppConfigParseErrTrap,
       "qtechAppRcvToDefConfig": qtechAppRcvToDefConfig,
       "qtechAppConfigFileName": qtechAppConfigFileName,
       "qtechAppConfigParseErrReason": qtechAppConfigParseErrReason,
       "qtechAppSyslogMIBObjects": qtechAppSyslogMIBObjects,
       "qtechAppSyslogSvcEnable": qtechAppSyslogSvcEnable,
       "qtechAppSyslogReportEventLevel": qtechAppSyslogReportEventLevel,
       "qtechAppSyslogSvrCfgTable": qtechAppSyslogSvrCfgTable,
       "qtechAppSyslogSvrCfgEntry": qtechAppSyslogSvrCfgEntry,
       "qtechAppSyslogSvrNetType": qtechAppSyslogSvrNetType,
       "qtechAppSyslogSvrNetAddr": qtechAppSyslogSvrNetAddr,
       "qtechAppSyslogSvrNetPort": qtechAppSyslogSvrNetPort,
       "qtechAppSyslogVrfName": qtechAppSyslogVrfName,
       "qtechAppSyslogStatus": qtechAppSyslogStatus,
       "qtechSyslogServerAddrInfoTable": qtechSyslogServerAddrInfoTable,
       "qtechSyslogServerAddrInfoEntry": qtechSyslogServerAddrInfoEntry,
       "qtechSyslogServerIndex": qtechSyslogServerIndex,
       "qtechSyslogServerAddr": qtechSyslogServerAddr,
       "qtechSyslogServerVrfName": qtechSyslogServerVrfName,
       "qtechSyslogServerStatus": qtechSyslogServerStatus,
       "qtechAppTrapActionMIBObjects": qtechAppTrapActionMIBObjects,
       "qtechAppTrapActionEnable": qtechAppTrapActionEnable,
       "qtechAppTrapActionTable": qtechAppTrapActionTable,
       "qtechAppTrapActionEntry": qtechAppTrapActionEntry,
       "qtechAppTrapType": qtechAppTrapType,
       "qtechAppTrapAction": qtechAppTrapAction,
       "qtechAppTrapDescr": qtechAppTrapDescr,
       "qtechZCMMIBObjects": qtechZCMMIBObjects,
       "qtechZCMMIBTraps": qtechZCMMIBTraps,
       "qtechZCMNotifyTrap": qtechZCMNotifyTrap,
       "qtechAssignedIPAddress": qtechAssignedIPAddress,
       "qtechNeedConfiguration": qtechNeedConfiguration,
       "qtechCapwapAppMIBConformance": qtechCapwapAppMIBConformance,
       "qtechCapwapAppMIBCompliances": qtechCapwapAppMIBCompliances,
       "qtechCapwapAppMIBCompliance": qtechCapwapAppMIBCompliance,
       "qtechCapwapAppMIBGroups": qtechCapwapAppMIBGroups,
       "qtechCapwapAppMIBGroup": qtechCapwapAppMIBGroup}
)
