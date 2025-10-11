# SNMP MIB module (MX-IPROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-IPROUTING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:26 2025
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

ipRoutingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpRoutingMIBObjects_ObjectIdentity = ObjectIdentity
ipRoutingMIBObjects = _IpRoutingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1)
)
_AdvancedIpRoutesTable_Object = MibTable
advancedIpRoutesTable = _AdvancedIpRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200)
)
if mibBuilder.loadTexts:
    advancedIpRoutesTable.setStatus("current")
_AdvancedIpRoutesEntry_Object = MibTableRow
advancedIpRoutesEntry = _AdvancedIpRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1)
)
advancedIpRoutesEntry.setIndexNames(
    (0, "MX-IPROUTING-MIB", "advancedIpRoutesId"),
)
if mibBuilder.loadTexts:
    advancedIpRoutesEntry.setStatus("current")
_AdvancedIpRoutesId_Type = Unsigned32
_AdvancedIpRoutesId_Object = MibTableColumn
advancedIpRoutesId = _AdvancedIpRoutesId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 50),
    _AdvancedIpRoutesId_Type()
)
advancedIpRoutesId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesId.setStatus("current")


class _AdvancedIpRoutesPriority_Type(Unsigned32):
    """Custom type advancedIpRoutesPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 252),
    )


_AdvancedIpRoutesPriority_Type.__name__ = "Unsigned32"
_AdvancedIpRoutesPriority_Object = MibTableColumn
advancedIpRoutesPriority = _AdvancedIpRoutesPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 100),
    _AdvancedIpRoutesPriority_Type()
)
advancedIpRoutesPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedIpRoutesPriority.setStatus("current")


class _AdvancedIpRoutesActivation_Type(MxEnableState):
    """Custom type advancedIpRoutesActivation based on MxEnableState"""
    defaultValue = 0


_AdvancedIpRoutesActivation_Type.__name__ = "MxEnableState"
_AdvancedIpRoutesActivation_Object = MibTableColumn
advancedIpRoutesActivation = _AdvancedIpRoutesActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 200),
    _AdvancedIpRoutesActivation_Type()
)
advancedIpRoutesActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedIpRoutesActivation.setStatus("current")


class _AdvancedIpRoutesSourceAddress_Type(OctetString):
    """Custom type advancedIpRoutesSourceAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_AdvancedIpRoutesSourceAddress_Type.__name__ = "OctetString"
_AdvancedIpRoutesSourceAddress_Object = MibTableColumn
advancedIpRoutesSourceAddress = _AdvancedIpRoutesSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 300),
    _AdvancedIpRoutesSourceAddress_Type()
)
advancedIpRoutesSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedIpRoutesSourceAddress.setStatus("current")


class _AdvancedIpRoutesSourceLink_Type(OctetString):
    """Custom type advancedIpRoutesSourceLink based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_AdvancedIpRoutesSourceLink_Type.__name__ = "OctetString"
_AdvancedIpRoutesSourceLink_Object = MibTableColumn
advancedIpRoutesSourceLink = _AdvancedIpRoutesSourceLink_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 400),
    _AdvancedIpRoutesSourceLink_Type()
)
advancedIpRoutesSourceLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedIpRoutesSourceLink.setStatus("current")


class _AdvancedIpRoutesForwardToNetwork_Type(OctetString):
    """Custom type advancedIpRoutesForwardToNetwork based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_AdvancedIpRoutesForwardToNetwork_Type.__name__ = "OctetString"
_AdvancedIpRoutesForwardToNetwork_Object = MibTableColumn
advancedIpRoutesForwardToNetwork = _AdvancedIpRoutesForwardToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 500),
    _AdvancedIpRoutesForwardToNetwork_Type()
)
advancedIpRoutesForwardToNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedIpRoutesForwardToNetwork.setStatus("current")


class _AdvancedIpRoutesDelete_Type(Integer32):
    """Custom type advancedIpRoutesDelete based on Integer32"""
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


