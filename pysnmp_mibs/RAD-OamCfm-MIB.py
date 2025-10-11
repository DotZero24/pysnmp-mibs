# SNMP MIB module (RAD-OamCfm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-OamCfm-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:36 2025
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

(Dot1agCfmCcmInterval,
 Dot1agCfmMepId,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListIdentifier,
 dot1agCfmMaNetName,
 dot1agCfmMdIndex,
 dot1agCfmMdName,
 dot1agCfmMepDbRMepIdentifier,
 dot1agCfmMepDbRMepState,
 dot1agCfmMepDbRdi,
 dot1agCfmMepDefects,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmCcmInterval",
    "Dot1agCfmMepId",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListIdentifier",
    "dot1agCfmMaNetName",
    "dot1agCfmMdIndex",
    "dot1agCfmMdName",
    "dot1agCfmMepDbRMepIdentifier",
    "dot1agCfmMepDbRMepState",
    "dot1agCfmMepDbRdi",
    "dot1agCfmMepDefects",
    "dot1agCfmMepIdentifier")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(LldpPortIdSubtype,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortIdSubtype")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(ethIf,) = mibBuilder.importSymbols(
    "RAD-EthIf-MIB",
    "ethIf")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(DayType,
 RadTestPbitValues) = mibBuilder.importSymbols(
    "RAD-TC",
    "DayType",
    "RadTestPbitValues")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

ethIfOamCfm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EthOamBinCounterType(TextualConvention, Integer32):
    status = "current"
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
        *(("rtDelay", 1),
          ("rtDelayVar", 2),
          ("fwDelay", 3),
          ("fwDelayVar", 4),
          ("bwDelay", 5),
          ("bwDelayVar", 6))
    )



# MIB Managed Objects in the order of their OIDs

_EthIfOamCfmEvents_ObjectIdentity = ObjectIdentity
ethIfOamCfmEvents = _EthIfOamCfmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0)
)
_RadMepTable_Object = MibTable
radMepTable = _RadMepTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    radMepTable.setStatus("deprecated")
_RadMepEntry_Object = MibTableRow
radMepEntry = _RadMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1)
)
radMepEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
)
if mibBuilder.loadTexts:
    radMepEntry.setStatus("deprecated")
_RadOamIdx1_Type = Unsigned32
_RadOamIdx1_Object = MibTableColumn
radOamIdx1 = _RadOamIdx1_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 1),
    _RadOamIdx1_Type()
)
radOamIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radOamIdx1.setStatus("deprecated")
_RadOamEvcIdx_Type = Unsigned32
_RadOamEvcIdx_Object = MibTableColumn
radOamEvcIdx = _RadOamEvcIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 2),
    _RadOamEvcIdx_Type()
)
radOamEvcIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radOamEvcIdx.setStatus("deprecated")
_RadMepIdx_Type = Unsigned32
_RadMepIdx_Object = MibTableColumn
radMepIdx = _RadMepIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 3),
    _RadMepIdx_Type()
)
radMepIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radMepIdx.setStatus("deprecated")
_RadMepRowStatus_Type = RowStatus
_RadMepRowStatus_Object = MibTableColumn
radMepRowStatus = _RadMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 4),
    _RadMepRowStatus_Type()
)
radMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepRowStatus.setStatus("deprecated")
_RadMepLocalMepId_Type = Unsigned32
_RadMepLocalMepId_Object = MibTableColumn
radMepLocalMepId = _RadMepLocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 5),
    _RadMepLocalMepId_Type()
)
radMepLocalMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepLocalMepId.setStatus("current")
_RadMepRemoteMepId_Type = Unsigned32
_RadMepRemoteMepId_Object = MibTableColumn
radMepRemoteMepId = _RadMepRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 6),
    _RadMepRemoteMepId_Type()
)
radMepRemoteMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepRemoteMepId.setStatus("current")


class _RadMepOamMode_Type(Integer32):
    """Custom type radMepOamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("initiate", 3),
          ("react", 4))
    )


_RadMepOamMode_Type.__name__ = "Integer32"
_RadMepOamMode_Object = MibTableColumn
radMepOamMode = _RadMepOamMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 7),
    _RadMepOamMode_Type()
)
radMepOamMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepOamMode.setStatus("current")


class _RadMepContinuityVerMode_Type(Integer32):
    """Custom type radMepContinuityVerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ccBased", 3),
          ("lbBased", 4))
    )


_RadMepContinuityVerMode_Type.__name__ = "Integer32"
_RadMepContinuityVerMode_Object = MibTableColumn
radMepContinuityVerMode = _RadMepContinuityVerMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 8),
    _RadMepContinuityVerMode_Type()
)
radMepContinuityVerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepContinuityVerMode.setStatus("current")


class _RadMepMeLevel_Type(Unsigned32):
    """Custom type radMepMeLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RadMepMeLevel_Type.__name__ = "Unsigned32"
_RadMepMeLevel_Object = MibTableColumn
radMepMeLevel = _RadMepMeLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 9),
    _RadMepMeLevel_Type()
)
radMepMeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepMeLevel.setStatus("current")


class _RadMepOamDestAddrType_Type(Integer32):
    """Custom type radMepOamDestAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_RadMepOamDestAddrType_Type.__name__ = "Integer32"
_RadMepOamDestAddrType_Object = MibTableColumn
radMepOamDestAddrType = _RadMepOamDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 10),
    _RadMepOamDestAddrType_Type()
)
radMepOamDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepOamDestAddrType.setStatus("current")
_RadMepOamDestMacAddr_Type = MacAddress
_RadMepOamDestMacAddr_Object = MibTableColumn
radMepOamDestMacAddr = _RadMepOamDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 11),
    _RadMepOamDestMacAddr_Type()
)
radMepOamDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepOamDestMacAddr.setStatus("current")


class _RadMepDefaultPriority_Type(Unsigned32):
    """Custom type radMepDefaultPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RadMepDefaultPriority_Type.__name__ = "Unsigned32"
_RadMepDefaultPriority_Object = MibTableColumn
radMepDefaultPriority = _RadMepDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 12),
    _RadMepDefaultPriority_Type()
)
radMepDefaultPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepDefaultPriority.setStatus("current")


class _RadMepCcStatus_Type(Integer32):
    """Custom type radMepCcStatus based on Integer32"""
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
        *(("notApplicable", 1),
          ("fail", 2),
          ("ok", 3),
          ("mismerge", 4),
          ("unexpectedMep", 5),
          ("unexpectedMeLevel", 6))
    )


_RadMepCcStatus_Type.__name__ = "Integer32"
_RadMepCcStatus_Object = MibTableColumn
radMepCcStatus = _RadMepCcStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 13),
    _RadMepCcStatus_Type()
)
radMepCcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepCcStatus.setStatus("current")


class _RadMepOamProtocol_Type(Integer32):
    """Custom type radMepOamProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("proprietary", 1),
          ("standard", 2))
    )


_RadMepOamProtocol_Type.__name__ = "Integer32"
_RadMepOamProtocol_Object = MibTableColumn
radMepOamProtocol = _RadMepOamProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 14),
    _RadMepOamProtocol_Type()
)
radMepOamProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepOamProtocol.setStatus("current")
_RadMepMdId_Type = Unsigned32
_RadMepMdId_Object = MibTableColumn
radMepMdId = _RadMepMdId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 15),
    _RadMepMdId_Type()
)
radMepMdId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepMdId.setStatus("current")


class _RadMepMaFormat_Type(Integer32):
    """Custom type radMepMaFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("primaryVid", 1),
          ("charString", 2),
          ("unsignedInt16", 3),
          ("rfc2865VpnId", 4),
          ("icc", 32))
    )


_RadMepMaFormat_Type.__name__ = "Integer32"
_RadMepMaFormat_Object = MibTableColumn
radMepMaFormat = _RadMepMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 16),
    _RadMepMaFormat_Type()
)
radMepMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepMaFormat.setStatus("current")


class _RadMepMaName_Type(OctetString):
    """Custom type radMepMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )


_RadMepMaName_Type.__name__ = "OctetString"
_RadMepMaName_Object = MibTableColumn
radMepMaName = _RadMepMaName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 17),
    _RadMepMaName_Type()
)
radMepMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepMaName.setStatus("current")
_RadMepSpVlanId_Type = Unsigned32
_RadMepSpVlanId_Object = MibTableColumn
radMepSpVlanId = _RadMepSpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 18),
    _RadMepSpVlanId_Type()
)
radMepSpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepSpVlanId.setStatus("current")


class _RadMepCcInterval_Type(Integer32):
    """Custom type radMepCcInterval based on Integer32"""
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
        *(("intervalInvalid", 0),
          ("interval300Hz", 1),
          ("interval10ms", 2),
          ("interval100ms", 3),
          ("interval1s", 4),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval10min", 7))
    )


_RadMepCcInterval_Type.__name__ = "Integer32"
_RadMepCcInterval_Object = MibTableColumn
radMepCcInterval = _RadMepCcInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 19),
    _RadMepCcInterval_Type()
)
radMepCcInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepCcInterval.setStatus("current")
_RadMepTransmitLbmDestMacAddress_Type = MacAddress
_RadMepTransmitLbmDestMacAddress_Object = MibTableColumn
radMepTransmitLbmDestMacAddress = _RadMepTransmitLbmDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 20),
    _RadMepTransmitLbmDestMacAddress_Type()
)
radMepTransmitLbmDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLbmDestMacAddress.setStatus("current")
_RadMepTransmitLbmDestMepId_Type = Unsigned32
_RadMepTransmitLbmDestMepId_Object = MibTableColumn
radMepTransmitLbmDestMepId = _RadMepTransmitLbmDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 21),
    _RadMepTransmitLbmDestMepId_Type()
)
radMepTransmitLbmDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLbmDestMepId.setStatus("current")


class _RadMepTransmitLbmDestIsMepId_Type(Integer32):
    """Custom type radMepTransmitLbmDestIsMepId based on Integer32"""
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


_RadMepTransmitLbmDestIsMepId_Type.__name__ = "Integer32"
_RadMepTransmitLbmDestIsMepId_Object = MibTableColumn
radMepTransmitLbmDestIsMepId = _RadMepTransmitLbmDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 22),
    _RadMepTransmitLbmDestIsMepId_Type()
)
radMepTransmitLbmDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLbmDestIsMepId.setStatus("current")


class _RadMepTransmitLbmMassages_Type(Integer32):
    """Custom type radMepTransmitLbmMassages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_RadMepTransmitLbmMassages_Type.__name__ = "Integer32"
_RadMepTransmitLbmMassages_Object = MibTableColumn
radMepTransmitLbmMassages = _RadMepTransmitLbmMassages_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 23),
    _RadMepTransmitLbmMassages_Type()
)
radMepTransmitLbmMassages.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLbmMassages.setStatus("current")


class _RadMepTransmitLbmVlanPriority_Type(Unsigned32):
    """Custom type radMepTransmitLbmVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RadMepTransmitLbmVlanPriority_Type.__name__ = "Unsigned32"
_RadMepTransmitLbmVlanPriority_Object = MibTableColumn
radMepTransmitLbmVlanPriority = _RadMepTransmitLbmVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 24),
    _RadMepTransmitLbmVlanPriority_Type()
)
radMepTransmitLbmVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLbmVlanPriority.setStatus("current")


class _RadMepTransmitLbmVlanDropEnable_Type(Integer32):
    """Custom type radMepTransmitLbmVlanDropEnable based on Integer32"""
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


_RadMepTransmitLbmVlanDropEnable_Type.__name__ = "Integer32"
_RadMepTransmitLbmVlanDropEnable_Object = MibTableColumn
radMepTransmitLbmVlanDropEnable = _RadMepTransmitLbmVlanDropEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 25),
    _RadMepTransmitLbmVlanDropEnable_Type()
)
radMepTransmitLbmVlanDropEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLbmVlanDropEnable.setStatus("current")
_RadMepLbrIn_Type = Counter32
_RadMepLbrIn_Object = MibTableColumn
radMepLbrIn = _RadMepLbrIn_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 26),
    _RadMepLbrIn_Type()
)
radMepLbrIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLbrIn.setStatus("current")
_RadMepLbrInOutOfOrder_Type = Counter32
_RadMepLbrInOutOfOrder_Object = MibTableColumn
radMepLbrInOutOfOrder = _RadMepLbrInOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 27),
    _RadMepLbrInOutOfOrder_Type()
)
radMepLbrInOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLbrInOutOfOrder.setStatus("current")
_RadMepLbmOut_Type = Counter32
_RadMepLbmOut_Object = MibTableColumn
radMepLbmOut = _RadMepLbmOut_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 28),
    _RadMepLbmOut_Type()
)
radMepLbmOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLbmOut.setStatus("current")
_RadMepTransmitLtmTargetMacAddress_Type = MacAddress
_RadMepTransmitLtmTargetMacAddress_Object = MibTableColumn
radMepTransmitLtmTargetMacAddress = _RadMepTransmitLtmTargetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 29),
    _RadMepTransmitLtmTargetMacAddress_Type()
)
radMepTransmitLtmTargetMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLtmTargetMacAddress.setStatus("current")
_RadMepTransmitLtmTargetMepId_Type = Unsigned32
_RadMepTransmitLtmTargetMepId_Object = MibTableColumn
radMepTransmitLtmTargetMepId = _RadMepTransmitLtmTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 30),
    _RadMepTransmitLtmTargetMepId_Type()
)
radMepTransmitLtmTargetMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLtmTargetMepId.setStatus("current")


class _RadMepTransmitLtmTargetIsMepId_Type(Integer32):
    """Custom type radMepTransmitLtmTargetIsMepId based on Integer32"""
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


_RadMepTransmitLtmTargetIsMepId_Type.__name__ = "Integer32"
_RadMepTransmitLtmTargetIsMepId_Object = MibTableColumn
radMepTransmitLtmTargetIsMepId = _RadMepTransmitLtmTargetIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 31),
    _RadMepTransmitLtmTargetIsMepId_Type()
)
radMepTransmitLtmTargetIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLtmTargetIsMepId.setStatus("current")
_RadMepTransmitLtmTtl_Type = Unsigned32
_RadMepTransmitLtmTtl_Object = MibTableColumn
radMepTransmitLtmTtl = _RadMepTransmitLtmTtl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 32),
    _RadMepTransmitLtmTtl_Type()
)
radMepTransmitLtmTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLtmTtl.setStatus("current")


class _RadMepTransmitLtmActivationCmd_Type(Integer32):
    """Custom type radMepTransmitLtmActivationCmd based on Integer32"""
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


_RadMepTransmitLtmActivationCmd_Type.__name__ = "Integer32"
_RadMepTransmitLtmActivationCmd_Object = MibTableColumn
radMepTransmitLtmActivationCmd = _RadMepTransmitLtmActivationCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 1, 1, 33),
    _RadMepTransmitLtmActivationCmd_Type()
)
radMepTransmitLtmActivationCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepTransmitLtmActivationCmd.setStatus("current")
_EthOamService_ObjectIdentity = ObjectIdentity
ethOamService = _EthOamService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2)
)
_EthOamServiceTable_Object = MibTable
ethOamServiceTable = _EthOamServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ethOamServiceTable.setStatus("current")
_EthOamServiceEntry_Object = MibTableRow
ethOamServiceEntry = _EthOamServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1)
)
ethOamServiceEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
)
if mibBuilder.loadTexts:
    ethOamServiceEntry.setStatus("current")
_EthOamServiceIdx_Type = Unsigned32
_EthOamServiceIdx_Object = MibTableColumn
ethOamServiceIdx = _EthOamServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 1),
    _EthOamServiceIdx_Type()
)
ethOamServiceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamServiceIdx.setStatus("current")
_EthOamServiceRowStatus_Type = RowStatus
_EthOamServiceRowStatus_Object = MibTableColumn
ethOamServiceRowStatus = _EthOamServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 2),
    _EthOamServiceRowStatus_Type()
)
ethOamServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceRowStatus.setStatus("current")


class _EthOamServicePriority_Type(Unsigned32):
    """Custom type ethOamServicePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EthOamServicePriority_Type.__name__ = "Unsigned32"
_EthOamServicePriority_Object = MibTableColumn
ethOamServicePriority = _EthOamServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 3),
    _EthOamServicePriority_Type()
)
ethOamServicePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServicePriority.setStatus("current")


class _EthOamServicePmEnable_Type(Integer32):
    """Custom type ethOamServicePmEnable based on Integer32"""
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


_EthOamServicePmEnable_Type.__name__ = "Integer32"
_EthOamServicePmEnable_Object = MibTableColumn
ethOamServicePmEnable = _EthOamServicePmEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 4),
    _EthOamServicePmEnable_Type()
)
ethOamServicePmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServicePmEnable.setStatus("current")


class _EthOamServiceFrameLossRatioThresh_Type(Integer32):
    """Custom type ethOamServiceFrameLossRatioThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_EthOamServiceFrameLossRatioThresh_Type.__name__ = "Integer32"
_EthOamServiceFrameLossRatioThresh_Object = MibTableColumn
ethOamServiceFrameLossRatioThresh = _EthOamServiceFrameLossRatioThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 5),
    _EthOamServiceFrameLossRatioThresh_Type()
)
ethOamServiceFrameLossRatioThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceFrameLossRatioThresh.setStatus("current")


class _EthOamServiceDelayThresh_Type(Integer32):
    """Custom type ethOamServiceDelayThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_EthOamServiceDelayThresh_Type.__name__ = "Integer32"
_EthOamServiceDelayThresh_Object = MibTableColumn
ethOamServiceDelayThresh = _EthOamServiceDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 6),
    _EthOamServiceDelayThresh_Type()
)
ethOamServiceDelayThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceDelayThresh.setStatus("current")


class _EthOamServiceDelayVarThresh_Type(Integer32):
    """Custom type ethOamServiceDelayVarThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000000),
    )


_EthOamServiceDelayVarThresh_Type.__name__ = "Integer32"
_EthOamServiceDelayVarThresh_Object = MibTableColumn
ethOamServiceDelayVarThresh = _EthOamServiceDelayVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 7),
    _EthOamServiceDelayVarThresh_Type()
)
ethOamServiceDelayVarThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceDelayVarThresh.setStatus("current")


