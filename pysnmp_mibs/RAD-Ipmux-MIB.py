# SNMP MIB module (RAD-Ipmux-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-Ipmux-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:08 2025
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

(ifAlias,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias")

(agnLed,) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "agnLed")

(atmInterfaceAlarmStatus,) = mibBuilder.importSymbols(
    "RAD-NtePrtCo-MIB",
    "atmInterfaceAlarmStatus")

(diverseIfWanGen,
 radSysWanEvents) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "diverseIfWanGen",
    "radSysWanEvents")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ip2If = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ip2IfTable_Object = MibTable
ip2IfTable = _Ip2IfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1)
)
if mibBuilder.loadTexts:
    ip2IfTable.setStatus("current")
_Ip2IfEntry_Object = MibTableRow
ip2IfEntry = _Ip2IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1)
)
ip2IfEntry.setIndexNames(
    (0, "RAD-Ipmux-MIB", "ip2IfChannelIndex"),
)
if mibBuilder.loadTexts:
    ip2IfEntry.setStatus("current")
_Ip2IfChannelIndex_Type = Integer32
_Ip2IfChannelIndex_Object = MibTableColumn
ip2IfChannelIndex = _Ip2IfChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 1),
    _Ip2IfChannelIndex_Type()
)
ip2IfChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfChannelIndex.setStatus("current")
_Ip2IfRowStatus_Type = RowStatus
_Ip2IfRowStatus_Object = MibTableColumn
ip2IfRowStatus = _Ip2IfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 2),
    _Ip2IfRowStatus_Type()
)
ip2IfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfRowStatus.setStatus("current")


class _Ip2IfOperStatus_Type(Integer32):
    """Custom type ip2IfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 3),
          ("disabled", 4),
          ("remoteFail", 5),
          ("localFail", 6),
          ("unavailable", 7),
          ("validationFail", 8),
          ("standby", 9),
          ("tdmFail", 10),
          ("hwMismatch", 11))
    )


_Ip2IfOperStatus_Type.__name__ = "Integer32"
_Ip2IfOperStatus_Object = MibTableColumn
ip2IfOperStatus = _Ip2IfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 3),
    _Ip2IfOperStatus_Type()
)
ip2IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfOperStatus.setStatus("current")


class _Ip2IfAdminStatus_Type(Integer32):
    """Custom type ip2IfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 3))
    )


_Ip2IfAdminStatus_Type.__name__ = "Integer32"
_Ip2IfAdminStatus_Object = MibTableColumn
ip2IfAdminStatus = _Ip2IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 4),
    _Ip2IfAdminStatus_Type()
)
ip2IfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfAdminStatus.setStatus("current")
_Ip2IfDestAddr_Type = IpAddress
_Ip2IfDestAddr_Object = MibTableColumn
ip2IfDestAddr = _Ip2IfDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 5),
    _Ip2IfDestAddr_Type()
)
ip2IfDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfDestAddr.setStatus("current")
_Ip2IfNextHop_Type = IpAddress
_Ip2IfNextHop_Object = MibTableColumn
ip2IfNextHop = _Ip2IfNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 6),
    _Ip2IfNextHop_Type()
)
ip2IfNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfNextHop.setStatus("current")
_Ip2IfDestPort_Type = Integer32
_Ip2IfDestPort_Object = MibTableColumn
ip2IfDestPort = _Ip2IfDestPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 7),
    _Ip2IfDestPort_Type()
)
ip2IfDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfDestPort.setStatus("current")
_Ip2IfMacAddr_Type = MacAddress
_Ip2IfMacAddr_Object = MibTableColumn
ip2IfMacAddr = _Ip2IfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 8),
    _Ip2IfMacAddr_Type()
)
ip2IfMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMacAddr.setStatus("current")
_Ip2IfJitterBuffer_Type = Integer32
_Ip2IfJitterBuffer_Object = MibTableColumn
ip2IfJitterBuffer = _Ip2IfJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 9),
    _Ip2IfJitterBuffer_Type()
)
ip2IfJitterBuffer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfJitterBuffer.setStatus("current")
_Ip2IfTos_Type = Integer32
_Ip2IfTos_Object = MibTableColumn
ip2IfTos = _Ip2IfTos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 10),
    _Ip2IfTos_Type()
)
ip2IfTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfTos.setStatus("current")
_Ip2IfTDMBytesInFrame_Type = Integer32
_Ip2IfTDMBytesInFrame_Object = MibTableColumn
ip2IfTDMBytesInFrame = _Ip2IfTDMBytesInFrame_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 11),
    _Ip2IfTDMBytesInFrame_Type()
)
ip2IfTDMBytesInFrame.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfTDMBytesInFrame.setStatus("current")


class _Ip2IfVlanSupport_Type(Integer32):
    """Custom type ip2IfVlanSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_Ip2IfVlanSupport_Type.__name__ = "Integer32"
_Ip2IfVlanSupport_Object = MibTableColumn
ip2IfVlanSupport = _Ip2IfVlanSupport_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 12),
    _Ip2IfVlanSupport_Type()
)
ip2IfVlanSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVlanSupport.setStatus("current")
_Ip2IfVlanIdentifier_Type = Integer32
_Ip2IfVlanIdentifier_Object = MibTableColumn
ip2IfVlanIdentifier = _Ip2IfVlanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 13),
    _Ip2IfVlanIdentifier_Type()
)
ip2IfVlanIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVlanIdentifier.setStatus("current")
_Ip2IfVlanFramePriority_Type = Integer32
_Ip2IfVlanFramePriority_Object = MibTableColumn
ip2IfVlanFramePriority = _Ip2IfVlanFramePriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 14),
    _Ip2IfVlanFramePriority_Type()
)
ip2IfVlanFramePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVlanFramePriority.setStatus("current")


class _Ip2IfExitPort_Type(Integer32):
    """Custom type ip2IfExitPort based on Integer32"""
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
              35)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ext1", 2),
          ("ext2", 3),
          ("auto", 4),
          ("card2Ext1", 5),
          ("card2Ext2", 6),
          ("ext5", 7),
          ("ext7", 8),
          ("ext6", 9),
          ("prt17", 10),
          ("prt18", 11),
          ("prt19", 12),
          ("prt20", 13),
          ("prtE1T1B", 14),
          ("prtEthUser", 15),
          ("card3Ext1", 16),
          ("card3Ext2", 17),
          ("card3Ext3", 18),
          ("card3Ext4", 19),
          ("card4Ext1", 20),
          ("card4Ext2", 21),
          ("card4Ext3", 22),
          ("card4Ext4", 23),
          ("card1Ext3", 24),
          ("card1Ext4", 25),
          ("card1Ext5", 26),
          ("card1Ext6", 27),
          ("card1Ext7", 28),
          ("card1Ext8", 29),
          ("card2Ext3", 30),
          ("card2Ext4", 31),
          ("card2Ext5", 32),
          ("card2Ext6", 33),
          ("card2Ext7", 34),
          ("card2Ext8", 35))
    )


_Ip2IfExitPort_Type.__name__ = "Integer32"
_Ip2IfExitPort_Object = MibTableColumn
ip2IfExitPort = _Ip2IfExitPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 15),
    _Ip2IfExitPort_Type()
)
ip2IfExitPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfExitPort.setStatus("current")
_Ip2IfVoiceOos_Type = OctetString
_Ip2IfVoiceOos_Object = MibTableColumn
ip2IfVoiceOos = _Ip2IfVoiceOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 16),
    _Ip2IfVoiceOos_Type()
)
ip2IfVoiceOos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVoiceOos.setStatus("current")
_Ip2IfDataOos_Type = OctetString
_Ip2IfDataOos_Object = MibTableColumn
ip2IfDataOos = _Ip2IfDataOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 17),
    _Ip2IfDataOos_Type()
)
ip2IfDataOos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfDataOos.setStatus("current")
_Ip2IfBundleUsage_Type = Integer32
_Ip2IfBundleUsage_Object = MibTableColumn
ip2IfBundleUsage = _Ip2IfBundleUsage_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 18),
    _Ip2IfBundleUsage_Type()
)
ip2IfBundleUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfBundleUsage.setStatus("current")
_Ip2IfOAM_Type = OctetString
_Ip2IfOAM_Object = MibTableColumn
ip2IfOAM = _Ip2IfOAM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 19),
    _Ip2IfOAM_Type()
)
ip2IfOAM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfOAM.setStatus("current")


class _Ip2IfTDMoIpMode_Type(Integer32):
    """Custom type ip2IfTDMoIpMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("static", 2),
          ("dynamicLES", 3),
          ("dynamicCAS", 4),
          ("cesOverIp", 5),
          ("voiceOverMpls", 6),
          ("hdlc", 7),
          ("voIpComprHeader", 8),
          ("voMplsComprHeader", 9),
          ("satop", 10),
          ("cesOverPsn", 11),
          ("hdlcOverPsn", 12))
    )


_Ip2IfTDMoIpMode_Type.__name__ = "Integer32"
_Ip2IfTDMoIpMode_Object = MibTableColumn
ip2IfTDMoIpMode = _Ip2IfTDMoIpMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 20),
    _Ip2IfTDMoIpMode_Type()
)
ip2IfTDMoIpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfTDMoIpMode.setStatus("current")


class _Ip2IfTimeElapsed_Type(Integer32):
    """Custom type ip2IfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Ip2IfTimeElapsed_Type.__name__ = "Integer32"
_Ip2IfTimeElapsed_Object = MibTableColumn
ip2IfTimeElapsed = _Ip2IfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 21),
    _Ip2IfTimeElapsed_Type()
)
ip2IfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfTimeElapsed.setStatus("current")


class _Ip2IfValidIntervals_Type(Integer32):
    """Custom type ip2IfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Ip2IfValidIntervals_Type.__name__ = "Integer32"
_Ip2IfValidIntervals_Object = MibTableColumn
ip2IfValidIntervals = _Ip2IfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 22),
    _Ip2IfValidIntervals_Type()
)
ip2IfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfValidIntervals.setStatus("current")


class _Ip2IfFarEndType_Type(Integer32):
    """Custom type ip2IfFarEndType based on Integer32"""
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
        *(("notApplicable", 1),
          ("e1", 2),
          ("t1Esf", 3),
          ("t1D4", 4),
          ("fxs", 5),
          ("serialLink", 6),
          ("t1Unframed", 7))
    )


