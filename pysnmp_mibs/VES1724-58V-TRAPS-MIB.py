# SNMP MIB module (VES1724-58V-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/VES1724-58V-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:38 2025
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

(ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(coaConfAnalyticMethod,
 coaConfIssueThreshold,
 dslPmCurr15minRxBroadcastPkts,
 dslPmCurr15minRxDiscardPkts,
 dslPmCurr15minRxMulticastPkts,
 dslPmCurr15minRxOctets,
 dslPmCurr15minRxPkts,
 dslPmCurr15minRxUnicastPkts,
 dslPmCurr15minTxBroadcastPkts,
 dslPmCurr15minTxDiscardPkts,
 dslPmCurr15minTxMulticastPkts,
 dslPmCurr15minTxOctets,
 dslPmCurr15minTxPkts,
 dslPmCurr15minTxUnicastPkts,
 dslPmThreshProfRxBroadcastPkts,
 dslPmThreshProfRxDiscardPkts,
 dslPmThreshProfRxMulticastPkts,
 dslPmThreshProfRxOctets,
 dslPmThreshProfRxPkts,
 dslPmThreshProfRxUnicastPkts,
 dslPmThreshProfTxBroadcastPkts,
 dslPmThreshProfTxDiscardPkts,
 dslPmThreshProfTxMulticastPkts,
 dslPmThreshProfTxOctets,
 dslPmThreshProfTxPkts,
 dslPmThreshProfTxUnicastPkts,
 externalAlarmName,
 externalBatteryConfDcCriticThreshold,
 externalBatteryConfDcErrThreshold,
 externalBatteryConfDcLowThreshold,
 externalBatteryConfTempHighThreshold,
 externalBatteryConfTempLowThreshold,
 externalBatteryStatsTemperature,
 externalBatteryStatsVoltage,
 fanConfHighThreshold,
 fanConfIndex,
 fanConfLowThreshold,
 fanRpmCurValue,
 fxsPmCurr15minRtpElapsedTime,
 fxsPmCurr15minRtpRxBytes,
 fxsPmCurr15minRtpRxLostPackets,
 fxsPmCurr15minRtpRxPackets,
 fxsPmCurr15minRtpTxBytes,
 fxsPmCurr15minRtpTxLostPackets,
 fxsPmCurr15minRtpTxPackets,
 fxsPmThreshProfRtpElapsedTime,
 fxsPmThreshProfRtpRxBytes,
 fxsPmThreshProfRtpRxLostPackets,
 fxsPmThreshProfRtpRxPackets,
 fxsPmThreshProfRtpTxBytes,
 fxsPmThreshProfRtpTxLostPackets,
 fxsPmThreshProfRtpTxPackets,
 gePmCurr15minCollisions,
 gePmCurr15minPkts1024to1518Octets,
 gePmCurr15minPkts128to255Octets,
 gePmCurr15minPkts1519to1522Octets,
 gePmCurr15minPkts256to511Octets,
 gePmCurr15minPkts512to1023Octets,
 gePmCurr15minPkts64Octets,
 gePmCurr15minPkts65to127Octets,
 gePmCurr15minRxBroadcastPkts,
 gePmCurr15minRxCRCAlignErrors,
 gePmCurr15minRxFragments,
 gePmCurr15minRxMulticastPkts,
 gePmCurr15minRxOctets,
 gePmCurr15minRxOversizePkts,
 gePmCurr15minRxPkts,
 gePmCurr15minRxUndersizePkts,
 gePmCurr15minTxBroadcastPkts,
 gePmCurr15minTxMulticastPkts,
 gePmCurr15minTxOctets,
 gePmCurr15minTxPkts,
 gePmThreshProfCollisions,
 gePmThreshProfPkts1024to1518Octets,
 gePmThreshProfPkts128to255Octets,
 gePmThreshProfPkts1519to1522Octets,
 gePmThreshProfPkts256to511Octets,
 gePmThreshProfPkts512to1023Octets,
 gePmThreshProfPkts64Octets,
 gePmThreshProfPkts65to127Octets,
 gePmThreshProfRxBroadcastPkts,
 gePmThreshProfRxCRCAlignErrors,
 gePmThreshProfRxFragments,
 gePmThreshProfRxMulticastPkts,
 gePmThreshProfRxOctets,
 gePmThreshProfRxOversizePkts,
 gePmThreshProfRxPkts,
 gePmThreshProfRxUndersizePkts,
 gePmThreshProfTxBroadcastPkts,
 gePmThreshProfTxMulticastPkts,
 gePmThreshProfTxOctets,
 gePmThreshProfTxPkts,
 geUtilRxCurrentPercent,
 geUtilRxIssueLvl1Threshold,
 geUtilRxIssueLvl2Threshold,
 geUtilTxCurrentPercent,
 geUtilTxIssueLvl1Threshold,
 geUtilTxIssueLvl2Threshold,
 h248MgcIpDn,
 sipProfileRegSvr,
 slotModuleIdVes1724_58v,
 sysPmSyncStatus,
 sysPmSyncUrl,
 temperatureConfHighThreshold,
 temperatureConfIndex,
 temperatureConfLowThreshold,
 temperatureCurValue,
 vdsl2LineAlarmConfProfileXtucThresh15MinLofs,
 vdsl2LineAlarmConfProfileXturThresh15MinLofs,
 vdsl2LineAlarmConfProfileXturThresh15MinLprs,
 ves1724_58v,
 voltageConfHighThreshold,
 voltageConfIndex,
 voltageConfLowThreshold,
 voltageCurValue,
 xdsl2PMLCurr15MLofs,
 xdsl2PMLInitCurr15MLprs,
 xdslBondingStatusName,
 xdslBondingStatusTransferMode) = mibBuilder.importSymbols(
    "VES1724-58V-MIB",
    "coaConfAnalyticMethod",
    "coaConfIssueThreshold",
    "dslPmCurr15minRxBroadcastPkts",
    "dslPmCurr15minRxDiscardPkts",
    "dslPmCurr15minRxMulticastPkts",
    "dslPmCurr15minRxOctets",
    "dslPmCurr15minRxPkts",
    "dslPmCurr15minRxUnicastPkts",
    "dslPmCurr15minTxBroadcastPkts",
    "dslPmCurr15minTxDiscardPkts",
    "dslPmCurr15minTxMulticastPkts",
    "dslPmCurr15minTxOctets",
    "dslPmCurr15minTxPkts",
    "dslPmCurr15minTxUnicastPkts",
    "dslPmThreshProfRxBroadcastPkts",
    "dslPmThreshProfRxDiscardPkts",
    "dslPmThreshProfRxMulticastPkts",
    "dslPmThreshProfRxOctets",
    "dslPmThreshProfRxPkts",
    "dslPmThreshProfRxUnicastPkts",
    "dslPmThreshProfTxBroadcastPkts",
    "dslPmThreshProfTxDiscardPkts",
    "dslPmThreshProfTxMulticastPkts",
    "dslPmThreshProfTxOctets",
    "dslPmThreshProfTxPkts",
    "dslPmThreshProfTxUnicastPkts",
    "externalAlarmName",
    "externalBatteryConfDcCriticThreshold",
    "externalBatteryConfDcErrThreshold",
    "externalBatteryConfDcLowThreshold",
    "externalBatteryConfTempHighThreshold",
    "externalBatteryConfTempLowThreshold",
    "externalBatteryStatsTemperature",
    "externalBatteryStatsVoltage",
    "fanConfHighThreshold",
    "fanConfIndex",
    "fanConfLowThreshold",
    "fanRpmCurValue",
    "fxsPmCurr15minRtpElapsedTime",
    "fxsPmCurr15minRtpRxBytes",
    "fxsPmCurr15minRtpRxLostPackets",
    "fxsPmCurr15minRtpRxPackets",
    "fxsPmCurr15minRtpTxBytes",
    "fxsPmCurr15minRtpTxLostPackets",
    "fxsPmCurr15minRtpTxPackets",
    "fxsPmThreshProfRtpElapsedTime",
    "fxsPmThreshProfRtpRxBytes",
    "fxsPmThreshProfRtpRxLostPackets",
    "fxsPmThreshProfRtpRxPackets",
    "fxsPmThreshProfRtpTxBytes",
    "fxsPmThreshProfRtpTxLostPackets",
    "fxsPmThreshProfRtpTxPackets",
    "gePmCurr15minCollisions",
    "gePmCurr15minPkts1024to1518Octets",
    "gePmCurr15minPkts128to255Octets",
    "gePmCurr15minPkts1519to1522Octets",
    "gePmCurr15minPkts256to511Octets",
    "gePmCurr15minPkts512to1023Octets",
    "gePmCurr15minPkts64Octets",
    "gePmCurr15minPkts65to127Octets",
    "gePmCurr15minRxBroadcastPkts",
    "gePmCurr15minRxCRCAlignErrors",
    "gePmCurr15minRxFragments",
    "gePmCurr15minRxMulticastPkts",
    "gePmCurr15minRxOctets",
    "gePmCurr15minRxOversizePkts",
    "gePmCurr15minRxPkts",
    "gePmCurr15minRxUndersizePkts",
    "gePmCurr15minTxBroadcastPkts",
    "gePmCurr15minTxMulticastPkts",
    "gePmCurr15minTxOctets",
    "gePmCurr15minTxPkts",
    "gePmThreshProfCollisions",
    "gePmThreshProfPkts1024to1518Octets",
    "gePmThreshProfPkts128to255Octets",
    "gePmThreshProfPkts1519to1522Octets",
    "gePmThreshProfPkts256to511Octets",
    "gePmThreshProfPkts512to1023Octets",
    "gePmThreshProfPkts64Octets",
    "gePmThreshProfPkts65to127Octets",
    "gePmThreshProfRxBroadcastPkts",
    "gePmThreshProfRxCRCAlignErrors",
    "gePmThreshProfRxFragments",
    "gePmThreshProfRxMulticastPkts",
    "gePmThreshProfRxOctets",
    "gePmThreshProfRxOversizePkts",
    "gePmThreshProfRxPkts",
    "gePmThreshProfRxUndersizePkts",
    "gePmThreshProfTxBroadcastPkts",
    "gePmThreshProfTxMulticastPkts",
    "gePmThreshProfTxOctets",
    "gePmThreshProfTxPkts",
    "geUtilRxCurrentPercent",
    "geUtilRxIssueLvl1Threshold",
    "geUtilRxIssueLvl2Threshold",
    "geUtilTxCurrentPercent",
    "geUtilTxIssueLvl1Threshold",
    "geUtilTxIssueLvl2Threshold",
    "h248MgcIpDn",
    "sipProfileRegSvr",
    "slotModuleIdVes1724-58v",
    "sysPmSyncStatus",
    "sysPmSyncUrl",
    "temperatureConfHighThreshold",
    "temperatureConfIndex",
    "temperatureConfLowThreshold",
    "temperatureCurValue",
    "vdsl2LineAlarmConfProfileXtucThresh15MinLofs",
    "vdsl2LineAlarmConfProfileXturThresh15MinLofs",
    "vdsl2LineAlarmConfProfileXturThresh15MinLprs",
    "ves1724-58v",
    "voltageConfHighThreshold",
    "voltageConfIndex",
    "voltageConfLowThreshold",
    "voltageCurValue",
    "xdsl2PMLCurr15MLofs",
    "xdsl2PMLInitCurr15MLprs",
    "xdslBondingStatusName",
    "xdslBondingStatusTransferMode")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19)
)
_Object_ObjectIdentity = ObjectIdentity
object = _Object_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1)
)
_DslLgSenderIfIndex_Type = Integer32
_DslLgSenderIfIndex_Object = MibScalar
dslLgSenderIfIndex = _DslLgSenderIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 1),
    _DslLgSenderIfIndex_Type()
)
dslLgSenderIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dslLgSenderIfIndex.setStatus("current")
_SysProblemCause_Type = DisplayString
_SysProblemCause_Object = MibScalar
sysProblemCause = _SysProblemCause_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 2),
    _SysProblemCause_Type()
)
sysProblemCause.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysProblemCause.setStatus("current")
_SysMacAntiSpoofOrig_Type = Integer32
_SysMacAntiSpoofOrig_Object = MibScalar
sysMacAntiSpoofOrig = _SysMacAntiSpoofOrig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 3),
    _SysMacAntiSpoofOrig_Type()
)
sysMacAntiSpoofOrig.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysMacAntiSpoofOrig.setStatus("current")
_SysMacAntiSpoofNew_Type = Integer32
_SysMacAntiSpoofNew_Object = MibScalar
sysMacAntiSpoofNew = _SysMacAntiSpoofNew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 4),
    _SysMacAntiSpoofNew_Type()
)
sysMacAntiSpoofNew.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysMacAntiSpoofNew.setStatus("current")
_SysMacAntiSpoofMAC_Type = DisplayString
_SysMacAntiSpoofMAC_Object = MibScalar
sysMacAntiSpoofMAC = _SysMacAntiSpoofMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 5),
    _SysMacAntiSpoofMAC_Type()
)
sysMacAntiSpoofMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysMacAntiSpoofMAC.setStatus("current")
_SysCoaIssuedLoad_Type = Unsigned32
_SysCoaIssuedLoad_Object = MibScalar
sysCoaIssuedLoad = _SysCoaIssuedLoad_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 6),
    _SysCoaIssuedLoad_Type()
)
sysCoaIssuedLoad.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysCoaIssuedLoad.setStatus("current")
_VoipDevId_Type = Integer32
_VoipDevId_Object = MibScalar
voipDevId = _VoipDevId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 7),
    _VoipDevId_Type()
)
voipDevId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipDevId.setStatus("current")
_VoipCount_Type = Integer32
_VoipCount_Object = MibScalar
voipCount = _VoipCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 8),
    _VoipCount_Type()
)
voipCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipCount.setStatus("current")


