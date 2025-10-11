# SNMP MIB module (ZTE-AN-VOICE-CALLCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VOICE-CALLCTRL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:51 2025
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

zxAnVoiceCallCtrlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_ZxAnVoiceMgmt_ObjectIdentity = ObjectIdentity
zxAnVoiceMgmt = _ZxAnVoiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_ZxAnVoipCallCtrl_ObjectIdentity = ObjectIdentity
zxAnVoipCallCtrl = _ZxAnVoipCallCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6)
)
_MsagCallResStatistic_ObjectIdentity = ObjectIdentity
msagCallResStatistic = _MsagCallResStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5)
)


class _MsagCRAccessRatio_Type(DisplayString):
    """Custom type msagCRAccessRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MsagCRAccessRatio_Type.__name__ = "DisplayString"
_MsagCRAccessRatio_Object = MibScalar
msagCRAccessRatio = _MsagCRAccessRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 1),
    _MsagCRAccessRatio_Type()
)
msagCRAccessRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRAccessRatio.setStatus("current")


class _MsagCRIPSUsingRatio_Type(DisplayString):
    """Custom type msagCRIPSUsingRatio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MsagCRIPSUsingRatio_Type.__name__ = "DisplayString"
_MsagCRIPSUsingRatio_Object = MibScalar
msagCRIPSUsingRatio = _MsagCRIPSUsingRatio_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 2),
    _MsagCRIPSUsingRatio_Type()
)
msagCRIPSUsingRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRIPSUsingRatio.setStatus("current")
_MsagCROpenChannelReq_Type = Integer32
_MsagCROpenChannelReq_Object = MibScalar
msagCROpenChannelReq = _MsagCROpenChannelReq_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 3),
    _MsagCROpenChannelReq_Type()
)
msagCROpenChannelReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCROpenChannelReq.setStatus("current")
_MsagCRRecOpenSucces_Type = Integer32
_MsagCRRecOpenSucces_Object = MibScalar
msagCRRecOpenSucces = _MsagCRRecOpenSucces_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 4),
    _MsagCRRecOpenSucces_Type()
)
msagCRRecOpenSucces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecOpenSucces.setStatus("current")
_MsagCRRecOpenFail_Type = Integer32
_MsagCRRecOpenFail_Object = MibScalar
msagCRRecOpenFail = _MsagCRRecOpenFail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 5),
    _MsagCRRecOpenFail_Type()
)
msagCRRecOpenFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecOpenFail.setStatus("current")
_MsagCROpenChannTimerOut_Type = Integer32
_MsagCROpenChannTimerOut_Object = MibScalar
msagCROpenChannTimerOut = _MsagCROpenChannTimerOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 6),
    _MsagCROpenChannTimerOut_Type()
)
msagCROpenChannTimerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCROpenChannTimerOut.setStatus("current")
_MsagCRModifyChannel_Type = Integer32
_MsagCRModifyChannel_Object = MibScalar
msagCRModifyChannel = _MsagCRModifyChannel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 7),
    _MsagCRModifyChannel_Type()
)
msagCRModifyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRModifyChannel.setStatus("current")
_MsagCRRecModifySucces_Type = Integer32
_MsagCRRecModifySucces_Object = MibScalar
msagCRRecModifySucces = _MsagCRRecModifySucces_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 8),
    _MsagCRRecModifySucces_Type()
)
msagCRRecModifySucces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecModifySucces.setStatus("current")
_MsagCRModifyChFail_Type = Integer32
_MsagCRModifyChFail_Object = MibScalar
msagCRModifyChFail = _MsagCRModifyChFail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 9),
    _MsagCRModifyChFail_Type()
)
msagCRModifyChFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRModifyChFail.setStatus("current")
_MsagCRWtModifyChannTimerOut_Type = Integer32
_MsagCRWtModifyChannTimerOut_Object = MibScalar
msagCRWtModifyChannTimerOut = _MsagCRWtModifyChannTimerOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 10),
    _MsagCRWtModifyChannTimerOut_Type()
)
msagCRWtModifyChannTimerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRWtModifyChannTimerOut.setStatus("current")
_MsagCRSendCloseChannel_Type = Integer32
_MsagCRSendCloseChannel_Object = MibScalar
msagCRSendCloseChannel = _MsagCRSendCloseChannel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 11),
    _MsagCRSendCloseChannel_Type()
)
msagCRSendCloseChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRSendCloseChannel.setStatus("current")
_MsagCRRecCloseChanSucc_Type = Integer32
_MsagCRRecCloseChanSucc_Object = MibScalar
msagCRRecCloseChanSucc = _MsagCRRecCloseChanSucc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 12),
    _MsagCRRecCloseChanSucc_Type()
)
msagCRRecCloseChanSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecCloseChanSucc.setStatus("current")
_MsagCRRecCloseChanFail_Type = Integer32
_MsagCRRecCloseChanFail_Object = MibScalar
msagCRRecCloseChanFail = _MsagCRRecCloseChanFail_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 13),
    _MsagCRRecCloseChanFail_Type()
)
msagCRRecCloseChanFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecCloseChanFail.setStatus("current")
_MsagCRRecCloseChanTimerOut_Type = Integer32
_MsagCRRecCloseChanTimerOut_Object = MibScalar
msagCRRecCloseChanTimerOut = _MsagCRRecCloseChanTimerOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 14),
    _MsagCRRecCloseChanTimerOut_Type()
)
msagCRRecCloseChanTimerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecCloseChanTimerOut.setStatus("current")
_MsagCRRecMprReload_Type = Integer32
_MsagCRRecMprReload_Object = MibScalar
msagCRRecMprReload = _MsagCRRecMprReload_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 15),
    _MsagCRRecMprReload_Type()
)
msagCRRecMprReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagCRRecMprReload.setStatus("current")


