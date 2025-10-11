# SNMP MIB module (MOXA-EDS508-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/moxa/MOXA-EDS508-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:13 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

etherDeviceSwitch = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1)
)
if mibBuilder.loadTexts:
    etherDeviceSwitch.setRevisions(
        ("2005-03-23 00:00",
         "2005-03-22 00:00",
         "2005-03-17 00:00",
         "2004-12-08 00:00",
         "2004-08-31 00:00",
         "2004-07-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )



# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_IndustrialEthernet_ObjectIdentity = ObjectIdentity
industrialEthernet = _IndustrialEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7)
)
_PortsNumber_Type = Integer32
_PortsNumber_Object = MibScalar
portsNumber = _PortsNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 1),
    _PortsNumber_Type()
)
portsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsNumber.setStatus("current")
_SwitchModel_Type = DisplayString
_SwitchModel_Object = MibScalar
switchModel = _SwitchModel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 2),
    _SwitchModel_Type()
)
switchModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchModel.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _EnableWebConfig_Type(Integer32):
    """Custom type enableWebConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableWebConfig_Type.__name__ = "Integer32"
_EnableWebConfig_Object = MibScalar
enableWebConfig = _EnableWebConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 5),
    _EnableWebConfig_Type()
)
enableWebConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableWebConfig.setStatus("current")


class _EnableTelnetConsole_Type(Integer32):
    """Custom type enableTelnetConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableTelnetConsole_Type.__name__ = "Integer32"
_EnableTelnetConsole_Object = MibScalar
enableTelnetConsole = _EnableTelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 6),
    _EnableTelnetConsole_Type()
)
enableTelnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTelnetConsole.setStatus("current")


class _LineSwapRecovery_Type(Integer32):
    """Custom type lineSwapRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LineSwapRecovery_Type.__name__ = "Integer32"
_LineSwapRecovery_Object = MibScalar
lineSwapRecovery = _LineSwapRecovery_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 7),
    _LineSwapRecovery_Type()
)
lineSwapRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSwapRecovery.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8)
)
_SwitchIpAddr_Type = IpAddress
_SwitchIpAddr_Object = MibScalar
switchIpAddr = _SwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 1),
    _SwitchIpAddr_Type()
)
switchIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIpAddr.setStatus("current")
_SwitchIpMask_Type = IpAddress
_SwitchIpMask_Object = MibScalar
switchIpMask = _SwitchIpMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 2),
    _SwitchIpMask_Type()
)
switchIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIpMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _EnableAutoIpConfig_Type(Integer32):
    """Custom type enableAutoIpConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableDHCP", 1),
          ("enableBOOTP", 2))
    )


_EnableAutoIpConfig_Type.__name__ = "Integer32"
_EnableAutoIpConfig_Object = MibScalar
enableAutoIpConfig = _EnableAutoIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 4),
    _EnableAutoIpConfig_Type()
)
enableAutoIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAutoIpConfig.setStatus("current")
_DnsServer1IpAddr_Type = IpAddress
_DnsServer1IpAddr_Object = MibScalar
dnsServer1IpAddr = _DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 5),
    _DnsServer1IpAddr_Type()
)
dnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1IpAddr.setStatus("current")
_SnmpCommunityName_Type = DisplayString
_SnmpCommunityName_Object = MibScalar
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 6),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")
_TrapServerAddr_Type = DisplayString
_TrapServerAddr_Object = MibScalar
trapServerAddr = _TrapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 7),
    _TrapServerAddr_Type()
)
trapServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerAddr.setStatus("current")
_DnsServer2IpAddr_Type = IpAddress
_DnsServer2IpAddr_Object = MibScalar
dnsServer2IpAddr = _DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 8, 8),
    _DnsServer2IpAddr_Type()
)
dnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2IpAddr.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1)
)
portEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortEnable_Type(Integer32):
    """Custom type portEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortEnable_Type.__name__ = "Integer32"
_PortEnable_Object = MibTableColumn
portEnable = _PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 2),
    _PortEnable_Type()
)
portEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnable.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
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
        *(("auto", 0),
          ("speed100M-Full", 1),
          ("speed100M-Half", 2),
          ("speed10M-Full", 3),
          ("speed10M-Half", 4))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 3),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")


class _PortMDI_Type(Integer32):
    """Custom type portMDI based on Integer32"""
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
        *(("auto", 0),
          ("mdiX", 1),
          ("mdi", 2),
          ("no", 3))
    )


_PortMDI_Type.__name__ = "Integer32"
_PortMDI_Object = MibTableColumn
portMDI = _PortMDI_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 4),
    _PortMDI_Type()
)
portMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMDI.setStatus("current")


class _PortFDXFlowCtrl_Type(Integer32):
    """Custom type portFDXFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortFDXFlowCtrl_Type.__name__ = "Integer32"
_PortFDXFlowCtrl_Object = MibTableColumn
portFDXFlowCtrl = _PortFDXFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 5),
    _PortFDXFlowCtrl_Type()
)
portFDXFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFDXFlowCtrl.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 6),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortTrunkingGroup_Type(Integer32):
    """Custom type portTrunkingGroup based on Integer32"""
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
        *(("none", 0),
          ("trunkingGroup1", 1),
          ("trunkingGroup2", 2),
          ("trunkingGroup3", 3),
          ("trunkingGroup4", 4))
    )


_PortTrunkingGroup_Type.__name__ = "Integer32"
_PortTrunkingGroup_Object = MibTableColumn
portTrunkingGroup = _PortTrunkingGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 9, 1, 1, 7),
    _PortTrunkingGroup_Type()
)
portTrunkingGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkingGroup.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10)
)


class _Power1InputStatus_Type(Integer32):
    """Custom type power1InputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_Power1InputStatus_Type.__name__ = "Integer32"
_Power1InputStatus_Object = MibScalar
power1InputStatus = _Power1InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 1),
    _Power1InputStatus_Type()
)
power1InputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power1InputStatus.setStatus("current")


class _Power2InputStatus_Type(Integer32):
    """Custom type power2InputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_Power2InputStatus_Type.__name__ = "Integer32"
_Power2InputStatus_Object = MibScalar
power2InputStatus = _Power2InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 2),
    _Power2InputStatus_Type()
)
power2InputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power2InputStatus.setStatus("current")
_MonitorPortTable_Object = MibTable
monitorPortTable = _MonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3)
)
if mibBuilder.loadTexts:
    monitorPortTable.setStatus("current")
_MonitorPortEntry_Object = MibTableRow
monitorPortEntry = _MonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1)
)
monitorPortEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "monitorPortIndex"),
)
if mibBuilder.loadTexts:
    monitorPortEntry.setStatus("current")


class _MonitorPortIndex_Type(Integer32):
    """Custom type monitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MonitorPortIndex_Type.__name__ = "Integer32"
_MonitorPortIndex_Object = MibTableColumn
monitorPortIndex = _MonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1, 1),
    _MonitorPortIndex_Type()
)
monitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorPortIndex.setStatus("current")


class _MonitorLinkStatus_Type(Integer32):
    """Custom type monitorLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", -1),
          ("off", 0),
          ("on", 1))
    )


_MonitorLinkStatus_Type.__name__ = "Integer32"
_MonitorLinkStatus_Object = MibTableColumn
monitorLinkStatus = _MonitorLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1, 2),
    _MonitorLinkStatus_Type()
)
monitorLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorLinkStatus.setStatus("current")


class _MonitorSpeed_Type(Integer32):
    """Custom type monitorSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("speed10M-Half", 0),
          ("speed10M-Full", 1),
          ("speed100M-Half", 2),
          ("speed100M-Full", 3))
    )


_MonitorSpeed_Type.__name__ = "Integer32"
_MonitorSpeed_Object = MibTableColumn
monitorSpeed = _MonitorSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1, 3),
    _MonitorSpeed_Type()
)
monitorSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorSpeed.setStatus("current")


class _MonitorAutoMDI_Type(Integer32):
    """Custom type monitorAutoMDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("mdi", 0),
          ("mdiX", 1))
    )


_MonitorAutoMDI_Type.__name__ = "Integer32"
_MonitorAutoMDI_Object = MibTableColumn
monitorAutoMDI = _MonitorAutoMDI_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1, 4),
    _MonitorAutoMDI_Type()
)
monitorAutoMDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorAutoMDI.setStatus("current")
_MonitorTraffic_Type = Integer32
_MonitorTraffic_Object = MibTableColumn
monitorTraffic = _MonitorTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1, 5),
    _MonitorTraffic_Type()
)
monitorTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTraffic.setStatus("current")


class _MonitorFDXFlowCtrl_Type(Integer32):
    """Custom type monitorFDXFlowCtrl based on Integer32"""
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


_MonitorFDXFlowCtrl_Type.__name__ = "Integer32"
_MonitorFDXFlowCtrl_Object = MibTableColumn
monitorFDXFlowCtrl = _MonitorFDXFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 3, 1, 6),
    _MonitorFDXFlowCtrl_Type()
)
monitorFDXFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFDXFlowCtrl.setStatus("current")
_MonitorDiTable_Object = MibTable
monitorDiTable = _MonitorDiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 4)
)
if mibBuilder.loadTexts:
    monitorDiTable.setStatus("current")
_MonitorDiEntry_Object = MibTableRow
monitorDiEntry = _MonitorDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 4, 1)
)
monitorDiEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    monitorDiEntry.setStatus("current")


