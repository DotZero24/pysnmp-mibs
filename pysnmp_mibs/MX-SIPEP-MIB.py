# SNMP MIB module (MX-SIPEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SIPEP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:56 2025
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

sipEpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SipEpMIBObjects_ObjectIdentity = ObjectIdentity
sipEpMIBObjects = _SipEpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1)
)
_GatewayTable_Object = MibTable
gatewayTable = _GatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100)
)
if mibBuilder.loadTexts:
    gatewayTable.setStatus("current")
_GatewayEntry_Object = MibTableRow
gatewayEntry = _GatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1)
)
gatewayEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gatewayName"),
)
if mibBuilder.loadTexts:
    gatewayEntry.setStatus("current")
_GatewayName_Type = OctetString
_GatewayName_Object = MibTableColumn
gatewayName = _GatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 100),
    _GatewayName_Type()
)
gatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayName.setStatus("current")


class _GatewayType_Type(Integer32):
    """Custom type gatewayType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("trunkGateway", 100),
          ("endpointGateway", 200))
    )


_GatewayType_Type.__name__ = "Integer32"
_GatewayType_Object = MibTableColumn
gatewayType = _GatewayType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 150),
    _GatewayType_Type()
)
gatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayType.setStatus("current")


class _GatewayNetworkInterface_Type(OctetString):
    """Custom type gatewayNetworkInterface based on OctetString"""
    defaultValue = OctetString("Lan1")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_GatewayNetworkInterface_Type.__name__ = "OctetString"
_GatewayNetworkInterface_Object = MibTableColumn
gatewayNetworkInterface = _GatewayNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 200),
    _GatewayNetworkInterface_Type()
)
gatewayNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayNetworkInterface.setStatus("current")


class _GatewayMediaNetworks_Type(OctetString):
    """Custom type gatewayMediaNetworks based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GatewayMediaNetworks_Type.__name__ = "OctetString"
_GatewayMediaNetworks_Object = MibTableColumn
gatewayMediaNetworks = _GatewayMediaNetworks_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 250),
    _GatewayMediaNetworks_Type()
)
gatewayMediaNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayMediaNetworks.setStatus("current")


class _GatewayPort_Type(MxAdvancedIpPort):
    """Custom type gatewayPort based on MxAdvancedIpPort"""
    defaultValue = 0


_GatewayPort_Type.__name__ = "MxAdvancedIpPort"
_GatewayPort_Object = MibTableColumn
gatewayPort = _GatewayPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 300),
    _GatewayPort_Type()
)
gatewayPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayPort.setStatus("current")


class _GatewaySecurePort_Type(MxAdvancedIpPort):
    """Custom type gatewaySecurePort based on MxAdvancedIpPort"""
    defaultValue = 0


_GatewaySecurePort_Type.__name__ = "MxAdvancedIpPort"
_GatewaySecurePort_Object = MibTableColumn
gatewaySecurePort = _GatewaySecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 325),
    _GatewaySecurePort_Type()
)
gatewaySecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewaySecurePort.setStatus("current")


class _GatewayDomain_Type(OctetString):
    """Custom type gatewayDomain based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GatewayDomain_Type.__name__ = "OctetString"
_GatewayDomain_Object = MibTableColumn
gatewayDomain = _GatewayDomain_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 350),
    _GatewayDomain_Type()
)
gatewayDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayDomain.setStatus("current")


class _GatewayDelete_Type(Integer32):
    """Custom type gatewayDelete based on Integer32"""
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


_GatewayDelete_Type.__name__ = "Integer32"
_GatewayDelete_Object = MibTableColumn
gatewayDelete = _GatewayDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 100, 1, 400),
    _GatewayDelete_Type()
)
gatewayDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayDelete.setStatus("current")
_GatewayStatusTable_Object = MibTable
gatewayStatusTable = _GatewayStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150)
)
if mibBuilder.loadTexts:
    gatewayStatusTable.setStatus("current")
_GatewayStatusEntry_Object = MibTableRow
gatewayStatusEntry = _GatewayStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1)
)
gatewayStatusEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gatewayStatusName"),
)
if mibBuilder.loadTexts:
    gatewayStatusEntry.setStatus("current")
_GatewayStatusName_Type = OctetString
_GatewayStatusName_Object = MibTableColumn
gatewayStatusName = _GatewayStatusName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 100),
    _GatewayStatusName_Type()
)
gatewayStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusName.setStatus("current")
_GatewayStatusNetworkInterface_Type = OctetString
_GatewayStatusNetworkInterface_Object = MibTableColumn
gatewayStatusNetworkInterface = _GatewayStatusNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 200),
    _GatewayStatusNetworkInterface_Type()
)
gatewayStatusNetworkInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusNetworkInterface.setStatus("current")
_GatewayStatusMediaNetworks_Type = OctetString
_GatewayStatusMediaNetworks_Object = MibTableColumn
gatewayStatusMediaNetworks = _GatewayStatusMediaNetworks_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 250),
    _GatewayStatusMediaNetworks_Type()
)
gatewayStatusMediaNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusMediaNetworks.setStatus("current")
_GatewayStatusPort_Type = MxAdvancedIpPort
_GatewayStatusPort_Object = MibTableColumn
gatewayStatusPort = _GatewayStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 300),
    _GatewayStatusPort_Type()
)
gatewayStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusPort.setStatus("current")
_GatewayStatusSecurePort_Type = MxAdvancedIpPort
_GatewayStatusSecurePort_Object = MibTableColumn
gatewayStatusSecurePort = _GatewayStatusSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 325),
    _GatewayStatusSecurePort_Type()
)
gatewayStatusSecurePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusSecurePort.setStatus("current")
_GatewayStatusDomain_Type = OctetString
_GatewayStatusDomain_Object = MibTableColumn
gatewayStatusDomain = _GatewayStatusDomain_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 350),
    _GatewayStatusDomain_Type()
)
gatewayStatusDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusDomain.setStatus("current")
_GatewayStatusState_Type = OctetString
_GatewayStatusState_Object = MibTableColumn
gatewayStatusState = _GatewayStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 150, 1, 400),
    _GatewayStatusState_Type()
)
gatewayStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayStatusState.setStatus("current")
_UserAgentTable_Object = MibTable
userAgentTable = _UserAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400)
)
if mibBuilder.loadTexts:
    userAgentTable.setStatus("current")
_UserAgentEntry_Object = MibTableRow
userAgentEntry = _UserAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1)
)
userAgentEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "userAgentEpId"),
)
if mibBuilder.loadTexts:
    userAgentEntry.setStatus("current")
_UserAgentEpId_Type = OctetString
_UserAgentEpId_Object = MibTableColumn
userAgentEpId = _UserAgentEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 100),
    _UserAgentEpId_Type()
)
userAgentEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userAgentEpId.setStatus("current")


class _UserAgentUsername_Type(OctetString):
    """Custom type userAgentUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserAgentUsername_Type.__name__ = "OctetString"
_UserAgentUsername_Object = MibTableColumn
userAgentUsername = _UserAgentUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 200),
    _UserAgentUsername_Type()
)
userAgentUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentUsername.setStatus("current")


class _UserAgentFriendlyName_Type(OctetString):
    """Custom type userAgentFriendlyName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserAgentFriendlyName_Type.__name__ = "OctetString"
_UserAgentFriendlyName_Object = MibTableColumn
userAgentFriendlyName = _UserAgentFriendlyName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 300),
    _UserAgentFriendlyName_Type()
)
userAgentFriendlyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentFriendlyName.setStatus("current")


class _UserAgentRegister_Type(MxEnableState):
    """Custom type userAgentRegister based on MxEnableState"""
    defaultValue = 0


_UserAgentRegister_Type.__name__ = "MxEnableState"
_UserAgentRegister_Object = MibTableColumn
userAgentRegister = _UserAgentRegister_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 400),
    _UserAgentRegister_Type()
)
userAgentRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentRegister.setStatus("current")


class _UserAgentGatewayName_Type(OctetString):
    """Custom type userAgentGatewayName based on OctetString"""
    defaultValue = OctetString("all")


_UserAgentGatewayName_Type.__name__ = "OctetString"
_UserAgentGatewayName_Object = MibTableColumn
userAgentGatewayName = _UserAgentGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 500),
    _UserAgentGatewayName_Type()
)
userAgentGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentGatewayName.setStatus("current")


class _UserAgentMwiSubscribe_Type(MxEnableState):
    """Custom type userAgentMwiSubscribe based on MxEnableState"""
    defaultValue = 0


_UserAgentMwiSubscribe_Type.__name__ = "MxEnableState"
_UserAgentMwiSubscribe_Object = MibTableColumn
userAgentMwiSubscribe = _UserAgentMwiSubscribe_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 700),
    _UserAgentMwiSubscribe_Type()
)
userAgentMwiSubscribe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentMwiSubscribe.setStatus("current")


class _UserAgentContactDomain_Type(OctetString):
    """Custom type userAgentContactDomain based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_UserAgentContactDomain_Type.__name__ = "OctetString"
_UserAgentContactDomain_Object = MibTableColumn
userAgentContactDomain = _UserAgentContactDomain_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 800),
    _UserAgentContactDomain_Type()
)
userAgentContactDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentContactDomain.setStatus("current")


class _UserAgentAcceptLanguage_Type(OctetString):
    """Custom type userAgentAcceptLanguage based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UserAgentAcceptLanguage_Type.__name__ = "OctetString"
_UserAgentAcceptLanguage_Object = MibTableColumn
userAgentAcceptLanguage = _UserAgentAcceptLanguage_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 400, 1, 900),
    _UserAgentAcceptLanguage_Type()
)
userAgentAcceptLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userAgentAcceptLanguage.setStatus("current")
_ProxyGroup_ObjectIdentity = ObjectIdentity
proxyGroup = _ProxyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500)
)


class _DefaultStaticProxyHomeDomainHost_Type(MxIpHostNamePort):
    """Custom type defaultStaticProxyHomeDomainHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.10.10:0")


_DefaultStaticProxyHomeDomainHost_Type.__name__ = "MxIpHostNamePort"
_DefaultStaticProxyHomeDomainHost_Object = MibScalar
defaultStaticProxyHomeDomainHost = _DefaultStaticProxyHomeDomainHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 100),
    _DefaultStaticProxyHomeDomainHost_Type()
)
defaultStaticProxyHomeDomainHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticProxyHomeDomainHost.setStatus("current")


class _DefaultStaticProxyOutboundHost_Type(MxIpHostNamePort):
    """Custom type defaultStaticProxyOutboundHost based on MxIpHostNamePort"""
    defaultValue = OctetString("")


_DefaultStaticProxyOutboundHost_Type.__name__ = "MxIpHostNamePort"
_DefaultStaticProxyOutboundHost_Object = MibScalar
defaultStaticProxyOutboundHost = _DefaultStaticProxyOutboundHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 200),
    _DefaultStaticProxyOutboundHost_Type()
)
defaultStaticProxyOutboundHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticProxyOutboundHost.setStatus("current")


class _DefaultProxyOutboundType_Type(Integer32):
    """Custom type defaultProxyOutboundType based on Integer32"""
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
        *(("looseRouter", 100),
          ("strictRouter", 200),
          ("noRouteHeader", 300))
    )


_DefaultProxyOutboundType_Type.__name__ = "Integer32"
_DefaultProxyOutboundType_Object = MibScalar
defaultProxyOutboundType = _DefaultProxyOutboundType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 300),
    _DefaultProxyOutboundType_Type()
)
defaultProxyOutboundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultProxyOutboundType.setStatus("current")
_GwSpecificProxyTable_Object = MibTable
gwSpecificProxyTable = _GwSpecificProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400)
)
if mibBuilder.loadTexts:
    gwSpecificProxyTable.setStatus("current")
_GwSpecificProxyEntry_Object = MibTableRow
gwSpecificProxyEntry = _GwSpecificProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400, 1)
)
gwSpecificProxyEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwSpecificProxyGatewayName"),
)
if mibBuilder.loadTexts:
    gwSpecificProxyEntry.setStatus("current")
_GwSpecificProxyGatewayName_Type = OctetString
_GwSpecificProxyGatewayName_Object = MibTableColumn
gwSpecificProxyGatewayName = _GwSpecificProxyGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400, 1, 100),
    _GwSpecificProxyGatewayName_Type()
)
gwSpecificProxyGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwSpecificProxyGatewayName.setStatus("current")


class _GwSpecificProxyEnableConfig_Type(MxEnableState):
    """Custom type gwSpecificProxyEnableConfig based on MxEnableState"""
    defaultValue = 0


_GwSpecificProxyEnableConfig_Type.__name__ = "MxEnableState"
_GwSpecificProxyEnableConfig_Object = MibTableColumn
gwSpecificProxyEnableConfig = _GwSpecificProxyEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400, 1, 200),
    _GwSpecificProxyEnableConfig_Type()
)
gwSpecificProxyEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificProxyEnableConfig.setStatus("current")


class _GwSpecificProxyHomeDomainHost_Type(MxIpHostNamePort):
    """Custom type gwSpecificProxyHomeDomainHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.0.10:0")


_GwSpecificProxyHomeDomainHost_Type.__name__ = "MxIpHostNamePort"
_GwSpecificProxyHomeDomainHost_Object = MibTableColumn
gwSpecificProxyHomeDomainHost = _GwSpecificProxyHomeDomainHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400, 1, 300),
    _GwSpecificProxyHomeDomainHost_Type()
)
gwSpecificProxyHomeDomainHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificProxyHomeDomainHost.setStatus("current")


class _GwSpecificProxyOutboundHost_Type(MxIpHostNamePort):
    """Custom type gwSpecificProxyOutboundHost based on MxIpHostNamePort"""
    defaultValue = OctetString("0.0.0.0:0")


_GwSpecificProxyOutboundHost_Type.__name__ = "MxIpHostNamePort"
_GwSpecificProxyOutboundHost_Object = MibTableColumn
gwSpecificProxyOutboundHost = _GwSpecificProxyOutboundHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400, 1, 400),
    _GwSpecificProxyOutboundHost_Type()
)
gwSpecificProxyOutboundHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificProxyOutboundHost.setStatus("current")


class _GwSpecificProxyOutboundType_Type(Integer32):
    """Custom type gwSpecificProxyOutboundType based on Integer32"""
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
        *(("looseRouter", 100),
          ("strictRouter", 200),
          ("noRouteHeader", 300))
    )


_GwSpecificProxyOutboundType_Type.__name__ = "Integer32"
_GwSpecificProxyOutboundType_Object = MibTableColumn
gwSpecificProxyOutboundType = _GwSpecificProxyOutboundType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 500, 400, 1, 500),
    _GwSpecificProxyOutboundType_Type()
)
gwSpecificProxyOutboundType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificProxyOutboundType.setStatus("current")
_SessionRefreshGroup_ObjectIdentity = ObjectIdentity
sessionRefreshGroup = _SessionRefreshGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 600)
)


class _DefaultSessionTimerEnable_Type(MxEnableState):
    """Custom type defaultSessionTimerEnable based on MxEnableState"""
    defaultValue = 1


_DefaultSessionTimerEnable_Type.__name__ = "MxEnableState"
_DefaultSessionTimerEnable_Object = MibScalar
defaultSessionTimerEnable = _DefaultSessionTimerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 600, 100),
    _DefaultSessionTimerEnable_Type()
)
defaultSessionTimerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSessionTimerEnable.setStatus("current")


class _DefaultSessionTimerMinimumExpirationDelay_Type(Unsigned32):
    """Custom type defaultSessionTimerMinimumExpirationDelay based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 86400),
    )


_DefaultSessionTimerMinimumExpirationDelay_Type.__name__ = "Unsigned32"
_DefaultSessionTimerMinimumExpirationDelay_Object = MibScalar
defaultSessionTimerMinimumExpirationDelay = _DefaultSessionTimerMinimumExpirationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 600, 200),
    _DefaultSessionTimerMinimumExpirationDelay_Type()
)
defaultSessionTimerMinimumExpirationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSessionTimerMinimumExpirationDelay.setStatus("current")


class _DefaultSessionTimerMaximumExpirationDelay_Type(Unsigned32):
    """Custom type defaultSessionTimerMaximumExpirationDelay based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 86400),
    )


_DefaultSessionTimerMaximumExpirationDelay_Type.__name__ = "Unsigned32"
_DefaultSessionTimerMaximumExpirationDelay_Object = MibScalar
defaultSessionTimerMaximumExpirationDelay = _DefaultSessionTimerMaximumExpirationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 600, 300),
    _DefaultSessionTimerMaximumExpirationDelay_Type()
)
defaultSessionTimerMaximumExpirationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSessionTimerMaximumExpirationDelay.setStatus("current")


class _SessionRefreshRequestMethod_Type(Integer32):
    """Custom type sessionRefreshRequestMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("reInvite", 100),
          ("update", 200))
    )


_SessionRefreshRequestMethod_Type.__name__ = "Integer32"
_SessionRefreshRequestMethod_Object = MibScalar
sessionRefreshRequestMethod = _SessionRefreshRequestMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 600, 400),
    _SessionRefreshRequestMethod_Type()
)
sessionRefreshRequestMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionRefreshRequestMethod.setStatus("current")
_AuthenticationGroup_ObjectIdentity = ObjectIdentity
authenticationGroup = _AuthenticationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700)
)
_AuthenticationTable_Object = MibTable
authenticationTable = _AuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100)
)
if mibBuilder.loadTexts:
    authenticationTable.setStatus("current")
_AuthenticationEntry_Object = MibTableRow
authenticationEntry = _AuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1)
)
authenticationEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "authenticationIndex"),
)
if mibBuilder.loadTexts:
    authenticationEntry.setStatus("current")
_AuthenticationIndex_Type = Unsigned32
_AuthenticationIndex_Object = MibTableColumn
authenticationIndex = _AuthenticationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 100),
    _AuthenticationIndex_Type()
)
authenticationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authenticationIndex.setStatus("current")


class _AuthenticationCriteriaSelection_Type(Integer32):
    """Custom type authenticationCriteriaSelection based on Integer32"""
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
        *(("unit", 100),
          ("endpoint", 200),
          ("gateway", 300),
          ("username", 400))
    )


_AuthenticationCriteriaSelection_Type.__name__ = "Integer32"
_AuthenticationCriteriaSelection_Object = MibTableColumn
authenticationCriteriaSelection = _AuthenticationCriteriaSelection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 200),
    _AuthenticationCriteriaSelection_Type()
)
authenticationCriteriaSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationCriteriaSelection.setStatus("current")


class _AuthenticationEpId_Type(OctetString):
    """Custom type authenticationEpId based on OctetString"""
    defaultValue = OctetString("")


_AuthenticationEpId_Type.__name__ = "OctetString"
_AuthenticationEpId_Object = MibTableColumn
authenticationEpId = _AuthenticationEpId_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 300),
    _AuthenticationEpId_Type()
)
authenticationEpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationEpId.setStatus("current")


class _AuthenticationGatewayName_Type(OctetString):
    """Custom type authenticationGatewayName based on OctetString"""
    defaultValue = OctetString("")


