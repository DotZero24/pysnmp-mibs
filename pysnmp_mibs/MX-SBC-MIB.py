# SNMP MIB module (MX-SBC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SBC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:59 2025
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

sbcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SbcMIBObjects_ObjectIdentity = ObjectIdentity
sbcMIBObjects = _SbcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1)
)
_ConfigGroup_ObjectIdentity = ObjectIdentity
configGroup = _ConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100)
)
_CallAgentTable_Object = MibTable
callAgentTable = _CallAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100)
)
if mibBuilder.loadTexts:
    callAgentTable.setStatus("current")
_CallAgentEntry_Object = MibTableRow
callAgentEntry = _CallAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1)
)
callAgentEntry.setIndexNames(
    (0, "MX-SBC-MIB", "callAgentId"),
)
if mibBuilder.loadTexts:
    callAgentEntry.setStatus("current")


class _CallAgentId_Type(Unsigned32):
    """Custom type callAgentId based on Unsigned32"""
    defaultValue = 0


_CallAgentId_Type.__name__ = "Unsigned32"
_CallAgentId_Object = MibTableColumn
callAgentId = _CallAgentId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 100),
    _CallAgentId_Type()
)
callAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentId.setStatus("current")


class _CallAgentName_Type(OctetString):
    """Custom type callAgentName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CallAgentName_Type.__name__ = "OctetString"
_CallAgentName_Object = MibTableColumn
callAgentName = _CallAgentName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 200),
    _CallAgentName_Type()
)
callAgentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentName.setStatus("current")


class _CallAgentEnable_Type(MxEnableState):
    """Custom type callAgentEnable based on MxEnableState"""
    defaultValue = 0


_CallAgentEnable_Type.__name__ = "MxEnableState"
_CallAgentEnable_Object = MibTableColumn
callAgentEnable = _CallAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 300),
    _CallAgentEnable_Type()
)
callAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentEnable.setStatus("current")


class _CallAgentSignalingInterface_Type(Unsigned32):
    """Custom type callAgentSignalingInterface based on Unsigned32"""
    defaultValue = 0


_CallAgentSignalingInterface_Type.__name__ = "Unsigned32"
_CallAgentSignalingInterface_Object = MibTableColumn
callAgentSignalingInterface = _CallAgentSignalingInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 400),
    _CallAgentSignalingInterface_Type()
)
callAgentSignalingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentSignalingInterface.setStatus("current")


class _CallAgentMediaInterface_Type(OctetString):
    """Custom type callAgentMediaInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_CallAgentMediaInterface_Type.__name__ = "OctetString"
_CallAgentMediaInterface_Object = MibTableColumn
callAgentMediaInterface = _CallAgentMediaInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 500),
    _CallAgentMediaInterface_Type()
)
callAgentMediaInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentMediaInterface.setStatus("current")


class _CallAgentGateway_Type(OctetString):
    """Custom type callAgentGateway based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CallAgentGateway_Type.__name__ = "OctetString"
_CallAgentGateway_Object = MibTableColumn
callAgentGateway = _CallAgentGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 600),
    _CallAgentGateway_Type()
)
callAgentGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentGateway.setStatus("current")


class _CallAgentPeerHost_Type(MxIpHostNamePort):
    """Custom type callAgentPeerHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_CallAgentPeerHost_Type.__name__ = "MxIpHostNamePort"
_CallAgentPeerHost_Object = MibTableColumn
callAgentPeerHost = _CallAgentPeerHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 700),
    _CallAgentPeerHost_Type()
)
callAgentPeerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentPeerHost.setStatus("current")


class _CallAgentPeerNetwork_Type(MxIpAddrMask):
    """Custom type callAgentPeerNetwork based on MxIpAddrMask"""
    defaultValue = OctetString("")


_CallAgentPeerNetwork_Type.__name__ = "MxIpAddrMask"
_CallAgentPeerNetwork_Object = MibTableColumn
callAgentPeerNetwork = _CallAgentPeerNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 800),
    _CallAgentPeerNetwork_Type()
)
callAgentPeerNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentPeerNetwork.setStatus("current")


class _CallAgentForceTransport_Type(Integer32):
    """Custom type callAgentForceTransport based on Integer32"""
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
        *(("none", 100),
          ("tCP", 200),
          ("uDP", 300),
          ("tLS", 400))
    )


_CallAgentForceTransport_Type.__name__ = "Integer32"
_CallAgentForceTransport_Object = MibTableColumn
callAgentForceTransport = _CallAgentForceTransport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 900),
    _CallAgentForceTransport_Type()
)
callAgentForceTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentForceTransport.setStatus("current")


class _CallAgentConfigStatus_Type(Integer32):
    """Custom type callAgentConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("unknownSignalingInterface", 200),
          ("unknownMediaInterface", 300),
          ("invalidGatewayBinding", 400),
          ("invalidConfig", 500),
          ("noMediaInterface", 600))
    )


_CallAgentConfigStatus_Type.__name__ = "Integer32"
_CallAgentConfigStatus_Object = MibTableColumn
callAgentConfigStatus = _CallAgentConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 1000),
    _CallAgentConfigStatus_Type()
)
callAgentConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentConfigStatus.setStatus("current")


class _CallAgentDelete_Type(Integer32):
    """Custom type callAgentDelete based on Integer32"""
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


_CallAgentDelete_Type.__name__ = "Integer32"
_CallAgentDelete_Object = MibTableColumn
callAgentDelete = _CallAgentDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 100, 1, 10000),
    _CallAgentDelete_Type()
)
callAgentDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentDelete.setStatus("current")
_CallAgentRulesetTable_Object = MibTable
callAgentRulesetTable = _CallAgentRulesetTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200)
)
if mibBuilder.loadTexts:
    callAgentRulesetTable.setStatus("current")
_CallAgentRulesetEntry_Object = MibTableRow
callAgentRulesetEntry = _CallAgentRulesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1)
)
callAgentRulesetEntry.setIndexNames(
    (0, "MX-SBC-MIB", "callAgentRulesetId"),
)
if mibBuilder.loadTexts:
    callAgentRulesetEntry.setStatus("current")


class _CallAgentRulesetId_Type(Unsigned32):
    """Custom type callAgentRulesetId based on Unsigned32"""
    defaultValue = 0


_CallAgentRulesetId_Type.__name__ = "Unsigned32"
_CallAgentRulesetId_Object = MibTableColumn
callAgentRulesetId = _CallAgentRulesetId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 100),
    _CallAgentRulesetId_Type()
)
callAgentRulesetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetId.setStatus("current")


class _CallAgentRulesetCallAgent_Type(Unsigned32):
    """Custom type callAgentRulesetCallAgent based on Unsigned32"""
    defaultValue = 0


_CallAgentRulesetCallAgent_Type.__name__ = "Unsigned32"
_CallAgentRulesetCallAgent_Object = MibTableColumn
callAgentRulesetCallAgent = _CallAgentRulesetCallAgent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 200),
    _CallAgentRulesetCallAgent_Type()
)
callAgentRulesetCallAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentRulesetCallAgent.setStatus("current")


class _CallAgentRulesetPriority_Type(Unsigned32):
    """Custom type callAgentRulesetPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CallAgentRulesetPriority_Type.__name__ = "Unsigned32"
_CallAgentRulesetPriority_Object = MibTableColumn
callAgentRulesetPriority = _CallAgentRulesetPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 300),
    _CallAgentRulesetPriority_Type()
)
callAgentRulesetPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentRulesetPriority.setStatus("current")


class _CallAgentRulesetRuleset_Type(OctetString):
    """Custom type callAgentRulesetRuleset based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CallAgentRulesetRuleset_Type.__name__ = "OctetString"
_CallAgentRulesetRuleset_Object = MibTableColumn
callAgentRulesetRuleset = _CallAgentRulesetRuleset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 400),
    _CallAgentRulesetRuleset_Type()
)
callAgentRulesetRuleset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentRulesetRuleset.setStatus("current")


class _CallAgentRulesetParameters_Type(OctetString):
    """Custom type callAgentRulesetParameters based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CallAgentRulesetParameters_Type.__name__ = "OctetString"
_CallAgentRulesetParameters_Object = MibTableColumn
callAgentRulesetParameters = _CallAgentRulesetParameters_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 500),
    _CallAgentRulesetParameters_Type()
)
callAgentRulesetParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentRulesetParameters.setStatus("current")


class _CallAgentRulesetConfigStatus_Type(Integer32):
    """Custom type callAgentRulesetConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("unknownRuleset", 200),
          ("invalidConfig", 300))
    )


_CallAgentRulesetConfigStatus_Type.__name__ = "Integer32"
_CallAgentRulesetConfigStatus_Object = MibTableColumn
callAgentRulesetConfigStatus = _CallAgentRulesetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 600),
    _CallAgentRulesetConfigStatus_Type()
)
callAgentRulesetConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetConfigStatus.setStatus("current")


class _CallAgentRulesetDelete_Type(Integer32):
    """Custom type callAgentRulesetDelete based on Integer32"""
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


_CallAgentRulesetDelete_Type.__name__ = "Integer32"
_CallAgentRulesetDelete_Object = MibTableColumn
callAgentRulesetDelete = _CallAgentRulesetDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 200, 1, 10000),
    _CallAgentRulesetDelete_Type()
)
callAgentRulesetDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callAgentRulesetDelete.setStatus("current")
_CallAgentRulesetCatalogTable_Object = MibTable
callAgentRulesetCatalogTable = _CallAgentRulesetCatalogTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 250)
)
if mibBuilder.loadTexts:
    callAgentRulesetCatalogTable.setStatus("current")
_CallAgentRulesetCatalogEntry_Object = MibTableRow
callAgentRulesetCatalogEntry = _CallAgentRulesetCatalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 250, 1)
)
callAgentRulesetCatalogEntry.setIndexNames(
    (0, "MX-SBC-MIB", "callAgentRulesetCatalogId"),
)
if mibBuilder.loadTexts:
    callAgentRulesetCatalogEntry.setStatus("current")
_CallAgentRulesetCatalogId_Type = Unsigned32
_CallAgentRulesetCatalogId_Object = MibTableColumn
callAgentRulesetCatalogId = _CallAgentRulesetCatalogId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 250, 1, 100),
    _CallAgentRulesetCatalogId_Type()
)
callAgentRulesetCatalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetCatalogId.setStatus("current")


class _CallAgentRulesetCatalogName_Type(OctetString):
    """Custom type callAgentRulesetCatalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CallAgentRulesetCatalogName_Type.__name__ = "OctetString"
