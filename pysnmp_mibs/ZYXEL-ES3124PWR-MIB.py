# SNMP MIB module (ZYXEL-ES3124PWR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-ES3124PWR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:40 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(OperationResponseStatus,) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "OperationResponseStatus")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

faultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26)
)

faultTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UtcTimeStamp(TextualConvention, Unsigned32):
    status = "current"


class EventIdNumber(TextualConvention, Integer32):
    status = "current"


class EventSeverity(TextualConvention, Integer32):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("informational", 4))
    )



class EventServiceAffective(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noServiceAffected", 1),
          ("serviceAffected", 2))
    )



class InstanceType(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("node", 2),
          ("shelf", 3),
          ("line", 4),
          ("switch", 5),
          ("lsp", 6),
          ("l2Interface", 7),
          ("l3Interface", 8),
          ("rowIndex", 9))
    )



class EventPersistence(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("delta", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Zyxel_ObjectIdentity = ObjectIdentity
zyxel = _Zyxel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1)
)
_AccessSwitch_ObjectIdentity = ObjectIdentity
accessSwitch = _AccessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5)
)
_EsSeries_ObjectIdentity = ObjectIdentity
esSeries = _EsSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8)
)
_Es3124pwr_ObjectIdentity = ObjectIdentity
es3124pwr = _Es3124pwr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14)
)
_SysInfo_ObjectIdentity = ObjectIdentity
sysInfo = _SysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1)
)
_SysSwPlatformMajorVers_Type = Integer32
_SysSwPlatformMajorVers_Object = MibScalar
sysSwPlatformMajorVers = _SysSwPlatformMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 1),
    _SysSwPlatformMajorVers_Type()
)
sysSwPlatformMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMajorVers.setStatus("mandatory")
_SysSwPlatformMinorVers_Type = Integer32
_SysSwPlatformMinorVers_Object = MibScalar
sysSwPlatformMinorVers = _SysSwPlatformMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 2),
    _SysSwPlatformMinorVers_Type()
)
sysSwPlatformMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwPlatformMinorVers.setStatus("mandatory")
_SysSwModelString_Type = DisplayString
_SysSwModelString_Object = MibScalar
sysSwModelString = _SysSwModelString_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 3),
    _SysSwModelString_Type()
)
sysSwModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwModelString.setStatus("mandatory")
_SysSwVersionControlNbr_Type = Integer32
_SysSwVersionControlNbr_Object = MibScalar
sysSwVersionControlNbr = _SysSwVersionControlNbr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 4),
    _SysSwVersionControlNbr_Type()
)
sysSwVersionControlNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwVersionControlNbr.setStatus("mandatory")
_SysSwDay_Type = Integer32
_SysSwDay_Object = MibScalar
sysSwDay = _SysSwDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 5),
    _SysSwDay_Type()
)
sysSwDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwDay.setStatus("mandatory")
_SysSwMonth_Type = Integer32
_SysSwMonth_Object = MibScalar
sysSwMonth = _SysSwMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 6),
    _SysSwMonth_Type()
)
sysSwMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwMonth.setStatus("mandatory")
_SysSwYear_Type = Integer32
_SysSwYear_Object = MibScalar
sysSwYear = _SysSwYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 7),
    _SysSwYear_Type()
)
sysSwYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSwYear.setStatus("mandatory")
_SysHwMajorVers_Type = Integer32
_SysHwMajorVers_Object = MibScalar
sysHwMajorVers = _SysHwMajorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 8),
    _SysHwMajorVers_Type()
)
sysHwMajorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMajorVers.setStatus("mandatory")
_SysHwMinorVers_Type = Integer32
_SysHwMinorVers_Object = MibScalar
sysHwMinorVers = _SysHwMinorVers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 9),
    _SysHwMinorVers_Type()
)
sysHwMinorVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHwMinorVers.setStatus("mandatory")
_SysSerialNumber_Type = DisplayString
_SysSerialNumber_Object = MibScalar
sysSerialNumber = _SysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 1, 10),
    _SysSerialNumber_Type()
)
sysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSerialNumber.setStatus("mandatory")
_RateLimitSetup_ObjectIdentity = ObjectIdentity
rateLimitSetup = _RateLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2)
)
_RateLimitState_Type = EnabledStatus
_RateLimitState_Object = MibScalar
rateLimitState = _RateLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2, 1),
    _RateLimitState_Type()
)
rateLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitState.setStatus("mandatory")
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("mandatory")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("mandatory")
_RateLimitPortState_Type = EnabledStatus
_RateLimitPortState_Object = MibTableColumn
rateLimitPortState = _RateLimitPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2, 2, 1, 1),
    _RateLimitPortState_Type()
)
rateLimitPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortState.setStatus("mandatory")
_RateLimitPortIngRate_Type = Integer32
_RateLimitPortIngRate_Object = MibTableColumn
rateLimitPortIngRate = _RateLimitPortIngRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2, 2, 1, 2),
    _RateLimitPortIngRate_Type()
)
rateLimitPortIngRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortIngRate.setStatus("mandatory")
_RateLimitPortEgrRate_Type = Integer32
_RateLimitPortEgrRate_Object = MibTableColumn
rateLimitPortEgrRate = _RateLimitPortEgrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 2, 2, 1, 3),
    _RateLimitPortEgrRate_Type()
)
rateLimitPortEgrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitPortEgrRate.setStatus("mandatory")
_BrLimitSetup_ObjectIdentity = ObjectIdentity
brLimitSetup = _BrLimitSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3)
)
_BrLimitState_Type = EnabledStatus
_BrLimitState_Object = MibScalar
brLimitState = _BrLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 1),
    _BrLimitState_Type()
)
brLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitState.setStatus("mandatory")
_BrLimitPortTable_Object = MibTable
brLimitPortTable = _BrLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2)
)
if mibBuilder.loadTexts:
    brLimitPortTable.setStatus("mandatory")
_BrLimitPortEntry_Object = MibTableRow
brLimitPortEntry = _BrLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1)
)
brLimitPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    brLimitPortEntry.setStatus("mandatory")
_BrLimitPortBrState_Type = EnabledStatus
_BrLimitPortBrState_Object = MibTableColumn
brLimitPortBrState = _BrLimitPortBrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1, 1),
    _BrLimitPortBrState_Type()
)
brLimitPortBrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrState.setStatus("mandatory")
_BrLimitPortBrRate_Type = Integer32
_BrLimitPortBrRate_Object = MibTableColumn
brLimitPortBrRate = _BrLimitPortBrRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1, 2),
    _BrLimitPortBrRate_Type()
)
brLimitPortBrRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortBrRate.setStatus("mandatory")
_BrLimitPortMcState_Type = EnabledStatus
_BrLimitPortMcState_Object = MibTableColumn
brLimitPortMcState = _BrLimitPortMcState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1, 3),
    _BrLimitPortMcState_Type()
)
brLimitPortMcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcState.setStatus("mandatory")
_BrLimitPortMcRate_Type = Integer32
_BrLimitPortMcRate_Object = MibTableColumn
brLimitPortMcRate = _BrLimitPortMcRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1, 4),
    _BrLimitPortMcRate_Type()
)
brLimitPortMcRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortMcRate.setStatus("mandatory")
_BrLimitPortDlfState_Type = EnabledStatus
_BrLimitPortDlfState_Object = MibTableColumn
brLimitPortDlfState = _BrLimitPortDlfState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1, 5),
    _BrLimitPortDlfState_Type()
)
brLimitPortDlfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfState.setStatus("mandatory")
_BrLimitPortDlfRate_Type = Integer32
_BrLimitPortDlfRate_Object = MibTableColumn
brLimitPortDlfRate = _BrLimitPortDlfRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 3, 2, 1, 6),
    _BrLimitPortDlfRate_Type()
)
brLimitPortDlfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brLimitPortDlfRate.setStatus("mandatory")
_PortSecuritySetup_ObjectIdentity = ObjectIdentity
portSecuritySetup = _PortSecuritySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4)
)
_PortSecurityState_Type = EnabledStatus
_PortSecurityState_Object = MibScalar
portSecurityState = _PortSecurityState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 1),
    _PortSecurityState_Type()
)
portSecurityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityState.setStatus("mandatory")
_PortSecurityPortTable_Object = MibTable
portSecurityPortTable = _PortSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 2)
)
if mibBuilder.loadTexts:
    portSecurityPortTable.setStatus("mandatory")
_PortSecurityPortEntry_Object = MibTableRow
portSecurityPortEntry = _PortSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 2, 1)
)
portSecurityPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portSecurityPortEntry.setStatus("mandatory")
_PortSecurityPortState_Type = EnabledStatus
_PortSecurityPortState_Object = MibTableColumn
portSecurityPortState = _PortSecurityPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 2, 1, 1),
    _PortSecurityPortState_Type()
)
portSecurityPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortState.setStatus("mandatory")
_PortSecurityPortLearnState_Type = EnabledStatus
_PortSecurityPortLearnState_Object = MibTableColumn
portSecurityPortLearnState = _PortSecurityPortLearnState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 2, 1, 2),
    _PortSecurityPortLearnState_Type()
)
portSecurityPortLearnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortLearnState.setStatus("mandatory")
_PortSecurityPortCount_Type = Integer32
_PortSecurityPortCount_Object = MibTableColumn
portSecurityPortCount = _PortSecurityPortCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 2, 1, 3),
    _PortSecurityPortCount_Type()
)
portSecurityPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityPortCount.setStatus("mandatory")
_PortSecurityMacFreeze_Type = PortList
_PortSecurityMacFreeze_Object = MibScalar
portSecurityMacFreeze = _PortSecurityMacFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 4, 3),
    _PortSecurityMacFreeze_Type()
)
portSecurityMacFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMacFreeze.setStatus("mandatory")
_VlanTrunkSetup_ObjectIdentity = ObjectIdentity
vlanTrunkSetup = _VlanTrunkSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 5)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 5, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("mandatory")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 5, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("mandatory")
_VlanTrunkPortState_Type = EnabledStatus
_VlanTrunkPortState_Object = MibTableColumn
vlanTrunkPortState = _VlanTrunkPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 5, 1, 1, 1),
    _VlanTrunkPortState_Type()
)
vlanTrunkPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortState.setStatus("mandatory")
_CtlProtTransSetup_ObjectIdentity = ObjectIdentity
ctlProtTransSetup = _CtlProtTransSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 6)
)
_CtlProtTransState_Type = EnabledStatus
_CtlProtTransState_Object = MibScalar
ctlProtTransState = _CtlProtTransState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 6, 1),
    _CtlProtTransState_Type()
)
ctlProtTransState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransState.setStatus("mandatory")
_CtlProtTransTunnelPortTable_Object = MibTable
ctlProtTransTunnelPortTable = _CtlProtTransTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 6, 2)
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortTable.setStatus("mandatory")
_CtlProtTransTunnelPortEntry_Object = MibTableRow
ctlProtTransTunnelPortEntry = _CtlProtTransTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 6, 2, 1)
)
ctlProtTransTunnelPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    ctlProtTransTunnelPortEntry.setStatus("mandatory")


class _CtlProtTransTunnelMode_Type(Integer32):
    """Custom type ctlProtTransTunnelMode based on Integer32"""
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
        *(("peer", 0),
          ("tunnel", 1),
          ("discard", 2),
          ("network", 3))
    )


_CtlProtTransTunnelMode_Type.__name__ = "Integer32"
_CtlProtTransTunnelMode_Object = MibTableColumn
ctlProtTransTunnelMode = _CtlProtTransTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 6, 2, 1, 1),
    _CtlProtTransTunnelMode_Type()
)
ctlProtTransTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctlProtTransTunnelMode.setStatus("mandatory")
_VlanStackSetup_ObjectIdentity = ObjectIdentity
vlanStackSetup = _VlanStackSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7)
)
_VlanStackState_Type = EnabledStatus
_VlanStackState_Object = MibScalar
vlanStackState = _VlanStackState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 1),
    _VlanStackState_Type()
)
vlanStackState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackState.setStatus("mandatory")
_VlanStackTpid_Type = Integer32
_VlanStackTpid_Object = MibScalar
vlanStackTpid = _VlanStackTpid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 2),
    _VlanStackTpid_Type()
)
vlanStackTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackTpid.setStatus("mandatory")
_VlanStackPortTable_Object = MibTable
vlanStackPortTable = _VlanStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 3)
)
if mibBuilder.loadTexts:
    vlanStackPortTable.setStatus("mandatory")
_VlanStackPortEntry_Object = MibTableRow
vlanStackPortEntry = _VlanStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 3, 1)
)
vlanStackPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    vlanStackPortEntry.setStatus("mandatory")


class _VlanStackPortMode_Type(Integer32):
    """Custom type vlanStackPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("access", 2),
          ("tunnel", 3))
    )


_VlanStackPortMode_Type.__name__ = "Integer32"
_VlanStackPortMode_Object = MibTableColumn
vlanStackPortMode = _VlanStackPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 3, 1, 1),
    _VlanStackPortMode_Type()
)
vlanStackPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortMode.setStatus("mandatory")
_VlanStackPortVid_Type = Integer32
_VlanStackPortVid_Object = MibTableColumn
vlanStackPortVid = _VlanStackPortVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 3, 1, 2),
    _VlanStackPortVid_Type()
)
vlanStackPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortVid.setStatus("mandatory")


class _VlanStackPortPrio_Type(Integer32):
    """Custom type vlanStackPortPrio based on Integer32"""
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
        *(("prioriry-0", 0),
          ("prioriry-1", 1),
          ("prioriry-2", 2),
          ("prioriry-3", 3),
          ("prioriry-4", 4),
          ("prioriry-5", 5),
          ("prioriry-6", 6),
          ("prioriry-7", 7))
    )


_VlanStackPortPrio_Type.__name__ = "Integer32"
_VlanStackPortPrio_Object = MibTableColumn
vlanStackPortPrio = _VlanStackPortPrio_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 7, 3, 1, 3),
    _VlanStackPortPrio_Type()
)
vlanStackPortPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStackPortPrio.setStatus("mandatory")
_Radius8021xSetup_ObjectIdentity = ObjectIdentity
radius8021xSetup = _Radius8021xSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8)
)
_RadiusLoginPrecedence_Type = Integer32
_RadiusLoginPrecedence_Object = MibScalar
radiusLoginPrecedence = _RadiusLoginPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 1),
    _RadiusLoginPrecedence_Type()
)
radiusLoginPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginPrecedence.setStatus("mandatory")
_RadiusAnd8021xServer_ObjectIdentity = ObjectIdentity
radiusAnd8021xServer = _RadiusAnd8021xServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 2)
)
_RadiusIpAddr_Type = IpAddress
_RadiusIpAddr_Object = MibScalar
radiusIpAddr = _RadiusIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 2, 1),
    _RadiusIpAddr_Type()
)
radiusIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusIpAddr.setStatus("mandatory")
_RadiusUdpPort_Type = Integer32
_RadiusUdpPort_Object = MibScalar
radiusUdpPort = _RadiusUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 2, 2),
    _RadiusUdpPort_Type()
)
radiusUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusUdpPort.setStatus("mandatory")
_RadiusSharedSecret_Type = DisplayString
_RadiusSharedSecret_Object = MibScalar
radiusSharedSecret = _RadiusSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 2, 3),
    _RadiusSharedSecret_Type()
)
radiusSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusSharedSecret.setStatus("mandatory")
_PortAuthState_Type = EnabledStatus
_PortAuthState_Object = MibScalar
portAuthState = _PortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 3),
    _PortAuthState_Type()
)
portAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthState.setStatus("mandatory")
_PortAuthTable_Object = MibTable
portAuthTable = _PortAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 4)
)
if mibBuilder.loadTexts:
    portAuthTable.setStatus("mandatory")
_PortAuthEntry_Object = MibTableRow
portAuthEntry = _PortAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 4, 1)
)
portAuthEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portAuthEntry.setStatus("mandatory")
_PortAuthEntryState_Type = EnabledStatus
_PortAuthEntryState_Object = MibTableColumn
portAuthEntryState = _PortAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 4, 1, 1),
    _PortAuthEntryState_Type()
)
portAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAuthEntryState.setStatus("mandatory")
_PortReAuthEntryState_Type = EnabledStatus
_PortReAuthEntryState_Object = MibTableColumn
portReAuthEntryState = _PortReAuthEntryState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 4, 1, 2),
    _PortReAuthEntryState_Type()
)
portReAuthEntryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryState.setStatus("mandatory")
_PortReAuthEntryTimer_Type = Integer32
_PortReAuthEntryTimer_Object = MibTableColumn
portReAuthEntryTimer = _PortReAuthEntryTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 8, 4, 1, 3),
    _PortReAuthEntryTimer_Type()
)
portReAuthEntryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portReAuthEntryTimer.setStatus("mandatory")
_HwMonitorInfo_ObjectIdentity = ObjectIdentity
hwMonitorInfo = _HwMonitorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9)
)
_FanRpmTable_Object = MibTable
fanRpmTable = _FanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1)
)
if mibBuilder.loadTexts:
    fanRpmTable.setStatus("current")
_FanRpmEntry_Object = MibTableRow
fanRpmEntry = _FanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1)
)
fanRpmEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "fanRpmIndex"),
)
if mibBuilder.loadTexts:
    fanRpmEntry.setStatus("current")
_FanRpmIndex_Type = Integer32
_FanRpmIndex_Object = MibTableColumn
fanRpmIndex = _FanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1, 1),
    _FanRpmIndex_Type()
)
fanRpmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmIndex.setStatus("current")
_FanRpmCurValue_Type = Integer32
_FanRpmCurValue_Object = MibTableColumn
fanRpmCurValue = _FanRpmCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1, 2),
    _FanRpmCurValue_Type()
)
fanRpmCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmCurValue.setStatus("current")
_FanRpmMaxValue_Type = Integer32
_FanRpmMaxValue_Object = MibTableColumn
fanRpmMaxValue = _FanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1, 3),
    _FanRpmMaxValue_Type()
)
fanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMaxValue.setStatus("current")
_FanRpmMinValue_Type = Integer32
_FanRpmMinValue_Object = MibTableColumn
fanRpmMinValue = _FanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1, 4),
    _FanRpmMinValue_Type()
)
fanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMinValue.setStatus("current")
_FanRpmLowThresh_Type = Integer32
_FanRpmLowThresh_Object = MibTableColumn
fanRpmLowThresh = _FanRpmLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1, 5),
    _FanRpmLowThresh_Type()
)
fanRpmLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmLowThresh.setStatus("current")
_FanRpmDescr_Type = DisplayString
_FanRpmDescr_Object = MibTableColumn
fanRpmDescr = _FanRpmDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 1, 1, 6),
    _FanRpmDescr_Type()
)
fanRpmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmDescr.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1)
)
tempEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")


class _TempIndex_Type(Integer32):
    """Custom type tempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("cpu", 2),
          ("phy", 3))
    )