_AuthenticationGatewayName_Type.__name__ = "OctetString"
_AuthenticationGatewayName_Object = MibTableColumn
authenticationGatewayName = _AuthenticationGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 350),
    _AuthenticationGatewayName_Type()
)
authenticationGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationGatewayName.setStatus("current")


class _AuthenticationUsernameCriteria_Type(OctetString):
    """Custom type authenticationUsernameCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AuthenticationUsernameCriteria_Type.__name__ = "OctetString"
_AuthenticationUsernameCriteria_Object = MibTableColumn
authenticationUsernameCriteria = _AuthenticationUsernameCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 360),
    _AuthenticationUsernameCriteria_Type()
)
authenticationUsernameCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationUsernameCriteria.setStatus("current")


class _AuthenticationValidateRealm_Type(MxEnableState):
    """Custom type authenticationValidateRealm based on MxEnableState"""
    defaultValue = 1


_AuthenticationValidateRealm_Type.__name__ = "MxEnableState"
_AuthenticationValidateRealm_Object = MibTableColumn
authenticationValidateRealm = _AuthenticationValidateRealm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 375),
    _AuthenticationValidateRealm_Type()
)
authenticationValidateRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationValidateRealm.setStatus("current")


class _AuthenticationRealm_Type(OctetString):
    """Custom type authenticationRealm based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AuthenticationRealm_Type.__name__ = "OctetString"
_AuthenticationRealm_Object = MibTableColumn
authenticationRealm = _AuthenticationRealm_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 400),
    _AuthenticationRealm_Type()
)
authenticationRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationRealm.setStatus("current")


class _AuthenticationUsername_Type(OctetString):
    """Custom type authenticationUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AuthenticationUsername_Type.__name__ = "OctetString"
_AuthenticationUsername_Object = MibTableColumn
authenticationUsername = _AuthenticationUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 500),
    _AuthenticationUsername_Type()
)
authenticationUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationUsername.setStatus("current")


class _AuthenticationPassword_Type(OctetString):
    """Custom type authenticationPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AuthenticationPassword_Type.__name__ = "OctetString"
_AuthenticationPassword_Object = MibTableColumn
authenticationPassword = _AuthenticationPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 600),
    _AuthenticationPassword_Type()
)
authenticationPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationPassword.setStatus("current")


class _AuthenticationUp_Type(Integer32):
    """Custom type authenticationUp based on Integer32"""
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


_AuthenticationUp_Type.__name__ = "Integer32"
_AuthenticationUp_Object = MibTableColumn
authenticationUp = _AuthenticationUp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 700),
    _AuthenticationUp_Type()
)
authenticationUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationUp.setStatus("current")


class _AuthenticationDown_Type(Integer32):
    """Custom type authenticationDown based on Integer32"""
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


_AuthenticationDown_Type.__name__ = "Integer32"
_AuthenticationDown_Object = MibTableColumn
authenticationDown = _AuthenticationDown_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 800),
    _AuthenticationDown_Type()
)
authenticationDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationDown.setStatus("current")


class _AuthenticationInsert_Type(Integer32):
    """Custom type authenticationInsert based on Integer32"""
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


_AuthenticationInsert_Type.__name__ = "Integer32"
_AuthenticationInsert_Object = MibTableColumn
authenticationInsert = _AuthenticationInsert_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 900),
    _AuthenticationInsert_Type()
)
authenticationInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationInsert.setStatus("current")


class _AuthenticationDelete_Type(Integer32):
    """Custom type authenticationDelete based on Integer32"""
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


_AuthenticationDelete_Type.__name__ = "Integer32"
_AuthenticationDelete_Object = MibTableColumn
authenticationDelete = _AuthenticationDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 700, 100, 1, 1000),
    _AuthenticationDelete_Type()
)
authenticationDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authenticationDelete.setStatus("current")
_RegistrationGroup_ObjectIdentity = ObjectIdentity
registrationGroup = _RegistrationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800)
)


class _DefaultRegistrationRefreshTime_Type(Unsigned32):
    """Custom type defaultRegistrationRefreshTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_DefaultRegistrationRefreshTime_Type.__name__ = "Unsigned32"
_DefaultRegistrationRefreshTime_Object = MibScalar
defaultRegistrationRefreshTime = _DefaultRegistrationRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 200),
    _DefaultRegistrationRefreshTime_Type()
)
defaultRegistrationRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRegistrationRefreshTime.setStatus("current")


class _DefaultRegistrationExpirationValue_Type(Unsigned32):
    """Custom type defaultRegistrationExpirationValue based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_DefaultRegistrationExpirationValue_Type.__name__ = "Unsigned32"
_DefaultRegistrationExpirationValue_Object = MibScalar
defaultRegistrationExpirationValue = _DefaultRegistrationExpirationValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 250),
    _DefaultRegistrationExpirationValue_Type()
)
defaultRegistrationExpirationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRegistrationExpirationValue.setStatus("current")


class _DefaultRegistrationProposedExpirationValue_Type(Unsigned32):
    """Custom type defaultRegistrationProposedExpirationValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DefaultRegistrationProposedExpirationValue_Type.__name__ = "Unsigned32"
_DefaultRegistrationProposedExpirationValue_Object = MibScalar
defaultRegistrationProposedExpirationValue = _DefaultRegistrationProposedExpirationValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 300),
    _DefaultRegistrationProposedExpirationValue_Type()
)
defaultRegistrationProposedExpirationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRegistrationProposedExpirationValue.setStatus("current")


class _DefaultRegistrationRetryTime_Type(Unsigned32):
    """Custom type defaultRegistrationRetryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_DefaultRegistrationRetryTime_Type.__name__ = "Unsigned32"
_DefaultRegistrationRetryTime_Object = MibScalar
defaultRegistrationRetryTime = _DefaultRegistrationRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 350),
    _DefaultRegistrationRetryTime_Type()
)
defaultRegistrationRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRegistrationRetryTime.setStatus("current")


class _DefaultRegistrationUnregisteredBehavior_Type(MxEnableState):
    """Custom type defaultRegistrationUnregisteredBehavior based on MxEnableState"""
    defaultValue = 0


_DefaultRegistrationUnregisteredBehavior_Type.__name__ = "MxEnableState"
_DefaultRegistrationUnregisteredBehavior_Object = MibScalar
defaultRegistrationUnregisteredBehavior = _DefaultRegistrationUnregisteredBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 400),
    _DefaultRegistrationUnregisteredBehavior_Type()
)
defaultRegistrationUnregisteredBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRegistrationUnregisteredBehavior.setStatus("current")


class _DefaultUnitRegistrationUnregisteredBehavior_Type(Integer32):
    """Custom type defaultUnitRegistrationUnregisteredBehavior based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("noEffect", 100),
          ("disableGateway", 200))
    )


_DefaultUnitRegistrationUnregisteredBehavior_Type.__name__ = "Integer32"
_DefaultUnitRegistrationUnregisteredBehavior_Object = MibScalar
defaultUnitRegistrationUnregisteredBehavior = _DefaultUnitRegistrationUnregisteredBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 450),
    _DefaultUnitRegistrationUnregisteredBehavior_Type()
)
defaultUnitRegistrationUnregisteredBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultUnitRegistrationUnregisteredBehavior.setStatus("current")


class _DefaultStaticRegistrarServerHost_Type(MxIpHostNamePort):
    """Custom type defaultStaticRegistrarServerHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.10.10:0")


_DefaultStaticRegistrarServerHost_Type.__name__ = "MxIpHostNamePort"
_DefaultStaticRegistrarServerHost_Object = MibScalar
defaultStaticRegistrarServerHost = _DefaultStaticRegistrarServerHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 500),
    _DefaultStaticRegistrarServerHost_Type()
)
defaultStaticRegistrarServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticRegistrarServerHost.setStatus("current")
_GwSpecificRegistrationTable_Object = MibTable
gwSpecificRegistrationTable = _GwSpecificRegistrationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600)
)
if mibBuilder.loadTexts:
    gwSpecificRegistrationTable.setStatus("current")
_GwSpecificRegistrationEntry_Object = MibTableRow
gwSpecificRegistrationEntry = _GwSpecificRegistrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1)
)
gwSpecificRegistrationEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwSpecificRegistrationGatewayName"),
)
if mibBuilder.loadTexts:
    gwSpecificRegistrationEntry.setStatus("current")
_GwSpecificRegistrationGatewayName_Type = OctetString
_GwSpecificRegistrationGatewayName_Object = MibTableColumn
gwSpecificRegistrationGatewayName = _GwSpecificRegistrationGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 100),
    _GwSpecificRegistrationGatewayName_Type()
)
gwSpecificRegistrationGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwSpecificRegistrationGatewayName.setStatus("current")


class _GwSpecificRegistrationEnableConfig_Type(MxEnableState):
    """Custom type gwSpecificRegistrationEnableConfig based on MxEnableState"""
    defaultValue = 0


_GwSpecificRegistrationEnableConfig_Type.__name__ = "MxEnableState"
_GwSpecificRegistrationEnableConfig_Object = MibTableColumn
gwSpecificRegistrationEnableConfig = _GwSpecificRegistrationEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 200),
    _GwSpecificRegistrationEnableConfig_Type()
)
gwSpecificRegistrationEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationEnableConfig.setStatus("current")


class _GwSpecificRegistrationRefreshTime_Type(Unsigned32):
    """Custom type gwSpecificRegistrationRefreshTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_GwSpecificRegistrationRefreshTime_Type.__name__ = "Unsigned32"
_GwSpecificRegistrationRefreshTime_Object = MibTableColumn
gwSpecificRegistrationRefreshTime = _GwSpecificRegistrationRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 300),
    _GwSpecificRegistrationRefreshTime_Type()
)
gwSpecificRegistrationRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationRefreshTime.setStatus("current")


class _GwSpecificRegistrationExpirationValue_Type(Unsigned32):
    """Custom type gwSpecificRegistrationExpirationValue based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_GwSpecificRegistrationExpirationValue_Type.__name__ = "Unsigned32"
_GwSpecificRegistrationExpirationValue_Object = MibTableColumn
gwSpecificRegistrationExpirationValue = _GwSpecificRegistrationExpirationValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 350),
    _GwSpecificRegistrationExpirationValue_Type()
)
gwSpecificRegistrationExpirationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationExpirationValue.setStatus("current")


class _GwSpecificRegistrationProposedExpirationValue_Type(Unsigned32):
    """Custom type gwSpecificRegistrationProposedExpirationValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_GwSpecificRegistrationProposedExpirationValue_Type.__name__ = "Unsigned32"
_GwSpecificRegistrationProposedExpirationValue_Object = MibTableColumn
gwSpecificRegistrationProposedExpirationValue = _GwSpecificRegistrationProposedExpirationValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 400),
    _GwSpecificRegistrationProposedExpirationValue_Type()
)
gwSpecificRegistrationProposedExpirationValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationProposedExpirationValue.setStatus("current")


class _GwSpecificRegistrationRetryTime_Type(Unsigned32):
    """Custom type gwSpecificRegistrationRetryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_GwSpecificRegistrationRetryTime_Type.__name__ = "Unsigned32"
_GwSpecificRegistrationRetryTime_Object = MibTableColumn
gwSpecificRegistrationRetryTime = _GwSpecificRegistrationRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 450),
    _GwSpecificRegistrationRetryTime_Type()
)
gwSpecificRegistrationRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationRetryTime.setStatus("current")


class _GwSpecificRegistrationUnregisteredBehavior_Type(MxEnableState):
    """Custom type gwSpecificRegistrationUnregisteredBehavior based on MxEnableState"""
    defaultValue = 0


_GwSpecificRegistrationUnregisteredBehavior_Type.__name__ = "MxEnableState"
_GwSpecificRegistrationUnregisteredBehavior_Object = MibTableColumn
gwSpecificRegistrationUnregisteredBehavior = _GwSpecificRegistrationUnregisteredBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 500),
    _GwSpecificRegistrationUnregisteredBehavior_Type()
)
gwSpecificRegistrationUnregisteredBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationUnregisteredBehavior.setStatus("current")


class _GwSpecificRegistrationServerHost_Type(MxIpHostNamePort):
    """Custom type gwSpecificRegistrationServerHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.0.10:0")


_GwSpecificRegistrationServerHost_Type.__name__ = "MxIpHostNamePort"
_GwSpecificRegistrationServerHost_Object = MibTableColumn
gwSpecificRegistrationServerHost = _GwSpecificRegistrationServerHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 600, 1, 600),
    _GwSpecificRegistrationServerHost_Type()
)
gwSpecificRegistrationServerHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRegistrationServerHost.setStatus("current")
_UnitRegistrationsTable_Object = MibTable
unitRegistrationsTable = _UnitRegistrationsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 700)
)
if mibBuilder.loadTexts:
    unitRegistrationsTable.setStatus("current")
_UnitRegistrationsEntry_Object = MibTableRow
unitRegistrationsEntry = _UnitRegistrationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 700, 1)
)
unitRegistrationsEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "unitRegistrationsIndex"),
)
if mibBuilder.loadTexts:
    unitRegistrationsEntry.setStatus("current")
_UnitRegistrationsIndex_Type = Unsigned32
_UnitRegistrationsIndex_Object = MibTableColumn
unitRegistrationsIndex = _UnitRegistrationsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 700, 1, 100),
    _UnitRegistrationsIndex_Type()
)
unitRegistrationsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitRegistrationsIndex.setStatus("current")


class _UnitRegistrationsUsername_Type(OctetString):
    """Custom type unitRegistrationsUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UnitRegistrationsUsername_Type.__name__ = "OctetString"
_UnitRegistrationsUsername_Object = MibTableColumn
unitRegistrationsUsername = _UnitRegistrationsUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 700, 1, 200),
    _UnitRegistrationsUsername_Type()
)
unitRegistrationsUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRegistrationsUsername.setStatus("current")


class _UnitRegistrationsGatewayName_Type(OctetString):
    """Custom type unitRegistrationsGatewayName based on OctetString"""
    defaultValue = OctetString("all")


_UnitRegistrationsGatewayName_Type.__name__ = "OctetString"
_UnitRegistrationsGatewayName_Object = MibTableColumn
unitRegistrationsGatewayName = _UnitRegistrationsGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 700, 1, 250),
    _UnitRegistrationsGatewayName_Type()
)
unitRegistrationsGatewayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRegistrationsGatewayName.setStatus("current")


class _UnitRegistrationsDelete_Type(Integer32):
    """Custom type unitRegistrationsDelete based on Integer32"""
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


_UnitRegistrationsDelete_Type.__name__ = "Integer32"
_UnitRegistrationsDelete_Object = MibTableColumn
unitRegistrationsDelete = _UnitRegistrationsDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 700, 1, 300),
    _UnitRegistrationsDelete_Type()
)
unitRegistrationsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitRegistrationsDelete.setStatus("current")


class _BehaviorOnInitialRegistrationReception_Type(Integer32):
    """Custom type behaviorOnInitialRegistrationReception based on Integer32"""
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
        *(("noRegistration", 100),
          ("endpointRegistration", 200),
          ("unitRegistration", 300),
          ("unitAndEndpointRegistration", 400))
    )


_BehaviorOnInitialRegistrationReception_Type.__name__ = "Integer32"
_BehaviorOnInitialRegistrationReception_Object = MibScalar
behaviorOnInitialRegistrationReception = _BehaviorOnInitialRegistrationReception_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 900),
    _BehaviorOnInitialRegistrationReception_Type()
)
behaviorOnInitialRegistrationReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    behaviorOnInitialRegistrationReception.setStatus("current")


class _RegistrationDelayOnInitialRegistrationReception_Type(Unsigned32):
    """Custom type registrationDelayOnInitialRegistrationReception based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_RegistrationDelayOnInitialRegistrationReception_Type.__name__ = "Unsigned32"
_RegistrationDelayOnInitialRegistrationReception_Object = MibScalar
registrationDelayOnInitialRegistrationReception = _RegistrationDelayOnInitialRegistrationReception_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 1000),
    _RegistrationDelayOnInitialRegistrationReception_Type()
)
registrationDelayOnInitialRegistrationReception.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    registrationDelayOnInitialRegistrationReception.setStatus("current")
_RegistrationStatusTable_Object = MibTable
registrationStatusTable = _RegistrationStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000)
)
if mibBuilder.loadTexts:
    registrationStatusTable.setStatus("current")
_RegistrationStatusEntry_Object = MibTableRow
registrationStatusEntry = _RegistrationStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1)
)
registrationStatusEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "registrationStatusIndex"),
)
if mibBuilder.loadTexts:
    registrationStatusEntry.setStatus("current")
_RegistrationStatusIndex_Type = Unsigned32
_RegistrationStatusIndex_Object = MibTableColumn
registrationStatusIndex = _RegistrationStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1, 100),
    _RegistrationStatusIndex_Type()
)
registrationStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationStatusIndex.setStatus("current")
_RegistrationStatusGateway_Type = OctetString
_RegistrationStatusGateway_Object = MibTableColumn
registrationStatusGateway = _RegistrationStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1, 200),
    _RegistrationStatusGateway_Type()
)
registrationStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationStatusGateway.setStatus("current")
_RegistrationStatusEndpoint_Type = OctetString
_RegistrationStatusEndpoint_Object = MibTableColumn
registrationStatusEndpoint = _RegistrationStatusEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1, 300),
    _RegistrationStatusEndpoint_Type()
)
registrationStatusEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationStatusEndpoint.setStatus("current")


class _RegistrationStatusState_Type(Integer32):
    """Custom type registrationStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("unregistered", 100),
          ("registering", 200),
          ("registered", 300),
          ("refreshing", 400),
          ("unregistering", 500),
          ("unreachable", 600),
          ("authFailed", 700),
          ("rejected", 800),
          ("configError", 900),
          ("invalidResponse", 1000))
    )


_RegistrationStatusState_Type.__name__ = "Integer32"
_RegistrationStatusState_Object = MibTableColumn
registrationStatusState = _RegistrationStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1, 400),
    _RegistrationStatusState_Type()
)
registrationStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationStatusState.setStatus("current")
_RegistrationStatusRegistrar_Type = OctetString
_RegistrationStatusRegistrar_Object = MibTableColumn
registrationStatusRegistrar = _RegistrationStatusRegistrar_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1, 500),
    _RegistrationStatusRegistrar_Type()
)
registrationStatusRegistrar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationStatusRegistrar.setStatus("current")
_RegistrationStatusUsername_Type = OctetString
_RegistrationStatusUsername_Object = MibTableColumn
registrationStatusUsername = _RegistrationStatusUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 800, 10000, 1, 600),
    _RegistrationStatusUsername_Type()
)
registrationStatusUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    registrationStatusUsername.setStatus("current")
_TransportGroup_ObjectIdentity = ObjectIdentity
transportGroup = _TransportGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900)
)


class _TransportPersistentBasePort_Type(Unsigned32):
    """Custom type transportPersistentBasePort based on Unsigned32"""
    defaultValue = 16000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 64535),
    )


_TransportPersistentBasePort_Type.__name__ = "Unsigned32"
_TransportPersistentBasePort_Object = MibScalar
transportPersistentBasePort = _TransportPersistentBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 50),
    _TransportPersistentBasePort_Type()
)
transportPersistentBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportPersistentBasePort.setStatus("current")