class _DiIndex_Type(Integer32):
    """Custom type diIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DiIndex_Type.__name__ = "Integer32"
_DiIndex_Object = MibTableColumn
diIndex = _DiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 4, 1, 1),
    _DiIndex_Type()
)
diIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diIndex.setStatus("current")


class _DiInputStatus_Type(Integer32):
    """Custom type diInputStatus based on Integer32"""
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


_DiInputStatus_Type.__name__ = "Integer32"
_DiInputStatus_Object = MibTableColumn
diInputStatus = _DiInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 10, 4, 1, 2),
    _DiInputStatus_Type()
)
diInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diInputStatus.setStatus("current")
_EmailWarning_ObjectIdentity = ObjectIdentity
emailWarning = _EmailWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11)
)
_EmailService_ObjectIdentity = ObjectIdentity
emailService = _EmailService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 1)
)
_EmailWarningMailServer_Type = DisplayString
_EmailWarningMailServer_Object = MibScalar
emailWarningMailServer = _EmailWarningMailServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 1, 1),
    _EmailWarningMailServer_Type()
)
emailWarningMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningMailServer.setStatus("current")
_EmailWarningFirstEmailAddr_Type = DisplayString
_EmailWarningFirstEmailAddr_Object = MibScalar
emailWarningFirstEmailAddr = _EmailWarningFirstEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 1, 2),
    _EmailWarningFirstEmailAddr_Type()
)
emailWarningFirstEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFirstEmailAddr.setStatus("current")
_EmailWarningSecondEmailAddr_Type = DisplayString
_EmailWarningSecondEmailAddr_Object = MibScalar
emailWarningSecondEmailAddr = _EmailWarningSecondEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 1, 3),
    _EmailWarningSecondEmailAddr_Type()
)
emailWarningSecondEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSecondEmailAddr.setStatus("current")
_EmailWarningThirdEmailAddr_Type = DisplayString
_EmailWarningThirdEmailAddr_Object = MibScalar
emailWarningThirdEmailAddr = _EmailWarningThirdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 1, 4),
    _EmailWarningThirdEmailAddr_Type()
)
emailWarningThirdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningThirdEmailAddr.setStatus("current")
_EmailWarningFourthEmailAddr_Type = DisplayString
_EmailWarningFourthEmailAddr_Object = MibScalar
emailWarningFourthEmailAddr = _EmailWarningFourthEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 1, 5),
    _EmailWarningFourthEmailAddr_Type()
)
emailWarningFourthEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFourthEmailAddr.setStatus("current")
_EmailWarningEventType_ObjectIdentity = ObjectIdentity
emailWarningEventType = _EmailWarningEventType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2)
)


class _EmailWarningEventServerColdStart_Type(Integer32):
    """Custom type emailWarningEventServerColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventServerColdStart_Type.__name__ = "Integer32"
_EmailWarningEventServerColdStart_Object = MibScalar
emailWarningEventServerColdStart = _EmailWarningEventServerColdStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 1),
    _EmailWarningEventServerColdStart_Type()
)
emailWarningEventServerColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventServerColdStart.setStatus("current")


class _EmailWarningEventServerWarmStart_Type(Integer32):
    """Custom type emailWarningEventServerWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventServerWarmStart_Type.__name__ = "Integer32"
_EmailWarningEventServerWarmStart_Object = MibScalar
emailWarningEventServerWarmStart = _EmailWarningEventServerWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 2),
    _EmailWarningEventServerWarmStart_Type()
)
emailWarningEventServerWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventServerWarmStart.setStatus("current")


class _EmailWarningEventConfigChange_Type(Integer32):
    """Custom type emailWarningEventConfigChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventConfigChange_Type.__name__ = "Integer32"
_EmailWarningEventConfigChange_Object = MibScalar
emailWarningEventConfigChange = _EmailWarningEventConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 3),
    _EmailWarningEventConfigChange_Type()
)
emailWarningEventConfigChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventConfigChange.setStatus("current")


class _EmailWarningEventPowerOn2Off_Type(Integer32):
    """Custom type emailWarningEventPowerOn2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventPowerOn2Off_Type.__name__ = "Integer32"
_EmailWarningEventPowerOn2Off_Object = MibScalar
emailWarningEventPowerOn2Off = _EmailWarningEventPowerOn2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 4),
    _EmailWarningEventPowerOn2Off_Type()
)
emailWarningEventPowerOn2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPowerOn2Off.setStatus("current")


class _EmailWarningEventPowerOff2On_Type(Integer32):
    """Custom type emailWarningEventPowerOff2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventPowerOff2On_Type.__name__ = "Integer32"
_EmailWarningEventPowerOff2On_Object = MibScalar
emailWarningEventPowerOff2On = _EmailWarningEventPowerOff2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 5),
    _EmailWarningEventPowerOff2On_Type()
)
emailWarningEventPowerOff2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPowerOff2On.setStatus("current")


class _EmailWarningEventAuthFail_Type(Integer32):
    """Custom type emailWarningEventAuthFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventAuthFail_Type.__name__ = "Integer32"
_EmailWarningEventAuthFail_Object = MibScalar
emailWarningEventAuthFail = _EmailWarningEventAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 6),
    _EmailWarningEventAuthFail_Type()
)
emailWarningEventAuthFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventAuthFail.setStatus("current")


class _EmailWarningEventCommRedundancyTopologyChanged_Type(Integer32):
    """Custom type emailWarningEventCommRedundancyTopologyChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventCommRedundancyTopologyChanged_Type.__name__ = "Integer32"
_EmailWarningEventCommRedundancyTopologyChanged_Object = MibScalar
emailWarningEventCommRedundancyTopologyChanged = _EmailWarningEventCommRedundancyTopologyChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 2, 7),
    _EmailWarningEventCommRedundancyTopologyChanged_Type()
)
emailWarningEventCommRedundancyTopologyChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventCommRedundancyTopologyChanged.setStatus("current")
_EmailWarningEventPortTable_Object = MibTable
emailWarningEventPortTable = _EmailWarningEventPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3)
)
if mibBuilder.loadTexts:
    emailWarningEventPortTable.setStatus("current")
_EmailWarningEventPortEntry_Object = MibTableRow
emailWarningEventPortEntry = _EmailWarningEventPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1)
)
emailWarningEventPortEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "emailWarningPortIndex"),
)
if mibBuilder.loadTexts:
    emailWarningEventPortEntry.setStatus("current")


class _EmailWarningPortIndex_Type(Integer32):
    """Custom type emailWarningPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EmailWarningPortIndex_Type.__name__ = "Integer32"
_EmailWarningPortIndex_Object = MibTableColumn
emailWarningPortIndex = _EmailWarningPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1, 1),
    _EmailWarningPortIndex_Type()
)
emailWarningPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailWarningPortIndex.setStatus("current")


class _EmailWarningEventPortLinkOn_Type(Integer32):
    """Custom type emailWarningEventPortLinkOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventPortLinkOn_Type.__name__ = "Integer32"
_EmailWarningEventPortLinkOn_Object = MibTableColumn
emailWarningEventPortLinkOn = _EmailWarningEventPortLinkOn_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1, 2),
    _EmailWarningEventPortLinkOn_Type()
)
emailWarningEventPortLinkOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPortLinkOn.setStatus("current")


class _EmailWarningEventPortLinkOff_Type(Integer32):
    """Custom type emailWarningEventPortLinkOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventPortLinkOff_Type.__name__ = "Integer32"
_EmailWarningEventPortLinkOff_Object = MibTableColumn
emailWarningEventPortLinkOff = _EmailWarningEventPortLinkOff_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1, 3),
    _EmailWarningEventPortLinkOff_Type()
)
emailWarningEventPortLinkOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPortLinkOff.setStatus("current")


class _EmailWarningEventPortTrafficOverload_Type(Integer32):
    """Custom type emailWarningEventPortTrafficOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventPortTrafficOverload_Type.__name__ = "Integer32"
_EmailWarningEventPortTrafficOverload_Object = MibTableColumn
emailWarningEventPortTrafficOverload = _EmailWarningEventPortTrafficOverload_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1, 4),
    _EmailWarningEventPortTrafficOverload_Type()
)
emailWarningEventPortTrafficOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPortTrafficOverload.setStatus("current")
_EmailWarningEventPortTrafficThreshold_Type = Integer32
_EmailWarningEventPortTrafficThreshold_Object = MibTableColumn
emailWarningEventPortTrafficThreshold = _EmailWarningEventPortTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1, 5),
    _EmailWarningEventPortTrafficThreshold_Type()
)
emailWarningEventPortTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPortTrafficThreshold.setStatus("current")
_EmailWarningEventPortTrafficDuration_Type = Integer32
_EmailWarningEventPortTrafficDuration_Object = MibTableColumn
emailWarningEventPortTrafficDuration = _EmailWarningEventPortTrafficDuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 3, 1, 6),
    _EmailWarningEventPortTrafficDuration_Type()
)
emailWarningEventPortTrafficDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventPortTrafficDuration.setStatus("current")
_EmailWarningEventDiTable_Object = MibTable
emailWarningEventDiTable = _EmailWarningEventDiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 4)
)
if mibBuilder.loadTexts:
    emailWarningEventDiTable.setStatus("current")
_EmailWarningEventDiEntry_Object = MibTableRow
emailWarningEventDiEntry = _EmailWarningEventDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 4, 1)
)
emailWarningEventDiEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    emailWarningEventDiEntry.setStatus("current")


class _EmailWarningEventDiInputOn2Off_Type(Integer32):
    """Custom type emailWarningEventDiInputOn2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventDiInputOn2Off_Type.__name__ = "Integer32"
_EmailWarningEventDiInputOn2Off_Object = MibTableColumn
emailWarningEventDiInputOn2Off = _EmailWarningEventDiInputOn2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 4, 1, 1),
    _EmailWarningEventDiInputOn2Off_Type()
)
emailWarningEventDiInputOn2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventDiInputOn2Off.setStatus("current")


class _EmailWarningEventDiInputOff2On_Type(Integer32):
    """Custom type emailWarningEventDiInputOff2On based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EmailWarningEventDiInputOff2On_Type.__name__ = "Integer32"
_EmailWarningEventDiInputOff2On_Object = MibTableColumn
emailWarningEventDiInputOff2On = _EmailWarningEventDiInputOff2On_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 11, 4, 1, 2),
    _EmailWarningEventDiInputOff2On_Type()
)
emailWarningEventDiInputOff2On.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningEventDiInputOff2On.setStatus("current")
_SetDeviceIp_ObjectIdentity = ObjectIdentity
setDeviceIp = _SetDeviceIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12)
)
_SetDevIpTable_Object = MibTable
setDevIpTable = _SetDevIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    setDevIpTable.setStatus("current")
_SetDevIpEntry_Object = MibTableRow
setDevIpEntry = _SetDevIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12, 1, 1)
)
setDevIpEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "setDevIpIndex"),
)
if mibBuilder.loadTexts:
    setDevIpEntry.setStatus("current")


class _SetDevIpIndex_Type(Integer32):
    """Custom type setDevIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SetDevIpIndex_Type.__name__ = "Integer32"
_SetDevIpIndex_Object = MibTableColumn
setDevIpIndex = _SetDevIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12, 1, 1, 1),
    _SetDevIpIndex_Type()
)
setDevIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpIndex.setStatus("current")
_SetDevIpCurrentIpofDevice_Type = DisplayString
_SetDevIpCurrentIpofDevice_Object = MibTableColumn
setDevIpCurrentIpofDevice = _SetDevIpCurrentIpofDevice_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12, 1, 1, 2),
    _SetDevIpCurrentIpofDevice_Type()
)
setDevIpCurrentIpofDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpCurrentIpofDevice.setStatus("current")


class _SetDevIpPresentBy_Type(Integer32):
    """Custom type setDevIpPresentBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("dhcpClient", 1),
          ("rarp", 2),
          ("bootp", 4))
    )


