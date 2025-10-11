# SNMP MIB module (OS-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-PTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:08 2025
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
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22)
)
if mibBuilder.loadTexts:
    osPtpMIB.setRevisions(
        ("2012-08-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClockDomainType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ClockIntervalBase2(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class ClockStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("freerun", 1),
          ("holdover", 2),
          ("acquiring", 3),
          ("frequencyLocked", 4),
          ("phaseAligned", 5))
    )



class ClockTxModeType(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 0),
          ("unicast", 1),
          ("multicast", 2),
          ("multicastmix", 3))
    )



# MIB Managed Objects in the order of their OIDs

_OsPtpMIBNotifications_ObjectIdentity = ObjectIdentity
osPtpMIBNotifications = _OsPtpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 0)
)
_OsPtpMIBObjects_ObjectIdentity = ObjectIdentity
osPtpMIBObjects = _OsPtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1)
)
_OsPtpMIBInfo_ObjectIdentity = ObjectIdentity
osPtpMIBInfo = _OsPtpMIBInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2)
)
_OsPtpMIBEventParams_ObjectIdentity = ObjectIdentity
osPtpMIBEventParams = _OsPtpMIBEventParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1)
)


class _OsPtpSlaveLastEvent_Type(Integer32):
    """Custom type osPtpSlaveLastEvent based on Integer32"""
    defaultValue = 0

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
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("inHoldover", 1),
          ("noCurrentMaster", 2),
          ("noClockInput", 3),
          ("noTimeOfDayInput", 4),
          ("toPSyncTimeNotTAI", 5),
          ("ptpPortNotOperational", 6),
          ("visibleMasterRefusedSyncGrantRequest", 7),
          ("visibleMasterIgnoredSyncGrantRequest", 8),
          ("visibleMasterRefusedDlyRespGrantRequest", 9),
          ("visibleMasterIgnoredDlyRespGrantRequest", 10),
          ("visibleMasterTooFewSyncMessages", 11),
          ("visibleMasterTooFewFollowUpMessages", 12),
          ("visibleMasterTooFewDelayResponseMessages", 13),
          ("accMasterRefusedAnnounceGrantRequest", 14),
          ("accMasterIgnoredAnnounceGrantRequest", 15),
          ("acceptableMasterTooFewAnnounceMessages", 16),
          ("currentMasterTooManySyncsWithoutFollowUp", 17),
          ("currentMasterTooManyFollowUpsWithoutSync", 18),
          ("currentMasterTooManyMissingDlyResponses", 19),
          ("m2SPacketDelayVaration", 20),
          ("s2MPacketDelayVaration", 21),
          ("toPSyncUTCOffsetUnknown", 22))
    )


_OsPtpSlaveLastEvent_Type.__name__ = "Integer32"
_OsPtpSlaveLastEvent_Object = MibScalar
osPtpSlaveLastEvent = _OsPtpSlaveLastEvent_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1, 1),
    _OsPtpSlaveLastEvent_Type()
)
osPtpSlaveLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPtpSlaveLastEvent.setStatus("current")


class _OsPtpSlaveEventReason_Type(Integer32):
    """Custom type osPtpSlaveEventReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmSet", 1),
          ("alarmClear", 2))
    )


_OsPtpSlaveEventReason_Type.__name__ = "Integer32"
_OsPtpSlaveEventReason_Object = MibScalar
osPtpSlaveEventReason = _OsPtpSlaveEventReason_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1, 2),
    _OsPtpSlaveEventReason_Type()
)
osPtpSlaveEventReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPtpSlaveEventReason.setStatus("current")


class _OsPtpSlaveEventDescription_Type(DisplayString):
    """Custom type osPtpSlaveEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_OsPtpSlaveEventDescription_Type.__name__ = "DisplayString"
