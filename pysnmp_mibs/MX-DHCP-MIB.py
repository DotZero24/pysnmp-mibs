# SNMP MIB module (MX-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:29 2025
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

dhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpMIBObjects_ObjectIdentity = ObjectIdentity
dhcpMIBObjects = _DhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1)
)
_SubnetsTable_Object = MibTable
subnetsTable = _SubnetsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100)
)
if mibBuilder.loadTexts:
    subnetsTable.setStatus("current")
_SubnetsEntry_Object = MibTableRow
subnetsEntry = _SubnetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1)
)
subnetsEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "subnetsNetworkInterfaceName"),
)
if mibBuilder.loadTexts:
    subnetsEntry.setStatus("current")
_SubnetsNetworkInterfaceName_Type = OctetString
_SubnetsNetworkInterfaceName_Object = MibTableColumn
subnetsNetworkInterfaceName = _SubnetsNetworkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 100),
    _SubnetsNetworkInterfaceName_Type()
)
subnetsNetworkInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetsNetworkInterfaceName.setStatus("current")


class _SubnetsEnableSubnet_Type(MxEnableState):
    """Custom type subnetsEnableSubnet based on MxEnableState"""
    defaultValue = 0


_SubnetsEnableSubnet_Type.__name__ = "MxEnableState"
_SubnetsEnableSubnet_Object = MibTableColumn
subnetsEnableSubnet = _SubnetsEnableSubnet_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 200),
    _SubnetsEnableSubnet_Type()
)
subnetsEnableSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetsEnableSubnet.setStatus("current")


class _SubnetsStartAddress_Type(MxIpAddr):
    """Custom type subnetsStartAddress based on MxIpAddr"""
    defaultValue = OctetString("")


_SubnetsStartAddress_Type.__name__ = "MxIpAddr"
_SubnetsStartAddress_Object = MibTableColumn
subnetsStartAddress = _SubnetsStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 300),
    _SubnetsStartAddress_Type()
)
subnetsStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetsStartAddress.setStatus("current")


class _SubnetsEndAddress_Type(MxIpAddr):
    """Custom type subnetsEndAddress based on MxIpAddr"""
    defaultValue = OctetString("")


_SubnetsEndAddress_Type.__name__ = "MxIpAddr"
_SubnetsEndAddress_Object = MibTableColumn
subnetsEndAddress = _SubnetsEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 400),
    _SubnetsEndAddress_Type()
)
subnetsEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetsEndAddress.setStatus("current")


class _SubnetsAutomaticConfigurationInterface_Type(OctetString):
    """Custom type subnetsAutomaticConfigurationInterface based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SubnetsAutomaticConfigurationInterface_Type.__name__ = "OctetString"
_SubnetsAutomaticConfigurationInterface_Object = MibTableColumn
subnetsAutomaticConfigurationInterface = _SubnetsAutomaticConfigurationInterface_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 450),
    _SubnetsAutomaticConfigurationInterface_Type()
)
subnetsAutomaticConfigurationInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetsAutomaticConfigurationInterface.setStatus("current")


class _SubnetsConfigStatus_Type(Integer32):
    """Custom type subnetsConfigStatus based on Integer32"""
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
          ("invalidConfig", 200),
          ("ok", 300))
    )


_SubnetsConfigStatus_Type.__name__ = "Integer32"
_SubnetsConfigStatus_Object = MibTableColumn
subnetsConfigStatus = _SubnetsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 500),
    _SubnetsConfigStatus_Type()
)
subnetsConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetsConfigStatus.setStatus("current")


class _SubnetsDelete_Type(Integer32):
    """Custom type subnetsDelete based on Integer32"""
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


_SubnetsDelete_Type.__name__ = "Integer32"
_SubnetsDelete_Object = MibTableColumn
subnetsDelete = _SubnetsDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 100, 1, 600),
    _SubnetsDelete_Type()
)
subnetsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetsDelete.setStatus("current")
_DomainNameGroup_ObjectIdentity = ObjectIdentity
domainNameGroup = _DomainNameGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200)
)


class _DefaultDomainNameConfigSource_Type(Integer32):
    """Custom type defaultDomainNameConfigSource based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              400)
        )
    )
    namedValues = NamedValues(
        *(("hostConfiguration", 200),
          ("static", 400))
    )


_DefaultDomainNameConfigSource_Type.__name__ = "Integer32"
_DefaultDomainNameConfigSource_Object = MibScalar
defaultDomainNameConfigSource = _DefaultDomainNameConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 100),
    _DefaultDomainNameConfigSource_Type()
)
defaultDomainNameConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDomainNameConfigSource.setStatus("current")


class _DefaultStaticDomainName_Type(MxIpHostName):
    """Custom type defaultStaticDomainName based on MxIpHostName"""
    defaultValue = OctetString("")


_DefaultStaticDomainName_Type.__name__ = "MxIpHostName"
_DefaultStaticDomainName_Object = MibScalar
defaultStaticDomainName = _DefaultStaticDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 200),
    _DefaultStaticDomainName_Type()
)
defaultStaticDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticDomainName.setStatus("current")
_SpecificDomainNamesTable_Object = MibTable
specificDomainNamesTable = _SpecificDomainNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300)
)
if mibBuilder.loadTexts:
    specificDomainNamesTable.setStatus("current")
_SpecificDomainNamesEntry_Object = MibTableRow
specificDomainNamesEntry = _SpecificDomainNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300, 1)
)
specificDomainNamesEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificDomainNamesSubnetName"),
)
if mibBuilder.loadTexts:
    specificDomainNamesEntry.setStatus("current")
_SpecificDomainNamesSubnetName_Type = OctetString
_SpecificDomainNamesSubnetName_Object = MibTableColumn
specificDomainNamesSubnetName = _SpecificDomainNamesSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300, 1, 100),
    _SpecificDomainNamesSubnetName_Type()
)
specificDomainNamesSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificDomainNamesSubnetName.setStatus("current")


class _SpecificDomainNamesEnableConfig_Type(MxEnableState):
    """Custom type specificDomainNamesEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificDomainNamesEnableConfig_Type.__name__ = "MxEnableState"
_SpecificDomainNamesEnableConfig_Object = MibTableColumn
specificDomainNamesEnableConfig = _SpecificDomainNamesEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300, 1, 200),
    _SpecificDomainNamesEnableConfig_Type()
)
specificDomainNamesEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDomainNamesEnableConfig.setStatus("current")


class _SpecificDomainNamesEnableOption_Type(MxEnableState):
    """Custom type specificDomainNamesEnableOption based on MxEnableState"""
    defaultValue = 0


_SpecificDomainNamesEnableOption_Type.__name__ = "MxEnableState"
_SpecificDomainNamesEnableOption_Object = MibTableColumn
specificDomainNamesEnableOption = _SpecificDomainNamesEnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300, 1, 300),
    _SpecificDomainNamesEnableOption_Type()
)
specificDomainNamesEnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDomainNamesEnableOption.setStatus("current")


class _SpecificDomainNamesConfigSource_Type(Integer32):
    """Custom type specificDomainNamesConfigSource based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              400)
        )
    )
    namedValues = NamedValues(
        *(("hostConfiguration", 200),
          ("static", 400))
    )


_SpecificDomainNamesConfigSource_Type.__name__ = "Integer32"
_SpecificDomainNamesConfigSource_Object = MibTableColumn
specificDomainNamesConfigSource = _SpecificDomainNamesConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300, 1, 400),
    _SpecificDomainNamesConfigSource_Type()
)
specificDomainNamesConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDomainNamesConfigSource.setStatus("current")


class _SpecificDomainNamesStaticName_Type(MxIpHostName):
    """Custom type specificDomainNamesStaticName based on MxIpHostName"""
    defaultValue = OctetString("")


