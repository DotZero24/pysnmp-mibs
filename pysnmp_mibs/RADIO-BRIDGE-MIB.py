# SNMP MIB module (RADIO-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siklu/RADIO-BRIDGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:16 2025
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

(dot1agCfmMepEntry,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMepEntry")

(ieee8021QBridgeTpFdbEntry,) = mibBuilder.importSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    "ieee8021QBridgeTpFdbEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class ModulationName(TextualConvention, Integer32):
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("qpsk1", 1),
          ("qpsk2", 2),
          ("qpsk3", 3),
          ("qam16", 4),
          ("qam64", 5),
          ("qam32", 6),
          ("bpsk1", 7),
          ("bpsk2", 8),
          ("qam128", 9),
          ("m8psk", 10))
    )



class ExtendMmPathOperStatus(TextualConvention, Integer32):
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
        *(("down", 0),
          ("active", 1),
          ("standby", 2),
          ("forced-active", 3),
          ("forced-standby", 4))
    )



class AlarmSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("no-alarm", 5))
    )



class AlarmType(TextualConvention, Integer32):
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
              8,
              9,
              10,
              11,
              12,
              13,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 1),
          ("temperature-out-of-range", 2),
          ("synthesizer-unlock", 3),
          ("pow-low", 4),
          ("cfm-mep-defect", 5),
          ("loopback-active", 6),
          ("tx-mute", 7),
          ("ql-eec1-or-worse", 8),
          ("poe-incompatible", 9),
          ("rssi-out-of-range", 10),
          ("cinr-out-of-range", 11),
          ("lowest-modulation", 12),
          ("pse-error", 13),
          ("sfp-ddm-tx-power-low", 18),
          ("sfp-ddm-tx-power-high", 19),
          ("sfp-ddm-bias-low", 20),
          ("sfp-ddm-bias-high", 21),
          ("sfp-ddm-vcc-low", 22),
          ("sfp-ddm-vcc-high", 23),
          ("sfp-ddm-temperature-low", 24),
          ("sfp-ddm-temperature-high", 25),
          ("sfp-ddm-rx-power-low", 26),
          ("sfp-ddm-rx-power-high", 27))
    )



class MhBridgePort(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d.2d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class MhBridgePortsList(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d."


class RulesVlansList(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d."


# MIB Managed Objects in the order of their OIDs

_RadioBridgeRoot_ObjectIdentity = ObjectIdentity
radioBridgeRoot = _RadioBridgeRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926)
)
_RadioBridgeSystem_ObjectIdentity = ObjectIdentity
radioBridgeSystem = _RadioBridgeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 1)
)
_RbSysVoltage_Type = Integer32
_RbSysVoltage_Object = MibScalar
rbSysVoltage = _RbSysVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 1),
    _RbSysVoltage_Type()
)
rbSysVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysVoltage.setStatus("current")
_RbSysTemperature_Type = Integer32
_RbSysTemperature_Object = MibScalar
rbSysTemperature = _RbSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 2),
    _RbSysTemperature_Type()
)
rbSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysTemperature.setStatus("current")
_RbSysSaveConfiguration_Type = Integer32
_RbSysSaveConfiguration_Object = MibScalar
rbSysSaveConfiguration = _RbSysSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 3),
    _RbSysSaveConfiguration_Type()
)
rbSysSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSysSaveConfiguration.setStatus("current")
_RbSysReset_Type = Integer32
_RbSysReset_Object = MibScalar
rbSysReset = _RbSysReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 4),
    _RbSysReset_Type()
)
rbSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSysReset.setStatus("current")
_RbSwBank1Version_Type = DisplayString
_RbSwBank1Version_Object = MibScalar
rbSwBank1Version = _RbSwBank1Version_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 5),
    _RbSwBank1Version_Type()
)
rbSwBank1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank1Version.setStatus("current")
_RbSwBank2Version_Type = DisplayString
_RbSwBank2Version_Object = MibScalar
rbSwBank2Version = _RbSwBank2Version_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 6),
    _RbSwBank2Version_Type()
)
rbSwBank2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank2Version.setStatus("current")


class _RbSwBank1Running_Type(Integer32):
    """Custom type rbSwBank1Running based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRunning", 1),
          ("running", 2),
          ("running-wait-accept", 3))
    )


_RbSwBank1Running_Type.__name__ = "Integer32"
_RbSwBank1Running_Object = MibScalar
rbSwBank1Running = _RbSwBank1Running_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 7),
    _RbSwBank1Running_Type()
)
rbSwBank1Running.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank1Running.setStatus("current")


class _RbSwBank2Running_Type(Integer32):
    """Custom type rbSwBank2Running based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRunning", 1),
          ("running", 2),
          ("running-wait-accept", 3))
    )


_RbSwBank2Running_Type.__name__ = "Integer32"
_RbSwBank2Running_Object = MibScalar
rbSwBank2Running = _RbSwBank2Running_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 8),
    _RbSwBank2Running_Type()
)
rbSwBank2Running.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank2Running.setStatus("current")
_RbSwBank1ScheduledToRunNextReset_Type = TruthValue
_RbSwBank1ScheduledToRunNextReset_Object = MibScalar
rbSwBank1ScheduledToRunNextReset = _RbSwBank1ScheduledToRunNextReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 9),
    _RbSwBank1ScheduledToRunNextReset_Type()
)
rbSwBank1ScheduledToRunNextReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank1ScheduledToRunNextReset.setStatus("current")
_RbSwBank2ScheduledToRunNextReset_Type = TruthValue
_RbSwBank2ScheduledToRunNextReset_Object = MibScalar
rbSwBank2ScheduledToRunNextReset = _RbSwBank2ScheduledToRunNextReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 10),
    _RbSwBank2ScheduledToRunNextReset_Type()
)
rbSwBank2ScheduledToRunNextReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank2ScheduledToRunNextReset.setStatus("current")
_RbSystemUpAbsoluteTime_Type = Counter64
_RbSystemUpAbsoluteTime_Object = MibScalar
rbSystemUpAbsoluteTime = _RbSystemUpAbsoluteTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 11),
    _RbSystemUpAbsoluteTime_Type()
)
rbSystemUpAbsoluteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemUpAbsoluteTime.setStatus("current")


class _RbSystemAuthenticationMode_Type(Integer32):
    """Custom type rbSystemAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_RbSystemAuthenticationMode_Type.__name__ = "Integer32"
_RbSystemAuthenticationMode_Object = MibScalar
rbSystemAuthenticationMode = _RbSystemAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 12),
    _RbSystemAuthenticationMode_Type()
)
rbSystemAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemAuthenticationMode.setStatus("current")
_RbSystemAuthenticationSecret_Type = DisplayString
_RbSystemAuthenticationSecret_Object = MibScalar
rbSystemAuthenticationSecret = _RbSystemAuthenticationSecret_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 13),
    _RbSystemAuthenticationSecret_Type()
)
rbSystemAuthenticationSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemAuthenticationSecret.setStatus("current")


class _RbSystemCapabilities_Type(Bits):
    """Custom type rbSystemCapabilities based on Bits"""
    namedValues = NamedValues(
        ("nmsFtp", 0)
    )

_RbSystemCapabilities_Type.__name__ = "Bits"
_RbSystemCapabilities_Object = MibScalar
rbSystemCapabilities = _RbSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 14),
    _RbSystemCapabilities_Type()
)
rbSystemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemCapabilities.setStatus("current")
_RbDate_Type = DisplayString
_RbDate_Object = MibScalar
rbDate = _RbDate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 15),
    _RbDate_Type()
)
rbDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbDate.setStatus("current")
_RbTime_Type = DisplayString
_RbTime_Object = MibScalar
rbTime = _RbTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 16),
    _RbTime_Type()
)
rbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTime.setStatus("current")
_RbSystemBridgeMode_Type = OctetString
_RbSystemBridgeMode_Object = MibScalar
rbSystemBridgeMode = _RbSystemBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 17),
    _RbSystemBridgeMode_Type()
)
rbSystemBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemBridgeMode.setStatus("current")
_RbSystemEthIsolation_Type = TruthValue
_RbSystemEthIsolation_Object = MibScalar
rbSystemEthIsolation = _RbSystemEthIsolation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 18),
    _RbSystemEthIsolation_Type()
)
rbSystemEthIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemEthIsolation.setStatus("current")
_RbSystemTuIsolation_Type = TruthValue
_RbSystemTuIsolation_Object = MibScalar
rbSystemTuIsolation = _RbSystemTuIsolation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 19),
    _RbSystemTuIsolation_Type()
)
rbSystemTuIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemTuIsolation.setStatus("current")
_RbSystemAdjustedDateTime_Type = DisplayString
_RbSystemAdjustedDateTime_Object = MibScalar
rbSystemAdjustedDateTime = _RbSystemAdjustedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 20),
    _RbSystemAdjustedDateTime_Type()
)
rbSystemAdjustedDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemAdjustedDateTime.setStatus("current")
_RbSystemEquipmentModel_Type = DisplayString
_RbSystemEquipmentModel_Object = MibScalar
rbSystemEquipmentModel = _RbSystemEquipmentModel_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 30),
    _RbSystemEquipmentModel_Type()
)
rbSystemEquipmentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemEquipmentModel.setStatus("current")
_RbSystemEquipmentSourceId_Type = OctetString
_RbSystemEquipmentSourceId_Object = MibScalar
rbSystemEquipmentSourceId = _RbSystemEquipmentSourceId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 31),
    _RbSystemEquipmentSourceId_Type()
)
rbSystemEquipmentSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemEquipmentSourceId.setStatus("current")
_RbSystemConfigChange_Type = Integer32
_RbSystemConfigChange_Object = MibScalar
rbSystemConfigChange = _RbSystemConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 32),
    _RbSystemConfigChange_Type()
)
rbSystemConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemConfigChange.setStatus("current")
_RbSystemNumOfAlarms_Type = Integer32
_RbSystemNumOfAlarms_Object = MibScalar
rbSystemNumOfAlarms = _RbSystemNumOfAlarms_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 33),
    _RbSystemNumOfAlarms_Type()
)
rbSystemNumOfAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemNumOfAlarms.setStatus("current")
_RbSystemHeartbeatPeriod_Type = Integer32
_RbSystemHeartbeatPeriod_Object = MibScalar
rbSystemHeartbeatPeriod = _RbSystemHeartbeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 34),
    _RbSystemHeartbeatPeriod_Type()
)
rbSystemHeartbeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemHeartbeatPeriod.setStatus("current")
_RbSystemIpv4List_Type = OctetString
_RbSystemIpv4List_Object = MibScalar
rbSystemIpv4List = _RbSystemIpv4List_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 35),
    _RbSystemIpv4List_Type()
)
rbSystemIpv4List.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemIpv4List.setStatus("current")
_RbSystemIpv6List_Type = OctetString
_RbSystemIpv6List_Object = MibScalar
rbSystemIpv6List = _RbSystemIpv6List_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 36),
    _RbSystemIpv6List_Type()
)
rbSystemIpv6List.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemIpv6List.setStatus("current")
_RbSystemHostname_Type = DisplayString
_RbSystemHostname_Object = MibScalar
rbSystemHostname = _RbSystemHostname_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 37),
    _RbSystemHostname_Type()
)
rbSystemHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemHostname.setStatus("current")
_RadioBridgeRf_ObjectIdentity = ObjectIdentity
radioBridgeRf = _RadioBridgeRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 2)
)
_RbRfTable_Object = MibTable
rbRfTable = _RbRfTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1)
)
if mibBuilder.loadTexts:
    rbRfTable.setStatus("current")
_RbRfEntry_Object = MibTableRow
rbRfEntry = _RbRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1)
)
rbRfEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rfIndex"),
)
if mibBuilder.loadTexts:
    rbRfEntry.setStatus("current")
_RfIndex_Type = Integer32
_RfIndex_Object = MibTableColumn
rfIndex = _RfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 1),
    _RfIndex_Type()
)
rfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfIndex.setStatus("current")


class _RfNumOfChannels_Type(Integer32):
    """Custom type rfNumOfChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_RfNumOfChannels_Type.__name__ = "Integer32"
_RfNumOfChannels_Object = MibTableColumn
rfNumOfChannels = _RfNumOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 2),
    _RfNumOfChannels_Type()
)
rfNumOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfNumOfChannels.setStatus("current")


class _RfChannelWidth_Type(Integer32):
    """Custom type rfChannelWidth based on Integer32"""
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
        *(("rfWidth250", 1),
          ("rfWidth500", 2),
          ("rfWidth750", 3),
          ("rfWidth1250", 4),
          ("rfWidth125", 5),
          ("rfWidth2000", 6))
    )


_RfChannelWidth_Type.__name__ = "Integer32"
_RfChannelWidth_Object = MibTableColumn
rfChannelWidth = _RfChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 3),
    _RfChannelWidth_Type()
)
rfChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfChannelWidth.setStatus("current")
_RfOperationalFrequency_Type = Integer32
_RfOperationalFrequency_Object = MibTableColumn
rfOperationalFrequency = _RfOperationalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 4),
    _RfOperationalFrequency_Type()
)
rfOperationalFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfOperationalFrequency.setStatus("current")


class _RfRole_Type(Integer32):
    """Custom type rfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfMaster", 1),
          ("rfSlave", 2),
          ("rfAuto", 3))
    )


_RfRole_Type.__name__ = "Integer32"
_RfRole_Object = MibTableColumn
rfRole = _RfRole_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 5),
    _RfRole_Type()
)
rfRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfRole.setStatus("current")


class _RfModeSelector_Type(Integer32):
    """Custom type rfModeSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfModeAdaptive", 1),
          ("rfModeStatic", 2),
          ("rfModeAlign", 3))
    )


_RfModeSelector_Type.__name__ = "Integer32"
_RfModeSelector_Object = MibTableColumn
rfModeSelector = _RfModeSelector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 6),
    _RfModeSelector_Type()
)
rfModeSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfModeSelector.setStatus("current")


class _RfModulationType_Type(Integer32):
    """Custom type rfModulationType based on Integer32"""
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
        *(("rfModulationQPSK", 1),
          ("rfModulationQAM-16", 2),
          ("rfModulationQAM-64", 3),
          ("rfModulationQAM-32", 4),
          ("rfModulationBPSK", 5))
    )


_RfModulationType_Type.__name__ = "Integer32"
_RfModulationType_Object = MibTableColumn
rfModulationType = _RfModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 7),
    _RfModulationType_Type()
)
rfModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfModulationType.setStatus("current")


class _RfNumOfSubchannels_Type(Integer32):
    """Custom type rfNumOfSubchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RfNumOfSubchannels_Type.__name__ = "Integer32"
_RfNumOfSubchannels_Object = MibTableColumn
rfNumOfSubchannels = _RfNumOfSubchannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 8),
    _RfNumOfSubchannels_Type()
)
rfNumOfSubchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfNumOfSubchannels.setStatus("current")


class _RfNumOfRepetitions_Type(Integer32):
    """Custom type rfNumOfRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_RfNumOfRepetitions_Type.__name__ = "Integer32"
_RfNumOfRepetitions_Object = MibTableColumn
rfNumOfRepetitions = _RfNumOfRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 9),
    _RfNumOfRepetitions_Type()
)
rfNumOfRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfNumOfRepetitions.setStatus("current")


class _RfFecRate_Type(Integer32):
    """Custom type rfFecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfFEC-05", 1),
          ("rfFEC-067", 2),
          ("rfFEC-08", 3))
    )


_RfFecRate_Type.__name__ = "Integer32"
_RfFecRate_Object = MibTableColumn
rfFecRate = _RfFecRate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 10),
    _RfFecRate_Type()
)
rfFecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfFecRate.setStatus("current")
_RfOperationalState_Type = TruthValue
_RfOperationalState_Object = MibTableColumn
rfOperationalState = _RfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 17),
    _RfOperationalState_Type()
)
rfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOperationalState.setStatus("current")
_RfAverageCinr_Type = Integer32
_RfAverageCinr_Object = MibTableColumn
rfAverageCinr = _RfAverageCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 18),
    _RfAverageCinr_Type()
)
rfAverageCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAverageCinr.setStatus("current")
_RfAverageRssi_Type = Integer32
_RfAverageRssi_Object = MibTableColumn
rfAverageRssi = _RfAverageRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 19),
    _RfAverageRssi_Type()
)
rfAverageRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAverageRssi.setStatus("current")


class _RfTxSynthLock_Type(Integer32):
    """Custom type rfTxSynthLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("txSynthUnlock", 0),
          ("txSynthLock", 1))
    )


_RfTxSynthLock_Type.__name__ = "Integer32"
_RfTxSynthLock_Object = MibTableColumn
rfTxSynthLock = _RfTxSynthLock_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 20),
    _RfTxSynthLock_Type()
)
rfTxSynthLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxSynthLock.setStatus("current")


class _RfRxSynthLock_Type(Integer32):
    """Custom type rfRxSynthLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rxSynthUnlock", 0),
          ("rxSynthLock", 1))
    )


_RfRxSynthLock_Type.__name__ = "Integer32"
_RfRxSynthLock_Object = MibTableColumn
rfRxSynthLock = _RfRxSynthLock_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 21),
    _RfRxSynthLock_Type()
)
rfRxSynthLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxSynthLock.setStatus("current")


class _RfRxLinkId_Type(Integer32):
    """Custom type rfRxLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RfRxLinkId_Type.__name__ = "Integer32"
_RfRxLinkId_Object = MibTableColumn
rfRxLinkId = _RfRxLinkId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 22),
    _RfRxLinkId_Type()
)
rfRxLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfRxLinkId.setStatus("current")


class _RfTxLinkId_Type(Integer32):
    """Custom type rfTxLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RfTxLinkId_Type.__name__ = "Integer32"
_RfTxLinkId_Object = MibTableColumn
rfTxLinkId = _RfTxLinkId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 23),
    _RfTxLinkId_Type()
)
rfTxLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxLinkId.setStatus("current")


class _RfTxState_Type(Integer32):
    """Custom type rfTxState based on Integer32"""
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
        *(("rf-sync", 1),
          ("rf-searchCountdown", 2),
          ("rf-foundCountdown", 3),
          ("rf-normal", 4))
    )


_RfTxState_Type.__name__ = "Integer32"
_RfTxState_Object = MibTableColumn
rfTxState = _RfTxState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 24),
    _RfTxState_Type()
)
rfTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxState.setStatus("current")


class _RfRxState_Type(Integer32):
    """Custom type rfRxState based on Integer32"""
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
        *(("rf-sync", 1),
          ("rf-searchCountdown", 2),
          ("rf-foundCountdown", 3),
          ("rf-normal", 4))
    )


_RfRxState_Type.__name__ = "Integer32"
_RfRxState_Object = MibTableColumn
rfRxState = _RfRxState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 25),
    _RfRxState_Type()
)
rfRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxState.setStatus("current")
_RfTemperature_Type = Integer32
_RfTemperature_Object = MibTableColumn
rfTemperature = _RfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 26),
    _RfTemperature_Type()
)
rfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTemperature.setStatus("current")


class _RfAsymmetry_Type(Integer32):
    """Custom type rfAsymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rf-asymmetry-25tx-75rx", 1),
          ("rf-asymmetry-50tx-50rx", 2),
          ("rf-asymmetry-75tx-25rx", 3))
    )


_RfAsymmetry_Type.__name__ = "Integer32"
_RfAsymmetry_Object = MibTableColumn
rfAsymmetry = _RfAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 27),
    _RfAsymmetry_Type()
)
rfAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAsymmetry.setStatus("current")


class _RfLowestModulationType_Type(Integer32):
    """Custom type rfLowestModulationType based on Integer32"""
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
        *(("rfModulationQPSK", 1),
          ("rfModulationQAM-16", 2),
          ("rfModulationQAM-64", 3),
          ("rfModulationQAM-32", 4),
          ("rfModulationBPSK", 5))
    )


_RfLowestModulationType_Type.__name__ = "Integer32"
_RfLowestModulationType_Object = MibTableColumn
rfLowestModulationType = _RfLowestModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 30),
    _RfLowestModulationType_Type()
)
rfLowestModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestModulationType.setStatus("current")


class _RfLowestNumOfSubchannels_Type(Integer32):
    """Custom type rfLowestNumOfSubchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RfLowestNumOfSubchannels_Type.__name__ = "Integer32"
_RfLowestNumOfSubchannels_Object = MibTableColumn
rfLowestNumOfSubchannels = _RfLowestNumOfSubchannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 31),
    _RfLowestNumOfSubchannels_Type()
)
rfLowestNumOfSubchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestNumOfSubchannels.setStatus("current")


class _RfLowestNumOfRepetitions_Type(Integer32):
    """Custom type rfLowestNumOfRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_RfLowestNumOfRepetitions_Type.__name__ = "Integer32"
_RfLowestNumOfRepetitions_Object = MibTableColumn
rfLowestNumOfRepetitions = _RfLowestNumOfRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 32),
    _RfLowestNumOfRepetitions_Type()
)
rfLowestNumOfRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestNumOfRepetitions.setStatus("current")


class _RfLowestFecRate_Type(Integer32):
    """Custom type rfLowestFecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfFEC-05", 1),
          ("rfFEC-067", 2),
          ("rfFEC-08", 3))
    )


_RfLowestFecRate_Type.__name__ = "Integer32"
_RfLowestFecRate_Object = MibTableColumn
rfLowestFecRate = _RfLowestFecRate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 33),
    _RfLowestFecRate_Type()
)
rfLowestFecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestFecRate.setStatus("current")
_RfTxMute_Type = TruthValue
_RfTxMute_Object = MibTableColumn
rfTxMute = _RfTxMute_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 34),
    _RfTxMute_Type()
)
rfTxMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxMute.setStatus("current")


class _RfRoleStatus_Type(Integer32):
    """Custom type rfRoleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfMaster", 1),
          ("rfSlave", 2),
          ("rfAuto", 3))
    )


_RfRoleStatus_Type.__name__ = "Integer32"
_RfRoleStatus_Object = MibTableColumn
rfRoleStatus = _RfRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 35),
    _RfRoleStatus_Type()
)
rfRoleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRoleStatus.setStatus("current")


class _RfLoopModeSelector_Type(Integer32):
    """Custom type rfLoopModeSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfLoopDisabled", 1),
          ("rfLoopInternalMacSwap", 2))
    )


_RfLoopModeSelector_Type.__name__ = "Integer32"
_RfLoopModeSelector_Object = MibTableColumn
rfLoopModeSelector = _RfLoopModeSelector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 36),
    _RfLoopModeSelector_Type()
)
rfLoopModeSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopModeSelector.setStatus("current")


class _RfLoopModulationType_Type(Integer32):
    """Custom type rfLoopModulationType based on Integer32"""
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
        *(("rfModulationQPSK", 1),
          ("rfModulationQAM-16", 2),
          ("rfModulationQAM-64", 3),
          ("rfModulationQAM-32", 4),
          ("rfModulationBPSK", 5))
    )


_RfLoopModulationType_Type.__name__ = "Integer32"
_RfLoopModulationType_Object = MibTableColumn
rfLoopModulationType = _RfLoopModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 37),
    _RfLoopModulationType_Type()
)
rfLoopModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopModulationType.setStatus("current")


class _RfLoopNumOfSubchannels_Type(Integer32):
    """Custom type rfLoopNumOfSubchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RfLoopNumOfSubchannels_Type.__name__ = "Integer32"
_RfLoopNumOfSubchannels_Object = MibTableColumn
rfLoopNumOfSubchannels = _RfLoopNumOfSubchannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 38),
    _RfLoopNumOfSubchannels_Type()
)
rfLoopNumOfSubchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopNumOfSubchannels.setStatus("current")


class _RfLoopNumOfRepetitions_Type(Integer32):
    """Custom type rfLoopNumOfRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_RfLoopNumOfRepetitions_Type.__name__ = "Integer32"
_RfLoopNumOfRepetitions_Object = MibTableColumn
rfLoopNumOfRepetitions = _RfLoopNumOfRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 39),
    _RfLoopNumOfRepetitions_Type()
)
rfLoopNumOfRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopNumOfRepetitions.setStatus("current")


class _RfLoopFecRate_Type(Integer32):
    """Custom type rfLoopFecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfFEC-05", 1),
          ("rfFEC-067", 2),
          ("rfFEC-08", 3))
    )