_OsPtpSlaveEventDescription_Object = MibScalar
osPtpSlaveEventDescription = _OsPtpSlaveEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 1, 3),
    _OsPtpSlaveEventDescription_Type()
)
osPtpSlaveEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPtpSlaveEventDescription.setStatus("current")
_OsPtpMIBSlaveInfo_ObjectIdentity = ObjectIdentity
osPtpMIBSlaveInfo = _OsPtpMIBSlaveInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 2, 2)
)
_OsPtpMIBCfg_ObjectIdentity = ObjectIdentity
osPtpMIBCfg = _OsPtpMIBCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3)
)
_OsPtpMIBSlaveCfg_ObjectIdentity = ObjectIdentity
osPtpMIBSlaveCfg = _OsPtpMIBSlaveCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2)
)
_OsPtpMIBSlaveCfgGen_ObjectIdentity = ObjectIdentity
osPtpMIBSlaveCfgGen = _OsPtpMIBSlaveCfgGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1)
)


class _OsPtpSlaveAdminStatus_Type(Integer32):
    """Custom type osPtpSlaveAdminStatus based on Integer32"""
    defaultValue = 4

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
        *(("unknown", 1),
          ("clear", 2),
          ("enabled", 3),
          ("disabled", 4))
    )


_OsPtpSlaveAdminStatus_Type.__name__ = "Integer32"
_OsPtpSlaveAdminStatus_Object = MibScalar
osPtpSlaveAdminStatus = _OsPtpSlaveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 1),
    _OsPtpSlaveAdminStatus_Type()
)
osPtpSlaveAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveAdminStatus.setStatus("current")


class _OsPtpSlavePortVifName_Type(DisplayString):
    """Custom type osPtpSlavePortVifName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_OsPtpSlavePortVifName_Type.__name__ = "DisplayString"
_OsPtpSlavePortVifName_Object = MibScalar
osPtpSlavePortVifName = _OsPtpSlavePortVifName_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 2),
    _OsPtpSlavePortVifName_Type()
)
osPtpSlavePortVifName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlavePortVifName.setStatus("current")


class _OsPtpSlaveAddressType_Type(InetAddressType):
    """Custom type osPtpSlaveAddressType based on InetAddressType"""
    defaultValue = 1


_OsPtpSlaveAddressType_Type.__name__ = "InetAddressType"
_OsPtpSlaveAddressType_Object = MibScalar
osPtpSlaveAddressType = _OsPtpSlaveAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 3),
    _OsPtpSlaveAddressType_Type()
)
osPtpSlaveAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveAddressType.setStatus("current")


class _OsPtpSlaveGatewayAddress_Type(InetAddress):
    """Custom type osPtpSlaveGatewayAddress based on InetAddress"""
    defaultValue = OctetString("")


_OsPtpSlaveGatewayAddress_Type.__name__ = "InetAddress"
_OsPtpSlaveGatewayAddress_Object = MibScalar
osPtpSlaveGatewayAddress = _OsPtpSlaveGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 4),
    _OsPtpSlaveGatewayAddress_Type()
)
osPtpSlaveGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveGatewayAddress.setStatus("current")


class _OsPtpSlavePortAddrPrefixLength_Type(InetAddressPrefixLength):
    """Custom type osPtpSlavePortAddrPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 24


_OsPtpSlavePortAddrPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_OsPtpSlavePortAddrPrefixLength_Object = MibScalar
osPtpSlavePortAddrPrefixLength = _OsPtpSlavePortAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 5),
    _OsPtpSlavePortAddrPrefixLength_Type()
)
osPtpSlavePortAddrPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlavePortAddrPrefixLength.setStatus("current")
_OsPtpSlavePortAddress_Type = InetAddress
_OsPtpSlavePortAddress_Object = MibScalar
osPtpSlavePortAddress = _OsPtpSlavePortAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 6),
    _OsPtpSlavePortAddress_Type()
)
osPtpSlavePortAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlavePortAddress.setStatus("current")


class _OsPtpSlaveDelayRequestInterval_Type(ClockIntervalBase2):
    """Custom type osPtpSlaveDelayRequestInterval based on ClockIntervalBase2"""
    defaultValue = -5