_CallAgentRulesetCatalogName_Object = MibTableColumn
callAgentRulesetCatalogName = _CallAgentRulesetCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 250, 1, 200),
    _CallAgentRulesetCatalogName_Type()
)
callAgentRulesetCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetCatalogName.setStatus("current")


class _CallAgentRulesetCatalogDescription_Type(OctetString):
    """Custom type callAgentRulesetCatalogDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CallAgentRulesetCatalogDescription_Type.__name__ = "OctetString"
_CallAgentRulesetCatalogDescription_Object = MibTableColumn
callAgentRulesetCatalogDescription = _CallAgentRulesetCatalogDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 250, 1, 300),
    _CallAgentRulesetCatalogDescription_Type()
)
callAgentRulesetCatalogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetCatalogDescription.setStatus("current")


class _CallAgentRulesetCatalogOrigin_Type(Integer32):
    """Custom type callAgentRulesetCatalogOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("factory", 100),
          ("custom", 200))
    )


_CallAgentRulesetCatalogOrigin_Type.__name__ = "Integer32"
_CallAgentRulesetCatalogOrigin_Object = MibTableColumn
callAgentRulesetCatalogOrigin = _CallAgentRulesetCatalogOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 250, 1, 400),
    _CallAgentRulesetCatalogOrigin_Type()
)
callAgentRulesetCatalogOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetCatalogOrigin.setStatus("current")
_RoutingRulesTable_Object = MibTable
routingRulesTable = _RoutingRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300)
)
if mibBuilder.loadTexts:
    routingRulesTable.setStatus("current")
_RoutingRulesEntry_Object = MibTableRow
routingRulesEntry = _RoutingRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1)
)
routingRulesEntry.setIndexNames(
    (0, "MX-SBC-MIB", "routingRulesId"),
)
if mibBuilder.loadTexts:
    routingRulesEntry.setStatus("current")


class _RoutingRulesId_Type(Unsigned32):
    """Custom type routingRulesId based on Unsigned32"""
    defaultValue = 0


_RoutingRulesId_Type.__name__ = "Unsigned32"
_RoutingRulesId_Object = MibTableColumn
routingRulesId = _RoutingRulesId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1, 100),
    _RoutingRulesId_Type()
)
routingRulesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesId.setStatus("current")


class _RoutingRulesPriority_Type(Unsigned32):
    """Custom type routingRulesPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RoutingRulesPriority_Type.__name__ = "Unsigned32"
_RoutingRulesPriority_Object = MibTableColumn
routingRulesPriority = _RoutingRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1, 200),
    _RoutingRulesPriority_Type()
)
routingRulesPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRulesPriority.setStatus("current")


class _RoutingRulesRuleset_Type(OctetString):
    """Custom type routingRulesRuleset based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RoutingRulesRuleset_Type.__name__ = "OctetString"
_RoutingRulesRuleset_Object = MibTableColumn
routingRulesRuleset = _RoutingRulesRuleset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1, 300),
    _RoutingRulesRuleset_Type()
)
routingRulesRuleset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRulesRuleset.setStatus("current")


class _RoutingRulesParameters_Type(OctetString):
    """Custom type routingRulesParameters based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RoutingRulesParameters_Type.__name__ = "OctetString"
_RoutingRulesParameters_Object = MibTableColumn
routingRulesParameters = _RoutingRulesParameters_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1, 400),
    _RoutingRulesParameters_Type()
)
routingRulesParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRulesParameters.setStatus("current")


class _RoutingRulesConfigStatus_Type(Integer32):
    """Custom type routingRulesConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("unknownRuleset", 200),
          ("invalidConfig", 300))
    )


_RoutingRulesConfigStatus_Type.__name__ = "Integer32"
_RoutingRulesConfigStatus_Object = MibTableColumn
routingRulesConfigStatus = _RoutingRulesConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1, 500),
    _RoutingRulesConfigStatus_Type()
)
routingRulesConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesConfigStatus.setStatus("current")


class _RoutingRulesDelete_Type(Integer32):
    """Custom type routingRulesDelete based on Integer32"""
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


_RoutingRulesDelete_Type.__name__ = "Integer32"
_RoutingRulesDelete_Object = MibTableColumn
routingRulesDelete = _RoutingRulesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 300, 1, 10000),
    _RoutingRulesDelete_Type()
)
routingRulesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingRulesDelete.setStatus("current")
_RoutingRulesetCatalogTable_Object = MibTable
routingRulesetCatalogTable = _RoutingRulesetCatalogTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 350)
)
if mibBuilder.loadTexts:
    routingRulesetCatalogTable.setStatus("current")
_RoutingRulesetCatalogEntry_Object = MibTableRow
routingRulesetCatalogEntry = _RoutingRulesetCatalogEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 350, 1)
)
routingRulesetCatalogEntry.setIndexNames(
    (0, "MX-SBC-MIB", "routingRulesetCatalogId"),
)
if mibBuilder.loadTexts:
    routingRulesetCatalogEntry.setStatus("current")
_RoutingRulesetCatalogId_Type = Unsigned32
_RoutingRulesetCatalogId_Object = MibTableColumn
routingRulesetCatalogId = _RoutingRulesetCatalogId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 350, 1, 100),
    _RoutingRulesetCatalogId_Type()
)
routingRulesetCatalogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesetCatalogId.setStatus("current")


class _RoutingRulesetCatalogName_Type(OctetString):
    """Custom type routingRulesetCatalogName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RoutingRulesetCatalogName_Type.__name__ = "OctetString"
_RoutingRulesetCatalogName_Object = MibTableColumn
routingRulesetCatalogName = _RoutingRulesetCatalogName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 350, 1, 200),
    _RoutingRulesetCatalogName_Type()
)
routingRulesetCatalogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesetCatalogName.setStatus("current")


class _RoutingRulesetCatalogDescription_Type(OctetString):
    """Custom type routingRulesetCatalogDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RoutingRulesetCatalogDescription_Type.__name__ = "OctetString"
_RoutingRulesetCatalogDescription_Object = MibTableColumn
routingRulesetCatalogDescription = _RoutingRulesetCatalogDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 350, 1, 300),
    _RoutingRulesetCatalogDescription_Type()
)
routingRulesetCatalogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesetCatalogDescription.setStatus("current")


class _RoutingRulesetCatalogOrigin_Type(Integer32):
    """Custom type routingRulesetCatalogOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("factory", 100),
          ("custom", 200))
    )


_RoutingRulesetCatalogOrigin_Type.__name__ = "Integer32"
_RoutingRulesetCatalogOrigin_Object = MibTableColumn
routingRulesetCatalogOrigin = _RoutingRulesetCatalogOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 350, 1, 400),
    _RoutingRulesetCatalogOrigin_Type()
)
routingRulesetCatalogOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesetCatalogOrigin.setStatus("current")
_SignalingInterfaceTable_Object = MibTable
signalingInterfaceTable = _SignalingInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400)
)
if mibBuilder.loadTexts:
    signalingInterfaceTable.setStatus("current")
_SignalingInterfaceEntry_Object = MibTableRow
signalingInterfaceEntry = _SignalingInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1)
)
signalingInterfaceEntry.setIndexNames(
    (0, "MX-SBC-MIB", "signalingInterfaceId"),
)
if mibBuilder.loadTexts:
    signalingInterfaceEntry.setStatus("current")


class _SignalingInterfaceId_Type(Unsigned32):
    """Custom type signalingInterfaceId based on Unsigned32"""
    defaultValue = 0


_SignalingInterfaceId_Type.__name__ = "Unsigned32"
_SignalingInterfaceId_Object = MibTableColumn
signalingInterfaceId = _SignalingInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 100),
    _SignalingInterfaceId_Type()
)
signalingInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceId.setStatus("current")


class _SignalingInterfaceName_Type(OctetString):
    """Custom type signalingInterfaceName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SignalingInterfaceName_Type.__name__ = "OctetString"
_SignalingInterfaceName_Object = MibTableColumn
signalingInterfaceName = _SignalingInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 200),
    _SignalingInterfaceName_Type()
)
signalingInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceName.setStatus("current")


class _SignalingInterfaceNetworkInterface_Type(OctetString):
    """Custom type signalingInterfaceNetworkInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SignalingInterfaceNetworkInterface_Type.__name__ = "OctetString"
_SignalingInterfaceNetworkInterface_Object = MibTableColumn
signalingInterfaceNetworkInterface = _SignalingInterfaceNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 300),
    _SignalingInterfaceNetworkInterface_Type()
)
signalingInterfaceNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceNetworkInterface.setStatus("current")


class _SignalingInterfacePort_Type(Unsigned32):
    """Custom type signalingInterfacePort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SignalingInterfacePort_Type.__name__ = "Unsigned32"
_SignalingInterfacePort_Object = MibTableColumn
signalingInterfacePort = _SignalingInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 400),
    _SignalingInterfacePort_Type()
)
signalingInterfacePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfacePort.setStatus("current")