class _MsagCRClearRTPRecord_Type(Integer32):
    """Custom type msagCRClearRTPRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MsagCRClearRTPRecord_Type.__name__ = "Integer32"
_MsagCRClearRTPRecord_Object = MibScalar
msagCRClearRTPRecord = _MsagCRClearRTPRecord_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 5, 16),
    _MsagCRClearRTPRecord_Type()
)
msagCRClearRTPRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagCRClearRTPRecord.setStatus("current")
_ZxAnVoipCallCtrlGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnVoipCallCtrlGlobalObjects = _ZxAnVoipCallCtrlGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1300)
)


class _ZxAnVoipCallCtrlMgmtCapabilities_Type(Bits):
    """Custom type zxAnVoipCallCtrlMgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        ("nbPlatform", 0)
    )

_ZxAnVoipCallCtrlMgmtCapabilities_Type.__name__ = "Bits"
_ZxAnVoipCallCtrlMgmtCapabilities_Object = MibScalar
zxAnVoipCallCtrlMgmtCapabilities = _ZxAnVoipCallCtrlMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1300, 1),
    _ZxAnVoipCallCtrlMgmtCapabilities_Type()
)
zxAnVoipCallCtrlMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoipCallCtrlMgmtCapabilities.setStatus("current")
_ZxAnCallOptimizationTable_Object = MibTable
zxAnCallOptimizationTable = _ZxAnCallOptimizationTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301)
)
if mibBuilder.loadTexts:
    zxAnCallOptimizationTable.setStatus("current")
_ZxAnCallOptimizationEntry_Object = MibTableRow
zxAnCallOptimizationEntry = _ZxAnCallOptimizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1)
)
zxAnCallOptimizationEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallOptIndex"),
)
if mibBuilder.loadTexts:
    zxAnCallOptimizationEntry.setStatus("current")


class _ZxAnCallOptIndex_Type(Integer32):
    """Custom type zxAnCallOptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ZxAnCallOptIndex_Type.__name__ = "Integer32"
_ZxAnCallOptIndex_Object = MibTableColumn
zxAnCallOptIndex = _ZxAnCallOptIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 1),
    _ZxAnCallOptIndex_Type()
)
zxAnCallOptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallOptIndex.setStatus("current")


class _ZxAnCallOptOpenMsgAck_Type(Integer32):
    """Custom type zxAnCallOptOpenMsgAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_ZxAnCallOptOpenMsgAck_Type.__name__ = "Integer32"
_ZxAnCallOptOpenMsgAck_Object = MibTableColumn
zxAnCallOptOpenMsgAck = _ZxAnCallOptOpenMsgAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 2),
    _ZxAnCallOptOpenMsgAck_Type()
)
zxAnCallOptOpenMsgAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptOpenMsgAck.setStatus("current")