_OsPtpSlaveDelayRequestInterval_Type.__name__ = "ClockIntervalBase2"
_OsPtpSlaveDelayRequestInterval_Object = MibScalar
osPtpSlaveDelayRequestInterval = _OsPtpSlaveDelayRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 10),
    _OsPtpSlaveDelayRequestInterval_Type()
)
osPtpSlaveDelayRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveDelayRequestInterval.setStatus("current")


class _OsPtpSlaveAnnounceInterval_Type(ClockIntervalBase2):
    """Custom type osPtpSlaveAnnounceInterval based on ClockIntervalBase2"""
    defaultValue = 1


_OsPtpSlaveAnnounceInterval_Type.__name__ = "ClockIntervalBase2"
_OsPtpSlaveAnnounceInterval_Object = MibScalar
osPtpSlaveAnnounceInterval = _OsPtpSlaveAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 11),
    _OsPtpSlaveAnnounceInterval_Type()
)
osPtpSlaveAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveAnnounceInterval.setStatus("current")


class _OsPtpSlaveSyncInterval_Type(ClockIntervalBase2):
    """Custom type osPtpSlaveSyncInterval based on ClockIntervalBase2"""
    defaultValue = -5


_OsPtpSlaveSyncInterval_Type.__name__ = "ClockIntervalBase2"
_OsPtpSlaveSyncInterval_Object = MibScalar
osPtpSlaveSyncInterval = _OsPtpSlaveSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 12),
    _OsPtpSlaveSyncInterval_Type()
)
osPtpSlaveSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveSyncInterval.setStatus("current")


class _OsPtpSlaveTodUartBaudRate_Type(Integer32):
    """Custom type osPtpSlaveTodUartBaudRate based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("none", 1),
          ("baud1200", 2),
          ("baud2400", 3),
          ("baud4800", 4),
          ("baud9600", 5),
          ("baud19200", 6))
    )


_OsPtpSlaveTodUartBaudRate_Type.__name__ = "Integer32"
_OsPtpSlaveTodUartBaudRate_Object = MibScalar
osPtpSlaveTodUartBaudRate = _OsPtpSlaveTodUartBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 20),
    _OsPtpSlaveTodUartBaudRate_Type()
)
osPtpSlaveTodUartBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveTodUartBaudRate.setStatus("current")


class _OsPtpSlavePortTxMode_Type(ClockTxModeType):
    """Custom type osPtpSlavePortTxMode based on ClockTxModeType"""
    defaultValue = 1


_OsPtpSlavePortTxMode_Type.__name__ = "ClockTxModeType"
_OsPtpSlavePortTxMode_Object = MibScalar
osPtpSlavePortTxMode = _OsPtpSlavePortTxMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 21),
    _OsPtpSlavePortTxMode_Type()
)
osPtpSlavePortTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlavePortTxMode.setStatus("current")


class _OsPtpSlaveDirection_Type(Integer32):
    """Custom type osPtpSlaveDirection based on Integer32"""
    defaultValue = 1

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
        *(("unknown", 0),
          ("both", 1),
          ("slaveToMaster", 2),
          ("masterToSlave", 3))
    )


_OsPtpSlaveDirection_Type.__name__ = "Integer32"
_OsPtpSlaveDirection_Object = MibScalar
osPtpSlaveDirection = _OsPtpSlaveDirection_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 22),
    _OsPtpSlaveDirection_Type()
)
osPtpSlaveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveDirection.setStatus("current")


class _OsPtpSlaveDomainIndex_Type(ClockDomainType):
    """Custom type osPtpSlaveDomainIndex based on ClockDomainType"""
    defaultValue = 0


_OsPtpSlaveDomainIndex_Type.__name__ = "ClockDomainType"
_OsPtpSlaveDomainIndex_Object = MibScalar
osPtpSlaveDomainIndex = _OsPtpSlaveDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 23),
    _OsPtpSlaveDomainIndex_Type()
)
osPtpSlaveDomainIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveDomainIndex.setStatus("current")


class _OsPtpSlaveOutClkFrequency_Type(Integer32):
    """Custom type osPtpSlaveOutClkFrequency based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 170000),
    )