_TempIndex_Type.__name__ = "Integer32"
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
_TempCurValue_Type = Integer32
_TempCurValue_Object = MibTableColumn
tempCurValue = _TempCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1, 2),
    _TempCurValue_Type()
)
tempCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCurValue.setStatus("current")
_TempMaxValue_Type = Integer32
_TempMaxValue_Object = MibTableColumn
tempMaxValue = _TempMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1, 3),
    _TempMaxValue_Type()
)
tempMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMaxValue.setStatus("current")
_TempMinValue_Type = Integer32
_TempMinValue_Object = MibTableColumn
tempMinValue = _TempMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1, 4),
    _TempMinValue_Type()
)
tempMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempMinValue.setStatus("current")
_TempHighThresh_Type = Integer32
_TempHighThresh_Object = MibTableColumn
tempHighThresh = _TempHighThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1, 5),
    _TempHighThresh_Type()
)
tempHighThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighThresh.setStatus("current")
_TempDescr_Type = DisplayString
_TempDescr_Object = MibTableColumn
tempDescr = _TempDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 2, 1, 6),
    _TempDescr_Type()
)
tempDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempDescr.setStatus("current")
_VoltageTable_Object = MibTable
voltageTable = _VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3)
)
if mibBuilder.loadTexts:
    voltageTable.setStatus("current")
_VoltageEntry_Object = MibTableRow
voltageEntry = _VoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1)
)
voltageEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "voltageIndex"),
)
if mibBuilder.loadTexts:
    voltageEntry.setStatus("current")
_VoltageIndex_Type = Integer32
_VoltageIndex_Object = MibTableColumn
voltageIndex = _VoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 1),
    _VoltageIndex_Type()
)
voltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageIndex.setStatus("current")
_VoltageCurValue_Type = Integer32
_VoltageCurValue_Object = MibTableColumn
voltageCurValue = _VoltageCurValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 2),
    _VoltageCurValue_Type()
)
voltageCurValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageCurValue.setStatus("current")
_VoltageMaxValue_Type = Integer32
_VoltageMaxValue_Object = MibTableColumn
voltageMaxValue = _VoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 3),
    _VoltageMaxValue_Type()
)
voltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMaxValue.setStatus("current")
_VoltageMinValue_Type = Integer32
_VoltageMinValue_Object = MibTableColumn
voltageMinValue = _VoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 4),
    _VoltageMinValue_Type()
)
voltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageMinValue.setStatus("current")
_VoltageNominalValue_Type = Integer32
_VoltageNominalValue_Object = MibTableColumn
voltageNominalValue = _VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 5),
    _VoltageNominalValue_Type()
)
voltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageNominalValue.setStatus("current")
_VoltageLowThresh_Type = Integer32
_VoltageLowThresh_Object = MibTableColumn
voltageLowThresh = _VoltageLowThresh_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 6),
    _VoltageLowThresh_Type()
)
voltageLowThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageLowThresh.setStatus("current")
_VoltageDescr_Type = DisplayString
_VoltageDescr_Object = MibTableColumn
voltageDescr = _VoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 9, 3, 1, 7),
    _VoltageDescr_Type()
)
voltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voltageDescr.setStatus("current")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10)
)
_SnmpGetCommunity_Type = DisplayString
_SnmpGetCommunity_Object = MibScalar
snmpGetCommunity = _SnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 1),
    _SnmpGetCommunity_Type()
)
snmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpGetCommunity.setStatus("mandatory")
_SnmpSetCommunity_Type = DisplayString
_SnmpSetCommunity_Object = MibScalar
snmpSetCommunity = _SnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 2),
    _SnmpSetCommunity_Type()
)
snmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpSetCommunity.setStatus("mandatory")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 3),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")
_SnmpTrapDestTable_Object = MibTable
snmpTrapDestTable = _SnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 4)
)
if mibBuilder.loadTexts:
    snmpTrapDestTable.setStatus("mandatory")
_SnmpTrapDestEntry_Object = MibTableRow
snmpTrapDestEntry = _SnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 4, 1)
)
snmpTrapDestEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "snmpTrapDestIP"),
)
if mibBuilder.loadTexts:
    snmpTrapDestEntry.setStatus("mandatory")
_SnmpTrapDestIP_Type = IpAddress
_SnmpTrapDestIP_Object = MibTableColumn
snmpTrapDestIP = _SnmpTrapDestIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 4, 1, 1),
    _SnmpTrapDestIP_Type()
)
snmpTrapDestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestIP.setStatus("mandatory")
_SnmpTrapDestRowStatus_Type = RowStatus
_SnmpTrapDestRowStatus_Object = MibTableColumn
snmpTrapDestRowStatus = _SnmpTrapDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 10, 4, 1, 2),
    _SnmpTrapDestRowStatus_Type()
)
snmpTrapDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapDestRowStatus.setStatus("mandatory")
_DateTimeServerSetup_ObjectIdentity = ObjectIdentity
dateTimeServerSetup = _DateTimeServerSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11)
)


class _DateTimeServerType_Type(Integer32):
    """Custom type dateTimeServerType based on Integer32"""
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
          ("daytime", 2),
          ("time", 3),
          ("ntp", 4))
    )


_DateTimeServerType_Type.__name__ = "Integer32"
_DateTimeServerType_Object = MibScalar
dateTimeServerType = _DateTimeServerType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 1),
    _DateTimeServerType_Type()
)
dateTimeServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerType.setStatus("mandatory")
_DateTimeServerIP_Type = IpAddress
_DateTimeServerIP_Object = MibScalar
dateTimeServerIP = _DateTimeServerIP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 2),
    _DateTimeServerIP_Type()
)
dateTimeServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeServerIP.setStatus("mandatory")
_DateTimeZone_Type = Integer32
_DateTimeZone_Object = MibScalar
dateTimeZone = _DateTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 3),
    _DateTimeZone_Type()
)
dateTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeZone.setStatus("mandatory")
_DateTimeNewDateYear_Type = Integer32
_DateTimeNewDateYear_Object = MibScalar
dateTimeNewDateYear = _DateTimeNewDateYear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 4),
    _DateTimeNewDateYear_Type()
)
dateTimeNewDateYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateYear.setStatus("mandatory")
_DateTimeNewDateMonth_Type = Integer32
_DateTimeNewDateMonth_Object = MibScalar
dateTimeNewDateMonth = _DateTimeNewDateMonth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 5),
    _DateTimeNewDateMonth_Type()
)
dateTimeNewDateMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateMonth.setStatus("mandatory")
_DateTimeNewDateDay_Type = Integer32
_DateTimeNewDateDay_Object = MibScalar
dateTimeNewDateDay = _DateTimeNewDateDay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 6),
    _DateTimeNewDateDay_Type()
)
dateTimeNewDateDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewDateDay.setStatus("mandatory")
_DateTimeNewTimeHour_Type = Integer32
_DateTimeNewTimeHour_Object = MibScalar
dateTimeNewTimeHour = _DateTimeNewTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 7),
    _DateTimeNewTimeHour_Type()
)
dateTimeNewTimeHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeHour.setStatus("mandatory")
_DateTimeNewTimeMinute_Type = Integer32
_DateTimeNewTimeMinute_Object = MibScalar
dateTimeNewTimeMinute = _DateTimeNewTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 8),
    _DateTimeNewTimeMinute_Type()
)
dateTimeNewTimeMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeMinute.setStatus("mandatory")
_DateTimeNewTimeSecond_Type = Integer32
_DateTimeNewTimeSecond_Object = MibScalar
dateTimeNewTimeSecond = _DateTimeNewTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 11, 9),
    _DateTimeNewTimeSecond_Type()
)
dateTimeNewTimeSecond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dateTimeNewTimeSecond.setStatus("mandatory")
_SysMgmt_ObjectIdentity = ObjectIdentity
sysMgmt = _SysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12)
)


class _SysMgmtConfigSave_Type(Integer32):
    """Custom type sysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtConfigSave_Type.__name__ = "Integer32"
_SysMgmtConfigSave_Object = MibScalar
sysMgmtConfigSave = _SysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12, 1),
    _SysMgmtConfigSave_Type()
)
sysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtConfigSave.setStatus("mandatory")


class _SysMgmtBootupConfig_Type(Integer32):
    """Custom type sysMgmtBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config-1", 1),
          ("config-2", 2))
    )


_SysMgmtBootupConfig_Type.__name__ = "Integer32"
_SysMgmtBootupConfig_Object = MibScalar
sysMgmtBootupConfig = _SysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12, 2),
    _SysMgmtBootupConfig_Type()
)
sysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtBootupConfig.setStatus("mandatory")


class _SysMgmtReboot_Type(Integer32):
    """Custom type sysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_SysMgmtReboot_Type.__name__ = "Integer32"
_SysMgmtReboot_Object = MibScalar
sysMgmtReboot = _SysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12, 3),
    _SysMgmtReboot_Type()
)
sysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtReboot.setStatus("mandatory")


class _SysMgmtDefaultConfig_Type(Integer32):
    """Custom type sysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reset-to-default", 1))
    )


_SysMgmtDefaultConfig_Type.__name__ = "Integer32"
_SysMgmtDefaultConfig_Object = MibScalar
sysMgmtDefaultConfig = _SysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12, 4),
    _SysMgmtDefaultConfig_Type()
)
sysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMgmtDefaultConfig.setStatus("mandatory")


class _SysMgmtLastActionStatus_Type(Integer32):
    """Custom type sysMgmtLastActionStatus based on Integer32"""
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
          ("success", 1),
          ("fail", 2))
    )


_SysMgmtLastActionStatus_Type.__name__ = "Integer32"
_SysMgmtLastActionStatus_Object = MibScalar
sysMgmtLastActionStatus = _SysMgmtLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12, 5),
    _SysMgmtLastActionStatus_Type()
)
sysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtLastActionStatus.setStatus("mandatory")


class _SysMgmtSystemStatus_Type(Bits):
    """Custom type sysMgmtSystemStatus based on Bits"""
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysTemperatureError", 1),
          ("sysFanRPMError", 2),
          ("sysVoltageRangeError", 3))
    )

_SysMgmtSystemStatus_Type.__name__ = "Bits"
_SysMgmtSystemStatus_Object = MibScalar
sysMgmtSystemStatus = _SysMgmtSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 12, 6),
    _SysMgmtSystemStatus_Type()
)
sysMgmtSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtSystemStatus.setStatus("mandatory")
_Layer2Setup_ObjectIdentity = ObjectIdentity
layer2Setup = _Layer2Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 13)
)


class _VlanTypeSetup_Type(Integer32):
    """Custom type vlanTypeSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1Q", 1),
          ("port-based", 2))
    )


_VlanTypeSetup_Type.__name__ = "Integer32"
_VlanTypeSetup_Object = MibScalar
vlanTypeSetup = _VlanTypeSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 13, 1),
    _VlanTypeSetup_Type()
)
vlanTypeSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTypeSetup.setStatus("mandatory")
_IgmpSnoopingStateSetup_Type = EnabledStatus
_IgmpSnoopingStateSetup_Object = MibScalar
igmpSnoopingStateSetup = _IgmpSnoopingStateSetup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 13, 2),
    _IgmpSnoopingStateSetup_Type()
)
igmpSnoopingStateSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopingStateSetup.setStatus("mandatory")
_TagVlanPortIsolationState_Type = EnabledStatus
_TagVlanPortIsolationState_Object = MibScalar
tagVlanPortIsolationState = _TagVlanPortIsolationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 13, 3),
    _TagVlanPortIsolationState_Type()
)
tagVlanPortIsolationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tagVlanPortIsolationState.setStatus("mandatory")
_StpState_Type = EnabledStatus
_StpState_Object = MibScalar
stpState = _StpState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 13, 4),
    _StpState_Type()
)
stpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpState.setStatus("mandatory")
_IpSetup_ObjectIdentity = ObjectIdentity
ipSetup = _IpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14)
)
_DnsIpAddress_Type = IpAddress
_DnsIpAddress_Object = MibScalar
dnsIpAddress = _DnsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 1),
    _DnsIpAddress_Type()
)
dnsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpAddress.setStatus("mandatory")


class _DefaultMgmt_Type(Integer32):
    """Custom type defaultMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-band", 0),
          ("out-of-band", 1))
    )


_DefaultMgmt_Type.__name__ = "Integer32"
_DefaultMgmt_Object = MibScalar
defaultMgmt = _DefaultMgmt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 2),
    _DefaultMgmt_Type()
)
defaultMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultMgmt.setStatus("mandatory")
_InbandIpSetup_ObjectIdentity = ObjectIdentity
inbandIpSetup = _InbandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 3)
)