_SpecificDomainNamesStaticName_Type.__name__ = "MxIpHostName"
_SpecificDomainNamesStaticName_Object = MibTableColumn
specificDomainNamesStaticName = _SpecificDomainNamesStaticName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 300, 1, 500),
    _SpecificDomainNamesStaticName_Type()
)
specificDomainNamesStaticName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDomainNamesStaticName.setStatus("current")
_DomainNamesInfoTable_Object = MibTable
domainNamesInfoTable = _DomainNamesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 400)
)
if mibBuilder.loadTexts:
    domainNamesInfoTable.setStatus("current")
_DomainNamesInfoEntry_Object = MibTableRow
domainNamesInfoEntry = _DomainNamesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 400, 1)
)
domainNamesInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "domainNamesInfoSubnetName"),
)
if mibBuilder.loadTexts:
    domainNamesInfoEntry.setStatus("current")
_DomainNamesInfoSubnetName_Type = OctetString
_DomainNamesInfoSubnetName_Object = MibTableColumn
domainNamesInfoSubnetName = _DomainNamesInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 400, 1, 100),
    _DomainNamesInfoSubnetName_Type()
)
domainNamesInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainNamesInfoSubnetName.setStatus("current")
_DomainNamesInfoDomainName_Type = OctetString
_DomainNamesInfoDomainName_Object = MibTableColumn
domainNamesInfoDomainName = _DomainNamesInfoDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 200, 400, 1, 200),
    _DomainNamesInfoDomainName_Type()
)
domainNamesInfoDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainNamesInfoDomainName.setStatus("current")
_LeaseTimeGroup_ObjectIdentity = ObjectIdentity
leaseTimeGroup = _LeaseTimeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300)
)


class _DefaultLeaseTime_Type(Unsigned32):
    """Custom type defaultLeaseTime based on Unsigned32"""
    defaultValue = 86400


_DefaultLeaseTime_Type.__name__ = "Unsigned32"
_DefaultLeaseTime_Object = MibScalar
defaultLeaseTime = _DefaultLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 100),
    _DefaultLeaseTime_Type()
)
defaultLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultLeaseTime.setStatus("current")
_SpecificLeaseTimesTable_Object = MibTable
specificLeaseTimesTable = _SpecificLeaseTimesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 200)
)
if mibBuilder.loadTexts:
    specificLeaseTimesTable.setStatus("current")
_SpecificLeaseTimesEntry_Object = MibTableRow
specificLeaseTimesEntry = _SpecificLeaseTimesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 200, 1)
)
specificLeaseTimesEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificLeaseTimesSubnetName"),
)
if mibBuilder.loadTexts:
    specificLeaseTimesEntry.setStatus("current")
_SpecificLeaseTimesSubnetName_Type = OctetString
_SpecificLeaseTimesSubnetName_Object = MibTableColumn
specificLeaseTimesSubnetName = _SpecificLeaseTimesSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 200, 1, 100),
    _SpecificLeaseTimesSubnetName_Type()
)
specificLeaseTimesSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificLeaseTimesSubnetName.setStatus("current")


class _SpecificLeaseTimesEnableConfig_Type(MxEnableState):
    """Custom type specificLeaseTimesEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificLeaseTimesEnableConfig_Type.__name__ = "MxEnableState"
_SpecificLeaseTimesEnableConfig_Object = MibTableColumn
specificLeaseTimesEnableConfig = _SpecificLeaseTimesEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 200, 1, 200),
    _SpecificLeaseTimesEnableConfig_Type()
)
specificLeaseTimesEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificLeaseTimesEnableConfig.setStatus("current")


class _SpecificLeaseTimesLeaseTime_Type(Unsigned32):
    """Custom type specificLeaseTimesLeaseTime based on Unsigned32"""
    defaultValue = 86400


_SpecificLeaseTimesLeaseTime_Type.__name__ = "Unsigned32"
_SpecificLeaseTimesLeaseTime_Object = MibTableColumn
specificLeaseTimesLeaseTime = _SpecificLeaseTimesLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 200, 1, 300),
    _SpecificLeaseTimesLeaseTime_Type()
)
specificLeaseTimesLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificLeaseTimesLeaseTime.setStatus("current")
_LeaseTimesInfoTable_Object = MibTable
leaseTimesInfoTable = _LeaseTimesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 300)
)
if mibBuilder.loadTexts:
    leaseTimesInfoTable.setStatus("current")
_LeaseTimesInfoEntry_Object = MibTableRow
leaseTimesInfoEntry = _LeaseTimesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 300, 1)
)
leaseTimesInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "leaseTimesInfoSubnetName"),
)
if mibBuilder.loadTexts:
    leaseTimesInfoEntry.setStatus("current")
_LeaseTimesInfoSubnetName_Type = OctetString
_LeaseTimesInfoSubnetName_Object = MibTableColumn
leaseTimesInfoSubnetName = _LeaseTimesInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 300, 1, 100),
    _LeaseTimesInfoSubnetName_Type()
)
leaseTimesInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaseTimesInfoSubnetName.setStatus("current")
_LeaseTimesInfoDefault_Type = Unsigned32
_LeaseTimesInfoDefault_Object = MibTableColumn
leaseTimesInfoDefault = _LeaseTimesInfoDefault_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 300, 300, 1, 200),
    _LeaseTimesInfoDefault_Type()
)
leaseTimesInfoDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leaseTimesInfoDefault.setStatus("current")
_DefaultRouterGroup_ObjectIdentity = ObjectIdentity
defaultRouterGroup = _DefaultRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400)
)
_SpecificDefaultRoutersTable_Object = MibTable
specificDefaultRoutersTable = _SpecificDefaultRoutersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 100)
)
if mibBuilder.loadTexts:
    specificDefaultRoutersTable.setStatus("current")
_SpecificDefaultRoutersEntry_Object = MibTableRow
specificDefaultRoutersEntry = _SpecificDefaultRoutersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 100, 1)
)
specificDefaultRoutersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificDefaultRoutersSubnetName"),
)
if mibBuilder.loadTexts:
    specificDefaultRoutersEntry.setStatus("current")
_SpecificDefaultRoutersSubnetName_Type = OctetString
_SpecificDefaultRoutersSubnetName_Object = MibTableColumn
specificDefaultRoutersSubnetName = _SpecificDefaultRoutersSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 100, 1, 100),
    _SpecificDefaultRoutersSubnetName_Type()
)
specificDefaultRoutersSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificDefaultRoutersSubnetName.setStatus("current")


class _SpecificDefaultRoutersEnableOption_Type(MxEnableState):
    """Custom type specificDefaultRoutersEnableOption based on MxEnableState"""
    defaultValue = 1


_SpecificDefaultRoutersEnableOption_Type.__name__ = "MxEnableState"
_SpecificDefaultRoutersEnableOption_Object = MibTableColumn
specificDefaultRoutersEnableOption = _SpecificDefaultRoutersEnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 100, 1, 200),
    _SpecificDefaultRoutersEnableOption_Type()
)
specificDefaultRoutersEnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDefaultRoutersEnableOption.setStatus("current")


class _SpecificDefaultRoutersConfigSource_Type(Integer32):
    """Custom type specificDefaultRoutersConfigSource based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              400)
        )
    )
    namedValues = NamedValues(
        *(("hostInterface", 100),
          ("static", 400))
    )


_SpecificDefaultRoutersConfigSource_Type.__name__ = "Integer32"
_SpecificDefaultRoutersConfigSource_Object = MibTableColumn
specificDefaultRoutersConfigSource = _SpecificDefaultRoutersConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 100, 1, 300),
    _SpecificDefaultRoutersConfigSource_Type()
)
specificDefaultRoutersConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDefaultRoutersConfigSource.setStatus("current")


