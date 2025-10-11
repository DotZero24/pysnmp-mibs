# SNMP MIB module (ADTRAN-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-ERPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:15 2025
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

(adGenErps,
 adGenErpsID) = mibBuilder.importSymbols(
    "ADTRAN-ERPS-CONTAINER-MIB",
    "adGenErps",
    "adGenErpsID")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

(HCPerfCurrentCount,
 HCPerfIntervalCount,
 HCPerfTotalCount) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount",
    "HCPerfIntervalCount",
    "HCPerfTotalCount")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

adErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 79, 1, 1)
)
if mibBuilder.loadTexts:
    adErpsMIB.setRevisions(
        ("2017-01-23 00:00",
         "2014-12-16 00:00",
         "2014-07-01 00:00",
         "2013-05-16 00:00",
         "2012-06-17 00:00",
         "2011-12-01 00:00",
         "2011-07-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ErpsSpan(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 2))
    )



class ErpsProtectionStatus(TextualConvention, Integer32):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("noRequest", 0),
          ("waitToRestore", 1),
          ("remoteManualSwitch", 2),
          ("manualSwitch", 3),
          ("remoteSignalDegraded", 4),
          ("signalDegraded", 5),
          ("remoteSignalFailed", 6),
          ("signalFailed", 7),
          ("remoteForcedSwitch", 8),
          ("forcedSwitch", 9))
    )



class ErpsRingTopoProtectionStatus(TextualConvention, Integer32):
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
        *(("noRequest", 0),
          ("ringSpanBlocked", 1),
          ("manualSwitch", 2),
          ("signalFail", 3),
          ("forcedSwitch", 4))
    )



# MIB Managed Objects in the order of their OIDs

_ErpsGeneral_ObjectIdentity = ObjectIdentity
erpsGeneral = _ErpsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1)
)
_ErpsIfTable_Object = MibTable
erpsIfTable = _ErpsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1)
)
if mibBuilder.loadTexts:
    erpsIfTable.setStatus("current")
_ErpsIfEntry_Object = MibTableRow
erpsIfEntry = _ErpsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1)
)
erpsIfEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsIfIndex"),
)
if mibBuilder.loadTexts:
    erpsIfEntry.setStatus("current")
_ErpsIfIndex_Type = InterfaceIndex
_ErpsIfIndex_Object = MibTableColumn
erpsIfIndex = _ErpsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 1),
    _ErpsIfIndex_Type()
)
erpsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfIndex.setStatus("current")


class _ErpsIfStationId_Type(Unsigned32):
    """Custom type erpsIfStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErpsIfStationId_Type.__name__ = "Unsigned32"
_ErpsIfStationId_Object = MibTableColumn
erpsIfStationId = _ErpsIfStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 2),
    _ErpsIfStationId_Type()
)
erpsIfStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfStationId.setStatus("current")


class _ErpsIfStationName_Type(OctetString):
    """Custom type erpsIfStationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ErpsIfStationName_Type.__name__ = "OctetString"
_ErpsIfStationName_Object = MibTableColumn
erpsIfStationName = _ErpsIfStationName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 3),
    _ErpsIfStationName_Type()
)
erpsIfStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfStationName.setStatus("current")


class _ErpsIfProtectionWTR_Type(Unsigned32):
    """Custom type erpsIfProtectionWTR based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 720),
    )


_ErpsIfProtectionWTR_Type.__name__ = "Unsigned32"
_ErpsIfProtectionWTR_Object = MibTableColumn
erpsIfProtectionWTR = _ErpsIfProtectionWTR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 4),
    _ErpsIfProtectionWTR_Type()
)
erpsIfProtectionWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfProtectionWTR.setStatus("current")
if mibBuilder.loadTexts:
    erpsIfProtectionWTR.setUnits("Seconds")


class _ErpsIfGuardTimer_Type(Unsigned32):
    """Custom type erpsIfGuardTimer based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_ErpsIfGuardTimer_Type.__name__ = "Unsigned32"
_ErpsIfGuardTimer_Object = MibTableColumn
erpsIfGuardTimer = _ErpsIfGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 5),
    _ErpsIfGuardTimer_Type()
)
erpsIfGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfGuardTimer.setStatus("current")
if mibBuilder.loadTexts:
    erpsIfGuardTimer.setUnits("Milliseconds")


class _ErpsIfMessageTimer_Type(Unsigned32):
    """Custom type erpsIfMessageTimer based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_ErpsIfMessageTimer_Type.__name__ = "Unsigned32"
_ErpsIfMessageTimer_Object = MibTableColumn
erpsIfMessageTimer = _ErpsIfMessageTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 6),
    _ErpsIfMessageTimer_Type()
)
erpsIfMessageTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfMessageTimer.setStatus("current")
if mibBuilder.loadTexts:
    erpsIfMessageTimer.setUnits("Milliseconds")
_ErpsIfMessageTimerRunning_Type = TruthValue
_ErpsIfMessageTimerRunning_Object = MibTableColumn
erpsIfMessageTimerRunning = _ErpsIfMessageTimerRunning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 7),
    _ErpsIfMessageTimerRunning_Type()
)
erpsIfMessageTimerRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfMessageTimerRunning.setStatus("current")
_ErpsIfRplOwner_Type = TruthValue
_ErpsIfRplOwner_Object = MibTableColumn
erpsIfRplOwner = _ErpsIfRplOwner_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 8),
    _ErpsIfRplOwner_Type()
)
erpsIfRplOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfRplOwner.setStatus("current")


class _ErpsIfRplLink_Type(Integer32):
    """Custom type erpsIfRplLink based on Integer32"""
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
        *(("east", 1),
          ("west", 2),
          ("none", 3))
    )


_ErpsIfRplLink_Type.__name__ = "Integer32"
_ErpsIfRplLink_Object = MibTableColumn
erpsIfRplLink = _ErpsIfRplLink_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 9),
    _ErpsIfRplLink_Type()
)
erpsIfRplLink.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfRplLink.setStatus("current")
_ErpsIfEnabled_Type = TruthValue
_ErpsIfEnabled_Object = MibTableColumn
erpsIfEnabled = _ErpsIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 10),
    _ErpsIfEnabled_Type()
)
erpsIfEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfEnabled.setStatus("current")
_ErpsIfWtrRunning_Type = TruthValue
_ErpsIfWtrRunning_Object = MibTableColumn
erpsIfWtrRunning = _ErpsIfWtrRunning_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 11),
    _ErpsIfWtrRunning_Type()
)
erpsIfWtrRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfWtrRunning.setStatus("current")


class _ErpsIfWtrRemaining_Type(Unsigned32):
    """Custom type erpsIfWtrRemaining based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_ErpsIfWtrRemaining_Type.__name__ = "Unsigned32"
_ErpsIfWtrRemaining_Object = MibTableColumn
erpsIfWtrRemaining = _ErpsIfWtrRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 12),
    _ErpsIfWtrRemaining_Type()
)
erpsIfWtrRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfWtrRemaining.setStatus("current")
if mibBuilder.loadTexts:
    erpsIfWtrRemaining.setUnits("Seconds")
_ErpsIfWestIfIndex_Type = InterfaceIndex
_ErpsIfWestIfIndex_Object = MibTableColumn
erpsIfWestIfIndex = _ErpsIfWestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 13),
    _ErpsIfWestIfIndex_Type()
)
erpsIfWestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfWestIfIndex.setStatus("current")
_ErpsIfEastIfIndex_Type = InterfaceIndex
_ErpsIfEastIfIndex_Object = MibTableColumn
erpsIfEastIfIndex = _ErpsIfEastIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 14),
    _ErpsIfEastIfIndex_Type()
)
erpsIfEastIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfEastIfIndex.setStatus("current")
_ErpsIfProtectState_Type = ErpsProtectionStatus
_ErpsIfProtectState_Object = MibTableColumn
erpsIfProtectState = _ErpsIfProtectState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 15),
    _ErpsIfProtectState_Type()
)
erpsIfProtectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfProtectState.setStatus("current")
_ErpsIfLastChange_Type = TimeStamp
_ErpsIfLastChange_Object = MibTableColumn
erpsIfLastChange = _ErpsIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 16),
    _ErpsIfLastChange_Type()
)
erpsIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfLastChange.setStatus("current")
_ErpsIfChanges_Type = Counter32
_ErpsIfChanges_Object = MibTableColumn
erpsIfChanges = _ErpsIfChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 17),
    _ErpsIfChanges_Type()
)
erpsIfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfChanges.setStatus("current")


class _ErpsIfStationsOnRing_Type(Unsigned32):
    """Custom type erpsIfStationsOnRing based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ErpsIfStationsOnRing_Type.__name__ = "Unsigned32"
_ErpsIfStationsOnRing_Object = MibTableColumn
erpsIfStationsOnRing = _ErpsIfStationsOnRing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 18),
    _ErpsIfStationsOnRing_Type()
)
erpsIfStationsOnRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfStationsOnRing.setStatus("current")
_ErpsIfIsRingClosed_Type = TruthValue
_ErpsIfIsRingClosed_Object = MibTableColumn
erpsIfIsRingClosed = _ErpsIfIsRingClosed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 19),
    _ErpsIfIsRingClosed_Type()
)
erpsIfIsRingClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfIsRingClosed.setStatus("current")


class _ErpsTopoIfCurrentStatus_Type(Bits):
    """Custom type erpsTopoIfCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("duplicateRplOwner", 0),
          ("duplicateMac", 1),
          ("duplicateNode", 2),
          ("exceedMaxStations", 3),
          ("topologyInconsistent", 4))
    )

_ErpsTopoIfCurrentStatus_Type.__name__ = "Bits"
_ErpsTopoIfCurrentStatus_Object = MibTableColumn
erpsTopoIfCurrentStatus = _ErpsTopoIfCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 20),
    _ErpsTopoIfCurrentStatus_Type()
)
erpsTopoIfCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsTopoIfCurrentStatus.setStatus("current")
_ErpsTopoIfLastChange_Type = TimeStamp
_ErpsTopoIfLastChange_Object = MibTableColumn
erpsTopoIfLastChange = _ErpsTopoIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 21),
    _ErpsTopoIfLastChange_Type()
)
erpsTopoIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsTopoIfLastChange.setStatus("current")
_ErpsTopoIfChanges_Type = Counter32
_ErpsTopoIfChanges_Object = MibTableColumn
erpsTopoIfChanges = _ErpsTopoIfChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 22),
    _ErpsTopoIfChanges_Type()
)
erpsTopoIfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsTopoIfChanges.setStatus("current")


class _ErpsIfControlStag_Type(Integer32):
    """Custom type erpsIfControlStag based on Integer32"""
    defaultValue = 4096


_ErpsIfControlStag_Type.__name__ = "Integer32"
_ErpsIfControlStag_Object = MibTableColumn
erpsIfControlStag = _ErpsIfControlStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 23),
    _ErpsIfControlStag_Type()
)
erpsIfControlStag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfControlStag.setStatus("current")


class _ErpsIfTransportStag_Type(OctetString):
    """Custom type erpsIfTransportStag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_ErpsIfTransportStag_Type.__name__ = "OctetString"
_ErpsIfTransportStag_Object = MibTableColumn
erpsIfTransportStag = _ErpsIfTransportStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 24),
    _ErpsIfTransportStag_Type()
)
erpsIfTransportStag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfTransportStag.setStatus("current")
_ErpsIfVlanMisconfig_Type = DisplayString
_ErpsIfVlanMisconfig_Object = MibTableColumn
erpsIfVlanMisconfig = _ErpsIfVlanMisconfig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 25),
    _ErpsIfVlanMisconfig_Type()
)
erpsIfVlanMisconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfVlanMisconfig.setStatus("current")
_ErpsIfStationIp_Type = IpAddress
_ErpsIfStationIp_Object = MibTableColumn
erpsIfStationIp = _ErpsIfStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 26),
    _ErpsIfStationIp_Type()
)
erpsIfStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfStationIp.setStatus("current")


class _ErpsIfUuid_Type(OctetString):
    """Custom type erpsIfUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ErpsIfUuid_Type.__name__ = "OctetString"
_ErpsIfUuid_Object = MibTableColumn
erpsIfUuid = _ErpsIfUuid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 27),
    _ErpsIfUuid_Type()
)
erpsIfUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfUuid.setStatus("current")


class _ErpsIfConfigTrapEnable_Type(TruthValue):
    """Custom type erpsIfConfigTrapEnable based on TruthValue"""
    defaultValue = 2


_ErpsIfConfigTrapEnable_Type.__name__ = "TruthValue"
_ErpsIfConfigTrapEnable_Object = MibTableColumn
erpsIfConfigTrapEnable = _ErpsIfConfigTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 28),
    _ErpsIfConfigTrapEnable_Type()
)
erpsIfConfigTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfConfigTrapEnable.setStatus("current")


class _ErpsIfTopologyEnable_Type(TruthValue):
    """Custom type erpsIfTopologyEnable based on TruthValue"""
    defaultValue = 1


_ErpsIfTopologyEnable_Type.__name__ = "TruthValue"
_ErpsIfTopologyEnable_Object = MibTableColumn
erpsIfTopologyEnable = _ErpsIfTopologyEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 29),
    _ErpsIfTopologyEnable_Type()
)
erpsIfTopologyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfTopologyEnable.setStatus("current")


class _ErpsIfRapsVirtualChannel_Type(TruthValue):
    """Custom type erpsIfRapsVirtualChannel based on TruthValue"""
    defaultValue = 2


_ErpsIfRapsVirtualChannel_Type.__name__ = "TruthValue"
_ErpsIfRapsVirtualChannel_Object = MibTableColumn
erpsIfRapsVirtualChannel = _ErpsIfRapsVirtualChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 30),
    _ErpsIfRapsVirtualChannel_Type()
)
erpsIfRapsVirtualChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfRapsVirtualChannel.setStatus("current")
_ErpsIfLastError_Type = DisplayString
_ErpsIfLastError_Object = MibTableColumn
erpsIfLastError = _ErpsIfLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 31),
    _ErpsIfLastError_Type()
)
erpsIfLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfLastError.setStatus("current")
_ErpsIfRowStatus_Type = RowStatus
_ErpsIfRowStatus_Object = MibTableColumn
erpsIfRowStatus = _ErpsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 32),
    _ErpsIfRowStatus_Type()
)
erpsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfRowStatus.setStatus("current")


class _ErpsIfTopologyRate_Type(Integer32):
    """Custom type erpsIfTopologyRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slow", 1),
          ("fast", 2))
    )


_ErpsIfTopologyRate_Type.__name__ = "Integer32"
_ErpsIfTopologyRate_Object = MibTableColumn
erpsIfTopologyRate = _ErpsIfTopologyRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 33),
    _ErpsIfTopologyRate_Type()
)
erpsIfTopologyRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfTopologyRate.setStatus("current")


class _ErpsIfRateMiscnfEnable_Type(TruthValue):
    """Custom type erpsIfRateMiscnfEnable based on TruthValue"""
    defaultValue = 1


_ErpsIfRateMiscnfEnable_Type.__name__ = "TruthValue"
_ErpsIfRateMiscnfEnable_Object = MibTableColumn
erpsIfRateMiscnfEnable = _ErpsIfRateMiscnfEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 1, 1, 34),
    _ErpsIfRateMiscnfEnable_Type()
)
erpsIfRateMiscnfEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsIfRateMiscnfEnable.setStatus("current")
_ErpsIfStatsControlTable_Object = MibTable
erpsIfStatsControlTable = _ErpsIfStatsControlTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2)
)
if mibBuilder.loadTexts:
    erpsIfStatsControlTable.setStatus("current")
_ErpsIfStatsControlEntry_Object = MibTableRow
erpsIfStatsControlEntry = _ErpsIfStatsControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1)
)
erpsIfStatsControlEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsIfStatsControlIfIndex"),
)
if mibBuilder.loadTexts:
    erpsIfStatsControlEntry.setStatus("current")
_ErpsIfStatsControlIfIndex_Type = InterfaceIndex
_ErpsIfStatsControlIfIndex_Object = MibTableColumn
erpsIfStatsControlIfIndex = _ErpsIfStatsControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 1),
    _ErpsIfStatsControlIfIndex_Type()
)
erpsIfStatsControlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsIfStatsControlIfIndex.setStatus("current")


class _ErpsIfStatsControlPeriodClear_Type(Integer32):
    """Custom type erpsIfStatsControlPeriodClear based on Integer32"""
    defaultValue = 1

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
        *(("idle", 1),
          ("clearAllIntervals", 2),
          ("clearCurrent", 3),
          ("clearIntervals", 4),
          ("clearSpecificInterval", 5),
          ("clearCumulative", 6),
          ("clearAll", 7))
    )


_ErpsIfStatsControlPeriodClear_Type.__name__ = "Integer32"
_ErpsIfStatsControlPeriodClear_Object = MibTableColumn
erpsIfStatsControlPeriodClear = _ErpsIfStatsControlPeriodClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 2),
    _ErpsIfStatsControlPeriodClear_Type()
)
erpsIfStatsControlPeriodClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsIfStatsControlPeriodClear.setStatus("current")


class _ErpsIfStatsControlCountPointClear_Type(Integer32):
    """Custom type erpsIfStatsControlCountPointClear based on Integer32"""
    defaultValue = 1

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
        *(("clearAll", 1),
          ("clearWest", 2),
          ("clearEast", 3),
          ("clearRing", 4))
    )


_ErpsIfStatsControlCountPointClear_Type.__name__ = "Integer32"
_ErpsIfStatsControlCountPointClear_Object = MibTableColumn
erpsIfStatsControlCountPointClear = _ErpsIfStatsControlCountPointClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 3),
    _ErpsIfStatsControlCountPointClear_Type()
)
erpsIfStatsControlCountPointClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsIfStatsControlCountPointClear.setStatus("current")


class _ErpsIfStatsControlIntervalClear_Type(Unsigned32):
    """Custom type erpsIfStatsControlIntervalClear based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ErpsIfStatsControlIntervalClear_Type.__name__ = "Unsigned32"
_ErpsIfStatsControlIntervalClear_Object = MibTableColumn
erpsIfStatsControlIntervalClear = _ErpsIfStatsControlIntervalClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 4),
    _ErpsIfStatsControlIntervalClear_Type()
)
erpsIfStatsControlIntervalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsIfStatsControlIntervalClear.setStatus("current")


class _ErpsIfStatsControlCommitClear_Type(Integer32):
    """Custom type erpsIfStatsControlCommitClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commit", 1),
          ("commitDone", 2),
          ("commitFailed", 3))
    )


_ErpsIfStatsControlCommitClear_Type.__name__ = "Integer32"
_ErpsIfStatsControlCommitClear_Object = MibTableColumn
erpsIfStatsControlCommitClear = _ErpsIfStatsControlCommitClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 5),
    _ErpsIfStatsControlCommitClear_Type()
)
erpsIfStatsControlCommitClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsIfStatsControlCommitClear.setStatus("current")


class _ErpsIfStatsControlTimeElapsed_Type(Unsigned32):
    """Custom type erpsIfStatsControlTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 910),
    )


_ErpsIfStatsControlTimeElapsed_Type.__name__ = "Unsigned32"
_ErpsIfStatsControlTimeElapsed_Object = MibTableColumn
erpsIfStatsControlTimeElapsed = _ErpsIfStatsControlTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 6),
    _ErpsIfStatsControlTimeElapsed_Type()
)
erpsIfStatsControlTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfStatsControlTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    erpsIfStatsControlTimeElapsed.setUnits("Seconds")