class _InbandIpType_Type(Integer32):
    """Custom type inbandIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-client", 0),
          ("static-ip", 1))
    )


_InbandIpType_Type.__name__ = "Integer32"
_InbandIpType_Object = MibScalar
inbandIpType = _InbandIpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 3, 1),
    _InbandIpType_Type()
)
inbandIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandIpType.setStatus("mandatory")
_InbandVid_Type = Integer32
_InbandVid_Object = MibScalar
inbandVid = _InbandVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 3, 2),
    _InbandVid_Type()
)
inbandVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandVid.setStatus("mandatory")
_InbandStaticIp_Type = IpAddress
_InbandStaticIp_Object = MibScalar
inbandStaticIp = _InbandStaticIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 3, 3),
    _InbandStaticIp_Type()
)
inbandStaticIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticIp.setStatus("mandatory")
_InbandStaticSubnetMask_Type = IpAddress
_InbandStaticSubnetMask_Object = MibScalar
inbandStaticSubnetMask = _InbandStaticSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 3, 4),
    _InbandStaticSubnetMask_Type()
)
inbandStaticSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticSubnetMask.setStatus("mandatory")
_InbandStaticGateway_Type = IpAddress
_InbandStaticGateway_Object = MibScalar
inbandStaticGateway = _InbandStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 3, 5),
    _InbandStaticGateway_Type()
)
inbandStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandStaticGateway.setStatus("mandatory")
_OutOfBandIpSetup_ObjectIdentity = ObjectIdentity
outOfBandIpSetup = _OutOfBandIpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 4)
)
_OutOfBandIp_Type = IpAddress
_OutOfBandIp_Object = MibScalar
outOfBandIp = _OutOfBandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 4, 1),
    _OutOfBandIp_Type()
)
outOfBandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandIp.setStatus("mandatory")
_OutOfBandSubnetMask_Type = IpAddress
_OutOfBandSubnetMask_Object = MibScalar
outOfBandSubnetMask = _OutOfBandSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 4, 2),
    _OutOfBandSubnetMask_Type()
)
outOfBandSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandSubnetMask.setStatus("mandatory")
_OutOfBandGateway_Type = IpAddress
_OutOfBandGateway_Object = MibScalar
outOfBandGateway = _OutOfBandGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 4, 3),
    _OutOfBandGateway_Type()
)
outOfBandGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    outOfBandGateway.setStatus("mandatory")
_MaxNumOfInbandIp_Type = Integer32
_MaxNumOfInbandIp_Object = MibScalar
maxNumOfInbandIp = _MaxNumOfInbandIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 5),
    _MaxNumOfInbandIp_Type()
)
maxNumOfInbandIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumOfInbandIp.setStatus("mandatory")
_InbandIpTable_Object = MibTable
inbandIpTable = _InbandIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6)
)
if mibBuilder.loadTexts:
    inbandIpTable.setStatus("mandatory")
_InbandIpEntry_Object = MibTableRow
inbandIpEntry = _InbandIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1)
)
inbandIpEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "inbandEntryIp"),
    (0, "ZYXEL-ES3124PWR-MIB", "inbandEntryVid"),
)
if mibBuilder.loadTexts:
    inbandIpEntry.setStatus("mandatory")
_InbandEntryIp_Type = IpAddress
_InbandEntryIp_Object = MibTableColumn
inbandEntryIp = _InbandEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1, 1),
    _InbandEntryIp_Type()
)
inbandEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryIp.setStatus("mandatory")
_InbandEntrySubnetMask_Type = IpAddress
_InbandEntrySubnetMask_Object = MibTableColumn
inbandEntrySubnetMask = _InbandEntrySubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1, 2),
    _InbandEntrySubnetMask_Type()
)
inbandEntrySubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntrySubnetMask.setStatus("mandatory")
_InbandEntryGateway_Type = IpAddress
_InbandEntryGateway_Object = MibTableColumn
inbandEntryGateway = _InbandEntryGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1, 3),
    _InbandEntryGateway_Type()
)
inbandEntryGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryGateway.setStatus("mandatory")
_InbandEntryVid_Type = Integer32
_InbandEntryVid_Object = MibTableColumn
inbandEntryVid = _InbandEntryVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1, 4),
    _InbandEntryVid_Type()
)
inbandEntryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryVid.setStatus("mandatory")
_InbandEntryManageable_Type = EnabledStatus
_InbandEntryManageable_Object = MibTableColumn
inbandEntryManageable = _InbandEntryManageable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1, 5),
    _InbandEntryManageable_Type()
)
inbandEntryManageable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inbandEntryManageable.setStatus("mandatory")
_InbandEntryRowStatus_Type = RowStatus
_InbandEntryRowStatus_Object = MibTableColumn
inbandEntryRowStatus = _InbandEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 14, 6, 1, 6),
    _InbandEntryRowStatus_Type()
)
inbandEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inbandEntryRowStatus.setStatus("mandatory")
_FilterSetup_ObjectIdentity = ObjectIdentity
filterSetup = _FilterSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15)
)
_FilterTable_Object = MibTable
filterTable = _FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1)
)
if mibBuilder.loadTexts:
    filterTable.setStatus("mandatory")
_FilterEntry_Object = MibTableRow
filterEntry = _FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1, 1)
)
filterEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "filterMacAddr"),
    (0, "ZYXEL-ES3124PWR-MIB", "filterVid"),
)
if mibBuilder.loadTexts:
    filterEntry.setStatus("mandatory")
_FilterName_Type = DisplayString
_FilterName_Object = MibTableColumn
filterName = _FilterName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1, 1, 1),
    _FilterName_Type()
)
filterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterName.setStatus("mandatory")


class _FilterActionState_Type(Integer32):
    """Custom type filterActionState based on Integer32"""
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
        *(("none", 0),
          ("discard-source", 1),
          ("discard-destination", 2),
          ("both", 3))
    )


_FilterActionState_Type.__name__ = "Integer32"
_FilterActionState_Object = MibTableColumn
filterActionState = _FilterActionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1, 1, 2),
    _FilterActionState_Type()
)
filterActionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterActionState.setStatus("mandatory")
_FilterMacAddr_Type = PhysAddress
_FilterMacAddr_Object = MibTableColumn
filterMacAddr = _FilterMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1, 1, 3),
    _FilterMacAddr_Type()
)
filterMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterMacAddr.setStatus("mandatory")
_FilterVid_Type = Integer32
_FilterVid_Object = MibTableColumn
filterVid = _FilterVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1, 1, 4),
    _FilterVid_Type()
)
filterVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterVid.setStatus("mandatory")
_FilterRowStatus_Type = RowStatus
_FilterRowStatus_Object = MibTableColumn
filterRowStatus = _FilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 15, 1, 1, 5),
    _FilterRowStatus_Type()
)
filterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterRowStatus.setStatus("mandatory")
_MirrorSetup_ObjectIdentity = ObjectIdentity
mirrorSetup = _MirrorSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16)
)
_MirrorState_Type = EnabledStatus
_MirrorState_Object = MibScalar
mirrorState = _MirrorState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16, 1),
    _MirrorState_Type()
)
mirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorState.setStatus("mandatory")
_MirrorMonitorPort_Type = Integer32
_MirrorMonitorPort_Object = MibScalar
mirrorMonitorPort = _MirrorMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16, 2),
    _MirrorMonitorPort_Type()
)
mirrorMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMonitorPort.setStatus("mandatory")
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16, 3)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("mandatory")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16, 3, 1)
)
mirrorEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("mandatory")
_MirrorMirroredState_Type = EnabledStatus
_MirrorMirroredState_Object = MibTableColumn
mirrorMirroredState = _MirrorMirroredState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16, 3, 1, 1),
    _MirrorMirroredState_Type()
)
mirrorMirroredState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorMirroredState.setStatus("mandatory")


class _MirrorDirection_Type(Integer32):
    """Custom type mirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 0),
          ("egress", 1),
          ("both", 2))
    )


_MirrorDirection_Type.__name__ = "Integer32"
_MirrorDirection_Object = MibTableColumn
mirrorDirection = _MirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 16, 3, 1, 2),
    _MirrorDirection_Type()
)
mirrorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirrorDirection.setStatus("mandatory")
_AggrSetup_ObjectIdentity = ObjectIdentity
aggrSetup = _AggrSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17)
)
_AggrState_Type = EnabledStatus
_AggrState_Object = MibScalar
aggrState = _AggrState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 1),
    _AggrState_Type()
)
aggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrState.setStatus("mandatory")
_AggrSystemPriority_Type = Integer32
_AggrSystemPriority_Object = MibScalar
aggrSystemPriority = _AggrSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 2),
    _AggrSystemPriority_Type()
)
aggrSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrSystemPriority.setStatus("mandatory")
_AggrGroupTable_Object = MibTable
aggrGroupTable = _AggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 3)
)
if mibBuilder.loadTexts:
    aggrGroupTable.setStatus("mandatory")
_AggrGroupEntry_Object = MibTableRow
aggrGroupEntry = _AggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 3, 1)
)
aggrGroupEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "aggrGroupIndex"),
)
if mibBuilder.loadTexts:
    aggrGroupEntry.setStatus("mandatory")
_AggrGroupIndex_Type = Integer32
_AggrGroupIndex_Object = MibTableColumn
aggrGroupIndex = _AggrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 3, 1, 1),
    _AggrGroupIndex_Type()
)
aggrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aggrGroupIndex.setStatus("mandatory")
_AggrGroupState_Type = EnabledStatus
_AggrGroupState_Object = MibTableColumn
aggrGroupState = _AggrGroupState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 3, 1, 2),
    _AggrGroupState_Type()
)
aggrGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupState.setStatus("mandatory")
_AggrGroupDynamicState_Type = EnabledStatus
_AggrGroupDynamicState_Object = MibTableColumn
aggrGroupDynamicState = _AggrGroupDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 3, 1, 3),
    _AggrGroupDynamicState_Type()
)
aggrGroupDynamicState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrGroupDynamicState.setStatus("mandatory")
_AggrPortTable_Object = MibTable
aggrPortTable = _AggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 4)
)
if mibBuilder.loadTexts:
    aggrPortTable.setStatus("mandatory")
_AggrPortEntry_Object = MibTableRow
aggrPortEntry = _AggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 4, 1)
)
aggrPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    aggrPortEntry.setStatus("mandatory")


class _AggrPortGroup_Type(Integer32):
    """Custom type aggrPortGroup based on Integer32"""
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
        *(("none", 0),
          ("t1", 1),
          ("t2", 2),
          ("t3", 3),
          ("t4", 4),
          ("t5", 5),
          ("t6", 6))
    )


_AggrPortGroup_Type.__name__ = "Integer32"
_AggrPortGroup_Object = MibTableColumn
aggrPortGroup = _AggrPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 4, 1, 1),
    _AggrPortGroup_Type()
)
aggrPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortGroup.setStatus("mandatory")
_AggrPortDynamicStateTimeout_Type = Integer32
_AggrPortDynamicStateTimeout_Object = MibTableColumn
aggrPortDynamicStateTimeout = _AggrPortDynamicStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 17, 4, 1, 2),
    _AggrPortDynamicStateTimeout_Type()
)
aggrPortDynamicStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aggrPortDynamicStateTimeout.setStatus("mandatory")
_AccessCtlSetup_ObjectIdentity = ObjectIdentity
accessCtlSetup = _AccessCtlSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18)
)
_AccessCtlTable_Object = MibTable
accessCtlTable = _AccessCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 1)
)
if mibBuilder.loadTexts:
    accessCtlTable.setStatus("mandatory")
_AccessCtlEntry_Object = MibTableRow
accessCtlEntry = _AccessCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 1, 1)
)
accessCtlEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "accessCtlService"),
)
if mibBuilder.loadTexts:
    accessCtlEntry.setStatus("mandatory")


class _AccessCtlService_Type(Integer32):
    """Custom type accessCtlService based on Integer32"""
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
        *(("telnet", 1),
          ("ssh", 2),
          ("ftp", 3),
          ("http", 4),
          ("https", 5),
          ("icmp", 6),
          ("snmp", 7))
    )


_AccessCtlService_Type.__name__ = "Integer32"
_AccessCtlService_Object = MibTableColumn
accessCtlService = _AccessCtlService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 1, 1, 1),
    _AccessCtlService_Type()
)
accessCtlService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessCtlService.setStatus("mandatory")
_AccessCtlEnable_Type = EnabledStatus
_AccessCtlEnable_Object = MibTableColumn
accessCtlEnable = _AccessCtlEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 1, 1, 2),
    _AccessCtlEnable_Type()
)
accessCtlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlEnable.setStatus("mandatory")
_AccessCtlServicePort_Type = Integer32
_AccessCtlServicePort_Object = MibTableColumn
accessCtlServicePort = _AccessCtlServicePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 1, 1, 3),
    _AccessCtlServicePort_Type()
)
accessCtlServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlServicePort.setStatus("mandatory")
_AccessCtlTimeout_Type = Integer32
_AccessCtlTimeout_Object = MibTableColumn
accessCtlTimeout = _AccessCtlTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 1, 1, 4),
    _AccessCtlTimeout_Type()
)
accessCtlTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessCtlTimeout.setStatus("mandatory")
_SecuredClientTable_Object = MibTable
securedClientTable = _SecuredClientTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2)
)
if mibBuilder.loadTexts:
    securedClientTable.setStatus("mandatory")
_SecuredClientEntry_Object = MibTableRow
securedClientEntry = _SecuredClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2, 1)
)
securedClientEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "securedClientIndex"),
)
if mibBuilder.loadTexts:
    securedClientEntry.setStatus("mandatory")
_SecuredClientIndex_Type = Integer32
_SecuredClientIndex_Object = MibTableColumn
securedClientIndex = _SecuredClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2, 1, 1),
    _SecuredClientIndex_Type()
)
securedClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securedClientIndex.setStatus("mandatory")
_SecuredClientEnable_Type = EnabledStatus
_SecuredClientEnable_Object = MibTableColumn
securedClientEnable = _SecuredClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2, 1, 2),
    _SecuredClientEnable_Type()
)
securedClientEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEnable.setStatus("mandatory")
_SecuredClientStartIp_Type = IpAddress
_SecuredClientStartIp_Object = MibTableColumn
securedClientStartIp = _SecuredClientStartIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2, 1, 3),
    _SecuredClientStartIp_Type()
)
securedClientStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientStartIp.setStatus("mandatory")
_SecuredClientEndIp_Type = IpAddress
_SecuredClientEndIp_Object = MibTableColumn
securedClientEndIp = _SecuredClientEndIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2, 1, 4),
    _SecuredClientEndIp_Type()
)
securedClientEndIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientEndIp.setStatus("mandatory")


class _SecuredClientService_Type(Bits):
    """Custom type securedClientService based on Bits"""
    namedValues = NamedValues(
        *(("telnet", 0),
          ("ftp", 1),
          ("http", 2),
          ("icmp", 3),
          ("snmp", 4),
          ("ssh", 5),
          ("https", 6))
    )

_SecuredClientService_Type.__name__ = "Bits"
_SecuredClientService_Object = MibTableColumn
securedClientService = _SecuredClientService_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 18, 2, 1, 5),
    _SecuredClientService_Type()
)
securedClientService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedClientService.setStatus("mandatory")
_QueuingMethodSetup_ObjectIdentity = ObjectIdentity
queuingMethodSetup = _QueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 19)
)