class _SpecificDefaultRoutersStaticRouter_Type(MxIpAddr):
    """Custom type specificDefaultRoutersStaticRouter based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificDefaultRoutersStaticRouter_Type.__name__ = "MxIpAddr"
_SpecificDefaultRoutersStaticRouter_Object = MibTableColumn
specificDefaultRoutersStaticRouter = _SpecificDefaultRoutersStaticRouter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 100, 1, 400),
    _SpecificDefaultRoutersStaticRouter_Type()
)
specificDefaultRoutersStaticRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDefaultRoutersStaticRouter.setStatus("current")
_DefaultRoutersInfoTable_Object = MibTable
defaultRoutersInfoTable = _DefaultRoutersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 200)
)
if mibBuilder.loadTexts:
    defaultRoutersInfoTable.setStatus("current")
_DefaultRoutersInfoEntry_Object = MibTableRow
defaultRoutersInfoEntry = _DefaultRoutersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 200, 1)
)
defaultRoutersInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "defaultRoutersInfoSubnetName"),
)
if mibBuilder.loadTexts:
    defaultRoutersInfoEntry.setStatus("current")
_DefaultRoutersInfoSubnetName_Type = OctetString
_DefaultRoutersInfoSubnetName_Object = MibTableColumn
defaultRoutersInfoSubnetName = _DefaultRoutersInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 200, 1, 100),
    _DefaultRoutersInfoSubnetName_Type()
)
defaultRoutersInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultRoutersInfoSubnetName.setStatus("current")
_DefaultRoutersInfoDefaultRouter_Type = MxIpAddr
_DefaultRoutersInfoDefaultRouter_Object = MibTableColumn
defaultRoutersInfoDefaultRouter = _DefaultRoutersInfoDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 400, 200, 1, 200),
    _DefaultRoutersInfoDefaultRouter_Type()
)
defaultRoutersInfoDefaultRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultRoutersInfoDefaultRouter.setStatus("current")
_DnsServersGroup_ObjectIdentity = ObjectIdentity
dnsServersGroup = _DnsServersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500)
)


class _DefaultDnsServersConfigSource_Type(Integer32):
    """Custom type defaultDnsServersConfigSource based on Integer32"""
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
        *(("hostConfiguration", 200),
          ("automatic", 300),
          ("static", 400))
    )


_DefaultDnsServersConfigSource_Type.__name__ = "Integer32"
_DefaultDnsServersConfigSource_Object = MibScalar
defaultDnsServersConfigSource = _DefaultDnsServersConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 100),
    _DefaultDnsServersConfigSource_Type()
)
defaultDnsServersConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultDnsServersConfigSource.setStatus("current")
_DefaultStaticDnsServersTable_Object = MibTable
defaultStaticDnsServersTable = _DefaultStaticDnsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 200)
)
if mibBuilder.loadTexts:
    defaultStaticDnsServersTable.setStatus("current")
_DefaultStaticDnsServersEntry_Object = MibTableRow
defaultStaticDnsServersEntry = _DefaultStaticDnsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 200, 1)
)
defaultStaticDnsServersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "defaultStaticDnsServersPriority"),
)
if mibBuilder.loadTexts:
    defaultStaticDnsServersEntry.setStatus("current")


class _DefaultStaticDnsServersPriority_Type(Unsigned32):
    """Custom type defaultStaticDnsServersPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DefaultStaticDnsServersPriority_Type.__name__ = "Unsigned32"
_DefaultStaticDnsServersPriority_Object = MibTableColumn
defaultStaticDnsServersPriority = _DefaultStaticDnsServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 200, 1, 100),
    _DefaultStaticDnsServersPriority_Type()
)
defaultStaticDnsServersPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultStaticDnsServersPriority.setStatus("current")
_DefaultStaticDnsServersIpAddress_Type = MxIpAddr
_DefaultStaticDnsServersIpAddress_Object = MibTableColumn
defaultStaticDnsServersIpAddress = _DefaultStaticDnsServersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 200, 1, 200),
    _DefaultStaticDnsServersIpAddress_Type()
)
defaultStaticDnsServersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticDnsServersIpAddress.setStatus("current")
_SpecificDnsServersTable_Object = MibTable
specificDnsServersTable = _SpecificDnsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300)
)
if mibBuilder.loadTexts:
    specificDnsServersTable.setStatus("current")
_SpecificDnsServersEntry_Object = MibTableRow
specificDnsServersEntry = _SpecificDnsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1)
)
specificDnsServersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificDnsServersSubnetName"),
)
if mibBuilder.loadTexts:
    specificDnsServersEntry.setStatus("current")
_SpecificDnsServersSubnetName_Type = OctetString
_SpecificDnsServersSubnetName_Object = MibTableColumn
specificDnsServersSubnetName = _SpecificDnsServersSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 100),
    _SpecificDnsServersSubnetName_Type()
)
specificDnsServersSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificDnsServersSubnetName.setStatus("current")


class _SpecificDnsServersEnableConfig_Type(MxEnableState):
    """Custom type specificDnsServersEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificDnsServersEnableConfig_Type.__name__ = "MxEnableState"
_SpecificDnsServersEnableConfig_Object = MibTableColumn
specificDnsServersEnableConfig = _SpecificDnsServersEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 200),
    _SpecificDnsServersEnableConfig_Type()
)
specificDnsServersEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersEnableConfig.setStatus("current")


class _SpecificDnsServersEnableOption_Type(MxEnableState):
    """Custom type specificDnsServersEnableOption based on MxEnableState"""
    defaultValue = 1


_SpecificDnsServersEnableOption_Type.__name__ = "MxEnableState"
_SpecificDnsServersEnableOption_Object = MibTableColumn
specificDnsServersEnableOption = _SpecificDnsServersEnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 300),
    _SpecificDnsServersEnableOption_Type()
)
specificDnsServersEnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersEnableOption.setStatus("current")


class _SpecificDnsServersConfigSource_Type(Integer32):
    """Custom type specificDnsServersConfigSource based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("hostConfiguration", 200),
          ("automatic", 300),
          ("static", 400))
    )


_SpecificDnsServersConfigSource_Type.__name__ = "Integer32"
_SpecificDnsServersConfigSource_Object = MibTableColumn
specificDnsServersConfigSource = _SpecificDnsServersConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 400),
    _SpecificDnsServersConfigSource_Type()
)
specificDnsServersConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersConfigSource.setStatus("current")


class _SpecificDnsServersStaticDns1_Type(MxIpAddr):
    """Custom type specificDnsServersStaticDns1 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificDnsServersStaticDns1_Type.__name__ = "MxIpAddr"
_SpecificDnsServersStaticDns1_Object = MibTableColumn
specificDnsServersStaticDns1 = _SpecificDnsServersStaticDns1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 500),
    _SpecificDnsServersStaticDns1_Type()
)
specificDnsServersStaticDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersStaticDns1.setStatus("current")


class _SpecificDnsServersStaticDns2_Type(MxIpAddr):
    """Custom type specificDnsServersStaticDns2 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificDnsServersStaticDns2_Type.__name__ = "MxIpAddr"
_SpecificDnsServersStaticDns2_Object = MibTableColumn
specificDnsServersStaticDns2 = _SpecificDnsServersStaticDns2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 600),
    _SpecificDnsServersStaticDns2_Type()
)
specificDnsServersStaticDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersStaticDns2.setStatus("current")


class _SpecificDnsServersStaticDns3_Type(MxIpAddr):
    """Custom type specificDnsServersStaticDns3 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificDnsServersStaticDns3_Type.__name__ = "MxIpAddr"
_SpecificDnsServersStaticDns3_Object = MibTableColumn
specificDnsServersStaticDns3 = _SpecificDnsServersStaticDns3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 700),
    _SpecificDnsServersStaticDns3_Type()
)
specificDnsServersStaticDns3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersStaticDns3.setStatus("current")


class _SpecificDnsServersStaticDns4_Type(MxIpAddr):
    """Custom type specificDnsServersStaticDns4 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificDnsServersStaticDns4_Type.__name__ = "MxIpAddr"
_SpecificDnsServersStaticDns4_Object = MibTableColumn
specificDnsServersStaticDns4 = _SpecificDnsServersStaticDns4_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 300, 1, 800),
    _SpecificDnsServersStaticDns4_Type()
)
specificDnsServersStaticDns4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificDnsServersStaticDns4.setStatus("current")
_DnsServersInfoTable_Object = MibTable
dnsServersInfoTable = _DnsServersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400)
)
if mibBuilder.loadTexts:
    dnsServersInfoTable.setStatus("current")