_SetDevIpPresentBy_Type.__name__ = "Integer32"
_SetDevIpPresentBy_Object = MibTableColumn
setDevIpPresentBy = _SetDevIpPresentBy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12, 1, 1, 3),
    _SetDevIpPresentBy_Type()
)
setDevIpPresentBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpPresentBy.setStatus("current")
_SetDevIpDedicatedIp_Type = IpAddress
_SetDevIpDedicatedIp_Object = MibTableColumn
setDevIpDedicatedIp = _SetDevIpDedicatedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 12, 1, 1, 4),
    _SetDevIpDedicatedIp_Type()
)
setDevIpDedicatedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDevIpDedicatedIp.setStatus("current")
_Mirroring_ObjectIdentity = ObjectIdentity
mirroring = _Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 13)
)


class _TargetPort_Type(Integer32):
    """Custom type targetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TargetPort_Type.__name__ = "Integer32"
_TargetPort_Object = MibScalar
targetPort = _TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 13, 1),
    _TargetPort_Type()
)
targetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetPort.setStatus("current")


class _MirroringPort_Type(Integer32):
    """Custom type mirroringPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MirroringPort_Type.__name__ = "Integer32"
_MirroringPort_Object = MibScalar
mirroringPort = _MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 13, 2),
    _MirroringPort_Type()
)
mirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirroringPort.setStatus("current")


class _MonitorDirection_Type(Integer32):
    """Custom type monitorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outputDataStream", 1),
          ("biDirectional", 2))
    )


_MonitorDirection_Type.__name__ = "Integer32"
_MonitorDirection_Object = MibScalar
monitorDirection = _MonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 13, 3),
    _MonitorDirection_Type()
)
monitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDirection.setStatus("current")
_CommRedundancy_ObjectIdentity = ObjectIdentity
commRedundancy = _CommRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16)
)


class _ProtocolOfRedundancySetup_Type(Integer32):
    """Custom type protocolOfRedundancySetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("spanningTree", 1),
          ("turboRing", 2))
    )


_ProtocolOfRedundancySetup_Type.__name__ = "Integer32"
_ProtocolOfRedundancySetup_Object = MibScalar
protocolOfRedundancySetup = _ProtocolOfRedundancySetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 1),
    _ProtocolOfRedundancySetup_Type()
)
protocolOfRedundancySetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolOfRedundancySetup.setStatus("current")
_TurboRing_ObjectIdentity = ObjectIdentity
turboRing = _TurboRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2)
)


class _TurboRingMaster_Type(Integer32):
    """Custom type turboRingMaster based on Integer32"""
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


_TurboRingMaster_Type.__name__ = "Integer32"
_TurboRingMaster_Object = MibScalar
turboRingMaster = _TurboRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 1),
    _TurboRingMaster_Type()
)
turboRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingMaster.setStatus("current")


class _TurboRingMasterSetup_Type(Integer32):
    """Custom type turboRingMasterSetup based on Integer32"""
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


_TurboRingMasterSetup_Type.__name__ = "Integer32"
_TurboRingMasterSetup_Object = MibScalar
turboRingMasterSetup = _TurboRingMasterSetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 2),
    _TurboRingMasterSetup_Type()
)
turboRingMasterSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingMasterSetup.setStatus("current")
_TurboRingPortTable_Object = MibTable
turboRingPortTable = _TurboRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    turboRingPortTable.setStatus("current")
_TurboRingPortEntry_Object = MibTableRow
turboRingPortEntry = _TurboRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 3, 1)
)
turboRingPortEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "turboRingPortIndex"),
)
if mibBuilder.loadTexts:
    turboRingPortEntry.setStatus("current")
_TurboRingPortIndex_Type = Integer32
_TurboRingPortIndex_Object = MibTableColumn
turboRingPortIndex = _TurboRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 3, 1, 1),
    _TurboRingPortIndex_Type()
)
turboRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortIndex.setStatus("current")


class _TurboRingPortStatus_Type(Integer32):
    """Custom type turboRingPortStatus based on Integer32"""
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
        *(("portDisabled", 0),
          ("notTurboRingPort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_TurboRingPortStatus_Type.__name__ = "Integer32"
_TurboRingPortStatus_Object = MibTableColumn
turboRingPortStatus = _TurboRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 3, 1, 2),
    _TurboRingPortStatus_Type()
)
turboRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortStatus.setStatus("current")


class _TurboRingPortDesignatedBridge_Type(OctetString):
    """Custom type turboRingPortDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TurboRingPortDesignatedBridge_Type.__name__ = "OctetString"
_TurboRingPortDesignatedBridge_Object = MibTableColumn
turboRingPortDesignatedBridge = _TurboRingPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 3, 1, 3),
    _TurboRingPortDesignatedBridge_Type()
)
turboRingPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortDesignatedBridge.setStatus("mandatory")
_TurboRingPortDesignatedPort_Type = Integer32
_TurboRingPortDesignatedPort_Object = MibTableColumn
turboRingPortDesignatedPort = _TurboRingPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 3, 1, 4),
    _TurboRingPortDesignatedPort_Type()
)
turboRingPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortDesignatedPort.setStatus("mandatory")


class _TurboRingDesignatedMaster_Type(OctetString):
    """Custom type turboRingDesignatedMaster based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_TurboRingDesignatedMaster_Type.__name__ = "OctetString"
_TurboRingDesignatedMaster_Object = MibScalar
turboRingDesignatedMaster = _TurboRingDesignatedMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 6),
    _TurboRingDesignatedMaster_Type()
)
turboRingDesignatedMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingDesignatedMaster.setStatus("mandatory")


class _TurboRingRdntPort1_Type(Integer32):
    """Custom type turboRingRdntPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TurboRingRdntPort1_Type.__name__ = "Integer32"
_TurboRingRdntPort1_Object = MibScalar
turboRingRdntPort1 = _TurboRingRdntPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 7),
    _TurboRingRdntPort1_Type()
)
turboRingRdntPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort1.setStatus("current")


class _TurboRingRdntPort2_Type(Integer32):
    """Custom type turboRingRdntPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TurboRingRdntPort2_Type.__name__ = "Integer32"
_TurboRingRdntPort2_Object = MibScalar
turboRingRdntPort2 = _TurboRingRdntPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 8),
    _TurboRingRdntPort2_Type()
)
turboRingRdntPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort2.setStatus("current")


class _TurboRingEnableCoupling_Type(Integer32):
    """Custom type turboRingEnableCoupling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TurboRingEnableCoupling_Type.__name__ = "Integer32"
_TurboRingEnableCoupling_Object = MibScalar
turboRingEnableCoupling = _TurboRingEnableCoupling_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 9),
    _TurboRingEnableCoupling_Type()
)
turboRingEnableCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingEnableCoupling.setStatus("current")


class _TurboRingCouplingPort_Type(Integer32):
    """Custom type turboRingCouplingPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TurboRingCouplingPort_Type.__name__ = "Integer32"
_TurboRingCouplingPort_Object = MibScalar
turboRingCouplingPort = _TurboRingCouplingPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 10),
    _TurboRingCouplingPort_Type()
)
turboRingCouplingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingCouplingPort.setStatus("current")


class _TurboRingCouplingPortStatus_Type(Integer32):
    """Custom type turboRingCouplingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("portDisabled", 0),
          ("notCouplingPort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("forwarding", 5))
    )


_TurboRingCouplingPortStatus_Type.__name__ = "Integer32"
_TurboRingCouplingPortStatus_Object = MibScalar
turboRingCouplingPortStatus = _TurboRingCouplingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 11),
    _TurboRingCouplingPortStatus_Type()
)
turboRingCouplingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingCouplingPortStatus.setStatus("current")


class _TurboRingControlPort_Type(Integer32):
    """Custom type turboRingControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_TurboRingControlPort_Type.__name__ = "Integer32"
_TurboRingControlPort_Object = MibScalar
turboRingControlPort = _TurboRingControlPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 12),
    _TurboRingControlPort_Type()
)
turboRingControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingControlPort.setStatus("current")


class _TurboRingControlPortStatus_Type(Integer32):
    """Custom type turboRingControlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("portDisabled", 0),
          ("notControlPort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("forwarding", 5),
          ("inactive", 6),
          ("active", 7))
    )


_TurboRingControlPortStatus_Type.__name__ = "Integer32"
_TurboRingControlPortStatus_Object = MibScalar
turboRingControlPortStatus = _TurboRingControlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 13),
    _TurboRingControlPortStatus_Type()
)
turboRingControlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingControlPortStatus.setStatus("current")


class _TurboRingBrokenStatus_Type(Integer32):
    """Custom type turboRingBrokenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("normal", 1),
          ("broken", 2))
    )


_TurboRingBrokenStatus_Type.__name__ = "Integer32"
_TurboRingBrokenStatus_Object = MibScalar
turboRingBrokenStatus = _TurboRingBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 2, 14),
    _TurboRingBrokenStatus_Type()
)
turboRingBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingBrokenStatus.setStatus("current")
_SpanningTree_ObjectIdentity = ObjectIdentity
spanningTree = _SpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3)
)


class _SpanningTreeRoot_Type(Integer32):
    """Custom type spanningTreeRoot based on Integer32"""
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


_SpanningTreeRoot_Type.__name__ = "Integer32"
_SpanningTreeRoot_Object = MibScalar
spanningTreeRoot = _SpanningTreeRoot_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 1),
    _SpanningTreeRoot_Type()
)
spanningTreeRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeRoot.setStatus("current")