_RfLoopFecRate_Type.__name__ = "Integer32"
_RfLoopFecRate_Object = MibTableColumn
rfLoopFecRate = _RfLoopFecRate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 40),
    _RfLoopFecRate_Type()
)
rfLoopFecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopFecRate.setStatus("current")
_RfLoopTimeout_Type = Integer32
_RfLoopTimeout_Object = MibTableColumn
rfLoopTimeout = _RfLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 41),
    _RfLoopTimeout_Type()
)
rfLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopTimeout.setStatus("current")
_RfTxPower_Type = Integer32
_RfTxPower_Object = MibTableColumn
rfTxPower = _RfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 42),
    _RfTxPower_Type()
)
rfTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxPower.setStatus("current")


class _RfTxMuteTimeout_Type(Integer32):
    """Custom type rfTxMuteTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_RfTxMuteTimeout_Type.__name__ = "Integer32"
_RfTxMuteTimeout_Object = MibTableColumn
rfTxMuteTimeout = _RfTxMuteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 43),
    _RfTxMuteTimeout_Type()
)
rfTxMuteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxMuteTimeout.setStatus("current")


class _RfAlignmentStatus_Type(Integer32):
    """Custom type rfAlignmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfAlignmentInactive", 0),
          ("rfAlignmentActive", 1))
    )


_RfAlignmentStatus_Type.__name__ = "Integer32"
_RfAlignmentStatus_Object = MibTableColumn
rfAlignmentStatus = _RfAlignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 44),
    _RfAlignmentStatus_Type()
)
rfAlignmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAlignmentStatus.setStatus("current")


class _RfLoopDirection_Type(Integer32):
    """Custom type rfLoopDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfLoop-tx", 1),
          ("rfLoop-rx", 2))
    )


_RfLoopDirection_Type.__name__ = "Integer32"
_RfLoopDirection_Object = MibTableColumn
rfLoopDirection = _RfLoopDirection_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 45),
    _RfLoopDirection_Type()
)
rfLoopDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopDirection.setStatus("current")
_RfModulationName_Type = ModulationName
_RfModulationName_Object = MibTableColumn
rfModulationName = _RfModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 46),
    _RfModulationName_Type()
)
rfModulationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfModulationName.setStatus("current")
_RfLowestModulationName_Type = ModulationName
_RfLowestModulationName_Object = MibTableColumn
rfLowestModulationName = _RfLowestModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 47),
    _RfLowestModulationName_Type()
)
rfLowestModulationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestModulationName.setStatus("current")
_RfLoopModulationName_Type = ModulationName
_RfLoopModulationName_Object = MibTableColumn
rfLoopModulationName = _RfLoopModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 48),
    _RfLoopModulationName_Type()
)
rfLoopModulationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopModulationName.setStatus("current")
_RfAverageCinrFractional_Type = Integer32
_RfAverageCinrFractional_Object = MibTableColumn
rfAverageCinrFractional = _RfAverageCinrFractional_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 49),
    _RfAverageCinrFractional_Type()
)
rfAverageCinrFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAverageCinrFractional.setStatus("current")
_RfAirCapacity_Type = Integer32
_RfAirCapacity_Object = MibTableColumn
rfAirCapacity = _RfAirCapacity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 50),
    _RfAirCapacity_Type()
)
rfAirCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAirCapacity.setStatus("current")
_RfRxFrequency_Type = Integer32
_RfRxFrequency_Object = MibTableColumn
rfRxFrequency = _RfRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 51),
    _RfRxFrequency_Type()
)
rfRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxFrequency.setStatus("current")
_RbRfStatisticsTable_Object = MibTable
rbRfStatisticsTable = _RbRfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2)
)
if mibBuilder.loadTexts:
    rbRfStatisticsTable.setStatus("current")
_RbRfStatisticsEntry_Object = MibTableRow
rbRfStatisticsEntry = _RbRfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1)
)
rbRfStatisticsEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rfIndex"),
)
if mibBuilder.loadTexts:
    rbRfStatisticsEntry.setStatus("current")
_RfInOctets_Type = Counter64
_RfInOctets_Object = MibTableColumn
rfInOctets = _RfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 1),
    _RfInOctets_Type()
)
rfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInOctets.setStatus("current")
_RfInIdleOctets_Type = Counter64
_RfInIdleOctets_Object = MibTableColumn
rfInIdleOctets = _RfInIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 2),
    _RfInIdleOctets_Type()
)
rfInIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInIdleOctets.setStatus("current")
_RfInGoodOctets_Type = Counter64
_RfInGoodOctets_Object = MibTableColumn
rfInGoodOctets = _RfInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 3),
    _RfInGoodOctets_Type()
)
rfInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInGoodOctets.setStatus("current")
_RfInErroredOctets_Type = Counter64
_RfInErroredOctets_Object = MibTableColumn
rfInErroredOctets = _RfInErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 4),
    _RfInErroredOctets_Type()
)
rfInErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInErroredOctets.setStatus("current")
_RfOutOctets_Type = Counter64
_RfOutOctets_Object = MibTableColumn
rfOutOctets = _RfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 5),
    _RfOutOctets_Type()
)
rfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutOctets.setStatus("current")
_RfOutIdleOctets_Type = Counter64
_RfOutIdleOctets_Object = MibTableColumn
rfOutIdleOctets = _RfOutIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 6),
    _RfOutIdleOctets_Type()
)
rfOutIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutIdleOctets.setStatus("current")
_RfInPkts_Type = Counter64
_RfInPkts_Object = MibTableColumn
rfInPkts = _RfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 7),
    _RfInPkts_Type()
)
rfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInPkts.setStatus("current")
_RfInGoodPkts_Type = Counter64
_RfInGoodPkts_Object = MibTableColumn
rfInGoodPkts = _RfInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 8),
    _RfInGoodPkts_Type()
)
rfInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInGoodPkts.setStatus("current")
_RfInErroredPkts_Type = Counter64
_RfInErroredPkts_Object = MibTableColumn
rfInErroredPkts = _RfInErroredPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 9),
    _RfInErroredPkts_Type()
)
rfInErroredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInErroredPkts.setStatus("current")
_RfInLostPkts_Type = Counter64
_RfInLostPkts_Object = MibTableColumn
rfInLostPkts = _RfInLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 10),
    _RfInLostPkts_Type()
)
rfInLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInLostPkts.setStatus("current")
_RfOutPkts_Type = Counter64
_RfOutPkts_Object = MibTableColumn
rfOutPkts = _RfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 11),
    _RfOutPkts_Type()
)
rfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutPkts.setStatus("current")
_RfMinCinr_Type = Counter64
_RfMinCinr_Object = MibTableColumn
rfMinCinr = _RfMinCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 15),
    _RfMinCinr_Type()
)
rfMinCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinCinr.setStatus("current")
_RfMaxCinr_Type = Counter64
_RfMaxCinr_Object = MibTableColumn
rfMaxCinr = _RfMaxCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 16),
    _RfMaxCinr_Type()
)
rfMaxCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxCinr.setStatus("current")
_RfMinRssi_Type = Counter64
_RfMinRssi_Object = MibTableColumn
rfMinRssi = _RfMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 17),
    _RfMinRssi_Type()
)
rfMinRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinRssi.setStatus("current")
_RfMaxRssi_Type = Counter64
_RfMaxRssi_Object = MibTableColumn
rfMaxRssi = _RfMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 18),
    _RfMaxRssi_Type()
)
rfMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxRssi.setStatus("current")
_RfMinModulation_Type = Counter64
_RfMinModulation_Object = MibTableColumn
rfMinModulation = _RfMinModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 19),
    _RfMinModulation_Type()
)
rfMinModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinModulation.setStatus("current")
_RfMaxModulation_Type = Counter64
_RfMaxModulation_Object = MibTableColumn
rfMaxModulation = _RfMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 20),
    _RfMaxModulation_Type()
)
rfMaxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxModulation.setStatus("current")
_RfValid_Type = TruthValue
_RfValid_Object = MibTableColumn
rfValid = _RfValid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 21),
    _RfValid_Type()
)
rfValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfValid.setStatus("current")
_RfArqInLoss_Type = Counter64
_RfArqInLoss_Object = MibTableColumn
rfArqInLoss = _RfArqInLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 22),
    _RfArqInLoss_Type()
)
rfArqInLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfArqInLoss.setStatus("current")
_RfArqOutLoss_Type = Counter64
_RfArqOutLoss_Object = MibTableColumn
rfArqOutLoss = _RfArqOutLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 23),
    _RfArqOutLoss_Type()
)
rfArqOutLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfArqOutLoss.setStatus("current")
_RfMinModulationName_Type = Counter64
_RfMinModulationName_Object = MibTableColumn
rfMinModulationName = _RfMinModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 24),
    _RfMinModulationName_Type()
)
rfMinModulationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinModulationName.setStatus("current")
_RfMaxModulationName_Type = Counter64
_RfMaxModulationName_Object = MibTableColumn
rfMaxModulationName = _RfMaxModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 25),
    _RfMaxModulationName_Type()
)
rfMaxModulationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxModulationName.setStatus("current")
_RfMinCinrFractional_Type = Counter64
_RfMinCinrFractional_Object = MibTableColumn
rfMinCinrFractional = _RfMinCinrFractional_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 26),
    _RfMinCinrFractional_Type()
)
rfMinCinrFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinCinrFractional.setStatus("current")
_RfMaxCinrFractional_Type = Counter64
_RfMaxCinrFractional_Object = MibTableColumn
rfMaxCinrFractional = _RfMaxCinrFractional_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 27),
    _RfMaxCinrFractional_Type()
)
rfMaxCinrFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxCinrFractional.setStatus("current")
_RfUptime_Type = Counter64
_RfUptime_Object = MibTableColumn
rfUptime = _RfUptime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 28),
    _RfUptime_Type()
)
rfUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfUptime.setStatus("current")
_RbRfStatisticsDaysTable_Object = MibTable
rbRfStatisticsDaysTable = _RbRfStatisticsDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3)
)
if mibBuilder.loadTexts:
    rbRfStatisticsDaysTable.setStatus("current")
_RbRfStatisticsDaysEntry_Object = MibTableRow
rbRfStatisticsDaysEntry = _RbRfStatisticsDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1)
)
rbRfStatisticsDaysEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rfIndex"),
    (0, "RADIO-BRIDGE-MIB", "rfDayIndex"),
)
if mibBuilder.loadTexts:
    rbRfStatisticsDaysEntry.setStatus("current")
_RfDaysInOctets_Type = Counter64
_RfDaysInOctets_Object = MibTableColumn
rfDaysInOctets = _RfDaysInOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 1),
    _RfDaysInOctets_Type()
)
rfDaysInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInOctets.setStatus("current")
_RfDaysInIdleOctets_Type = Counter64
_RfDaysInIdleOctets_Object = MibTableColumn
rfDaysInIdleOctets = _RfDaysInIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 2),
    _RfDaysInIdleOctets_Type()
)
rfDaysInIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInIdleOctets.setStatus("current")
_RfDaysInGoodOctets_Type = Counter64
_RfDaysInGoodOctets_Object = MibTableColumn
rfDaysInGoodOctets = _RfDaysInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 3),
    _RfDaysInGoodOctets_Type()
)
rfDaysInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInGoodOctets.setStatus("current")
_RfDaysInErroredOctets_Type = Counter64
_RfDaysInErroredOctets_Object = MibTableColumn
rfDaysInErroredOctets = _RfDaysInErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 4),
    _RfDaysInErroredOctets_Type()
)
rfDaysInErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInErroredOctets.setStatus("current")
_RfDaysOutOctets_Type = Counter64
_RfDaysOutOctets_Object = MibTableColumn
rfDaysOutOctets = _RfDaysOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 5),
    _RfDaysOutOctets_Type()
)
rfDaysOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysOutOctets.setStatus("current")
_RfDaysOutIdleOctets_Type = Counter64
_RfDaysOutIdleOctets_Object = MibTableColumn
rfDaysOutIdleOctets = _RfDaysOutIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 6),
    _RfDaysOutIdleOctets_Type()
)
rfDaysOutIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysOutIdleOctets.setStatus("current")
_RfDaysInPkts_Type = Counter64
_RfDaysInPkts_Object = MibTableColumn
rfDaysInPkts = _RfDaysInPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 7),
    _RfDaysInPkts_Type()
)
rfDaysInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInPkts.setStatus("current")
_RfDaysInGoodPkts_Type = Counter64
_RfDaysInGoodPkts_Object = MibTableColumn
rfDaysInGoodPkts = _RfDaysInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 8),
    _RfDaysInGoodPkts_Type()
)
rfDaysInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInGoodPkts.setStatus("current")
_RfDaysInErroredPkts_Type = Counter64
_RfDaysInErroredPkts_Object = MibTableColumn
rfDaysInErroredPkts = _RfDaysInErroredPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 9),
    _RfDaysInErroredPkts_Type()
)
rfDaysInErroredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInErroredPkts.setStatus("current")
_RfDaysInLostPkts_Type = Counter64
_RfDaysInLostPkts_Object = MibTableColumn
rfDaysInLostPkts = _RfDaysInLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 10),
    _RfDaysInLostPkts_Type()
)
rfDaysInLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInLostPkts.setStatus("current")
_RfDaysOutPkts_Type = Counter64
_RfDaysOutPkts_Object = MibTableColumn
rfDaysOutPkts = _RfDaysOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 11),
    _RfDaysOutPkts_Type()
)
rfDaysOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysOutPkts.setStatus("current")
_RfDaysMinCinr_Type = Counter64
_RfDaysMinCinr_Object = MibTableColumn
rfDaysMinCinr = _RfDaysMinCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 15),
    _RfDaysMinCinr_Type()
)
rfDaysMinCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinCinr.setStatus("current")
_RfDaysMaxCinr_Type = Counter64
_RfDaysMaxCinr_Object = MibTableColumn
rfDaysMaxCinr = _RfDaysMaxCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 16),
    _RfDaysMaxCinr_Type()
)
rfDaysMaxCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxCinr.setStatus("current")
_RfDaysMinRssi_Type = Counter64
_RfDaysMinRssi_Object = MibTableColumn
rfDaysMinRssi = _RfDaysMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 17),
    _RfDaysMinRssi_Type()
)
rfDaysMinRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinRssi.setStatus("current")
_RfDaysMaxRssi_Type = Counter64
_RfDaysMaxRssi_Object = MibTableColumn
rfDaysMaxRssi = _RfDaysMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 18),
    _RfDaysMaxRssi_Type()
)
rfDaysMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxRssi.setStatus("current")
_RfDaysMinModulation_Type = Counter64
_RfDaysMinModulation_Object = MibTableColumn
rfDaysMinModulation = _RfDaysMinModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 19),
    _RfDaysMinModulation_Type()
)
rfDaysMinModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinModulation.setStatus("current")
_RfDaysMaxModulation_Type = Counter64
_RfDaysMaxModulation_Object = MibTableColumn
rfDaysMaxModulation = _RfDaysMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 20),
    _RfDaysMaxModulation_Type()
)
rfDaysMaxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxModulation.setStatus("current")
_RfDaysValid_Type = TruthValue
_RfDaysValid_Object = MibTableColumn
rfDaysValid = _RfDaysValid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 21),
    _RfDaysValid_Type()
)
rfDaysValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysValid.setStatus("current")
_RfDaysArqInLoss_Type = Counter64
_RfDaysArqInLoss_Object = MibTableColumn
rfDaysArqInLoss = _RfDaysArqInLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 22),
    _RfDaysArqInLoss_Type()
)
rfDaysArqInLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysArqInLoss.setStatus("current")
_RfDaysArqOutLoss_Type = Counter64
_RfDaysArqOutLoss_Object = MibTableColumn
rfDaysArqOutLoss = _RfDaysArqOutLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 23),
    _RfDaysArqOutLoss_Type()
)
rfDaysArqOutLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysArqOutLoss.setStatus("current")
_RfDaysMinModulationName_Type = Counter64
_RfDaysMinModulationName_Object = MibTableColumn
rfDaysMinModulationName = _RfDaysMinModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 24),
    _RfDaysMinModulationName_Type()
)
rfDaysMinModulationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinModulationName.setStatus("current")
_RfDaysMaxModulationName_Type = Counter64
_RfDaysMaxModulationName_Object = MibTableColumn
rfDaysMaxModulationName = _RfDaysMaxModulationName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 25),
    _RfDaysMaxModulationName_Type()
)
rfDaysMaxModulationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxModulationName.setStatus("current")
_RfDaysMinCinrFractional_Type = Counter64
_RfDaysMinCinrFractional_Object = MibTableColumn
rfDaysMinCinrFractional = _RfDaysMinCinrFractional_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 26),
    _RfDaysMinCinrFractional_Type()
)
rfDaysMinCinrFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinCinrFractional.setStatus("current")
_RfDaysMaxCinrFractional_Type = Counter64
_RfDaysMaxCinrFractional_Object = MibTableColumn
rfDaysMaxCinrFractional = _RfDaysMaxCinrFractional_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 27),
    _RfDaysMaxCinrFractional_Type()
)
rfDaysMaxCinrFractional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxCinrFractional.setStatus("current")
_RfDayIndex_Type = Integer32
_RfDayIndex_Object = MibTableColumn
rfDayIndex = _RfDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 50),
    _RfDayIndex_Type()
)
rfDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfDayIndex.setStatus("current")
_RfDaysStart_Type = TimeTicks
_RfDaysStart_Object = MibTableColumn
rfDaysStart = _RfDaysStart_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 51),
    _RfDaysStart_Type()
)
rfDaysStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfDaysStart.setStatus("current")
_RadioBridgeTraps_ObjectIdentity = ObjectIdentity
radioBridgeTraps = _RadioBridgeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 3)
)
_RadioBridgeRefClock_ObjectIdentity = ObjectIdentity
radioBridgeRefClock = _RadioBridgeRefClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 4)
)
_RbRefClockTable_Object = MibTable
rbRefClockTable = _RbRefClockTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1)
)
if mibBuilder.loadTexts:
    rbRefClockTable.setStatus("current")
_RbRefClockEntry_Object = MibTableRow
rbRefClockEntry = _RbRefClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1)
)
rbRefClockEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbRefClockEntry.setStatus("current")


class _RefClockPrio_Type(Integer32):
    """Custom type refClockPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RefClockPrio_Type.__name__ = "Integer32"
_RefClockPrio_Object = MibTableColumn
refClockPrio = _RefClockPrio_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 1),
    _RefClockPrio_Type()
)
refClockPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockPrio.setStatus("current")


class _RefClockStatus_Type(Integer32):
    """Custom type refClockStatus based on Integer32"""
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
        *(("down", 0),
          ("active", 1),
          ("backup-1", 2),
          ("backup-2", 3),
          ("backup-3", 4))
    )


_RefClockStatus_Type.__name__ = "Integer32"
_RefClockStatus_Object = MibTableColumn
refClockStatus = _RefClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 2),
    _RefClockStatus_Type()
)
refClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refClockStatus.setStatus("current")


class _RefClockQualityLevelActual_Type(Integer32):
    """Custom type refClockQualityLevelActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RefClockQualityLevelActual_Type.__name__ = "Integer32"
_RefClockQualityLevelActual_Object = MibTableColumn
refClockQualityLevelActual = _RefClockQualityLevelActual_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 3),
    _RefClockQualityLevelActual_Type()
)
refClockQualityLevelActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refClockQualityLevelActual.setStatus("current")


class _RefClockQualityLevelConfig_Type(Integer32):
    """Custom type refClockQualityLevelConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RefClockQualityLevelConfig_Type.__name__ = "Integer32"
_RefClockQualityLevelConfig_Object = MibTableColumn
refClockQualityLevelConfig = _RefClockQualityLevelConfig_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 4),
    _RefClockQualityLevelConfig_Type()
)
refClockQualityLevelConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockQualityLevelConfig.setStatus("current")
_RefClockQualityLevelMode_Type = TruthValue
_RefClockQualityLevelMode_Object = MibTableColumn
refClockQualityLevelMode = _RefClockQualityLevelMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 5),
    _RefClockQualityLevelMode_Type()
)
refClockQualityLevelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockQualityLevelMode.setStatus("current")
_RefClockSsmCvid_Type = Integer32
_RefClockSsmCvid_Object = MibTableColumn
refClockSsmCvid = _RefClockSsmCvid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 6),
    _RefClockSsmCvid_Type()
)
refClockSsmCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refClockSsmCvid.setStatus("current")
_RefClockRowStatus_Type = RowStatus
_RefClockRowStatus_Object = MibTableColumn
refClockRowStatus = _RefClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 7),
    _RefClockRowStatus_Type()
)
refClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockRowStatus.setStatus("current")
_RadioBridgeEthernet_ObjectIdentity = ObjectIdentity
radioBridgeEthernet = _RadioBridgeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 5)
)
_RbEthernetTable_Object = MibTable
rbEthernetTable = _RbEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1)
)
if mibBuilder.loadTexts:
    rbEthernetTable.setStatus("current")
_RbEthernetEntry_Object = MibTableRow
rbEthernetEntry = _RbEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1)
)
rbEthernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbEthernetEntry.setStatus("current")


class _EthernetAlarmPropagation_Type(Integer32):
    """Custom type ethernetAlarmPropagation based on Integer32"""
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
        *(("disabled", 0),
          ("backward", 1),
          ("forward", 2),
          ("both-direct", 3))
    )


_EthernetAlarmPropagation_Type.__name__ = "Integer32"
_EthernetAlarmPropagation_Object = MibTableColumn
ethernetAlarmPropagation = _EthernetAlarmPropagation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 2),
    _EthernetAlarmPropagation_Type()
)
ethernetAlarmPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetAlarmPropagation.setStatus("current")


class _EthernetLoopMode_Type(Integer32):
    """Custom type ethernetLoopMode based on Integer32"""
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
        *(("disabled", 0),
          ("external", 1),
          ("external-mac-swap", 2),
          ("internal", 3),
          ("internal-mac-swap", 4))
    )


_EthernetLoopMode_Type.__name__ = "Integer32"
_EthernetLoopMode_Object = MibTableColumn
ethernetLoopMode = _EthernetLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 3),
    _EthernetLoopMode_Type()
)
ethernetLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLoopMode.setStatus("current")
_EthernetLoopTimeout_Type = Integer32
_EthernetLoopTimeout_Object = MibTableColumn
ethernetLoopTimeout = _EthernetLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 4),
    _EthernetLoopTimeout_Type()
)
ethernetLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLoopTimeout.setStatus("current")


class _EthernetNetworkType_Type(Integer32):
    """Custom type ethernetNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("provider-nni", 1),
          ("customer-uni", 2),
          ("customer-nni", 3))
    )


_EthernetNetworkType_Type.__name__ = "Integer32"
_EthernetNetworkType_Object = MibTableColumn
ethernetNetworkType = _EthernetNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 5),
    _EthernetNetworkType_Type()
)
ethernetNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNetworkType.setStatus("current")
_EthernetPcpWriteProfileId_Type = Integer32
_EthernetPcpWriteProfileId_Object = MibTableColumn
ethernetPcpWriteProfileId = _EthernetPcpWriteProfileId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 6),
    _EthernetPcpWriteProfileId_Type()
)
ethernetPcpWriteProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPcpWriteProfileId.setStatus("current")


class _EthernetClassifierMode_Type(Integer32):
    """Custom type ethernetClassifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classifier-mode-dscp", 1),
          ("classifier-mode-pcp-dscp", 2))
    )


