# SNMP MIB module (ZTE-AN-CTRL-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-CTRL-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:03 2025
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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(ZxAnIdList,
 ZxAnIfindex,
 ZxAnPortList,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIdList",
    "ZxAnIfindex",
    "ZxAnPortList",
    "zxAn")


# MODULE-IDENTITY

zxAnCtrlMulticastMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnCtrlMulticastObjects_ObjectIdentity = ObjectIdentity
zxAnCtrlMulticastObjects = _ZxAnCtrlMulticastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1)
)
_ZxAnCtrlMcastSysMgmt_ObjectIdentity = ObjectIdentity
zxAnCtrlMcastSysMgmt = _ZxAnCtrlMcastSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1)
)


class _ZxAnIptvAccessControlEnable_Type(Integer32):
    """Custom type zxAnIptvAccessControlEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableFullMcast", 1),
          ("disable", 2))
    )


_ZxAnIptvAccessControlEnable_Type.__name__ = "Integer32"
_ZxAnIptvAccessControlEnable_Object = MibScalar
zxAnIptvAccessControlEnable = _ZxAnIptvAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 1),
    _ZxAnIptvAccessControlEnable_Type()
)
zxAnIptvAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvAccessControlEnable.setStatus("current")


class _ZxAnCtrlMcastBandwidthCtrl_Type(Integer32):
    """Custom type zxAnCtrlMcastBandwidthCtrl based on Integer32"""
    defaultValue = 2

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


_ZxAnCtrlMcastBandwidthCtrl_Type.__name__ = "Integer32"
_ZxAnCtrlMcastBandwidthCtrl_Object = MibScalar
zxAnCtrlMcastBandwidthCtrl = _ZxAnCtrlMcastBandwidthCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 2),
    _ZxAnCtrlMcastBandwidthCtrl_Type()
)
zxAnCtrlMcastBandwidthCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCtrlMcastBandwidthCtrl.setStatus("current")


class _ZxAnCtrlMcastCapabilities_Type(Bits):
    """Custom type zxAnCtrlMcastCapabilities based on Bits"""
    namedValues = NamedValues(
        ("prwRecognizeTimePkgStartEndTime", 0)
    )

_ZxAnCtrlMcastCapabilities_Type.__name__ = "Bits"
_ZxAnCtrlMcastCapabilities_Object = MibScalar
zxAnCtrlMcastCapabilities = _ZxAnCtrlMcastCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 19),
    _ZxAnCtrlMcastCapabilities_Type()
)
zxAnCtrlMcastCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCtrlMcastCapabilities.setStatus("current")
_ZxAnCtrlMcastConfInitMgmt_ObjectIdentity = ObjectIdentity
zxAnCtrlMcastConfInitMgmt = _ZxAnCtrlMcastConfInitMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 20)
)
_ZxAnCtrlMcastConfInitSmsIp_Type = IpAddress
_ZxAnCtrlMcastConfInitSmsIp_Object = MibScalar
zxAnCtrlMcastConfInitSmsIp = _ZxAnCtrlMcastConfInitSmsIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 20, 1),
    _ZxAnCtrlMcastConfInitSmsIp_Type()
)
zxAnCtrlMcastConfInitSmsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCtrlMcastConfInitSmsIp.setStatus("current")
_ZxAnCtrlMcastConfIpv6InitSms_Type = InetAddress
_ZxAnCtrlMcastConfIpv6InitSms_Object = MibScalar
zxAnCtrlMcastConfIpv6InitSms = _ZxAnCtrlMcastConfIpv6InitSms_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 20, 2),
    _ZxAnCtrlMcastConfIpv6InitSms_Type()
)
zxAnCtrlMcastConfIpv6InitSms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCtrlMcastConfIpv6InitSms.setStatus("current")
_ZxAnCtrlMcastPrw_ObjectIdentity = ObjectIdentity
zxAnCtrlMcastPrw = _ZxAnCtrlMcastPrw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 21)
)


class _ZxAnIptvPrwCounterReset_Type(Integer32):
    """Custom type zxAnIptvPrwCounterReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounter", 1)
    )


_ZxAnIptvPrwCounterReset_Type.__name__ = "Integer32"
_ZxAnIptvPrwCounterReset_Object = MibScalar
zxAnIptvPrwCounterReset = _ZxAnIptvPrwCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 21, 1),
    _ZxAnIptvPrwCounterReset_Type()
)
zxAnIptvPrwCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvPrwCounterReset.setStatus("current")


class _ZxAnIptvPrwCounterAutoResetTime_Type(Integer32):
    """Custom type zxAnIptvPrwCounterAutoResetTime based on Integer32"""
    defaultValue = 0


_ZxAnIptvPrwCounterAutoResetTime_Type.__name__ = "Integer32"
_ZxAnIptvPrwCounterAutoResetTime_Object = MibScalar
zxAnIptvPrwCounterAutoResetTime = _ZxAnIptvPrwCounterAutoResetTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 21, 2),
    _ZxAnIptvPrwCounterAutoResetTime_Type()
)
zxAnIptvPrwCounterAutoResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvPrwCounterAutoResetTime.setStatus("current")


class _ZxAnIptvPrwRecognizeTime_Type(Integer32):
    """Custom type zxAnIptvPrwRecognizeTime based on Integer32"""
    defaultValue = 5


_ZxAnIptvPrwRecognizeTime_Type.__name__ = "Integer32"
_ZxAnIptvPrwRecognizeTime_Object = MibScalar
zxAnIptvPrwRecognizeTime = _ZxAnIptvPrwRecognizeTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 21, 3),
    _ZxAnIptvPrwRecognizeTime_Type()
)
zxAnIptvPrwRecognizeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvPrwRecognizeTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIptvPrwRecognizeTime.setUnits("seconds")


class _ZxAnIptvPrwEnable_Type(Integer32):
    """Custom type zxAnIptvPrwEnable based on Integer32"""
    defaultValue = 1

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


_ZxAnIptvPrwEnable_Type.__name__ = "Integer32"
_ZxAnIptvPrwEnable_Object = MibScalar
zxAnIptvPrwEnable = _ZxAnIptvPrwEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 1, 21, 4),
    _ZxAnIptvPrwEnable_Type()
)
zxAnIptvPrwEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvPrwEnable.setStatus("current")
_ZxAnCtrlMcastAccessMgmt_ObjectIdentity = ObjectIdentity
zxAnCtrlMcastAccessMgmt = _ZxAnCtrlMcastAccessMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2)
)
_ZxAnMcastPortTable_Object = MibTable
zxAnMcastPortTable = _ZxAnMcastPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10)
)
if mibBuilder.loadTexts:
    zxAnMcastPortTable.setStatus("current")
_ZxAnMcastPortEntry_Object = MibTableRow
zxAnMcastPortEntry = _ZxAnMcastPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1)
)
zxAnMcastPortEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnMcastIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnMcastPortEntry.setStatus("current")
_ZxAnMcastIfIndex_Type = ZxAnIfindex
_ZxAnMcastIfIndex_Object = MibTableColumn
zxAnMcastIfIndex = _ZxAnMcastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 1),
    _ZxAnMcastIfIndex_Type()
)
zxAnMcastIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMcastIfIndex.setStatus("current")


class _ZxAnIptvIfConfAdminStatus_Type(Integer32):
    """Custom type zxAnIptvIfConfAdminStatus based on Integer32"""
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
        *(("start", 1),
          ("pause", 2),
          ("resume", 3),
          ("stop", 4))
    )


_ZxAnIptvIfConfAdminStatus_Type.__name__ = "Integer32"
_ZxAnIptvIfConfAdminStatus_Object = MibTableColumn
zxAnIptvIfConfAdminStatus = _ZxAnIptvIfConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 2),
    _ZxAnIptvIfConfAdminStatus_Type()
)
zxAnIptvIfConfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvIfConfAdminStatus.setStatus("current")