class _SpanningTreeBridgePriority_Type(Integer32):
    """Custom type spanningTreeBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              8192,
              12288,
              16384,
              20480,
              24576,
              28672,
              32768,
              36864,
              40960,
              45056,
              49152,
              53248,
              57344,
              61440)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority4096", 4096),
          ("priority8192", 8192),
          ("priority12288", 12288),
          ("priority16384", 16384),
          ("priority20480", 20480),
          ("priority24576", 24576),
          ("priority28672", 28672),
          ("priority32768", 32768),
          ("priority36864", 36864),
          ("priority40960", 40960),
          ("priority45056", 45056),
          ("priority49152", 49152),
          ("priority53248", 53248),
          ("priority57344", 57344),
          ("priority61440", 61440))
    )


_SpanningTreeBridgePriority_Type.__name__ = "Integer32"
_SpanningTreeBridgePriority_Object = MibScalar
spanningTreeBridgePriority = _SpanningTreeBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 2),
    _SpanningTreeBridgePriority_Type()
)
spanningTreeBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeBridgePriority.setStatus("current")
_SpanningTreeHelloTime_Type = Integer32
_SpanningTreeHelloTime_Object = MibScalar
spanningTreeHelloTime = _SpanningTreeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 3),
    _SpanningTreeHelloTime_Type()
)
spanningTreeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeHelloTime.setStatus("current")
_SpanningTreeMaxAge_Type = Integer32
_SpanningTreeMaxAge_Object = MibScalar
spanningTreeMaxAge = _SpanningTreeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 4),
    _SpanningTreeMaxAge_Type()
)
spanningTreeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeMaxAge.setStatus("current")
_SpanningTreeForwardingDelay_Type = Integer32
_SpanningTreeForwardingDelay_Object = MibScalar
spanningTreeForwardingDelay = _SpanningTreeForwardingDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 5),
    _SpanningTreeForwardingDelay_Type()
)
spanningTreeForwardingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeForwardingDelay.setStatus("current")
_SpanningTreeTable_Object = MibTable
spanningTreeTable = _SpanningTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6)
)
if mibBuilder.loadTexts:
    spanningTreeTable.setStatus("current")
_SpanningTreeEntry_Object = MibTableRow
spanningTreeEntry = _SpanningTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6, 1)
)
spanningTreeEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "spanningTreeIndex"),
)
if mibBuilder.loadTexts:
    spanningTreeEntry.setStatus("current")


class _SpanningTreeIndex_Type(Integer32):
    """Custom type spanningTreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SpanningTreeIndex_Type.__name__ = "Integer32"
_SpanningTreeIndex_Object = MibTableColumn
spanningTreeIndex = _SpanningTreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6, 1, 1),
    _SpanningTreeIndex_Type()
)
spanningTreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeIndex.setStatus("current")


class _EnableSpanningTree_Type(Integer32):
    """Custom type enableSpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableSpanningTree_Type.__name__ = "Integer32"
_EnableSpanningTree_Object = MibTableColumn
enableSpanningTree = _EnableSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6, 1, 2),
    _EnableSpanningTree_Type()
)
enableSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSpanningTree.setStatus("current")


class _SpanningTreePortPriority_Type(Integer32):
    """Custom type spanningTreePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              80,
              96,
              112,
              128,
              144,
              160,
              176,
              192,
              208,
              224,
              240)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority16", 16),
          ("priority32", 32),
          ("priority48", 48),
          ("priority64", 64),
          ("priority80", 80),
          ("priority96", 96),
          ("priority112", 112),
          ("priority128", 128),
          ("priority144", 144),
          ("priority160", 160),
          ("priority176", 176),
          ("priority192", 192),
          ("priority208", 208),
          ("priority224", 224),
          ("priority240", 240))
    )


_SpanningTreePortPriority_Type.__name__ = "Integer32"
_SpanningTreePortPriority_Object = MibTableColumn
spanningTreePortPriority = _SpanningTreePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6, 1, 3),
    _SpanningTreePortPriority_Type()
)
spanningTreePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortPriority.setStatus("current")
_SpanningTreePortCost_Type = Integer32
_SpanningTreePortCost_Object = MibTableColumn
spanningTreePortCost = _SpanningTreePortCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6, 1, 4),
    _SpanningTreePortCost_Type()
)
spanningTreePortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortCost.setStatus("current")


class _SpanningTreePortStatus_Type(Integer32):
    """Custom type spanningTreePortStatus based on Integer32"""
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
        *(("portDisabled", 0),
          ("notSpanningTreePort", 1),
          ("linkDown", 2),
          ("blocked", 3),
          ("learning", 4),
          ("forwarding", 5))
    )


_SpanningTreePortStatus_Type.__name__ = "Integer32"
_SpanningTreePortStatus_Object = MibTableColumn
spanningTreePortStatus = _SpanningTreePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 3, 6, 1, 5),
    _SpanningTreePortStatus_Type()
)
spanningTreePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortStatus.setStatus("current")


class _ActiveProtocolOfRedundancy_Type(Integer32):
    """Custom type activeProtocolOfRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("spanningTree", 1),
          ("turboRing", 2))
    )


_ActiveProtocolOfRedundancy_Type.__name__ = "Integer32"
_ActiveProtocolOfRedundancy_Object = MibScalar
activeProtocolOfRedundancy = _ActiveProtocolOfRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 16, 4),
    _ActiveProtocolOfRedundancy_Type()
)
activeProtocolOfRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeProtocolOfRedundancy.setStatus("current")
_RelayWarning_ObjectIdentity = ObjectIdentity
relayWarning = _RelayWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17)
)
_RelayWarningTable_Object = MibTable
relayWarningTable = _RelayWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11)
)
if mibBuilder.loadTexts:
    relayWarningTable.setStatus("current")
_RelayWarningEntry_Object = MibTableRow
relayWarningEntry = _RelayWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1)
)
relayWarningEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "relayAlarmIndex"),
)
if mibBuilder.loadTexts:
    relayWarningEntry.setStatus("current")


class _RelayAlarmIndex_Type(Integer32):
    """Custom type relayAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RelayAlarmIndex_Type.__name__ = "Integer32"
_RelayAlarmIndex_Object = MibTableColumn
relayAlarmIndex = _RelayAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 1),
    _RelayAlarmIndex_Type()
)
relayAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayAlarmIndex.setStatus("current")


class _RelayWarningRelayContact_Type(Integer32):
    """Custom type relayWarningRelayContact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("opened", 1))
    )


_RelayWarningRelayContact_Type.__name__ = "Integer32"
_RelayWarningRelayContact_Object = MibTableColumn
relayWarningRelayContact = _RelayWarningRelayContact_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 2),
    _RelayWarningRelayContact_Type()
)
relayWarningRelayContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningRelayContact.setStatus("current")


class _OverrideRelayWarningSetting_Type(Integer32):
    """Custom type overrideRelayWarningSetting based on Integer32"""
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


_OverrideRelayWarningSetting_Type.__name__ = "Integer32"
_OverrideRelayWarningSetting_Object = MibTableColumn
overrideRelayWarningSetting = _OverrideRelayWarningSetting_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 3),
    _OverrideRelayWarningSetting_Type()
)
overrideRelayWarningSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    overrideRelayWarningSetting.setStatus("current")


class _RelayWarningPower1Off_Type(Integer32):
    """Custom type relayWarningPower1Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RelayWarningPower1Off_Type.__name__ = "Integer32"
_RelayWarningPower1Off_Object = MibTableColumn
relayWarningPower1Off = _RelayWarningPower1Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 4),
    _RelayWarningPower1Off_Type()
)
relayWarningPower1Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningPower1Off.setStatus("current")


class _RelayWarningPower1OffStatus_Type(Integer32):
    """Custom type relayWarningPower1OffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningPower1OffStatus_Type.__name__ = "Integer32"
_RelayWarningPower1OffStatus_Object = MibTableColumn
relayWarningPower1OffStatus = _RelayWarningPower1OffStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 5),
    _RelayWarningPower1OffStatus_Type()
)
relayWarningPower1OffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningPower1OffStatus.setStatus("current")


class _RelayWarningPower2Off_Type(Integer32):
    """Custom type relayWarningPower2Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RelayWarningPower2Off_Type.__name__ = "Integer32"
_RelayWarningPower2Off_Object = MibTableColumn
relayWarningPower2Off = _RelayWarningPower2Off_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 6),
    _RelayWarningPower2Off_Type()
)
relayWarningPower2Off.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningPower2Off.setStatus("current")


class _RelayWarningPower2OffStatus_Type(Integer32):
    """Custom type relayWarningPower2OffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningPower2OffStatus_Type.__name__ = "Integer32"
_RelayWarningPower2OffStatus_Object = MibTableColumn
relayWarningPower2OffStatus = _RelayWarningPower2OffStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 11, 1, 7),
    _RelayWarningPower2OffStatus_Type()
)
relayWarningPower2OffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningPower2OffStatus.setStatus("current")
_PortRelayWarningTable_Object = MibTable
portRelayWarningTable = _PortRelayWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12)
)
if mibBuilder.loadTexts:
    portRelayWarningTable.setStatus("current")
_PortRelayWarningEntry_Object = MibTableRow
portRelayWarningEntry = _PortRelayWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1)
)
portRelayWarningEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "portIndex"),
    (0, "MOXA-EDS508-MIB", "relayAlarmIndex"),
)
if mibBuilder.loadTexts:
    portRelayWarningEntry.setStatus("current")


class _RelayWarningLinkChanged_Type(Integer32):
    """Custom type relayWarningLinkChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 0),
          ("on2off", 1),
          ("off2on", 2))
    )


_RelayWarningLinkChanged_Type.__name__ = "Integer32"
_RelayWarningLinkChanged_Object = MibTableColumn
relayWarningLinkChanged = _RelayWarningLinkChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1, 1),
    _RelayWarningLinkChanged_Type()
)
relayWarningLinkChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningLinkChanged.setStatus("current")


class _RelayWarningLinkChangedStatus_Type(Integer32):
    """Custom type relayWarningLinkChangedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningLinkChangedStatus_Type.__name__ = "Integer32"
_RelayWarningLinkChangedStatus_Object = MibTableColumn
relayWarningLinkChangedStatus = _RelayWarningLinkChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1, 2),
    _RelayWarningLinkChangedStatus_Type()
)
relayWarningLinkChangedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningLinkChangedStatus.setStatus("current")


class _RelayWarningTrafficOverload_Type(Integer32):
    """Custom type relayWarningTrafficOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RelayWarningTrafficOverload_Type.__name__ = "Integer32"
_RelayWarningTrafficOverload_Object = MibTableColumn
relayWarningTrafficOverload = _RelayWarningTrafficOverload_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1, 3),
    _RelayWarningTrafficOverload_Type()
)
relayWarningTrafficOverload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningTrafficOverload.setStatus("current")