_EthernetClassifierMode_Type.__name__ = "Integer32"
_EthernetClassifierMode_Object = MibTableColumn
ethernetClassifierMode = _EthernetClassifierMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 7),
    _EthernetClassifierMode_Type()
)
ethernetClassifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetClassifierMode.setStatus("current")
_EthernetAlarmPropagationRemotePort_Type = Integer32
_EthernetAlarmPropagationRemotePort_Object = MibTableColumn
ethernetAlarmPropagationRemotePort = _EthernetAlarmPropagationRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 8),
    _EthernetAlarmPropagationRemotePort_Type()
)
ethernetAlarmPropagationRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetAlarmPropagationRemotePort.setStatus("current")
_EthernetTxThroughput_Type = Counter64
_EthernetTxThroughput_Object = MibTableColumn
ethernetTxThroughput = _EthernetTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 9),
    _EthernetTxThroughput_Type()
)
ethernetTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetTxThroughput.setStatus("current")
_EthernetRxThroughput_Type = Counter64
_EthernetRxThroughput_Object = MibTableColumn
ethernetRxThroughput = _EthernetRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 10),
    _EthernetRxThroughput_Type()
)
ethernetRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetRxThroughput.setStatus("current")
_RadioBridgeQosClassifier_ObjectIdentity = ObjectIdentity
radioBridgeQosClassifier = _RadioBridgeQosClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 6)
)
_RbClassifierCosTable_Object = MibTable
rbClassifierCosTable = _RbClassifierCosTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1)
)
if mibBuilder.loadTexts:
    rbClassifierCosTable.setStatus("current")
_RbClassifierCosEntry_Object = MibTableRow
rbClassifierCosEntry = _RbClassifierCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1)
)
rbClassifierCosEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "classifierCosId"),
)
if mibBuilder.loadTexts:
    rbClassifierCosEntry.setStatus("current")


class _ClassifierCosId_Type(Integer32):
    """Custom type classifierCosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_ClassifierCosId_Type.__name__ = "Integer32"
_ClassifierCosId_Object = MibTableColumn
classifierCosId = _ClassifierCosId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 1),
    _ClassifierCosId_Type()
)
classifierCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    classifierCosId.setStatus("current")
_ClassifierCosPortList_Type = OctetString
_ClassifierCosPortList_Object = MibTableColumn
classifierCosPortList = _ClassifierCosPortList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 2),
    _ClassifierCosPortList_Type()
)
classifierCosPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPortList.setStatus("current")


class _ClassifierCosPrecedence_Type(Integer32):
    """Custom type classifierCosPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ClassifierCosPrecedence_Type.__name__ = "Integer32"
_ClassifierCosPrecedence_Object = MibTableColumn
classifierCosPrecedence = _ClassifierCosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 3),
    _ClassifierCosPrecedence_Type()
)
classifierCosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPrecedence.setStatus("current")
_ClassifierCosVidList_Type = OctetString
_ClassifierCosVidList_Object = MibTableColumn
classifierCosVidList = _ClassifierCosVidList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 4),
    _ClassifierCosVidList_Type()
)
classifierCosVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosVidList.setStatus("current")
_ClassifierCosPcpList_Type = OctetString
_ClassifierCosPcpList_Object = MibTableColumn
classifierCosPcpList = _ClassifierCosPcpList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 5),
    _ClassifierCosPcpList_Type()
)
classifierCosPcpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPcpList.setStatus("current")


class _ClassifierCosCos_Type(Integer32):
    """Custom type classifierCosCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ClassifierCosCos_Type.__name__ = "Integer32"
_ClassifierCosCos_Object = MibTableColumn
classifierCosCos = _ClassifierCosCos_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 6),
    _ClassifierCosCos_Type()
)
classifierCosCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosCos.setStatus("current")


class _ClassifierCosIpCosType_Type(Integer32):
    """Custom type classifierCosIpCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-cos-dscp", 1),
          ("ip-cos-mpls", 2),
          ("ip-cos-dont-care", 3))
    )


_ClassifierCosIpCosType_Type.__name__ = "Integer32"
_ClassifierCosIpCosType_Object = MibTableColumn
classifierCosIpCosType = _ClassifierCosIpCosType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 7),
    _ClassifierCosIpCosType_Type()
)
classifierCosIpCosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosIpCosType.setStatus("current")
_ClassifierCosIpCosList_Type = OctetString
_ClassifierCosIpCosList_Object = MibTableColumn
classifierCosIpCosList = _ClassifierCosIpCosList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 8),
    _ClassifierCosIpCosList_Type()
)
classifierCosIpCosList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosIpCosList.setStatus("current")
_ClassifierCosRowStatus_Type = RowStatus
_ClassifierCosRowStatus_Object = MibTableColumn
classifierCosRowStatus = _ClassifierCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 9),
    _ClassifierCosRowStatus_Type()
)
classifierCosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosRowStatus.setStatus("current")


class _ClassifierCosPacketType_Type(Integer32):
    """Custom type classifierCosPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("non-unicast", 2),
          ("all", 3))
    )


_ClassifierCosPacketType_Type.__name__ = "Integer32"
_ClassifierCosPacketType_Object = MibTableColumn
classifierCosPacketType = _ClassifierCosPacketType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 10),
    _ClassifierCosPacketType_Type()
)
classifierCosPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPacketType.setStatus("current")
_RbClassifierEvcTable_Object = MibTable
rbClassifierEvcTable = _RbClassifierEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2)
)
if mibBuilder.loadTexts:
    rbClassifierEvcTable.setStatus("current")
_RbClassifierEvcEntry_Object = MibTableRow
rbClassifierEvcEntry = _RbClassifierEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1)
)
rbClassifierEvcEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "classifierEvcId"),
)
if mibBuilder.loadTexts:
    rbClassifierEvcEntry.setStatus("current")


class _ClassifierEvcId_Type(Integer32):
    """Custom type classifierEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_ClassifierEvcId_Type.__name__ = "Integer32"
_ClassifierEvcId_Object = MibTableColumn
classifierEvcId = _ClassifierEvcId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 1),
    _ClassifierEvcId_Type()
)
classifierEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    classifierEvcId.setStatus("current")
_ClassifierEvcPortList_Type = OctetString
_ClassifierEvcPortList_Object = MibTableColumn
classifierEvcPortList = _ClassifierEvcPortList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 2),
    _ClassifierEvcPortList_Type()
)
classifierEvcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPortList.setStatus("current")


class _ClassifierEvcPrecedence_Type(Integer32):
    """Custom type classifierEvcPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ClassifierEvcPrecedence_Type.__name__ = "Integer32"
_ClassifierEvcPrecedence_Object = MibTableColumn
classifierEvcPrecedence = _ClassifierEvcPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 3),
    _ClassifierEvcPrecedence_Type()
)
classifierEvcPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPrecedence.setStatus("current")
_ClassifierEvcVidList_Type = OctetString
_ClassifierEvcVidList_Object = MibTableColumn
classifierEvcVidList = _ClassifierEvcVidList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 4),
    _ClassifierEvcVidList_Type()
)
classifierEvcVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcVidList.setStatus("current")
_ClassifierEvcPcpList_Type = OctetString
_ClassifierEvcPcpList_Object = MibTableColumn
classifierEvcPcpList = _ClassifierEvcPcpList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 5),
    _ClassifierEvcPcpList_Type()
)
classifierEvcPcpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPcpList.setStatus("current")


class _ClassifierEvcEvc_Type(Integer32):
    """Custom type classifierEvcEvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ClassifierEvcEvc_Type.__name__ = "Integer32"
_ClassifierEvcEvc_Object = MibTableColumn
classifierEvcEvc = _ClassifierEvcEvc_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 6),
    _ClassifierEvcEvc_Type()
)
classifierEvcEvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcEvc.setStatus("current")


class _ClassifierEvcIpCosType_Type(Integer32):
    """Custom type classifierEvcIpCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-cos-dscp", 1),
          ("ip-cos-mpls", 2),
          ("ip-cos-dont-care", 3))
    )


_ClassifierEvcIpCosType_Type.__name__ = "Integer32"
_ClassifierEvcIpCosType_Object = MibTableColumn
classifierEvcIpCosType = _ClassifierEvcIpCosType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 7),
    _ClassifierEvcIpCosType_Type()
)
classifierEvcIpCosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcIpCosType.setStatus("current")
_ClassifierEvcIpCosList_Type = OctetString
_ClassifierEvcIpCosList_Object = MibTableColumn
classifierEvcIpCosList = _ClassifierEvcIpCosList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 8),
    _ClassifierEvcIpCosList_Type()
)
classifierEvcIpCosList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcIpCosList.setStatus("current")
_ClassifierEvcRowStatus_Type = RowStatus
_ClassifierEvcRowStatus_Object = MibTableColumn
classifierEvcRowStatus = _ClassifierEvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 9),
    _ClassifierEvcRowStatus_Type()
)
classifierEvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcRowStatus.setStatus("current")


class _ClassifierEvcPacketType_Type(Integer32):
    """Custom type classifierEvcPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("non-unicast", 2),
          ("all", 3))
    )


_ClassifierEvcPacketType_Type.__name__ = "Integer32"
_ClassifierEvcPacketType_Object = MibTableColumn
classifierEvcPacketType = _ClassifierEvcPacketType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 10),
    _ClassifierEvcPacketType_Type()
)
classifierEvcPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPacketType.setStatus("current")
_RadioBridgeQosIngressQueue_ObjectIdentity = ObjectIdentity
radioBridgeQosIngressQueue = _RadioBridgeQosIngressQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 7)
)
_RbQosIngressQueueTable_Object = MibTable
rbQosIngressQueueTable = _RbQosIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1)
)
if mibBuilder.loadTexts:
    rbQosIngressQueueTable.setStatus("current")
_RbQosIngressQueueEntry_Object = MibTableRow
rbQosIngressQueueEntry = _RbQosIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1)
)
rbQosIngressQueueEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "qosIngressQueueEvcId"),
    (0, "RADIO-BRIDGE-MIB", "qosIngressQueueCosId"),
)
if mibBuilder.loadTexts:
    rbQosIngressQueueEntry.setStatus("current")
_QosIngressQueueEvcId_Type = Integer32
_QosIngressQueueEvcId_Object = MibTableColumn
qosIngressQueueEvcId = _QosIngressQueueEvcId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 1),
    _QosIngressQueueEvcId_Type()
)
qosIngressQueueEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIngressQueueEvcId.setStatus("current")
_QosIngressQueueCosId_Type = Integer32
_QosIngressQueueCosId_Object = MibTableColumn
qosIngressQueueCosId = _QosIngressQueueCosId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 2),
    _QosIngressQueueCosId_Type()
)
qosIngressQueueCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIngressQueueCosId.setStatus("current")
_QosIngressQueueMeterId_Type = Integer32
_QosIngressQueueMeterId_Object = MibTableColumn
qosIngressQueueMeterId = _QosIngressQueueMeterId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 3),
    _QosIngressQueueMeterId_Type()
)
qosIngressQueueMeterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressQueueMeterId.setStatus("current")
_QosIngressQueueMarking_Type = TruthValue
_QosIngressQueueMarking_Object = MibTableColumn
qosIngressQueueMarking = _QosIngressQueueMarking_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 4),
    _QosIngressQueueMarking_Type()
)
qosIngressQueueMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressQueueMarking.setStatus("current")
_QosIngressQueueRowStatus_Type = RowStatus
_QosIngressQueueRowStatus_Object = MibTableColumn
qosIngressQueueRowStatus = _QosIngressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 6),
    _QosIngressQueueRowStatus_Type()
)
qosIngressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressQueueRowStatus.setStatus("current")
_RadioBridgeQosEgressQueue_ObjectIdentity = ObjectIdentity
radioBridgeQosEgressQueue = _RadioBridgeQosEgressQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 8)
)
_RbQosEgressQueueTable_Object = MibTable
rbQosEgressQueueTable = _RbQosEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1)
)
if mibBuilder.loadTexts:
    rbQosEgressQueueTable.setStatus("current")
_RbQosEgressQueueEntry_Object = MibTableRow
rbQosEgressQueueEntry = _RbQosEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1)
)
rbQosEgressQueueEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "qosEgressQueuePortNum"),
    (0, "RADIO-BRIDGE-MIB", "qosEgressQueueCosId"),
)
if mibBuilder.loadTexts:
    rbQosEgressQueueEntry.setStatus("current")
_QosEgressQueuePortNum_Type = Integer32
_QosEgressQueuePortNum_Object = MibTableColumn
qosEgressQueuePortNum = _QosEgressQueuePortNum_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 1),
    _QosEgressQueuePortNum_Type()
)
qosEgressQueuePortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEgressQueuePortNum.setStatus("current")
_QosEgressQueueCosId_Type = Integer32
_QosEgressQueueCosId_Object = MibTableColumn
qosEgressQueueCosId = _QosEgressQueueCosId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 2),
    _QosEgressQueueCosId_Type()
)
qosEgressQueueCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEgressQueueCosId.setStatus("current")


class _QosEgressQueueWfqWeight_Type(Integer32):
    """Custom type qosEgressQueueWfqWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_QosEgressQueueWfqWeight_Type.__name__ = "Integer32"
_QosEgressQueueWfqWeight_Object = MibTableColumn
qosEgressQueueWfqWeight = _QosEgressQueueWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 4),
    _QosEgressQueueWfqWeight_Type()
)
qosEgressQueueWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressQueueWfqWeight.setStatus("current")


class _QosEgressQueueCir_Type(Integer32):
    """Custom type qosEgressQueueCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_QosEgressQueueCir_Type.__name__ = "Integer32"
_QosEgressQueueCir_Object = MibTableColumn
qosEgressQueueCir = _QosEgressQueueCir_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 5),
    _QosEgressQueueCir_Type()
)
qosEgressQueueCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressQueueCir.setStatus("current")


class _QosEgressQueueMode_Type(Integer32):
    """Custom type qosEgressQueueMode based on Integer32"""
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
        *(("strictPriority", 1),
          ("wfg", 2),
          ("priority-shaper", 3),
          ("wfq-shaper", 4))
    )


_QosEgressQueueMode_Type.__name__ = "Integer32"
_QosEgressQueueMode_Object = MibTableColumn
qosEgressQueueMode = _QosEgressQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 6),
    _QosEgressQueueMode_Type()
)
qosEgressQueueMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosEgressQueueMode.setStatus("current")


class _QosEgressQueueColorDrop_Type(Integer32):
    """Custom type qosEgressQueueColorDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-drop", 2))
    )


_QosEgressQueueColorDrop_Type.__name__ = "Integer32"
_QosEgressQueueColorDrop_Object = MibTableColumn
qosEgressQueueColorDrop = _QosEgressQueueColorDrop_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 7),
    _QosEgressQueueColorDrop_Type()
)
qosEgressQueueColorDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressQueueColorDrop.setStatus("current")
_QosEgressDropMode_Type = Integer32
_QosEgressDropMode_Object = MibTableColumn
qosEgressDropMode = _QosEgressDropMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 8),
    _QosEgressDropMode_Type()
)
qosEgressDropMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressDropMode.setStatus("current")
_RadioBridgeIp_ObjectIdentity = ObjectIdentity
radioBridgeIp = _RadioBridgeIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 9)
)
_RbIpTable_Object = MibTable
rbIpTable = _RbIpTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1)
)
if mibBuilder.loadTexts:
    rbIpTable.setStatus("current")
_RbIpEntry_Object = MibTableRow
rbIpEntry = _RbIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1)
)
rbIpEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbIpIndex"),
)
if mibBuilder.loadTexts:
    rbIpEntry.setStatus("current")
_RbIpIndex_Type = Integer32
_RbIpIndex_Object = MibTableColumn
rbIpIndex = _RbIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 1),
    _RbIpIndex_Type()
)
rbIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbIpIndex.setStatus("current")
_RbIpAddress_Type = IpAddress
_RbIpAddress_Object = MibTableColumn
rbIpAddress = _RbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 2),
    _RbIpAddress_Type()
)
rbIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpAddress.setStatus("current")


class _RbIpPrefixLen_Type(Integer32):
    """Custom type rbIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RbIpPrefixLen_Type.__name__ = "Integer32"
_RbIpPrefixLen_Object = MibTableColumn
rbIpPrefixLen = _RbIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 3),
    _RbIpPrefixLen_Type()
)
rbIpPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbIpPrefixLen.setStatus("current")
_RbIpVlanId_Type = Integer32
_RbIpVlanId_Object = MibTableColumn
rbIpVlanId = _RbIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 4),
    _RbIpVlanId_Type()
)
rbIpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpVlanId.setStatus("current")
_RbIpRowStatus_Type = RowStatus
_RbIpRowStatus_Object = MibTableColumn
rbIpRowStatus = _RbIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 5),
    _RbIpRowStatus_Type()
)
rbIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpRowStatus.setStatus("current")


class _RbIpType_Type(Integer32):
    """Custom type rbIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-static", 1),
          ("ip-dhcp", 2))
    )


_RbIpType_Type.__name__ = "Integer32"
_RbIpType_Object = MibTableColumn
rbIpType = _RbIpType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 6),
    _RbIpType_Type()
)
rbIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpType.setStatus("current")
_RbIpGateway_Type = IpAddress
_RbIpGateway_Object = MibTableColumn
rbIpGateway = _RbIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 7),
    _RbIpGateway_Type()
)
rbIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbIpGateway.setStatus("current")
_RadioBridgeCfm_ObjectIdentity = ObjectIdentity
radioBridgeCfm = _RadioBridgeCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 10)
)
_RbPeerMep_Object = MibTable
rbPeerMep = _RbPeerMep_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1)
)
if mibBuilder.loadTexts:
    rbPeerMep.setStatus("current")
_RbPeerMepEntry_Object = MibTableRow
rbPeerMepEntry = _RbPeerMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1)
)
rbPeerMepEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbMdIndex"),
    (0, "RADIO-BRIDGE-MIB", "rbMaIndex"),
    (0, "RADIO-BRIDGE-MIB", "rbMepId"),
    (0, "RADIO-BRIDGE-MIB", "rbPeerMepId"),
)
if mibBuilder.loadTexts:
    rbPeerMepEntry.setStatus("current")
_RbMdIndex_Type = Integer32
_RbMdIndex_Object = MibTableColumn
rbMdIndex = _RbMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 1),
    _RbMdIndex_Type()
)
rbMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMdIndex.setStatus("current")
_RbMaIndex_Type = Integer32
_RbMaIndex_Object = MibTableColumn
rbMaIndex = _RbMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 2),
    _RbMaIndex_Type()
)
rbMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMaIndex.setStatus("current")
_RbMepId_Type = Integer32
_RbMepId_Object = MibTableColumn
rbMepId = _RbMepId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 3),
    _RbMepId_Type()
)
rbMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMepId.setStatus("current")
_RbPeerMepId_Type = Integer32
_RbPeerMepId_Object = MibTableColumn
rbPeerMepId = _RbPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 4),
    _RbPeerMepId_Type()
)
rbPeerMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepId.setStatus("current")
_RbPeerMepFarEndLoss_Type = Counter64
_RbPeerMepFarEndLoss_Object = MibTableColumn
rbPeerMepFarEndLoss = _RbPeerMepFarEndLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 5),
    _RbPeerMepFarEndLoss_Type()
)
rbPeerMepFarEndLoss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepFarEndLoss.setStatus("current")
_RbPeerMepNearEndLoss_Type = Counter64
_RbPeerMepNearEndLoss_Object = MibTableColumn
rbPeerMepNearEndLoss = _RbPeerMepNearEndLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 6),
    _RbPeerMepNearEndLoss_Type()
)
rbPeerMepNearEndLoss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepNearEndLoss.setStatus("current")
_RbPeerMepTotalTxFarEnd_Type = Counter64
_RbPeerMepTotalTxFarEnd_Object = MibTableColumn
rbPeerMepTotalTxFarEnd = _RbPeerMepTotalTxFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 7),
    _RbPeerMepTotalTxFarEnd_Type()
)
rbPeerMepTotalTxFarEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepTotalTxFarEnd.setStatus("current")
_RbPeerMepTotalTxNearEnd_Type = Counter64
_RbPeerMepTotalTxNearEnd_Object = MibTableColumn
rbPeerMepTotalTxNearEnd = _RbPeerMepTotalTxNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 8),
    _RbPeerMepTotalTxNearEnd_Type()
)
rbPeerMepTotalTxNearEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepTotalTxNearEnd.setStatus("current")
_RbPeerMepFrameDelay_Type = Counter64
_RbPeerMepFrameDelay_Object = MibTableColumn
rbPeerMepFrameDelay = _RbPeerMepFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 9),
    _RbPeerMepFrameDelay_Type()
)
rbPeerMepFrameDelay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepFrameDelay.setStatus("current")
_RbPeerMepFrameDelayVariation_Type = Counter64
_RbPeerMepFrameDelayVariation_Object = MibTableColumn
rbPeerMepFrameDelayVariation = _RbPeerMepFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 10),
    _RbPeerMepFrameDelayVariation_Type()
)
rbPeerMepFrameDelayVariation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepFrameDelayVariation.setStatus("current")
_RbMep_Object = MibTable
rbMep = _RbMep_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2)
)
if mibBuilder.loadTexts:
    rbMep.setStatus("current")
_RbMepEntry_Object = MibTableRow
rbMepEntry = _RbMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1)
)
if mibBuilder.loadTexts:
    rbMepEntry.setStatus("current")
_RbMepAisEnable_Type = TruthValue
_RbMepAisEnable_Object = MibTableColumn
rbMepAisEnable = _RbMepAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 1),
    _RbMepAisEnable_Type()
)
rbMepAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisEnable.setStatus("current")


class _RbMepAisPeriod_Type(Integer32):
    """Custom type rbMepAisPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aisPeriod-1-sec", 4),
          ("aisPeriod-1-min", 6))
    )


_RbMepAisPeriod_Type.__name__ = "Integer32"
_RbMepAisPeriod_Object = MibTableColumn
rbMepAisPeriod = _RbMepAisPeriod_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 2),
    _RbMepAisPeriod_Type()
)
rbMepAisPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisPeriod.setStatus("current")
_RbMepAisSuppress_Type = TruthValue
_RbMepAisSuppress_Object = MibTableColumn
rbMepAisSuppress = _RbMepAisSuppress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 3),
    _RbMepAisSuppress_Type()
)
rbMepAisSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisSuppress.setStatus("current")
_RbMepAisLevel_Type = Integer32
_RbMepAisLevel_Object = MibTableColumn
rbMepAisLevel = _RbMepAisLevel_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 4),
    _RbMepAisLevel_Type()
)
rbMepAisLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisLevel.setStatus("current")
_RbMepAisDefects_Type = TruthValue
_RbMepAisDefects_Object = MibTableColumn
rbMepAisDefects = _RbMepAisDefects_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 5),
    _RbMepAisDefects_Type()
)
rbMepAisDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMepAisDefects.setStatus("current")
_RadioBridgeAlarms_ObjectIdentity = ObjectIdentity
radioBridgeAlarms = _RadioBridgeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 11)
)
_RbAlarmsCommon_ObjectIdentity = ObjectIdentity
rbAlarmsCommon = _RbAlarmsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1)
)
_RbCurrentAlarmChangeCounter_Type = Integer32
_RbCurrentAlarmChangeCounter_Object = MibScalar
rbCurrentAlarmChangeCounter = _RbCurrentAlarmChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 1),
    _RbCurrentAlarmChangeCounter_Type()
)
rbCurrentAlarmChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmChangeCounter.setStatus("current")
_RbCurrentAlarmMostSevere_Type = AlarmSeverity
_RbCurrentAlarmMostSevere_Object = MibScalar
rbCurrentAlarmMostSevere = _RbCurrentAlarmMostSevere_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 2),
    _RbCurrentAlarmMostSevere_Type()
)
rbCurrentAlarmMostSevere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmMostSevere.setStatus("current")
_RbCurrentAlarmLastIndex_Type = Integer32
_RbCurrentAlarmLastIndex_Object = MibScalar
rbCurrentAlarmLastIndex = _RbCurrentAlarmLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 3),
    _RbCurrentAlarmLastIndex_Type()
)
rbCurrentAlarmLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmLastIndex.setStatus("current")