class _ErpsIfStatsControlValidIntervals_Type(Unsigned32):
    """Custom type erpsIfStatsControlValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ErpsIfStatsControlValidIntervals_Type.__name__ = "Unsigned32"
_ErpsIfStatsControlValidIntervals_Object = MibTableColumn
erpsIfStatsControlValidIntervals = _ErpsIfStatsControlValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 2, 1, 7),
    _ErpsIfStatsControlValidIntervals_Type()
)
erpsIfStatsControlValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfStatsControlValidIntervals.setStatus("current")
_ErpsSpanTable_Object = MibTable
erpsSpanTable = _ErpsSpanTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3)
)
if mibBuilder.loadTexts:
    erpsSpanTable.setStatus("current")
_ErpsSpanEntry_Object = MibTableRow
erpsSpanEntry = _ErpsSpanEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1)
)
erpsSpanEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpanIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpanId"),
)
if mibBuilder.loadTexts:
    erpsSpanEntry.setStatus("current")
_ErpsSpanIfIndex_Type = InterfaceIndex
_ErpsSpanIfIndex_Object = MibTableColumn
erpsSpanIfIndex = _ErpsSpanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 1),
    _ErpsSpanIfIndex_Type()
)
erpsSpanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanIfIndex.setStatus("current")
_ErpsSpanId_Type = ErpsSpan
_ErpsSpanId_Object = MibTableColumn
erpsSpanId = _ErpsSpanId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 2),
    _ErpsSpanId_Type()
)
erpsSpanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanId.setStatus("current")


class _ErpsSpanProtectionCommand_Type(Integer32):
    """Custom type erpsSpanProtectionCommand based on Integer32"""
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
        *(("idle", 1),
          ("manualSwitch", 2),
          ("forcedSwitch", 3))
    )


_ErpsSpanProtectionCommand_Type.__name__ = "Integer32"
_ErpsSpanProtectionCommand_Object = MibTableColumn
erpsSpanProtectionCommand = _ErpsSpanProtectionCommand_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 3),
    _ErpsSpanProtectionCommand_Type()
)
erpsSpanProtectionCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsSpanProtectionCommand.setStatus("current")


class _ErpsSpanStatus_Type(Integer32):
    """Custom type erpsSpanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ErpsSpanStatus_Type.__name__ = "Integer32"
_ErpsSpanStatus_Object = MibTableColumn
erpsSpanStatus = _ErpsSpanStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 4),
    _ErpsSpanStatus_Type()
)
erpsSpanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatus.setStatus("current")


class _ErpsSpanForwardingStatus_Type(Integer32):
    """Custom type erpsSpanForwardingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("blocked", 2))
    )


_ErpsSpanForwardingStatus_Type.__name__ = "Integer32"
_ErpsSpanForwardingStatus_Object = MibTableColumn
erpsSpanForwardingStatus = _ErpsSpanForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 5),
    _ErpsSpanForwardingStatus_Type()
)
erpsSpanForwardingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanForwardingStatus.setStatus("current")


class _ErpsSpanCurrentStatus_Type(Bits):
    """Custom type erpsSpanCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("keepAliveTimeout", 0),
          ("miswired", 1),
          ("phyLinkDegrade", 2),
          ("phyLinkFail", 3),
          ("ccmLinkFail", 4))
    )

_ErpsSpanCurrentStatus_Type.__name__ = "Bits"
_ErpsSpanCurrentStatus_Object = MibTableColumn
erpsSpanCurrentStatus = _ErpsSpanCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 6),
    _ErpsSpanCurrentStatus_Type()
)
erpsSpanCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentStatus.setStatus("current")
_ErpsSpanLastChange_Type = TimeStamp
_ErpsSpanLastChange_Object = MibTableColumn
erpsSpanLastChange = _ErpsSpanLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 7),
    _ErpsSpanLastChange_Type()
)
erpsSpanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanLastChange.setStatus("current")
_ErpsSpanChanges_Type = Counter32
_ErpsSpanChanges_Object = MibTableColumn
erpsSpanChanges = _ErpsSpanChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 3, 1, 8),
    _ErpsSpanChanges_Type()
)
erpsSpanChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanChanges.setStatus("current")
_ErpsUuidMapTable_Object = MibTable
erpsUuidMapTable = _ErpsUuidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 4)
)
if mibBuilder.loadTexts:
    erpsUuidMapTable.setStatus("current")
_ErpsUuidMapEntry_Object = MibTableRow
erpsUuidMapEntry = _ErpsUuidMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 4, 1)
)
erpsUuidMapEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsUuidMapUuid"),
)
if mibBuilder.loadTexts:
    erpsUuidMapEntry.setStatus("current")


class _ErpsUuidMapUuid_Type(OctetString):
    """Custom type erpsUuidMapUuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ErpsUuidMapUuid_Type.__name__ = "OctetString"
_ErpsUuidMapUuid_Object = MibTableColumn
erpsUuidMapUuid = _ErpsUuidMapUuid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 4, 1, 1),
    _ErpsUuidMapUuid_Type()
)
erpsUuidMapUuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsUuidMapUuid.setStatus("current")
_ErpsUuidMapRingIfIndex_Type = InterfaceIndex
_ErpsUuidMapRingIfIndex_Object = MibTableColumn
erpsUuidMapRingIfIndex = _ErpsUuidMapRingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 4, 1, 2),
    _ErpsUuidMapRingIfIndex_Type()
)
erpsUuidMapRingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsUuidMapRingIfIndex.setStatus("current")
_ErpsIfChangeSummaryObject_ObjectIdentity = ObjectIdentity
erpsIfChangeSummaryObject = _ErpsIfChangeSummaryObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 5)
)
_ErpsIfChangeSummaryNumInterfaces_Type = Unsigned32
_ErpsIfChangeSummaryNumInterfaces_Object = MibScalar
erpsIfChangeSummaryNumInterfaces = _ErpsIfChangeSummaryNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 5, 1),
    _ErpsIfChangeSummaryNumInterfaces_Type()
)
erpsIfChangeSummaryNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfChangeSummaryNumInterfaces.setStatus("current")
_ErpsIfChangeSummaryIfLastChange_Type = TimeStamp
_ErpsIfChangeSummaryIfLastChange_Object = MibScalar
erpsIfChangeSummaryIfLastChange = _ErpsIfChangeSummaryIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 5, 2),
    _ErpsIfChangeSummaryIfLastChange_Type()
)
erpsIfChangeSummaryIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfChangeSummaryIfLastChange.setStatus("current")
_ErpsIfChangeSummaryIfChanges_Type = Counter32
_ErpsIfChangeSummaryIfChanges_Object = MibScalar
erpsIfChangeSummaryIfChanges = _ErpsIfChangeSummaryIfChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 5, 3),
    _ErpsIfChangeSummaryIfChanges_Type()
)
erpsIfChangeSummaryIfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfChangeSummaryIfChanges.setStatus("current")
_ErpsIfChangeSummarySpanLastChange_Type = TimeStamp
_ErpsIfChangeSummarySpanLastChange_Object = MibScalar
erpsIfChangeSummarySpanLastChange = _ErpsIfChangeSummarySpanLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 5, 4),
    _ErpsIfChangeSummarySpanLastChange_Type()
)
erpsIfChangeSummarySpanLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfChangeSummarySpanLastChange.setStatus("current")
_ErpsIfChangeSummarySpanChanges_Type = Counter32
_ErpsIfChangeSummarySpanChanges_Object = MibScalar
erpsIfChangeSummarySpanChanges = _ErpsIfChangeSummarySpanChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 5, 5),
    _ErpsIfChangeSummarySpanChanges_Type()
)
erpsIfChangeSummarySpanChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfChangeSummarySpanChanges.setStatus("current")
_ErpsIfLastCreateErrorTable_Object = MibTable
erpsIfLastCreateErrorTable = _ErpsIfLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 6)
)
if mibBuilder.loadTexts:
    erpsIfLastCreateErrorTable.setStatus("current")
_ErpsIfLastCreateErrorEntry_Object = MibTableRow
erpsIfLastCreateErrorEntry = _ErpsIfLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 6, 1)
)
erpsIfLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    erpsIfLastCreateErrorEntry.setStatus("current")
_ErpsIfLastCreateError_Type = DisplayString
_ErpsIfLastCreateError_Object = MibTableColumn
erpsIfLastCreateError = _ErpsIfLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 1, 6, 1, 1),
    _ErpsIfLastCreateError_Type()
)
erpsIfLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIfLastCreateError.setStatus("current")
_ErpsProtocol_ObjectIdentity = ObjectIdentity
erpsProtocol = _ErpsProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2)
)
_ErpsRingTopoTable_Object = MibTable
erpsRingTopoTable = _ErpsRingTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2)
)
if mibBuilder.loadTexts:
    erpsRingTopoTable.setStatus("current")
_ErpsRingTopoEntry_Object = MibTableRow
erpsRingTopoEntry = _ErpsRingTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1)
)
erpsRingTopoEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsRingTopoIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsRingTopoStationId"),
)
if mibBuilder.loadTexts:
    erpsRingTopoEntry.setStatus("current")
_ErpsRingTopoIndex_Type = InterfaceIndex
_ErpsRingTopoIndex_Object = MibTableColumn
erpsRingTopoIndex = _ErpsRingTopoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 1),
    _ErpsRingTopoIndex_Type()
)
erpsRingTopoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsRingTopoIndex.setStatus("current")


class _ErpsRingTopoStationId_Type(Unsigned32):
    """Custom type erpsRingTopoStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErpsRingTopoStationId_Type.__name__ = "Unsigned32"
_ErpsRingTopoStationId_Object = MibTableColumn
erpsRingTopoStationId = _ErpsRingTopoStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 2),
    _ErpsRingTopoStationId_Type()
)
erpsRingTopoStationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsRingTopoStationId.setStatus("current")


class _ErpsRingTopoStationName_Type(OctetString):
    """Custom type erpsRingTopoStationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ErpsRingTopoStationName_Type.__name__ = "OctetString"
_ErpsRingTopoStationName_Object = MibTableColumn
erpsRingTopoStationName = _ErpsRingTopoStationName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 3),
    _ErpsRingTopoStationName_Type()
)
erpsRingTopoStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoStationName.setStatus("current")


class _ErpsRingTopoStationFlags_Type(Bits):
    """Custom type erpsRingTopoStationFlags based on Bits"""
    namedValues = NamedValues(
        *(("isRplOwner", 0),
          ("isHub", 1),
          ("isTopoInconsistentWithNeighbor", 2))
    )

_ErpsRingTopoStationFlags_Type.__name__ = "Bits"
_ErpsRingTopoStationFlags_Object = MibTableColumn
erpsRingTopoStationFlags = _ErpsRingTopoStationFlags_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 4),
    _ErpsRingTopoStationFlags_Type()
)
erpsRingTopoStationFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoStationFlags.setStatus("current")
_ErpsRingTopoMacAddress_Type = MacAddress
_ErpsRingTopoMacAddress_Object = MibTableColumn
erpsRingTopoMacAddress = _ErpsRingTopoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 5),
    _ErpsRingTopoMacAddress_Type()
)
erpsRingTopoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacAddress.setStatus("current")


class _ErpsRingTopoWestStationId_Type(Unsigned32):
    """Custom type erpsRingTopoWestStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErpsRingTopoWestStationId_Type.__name__ = "Unsigned32"
_ErpsRingTopoWestStationId_Object = MibTableColumn
erpsRingTopoWestStationId = _ErpsRingTopoWestStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 6),
    _ErpsRingTopoWestStationId_Type()
)
erpsRingTopoWestStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoWestStationId.setStatus("current")


class _ErpsRingTopoEastStationId_Type(Unsigned32):
    """Custom type erpsRingTopoEastStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ErpsRingTopoEastStationId_Type.__name__ = "Unsigned32"
_ErpsRingTopoEastStationId_Object = MibTableColumn
erpsRingTopoEastStationId = _ErpsRingTopoEastStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 7),
    _ErpsRingTopoEastStationId_Type()
)
erpsRingTopoEastStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoEastStationId.setStatus("current")
_ErpsRingTopoWestNeighborMacAddress_Type = MacAddress
_ErpsRingTopoWestNeighborMacAddress_Object = MibTableColumn
erpsRingTopoWestNeighborMacAddress = _ErpsRingTopoWestNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 8),
    _ErpsRingTopoWestNeighborMacAddress_Type()
)
erpsRingTopoWestNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoWestNeighborMacAddress.setStatus("current")
_ErpsRingTopoEastNeighborMacAddress_Type = MacAddress
_ErpsRingTopoEastNeighborMacAddress_Object = MibTableColumn
erpsRingTopoEastNeighborMacAddress = _ErpsRingTopoEastNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 9),
    _ErpsRingTopoEastNeighborMacAddress_Type()
)
erpsRingTopoEastNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoEastNeighborMacAddress.setStatus("current")
_ErpsRingTopoWestProtectionStatus_Type = ErpsRingTopoProtectionStatus
_ErpsRingTopoWestProtectionStatus_Object = MibTableColumn
erpsRingTopoWestProtectionStatus = _ErpsRingTopoWestProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 10),
    _ErpsRingTopoWestProtectionStatus_Type()
)
erpsRingTopoWestProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoWestProtectionStatus.setStatus("current")
_ErpsRingTopoEastProtectionStatus_Type = ErpsRingTopoProtectionStatus
_ErpsRingTopoEastProtectionStatus_Object = MibTableColumn
erpsRingTopoEastProtectionStatus = _ErpsRingTopoEastProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 11),
    _ErpsRingTopoEastProtectionStatus_Type()
)
erpsRingTopoEastProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoEastProtectionStatus.setStatus("current")
_ErpsRingTopoLastChange_Type = TimeStamp
_ErpsRingTopoLastChange_Object = MibTableColumn
erpsRingTopoLastChange = _ErpsRingTopoLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 12),
    _ErpsRingTopoLastChange_Type()
)
erpsRingTopoLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoLastChange.setStatus("current")
_ErpsRingTopoChanges_Type = Counter32
_ErpsRingTopoChanges_Object = MibTableColumn
erpsRingTopoChanges = _ErpsRingTopoChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 13),
    _ErpsRingTopoChanges_Type()
)
erpsRingTopoChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoChanges.setStatus("current")
_ErpsRingTopoStationIp_Type = IpAddress
_ErpsRingTopoStationIp_Object = MibTableColumn
erpsRingTopoStationIp = _ErpsRingTopoStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 14),
    _ErpsRingTopoStationIp_Type()
)
erpsRingTopoStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoStationIp.setStatus("current")
_ErpsRingTopoWestStationIp_Type = IpAddress
_ErpsRingTopoWestStationIp_Object = MibTableColumn
erpsRingTopoWestStationIp = _ErpsRingTopoWestStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 15),
    _ErpsRingTopoWestStationIp_Type()
)
erpsRingTopoWestStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoWestStationIp.setStatus("current")
_ErpsRingTopoEastStationIp_Type = IpAddress
_ErpsRingTopoEastStationIp_Object = MibTableColumn
erpsRingTopoEastStationIp = _ErpsRingTopoEastStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 2, 1, 16),
    _ErpsRingTopoEastStationIp_Type()
)
erpsRingTopoEastStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoEastStationIp.setStatus("current")
_ErpsRingTopoMacTable_Object = MibTable
erpsRingTopoMacTable = _ErpsRingTopoMacTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3)
)
if mibBuilder.loadTexts:
    erpsRingTopoMacTable.setStatus("current")
_ErpsRingTopoMacEntry_Object = MibTableRow
erpsRingTopoMacEntry = _ErpsRingTopoMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1)
)
erpsRingTopoMacEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsRingTopoMacIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsRingTopoMacMacAddress"),
)
if mibBuilder.loadTexts:
    erpsRingTopoMacEntry.setStatus("current")
_ErpsRingTopoMacIndex_Type = InterfaceIndex
_ErpsRingTopoMacIndex_Object = MibTableColumn
erpsRingTopoMacIndex = _ErpsRingTopoMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 1),
    _ErpsRingTopoMacIndex_Type()
)
erpsRingTopoMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsRingTopoMacIndex.setStatus("current")
_ErpsRingTopoMacMacAddress_Type = MacAddress
_ErpsRingTopoMacMacAddress_Object = MibTableColumn
erpsRingTopoMacMacAddress = _ErpsRingTopoMacMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 2),
    _ErpsRingTopoMacMacAddress_Type()
)
erpsRingTopoMacMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsRingTopoMacMacAddress.setStatus("current")


class _ErpsRingTopoMacStationId_Type(Unsigned32):
    """Custom type erpsRingTopoMacStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ErpsRingTopoMacStationId_Type.__name__ = "Unsigned32"
_ErpsRingTopoMacStationId_Object = MibTableColumn
erpsRingTopoMacStationId = _ErpsRingTopoMacStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 3),
    _ErpsRingTopoMacStationId_Type()
)
erpsRingTopoMacStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacStationId.setStatus("current")


class _ErpsRingTopoMacStationName_Type(OctetString):
    """Custom type erpsRingTopoMacStationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ErpsRingTopoMacStationName_Type.__name__ = "OctetString"
_ErpsRingTopoMacStationName_Object = MibTableColumn
erpsRingTopoMacStationName = _ErpsRingTopoMacStationName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 4),
    _ErpsRingTopoMacStationName_Type()
)
erpsRingTopoMacStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacStationName.setStatus("current")


class _ErpsRingTopoMacStationFlags_Type(Bits):
    """Custom type erpsRingTopoMacStationFlags based on Bits"""
    namedValues = NamedValues(
        *(("isRplOwner", 0),
          ("isHub", 1),
          ("isTopoInconsistentWithNeighbor", 2))
    )

_ErpsRingTopoMacStationFlags_Type.__name__ = "Bits"
_ErpsRingTopoMacStationFlags_Object = MibTableColumn
erpsRingTopoMacStationFlags = _ErpsRingTopoMacStationFlags_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 5),
    _ErpsRingTopoMacStationFlags_Type()
)
erpsRingTopoMacStationFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacStationFlags.setStatus("current")


class _ErpsRingTopoMacWestStationId_Type(Unsigned32):
    """Custom type erpsRingTopoMacWestStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ErpsRingTopoMacWestStationId_Type.__name__ = "Unsigned32"
_ErpsRingTopoMacWestStationId_Object = MibTableColumn
erpsRingTopoMacWestStationId = _ErpsRingTopoMacWestStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 6),
    _ErpsRingTopoMacWestStationId_Type()
)
erpsRingTopoMacWestStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacWestStationId.setStatus("current")