class _ZxAnCallOptPlayToneAck_Type(Integer32):
    """Custom type zxAnCallOptPlayToneAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_ZxAnCallOptPlayToneAck_Type.__name__ = "Integer32"
_ZxAnCallOptPlayToneAck_Object = MibTableColumn
zxAnCallOptPlayToneAck = _ZxAnCallOptPlayToneAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 3),
    _ZxAnCallOptPlayToneAck_Type()
)
zxAnCallOptPlayToneAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptPlayToneAck.setStatus("current")


class _ZxAnCallOptSubPriority_Type(Integer32):
    """Custom type zxAnCallOptSubPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("higher", 1),
          ("nothigher", 2))
    )


_ZxAnCallOptSubPriority_Type.__name__ = "Integer32"
_ZxAnCallOptSubPriority_Object = MibTableColumn
zxAnCallOptSubPriority = _ZxAnCallOptSubPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 4),
    _ZxAnCallOptSubPriority_Type()
)
zxAnCallOptSubPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptSubPriority.setStatus("current")


class _ZxAnCallOptH248Statistic_Type(Integer32):
    """Custom type zxAnCallOptH248Statistic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("send", 1),
          ("notsend", 2))
    )


_ZxAnCallOptH248Statistic_Type.__name__ = "Integer32"
_ZxAnCallOptH248Statistic_Object = MibTableColumn
zxAnCallOptH248Statistic = _ZxAnCallOptH248Statistic_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 8),
    _ZxAnCallOptH248Statistic_Type()
)
zxAnCallOptH248Statistic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptH248Statistic.setStatus("current")


class _ZxAnCallOptServiceAbnormal_Type(Integer32):
    """Custom type zxAnCallOptServiceAbnormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_ZxAnCallOptServiceAbnormal_Type.__name__ = "Integer32"
_ZxAnCallOptServiceAbnormal_Object = MibTableColumn
zxAnCallOptServiceAbnormal = _ZxAnCallOptServiceAbnormal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 11),
    _ZxAnCallOptServiceAbnormal_Type()
)
zxAnCallOptServiceAbnormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptServiceAbnormal.setStatus("current")


class _ZxAnCallOptMgProtocolErr_Type(Integer32):
    """Custom type zxAnCallOptMgProtocolErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_ZxAnCallOptMgProtocolErr_Type.__name__ = "Integer32"
_ZxAnCallOptMgProtocolErr_Object = MibTableColumn
zxAnCallOptMgProtocolErr = _ZxAnCallOptMgProtocolErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 12),
    _ZxAnCallOptMgProtocolErr_Type()
)
zxAnCallOptMgProtocolErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptMgProtocolErr.setStatus("current")


class _ZxAnCallOptMgcProtocolErr_Type(Integer32):
    """Custom type zxAnCallOptMgcProtocolErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_ZxAnCallOptMgcProtocolErr_Type.__name__ = "Integer32"
_ZxAnCallOptMgcProtocolErr_Object = MibTableColumn
zxAnCallOptMgcProtocolErr = _ZxAnCallOptMgcProtocolErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 13),
    _ZxAnCallOptMgcProtocolErr_Type()
)
zxAnCallOptMgcProtocolErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptMgcProtocolErr.setStatus("current")


class _ZxAnCallOptMgInsideErr_Type(Integer32):
    """Custom type zxAnCallOptMgInsideErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwayssend", 1),
          ("notalways", 2))
    )


_ZxAnCallOptMgInsideErr_Type.__name__ = "Integer32"
_ZxAnCallOptMgInsideErr_Object = MibTableColumn
zxAnCallOptMgInsideErr = _ZxAnCallOptMgInsideErr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 14),
    _ZxAnCallOptMgInsideErr_Type()
)
zxAnCallOptMgInsideErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptMgInsideErr.setStatus("current")


class _ZxAnCallOptCallLimit_Type(Integer32):
    """Custom type zxAnCallOptCallLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("limitByMg", 1),
          ("limitByMgc", 2),
          ("noLimit", 3))
    )


_ZxAnCallOptCallLimit_Type.__name__ = "Integer32"
_ZxAnCallOptCallLimit_Object = MibTableColumn
zxAnCallOptCallLimit = _ZxAnCallOptCallLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 15),
    _ZxAnCallOptCallLimit_Type()
)
zxAnCallOptCallLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptCallLimit.setStatus("current")


