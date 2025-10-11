# SNMP MIB module (SL-FC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-FC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:32:05 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fcBxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliSeconds(TextualConvention, Unsigned32):
    status = "current"


class MicroSeconds(TextualConvention, Unsigned32):
    status = "current"


class FcNameId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class FcAddressId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class FcRxDataFieldSize(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 2112),
    )



class FcBbCredit(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )



class FcphVersion(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class FcStackedConnMode(TextualConvention, Integer32):
    status = "current"
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
          ("transparent", 2),
          ("lockedDown", 3))
    )



class FcCosCap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("classF", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5),
          ("class6", 6))
    )


class FcBxPortCapacity(TextualConvention, Unsigned32):
    status = "current"


class FcBxPortIndex(TextualConvention, Unsigned32):
    status = "current"


class FcExPortIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )



class FcBbCreditModel(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("alternate", 2))
    )



class FcPortSpeed(TextualConvention, Integer32):
    status = "current"
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
        *(("auto", 1),
          ("eighthGbs", 2),
          ("quarterGbs", 3),
          ("halfGbs", 4),
          ("oneGbs", 5),
          ("twoGbs", 6),
          ("fourGbs", 7),
          ("tenGbs", 8))
    )



# MIB Managed Objects in the order of their OIDs

_FcBxMIBObjects_ObjectIdentity = ObjectIdentity
fcBxMIBObjects = _FcBxMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1)
)
_FcBxConfig_ObjectIdentity = ObjectIdentity
fcBxConfig = _FcBxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1)
)
_FcBxPortTable_Object = MibTable
fcBxPortTable = _FcBxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fcBxPortTable.setStatus("current")
_FcBxPortEntry_Object = MibTableRow
fcBxPortEntry = _FcBxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1)
)
fcBxPortEntry.setIndexNames(
    (0, "SL-FC-MIB", "fcBxPortIndex"),
)
if mibBuilder.loadTexts:
    fcBxPortEntry.setStatus("current")
_FcBxPortIndex_Type = FcBxPortIndex
_FcBxPortIndex_Object = MibTableColumn
fcBxPortIndex = _FcBxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 1),
    _FcBxPortIndex_Type()
)
fcBxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIndex.setStatus("current")
_FcBxPortName_Type = FcNameId
_FcBxPortName_Object = MibTableColumn
fcBxPortName = _FcBxPortName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 2),
    _FcBxPortName_Type()
)
fcBxPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortName.setStatus("current")
_FcBxPortFcphVersionHigh_Type = FcphVersion
_FcBxPortFcphVersionHigh_Object = MibTableColumn
fcBxPortFcphVersionHigh = _FcBxPortFcphVersionHigh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 3),
    _FcBxPortFcphVersionHigh_Type()
)
fcBxPortFcphVersionHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortFcphVersionHigh.setStatus("current")
_FcBxPortFcphVersionLow_Type = FcphVersion
_FcBxPortFcphVersionLow_Object = MibTableColumn
fcBxPortFcphVersionLow = _FcBxPortFcphVersionLow_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 4),
    _FcBxPortFcphVersionLow_Type()
)
fcBxPortFcphVersionLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortFcphVersionLow.setStatus("current")
_FcBxPortBbCredit_Type = FcBbCredit
_FcBxPortBbCredit_Object = MibTableColumn
fcBxPortBbCredit = _FcBxPortBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 5),
    _FcBxPortBbCredit_Type()
)
fcBxPortBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortBbCredit.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortBbCredit.setUnits("buffers")
_FcBxPortRxBufSize_Type = FcRxDataFieldSize
_FcBxPortRxBufSize_Object = MibTableColumn
fcBxPortRxBufSize = _FcBxPortRxBufSize_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 6),
    _FcBxPortRxBufSize_Type()
)
fcBxPortRxBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortRxBufSize.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortRxBufSize.setUnits("bytes")
_FcBxPortRatov_Type = MilliSeconds
_FcBxPortRatov_Object = MibTableColumn
fcBxPortRatov = _FcBxPortRatov_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 7),
    _FcBxPortRatov_Type()
)
fcBxPortRatov.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortRatov.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortRatov.setUnits("milliseconds")
_FcBxPortEdtov_Type = MilliSeconds
_FcBxPortEdtov_Object = MibTableColumn
fcBxPortEdtov = _FcBxPortEdtov_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 8),
    _FcBxPortEdtov_Type()
)
fcBxPortEdtov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortEdtov.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortEdtov.setUnits("milliseconds")
_FcBxPortCosSupported_Type = FcCosCap
_FcBxPortCosSupported_Object = MibTableColumn
fcBxPortCosSupported = _FcBxPortCosSupported_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 9),
    _FcBxPortCosSupported_Type()
)
fcBxPortCosSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCosSupported.setStatus("current")
_FcBxPortClass2SeqDeliv_Type = TruthValue
_FcBxPortClass2SeqDeliv_Object = MibTableColumn
fcBxPortClass2SeqDeliv = _FcBxPortClass2SeqDeliv_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 10),
    _FcBxPortClass2SeqDeliv_Type()
)
fcBxPortClass2SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortClass2SeqDeliv.setStatus("current")
_FcBxPortClass3SeqDeliv_Type = TruthValue
_FcBxPortClass3SeqDeliv_Object = MibTableColumn
fcBxPortClass3SeqDeliv = _FcBxPortClass3SeqDeliv_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 11),
    _FcBxPortClass3SeqDeliv_Type()
)
fcBxPortClass3SeqDeliv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortClass3SeqDeliv.setStatus("current")
_FcBxPortHoldTime_Type = MicroSeconds
_FcBxPortHoldTime_Object = MibTableColumn
fcBxPortHoldTime = _FcBxPortHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 14),
    _FcBxPortHoldTime_Type()
)
fcBxPortHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortHoldTime.setUnits("microseconds")
_FcBxPortFabricName_Type = FcNameId
_FcBxPortFabricName_Object = MibTableColumn
fcBxPortFabricName = _FcBxPortFabricName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 15),
    _FcBxPortFabricName_Type()
)
fcBxPortFabricName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortFabricName.setStatus("current")
_FcBxPortPhysRttov_Type = MilliSeconds
_FcBxPortPhysRttov_Object = MibTableColumn
fcBxPortPhysRttov = _FcBxPortPhysRttov_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 16),
    _FcBxPortPhysRttov_Type()
)
fcBxPortPhysRttov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortPhysRttov.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortPhysRttov.setUnits("milliseconds")


class _FcBxPortTranceiverMedia_Type(Integer32):
    """Custom type fcBxPortTranceiverMedia based on Integer32"""
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
          ("sm", 2),
          ("mm", 3))
    )


_FcBxPortTranceiverMedia_Type.__name__ = "Integer32"
_FcBxPortTranceiverMedia_Object = MibTableColumn
fcBxPortTranceiverMedia = _FcBxPortTranceiverMedia_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 17),
    _FcBxPortTranceiverMedia_Type()
)
fcBxPortTranceiverMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTranceiverMedia.setStatus("current")
_FcBxPortPauseTimeout_Type = MilliSeconds
_FcBxPortPauseTimeout_Object = MibTableColumn
fcBxPortPauseTimeout = _FcBxPortPauseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 18),
    _FcBxPortPauseTimeout_Type()
)
fcBxPortPauseTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortPauseTimeout.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortPauseTimeout.setUnits("milliseconds")
_FcBxPortBbThresholdRx_Type = FcBbCredit
_FcBxPortBbThresholdRx_Object = MibTableColumn
fcBxPortBbThresholdRx = _FcBxPortBbThresholdRx_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 19),
    _FcBxPortBbThresholdRx_Type()
)
fcBxPortBbThresholdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortBbThresholdRx.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortBbThresholdRx.setUnits("buffers")
_FcBxPortBbThresholdTx_Type = FcBbCredit
_FcBxPortBbThresholdTx_Object = MibTableColumn
fcBxPortBbThresholdTx = _FcBxPortBbThresholdTx_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 20),
    _FcBxPortBbThresholdTx_Type()
)
fcBxPortBbThresholdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortBbThresholdTx.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortBbThresholdTx.setUnits("buffers")
_FcBxPortResetPmCounters_Type = Integer32
_FcBxPortResetPmCounters_Object = MibTableColumn
fcBxPortResetPmCounters = _FcBxPortResetPmCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 21),
    _FcBxPortResetPmCounters_Type()
)
fcBxPortResetPmCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortResetPmCounters.setStatus("current")


class _FcBxPortTranceiverType_Type(Integer32):
    """Custom type fcBxPortTranceiverType based on Integer32"""
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
          ("shortWave", 2),
          ("longWave", 3))
    )


_FcBxPortTranceiverType_Type.__name__ = "Integer32"
_FcBxPortTranceiverType_Object = MibTableColumn
fcBxPortTranceiverType = _FcBxPortTranceiverType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 22),
    _FcBxPortTranceiverType_Type()
)
fcBxPortTranceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTranceiverType.setStatus("current")
_FcBxPortWwnTransparent_Type = TruthValue
_FcBxPortWwnTransparent_Object = MibTableColumn
fcBxPortWwnTransparent = _FcBxPortWwnTransparent_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 23),
    _FcBxPortWwnTransparent_Type()
)
fcBxPortWwnTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortWwnTransparent.setStatus("current")
_FcBxPortAdminSpeed_Type = FcPortSpeed
_FcBxPortAdminSpeed_Object = MibTableColumn
fcBxPortAdminSpeed = _FcBxPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 24),
    _FcBxPortAdminSpeed_Type()
)
fcBxPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortAdminSpeed.setStatus("current")
_FcBxPortRestartLink_Type = TruthValue
_FcBxPortRestartLink_Object = MibTableColumn
fcBxPortRestartLink = _FcBxPortRestartLink_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 25),
    _FcBxPortRestartLink_Type()
)
fcBxPortRestartLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortRestartLink.setStatus("current")
_FcBxPortTransceiverRate_Type = Integer32
_FcBxPortTransceiverRate_Object = MibTableColumn
fcBxPortTransceiverRate = _FcBxPortTransceiverRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 26),
    _FcBxPortTransceiverRate_Type()
)
fcBxPortTransceiverRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTransceiverRate.setStatus("current")
_FcBxPortElpInitiator_Type = Integer32
_FcBxPortElpInitiator_Object = MibTableColumn
fcBxPortElpInitiator = _FcBxPortElpInitiator_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 27),
    _FcBxPortElpInitiator_Type()
)
fcBxPortElpInitiator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortElpInitiator.setStatus("current")
_FcBxPortRemoteSwitchFabricName_Type = FcNameId
_FcBxPortRemoteSwitchFabricName_Object = MibTableColumn
fcBxPortRemoteSwitchFabricName = _FcBxPortRemoteSwitchFabricName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 28),
    _FcBxPortRemoteSwitchFabricName_Type()
)
fcBxPortRemoteSwitchFabricName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortRemoteSwitchFabricName.setStatus("current")
_FcBxPortRemoteSwitchPortName_Type = FcNameId
_FcBxPortRemoteSwitchPortName_Object = MibTableColumn
fcBxPortRemoteSwitchPortName = _FcBxPortRemoteSwitchPortName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 1, 1, 1, 29),
    _FcBxPortRemoteSwitchPortName_Type()
)
fcBxPortRemoteSwitchPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcBxPortRemoteSwitchPortName.setStatus("current")
_FcBxStatus_ObjectIdentity = ObjectIdentity
fcBxStatus = _FcBxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2)
)
_FcBxPortStatusTable_Object = MibTable
fcBxPortStatusTable = _FcBxPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fcBxPortStatusTable.setStatus("current")
_FcBxPortStatusEntry_Object = MibTableRow
fcBxPortStatusEntry = _FcBxPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fcBxPortStatusEntry.setStatus("current")
_FcBxPortBbRxBufferAvailable_Type = Gauge32
_FcBxPortBbRxBufferAvailable_Object = MibTableColumn
fcBxPortBbRxBufferAvailable = _FcBxPortBbRxBufferAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1, 1),
    _FcBxPortBbRxBufferAvailable_Type()
)
fcBxPortBbRxBufferAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortBbRxBufferAvailable.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortBbRxBufferAvailable.setUnits("buffers")
_FcBxPortBbTxBufferAvailable_Type = Gauge32
_FcBxPortBbTxBufferAvailable_Object = MibTableColumn
fcBxPortBbTxBufferAvailable = _FcBxPortBbTxBufferAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1, 2),
    _FcBxPortBbTxBufferAvailable_Type()
)
fcBxPortBbTxBufferAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortBbTxBufferAvailable.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortBbTxBufferAvailable.setUnits("buffers")