class _RbCurrentAlarmLastTrapType_Type(Integer32):
    """Custom type rbCurrentAlarmLastTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-up", 1),
          ("alarm-down", 2))
    )


_RbCurrentAlarmLastTrapType_Type.__name__ = "Integer32"
_RbCurrentAlarmLastTrapType_Object = MibScalar
rbCurrentAlarmLastTrapType = _RbCurrentAlarmLastTrapType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 4),
    _RbCurrentAlarmLastTrapType_Type()
)
rbCurrentAlarmLastTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmLastTrapType.setStatus("current")
_RbCurrentAlarmSourceAddr_Type = IpAddress
_RbCurrentAlarmSourceAddr_Object = MibScalar
rbCurrentAlarmSourceAddr = _RbCurrentAlarmSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 10),
    _RbCurrentAlarmSourceAddr_Type()
)
rbCurrentAlarmSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSourceAddr.setStatus("current")
_RbCurrentAlarmTable_Object = MibTable
rbCurrentAlarmTable = _RbCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2)
)
if mibBuilder.loadTexts:
    rbCurrentAlarmTable.setStatus("current")
_RbCurrentAlarmEntry_Object = MibTableRow
rbCurrentAlarmEntry = _RbCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1)
)
rbCurrentAlarmEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbCurrentAlarmIndex"),
)
if mibBuilder.loadTexts:
    rbCurrentAlarmEntry.setStatus("current")
_RbCurrentAlarmIndex_Type = Integer32
_RbCurrentAlarmIndex_Object = MibTableColumn
rbCurrentAlarmIndex = _RbCurrentAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 1),
    _RbCurrentAlarmIndex_Type()
)
rbCurrentAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmIndex.setStatus("current")
_RbCurrentAlarmType_Type = AlarmType
_RbCurrentAlarmType_Object = MibTableColumn
rbCurrentAlarmType = _RbCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 2),
    _RbCurrentAlarmType_Type()
)
rbCurrentAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmType.setStatus("current")
_RbCurrentAlarmTypeName_Type = DisplayString
_RbCurrentAlarmTypeName_Object = MibTableColumn
rbCurrentAlarmTypeName = _RbCurrentAlarmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 3),
    _RbCurrentAlarmTypeName_Type()
)
rbCurrentAlarmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmTypeName.setStatus("current")
_RbCurrentAlarmSource_Type = DisplayString
_RbCurrentAlarmSource_Object = MibTableColumn
rbCurrentAlarmSource = _RbCurrentAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 4),
    _RbCurrentAlarmSource_Type()
)
rbCurrentAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSource.setStatus("current")
_RbCurrentAlarmSeverity_Type = AlarmSeverity
_RbCurrentAlarmSeverity_Object = MibTableColumn
rbCurrentAlarmSeverity = _RbCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 5),
    _RbCurrentAlarmSeverity_Type()
)
rbCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSeverity.setStatus("current")
_RbCurrentAlarmRaisedTime_Type = TimeTicks
_RbCurrentAlarmRaisedTime_Object = MibTableColumn
rbCurrentAlarmRaisedTime = _RbCurrentAlarmRaisedTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 6),
    _RbCurrentAlarmRaisedTime_Type()
)
rbCurrentAlarmRaisedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmRaisedTime.setStatus("current")
_RbCurrentAlarmDesc_Type = DisplayString
_RbCurrentAlarmDesc_Object = MibTableColumn
rbCurrentAlarmDesc = _RbCurrentAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 7),
    _RbCurrentAlarmDesc_Type()
)
rbCurrentAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmDesc.setStatus("current")
_RbCurrentAlarmCause_Type = DisplayString
_RbCurrentAlarmCause_Object = MibTableColumn
rbCurrentAlarmCause = _RbCurrentAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 8),
    _RbCurrentAlarmCause_Type()
)
rbCurrentAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmCause.setStatus("current")
_RbCurrentAlarmAction_Type = DisplayString
_RbCurrentAlarmAction_Object = MibTableColumn
rbCurrentAlarmAction = _RbCurrentAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 9),
    _RbCurrentAlarmAction_Type()
)
rbCurrentAlarmAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmAction.setStatus("current")
_RbCurrentAlarmIfIndex_Type = Integer32
_RbCurrentAlarmIfIndex_Object = MibTableColumn
rbCurrentAlarmIfIndex = _RbCurrentAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 10),
    _RbCurrentAlarmIfIndex_Type()
)
rbCurrentAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmIfIndex.setStatus("current")
_RadioBridgeScheduler_ObjectIdentity = ObjectIdentity
radioBridgeScheduler = _RadioBridgeScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 12)
)


class _RbSchedulerMode_Type(Integer32):
    """Custom type rbSchedulerMode based on Integer32"""
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
        *(("strictPriority", 1),
          ("wfg", 2),
          ("priority-shaper", 3),
          ("wfq-shaper", 4))
    )


_RbSchedulerMode_Type.__name__ = "Integer32"
_RbSchedulerMode_Object = MibScalar
rbSchedulerMode = _RbSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 12, 1),
    _RbSchedulerMode_Type()
)
rbSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSchedulerMode.setStatus("current")


class _RbClassifierMode_Type(Integer32):
    """Custom type rbClassifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 1),
          ("pcp", 2))
    )


_RbClassifierMode_Type.__name__ = "Integer32"
_RbClassifierMode_Object = MibScalar
rbClassifierMode = _RbClassifierMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 12, 2),
    _RbClassifierMode_Type()
)
rbClassifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbClassifierMode.setStatus("current")
_RadioBridgeEncryption_ObjectIdentity = ObjectIdentity
radioBridgeEncryption = _RadioBridgeEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 13)
)
_RbRfEncryption_Type = TruthValue
_RbRfEncryption_Object = MibScalar
rbRfEncryption = _RbRfEncryption_Object(
    (1, 3, 6, 1, 4, 1, 31926, 13, 1),
    _RbRfEncryption_Type()
)
rbRfEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRfEncryption.setStatus("current")
_RbRfStaticKey_Type = OctetString
_RbRfStaticKey_Object = MibScalar
rbRfStaticKey = _RbRfStaticKey_Object(
    (1, 3, 6, 1, 4, 1, 31926, 13, 2),
    _RbRfStaticKey_Type()
)
rbRfStaticKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRfStaticKey.setStatus("current")
_RbRfAuthenticationString_Type = OctetString
_RbRfAuthenticationString_Object = MibScalar
rbRfAuthenticationString = _RbRfAuthenticationString_Object(
    (1, 3, 6, 1, 4, 1, 31926, 13, 3),
    _RbRfAuthenticationString_Type()
)
rbRfAuthenticationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRfAuthenticationString.setStatus("current")
_RadioBridgeMeter_ObjectIdentity = ObjectIdentity
radioBridgeMeter = _RadioBridgeMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 14)
)
_RbMeterTable_Object = MibTable
rbMeterTable = _RbMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1)
)
if mibBuilder.loadTexts:
    rbMeterTable.setStatus("current")
_RbMeterEntry_Object = MibTableRow
rbMeterEntry = _RbMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1)
)
rbMeterEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbMeterId"),
)
if mibBuilder.loadTexts:
    rbMeterEntry.setStatus("current")


class _RbMeterId_Type(Integer32):
    """Custom type rbMeterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_RbMeterId_Type.__name__ = "Integer32"
_RbMeterId_Object = MibTableColumn
rbMeterId = _RbMeterId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 1),
    _RbMeterId_Type()
)
rbMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMeterId.setStatus("current")


class _RbMeterCir_Type(Integer32):
    """Custom type rbMeterCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RbMeterCir_Type.__name__ = "Integer32"
_RbMeterCir_Object = MibTableColumn
rbMeterCir = _RbMeterCir_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 2),
    _RbMeterCir_Type()
)
rbMeterCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterCir.setStatus("current")


class _RbMeterCbs_Type(Integer32):
    """Custom type rbMeterCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9216, 50000),
    )


_RbMeterCbs_Type.__name__ = "Integer32"
_RbMeterCbs_Object = MibTableColumn
rbMeterCbs = _RbMeterCbs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 3),
    _RbMeterCbs_Type()
)
rbMeterCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterCbs.setStatus("current")


class _RbMeterEir_Type(Integer32):
    """Custom type rbMeterEir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RbMeterEir_Type.__name__ = "Integer32"
_RbMeterEir_Object = MibTableColumn
rbMeterEir = _RbMeterEir_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 4),
    _RbMeterEir_Type()
)
rbMeterEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterEir.setStatus("current")


class _RbMeterEbs_Type(Integer32):
    """Custom type rbMeterEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9216, 100000),
    )


_RbMeterEbs_Type.__name__ = "Integer32"
_RbMeterEbs_Object = MibTableColumn
rbMeterEbs = _RbMeterEbs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 5),
    _RbMeterEbs_Type()
)
rbMeterEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterEbs.setStatus("current")


class _RbMeterColorMode_Type(Integer32):
    """Custom type rbMeterColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-blind", 2))
    )


_RbMeterColorMode_Type.__name__ = "Integer32"
_RbMeterColorMode_Object = MibTableColumn
rbMeterColorMode = _RbMeterColorMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 6),
    _RbMeterColorMode_Type()
)
rbMeterColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterColorMode.setStatus("current")
_RbMeterRowStatus_Type = RowStatus
_RbMeterRowStatus_Object = MibTableColumn
rbMeterRowStatus = _RbMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 7),
    _RbMeterRowStatus_Type()
)
rbMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterRowStatus.setStatus("current")
_RadioBridgeEventConfig_ObjectIdentity = ObjectIdentity
radioBridgeEventConfig = _RadioBridgeEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 15)
)
_RbEventConfigTable_Object = MibTable
rbEventConfigTable = _RbEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1)
)
if mibBuilder.loadTexts:
    rbEventConfigTable.setStatus("current")
_RbEventConfigEntry_Object = MibTableRow
rbEventConfigEntry = _RbEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1)
)
rbEventConfigEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbEventConfigIndex"),
)
if mibBuilder.loadTexts:
    rbEventConfigEntry.setStatus("current")
_RbEventConfigIndex_Type = Integer32
_RbEventConfigIndex_Object = MibTableColumn
rbEventConfigIndex = _RbEventConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1, 1),
    _RbEventConfigIndex_Type()
)
rbEventConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbEventConfigIndex.setStatus("current")
_RbEventConfigId_Type = OctetString
_RbEventConfigId_Object = MibTableColumn
rbEventConfigId = _RbEventConfigId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1, 2),
    _RbEventConfigId_Type()
)
rbEventConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbEventConfigId.setStatus("current")
_RbEventConfigMask_Type = TruthValue
_RbEventConfigMask_Object = MibTableColumn
rbEventConfigMask = _RbEventConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1, 3),
    _RbEventConfigMask_Type()
)
rbEventConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbEventConfigMask.setStatus("current")
_RadioBridgeSnmp_ObjectIdentity = ObjectIdentity
radioBridgeSnmp = _RadioBridgeSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 17)
)
_RbAgentReadCommunity_Type = DisplayString
_RbAgentReadCommunity_Object = MibScalar
rbAgentReadCommunity = _RbAgentReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 17, 1),
    _RbAgentReadCommunity_Type()
)
rbAgentReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAgentReadCommunity.setStatus("current")
_RbAgentWriteCommunity_Type = DisplayString
_RbAgentWriteCommunity_Object = MibScalar
rbAgentWriteCommunity = _RbAgentWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 17, 2),
    _RbAgentWriteCommunity_Type()
)
rbAgentWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAgentWriteCommunity.setStatus("current")


class _RbAgentSnmpVersion_Type(Integer32):
    """Custom type rbAgentSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 2),
          ("v3", 3))
    )


_RbAgentSnmpVersion_Type.__name__ = "Integer32"
_RbAgentSnmpVersion_Object = MibScalar
rbAgentSnmpVersion = _RbAgentSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 31926, 17, 3),
    _RbAgentSnmpVersion_Type()
)
rbAgentSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAgentSnmpVersion.setStatus("current")
_RbSysFileOperationTable_Object = MibTable
rbSysFileOperationTable = _RbSysFileOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18)
)
if mibBuilder.loadTexts:
    rbSysFileOperationTable.setStatus("current")
_RbSysFileOperationEntry_Object = MibTableRow
rbSysFileOperationEntry = _RbSysFileOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1)
)
rbSysFileOperationEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "fileSessionIndex"),
)
if mibBuilder.loadTexts:
    rbSysFileOperationEntry.setStatus("current")
_FileSessionIndex_Type = Integer32
_FileSessionIndex_Object = MibTableColumn
fileSessionIndex = _FileSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 1),
    _FileSessionIndex_Type()
)
fileSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSessionIndex.setStatus("current")


class _FileSessionCommand_Type(Integer32):
    """Custom type fileSessionCommand based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("copySwFromRemote", 1),
          ("copyLicenseFromRemote", 2),
          ("copyFileFromRemoteToLocal", 3),
          ("copyFileFromLocalToRemote", 4),
          ("acceptSw", 5),
          ("runSw", 6),
          ("copyDirToRemote", 7),
          ("copyEventLog", 9),
          ("copyUserActivityLog", 10),
          ("runScript", 11),
          ("copyInventory", 12),
          ("copyStatsHistory", 13))
    )


_FileSessionCommand_Type.__name__ = "Integer32"
_FileSessionCommand_Object = MibTableColumn
fileSessionCommand = _FileSessionCommand_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 2),
    _FileSessionCommand_Type()
)
fileSessionCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionCommand.setStatus("current")
_FileSessionLocalParams_Type = DisplayString
_FileSessionLocalParams_Object = MibTableColumn
fileSessionLocalParams = _FileSessionLocalParams_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 3),
    _FileSessionLocalParams_Type()
)
fileSessionLocalParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionLocalParams.setStatus("current")
_FileSessionRemotePath_Type = DisplayString
_FileSessionRemotePath_Object = MibTableColumn
fileSessionRemotePath = _FileSessionRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 4),
    _FileSessionRemotePath_Type()
)
fileSessionRemotePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionRemotePath.setStatus("current")
_FileSessionServer_Type = DisplayString
_FileSessionServer_Object = MibTableColumn
fileSessionServer = _FileSessionServer_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 5),
    _FileSessionServer_Type()
)
fileSessionServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionServer.setStatus("current")
_FileSessionUser_Type = DisplayString
_FileSessionUser_Object = MibTableColumn
fileSessionUser = _FileSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 6),
    _FileSessionUser_Type()
)
fileSessionUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionUser.setStatus("current")
_FileSessionPassword_Type = DisplayString
_FileSessionPassword_Object = MibTableColumn
fileSessionPassword = _FileSessionPassword_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 7),
    _FileSessionPassword_Type()
)
fileSessionPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionPassword.setStatus("current")
_FileSessionResult_Type = DisplayString
_FileSessionResult_Object = MibTableColumn
fileSessionResult = _FileSessionResult_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 8),
    _FileSessionResult_Type()
)
fileSessionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSessionResult.setStatus("current")


class _FileSessionState_Type(Integer32):
    """Custom type fileSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("terminated-ok", 2),
          ("terminated-error", 3))
    )


_FileSessionState_Type.__name__ = "Integer32"
_FileSessionState_Object = MibTableColumn
fileSessionState = _FileSessionState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 9),
    _FileSessionState_Type()
)
fileSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSessionState.setStatus("current")
_FileSessionRowStatus_Type = RowStatus
_FileSessionRowStatus_Object = MibTableColumn
fileSessionRowStatus = _FileSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 10),
    _FileSessionRowStatus_Type()
)
fileSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionRowStatus.setStatus("current")


class _FileSessionProtocol_Type(Integer32):
    """Custom type fileSessionProtocol based on Integer32"""
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


_FileSessionProtocol_Type.__name__ = "Integer32"
_FileSessionProtocol_Object = MibTableColumn
fileSessionProtocol = _FileSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 13),
    _FileSessionProtocol_Type()
)
fileSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSessionProtocol.setStatus("current")
_RadioBridgeLldp_ObjectIdentity = ObjectIdentity
radioBridgeLldp = _RadioBridgeLldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 19)
)
_RbLldpPortExtensionTable_Object = MibTable
rbLldpPortExtensionTable = _RbLldpPortExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1)
)
if mibBuilder.loadTexts:
    rbLldpPortExtensionTable.setStatus("current")
_RbLldpPortExtensionEntry_Object = MibTableRow
rbLldpPortExtensionEntry = _RbLldpPortExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1)
)
rbLldpPortExtensionEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbLldpPortIfIndex"),
    (0, "RADIO-BRIDGE-MIB", "rbLldpPortDestAddressIndex"),
)
if mibBuilder.loadTexts:
    rbLldpPortExtensionEntry.setStatus("current")
_RbLldpPortIfIndex_Type = InterfaceIndex
_RbLldpPortIfIndex_Object = MibTableColumn
rbLldpPortIfIndex = _RbLldpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 1),
    _RbLldpPortIfIndex_Type()
)
rbLldpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbLldpPortIfIndex.setStatus("current")
_RbLldpPortDestAddressIndex_Type = Unsigned32
_RbLldpPortDestAddressIndex_Object = MibTableColumn
rbLldpPortDestAddressIndex = _RbLldpPortDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 2),
    _RbLldpPortDestAddressIndex_Type()
)
rbLldpPortDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbLldpPortDestAddressIndex.setStatus("current")
_RbLldpPortVid_Type = Unsigned32
_RbLldpPortVid_Object = MibTableColumn
rbLldpPortVid = _RbLldpPortVid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 3),
    _RbLldpPortVid_Type()
)
rbLldpPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbLldpPortVid.setStatus("current")


class _RbLldpPortAddrType_Type(Integer32):
    """Custom type rbLldpPortAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_RbLldpPortAddrType_Type.__name__ = "Integer32"
_RbLldpPortAddrType_Object = MibTableColumn
rbLldpPortAddrType = _RbLldpPortAddrType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 4),
    _RbLldpPortAddrType_Type()
)
rbLldpPortAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbLldpPortAddrType.setStatus("current")


class _RbLldpPortIpIndex_Type(Integer32):
    """Custom type rbLldpPortIpIndex based on Integer32"""
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
        *(("lowest", 0),
          ("first", 1),
          ("second", 2),
          ("third", 3),
          ("forth", 4),
          ("highest", 5))
    )


_RbLldpPortIpIndex_Type.__name__ = "Integer32"
_RbLldpPortIpIndex_Object = MibTableColumn
rbLldpPortIpIndex = _RbLldpPortIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 5),
    _RbLldpPortIpIndex_Type()
)
rbLldpPortIpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbLldpPortIpIndex.setStatus("current")
_RadioBridgeWred_ObjectIdentity = ObjectIdentity
radioBridgeWred = _RadioBridgeWred_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 20)
)
_RbWredTable_Object = MibTable
rbWredTable = _RbWredTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1)
)
if mibBuilder.loadTexts:
    rbWredTable.setStatus("current")
_RbWredEntry_Object = MibTableRow
rbWredEntry = _RbWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1)
)
rbWredEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbWredId"),
)
if mibBuilder.loadTexts:
    rbWredEntry.setStatus("current")
_RbWredId_Type = Integer32
_RbWredId_Object = MibTableColumn
rbWredId = _RbWredId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 1),
    _RbWredId_Type()
)
rbWredId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbWredId.setStatus("current")


class _RbWredNfactor_Type(Integer32):
    """Custom type rbWredNfactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RbWredNfactor_Type.__name__ = "Integer32"
_RbWredNfactor_Object = MibTableColumn
rbWredNfactor = _RbWredNfactor_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 2),
    _RbWredNfactor_Type()
)
rbWredNfactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredNfactor.setStatus("current")
_RbWredMinThreshold_Type = Integer32
_RbWredMinThreshold_Object = MibTableColumn
rbWredMinThreshold = _RbWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 3),
    _RbWredMinThreshold_Type()
)
rbWredMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMinThreshold.setStatus("current")
_RbWredMaxThreshold_Type = Integer32
_RbWredMaxThreshold_Object = MibTableColumn
rbWredMaxThreshold = _RbWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 4),
    _RbWredMaxThreshold_Type()
)
rbWredMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMaxThreshold.setStatus("current")


class _RbWredProbability_Type(Integer32):
    """Custom type rbWredProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RbWredProbability_Type.__name__ = "Integer32"
_RbWredProbability_Object = MibTableColumn
rbWredProbability = _RbWredProbability_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 5),
    _RbWredProbability_Type()
)
rbWredProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredProbability.setStatus("current")
_RbWredMinThresholdYellow_Type = Integer32
_RbWredMinThresholdYellow_Object = MibTableColumn
rbWredMinThresholdYellow = _RbWredMinThresholdYellow_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 6),
    _RbWredMinThresholdYellow_Type()
)
rbWredMinThresholdYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMinThresholdYellow.setStatus("current")
_RbWredMaxThresholdYellow_Type = Integer32
_RbWredMaxThresholdYellow_Object = MibTableColumn
rbWredMaxThresholdYellow = _RbWredMaxThresholdYellow_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 7),
    _RbWredMaxThresholdYellow_Type()
)
rbWredMaxThresholdYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMaxThresholdYellow.setStatus("current")


class _RbWredProbabilityYellow_Type(Integer32):
    """Custom type rbWredProbabilityYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RbWredProbabilityYellow_Type.__name__ = "Integer32"
_RbWredProbabilityYellow_Object = MibTableColumn
rbWredProbabilityYellow = _RbWredProbabilityYellow_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 8),
    _RbWredProbabilityYellow_Type()
)
rbWredProbabilityYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredProbabilityYellow.setStatus("current")
_RbWredRowStatus_Type = RowStatus
_RbWredRowStatus_Object = MibTableColumn
rbWredRowStatus = _RbWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 9),
    _RbWredRowStatus_Type()
)
rbWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredRowStatus.setStatus("current")
_RadioBridgeAuthentication_ObjectIdentity = ObjectIdentity
radioBridgeAuthentication = _RadioBridgeAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 21)
)
_RbAuthServersTable_Object = MibTable
rbAuthServersTable = _RbAuthServersTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1)
)
if mibBuilder.loadTexts:
    rbAuthServersTable.setStatus("current")
_RbAuthServersEntry_Object = MibTableRow
rbAuthServersEntry = _RbAuthServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1)
)
rbAuthServersEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbAuthServerId"),
)
if mibBuilder.loadTexts:
    rbAuthServersEntry.setStatus("current")


class _RbAuthServerId_Type(Integer32):
    """Custom type rbAuthServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RbAuthServerId_Type.__name__ = "Integer32"
_RbAuthServerId_Object = MibTableColumn
rbAuthServerId = _RbAuthServerId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 1),
    _RbAuthServerId_Type()
)
rbAuthServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbAuthServerId.setStatus("current")
_RbAuthServerIpAddress_Type = OctetString
_RbAuthServerIpAddress_Object = MibTableColumn
rbAuthServerIpAddress = _RbAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 2),
    _RbAuthServerIpAddress_Type()
)
rbAuthServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbAuthServerIpAddress.setStatus("current")
_RbAuthServerPort_Type = Integer32
_RbAuthServerPort_Object = MibTableColumn
rbAuthServerPort = _RbAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 3),
    _RbAuthServerPort_Type()
)
rbAuthServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbAuthServerPort.setStatus("current")
_RbAuthServerRowStatus_Type = RowStatus
_RbAuthServerRowStatus_Object = MibTableColumn
rbAuthServerRowStatus = _RbAuthServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 4),
    _RbAuthServerRowStatus_Type()
)
rbAuthServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbAuthServerRowStatus.setStatus("current")
_RadioBridgeQuota_ObjectIdentity = ObjectIdentity
radioBridgeQuota = _RadioBridgeQuota_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 22)
)
_RbFdbQuotaTable_Object = MibTable
rbFdbQuotaTable = _RbFdbQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1)
)
if mibBuilder.loadTexts:
    rbFdbQuotaTable.setStatus("current")
_RbFdbQuotaEntry_Object = MibTableRow
rbFdbQuotaEntry = _RbFdbQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1)
)
rbFdbQuotaEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbFdbQuotaId"),
)
if mibBuilder.loadTexts:
    rbFdbQuotaEntry.setStatus("current")


class _RbFdbQuotaId_Type(Integer32):
    """Custom type rbFdbQuotaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbFdbQuotaId_Type.__name__ = "Integer32"
_RbFdbQuotaId_Object = MibTableColumn
rbFdbQuotaId = _RbFdbQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 1),
    _RbFdbQuotaId_Type()
)
rbFdbQuotaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbFdbQuotaId.setStatus("current")


class _RbFdbQuotaSize_Type(Integer32):
    """Custom type rbFdbQuotaSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RbFdbQuotaSize_Type.__name__ = "Integer32"