class _TransportPersistentPortInterval_Type(Unsigned32):
    """Custom type transportPersistentPortInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 1000),
    )


_TransportPersistentPortInterval_Type.__name__ = "Unsigned32"
_TransportPersistentPortInterval_Object = MibScalar
transportPersistentPortInterval = _TransportPersistentPortInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 55),
    _TransportPersistentPortInterval_Type()
)
transportPersistentPortInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportPersistentPortInterval.setStatus("current")


class _TransportFailbackInterval_Type(Unsigned32):
    """Custom type transportFailbackInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_TransportFailbackInterval_Type.__name__ = "Unsigned32"
_TransportFailbackInterval_Object = MibScalar
transportFailbackInterval = _TransportFailbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 75),
    _TransportFailbackInterval_Type()
)
transportFailbackInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportFailbackInterval.setStatus("current")


class _TransportTlsCertificateTrustLevel_Type(Integer32):
    """Custom type transportTlsCertificateTrustLevel based on Integer32"""
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
        *(("locallyTrusted", 100),
          ("ocspOptional", 200),
          ("ocspMandatory", 300))
    )


_TransportTlsCertificateTrustLevel_Type.__name__ = "Integer32"
_TransportTlsCertificateTrustLevel_Object = MibScalar
transportTlsCertificateTrustLevel = _TransportTlsCertificateTrustLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 85),
    _TransportTlsCertificateTrustLevel_Type()
)
transportTlsCertificateTrustLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportTlsCertificateTrustLevel.setStatus("current")


class _TransportTlsCipherSuite_Type(Integer32):
    """Custom type transportTlsCipherSuite based on Integer32"""
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
        *(("cS1", 100),
          ("cS2", 200),
          ("cS3", 300))
    )


_TransportTlsCipherSuite_Type.__name__ = "Integer32"
_TransportTlsCipherSuite_Object = MibScalar
transportTlsCipherSuite = _TransportTlsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 90),
    _TransportTlsCipherSuite_Type()
)
transportTlsCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportTlsCipherSuite.setStatus("current")


class _TransportTlsVersion_Type(Integer32):
    """Custom type transportTlsVersion based on Integer32"""
    defaultValue = 200

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
        *(("sSLv3", 100),
          ("tLSv1", 200),
          ("tLSv1-1", 300),
          ("tLSv1-2", 400))
    )


_TransportTlsVersion_Type.__name__ = "Integer32"
_TransportTlsVersion_Object = MibScalar
transportTlsVersion = _TransportTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 95),
    _TransportTlsVersion_Type()
)
transportTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportTlsVersion.setStatus("current")
_TransportConfigTable_Object = MibTable
transportConfigTable = _TransportConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100)
)
if mibBuilder.loadTexts:
    transportConfigTable.setStatus("current")
_TransportConfigEntry_Object = MibTableRow
transportConfigEntry = _TransportConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1)
)
transportConfigEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "transportConfigGatewayName"),
)
if mibBuilder.loadTexts:
    transportConfigEntry.setStatus("current")
_TransportConfigGatewayName_Type = OctetString
_TransportConfigGatewayName_Object = MibTableColumn
transportConfigGatewayName = _TransportConfigGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 100),
    _TransportConfigGatewayName_Type()
)
transportConfigGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transportConfigGatewayName.setStatus("current")


class _TransportConfigRegistrationEnable_Type(MxEnableState):
    """Custom type transportConfigRegistrationEnable based on MxEnableState"""
    defaultValue = 0


_TransportConfigRegistrationEnable_Type.__name__ = "MxEnableState"
_TransportConfigRegistrationEnable_Object = MibTableColumn
transportConfigRegistrationEnable = _TransportConfigRegistrationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 200),
    _TransportConfigRegistrationEnable_Type()
)
transportConfigRegistrationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigRegistrationEnable.setStatus("current")


class _TransportConfigContactEnable_Type(MxEnableState):
    """Custom type transportConfigContactEnable based on MxEnableState"""
    defaultValue = 0


_TransportConfigContactEnable_Type.__name__ = "MxEnableState"
_TransportConfigContactEnable_Object = MibTableColumn
transportConfigContactEnable = _TransportConfigContactEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 300),
    _TransportConfigContactEnable_Type()
)
transportConfigContactEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigContactEnable.setStatus("current")


class _TransportConfigUdpEnable_Type(MxEnableState):
    """Custom type transportConfigUdpEnable based on MxEnableState"""
    defaultValue = 1


_TransportConfigUdpEnable_Type.__name__ = "MxEnableState"
_TransportConfigUdpEnable_Object = MibTableColumn
transportConfigUdpEnable = _TransportConfigUdpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 400),
    _TransportConfigUdpEnable_Type()
)
transportConfigUdpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigUdpEnable.setStatus("current")


class _TransportConfigUdpQValue_Type(OctetString):
    """Custom type transportConfigUdpQValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_TransportConfigUdpQValue_Type.__name__ = "OctetString"
_TransportConfigUdpQValue_Object = MibTableColumn
transportConfigUdpQValue = _TransportConfigUdpQValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 500),
    _TransportConfigUdpQValue_Type()
)
transportConfigUdpQValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigUdpQValue.setStatus("current")


class _TransportConfigTcpEnable_Type(MxEnableState):
    """Custom type transportConfigTcpEnable based on MxEnableState"""
    defaultValue = 0


_TransportConfigTcpEnable_Type.__name__ = "MxEnableState"
_TransportConfigTcpEnable_Object = MibTableColumn
transportConfigTcpEnable = _TransportConfigTcpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 600),
    _TransportConfigTcpEnable_Type()
)
transportConfigTcpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigTcpEnable.setStatus("current")


class _TransportConfigTcpQValue_Type(OctetString):
    """Custom type transportConfigTcpQValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_TransportConfigTcpQValue_Type.__name__ = "OctetString"
_TransportConfigTcpQValue_Object = MibTableColumn
transportConfigTcpQValue = _TransportConfigTcpQValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 700),
    _TransportConfigTcpQValue_Type()
)
transportConfigTcpQValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigTcpQValue.setStatus("current")


class _TransportConfigTlsEnable_Type(MxEnableState):
    """Custom type transportConfigTlsEnable based on MxEnableState"""
    defaultValue = 0


_TransportConfigTlsEnable_Type.__name__ = "MxEnableState"
_TransportConfigTlsEnable_Object = MibTableColumn
transportConfigTlsEnable = _TransportConfigTlsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 800),
    _TransportConfigTlsEnable_Type()
)
transportConfigTlsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigTlsEnable.setStatus("current")


class _TransportConfigTlsQValue_Type(OctetString):
    """Custom type transportConfigTlsQValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_TransportConfigTlsQValue_Type.__name__ = "OctetString"
_TransportConfigTlsQValue_Object = MibTableColumn
transportConfigTlsQValue = _TransportConfigTlsQValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 100, 1, 900),
    _TransportConfigTlsQValue_Type()
)
transportConfigTlsQValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportConfigTlsQValue.setStatus("current")
_TlsPersistentConnectionStatusTable_Object = MibTable
tlsPersistentConnectionStatusTable = _TlsPersistentConnectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000)
)
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusTable.setStatus("current")
_TlsPersistentConnectionStatusEntry_Object = MibTableRow
tlsPersistentConnectionStatusEntry = _TlsPersistentConnectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1)
)
tlsPersistentConnectionStatusEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "tlsPersistentConnectionStatusIndex"),
)
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusEntry.setStatus("current")
_TlsPersistentConnectionStatusIndex_Type = Unsigned32
_TlsPersistentConnectionStatusIndex_Object = MibTableColumn
tlsPersistentConnectionStatusIndex = _TlsPersistentConnectionStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1, 100),
    _TlsPersistentConnectionStatusIndex_Type()
)
tlsPersistentConnectionStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusIndex.setStatus("current")
_TlsPersistentConnectionStatusGateway_Type = OctetString
_TlsPersistentConnectionStatusGateway_Object = MibTableColumn
tlsPersistentConnectionStatusGateway = _TlsPersistentConnectionStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1, 200),
    _TlsPersistentConnectionStatusGateway_Type()
)
tlsPersistentConnectionStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusGateway.setStatus("current")
_TlsPersistentConnectionStatusLocalPort_Type = MxAdvancedIpPort
_TlsPersistentConnectionStatusLocalPort_Object = MibTableColumn
tlsPersistentConnectionStatusLocalPort = _TlsPersistentConnectionStatusLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1, 300),
    _TlsPersistentConnectionStatusLocalPort_Type()
)
tlsPersistentConnectionStatusLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusLocalPort.setStatus("current")
_TlsPersistentConnectionStatusRemoteHost_Type = OctetString
_TlsPersistentConnectionStatusRemoteHost_Object = MibTableColumn
tlsPersistentConnectionStatusRemoteHost = _TlsPersistentConnectionStatusRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1, 400),
    _TlsPersistentConnectionStatusRemoteHost_Type()
)
tlsPersistentConnectionStatusRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusRemoteHost.setStatus("current")
_TlsPersistentConnectionStatusRemoteHostIpAddr_Type = OctetString
_TlsPersistentConnectionStatusRemoteHostIpAddr_Object = MibTableColumn
tlsPersistentConnectionStatusRemoteHostIpAddr = _TlsPersistentConnectionStatusRemoteHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1, 450),
    _TlsPersistentConnectionStatusRemoteHostIpAddr_Type()
)
tlsPersistentConnectionStatusRemoteHostIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusRemoteHostIpAddr.setStatus("current")


class _TlsPersistentConnectionStatusState_Type(Integer32):
    """Custom type tlsPersistentConnectionStatusState based on Integer32"""
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
        *(("up", 100),
          ("down", 200),
          ("waitingShutdown", 300),
          ("waitingUp", 400))
    )


_TlsPersistentConnectionStatusState_Type.__name__ = "Integer32"
_TlsPersistentConnectionStatusState_Object = MibTableColumn
tlsPersistentConnectionStatusState = _TlsPersistentConnectionStatusState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 900, 10000, 1, 500),
    _TlsPersistentConnectionStatusState_Type()
)
tlsPersistentConnectionStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tlsPersistentConnectionStatusState.setStatus("current")
_FailoverGroup_ObjectIdentity = ObjectIdentity
failoverGroup = _FailoverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930)
)


class _DefaultSipFailoverConditions_Type(OctetString):
    """Custom type defaultSipFailoverConditions based on OctetString"""
    defaultValue = OctetString("5xxOnRegistration")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DefaultSipFailoverConditions_Type.__name__ = "OctetString"
_DefaultSipFailoverConditions_Object = MibScalar
defaultSipFailoverConditions = _DefaultSipFailoverConditions_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930, 100),
    _DefaultSipFailoverConditions_Type()
)
defaultSipFailoverConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultSipFailoverConditions.setStatus("current")
_GwSpecificFailoverTable_Object = MibTable
gwSpecificFailoverTable = _GwSpecificFailoverTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930, 500)
)
if mibBuilder.loadTexts:
    gwSpecificFailoverTable.setStatus("current")
_GwSpecificFailoverEntry_Object = MibTableRow
gwSpecificFailoverEntry = _GwSpecificFailoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930, 500, 1)
)
gwSpecificFailoverEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwSpecificFailoverGatewayName"),
)
if mibBuilder.loadTexts:
    gwSpecificFailoverEntry.setStatus("current")
_GwSpecificFailoverGatewayName_Type = OctetString
_GwSpecificFailoverGatewayName_Object = MibTableColumn
gwSpecificFailoverGatewayName = _GwSpecificFailoverGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930, 500, 1, 100),
    _GwSpecificFailoverGatewayName_Type()
)
gwSpecificFailoverGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwSpecificFailoverGatewayName.setStatus("current")


class _GwSpecificFailoverEnableConfig_Type(MxEnableState):
    """Custom type gwSpecificFailoverEnableConfig based on MxEnableState"""
    defaultValue = 0


_GwSpecificFailoverEnableConfig_Type.__name__ = "MxEnableState"
_GwSpecificFailoverEnableConfig_Object = MibTableColumn
gwSpecificFailoverEnableConfig = _GwSpecificFailoverEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930, 500, 1, 200),
    _GwSpecificFailoverEnableConfig_Type()
)
gwSpecificFailoverEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificFailoverEnableConfig.setStatus("current")


class _GwSpecificFailoverSipFailoverConditions_Type(OctetString):
    """Custom type gwSpecificFailoverSipFailoverConditions based on OctetString"""
    defaultValue = OctetString("5xxOnRegistration")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_GwSpecificFailoverSipFailoverConditions_Type.__name__ = "OctetString"
_GwSpecificFailoverSipFailoverConditions_Object = MibTableColumn
gwSpecificFailoverSipFailoverConditions = _GwSpecificFailoverSipFailoverConditions_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 930, 500, 1, 300),
    _GwSpecificFailoverSipFailoverConditions_Type()
)
gwSpecificFailoverSipFailoverConditions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificFailoverSipFailoverConditions.setStatus("current")
_PenaltyBoxGroup_ObjectIdentity = ObjectIdentity
penaltyBoxGroup = _PenaltyBoxGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1000)
)


class _PenaltyBoxEnable_Type(MxEnableState):
    """Custom type penaltyBoxEnable based on MxEnableState"""
    defaultValue = 0


_PenaltyBoxEnable_Type.__name__ = "MxEnableState"
_PenaltyBoxEnable_Object = MibScalar
penaltyBoxEnable = _PenaltyBoxEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1000, 100),
    _PenaltyBoxEnable_Type()
)
penaltyBoxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    penaltyBoxEnable.setStatus("current")


class _PenaltyBoxTime_Type(Unsigned32):
    """Custom type penaltyBoxTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 7200),
    )


_PenaltyBoxTime_Type.__name__ = "Unsigned32"
_PenaltyBoxTime_Object = MibScalar
penaltyBoxTime = _PenaltyBoxTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1000, 200),
    _PenaltyBoxTime_Type()
)
penaltyBoxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    penaltyBoxTime.setStatus("current")
_ErrorMappingGroup_ObjectIdentity = ObjectIdentity
errorMappingGroup = _ErrorMappingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100)
)
_ErrorMappingSipToCauseTable_Object = MibTable
errorMappingSipToCauseTable = _ErrorMappingSipToCauseTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 100)
)
if mibBuilder.loadTexts:
    errorMappingSipToCauseTable.setStatus("current")
_ErrorMappingSipToCauseEntry_Object = MibTableRow
errorMappingSipToCauseEntry = _ErrorMappingSipToCauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 100, 1)
)
errorMappingSipToCauseEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "errorMappingSipToCauseSipCode"),
)
if mibBuilder.loadTexts:
    errorMappingSipToCauseEntry.setStatus("current")


class _ErrorMappingSipToCauseSipCode_Type(Unsigned32):
    """Custom type errorMappingSipToCauseSipCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 699),
    )


_ErrorMappingSipToCauseSipCode_Type.__name__ = "Unsigned32"
_ErrorMappingSipToCauseSipCode_Object = MibTableColumn
errorMappingSipToCauseSipCode = _ErrorMappingSipToCauseSipCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 100, 1, 100),
    _ErrorMappingSipToCauseSipCode_Type()
)
errorMappingSipToCauseSipCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMappingSipToCauseSipCode.setStatus("current")


class _ErrorMappingSipToCauseCause_Type(Unsigned32):
    """Custom type errorMappingSipToCauseCause based on Unsigned32"""
    defaultValue = 127

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ErrorMappingSipToCauseCause_Type.__name__ = "Unsigned32"
_ErrorMappingSipToCauseCause_Object = MibTableColumn
errorMappingSipToCauseCause = _ErrorMappingSipToCauseCause_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 100, 1, 200),
    _ErrorMappingSipToCauseCause_Type()
)
errorMappingSipToCauseCause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorMappingSipToCauseCause.setStatus("current")


class _ErrorMappingSipToCauseDelete_Type(Integer32):
    """Custom type errorMappingSipToCauseDelete based on Integer32"""
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


_ErrorMappingSipToCauseDelete_Type.__name__ = "Integer32"
_ErrorMappingSipToCauseDelete_Object = MibTableColumn
errorMappingSipToCauseDelete = _ErrorMappingSipToCauseDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 100, 1, 300),
    _ErrorMappingSipToCauseDelete_Type()
)
errorMappingSipToCauseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorMappingSipToCauseDelete.setStatus("current")
_ErrorMappingCauseToSipTable_Object = MibTable
errorMappingCauseToSipTable = _ErrorMappingCauseToSipTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 300)
)
if mibBuilder.loadTexts:
    errorMappingCauseToSipTable.setStatus("current")
_ErrorMappingCauseToSipEntry_Object = MibTableRow
errorMappingCauseToSipEntry = _ErrorMappingCauseToSipEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 300, 1)
)
errorMappingCauseToSipEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "errorMappingCauseToSipCause"),
)
if mibBuilder.loadTexts:
    errorMappingCauseToSipEntry.setStatus("current")


class _ErrorMappingCauseToSipCause_Type(Unsigned32):
    """Custom type errorMappingCauseToSipCause based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ErrorMappingCauseToSipCause_Type.__name__ = "Unsigned32"
_ErrorMappingCauseToSipCause_Object = MibTableColumn
errorMappingCauseToSipCause = _ErrorMappingCauseToSipCause_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 300, 1, 100),
    _ErrorMappingCauseToSipCause_Type()
)
errorMappingCauseToSipCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMappingCauseToSipCause.setStatus("current")


class _ErrorMappingCauseToSipSipCode_Type(Unsigned32):
    """Custom type errorMappingCauseToSipSipCode based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 699),
    )


_ErrorMappingCauseToSipSipCode_Type.__name__ = "Unsigned32"
_ErrorMappingCauseToSipSipCode_Object = MibTableColumn
errorMappingCauseToSipSipCode = _ErrorMappingCauseToSipSipCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 300, 1, 200),
    _ErrorMappingCauseToSipSipCode_Type()
)
errorMappingCauseToSipSipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorMappingCauseToSipSipCode.setStatus("current")


class _ErrorMappingCauseToSipDelete_Type(Integer32):
    """Custom type errorMappingCauseToSipDelete based on Integer32"""
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


_ErrorMappingCauseToSipDelete_Type.__name__ = "Integer32"
_ErrorMappingCauseToSipDelete_Object = MibTableColumn
errorMappingCauseToSipDelete = _ErrorMappingCauseToSipDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 300, 1, 300),
    _ErrorMappingCauseToSipDelete_Type()
)
errorMappingCauseToSipDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorMappingCauseToSipDelete.setStatus("current")


class _ReasonHeaderSupport_Type(Integer32):
    """Custom type reasonHeaderSupport based on Integer32"""
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
          ("sendQ850", 200),
          ("receiveQ850", 300),
          ("sendReceiveQ850", 400))
    )


_ReasonHeaderSupport_Type.__name__ = "Integer32"
_ReasonHeaderSupport_Object = MibScalar
reasonHeaderSupport = _ReasonHeaderSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1100, 500),
    _ReasonHeaderSupport_Type()
)
reasonHeaderSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reasonHeaderSupport.setStatus("current")
_SipKeepAliveGroup_ObjectIdentity = ObjectIdentity
sipKeepAliveGroup = _SipKeepAliveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300)
)


class _SipKeepAliveMethod_Type(Integer32):
    """Custom type sipKeepAliveMethod based on Integer32"""
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
          ("sipOptions", 200),
          ("ping", 300),
          ("tcpKeepAlive", 400))
    )


_SipKeepAliveMethod_Type.__name__ = "Integer32"
_SipKeepAliveMethod_Object = MibScalar
sipKeepAliveMethod = _SipKeepAliveMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 100),
    _SipKeepAliveMethod_Type()
)
sipKeepAliveMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipKeepAliveMethod.setStatus("current")


class _SipKeepAliveInterval_Type(Unsigned32):
    """Custom type sipKeepAliveInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SipKeepAliveInterval_Type.__name__ = "Unsigned32"