class _FcBxPortStatus_Type(Integer32):
    """Custom type fcBxPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FcBxPortStatus_Type.__name__ = "Integer32"
_FcBxPortStatus_Object = MibTableColumn
fcBxPortStatus = _FcBxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1, 3),
    _FcBxPortStatus_Type()
)
fcBxPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortStatus.setStatus("current")


class _FcBxPortStatusValidIntervals_Type(Integer32):
    """Custom type fcBxPortStatusValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_FcBxPortStatusValidIntervals_Type.__name__ = "Integer32"
_FcBxPortStatusValidIntervals_Object = MibTableColumn
fcBxPortStatusValidIntervals = _FcBxPortStatusValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1, 4),
    _FcBxPortStatusValidIntervals_Type()
)
fcBxPortStatusValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortStatusValidIntervals.setStatus("current")


class _FcBxPortStatusLoginState_Type(Bits):
    """Custom type fcBxPortStatusLoginState based on Bits"""
    namedValues = NamedValues(
        *(("signalSense", 0),
          ("syncPort", 1),
          ("validLogin", 2))
    )

_FcBxPortStatusLoginState_Type.__name__ = "Bits"
_FcBxPortStatusLoginState_Object = MibTableColumn
fcBxPortStatusLoginState = _FcBxPortStatusLoginState_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1, 5),
    _FcBxPortStatusLoginState_Type()
)
fcBxPortStatusLoginState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortStatusLoginState.setStatus("current")


class _FcBxPortStatusAttachedPortType_Type(Integer32):
    """Custom type fcBxPortStatusAttachedPortType based on Integer32"""
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
        *(("nPort", 1),
          ("fPort", 2),
          ("ePort", 3),
          ("tPort", 4))
    )


_FcBxPortStatusAttachedPortType_Type.__name__ = "Integer32"
_FcBxPortStatusAttachedPortType_Object = MibTableColumn
fcBxPortStatusAttachedPortType = _FcBxPortStatusAttachedPortType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 1, 1, 6),
    _FcBxPortStatusAttachedPortType_Type()
)
fcBxPortStatusAttachedPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortStatusAttachedPortType.setStatus("current")
_FcBxLoginTable_Object = MibTable
fcBxLoginTable = _FcBxLoginTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fcBxLoginTable.setStatus("current")
_FcBxLoginEntry_Object = MibTableRow
fcBxLoginEntry = _FcBxLoginEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fcBxLoginEntry.setStatus("current")