_RbFdbQuotaSize_Object = MibTableColumn
rbFdbQuotaSize = _RbFdbQuotaSize_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 2),
    _RbFdbQuotaSize_Type()
)
rbFdbQuotaSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbFdbQuotaSize.setStatus("current")
_RbFdbQuotaRowStatus_Type = RowStatus
_RbFdbQuotaRowStatus_Object = MibTableColumn
rbFdbQuotaRowStatus = _RbFdbQuotaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 3),
    _RbFdbQuotaRowStatus_Type()
)
rbFdbQuotaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbFdbQuotaRowStatus.setStatus("current")
_RbFdbQuotaMaxSize_Type = Counter64
_RbFdbQuotaMaxSize_Object = MibTableColumn
rbFdbQuotaMaxSize = _RbFdbQuotaMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 11),
    _RbFdbQuotaMaxSize_Type()
)
rbFdbQuotaMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaMaxSize.setStatus("current")
_RbFdbQuotaUsedEntries_Type = Counter64
_RbFdbQuotaUsedEntries_Object = MibTableColumn
rbFdbQuotaUsedEntries = _RbFdbQuotaUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 12),
    _RbFdbQuotaUsedEntries_Type()
)
rbFdbQuotaUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaUsedEntries.setStatus("current")
_RbFdbQuotaStaticEntries_Type = Counter64
_RbFdbQuotaStaticEntries_Object = MibTableColumn
rbFdbQuotaStaticEntries = _RbFdbQuotaStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 13),
    _RbFdbQuotaStaticEntries_Type()
)
rbFdbQuotaStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaStaticEntries.setStatus("current")
_RbFdbQuotaDynamicEntries_Type = Counter64
_RbFdbQuotaDynamicEntries_Object = MibTableColumn
rbFdbQuotaDynamicEntries = _RbFdbQuotaDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 14),
    _RbFdbQuotaDynamicEntries_Type()
)
rbFdbQuotaDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaDynamicEntries.setStatus("current")
_RbFdbQuotaUnusedEntries_Type = Counter64
_RbFdbQuotaUnusedEntries_Object = MibTableColumn
rbFdbQuotaUnusedEntries = _RbFdbQuotaUnusedEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 15),
    _RbFdbQuotaUnusedEntries_Type()
)
rbFdbQuotaUnusedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaUnusedEntries.setStatus("current")
_RbFdbEvcQuotaTable_Object = MibTable
rbFdbEvcQuotaTable = _RbFdbEvcQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2)
)
if mibBuilder.loadTexts:
    rbFdbEvcQuotaTable.setStatus("current")
_RbFdbEvcQuotaEntry_Object = MibTableRow
rbFdbEvcQuotaEntry = _RbFdbEvcQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1)
)
rbFdbEvcQuotaEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbFdbEvcQuotaId"),
)
if mibBuilder.loadTexts:
    rbFdbEvcQuotaEntry.setStatus("current")


class _RbFdbEvcQuotaId_Type(Integer32):
    """Custom type rbFdbEvcQuotaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbFdbEvcQuotaId_Type.__name__ = "Integer32"
_RbFdbEvcQuotaId_Object = MibTableColumn
rbFdbEvcQuotaId = _RbFdbEvcQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 1),
    _RbFdbEvcQuotaId_Type()
)
rbFdbEvcQuotaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbFdbEvcQuotaId.setStatus("current")
_RbRefEvcId_Type = Integer32
_RbRefEvcId_Object = MibTableColumn
rbRefEvcId = _RbRefEvcId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 2),
    _RbRefEvcId_Type()
)
rbRefEvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRefEvcId.setStatus("current")
_RbRefFdbQuotaId_Type = Integer32
_RbRefFdbQuotaId_Object = MibTableColumn
rbRefFdbQuotaId = _RbRefFdbQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 3),
    _RbRefFdbQuotaId_Type()
)
rbRefFdbQuotaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRefFdbQuotaId.setStatus("current")
_RbFdbEvcQuotaRowStatus_Type = RowStatus
_RbFdbEvcQuotaRowStatus_Object = MibTableColumn
rbFdbEvcQuotaRowStatus = _RbFdbEvcQuotaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 4),
    _RbFdbEvcQuotaRowStatus_Type()
)
rbFdbEvcQuotaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbFdbEvcQuotaRowStatus.setStatus("current")
_RbFdbExtensionTable_Object = MibTable
rbFdbExtensionTable = _RbFdbExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 3)
)
if mibBuilder.loadTexts:
    rbFdbExtensionTable.setStatus("current")
_RbFdbExtensionEntry_Object = MibTableRow
rbFdbExtensionEntry = _RbFdbExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 3, 1)
)
if mibBuilder.loadTexts:
    rbFdbExtensionEntry.setStatus("current")
_RbRefExtFdbQuotaId_Type = Integer32
_RbRefExtFdbQuotaId_Object = MibTableColumn
rbRefExtFdbQuotaId = _RbRefExtFdbQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 3, 1, 1),
    _RbRefExtFdbQuotaId_Type()
)
rbRefExtFdbQuotaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRefExtFdbQuotaId.setStatus("current")
_RadioBridgePcpProfile_ObjectIdentity = ObjectIdentity
radioBridgePcpProfile = _RadioBridgePcpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 23)
)
_RbPcpWriteProfileTable_Object = MibTable
rbPcpWriteProfileTable = _RbPcpWriteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1)
)
if mibBuilder.loadTexts:
    rbPcpWriteProfileTable.setStatus("current")
_RbPcpWriteProfileEntry_Object = MibTableRow
rbPcpWriteProfileEntry = _RbPcpWriteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1)
)
rbPcpWriteProfileEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbPcpWriteProfileId"),
)
if mibBuilder.loadTexts:
    rbPcpWriteProfileEntry.setStatus("current")


class _RbPcpWriteProfileId_Type(Integer32):
    """Custom type rbPcpWriteProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbPcpWriteProfileId_Type.__name__ = "Integer32"
_RbPcpWriteProfileId_Object = MibTableColumn
rbPcpWriteProfileId = _RbPcpWriteProfileId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1, 1),
    _RbPcpWriteProfileId_Type()
)
rbPcpWriteProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPcpWriteProfileId.setStatus("current")


class _RbPcpWriteProfilePcp_Type(OctetString):
    """Custom type rbPcpWriteProfilePcp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_RbPcpWriteProfilePcp_Type.__name__ = "OctetString"
_RbPcpWriteProfilePcp_Object = MibTableColumn
rbPcpWriteProfilePcp = _RbPcpWriteProfilePcp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1, 2),
    _RbPcpWriteProfilePcp_Type()
)
rbPcpWriteProfilePcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbPcpWriteProfilePcp.setStatus("current")
_RbPcpWriteProfileRowStatus_Type = RowStatus
_RbPcpWriteProfileRowStatus_Object = MibTableColumn
rbPcpWriteProfileRowStatus = _RbPcpWriteProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1, 3),
    _RbPcpWriteProfileRowStatus_Type()
)
rbPcpWriteProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbPcpWriteProfileRowStatus.setStatus("current")
_RadioBridgeSyslog_ObjectIdentity = ObjectIdentity
radioBridgeSyslog = _RadioBridgeSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 24)
)
_RbSyslogTable_Object = MibTable
rbSyslogTable = _RbSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1)
)
if mibBuilder.loadTexts:
    rbSyslogTable.setStatus("current")
_RbSyslogEntry_Object = MibTableRow
rbSyslogEntry = _RbSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1)
)
rbSyslogEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbSyslogId"),
)
if mibBuilder.loadTexts:
    rbSyslogEntry.setStatus("current")
_RbSyslogId_Type = Integer32
_RbSyslogId_Object = MibTableColumn
rbSyslogId = _RbSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1, 1),
    _RbSyslogId_Type()
)
rbSyslogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbSyslogId.setStatus("current")
_RbSyslogServerIp_Type = OctetString
_RbSyslogServerIp_Object = MibTableColumn
rbSyslogServerIp = _RbSyslogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1, 2),
    _RbSyslogServerIp_Type()
)
rbSyslogServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbSyslogServerIp.setStatus("current")
_RbSyslogRowStatus_Type = RowStatus
_RbSyslogRowStatus_Object = MibTableColumn
rbSyslogRowStatus = _RbSyslogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1, 3),
    _RbSyslogRowStatus_Type()
)
rbSyslogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbSyslogRowStatus.setStatus("current")
_RadioBridgeNtp_ObjectIdentity = ObjectIdentity
radioBridgeNtp = _RadioBridgeNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 25)
)
_RbNtpTable_Object = MibTable
rbNtpTable = _RbNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1)
)
if mibBuilder.loadTexts:
    rbNtpTable.setStatus("current")
_RbNtpEntry_Object = MibTableRow
rbNtpEntry = _RbNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1)
)
rbNtpEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbNtpId"),
)
if mibBuilder.loadTexts:
    rbNtpEntry.setStatus("current")
_RbNtpId_Type = Integer32
_RbNtpId_Object = MibTableColumn
rbNtpId = _RbNtpId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 1),
    _RbNtpId_Type()
)
rbNtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbNtpId.setStatus("current")
_RbNtpServerIp_Type = OctetString
_RbNtpServerIp_Object = MibTableColumn
rbNtpServerIp = _RbNtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 2),
    _RbNtpServerIp_Type()
)
rbNtpServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpServerIp.setStatus("current")
_RbNtpSecondaryServerIp_Type = OctetString
_RbNtpSecondaryServerIp_Object = MibTableColumn
rbNtpSecondaryServerIp = _RbNtpSecondaryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 3),
    _RbNtpSecondaryServerIp_Type()
)
rbNtpSecondaryServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpSecondaryServerIp.setStatus("current")


class _RbNtpTmz_Type(Integer32):
    """Custom type rbNtpTmz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 14),
    )


_RbNtpTmz_Type.__name__ = "Integer32"
_RbNtpTmz_Object = MibTableColumn
rbNtpTmz = _RbNtpTmz_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 4),
    _RbNtpTmz_Type()
)
rbNtpTmz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpTmz.setStatus("deprecated")
_RbNtpRowStatus_Type = RowStatus
_RbNtpRowStatus_Object = MibTableColumn
rbNtpRowStatus = _RbNtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 5),
    _RbNtpRowStatus_Type()
)
rbNtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpRowStatus.setStatus("current")
_RadioBridgeLicense_ObjectIdentity = ObjectIdentity
radioBridgeLicense = _RadioBridgeLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 26)
)
_RbLicenseTable_Object = MibTable
rbLicenseTable = _RbLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1)
)
if mibBuilder.loadTexts:
    rbLicenseTable.setStatus("current")
_RbLicenseEntry_Object = MibTableRow
rbLicenseEntry = _RbLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1)
)
rbLicenseEntry.setIndexNames(
    (1, "RADIO-BRIDGE-MIB", "rbLicenseId"),
)
if mibBuilder.loadTexts:
    rbLicenseEntry.setStatus("current")


class _RbLicenseId_Type(DisplayString):
    """Custom type rbLicenseId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbLicenseId_Type.__name__ = "DisplayString"
_RbLicenseId_Object = MibTableColumn
rbLicenseId = _RbLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1, 1),
    _RbLicenseId_Type()
)
rbLicenseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbLicenseId.setStatus("current")
_RbLicenseCurrentValue_Type = Integer32
_RbLicenseCurrentValue_Object = MibTableColumn
rbLicenseCurrentValue = _RbLicenseCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1, 2),
    _RbLicenseCurrentValue_Type()
)
rbLicenseCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbLicenseCurrentValue.setStatus("current")
_RbLicenseMaxValue_Type = Integer32
_RbLicenseMaxValue_Object = MibTableColumn
rbLicenseMaxValue = _RbLicenseMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1, 3),
    _RbLicenseMaxValue_Type()
)
rbLicenseMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbLicenseMaxValue.setStatus("current")
_RadioBridgeMultiHaulRadio_ObjectIdentity = ObjectIdentity
radioBridgeMultiHaulRadio = _RadioBridgeMultiHaulRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 27)
)
_RbMhBaseUnitTable_Object = MibTable
rbMhBaseUnitTable = _RbMhBaseUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1)
)
if mibBuilder.loadTexts:
    rbMhBaseUnitTable.setStatus("current")
_RbMhBaseUnitEntry_Object = MibTableRow
rbMhBaseUnitEntry = _RbMhBaseUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1)
)
rbMhBaseUnitEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "buNumber"),
)
if mibBuilder.loadTexts:
    rbMhBaseUnitEntry.setStatus("current")
_BuNumber_Type = Integer32
_BuNumber_Object = MibTableColumn
buNumber = _BuNumber_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 1),
    _BuNumber_Type()
)
buNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    buNumber.setStatus("current")
_BuSelfMac_Type = MacAddress
_BuSelfMac_Object = MibTableColumn
buSelfMac = _BuSelfMac_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 2),
    _BuSelfMac_Type()
)
buSelfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buSelfMac.setStatus("current")
_BuSSID_Type = DisplayString
_BuSSID_Object = MibTableColumn
buSSID = _BuSSID_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 3),
    _BuSSID_Type()
)
buSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buSSID.setStatus("current")
_BuUserPassword_Type = DisplayString
_BuUserPassword_Object = MibTableColumn
buUserPassword = _BuUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 4),
    _BuUserPassword_Type()
)
buUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buUserPassword.setStatus("current")


class _BuFrequency_Type(Integer32):
    """Custom type buFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel-1", 1),
          ("channel-2", 2),
          ("channel-3", 3))
    )


_BuFrequency_Type.__name__ = "Integer32"
_BuFrequency_Object = MibTableColumn
buFrequency = _BuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 5),
    _BuFrequency_Type()
)
buFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buFrequency.setStatus("current")
_BuSsidVisible_Type = TruthValue
_BuSsidVisible_Object = MibTableColumn
buSsidVisible = _BuSsidVisible_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 6),
    _BuSsidVisible_Type()
)
buSsidVisible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buSsidVisible.setStatus("current")
_BuGuestConnection_Type = TruthValue
_BuGuestConnection_Object = MibTableColumn
buGuestConnection = _BuGuestConnection_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 7),
    _BuGuestConnection_Type()
)
buGuestConnection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buGuestConnection.setStatus("current")


class _BuMaxTerminalUnits_Type(Integer32):
    """Custom type buMaxTerminalUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_BuMaxTerminalUnits_Type.__name__ = "Integer32"
_BuMaxTerminalUnits_Object = MibTableColumn
buMaxTerminalUnits = _BuMaxTerminalUnits_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 8),
    _BuMaxTerminalUnits_Type()
)
buMaxTerminalUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buMaxTerminalUnits.setStatus("current")
_BuTxThroughput_Type = Integer32
_BuTxThroughput_Object = MibTableColumn
buTxThroughput = _BuTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 9),
    _BuTxThroughput_Type()
)
buTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buTxThroughput.setStatus("current")
_BuRxThroughput_Type = Integer32
_BuRxThroughput_Object = MibTableColumn
buRxThroughput = _BuRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 10),
    _BuRxThroughput_Type()
)
buRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buRxThroughput.setStatus("current")
_BuReset_Type = Integer32
_BuReset_Object = MibTableColumn
buReset = _BuReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 11),
    _BuReset_Type()
)
buReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buReset.setStatus("current")


class _BuAccessControl_Type(Integer32):
    """Custom type buAccessControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("by-mac", 1),
          ("by-name", 2))
    )


_BuAccessControl_Type.__name__ = "Integer32"
_BuAccessControl_Object = MibTableColumn
buAccessControl = _BuAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 12),
    _BuAccessControl_Type()
)
buAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    buAccessControl.setStatus("current")
_BuRxOctets_Type = Counter64
_BuRxOctets_Object = MibTableColumn
buRxOctets = _BuRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 31),
    _BuRxOctets_Type()
)
buRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buRxOctets.setStatus("current")
_BuTxOctets_Type = Counter64
_BuTxOctets_Object = MibTableColumn
buTxOctets = _BuTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 32),
    _BuTxOctets_Type()
)
buTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buTxOctets.setStatus("current")
_BuRxPackets_Type = Counter64
_BuRxPackets_Object = MibTableColumn
buRxPackets = _BuRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 33),
    _BuRxPackets_Type()
)
buRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buRxPackets.setStatus("current")
_BuTxPackets_Type = Counter64
_BuTxPackets_Object = MibTableColumn
buTxPackets = _BuTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 34),
    _BuTxPackets_Type()
)
buTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buTxPackets.setStatus("current")
_BuRxDiscards_Type = Counter64
_BuRxDiscards_Object = MibTableColumn
buRxDiscards = _BuRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 35),
    _BuRxDiscards_Type()
)
buRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buRxDiscards.setStatus("current")
_BuTxDiscards_Type = Counter64
_BuTxDiscards_Object = MibTableColumn
buTxDiscards = _BuTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 36),
    _BuTxDiscards_Type()
)
buTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buTxDiscards.setStatus("current")
_BuRxErrors_Type = Counter64
_BuRxErrors_Object = MibTableColumn
buRxErrors = _BuRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 37),
    _BuRxErrors_Type()
)
buRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buRxErrors.setStatus("current")
_BuTxErrors_Type = Counter64
_BuTxErrors_Object = MibTableColumn
buTxErrors = _BuTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 1, 1, 38),
    _BuTxErrors_Type()
)
buTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buTxErrors.setStatus("current")
_RbMhTerminalUnitTable_Object = MibTable
rbMhTerminalUnitTable = _RbMhTerminalUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2)
)
if mibBuilder.loadTexts:
    rbMhTerminalUnitTable.setStatus("current")
_RbMhTerminalUnitEntry_Object = MibTableRow
rbMhTerminalUnitEntry = _RbMhTerminalUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1)
)
rbMhTerminalUnitEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "tuNumber"),
)
if mibBuilder.loadTexts:
    rbMhTerminalUnitEntry.setStatus("current")
_TuNumber_Type = Integer32
_TuNumber_Object = MibTableColumn
tuNumber = _TuNumber_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 1),
    _TuNumber_Type()
)
tuNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tuNumber.setStatus("current")
_TuSelfMac_Type = MacAddress
_TuSelfMac_Object = MibTableColumn
tuSelfMac = _TuSelfMac_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 2),
    _TuSelfMac_Type()
)
tuSelfMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuSelfMac.setStatus("current")
_TuSSID_Type = DisplayString
_TuSSID_Object = MibTableColumn
tuSSID = _TuSSID_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 3),
    _TuSSID_Type()
)
tuSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuSSID.setStatus("current")
_TuUserPassword_Type = DisplayString
_TuUserPassword_Object = MibTableColumn
tuUserPassword = _TuUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 4),
    _TuUserPassword_Type()
)
tuUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuUserPassword.setStatus("current")


class _TuFrequency_Type(Integer32):
    """Custom type tuFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("channel-1", 1),
          ("channel-2", 2),
          ("channel-3", 3))
    )


_TuFrequency_Type.__name__ = "Integer32"
_TuFrequency_Object = MibTableColumn
tuFrequency = _TuFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 5),
    _TuFrequency_Type()
)
tuFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuFrequency.setStatus("current")
_TuTxThroughput_Type = Integer32
_TuTxThroughput_Object = MibTableColumn
tuTxThroughput = _TuTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 6),
    _TuTxThroughput_Type()
)
tuTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuTxThroughput.setStatus("current")
_TuRxThroughput_Type = Integer32
_TuRxThroughput_Object = MibTableColumn
tuRxThroughput = _TuRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 7),
    _TuRxThroughput_Type()
)
tuRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuRxThroughput.setStatus("current")
_TuScanMode_Type = TruthValue
_TuScanMode_Object = MibTableColumn
tuScanMode = _TuScanMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 8),
    _TuScanMode_Type()
)
tuScanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuScanMode.setStatus("current")


class _TuStatus_Type(Integer32):
    """Custom type tuStatus based on Integer32"""
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
        *(("scanning", 1),
          ("authentication", 2),
          ("association", 3),
          ("association-rejected", 4),
          ("authentication-rejected", 5),
          ("cannot-connect-guests", 6),
          ("connected", 7))
    )


_TuStatus_Type.__name__ = "Integer32"
_TuStatus_Object = MibTableColumn
tuStatus = _TuStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 9),
    _TuStatus_Type()
)
tuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuStatus.setStatus("current")
_TuBuMac_Type = MacAddress
_TuBuMac_Object = MibTableColumn
tuBuMac = _TuBuMac_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 10),
    _TuBuMac_Type()
)
tuBuMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuBuMac.setStatus("current")
_TuTxMcs_Type = Integer32
_TuTxMcs_Object = MibTableColumn
tuTxMcs = _TuTxMcs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 11),
    _TuTxMcs_Type()
)
tuTxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuTxMcs.setStatus("current")
_TuSignalQuality_Type = Integer32
_TuSignalQuality_Object = MibTableColumn
tuSignalQuality = _TuSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 12),
    _TuSignalQuality_Type()
)
tuSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuSignalQuality.setStatus("current")


class _TuTxRateLimiter_Type(Integer32):
    """Custom type tuTxRateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2500),
    )


_TuTxRateLimiter_Type.__name__ = "Integer32"
_TuTxRateLimiter_Object = MibTableColumn
tuTxRateLimiter = _TuTxRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 13),
    _TuTxRateLimiter_Type()
)
tuTxRateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuTxRateLimiter.setStatus("current")
_TuBuScan_Type = DisplayString
_TuBuScan_Object = MibTableColumn
tuBuScan = _TuBuScan_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 14),
    _TuBuScan_Type()
)
tuBuScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuBuScan.setStatus("current")
_TuReset_Type = Integer32
_TuReset_Object = MibTableColumn
tuReset = _TuReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 15),
    _TuReset_Type()
)
tuReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tuReset.setStatus("current")
_TuConnectTime_Type = TimeTicks
_TuConnectTime_Object = MibTableColumn
tuConnectTime = _TuConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 16),
    _TuConnectTime_Type()
)
tuConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuConnectTime.setStatus("current")
_TuRssi_Type = Integer32
_TuRssi_Object = MibTableColumn
tuRssi = _TuRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 17),
    _TuRssi_Type()
)
tuRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuRssi.setStatus("current")
_TuTxPackets_Type = Counter64
_TuTxPackets_Object = MibTableColumn
tuTxPackets = _TuTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 31),
    _TuTxPackets_Type()
)
tuTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuTxPackets.setStatus("current")
_TuRxPackets_Type = Counter64
_TuRxPackets_Object = MibTableColumn
tuRxPackets = _TuRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 32),
    _TuRxPackets_Type()
)
tuRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuRxPackets.setStatus("current")
_TuTxBytes_Type = Counter64
_TuTxBytes_Object = MibTableColumn
tuTxBytes = _TuTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 33),
    _TuTxBytes_Type()
)
tuTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuTxBytes.setStatus("current")
_TuRxBytes_Type = Counter64
_TuRxBytes_Object = MibTableColumn
tuRxBytes = _TuRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 34),
    _TuRxBytes_Type()
)
tuRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuRxBytes.setStatus("current")
_TuTxErrors_Type = Counter64
_TuTxErrors_Object = MibTableColumn
tuTxErrors = _TuTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 35),
    _TuTxErrors_Type()
)
tuTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuTxErrors.setStatus("current")
_TuRxDropped_Type = Counter64
_TuRxDropped_Object = MibTableColumn
tuRxDropped = _TuRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 2, 1, 36),
    _TuRxDropped_Type()
)
tuRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuRxDropped.setStatus("current")
_RbMhTerminalUnitMcsTable_Object = MibTable
rbMhTerminalUnitMcsTable = _RbMhTerminalUnitMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 3)
)
if mibBuilder.loadTexts:
    rbMhTerminalUnitMcsTable.setStatus("current")
_RbMhTerminalUnitMcsEntry_Object = MibTableRow
rbMhTerminalUnitMcsEntry = _RbMhTerminalUnitMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 3, 1)
)
rbMhTerminalUnitMcsEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "tuNumber"),
    (0, "RADIO-BRIDGE-MIB", "mcsIndex"),
)
if mibBuilder.loadTexts:
    rbMhTerminalUnitMcsEntry.setStatus("current")