_Ip2IfFarEndType_Type.__name__ = "Integer32"
_Ip2IfFarEndType_Object = MibTableColumn
ip2IfFarEndType = _Ip2IfFarEndType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 23),
    _Ip2IfFarEndType_Type()
)
ip2IfFarEndType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfFarEndType.setStatus("current")


class _Ip2IfRdnState_Type(Integer32):
    """Custom type ip2IfRdnState based on Integer32"""
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
        *(("notApplicable", 1),
          ("none", 2),
          ("primary", 3),
          ("secondary", 4))
    )


_Ip2IfRdnState_Type.__name__ = "Integer32"
_Ip2IfRdnState_Object = MibTableColumn
ip2IfRdnState = _Ip2IfRdnState_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 24),
    _Ip2IfRdnState_Type()
)
ip2IfRdnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfRdnState.setStatus("current")
_Ip2IfSourceAddr_Type = IpAddress
_Ip2IfSourceAddr_Object = MibTableColumn
ip2IfSourceAddr = _Ip2IfSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 25),
    _Ip2IfSourceAddr_Type()
)
ip2IfSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfSourceAddr.setStatus("current")
_Ip2IfBandWidth_Type = Integer32
_Ip2IfBandWidth_Object = MibTableColumn
ip2IfBandWidth = _Ip2IfBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 26),
    _Ip2IfBandWidth_Type()
)
ip2IfBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfBandWidth.setStatus("current")
_Ip2IfMeasuredSilence_Type = Integer32
_Ip2IfMeasuredSilence_Object = MibTableColumn
ip2IfMeasuredSilence = _Ip2IfMeasuredSilence_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 27),
    _Ip2IfMeasuredSilence_Type()
)
ip2IfMeasuredSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfMeasuredSilence.setStatus("current")


class _Ip2IfPayloadType_Type(Integer32):
    """Custom type ip2IfPayloadType based on Integer32"""
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
        *(("notApplicable", 1),
          ("data", 2),
          ("voice", 3),
          ("voiceAndCas", 4))
    )


_Ip2IfPayloadType_Type.__name__ = "Integer32"
_Ip2IfPayloadType_Object = MibTableColumn
ip2IfPayloadType = _Ip2IfPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 28),
    _Ip2IfPayloadType_Type()
)
ip2IfPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfPayloadType.setStatus("current")


class _Ip2IfProtocolVersion_Type(Integer32):
    """Custom type ip2IfProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("v1", 2),
          ("v2", 3))
    )


_Ip2IfProtocolVersion_Type.__name__ = "Integer32"
_Ip2IfProtocolVersion_Object = MibTableColumn
ip2IfProtocolVersion = _Ip2IfProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 29),
    _Ip2IfProtocolVersion_Type()
)
ip2IfProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfProtocolVersion.setStatus("current")
_Ip2IfTdmBackUpNextHop_Type = IpAddress
_Ip2IfTdmBackUpNextHop_Object = MibTableColumn
ip2IfTdmBackUpNextHop = _Ip2IfTdmBackUpNextHop_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 30),
    _Ip2IfTdmBackUpNextHop_Type()
)
ip2IfTdmBackUpNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfTdmBackUpNextHop.setStatus("current")


class _Ip2IfOosTxEnable_Type(Integer32):
    """Custom type ip2IfOosTxEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfOosTxEnable_Type.__name__ = "Integer32"
_Ip2IfOosTxEnable_Object = MibTableColumn
ip2IfOosTxEnable = _Ip2IfOosTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 31),
    _Ip2IfOosTxEnable_Type()
)
ip2IfOosTxEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfOosTxEnable.setStatus("current")
_Ip2IfConnCheckPktFrequency_Type = Integer32
_Ip2IfConnCheckPktFrequency_Object = MibTableColumn
ip2IfConnCheckPktFrequency = _Ip2IfConnCheckPktFrequency_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 32),
    _Ip2IfConnCheckPktFrequency_Type()
)
ip2IfConnCheckPktFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfConnCheckPktFrequency.setStatus("current")
_Ip2IfConnPktTimeOutCycles_Type = Integer32
_Ip2IfConnPktTimeOutCycles_Object = MibTableColumn
ip2IfConnPktTimeOutCycles = _Ip2IfConnPktTimeOutCycles_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 33),
    _Ip2IfConnPktTimeOutCycles_Type()
)
ip2IfConnPktTimeOutCycles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfConnPktTimeOutCycles.setStatus("current")


class _Ip2IfMfRelay_Type(Integer32):
    """Custom type ip2IfMfRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfMfRelay_Type.__name__ = "Integer32"
_Ip2IfMfRelay_Object = MibTableColumn
ip2IfMfRelay = _Ip2IfMfRelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 34),
    _Ip2IfMfRelay_Type()
)
ip2IfMfRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMfRelay.setStatus("current")
_Ip2IfTxGain_Type = Integer32
_Ip2IfTxGain_Object = MibTableColumn
ip2IfTxGain = _Ip2IfTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 35),
    _Ip2IfTxGain_Type()
)
ip2IfTxGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfTxGain.setStatus("current")


class _Ip2IfSuperTandem_Type(Integer32):
    """Custom type ip2IfSuperTandem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfSuperTandem_Type.__name__ = "Integer32"
_Ip2IfSuperTandem_Object = MibTableColumn
ip2IfSuperTandem = _Ip2IfSuperTandem_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 36),
    _Ip2IfSuperTandem_Type()
)
ip2IfSuperTandem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfSuperTandem.setStatus("current")
_Ip2IfSrcPort_Type = Integer32
_Ip2IfSrcPort_Object = MibTableColumn
ip2IfSrcPort = _Ip2IfSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 37),
    _Ip2IfSrcPort_Type()
)
ip2IfSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfSrcPort.setStatus("current")


class _Ip2IfModemCalls_Type(Integer32):
    """Custom type ip2IfModemCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("relay", 4))
    )


_Ip2IfModemCalls_Type.__name__ = "Integer32"
_Ip2IfModemCalls_Object = MibTableColumn
ip2IfModemCalls = _Ip2IfModemCalls_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 38),
    _Ip2IfModemCalls_Type()
)
ip2IfModemCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfModemCalls.setStatus("current")
_Ip2IfMinPulseWidth_Type = Integer32
_Ip2IfMinPulseWidth_Object = MibTableColumn
ip2IfMinPulseWidth = _Ip2IfMinPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 39),
    _Ip2IfMinPulseWidth_Type()
)
ip2IfMinPulseWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMinPulseWidth.setStatus("current")
_Ip2IfMinPowerLevel_Type = Integer32
_Ip2IfMinPowerLevel_Object = MibTableColumn
ip2IfMinPowerLevel = _Ip2IfMinPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 40),
    _Ip2IfMinPowerLevel_Type()
)
ip2IfMinPowerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMinPowerLevel.setStatus("current")


class _Ip2IfEchoCanceler_Type(Integer32):
    """Custom type ip2IfEchoCanceler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3))
    )


_Ip2IfEchoCanceler_Type.__name__ = "Integer32"
_Ip2IfEchoCanceler_Object = MibTableColumn
ip2IfEchoCanceler = _Ip2IfEchoCanceler_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 41),
    _Ip2IfEchoCanceler_Type()
)
ip2IfEchoCanceler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfEchoCanceler.setStatus("current")


class _Ip2IfCodingLaw_Type(Integer32):
    """Custom type ip2IfCodingLaw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLAW", 1),
          ("uLAW", 2))
    )


_Ip2IfCodingLaw_Type.__name__ = "Integer32"
_Ip2IfCodingLaw_Object = MibTableColumn
ip2IfCodingLaw = _Ip2IfCodingLaw_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 42),
    _Ip2IfCodingLaw_Type()
)
ip2IfCodingLaw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCodingLaw.setStatus("current")


class _Ip2IfCustomToneDetect_Type(Integer32):
    """Custom type ip2IfCustomToneDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_Ip2IfCustomToneDetect_Type.__name__ = "Integer32"
_Ip2IfCustomToneDetect_Object = MibTableColumn
ip2IfCustomToneDetect = _Ip2IfCustomToneDetect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 43),
    _Ip2IfCustomToneDetect_Type()
)
ip2IfCustomToneDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCustomToneDetect.setStatus("current")
_Ip2IfCallerIdDelay_Type = Integer32
_Ip2IfCallerIdDelay_Object = MibTableColumn
ip2IfCallerIdDelay = _Ip2IfCallerIdDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 44),
    _Ip2IfCallerIdDelay_Type()
)
ip2IfCallerIdDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCallerIdDelay.setStatus("current")


class _Ip2IfConnectivityMode_Type(Integer32):
    """Custom type ip2IfConnectivityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ping", 2),
          ("oam", 3))
    )


_Ip2IfConnectivityMode_Type.__name__ = "Integer32"
_Ip2IfConnectivityMode_Object = MibTableColumn
ip2IfConnectivityMode = _Ip2IfConnectivityMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 45),
    _Ip2IfConnectivityMode_Type()
)
ip2IfConnectivityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfConnectivityMode.setStatus("current")


class _Ip2IfClockSourceEnable_Type(Integer32):
    """Custom type ip2IfClockSourceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfClockSourceEnable_Type.__name__ = "Integer32"
_Ip2IfClockSourceEnable_Object = MibTableColumn
ip2IfClockSourceEnable = _Ip2IfClockSourceEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 46),
    _Ip2IfClockSourceEnable_Type()
)
ip2IfClockSourceEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfClockSourceEnable.setStatus("current")


class _Ip2IfNetworkType_Type(Integer32):
    """Custom type ip2IfNetworkType based on Integer32"""
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
        *(("notApplicable", 1),
          ("ip", 2),
          ("mplsEth", 3),
          ("mac", 4),
          ("ipComprHeader", 5),
          ("mplsComprHeader", 6),
          ("udp", 7))
    )


_Ip2IfNetworkType_Type.__name__ = "Integer32"
_Ip2IfNetworkType_Object = MibTableColumn
ip2IfNetworkType = _Ip2IfNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 47),
    _Ip2IfNetworkType_Type()
)
ip2IfNetworkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfNetworkType.setStatus("current")