class _SignalingInterfaceSecurePort_Type(Unsigned32):
    """Custom type signalingInterfaceSecurePort based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SignalingInterfaceSecurePort_Type.__name__ = "Unsigned32"
_SignalingInterfaceSecurePort_Object = MibTableColumn
signalingInterfaceSecurePort = _SignalingInterfaceSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 450),
    _SignalingInterfaceSecurePort_Type()
)
signalingInterfaceSecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceSecurePort.setStatus("current")


class _SignalingInterfaceTlsMode_Type(Integer32):
    """Custom type signalingInterfaceTlsMode based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("both", 100),
          ("client", 200),
          ("server", 300))
    )


_SignalingInterfaceTlsMode_Type.__name__ = "Integer32"
_SignalingInterfaceTlsMode_Object = MibTableColumn
signalingInterfaceTlsMode = _SignalingInterfaceTlsMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 475),
    _SignalingInterfaceTlsMode_Type()
)
signalingInterfaceTlsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceTlsMode.setStatus("current")


class _SignalingInterfaceAllowedTransports_Type(Integer32):
    """Custom type signalingInterfaceAllowedTransports based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tlsOnly", 200))
    )


_SignalingInterfaceAllowedTransports_Type.__name__ = "Integer32"
_SignalingInterfaceAllowedTransports_Object = MibTableColumn
signalingInterfaceAllowedTransports = _SignalingInterfaceAllowedTransports_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 480),
    _SignalingInterfaceAllowedTransports_Type()
)
signalingInterfaceAllowedTransports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceAllowedTransports.setStatus("current")


class _SignalingInterfacePublicIpAddr_Type(MxIpAddress):
    """Custom type signalingInterfacePublicIpAddr based on MxIpAddress"""
    defaultValue = OctetString("")


_SignalingInterfacePublicIpAddr_Type.__name__ = "MxIpAddress"
_SignalingInterfacePublicIpAddr_Object = MibTableColumn
signalingInterfacePublicIpAddr = _SignalingInterfacePublicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 500),
    _SignalingInterfacePublicIpAddr_Type()
)
signalingInterfacePublicIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfacePublicIpAddr.setStatus("current")


class _SignalingInterfaceTcpConnectTimeout_Type(Unsigned32):
    """Custom type signalingInterfaceTcpConnectTimeout based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127000),
    )


_SignalingInterfaceTcpConnectTimeout_Type.__name__ = "Unsigned32"
_SignalingInterfaceTcpConnectTimeout_Object = MibTableColumn
signalingInterfaceTcpConnectTimeout = _SignalingInterfaceTcpConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 600),
    _SignalingInterfaceTcpConnectTimeout_Type()
)
signalingInterfaceTcpConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceTcpConnectTimeout.setStatus("current")


class _SignalingInterfaceTcpIdleTimeout_Type(Unsigned32):
    """Custom type signalingInterfaceTcpIdleTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300000),
    )


_SignalingInterfaceTcpIdleTimeout_Type.__name__ = "Unsigned32"
_SignalingInterfaceTcpIdleTimeout_Object = MibTableColumn
signalingInterfaceTcpIdleTimeout = _SignalingInterfaceTcpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 700),
    _SignalingInterfaceTcpIdleTimeout_Type()
)
signalingInterfaceTcpIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceTcpIdleTimeout.setStatus("current")


class _SignalingInterfaceConfigStatus_Type(Integer32):
    """Custom type signalingInterfaceConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              350,
              380,
              400)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("unknownNetworkInterface", 200),
          ("portConflict", 300),
          ("invalidTlsMode", 350),
          ("invalidTransportMode", 380),
          ("invalidConfig", 400))
    )


_SignalingInterfaceConfigStatus_Type.__name__ = "Integer32"
_SignalingInterfaceConfigStatus_Object = MibTableColumn
signalingInterfaceConfigStatus = _SignalingInterfaceConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 800),
    _SignalingInterfaceConfigStatus_Type()
)
signalingInterfaceConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceConfigStatus.setStatus("current")


class _SignalingInterfaceDelete_Type(Integer32):
    """Custom type signalingInterfaceDelete based on Integer32"""
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


_SignalingInterfaceDelete_Type.__name__ = "Integer32"
_SignalingInterfaceDelete_Object = MibTableColumn
signalingInterfaceDelete = _SignalingInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 400, 1, 10000),
    _SignalingInterfaceDelete_Type()
)
signalingInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    signalingInterfaceDelete.setStatus("current")
_MediaInterfaceTable_Object = MibTable
mediaInterfaceTable = _MediaInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500)
)
if mibBuilder.loadTexts:
    mediaInterfaceTable.setStatus("current")
_MediaInterfaceEntry_Object = MibTableRow
mediaInterfaceEntry = _MediaInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1)
)
mediaInterfaceEntry.setIndexNames(
    (0, "MX-SBC-MIB", "mediaInterfaceId"),
)
if mibBuilder.loadTexts:
    mediaInterfaceEntry.setStatus("current")


class _MediaInterfaceId_Type(Unsigned32):
    """Custom type mediaInterfaceId based on Unsigned32"""
    defaultValue = 0


_MediaInterfaceId_Type.__name__ = "Unsigned32"
_MediaInterfaceId_Object = MibTableColumn
mediaInterfaceId = _MediaInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 100),
    _MediaInterfaceId_Type()
)
mediaInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceId.setStatus("current")


class _MediaInterfaceName_Type(OctetString):
    """Custom type mediaInterfaceName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_MediaInterfaceName_Type.__name__ = "OctetString"
_MediaInterfaceName_Object = MibTableColumn
mediaInterfaceName = _MediaInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 200),
    _MediaInterfaceName_Type()
)
mediaInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaInterfaceName.setStatus("current")


class _MediaInterfaceNetworkInterface_Type(OctetString):
    """Custom type mediaInterfaceNetworkInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MediaInterfaceNetworkInterface_Type.__name__ = "OctetString"
_MediaInterfaceNetworkInterface_Object = MibTableColumn
mediaInterfaceNetworkInterface = _MediaInterfaceNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 300),
    _MediaInterfaceNetworkInterface_Type()
)
mediaInterfaceNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaInterfaceNetworkInterface.setStatus("current")


class _MediaInterfacePortRange_Type(OctetString):
    """Custom type mediaInterfacePortRange based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MediaInterfacePortRange_Type.__name__ = "OctetString"
_MediaInterfacePortRange_Object = MibTableColumn
mediaInterfacePortRange = _MediaInterfacePortRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 400),
    _MediaInterfacePortRange_Type()
)
mediaInterfacePortRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaInterfacePortRange.setStatus("current")


class _MediaInterfacePublicIpAddr_Type(MxIpAddress):
    """Custom type mediaInterfacePublicIpAddr based on MxIpAddress"""
    defaultValue = OctetString("")


_MediaInterfacePublicIpAddr_Type.__name__ = "MxIpAddress"
_MediaInterfacePublicIpAddr_Object = MibTableColumn
mediaInterfacePublicIpAddr = _MediaInterfacePublicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 500),
    _MediaInterfacePublicIpAddr_Type()
)
mediaInterfacePublicIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaInterfacePublicIpAddr.setStatus("current")


class _MediaInterfaceConfigStatus_Type(Integer32):
    """Custom type mediaInterfaceConfigStatus based on Integer32"""
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
        *(("valid", 100),
          ("unknownNetworkInterface", 200),
          ("portConflict", 300),
          ("invalidConfig", 400))
    )


_MediaInterfaceConfigStatus_Type.__name__ = "Integer32"
_MediaInterfaceConfigStatus_Object = MibTableColumn
mediaInterfaceConfigStatus = _MediaInterfaceConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 600),
    _MediaInterfaceConfigStatus_Type()
)
mediaInterfaceConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceConfigStatus.setStatus("current")


class _MediaInterfaceDelete_Type(Integer32):
    """Custom type mediaInterfaceDelete based on Integer32"""
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


_MediaInterfaceDelete_Type.__name__ = "Integer32"
_MediaInterfaceDelete_Object = MibTableColumn
mediaInterfaceDelete = _MediaInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 500, 1, 10000),
    _MediaInterfaceDelete_Type()
)
mediaInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaInterfaceDelete.setStatus("current")
_RegistrationAgentTable_Object = MibTable
registrationAgentTable = _RegistrationAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600)
)
if mibBuilder.loadTexts:
    registrationAgentTable.setStatus("current")
_RegistrationAgentEntry_Object = MibTableRow
registrationAgentEntry = _RegistrationAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1)
)
registrationAgentEntry.setIndexNames(
    (0, "MX-SBC-MIB", "registrationAgentId"),
)
if mibBuilder.loadTexts:
    registrationAgentEntry.setStatus("current")


class _RegistrationAgentId_Type(Unsigned32):
    """Custom type registrationAgentId based on Unsigned32"""
    defaultValue = 0


_RegistrationAgentId_Type.__name__ = "Unsigned32"
_RegistrationAgentId_Object = MibTableColumn
registrationAgentId = _RegistrationAgentId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 100),
    _RegistrationAgentId_Type()
)
registrationAgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationAgentId.setStatus("current")


class _RegistrationAgentUsername_Type(OctetString):
    """Custom type registrationAgentUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RegistrationAgentUsername_Type.__name__ = "OctetString"
_RegistrationAgentUsername_Object = MibTableColumn
registrationAgentUsername = _RegistrationAgentUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 200),
    _RegistrationAgentUsername_Type()
)
registrationAgentUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentUsername.setStatus("current")


class _RegistrationAgentDomain_Type(OctetString):
    """Custom type registrationAgentDomain based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RegistrationAgentDomain_Type.__name__ = "OctetString"
_RegistrationAgentDomain_Object = MibTableColumn
registrationAgentDomain = _RegistrationAgentDomain_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 300),
    _RegistrationAgentDomain_Type()
)
registrationAgentDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentDomain.setStatus("current")


class _RegistrationAgentFriendlyName_Type(OctetString):
    """Custom type registrationAgentFriendlyName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RegistrationAgentFriendlyName_Type.__name__ = "OctetString"