_SipKeepAliveInterval_Object = MibScalar
sipKeepAliveInterval = _SipKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 200),
    _SipKeepAliveInterval_Type()
)
sipKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipKeepAliveInterval.setStatus("current")


class _SipKeepAliveRetry_Type(Unsigned32):
    """Custom type sipKeepAliveRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SipKeepAliveRetry_Type.__name__ = "Unsigned32"
_SipKeepAliveRetry_Object = MibScalar
sipKeepAliveRetry = _SipKeepAliveRetry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 210),
    _SipKeepAliveRetry_Type()
)
sipKeepAliveRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipKeepAliveRetry.setStatus("current")


class _SipKeepAliveDestination_Type(Integer32):
    """Custom type sipKeepAliveDestination based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("firstSipDestination", 100),
          ("alternateDestination", 200))
    )


_SipKeepAliveDestination_Type.__name__ = "Integer32"
_SipKeepAliveDestination_Object = MibScalar
sipKeepAliveDestination = _SipKeepAliveDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 300),
    _SipKeepAliveDestination_Type()
)
sipKeepAliveDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipKeepAliveDestination.setStatus("current")
_GwKeepAliveAlternateDestinationTable_Object = MibTable
gwKeepAliveAlternateDestinationTable = _GwKeepAliveAlternateDestinationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 400)
)
if mibBuilder.loadTexts:
    gwKeepAliveAlternateDestinationTable.setStatus("current")
_GwKeepAliveAlternateDestinationEntry_Object = MibTableRow
gwKeepAliveAlternateDestinationEntry = _GwKeepAliveAlternateDestinationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 400, 1)
)
gwKeepAliveAlternateDestinationEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwKeepAliveAlternateDestinationGatewayName"),
)
if mibBuilder.loadTexts:
    gwKeepAliveAlternateDestinationEntry.setStatus("current")
_GwKeepAliveAlternateDestinationGatewayName_Type = OctetString
_GwKeepAliveAlternateDestinationGatewayName_Object = MibTableColumn
gwKeepAliveAlternateDestinationGatewayName = _GwKeepAliveAlternateDestinationGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 400, 1, 100),
    _GwKeepAliveAlternateDestinationGatewayName_Type()
)
gwKeepAliveAlternateDestinationGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwKeepAliveAlternateDestinationGatewayName.setStatus("current")


class _GwKeepAliveAlternateDestinationAlternateDestination_Type(MxIpHostNamePort):
    """Custom type gwKeepAliveAlternateDestinationAlternateDestination based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.0.10:0")


_GwKeepAliveAlternateDestinationAlternateDestination_Type.__name__ = "MxIpHostNamePort"
_GwKeepAliveAlternateDestinationAlternateDestination_Object = MibTableColumn
gwKeepAliveAlternateDestinationAlternateDestination = _GwKeepAliveAlternateDestinationAlternateDestination_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1300, 400, 1, 200),
    _GwKeepAliveAlternateDestinationAlternateDestination_Type()
)
gwKeepAliveAlternateDestinationAlternateDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwKeepAliveAlternateDestinationAlternateDestination.setStatus("current")
_PrackGroup_ObjectIdentity = ObjectIdentity
prackGroup = _PrackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1400)
)


class _UasPrackSupport_Type(Integer32):
    """Custom type uasPrackSupport based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 200),
          ("supported", 300))
    )


_UasPrackSupport_Type.__name__ = "Integer32"
_UasPrackSupport_Object = MibScalar
uasPrackSupport = _UasPrackSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1400, 100),
    _UasPrackSupport_Type()
)
uasPrackSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uasPrackSupport.setStatus("current")


class _UacPrackSupport_Type(Integer32):
    """Custom type uacPrackSupport based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 200),
          ("supported", 300),
          ("required", 400))
    )


_UacPrackSupport_Type.__name__ = "Integer32"
_UacPrackSupport_Object = MibScalar
uacPrackSupport = _UacPrackSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1400, 200),
    _UacPrackSupport_Type()
)
uacPrackSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uacPrackSupport.setStatus("current")
_OfferAnswerGroup_ObjectIdentity = ObjectIdentity
offerAnswerGroup = _OfferAnswerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1500)
)


class _AnswerCodecNegotiation_Type(Integer32):
    """Custom type answerCodecNegotiation based on Integer32"""
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
        *(("allCommonLocalPriority", 100),
          ("firstCommonLocalPriority", 200),
          ("allCommonPeerPriority", 300),
          ("firstCommonPeerPriority", 400))
    )


_AnswerCodecNegotiation_Type.__name__ = "Integer32"
_AnswerCodecNegotiation_Object = MibScalar
answerCodecNegotiation = _AnswerCodecNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1500, 100),
    _AnswerCodecNegotiation_Type()
)
answerCodecNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    answerCodecNegotiation.setStatus("current")
_DiversionGroup_ObjectIdentity = ObjectIdentity
diversionGroup = _DiversionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1600)
)
_DiversionConfigTable_Object = MibTable
diversionConfigTable = _DiversionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1600, 100)
)
if mibBuilder.loadTexts:
    diversionConfigTable.setStatus("current")
_DiversionConfigEntry_Object = MibTableRow
diversionConfigEntry = _DiversionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1600, 100, 1)
)
diversionConfigEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "diversionConfigGatewayName"),
)
if mibBuilder.loadTexts:
    diversionConfigEntry.setStatus("current")
_DiversionConfigGatewayName_Type = OctetString
_DiversionConfigGatewayName_Object = MibTableColumn
diversionConfigGatewayName = _DiversionConfigGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1600, 100, 1, 100),
    _DiversionConfigGatewayName_Type()
)
diversionConfigGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diversionConfigGatewayName.setStatus("current")


class _DiversionConfigMethod_Type(Integer32):
    """Custom type diversionConfigMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("diversionHeader", 200))
    )


_DiversionConfigMethod_Type.__name__ = "Integer32"
_DiversionConfigMethod_Object = MibTableColumn
diversionConfigMethod = _DiversionConfigMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1600, 100, 1, 200),
    _DiversionConfigMethod_Type()
)
diversionConfigMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diversionConfigMethod.setStatus("current")
_DnsGroup_ObjectIdentity = ObjectIdentity
dnsGroup = _DnsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1700)
)


class _SupportedDnsQueries_Type(Integer32):
    """Custom type supportedDnsQueries based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("address", 100),
          ("srv", 200),
          ("naptr", 300))
    )


_SupportedDnsQueries_Type.__name__ = "Integer32"
_SupportedDnsQueries_Object = MibScalar
supportedDnsQueries = _SupportedDnsQueries_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1700, 100),
    _SupportedDnsQueries_Type()
)
supportedDnsQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    supportedDnsQueries.setStatus("current")


class _DnsFailureConcealment_Type(Integer32):
    """Custom type dnsFailureConcealment based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              300)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("onNoResolution", 300))
    )


_DnsFailureConcealment_Type.__name__ = "Integer32"
_DnsFailureConcealment_Object = MibScalar
dnsFailureConcealment = _DnsFailureConcealment_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1700, 200),
    _DnsFailureConcealment_Type()
)
dnsFailureConcealment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsFailureConcealment.setStatus("current")


class _DnsIpVersion_Type(Integer32):
    """Custom type dnsIpVersion based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("ipV4Only", 100),
          ("ipV4Preferred", 200))
    )


_DnsIpVersion_Type.__name__ = "Integer32"
_DnsIpVersion_Object = MibScalar
dnsIpVersion = _DnsIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1700, 300),
    _DnsIpVersion_Type()
)
dnsIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsIpVersion.setStatus("current")
_MessageWaitingIndication_ObjectIdentity = ObjectIdentity
messageWaitingIndication = _MessageWaitingIndication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800)
)


class _DefaultStaticMessagingHost_Type(MxIpHostNamePort):
    """Custom type defaultStaticMessagingHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.10.10:0")


_DefaultStaticMessagingHost_Type.__name__ = "MxIpHostNamePort"
_DefaultStaticMessagingHost_Object = MibScalar
defaultStaticMessagingHost = _DefaultStaticMessagingHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 100),
    _DefaultStaticMessagingHost_Type()
)
defaultStaticMessagingHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticMessagingHost.setStatus("current")


class _DefaultUsernameInRequestUriEnable_Type(MxEnableState):
    """Custom type defaultUsernameInRequestUriEnable based on MxEnableState"""
    defaultValue = 0


_DefaultUsernameInRequestUriEnable_Type.__name__ = "MxEnableState"
_DefaultUsernameInRequestUriEnable_Object = MibScalar
defaultUsernameInRequestUriEnable = _DefaultUsernameInRequestUriEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 110),
    _DefaultUsernameInRequestUriEnable_Type()
)
defaultUsernameInRequestUriEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultUsernameInRequestUriEnable.setStatus("current")
_GwSpecificMwiTable_Object = MibTable
gwSpecificMwiTable = _GwSpecificMwiTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 200)
)
if mibBuilder.loadTexts:
    gwSpecificMwiTable.setStatus("current")
_GwSpecificMwiEntry_Object = MibTableRow
gwSpecificMwiEntry = _GwSpecificMwiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 200, 1)
)
gwSpecificMwiEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwSpecificMwiGatewayName"),
)
if mibBuilder.loadTexts:
    gwSpecificMwiEntry.setStatus("current")
_GwSpecificMwiGatewayName_Type = OctetString
_GwSpecificMwiGatewayName_Object = MibTableColumn
gwSpecificMwiGatewayName = _GwSpecificMwiGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 200, 1, 100),
    _GwSpecificMwiGatewayName_Type()
)
gwSpecificMwiGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwSpecificMwiGatewayName.setStatus("current")


class _GwSpecificMwiEnableConfig_Type(MxEnableState):
    """Custom type gwSpecificMwiEnableConfig based on MxEnableState"""
    defaultValue = 0


_GwSpecificMwiEnableConfig_Type.__name__ = "MxEnableState"
_GwSpecificMwiEnableConfig_Object = MibTableColumn
gwSpecificMwiEnableConfig = _GwSpecificMwiEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 200, 1, 200),
    _GwSpecificMwiEnableConfig_Type()
)
gwSpecificMwiEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificMwiEnableConfig.setStatus("current")


class _GwSpecificMwiMessagingHost_Type(MxIpHostNamePort):
    """Custom type gwSpecificMwiMessagingHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.10.10:0")


_GwSpecificMwiMessagingHost_Type.__name__ = "MxIpHostNamePort"
_GwSpecificMwiMessagingHost_Object = MibTableColumn
gwSpecificMwiMessagingHost = _GwSpecificMwiMessagingHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 200, 1, 300),
    _GwSpecificMwiMessagingHost_Type()
)
gwSpecificMwiMessagingHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificMwiMessagingHost.setStatus("current")


class _GwSpecificMwiUsernameInRequestUriEnable_Type(MxEnableState):
    """Custom type gwSpecificMwiUsernameInRequestUriEnable based on MxEnableState"""
    defaultValue = 0


_GwSpecificMwiUsernameInRequestUriEnable_Type.__name__ = "MxEnableState"
_GwSpecificMwiUsernameInRequestUriEnable_Object = MibTableColumn
gwSpecificMwiUsernameInRequestUriEnable = _GwSpecificMwiUsernameInRequestUriEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 200, 1, 400),
    _GwSpecificMwiUsernameInRequestUriEnable_Type()
)
gwSpecificMwiUsernameInRequestUriEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificMwiUsernameInRequestUriEnable.setStatus("current")
_MwiStatusTable_Object = MibTable
mwiStatusTable = _MwiStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300)
)
if mibBuilder.loadTexts:
    mwiStatusTable.setStatus("current")
_MwiStatusEntry_Object = MibTableRow
mwiStatusEntry = _MwiStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1)
)
mwiStatusEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "mwiStatusIndex"),
)
if mibBuilder.loadTexts:
    mwiStatusEntry.setStatus("current")
_MwiStatusIndex_Type = Unsigned32
_MwiStatusIndex_Object = MibTableColumn
mwiStatusIndex = _MwiStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1, 100),
    _MwiStatusIndex_Type()
)
mwiStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiStatusIndex.setStatus("current")
_MwiStatusGatewayName_Type = OctetString
_MwiStatusGatewayName_Object = MibTableColumn
mwiStatusGatewayName = _MwiStatusGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1, 200),
    _MwiStatusGatewayName_Type()
)
mwiStatusGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiStatusGatewayName.setStatus("current")


class _MwiStatusSubscriptionState_Type(Integer32):
    """Custom type mwiStatusSubscriptionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600,
              700,
              800,
              900,
              1000,
              1100)
        )
    )
    namedValues = NamedValues(
        *(("unsubscribed", 100),
          ("subscribing", 200),
          ("subscribed", 300),
          ("refreshing", 400),
          ("unsubscribing", 500),
          ("unreachable", 600),
          ("authFailed", 700),
          ("rejected", 800),
          ("configError", 900),
          ("invalidResponse", 1000),
          ("error", 1100))
    )


_MwiStatusSubscriptionState_Type.__name__ = "Integer32"
_MwiStatusSubscriptionState_Object = MibTableColumn
mwiStatusSubscriptionState = _MwiStatusSubscriptionState_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1, 300),
    _MwiStatusSubscriptionState_Type()
)
mwiStatusSubscriptionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiStatusSubscriptionState.setStatus("current")
_MwiStatusEndpoint_Type = OctetString
_MwiStatusEndpoint_Object = MibTableColumn
mwiStatusEndpoint = _MwiStatusEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1, 400),
    _MwiStatusEndpoint_Type()
)
mwiStatusEndpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiStatusEndpoint.setStatus("current")
_MwiStatusMessagingHost_Type = OctetString
_MwiStatusMessagingHost_Object = MibTableColumn
mwiStatusMessagingHost = _MwiStatusMessagingHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1, 500),
    _MwiStatusMessagingHost_Type()
)
mwiStatusMessagingHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiStatusMessagingHost.setStatus("current")
_MwiStatusUsername_Type = OctetString
_MwiStatusUsername_Object = MibTableColumn
mwiStatusUsername = _MwiStatusUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1800, 300, 1, 600),
    _MwiStatusUsername_Type()
)
mwiStatusUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwiStatusUsername.setStatus("current")
_ConferenceGroup_ObjectIdentity = ObjectIdentity
conferenceGroup = _ConferenceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900)
)


class _DefaultStaticConferenceServerUri_Type(OctetString):
    """Custom type defaultStaticConferenceServerUri based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DefaultStaticConferenceServerUri_Type.__name__ = "OctetString"
_DefaultStaticConferenceServerUri_Object = MibScalar
defaultStaticConferenceServerUri = _DefaultStaticConferenceServerUri_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900, 100),
    _DefaultStaticConferenceServerUri_Type()
)
defaultStaticConferenceServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticConferenceServerUri.setStatus("current")
_GwSpecificConferenceTable_Object = MibTable
gwSpecificConferenceTable = _GwSpecificConferenceTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900, 1000)
)
if mibBuilder.loadTexts:
    gwSpecificConferenceTable.setStatus("current")
_GwSpecificConferenceEntry_Object = MibTableRow
gwSpecificConferenceEntry = _GwSpecificConferenceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900, 1000, 1)
)
gwSpecificConferenceEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwSpecificConferenceGatewayName"),
)
if mibBuilder.loadTexts:
    gwSpecificConferenceEntry.setStatus("current")
_GwSpecificConferenceGatewayName_Type = OctetString
_GwSpecificConferenceGatewayName_Object = MibTableColumn
gwSpecificConferenceGatewayName = _GwSpecificConferenceGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900, 1000, 1, 100),
    _GwSpecificConferenceGatewayName_Type()
)
gwSpecificConferenceGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwSpecificConferenceGatewayName.setStatus("current")


class _GwSpecificConferenceEnableConfig_Type(MxEnableState):
    """Custom type gwSpecificConferenceEnableConfig based on MxEnableState"""
    defaultValue = 0


_GwSpecificConferenceEnableConfig_Type.__name__ = "MxEnableState"
_GwSpecificConferenceEnableConfig_Object = MibTableColumn
gwSpecificConferenceEnableConfig = _GwSpecificConferenceEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900, 1000, 1, 200),
    _GwSpecificConferenceEnableConfig_Type()
)
gwSpecificConferenceEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificConferenceEnableConfig.setStatus("current")


class _GwSpecificConferenceServerUri_Type(OctetString):
    """Custom type gwSpecificConferenceServerUri based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwSpecificConferenceServerUri_Type.__name__ = "OctetString"
_GwSpecificConferenceServerUri_Object = MibTableColumn
gwSpecificConferenceServerUri = _GwSpecificConferenceServerUri_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 1900, 1000, 1, 300),
    _GwSpecificConferenceServerUri_Type()
)
gwSpecificConferenceServerUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificConferenceServerUri.setStatus("current")
_PriorityGroup_ObjectIdentity = ObjectIdentity
priorityGroup = _PriorityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2000)
)


class _DefaultOutboundPriorityCallRouting_Type(Integer32):
    """Custom type defaultOutboundPriorityCallRouting based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("normal", 100),
          ("skipOutboundProxy", 200))
    )


_DefaultOutboundPriorityCallRouting_Type.__name__ = "Integer32"
_DefaultOutboundPriorityCallRouting_Object = MibScalar
defaultOutboundPriorityCallRouting = _DefaultOutboundPriorityCallRouting_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2000, 100),
    _DefaultOutboundPriorityCallRouting_Type()
)
defaultOutboundPriorityCallRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultOutboundPriorityCallRouting.setStatus("current")
_EventHandlingGroup_ObjectIdentity = ObjectIdentity
eventHandlingGroup = _EventHandlingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100)
)
_GwEventHandlingTable_Object = MibTable
gwEventHandlingTable = _GwEventHandlingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100, 100)
)
if mibBuilder.loadTexts:
    gwEventHandlingTable.setStatus("current")
_GwEventHandlingEntry_Object = MibTableRow
gwEventHandlingEntry = _GwEventHandlingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100, 100, 1)
)
gwEventHandlingEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwEventHandlingGatewayName"),
)
if mibBuilder.loadTexts:
    gwEventHandlingEntry.setStatus("current")
_GwEventHandlingGatewayName_Type = OctetString
_GwEventHandlingGatewayName_Object = MibTableColumn
gwEventHandlingGatewayName = _GwEventHandlingGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100, 100, 1, 100),
    _GwEventHandlingGatewayName_Type()
)
gwEventHandlingGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwEventHandlingGatewayName.setStatus("current")


class _GwEventHandlingReboot_Type(Integer32):
    """Custom type gwEventHandlingReboot based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("rejected", 100),
          ("restart", 200))
    )


