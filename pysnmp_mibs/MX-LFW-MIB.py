# SNMP MIB module (MX-LFW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-LFW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:33 2025
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

lfwMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LfwMIBObjects_ObjectIdentity = ObjectIdentity
lfwMIBObjects = _LfwMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 100),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")
_LocalRulesStatusTable_Object = MibTable
localRulesStatusTable = _LocalRulesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200)
)
if mibBuilder.loadTexts:
    localRulesStatusTable.setStatus("current")
_LocalRulesStatusEntry_Object = MibTableRow
localRulesStatusEntry = _LocalRulesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1)
)
localRulesStatusEntry.setIndexNames(
    (0, "MX-LFW-MIB", "localRulesStatusPriority"),
)
if mibBuilder.loadTexts:
    localRulesStatusEntry.setStatus("current")
_LocalRulesStatusPriority_Type = Unsigned32
_LocalRulesStatusPriority_Object = MibTableColumn
localRulesStatusPriority = _LocalRulesStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 100),
    _LocalRulesStatusPriority_Type()
)
localRulesStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusPriority.setStatus("current")
_LocalRulesStatusSourceAddress_Type = OctetString
_LocalRulesStatusSourceAddress_Object = MibTableColumn
localRulesStatusSourceAddress = _LocalRulesStatusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 200),
    _LocalRulesStatusSourceAddress_Type()
)
localRulesStatusSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusSourceAddress.setStatus("current")
_LocalRulesStatusSourcePort_Type = OctetString
_LocalRulesStatusSourcePort_Object = MibTableColumn
localRulesStatusSourcePort = _LocalRulesStatusSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 300),
    _LocalRulesStatusSourcePort_Type()
)
localRulesStatusSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusSourcePort.setStatus("current")
_LocalRulesStatusDestinationAddress_Type = OctetString
_LocalRulesStatusDestinationAddress_Object = MibTableColumn
localRulesStatusDestinationAddress = _LocalRulesStatusDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 400),
    _LocalRulesStatusDestinationAddress_Type()
)
localRulesStatusDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusDestinationAddress.setStatus("current")
_LocalRulesStatusDestinationPort_Type = OctetString
_LocalRulesStatusDestinationPort_Object = MibTableColumn
localRulesStatusDestinationPort = _LocalRulesStatusDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 500),
    _LocalRulesStatusDestinationPort_Type()
)
localRulesStatusDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusDestinationPort.setStatus("current")


class _LocalRulesStatusProtocol_Type(Integer32):
    """Custom type localRulesStatusProtocol based on Integer32"""
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


_LocalRulesStatusProtocol_Type.__name__ = "Integer32"
_LocalRulesStatusProtocol_Object = MibTableColumn
localRulesStatusProtocol = _LocalRulesStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 600),
    _LocalRulesStatusProtocol_Type()
)
localRulesStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusProtocol.setStatus("current")
_LocalRulesStatusBlacklistEnable_Type = MxEnableState
_LocalRulesStatusBlacklistEnable_Object = MibTableColumn
localRulesStatusBlacklistEnable = _LocalRulesStatusBlacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 620),
    _LocalRulesStatusBlacklistEnable_Type()
)
localRulesStatusBlacklistEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusBlacklistEnable.setStatus("current")


class _LocalRulesStatusRateLimitValue_Type(Unsigned32):
    """Custom type localRulesStatusRateLimitValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_LocalRulesStatusRateLimitValue_Type.__name__ = "Unsigned32"
_LocalRulesStatusRateLimitValue_Object = MibTableColumn
localRulesStatusRateLimitValue = _LocalRulesStatusRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 650),
    _LocalRulesStatusRateLimitValue_Type()
)
localRulesStatusRateLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusRateLimitValue.setStatus("current")


class _LocalRulesStatusRateLimitTimePeriod_Type(Unsigned32):
    """Custom type localRulesStatusRateLimitTimePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_LocalRulesStatusRateLimitTimePeriod_Type.__name__ = "Unsigned32"
_LocalRulesStatusRateLimitTimePeriod_Object = MibTableColumn
localRulesStatusRateLimitTimePeriod = _LocalRulesStatusRateLimitTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 680),
    _LocalRulesStatusRateLimitTimePeriod_Type()
)
localRulesStatusRateLimitTimePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusRateLimitTimePeriod.setStatus("current")


class _LocalRulesStatusAction_Type(Integer32):
    """Custom type localRulesStatusAction based on Integer32"""
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


_LocalRulesStatusAction_Type.__name__ = "Integer32"
_LocalRulesStatusAction_Object = MibTableColumn
localRulesStatusAction = _LocalRulesStatusAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 200, 1, 700),
    _LocalRulesStatusAction_Type()
)
localRulesStatusAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesStatusAction.setStatus("current")


