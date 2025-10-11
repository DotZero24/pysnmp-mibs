# SNMP MIB module (MX-NFW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-NFW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:39 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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


# MODULE-IDENTITY

nfwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NfwMIBObjects_ObjectIdentity = ObjectIdentity
nfwMIBObjects = _NfwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1)
)


class _ConfigModifiedStatus_Type(Integer32):
    """Custom type configModifiedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("yes", 100),
          ("no", 200))
    )


_ConfigModifiedStatus_Type.__name__ = "Integer32"
_ConfigModifiedStatus_Object = MibScalar
configModifiedStatus = _ConfigModifiedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 100),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")
_NetworkRulesStatusTable_Object = MibTable
networkRulesStatusTable = _NetworkRulesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200)
)
if mibBuilder.loadTexts:
    networkRulesStatusTable.setStatus("current")
_NetworkRulesStatusEntry_Object = MibTableRow
networkRulesStatusEntry = _NetworkRulesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1)
)
networkRulesStatusEntry.setIndexNames(
    (0, "MX-NFW-MIB", "networkRulesStatusPriority"),
)
if mibBuilder.loadTexts:
    networkRulesStatusEntry.setStatus("current")
_NetworkRulesStatusPriority_Type = Unsigned32
_NetworkRulesStatusPriority_Object = MibTableColumn
networkRulesStatusPriority = _NetworkRulesStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 100),
    _NetworkRulesStatusPriority_Type()
)
networkRulesStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusPriority.setStatus("current")
_NetworkRulesStatusSourceAddress_Type = OctetString
_NetworkRulesStatusSourceAddress_Object = MibTableColumn
networkRulesStatusSourceAddress = _NetworkRulesStatusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 200),
    _NetworkRulesStatusSourceAddress_Type()
)
networkRulesStatusSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusSourceAddress.setStatus("current")
_NetworkRulesStatusSourcePort_Type = OctetString
_NetworkRulesStatusSourcePort_Object = MibTableColumn
networkRulesStatusSourcePort = _NetworkRulesStatusSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 300),
    _NetworkRulesStatusSourcePort_Type()
)
networkRulesStatusSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusSourcePort.setStatus("current")
_NetworkRulesStatusDestinationAddress_Type = OctetString
_NetworkRulesStatusDestinationAddress_Object = MibTableColumn
networkRulesStatusDestinationAddress = _NetworkRulesStatusDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 400),
    _NetworkRulesStatusDestinationAddress_Type()
)
networkRulesStatusDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusDestinationAddress.setStatus("current")
_NetworkRulesStatusDestinationPort_Type = OctetString
_NetworkRulesStatusDestinationPort_Object = MibTableColumn
networkRulesStatusDestinationPort = _NetworkRulesStatusDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 500),
    _NetworkRulesStatusDestinationPort_Type()
)
networkRulesStatusDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusDestinationPort.setStatus("current")


class _NetworkRulesStatusProtocol_Type(Integer32):
    """Custom type networkRulesStatusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tcp", 200),
          ("udp", 300),
          ("icmp", 400))
    )


_NetworkRulesStatusProtocol_Type.__name__ = "Integer32"
_NetworkRulesStatusProtocol_Object = MibTableColumn
networkRulesStatusProtocol = _NetworkRulesStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 600),
    _NetworkRulesStatusProtocol_Type()
)
networkRulesStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusProtocol.setStatus("current")


class _NetworkRulesStatusConnectionState_Type(Integer32):
    """Custom type networkRulesStatusConnectionState based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("new", 200),
          ("establishedOrRelated", 300))
    )


_NetworkRulesStatusConnectionState_Type.__name__ = "Integer32"
_NetworkRulesStatusConnectionState_Object = MibTableColumn
networkRulesStatusConnectionState = _NetworkRulesStatusConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 650),
    _NetworkRulesStatusConnectionState_Type()
)
networkRulesStatusConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusConnectionState.setStatus("current")
_NetworkRulesStatusBlacklistEnable_Type = MxEnableState
_NetworkRulesStatusBlacklistEnable_Object = MibTableColumn
networkRulesStatusBlacklistEnable = _NetworkRulesStatusBlacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 660),
    _NetworkRulesStatusBlacklistEnable_Type()
)
networkRulesStatusBlacklistEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusBlacklistEnable.setStatus("current")


class _NetworkRulesStatusRateLimitValue_Type(Unsigned32):
    """Custom type networkRulesStatusRateLimitValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_NetworkRulesStatusRateLimitValue_Type.__name__ = "Unsigned32"