class _VoipPhoneState_Type(Integer32):
    """Custom type voipPhoneState based on Integer32"""
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
        *(("disable", 1),
          ("onHook", 2),
          ("offHook", 3),
          ("ringing", 4),
          ("testing", 5),
          ("powerCutDown", 6),
          ("fault", 7),
          ("bad", 8),
          ("uninitialized", 9))
    )


_VoipPhoneState_Type.__name__ = "Integer32"
_VoipPhoneState_Object = MibScalar
voipPhoneState = _VoipPhoneState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 9),
    _VoipPhoneState_Type()
)
voipPhoneState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipPhoneState.setStatus("current")


class _VoipBatType_Type(Integer32):
    """Custom type voipBatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("batteryLow", 0),
          ("batteryHigh", 1),
          ("batteryPositive", 2))
    )


_VoipBatType_Type.__name__ = "Integer32"
_VoipBatType_Object = MibScalar
voipBatType = _VoipBatType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 10),
    _VoipBatType_Type()
)
voipBatType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipBatType.setStatus("current")
_VoipRingSegment_Type = Unsigned32
_VoipRingSegment_Object = MibScalar
voipRingSegment = _VoipRingSegment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 11),
    _VoipRingSegment_Type()
)
voipRingSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipRingSegment.setStatus("current")
_VoipRingTimerId_Type = Unsigned32
_VoipRingTimerId_Object = MibScalar
voipRingTimerId = _VoipRingTimerId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 12),
    _VoipRingTimerId_Type()
)
voipRingTimerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipRingTimerId.setStatus("current")
_XdslDevId_Type = Integer32
_XdslDevId_Object = MibScalar
xdslDevId = _XdslDevId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 13),
    _XdslDevId_Type()
)
xdslDevId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdslDevId.setStatus("current")


class _VoipCodecType_Type(Integer32):
    """Custom type voipCodecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("g711", 0),
          ("g711mu", 1),
          ("g723", 2),
          ("g726x16", 3),
          ("g726x24", 4),
          ("g726x32", 5),
          ("g726x40", 6),
          ("g729ab", 7))
    )