_RegistrationAgentFriendlyName_Object = MibTableColumn
registrationAgentFriendlyName = _RegistrationAgentFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 400),
    _RegistrationAgentFriendlyName_Type()
)
registrationAgentFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentFriendlyName.setStatus("current")


class _RegistrationAgentContact_Type(OctetString):
    """Custom type registrationAgentContact based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RegistrationAgentContact_Type.__name__ = "OctetString"
_RegistrationAgentContact_Object = MibTableColumn
registrationAgentContact = _RegistrationAgentContact_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 500),
    _RegistrationAgentContact_Type()
)
registrationAgentContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentContact.setStatus("current")


class _RegistrationAgentRegistrationType_Type(Integer32):
    """Custom type registrationAgentRegistrationType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("normal", 100),
          ("rFC6140", 200))
    )


_RegistrationAgentRegistrationType_Type.__name__ = "Integer32"
_RegistrationAgentRegistrationType_Object = MibTableColumn
registrationAgentRegistrationType = _RegistrationAgentRegistrationType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 550),
    _RegistrationAgentRegistrationType_Type()
)
registrationAgentRegistrationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentRegistrationType.setStatus("current")


class _RegistrationAgentExpireValue_Type(Unsigned32):
    """Custom type registrationAgentExpireValue based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_RegistrationAgentExpireValue_Type.__name__ = "Unsigned32"
_RegistrationAgentExpireValue_Object = MibTableColumn
registrationAgentExpireValue = _RegistrationAgentExpireValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 600),
    _RegistrationAgentExpireValue_Type()
)
registrationAgentExpireValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentExpireValue.setStatus("current")


class _RegistrationAgentRetryInterval_Type(Unsigned32):
    """Custom type registrationAgentRetryInterval based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_RegistrationAgentRetryInterval_Type.__name__ = "Unsigned32"
_RegistrationAgentRetryInterval_Object = MibTableColumn
registrationAgentRetryInterval = _RegistrationAgentRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 700),
    _RegistrationAgentRetryInterval_Type()
)
registrationAgentRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentRetryInterval.setStatus("current")


class _RegistrationAgentConfigStatus_Type(Integer32):
    """Custom type registrationAgentConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("invalidConfig", 200),
          ("invalidContact", 300))
    )


_RegistrationAgentConfigStatus_Type.__name__ = "Integer32"
_RegistrationAgentConfigStatus_Object = MibTableColumn
registrationAgentConfigStatus = _RegistrationAgentConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 800),
    _RegistrationAgentConfigStatus_Type()
)
registrationAgentConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationAgentConfigStatus.setStatus("current")


class _RegistrationAgentDelete_Type(Integer32):
    """Custom type registrationAgentDelete based on Integer32"""
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


_RegistrationAgentDelete_Type.__name__ = "Integer32"
_RegistrationAgentDelete_Object = MibTableColumn
registrationAgentDelete = _RegistrationAgentDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 600, 1, 10000),
    _RegistrationAgentDelete_Type()
)
registrationAgentDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationAgentDelete.setStatus("current")
_PeerMonitoringTable_Object = MibTable
peerMonitoringTable = _PeerMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700)
)
if mibBuilder.loadTexts:
    peerMonitoringTable.setStatus("current")
_PeerMonitoringEntry_Object = MibTableRow
peerMonitoringEntry = _PeerMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700, 1)
)
peerMonitoringEntry.setIndexNames(
    (0, "MX-SBC-MIB", "peerMonitoringId"),
)
if mibBuilder.loadTexts:
    peerMonitoringEntry.setStatus("current")


class _PeerMonitoringId_Type(Unsigned32):
    """Custom type peerMonitoringId based on Unsigned32"""
    defaultValue = 0


_PeerMonitoringId_Type.__name__ = "Unsigned32"
_PeerMonitoringId_Object = MibTableColumn
peerMonitoringId = _PeerMonitoringId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700, 1, 100),
    _PeerMonitoringId_Type()
)
peerMonitoringId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerMonitoringId.setStatus("current")


class _PeerMonitoringKeepAliveInterval_Type(Unsigned32):
    """Custom type peerMonitoringKeepAliveInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_PeerMonitoringKeepAliveInterval_Type.__name__ = "Unsigned32"
_PeerMonitoringKeepAliveInterval_Object = MibTableColumn
peerMonitoringKeepAliveInterval = _PeerMonitoringKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700, 1, 200),
    _PeerMonitoringKeepAliveInterval_Type()
)
peerMonitoringKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peerMonitoringKeepAliveInterval.setStatus("current")


class _PeerMonitoringBlackListingDuration_Type(Unsigned32):
    """Custom type peerMonitoringBlackListingDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PeerMonitoringBlackListingDuration_Type.__name__ = "Unsigned32"
_PeerMonitoringBlackListingDuration_Object = MibTableColumn
peerMonitoringBlackListingDuration = _PeerMonitoringBlackListingDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700, 1, 300),
    _PeerMonitoringBlackListingDuration_Type()
)
peerMonitoringBlackListingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peerMonitoringBlackListingDuration.setStatus("current")


class _PeerMonitoringBlackListingDelay_Type(Unsigned32):
    """Custom type peerMonitoringBlackListingDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_PeerMonitoringBlackListingDelay_Type.__name__ = "Unsigned32"
_PeerMonitoringBlackListingDelay_Object = MibTableColumn
peerMonitoringBlackListingDelay = _PeerMonitoringBlackListingDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700, 1, 400),
    _PeerMonitoringBlackListingDelay_Type()
)
peerMonitoringBlackListingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peerMonitoringBlackListingDelay.setStatus("current")


class _PeerMonitoringBlackListingErrorCodes_Type(OctetString):
    """Custom type peerMonitoringBlackListingErrorCodes based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_PeerMonitoringBlackListingErrorCodes_Type.__name__ = "OctetString"
_PeerMonitoringBlackListingErrorCodes_Object = MibTableColumn
peerMonitoringBlackListingErrorCodes = _PeerMonitoringBlackListingErrorCodes_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 700, 1, 500),
    _PeerMonitoringBlackListingErrorCodes_Type()
)
peerMonitoringBlackListingErrorCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peerMonitoringBlackListingErrorCodes.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 100, 800),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")
_RoutingGroup_ObjectIdentity = ObjectIdentity
routingGroup = _RoutingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150)
)
_PrefixBasedRoutingTable_Object = MibTable
prefixBasedRoutingTable = _PrefixBasedRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100)
)
if mibBuilder.loadTexts:
    prefixBasedRoutingTable.setStatus("current")
_PrefixBasedRoutingEntry_Object = MibTableRow
prefixBasedRoutingEntry = _PrefixBasedRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1)
)
prefixBasedRoutingEntry.setIndexNames(
    (0, "MX-SBC-MIB", "prefixBasedRoutingRuleId"),
)
if mibBuilder.loadTexts:
    prefixBasedRoutingEntry.setStatus("current")


class _PrefixBasedRoutingRuleId_Type(Unsigned32):
    """Custom type prefixBasedRoutingRuleId based on Unsigned32"""
    defaultValue = 0


_PrefixBasedRoutingRuleId_Type.__name__ = "Unsigned32"
_PrefixBasedRoutingRuleId_Object = MibTableColumn
prefixBasedRoutingRuleId = _PrefixBasedRoutingRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 100),
    _PrefixBasedRoutingRuleId_Type()
)
prefixBasedRoutingRuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prefixBasedRoutingRuleId.setStatus("current")


class _PrefixBasedRoutingPrefix_Type(OctetString):
    """Custom type prefixBasedRoutingPrefix based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_PrefixBasedRoutingPrefix_Type.__name__ = "OctetString"
_PrefixBasedRoutingPrefix_Object = MibTableColumn
prefixBasedRoutingPrefix = _PrefixBasedRoutingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 200),
    _PrefixBasedRoutingPrefix_Type()
)
prefixBasedRoutingPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingPrefix.setStatus("current")


class _PrefixBasedRoutingDestinationCa_Type(Unsigned32):
    """Custom type prefixBasedRoutingDestinationCa based on Unsigned32"""
    defaultValue = 0


_PrefixBasedRoutingDestinationCa_Type.__name__ = "Unsigned32"
_PrefixBasedRoutingDestinationCa_Object = MibTableColumn
prefixBasedRoutingDestinationCa = _PrefixBasedRoutingDestinationCa_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 300),
    _PrefixBasedRoutingDestinationCa_Type()
)
prefixBasedRoutingDestinationCa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingDestinationCa.setStatus("current")


class _PrefixBasedRoutingRoutingMethod_Type(Integer32):
    """Custom type prefixBasedRoutingRoutingMethod based on Integer32"""
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
        *(("nextHop", 100),
          ("outboundProxy", 200),
          ("requestUri", 300))
    )


_PrefixBasedRoutingRoutingMethod_Type.__name__ = "Integer32"
_PrefixBasedRoutingRoutingMethod_Object = MibTableColumn
prefixBasedRoutingRoutingMethod = _PrefixBasedRoutingRoutingMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 400),
    _PrefixBasedRoutingRoutingMethod_Type()
)
prefixBasedRoutingRoutingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingRoutingMethod.setStatus("current")