_DnsServersInfoEntry_Object = MibTableRow
dnsServersInfoEntry = _DnsServersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400, 1)
)
dnsServersInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "dnsServersInfoSubnetName"),
)
if mibBuilder.loadTexts:
    dnsServersInfoEntry.setStatus("current")
_DnsServersInfoSubnetName_Type = OctetString
_DnsServersInfoSubnetName_Object = MibTableColumn
dnsServersInfoSubnetName = _DnsServersInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400, 1, 100),
    _DnsServersInfoSubnetName_Type()
)
dnsServersInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoSubnetName.setStatus("current")
_DnsServersInfoDns1_Type = MxIpAddr
_DnsServersInfoDns1_Object = MibTableColumn
dnsServersInfoDns1 = _DnsServersInfoDns1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400, 1, 200),
    _DnsServersInfoDns1_Type()
)
dnsServersInfoDns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoDns1.setStatus("current")
_DnsServersInfoDns2_Type = MxIpAddr
_DnsServersInfoDns2_Object = MibTableColumn
dnsServersInfoDns2 = _DnsServersInfoDns2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400, 1, 300),
    _DnsServersInfoDns2_Type()
)
dnsServersInfoDns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoDns2.setStatus("current")
_DnsServersInfoDns3_Type = MxIpAddr
_DnsServersInfoDns3_Object = MibTableColumn
dnsServersInfoDns3 = _DnsServersInfoDns3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400, 1, 400),
    _DnsServersInfoDns3_Type()
)
dnsServersInfoDns3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoDns3.setStatus("current")
_DnsServersInfoDns4_Type = MxIpAddr
_DnsServersInfoDns4_Object = MibTableColumn
dnsServersInfoDns4 = _DnsServersInfoDns4_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 500, 400, 1, 500),
    _DnsServersInfoDns4_Type()
)
dnsServersInfoDns4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServersInfoDns4.setStatus("current")
_NtpServersGroup_ObjectIdentity = ObjectIdentity
ntpServersGroup = _NtpServersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600)
)


class _DefaultNtpServersConfigSource_Type(Integer32):
    """Custom type defaultNtpServersConfigSource based on Integer32"""
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
        *(("hostConfiguration", 200),
          ("automatic", 300),
          ("static", 400))
    )


_DefaultNtpServersConfigSource_Type.__name__ = "Integer32"
_DefaultNtpServersConfigSource_Object = MibScalar
defaultNtpServersConfigSource = _DefaultNtpServersConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 100),
    _DefaultNtpServersConfigSource_Type()
)
defaultNtpServersConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultNtpServersConfigSource.setStatus("current")
_DefaultStaticNtpServersTable_Object = MibTable
defaultStaticNtpServersTable = _DefaultStaticNtpServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 200)
)
if mibBuilder.loadTexts:
    defaultStaticNtpServersTable.setStatus("current")
_DefaultStaticNtpServersEntry_Object = MibTableRow
defaultStaticNtpServersEntry = _DefaultStaticNtpServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 200, 1)
)
defaultStaticNtpServersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "defaultStaticNtpServersPriority"),
)
if mibBuilder.loadTexts:
    defaultStaticNtpServersEntry.setStatus("current")


class _DefaultStaticNtpServersPriority_Type(Unsigned32):
    """Custom type defaultStaticNtpServersPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DefaultStaticNtpServersPriority_Type.__name__ = "Unsigned32"
_DefaultStaticNtpServersPriority_Object = MibTableColumn
defaultStaticNtpServersPriority = _DefaultStaticNtpServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 200, 1, 100),
    _DefaultStaticNtpServersPriority_Type()
)
defaultStaticNtpServersPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultStaticNtpServersPriority.setStatus("current")
_DefaultStaticNtpServersIpAddress_Type = MxIpAddr
_DefaultStaticNtpServersIpAddress_Object = MibTableColumn
defaultStaticNtpServersIpAddress = _DefaultStaticNtpServersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 200, 1, 200),
    _DefaultStaticNtpServersIpAddress_Type()
)
defaultStaticNtpServersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticNtpServersIpAddress.setStatus("current")
_SpecificNtpServersTable_Object = MibTable
specificNtpServersTable = _SpecificNtpServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300)
)
if mibBuilder.loadTexts:
    specificNtpServersTable.setStatus("current")
_SpecificNtpServersEntry_Object = MibTableRow
specificNtpServersEntry = _SpecificNtpServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1)
)
specificNtpServersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificNtpServersSubnetName"),
)
if mibBuilder.loadTexts:
    specificNtpServersEntry.setStatus("current")
_SpecificNtpServersSubnetName_Type = OctetString
_SpecificNtpServersSubnetName_Object = MibTableColumn
specificNtpServersSubnetName = _SpecificNtpServersSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 100),
    _SpecificNtpServersSubnetName_Type()
)
specificNtpServersSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificNtpServersSubnetName.setStatus("current")


class _SpecificNtpServersEnableConfig_Type(MxEnableState):
    """Custom type specificNtpServersEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificNtpServersEnableConfig_Type.__name__ = "MxEnableState"
_SpecificNtpServersEnableConfig_Object = MibTableColumn
specificNtpServersEnableConfig = _SpecificNtpServersEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 200),
    _SpecificNtpServersEnableConfig_Type()
)
specificNtpServersEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersEnableConfig.setStatus("current")


class _SpecificNtpServersEnableOption_Type(MxEnableState):
    """Custom type specificNtpServersEnableOption based on MxEnableState"""
    defaultValue = 0


_SpecificNtpServersEnableOption_Type.__name__ = "MxEnableState"
_SpecificNtpServersEnableOption_Object = MibTableColumn
specificNtpServersEnableOption = _SpecificNtpServersEnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 300),
    _SpecificNtpServersEnableOption_Type()
)
specificNtpServersEnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersEnableOption.setStatus("current")


class _SpecificNtpServersConfigSource_Type(Integer32):
    """Custom type specificNtpServersConfigSource based on Integer32"""
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
        *(("hostConfiguration", 200),
          ("automatic", 300),
          ("static", 400))
    )


_SpecificNtpServersConfigSource_Type.__name__ = "Integer32"
_SpecificNtpServersConfigSource_Object = MibTableColumn
specificNtpServersConfigSource = _SpecificNtpServersConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 400),
    _SpecificNtpServersConfigSource_Type()
)
specificNtpServersConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersConfigSource.setStatus("current")


class _SpecificNtpServersStaticNtp1_Type(MxIpAddr):
    """Custom type specificNtpServersStaticNtp1 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNtpServersStaticNtp1_Type.__name__ = "MxIpAddr"
_SpecificNtpServersStaticNtp1_Object = MibTableColumn
specificNtpServersStaticNtp1 = _SpecificNtpServersStaticNtp1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 500),
    _SpecificNtpServersStaticNtp1_Type()
)
specificNtpServersStaticNtp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersStaticNtp1.setStatus("current")


class _SpecificNtpServersStaticNtp2_Type(MxIpAddr):
    """Custom type specificNtpServersStaticNtp2 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNtpServersStaticNtp2_Type.__name__ = "MxIpAddr"
_SpecificNtpServersStaticNtp2_Object = MibTableColumn
specificNtpServersStaticNtp2 = _SpecificNtpServersStaticNtp2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 600),
    _SpecificNtpServersStaticNtp2_Type()
)
specificNtpServersStaticNtp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersStaticNtp2.setStatus("current")