class _ZxAnIptvIfConfOperStatus_Type(Integer32):
    """Custom type zxAnIptvIfConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("pausedService", 2),
          ("stoppedService", 3))
    )


_ZxAnIptvIfConfOperStatus_Type.__name__ = "Integer32"
_ZxAnIptvIfConfOperStatus_Object = MibTableColumn
zxAnIptvIfConfOperStatus = _ZxAnIptvIfConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 3),
    _ZxAnIptvIfConfOperStatus_Type()
)
zxAnIptvIfConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvIfConfOperStatus.setStatus("current")


class _ZxAnIptvIfConfAuthCtrlMode_Type(Integer32):
    """Custom type zxAnIptvIfConfAuthCtrlMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlBasedPort", 1),
          ("controlBasedPkg", 2))
    )


_ZxAnIptvIfConfAuthCtrlMode_Type.__name__ = "Integer32"
_ZxAnIptvIfConfAuthCtrlMode_Object = MibTableColumn
zxAnIptvIfConfAuthCtrlMode = _ZxAnIptvIfConfAuthCtrlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 4),
    _ZxAnIptvIfConfAuthCtrlMode_Type()
)
zxAnIptvIfConfAuthCtrlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvIfConfAuthCtrlMode.setStatus("current")
_ZxAnIptvIfConfPkgIdList_Type = ZxAnIdList
_ZxAnIptvIfConfPkgIdList_Object = MibTableColumn
zxAnIptvIfConfPkgIdList = _ZxAnIptvIfConfPkgIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 5),
    _ZxAnIptvIfConfPkgIdList_Type()
)
zxAnIptvIfConfPkgIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvIfConfPkgIdList.setStatus("current")
_ZxAnIptvIfConfWatchChanIdList_Type = ZxAnIdList
_ZxAnIptvIfConfWatchChanIdList_Object = MibTableColumn
zxAnIptvIfConfWatchChanIdList = _ZxAnIptvIfConfWatchChanIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 6),
    _ZxAnIptvIfConfWatchChanIdList_Type()
)
zxAnIptvIfConfWatchChanIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvIfConfWatchChanIdList.setStatus("current")
_ZxAnIptvIfConfPrwChanIdList_Type = ZxAnIdList
_ZxAnIptvIfConfPrwChanIdList_Object = MibTableColumn
zxAnIptvIfConfPrwChanIdList = _ZxAnIptvIfConfPrwChanIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 7),
    _ZxAnIptvIfConfPrwChanIdList_Type()
)
zxAnIptvIfConfPrwChanIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvIfConfPrwChanIdList.setStatus("current")


class _ZxAnMcastPortMaxBandwidth_Type(Integer32):
    """Custom type zxAnMcastPortMaxBandwidth based on Integer32"""
    defaultValue = 2048


_ZxAnMcastPortMaxBandwidth_Type.__name__ = "Integer32"
_ZxAnMcastPortMaxBandwidth_Object = MibTableColumn
zxAnMcastPortMaxBandwidth = _ZxAnMcastPortMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 10, 1, 8),
    _ZxAnMcastPortMaxBandwidth_Type()
)
zxAnMcastPortMaxBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastPortMaxBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMcastPortMaxBandwidth.setUnits("kbps")
_ZxAnMcastPortParamListCmdTable_Object = MibTable
zxAnMcastPortParamListCmdTable = _ZxAnMcastPortParamListCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 11)
)
if mibBuilder.loadTexts:
    zxAnMcastPortParamListCmdTable.setStatus("current")
_ZxAnMcastPortParamListCmdEntry_Object = MibTableRow
zxAnMcastPortParamListCmdEntry = _ZxAnMcastPortParamListCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 11, 1)
)
zxAnMcastPortParamListCmdEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnMcastPortParamListCmd"),
)
if mibBuilder.loadTexts:
    zxAnMcastPortParamListCmdEntry.setStatus("current")


class _ZxAnMcastPortParamListCmd_Type(Integer32):
    """Custom type zxAnMcastPortParamListCmd based on Integer32"""
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
        *(("addPkg", 1),
          ("delPkg", 2),
          ("addViewChan", 3),
          ("delViewChan", 4),
          ("addPreviewChan", 5),
          ("delPreviewChan", 6))
    )


_ZxAnMcastPortParamListCmd_Type.__name__ = "Integer32"
_ZxAnMcastPortParamListCmd_Object = MibTableColumn
zxAnMcastPortParamListCmd = _ZxAnMcastPortParamListCmd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 11, 1, 1),
    _ZxAnMcastPortParamListCmd_Type()
)
zxAnMcastPortParamListCmd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMcastPortParamListCmd.setStatus("current")
_ZxAnMcastPortIndex_Type = ZxAnIfindex
_ZxAnMcastPortIndex_Object = MibTableColumn
zxAnMcastPortIndex = _ZxAnMcastPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 11, 1, 2),
    _ZxAnMcastPortIndex_Type()
)
zxAnMcastPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastPortIndex.setStatus("current")
_ZxAnMcastPortParamObjName_Type = DisplayString
_ZxAnMcastPortParamObjName_Object = MibTableColumn
zxAnMcastPortParamObjName = _ZxAnMcastPortParamObjName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 11, 1, 3),
    _ZxAnMcastPortParamObjName_Type()
)
zxAnMcastPortParamObjName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastPortParamObjName.setStatus("current")


class _ZxAnIptvNextChannelId_Type(Integer32):
    """Custom type zxAnIptvNextChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnIptvNextChannelId_Type.__name__ = "Integer32"
_ZxAnIptvNextChannelId_Object = MibScalar
zxAnIptvNextChannelId = _ZxAnIptvNextChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 12),
    _ZxAnIptvNextChannelId_Type()
)
zxAnIptvNextChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvNextChannelId.setStatus("current")
_ZxAnMcastChannelTable_Object = MibTable
zxAnMcastChannelTable = _ZxAnMcastChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13)
)
if mibBuilder.loadTexts:
    zxAnMcastChannelTable.setStatus("current")
_ZxAnMcastChannelEntry_Object = MibTableRow
zxAnMcastChannelEntry = _ZxAnMcastChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1)
)
zxAnMcastChannelEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvChanName"),
)
if mibBuilder.loadTexts:
    zxAnMcastChannelEntry.setStatus("current")


class _ZxAnIptvChanName_Type(DisplayString):
    """Custom type zxAnIptvChanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnIptvChanName_Type.__name__ = "DisplayString"
_ZxAnIptvChanName_Object = MibTableColumn
zxAnIptvChanName = _ZxAnIptvChanName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 1),
    _ZxAnIptvChanName_Type()
)
zxAnIptvChanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIptvChanName.setStatus("current")


class _ZxAnIptvMVid_Type(Integer32):
    """Custom type zxAnIptvMVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnIptvMVid_Type.__name__ = "Integer32"
_ZxAnIptvMVid_Object = MibTableColumn
zxAnIptvMVid = _ZxAnIptvMVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 2),
    _ZxAnIptvMVid_Type()
)
zxAnIptvMVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvMVid.setStatus("current")
_ZxAnMcastSrcIp_Type = IpAddress
_ZxAnMcastSrcIp_Object = MibTableColumn
zxAnMcastSrcIp = _ZxAnMcastSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 3),
    _ZxAnMcastSrcIp_Type()
)
zxAnMcastSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastSrcIp.setStatus("current")
_ZxAnMcastGrpIp_Type = IpAddress
_ZxAnMcastGrpIp_Object = MibTableColumn
zxAnMcastGrpIp = _ZxAnMcastGrpIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 4),
    _ZxAnMcastGrpIp_Type()
)
zxAnMcastGrpIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastGrpIp.setStatus("current")


class _ZxAnIptvChanId_Type(Integer32):
    """Custom type zxAnIptvChanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnIptvChanId_Type.__name__ = "Integer32"