class _ZxAnCallOptCallLimitMaxUserNum_Type(Integer32):
    """Custom type zxAnCallOptCallLimitMaxUserNum based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_ZxAnCallOptCallLimitMaxUserNum_Type.__name__ = "Integer32"
_ZxAnCallOptCallLimitMaxUserNum_Object = MibTableColumn
zxAnCallOptCallLimitMaxUserNum = _ZxAnCallOptCallLimitMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1301, 1, 16),
    _ZxAnCallOptCallLimitMaxUserNum_Type()
)
zxAnCallOptCallLimitMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCallOptCallLimitMaxUserNum.setStatus("current")
_ZxAnCallEscapeObjects_ObjectIdentity = ObjectIdentity
zxAnCallEscapeObjects = _ZxAnCallEscapeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302)
)
_ZxAnCallEscapeFxoTable_Object = MibTable
zxAnCallEscapeFxoTable = _ZxAnCallEscapeFxoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2)
)
if mibBuilder.loadTexts:
    zxAnCallEscapeFxoTable.setStatus("current")
_ZxAnCallEscapeFxoEntry_Object = MibTableRow
zxAnCallEscapeFxoEntry = _ZxAnCallEscapeFxoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1)
)
zxAnCallEscapeFxoEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeRack"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeShelf"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeSlot"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapePort"),
)
if mibBuilder.loadTexts:
    zxAnCallEscapeFxoEntry.setStatus("current")
_ZxAnCallEscapeRack_Type = Integer32
_ZxAnCallEscapeRack_Object = MibTableColumn
zxAnCallEscapeRack = _ZxAnCallEscapeRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1, 1),
    _ZxAnCallEscapeRack_Type()
)
zxAnCallEscapeRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallEscapeRack.setStatus("current")
_ZxAnCallEscapeShelf_Type = Integer32
_ZxAnCallEscapeShelf_Object = MibTableColumn
zxAnCallEscapeShelf = _ZxAnCallEscapeShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1, 2),
    _ZxAnCallEscapeShelf_Type()
)
zxAnCallEscapeShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallEscapeShelf.setStatus("current")
_ZxAnCallEscapeSlot_Type = Integer32
_ZxAnCallEscapeSlot_Object = MibTableColumn
zxAnCallEscapeSlot = _ZxAnCallEscapeSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1, 3),
    _ZxAnCallEscapeSlot_Type()
)
zxAnCallEscapeSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallEscapeSlot.setStatus("current")
_ZxAnCallEscapePort_Type = Integer32
_ZxAnCallEscapePort_Object = MibTableColumn
zxAnCallEscapePort = _ZxAnCallEscapePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1, 4),
    _ZxAnCallEscapePort_Type()
)
zxAnCallEscapePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallEscapePort.setStatus("current")
_ZxAnCallEscapeFxoOperNum_Type = Integer32
_ZxAnCallEscapeFxoOperNum_Object = MibTableColumn
zxAnCallEscapeFxoOperNum = _ZxAnCallEscapeFxoOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1, 5),
    _ZxAnCallEscapeFxoOperNum_Type()
)
zxAnCallEscapeFxoOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapeFxoOperNum.setStatus("current")
_ZxAnCallEscapeFxoRowStatus_Type = RowStatus
_ZxAnCallEscapeFxoRowStatus_Object = MibTableColumn
zxAnCallEscapeFxoRowStatus = _ZxAnCallEscapeFxoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 2, 1, 50),
    _ZxAnCallEscapeFxoRowStatus_Type()
)
zxAnCallEscapeFxoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapeFxoRowStatus.setStatus("current")
_ZxAnCallEscapePriTable_Object = MibTable
zxAnCallEscapePriTable = _ZxAnCallEscapePriTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 3)
)
if mibBuilder.loadTexts:
    zxAnCallEscapePriTable.setStatus("current")
_ZxAnCallEscapePriEntry_Object = MibTableRow
zxAnCallEscapePriEntry = _ZxAnCallEscapePriEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 3, 1)
)
zxAnCallEscapePriEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeRack"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeShelf"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeSlot"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeDsx1LinkNo"),
)
if mibBuilder.loadTexts:
    zxAnCallEscapePriEntry.setStatus("current")
_ZxAnCallEscapeDsx1LinkNo_Type = Integer32
_ZxAnCallEscapeDsx1LinkNo_Object = MibTableColumn
zxAnCallEscapeDsx1LinkNo = _ZxAnCallEscapeDsx1LinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 3, 1, 1),
    _ZxAnCallEscapeDsx1LinkNo_Type()
)
zxAnCallEscapeDsx1LinkNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallEscapeDsx1LinkNo.setStatus("current")
_ZxAnCallEscapePriOperNum_Type = Integer32
_ZxAnCallEscapePriOperNum_Object = MibTableColumn
zxAnCallEscapePriOperNum = _ZxAnCallEscapePriOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 3, 1, 2),
    _ZxAnCallEscapePriOperNum_Type()
)
zxAnCallEscapePriOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapePriOperNum.setStatus("current")
_ZxAnCallEscapePriRowStatus_Type = RowStatus
_ZxAnCallEscapePriRowStatus_Object = MibTableColumn
zxAnCallEscapePriRowStatus = _ZxAnCallEscapePriRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 3, 1, 50),
    _ZxAnCallEscapePriRowStatus_Type()
)
zxAnCallEscapePriRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapePriRowStatus.setStatus("current")
_ZxAnCallEscapePriDLinkTable_Object = MibTable
zxAnCallEscapePriDLinkTable = _ZxAnCallEscapePriDLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4)
)
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkTable.setStatus("current")
_ZxAnCallEscapePriDLinkEntry_Object = MibTableRow
zxAnCallEscapePriDLinkEntry = _ZxAnCallEscapePriDLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4, 1)
)
zxAnCallEscapePriDLinkEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeRack"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeShelf"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeSlot"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapeDsx1LinkNo"),
    (0, "ZTE-AN-VOICE-CALLCTRL-MIB", "zxAnCallEscapePriDLinkTimeslot"),
)
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkEntry.setStatus("current")


class _ZxAnCallEscapePriDLinkTimeslot_Type(Integer32):
    """Custom type zxAnCallEscapePriDLinkTimeslot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_ZxAnCallEscapePriDLinkTimeslot_Type.__name__ = "Integer32"