_NetworkRulesStatusRateLimitValue_Object = MibTableColumn
networkRulesStatusRateLimitValue = _NetworkRulesStatusRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 670),
    _NetworkRulesStatusRateLimitValue_Type()
)
networkRulesStatusRateLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusRateLimitValue.setStatus("current")


class _NetworkRulesStatusRateLimitTimePeriod_Type(Unsigned32):
    """Custom type networkRulesStatusRateLimitTimePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_NetworkRulesStatusRateLimitTimePeriod_Type.__name__ = "Unsigned32"
_NetworkRulesStatusRateLimitTimePeriod_Object = MibTableColumn
networkRulesStatusRateLimitTimePeriod = _NetworkRulesStatusRateLimitTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 680),
    _NetworkRulesStatusRateLimitTimePeriod_Type()
)
networkRulesStatusRateLimitTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusRateLimitTimePeriod.setStatus("current")


class _NetworkRulesStatusAction_Type(Integer32):
    """Custom type networkRulesStatusAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("accept", 100),
          ("reject", 200),
          ("drop", 300),
          ("rateLimitPerSource", 400))
    )


_NetworkRulesStatusAction_Type.__name__ = "Integer32"
_NetworkRulesStatusAction_Object = MibTableColumn
networkRulesStatusAction = _NetworkRulesStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 200, 1, 700),
    _NetworkRulesStatusAction_Type()
)
networkRulesStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesStatusAction.setStatus("current")


class _DefaultPolicy_Type(Integer32):
    """Custom type defaultPolicy based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              300)
        )
    )
    namedValues = NamedValues(
        *(("accept", 100),
          ("drop", 300))
    )


_DefaultPolicy_Type.__name__ = "Integer32"
_DefaultPolicy_Object = MibScalar
defaultPolicy = _DefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 550),
    _DefaultPolicy_Type()
)
defaultPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultPolicy.setStatus("current")
_NetworkRulesTable_Object = MibTable
networkRulesTable = _NetworkRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600)
)
if mibBuilder.loadTexts:
    networkRulesTable.setStatus("current")
_NetworkRulesEntry_Object = MibTableRow
networkRulesEntry = _NetworkRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1)
)
networkRulesEntry.setIndexNames(
    (0, "MX-NFW-MIB", "networkRulesPriority"),
)
if mibBuilder.loadTexts:
    networkRulesEntry.setStatus("current")
_NetworkRulesPriority_Type = Unsigned32
_NetworkRulesPriority_Object = MibTableColumn
networkRulesPriority = _NetworkRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 100),
    _NetworkRulesPriority_Type()
)
networkRulesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkRulesPriority.setStatus("current")


class _NetworkRulesActivation_Type(MxEnableState):
    """Custom type networkRulesActivation based on MxEnableState"""
    defaultValue = 0


_NetworkRulesActivation_Type.__name__ = "MxEnableState"
_NetworkRulesActivation_Object = MibTableColumn
networkRulesActivation = _NetworkRulesActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 200),
    _NetworkRulesActivation_Type()
)
networkRulesActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesActivation.setStatus("current")


class _NetworkRulesSourceAddress_Type(OctetString):
    """Custom type networkRulesSourceAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_NetworkRulesSourceAddress_Type.__name__ = "OctetString"
_NetworkRulesSourceAddress_Object = MibTableColumn
networkRulesSourceAddress = _NetworkRulesSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 300),
    _NetworkRulesSourceAddress_Type()
)
networkRulesSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesSourceAddress.setStatus("current")


class _NetworkRulesSourcePort_Type(OctetString):
    """Custom type networkRulesSourcePort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_NetworkRulesSourcePort_Type.__name__ = "OctetString"
_NetworkRulesSourcePort_Object = MibTableColumn
networkRulesSourcePort = _NetworkRulesSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 400),
    _NetworkRulesSourcePort_Type()
)
networkRulesSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesSourcePort.setStatus("current")


class _NetworkRulesDestinationAddress_Type(OctetString):
    """Custom type networkRulesDestinationAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_NetworkRulesDestinationAddress_Type.__name__ = "OctetString"