class _RelayWarningTrafficOverloadStatus_Type(Integer32):
    """Custom type relayWarningTrafficOverloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningTrafficOverloadStatus_Type.__name__ = "Integer32"
_RelayWarningTrafficOverloadStatus_Object = MibTableColumn
relayWarningTrafficOverloadStatus = _RelayWarningTrafficOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1, 4),
    _RelayWarningTrafficOverloadStatus_Type()
)
relayWarningTrafficOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningTrafficOverloadStatus.setStatus("current")
_RelayWarningTrafficThreshold_Type = Integer32
_RelayWarningTrafficThreshold_Object = MibTableColumn
relayWarningTrafficThreshold = _RelayWarningTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1, 5),
    _RelayWarningTrafficThreshold_Type()
)
relayWarningTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningTrafficThreshold.setStatus("current")
_RelayWarningTrafficDuration_Type = Integer32
_RelayWarningTrafficDuration_Object = MibTableColumn
relayWarningTrafficDuration = _RelayWarningTrafficDuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 12, 1, 6),
    _RelayWarningTrafficDuration_Type()
)
relayWarningTrafficDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningTrafficDuration.setStatus("current")
_DiRelayWarningTable_Object = MibTable
diRelayWarningTable = _DiRelayWarningTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 13)
)
if mibBuilder.loadTexts:
    diRelayWarningTable.setStatus("current")
_DiRelayWarningEntry_Object = MibTableRow
diRelayWarningEntry = _DiRelayWarningEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 13, 1)
)
diRelayWarningEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "diIndex"),
    (0, "MOXA-EDS508-MIB", "relayAlarmIndex"),
)
if mibBuilder.loadTexts:
    diRelayWarningEntry.setStatus("current")


class _RelayWarningDiInputChanged_Type(Integer32):
    """Custom type relayWarningDiInputChanged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("off", 1),
          ("on", 2))
    )


_RelayWarningDiInputChanged_Type.__name__ = "Integer32"
_RelayWarningDiInputChanged_Object = MibTableColumn
relayWarningDiInputChanged = _RelayWarningDiInputChanged_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 13, 1, 1),
    _RelayWarningDiInputChanged_Type()
)
relayWarningDiInputChanged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayWarningDiInputChanged.setStatus("current")


class _RelayWarningDiInputChangedStatus_Type(Integer32):
    """Custom type relayWarningDiInputChangedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-triggered", 0),
          ("triggered", 1))
    )


_RelayWarningDiInputChangedStatus_Type.__name__ = "Integer32"
_RelayWarningDiInputChangedStatus_Object = MibTableColumn
relayWarningDiInputChangedStatus = _RelayWarningDiInputChangedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 17, 13, 1, 2),
    _RelayWarningDiInputChangedStatus_Type()
)
relayWarningDiInputChangedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayWarningDiInputChangedStatus.setStatus("current")
_TrafficPrioritization_ObjectIdentity = ObjectIdentity
trafficPrioritization = _TrafficPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18)
)
_QosClassification_ObjectIdentity = ObjectIdentity
qosClassification = _QosClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1)
)


class _QueuingMechanism_Type(Integer32):
    """Custom type queuingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schedweightfair", 0),
          ("schedstrict", 1))
    )


_QueuingMechanism_Type.__name__ = "Integer32"
_QueuingMechanism_Object = MibScalar
queuingMechanism = _QueuingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1, 1),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("current")
_QosPortTable_Object = MibTable
qosPortTable = _QosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    qosPortTable.setStatus("current")
_QosPortEntry_Object = MibTableRow
qosPortEntry = _QosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1, 2, 1)
)
qosPortEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    qosPortEntry.setStatus("current")


class _InspectTos_Type(Integer32):
    """Custom type inspectTos based on Integer32"""
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


_InspectTos_Type.__name__ = "Integer32"
_InspectTos_Object = MibTableColumn
inspectTos = _InspectTos_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1, 2, 1, 1),
    _InspectTos_Type()
)
inspectTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inspectTos.setStatus("current")


class _InspectCos_Type(Integer32):
    """Custom type inspectCos based on Integer32"""
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


_InspectCos_Type.__name__ = "Integer32"
_InspectCos_Object = MibTableColumn
inspectCos = _InspectCos_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1, 2, 1, 2),
    _InspectCos_Type()
)
inspectCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inspectCos.setStatus("current")


class _DefaultPriority_Type(Integer32):
    """Custom type defaultPriority based on Integer32"""
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
        *(("low", 0),
          ("normal", 1),
          ("medium", 2),
          ("high", 3))
    )


_DefaultPriority_Type.__name__ = "Integer32"
_DefaultPriority_Object = MibTableColumn
defaultPriority = _DefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 1, 2, 1, 3),
    _DefaultPriority_Type()
)
defaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultPriority.setStatus("current")
_CosMapping_ObjectIdentity = ObjectIdentity
cosMapping = _CosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 2)
)
_CosMappingTable_Object = MibTable
cosMappingTable = _CosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    cosMappingTable.setStatus("current")
_CosMappingEntry_Object = MibTableRow
cosMappingEntry = _CosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 2, 1, 1)
)
cosMappingEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "cosTag"),
)
if mibBuilder.loadTexts:
    cosMappingEntry.setStatus("current")


class _CosTag_Type(Integer32):
    """Custom type cosTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CosTag_Type.__name__ = "Integer32"
_CosTag_Object = MibTableColumn
cosTag = _CosTag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 2, 1, 1, 1),
    _CosTag_Type()
)
cosTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosTag.setStatus("current")


class _CosMappedPriority_Type(Integer32):
    """Custom type cosMappedPriority based on Integer32"""
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
        *(("low", 0),
          ("normal", 1),
          ("medium", 2),
          ("high", 3))
    )


_CosMappedPriority_Type.__name__ = "Integer32"
_CosMappedPriority_Object = MibTableColumn
cosMappedPriority = _CosMappedPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 2, 1, 1, 2),
    _CosMappedPriority_Type()
)
cosMappedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosMappedPriority.setStatus("current")
_TosMapping_ObjectIdentity = ObjectIdentity
tosMapping = _TosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 3)
)
_TosMappingTable_Object = MibTable
tosMappingTable = _TosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    tosMappingTable.setStatus("current")
_TosMappingEntry_Object = MibTableRow
tosMappingEntry = _TosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 3, 1, 1)
)
tosMappingEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "tosClass"),
)
if mibBuilder.loadTexts:
    tosMappingEntry.setStatus("current")
_TosClass_Type = Integer32
_TosClass_Object = MibTableColumn
tosClass = _TosClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 3, 1, 1, 1),
    _TosClass_Type()
)
tosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tosClass.setStatus("current")


class _TosMappedPriority_Type(Integer32):
    """Custom type tosMappedPriority based on Integer32"""
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
        *(("low", 0),
          ("normal", 1),
          ("medium", 2),
          ("high", 3))
    )


_TosMappedPriority_Type.__name__ = "Integer32"
_TosMappedPriority_Object = MibTableColumn
tosMappedPriority = _TosMappedPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 18, 3, 1, 1, 2),
    _TosMappedPriority_Type()
)
tosMappedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tosMappedPriority.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19)
)
_VlanPortSettingTable_Object = MibTable
vlanPortSettingTable = _VlanPortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 1)
)
if mibBuilder.loadTexts:
    vlanPortSettingTable.setStatus("current")
_VlanPortSettingEntry_Object = MibTableRow
vlanPortSettingEntry = _VlanPortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 1, 1)
)
vlanPortSettingEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    vlanPortSettingEntry.setStatus("current")


class _PortVlanType_Type(Integer32):
    """Custom type portVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1))
    )


_PortVlanType_Type.__name__ = "Integer32"
_PortVlanType_Object = MibTableColumn
portVlanType = _PortVlanType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 1, 1, 1),
    _PortVlanType_Type()
)
portVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanType.setStatus("current")


class _PortDefaultVid_Type(Integer32):
    """Custom type portDefaultVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortDefaultVid_Type.__name__ = "Integer32"
_PortDefaultVid_Object = MibTableColumn
portDefaultVid = _PortDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 1, 1, 2),
    _PortDefaultVid_Type()
)
portDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDefaultVid.setStatus("current")
_PortFixedVid_Type = DisplayString
_PortFixedVid_Object = MibTableColumn
portFixedVid = _PortFixedVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 1, 1, 3),
    _PortFixedVid_Type()
)
portFixedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFixedVid.setStatus("current")
_PortForbiddenVid_Type = DisplayString
_PortForbiddenVid_Object = MibTableColumn
portForbiddenVid = _PortForbiddenVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 1, 1, 4),
    _PortForbiddenVid_Type()
)
portForbiddenVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForbiddenVid.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 2)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 2, 1)
)
vlanEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 2, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_JoinedAccessPorts_Type = OctetString
_JoinedAccessPorts_Object = MibTableColumn
joinedAccessPorts = _JoinedAccessPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 2, 1, 2),
    _JoinedAccessPorts_Type()
)
joinedAccessPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedAccessPorts.setStatus("current")
_JoinedTrunkPorts_Type = OctetString
_JoinedTrunkPorts_Object = MibTableColumn
joinedTrunkPorts = _JoinedTrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 2, 1, 3),
    _JoinedTrunkPorts_Type()
)
joinedTrunkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedTrunkPorts.setStatus("current")
_PortVidSetTable_ObjectIdentity = ObjectIdentity
portVidSetTable = _PortVidSetTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3)
)
_Port1DefaultVid_Type = Integer32
_Port1DefaultVid_Object = MibScalar
port1DefaultVid = _Port1DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 1),
    _Port1DefaultVid_Type()
)
port1DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port1DefaultVid.setStatus("current")
_Port2DefaultVid_Type = Integer32
_Port2DefaultVid_Object = MibScalar
port2DefaultVid = _Port2DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 2),
    _Port2DefaultVid_Type()
)
port2DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port2DefaultVid.setStatus("current")
_Port3DefaultVid_Type = Integer32
_Port3DefaultVid_Object = MibScalar
port3DefaultVid = _Port3DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 3),
    _Port3DefaultVid_Type()
)
port3DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port3DefaultVid.setStatus("current")
_Port4DefaultVid_Type = Integer32
_Port4DefaultVid_Object = MibScalar
port4DefaultVid = _Port4DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 4),
    _Port4DefaultVid_Type()
)
port4DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port4DefaultVid.setStatus("current")
_Port5DefaultVid_Type = Integer32
_Port5DefaultVid_Object = MibScalar
port5DefaultVid = _Port5DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 5),
    _Port5DefaultVid_Type()
)
port5DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port5DefaultVid.setStatus("current")
_Port6DefaultVid_Type = Integer32
_Port6DefaultVid_Object = MibScalar
port6DefaultVid = _Port6DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 6),
    _Port6DefaultVid_Type()
)
port6DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port6DefaultVid.setStatus("current")
_Port7DefaultVid_Type = Integer32
_Port7DefaultVid_Object = MibScalar
port7DefaultVid = _Port7DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 7),
    _Port7DefaultVid_Type()
)
port7DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port7DefaultVid.setStatus("current")
_Port8DefaultVid_Type = Integer32
_Port8DefaultVid_Object = MibScalar
port8DefaultVid = _Port8DefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 8),
    _Port8DefaultVid_Type()
)
port8DefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    port8DefaultVid.setStatus("current")
_ManagementVlanId_Type = Integer32
_ManagementVlanId_Object = MibScalar
managementVlanId = _ManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 9),
    _ManagementVlanId_Type()
)
managementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVlanId.setStatus("current")


class _PvidsAction_Type(Integer32):
    """Custom type pvidsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("activate", 1))
    )