class _PrefixBasedRoutingDestinationOverride_Type(OctetString):
    """Custom type prefixBasedRoutingDestinationOverride based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_PrefixBasedRoutingDestinationOverride_Type.__name__ = "OctetString"
_PrefixBasedRoutingDestinationOverride_Object = MibTableColumn
prefixBasedRoutingDestinationOverride = _PrefixBasedRoutingDestinationOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 500),
    _PrefixBasedRoutingDestinationOverride_Type()
)
prefixBasedRoutingDestinationOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingDestinationOverride.setStatus("current")


class _PrefixBasedRoutingRUriHandling_Type(Integer32):
    """Custom type prefixBasedRoutingRUriHandling based on Integer32"""
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
        *(("none", 100),
          ("update", 200),
          ("replace", 300))
    )


_PrefixBasedRoutingRUriHandling_Type.__name__ = "Integer32"
_PrefixBasedRoutingRUriHandling_Object = MibTableColumn
prefixBasedRoutingRUriHandling = _PrefixBasedRoutingRUriHandling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 600),
    _PrefixBasedRoutingRUriHandling_Type()
)
prefixBasedRoutingRUriHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingRUriHandling.setStatus("current")


class _PrefixBasedRoutingForceTransport_Type(Integer32):
    """Custom type prefixBasedRoutingForceTransport based on Integer32"""
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
        *(("none", 100),
          ("tCP", 200),
          ("uDP", 300),
          ("tLS", 400))
    )


_PrefixBasedRoutingForceTransport_Type.__name__ = "Integer32"
_PrefixBasedRoutingForceTransport_Object = MibTableColumn
prefixBasedRoutingForceTransport = _PrefixBasedRoutingForceTransport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 700),
    _PrefixBasedRoutingForceTransport_Type()
)
prefixBasedRoutingForceTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingForceTransport.setStatus("current")


class _PrefixBasedRoutingConfigStatus_Type(Integer32):
    """Custom type prefixBasedRoutingConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("invalidCa", 200),
          ("noPrefix", 300),
          ("invalidDestination", 400),
          ("destinationOverrideMandatory", 500),
          ("prefixDuplicate", 600),
          ("invalidConfig", 700))
    )


_PrefixBasedRoutingConfigStatus_Type.__name__ = "Integer32"
_PrefixBasedRoutingConfigStatus_Object = MibTableColumn
prefixBasedRoutingConfigStatus = _PrefixBasedRoutingConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 1000),
    _PrefixBasedRoutingConfigStatus_Type()
)
prefixBasedRoutingConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prefixBasedRoutingConfigStatus.setStatus("current")


class _PrefixBasedRoutingDelete_Type(Integer32):
    """Custom type prefixBasedRoutingDelete based on Integer32"""
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


_PrefixBasedRoutingDelete_Type.__name__ = "Integer32"
_PrefixBasedRoutingDelete_Object = MibTableColumn
prefixBasedRoutingDelete = _PrefixBasedRoutingDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 150, 100, 1, 10000),
    _PrefixBasedRoutingDelete_Type()
)
prefixBasedRoutingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prefixBasedRoutingDelete.setStatus("current")
_RegistrationGroup_ObjectIdentity = ObjectIdentity
registrationGroup = _RegistrationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170)
)
_StaticRegistrationTable_Object = MibTable
staticRegistrationTable = _StaticRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100)
)
if mibBuilder.loadTexts:
    staticRegistrationTable.setStatus("current")
_StaticRegistrationEntry_Object = MibTableRow
staticRegistrationEntry = _StaticRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100, 1)
)
staticRegistrationEntry.setIndexNames(
    (0, "MX-SBC-MIB", "staticRegistrationRegistrationId"),
)
if mibBuilder.loadTexts:
    staticRegistrationEntry.setStatus("current")


class _StaticRegistrationRegistrationId_Type(Unsigned32):
    """Custom type staticRegistrationRegistrationId based on Unsigned32"""
    defaultValue = 0


_StaticRegistrationRegistrationId_Type.__name__ = "Unsigned32"
_StaticRegistrationRegistrationId_Object = MibTableColumn
staticRegistrationRegistrationId = _StaticRegistrationRegistrationId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100, 1, 100),
    _StaticRegistrationRegistrationId_Type()
)
staticRegistrationRegistrationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRegistrationRegistrationId.setStatus("current")


class _StaticRegistrationAor_Type(OctetString):
    """Custom type staticRegistrationAor based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_StaticRegistrationAor_Type.__name__ = "OctetString"
_StaticRegistrationAor_Object = MibTableColumn
staticRegistrationAor = _StaticRegistrationAor_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100, 1, 200),
    _StaticRegistrationAor_Type()
)
staticRegistrationAor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRegistrationAor.setStatus("current")


class _StaticRegistrationContact_Type(OctetString):
    """Custom type staticRegistrationContact based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_StaticRegistrationContact_Type.__name__ = "OctetString"
_StaticRegistrationContact_Object = MibTableColumn
staticRegistrationContact = _StaticRegistrationContact_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100, 1, 300),
    _StaticRegistrationContact_Type()
)
staticRegistrationContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRegistrationContact.setStatus("current")


class _StaticRegistrationConfigStatus_Type(Integer32):
    """Custom type staticRegistrationConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("valid", 100),
          ("aorDuplicate", 200),
          ("invalidConfig", 300))
    )


_StaticRegistrationConfigStatus_Type.__name__ = "Integer32"
_StaticRegistrationConfigStatus_Object = MibTableColumn
staticRegistrationConfigStatus = _StaticRegistrationConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100, 1, 1000),
    _StaticRegistrationConfigStatus_Type()
)
staticRegistrationConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticRegistrationConfigStatus.setStatus("current")


class _StaticRegistrationDelete_Type(Integer32):
    """Custom type staticRegistrationDelete based on Integer32"""
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


_StaticRegistrationDelete_Type.__name__ = "Integer32"
_StaticRegistrationDelete_Object = MibTableColumn
staticRegistrationDelete = _StaticRegistrationDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 170, 100, 1, 10000),
    _StaticRegistrationDelete_Type()
)
staticRegistrationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticRegistrationDelete.setStatus("current")
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200)
)
_CallAgentStatusTable_Object = MibTable
callAgentStatusTable = _CallAgentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100)
)
if mibBuilder.loadTexts:
    callAgentStatusTable.setStatus("current")
_CallAgentStatusEntry_Object = MibTableRow
callAgentStatusEntry = _CallAgentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1)
)
callAgentStatusEntry.setIndexNames(
    (0, "MX-SBC-MIB", "callAgentStatusId"),
)
if mibBuilder.loadTexts:
    callAgentStatusEntry.setStatus("current")
_CallAgentStatusId_Type = Unsigned32
_CallAgentStatusId_Object = MibTableColumn
callAgentStatusId = _CallAgentStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 100),
    _CallAgentStatusId_Type()
)
callAgentStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusId.setStatus("current")


class _CallAgentStatusName_Type(OctetString):
    """Custom type callAgentStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CallAgentStatusName_Type.__name__ = "OctetString"
_CallAgentStatusName_Object = MibTableColumn
callAgentStatusName = _CallAgentStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 200),
    _CallAgentStatusName_Type()
)
callAgentStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusName.setStatus("current")
_CallAgentStatusSignalingInterface_Type = Unsigned32
_CallAgentStatusSignalingInterface_Object = MibTableColumn
callAgentStatusSignalingInterface = _CallAgentStatusSignalingInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 300),
    _CallAgentStatusSignalingInterface_Type()
)
callAgentStatusSignalingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusSignalingInterface.setStatus("current")
_CallAgentStatusMediaInterface_Type = OctetString
_CallAgentStatusMediaInterface_Object = MibTableColumn
callAgentStatusMediaInterface = _CallAgentStatusMediaInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 400),
    _CallAgentStatusMediaInterface_Type()
)
callAgentStatusMediaInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusMediaInterface.setStatus("current")


class _CallAgentStatusGateway_Type(OctetString):
    """Custom type callAgentStatusGateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CallAgentStatusGateway_Type.__name__ = "OctetString"
_CallAgentStatusGateway_Object = MibTableColumn
callAgentStatusGateway = _CallAgentStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 500),
    _CallAgentStatusGateway_Type()
)
callAgentStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusGateway.setStatus("current")
_CallAgentStatusPeerHost_Type = MxIpAddress
_CallAgentStatusPeerHost_Object = MibTableColumn
callAgentStatusPeerHost = _CallAgentStatusPeerHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 600),
    _CallAgentStatusPeerHost_Type()
)
callAgentStatusPeerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusPeerHost.setStatus("current")


class _CallAgentStatusState_Type(Integer32):
    """Custom type callAgentStatusState based on Integer32"""
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
        *(("active", 100),
          ("networkDown", 200),
          ("internalError", 300),
          ("peerDown", 400))
    )


_CallAgentStatusState_Type.__name__ = "Integer32"
_CallAgentStatusState_Object = MibTableColumn
callAgentStatusState = _CallAgentStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 100, 1, 700),
    _CallAgentStatusState_Type()
)
callAgentStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatusState.setStatus("current")
_SignalingInterfaceStatusTable_Object = MibTable
signalingInterfaceStatusTable = _SignalingInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200)
)
if mibBuilder.loadTexts:
    signalingInterfaceStatusTable.setStatus("current")
_SignalingInterfaceStatusEntry_Object = MibTableRow
signalingInterfaceStatusEntry = _SignalingInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1)
)
signalingInterfaceStatusEntry.setIndexNames(
    (0, "MX-SBC-MIB", "signalingInterfaceStatusId"),
)
if mibBuilder.loadTexts:
    signalingInterfaceStatusEntry.setStatus("current")
_SignalingInterfaceStatusId_Type = Unsigned32
_SignalingInterfaceStatusId_Object = MibTableColumn
signalingInterfaceStatusId = _SignalingInterfaceStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 100),
    _SignalingInterfaceStatusId_Type()
)
signalingInterfaceStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusId.setStatus("current")


class _SignalingInterfaceStatusName_Type(OctetString):
    """Custom type signalingInterfaceStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SignalingInterfaceStatusName_Type.__name__ = "OctetString"