class _QueuingMethodType_Type(Integer32):
    """Custom type queuingMethodType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("strictly-priority", 0),
          ("weighted-fair-scheduling", 1))
    )


_QueuingMethodType_Type.__name__ = "Integer32"
_QueuingMethodType_Object = MibScalar
queuingMethodType = _QueuingMethodType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 19, 1),
    _QueuingMethodType_Type()
)
queuingMethodType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMethodType.setStatus("mandatory")
_PortQueuingMethodTable_Object = MibTable
portQueuingMethodTable = _PortQueuingMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 19, 2)
)
if mibBuilder.loadTexts:
    portQueuingMethodTable.setStatus("mandatory")
_PortQueuingMethodEntry_Object = MibTableRow
portQueuingMethodEntry = _PortQueuingMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 19, 2, 1)
)
portQueuingMethodEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "portQueuingMethodQueue"),
)
if mibBuilder.loadTexts:
    portQueuingMethodEntry.setStatus("mandatory")
_PortQueuingMethodQueue_Type = Integer32
_PortQueuingMethodQueue_Object = MibTableColumn
portQueuingMethodQueue = _PortQueuingMethodQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 19, 2, 1, 1),
    _PortQueuingMethodQueue_Type()
)
portQueuingMethodQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portQueuingMethodQueue.setStatus("mandatory")
_PortQueuingMethodWeight_Type = Integer32
_PortQueuingMethodWeight_Object = MibTableColumn
portQueuingMethodWeight = _PortQueuingMethodWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 19, 2, 1, 2),
    _PortQueuingMethodWeight_Type()
)
portQueuingMethodWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portQueuingMethodWeight.setStatus("mandatory")
_DhcpSetup_ObjectIdentity = ObjectIdentity
dhcpSetup = _DhcpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20)
)
_DhcpRelay_ObjectIdentity = ObjectIdentity
dhcpRelay = _DhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1)
)
_DhcpRelayEnable_Type = EnabledStatus
_DhcpRelayEnable_Object = MibScalar
dhcpRelayEnable = _DhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 1),
    _DhcpRelayEnable_Type()
)
dhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayEnable.setStatus("mandatory")
_DhcpRelayOption82Enable_Type = EnabledStatus
_DhcpRelayOption82Enable_Object = MibScalar
dhcpRelayOption82Enable = _DhcpRelayOption82Enable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 2),
    _DhcpRelayOption82Enable_Type()
)
dhcpRelayOption82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayOption82Enable.setStatus("mandatory")
_DhcpRelayInfoEnable_Type = EnabledStatus
_DhcpRelayInfoEnable_Object = MibScalar
dhcpRelayInfoEnable = _DhcpRelayInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 3),
    _DhcpRelayInfoEnable_Type()
)
dhcpRelayInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoEnable.setStatus("mandatory")
_DhcpRelayInfoData_Type = DisplayString
_DhcpRelayInfoData_Object = MibScalar
dhcpRelayInfoData = _DhcpRelayInfoData_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 4),
    _DhcpRelayInfoData_Type()
)
dhcpRelayInfoData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayInfoData.setStatus("mandatory")
_MaxNumberOfDhcpRemoteServer_Type = Integer32
_MaxNumberOfDhcpRemoteServer_Object = MibScalar
maxNumberOfDhcpRemoteServer = _MaxNumberOfDhcpRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 5),
    _MaxNumberOfDhcpRemoteServer_Type()
)
maxNumberOfDhcpRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfDhcpRemoteServer.setStatus("mandatory")
_DhcpRemoteServerTable_Object = MibTable
dhcpRemoteServerTable = _DhcpRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 6)
)
if mibBuilder.loadTexts:
    dhcpRemoteServerTable.setStatus("mandatory")
_DhcpRemoteServerEntry_Object = MibTableRow
dhcpRemoteServerEntry = _DhcpRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 6, 1)
)
dhcpRemoteServerEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "dhcpRemoteServerIp"),
)
if mibBuilder.loadTexts:
    dhcpRemoteServerEntry.setStatus("mandatory")
_DhcpRemoteServerIp_Type = IpAddress
_DhcpRemoteServerIp_Object = MibTableColumn
dhcpRemoteServerIp = _DhcpRemoteServerIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 6, 1, 1),
    _DhcpRemoteServerIp_Type()
)
dhcpRemoteServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpRemoteServerIp.setStatus("mandatory")
_DhcpRemoteServerRowStatus_Type = RowStatus
_DhcpRemoteServerRowStatus_Object = MibTableColumn
dhcpRemoteServerRowStatus = _DhcpRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 20, 1, 6, 1, 2),
    _DhcpRemoteServerRowStatus_Type()
)
dhcpRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dhcpRemoteServerRowStatus.setStatus("mandatory")
_StaticRouteSetup_ObjectIdentity = ObjectIdentity
staticRouteSetup = _StaticRouteSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21)
)
_MaxNumberOfStaticRoutes_Type = Integer32
_MaxNumberOfStaticRoutes_Object = MibScalar
maxNumberOfStaticRoutes = _MaxNumberOfStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 1),
    _MaxNumberOfStaticRoutes_Type()
)
maxNumberOfStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxNumberOfStaticRoutes.setStatus("mandatory")
_StaticRouteTable_Object = MibTable
staticRouteTable = _StaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2)
)
if mibBuilder.loadTexts:
    staticRouteTable.setStatus("mandatory")
_StaticRouteEntry_Object = MibTableRow
staticRouteEntry = _StaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1)
)
staticRouteEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "staticRouteIp"),
    (0, "ZYXEL-ES3124PWR-MIB", "staticRouteMask"),
)
if mibBuilder.loadTexts:
    staticRouteEntry.setStatus("mandatory")
_StaticRouteName_Type = DisplayString
_StaticRouteName_Object = MibTableColumn
staticRouteName = _StaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1, 1),
    _StaticRouteName_Type()
)
staticRouteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteName.setStatus("mandatory")
_StaticRouteIp_Type = IpAddress
_StaticRouteIp_Object = MibTableColumn
staticRouteIp = _StaticRouteIp_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1, 2),
    _StaticRouteIp_Type()
)
staticRouteIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteIp.setStatus("mandatory")
_StaticRouteMask_Type = IpAddress
_StaticRouteMask_Object = MibTableColumn
staticRouteMask = _StaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1, 3),
    _StaticRouteMask_Type()
)
staticRouteMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticRouteMask.setStatus("mandatory")
_StaticRouteGateway_Type = IpAddress
_StaticRouteGateway_Object = MibTableColumn
staticRouteGateway = _StaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1, 4),
    _StaticRouteGateway_Type()
)
staticRouteGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteGateway.setStatus("mandatory")
_StaticRouteMetric_Type = Integer32
_StaticRouteMetric_Object = MibTableColumn
staticRouteMetric = _StaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1, 5),
    _StaticRouteMetric_Type()
)
staticRouteMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRouteMetric.setStatus("mandatory")
_StaticRouteRowStatus_Type = RowStatus
_StaticRouteRowStatus_Object = MibTableColumn
staticRouteRowStatus = _StaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 21, 2, 1, 6),
    _StaticRouteRowStatus_Type()
)
staticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticRouteRowStatus.setStatus("mandatory")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22)
)
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("mandatory")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1, 1)
)
arpEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "arpIndex"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("mandatory")
_ArpIndex_Type = Integer32
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1, 1, 1),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("mandatory")
_ArpIpAddr_Type = IpAddress
_ArpIpAddr_Object = MibTableColumn
arpIpAddr = _ArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1, 1, 2),
    _ArpIpAddr_Type()
)
arpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIpAddr.setStatus("mandatory")
_ArpMacAddr_Type = PhysAddress
_ArpMacAddr_Object = MibTableColumn
arpMacAddr = _ArpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1, 1, 3),
    _ArpMacAddr_Type()
)
arpMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacAddr.setStatus("mandatory")
_ArpMacVid_Type = Integer32
_ArpMacVid_Object = MibTableColumn
arpMacVid = _ArpMacVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1, 1, 4),
    _ArpMacVid_Type()
)
arpMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMacVid.setStatus("mandatory")
_ArpType_Type = Integer32
_ArpType_Object = MibTableColumn
arpType = _ArpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 22, 1, 1, 5),
    _ArpType_Type()
)
arpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpType.setStatus("mandatory")
_PltMgmt_ObjectIdentity = ObjectIdentity
pltMgmt = _PltMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23)
)
_PltCtlTable_Object = MibTable
pltCtlTable = _PltCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1)
)
if mibBuilder.loadTexts:
    pltCtlTable.setStatus("mandatory")
_PltCtlEntry_Object = MibTableRow
pltCtlEntry = _PltCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1)
)
pltCtlEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "pltCtlInstType"),
    (0, "ZYXEL-ES3124PWR-MIB", "pltCtlInstId"),
)
if mibBuilder.loadTexts:
    pltCtlEntry.setStatus("mandatory")


class _PltCtlInstType_Type(Integer32):
    """Custom type pltCtlInstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_PltCtlInstType_Type.__name__ = "Integer32"
_PltCtlInstType_Object = MibTableColumn
pltCtlInstType = _PltCtlInstType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1, 1),
    _PltCtlInstType_Type()
)
pltCtlInstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pltCtlInstType.setStatus("mandatory")
_PltCtlInstId_Type = Integer32
_PltCtlInstId_Object = MibTableColumn
pltCtlInstId = _PltCtlInstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1, 2),
    _PltCtlInstId_Type()
)
pltCtlInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pltCtlInstId.setStatus("mandatory")
_PltCtlIpAddr_Type = IpAddress
_PltCtlIpAddr_Object = MibTableColumn
pltCtlIpAddr = _PltCtlIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1, 3),
    _PltCtlIpAddr_Type()
)
pltCtlIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pltCtlIpAddr.setStatus("mandatory")
_PltCtlMask_Type = IpAddress
_PltCtlMask_Object = MibTableColumn
pltCtlMask = _PltCtlMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1, 4),
    _PltCtlMask_Type()
)
pltCtlMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pltCtlMask.setStatus("mandatory")
_PltCtlGw_Type = IpAddress
_PltCtlGw_Object = MibTableColumn
pltCtlGw = _PltCtlGw_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1, 5),
    _PltCtlGw_Type()
)
pltCtlGw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pltCtlGw.setStatus("mandatory")
_PltCtlRowStatus_Type = RowStatus
_PltCtlRowStatus_Object = MibTableColumn
pltCtlRowStatus = _PltCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 1, 1, 6),
    _PltCtlRowStatus_Type()
)
pltCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pltCtlRowStatus.setStatus("mandatory")
_PingCtlTable_Object = MibTable
pingCtlTable = _PingCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2)
)
if mibBuilder.loadTexts:
    pingCtlTable.setStatus("current")
_PingCtlEntry_Object = MibTableRow
pingCtlEntry = _PingCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1)
)
pingCtlEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlServInstType"),
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlServInstId"),
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    pingCtlEntry.setStatus("current")


class _PingCtlServInstType_Type(Integer32):
    """Custom type pingCtlServInstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_PingCtlServInstType_Type.__name__ = "Integer32"
_PingCtlServInstType_Object = MibTableColumn
pingCtlServInstType = _PingCtlServInstType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 1),
    _PingCtlServInstType_Type()
)
pingCtlServInstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingCtlServInstType.setStatus("mandatory")
_PingCtlServInstId_Type = Integer32
_PingCtlServInstId_Object = MibTableColumn
pingCtlServInstId = _PingCtlServInstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 2),
    _PingCtlServInstId_Type()
)
pingCtlServInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingCtlServInstId.setStatus("mandatory")


class _PingCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type pingCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PingCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_PingCtlOwnerIndex_Object = MibTableColumn
pingCtlOwnerIndex = _PingCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 3),
    _PingCtlOwnerIndex_Type()
)
pingCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingCtlOwnerIndex.setStatus("current")


class _PingCtlTestName_Type(SnmpAdminString):
    """Custom type pingCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PingCtlTestName_Type.__name__ = "SnmpAdminString"
_PingCtlTestName_Object = MibTableColumn
pingCtlTestName = _PingCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 4),
    _PingCtlTestName_Type()
)
pingCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingCtlTestName.setStatus("current")


class _PingCtlTargetAddressType_Type(InetAddressType):
    """Custom type pingCtlTargetAddressType based on InetAddressType"""
    defaultValue = 0


_PingCtlTargetAddressType_Type.__name__ = "InetAddressType"
_PingCtlTargetAddressType_Object = MibTableColumn
pingCtlTargetAddressType = _PingCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 5),
    _PingCtlTargetAddressType_Type()
)
pingCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTargetAddressType.setStatus("current")


class _PingCtlTargetAddress_Type(InetAddress):
    """Custom type pingCtlTargetAddress based on InetAddress"""
    defaultHexValue = ""


_PingCtlTargetAddress_Type.__name__ = "InetAddress"
_PingCtlTargetAddress_Object = MibTableColumn
pingCtlTargetAddress = _PingCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 6),
    _PingCtlTargetAddress_Type()
)
pingCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTargetAddress.setStatus("current")


class _PingCtlDataSize_Type(Unsigned32):
    """Custom type pingCtlDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65507),
    )


_PingCtlDataSize_Type.__name__ = "Unsigned32"
_PingCtlDataSize_Object = MibTableColumn
pingCtlDataSize = _PingCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 7),
    _PingCtlDataSize_Type()
)
pingCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlDataSize.setUnits("octets")


class _PingCtlTimeOut_Type(Unsigned32):
    """Custom type pingCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_PingCtlTimeOut_Type.__name__ = "Unsigned32"
_PingCtlTimeOut_Object = MibTableColumn
pingCtlTimeOut = _PingCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 8),
    _PingCtlTimeOut_Type()
)
pingCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlTimeOut.setUnits("seconds")


class _PingCtlProbeCount_Type(Unsigned32):
    """Custom type pingCtlProbeCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_PingCtlProbeCount_Type.__name__ = "Unsigned32"
_PingCtlProbeCount_Object = MibTableColumn
pingCtlProbeCount = _PingCtlProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 9),
    _PingCtlProbeCount_Type()
)
pingCtlProbeCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlProbeCount.setUnits("probes")


class _PingCtlAdminStatus_Type(Integer32):
    """Custom type pingCtlAdminStatus based on Integer32"""
    defaultValue = 2

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


_PingCtlAdminStatus_Type.__name__ = "Integer32"
_PingCtlAdminStatus_Object = MibTableColumn
pingCtlAdminStatus = _PingCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 10),
    _PingCtlAdminStatus_Type()
)
pingCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlAdminStatus.setStatus("current")


class _PingCtlDataFill_Type(OctetString):
    """Custom type pingCtlDataFill based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_PingCtlDataFill_Type.__name__ = "OctetString"
_PingCtlDataFill_Object = MibTableColumn
pingCtlDataFill = _PingCtlDataFill_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 11),
    _PingCtlDataFill_Type()
)
pingCtlDataFill.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDataFill.setStatus("current")


class _PingCtlFrequency_Type(Unsigned32):
    """Custom type pingCtlFrequency based on Unsigned32"""
    defaultValue = 0


_PingCtlFrequency_Type.__name__ = "Unsigned32"
_PingCtlFrequency_Object = MibTableColumn
pingCtlFrequency = _PingCtlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 12),
    _PingCtlFrequency_Type()
)
pingCtlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlFrequency.setUnits("seconds")


class _PingCtlMaxRows_Type(Unsigned32):
    """Custom type pingCtlMaxRows based on Unsigned32"""
    defaultValue = 50


_PingCtlMaxRows_Type.__name__ = "Unsigned32"
_PingCtlMaxRows_Object = MibTableColumn
pingCtlMaxRows = _PingCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 13),
    _PingCtlMaxRows_Type()
)
pingCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    pingCtlMaxRows.setUnits("rows")


class _PingCtlStorageType_Type(StorageType):
    """Custom type pingCtlStorageType based on StorageType"""
    defaultValue = 3


_PingCtlStorageType_Type.__name__ = "StorageType"
_PingCtlStorageType_Object = MibTableColumn
pingCtlStorageType = _PingCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 14),
    _PingCtlStorageType_Type()
)
pingCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlStorageType.setStatus("current")


class _PingCtlTrapGeneration_Type(Bits):
    """Custom type pingCtlTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("probeFailure", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_PingCtlTrapGeneration_Type.__name__ = "Bits"
_PingCtlTrapGeneration_Object = MibTableColumn
pingCtlTrapGeneration = _PingCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 15),
    _PingCtlTrapGeneration_Type()
)
pingCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTrapGeneration.setStatus("current")


class _PingCtlTrapProbeFailureFilter_Type(Unsigned32):
    """Custom type pingCtlTrapProbeFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PingCtlTrapProbeFailureFilter_Type.__name__ = "Unsigned32"
_PingCtlTrapProbeFailureFilter_Object = MibTableColumn
pingCtlTrapProbeFailureFilter = _PingCtlTrapProbeFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 16),
    _PingCtlTrapProbeFailureFilter_Type()
)
pingCtlTrapProbeFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTrapProbeFailureFilter.setStatus("current")


class _PingCtlTrapTestFailureFilter_Type(Unsigned32):
    """Custom type pingCtlTrapTestFailureFilter based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PingCtlTrapTestFailureFilter_Type.__name__ = "Unsigned32"
_PingCtlTrapTestFailureFilter_Object = MibTableColumn
pingCtlTrapTestFailureFilter = _PingCtlTrapTestFailureFilter_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 17),
    _PingCtlTrapTestFailureFilter_Type()
)
pingCtlTrapTestFailureFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlTrapTestFailureFilter.setStatus("current")
_PingCtlType_Type = ObjectIdentifier
_PingCtlType_Object = MibTableColumn
pingCtlType = _PingCtlType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 18),
    _PingCtlType_Type()
)
pingCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlType.setStatus("current")


class _PingCtlDescr_Type(SnmpAdminString):
    """Custom type pingCtlDescr based on SnmpAdminString"""
    defaultHexValue = "00"


_PingCtlDescr_Type.__name__ = "SnmpAdminString"
_PingCtlDescr_Object = MibTableColumn
pingCtlDescr = _PingCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 19),
    _PingCtlDescr_Type()
)
pingCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDescr.setStatus("current")


class _PingCtlSourceAddressType_Type(InetAddressType):
    """Custom type pingCtlSourceAddressType based on InetAddressType"""
    defaultValue = 1


_PingCtlSourceAddressType_Type.__name__ = "InetAddressType"
_PingCtlSourceAddressType_Object = MibTableColumn
pingCtlSourceAddressType = _PingCtlSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 20),
    _PingCtlSourceAddressType_Type()
)
pingCtlSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlSourceAddressType.setStatus("current")


class _PingCtlSourceAddress_Type(InetAddress):
    """Custom type pingCtlSourceAddress based on InetAddress"""
    defaultHexValue = ""


_PingCtlSourceAddress_Type.__name__ = "InetAddress"
_PingCtlSourceAddress_Object = MibTableColumn
pingCtlSourceAddress = _PingCtlSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 21),
    _PingCtlSourceAddress_Type()
)
pingCtlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlSourceAddress.setStatus("current")


class _PingCtlIfIndex_Type(InterfaceIndexOrZero):
    """Custom type pingCtlIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_PingCtlIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_PingCtlIfIndex_Object = MibTableColumn