_ZxAnIptvChanId_Object = MibTableColumn
zxAnIptvChanId = _ZxAnIptvChanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 5),
    _ZxAnIptvChanId_Type()
)
zxAnIptvChanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvChanId.setStatus("current")


class _ZxAnIptvChanPreviewProfile_Type(DisplayString):
    """Custom type zxAnIptvChanPreviewProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnIptvChanPreviewProfile_Type.__name__ = "DisplayString"
_ZxAnIptvChanPreviewProfile_Object = MibTableColumn
zxAnIptvChanPreviewProfile = _ZxAnIptvChanPreviewProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 6),
    _ZxAnIptvChanPreviewProfile_Type()
)
zxAnIptvChanPreviewProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvChanPreviewProfile.setStatus("current")


class _ZxAnIptvChanCdrEnable_Type(Integer32):
    """Custom type zxAnIptvChanCdrEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnIptvChanCdrEnable_Type.__name__ = "Integer32"
_ZxAnIptvChanCdrEnable_Object = MibTableColumn
zxAnIptvChanCdrEnable = _ZxAnIptvChanCdrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 7),
    _ZxAnIptvChanCdrEnable_Type()
)
zxAnIptvChanCdrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvChanCdrEnable.setStatus("current")


class _ZxAnIptvChanNewName_Type(DisplayString):
    """Custom type zxAnIptvChanNewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnIptvChanNewName_Type.__name__ = "DisplayString"
_ZxAnIptvChanNewName_Object = MibTableColumn
zxAnIptvChanNewName = _ZxAnIptvChanNewName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 8),
    _ZxAnIptvChanNewName_Type()
)
zxAnIptvChanNewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvChanNewName.setStatus("current")
_ZxAnIptvChanRowStatus_Type = RowStatus
_ZxAnIptvChanRowStatus_Object = MibTableColumn
zxAnIptvChanRowStatus = _ZxAnIptvChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 9),
    _ZxAnIptvChanRowStatus_Type()
)
zxAnIptvChanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvChanRowStatus.setStatus("current")


class _ZxAnIMcastGroupBandwidthCost_Type(Integer32):
    """Custom type zxAnIMcastGroupBandwidthCost based on Integer32"""
    defaultValue = 2048


_ZxAnIMcastGroupBandwidthCost_Type.__name__ = "Integer32"
_ZxAnIMcastGroupBandwidthCost_Object = MibTableColumn
zxAnIMcastGroupBandwidthCost = _ZxAnIMcastGroupBandwidthCost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 10),
    _ZxAnIMcastGroupBandwidthCost_Type()
)
zxAnIMcastGroupBandwidthCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIMcastGroupBandwidthCost.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIMcastGroupBandwidthCost.setUnits("kbps")


class _ZxAnMcastChannelAddressType_Type(InetAddressType):
    """Custom type zxAnMcastChannelAddressType based on InetAddressType"""
    defaultValue = 1


_ZxAnMcastChannelAddressType_Type.__name__ = "InetAddressType"
_ZxAnMcastChannelAddressType_Object = MibTableColumn
zxAnMcastChannelAddressType = _ZxAnMcastChannelAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 11),
    _ZxAnMcastChannelAddressType_Type()
)
zxAnMcastChannelAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastChannelAddressType.setStatus("current")
_ZxAnMcastSrcIpv6_Type = InetAddress
_ZxAnMcastSrcIpv6_Object = MibTableColumn
zxAnMcastSrcIpv6 = _ZxAnMcastSrcIpv6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 12),
    _ZxAnMcastSrcIpv6_Type()
)
zxAnMcastSrcIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastSrcIpv6.setStatus("current")
_ZxAnMcastGrpIpv6_Type = InetAddress
_ZxAnMcastGrpIpv6_Object = MibTableColumn
zxAnMcastGrpIpv6 = _ZxAnMcastGrpIpv6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 13, 1, 13),
    _ZxAnMcastGrpIpv6_Type()
)
zxAnMcastGrpIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastGrpIpv6.setStatus("current")


class _ZxAnIptvNextPkgId_Type(Integer32):
    """Custom type zxAnIptvNextPkgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnIptvNextPkgId_Type.__name__ = "Integer32"
_ZxAnIptvNextPkgId_Object = MibScalar
zxAnIptvNextPkgId = _ZxAnIptvNextPkgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 14),
    _ZxAnIptvNextPkgId_Type()
)
zxAnIptvNextPkgId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvNextPkgId.setStatus("current")
_ZxAnMcastPkgTable_Object = MibTable
zxAnMcastPkgTable = _ZxAnMcastPkgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15)
)
if mibBuilder.loadTexts:
    zxAnMcastPkgTable.setStatus("current")
_ZxAnMcastPkgEntry_Object = MibTableRow
zxAnMcastPkgEntry = _ZxAnMcastPkgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1)
)
zxAnMcastPkgEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgName"),
)
if mibBuilder.loadTexts:
    zxAnMcastPkgEntry.setStatus("current")


class _ZxAnIptvPkgName_Type(DisplayString):
    """Custom type zxAnIptvPkgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnIptvPkgName_Type.__name__ = "DisplayString"
_ZxAnIptvPkgName_Object = MibTableColumn
zxAnIptvPkgName = _ZxAnIptvPkgName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1, 1),
    _ZxAnIptvPkgName_Type()
)
zxAnIptvPkgName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIptvPkgName.setStatus("current")


class _ZxAnIptvPkgId_Type(Integer32):
    """Custom type zxAnIptvPkgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_ZxAnIptvPkgId_Type.__name__ = "Integer32"
_ZxAnIptvPkgId_Object = MibTableColumn
zxAnIptvPkgId = _ZxAnIptvPkgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1, 2),
    _ZxAnIptvPkgId_Type()
)
zxAnIptvPkgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgId.setStatus("current")


class _ZxAnIptvPkgDescription_Type(DisplayString):
    """Custom type zxAnIptvPkgDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnIptvPkgDescription_Type.__name__ = "DisplayString"
_ZxAnIptvPkgDescription_Object = MibTableColumn
zxAnIptvPkgDescription = _ZxAnIptvPkgDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1, 3),
    _ZxAnIptvPkgDescription_Type()
)
zxAnIptvPkgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgDescription.setStatus("current")
_ZxAnIptvPkgRowStatus_Type = RowStatus
_ZxAnIptvPkgRowStatus_Object = MibTableColumn
zxAnIptvPkgRowStatus = _ZxAnIptvPkgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1, 4),
    _ZxAnIptvPkgRowStatus_Type()
)
zxAnIptvPkgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgRowStatus.setStatus("current")


class _ZxAnIptvPkgStartTime_Type(DisplayString):
    """Custom type zxAnIptvPkgStartTime based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ZxAnIptvPkgStartTime_Type.__name__ = "DisplayString"
_ZxAnIptvPkgStartTime_Object = MibTableColumn
zxAnIptvPkgStartTime = _ZxAnIptvPkgStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1, 5),
    _ZxAnIptvPkgStartTime_Type()
)
zxAnIptvPkgStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgStartTime.setStatus("current")