class _EthOamServiceUnavailRatioThresh_Type(Integer32):
    """Custom type ethOamServiceUnavailRatioThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_EthOamServiceUnavailRatioThresh_Type.__name__ = "Integer32"
_EthOamServiceUnavailRatioThresh_Object = MibTableColumn
ethOamServiceUnavailRatioThresh = _EthOamServiceUnavailRatioThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 8),
    _EthOamServiceUnavailRatioThresh_Type()
)
ethOamServiceUnavailRatioThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceUnavailRatioThresh.setStatus("current")
_EthOamServiceTxFrames_Type = Counter32
_EthOamServiceTxFrames_Object = MibTableColumn
ethOamServiceTxFrames = _EthOamServiceTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 9),
    _EthOamServiceTxFrames_Type()
)
ethOamServiceTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceTxFrames.setStatus("current")
_EthOamServiceOverflowTxFrames_Type = Counter32
_EthOamServiceOverflowTxFrames_Object = MibTableColumn
ethOamServiceOverflowTxFrames = _EthOamServiceOverflowTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 10),
    _EthOamServiceOverflowTxFrames_Type()
)
ethOamServiceOverflowTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowTxFrames.setStatus("current")
_EthOamServiceFarEndFrameLoss_Type = Counter32
_EthOamServiceFarEndFrameLoss_Object = MibTableColumn
ethOamServiceFarEndFrameLoss = _EthOamServiceFarEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 11),
    _EthOamServiceFarEndFrameLoss_Type()
)
ethOamServiceFarEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceFarEndFrameLoss.setStatus("current")
_EthOamServiceOverflowFarEndFrameLoss_Type = Counter32
_EthOamServiceOverflowFarEndFrameLoss_Object = MibTableColumn
ethOamServiceOverflowFarEndFrameLoss = _EthOamServiceOverflowFarEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 12),
    _EthOamServiceOverflowFarEndFrameLoss_Type()
)
ethOamServiceOverflowFarEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowFarEndFrameLoss.setStatus("current")
_EthOamServiceFarEndFrameLossRatio_Type = Unsigned32
_EthOamServiceFarEndFrameLossRatio_Object = MibTableColumn
ethOamServiceFarEndFrameLossRatio = _EthOamServiceFarEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 13),
    _EthOamServiceFarEndFrameLossRatio_Type()
)
ethOamServiceFarEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceFarEndFrameLossRatio.setStatus("current")
_EthOamServiceElapsedTime_Type = Counter32
_EthOamServiceElapsedTime_Object = MibTableColumn
ethOamServiceElapsedTime = _EthOamServiceElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 14),
    _EthOamServiceElapsedTime_Type()
)
ethOamServiceElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceElapsedTime.setStatus("current")
_EthOamServiceUnavailSec_Type = Counter32
_EthOamServiceUnavailSec_Object = MibTableColumn
ethOamServiceUnavailSec = _EthOamServiceUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 15),
    _EthOamServiceUnavailSec_Type()
)
ethOamServiceUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceUnavailSec.setStatus("current")
_EthOamServiceUnavailRatio_Type = Unsigned32
_EthOamServiceUnavailRatio_Object = MibTableColumn
ethOamServiceUnavailRatio = _EthOamServiceUnavailRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 16),
    _EthOamServiceUnavailRatio_Type()
)
ethOamServiceUnavailRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceUnavailRatio.setStatus("current")
_EthOamServiceFramesAboveDelay_Type = Counter32
_EthOamServiceFramesAboveDelay_Object = MibTableColumn
ethOamServiceFramesAboveDelay = _EthOamServiceFramesAboveDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 17),
    _EthOamServiceFramesAboveDelay_Type()
)
ethOamServiceFramesAboveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceFramesAboveDelay.setStatus("current")
_EthOamServiceOverflowFramesAboveDelay_Type = Counter32
_EthOamServiceOverflowFramesAboveDelay_Object = MibTableColumn
ethOamServiceOverflowFramesAboveDelay = _EthOamServiceOverflowFramesAboveDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 18),
    _EthOamServiceOverflowFramesAboveDelay_Type()
)
ethOamServiceOverflowFramesAboveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowFramesAboveDelay.setStatus("current")
_EthOamServiceFramesAboveDelayVar_Type = Counter32
_EthOamServiceFramesAboveDelayVar_Object = MibTableColumn
ethOamServiceFramesAboveDelayVar = _EthOamServiceFramesAboveDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 19),
    _EthOamServiceFramesAboveDelayVar_Type()
)
ethOamServiceFramesAboveDelayVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceFramesAboveDelayVar.setStatus("current")
_EthOamServiceOverflowFramesAboveDelayVar_Type = Counter32
_EthOamServiceOverflowFramesAboveDelayVar_Object = MibTableColumn
ethOamServiceOverflowFramesAboveDelayVar = _EthOamServiceOverflowFramesAboveDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 20),
    _EthOamServiceOverflowFramesAboveDelayVar_Type()
)
ethOamServiceOverflowFramesAboveDelayVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowFramesAboveDelayVar.setStatus("current")
_EthOamServiceCurrentDelay_Type = Unsigned32
_EthOamServiceCurrentDelay_Object = MibTableColumn
ethOamServiceCurrentDelay = _EthOamServiceCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 21),
    _EthOamServiceCurrentDelay_Type()
)
ethOamServiceCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceCurrentDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamServiceCurrentDelay.setUnits("microseconds")
_EthOamServiceCurrentDelayVariation_Type = Unsigned32
_EthOamServiceCurrentDelayVariation_Object = MibTableColumn
ethOamServiceCurrentDelayVariation = _EthOamServiceCurrentDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 22),
    _EthOamServiceCurrentDelayVariation_Type()
)
ethOamServiceCurrentDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceCurrentDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    ethOamServiceCurrentDelayVariation.setUnits("microseconds")


class _EthOamServiceResetCounters_Type(Integer32):
    """Custom type ethOamServiceResetCounters based on Integer32"""
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


_EthOamServiceResetCounters_Type.__name__ = "Integer32"
_EthOamServiceResetCounters_Object = MibTableColumn
ethOamServiceResetCounters = _EthOamServiceResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 23),
    _EthOamServiceResetCounters_Type()
)
ethOamServiceResetCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceResetCounters.setStatus("current")
_EthOamServiceNearEndFrameLoss_Type = Counter32
_EthOamServiceNearEndFrameLoss_Object = MibTableColumn
ethOamServiceNearEndFrameLoss = _EthOamServiceNearEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 25),
    _EthOamServiceNearEndFrameLoss_Type()
)
ethOamServiceNearEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceNearEndFrameLoss.setStatus("current")
_EthOamServiceOverflowNearEndFrameLoss_Type = Counter32
_EthOamServiceOverflowNearEndFrameLoss_Object = MibTableColumn
ethOamServiceOverflowNearEndFrameLoss = _EthOamServiceOverflowNearEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 26),
    _EthOamServiceOverflowNearEndFrameLoss_Type()
)
ethOamServiceOverflowNearEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowNearEndFrameLoss.setStatus("current")
_EthOamServiceNearEndFrameLossRatio_Type = Unsigned32
_EthOamServiceNearEndFrameLossRatio_Object = MibTableColumn
ethOamServiceNearEndFrameLossRatio = _EthOamServiceNearEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 27),
    _EthOamServiceNearEndFrameLossRatio_Type()
)
ethOamServiceNearEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceNearEndFrameLossRatio.setStatus("current")


class _EthOamServiceDmmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type ethOamServiceDmmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_EthOamServiceDmmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_EthOamServiceDmmInterval_Object = MibTableColumn
ethOamServiceDmmInterval = _EthOamServiceDmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 28),
    _EthOamServiceDmmInterval_Type()
)
ethOamServiceDmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceDmmInterval.setStatus("current")


class _EthOamServiceLmmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type ethOamServiceLmmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_EthOamServiceLmmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_EthOamServiceLmmInterval_Object = MibTableColumn
ethOamServiceLmmInterval = _EthOamServiceLmmInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 29),
    _EthOamServiceLmmInterval_Type()
)
ethOamServiceLmmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamServiceLmmInterval.setStatus("current")
_EthOamServiceTxLmm_Type = Counter32
_EthOamServiceTxLmm_Object = MibTableColumn
ethOamServiceTxLmm = _EthOamServiceTxLmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 30),
    _EthOamServiceTxLmm_Type()
)
ethOamServiceTxLmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceTxLmm.setStatus("current")
_EthOamServiceOverflowTxLmm_Type = Counter32
_EthOamServiceOverflowTxLmm_Object = MibTableColumn
ethOamServiceOverflowTxLmm = _EthOamServiceOverflowTxLmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 31),
    _EthOamServiceOverflowTxLmm_Type()
)
ethOamServiceOverflowTxLmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowTxLmm.setStatus("current")
_EthOamServiceTxDmm_Type = Counter32
_EthOamServiceTxDmm_Object = MibTableColumn
ethOamServiceTxDmm = _EthOamServiceTxDmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 32),
    _EthOamServiceTxDmm_Type()
)
ethOamServiceTxDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceTxDmm.setStatus("current")
_EthOamServiceOverflowTxDmm_Type = Counter32
_EthOamServiceOverflowTxDmm_Object = MibTableColumn
ethOamServiceOverflowTxDmm = _EthOamServiceOverflowTxDmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 33),
    _EthOamServiceOverflowTxDmm_Type()
)
ethOamServiceOverflowTxDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowTxDmm.setStatus("current")
_EthOamServiceRxLmr_Type = Counter32
_EthOamServiceRxLmr_Object = MibTableColumn
ethOamServiceRxLmr = _EthOamServiceRxLmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 34),
    _EthOamServiceRxLmr_Type()
)
ethOamServiceRxLmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceRxLmr.setStatus("current")
_EthOamServiceOverflowRxLmr_Type = Counter32
_EthOamServiceOverflowRxLmr_Object = MibTableColumn
ethOamServiceOverflowRxLmr = _EthOamServiceOverflowRxLmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 35),
    _EthOamServiceOverflowRxLmr_Type()
)
ethOamServiceOverflowRxLmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowRxLmr.setStatus("current")
_EthOamServiceRxDmr_Type = Counter32
_EthOamServiceRxDmr_Object = MibTableColumn
ethOamServiceRxDmr = _EthOamServiceRxDmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 36),
    _EthOamServiceRxDmr_Type()
)
ethOamServiceRxDmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceRxDmr.setStatus("current")
_EthOamServiceOverflowRxDmr_Type = Counter32
_EthOamServiceOverflowRxDmr_Object = MibTableColumn
ethOamServiceOverflowRxDmr = _EthOamServiceOverflowRxDmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 37),
    _EthOamServiceOverflowRxDmr_Type()
)
ethOamServiceOverflowRxDmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowRxDmr.setStatus("current")
_EthOamServiceTxForward_Type = Counter32
_EthOamServiceTxForward_Object = MibTableColumn
ethOamServiceTxForward = _EthOamServiceTxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 38),
    _EthOamServiceTxForward_Type()
)
ethOamServiceTxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceTxForward.setStatus("current")
_EthOamServiceOverflowTxForward_Type = Counter32
_EthOamServiceOverflowTxForward_Object = MibTableColumn
ethOamServiceOverflowTxForward = _EthOamServiceOverflowTxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 39),
    _EthOamServiceOverflowTxForward_Type()
)
ethOamServiceOverflowTxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowTxForward.setStatus("current")
_EthOamServiceRxForward_Type = Counter32
_EthOamServiceRxForward_Object = MibTableColumn
ethOamServiceRxForward = _EthOamServiceRxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 40),
    _EthOamServiceRxForward_Type()
)
ethOamServiceRxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceRxForward.setStatus("current")
_EthOamServiceOverflowRxForward_Type = Counter32
_EthOamServiceOverflowRxForward_Object = MibTableColumn
ethOamServiceOverflowRxForward = _EthOamServiceOverflowRxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 41),
    _EthOamServiceOverflowRxForward_Type()
)
ethOamServiceOverflowRxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowRxForward.setStatus("current")
_EthOamServiceTxBackward_Type = Counter32
_EthOamServiceTxBackward_Object = MibTableColumn
ethOamServiceTxBackward = _EthOamServiceTxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 42),
    _EthOamServiceTxBackward_Type()
)
ethOamServiceTxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceTxBackward.setStatus("current")
_EthOamServiceOverflowTxBackward_Type = Counter32
_EthOamServiceOverflowTxBackward_Object = MibTableColumn
ethOamServiceOverflowTxBackward = _EthOamServiceOverflowTxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 43),
    _EthOamServiceOverflowTxBackward_Type()
)
ethOamServiceOverflowTxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowTxBackward.setStatus("current")
_EthOamServiceRxBackward_Type = Counter32
_EthOamServiceRxBackward_Object = MibTableColumn
ethOamServiceRxBackward = _EthOamServiceRxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 44),
    _EthOamServiceRxBackward_Type()
)
ethOamServiceRxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceRxBackward.setStatus("current")
_EthOamServiceOverflowRxBackward_Type = Counter32
_EthOamServiceOverflowRxBackward_Object = MibTableColumn
ethOamServiceOverflowRxBackward = _EthOamServiceOverflowRxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 45),
    _EthOamServiceOverflowRxBackward_Type()
)
ethOamServiceOverflowRxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceOverflowRxBackward.setStatus("current")
_EthOamServiceConvertedIndex_Type = Unsigned32
_EthOamServiceConvertedIndex_Object = MibTableColumn
ethOamServiceConvertedIndex = _EthOamServiceConvertedIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 1, 1, 46),
    _EthOamServiceConvertedIndex_Type()
)
ethOamServiceConvertedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamServiceConvertedIndex.setStatus("current")
_EthOamSvcCurrentStatTable_Object = MibTable
ethOamSvcCurrentStatTable = _EthOamSvcCurrentStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ethOamSvcCurrentStatTable.setStatus("current")
_EthOamSvcCurrentStatEntry_Object = MibTableRow
ethOamSvcCurrentStatEntry = _EthOamSvcCurrentStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1)
)
ethOamSvcCurrentStatEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
)
if mibBuilder.loadTexts:
    ethOamSvcCurrentStatEntry.setStatus("current")
_EthOamSvcCurrFramesAboveDelayThresh_Type = PerfCurrentCount
_EthOamSvcCurrFramesAboveDelayThresh_Object = MibTableColumn
ethOamSvcCurrFramesAboveDelayThresh = _EthOamSvcCurrFramesAboveDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 1),
    _EthOamSvcCurrFramesAboveDelayThresh_Type()
)
ethOamSvcCurrFramesAboveDelayThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFramesAboveDelayThresh.setStatus("current")
_EthOamSvcCurrFramesBelowDelayThresh_Type = PerfCurrentCount
_EthOamSvcCurrFramesBelowDelayThresh_Object = MibTableColumn
ethOamSvcCurrFramesBelowDelayThresh = _EthOamSvcCurrFramesBelowDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 2),
    _EthOamSvcCurrFramesBelowDelayThresh_Type()
)
ethOamSvcCurrFramesBelowDelayThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFramesBelowDelayThresh.setStatus("current")
_EthOamSvcCurrFramesAboveDVarThresh_Type = PerfCurrentCount
_EthOamSvcCurrFramesAboveDVarThresh_Object = MibTableColumn
ethOamSvcCurrFramesAboveDVarThresh = _EthOamSvcCurrFramesAboveDVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 3),
    _EthOamSvcCurrFramesAboveDVarThresh_Type()
)
ethOamSvcCurrFramesAboveDVarThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFramesAboveDVarThresh.setStatus("current")
_EthOamSvcCurrFramesBelowDVarThresh_Type = PerfCurrentCount
_EthOamSvcCurrFramesBelowDVarThresh_Object = MibTableColumn
ethOamSvcCurrFramesBelowDVarThresh = _EthOamSvcCurrFramesBelowDVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 4),
    _EthOamSvcCurrFramesBelowDVarThresh_Type()
)
ethOamSvcCurrFramesBelowDVarThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFramesBelowDVarThresh.setStatus("current")
_EthOamSvcCurrFramesTxCounter_Type = PerfCurrentCount
_EthOamSvcCurrFramesTxCounter_Object = MibTableColumn
ethOamSvcCurrFramesTxCounter = _EthOamSvcCurrFramesTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 5),
    _EthOamSvcCurrFramesTxCounter_Type()
)
ethOamSvcCurrFramesTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFramesTxCounter.setStatus("current")
_EthOamSvcCurrFarEndFramesLossCounter_Type = PerfCurrentCount
_EthOamSvcCurrFarEndFramesLossCounter_Object = MibTableColumn
ethOamSvcCurrFarEndFramesLossCounter = _EthOamSvcCurrFarEndFramesLossCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 6),
    _EthOamSvcCurrFarEndFramesLossCounter_Type()
)
ethOamSvcCurrFarEndFramesLossCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFarEndFramesLossCounter.setStatus("current")
_EthOamSvcCurrMinRoundTripDelay_Type = Unsigned32
_EthOamSvcCurrMinRoundTripDelay_Object = MibTableColumn
ethOamSvcCurrMinRoundTripDelay = _EthOamSvcCurrMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 7),
    _EthOamSvcCurrMinRoundTripDelay_Type()
)
ethOamSvcCurrMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinRoundTripDelay.setUnits("microseconds")
_EthOamSvcCurrMaxRoundTripDelay_Type = Unsigned32
_EthOamSvcCurrMaxRoundTripDelay_Object = MibTableColumn
ethOamSvcCurrMaxRoundTripDelay = _EthOamSvcCurrMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 8),
    _EthOamSvcCurrMaxRoundTripDelay_Type()
)
ethOamSvcCurrMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxRoundTripDelay.setUnits("microseconds")
_EthOamSvcCurrAvgRoundTripDelay_Type = Unsigned32
_EthOamSvcCurrAvgRoundTripDelay_Object = MibTableColumn
ethOamSvcCurrAvgRoundTripDelay = _EthOamSvcCurrAvgRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 9),
    _EthOamSvcCurrAvgRoundTripDelay_Type()
)
ethOamSvcCurrAvgRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgRoundTripDelay.setUnits("microseconds")
_EthOamSvcCurrMaxRoundTripDVar_Type = Unsigned32
_EthOamSvcCurrMaxRoundTripDVar_Object = MibTableColumn
ethOamSvcCurrMaxRoundTripDVar = _EthOamSvcCurrMaxRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 10),
    _EthOamSvcCurrMaxRoundTripDVar_Type()
)
ethOamSvcCurrMaxRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxRoundTripDVar.setUnits("microseconds")
_EthOamSvcCurrAvgRoundTripDVar_Type = Unsigned32
_EthOamSvcCurrAvgRoundTripDVar_Object = MibTableColumn
ethOamSvcCurrAvgRoundTripDVar = _EthOamSvcCurrAvgRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 11),
    _EthOamSvcCurrAvgRoundTripDVar_Type()
)
ethOamSvcCurrAvgRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgRoundTripDVar.setUnits("microseconds")


class _EthOamSvcCurrElapsedTime_Type(Integer32):
    """Custom type ethOamSvcCurrElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_EthOamSvcCurrElapsedTime_Type.__name__ = "Integer32"
_EthOamSvcCurrElapsedTime_Object = MibTableColumn
ethOamSvcCurrElapsedTime = _EthOamSvcCurrElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 12),
    _EthOamSvcCurrElapsedTime_Type()
)
ethOamSvcCurrElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrElapsedTime.setStatus("current")
_EthOamSvcCurrUnavailSec_Type = PerfCurrentCount
_EthOamSvcCurrUnavailSec_Object = MibTableColumn
ethOamSvcCurrUnavailSec = _EthOamSvcCurrUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 13),
    _EthOamSvcCurrUnavailSec_Type()
)
ethOamSvcCurrUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrUnavailSec.setStatus("current")
_EthOamSvcCurrLmmTxFrames_Type = PerfCurrentCount
_EthOamSvcCurrLmmTxFrames_Object = MibTableColumn
ethOamSvcCurrLmmTxFrames = _EthOamSvcCurrLmmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 14),
    _EthOamSvcCurrLmmTxFrames_Type()
)
ethOamSvcCurrLmmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrLmmTxFrames.setStatus("current")
_EthOamSvcCurrDmmTxFrames_Type = PerfCurrentCount
_EthOamSvcCurrDmmTxFrames_Object = MibTableColumn
ethOamSvcCurrDmmTxFrames = _EthOamSvcCurrDmmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 16),
    _EthOamSvcCurrDmmTxFrames_Type()
)
ethOamSvcCurrDmmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrDmmTxFrames.setStatus("current")
_EthOamSvcCurrLmrRxFrames_Type = PerfCurrentCount
_EthOamSvcCurrLmrRxFrames_Object = MibTableColumn
ethOamSvcCurrLmrRxFrames = _EthOamSvcCurrLmrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 19),
    _EthOamSvcCurrLmrRxFrames_Type()
)
ethOamSvcCurrLmrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrLmrRxFrames.setStatus("current")
_EthOamSvcCurrDmrRxFrames_Type = PerfCurrentCount
_EthOamSvcCurrDmrRxFrames_Object = MibTableColumn
ethOamSvcCurrDmrRxFrames = _EthOamSvcCurrDmrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 21),
    _EthOamSvcCurrDmrRxFrames_Type()
)
ethOamSvcCurrDmrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrDmrRxFrames.setStatus("current")
_EthOamSvcCurrNearEndFramesLossCounter_Type = PerfCurrentCount
_EthOamSvcCurrNearEndFramesLossCounter_Object = MibTableColumn
ethOamSvcCurrNearEndFramesLossCounter = _EthOamSvcCurrNearEndFramesLossCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 22),
    _EthOamSvcCurrNearEndFramesLossCounter_Type()
)
ethOamSvcCurrNearEndFramesLossCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrNearEndFramesLossCounter.setStatus("current")
_EthOamSvcCurrTxFramesForward_Type = PerfCurrentCount
_EthOamSvcCurrTxFramesForward_Object = MibTableColumn
ethOamSvcCurrTxFramesForward = _EthOamSvcCurrTxFramesForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 23),
    _EthOamSvcCurrTxFramesForward_Type()
)
ethOamSvcCurrTxFramesForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrTxFramesForward.setStatus("current")
_EthOamSvcCurrRxFramesForward_Type = PerfCurrentCount
_EthOamSvcCurrRxFramesForward_Object = MibTableColumn
ethOamSvcCurrRxFramesForward = _EthOamSvcCurrRxFramesForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 24),
    _EthOamSvcCurrRxFramesForward_Type()
)
ethOamSvcCurrRxFramesForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrRxFramesForward.setStatus("current")
_EthOamSvcCurrTxFramesBackward_Type = PerfCurrentCount
_EthOamSvcCurrTxFramesBackward_Object = MibTableColumn
ethOamSvcCurrTxFramesBackward = _EthOamSvcCurrTxFramesBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 25),
    _EthOamSvcCurrTxFramesBackward_Type()
)
ethOamSvcCurrTxFramesBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrTxFramesBackward.setStatus("current")
_EthOamSvcCurrRxFramesBackward_Type = PerfCurrentCount
_EthOamSvcCurrRxFramesBackward_Object = MibTableColumn
ethOamSvcCurrRxFramesBackward = _EthOamSvcCurrRxFramesBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 26),
    _EthOamSvcCurrRxFramesBackward_Type()
)
ethOamSvcCurrRxFramesBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrRxFramesBackward.setStatus("current")
_EthOamSvcCurrUnavailableIndForward_Type = PerfCurrentCount
_EthOamSvcCurrUnavailableIndForward_Object = MibTableColumn
ethOamSvcCurrUnavailableIndForward = _EthOamSvcCurrUnavailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 27),
    _EthOamSvcCurrUnavailableIndForward_Type()
)
ethOamSvcCurrUnavailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrUnavailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrUnavailableIndForward.setUnits("seconds")
_EthOamSvcCurrUnavailableIndBackward_Type = PerfCurrentCount
_EthOamSvcCurrUnavailableIndBackward_Object = MibTableColumn
ethOamSvcCurrUnavailableIndBackward = _EthOamSvcCurrUnavailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 28),
    _EthOamSvcCurrUnavailableIndBackward_Type()
)
ethOamSvcCurrUnavailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrUnavailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrUnavailableIndBackward.setUnits("seconds")
_EthOamSvcCurrNearEndFrameLossRatio_Type = PerfCurrentCount
_EthOamSvcCurrNearEndFrameLossRatio_Object = MibTableColumn
ethOamSvcCurrNearEndFrameLossRatio = _EthOamSvcCurrNearEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 29),
    _EthOamSvcCurrNearEndFrameLossRatio_Type()
)
ethOamSvcCurrNearEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrNearEndFrameLossRatio.setStatus("current")
_EthOamSvcCurrFarEndFrameLossRatio_Type = PerfCurrentCount
_EthOamSvcCurrFarEndFrameLossRatio_Object = MibTableColumn
ethOamSvcCurrFarEndFrameLossRatio = _EthOamSvcCurrFarEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 30),
    _EthOamSvcCurrFarEndFrameLossRatio_Type()
)
ethOamSvcCurrFarEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrFarEndFrameLossRatio.setStatus("current")
_EthOamSvcCurrMinRoundTripDVar_Type = Unsigned32
_EthOamSvcCurrMinRoundTripDVar_Object = MibTableColumn
ethOamSvcCurrMinRoundTripDVar = _EthOamSvcCurrMinRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 31),
    _EthOamSvcCurrMinRoundTripDVar_Type()
)
ethOamSvcCurrMinRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinRoundTripDVar.setUnits("microseconds")
_EthOamSvcCurrMinForwardDelay_Type = Unsigned32
_EthOamSvcCurrMinForwardDelay_Object = MibTableColumn
ethOamSvcCurrMinForwardDelay = _EthOamSvcCurrMinForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 32),
    _EthOamSvcCurrMinForwardDelay_Type()
)
ethOamSvcCurrMinForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinForwardDelay.setUnits("microseconds")
_EthOamSvcCurrMaxForwardDelay_Type = Unsigned32
_EthOamSvcCurrMaxForwardDelay_Object = MibTableColumn
ethOamSvcCurrMaxForwardDelay = _EthOamSvcCurrMaxForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 33),
    _EthOamSvcCurrMaxForwardDelay_Type()
)
ethOamSvcCurrMaxForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxForwardDelay.setUnits("microseconds")
_EthOamSvcCurrAvgForwardDelay_Type = Unsigned32
_EthOamSvcCurrAvgForwardDelay_Object = MibTableColumn
ethOamSvcCurrAvgForwardDelay = _EthOamSvcCurrAvgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 34),
    _EthOamSvcCurrAvgForwardDelay_Type()
)
ethOamSvcCurrAvgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgForwardDelay.setUnits("microseconds")
_EthOamSvcCurrMinForwardDVar_Type = Unsigned32
_EthOamSvcCurrMinForwardDVar_Object = MibTableColumn
ethOamSvcCurrMinForwardDVar = _EthOamSvcCurrMinForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 35),
    _EthOamSvcCurrMinForwardDVar_Type()
)
ethOamSvcCurrMinForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinForwardDVar.setUnits("microseconds")
_EthOamSvcCurrMaxForwardDVar_Type = Unsigned32
_EthOamSvcCurrMaxForwardDVar_Object = MibTableColumn
ethOamSvcCurrMaxForwardDVar = _EthOamSvcCurrMaxForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 36),
    _EthOamSvcCurrMaxForwardDVar_Type()
)
ethOamSvcCurrMaxForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxForwardDVar.setUnits("microseconds")
_EthOamSvcCurrAvgForwardDVar_Type = Unsigned32
_EthOamSvcCurrAvgForwardDVar_Object = MibTableColumn
ethOamSvcCurrAvgForwardDVar = _EthOamSvcCurrAvgForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 37),
    _EthOamSvcCurrAvgForwardDVar_Type()
)
ethOamSvcCurrAvgForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgForwardDVar.setUnits("microseconds")
_EthOamSvcCurrMinBackwardDVar_Type = Unsigned32
_EthOamSvcCurrMinBackwardDVar_Object = MibTableColumn
ethOamSvcCurrMinBackwardDVar = _EthOamSvcCurrMinBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 38),
    _EthOamSvcCurrMinBackwardDVar_Type()
)
ethOamSvcCurrMinBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMinBackwardDVar.setUnits("microseconds")
_EthOamSvcCurrMaxBackwardDVar_Type = Unsigned32
_EthOamSvcCurrMaxBackwardDVar_Object = MibTableColumn
ethOamSvcCurrMaxBackwardDVar = _EthOamSvcCurrMaxBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 39),
    _EthOamSvcCurrMaxBackwardDVar_Type()
)
ethOamSvcCurrMaxBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrMaxBackwardDVar.setUnits("microseconds")
_EthOamSvcCurrAvgBackwardDVar_Type = Unsigned32
_EthOamSvcCurrAvgBackwardDVar_Object = MibTableColumn
ethOamSvcCurrAvgBackwardDVar = _EthOamSvcCurrAvgBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 40),
    _EthOamSvcCurrAvgBackwardDVar_Type()
)
ethOamSvcCurrAvgBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvgBackwardDVar.setUnits("microseconds")
_EthOamSvcCurrAvailableIndForward_Type = PerfCurrentCount
_EthOamSvcCurrAvailableIndForward_Object = MibTableColumn
ethOamSvcCurrAvailableIndForward = _EthOamSvcCurrAvailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 41),
    _EthOamSvcCurrAvailableIndForward_Type()
)
ethOamSvcCurrAvailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvailableIndForward.setUnits("seconds")
_EthOamSvcCurrAvailableIndBackward_Type = PerfCurrentCount
_EthOamSvcCurrAvailableIndBackward_Object = MibTableColumn
ethOamSvcCurrAvailableIndBackward = _EthOamSvcCurrAvailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 2, 1, 42),
    _EthOamSvcCurrAvailableIndBackward_Type()
)
ethOamSvcCurrAvailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcCurrAvailableIndBackward.setUnits("seconds")
_EthOamSvcIntervalTable_Object = MibTable
ethOamSvcIntervalTable = _EthOamSvcIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3)
)
if mibBuilder.loadTexts:
    ethOamSvcIntervalTable.setStatus("current")
_EthOamSvcIntervalEntry_Object = MibTableRow
ethOamSvcIntervalEntry = _EthOamSvcIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1)
)
ethOamSvcIntervalEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamSvcIntervalNum"),
)
if mibBuilder.loadTexts:
    ethOamSvcIntervalEntry.setStatus("current")


class _EthOamSvcIntervalNum_Type(Integer32):
    """Custom type ethOamSvcIntervalNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EthOamSvcIntervalNum_Type.__name__ = "Integer32"
_EthOamSvcIntervalNum_Object = MibTableColumn
ethOamSvcIntervalNum = _EthOamSvcIntervalNum_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 1),
    _EthOamSvcIntervalNum_Type()
)
ethOamSvcIntervalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamSvcIntervalNum.setStatus("current")
_EthOamSvcIntervalFramesAboveDelayThresh_Type = PerfIntervalCount
_EthOamSvcIntervalFramesAboveDelayThresh_Object = MibTableColumn
ethOamSvcIntervalFramesAboveDelayThresh = _EthOamSvcIntervalFramesAboveDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 2),
    _EthOamSvcIntervalFramesAboveDelayThresh_Type()
)
ethOamSvcIntervalFramesAboveDelayThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFramesAboveDelayThresh.setStatus("current")
_EthOamSvcIntervalFramesBelowDelayThresh_Type = PerfIntervalCount
_EthOamSvcIntervalFramesBelowDelayThresh_Object = MibTableColumn
ethOamSvcIntervalFramesBelowDelayThresh = _EthOamSvcIntervalFramesBelowDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 3),
    _EthOamSvcIntervalFramesBelowDelayThresh_Type()
)
ethOamSvcIntervalFramesBelowDelayThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFramesBelowDelayThresh.setStatus("current")
_EthOamSvcIntervalFramesAboveDVarThresh_Type = PerfIntervalCount
_EthOamSvcIntervalFramesAboveDVarThresh_Object = MibTableColumn
ethOamSvcIntervalFramesAboveDVarThresh = _EthOamSvcIntervalFramesAboveDVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 4),
    _EthOamSvcIntervalFramesAboveDVarThresh_Type()
)
ethOamSvcIntervalFramesAboveDVarThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFramesAboveDVarThresh.setStatus("current")
_EthOamSvcIntervalFramesBelowDVarThresh_Type = PerfIntervalCount
_EthOamSvcIntervalFramesBelowDVarThresh_Object = MibTableColumn
ethOamSvcIntervalFramesBelowDVarThresh = _EthOamSvcIntervalFramesBelowDVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 5),
    _EthOamSvcIntervalFramesBelowDVarThresh_Type()
)
ethOamSvcIntervalFramesBelowDVarThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFramesBelowDVarThresh.setStatus("current")
_EthOamSvcIntervalFramesTxCounter_Type = PerfIntervalCount
_EthOamSvcIntervalFramesTxCounter_Object = MibTableColumn
ethOamSvcIntervalFramesTxCounter = _EthOamSvcIntervalFramesTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 6),
    _EthOamSvcIntervalFramesTxCounter_Type()
)
ethOamSvcIntervalFramesTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFramesTxCounter.setStatus("current")
_EthOamSvcIntervalFarEndFramesLossCounter_Type = PerfIntervalCount
_EthOamSvcIntervalFarEndFramesLossCounter_Object = MibTableColumn
ethOamSvcIntervalFarEndFramesLossCounter = _EthOamSvcIntervalFarEndFramesLossCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 7),
    _EthOamSvcIntervalFarEndFramesLossCounter_Type()
)
ethOamSvcIntervalFarEndFramesLossCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFarEndFramesLossCounter.setStatus("current")
_EthOamSvcIntervalMinRoundTripDelay_Type = Unsigned32
_EthOamSvcIntervalMinRoundTripDelay_Object = MibTableColumn
ethOamSvcIntervalMinRoundTripDelay = _EthOamSvcIntervalMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 8),
    _EthOamSvcIntervalMinRoundTripDelay_Type()
)
ethOamSvcIntervalMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinRoundTripDelay.setUnits("microseconds")
_EthOamSvcIntervalMaxRoundTripDelay_Type = Unsigned32
_EthOamSvcIntervalMaxRoundTripDelay_Object = MibTableColumn
ethOamSvcIntervalMaxRoundTripDelay = _EthOamSvcIntervalMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 9),
    _EthOamSvcIntervalMaxRoundTripDelay_Type()
)
ethOamSvcIntervalMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxRoundTripDelay.setUnits("microseconds")
_EthOamSvcIntervalAvgRoundTripDelay_Type = Unsigned32
_EthOamSvcIntervalAvgRoundTripDelay_Object = MibTableColumn
ethOamSvcIntervalAvgRoundTripDelay = _EthOamSvcIntervalAvgRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 10),
    _EthOamSvcIntervalAvgRoundTripDelay_Type()
)
ethOamSvcIntervalAvgRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgRoundTripDelay.setUnits("microseconds")
_EthOamSvcIntervalMaxRoundTripDVar_Type = Unsigned32
_EthOamSvcIntervalMaxRoundTripDVar_Object = MibTableColumn
ethOamSvcIntervalMaxRoundTripDVar = _EthOamSvcIntervalMaxRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 11),
    _EthOamSvcIntervalMaxRoundTripDVar_Type()
)
ethOamSvcIntervalMaxRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxRoundTripDVar.setUnits("microseconds")
_EthOamSvcIntervalAvgRoundTripDVar_Type = Unsigned32
_EthOamSvcIntervalAvgRoundTripDVar_Object = MibTableColumn
ethOamSvcIntervalAvgRoundTripDVar = _EthOamSvcIntervalAvgRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 12),
    _EthOamSvcIntervalAvgRoundTripDVar_Type()
)
ethOamSvcIntervalAvgRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgRoundTripDVar.setUnits("microseconds")
_EthOamSvcIntervalUnavailSec_Type = PerfIntervalCount
_EthOamSvcIntervalUnavailSec_Object = MibTableColumn
ethOamSvcIntervalUnavailSec = _EthOamSvcIntervalUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 13),
    _EthOamSvcIntervalUnavailSec_Type()
)
ethOamSvcIntervalUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalUnavailSec.setStatus("current")
_EthOamSvcIntervalLmmTxFrames_Type = PerfIntervalCount
_EthOamSvcIntervalLmmTxFrames_Object = MibTableColumn
ethOamSvcIntervalLmmTxFrames = _EthOamSvcIntervalLmmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 14),
    _EthOamSvcIntervalLmmTxFrames_Type()
)
ethOamSvcIntervalLmmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalLmmTxFrames.setStatus("current")
_EthOamSvcIntervalDmmTxFrames_Type = PerfIntervalCount
_EthOamSvcIntervalDmmTxFrames_Object = MibTableColumn
ethOamSvcIntervalDmmTxFrames = _EthOamSvcIntervalDmmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 16),
    _EthOamSvcIntervalDmmTxFrames_Type()
)
ethOamSvcIntervalDmmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalDmmTxFrames.setStatus("current")
_EthOamSvcIntervalLmrRxFrames_Type = PerfIntervalCount
_EthOamSvcIntervalLmrRxFrames_Object = MibTableColumn
ethOamSvcIntervalLmrRxFrames = _EthOamSvcIntervalLmrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 19),
    _EthOamSvcIntervalLmrRxFrames_Type()
)
ethOamSvcIntervalLmrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalLmrRxFrames.setStatus("current")
_EthOamSvcIntervalDmrRxFrames_Type = PerfIntervalCount
_EthOamSvcIntervalDmrRxFrames_Object = MibTableColumn
ethOamSvcIntervalDmrRxFrames = _EthOamSvcIntervalDmrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 21),
    _EthOamSvcIntervalDmrRxFrames_Type()
)
ethOamSvcIntervalDmrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalDmrRxFrames.setStatus("current")
_EthOamSvcIntervalNearEndFramesLossCounter_Type = PerfIntervalCount
_EthOamSvcIntervalNearEndFramesLossCounter_Object = MibTableColumn
ethOamSvcIntervalNearEndFramesLossCounter = _EthOamSvcIntervalNearEndFramesLossCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 22),
    _EthOamSvcIntervalNearEndFramesLossCounter_Type()
)
ethOamSvcIntervalNearEndFramesLossCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalNearEndFramesLossCounter.setStatus("current")
_EthOamSvcIntervalTxFramesForward_Type = PerfIntervalCount
_EthOamSvcIntervalTxFramesForward_Object = MibTableColumn
ethOamSvcIntervalTxFramesForward = _EthOamSvcIntervalTxFramesForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 23),
    _EthOamSvcIntervalTxFramesForward_Type()
)
ethOamSvcIntervalTxFramesForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalTxFramesForward.setStatus("current")
_EthOamSvcIntervalRxFramesForward_Type = PerfIntervalCount
_EthOamSvcIntervalRxFramesForward_Object = MibTableColumn
ethOamSvcIntervalRxFramesForward = _EthOamSvcIntervalRxFramesForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 24),
    _EthOamSvcIntervalRxFramesForward_Type()
)
ethOamSvcIntervalRxFramesForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalRxFramesForward.setStatus("current")
_EthOamSvcIntervalTxFramesBackward_Type = PerfIntervalCount
_EthOamSvcIntervalTxFramesBackward_Object = MibTableColumn
ethOamSvcIntervalTxFramesBackward = _EthOamSvcIntervalTxFramesBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 25),
    _EthOamSvcIntervalTxFramesBackward_Type()
)
ethOamSvcIntervalTxFramesBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalTxFramesBackward.setStatus("current")
_EthOamSvcIntervalRxFramesBackward_Type = PerfIntervalCount
_EthOamSvcIntervalRxFramesBackward_Object = MibTableColumn
ethOamSvcIntervalRxFramesBackward = _EthOamSvcIntervalRxFramesBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 26),
    _EthOamSvcIntervalRxFramesBackward_Type()
)
ethOamSvcIntervalRxFramesBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalRxFramesBackward.setStatus("current")
_EthOamSvcIntervalUnavailableIndForward_Type = PerfIntervalCount
_EthOamSvcIntervalUnavailableIndForward_Object = MibTableColumn
ethOamSvcIntervalUnavailableIndForward = _EthOamSvcIntervalUnavailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 27),
    _EthOamSvcIntervalUnavailableIndForward_Type()
)
ethOamSvcIntervalUnavailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalUnavailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalUnavailableIndForward.setUnits("seconds")
_EthOamSvcIntervalUnavailableIndBackward_Type = PerfIntervalCount
_EthOamSvcIntervalUnavailableIndBackward_Object = MibTableColumn
ethOamSvcIntervalUnavailableIndBackward = _EthOamSvcIntervalUnavailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 28),
    _EthOamSvcIntervalUnavailableIndBackward_Type()
)
ethOamSvcIntervalUnavailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalUnavailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalUnavailableIndBackward.setUnits("seconds")
_EthOamSvcIntervalNearEndFrameLossRatio_Type = PerfIntervalCount
_EthOamSvcIntervalNearEndFrameLossRatio_Object = MibTableColumn
ethOamSvcIntervalNearEndFrameLossRatio = _EthOamSvcIntervalNearEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 29),
    _EthOamSvcIntervalNearEndFrameLossRatio_Type()
)
ethOamSvcIntervalNearEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalNearEndFrameLossRatio.setStatus("current")
_EthOamSvcIntervalFarEndFrameLossRatio_Type = PerfIntervalCount
_EthOamSvcIntervalFarEndFrameLossRatio_Object = MibTableColumn
ethOamSvcIntervalFarEndFrameLossRatio = _EthOamSvcIntervalFarEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 30),
    _EthOamSvcIntervalFarEndFrameLossRatio_Type()
)
ethOamSvcIntervalFarEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalFarEndFrameLossRatio.setStatus("current")
_EthOamSvcIntervalValidData_Type = TruthValue
_EthOamSvcIntervalValidData_Object = MibTableColumn
ethOamSvcIntervalValidData = _EthOamSvcIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 31),
    _EthOamSvcIntervalValidData_Type()
)
ethOamSvcIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalValidData.setStatus("current")


class _EthOamSvcIntervalDuration_Type(Integer32):
    """Custom type ethOamSvcIntervalDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_EthOamSvcIntervalDuration_Type.__name__ = "Integer32"