class _ErpsRingTopoMacEastStationId_Type(Unsigned32):
    """Custom type erpsRingTopoMacEastStationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_ErpsRingTopoMacEastStationId_Type.__name__ = "Unsigned32"
_ErpsRingTopoMacEastStationId_Object = MibTableColumn
erpsRingTopoMacEastStationId = _ErpsRingTopoMacEastStationId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 7),
    _ErpsRingTopoMacEastStationId_Type()
)
erpsRingTopoMacEastStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacEastStationId.setStatus("current")
_ErpsRingTopoMacWestNeighborMacAddress_Type = MacAddress
_ErpsRingTopoMacWestNeighborMacAddress_Object = MibTableColumn
erpsRingTopoMacWestNeighborMacAddress = _ErpsRingTopoMacWestNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 8),
    _ErpsRingTopoMacWestNeighborMacAddress_Type()
)
erpsRingTopoMacWestNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacWestNeighborMacAddress.setStatus("current")
_ErpsRingTopoMacEastNeighborMacAddress_Type = MacAddress
_ErpsRingTopoMacEastNeighborMacAddress_Object = MibTableColumn
erpsRingTopoMacEastNeighborMacAddress = _ErpsRingTopoMacEastNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 9),
    _ErpsRingTopoMacEastNeighborMacAddress_Type()
)
erpsRingTopoMacEastNeighborMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacEastNeighborMacAddress.setStatus("current")
_ErpsRingTopoMacWestProtectionStatus_Type = ErpsRingTopoProtectionStatus
_ErpsRingTopoMacWestProtectionStatus_Object = MibTableColumn
erpsRingTopoMacWestProtectionStatus = _ErpsRingTopoMacWestProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 10),
    _ErpsRingTopoMacWestProtectionStatus_Type()
)
erpsRingTopoMacWestProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacWestProtectionStatus.setStatus("current")
_ErpsRingTopoMacEastProtectionStatus_Type = ErpsRingTopoProtectionStatus
_ErpsRingTopoMacEastProtectionStatus_Object = MibTableColumn
erpsRingTopoMacEastProtectionStatus = _ErpsRingTopoMacEastProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 11),
    _ErpsRingTopoMacEastProtectionStatus_Type()
)
erpsRingTopoMacEastProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacEastProtectionStatus.setStatus("current")
_ErpsRingTopoMacLastChange_Type = TimeStamp
_ErpsRingTopoMacLastChange_Object = MibTableColumn
erpsRingTopoMacLastChange = _ErpsRingTopoMacLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 12),
    _ErpsRingTopoMacLastChange_Type()
)
erpsRingTopoMacLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacLastChange.setStatus("current")
_ErpsRingTopoMacChanges_Type = Counter32
_ErpsRingTopoMacChanges_Object = MibTableColumn
erpsRingTopoMacChanges = _ErpsRingTopoMacChanges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 13),
    _ErpsRingTopoMacChanges_Type()
)
erpsRingTopoMacChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacChanges.setStatus("current")
_ErpsRingTopoMacStationIp_Type = IpAddress
_ErpsRingTopoMacStationIp_Object = MibTableColumn
erpsRingTopoMacStationIp = _ErpsRingTopoMacStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 14),
    _ErpsRingTopoMacStationIp_Type()
)
erpsRingTopoMacStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacStationIp.setStatus("current")
_ErpsRingTopoMacWestStationIp_Type = IpAddress
_ErpsRingTopoMacWestStationIp_Object = MibTableColumn
erpsRingTopoMacWestStationIp = _ErpsRingTopoMacWestStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 15),
    _ErpsRingTopoMacWestStationIp_Type()
)
erpsRingTopoMacWestStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacWestStationIp.setStatus("current")
_ErpsRingTopoMacEastStationIp_Type = IpAddress
_ErpsRingTopoMacEastStationIp_Object = MibTableColumn
erpsRingTopoMacEastStationIp = _ErpsRingTopoMacEastStationIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 2, 3, 1, 16),
    _ErpsRingTopoMacEastStationIp_Type()
)
erpsRingTopoMacEastStationIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsRingTopoMacEastStationIp.setStatus("current")
_ErpsCounters_ObjectIdentity = ObjectIdentity
erpsCounters = _ErpsCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3)
)
_ErpsCountersCurrentTable_Object = MibTable
erpsCountersCurrentTable = _ErpsCountersCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1)
)
if mibBuilder.loadTexts:
    erpsCountersCurrentTable.setStatus("current")
_ErpsCountersCurrentEntry_Object = MibTableRow
erpsCountersCurrentEntry = _ErpsCountersCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1)
)
erpsCountersCurrentEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    erpsCountersCurrentEntry.setStatus("current")
_ErpsCurrentIfIndex_Type = InterfaceIndex
_ErpsCurrentIfIndex_Object = MibTableColumn
erpsCurrentIfIndex = _ErpsCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 1),
    _ErpsCurrentIfIndex_Type()
)
erpsCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsCurrentIfIndex.setStatus("current")
_ErpsCurrentInRapsNrRb_Type = Counter32
_ErpsCurrentInRapsNrRb_Object = MibTableColumn
erpsCurrentInRapsNrRb = _ErpsCurrentInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 2),
    _ErpsCurrentInRapsNrRb_Type()
)
erpsCurrentInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsNrRb.setStatus("current")
_ErpsCurrentInRapsNrRbDnf_Type = Counter32
_ErpsCurrentInRapsNrRbDnf_Object = MibTableColumn
erpsCurrentInRapsNrRbDnf = _ErpsCurrentInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 3),
    _ErpsCurrentInRapsNrRbDnf_Type()
)
erpsCurrentInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsNrRbDnf.setStatus("current")
_ErpsCurrentInRapsNr_Type = Counter32
_ErpsCurrentInRapsNr_Object = MibTableColumn
erpsCurrentInRapsNr = _ErpsCurrentInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 4),
    _ErpsCurrentInRapsNr_Type()
)
erpsCurrentInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsNr.setStatus("current")
_ErpsCurrentInRapsFs_Type = Counter32
_ErpsCurrentInRapsFs_Object = MibTableColumn
erpsCurrentInRapsFs = _ErpsCurrentInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 5),
    _ErpsCurrentInRapsFs_Type()
)
erpsCurrentInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsFs.setStatus("current")
_ErpsCurrentInRapsSf_Type = Counter32
_ErpsCurrentInRapsSf_Object = MibTableColumn
erpsCurrentInRapsSf = _ErpsCurrentInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 6),
    _ErpsCurrentInRapsSf_Type()
)
erpsCurrentInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsSf.setStatus("current")
_ErpsCurrentInRapsMs_Type = Counter32
_ErpsCurrentInRapsMs_Object = MibTableColumn
erpsCurrentInRapsMs = _ErpsCurrentInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 7),
    _ErpsCurrentInRapsMs_Type()
)
erpsCurrentInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsMs.setStatus("current")
_ErpsCurrentInRapsIgnored_Type = Counter32
_ErpsCurrentInRapsIgnored_Object = MibTableColumn
erpsCurrentInRapsIgnored = _ErpsCurrentInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 8),
    _ErpsCurrentInRapsIgnored_Type()
)
erpsCurrentInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsIgnored.setStatus("current")
_ErpsCurrentInRapsTotal_Type = Counter32
_ErpsCurrentInRapsTotal_Object = MibTableColumn
erpsCurrentInRapsTotal = _ErpsCurrentInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 9),
    _ErpsCurrentInRapsTotal_Type()
)
erpsCurrentInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentInRapsTotal.setStatus("current")
_ErpsCurrentOutRapsNrRb_Type = Counter32
_ErpsCurrentOutRapsNrRb_Object = MibTableColumn
erpsCurrentOutRapsNrRb = _ErpsCurrentOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 10),
    _ErpsCurrentOutRapsNrRb_Type()
)
erpsCurrentOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsNrRb.setStatus("current")
_ErpsCurrentOutRapsNrRbDnf_Type = Counter32
_ErpsCurrentOutRapsNrRbDnf_Object = MibTableColumn
erpsCurrentOutRapsNrRbDnf = _ErpsCurrentOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 11),
    _ErpsCurrentOutRapsNrRbDnf_Type()
)
erpsCurrentOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsNrRbDnf.setStatus("current")
_ErpsCurrentOutRapsNr_Type = Counter32
_ErpsCurrentOutRapsNr_Object = MibTableColumn
erpsCurrentOutRapsNr = _ErpsCurrentOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 12),
    _ErpsCurrentOutRapsNr_Type()
)
erpsCurrentOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsNr.setStatus("current")
_ErpsCurrentOutRapsFs_Type = Counter32
_ErpsCurrentOutRapsFs_Object = MibTableColumn
erpsCurrentOutRapsFs = _ErpsCurrentOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 13),
    _ErpsCurrentOutRapsFs_Type()
)
erpsCurrentOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsFs.setStatus("current")
_ErpsCurrentOutRapsSf_Type = Counter32
_ErpsCurrentOutRapsSf_Object = MibTableColumn
erpsCurrentOutRapsSf = _ErpsCurrentOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 14),
    _ErpsCurrentOutRapsSf_Type()
)
erpsCurrentOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsSf.setStatus("current")
_ErpsCurrentOutRapsMs_Type = Counter32
_ErpsCurrentOutRapsMs_Object = MibTableColumn
erpsCurrentOutRapsMs = _ErpsCurrentOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 15),
    _ErpsCurrentOutRapsMs_Type()
)
erpsCurrentOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsMs.setStatus("current")
_ErpsCurrentOutRapsTotal_Type = Counter32
_ErpsCurrentOutRapsTotal_Object = MibTableColumn
erpsCurrentOutRapsTotal = _ErpsCurrentOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 16),
    _ErpsCurrentOutRapsTotal_Type()
)
erpsCurrentOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentOutRapsTotal.setStatus("current")
_ErpsCurrentProtectionSwitches_Type = Counter32
_ErpsCurrentProtectionSwitches_Object = MibTableColumn
erpsCurrentProtectionSwitches = _ErpsCurrentProtectionSwitches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 1, 1, 17),
    _ErpsCurrentProtectionSwitches_Type()
)
erpsCurrentProtectionSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsCurrentProtectionSwitches.setStatus("current")
_ErpsCountersIntervalTable_Object = MibTable
erpsCountersIntervalTable = _ErpsCountersIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2)
)
if mibBuilder.loadTexts:
    erpsCountersIntervalTable.setStatus("current")
_ErpsCountersIntervalEntry_Object = MibTableRow
erpsCountersIntervalEntry = _ErpsCountersIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1)
)
erpsCountersIntervalEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsIntervalIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsIntervalNumber"),
)
if mibBuilder.loadTexts:
    erpsCountersIntervalEntry.setStatus("current")
_ErpsIntervalIfIndex_Type = InterfaceIndex
_ErpsIntervalIfIndex_Object = MibTableColumn
erpsIntervalIfIndex = _ErpsIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 1),
    _ErpsIntervalIfIndex_Type()
)
erpsIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsIntervalIfIndex.setStatus("current")


class _ErpsIntervalNumber_Type(Unsigned32):
    """Custom type erpsIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ErpsIntervalNumber_Type.__name__ = "Unsigned32"
_ErpsIntervalNumber_Object = MibTableColumn
erpsIntervalNumber = _ErpsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 2),
    _ErpsIntervalNumber_Type()
)
erpsIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsIntervalNumber.setStatus("current")
_ErpsIntervalValidData_Type = TruthValue
_ErpsIntervalValidData_Object = MibTableColumn
erpsIntervalValidData = _ErpsIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 3),
    _ErpsIntervalValidData_Type()
)
erpsIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalValidData.setStatus("current")