class _Ip2IfMplsRxLabelEnable_Type(Integer32):
    """Custom type ip2IfMplsRxLabelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfMplsRxLabelEnable_Type.__name__ = "Integer32"
_Ip2IfMplsRxLabelEnable_Object = MibTableColumn
ip2IfMplsRxLabelEnable = _Ip2IfMplsRxLabelEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 48),
    _Ip2IfMplsRxLabelEnable_Type()
)
ip2IfMplsRxLabelEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMplsRxLabelEnable.setStatus("current")
_Ip2IfMplsRxLabel_Type = Integer32
_Ip2IfMplsRxLabel_Object = MibTableColumn
ip2IfMplsRxLabel = _Ip2IfMplsRxLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 49),
    _Ip2IfMplsRxLabel_Type()
)
ip2IfMplsRxLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMplsRxLabel.setStatus("current")


class _Ip2IfMplsTxLabelEnable_Type(Integer32):
    """Custom type ip2IfMplsTxLabelEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfMplsTxLabelEnable_Type.__name__ = "Integer32"
_Ip2IfMplsTxLabelEnable_Object = MibTableColumn
ip2IfMplsTxLabelEnable = _Ip2IfMplsTxLabelEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 50),
    _Ip2IfMplsTxLabelEnable_Type()
)
ip2IfMplsTxLabelEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMplsTxLabelEnable.setStatus("current")
_Ip2IfMplsTxLabel_Type = Integer32
_Ip2IfMplsTxLabel_Object = MibTableColumn
ip2IfMplsTxLabel = _Ip2IfMplsTxLabel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 51),
    _Ip2IfMplsTxLabel_Type()
)
ip2IfMplsTxLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMplsTxLabel.setStatus("current")


class _Ip2IfMplsTxExpBits_Type(Integer32):
    """Custom type ip2IfMplsTxExpBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Ip2IfMplsTxExpBits_Type.__name__ = "Integer32"
_Ip2IfMplsTxExpBits_Object = MibTableColumn
ip2IfMplsTxExpBits = _Ip2IfMplsTxExpBits_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 52),
    _Ip2IfMplsTxExpBits_Type()
)
ip2IfMplsTxExpBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMplsTxExpBits.setStatus("current")


class _Ip2IfMfcSpoofing_Type(Integer32):
    """Custom type ip2IfMfcSpoofing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfMfcSpoofing_Type.__name__ = "Integer32"
_Ip2IfMfcSpoofing_Object = MibTableColumn
ip2IfMfcSpoofing = _Ip2IfMfcSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 53),
    _Ip2IfMfcSpoofing_Type()
)
ip2IfMfcSpoofing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMfcSpoofing.setStatus("current")
_Ip2IfToneAckInterval_Type = Integer32
_Ip2IfToneAckInterval_Object = MibTableColumn
ip2IfToneAckInterval = _Ip2IfToneAckInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 54),
    _Ip2IfToneAckInterval_Type()
)
ip2IfToneAckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfToneAckInterval.setStatus("current")


class _Ip2IfNextHopType_Type(Integer32):
    """Custom type ip2IfNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ipAddress", 2),
          ("macAddress", 3))
    )


_Ip2IfNextHopType_Type.__name__ = "Integer32"
_Ip2IfNextHopType_Object = MibTableColumn
ip2IfNextHopType = _Ip2IfNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 55),
    _Ip2IfNextHopType_Type()
)
ip2IfNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfNextHopType.setStatus("current")


class _Ip2IfNoiseLevelForVAD_Type(Integer32):
    """Custom type ip2IfNoiseLevelForVAD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("high", 3),
          ("off", 4))
    )


_Ip2IfNoiseLevelForVAD_Type.__name__ = "Integer32"
_Ip2IfNoiseLevelForVAD_Object = MibTableColumn
ip2IfNoiseLevelForVAD = _Ip2IfNoiseLevelForVAD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 56),
    _Ip2IfNoiseLevelForVAD_Type()
)
ip2IfNoiseLevelForVAD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfNoiseLevelForVAD.setStatus("current")


class _Ip2IfClockPreferences_Type(Integer32):
    """Custom type ip2IfClockPreferences based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accurateness", 2),
          ("constantDelay", 3))
    )


_Ip2IfClockPreferences_Type.__name__ = "Integer32"
_Ip2IfClockPreferences_Object = MibTableColumn
ip2IfClockPreferences = _Ip2IfClockPreferences_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 57),
    _Ip2IfClockPreferences_Type()
)
ip2IfClockPreferences.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfClockPreferences.setStatus("current")


class _Ip2IfConnectionMode_Type(Integer32):
    """Custom type ip2IfConnectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tdmOIpCe", 2),
          ("tdmOIpCv", 3))
    )


_Ip2IfConnectionMode_Type.__name__ = "Integer32"
_Ip2IfConnectionMode_Object = MibTableColumn
ip2IfConnectionMode = _Ip2IfConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 58),
    _Ip2IfConnectionMode_Type()
)
ip2IfConnectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfConnectionMode.setStatus("current")


class _Ip2IfRingBack_Type(Integer32):
    """Custom type ip2IfRingBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_Ip2IfRingBack_Type.__name__ = "Integer32"
_Ip2IfRingBack_Object = MibTableColumn
ip2IfRingBack = _Ip2IfRingBack_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 59),
    _Ip2IfRingBack_Type()
)
ip2IfRingBack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfRingBack.setStatus("current")


class _Ip2IfReversePolarity_Type(Integer32):
    """Custom type ip2IfReversePolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_Ip2IfReversePolarity_Type.__name__ = "Integer32"
_Ip2IfReversePolarity_Object = MibTableColumn
ip2IfReversePolarity = _Ip2IfReversePolarity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 60),
    _Ip2IfReversePolarity_Type()
)
ip2IfReversePolarity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfReversePolarity.setStatus("current")


class _Ip2IfPulseMeter_Type(Integer32):
    """Custom type ip2IfPulseMeter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_Ip2IfPulseMeter_Type.__name__ = "Integer32"
_Ip2IfPulseMeter_Object = MibTableColumn
ip2IfPulseMeter = _Ip2IfPulseMeter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 61),
    _Ip2IfPulseMeter_Type()
)
ip2IfPulseMeter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfPulseMeter.setStatus("current")


class _Ip2IfPulseMeterFreq_Type(Integer32):
    """Custom type ip2IfPulseMeterFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rate12Khz", 2),
          ("rate16Khz", 3))
    )


_Ip2IfPulseMeterFreq_Type.__name__ = "Integer32"
_Ip2IfPulseMeterFreq_Object = MibTableColumn
ip2IfPulseMeterFreq = _Ip2IfPulseMeterFreq_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 62),
    _Ip2IfPulseMeterFreq_Type()
)
ip2IfPulseMeterFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfPulseMeterFreq.setStatus("current")
_Ip2IfPulseMeterPeriod_Type = Integer32
_Ip2IfPulseMeterPeriod_Object = MibTableColumn
ip2IfPulseMeterPeriod = _Ip2IfPulseMeterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 63),
    _Ip2IfPulseMeterPeriod_Type()
)
ip2IfPulseMeterPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfPulseMeterPeriod.setStatus("current")


class _Ip2IfOnHookDetect_Type(Integer32):
    """Custom type ip2IfOnHookDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_Ip2IfOnHookDetect_Type.__name__ = "Integer32"
_Ip2IfOnHookDetect_Object = MibTableColumn
ip2IfOnHookDetect = _Ip2IfOnHookDetect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 64),
    _Ip2IfOnHookDetect_Type()
)
ip2IfOnHookDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfOnHookDetect.setStatus("current")


class _Ip2IfComfortNoiseGen_Type(Integer32):
    """Custom type ip2IfComfortNoiseGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_Ip2IfComfortNoiseGen_Type.__name__ = "Integer32"
_Ip2IfComfortNoiseGen_Object = MibTableColumn
ip2IfComfortNoiseGen = _Ip2IfComfortNoiseGen_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 65),
    _Ip2IfComfortNoiseGen_Type()
)
ip2IfComfortNoiseGen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfComfortNoiseGen.setStatus("current")
_Ip2IfExitChannel_Type = Integer32
_Ip2IfExitChannel_Object = MibTableColumn
ip2IfExitChannel = _Ip2IfExitChannel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 66),
    _Ip2IfExitChannel_Type()
)
ip2IfExitChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfExitChannel.setStatus("current")
_Ip2IfMaxVBDModemCalls_Type = Integer32
_Ip2IfMaxVBDModemCalls_Object = MibTableColumn
ip2IfMaxVBDModemCalls = _Ip2IfMaxVBDModemCalls_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 67),
    _Ip2IfMaxVBDModemCalls_Type()
)
ip2IfMaxVBDModemCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMaxVBDModemCalls.setStatus("current")
_Ip2IfMaxRelayModemCalls_Type = Integer32
_Ip2IfMaxRelayModemCalls_Object = MibTableColumn
ip2IfMaxRelayModemCalls = _Ip2IfMaxRelayModemCalls_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 68),
    _Ip2IfMaxRelayModemCalls_Type()
)
ip2IfMaxRelayModemCalls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMaxRelayModemCalls.setStatus("current")


class _Ip2IfCustomToneFrequency_Type(Integer32):
    """Custom type ip2IfCustomToneFrequency based on Integer32"""
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
        *(("notApplicable", 1),
          ("f1780Hz", 2),
          ("f2000Hz", 3),
          ("f1780Plus2000Hz", 4))
    )


_Ip2IfCustomToneFrequency_Type.__name__ = "Integer32"
_Ip2IfCustomToneFrequency_Object = MibTableColumn
ip2IfCustomToneFrequency = _Ip2IfCustomToneFrequency_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 69),
    _Ip2IfCustomToneFrequency_Type()
)
ip2IfCustomToneFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCustomToneFrequency.setStatus("current")


class _Ip2IfVadMethod_Type(Integer32):
    """Custom type ip2IfVadMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 2),
          ("internalITUT", 3))
    )


_Ip2IfVadMethod_Type.__name__ = "Integer32"
_Ip2IfVadMethod_Object = MibTableColumn
ip2IfVadMethod = _Ip2IfVadMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 70),
    _Ip2IfVadMethod_Type()
)
ip2IfVadMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVadMethod.setStatus("current")
_Ip2IfRxGain_Type = Integer32
_Ip2IfRxGain_Object = MibTableColumn
ip2IfRxGain = _Ip2IfRxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 71),
    _Ip2IfRxGain_Type()
)
ip2IfRxGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfRxGain.setStatus("current")


class _Ip2IfCallerIDType_Type(Integer32):
    """Custom type ip2IfCallerIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bellcoreType1", 2),
          ("v23", 3))
    )