_VoipCodecType_Type.__name__ = "Integer32"
_VoipCodecType_Object = MibScalar
voipCodecType = _VoipCodecType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 14),
    _VoipCodecType_Type()
)
voipCodecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipCodecType.setStatus("current")


class _VoipOpType_Type(Integer32):
    """Custom type voipOpType based on Integer32"""
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
        *(("offHookShort", 0),
          ("offHookLong", 1),
          ("ringing", 2),
          ("cardInsert", 3))
    )


_VoipOpType_Type.__name__ = "Integer32"
_VoipOpType_Object = MibScalar
voipOpType = _VoipOpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 15),
    _VoipOpType_Type()
)
voipOpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipOpType.setStatus("current")
_VoipPwrExceedCounter_Type = Integer32
_VoipPwrExceedCounter_Object = MibScalar
voipPwrExceedCounter = _VoipPwrExceedCounter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 17),
    _VoipPwrExceedCounter_Type()
)
voipPwrExceedCounter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipPwrExceedCounter.setStatus("current")
_VoipVtipVoltage_Type = Integer32
_VoipVtipVoltage_Object = MibScalar
voipVtipVoltage = _VoipVtipVoltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 30),
    _VoipVtipVoltage_Type()
)
voipVtipVoltage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipVtipVoltage.setStatus("current")
_VoipVringVoltage_Type = Integer32
_VoipVringVoltage_Object = MibScalar
voipVringVoltage = _VoipVringVoltage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 1, 31),
    _VoipVringVoltage_Type()
)
voipVringVoltage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voipVringVoltage.setStatus("current")
_Dsltrap_ObjectIdentity = ObjectIdentity
dsltrap = _Dsltrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2)
)
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3)
)
_Systrap_ObjectIdentity = ObjectIdentity
systrap = _Systrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4)
)
_Getrap_ObjectIdentity = ObjectIdentity
getrap = _Getrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5)
)
_Voiptrap_ObjectIdentity = ObjectIdentity
voiptrap = _Voiptrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6)
)
_Fxstrap_ObjectIdentity = ObjectIdentity
fxstrap = _Fxstrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7)
)

# Managed Objects groups


# Notification objects

dslLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 1)
)
dslLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    dslLinkDown.setStatus(
        "current"
    )

dslLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 2)
)
dslLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    dslLinkUp.setStatus(
        "current"
    )

xdslXtucLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 3)
)
xdslXtucLof.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXtucLof.setStatus(
        "current"
    )

xdslXtucLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 4)
)
xdslXtucLos.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXtucLos.setStatus(
        "current"
    )

xdslXturLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 5)
)
xdslXturLof.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXturLof.setStatus(
        "current"
    )

xdslXturLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 6)
)
xdslXturLos.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXturLos.setStatus(
        "current"
    )

xdslXturLpr = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 7)
)
xdslXturLpr.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXturLpr.setStatus(
        "current"
    )

xdslXtucLofClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 8)
)
xdslXtucLofClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXtucLofClear.setStatus(
        "current"
    )

xdslXtucLosClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 9)
)
xdslXtucLosClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXtucLosClear.setStatus(
        "current"
    )

xdslXturLofClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 10)
)
xdslXturLofClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXturLofClear.setStatus(
        "current"
    )

xdslXturLosClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 11)
)
xdslXturLosClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXturLosClear.setStatus(
        "current"
    )

xdslXturLprClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 12)
)
xdslXturLprClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslXturLprClear.setStatus(
        "current"
    )

xdslLoopguard = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 13)
)
xdslLoopguard.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "dslLgSenderIfIndex"))
)
if mibBuilder.loadTexts:
    xdslLoopguard.setStatus(
        "current"
    )

xdslLoopguardClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 14)
)
xdslLoopguardClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "dslLgSenderIfIndex"))
)
if mibBuilder.loadTexts:
    xdslLoopguardClear.setStatus(
        "current"
    )

xdslDspDownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 15)
)
xdslDspDownloadFail.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "xdslDevId"))
)
if mibBuilder.loadTexts:
    xdslDspDownloadFail.setStatus(
        "current"
    )

xdslDspDownloadFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 16)
)
xdslDspDownloadFailClear.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "xdslDevId"))
)
if mibBuilder.loadTexts:
    xdslDspDownloadFailClear.setStatus(
        "current"
    )

xdslDspInoperable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 17)
)
xdslDspInoperable.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "xdslDevId"))
)
if mibBuilder.loadTexts:
    xdslDspInoperable.setStatus(
        "current"
    )

xdslHtPortPolicer = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 18)
)
xdslHtPortPolicer.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    xdslHtPortPolicer.setStatus(
        "current"
    )

xdslLinePerfLOFSThreshXtuc = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 19)
)
xdslLinePerfLOFSThreshXtuc.setObjects(
      *(("VES1724-58V-MIB", "xdsl2PMLCurr15MLofs"),
        ("VES1724-58V-MIB", "vdsl2LineAlarmConfProfileXtucThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    xdslLinePerfLOFSThreshXtuc.setStatus(
        "current"
    )

xdslLinePerfLOFSThreshXtur = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 20)
)
xdslLinePerfLOFSThreshXtur.setObjects(
      *(("VES1724-58V-MIB", "xdsl2PMLCurr15MLofs"),
        ("VES1724-58V-MIB", "vdsl2LineAlarmConfProfileXturThresh15MinLofs"))
)
if mibBuilder.loadTexts:
    xdslLinePerfLOFSThreshXtur.setStatus(
        "current"
    )

xdslLinePerfLPRSThreshXtur = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 21)
)
xdslLinePerfLPRSThreshXtur.setObjects(
      *(("VES1724-58V-MIB", "xdsl2PMLInitCurr15MLprs"),
        ("VES1724-58V-MIB", "vdsl2LineAlarmConfProfileXturThresh15MinLprs"))
)
if mibBuilder.loadTexts:
    xdslLinePerfLPRSThreshXtur.setStatus(
        "current"
    )

xdslPmTrapTxOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 22)
)
xdslPmTrapTxOctets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minTxOctets"),
        ("VES1724-58V-MIB", "dslPmThreshProfTxOctets"))
)
if mibBuilder.loadTexts:
    xdslPmTrapTxOctets.setStatus(
        "current"
    )

xdslPmTrapTxPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 23)
)
xdslPmTrapTxPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minTxPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfTxPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapTxPkts.setStatus(
        "current"
    )

xdslPmTrapTxUnicastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 24)
)
xdslPmTrapTxUnicastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minTxUnicastPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfTxUnicastPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapTxUnicastPkts.setStatus(
        "current"
    )

xdslPmTrapTxBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 25)
)
xdslPmTrapTxBroadcastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minTxBroadcastPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfTxBroadcastPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapTxBroadcastPkts.setStatus(
        "current"
    )

xdslPmTrapTxMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 26)
)
xdslPmTrapTxMulticastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minTxMulticastPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfTxMulticastPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapTxMulticastPkts.setStatus(
        "current"
    )

xdslPmTrapTxDiscardPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 27)
)
xdslPmTrapTxDiscardPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minTxDiscardPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfTxDiscardPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapTxDiscardPkts.setStatus(
        "current"
    )

xdslPmTrapRxOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 28)
)
xdslPmTrapRxOctets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minRxOctets"),
        ("VES1724-58V-MIB", "dslPmThreshProfRxOctets"))
)
if mibBuilder.loadTexts:
    xdslPmTrapRxOctets.setStatus(
        "current"
    )

xdslPmTrapRxPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 29)
)
xdslPmTrapRxPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minRxPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfRxPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapRxPkts.setStatus(
        "current"
    )

xdslPmTrapRxUnicastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 30)
)
xdslPmTrapRxUnicastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minRxUnicastPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfRxUnicastPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapRxUnicastPkts.setStatus(
        "current"
    )

xdslPmTrapRxBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 31)
)
xdslPmTrapRxBroadcastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minRxBroadcastPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfRxBroadcastPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapRxBroadcastPkts.setStatus(
        "current"
    )

xdslPmTrapRxMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 32)
)
xdslPmTrapRxMulticastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minRxMulticastPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfRxMulticastPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapRxMulticastPkts.setStatus(
        "current"
    )

xdslPmTrapRxDiscardPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 33)
)
xdslPmTrapRxDiscardPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "dslPmCurr15minRxDiscardPkts"),
        ("VES1724-58V-MIB", "dslPmThreshProfRxDiscardPkts"))
)
if mibBuilder.loadTexts:
    xdslPmTrapRxDiscardPkts.setStatus(
        "current"
    )

xdslBondLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 34)
)
xdslBondLinkUp.setObjects(
      *(("VES1724-58V-MIB", "xdslBondingStatusName"),
        ("VES1724-58V-MIB", "xdslBondingStatusTransferMode"))
)
if mibBuilder.loadTexts:
    xdslBondLinkUp.setStatus(
        "current"
    )

xdslBondLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 35)
)
xdslBondLinkDown.setObjects(
      *(("VES1724-58V-MIB", "xdslBondingStatusName"),
        ("VES1724-58V-MIB", "xdslBondingStatusTransferMode"))
)
if mibBuilder.loadTexts:
    xdslBondLinkDown.setStatus(
        "current"
    )

xdslBondPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 36)
)
xdslBondPortLinkUp.setObjects(
      *(("VES1724-58V-MIB", "xdslBondingStatusName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    xdslBondPortLinkUp.setStatus(
        "current"
    )

xdslBondPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 2, 37)
)
xdslBondPortLinkDown.setObjects(
      *(("VES1724-58V-MIB", "xdslBondingStatusName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    xdslBondPortLinkDown.setStatus(
        "current"
    )

hwMonitorFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 1)
)
hwMonitorFail.setObjects(
    ("VES1724-58V-MIB", "slotModuleIdVes1724-58v")
)
if mibBuilder.loadTexts:
    hwMonitorFail.setStatus(
        "current"
    )

voltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 2)
)
voltageOutOfRange.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-MIB", "voltageConfIndex"),
        ("VES1724-58V-MIB", "voltageCurValue"),
        ("VES1724-58V-MIB", "voltageConfHighThreshold"),
        ("VES1724-58V-MIB", "voltageConfLowThreshold"))
)
if mibBuilder.loadTexts:
    voltageOutOfRange.setStatus(
        "current"
    )

voltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 3)
)
voltageNormal.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-MIB", "voltageConfIndex"),
        ("VES1724-58V-MIB", "voltageCurValue"),
        ("VES1724-58V-MIB", "voltageConfHighThreshold"),
        ("VES1724-58V-MIB", "voltageConfLowThreshold"))
)
if mibBuilder.loadTexts:
    voltageNormal.setStatus(
        "current"
    )

temperatureOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 4)
)
temperatureOutOfRange.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-MIB", "temperatureConfIndex"),
        ("VES1724-58V-MIB", "temperatureCurValue"),
        ("VES1724-58V-MIB", "temperatureConfHighThreshold"),
        ("VES1724-58V-MIB", "temperatureConfLowThreshold"))
)
if mibBuilder.loadTexts:
    temperatureOutOfRange.setStatus(
        "current"
    )

temperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 5)
)
temperatureNormal.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-MIB", "temperatureConfIndex"),
        ("VES1724-58V-MIB", "temperatureCurValue"),
        ("VES1724-58V-MIB", "temperatureConfHighThreshold"),
        ("VES1724-58V-MIB", "temperatureConfLowThreshold"))
)
if mibBuilder.loadTexts:
    temperatureNormal.setStatus(
        "current"
    )

fanRpmOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 6)
)
fanRpmOutOfRange.setObjects(
      *(("VES1724-58V-MIB", "fanConfIndex"),
        ("VES1724-58V-MIB", "fanRpmCurValue"),
        ("VES1724-58V-MIB", "fanConfHighThreshold"),
        ("VES1724-58V-MIB", "fanConfLowThreshold"))
)
if mibBuilder.loadTexts:
    fanRpmOutOfRange.setStatus(
        "current"
    )

fanRpmNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 7)
)
fanRpmNormal.setObjects(
      *(("VES1724-58V-MIB", "fanConfIndex"),
        ("VES1724-58V-MIB", "fanRpmCurValue"),
        ("VES1724-58V-MIB", "fanConfHighThreshold"),
        ("VES1724-58V-MIB", "fanConfLowThreshold"))
)
if mibBuilder.loadTexts:
    fanRpmNormal.setStatus(
        "current"
    )

hwRtcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 8)
)
if mibBuilder.loadTexts:
    hwRtcFail.setStatus(
        "current"
    )

extAlarmInput1Trigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 9)
)
extAlarmInput1Trigger.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput1Trigger.setStatus(
        "current"
    )

extAlarmInput1Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 10)
)
extAlarmInput1Release.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput1Release.setStatus(
        "current"
    )

extAlarmInput2Trigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 11)
)
extAlarmInput2Trigger.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput2Trigger.setStatus(
        "current"
    )

extAlarmInput2Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 12)
)
extAlarmInput2Release.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput2Release.setStatus(
        "current"
    )

extAlarmInput3Trigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 13)
)
extAlarmInput3Trigger.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput3Trigger.setStatus(
        "current"
    )