_GwEventHandlingReboot_Type.__name__ = "Integer32"
_GwEventHandlingReboot_Object = MibTableColumn
gwEventHandlingReboot = _GwEventHandlingReboot_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100, 100, 1, 200),
    _GwEventHandlingReboot_Type()
)
gwEventHandlingReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEventHandlingReboot.setStatus("current")


class _GwEventHandlingCheckSync_Type(Integer32):
    """Custom type gwEventHandlingCheckSync based on Integer32"""
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
        *(("rejected", 100),
          ("transferScript", 200),
          ("cwmpInform", 300))
    )


_GwEventHandlingCheckSync_Type.__name__ = "Integer32"
_GwEventHandlingCheckSync_Object = MibTableColumn
gwEventHandlingCheckSync = _GwEventHandlingCheckSync_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100, 100, 1, 300),
    _GwEventHandlingCheckSync_Type()
)
gwEventHandlingCheckSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwEventHandlingCheckSync.setStatus("current")


class _SipMessageSupport_Type(Integer32):
    """Custom type sipMessageSupport based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 100),
          ("acceptPlainText", 200))
    )


_SipMessageSupport_Type.__name__ = "Integer32"
_SipMessageSupport_Object = MibScalar
sipMessageSupport = _SipMessageSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2100, 200),
    _SipMessageSupport_Type()
)
sipMessageSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipMessageSupport.setStatus("current")
_TransferGroup_ObjectIdentity = ObjectIdentity
transferGroup = _TransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2200)
)


class _ReferredByHeader_Type(Integer32):
    """Custom type referredByHeader based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("headerOnly", 200))
    )


_ReferredByHeader_Type.__name__ = "Integer32"
_ReferredByHeader_Object = MibScalar
referredByHeader = _ReferredByHeader_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2200, 100),
    _ReferredByHeader_Type()
)
referredByHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    referredByHeader.setStatus("current")


class _BlindTransferMethod_Type(Integer32):
    """Custom type blindTransferMethod based on Integer32"""
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
        *(("semiAttended", 100),
          ("semiAttendedConfirmed", 200),
          ("semiAttendedCancelled", 300))
    )


_BlindTransferMethod_Type.__name__ = "Integer32"
_BlindTransferMethod_Object = MibScalar
blindTransferMethod = _BlindTransferMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2200, 200),
    _BlindTransferMethod_Type()
)
blindTransferMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blindTransferMethod.setStatus("current")


class _ReferToHeaderUriSource_Type(Integer32):
    """Custom type referToHeaderUriSource based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("aor", 100),
          ("contactUri", 200))
    )


_ReferToHeaderUriSource_Type.__name__ = "Integer32"
_ReferToHeaderUriSource_Object = MibScalar
referToHeaderUriSource = _ReferToHeaderUriSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2200, 300),
    _ReferToHeaderUriSource_Type()
)
referToHeaderUriSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    referToHeaderUriSource.setStatus("current")
_AocGroup_ObjectIdentity = ObjectIdentity
aocGroup = _AocGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2300)
)
_AocConfigTable_Object = MibTable
aocConfigTable = _AocConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2300, 100)
)
if mibBuilder.loadTexts:
    aocConfigTable.setStatus("current")
_AocConfigEntry_Object = MibTableRow
aocConfigEntry = _AocConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2300, 100, 1)
)
aocConfigEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "aocConfigGatewayName"),
)
if mibBuilder.loadTexts:
    aocConfigEntry.setStatus("current")
_AocConfigGatewayName_Type = OctetString
_AocConfigGatewayName_Object = MibTableColumn
aocConfigGatewayName = _AocConfigGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2300, 100, 1, 100),
    _AocConfigGatewayName_Type()
)
aocConfigGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aocConfigGatewayName.setStatus("current")


class _AocConfigAocDSupport_Type(Integer32):
    """Custom type aocConfigAocDSupport based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 100),
          ("transparent", 200))
    )


_AocConfigAocDSupport_Type.__name__ = "Integer32"
_AocConfigAocDSupport_Object = MibTableColumn
aocConfigAocDSupport = _AocConfigAocDSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2300, 100, 1, 200),
    _AocConfigAocDSupport_Type()
)
aocConfigAocDSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aocConfigAocDSupport.setStatus("current")


class _AocConfigAocESupport_Type(Integer32):
    """Custom type aocConfigAocESupport based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 100),
          ("transparent", 200))
    )


_AocConfigAocESupport_Type.__name__ = "Integer32"
_AocConfigAocESupport_Object = MibTableColumn
aocConfigAocESupport = _AocConfigAocESupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2300, 100, 1, 300),
    _AocConfigAocESupport_Type()
)
aocConfigAocESupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aocConfigAocESupport.setStatus("current")
_KpmlGroup_ObjectIdentity = ObjectIdentity
kpmlGroup = _KpmlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2400)
)


class _UasKpmlSupport_Type(Integer32):
    """Custom type uasKpmlSupport based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 100),
          ("supportedInDialog", 200))
    )


_UasKpmlSupport_Type.__name__ = "Integer32"
_UasKpmlSupport_Object = MibScalar
uasKpmlSupport = _UasKpmlSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2400, 100),
    _UasKpmlSupport_Type()
)
uasKpmlSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uasKpmlSupport.setStatus("current")
_SecurityAgreementGroup_ObjectIdentity = ObjectIdentity
securityAgreementGroup = _SecurityAgreementGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2500)
)


class _MediaSecurityAgreementEnable_Type(MxEnableState):
    """Custom type mediaSecurityAgreementEnable based on MxEnableState"""
    defaultValue = 0


_MediaSecurityAgreementEnable_Type.__name__ = "MxEnableState"
_MediaSecurityAgreementEnable_Object = MibScalar
mediaSecurityAgreementEnable = _MediaSecurityAgreementEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2500, 100),
    _MediaSecurityAgreementEnable_Type()
)
mediaSecurityAgreementEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaSecurityAgreementEnable.setStatus("current")
_PrivacyHeadersGroup_ObjectIdentity = ObjectIdentity
privacyHeadersGroup = _PrivacyHeadersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2600)
)


class _PrivacyHeadersInResponse_Type(Integer32):
    """Custom type privacyHeadersInResponse based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 100),
          ("supportedPAssertedIdentity", 200))
    )


_PrivacyHeadersInResponse_Type.__name__ = "Integer32"
_PrivacyHeadersInResponse_Object = MibScalar
privacyHeadersInResponse = _PrivacyHeadersInResponse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2600, 100),
    _PrivacyHeadersInResponse_Type()
)
privacyHeadersInResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privacyHeadersInResponse.setStatus("current")
_RtcpXrGroup_ObjectIdentity = ObjectIdentity
rtcpXrGroup = _RtcpXrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700)
)


class _DefaultStaticRtcpXrCollectorUri_Type(OctetString):
    """Custom type defaultStaticRtcpXrCollectorUri based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DefaultStaticRtcpXrCollectorUri_Type.__name__ = "OctetString"
_DefaultStaticRtcpXrCollectorUri_Object = MibScalar
defaultStaticRtcpXrCollectorUri = _DefaultStaticRtcpXrCollectorUri_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 100),
    _DefaultStaticRtcpXrCollectorUri_Type()
)
defaultStaticRtcpXrCollectorUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticRtcpXrCollectorUri.setStatus("current")


class _DefaultRtcpXrPeriodicReportsInterval_Type(Unsigned32):
    """Custom type defaultRtcpXrPeriodicReportsInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_DefaultRtcpXrPeriodicReportsInterval_Type.__name__ = "Unsigned32"
_DefaultRtcpXrPeriodicReportsInterval_Object = MibScalar
defaultRtcpXrPeriodicReportsInterval = _DefaultRtcpXrPeriodicReportsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 200),
    _DefaultRtcpXrPeriodicReportsInterval_Type()
)
defaultRtcpXrPeriodicReportsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRtcpXrPeriodicReportsInterval.setStatus("current")
_GwSpecificRtcpXrTable_Object = MibTable
gwSpecificRtcpXrTable = _GwSpecificRtcpXrTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 1000)
)
if mibBuilder.loadTexts:
    gwSpecificRtcpXrTable.setStatus("current")
_GwSpecificRtcpXrEntry_Object = MibTableRow
gwSpecificRtcpXrEntry = _GwSpecificRtcpXrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 1000, 1)
)
gwSpecificRtcpXrEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "gwSpecificRtcpXrGatewayName"),
)
if mibBuilder.loadTexts:
    gwSpecificRtcpXrEntry.setStatus("current")
_GwSpecificRtcpXrGatewayName_Type = OctetString
_GwSpecificRtcpXrGatewayName_Object = MibTableColumn
gwSpecificRtcpXrGatewayName = _GwSpecificRtcpXrGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 1000, 1, 100),
    _GwSpecificRtcpXrGatewayName_Type()
)
gwSpecificRtcpXrGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gwSpecificRtcpXrGatewayName.setStatus("current")


class _GwSpecificRtcpXrEnableConfig_Type(MxEnableState):
    """Custom type gwSpecificRtcpXrEnableConfig based on MxEnableState"""
    defaultValue = 0


_GwSpecificRtcpXrEnableConfig_Type.__name__ = "MxEnableState"
_GwSpecificRtcpXrEnableConfig_Object = MibTableColumn
gwSpecificRtcpXrEnableConfig = _GwSpecificRtcpXrEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 1000, 1, 200),
    _GwSpecificRtcpXrEnableConfig_Type()
)
gwSpecificRtcpXrEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRtcpXrEnableConfig.setStatus("current")


class _GwSpecificRtcpXrCollectorUri_Type(OctetString):
    """Custom type gwSpecificRtcpXrCollectorUri based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GwSpecificRtcpXrCollectorUri_Type.__name__ = "OctetString"
_GwSpecificRtcpXrCollectorUri_Object = MibTableColumn
gwSpecificRtcpXrCollectorUri = _GwSpecificRtcpXrCollectorUri_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 1000, 1, 300),
    _GwSpecificRtcpXrCollectorUri_Type()
)
gwSpecificRtcpXrCollectorUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRtcpXrCollectorUri.setStatus("current")


class _GwSpecificRtcpXrPeriodicReportsInterval_Type(Unsigned32):
    """Custom type gwSpecificRtcpXrPeriodicReportsInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_GwSpecificRtcpXrPeriodicReportsInterval_Type.__name__ = "Unsigned32"
_GwSpecificRtcpXrPeriodicReportsInterval_Object = MibTableColumn
gwSpecificRtcpXrPeriodicReportsInterval = _GwSpecificRtcpXrPeriodicReportsInterval_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 2700, 1000, 1, 400),
    _GwSpecificRtcpXrPeriodicReportsInterval_Type()
)
gwSpecificRtcpXrPeriodicReportsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gwSpecificRtcpXrPeriodicReportsInterval.setStatus("current")
_InteropGroup_ObjectIdentity = ObjectIdentity
interopGroup = _InteropGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000)
)


class _InteropTransmissionTimeout_Type(Unsigned32):
    """Custom type interopTransmissionTimeout based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_InteropTransmissionTimeout_Type.__name__ = "Unsigned32"
_InteropTransmissionTimeout_Object = MibScalar
interopTransmissionTimeout = _InteropTransmissionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 400),
    _InteropTransmissionTimeout_Type()
)
interopTransmissionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopTransmissionTimeout.setStatus("current")


class _InteropTcpConnectTimeout_Type(Unsigned32):
    """Custom type interopTcpConnectTimeout based on Unsigned32"""
    defaultValue = 127

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_InteropTcpConnectTimeout_Type.__name__ = "Unsigned32"
_InteropTcpConnectTimeout_Object = MibScalar
interopTcpConnectTimeout = _InteropTcpConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 450),
    _InteropTcpConnectTimeout_Type()
)
interopTcpConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopTcpConnectTimeout.setStatus("current")


class _InteropSymmetricUdpSourcePortEnable_Type(MxEnableState):
    """Custom type interopSymmetricUdpSourcePortEnable based on MxEnableState"""
    defaultValue = 1


_InteropSymmetricUdpSourcePortEnable_Type.__name__ = "MxEnableState"
_InteropSymmetricUdpSourcePortEnable_Object = MibScalar
interopSymmetricUdpSourcePortEnable = _InteropSymmetricUdpSourcePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 600),
    _InteropSymmetricUdpSourcePortEnable_Type()
)
interopSymmetricUdpSourcePortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSymmetricUdpSourcePortEnable.setStatus("current")


class _InteropMaxForwardsValue_Type(Integer32):
    """Custom type interopMaxForwardsValue based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_InteropMaxForwardsValue_Type.__name__ = "Integer32"
_InteropMaxForwardsValue_Object = MibScalar
interopMaxForwardsValue = _InteropMaxForwardsValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 700),
    _InteropMaxForwardsValue_Type()
)
interopMaxForwardsValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopMaxForwardsValue.setStatus("current")


class _InteropSendUaHeaderEnable_Type(MxEnableState):
    """Custom type interopSendUaHeaderEnable based on MxEnableState"""
    defaultValue = 1


_InteropSendUaHeaderEnable_Type.__name__ = "MxEnableState"
_InteropSendUaHeaderEnable_Object = MibScalar
interopSendUaHeaderEnable = _InteropSendUaHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 800),
    _InteropSendUaHeaderEnable_Type()
)
interopSendUaHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSendUaHeaderEnable.setStatus("current")


class _InteropSdpDirectionAttributeEnable_Type(MxEnableState):
    """Custom type interopSdpDirectionAttributeEnable based on MxEnableState"""
    defaultValue = 1


_InteropSdpDirectionAttributeEnable_Type.__name__ = "MxEnableState"
_InteropSdpDirectionAttributeEnable_Object = MibScalar
interopSdpDirectionAttributeEnable = _InteropSdpDirectionAttributeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 900),
    _InteropSdpDirectionAttributeEnable_Type()
)
interopSdpDirectionAttributeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpDirectionAttributeEnable.setStatus("current")


class _InteropSdpDetectPeerDirectionAttributeSupportEnable_Type(MxEnableState):
    """Custom type interopSdpDetectPeerDirectionAttributeSupportEnable based on MxEnableState"""
    defaultValue = 1


_InteropSdpDetectPeerDirectionAttributeSupportEnable_Type.__name__ = "MxEnableState"
_InteropSdpDetectPeerDirectionAttributeSupportEnable_Object = MibScalar
interopSdpDetectPeerDirectionAttributeSupportEnable = _InteropSdpDetectPeerDirectionAttributeSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 950),
    _InteropSdpDetectPeerDirectionAttributeSupportEnable_Type()
)
interopSdpDetectPeerDirectionAttributeSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpDetectPeerDirectionAttributeSupportEnable.setStatus("current")


class _InteropOnHoldSdpConnectionAddress_Type(Integer32):
    """Custom type interopOnHoldSdpConnectionAddress based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("holdAddress", 100),
          ("mediaAddress", 200))
    )


_InteropOnHoldSdpConnectionAddress_Type.__name__ = "Integer32"
_InteropOnHoldSdpConnectionAddress_Object = MibScalar
interopOnHoldSdpConnectionAddress = _InteropOnHoldSdpConnectionAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 975),
    _InteropOnHoldSdpConnectionAddress_Type()
)
interopOnHoldSdpConnectionAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopOnHoldSdpConnectionAddress.setStatus("current")


class _InteropOnHoldSdpStreamDirection_Type(Integer32):
    """Custom type interopOnHoldSdpStreamDirection based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 100),
          ("sendonly", 200))
    )


_InteropOnHoldSdpStreamDirection_Type.__name__ = "Integer32"
_InteropOnHoldSdpStreamDirection_Object = MibScalar
interopOnHoldSdpStreamDirection = _InteropOnHoldSdpStreamDirection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1000),
    _InteropOnHoldSdpStreamDirection_Type()
)
interopOnHoldSdpStreamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopOnHoldSdpStreamDirection.setStatus("current")


class _InteropOnHoldAnswerSdpStreamDirection_Type(Integer32):
    """Custom type interopOnHoldAnswerSdpStreamDirection based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 100),
          ("recvonly", 200))
    )


_InteropOnHoldAnswerSdpStreamDirection_Type.__name__ = "Integer32"
_InteropOnHoldAnswerSdpStreamDirection_Object = MibScalar
interopOnHoldAnswerSdpStreamDirection = _InteropOnHoldAnswerSdpStreamDirection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1025),
    _InteropOnHoldAnswerSdpStreamDirection_Type()
)
interopOnHoldAnswerSdpStreamDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopOnHoldAnswerSdpStreamDirection.setStatus("current")


class _InteropSdpDirectionAttributeLevel_Type(Integer32):
    """Custom type interopSdpDirectionAttributeLevel based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("mediaOrSessionLevel", 100),
          ("mediaAndSessionLevel", 200))
    )


_InteropSdpDirectionAttributeLevel_Type.__name__ = "Integer32"
_InteropSdpDirectionAttributeLevel_Object = MibScalar
interopSdpDirectionAttributeLevel = _InteropSdpDirectionAttributeLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1050),
    _InteropSdpDirectionAttributeLevel_Type()
)
interopSdpDirectionAttributeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpDirectionAttributeLevel.setStatus("current")


class _InteropLocalRingOnProvisionalResponse_Type(Integer32):
    """Custom type interopLocalRingOnProvisionalResponse based on Integer32"""
    defaultValue = 0

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
          ("localRingWhenNoEstablishedMediaStream", 1),
          ("localRingAlways", 2))
    )


_InteropLocalRingOnProvisionalResponse_Type.__name__ = "Integer32"
_InteropLocalRingOnProvisionalResponse_Object = MibScalar
interopLocalRingOnProvisionalResponse = _InteropLocalRingOnProvisionalResponse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1100),
    _InteropLocalRingOnProvisionalResponse_Type()
)
interopLocalRingOnProvisionalResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopLocalRingOnProvisionalResponse.setStatus("current")


class _InteropSdpOriginLineSessionIdAndVersionMaxLength_Type(Integer32):
    """Custom type interopSdpOriginLineSessionIdAndVersionMaxLength based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("max32bits", 100),
          ("max64bits", 200))
    )


_InteropSdpOriginLineSessionIdAndVersionMaxLength_Type.__name__ = "Integer32"
_InteropSdpOriginLineSessionIdAndVersionMaxLength_Object = MibScalar
interopSdpOriginLineSessionIdAndVersionMaxLength = _InteropSdpOriginLineSessionIdAndVersionMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1200),
    _InteropSdpOriginLineSessionIdAndVersionMaxLength_Type()
)
interopSdpOriginLineSessionIdAndVersionMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpOriginLineSessionIdAndVersionMaxLength.setStatus("current")


class _InteropLockDnsSrvRecordPerCallEnable_Type(MxEnableState):
    """Custom type interopLockDnsSrvRecordPerCallEnable based on MxEnableState"""
    defaultValue = 0