_AdvancedIpRoutesDelete_Type.__name__ = "Integer32"
_AdvancedIpRoutesDelete_Object = MibTableColumn
advancedIpRoutesDelete = _AdvancedIpRoutesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 200, 1, 900),
    _AdvancedIpRoutesDelete_Type()
)
advancedIpRoutesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    advancedIpRoutesDelete.setStatus("current")
_StaticIpRoutesTable_Object = MibTable
staticIpRoutesTable = _StaticIpRoutesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600)
)
if mibBuilder.loadTexts:
    staticIpRoutesTable.setStatus("current")
_StaticIpRoutesEntry_Object = MibTableRow
staticIpRoutesEntry = _StaticIpRoutesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600, 1)
)
staticIpRoutesEntry.setIndexNames(
    (0, "MX-IPROUTING-MIB", "staticIpRoutesIndex"),
)
if mibBuilder.loadTexts:
    staticIpRoutesEntry.setStatus("current")
_StaticIpRoutesIndex_Type = Unsigned32
_StaticIpRoutesIndex_Object = MibTableColumn
staticIpRoutesIndex = _StaticIpRoutesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600, 1, 100),
    _StaticIpRoutesIndex_Type()
)
staticIpRoutesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticIpRoutesIndex.setStatus("current")


class _StaticIpRoutesLink_Type(OctetString):
    """Custom type staticIpRoutesLink based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_StaticIpRoutesLink_Type.__name__ = "OctetString"
_StaticIpRoutesLink_Object = MibTableColumn
staticIpRoutesLink = _StaticIpRoutesLink_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600, 1, 200),
    _StaticIpRoutesLink_Type()
)
staticIpRoutesLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpRoutesLink.setStatus("current")


class _StaticIpRoutesDestination_Type(OctetString):
    """Custom type staticIpRoutesDestination based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_StaticIpRoutesDestination_Type.__name__ = "OctetString"
_StaticIpRoutesDestination_Object = MibTableColumn
staticIpRoutesDestination = _StaticIpRoutesDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600, 1, 300),
    _StaticIpRoutesDestination_Type()
)
staticIpRoutesDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpRoutesDestination.setStatus("current")