class _DefaultPolicy_Type(Integer32):
    """Custom type defaultPolicy based on Integer32"""
    defaultValue = 100

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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 550),
    _DefaultPolicy_Type()
)
defaultPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultPolicy.setStatus("current")
_LocalRulesTable_Object = MibTable
localRulesTable = _LocalRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600)
)
if mibBuilder.loadTexts:
    localRulesTable.setStatus("current")
_LocalRulesEntry_Object = MibTableRow
localRulesEntry = _LocalRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1)
)
localRulesEntry.setIndexNames(
    (0, "MX-LFW-MIB", "localRulesPriority"),
)
if mibBuilder.loadTexts:
    localRulesEntry.setStatus("current")
_LocalRulesPriority_Type = Unsigned32
_LocalRulesPriority_Object = MibTableColumn
localRulesPriority = _LocalRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 100),
    _LocalRulesPriority_Type()
)
localRulesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localRulesPriority.setStatus("current")


class _LocalRulesActivation_Type(MxEnableState):
    """Custom type localRulesActivation based on MxEnableState"""
    defaultValue = 0


_LocalRulesActivation_Type.__name__ = "MxEnableState"
_LocalRulesActivation_Object = MibTableColumn
localRulesActivation = _LocalRulesActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 200),
    _LocalRulesActivation_Type()
)
localRulesActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesActivation.setStatus("current")


class _LocalRulesSourceAddress_Type(OctetString):
    """Custom type localRulesSourceAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_LocalRulesSourceAddress_Type.__name__ = "OctetString"
_LocalRulesSourceAddress_Object = MibTableColumn
localRulesSourceAddress = _LocalRulesSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 300),
    _LocalRulesSourceAddress_Type()
)
localRulesSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesSourceAddress.setStatus("current")


class _LocalRulesSourcePort_Type(OctetString):
    """Custom type localRulesSourcePort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_LocalRulesSourcePort_Type.__name__ = "OctetString"
_LocalRulesSourcePort_Object = MibTableColumn
localRulesSourcePort = _LocalRulesSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 400),
    _LocalRulesSourcePort_Type()
)
localRulesSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesSourcePort.setStatus("current")


class _LocalRulesDestinationAddress_Type(OctetString):
    """Custom type localRulesDestinationAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_LocalRulesDestinationAddress_Type.__name__ = "OctetString"
_LocalRulesDestinationAddress_Object = MibTableColumn
localRulesDestinationAddress = _LocalRulesDestinationAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 500),
    _LocalRulesDestinationAddress_Type()
)
localRulesDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesDestinationAddress.setStatus("current")


class _LocalRulesDestinationPort_Type(OctetString):
    """Custom type localRulesDestinationPort based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_LocalRulesDestinationPort_Type.__name__ = "OctetString"
_LocalRulesDestinationPort_Object = MibTableColumn
localRulesDestinationPort = _LocalRulesDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 600),
    _LocalRulesDestinationPort_Type()
)
localRulesDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesDestinationPort.setStatus("current")


class _LocalRulesProtocol_Type(Integer32):
    """Custom type localRulesProtocol based on Integer32"""
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


_LocalRulesProtocol_Type.__name__ = "Integer32"
_LocalRulesProtocol_Object = MibTableColumn
localRulesProtocol = _LocalRulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 700),
    _LocalRulesProtocol_Type()
)
localRulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesProtocol.setStatus("current")


class _LocalRulesBlacklistEnable_Type(MxEnableState):
    """Custom type localRulesBlacklistEnable based on MxEnableState"""
    defaultValue = 0


_LocalRulesBlacklistEnable_Type.__name__ = "MxEnableState"
_LocalRulesBlacklistEnable_Object = MibTableColumn
localRulesBlacklistEnable = _LocalRulesBlacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 720),
    _LocalRulesBlacklistEnable_Type()
)
localRulesBlacklistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesBlacklistEnable.setStatus("current")


class _LocalRulesRateLimitValue_Type(Unsigned32):
    """Custom type localRulesRateLimitValue based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_LocalRulesRateLimitValue_Type.__name__ = "Unsigned32"
_LocalRulesRateLimitValue_Object = MibTableColumn
localRulesRateLimitValue = _LocalRulesRateLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 750),
    _LocalRulesRateLimitValue_Type()
)
localRulesRateLimitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesRateLimitValue.setStatus("current")


class _LocalRulesRateLimitTimePeriod_Type(Unsigned32):
    """Custom type localRulesRateLimitTimePeriod based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_LocalRulesRateLimitTimePeriod_Type.__name__ = "Unsigned32"