_InteropLockDnsSrvRecordPerCallEnable_Type.__name__ = "MxEnableState"
_InteropLockDnsSrvRecordPerCallEnable_Object = MibScalar
interopLockDnsSrvRecordPerCallEnable = _InteropLockDnsSrvRecordPerCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1400),
    _InteropLockDnsSrvRecordPerCallEnable_Type()
)
interopLockDnsSrvRecordPerCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopLockDnsSrvRecordPerCallEnable.setStatus("current")


class _InteropRejectCodeForUnsupportedSdpOffer_Type(Integer32):
    """Custom type interopRejectCodeForUnsupportedSdpOffer based on Integer32"""
    defaultValue = 415

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(415,
              488)
        )
    )
    namedValues = NamedValues(
        *(("unsupportedMediaType", 415),
          ("notAcceptableHere", 488))
    )


_InteropRejectCodeForUnsupportedSdpOffer_Type.__name__ = "Integer32"
_InteropRejectCodeForUnsupportedSdpOffer_Object = MibScalar
interopRejectCodeForUnsupportedSdpOffer = _InteropRejectCodeForUnsupportedSdpOffer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 1750),
    _InteropRejectCodeForUnsupportedSdpOffer_Type()
)
interopRejectCodeForUnsupportedSdpOffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopRejectCodeForUnsupportedSdpOffer.setStatus("current")


class _InteropUseDtmfPayloadTypeFoundInAnswer_Type(MxEnableState):
    """Custom type interopUseDtmfPayloadTypeFoundInAnswer based on MxEnableState"""
    defaultValue = 0


_InteropUseDtmfPayloadTypeFoundInAnswer_Type.__name__ = "MxEnableState"
_InteropUseDtmfPayloadTypeFoundInAnswer_Object = MibScalar
interopUseDtmfPayloadTypeFoundInAnswer = _InteropUseDtmfPayloadTypeFoundInAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 2200),
    _InteropUseDtmfPayloadTypeFoundInAnswer_Type()
)
interopUseDtmfPayloadTypeFoundInAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopUseDtmfPayloadTypeFoundInAnswer.setStatus("current")


class _InteropRegisterHomeDomainOverride_Type(OctetString):
    """Custom type interopRegisterHomeDomainOverride based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InteropRegisterHomeDomainOverride_Type.__name__ = "OctetString"
_InteropRegisterHomeDomainOverride_Object = MibScalar
interopRegisterHomeDomainOverride = _InteropRegisterHomeDomainOverride_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 2400),
    _InteropRegisterHomeDomainOverride_Type()
)
interopRegisterHomeDomainOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopRegisterHomeDomainOverride.setStatus("current")


class _InteropEnforceOfferAnswerModel_Type(MxEnableState):
    """Custom type interopEnforceOfferAnswerModel based on MxEnableState"""
    defaultValue = 1


_InteropEnforceOfferAnswerModel_Type.__name__ = "MxEnableState"
_InteropEnforceOfferAnswerModel_Object = MibScalar
interopEnforceOfferAnswerModel = _InteropEnforceOfferAnswerModel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 2600),
    _InteropEnforceOfferAnswerModel_Type()
)
interopEnforceOfferAnswerModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopEnforceOfferAnswerModel.setStatus("current")


class _InteropMapPlusToTonInternational_Type(MxEnableState):
    """Custom type interopMapPlusToTonInternational based on MxEnableState"""
    defaultValue = 1


_InteropMapPlusToTonInternational_Type.__name__ = "MxEnableState"
_InteropMapPlusToTonInternational_Object = MibScalar
interopMapPlusToTonInternational = _InteropMapPlusToTonInternational_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 2700),
    _InteropMapPlusToTonInternational_Type()
)
interopMapPlusToTonInternational.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopMapPlusToTonInternational.setStatus("current")


class _InteropAllowLessMediaInResponse_Type(MxEnableState):
    """Custom type interopAllowLessMediaInResponse based on MxEnableState"""
    defaultValue = 0


_InteropAllowLessMediaInResponse_Type.__name__ = "MxEnableState"
_InteropAllowLessMediaInResponse_Object = MibScalar
interopAllowLessMediaInResponse = _InteropAllowLessMediaInResponse_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 2800),
    _InteropAllowLessMediaInResponse_Type()
)
interopAllowLessMediaInResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopAllowLessMediaInResponse.setStatus("current")


class _InteropDefaultUsernameValue_Type(Integer32):
    """Custom type interopDefaultUsernameValue based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("anonymous", 100),
          ("host", 200))
    )


_InteropDefaultUsernameValue_Type.__name__ = "Integer32"
_InteropDefaultUsernameValue_Object = MibScalar
interopDefaultUsernameValue = _InteropDefaultUsernameValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3000),
    _InteropDefaultUsernameValue_Type()
)
interopDefaultUsernameValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDefaultUsernameValue.setStatus("current")


class _InteropCallWaitingSipInfoPrivateNumberCriteria_Type(OctetString):
    """Custom type interopCallWaitingSipInfoPrivateNumberCriteria based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InteropCallWaitingSipInfoPrivateNumberCriteria_Type.__name__ = "OctetString"
_InteropCallWaitingSipInfoPrivateNumberCriteria_Object = MibScalar
interopCallWaitingSipInfoPrivateNumberCriteria = _InteropCallWaitingSipInfoPrivateNumberCriteria_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3250),
    _InteropCallWaitingSipInfoPrivateNumberCriteria_Type()
)
interopCallWaitingSipInfoPrivateNumberCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopCallWaitingSipInfoPrivateNumberCriteria.setStatus("current")


class _InteropSdpT38ParametersEncoding_Type(Integer32):
    """Custom type interopSdpT38ParametersEncoding based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("ituT38AnnexD", 100),
          ("sippingRealTimeFax00InternetDraft", 200))
    )


_InteropSdpT38ParametersEncoding_Type.__name__ = "Integer32"
_InteropSdpT38ParametersEncoding_Object = MibScalar
interopSdpT38ParametersEncoding = _InteropSdpT38ParametersEncoding_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3300),
    _InteropSdpT38ParametersEncoding_Type()
)
interopSdpT38ParametersEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpT38ParametersEncoding.setStatus("current")


class _InteropReInviteForVoiceOn606NotAcceptable_Type(MxEnableState):
    """Custom type interopReInviteForVoiceOn606NotAcceptable based on MxEnableState"""
    defaultValue = 0


_InteropReInviteForVoiceOn606NotAcceptable_Type.__name__ = "MxEnableState"
_InteropReInviteForVoiceOn606NotAcceptable_Object = MibScalar
interopReInviteForVoiceOn606NotAcceptable = _InteropReInviteForVoiceOn606NotAcceptable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3400),
    _InteropReInviteForVoiceOn606NotAcceptable_Type()
)
interopReInviteForVoiceOn606NotAcceptable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopReInviteForVoiceOn606NotAcceptable.setStatus("current")


class _InteropAllowMultipleActiveMediaInAnswer_Type(MxEnableState):
    """Custom type interopAllowMultipleActiveMediaInAnswer based on MxEnableState"""
    defaultValue = 1


_InteropAllowMultipleActiveMediaInAnswer_Type.__name__ = "MxEnableState"
_InteropAllowMultipleActiveMediaInAnswer_Object = MibScalar
interopAllowMultipleActiveMediaInAnswer = _InteropAllowMultipleActiveMediaInAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3500),
    _InteropAllowMultipleActiveMediaInAnswer_Type()
)
interopAllowMultipleActiveMediaInAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopAllowMultipleActiveMediaInAnswer.setStatus("current")


class _InteropIgnoreSipOptionsOnNoUsuableEndpoints_Type(MxEnableState):
    """Custom type interopIgnoreSipOptionsOnNoUsuableEndpoints based on MxEnableState"""
    defaultValue = 0


_InteropIgnoreSipOptionsOnNoUsuableEndpoints_Type.__name__ = "MxEnableState"
_InteropIgnoreSipOptionsOnNoUsuableEndpoints_Object = MibScalar
interopIgnoreSipOptionsOnNoUsuableEndpoints = _InteropIgnoreSipOptionsOnNoUsuableEndpoints_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3550),
    _InteropIgnoreSipOptionsOnNoUsuableEndpoints_Type()
)
interopIgnoreSipOptionsOnNoUsuableEndpoints.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopIgnoreSipOptionsOnNoUsuableEndpoints.setStatus("current")


class _InteropSipOptionsMethodSupport_Type(Integer32):
    """Custom type interopSipOptionsMethodSupport based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("alwaysOk", 200))
    )


_InteropSipOptionsMethodSupport_Type.__name__ = "Integer32"
_InteropSipOptionsMethodSupport_Object = MibScalar
interopSipOptionsMethodSupport = _InteropSipOptionsMethodSupport_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3600),
    _InteropSipOptionsMethodSupport_Type()
)
interopSipOptionsMethodSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSipOptionsMethodSupport.setStatus("current")


class _InteropAllowMediaReactivationInAnswer_Type(MxEnableState):
    """Custom type interopAllowMediaReactivationInAnswer based on MxEnableState"""
    defaultValue = 0


_InteropAllowMediaReactivationInAnswer_Type.__name__ = "MxEnableState"
_InteropAllowMediaReactivationInAnswer_Object = MibScalar
interopAllowMediaReactivationInAnswer = _InteropAllowMediaReactivationInAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3700),
    _InteropAllowMediaReactivationInAnswer_Type()
)
interopAllowMediaReactivationInAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopAllowMediaReactivationInAnswer.setStatus("current")


class _InteropAllowAudioAndImageNegotiation_Type(Integer32):
    """Custom type interopAllowAudioAndImageNegotiation based on Integer32"""
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
        *(("enable", 100),
          ("disableOffer", 200),
          ("disableAll", 300))
    )


_InteropAllowAudioAndImageNegotiation_Type.__name__ = "Integer32"
_InteropAllowAudioAndImageNegotiation_Object = MibScalar
interopAllowAudioAndImageNegotiation = _InteropAllowAudioAndImageNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 3800),
    _InteropAllowAudioAndImageNegotiation_Type()
)
interopAllowAudioAndImageNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopAllowAudioAndImageNegotiation.setStatus("current")


class _InteropEscapePoundInSipUriUsername_Type(MxEnableState):
    """Custom type interopEscapePoundInSipUriUsername based on MxEnableState"""
    defaultValue = 1


_InteropEscapePoundInSipUriUsername_Type.__name__ = "MxEnableState"
_InteropEscapePoundInSipUriUsername_Object = MibScalar
interopEscapePoundInSipUriUsername = _InteropEscapePoundInSipUriUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4000),
    _InteropEscapePoundInSipUriUsername_Type()
)
interopEscapePoundInSipUriUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopEscapePoundInSipUriUsername.setStatus("current")


class _InteropSiemensTransportHeaderEnable_Type(MxEnableState):
    """Custom type interopSiemensTransportHeaderEnable based on MxEnableState"""
    defaultValue = 0


_InteropSiemensTransportHeaderEnable_Type.__name__ = "MxEnableState"
_InteropSiemensTransportHeaderEnable_Object = MibScalar
interopSiemensTransportHeaderEnable = _InteropSiemensTransportHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4100),
    _InteropSiemensTransportHeaderEnable_Type()
)
interopSiemensTransportHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSiemensTransportHeaderEnable.setStatus("current")


class _InteropTlsClientAuthenticationEnable_Type(MxEnableState):
    """Custom type interopTlsClientAuthenticationEnable based on MxEnableState"""
    defaultValue = 0


_InteropTlsClientAuthenticationEnable_Type.__name__ = "MxEnableState"
_InteropTlsClientAuthenticationEnable_Object = MibScalar
interopTlsClientAuthenticationEnable = _InteropTlsClientAuthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4200),
    _InteropTlsClientAuthenticationEnable_Type()
)
interopTlsClientAuthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopTlsClientAuthenticationEnable.setStatus("current")


class _InteropTlsCertificateValidation_Type(Integer32):
    """Custom type interopTlsCertificateValidation based on Integer32"""
    defaultValue = 400

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
        *(("noValidation", 100),
          ("trustedCertificate", 200),
          ("dnsSrvResponse", 300),
          ("hostName", 400))
    )


_InteropTlsCertificateValidation_Type.__name__ = "Integer32"
_InteropTlsCertificateValidation_Object = MibScalar
interopTlsCertificateValidation = _InteropTlsCertificateValidation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4250),
    _InteropTlsCertificateValidation_Type()
)
interopTlsCertificateValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopTlsCertificateValidation.setStatus("current")


class _InteropIgnorePlusInUsername_Type(MxEnableState):
    """Custom type interopIgnorePlusInUsername based on MxEnableState"""
    defaultValue = 0


_InteropIgnorePlusInUsername_Type.__name__ = "MxEnableState"
_InteropIgnorePlusInUsername_Object = MibScalar
interopIgnorePlusInUsername = _InteropIgnorePlusInUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4300),
    _InteropIgnorePlusInUsername_Type()
)
interopIgnorePlusInUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopIgnorePlusInUsername.setStatus("current")
_BehaviorOnT38InviteNotAcceptedTable_Object = MibTable
behaviorOnT38InviteNotAcceptedTable = _BehaviorOnT38InviteNotAcceptedTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4600)
)
if mibBuilder.loadTexts:
    behaviorOnT38InviteNotAcceptedTable.setStatus("current")
_BehaviorOnT38InviteNotAcceptedEntry_Object = MibTableRow
behaviorOnT38InviteNotAcceptedEntry = _BehaviorOnT38InviteNotAcceptedEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4600, 1)
)
behaviorOnT38InviteNotAcceptedEntry.setIndexNames(
    (0, "MX-SIPEP-MIB", "behaviorOnT38InviteNotAcceptedSipErrorCode"),
)
if mibBuilder.loadTexts:
    behaviorOnT38InviteNotAcceptedEntry.setStatus("current")


class _BehaviorOnT38InviteNotAcceptedSipErrorCode_Type(Unsigned32):
    """Custom type behaviorOnT38InviteNotAcceptedSipErrorCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(406, 406),
        ValueRangeConstraint(415, 415),
        ValueRangeConstraint(488, 488),
        ValueRangeConstraint(606, 606),
    )


_BehaviorOnT38InviteNotAcceptedSipErrorCode_Type.__name__ = "Unsigned32"
_BehaviorOnT38InviteNotAcceptedSipErrorCode_Object = MibTableColumn
behaviorOnT38InviteNotAcceptedSipErrorCode = _BehaviorOnT38InviteNotAcceptedSipErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4600, 1, 100),
    _BehaviorOnT38InviteNotAcceptedSipErrorCode_Type()
)
behaviorOnT38InviteNotAcceptedSipErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    behaviorOnT38InviteNotAcceptedSipErrorCode.setStatus("current")


class _BehaviorOnT38InviteNotAcceptedBehavior_Type(Integer32):
    """Custom type behaviorOnT38InviteNotAcceptedBehavior based on Integer32"""
    defaultValue = 200

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
        *(("dropCall", 100),
          ("reInviteForClearChannelOnly", 200),
          ("reEstablishAudio", 300),
          ("usePreviousMediaNegotiation", 400))
    )


_BehaviorOnT38InviteNotAcceptedBehavior_Type.__name__ = "Integer32"
_BehaviorOnT38InviteNotAcceptedBehavior_Object = MibTableColumn
behaviorOnT38InviteNotAcceptedBehavior = _BehaviorOnT38InviteNotAcceptedBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4600, 1, 200),
    _BehaviorOnT38InviteNotAcceptedBehavior_Type()
)
behaviorOnT38InviteNotAcceptedBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    behaviorOnT38InviteNotAcceptedBehavior.setStatus("current")


class _InteropBehaviorOnMachineDetection_Type(Integer32):
    """Custom type interopBehaviorOnMachineDetection based on Integer32"""
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
        *(("reInviteOnFaxT38Only", 100),
          ("reInviteOnNoNegotiatedDataCodec", 200),
          ("reInviteUnconditional", 300))
    )


_InteropBehaviorOnMachineDetection_Type.__name__ = "Integer32"
_InteropBehaviorOnMachineDetection_Object = MibScalar
interopBehaviorOnMachineDetection = _InteropBehaviorOnMachineDetection_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4650),
    _InteropBehaviorOnMachineDetection_Type()
)
interopBehaviorOnMachineDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopBehaviorOnMachineDetection.setStatus("current")


class _InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Type(Integer32):
    """Custom type interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("firstCodec", 100),
          ("prioritizeClearChannel", 200))
    )


_InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Type.__name__ = "Integer32"
_InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Object = MibScalar
interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice = _InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4700),
    _InteropCodecVsBearerCapabilitiesMappingPreferredCodecChoice_Type()
)
interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice.setStatus("current")


class _InteropSipUriUserParameterValue_Type(OctetString):
    """Custom type interopSipUriUserParameterValue based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InteropSipUriUserParameterValue_Type.__name__ = "OctetString"
_InteropSipUriUserParameterValue_Object = MibScalar
interopSipUriUserParameterValue = _InteropSipUriUserParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4800),
    _InteropSipUriUserParameterValue_Type()
)
interopSipUriUserParameterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSipUriUserParameterValue.setStatus("current")


class _InteropListenForEarlyRtpEnable_Type(MxEnableState):
    """Custom type interopListenForEarlyRtpEnable based on MxEnableState"""
    defaultValue = 0


_InteropListenForEarlyRtpEnable_Type.__name__ = "MxEnableState"
_InteropListenForEarlyRtpEnable_Object = MibScalar
interopListenForEarlyRtpEnable = _InteropListenForEarlyRtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 4900),
    _InteropListenForEarlyRtpEnable_Type()
)
interopListenForEarlyRtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopListenForEarlyRtpEnable.setStatus("current")


class _InteropRegistrationContactMatching_Type(Integer32):
    """Custom type interopRegistrationContactMatching based on Integer32"""
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
        *(("strict", 100),
          ("ignoreUriParams", 200),
          ("ignoreUriAndPortParams", 300))
    )


_InteropRegistrationContactMatching_Type.__name__ = "Integer32"
_InteropRegistrationContactMatching_Object = MibScalar
interopRegistrationContactMatching = _InteropRegistrationContactMatching_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5000),
    _InteropRegistrationContactMatching_Type()
)
interopRegistrationContactMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopRegistrationContactMatching.setStatus("current")


class _InteropResolveRouteHeaderEnable_Type(MxEnableState):
    """Custom type interopResolveRouteHeaderEnable based on MxEnableState"""
    defaultValue = 0


_InteropResolveRouteHeaderEnable_Type.__name__ = "MxEnableState"
_InteropResolveRouteHeaderEnable_Object = MibScalar
interopResolveRouteHeaderEnable = _InteropResolveRouteHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5100),
    _InteropResolveRouteHeaderEnable_Type()
)
interopResolveRouteHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopResolveRouteHeaderEnable.setStatus("current")


class _InteropForceDnsNaptrInTls_Type(MxEnableState):
    """Custom type interopForceDnsNaptrInTls based on MxEnableState"""
    defaultValue = 0


_InteropForceDnsNaptrInTls_Type.__name__ = "MxEnableState"
_InteropForceDnsNaptrInTls_Object = MibScalar
interopForceDnsNaptrInTls = _InteropForceDnsNaptrInTls_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5200),
    _InteropForceDnsNaptrInTls_Type()
)
interopForceDnsNaptrInTls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopForceDnsNaptrInTls.setStatus("current")