_ZxAnCallEscapePriDLinkTimeslot_Object = MibTableColumn
zxAnCallEscapePriDLinkTimeslot = _ZxAnCallEscapePriDLinkTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4, 1, 1),
    _ZxAnCallEscapePriDLinkTimeslot_Type()
)
zxAnCallEscapePriDLinkTimeslot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkTimeslot.setStatus("current")


class _ZxAnCallEscapePriDLinkLinkId_Type(Integer32):
    """Custom type zxAnCallEscapePriDLinkLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_ZxAnCallEscapePriDLinkLinkId_Type.__name__ = "Integer32"
_ZxAnCallEscapePriDLinkLinkId_Object = MibTableColumn
zxAnCallEscapePriDLinkLinkId = _ZxAnCallEscapePriDLinkLinkId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4, 1, 2),
    _ZxAnCallEscapePriDLinkLinkId_Type()
)
zxAnCallEscapePriDLinkLinkId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkLinkId.setStatus("current")
_ZxAnCallEscapePriDLinkOperNum_Type = Integer32
_ZxAnCallEscapePriDLinkOperNum_Object = MibTableColumn
zxAnCallEscapePriDLinkOperNum = _ZxAnCallEscapePriDLinkOperNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4, 1, 3),
    _ZxAnCallEscapePriDLinkOperNum_Type()
)
zxAnCallEscapePriDLinkOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkOperNum.setStatus("current")


class _ZxAnCallEscapePriDLinkLinkType_Type(Integer32):
    """Custom type zxAnCallEscapePriDLinkLinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("networkSide", 1),
          ("subscriberSide", 2))
    )