class _ErpsIntervalTimeElapsed_Type(Unsigned32):
    """Custom type erpsIntervalTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 910),
    )


_ErpsIntervalTimeElapsed_Type.__name__ = "Unsigned32"
_ErpsIntervalTimeElapsed_Object = MibTableColumn
erpsIntervalTimeElapsed = _ErpsIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 4),
    _ErpsIntervalTimeElapsed_Type()
)
erpsIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    erpsIntervalTimeElapsed.setUnits("Seconds")
_ErpsIntervalStartTime_Type = DateAndTime
_ErpsIntervalStartTime_Object = MibTableColumn
erpsIntervalStartTime = _ErpsIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 5),
    _ErpsIntervalStartTime_Type()
)
erpsIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalStartTime.setStatus("current")
_ErpsIntervalInRapsNrRb_Type = Counter32
_ErpsIntervalInRapsNrRb_Object = MibTableColumn
erpsIntervalInRapsNrRb = _ErpsIntervalInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 6),
    _ErpsIntervalInRapsNrRb_Type()
)
erpsIntervalInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsNrRb.setStatus("current")
_ErpsIntervalInRapsNrRbDnf_Type = Counter32
_ErpsIntervalInRapsNrRbDnf_Object = MibTableColumn
erpsIntervalInRapsNrRbDnf = _ErpsIntervalInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 7),
    _ErpsIntervalInRapsNrRbDnf_Type()
)
erpsIntervalInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsNrRbDnf.setStatus("current")
_ErpsIntervalInRapsNr_Type = Counter32
_ErpsIntervalInRapsNr_Object = MibTableColumn
erpsIntervalInRapsNr = _ErpsIntervalInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 8),
    _ErpsIntervalInRapsNr_Type()
)
erpsIntervalInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsNr.setStatus("current")
_ErpsIntervalInRapsFs_Type = Counter32
_ErpsIntervalInRapsFs_Object = MibTableColumn
erpsIntervalInRapsFs = _ErpsIntervalInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 9),
    _ErpsIntervalInRapsFs_Type()
)
erpsIntervalInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsFs.setStatus("current")
_ErpsIntervalInRapsSf_Type = Counter32
_ErpsIntervalInRapsSf_Object = MibTableColumn
erpsIntervalInRapsSf = _ErpsIntervalInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 10),
    _ErpsIntervalInRapsSf_Type()
)
erpsIntervalInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsSf.setStatus("current")
_ErpsIntervalInRapsMs_Type = Counter32
_ErpsIntervalInRapsMs_Object = MibTableColumn
erpsIntervalInRapsMs = _ErpsIntervalInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 11),
    _ErpsIntervalInRapsMs_Type()
)
erpsIntervalInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsMs.setStatus("current")
_ErpsIntervalInRapsIgnored_Type = Counter32
_ErpsIntervalInRapsIgnored_Object = MibTableColumn
erpsIntervalInRapsIgnored = _ErpsIntervalInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 12),
    _ErpsIntervalInRapsIgnored_Type()
)
erpsIntervalInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsIgnored.setStatus("current")
_ErpsIntervalInRapsTotal_Type = Counter32
_ErpsIntervalInRapsTotal_Object = MibTableColumn
erpsIntervalInRapsTotal = _ErpsIntervalInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 13),
    _ErpsIntervalInRapsTotal_Type()
)
erpsIntervalInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalInRapsTotal.setStatus("current")
_ErpsIntervalOutRapsNrRb_Type = Counter32
_ErpsIntervalOutRapsNrRb_Object = MibTableColumn
erpsIntervalOutRapsNrRb = _ErpsIntervalOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 14),
    _ErpsIntervalOutRapsNrRb_Type()
)
erpsIntervalOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsNrRb.setStatus("current")
_ErpsIntervalOutRapsNrRbDnf_Type = Counter32
_ErpsIntervalOutRapsNrRbDnf_Object = MibTableColumn
erpsIntervalOutRapsNrRbDnf = _ErpsIntervalOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 15),
    _ErpsIntervalOutRapsNrRbDnf_Type()
)
erpsIntervalOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsNrRbDnf.setStatus("current")
_ErpsIntervalOutRapsNr_Type = Counter32
_ErpsIntervalOutRapsNr_Object = MibTableColumn
erpsIntervalOutRapsNr = _ErpsIntervalOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 16),
    _ErpsIntervalOutRapsNr_Type()
)
erpsIntervalOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsNr.setStatus("current")
_ErpsIntervalOutRapsFs_Type = Counter32
_ErpsIntervalOutRapsFs_Object = MibTableColumn
erpsIntervalOutRapsFs = _ErpsIntervalOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 17),
    _ErpsIntervalOutRapsFs_Type()
)
erpsIntervalOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsFs.setStatus("current")
_ErpsIntervalOutRapsSf_Type = Counter32
_ErpsIntervalOutRapsSf_Object = MibTableColumn
erpsIntervalOutRapsSf = _ErpsIntervalOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 18),
    _ErpsIntervalOutRapsSf_Type()
)
erpsIntervalOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsSf.setStatus("current")
_ErpsIntervalOutRapsMs_Type = Counter32
_ErpsIntervalOutRapsMs_Object = MibTableColumn
erpsIntervalOutRapsMs = _ErpsIntervalOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 19),
    _ErpsIntervalOutRapsMs_Type()
)
erpsIntervalOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsMs.setStatus("current")
_ErpsIntervalOutRapsTotal_Type = Counter32
_ErpsIntervalOutRapsTotal_Object = MibTableColumn
erpsIntervalOutRapsTotal = _ErpsIntervalOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 20),
    _ErpsIntervalOutRapsTotal_Type()
)
erpsIntervalOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalOutRapsTotal.setStatus("current")
_ErpsIntervalProtectionSwitches_Type = Counter32
_ErpsIntervalProtectionSwitches_Object = MibTableColumn
erpsIntervalProtectionSwitches = _ErpsIntervalProtectionSwitches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 2, 1, 21),
    _ErpsIntervalProtectionSwitches_Type()
)
erpsIntervalProtectionSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsIntervalProtectionSwitches.setStatus("current")
_ErpsCountersDayTable_Object = MibTable
erpsCountersDayTable = _ErpsCountersDayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3)
)
if mibBuilder.loadTexts:
    erpsCountersDayTable.setStatus("current")
_ErpsCountersDayEntry_Object = MibTableRow
erpsCountersDayEntry = _ErpsCountersDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1)
)
erpsCountersDayEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsDayIfIndex"),
)
if mibBuilder.loadTexts:
    erpsCountersDayEntry.setStatus("current")
_ErpsDayIfIndex_Type = InterfaceIndex
_ErpsDayIfIndex_Object = MibTableColumn
erpsDayIfIndex = _ErpsDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 1),
    _ErpsDayIfIndex_Type()
)
erpsDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsDayIfIndex.setStatus("current")
_ErpsDayInRapsNrRb_Type = Counter32
_ErpsDayInRapsNrRb_Object = MibTableColumn
erpsDayInRapsNrRb = _ErpsDayInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 2),
    _ErpsDayInRapsNrRb_Type()
)
erpsDayInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsNrRb.setStatus("current")
_ErpsDayInRapsNrRbDnf_Type = Counter32
_ErpsDayInRapsNrRbDnf_Object = MibTableColumn
erpsDayInRapsNrRbDnf = _ErpsDayInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 3),
    _ErpsDayInRapsNrRbDnf_Type()
)
erpsDayInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsNrRbDnf.setStatus("current")
_ErpsDayInRapsNr_Type = Counter32
_ErpsDayInRapsNr_Object = MibTableColumn
erpsDayInRapsNr = _ErpsDayInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 4),
    _ErpsDayInRapsNr_Type()
)
erpsDayInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsNr.setStatus("current")
_ErpsDayInRapsFs_Type = Counter32
_ErpsDayInRapsFs_Object = MibTableColumn
erpsDayInRapsFs = _ErpsDayInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 5),
    _ErpsDayInRapsFs_Type()
)
erpsDayInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsFs.setStatus("current")
_ErpsDayInRapsSf_Type = Counter32
_ErpsDayInRapsSf_Object = MibTableColumn
erpsDayInRapsSf = _ErpsDayInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 6),
    _ErpsDayInRapsSf_Type()
)
erpsDayInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsSf.setStatus("current")
_ErpsDayInRapsMs_Type = Counter32
_ErpsDayInRapsMs_Object = MibTableColumn
erpsDayInRapsMs = _ErpsDayInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 7),
    _ErpsDayInRapsMs_Type()
)
erpsDayInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsMs.setStatus("current")
_ErpsDayInRapsIgnored_Type = Counter32
_ErpsDayInRapsIgnored_Object = MibTableColumn
erpsDayInRapsIgnored = _ErpsDayInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 8),
    _ErpsDayInRapsIgnored_Type()
)
erpsDayInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsIgnored.setStatus("current")
_ErpsDayInRapsTotal_Type = Counter32
_ErpsDayInRapsTotal_Object = MibTableColumn
erpsDayInRapsTotal = _ErpsDayInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 9),
    _ErpsDayInRapsTotal_Type()
)
erpsDayInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayInRapsTotal.setStatus("current")
_ErpsDayOutRapsNrRb_Type = Counter32
_ErpsDayOutRapsNrRb_Object = MibTableColumn
erpsDayOutRapsNrRb = _ErpsDayOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 10),
    _ErpsDayOutRapsNrRb_Type()
)
erpsDayOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsNrRb.setStatus("current")
_ErpsDayOutRapsNrRbDnf_Type = Counter32
_ErpsDayOutRapsNrRbDnf_Object = MibTableColumn
erpsDayOutRapsNrRbDnf = _ErpsDayOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 11),
    _ErpsDayOutRapsNrRbDnf_Type()
)
erpsDayOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsNrRbDnf.setStatus("current")
_ErpsDayOutRapsNr_Type = Counter32
_ErpsDayOutRapsNr_Object = MibTableColumn
erpsDayOutRapsNr = _ErpsDayOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 12),
    _ErpsDayOutRapsNr_Type()
)
erpsDayOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsNr.setStatus("current")
_ErpsDayOutRapsFs_Type = Counter32
_ErpsDayOutRapsFs_Object = MibTableColumn
erpsDayOutRapsFs = _ErpsDayOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 13),
    _ErpsDayOutRapsFs_Type()
)
erpsDayOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsFs.setStatus("current")
_ErpsDayOutRapsSf_Type = Counter32
_ErpsDayOutRapsSf_Object = MibTableColumn
erpsDayOutRapsSf = _ErpsDayOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 14),
    _ErpsDayOutRapsSf_Type()
)
erpsDayOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsSf.setStatus("current")
_ErpsDayOutRapsMs_Type = Counter32
_ErpsDayOutRapsMs_Object = MibTableColumn
erpsDayOutRapsMs = _ErpsDayOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 15),
    _ErpsDayOutRapsMs_Type()
)
erpsDayOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsMs.setStatus("current")
_ErpsDayOutRapsTotal_Type = Counter32
_ErpsDayOutRapsTotal_Object = MibTableColumn
erpsDayOutRapsTotal = _ErpsDayOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 16),
    _ErpsDayOutRapsTotal_Type()
)
erpsDayOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayOutRapsTotal.setStatus("current")
_ErpsDayProtectionSwitches_Type = Counter32
_ErpsDayProtectionSwitches_Object = MibTableColumn
erpsDayProtectionSwitches = _ErpsDayProtectionSwitches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 3, 1, 17),
    _ErpsDayProtectionSwitches_Type()
)
erpsDayProtectionSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDayProtectionSwitches.setStatus("current")
_ErpsCountersStatsTable_Object = MibTable
erpsCountersStatsTable = _ErpsCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4)
)
if mibBuilder.loadTexts:
    erpsCountersStatsTable.setStatus("current")
_ErpsCountersStatsEntry_Object = MibTableRow
erpsCountersStatsEntry = _ErpsCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1)
)
erpsCountersStatsEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsStatsIfIndex"),
)
if mibBuilder.loadTexts:
    erpsCountersStatsEntry.setStatus("current")
_ErpsStatsIfIndex_Type = InterfaceIndex
_ErpsStatsIfIndex_Object = MibTableColumn
erpsStatsIfIndex = _ErpsStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 1),
    _ErpsStatsIfIndex_Type()
)
erpsStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsStatsIfIndex.setStatus("current")
_ErpsStatsInRapsNrRb_Type = Counter32
_ErpsStatsInRapsNrRb_Object = MibTableColumn
erpsStatsInRapsNrRb = _ErpsStatsInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 2),
    _ErpsStatsInRapsNrRb_Type()
)
erpsStatsInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsNrRb.setStatus("current")
_ErpsStatsInRapsNrRbDnf_Type = Counter32
_ErpsStatsInRapsNrRbDnf_Object = MibTableColumn
erpsStatsInRapsNrRbDnf = _ErpsStatsInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 3),
    _ErpsStatsInRapsNrRbDnf_Type()
)
erpsStatsInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsNrRbDnf.setStatus("current")
_ErpsStatsInRapsNr_Type = Counter32
_ErpsStatsInRapsNr_Object = MibTableColumn
erpsStatsInRapsNr = _ErpsStatsInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 4),
    _ErpsStatsInRapsNr_Type()
)
erpsStatsInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsNr.setStatus("current")
_ErpsStatsInRapsFs_Type = Counter32
_ErpsStatsInRapsFs_Object = MibTableColumn
erpsStatsInRapsFs = _ErpsStatsInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 5),
    _ErpsStatsInRapsFs_Type()
)
erpsStatsInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsFs.setStatus("current")
_ErpsStatsInRapsSf_Type = Counter32
_ErpsStatsInRapsSf_Object = MibTableColumn
erpsStatsInRapsSf = _ErpsStatsInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 6),
    _ErpsStatsInRapsSf_Type()
)
erpsStatsInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsSf.setStatus("current")
_ErpsStatsInRapsMs_Type = Counter32
_ErpsStatsInRapsMs_Object = MibTableColumn
erpsStatsInRapsMs = _ErpsStatsInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 7),
    _ErpsStatsInRapsMs_Type()
)
erpsStatsInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsMs.setStatus("current")
_ErpsStatsInRapsIgnored_Type = Counter32
_ErpsStatsInRapsIgnored_Object = MibTableColumn
erpsStatsInRapsIgnored = _ErpsStatsInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 8),
    _ErpsStatsInRapsIgnored_Type()
)
erpsStatsInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsIgnored.setStatus("current")
_ErpsStatsInRapsTotal_Type = Counter32
_ErpsStatsInRapsTotal_Object = MibTableColumn
erpsStatsInRapsTotal = _ErpsStatsInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 9),
    _ErpsStatsInRapsTotal_Type()
)
erpsStatsInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsInRapsTotal.setStatus("current")
_ErpsStatsOutRapsNrRb_Type = Counter32
_ErpsStatsOutRapsNrRb_Object = MibTableColumn
erpsStatsOutRapsNrRb = _ErpsStatsOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 10),
    _ErpsStatsOutRapsNrRb_Type()
)
erpsStatsOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsNrRb.setStatus("current")
_ErpsStatsOutRapsNrRbDnf_Type = Counter32
_ErpsStatsOutRapsNrRbDnf_Object = MibTableColumn
erpsStatsOutRapsNrRbDnf = _ErpsStatsOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 11),
    _ErpsStatsOutRapsNrRbDnf_Type()
)
erpsStatsOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsNrRbDnf.setStatus("current")
_ErpsStatsOutRapsNr_Type = Counter32
_ErpsStatsOutRapsNr_Object = MibTableColumn
erpsStatsOutRapsNr = _ErpsStatsOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 12),
    _ErpsStatsOutRapsNr_Type()
)
erpsStatsOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsNr.setStatus("current")
_ErpsStatsOutRapsFs_Type = Counter32
_ErpsStatsOutRapsFs_Object = MibTableColumn
erpsStatsOutRapsFs = _ErpsStatsOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 13),
    _ErpsStatsOutRapsFs_Type()
)
erpsStatsOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsFs.setStatus("current")
_ErpsStatsOutRapsSf_Type = Counter32
_ErpsStatsOutRapsSf_Object = MibTableColumn
erpsStatsOutRapsSf = _ErpsStatsOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 14),
    _ErpsStatsOutRapsSf_Type()
)
erpsStatsOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsSf.setStatus("current")
_ErpsStatsOutRapsMs_Type = Counter32
_ErpsStatsOutRapsMs_Object = MibTableColumn
erpsStatsOutRapsMs = _ErpsStatsOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 15),
    _ErpsStatsOutRapsMs_Type()
)
erpsStatsOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsMs.setStatus("current")
_ErpsStatsOutRapsTotal_Type = Counter32
_ErpsStatsOutRapsTotal_Object = MibTableColumn
erpsStatsOutRapsTotal = _ErpsStatsOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 16),
    _ErpsStatsOutRapsTotal_Type()
)
erpsStatsOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsOutRapsTotal.setStatus("current")
_ErpsStatsProtectionSwitches_Type = Counter32
_ErpsStatsProtectionSwitches_Object = MibTableColumn
erpsStatsProtectionSwitches = _ErpsStatsProtectionSwitches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 4, 1, 17),
    _ErpsStatsProtectionSwitches_Type()
)
erpsStatsProtectionSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsStatsProtectionSwitches.setStatus("current")
_ErpsCounters24HrCurrentTable_Object = MibTable
erpsCounters24HrCurrentTable = _ErpsCounters24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5)
)
if mibBuilder.loadTexts:
    erpsCounters24HrCurrentTable.setStatus("current")
_ErpsCounters24HrCurrentEntry_Object = MibTableRow
erpsCounters24HrCurrentEntry = _ErpsCounters24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1)
)
erpsCounters24HrCurrentEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erps24HrCurrentIfIndex"),
)
if mibBuilder.loadTexts:
    erpsCounters24HrCurrentEntry.setStatus("current")
_Erps24HrCurrentIfIndex_Type = InterfaceIndex
_Erps24HrCurrentIfIndex_Object = MibTableColumn
erps24HrCurrentIfIndex = _Erps24HrCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 1),
    _Erps24HrCurrentIfIndex_Type()
)
erps24HrCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erps24HrCurrentIfIndex.setStatus("current")
_Erps24HrCurrentInRapsNrRb_Type = Counter32
_Erps24HrCurrentInRapsNrRb_Object = MibTableColumn
erps24HrCurrentInRapsNrRb = _Erps24HrCurrentInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 2),
    _Erps24HrCurrentInRapsNrRb_Type()
)
erps24HrCurrentInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsNrRb.setStatus("current")
_Erps24HrCurrentInRapsDnf_Type = Counter32
_Erps24HrCurrentInRapsDnf_Object = MibTableColumn
erps24HrCurrentInRapsDnf = _Erps24HrCurrentInRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 3),
    _Erps24HrCurrentInRapsDnf_Type()
)
erps24HrCurrentInRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsDnf.setStatus("current")
_Erps24HrCurrentInRapsNr_Type = Counter32
_Erps24HrCurrentInRapsNr_Object = MibTableColumn
erps24HrCurrentInRapsNr = _Erps24HrCurrentInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 4),
    _Erps24HrCurrentInRapsNr_Type()
)
erps24HrCurrentInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsNr.setStatus("current")
_Erps24HrCurrentInRapsFs_Type = Counter32
_Erps24HrCurrentInRapsFs_Object = MibTableColumn
erps24HrCurrentInRapsFs = _Erps24HrCurrentInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 5),
    _Erps24HrCurrentInRapsFs_Type()
)
erps24HrCurrentInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsFs.setStatus("current")
_Erps24HrCurrentInRapsSf_Type = Counter32
_Erps24HrCurrentInRapsSf_Object = MibTableColumn
erps24HrCurrentInRapsSf = _Erps24HrCurrentInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 6),
    _Erps24HrCurrentInRapsSf_Type()
)
erps24HrCurrentInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsSf.setStatus("current")
_Erps24HrCurrentInRapsMs_Type = Counter32
_Erps24HrCurrentInRapsMs_Object = MibTableColumn
erps24HrCurrentInRapsMs = _Erps24HrCurrentInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 7),
    _Erps24HrCurrentInRapsMs_Type()
)
erps24HrCurrentInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsMs.setStatus("current")
_Erps24HrCurrentInRapsIgnored_Type = Counter32
_Erps24HrCurrentInRapsIgnored_Object = MibTableColumn
erps24HrCurrentInRapsIgnored = _Erps24HrCurrentInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 8),
    _Erps24HrCurrentInRapsIgnored_Type()
)
erps24HrCurrentInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsIgnored.setStatus("current")
_Erps24HrCurrentInRapsTotal_Type = Counter32
_Erps24HrCurrentInRapsTotal_Object = MibTableColumn
erps24HrCurrentInRapsTotal = _Erps24HrCurrentInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 9),
    _Erps24HrCurrentInRapsTotal_Type()
)
erps24HrCurrentInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentInRapsTotal.setStatus("current")
_Erps24HrCurrentOutRapsNrRb_Type = Counter32
_Erps24HrCurrentOutRapsNrRb_Object = MibTableColumn
erps24HrCurrentOutRapsNrRb = _Erps24HrCurrentOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 10),
    _Erps24HrCurrentOutRapsNrRb_Type()
)
erps24HrCurrentOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsNrRb.setStatus("current")
_Erps24HrCurrentOutRapsDnf_Type = Counter32
_Erps24HrCurrentOutRapsDnf_Object = MibTableColumn
erps24HrCurrentOutRapsDnf = _Erps24HrCurrentOutRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 11),
    _Erps24HrCurrentOutRapsDnf_Type()
)
erps24HrCurrentOutRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsDnf.setStatus("current")
_Erps24HrCurrentOutRapsNr_Type = Counter32
_Erps24HrCurrentOutRapsNr_Object = MibTableColumn
erps24HrCurrentOutRapsNr = _Erps24HrCurrentOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 12),
    _Erps24HrCurrentOutRapsNr_Type()
)
erps24HrCurrentOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsNr.setStatus("current")
_Erps24HrCurrentOutRapsFs_Type = Counter32
_Erps24HrCurrentOutRapsFs_Object = MibTableColumn
erps24HrCurrentOutRapsFs = _Erps24HrCurrentOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 13),
    _Erps24HrCurrentOutRapsFs_Type()
)
erps24HrCurrentOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsFs.setStatus("current")
_Erps24HrCurrentOutRapsSf_Type = Counter32
_Erps24HrCurrentOutRapsSf_Object = MibTableColumn
erps24HrCurrentOutRapsSf = _Erps24HrCurrentOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 14),
    _Erps24HrCurrentOutRapsSf_Type()
)
erps24HrCurrentOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsSf.setStatus("current")
_Erps24HrCurrentOutRapsMs_Type = Counter32
_Erps24HrCurrentOutRapsMs_Object = MibTableColumn
erps24HrCurrentOutRapsMs = _Erps24HrCurrentOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 15),
    _Erps24HrCurrentOutRapsMs_Type()
)
erps24HrCurrentOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsMs.setStatus("current")
_Erps24HrCurrentOutRapsTotal_Type = Counter32
_Erps24HrCurrentOutRapsTotal_Object = MibTableColumn
erps24HrCurrentOutRapsTotal = _Erps24HrCurrentOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 16),
    _Erps24HrCurrentOutRapsTotal_Type()
)
erps24HrCurrentOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentOutRapsTotal.setStatus("current")
_Erps24HrCurrentProtectionSwitches_Type = Counter32
_Erps24HrCurrentProtectionSwitches_Object = MibTableColumn
erps24HrCurrentProtectionSwitches = _Erps24HrCurrentProtectionSwitches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 5, 1, 17),
    _Erps24HrCurrentProtectionSwitches_Type()
)
erps24HrCurrentProtectionSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrCurrentProtectionSwitches.setStatus("current")
_ErpsCounters24HrIntervalTable_Object = MibTable
erpsCounters24HrIntervalTable = _ErpsCounters24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6)
)
if mibBuilder.loadTexts:
    erpsCounters24HrIntervalTable.setStatus("current")
_ErpsCounters24HrIntervalEntry_Object = MibTableRow
erpsCounters24HrIntervalEntry = _ErpsCounters24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1)
)
erpsCounters24HrIntervalEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erps24HrIntervalIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erps24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    erpsCounters24HrIntervalEntry.setStatus("current")
_Erps24HrIntervalIfIndex_Type = InterfaceIndex
_Erps24HrIntervalIfIndex_Object = MibTableColumn
erps24HrIntervalIfIndex = _Erps24HrIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 1),
    _Erps24HrIntervalIfIndex_Type()
)
erps24HrIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erps24HrIntervalIfIndex.setStatus("current")


class _Erps24HrIntervalNumber_Type(Unsigned32):
    """Custom type erps24HrIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Erps24HrIntervalNumber_Type.__name__ = "Unsigned32"
_Erps24HrIntervalNumber_Object = MibTableColumn
erps24HrIntervalNumber = _Erps24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 2),
    _Erps24HrIntervalNumber_Type()
)
erps24HrIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erps24HrIntervalNumber.setStatus("current")
_Erps24HrIntervalValidData_Type = TruthValue
_Erps24HrIntervalValidData_Object = MibTableColumn
erps24HrIntervalValidData = _Erps24HrIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 3),
    _Erps24HrIntervalValidData_Type()
)
erps24HrIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalValidData.setStatus("current")
_Erps24HrIntervalTimeElapsed_Type = Unsigned32
_Erps24HrIntervalTimeElapsed_Object = MibTableColumn
erps24HrIntervalTimeElapsed = _Erps24HrIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 4),
    _Erps24HrIntervalTimeElapsed_Type()
)
erps24HrIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    erps24HrIntervalTimeElapsed.setUnits("Seconds")
_Erps24HrIntervalStartTime_Type = DateAndTime
_Erps24HrIntervalStartTime_Object = MibTableColumn
erps24HrIntervalStartTime = _Erps24HrIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 5),
    _Erps24HrIntervalStartTime_Type()
)
erps24HrIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalStartTime.setStatus("current")
_Erps24HrIntervalInRapsNrRb_Type = Counter32
_Erps24HrIntervalInRapsNrRb_Object = MibTableColumn
erps24HrIntervalInRapsNrRb = _Erps24HrIntervalInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 6),
    _Erps24HrIntervalInRapsNrRb_Type()
)
erps24HrIntervalInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsNrRb.setStatus("current")
_Erps24HrIntervalInRapsDnf_Type = Counter32
_Erps24HrIntervalInRapsDnf_Object = MibTableColumn
erps24HrIntervalInRapsDnf = _Erps24HrIntervalInRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 7),
    _Erps24HrIntervalInRapsDnf_Type()
)
erps24HrIntervalInRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsDnf.setStatus("current")
_Erps24HrIntervalInRapsNr_Type = Counter32
_Erps24HrIntervalInRapsNr_Object = MibTableColumn
erps24HrIntervalInRapsNr = _Erps24HrIntervalInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 8),
    _Erps24HrIntervalInRapsNr_Type()
)
erps24HrIntervalInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsNr.setStatus("current")
_Erps24HrIntervalInRapsFs_Type = Counter32
_Erps24HrIntervalInRapsFs_Object = MibTableColumn
erps24HrIntervalInRapsFs = _Erps24HrIntervalInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 9),
    _Erps24HrIntervalInRapsFs_Type()
)
erps24HrIntervalInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsFs.setStatus("current")
_Erps24HrIntervalInRapsSf_Type = Counter32
_Erps24HrIntervalInRapsSf_Object = MibTableColumn
erps24HrIntervalInRapsSf = _Erps24HrIntervalInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 10),
    _Erps24HrIntervalInRapsSf_Type()
)
erps24HrIntervalInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsSf.setStatus("current")
_Erps24HrIntervalInRapsMs_Type = Counter32
_Erps24HrIntervalInRapsMs_Object = MibTableColumn
erps24HrIntervalInRapsMs = _Erps24HrIntervalInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 11),
    _Erps24HrIntervalInRapsMs_Type()
)
erps24HrIntervalInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsMs.setStatus("current")
_Erps24HrIntervalInRapsIgnored_Type = Counter32
_Erps24HrIntervalInRapsIgnored_Object = MibTableColumn
erps24HrIntervalInRapsIgnored = _Erps24HrIntervalInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 12),
    _Erps24HrIntervalInRapsIgnored_Type()
)
erps24HrIntervalInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsIgnored.setStatus("current")
_Erps24HrIntervalInRapsTotal_Type = Counter32
_Erps24HrIntervalInRapsTotal_Object = MibTableColumn
erps24HrIntervalInRapsTotal = _Erps24HrIntervalInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 13),
    _Erps24HrIntervalInRapsTotal_Type()
)
erps24HrIntervalInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalInRapsTotal.setStatus("current")
_Erps24HrIntervalOutRapsNrRb_Type = Counter32
_Erps24HrIntervalOutRapsNrRb_Object = MibTableColumn
erps24HrIntervalOutRapsNrRb = _Erps24HrIntervalOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 14),
    _Erps24HrIntervalOutRapsNrRb_Type()
)
erps24HrIntervalOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsNrRb.setStatus("current")
_Erps24HrIntervalOutRapsDnf_Type = Counter32
_Erps24HrIntervalOutRapsDnf_Object = MibTableColumn
erps24HrIntervalOutRapsDnf = _Erps24HrIntervalOutRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 15),
    _Erps24HrIntervalOutRapsDnf_Type()
)
erps24HrIntervalOutRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsDnf.setStatus("current")
_Erps24HrIntervalOutRapsNr_Type = Counter32
_Erps24HrIntervalOutRapsNr_Object = MibTableColumn
erps24HrIntervalOutRapsNr = _Erps24HrIntervalOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 16),
    _Erps24HrIntervalOutRapsNr_Type()
)
erps24HrIntervalOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsNr.setStatus("current")
_Erps24HrIntervalOutRapsFs_Type = Counter32
_Erps24HrIntervalOutRapsFs_Object = MibTableColumn
erps24HrIntervalOutRapsFs = _Erps24HrIntervalOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 17),
    _Erps24HrIntervalOutRapsFs_Type()
)
erps24HrIntervalOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsFs.setStatus("current")
_Erps24HrIntervalOutRapsSf_Type = Counter32
_Erps24HrIntervalOutRapsSf_Object = MibTableColumn
erps24HrIntervalOutRapsSf = _Erps24HrIntervalOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 18),
    _Erps24HrIntervalOutRapsSf_Type()
)
erps24HrIntervalOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsSf.setStatus("current")
_Erps24HrIntervalOutRapsMs_Type = Counter32
_Erps24HrIntervalOutRapsMs_Object = MibTableColumn
erps24HrIntervalOutRapsMs = _Erps24HrIntervalOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 19),
    _Erps24HrIntervalOutRapsMs_Type()
)
erps24HrIntervalOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsMs.setStatus("current")
_Erps24HrIntervalOutRapsTotal_Type = Counter32
_Erps24HrIntervalOutRapsTotal_Object = MibTableColumn
erps24HrIntervalOutRapsTotal = _Erps24HrIntervalOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 20),
    _Erps24HrIntervalOutRapsTotal_Type()
)
erps24HrIntervalOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalOutRapsTotal.setStatus("current")
_Erps24HrIntervalProtectionSwitches_Type = Counter32
_Erps24HrIntervalProtectionSwitches_Object = MibTableColumn
erps24HrIntervalProtectionSwitches = _Erps24HrIntervalProtectionSwitches_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 3, 6, 1, 21),
    _Erps24HrIntervalProtectionSwitches_Type()
)
erps24HrIntervalProtectionSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erps24HrIntervalProtectionSwitches.setStatus("current")
_ErpsSpanCounters_ObjectIdentity = ObjectIdentity
erpsSpanCounters = _ErpsSpanCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4)
)
_ErpsSpanCountersCurrentTable_Object = MibTable
erpsSpanCountersCurrentTable = _ErpsSpanCountersCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1)
)
if mibBuilder.loadTexts:
    erpsSpanCountersCurrentTable.setStatus("current")
_ErpsSpanCountersCurrentEntry_Object = MibTableRow
erpsSpanCountersCurrentEntry = _ErpsSpanCountersCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1)
)
erpsSpanCountersCurrentEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpanCurrentIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpanCurrentSpan"),
)
if mibBuilder.loadTexts:
    erpsSpanCountersCurrentEntry.setStatus("current")