class _InteropAckBranchMatching_Type(Integer32):
    """Custom type interopAckBranchMatching based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("rfc3261", 100),
          ("rfc3261WithoutAck", 200))
    )


_InteropAckBranchMatching_Type.__name__ = "Integer32"
_InteropAckBranchMatching_Object = MibScalar
interopAckBranchMatching = _InteropAckBranchMatching_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5300),
    _InteropAckBranchMatching_Type()
)
interopAckBranchMatching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopAckBranchMatching.setStatus("current")


class _InteropIgnoreRequireHeaderEnable_Type(MxEnableState):
    """Custom type interopIgnoreRequireHeaderEnable based on MxEnableState"""
    defaultValue = 1


_InteropIgnoreRequireHeaderEnable_Type.__name__ = "MxEnableState"
_InteropIgnoreRequireHeaderEnable_Object = MibScalar
interopIgnoreRequireHeaderEnable = _InteropIgnoreRequireHeaderEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5400),
    _InteropIgnoreRequireHeaderEnable_Type()
)
interopIgnoreRequireHeaderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopIgnoreRequireHeaderEnable.setStatus("current")


class _InteropUaHeaderFormat_Type(OctetString):
    """Custom type interopUaHeaderFormat based on OctetString"""
    defaultValue = OctetString("%product%/v%version% %profile%")


_InteropUaHeaderFormat_Type.__name__ = "OctetString"
_InteropUaHeaderFormat_Object = MibScalar
interopUaHeaderFormat = _InteropUaHeaderFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5500),
    _InteropUaHeaderFormat_Type()
)
interopUaHeaderFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopUaHeaderFormat.setStatus("current")


class _InteropSipInfoWithoutContentAnswer_Type(Integer32):
    """Custom type interopSipInfoWithoutContentAnswer based on Integer32"""
    defaultValue = 415

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              415)
        )
    )
    namedValues = NamedValues(
        *(("ok", 200),
          ("unsupportedMediaType", 415))
    )


_InteropSipInfoWithoutContentAnswer_Type.__name__ = "Integer32"
_InteropSipInfoWithoutContentAnswer_Object = MibScalar
interopSipInfoWithoutContentAnswer = _InteropSipInfoWithoutContentAnswer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5600),
    _InteropSipInfoWithoutContentAnswer_Type()
)
interopSipInfoWithoutContentAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSipInfoWithoutContentAnswer.setStatus("current")


class _InteropRegistrationDelayValue_Type(Unsigned32):
    """Custom type interopRegistrationDelayValue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_InteropRegistrationDelayValue_Type.__name__ = "Unsigned32"
_InteropRegistrationDelayValue_Object = MibScalar
interopRegistrationDelayValue = _InteropRegistrationDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5700),
    _InteropRegistrationDelayValue_Type()
)
interopRegistrationDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopRegistrationDelayValue.setStatus("current")


class _InteropUnsupportedContentType_Type(Integer32):
    """Custom type interopUnsupportedContentType based on Integer32"""
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
        *(("reject", 100),
          ("allow", 200),
          ("ignore", 300))
    )


_InteropUnsupportedContentType_Type.__name__ = "Integer32"
_InteropUnsupportedContentType_Object = MibScalar
interopUnsupportedContentType = _InteropUnsupportedContentType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5800),
    _InteropUnsupportedContentType_Type()
)
interopUnsupportedContentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopUnsupportedContentType.setStatus("current")


class _InteropWaitConfirmedDialogForBlindTransfer_Type(MxEnableState):
    """Custom type interopWaitConfirmedDialogForBlindTransfer based on MxEnableState"""
    defaultValue = 0


_InteropWaitConfirmedDialogForBlindTransfer_Type.__name__ = "MxEnableState"
_InteropWaitConfirmedDialogForBlindTransfer_Object = MibScalar
interopWaitConfirmedDialogForBlindTransfer = _InteropWaitConfirmedDialogForBlindTransfer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 5900),
    _InteropWaitConfirmedDialogForBlindTransfer_Type()
)
interopWaitConfirmedDialogForBlindTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopWaitConfirmedDialogForBlindTransfer.setStatus("obsolete")


class _InteropPendingBlindTransferTimeout_Type(Unsigned32):
    """Custom type interopPendingBlindTransferTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_InteropPendingBlindTransferTimeout_Type.__name__ = "Unsigned32"
_InteropPendingBlindTransferTimeout_Object = MibScalar
interopPendingBlindTransferTimeout = _InteropPendingBlindTransferTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6000),
    _InteropPendingBlindTransferTimeout_Type()
)
interopPendingBlindTransferTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopPendingBlindTransferTimeout.setStatus("current")


class _InteropForkedProvisionalResponsesBehavior_Type(Integer32):
    """Custom type interopForkedProvisionalResponsesBehavior based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("interpretFirst", 100),
          ("interpretAll", 200))
    )


_InteropForkedProvisionalResponsesBehavior_Type.__name__ = "Integer32"
_InteropForkedProvisionalResponsesBehavior_Object = MibScalar
interopForkedProvisionalResponsesBehavior = _InteropForkedProvisionalResponsesBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6100),
    _InteropForkedProvisionalResponsesBehavior_Type()
)
interopForkedProvisionalResponsesBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopForkedProvisionalResponsesBehavior.setStatus("current")


class _InteropReliableForkedProvisionalResponsesBehavior_Type(Integer32):
    """Custom type interopReliableForkedProvisionalResponsesBehavior based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("interpretFirst", 100),
          ("interpretFirstRemoteMedia", 200))
    )


_InteropReliableForkedProvisionalResponsesBehavior_Type.__name__ = "Integer32"
_InteropReliableForkedProvisionalResponsesBehavior_Object = MibScalar
interopReliableForkedProvisionalResponsesBehavior = _InteropReliableForkedProvisionalResponsesBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6110),
    _InteropReliableForkedProvisionalResponsesBehavior_Type()
)
interopReliableForkedProvisionalResponsesBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopReliableForkedProvisionalResponsesBehavior.setStatus("current")


class _InteropSipContactDisplayNamePresence_Type(MxEnableState):
    """Custom type interopSipContactDisplayNamePresence based on MxEnableState"""
    defaultValue = 1


_InteropSipContactDisplayNamePresence_Type.__name__ = "MxEnableState"
_InteropSipContactDisplayNamePresence_Object = MibScalar
interopSipContactDisplayNamePresence = _InteropSipContactDisplayNamePresence_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6200),
    _InteropSipContactDisplayNamePresence_Type()
)
interopSipContactDisplayNamePresence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSipContactDisplayNamePresence.setStatus("current")


class _InteropEscapeFormat_Type(Integer32):
    """Custom type interopEscapeFormat based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("lowercaseHex", 100),
          ("uppercaseHex", 200))
    )


_InteropEscapeFormat_Type.__name__ = "Integer32"
_InteropEscapeFormat_Object = MibScalar
interopEscapeFormat = _InteropEscapeFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6300),
    _InteropEscapeFormat_Type()
)
interopEscapeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopEscapeFormat.setStatus("current")


class _InteropKeepAliveOptionFormat_Type(Integer32):
    """Custom type interopKeepAliveOptionFormat based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("shortFrom", 100),
          ("fullFrom", 200))
    )


_InteropKeepAliveOptionFormat_Type.__name__ = "Integer32"
_InteropKeepAliveOptionFormat_Object = MibScalar
interopKeepAliveOptionFormat = _InteropKeepAliveOptionFormat_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6400),
    _InteropKeepAliveOptionFormat_Type()
)
interopKeepAliveOptionFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopKeepAliveOptionFormat.setStatus("current")


class _InteropInfoDtmfRelayFlashEvent_Type(Integer32):
    """Custom type interopInfoDtmfRelayFlashEvent based on Integer32"""
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
        *(("disable", 100),
          ("evR", 200),
          ("ev16", 300))
    )


_InteropInfoDtmfRelayFlashEvent_Type.__name__ = "Integer32"
_InteropInfoDtmfRelayFlashEvent_Object = MibScalar
interopInfoDtmfRelayFlashEvent = _InteropInfoDtmfRelayFlashEvent_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6500),
    _InteropInfoDtmfRelayFlashEvent_Type()
)
interopInfoDtmfRelayFlashEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopInfoDtmfRelayFlashEvent.setStatus("current")


class _InteropSdpPTimeAttribute_Type(Integer32):
    """Custom type interopSdpPTimeAttribute based on Integer32"""
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
        *(("disabled", 100),
          ("declarativePreferredCodec", 200),
          ("declarativeConfigured", 300))
    )


_InteropSdpPTimeAttribute_Type.__name__ = "Integer32"
_InteropSdpPTimeAttribute_Object = MibScalar
interopSdpPTimeAttribute = _InteropSdpPTimeAttribute_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6600),
    _InteropSdpPTimeAttribute_Type()
)
interopSdpPTimeAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpPTimeAttribute.setStatus("current")


class _InteropSdpPTimeAttributeValue_Type(Unsigned32):
    """Custom type interopSdpPTimeAttributeValue based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 80),
    )


_InteropSdpPTimeAttributeValue_Type.__name__ = "Unsigned32"
_InteropSdpPTimeAttributeValue_Object = MibScalar
interopSdpPTimeAttributeValue = _InteropSdpPTimeAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6700),
    _InteropSdpPTimeAttributeValue_Type()
)
interopSdpPTimeAttributeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSdpPTimeAttributeValue.setStatus("current")


class _InteropIncrementSdpVersionWhenModified_Type(MxEnableState):
    """Custom type interopIncrementSdpVersionWhenModified based on MxEnableState"""
    defaultValue = 1


_InteropIncrementSdpVersionWhenModified_Type.__name__ = "MxEnableState"
_InteropIncrementSdpVersionWhenModified_Object = MibScalar
interopIncrementSdpVersionWhenModified = _InteropIncrementSdpVersionWhenModified_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 6800),
    _InteropIncrementSdpVersionWhenModified_Type()
)
interopIncrementSdpVersionWhenModified.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopIncrementSdpVersionWhenModified.setStatus("current")


class _InteropActivateEarlyMediaOnProvisionalResponseAck_Type(MxEnableState):
    """Custom type interopActivateEarlyMediaOnProvisionalResponseAck based on MxEnableState"""
    defaultValue = 0


_InteropActivateEarlyMediaOnProvisionalResponseAck_Type.__name__ = "MxEnableState"
_InteropActivateEarlyMediaOnProvisionalResponseAck_Object = MibScalar
interopActivateEarlyMediaOnProvisionalResponseAck = _InteropActivateEarlyMediaOnProvisionalResponseAck_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 7000),
    _InteropActivateEarlyMediaOnProvisionalResponseAck_Type()
)
interopActivateEarlyMediaOnProvisionalResponseAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopActivateEarlyMediaOnProvisionalResponseAck.setStatus("current")


class _InteropSend183WithSdpBefore180WithoutSdp_Type(MxEnableState):
    """Custom type interopSend183WithSdpBefore180WithoutSdp based on MxEnableState"""
    defaultValue = 0


_InteropSend183WithSdpBefore180WithoutSdp_Type.__name__ = "MxEnableState"
_InteropSend183WithSdpBefore180WithoutSdp_Object = MibScalar
interopSend183WithSdpBefore180WithoutSdp = _InteropSend183WithSdpBefore180WithoutSdp_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 7100),
    _InteropSend183WithSdpBefore180WithoutSdp_Type()
)
interopSend183WithSdpBefore180WithoutSdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopSend183WithSdpBefore180WithoutSdp.setStatus("current")


class _InteropCollectCallProprietaryHeader_Type(Integer32):
    """Custom type interopCollectCallProprietaryHeader based on Integer32"""
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
        *(("ignore", 100),
          ("relay", 200),
          ("block", 300))
    )


_InteropCollectCallProprietaryHeader_Type.__name__ = "Integer32"
_InteropCollectCallProprietaryHeader_Object = MibScalar
interopCollectCallProprietaryHeader = _InteropCollectCallProprietaryHeader_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 7200),
    _InteropCollectCallProprietaryHeader_Type()
)
interopCollectCallProprietaryHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopCollectCallProprietaryHeader.setStatus("current")
_InteropDtmfGroup_ObjectIdentity = ObjectIdentity
interopDtmfGroup = _InteropDtmfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 50000)
)


class _InteropDtmfTransportMethod_Type(Integer32):
    """Custom type interopDtmfTransportMethod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("draftChoudhuriSipInfoDigit00", 100),
          ("infoDtmfRelay", 200))
    )


_InteropDtmfTransportMethod_Type.__name__ = "Integer32"
_InteropDtmfTransportMethod_Object = MibScalar
interopDtmfTransportMethod = _InteropDtmfTransportMethod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 50000, 100),
    _InteropDtmfTransportMethod_Type()
)
interopDtmfTransportMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfTransportMethod.setStatus("current")


class _InteropDtmfTransportDuration_Type(Integer32):
    """Custom type interopDtmfTransportDuration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_InteropDtmfTransportDuration_Type.__name__ = "Integer32"
_InteropDtmfTransportDuration_Object = MibScalar
interopDtmfTransportDuration = _InteropDtmfTransportDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50000, 50000, 200),
    _InteropDtmfTransportDuration_Type()
)
interopDtmfTransportDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopDtmfTransportDuration.setStatus("current")
_MonitoringGroup_ObjectIdentity = ObjectIdentity
monitoringGroup = _MonitoringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50500)
)


class _SipNotificationsGateway_Type(OctetString):
    """Custom type sipNotificationsGateway based on OctetString"""
    defaultValue = OctetString("default")


_SipNotificationsGateway_Type.__name__ = "OctetString"
_SipNotificationsGateway_Object = MibScalar
sipNotificationsGateway = _SipNotificationsGateway_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50500, 100),
    _SipNotificationsGateway_Type()
)
sipNotificationsGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipNotificationsGateway.setStatus("current")


class _MaxNotificationsPerNotify_Type(Unsigned32):
    """Custom type maxNotificationsPerNotify based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_MaxNotificationsPerNotify_Type.__name__ = "Unsigned32"
_MaxNotificationsPerNotify_Object = MibScalar
maxNotificationsPerNotify = _MaxNotificationsPerNotify_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 50500, 200),
    _MaxNotificationsPerNotify_Type()
)
maxNotificationsPerNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxNotificationsPerNotify.setStatus("current")
_DebugGroup_ObjectIdentity = ObjectIdentity
debugGroup = _DebugGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 51000)
)


class _DebugSignalingLogEnable_Type(MxEnableState):
    """Custom type debugSignalingLogEnable based on MxEnableState"""
    defaultValue = 0


_DebugSignalingLogEnable_Type.__name__ = "MxEnableState"
_DebugSignalingLogEnable_Object = MibScalar
debugSignalingLogEnable = _DebugSignalingLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 51000, 100),
    _DebugSignalingLogEnable_Type()
)
debugSignalingLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugSignalingLogEnable.setStatus("current")


class _DebugSignalingLogHost_Type(MxIpHostNamePort):
    """Custom type debugSignalingLogHost based on MxIpHostNamePort"""
    defaultValue = OctetString("192.168.10.10:0")


_DebugSignalingLogHost_Type.__name__ = "MxIpHostNamePort"
_DebugSignalingLogHost_Object = MibScalar
debugSignalingLogHost = _DebugSignalingLogHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 51000, 200),
    _DebugSignalingLogHost_Type()
)
debugSignalingLogHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugSignalingLogHost.setStatus("current")


class _DebugContextSnapshotTime_Type(Unsigned32):
    """Custom type debugContextSnapshotTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_DebugContextSnapshotTime_Type.__name__ = "Unsigned32"