pingCtlIfIndex = _PingCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 22),
    _PingCtlIfIndex_Type()
)
pingCtlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlIfIndex.setStatus("current")


class _PingCtlByPassRouteTable_Type(TruthValue):
    """Custom type pingCtlByPassRouteTable based on TruthValue"""
    defaultValue = 2


_PingCtlByPassRouteTable_Type.__name__ = "TruthValue"
_PingCtlByPassRouteTable_Object = MibTableColumn
pingCtlByPassRouteTable = _PingCtlByPassRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 23),
    _PingCtlByPassRouteTable_Type()
)
pingCtlByPassRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlByPassRouteTable.setStatus("current")


class _PingCtlDSField_Type(Unsigned32):
    """Custom type pingCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PingCtlDSField_Type.__name__ = "Unsigned32"
_PingCtlDSField_Object = MibTableColumn
pingCtlDSField = _PingCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 24),
    _PingCtlDSField_Type()
)
pingCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlDSField.setStatus("current")
_PingCtlRowStatus_Type = RowStatus
_PingCtlRowStatus_Object = MibTableColumn
pingCtlRowStatus = _PingCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 2, 1, 25),
    _PingCtlRowStatus_Type()
)
pingCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pingCtlRowStatus.setStatus("current")
_PingResultsTable_Object = MibTable
pingResultsTable = _PingResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3)
)
if mibBuilder.loadTexts:
    pingResultsTable.setStatus("current")
_PingResultsEntry_Object = MibTableRow
pingResultsEntry = _PingResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1)
)
pingResultsEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    pingResultsEntry.setStatus("current")


class _PingResultsOperStatus_Type(Integer32):
    """Custom type pingResultsOperStatus based on Integer32"""
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


_PingResultsOperStatus_Type.__name__ = "Integer32"
_PingResultsOperStatus_Object = MibTableColumn
pingResultsOperStatus = _PingResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 1),
    _PingResultsOperStatus_Type()
)
pingResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsOperStatus.setStatus("current")


class _PingResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type pingResultsIpTargetAddressType based on InetAddressType"""
    defaultValue = 0


_PingResultsIpTargetAddressType_Type.__name__ = "InetAddressType"
_PingResultsIpTargetAddressType_Object = MibTableColumn
pingResultsIpTargetAddressType = _PingResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 2),
    _PingResultsIpTargetAddressType_Type()
)
pingResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsIpTargetAddressType.setStatus("current")


class _PingResultsIpTargetAddress_Type(InetAddress):
    """Custom type pingResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_PingResultsIpTargetAddress_Type.__name__ = "InetAddress"
_PingResultsIpTargetAddress_Object = MibTableColumn
pingResultsIpTargetAddress = _PingResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 3),
    _PingResultsIpTargetAddress_Type()
)
pingResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsIpTargetAddress.setStatus("current")
_PingResultsMinRtt_Type = Unsigned32
_PingResultsMinRtt_Object = MibTableColumn
pingResultsMinRtt = _PingResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 4),
    _PingResultsMinRtt_Type()
)
pingResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsMinRtt.setUnits("milliseconds")
_PingResultsMaxRtt_Type = Unsigned32
_PingResultsMaxRtt_Object = MibTableColumn
pingResultsMaxRtt = _PingResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 5),
    _PingResultsMaxRtt_Type()
)
pingResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsMaxRtt.setUnits("milliseconds")
_PingResultsAverageRtt_Type = Unsigned32
_PingResultsAverageRtt_Object = MibTableColumn
pingResultsAverageRtt = _PingResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 6),
    _PingResultsAverageRtt_Type()
)
pingResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsAverageRtt.setUnits("milliseconds")
_PingResultsProbeResponses_Type = Unsigned32
_PingResultsProbeResponses_Object = MibTableColumn
pingResultsProbeResponses = _PingResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 7),
    _PingResultsProbeResponses_Type()
)
pingResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsProbeResponses.setUnits("responses")
_PingResultsSentProbes_Type = Unsigned32
_PingResultsSentProbes_Object = MibTableColumn
pingResultsSentProbes = _PingResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 8),
    _PingResultsSentProbes_Type()
)
pingResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsSentProbes.setUnits("probes")
_PingResultsRttSumOfSquares_Type = Unsigned32
_PingResultsRttSumOfSquares_Object = MibTableColumn
pingResultsRttSumOfSquares = _PingResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 9),
    _PingResultsRttSumOfSquares_Type()
)
pingResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    pingResultsRttSumOfSquares.setUnits("milliseconds")
_PingResultsLastGoodProbe_Type = DateAndTime
_PingResultsLastGoodProbe_Object = MibTableColumn
pingResultsLastGoodProbe = _PingResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 3, 1, 10),
    _PingResultsLastGoodProbe_Type()
)
pingResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingResultsLastGoodProbe.setStatus("current")
_PingProbeHistoryTable_Object = MibTable
pingProbeHistoryTable = _PingProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4)
)
if mibBuilder.loadTexts:
    pingProbeHistoryTable.setStatus("current")
_PingProbeHistoryEntry_Object = MibTableRow
pingProbeHistoryEntry = _PingProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4, 1)
)
pingProbeHistoryEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "pingCtlTestName"),
    (0, "ZYXEL-ES3124PWR-MIB", "pingProbeHistoryIndex"),
)
if mibBuilder.loadTexts:
    pingProbeHistoryEntry.setStatus("current")


class _PingProbeHistoryIndex_Type(Unsigned32):
    """Custom type pingProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_PingProbeHistoryIndex_Type.__name__ = "Unsigned32"
_PingProbeHistoryIndex_Object = MibTableColumn
pingProbeHistoryIndex = _PingProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4, 1, 1),
    _PingProbeHistoryIndex_Type()
)
pingProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pingProbeHistoryIndex.setStatus("current")
_PingProbeHistoryResponse_Type = Unsigned32
_PingProbeHistoryResponse_Object = MibTableColumn
pingProbeHistoryResponse = _PingProbeHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4, 1, 2),
    _PingProbeHistoryResponse_Type()
)
pingProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    pingProbeHistoryResponse.setUnits("milliseconds")
_PingProbeHistoryStatus_Type = OperationResponseStatus
_PingProbeHistoryStatus_Object = MibTableColumn
pingProbeHistoryStatus = _PingProbeHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4, 1, 3),
    _PingProbeHistoryStatus_Type()
)
pingProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryStatus.setStatus("current")
_PingProbeHistoryLastRC_Type = Integer32
_PingProbeHistoryLastRC_Object = MibTableColumn
pingProbeHistoryLastRC = _PingProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4, 1, 4),
    _PingProbeHistoryLastRC_Type()
)
pingProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryLastRC.setStatus("current")
_PingProbeHistoryTime_Type = DateAndTime
_PingProbeHistoryTime_Object = MibTableColumn
pingProbeHistoryTime = _PingProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 4, 1, 5),
    _PingProbeHistoryTime_Type()
)
pingProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingProbeHistoryTime.setStatus("current")
_TraceRouteCtlTable_Object = MibTable
traceRouteCtlTable = _TraceRouteCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5)
)
if mibBuilder.loadTexts:
    traceRouteCtlTable.setStatus("current")
_TraceRouteCtlEntry_Object = MibTableRow
traceRouteCtlEntry = _TraceRouteCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1)
)
traceRouteCtlEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlServInstType"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlServInstId"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlTestName"),
)
if mibBuilder.loadTexts:
    traceRouteCtlEntry.setStatus("current")


class _TraceRouteCtlServInstType_Type(Integer32):
    """Custom type traceRouteCtlServInstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlan", 1)
    )


_TraceRouteCtlServInstType_Type.__name__ = "Integer32"
_TraceRouteCtlServInstType_Object = MibTableColumn
traceRouteCtlServInstType = _TraceRouteCtlServInstType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 1),
    _TraceRouteCtlServInstType_Type()
)
traceRouteCtlServInstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteCtlServInstType.setStatus("mandatory")
_TraceRouteCtlServInstId_Type = Integer32
_TraceRouteCtlServInstId_Object = MibTableColumn
traceRouteCtlServInstId = _TraceRouteCtlServInstId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 2),
    _TraceRouteCtlServInstId_Type()
)
traceRouteCtlServInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteCtlServInstId.setStatus("mandatory")


class _TraceRouteCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type traceRouteCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraceRouteCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_TraceRouteCtlOwnerIndex_Object = MibTableColumn
traceRouteCtlOwnerIndex = _TraceRouteCtlOwnerIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 3),
    _TraceRouteCtlOwnerIndex_Type()
)
traceRouteCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteCtlOwnerIndex.setStatus("current")


class _TraceRouteCtlTestName_Type(SnmpAdminString):
    """Custom type traceRouteCtlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TraceRouteCtlTestName_Type.__name__ = "SnmpAdminString"
_TraceRouteCtlTestName_Object = MibTableColumn
traceRouteCtlTestName = _TraceRouteCtlTestName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 4),
    _TraceRouteCtlTestName_Type()
)
traceRouteCtlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteCtlTestName.setStatus("current")


class _TraceRouteCtlTargetAddressType_Type(InetAddressType):
    """Custom type traceRouteCtlTargetAddressType based on InetAddressType"""
    defaultValue = 1


_TraceRouteCtlTargetAddressType_Type.__name__ = "InetAddressType"
_TraceRouteCtlTargetAddressType_Object = MibTableColumn
traceRouteCtlTargetAddressType = _TraceRouteCtlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 5),
    _TraceRouteCtlTargetAddressType_Type()
)
traceRouteCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTargetAddressType.setStatus("current")
_TraceRouteCtlTargetAddress_Type = InetAddress
_TraceRouteCtlTargetAddress_Object = MibTableColumn
traceRouteCtlTargetAddress = _TraceRouteCtlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 6),
    _TraceRouteCtlTargetAddress_Type()
)
traceRouteCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTargetAddress.setStatus("current")


class _TraceRouteCtlByPassRouteTable_Type(TruthValue):
    """Custom type traceRouteCtlByPassRouteTable based on TruthValue"""
    defaultValue = 2


_TraceRouteCtlByPassRouteTable_Type.__name__ = "TruthValue"
_TraceRouteCtlByPassRouteTable_Object = MibTableColumn
traceRouteCtlByPassRouteTable = _TraceRouteCtlByPassRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 7),
    _TraceRouteCtlByPassRouteTable_Type()
)
traceRouteCtlByPassRouteTable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlByPassRouteTable.setStatus("current")


class _TraceRouteCtlDataSize_Type(Unsigned32):
    """Custom type traceRouteCtlDataSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65507),
    )


_TraceRouteCtlDataSize_Type.__name__ = "Unsigned32"
_TraceRouteCtlDataSize_Object = MibTableColumn
traceRouteCtlDataSize = _TraceRouteCtlDataSize_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 8),
    _TraceRouteCtlDataSize_Type()
)
traceRouteCtlDataSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDataSize.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlDataSize.setUnits("octets")


class _TraceRouteCtlTimeOut_Type(Unsigned32):
    """Custom type traceRouteCtlTimeOut based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TraceRouteCtlTimeOut_Type.__name__ = "Unsigned32"
_TraceRouteCtlTimeOut_Object = MibTableColumn
traceRouteCtlTimeOut = _TraceRouteCtlTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 9),
    _TraceRouteCtlTimeOut_Type()
)
traceRouteCtlTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlTimeOut.setUnits("seconds")


class _TraceRouteCtlProbesPerHop_Type(Unsigned32):
    """Custom type traceRouteCtlProbesPerHop based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TraceRouteCtlProbesPerHop_Type.__name__ = "Unsigned32"
_TraceRouteCtlProbesPerHop_Object = MibTableColumn
traceRouteCtlProbesPerHop = _TraceRouteCtlProbesPerHop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 10),
    _TraceRouteCtlProbesPerHop_Type()
)
traceRouteCtlProbesPerHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlProbesPerHop.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlProbesPerHop.setUnits("probes")


class _TraceRouteCtlPort_Type(Unsigned32):
    """Custom type traceRouteCtlPort based on Unsigned32"""
    defaultValue = 33434

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteCtlPort_Type.__name__ = "Unsigned32"
_TraceRouteCtlPort_Object = MibTableColumn
traceRouteCtlPort = _TraceRouteCtlPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 11),
    _TraceRouteCtlPort_Type()
)
traceRouteCtlPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlPort.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlPort.setUnits("UDP Port")


class _TraceRouteCtlMaxTtl_Type(Unsigned32):
    """Custom type traceRouteCtlMaxTtl based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteCtlMaxTtl_Type.__name__ = "Unsigned32"
_TraceRouteCtlMaxTtl_Object = MibTableColumn
traceRouteCtlMaxTtl = _TraceRouteCtlMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 12),
    _TraceRouteCtlMaxTtl_Type()
)
traceRouteCtlMaxTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMaxTtl.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlMaxTtl.setUnits("time-to-live value")


class _TraceRouteCtlDSField_Type(Unsigned32):
    """Custom type traceRouteCtlDSField based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceRouteCtlDSField_Type.__name__ = "Unsigned32"
_TraceRouteCtlDSField_Object = MibTableColumn
traceRouteCtlDSField = _TraceRouteCtlDSField_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 13),
    _TraceRouteCtlDSField_Type()
)
traceRouteCtlDSField.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDSField.setStatus("current")


class _TraceRouteCtlSourceAddressType_Type(InetAddressType):
    """Custom type traceRouteCtlSourceAddressType based on InetAddressType"""
    defaultValue = 0


_TraceRouteCtlSourceAddressType_Type.__name__ = "InetAddressType"
_TraceRouteCtlSourceAddressType_Object = MibTableColumn
traceRouteCtlSourceAddressType = _TraceRouteCtlSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 14),
    _TraceRouteCtlSourceAddressType_Type()
)
traceRouteCtlSourceAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlSourceAddressType.setStatus("current")


class _TraceRouteCtlSourceAddress_Type(InetAddress):
    """Custom type traceRouteCtlSourceAddress based on InetAddress"""
    defaultHexValue = ""


_TraceRouteCtlSourceAddress_Type.__name__ = "InetAddress"
_TraceRouteCtlSourceAddress_Object = MibTableColumn
traceRouteCtlSourceAddress = _TraceRouteCtlSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 15),
    _TraceRouteCtlSourceAddress_Type()
)
traceRouteCtlSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlSourceAddress.setStatus("current")


class _TraceRouteCtlIfIndex_Type(InterfaceIndexOrZero):
    """Custom type traceRouteCtlIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_TraceRouteCtlIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_TraceRouteCtlIfIndex_Object = MibTableColumn
traceRouteCtlIfIndex = _TraceRouteCtlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 16),
    _TraceRouteCtlIfIndex_Type()
)
traceRouteCtlIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlIfIndex.setStatus("current")


class _TraceRouteCtlMiscOptions_Type(SnmpAdminString):
    """Custom type traceRouteCtlMiscOptions based on SnmpAdminString"""
    defaultHexValue = ""


_TraceRouteCtlMiscOptions_Type.__name__ = "SnmpAdminString"
_TraceRouteCtlMiscOptions_Object = MibTableColumn
traceRouteCtlMiscOptions = _TraceRouteCtlMiscOptions_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 17),
    _TraceRouteCtlMiscOptions_Type()
)
traceRouteCtlMiscOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMiscOptions.setStatus("current")