_EthOamSvcIntervalDuration_Object = MibTableColumn
ethOamSvcIntervalDuration = _EthOamSvcIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 32),
    _EthOamSvcIntervalDuration_Type()
)
ethOamSvcIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalDuration.setStatus("current")
_EthOamSvcIntervalTimeStamp_Type = DateAndTime
_EthOamSvcIntervalTimeStamp_Object = MibTableColumn
ethOamSvcIntervalTimeStamp = _EthOamSvcIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 33),
    _EthOamSvcIntervalTimeStamp_Type()
)
ethOamSvcIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalTimeStamp.setStatus("current")
_EthOamSvcIntervalMinRoundTripDVar_Type = Unsigned32
_EthOamSvcIntervalMinRoundTripDVar_Object = MibTableColumn
ethOamSvcIntervalMinRoundTripDVar = _EthOamSvcIntervalMinRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 34),
    _EthOamSvcIntervalMinRoundTripDVar_Type()
)
ethOamSvcIntervalMinRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinRoundTripDVar.setUnits("microseconds")
_EthOamSvcIntervalMinForwardDelay_Type = Unsigned32
_EthOamSvcIntervalMinForwardDelay_Object = MibTableColumn
ethOamSvcIntervalMinForwardDelay = _EthOamSvcIntervalMinForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 35),
    _EthOamSvcIntervalMinForwardDelay_Type()
)
ethOamSvcIntervalMinForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinForwardDelay.setUnits("microseconds")
_EthOamSvcIntervalMaxForwardDelay_Type = Unsigned32
_EthOamSvcIntervalMaxForwardDelay_Object = MibTableColumn
ethOamSvcIntervalMaxForwardDelay = _EthOamSvcIntervalMaxForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 36),
    _EthOamSvcIntervalMaxForwardDelay_Type()
)
ethOamSvcIntervalMaxForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxForwardDelay.setUnits("microseconds")
_EthOamSvcIntervalAvgForwardDelay_Type = Unsigned32
_EthOamSvcIntervalAvgForwardDelay_Object = MibTableColumn
ethOamSvcIntervalAvgForwardDelay = _EthOamSvcIntervalAvgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 37),
    _EthOamSvcIntervalAvgForwardDelay_Type()
)
ethOamSvcIntervalAvgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgForwardDelay.setUnits("microseconds")
_EthOamSvcIntervalMinForwardDVar_Type = Unsigned32
_EthOamSvcIntervalMinForwardDVar_Object = MibTableColumn
ethOamSvcIntervalMinForwardDVar = _EthOamSvcIntervalMinForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 38),
    _EthOamSvcIntervalMinForwardDVar_Type()
)
ethOamSvcIntervalMinForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinForwardDVar.setUnits("microseconds")
_EthOamSvcIntervalMaxForwardDVar_Type = Unsigned32
_EthOamSvcIntervalMaxForwardDVar_Object = MibTableColumn
ethOamSvcIntervalMaxForwardDVar = _EthOamSvcIntervalMaxForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 39),
    _EthOamSvcIntervalMaxForwardDVar_Type()
)
ethOamSvcIntervalMaxForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxForwardDVar.setUnits("microseconds")
_EthOamSvcIntervalAvgForwardDVar_Type = Unsigned32
_EthOamSvcIntervalAvgForwardDVar_Object = MibTableColumn
ethOamSvcIntervalAvgForwardDVar = _EthOamSvcIntervalAvgForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 40),
    _EthOamSvcIntervalAvgForwardDVar_Type()
)
ethOamSvcIntervalAvgForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgForwardDVar.setUnits("microseconds")
_EthOamSvcIntervalMinBackwardDVar_Type = Unsigned32
_EthOamSvcIntervalMinBackwardDVar_Object = MibTableColumn
ethOamSvcIntervalMinBackwardDVar = _EthOamSvcIntervalMinBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 41),
    _EthOamSvcIntervalMinBackwardDVar_Type()
)
ethOamSvcIntervalMinBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMinBackwardDVar.setUnits("microseconds")
_EthOamSvcIntervalMaxBackwardDVar_Type = Unsigned32
_EthOamSvcIntervalMaxBackwardDVar_Object = MibTableColumn
ethOamSvcIntervalMaxBackwardDVar = _EthOamSvcIntervalMaxBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 42),
    _EthOamSvcIntervalMaxBackwardDVar_Type()
)
ethOamSvcIntervalMaxBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalMaxBackwardDVar.setUnits("microseconds")
_EthOamSvcIntervalAvgBackwardDVar_Type = Unsigned32
_EthOamSvcIntervalAvgBackwardDVar_Object = MibTableColumn
ethOamSvcIntervalAvgBackwardDVar = _EthOamSvcIntervalAvgBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 43),
    _EthOamSvcIntervalAvgBackwardDVar_Type()
)
ethOamSvcIntervalAvgBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvgBackwardDVar.setUnits("microseconds")
_EthOamSvcIntervalAvailableIndForward_Type = PerfIntervalCount
_EthOamSvcIntervalAvailableIndForward_Object = MibTableColumn
ethOamSvcIntervalAvailableIndForward = _EthOamSvcIntervalAvailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 44),
    _EthOamSvcIntervalAvailableIndForward_Type()
)
ethOamSvcIntervalAvailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvailableIndForward.setUnits("seconds")
_EthOamSvcIntervalAvailableIndBackward_Type = PerfIntervalCount
_EthOamSvcIntervalAvailableIndBackward_Object = MibTableColumn
ethOamSvcIntervalAvailableIndBackward = _EthOamSvcIntervalAvailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 3, 1, 45),
    _EthOamSvcIntervalAvailableIndBackward_Type()
)
ethOamSvcIntervalAvailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcIntervalAvailableIndBackward.setUnits("seconds")
_EthOamSvcTotalTable_Object = MibTable
ethOamSvcTotalTable = _EthOamSvcTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    ethOamSvcTotalTable.setStatus("current")
_EthOamSvcTotalEntry_Object = MibTableRow
ethOamSvcTotalEntry = _EthOamSvcTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1)
)
ethOamSvcTotalEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
)
if mibBuilder.loadTexts:
    ethOamSvcTotalEntry.setStatus("current")
_EthOamSvcTotalFramesAboveDelayThresh_Type = PerfTotalCount
_EthOamSvcTotalFramesAboveDelayThresh_Object = MibTableColumn
ethOamSvcTotalFramesAboveDelayThresh = _EthOamSvcTotalFramesAboveDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 1),
    _EthOamSvcTotalFramesAboveDelayThresh_Type()
)
ethOamSvcTotalFramesAboveDelayThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalFramesAboveDelayThresh.setStatus("current")
_EthOamSvcTotalFramesBelowDelayThresh_Type = PerfTotalCount
_EthOamSvcTotalFramesBelowDelayThresh_Object = MibTableColumn
ethOamSvcTotalFramesBelowDelayThresh = _EthOamSvcTotalFramesBelowDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 2),
    _EthOamSvcTotalFramesBelowDelayThresh_Type()
)
ethOamSvcTotalFramesBelowDelayThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalFramesBelowDelayThresh.setStatus("current")
_EthOamSvcTotalFramesAboveDVarThresh_Type = PerfTotalCount
_EthOamSvcTotalFramesAboveDVarThresh_Object = MibTableColumn
ethOamSvcTotalFramesAboveDVarThresh = _EthOamSvcTotalFramesAboveDVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 3),
    _EthOamSvcTotalFramesAboveDVarThresh_Type()
)
ethOamSvcTotalFramesAboveDVarThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalFramesAboveDVarThresh.setStatus("current")
_EthOamSvcTotalFramesBelowDVarThresh_Type = PerfTotalCount
_EthOamSvcTotalFramesBelowDVarThresh_Object = MibTableColumn
ethOamSvcTotalFramesBelowDVarThresh = _EthOamSvcTotalFramesBelowDVarThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 4),
    _EthOamSvcTotalFramesBelowDVarThresh_Type()
)
ethOamSvcTotalFramesBelowDVarThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalFramesBelowDVarThresh.setStatus("current")
_EthOamSvcTotalFramesTxCounter_Type = PerfTotalCount
_EthOamSvcTotalFramesTxCounter_Object = MibTableColumn
ethOamSvcTotalFramesTxCounter = _EthOamSvcTotalFramesTxCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 5),
    _EthOamSvcTotalFramesTxCounter_Type()
)
ethOamSvcTotalFramesTxCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalFramesTxCounter.setStatus("current")
_EthOamSvcTotalFarEndFramesLossCounter_Type = PerfTotalCount
_EthOamSvcTotalFarEndFramesLossCounter_Object = MibTableColumn
ethOamSvcTotalFarEndFramesLossCounter = _EthOamSvcTotalFarEndFramesLossCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 6),
    _EthOamSvcTotalFarEndFramesLossCounter_Type()
)
ethOamSvcTotalFarEndFramesLossCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalFarEndFramesLossCounter.setStatus("current")
_EthOamSvcTotalMinRoundTripDelay_Type = Unsigned32
_EthOamSvcTotalMinRoundTripDelay_Object = MibTableColumn
ethOamSvcTotalMinRoundTripDelay = _EthOamSvcTotalMinRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 7),
    _EthOamSvcTotalMinRoundTripDelay_Type()
)
ethOamSvcTotalMinRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinRoundTripDelay.setUnits("microseconds")
_EthOamSvcTotalMaxRoundTripDelay_Type = Unsigned32
_EthOamSvcTotalMaxRoundTripDelay_Object = MibTableColumn
ethOamSvcTotalMaxRoundTripDelay = _EthOamSvcTotalMaxRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 8),
    _EthOamSvcTotalMaxRoundTripDelay_Type()
)
ethOamSvcTotalMaxRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxRoundTripDelay.setUnits("microseconds")
_EthOamSvcTotalAvgRoundTripDelay_Type = Unsigned32
_EthOamSvcTotalAvgRoundTripDelay_Object = MibTableColumn
ethOamSvcTotalAvgRoundTripDelay = _EthOamSvcTotalAvgRoundTripDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 9),
    _EthOamSvcTotalAvgRoundTripDelay_Type()
)
ethOamSvcTotalAvgRoundTripDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgRoundTripDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgRoundTripDelay.setUnits("microseconds")
_EthOamSvcTotalMaxRoundTripDVar_Type = Unsigned32
_EthOamSvcTotalMaxRoundTripDVar_Object = MibTableColumn
ethOamSvcTotalMaxRoundTripDVar = _EthOamSvcTotalMaxRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 10),
    _EthOamSvcTotalMaxRoundTripDVar_Type()
)
ethOamSvcTotalMaxRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxRoundTripDVar.setUnits("microseconds")
_EthOamSvcTotalAvgRoundTripDVar_Type = Unsigned32
_EthOamSvcTotalAvgRoundTripDVar_Object = MibTableColumn
ethOamSvcTotalAvgRoundTripDVar = _EthOamSvcTotalAvgRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 11),
    _EthOamSvcTotalAvgRoundTripDVar_Type()
)
ethOamSvcTotalAvgRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgRoundTripDVar.setUnits("microseconds")
_EthOamSvcTotalUnavailSec_Type = PerfTotalCount
_EthOamSvcTotalUnavailSec_Object = MibTableColumn
ethOamSvcTotalUnavailSec = _EthOamSvcTotalUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 12),
    _EthOamSvcTotalUnavailSec_Type()
)
ethOamSvcTotalUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalUnavailSec.setStatus("current")
_EthOamSvcTotalLmmTxFrames_Type = PerfTotalCount
_EthOamSvcTotalLmmTxFrames_Object = MibTableColumn
ethOamSvcTotalLmmTxFrames = _EthOamSvcTotalLmmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 13),
    _EthOamSvcTotalLmmTxFrames_Type()
)
ethOamSvcTotalLmmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalLmmTxFrames.setStatus("current")
_EthOamSvcTotalDmmTxFrames_Type = PerfTotalCount
_EthOamSvcTotalDmmTxFrames_Object = MibTableColumn
ethOamSvcTotalDmmTxFrames = _EthOamSvcTotalDmmTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 15),
    _EthOamSvcTotalDmmTxFrames_Type()
)
ethOamSvcTotalDmmTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalDmmTxFrames.setStatus("current")
_EthOamSvcTotalLmrRxFrames_Type = PerfTotalCount
_EthOamSvcTotalLmrRxFrames_Object = MibTableColumn
ethOamSvcTotalLmrRxFrames = _EthOamSvcTotalLmrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 18),
    _EthOamSvcTotalLmrRxFrames_Type()
)
ethOamSvcTotalLmrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalLmrRxFrames.setStatus("current")
_EthOamSvcTotalDmrRxFrames_Type = PerfTotalCount
_EthOamSvcTotalDmrRxFrames_Object = MibTableColumn
ethOamSvcTotalDmrRxFrames = _EthOamSvcTotalDmrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 20),
    _EthOamSvcTotalDmrRxFrames_Type()
)
ethOamSvcTotalDmrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalDmrRxFrames.setStatus("current")
_EthOamSvcTotalNearEndFramesLossCounter_Type = PerfTotalCount
_EthOamSvcTotalNearEndFramesLossCounter_Object = MibTableColumn
ethOamSvcTotalNearEndFramesLossCounter = _EthOamSvcTotalNearEndFramesLossCounter_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 21),
    _EthOamSvcTotalNearEndFramesLossCounter_Type()
)
ethOamSvcTotalNearEndFramesLossCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalNearEndFramesLossCounter.setStatus("current")
_EthOamSvcTotalTxFramesForward_Type = PerfTotalCount
_EthOamSvcTotalTxFramesForward_Object = MibTableColumn
ethOamSvcTotalTxFramesForward = _EthOamSvcTotalTxFramesForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 22),
    _EthOamSvcTotalTxFramesForward_Type()
)
ethOamSvcTotalTxFramesForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalTxFramesForward.setStatus("current")
_EthOamSvcTotalRxFramesForward_Type = PerfTotalCount
_EthOamSvcTotalRxFramesForward_Object = MibTableColumn
ethOamSvcTotalRxFramesForward = _EthOamSvcTotalRxFramesForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 23),
    _EthOamSvcTotalRxFramesForward_Type()
)
ethOamSvcTotalRxFramesForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalRxFramesForward.setStatus("current")
_EthOamSvcTotalTxFramesBackward_Type = PerfTotalCount
_EthOamSvcTotalTxFramesBackward_Object = MibTableColumn
ethOamSvcTotalTxFramesBackward = _EthOamSvcTotalTxFramesBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 24),
    _EthOamSvcTotalTxFramesBackward_Type()
)
ethOamSvcTotalTxFramesBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalTxFramesBackward.setStatus("current")
_EthOamSvcTotalRxFramesBackward_Type = PerfTotalCount
_EthOamSvcTotalRxFramesBackward_Object = MibTableColumn
ethOamSvcTotalRxFramesBackward = _EthOamSvcTotalRxFramesBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 25),
    _EthOamSvcTotalRxFramesBackward_Type()
)
ethOamSvcTotalRxFramesBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalRxFramesBackward.setStatus("current")
_EthOamSvcTotalUnavailableIndForward_Type = PerfTotalCount
_EthOamSvcTotalUnavailableIndForward_Object = MibTableColumn
ethOamSvcTotalUnavailableIndForward = _EthOamSvcTotalUnavailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 26),
    _EthOamSvcTotalUnavailableIndForward_Type()
)
ethOamSvcTotalUnavailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalUnavailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalUnavailableIndForward.setUnits("seconds")
_EthOamSvcTotalUnavailableIndBackward_Type = PerfTotalCount
_EthOamSvcTotalUnavailableIndBackward_Object = MibTableColumn
ethOamSvcTotalUnavailableIndBackward = _EthOamSvcTotalUnavailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 27),
    _EthOamSvcTotalUnavailableIndBackward_Type()
)
ethOamSvcTotalUnavailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalUnavailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalUnavailableIndBackward.setUnits("seconds")
_EthOamSvcTotalMinRoundTripDVar_Type = Unsigned32
_EthOamSvcTotalMinRoundTripDVar_Object = MibTableColumn
ethOamSvcTotalMinRoundTripDVar = _EthOamSvcTotalMinRoundTripDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 29),
    _EthOamSvcTotalMinRoundTripDVar_Type()
)
ethOamSvcTotalMinRoundTripDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinRoundTripDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinRoundTripDVar.setUnits("microseconds")
_EthOamSvcTotalMinForwardDelay_Type = Unsigned32
_EthOamSvcTotalMinForwardDelay_Object = MibTableColumn
ethOamSvcTotalMinForwardDelay = _EthOamSvcTotalMinForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 30),
    _EthOamSvcTotalMinForwardDelay_Type()
)
ethOamSvcTotalMinForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinForwardDelay.setUnits("microseconds")
_EthOamSvcTotalMaxForwardDelay_Type = Unsigned32
_EthOamSvcTotalMaxForwardDelay_Object = MibTableColumn
ethOamSvcTotalMaxForwardDelay = _EthOamSvcTotalMaxForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 31),
    _EthOamSvcTotalMaxForwardDelay_Type()
)
ethOamSvcTotalMaxForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxForwardDelay.setUnits("microseconds")
_EthOamSvcTotalAvgForwardDelay_Type = Unsigned32
_EthOamSvcTotalAvgForwardDelay_Object = MibTableColumn
ethOamSvcTotalAvgForwardDelay = _EthOamSvcTotalAvgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 32),
    _EthOamSvcTotalAvgForwardDelay_Type()
)
ethOamSvcTotalAvgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgForwardDelay.setUnits("microseconds")
_EthOamSvcTotalMinForwardDVar_Type = Unsigned32
_EthOamSvcTotalMinForwardDVar_Object = MibTableColumn
ethOamSvcTotalMinForwardDVar = _EthOamSvcTotalMinForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 33),
    _EthOamSvcTotalMinForwardDVar_Type()
)
ethOamSvcTotalMinForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinForwardDVar.setUnits("microseconds")
_EthOamSvcTotalMaxForwardDVar_Type = Unsigned32
_EthOamSvcTotalMaxForwardDVar_Object = MibTableColumn
ethOamSvcTotalMaxForwardDVar = _EthOamSvcTotalMaxForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 34),
    _EthOamSvcTotalMaxForwardDVar_Type()
)
ethOamSvcTotalMaxForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxForwardDVar.setUnits("microseconds")
_EthOamSvcTotalAvgForwardDVar_Type = Unsigned32
_EthOamSvcTotalAvgForwardDVar_Object = MibTableColumn
ethOamSvcTotalAvgForwardDVar = _EthOamSvcTotalAvgForwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 35),
    _EthOamSvcTotalAvgForwardDVar_Type()
)
ethOamSvcTotalAvgForwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgForwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgForwardDVar.setUnits("microseconds")
_EthOamSvcTotalMinBackwardDVar_Type = Unsigned32
_EthOamSvcTotalMinBackwardDVar_Object = MibTableColumn
ethOamSvcTotalMinBackwardDVar = _EthOamSvcTotalMinBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 36),
    _EthOamSvcTotalMinBackwardDVar_Type()
)
ethOamSvcTotalMinBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMinBackwardDVar.setUnits("microseconds")
_EthOamSvcTotalMaxBackwardDVar_Type = Unsigned32
_EthOamSvcTotalMaxBackwardDVar_Object = MibTableColumn
ethOamSvcTotalMaxBackwardDVar = _EthOamSvcTotalMaxBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 37),
    _EthOamSvcTotalMaxBackwardDVar_Type()
)
ethOamSvcTotalMaxBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalMaxBackwardDVar.setUnits("microseconds")
_EthOamSvcTotalAvgBackwardDVar_Type = Unsigned32
_EthOamSvcTotalAvgBackwardDVar_Object = MibTableColumn
ethOamSvcTotalAvgBackwardDVar = _EthOamSvcTotalAvgBackwardDVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 38),
    _EthOamSvcTotalAvgBackwardDVar_Type()
)
ethOamSvcTotalAvgBackwardDVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgBackwardDVar.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvgBackwardDVar.setUnits("microseconds")
_EthOamSvcTotalForwardFrameLossRatio_Type = PerfTotalCount
_EthOamSvcTotalForwardFrameLossRatio_Object = MibTableColumn
ethOamSvcTotalForwardFrameLossRatio = _EthOamSvcTotalForwardFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 39),
    _EthOamSvcTotalForwardFrameLossRatio_Type()
)
ethOamSvcTotalForwardFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalForwardFrameLossRatio.setStatus("current")
_EthOamSvcTotalBackwardFrameLossRatio_Type = PerfTotalCount
_EthOamSvcTotalBackwardFrameLossRatio_Object = MibTableColumn
ethOamSvcTotalBackwardFrameLossRatio = _EthOamSvcTotalBackwardFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 40),
    _EthOamSvcTotalBackwardFrameLossRatio_Type()
)
ethOamSvcTotalBackwardFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalBackwardFrameLossRatio.setStatus("current")
_EthOamSvcTotalAvailableIndForward_Type = Counter32
_EthOamSvcTotalAvailableIndForward_Object = MibTableColumn
ethOamSvcTotalAvailableIndForward = _EthOamSvcTotalAvailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 41),
    _EthOamSvcTotalAvailableIndForward_Type()
)
ethOamSvcTotalAvailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvailableIndForward.setUnits("seconds")
_EthOamSvcTotalAvailableIndBackward_Type = Counter32
_EthOamSvcTotalAvailableIndBackward_Object = MibTableColumn
ethOamSvcTotalAvailableIndBackward = _EthOamSvcTotalAvailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 4, 1, 42),
    _EthOamSvcTotalAvailableIndBackward_Type()
)
ethOamSvcTotalAvailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamSvcTotalAvailableIndBackward.setUnits("seconds")
_EthOamDestNeTable_Object = MibTable
ethOamDestNeTable = _EthOamDestNeTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    ethOamDestNeTable.setStatus("current")
_EthOamDestNeEntry_Object = MibTableRow
ethOamDestNeEntry = _EthOamDestNeEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1)
)
ethOamDestNeEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamDestNeIdx"),
)
if mibBuilder.loadTexts:
    ethOamDestNeEntry.setStatus("current")