_OsPtpSlaveOutClkFrequency_Type.__name__ = "Integer32"
_OsPtpSlaveOutClkFrequency_Object = MibScalar
osPtpSlaveOutClkFrequency = _OsPtpSlaveOutClkFrequency_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 24),
    _OsPtpSlaveOutClkFrequency_Type()
)
osPtpSlaveOutClkFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveOutClkFrequency.setStatus("current")


class _OsPtpSlaveDirectMasterOnly_Type(TruthValue):
    """Custom type osPtpSlaveDirectMasterOnly based on TruthValue"""
    defaultValue = 2


_OsPtpSlaveDirectMasterOnly_Type.__name__ = "TruthValue"
_OsPtpSlaveDirectMasterOnly_Object = MibScalar
osPtpSlaveDirectMasterOnly = _OsPtpSlaveDirectMasterOnly_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 1, 30),
    _OsPtpSlaveDirectMasterOnly_Type()
)
osPtpSlaveDirectMasterOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveDirectMasterOnly.setStatus("current")
_OsPtpMIBSlaveCfgTbl_ObjectIdentity = ObjectIdentity
osPtpMIBSlaveCfgTbl = _OsPtpMIBSlaveCfgTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2)
)
_OsPtpSlaveDirectMasterTable_Object = MibTable
osPtpSlaveDirectMasterTable = _OsPtpSlaveDirectMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    osPtpSlaveDirectMasterTable.setStatus("current")
_OsPtpSlaveDirectMasterEntry_Object = MibTableRow
osPtpSlaveDirectMasterEntry = _OsPtpSlaveDirectMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1, 1)
)
osPtpSlaveDirectMasterEntry.setIndexNames(
    (0, "OS-PTP-MIB", "osPtpSlaveDirectMasterId"),
)
if mibBuilder.loadTexts:
    osPtpSlaveDirectMasterEntry.setStatus("current")


class _OsPtpSlaveDirectMasterId_Type(Integer32):
    """Custom type osPtpSlaveDirectMasterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsPtpSlaveDirectMasterId_Type.__name__ = "Integer32"
_OsPtpSlaveDirectMasterId_Object = MibTableColumn
osPtpSlaveDirectMasterId = _OsPtpSlaveDirectMasterId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1, 1, 1),
    _OsPtpSlaveDirectMasterId_Type()
)
osPtpSlaveDirectMasterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osPtpSlaveDirectMasterId.setStatus("current")
_OsPtpSlaveDirectMasterAddress_Type = InetAddress
_OsPtpSlaveDirectMasterAddress_Object = MibTableColumn
osPtpSlaveDirectMasterAddress = _OsPtpSlaveDirectMasterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 1, 3, 2, 2, 1, 1, 2),
    _OsPtpSlaveDirectMasterAddress_Type()
)
osPtpSlaveDirectMasterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osPtpSlaveDirectMasterAddress.setStatus("current")
_OsPtpMIBCapabilities_ObjectIdentity = ObjectIdentity
osPtpMIBCapabilities = _OsPtpMIBCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 3)
)
_OsPtpSlaveSupported_Type = TruthValue
_OsPtpSlaveSupported_Object = MibScalar
osPtpSlaveSupported = _OsPtpSlaveSupported_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 3, 1),
    _OsPtpSlaveSupported_Type()
)
osPtpSlaveSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPtpSlaveSupported.setStatus("current")


class _OsPtpSlaveAddressTypesSupported_Type(Bits):
    """Custom type osPtpSlaveAddressTypesSupported based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1),
          ("ipv4z", 2),
          ("ipv6z", 3))
    )