_SignalingInterfaceStatusName_Object = MibTableColumn
signalingInterfaceStatusName = _SignalingInterfaceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 200),
    _SignalingInterfaceStatusName_Type()
)
signalingInterfaceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusName.setStatus("current")
_SignalingInterfaceStatusNetworkInterface_Type = OctetString
_SignalingInterfaceStatusNetworkInterface_Object = MibTableColumn
signalingInterfaceStatusNetworkInterface = _SignalingInterfaceStatusNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 300),
    _SignalingInterfaceStatusNetworkInterface_Type()
)
signalingInterfaceStatusNetworkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusNetworkInterface.setStatus("current")
_SignalingInterfaceStatusPort_Type = Unsigned32
_SignalingInterfaceStatusPort_Object = MibTableColumn
signalingInterfaceStatusPort = _SignalingInterfaceStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 400),
    _SignalingInterfaceStatusPort_Type()
)
signalingInterfaceStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusPort.setStatus("current")
_SignalingInterfaceStatusSecurePort_Type = Unsigned32
_SignalingInterfaceStatusSecurePort_Object = MibTableColumn
signalingInterfaceStatusSecurePort = _SignalingInterfaceStatusSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 450),
    _SignalingInterfaceStatusSecurePort_Type()
)
signalingInterfaceStatusSecurePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusSecurePort.setStatus("current")


class _SignalingInterfaceStatusTlsMode_Type(Integer32):
    """Custom type signalingInterfaceStatusTlsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("both", 100),
          ("client", 200),
          ("server", 300))
    )


_SignalingInterfaceStatusTlsMode_Type.__name__ = "Integer32"
_SignalingInterfaceStatusTlsMode_Object = MibTableColumn
signalingInterfaceStatusTlsMode = _SignalingInterfaceStatusTlsMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 475),
    _SignalingInterfaceStatusTlsMode_Type()
)
signalingInterfaceStatusTlsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusTlsMode.setStatus("current")


class _SignalingInterfaceStatusAllowedTransports_Type(Integer32):
    """Custom type signalingInterfaceStatusAllowedTransports based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("tlsOnly", 200))
    )


_SignalingInterfaceStatusAllowedTransports_Type.__name__ = "Integer32"
_SignalingInterfaceStatusAllowedTransports_Object = MibTableColumn
signalingInterfaceStatusAllowedTransports = _SignalingInterfaceStatusAllowedTransports_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 485),
    _SignalingInterfaceStatusAllowedTransports_Type()
)
signalingInterfaceStatusAllowedTransports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusAllowedTransports.setStatus("current")
_SignalingInterfaceStatusPublicIpAddr_Type = MxIpAddress
_SignalingInterfaceStatusPublicIpAddr_Object = MibTableColumn
signalingInterfaceStatusPublicIpAddr = _SignalingInterfaceStatusPublicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 500),
    _SignalingInterfaceStatusPublicIpAddr_Type()
)
signalingInterfaceStatusPublicIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusPublicIpAddr.setStatus("current")
_SignalingInterfaceStatusTcpConnectTimeout_Type = Unsigned32
_SignalingInterfaceStatusTcpConnectTimeout_Object = MibTableColumn
signalingInterfaceStatusTcpConnectTimeout = _SignalingInterfaceStatusTcpConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 600),
    _SignalingInterfaceStatusTcpConnectTimeout_Type()
)
signalingInterfaceStatusTcpConnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusTcpConnectTimeout.setStatus("current")
_SignalingInterfaceStatusTcpIdleTimeout_Type = Unsigned32
_SignalingInterfaceStatusTcpIdleTimeout_Object = MibTableColumn
signalingInterfaceStatusTcpIdleTimeout = _SignalingInterfaceStatusTcpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 700),
    _SignalingInterfaceStatusTcpIdleTimeout_Type()
)
signalingInterfaceStatusTcpIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusTcpIdleTimeout.setStatus("current")
_SignalingInterfaceStatusIpAddress_Type = MxIpAddress
_SignalingInterfaceStatusIpAddress_Object = MibTableColumn
signalingInterfaceStatusIpAddress = _SignalingInterfaceStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 800),
    _SignalingInterfaceStatusIpAddress_Type()
)
signalingInterfaceStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusIpAddress.setStatus("current")


class _SignalingInterfaceStatusState_Type(Integer32):
    """Custom type signalingInterfaceStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("active", 100),
          ("networkDown", 200),
          ("noIpAddress", 300))
    )


_SignalingInterfaceStatusState_Type.__name__ = "Integer32"
_SignalingInterfaceStatusState_Object = MibTableColumn
signalingInterfaceStatusState = _SignalingInterfaceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 200, 1, 900),
    _SignalingInterfaceStatusState_Type()
)
signalingInterfaceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalingInterfaceStatusState.setStatus("current")
_MediaInterfaceStatusTable_Object = MibTable
mediaInterfaceStatusTable = _MediaInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300)
)
if mibBuilder.loadTexts:
    mediaInterfaceStatusTable.setStatus("current")
_MediaInterfaceStatusEntry_Object = MibTableRow
mediaInterfaceStatusEntry = _MediaInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1)
)
mediaInterfaceStatusEntry.setIndexNames(
    (0, "MX-SBC-MIB", "mediaInterfaceStatusId"),
)
if mibBuilder.loadTexts:
    mediaInterfaceStatusEntry.setStatus("current")
_MediaInterfaceStatusId_Type = Unsigned32
_MediaInterfaceStatusId_Object = MibTableColumn
mediaInterfaceStatusId = _MediaInterfaceStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 100),
    _MediaInterfaceStatusId_Type()
)
mediaInterfaceStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusId.setStatus("current")


class _MediaInterfaceStatusName_Type(OctetString):
    """Custom type mediaInterfaceStatusName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_MediaInterfaceStatusName_Type.__name__ = "OctetString"
_MediaInterfaceStatusName_Object = MibTableColumn
mediaInterfaceStatusName = _MediaInterfaceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 200),
    _MediaInterfaceStatusName_Type()
)
mediaInterfaceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusName.setStatus("current")
_MediaInterfaceStatusNetworkInterface_Type = OctetString
_MediaInterfaceStatusNetworkInterface_Object = MibTableColumn
mediaInterfaceStatusNetworkInterface = _MediaInterfaceStatusNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 300),
    _MediaInterfaceStatusNetworkInterface_Type()
)
mediaInterfaceStatusNetworkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusNetworkInterface.setStatus("current")


class _MediaInterfaceStatusPortRange_Type(OctetString):
    """Custom type mediaInterfaceStatusPortRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MediaInterfaceStatusPortRange_Type.__name__ = "OctetString"
_MediaInterfaceStatusPortRange_Object = MibTableColumn
mediaInterfaceStatusPortRange = _MediaInterfaceStatusPortRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 400),
    _MediaInterfaceStatusPortRange_Type()
)
mediaInterfaceStatusPortRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusPortRange.setStatus("current")
_MediaInterfaceStatusPublicIpAddr_Type = MxIpAddress
_MediaInterfaceStatusPublicIpAddr_Object = MibTableColumn
mediaInterfaceStatusPublicIpAddr = _MediaInterfaceStatusPublicIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 500),
    _MediaInterfaceStatusPublicIpAddr_Type()
)
mediaInterfaceStatusPublicIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusPublicIpAddr.setStatus("current")
_MediaInterfaceStatusIpAddress_Type = MxIpAddress
_MediaInterfaceStatusIpAddress_Object = MibTableColumn
mediaInterfaceStatusIpAddress = _MediaInterfaceStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 600),
    _MediaInterfaceStatusIpAddress_Type()
)
mediaInterfaceStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusIpAddress.setStatus("current")


class _MediaInterfaceStatusState_Type(Integer32):
    """Custom type mediaInterfaceStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("active", 100),
          ("networkDown", 200),
          ("noIpAddress", 300))
    )


_MediaInterfaceStatusState_Type.__name__ = "Integer32"
_MediaInterfaceStatusState_Object = MibTableColumn
mediaInterfaceStatusState = _MediaInterfaceStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 300, 1, 700),
    _MediaInterfaceStatusState_Type()
)
mediaInterfaceStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaInterfaceStatusState.setStatus("current")
_CallAgentRulesetStatusTable_Object = MibTable
callAgentRulesetStatusTable = _CallAgentRulesetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400)
)
if mibBuilder.loadTexts:
    callAgentRulesetStatusTable.setStatus("current")
_CallAgentRulesetStatusEntry_Object = MibTableRow
callAgentRulesetStatusEntry = _CallAgentRulesetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400, 1)
)
callAgentRulesetStatusEntry.setIndexNames(
    (0, "MX-SBC-MIB", "callAgentRulesetStatusId"),
)
if mibBuilder.loadTexts:
    callAgentRulesetStatusEntry.setStatus("current")
_CallAgentRulesetStatusId_Type = Unsigned32
_CallAgentRulesetStatusId_Object = MibTableColumn
callAgentRulesetStatusId = _CallAgentRulesetStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400, 1, 100),
    _CallAgentRulesetStatusId_Type()
)
callAgentRulesetStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetStatusId.setStatus("current")
_CallAgentRulesetStatusCallAgent_Type = Unsigned32
_CallAgentRulesetStatusCallAgent_Object = MibTableColumn
callAgentRulesetStatusCallAgent = _CallAgentRulesetStatusCallAgent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400, 1, 200),
    _CallAgentRulesetStatusCallAgent_Type()
)
callAgentRulesetStatusCallAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetStatusCallAgent.setStatus("current")
_CallAgentRulesetStatusPriority_Type = Unsigned32
_CallAgentRulesetStatusPriority_Object = MibTableColumn
callAgentRulesetStatusPriority = _CallAgentRulesetStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400, 1, 300),
    _CallAgentRulesetStatusPriority_Type()
)
callAgentRulesetStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetStatusPriority.setStatus("current")