_ErpsSpanCurrentIfIndex_Type = InterfaceIndex
_ErpsSpanCurrentIfIndex_Object = MibTableColumn
erpsSpanCurrentIfIndex = _ErpsSpanCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 1),
    _ErpsSpanCurrentIfIndex_Type()
)
erpsSpanCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanCurrentIfIndex.setStatus("current")
_ErpsSpanCurrentSpan_Type = ErpsSpan
_ErpsSpanCurrentSpan_Object = MibTableColumn
erpsSpanCurrentSpan = _ErpsSpanCurrentSpan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 2),
    _ErpsSpanCurrentSpan_Type()
)
erpsSpanCurrentSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanCurrentSpan.setStatus("current")
_ErpsSpanCurrentInRapsNrRb_Type = Counter32
_ErpsSpanCurrentInRapsNrRb_Object = MibTableColumn
erpsSpanCurrentInRapsNrRb = _ErpsSpanCurrentInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 3),
    _ErpsSpanCurrentInRapsNrRb_Type()
)
erpsSpanCurrentInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsNrRb.setStatus("current")
_ErpsSpanCurrentInRapsNrRbDnf_Type = Counter32
_ErpsSpanCurrentInRapsNrRbDnf_Object = MibTableColumn
erpsSpanCurrentInRapsNrRbDnf = _ErpsSpanCurrentInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 4),
    _ErpsSpanCurrentInRapsNrRbDnf_Type()
)
erpsSpanCurrentInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsNrRbDnf.setStatus("current")
_ErpsSpanCurrentInRapsNr_Type = Counter32
_ErpsSpanCurrentInRapsNr_Object = MibTableColumn
erpsSpanCurrentInRapsNr = _ErpsSpanCurrentInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 5),
    _ErpsSpanCurrentInRapsNr_Type()
)
erpsSpanCurrentInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsNr.setStatus("current")
_ErpsSpanCurrentInRapsFs_Type = Counter32
_ErpsSpanCurrentInRapsFs_Object = MibTableColumn
erpsSpanCurrentInRapsFs = _ErpsSpanCurrentInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 6),
    _ErpsSpanCurrentInRapsFs_Type()
)
erpsSpanCurrentInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsFs.setStatus("current")
_ErpsSpanCurrentInRapsSf_Type = Counter32
_ErpsSpanCurrentInRapsSf_Object = MibTableColumn
erpsSpanCurrentInRapsSf = _ErpsSpanCurrentInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 7),
    _ErpsSpanCurrentInRapsSf_Type()
)
erpsSpanCurrentInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsSf.setStatus("current")
_ErpsSpanCurrentInRapsMs_Type = Counter32
_ErpsSpanCurrentInRapsMs_Object = MibTableColumn
erpsSpanCurrentInRapsMs = _ErpsSpanCurrentInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 8),
    _ErpsSpanCurrentInRapsMs_Type()
)
erpsSpanCurrentInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsMs.setStatus("current")
_ErpsSpanCurrentInRapsIgnored_Type = Counter32
_ErpsSpanCurrentInRapsIgnored_Object = MibTableColumn
erpsSpanCurrentInRapsIgnored = _ErpsSpanCurrentInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 9),
    _ErpsSpanCurrentInRapsIgnored_Type()
)
erpsSpanCurrentInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsIgnored.setStatus("current")
_ErpsSpanCurrentInRapsTotal_Type = Counter32
_ErpsSpanCurrentInRapsTotal_Object = MibTableColumn
erpsSpanCurrentInRapsTotal = _ErpsSpanCurrentInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 10),
    _ErpsSpanCurrentInRapsTotal_Type()
)
erpsSpanCurrentInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentInRapsTotal.setStatus("current")
_ErpsSpanCurrentOutRapsNrRb_Type = Counter32
_ErpsSpanCurrentOutRapsNrRb_Object = MibTableColumn
erpsSpanCurrentOutRapsNrRb = _ErpsSpanCurrentOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 11),
    _ErpsSpanCurrentOutRapsNrRb_Type()
)
erpsSpanCurrentOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsNrRb.setStatus("current")
_ErpsSpanCurrentOutRapsNrRbDnf_Type = Counter32
_ErpsSpanCurrentOutRapsNrRbDnf_Object = MibTableColumn
erpsSpanCurrentOutRapsNrRbDnf = _ErpsSpanCurrentOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 12),
    _ErpsSpanCurrentOutRapsNrRbDnf_Type()
)
erpsSpanCurrentOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsNrRbDnf.setStatus("current")
_ErpsSpanCurrentOutRapsNr_Type = Counter32
_ErpsSpanCurrentOutRapsNr_Object = MibTableColumn
erpsSpanCurrentOutRapsNr = _ErpsSpanCurrentOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 13),
    _ErpsSpanCurrentOutRapsNr_Type()
)
erpsSpanCurrentOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsNr.setStatus("current")
_ErpsSpanCurrentOutRapsFs_Type = Counter32
_ErpsSpanCurrentOutRapsFs_Object = MibTableColumn
erpsSpanCurrentOutRapsFs = _ErpsSpanCurrentOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 14),
    _ErpsSpanCurrentOutRapsFs_Type()
)
erpsSpanCurrentOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsFs.setStatus("current")
_ErpsSpanCurrentOutRapsSf_Type = Counter32
_ErpsSpanCurrentOutRapsSf_Object = MibTableColumn
erpsSpanCurrentOutRapsSf = _ErpsSpanCurrentOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 15),
    _ErpsSpanCurrentOutRapsSf_Type()
)
erpsSpanCurrentOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsSf.setStatus("current")
_ErpsSpanCurrentOutRapsMs_Type = Counter32
_ErpsSpanCurrentOutRapsMs_Object = MibTableColumn
erpsSpanCurrentOutRapsMs = _ErpsSpanCurrentOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 16),
    _ErpsSpanCurrentOutRapsMs_Type()
)
erpsSpanCurrentOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsMs.setStatus("current")
_ErpsSpanCurrentOutRapsTotal_Type = Counter32
_ErpsSpanCurrentOutRapsTotal_Object = MibTableColumn
erpsSpanCurrentOutRapsTotal = _ErpsSpanCurrentOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 1, 1, 17),
    _ErpsSpanCurrentOutRapsTotal_Type()
)
erpsSpanCurrentOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanCurrentOutRapsTotal.setStatus("current")
_ErpsSpanCountersIntervalTable_Object = MibTable
erpsSpanCountersIntervalTable = _ErpsSpanCountersIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2)
)
if mibBuilder.loadTexts:
    erpsSpanCountersIntervalTable.setStatus("current")
_ErpsSpanCountersIntervalEntry_Object = MibTableRow
erpsSpanCountersIntervalEntry = _ErpsSpanCountersIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1)
)
erpsSpanCountersIntervalEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpanIntervalIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpanIntervalSpan"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpanIntervalNumber"),
)
if mibBuilder.loadTexts:
    erpsSpanCountersIntervalEntry.setStatus("current")
_ErpsSpanIntervalIfIndex_Type = InterfaceIndex
_ErpsSpanIntervalIfIndex_Object = MibTableColumn
erpsSpanIntervalIfIndex = _ErpsSpanIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 1),
    _ErpsSpanIntervalIfIndex_Type()
)
erpsSpanIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanIntervalIfIndex.setStatus("current")
_ErpsSpanIntervalSpan_Type = ErpsSpan
_ErpsSpanIntervalSpan_Object = MibTableColumn
erpsSpanIntervalSpan = _ErpsSpanIntervalSpan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 2),
    _ErpsSpanIntervalSpan_Type()
)
erpsSpanIntervalSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanIntervalSpan.setStatus("current")


class _ErpsSpanIntervalNumber_Type(Unsigned32):
    """Custom type erpsSpanIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ErpsSpanIntervalNumber_Type.__name__ = "Unsigned32"
_ErpsSpanIntervalNumber_Object = MibTableColumn
erpsSpanIntervalNumber = _ErpsSpanIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 3),
    _ErpsSpanIntervalNumber_Type()
)
erpsSpanIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanIntervalNumber.setStatus("current")
_ErpsSpanIntervalValidData_Type = TruthValue
_ErpsSpanIntervalValidData_Object = MibTableColumn
erpsSpanIntervalValidData = _ErpsSpanIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 4),
    _ErpsSpanIntervalValidData_Type()
)
erpsSpanIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalValidData.setStatus("current")


class _ErpsSpanIntervalTimeElapsed_Type(Unsigned32):
    """Custom type erpsSpanIntervalTimeElapsed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 910),
    )


_ErpsSpanIntervalTimeElapsed_Type.__name__ = "Unsigned32"
_ErpsSpanIntervalTimeElapsed_Object = MibTableColumn
erpsSpanIntervalTimeElapsed = _ErpsSpanIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 5),
    _ErpsSpanIntervalTimeElapsed_Type()
)
erpsSpanIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    erpsSpanIntervalTimeElapsed.setUnits("Seconds")
_ErpsSpanIntervalStartTime_Type = DateAndTime
_ErpsSpanIntervalStartTime_Object = MibTableColumn
erpsSpanIntervalStartTime = _ErpsSpanIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 6),
    _ErpsSpanIntervalStartTime_Type()
)
erpsSpanIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalStartTime.setStatus("current")
_ErpsSpanIntervalInRapsNrRb_Type = Counter32
_ErpsSpanIntervalInRapsNrRb_Object = MibTableColumn
erpsSpanIntervalInRapsNrRb = _ErpsSpanIntervalInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 7),
    _ErpsSpanIntervalInRapsNrRb_Type()
)
erpsSpanIntervalInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsNrRb.setStatus("current")
_ErpsSpanIntervalInRapsNrRbDnf_Type = Counter32
_ErpsSpanIntervalInRapsNrRbDnf_Object = MibTableColumn
erpsSpanIntervalInRapsNrRbDnf = _ErpsSpanIntervalInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 8),
    _ErpsSpanIntervalInRapsNrRbDnf_Type()
)
erpsSpanIntervalInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsNrRbDnf.setStatus("current")
_ErpsSpanIntervalInRapsNr_Type = Counter32
_ErpsSpanIntervalInRapsNr_Object = MibTableColumn
erpsSpanIntervalInRapsNr = _ErpsSpanIntervalInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 9),
    _ErpsSpanIntervalInRapsNr_Type()
)
erpsSpanIntervalInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsNr.setStatus("current")
_ErpsSpanIntervalInRapsFs_Type = Counter32
_ErpsSpanIntervalInRapsFs_Object = MibTableColumn
erpsSpanIntervalInRapsFs = _ErpsSpanIntervalInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 10),
    _ErpsSpanIntervalInRapsFs_Type()
)
erpsSpanIntervalInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsFs.setStatus("current")
_ErpsSpanIntervalInRapsSf_Type = Counter32
_ErpsSpanIntervalInRapsSf_Object = MibTableColumn
erpsSpanIntervalInRapsSf = _ErpsSpanIntervalInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 11),
    _ErpsSpanIntervalInRapsSf_Type()
)
erpsSpanIntervalInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsSf.setStatus("current")
_ErpsSpanIntervalInRapsMs_Type = Counter32
_ErpsSpanIntervalInRapsMs_Object = MibTableColumn
erpsSpanIntervalInRapsMs = _ErpsSpanIntervalInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 12),
    _ErpsSpanIntervalInRapsMs_Type()
)
erpsSpanIntervalInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsMs.setStatus("current")
_ErpsSpanIntervalInRapsIgnored_Type = Counter32
_ErpsSpanIntervalInRapsIgnored_Object = MibTableColumn
erpsSpanIntervalInRapsIgnored = _ErpsSpanIntervalInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 13),
    _ErpsSpanIntervalInRapsIgnored_Type()
)
erpsSpanIntervalInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsIgnored.setStatus("current")
_ErpsSpanIntervalInRapsTotal_Type = Counter32
_ErpsSpanIntervalInRapsTotal_Object = MibTableColumn
erpsSpanIntervalInRapsTotal = _ErpsSpanIntervalInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 14),
    _ErpsSpanIntervalInRapsTotal_Type()
)
erpsSpanIntervalInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalInRapsTotal.setStatus("current")
_ErpsSpanIntervalOutRapsNrRb_Type = Counter32
_ErpsSpanIntervalOutRapsNrRb_Object = MibTableColumn
erpsSpanIntervalOutRapsNrRb = _ErpsSpanIntervalOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 15),
    _ErpsSpanIntervalOutRapsNrRb_Type()
)
erpsSpanIntervalOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsNrRb.setStatus("current")
_ErpsSpanIntervalOutRapsNrRbDnf_Type = Counter32
_ErpsSpanIntervalOutRapsNrRbDnf_Object = MibTableColumn
erpsSpanIntervalOutRapsNrRbDnf = _ErpsSpanIntervalOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 16),
    _ErpsSpanIntervalOutRapsNrRbDnf_Type()
)
erpsSpanIntervalOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsNrRbDnf.setStatus("current")
_ErpsSpanIntervalOutRapsNr_Type = Counter32
_ErpsSpanIntervalOutRapsNr_Object = MibTableColumn
erpsSpanIntervalOutRapsNr = _ErpsSpanIntervalOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 17),
    _ErpsSpanIntervalOutRapsNr_Type()
)
erpsSpanIntervalOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsNr.setStatus("current")
_ErpsSpanIntervalOutRapsFs_Type = Counter32
_ErpsSpanIntervalOutRapsFs_Object = MibTableColumn
erpsSpanIntervalOutRapsFs = _ErpsSpanIntervalOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 18),
    _ErpsSpanIntervalOutRapsFs_Type()
)
erpsSpanIntervalOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsFs.setStatus("current")
_ErpsSpanIntervalOutRapsSf_Type = Counter32
_ErpsSpanIntervalOutRapsSf_Object = MibTableColumn
erpsSpanIntervalOutRapsSf = _ErpsSpanIntervalOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 19),
    _ErpsSpanIntervalOutRapsSf_Type()
)
erpsSpanIntervalOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsSf.setStatus("current")
_ErpsSpanIntervalOutRapsMs_Type = Counter32
_ErpsSpanIntervalOutRapsMs_Object = MibTableColumn
erpsSpanIntervalOutRapsMs = _ErpsSpanIntervalOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 20),
    _ErpsSpanIntervalOutRapsMs_Type()
)
erpsSpanIntervalOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsMs.setStatus("current")
_ErpsSpanIntervalOutRapsTotal_Type = Counter32
_ErpsSpanIntervalOutRapsTotal_Object = MibTableColumn
erpsSpanIntervalOutRapsTotal = _ErpsSpanIntervalOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 2, 1, 21),
    _ErpsSpanIntervalOutRapsTotal_Type()
)
erpsSpanIntervalOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanIntervalOutRapsTotal.setStatus("current")
_ErpsSpanCountersDayTable_Object = MibTable
erpsSpanCountersDayTable = _ErpsSpanCountersDayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3)
)
if mibBuilder.loadTexts:
    erpsSpanCountersDayTable.setStatus("current")
_ErpsSpanCountersDayEntry_Object = MibTableRow
erpsSpanCountersDayEntry = _ErpsSpanCountersDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1)
)
erpsSpanCountersDayEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpanDayIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpanDaySpan"),
)
if mibBuilder.loadTexts:
    erpsSpanCountersDayEntry.setStatus("current")
_ErpsSpanDayIfIndex_Type = InterfaceIndex
_ErpsSpanDayIfIndex_Object = MibTableColumn
erpsSpanDayIfIndex = _ErpsSpanDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 1),
    _ErpsSpanDayIfIndex_Type()
)
erpsSpanDayIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanDayIfIndex.setStatus("current")
_ErpsSpanDaySpan_Type = ErpsSpan
_ErpsSpanDaySpan_Object = MibTableColumn
erpsSpanDaySpan = _ErpsSpanDaySpan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 2),
    _ErpsSpanDaySpan_Type()
)
erpsSpanDaySpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanDaySpan.setStatus("current")
_ErpsSpanDayInRapsNrRb_Type = Counter32
_ErpsSpanDayInRapsNrRb_Object = MibTableColumn
erpsSpanDayInRapsNrRb = _ErpsSpanDayInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 3),
    _ErpsSpanDayInRapsNrRb_Type()
)
erpsSpanDayInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsNrRb.setStatus("current")
_ErpsSpanDayInRapsNrRbDnf_Type = Counter32
_ErpsSpanDayInRapsNrRbDnf_Object = MibTableColumn
erpsSpanDayInRapsNrRbDnf = _ErpsSpanDayInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 4),
    _ErpsSpanDayInRapsNrRbDnf_Type()
)
erpsSpanDayInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsNrRbDnf.setStatus("current")
_ErpsSpanDayInRapsNr_Type = Counter32
_ErpsSpanDayInRapsNr_Object = MibTableColumn
erpsSpanDayInRapsNr = _ErpsSpanDayInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 5),
    _ErpsSpanDayInRapsNr_Type()
)
erpsSpanDayInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsNr.setStatus("current")
_ErpsSpanDayInRapsFs_Type = Counter32
_ErpsSpanDayInRapsFs_Object = MibTableColumn
erpsSpanDayInRapsFs = _ErpsSpanDayInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 6),
    _ErpsSpanDayInRapsFs_Type()
)
erpsSpanDayInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsFs.setStatus("current")
_ErpsSpanDayInRapsSf_Type = Counter32
_ErpsSpanDayInRapsSf_Object = MibTableColumn
erpsSpanDayInRapsSf = _ErpsSpanDayInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 7),
    _ErpsSpanDayInRapsSf_Type()
)
erpsSpanDayInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsSf.setStatus("current")
_ErpsSpanDayInRapsMs_Type = Counter32
_ErpsSpanDayInRapsMs_Object = MibTableColumn
erpsSpanDayInRapsMs = _ErpsSpanDayInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 8),
    _ErpsSpanDayInRapsMs_Type()
)
erpsSpanDayInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsMs.setStatus("current")
_ErpsSpanDayInRapsIgnored_Type = Counter32
_ErpsSpanDayInRapsIgnored_Object = MibTableColumn
erpsSpanDayInRapsIgnored = _ErpsSpanDayInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 9),
    _ErpsSpanDayInRapsIgnored_Type()
)
erpsSpanDayInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsIgnored.setStatus("current")
_ErpsSpanDayInRapsTotal_Type = Counter32
_ErpsSpanDayInRapsTotal_Object = MibTableColumn
erpsSpanDayInRapsTotal = _ErpsSpanDayInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 10),
    _ErpsSpanDayInRapsTotal_Type()
)
erpsSpanDayInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayInRapsTotal.setStatus("current")
_ErpsSpanDayOutRapsNrRb_Type = Counter32
_ErpsSpanDayOutRapsNrRb_Object = MibTableColumn
erpsSpanDayOutRapsNrRb = _ErpsSpanDayOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 11),
    _ErpsSpanDayOutRapsNrRb_Type()
)
erpsSpanDayOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsNrRb.setStatus("current")
_ErpsSpanDayOutRapsNrRbDnf_Type = Counter32
_ErpsSpanDayOutRapsNrRbDnf_Object = MibTableColumn
erpsSpanDayOutRapsNrRbDnf = _ErpsSpanDayOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 12),
    _ErpsSpanDayOutRapsNrRbDnf_Type()
)
erpsSpanDayOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsNrRbDnf.setStatus("current")
_ErpsSpanDayOutRapsNr_Type = Counter32
_ErpsSpanDayOutRapsNr_Object = MibTableColumn
erpsSpanDayOutRapsNr = _ErpsSpanDayOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 13),
    _ErpsSpanDayOutRapsNr_Type()
)
erpsSpanDayOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsNr.setStatus("current")
_ErpsSpanDayOutRapsFs_Type = Counter32
_ErpsSpanDayOutRapsFs_Object = MibTableColumn
erpsSpanDayOutRapsFs = _ErpsSpanDayOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 14),
    _ErpsSpanDayOutRapsFs_Type()
)
erpsSpanDayOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsFs.setStatus("current")
_ErpsSpanDayOutRapsSf_Type = Counter32
_ErpsSpanDayOutRapsSf_Object = MibTableColumn
erpsSpanDayOutRapsSf = _ErpsSpanDayOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 15),
    _ErpsSpanDayOutRapsSf_Type()
)
erpsSpanDayOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsSf.setStatus("current")
_ErpsSpanDayOutRapsMs_Type = Counter32
_ErpsSpanDayOutRapsMs_Object = MibTableColumn
erpsSpanDayOutRapsMs = _ErpsSpanDayOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 16),
    _ErpsSpanDayOutRapsMs_Type()
)
erpsSpanDayOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsMs.setStatus("current")
_ErpsSpanDayOutRapsTotal_Type = Counter32
_ErpsSpanDayOutRapsTotal_Object = MibTableColumn
erpsSpanDayOutRapsTotal = _ErpsSpanDayOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 3, 1, 17),
    _ErpsSpanDayOutRapsTotal_Type()
)
erpsSpanDayOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanDayOutRapsTotal.setStatus("current")
_ErpsSpanCountersStatsTable_Object = MibTable
erpsSpanCountersStatsTable = _ErpsSpanCountersStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4)
)
if mibBuilder.loadTexts:
    erpsSpanCountersStatsTable.setStatus("current")