class _SpecificNtpServersStaticNtp3_Type(MxIpAddr):
    """Custom type specificNtpServersStaticNtp3 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNtpServersStaticNtp3_Type.__name__ = "MxIpAddr"
_SpecificNtpServersStaticNtp3_Object = MibTableColumn
specificNtpServersStaticNtp3 = _SpecificNtpServersStaticNtp3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 700),
    _SpecificNtpServersStaticNtp3_Type()
)
specificNtpServersStaticNtp3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersStaticNtp3.setStatus("current")


class _SpecificNtpServersStaticNtp4_Type(MxIpAddr):
    """Custom type specificNtpServersStaticNtp4 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNtpServersStaticNtp4_Type.__name__ = "MxIpAddr"
_SpecificNtpServersStaticNtp4_Object = MibTableColumn
specificNtpServersStaticNtp4 = _SpecificNtpServersStaticNtp4_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 300, 1, 800),
    _SpecificNtpServersStaticNtp4_Type()
)
specificNtpServersStaticNtp4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNtpServersStaticNtp4.setStatus("current")
_NtpServersInfoTable_Object = MibTable
ntpServersInfoTable = _NtpServersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400)
)
if mibBuilder.loadTexts:
    ntpServersInfoTable.setStatus("current")
_NtpServersInfoEntry_Object = MibTableRow
ntpServersInfoEntry = _NtpServersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400, 1)
)
ntpServersInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "ntpServersInfoSubnetName"),
)
if mibBuilder.loadTexts:
    ntpServersInfoEntry.setStatus("current")
_NtpServersInfoSubnetName_Type = OctetString
_NtpServersInfoSubnetName_Object = MibTableColumn
ntpServersInfoSubnetName = _NtpServersInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400, 1, 100),
    _NtpServersInfoSubnetName_Type()
)
ntpServersInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServersInfoSubnetName.setStatus("current")
_NtpServersInfoNtp1_Type = MxIpAddr
_NtpServersInfoNtp1_Object = MibTableColumn
ntpServersInfoNtp1 = _NtpServersInfoNtp1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400, 1, 200),
    _NtpServersInfoNtp1_Type()
)
ntpServersInfoNtp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServersInfoNtp1.setStatus("current")
_NtpServersInfoNtp2_Type = MxIpAddr
_NtpServersInfoNtp2_Object = MibTableColumn
ntpServersInfoNtp2 = _NtpServersInfoNtp2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400, 1, 300),
    _NtpServersInfoNtp2_Type()
)
ntpServersInfoNtp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServersInfoNtp2.setStatus("current")
_NtpServersInfoNtp3_Type = MxIpAddr
_NtpServersInfoNtp3_Object = MibTableColumn
ntpServersInfoNtp3 = _NtpServersInfoNtp3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400, 1, 400),
    _NtpServersInfoNtp3_Type()
)
ntpServersInfoNtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServersInfoNtp3.setStatus("current")
_NtpServersInfoNtp4_Type = MxIpAddr
_NtpServersInfoNtp4_Object = MibTableColumn
ntpServersInfoNtp4 = _NtpServersInfoNtp4_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 600, 400, 1, 500),
    _NtpServersInfoNtp4_Type()
)
ntpServersInfoNtp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServersInfoNtp4.setStatus("current")
_NbnsServersGroup_ObjectIdentity = ObjectIdentity
nbnsServersGroup = _NbnsServersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700)
)
_DefaultStaticNbnsServersTable_Object = MibTable
defaultStaticNbnsServersTable = _DefaultStaticNbnsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 100)
)
if mibBuilder.loadTexts:
    defaultStaticNbnsServersTable.setStatus("current")
_DefaultStaticNbnsServersEntry_Object = MibTableRow
defaultStaticNbnsServersEntry = _DefaultStaticNbnsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 100, 1)
)
defaultStaticNbnsServersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "defaultStaticNbnsServersPriority"),
)
if mibBuilder.loadTexts:
    defaultStaticNbnsServersEntry.setStatus("current")


class _DefaultStaticNbnsServersPriority_Type(Unsigned32):
    """Custom type defaultStaticNbnsServersPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DefaultStaticNbnsServersPriority_Type.__name__ = "Unsigned32"
_DefaultStaticNbnsServersPriority_Object = MibTableColumn
defaultStaticNbnsServersPriority = _DefaultStaticNbnsServersPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 100, 1, 100),
    _DefaultStaticNbnsServersPriority_Type()
)
defaultStaticNbnsServersPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultStaticNbnsServersPriority.setStatus("current")
_DefaultStaticNbnsServersIpAddress_Type = MxIpAddr
_DefaultStaticNbnsServersIpAddress_Object = MibTableColumn
defaultStaticNbnsServersIpAddress = _DefaultStaticNbnsServersIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 100, 1, 200),
    _DefaultStaticNbnsServersIpAddress_Type()
)
defaultStaticNbnsServersIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticNbnsServersIpAddress.setStatus("current")
_SpecificNbnsServersTable_Object = MibTable
specificNbnsServersTable = _SpecificNbnsServersTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200)
)
if mibBuilder.loadTexts:
    specificNbnsServersTable.setStatus("current")
_SpecificNbnsServersEntry_Object = MibTableRow
specificNbnsServersEntry = _SpecificNbnsServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1)
)
specificNbnsServersEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificNbnsServersSubnetName"),
)
if mibBuilder.loadTexts:
    specificNbnsServersEntry.setStatus("current")
_SpecificNbnsServersSubnetName_Type = OctetString
_SpecificNbnsServersSubnetName_Object = MibTableColumn
specificNbnsServersSubnetName = _SpecificNbnsServersSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 100),
    _SpecificNbnsServersSubnetName_Type()
)
specificNbnsServersSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificNbnsServersSubnetName.setStatus("current")


class _SpecificNbnsServersEnableConfig_Type(MxEnableState):
    """Custom type specificNbnsServersEnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificNbnsServersEnableConfig_Type.__name__ = "MxEnableState"
_SpecificNbnsServersEnableConfig_Object = MibTableColumn
specificNbnsServersEnableConfig = _SpecificNbnsServersEnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 200),
    _SpecificNbnsServersEnableConfig_Type()
)
specificNbnsServersEnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNbnsServersEnableConfig.setStatus("current")


class _SpecificNbnsServersEnableOption_Type(MxEnableState):
    """Custom type specificNbnsServersEnableOption based on MxEnableState"""
    defaultValue = 0


_SpecificNbnsServersEnableOption_Type.__name__ = "MxEnableState"
_SpecificNbnsServersEnableOption_Object = MibTableColumn
specificNbnsServersEnableOption = _SpecificNbnsServersEnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 300),
    _SpecificNbnsServersEnableOption_Type()
)
specificNbnsServersEnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNbnsServersEnableOption.setStatus("current")


class _SpecificNbnsServersStaticNbns1_Type(MxIpAddr):
    """Custom type specificNbnsServersStaticNbns1 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNbnsServersStaticNbns1_Type.__name__ = "MxIpAddr"
_SpecificNbnsServersStaticNbns1_Object = MibTableColumn
specificNbnsServersStaticNbns1 = _SpecificNbnsServersStaticNbns1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 400),
    _SpecificNbnsServersStaticNbns1_Type()
)
specificNbnsServersStaticNbns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNbnsServersStaticNbns1.setStatus("current")


class _SpecificNbnsServersStaticNbns2_Type(MxIpAddr):
    """Custom type specificNbnsServersStaticNbns2 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNbnsServersStaticNbns2_Type.__name__ = "MxIpAddr"
_SpecificNbnsServersStaticNbns2_Object = MibTableColumn
specificNbnsServersStaticNbns2 = _SpecificNbnsServersStaticNbns2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 500),
    _SpecificNbnsServersStaticNbns2_Type()
)
specificNbnsServersStaticNbns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNbnsServersStaticNbns2.setStatus("current")