class _TraceRouteCtlMaxFailures_Type(Unsigned32):
    """Custom type traceRouteCtlMaxFailures based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceRouteCtlMaxFailures_Type.__name__ = "Unsigned32"
_TraceRouteCtlMaxFailures_Object = MibTableColumn
traceRouteCtlMaxFailures = _TraceRouteCtlMaxFailures_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 18),
    _TraceRouteCtlMaxFailures_Type()
)
traceRouteCtlMaxFailures.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMaxFailures.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlMaxFailures.setUnits("timeouts")


class _TraceRouteCtlDontFragment_Type(TruthValue):
    """Custom type traceRouteCtlDontFragment based on TruthValue"""
    defaultValue = 2


_TraceRouteCtlDontFragment_Type.__name__ = "TruthValue"
_TraceRouteCtlDontFragment_Object = MibTableColumn
traceRouteCtlDontFragment = _TraceRouteCtlDontFragment_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 19),
    _TraceRouteCtlDontFragment_Type()
)
traceRouteCtlDontFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDontFragment.setStatus("current")


class _TraceRouteCtlInitialTtl_Type(Unsigned32):
    """Custom type traceRouteCtlInitialTtl based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceRouteCtlInitialTtl_Type.__name__ = "Unsigned32"
_TraceRouteCtlInitialTtl_Object = MibTableColumn
traceRouteCtlInitialTtl = _TraceRouteCtlInitialTtl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 20),
    _TraceRouteCtlInitialTtl_Type()
)
traceRouteCtlInitialTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlInitialTtl.setStatus("current")


class _TraceRouteCtlFrequency_Type(Unsigned32):
    """Custom type traceRouteCtlFrequency based on Unsigned32"""
    defaultValue = 0


_TraceRouteCtlFrequency_Type.__name__ = "Unsigned32"
_TraceRouteCtlFrequency_Object = MibTableColumn
traceRouteCtlFrequency = _TraceRouteCtlFrequency_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 21),
    _TraceRouteCtlFrequency_Type()
)
traceRouteCtlFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlFrequency.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlFrequency.setUnits("seconds")


class _TraceRouteCtlStorageType_Type(StorageType):
    """Custom type traceRouteCtlStorageType based on StorageType"""
    defaultValue = 3


_TraceRouteCtlStorageType_Type.__name__ = "StorageType"
_TraceRouteCtlStorageType_Object = MibTableColumn
traceRouteCtlStorageType = _TraceRouteCtlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 22),
    _TraceRouteCtlStorageType_Type()
)
traceRouteCtlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlStorageType.setStatus("current")


class _TraceRouteCtlAdminStatus_Type(Integer32):
    """Custom type traceRouteCtlAdminStatus based on Integer32"""
    defaultValue = 2

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


_TraceRouteCtlAdminStatus_Type.__name__ = "Integer32"
_TraceRouteCtlAdminStatus_Object = MibTableColumn
traceRouteCtlAdminStatus = _TraceRouteCtlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 23),
    _TraceRouteCtlAdminStatus_Type()
)
traceRouteCtlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlAdminStatus.setStatus("current")


class _TraceRouteCtlDescr_Type(SnmpAdminString):
    """Custom type traceRouteCtlDescr based on SnmpAdminString"""
    defaultHexValue = "00"


_TraceRouteCtlDescr_Type.__name__ = "SnmpAdminString"
_TraceRouteCtlDescr_Object = MibTableColumn
traceRouteCtlDescr = _TraceRouteCtlDescr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 24),
    _TraceRouteCtlDescr_Type()
)
traceRouteCtlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlDescr.setStatus("current")


class _TraceRouteCtlMaxRows_Type(Unsigned32):
    """Custom type traceRouteCtlMaxRows based on Unsigned32"""
    defaultValue = 50


_TraceRouteCtlMaxRows_Type.__name__ = "Unsigned32"
_TraceRouteCtlMaxRows_Object = MibTableColumn
traceRouteCtlMaxRows = _TraceRouteCtlMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 25),
    _TraceRouteCtlMaxRows_Type()
)
traceRouteCtlMaxRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlMaxRows.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteCtlMaxRows.setUnits("rows")


class _TraceRouteCtlTrapGeneration_Type(Bits):
    """Custom type traceRouteCtlTrapGeneration based on Bits"""
    namedValues = NamedValues(
        *(("pathChange", 0),
          ("testFailure", 1),
          ("testCompletion", 2))
    )

_TraceRouteCtlTrapGeneration_Type.__name__ = "Bits"
_TraceRouteCtlTrapGeneration_Object = MibTableColumn
traceRouteCtlTrapGeneration = _TraceRouteCtlTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 26),
    _TraceRouteCtlTrapGeneration_Type()
)
traceRouteCtlTrapGeneration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlTrapGeneration.setStatus("current")


class _TraceRouteCtlCreateHopsEntries_Type(TruthValue):
    """Custom type traceRouteCtlCreateHopsEntries based on TruthValue"""
    defaultValue = 2


_TraceRouteCtlCreateHopsEntries_Type.__name__ = "TruthValue"
_TraceRouteCtlCreateHopsEntries_Object = MibTableColumn
traceRouteCtlCreateHopsEntries = _TraceRouteCtlCreateHopsEntries_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 27),
    _TraceRouteCtlCreateHopsEntries_Type()
)
traceRouteCtlCreateHopsEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlCreateHopsEntries.setStatus("current")
_TraceRouteCtlType_Type = ObjectIdentifier
_TraceRouteCtlType_Object = MibTableColumn
traceRouteCtlType = _TraceRouteCtlType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 28),
    _TraceRouteCtlType_Type()
)
traceRouteCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlType.setStatus("current")
_TraceRouteCtlRowStatus_Type = RowStatus
_TraceRouteCtlRowStatus_Object = MibTableColumn
traceRouteCtlRowStatus = _TraceRouteCtlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 5, 1, 29),
    _TraceRouteCtlRowStatus_Type()
)
traceRouteCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteCtlRowStatus.setStatus("current")
_TraceRouteResultsTable_Object = MibTable
traceRouteResultsTable = _TraceRouteResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6)
)
if mibBuilder.loadTexts:
    traceRouteResultsTable.setStatus("current")
_TraceRouteResultsEntry_Object = MibTableRow
traceRouteResultsEntry = _TraceRouteResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1)
)
traceRouteResultsEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlTestName"),
)
if mibBuilder.loadTexts:
    traceRouteResultsEntry.setStatus("current")


class _TraceRouteResultsOperStatus_Type(Integer32):
    """Custom type traceRouteResultsOperStatus based on Integer32"""
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


_TraceRouteResultsOperStatus_Type.__name__ = "Integer32"
_TraceRouteResultsOperStatus_Object = MibTableColumn
traceRouteResultsOperStatus = _TraceRouteResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 1),
    _TraceRouteResultsOperStatus_Type()
)
traceRouteResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsOperStatus.setStatus("current")
_TraceRouteResultsCurHopCount_Type = Gauge32
_TraceRouteResultsCurHopCount_Object = MibTableColumn
traceRouteResultsCurHopCount = _TraceRouteResultsCurHopCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 2),
    _TraceRouteResultsCurHopCount_Type()
)
traceRouteResultsCurHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsCurHopCount.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsCurHopCount.setUnits("hops")
_TraceRouteResultsCurProbeCount_Type = Gauge32
_TraceRouteResultsCurProbeCount_Object = MibTableColumn
traceRouteResultsCurProbeCount = _TraceRouteResultsCurProbeCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 3),
    _TraceRouteResultsCurProbeCount_Type()
)
traceRouteResultsCurProbeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsCurProbeCount.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsCurProbeCount.setUnits("probes")
_TraceRouteResultsIpTgtAddrType_Type = InetAddressType
_TraceRouteResultsIpTgtAddrType_Object = MibTableColumn
traceRouteResultsIpTgtAddrType = _TraceRouteResultsIpTgtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 4),
    _TraceRouteResultsIpTgtAddrType_Type()
)
traceRouteResultsIpTgtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsIpTgtAddrType.setStatus("current")
_TraceRouteResultsIpTgtAddr_Type = InetAddress
_TraceRouteResultsIpTgtAddr_Object = MibTableColumn
traceRouteResultsIpTgtAddr = _TraceRouteResultsIpTgtAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 5),
    _TraceRouteResultsIpTgtAddr_Type()
)
traceRouteResultsIpTgtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsIpTgtAddr.setStatus("current")
_TraceRouteResultsTestAttempts_Type = Unsigned32
_TraceRouteResultsTestAttempts_Object = MibTableColumn
traceRouteResultsTestAttempts = _TraceRouteResultsTestAttempts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 6),
    _TraceRouteResultsTestAttempts_Type()
)
traceRouteResultsTestAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsTestAttempts.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsTestAttempts.setUnits("tests")
_TraceRouteResultsTestSuccesses_Type = Unsigned32
_TraceRouteResultsTestSuccesses_Object = MibTableColumn
traceRouteResultsTestSuccesses = _TraceRouteResultsTestSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 7),
    _TraceRouteResultsTestSuccesses_Type()
)
traceRouteResultsTestSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsTestSuccesses.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteResultsTestSuccesses.setUnits("tests")
_TraceRouteResultsLastGoodPath_Type = DateAndTime
_TraceRouteResultsLastGoodPath_Object = MibTableColumn
traceRouteResultsLastGoodPath = _TraceRouteResultsLastGoodPath_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 6, 1, 8),
    _TraceRouteResultsLastGoodPath_Type()
)
traceRouteResultsLastGoodPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteResultsLastGoodPath.setStatus("current")
_TraceRouteProbeHistoryTable_Object = MibTable
traceRouteProbeHistoryTable = _TraceRouteProbeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7)
)
if mibBuilder.loadTexts:
    traceRouteProbeHistoryTable.setStatus("current")
_TraceRouteProbeHistoryEntry_Object = MibTableRow
traceRouteProbeHistoryEntry = _TraceRouteProbeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1)
)
traceRouteProbeHistoryEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlTestName"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteProbeHistoryIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteProbeHistoryHopIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteProbeHistoryProbeIndex"),
)
if mibBuilder.loadTexts:
    traceRouteProbeHistoryEntry.setStatus("current")


class _TraceRouteProbeHistoryIndex_Type(Unsigned32):
    """Custom type traceRouteProbeHistoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_TraceRouteProbeHistoryIndex_Type.__name__ = "Unsigned32"
_TraceRouteProbeHistoryIndex_Object = MibTableColumn
traceRouteProbeHistoryIndex = _TraceRouteProbeHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 1),
    _TraceRouteProbeHistoryIndex_Type()
)
traceRouteProbeHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryIndex.setStatus("current")


class _TraceRouteProbeHistoryHopIndex_Type(Unsigned32):
    """Custom type traceRouteProbeHistoryHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteProbeHistoryHopIndex_Type.__name__ = "Unsigned32"
_TraceRouteProbeHistoryHopIndex_Object = MibTableColumn
traceRouteProbeHistoryHopIndex = _TraceRouteProbeHistoryHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 2),
    _TraceRouteProbeHistoryHopIndex_Type()
)
traceRouteProbeHistoryHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryHopIndex.setStatus("current")


class _TraceRouteProbeHistoryProbeIndex_Type(Unsigned32):
    """Custom type traceRouteProbeHistoryProbeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TraceRouteProbeHistoryProbeIndex_Type.__name__ = "Unsigned32"
_TraceRouteProbeHistoryProbeIndex_Object = MibTableColumn
traceRouteProbeHistoryProbeIndex = _TraceRouteProbeHistoryProbeIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 3),
    _TraceRouteProbeHistoryProbeIndex_Type()
)
traceRouteProbeHistoryProbeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryProbeIndex.setStatus("current")
_TraceRouteProbeHistoryHAddrType_Type = InetAddressType
_TraceRouteProbeHistoryHAddrType_Object = MibTableColumn
traceRouteProbeHistoryHAddrType = _TraceRouteProbeHistoryHAddrType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 4),
    _TraceRouteProbeHistoryHAddrType_Type()
)
traceRouteProbeHistoryHAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryHAddrType.setStatus("current")
_TraceRouteProbeHistoryHAddr_Type = InetAddress
_TraceRouteProbeHistoryHAddr_Object = MibTableColumn
traceRouteProbeHistoryHAddr = _TraceRouteProbeHistoryHAddr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 5),
    _TraceRouteProbeHistoryHAddr_Type()
)
traceRouteProbeHistoryHAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryHAddr.setStatus("current")
_TraceRouteProbeHistoryResponse_Type = Unsigned32
_TraceRouteProbeHistoryResponse_Object = MibTableColumn
traceRouteProbeHistoryResponse = _TraceRouteProbeHistoryResponse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 6),
    _TraceRouteProbeHistoryResponse_Type()
)
traceRouteProbeHistoryResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryResponse.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryResponse.setUnits("milliseconds")
_TraceRouteProbeHistoryStatus_Type = OperationResponseStatus
_TraceRouteProbeHistoryStatus_Object = MibTableColumn
traceRouteProbeHistoryStatus = _TraceRouteProbeHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 7),
    _TraceRouteProbeHistoryStatus_Type()
)
traceRouteProbeHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryStatus.setStatus("current")
_TraceRouteProbeHistoryLastRC_Type = Integer32
_TraceRouteProbeHistoryLastRC_Object = MibTableColumn
traceRouteProbeHistoryLastRC = _TraceRouteProbeHistoryLastRC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 8),
    _TraceRouteProbeHistoryLastRC_Type()
)
traceRouteProbeHistoryLastRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryLastRC.setStatus("current")
_TraceRouteProbeHistoryTime_Type = DateAndTime
_TraceRouteProbeHistoryTime_Object = MibTableColumn
traceRouteProbeHistoryTime = _TraceRouteProbeHistoryTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 7, 1, 9),
    _TraceRouteProbeHistoryTime_Type()
)
traceRouteProbeHistoryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteProbeHistoryTime.setStatus("current")
_TraceRouteHopsTable_Object = MibTable
traceRouteHopsTable = _TraceRouteHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8)
)
if mibBuilder.loadTexts:
    traceRouteHopsTable.setStatus("current")
_TraceRouteHopsEntry_Object = MibTableRow
traceRouteHopsEntry = _TraceRouteHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1)
)
traceRouteHopsEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlOwnerIndex"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteCtlTestName"),
    (0, "ZYXEL-ES3124PWR-MIB", "traceRouteHopsHopIndex"),
)
if mibBuilder.loadTexts:
    traceRouteHopsEntry.setStatus("current")
_TraceRouteHopsHopIndex_Type = Unsigned32
_TraceRouteHopsHopIndex_Object = MibTableColumn
traceRouteHopsHopIndex = _TraceRouteHopsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 1),
    _TraceRouteHopsHopIndex_Type()
)
traceRouteHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    traceRouteHopsHopIndex.setStatus("current")
_TraceRouteHopsIpTgtAddressType_Type = InetAddressType
_TraceRouteHopsIpTgtAddressType_Object = MibTableColumn
traceRouteHopsIpTgtAddressType = _TraceRouteHopsIpTgtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 2),
    _TraceRouteHopsIpTgtAddressType_Type()
)
traceRouteHopsIpTgtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsIpTgtAddressType.setStatus("current")
_TraceRouteHopsIpTgtAddress_Type = InetAddress
_TraceRouteHopsIpTgtAddress_Object = MibTableColumn
traceRouteHopsIpTgtAddress = _TraceRouteHopsIpTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 3),
    _TraceRouteHopsIpTgtAddress_Type()
)
traceRouteHopsIpTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsIpTgtAddress.setStatus("current")
_TraceRouteHopsMinRtt_Type = Unsigned32
_TraceRouteHopsMinRtt_Object = MibTableColumn
traceRouteHopsMinRtt = _TraceRouteHopsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 4),
    _TraceRouteHopsMinRtt_Type()
)
traceRouteHopsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsMinRtt.setStatus("current")
_TraceRouteHopsMaxRtt_Type = Unsigned32
_TraceRouteHopsMaxRtt_Object = MibTableColumn
traceRouteHopsMaxRtt = _TraceRouteHopsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 5),
    _TraceRouteHopsMaxRtt_Type()
)
traceRouteHopsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsMaxRtt.setStatus("current")
_TraceRouteHopsAverageRtt_Type = Unsigned32
_TraceRouteHopsAverageRtt_Object = MibTableColumn
traceRouteHopsAverageRtt = _TraceRouteHopsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 6),
    _TraceRouteHopsAverageRtt_Type()
)
traceRouteHopsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsAverageRtt.setStatus("current")
_TraceRouteHopsRttSumOfSquares_Type = Unsigned32
_TraceRouteHopsRttSumOfSquares_Object = MibTableColumn
traceRouteHopsRttSumOfSquares = _TraceRouteHopsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 7),
    _TraceRouteHopsRttSumOfSquares_Type()
)
traceRouteHopsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsRttSumOfSquares.setStatus("current")
_TraceRouteHopsSentProbes_Type = Unsigned32
_TraceRouteHopsSentProbes_Object = MibTableColumn
traceRouteHopsSentProbes = _TraceRouteHopsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 8),
    _TraceRouteHopsSentProbes_Type()
)
traceRouteHopsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsSentProbes.setStatus("current")
_TraceRouteHopsProbeResponses_Type = Unsigned32
_TraceRouteHopsProbeResponses_Object = MibTableColumn
traceRouteHopsProbeResponses = _TraceRouteHopsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 9),
    _TraceRouteHopsProbeResponses_Type()
)
traceRouteHopsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsProbeResponses.setStatus("current")
_TraceRouteHopsLastGoodProbe_Type = DateAndTime
_TraceRouteHopsLastGoodProbe_Object = MibTableColumn
traceRouteHopsLastGoodProbe = _TraceRouteHopsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 23, 8, 1, 10),
    _TraceRouteHopsLastGoodProbe_Type()
)
traceRouteHopsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteHopsLastGoodProbe.setStatus("current")
_PortOpModeSetup_ObjectIdentity = ObjectIdentity
portOpModeSetup = _PortOpModeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24)
)
_PortOpModePortTable_Object = MibTable
portOpModePortTable = _PortOpModePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1)
)
if mibBuilder.loadTexts:
    portOpModePortTable.setStatus("mandatory")
_PortOpModePortEntry_Object = MibTableRow
portOpModePortEntry = _PortOpModePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1)
)
portOpModePortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portOpModePortEntry.setStatus("mandatory")


class _PortOpModePortSpeedDuplex_Type(Integer32):
    """Custom type portOpModePortSpeedDuplex based on Integer32"""
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
        *(("auto", 0),
          ("speed-10-half", 1),
          ("speed-10-full", 2),
          ("speed-100-half", 3),
          ("speed-100-full", 4),
          ("speed-1000-full", 5))
    )


_PortOpModePortSpeedDuplex_Type.__name__ = "Integer32"
_PortOpModePortSpeedDuplex_Object = MibTableColumn
portOpModePortSpeedDuplex = _PortOpModePortSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 1),
    _PortOpModePortSpeedDuplex_Type()
)
portOpModePortSpeedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortSpeedDuplex.setStatus("mandatory")


class _PortOpModePortFlowCntl_Type(Integer32):
    """Custom type portOpModePortFlowCntl based on Integer32"""
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


_PortOpModePortFlowCntl_Type.__name__ = "Integer32"
_PortOpModePortFlowCntl_Object = MibTableColumn
portOpModePortFlowCntl = _PortOpModePortFlowCntl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 2),
    _PortOpModePortFlowCntl_Type()
)
portOpModePortFlowCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortFlowCntl.setStatus("mandatory")


class _PortOpModePortName_Type(OctetString):
    """Custom type portOpModePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortOpModePortName_Type.__name__ = "OctetString"