class _ZxAnIptvPkgEndTime_Type(DisplayString):
    """Custom type zxAnIptvPkgEndTime based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_ZxAnIptvPkgEndTime_Type.__name__ = "DisplayString"
_ZxAnIptvPkgEndTime_Object = MibTableColumn
zxAnIptvPkgEndTime = _ZxAnIptvPkgEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 15, 1, 6),
    _ZxAnIptvPkgEndTime_Type()
)
zxAnIptvPkgEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgEndTime.setStatus("current")
_ZxAnMcastPkgChanTable_Object = MibTable
zxAnMcastPkgChanTable = _ZxAnMcastPkgChanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 16)
)
if mibBuilder.loadTexts:
    zxAnMcastPkgChanTable.setStatus("current")
_ZxAnMcastPkgChanEntry_Object = MibTableRow
zxAnMcastPkgChanEntry = _ZxAnMcastPkgChanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 16, 1)
)
zxAnMcastPkgChanEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgName"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvChanName"),
)
if mibBuilder.loadTexts:
    zxAnMcastPkgChanEntry.setStatus("current")


class _ZxAnIptvPkgChanAccessRight_Type(Integer32):
    """Custom type zxAnIptvPkgChanAccessRight based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRight", 0),
          ("view", 1),
          ("preview", 2))
    )


_ZxAnIptvPkgChanAccessRight_Type.__name__ = "Integer32"
_ZxAnIptvPkgChanAccessRight_Object = MibTableColumn
zxAnIptvPkgChanAccessRight = _ZxAnIptvPkgChanAccessRight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 16, 1, 1),
    _ZxAnIptvPkgChanAccessRight_Type()
)
zxAnIptvPkgChanAccessRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgChanAccessRight.setStatus("current")
_ZxAnIptvPkgChanRowStatus_Type = RowStatus
_ZxAnIptvPkgChanRowStatus_Object = MibTableColumn
zxAnIptvPkgChanRowStatus = _ZxAnIptvPkgChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 16, 1, 2),
    _ZxAnIptvPkgChanRowStatus_Type()
)
zxAnIptvPkgChanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPkgChanRowStatus.setStatus("current")
_ZxAnMcastChanPortTable_Object = MibTable
zxAnMcastChanPortTable = _ZxAnMcastChanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 17)
)
if mibBuilder.loadTexts:
    zxAnMcastChanPortTable.setStatus("current")
_ZxAnMcastChanPortEntry_Object = MibTableRow
zxAnMcastChanPortEntry = _ZxAnMcastChanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 17, 1)
)
zxAnMcastChanPortEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvChanName"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgPortListShelf"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgPortListSlot"),
)
if mibBuilder.loadTexts:
    zxAnMcastChanPortEntry.setStatus("current")
_ZxAnIptvPkgPortListShelf_Type = Integer32
_ZxAnIptvPkgPortListShelf_Object = MibTableColumn
zxAnIptvPkgPortListShelf = _ZxAnIptvPkgPortListShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 17, 1, 1),
    _ZxAnIptvPkgPortListShelf_Type()
)
zxAnIptvPkgPortListShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIptvPkgPortListShelf.setStatus("current")
_ZxAnIptvPkgPortListSlot_Type = Integer32
_ZxAnIptvPkgPortListSlot_Object = MibTableColumn
zxAnIptvPkgPortListSlot = _ZxAnIptvPkgPortListSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 17, 1, 2),
    _ZxAnIptvPkgPortListSlot_Type()
)
zxAnIptvPkgPortListSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIptvPkgPortListSlot.setStatus("current")
_ZxAnIptvChanPortListWatch_Type = ZxAnPortList
_ZxAnIptvChanPortListWatch_Object = MibTableColumn
zxAnIptvChanPortListWatch = _ZxAnIptvChanPortListWatch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 17, 1, 3),
    _ZxAnIptvChanPortListWatch_Type()
)
zxAnIptvChanPortListWatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvChanPortListWatch.setStatus("current")
_ZxAnIptvChanPortListPreview_Type = ZxAnPortList
_ZxAnIptvChanPortListPreview_Object = MibTableColumn
zxAnIptvChanPortListPreview = _ZxAnIptvChanPortListPreview_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 17, 1, 4),
    _ZxAnIptvChanPortListPreview_Type()
)
zxAnIptvChanPortListPreview.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvChanPortListPreview.setStatus("current")
_ZxAnMcastPkgPortTable_Object = MibTable
zxAnMcastPkgPortTable = _ZxAnMcastPkgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 18)
)
if mibBuilder.loadTexts:
    zxAnMcastPkgPortTable.setStatus("current")
_ZxAnMcastPkgPortEntry_Object = MibTableRow
zxAnMcastPkgPortEntry = _ZxAnMcastPkgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 18, 1)
)
zxAnMcastPkgPortEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgName"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgPortListShelf"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPkgPortListSlot"),
)
if mibBuilder.loadTexts:
    zxAnMcastPkgPortEntry.setStatus("current")
_ZxAnIptvPkgPortList_Type = ZxAnPortList
_ZxAnIptvPkgPortList_Object = MibTableColumn
zxAnIptvPkgPortList = _ZxAnIptvPkgPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 18, 1, 1),
    _ZxAnIptvPkgPortList_Type()
)
zxAnIptvPkgPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvPkgPortList.setStatus("current")
_ZxAnMcastViewConfProfileTable_Object = MibTable
zxAnMcastViewConfProfileTable = _ZxAnMcastViewConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19)
)
if mibBuilder.loadTexts:
    zxAnMcastViewConfProfileTable.setStatus("current")
_ZxAnMcastViewConfProfileEntry_Object = MibTableRow
zxAnMcastViewConfProfileEntry = _ZxAnMcastViewConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1)
)
zxAnMcastViewConfProfileEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvPreviewProfileName"),
)
if mibBuilder.loadTexts:
    zxAnMcastViewConfProfileEntry.setStatus("current")


class _ZxAnIptvPreviewProfileName_Type(DisplayString):
    """Custom type zxAnIptvPreviewProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnIptvPreviewProfileName_Type.__name__ = "DisplayString"
_ZxAnIptvPreviewProfileName_Object = MibTableColumn
zxAnIptvPreviewProfileName = _ZxAnIptvPreviewProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1, 1),
    _ZxAnIptvPreviewProfileName_Type()
)
zxAnIptvPreviewProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIptvPreviewProfileName.setStatus("current")
_ZxAnIptvPreviewMaxCount_Type = Integer32
_ZxAnIptvPreviewMaxCount_Object = MibTableColumn
zxAnIptvPreviewMaxCount = _ZxAnIptvPreviewMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1, 2),
    _ZxAnIptvPreviewMaxCount_Type()
)
zxAnIptvPreviewMaxCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPreviewMaxCount.setStatus("current")
_ZxAnIptvPreviewMaxDuration_Type = Integer32
_ZxAnIptvPreviewMaxDuration_Object = MibTableColumn
zxAnIptvPreviewMaxDuration = _ZxAnIptvPreviewMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1, 3),
    _ZxAnIptvPreviewMaxDuration_Type()
)
zxAnIptvPreviewMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPreviewMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIptvPreviewMaxDuration.setUnits("seconds")
_ZxAnIptvPreviewBlackoutInterval_Type = Integer32
_ZxAnIptvPreviewBlackoutInterval_Object = MibTableColumn
zxAnIptvPreviewBlackoutInterval = _ZxAnIptvPreviewBlackoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1, 4),
    _ZxAnIptvPreviewBlackoutInterval_Type()
)
zxAnIptvPreviewBlackoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPreviewBlackoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIptvPreviewBlackoutInterval.setUnits("seconds")
_ZxAnIptvPreviewProfileRowStatus_Type = RowStatus
_ZxAnIptvPreviewProfileRowStatus_Object = MibTableColumn
zxAnIptvPreviewProfileRowStatus = _ZxAnIptvPreviewProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1, 5),
    _ZxAnIptvPreviewProfileRowStatus_Type()
)
zxAnIptvPreviewProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPreviewProfileRowStatus.setStatus("current")


class _ZxAnIptvPreviewRecognizeTime_Type(Integer32):
    """Custom type zxAnIptvPreviewRecognizeTime based on Integer32"""
    defaultValue = 20


_ZxAnIptvPreviewRecognizeTime_Type.__name__ = "Integer32"
_ZxAnIptvPreviewRecognizeTime_Object = MibTableColumn
zxAnIptvPreviewRecognizeTime = _ZxAnIptvPreviewRecognizeTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 19, 1, 6),
    _ZxAnIptvPreviewRecognizeTime_Type()
)
zxAnIptvPreviewRecognizeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIptvPreviewRecognizeTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIptvPreviewRecognizeTime.setUnits("seconds")
_ZxAnMcastViewSchedule_ObjectIdentity = ObjectIdentity
zxAnMcastViewSchedule = _ZxAnMcastViewSchedule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20)
)


class _ZxAnMcastViewSchedObjRemoveMode_Type(Integer32):
    """Custom type zxAnMcastViewSchedObjRemoveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoRemoveExpired", 1),
          ("manualRemoveExpired", 2))
    )