_PvidsAction_Type.__name__ = "Integer32"
_PvidsAction_Object = MibScalar
pvidsAction = _PvidsAction_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 19, 3, 10),
    _PvidsAction_Type()
)
pvidsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pvidsAction.setStatus("current")
_MulticastFiltering_ObjectIdentity = ObjectIdentity
multicastFiltering = _MulticastFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20)
)
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1)
)
_QuerierQueryInterval_Type = Integer32
_QuerierQueryInterval_Object = MibScalar
querierQueryInterval = _QuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 1),
    _QuerierQueryInterval_Type()
)
querierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    querierQueryInterval.setStatus("current")
_IgmpSnoopingSettingTable_Object = MibTable
igmpSnoopingSettingTable = _IgmpSnoopingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    igmpSnoopingSettingTable.setStatus("current")
_IgmpSnoopingSettingEntry_Object = MibTableRow
igmpSnoopingSettingEntry = _IgmpSnoopingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 2, 1)
)
igmpSnoopingSettingEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    igmpSnoopingSettingEntry.setStatus("current")


class _EnableIgmpSnooping_Type(Integer32):
    """Custom type enableIgmpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableIgmpSnooping_Type.__name__ = "Integer32"
_EnableIgmpSnooping_Object = MibTableColumn
enableIgmpSnooping = _EnableIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 2, 1, 1),
    _EnableIgmpSnooping_Type()
)
enableIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableIgmpSnooping.setStatus("current")


class _EnableQuerier_Type(Integer32):
    """Custom type enableQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableQuerier_Type.__name__ = "Integer32"
_EnableQuerier_Object = MibTableColumn
enableQuerier = _EnableQuerier_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 2, 1, 2),
    _EnableQuerier_Type()
)
enableQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableQuerier.setStatus("current")
_FixedMulticastRouterPorts_Type = OctetString
_FixedMulticastRouterPorts_Object = MibTableColumn
fixedMulticastRouterPorts = _FixedMulticastRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 2, 1, 3),
    _FixedMulticastRouterPorts_Type()
)
fixedMulticastRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedMulticastRouterPorts.setStatus("current")
_LearnedMulticastRouterPorts_Type = OctetString
_LearnedMulticastRouterPorts_Object = MibTableColumn
learnedMulticastRouterPorts = _LearnedMulticastRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 2, 1, 4),
    _LearnedMulticastRouterPorts_Type()
)
learnedMulticastRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMulticastRouterPorts.setStatus("current")
_IgmpSnoopingMulticastGroupTable_Object = MibTable
igmpSnoopingMulticastGroupTable = _IgmpSnoopingMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    igmpSnoopingMulticastGroupTable.setStatus("current")
_IgmpSnoopingMulticastGroupEntry_Object = MibTableRow
igmpSnoopingMulticastGroupEntry = _IgmpSnoopingMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 3, 1)
)
igmpSnoopingMulticastGroupEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "vlanId"),
    (0, "MOXA-EDS508-MIB", "igmpSnoopingIpGroup"),
)
if mibBuilder.loadTexts:
    igmpSnoopingMulticastGroupEntry.setStatus("current")
_IgmpSnoopingIpGroup_Type = IpAddress
_IgmpSnoopingIpGroup_Object = MibTableColumn
igmpSnoopingIpGroup = _IgmpSnoopingIpGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 3, 1, 1),
    _IgmpSnoopingIpGroup_Type()
)
igmpSnoopingIpGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingIpGroup.setStatus("current")
_IgmpSnoopingMacGroup_Type = OctetString
_IgmpSnoopingMacGroup_Object = MibTableColumn
igmpSnoopingMacGroup = _IgmpSnoopingMacGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 3, 1, 2),
    _IgmpSnoopingMacGroup_Type()
)
igmpSnoopingMacGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingMacGroup.setStatus("current")
_IgmpSnoopingJoinedPorts_Type = OctetString
_IgmpSnoopingJoinedPorts_Object = MibTableColumn
igmpSnoopingJoinedPorts = _IgmpSnoopingJoinedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 3, 1, 3),
    _IgmpSnoopingJoinedPorts_Type()
)
igmpSnoopingJoinedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopingJoinedPorts.setStatus("current")


class _EnableGlobalIgmpSnooping_Type(Integer32):
    """Custom type enableGlobalIgmpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableGlobalIgmpSnooping_Type.__name__ = "Integer32"
_EnableGlobalIgmpSnooping_Object = MibScalar
enableGlobalIgmpSnooping = _EnableGlobalIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 1, 4),
    _EnableGlobalIgmpSnooping_Type()
)
enableGlobalIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGlobalIgmpSnooping.setStatus("current")
_StaticMulticast_ObjectIdentity = ObjectIdentity
staticMulticast = _StaticMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 2)
)
_StaticMulticastTable_Object = MibTable
staticMulticastTable = _StaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    staticMulticastTable.setStatus("current")
_StaticMulticastEntry_Object = MibTableRow
staticMulticastEntry = _StaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 2, 1, 1)
)
staticMulticastEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "staticMulticastAddress"),
)
if mibBuilder.loadTexts:
    staticMulticastEntry.setStatus("current")


class _StaticMulticastAddress_Type(OctetString):
    """Custom type staticMulticastAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_StaticMulticastAddress_Type.__name__ = "OctetString"
_StaticMulticastAddress_Object = MibTableColumn
staticMulticastAddress = _StaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 2, 1, 1, 1),
    _StaticMulticastAddress_Type()
)
staticMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastAddress.setStatus("current")
_StaticMulticastPortMask_Type = OctetString
_StaticMulticastPortMask_Object = MibTableColumn
staticMulticastPortMask = _StaticMulticastPortMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 2, 1, 1, 2),
    _StaticMulticastPortMask_Type()
)
staticMulticastPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastPortMask.setStatus("current")


class _StaticMulticastStatus_Type(Integer32):
    """Custom type staticMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_StaticMulticastStatus_Type.__name__ = "Integer32"
_StaticMulticastStatus_Object = MibTableColumn
staticMulticastStatus = _StaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 20, 2, 1, 1, 3),
    _StaticMulticastStatus_Type()
)
staticMulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastStatus.setStatus("current")
_RateLimiting_ObjectIdentity = ObjectIdentity
rateLimiting = _RateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21)
)
_RateLimitingTable_Object = MibTable
rateLimitingTable = _RateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1)
)
if mibBuilder.loadTexts:
    rateLimitingTable.setStatus("current")
_RateLimitingEntry_Object = MibTableRow
rateLimitingEntry = _RateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1)
)
rateLimitingEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    rateLimitingEntry.setStatus("current")


class _IngressLimitMode_Type(Integer32):
    """Custom type ingressLimitMode based on Integer32"""
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
        *(("all", 0),
          ("bmucast", 1),
          ("bmcast", 2),
          ("bcast", 3))
    )


_IngressLimitMode_Type.__name__ = "Integer32"
_IngressLimitMode_Object = MibTableColumn
ingressLimitMode = _IngressLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1, 1),
    _IngressLimitMode_Type()
)
ingressLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressLimitMode.setStatus("current")


class _IngressLowPriLimitRate_Type(Integer32):
    """Custom type ingressLowPriLimitRate based on Integer32"""
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
        *(("notlimit", 0),
          ("limit128k", 1),
          ("limit256k", 2),
          ("limit512k", 3),
          ("limit1M", 4),
          ("limit2M", 5),
          ("limit4M", 6),
          ("limit8M", 7))
    )


_IngressLowPriLimitRate_Type.__name__ = "Integer32"
_IngressLowPriLimitRate_Object = MibTableColumn
ingressLowPriLimitRate = _IngressLowPriLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1, 2),
    _IngressLowPriLimitRate_Type()
)
ingressLowPriLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressLowPriLimitRate.setStatus("current")


class _IngressNormalPriLimitRate_Type(Integer32):
    """Custom type ingressNormalPriLimitRate based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notlimit", 0),
          ("limit128k", 1),
          ("limit256k", 2),
          ("limit512k", 3),
          ("limit1M", 4),
          ("limit2M", 5),
          ("limit4M", 6),
          ("limit8M", 7),
          ("limit16M", 8))
    )


_IngressNormalPriLimitRate_Type.__name__ = "Integer32"
_IngressNormalPriLimitRate_Object = MibTableColumn
ingressNormalPriLimitRate = _IngressNormalPriLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1, 3),
    _IngressNormalPriLimitRate_Type()
)
ingressNormalPriLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressNormalPriLimitRate.setStatus("current")


class _IngressMediumPriLimitRate_Type(Integer32):
    """Custom type ingressMediumPriLimitRate based on Integer32"""
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
        *(("notlimit", 0),
          ("limit128k", 1),
          ("limit256k", 2),
          ("limit512k", 3),
          ("limit1M", 4),
          ("limit2M", 5),
          ("limit4M", 6),
          ("limit8M", 7),
          ("limit16M", 8),
          ("limit32M", 9))
    )


_IngressMediumPriLimitRate_Type.__name__ = "Integer32"
_IngressMediumPriLimitRate_Object = MibTableColumn
ingressMediumPriLimitRate = _IngressMediumPriLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1, 4),
    _IngressMediumPriLimitRate_Type()
)
ingressMediumPriLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressMediumPriLimitRate.setStatus("current")


class _IngressHighPriLimitRate_Type(Integer32):
    """Custom type ingressHighPriLimitRate based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notlimit", 0),
          ("limit128k", 1),
          ("limit256k", 2),
          ("limit512k", 3),
          ("limit1M", 4),
          ("limit2M", 5),
          ("limit4M", 6),
          ("limit8M", 7),
          ("limit16M", 8),
          ("limit32M", 9),
          ("limit64M", 10))
    )


_IngressHighPriLimitRate_Type.__name__ = "Integer32"
_IngressHighPriLimitRate_Object = MibTableColumn
ingressHighPriLimitRate = _IngressHighPriLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1, 5),
    _IngressHighPriLimitRate_Type()
)
ingressHighPriLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressHighPriLimitRate.setStatus("current")


class _EgressLimitRate_Type(Integer32):
    """Custom type egressLimitRate based on Integer32"""
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
        *(("notlimit", 0),
          ("limit128k", 1),
          ("limit256k", 2),
          ("limit512k", 3),
          ("limit1M", 4),
          ("limit2M", 5),
          ("limit4M", 6),
          ("limit8M", 7))
    )


_EgressLimitRate_Type.__name__ = "Integer32"
_EgressLimitRate_Object = MibTableColumn
egressLimitRate = _EgressLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 21, 1, 1, 6),
    _EgressLimitRate_Type()
)
egressLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressLimitRate.setStatus("current")
_PortLock_ObjectIdentity = ObjectIdentity
portLock = _PortLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22)
)
_PortLockTable_Object = MibTable
portLockTable = _PortLockTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 1)
)
if mibBuilder.loadTexts:
    portLockTable.setStatus("current")
_PortLockEntry_Object = MibTableRow
portLockEntry = _PortLockEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 1, 1)
)
portLockEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portLockEntry.setStatus("current")


class _EnablePortLock_Type(Integer32):
    """Custom type enablePortLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnablePortLock_Type.__name__ = "Integer32"