_McsIndex_Type = Integer32
_McsIndex_Object = MibTableColumn
mcsIndex = _McsIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 3, 1, 1),
    _McsIndex_Type()
)
mcsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcsIndex.setStatus("current")
_TuRxMcs_Type = Counter64
_TuRxMcs_Object = MibTableColumn
tuRxMcs = _TuRxMcs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 3, 1, 2),
    _TuRxMcs_Type()
)
tuRxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuRxMcs.setStatus("current")
_RbMhRemTerminalUnitTable_Object = MibTable
rbMhRemTerminalUnitTable = _RbMhRemTerminalUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4)
)
if mibBuilder.loadTexts:
    rbMhRemTerminalUnitTable.setStatus("current")
_RbMhRemTerminalUnitEntry_Object = MibTableRow
rbMhRemTerminalUnitEntry = _RbMhRemTerminalUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1)
)
rbMhRemTerminalUnitEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "remTuNumber"),
)
if mibBuilder.loadTexts:
    rbMhRemTerminalUnitEntry.setStatus("current")
_RemTuNumber_Type = Integer32
_RemTuNumber_Object = MibTableColumn
remTuNumber = _RemTuNumber_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 1),
    _RemTuNumber_Type()
)
remTuNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remTuNumber.setStatus("current")
_RemTuPort_Type = Integer32
_RemTuPort_Object = MibTableColumn
remTuPort = _RemTuPort_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 2),
    _RemTuPort_Type()
)
remTuPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remTuPort.setStatus("current")
_RemTuMac_Type = MacAddress
_RemTuMac_Object = MibTableColumn
remTuMac = _RemTuMac_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 3),
    _RemTuMac_Type()
)
remTuMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remTuMac.setStatus("current")
_RemTuName_Type = DisplayString
_RemTuName_Object = MibTableColumn
remTuName = _RemTuName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 4),
    _RemTuName_Type()
)
remTuName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remTuName.setStatus("current")


class _RemTuStatus_Type(Integer32):
    """Custom type remTuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 1),
          ("connected", 2))
    )


_RemTuStatus_Type.__name__ = "Integer32"
_RemTuStatus_Object = MibTableColumn
remTuStatus = _RemTuStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 5),
    _RemTuStatus_Type()
)
remTuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuStatus.setStatus("current")


class _RemTuAssociation_Type(Integer32):
    """Custom type remTuAssociation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("managed", 1),
          ("guest", 2))
    )


_RemTuAssociation_Type.__name__ = "Integer32"
_RemTuAssociation_Object = MibTableColumn
remTuAssociation = _RemTuAssociation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 6),
    _RemTuAssociation_Type()
)
remTuAssociation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remTuAssociation.setStatus("current")
_RemTuTxMcs_Type = Integer32
_RemTuTxMcs_Object = MibTableColumn
remTuTxMcs = _RemTuTxMcs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 7),
    _RemTuTxMcs_Type()
)
remTuTxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuTxMcs.setStatus("current")
_RemTuSignalQuality_Type = Integer32
_RemTuSignalQuality_Object = MibTableColumn
remTuSignalQuality = _RemTuSignalQuality_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 8),
    _RemTuSignalQuality_Type()
)
remTuSignalQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuSignalQuality.setStatus("current")


class _RemTuTxRateLimiter_Type(Integer32):
    """Custom type remTuTxRateLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2500),
    )


_RemTuTxRateLimiter_Type.__name__ = "Integer32"
_RemTuTxRateLimiter_Object = MibTableColumn
remTuTxRateLimiter = _RemTuTxRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 9),
    _RemTuTxRateLimiter_Type()
)
remTuTxRateLimiter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remTuTxRateLimiter.setStatus("current")
_RemTuRowStatus_Type = RowStatus
_RemTuRowStatus_Object = MibTableColumn
remTuRowStatus = _RemTuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 10),
    _RemTuRowStatus_Type()
)
remTuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remTuRowStatus.setStatus("current")
_RemTuConnectTime_Type = TimeTicks
_RemTuConnectTime_Object = MibTableColumn
remTuConnectTime = _RemTuConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 11),
    _RemTuConnectTime_Type()
)
remTuConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuConnectTime.setStatus("current")
_RemTuRssi_Type = Integer32
_RemTuRssi_Object = MibTableColumn
remTuRssi = _RemTuRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 12),
    _RemTuRssi_Type()
)
remTuRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuRssi.setStatus("current")
_RemTuTxSector_Type = Integer32
_RemTuTxSector_Object = MibTableColumn
remTuTxSector = _RemTuTxSector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 13),
    _RemTuTxSector_Type()
)
remTuTxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuTxSector.setStatus("current")
_RemTuRemTxSector_Type = Integer32
_RemTuRemTxSector_Object = MibTableColumn
remTuRemTxSector = _RemTuRemTxSector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 14),
    _RemTuRemTxSector_Type()
)
remTuRemTxSector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuRemTxSector.setStatus("current")
_RemTuTxPackets_Type = Counter64
_RemTuTxPackets_Object = MibTableColumn
remTuTxPackets = _RemTuTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 31),
    _RemTuTxPackets_Type()
)
remTuTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuTxPackets.setStatus("current")
_RemTuRxPackets_Type = Counter64
_RemTuRxPackets_Object = MibTableColumn
remTuRxPackets = _RemTuRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 32),
    _RemTuRxPackets_Type()
)
remTuRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuRxPackets.setStatus("current")
_RemTuTxBytes_Type = Counter64
_RemTuTxBytes_Object = MibTableColumn
remTuTxBytes = _RemTuTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 33),
    _RemTuTxBytes_Type()
)
remTuTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuTxBytes.setStatus("current")
_RemTuRxBytes_Type = Counter64
_RemTuRxBytes_Object = MibTableColumn
remTuRxBytes = _RemTuRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 34),
    _RemTuRxBytes_Type()
)
remTuRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuRxBytes.setStatus("current")
_RemTuTxErrors_Type = Counter64
_RemTuTxErrors_Object = MibTableColumn
remTuTxErrors = _RemTuTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 35),
    _RemTuTxErrors_Type()
)
remTuTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuTxErrors.setStatus("current")
_RemTuRxDropped_Type = Counter64
_RemTuRxDropped_Object = MibTableColumn
remTuRxDropped = _RemTuRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 4, 1, 36),
    _RemTuRxDropped_Type()
)
remTuRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuRxDropped.setStatus("current")
_RbMhRemTerminalUnitMcsTable_Object = MibTable
rbMhRemTerminalUnitMcsTable = _RbMhRemTerminalUnitMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 5)
)
if mibBuilder.loadTexts:
    rbMhRemTerminalUnitMcsTable.setStatus("current")
_RbMhRemTerminalUnitMcsEntry_Object = MibTableRow
rbMhRemTerminalUnitMcsEntry = _RbMhRemTerminalUnitMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 5, 1)
)
rbMhRemTerminalUnitMcsEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "tuNumber"),
    (0, "RADIO-BRIDGE-MIB", "mcsIndex"),
)
if mibBuilder.loadTexts:
    rbMhRemTerminalUnitMcsEntry.setStatus("current")
_RemTuRxMcs_Type = Counter64
_RemTuRxMcs_Object = MibTableColumn
remTuRxMcs = _RemTuRxMcs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 27, 5, 1, 2),
    _RemTuRxMcs_Type()
)
remTuRxMcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remTuRxMcs.setStatus("current")
_RadioBridgeMultiHaulNetwork_ObjectIdentity = ObjectIdentity
radioBridgeMultiHaulNetwork = _RadioBridgeMultiHaulNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 28)
)
_RbMhBridgeTable_Object = MibTable
rbMhBridgeTable = _RbMhBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1)
)
if mibBuilder.loadTexts:
    rbMhBridgeTable.setStatus("current")
_RbMhBridgeEntry_Object = MibTableRow
rbMhBridgeEntry = _RbMhBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1, 1)
)
rbMhBridgeEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "mhBridgeId"),
)
if mibBuilder.loadTexts:
    rbMhBridgeEntry.setStatus("current")
_MhBridgeId_Type = Integer32
_MhBridgeId_Object = MibTableColumn
mhBridgeId = _MhBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1, 1, 1),
    _MhBridgeId_Type()
)
mhBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mhBridgeId.setStatus("current")
_MhBridgeName_Type = DisplayString
_MhBridgeName_Object = MibTableColumn
mhBridgeName = _MhBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1, 1, 2),
    _MhBridgeName_Type()
)
mhBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mhBridgeName.setStatus("current")
_MhBridgePorts_Type = MhBridgePortsList
_MhBridgePorts_Object = MibTableColumn
mhBridgePorts = _MhBridgePorts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1, 1, 3),
    _MhBridgePorts_Type()
)
mhBridgePorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mhBridgePorts.setStatus("current")
_MhBridgePortsCli_Type = DisplayString
_MhBridgePortsCli_Object = MibTableColumn
mhBridgePortsCli = _MhBridgePortsCli_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1, 1, 4),
    _MhBridgePortsCli_Type()
)
mhBridgePortsCli.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mhBridgePortsCli.setStatus("current")
_MhBridgeRowStatus_Type = RowStatus
_MhBridgeRowStatus_Object = MibTableColumn
mhBridgeRowStatus = _MhBridgeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 1, 1, 5),
    _MhBridgeRowStatus_Type()
)
mhBridgeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mhBridgeRowStatus.setStatus("current")
_RbMhBridgePortTable_Object = MibTable
rbMhBridgePortTable = _RbMhBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2)
)
if mibBuilder.loadTexts:
    rbMhBridgePortTable.setStatus("current")
_RbMhBridgePortEntry_Object = MibTableRow
rbMhBridgePortEntry = _RbMhBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1)
)
rbMhBridgePortEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "mhBridgePortId"),
)
if mibBuilder.loadTexts:
    rbMhBridgePortEntry.setStatus("current")
_MhBridgePortId_Type = MhBridgePort
_MhBridgePortId_Object = MibTableColumn
mhBridgePortId = _MhBridgePortId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 1),
    _MhBridgePortId_Type()
)
mhBridgePortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mhBridgePortId.setStatus("current")
_MhBridgePortEthType_Type = DisplayString
_MhBridgePortEthType_Object = MibTableColumn
mhBridgePortEthType = _MhBridgePortEthType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 3),
    _MhBridgePortEthType_Type()
)
mhBridgePortEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortEthType.setStatus("current")
_MhBridgePortOwner_Type = Integer32
_MhBridgePortOwner_Object = MibTableColumn
mhBridgePortOwner = _MhBridgePortOwner_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 4),
    _MhBridgePortOwner_Type()
)
mhBridgePortOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortOwner.setStatus("current")
_MhBridgePortCliName_Type = DisplayString
_MhBridgePortCliName_Object = MibTableColumn
mhBridgePortCliName = _MhBridgePortCliName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 5),
    _MhBridgePortCliName_Type()
)
mhBridgePortCliName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortCliName.setStatus("current")
_MhBridgePortInOctets_Type = Counter64
_MhBridgePortInOctets_Object = MibTableColumn
mhBridgePortInOctets = _MhBridgePortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 31),
    _MhBridgePortInOctets_Type()
)
mhBridgePortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortInOctets.setStatus("current")
_MhBridgePortInPackets_Type = Counter64
_MhBridgePortInPackets_Object = MibTableColumn
mhBridgePortInPackets = _MhBridgePortInPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 32),
    _MhBridgePortInPackets_Type()
)
mhBridgePortInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortInPackets.setStatus("current")
_MhBridgePortInMcastPackets_Type = Counter64
_MhBridgePortInMcastPackets_Object = MibTableColumn
mhBridgePortInMcastPackets = _MhBridgePortInMcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 33),
    _MhBridgePortInMcastPackets_Type()
)
mhBridgePortInMcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortInMcastPackets.setStatus("current")
_MhBridgePortInErrorPackets_Type = Counter64
_MhBridgePortInErrorPackets_Object = MibTableColumn
mhBridgePortInErrorPackets = _MhBridgePortInErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 34),
    _MhBridgePortInErrorPackets_Type()
)
mhBridgePortInErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortInErrorPackets.setStatus("current")
_MhBridgePortInDiscardPackets_Type = Counter64
_MhBridgePortInDiscardPackets_Object = MibTableColumn
mhBridgePortInDiscardPackets = _MhBridgePortInDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 35),
    _MhBridgePortInDiscardPackets_Type()
)
mhBridgePortInDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortInDiscardPackets.setStatus("current")
_MhBridgePortOutOctets_Type = Counter64
_MhBridgePortOutOctets_Object = MibTableColumn
mhBridgePortOutOctets = _MhBridgePortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 36),
    _MhBridgePortOutOctets_Type()
)
mhBridgePortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortOutOctets.setStatus("current")
_MhBridgePortOutPackets_Type = Counter64
_MhBridgePortOutPackets_Object = MibTableColumn
mhBridgePortOutPackets = _MhBridgePortOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 37),
    _MhBridgePortOutPackets_Type()
)
mhBridgePortOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortOutPackets.setStatus("current")
_MhBridgePortOutErrorPackets_Type = Counter64
_MhBridgePortOutErrorPackets_Object = MibTableColumn
mhBridgePortOutErrorPackets = _MhBridgePortOutErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 38),
    _MhBridgePortOutErrorPackets_Type()
)
mhBridgePortOutErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortOutErrorPackets.setStatus("current")
_MhBridgePortOutDiscardPackets_Type = Counter64
_MhBridgePortOutDiscardPackets_Object = MibTableColumn
mhBridgePortOutDiscardPackets = _MhBridgePortOutDiscardPackets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 2, 1, 39),
    _MhBridgePortOutDiscardPackets_Type()
)
mhBridgePortOutDiscardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhBridgePortOutDiscardPackets.setStatus("current")
_RbMhFdbTable_Object = MibTable
rbMhFdbTable = _RbMhFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 3)
)
if mibBuilder.loadTexts:
    rbMhFdbTable.setStatus("current")
_RbMhFdbEntry_Object = MibTableRow
rbMhFdbEntry = _RbMhFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 3, 1)
)
rbMhFdbEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "mhFdbBridgeId"),
    (0, "RADIO-BRIDGE-MIB", "mhFdbAddress"),
)
if mibBuilder.loadTexts:
    rbMhFdbEntry.setStatus("current")
_MhFdbBridgeId_Type = Integer32
_MhFdbBridgeId_Object = MibTableColumn
mhFdbBridgeId = _MhFdbBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 3, 1, 1),
    _MhFdbBridgeId_Type()
)
mhFdbBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhFdbBridgeId.setStatus("current")
_MhFdbAddress_Type = MacAddress
_MhFdbAddress_Object = MibTableColumn
mhFdbAddress = _MhFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 3, 1, 2),
    _MhFdbAddress_Type()
)
mhFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhFdbAddress.setStatus("current")
_MhFdbPortId_Type = MhBridgePort
_MhFdbPortId_Object = MibTableColumn
mhFdbPortId = _MhFdbPortId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 3, 1, 3),
    _MhFdbPortId_Type()
)
mhFdbPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhFdbPortId.setStatus("current")


class _MhFdbStatus_Type(Integer32):
    """Custom type mhFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("learned", 3),
          ("self", 4),
          ("mgmt", 5))
    )


_MhFdbStatus_Type.__name__ = "Integer32"
_MhFdbStatus_Object = MibTableColumn
mhFdbStatus = _MhFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 28, 3, 1, 4),
    _MhFdbStatus_Type()
)
mhFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhFdbStatus.setStatus("current")
_RadioBridge8021x_ObjectIdentity = ObjectIdentity
radioBridge8021x = _RadioBridge8021x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 29)
)
_Rb8021xCommonTable_Object = MibTable
rb8021xCommonTable = _Rb8021xCommonTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 1)
)
if mibBuilder.loadTexts:
    rb8021xCommonTable.setStatus("current")
_Rb8021xCommonEntry_Object = MibTableRow
rb8021xCommonEntry = _Rb8021xCommonEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 1, 1)
)
rb8021xCommonEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rb8021xCommonNumber"),
)
if mibBuilder.loadTexts:
    rb8021xCommonEntry.setStatus("current")
_Rb8021xCommonNumber_Type = Integer32
_Rb8021xCommonNumber_Object = MibTableColumn
rb8021xCommonNumber = _Rb8021xCommonNumber_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 1, 1, 1),
    _Rb8021xCommonNumber_Type()
)
rb8021xCommonNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rb8021xCommonNumber.setStatus("current")
_Rb8021xCommonNasId_Type = DisplayString
_Rb8021xCommonNasId_Object = MibTableColumn
rb8021xCommonNasId = _Rb8021xCommonNasId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 1, 1, 2),
    _Rb8021xCommonNasId_Type()
)
rb8021xCommonNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xCommonNasId.setStatus("current")
_Rb8021xCommonNasIpIndex_Type = Integer32
_Rb8021xCommonNasIpIndex_Object = MibTableColumn
rb8021xCommonNasIpIndex = _Rb8021xCommonNasIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 1, 1, 3),
    _Rb8021xCommonNasIpIndex_Type()
)
rb8021xCommonNasIpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xCommonNasIpIndex.setStatus("current")
_Rb8021xCommonReauthPeriod_Type = Integer32
_Rb8021xCommonReauthPeriod_Object = MibTableColumn
rb8021xCommonReauthPeriod = _Rb8021xCommonReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 1, 1, 4),
    _Rb8021xCommonReauthPeriod_Type()
)
rb8021xCommonReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xCommonReauthPeriod.setStatus("current")
_Rb8021xServerTable_Object = MibTable
rb8021xServerTable = _Rb8021xServerTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 2)
)
if mibBuilder.loadTexts:
    rb8021xServerTable.setStatus("current")
_Rb8021xServerEntry_Object = MibTableRow
rb8021xServerEntry = _Rb8021xServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 2, 1)
)
rb8021xServerEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rb8021xServerId"),
)
if mibBuilder.loadTexts:
    rb8021xServerEntry.setStatus("current")
_Rb8021xServerId_Type = Integer32
_Rb8021xServerId_Object = MibTableColumn
rb8021xServerId = _Rb8021xServerId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 2, 1, 1),
    _Rb8021xServerId_Type()
)
rb8021xServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rb8021xServerId.setStatus("current")
_Rb8021xServerIpAddr_Type = IpAddress
_Rb8021xServerIpAddr_Object = MibTableColumn
rb8021xServerIpAddr = _Rb8021xServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 2, 1, 2),
    _Rb8021xServerIpAddr_Type()
)
rb8021xServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xServerIpAddr.setStatus("current")
_Rb8021xServerPort_Type = Integer32
_Rb8021xServerPort_Object = MibTableColumn
rb8021xServerPort = _Rb8021xServerPort_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 2, 1, 3),
    _Rb8021xServerPort_Type()
)
rb8021xServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xServerPort.setStatus("current")
_Rb8021xServerSharedSecret_Type = DisplayString
_Rb8021xServerSharedSecret_Object = MibTableColumn
rb8021xServerSharedSecret = _Rb8021xServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 2, 1, 4),
    _Rb8021xServerSharedSecret_Type()
)
rb8021xServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xServerSharedSecret.setStatus("current")
_Rb8021xTable_Object = MibTable
rb8021xTable = _Rb8021xTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 3)
)
if mibBuilder.loadTexts:
    rb8021xTable.setStatus("current")
_Rb8021xEntry_Object = MibTableRow
rb8021xEntry = _Rb8021xEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 3, 1)
)
rb8021xEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rb8021xEthNum"),
)
if mibBuilder.loadTexts:
    rb8021xEntry.setStatus("current")
_Rb8021xEthNum_Type = Integer32
_Rb8021xEthNum_Object = MibTableColumn
rb8021xEthNum = _Rb8021xEthNum_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 3, 1, 1),
    _Rb8021xEthNum_Type()
)
rb8021xEthNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rb8021xEthNum.setStatus("current")


class _Rb8021xAdmin_Type(Integer32):
    """Custom type rb8021xAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Rb8021xAdmin_Type.__name__ = "Integer32"
_Rb8021xAdmin_Object = MibTableColumn
rb8021xAdmin = _Rb8021xAdmin_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 3, 1, 2),
    _Rb8021xAdmin_Type()
)
rb8021xAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rb8021xAdmin.setStatus("current")


class _Rb8021xStatus_Type(Integer32):
    """Custom type rb8021xStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-controlled", 1),
          ("controlled-open", 2),
          ("controlled-closed", 3))
    )


_Rb8021xStatus_Type.__name__ = "Integer32"
_Rb8021xStatus_Object = MibTableColumn
rb8021xStatus = _Rb8021xStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 29, 3, 1, 3),
    _Rb8021xStatus_Type()
)
rb8021xStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rb8021xStatus.setStatus("current")
_RadioBridgeTuConfig_ObjectIdentity = ObjectIdentity
radioBridgeTuConfig = _RadioBridgeTuConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 30)
)
_RbTuConfigTable_Object = MibTable
rbTuConfigTable = _RbTuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1)
)
if mibBuilder.loadTexts:
    rbTuConfigTable.setStatus("current")
_RbTuConfigEntry_Object = MibTableRow
rbTuConfigEntry = _RbTuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1, 1)
)
rbTuConfigEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "tuConfigSnmpIndex"),
)
if mibBuilder.loadTexts:
    rbTuConfigEntry.setStatus("current")
_TuConfigSnmpIndex_Type = Integer32
_TuConfigSnmpIndex_Object = MibTableColumn
tuConfigSnmpIndex = _TuConfigSnmpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1, 1, 1),
    _TuConfigSnmpIndex_Type()
)
tuConfigSnmpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuConfigSnmpIndex.setStatus("current")
_TuConfigTuId_Type = Integer32
_TuConfigTuId_Object = MibTableColumn
tuConfigTuId = _TuConfigTuId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1, 1, 2),
    _TuConfigTuId_Type()
)
tuConfigTuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuConfigTuId.setStatus("current")
_TuConfigString_Type = DisplayString
_TuConfigString_Object = MibTableColumn
tuConfigString = _TuConfigString_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1, 1, 3),
    _TuConfigString_Type()
)
tuConfigString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tuConfigString.setStatus("current")
_TuConfigStatus_Type = DisplayString
_TuConfigStatus_Object = MibTableColumn
tuConfigStatus = _TuConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1, 1, 4),
    _TuConfigStatus_Type()
)
tuConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tuConfigStatus.setStatus("current")
_TuConfigRowStatus_Type = RowStatus
_TuConfigRowStatus_Object = MibTableColumn
tuConfigRowStatus = _TuConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 30, 1, 1, 5),
    _TuConfigRowStatus_Type()
)
tuConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tuConfigRowStatus.setStatus("current")
_RadioBridgeRules_ObjectIdentity = ObjectIdentity
radioBridgeRules = _RadioBridgeRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 31)
)
_RbRulesBridgePortTable_Object = MibTable
rbRulesBridgePortTable = _RbRulesBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1)
)
if mibBuilder.loadTexts:
    rbRulesBridgePortTable.setStatus("current")
_RbRulesBridgePortEntry_Object = MibTableRow
rbRulesBridgePortEntry = _RbRulesBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1)
)
rbRulesBridgePortEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbRulesBridgePortId"),
)
if mibBuilder.loadTexts:
    rbRulesBridgePortEntry.setStatus("current")
_RbRulesBridgePortId_Type = Integer32
_RbRulesBridgePortId_Object = MibTableColumn
rbRulesBridgePortId = _RbRulesBridgePortId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1, 1),
    _RbRulesBridgePortId_Type()
)
rbRulesBridgePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRulesBridgePortId.setStatus("current")