class _EthOamDestNeIdx_Type(Unsigned32):
    """Custom type ethOamDestNeIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EthOamDestNeIdx_Type.__name__ = "Unsigned32"
_EthOamDestNeIdx_Object = MibTableColumn
ethOamDestNeIdx = _EthOamDestNeIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 1),
    _EthOamDestNeIdx_Type()
)
ethOamDestNeIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamDestNeIdx.setStatus("current")
_EthOamDestNeRowStatus_Type = RowStatus
_EthOamDestNeRowStatus_Object = MibTableColumn
ethOamDestNeRowStatus = _EthOamDestNeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 2),
    _EthOamDestNeRowStatus_Type()
)
ethOamDestNeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeRowStatus.setStatus("current")
_EthOamDestNePmDestAddr_Type = MacAddress
_EthOamDestNePmDestAddr_Object = MibTableColumn
ethOamDestNePmDestAddr = _EthOamDestNePmDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 3),
    _EthOamDestNePmDestAddr_Type()
)
ethOamDestNePmDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNePmDestAddr.setStatus("current")
_EthOamDestNePmRemoteMepId_Type = Unsigned32
_EthOamDestNePmRemoteMepId_Object = MibTableColumn
ethOamDestNePmRemoteMepId = _EthOamDestNePmRemoteMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 4),
    _EthOamDestNePmRemoteMepId_Type()
)
ethOamDestNePmRemoteMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNePmRemoteMepId.setStatus("current")


class _EthOamDestNePmActivity_Type(Bits):
    """Custom type ethOamDestNePmActivity based on Bits"""
    namedValues = NamedValues(
        *(("singleEndedLoss", 0),
          ("dualEndedLoss", 1),
          ("oneWayDelay", 2),
          ("twoWayDelay", 3))
    )

_EthOamDestNePmActivity_Type.__name__ = "Bits"
_EthOamDestNePmActivity_Object = MibTableColumn
ethOamDestNePmActivity = _EthOamDestNePmActivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 5),
    _EthOamDestNePmActivity_Type()
)
ethOamDestNePmActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNePmActivity.setStatus("deprecated")
_EthOamDestNeTxFrames_Type = Counter32
_EthOamDestNeTxFrames_Object = MibTableColumn
ethOamDestNeTxFrames = _EthOamDestNeTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 6),
    _EthOamDestNeTxFrames_Type()
)
ethOamDestNeTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeTxFrames.setStatus("current")
_EthOamDestNeOverflowTxFrames_Type = Counter32
_EthOamDestNeOverflowTxFrames_Object = MibTableColumn
ethOamDestNeOverflowTxFrames = _EthOamDestNeOverflowTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 7),
    _EthOamDestNeOverflowTxFrames_Type()
)
ethOamDestNeOverflowTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowTxFrames.setStatus("current")
_EthOamDestNeTxLmm_Type = Counter32
_EthOamDestNeTxLmm_Object = MibTableColumn
ethOamDestNeTxLmm = _EthOamDestNeTxLmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 8),
    _EthOamDestNeTxLmm_Type()
)
ethOamDestNeTxLmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeTxLmm.setStatus("current")
_EthOamDestNeOverflowTxLmm_Type = Counter32
_EthOamDestNeOverflowTxLmm_Object = MibTableColumn
ethOamDestNeOverflowTxLmm = _EthOamDestNeOverflowTxLmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 9),
    _EthOamDestNeOverflowTxLmm_Type()
)
ethOamDestNeOverflowTxLmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowTxLmm.setStatus("current")
_EthOamDestNeTxDmm_Type = Counter32
_EthOamDestNeTxDmm_Object = MibTableColumn
ethOamDestNeTxDmm = _EthOamDestNeTxDmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 12),
    _EthOamDestNeTxDmm_Type()
)
ethOamDestNeTxDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeTxDmm.setStatus("current")
_EthOamDestNeOverflowTxDmm_Type = Counter32
_EthOamDestNeOverflowTxDmm_Object = MibTableColumn
ethOamDestNeOverflowTxDmm = _EthOamDestNeOverflowTxDmm_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 13),
    _EthOamDestNeOverflowTxDmm_Type()
)
ethOamDestNeOverflowTxDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowTxDmm.setStatus("current")
_EthOamDestNeRxLmr_Type = Counter32
_EthOamDestNeRxLmr_Object = MibTableColumn
ethOamDestNeRxLmr = _EthOamDestNeRxLmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 18),
    _EthOamDestNeRxLmr_Type()
)
ethOamDestNeRxLmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeRxLmr.setStatus("current")
_EthOamDestNeOverflowRxLmr_Type = Counter32
_EthOamDestNeOverflowRxLmr_Object = MibTableColumn
ethOamDestNeOverflowRxLmr = _EthOamDestNeOverflowRxLmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 19),
    _EthOamDestNeOverflowRxLmr_Type()
)
ethOamDestNeOverflowRxLmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowRxLmr.setStatus("current")
_EthOamDestNeRxDmr_Type = Counter32
_EthOamDestNeRxDmr_Object = MibTableColumn
ethOamDestNeRxDmr = _EthOamDestNeRxDmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 22),
    _EthOamDestNeRxDmr_Type()
)
ethOamDestNeRxDmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeRxDmr.setStatus("current")
_EthOamDestNeOverflowRxDmr_Type = Counter32
_EthOamDestNeOverflowRxDmr_Object = MibTableColumn
ethOamDestNeOverflowRxDmr = _EthOamDestNeOverflowRxDmr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 23),
    _EthOamDestNeOverflowRxDmr_Type()
)
ethOamDestNeOverflowRxDmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowRxDmr.setStatus("current")
_EthOamDestNeFarEndFrameLoss_Type = Counter32
_EthOamDestNeFarEndFrameLoss_Object = MibTableColumn
ethOamDestNeFarEndFrameLoss = _EthOamDestNeFarEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 24),
    _EthOamDestNeFarEndFrameLoss_Type()
)
ethOamDestNeFarEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeFarEndFrameLoss.setStatus("current")
_EthOamDestNeOverflowFarEndFrameLoss_Type = Counter32
_EthOamDestNeOverflowFarEndFrameLoss_Object = MibTableColumn
ethOamDestNeOverflowFarEndFrameLoss = _EthOamDestNeOverflowFarEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 25),
    _EthOamDestNeOverflowFarEndFrameLoss_Type()
)
ethOamDestNeOverflowFarEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowFarEndFrameLoss.setStatus("current")
_EthOamDestNeFarEndFrameLossRatio_Type = Unsigned32
_EthOamDestNeFarEndFrameLossRatio_Object = MibTableColumn
ethOamDestNeFarEndFrameLossRatio = _EthOamDestNeFarEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 26),
    _EthOamDestNeFarEndFrameLossRatio_Type()
)
ethOamDestNeFarEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeFarEndFrameLossRatio.setStatus("current")
_EthOamDestNeTimeElapsed_Type = Unsigned32
_EthOamDestNeTimeElapsed_Object = MibTableColumn
ethOamDestNeTimeElapsed = _EthOamDestNeTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 27),
    _EthOamDestNeTimeElapsed_Type()
)
ethOamDestNeTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeTimeElapsed.setStatus("current")
_EthOamDestNeFramesAboveDelay_Type = Counter32
_EthOamDestNeFramesAboveDelay_Object = MibTableColumn
ethOamDestNeFramesAboveDelay = _EthOamDestNeFramesAboveDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 30),
    _EthOamDestNeFramesAboveDelay_Type()
)
ethOamDestNeFramesAboveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeFramesAboveDelay.setStatus("current")
_EthOamDestNeOverflowFramesAboveDelay_Type = Counter32
_EthOamDestNeOverflowFramesAboveDelay_Object = MibTableColumn
ethOamDestNeOverflowFramesAboveDelay = _EthOamDestNeOverflowFramesAboveDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 31),
    _EthOamDestNeOverflowFramesAboveDelay_Type()
)
ethOamDestNeOverflowFramesAboveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowFramesAboveDelay.setStatus("current")
_EthOamDestNeFramesAboveDelayVar_Type = Counter32
_EthOamDestNeFramesAboveDelayVar_Object = MibTableColumn
ethOamDestNeFramesAboveDelayVar = _EthOamDestNeFramesAboveDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 32),
    _EthOamDestNeFramesAboveDelayVar_Type()
)
ethOamDestNeFramesAboveDelayVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeFramesAboveDelayVar.setStatus("current")
_EthOamDestNeOverflowFramesAboveDelayVar_Type = Counter32
_EthOamDestNeOverflowFramesAboveDelayVar_Object = MibTableColumn
ethOamDestNeOverflowFramesAboveDelayVar = _EthOamDestNeOverflowFramesAboveDelayVar_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 33),
    _EthOamDestNeOverflowFramesAboveDelayVar_Type()
)
ethOamDestNeOverflowFramesAboveDelayVar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowFramesAboveDelayVar.setStatus("current")
_EthOamDestNeCurrentDelay_Type = Unsigned32
_EthOamDestNeCurrentDelay_Object = MibTableColumn
ethOamDestNeCurrentDelay = _EthOamDestNeCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 34),
    _EthOamDestNeCurrentDelay_Type()
)
ethOamDestNeCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeCurrentDelay.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeCurrentDelay.setUnits("microseconds")
_EthOamDestNeCurrentDelayVariation_Type = Unsigned32
_EthOamDestNeCurrentDelayVariation_Object = MibTableColumn
ethOamDestNeCurrentDelayVariation = _EthOamDestNeCurrentDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 35),
    _EthOamDestNeCurrentDelayVariation_Type()
)
ethOamDestNeCurrentDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeCurrentDelayVariation.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeCurrentDelayVariation.setUnits("microseconds")


class _EthOamDestNeResetCounters_Type(Integer32):
    """Custom type ethOamDestNeResetCounters based on Integer32"""
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


_EthOamDestNeResetCounters_Type.__name__ = "Integer32"
_EthOamDestNeResetCounters_Object = MibTableColumn
ethOamDestNeResetCounters = _EthOamDestNeResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 36),
    _EthOamDestNeResetCounters_Type()
)
ethOamDestNeResetCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeResetCounters.setStatus("current")
_EthOamDestNeNearEndFrameLoss_Type = Counter32
_EthOamDestNeNearEndFrameLoss_Object = MibTableColumn
ethOamDestNeNearEndFrameLoss = _EthOamDestNeNearEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 37),
    _EthOamDestNeNearEndFrameLoss_Type()
)
ethOamDestNeNearEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeNearEndFrameLoss.setStatus("current")
_EthOamDestNeOverflowNearEndFrameLoss_Type = Counter32
_EthOamDestNeOverflowNearEndFrameLoss_Object = MibTableColumn
ethOamDestNeOverflowNearEndFrameLoss = _EthOamDestNeOverflowNearEndFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 38),
    _EthOamDestNeOverflowNearEndFrameLoss_Type()
)
ethOamDestNeOverflowNearEndFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowNearEndFrameLoss.setStatus("current")
_EthOamDestNeNearEndFrameLossRatio_Type = Unsigned32
_EthOamDestNeNearEndFrameLossRatio_Object = MibTableColumn
ethOamDestNeNearEndFrameLossRatio = _EthOamDestNeNearEndFrameLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 39),
    _EthOamDestNeNearEndFrameLossRatio_Type()
)
ethOamDestNeNearEndFrameLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeNearEndFrameLossRatio.setStatus("current")


class _EthOamDestNeLmmTraffic_Type(Integer32):
    """Custom type ethOamDestNeLmmTraffic based on Integer32"""
    defaultValue = 2

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("syntheticTraffic", 1),
          ("realTraffic", 2),
          ("lmmSynthetic", 3),
          ("slm", 4),
          ("realTrafficGreen", 5),
          ("realTrafficYellow", 6),
          ("realTrafficNoCcm", 7),
          ("realTrafficGreenNoCcm", 8),
          ("notApplicable", 255))
    )


_EthOamDestNeLmmTraffic_Type.__name__ = "Integer32"
_EthOamDestNeLmmTraffic_Object = MibTableColumn
ethOamDestNeLmmTraffic = _EthOamDestNeLmmTraffic_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 40),
    _EthOamDestNeLmmTraffic_Type()
)
ethOamDestNeLmmTraffic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeLmmTraffic.setStatus("current")
_EthOamDestNeFramesAboveDelayBinProfile_Type = Unsigned32
_EthOamDestNeFramesAboveDelayBinProfile_Object = MibTableColumn
ethOamDestNeFramesAboveDelayBinProfile = _EthOamDestNeFramesAboveDelayBinProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 41),
    _EthOamDestNeFramesAboveDelayBinProfile_Type()
)
ethOamDestNeFramesAboveDelayBinProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeFramesAboveDelayBinProfile.setStatus("current")
_EthOamDestNeFramesAboveDelayVarBinProfile_Type = Unsigned32
_EthOamDestNeFramesAboveDelayVarBinProfile_Object = MibTableColumn
ethOamDestNeFramesAboveDelayVarBinProfile = _EthOamDestNeFramesAboveDelayVarBinProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 42),
    _EthOamDestNeFramesAboveDelayVarBinProfile_Type()
)
ethOamDestNeFramesAboveDelayVarBinProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeFramesAboveDelayVarBinProfile.setStatus("current")


class _EthOamDestNeDmmDataTlvLength_Type(Unsigned32):
    """Custom type ethOamDestNeDmmDataTlvLength based on Unsigned32"""
    defaultValue = 0


_EthOamDestNeDmmDataTlvLength_Type.__name__ = "Unsigned32"
_EthOamDestNeDmmDataTlvLength_Object = MibTableColumn
ethOamDestNeDmmDataTlvLength = _EthOamDestNeDmmDataTlvLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 43),
    _EthOamDestNeDmmDataTlvLength_Type()
)
ethOamDestNeDmmDataTlvLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeDmmDataTlvLength.setStatus("current")


class _EthOamDestNeLossActivity_Type(Integer32):
    """Custom type ethOamDestNeLossActivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("singleEnded", 2),
          ("dualEnded", 3))
    )


_EthOamDestNeLossActivity_Type.__name__ = "Integer32"
_EthOamDestNeLossActivity_Object = MibTableColumn
ethOamDestNeLossActivity = _EthOamDestNeLossActivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 44),
    _EthOamDestNeLossActivity_Type()
)
ethOamDestNeLossActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeLossActivity.setStatus("current")


class _EthOamDestNeDelayActivity_Type(Integer32):
    """Custom type ethOamDestNeDelayActivity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("oneWay", 2),
          ("twoWay", 3))
    )


_EthOamDestNeDelayActivity_Type.__name__ = "Integer32"
_EthOamDestNeDelayActivity_Object = MibTableColumn
ethOamDestNeDelayActivity = _EthOamDestNeDelayActivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 45),
    _EthOamDestNeDelayActivity_Type()
)
ethOamDestNeDelayActivity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeDelayActivity.setStatus("current")
_EthOamDestNeTxForward_Type = Counter32
_EthOamDestNeTxForward_Object = MibTableColumn
ethOamDestNeTxForward = _EthOamDestNeTxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 46),
    _EthOamDestNeTxForward_Type()
)
ethOamDestNeTxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeTxForward.setStatus("current")
_EthOamDestNeOverflowTxForward_Type = Counter32
_EthOamDestNeOverflowTxForward_Object = MibTableColumn
ethOamDestNeOverflowTxForward = _EthOamDestNeOverflowTxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 47),
    _EthOamDestNeOverflowTxForward_Type()
)
ethOamDestNeOverflowTxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowTxForward.setStatus("current")
_EthOamDestNeRxForward_Type = Counter32
_EthOamDestNeRxForward_Object = MibTableColumn
ethOamDestNeRxForward = _EthOamDestNeRxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 48),
    _EthOamDestNeRxForward_Type()
)
ethOamDestNeRxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeRxForward.setStatus("current")
_EthOamDestNeOverflowRxForward_Type = Counter32
_EthOamDestNeOverflowRxForward_Object = MibTableColumn
ethOamDestNeOverflowRxForward = _EthOamDestNeOverflowRxForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 49),
    _EthOamDestNeOverflowRxForward_Type()
)
ethOamDestNeOverflowRxForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowRxForward.setStatus("current")
_EthOamDestNeTxBackward_Type = Counter32
_EthOamDestNeTxBackward_Object = MibTableColumn
ethOamDestNeTxBackward = _EthOamDestNeTxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 50),
    _EthOamDestNeTxBackward_Type()
)
ethOamDestNeTxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeTxBackward.setStatus("current")
_EthOamDestNeOverflowTxBackward_Type = Counter32
_EthOamDestNeOverflowTxBackward_Object = MibTableColumn
ethOamDestNeOverflowTxBackward = _EthOamDestNeOverflowTxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 51),
    _EthOamDestNeOverflowTxBackward_Type()
)
ethOamDestNeOverflowTxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowTxBackward.setStatus("current")
_EthOamDestNeRxBackward_Type = Counter32
_EthOamDestNeRxBackward_Object = MibTableColumn
ethOamDestNeRxBackward = _EthOamDestNeRxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 52),
    _EthOamDestNeRxBackward_Type()
)
ethOamDestNeRxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeRxBackward.setStatus("current")
_EthOamDestNeOverflowRxBackward_Type = Counter32
_EthOamDestNeOverflowRxBackward_Object = MibTableColumn
ethOamDestNeOverflowRxBackward = _EthOamDestNeOverflowRxBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 53),
    _EthOamDestNeOverflowRxBackward_Type()
)
ethOamDestNeOverflowRxBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowRxBackward.setStatus("current")
_EthOamDestNeUnavailableIndForward_Type = Counter32
_EthOamDestNeUnavailableIndForward_Object = MibTableColumn
ethOamDestNeUnavailableIndForward = _EthOamDestNeUnavailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 54),
    _EthOamDestNeUnavailableIndForward_Type()
)
ethOamDestNeUnavailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeUnavailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeUnavailableIndForward.setUnits("seconds")
_EthOamDestNeOverflowUnavailableIndForward_Type = Counter32
_EthOamDestNeOverflowUnavailableIndForward_Object = MibTableColumn
ethOamDestNeOverflowUnavailableIndForward = _EthOamDestNeOverflowUnavailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 55),
    _EthOamDestNeOverflowUnavailableIndForward_Type()
)
ethOamDestNeOverflowUnavailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowUnavailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowUnavailableIndForward.setUnits("seconds")
_EthOamDestNeUnavailableIndBackward_Type = Counter32
_EthOamDestNeUnavailableIndBackward_Object = MibTableColumn
ethOamDestNeUnavailableIndBackward = _EthOamDestNeUnavailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 56),
    _EthOamDestNeUnavailableIndBackward_Type()
)
ethOamDestNeUnavailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeUnavailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeUnavailableIndBackward.setUnits("seconds")
_EthOamDestNeOverflowUnavailableIndBackward_Type = Counter32
_EthOamDestNeOverflowUnavailableIndBackward_Object = MibTableColumn
ethOamDestNeOverflowUnavailableIndBackward = _EthOamDestNeOverflowUnavailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 57),
    _EthOamDestNeOverflowUnavailableIndBackward_Type()
)
ethOamDestNeOverflowUnavailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowUnavailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeOverflowUnavailableIndBackward.setUnits("seconds")
_EthOamDestNeUnavailRatioForward_Type = Unsigned32
_EthOamDestNeUnavailRatioForward_Object = MibTableColumn
ethOamDestNeUnavailRatioForward = _EthOamDestNeUnavailRatioForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 58),
    _EthOamDestNeUnavailRatioForward_Type()
)
ethOamDestNeUnavailRatioForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeUnavailRatioForward.setStatus("current")
_EthOamDestNeUnavailRatioBackward_Type = Unsigned32
_EthOamDestNeUnavailRatioBackward_Object = MibTableColumn
ethOamDestNeUnavailRatioBackward = _EthOamDestNeUnavailRatioBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 59),
    _EthOamDestNeUnavailRatioBackward_Type()
)
ethOamDestNeUnavailRatioBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeUnavailRatioBackward.setStatus("current")


class _EthOamDestNeDescr_Type(SnmpAdminString):
    """Custom type ethOamDestNeDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_EthOamDestNeDescr_Type.__name__ = "SnmpAdminString"
_EthOamDestNeDescr_Object = MibTableColumn
ethOamDestNeDescr = _EthOamDestNeDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 61),
    _EthOamDestNeDescr_Type()
)
ethOamDestNeDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeDescr.setStatus("current")
_EthOamDestNeConvertedIndex_Type = Unsigned32
_EthOamDestNeConvertedIndex_Object = MibTableColumn
ethOamDestNeConvertedIndex = _EthOamDestNeConvertedIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 62),
    _EthOamDestNeConvertedIndex_Type()
)
ethOamDestNeConvertedIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeConvertedIndex.setStatus("current")


class _EthOamDestNeSlmDataTlvLength_Type(Unsigned32):
    """Custom type ethOamDestNeSlmDataTlvLength based on Unsigned32"""
    defaultValue = 0


_EthOamDestNeSlmDataTlvLength_Type.__name__ = "Unsigned32"
_EthOamDestNeSlmDataTlvLength_Object = MibTableColumn
ethOamDestNeSlmDataTlvLength = _EthOamDestNeSlmDataTlvLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 63),
    _EthOamDestNeSlmDataTlvLength_Type()
)
ethOamDestNeSlmDataTlvLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeSlmDataTlvLength.setStatus("current")


class _EthOamDestNeLmMode_Type(Integer32):
    """Custom type ethOamDestNeLmMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("txAndRx", 2))
    )


_EthOamDestNeLmMode_Type.__name__ = "Integer32"
_EthOamDestNeLmMode_Object = MibTableColumn
ethOamDestNeLmMode = _EthOamDestNeLmMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 64),
    _EthOamDestNeLmMode_Type()
)
ethOamDestNeLmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeLmMode.setStatus("current")


class _EthOamDestNeSlmTestId_Type(Unsigned32):
    """Custom type ethOamDestNeSlmTestId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_EthOamDestNeSlmTestId_Type.__name__ = "Unsigned32"
_EthOamDestNeSlmTestId_Object = MibTableColumn
ethOamDestNeSlmTestId = _EthOamDestNeSlmTestId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 65),
    _EthOamDestNeSlmTestId_Type()
)
ethOamDestNeSlmTestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeSlmTestId.setStatus("current")


class _EthOamDestNeForwardDelayVarBinProfile_Type(Unsigned32):
    """Custom type ethOamDestNeForwardDelayVarBinProfile based on Unsigned32"""
    defaultValue = 0


_EthOamDestNeForwardDelayVarBinProfile_Type.__name__ = "Unsigned32"
_EthOamDestNeForwardDelayVarBinProfile_Object = MibTableColumn
ethOamDestNeForwardDelayVarBinProfile = _EthOamDestNeForwardDelayVarBinProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 66),
    _EthOamDestNeForwardDelayVarBinProfile_Type()
)
ethOamDestNeForwardDelayVarBinProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeForwardDelayVarBinProfile.setStatus("current")


class _EthOamDestNeBackwardDelayVarBinProfile_Type(Unsigned32):
    """Custom type ethOamDestNeBackwardDelayVarBinProfile based on Unsigned32"""
    defaultValue = 0


_EthOamDestNeBackwardDelayVarBinProfile_Type.__name__ = "Unsigned32"
_EthOamDestNeBackwardDelayVarBinProfile_Object = MibTableColumn
ethOamDestNeBackwardDelayVarBinProfile = _EthOamDestNeBackwardDelayVarBinProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 67),
    _EthOamDestNeBackwardDelayVarBinProfile_Type()
)
ethOamDestNeBackwardDelayVarBinProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamDestNeBackwardDelayVarBinProfile.setStatus("current")
_EthOamDestNeAvailableIndForward_Type = Counter32
_EthOamDestNeAvailableIndForward_Object = MibTableColumn
ethOamDestNeAvailableIndForward = _EthOamDestNeAvailableIndForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 68),
    _EthOamDestNeAvailableIndForward_Type()
)
ethOamDestNeAvailableIndForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeAvailableIndForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeAvailableIndForward.setUnits("seconds")
_EthOamDestNeAvailableIndBackward_Type = Counter32
_EthOamDestNeAvailableIndBackward_Object = MibTableColumn
ethOamDestNeAvailableIndBackward = _EthOamDestNeAvailableIndBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 69),
    _EthOamDestNeAvailableIndBackward_Type()
)
ethOamDestNeAvailableIndBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeAvailableIndBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeAvailableIndBackward.setUnits("seconds")
_EthOamDestNeDelayVariationForward_Type = Unsigned32
_EthOamDestNeDelayVariationForward_Object = MibTableColumn
ethOamDestNeDelayVariationForward = _EthOamDestNeDelayVariationForward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 70),
    _EthOamDestNeDelayVariationForward_Type()
)
ethOamDestNeDelayVariationForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeDelayVariationForward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeDelayVariationForward.setUnits("microseconds")
_EthOamDestNeDelayVariationBackward_Type = Unsigned32
_EthOamDestNeDelayVariationBackward_Object = MibTableColumn
ethOamDestNeDelayVariationBackward = _EthOamDestNeDelayVariationBackward_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 5, 1, 71),
    _EthOamDestNeDelayVariationBackward_Type()
)
ethOamDestNeDelayVariationBackward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDestNeDelayVariationBackward.setStatus("current")
if mibBuilder.loadTexts:
    ethOamDestNeDelayVariationBackward.setUnits("microseconds")
_EthOamSvcRmonConfigTable_Object = MibTable
ethOamSvcRmonConfigTable = _EthOamSvcRmonConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigTable.setStatus("current")
_EthOamSvcRmonConfigEntry_Object = MibTableRow
ethOamSvcRmonConfigEntry = _EthOamSvcRmonConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1)
)
ethOamSvcRmonConfigEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamSvcRmonConfigPerfAttrib"),
)
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigEntry.setStatus("current")


class _EthOamSvcRmonConfigPerfAttrib_Type(Integer32):
    """Custom type ethOamSvcRmonConfigPerfAttrib based on Integer32"""
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
        *(("framesAboveDelay", 1),
          ("framesAboveDelayVar", 2),
          ("farEndFrameLossRatio", 3),
          ("nearEndFrameLossRatio", 4),
          ("unavailabilityRatio", 5),
          ("farEndUnavailabilityRatio", 6),
          ("nearEndUnavailabilityRatio", 7))
    )