class _StaticIpRoutesGateway_Type(OctetString):
    """Custom type staticIpRoutesGateway based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 51),
    )


_StaticIpRoutesGateway_Type.__name__ = "OctetString"
_StaticIpRoutesGateway_Object = MibTableColumn
staticIpRoutesGateway = _StaticIpRoutesGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600, 1, 400),
    _StaticIpRoutesGateway_Type()
)
staticIpRoutesGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpRoutesGateway.setStatus("current")


class _StaticIpRoutesDelete_Type(Integer32):
    """Custom type staticIpRoutesDelete based on Integer32"""
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


_StaticIpRoutesDelete_Type.__name__ = "Integer32"
_StaticIpRoutesDelete_Object = MibTableColumn
staticIpRoutesDelete = _StaticIpRoutesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 600, 1, 500),
    _StaticIpRoutesDelete_Type()
)
staticIpRoutesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpRoutesDelete.setStatus("current")


class _Ipv4ForwardingEnable_Type(MxEnableState):
    """Custom type ipv4ForwardingEnable based on MxEnableState"""
    defaultValue = 1


_Ipv4ForwardingEnable_Type.__name__ = "MxEnableState"
_Ipv4ForwardingEnable_Object = MibScalar
ipv4ForwardingEnable = _Ipv4ForwardingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 800),
    _Ipv4ForwardingEnable_Type()
)
ipv4ForwardingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv4ForwardingEnable.setStatus("current")
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 100),
    _ConfigModifiedStatus_Type()
)
configModifiedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModifiedStatus.setStatus("current")
_AdvancedIpRoutesStatusTable_Object = MibTable
advancedIpRoutesStatusTable = _AdvancedIpRoutesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200)
)
if mibBuilder.loadTexts:
    advancedIpRoutesStatusTable.setStatus("current")
_AdvancedIpRoutesStatusEntry_Object = MibTableRow
advancedIpRoutesStatusEntry = _AdvancedIpRoutesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1)
)
advancedIpRoutesStatusEntry.setIndexNames(
    (0, "MX-IPROUTING-MIB", "advancedIpRoutesStatusId"),
)
if mibBuilder.loadTexts:
    advancedIpRoutesStatusEntry.setStatus("current")
_AdvancedIpRoutesStatusId_Type = Unsigned32
_AdvancedIpRoutesStatusId_Object = MibTableColumn
advancedIpRoutesStatusId = _AdvancedIpRoutesStatusId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1, 50),
    _AdvancedIpRoutesStatusId_Type()
)
advancedIpRoutesStatusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesStatusId.setStatus("current")
_AdvancedIpRoutesStatusPriority_Type = Unsigned32
_AdvancedIpRoutesStatusPriority_Object = MibTableColumn
advancedIpRoutesStatusPriority = _AdvancedIpRoutesStatusPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1, 100),
    _AdvancedIpRoutesStatusPriority_Type()
)
advancedIpRoutesStatusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesStatusPriority.setStatus("current")
_AdvancedIpRoutesStatusSourceAddress_Type = OctetString
_AdvancedIpRoutesStatusSourceAddress_Object = MibTableColumn
advancedIpRoutesStatusSourceAddress = _AdvancedIpRoutesStatusSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1, 200),
    _AdvancedIpRoutesStatusSourceAddress_Type()
)
advancedIpRoutesStatusSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesStatusSourceAddress.setStatus("current")
_AdvancedIpRoutesStatusSourceLink_Type = OctetString
_AdvancedIpRoutesStatusSourceLink_Object = MibTableColumn
advancedIpRoutesStatusSourceLink = _AdvancedIpRoutesStatusSourceLink_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1, 300),
    _AdvancedIpRoutesStatusSourceLink_Type()
)
advancedIpRoutesStatusSourceLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesStatusSourceLink.setStatus("current")
_AdvancedIpRoutesStatusForwardToNetwork_Type = OctetString
_AdvancedIpRoutesStatusForwardToNetwork_Object = MibTableColumn
advancedIpRoutesStatusForwardToNetwork = _AdvancedIpRoutesStatusForwardToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1, 350),
    _AdvancedIpRoutesStatusForwardToNetwork_Type()
)
advancedIpRoutesStatusForwardToNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesStatusForwardToNetwork.setStatus("current")


class _AdvancedIpRoutesStatusStatus_Type(Integer32):
    """Custom type advancedIpRoutesStatusStatus based on Integer32"""
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
        *(("disabled", 100),
          ("invalidConfig", 200),
          ("active", 300),
          ("duplicatePriority", 400))
    )


_AdvancedIpRoutesStatusStatus_Type.__name__ = "Integer32"
_AdvancedIpRoutesStatusStatus_Object = MibTableColumn
advancedIpRoutesStatusStatus = _AdvancedIpRoutesStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 200, 1, 400),
    _AdvancedIpRoutesStatusStatus_Type()
)
advancedIpRoutesStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    advancedIpRoutesStatusStatus.setStatus("current")
_IpRoutesStatusTable_Object = MibTable
ipRoutesStatusTable = _IpRoutesStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300)
)
if mibBuilder.loadTexts:
    ipRoutesStatusTable.setStatus("current")
_IpRoutesStatusEntry_Object = MibTableRow
ipRoutesStatusEntry = _IpRoutesStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300, 1)
)
ipRoutesStatusEntry.setIndexNames(
    (0, "MX-IPROUTING-MIB", "ipRoutesStatusIndex"),
)
if mibBuilder.loadTexts:
    ipRoutesStatusEntry.setStatus("current")
_IpRoutesStatusIndex_Type = Unsigned32
_IpRoutesStatusIndex_Object = MibTableColumn
ipRoutesStatusIndex = _IpRoutesStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300, 1, 100),
    _IpRoutesStatusIndex_Type()
)
ipRoutesStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesStatusIndex.setStatus("current")
_IpRoutesStatusLink_Type = OctetString
_IpRoutesStatusLink_Object = MibTableColumn
ipRoutesStatusLink = _IpRoutesStatusLink_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300, 1, 200),
    _IpRoutesStatusLink_Type()
)
ipRoutesStatusLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesStatusLink.setStatus("current")
_IpRoutesStatusDestination_Type = OctetString
_IpRoutesStatusDestination_Object = MibTableColumn
ipRoutesStatusDestination = _IpRoutesStatusDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300, 1, 300),
    _IpRoutesStatusDestination_Type()
)
ipRoutesStatusDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesStatusDestination.setStatus("current")
_IpRoutesStatusGateway_Type = OctetString
_IpRoutesStatusGateway_Object = MibTableColumn
ipRoutesStatusGateway = _IpRoutesStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300, 1, 400),
    _IpRoutesStatusGateway_Type()
)
ipRoutesStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesStatusGateway.setStatus("current")


class _IpRoutesStatusProtocol_Type(Integer32):
    """Custom type ipRoutesStatusProtocol based on Integer32"""
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
        *(("other", 100),
          ("kernel", 200),
          ("static", 300),
          ("dhcp", 400))
    )


_IpRoutesStatusProtocol_Type.__name__ = "Integer32"
_IpRoutesStatusProtocol_Object = MibTableColumn
ipRoutesStatusProtocol = _IpRoutesStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 10000, 300, 1, 500),
    _IpRoutesStatusProtocol_Type()
)
ipRoutesStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutesStatusProtocol.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 3500, 1, 60020, 100),
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
    "MX-IPROUTING-MIB",
    **{"ipRoutingMIB": ipRoutingMIB,
       "ipRoutingMIBObjects": ipRoutingMIBObjects,
       "advancedIpRoutesTable": advancedIpRoutesTable,
       "advancedIpRoutesEntry": advancedIpRoutesEntry,
       "advancedIpRoutesId": advancedIpRoutesId,
       "advancedIpRoutesPriority": advancedIpRoutesPriority,
       "advancedIpRoutesActivation": advancedIpRoutesActivation,
       "advancedIpRoutesSourceAddress": advancedIpRoutesSourceAddress,
       "advancedIpRoutesSourceLink": advancedIpRoutesSourceLink,
       "advancedIpRoutesForwardToNetwork": advancedIpRoutesForwardToNetwork,
       "advancedIpRoutesDelete": advancedIpRoutesDelete,
       "staticIpRoutesTable": staticIpRoutesTable,
       "staticIpRoutesEntry": staticIpRoutesEntry,
       "staticIpRoutesIndex": staticIpRoutesIndex,
       "staticIpRoutesLink": staticIpRoutesLink,
       "staticIpRoutesDestination": staticIpRoutesDestination,
       "staticIpRoutesGateway": staticIpRoutesGateway,
       "staticIpRoutesDelete": staticIpRoutesDelete,
       "ipv4ForwardingEnable": ipv4ForwardingEnable,
       "statusGroup": statusGroup,
       "configModifiedStatus": configModifiedStatus,
       "advancedIpRoutesStatusTable": advancedIpRoutesStatusTable,
       "advancedIpRoutesStatusEntry": advancedIpRoutesStatusEntry,
       "advancedIpRoutesStatusId": advancedIpRoutesStatusId,
       "advancedIpRoutesStatusPriority": advancedIpRoutesStatusPriority,
       "advancedIpRoutesStatusSourceAddress": advancedIpRoutesStatusSourceAddress,
       "advancedIpRoutesStatusSourceLink": advancedIpRoutesStatusSourceLink,
       "advancedIpRoutesStatusForwardToNetwork": advancedIpRoutesStatusForwardToNetwork,
       "advancedIpRoutesStatusStatus": advancedIpRoutesStatusStatus,
       "ipRoutesStatusTable": ipRoutesStatusTable,
       "ipRoutesStatusEntry": ipRoutesStatusEntry,
       "ipRoutesStatusIndex": ipRoutesStatusIndex,
       "ipRoutesStatusLink": ipRoutesStatusLink,
       "ipRoutesStatusDestination": ipRoutesStatusDestination,
       "ipRoutesStatusGateway": ipRoutesStatusGateway,
       "ipRoutesStatusProtocol": ipRoutesStatusProtocol,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