_ErpsSpanCountersStatsEntry_Object = MibTableRow
erpsSpanCountersStatsEntry = _ErpsSpanCountersStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1)
)
erpsSpanCountersStatsEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpanStatsIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpanStatsSpan"),
)
if mibBuilder.loadTexts:
    erpsSpanCountersStatsEntry.setStatus("current")
_ErpsSpanStatsIfIndex_Type = InterfaceIndex
_ErpsSpanStatsIfIndex_Object = MibTableColumn
erpsSpanStatsIfIndex = _ErpsSpanStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 1),
    _ErpsSpanStatsIfIndex_Type()
)
erpsSpanStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanStatsIfIndex.setStatus("current")
_ErpsSpanStatsSpan_Type = ErpsSpan
_ErpsSpanStatsSpan_Object = MibTableColumn
erpsSpanStatsSpan = _ErpsSpanStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 2),
    _ErpsSpanStatsSpan_Type()
)
erpsSpanStatsSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpanStatsSpan.setStatus("current")
_ErpsSpanStatsInRapsNrRb_Type = Counter32
_ErpsSpanStatsInRapsNrRb_Object = MibTableColumn
erpsSpanStatsInRapsNrRb = _ErpsSpanStatsInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 3),
    _ErpsSpanStatsInRapsNrRb_Type()
)
erpsSpanStatsInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsNrRb.setStatus("current")
_ErpsSpanStatsInRapsNrRbDnf_Type = Counter32
_ErpsSpanStatsInRapsNrRbDnf_Object = MibTableColumn
erpsSpanStatsInRapsNrRbDnf = _ErpsSpanStatsInRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 4),
    _ErpsSpanStatsInRapsNrRbDnf_Type()
)
erpsSpanStatsInRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsNrRbDnf.setStatus("current")
_ErpsSpanStatsInRapsNr_Type = Counter32
_ErpsSpanStatsInRapsNr_Object = MibTableColumn
erpsSpanStatsInRapsNr = _ErpsSpanStatsInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 5),
    _ErpsSpanStatsInRapsNr_Type()
)
erpsSpanStatsInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsNr.setStatus("current")
_ErpsSpanStatsInRapsFs_Type = Counter32
_ErpsSpanStatsInRapsFs_Object = MibTableColumn
erpsSpanStatsInRapsFs = _ErpsSpanStatsInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 6),
    _ErpsSpanStatsInRapsFs_Type()
)
erpsSpanStatsInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsFs.setStatus("current")
_ErpsSpanStatsInRapsSf_Type = Counter32
_ErpsSpanStatsInRapsSf_Object = MibTableColumn
erpsSpanStatsInRapsSf = _ErpsSpanStatsInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 7),
    _ErpsSpanStatsInRapsSf_Type()
)
erpsSpanStatsInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsSf.setStatus("current")
_ErpsSpanStatsInRapsMs_Type = Counter32
_ErpsSpanStatsInRapsMs_Object = MibTableColumn
erpsSpanStatsInRapsMs = _ErpsSpanStatsInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 8),
    _ErpsSpanStatsInRapsMs_Type()
)
erpsSpanStatsInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsMs.setStatus("current")
_ErpsSpanStatsInRapsIgnored_Type = Counter32
_ErpsSpanStatsInRapsIgnored_Object = MibTableColumn
erpsSpanStatsInRapsIgnored = _ErpsSpanStatsInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 9),
    _ErpsSpanStatsInRapsIgnored_Type()
)
erpsSpanStatsInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsIgnored.setStatus("current")
_ErpsSpanStatsInRapsTotal_Type = Counter32
_ErpsSpanStatsInRapsTotal_Object = MibTableColumn
erpsSpanStatsInRapsTotal = _ErpsSpanStatsInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 10),
    _ErpsSpanStatsInRapsTotal_Type()
)
erpsSpanStatsInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsInRapsTotal.setStatus("current")
_ErpsSpanStatsOutRapsNrRb_Type = Counter32
_ErpsSpanStatsOutRapsNrRb_Object = MibTableColumn
erpsSpanStatsOutRapsNrRb = _ErpsSpanStatsOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 11),
    _ErpsSpanStatsOutRapsNrRb_Type()
)
erpsSpanStatsOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsNrRb.setStatus("current")
_ErpsSpanStatsOutRapsNrRbDnf_Type = Counter32
_ErpsSpanStatsOutRapsNrRbDnf_Object = MibTableColumn
erpsSpanStatsOutRapsNrRbDnf = _ErpsSpanStatsOutRapsNrRbDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 12),
    _ErpsSpanStatsOutRapsNrRbDnf_Type()
)
erpsSpanStatsOutRapsNrRbDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsNrRbDnf.setStatus("current")
_ErpsSpanStatsOutRapsNr_Type = Counter32
_ErpsSpanStatsOutRapsNr_Object = MibTableColumn
erpsSpanStatsOutRapsNr = _ErpsSpanStatsOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 13),
    _ErpsSpanStatsOutRapsNr_Type()
)
erpsSpanStatsOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsNr.setStatus("current")
_ErpsSpanStatsOutRapsFs_Type = Counter32
_ErpsSpanStatsOutRapsFs_Object = MibTableColumn
erpsSpanStatsOutRapsFs = _ErpsSpanStatsOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 14),
    _ErpsSpanStatsOutRapsFs_Type()
)
erpsSpanStatsOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsFs.setStatus("current")
_ErpsSpanStatsOutRapsSf_Type = Counter32
_ErpsSpanStatsOutRapsSf_Object = MibTableColumn
erpsSpanStatsOutRapsSf = _ErpsSpanStatsOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 15),
    _ErpsSpanStatsOutRapsSf_Type()
)
erpsSpanStatsOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsSf.setStatus("current")
_ErpsSpanStatsOutRapsMs_Type = Counter32
_ErpsSpanStatsOutRapsMs_Object = MibTableColumn
erpsSpanStatsOutRapsMs = _ErpsSpanStatsOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 16),
    _ErpsSpanStatsOutRapsMs_Type()
)
erpsSpanStatsOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsMs.setStatus("current")
_ErpsSpanStatsOutRapsTotal_Type = Counter32
_ErpsSpanStatsOutRapsTotal_Object = MibTableColumn
erpsSpanStatsOutRapsTotal = _ErpsSpanStatsOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 4, 1, 17),
    _ErpsSpanStatsOutRapsTotal_Type()
)
erpsSpanStatsOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpanStatsOutRapsTotal.setStatus("current")
_ErpsSpanCounters24HrCurrentTable_Object = MibTable
erpsSpanCounters24HrCurrentTable = _ErpsSpanCounters24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5)
)
if mibBuilder.loadTexts:
    erpsSpanCounters24HrCurrentTable.setStatus("current")
_ErpsSpanCounters24HrCurrentEntry_Object = MibTableRow
erpsSpanCounters24HrCurrentEntry = _ErpsSpanCounters24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1)
)
erpsSpanCounters24HrCurrentEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpan24HrCurrentIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpan24HrCurrentSpan"),
)
if mibBuilder.loadTexts:
    erpsSpanCounters24HrCurrentEntry.setStatus("current")
_ErpsSpan24HrCurrentIfIndex_Type = InterfaceIndex
_ErpsSpan24HrCurrentIfIndex_Object = MibTableColumn
erpsSpan24HrCurrentIfIndex = _ErpsSpan24HrCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 1),
    _ErpsSpan24HrCurrentIfIndex_Type()
)
erpsSpan24HrCurrentIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentIfIndex.setStatus("current")
_ErpsSpan24HrCurrentSpan_Type = ErpsSpan
_ErpsSpan24HrCurrentSpan_Object = MibTableColumn
erpsSpan24HrCurrentSpan = _ErpsSpan24HrCurrentSpan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 2),
    _ErpsSpan24HrCurrentSpan_Type()
)
erpsSpan24HrCurrentSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentSpan.setStatus("current")
_ErpsSpan24HrCurrentInRapsNrRb_Type = Counter32
_ErpsSpan24HrCurrentInRapsNrRb_Object = MibTableColumn
erpsSpan24HrCurrentInRapsNrRb = _ErpsSpan24HrCurrentInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 3),
    _ErpsSpan24HrCurrentInRapsNrRb_Type()
)
erpsSpan24HrCurrentInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsNrRb.setStatus("current")
_ErpsSpan24HrCurrentInRapsDnf_Type = Counter32
_ErpsSpan24HrCurrentInRapsDnf_Object = MibTableColumn
erpsSpan24HrCurrentInRapsDnf = _ErpsSpan24HrCurrentInRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 4),
    _ErpsSpan24HrCurrentInRapsDnf_Type()
)
erpsSpan24HrCurrentInRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsDnf.setStatus("current")
_ErpsSpan24HrCurrentInRapsNr_Type = Counter32
_ErpsSpan24HrCurrentInRapsNr_Object = MibTableColumn
erpsSpan24HrCurrentInRapsNr = _ErpsSpan24HrCurrentInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 5),
    _ErpsSpan24HrCurrentInRapsNr_Type()
)
erpsSpan24HrCurrentInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsNr.setStatus("current")
_ErpsSpan24HrCurrentInRapsFs_Type = Counter32
_ErpsSpan24HrCurrentInRapsFs_Object = MibTableColumn
erpsSpan24HrCurrentInRapsFs = _ErpsSpan24HrCurrentInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 6),
    _ErpsSpan24HrCurrentInRapsFs_Type()
)
erpsSpan24HrCurrentInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsFs.setStatus("current")
_ErpsSpan24HrCurrentInRapsSf_Type = Counter32
_ErpsSpan24HrCurrentInRapsSf_Object = MibTableColumn
erpsSpan24HrCurrentInRapsSf = _ErpsSpan24HrCurrentInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 7),
    _ErpsSpan24HrCurrentInRapsSf_Type()
)
erpsSpan24HrCurrentInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsSf.setStatus("current")
_ErpsSpan24HrCurrentInRapsMs_Type = Counter32
_ErpsSpan24HrCurrentInRapsMs_Object = MibTableColumn
erpsSpan24HrCurrentInRapsMs = _ErpsSpan24HrCurrentInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 8),
    _ErpsSpan24HrCurrentInRapsMs_Type()
)
erpsSpan24HrCurrentInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsMs.setStatus("current")
_ErpsSpan24HrCurrentInRapsIgnored_Type = Counter32
_ErpsSpan24HrCurrentInRapsIgnored_Object = MibTableColumn
erpsSpan24HrCurrentInRapsIgnored = _ErpsSpan24HrCurrentInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 9),
    _ErpsSpan24HrCurrentInRapsIgnored_Type()
)
erpsSpan24HrCurrentInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsIgnored.setStatus("current")
_ErpsSpan24HrCurrentInRapsTotal_Type = Counter32
_ErpsSpan24HrCurrentInRapsTotal_Object = MibTableColumn
erpsSpan24HrCurrentInRapsTotal = _ErpsSpan24HrCurrentInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 10),
    _ErpsSpan24HrCurrentInRapsTotal_Type()
)
erpsSpan24HrCurrentInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentInRapsTotal.setStatus("current")
_ErpsSpan24HrCurrentOutRapsNrRb_Type = Counter32
_ErpsSpan24HrCurrentOutRapsNrRb_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsNrRb = _ErpsSpan24HrCurrentOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 11),
    _ErpsSpan24HrCurrentOutRapsNrRb_Type()
)
erpsSpan24HrCurrentOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsNrRb.setStatus("current")
_ErpsSpan24HrCurrentOutRapsDnf_Type = Counter32
_ErpsSpan24HrCurrentOutRapsDnf_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsDnf = _ErpsSpan24HrCurrentOutRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 12),
    _ErpsSpan24HrCurrentOutRapsDnf_Type()
)
erpsSpan24HrCurrentOutRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsDnf.setStatus("current")
_ErpsSpan24HrCurrentOutRapsNr_Type = Counter32
_ErpsSpan24HrCurrentOutRapsNr_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsNr = _ErpsSpan24HrCurrentOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 13),
    _ErpsSpan24HrCurrentOutRapsNr_Type()
)
erpsSpan24HrCurrentOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsNr.setStatus("current")
_ErpsSpan24HrCurrentOutRapsFs_Type = Counter32
_ErpsSpan24HrCurrentOutRapsFs_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsFs = _ErpsSpan24HrCurrentOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 14),
    _ErpsSpan24HrCurrentOutRapsFs_Type()
)
erpsSpan24HrCurrentOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsFs.setStatus("current")
_ErpsSpan24HrCurrentOutRapsSf_Type = Counter32
_ErpsSpan24HrCurrentOutRapsSf_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsSf = _ErpsSpan24HrCurrentOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 15),
    _ErpsSpan24HrCurrentOutRapsSf_Type()
)
erpsSpan24HrCurrentOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsSf.setStatus("current")
_ErpsSpan24HrCurrentOutRapsMs_Type = Counter32
_ErpsSpan24HrCurrentOutRapsMs_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsMs = _ErpsSpan24HrCurrentOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 16),
    _ErpsSpan24HrCurrentOutRapsMs_Type()
)
erpsSpan24HrCurrentOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsMs.setStatus("current")
_ErpsSpan24HrCurrentOutRapsTotal_Type = Counter32
_ErpsSpan24HrCurrentOutRapsTotal_Object = MibTableColumn
erpsSpan24HrCurrentOutRapsTotal = _ErpsSpan24HrCurrentOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 5, 1, 17),
    _ErpsSpan24HrCurrentOutRapsTotal_Type()
)
erpsSpan24HrCurrentOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrCurrentOutRapsTotal.setStatus("current")
_ErpsSpanCounters24HrIntervalTable_Object = MibTable
erpsSpanCounters24HrIntervalTable = _ErpsSpanCounters24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6)
)
if mibBuilder.loadTexts:
    erpsSpanCounters24HrIntervalTable.setStatus("current")
_ErpsSpanCounters24HrIntervalEntry_Object = MibTableRow
erpsSpanCounters24HrIntervalEntry = _ErpsSpanCounters24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1)
)
erpsSpanCounters24HrIntervalEntry.setIndexNames(
    (0, "ADTRAN-ERPS-MIB", "erpsSpan24HrIntervalIfIndex"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpan24HrIntervalSpan"),
    (0, "ADTRAN-ERPS-MIB", "erpsSpan24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    erpsSpanCounters24HrIntervalEntry.setStatus("current")
_ErpsSpan24HrIntervalIfIndex_Type = InterfaceIndex
_ErpsSpan24HrIntervalIfIndex_Object = MibTableColumn
erpsSpan24HrIntervalIfIndex = _ErpsSpan24HrIntervalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 1),
    _ErpsSpan24HrIntervalIfIndex_Type()
)
erpsSpan24HrIntervalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalIfIndex.setStatus("current")
_ErpsSpan24HrIntervalSpan_Type = ErpsSpan
_ErpsSpan24HrIntervalSpan_Object = MibTableColumn
erpsSpan24HrIntervalSpan = _ErpsSpan24HrIntervalSpan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 2),
    _ErpsSpan24HrIntervalSpan_Type()
)
erpsSpan24HrIntervalSpan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalSpan.setStatus("current")