_LocalRulesRateLimitTimePeriod_Object = MibTableColumn
localRulesRateLimitTimePeriod = _LocalRulesRateLimitTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 780),
    _LocalRulesRateLimitTimePeriod_Type()
)
localRulesRateLimitTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesRateLimitTimePeriod.setStatus("current")


class _LocalRulesAction_Type(Integer32):
    """Custom type localRulesAction based on Integer32"""
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


_LocalRulesAction_Type.__name__ = "Integer32"
_LocalRulesAction_Object = MibTableColumn
localRulesAction = _LocalRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 800),
    _LocalRulesAction_Type()
)
localRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesAction.setStatus("current")


class _LocalRulesUp_Type(Integer32):
    """Custom type localRulesUp based on Integer32"""
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


_LocalRulesUp_Type.__name__ = "Integer32"
_LocalRulesUp_Object = MibTableColumn
localRulesUp = _LocalRulesUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 900),
    _LocalRulesUp_Type()
)
localRulesUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesUp.setStatus("current")


class _LocalRulesDown_Type(Integer32):
    """Custom type localRulesDown based on Integer32"""
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


_LocalRulesDown_Type.__name__ = "Integer32"
_LocalRulesDown_Object = MibTableColumn
localRulesDown = _LocalRulesDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 1000),
    _LocalRulesDown_Type()
)
localRulesDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesDown.setStatus("current")


class _LocalRulesInsert_Type(Integer32):
    """Custom type localRulesInsert based on Integer32"""
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


_LocalRulesInsert_Type.__name__ = "Integer32"
_LocalRulesInsert_Object = MibTableColumn
localRulesInsert = _LocalRulesInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 1100),
    _LocalRulesInsert_Type()
)
localRulesInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesInsert.setStatus("current")


class _LocalRulesDelete_Type(Integer32):
    """Custom type localRulesDelete based on Integer32"""
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


_LocalRulesDelete_Type.__name__ = "Integer32"
_LocalRulesDelete_Object = MibTableColumn
localRulesDelete = _LocalRulesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 600, 1, 1200),
    _LocalRulesDelete_Type()
)
localRulesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localRulesDelete.setStatus("current")
_BlacklistGroup_ObjectIdentity = ObjectIdentity
blacklistGroup = _BlacklistGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 700)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 700, 100),
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 700, 200),
    _BlacklistRateLimitTimeout_Type()
)
blacklistRateLimitTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blacklistRateLimitTimeout.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2200, 1, 60020, 100),
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
    "MX-LFW-MIB",
    **{"lfwMIB": lfwMIB,
       "lfwMIBObjects": lfwMIBObjects,
       "configModifiedStatus": configModifiedStatus,
       "localRulesStatusTable": localRulesStatusTable,
       "localRulesStatusEntry": localRulesStatusEntry,
       "localRulesStatusPriority": localRulesStatusPriority,
       "localRulesStatusSourceAddress": localRulesStatusSourceAddress,
       "localRulesStatusSourcePort": localRulesStatusSourcePort,
       "localRulesStatusDestinationAddress": localRulesStatusDestinationAddress,
       "localRulesStatusDestinationPort": localRulesStatusDestinationPort,
       "localRulesStatusProtocol": localRulesStatusProtocol,
       "localRulesStatusBlacklistEnable": localRulesStatusBlacklistEnable,
       "localRulesStatusRateLimitValue": localRulesStatusRateLimitValue,
       "localRulesStatusRateLimitTimePeriod": localRulesStatusRateLimitTimePeriod,
       "localRulesStatusAction": localRulesStatusAction,
       "defaultPolicy": defaultPolicy,
       "localRulesTable": localRulesTable,
       "localRulesEntry": localRulesEntry,
       "localRulesPriority": localRulesPriority,
       "localRulesActivation": localRulesActivation,
       "localRulesSourceAddress": localRulesSourceAddress,
       "localRulesSourcePort": localRulesSourcePort,
       "localRulesDestinationAddress": localRulesDestinationAddress,
       "localRulesDestinationPort": localRulesDestinationPort,
       "localRulesProtocol": localRulesProtocol,
       "localRulesBlacklistEnable": localRulesBlacklistEnable,
       "localRulesRateLimitValue": localRulesRateLimitValue,
       "localRulesRateLimitTimePeriod": localRulesRateLimitTimePeriod,
       "localRulesAction": localRulesAction,
       "localRulesUp": localRulesUp,
       "localRulesDown": localRulesDown,
       "localRulesInsert": localRulesInsert,
       "localRulesDelete": localRulesDelete,
       "blacklistGroup": blacklistGroup,
       "blacklistTimeout": blacklistTimeout,
       "blacklistRateLimitTimeout": blacklistRateLimitTimeout,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