class _FcBxPortVersionAgreed_Type(Integer32):
    """Custom type fcBxPortVersionAgreed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FcBxPortVersionAgreed_Type.__name__ = "Integer32"
_FcBxPortVersionAgreed_Object = MibTableColumn
fcBxPortVersionAgreed = _FcBxPortVersionAgreed_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 1),
    _FcBxPortVersionAgreed_Type()
)
fcBxPortVersionAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortVersionAgreed.setStatus("current")
_FcBxPortExPortBbCredit_Type = FcBbCredit
_FcBxPortExPortBbCredit_Object = MibTableColumn
fcBxPortExPortBbCredit = _FcBxPortExPortBbCredit_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 2),
    _FcBxPortExPortBbCredit_Type()
)
fcBxPortExPortBbCredit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortExPortBbCredit.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortExPortBbCredit.setUnits("buffers")
_FcBxPortExPortRxDataFieldSize_Type = FcRxDataFieldSize
_FcBxPortExPortRxDataFieldSize_Object = MibTableColumn
fcBxPortExPortRxDataFieldSize = _FcBxPortExPortRxDataFieldSize_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 3),
    _FcBxPortExPortRxDataFieldSize_Type()
)
fcBxPortExPortRxDataFieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortExPortRxDataFieldSize.setStatus("current")
if mibBuilder.loadTexts:
    fcBxPortExPortRxDataFieldSize.setUnits("bytes")
_FcBxPortCosSuppAgreed_Type = FcCosCap
_FcBxPortCosSuppAgreed_Object = MibTableColumn
fcBxPortCosSuppAgreed = _FcBxPortCosSuppAgreed_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 4),
    _FcBxPortCosSuppAgreed_Type()
)
fcBxPortCosSuppAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCosSuppAgreed.setStatus("current")
_FcBxPortClass2SeqDelivAgreed_Type = TruthValue
_FcBxPortClass2SeqDelivAgreed_Object = MibTableColumn
fcBxPortClass2SeqDelivAgreed = _FcBxPortClass2SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 5),
    _FcBxPortClass2SeqDelivAgreed_Type()
)
fcBxPortClass2SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortClass2SeqDelivAgreed.setStatus("current")
_FcBxPortClass3SeqDelivAgreed_Type = TruthValue
_FcBxPortClass3SeqDelivAgreed_Object = MibTableColumn
fcBxPortClass3SeqDelivAgreed = _FcBxPortClass3SeqDelivAgreed_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 6),
    _FcBxPortClass3SeqDelivAgreed_Type()
)
fcBxPortClass3SeqDelivAgreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortClass3SeqDelivAgreed.setStatus("current")
_FcBxPortExPortName_Type = FcNameId
_FcBxPortExPortName_Object = MibTableColumn
fcBxPortExPortName = _FcBxPortExPortName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 7),
    _FcBxPortExPortName_Type()
)
fcBxPortExPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortExPortName.setStatus("current")
_FcBxPortBbCreditModel_Type = FcBbCreditModel
_FcBxPortBbCreditModel_Object = MibTableColumn
fcBxPortBbCreditModel = _FcBxPortBbCreditModel_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 8),
    _FcBxPortBbCreditModel_Type()
)
fcBxPortBbCreditModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortBbCreditModel.setStatus("current")
_FcBxPortExFabricName_Type = FcNameId
_FcBxPortExFabricName_Object = MibTableColumn
fcBxPortExFabricName = _FcBxPortExFabricName_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 2, 3, 1, 9),
    _FcBxPortExFabricName_Type()
)
fcBxPortExFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortExFabricName.setStatus("current")
_FcBxPm_ObjectIdentity = ObjectIdentity
fcBxPm = _FcBxPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3)
)
_FcBxPortCurrentTable_Object = MibTable
fcBxPortCurrentTable = _FcBxPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fcBxPortCurrentTable.setStatus("current")
_FcBxPortCurrentEntry_Object = MibTableRow
fcBxPortCurrentEntry = _FcBxPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1)
)
fcBxPortCurrentEntry.setIndexNames(
    (0, "SL-FC-MIB", "fcBxPortCurrentIndex"),
)
if mibBuilder.loadTexts:
    fcBxPortCurrentEntry.setStatus("current")
_FcBxPortCurrentIndex_Type = InterfaceIndex
_FcBxPortCurrentIndex_Object = MibTableColumn
fcBxPortCurrentIndex = _FcBxPortCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 1),
    _FcBxPortCurrentIndex_Type()
)
fcBxPortCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentIndex.setStatus("current")
_FcBxPortCurrentLinkFailures_Type = Counter64
_FcBxPortCurrentLinkFailures_Object = MibTableColumn
fcBxPortCurrentLinkFailures = _FcBxPortCurrentLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 2),
    _FcBxPortCurrentLinkFailures_Type()
)
fcBxPortCurrentLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentLinkFailures.setStatus("current")
_FcBxPortCurrentSyncLosses_Type = Counter64
_FcBxPortCurrentSyncLosses_Object = MibTableColumn
fcBxPortCurrentSyncLosses = _FcBxPortCurrentSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 3),
    _FcBxPortCurrentSyncLosses_Type()
)
fcBxPortCurrentSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentSyncLosses.setStatus("current")
_FcBxPortCurrentSigLosses_Type = Counter64
_FcBxPortCurrentSigLosses_Object = MibTableColumn
fcBxPortCurrentSigLosses = _FcBxPortCurrentSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 4),
    _FcBxPortCurrentSigLosses_Type()
)
fcBxPortCurrentSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentSigLosses.setStatus("current")
_FcBxPortCurrentPrimSeqProtoErrors_Type = Counter64
_FcBxPortCurrentPrimSeqProtoErrors_Object = MibTableColumn
fcBxPortCurrentPrimSeqProtoErrors = _FcBxPortCurrentPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 5),
    _FcBxPortCurrentPrimSeqProtoErrors_Type()
)
fcBxPortCurrentPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentPrimSeqProtoErrors.setStatus("current")
_FcBxPortCurrentInvalidTxWords_Type = Counter64
_FcBxPortCurrentInvalidTxWords_Object = MibTableColumn
fcBxPortCurrentInvalidTxWords = _FcBxPortCurrentInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 6),
    _FcBxPortCurrentInvalidTxWords_Type()
)
fcBxPortCurrentInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentInvalidTxWords.setStatus("current")
_FcBxPortCurrentInvalidCrcs_Type = Counter64
_FcBxPortCurrentInvalidCrcs_Object = MibTableColumn
fcBxPortCurrentInvalidCrcs = _FcBxPortCurrentInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 7),
    _FcBxPortCurrentInvalidCrcs_Type()
)
fcBxPortCurrentInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentInvalidCrcs.setStatus("current")
_FcBxPortCurrentDelimiterErrors_Type = Counter64
_FcBxPortCurrentDelimiterErrors_Object = MibTableColumn
fcBxPortCurrentDelimiterErrors = _FcBxPortCurrentDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 8),
    _FcBxPortCurrentDelimiterErrors_Type()
)
fcBxPortCurrentDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentDelimiterErrors.setStatus("current")
_FcBxPortCurrentRxFlowControl_Type = Counter64
_FcBxPortCurrentRxFlowControl_Object = MibTableColumn
fcBxPortCurrentRxFlowControl = _FcBxPortCurrentRxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 9),
    _FcBxPortCurrentRxFlowControl_Type()
)
fcBxPortCurrentRxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxFlowControl.setStatus("current")
_FcBxPortCurrentTxFlowControl_Type = Counter64
_FcBxPortCurrentTxFlowControl_Object = MibTableColumn
fcBxPortCurrentTxFlowControl = _FcBxPortCurrentTxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 10),
    _FcBxPortCurrentTxFlowControl_Type()
)
fcBxPortCurrentTxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxFlowControl.setStatus("current")
_FcBxPortCurrentRxOctets_Type = Counter64
_FcBxPortCurrentRxOctets_Object = MibTableColumn
fcBxPortCurrentRxOctets = _FcBxPortCurrentRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 11),
    _FcBxPortCurrentRxOctets_Type()
)
fcBxPortCurrentRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxOctets.setStatus("current")
_FcBxPortCurrentRxPkts_Type = Counter64
_FcBxPortCurrentRxPkts_Object = MibTableColumn
fcBxPortCurrentRxPkts = _FcBxPortCurrentRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 12),
    _FcBxPortCurrentRxPkts_Type()
)
fcBxPortCurrentRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxPkts.setStatus("current")
_FcBxPortCurrentTxOctets_Type = Counter64
_FcBxPortCurrentTxOctets_Object = MibTableColumn
fcBxPortCurrentTxOctets = _FcBxPortCurrentTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 13),
    _FcBxPortCurrentTxOctets_Type()
)
fcBxPortCurrentTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxOctets.setStatus("current")
_FcBxPortCurrentTxPkts_Type = Counter64
_FcBxPortCurrentTxPkts_Object = MibTableColumn
fcBxPortCurrentTxPkts = _FcBxPortCurrentTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 14),
    _FcBxPortCurrentTxPkts_Type()
)
fcBxPortCurrentTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxPkts.setStatus("current")
_FcBxPortCurrentRxLinkReset_Type = Counter64
_FcBxPortCurrentRxLinkReset_Object = MibTableColumn
fcBxPortCurrentRxLinkReset = _FcBxPortCurrentRxLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 15),
    _FcBxPortCurrentRxLinkReset_Type()
)
fcBxPortCurrentRxLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxLinkReset.setStatus("current")
_FcBxPortCurrentTxLinkReset_Type = Counter64
_FcBxPortCurrentTxLinkReset_Object = MibTableColumn
fcBxPortCurrentTxLinkReset = _FcBxPortCurrentTxLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 16),
    _FcBxPortCurrentTxLinkReset_Type()
)
fcBxPortCurrentTxLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxLinkReset.setStatus("current")
_FcBxPortCurrentRxOls_Type = Counter64
_FcBxPortCurrentRxOls_Object = MibTableColumn
fcBxPortCurrentRxOls = _FcBxPortCurrentRxOls_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 17),
    _FcBxPortCurrentRxOls_Type()
)
fcBxPortCurrentRxOls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxOls.setStatus("current")
_FcBxPortCurrentTxOls_Type = Counter64
_FcBxPortCurrentTxOls_Object = MibTableColumn
fcBxPortCurrentTxOls = _FcBxPortCurrentTxOls_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 18),
    _FcBxPortCurrentTxOls_Type()
)
fcBxPortCurrentTxOls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxOls.setStatus("current")
_FcBxPortCurrentRxErroredBbwHeaders_Type = Counter64
_FcBxPortCurrentRxErroredBbwHeaders_Object = MibTableColumn
fcBxPortCurrentRxErroredBbwHeaders = _FcBxPortCurrentRxErroredBbwHeaders_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 19),
    _FcBxPortCurrentRxErroredBbwHeaders_Type()
)
fcBxPortCurrentRxErroredBbwHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxErroredBbwHeaders.setStatus("current")
_FcBxPortCurrentRxC2FramesDiscarded_Type = Counter64
_FcBxPortCurrentRxC2FramesDiscarded_Object = MibTableColumn
fcBxPortCurrentRxC2FramesDiscarded = _FcBxPortCurrentRxC2FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 20),
    _FcBxPortCurrentRxC2FramesDiscarded_Type()
)
fcBxPortCurrentRxC2FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC2FramesDiscarded.setStatus("current")
_FcBxPortCurrentTxC2Octets_Type = Counter64
_FcBxPortCurrentTxC2Octets_Object = MibTableColumn
fcBxPortCurrentTxC2Octets = _FcBxPortCurrentTxC2Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 21),
    _FcBxPortCurrentTxC2Octets_Type()
)
fcBxPortCurrentTxC2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxC2Octets.setStatus("current")
_FcBxPortCurrentTxC2Packets_Type = Counter64
_FcBxPortCurrentTxC2Packets_Object = MibTableColumn
fcBxPortCurrentTxC2Packets = _FcBxPortCurrentTxC2Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 22),
    _FcBxPortCurrentTxC2Packets_Type()
)
fcBxPortCurrentTxC2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxC2Packets.setStatus("current")
_FcBxPortCurrentRxC2Octets_Type = Counter64
_FcBxPortCurrentRxC2Octets_Object = MibTableColumn
fcBxPortCurrentRxC2Octets = _FcBxPortCurrentRxC2Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 23),
    _FcBxPortCurrentRxC2Octets_Type()
)
fcBxPortCurrentRxC2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC2Octets.setStatus("current")
_FcBxPortCurrentRxC2Packets_Type = Counter64
_FcBxPortCurrentRxC2Packets_Object = MibTableColumn
fcBxPortCurrentRxC2Packets = _FcBxPortCurrentRxC2Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 24),
    _FcBxPortCurrentRxC2Packets_Type()
)
fcBxPortCurrentRxC2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC2Packets.setStatus("current")
_FcBxPortCurrentRxC2ErroredSizeFrames_Type = Counter64
_FcBxPortCurrentRxC2ErroredSizeFrames_Object = MibTableColumn
fcBxPortCurrentRxC2ErroredSizeFrames = _FcBxPortCurrentRxC2ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 25),
    _FcBxPortCurrentRxC2ErroredSizeFrames_Type()
)
fcBxPortCurrentRxC2ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC2ErroredSizeFrames.setStatus("current")
_FcBxPortCurrentRxC3FramesDiscarded_Type = Counter64
_FcBxPortCurrentRxC3FramesDiscarded_Object = MibTableColumn
fcBxPortCurrentRxC3FramesDiscarded = _FcBxPortCurrentRxC3FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 26),
    _FcBxPortCurrentRxC3FramesDiscarded_Type()
)
fcBxPortCurrentRxC3FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC3FramesDiscarded.setStatus("current")
_FcBxPortCurrentTxC3Octets_Type = Counter64
_FcBxPortCurrentTxC3Octets_Object = MibTableColumn
fcBxPortCurrentTxC3Octets = _FcBxPortCurrentTxC3Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 27),
    _FcBxPortCurrentTxC3Octets_Type()
)
fcBxPortCurrentTxC3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxC3Octets.setStatus("current")
_FcBxPortCurrentTxC3Packets_Type = Counter64
_FcBxPortCurrentTxC3Packets_Object = MibTableColumn
fcBxPortCurrentTxC3Packets = _FcBxPortCurrentTxC3Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 28),
    _FcBxPortCurrentTxC3Packets_Type()
)
fcBxPortCurrentTxC3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxC3Packets.setStatus("current")
_FcBxPortCurrentRxC3Octets_Type = Counter64
_FcBxPortCurrentRxC3Octets_Object = MibTableColumn
fcBxPortCurrentRxC3Octets = _FcBxPortCurrentRxC3Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 29),
    _FcBxPortCurrentRxC3Octets_Type()
)
fcBxPortCurrentRxC3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC3Octets.setStatus("current")
_FcBxPortCurrentRxC3Packets_Type = Counter64
_FcBxPortCurrentRxC3Packets_Object = MibTableColumn
fcBxPortCurrentRxC3Packets = _FcBxPortCurrentRxC3Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 30),
    _FcBxPortCurrentRxC3Packets_Type()
)
fcBxPortCurrentRxC3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC3Packets.setStatus("current")
_FcBxPortCurrentRxC3ErroredSizeFrames_Type = Counter64
_FcBxPortCurrentRxC3ErroredSizeFrames_Object = MibTableColumn
fcBxPortCurrentRxC3ErroredSizeFrames = _FcBxPortCurrentRxC3ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 31),
    _FcBxPortCurrentRxC3ErroredSizeFrames_Type()
)
fcBxPortCurrentRxC3ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC3ErroredSizeFrames.setStatus("current")
_FcBxPortCurrentTxC4Octets_Type = Counter64
_FcBxPortCurrentTxC4Octets_Object = MibTableColumn
fcBxPortCurrentTxC4Octets = _FcBxPortCurrentTxC4Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 32),
    _FcBxPortCurrentTxC4Octets_Type()
)
fcBxPortCurrentTxC4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxC4Octets.setStatus("current")
_FcBxPortCurrentTxC4Packets_Type = Counter64
_FcBxPortCurrentTxC4Packets_Object = MibTableColumn
fcBxPortCurrentTxC4Packets = _FcBxPortCurrentTxC4Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 33),
    _FcBxPortCurrentTxC4Packets_Type()
)
fcBxPortCurrentTxC4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxC4Packets.setStatus("current")
_FcBxPortCurrentRxC4Octets_Type = Counter64
_FcBxPortCurrentRxC4Octets_Object = MibTableColumn
fcBxPortCurrentRxC4Octets = _FcBxPortCurrentRxC4Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 34),
    _FcBxPortCurrentRxC4Octets_Type()
)
fcBxPortCurrentRxC4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC4Octets.setStatus("current")
_FcBxPortCurrentRxC4Packets_Type = Counter64
_FcBxPortCurrentRxC4Packets_Object = MibTableColumn
fcBxPortCurrentRxC4Packets = _FcBxPortCurrentRxC4Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 35),
    _FcBxPortCurrentRxC4Packets_Type()
)
fcBxPortCurrentRxC4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC4Packets.setStatus("current")
_FcBxPortCurrentRxC4ErroredSizeFrames_Type = Counter64
_FcBxPortCurrentRxC4ErroredSizeFrames_Object = MibTableColumn
fcBxPortCurrentRxC4ErroredSizeFrames = _FcBxPortCurrentRxC4ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 36),
    _FcBxPortCurrentRxC4ErroredSizeFrames_Type()
)
fcBxPortCurrentRxC4ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxC4ErroredSizeFrames.setStatus("current")
_FcBxPortCurrentTxCFOctets_Type = Counter64
_FcBxPortCurrentTxCFOctets_Object = MibTableColumn
fcBxPortCurrentTxCFOctets = _FcBxPortCurrentTxCFOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 37),
    _FcBxPortCurrentTxCFOctets_Type()
)
fcBxPortCurrentTxCFOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxCFOctets.setStatus("current")
_FcBxPortCurrentTxCFPackets_Type = Counter64
_FcBxPortCurrentTxCFPackets_Object = MibTableColumn
fcBxPortCurrentTxCFPackets = _FcBxPortCurrentTxCFPackets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 38),
    _FcBxPortCurrentTxCFPackets_Type()
)
fcBxPortCurrentTxCFPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentTxCFPackets.setStatus("current")
_FcBxPortCurrentRxCFOctets_Type = Counter64
_FcBxPortCurrentRxCFOctets_Object = MibTableColumn
fcBxPortCurrentRxCFOctets = _FcBxPortCurrentRxCFOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 39),
    _FcBxPortCurrentRxCFOctets_Type()
)
fcBxPortCurrentRxCFOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxCFOctets.setStatus("current")
_FcBxPortCurrentRxCFPackets_Type = Counter64
_FcBxPortCurrentRxCFPackets_Object = MibTableColumn
fcBxPortCurrentRxCFPackets = _FcBxPortCurrentRxCFPackets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 40),
    _FcBxPortCurrentRxCFPackets_Type()
)
fcBxPortCurrentRxCFPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxCFPackets.setStatus("current")
_FcBxPortCurrentRxCFErroredSizeFrame_Type = Counter64
_FcBxPortCurrentRxCFErroredSizeFrame_Object = MibTableColumn
fcBxPortCurrentRxCFErroredSizeFrame = _FcBxPortCurrentRxCFErroredSizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 1, 1, 41),
    _FcBxPortCurrentRxCFErroredSizeFrame_Type()
)
fcBxPortCurrentRxCFErroredSizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortCurrentRxCFErroredSizeFrame.setStatus("current")
_FcBxPortIntervalTable_Object = MibTable
fcBxPortIntervalTable = _FcBxPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fcBxPortIntervalTable.setStatus("current")
_FcBxPortIntervalEntry_Object = MibTableRow
fcBxPortIntervalEntry = _FcBxPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1)
)
fcBxPortIntervalEntry.setIndexNames(
    (0, "SL-FC-MIB", "fcBxPortIntervalIndex"),
    (0, "SL-FC-MIB", "fcBxPortIntervalNumber"),
)
if mibBuilder.loadTexts:
    fcBxPortIntervalEntry.setStatus("current")
_FcBxPortIntervalIndex_Type = InterfaceIndex
_FcBxPortIntervalIndex_Object = MibTableColumn
fcBxPortIntervalIndex = _FcBxPortIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 1),
    _FcBxPortIntervalIndex_Type()
)
fcBxPortIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalIndex.setStatus("current")


class _FcBxPortIntervalNumber_Type(Integer32):
    """Custom type fcBxPortIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_FcBxPortIntervalNumber_Type.__name__ = "Integer32"