_EthOamSvcRmonConfigPerfAttrib_Type.__name__ = "Integer32"
_EthOamSvcRmonConfigPerfAttrib_Object = MibTableColumn
ethOamSvcRmonConfigPerfAttrib = _EthOamSvcRmonConfigPerfAttrib_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1, 1),
    _EthOamSvcRmonConfigPerfAttrib_Type()
)
ethOamSvcRmonConfigPerfAttrib.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigPerfAttrib.setStatus("current")
_EthOamSvcRmonConfigRowStatus_Type = RowStatus
_EthOamSvcRmonConfigRowStatus_Object = MibTableColumn
ethOamSvcRmonConfigRowStatus = _EthOamSvcRmonConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1, 2),
    _EthOamSvcRmonConfigRowStatus_Type()
)
ethOamSvcRmonConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigRowStatus.setStatus("current")
_EthOamSvcRmonConfigAlarmInterval_Type = Integer32
_EthOamSvcRmonConfigAlarmInterval_Object = MibTableColumn
ethOamSvcRmonConfigAlarmInterval = _EthOamSvcRmonConfigAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1, 3),
    _EthOamSvcRmonConfigAlarmInterval_Type()
)
ethOamSvcRmonConfigAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigAlarmInterval.setStatus("current")
_EthOamSvcRmonConfigAlarmRisingThresh_Type = Integer32
_EthOamSvcRmonConfigAlarmRisingThresh_Object = MibTableColumn
ethOamSvcRmonConfigAlarmRisingThresh = _EthOamSvcRmonConfigAlarmRisingThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1, 4),
    _EthOamSvcRmonConfigAlarmRisingThresh_Type()
)
ethOamSvcRmonConfigAlarmRisingThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigAlarmRisingThresh.setStatus("current")
_EthOamSvcRmonConfigAlarmFallingThresh_Type = Integer32
_EthOamSvcRmonConfigAlarmFallingThresh_Object = MibTableColumn
ethOamSvcRmonConfigAlarmFallingThresh = _EthOamSvcRmonConfigAlarmFallingThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1, 5),
    _EthOamSvcRmonConfigAlarmFallingThresh_Type()
)
ethOamSvcRmonConfigAlarmFallingThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigAlarmFallingThresh.setStatus("current")


class _EthOamSvcRmonConfigEventType_Type(Integer32):
    """Custom type ethOamSvcRmonConfigEventType based on Integer32"""
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
        *(("none", 1),
          ("log", 2),
          ("snmptrap", 3),
          ("logandtrap", 4))
    )


_EthOamSvcRmonConfigEventType_Type.__name__ = "Integer32"
_EthOamSvcRmonConfigEventType_Object = MibTableColumn
ethOamSvcRmonConfigEventType = _EthOamSvcRmonConfigEventType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 6, 1, 6),
    _EthOamSvcRmonConfigEventType_Type()
)
ethOamSvcRmonConfigEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamSvcRmonConfigEventType.setStatus("current")
_EthOamMeasureBinProfileTable_Object = MibTable
ethOamMeasureBinProfileTable = _EthOamMeasureBinProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    ethOamMeasureBinProfileTable.setStatus("current")
_EthOamMeasureBinProfileEntry_Object = MibTableRow
ethOamMeasureBinProfileEntry = _EthOamMeasureBinProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 7, 1)
)
ethOamMeasureBinProfileEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "ethOamMeasureBinProfileIndex"),
)
if mibBuilder.loadTexts:
    ethOamMeasureBinProfileEntry.setStatus("current")
_EthOamMeasureBinProfileIndex_Type = Unsigned32
_EthOamMeasureBinProfileIndex_Object = MibTableColumn
ethOamMeasureBinProfileIndex = _EthOamMeasureBinProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 7, 1, 1),
    _EthOamMeasureBinProfileIndex_Type()
)
ethOamMeasureBinProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMeasureBinProfileIndex.setStatus("current")
_EthOamMeasureBinProfileRowStatus_Type = RowStatus
_EthOamMeasureBinProfileRowStatus_Object = MibTableColumn
ethOamMeasureBinProfileRowStatus = _EthOamMeasureBinProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 7, 1, 2),
    _EthOamMeasureBinProfileRowStatus_Type()
)
ethOamMeasureBinProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamMeasureBinProfileRowStatus.setStatus("current")
_EthOamMeasureBinProfileName_Type = SnmpAdminString
_EthOamMeasureBinProfileName_Object = MibTableColumn
ethOamMeasureBinProfileName = _EthOamMeasureBinProfileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 7, 1, 3),
    _EthOamMeasureBinProfileName_Type()
)
ethOamMeasureBinProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamMeasureBinProfileName.setStatus("current")


class _EthOamMeasureBinThresh_Type(OctetString):
    """Custom type ethOamMeasureBinThresh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(36, 36),
    )
    fixed_length = 36


_EthOamMeasureBinThresh_Type.__name__ = "OctetString"
_EthOamMeasureBinThresh_Object = MibTableColumn
ethOamMeasureBinThresh = _EthOamMeasureBinThresh_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 7, 1, 4),
    _EthOamMeasureBinThresh_Type()
)
ethOamMeasureBinThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamMeasureBinThresh.setStatus("current")
_EthOamDelayCurrentBinsTable_Object = MibTable
ethOamDelayCurrentBinsTable = _EthOamDelayCurrentBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    ethOamDelayCurrentBinsTable.setStatus("current")
_EthOamDelayCurrentBinsEntry_Object = MibTableRow
ethOamDelayCurrentBinsEntry = _EthOamDelayCurrentBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 8, 1)
)
ethOamDelayCurrentBinsEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamDelayCurrentBinCounterType"),
    (0, "RAD-OamCfm-MIB", "ethOamDelayCurrentBinNumber"),
)
if mibBuilder.loadTexts:
    ethOamDelayCurrentBinsEntry.setStatus("current")
_EthOamDelayCurrentBinCounterType_Type = EthOamBinCounterType
_EthOamDelayCurrentBinCounterType_Object = MibTableColumn
ethOamDelayCurrentBinCounterType = _EthOamDelayCurrentBinCounterType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 8, 1, 1),
    _EthOamDelayCurrentBinCounterType_Type()
)
ethOamDelayCurrentBinCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamDelayCurrentBinCounterType.setStatus("current")


class _EthOamDelayCurrentBinNumber_Type(Unsigned32):
    """Custom type ethOamDelayCurrentBinNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EthOamDelayCurrentBinNumber_Type.__name__ = "Unsigned32"
_EthOamDelayCurrentBinNumber_Object = MibTableColumn
ethOamDelayCurrentBinNumber = _EthOamDelayCurrentBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 8, 1, 2),
    _EthOamDelayCurrentBinNumber_Type()
)
ethOamDelayCurrentBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamDelayCurrentBinNumber.setStatus("current")
_EthOamDelayCurrentBinValue_Type = PerfCurrentCount
_EthOamDelayCurrentBinValue_Object = MibTableColumn
ethOamDelayCurrentBinValue = _EthOamDelayCurrentBinValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 8, 1, 3),
    _EthOamDelayCurrentBinValue_Type()
)
ethOamDelayCurrentBinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDelayCurrentBinValue.setStatus("current")
_EthOamDelayIntervalBinsTable_Object = MibTable
ethOamDelayIntervalBinsTable = _EthOamDelayIntervalBinsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 10)
)
if mibBuilder.loadTexts:
    ethOamDelayIntervalBinsTable.setStatus("current")
_EthOamDelayIntervalBinsEntry_Object = MibTableRow
ethOamDelayIntervalBinsEntry = _EthOamDelayIntervalBinsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 10, 1)
)
ethOamDelayIntervalBinsEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radOamEvcIdx"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamServiceIdx"),
    (0, "RAD-OamCfm-MIB", "ethOamSvcIntervalNum"),
    (0, "RAD-OamCfm-MIB", "ethOamDelayIntervalBinCounterType"),
    (0, "RAD-OamCfm-MIB", "ethOamDelayIntervalBinNumber"),
)
if mibBuilder.loadTexts:
    ethOamDelayIntervalBinsEntry.setStatus("current")
_EthOamDelayIntervalBinCounterType_Type = EthOamBinCounterType
_EthOamDelayIntervalBinCounterType_Object = MibTableColumn
ethOamDelayIntervalBinCounterType = _EthOamDelayIntervalBinCounterType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 10, 1, 1),
    _EthOamDelayIntervalBinCounterType_Type()
)
ethOamDelayIntervalBinCounterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamDelayIntervalBinCounterType.setStatus("current")


class _EthOamDelayIntervalBinNumber_Type(Unsigned32):
    """Custom type ethOamDelayIntervalBinNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EthOamDelayIntervalBinNumber_Type.__name__ = "Unsigned32"
_EthOamDelayIntervalBinNumber_Object = MibTableColumn
ethOamDelayIntervalBinNumber = _EthOamDelayIntervalBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 10, 1, 2),
    _EthOamDelayIntervalBinNumber_Type()
)
ethOamDelayIntervalBinNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamDelayIntervalBinNumber.setStatus("current")
_EthOamDelayIntervalBinValue_Type = PerfIntervalCount
_EthOamDelayIntervalBinValue_Object = MibTableColumn
ethOamDelayIntervalBinValue = _EthOamDelayIntervalBinValue_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 2, 10, 1, 3),
    _EthOamDelayIntervalBinValue_Type()
)
ethOamDelayIntervalBinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamDelayIntervalBinValue.setStatus("current")
_RadMdTable_Object = MibTable
radMdTable = _RadMdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 3)
)
if mibBuilder.loadTexts:
    radMdTable.setStatus("current")
_RadMdEntry_Object = MibTableRow
radMdEntry = _RadMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 3, 1)
)
radMdEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radMdIndex"),
)
if mibBuilder.loadTexts:
    radMdEntry.setStatus("current")
_RadMdIndex_Type = Unsigned32
_RadMdIndex_Object = MibTableColumn
radMdIndex = _RadMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 3, 1, 1),
    _RadMdIndex_Type()
)
radMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radMdIndex.setStatus("current")


class _RadMdFormat_Type(Integer32):
    """Custom type radMdFormat based on Integer32"""
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
        *(("none", 1),
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("charString", 4))
    )


_RadMdFormat_Type.__name__ = "Integer32"
_RadMdFormat_Object = MibTableColumn
radMdFormat = _RadMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 3, 1, 2),
    _RadMdFormat_Type()
)
radMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMdFormat.setStatus("current")


class _RadMdName_Type(OctetString):
    """Custom type radMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )


_RadMdName_Type.__name__ = "OctetString"
_RadMdName_Object = MibTableColumn
radMdName = _RadMdName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 3, 1, 3),
    _RadMdName_Type()
)
radMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMdName.setStatus("current")
_RadMdRowStatus_Type = RowStatus
_RadMdRowStatus_Object = MibTableColumn
radMdRowStatus = _RadMdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 3, 1, 4),
    _RadMdRowStatus_Type()
)
radMdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMdRowStatus.setStatus("current")
_RadMepLtrTable_Object = MibTable
radMepLtrTable = _RadMepLtrTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4)
)
if mibBuilder.loadTexts:
    radMepLtrTable.setStatus("current")
_RadMepLtrEntry_Object = MibTableRow
radMepLtrEntry = _RadMepLtrEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1)
)
radMepLtrEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "radMepLtrReceiveOrder"),
)
if mibBuilder.loadTexts:
    radMepLtrEntry.setStatus("current")
_RadMepLtrReceiveOrder_Type = Unsigned32
_RadMepLtrReceiveOrder_Object = MibTableColumn
radMepLtrReceiveOrder = _RadMepLtrReceiveOrder_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 1),
    _RadMepLtrReceiveOrder_Type()
)
radMepLtrReceiveOrder.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radMepLtrReceiveOrder.setStatus("current")


class _RadMepLtrTtl_Type(Unsigned32):
    """Custom type radMepLtrTtl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RadMepLtrTtl_Type.__name__ = "Unsigned32"
_RadMepLtrTtl_Object = MibTableColumn
radMepLtrTtl = _RadMepLtrTtl_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 2),
    _RadMepLtrTtl_Type()
)
radMepLtrTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrTtl.setStatus("current")
_RadMepLtrMacAddr_Type = MacAddress
_RadMepLtrMacAddr_Object = MibTableColumn
radMepLtrMacAddr = _RadMepLtrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 3),
    _RadMepLtrMacAddr_Type()
)
radMepLtrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrMacAddr.setStatus("current")


class _RadMepLtrRelay_Type(Integer32):
    """Custom type radMepLtrRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rlyHit", 1),
          ("rlyFdb", 2),
          ("rlyMpdb", 3))
    )


_RadMepLtrRelay_Type.__name__ = "Integer32"
_RadMepLtrRelay_Object = MibTableColumn
radMepLtrRelay = _RadMepLtrRelay_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 4),
    _RadMepLtrRelay_Type()
)
radMepLtrRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrRelay.setStatus("current")


class _RadMepLtrIngress_Type(Integer32):
    """Custom type radMepLtrIngress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ingNoTlv", 1),
          ("ingOk", 2),
          ("ingDown", 3),
          ("ingBlocked", 4),
          ("ingVid", 5))
    )


_RadMepLtrIngress_Type.__name__ = "Integer32"
_RadMepLtrIngress_Object = MibTableColumn
radMepLtrIngress = _RadMepLtrIngress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 5),
    _RadMepLtrIngress_Type()
)
radMepLtrIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrIngress.setStatus("current")
_RadMepLtrIngressPortIdSubtype_Type = LldpPortIdSubtype
_RadMepLtrIngressPortIdSubtype_Object = MibTableColumn
radMepLtrIngressPortIdSubtype = _RadMepLtrIngressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 6),
    _RadMepLtrIngressPortIdSubtype_Type()
)
radMepLtrIngressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrIngressPortIdSubtype.setStatus("current")


class _RadMepLtrIngressPortId_Type(OctetString):
    """Custom type radMepLtrIngressPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RadMepLtrIngressPortId_Type.__name__ = "OctetString"
_RadMepLtrIngressPortId_Object = MibTableColumn
radMepLtrIngressPortId = _RadMepLtrIngressPortId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 7),
    _RadMepLtrIngressPortId_Type()
)
radMepLtrIngressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrIngressPortId.setStatus("current")


class _RadMepLtrEgress_Type(Integer32):
    """Custom type radMepLtrEgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("egrNoTlv", 1),
          ("egrOK", 2),
          ("egrDown", 3),
          ("egrBlocked", 4),
          ("egrVid", 5))
    )


_RadMepLtrEgress_Type.__name__ = "Integer32"
_RadMepLtrEgress_Object = MibTableColumn
radMepLtrEgress = _RadMepLtrEgress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 8),
    _RadMepLtrEgress_Type()
)
radMepLtrEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrEgress.setStatus("current")
_RadMepLtrEgressPortIdSubtype_Type = LldpPortIdSubtype
_RadMepLtrEgressPortIdSubtype_Object = MibTableColumn
radMepLtrEgressPortIdSubtype = _RadMepLtrEgressPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 9),
    _RadMepLtrEgressPortIdSubtype_Type()
)
radMepLtrEgressPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrEgressPortIdSubtype.setStatus("current")


class _RadMepLtrEgressPortId_Type(OctetString):
    """Custom type radMepLtrEgressPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RadMepLtrEgressPortId_Type.__name__ = "OctetString"
_RadMepLtrEgressPortId_Object = MibTableColumn
radMepLtrEgressPortId = _RadMepLtrEgressPortId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 4, 1, 10),
    _RadMepLtrEgressPortId_Type()
)
radMepLtrEgressPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepLtrEgressPortId.setStatus("current")
_RadMepCcStatusTable_Object = MibTable
radMepCcStatusTable = _RadMepCcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 5)
)
if mibBuilder.loadTexts:
    radMepCcStatusTable.setStatus("current")
_RadMepCcStatusEntry_Object = MibTableRow
radMepCcStatusEntry = _RadMepCcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 5, 1)
)
radMepCcStatusEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "radOamIdx1"),
    (0, "RAD-OamCfm-MIB", "radMepIdx"),
    (0, "RAD-OamCfm-MIB", "radMepRemoteMepIdx"),
)
if mibBuilder.loadTexts:
    radMepCcStatusEntry.setStatus("current")
_RadMepRemoteMepIdx_Type = Unsigned32
_RadMepRemoteMepIdx_Object = MibTableColumn
radMepRemoteMepIdx = _RadMepRemoteMepIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 5, 1, 1),
    _RadMepRemoteMepIdx_Type()
)
radMepRemoteMepIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radMepRemoteMepIdx.setStatus("current")
_RadMepCcStatusRemMepId_Type = Unsigned32
_RadMepCcStatusRemMepId_Object = MibTableColumn
radMepCcStatusRemMepId = _RadMepCcStatusRemMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 5, 1, 2),
    _RadMepCcStatusRemMepId_Type()
)
radMepCcStatusRemMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radMepCcStatusRemMepId.setStatus("current")


class _RadMepCcStat_Type(Integer32):
    """Custom type radMepCcStat based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("fail", 2),
          ("ok", 3),
          ("mismerge", 4),
          ("unexpectedMep", 5),
          ("unexpectedMeLevel", 6),
          ("unexpectedPeriod", 7),
          ("rdi", 8))
    )


_RadMepCcStat_Type.__name__ = "Integer32"
_RadMepCcStat_Object = MibTableColumn
radMepCcStat = _RadMepCcStat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 5, 1, 3),
    _RadMepCcStat_Type()
)
radMepCcStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepCcStat.setStatus("current")
_RadMepCcStatusMacAddr_Type = MacAddress
_RadMepCcStatusMacAddr_Object = MibTableColumn
radMepCcStatusMacAddr = _RadMepCcStatusMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 5, 1, 4),
    _RadMepCcStatusMacAddr_Type()
)
radMepCcStatusMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radMepCcStatusMacAddr.setStatus("current")
_EthOamStdEtherType_Type = Unsigned32
_EthOamStdEtherType_Object = MibScalar
ethOamStdEtherType = _EthOamStdEtherType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 6),
    _EthOamStdEtherType_Type()
)
ethOamStdEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamStdEtherType.setStatus("current")
_EthOamStdMacAddress_Type = MacAddress
_EthOamStdMacAddress_Object = MibScalar
ethOamStdMacAddress = _EthOamStdMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 7),
    _EthOamStdMacAddress_Type()
)
ethOamStdMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamStdMacAddress.setStatus("current")
_Dot1agXCfmMdTable_Object = MibTable
dot1agXCfmMdTable = _Dot1agXCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 8)
)
if mibBuilder.loadTexts:
    dot1agXCfmMdTable.setStatus("current")
_Dot1agXCfmMdEntry_Object = MibTableRow
dot1agXCfmMdEntry = _Dot1agXCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 8, 1)
)
dot1agXCfmMdEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
)
if mibBuilder.loadTexts:
    dot1agXCfmMdEntry.setStatus("current")


class _Dot1agXCfmMdProtocol_Type(Integer32):
    """Custom type dot1agXCfmMdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preStandard", 1),
          ("standard", 2))
    )


_Dot1agXCfmMdProtocol_Type.__name__ = "Integer32"
_Dot1agXCfmMdProtocol_Object = MibTableColumn
dot1agXCfmMdProtocol = _Dot1agXCfmMdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 8, 1, 1),
    _Dot1agXCfmMdProtocol_Type()
)
dot1agXCfmMdProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMdProtocol.setStatus("current")
_Dot1agXCfmMepTable_Object = MibTable
dot1agXCfmMepTable = _Dot1agXCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9)
)
if mibBuilder.loadTexts:
    dot1agXCfmMepTable.setStatus("current")
_Dot1agXCfmMepEntry_Object = MibTableRow
dot1agXCfmMepEntry = _Dot1agXCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1)
)
dot1agXCfmMepEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agXCfmMepEntry.setStatus("current")


class _Dot1agXCfmMepContinuityVerMode_Type(Integer32):
    """Custom type dot1agXCfmMepContinuityVerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("ccBased", 3),
          ("lbBased", 4))
    )


_Dot1agXCfmMepContinuityVerMode_Type.__name__ = "Integer32"
_Dot1agXCfmMepContinuityVerMode_Object = MibTableColumn
dot1agXCfmMepContinuityVerMode = _Dot1agXCfmMepContinuityVerMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 1),
    _Dot1agXCfmMepContinuityVerMode_Type()
)
dot1agXCfmMepContinuityVerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepContinuityVerMode.setStatus("current")


class _Dot1agXCfmMepDestAddrType_Type(Integer32):
    """Custom type dot1agXCfmMepDestAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_Dot1agXCfmMepDestAddrType_Type.__name__ = "Integer32"
_Dot1agXCfmMepDestAddrType_Object = MibTableColumn
dot1agXCfmMepDestAddrType = _Dot1agXCfmMepDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 2),
    _Dot1agXCfmMepDestAddrType_Type()
)
dot1agXCfmMepDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepDestAddrType.setStatus("current")
_Dot1agXCfmMepDestMacAddr_Type = MacAddress
_Dot1agXCfmMepDestMacAddr_Object = MibTableColumn
dot1agXCfmMepDestMacAddr = _Dot1agXCfmMepDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 3),
    _Dot1agXCfmMepDestMacAddr_Type()
)
dot1agXCfmMepDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepDestMacAddr.setStatus("current")
_Dot1agXCfmMepMappingProfile_Type = Unsigned32
_Dot1agXCfmMepMappingProfile_Object = MibTableColumn
dot1agXCfmMepMappingProfile = _Dot1agXCfmMepMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 4),
    _Dot1agXCfmMepMappingProfile_Type()
)
dot1agXCfmMepMappingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepMappingProfile.setStatus("current")
_Dot1agXCfmMepQBlock_Type = ObjectIdentifier
_Dot1agXCfmMepQBlock_Object = MibTableColumn
dot1agXCfmMepQBlock = _Dot1agXCfmMepQBlock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 5),
    _Dot1agXCfmMepQBlock_Type()
)
dot1agXCfmMepQBlock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepQBlock.setStatus("current")
_Dot1agXCfmMepFixedQueueMapping_Type = Unsigned32
_Dot1agXCfmMepFixedQueueMapping_Object = MibTableColumn
dot1agXCfmMepFixedQueueMapping = _Dot1agXCfmMepFixedQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 6),
    _Dot1agXCfmMepFixedQueueMapping_Type()
)
dot1agXCfmMepFixedQueueMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepFixedQueueMapping.setStatus("current")
_Dot1agXCfmMepQueueMappingProfile_Type = Unsigned32
_Dot1agXCfmMepQueueMappingProfile_Object = MibTableColumn
dot1agXCfmMepQueueMappingProfile = _Dot1agXCfmMepQueueMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 7),
    _Dot1agXCfmMepQueueMappingProfile_Type()
)
dot1agXCfmMepQueueMappingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepQueueMappingProfile.setStatus("current")
_Dot1agXCfmMepConvertedIndex_Type = Unsigned32
_Dot1agXCfmMepConvertedIndex_Object = MibTableColumn
dot1agXCfmMepConvertedIndex = _Dot1agXCfmMepConvertedIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 8),
    _Dot1agXCfmMepConvertedIndex_Type()
)
dot1agXCfmMepConvertedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepConvertedIndex.setStatus("current")


class _Dot1agXCfmMepPmDestAddrType_Type(Integer32):
    """Custom type dot1agXCfmMepPmDestAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2))
    )


_Dot1agXCfmMepPmDestAddrType_Type.__name__ = "Integer32"
_Dot1agXCfmMepPmDestAddrType_Object = MibTableColumn
dot1agXCfmMepPmDestAddrType = _Dot1agXCfmMepPmDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 9),
    _Dot1agXCfmMepPmDestAddrType_Type()
)
dot1agXCfmMepPmDestAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepPmDestAddrType.setStatus("current")


class _Dot1agXCfmMepForwardingMode_Type(Integer32):
    """Custom type dot1agXCfmMepForwardingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eline", 1),
          ("elan", 2))
    )


_Dot1agXCfmMepForwardingMode_Type.__name__ = "Integer32"
_Dot1agXCfmMepForwardingMode_Object = MibTableColumn
dot1agXCfmMepForwardingMode = _Dot1agXCfmMepForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 10),
    _Dot1agXCfmMepForwardingMode_Type()
)
dot1agXCfmMepForwardingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepForwardingMode.setStatus("current")


class _Dot1agXCfmMepLbmDataTlvLength_Type(Unsigned32):
    """Custom type dot1agXCfmMepLbmDataTlvLength based on Unsigned32"""
    defaultValue = 0


_Dot1agXCfmMepLbmDataTlvLength_Type.__name__ = "Unsigned32"
_Dot1agXCfmMepLbmDataTlvLength_Object = MibTableColumn
dot1agXCfmMepLbmDataTlvLength = _Dot1agXCfmMepLbmDataTlvLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 11),
    _Dot1agXCfmMepLbmDataTlvLength_Type()
)
dot1agXCfmMepLbmDataTlvLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepLbmDataTlvLength.setStatus("current")


class _Dot1agXCfmMepClientMdLevel_Type(Unsigned32):
    """Custom type dot1agXCfmMepClientMdLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agXCfmMepClientMdLevel_Type.__name__ = "Unsigned32"
_Dot1agXCfmMepClientMdLevel_Object = MibTableColumn
dot1agXCfmMepClientMdLevel = _Dot1agXCfmMepClientMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 12),
    _Dot1agXCfmMepClientMdLevel_Type()
)
dot1agXCfmMepClientMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepClientMdLevel.setStatus("current")


class _Dot1agXCfmMepAisTransmit_Type(Integer32):
    """Custom type dot1agXCfmMepAisTransmit based on Integer32"""
    defaultValue = 2

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


_Dot1agXCfmMepAisTransmit_Type.__name__ = "Integer32"
_Dot1agXCfmMepAisTransmit_Object = MibTableColumn
dot1agXCfmMepAisTransmit = _Dot1agXCfmMepAisTransmit_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 13),
    _Dot1agXCfmMepAisTransmit_Type()
)
dot1agXCfmMepAisTransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepAisTransmit.setStatus("current")


class _Dot1agXCfmMepAisInterval_Type(Dot1agCfmCcmInterval):
    """Custom type dot1agXCfmMepAisInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 4


_Dot1agXCfmMepAisInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_Dot1agXCfmMepAisInterval_Object = MibTableColumn
dot1agXCfmMepAisInterval = _Dot1agXCfmMepAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 14),
    _Dot1agXCfmMepAisInterval_Type()
)
dot1agXCfmMepAisInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepAisInterval.setStatus("current")


class _Dot1agXCfmMepAisPriority_Type(Unsigned32):
    """Custom type dot1agXCfmMepAisPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot1agXCfmMepAisPriority_Type.__name__ = "Unsigned32"
_Dot1agXCfmMepAisPriority_Object = MibTableColumn
dot1agXCfmMepAisPriority = _Dot1agXCfmMepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 15),
    _Dot1agXCfmMepAisPriority_Type()
)
dot1agXCfmMepAisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepAisPriority.setStatus("current")


class _Dot1agXCfmMepDefects_Type(Bits):
    """Custom type dot1agXCfmMepDefects based on Bits"""
    namedValues = NamedValues(
        *(("bDefAIS", 0),
          ("bDefLCK", 1))
    )

_Dot1agXCfmMepDefects_Type.__name__ = "Bits"
_Dot1agXCfmMepDefects_Object = MibTableColumn
dot1agXCfmMepDefects = _Dot1agXCfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 16),
    _Dot1agXCfmMepDefects_Type()
)
dot1agXCfmMepDefects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepDefects.setStatus("current")


class _Dot1agXCfmMepLastAlarmDefect_Type(Integer32):
    """Custom type dot1agXCfmMepLastAlarmDefect based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("defRDICCM", 2),
          ("defMACstatus", 3),
          ("defRemoteCCM", 4),
          ("defErrorCCM", 5),
          ("defXconCCM", 6),
          ("defAIS", 7),
          ("defLCK", 8))
    )