_ZxAnMcastViewSchedObjRemoveMode_Type.__name__ = "Integer32"
_ZxAnMcastViewSchedObjRemoveMode_Object = MibScalar
zxAnMcastViewSchedObjRemoveMode = _ZxAnMcastViewSchedObjRemoveMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 1),
    _ZxAnMcastViewSchedObjRemoveMode_Type()
)
zxAnMcastViewSchedObjRemoveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedObjRemoveMode.setStatus("current")
_ZxAnMcastViewSchedTable_Object = MibTable
zxAnMcastViewSchedTable = _ZxAnMcastViewSchedTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10)
)
if mibBuilder.loadTexts:
    zxAnMcastViewSchedTable.setStatus("current")
_ZxAnMcastViewSchedEntry_Object = MibTableRow
zxAnMcastViewSchedEntry = _ZxAnMcastViewSchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1)
)
zxAnMcastViewSchedEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnMcastIfIndex"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnMcastViewSchedIndex"),
)
if mibBuilder.loadTexts:
    zxAnMcastViewSchedEntry.setStatus("current")
_ZxAnMcastViewSchedIndex_Type = Integer32
_ZxAnMcastViewSchedIndex_Object = MibTableColumn
zxAnMcastViewSchedIndex = _ZxAnMcastViewSchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 1),
    _ZxAnMcastViewSchedIndex_Type()
)
zxAnMcastViewSchedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedIndex.setStatus("current")


class _ZxAnMcastViewSchedObjectType_Type(Integer32):
    """Custom type zxAnMcastViewSchedObjectType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pkg", 1),
          ("channel", 2))
    )


_ZxAnMcastViewSchedObjectType_Type.__name__ = "Integer32"
_ZxAnMcastViewSchedObjectType_Object = MibTableColumn
zxAnMcastViewSchedObjectType = _ZxAnMcastViewSchedObjectType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 2),
    _ZxAnMcastViewSchedObjectType_Type()
)
zxAnMcastViewSchedObjectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedObjectType.setStatus("current")
_ZxAnMcastViewSchedObjectId_Type = Integer32
_ZxAnMcastViewSchedObjectId_Object = MibTableColumn
zxAnMcastViewSchedObjectId = _ZxAnMcastViewSchedObjectId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 3),
    _ZxAnMcastViewSchedObjectId_Type()
)
zxAnMcastViewSchedObjectId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedObjectId.setStatus("current")


class _ZxAnMcastViewSchedType_Type(Integer32):
    """Custom type zxAnMcastViewSchedType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onlyOnce", 1),
          ("eachDay", 2))
    )


_ZxAnMcastViewSchedType_Type.__name__ = "Integer32"
_ZxAnMcastViewSchedType_Object = MibTableColumn
zxAnMcastViewSchedType = _ZxAnMcastViewSchedType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 4),
    _ZxAnMcastViewSchedType_Type()
)
zxAnMcastViewSchedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedType.setStatus("current")
_ZxAnMcastViewSchedStartDate_Type = Integer32
_ZxAnMcastViewSchedStartDate_Object = MibTableColumn
zxAnMcastViewSchedStartDate = _ZxAnMcastViewSchedStartDate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 5),
    _ZxAnMcastViewSchedStartDate_Type()
)
zxAnMcastViewSchedStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedStartDate.setStatus("current")
_ZxAnMcastViewSchedStartTime_Type = Integer32
_ZxAnMcastViewSchedStartTime_Object = MibTableColumn
zxAnMcastViewSchedStartTime = _ZxAnMcastViewSchedStartTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 6),
    _ZxAnMcastViewSchedStartTime_Type()
)
zxAnMcastViewSchedStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedStartTime.setStatus("current")
_ZxAnMcastViewSchedEndDate_Type = Integer32
_ZxAnMcastViewSchedEndDate_Object = MibTableColumn
zxAnMcastViewSchedEndDate = _ZxAnMcastViewSchedEndDate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 7),
    _ZxAnMcastViewSchedEndDate_Type()
)
zxAnMcastViewSchedEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedEndDate.setStatus("current")
_ZxAnMcastViewSchedEndTime_Type = Integer32
_ZxAnMcastViewSchedEndTime_Object = MibTableColumn
zxAnMcastViewSchedEndTime = _ZxAnMcastViewSchedEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 8),
    _ZxAnMcastViewSchedEndTime_Type()
)
zxAnMcastViewSchedEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedEndTime.setStatus("current")


class _ZxAnMcastViewSchedOperStatus_Type(Integer32):
    """Custom type zxAnMcastViewSchedOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("inService", 2),
          ("expired", 3))
    )


_ZxAnMcastViewSchedOperStatus_Type.__name__ = "Integer32"
_ZxAnMcastViewSchedOperStatus_Object = MibTableColumn
zxAnMcastViewSchedOperStatus = _ZxAnMcastViewSchedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 9),
    _ZxAnMcastViewSchedOperStatus_Type()
)
zxAnMcastViewSchedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedOperStatus.setStatus("current")


class _ZxAnMcastViewSchedDescr_Type(DisplayString):
    """Custom type zxAnMcastViewSchedDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnMcastViewSchedDescr_Type.__name__ = "DisplayString"
_ZxAnMcastViewSchedDescr_Object = MibTableColumn
zxAnMcastViewSchedDescr = _ZxAnMcastViewSchedDescr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 10),
    _ZxAnMcastViewSchedDescr_Type()
)
zxAnMcastViewSchedDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedDescr.setStatus("current")
_ZxAnMcastViewSchedRowStatus_Type = RowStatus
_ZxAnMcastViewSchedRowStatus_Object = MibTableColumn
zxAnMcastViewSchedRowStatus = _ZxAnMcastViewSchedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 2, 20, 10, 1, 11),
    _ZxAnMcastViewSchedRowStatus_Type()
)
zxAnMcastViewSchedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastViewSchedRowStatus.setStatus("current")
_ZxAnCtrlMcastCdr_ObjectIdentity = ObjectIdentity
zxAnCtrlMcastCdr = _ZxAnCtrlMcastCdr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3)
)


class _ZxAnIptvCdrEnable_Type(Integer32):
    """Custom type zxAnIptvCdrEnable based on Integer32"""
    defaultValue = 2

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


_ZxAnIptvCdrEnable_Type.__name__ = "Integer32"
_ZxAnIptvCdrEnable_Object = MibScalar
zxAnIptvCdrEnable = _ZxAnIptvCdrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 1),
    _ZxAnIptvCdrEnable_Type()
)
zxAnIptvCdrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvCdrEnable.setStatus("current")