class _SpecificNbnsServersStaticNbns3_Type(MxIpAddr):
    """Custom type specificNbnsServersStaticNbns3 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNbnsServersStaticNbns3_Type.__name__ = "MxIpAddr"
_SpecificNbnsServersStaticNbns3_Object = MibTableColumn
specificNbnsServersStaticNbns3 = _SpecificNbnsServersStaticNbns3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 600),
    _SpecificNbnsServersStaticNbns3_Type()
)
specificNbnsServersStaticNbns3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNbnsServersStaticNbns3.setStatus("current")


class _SpecificNbnsServersStaticNbns4_Type(MxIpAddr):
    """Custom type specificNbnsServersStaticNbns4 based on MxIpAddr"""
    defaultValue = OctetString("")


_SpecificNbnsServersStaticNbns4_Type.__name__ = "MxIpAddr"
_SpecificNbnsServersStaticNbns4_Object = MibTableColumn
specificNbnsServersStaticNbns4 = _SpecificNbnsServersStaticNbns4_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 200, 1, 700),
    _SpecificNbnsServersStaticNbns4_Type()
)
specificNbnsServersStaticNbns4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificNbnsServersStaticNbns4.setStatus("current")
_NbnsServersInfoTable_Object = MibTable
nbnsServersInfoTable = _NbnsServersInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300)
)
if mibBuilder.loadTexts:
    nbnsServersInfoTable.setStatus("current")
_NbnsServersInfoEntry_Object = MibTableRow
nbnsServersInfoEntry = _NbnsServersInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300, 1)
)
nbnsServersInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "nbnsServersInfoSubnetName"),
)
if mibBuilder.loadTexts:
    nbnsServersInfoEntry.setStatus("current")
_NbnsServersInfoSubnetName_Type = OctetString
_NbnsServersInfoSubnetName_Object = MibTableColumn
nbnsServersInfoSubnetName = _NbnsServersInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300, 1, 100),
    _NbnsServersInfoSubnetName_Type()
)
nbnsServersInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbnsServersInfoSubnetName.setStatus("current")
_NbnsServersInfoNbns1_Type = MxIpAddr
_NbnsServersInfoNbns1_Object = MibTableColumn
nbnsServersInfoNbns1 = _NbnsServersInfoNbns1_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300, 1, 200),
    _NbnsServersInfoNbns1_Type()
)
nbnsServersInfoNbns1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbnsServersInfoNbns1.setStatus("current")
_NbnsServersInfoNbns2_Type = MxIpAddr
_NbnsServersInfoNbns2_Object = MibTableColumn
nbnsServersInfoNbns2 = _NbnsServersInfoNbns2_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300, 1, 300),
    _NbnsServersInfoNbns2_Type()
)
nbnsServersInfoNbns2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbnsServersInfoNbns2.setStatus("current")
_NbnsServersInfoNbns3_Type = MxIpAddr
_NbnsServersInfoNbns3_Object = MibTableColumn
nbnsServersInfoNbns3 = _NbnsServersInfoNbns3_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300, 1, 400),
    _NbnsServersInfoNbns3_Type()
)
nbnsServersInfoNbns3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbnsServersInfoNbns3.setStatus("current")
_NbnsServersInfoNbns4_Type = MxIpAddr
_NbnsServersInfoNbns4_Object = MibTableColumn
nbnsServersInfoNbns4 = _NbnsServersInfoNbns4_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 700, 300, 1, 500),
    _NbnsServersInfoNbns4_Type()
)
nbnsServersInfoNbns4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbnsServersInfoNbns4.setStatus("current")
_StaticLeasesTable_Object = MibTable
staticLeasesTable = _StaticLeasesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 800)
)
if mibBuilder.loadTexts:
    staticLeasesTable.setStatus("current")
_StaticLeasesEntry_Object = MibTableRow
staticLeasesEntry = _StaticLeasesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 800, 1)
)
staticLeasesEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "staticLeasesMacAddress"),
)
if mibBuilder.loadTexts:
    staticLeasesEntry.setStatus("current")
_StaticLeasesMacAddress_Type = OctetString
_StaticLeasesMacAddress_Object = MibTableColumn
staticLeasesMacAddress = _StaticLeasesMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 800, 1, 100),
    _StaticLeasesMacAddress_Type()
)
staticLeasesMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticLeasesMacAddress.setStatus("current")


class _StaticLeasesIpAddress_Type(MxIpAddr):
    """Custom type staticLeasesIpAddress based on MxIpAddr"""
    defaultValue = OctetString("")


_StaticLeasesIpAddress_Type.__name__ = "MxIpAddr"
_StaticLeasesIpAddress_Object = MibTableColumn
staticLeasesIpAddress = _StaticLeasesIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 800, 1, 200),
    _StaticLeasesIpAddress_Type()
)
staticLeasesIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticLeasesIpAddress.setStatus("current")


class _StaticLeasesDelete_Type(Integer32):
    """Custom type staticLeasesDelete based on Integer32"""
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


_StaticLeasesDelete_Type.__name__ = "Integer32"
_StaticLeasesDelete_Object = MibTableColumn
staticLeasesDelete = _StaticLeasesDelete_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 800, 1, 300),
    _StaticLeasesDelete_Type()
)
staticLeasesDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticLeasesDelete.setStatus("current")
_AssignedLeasesInfoTable_Object = MibTable
assignedLeasesInfoTable = _AssignedLeasesInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 900)
)
if mibBuilder.loadTexts:
    assignedLeasesInfoTable.setStatus("current")
_AssignedLeasesInfoEntry_Object = MibTableRow
assignedLeasesInfoEntry = _AssignedLeasesInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 900, 1)
)
assignedLeasesInfoEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "assignedLeasesInfoIpAddress"),
)
if mibBuilder.loadTexts:
    assignedLeasesInfoEntry.setStatus("current")
_AssignedLeasesInfoIpAddress_Type = MxIpAddr
_AssignedLeasesInfoIpAddress_Object = MibTableColumn
assignedLeasesInfoIpAddress = _AssignedLeasesInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 900, 1, 100),
    _AssignedLeasesInfoIpAddress_Type()
)
assignedLeasesInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assignedLeasesInfoIpAddress.setStatus("current")
_AssignedLeasesInfoMacAddress_Type = OctetString
_AssignedLeasesInfoMacAddress_Object = MibTableColumn
assignedLeasesInfoMacAddress = _AssignedLeasesInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 900, 1, 200),
    _AssignedLeasesInfoMacAddress_Type()
)
assignedLeasesInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assignedLeasesInfoMacAddress.setStatus("current")
_AssignedLeasesInfoSubnetName_Type = OctetString
_AssignedLeasesInfoSubnetName_Object = MibTableColumn
assignedLeasesInfoSubnetName = _AssignedLeasesInfoSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 900, 1, 300),
    _AssignedLeasesInfoSubnetName_Type()
)
assignedLeasesInfoSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assignedLeasesInfoSubnetName.setStatus("current")
_AssignedLeasesInfoLeaseTimeLeft_Type = Unsigned32
_AssignedLeasesInfoLeaseTimeLeft_Object = MibTableColumn
assignedLeasesInfoLeaseTimeLeft = _AssignedLeasesInfoLeaseTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 900, 1, 400),
    _AssignedLeasesInfoLeaseTimeLeft_Type()
)
assignedLeasesInfoLeaseTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    assignedLeasesInfoLeaseTimeLeft.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000)
)


class _DefaultStaticOption66_Type(OctetString):
    """Custom type defaultStaticOption66 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_DefaultStaticOption66_Type.__name__ = "OctetString"
_DefaultStaticOption66_Object = MibScalar
defaultStaticOption66 = _DefaultStaticOption66_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 100),
    _DefaultStaticOption66_Type()
)
defaultStaticOption66.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticOption66.setStatus("current")