_Dot1agXCfmMepLastAlarmDefect_Type.__name__ = "Integer32"
_Dot1agXCfmMepLastAlarmDefect_Object = MibTableColumn
dot1agXCfmMepLastAlarmDefect = _Dot1agXCfmMepLastAlarmDefect_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 17),
    _Dot1agXCfmMepLastAlarmDefect_Type()
)
dot1agXCfmMepLastAlarmDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepLastAlarmDefect.setStatus("current")
_Dot1agXCfmMepCosMapping_Type = Unsigned32
_Dot1agXCfmMepCosMapping_Object = MibTableColumn
dot1agXCfmMepCosMapping = _Dot1agXCfmMepCosMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 19),
    _Dot1agXCfmMepCosMapping_Type()
)
dot1agXCfmMepCosMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepCosMapping.setStatus("current")
_Dot1agXCfmMepCosMappingProfile_Type = Unsigned32
_Dot1agXCfmMepCosMappingProfile_Object = MibTableColumn
dot1agXCfmMepCosMappingProfile = _Dot1agXCfmMepCosMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 20),
    _Dot1agXCfmMepCosMappingProfile_Type()
)
dot1agXCfmMepCosMappingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepCosMappingProfile.setStatus("current")


class _Dot1agXCfmMepCcStatus_Type(Bits):
    """Custom type dot1agXCfmMepCcStatus based on Bits"""
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("otherFail", 1),
          ("mismerge", 2),
          ("unexpectedMep", 3),
          ("unexpectedMepLevel", 4),
          ("unexpectedPeriod", 5))
    )

_Dot1agXCfmMepCcStatus_Type.__name__ = "Bits"
_Dot1agXCfmMepCcStatus_Object = MibTableColumn
dot1agXCfmMepCcStatus = _Dot1agXCfmMepCcStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 24),
    _Dot1agXCfmMepCcStatus_Type()
)
dot1agXCfmMepCcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepCcStatus.setStatus("current")


class _Dot1agXCfmMepStatus_Type(Integer32):
    """Custom type dot1agXCfmMepStatus based on Integer32"""
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
        *(("none", 1),
          ("y1564", 2),
          ("rfc2544", 3),
          ("mef46Loop", 4))
    )


_Dot1agXCfmMepStatus_Type.__name__ = "Integer32"
_Dot1agXCfmMepStatus_Object = MibTableColumn
dot1agXCfmMepStatus = _Dot1agXCfmMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 28),
    _Dot1agXCfmMepStatus_Type()
)
dot1agXCfmMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepStatus.setStatus("current")
_Dot1agXCfmMepExcludeCustomerTags_Type = TruthValue
_Dot1agXCfmMepExcludeCustomerTags_Object = MibTableColumn
dot1agXCfmMepExcludeCustomerTags = _Dot1agXCfmMepExcludeCustomerTags_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 29),
    _Dot1agXCfmMepExcludeCustomerTags_Type()
)
dot1agXCfmMepExcludeCustomerTags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepExcludeCustomerTags.setStatus("current")


class _Dot1agXCfmMepClearStatsCmd_Type(Integer32):
    """Custom type dot1agXCfmMepClearStatsCmd based on Integer32"""
    defaultValue = 2

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


_Dot1agXCfmMepClearStatsCmd_Type.__name__ = "Integer32"
_Dot1agXCfmMepClearStatsCmd_Object = MibTableColumn
dot1agXCfmMepClearStatsCmd = _Dot1agXCfmMepClearStatsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 30),
    _Dot1agXCfmMepClearStatsCmd_Type()
)
dot1agXCfmMepClearStatsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMepClearStatsCmd.setStatus("current")


class _Dot1agXCfmMepTimeElapsed_Type(Unsigned32):
    """Custom type dot1agXCfmMepTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_Dot1agXCfmMepTimeElapsed_Type.__name__ = "Unsigned32"
_Dot1agXCfmMepTimeElapsed_Object = MibTableColumn
dot1agXCfmMepTimeElapsed = _Dot1agXCfmMepTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 31),
    _Dot1agXCfmMepTimeElapsed_Type()
)
dot1agXCfmMepTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepTimeElapsed.setStatus("current")
_Dot1agXCfmMepCcmTx_Type = Counter64
_Dot1agXCfmMepCcmTx_Object = MibTableColumn
dot1agXCfmMepCcmTx = _Dot1agXCfmMepCcmTx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 9, 1, 32),
    _Dot1agXCfmMepCcmTx_Type()
)
dot1agXCfmMepCcmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepCcmTx.setStatus("current")
_Dot1agXCfmMepDbTable_Object = MibTable
dot1agXCfmMepDbTable = _Dot1agXCfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 10)
)
if mibBuilder.loadTexts:
    dot1agXCfmMepDbTable.setStatus("deprecated")
_Dot1agXCfmMepDbEntry_Object = MibTableRow
dot1agXCfmMepDbEntry = _Dot1agXCfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 10, 1)
)
dot1agXCfmMepDbEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agXCfmMepDbEntry.setStatus("deprecated")


class _Dot1agXCfmMepCcStat_Type(Integer32):
    """Custom type dot1agXCfmMepCcStat based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("fail", 2),
          ("ok", 3),
          ("mismerge", 4),
          ("unexpectedMep", 5),
          ("unexpectedMeLevel", 6),
          ("unexpectedPeriod", 7),
          ("rdi", 8))
    )


_Dot1agXCfmMepCcStat_Type.__name__ = "Integer32"
_Dot1agXCfmMepCcStat_Object = MibTableColumn
dot1agXCfmMepCcStat = _Dot1agXCfmMepCcStat_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 10, 1, 1),
    _Dot1agXCfmMepCcStat_Type()
)
dot1agXCfmMepCcStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMepCcStat.setStatus("deprecated")
_Dot1agXCfmMepDbConvertedIndex_Type = Unsigned32
_Dot1agXCfmMepDbConvertedIndex_Object = MibTableColumn
dot1agXCfmMepDbConvertedIndex = _Dot1agXCfmMepDbConvertedIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 10, 1, 2),
    _Dot1agXCfmMepDbConvertedIndex_Type()
)
dot1agXCfmMepDbConvertedIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1agXCfmMepDbConvertedIndex.setStatus("deprecated")
_Dot1agXCfmMaMepListTable_Object = MibTable
dot1agXCfmMaMepListTable = _Dot1agXCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 11)
)
if mibBuilder.loadTexts:
    dot1agXCfmMaMepListTable.setStatus("current")
_Dot1agXCfmMaMepListEntry_Object = MibTableRow
dot1agXCfmMaMepListEntry = _Dot1agXCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 11, 1)
)
dot1agXCfmMaMepListEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"),
)
if mibBuilder.loadTexts:
    dot1agXCfmMaMepListEntry.setStatus("current")
_Dot1agXCfmMaMepListLocalMep_Type = Unsigned32
_Dot1agXCfmMaMepListLocalMep_Object = MibTableColumn
dot1agXCfmMaMepListLocalMep = _Dot1agXCfmMaMepListLocalMep_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 11, 1, 1),
    _Dot1agXCfmMaMepListLocalMep_Type()
)
dot1agXCfmMaMepListLocalMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMaMepListLocalMep.setStatus("current")
_Dot1agXCfmMaMepListDescr_Type = SnmpAdminString
_Dot1agXCfmMaMepListDescr_Object = MibTableColumn
dot1agXCfmMaMepListDescr = _Dot1agXCfmMaMepListDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 11, 1, 2),
    _Dot1agXCfmMaMepListDescr_Type()
)
dot1agXCfmMaMepListDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMaMepListDescr.setStatus("current")
_EthIfOamCfmMip_ObjectIdentity = ObjectIdentity
ethIfOamCfmMip = _EthIfOamCfmMip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12)
)
_EthIfOamCfmMipTable_Object = MibTable
ethIfOamCfmMipTable = _EthIfOamCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1)
)
if mibBuilder.loadTexts:
    ethIfOamCfmMipTable.setStatus("current")
_EthIfOamCfmMipEntry_Object = MibTableRow
ethIfOamCfmMipEntry = _EthIfOamCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1)
)
ethIfOamCfmMipEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "ethIfOamCfmMipMdIdx"),
    (0, "RAD-OamCfm-MIB", "ethIfOamCfmMipIdx"),
)
if mibBuilder.loadTexts:
    ethIfOamCfmMipEntry.setStatus("current")
_EthIfOamCfmMipMdIdx_Type = Unsigned32
_EthIfOamCfmMipMdIdx_Object = MibTableColumn
ethIfOamCfmMipMdIdx = _EthIfOamCfmMipMdIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 1),
    _EthIfOamCfmMipMdIdx_Type()
)
ethIfOamCfmMipMdIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfOamCfmMipMdIdx.setStatus("current")
_EthIfOamCfmMipIdx_Type = Unsigned32
_EthIfOamCfmMipIdx_Object = MibTableColumn
ethIfOamCfmMipIdx = _EthIfOamCfmMipIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 2),
    _EthIfOamCfmMipIdx_Type()
)
ethIfOamCfmMipIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfOamCfmMipIdx.setStatus("current")
_EthIfOamCfmMipRowStatus_Type = RowStatus
_EthIfOamCfmMipRowStatus_Object = MibTableColumn
ethIfOamCfmMipRowStatus = _EthIfOamCfmMipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 3),
    _EthIfOamCfmMipRowStatus_Type()
)
ethIfOamCfmMipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfOamCfmMipRowStatus.setStatus("current")
_EthIfOamCfmMipBoundedPortIfIndex_Type = InterfaceIndexOrZero
_EthIfOamCfmMipBoundedPortIfIndex_Object = MibTableColumn
ethIfOamCfmMipBoundedPortIfIndex = _EthIfOamCfmMipBoundedPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 4),
    _EthIfOamCfmMipBoundedPortIfIndex_Type()
)
ethIfOamCfmMipBoundedPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfOamCfmMipBoundedPortIfIndex.setStatus("current")


class _EthIfOamCfmMipFlowType_Type(Integer32):
    """Custom type ethIfOamCfmMipFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 1),
          ("biDirectional", 2))
    )


_EthIfOamCfmMipFlowType_Type.__name__ = "Integer32"
_EthIfOamCfmMipFlowType_Object = MibTableColumn
ethIfOamCfmMipFlowType = _EthIfOamCfmMipFlowType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 5),
    _EthIfOamCfmMipFlowType_Type()
)
ethIfOamCfmMipFlowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfOamCfmMipFlowType.setStatus("current")
_EthIfOamCfmMipFlowRxIndex_Type = Unsigned32
_EthIfOamCfmMipFlowRxIndex_Object = MibTableColumn
ethIfOamCfmMipFlowRxIndex = _EthIfOamCfmMipFlowRxIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 6),
    _EthIfOamCfmMipFlowRxIndex_Type()
)
ethIfOamCfmMipFlowRxIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfOamCfmMipFlowRxIndex.setStatus("current")
_EthIfOamCfmMipFlowTxIndex_Type = Unsigned32
_EthIfOamCfmMipFlowTxIndex_Object = MibTableColumn
ethIfOamCfmMipFlowTxIndex = _EthIfOamCfmMipFlowTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 1, 1, 7),
    _EthIfOamCfmMipFlowTxIndex_Type()
)
ethIfOamCfmMipFlowTxIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethIfOamCfmMipFlowTxIndex.setStatus("current")
_EthIfOamCfmMhfTable_Object = MibTable
ethIfOamCfmMhfTable = _EthIfOamCfmMhfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2)
)
if mibBuilder.loadTexts:
    ethIfOamCfmMhfTable.setStatus("current")
_EthIfOamCfmMhfEntry_Object = MibTableRow
ethIfOamCfmMhfEntry = _EthIfOamCfmMhfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1)
)
ethIfOamCfmMhfEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "ethIfOamCfmMhfMdIdx"),
    (0, "RAD-OamCfm-MIB", "ethIfOamCfmMhfMipIdx"),
    (0, "RAD-OamCfm-MIB", "ethIfOamCfmMhfIdx"),
)
if mibBuilder.loadTexts:
    ethIfOamCfmMhfEntry.setStatus("current")
_EthIfOamCfmMhfMdIdx_Type = Unsigned32
_EthIfOamCfmMhfMdIdx_Object = MibTableColumn
ethIfOamCfmMhfMdIdx = _EthIfOamCfmMhfMdIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 1),
    _EthIfOamCfmMhfMdIdx_Type()
)
ethIfOamCfmMhfMdIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfMdIdx.setStatus("current")
_EthIfOamCfmMhfMipIdx_Type = Unsigned32
_EthIfOamCfmMhfMipIdx_Object = MibTableColumn
ethIfOamCfmMhfMipIdx = _EthIfOamCfmMhfMipIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 2),
    _EthIfOamCfmMhfMipIdx_Type()
)
ethIfOamCfmMhfMipIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfMipIdx.setStatus("current")


class _EthIfOamCfmMhfIdx_Type(Unsigned32):
    """Custom type ethIfOamCfmMhfIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EthIfOamCfmMhfIdx_Type.__name__ = "Unsigned32"
_EthIfOamCfmMhfIdx_Object = MibTableColumn
ethIfOamCfmMhfIdx = _EthIfOamCfmMhfIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 3),
    _EthIfOamCfmMhfIdx_Type()
)
ethIfOamCfmMhfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfIdx.setStatus("current")
_EthIfOamCfmMhfActive_Type = TruthValue
_EthIfOamCfmMhfActive_Object = MibTableColumn
ethIfOamCfmMhfActive = _EthIfOamCfmMhfActive_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 4),
    _EthIfOamCfmMhfActive_Type()
)
ethIfOamCfmMhfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfActive.setStatus("current")
_EthIfOamCfmMhfOutputPortIfIndex_Type = InterfaceIndexOrZero
_EthIfOamCfmMhfOutputPortIfIndex_Object = MibTableColumn
ethIfOamCfmMhfOutputPortIfIndex = _EthIfOamCfmMhfOutputPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 5),
    _EthIfOamCfmMhfOutputPortIfIndex_Type()
)
ethIfOamCfmMhfOutputPortIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfOutputPortIfIndex.setStatus("current")
_EthIfOamCfmMhfPrimaryVid_Type = Unsigned32
_EthIfOamCfmMhfPrimaryVid_Object = MibTableColumn
ethIfOamCfmMhfPrimaryVid = _EthIfOamCfmMhfPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 6),
    _EthIfOamCfmMhfPrimaryVid_Type()
)
ethIfOamCfmMhfPrimaryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfPrimaryVid.setStatus("current")
_EthIfOamCfmMhfMappingProfile_Type = Unsigned32
_EthIfOamCfmMhfMappingProfile_Object = MibTableColumn
ethIfOamCfmMhfMappingProfile = _EthIfOamCfmMhfMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 7),
    _EthIfOamCfmMhfMappingProfile_Type()
)
ethIfOamCfmMhfMappingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfMappingProfile.setStatus("current")
_EthIfOamCfmMhfCosMapping_Type = Unsigned32
_EthIfOamCfmMhfCosMapping_Object = MibTableColumn
ethIfOamCfmMhfCosMapping = _EthIfOamCfmMhfCosMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 8),
    _EthIfOamCfmMhfCosMapping_Type()
)
ethIfOamCfmMhfCosMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfCosMapping.setStatus("current")
_EthIfOamCfmMhfCosMappingProfile_Type = Unsigned32
_EthIfOamCfmMhfCosMappingProfile_Object = MibTableColumn
ethIfOamCfmMhfCosMappingProfile = _EthIfOamCfmMhfCosMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 9),
    _EthIfOamCfmMhfCosMappingProfile_Type()
)
ethIfOamCfmMhfCosMappingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfCosMappingProfile.setStatus("current")
_EthIfOamCfmMhfQBlock_Type = ObjectIdentifier
_EthIfOamCfmMhfQBlock_Object = MibTableColumn
ethIfOamCfmMhfQBlock = _EthIfOamCfmMhfQBlock_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 10),
    _EthIfOamCfmMhfQBlock_Type()
)
ethIfOamCfmMhfQBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfQBlock.setStatus("current")
_EthIfOamCfmMhfFixedQueueMapping_Type = Unsigned32
_EthIfOamCfmMhfFixedQueueMapping_Object = MibTableColumn
ethIfOamCfmMhfFixedQueueMapping = _EthIfOamCfmMhfFixedQueueMapping_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 11),
    _EthIfOamCfmMhfFixedQueueMapping_Type()
)
ethIfOamCfmMhfFixedQueueMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfFixedQueueMapping.setStatus("current")
_EthIfOamCfmMhfQueueMappingProfile_Type = Unsigned32
_EthIfOamCfmMhfQueueMappingProfile_Object = MibTableColumn
ethIfOamCfmMhfQueueMappingProfile = _EthIfOamCfmMhfQueueMappingProfile_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 12, 2, 1, 12),
    _EthIfOamCfmMhfQueueMappingProfile_Type()
)
ethIfOamCfmMhfQueueMappingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfOamCfmMhfQueueMappingProfile.setStatus("current")
_EthOamMip_ObjectIdentity = ObjectIdentity
ethOamMip = _EthOamMip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13)
)
_EthOamMipTable_Object = MibTable
ethOamMipTable = _EthOamMipTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13, 1)
)
if mibBuilder.loadTexts:
    ethOamMipTable.setStatus("current")
_EthOamMipEntry_Object = MibTableRow
ethOamMipEntry = _EthOamMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13, 1, 1)
)
ethOamMipEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "ethOamMipIfIndex"),
    (0, "RAD-OamCfm-MIB", "ethOamMipVlanId"),
)
if mibBuilder.loadTexts:
    ethOamMipEntry.setStatus("current")
_EthOamMipIfIndex_Type = Unsigned32
_EthOamMipIfIndex_Object = MibTableColumn
ethOamMipIfIndex = _EthOamMipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13, 1, 1, 1),
    _EthOamMipIfIndex_Type()
)
ethOamMipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMipIfIndex.setStatus("current")
_EthOamMipVlanId_Type = Unsigned32
_EthOamMipVlanId_Object = MibTableColumn
ethOamMipVlanId = _EthOamMipVlanId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13, 1, 1, 2),
    _EthOamMipVlanId_Type()
)
ethOamMipVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMipVlanId.setStatus("current")
_EthOamMipMdLevel_Type = Unsigned32
_EthOamMipMdLevel_Object = MibTableColumn
ethOamMipMdLevel = _EthOamMipMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13, 1, 1, 3),
    _EthOamMipMdLevel_Type()
)
ethOamMipMdLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamMipMdLevel.setStatus("current")


class _AgnAutoMipAssign_Type(Integer32):
    """Custom type agnAutoMipAssign based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_AgnAutoMipAssign_Type.__name__ = "Integer32"
_AgnAutoMipAssign_Object = MibScalar
agnAutoMipAssign = _AgnAutoMipAssign_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 13, 2),
    _AgnAutoMipAssign_Type()
)
agnAutoMipAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agnAutoMipAssign.setStatus("current")
_EthIfOamCfmSumMipMep_ObjectIdentity = ObjectIdentity
ethIfOamCfmSumMipMep = _EthIfOamCfmSumMipMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 14)
)
if mibBuilder.loadTexts:
    ethIfOamCfmSumMipMep.setStatus("current")
_Dot1agXCfmMaNetTable_Object = MibTable
dot1agXCfmMaNetTable = _Dot1agXCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 15)
)
if mibBuilder.loadTexts:
    dot1agXCfmMaNetTable.setStatus("current")
_Dot1agXCfmMaNetEntry_Object = MibTableRow
dot1agXCfmMaNetEntry = _Dot1agXCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 15, 1)
)
dot1agXCfmMaNetEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
)
if mibBuilder.loadTexts:
    dot1agXCfmMaNetEntry.setStatus("current")
_Dot1agXCfmMaNetServiceIdName_Type = SnmpAdminString
_Dot1agXCfmMaNetServiceIdName_Object = MibTableColumn
dot1agXCfmMaNetServiceIdName = _Dot1agXCfmMaNetServiceIdName_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 15, 1, 1),
    _Dot1agXCfmMaNetServiceIdName_Type()
)
dot1agXCfmMaNetServiceIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1agXCfmMaNetServiceIdName.setStatus("current")


class _Dot1agXCfmMaNetIfStatusTlv_Type(Integer32):
    """Custom type dot1agXCfmMaNetIfStatusTlv based on Integer32"""
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


_Dot1agXCfmMaNetIfStatusTlv_Type.__name__ = "Integer32"
_Dot1agXCfmMaNetIfStatusTlv_Object = MibTableColumn
dot1agXCfmMaNetIfStatusTlv = _Dot1agXCfmMaNetIfStatusTlv_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 15, 1, 2),
    _Dot1agXCfmMaNetIfStatusTlv_Type()
)
dot1agXCfmMaNetIfStatusTlv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1agXCfmMaNetIfStatusTlv.setStatus("current")
_EthOamMepFlowsTable_Object = MibTable
ethOamMepFlowsTable = _EthOamMepFlowsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 16)
)
if mibBuilder.loadTexts:
    ethOamMepFlowsTable.setStatus("current")
_EthOamMepFlowsEntry_Object = MibTableRow
ethOamMepFlowsEntry = _EthOamMepFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 16, 1)
)
ethOamMepFlowsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAD-OamCfm-MIB", "ethOamMepFlowType"),
    (0, "RAD-OamCfm-MIB", "ethOamMepFlowIndex1"),
    (0, "RAD-OamCfm-MIB", "ethOamMepFlowIndex2"),
)
if mibBuilder.loadTexts:
    ethOamMepFlowsEntry.setStatus("current")


class _EthOamMepFlowType_Type(Integer32):
    """Custom type ethOamMepFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectionalRx", 1),
          ("uniDirectionalTx", 2),
          ("biDirectional", 3))
    )


_EthOamMepFlowType_Type.__name__ = "Integer32"
_EthOamMepFlowType_Object = MibTableColumn
ethOamMepFlowType = _EthOamMepFlowType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 16, 1, 1),
    _EthOamMepFlowType_Type()
)
ethOamMepFlowType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMepFlowType.setStatus("current")
_EthOamMepFlowIndex1_Type = Unsigned32
_EthOamMepFlowIndex1_Object = MibTableColumn
ethOamMepFlowIndex1 = _EthOamMepFlowIndex1_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 16, 1, 2),
    _EthOamMepFlowIndex1_Type()
)
ethOamMepFlowIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMepFlowIndex1.setStatus("current")
_EthOamMepFlowIndex2_Type = Unsigned32
_EthOamMepFlowIndex2_Object = MibTableColumn
ethOamMepFlowIndex2 = _EthOamMepFlowIndex2_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 16, 1, 3),
    _EthOamMepFlowIndex2_Type()
)
ethOamMepFlowIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMepFlowIndex2.setStatus("current")
_EthOamMepFlowsRowStatus_Type = RowStatus
_EthOamMepFlowsRowStatus_Object = MibTableColumn
ethOamMepFlowsRowStatus = _EthOamMepFlowsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 16, 1, 4),
    _EthOamMepFlowsRowStatus_Type()
)
ethOamMepFlowsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ethOamMepFlowsRowStatus.setStatus("current")
_EthOamConfigTable_Object = MibTable
ethOamConfigTable = _EthOamConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17)
)
if mibBuilder.loadTexts:
    ethOamConfigTable.setStatus("current")
_EthOamConfigEntry_Object = MibTableRow
ethOamConfigEntry = _EthOamConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1)
)
ethOamConfigEntry.setIndexNames(
    (0, "RAD-OamCfm-MIB", "ethOamConfigIdx"),
)
if mibBuilder.loadTexts:
    ethOamConfigEntry.setStatus("current")
_EthOamConfigIdx_Type = Unsigned32
_EthOamConfigIdx_Object = MibTableColumn
ethOamConfigIdx = _EthOamConfigIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 1),
    _EthOamConfigIdx_Type()
)
ethOamConfigIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamConfigIdx.setStatus("current")


class _EthOamConfigAlarmType_Type(Integer32):
    """Custom type ethOamConfigAlarmType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("legacy", 1),
          ("soam", 2))
    )


_EthOamConfigAlarmType_Type.__name__ = "Integer32"
_EthOamConfigAlarmType_Object = MibTableColumn
ethOamConfigAlarmType = _EthOamConfigAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 2),
    _EthOamConfigAlarmType_Type()
)
ethOamConfigAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamConfigAlarmType.setStatus("current")


class _EthOamConfigAvailabilityDeltaT_Type(Unsigned32):
    """Custom type ethOamConfigAvailabilityDeltaT based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(3, 3),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(5, 5),
        ValueRangeConstraint(6, 6),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(12, 12),
        ValueRangeConstraint(15, 15),
        ValueRangeConstraint(20, 20),
    )


_EthOamConfigAvailabilityDeltaT_Type.__name__ = "Unsigned32"
_EthOamConfigAvailabilityDeltaT_Object = MibTableColumn
ethOamConfigAvailabilityDeltaT = _EthOamConfigAvailabilityDeltaT_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 3),
    _EthOamConfigAvailabilityDeltaT_Type()
)
ethOamConfigAvailabilityDeltaT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityDeltaT.setStatus("current")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityDeltaT.setUnits("seconds")


class _EthOamConfigAvailabilityNumDeltaTs_Type(Unsigned32):
    """Custom type ethOamConfigAvailabilityNumDeltaTs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EthOamConfigAvailabilityNumDeltaTs_Type.__name__ = "Unsigned32"
_EthOamConfigAvailabilityNumDeltaTs_Object = MibTableColumn
ethOamConfigAvailabilityNumDeltaTs = _EthOamConfigAvailabilityNumDeltaTs_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 4),
    _EthOamConfigAvailabilityNumDeltaTs_Type()
)
ethOamConfigAvailabilityNumDeltaTs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityNumDeltaTs.setStatus("current")


class _EthOamConfigAvailabilityFwdFlrThreshold_Type(Unsigned32):
    """Custom type ethOamConfigAvailabilityFwdFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EthOamConfigAvailabilityFwdFlrThreshold_Type.__name__ = "Unsigned32"
_EthOamConfigAvailabilityFwdFlrThreshold_Object = MibTableColumn
ethOamConfigAvailabilityFwdFlrThreshold = _EthOamConfigAvailabilityFwdFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 5),
    _EthOamConfigAvailabilityFwdFlrThreshold_Type()
)
ethOamConfigAvailabilityFwdFlrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityFwdFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityFwdFlrThreshold.setUnits("percents")


class _EthOamConfigAvailabilityBckFlrThreshold_Type(Unsigned32):
    """Custom type ethOamConfigAvailabilityBckFlrThreshold based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_EthOamConfigAvailabilityBckFlrThreshold_Type.__name__ = "Unsigned32"
_EthOamConfigAvailabilityBckFlrThreshold_Object = MibTableColumn
ethOamConfigAvailabilityBckFlrThreshold = _EthOamConfigAvailabilityBckFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 6),
    _EthOamConfigAvailabilityBckFlrThreshold_Type()
)
ethOamConfigAvailabilityBckFlrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityBckFlrThreshold.setStatus("current")
if mibBuilder.loadTexts:
    ethOamConfigAvailabilityBckFlrThreshold.setUnits("percents")


class _EthOamConfigMdLevelMips_Type(Bits):
    """Custom type ethOamConfigMdLevelMips based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("mdlLevel0", 0),
          ("mdlLevel1", 1),
          ("mdlLevel2", 2),
          ("mdlLevel3", 3),
          ("mdlLevel4", 4),
          ("mdlLevel5", 5),
          ("mdlLevel6", 6),
          ("mdlLevel7", 7))
    )