_OsPtpSlaveAddressTypesSupported_Type.__name__ = "Bits"
_OsPtpSlaveAddressTypesSupported_Object = MibScalar
osPtpSlaveAddressTypesSupported = _OsPtpSlaveAddressTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 3, 2),
    _OsPtpSlaveAddressTypesSupported_Type()
)
osPtpSlaveAddressTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPtpSlaveAddressTypesSupported.setStatus("current")
_OsPtpSlaveNumOfDirectMasterRows_Type = Unsigned32
_OsPtpSlaveNumOfDirectMasterRows_Object = MibScalar
osPtpSlaveNumOfDirectMasterRows = _OsPtpSlaveNumOfDirectMasterRows_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 3, 3),
    _OsPtpSlaveNumOfDirectMasterRows_Type()
)
osPtpSlaveNumOfDirectMasterRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osPtpSlaveNumOfDirectMasterRows.setStatus("current")
if mibBuilder.loadTexts:
    osPtpSlaveNumOfDirectMasterRows.setUnits("rows")
_OsPtpMIBConformance_ObjectIdentity = ObjectIdentity
osPtpMIBConformance = _OsPtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 100)
)
_OsPtpMIBCompliances_ObjectIdentity = ObjectIdentity
osPtpMIBCompliances = _OsPtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 1)
)
_OsPtpMIBGroups_ObjectIdentity = ObjectIdentity
osPtpMIBGroups = _OsPtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 2)
)

# Managed Objects groups

osPtpMibMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 2, 1)
)
osPtpMibMandatoryGroup.setObjects(
      *(("OS-PTP-MIB", "osPtpSlaveLastEvent"),
        ("OS-PTP-MIB", "osPtpSlaveEventReason"),
        ("OS-PTP-MIB", "osPtpSlaveEventDescription"),
        ("OS-PTP-MIB", "osPtpSlaveSupported"),
        ("OS-PTP-MIB", "osPtpSlaveAddressTypesSupported"),
        ("OS-PTP-MIB", "osPtpSlaveNumOfDirectMasterRows"),
        ("OS-PTP-MIB", "osPtpSlaveAdminStatus"),
        ("OS-PTP-MIB", "osPtpSlavePortVifName"),
        ("OS-PTP-MIB", "osPtpSlaveGatewayAddress"),
        ("OS-PTP-MIB", "osPtpSlaveAddressType"),
        ("OS-PTP-MIB", "osPtpSlavePortAddrPrefixLength"),
        ("OS-PTP-MIB", "osPtpSlavePortAddress"),
        ("OS-PTP-MIB", "osPtpSlaveDirectMasterOnly"),
        ("OS-PTP-MIB", "osPtpSlaveDirectMasterAddress"),
        ("OS-PTP-MIB", "osPtpSlaveDelayRequestInterval"),
        ("OS-PTP-MIB", "osPtpSlaveAnnounceInterval"),
        ("OS-PTP-MIB", "osPtpSlaveSyncInterval"),
        ("OS-PTP-MIB", "osPtpSlaveTodUartBaudRate"),
        ("OS-PTP-MIB", "osPtpSlavePortTxMode"),
        ("OS-PTP-MIB", "osPtpSlaveDirection"),
        ("OS-PTP-MIB", "osPtpSlaveDomainIndex"),
        ("OS-PTP-MIB", "osPtpSlaveOutClkFrequency"))
)
if mibBuilder.loadTexts:
    osPtpMibMandatoryGroup.setStatus("current")


# Notification objects

osPtpMIBSlaveAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 0, 1)
)
osPtpMIBSlaveAlarm.setObjects(
      *(("OS-PTP-MIB", "osPtpSlaveLastEvent"),
        ("OS-PTP-MIB", "osPtpSlaveEventReason"),
        ("OS-PTP-MIB", "osPtpSlaveEventDescription"))
)
if mibBuilder.loadTexts:
    osPtpMIBSlaveAlarm.setStatus(
        "current"
    )


# Notifications groups

osPtpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 2, 2)
)
osPtpNotificationsGroup.setObjects(
    ("OS-PTP-MIB", "osPtpMIBSlaveAlarm")
)
if mibBuilder.loadTexts:
    osPtpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osPtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 22, 100, 1, 1)
)
osPtpMIBCompliance.setObjects(
      *(("OS-PTP-MIB", "osPtpMibMandatoryGroup"),
        ("OS-PTP-MIB", "osPtpNotificationsGroup"))
)
if mibBuilder.loadTexts:
    osPtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-PTP-MIB",
    **{"ClockDomainType": ClockDomainType,
       "ClockIntervalBase2": ClockIntervalBase2,
       "ClockStateType": ClockStateType,
       "ClockTxModeType": ClockTxModeType,
       "osPtpMIB": osPtpMIB,
       "osPtpMIBNotifications": osPtpMIBNotifications,
       "osPtpMIBSlaveAlarm": osPtpMIBSlaveAlarm,
       "osPtpMIBObjects": osPtpMIBObjects,
       "osPtpMIBInfo": osPtpMIBInfo,
       "osPtpMIBEventParams": osPtpMIBEventParams,
       "osPtpSlaveLastEvent": osPtpSlaveLastEvent,
       "osPtpSlaveEventReason": osPtpSlaveEventReason,
       "osPtpSlaveEventDescription": osPtpSlaveEventDescription,
       "osPtpMIBSlaveInfo": osPtpMIBSlaveInfo,
       "osPtpMIBCfg": osPtpMIBCfg,
       "osPtpMIBSlaveCfg": osPtpMIBSlaveCfg,
       "osPtpMIBSlaveCfgGen": osPtpMIBSlaveCfgGen,
       "osPtpSlaveAdminStatus": osPtpSlaveAdminStatus,
       "osPtpSlavePortVifName": osPtpSlavePortVifName,
       "osPtpSlaveAddressType": osPtpSlaveAddressType,
       "osPtpSlaveGatewayAddress": osPtpSlaveGatewayAddress,
       "osPtpSlavePortAddrPrefixLength": osPtpSlavePortAddrPrefixLength,
       "osPtpSlavePortAddress": osPtpSlavePortAddress,
       "osPtpSlaveDelayRequestInterval": osPtpSlaveDelayRequestInterval,
       "osPtpSlaveAnnounceInterval": osPtpSlaveAnnounceInterval,
       "osPtpSlaveSyncInterval": osPtpSlaveSyncInterval,
       "osPtpSlaveTodUartBaudRate": osPtpSlaveTodUartBaudRate,
       "osPtpSlavePortTxMode": osPtpSlavePortTxMode,
       "osPtpSlaveDirection": osPtpSlaveDirection,
       "osPtpSlaveDomainIndex": osPtpSlaveDomainIndex,
       "osPtpSlaveOutClkFrequency": osPtpSlaveOutClkFrequency,
       "osPtpSlaveDirectMasterOnly": osPtpSlaveDirectMasterOnly,
       "osPtpMIBSlaveCfgTbl": osPtpMIBSlaveCfgTbl,
       "osPtpSlaveDirectMasterTable": osPtpSlaveDirectMasterTable,
       "osPtpSlaveDirectMasterEntry": osPtpSlaveDirectMasterEntry,
       "osPtpSlaveDirectMasterId": osPtpSlaveDirectMasterId,
       "osPtpSlaveDirectMasterAddress": osPtpSlaveDirectMasterAddress,
       "osPtpMIBCapabilities": osPtpMIBCapabilities,
       "osPtpSlaveSupported": osPtpSlaveSupported,
       "osPtpSlaveAddressTypesSupported": osPtpSlaveAddressTypesSupported,
       "osPtpSlaveNumOfDirectMasterRows": osPtpSlaveNumOfDirectMasterRows,
       "osPtpMIBConformance": osPtpMIBConformance,
       "osPtpMIBCompliances": osPtpMIBCompliances,
       "osPtpMIBCompliance": osPtpMIBCompliance,
       "osPtpMIBGroups": osPtpMIBGroups,
       "osPtpMibMandatoryGroup": osPtpMibMandatoryGroup,
       "osPtpNotificationsGroup": osPtpNotificationsGroup}
)