_ZxAnCallEscapePriDLinkLinkType_Type.__name__ = "Integer32"
_ZxAnCallEscapePriDLinkLinkType_Object = MibTableColumn
zxAnCallEscapePriDLinkLinkType = _ZxAnCallEscapePriDLinkLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4, 1, 4),
    _ZxAnCallEscapePriDLinkLinkType_Type()
)
zxAnCallEscapePriDLinkLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkLinkType.setStatus("current")
_ZxAnCallEscapePriDLinkRowStatus_Type = RowStatus
_ZxAnCallEscapePriDLinkRowStatus_Object = MibTableColumn
zxAnCallEscapePriDLinkRowStatus = _ZxAnCallEscapePriDLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 6, 1302, 4, 1, 50),
    _ZxAnCallEscapePriDLinkRowStatus_Type()
)
zxAnCallEscapePriDLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCallEscapePriDLinkRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VOICE-CALLCTRL-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnVoiceCallCtrlMib": zxAnVoiceCallCtrlMib,
       "zxAnVoiceMgmt": zxAnVoiceMgmt,
       "zxAnVoipCallCtrl": zxAnVoipCallCtrl,
       "msagCallResStatistic": msagCallResStatistic,
       "msagCRAccessRatio": msagCRAccessRatio,
       "msagCRIPSUsingRatio": msagCRIPSUsingRatio,
       "msagCROpenChannelReq": msagCROpenChannelReq,
       "msagCRRecOpenSucces": msagCRRecOpenSucces,
       "msagCRRecOpenFail": msagCRRecOpenFail,
       "msagCROpenChannTimerOut": msagCROpenChannTimerOut,
       "msagCRModifyChannel": msagCRModifyChannel,
       "msagCRRecModifySucces": msagCRRecModifySucces,
       "msagCRModifyChFail": msagCRModifyChFail,
       "msagCRWtModifyChannTimerOut": msagCRWtModifyChannTimerOut,
       "msagCRSendCloseChannel": msagCRSendCloseChannel,
       "msagCRRecCloseChanSucc": msagCRRecCloseChanSucc,
       "msagCRRecCloseChanFail": msagCRRecCloseChanFail,
       "msagCRRecCloseChanTimerOut": msagCRRecCloseChanTimerOut,
       "msagCRRecMprReload": msagCRRecMprReload,
       "msagCRClearRTPRecord": msagCRClearRTPRecord,
       "zxAnVoipCallCtrlGlobalObjects": zxAnVoipCallCtrlGlobalObjects,
       "zxAnVoipCallCtrlMgmtCapabilities": zxAnVoipCallCtrlMgmtCapabilities,
       "zxAnCallOptimizationTable": zxAnCallOptimizationTable,
       "zxAnCallOptimizationEntry": zxAnCallOptimizationEntry,
       "zxAnCallOptIndex": zxAnCallOptIndex,
       "zxAnCallOptOpenMsgAck": zxAnCallOptOpenMsgAck,
       "zxAnCallOptPlayToneAck": zxAnCallOptPlayToneAck,
       "zxAnCallOptSubPriority": zxAnCallOptSubPriority,
       "zxAnCallOptH248Statistic": zxAnCallOptH248Statistic,
       "zxAnCallOptServiceAbnormal": zxAnCallOptServiceAbnormal,
       "zxAnCallOptMgProtocolErr": zxAnCallOptMgProtocolErr,
       "zxAnCallOptMgcProtocolErr": zxAnCallOptMgcProtocolErr,
       "zxAnCallOptMgInsideErr": zxAnCallOptMgInsideErr,
       "zxAnCallOptCallLimit": zxAnCallOptCallLimit,
       "zxAnCallOptCallLimitMaxUserNum": zxAnCallOptCallLimitMaxUserNum,
       "zxAnCallEscapeObjects": zxAnCallEscapeObjects,
       "zxAnCallEscapeFxoTable": zxAnCallEscapeFxoTable,
       "zxAnCallEscapeFxoEntry": zxAnCallEscapeFxoEntry,
       "zxAnCallEscapeRack": zxAnCallEscapeRack,
       "zxAnCallEscapeShelf": zxAnCallEscapeShelf,
       "zxAnCallEscapeSlot": zxAnCallEscapeSlot,
       "zxAnCallEscapePort": zxAnCallEscapePort,
       "zxAnCallEscapeFxoOperNum": zxAnCallEscapeFxoOperNum,
       "zxAnCallEscapeFxoRowStatus": zxAnCallEscapeFxoRowStatus,
       "zxAnCallEscapePriTable": zxAnCallEscapePriTable,
       "zxAnCallEscapePriEntry": zxAnCallEscapePriEntry,
       "zxAnCallEscapeDsx1LinkNo": zxAnCallEscapeDsx1LinkNo,
       "zxAnCallEscapePriOperNum": zxAnCallEscapePriOperNum,
       "zxAnCallEscapePriRowStatus": zxAnCallEscapePriRowStatus,
       "zxAnCallEscapePriDLinkTable": zxAnCallEscapePriDLinkTable,
       "zxAnCallEscapePriDLinkEntry": zxAnCallEscapePriDLinkEntry,
       "zxAnCallEscapePriDLinkTimeslot": zxAnCallEscapePriDLinkTimeslot,
       "zxAnCallEscapePriDLinkLinkId": zxAnCallEscapePriDLinkLinkId,
       "zxAnCallEscapePriDLinkOperNum": zxAnCallEscapePriDLinkOperNum,
       "zxAnCallEscapePriDLinkLinkType": zxAnCallEscapePriDLinkLinkType,
       "zxAnCallEscapePriDLinkRowStatus": zxAnCallEscapePriDLinkRowStatus}
)