class _ErpsSpan24HrIntervalNumber_Type(Unsigned32):
    """Custom type erpsSpan24HrIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_ErpsSpan24HrIntervalNumber_Type.__name__ = "Unsigned32"
_ErpsSpan24HrIntervalNumber_Object = MibTableColumn
erpsSpan24HrIntervalNumber = _ErpsSpan24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 3),
    _ErpsSpan24HrIntervalNumber_Type()
)
erpsSpan24HrIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalNumber.setStatus("current")
_ErpsSpan24HrIntervalValidData_Type = TruthValue
_ErpsSpan24HrIntervalValidData_Object = MibTableColumn
erpsSpan24HrIntervalValidData = _ErpsSpan24HrIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 4),
    _ErpsSpan24HrIntervalValidData_Type()
)
erpsSpan24HrIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalValidData.setStatus("current")
_ErpsSpan24HrIntervalTimeElapsed_Type = Unsigned32
_ErpsSpan24HrIntervalTimeElapsed_Object = MibTableColumn
erpsSpan24HrIntervalTimeElapsed = _ErpsSpan24HrIntervalTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 5),
    _ErpsSpan24HrIntervalTimeElapsed_Type()
)
erpsSpan24HrIntervalTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalTimeElapsed.setUnits("Seconds")
_ErpsSpan24HrIntervalStartTime_Type = DateAndTime
_ErpsSpan24HrIntervalStartTime_Object = MibTableColumn
erpsSpan24HrIntervalStartTime = _ErpsSpan24HrIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 6),
    _ErpsSpan24HrIntervalStartTime_Type()
)
erpsSpan24HrIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalStartTime.setStatus("current")
_ErpsSpan24HrIntervalInRapsNrRb_Type = Counter32
_ErpsSpan24HrIntervalInRapsNrRb_Object = MibTableColumn
erpsSpan24HrIntervalInRapsNrRb = _ErpsSpan24HrIntervalInRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 7),
    _ErpsSpan24HrIntervalInRapsNrRb_Type()
)
erpsSpan24HrIntervalInRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsNrRb.setStatus("current")
_ErpsSpan24HrIntervalInRapsDnf_Type = Counter32
_ErpsSpan24HrIntervalInRapsDnf_Object = MibTableColumn
erpsSpan24HrIntervalInRapsDnf = _ErpsSpan24HrIntervalInRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 8),
    _ErpsSpan24HrIntervalInRapsDnf_Type()
)
erpsSpan24HrIntervalInRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsDnf.setStatus("current")
_ErpsSpan24HrIntervalInRapsNr_Type = Counter32
_ErpsSpan24HrIntervalInRapsNr_Object = MibTableColumn
erpsSpan24HrIntervalInRapsNr = _ErpsSpan24HrIntervalInRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 9),
    _ErpsSpan24HrIntervalInRapsNr_Type()
)
erpsSpan24HrIntervalInRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsNr.setStatus("current")
_ErpsSpan24HrIntervalInRapsFs_Type = Counter32
_ErpsSpan24HrIntervalInRapsFs_Object = MibTableColumn
erpsSpan24HrIntervalInRapsFs = _ErpsSpan24HrIntervalInRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 10),
    _ErpsSpan24HrIntervalInRapsFs_Type()
)
erpsSpan24HrIntervalInRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsFs.setStatus("current")
_ErpsSpan24HrIntervalInRapsSf_Type = Counter32
_ErpsSpan24HrIntervalInRapsSf_Object = MibTableColumn
erpsSpan24HrIntervalInRapsSf = _ErpsSpan24HrIntervalInRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 11),
    _ErpsSpan24HrIntervalInRapsSf_Type()
)
erpsSpan24HrIntervalInRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsSf.setStatus("current")
_ErpsSpan24HrIntervalInRapsMs_Type = Counter32
_ErpsSpan24HrIntervalInRapsMs_Object = MibTableColumn
erpsSpan24HrIntervalInRapsMs = _ErpsSpan24HrIntervalInRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 12),
    _ErpsSpan24HrIntervalInRapsMs_Type()
)
erpsSpan24HrIntervalInRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsMs.setStatus("current")
_ErpsSpan24HrIntervalInRapsIgnored_Type = Counter32
_ErpsSpan24HrIntervalInRapsIgnored_Object = MibTableColumn
erpsSpan24HrIntervalInRapsIgnored = _ErpsSpan24HrIntervalInRapsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 13),
    _ErpsSpan24HrIntervalInRapsIgnored_Type()
)
erpsSpan24HrIntervalInRapsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsIgnored.setStatus("current")
_ErpsSpan24HrIntervalInRapsTotal_Type = Counter32
_ErpsSpan24HrIntervalInRapsTotal_Object = MibTableColumn
erpsSpan24HrIntervalInRapsTotal = _ErpsSpan24HrIntervalInRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 14),
    _ErpsSpan24HrIntervalInRapsTotal_Type()
)
erpsSpan24HrIntervalInRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalInRapsTotal.setStatus("current")
_ErpsSpan24HrIntervalOutRapsNrRb_Type = Counter32
_ErpsSpan24HrIntervalOutRapsNrRb_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsNrRb = _ErpsSpan24HrIntervalOutRapsNrRb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 15),
    _ErpsSpan24HrIntervalOutRapsNrRb_Type()
)
erpsSpan24HrIntervalOutRapsNrRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsNrRb.setStatus("current")
_ErpsSpan24HrIntervalOutRapsDnf_Type = Counter32
_ErpsSpan24HrIntervalOutRapsDnf_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsDnf = _ErpsSpan24HrIntervalOutRapsDnf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 16),
    _ErpsSpan24HrIntervalOutRapsDnf_Type()
)
erpsSpan24HrIntervalOutRapsDnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsDnf.setStatus("current")
_ErpsSpan24HrIntervalOutRapsNr_Type = Counter32
_ErpsSpan24HrIntervalOutRapsNr_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsNr = _ErpsSpan24HrIntervalOutRapsNr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 17),
    _ErpsSpan24HrIntervalOutRapsNr_Type()
)
erpsSpan24HrIntervalOutRapsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsNr.setStatus("current")
_ErpsSpan24HrIntervalOutRapsFs_Type = Counter32
_ErpsSpan24HrIntervalOutRapsFs_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsFs = _ErpsSpan24HrIntervalOutRapsFs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 18),
    _ErpsSpan24HrIntervalOutRapsFs_Type()
)
erpsSpan24HrIntervalOutRapsFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsFs.setStatus("current")
_ErpsSpan24HrIntervalOutRapsSf_Type = Counter32
_ErpsSpan24HrIntervalOutRapsSf_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsSf = _ErpsSpan24HrIntervalOutRapsSf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 19),
    _ErpsSpan24HrIntervalOutRapsSf_Type()
)
erpsSpan24HrIntervalOutRapsSf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsSf.setStatus("current")
_ErpsSpan24HrIntervalOutRapsMs_Type = Counter32
_ErpsSpan24HrIntervalOutRapsMs_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsMs = _ErpsSpan24HrIntervalOutRapsMs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 20),
    _ErpsSpan24HrIntervalOutRapsMs_Type()
)
erpsSpan24HrIntervalOutRapsMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsMs.setStatus("current")
_ErpsSpan24HrIntervalOutRapsTotal_Type = Counter32
_ErpsSpan24HrIntervalOutRapsTotal_Object = MibTableColumn
erpsSpan24HrIntervalOutRapsTotal = _ErpsSpan24HrIntervalOutRapsTotal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 4, 6, 1, 21),
    _ErpsSpan24HrIntervalOutRapsTotal_Type()
)
erpsSpan24HrIntervalOutRapsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsSpan24HrIntervalOutRapsTotal.setStatus("current")
_ErpsAllTraps_ObjectIdentity = ObjectIdentity
erpsAllTraps = _ErpsAllTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5)
)
_ErpsTraps_ObjectIdentity = ObjectIdentity
erpsTraps = _ErpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0)
)

# Managed Objects groups


# Notification objects

erpsAlarmDupRPLOwnerSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 1)
)
erpsAlarmDupRPLOwnerSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmDupRPLOwnerSet.setStatus(
        "current"
    )

erpsAlarmDupRPLOwnerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 2)
)
erpsAlarmDupRPLOwnerClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmDupRPLOwnerClear.setStatus(
        "current"
    )

erpsAlarmNoRPLOwnerSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 3)
)
erpsAlarmNoRPLOwnerSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoRPLOwnerSet.setStatus(
        "current"
    )

erpsAlarmNoRPLOwnerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 4)
)
erpsAlarmNoRPLOwnerClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoRPLOwnerClear.setStatus(
        "current"
    )

erpsAlarmDupHubSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 5)
)
erpsAlarmDupHubSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmDupHubSet.setStatus(
        "current"
    )

erpsAlarmDupHubClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 6)
)
erpsAlarmDupHubClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmDupHubClear.setStatus(
        "current"
    )

erpsAlarmNoHubSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 7)
)
erpsAlarmNoHubSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoHubSet.setStatus(
        "current"
    )

erpsAlarmNoHubClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 8)
)
erpsAlarmNoHubClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoHubClear.setStatus(
        "current"
    )

erpsAlarmMaxNodesExceededSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 9)
)
erpsAlarmMaxNodesExceededSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmMaxNodesExceededSet.setStatus(
        "current"
    )

erpsAlarmMaxNodesExceededClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 10)
)
erpsAlarmMaxNodesExceededClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmMaxNodesExceededClear.setStatus(
        "current"
    )

erpsAlarmWestMiswiredSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 11)
)
erpsAlarmWestMiswiredSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmWestMiswiredSet.setStatus(
        "current"
    )

erpsAlarmWestMiswiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 12)
)
erpsAlarmWestMiswiredClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmWestMiswiredClear.setStatus(
        "current"
    )

erpsAlarmEastMiswiredSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 13)
)
erpsAlarmEastMiswiredSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmEastMiswiredSet.setStatus(
        "current"
    )

erpsAlarmEastMiswiredClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 14)
)
erpsAlarmEastMiswiredClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmEastMiswiredClear.setStatus(
        "current"
    )

erpsAlarmTopoInconsistentSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 15)
)
erpsAlarmTopoInconsistentSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmTopoInconsistentSet.setStatus(
        "current"
    )

erpsAlarmTopoInconsistentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 16)
)
erpsAlarmTopoInconsistentClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmTopoInconsistentClear.setStatus(
        "current"
    )

erpsAlarmWestEdgeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 17)
)
erpsAlarmWestEdgeSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmWestEdgeSet.setStatus(
        "current"
    )

erpsAlarmWestEdgeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 18)
)
erpsAlarmWestEdgeClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmWestEdgeClear.setStatus(
        "current"
    )

erpsAlarmEastEdgeSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 19)
)
erpsAlarmEastEdgeSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmEastEdgeSet.setStatus(
        "current"
    )

erpsAlarmEastEdgeClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 20)
)
erpsAlarmEastEdgeClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmEastEdgeClear.setStatus(
        "current"
    )

erpsAlarmNoNeighborWestSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 21)
)
erpsAlarmNoNeighborWestSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoNeighborWestSet.setStatus(
        "current"
    )

erpsAlarmNoNeighborWestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 22)
)
erpsAlarmNoNeighborWestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoNeighborWestClear.setStatus(
        "current"
    )

erpsAlarmNoNeighborEastSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 23)
)
erpsAlarmNoNeighborEastSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoNeighborEastSet.setStatus(
        "current"
    )

erpsAlarmNoNeighborEastClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 24)
)
erpsAlarmNoNeighborEastClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmNoNeighborEastClear.setStatus(
        "current"
    )

erpsAlarmRingIncompleteSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 25)
)
erpsAlarmRingIncompleteSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmRingIncompleteSet.setStatus(
        "current"
    )

erpsAlarmRingIncompleteClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 26)
)
erpsAlarmRingIncompleteClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmRingIncompleteClear.setStatus(
        "current"
    )

erpsAlarmVlanMisconfigSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 27)
)
erpsAlarmVlanMisconfigSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmVlanMisconfigSet.setStatus(
        "current"
    )

erpsAlarmVlanMisconfigClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 28)
)
erpsAlarmVlanMisconfigClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmVlanMisconfigClear.setStatus(
        "current"
    )

erpsAlarmConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 29)
)
erpsAlarmConfigurationChange.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmConfigurationChange.setStatus(
        "current"
    )

erpsAlarmTopoRateInconsistentSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 30)
)
erpsAlarmTopoRateInconsistentSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmTopoRateInconsistentSet.setStatus(
        "current"
    )

erpsAlarmTopoRateInconsistentClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 79, 1, 5, 0, 31)
)
erpsAlarmTopoRateInconsistentClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("ADTRAN-ERPS-MIB", "erpsIfStationName"),
        ("ADTRAN-ERPS-MIB", "erpsIfUuid"),
        ("ADTRAN-ERPS-MIB", "erpsIfIndex"))
)
if mibBuilder.loadTexts:
    erpsAlarmTopoRateInconsistentClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ERPS-MIB",
    **{"ErpsSpan": ErpsSpan,
       "ErpsProtectionStatus": ErpsProtectionStatus,
       "ErpsRingTopoProtectionStatus": ErpsRingTopoProtectionStatus,
       "erpsGeneral": erpsGeneral,
       "erpsIfTable": erpsIfTable,
       "erpsIfEntry": erpsIfEntry,
       "erpsIfIndex": erpsIfIndex,
       "erpsIfStationId": erpsIfStationId,
       "erpsIfStationName": erpsIfStationName,
       "erpsIfProtectionWTR": erpsIfProtectionWTR,
       "erpsIfGuardTimer": erpsIfGuardTimer,
       "erpsIfMessageTimer": erpsIfMessageTimer,
       "erpsIfMessageTimerRunning": erpsIfMessageTimerRunning,
       "erpsIfRplOwner": erpsIfRplOwner,
       "erpsIfRplLink": erpsIfRplLink,
       "erpsIfEnabled": erpsIfEnabled,
       "erpsIfWtrRunning": erpsIfWtrRunning,
       "erpsIfWtrRemaining": erpsIfWtrRemaining,
       "erpsIfWestIfIndex": erpsIfWestIfIndex,
       "erpsIfEastIfIndex": erpsIfEastIfIndex,
       "erpsIfProtectState": erpsIfProtectState,
       "erpsIfLastChange": erpsIfLastChange,
       "erpsIfChanges": erpsIfChanges,
       "erpsIfStationsOnRing": erpsIfStationsOnRing,
       "erpsIfIsRingClosed": erpsIfIsRingClosed,
       "erpsTopoIfCurrentStatus": erpsTopoIfCurrentStatus,
       "erpsTopoIfLastChange": erpsTopoIfLastChange,
       "erpsTopoIfChanges": erpsTopoIfChanges,
       "erpsIfControlStag": erpsIfControlStag,
       "erpsIfTransportStag": erpsIfTransportStag,
       "erpsIfVlanMisconfig": erpsIfVlanMisconfig,
       "erpsIfStationIp": erpsIfStationIp,
       "erpsIfUuid": erpsIfUuid,
       "erpsIfConfigTrapEnable": erpsIfConfigTrapEnable,
       "erpsIfTopologyEnable": erpsIfTopologyEnable,
       "erpsIfRapsVirtualChannel": erpsIfRapsVirtualChannel,
       "erpsIfLastError": erpsIfLastError,
       "erpsIfRowStatus": erpsIfRowStatus,
       "erpsIfTopologyRate": erpsIfTopologyRate,
       "erpsIfRateMiscnfEnable": erpsIfRateMiscnfEnable,
       "erpsIfStatsControlTable": erpsIfStatsControlTable,
       "erpsIfStatsControlEntry": erpsIfStatsControlEntry,
       "erpsIfStatsControlIfIndex": erpsIfStatsControlIfIndex,
       "erpsIfStatsControlPeriodClear": erpsIfStatsControlPeriodClear,
       "erpsIfStatsControlCountPointClear": erpsIfStatsControlCountPointClear,
       "erpsIfStatsControlIntervalClear": erpsIfStatsControlIntervalClear,
       "erpsIfStatsControlCommitClear": erpsIfStatsControlCommitClear,
       "erpsIfStatsControlTimeElapsed": erpsIfStatsControlTimeElapsed,
       "erpsIfStatsControlValidIntervals": erpsIfStatsControlValidIntervals,
       "erpsSpanTable": erpsSpanTable,
       "erpsSpanEntry": erpsSpanEntry,
       "erpsSpanIfIndex": erpsSpanIfIndex,
       "erpsSpanId": erpsSpanId,
       "erpsSpanProtectionCommand": erpsSpanProtectionCommand,
       "erpsSpanStatus": erpsSpanStatus,
       "erpsSpanForwardingStatus": erpsSpanForwardingStatus,
       "erpsSpanCurrentStatus": erpsSpanCurrentStatus,
       "erpsSpanLastChange": erpsSpanLastChange,
       "erpsSpanChanges": erpsSpanChanges,
       "erpsUuidMapTable": erpsUuidMapTable,
       "erpsUuidMapEntry": erpsUuidMapEntry,
       "erpsUuidMapUuid": erpsUuidMapUuid,
       "erpsUuidMapRingIfIndex": erpsUuidMapRingIfIndex,
       "erpsIfChangeSummaryObject": erpsIfChangeSummaryObject,
       "erpsIfChangeSummaryNumInterfaces": erpsIfChangeSummaryNumInterfaces,
       "erpsIfChangeSummaryIfLastChange": erpsIfChangeSummaryIfLastChange,
       "erpsIfChangeSummaryIfChanges": erpsIfChangeSummaryIfChanges,
       "erpsIfChangeSummarySpanLastChange": erpsIfChangeSummarySpanLastChange,
       "erpsIfChangeSummarySpanChanges": erpsIfChangeSummarySpanChanges,
       "erpsIfLastCreateErrorTable": erpsIfLastCreateErrorTable,
       "erpsIfLastCreateErrorEntry": erpsIfLastCreateErrorEntry,
       "erpsIfLastCreateError": erpsIfLastCreateError,
       "erpsProtocol": erpsProtocol,
       "erpsRingTopoTable": erpsRingTopoTable,
       "erpsRingTopoEntry": erpsRingTopoEntry,
       "erpsRingTopoIndex": erpsRingTopoIndex,
       "erpsRingTopoStationId": erpsRingTopoStationId,
       "erpsRingTopoStationName": erpsRingTopoStationName,
       "erpsRingTopoStationFlags": erpsRingTopoStationFlags,
       "erpsRingTopoMacAddress": erpsRingTopoMacAddress,
       "erpsRingTopoWestStationId": erpsRingTopoWestStationId,
       "erpsRingTopoEastStationId": erpsRingTopoEastStationId,
       "erpsRingTopoWestNeighborMacAddress": erpsRingTopoWestNeighborMacAddress,
       "erpsRingTopoEastNeighborMacAddress": erpsRingTopoEastNeighborMacAddress,
       "erpsRingTopoWestProtectionStatus": erpsRingTopoWestProtectionStatus,
       "erpsRingTopoEastProtectionStatus": erpsRingTopoEastProtectionStatus,
       "erpsRingTopoLastChange": erpsRingTopoLastChange,
       "erpsRingTopoChanges": erpsRingTopoChanges,
       "erpsRingTopoStationIp": erpsRingTopoStationIp,
       "erpsRingTopoWestStationIp": erpsRingTopoWestStationIp,
       "erpsRingTopoEastStationIp": erpsRingTopoEastStationIp,
       "erpsRingTopoMacTable": erpsRingTopoMacTable,
       "erpsRingTopoMacEntry": erpsRingTopoMacEntry,
       "erpsRingTopoMacIndex": erpsRingTopoMacIndex,
       "erpsRingTopoMacMacAddress": erpsRingTopoMacMacAddress,
       "erpsRingTopoMacStationId": erpsRingTopoMacStationId,
       "erpsRingTopoMacStationName": erpsRingTopoMacStationName,
       "erpsRingTopoMacStationFlags": erpsRingTopoMacStationFlags,
       "erpsRingTopoMacWestStationId": erpsRingTopoMacWestStationId,
       "erpsRingTopoMacEastStationId": erpsRingTopoMacEastStationId,
       "erpsRingTopoMacWestNeighborMacAddress": erpsRingTopoMacWestNeighborMacAddress,
       "erpsRingTopoMacEastNeighborMacAddress": erpsRingTopoMacEastNeighborMacAddress,
       "erpsRingTopoMacWestProtectionStatus": erpsRingTopoMacWestProtectionStatus,
       "erpsRingTopoMacEastProtectionStatus": erpsRingTopoMacEastProtectionStatus,
       "erpsRingTopoMacLastChange": erpsRingTopoMacLastChange,
       "erpsRingTopoMacChanges": erpsRingTopoMacChanges,
       "erpsRingTopoMacStationIp": erpsRingTopoMacStationIp,
       "erpsRingTopoMacWestStationIp": erpsRingTopoMacWestStationIp,
       "erpsRingTopoMacEastStationIp": erpsRingTopoMacEastStationIp,
       "erpsCounters": erpsCounters,
       "erpsCountersCurrentTable": erpsCountersCurrentTable,
       "erpsCountersCurrentEntry": erpsCountersCurrentEntry,
       "erpsCurrentIfIndex": erpsCurrentIfIndex,
       "erpsCurrentInRapsNrRb": erpsCurrentInRapsNrRb,
       "erpsCurrentInRapsNrRbDnf": erpsCurrentInRapsNrRbDnf,
       "erpsCurrentInRapsNr": erpsCurrentInRapsNr,
       "erpsCurrentInRapsFs": erpsCurrentInRapsFs,
       "erpsCurrentInRapsSf": erpsCurrentInRapsSf,
       "erpsCurrentInRapsMs": erpsCurrentInRapsMs,
       "erpsCurrentInRapsIgnored": erpsCurrentInRapsIgnored,
       "erpsCurrentInRapsTotal": erpsCurrentInRapsTotal,
       "erpsCurrentOutRapsNrRb": erpsCurrentOutRapsNrRb,
       "erpsCurrentOutRapsNrRbDnf": erpsCurrentOutRapsNrRbDnf,
       "erpsCurrentOutRapsNr": erpsCurrentOutRapsNr,
       "erpsCurrentOutRapsFs": erpsCurrentOutRapsFs,
       "erpsCurrentOutRapsSf": erpsCurrentOutRapsSf,
       "erpsCurrentOutRapsMs": erpsCurrentOutRapsMs,
       "erpsCurrentOutRapsTotal": erpsCurrentOutRapsTotal,
       "erpsCurrentProtectionSwitches": erpsCurrentProtectionSwitches,
       "erpsCountersIntervalTable": erpsCountersIntervalTable,
       "erpsCountersIntervalEntry": erpsCountersIntervalEntry,
       "erpsIntervalIfIndex": erpsIntervalIfIndex,
       "erpsIntervalNumber": erpsIntervalNumber,
       "erpsIntervalValidData": erpsIntervalValidData,
       "erpsIntervalTimeElapsed": erpsIntervalTimeElapsed,
       "erpsIntervalStartTime": erpsIntervalStartTime,
       "erpsIntervalInRapsNrRb": erpsIntervalInRapsNrRb,
       "erpsIntervalInRapsNrRbDnf": erpsIntervalInRapsNrRbDnf,
       "erpsIntervalInRapsNr": erpsIntervalInRapsNr,
       "erpsIntervalInRapsFs": erpsIntervalInRapsFs,
       "erpsIntervalInRapsSf": erpsIntervalInRapsSf,
       "erpsIntervalInRapsMs": erpsIntervalInRapsMs,
       "erpsIntervalInRapsIgnored": erpsIntervalInRapsIgnored,
       "erpsIntervalInRapsTotal": erpsIntervalInRapsTotal,
       "erpsIntervalOutRapsNrRb": erpsIntervalOutRapsNrRb,
       "erpsIntervalOutRapsNrRbDnf": erpsIntervalOutRapsNrRbDnf,
       "erpsIntervalOutRapsNr": erpsIntervalOutRapsNr,
       "erpsIntervalOutRapsFs": erpsIntervalOutRapsFs,
       "erpsIntervalOutRapsSf": erpsIntervalOutRapsSf,
       "erpsIntervalOutRapsMs": erpsIntervalOutRapsMs,
       "erpsIntervalOutRapsTotal": erpsIntervalOutRapsTotal,
       "erpsIntervalProtectionSwitches": erpsIntervalProtectionSwitches,
       "erpsCountersDayTable": erpsCountersDayTable,
       "erpsCountersDayEntry": erpsCountersDayEntry,
       "erpsDayIfIndex": erpsDayIfIndex,
       "erpsDayInRapsNrRb": erpsDayInRapsNrRb,
       "erpsDayInRapsNrRbDnf": erpsDayInRapsNrRbDnf,
       "erpsDayInRapsNr": erpsDayInRapsNr,
       "erpsDayInRapsFs": erpsDayInRapsFs,
       "erpsDayInRapsSf": erpsDayInRapsSf,
       "erpsDayInRapsMs": erpsDayInRapsMs,
       "erpsDayInRapsIgnored": erpsDayInRapsIgnored,
       "erpsDayInRapsTotal": erpsDayInRapsTotal,
       "erpsDayOutRapsNrRb": erpsDayOutRapsNrRb,
       "erpsDayOutRapsNrRbDnf": erpsDayOutRapsNrRbDnf,
       "erpsDayOutRapsNr": erpsDayOutRapsNr,
       "erpsDayOutRapsFs": erpsDayOutRapsFs,
       "erpsDayOutRapsSf": erpsDayOutRapsSf,
       "erpsDayOutRapsMs": erpsDayOutRapsMs,
       "erpsDayOutRapsTotal": erpsDayOutRapsTotal,
       "erpsDayProtectionSwitches": erpsDayProtectionSwitches,
       "erpsCountersStatsTable": erpsCountersStatsTable,
       "erpsCountersStatsEntry": erpsCountersStatsEntry,
       "erpsStatsIfIndex": erpsStatsIfIndex,
       "erpsStatsInRapsNrRb": erpsStatsInRapsNrRb,
       "erpsStatsInRapsNrRbDnf": erpsStatsInRapsNrRbDnf,
       "erpsStatsInRapsNr": erpsStatsInRapsNr,
       "erpsStatsInRapsFs": erpsStatsInRapsFs,
       "erpsStatsInRapsSf": erpsStatsInRapsSf,
       "erpsStatsInRapsMs": erpsStatsInRapsMs,
       "erpsStatsInRapsIgnored": erpsStatsInRapsIgnored,
       "erpsStatsInRapsTotal": erpsStatsInRapsTotal,
       "erpsStatsOutRapsNrRb": erpsStatsOutRapsNrRb,
       "erpsStatsOutRapsNrRbDnf": erpsStatsOutRapsNrRbDnf,
       "erpsStatsOutRapsNr": erpsStatsOutRapsNr,
       "erpsStatsOutRapsFs": erpsStatsOutRapsFs,
       "erpsStatsOutRapsSf": erpsStatsOutRapsSf,
       "erpsStatsOutRapsMs": erpsStatsOutRapsMs,
       "erpsStatsOutRapsTotal": erpsStatsOutRapsTotal,
       "erpsStatsProtectionSwitches": erpsStatsProtectionSwitches,
       "erpsCounters24HrCurrentTable": erpsCounters24HrCurrentTable,
       "erpsCounters24HrCurrentEntry": erpsCounters24HrCurrentEntry,
       "erps24HrCurrentIfIndex": erps24HrCurrentIfIndex,
       "erps24HrCurrentInRapsNrRb": erps24HrCurrentInRapsNrRb,
       "erps24HrCurrentInRapsDnf": erps24HrCurrentInRapsDnf,
       "erps24HrCurrentInRapsNr": erps24HrCurrentInRapsNr,
       "erps24HrCurrentInRapsFs": erps24HrCurrentInRapsFs,
       "erps24HrCurrentInRapsSf": erps24HrCurrentInRapsSf,
       "erps24HrCurrentInRapsMs": erps24HrCurrentInRapsMs,
       "erps24HrCurrentInRapsIgnored": erps24HrCurrentInRapsIgnored,
       "erps24HrCurrentInRapsTotal": erps24HrCurrentInRapsTotal,
       "erps24HrCurrentOutRapsNrRb": erps24HrCurrentOutRapsNrRb,
       "erps24HrCurrentOutRapsDnf": erps24HrCurrentOutRapsDnf,
       "erps24HrCurrentOutRapsNr": erps24HrCurrentOutRapsNr,
       "erps24HrCurrentOutRapsFs": erps24HrCurrentOutRapsFs,
       "erps24HrCurrentOutRapsSf": erps24HrCurrentOutRapsSf,
       "erps24HrCurrentOutRapsMs": erps24HrCurrentOutRapsMs,
       "erps24HrCurrentOutRapsTotal": erps24HrCurrentOutRapsTotal,
       "erps24HrCurrentProtectionSwitches": erps24HrCurrentProtectionSwitches,
       "erpsCounters24HrIntervalTable": erpsCounters24HrIntervalTable,
       "erpsCounters24HrIntervalEntry": erpsCounters24HrIntervalEntry,
       "erps24HrIntervalIfIndex": erps24HrIntervalIfIndex,
       "erps24HrIntervalNumber": erps24HrIntervalNumber,
       "erps24HrIntervalValidData": erps24HrIntervalValidData,
       "erps24HrIntervalTimeElapsed": erps24HrIntervalTimeElapsed,
       "erps24HrIntervalStartTime": erps24HrIntervalStartTime,
       "erps24HrIntervalInRapsNrRb": erps24HrIntervalInRapsNrRb,
       "erps24HrIntervalInRapsDnf": erps24HrIntervalInRapsDnf,
       "erps24HrIntervalInRapsNr": erps24HrIntervalInRapsNr,
       "erps24HrIntervalInRapsFs": erps24HrIntervalInRapsFs,
       "erps24HrIntervalInRapsSf": erps24HrIntervalInRapsSf,
       "erps24HrIntervalInRapsMs": erps24HrIntervalInRapsMs,
       "erps24HrIntervalInRapsIgnored": erps24HrIntervalInRapsIgnored,
       "erps24HrIntervalInRapsTotal": erps24HrIntervalInRapsTotal,
       "erps24HrIntervalOutRapsNrRb": erps24HrIntervalOutRapsNrRb,
       "erps24HrIntervalOutRapsDnf": erps24HrIntervalOutRapsDnf,
       "erps24HrIntervalOutRapsNr": erps24HrIntervalOutRapsNr,
       "erps24HrIntervalOutRapsFs": erps24HrIntervalOutRapsFs,
       "erps24HrIntervalOutRapsSf": erps24HrIntervalOutRapsSf,
       "erps24HrIntervalOutRapsMs": erps24HrIntervalOutRapsMs,
       "erps24HrIntervalOutRapsTotal": erps24HrIntervalOutRapsTotal,
       "erps24HrIntervalProtectionSwitches": erps24HrIntervalProtectionSwitches,
       "erpsSpanCounters": erpsSpanCounters,
       "erpsSpanCountersCurrentTable": erpsSpanCountersCurrentTable,
       "erpsSpanCountersCurrentEntry": erpsSpanCountersCurrentEntry,
       "erpsSpanCurrentIfIndex": erpsSpanCurrentIfIndex,
       "erpsSpanCurrentSpan": erpsSpanCurrentSpan,
       "erpsSpanCurrentInRapsNrRb": erpsSpanCurrentInRapsNrRb,
       "erpsSpanCurrentInRapsNrRbDnf": erpsSpanCurrentInRapsNrRbDnf,
       "erpsSpanCurrentInRapsNr": erpsSpanCurrentInRapsNr,
       "erpsSpanCurrentInRapsFs": erpsSpanCurrentInRapsFs,
       "erpsSpanCurrentInRapsSf": erpsSpanCurrentInRapsSf,
       "erpsSpanCurrentInRapsMs": erpsSpanCurrentInRapsMs,
       "erpsSpanCurrentInRapsIgnored": erpsSpanCurrentInRapsIgnored,
       "erpsSpanCurrentInRapsTotal": erpsSpanCurrentInRapsTotal,
       "erpsSpanCurrentOutRapsNrRb": erpsSpanCurrentOutRapsNrRb,
       "erpsSpanCurrentOutRapsNrRbDnf": erpsSpanCurrentOutRapsNrRbDnf,
       "erpsSpanCurrentOutRapsNr": erpsSpanCurrentOutRapsNr,
       "erpsSpanCurrentOutRapsFs": erpsSpanCurrentOutRapsFs,
       "erpsSpanCurrentOutRapsSf": erpsSpanCurrentOutRapsSf,
       "erpsSpanCurrentOutRapsMs": erpsSpanCurrentOutRapsMs,
       "erpsSpanCurrentOutRapsTotal": erpsSpanCurrentOutRapsTotal,
       "erpsSpanCountersIntervalTable": erpsSpanCountersIntervalTable,
       "erpsSpanCountersIntervalEntry": erpsSpanCountersIntervalEntry,
       "erpsSpanIntervalIfIndex": erpsSpanIntervalIfIndex,
       "erpsSpanIntervalSpan": erpsSpanIntervalSpan,
       "erpsSpanIntervalNumber": erpsSpanIntervalNumber,
       "erpsSpanIntervalValidData": erpsSpanIntervalValidData,
       "erpsSpanIntervalTimeElapsed": erpsSpanIntervalTimeElapsed,
       "erpsSpanIntervalStartTime": erpsSpanIntervalStartTime,
       "erpsSpanIntervalInRapsNrRb": erpsSpanIntervalInRapsNrRb,
       "erpsSpanIntervalInRapsNrRbDnf": erpsSpanIntervalInRapsNrRbDnf,
       "erpsSpanIntervalInRapsNr": erpsSpanIntervalInRapsNr,
       "erpsSpanIntervalInRapsFs": erpsSpanIntervalInRapsFs,
       "erpsSpanIntervalInRapsSf": erpsSpanIntervalInRapsSf,
       "erpsSpanIntervalInRapsMs": erpsSpanIntervalInRapsMs,
       "erpsSpanIntervalInRapsIgnored": erpsSpanIntervalInRapsIgnored,
       "erpsSpanIntervalInRapsTotal": erpsSpanIntervalInRapsTotal,
       "erpsSpanIntervalOutRapsNrRb": erpsSpanIntervalOutRapsNrRb,
       "erpsSpanIntervalOutRapsNrRbDnf": erpsSpanIntervalOutRapsNrRbDnf,
       "erpsSpanIntervalOutRapsNr": erpsSpanIntervalOutRapsNr,
       "erpsSpanIntervalOutRapsFs": erpsSpanIntervalOutRapsFs,
       "erpsSpanIntervalOutRapsSf": erpsSpanIntervalOutRapsSf,
       "erpsSpanIntervalOutRapsMs": erpsSpanIntervalOutRapsMs,
       "erpsSpanIntervalOutRapsTotal": erpsSpanIntervalOutRapsTotal,
       "erpsSpanCountersDayTable": erpsSpanCountersDayTable,
       "erpsSpanCountersDayEntry": erpsSpanCountersDayEntry,
       "erpsSpanDayIfIndex": erpsSpanDayIfIndex,
       "erpsSpanDaySpan": erpsSpanDaySpan,
       "erpsSpanDayInRapsNrRb": erpsSpanDayInRapsNrRb,
       "erpsSpanDayInRapsNrRbDnf": erpsSpanDayInRapsNrRbDnf,
       "erpsSpanDayInRapsNr": erpsSpanDayInRapsNr,
       "erpsSpanDayInRapsFs": erpsSpanDayInRapsFs,
       "erpsSpanDayInRapsSf": erpsSpanDayInRapsSf,
       "erpsSpanDayInRapsMs": erpsSpanDayInRapsMs,
       "erpsSpanDayInRapsIgnored": erpsSpanDayInRapsIgnored,
       "erpsSpanDayInRapsTotal": erpsSpanDayInRapsTotal,
       "erpsSpanDayOutRapsNrRb": erpsSpanDayOutRapsNrRb,
       "erpsSpanDayOutRapsNrRbDnf": erpsSpanDayOutRapsNrRbDnf,
       "erpsSpanDayOutRapsNr": erpsSpanDayOutRapsNr,
       "erpsSpanDayOutRapsFs": erpsSpanDayOutRapsFs,
       "erpsSpanDayOutRapsSf": erpsSpanDayOutRapsSf,
       "erpsSpanDayOutRapsMs": erpsSpanDayOutRapsMs,
       "erpsSpanDayOutRapsTotal": erpsSpanDayOutRapsTotal,
       "erpsSpanCountersStatsTable": erpsSpanCountersStatsTable,
       "erpsSpanCountersStatsEntry": erpsSpanCountersStatsEntry,
       "erpsSpanStatsIfIndex": erpsSpanStatsIfIndex,
       "erpsSpanStatsSpan": erpsSpanStatsSpan,
       "erpsSpanStatsInRapsNrRb": erpsSpanStatsInRapsNrRb,
       "erpsSpanStatsInRapsNrRbDnf": erpsSpanStatsInRapsNrRbDnf,
       "erpsSpanStatsInRapsNr": erpsSpanStatsInRapsNr,
       "erpsSpanStatsInRapsFs": erpsSpanStatsInRapsFs,
       "erpsSpanStatsInRapsSf": erpsSpanStatsInRapsSf,
       "erpsSpanStatsInRapsMs": erpsSpanStatsInRapsMs,
       "erpsSpanStatsInRapsIgnored": erpsSpanStatsInRapsIgnored,
       "erpsSpanStatsInRapsTotal": erpsSpanStatsInRapsTotal,
       "erpsSpanStatsOutRapsNrRb": erpsSpanStatsOutRapsNrRb,
       "erpsSpanStatsOutRapsNrRbDnf": erpsSpanStatsOutRapsNrRbDnf,
       "erpsSpanStatsOutRapsNr": erpsSpanStatsOutRapsNr,
       "erpsSpanStatsOutRapsFs": erpsSpanStatsOutRapsFs,
       "erpsSpanStatsOutRapsSf": erpsSpanStatsOutRapsSf,
       "erpsSpanStatsOutRapsMs": erpsSpanStatsOutRapsMs,
       "erpsSpanStatsOutRapsTotal": erpsSpanStatsOutRapsTotal,
       "erpsSpanCounters24HrCurrentTable": erpsSpanCounters24HrCurrentTable,
       "erpsSpanCounters24HrCurrentEntry": erpsSpanCounters24HrCurrentEntry,
       "erpsSpan24HrCurrentIfIndex": erpsSpan24HrCurrentIfIndex,
       "erpsSpan24HrCurrentSpan": erpsSpan24HrCurrentSpan,
       "erpsSpan24HrCurrentInRapsNrRb": erpsSpan24HrCurrentInRapsNrRb,
       "erpsSpan24HrCurrentInRapsDnf": erpsSpan24HrCurrentInRapsDnf,
       "erpsSpan24HrCurrentInRapsNr": erpsSpan24HrCurrentInRapsNr,
       "erpsSpan24HrCurrentInRapsFs": erpsSpan24HrCurrentInRapsFs,
       "erpsSpan24HrCurrentInRapsSf": erpsSpan24HrCurrentInRapsSf,
       "erpsSpan24HrCurrentInRapsMs": erpsSpan24HrCurrentInRapsMs,
       "erpsSpan24HrCurrentInRapsIgnored": erpsSpan24HrCurrentInRapsIgnored,
       "erpsSpan24HrCurrentInRapsTotal": erpsSpan24HrCurrentInRapsTotal,
       "erpsSpan24HrCurrentOutRapsNrRb": erpsSpan24HrCurrentOutRapsNrRb,
       "erpsSpan24HrCurrentOutRapsDnf": erpsSpan24HrCurrentOutRapsDnf,
       "erpsSpan24HrCurrentOutRapsNr": erpsSpan24HrCurrentOutRapsNr,
       "erpsSpan24HrCurrentOutRapsFs": erpsSpan24HrCurrentOutRapsFs,
       "erpsSpan24HrCurrentOutRapsSf": erpsSpan24HrCurrentOutRapsSf,
       "erpsSpan24HrCurrentOutRapsMs": erpsSpan24HrCurrentOutRapsMs,
       "erpsSpan24HrCurrentOutRapsTotal": erpsSpan24HrCurrentOutRapsTotal,
       "erpsSpanCounters24HrIntervalTable": erpsSpanCounters24HrIntervalTable,
       "erpsSpanCounters24HrIntervalEntry": erpsSpanCounters24HrIntervalEntry,
       "erpsSpan24HrIntervalIfIndex": erpsSpan24HrIntervalIfIndex,
       "erpsSpan24HrIntervalSpan": erpsSpan24HrIntervalSpan,
       "erpsSpan24HrIntervalNumber": erpsSpan24HrIntervalNumber,
       "erpsSpan24HrIntervalValidData": erpsSpan24HrIntervalValidData,
       "erpsSpan24HrIntervalTimeElapsed": erpsSpan24HrIntervalTimeElapsed,
       "erpsSpan24HrIntervalStartTime": erpsSpan24HrIntervalStartTime,
       "erpsSpan24HrIntervalInRapsNrRb": erpsSpan24HrIntervalInRapsNrRb,
       "erpsSpan24HrIntervalInRapsDnf": erpsSpan24HrIntervalInRapsDnf,
       "erpsSpan24HrIntervalInRapsNr": erpsSpan24HrIntervalInRapsNr,
       "erpsSpan24HrIntervalInRapsFs": erpsSpan24HrIntervalInRapsFs,
       "erpsSpan24HrIntervalInRapsSf": erpsSpan24HrIntervalInRapsSf,
       "erpsSpan24HrIntervalInRapsMs": erpsSpan24HrIntervalInRapsMs,
       "erpsSpan24HrIntervalInRapsIgnored": erpsSpan24HrIntervalInRapsIgnored,
       "erpsSpan24HrIntervalInRapsTotal": erpsSpan24HrIntervalInRapsTotal,
       "erpsSpan24HrIntervalOutRapsNrRb": erpsSpan24HrIntervalOutRapsNrRb,
       "erpsSpan24HrIntervalOutRapsDnf": erpsSpan24HrIntervalOutRapsDnf,
       "erpsSpan24HrIntervalOutRapsNr": erpsSpan24HrIntervalOutRapsNr,
       "erpsSpan24HrIntervalOutRapsFs": erpsSpan24HrIntervalOutRapsFs,
       "erpsSpan24HrIntervalOutRapsSf": erpsSpan24HrIntervalOutRapsSf,
       "erpsSpan24HrIntervalOutRapsMs": erpsSpan24HrIntervalOutRapsMs,
       "erpsSpan24HrIntervalOutRapsTotal": erpsSpan24HrIntervalOutRapsTotal,
       "erpsAllTraps": erpsAllTraps,
       "erpsTraps": erpsTraps,
       "erpsAlarmDupRPLOwnerSet": erpsAlarmDupRPLOwnerSet,
       "erpsAlarmDupRPLOwnerClear": erpsAlarmDupRPLOwnerClear,
       "erpsAlarmNoRPLOwnerSet": erpsAlarmNoRPLOwnerSet,
       "erpsAlarmNoRPLOwnerClear": erpsAlarmNoRPLOwnerClear,
       "erpsAlarmDupHubSet": erpsAlarmDupHubSet,
       "erpsAlarmDupHubClear": erpsAlarmDupHubClear,
       "erpsAlarmNoHubSet": erpsAlarmNoHubSet,
       "erpsAlarmNoHubClear": erpsAlarmNoHubClear,
       "erpsAlarmMaxNodesExceededSet": erpsAlarmMaxNodesExceededSet,
       "erpsAlarmMaxNodesExceededClear": erpsAlarmMaxNodesExceededClear,
       "erpsAlarmWestMiswiredSet": erpsAlarmWestMiswiredSet,
       "erpsAlarmWestMiswiredClear": erpsAlarmWestMiswiredClear,
       "erpsAlarmEastMiswiredSet": erpsAlarmEastMiswiredSet,
       "erpsAlarmEastMiswiredClear": erpsAlarmEastMiswiredClear,
       "erpsAlarmTopoInconsistentSet": erpsAlarmTopoInconsistentSet,
       "erpsAlarmTopoInconsistentClear": erpsAlarmTopoInconsistentClear,
       "erpsAlarmWestEdgeSet": erpsAlarmWestEdgeSet,
       "erpsAlarmWestEdgeClear": erpsAlarmWestEdgeClear,
       "erpsAlarmEastEdgeSet": erpsAlarmEastEdgeSet,
       "erpsAlarmEastEdgeClear": erpsAlarmEastEdgeClear,
       "erpsAlarmNoNeighborWestSet": erpsAlarmNoNeighborWestSet,
       "erpsAlarmNoNeighborWestClear": erpsAlarmNoNeighborWestClear,
       "erpsAlarmNoNeighborEastSet": erpsAlarmNoNeighborEastSet,
       "erpsAlarmNoNeighborEastClear": erpsAlarmNoNeighborEastClear,
       "erpsAlarmRingIncompleteSet": erpsAlarmRingIncompleteSet,
       "erpsAlarmRingIncompleteClear": erpsAlarmRingIncompleteClear,
       "erpsAlarmVlanMisconfigSet": erpsAlarmVlanMisconfigSet,
       "erpsAlarmVlanMisconfigClear": erpsAlarmVlanMisconfigClear,
       "erpsAlarmConfigurationChange": erpsAlarmConfigurationChange,
       "erpsAlarmTopoRateInconsistentSet": erpsAlarmTopoRateInconsistentSet,
       "erpsAlarmTopoRateInconsistentClear": erpsAlarmTopoRateInconsistentClear,
       "adErpsMIB": adErpsMIB}
)