_NetworkRulesDestinationAddress_Object = MibTableColumn
networkRulesDestinationAddress = _NetworkRulesDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 500),
    _NetworkRulesDestinationAddress_Type()
)
networkRulesDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesDestinationAddress.setStatus("current")


class _NetworkRulesDestinationPort_Type(OctetString):
    """Custom type networkRulesDestinationPort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_NetworkRulesDestinationPort_Type.__name__ = "OctetString"
_NetworkRulesDestinationPort_Object = MibTableColumn
networkRulesDestinationPort = _NetworkRulesDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 600),
    _NetworkRulesDestinationPort_Type()
)
networkRulesDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesDestinationPort.setStatus("current")


class _NetworkRulesProtocol_Type(Integer32):
    """Custom type networkRulesProtocol based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tcp", 200),
          ("udp", 300),
          ("icmp", 400))
    )


_NetworkRulesProtocol_Type.__name__ = "Integer32"
_NetworkRulesProtocol_Object = MibTableColumn
networkRulesProtocol = _NetworkRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 700),
    _NetworkRulesProtocol_Type()
)
networkRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesProtocol.setStatus("current")


class _NetworkRulesBlacklistEnable_Type(MxEnableState):
    """Custom type networkRulesBlacklistEnable based on MxEnableState"""
    defaultValue = 0


_NetworkRulesBlacklistEnable_Type.__name__ = "MxEnableState"
_NetworkRulesBlacklistEnable_Object = MibTableColumn
networkRulesBlacklistEnable = _NetworkRulesBlacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 720),
    _NetworkRulesBlacklistEnable_Type()
)
networkRulesBlacklistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesBlacklistEnable.setStatus("current")


class _NetworkRulesRateLimitValue_Type(Unsigned32):
    """Custom type networkRulesRateLimitValue based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_NetworkRulesRateLimitValue_Type.__name__ = "Unsigned32"
_NetworkRulesRateLimitValue_Object = MibTableColumn
networkRulesRateLimitValue = _NetworkRulesRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 730),
    _NetworkRulesRateLimitValue_Type()
)
networkRulesRateLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesRateLimitValue.setStatus("current")


class _NetworkRulesRateLimitTimePeriod_Type(Unsigned32):
    """Custom type networkRulesRateLimitTimePeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_NetworkRulesRateLimitTimePeriod_Type.__name__ = "Unsigned32"
_NetworkRulesRateLimitTimePeriod_Object = MibTableColumn
networkRulesRateLimitTimePeriod = _NetworkRulesRateLimitTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 740),
    _NetworkRulesRateLimitTimePeriod_Type()
)
networkRulesRateLimitTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesRateLimitTimePeriod.setStatus("current")


class _NetworkRulesConnectionState_Type(Integer32):
    """Custom type networkRulesConnectionState based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("new", 200),
          ("establishedOrRelated", 300))
    )


_NetworkRulesConnectionState_Type.__name__ = "Integer32"
_NetworkRulesConnectionState_Object = MibTableColumn
networkRulesConnectionState = _NetworkRulesConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 750),
    _NetworkRulesConnectionState_Type()
)
networkRulesConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesConnectionState.setStatus("current")


class _NetworkRulesAction_Type(Integer32):
    """Custom type networkRulesAction based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("accept", 100),
          ("reject", 200),
          ("drop", 300),
          ("rateLimitPerSource", 400))
    )


_NetworkRulesAction_Type.__name__ = "Integer32"
_NetworkRulesAction_Object = MibTableColumn
networkRulesAction = _NetworkRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 800),
    _NetworkRulesAction_Type()
)
networkRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesAction.setStatus("current")


class _NetworkRulesUp_Type(Integer32):
    """Custom type networkRulesUp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("up", 10))
    )


_NetworkRulesUp_Type.__name__ = "Integer32"
_NetworkRulesUp_Object = MibTableColumn
networkRulesUp = _NetworkRulesUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 900),
    _NetworkRulesUp_Type()
)
networkRulesUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesUp.setStatus("current")


class _NetworkRulesDown_Type(Integer32):
    """Custom type networkRulesDown based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("down", 10))
    )


_NetworkRulesDown_Type.__name__ = "Integer32"
_NetworkRulesDown_Object = MibTableColumn
networkRulesDown = _NetworkRulesDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 1000),
    _NetworkRulesDown_Type()
)
networkRulesDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesDown.setStatus("current")