_DebugContextSnapshotTime_Object = MibScalar
debugContextSnapshotTime = _DebugContextSnapshotTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 51000, 300),
    _DebugContextSnapshotTime_Type()
)
debugContextSnapshotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    debugContextSnapshotTime.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1400, 1, 60020, 100),
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
    "MX-SIPEP-MIB",
    **{"sipEpMIB": sipEpMIB,
       "sipEpMIBObjects": sipEpMIBObjects,
       "gatewayTable": gatewayTable,
       "gatewayEntry": gatewayEntry,
       "gatewayName": gatewayName,
       "gatewayType": gatewayType,
       "gatewayNetworkInterface": gatewayNetworkInterface,
       "gatewayMediaNetworks": gatewayMediaNetworks,
       "gatewayPort": gatewayPort,
       "gatewaySecurePort": gatewaySecurePort,
       "gatewayDomain": gatewayDomain,
       "gatewayDelete": gatewayDelete,
       "gatewayStatusTable": gatewayStatusTable,
       "gatewayStatusEntry": gatewayStatusEntry,
       "gatewayStatusName": gatewayStatusName,
       "gatewayStatusNetworkInterface": gatewayStatusNetworkInterface,
       "gatewayStatusMediaNetworks": gatewayStatusMediaNetworks,
       "gatewayStatusPort": gatewayStatusPort,
       "gatewayStatusSecurePort": gatewayStatusSecurePort,
       "gatewayStatusDomain": gatewayStatusDomain,
       "gatewayStatusState": gatewayStatusState,
       "userAgentTable": userAgentTable,
       "userAgentEntry": userAgentEntry,
       "userAgentEpId": userAgentEpId,
       "userAgentUsername": userAgentUsername,
       "userAgentFriendlyName": userAgentFriendlyName,
       "userAgentRegister": userAgentRegister,
       "userAgentGatewayName": userAgentGatewayName,
       "userAgentMwiSubscribe": userAgentMwiSubscribe,
       "userAgentContactDomain": userAgentContactDomain,
       "userAgentAcceptLanguage": userAgentAcceptLanguage,
       "proxyGroup": proxyGroup,
       "defaultStaticProxyHomeDomainHost": defaultStaticProxyHomeDomainHost,
       "defaultStaticProxyOutboundHost": defaultStaticProxyOutboundHost,
       "defaultProxyOutboundType": defaultProxyOutboundType,
       "gwSpecificProxyTable": gwSpecificProxyTable,
       "gwSpecificProxyEntry": gwSpecificProxyEntry,
       "gwSpecificProxyGatewayName": gwSpecificProxyGatewayName,
       "gwSpecificProxyEnableConfig": gwSpecificProxyEnableConfig,
       "gwSpecificProxyHomeDomainHost": gwSpecificProxyHomeDomainHost,
       "gwSpecificProxyOutboundHost": gwSpecificProxyOutboundHost,
       "gwSpecificProxyOutboundType": gwSpecificProxyOutboundType,
       "sessionRefreshGroup": sessionRefreshGroup,
       "defaultSessionTimerEnable": defaultSessionTimerEnable,
       "defaultSessionTimerMinimumExpirationDelay": defaultSessionTimerMinimumExpirationDelay,
       "defaultSessionTimerMaximumExpirationDelay": defaultSessionTimerMaximumExpirationDelay,
       "sessionRefreshRequestMethod": sessionRefreshRequestMethod,
       "authenticationGroup": authenticationGroup,
       "authenticationTable": authenticationTable,
       "authenticationEntry": authenticationEntry,
       "authenticationIndex": authenticationIndex,
       "authenticationCriteriaSelection": authenticationCriteriaSelection,
       "authenticationEpId": authenticationEpId,
       "authenticationGatewayName": authenticationGatewayName,
       "authenticationUsernameCriteria": authenticationUsernameCriteria,
       "authenticationValidateRealm": authenticationValidateRealm,
       "authenticationRealm": authenticationRealm,
       "authenticationUsername": authenticationUsername,
       "authenticationPassword": authenticationPassword,
       "authenticationUp": authenticationUp,
       "authenticationDown": authenticationDown,
       "authenticationInsert": authenticationInsert,
       "authenticationDelete": authenticationDelete,
       "registrationGroup": registrationGroup,
       "defaultRegistrationRefreshTime": defaultRegistrationRefreshTime,
       "defaultRegistrationExpirationValue": defaultRegistrationExpirationValue,
       "defaultRegistrationProposedExpirationValue": defaultRegistrationProposedExpirationValue,
       "defaultRegistrationRetryTime": defaultRegistrationRetryTime,
       "defaultRegistrationUnregisteredBehavior": defaultRegistrationUnregisteredBehavior,
       "defaultUnitRegistrationUnregisteredBehavior": defaultUnitRegistrationUnregisteredBehavior,
       "defaultStaticRegistrarServerHost": defaultStaticRegistrarServerHost,
       "gwSpecificRegistrationTable": gwSpecificRegistrationTable,
       "gwSpecificRegistrationEntry": gwSpecificRegistrationEntry,
       "gwSpecificRegistrationGatewayName": gwSpecificRegistrationGatewayName,
       "gwSpecificRegistrationEnableConfig": gwSpecificRegistrationEnableConfig,
       "gwSpecificRegistrationRefreshTime": gwSpecificRegistrationRefreshTime,
       "gwSpecificRegistrationExpirationValue": gwSpecificRegistrationExpirationValue,
       "gwSpecificRegistrationProposedExpirationValue": gwSpecificRegistrationProposedExpirationValue,
       "gwSpecificRegistrationRetryTime": gwSpecificRegistrationRetryTime,
       "gwSpecificRegistrationUnregisteredBehavior": gwSpecificRegistrationUnregisteredBehavior,
       "gwSpecificRegistrationServerHost": gwSpecificRegistrationServerHost,
       "unitRegistrationsTable": unitRegistrationsTable,
       "unitRegistrationsEntry": unitRegistrationsEntry,
       "unitRegistrationsIndex": unitRegistrationsIndex,
       "unitRegistrationsUsername": unitRegistrationsUsername,
       "unitRegistrationsGatewayName": unitRegistrationsGatewayName,
       "unitRegistrationsDelete": unitRegistrationsDelete,
       "behaviorOnInitialRegistrationReception": behaviorOnInitialRegistrationReception,
       "registrationDelayOnInitialRegistrationReception": registrationDelayOnInitialRegistrationReception,
       "registrationStatusTable": registrationStatusTable,
       "registrationStatusEntry": registrationStatusEntry,
       "registrationStatusIndex": registrationStatusIndex,
       "registrationStatusGateway": registrationStatusGateway,
       "registrationStatusEndpoint": registrationStatusEndpoint,
       "registrationStatusState": registrationStatusState,
       "registrationStatusRegistrar": registrationStatusRegistrar,
       "registrationStatusUsername": registrationStatusUsername,
       "transportGroup": transportGroup,
       "transportPersistentBasePort": transportPersistentBasePort,
       "transportPersistentPortInterval": transportPersistentPortInterval,
       "transportFailbackInterval": transportFailbackInterval,
       "transportTlsCertificateTrustLevel": transportTlsCertificateTrustLevel,
       "transportTlsCipherSuite": transportTlsCipherSuite,
       "transportTlsVersion": transportTlsVersion,
       "transportConfigTable": transportConfigTable,
       "transportConfigEntry": transportConfigEntry,
       "transportConfigGatewayName": transportConfigGatewayName,
       "transportConfigRegistrationEnable": transportConfigRegistrationEnable,
       "transportConfigContactEnable": transportConfigContactEnable,
       "transportConfigUdpEnable": transportConfigUdpEnable,
       "transportConfigUdpQValue": transportConfigUdpQValue,
       "transportConfigTcpEnable": transportConfigTcpEnable,
       "transportConfigTcpQValue": transportConfigTcpQValue,
       "transportConfigTlsEnable": transportConfigTlsEnable,
       "transportConfigTlsQValue": transportConfigTlsQValue,
       "tlsPersistentConnectionStatusTable": tlsPersistentConnectionStatusTable,
       "tlsPersistentConnectionStatusEntry": tlsPersistentConnectionStatusEntry,
       "tlsPersistentConnectionStatusIndex": tlsPersistentConnectionStatusIndex,
       "tlsPersistentConnectionStatusGateway": tlsPersistentConnectionStatusGateway,
       "tlsPersistentConnectionStatusLocalPort": tlsPersistentConnectionStatusLocalPort,
       "tlsPersistentConnectionStatusRemoteHost": tlsPersistentConnectionStatusRemoteHost,
       "tlsPersistentConnectionStatusRemoteHostIpAddr": tlsPersistentConnectionStatusRemoteHostIpAddr,
       "tlsPersistentConnectionStatusState": tlsPersistentConnectionStatusState,
       "failoverGroup": failoverGroup,
       "defaultSipFailoverConditions": defaultSipFailoverConditions,
       "gwSpecificFailoverTable": gwSpecificFailoverTable,
       "gwSpecificFailoverEntry": gwSpecificFailoverEntry,
       "gwSpecificFailoverGatewayName": gwSpecificFailoverGatewayName,
       "gwSpecificFailoverEnableConfig": gwSpecificFailoverEnableConfig,
       "gwSpecificFailoverSipFailoverConditions": gwSpecificFailoverSipFailoverConditions,
       "penaltyBoxGroup": penaltyBoxGroup,
       "penaltyBoxEnable": penaltyBoxEnable,
       "penaltyBoxTime": penaltyBoxTime,
       "errorMappingGroup": errorMappingGroup,
       "errorMappingSipToCauseTable": errorMappingSipToCauseTable,
       "errorMappingSipToCauseEntry": errorMappingSipToCauseEntry,
       "errorMappingSipToCauseSipCode": errorMappingSipToCauseSipCode,
       "errorMappingSipToCauseCause": errorMappingSipToCauseCause,
       "errorMappingSipToCauseDelete": errorMappingSipToCauseDelete,
       "errorMappingCauseToSipTable": errorMappingCauseToSipTable,
       "errorMappingCauseToSipEntry": errorMappingCauseToSipEntry,
       "errorMappingCauseToSipCause": errorMappingCauseToSipCause,
       "errorMappingCauseToSipSipCode": errorMappingCauseToSipSipCode,
       "errorMappingCauseToSipDelete": errorMappingCauseToSipDelete,
       "reasonHeaderSupport": reasonHeaderSupport,
       "sipKeepAliveGroup": sipKeepAliveGroup,
       "sipKeepAliveMethod": sipKeepAliveMethod,
       "sipKeepAliveInterval": sipKeepAliveInterval,
       "sipKeepAliveRetry": sipKeepAliveRetry,
       "sipKeepAliveDestination": sipKeepAliveDestination,
       "gwKeepAliveAlternateDestinationTable": gwKeepAliveAlternateDestinationTable,
       "gwKeepAliveAlternateDestinationEntry": gwKeepAliveAlternateDestinationEntry,
       "gwKeepAliveAlternateDestinationGatewayName": gwKeepAliveAlternateDestinationGatewayName,
       "gwKeepAliveAlternateDestinationAlternateDestination": gwKeepAliveAlternateDestinationAlternateDestination,
       "prackGroup": prackGroup,
       "uasPrackSupport": uasPrackSupport,
       "uacPrackSupport": uacPrackSupport,
       "offerAnswerGroup": offerAnswerGroup,
       "answerCodecNegotiation": answerCodecNegotiation,
       "diversionGroup": diversionGroup,
       "diversionConfigTable": diversionConfigTable,
       "diversionConfigEntry": diversionConfigEntry,
       "diversionConfigGatewayName": diversionConfigGatewayName,
       "diversionConfigMethod": diversionConfigMethod,
       "dnsGroup": dnsGroup,
       "supportedDnsQueries": supportedDnsQueries,
       "dnsFailureConcealment": dnsFailureConcealment,
       "dnsIpVersion": dnsIpVersion,
       "messageWaitingIndication": messageWaitingIndication,
       "defaultStaticMessagingHost": defaultStaticMessagingHost,
       "defaultUsernameInRequestUriEnable": defaultUsernameInRequestUriEnable,
       "gwSpecificMwiTable": gwSpecificMwiTable,
       "gwSpecificMwiEntry": gwSpecificMwiEntry,
       "gwSpecificMwiGatewayName": gwSpecificMwiGatewayName,
       "gwSpecificMwiEnableConfig": gwSpecificMwiEnableConfig,
       "gwSpecificMwiMessagingHost": gwSpecificMwiMessagingHost,
       "gwSpecificMwiUsernameInRequestUriEnable": gwSpecificMwiUsernameInRequestUriEnable,
       "mwiStatusTable": mwiStatusTable,
       "mwiStatusEntry": mwiStatusEntry,
       "mwiStatusIndex": mwiStatusIndex,
       "mwiStatusGatewayName": mwiStatusGatewayName,
       "mwiStatusSubscriptionState": mwiStatusSubscriptionState,
       "mwiStatusEndpoint": mwiStatusEndpoint,
       "mwiStatusMessagingHost": mwiStatusMessagingHost,
       "mwiStatusUsername": mwiStatusUsername,
       "conferenceGroup": conferenceGroup,
       "defaultStaticConferenceServerUri": defaultStaticConferenceServerUri,
       "gwSpecificConferenceTable": gwSpecificConferenceTable,
       "gwSpecificConferenceEntry": gwSpecificConferenceEntry,
       "gwSpecificConferenceGatewayName": gwSpecificConferenceGatewayName,
       "gwSpecificConferenceEnableConfig": gwSpecificConferenceEnableConfig,
       "gwSpecificConferenceServerUri": gwSpecificConferenceServerUri,
       "priorityGroup": priorityGroup,
       "defaultOutboundPriorityCallRouting": defaultOutboundPriorityCallRouting,
       "eventHandlingGroup": eventHandlingGroup,
       "gwEventHandlingTable": gwEventHandlingTable,
       "gwEventHandlingEntry": gwEventHandlingEntry,
       "gwEventHandlingGatewayName": gwEventHandlingGatewayName,
       "gwEventHandlingReboot": gwEventHandlingReboot,
       "gwEventHandlingCheckSync": gwEventHandlingCheckSync,
       "sipMessageSupport": sipMessageSupport,
       "transferGroup": transferGroup,
       "referredByHeader": referredByHeader,
       "blindTransferMethod": blindTransferMethod,
       "referToHeaderUriSource": referToHeaderUriSource,
       "aocGroup": aocGroup,
       "aocConfigTable": aocConfigTable,
       "aocConfigEntry": aocConfigEntry,
       "aocConfigGatewayName": aocConfigGatewayName,
       "aocConfigAocDSupport": aocConfigAocDSupport,
       "aocConfigAocESupport": aocConfigAocESupport,
       "kpmlGroup": kpmlGroup,
       "uasKpmlSupport": uasKpmlSupport,
       "securityAgreementGroup": securityAgreementGroup,
       "mediaSecurityAgreementEnable": mediaSecurityAgreementEnable,
       "privacyHeadersGroup": privacyHeadersGroup,
       "privacyHeadersInResponse": privacyHeadersInResponse,
       "rtcpXrGroup": rtcpXrGroup,
       "defaultStaticRtcpXrCollectorUri": defaultStaticRtcpXrCollectorUri,
       "defaultRtcpXrPeriodicReportsInterval": defaultRtcpXrPeriodicReportsInterval,
       "gwSpecificRtcpXrTable": gwSpecificRtcpXrTable,
       "gwSpecificRtcpXrEntry": gwSpecificRtcpXrEntry,
       "gwSpecificRtcpXrGatewayName": gwSpecificRtcpXrGatewayName,
       "gwSpecificRtcpXrEnableConfig": gwSpecificRtcpXrEnableConfig,
       "gwSpecificRtcpXrCollectorUri": gwSpecificRtcpXrCollectorUri,
       "gwSpecificRtcpXrPeriodicReportsInterval": gwSpecificRtcpXrPeriodicReportsInterval,
       "interopGroup": interopGroup,
       "interopTransmissionTimeout": interopTransmissionTimeout,
       "interopTcpConnectTimeout": interopTcpConnectTimeout,
       "interopSymmetricUdpSourcePortEnable": interopSymmetricUdpSourcePortEnable,
       "interopMaxForwardsValue": interopMaxForwardsValue,
       "interopSendUaHeaderEnable": interopSendUaHeaderEnable,
       "interopSdpDirectionAttributeEnable": interopSdpDirectionAttributeEnable,
       "interopSdpDetectPeerDirectionAttributeSupportEnable": interopSdpDetectPeerDirectionAttributeSupportEnable,
       "interopOnHoldSdpConnectionAddress": interopOnHoldSdpConnectionAddress,
       "interopOnHoldSdpStreamDirection": interopOnHoldSdpStreamDirection,
       "interopOnHoldAnswerSdpStreamDirection": interopOnHoldAnswerSdpStreamDirection,
       "interopSdpDirectionAttributeLevel": interopSdpDirectionAttributeLevel,
       "interopLocalRingOnProvisionalResponse": interopLocalRingOnProvisionalResponse,
       "interopSdpOriginLineSessionIdAndVersionMaxLength": interopSdpOriginLineSessionIdAndVersionMaxLength,
       "interopLockDnsSrvRecordPerCallEnable": interopLockDnsSrvRecordPerCallEnable,
       "interopRejectCodeForUnsupportedSdpOffer": interopRejectCodeForUnsupportedSdpOffer,
       "interopUseDtmfPayloadTypeFoundInAnswer": interopUseDtmfPayloadTypeFoundInAnswer,
       "interopRegisterHomeDomainOverride": interopRegisterHomeDomainOverride,
       "interopEnforceOfferAnswerModel": interopEnforceOfferAnswerModel,
       "interopMapPlusToTonInternational": interopMapPlusToTonInternational,
       "interopAllowLessMediaInResponse": interopAllowLessMediaInResponse,
       "interopDefaultUsernameValue": interopDefaultUsernameValue,
       "interopCallWaitingSipInfoPrivateNumberCriteria": interopCallWaitingSipInfoPrivateNumberCriteria,
       "interopSdpT38ParametersEncoding": interopSdpT38ParametersEncoding,
       "interopReInviteForVoiceOn606NotAcceptable": interopReInviteForVoiceOn606NotAcceptable,
       "interopAllowMultipleActiveMediaInAnswer": interopAllowMultipleActiveMediaInAnswer,
       "interopIgnoreSipOptionsOnNoUsuableEndpoints": interopIgnoreSipOptionsOnNoUsuableEndpoints,
       "interopSipOptionsMethodSupport": interopSipOptionsMethodSupport,
       "interopAllowMediaReactivationInAnswer": interopAllowMediaReactivationInAnswer,
       "interopAllowAudioAndImageNegotiation": interopAllowAudioAndImageNegotiation,
       "interopEscapePoundInSipUriUsername": interopEscapePoundInSipUriUsername,
       "interopSiemensTransportHeaderEnable": interopSiemensTransportHeaderEnable,
       "interopTlsClientAuthenticationEnable": interopTlsClientAuthenticationEnable,
       "interopTlsCertificateValidation": interopTlsCertificateValidation,
       "interopIgnorePlusInUsername": interopIgnorePlusInUsername,
       "behaviorOnT38InviteNotAcceptedTable": behaviorOnT38InviteNotAcceptedTable,
       "behaviorOnT38InviteNotAcceptedEntry": behaviorOnT38InviteNotAcceptedEntry,
       "behaviorOnT38InviteNotAcceptedSipErrorCode": behaviorOnT38InviteNotAcceptedSipErrorCode,
       "behaviorOnT38InviteNotAcceptedBehavior": behaviorOnT38InviteNotAcceptedBehavior,
       "interopBehaviorOnMachineDetection": interopBehaviorOnMachineDetection,
       "interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice": interopCodecVsBearerCapabilitiesMappingPreferredCodecChoice,
       "interopSipUriUserParameterValue": interopSipUriUserParameterValue,
       "interopListenForEarlyRtpEnable": interopListenForEarlyRtpEnable,
       "interopRegistrationContactMatching": interopRegistrationContactMatching,
       "interopResolveRouteHeaderEnable": interopResolveRouteHeaderEnable,
       "interopForceDnsNaptrInTls": interopForceDnsNaptrInTls,
       "interopAckBranchMatching": interopAckBranchMatching,
       "interopIgnoreRequireHeaderEnable": interopIgnoreRequireHeaderEnable,
       "interopUaHeaderFormat": interopUaHeaderFormat,
       "interopSipInfoWithoutContentAnswer": interopSipInfoWithoutContentAnswer,
       "interopRegistrationDelayValue": interopRegistrationDelayValue,
       "interopUnsupportedContentType": interopUnsupportedContentType,
       "interopWaitConfirmedDialogForBlindTransfer": interopWaitConfirmedDialogForBlindTransfer,
       "interopPendingBlindTransferTimeout": interopPendingBlindTransferTimeout,
       "interopForkedProvisionalResponsesBehavior": interopForkedProvisionalResponsesBehavior,
       "interopReliableForkedProvisionalResponsesBehavior": interopReliableForkedProvisionalResponsesBehavior,
       "interopSipContactDisplayNamePresence": interopSipContactDisplayNamePresence,
       "interopEscapeFormat": interopEscapeFormat,
       "interopKeepAliveOptionFormat": interopKeepAliveOptionFormat,
       "interopInfoDtmfRelayFlashEvent": interopInfoDtmfRelayFlashEvent,
       "interopSdpPTimeAttribute": interopSdpPTimeAttribute,
       "interopSdpPTimeAttributeValue": interopSdpPTimeAttributeValue,
       "interopIncrementSdpVersionWhenModified": interopIncrementSdpVersionWhenModified,
       "interopActivateEarlyMediaOnProvisionalResponseAck": interopActivateEarlyMediaOnProvisionalResponseAck,
       "interopSend183WithSdpBefore180WithoutSdp": interopSend183WithSdpBefore180WithoutSdp,
       "interopCollectCallProprietaryHeader": interopCollectCallProprietaryHeader,
       "interopDtmfGroup": interopDtmfGroup,
       "interopDtmfTransportMethod": interopDtmfTransportMethod,
       "interopDtmfTransportDuration": interopDtmfTransportDuration,
       "monitoringGroup": monitoringGroup,
       "sipNotificationsGateway": sipNotificationsGateway,
       "maxNotificationsPerNotify": maxNotificationsPerNotify,
       "debugGroup": debugGroup,
       "debugSignalingLogEnable": debugSignalingLogEnable,
       "debugSignalingLogHost": debugSignalingLogHost,
       "debugContextSnapshotTime": debugContextSnapshotTime,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