class _DefaultStaticOption67_Type(OctetString):
    """Custom type defaultStaticOption67 based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_DefaultStaticOption67_Type.__name__ = "OctetString"
_DefaultStaticOption67_Object = MibScalar
defaultStaticOption67 = _DefaultStaticOption67_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 200),
    _DefaultStaticOption67_Type()
)
defaultStaticOption67.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStaticOption67.setStatus("current")
_SpecificOption66Table_Object = MibTable
specificOption66Table = _SpecificOption66Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1000)
)
if mibBuilder.loadTexts:
    specificOption66Table.setStatus("current")
_SpecificOption66Entry_Object = MibTableRow
specificOption66Entry = _SpecificOption66Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1000, 1)
)
specificOption66Entry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificOption66SubnetName"),
)
if mibBuilder.loadTexts:
    specificOption66Entry.setStatus("current")
_SpecificOption66SubnetName_Type = OctetString
_SpecificOption66SubnetName_Object = MibTableColumn
specificOption66SubnetName = _SpecificOption66SubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1000, 1, 100),
    _SpecificOption66SubnetName_Type()
)
specificOption66SubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificOption66SubnetName.setStatus("current")


class _SpecificOption66EnableConfig_Type(MxEnableState):
    """Custom type specificOption66EnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificOption66EnableConfig_Type.__name__ = "MxEnableState"
_SpecificOption66EnableConfig_Object = MibTableColumn
specificOption66EnableConfig = _SpecificOption66EnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1000, 1, 200),
    _SpecificOption66EnableConfig_Type()
)
specificOption66EnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificOption66EnableConfig.setStatus("current")


class _SpecificOption66EnableOption_Type(MxEnableState):
    """Custom type specificOption66EnableOption based on MxEnableState"""
    defaultValue = 0


_SpecificOption66EnableOption_Type.__name__ = "MxEnableState"
_SpecificOption66EnableOption_Object = MibTableColumn
specificOption66EnableOption = _SpecificOption66EnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1000, 1, 300),
    _SpecificOption66EnableOption_Type()
)
specificOption66EnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificOption66EnableOption.setStatus("current")


class _SpecificOption66Value_Type(OctetString):
    """Custom type specificOption66Value based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_SpecificOption66Value_Type.__name__ = "OctetString"
_SpecificOption66Value_Object = MibTableColumn
specificOption66Value = _SpecificOption66Value_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1000, 1, 400),
    _SpecificOption66Value_Type()
)
specificOption66Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificOption66Value.setStatus("current")
_SpecificOption67Table_Object = MibTable
specificOption67Table = _SpecificOption67Table_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1100)
)
if mibBuilder.loadTexts:
    specificOption67Table.setStatus("current")
_SpecificOption67Entry_Object = MibTableRow
specificOption67Entry = _SpecificOption67Entry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1100, 1)
)
specificOption67Entry.setIndexNames(
    (0, "MX-DHCP-MIB", "specificOption67SubnetName"),
)
if mibBuilder.loadTexts:
    specificOption67Entry.setStatus("current")
_SpecificOption67SubnetName_Type = OctetString
_SpecificOption67SubnetName_Object = MibTableColumn
specificOption67SubnetName = _SpecificOption67SubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1100, 1, 100),
    _SpecificOption67SubnetName_Type()
)
specificOption67SubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specificOption67SubnetName.setStatus("current")


class _SpecificOption67EnableConfig_Type(MxEnableState):
    """Custom type specificOption67EnableConfig based on MxEnableState"""
    defaultValue = 0


_SpecificOption67EnableConfig_Type.__name__ = "MxEnableState"
_SpecificOption67EnableConfig_Object = MibTableColumn
specificOption67EnableConfig = _SpecificOption67EnableConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1100, 1, 200),
    _SpecificOption67EnableConfig_Type()
)
specificOption67EnableConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificOption67EnableConfig.setStatus("current")


class _SpecificOption67EnableOption_Type(MxEnableState):
    """Custom type specificOption67EnableOption based on MxEnableState"""
    defaultValue = 0


_SpecificOption67EnableOption_Type.__name__ = "MxEnableState"
_SpecificOption67EnableOption_Object = MibTableColumn
specificOption67EnableOption = _SpecificOption67EnableOption_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1100, 1, 300),
    _SpecificOption67EnableOption_Type()
)
specificOption67EnableOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificOption67EnableOption.setStatus("current")


class _SpecificOption67Value_Type(OctetString):
    """Custom type specificOption67Value based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_SpecificOption67Value_Type.__name__ = "OctetString"
_SpecificOption67Value_Object = MibTableColumn
specificOption67Value = _SpecificOption67Value_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 1000, 1100, 1, 400),
    _SpecificOption67Value_Type()
)
specificOption67Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specificOption67Value.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 10000)
)
_SubnetsStatsTable_Object = MibTable
subnetsStatsTable = _SubnetsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 10000, 100)
)
if mibBuilder.loadTexts:
    subnetsStatsTable.setStatus("current")
_SubnetsStatsEntry_Object = MibTableRow
subnetsStatsEntry = _SubnetsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 10000, 100, 1)
)
subnetsStatsEntry.setIndexNames(
    (0, "MX-DHCP-MIB", "subnetsStatsSubnetName"),
)
if mibBuilder.loadTexts:
    subnetsStatsEntry.setStatus("current")