class _NetworkRulesInsert_Type(Integer32):
    """Custom type networkRulesInsert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("insert", 10))
    )


_NetworkRulesInsert_Type.__name__ = "Integer32"
_NetworkRulesInsert_Object = MibTableColumn
networkRulesInsert = _NetworkRulesInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 1100),
    _NetworkRulesInsert_Type()
)
networkRulesInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesInsert.setStatus("current")


class _NetworkRulesDelete_Type(Integer32):
    """Custom type networkRulesDelete based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("delete", 10))
    )


_NetworkRulesDelete_Type.__name__ = "Integer32"
_NetworkRulesDelete_Object = MibTableColumn
networkRulesDelete = _NetworkRulesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 600, 1, 1200),
    _NetworkRulesDelete_Type()
)
networkRulesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkRulesDelete.setStatus("current")
_BlacklistGroup_ObjectIdentity = ObjectIdentity
blacklistGroup = _BlacklistGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 700)
)


class _BlacklistTimeout_Type(Unsigned32):
    """Custom type blacklistTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_BlacklistTimeout_Type.__name__ = "Unsigned32"
_BlacklistTimeout_Object = MibScalar
blacklistTimeout = _BlacklistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 700, 100),
    _BlacklistTimeout_Type()
)
blacklistTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blacklistTimeout.setStatus("current")


class _BlacklistRateLimitTimeout_Type(Unsigned32):
    """Custom type blacklistRateLimitTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_BlacklistRateLimitTimeout_Type.__name__ = "Unsigned32"
_BlacklistRateLimitTimeout_Object = MibScalar
blacklistRateLimitTimeout = _BlacklistRateLimitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 700, 200),
    _BlacklistRateLimitTimeout_Type()
)
blacklistRateLimitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blacklistRateLimitTimeout.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2250, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-NFW-MIB",
    **{"nfwMIB": nfwMIB,
       "nfwMIBObjects": nfwMIBObjects,
       "configModifiedStatus": configModifiedStatus,
       "networkRulesStatusTable": networkRulesStatusTable,
       "networkRulesStatusEntry": networkRulesStatusEntry,
       "networkRulesStatusPriority": networkRulesStatusPriority,
       "networkRulesStatusSourceAddress": networkRulesStatusSourceAddress,
       "networkRulesStatusSourcePort": networkRulesStatusSourcePort,
       "networkRulesStatusDestinationAddress": networkRulesStatusDestinationAddress,
       "networkRulesStatusDestinationPort": networkRulesStatusDestinationPort,
       "networkRulesStatusProtocol": networkRulesStatusProtocol,
       "networkRulesStatusConnectionState": networkRulesStatusConnectionState,
       "networkRulesStatusBlacklistEnable": networkRulesStatusBlacklistEnable,
       "networkRulesStatusRateLimitValue": networkRulesStatusRateLimitValue,
       "networkRulesStatusRateLimitTimePeriod": networkRulesStatusRateLimitTimePeriod,
       "networkRulesStatusAction": networkRulesStatusAction,
       "defaultPolicy": defaultPolicy,
       "networkRulesTable": networkRulesTable,
       "networkRulesEntry": networkRulesEntry,
       "networkRulesPriority": networkRulesPriority,
       "networkRulesActivation": networkRulesActivation,
       "networkRulesSourceAddress": networkRulesSourceAddress,
       "networkRulesSourcePort": networkRulesSourcePort,
       "networkRulesDestinationAddress": networkRulesDestinationAddress,
       "networkRulesDestinationPort": networkRulesDestinationPort,
       "networkRulesProtocol": networkRulesProtocol,
       "networkRulesBlacklistEnable": networkRulesBlacklistEnable,
       "networkRulesRateLimitValue": networkRulesRateLimitValue,
       "networkRulesRateLimitTimePeriod": networkRulesRateLimitTimePeriod,
       "networkRulesConnectionState": networkRulesConnectionState,
       "networkRulesAction": networkRulesAction,
       "networkRulesUp": networkRulesUp,
       "networkRulesDown": networkRulesDown,
       "networkRulesInsert": networkRulesInsert,
       "networkRulesDelete": networkRulesDelete,
       "blacklistGroup": blacklistGroup,
       "blacklistTimeout": blacklistTimeout,
       "blacklistRateLimitTimeout": blacklistRateLimitTimeout,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