extAlarmInput3Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 14)
)
extAlarmInput3Release.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput3Release.setStatus(
        "current"
    )

extAlarmInput4Trigger = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 15)
)
extAlarmInput4Trigger.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput4Trigger.setStatus(
        "current"
    )

extAlarmInput4Release = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 16)
)
extAlarmInput4Release.setObjects(
    ("VES1724-58V-MIB", "externalAlarmName")
)
if mibBuilder.loadTexts:
    extAlarmInput4Release.setStatus(
        "current"
    )

acDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 38)
)
if mibBuilder.loadTexts:
    acDown.setStatus(
        "current"
    )

acDownClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 39)
)
if mibBuilder.loadTexts:
    acDownClear.setStatus(
        "current"
    )

battTempSensorAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 43)
)
if mibBuilder.loadTexts:
    battTempSensorAbsent.setStatus(
        "current"
    )

battTempSensorAbsentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 44)
)
if mibBuilder.loadTexts:
    battTempSensorAbsentClear.setStatus(
        "current"
    )

batteryTempOutofRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 45)
)
batteryTempOutofRange.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsTemperature"),
        ("VES1724-58V-MIB", "externalBatteryConfTempHighThreshold"),
        ("VES1724-58V-MIB", "externalBatteryConfTempLowThreshold"))
)
if mibBuilder.loadTexts:
    batteryTempOutofRange.setStatus(
        "current"
    )

batteryTempNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 46)
)
batteryTempNormal.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsTemperature"),
        ("VES1724-58V-MIB", "externalBatteryConfTempHighThreshold"),
        ("VES1724-58V-MIB", "externalBatteryConfTempLowThreshold"))
)
if mibBuilder.loadTexts:
    batteryTempNormal.setStatus(
        "current"
    )

dcCriticIssue = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 49)
)
dcCriticIssue.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsVoltage"),
        ("VES1724-58V-MIB", "externalBatteryConfDcCriticThreshold"))
)
if mibBuilder.loadTexts:
    dcCriticIssue.setStatus(
        "current"
    )

dcCriticClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 50)
)
dcCriticClear.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsVoltage"),
        ("VES1724-58V-MIB", "externalBatteryConfDcCriticThreshold"))
)
if mibBuilder.loadTexts:
    dcCriticClear.setStatus(
        "current"
    )

dcLowIssue = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 51)
)
dcLowIssue.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsVoltage"),
        ("VES1724-58V-MIB", "externalBatteryConfDcLowThreshold"))
)
if mibBuilder.loadTexts:
    dcLowIssue.setStatus(
        "current"
    )

dcLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 52)
)
dcLowClear.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsVoltage"),
        ("VES1724-58V-MIB", "externalBatteryConfDcLowThreshold"))
)
if mibBuilder.loadTexts:
    dcLowClear.setStatus(
        "current"
    )

dcErrorIssue = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 53)
)
dcErrorIssue.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsVoltage"),
        ("VES1724-58V-MIB", "externalBatteryConfDcErrThreshold"))
)
if mibBuilder.loadTexts:
    dcErrorIssue.setStatus(
        "current"
    )

dcErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 54)
)
dcErrorClear.setObjects(
      *(("VES1724-58V-MIB", "externalBatteryStatsVoltage"),
        ("VES1724-58V-MIB", "externalBatteryConfDcErrThreshold"))
)
if mibBuilder.loadTexts:
    dcErrorClear.setStatus(
        "current"
    )

dcFailIssue = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 55)
)
if mibBuilder.loadTexts:
    dcFailIssue.setStatus(
        "current"
    )

dcFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 3, 56)
)
if mibBuilder.loadTexts:
    dcFailClear.setStatus(
        "current"
    )

sysMacAntiSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 1)
)
sysMacAntiSpoofing.setObjects(
      *(("VES1724-58V-TRAPS-MIB", "sysMacAntiSpoofOrig"),
        ("VES1724-58V-TRAPS-MIB", "sysMacAntiSpoofNew"),
        ("VES1724-58V-TRAPS-MIB", "sysMacAntiSpoofMAC"))
)
if mibBuilder.loadTexts:
    sysMacAntiSpoofing.setStatus(
        "current"
    )

sysAlarmClearEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 2)
)
if mibBuilder.loadTexts:
    sysAlarmClearEnable.setStatus(
        "current"
    )

sysLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 3)
)
if mibBuilder.loadTexts:
    sysLoginFailure.setStatus(
        "current"
    )

reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 4)
)
reboot.setObjects(
    ("VES1724-58V-TRAPS-MIB", "sysProblemCause")
)
if mibBuilder.loadTexts:
    reboot.setStatus(
        "current"
    )

cpuOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 5)
)
cpuOverload.setObjects(
      *(("VES1724-58V-TRAPS-MIB", "sysCoaIssuedLoad"),
        ("VES1724-58V-MIB", "coaConfIssueThreshold"),
        ("VES1724-58V-MIB", "coaConfAnalyticMethod"))
)
if mibBuilder.loadTexts:
    cpuOverload.setStatus(
        "current"
    )

cpuOverloadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 6)
)
cpuOverloadClear.setObjects(
      *(("VES1724-58V-TRAPS-MIB", "sysCoaIssuedLoad"),
        ("VES1724-58V-MIB", "coaConfIssueThreshold"),
        ("VES1724-58V-MIB", "coaConfAnalyticMethod"))
)
if mibBuilder.loadTexts:
    cpuOverloadClear.setStatus(
        "current"
    )

cfgUploadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 7)
)
if mibBuilder.loadTexts:
    cfgUploadFail.setStatus(
        "current"
    )

cfgReloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 8)
)
if mibBuilder.loadTexts:
    cfgReloadFail.setStatus(
        "current"
    )

writeFlashFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 9)
)
if mibBuilder.loadTexts:
    writeFlashFail.setStatus(
        "current"
    )

mfgDataFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 4, 10)
)
if mibBuilder.loadTexts:
    mfgDataFail.setStatus(
        "current"
    )

geLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 1)
)
geLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    geLinkDown.setStatus(
        "current"
    )

geLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 2)
)
geLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    geLinkUp.setStatus(
        "current"
    )

gePmTrapTxOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 3)
)
gePmTrapTxOctets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minTxOctets"),
        ("VES1724-58V-MIB", "gePmThreshProfTxOctets"))
)
if mibBuilder.loadTexts:
    gePmTrapTxOctets.setStatus(
        "current"
    )

gePmTrapTxPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 4)
)
gePmTrapTxPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minTxPkts"),
        ("VES1724-58V-MIB", "gePmThreshProfTxPkts"))
)
if mibBuilder.loadTexts:
    gePmTrapTxPkts.setStatus(
        "current"
    )

gePmTrapTxBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 5)
)
gePmTrapTxBroadcastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minTxBroadcastPkts"),
        ("VES1724-58V-MIB", "gePmThreshProfTxBroadcastPkts"))
)
if mibBuilder.loadTexts:
    gePmTrapTxBroadcastPkts.setStatus(
        "current"
    )

gePmTrapTxMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 6)
)
gePmTrapTxMulticastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minTxMulticastPkts"),
        ("VES1724-58V-MIB", "gePmThreshProfTxMulticastPkts"))
)
if mibBuilder.loadTexts:
    gePmTrapTxMulticastPkts.setStatus(
        "current"
    )

gePmTrapRxOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 7)
)
gePmTrapRxOctets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxOctets"),
        ("VES1724-58V-MIB", "gePmThreshProfRxOctets"))
)
if mibBuilder.loadTexts:
    gePmTrapRxOctets.setStatus(
        "current"
    )

gePmTrapRxPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 8)
)
gePmTrapRxPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxPkts"),
        ("VES1724-58V-MIB", "gePmThreshProfRxPkts"))
)
if mibBuilder.loadTexts:
    gePmTrapRxPkts.setStatus(
        "current"
    )

gePmTrapRxBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 9)
)
gePmTrapRxBroadcastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxBroadcastPkts"),
        ("VES1724-58V-MIB", "gePmThreshProfRxBroadcastPkts"))
)
if mibBuilder.loadTexts:
    gePmTrapRxBroadcastPkts.setStatus(
        "current"
    )

gePmTrapRxMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 10)
)
gePmTrapRxMulticastPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxMulticastPkts"),
        ("VES1724-58V-MIB", "gePmThreshProfRxMulticastPkts"))
)
if mibBuilder.loadTexts:
    gePmTrapRxMulticastPkts.setStatus(
        "current"
    )

gePmTrapRxCRCAlignErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 11)
)
gePmTrapRxCRCAlignErrors.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxCRCAlignErrors"),
        ("VES1724-58V-MIB", "gePmThreshProfRxCRCAlignErrors"))
)
if mibBuilder.loadTexts:
    gePmTrapRxCRCAlignErrors.setStatus(
        "current"
    )

gePmTrapRxUndersizePkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 12)
)
gePmTrapRxUndersizePkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxUndersizePkts"),
        ("VES1724-58V-MIB", "gePmThreshProfRxUndersizePkts"))
)
if mibBuilder.loadTexts:
    gePmTrapRxUndersizePkts.setStatus(
        "current"
    )

gePmTrapRxOversizePkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 13)
)
gePmTrapRxOversizePkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxOversizePkts"),
        ("VES1724-58V-MIB", "gePmThreshProfRxOversizePkts"))
)
if mibBuilder.loadTexts:
    gePmTrapRxOversizePkts.setStatus(
        "current"
    )

gePmTrapRxFragments = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 14)
)
gePmTrapRxFragments.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minRxFragments"),
        ("VES1724-58V-MIB", "gePmThreshProfRxFragments"))
)
if mibBuilder.loadTexts:
    gePmTrapRxFragments.setStatus(
        "current"
    )

gePmTrapCollisions = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 15)
)
gePmTrapCollisions.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minCollisions"),
        ("VES1724-58V-MIB", "gePmThreshProfCollisions"))
)
if mibBuilder.loadTexts:
    gePmTrapCollisions.setStatus(
        "current"
    )

gePmTrapPkts64Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 16)
)
gePmTrapPkts64Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts64Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts64Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts64Octets.setStatus(
        "current"
    )

gePmTrapPkts65to127Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 17)
)
gePmTrapPkts65to127Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts65to127Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts65to127Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts65to127Octets.setStatus(
        "current"
    )

gePmTrapPkts128to255Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 18)
)
gePmTrapPkts128to255Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts128to255Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts128to255Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts128to255Octets.setStatus(
        "current"
    )

gePmTrapPkts256to511Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 19)
)
gePmTrapPkts256to511Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts256to511Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts256to511Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts256to511Octets.setStatus(
        "current"
    )

gePmTrapPkts512to1023Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 20)
)
gePmTrapPkts512to1023Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts512to1023Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts512to1023Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts512to1023Octets.setStatus(
        "current"
    )

gePmTrapPkts1024to1518Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 21)
)
gePmTrapPkts1024to1518Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts1024to1518Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts1024to1518Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts1024to1518Octets.setStatus(
        "current"
    )

gePmTrapPkts1519to1522Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 22)
)
gePmTrapPkts1519to1522Octets.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "gePmCurr15minPkts1519to1522Octets"),
        ("VES1724-58V-MIB", "gePmThreshProfPkts1519to1522Octets"))
)
if mibBuilder.loadTexts:
    gePmTrapPkts1519to1522Octets.setStatus(
        "current"
    )

geTxUtilizationLevel1Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 23)
)
geTxUtilizationLevel1Over.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilTxIssueLvl1Threshold"),
        ("VES1724-58V-MIB", "geUtilTxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geTxUtilizationLevel1Over.setStatus(
        "current"
    )

geTxUtilizationLevel1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 24)
)
geTxUtilizationLevel1Normal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilTxIssueLvl1Threshold"),
        ("VES1724-58V-MIB", "geUtilTxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geTxUtilizationLevel1Normal.setStatus(
        "current"
    )

geTxUtilizationLevel2Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 25)
)
geTxUtilizationLevel2Over.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilTxIssueLvl2Threshold"),
        ("VES1724-58V-MIB", "geUtilTxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geTxUtilizationLevel2Over.setStatus(
        "current"
    )

geTxUtilizationLevel2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 26)
)
geTxUtilizationLevel2Normal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilTxIssueLvl2Threshold"),
        ("VES1724-58V-MIB", "geUtilTxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geTxUtilizationLevel2Normal.setStatus(
        "current"
    )

geRxUtilizationLevel1Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 27)
)
geRxUtilizationLevel1Over.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilRxIssueLvl1Threshold"),
        ("VES1724-58V-MIB", "geUtilRxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geRxUtilizationLevel1Over.setStatus(
        "current"
    )

geRxUtilizationLevel1Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 28)
)
geRxUtilizationLevel1Normal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilRxIssueLvl1Threshold"),
        ("VES1724-58V-MIB", "geUtilRxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geRxUtilizationLevel1Normal.setStatus(
        "current"
    )

geRxUtilizationLevel2Over = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 29)
)
geRxUtilizationLevel2Over.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilRxIssueLvl2Threshold"),
        ("VES1724-58V-MIB", "geUtilRxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geRxUtilizationLevel2Over.setStatus(
        "current"
    )

geRxUtilizationLevel2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 5, 30)
)
geRxUtilizationLevel2Normal.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "geUtilRxIssueLvl2Threshold"),
        ("VES1724-58V-MIB", "geUtilRxCurrentPercent"))
)
if mibBuilder.loadTexts:
    geRxUtilizationLevel2Normal.setStatus(
        "current"
    )

voipBatteryFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 1)
)
voipBatteryFail.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "voipDevId"),
        ("VES1724-58V-TRAPS-MIB", "voipBatType"))
)
if mibBuilder.loadTexts:
    voipBatteryFail.setStatus(
        "current"
    )

voipBatteryClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 2)
)
voipBatteryClear.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "voipDevId"),
        ("VES1724-58V-TRAPS-MIB", "voipBatType"))
)
if mibBuilder.loadTexts:
    voipBatteryClear.setStatus(
        "current"
    )

voipClockFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 3)
)
voipClockFail.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "voipDevId"))
)
if mibBuilder.loadTexts:
    voipClockFail.setStatus(
        "current"
    )

voipClockClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 4)
)
voipClockClear.setObjects(
      *(("VES1724-58V-MIB", "slotModuleIdVes1724-58v"),
        ("VES1724-58V-TRAPS-MIB", "voipDevId"))
)
if mibBuilder.loadTexts:
    voipClockClear.setStatus(
        "current"
    )

voipTempError = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 5)
)
voipTempError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipPhoneState"))
)
if mibBuilder.loadTexts:
    voipTempError.setStatus(
        "current"
    )

voipTempClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 6)
)
voipTempClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipPhoneState"))
)
if mibBuilder.loadTexts:
    voipTempClear.setStatus(
        "current"
    )

voipDcPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 7)
)
voipDcPowerFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipPhoneState"))
)
if mibBuilder.loadTexts:
    voipDcPowerFail.setStatus(
        "current"
    )

voipDcPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 8)
)
voipDcPowerClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipPhoneState"))
)
if mibBuilder.loadTexts:
    voipDcPowerClear.setStatus(
        "current"
    )

voipAcPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 9)
)
voipAcPowerFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipPhoneState"))
)
if mibBuilder.loadTexts:
    voipAcPowerFail.setStatus(
        "current"
    )

voipAcPowerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 10)
)
voipAcPowerClear.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipPhoneState"))
)
if mibBuilder.loadTexts:
    voipAcPowerClear.setStatus(
        "current"
    )

voipRingTimerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 11)
)
voipRingTimerFail.setObjects(
      *(("VES1724-58V-TRAPS-MIB", "voipRingSegment"),
        ("VES1724-58V-TRAPS-MIB", "voipRingTimerId"))
)
if mibBuilder.loadTexts:
    voipRingTimerFail.setStatus(
        "current"
    )

voipRingRsrceFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 12)
)
voipRingRsrceFail.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    voipRingRsrceFail.setStatus(
        "current"
    )

voipNoFreeDspChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 13)
)
voipNoFreeDspChannel.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-TRAPS-MIB", "voipCodecType"))
)
if mibBuilder.loadTexts:
    voipNoFreeDspChannel.setStatus(
        "current"
    )

voipPortServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 14)
)
voipPortServiceUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    voipPortServiceUp.setStatus(
        "current"
    )

voipPortServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 15)
)
voipPortServiceDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    voipPortServiceDown.setStatus(
        "current"
    )

voipMgcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 20)
)
voipMgcUp.setObjects(
    ("VES1724-58V-MIB", "h248MgcIpDn")
)
if mibBuilder.loadTexts:
    voipMgcUp.setStatus(
        "current"
    )

voipMgcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 21)
)
voipMgcDown.setObjects(
    ("VES1724-58V-MIB", "h248MgcIpDn")
)
if mibBuilder.loadTexts:
    voipMgcDown.setStatus(
        "current"
    )

voipSipSvrUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 22)
)
voipSipSvrUp.setObjects(
    ("VES1724-58V-MIB", "sipProfileRegSvr")
)
if mibBuilder.loadTexts:
    voipSipSvrUp.setStatus(
        "current"
    )

voipSipSvrDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 6, 23)
)
voipSipSvrDown.setObjects(
    ("VES1724-58V-MIB", "sipProfileRegSvr")
)
if mibBuilder.loadTexts:
    voipSipSvrDown.setStatus(
        "current"
    )

fxsPmTrapRtpElapsedTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 1)
)
fxsPmTrapRtpElapsedTime.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpElapsedTime"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpElapsedTime"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpElapsedTime.setStatus(
        "current"
    )

fxsPmTrapRtpTxBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 2)
)
fxsPmTrapRtpTxBytes.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpTxBytes"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpTxBytes"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpTxBytes.setStatus(
        "current"
    )

fxsPmTrapRtpRxBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 3)
)
fxsPmTrapRtpRxBytes.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpRxBytes"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpRxBytes"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpRxBytes.setStatus(
        "current"
    )

fxsPmTrapRtpTxPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 4)
)
fxsPmTrapRtpTxPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpTxPackets"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpTxPackets"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpTxPkts.setStatus(
        "current"
    )

fxsPmTrapRtpRxPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 5)
)
fxsPmTrapRtpRxPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpRxPackets"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpRxPackets"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpRxPkts.setStatus(
        "current"
    )

fxsPmTrapRtpTxLostPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 6)
)
fxsPmTrapRtpTxLostPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpTxLostPackets"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpTxLostPackets"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpTxLostPkts.setStatus(
        "current"
    )

fxsPmTrapRtpRxLostPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 12, 49, 19, 7, 7)
)
fxsPmTrapRtpRxLostPkts.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("VES1724-58V-MIB", "fxsPmCurr15minRtpRxLostPackets"),
        ("VES1724-58V-MIB", "fxsPmThreshProfRtpRxLostPackets"))
)
if mibBuilder.loadTexts:
    fxsPmTrapRtpRxLostPkts.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VES1724-58V-TRAPS-MIB",
    **{"trap": trap,
       "object": object,
       "dslLgSenderIfIndex": dslLgSenderIfIndex,
       "sysProblemCause": sysProblemCause,
       "sysMacAntiSpoofOrig": sysMacAntiSpoofOrig,
       "sysMacAntiSpoofNew": sysMacAntiSpoofNew,
       "sysMacAntiSpoofMAC": sysMacAntiSpoofMAC,
       "sysCoaIssuedLoad": sysCoaIssuedLoad,
       "voipDevId": voipDevId,
       "voipCount": voipCount,
       "voipPhoneState": voipPhoneState,
       "voipBatType": voipBatType,
       "voipRingSegment": voipRingSegment,
       "voipRingTimerId": voipRingTimerId,
       "xdslDevId": xdslDevId,
       "voipCodecType": voipCodecType,
       "voipOpType": voipOpType,
       "voipPwrExceedCounter": voipPwrExceedCounter,
       "voipVtipVoltage": voipVtipVoltage,
       "voipVringVoltage": voipVringVoltage,
       "dsltrap": dsltrap,
       "dslLinkDown": dslLinkDown,
       "dslLinkUp": dslLinkUp,
       "xdslXtucLof": xdslXtucLof,
       "xdslXtucLos": xdslXtucLos,
       "xdslXturLof": xdslXturLof,
       "xdslXturLos": xdslXturLos,
       "xdslXturLpr": xdslXturLpr,
       "xdslXtucLofClear": xdslXtucLofClear,
       "xdslXtucLosClear": xdslXtucLosClear,
       "xdslXturLofClear": xdslXturLofClear,
       "xdslXturLosClear": xdslXturLosClear,
       "xdslXturLprClear": xdslXturLprClear,
       "xdslLoopguard": xdslLoopguard,
       "xdslLoopguardClear": xdslLoopguardClear,
       "xdslDspDownloadFail": xdslDspDownloadFail,
       "xdslDspDownloadFailClear": xdslDspDownloadFailClear,
       "xdslDspInoperable": xdslDspInoperable,
       "xdslHtPortPolicer": xdslHtPortPolicer,
       "xdslLinePerfLOFSThreshXtuc": xdslLinePerfLOFSThreshXtuc,
       "xdslLinePerfLOFSThreshXtur": xdslLinePerfLOFSThreshXtur,
       "xdslLinePerfLPRSThreshXtur": xdslLinePerfLPRSThreshXtur,
       "xdslPmTrapTxOctets": xdslPmTrapTxOctets,
       "xdslPmTrapTxPkts": xdslPmTrapTxPkts,
       "xdslPmTrapTxUnicastPkts": xdslPmTrapTxUnicastPkts,
       "xdslPmTrapTxBroadcastPkts": xdslPmTrapTxBroadcastPkts,
       "xdslPmTrapTxMulticastPkts": xdslPmTrapTxMulticastPkts,
       "xdslPmTrapTxDiscardPkts": xdslPmTrapTxDiscardPkts,
       "xdslPmTrapRxOctets": xdslPmTrapRxOctets,
       "xdslPmTrapRxPkts": xdslPmTrapRxPkts,
       "xdslPmTrapRxUnicastPkts": xdslPmTrapRxUnicastPkts,
       "xdslPmTrapRxBroadcastPkts": xdslPmTrapRxBroadcastPkts,
       "xdslPmTrapRxMulticastPkts": xdslPmTrapRxMulticastPkts,
       "xdslPmTrapRxDiscardPkts": xdslPmTrapRxDiscardPkts,
       "xdslBondLinkUp": xdslBondLinkUp,
       "xdslBondLinkDown": xdslBondLinkDown,
       "xdslBondPortLinkUp": xdslBondPortLinkUp,
       "xdslBondPortLinkDown": xdslBondPortLinkDown,
       "equipment": equipment,
       "hwMonitorFail": hwMonitorFail,
       "voltageOutOfRange": voltageOutOfRange,
       "voltageNormal": voltageNormal,
       "temperatureOutOfRange": temperatureOutOfRange,
       "temperatureNormal": temperatureNormal,
       "fanRpmOutOfRange": fanRpmOutOfRange,
       "fanRpmNormal": fanRpmNormal,
       "hwRtcFail": hwRtcFail,
       "extAlarmInput1Trigger": extAlarmInput1Trigger,
       "extAlarmInput1Release": extAlarmInput1Release,
       "extAlarmInput2Trigger": extAlarmInput2Trigger,
       "extAlarmInput2Release": extAlarmInput2Release,
       "extAlarmInput3Trigger": extAlarmInput3Trigger,
       "extAlarmInput3Release": extAlarmInput3Release,
       "extAlarmInput4Trigger": extAlarmInput4Trigger,
       "extAlarmInput4Release": extAlarmInput4Release,
       "acDown": acDown,
       "acDownClear": acDownClear,
       "battTempSensorAbsent": battTempSensorAbsent,
       "battTempSensorAbsentClear": battTempSensorAbsentClear,
       "batteryTempOutofRange": batteryTempOutofRange,
       "batteryTempNormal": batteryTempNormal,
       "dcCriticIssue": dcCriticIssue,
       "dcCriticClear": dcCriticClear,
       "dcLowIssue": dcLowIssue,
       "dcLowClear": dcLowClear,
       "dcErrorIssue": dcErrorIssue,
       "dcErrorClear": dcErrorClear,
       "dcFailIssue": dcFailIssue,
       "dcFailClear": dcFailClear,
       "systrap": systrap,
       "sysMacAntiSpoofing": sysMacAntiSpoofing,
       "sysAlarmClearEnable": sysAlarmClearEnable,
       "sysLoginFailure": sysLoginFailure,
       "reboot": reboot,
       "cpuOverload": cpuOverload,
       "cpuOverloadClear": cpuOverloadClear,
       "cfgUploadFail": cfgUploadFail,
       "cfgReloadFail": cfgReloadFail,
       "writeFlashFail": writeFlashFail,
       "mfgDataFail": mfgDataFail,
       "getrap": getrap,
       "geLinkDown": geLinkDown,
       "geLinkUp": geLinkUp,
       "gePmTrapTxOctets": gePmTrapTxOctets,
       "gePmTrapTxPkts": gePmTrapTxPkts,
       "gePmTrapTxBroadcastPkts": gePmTrapTxBroadcastPkts,
       "gePmTrapTxMulticastPkts": gePmTrapTxMulticastPkts,
       "gePmTrapRxOctets": gePmTrapRxOctets,
       "gePmTrapRxPkts": gePmTrapRxPkts,
       "gePmTrapRxBroadcastPkts": gePmTrapRxBroadcastPkts,
       "gePmTrapRxMulticastPkts": gePmTrapRxMulticastPkts,
       "gePmTrapRxCRCAlignErrors": gePmTrapRxCRCAlignErrors,
       "gePmTrapRxUndersizePkts": gePmTrapRxUndersizePkts,
       "gePmTrapRxOversizePkts": gePmTrapRxOversizePkts,
       "gePmTrapRxFragments": gePmTrapRxFragments,
       "gePmTrapCollisions": gePmTrapCollisions,
       "gePmTrapPkts64Octets": gePmTrapPkts64Octets,
       "gePmTrapPkts65to127Octets": gePmTrapPkts65to127Octets,
       "gePmTrapPkts128to255Octets": gePmTrapPkts128to255Octets,
       "gePmTrapPkts256to511Octets": gePmTrapPkts256to511Octets,
       "gePmTrapPkts512to1023Octets": gePmTrapPkts512to1023Octets,
       "gePmTrapPkts1024to1518Octets": gePmTrapPkts1024to1518Octets,
       "gePmTrapPkts1519to1522Octets": gePmTrapPkts1519to1522Octets,
       "geTxUtilizationLevel1Over": geTxUtilizationLevel1Over,
       "geTxUtilizationLevel1Normal": geTxUtilizationLevel1Normal,
       "geTxUtilizationLevel2Over": geTxUtilizationLevel2Over,
       "geTxUtilizationLevel2Normal": geTxUtilizationLevel2Normal,
       "geRxUtilizationLevel1Over": geRxUtilizationLevel1Over,
       "geRxUtilizationLevel1Normal": geRxUtilizationLevel1Normal,
       "geRxUtilizationLevel2Over": geRxUtilizationLevel2Over,
       "geRxUtilizationLevel2Normal": geRxUtilizationLevel2Normal,
       "voiptrap": voiptrap,
       "voipBatteryFail": voipBatteryFail,
       "voipBatteryClear": voipBatteryClear,
       "voipClockFail": voipClockFail,
       "voipClockClear": voipClockClear,
       "voipTempError": voipTempError,
       "voipTempClear": voipTempClear,
       "voipDcPowerFail": voipDcPowerFail,
       "voipDcPowerClear": voipDcPowerClear,
       "voipAcPowerFail": voipAcPowerFail,
       "voipAcPowerClear": voipAcPowerClear,
       "voipRingTimerFail": voipRingTimerFail,
       "voipRingRsrceFail": voipRingRsrceFail,
       "voipNoFreeDspChannel": voipNoFreeDspChannel,
       "voipPortServiceUp": voipPortServiceUp,
       "voipPortServiceDown": voipPortServiceDown,
       "voipMgcUp": voipMgcUp,
       "voipMgcDown": voipMgcDown,
       "voipSipSvrUp": voipSipSvrUp,
       "voipSipSvrDown": voipSipSvrDown,
       "fxstrap": fxstrap,
       "fxsPmTrapRtpElapsedTime": fxsPmTrapRtpElapsedTime,
       "fxsPmTrapRtpTxBytes": fxsPmTrapRtpTxBytes,
       "fxsPmTrapRtpRxBytes": fxsPmTrapRtpRxBytes,
       "fxsPmTrapRtpTxPkts": fxsPmTrapRtpTxPkts,
       "fxsPmTrapRtpRxPkts": fxsPmTrapRtpRxPkts,
       "fxsPmTrapRtpTxLostPkts": fxsPmTrapRtpTxLostPkts,
       "fxsPmTrapRtpRxLostPkts": fxsPmTrapRtpRxLostPkts}
)