_PortOpModePortName_Object = MibTableColumn
portOpModePortName = _PortOpModePortName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 3),
    _PortOpModePortName_Type()
)
portOpModePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortName.setStatus("mandatory")


class _PortOpModePortModuleType_Type(Integer32):
    """Custom type portOpModePortModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast-ethernet-10-100", 0),
          ("gigabit-ethernet-100-1000", 1))
    )


_PortOpModePortModuleType_Type.__name__ = "Integer32"
_PortOpModePortModuleType_Object = MibTableColumn
portOpModePortModuleType = _PortOpModePortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 4),
    _PortOpModePortModuleType_Type()
)
portOpModePortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortModuleType.setStatus("mandatory")


class _PortOpModePortLinkUpType_Type(Integer32):
    """Custom type portOpModePortLinkUpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("copper", 1),
          ("fiber", 2))
    )


_PortOpModePortLinkUpType_Type.__name__ = "Integer32"
_PortOpModePortLinkUpType_Object = MibTableColumn
portOpModePortLinkUpType = _PortOpModePortLinkUpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 5),
    _PortOpModePortLinkUpType_Type()
)
portOpModePortLinkUpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLinkUpType.setStatus("mandatory")
_PortOpModePortIntrusionLock_Type = EnabledStatus
_PortOpModePortIntrusionLock_Object = MibTableColumn
portOpModePortIntrusionLock = _PortOpModePortIntrusionLock_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 6),
    _PortOpModePortIntrusionLock_Type()
)
portOpModePortIntrusionLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portOpModePortIntrusionLock.setStatus("mandatory")


class _PortOpModePortLBTestStatus_Type(Integer32):
    """Custom type portOpModePortLBTestStatus based on Integer32"""
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
        *(("none", 0),
          ("underTesting", 1),
          ("success", 2),
          ("fail", 3))
    )


_PortOpModePortLBTestStatus_Type.__name__ = "Integer32"
_PortOpModePortLBTestStatus_Object = MibTableColumn
portOpModePortLBTestStatus = _PortOpModePortLBTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 24, 1, 1, 7),
    _PortOpModePortLBTestStatus_Type()
)
portOpModePortLBTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOpModePortLBTestStatus.setStatus("mandatory")
_PortBasedVlanSetup_ObjectIdentity = ObjectIdentity
portBasedVlanSetup = _PortBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 25)
)
_PortBasedVlanPortListTable_Object = MibTable
portBasedVlanPortListTable = _PortBasedVlanPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 25, 1)
)
if mibBuilder.loadTexts:
    portBasedVlanPortListTable.setStatus("mandatory")
_PortBasedVlanPortListEntry_Object = MibTableRow
portBasedVlanPortListEntry = _PortBasedVlanPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 25, 1, 1)
)
portBasedVlanPortListEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    portBasedVlanPortListEntry.setStatus("mandatory")
_PortBasedVlanPortListMembers_Type = PortList
_PortBasedVlanPortListMembers_Object = MibTableColumn
portBasedVlanPortListMembers = _PortBasedVlanPortListMembers_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 25, 1, 1, 1),
    _PortBasedVlanPortListMembers_Type()
)
portBasedVlanPortListMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portBasedVlanPortListMembers.setStatus("mandatory")
_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1)
)
eventEntry.setIndexNames(
    (0, "ZYXEL-ES3124PWR-MIB", "eventSeqNum"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventSeqNum_Type = Integer32
_EventSeqNum_Object = MibTableColumn
eventSeqNum = _EventSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 1),
    _EventSeqNum_Type()
)
eventSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeqNum.setStatus("current")
_EventEventId_Type = EventIdNumber
_EventEventId_Object = MibTableColumn
eventEventId = _EventEventId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 2),
    _EventEventId_Type()
)
eventEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventEventId.setStatus("current")