_Ip2IfCallerIDType_Type.__name__ = "Integer32"
_Ip2IfCallerIDType_Object = MibTableColumn
ip2IfCallerIDType = _Ip2IfCallerIDType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 72),
    _Ip2IfCallerIDType_Type()
)
ip2IfCallerIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCallerIDType.setStatus("current")


class _Ip2IfPeerAddrType_Type(Integer32):
    """Custom type ip2IfPeerAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("ipAddress", 2),
          ("macAddress", 3))
    )


_Ip2IfPeerAddrType_Type.__name__ = "Integer32"
_Ip2IfPeerAddrType_Object = MibTableColumn
ip2IfPeerAddrType = _Ip2IfPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 73),
    _Ip2IfPeerAddrType_Type()
)
ip2IfPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfPeerAddrType.setStatus("current")


class _Ip2IfVbdRate_Type(Integer32):
    """Custom type ip2IfVbdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("r64KbpsIn5msecIntervalsG711", 2),
          ("r64KbpsIn10msecIntervalsG711", 3),
          ("r32KbpsG726", 4),
          ("r24KbpsG726", 5))
    )


_Ip2IfVbdRate_Type.__name__ = "Integer32"
_Ip2IfVbdRate_Object = MibTableColumn
ip2IfVbdRate = _Ip2IfVbdRate_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 74),
    _Ip2IfVbdRate_Type()
)
ip2IfVbdRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVbdRate.setStatus("current")


class _Ip2IfDtmfDetection_Type(Integer32):
    """Custom type ip2IfDtmfDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfDtmfDetection_Type.__name__ = "Integer32"
_Ip2IfDtmfDetection_Object = MibTableColumn
ip2IfDtmfDetection = _Ip2IfDtmfDetection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 75),
    _Ip2IfDtmfDetection_Type()
)
ip2IfDtmfDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfDtmfDetection.setStatus("current")
_Ip2IfNlpCutoffLevel_Type = Unsigned32
_Ip2IfNlpCutoffLevel_Object = MibTableColumn
ip2IfNlpCutoffLevel = _Ip2IfNlpCutoffLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 76),
    _Ip2IfNlpCutoffLevel_Type()
)
ip2IfNlpCutoffLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfNlpCutoffLevel.setStatus("current")
_Ip2IfDtdErlRatioCutoffQ3_Type = Unsigned32
_Ip2IfDtdErlRatioCutoffQ3_Object = MibTableColumn
ip2IfDtdErlRatioCutoffQ3 = _Ip2IfDtdErlRatioCutoffQ3_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 77),
    _Ip2IfDtdErlRatioCutoffQ3_Type()
)
ip2IfDtdErlRatioCutoffQ3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfDtdErlRatioCutoffQ3.setStatus("current")


class _Ip2IfCASRedundancy_Type(Integer32):
    """Custom type ip2IfCASRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfCASRedundancy_Type.__name__ = "Integer32"
_Ip2IfCASRedundancy_Object = MibTableColumn
ip2IfCASRedundancy = _Ip2IfCASRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 78),
    _Ip2IfCASRedundancy_Type()
)
ip2IfCASRedundancy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCASRedundancy.setStatus("current")


class _Ip2IfBundleSensitivity_Type(Integer32):
    """Custom type ip2IfBundleSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delaySensitive", 2),
          ("dataSensitive", 3))
    )


_Ip2IfBundleSensitivity_Type.__name__ = "Integer32"
_Ip2IfBundleSensitivity_Object = MibTableColumn
ip2IfBundleSensitivity = _Ip2IfBundleSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 79),
    _Ip2IfBundleSensitivity_Type()
)
ip2IfBundleSensitivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfBundleSensitivity.setStatus("current")


class _Ip2IfOAMBundleIdent_Type(Integer32):
    """Custom type ip2IfOAMBundleIdent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bundleNumber", 2),
          ("vccvCtrlWord", 3))
    )


_Ip2IfOAMBundleIdent_Type.__name__ = "Integer32"
_Ip2IfOAMBundleIdent_Object = MibTableColumn
ip2IfOAMBundleIdent = _Ip2IfOAMBundleIdent_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 80),
    _Ip2IfOAMBundleIdent_Type()
)
ip2IfOAMBundleIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfOAMBundleIdent.setStatus("current")
_Ip2IfMaxTxQueue_Type = Unsigned32
_Ip2IfMaxTxQueue_Object = MibTableColumn
ip2IfMaxTxQueue = _Ip2IfMaxTxQueue_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 81),
    _Ip2IfMaxTxQueue_Type()
)
ip2IfMaxTxQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMaxTxQueue.setStatus("current")
_Ip2IfMaxGprsTxQueue_Type = Unsigned32
_Ip2IfMaxGprsTxQueue_Object = MibTableColumn
ip2IfMaxGprsTxQueue = _Ip2IfMaxGprsTxQueue_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 82),
    _Ip2IfMaxGprsTxQueue_Type()
)
ip2IfMaxGprsTxQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfMaxGprsTxQueue.setStatus("current")


class _Ip2IfV23HD_Type(Integer32):
    """Custom type ip2IfV23HD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfV23HD_Type.__name__ = "Integer32"
_Ip2IfV23HD_Object = MibTableColumn
ip2IfV23HD = _Ip2IfV23HD_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 83),
    _Ip2IfV23HD_Type()
)
ip2IfV23HD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfV23HD.setStatus("current")
_Ip2IfModemProtocolMode_Type = OctetString
_Ip2IfModemProtocolMode_Object = MibTableColumn
ip2IfModemProtocolMode = _Ip2IfModemProtocolMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 84),
    _Ip2IfModemProtocolMode_Type()
)
ip2IfModemProtocolMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfModemProtocolMode.setStatus("current")
_Ip2IfCdisCngDetectionTime_Type = Unsigned32
_Ip2IfCdisCngDetectionTime_Object = MibTableColumn
ip2IfCdisCngDetectionTime = _Ip2IfCdisCngDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 85),
    _Ip2IfCdisCngDetectionTime_Type()
)
ip2IfCdisCngDetectionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCdisCngDetectionTime.setStatus("current")
_Ip2IfSuperTandemBitMask_Type = OctetString
_Ip2IfSuperTandemBitMask_Object = MibTableColumn
ip2IfSuperTandemBitMask = _Ip2IfSuperTandemBitMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 86),
    _Ip2IfSuperTandemBitMask_Type()
)
ip2IfSuperTandemBitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfSuperTandemBitMask.setStatus("current")
_Ip2IfVbdSwitchbackTime_Type = Unsigned32
_Ip2IfVbdSwitchbackTime_Object = MibTableColumn
ip2IfVbdSwitchbackTime = _Ip2IfVbdSwitchbackTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 87),
    _Ip2IfVbdSwitchbackTime_Type()
)
ip2IfVbdSwitchbackTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfVbdSwitchbackTime.setStatus("current")
_Ip2IfCallerIdTxGain_Type = Integer32
_Ip2IfCallerIdTxGain_Object = MibTableColumn
ip2IfCallerIdTxGain = _Ip2IfCallerIdTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 88),
    _Ip2IfCallerIdTxGain_Type()
)
ip2IfCallerIdTxGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCallerIdTxGain.setStatus("current")
_Ip2IfCallerIdRxGain_Type = Integer32
_Ip2IfCallerIdRxGain_Object = MibTableColumn
ip2IfCallerIdRxGain = _Ip2IfCallerIdRxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 89),
    _Ip2IfCallerIdRxGain_Type()
)
ip2IfCallerIdRxGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCallerIdRxGain.setStatus("current")


class _Ip2IfUdpMuxMethod_Type(Integer32):
    """Custom type ip2IfUdpMuxMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("srcPort", 2),
          ("destPort", 3))
    )


_Ip2IfUdpMuxMethod_Type.__name__ = "Integer32"
_Ip2IfUdpMuxMethod_Object = MibTableColumn
ip2IfUdpMuxMethod = _Ip2IfUdpMuxMethod_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 90),
    _Ip2IfUdpMuxMethod_Type()
)
ip2IfUdpMuxMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfUdpMuxMethod.setStatus("current")


class _Ip2IfCallerIdDetection_Type(Integer32):
    """Custom type ip2IfCallerIdDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfCallerIdDetection_Type.__name__ = "Integer32"
_Ip2IfCallerIdDetection_Object = MibTableColumn
ip2IfCallerIdDetection = _Ip2IfCallerIdDetection_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 91),
    _Ip2IfCallerIdDetection_Type()
)
ip2IfCallerIdDetection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfCallerIdDetection.setStatus("current")


class _Ip2IfWap_Type(Integer32):
    """Custom type ip2IfWap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Ip2IfWap_Type.__name__ = "Integer32"
_Ip2IfWap_Object = MibTableColumn
ip2IfWap = _Ip2IfWap_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 92),
    _Ip2IfWap_Type()
)
ip2IfWap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfWap.setStatus("current")


class _Ip2IfSignalingOos_Type(Integer32):
    """Custom type ip2IfSignalingOos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("forcedIdle", 3),
          ("forcedBusy", 4))
    )


_Ip2IfSignalingOos_Type.__name__ = "Integer32"
_Ip2IfSignalingOos_Object = MibTableColumn
ip2IfSignalingOos = _Ip2IfSignalingOos_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 1, 1, 93),
    _Ip2IfSignalingOos_Type()
)
ip2IfSignalingOos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ip2IfSignalingOos.setStatus("current")
_Ip2IfTDMFrameBytes_Type = Integer32
_Ip2IfTDMFrameBytes_Object = MibScalar
ip2IfTDMFrameBytes = _Ip2IfTDMFrameBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 2),
    _Ip2IfTDMFrameBytes_Type()
)
ip2IfTDMFrameBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfTDMFrameBytes.setStatus("current")
_Ip2IfTosValue_Type = Integer32
_Ip2IfTosValue_Object = MibScalar
ip2IfTosValue = _Ip2IfTosValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 3),
    _Ip2IfTosValue_Type()
)
ip2IfTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfTosValue.setStatus("current")


class _Ip2IfVlanTagging_Type(Integer32):
    """Custom type ip2IfVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Ip2IfVlanTagging_Type.__name__ = "Integer32"