class _ZxAnIptvCdrManualSendAction_Type(Integer32):
    """Custom type zxAnIptvCdrManualSendAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sendCdrToServer", 1)
    )


_ZxAnIptvCdrManualSendAction_Type.__name__ = "Integer32"
_ZxAnIptvCdrManualSendAction_Object = MibScalar
zxAnIptvCdrManualSendAction = _ZxAnIptvCdrManualSendAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 2),
    _ZxAnIptvCdrManualSendAction_Type()
)
zxAnIptvCdrManualSendAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvCdrManualSendAction.setStatus("current")
_ZxAnMcastCdrServerIP_Type = IpAddress
_ZxAnMcastCdrServerIP_Object = MibScalar
zxAnMcastCdrServerIP = _ZxAnMcastCdrServerIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 3),
    _ZxAnMcastCdrServerIP_Type()
)
zxAnMcastCdrServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerIP.setStatus("current")


class _ZxAnIptvCdrAutoSendPeriod_Type(Integer32):
    """Custom type zxAnIptvCdrAutoSendPeriod based on Integer32"""
    defaultValue = 240


_ZxAnIptvCdrAutoSendPeriod_Type.__name__ = "Integer32"
_ZxAnIptvCdrAutoSendPeriod_Object = MibScalar
zxAnIptvCdrAutoSendPeriod = _ZxAnIptvCdrAutoSendPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 4),
    _ZxAnIptvCdrAutoSendPeriod_Type()
)
zxAnIptvCdrAutoSendPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvCdrAutoSendPeriod.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIptvCdrAutoSendPeriod.setUnits("minute")


class _ZxAnIptvCdrGenerationMode_Type(Bits):
    """Custom type zxAnIptvCdrGenerationMode based on Bits"""
    namedValues = NamedValues(
        *(("loggingView", 0),
          ("loggingPreview", 1),
          ("loggingCountLimitOverPreview", 2),
          ("loggingDeny", 3))
    )

_ZxAnIptvCdrGenerationMode_Type.__name__ = "Bits"
_ZxAnIptvCdrGenerationMode_Object = MibScalar
zxAnIptvCdrGenerationMode = _ZxAnIptvCdrGenerationMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 5),
    _ZxAnIptvCdrGenerationMode_Type()
)
zxAnIptvCdrGenerationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvCdrGenerationMode.setStatus("current")


class _ZxAnIptvCdrMaxRecordNumer_Type(Integer32):
    """Custom type zxAnIptvCdrMaxRecordNumer based on Integer32"""
    defaultValue = 65535


_ZxAnIptvCdrMaxRecordNumer_Type.__name__ = "Integer32"
_ZxAnIptvCdrMaxRecordNumer_Object = MibScalar
zxAnIptvCdrMaxRecordNumer = _ZxAnIptvCdrMaxRecordNumer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 6),
    _ZxAnIptvCdrMaxRecordNumer_Type()
)
zxAnIptvCdrMaxRecordNumer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvCdrMaxRecordNumer.setStatus("current")
_ZxAnIptvCdrCurrentRecordNumber_Type = Integer32
_ZxAnIptvCdrCurrentRecordNumber_Object = MibScalar
zxAnIptvCdrCurrentRecordNumber = _ZxAnIptvCdrCurrentRecordNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 7),
    _ZxAnIptvCdrCurrentRecordNumber_Type()
)
zxAnIptvCdrCurrentRecordNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIptvCdrCurrentRecordNumber.setStatus("current")


class _ZxAnIptvCdrOnlineMsgGenPeriod_Type(Integer32):
    """Custom type zxAnIptvCdrOnlineMsgGenPeriod based on Integer32"""
    defaultValue = 60


_ZxAnIptvCdrOnlineMsgGenPeriod_Type.__name__ = "Integer32"
_ZxAnIptvCdrOnlineMsgGenPeriod_Object = MibScalar
zxAnIptvCdrOnlineMsgGenPeriod = _ZxAnIptvCdrOnlineMsgGenPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 8),
    _ZxAnIptvCdrOnlineMsgGenPeriod_Type()
)
zxAnIptvCdrOnlineMsgGenPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIptvCdrOnlineMsgGenPeriod.setStatus("current")
if mibBuilder.loadTexts:
    zxAnIptvCdrOnlineMsgGenPeriod.setUnits("minute")


class _ZxAnMcastCdrSizeThresh_Type(Integer32):
    """Custom type zxAnMcastCdrSizeThresh based on Integer32"""
    defaultValue = 0


_ZxAnMcastCdrSizeThresh_Type.__name__ = "Integer32"
_ZxAnMcastCdrSizeThresh_Object = MibScalar
zxAnMcastCdrSizeThresh = _ZxAnMcastCdrSizeThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 9),
    _ZxAnMcastCdrSizeThresh_Type()
)
zxAnMcastCdrSizeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastCdrSizeThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMcastCdrSizeThresh.setUnits("percent")
_ZxAnMcastIpv6CdrServerIP_Type = InetAddress
_ZxAnMcastIpv6CdrServerIP_Object = MibScalar
zxAnMcastIpv6CdrServerIP = _ZxAnMcastIpv6CdrServerIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 10),
    _ZxAnMcastIpv6CdrServerIP_Type()
)
zxAnMcastIpv6CdrServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastIpv6CdrServerIP.setStatus("current")


class _ZxAnMcastCdrRecognizeTime_Type(Integer32):
    """Custom type zxAnMcastCdrRecognizeTime based on Integer32"""
    defaultValue = 20


_ZxAnMcastCdrRecognizeTime_Type.__name__ = "Integer32"
_ZxAnMcastCdrRecognizeTime_Object = MibScalar
zxAnMcastCdrRecognizeTime = _ZxAnMcastCdrRecognizeTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 11),
    _ZxAnMcastCdrRecognizeTime_Type()
)
zxAnMcastCdrRecognizeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastCdrRecognizeTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMcastCdrRecognizeTime.setUnits("seconds")


class _ZxAnMcastCdrAutoSendSizeThresh_Type(Integer32):
    """Custom type zxAnMcastCdrAutoSendSizeThresh based on Integer32"""
    defaultValue = 2000


_ZxAnMcastCdrAutoSendSizeThresh_Type.__name__ = "Integer32"
_ZxAnMcastCdrAutoSendSizeThresh_Object = MibScalar
zxAnMcastCdrAutoSendSizeThresh = _ZxAnMcastCdrAutoSendSizeThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 12),
    _ZxAnMcastCdrAutoSendSizeThresh_Type()
)
zxAnMcastCdrAutoSendSizeThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMcastCdrAutoSendSizeThresh.setStatus("current")
_ZxAnMcastCdrServerTable_Object = MibTable
zxAnMcastCdrServerTable = _ZxAnMcastCdrServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50)
)
if mibBuilder.loadTexts:
    zxAnMcastCdrServerTable.setStatus("current")
_ZxAnMcastCdrServerEntry_Object = MibTableRow
zxAnMcastCdrServerEntry = _ZxAnMcastCdrServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1)
)
zxAnMcastCdrServerEntry.setIndexNames(
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnMcastCdrServerIpType"),
    (0, "ZTE-AN-CTRL-MULTICAST-MIB", "zxAnMcastCdrServerIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnMcastCdrServerEntry.setStatus("current")


class _ZxAnMcastCdrServerIpType_Type(InetAddressType):
    """Custom type zxAnMcastCdrServerIpType based on InetAddressType"""
    defaultValue = 1


_ZxAnMcastCdrServerIpType_Type.__name__ = "InetAddressType"
_ZxAnMcastCdrServerIpType_Object = MibTableColumn
zxAnMcastCdrServerIpType = _ZxAnMcastCdrServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 1),
    _ZxAnMcastCdrServerIpType_Type()
)
zxAnMcastCdrServerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerIpType.setStatus("current")


class _ZxAnMcastCdrServerIpAddr_Type(InetAddress):
    """Custom type zxAnMcastCdrServerIpAddr based on InetAddress"""
    defaultHexValue = ""


_ZxAnMcastCdrServerIpAddr_Type.__name__ = "InetAddress"
_ZxAnMcastCdrServerIpAddr_Object = MibTableColumn
zxAnMcastCdrServerIpAddr = _ZxAnMcastCdrServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 2),
    _ZxAnMcastCdrServerIpAddr_Type()
)
zxAnMcastCdrServerIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerIpAddr.setStatus("current")


class _ZxAnMcastCdrServerType_Type(Integer32):
    """Custom type zxAnMcastCdrServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ZxAnMcastCdrServerType_Type.__name__ = "Integer32"