class _RbRulesBridgePortType_Type(Integer32):
    """Custom type rbRulesBridgePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("customer", 0),
          ("provider", 1))
    )


_RbRulesBridgePortType_Type.__name__ = "Integer32"
_RbRulesBridgePortType_Object = MibTableColumn
rbRulesBridgePortType = _RbRulesBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1, 2),
    _RbRulesBridgePortType_Type()
)
rbRulesBridgePortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRulesBridgePortType.setStatus("current")
_RbRulesBridgePortMemberVlans_Type = RulesVlansList
_RbRulesBridgePortMemberVlans_Object = MibTableColumn
rbRulesBridgePortMemberVlans = _RbRulesBridgePortMemberVlans_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1, 3),
    _RbRulesBridgePortMemberVlans_Type()
)
rbRulesBridgePortMemberVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRulesBridgePortMemberVlans.setStatus("current")
_RbRulesBridgePortPvid_Type = Integer32
_RbRulesBridgePortPvid_Object = MibTableColumn
rbRulesBridgePortPvid = _RbRulesBridgePortPvid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1, 4),
    _RbRulesBridgePortPvid_Type()
)
rbRulesBridgePortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRulesBridgePortPvid.setStatus("current")
_RbRulesBridgePortExcludeVlans_Type = OctetString
_RbRulesBridgePortExcludeVlans_Object = MibTableColumn
rbRulesBridgePortExcludeVlans = _RbRulesBridgePortExcludeVlans_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1, 5),
    _RbRulesBridgePortExcludeVlans_Type()
)
rbRulesBridgePortExcludeVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRulesBridgePortExcludeVlans.setStatus("current")
_RbRulesBridgePortOutOfBand_Type = TruthValue
_RbRulesBridgePortOutOfBand_Object = MibTableColumn
rbRulesBridgePortOutOfBand = _RbRulesBridgePortOutOfBand_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 1, 1, 6),
    _RbRulesBridgePortOutOfBand_Type()
)
rbRulesBridgePortOutOfBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRulesBridgePortOutOfBand.setStatus("current")
_RbRulesBridgeRuleTable_Object = MibTable
rbRulesBridgeRuleTable = _RbRulesBridgeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2)
)
if mibBuilder.loadTexts:
    rbRulesBridgeRuleTable.setStatus("current")
_RbRulesBridgeRuleEntry_Object = MibTableRow
rbRulesBridgeRuleEntry = _RbRulesBridgeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1)
)
rbRulesBridgeRuleEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbRulesBridgePortId"),
    (0, "RADIO-BRIDGE-MIB", "rbRulesBridgeRuleId"),
)
if mibBuilder.loadTexts:
    rbRulesBridgeRuleEntry.setStatus("current")
_RbRulesBridgeRulePortId_Type = Integer32
_RbRulesBridgeRulePortId_Object = MibTableColumn
rbRulesBridgeRulePortId = _RbRulesBridgeRulePortId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1, 1),
    _RbRulesBridgeRulePortId_Type()
)
rbRulesBridgeRulePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRulesBridgeRulePortId.setStatus("current")
_RbRulesBridgeRuleId_Type = Integer32
_RbRulesBridgeRuleId_Object = MibTableColumn
rbRulesBridgeRuleId = _RbRulesBridgeRuleId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1, 2),
    _RbRulesBridgeRuleId_Type()
)
rbRulesBridgeRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRulesBridgeRuleId.setStatus("current")
_RbRulesBridgeRuleRowStatus_Type = RowStatus
_RbRulesBridgeRuleRowStatus_Object = MibTableColumn
rbRulesBridgeRuleRowStatus = _RbRulesBridgeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1, 3),
    _RbRulesBridgeRuleRowStatus_Type()
)
rbRulesBridgeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRulesBridgeRuleRowStatus.setStatus("current")
_RbRulesBridgeRuleClassifyVlans_Type = RulesVlansList
_RbRulesBridgeRuleClassifyVlans_Object = MibTableColumn
rbRulesBridgeRuleClassifyVlans = _RbRulesBridgeRuleClassifyVlans_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1, 4),
    _RbRulesBridgeRuleClassifyVlans_Type()
)
rbRulesBridgeRuleClassifyVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRulesBridgeRuleClassifyVlans.setStatus("current")


class _RbRulesBridgeRuleType_Type(Integer32):
    """Custom type rbRulesBridgeRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("translate", 2))
    )


_RbRulesBridgeRuleType_Type.__name__ = "Integer32"
_RbRulesBridgeRuleType_Object = MibTableColumn
rbRulesBridgeRuleType = _RbRulesBridgeRuleType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1, 5),
    _RbRulesBridgeRuleType_Type()
)
rbRulesBridgeRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRulesBridgeRuleType.setStatus("current")
_RbRulesBridgeRuleEgressVlan_Type = Integer32
_RbRulesBridgeRuleEgressVlan_Object = MibTableColumn
rbRulesBridgeRuleEgressVlan = _RbRulesBridgeRuleEgressVlan_Object(
    (1, 3, 6, 1, 4, 1, 31926, 31, 2, 1, 6),
    _RbRulesBridgeRuleEgressVlan_Type()
)
rbRulesBridgeRuleEgressVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRulesBridgeRuleEgressVlan.setStatus("current")
_RadioBridgeSfp_ObjectIdentity = ObjectIdentity
radioBridgeSfp = _RadioBridgeSfp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 32)
)
_RbSfpDdmTable_Object = MibTable
rbSfpDdmTable = _RbSfpDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1)
)
if mibBuilder.loadTexts:
    rbSfpDdmTable.setStatus("current")
_RbSfpDdmEntry_Object = MibTableRow
rbSfpDdmEntry = _RbSfpDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1)
)
rbSfpDdmEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbSfpIndex"),
)
if mibBuilder.loadTexts:
    rbSfpDdmEntry.setStatus("current")
_RbSfpIndex_Type = Unsigned32
_RbSfpIndex_Object = MibTableColumn
rbSfpIndex = _RbSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1, 1),
    _RbSfpIndex_Type()
)
rbSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSfpIndex.setStatus("current")
_RbSfpTemperature_Type = Integer32
_RbSfpTemperature_Object = MibTableColumn
rbSfpTemperature = _RbSfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1, 2),
    _RbSfpTemperature_Type()
)
rbSfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSfpTemperature.setStatus("current")
_RbSfpVcc_Type = Unsigned32
_RbSfpVcc_Object = MibTableColumn
rbSfpVcc = _RbSfpVcc_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1, 3),
    _RbSfpVcc_Type()
)
rbSfpVcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSfpVcc.setStatus("current")
_RbSfpTxBias_Type = Unsigned32
_RbSfpTxBias_Object = MibTableColumn
rbSfpTxBias = _RbSfpTxBias_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1, 4),
    _RbSfpTxBias_Type()
)
rbSfpTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSfpTxBias.setStatus("current")
_RbSfpTxPower_Type = Unsigned32
_RbSfpTxPower_Object = MibTableColumn
rbSfpTxPower = _RbSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1, 5),
    _RbSfpTxPower_Type()
)
rbSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSfpTxPower.setStatus("current")
_RbSfpRxPower_Type = Unsigned32
_RbSfpRxPower_Object = MibTableColumn
rbSfpRxPower = _RbSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 31926, 32, 1, 1, 6),
    _RbSfpRxPower_Type()
)
rbSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSfpRxPower.setStatus("current")
_RadioBridgeIeee1588_ObjectIdentity = ObjectIdentity
radioBridgeIeee1588 = _RadioBridgeIeee1588_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 33)
)


class _RbIeee1588Admin_Type(Integer32):
    """Custom type rbIeee1588Admin based on Integer32"""
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


_RbIeee1588Admin_Type.__name__ = "Integer32"
_RbIeee1588Admin_Object = MibScalar
rbIeee1588Admin = _RbIeee1588Admin_Object(
    (1, 3, 6, 1, 4, 1, 31926, 33, 1),
    _RbIeee1588Admin_Type()
)
rbIeee1588Admin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbIeee1588Admin.setStatus("current")


class _RbIeee1588Operational_Type(Integer32):
    """Custom type rbIeee1588Operational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_RbIeee1588Operational_Type.__name__ = "Integer32"
_RbIeee1588Operational_Object = MibScalar
rbIeee1588Operational = _RbIeee1588Operational_Object(
    (1, 3, 6, 1, 4, 1, 31926, 33, 2),
    _RbIeee1588Operational_Type()
)
rbIeee1588Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbIeee1588Operational.setStatus("current")
_RadioBridgeExtendMm_ObjectIdentity = ObjectIdentity
radioBridgeExtendMm = _RadioBridgeExtendMm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 34)
)


class _RbExtendMmAdminStatus_Type(Integer32):
    """Custom type rbExtendMmAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RbExtendMmAdminStatus_Type.__name__ = "Integer32"
_RbExtendMmAdminStatus_Object = MibScalar
rbExtendMmAdminStatus = _RbExtendMmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 34, 1),
    _RbExtendMmAdminStatus_Type()
)
rbExtendMmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbExtendMmAdminStatus.setStatus("current")
_RbExtendMmMainPathOperStatus_Type = ExtendMmPathOperStatus
_RbExtendMmMainPathOperStatus_Object = MibScalar
rbExtendMmMainPathOperStatus = _RbExtendMmMainPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 34, 2),
    _RbExtendMmMainPathOperStatus_Type()
)
rbExtendMmMainPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbExtendMmMainPathOperStatus.setStatus("current")
_RbExtendMmBackupPathOperStatus_Type = ExtendMmPathOperStatus
_RbExtendMmBackupPathOperStatus_Object = MibScalar
rbExtendMmBackupPathOperStatus = _RbExtendMmBackupPathOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 34, 3),
    _RbExtendMmBackupPathOperStatus_Type()
)
rbExtendMmBackupPathOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbExtendMmBackupPathOperStatus.setStatus("current")


class _RbExtendMmRole_Type(Integer32):
    """Custom type rbExtendMmRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slave", 1),
          ("master", 2))
    )


_RbExtendMmRole_Type.__name__ = "Integer32"
_RbExtendMmRole_Object = MibScalar
rbExtendMmRole = _RbExtendMmRole_Object(
    (1, 3, 6, 1, 4, 1, 31926, 34, 4),
    _RbExtendMmRole_Type()
)
rbExtendMmRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbExtendMmRole.setStatus("current")


class _RbExtendMmPortNum_Type(Integer32):
    """Custom type rbExtendMmPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eth1", 2),
          ("eth2", 3),
          ("eth3", 4))
    )


_RbExtendMmPortNum_Type.__name__ = "Integer32"
_RbExtendMmPortNum_Object = MibScalar
rbExtendMmPortNum = _RbExtendMmPortNum_Object(
    (1, 3, 6, 1, 4, 1, 31926, 34, 5),
    _RbExtendMmPortNum_Type()
)
rbExtendMmPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbExtendMmPortNum.setStatus("current")