_EnablePortLock_Object = MibTableColumn
enablePortLock = _EnablePortLock_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 1, 1, 1),
    _EnablePortLock_Type()
)
enablePortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePortLock.setStatus("current")
_StaticUnicastTable_Object = MibTable
staticUnicastTable = _StaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 2)
)
if mibBuilder.loadTexts:
    staticUnicastTable.setStatus("current")
_StaticUnicastEntry_Object = MibTableRow
staticUnicastEntry = _StaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 2, 1)
)
staticUnicastEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "staticUnicastAddress"),
)
if mibBuilder.loadTexts:
    staticUnicastEntry.setStatus("current")


class _StaticUnicastAddress_Type(OctetString):
    """Custom type staticUnicastAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_StaticUnicastAddress_Type.__name__ = "OctetString"
_StaticUnicastAddress_Object = MibTableColumn
staticUnicastAddress = _StaticUnicastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 2, 1, 1),
    _StaticUnicastAddress_Type()
)
staticUnicastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticUnicastAddress.setStatus("current")
_StaticUnicastPort_Type = Integer32
_StaticUnicastPort_Object = MibTableColumn
staticUnicastPort = _StaticUnicastPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 2, 1, 2),
    _StaticUnicastPort_Type()
)
staticUnicastPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticUnicastPort.setStatus("current")


class _StaticUnicastPriority_Type(Integer32):
    """Custom type staticUnicastPriority based on Integer32"""
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
        *(("low", 0),
          ("normal", 1),
          ("medium", 2),
          ("high", 3))
    )


_StaticUnicastPriority_Type.__name__ = "Integer32"
_StaticUnicastPriority_Object = MibTableColumn
staticUnicastPriority = _StaticUnicastPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 2, 1, 3),
    _StaticUnicastPriority_Type()
)
staticUnicastPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticUnicastPriority.setStatus("current")


class _StaticUnicastStatus_Type(Integer32):
    """Custom type staticUnicastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_StaticUnicastStatus_Type.__name__ = "Integer32"
_StaticUnicastStatus_Object = MibTableColumn
staticUnicastStatus = _StaticUnicastStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 22, 2, 1, 4),
    _StaticUnicastStatus_Type()
)
staticUnicastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticUnicastStatus.setStatus("current")
_AccessibleIP_ObjectIdentity = ObjectIdentity
accessibleIP = _AccessibleIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30)
)


class _EnableAccessibleIP_Type(Integer32):
    """Custom type enableAccessibleIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableAccessibleIP_Type.__name__ = "Integer32"
_EnableAccessibleIP_Object = MibScalar
enableAccessibleIP = _EnableAccessibleIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30, 1),
    _EnableAccessibleIP_Type()
)
enableAccessibleIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAccessibleIP.setStatus("current")
_AccessibleIpTable_Object = MibTable
accessibleIpTable = _AccessibleIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30, 2)
)
if mibBuilder.loadTexts:
    accessibleIpTable.setStatus("current")
_AccessibleIpEntry_Object = MibTableRow
accessibleIpEntry = _AccessibleIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30, 2, 1)
)
accessibleIpEntry.setIndexNames(
    (0, "MOXA-EDS508-MIB", "accessibleIpAddress"),
)
if mibBuilder.loadTexts:
    accessibleIpEntry.setStatus("current")
_AccessibleIpAddress_Type = IpAddress
_AccessibleIpAddress_Object = MibTableColumn
accessibleIpAddress = _AccessibleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30, 2, 1, 1),
    _AccessibleIpAddress_Type()
)
accessibleIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpAddress.setStatus("current")
_AccessibleIpNetMask_Type = IpAddress
_AccessibleIpNetMask_Object = MibTableColumn
accessibleIpNetMask = _AccessibleIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30, 2, 1, 2),
    _AccessibleIpNetMask_Type()
)
accessibleIpNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpNetMask.setStatus("current")


class _AIpStatus_Type(Integer32):
    """Custom type aIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_AIpStatus_Type.__name__ = "Integer32"
_AIpStatus_Object = MibTableColumn
aIpStatus = _AIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 30, 2, 1, 3),
    _AIpStatus_Type()
)
aIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aIpStatus.setStatus("current")
_SysFileUpdate_ObjectIdentity = ObjectIdentity
sysFileUpdate = _SysFileUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 31)
)
_TftpServer_Type = DisplayString
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 31, 1),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")
_FirmwarePathName_Type = DisplayString
_FirmwarePathName_Object = MibScalar
firmwarePathName = _FirmwarePathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 31, 2),
    _FirmwarePathName_Type()
)
firmwarePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwarePathName.setStatus("current")
_LogPathName_Type = DisplayString
_LogPathName_Object = MibScalar
logPathName = _LogPathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 31, 3),
    _LogPathName_Type()
)
logPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPathName.setStatus("current")
_ConfPathName_Type = DisplayString
_ConfPathName_Object = MibScalar
confPathName = _ConfPathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 31, 4),
    _ConfPathName_Type()
)
confPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confPathName.setStatus("current")
_TimeSetting_ObjectIdentity = ObjectIdentity
timeSetting = _TimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 32)
)
_SysDateTime_Type = DateAndTime
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 32, 1),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")
_CalibratePeriod_Type = Integer32
_CalibratePeriod_Object = MibScalar
calibratePeriod = _CalibratePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 32, 2),
    _CalibratePeriod_Type()
)
calibratePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibratePeriod.setStatus("current")
_TimeServer1_Type = DisplayString
_TimeServer1_Object = MibScalar
timeServer1 = _TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 32, 3),
    _TimeServer1_Type()
)
timeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer1.setStatus("current")
_TimeServer2_Type = DisplayString
_TimeServer2_Object = MibScalar
timeServer2 = _TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 32, 4),
    _TimeServer2_Type()
)
timeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer2.setStatus("current")

# Managed Objects groups


# Notification objects

configChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 10)
)
if mibBuilder.loadTexts:
    configChangeTrap.setStatus(
        ""
    )

powerOn2OffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 11)
)
if mibBuilder.loadTexts:
    powerOn2OffTrap.setStatus(
        ""
    )

powerOff2OnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 12)
)
if mibBuilder.loadTexts:
    powerOff2OnTrap.setStatus(
        ""
    )

trafficOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 13)
)
if mibBuilder.loadTexts:
    trafficOverloadTrap.setStatus(
        ""
    )

redundancyTopologyChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 14)
)
if mibBuilder.loadTexts:
    redundancyTopologyChangedTrap.setStatus(
        ""
    )

turboRingCouplingPortChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 15)
)
if mibBuilder.loadTexts:
    turboRingCouplingPortChangedTrap.setStatus(
        ""
    )

turboRingMasterChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 1, 0, 16)
)
if mibBuilder.loadTexts:
    turboRingMasterChangedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-EDS508-MIB",
    **{"DisplayString": DisplayString,
       "moxa": moxa,
       "industrialEthernet": industrialEthernet,
       "etherDeviceSwitch": etherDeviceSwitch,
       "configChangeTrap": configChangeTrap,
       "powerOn2OffTrap": powerOn2OffTrap,
       "powerOff2OnTrap": powerOff2OnTrap,
       "trafficOverloadTrap": trafficOverloadTrap,
       "redundancyTopologyChangedTrap": redundancyTopologyChangedTrap,
       "turboRingCouplingPortChangedTrap": turboRingCouplingPortChangedTrap,
       "turboRingMasterChangedTrap": turboRingMasterChangedTrap,
       "portsNumber": portsNumber,
       "switchModel": switchModel,
       "firmwareVersion": firmwareVersion,
       "enableWebConfig": enableWebConfig,
       "enableTelnetConsole": enableTelnetConsole,
       "lineSwapRecovery": lineSwapRecovery,
       "networkSetting": networkSetting,
       "switchIpAddr": switchIpAddr,
       "switchIpMask": switchIpMask,
       "defaultGateway": defaultGateway,
       "enableAutoIpConfig": enableAutoIpConfig,
       "dnsServer1IpAddr": dnsServer1IpAddr,
       "snmpCommunityName": snmpCommunityName,
       "trapServerAddr": trapServerAddr,
       "dnsServer2IpAddr": dnsServer2IpAddr,
       "portSetting": portSetting,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portEnable": portEnable,
       "portSpeed": portSpeed,
       "portMDI": portMDI,
       "portFDXFlowCtrl": portFDXFlowCtrl,
       "portName": portName,
       "portTrunkingGroup": portTrunkingGroup,
       "monitor": monitor,
       "power1InputStatus": power1InputStatus,
       "power2InputStatus": power2InputStatus,
       "monitorPortTable": monitorPortTable,
       "monitorPortEntry": monitorPortEntry,
       "monitorPortIndex": monitorPortIndex,
       "monitorLinkStatus": monitorLinkStatus,
       "monitorSpeed": monitorSpeed,
       "monitorAutoMDI": monitorAutoMDI,
       "monitorTraffic": monitorTraffic,
       "monitorFDXFlowCtrl": monitorFDXFlowCtrl,
       "monitorDiTable": monitorDiTable,
       "monitorDiEntry": monitorDiEntry,
       "diIndex": diIndex,
       "diInputStatus": diInputStatus,
       "emailWarning": emailWarning,
       "emailService": emailService,
       "emailWarningMailServer": emailWarningMailServer,
       "emailWarningFirstEmailAddr": emailWarningFirstEmailAddr,
       "emailWarningSecondEmailAddr": emailWarningSecondEmailAddr,
       "emailWarningThirdEmailAddr": emailWarningThirdEmailAddr,
       "emailWarningFourthEmailAddr": emailWarningFourthEmailAddr,
       "emailWarningEventType": emailWarningEventType,
       "emailWarningEventServerColdStart": emailWarningEventServerColdStart,
       "emailWarningEventServerWarmStart": emailWarningEventServerWarmStart,
       "emailWarningEventConfigChange": emailWarningEventConfigChange,
       "emailWarningEventPowerOn2Off": emailWarningEventPowerOn2Off,
       "emailWarningEventPowerOff2On": emailWarningEventPowerOff2On,
       "emailWarningEventAuthFail": emailWarningEventAuthFail,
       "emailWarningEventCommRedundancyTopologyChanged": emailWarningEventCommRedundancyTopologyChanged,
       "emailWarningEventPortTable": emailWarningEventPortTable,
       "emailWarningEventPortEntry": emailWarningEventPortEntry,
       "emailWarningPortIndex": emailWarningPortIndex,
       "emailWarningEventPortLinkOn": emailWarningEventPortLinkOn,
       "emailWarningEventPortLinkOff": emailWarningEventPortLinkOff,
       "emailWarningEventPortTrafficOverload": emailWarningEventPortTrafficOverload,
       "emailWarningEventPortTrafficThreshold": emailWarningEventPortTrafficThreshold,
       "emailWarningEventPortTrafficDuration": emailWarningEventPortTrafficDuration,
       "emailWarningEventDiTable": emailWarningEventDiTable,
       "emailWarningEventDiEntry": emailWarningEventDiEntry,
       "emailWarningEventDiInputOn2Off": emailWarningEventDiInputOn2Off,
       "emailWarningEventDiInputOff2On": emailWarningEventDiInputOff2On,
       "setDeviceIp": setDeviceIp,
       "setDevIpTable": setDevIpTable,
       "setDevIpEntry": setDevIpEntry,
       "setDevIpIndex": setDevIpIndex,
       "setDevIpCurrentIpofDevice": setDevIpCurrentIpofDevice,
       "setDevIpPresentBy": setDevIpPresentBy,
       "setDevIpDedicatedIp": setDevIpDedicatedIp,
       "mirroring": mirroring,
       "targetPort": targetPort,
       "mirroringPort": mirroringPort,
       "monitorDirection": monitorDirection,
       "commRedundancy": commRedundancy,
       "protocolOfRedundancySetup": protocolOfRedundancySetup,
       "turboRing": turboRing,
       "turboRingMaster": turboRingMaster,
       "turboRingMasterSetup": turboRingMasterSetup,
       "turboRingPortTable": turboRingPortTable,
       "turboRingPortEntry": turboRingPortEntry,
       "turboRingPortIndex": turboRingPortIndex,
       "turboRingPortStatus": turboRingPortStatus,
       "turboRingPortDesignatedBridge": turboRingPortDesignatedBridge,
       "turboRingPortDesignatedPort": turboRingPortDesignatedPort,
       "turboRingDesignatedMaster": turboRingDesignatedMaster,
       "turboRingRdntPort1": turboRingRdntPort1,
       "turboRingRdntPort2": turboRingRdntPort2,
       "turboRingEnableCoupling": turboRingEnableCoupling,
       "turboRingCouplingPort": turboRingCouplingPort,
       "turboRingCouplingPortStatus": turboRingCouplingPortStatus,
       "turboRingControlPort": turboRingControlPort,
       "turboRingControlPortStatus": turboRingControlPortStatus,
       "turboRingBrokenStatus": turboRingBrokenStatus,
       "spanningTree": spanningTree,
       "spanningTreeRoot": spanningTreeRoot,
       "spanningTreeBridgePriority": spanningTreeBridgePriority,
       "spanningTreeHelloTime": spanningTreeHelloTime,
       "spanningTreeMaxAge": spanningTreeMaxAge,
       "spanningTreeForwardingDelay": spanningTreeForwardingDelay,
       "spanningTreeTable": spanningTreeTable,
       "spanningTreeEntry": spanningTreeEntry,
       "spanningTreeIndex": spanningTreeIndex,
       "enableSpanningTree": enableSpanningTree,
       "spanningTreePortPriority": spanningTreePortPriority,
       "spanningTreePortCost": spanningTreePortCost,
       "spanningTreePortStatus": spanningTreePortStatus,
       "activeProtocolOfRedundancy": activeProtocolOfRedundancy,
       "relayWarning": relayWarning,
       "relayWarningTable": relayWarningTable,
       "relayWarningEntry": relayWarningEntry,
       "relayAlarmIndex": relayAlarmIndex,
       "relayWarningRelayContact": relayWarningRelayContact,
       "overrideRelayWarningSetting": overrideRelayWarningSetting,
       "relayWarningPower1Off": relayWarningPower1Off,
       "relayWarningPower1OffStatus": relayWarningPower1OffStatus,
       "relayWarningPower2Off": relayWarningPower2Off,
       "relayWarningPower2OffStatus": relayWarningPower2OffStatus,
       "portRelayWarningTable": portRelayWarningTable,
       "portRelayWarningEntry": portRelayWarningEntry,
       "relayWarningLinkChanged": relayWarningLinkChanged,
       "relayWarningLinkChangedStatus": relayWarningLinkChangedStatus,
       "relayWarningTrafficOverload": relayWarningTrafficOverload,
       "relayWarningTrafficOverloadStatus": relayWarningTrafficOverloadStatus,
       "relayWarningTrafficThreshold": relayWarningTrafficThreshold,
       "relayWarningTrafficDuration": relayWarningTrafficDuration,
       "diRelayWarningTable": diRelayWarningTable,
       "diRelayWarningEntry": diRelayWarningEntry,
       "relayWarningDiInputChanged": relayWarningDiInputChanged,
       "relayWarningDiInputChangedStatus": relayWarningDiInputChangedStatus,
       "trafficPrioritization": trafficPrioritization,
       "qosClassification": qosClassification,
       "queuingMechanism": queuingMechanism,
       "qosPortTable": qosPortTable,
       "qosPortEntry": qosPortEntry,
       "inspectTos": inspectTos,
       "inspectCos": inspectCos,
       "defaultPriority": defaultPriority,
       "cosMapping": cosMapping,
       "cosMappingTable": cosMappingTable,
       "cosMappingEntry": cosMappingEntry,
       "cosTag": cosTag,
       "cosMappedPriority": cosMappedPriority,
       "tosMapping": tosMapping,
       "tosMappingTable": tosMappingTable,
       "tosMappingEntry": tosMappingEntry,
       "tosClass": tosClass,
       "tosMappedPriority": tosMappedPriority,
       "vlan": vlan,
       "vlanPortSettingTable": vlanPortSettingTable,
       "vlanPortSettingEntry": vlanPortSettingEntry,
       "portVlanType": portVlanType,
       "portDefaultVid": portDefaultVid,
       "portFixedVid": portFixedVid,
       "portForbiddenVid": portForbiddenVid,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanId": vlanId,
       "joinedAccessPorts": joinedAccessPorts,
       "joinedTrunkPorts": joinedTrunkPorts,
       "portVidSetTable": portVidSetTable,
       "port1DefaultVid": port1DefaultVid,
       "port2DefaultVid": port2DefaultVid,
       "port3DefaultVid": port3DefaultVid,
       "port4DefaultVid": port4DefaultVid,
       "port5DefaultVid": port5DefaultVid,
       "port6DefaultVid": port6DefaultVid,
       "port7DefaultVid": port7DefaultVid,
       "port8DefaultVid": port8DefaultVid,
       "managementVlanId": managementVlanId,
       "pvidsAction": pvidsAction,
       "multicastFiltering": multicastFiltering,
       "igmpSnooping": igmpSnooping,
       "querierQueryInterval": querierQueryInterval,
       "igmpSnoopingSettingTable": igmpSnoopingSettingTable,
       "igmpSnoopingSettingEntry": igmpSnoopingSettingEntry,
       "enableIgmpSnooping": enableIgmpSnooping,
       "enableQuerier": enableQuerier,
       "fixedMulticastRouterPorts": fixedMulticastRouterPorts,
       "learnedMulticastRouterPorts": learnedMulticastRouterPorts,
       "igmpSnoopingMulticastGroupTable": igmpSnoopingMulticastGroupTable,
       "igmpSnoopingMulticastGroupEntry": igmpSnoopingMulticastGroupEntry,
       "igmpSnoopingIpGroup": igmpSnoopingIpGroup,
       "igmpSnoopingMacGroup": igmpSnoopingMacGroup,
       "igmpSnoopingJoinedPorts": igmpSnoopingJoinedPorts,
       "enableGlobalIgmpSnooping": enableGlobalIgmpSnooping,
       "staticMulticast": staticMulticast,
       "staticMulticastTable": staticMulticastTable,
       "staticMulticastEntry": staticMulticastEntry,
       "staticMulticastAddress": staticMulticastAddress,
       "staticMulticastPortMask": staticMulticastPortMask,
       "staticMulticastStatus": staticMulticastStatus,
       "rateLimiting": rateLimiting,
       "rateLimitingTable": rateLimitingTable,
       "rateLimitingEntry": rateLimitingEntry,
       "ingressLimitMode": ingressLimitMode,
       "ingressLowPriLimitRate": ingressLowPriLimitRate,
       "ingressNormalPriLimitRate": ingressNormalPriLimitRate,
       "ingressMediumPriLimitRate": ingressMediumPriLimitRate,
       "ingressHighPriLimitRate": ingressHighPriLimitRate,
       "egressLimitRate": egressLimitRate,
       "portLock": portLock,
       "portLockTable": portLockTable,
       "portLockEntry": portLockEntry,
       "enablePortLock": enablePortLock,
       "staticUnicastTable": staticUnicastTable,
       "staticUnicastEntry": staticUnicastEntry,
       "staticUnicastAddress": staticUnicastAddress,
       "staticUnicastPort": staticUnicastPort,
       "staticUnicastPriority": staticUnicastPriority,
       "staticUnicastStatus": staticUnicastStatus,
       "accessibleIP": accessibleIP,
       "enableAccessibleIP": enableAccessibleIP,
       "accessibleIpTable": accessibleIpTable,
       "accessibleIpEntry": accessibleIpEntry,
       "accessibleIpAddress": accessibleIpAddress,
       "accessibleIpNetMask": accessibleIpNetMask,
       "aIpStatus": aIpStatus,
       "sysFileUpdate": sysFileUpdate,
       "tftpServer": tftpServer,
       "firmwarePathName": firmwarePathName,
       "logPathName": logPathName,
       "confPathName": confPathName,
       "timeSetting": timeSetting,
       "sysDateTime": sysDateTime,
       "calibratePeriod": calibratePeriod,
       "timeServer1": timeServer1,
       "timeServer2": timeServer2}
)