_Ip2IfVlanTagging_Object = MibScalar
ip2IfVlanTagging = _Ip2IfVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 4),
    _Ip2IfVlanTagging_Type()
)
ip2IfVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfVlanTagging.setStatus("current")
_Ip2IfVlanID_Type = Integer32
_Ip2IfVlanID_Object = MibScalar
ip2IfVlanID = _Ip2IfVlanID_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 5),
    _Ip2IfVlanID_Type()
)
ip2IfVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfVlanID.setStatus("current")
_Ip2IfVlanPriority_Type = Integer32
_Ip2IfVlanPriority_Object = MibScalar
ip2IfVlanPriority = _Ip2IfVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 6),
    _Ip2IfVlanPriority_Type()
)
ip2IfVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfVlanPriority.setStatus("current")
_Ip2IfStatTable_Object = MibTable
ip2IfStatTable = _Ip2IfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7)
)
if mibBuilder.loadTexts:
    ip2IfStatTable.setStatus("current")
_Ip2IfStatEntry_Object = MibTableRow
ip2IfStatEntry = _Ip2IfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1)
)
ip2IfStatEntry.setIndexNames(
    (0, "RAD-Ipmux-MIB", "ip2IfStatChIndex"),
)
if mibBuilder.loadTexts:
    ip2IfStatEntry.setStatus("current")
_Ip2IfStatChIndex_Type = Integer32
_Ip2IfStatChIndex_Object = MibTableColumn
ip2IfStatChIndex = _Ip2IfStatChIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 1),
    _Ip2IfStatChIndex_Type()
)
ip2IfStatChIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatChIndex.setStatus("current")
_Ip2IfStatSeqErrors_Type = Integer32
_Ip2IfStatSeqErrors_Object = MibTableColumn
ip2IfStatSeqErrors = _Ip2IfStatSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 2),
    _Ip2IfStatSeqErrors_Type()
)
ip2IfStatSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatSeqErrors.setStatus("current")
_Ip2IfStatBufUnderflows_Type = Integer32
_Ip2IfStatBufUnderflows_Object = MibTableColumn
ip2IfStatBufUnderflows = _Ip2IfStatBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 3),
    _Ip2IfStatBufUnderflows_Type()
)
ip2IfStatBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatBufUnderflows.setStatus("current")
_Ip2IfStatBufOverflows_Type = Integer32
_Ip2IfStatBufOverflows_Object = MibTableColumn
ip2IfStatBufOverflows = _Ip2IfStatBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 4),
    _Ip2IfStatBufOverflows_Type()
)
ip2IfStatBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatBufOverflows.setStatus("current")
_Ip2IfStatTxOnTimeInterval_Type = Counter32
_Ip2IfStatTxOnTimeInterval_Object = MibTableColumn
ip2IfStatTxOnTimeInterval = _Ip2IfStatTxOnTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 5),
    _Ip2IfStatTxOnTimeInterval_Type()
)
ip2IfStatTxOnTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatTxOnTimeInterval.setStatus("current")
_Ip2IfStatTxOnMaxSize_Type = Counter32
_Ip2IfStatTxOnMaxSize_Object = MibTableColumn
ip2IfStatTxOnMaxSize = _Ip2IfStatTxOnMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 6),
    _Ip2IfStatTxOnMaxSize_Type()
)
ip2IfStatTxOnMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatTxOnMaxSize.setStatus("current")
_Ip2IfStatRxSignaling_Type = Counter32
_Ip2IfStatRxSignaling_Object = MibTableColumn
ip2IfStatRxSignaling = _Ip2IfStatRxSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 7),
    _Ip2IfStatRxSignaling_Type()
)
ip2IfStatRxSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRxSignaling.setStatus("current")
_Ip2IfStatRxVoice_Type = Counter32
_Ip2IfStatRxVoice_Object = MibTableColumn
ip2IfStatRxVoice = _Ip2IfStatRxVoice_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 8),
    _Ip2IfStatRxVoice_Type()
)
ip2IfStatRxVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRxVoice.setStatus("current")
_Ip2IfStatRxHdlc_Type = Counter32
_Ip2IfStatRxHdlc_Object = MibTableColumn
ip2IfStatRxHdlc = _Ip2IfStatRxHdlc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 9),
    _Ip2IfStatRxHdlc_Type()
)
ip2IfStatRxHdlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRxHdlc.setStatus("current")
_Ip2IfStatTxSignaling_Type = Counter32
_Ip2IfStatTxSignaling_Object = MibTableColumn
ip2IfStatTxSignaling = _Ip2IfStatTxSignaling_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 10),
    _Ip2IfStatTxSignaling_Type()
)
ip2IfStatTxSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatTxSignaling.setStatus("current")
_Ip2IfStatTxVoice_Type = Counter32
_Ip2IfStatTxVoice_Object = MibTableColumn
ip2IfStatTxVoice = _Ip2IfStatTxVoice_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 11),
    _Ip2IfStatTxVoice_Type()
)
ip2IfStatTxVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatTxVoice.setStatus("current")
_Ip2IfStatTxHdlc_Type = Counter32
_Ip2IfStatTxHdlc_Object = MibTableColumn
ip2IfStatTxHdlc = _Ip2IfStatTxHdlc_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 12),
    _Ip2IfStatTxHdlc_Type()
)
ip2IfStatTxHdlc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatTxHdlc.setStatus("current")
_Ip2IfStatRdnFlip_Type = Counter32
_Ip2IfStatRdnFlip_Object = MibTableColumn
ip2IfStatRdnFlip = _Ip2IfStatRdnFlip_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 13),
    _Ip2IfStatRdnFlip_Type()
)
ip2IfStatRdnFlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRdnFlip.setStatus("current")