_EthOamConfigMdLevelMips_Type.__name__ = "Bits"
_EthOamConfigMdLevelMips_Object = MibTableColumn
ethOamConfigMdLevelMips = _EthOamConfigMdLevelMips_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 17, 1, 7),
    _EthOamConfigMdLevelMips_Type()
)
ethOamConfigMdLevelMips.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamConfigMdLevelMips.setStatus("current")
_EthOamMepStats_ObjectIdentity = ObjectIdentity
ethOamMepStats = _EthOamMepStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18)
)
_EthOamMepCurrentTable_Object = MibTable
ethOamMepCurrentTable = _EthOamMepCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 1)
)
if mibBuilder.loadTexts:
    ethOamMepCurrentTable.setStatus("current")
_EthOamMepCurrentEntry_Object = MibTableRow
ethOamMepCurrentEntry = _EthOamMepCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 1, 1)
)
ethOamMepCurrentEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    ethOamMepCurrentEntry.setStatus("current")
_EthOamMepCurrentCcmTx_Type = Counter64
_EthOamMepCurrentCcmTx_Object = MibTableColumn
ethOamMepCurrentCcmTx = _EthOamMepCurrentCcmTx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 1, 1, 1),
    _EthOamMepCurrentCcmTx_Type()
)
ethOamMepCurrentCcmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamMepCurrentCcmTx.setStatus("current")
_EthOamMepIntervalTable_Object = MibTable
ethOamMepIntervalTable = _EthOamMepIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2)
)
if mibBuilder.loadTexts:
    ethOamMepIntervalTable.setStatus("current")
_EthOamMepIntervalEntry_Object = MibTableRow
ethOamMepIntervalEntry = _EthOamMepIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2, 1)
)
ethOamMepIntervalEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAD-OamCfm-MIB", "ethOamMepIntervalNumber"),
)
if mibBuilder.loadTexts:
    ethOamMepIntervalEntry.setStatus("current")


class _EthOamMepIntervalNumber_Type(Unsigned32):
    """Custom type ethOamMepIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EthOamMepIntervalNumber_Type.__name__ = "Unsigned32"
_EthOamMepIntervalNumber_Object = MibTableColumn
ethOamMepIntervalNumber = _EthOamMepIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2, 1, 1),
    _EthOamMepIntervalNumber_Type()
)
ethOamMepIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamMepIntervalNumber.setStatus("current")
_EthOamMepIntervalValidData_Type = TruthValue
_EthOamMepIntervalValidData_Object = MibTableColumn
ethOamMepIntervalValidData = _EthOamMepIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2, 1, 2),
    _EthOamMepIntervalValidData_Type()
)
ethOamMepIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamMepIntervalValidData.setStatus("current")


class _EthOamMepIntervalDuration_Type(Unsigned32):
    """Custom type ethOamMepIntervalDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EthOamMepIntervalDuration_Type.__name__ = "Unsigned32"
_EthOamMepIntervalDuration_Object = MibTableColumn
ethOamMepIntervalDuration = _EthOamMepIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2, 1, 3),
    _EthOamMepIntervalDuration_Type()
)
ethOamMepIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamMepIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    ethOamMepIntervalDuration.setUnits("seconds")
_EthOamMepIntervalTimeStamp_Type = DateAndTime
_EthOamMepIntervalTimeStamp_Object = MibTableColumn
ethOamMepIntervalTimeStamp = _EthOamMepIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2, 1, 4),
    _EthOamMepIntervalTimeStamp_Type()
)
ethOamMepIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamMepIntervalTimeStamp.setStatus("current")
_EthOamMepIntervalCcmTx_Type = Counter64
_EthOamMepIntervalCcmTx_Object = MibTableColumn
ethOamMepIntervalCcmTx = _EthOamMepIntervalCcmTx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 2, 1, 5),
    _EthOamMepIntervalCcmTx_Type()
)
ethOamMepIntervalCcmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamMepIntervalCcmTx.setStatus("current")
_EthOamRMepStatsTable_Object = MibTable
ethOamRMepStatsTable = _EthOamRMepStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 3)
)
if mibBuilder.loadTexts:
    ethOamRMepStatsTable.setStatus("current")
_EthOamRMepStatsEntry_Object = MibTableRow
ethOamRMepStatsEntry = _EthOamRMepStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 3, 1)
)
ethOamRMepStatsEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAD-OamCfm-MIB", "ethOamRMepStatsRMepId"),
)
if mibBuilder.loadTexts:
    ethOamRMepStatsEntry.setStatus("current")
_EthOamRMepStatsRMepId_Type = Dot1agCfmMepId
_EthOamRMepStatsRMepId_Object = MibTableColumn
ethOamRMepStatsRMepId = _EthOamRMepStatsRMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 3, 1, 1),
    _EthOamRMepStatsRMepId_Type()
)
ethOamRMepStatsRMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamRMepStatsRMepId.setStatus("current")
_EthOamRMepStatsCcmRx_Type = Counter64
_EthOamRMepStatsCcmRx_Object = MibTableColumn
ethOamRMepStatsCcmRx = _EthOamRMepStatsCcmRx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 3, 1, 2),
    _EthOamRMepStatsCcmRx_Type()
)
ethOamRMepStatsCcmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamRMepStatsCcmRx.setStatus("current")


class _EthOamRMepStatsClearCmd_Type(Integer32):
    """Custom type ethOamRMepStatsClearCmd based on Integer32"""
    defaultValue = 2

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


_EthOamRMepStatsClearCmd_Type.__name__ = "Integer32"
_EthOamRMepStatsClearCmd_Object = MibTableColumn
ethOamRMepStatsClearCmd = _EthOamRMepStatsClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 3, 1, 3),
    _EthOamRMepStatsClearCmd_Type()
)
ethOamRMepStatsClearCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethOamRMepStatsClearCmd.setStatus("current")
_EthOamRMepCurrentTable_Object = MibTable
ethOamRMepCurrentTable = _EthOamRMepCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 4)
)
if mibBuilder.loadTexts:
    ethOamRMepCurrentTable.setStatus("current")
_EthOamRMepCurrentEntry_Object = MibTableRow
ethOamRMepCurrentEntry = _EthOamRMepCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 4, 1)
)
ethOamRMepCurrentEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAD-OamCfm-MIB", "ethOamRMepStatsRMepId"),
)
if mibBuilder.loadTexts:
    ethOamRMepCurrentEntry.setStatus("current")
_EthOamRMepCurrentCcmRx_Type = Counter64
_EthOamRMepCurrentCcmRx_Object = MibTableColumn
ethOamRMepCurrentCcmRx = _EthOamRMepCurrentCcmRx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 4, 1, 1),
    _EthOamRMepCurrentCcmRx_Type()
)
ethOamRMepCurrentCcmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamRMepCurrentCcmRx.setStatus("current")
_EthOamRMepIntervalTable_Object = MibTable
ethOamRMepIntervalTable = _EthOamRMepIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5)
)
if mibBuilder.loadTexts:
    ethOamRMepIntervalTable.setStatus("current")
_EthOamRMepIntervalEntry_Object = MibTableRow
ethOamRMepIntervalEntry = _EthOamRMepIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5, 1)
)
ethOamRMepIntervalEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "RAD-OamCfm-MIB", "ethOamRMepStatsRMepId"),
    (0, "RAD-OamCfm-MIB", "ethOamRMepIntervalNumber"),
)
if mibBuilder.loadTexts:
    ethOamRMepIntervalEntry.setStatus("current")


class _EthOamRMepIntervalNumber_Type(Unsigned32):
    """Custom type ethOamRMepIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_EthOamRMepIntervalNumber_Type.__name__ = "Unsigned32"
_EthOamRMepIntervalNumber_Object = MibTableColumn
ethOamRMepIntervalNumber = _EthOamRMepIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5, 1, 1),
    _EthOamRMepIntervalNumber_Type()
)
ethOamRMepIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethOamRMepIntervalNumber.setStatus("current")
_EthOamRMepIntervalValidData_Type = TruthValue
_EthOamRMepIntervalValidData_Object = MibTableColumn
ethOamRMepIntervalValidData = _EthOamRMepIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5, 1, 2),
    _EthOamRMepIntervalValidData_Type()
)
ethOamRMepIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamRMepIntervalValidData.setStatus("current")


class _EthOamRMepIntervalDuration_Type(Unsigned32):
    """Custom type ethOamRMepIntervalDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_EthOamRMepIntervalDuration_Type.__name__ = "Unsigned32"
_EthOamRMepIntervalDuration_Object = MibTableColumn
ethOamRMepIntervalDuration = _EthOamRMepIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5, 1, 3),
    _EthOamRMepIntervalDuration_Type()
)
ethOamRMepIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamRMepIntervalDuration.setStatus("current")
if mibBuilder.loadTexts:
    ethOamRMepIntervalDuration.setUnits("seconds")
_EthOamRMepIntervalTimeStamp_Type = DateAndTime
_EthOamRMepIntervalTimeStamp_Object = MibTableColumn
ethOamRMepIntervalTimeStamp = _EthOamRMepIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5, 1, 4),
    _EthOamRMepIntervalTimeStamp_Type()
)
ethOamRMepIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamRMepIntervalTimeStamp.setStatus("current")
_EthOamRMepIntervalCcmRx_Type = Counter64
_EthOamRMepIntervalCcmRx_Object = MibTableColumn
ethOamRMepIntervalCcmRx = _EthOamRMepIntervalCcmRx_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 18, 5, 1, 5),
    _EthOamRMepIntervalCcmRx_Type()
)
ethOamRMepIntervalCcmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOamRMepIntervalCcmRx.setStatus("current")

# Managed Objects groups


# Notification objects

ethOamCfmDefectCondition = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    ethOamCfmDefectCondition.setStatus(
        "current"
    )

oamCfmMepAis = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 4)
)
oamCfmMepAis.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmMepAis.setStatus(
        "current"
    )

oamCfmMepLck = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 5)
)
oamCfmMepLck.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmMepLck.setStatus(
        "current"
    )

oamCfmMepMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 6)
)
oamCfmMepMismatch.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMepCcStatus"))
)
if mibBuilder.loadTexts:
    oamCfmMepMismatch.setStatus(
        "current"
    )

oamCfmRmepLoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 7)
)
oamCfmRmepLoc.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmRmepLoc.setStatus(
        "current"
    )

oamCfmRmepRdi = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 8)
)
oamCfmRmepRdi.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmRmepRdi.setStatus(
        "current"
    )

oamCfmDestNeDelayTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 9)
)
oamCfmDestNeDelayTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeDelayTca.setStatus(
        "current"
    )

oamCfmDestNeDelayTcaOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 10)
)
oamCfmDestNeDelayTcaOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeDelayTcaOff.setStatus(
        "current"
    )

oamCfmDestNeDelayVarTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 11)
)
oamCfmDestNeDelayVarTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeDelayVarTca.setStatus(
        "current"
    )

oamCfmDestNeDelayVarTcaOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 12)
)
oamCfmDestNeDelayVarTcaOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeDelayVarTcaOff.setStatus(
        "current"
    )

oamCfmDestNeLossRatioTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 13)
)
oamCfmDestNeLossRatioTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeLossRatioTca.setStatus(
        "current"
    )

oamCfmDestNeLossRatioTcaOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 14)
)
oamCfmDestNeLossRatioTcaOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeLossRatioTcaOff.setStatus(
        "current"
    )

oamCfmDestNeLossRatioTcaFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 15)
)
oamCfmDestNeLossRatioTcaFe.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeLossRatioTcaFe.setStatus(
        "current"
    )

oamCfmDestNeLossRatioTcaFeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 16)
)
oamCfmDestNeLossRatioTcaFeOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeLossRatioTcaFeOff.setStatus(
        "current"
    )

oamCfmDestNeUnavailRatioTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 17)
)
oamCfmDestNeUnavailRatioTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeUnavailRatioTca.setStatus(
        "current"
    )

oamCfmDestNeUnavailRatioTcaOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 18)
)
oamCfmDestNeUnavailRatioTcaOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeUnavailRatioTcaOff.setStatus(
        "current"
    )

oamCfmDestNeUnavailRatioTcaFe = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 19)
)
oamCfmDestNeUnavailRatioTcaFe.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeUnavailRatioTcaFe.setStatus(
        "current"
    )

oamCfmDestNeUnavailRatioTcaFeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 20)
)
oamCfmDestNeUnavailRatioTcaFeOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "ethOamDestNeDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmDestNeUnavailRatioTcaFeOff.setStatus(
        "current"
    )

oamCfmMepDefXconCCM = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 21)
)
oamCfmMepDefXconCCM.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmMepDefXconCCM.setStatus(
        "current"
    )

oamCfmMepDefErrorCCM = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 22)
)
oamCfmMepDefErrorCCM.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmMepDefErrorCCM.setStatus(
        "current"
    )

oamCfmRmepDefRemoteCCM = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 23)
)
oamCfmRmepDefRemoteCCM.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmRmepDefRemoteCCM.setStatus(
        "current"
    )

oamCfmRmepDefRDICCM = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 24)
)
oamCfmRmepDefRDICCM.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmRmepDefRDICCM.setStatus(
        "current"
    )

oamCfmRmepDefMACstatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 25)
)
oamCfmRmepDefMACstatus.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-OamCfm-MIB", "dot1agXCfmMaMepListDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"))
)
if mibBuilder.loadTexts:
    oamCfmRmepDefMACstatus.setStatus(
        "current"
    )

systemCfmSoamRxPacketDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 1, 3, 0, 26)
)
systemCfmSoamRxPacketDropped.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    systemCfmSoamRxPacketDropped.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-OamCfm-MIB",
    **{"EthOamBinCounterType": EthOamBinCounterType,
       "ethIfOamCfm": ethIfOamCfm,
       "ethIfOamCfmEvents": ethIfOamCfmEvents,
       "ethOamCfmDefectCondition": ethOamCfmDefectCondition,
       "oamCfmMepAis": oamCfmMepAis,
       "oamCfmMepLck": oamCfmMepLck,
       "oamCfmMepMismatch": oamCfmMepMismatch,
       "oamCfmRmepLoc": oamCfmRmepLoc,
       "oamCfmRmepRdi": oamCfmRmepRdi,
       "oamCfmDestNeDelayTca": oamCfmDestNeDelayTca,
       "oamCfmDestNeDelayTcaOff": oamCfmDestNeDelayTcaOff,
       "oamCfmDestNeDelayVarTca": oamCfmDestNeDelayVarTca,
       "oamCfmDestNeDelayVarTcaOff": oamCfmDestNeDelayVarTcaOff,
       "oamCfmDestNeLossRatioTca": oamCfmDestNeLossRatioTca,
       "oamCfmDestNeLossRatioTcaOff": oamCfmDestNeLossRatioTcaOff,
       "oamCfmDestNeLossRatioTcaFe": oamCfmDestNeLossRatioTcaFe,
       "oamCfmDestNeLossRatioTcaFeOff": oamCfmDestNeLossRatioTcaFeOff,
       "oamCfmDestNeUnavailRatioTca": oamCfmDestNeUnavailRatioTca,
       "oamCfmDestNeUnavailRatioTcaOff": oamCfmDestNeUnavailRatioTcaOff,
       "oamCfmDestNeUnavailRatioTcaFe": oamCfmDestNeUnavailRatioTcaFe,
       "oamCfmDestNeUnavailRatioTcaFeOff": oamCfmDestNeUnavailRatioTcaFeOff,
       "oamCfmMepDefXconCCM": oamCfmMepDefXconCCM,
       "oamCfmMepDefErrorCCM": oamCfmMepDefErrorCCM,
       "oamCfmRmepDefRemoteCCM": oamCfmRmepDefRemoteCCM,
       "oamCfmRmepDefRDICCM": oamCfmRmepDefRDICCM,
       "oamCfmRmepDefMACstatus": oamCfmRmepDefMACstatus,
       "systemCfmSoamRxPacketDropped": systemCfmSoamRxPacketDropped,
       "radMepTable": radMepTable,
       "radMepEntry": radMepEntry,
       "radOamIdx1": radOamIdx1,
       "radOamEvcIdx": radOamEvcIdx,
       "radMepIdx": radMepIdx,
       "radMepRowStatus": radMepRowStatus,
       "radMepLocalMepId": radMepLocalMepId,
       "radMepRemoteMepId": radMepRemoteMepId,
       "radMepOamMode": radMepOamMode,
       "radMepContinuityVerMode": radMepContinuityVerMode,
       "radMepMeLevel": radMepMeLevel,
       "radMepOamDestAddrType": radMepOamDestAddrType,
       "radMepOamDestMacAddr": radMepOamDestMacAddr,
       "radMepDefaultPriority": radMepDefaultPriority,
       "radMepCcStatus": radMepCcStatus,
       "radMepOamProtocol": radMepOamProtocol,
       "radMepMdId": radMepMdId,
       "radMepMaFormat": radMepMaFormat,
       "radMepMaName": radMepMaName,
       "radMepSpVlanId": radMepSpVlanId,
       "radMepCcInterval": radMepCcInterval,
       "radMepTransmitLbmDestMacAddress": radMepTransmitLbmDestMacAddress,
       "radMepTransmitLbmDestMepId": radMepTransmitLbmDestMepId,
       "radMepTransmitLbmDestIsMepId": radMepTransmitLbmDestIsMepId,
       "radMepTransmitLbmMassages": radMepTransmitLbmMassages,
       "radMepTransmitLbmVlanPriority": radMepTransmitLbmVlanPriority,
       "radMepTransmitLbmVlanDropEnable": radMepTransmitLbmVlanDropEnable,
       "radMepLbrIn": radMepLbrIn,
       "radMepLbrInOutOfOrder": radMepLbrInOutOfOrder,
       "radMepLbmOut": radMepLbmOut,
       "radMepTransmitLtmTargetMacAddress": radMepTransmitLtmTargetMacAddress,
       "radMepTransmitLtmTargetMepId": radMepTransmitLtmTargetMepId,
       "radMepTransmitLtmTargetIsMepId": radMepTransmitLtmTargetIsMepId,
       "radMepTransmitLtmTtl": radMepTransmitLtmTtl,
       "radMepTransmitLtmActivationCmd": radMepTransmitLtmActivationCmd,
       "ethOamService": ethOamService,
       "ethOamServiceTable": ethOamServiceTable,
       "ethOamServiceEntry": ethOamServiceEntry,
       "ethOamServiceIdx": ethOamServiceIdx,
       "ethOamServiceRowStatus": ethOamServiceRowStatus,
       "ethOamServicePriority": ethOamServicePriority,
       "ethOamServicePmEnable": ethOamServicePmEnable,
       "ethOamServiceFrameLossRatioThresh": ethOamServiceFrameLossRatioThresh,
       "ethOamServiceDelayThresh": ethOamServiceDelayThresh,
       "ethOamServiceDelayVarThresh": ethOamServiceDelayVarThresh,
       "ethOamServiceUnavailRatioThresh": ethOamServiceUnavailRatioThresh,
       "ethOamServiceTxFrames": ethOamServiceTxFrames,
       "ethOamServiceOverflowTxFrames": ethOamServiceOverflowTxFrames,
       "ethOamServiceFarEndFrameLoss": ethOamServiceFarEndFrameLoss,
       "ethOamServiceOverflowFarEndFrameLoss": ethOamServiceOverflowFarEndFrameLoss,
       "ethOamServiceFarEndFrameLossRatio": ethOamServiceFarEndFrameLossRatio,
       "ethOamServiceElapsedTime": ethOamServiceElapsedTime,
       "ethOamServiceUnavailSec": ethOamServiceUnavailSec,
       "ethOamServiceUnavailRatio": ethOamServiceUnavailRatio,
       "ethOamServiceFramesAboveDelay": ethOamServiceFramesAboveDelay,
       "ethOamServiceOverflowFramesAboveDelay": ethOamServiceOverflowFramesAboveDelay,
       "ethOamServiceFramesAboveDelayVar": ethOamServiceFramesAboveDelayVar,
       "ethOamServiceOverflowFramesAboveDelayVar": ethOamServiceOverflowFramesAboveDelayVar,
       "ethOamServiceCurrentDelay": ethOamServiceCurrentDelay,
       "ethOamServiceCurrentDelayVariation": ethOamServiceCurrentDelayVariation,
       "ethOamServiceResetCounters": ethOamServiceResetCounters,
       "ethOamServiceNearEndFrameLoss": ethOamServiceNearEndFrameLoss,
       "ethOamServiceOverflowNearEndFrameLoss": ethOamServiceOverflowNearEndFrameLoss,
       "ethOamServiceNearEndFrameLossRatio": ethOamServiceNearEndFrameLossRatio,
       "ethOamServiceDmmInterval": ethOamServiceDmmInterval,
       "ethOamServiceLmmInterval": ethOamServiceLmmInterval,
       "ethOamServiceTxLmm": ethOamServiceTxLmm,
       "ethOamServiceOverflowTxLmm": ethOamServiceOverflowTxLmm,
       "ethOamServiceTxDmm": ethOamServiceTxDmm,
       "ethOamServiceOverflowTxDmm": ethOamServiceOverflowTxDmm,
       "ethOamServiceRxLmr": ethOamServiceRxLmr,
       "ethOamServiceOverflowRxLmr": ethOamServiceOverflowRxLmr,
       "ethOamServiceRxDmr": ethOamServiceRxDmr,
       "ethOamServiceOverflowRxDmr": ethOamServiceOverflowRxDmr,
       "ethOamServiceTxForward": ethOamServiceTxForward,
       "ethOamServiceOverflowTxForward": ethOamServiceOverflowTxForward,
       "ethOamServiceRxForward": ethOamServiceRxForward,
       "ethOamServiceOverflowRxForward": ethOamServiceOverflowRxForward,
       "ethOamServiceTxBackward": ethOamServiceTxBackward,
       "ethOamServiceOverflowTxBackward": ethOamServiceOverflowTxBackward,
       "ethOamServiceRxBackward": ethOamServiceRxBackward,
       "ethOamServiceOverflowRxBackward": ethOamServiceOverflowRxBackward,
       "ethOamServiceConvertedIndex": ethOamServiceConvertedIndex,
       "ethOamSvcCurrentStatTable": ethOamSvcCurrentStatTable,
       "ethOamSvcCurrentStatEntry": ethOamSvcCurrentStatEntry,
       "ethOamSvcCurrFramesAboveDelayThresh": ethOamSvcCurrFramesAboveDelayThresh,
       "ethOamSvcCurrFramesBelowDelayThresh": ethOamSvcCurrFramesBelowDelayThresh,
       "ethOamSvcCurrFramesAboveDVarThresh": ethOamSvcCurrFramesAboveDVarThresh,
       "ethOamSvcCurrFramesBelowDVarThresh": ethOamSvcCurrFramesBelowDVarThresh,
       "ethOamSvcCurrFramesTxCounter": ethOamSvcCurrFramesTxCounter,
       "ethOamSvcCurrFarEndFramesLossCounter": ethOamSvcCurrFarEndFramesLossCounter,
       "ethOamSvcCurrMinRoundTripDelay": ethOamSvcCurrMinRoundTripDelay,
       "ethOamSvcCurrMaxRoundTripDelay": ethOamSvcCurrMaxRoundTripDelay,
       "ethOamSvcCurrAvgRoundTripDelay": ethOamSvcCurrAvgRoundTripDelay,
       "ethOamSvcCurrMaxRoundTripDVar": ethOamSvcCurrMaxRoundTripDVar,
       "ethOamSvcCurrAvgRoundTripDVar": ethOamSvcCurrAvgRoundTripDVar,
       "ethOamSvcCurrElapsedTime": ethOamSvcCurrElapsedTime,
       "ethOamSvcCurrUnavailSec": ethOamSvcCurrUnavailSec,
       "ethOamSvcCurrLmmTxFrames": ethOamSvcCurrLmmTxFrames,
       "ethOamSvcCurrDmmTxFrames": ethOamSvcCurrDmmTxFrames,
       "ethOamSvcCurrLmrRxFrames": ethOamSvcCurrLmrRxFrames,
       "ethOamSvcCurrDmrRxFrames": ethOamSvcCurrDmrRxFrames,
       "ethOamSvcCurrNearEndFramesLossCounter": ethOamSvcCurrNearEndFramesLossCounter,
       "ethOamSvcCurrTxFramesForward": ethOamSvcCurrTxFramesForward,
       "ethOamSvcCurrRxFramesForward": ethOamSvcCurrRxFramesForward,
       "ethOamSvcCurrTxFramesBackward": ethOamSvcCurrTxFramesBackward,
       "ethOamSvcCurrRxFramesBackward": ethOamSvcCurrRxFramesBackward,
       "ethOamSvcCurrUnavailableIndForward": ethOamSvcCurrUnavailableIndForward,
       "ethOamSvcCurrUnavailableIndBackward": ethOamSvcCurrUnavailableIndBackward,
       "ethOamSvcCurrNearEndFrameLossRatio": ethOamSvcCurrNearEndFrameLossRatio,
       "ethOamSvcCurrFarEndFrameLossRatio": ethOamSvcCurrFarEndFrameLossRatio,
       "ethOamSvcCurrMinRoundTripDVar": ethOamSvcCurrMinRoundTripDVar,
       "ethOamSvcCurrMinForwardDelay": ethOamSvcCurrMinForwardDelay,
       "ethOamSvcCurrMaxForwardDelay": ethOamSvcCurrMaxForwardDelay,
       "ethOamSvcCurrAvgForwardDelay": ethOamSvcCurrAvgForwardDelay,
       "ethOamSvcCurrMinForwardDVar": ethOamSvcCurrMinForwardDVar,
       "ethOamSvcCurrMaxForwardDVar": ethOamSvcCurrMaxForwardDVar,
       "ethOamSvcCurrAvgForwardDVar": ethOamSvcCurrAvgForwardDVar,
       "ethOamSvcCurrMinBackwardDVar": ethOamSvcCurrMinBackwardDVar,
       "ethOamSvcCurrMaxBackwardDVar": ethOamSvcCurrMaxBackwardDVar,
       "ethOamSvcCurrAvgBackwardDVar": ethOamSvcCurrAvgBackwardDVar,
       "ethOamSvcCurrAvailableIndForward": ethOamSvcCurrAvailableIndForward,
       "ethOamSvcCurrAvailableIndBackward": ethOamSvcCurrAvailableIndBackward,
       "ethOamSvcIntervalTable": ethOamSvcIntervalTable,
       "ethOamSvcIntervalEntry": ethOamSvcIntervalEntry,
       "ethOamSvcIntervalNum": ethOamSvcIntervalNum,
       "ethOamSvcIntervalFramesAboveDelayThresh": ethOamSvcIntervalFramesAboveDelayThresh,
       "ethOamSvcIntervalFramesBelowDelayThresh": ethOamSvcIntervalFramesBelowDelayThresh,
       "ethOamSvcIntervalFramesAboveDVarThresh": ethOamSvcIntervalFramesAboveDVarThresh,
       "ethOamSvcIntervalFramesBelowDVarThresh": ethOamSvcIntervalFramesBelowDVarThresh,
       "ethOamSvcIntervalFramesTxCounter": ethOamSvcIntervalFramesTxCounter,
       "ethOamSvcIntervalFarEndFramesLossCounter": ethOamSvcIntervalFarEndFramesLossCounter,
       "ethOamSvcIntervalMinRoundTripDelay": ethOamSvcIntervalMinRoundTripDelay,
       "ethOamSvcIntervalMaxRoundTripDelay": ethOamSvcIntervalMaxRoundTripDelay,
       "ethOamSvcIntervalAvgRoundTripDelay": ethOamSvcIntervalAvgRoundTripDelay,
       "ethOamSvcIntervalMaxRoundTripDVar": ethOamSvcIntervalMaxRoundTripDVar,
       "ethOamSvcIntervalAvgRoundTripDVar": ethOamSvcIntervalAvgRoundTripDVar,
       "ethOamSvcIntervalUnavailSec": ethOamSvcIntervalUnavailSec,
       "ethOamSvcIntervalLmmTxFrames": ethOamSvcIntervalLmmTxFrames,
       "ethOamSvcIntervalDmmTxFrames": ethOamSvcIntervalDmmTxFrames,
       "ethOamSvcIntervalLmrRxFrames": ethOamSvcIntervalLmrRxFrames,
       "ethOamSvcIntervalDmrRxFrames": ethOamSvcIntervalDmrRxFrames,
       "ethOamSvcIntervalNearEndFramesLossCounter": ethOamSvcIntervalNearEndFramesLossCounter,
       "ethOamSvcIntervalTxFramesForward": ethOamSvcIntervalTxFramesForward,
       "ethOamSvcIntervalRxFramesForward": ethOamSvcIntervalRxFramesForward,
       "ethOamSvcIntervalTxFramesBackward": ethOamSvcIntervalTxFramesBackward,
       "ethOamSvcIntervalRxFramesBackward": ethOamSvcIntervalRxFramesBackward,
       "ethOamSvcIntervalUnavailableIndForward": ethOamSvcIntervalUnavailableIndForward,
       "ethOamSvcIntervalUnavailableIndBackward": ethOamSvcIntervalUnavailableIndBackward,
       "ethOamSvcIntervalNearEndFrameLossRatio": ethOamSvcIntervalNearEndFrameLossRatio,
       "ethOamSvcIntervalFarEndFrameLossRatio": ethOamSvcIntervalFarEndFrameLossRatio,
       "ethOamSvcIntervalValidData": ethOamSvcIntervalValidData,
       "ethOamSvcIntervalDuration": ethOamSvcIntervalDuration,
       "ethOamSvcIntervalTimeStamp": ethOamSvcIntervalTimeStamp,
       "ethOamSvcIntervalMinRoundTripDVar": ethOamSvcIntervalMinRoundTripDVar,
       "ethOamSvcIntervalMinForwardDelay": ethOamSvcIntervalMinForwardDelay,
       "ethOamSvcIntervalMaxForwardDelay": ethOamSvcIntervalMaxForwardDelay,
       "ethOamSvcIntervalAvgForwardDelay": ethOamSvcIntervalAvgForwardDelay,
       "ethOamSvcIntervalMinForwardDVar": ethOamSvcIntervalMinForwardDVar,
       "ethOamSvcIntervalMaxForwardDVar": ethOamSvcIntervalMaxForwardDVar,
       "ethOamSvcIntervalAvgForwardDVar": ethOamSvcIntervalAvgForwardDVar,
       "ethOamSvcIntervalMinBackwardDVar": ethOamSvcIntervalMinBackwardDVar,
       "ethOamSvcIntervalMaxBackwardDVar": ethOamSvcIntervalMaxBackwardDVar,
       "ethOamSvcIntervalAvgBackwardDVar": ethOamSvcIntervalAvgBackwardDVar,
       "ethOamSvcIntervalAvailableIndForward": ethOamSvcIntervalAvailableIndForward,
       "ethOamSvcIntervalAvailableIndBackward": ethOamSvcIntervalAvailableIndBackward,
       "ethOamSvcTotalTable": ethOamSvcTotalTable,
       "ethOamSvcTotalEntry": ethOamSvcTotalEntry,
       "ethOamSvcTotalFramesAboveDelayThresh": ethOamSvcTotalFramesAboveDelayThresh,
       "ethOamSvcTotalFramesBelowDelayThresh": ethOamSvcTotalFramesBelowDelayThresh,
       "ethOamSvcTotalFramesAboveDVarThresh": ethOamSvcTotalFramesAboveDVarThresh,
       "ethOamSvcTotalFramesBelowDVarThresh": ethOamSvcTotalFramesBelowDVarThresh,
       "ethOamSvcTotalFramesTxCounter": ethOamSvcTotalFramesTxCounter,
       "ethOamSvcTotalFarEndFramesLossCounter": ethOamSvcTotalFarEndFramesLossCounter,
       "ethOamSvcTotalMinRoundTripDelay": ethOamSvcTotalMinRoundTripDelay,
       "ethOamSvcTotalMaxRoundTripDelay": ethOamSvcTotalMaxRoundTripDelay,
       "ethOamSvcTotalAvgRoundTripDelay": ethOamSvcTotalAvgRoundTripDelay,
       "ethOamSvcTotalMaxRoundTripDVar": ethOamSvcTotalMaxRoundTripDVar,
       "ethOamSvcTotalAvgRoundTripDVar": ethOamSvcTotalAvgRoundTripDVar,
       "ethOamSvcTotalUnavailSec": ethOamSvcTotalUnavailSec,
       "ethOamSvcTotalLmmTxFrames": ethOamSvcTotalLmmTxFrames,
       "ethOamSvcTotalDmmTxFrames": ethOamSvcTotalDmmTxFrames,
       "ethOamSvcTotalLmrRxFrames": ethOamSvcTotalLmrRxFrames,
       "ethOamSvcTotalDmrRxFrames": ethOamSvcTotalDmrRxFrames,
       "ethOamSvcTotalNearEndFramesLossCounter": ethOamSvcTotalNearEndFramesLossCounter,
       "ethOamSvcTotalTxFramesForward": ethOamSvcTotalTxFramesForward,
       "ethOamSvcTotalRxFramesForward": ethOamSvcTotalRxFramesForward,
       "ethOamSvcTotalTxFramesBackward": ethOamSvcTotalTxFramesBackward,
       "ethOamSvcTotalRxFramesBackward": ethOamSvcTotalRxFramesBackward,
       "ethOamSvcTotalUnavailableIndForward": ethOamSvcTotalUnavailableIndForward,
       "ethOamSvcTotalUnavailableIndBackward": ethOamSvcTotalUnavailableIndBackward,
       "ethOamSvcTotalMinRoundTripDVar": ethOamSvcTotalMinRoundTripDVar,
       "ethOamSvcTotalMinForwardDelay": ethOamSvcTotalMinForwardDelay,
       "ethOamSvcTotalMaxForwardDelay": ethOamSvcTotalMaxForwardDelay,
       "ethOamSvcTotalAvgForwardDelay": ethOamSvcTotalAvgForwardDelay,
       "ethOamSvcTotalMinForwardDVar": ethOamSvcTotalMinForwardDVar,
       "ethOamSvcTotalMaxForwardDVar": ethOamSvcTotalMaxForwardDVar,
       "ethOamSvcTotalAvgForwardDVar": ethOamSvcTotalAvgForwardDVar,
       "ethOamSvcTotalMinBackwardDVar": ethOamSvcTotalMinBackwardDVar,
       "ethOamSvcTotalMaxBackwardDVar": ethOamSvcTotalMaxBackwardDVar,
       "ethOamSvcTotalAvgBackwardDVar": ethOamSvcTotalAvgBackwardDVar,
       "ethOamSvcTotalForwardFrameLossRatio": ethOamSvcTotalForwardFrameLossRatio,
       "ethOamSvcTotalBackwardFrameLossRatio": ethOamSvcTotalBackwardFrameLossRatio,
       "ethOamSvcTotalAvailableIndForward": ethOamSvcTotalAvailableIndForward,
       "ethOamSvcTotalAvailableIndBackward": ethOamSvcTotalAvailableIndBackward,
       "ethOamDestNeTable": ethOamDestNeTable,
       "ethOamDestNeEntry": ethOamDestNeEntry,
       "ethOamDestNeIdx": ethOamDestNeIdx,
       "ethOamDestNeRowStatus": ethOamDestNeRowStatus,
       "ethOamDestNePmDestAddr": ethOamDestNePmDestAddr,
       "ethOamDestNePmRemoteMepId": ethOamDestNePmRemoteMepId,
       "ethOamDestNePmActivity": ethOamDestNePmActivity,
       "ethOamDestNeTxFrames": ethOamDestNeTxFrames,
       "ethOamDestNeOverflowTxFrames": ethOamDestNeOverflowTxFrames,
       "ethOamDestNeTxLmm": ethOamDestNeTxLmm,
       "ethOamDestNeOverflowTxLmm": ethOamDestNeOverflowTxLmm,
       "ethOamDestNeTxDmm": ethOamDestNeTxDmm,
       "ethOamDestNeOverflowTxDmm": ethOamDestNeOverflowTxDmm,
       "ethOamDestNeRxLmr": ethOamDestNeRxLmr,
       "ethOamDestNeOverflowRxLmr": ethOamDestNeOverflowRxLmr,
       "ethOamDestNeRxDmr": ethOamDestNeRxDmr,
       "ethOamDestNeOverflowRxDmr": ethOamDestNeOverflowRxDmr,
       "ethOamDestNeFarEndFrameLoss": ethOamDestNeFarEndFrameLoss,
       "ethOamDestNeOverflowFarEndFrameLoss": ethOamDestNeOverflowFarEndFrameLoss,
       "ethOamDestNeFarEndFrameLossRatio": ethOamDestNeFarEndFrameLossRatio,
       "ethOamDestNeTimeElapsed": ethOamDestNeTimeElapsed,
       "ethOamDestNeFramesAboveDelay": ethOamDestNeFramesAboveDelay,
       "ethOamDestNeOverflowFramesAboveDelay": ethOamDestNeOverflowFramesAboveDelay,
       "ethOamDestNeFramesAboveDelayVar": ethOamDestNeFramesAboveDelayVar,
       "ethOamDestNeOverflowFramesAboveDelayVar": ethOamDestNeOverflowFramesAboveDelayVar,
       "ethOamDestNeCurrentDelay": ethOamDestNeCurrentDelay,
       "ethOamDestNeCurrentDelayVariation": ethOamDestNeCurrentDelayVariation,
       "ethOamDestNeResetCounters": ethOamDestNeResetCounters,
       "ethOamDestNeNearEndFrameLoss": ethOamDestNeNearEndFrameLoss,
       "ethOamDestNeOverflowNearEndFrameLoss": ethOamDestNeOverflowNearEndFrameLoss,
       "ethOamDestNeNearEndFrameLossRatio": ethOamDestNeNearEndFrameLossRatio,
       "ethOamDestNeLmmTraffic": ethOamDestNeLmmTraffic,
       "ethOamDestNeFramesAboveDelayBinProfile": ethOamDestNeFramesAboveDelayBinProfile,
       "ethOamDestNeFramesAboveDelayVarBinProfile": ethOamDestNeFramesAboveDelayVarBinProfile,
       "ethOamDestNeDmmDataTlvLength": ethOamDestNeDmmDataTlvLength,
       "ethOamDestNeLossActivity": ethOamDestNeLossActivity,
       "ethOamDestNeDelayActivity": ethOamDestNeDelayActivity,
       "ethOamDestNeTxForward": ethOamDestNeTxForward,
       "ethOamDestNeOverflowTxForward": ethOamDestNeOverflowTxForward,
       "ethOamDestNeRxForward": ethOamDestNeRxForward,
       "ethOamDestNeOverflowRxForward": ethOamDestNeOverflowRxForward,
       "ethOamDestNeTxBackward": ethOamDestNeTxBackward,
       "ethOamDestNeOverflowTxBackward": ethOamDestNeOverflowTxBackward,
       "ethOamDestNeRxBackward": ethOamDestNeRxBackward,
       "ethOamDestNeOverflowRxBackward": ethOamDestNeOverflowRxBackward,
       "ethOamDestNeUnavailableIndForward": ethOamDestNeUnavailableIndForward,
       "ethOamDestNeOverflowUnavailableIndForward": ethOamDestNeOverflowUnavailableIndForward,
       "ethOamDestNeUnavailableIndBackward": ethOamDestNeUnavailableIndBackward,
       "ethOamDestNeOverflowUnavailableIndBackward": ethOamDestNeOverflowUnavailableIndBackward,
       "ethOamDestNeUnavailRatioForward": ethOamDestNeUnavailRatioForward,
       "ethOamDestNeUnavailRatioBackward": ethOamDestNeUnavailRatioBackward,
       "ethOamDestNeDescr": ethOamDestNeDescr,
       "ethOamDestNeConvertedIndex": ethOamDestNeConvertedIndex,
       "ethOamDestNeSlmDataTlvLength": ethOamDestNeSlmDataTlvLength,
       "ethOamDestNeLmMode": ethOamDestNeLmMode,
       "ethOamDestNeSlmTestId": ethOamDestNeSlmTestId,
       "ethOamDestNeForwardDelayVarBinProfile": ethOamDestNeForwardDelayVarBinProfile,
       "ethOamDestNeBackwardDelayVarBinProfile": ethOamDestNeBackwardDelayVarBinProfile,
       "ethOamDestNeAvailableIndForward": ethOamDestNeAvailableIndForward,
       "ethOamDestNeAvailableIndBackward": ethOamDestNeAvailableIndBackward,
       "ethOamDestNeDelayVariationForward": ethOamDestNeDelayVariationForward,
       "ethOamDestNeDelayVariationBackward": ethOamDestNeDelayVariationBackward,
       "ethOamSvcRmonConfigTable": ethOamSvcRmonConfigTable,
       "ethOamSvcRmonConfigEntry": ethOamSvcRmonConfigEntry,
       "ethOamSvcRmonConfigPerfAttrib": ethOamSvcRmonConfigPerfAttrib,
       "ethOamSvcRmonConfigRowStatus": ethOamSvcRmonConfigRowStatus,
       "ethOamSvcRmonConfigAlarmInterval": ethOamSvcRmonConfigAlarmInterval,
       "ethOamSvcRmonConfigAlarmRisingThresh": ethOamSvcRmonConfigAlarmRisingThresh,
       "ethOamSvcRmonConfigAlarmFallingThresh": ethOamSvcRmonConfigAlarmFallingThresh,
       "ethOamSvcRmonConfigEventType": ethOamSvcRmonConfigEventType,
       "ethOamMeasureBinProfileTable": ethOamMeasureBinProfileTable,
       "ethOamMeasureBinProfileEntry": ethOamMeasureBinProfileEntry,
       "ethOamMeasureBinProfileIndex": ethOamMeasureBinProfileIndex,
       "ethOamMeasureBinProfileRowStatus": ethOamMeasureBinProfileRowStatus,
       "ethOamMeasureBinProfileName": ethOamMeasureBinProfileName,
       "ethOamMeasureBinThresh": ethOamMeasureBinThresh,
       "ethOamDelayCurrentBinsTable": ethOamDelayCurrentBinsTable,
       "ethOamDelayCurrentBinsEntry": ethOamDelayCurrentBinsEntry,
       "ethOamDelayCurrentBinCounterType": ethOamDelayCurrentBinCounterType,
       "ethOamDelayCurrentBinNumber": ethOamDelayCurrentBinNumber,
       "ethOamDelayCurrentBinValue": ethOamDelayCurrentBinValue,
       "ethOamDelayIntervalBinsTable": ethOamDelayIntervalBinsTable,
       "ethOamDelayIntervalBinsEntry": ethOamDelayIntervalBinsEntry,
       "ethOamDelayIntervalBinCounterType": ethOamDelayIntervalBinCounterType,
       "ethOamDelayIntervalBinNumber": ethOamDelayIntervalBinNumber,
       "ethOamDelayIntervalBinValue": ethOamDelayIntervalBinValue,
       "radMdTable": radMdTable,
       "radMdEntry": radMdEntry,
       "radMdIndex": radMdIndex,
       "radMdFormat": radMdFormat,
       "radMdName": radMdName,
       "radMdRowStatus": radMdRowStatus,
       "radMepLtrTable": radMepLtrTable,
       "radMepLtrEntry": radMepLtrEntry,
       "radMepLtrReceiveOrder": radMepLtrReceiveOrder,
       "radMepLtrTtl": radMepLtrTtl,
       "radMepLtrMacAddr": radMepLtrMacAddr,
       "radMepLtrRelay": radMepLtrRelay,
       "radMepLtrIngress": radMepLtrIngress,
       "radMepLtrIngressPortIdSubtype": radMepLtrIngressPortIdSubtype,
       "radMepLtrIngressPortId": radMepLtrIngressPortId,
       "radMepLtrEgress": radMepLtrEgress,
       "radMepLtrEgressPortIdSubtype": radMepLtrEgressPortIdSubtype,
       "radMepLtrEgressPortId": radMepLtrEgressPortId,
       "radMepCcStatusTable": radMepCcStatusTable,
       "radMepCcStatusEntry": radMepCcStatusEntry,
       "radMepRemoteMepIdx": radMepRemoteMepIdx,
       "radMepCcStatusRemMepId": radMepCcStatusRemMepId,
       "radMepCcStat": radMepCcStat,
       "radMepCcStatusMacAddr": radMepCcStatusMacAddr,
       "ethOamStdEtherType": ethOamStdEtherType,
       "ethOamStdMacAddress": ethOamStdMacAddress,
       "dot1agXCfmMdTable": dot1agXCfmMdTable,
       "dot1agXCfmMdEntry": dot1agXCfmMdEntry,
       "dot1agXCfmMdProtocol": dot1agXCfmMdProtocol,
       "dot1agXCfmMepTable": dot1agXCfmMepTable,
       "dot1agXCfmMepEntry": dot1agXCfmMepEntry,
       "dot1agXCfmMepContinuityVerMode": dot1agXCfmMepContinuityVerMode,
       "dot1agXCfmMepDestAddrType": dot1agXCfmMepDestAddrType,
       "dot1agXCfmMepDestMacAddr": dot1agXCfmMepDestMacAddr,
       "dot1agXCfmMepMappingProfile": dot1agXCfmMepMappingProfile,
       "dot1agXCfmMepQBlock": dot1agXCfmMepQBlock,
       "dot1agXCfmMepFixedQueueMapping": dot1agXCfmMepFixedQueueMapping,
       "dot1agXCfmMepQueueMappingProfile": dot1agXCfmMepQueueMappingProfile,
       "dot1agXCfmMepConvertedIndex": dot1agXCfmMepConvertedIndex,
       "dot1agXCfmMepPmDestAddrType": dot1agXCfmMepPmDestAddrType,
       "dot1agXCfmMepForwardingMode": dot1agXCfmMepForwardingMode,
       "dot1agXCfmMepLbmDataTlvLength": dot1agXCfmMepLbmDataTlvLength,
       "dot1agXCfmMepClientMdLevel": dot1agXCfmMepClientMdLevel,
       "dot1agXCfmMepAisTransmit": dot1agXCfmMepAisTransmit,
       "dot1agXCfmMepAisInterval": dot1agXCfmMepAisInterval,
       "dot1agXCfmMepAisPriority": dot1agXCfmMepAisPriority,
       "dot1agXCfmMepDefects": dot1agXCfmMepDefects,
       "dot1agXCfmMepLastAlarmDefect": dot1agXCfmMepLastAlarmDefect,
       "dot1agXCfmMepCosMapping": dot1agXCfmMepCosMapping,
       "dot1agXCfmMepCosMappingProfile": dot1agXCfmMepCosMappingProfile,
       "dot1agXCfmMepCcStatus": dot1agXCfmMepCcStatus,
       "dot1agXCfmMepStatus": dot1agXCfmMepStatus,
       "dot1agXCfmMepExcludeCustomerTags": dot1agXCfmMepExcludeCustomerTags,
       "dot1agXCfmMepClearStatsCmd": dot1agXCfmMepClearStatsCmd,
       "dot1agXCfmMepTimeElapsed": dot1agXCfmMepTimeElapsed,
       "dot1agXCfmMepCcmTx": dot1agXCfmMepCcmTx,
       "dot1agXCfmMepDbTable": dot1agXCfmMepDbTable,
       "dot1agXCfmMepDbEntry": dot1agXCfmMepDbEntry,
       "dot1agXCfmMepCcStat": dot1agXCfmMepCcStat,
       "dot1agXCfmMepDbConvertedIndex": dot1agXCfmMepDbConvertedIndex,
       "dot1agXCfmMaMepListTable": dot1agXCfmMaMepListTable,
       "dot1agXCfmMaMepListEntry": dot1agXCfmMaMepListEntry,
       "dot1agXCfmMaMepListLocalMep": dot1agXCfmMaMepListLocalMep,
       "dot1agXCfmMaMepListDescr": dot1agXCfmMaMepListDescr,
       "ethIfOamCfmMip": ethIfOamCfmMip,
       "ethIfOamCfmMipTable": ethIfOamCfmMipTable,
       "ethIfOamCfmMipEntry": ethIfOamCfmMipEntry,
       "ethIfOamCfmMipMdIdx": ethIfOamCfmMipMdIdx,
       "ethIfOamCfmMipIdx": ethIfOamCfmMipIdx,
       "ethIfOamCfmMipRowStatus": ethIfOamCfmMipRowStatus,
       "ethIfOamCfmMipBoundedPortIfIndex": ethIfOamCfmMipBoundedPortIfIndex,
       "ethIfOamCfmMipFlowType": ethIfOamCfmMipFlowType,
       "ethIfOamCfmMipFlowRxIndex": ethIfOamCfmMipFlowRxIndex,
       "ethIfOamCfmMipFlowTxIndex": ethIfOamCfmMipFlowTxIndex,
       "ethIfOamCfmMhfTable": ethIfOamCfmMhfTable,
       "ethIfOamCfmMhfEntry": ethIfOamCfmMhfEntry,
       "ethIfOamCfmMhfMdIdx": ethIfOamCfmMhfMdIdx,
       "ethIfOamCfmMhfMipIdx": ethIfOamCfmMhfMipIdx,
       "ethIfOamCfmMhfIdx": ethIfOamCfmMhfIdx,
       "ethIfOamCfmMhfActive": ethIfOamCfmMhfActive,
       "ethIfOamCfmMhfOutputPortIfIndex": ethIfOamCfmMhfOutputPortIfIndex,
       "ethIfOamCfmMhfPrimaryVid": ethIfOamCfmMhfPrimaryVid,
       "ethIfOamCfmMhfMappingProfile": ethIfOamCfmMhfMappingProfile,
       "ethIfOamCfmMhfCosMapping": ethIfOamCfmMhfCosMapping,
       "ethIfOamCfmMhfCosMappingProfile": ethIfOamCfmMhfCosMappingProfile,
       "ethIfOamCfmMhfQBlock": ethIfOamCfmMhfQBlock,
       "ethIfOamCfmMhfFixedQueueMapping": ethIfOamCfmMhfFixedQueueMapping,
       "ethIfOamCfmMhfQueueMappingProfile": ethIfOamCfmMhfQueueMappingProfile,
       "ethOamMip": ethOamMip,
       "ethOamMipTable": ethOamMipTable,
       "ethOamMipEntry": ethOamMipEntry,
       "ethOamMipIfIndex": ethOamMipIfIndex,
       "ethOamMipVlanId": ethOamMipVlanId,
       "ethOamMipMdLevel": ethOamMipMdLevel,
       "agnAutoMipAssign": agnAutoMipAssign,
       "ethIfOamCfmSumMipMep": ethIfOamCfmSumMipMep,
       "dot1agXCfmMaNetTable": dot1agXCfmMaNetTable,
       "dot1agXCfmMaNetEntry": dot1agXCfmMaNetEntry,
       "dot1agXCfmMaNetServiceIdName": dot1agXCfmMaNetServiceIdName,
       "dot1agXCfmMaNetIfStatusTlv": dot1agXCfmMaNetIfStatusTlv,
       "ethOamMepFlowsTable": ethOamMepFlowsTable,
       "ethOamMepFlowsEntry": ethOamMepFlowsEntry,
       "ethOamMepFlowType": ethOamMepFlowType,
       "ethOamMepFlowIndex1": ethOamMepFlowIndex1,
       "ethOamMepFlowIndex2": ethOamMepFlowIndex2,
       "ethOamMepFlowsRowStatus": ethOamMepFlowsRowStatus,
       "ethOamConfigTable": ethOamConfigTable,
       "ethOamConfigEntry": ethOamConfigEntry,
       "ethOamConfigIdx": ethOamConfigIdx,
       "ethOamConfigAlarmType": ethOamConfigAlarmType,
       "ethOamConfigAvailabilityDeltaT": ethOamConfigAvailabilityDeltaT,
       "ethOamConfigAvailabilityNumDeltaTs": ethOamConfigAvailabilityNumDeltaTs,
       "ethOamConfigAvailabilityFwdFlrThreshold": ethOamConfigAvailabilityFwdFlrThreshold,
       "ethOamConfigAvailabilityBckFlrThreshold": ethOamConfigAvailabilityBckFlrThreshold,
       "ethOamConfigMdLevelMips": ethOamConfigMdLevelMips,
       "ethOamMepStats": ethOamMepStats,
       "ethOamMepCurrentTable": ethOamMepCurrentTable,
       "ethOamMepCurrentEntry": ethOamMepCurrentEntry,
       "ethOamMepCurrentCcmTx": ethOamMepCurrentCcmTx,
       "ethOamMepIntervalTable": ethOamMepIntervalTable,
       "ethOamMepIntervalEntry": ethOamMepIntervalEntry,
       "ethOamMepIntervalNumber": ethOamMepIntervalNumber,
       "ethOamMepIntervalValidData": ethOamMepIntervalValidData,
       "ethOamMepIntervalDuration": ethOamMepIntervalDuration,
       "ethOamMepIntervalTimeStamp": ethOamMepIntervalTimeStamp,
       "ethOamMepIntervalCcmTx": ethOamMepIntervalCcmTx,
       "ethOamRMepStatsTable": ethOamRMepStatsTable,
       "ethOamRMepStatsEntry": ethOamRMepStatsEntry,
       "ethOamRMepStatsRMepId": ethOamRMepStatsRMepId,
       "ethOamRMepStatsCcmRx": ethOamRMepStatsCcmRx,
       "ethOamRMepStatsClearCmd": ethOamRMepStatsClearCmd,
       "ethOamRMepCurrentTable": ethOamRMepCurrentTable,
       "ethOamRMepCurrentEntry": ethOamRMepCurrentEntry,
       "ethOamRMepCurrentCcmRx": ethOamRMepCurrentCcmRx,
       "ethOamRMepIntervalTable": ethOamRMepIntervalTable,
       "ethOamRMepIntervalEntry": ethOamRMepIntervalEntry,
       "ethOamRMepIntervalNumber": ethOamRMepIntervalNumber,
       "ethOamRMepIntervalValidData": ethOamRMepIntervalValidData,
       "ethOamRMepIntervalDuration": ethOamRMepIntervalDuration,
       "ethOamRMepIntervalTimeStamp": ethOamRMepIntervalTimeStamp,
       "ethOamRMepIntervalCcmRx": ethOamRMepIntervalCcmRx}
)