class _RbExtendMmSwitchMode_Type(Integer32):
    """Custom type rbExtendMmSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("main", 1),
          ("backup", 2))
    )


_RbExtendMmSwitchMode_Type.__name__ = "Integer32"
_RbExtendMmSwitchMode_Object = MibScalar
rbExtendMmSwitchMode = _RbExtendMmSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 34, 6),
    _RbExtendMmSwitchMode_Type()
)
rbExtendMmSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbExtendMmSwitchMode.setStatus("current")
dot1agCfmMepEntry.registerAugmentions(
    ("RADIO-BRIDGE-MIB",
     "rbMepEntry")
)
rbMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
ieee8021QBridgeTpFdbEntry.registerAugmentions(
    ("RADIO-BRIDGE-MIB",
     "rbFdbExtensionEntry")
)
rbFdbExtensionEntry.setIndexNames(*ieee8021QBridgeTpFdbEntry.getIndexNames())

# Managed Objects groups


# Notification objects

trapModulationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 1)
)
trapModulationChange.setObjects(
      *(("RADIO-BRIDGE-MIB", "rfModulationType"),
        ("RADIO-BRIDGE-MIB", "rfNumOfSubchannels"),
        ("RADIO-BRIDGE-MIB", "rfNumOfRepetitions"),
        ("RADIO-BRIDGE-MIB", "rfFecRate"))
)
if mibBuilder.loadTexts:
    trapModulationChange.setStatus(
        "current"
    )

trapTemperatureOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 2)
)
if mibBuilder.loadTexts:
    trapTemperatureOutOfRange.setStatus(
        "current"
    )

trapTemperatureInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 3)
)
if mibBuilder.loadTexts:
    trapTemperatureInRange.setStatus(
        "current"
    )

trapSfpIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 4)
)
trapSfpIn.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapSfpIn.setStatus(
        "current"
    )

trapSfpOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 5)
)
trapSfpOut.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapSfpOut.setStatus(
        "current"
    )

trapRefClockChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 6)
)
trapRefClockChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RADIO-BRIDGE-MIB", "refClockQualityLevelActual"))
)
if mibBuilder.loadTexts:
    trapRefClockChanged.setStatus(
        "current"
    )

trapCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 11)
)
trapCurrentAlarm.setObjects(
      *(("RADIO-BRIDGE-MIB", "rbCurrentAlarmChangeCounter"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmMostSevere"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmType"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmTypeName"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmSourceAddr"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmSource"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmSeverity"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmRaisedTime"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmIfIndex"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmLastTrapType"))
)
if mibBuilder.loadTexts:
    trapCurrentAlarm.setStatus(
        "current"
    )

trapLoopEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 12)
)
trapLoopEnabled.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapLoopEnabled.setStatus(
        "current"
    )

trapLoopDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 13)
)
trapLoopDisabled.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapLoopDisabled.setStatus(
        "current"
    )

trapTxMuteEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 14)
)
if mibBuilder.loadTexts:
    trapTxMuteEnabled.setStatus(
        "current"
    )

trapTxMuteDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 15)
)
if mibBuilder.loadTexts:
    trapTxMuteDisabled.setStatus(
        "current"
    )

trapCinrOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 19)
)
if mibBuilder.loadTexts:
    trapCinrOutOfRange.setStatus(
        "current"
    )

trapCinrInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 20)
)
if mibBuilder.loadTexts:
    trapCinrInRange.setStatus(
        "current"
    )

trapRssiOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 21)
)
if mibBuilder.loadTexts:
    trapRssiOutOfRange.setStatus(
        "current"
    )

trapRssiInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 22)
)
if mibBuilder.loadTexts:
    trapRssiInRange.setStatus(
        "current"
    )

trapLowestModulation = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 23)
)
if mibBuilder.loadTexts:
    trapLowestModulation.setStatus(
        "current"
    )

trapNoLowestModulation = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 24)
)
if mibBuilder.loadTexts:
    trapNoLowestModulation.setStatus(
        "current"
    )

trapAdjustedDateTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 25)
)
trapAdjustedDateTime.setObjects(
    ("RADIO-BRIDGE-MIB", "rbSystemAdjustedDateTime")
)
if mibBuilder.loadTexts:
    trapAdjustedDateTime.setStatus(
        "current"
    )

trapHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 32)
)
trapHeartBeat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("RADIO-BRIDGE-MIB", "rbSystemEquipmentModel"),
        ("RADIO-BRIDGE-MIB", "rbSystemEquipmentSourceId"),
        ("RADIO-BRIDGE-MIB", "rbSystemConfigChange"),
        ("RADIO-BRIDGE-MIB", "rbSystemNumOfAlarms"),
        ("RADIO-BRIDGE-MIB", "rbSystemIpv4List"),
        ("RADIO-BRIDGE-MIB", "rbSystemIpv6List"))
)
if mibBuilder.loadTexts:
    trapHeartBeat.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIO-BRIDGE-MIB",
    **{"ModulationName": ModulationName,
       "ExtendMmPathOperStatus": ExtendMmPathOperStatus,
       "AlarmSeverity": AlarmSeverity,
       "AlarmType": AlarmType,
       "MhBridgePort": MhBridgePort,
       "MhBridgePortsList": MhBridgePortsList,
       "RulesVlansList": RulesVlansList,
       "radioBridgeRoot": radioBridgeRoot,
       "radioBridgeSystem": radioBridgeSystem,
       "rbSysVoltage": rbSysVoltage,
       "rbSysTemperature": rbSysTemperature,
       "rbSysSaveConfiguration": rbSysSaveConfiguration,
       "rbSysReset": rbSysReset,
       "rbSwBank1Version": rbSwBank1Version,
       "rbSwBank2Version": rbSwBank2Version,
       "rbSwBank1Running": rbSwBank1Running,
       "rbSwBank2Running": rbSwBank2Running,
       "rbSwBank1ScheduledToRunNextReset": rbSwBank1ScheduledToRunNextReset,
       "rbSwBank2ScheduledToRunNextReset": rbSwBank2ScheduledToRunNextReset,
       "rbSystemUpAbsoluteTime": rbSystemUpAbsoluteTime,
       "rbSystemAuthenticationMode": rbSystemAuthenticationMode,
       "rbSystemAuthenticationSecret": rbSystemAuthenticationSecret,
       "rbSystemCapabilities": rbSystemCapabilities,
       "rbDate": rbDate,
       "rbTime": rbTime,
       "rbSystemBridgeMode": rbSystemBridgeMode,
       "rbSystemEthIsolation": rbSystemEthIsolation,
       "rbSystemTuIsolation": rbSystemTuIsolation,
       "rbSystemAdjustedDateTime": rbSystemAdjustedDateTime,
       "rbSystemEquipmentModel": rbSystemEquipmentModel,
       "rbSystemEquipmentSourceId": rbSystemEquipmentSourceId,
       "rbSystemConfigChange": rbSystemConfigChange,
       "rbSystemNumOfAlarms": rbSystemNumOfAlarms,
       "rbSystemHeartbeatPeriod": rbSystemHeartbeatPeriod,
       "rbSystemIpv4List": rbSystemIpv4List,
       "rbSystemIpv6List": rbSystemIpv6List,
       "rbSystemHostname": rbSystemHostname,
       "radioBridgeRf": radioBridgeRf,
       "rbRfTable": rbRfTable,
       "rbRfEntry": rbRfEntry,
       "rfIndex": rfIndex,
       "rfNumOfChannels": rfNumOfChannels,
       "rfChannelWidth": rfChannelWidth,
       "rfOperationalFrequency": rfOperationalFrequency,
       "rfRole": rfRole,
       "rfModeSelector": rfModeSelector,
       "rfModulationType": rfModulationType,
       "rfNumOfSubchannels": rfNumOfSubchannels,
       "rfNumOfRepetitions": rfNumOfRepetitions,
       "rfFecRate": rfFecRate,
       "rfOperationalState": rfOperationalState,
       "rfAverageCinr": rfAverageCinr,
       "rfAverageRssi": rfAverageRssi,
       "rfTxSynthLock": rfTxSynthLock,
       "rfRxSynthLock": rfRxSynthLock,
       "rfRxLinkId": rfRxLinkId,
       "rfTxLinkId": rfTxLinkId,
       "rfTxState": rfTxState,
       "rfRxState": rfRxState,
       "rfTemperature": rfTemperature,
       "rfAsymmetry": rfAsymmetry,
       "rfLowestModulationType": rfLowestModulationType,
       "rfLowestNumOfSubchannels": rfLowestNumOfSubchannels,
       "rfLowestNumOfRepetitions": rfLowestNumOfRepetitions,
       "rfLowestFecRate": rfLowestFecRate,
       "rfTxMute": rfTxMute,
       "rfRoleStatus": rfRoleStatus,
       "rfLoopModeSelector": rfLoopModeSelector,
       "rfLoopModulationType": rfLoopModulationType,
       "rfLoopNumOfSubchannels": rfLoopNumOfSubchannels,
       "rfLoopNumOfRepetitions": rfLoopNumOfRepetitions,
       "rfLoopFecRate": rfLoopFecRate,
       "rfLoopTimeout": rfLoopTimeout,
       "rfTxPower": rfTxPower,
       "rfTxMuteTimeout": rfTxMuteTimeout,
       "rfAlignmentStatus": rfAlignmentStatus,
       "rfLoopDirection": rfLoopDirection,
       "rfModulationName": rfModulationName,
       "rfLowestModulationName": rfLowestModulationName,
       "rfLoopModulationName": rfLoopModulationName,
       "rfAverageCinrFractional": rfAverageCinrFractional,
       "rfAirCapacity": rfAirCapacity,
       "rfRxFrequency": rfRxFrequency,
       "rbRfStatisticsTable": rbRfStatisticsTable,
       "rbRfStatisticsEntry": rbRfStatisticsEntry,
       "rfInOctets": rfInOctets,
       "rfInIdleOctets": rfInIdleOctets,
       "rfInGoodOctets": rfInGoodOctets,
       "rfInErroredOctets": rfInErroredOctets,
       "rfOutOctets": rfOutOctets,
       "rfOutIdleOctets": rfOutIdleOctets,
       "rfInPkts": rfInPkts,
       "rfInGoodPkts": rfInGoodPkts,
       "rfInErroredPkts": rfInErroredPkts,
       "rfInLostPkts": rfInLostPkts,
       "rfOutPkts": rfOutPkts,
       "rfMinCinr": rfMinCinr,
       "rfMaxCinr": rfMaxCinr,
       "rfMinRssi": rfMinRssi,
       "rfMaxRssi": rfMaxRssi,
       "rfMinModulation": rfMinModulation,
       "rfMaxModulation": rfMaxModulation,
       "rfValid": rfValid,
       "rfArqInLoss": rfArqInLoss,
       "rfArqOutLoss": rfArqOutLoss,
       "rfMinModulationName": rfMinModulationName,
       "rfMaxModulationName": rfMaxModulationName,
       "rfMinCinrFractional": rfMinCinrFractional,
       "rfMaxCinrFractional": rfMaxCinrFractional,
       "rfUptime": rfUptime,
       "rbRfStatisticsDaysTable": rbRfStatisticsDaysTable,
       "rbRfStatisticsDaysEntry": rbRfStatisticsDaysEntry,
       "rfDaysInOctets": rfDaysInOctets,
       "rfDaysInIdleOctets": rfDaysInIdleOctets,
       "rfDaysInGoodOctets": rfDaysInGoodOctets,
       "rfDaysInErroredOctets": rfDaysInErroredOctets,
       "rfDaysOutOctets": rfDaysOutOctets,
       "rfDaysOutIdleOctets": rfDaysOutIdleOctets,
       "rfDaysInPkts": rfDaysInPkts,
       "rfDaysInGoodPkts": rfDaysInGoodPkts,
       "rfDaysInErroredPkts": rfDaysInErroredPkts,
       "rfDaysInLostPkts": rfDaysInLostPkts,
       "rfDaysOutPkts": rfDaysOutPkts,
       "rfDaysMinCinr": rfDaysMinCinr,
       "rfDaysMaxCinr": rfDaysMaxCinr,
       "rfDaysMinRssi": rfDaysMinRssi,
       "rfDaysMaxRssi": rfDaysMaxRssi,
       "rfDaysMinModulation": rfDaysMinModulation,
       "rfDaysMaxModulation": rfDaysMaxModulation,
       "rfDaysValid": rfDaysValid,
       "rfDaysArqInLoss": rfDaysArqInLoss,
       "rfDaysArqOutLoss": rfDaysArqOutLoss,
       "rfDaysMinModulationName": rfDaysMinModulationName,
       "rfDaysMaxModulationName": rfDaysMaxModulationName,
       "rfDaysMinCinrFractional": rfDaysMinCinrFractional,
       "rfDaysMaxCinrFractional": rfDaysMaxCinrFractional,
       "rfDayIndex": rfDayIndex,
       "rfDaysStart": rfDaysStart,
       "radioBridgeTraps": radioBridgeTraps,
       "trapModulationChange": trapModulationChange,
       "trapTemperatureOutOfRange": trapTemperatureOutOfRange,
       "trapTemperatureInRange": trapTemperatureInRange,
       "trapSfpIn": trapSfpIn,
       "trapSfpOut": trapSfpOut,
       "trapRefClockChanged": trapRefClockChanged,
       "trapCurrentAlarm": trapCurrentAlarm,
       "trapLoopEnabled": trapLoopEnabled,
       "trapLoopDisabled": trapLoopDisabled,
       "trapTxMuteEnabled": trapTxMuteEnabled,
       "trapTxMuteDisabled": trapTxMuteDisabled,
       "trapCinrOutOfRange": trapCinrOutOfRange,
       "trapCinrInRange": trapCinrInRange,
       "trapRssiOutOfRange": trapRssiOutOfRange,
       "trapRssiInRange": trapRssiInRange,
       "trapLowestModulation": trapLowestModulation,
       "trapNoLowestModulation": trapNoLowestModulation,
       "trapAdjustedDateTime": trapAdjustedDateTime,
       "trapHeartBeat": trapHeartBeat,
       "radioBridgeRefClock": radioBridgeRefClock,
       "rbRefClockTable": rbRefClockTable,
       "rbRefClockEntry": rbRefClockEntry,
       "refClockPrio": refClockPrio,
       "refClockStatus": refClockStatus,
       "refClockQualityLevelActual": refClockQualityLevelActual,
       "refClockQualityLevelConfig": refClockQualityLevelConfig,
       "refClockQualityLevelMode": refClockQualityLevelMode,
       "refClockSsmCvid": refClockSsmCvid,
       "refClockRowStatus": refClockRowStatus,
       "radioBridgeEthernet": radioBridgeEthernet,
       "rbEthernetTable": rbEthernetTable,
       "rbEthernetEntry": rbEthernetEntry,
       "ethernetAlarmPropagation": ethernetAlarmPropagation,
       "ethernetLoopMode": ethernetLoopMode,
       "ethernetLoopTimeout": ethernetLoopTimeout,
       "ethernetNetworkType": ethernetNetworkType,
       "ethernetPcpWriteProfileId": ethernetPcpWriteProfileId,
       "ethernetClassifierMode": ethernetClassifierMode,
       "ethernetAlarmPropagationRemotePort": ethernetAlarmPropagationRemotePort,
       "ethernetTxThroughput": ethernetTxThroughput,
       "ethernetRxThroughput": ethernetRxThroughput,
       "radioBridgeQosClassifier": radioBridgeQosClassifier,
       "rbClassifierCosTable": rbClassifierCosTable,
       "rbClassifierCosEntry": rbClassifierCosEntry,
       "classifierCosId": classifierCosId,
       "classifierCosPortList": classifierCosPortList,
       "classifierCosPrecedence": classifierCosPrecedence,
       "classifierCosVidList": classifierCosVidList,
       "classifierCosPcpList": classifierCosPcpList,
       "classifierCosCos": classifierCosCos,
       "classifierCosIpCosType": classifierCosIpCosType,
       "classifierCosIpCosList": classifierCosIpCosList,
       "classifierCosRowStatus": classifierCosRowStatus,
       "classifierCosPacketType": classifierCosPacketType,
       "rbClassifierEvcTable": rbClassifierEvcTable,
       "rbClassifierEvcEntry": rbClassifierEvcEntry,
       "classifierEvcId": classifierEvcId,
       "classifierEvcPortList": classifierEvcPortList,
       "classifierEvcPrecedence": classifierEvcPrecedence,
       "classifierEvcVidList": classifierEvcVidList,
       "classifierEvcPcpList": classifierEvcPcpList,
       "classifierEvcEvc": classifierEvcEvc,
       "classifierEvcIpCosType": classifierEvcIpCosType,
       "classifierEvcIpCosList": classifierEvcIpCosList,
       "classifierEvcRowStatus": classifierEvcRowStatus,
       "classifierEvcPacketType": classifierEvcPacketType,
       "radioBridgeQosIngressQueue": radioBridgeQosIngressQueue,
       "rbQosIngressQueueTable": rbQosIngressQueueTable,
       "rbQosIngressQueueEntry": rbQosIngressQueueEntry,
       "qosIngressQueueEvcId": qosIngressQueueEvcId,
       "qosIngressQueueCosId": qosIngressQueueCosId,
       "qosIngressQueueMeterId": qosIngressQueueMeterId,
       "qosIngressQueueMarking": qosIngressQueueMarking,
       "qosIngressQueueRowStatus": qosIngressQueueRowStatus,
       "radioBridgeQosEgressQueue": radioBridgeQosEgressQueue,
       "rbQosEgressQueueTable": rbQosEgressQueueTable,
       "rbQosEgressQueueEntry": rbQosEgressQueueEntry,
       "qosEgressQueuePortNum": qosEgressQueuePortNum,
       "qosEgressQueueCosId": qosEgressQueueCosId,
       "qosEgressQueueWfqWeight": qosEgressQueueWfqWeight,
       "qosEgressQueueCir": qosEgressQueueCir,
       "qosEgressQueueMode": qosEgressQueueMode,
       "qosEgressQueueColorDrop": qosEgressQueueColorDrop,
       "qosEgressDropMode": qosEgressDropMode,
       "radioBridgeIp": radioBridgeIp,
       "rbIpTable": rbIpTable,
       "rbIpEntry": rbIpEntry,
       "rbIpIndex": rbIpIndex,
       "rbIpAddress": rbIpAddress,
       "rbIpPrefixLen": rbIpPrefixLen,
       "rbIpVlanId": rbIpVlanId,
       "rbIpRowStatus": rbIpRowStatus,
       "rbIpType": rbIpType,
       "rbIpGateway": rbIpGateway,
       "radioBridgeCfm": radioBridgeCfm,
       "rbPeerMep": rbPeerMep,
       "rbPeerMepEntry": rbPeerMepEntry,
       "rbMdIndex": rbMdIndex,
       "rbMaIndex": rbMaIndex,
       "rbMepId": rbMepId,
       "rbPeerMepId": rbPeerMepId,
       "rbPeerMepFarEndLoss": rbPeerMepFarEndLoss,
       "rbPeerMepNearEndLoss": rbPeerMepNearEndLoss,
       "rbPeerMepTotalTxFarEnd": rbPeerMepTotalTxFarEnd,
       "rbPeerMepTotalTxNearEnd": rbPeerMepTotalTxNearEnd,
       "rbPeerMepFrameDelay": rbPeerMepFrameDelay,
       "rbPeerMepFrameDelayVariation": rbPeerMepFrameDelayVariation,
       "rbMep": rbMep,
       "rbMepEntry": rbMepEntry,
       "rbMepAisEnable": rbMepAisEnable,
       "rbMepAisPeriod": rbMepAisPeriod,
       "rbMepAisSuppress": rbMepAisSuppress,
       "rbMepAisLevel": rbMepAisLevel,
       "rbMepAisDefects": rbMepAisDefects,
       "radioBridgeAlarms": radioBridgeAlarms,
       "rbAlarmsCommon": rbAlarmsCommon,
       "rbCurrentAlarmChangeCounter": rbCurrentAlarmChangeCounter,
       "rbCurrentAlarmMostSevere": rbCurrentAlarmMostSevere,
       "rbCurrentAlarmLastIndex": rbCurrentAlarmLastIndex,
       "rbCurrentAlarmLastTrapType": rbCurrentAlarmLastTrapType,
       "rbCurrentAlarmSourceAddr": rbCurrentAlarmSourceAddr,
       "rbCurrentAlarmTable": rbCurrentAlarmTable,
       "rbCurrentAlarmEntry": rbCurrentAlarmEntry,
       "rbCurrentAlarmIndex": rbCurrentAlarmIndex,
       "rbCurrentAlarmType": rbCurrentAlarmType,
       "rbCurrentAlarmTypeName": rbCurrentAlarmTypeName,
       "rbCurrentAlarmSource": rbCurrentAlarmSource,
       "rbCurrentAlarmSeverity": rbCurrentAlarmSeverity,
       "rbCurrentAlarmRaisedTime": rbCurrentAlarmRaisedTime,
       "rbCurrentAlarmDesc": rbCurrentAlarmDesc,
       "rbCurrentAlarmCause": rbCurrentAlarmCause,
       "rbCurrentAlarmAction": rbCurrentAlarmAction,
       "rbCurrentAlarmIfIndex": rbCurrentAlarmIfIndex,
       "radioBridgeScheduler": radioBridgeScheduler,
       "rbSchedulerMode": rbSchedulerMode,
       "rbClassifierMode": rbClassifierMode,
       "radioBridgeEncryption": radioBridgeEncryption,
       "rbRfEncryption": rbRfEncryption,
       "rbRfStaticKey": rbRfStaticKey,
       "rbRfAuthenticationString": rbRfAuthenticationString,
       "radioBridgeMeter": radioBridgeMeter,
       "rbMeterTable": rbMeterTable,
       "rbMeterEntry": rbMeterEntry,
       "rbMeterId": rbMeterId,
       "rbMeterCir": rbMeterCir,
       "rbMeterCbs": rbMeterCbs,
       "rbMeterEir": rbMeterEir,
       "rbMeterEbs": rbMeterEbs,
       "rbMeterColorMode": rbMeterColorMode,
       "rbMeterRowStatus": rbMeterRowStatus,
       "radioBridgeEventConfig": radioBridgeEventConfig,
       "rbEventConfigTable": rbEventConfigTable,
       "rbEventConfigEntry": rbEventConfigEntry,
       "rbEventConfigIndex": rbEventConfigIndex,
       "rbEventConfigId": rbEventConfigId,
       "rbEventConfigMask": rbEventConfigMask,
       "radioBridgeSnmp": radioBridgeSnmp,
       "rbAgentReadCommunity": rbAgentReadCommunity,
       "rbAgentWriteCommunity": rbAgentWriteCommunity,
       "rbAgentSnmpVersion": rbAgentSnmpVersion,
       "rbSysFileOperationTable": rbSysFileOperationTable,
       "rbSysFileOperationEntry": rbSysFileOperationEntry,
       "fileSessionIndex": fileSessionIndex,
       "fileSessionCommand": fileSessionCommand,
       "fileSessionLocalParams": fileSessionLocalParams,
       "fileSessionRemotePath": fileSessionRemotePath,
       "fileSessionServer": fileSessionServer,
       "fileSessionUser": fileSessionUser,
       "fileSessionPassword": fileSessionPassword,
       "fileSessionResult": fileSessionResult,
       "fileSessionState": fileSessionState,
       "fileSessionRowStatus": fileSessionRowStatus,
       "fileSessionProtocol": fileSessionProtocol,
       "radioBridgeLldp": radioBridgeLldp,
       "rbLldpPortExtensionTable": rbLldpPortExtensionTable,
       "rbLldpPortExtensionEntry": rbLldpPortExtensionEntry,
       "rbLldpPortIfIndex": rbLldpPortIfIndex,
       "rbLldpPortDestAddressIndex": rbLldpPortDestAddressIndex,
       "rbLldpPortVid": rbLldpPortVid,
       "rbLldpPortAddrType": rbLldpPortAddrType,
       "rbLldpPortIpIndex": rbLldpPortIpIndex,
       "radioBridgeWred": radioBridgeWred,
       "rbWredTable": rbWredTable,
       "rbWredEntry": rbWredEntry,
       "rbWredId": rbWredId,
       "rbWredNfactor": rbWredNfactor,
       "rbWredMinThreshold": rbWredMinThreshold,
       "rbWredMaxThreshold": rbWredMaxThreshold,
       "rbWredProbability": rbWredProbability,
       "rbWredMinThresholdYellow": rbWredMinThresholdYellow,
       "rbWredMaxThresholdYellow": rbWredMaxThresholdYellow,
       "rbWredProbabilityYellow": rbWredProbabilityYellow,
       "rbWredRowStatus": rbWredRowStatus,
       "radioBridgeAuthentication": radioBridgeAuthentication,
       "rbAuthServersTable": rbAuthServersTable,
       "rbAuthServersEntry": rbAuthServersEntry,
       "rbAuthServerId": rbAuthServerId,
       "rbAuthServerIpAddress": rbAuthServerIpAddress,
       "rbAuthServerPort": rbAuthServerPort,
       "rbAuthServerRowStatus": rbAuthServerRowStatus,
       "radioBridgeQuota": radioBridgeQuota,
       "rbFdbQuotaTable": rbFdbQuotaTable,
       "rbFdbQuotaEntry": rbFdbQuotaEntry,
       "rbFdbQuotaId": rbFdbQuotaId,
       "rbFdbQuotaSize": rbFdbQuotaSize,
       "rbFdbQuotaRowStatus": rbFdbQuotaRowStatus,
       "rbFdbQuotaMaxSize": rbFdbQuotaMaxSize,
       "rbFdbQuotaUsedEntries": rbFdbQuotaUsedEntries,
       "rbFdbQuotaStaticEntries": rbFdbQuotaStaticEntries,
       "rbFdbQuotaDynamicEntries": rbFdbQuotaDynamicEntries,
       "rbFdbQuotaUnusedEntries": rbFdbQuotaUnusedEntries,
       "rbFdbEvcQuotaTable": rbFdbEvcQuotaTable,
       "rbFdbEvcQuotaEntry": rbFdbEvcQuotaEntry,
       "rbFdbEvcQuotaId": rbFdbEvcQuotaId,
       "rbRefEvcId": rbRefEvcId,
       "rbRefFdbQuotaId": rbRefFdbQuotaId,
       "rbFdbEvcQuotaRowStatus": rbFdbEvcQuotaRowStatus,
       "rbFdbExtensionTable": rbFdbExtensionTable,
       "rbFdbExtensionEntry": rbFdbExtensionEntry,
       "rbRefExtFdbQuotaId": rbRefExtFdbQuotaId,
       "radioBridgePcpProfile": radioBridgePcpProfile,
       "rbPcpWriteProfileTable": rbPcpWriteProfileTable,
       "rbPcpWriteProfileEntry": rbPcpWriteProfileEntry,
       "rbPcpWriteProfileId": rbPcpWriteProfileId,
       "rbPcpWriteProfilePcp": rbPcpWriteProfilePcp,
       "rbPcpWriteProfileRowStatus": rbPcpWriteProfileRowStatus,
       "radioBridgeSyslog": radioBridgeSyslog,
       "rbSyslogTable": rbSyslogTable,
       "rbSyslogEntry": rbSyslogEntry,
       "rbSyslogId": rbSyslogId,
       "rbSyslogServerIp": rbSyslogServerIp,
       "rbSyslogRowStatus": rbSyslogRowStatus,
       "radioBridgeNtp": radioBridgeNtp,
       "rbNtpTable": rbNtpTable,
       "rbNtpEntry": rbNtpEntry,
       "rbNtpId": rbNtpId,
       "rbNtpServerIp": rbNtpServerIp,
       "rbNtpSecondaryServerIp": rbNtpSecondaryServerIp,
       "rbNtpTmz": rbNtpTmz,
       "rbNtpRowStatus": rbNtpRowStatus,
       "radioBridgeLicense": radioBridgeLicense,
       "rbLicenseTable": rbLicenseTable,
       "rbLicenseEntry": rbLicenseEntry,
       "rbLicenseId": rbLicenseId,
       "rbLicenseCurrentValue": rbLicenseCurrentValue,
       "rbLicenseMaxValue": rbLicenseMaxValue,
       "radioBridgeMultiHaulRadio": radioBridgeMultiHaulRadio,
       "rbMhBaseUnitTable": rbMhBaseUnitTable,
       "rbMhBaseUnitEntry": rbMhBaseUnitEntry,
       "buNumber": buNumber,
       "buSelfMac": buSelfMac,
       "buSSID": buSSID,
       "buUserPassword": buUserPassword,
       "buFrequency": buFrequency,
       "buSsidVisible": buSsidVisible,
       "buGuestConnection": buGuestConnection,
       "buMaxTerminalUnits": buMaxTerminalUnits,
       "buTxThroughput": buTxThroughput,
       "buRxThroughput": buRxThroughput,
       "buReset": buReset,
       "buAccessControl": buAccessControl,
       "buRxOctets": buRxOctets,
       "buTxOctets": buTxOctets,
       "buRxPackets": buRxPackets,
       "buTxPackets": buTxPackets,
       "buRxDiscards": buRxDiscards,
       "buTxDiscards": buTxDiscards,
       "buRxErrors": buRxErrors,
       "buTxErrors": buTxErrors,
       "rbMhTerminalUnitTable": rbMhTerminalUnitTable,
       "rbMhTerminalUnitEntry": rbMhTerminalUnitEntry,
       "tuNumber": tuNumber,
       "tuSelfMac": tuSelfMac,
       "tuSSID": tuSSID,
       "tuUserPassword": tuUserPassword,
       "tuFrequency": tuFrequency,
       "tuTxThroughput": tuTxThroughput,
       "tuRxThroughput": tuRxThroughput,
       "tuScanMode": tuScanMode,
       "tuStatus": tuStatus,
       "tuBuMac": tuBuMac,
       "tuTxMcs": tuTxMcs,
       "tuSignalQuality": tuSignalQuality,
       "tuTxRateLimiter": tuTxRateLimiter,
       "tuBuScan": tuBuScan,
       "tuReset": tuReset,
       "tuConnectTime": tuConnectTime,
       "tuRssi": tuRssi,
       "tuTxPackets": tuTxPackets,
       "tuRxPackets": tuRxPackets,
       "tuTxBytes": tuTxBytes,
       "tuRxBytes": tuRxBytes,
       "tuTxErrors": tuTxErrors,
       "tuRxDropped": tuRxDropped,
       "rbMhTerminalUnitMcsTable": rbMhTerminalUnitMcsTable,
       "rbMhTerminalUnitMcsEntry": rbMhTerminalUnitMcsEntry,
       "mcsIndex": mcsIndex,
       "tuRxMcs": tuRxMcs,
       "rbMhRemTerminalUnitTable": rbMhRemTerminalUnitTable,
       "rbMhRemTerminalUnitEntry": rbMhRemTerminalUnitEntry,
       "remTuNumber": remTuNumber,
       "remTuPort": remTuPort,
       "remTuMac": remTuMac,
       "remTuName": remTuName,
       "remTuStatus": remTuStatus,
       "remTuAssociation": remTuAssociation,
       "remTuTxMcs": remTuTxMcs,
       "remTuSignalQuality": remTuSignalQuality,
       "remTuTxRateLimiter": remTuTxRateLimiter,
       "remTuRowStatus": remTuRowStatus,
       "remTuConnectTime": remTuConnectTime,
       "remTuRssi": remTuRssi,
       "remTuTxSector": remTuTxSector,
       "remTuRemTxSector": remTuRemTxSector,
       "remTuTxPackets": remTuTxPackets,
       "remTuRxPackets": remTuRxPackets,
       "remTuTxBytes": remTuTxBytes,
       "remTuRxBytes": remTuRxBytes,
       "remTuTxErrors": remTuTxErrors,
       "remTuRxDropped": remTuRxDropped,
       "rbMhRemTerminalUnitMcsTable": rbMhRemTerminalUnitMcsTable,
       "rbMhRemTerminalUnitMcsEntry": rbMhRemTerminalUnitMcsEntry,
       "remTuRxMcs": remTuRxMcs,
       "radioBridgeMultiHaulNetwork": radioBridgeMultiHaulNetwork,
       "rbMhBridgeTable": rbMhBridgeTable,
       "rbMhBridgeEntry": rbMhBridgeEntry,
       "mhBridgeId": mhBridgeId,
       "mhBridgeName": mhBridgeName,
       "mhBridgePorts": mhBridgePorts,
       "mhBridgePortsCli": mhBridgePortsCli,
       "mhBridgeRowStatus": mhBridgeRowStatus,
       "rbMhBridgePortTable": rbMhBridgePortTable,
       "rbMhBridgePortEntry": rbMhBridgePortEntry,
       "mhBridgePortId": mhBridgePortId,
       "mhBridgePortEthType": mhBridgePortEthType,
       "mhBridgePortOwner": mhBridgePortOwner,
       "mhBridgePortCliName": mhBridgePortCliName,
       "mhBridgePortInOctets": mhBridgePortInOctets,
       "mhBridgePortInPackets": mhBridgePortInPackets,
       "mhBridgePortInMcastPackets": mhBridgePortInMcastPackets,
       "mhBridgePortInErrorPackets": mhBridgePortInErrorPackets,
       "mhBridgePortInDiscardPackets": mhBridgePortInDiscardPackets,
       "mhBridgePortOutOctets": mhBridgePortOutOctets,
       "mhBridgePortOutPackets": mhBridgePortOutPackets,
       "mhBridgePortOutErrorPackets": mhBridgePortOutErrorPackets,
       "mhBridgePortOutDiscardPackets": mhBridgePortOutDiscardPackets,
       "rbMhFdbTable": rbMhFdbTable,
       "rbMhFdbEntry": rbMhFdbEntry,
       "mhFdbBridgeId": mhFdbBridgeId,
       "mhFdbAddress": mhFdbAddress,
       "mhFdbPortId": mhFdbPortId,
       "mhFdbStatus": mhFdbStatus,
       "radioBridge8021x": radioBridge8021x,
       "rb8021xCommonTable": rb8021xCommonTable,
       "rb8021xCommonEntry": rb8021xCommonEntry,
       "rb8021xCommonNumber": rb8021xCommonNumber,
       "rb8021xCommonNasId": rb8021xCommonNasId,
       "rb8021xCommonNasIpIndex": rb8021xCommonNasIpIndex,
       "rb8021xCommonReauthPeriod": rb8021xCommonReauthPeriod,
       "rb8021xServerTable": rb8021xServerTable,
       "rb8021xServerEntry": rb8021xServerEntry,
       "rb8021xServerId": rb8021xServerId,
       "rb8021xServerIpAddr": rb8021xServerIpAddr,
       "rb8021xServerPort": rb8021xServerPort,
       "rb8021xServerSharedSecret": rb8021xServerSharedSecret,
       "rb8021xTable": rb8021xTable,
       "rb8021xEntry": rb8021xEntry,
       "rb8021xEthNum": rb8021xEthNum,
       "rb8021xAdmin": rb8021xAdmin,
       "rb8021xStatus": rb8021xStatus,
       "radioBridgeTuConfig": radioBridgeTuConfig,
       "rbTuConfigTable": rbTuConfigTable,
       "rbTuConfigEntry": rbTuConfigEntry,
       "tuConfigSnmpIndex": tuConfigSnmpIndex,
       "tuConfigTuId": tuConfigTuId,
       "tuConfigString": tuConfigString,
       "tuConfigStatus": tuConfigStatus,
       "tuConfigRowStatus": tuConfigRowStatus,
       "radioBridgeRules": radioBridgeRules,
       "rbRulesBridgePortTable": rbRulesBridgePortTable,
       "rbRulesBridgePortEntry": rbRulesBridgePortEntry,
       "rbRulesBridgePortId": rbRulesBridgePortId,
       "rbRulesBridgePortType": rbRulesBridgePortType,
       "rbRulesBridgePortMemberVlans": rbRulesBridgePortMemberVlans,
       "rbRulesBridgePortPvid": rbRulesBridgePortPvid,
       "rbRulesBridgePortExcludeVlans": rbRulesBridgePortExcludeVlans,
       "rbRulesBridgePortOutOfBand": rbRulesBridgePortOutOfBand,
       "rbRulesBridgeRuleTable": rbRulesBridgeRuleTable,
       "rbRulesBridgeRuleEntry": rbRulesBridgeRuleEntry,
       "rbRulesBridgeRulePortId": rbRulesBridgeRulePortId,
       "rbRulesBridgeRuleId": rbRulesBridgeRuleId,
       "rbRulesBridgeRuleRowStatus": rbRulesBridgeRuleRowStatus,
       "rbRulesBridgeRuleClassifyVlans": rbRulesBridgeRuleClassifyVlans,
       "rbRulesBridgeRuleType": rbRulesBridgeRuleType,
       "rbRulesBridgeRuleEgressVlan": rbRulesBridgeRuleEgressVlan,
       "radioBridgeSfp": radioBridgeSfp,
       "rbSfpDdmTable": rbSfpDdmTable,
       "rbSfpDdmEntry": rbSfpDdmEntry,
       "rbSfpIndex": rbSfpIndex,
       "rbSfpTemperature": rbSfpTemperature,
       "rbSfpVcc": rbSfpVcc,
       "rbSfpTxBias": rbSfpTxBias,
       "rbSfpTxPower": rbSfpTxPower,
       "rbSfpRxPower": rbSfpRxPower,
       "radioBridgeIeee1588": radioBridgeIeee1588,
       "rbIeee1588Admin": rbIeee1588Admin,
       "rbIeee1588Operational": rbIeee1588Operational,
       "radioBridgeExtendMm": radioBridgeExtendMm,
       "rbExtendMmAdminStatus": rbExtendMmAdminStatus,
       "rbExtendMmMainPathOperStatus": rbExtendMmMainPathOperStatus,
       "rbExtendMmBackupPathOperStatus": rbExtendMmBackupPathOperStatus,
       "rbExtendMmRole": rbExtendMmRole,
       "rbExtendMmPortNum": rbExtendMmPortNum,
       "rbExtendMmSwitchMode": rbExtendMmSwitchMode}
)