class _Ip2IfFarEndTdmStatus_Type(Integer32):
    """Custom type ip2IfFarEndTdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Ip2IfFarEndTdmStatus_Type.__name__ = "Integer32"
_Ip2IfFarEndTdmStatus_Object = MibTableColumn
ip2IfFarEndTdmStatus = _Ip2IfFarEndTdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 14),
    _Ip2IfFarEndTdmStatus_Type()
)
ip2IfFarEndTdmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfFarEndTdmStatus.setStatus("current")
_Ip2IfStatPsnTxFrames_Type = Counter32
_Ip2IfStatPsnTxFrames_Object = MibTableColumn
ip2IfStatPsnTxFrames = _Ip2IfStatPsnTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 15),
    _Ip2IfStatPsnTxFrames_Type()
)
ip2IfStatPsnTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatPsnTxFrames.setStatus("current")
_Ip2IfStatPsnRxFrames_Type = Counter32
_Ip2IfStatPsnRxFrames_Object = MibTableColumn
ip2IfStatPsnRxFrames = _Ip2IfStatPsnRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 16),
    _Ip2IfStatPsnRxFrames_Type()
)
ip2IfStatPsnRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatPsnRxFrames.setStatus("current")
_Ip2IfStatMinJittBufLevel_Type = Unsigned32
_Ip2IfStatMinJittBufLevel_Object = MibTableColumn
ip2IfStatMinJittBufLevel = _Ip2IfStatMinJittBufLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 17),
    _Ip2IfStatMinJittBufLevel_Type()
)
ip2IfStatMinJittBufLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatMinJittBufLevel.setStatus("current")
_Ip2IfStatMaxJittBufLevel_Type = Unsigned32
_Ip2IfStatMaxJittBufLevel_Object = MibTableColumn
ip2IfStatMaxJittBufLevel = _Ip2IfStatMaxJittBufLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 18),
    _Ip2IfStatMaxJittBufLevel_Type()
)
ip2IfStatMaxJittBufLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatMaxJittBufLevel.setStatus("current")
_Ip2IfStatRecommendedJittBufSize_Type = Unsigned32
_Ip2IfStatRecommendedJittBufSize_Object = MibTableColumn
ip2IfStatRecommendedJittBufSize = _Ip2IfStatRecommendedJittBufSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 19),
    _Ip2IfStatRecommendedJittBufSize_Type()
)
ip2IfStatRecommendedJittBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRecommendedJittBufSize.setStatus("current")
_Ip2IfStatPsnSeqErrors_Type = Counter32
_Ip2IfStatPsnSeqErrors_Object = MibTableColumn
ip2IfStatPsnSeqErrors = _Ip2IfStatPsnSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 20),
    _Ip2IfStatPsnSeqErrors_Type()
)
ip2IfStatPsnSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatPsnSeqErrors.setStatus("current")
_Ip2IfStatPsnReorderFrames_Type = Counter32
_Ip2IfStatPsnReorderFrames_Object = MibTableColumn
ip2IfStatPsnReorderFrames = _Ip2IfStatPsnReorderFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 21),
    _Ip2IfStatPsnReorderFrames_Type()
)
ip2IfStatPsnReorderFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatPsnReorderFrames.setStatus("current")
_Ip2IfStatMinRoundTripDelay_Type = Unsigned32
_Ip2IfStatMinRoundTripDelay_Object = MibTableColumn
ip2IfStatMinRoundTripDelay = _Ip2IfStatMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 22),
    _Ip2IfStatMinRoundTripDelay_Type()
)
ip2IfStatMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatMinRoundTripDelay.setStatus("current")
_Ip2IfStatMaxRoundTripDelay_Type = Unsigned32
_Ip2IfStatMaxRoundTripDelay_Object = MibTableColumn
ip2IfStatMaxRoundTripDelay = _Ip2IfStatMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 23),
    _Ip2IfStatMaxRoundTripDelay_Type()
)
ip2IfStatMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatMaxRoundTripDelay.setStatus("current")
_Ip2IfStatAvrRoundTripDelay_Type = Unsigned32
_Ip2IfStatAvrRoundTripDelay_Object = MibTableColumn
ip2IfStatAvrRoundTripDelay = _Ip2IfStatAvrRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 24),
    _Ip2IfStatAvrRoundTripDelay_Type()
)
ip2IfStatAvrRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatAvrRoundTripDelay.setStatus("current")
_Ip2IfStatFrameTrackDupDrop_Type = Counter32
_Ip2IfStatFrameTrackDupDrop_Object = MibTableColumn
ip2IfStatFrameTrackDupDrop = _Ip2IfStatFrameTrackDupDrop_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 25),
    _Ip2IfStatFrameTrackDupDrop_Type()
)
ip2IfStatFrameTrackDupDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatFrameTrackDupDrop.setStatus("current")
_Ip2IfStatFrameTrackMissing_Type = Counter32
_Ip2IfStatFrameTrackMissing_Object = MibTableColumn
ip2IfStatFrameTrackMissing = _Ip2IfStatFrameTrackMissing_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 26),
    _Ip2IfStatFrameTrackMissing_Type()
)
ip2IfStatFrameTrackMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatFrameTrackMissing.setStatus("current")
_Ip2IfStatFrameTrackLongSerMiss_Type = Integer32
_Ip2IfStatFrameTrackLongSerMiss_Object = MibTableColumn
ip2IfStatFrameTrackLongSerMiss = _Ip2IfStatFrameTrackLongSerMiss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 27),
    _Ip2IfStatFrameTrackLongSerMiss_Type()
)
ip2IfStatFrameTrackLongSerMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatFrameTrackLongSerMiss.setStatus("current")
_Ip2IfStatTxMeasuredSilence_Type = Integer32
_Ip2IfStatTxMeasuredSilence_Object = MibTableColumn
ip2IfStatTxMeasuredSilence = _Ip2IfStatTxMeasuredSilence_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 28),
    _Ip2IfStatTxMeasuredSilence_Type()
)
ip2IfStatTxMeasuredSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatTxMeasuredSilence.setStatus("current")
_Ip2IfStatRxMeasuredSilence_Type = Integer32
_Ip2IfStatRxMeasuredSilence_Object = MibTableColumn
ip2IfStatRxMeasuredSilence = _Ip2IfStatRxMeasuredSilence_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 29),
    _Ip2IfStatRxMeasuredSilence_Type()
)
ip2IfStatRxMeasuredSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRxMeasuredSilence.setStatus("current")
_Ip2IfStatHdlcCrcErr_Type = Counter32
_Ip2IfStatHdlcCrcErr_Object = MibTableColumn
ip2IfStatHdlcCrcErr = _Ip2IfStatHdlcCrcErr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 30),
    _Ip2IfStatHdlcCrcErr_Type()
)
ip2IfStatHdlcCrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatHdlcCrcErr.setStatus("current")
_Ip2IfStatHdlcAlignErr_Type = Counter32
_Ip2IfStatHdlcAlignErr_Object = MibTableColumn
ip2IfStatHdlcAlignErr = _Ip2IfStatHdlcAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 31),
    _Ip2IfStatHdlcAlignErr_Type()
)
ip2IfStatHdlcAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatHdlcAlignErr.setStatus("current")
_Ip2IfStatHdlcOversize_Type = Counter32
_Ip2IfStatHdlcOversize_Object = MibTableColumn
ip2IfStatHdlcOversize = _Ip2IfStatHdlcOversize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 32),
    _Ip2IfStatHdlcOversize_Type()
)
ip2IfStatHdlcOversize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatHdlcOversize.setStatus("current")
_Ip2IfStatHdlcUndersize_Type = Counter32
_Ip2IfStatHdlcUndersize_Object = MibTableColumn
ip2IfStatHdlcUndersize = _Ip2IfStatHdlcUndersize_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 33),
    _Ip2IfStatHdlcUndersize_Type()
)
ip2IfStatHdlcUndersize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatHdlcUndersize.setStatus("current")
_Ip2IfStatHdlcAbort_Type = Counter32
_Ip2IfStatHdlcAbort_Object = MibTableColumn
ip2IfStatHdlcAbort = _Ip2IfStatHdlcAbort_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 34),
    _Ip2IfStatHdlcAbort_Type()
)
ip2IfStatHdlcAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatHdlcAbort.setStatus("current")
_Ip2IfStatRxCorrectFrames_Type = Counter32
_Ip2IfStatRxCorrectFrames_Object = MibTableColumn
ip2IfStatRxCorrectFrames = _Ip2IfStatRxCorrectFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 35),
    _Ip2IfStatRxCorrectFrames_Type()
)
ip2IfStatRxCorrectFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatRxCorrectFrames.setStatus("current")
_Ip2IfStatHdlcErroredFrames_Type = Counter32
_Ip2IfStatHdlcErroredFrames_Object = MibTableColumn
ip2IfStatHdlcErroredFrames = _Ip2IfStatHdlcErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 7, 1, 36),
    _Ip2IfStatHdlcErroredFrames_Type()
)
ip2IfStatHdlcErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfStatHdlcErroredFrames.setStatus("current")
_Ip2IfRateLimit_Type = Integer32
_Ip2IfRateLimit_Object = MibScalar
ip2IfRateLimit = _Ip2IfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 8),
    _Ip2IfRateLimit_Type()
)
ip2IfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfRateLimit.setStatus("current")
_Ip2IfPortTable_Object = MibTable
ip2IfPortTable = _Ip2IfPortTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 9)
)
if mibBuilder.loadTexts:
    ip2IfPortTable.setStatus("current")
_Ip2IfPortEntry_Object = MibTableRow
ip2IfPortEntry = _Ip2IfPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 9, 1)
)
ip2IfPortEntry.setIndexNames(
    (0, "RAD-Ipmux-MIB", "ip2IfPortIndex"),
)
if mibBuilder.loadTexts:
    ip2IfPortEntry.setStatus("current")
_Ip2IfPortIndex_Type = Integer32
_Ip2IfPortIndex_Object = MibTableColumn
ip2IfPortIndex = _Ip2IfPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 9, 1, 1),
    _Ip2IfPortIndex_Type()
)
ip2IfPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfPortIndex.setStatus("current")
_Ip2IfPortUsage_Type = Integer32
_Ip2IfPortUsage_Object = MibTableColumn
ip2IfPortUsage = _Ip2IfPortUsage_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 9, 1, 2),
    _Ip2IfPortUsage_Type()
)
ip2IfPortUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfPortUsage.setStatus("current")


class _Ip2IfPortMask_Type(Integer32):
    """Custom type ip2IfPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("dontMask", 2),
          ("mask", 3))
    )


_Ip2IfPortMask_Type.__name__ = "Integer32"
_Ip2IfPortMask_Object = MibTableColumn
ip2IfPortMask = _Ip2IfPortMask_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 9, 1, 3),
    _Ip2IfPortMask_Type()
)
ip2IfPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfPortMask.setStatus("current")
_Ip2IfPortTotalThroughput_Type = Integer32
_Ip2IfPortTotalThroughput_Object = MibTableColumn
ip2IfPortTotalThroughput = _Ip2IfPortTotalThroughput_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 9, 1, 4),
    _Ip2IfPortTotalThroughput_Type()
)
ip2IfPortTotalThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfPortTotalThroughput.setStatus("current")
_Ip2IfCurrentStatTable_Object = MibTable
ip2IfCurrentStatTable = _Ip2IfCurrentStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10)
)
if mibBuilder.loadTexts:
    ip2IfCurrentStatTable.setStatus("current")
_Ip2IfCurrentStatEntry_Object = MibTableRow
ip2IfCurrentStatEntry = _Ip2IfCurrentStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1)
)
ip2IfCurrentStatEntry.setIndexNames(
    (0, "RAD-Ipmux-MIB", "ip2IfChannelIndex"),
)
if mibBuilder.loadTexts:
    ip2IfCurrentStatEntry.setStatus("current")
_Ip2IfCurrentStatSeqErrors_Type = Counter32
_Ip2IfCurrentStatSeqErrors_Object = MibTableColumn
ip2IfCurrentStatSeqErrors = _Ip2IfCurrentStatSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 1),
    _Ip2IfCurrentStatSeqErrors_Type()
)
ip2IfCurrentStatSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatSeqErrors.setStatus("current")
_Ip2IfCurrentStatBufUnderflows_Type = Counter32
_Ip2IfCurrentStatBufUnderflows_Object = MibTableColumn
ip2IfCurrentStatBufUnderflows = _Ip2IfCurrentStatBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 2),
    _Ip2IfCurrentStatBufUnderflows_Type()
)
ip2IfCurrentStatBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatBufUnderflows.setStatus("current")
_Ip2IfCurrentStatBufOverflows_Type = Counter32
_Ip2IfCurrentStatBufOverflows_Object = MibTableColumn
ip2IfCurrentStatBufOverflows = _Ip2IfCurrentStatBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 3),
    _Ip2IfCurrentStatBufOverflows_Type()
)
ip2IfCurrentStatBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatBufOverflows.setStatus("current")
_Ip2IfCurrentStatMaxDelayVar_Type = Integer32
_Ip2IfCurrentStatMaxDelayVar_Object = MibTableColumn
ip2IfCurrentStatMaxDelayVar = _Ip2IfCurrentStatMaxDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 4),
    _Ip2IfCurrentStatMaxDelayVar_Type()
)
ip2IfCurrentStatMaxDelayVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatMaxDelayVar.setStatus("current")
_Ip2IfCurrentStatMinJittBufLevel_Type = Unsigned32
_Ip2IfCurrentStatMinJittBufLevel_Object = MibTableColumn
ip2IfCurrentStatMinJittBufLevel = _Ip2IfCurrentStatMinJittBufLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 5),
    _Ip2IfCurrentStatMinJittBufLevel_Type()
)
ip2IfCurrentStatMinJittBufLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatMinJittBufLevel.setStatus("current")
_Ip2IfCurrentStatMaxJittBufLevel_Type = Unsigned32
_Ip2IfCurrentStatMaxJittBufLevel_Object = MibTableColumn
ip2IfCurrentStatMaxJittBufLevel = _Ip2IfCurrentStatMaxJittBufLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 6),
    _Ip2IfCurrentStatMaxJittBufLevel_Type()
)
ip2IfCurrentStatMaxJittBufLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatMaxJittBufLevel.setStatus("current")
_Ip2IfCurrentStatTxErrFrameSec_Type = Counter32
_Ip2IfCurrentStatTxErrFrameSec_Object = MibTableColumn
ip2IfCurrentStatTxErrFrameSec = _Ip2IfCurrentStatTxErrFrameSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 10, 1, 7),
    _Ip2IfCurrentStatTxErrFrameSec_Type()
)
ip2IfCurrentStatTxErrFrameSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfCurrentStatTxErrFrameSec.setStatus("current")
_Ip2IfIntervalStatTable_Object = MibTable
ip2IfIntervalStatTable = _Ip2IfIntervalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11)
)
if mibBuilder.loadTexts:
    ip2IfIntervalStatTable.setStatus("current")