class _CallAgentRulesetStatusRuleset_Type(OctetString):
    """Custom type callAgentRulesetStatusRuleset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CallAgentRulesetStatusRuleset_Type.__name__ = "OctetString"
_CallAgentRulesetStatusRuleset_Object = MibTableColumn
callAgentRulesetStatusRuleset = _CallAgentRulesetStatusRuleset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400, 1, 400),
    _CallAgentRulesetStatusRuleset_Type()
)
callAgentRulesetStatusRuleset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetStatusRuleset.setStatus("current")


class _CallAgentRulesetStatusParameters_Type(OctetString):
    """Custom type callAgentRulesetStatusParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CallAgentRulesetStatusParameters_Type.__name__ = "OctetString"
_CallAgentRulesetStatusParameters_Object = MibTableColumn
callAgentRulesetStatusParameters = _CallAgentRulesetStatusParameters_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 400, 1, 500),
    _CallAgentRulesetStatusParameters_Type()
)
callAgentRulesetStatusParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentRulesetStatusParameters.setStatus("current")
_RoutingRulesStatusTable_Object = MibTable
routingRulesStatusTable = _RoutingRulesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 500)
)
if mibBuilder.loadTexts:
    routingRulesStatusTable.setStatus("current")
_RoutingRulesStatusEntry_Object = MibTableRow
routingRulesStatusEntry = _RoutingRulesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 500, 1)
)
routingRulesStatusEntry.setIndexNames(
    (0, "MX-SBC-MIB", "routingRulesStatusId"),
)
if mibBuilder.loadTexts:
    routingRulesStatusEntry.setStatus("current")
_RoutingRulesStatusId_Type = Unsigned32
_RoutingRulesStatusId_Object = MibTableColumn
routingRulesStatusId = _RoutingRulesStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 500, 1, 100),
    _RoutingRulesStatusId_Type()
)
routingRulesStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesStatusId.setStatus("current")
_RoutingRulesStatusPriority_Type = Unsigned32
_RoutingRulesStatusPriority_Object = MibTableColumn
routingRulesStatusPriority = _RoutingRulesStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 500, 1, 200),
    _RoutingRulesStatusPriority_Type()
)
routingRulesStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesStatusPriority.setStatus("current")


class _RoutingRulesStatusRuleset_Type(OctetString):
    """Custom type routingRulesStatusRuleset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RoutingRulesStatusRuleset_Type.__name__ = "OctetString"
_RoutingRulesStatusRuleset_Object = MibTableColumn
routingRulesStatusRuleset = _RoutingRulesStatusRuleset_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 500, 1, 300),
    _RoutingRulesStatusRuleset_Type()
)
routingRulesStatusRuleset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesStatusRuleset.setStatus("current")


class _RoutingRulesStatusParameters_Type(OctetString):
    """Custom type routingRulesStatusParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RoutingRulesStatusParameters_Type.__name__ = "OctetString"
_RoutingRulesStatusParameters_Object = MibTableColumn
routingRulesStatusParameters = _RoutingRulesStatusParameters_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 500, 1, 400),
    _RoutingRulesStatusParameters_Type()
)
routingRulesStatusParameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routingRulesStatusParameters.setStatus("current")
_RegistrationAgentStatusTable_Object = MibTable
registrationAgentStatusTable = _RegistrationAgentStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 600)
)
if mibBuilder.loadTexts:
    registrationAgentStatusTable.setStatus("current")
_RegistrationAgentStatusEntry_Object = MibTableRow
registrationAgentStatusEntry = _RegistrationAgentStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 600, 1)
)
registrationAgentStatusEntry.setIndexNames(
    (0, "MX-SBC-MIB", "registrationAgentStatusId"),
)
if mibBuilder.loadTexts:
    registrationAgentStatusEntry.setStatus("current")
_RegistrationAgentStatusId_Type = Unsigned32
_RegistrationAgentStatusId_Object = MibTableColumn
registrationAgentStatusId = _RegistrationAgentStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 600, 1, 100),
    _RegistrationAgentStatusId_Type()
)
registrationAgentStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationAgentStatusId.setStatus("current")


class _RegistrationAgentStatusState_Type(Integer32):
    """Custom type registrationAgentStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              300,
              400,
              600,
              800,
              1000,
              1100,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("registering", 200),
          ("registered", 300),
          ("refreshing", 400),
          ("unreachable", 600),
          ("rejected", 800),
          ("invalidResponse", 1000),
          ("notFound", 1100),
          ("unknown", 1200))
    )


_RegistrationAgentStatusState_Type.__name__ = "Integer32"
_RegistrationAgentStatusState_Object = MibTableColumn
registrationAgentStatusState = _RegistrationAgentStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 200, 600, 1, 200),
    _RegistrationAgentStatusState_Type()
)
registrationAgentStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationAgentStatusState.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300)
)
_NbActiveCalls_Type = Unsigned32
_NbActiveCalls_Object = MibScalar
nbActiveCalls = _NbActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 100),
    _NbActiveCalls_Type()
)
nbActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbActiveCalls.setStatus("current")
_CallAgentStatsTable_Object = MibTable
callAgentStatsTable = _CallAgentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200)
)
if mibBuilder.loadTexts:
    callAgentStatsTable.setStatus("current")
_CallAgentStatsEntry_Object = MibTableRow
callAgentStatsEntry = _CallAgentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200, 1)
)
callAgentStatsEntry.setIndexNames(
    (0, "MX-SBC-MIB", "callAgentStatsCallAgent"),
)
if mibBuilder.loadTexts:
    callAgentStatsEntry.setStatus("current")
_CallAgentStatsCallAgent_Type = Unsigned32
_CallAgentStatsCallAgent_Object = MibTableColumn
callAgentStatsCallAgent = _CallAgentStatsCallAgent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200, 1, 100),
    _CallAgentStatsCallAgent_Type()
)
callAgentStatsCallAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatsCallAgent.setStatus("current")
_CallAgentStatsInboundCallAttempts_Type = Unsigned32
_CallAgentStatsInboundCallAttempts_Object = MibTableColumn
callAgentStatsInboundCallAttempts = _CallAgentStatsInboundCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200, 1, 200),
    _CallAgentStatsInboundCallAttempts_Type()
)
callAgentStatsInboundCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatsInboundCallAttempts.setStatus("current")
_CallAgentStatsOutboundCallAttempts_Type = Unsigned32
_CallAgentStatsOutboundCallAttempts_Object = MibTableColumn
callAgentStatsOutboundCallAttempts = _CallAgentStatsOutboundCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200, 1, 300),
    _CallAgentStatsOutboundCallAttempts_Type()
)
callAgentStatsOutboundCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatsOutboundCallAttempts.setStatus("current")
_CallAgentStatsInboundCallCompleted_Type = Unsigned32
_CallAgentStatsInboundCallCompleted_Object = MibTableColumn
callAgentStatsInboundCallCompleted = _CallAgentStatsInboundCallCompleted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200, 1, 400),
    _CallAgentStatsInboundCallCompleted_Type()
)
callAgentStatsInboundCallCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatsInboundCallCompleted.setStatus("current")
_CallAgentStatsOutboundCallCompleted_Type = Unsigned32
_CallAgentStatsOutboundCallCompleted_Object = MibTableColumn
callAgentStatsOutboundCallCompleted = _CallAgentStatsOutboundCallCompleted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 300, 200, 1, 500),
    _CallAgentStatsOutboundCallCompleted_Type()
)
callAgentStatsOutboundCallCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callAgentStatsOutboundCallCompleted.setStatus("current")
_TransportGroup_ObjectIdentity = ObjectIdentity
transportGroup = _TransportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 400)
)


class _CertificateValidation_Type(Integer32):
    """Custom type certificateValidation based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("noValidation", 100),
          ("hostName", 200))
    )