class _EventName_Type(DisplayString):
    """Custom type eventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EventName_Type.__name__ = "DisplayString"
_EventName_Object = MibTableColumn
eventName = _EventName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 3),
    _EventName_Type()
)
eventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventName.setStatus("current")
_EventInstanceType_Type = InstanceType
_EventInstanceType_Object = MibTableColumn
eventInstanceType = _EventInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 4),
    _EventInstanceType_Type()
)
eventInstanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceType.setStatus("current")
_EventInstanceId_Type = DisplayString
_EventInstanceId_Object = MibTableColumn
eventInstanceId = _EventInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 5),
    _EventInstanceId_Type()
)
eventInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceId.setStatus("current")
_EventInstanceName_Type = DisplayString
_EventInstanceName_Object = MibTableColumn
eventInstanceName = _EventInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 6),
    _EventInstanceName_Type()
)
eventInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInstanceName.setStatus("current")
_EventSeverity_Type = EventSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventSetTime_Type = UtcTimeStamp
_EventSetTime_Object = MibTableColumn
eventSetTime = _EventSetTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 8),
    _EventSetTime_Type()
)
eventSetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSetTime.setStatus("current")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 9),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
_EventServAffective_Type = EventServiceAffective
_EventServAffective_Object = MibTableColumn
eventServAffective = _EventServAffective_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 26, 1, 1, 1, 10),
    _EventServAffective_Type()
)
eventServAffective.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventServAffective.setStatus("current")
_TrapInfoObjects_ObjectIdentity = ObjectIdentity
trapInfoObjects = _TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 1)
)
_TrapRefSeqNum_Type = Integer32
_TrapRefSeqNum_Object = MibScalar
trapRefSeqNum = _TrapRefSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 1, 1),
    _TrapRefSeqNum_Type()
)
trapRefSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRefSeqNum.setStatus("current")
_TrapPersistence_Type = EventPersistence
_TrapPersistence_Object = MibScalar
trapPersistence = _TrapPersistence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 1, 2),
    _TrapPersistence_Type()
)
trapPersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapPersistence.setStatus("current")
_TrapSenderNodeId_Type = Integer32
_TrapSenderNodeId_Object = MibScalar
trapSenderNodeId = _TrapSenderNodeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 1, 3),
    _TrapSenderNodeId_Type()
)
trapSenderNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSenderNodeId.setStatus("current")
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 2)
)

# Managed Objects groups


# Notification objects

eventOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 2, 1)
)
eventOnTrap.setObjects(
      *(("ZYXEL-ES3124PWR-MIB", "eventSeqNum"),
        ("ZYXEL-ES3124PWR-MIB", "eventEventId"),
        ("ZYXEL-ES3124PWR-MIB", "eventName"),
        ("ZYXEL-ES3124PWR-MIB", "eventSetTime"),
        ("ZYXEL-ES3124PWR-MIB", "eventSeverity"),
        ("ZYXEL-ES3124PWR-MIB", "eventInstanceType"),
        ("ZYXEL-ES3124PWR-MIB", "eventInstanceId"),
        ("ZYXEL-ES3124PWR-MIB", "eventInstanceName"),
        ("ZYXEL-ES3124PWR-MIB", "eventServAffective"),
        ("ZYXEL-ES3124PWR-MIB", "eventDescription"),
        ("ZYXEL-ES3124PWR-MIB", "trapPersistence"),
        ("ZYXEL-ES3124PWR-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventOnTrap.setStatus(
        "current"
    )

eventClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 8, 14, 27, 2, 2)
)
eventClearedTrap.setObjects(
      *(("ZYXEL-ES3124PWR-MIB", "eventSeqNum"),
        ("ZYXEL-ES3124PWR-MIB", "eventEventId"),
        ("ZYXEL-ES3124PWR-MIB", "eventSetTime"),
        ("ZYXEL-ES3124PWR-MIB", "eventInstanceType"),
        ("ZYXEL-ES3124PWR-MIB", "eventInstanceId"),
        ("ZYXEL-ES3124PWR-MIB", "trapRefSeqNum"),
        ("ZYXEL-ES3124PWR-MIB", "trapSenderNodeId"),
        ("SNMPv2-MIB", "sysObjectID"))
)
if mibBuilder.loadTexts:
    eventClearedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ES3124PWR-MIB",
    **{"UtcTimeStamp": UtcTimeStamp,
       "EventIdNumber": EventIdNumber,
       "EventSeverity": EventSeverity,
       "EventServiceAffective": EventServiceAffective,
       "InstanceType": InstanceType,
       "EventPersistence": EventPersistence,
       "zyxel": zyxel,
       "products": products,
       "accessSwitch": accessSwitch,
       "esSeries": esSeries,
       "es3124pwr": es3124pwr,
       "sysInfo": sysInfo,
       "sysSwPlatformMajorVers": sysSwPlatformMajorVers,
       "sysSwPlatformMinorVers": sysSwPlatformMinorVers,
       "sysSwModelString": sysSwModelString,
       "sysSwVersionControlNbr": sysSwVersionControlNbr,
       "sysSwDay": sysSwDay,
       "sysSwMonth": sysSwMonth,
       "sysSwYear": sysSwYear,
       "sysHwMajorVers": sysHwMajorVers,
       "sysHwMinorVers": sysHwMinorVers,
       "sysSerialNumber": sysSerialNumber,
       "rateLimitSetup": rateLimitSetup,
       "rateLimitState": rateLimitState,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rateLimitPortState": rateLimitPortState,
       "rateLimitPortIngRate": rateLimitPortIngRate,
       "rateLimitPortEgrRate": rateLimitPortEgrRate,
       "brLimitSetup": brLimitSetup,
       "brLimitState": brLimitState,
       "brLimitPortTable": brLimitPortTable,
       "brLimitPortEntry": brLimitPortEntry,
       "brLimitPortBrState": brLimitPortBrState,
       "brLimitPortBrRate": brLimitPortBrRate,
       "brLimitPortMcState": brLimitPortMcState,
       "brLimitPortMcRate": brLimitPortMcRate,
       "brLimitPortDlfState": brLimitPortDlfState,
       "brLimitPortDlfRate": brLimitPortDlfRate,
       "portSecuritySetup": portSecuritySetup,
       "portSecurityState": portSecurityState,
       "portSecurityPortTable": portSecurityPortTable,
       "portSecurityPortEntry": portSecurityPortEntry,
       "portSecurityPortState": portSecurityPortState,
       "portSecurityPortLearnState": portSecurityPortLearnState,
       "portSecurityPortCount": portSecurityPortCount,
       "portSecurityMacFreeze": portSecurityMacFreeze,
       "vlanTrunkSetup": vlanTrunkSetup,
       "vlanTrunkPortTable": vlanTrunkPortTable,
       "vlanTrunkPortEntry": vlanTrunkPortEntry,
       "vlanTrunkPortState": vlanTrunkPortState,
       "ctlProtTransSetup": ctlProtTransSetup,
       "ctlProtTransState": ctlProtTransState,
       "ctlProtTransTunnelPortTable": ctlProtTransTunnelPortTable,
       "ctlProtTransTunnelPortEntry": ctlProtTransTunnelPortEntry,
       "ctlProtTransTunnelMode": ctlProtTransTunnelMode,
       "vlanStackSetup": vlanStackSetup,
       "vlanStackState": vlanStackState,
       "vlanStackTpid": vlanStackTpid,
       "vlanStackPortTable": vlanStackPortTable,
       "vlanStackPortEntry": vlanStackPortEntry,
       "vlanStackPortMode": vlanStackPortMode,
       "vlanStackPortVid": vlanStackPortVid,
       "vlanStackPortPrio": vlanStackPortPrio,
       "radius8021xSetup": radius8021xSetup,
       "radiusLoginPrecedence": radiusLoginPrecedence,
       "radiusAnd8021xServer": radiusAnd8021xServer,
       "radiusIpAddr": radiusIpAddr,
       "radiusUdpPort": radiusUdpPort,
       "radiusSharedSecret": radiusSharedSecret,
       "portAuthState": portAuthState,
       "portAuthTable": portAuthTable,
       "portAuthEntry": portAuthEntry,
       "portAuthEntryState": portAuthEntryState,
       "portReAuthEntryState": portReAuthEntryState,
       "portReAuthEntryTimer": portReAuthEntryTimer,
       "hwMonitorInfo": hwMonitorInfo,
       "fanRpmTable": fanRpmTable,
       "fanRpmEntry": fanRpmEntry,
       "fanRpmIndex": fanRpmIndex,
       "fanRpmCurValue": fanRpmCurValue,
       "fanRpmMaxValue": fanRpmMaxValue,
       "fanRpmMinValue": fanRpmMinValue,
       "fanRpmLowThresh": fanRpmLowThresh,
       "fanRpmDescr": fanRpmDescr,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempCurValue": tempCurValue,
       "tempMaxValue": tempMaxValue,
       "tempMinValue": tempMinValue,
       "tempHighThresh": tempHighThresh,
       "tempDescr": tempDescr,
       "voltageTable": voltageTable,
       "voltageEntry": voltageEntry,
       "voltageIndex": voltageIndex,
       "voltageCurValue": voltageCurValue,
       "voltageMaxValue": voltageMaxValue,
       "voltageMinValue": voltageMinValue,
       "voltageNominalValue": voltageNominalValue,
       "voltageLowThresh": voltageLowThresh,
       "voltageDescr": voltageDescr,
       "snmpSetup": snmpSetup,
       "snmpGetCommunity": snmpGetCommunity,
       "snmpSetCommunity": snmpSetCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapDestTable": snmpTrapDestTable,
       "snmpTrapDestEntry": snmpTrapDestEntry,
       "snmpTrapDestIP": snmpTrapDestIP,
       "snmpTrapDestRowStatus": snmpTrapDestRowStatus,
       "dateTimeServerSetup": dateTimeServerSetup,
       "dateTimeServerType": dateTimeServerType,
       "dateTimeServerIP": dateTimeServerIP,
       "dateTimeZone": dateTimeZone,
       "dateTimeNewDateYear": dateTimeNewDateYear,
       "dateTimeNewDateMonth": dateTimeNewDateMonth,
       "dateTimeNewDateDay": dateTimeNewDateDay,
       "dateTimeNewTimeHour": dateTimeNewTimeHour,
       "dateTimeNewTimeMinute": dateTimeNewTimeMinute,
       "dateTimeNewTimeSecond": dateTimeNewTimeSecond,
       "sysMgmt": sysMgmt,
       "sysMgmtConfigSave": sysMgmtConfigSave,
       "sysMgmtBootupConfig": sysMgmtBootupConfig,
       "sysMgmtReboot": sysMgmtReboot,
       "sysMgmtDefaultConfig": sysMgmtDefaultConfig,
       "sysMgmtLastActionStatus": sysMgmtLastActionStatus,
       "sysMgmtSystemStatus": sysMgmtSystemStatus,
       "layer2Setup": layer2Setup,
       "vlanTypeSetup": vlanTypeSetup,
       "igmpSnoopingStateSetup": igmpSnoopingStateSetup,
       "tagVlanPortIsolationState": tagVlanPortIsolationState,
       "stpState": stpState,
       "ipSetup": ipSetup,
       "dnsIpAddress": dnsIpAddress,
       "defaultMgmt": defaultMgmt,
       "inbandIpSetup": inbandIpSetup,
       "inbandIpType": inbandIpType,
       "inbandVid": inbandVid,
       "inbandStaticIp": inbandStaticIp,
       "inbandStaticSubnetMask": inbandStaticSubnetMask,
       "inbandStaticGateway": inbandStaticGateway,
       "outOfBandIpSetup": outOfBandIpSetup,
       "outOfBandIp": outOfBandIp,
       "outOfBandSubnetMask": outOfBandSubnetMask,
       "outOfBandGateway": outOfBandGateway,
       "maxNumOfInbandIp": maxNumOfInbandIp,
       "inbandIpTable": inbandIpTable,
       "inbandIpEntry": inbandIpEntry,
       "inbandEntryIp": inbandEntryIp,
       "inbandEntrySubnetMask": inbandEntrySubnetMask,
       "inbandEntryGateway": inbandEntryGateway,
       "inbandEntryVid": inbandEntryVid,
       "inbandEntryManageable": inbandEntryManageable,
       "inbandEntryRowStatus": inbandEntryRowStatus,
       "filterSetup": filterSetup,
       "filterTable": filterTable,
       "filterEntry": filterEntry,
       "filterName": filterName,
       "filterActionState": filterActionState,
       "filterMacAddr": filterMacAddr,
       "filterVid": filterVid,
       "filterRowStatus": filterRowStatus,
       "mirrorSetup": mirrorSetup,
       "mirrorState": mirrorState,
       "mirrorMonitorPort": mirrorMonitorPort,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorMirroredState": mirrorMirroredState,
       "mirrorDirection": mirrorDirection,
       "aggrSetup": aggrSetup,
       "aggrState": aggrState,
       "aggrSystemPriority": aggrSystemPriority,
       "aggrGroupTable": aggrGroupTable,
       "aggrGroupEntry": aggrGroupEntry,
       "aggrGroupIndex": aggrGroupIndex,
       "aggrGroupState": aggrGroupState,
       "aggrGroupDynamicState": aggrGroupDynamicState,
       "aggrPortTable": aggrPortTable,
       "aggrPortEntry": aggrPortEntry,
       "aggrPortGroup": aggrPortGroup,
       "aggrPortDynamicStateTimeout": aggrPortDynamicStateTimeout,
       "accessCtlSetup": accessCtlSetup,
       "accessCtlTable": accessCtlTable,
       "accessCtlEntry": accessCtlEntry,
       "accessCtlService": accessCtlService,
       "accessCtlEnable": accessCtlEnable,
       "accessCtlServicePort": accessCtlServicePort,
       "accessCtlTimeout": accessCtlTimeout,
       "securedClientTable": securedClientTable,
       "securedClientEntry": securedClientEntry,
       "securedClientIndex": securedClientIndex,
       "securedClientEnable": securedClientEnable,
       "securedClientStartIp": securedClientStartIp,
       "securedClientEndIp": securedClientEndIp,
       "securedClientService": securedClientService,
       "queuingMethodSetup": queuingMethodSetup,
       "queuingMethodType": queuingMethodType,
       "portQueuingMethodTable": portQueuingMethodTable,
       "portQueuingMethodEntry": portQueuingMethodEntry,
       "portQueuingMethodQueue": portQueuingMethodQueue,
       "portQueuingMethodWeight": portQueuingMethodWeight,
       "dhcpSetup": dhcpSetup,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayEnable": dhcpRelayEnable,
       "dhcpRelayOption82Enable": dhcpRelayOption82Enable,
       "dhcpRelayInfoEnable": dhcpRelayInfoEnable,
       "dhcpRelayInfoData": dhcpRelayInfoData,
       "maxNumberOfDhcpRemoteServer": maxNumberOfDhcpRemoteServer,
       "dhcpRemoteServerTable": dhcpRemoteServerTable,
       "dhcpRemoteServerEntry": dhcpRemoteServerEntry,
       "dhcpRemoteServerIp": dhcpRemoteServerIp,
       "dhcpRemoteServerRowStatus": dhcpRemoteServerRowStatus,
       "staticRouteSetup": staticRouteSetup,
       "maxNumberOfStaticRoutes": maxNumberOfStaticRoutes,
       "staticRouteTable": staticRouteTable,
       "staticRouteEntry": staticRouteEntry,
       "staticRouteName": staticRouteName,
       "staticRouteIp": staticRouteIp,
       "staticRouteMask": staticRouteMask,
       "staticRouteGateway": staticRouteGateway,
       "staticRouteMetric": staticRouteMetric,
       "staticRouteRowStatus": staticRouteRowStatus,
       "arpInfo": arpInfo,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpIndex": arpIndex,
       "arpIpAddr": arpIpAddr,
       "arpMacAddr": arpMacAddr,
       "arpMacVid": arpMacVid,
       "arpType": arpType,
       "pltMgmt": pltMgmt,
       "pltCtlTable": pltCtlTable,
       "pltCtlEntry": pltCtlEntry,
       "pltCtlInstType": pltCtlInstType,
       "pltCtlInstId": pltCtlInstId,
       "pltCtlIpAddr": pltCtlIpAddr,
       "pltCtlMask": pltCtlMask,
       "pltCtlGw": pltCtlGw,
       "pltCtlRowStatus": pltCtlRowStatus,
       "pingCtlTable": pingCtlTable,
       "pingCtlEntry": pingCtlEntry,
       "pingCtlServInstType": pingCtlServInstType,
       "pingCtlServInstId": pingCtlServInstId,
       "pingCtlOwnerIndex": pingCtlOwnerIndex,
       "pingCtlTestName": pingCtlTestName,
       "pingCtlTargetAddressType": pingCtlTargetAddressType,
       "pingCtlTargetAddress": pingCtlTargetAddress,
       "pingCtlDataSize": pingCtlDataSize,
       "pingCtlTimeOut": pingCtlTimeOut,
       "pingCtlProbeCount": pingCtlProbeCount,
       "pingCtlAdminStatus": pingCtlAdminStatus,
       "pingCtlDataFill": pingCtlDataFill,
       "pingCtlFrequency": pingCtlFrequency,
       "pingCtlMaxRows": pingCtlMaxRows,
       "pingCtlStorageType": pingCtlStorageType,
       "pingCtlTrapGeneration": pingCtlTrapGeneration,
       "pingCtlTrapProbeFailureFilter": pingCtlTrapProbeFailureFilter,
       "pingCtlTrapTestFailureFilter": pingCtlTrapTestFailureFilter,
       "pingCtlType": pingCtlType,
       "pingCtlDescr": pingCtlDescr,
       "pingCtlSourceAddressType": pingCtlSourceAddressType,
       "pingCtlSourceAddress": pingCtlSourceAddress,
       "pingCtlIfIndex": pingCtlIfIndex,
       "pingCtlByPassRouteTable": pingCtlByPassRouteTable,
       "pingCtlDSField": pingCtlDSField,
       "pingCtlRowStatus": pingCtlRowStatus,
       "pingResultsTable": pingResultsTable,
       "pingResultsEntry": pingResultsEntry,
       "pingResultsOperStatus": pingResultsOperStatus,
       "pingResultsIpTargetAddressType": pingResultsIpTargetAddressType,
       "pingResultsIpTargetAddress": pingResultsIpTargetAddress,
       "pingResultsMinRtt": pingResultsMinRtt,
       "pingResultsMaxRtt": pingResultsMaxRtt,
       "pingResultsAverageRtt": pingResultsAverageRtt,
       "pingResultsProbeResponses": pingResultsProbeResponses,
       "pingResultsSentProbes": pingResultsSentProbes,
       "pingResultsRttSumOfSquares": pingResultsRttSumOfSquares,
       "pingResultsLastGoodProbe": pingResultsLastGoodProbe,
       "pingProbeHistoryTable": pingProbeHistoryTable,
       "pingProbeHistoryEntry": pingProbeHistoryEntry,
       "pingProbeHistoryIndex": pingProbeHistoryIndex,
       "pingProbeHistoryResponse": pingProbeHistoryResponse,
       "pingProbeHistoryStatus": pingProbeHistoryStatus,
       "pingProbeHistoryLastRC": pingProbeHistoryLastRC,
       "pingProbeHistoryTime": pingProbeHistoryTime,
       "traceRouteCtlTable": traceRouteCtlTable,
       "traceRouteCtlEntry": traceRouteCtlEntry,
       "traceRouteCtlServInstType": traceRouteCtlServInstType,
       "traceRouteCtlServInstId": traceRouteCtlServInstId,
       "traceRouteCtlOwnerIndex": traceRouteCtlOwnerIndex,
       "traceRouteCtlTestName": traceRouteCtlTestName,
       "traceRouteCtlTargetAddressType": traceRouteCtlTargetAddressType,
       "traceRouteCtlTargetAddress": traceRouteCtlTargetAddress,
       "traceRouteCtlByPassRouteTable": traceRouteCtlByPassRouteTable,
       "traceRouteCtlDataSize": traceRouteCtlDataSize,
       "traceRouteCtlTimeOut": traceRouteCtlTimeOut,
       "traceRouteCtlProbesPerHop": traceRouteCtlProbesPerHop,
       "traceRouteCtlPort": traceRouteCtlPort,
       "traceRouteCtlMaxTtl": traceRouteCtlMaxTtl,
       "traceRouteCtlDSField": traceRouteCtlDSField,
       "traceRouteCtlSourceAddressType": traceRouteCtlSourceAddressType,
       "traceRouteCtlSourceAddress": traceRouteCtlSourceAddress,
       "traceRouteCtlIfIndex": traceRouteCtlIfIndex,
       "traceRouteCtlMiscOptions": traceRouteCtlMiscOptions,
       "traceRouteCtlMaxFailures": traceRouteCtlMaxFailures,
       "traceRouteCtlDontFragment": traceRouteCtlDontFragment,
       "traceRouteCtlInitialTtl": traceRouteCtlInitialTtl,
       "traceRouteCtlFrequency": traceRouteCtlFrequency,
       "traceRouteCtlStorageType": traceRouteCtlStorageType,
       "traceRouteCtlAdminStatus": traceRouteCtlAdminStatus,
       "traceRouteCtlDescr": traceRouteCtlDescr,
       "traceRouteCtlMaxRows": traceRouteCtlMaxRows,
       "traceRouteCtlTrapGeneration": traceRouteCtlTrapGeneration,
       "traceRouteCtlCreateHopsEntries": traceRouteCtlCreateHopsEntries,
       "traceRouteCtlType": traceRouteCtlType,
       "traceRouteCtlRowStatus": traceRouteCtlRowStatus,
       "traceRouteResultsTable": traceRouteResultsTable,
       "traceRouteResultsEntry": traceRouteResultsEntry,
       "traceRouteResultsOperStatus": traceRouteResultsOperStatus,
       "traceRouteResultsCurHopCount": traceRouteResultsCurHopCount,
       "traceRouteResultsCurProbeCount": traceRouteResultsCurProbeCount,
       "traceRouteResultsIpTgtAddrType": traceRouteResultsIpTgtAddrType,
       "traceRouteResultsIpTgtAddr": traceRouteResultsIpTgtAddr,
       "traceRouteResultsTestAttempts": traceRouteResultsTestAttempts,
       "traceRouteResultsTestSuccesses": traceRouteResultsTestSuccesses,
       "traceRouteResultsLastGoodPath": traceRouteResultsLastGoodPath,
       "traceRouteProbeHistoryTable": traceRouteProbeHistoryTable,
       "traceRouteProbeHistoryEntry": traceRouteProbeHistoryEntry,
       "traceRouteProbeHistoryIndex": traceRouteProbeHistoryIndex,
       "traceRouteProbeHistoryHopIndex": traceRouteProbeHistoryHopIndex,
       "traceRouteProbeHistoryProbeIndex": traceRouteProbeHistoryProbeIndex,
       "traceRouteProbeHistoryHAddrType": traceRouteProbeHistoryHAddrType,
       "traceRouteProbeHistoryHAddr": traceRouteProbeHistoryHAddr,
       "traceRouteProbeHistoryResponse": traceRouteProbeHistoryResponse,
       "traceRouteProbeHistoryStatus": traceRouteProbeHistoryStatus,
       "traceRouteProbeHistoryLastRC": traceRouteProbeHistoryLastRC,
       "traceRouteProbeHistoryTime": traceRouteProbeHistoryTime,
       "traceRouteHopsTable": traceRouteHopsTable,
       "traceRouteHopsEntry": traceRouteHopsEntry,
       "traceRouteHopsHopIndex": traceRouteHopsHopIndex,
       "traceRouteHopsIpTgtAddressType": traceRouteHopsIpTgtAddressType,
       "traceRouteHopsIpTgtAddress": traceRouteHopsIpTgtAddress,
       "traceRouteHopsMinRtt": traceRouteHopsMinRtt,
       "traceRouteHopsMaxRtt": traceRouteHopsMaxRtt,
       "traceRouteHopsAverageRtt": traceRouteHopsAverageRtt,
       "traceRouteHopsRttSumOfSquares": traceRouteHopsRttSumOfSquares,
       "traceRouteHopsSentProbes": traceRouteHopsSentProbes,
       "traceRouteHopsProbeResponses": traceRouteHopsProbeResponses,
       "traceRouteHopsLastGoodProbe": traceRouteHopsLastGoodProbe,
       "portOpModeSetup": portOpModeSetup,
       "portOpModePortTable": portOpModePortTable,
       "portOpModePortEntry": portOpModePortEntry,
       "portOpModePortSpeedDuplex": portOpModePortSpeedDuplex,
       "portOpModePortFlowCntl": portOpModePortFlowCntl,
       "portOpModePortName": portOpModePortName,
       "portOpModePortModuleType": portOpModePortModuleType,
       "portOpModePortLinkUpType": portOpModePortLinkUpType,
       "portOpModePortIntrusionLock": portOpModePortIntrusionLock,
       "portOpModePortLBTestStatus": portOpModePortLBTestStatus,
       "portBasedVlanSetup": portBasedVlanSetup,
       "portBasedVlanPortListTable": portBasedVlanPortListTable,
       "portBasedVlanPortListEntry": portBasedVlanPortListEntry,
       "portBasedVlanPortListMembers": portBasedVlanPortListMembers,
       "faultMIB": faultMIB,
       "eventObjects": eventObjects,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventSeqNum": eventSeqNum,
       "eventEventId": eventEventId,
       "eventName": eventName,
       "eventInstanceType": eventInstanceType,
       "eventInstanceId": eventInstanceId,
       "eventInstanceName": eventInstanceName,
       "eventSeverity": eventSeverity,
       "eventSetTime": eventSetTime,
       "eventDescription": eventDescription,
       "eventServAffective": eventServAffective,
       "faultTrapsMIB": faultTrapsMIB,
       "trapInfoObjects": trapInfoObjects,
       "trapRefSeqNum": trapRefSeqNum,
       "trapPersistence": trapPersistence,
       "trapSenderNodeId": trapSenderNodeId,
       "trapNotifications": trapNotifications,
       "eventOnTrap": eventOnTrap,
       "eventClearedTrap": eventClearedTrap}
)