_FcBxPortIntervalNumber_Object = MibTableColumn
fcBxPortIntervalNumber = _FcBxPortIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 2),
    _FcBxPortIntervalNumber_Type()
)
fcBxPortIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalNumber.setStatus("current")
_FcBxPortIntervalLinkFailures_Type = Counter64
_FcBxPortIntervalLinkFailures_Object = MibTableColumn
fcBxPortIntervalLinkFailures = _FcBxPortIntervalLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 3),
    _FcBxPortIntervalLinkFailures_Type()
)
fcBxPortIntervalLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalLinkFailures.setStatus("current")
_FcBxPortIntervalSyncLosses_Type = Counter64
_FcBxPortIntervalSyncLosses_Object = MibTableColumn
fcBxPortIntervalSyncLosses = _FcBxPortIntervalSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 4),
    _FcBxPortIntervalSyncLosses_Type()
)
fcBxPortIntervalSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalSyncLosses.setStatus("current")
_FcBxPortIntervalSigLosses_Type = Counter64
_FcBxPortIntervalSigLosses_Object = MibTableColumn
fcBxPortIntervalSigLosses = _FcBxPortIntervalSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 5),
    _FcBxPortIntervalSigLosses_Type()
)
fcBxPortIntervalSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalSigLosses.setStatus("current")
_FcBxPortIntervalPrimSeqProtoErrors_Type = Counter64
_FcBxPortIntervalPrimSeqProtoErrors_Object = MibTableColumn
fcBxPortIntervalPrimSeqProtoErrors = _FcBxPortIntervalPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 6),
    _FcBxPortIntervalPrimSeqProtoErrors_Type()
)
fcBxPortIntervalPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalPrimSeqProtoErrors.setStatus("current")
_FcBxPortIntervalInvalidTxWords_Type = Counter64
_FcBxPortIntervalInvalidTxWords_Object = MibTableColumn
fcBxPortIntervalInvalidTxWords = _FcBxPortIntervalInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 7),
    _FcBxPortIntervalInvalidTxWords_Type()
)
fcBxPortIntervalInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalInvalidTxWords.setStatus("current")
_FcBxPortIntervalInvalidCrcs_Type = Counter64
_FcBxPortIntervalInvalidCrcs_Object = MibTableColumn
fcBxPortIntervalInvalidCrcs = _FcBxPortIntervalInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 8),
    _FcBxPortIntervalInvalidCrcs_Type()
)
fcBxPortIntervalInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalInvalidCrcs.setStatus("current")
_FcBxPortIntervalDelimiterErrors_Type = Counter64
_FcBxPortIntervalDelimiterErrors_Object = MibTableColumn
fcBxPortIntervalDelimiterErrors = _FcBxPortIntervalDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 9),
    _FcBxPortIntervalDelimiterErrors_Type()
)
fcBxPortIntervalDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalDelimiterErrors.setStatus("current")
_FcBxPortIntervalRxFlowControl_Type = Counter64
_FcBxPortIntervalRxFlowControl_Object = MibTableColumn
fcBxPortIntervalRxFlowControl = _FcBxPortIntervalRxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 10),
    _FcBxPortIntervalRxFlowControl_Type()
)
fcBxPortIntervalRxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxFlowControl.setStatus("current")
_FcBxPortIntervalTxFlowControl_Type = Counter64
_FcBxPortIntervalTxFlowControl_Object = MibTableColumn
fcBxPortIntervalTxFlowControl = _FcBxPortIntervalTxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 11),
    _FcBxPortIntervalTxFlowControl_Type()
)
fcBxPortIntervalTxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxFlowControl.setStatus("current")
_FcBxPortIntervalRxOctets_Type = Counter64
_FcBxPortIntervalRxOctets_Object = MibTableColumn
fcBxPortIntervalRxOctets = _FcBxPortIntervalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 12),
    _FcBxPortIntervalRxOctets_Type()
)
fcBxPortIntervalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxOctets.setStatus("current")
_FcBxPortIntervalRxPkts_Type = Counter64
_FcBxPortIntervalRxPkts_Object = MibTableColumn
fcBxPortIntervalRxPkts = _FcBxPortIntervalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 13),
    _FcBxPortIntervalRxPkts_Type()
)
fcBxPortIntervalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxPkts.setStatus("current")
_FcBxPortIntervalTxOctets_Type = Counter64
_FcBxPortIntervalTxOctets_Object = MibTableColumn
fcBxPortIntervalTxOctets = _FcBxPortIntervalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 14),
    _FcBxPortIntervalTxOctets_Type()
)
fcBxPortIntervalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxOctets.setStatus("current")
_FcBxPortIntervalTxPkts_Type = Counter64
_FcBxPortIntervalTxPkts_Object = MibTableColumn
fcBxPortIntervalTxPkts = _FcBxPortIntervalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 15),
    _FcBxPortIntervalTxPkts_Type()
)
fcBxPortIntervalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxPkts.setStatus("current")
_FcBxPortIntervalRxLinkReset_Type = Counter64
_FcBxPortIntervalRxLinkReset_Object = MibTableColumn
fcBxPortIntervalRxLinkReset = _FcBxPortIntervalRxLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 16),
    _FcBxPortIntervalRxLinkReset_Type()
)
fcBxPortIntervalRxLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxLinkReset.setStatus("current")
_FcBxPortIntervalTxLinkReset_Type = Counter64
_FcBxPortIntervalTxLinkReset_Object = MibTableColumn
fcBxPortIntervalTxLinkReset = _FcBxPortIntervalTxLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 17),
    _FcBxPortIntervalTxLinkReset_Type()
)
fcBxPortIntervalTxLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxLinkReset.setStatus("current")
_FcBxPortIntervalRxOls_Type = Counter64
_FcBxPortIntervalRxOls_Object = MibTableColumn
fcBxPortIntervalRxOls = _FcBxPortIntervalRxOls_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 18),
    _FcBxPortIntervalRxOls_Type()
)
fcBxPortIntervalRxOls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxOls.setStatus("current")
_FcBxPortIntervalTxOls_Type = Counter64
_FcBxPortIntervalTxOls_Object = MibTableColumn
fcBxPortIntervalTxOls = _FcBxPortIntervalTxOls_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 19),
    _FcBxPortIntervalTxOls_Type()
)
fcBxPortIntervalTxOls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxOls.setStatus("current")
_FcBxPortIntervalRxErroredBbwHeaders_Type = Counter64
_FcBxPortIntervalRxErroredBbwHeaders_Object = MibTableColumn
fcBxPortIntervalRxErroredBbwHeaders = _FcBxPortIntervalRxErroredBbwHeaders_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 20),
    _FcBxPortIntervalRxErroredBbwHeaders_Type()
)
fcBxPortIntervalRxErroredBbwHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxErroredBbwHeaders.setStatus("current")
_FcBxPortIntervalRxC2FramesDiscarded_Type = Counter64
_FcBxPortIntervalRxC2FramesDiscarded_Object = MibTableColumn
fcBxPortIntervalRxC2FramesDiscarded = _FcBxPortIntervalRxC2FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 21),
    _FcBxPortIntervalRxC2FramesDiscarded_Type()
)
fcBxPortIntervalRxC2FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC2FramesDiscarded.setStatus("current")
_FcBxPortIntervalTxC2Octets_Type = Counter64
_FcBxPortIntervalTxC2Octets_Object = MibTableColumn
fcBxPortIntervalTxC2Octets = _FcBxPortIntervalTxC2Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 22),
    _FcBxPortIntervalTxC2Octets_Type()
)
fcBxPortIntervalTxC2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxC2Octets.setStatus("current")
_FcBxPortIntervalTxC2Packets_Type = Counter64
_FcBxPortIntervalTxC2Packets_Object = MibTableColumn
fcBxPortIntervalTxC2Packets = _FcBxPortIntervalTxC2Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 23),
    _FcBxPortIntervalTxC2Packets_Type()
)
fcBxPortIntervalTxC2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxC2Packets.setStatus("current")
_FcBxPortIntervalRxC2Octets_Type = Counter64
_FcBxPortIntervalRxC2Octets_Object = MibTableColumn
fcBxPortIntervalRxC2Octets = _FcBxPortIntervalRxC2Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 24),
    _FcBxPortIntervalRxC2Octets_Type()
)
fcBxPortIntervalRxC2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC2Octets.setStatus("current")
_FcBxPortIntervalRxC2Packets_Type = Counter64
_FcBxPortIntervalRxC2Packets_Object = MibTableColumn
fcBxPortIntervalRxC2Packets = _FcBxPortIntervalRxC2Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 25),
    _FcBxPortIntervalRxC2Packets_Type()
)
fcBxPortIntervalRxC2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC2Packets.setStatus("current")
_FcBxPortIntervalRxC2ErroredSizeFrames_Type = Counter64
_FcBxPortIntervalRxC2ErroredSizeFrames_Object = MibTableColumn
fcBxPortIntervalRxC2ErroredSizeFrames = _FcBxPortIntervalRxC2ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 26),
    _FcBxPortIntervalRxC2ErroredSizeFrames_Type()
)
fcBxPortIntervalRxC2ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC2ErroredSizeFrames.setStatus("current")
_FcBxPortIntervalRxC3FramesDiscarded_Type = Counter64
_FcBxPortIntervalRxC3FramesDiscarded_Object = MibTableColumn
fcBxPortIntervalRxC3FramesDiscarded = _FcBxPortIntervalRxC3FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 27),
    _FcBxPortIntervalRxC3FramesDiscarded_Type()
)
fcBxPortIntervalRxC3FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC3FramesDiscarded.setStatus("current")
_FcBxPortIntervalTxC3Octets_Type = Counter64
_FcBxPortIntervalTxC3Octets_Object = MibTableColumn
fcBxPortIntervalTxC3Octets = _FcBxPortIntervalTxC3Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 28),
    _FcBxPortIntervalTxC3Octets_Type()
)
fcBxPortIntervalTxC3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxC3Octets.setStatus("current")
_FcBxPortIntervalTxC3Packets_Type = Counter64
_FcBxPortIntervalTxC3Packets_Object = MibTableColumn
fcBxPortIntervalTxC3Packets = _FcBxPortIntervalTxC3Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 29),
    _FcBxPortIntervalTxC3Packets_Type()
)
fcBxPortIntervalTxC3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxC3Packets.setStatus("current")
_FcBxPortIntervalRxC3Octets_Type = Counter64
_FcBxPortIntervalRxC3Octets_Object = MibTableColumn
fcBxPortIntervalRxC3Octets = _FcBxPortIntervalRxC3Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 30),
    _FcBxPortIntervalRxC3Octets_Type()
)
fcBxPortIntervalRxC3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC3Octets.setStatus("current")
_FcBxPortIntervalRxC3Packets_Type = Counter64
_FcBxPortIntervalRxC3Packets_Object = MibTableColumn
fcBxPortIntervalRxC3Packets = _FcBxPortIntervalRxC3Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 31),
    _FcBxPortIntervalRxC3Packets_Type()
)
fcBxPortIntervalRxC3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC3Packets.setStatus("current")
_FcBxPortIntervalRxC3ErroredSizeFrames_Type = Counter64
_FcBxPortIntervalRxC3ErroredSizeFrames_Object = MibTableColumn
fcBxPortIntervalRxC3ErroredSizeFrames = _FcBxPortIntervalRxC3ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 32),
    _FcBxPortIntervalRxC3ErroredSizeFrames_Type()
)
fcBxPortIntervalRxC3ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC3ErroredSizeFrames.setStatus("current")
_FcBxPortIntervalTxC4Octets_Type = Counter64
_FcBxPortIntervalTxC4Octets_Object = MibTableColumn
fcBxPortIntervalTxC4Octets = _FcBxPortIntervalTxC4Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 33),
    _FcBxPortIntervalTxC4Octets_Type()
)
fcBxPortIntervalTxC4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxC4Octets.setStatus("current")
_FcBxPortIntervalTxC4Packets_Type = Counter64
_FcBxPortIntervalTxC4Packets_Object = MibTableColumn
fcBxPortIntervalTxC4Packets = _FcBxPortIntervalTxC4Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 34),
    _FcBxPortIntervalTxC4Packets_Type()
)
fcBxPortIntervalTxC4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxC4Packets.setStatus("current")
_FcBxPortIntervalRxC4Octets_Type = Counter64
_FcBxPortIntervalRxC4Octets_Object = MibTableColumn
fcBxPortIntervalRxC4Octets = _FcBxPortIntervalRxC4Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 35),
    _FcBxPortIntervalRxC4Octets_Type()
)
fcBxPortIntervalRxC4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC4Octets.setStatus("current")
_FcBxPortIntervalRxC4Packets_Type = Counter64
_FcBxPortIntervalRxC4Packets_Object = MibTableColumn
fcBxPortIntervalRxC4Packets = _FcBxPortIntervalRxC4Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 36),
    _FcBxPortIntervalRxC4Packets_Type()
)
fcBxPortIntervalRxC4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC4Packets.setStatus("current")
_FcBxPortIntervalRxC4ErroredSizeFrames_Type = Counter64
_FcBxPortIntervalRxC4ErroredSizeFrames_Object = MibTableColumn
fcBxPortIntervalRxC4ErroredSizeFrames = _FcBxPortIntervalRxC4ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 37),
    _FcBxPortIntervalRxC4ErroredSizeFrames_Type()
)
fcBxPortIntervalRxC4ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxC4ErroredSizeFrames.setStatus("current")
_FcBxPortIntervalTxCFOctets_Type = Counter64
_FcBxPortIntervalTxCFOctets_Object = MibTableColumn
fcBxPortIntervalTxCFOctets = _FcBxPortIntervalTxCFOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 38),
    _FcBxPortIntervalTxCFOctets_Type()
)
fcBxPortIntervalTxCFOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxCFOctets.setStatus("current")
_FcBxPortIntervalTxCFPackets_Type = Counter64
_FcBxPortIntervalTxCFPackets_Object = MibTableColumn
fcBxPortIntervalTxCFPackets = _FcBxPortIntervalTxCFPackets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 39),
    _FcBxPortIntervalTxCFPackets_Type()
)
fcBxPortIntervalTxCFPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalTxCFPackets.setStatus("current")
_FcBxPortIntervalRxCFOctets_Type = Counter64
_FcBxPortIntervalRxCFOctets_Object = MibTableColumn
fcBxPortIntervalRxCFOctets = _FcBxPortIntervalRxCFOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 40),
    _FcBxPortIntervalRxCFOctets_Type()
)
fcBxPortIntervalRxCFOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxCFOctets.setStatus("current")
_FcBxPortIntervalRxCFPackets_Type = Counter64
_FcBxPortIntervalRxCFPackets_Object = MibTableColumn
fcBxPortIntervalRxCFPackets = _FcBxPortIntervalRxCFPackets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 41),
    _FcBxPortIntervalRxCFPackets_Type()
)
fcBxPortIntervalRxCFPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxCFPackets.setStatus("current")
_FcBxPortIntervalRxCFErroredSizeFrame_Type = Counter64
_FcBxPortIntervalRxCFErroredSizeFrame_Object = MibTableColumn
fcBxPortIntervalRxCFErroredSizeFrame = _FcBxPortIntervalRxCFErroredSizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 42),
    _FcBxPortIntervalRxCFErroredSizeFrame_Type()
)
fcBxPortIntervalRxCFErroredSizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalRxCFErroredSizeFrame.setStatus("current")
_FcBxPortIntervalValidData_Type = TruthValue
_FcBxPortIntervalValidData_Object = MibTableColumn
fcBxPortIntervalValidData = _FcBxPortIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 2, 1, 43),
    _FcBxPortIntervalValidData_Type()
)
fcBxPortIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortIntervalValidData.setStatus("current")
_FcBxPortTotalTable_Object = MibTable
fcBxPortTotalTable = _FcBxPortTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    fcBxPortTotalTable.setStatus("current")
_FcBxPortTotalEntry_Object = MibTableRow
fcBxPortTotalEntry = _FcBxPortTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1)
)
fcBxPortTotalEntry.setIndexNames(
    (0, "SL-FC-MIB", "fcBxPortTotalIndex"),
    (0, "SL-FC-MIB", "fcBxPortTotalDayNumber"),
)
if mibBuilder.loadTexts:
    fcBxPortTotalEntry.setStatus("current")