_ZxAnMcastCdrServerType_Object = MibTableColumn
zxAnMcastCdrServerType = _ZxAnMcastCdrServerType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 3),
    _ZxAnMcastCdrServerType_Type()
)
zxAnMcastCdrServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerType.setStatus("current")


class _ZxAnMcastCdrServerUserName_Type(DisplayString):
    """Custom type zxAnMcastCdrServerUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnMcastCdrServerUserName_Type.__name__ = "DisplayString"
_ZxAnMcastCdrServerUserName_Object = MibTableColumn
zxAnMcastCdrServerUserName = _ZxAnMcastCdrServerUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 4),
    _ZxAnMcastCdrServerUserName_Type()
)
zxAnMcastCdrServerUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerUserName.setStatus("current")


class _ZxAnMcastCdrServerUserPwd_Type(DisplayString):
    """Custom type zxAnMcastCdrServerUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnMcastCdrServerUserPwd_Type.__name__ = "DisplayString"
_ZxAnMcastCdrServerUserPwd_Object = MibTableColumn
zxAnMcastCdrServerUserPwd = _ZxAnMcastCdrServerUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 5),
    _ZxAnMcastCdrServerUserPwd_Type()
)
zxAnMcastCdrServerUserPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerUserPwd.setStatus("current")