_Ip2IfIntervalStatEntry_Object = MibTableRow
ip2IfIntervalStatEntry = _Ip2IfIntervalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1)
)
ip2IfIntervalStatEntry.setIndexNames(
    (0, "RAD-Ipmux-MIB", "ip2IfChannelIndex"),
    (0, "RAD-Ipmux-MIB", "ip2IfIntervalStatIndex"),
)
if mibBuilder.loadTexts:
    ip2IfIntervalStatEntry.setStatus("current")
_Ip2IfIntervalStatIndex_Type = Integer32
_Ip2IfIntervalStatIndex_Object = MibTableColumn
ip2IfIntervalStatIndex = _Ip2IfIntervalStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 1),
    _Ip2IfIntervalStatIndex_Type()
)
ip2IfIntervalStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatIndex.setStatus("current")
_Ip2IfIntervalStatSeqErrors_Type = Counter32
_Ip2IfIntervalStatSeqErrors_Object = MibTableColumn
ip2IfIntervalStatSeqErrors = _Ip2IfIntervalStatSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 2),
    _Ip2IfIntervalStatSeqErrors_Type()
)
ip2IfIntervalStatSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatSeqErrors.setStatus("current")
_Ip2IfIntervalStatBufUnderflows_Type = Counter32
_Ip2IfIntervalStatBufUnderflows_Object = MibTableColumn
ip2IfIntervalStatBufUnderflows = _Ip2IfIntervalStatBufUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 3),
    _Ip2IfIntervalStatBufUnderflows_Type()
)
ip2IfIntervalStatBufUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatBufUnderflows.setStatus("current")
_Ip2IfIntervalStatBufOverflows_Type = Counter32
_Ip2IfIntervalStatBufOverflows_Object = MibTableColumn
ip2IfIntervalStatBufOverflows = _Ip2IfIntervalStatBufOverflows_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 4),
    _Ip2IfIntervalStatBufOverflows_Type()
)
ip2IfIntervalStatBufOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatBufOverflows.setStatus("current")
_Ip2IfIntervalStatMaxDelayVar_Type = Integer32
_Ip2IfIntervalStatMaxDelayVar_Object = MibTableColumn
ip2IfIntervalStatMaxDelayVar = _Ip2IfIntervalStatMaxDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 5),
    _Ip2IfIntervalStatMaxDelayVar_Type()
)
ip2IfIntervalStatMaxDelayVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatMaxDelayVar.setStatus("current")
_Ip2IfIntervalStatMinJittBufLevel_Type = Unsigned32
_Ip2IfIntervalStatMinJittBufLevel_Object = MibTableColumn
ip2IfIntervalStatMinJittBufLevel = _Ip2IfIntervalStatMinJittBufLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 6),
    _Ip2IfIntervalStatMinJittBufLevel_Type()
)
ip2IfIntervalStatMinJittBufLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatMinJittBufLevel.setStatus("current")
_Ip2IfIntervalStatMaxJittBufLevel_Type = Unsigned32
_Ip2IfIntervalStatMaxJittBufLevel_Object = MibTableColumn
ip2IfIntervalStatMaxJittBufLevel = _Ip2IfIntervalStatMaxJittBufLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 7),
    _Ip2IfIntervalStatMaxJittBufLevel_Type()
)
ip2IfIntervalStatMaxJittBufLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatMaxJittBufLevel.setStatus("current")
_Ip2IfIntervalStatTxErrFrameSec_Type = Counter32
_Ip2IfIntervalStatTxErrFrameSec_Object = MibTableColumn
ip2IfIntervalStatTxErrFrameSec = _Ip2IfIntervalStatTxErrFrameSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 11, 1, 8),
    _Ip2IfIntervalStatTxErrFrameSec_Type()
)
ip2IfIntervalStatTxErrFrameSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip2IfIntervalStatTxErrFrameSec.setStatus("current")


class _Ip2IfLogEvents_Type(Integer32):
    """Custom type ip2IfLogEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("all", 2),
          ("oneMinStep", 3))
    )


_Ip2IfLogEvents_Type.__name__ = "Integer32"
_Ip2IfLogEvents_Object = MibScalar
ip2IfLogEvents = _Ip2IfLogEvents_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 12),
    _Ip2IfLogEvents_Type()
)
ip2IfLogEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfLogEvents.setStatus("current")


class _Ip2IfEthSwitchMode_Type(Integer32):
    """Custom type ip2IfEthSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("unTagged", 2),
          ("tagged", 3))
    )


_Ip2IfEthSwitchMode_Type.__name__ = "Integer32"
_Ip2IfEthSwitchMode_Object = MibScalar
ip2IfEthSwitchMode = _Ip2IfEthSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 7, 13),
    _Ip2IfEthSwitchMode_Type()
)
ip2IfEthSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ip2IfEthSwitchMode.setStatus("current")

# Managed Objects groups


# Notification objects

alarmStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 5)
)
alarmStatusTrap.setObjects(
    ("RAD-NtePrtCo-MIB", "atmInterfaceAlarmStatus")
)
if mibBuilder.loadTexts:
    alarmStatusTrap.setStatus(
        "current"
    )

systemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 6)
)
systemTrap.setObjects(
      *(("RAD-Ipmux-MIB", "atmNteEventType"),
        ("RAD-GEN-MIB", "agnLed"),
        ("RAD-Ipmux-MIB", "alarmSeverity"))
)
if mibBuilder.loadTexts:
    systemTrap.setStatus(
        "current"
    )

alarmLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 7)
)
alarmLOS.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    alarmLOS.setStatus(
        "current"
    )

alarmLOF = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 8)
)
alarmLOF.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    alarmLOF.setStatus(
        "current"
    )

channelOperStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 9)
)
channelOperStatusTrap.setObjects(
    ("RAD-Ipmux-MIB", "ip2IfOperStatus")
)
if mibBuilder.loadTexts:
    channelOperStatusTrap.setStatus(
        "current"
    )

alarmAIS = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 10)
)
alarmAIS.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    alarmAIS.setStatus(
        "current"
    )

alarmRDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 11)
)
alarmRDI.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    alarmRDI.setStatus(
        "current"
    )

alarmFEBE = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 12)
)
alarmFEBE.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    alarmFEBE.setStatus(
        "current"
    )

localConnStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 13)
)
localConnStatusTrap.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    localConnStatusTrap.setStatus(
        "current"
    )

remoteConnStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 14)
)
remoteConnStatusTrap.setObjects(
      *(("RAD-Ipmux-MIB", "alarmSeverity"),
        ("RAD-Ipmux-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    remoteConnStatusTrap.setStatus(
        "current"
    )

bundleConnectionStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 3, 0, 15)
)
bundleConnectionStatusTrap.setObjects(
      *(("IF-MIB", "ifAlias"),
        ("RAD-Ipmux-MIB", "ip2IfOperStatus"))
)
if mibBuilder.loadTexts:
    bundleConnectionStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-Ipmux-MIB",
    **{"ip2If": ip2If,
       "ip2IfTable": ip2IfTable,
       "ip2IfEntry": ip2IfEntry,
       "ip2IfChannelIndex": ip2IfChannelIndex,
       "ip2IfRowStatus": ip2IfRowStatus,
       "ip2IfOperStatus": ip2IfOperStatus,
       "ip2IfAdminStatus": ip2IfAdminStatus,
       "ip2IfDestAddr": ip2IfDestAddr,
       "ip2IfNextHop": ip2IfNextHop,
       "ip2IfDestPort": ip2IfDestPort,
       "ip2IfMacAddr": ip2IfMacAddr,
       "ip2IfJitterBuffer": ip2IfJitterBuffer,
       "ip2IfTos": ip2IfTos,
       "ip2IfTDMBytesInFrame": ip2IfTDMBytesInFrame,
       "ip2IfVlanSupport": ip2IfVlanSupport,
       "ip2IfVlanIdentifier": ip2IfVlanIdentifier,
       "ip2IfVlanFramePriority": ip2IfVlanFramePriority,
       "ip2IfExitPort": ip2IfExitPort,
       "ip2IfVoiceOos": ip2IfVoiceOos,
       "ip2IfDataOos": ip2IfDataOos,
       "ip2IfBundleUsage": ip2IfBundleUsage,
       "ip2IfOAM": ip2IfOAM,
       "ip2IfTDMoIpMode": ip2IfTDMoIpMode,
       "ip2IfTimeElapsed": ip2IfTimeElapsed,
       "ip2IfValidIntervals": ip2IfValidIntervals,
       "ip2IfFarEndType": ip2IfFarEndType,
       "ip2IfRdnState": ip2IfRdnState,
       "ip2IfSourceAddr": ip2IfSourceAddr,
       "ip2IfBandWidth": ip2IfBandWidth,
       "ip2IfMeasuredSilence": ip2IfMeasuredSilence,
       "ip2IfPayloadType": ip2IfPayloadType,
       "ip2IfProtocolVersion": ip2IfProtocolVersion,
       "ip2IfTdmBackUpNextHop": ip2IfTdmBackUpNextHop,
       "ip2IfOosTxEnable": ip2IfOosTxEnable,
       "ip2IfConnCheckPktFrequency": ip2IfConnCheckPktFrequency,
       "ip2IfConnPktTimeOutCycles": ip2IfConnPktTimeOutCycles,
       "ip2IfMfRelay": ip2IfMfRelay,
       "ip2IfTxGain": ip2IfTxGain,
       "ip2IfSuperTandem": ip2IfSuperTandem,
       "ip2IfSrcPort": ip2IfSrcPort,
       "ip2IfModemCalls": ip2IfModemCalls,
       "ip2IfMinPulseWidth": ip2IfMinPulseWidth,
       "ip2IfMinPowerLevel": ip2IfMinPowerLevel,
       "ip2IfEchoCanceler": ip2IfEchoCanceler,
       "ip2IfCodingLaw": ip2IfCodingLaw,
       "ip2IfCustomToneDetect": ip2IfCustomToneDetect,
       "ip2IfCallerIdDelay": ip2IfCallerIdDelay,
       "ip2IfConnectivityMode": ip2IfConnectivityMode,
       "ip2IfClockSourceEnable": ip2IfClockSourceEnable,
       "ip2IfNetworkType": ip2IfNetworkType,
       "ip2IfMplsRxLabelEnable": ip2IfMplsRxLabelEnable,
       "ip2IfMplsRxLabel": ip2IfMplsRxLabel,
       "ip2IfMplsTxLabelEnable": ip2IfMplsTxLabelEnable,
       "ip2IfMplsTxLabel": ip2IfMplsTxLabel,
       "ip2IfMplsTxExpBits": ip2IfMplsTxExpBits,
       "ip2IfMfcSpoofing": ip2IfMfcSpoofing,
       "ip2IfToneAckInterval": ip2IfToneAckInterval,
       "ip2IfNextHopType": ip2IfNextHopType,
       "ip2IfNoiseLevelForVAD": ip2IfNoiseLevelForVAD,
       "ip2IfClockPreferences": ip2IfClockPreferences,
       "ip2IfConnectionMode": ip2IfConnectionMode,
       "ip2IfRingBack": ip2IfRingBack,
       "ip2IfReversePolarity": ip2IfReversePolarity,
       "ip2IfPulseMeter": ip2IfPulseMeter,
       "ip2IfPulseMeterFreq": ip2IfPulseMeterFreq,
       "ip2IfPulseMeterPeriod": ip2IfPulseMeterPeriod,
       "ip2IfOnHookDetect": ip2IfOnHookDetect,
       "ip2IfComfortNoiseGen": ip2IfComfortNoiseGen,
       "ip2IfExitChannel": ip2IfExitChannel,
       "ip2IfMaxVBDModemCalls": ip2IfMaxVBDModemCalls,
       "ip2IfMaxRelayModemCalls": ip2IfMaxRelayModemCalls,
       "ip2IfCustomToneFrequency": ip2IfCustomToneFrequency,
       "ip2IfVadMethod": ip2IfVadMethod,
       "ip2IfRxGain": ip2IfRxGain,
       "ip2IfCallerIDType": ip2IfCallerIDType,
       "ip2IfPeerAddrType": ip2IfPeerAddrType,
       "ip2IfVbdRate": ip2IfVbdRate,
       "ip2IfDtmfDetection": ip2IfDtmfDetection,
       "ip2IfNlpCutoffLevel": ip2IfNlpCutoffLevel,
       "ip2IfDtdErlRatioCutoffQ3": ip2IfDtdErlRatioCutoffQ3,
       "ip2IfCASRedundancy": ip2IfCASRedundancy,
       "ip2IfBundleSensitivity": ip2IfBundleSensitivity,
       "ip2IfOAMBundleIdent": ip2IfOAMBundleIdent,
       "ip2IfMaxTxQueue": ip2IfMaxTxQueue,
       "ip2IfMaxGprsTxQueue": ip2IfMaxGprsTxQueue,
       "ip2IfV23HD": ip2IfV23HD,
       "ip2IfModemProtocolMode": ip2IfModemProtocolMode,
       "ip2IfCdisCngDetectionTime": ip2IfCdisCngDetectionTime,
       "ip2IfSuperTandemBitMask": ip2IfSuperTandemBitMask,
       "ip2IfVbdSwitchbackTime": ip2IfVbdSwitchbackTime,
       "ip2IfCallerIdTxGain": ip2IfCallerIdTxGain,
       "ip2IfCallerIdRxGain": ip2IfCallerIdRxGain,
       "ip2IfUdpMuxMethod": ip2IfUdpMuxMethod,
       "ip2IfCallerIdDetection": ip2IfCallerIdDetection,
       "ip2IfWap": ip2IfWap,
       "ip2IfSignalingOos": ip2IfSignalingOos,
       "ip2IfTDMFrameBytes": ip2IfTDMFrameBytes,
       "ip2IfTosValue": ip2IfTosValue,
       "ip2IfVlanTagging": ip2IfVlanTagging,
       "ip2IfVlanID": ip2IfVlanID,
       "ip2IfVlanPriority": ip2IfVlanPriority,
       "ip2IfStatTable": ip2IfStatTable,
       "ip2IfStatEntry": ip2IfStatEntry,
       "ip2IfStatChIndex": ip2IfStatChIndex,
       "ip2IfStatSeqErrors": ip2IfStatSeqErrors,
       "ip2IfStatBufUnderflows": ip2IfStatBufUnderflows,
       "ip2IfStatBufOverflows": ip2IfStatBufOverflows,
       "ip2IfStatTxOnTimeInterval": ip2IfStatTxOnTimeInterval,
       "ip2IfStatTxOnMaxSize": ip2IfStatTxOnMaxSize,
       "ip2IfStatRxSignaling": ip2IfStatRxSignaling,
       "ip2IfStatRxVoice": ip2IfStatRxVoice,
       "ip2IfStatRxHdlc": ip2IfStatRxHdlc,
       "ip2IfStatTxSignaling": ip2IfStatTxSignaling,
       "ip2IfStatTxVoice": ip2IfStatTxVoice,
       "ip2IfStatTxHdlc": ip2IfStatTxHdlc,
       "ip2IfStatRdnFlip": ip2IfStatRdnFlip,
       "ip2IfFarEndTdmStatus": ip2IfFarEndTdmStatus,
       "ip2IfStatPsnTxFrames": ip2IfStatPsnTxFrames,
       "ip2IfStatPsnRxFrames": ip2IfStatPsnRxFrames,
       "ip2IfStatMinJittBufLevel": ip2IfStatMinJittBufLevel,
       "ip2IfStatMaxJittBufLevel": ip2IfStatMaxJittBufLevel,
       "ip2IfStatRecommendedJittBufSize": ip2IfStatRecommendedJittBufSize,
       "ip2IfStatPsnSeqErrors": ip2IfStatPsnSeqErrors,
       "ip2IfStatPsnReorderFrames": ip2IfStatPsnReorderFrames,
       "ip2IfStatMinRoundTripDelay": ip2IfStatMinRoundTripDelay,
       "ip2IfStatMaxRoundTripDelay": ip2IfStatMaxRoundTripDelay,
       "ip2IfStatAvrRoundTripDelay": ip2IfStatAvrRoundTripDelay,
       "ip2IfStatFrameTrackDupDrop": ip2IfStatFrameTrackDupDrop,
       "ip2IfStatFrameTrackMissing": ip2IfStatFrameTrackMissing,
       "ip2IfStatFrameTrackLongSerMiss": ip2IfStatFrameTrackLongSerMiss,
       "ip2IfStatTxMeasuredSilence": ip2IfStatTxMeasuredSilence,
       "ip2IfStatRxMeasuredSilence": ip2IfStatRxMeasuredSilence,
       "ip2IfStatHdlcCrcErr": ip2IfStatHdlcCrcErr,
       "ip2IfStatHdlcAlignErr": ip2IfStatHdlcAlignErr,
       "ip2IfStatHdlcOversize": ip2IfStatHdlcOversize,
       "ip2IfStatHdlcUndersize": ip2IfStatHdlcUndersize,
       "ip2IfStatHdlcAbort": ip2IfStatHdlcAbort,
       "ip2IfStatRxCorrectFrames": ip2IfStatRxCorrectFrames,
       "ip2IfStatHdlcErroredFrames": ip2IfStatHdlcErroredFrames,
       "ip2IfRateLimit": ip2IfRateLimit,
       "ip2IfPortTable": ip2IfPortTable,
       "ip2IfPortEntry": ip2IfPortEntry,
       "ip2IfPortIndex": ip2IfPortIndex,
       "ip2IfPortUsage": ip2IfPortUsage,
       "ip2IfPortMask": ip2IfPortMask,
       "ip2IfPortTotalThroughput": ip2IfPortTotalThroughput,
       "ip2IfCurrentStatTable": ip2IfCurrentStatTable,
       "ip2IfCurrentStatEntry": ip2IfCurrentStatEntry,
       "ip2IfCurrentStatSeqErrors": ip2IfCurrentStatSeqErrors,
       "ip2IfCurrentStatBufUnderflows": ip2IfCurrentStatBufUnderflows,
       "ip2IfCurrentStatBufOverflows": ip2IfCurrentStatBufOverflows,
       "ip2IfCurrentStatMaxDelayVar": ip2IfCurrentStatMaxDelayVar,
       "ip2IfCurrentStatMinJittBufLevel": ip2IfCurrentStatMinJittBufLevel,
       "ip2IfCurrentStatMaxJittBufLevel": ip2IfCurrentStatMaxJittBufLevel,
       "ip2IfCurrentStatTxErrFrameSec": ip2IfCurrentStatTxErrFrameSec,
       "ip2IfIntervalStatTable": ip2IfIntervalStatTable,
       "ip2IfIntervalStatEntry": ip2IfIntervalStatEntry,
       "ip2IfIntervalStatIndex": ip2IfIntervalStatIndex,
       "ip2IfIntervalStatSeqErrors": ip2IfIntervalStatSeqErrors,
       "ip2IfIntervalStatBufUnderflows": ip2IfIntervalStatBufUnderflows,
       "ip2IfIntervalStatBufOverflows": ip2IfIntervalStatBufOverflows,
       "ip2IfIntervalStatMaxDelayVar": ip2IfIntervalStatMaxDelayVar,
       "ip2IfIntervalStatMinJittBufLevel": ip2IfIntervalStatMinJittBufLevel,
       "ip2IfIntervalStatMaxJittBufLevel": ip2IfIntervalStatMaxJittBufLevel,
       "ip2IfIntervalStatTxErrFrameSec": ip2IfIntervalStatTxErrFrameSec,
       "ip2IfLogEvents": ip2IfLogEvents,
       "ip2IfEthSwitchMode": ip2IfEthSwitchMode,
       "alarmStatusTrap": alarmStatusTrap,
       "systemTrap": systemTrap,
       "alarmLOS": alarmLOS,
       "alarmLOF": alarmLOF,
       "channelOperStatusTrap": channelOperStatusTrap,
       "alarmAIS": alarmAIS,
       "alarmRDI": alarmRDI,
       "alarmFEBE": alarmFEBE,
       "localConnStatusTrap": localConnStatusTrap,
       "remoteConnStatusTrap": remoteConnStatusTrap,
       "bundleConnectionStatusTrap": bundleConnectionStatusTrap}
)