_FcBxPortTotalIndex_Type = InterfaceIndex
_FcBxPortTotalIndex_Object = MibTableColumn
fcBxPortTotalIndex = _FcBxPortTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 1),
    _FcBxPortTotalIndex_Type()
)
fcBxPortTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalIndex.setStatus("current")


class _FcBxPortTotalDayNumber_Type(Integer32):
    """Custom type fcBxPortTotalDayNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_FcBxPortTotalDayNumber_Type.__name__ = "Integer32"
_FcBxPortTotalDayNumber_Object = MibTableColumn
fcBxPortTotalDayNumber = _FcBxPortTotalDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 2),
    _FcBxPortTotalDayNumber_Type()
)
fcBxPortTotalDayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fcBxPortTotalDayNumber.setStatus("current")
_FcBxPortTotalLinkFailures_Type = Counter64
_FcBxPortTotalLinkFailures_Object = MibTableColumn
fcBxPortTotalLinkFailures = _FcBxPortTotalLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 3),
    _FcBxPortTotalLinkFailures_Type()
)
fcBxPortTotalLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalLinkFailures.setStatus("current")
_FcBxPortTotalSyncLosses_Type = Counter64
_FcBxPortTotalSyncLosses_Object = MibTableColumn
fcBxPortTotalSyncLosses = _FcBxPortTotalSyncLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 4),
    _FcBxPortTotalSyncLosses_Type()
)
fcBxPortTotalSyncLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalSyncLosses.setStatus("current")
_FcBxPortTotalSigLosses_Type = Counter64
_FcBxPortTotalSigLosses_Object = MibTableColumn
fcBxPortTotalSigLosses = _FcBxPortTotalSigLosses_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 5),
    _FcBxPortTotalSigLosses_Type()
)
fcBxPortTotalSigLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalSigLosses.setStatus("current")
_FcBxPortTotalPrimSeqProtoErrors_Type = Counter64
_FcBxPortTotalPrimSeqProtoErrors_Object = MibTableColumn
fcBxPortTotalPrimSeqProtoErrors = _FcBxPortTotalPrimSeqProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 6),
    _FcBxPortTotalPrimSeqProtoErrors_Type()
)
fcBxPortTotalPrimSeqProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalPrimSeqProtoErrors.setStatus("current")
_FcBxPortTotalInvalidTxWords_Type = Counter64
_FcBxPortTotalInvalidTxWords_Object = MibTableColumn
fcBxPortTotalInvalidTxWords = _FcBxPortTotalInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 7),
    _FcBxPortTotalInvalidTxWords_Type()
)
fcBxPortTotalInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalInvalidTxWords.setStatus("current")
_FcBxPortTotalInvalidCrcs_Type = Counter64
_FcBxPortTotalInvalidCrcs_Object = MibTableColumn
fcBxPortTotalInvalidCrcs = _FcBxPortTotalInvalidCrcs_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 8),
    _FcBxPortTotalInvalidCrcs_Type()
)
fcBxPortTotalInvalidCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalInvalidCrcs.setStatus("current")
_FcBxPortTotalDelimiterErrors_Type = Counter64
_FcBxPortTotalDelimiterErrors_Object = MibTableColumn
fcBxPortTotalDelimiterErrors = _FcBxPortTotalDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 9),
    _FcBxPortTotalDelimiterErrors_Type()
)
fcBxPortTotalDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalDelimiterErrors.setStatus("current")
_FcBxPortTotalRxFlowControl_Type = Counter64
_FcBxPortTotalRxFlowControl_Object = MibTableColumn
fcBxPortTotalRxFlowControl = _FcBxPortTotalRxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 10),
    _FcBxPortTotalRxFlowControl_Type()
)
fcBxPortTotalRxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxFlowControl.setStatus("current")
_FcBxPortTotalTxFlowControl_Type = Counter64
_FcBxPortTotalTxFlowControl_Object = MibTableColumn
fcBxPortTotalTxFlowControl = _FcBxPortTotalTxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 11),
    _FcBxPortTotalTxFlowControl_Type()
)
fcBxPortTotalTxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxFlowControl.setStatus("current")
_FcBxPortTotalRxOctets_Type = Counter64
_FcBxPortTotalRxOctets_Object = MibTableColumn
fcBxPortTotalRxOctets = _FcBxPortTotalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 12),
    _FcBxPortTotalRxOctets_Type()
)
fcBxPortTotalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxOctets.setStatus("current")
_FcBxPortTotalRxPkts_Type = Counter64
_FcBxPortTotalRxPkts_Object = MibTableColumn
fcBxPortTotalRxPkts = _FcBxPortTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 13),
    _FcBxPortTotalRxPkts_Type()
)
fcBxPortTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxPkts.setStatus("current")
_FcBxPortTotalTxOctets_Type = Counter64
_FcBxPortTotalTxOctets_Object = MibTableColumn
fcBxPortTotalTxOctets = _FcBxPortTotalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 14),
    _FcBxPortTotalTxOctets_Type()
)
fcBxPortTotalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxOctets.setStatus("current")
_FcBxPortTotalTxPkts_Type = Counter64
_FcBxPortTotalTxPkts_Object = MibTableColumn
fcBxPortTotalTxPkts = _FcBxPortTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 15),
    _FcBxPortTotalTxPkts_Type()
)
fcBxPortTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxPkts.setStatus("current")
_FcBxPortTotalRxLinkReset_Type = Counter64
_FcBxPortTotalRxLinkReset_Object = MibTableColumn
fcBxPortTotalRxLinkReset = _FcBxPortTotalRxLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 16),
    _FcBxPortTotalRxLinkReset_Type()
)
fcBxPortTotalRxLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxLinkReset.setStatus("current")
_FcBxPortTotalTxLinkReset_Type = Counter64
_FcBxPortTotalTxLinkReset_Object = MibTableColumn
fcBxPortTotalTxLinkReset = _FcBxPortTotalTxLinkReset_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 17),
    _FcBxPortTotalTxLinkReset_Type()
)
fcBxPortTotalTxLinkReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxLinkReset.setStatus("current")
_FcBxPortTotalRxOls_Type = Counter64
_FcBxPortTotalRxOls_Object = MibTableColumn
fcBxPortTotalRxOls = _FcBxPortTotalRxOls_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 18),
    _FcBxPortTotalRxOls_Type()
)
fcBxPortTotalRxOls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxOls.setStatus("current")
_FcBxPortTotalTxOls_Type = Counter64
_FcBxPortTotalTxOls_Object = MibTableColumn
fcBxPortTotalTxOls = _FcBxPortTotalTxOls_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 19),
    _FcBxPortTotalTxOls_Type()
)
fcBxPortTotalTxOls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxOls.setStatus("current")
_FcBxPortTotalRxErroredBbwHeaders_Type = Counter64
_FcBxPortTotalRxErroredBbwHeaders_Object = MibTableColumn
fcBxPortTotalRxErroredBbwHeaders = _FcBxPortTotalRxErroredBbwHeaders_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 20),
    _FcBxPortTotalRxErroredBbwHeaders_Type()
)
fcBxPortTotalRxErroredBbwHeaders.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxErroredBbwHeaders.setStatus("current")
_FcBxPortTotalRxC2FramesDiscarded_Type = Counter64
_FcBxPortTotalRxC2FramesDiscarded_Object = MibTableColumn
fcBxPortTotalRxC2FramesDiscarded = _FcBxPortTotalRxC2FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 21),
    _FcBxPortTotalRxC2FramesDiscarded_Type()
)
fcBxPortTotalRxC2FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC2FramesDiscarded.setStatus("current")
_FcBxPortTotalTxC2Octets_Type = Counter64
_FcBxPortTotalTxC2Octets_Object = MibTableColumn
fcBxPortTotalTxC2Octets = _FcBxPortTotalTxC2Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 22),
    _FcBxPortTotalTxC2Octets_Type()
)
fcBxPortTotalTxC2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxC2Octets.setStatus("current")
_FcBxPortTotalTxC2Packets_Type = Counter64
_FcBxPortTotalTxC2Packets_Object = MibTableColumn
fcBxPortTotalTxC2Packets = _FcBxPortTotalTxC2Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 23),
    _FcBxPortTotalTxC2Packets_Type()
)
fcBxPortTotalTxC2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxC2Packets.setStatus("current")
_FcBxPortTotalRxC2Octets_Type = Counter64
_FcBxPortTotalRxC2Octets_Object = MibTableColumn
fcBxPortTotalRxC2Octets = _FcBxPortTotalRxC2Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 24),
    _FcBxPortTotalRxC2Octets_Type()
)
fcBxPortTotalRxC2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC2Octets.setStatus("current")
_FcBxPortTotalRxC2Packets_Type = Counter64
_FcBxPortTotalRxC2Packets_Object = MibTableColumn
fcBxPortTotalRxC2Packets = _FcBxPortTotalRxC2Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 25),
    _FcBxPortTotalRxC2Packets_Type()
)
fcBxPortTotalRxC2Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC2Packets.setStatus("current")
_FcBxPortTotalRxC2ErroredSizeFrames_Type = Counter64
_FcBxPortTotalRxC2ErroredSizeFrames_Object = MibTableColumn
fcBxPortTotalRxC2ErroredSizeFrames = _FcBxPortTotalRxC2ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 26),
    _FcBxPortTotalRxC2ErroredSizeFrames_Type()
)
fcBxPortTotalRxC2ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC2ErroredSizeFrames.setStatus("current")
_FcBxPortTotalRxC3FramesDiscarded_Type = Counter64
_FcBxPortTotalRxC3FramesDiscarded_Object = MibTableColumn
fcBxPortTotalRxC3FramesDiscarded = _FcBxPortTotalRxC3FramesDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 27),
    _FcBxPortTotalRxC3FramesDiscarded_Type()
)
fcBxPortTotalRxC3FramesDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC3FramesDiscarded.setStatus("current")
_FcBxPortTotalTxC3Octets_Type = Counter64
_FcBxPortTotalTxC3Octets_Object = MibTableColumn
fcBxPortTotalTxC3Octets = _FcBxPortTotalTxC3Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 28),
    _FcBxPortTotalTxC3Octets_Type()
)
fcBxPortTotalTxC3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxC3Octets.setStatus("current")
_FcBxPortTotalTxC3Packets_Type = Counter64
_FcBxPortTotalTxC3Packets_Object = MibTableColumn
fcBxPortTotalTxC3Packets = _FcBxPortTotalTxC3Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 29),
    _FcBxPortTotalTxC3Packets_Type()
)
fcBxPortTotalTxC3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxC3Packets.setStatus("current")
_FcBxPortTotalRxC3Octets_Type = Counter64
_FcBxPortTotalRxC3Octets_Object = MibTableColumn
fcBxPortTotalRxC3Octets = _FcBxPortTotalRxC3Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 30),
    _FcBxPortTotalRxC3Octets_Type()
)
fcBxPortTotalRxC3Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC3Octets.setStatus("current")
_FcBxPortTotalRxC3Packets_Type = Counter64
_FcBxPortTotalRxC3Packets_Object = MibTableColumn
fcBxPortTotalRxC3Packets = _FcBxPortTotalRxC3Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 31),
    _FcBxPortTotalRxC3Packets_Type()
)
fcBxPortTotalRxC3Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC3Packets.setStatus("current")
_FcBxPortTotalRxC3ErroredSizeFrames_Type = Counter64
_FcBxPortTotalRxC3ErroredSizeFrames_Object = MibTableColumn
fcBxPortTotalRxC3ErroredSizeFrames = _FcBxPortTotalRxC3ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 32),
    _FcBxPortTotalRxC3ErroredSizeFrames_Type()
)
fcBxPortTotalRxC3ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC3ErroredSizeFrames.setStatus("current")
_FcBxPortTotalTxC4Octets_Type = Counter64
_FcBxPortTotalTxC4Octets_Object = MibTableColumn
fcBxPortTotalTxC4Octets = _FcBxPortTotalTxC4Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 33),
    _FcBxPortTotalTxC4Octets_Type()
)
fcBxPortTotalTxC4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxC4Octets.setStatus("current")
_FcBxPortTotalTxC4Packets_Type = Counter64
_FcBxPortTotalTxC4Packets_Object = MibTableColumn
fcBxPortTotalTxC4Packets = _FcBxPortTotalTxC4Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 34),
    _FcBxPortTotalTxC4Packets_Type()
)
fcBxPortTotalTxC4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxC4Packets.setStatus("current")
_FcBxPortTotalRxC4Octets_Type = Counter64
_FcBxPortTotalRxC4Octets_Object = MibTableColumn
fcBxPortTotalRxC4Octets = _FcBxPortTotalRxC4Octets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 35),
    _FcBxPortTotalRxC4Octets_Type()
)
fcBxPortTotalRxC4Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC4Octets.setStatus("current")
_FcBxPortTotalRxC4Packets_Type = Counter64
_FcBxPortTotalRxC4Packets_Object = MibTableColumn
fcBxPortTotalRxC4Packets = _FcBxPortTotalRxC4Packets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 36),
    _FcBxPortTotalRxC4Packets_Type()
)
fcBxPortTotalRxC4Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC4Packets.setStatus("current")
_FcBxPortTotalRxC4ErroredSizeFrames_Type = Counter64
_FcBxPortTotalRxC4ErroredSizeFrames_Object = MibTableColumn
fcBxPortTotalRxC4ErroredSizeFrames = _FcBxPortTotalRxC4ErroredSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 37),
    _FcBxPortTotalRxC4ErroredSizeFrames_Type()
)
fcBxPortTotalRxC4ErroredSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxC4ErroredSizeFrames.setStatus("current")
_FcBxPortTotalTxCFOctets_Type = Counter64
_FcBxPortTotalTxCFOctets_Object = MibTableColumn
fcBxPortTotalTxCFOctets = _FcBxPortTotalTxCFOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 38),
    _FcBxPortTotalTxCFOctets_Type()
)
fcBxPortTotalTxCFOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxCFOctets.setStatus("current")
_FcBxPortTotalTxCFPackets_Type = Counter64
_FcBxPortTotalTxCFPackets_Object = MibTableColumn
fcBxPortTotalTxCFPackets = _FcBxPortTotalTxCFPackets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 39),
    _FcBxPortTotalTxCFPackets_Type()
)
fcBxPortTotalTxCFPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalTxCFPackets.setStatus("current")
_FcBxPortTotalRxCFOctets_Type = Counter64
_FcBxPortTotalRxCFOctets_Object = MibTableColumn
fcBxPortTotalRxCFOctets = _FcBxPortTotalRxCFOctets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 40),
    _FcBxPortTotalRxCFOctets_Type()
)
fcBxPortTotalRxCFOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxCFOctets.setStatus("current")
_FcBxPortTotalRxCFPackets_Type = Counter64
_FcBxPortTotalRxCFPackets_Object = MibTableColumn
fcBxPortTotalRxCFPackets = _FcBxPortTotalRxCFPackets_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 41),
    _FcBxPortTotalRxCFPackets_Type()
)
fcBxPortTotalRxCFPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxCFPackets.setStatus("current")
_FcBxPortTotalRxCFErroredSizeFrame_Type = Counter64
_FcBxPortTotalRxCFErroredSizeFrame_Object = MibTableColumn
fcBxPortTotalRxCFErroredSizeFrame = _FcBxPortTotalRxCFErroredSizeFrame_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 42),
    _FcBxPortTotalRxCFErroredSizeFrame_Type()
)
fcBxPortTotalRxCFErroredSizeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalRxCFErroredSizeFrame.setStatus("current")
_FcBxPortTotalValidData_Type = TruthValue
_FcBxPortTotalValidData_Object = MibTableColumn
fcBxPortTotalValidData = _FcBxPortTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 3, 3, 1, 43),
    _FcBxPortTotalValidData_Type()
)
fcBxPortTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcBxPortTotalValidData.setStatus("current")
_FcBxTraps_ObjectIdentity = ObjectIdentity
fcBxTraps = _FcBxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 4)
)
fcBxPortEntry.registerAugmentions(
    ("SL-FC-MIB",
     "fcBxPortStatusEntry")
)
fcBxPortStatusEntry.setIndexNames(*fcBxPortEntry.getIndexNames())
fcBxPortEntry.registerAugmentions(
    ("SL-FC-MIB",
     "fcBxLoginEntry")
)
fcBxLoginEntry.setIndexNames(*fcBxPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fcBxPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 4, 1)
)
fcBxPortStatusChange.setObjects(
      *(("SL-FC-MIB", "fcBxPortIndex"),
        ("SL-FC-MIB", "fcBxPortStatus"))
)
if mibBuilder.loadTexts:
    fcBxPortStatusChange.setStatus(
        "current"
    )

fcBxPortLinkRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 3, 1, 4, 2)
)
fcBxPortLinkRestart.setObjects(
    ("SL-FC-MIB", "fcBxPortIndex")
)
if mibBuilder.loadTexts:
    fcBxPortLinkRestart.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-FC-MIB",
    **{"MilliSeconds": MilliSeconds,
       "MicroSeconds": MicroSeconds,
       "FcNameId": FcNameId,
       "FcAddressId": FcAddressId,
       "FcRxDataFieldSize": FcRxDataFieldSize,
       "FcBbCredit": FcBbCredit,
       "FcphVersion": FcphVersion,
       "FcStackedConnMode": FcStackedConnMode,
       "FcCosCap": FcCosCap,
       "FcBxPortCapacity": FcBxPortCapacity,
       "FcBxPortIndex": FcBxPortIndex,
       "FcExPortIndex": FcExPortIndex,
       "FcBbCreditModel": FcBbCreditModel,
       "FcPortSpeed": FcPortSpeed,
       "fcBxMIB": fcBxMIB,
       "fcBxMIBObjects": fcBxMIBObjects,
       "fcBxConfig": fcBxConfig,
       "fcBxPortTable": fcBxPortTable,
       "fcBxPortEntry": fcBxPortEntry,
       "fcBxPortIndex": fcBxPortIndex,
       "fcBxPortName": fcBxPortName,
       "fcBxPortFcphVersionHigh": fcBxPortFcphVersionHigh,
       "fcBxPortFcphVersionLow": fcBxPortFcphVersionLow,
       "fcBxPortBbCredit": fcBxPortBbCredit,
       "fcBxPortRxBufSize": fcBxPortRxBufSize,
       "fcBxPortRatov": fcBxPortRatov,
       "fcBxPortEdtov": fcBxPortEdtov,
       "fcBxPortCosSupported": fcBxPortCosSupported,
       "fcBxPortClass2SeqDeliv": fcBxPortClass2SeqDeliv,
       "fcBxPortClass3SeqDeliv": fcBxPortClass3SeqDeliv,
       "fcBxPortHoldTime": fcBxPortHoldTime,
       "fcBxPortFabricName": fcBxPortFabricName,
       "fcBxPortPhysRttov": fcBxPortPhysRttov,
       "fcBxPortTranceiverMedia": fcBxPortTranceiverMedia,
       "fcBxPortPauseTimeout": fcBxPortPauseTimeout,
       "fcBxPortBbThresholdRx": fcBxPortBbThresholdRx,
       "fcBxPortBbThresholdTx": fcBxPortBbThresholdTx,
       "fcBxPortResetPmCounters": fcBxPortResetPmCounters,
       "fcBxPortTranceiverType": fcBxPortTranceiverType,
       "fcBxPortWwnTransparent": fcBxPortWwnTransparent,
       "fcBxPortAdminSpeed": fcBxPortAdminSpeed,
       "fcBxPortRestartLink": fcBxPortRestartLink,
       "fcBxPortTransceiverRate": fcBxPortTransceiverRate,
       "fcBxPortElpInitiator": fcBxPortElpInitiator,
       "fcBxPortRemoteSwitchFabricName": fcBxPortRemoteSwitchFabricName,
       "fcBxPortRemoteSwitchPortName": fcBxPortRemoteSwitchPortName,
       "fcBxStatus": fcBxStatus,
       "fcBxPortStatusTable": fcBxPortStatusTable,
       "fcBxPortStatusEntry": fcBxPortStatusEntry,
       "fcBxPortBbRxBufferAvailable": fcBxPortBbRxBufferAvailable,
       "fcBxPortBbTxBufferAvailable": fcBxPortBbTxBufferAvailable,
       "fcBxPortStatus": fcBxPortStatus,
       "fcBxPortStatusValidIntervals": fcBxPortStatusValidIntervals,
       "fcBxPortStatusLoginState": fcBxPortStatusLoginState,
       "fcBxPortStatusAttachedPortType": fcBxPortStatusAttachedPortType,
       "fcBxLoginTable": fcBxLoginTable,
       "fcBxLoginEntry": fcBxLoginEntry,
       "fcBxPortVersionAgreed": fcBxPortVersionAgreed,
       "fcBxPortExPortBbCredit": fcBxPortExPortBbCredit,
       "fcBxPortExPortRxDataFieldSize": fcBxPortExPortRxDataFieldSize,
       "fcBxPortCosSuppAgreed": fcBxPortCosSuppAgreed,
       "fcBxPortClass2SeqDelivAgreed": fcBxPortClass2SeqDelivAgreed,
       "fcBxPortClass3SeqDelivAgreed": fcBxPortClass3SeqDelivAgreed,
       "fcBxPortExPortName": fcBxPortExPortName,
       "fcBxPortBbCreditModel": fcBxPortBbCreditModel,
       "fcBxPortExFabricName": fcBxPortExFabricName,
       "fcBxPm": fcBxPm,
       "fcBxPortCurrentTable": fcBxPortCurrentTable,
       "fcBxPortCurrentEntry": fcBxPortCurrentEntry,
       "fcBxPortCurrentIndex": fcBxPortCurrentIndex,
       "fcBxPortCurrentLinkFailures": fcBxPortCurrentLinkFailures,
       "fcBxPortCurrentSyncLosses": fcBxPortCurrentSyncLosses,
       "fcBxPortCurrentSigLosses": fcBxPortCurrentSigLosses,
       "fcBxPortCurrentPrimSeqProtoErrors": fcBxPortCurrentPrimSeqProtoErrors,
       "fcBxPortCurrentInvalidTxWords": fcBxPortCurrentInvalidTxWords,
       "fcBxPortCurrentInvalidCrcs": fcBxPortCurrentInvalidCrcs,
       "fcBxPortCurrentDelimiterErrors": fcBxPortCurrentDelimiterErrors,
       "fcBxPortCurrentRxFlowControl": fcBxPortCurrentRxFlowControl,
       "fcBxPortCurrentTxFlowControl": fcBxPortCurrentTxFlowControl,
       "fcBxPortCurrentRxOctets": fcBxPortCurrentRxOctets,
       "fcBxPortCurrentRxPkts": fcBxPortCurrentRxPkts,
       "fcBxPortCurrentTxOctets": fcBxPortCurrentTxOctets,
       "fcBxPortCurrentTxPkts": fcBxPortCurrentTxPkts,
       "fcBxPortCurrentRxLinkReset": fcBxPortCurrentRxLinkReset,
       "fcBxPortCurrentTxLinkReset": fcBxPortCurrentTxLinkReset,
       "fcBxPortCurrentRxOls": fcBxPortCurrentRxOls,
       "fcBxPortCurrentTxOls": fcBxPortCurrentTxOls,
       "fcBxPortCurrentRxErroredBbwHeaders": fcBxPortCurrentRxErroredBbwHeaders,
       "fcBxPortCurrentRxC2FramesDiscarded": fcBxPortCurrentRxC2FramesDiscarded,
       "fcBxPortCurrentTxC2Octets": fcBxPortCurrentTxC2Octets,
       "fcBxPortCurrentTxC2Packets": fcBxPortCurrentTxC2Packets,
       "fcBxPortCurrentRxC2Octets": fcBxPortCurrentRxC2Octets,
       "fcBxPortCurrentRxC2Packets": fcBxPortCurrentRxC2Packets,
       "fcBxPortCurrentRxC2ErroredSizeFrames": fcBxPortCurrentRxC2ErroredSizeFrames,
       "fcBxPortCurrentRxC3FramesDiscarded": fcBxPortCurrentRxC3FramesDiscarded,
       "fcBxPortCurrentTxC3Octets": fcBxPortCurrentTxC3Octets,
       "fcBxPortCurrentTxC3Packets": fcBxPortCurrentTxC3Packets,
       "fcBxPortCurrentRxC3Octets": fcBxPortCurrentRxC3Octets,
       "fcBxPortCurrentRxC3Packets": fcBxPortCurrentRxC3Packets,
       "fcBxPortCurrentRxC3ErroredSizeFrames": fcBxPortCurrentRxC3ErroredSizeFrames,
       "fcBxPortCurrentTxC4Octets": fcBxPortCurrentTxC4Octets,
       "fcBxPortCurrentTxC4Packets": fcBxPortCurrentTxC4Packets,
       "fcBxPortCurrentRxC4Octets": fcBxPortCurrentRxC4Octets,
       "fcBxPortCurrentRxC4Packets": fcBxPortCurrentRxC4Packets,
       "fcBxPortCurrentRxC4ErroredSizeFrames": fcBxPortCurrentRxC4ErroredSizeFrames,
       "fcBxPortCurrentTxCFOctets": fcBxPortCurrentTxCFOctets,
       "fcBxPortCurrentTxCFPackets": fcBxPortCurrentTxCFPackets,
       "fcBxPortCurrentRxCFOctets": fcBxPortCurrentRxCFOctets,
       "fcBxPortCurrentRxCFPackets": fcBxPortCurrentRxCFPackets,
       "fcBxPortCurrentRxCFErroredSizeFrame": fcBxPortCurrentRxCFErroredSizeFrame,
       "fcBxPortIntervalTable": fcBxPortIntervalTable,
       "fcBxPortIntervalEntry": fcBxPortIntervalEntry,
       "fcBxPortIntervalIndex": fcBxPortIntervalIndex,
       "fcBxPortIntervalNumber": fcBxPortIntervalNumber,
       "fcBxPortIntervalLinkFailures": fcBxPortIntervalLinkFailures,
       "fcBxPortIntervalSyncLosses": fcBxPortIntervalSyncLosses,
       "fcBxPortIntervalSigLosses": fcBxPortIntervalSigLosses,
       "fcBxPortIntervalPrimSeqProtoErrors": fcBxPortIntervalPrimSeqProtoErrors,
       "fcBxPortIntervalInvalidTxWords": fcBxPortIntervalInvalidTxWords,
       "fcBxPortIntervalInvalidCrcs": fcBxPortIntervalInvalidCrcs,
       "fcBxPortIntervalDelimiterErrors": fcBxPortIntervalDelimiterErrors,
       "fcBxPortIntervalRxFlowControl": fcBxPortIntervalRxFlowControl,
       "fcBxPortIntervalTxFlowControl": fcBxPortIntervalTxFlowControl,
       "fcBxPortIntervalRxOctets": fcBxPortIntervalRxOctets,
       "fcBxPortIntervalRxPkts": fcBxPortIntervalRxPkts,
       "fcBxPortIntervalTxOctets": fcBxPortIntervalTxOctets,
       "fcBxPortIntervalTxPkts": fcBxPortIntervalTxPkts,
       "fcBxPortIntervalRxLinkReset": fcBxPortIntervalRxLinkReset,
       "fcBxPortIntervalTxLinkReset": fcBxPortIntervalTxLinkReset,
       "fcBxPortIntervalRxOls": fcBxPortIntervalRxOls,
       "fcBxPortIntervalTxOls": fcBxPortIntervalTxOls,
       "fcBxPortIntervalRxErroredBbwHeaders": fcBxPortIntervalRxErroredBbwHeaders,
       "fcBxPortIntervalRxC2FramesDiscarded": fcBxPortIntervalRxC2FramesDiscarded,
       "fcBxPortIntervalTxC2Octets": fcBxPortIntervalTxC2Octets,
       "fcBxPortIntervalTxC2Packets": fcBxPortIntervalTxC2Packets,
       "fcBxPortIntervalRxC2Octets": fcBxPortIntervalRxC2Octets,
       "fcBxPortIntervalRxC2Packets": fcBxPortIntervalRxC2Packets,
       "fcBxPortIntervalRxC2ErroredSizeFrames": fcBxPortIntervalRxC2ErroredSizeFrames,
       "fcBxPortIntervalRxC3FramesDiscarded": fcBxPortIntervalRxC3FramesDiscarded,
       "fcBxPortIntervalTxC3Octets": fcBxPortIntervalTxC3Octets,
       "fcBxPortIntervalTxC3Packets": fcBxPortIntervalTxC3Packets,
       "fcBxPortIntervalRxC3Octets": fcBxPortIntervalRxC3Octets,
       "fcBxPortIntervalRxC3Packets": fcBxPortIntervalRxC3Packets,
       "fcBxPortIntervalRxC3ErroredSizeFrames": fcBxPortIntervalRxC3ErroredSizeFrames,
       "fcBxPortIntervalTxC4Octets": fcBxPortIntervalTxC4Octets,
       "fcBxPortIntervalTxC4Packets": fcBxPortIntervalTxC4Packets,
       "fcBxPortIntervalRxC4Octets": fcBxPortIntervalRxC4Octets,
       "fcBxPortIntervalRxC4Packets": fcBxPortIntervalRxC4Packets,
       "fcBxPortIntervalRxC4ErroredSizeFrames": fcBxPortIntervalRxC4ErroredSizeFrames,
       "fcBxPortIntervalTxCFOctets": fcBxPortIntervalTxCFOctets,
       "fcBxPortIntervalTxCFPackets": fcBxPortIntervalTxCFPackets,
       "fcBxPortIntervalRxCFOctets": fcBxPortIntervalRxCFOctets,
       "fcBxPortIntervalRxCFPackets": fcBxPortIntervalRxCFPackets,
       "fcBxPortIntervalRxCFErroredSizeFrame": fcBxPortIntervalRxCFErroredSizeFrame,
       "fcBxPortIntervalValidData": fcBxPortIntervalValidData,
       "fcBxPortTotalTable": fcBxPortTotalTable,
       "fcBxPortTotalEntry": fcBxPortTotalEntry,
       "fcBxPortTotalIndex": fcBxPortTotalIndex,
       "fcBxPortTotalDayNumber": fcBxPortTotalDayNumber,
       "fcBxPortTotalLinkFailures": fcBxPortTotalLinkFailures,
       "fcBxPortTotalSyncLosses": fcBxPortTotalSyncLosses,
       "fcBxPortTotalSigLosses": fcBxPortTotalSigLosses,
       "fcBxPortTotalPrimSeqProtoErrors": fcBxPortTotalPrimSeqProtoErrors,
       "fcBxPortTotalInvalidTxWords": fcBxPortTotalInvalidTxWords,
       "fcBxPortTotalInvalidCrcs": fcBxPortTotalInvalidCrcs,
       "fcBxPortTotalDelimiterErrors": fcBxPortTotalDelimiterErrors,
       "fcBxPortTotalRxFlowControl": fcBxPortTotalRxFlowControl,
       "fcBxPortTotalTxFlowControl": fcBxPortTotalTxFlowControl,
       "fcBxPortTotalRxOctets": fcBxPortTotalRxOctets,
       "fcBxPortTotalRxPkts": fcBxPortTotalRxPkts,
       "fcBxPortTotalTxOctets": fcBxPortTotalTxOctets,
       "fcBxPortTotalTxPkts": fcBxPortTotalTxPkts,
       "fcBxPortTotalRxLinkReset": fcBxPortTotalRxLinkReset,
       "fcBxPortTotalTxLinkReset": fcBxPortTotalTxLinkReset,
       "fcBxPortTotalRxOls": fcBxPortTotalRxOls,
       "fcBxPortTotalTxOls": fcBxPortTotalTxOls,
       "fcBxPortTotalRxErroredBbwHeaders": fcBxPortTotalRxErroredBbwHeaders,
       "fcBxPortTotalRxC2FramesDiscarded": fcBxPortTotalRxC2FramesDiscarded,
       "fcBxPortTotalTxC2Octets": fcBxPortTotalTxC2Octets,
       "fcBxPortTotalTxC2Packets": fcBxPortTotalTxC2Packets,
       "fcBxPortTotalRxC2Octets": fcBxPortTotalRxC2Octets,
       "fcBxPortTotalRxC2Packets": fcBxPortTotalRxC2Packets,
       "fcBxPortTotalRxC2ErroredSizeFrames": fcBxPortTotalRxC2ErroredSizeFrames,
       "fcBxPortTotalRxC3FramesDiscarded": fcBxPortTotalRxC3FramesDiscarded,
       "fcBxPortTotalTxC3Octets": fcBxPortTotalTxC3Octets,
       "fcBxPortTotalTxC3Packets": fcBxPortTotalTxC3Packets,
       "fcBxPortTotalRxC3Octets": fcBxPortTotalRxC3Octets,
       "fcBxPortTotalRxC3Packets": fcBxPortTotalRxC3Packets,
       "fcBxPortTotalRxC3ErroredSizeFrames": fcBxPortTotalRxC3ErroredSizeFrames,
       "fcBxPortTotalTxC4Octets": fcBxPortTotalTxC4Octets,
       "fcBxPortTotalTxC4Packets": fcBxPortTotalTxC4Packets,
       "fcBxPortTotalRxC4Octets": fcBxPortTotalRxC4Octets,
       "fcBxPortTotalRxC4Packets": fcBxPortTotalRxC4Packets,
       "fcBxPortTotalRxC4ErroredSizeFrames": fcBxPortTotalRxC4ErroredSizeFrames,
       "fcBxPortTotalTxCFOctets": fcBxPortTotalTxCFOctets,
       "fcBxPortTotalTxCFPackets": fcBxPortTotalTxCFPackets,
       "fcBxPortTotalRxCFOctets": fcBxPortTotalRxCFOctets,
       "fcBxPortTotalRxCFPackets": fcBxPortTotalRxCFPackets,
       "fcBxPortTotalRxCFErroredSizeFrame": fcBxPortTotalRxCFErroredSizeFrame,
       "fcBxPortTotalValidData": fcBxPortTotalValidData,
       "fcBxTraps": fcBxTraps,
       "fcBxPortStatusChange": fcBxPortStatusChange,
       "fcBxPortLinkRestart": fcBxPortLinkRestart}
)