class _ZxAnMcastCdrServerFtpType_Type(Integer32):
    """Custom type zxAnMcastCdrServerFtpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_ZxAnMcastCdrServerFtpType_Type.__name__ = "Integer32"
_ZxAnMcastCdrServerFtpType_Object = MibTableColumn
zxAnMcastCdrServerFtpType = _ZxAnMcastCdrServerFtpType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 6),
    _ZxAnMcastCdrServerFtpType_Type()
)
zxAnMcastCdrServerFtpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerFtpType.setStatus("current")
_ZxAnMcastCdrServerRowStatus_Type = RowStatus
_ZxAnMcastCdrServerRowStatus_Object = MibTableColumn
zxAnMcastCdrServerRowStatus = _ZxAnMcastCdrServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 1, 3, 50, 1, 50),
    _ZxAnMcastCdrServerRowStatus_Type()
)
zxAnMcastCdrServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMcastCdrServerRowStatus.setStatus("current")
_ZxAnCtrlMulticastTrapObjects_ObjectIdentity = ObjectIdentity
zxAnCtrlMulticastTrapObjects = _ZxAnCtrlMulticastTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 2)
)
_ZxAnCtrlMcastTraps_ObjectIdentity = ObjectIdentity
zxAnCtrlMcastTraps = _ZxAnCtrlMcastTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 2, 2)
)

# Managed Objects groups


# Notification objects

zxAnCtrlMcastCdrSizeOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 2, 2, 1)
)
zxAnCtrlMcastCdrSizeOverThreshTrap.setObjects(
    ("ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvCdrCurrentRecordNumber")
)
if mibBuilder.loadTexts:
    zxAnCtrlMcastCdrSizeOverThreshTrap.setStatus(
        "current"
    )

zxAnCtrlMcastCdrSizeUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 2, 2, 2)
)
zxAnCtrlMcastCdrSizeUnderThreshTrap.setObjects(
    ("ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvCdrCurrentRecordNumber")
)
if mibBuilder.loadTexts:
    zxAnCtrlMcastCdrSizeUnderThreshTrap.setStatus(
        "current"
    )

zxAnMcastChanAccessDenyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 30, 2, 2, 3)
)
zxAnMcastChanAccessDenyTrap.setObjects(
      *(("ZTE-AN-CTRL-MULTICAST-MIB", "ifIndex"),
        ("ZTE-AN-CTRL-MULTICAST-MIB", "zxAnIptvChanNewName"))
)
if mibBuilder.loadTexts:
    zxAnMcastChanAccessDenyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-CTRL-MULTICAST-MIB",
    **{"zxAnCtrlMulticastMib": zxAnCtrlMulticastMib,
       "zxAnCtrlMulticastObjects": zxAnCtrlMulticastObjects,
       "zxAnCtrlMcastSysMgmt": zxAnCtrlMcastSysMgmt,
       "zxAnIptvAccessControlEnable": zxAnIptvAccessControlEnable,
       "zxAnCtrlMcastBandwidthCtrl": zxAnCtrlMcastBandwidthCtrl,
       "zxAnCtrlMcastCapabilities": zxAnCtrlMcastCapabilities,
       "zxAnCtrlMcastConfInitMgmt": zxAnCtrlMcastConfInitMgmt,
       "zxAnCtrlMcastConfInitSmsIp": zxAnCtrlMcastConfInitSmsIp,
       "zxAnCtrlMcastConfIpv6InitSms": zxAnCtrlMcastConfIpv6InitSms,
       "zxAnCtrlMcastPrw": zxAnCtrlMcastPrw,
       "zxAnIptvPrwCounterReset": zxAnIptvPrwCounterReset,
       "zxAnIptvPrwCounterAutoResetTime": zxAnIptvPrwCounterAutoResetTime,
       "zxAnIptvPrwRecognizeTime": zxAnIptvPrwRecognizeTime,
       "zxAnIptvPrwEnable": zxAnIptvPrwEnable,
       "zxAnCtrlMcastAccessMgmt": zxAnCtrlMcastAccessMgmt,
       "zxAnMcastPortTable": zxAnMcastPortTable,
       "zxAnMcastPortEntry": zxAnMcastPortEntry,
       "zxAnMcastIfIndex": zxAnMcastIfIndex,
       "zxAnIptvIfConfAdminStatus": zxAnIptvIfConfAdminStatus,
       "zxAnIptvIfConfOperStatus": zxAnIptvIfConfOperStatus,
       "zxAnIptvIfConfAuthCtrlMode": zxAnIptvIfConfAuthCtrlMode,
       "zxAnIptvIfConfPkgIdList": zxAnIptvIfConfPkgIdList,
       "zxAnIptvIfConfWatchChanIdList": zxAnIptvIfConfWatchChanIdList,
       "zxAnIptvIfConfPrwChanIdList": zxAnIptvIfConfPrwChanIdList,
       "zxAnMcastPortMaxBandwidth": zxAnMcastPortMaxBandwidth,
       "zxAnMcastPortParamListCmdTable": zxAnMcastPortParamListCmdTable,
       "zxAnMcastPortParamListCmdEntry": zxAnMcastPortParamListCmdEntry,
       "zxAnMcastPortParamListCmd": zxAnMcastPortParamListCmd,
       "zxAnMcastPortIndex": zxAnMcastPortIndex,
       "zxAnMcastPortParamObjName": zxAnMcastPortParamObjName,
       "zxAnIptvNextChannelId": zxAnIptvNextChannelId,
       "zxAnMcastChannelTable": zxAnMcastChannelTable,
       "zxAnMcastChannelEntry": zxAnMcastChannelEntry,
       "zxAnIptvChanName": zxAnIptvChanName,
       "zxAnIptvMVid": zxAnIptvMVid,
       "zxAnMcastSrcIp": zxAnMcastSrcIp,
       "zxAnMcastGrpIp": zxAnMcastGrpIp,
       "zxAnIptvChanId": zxAnIptvChanId,
       "zxAnIptvChanPreviewProfile": zxAnIptvChanPreviewProfile,
       "zxAnIptvChanCdrEnable": zxAnIptvChanCdrEnable,
       "zxAnIptvChanNewName": zxAnIptvChanNewName,
       "zxAnIptvChanRowStatus": zxAnIptvChanRowStatus,
       "zxAnIMcastGroupBandwidthCost": zxAnIMcastGroupBandwidthCost,
       "zxAnMcastChannelAddressType": zxAnMcastChannelAddressType,
       "zxAnMcastSrcIpv6": zxAnMcastSrcIpv6,
       "zxAnMcastGrpIpv6": zxAnMcastGrpIpv6,
       "zxAnIptvNextPkgId": zxAnIptvNextPkgId,
       "zxAnMcastPkgTable": zxAnMcastPkgTable,
       "zxAnMcastPkgEntry": zxAnMcastPkgEntry,
       "zxAnIptvPkgName": zxAnIptvPkgName,
       "zxAnIptvPkgId": zxAnIptvPkgId,
       "zxAnIptvPkgDescription": zxAnIptvPkgDescription,
       "zxAnIptvPkgRowStatus": zxAnIptvPkgRowStatus,
       "zxAnIptvPkgStartTime": zxAnIptvPkgStartTime,
       "zxAnIptvPkgEndTime": zxAnIptvPkgEndTime,
       "zxAnMcastPkgChanTable": zxAnMcastPkgChanTable,
       "zxAnMcastPkgChanEntry": zxAnMcastPkgChanEntry,
       "zxAnIptvPkgChanAccessRight": zxAnIptvPkgChanAccessRight,
       "zxAnIptvPkgChanRowStatus": zxAnIptvPkgChanRowStatus,
       "zxAnMcastChanPortTable": zxAnMcastChanPortTable,
       "zxAnMcastChanPortEntry": zxAnMcastChanPortEntry,
       "zxAnIptvPkgPortListShelf": zxAnIptvPkgPortListShelf,
       "zxAnIptvPkgPortListSlot": zxAnIptvPkgPortListSlot,
       "zxAnIptvChanPortListWatch": zxAnIptvChanPortListWatch,
       "zxAnIptvChanPortListPreview": zxAnIptvChanPortListPreview,
       "zxAnMcastPkgPortTable": zxAnMcastPkgPortTable,
       "zxAnMcastPkgPortEntry": zxAnMcastPkgPortEntry,
       "zxAnIptvPkgPortList": zxAnIptvPkgPortList,
       "zxAnMcastViewConfProfileTable": zxAnMcastViewConfProfileTable,
       "zxAnMcastViewConfProfileEntry": zxAnMcastViewConfProfileEntry,
       "zxAnIptvPreviewProfileName": zxAnIptvPreviewProfileName,
       "zxAnIptvPreviewMaxCount": zxAnIptvPreviewMaxCount,
       "zxAnIptvPreviewMaxDuration": zxAnIptvPreviewMaxDuration,
       "zxAnIptvPreviewBlackoutInterval": zxAnIptvPreviewBlackoutInterval,
       "zxAnIptvPreviewProfileRowStatus": zxAnIptvPreviewProfileRowStatus,
       "zxAnIptvPreviewRecognizeTime": zxAnIptvPreviewRecognizeTime,
       "zxAnMcastViewSchedule": zxAnMcastViewSchedule,
       "zxAnMcastViewSchedObjRemoveMode": zxAnMcastViewSchedObjRemoveMode,
       "zxAnMcastViewSchedTable": zxAnMcastViewSchedTable,
       "zxAnMcastViewSchedEntry": zxAnMcastViewSchedEntry,
       "zxAnMcastViewSchedIndex": zxAnMcastViewSchedIndex,
       "zxAnMcastViewSchedObjectType": zxAnMcastViewSchedObjectType,
       "zxAnMcastViewSchedObjectId": zxAnMcastViewSchedObjectId,
       "zxAnMcastViewSchedType": zxAnMcastViewSchedType,
       "zxAnMcastViewSchedStartDate": zxAnMcastViewSchedStartDate,
       "zxAnMcastViewSchedStartTime": zxAnMcastViewSchedStartTime,
       "zxAnMcastViewSchedEndDate": zxAnMcastViewSchedEndDate,
       "zxAnMcastViewSchedEndTime": zxAnMcastViewSchedEndTime,
       "zxAnMcastViewSchedOperStatus": zxAnMcastViewSchedOperStatus,
       "zxAnMcastViewSchedDescr": zxAnMcastViewSchedDescr,
       "zxAnMcastViewSchedRowStatus": zxAnMcastViewSchedRowStatus,
       "zxAnCtrlMcastCdr": zxAnCtrlMcastCdr,
       "zxAnIptvCdrEnable": zxAnIptvCdrEnable,
       "zxAnIptvCdrManualSendAction": zxAnIptvCdrManualSendAction,
       "zxAnMcastCdrServerIP": zxAnMcastCdrServerIP,
       "zxAnIptvCdrAutoSendPeriod": zxAnIptvCdrAutoSendPeriod,
       "zxAnIptvCdrGenerationMode": zxAnIptvCdrGenerationMode,
       "zxAnIptvCdrMaxRecordNumer": zxAnIptvCdrMaxRecordNumer,
       "zxAnIptvCdrCurrentRecordNumber": zxAnIptvCdrCurrentRecordNumber,
       "zxAnIptvCdrOnlineMsgGenPeriod": zxAnIptvCdrOnlineMsgGenPeriod,
       "zxAnMcastCdrSizeThresh": zxAnMcastCdrSizeThresh,
       "zxAnMcastIpv6CdrServerIP": zxAnMcastIpv6CdrServerIP,
       "zxAnMcastCdrRecognizeTime": zxAnMcastCdrRecognizeTime,
       "zxAnMcastCdrAutoSendSizeThresh": zxAnMcastCdrAutoSendSizeThresh,
       "zxAnMcastCdrServerTable": zxAnMcastCdrServerTable,
       "zxAnMcastCdrServerEntry": zxAnMcastCdrServerEntry,
       "zxAnMcastCdrServerIpType": zxAnMcastCdrServerIpType,
       "zxAnMcastCdrServerIpAddr": zxAnMcastCdrServerIpAddr,
       "zxAnMcastCdrServerType": zxAnMcastCdrServerType,
       "zxAnMcastCdrServerUserName": zxAnMcastCdrServerUserName,
       "zxAnMcastCdrServerUserPwd": zxAnMcastCdrServerUserPwd,
       "zxAnMcastCdrServerFtpType": zxAnMcastCdrServerFtpType,
       "zxAnMcastCdrServerRowStatus": zxAnMcastCdrServerRowStatus,
       "zxAnCtrlMulticastTrapObjects": zxAnCtrlMulticastTrapObjects,
       "zxAnCtrlMcastTraps": zxAnCtrlMcastTraps,
       "zxAnCtrlMcastCdrSizeOverThreshTrap": zxAnCtrlMcastCdrSizeOverThreshTrap,
       "zxAnCtrlMcastCdrSizeUnderThreshTrap": zxAnCtrlMcastCdrSizeUnderThreshTrap,
       "zxAnMcastChanAccessDenyTrap": zxAnMcastChanAccessDenyTrap}
)