_CertificateValidation_Type.__name__ = "Integer32"
_CertificateValidation_Object = MibScalar
certificateValidation = _CertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 400, 100),
    _CertificateValidation_Type()
)
certificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateValidation.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4400, 1, 60020, 100),
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
    "MX-SBC-MIB",
    **{"sbcMIB": sbcMIB,
       "sbcMIBObjects": sbcMIBObjects,
       "configGroup": configGroup,
       "callAgentTable": callAgentTable,
       "callAgentEntry": callAgentEntry,
       "callAgentId": callAgentId,
       "callAgentName": callAgentName,
       "callAgentEnable": callAgentEnable,
       "callAgentSignalingInterface": callAgentSignalingInterface,
       "callAgentMediaInterface": callAgentMediaInterface,
       "callAgentGateway": callAgentGateway,
       "callAgentPeerHost": callAgentPeerHost,
       "callAgentPeerNetwork": callAgentPeerNetwork,
       "callAgentForceTransport": callAgentForceTransport,
       "callAgentConfigStatus": callAgentConfigStatus,
       "callAgentDelete": callAgentDelete,
       "callAgentRulesetTable": callAgentRulesetTable,
       "callAgentRulesetEntry": callAgentRulesetEntry,
       "callAgentRulesetId": callAgentRulesetId,
       "callAgentRulesetCallAgent": callAgentRulesetCallAgent,
       "callAgentRulesetPriority": callAgentRulesetPriority,
       "callAgentRulesetRuleset": callAgentRulesetRuleset,
       "callAgentRulesetParameters": callAgentRulesetParameters,
       "callAgentRulesetConfigStatus": callAgentRulesetConfigStatus,
       "callAgentRulesetDelete": callAgentRulesetDelete,
       "callAgentRulesetCatalogTable": callAgentRulesetCatalogTable,
       "callAgentRulesetCatalogEntry": callAgentRulesetCatalogEntry,
       "callAgentRulesetCatalogId": callAgentRulesetCatalogId,
       "callAgentRulesetCatalogName": callAgentRulesetCatalogName,
       "callAgentRulesetCatalogDescription": callAgentRulesetCatalogDescription,
       "callAgentRulesetCatalogOrigin": callAgentRulesetCatalogOrigin,
       "routingRulesTable": routingRulesTable,
       "routingRulesEntry": routingRulesEntry,
       "routingRulesId": routingRulesId,
       "routingRulesPriority": routingRulesPriority,
       "routingRulesRuleset": routingRulesRuleset,
       "routingRulesParameters": routingRulesParameters,
       "routingRulesConfigStatus": routingRulesConfigStatus,
       "routingRulesDelete": routingRulesDelete,
       "routingRulesetCatalogTable": routingRulesetCatalogTable,
       "routingRulesetCatalogEntry": routingRulesetCatalogEntry,
       "routingRulesetCatalogId": routingRulesetCatalogId,
       "routingRulesetCatalogName": routingRulesetCatalogName,
       "routingRulesetCatalogDescription": routingRulesetCatalogDescription,
       "routingRulesetCatalogOrigin": routingRulesetCatalogOrigin,
       "signalingInterfaceTable": signalingInterfaceTable,
       "signalingInterfaceEntry": signalingInterfaceEntry,
       "signalingInterfaceId": signalingInterfaceId,
       "signalingInterfaceName": signalingInterfaceName,
       "signalingInterfaceNetworkInterface": signalingInterfaceNetworkInterface,
       "signalingInterfacePort": signalingInterfacePort,
       "signalingInterfaceSecurePort": signalingInterfaceSecurePort,
       "signalingInterfaceTlsMode": signalingInterfaceTlsMode,
       "signalingInterfaceAllowedTransports": signalingInterfaceAllowedTransports,
       "signalingInterfacePublicIpAddr": signalingInterfacePublicIpAddr,
       "signalingInterfaceTcpConnectTimeout": signalingInterfaceTcpConnectTimeout,
       "signalingInterfaceTcpIdleTimeout": signalingInterfaceTcpIdleTimeout,
       "signalingInterfaceConfigStatus": signalingInterfaceConfigStatus,
       "signalingInterfaceDelete": signalingInterfaceDelete,
       "mediaInterfaceTable": mediaInterfaceTable,
       "mediaInterfaceEntry": mediaInterfaceEntry,
       "mediaInterfaceId": mediaInterfaceId,
       "mediaInterfaceName": mediaInterfaceName,
       "mediaInterfaceNetworkInterface": mediaInterfaceNetworkInterface,
       "mediaInterfacePortRange": mediaInterfacePortRange,
       "mediaInterfacePublicIpAddr": mediaInterfacePublicIpAddr,
       "mediaInterfaceConfigStatus": mediaInterfaceConfigStatus,
       "mediaInterfaceDelete": mediaInterfaceDelete,
       "registrationAgentTable": registrationAgentTable,
       "registrationAgentEntry": registrationAgentEntry,
       "registrationAgentId": registrationAgentId,
       "registrationAgentUsername": registrationAgentUsername,
       "registrationAgentDomain": registrationAgentDomain,
       "registrationAgentFriendlyName": registrationAgentFriendlyName,
       "registrationAgentContact": registrationAgentContact,
       "registrationAgentRegistrationType": registrationAgentRegistrationType,
       "registrationAgentExpireValue": registrationAgentExpireValue,
       "registrationAgentRetryInterval": registrationAgentRetryInterval,
       "registrationAgentConfigStatus": registrationAgentConfigStatus,
       "registrationAgentDelete": registrationAgentDelete,
       "peerMonitoringTable": peerMonitoringTable,
       "peerMonitoringEntry": peerMonitoringEntry,
       "peerMonitoringId": peerMonitoringId,
       "peerMonitoringKeepAliveInterval": peerMonitoringKeepAliveInterval,
       "peerMonitoringBlackListingDuration": peerMonitoringBlackListingDuration,
       "peerMonitoringBlackListingDelay": peerMonitoringBlackListingDelay,
       "peerMonitoringBlackListingErrorCodes": peerMonitoringBlackListingErrorCodes,
       "configModifiedStatus": configModifiedStatus,
       "routingGroup": routingGroup,
       "prefixBasedRoutingTable": prefixBasedRoutingTable,
       "prefixBasedRoutingEntry": prefixBasedRoutingEntry,
       "prefixBasedRoutingRuleId": prefixBasedRoutingRuleId,
       "prefixBasedRoutingPrefix": prefixBasedRoutingPrefix,
       "prefixBasedRoutingDestinationCa": prefixBasedRoutingDestinationCa,
       "prefixBasedRoutingRoutingMethod": prefixBasedRoutingRoutingMethod,
       "prefixBasedRoutingDestinationOverride": prefixBasedRoutingDestinationOverride,
       "prefixBasedRoutingRUriHandling": prefixBasedRoutingRUriHandling,
       "prefixBasedRoutingForceTransport": prefixBasedRoutingForceTransport,
       "prefixBasedRoutingConfigStatus": prefixBasedRoutingConfigStatus,
       "prefixBasedRoutingDelete": prefixBasedRoutingDelete,
       "registrationGroup": registrationGroup,
       "staticRegistrationTable": staticRegistrationTable,
       "staticRegistrationEntry": staticRegistrationEntry,
       "staticRegistrationRegistrationId": staticRegistrationRegistrationId,
       "staticRegistrationAor": staticRegistrationAor,
       "staticRegistrationContact": staticRegistrationContact,
       "staticRegistrationConfigStatus": staticRegistrationConfigStatus,
       "staticRegistrationDelete": staticRegistrationDelete,
       "statusGroup": statusGroup,
       "callAgentStatusTable": callAgentStatusTable,
       "callAgentStatusEntry": callAgentStatusEntry,
       "callAgentStatusId": callAgentStatusId,
       "callAgentStatusName": callAgentStatusName,
       "callAgentStatusSignalingInterface": callAgentStatusSignalingInterface,
       "callAgentStatusMediaInterface": callAgentStatusMediaInterface,
       "callAgentStatusGateway": callAgentStatusGateway,
       "callAgentStatusPeerHost": callAgentStatusPeerHost,
       "callAgentStatusState": callAgentStatusState,
       "signalingInterfaceStatusTable": signalingInterfaceStatusTable,
       "signalingInterfaceStatusEntry": signalingInterfaceStatusEntry,
       "signalingInterfaceStatusId": signalingInterfaceStatusId,
       "signalingInterfaceStatusName": signalingInterfaceStatusName,
       "signalingInterfaceStatusNetworkInterface": signalingInterfaceStatusNetworkInterface,
       "signalingInterfaceStatusPort": signalingInterfaceStatusPort,
       "signalingInterfaceStatusSecurePort": signalingInterfaceStatusSecurePort,
       "signalingInterfaceStatusTlsMode": signalingInterfaceStatusTlsMode,
       "signalingInterfaceStatusAllowedTransports": signalingInterfaceStatusAllowedTransports,
       "signalingInterfaceStatusPublicIpAddr": signalingInterfaceStatusPublicIpAddr,
       "signalingInterfaceStatusTcpConnectTimeout": signalingInterfaceStatusTcpConnectTimeout,
       "signalingInterfaceStatusTcpIdleTimeout": signalingInterfaceStatusTcpIdleTimeout,
       "signalingInterfaceStatusIpAddress": signalingInterfaceStatusIpAddress,
       "signalingInterfaceStatusState": signalingInterfaceStatusState,
       "mediaInterfaceStatusTable": mediaInterfaceStatusTable,
       "mediaInterfaceStatusEntry": mediaInterfaceStatusEntry,
       "mediaInterfaceStatusId": mediaInterfaceStatusId,
       "mediaInterfaceStatusName": mediaInterfaceStatusName,
       "mediaInterfaceStatusNetworkInterface": mediaInterfaceStatusNetworkInterface,
       "mediaInterfaceStatusPortRange": mediaInterfaceStatusPortRange,
       "mediaInterfaceStatusPublicIpAddr": mediaInterfaceStatusPublicIpAddr,
       "mediaInterfaceStatusIpAddress": mediaInterfaceStatusIpAddress,
       "mediaInterfaceStatusState": mediaInterfaceStatusState,
       "callAgentRulesetStatusTable": callAgentRulesetStatusTable,
       "callAgentRulesetStatusEntry": callAgentRulesetStatusEntry,
       "callAgentRulesetStatusId": callAgentRulesetStatusId,
       "callAgentRulesetStatusCallAgent": callAgentRulesetStatusCallAgent,
       "callAgentRulesetStatusPriority": callAgentRulesetStatusPriority,
       "callAgentRulesetStatusRuleset": callAgentRulesetStatusRuleset,
       "callAgentRulesetStatusParameters": callAgentRulesetStatusParameters,
       "routingRulesStatusTable": routingRulesStatusTable,
       "routingRulesStatusEntry": routingRulesStatusEntry,
       "routingRulesStatusId": routingRulesStatusId,
       "routingRulesStatusPriority": routingRulesStatusPriority,
       "routingRulesStatusRuleset": routingRulesStatusRuleset,
       "routingRulesStatusParameters": routingRulesStatusParameters,
       "registrationAgentStatusTable": registrationAgentStatusTable,
       "registrationAgentStatusEntry": registrationAgentStatusEntry,
       "registrationAgentStatusId": registrationAgentStatusId,
       "registrationAgentStatusState": registrationAgentStatusState,
       "statisticsGroup": statisticsGroup,
       "nbActiveCalls": nbActiveCalls,
       "callAgentStatsTable": callAgentStatsTable,
       "callAgentStatsEntry": callAgentStatsEntry,
       "callAgentStatsCallAgent": callAgentStatsCallAgent,
       "callAgentStatsInboundCallAttempts": callAgentStatsInboundCallAttempts,
       "callAgentStatsOutboundCallAttempts": callAgentStatsOutboundCallAttempts,
       "callAgentStatsInboundCallCompleted": callAgentStatsInboundCallCompleted,
       "callAgentStatsOutboundCallCompleted": callAgentStatsOutboundCallCompleted,
       "transportGroup": transportGroup,
       "certificateValidation": certificateValidation,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