_SubnetsStatsSubnetName_Type = OctetString
_SubnetsStatsSubnetName_Object = MibTableColumn
subnetsStatsSubnetName = _SubnetsStatsSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 10000, 100, 1, 100),
    _SubnetsStatsSubnetName_Type()
)
subnetsStatsSubnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetsStatsSubnetName.setStatus("current")
_SubnetsStatsNumberOfLeases_Type = Unsigned32
_SubnetsStatsNumberOfLeases_Object = MibTableColumn
subnetsStatsNumberOfLeases = _SubnetsStatsNumberOfLeases_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 10000, 100, 1, 200),
    _SubnetsStatsNumberOfLeases_Type()
)
subnetsStatsNumberOfLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subnetsStatsNumberOfLeases.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 60010)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 60020)
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
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 1900, 1, 60020, 100),
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
    "MX-DHCP-MIB",
    **{"dhcpMIB": dhcpMIB,
       "dhcpMIBObjects": dhcpMIBObjects,
       "subnetsTable": subnetsTable,
       "subnetsEntry": subnetsEntry,
       "subnetsNetworkInterfaceName": subnetsNetworkInterfaceName,
       "subnetsEnableSubnet": subnetsEnableSubnet,
       "subnetsStartAddress": subnetsStartAddress,
       "subnetsEndAddress": subnetsEndAddress,
       "subnetsAutomaticConfigurationInterface": subnetsAutomaticConfigurationInterface,
       "subnetsConfigStatus": subnetsConfigStatus,
       "subnetsDelete": subnetsDelete,
       "domainNameGroup": domainNameGroup,
       "defaultDomainNameConfigSource": defaultDomainNameConfigSource,
       "defaultStaticDomainName": defaultStaticDomainName,
       "specificDomainNamesTable": specificDomainNamesTable,
       "specificDomainNamesEntry": specificDomainNamesEntry,
       "specificDomainNamesSubnetName": specificDomainNamesSubnetName,
       "specificDomainNamesEnableConfig": specificDomainNamesEnableConfig,
       "specificDomainNamesEnableOption": specificDomainNamesEnableOption,
       "specificDomainNamesConfigSource": specificDomainNamesConfigSource,
       "specificDomainNamesStaticName": specificDomainNamesStaticName,
       "domainNamesInfoTable": domainNamesInfoTable,
       "domainNamesInfoEntry": domainNamesInfoEntry,
       "domainNamesInfoSubnetName": domainNamesInfoSubnetName,
       "domainNamesInfoDomainName": domainNamesInfoDomainName,
       "leaseTimeGroup": leaseTimeGroup,
       "defaultLeaseTime": defaultLeaseTime,
       "specificLeaseTimesTable": specificLeaseTimesTable,
       "specificLeaseTimesEntry": specificLeaseTimesEntry,
       "specificLeaseTimesSubnetName": specificLeaseTimesSubnetName,
       "specificLeaseTimesEnableConfig": specificLeaseTimesEnableConfig,
       "specificLeaseTimesLeaseTime": specificLeaseTimesLeaseTime,
       "leaseTimesInfoTable": leaseTimesInfoTable,
       "leaseTimesInfoEntry": leaseTimesInfoEntry,
       "leaseTimesInfoSubnetName": leaseTimesInfoSubnetName,
       "leaseTimesInfoDefault": leaseTimesInfoDefault,
       "defaultRouterGroup": defaultRouterGroup,
       "specificDefaultRoutersTable": specificDefaultRoutersTable,
       "specificDefaultRoutersEntry": specificDefaultRoutersEntry,
       "specificDefaultRoutersSubnetName": specificDefaultRoutersSubnetName,
       "specificDefaultRoutersEnableOption": specificDefaultRoutersEnableOption,
       "specificDefaultRoutersConfigSource": specificDefaultRoutersConfigSource,
       "specificDefaultRoutersStaticRouter": specificDefaultRoutersStaticRouter,
       "defaultRoutersInfoTable": defaultRoutersInfoTable,
       "defaultRoutersInfoEntry": defaultRoutersInfoEntry,
       "defaultRoutersInfoSubnetName": defaultRoutersInfoSubnetName,
       "defaultRoutersInfoDefaultRouter": defaultRoutersInfoDefaultRouter,
       "dnsServersGroup": dnsServersGroup,
       "defaultDnsServersConfigSource": defaultDnsServersConfigSource,
       "defaultStaticDnsServersTable": defaultStaticDnsServersTable,
       "defaultStaticDnsServersEntry": defaultStaticDnsServersEntry,
       "defaultStaticDnsServersPriority": defaultStaticDnsServersPriority,
       "defaultStaticDnsServersIpAddress": defaultStaticDnsServersIpAddress,
       "specificDnsServersTable": specificDnsServersTable,
       "specificDnsServersEntry": specificDnsServersEntry,
       "specificDnsServersSubnetName": specificDnsServersSubnetName,
       "specificDnsServersEnableConfig": specificDnsServersEnableConfig,
       "specificDnsServersEnableOption": specificDnsServersEnableOption,
       "specificDnsServersConfigSource": specificDnsServersConfigSource,
       "specificDnsServersStaticDns1": specificDnsServersStaticDns1,
       "specificDnsServersStaticDns2": specificDnsServersStaticDns2,
       "specificDnsServersStaticDns3": specificDnsServersStaticDns3,
       "specificDnsServersStaticDns4": specificDnsServersStaticDns4,
       "dnsServersInfoTable": dnsServersInfoTable,
       "dnsServersInfoEntry": dnsServersInfoEntry,
       "dnsServersInfoSubnetName": dnsServersInfoSubnetName,
       "dnsServersInfoDns1": dnsServersInfoDns1,
       "dnsServersInfoDns2": dnsServersInfoDns2,
       "dnsServersInfoDns3": dnsServersInfoDns3,
       "dnsServersInfoDns4": dnsServersInfoDns4,
       "ntpServersGroup": ntpServersGroup,
       "defaultNtpServersConfigSource": defaultNtpServersConfigSource,
       "defaultStaticNtpServersTable": defaultStaticNtpServersTable,
       "defaultStaticNtpServersEntry": defaultStaticNtpServersEntry,
       "defaultStaticNtpServersPriority": defaultStaticNtpServersPriority,
       "defaultStaticNtpServersIpAddress": defaultStaticNtpServersIpAddress,
       "specificNtpServersTable": specificNtpServersTable,
       "specificNtpServersEntry": specificNtpServersEntry,
       "specificNtpServersSubnetName": specificNtpServersSubnetName,
       "specificNtpServersEnableConfig": specificNtpServersEnableConfig,
       "specificNtpServersEnableOption": specificNtpServersEnableOption,
       "specificNtpServersConfigSource": specificNtpServersConfigSource,
       "specificNtpServersStaticNtp1": specificNtpServersStaticNtp1,
       "specificNtpServersStaticNtp2": specificNtpServersStaticNtp2,
       "specificNtpServersStaticNtp3": specificNtpServersStaticNtp3,
       "specificNtpServersStaticNtp4": specificNtpServersStaticNtp4,
       "ntpServersInfoTable": ntpServersInfoTable,
       "ntpServersInfoEntry": ntpServersInfoEntry,
       "ntpServersInfoSubnetName": ntpServersInfoSubnetName,
       "ntpServersInfoNtp1": ntpServersInfoNtp1,
       "ntpServersInfoNtp2": ntpServersInfoNtp2,
       "ntpServersInfoNtp3": ntpServersInfoNtp3,
       "ntpServersInfoNtp4": ntpServersInfoNtp4,
       "nbnsServersGroup": nbnsServersGroup,
       "defaultStaticNbnsServersTable": defaultStaticNbnsServersTable,
       "defaultStaticNbnsServersEntry": defaultStaticNbnsServersEntry,
       "defaultStaticNbnsServersPriority": defaultStaticNbnsServersPriority,
       "defaultStaticNbnsServersIpAddress": defaultStaticNbnsServersIpAddress,
       "specificNbnsServersTable": specificNbnsServersTable,
       "specificNbnsServersEntry": specificNbnsServersEntry,
       "specificNbnsServersSubnetName": specificNbnsServersSubnetName,
       "specificNbnsServersEnableConfig": specificNbnsServersEnableConfig,
       "specificNbnsServersEnableOption": specificNbnsServersEnableOption,
       "specificNbnsServersStaticNbns1": specificNbnsServersStaticNbns1,
       "specificNbnsServersStaticNbns2": specificNbnsServersStaticNbns2,
       "specificNbnsServersStaticNbns3": specificNbnsServersStaticNbns3,
       "specificNbnsServersStaticNbns4": specificNbnsServersStaticNbns4,
       "nbnsServersInfoTable": nbnsServersInfoTable,
       "nbnsServersInfoEntry": nbnsServersInfoEntry,
       "nbnsServersInfoSubnetName": nbnsServersInfoSubnetName,
       "nbnsServersInfoNbns1": nbnsServersInfoNbns1,
       "nbnsServersInfoNbns2": nbnsServersInfoNbns2,
       "nbnsServersInfoNbns3": nbnsServersInfoNbns3,
       "nbnsServersInfoNbns4": nbnsServersInfoNbns4,
       "staticLeasesTable": staticLeasesTable,
       "staticLeasesEntry": staticLeasesEntry,
       "staticLeasesMacAddress": staticLeasesMacAddress,
       "staticLeasesIpAddress": staticLeasesIpAddress,
       "staticLeasesDelete": staticLeasesDelete,
       "assignedLeasesInfoTable": assignedLeasesInfoTable,
       "assignedLeasesInfoEntry": assignedLeasesInfoEntry,
       "assignedLeasesInfoIpAddress": assignedLeasesInfoIpAddress,
       "assignedLeasesInfoMacAddress": assignedLeasesInfoMacAddress,
       "assignedLeasesInfoSubnetName": assignedLeasesInfoSubnetName,
       "assignedLeasesInfoLeaseTimeLeft": assignedLeasesInfoLeaseTimeLeft,
       "provisioningGroup": provisioningGroup,
       "defaultStaticOption66": defaultStaticOption66,
       "defaultStaticOption67": defaultStaticOption67,
       "specificOption66Table": specificOption66Table,
       "specificOption66Entry": specificOption66Entry,
       "specificOption66SubnetName": specificOption66SubnetName,
       "specificOption66EnableConfig": specificOption66EnableConfig,
       "specificOption66EnableOption": specificOption66EnableOption,
       "specificOption66Value": specificOption66Value,
       "specificOption67Table": specificOption67Table,
       "specificOption67Entry": specificOption67Entry,
       "specificOption67SubnetName": specificOption67SubnetName,
       "specificOption67EnableConfig": specificOption67EnableConfig,
       "specificOption67EnableOption": specificOption67EnableOption,
       "specificOption67Value": specificOption67Value,
       "statisticsGroup": statisticsGroup,
       "subnetsStatsTable": subnetsStatsTable,
       "subnetsStatsEntry": subnetsStatsEntry,
       "subnetsStatsSubnetName": subnetsStatsSubnetName,
       "subnetsStatsNumberOfLeases": subnetsStatsNumberOfLeases,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
