# SNMP MIB module (FOUNDRY-DHCPSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/FOUNDRY-DHCPSERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:00:45 2025
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

snDhcpServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42)
)
if mibBuilder.loadTexts:
    snDhcpServer.setRevisions(
        ("2018-08-07 00:00",
         "2018-08-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnDhcpServerGlobalObjects_ObjectIdentity = ObjectIdentity
snDhcpServerGlobalObjects = _SnDhcpServerGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 1)
)


class _SnDhcpServerGlobalConfigState_Type(Integer32):
    """Custom type snDhcpServerGlobalConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnDhcpServerGlobalConfigState_Type.__name__ = "Integer32"
_SnDhcpServerGlobalConfigState_Object = MibScalar
snDhcpServerGlobalConfigState = _SnDhcpServerGlobalConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 1, 1),
    _SnDhcpServerGlobalConfigState_Type()
)
snDhcpServerGlobalConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerGlobalConfigState.setStatus("current")
_SnDhcpServerTableObjects_ObjectIdentity = ObjectIdentity
snDhcpServerTableObjects = _SnDhcpServerTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2)
)
_SnDhcpServerPoolConfigTable_Object = MibTable
snDhcpServerPoolConfigTable = _SnDhcpServerPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1)
)
if mibBuilder.loadTexts:
    snDhcpServerPoolConfigTable.setStatus("current")
_SnDhcpServerPoolConfigEntry_Object = MibTableRow
snDhcpServerPoolConfigEntry = _SnDhcpServerPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1)
)
snDhcpServerPoolConfigEntry.setIndexNames(
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolName"),
)
if mibBuilder.loadTexts:
    snDhcpServerPoolConfigEntry.setStatus("current")


class _SnDhcpServerPoolName_Type(OctetString):
    """Custom type snDhcpServerPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnDhcpServerPoolName_Type.__name__ = "OctetString"
_SnDhcpServerPoolName_Object = MibTableColumn
snDhcpServerPoolName = _SnDhcpServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 1),
    _SnDhcpServerPoolName_Type()
)
snDhcpServerPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snDhcpServerPoolName.setStatus("current")
_SnDhcpServerPoolNetwork_Type = IpAddress
_SnDhcpServerPoolNetwork_Object = MibTableColumn
snDhcpServerPoolNetwork = _SnDhcpServerPoolNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 2),
    _SnDhcpServerPoolNetwork_Type()
)
snDhcpServerPoolNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolNetwork.setStatus("current")
_SnDhcpServerPoolNetworkMask_Type = IpAddress
_SnDhcpServerPoolNetworkMask_Object = MibTableColumn
snDhcpServerPoolNetworkMask = _SnDhcpServerPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 3),
    _SnDhcpServerPoolNetworkMask_Type()
)
snDhcpServerPoolNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolNetworkMask.setStatus("current")
_SnDhcpServerPoolStartAddr_Type = IpAddress
_SnDhcpServerPoolStartAddr_Object = MibTableColumn
snDhcpServerPoolStartAddr = _SnDhcpServerPoolStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 4),
    _SnDhcpServerPoolStartAddr_Type()
)
snDhcpServerPoolStartAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolStartAddr.setStatus("current")
_SnDhcpServerPoolEndAddr_Type = IpAddress
_SnDhcpServerPoolEndAddr_Object = MibTableColumn
snDhcpServerPoolEndAddr = _SnDhcpServerPoolEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 5),
    _SnDhcpServerPoolEndAddr_Type()
)
snDhcpServerPoolEndAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolEndAddr.setStatus("current")


class _SnDhcpServerPoolLeaseDay_Type(Integer32):
    """Custom type snDhcpServerPoolLeaseDay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_SnDhcpServerPoolLeaseDay_Type.__name__ = "Integer32"
_SnDhcpServerPoolLeaseDay_Object = MibTableColumn
snDhcpServerPoolLeaseDay = _SnDhcpServerPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 6),
    _SnDhcpServerPoolLeaseDay_Type()
)
snDhcpServerPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolLeaseDay.setStatus("current")


class _SnDhcpServerPoolLeaseHour_Type(Integer32):
    """Custom type snDhcpServerPoolLeaseHour based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SnDhcpServerPoolLeaseHour_Type.__name__ = "Integer32"
_SnDhcpServerPoolLeaseHour_Object = MibTableColumn
snDhcpServerPoolLeaseHour = _SnDhcpServerPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 7),
    _SnDhcpServerPoolLeaseHour_Type()
)
snDhcpServerPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolLeaseHour.setStatus("current")


class _SnDhcpServerPoolLeaseMinute_Type(Integer32):
    """Custom type snDhcpServerPoolLeaseMinute based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_SnDhcpServerPoolLeaseMinute_Type.__name__ = "Integer32"
_SnDhcpServerPoolLeaseMinute_Object = MibTableColumn
snDhcpServerPoolLeaseMinute = _SnDhcpServerPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 8),
    _SnDhcpServerPoolLeaseMinute_Type()
)
snDhcpServerPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolLeaseMinute.setStatus("current")


class _SnDhcpServerPoolDeploy_Type(Integer32):
    """Custom type snDhcpServerPoolDeploy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nodeploy", 0),
          ("deploy", 1))
    )


_SnDhcpServerPoolDeploy_Type.__name__ = "Integer32"
_SnDhcpServerPoolDeploy_Object = MibTableColumn
snDhcpServerPoolDeploy = _SnDhcpServerPoolDeploy_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 9),
    _SnDhcpServerPoolDeploy_Type()
)
snDhcpServerPoolDeploy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolDeploy.setStatus("current")


class _SnDhcpServerPoolRowStatus_Type(Integer32):
    """Custom type snDhcpServerPoolRowStatus based on Integer32"""
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
        *(("other", 1),
          ("valid", 2),
          ("delete", 3),
          ("create", 4))
    )


_SnDhcpServerPoolRowStatus_Type.__name__ = "Integer32"
_SnDhcpServerPoolRowStatus_Object = MibTableColumn
snDhcpServerPoolRowStatus = _SnDhcpServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 1, 1, 10),
    _SnDhcpServerPoolRowStatus_Type()
)
snDhcpServerPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snDhcpServerPoolRowStatus.setStatus("current")
_SnDhcpServerPoolOptionConfigTable_Object = MibTable
snDhcpServerPoolOptionConfigTable = _SnDhcpServerPoolOptionConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2)
)
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionConfigTable.setStatus("current")
_SnDhcpServerPoolOptionConfigEntry_Object = MibTableRow
snDhcpServerPoolOptionConfigEntry = _SnDhcpServerPoolOptionConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1)
)
snDhcpServerPoolOptionConfigEntry.setIndexNames(
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolName"),
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolOptionCode"),
)
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionConfigEntry.setStatus("current")


class _SnDhcpServerPoolOptionCode_Type(Integer32):
    """Custom type snDhcpServerPoolOptionCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_SnDhcpServerPoolOptionCode_Type.__name__ = "Integer32"
_SnDhcpServerPoolOptionCode_Object = MibTableColumn
snDhcpServerPoolOptionCode = _SnDhcpServerPoolOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 1),
    _SnDhcpServerPoolOptionCode_Type()
)
snDhcpServerPoolOptionCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionCode.setStatus("current")


class _SnDhcpServerPoolOptionType_Type(Integer32):
    """Custom type snDhcpServerPoolOptionType based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("hex", 1),
          ("ip", 2),
          ("bool", 3),
          ("integer", 4),
          ("telephony", 5),
          ("ipaddrpair", 6),
          ("staticroute", 7),
          ("slpdiragent", 8),
          ("slpsrvscope", 9),
          ("pxeintfid", 10),
          ("pxeclientid", 11))
    )


_SnDhcpServerPoolOptionType_Type.__name__ = "Integer32"
_SnDhcpServerPoolOptionType_Object = MibTableColumn
snDhcpServerPoolOptionType = _SnDhcpServerPoolOptionType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 2),
    _SnDhcpServerPoolOptionType_Type()
)
snDhcpServerPoolOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionType.setStatus("current")


class _SnDhcpServerPoolOptionAscii_Type(OctetString):
    """Custom type snDhcpServerPoolOptionAscii based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnDhcpServerPoolOptionAscii_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionAscii_Object = MibTableColumn
snDhcpServerPoolOptionAscii = _SnDhcpServerPoolOptionAscii_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 3),
    _SnDhcpServerPoolOptionAscii_Type()
)
snDhcpServerPoolOptionAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionAscii.setStatus("current")


class _SnDhcpServerPoolOptionHexString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionHexString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SnDhcpServerPoolOptionHexString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionHexString_Object = MibTableColumn
snDhcpServerPoolOptionHexString = _SnDhcpServerPoolOptionHexString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 4),
    _SnDhcpServerPoolOptionHexString_Type()
)
snDhcpServerPoolOptionHexString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionHexString.setStatus("current")


class _SnDhcpServerPoolOptionIPString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionIPString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 12),
    )


_SnDhcpServerPoolOptionIPString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionIPString_Object = MibTableColumn
snDhcpServerPoolOptionIPString = _SnDhcpServerPoolOptionIPString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 5),
    _SnDhcpServerPoolOptionIPString_Type()
)
snDhcpServerPoolOptionIPString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionIPString.setStatus("current")
_SnDhcpServerPoolOptionRowStatus_Type = RowStatus
_SnDhcpServerPoolOptionRowStatus_Object = MibTableColumn
snDhcpServerPoolOptionRowStatus = _SnDhcpServerPoolOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 6),
    _SnDhcpServerPoolOptionRowStatus_Type()
)
snDhcpServerPoolOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionRowStatus.setStatus("current")


class _SnDhcpServerPoolOptionBoolString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionBoolString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 12),
    )


_SnDhcpServerPoolOptionBoolString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionBoolString_Object = MibTableColumn
snDhcpServerPoolOptionBoolString = _SnDhcpServerPoolOptionBoolString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 7),
    _SnDhcpServerPoolOptionBoolString_Type()
)
snDhcpServerPoolOptionBoolString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionBoolString.setStatus("current")


class _SnDhcpServerPoolOptionIntString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionIntString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 12),
    )


_SnDhcpServerPoolOptionIntString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionIntString_Object = MibTableColumn
snDhcpServerPoolOptionIntString = _SnDhcpServerPoolOptionIntString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 8),
    _SnDhcpServerPoolOptionIntString_Type()
)
snDhcpServerPoolOptionIntString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionIntString.setStatus("current")


class _SnDhcpServerPoolOptionIPAddrPairString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionIPAddrPairString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 16),
    )


_SnDhcpServerPoolOptionIPAddrPairString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionIPAddrPairString_Object = MibTableColumn
snDhcpServerPoolOptionIPAddrPairString = _SnDhcpServerPoolOptionIPAddrPairString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 9),
    _SnDhcpServerPoolOptionIPAddrPairString_Type()
)
snDhcpServerPoolOptionIPAddrPairString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionIPAddrPairString.setStatus("current")


class _SnDhcpServerPoolOptionStaticRouteString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionStaticRouteString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 16),
    )


_SnDhcpServerPoolOptionStaticRouteString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionStaticRouteString_Object = MibTableColumn
snDhcpServerPoolOptionStaticRouteString = _SnDhcpServerPoolOptionStaticRouteString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 10),
    _SnDhcpServerPoolOptionStaticRouteString_Type()
)
snDhcpServerPoolOptionStaticRouteString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionStaticRouteString.setStatus("current")


class _SnDhcpServerPoolOptionSlpDirAgentString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionSlpDirAgentString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 54),
    )


_SnDhcpServerPoolOptionSlpDirAgentString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionSlpDirAgentString_Object = MibTableColumn
snDhcpServerPoolOptionSlpDirAgentString = _SnDhcpServerPoolOptionSlpDirAgentString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 11),
    _SnDhcpServerPoolOptionSlpDirAgentString_Type()
)
snDhcpServerPoolOptionSlpDirAgentString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionSlpDirAgentString.setStatus("current")


class _SnDhcpServerPoolOptionSlpSrvScopeString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionSlpSrvScopeString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 135),
    )


_SnDhcpServerPoolOptionSlpSrvScopeString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionSlpSrvScopeString_Object = MibTableColumn
snDhcpServerPoolOptionSlpSrvScopeString = _SnDhcpServerPoolOptionSlpSrvScopeString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 12),
    _SnDhcpServerPoolOptionSlpSrvScopeString_Type()
)
snDhcpServerPoolOptionSlpSrvScopeString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionSlpSrvScopeString.setStatus("current")


class _SnDhcpServerPoolOptionPxeIntfIdString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionPxeIntfIdString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_SnDhcpServerPoolOptionPxeIntfIdString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionPxeIntfIdString_Object = MibTableColumn
snDhcpServerPoolOptionPxeIntfIdString = _SnDhcpServerPoolOptionPxeIntfIdString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 13),
    _SnDhcpServerPoolOptionPxeIntfIdString_Type()
)
snDhcpServerPoolOptionPxeIntfIdString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionPxeIntfIdString.setStatus("current")


class _SnDhcpServerPoolOptionPxeClientIdString_Type(OctetString):
    """Custom type snDhcpServerPoolOptionPxeClientIdString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 132),
    )


_SnDhcpServerPoolOptionPxeClientIdString_Type.__name__ = "OctetString"
_SnDhcpServerPoolOptionPxeClientIdString_Object = MibTableColumn
snDhcpServerPoolOptionPxeClientIdString = _SnDhcpServerPoolOptionPxeClientIdString_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 2, 1, 14),
    _SnDhcpServerPoolOptionPxeClientIdString_Type()
)
snDhcpServerPoolOptionPxeClientIdString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolOptionPxeClientIdString.setStatus("current")
_SnDhcpServerPoolExcludedSingleAddressTable_Object = MibTable
snDhcpServerPoolExcludedSingleAddressTable = _SnDhcpServerPoolExcludedSingleAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 3)
)
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedSingleAddressTable.setStatus("current")
_SnDhcpServerPoolExcludedSingleAddressEntry_Object = MibTableRow
snDhcpServerPoolExcludedSingleAddressEntry = _SnDhcpServerPoolExcludedSingleAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 3, 1)
)
snDhcpServerPoolExcludedSingleAddressEntry.setIndexNames(
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolName"),
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolExcludedAddressIndex"),
)
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedSingleAddressEntry.setStatus("current")


class _SnDhcpServerPoolExcludedAddressIndex_Type(Integer32):
    """Custom type snDhcpServerPoolExcludedAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SnDhcpServerPoolExcludedAddressIndex_Type.__name__ = "Integer32"
_SnDhcpServerPoolExcludedAddressIndex_Object = MibTableColumn
snDhcpServerPoolExcludedAddressIndex = _SnDhcpServerPoolExcludedAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 3, 1, 1),
    _SnDhcpServerPoolExcludedAddressIndex_Type()
)
snDhcpServerPoolExcludedAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedAddressIndex.setStatus("current")
_SnDhcpServerPoolExcludedSingleAddress_Type = IpAddress
_SnDhcpServerPoolExcludedSingleAddress_Object = MibTableColumn
snDhcpServerPoolExcludedSingleAddress = _SnDhcpServerPoolExcludedSingleAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 3, 1, 2),
    _SnDhcpServerPoolExcludedSingleAddress_Type()
)
snDhcpServerPoolExcludedSingleAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedSingleAddress.setStatus("current")
_SnDhcpServerPoolExcludedSingleAddressRowStatus_Type = RowStatus
_SnDhcpServerPoolExcludedSingleAddressRowStatus_Object = MibTableColumn
snDhcpServerPoolExcludedSingleAddressRowStatus = _SnDhcpServerPoolExcludedSingleAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 3, 1, 3),
    _SnDhcpServerPoolExcludedSingleAddressRowStatus_Type()
)
snDhcpServerPoolExcludedSingleAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedSingleAddressRowStatus.setStatus("current")
_SnDhcpServerPoolExcludedAddressRangeTable_Object = MibTable
snDhcpServerPoolExcludedAddressRangeTable = _SnDhcpServerPoolExcludedAddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 4)
)
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedAddressRangeTable.setStatus("current")
_SnDhcpServerPoolExcludedAddressRangeEntry_Object = MibTableRow
snDhcpServerPoolExcludedAddressRangeEntry = _SnDhcpServerPoolExcludedAddressRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 4, 1)
)
snDhcpServerPoolExcludedAddressRangeEntry.setIndexNames(
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolName"),
    (0, "FOUNDRY-DHCPSERVER-MIB", "snDhcpServerPoolExcludedAddressRangeIndex"),
)
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedAddressRangeEntry.setStatus("current")


class _SnDhcpServerPoolExcludedAddressRangeIndex_Type(Integer32):
    """Custom type snDhcpServerPoolExcludedAddressRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 85),
    )


_SnDhcpServerPoolExcludedAddressRangeIndex_Type.__name__ = "Integer32"
_SnDhcpServerPoolExcludedAddressRangeIndex_Object = MibTableColumn
snDhcpServerPoolExcludedAddressRangeIndex = _SnDhcpServerPoolExcludedAddressRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 4, 1, 1),
    _SnDhcpServerPoolExcludedAddressRangeIndex_Type()
)
snDhcpServerPoolExcludedAddressRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedAddressRangeIndex.setStatus("current")
_SnDhcpServerPoolExcludedStartAddress_Type = IpAddress
_SnDhcpServerPoolExcludedStartAddress_Object = MibTableColumn
snDhcpServerPoolExcludedStartAddress = _SnDhcpServerPoolExcludedStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 4, 1, 2),
    _SnDhcpServerPoolExcludedStartAddress_Type()
)
snDhcpServerPoolExcludedStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedStartAddress.setStatus("current")
_SnDhcpServerPoolExcludedEndAddress_Type = IpAddress
_SnDhcpServerPoolExcludedEndAddress_Object = MibTableColumn
snDhcpServerPoolExcludedEndAddress = _SnDhcpServerPoolExcludedEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 4, 1, 3),
    _SnDhcpServerPoolExcludedEndAddress_Type()
)
snDhcpServerPoolExcludedEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedEndAddress.setStatus("current")
_SnDhcpServerPoolExcludedAddressRowStatus_Type = RowStatus
_SnDhcpServerPoolExcludedAddressRowStatus_Object = MibTableColumn
snDhcpServerPoolExcludedAddressRowStatus = _SnDhcpServerPoolExcludedAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 42, 2, 4, 1, 4),
    _SnDhcpServerPoolExcludedAddressRowStatus_Type()
)
snDhcpServerPoolExcludedAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snDhcpServerPoolExcludedAddressRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-DHCPSERVER-MIB",
    **{"snDhcpServer": snDhcpServer,
       "snDhcpServerGlobalObjects": snDhcpServerGlobalObjects,
       "snDhcpServerGlobalConfigState": snDhcpServerGlobalConfigState,
       "snDhcpServerTableObjects": snDhcpServerTableObjects,
       "snDhcpServerPoolConfigTable": snDhcpServerPoolConfigTable,
       "snDhcpServerPoolConfigEntry": snDhcpServerPoolConfigEntry,
       "snDhcpServerPoolName": snDhcpServerPoolName,
       "snDhcpServerPoolNetwork": snDhcpServerPoolNetwork,
       "snDhcpServerPoolNetworkMask": snDhcpServerPoolNetworkMask,
       "snDhcpServerPoolStartAddr": snDhcpServerPoolStartAddr,
       "snDhcpServerPoolEndAddr": snDhcpServerPoolEndAddr,
       "snDhcpServerPoolLeaseDay": snDhcpServerPoolLeaseDay,
       "snDhcpServerPoolLeaseHour": snDhcpServerPoolLeaseHour,
       "snDhcpServerPoolLeaseMinute": snDhcpServerPoolLeaseMinute,
       "snDhcpServerPoolDeploy": snDhcpServerPoolDeploy,
       "snDhcpServerPoolRowStatus": snDhcpServerPoolRowStatus,
       "snDhcpServerPoolOptionConfigTable": snDhcpServerPoolOptionConfigTable,
       "snDhcpServerPoolOptionConfigEntry": snDhcpServerPoolOptionConfigEntry,
       "snDhcpServerPoolOptionCode": snDhcpServerPoolOptionCode,
       "snDhcpServerPoolOptionType": snDhcpServerPoolOptionType,
       "snDhcpServerPoolOptionAscii": snDhcpServerPoolOptionAscii,
       "snDhcpServerPoolOptionHexString": snDhcpServerPoolOptionHexString,
       "snDhcpServerPoolOptionIPString": snDhcpServerPoolOptionIPString,
       "snDhcpServerPoolOptionRowStatus": snDhcpServerPoolOptionRowStatus,
       "snDhcpServerPoolOptionBoolString": snDhcpServerPoolOptionBoolString,
       "snDhcpServerPoolOptionIntString": snDhcpServerPoolOptionIntString,
       "snDhcpServerPoolOptionIPAddrPairString": snDhcpServerPoolOptionIPAddrPairString,
       "snDhcpServerPoolOptionStaticRouteString": snDhcpServerPoolOptionStaticRouteString,
       "snDhcpServerPoolOptionSlpDirAgentString": snDhcpServerPoolOptionSlpDirAgentString,
       "snDhcpServerPoolOptionSlpSrvScopeString": snDhcpServerPoolOptionSlpSrvScopeString,
       "snDhcpServerPoolOptionPxeIntfIdString": snDhcpServerPoolOptionPxeIntfIdString,
       "snDhcpServerPoolOptionPxeClientIdString": snDhcpServerPoolOptionPxeClientIdString,
       "snDhcpServerPoolExcludedSingleAddressTable": snDhcpServerPoolExcludedSingleAddressTable,
       "snDhcpServerPoolExcludedSingleAddressEntry": snDhcpServerPoolExcludedSingleAddressEntry,
       "snDhcpServerPoolExcludedAddressIndex": snDhcpServerPoolExcludedAddressIndex,
       "snDhcpServerPoolExcludedSingleAddress": snDhcpServerPoolExcludedSingleAddress,
       "snDhcpServerPoolExcludedSingleAddressRowStatus": snDhcpServerPoolExcludedSingleAddressRowStatus,
       "snDhcpServerPoolExcludedAddressRangeTable": snDhcpServerPoolExcludedAddressRangeTable,
       "snDhcpServerPoolExcludedAddressRangeEntry": snDhcpServerPoolExcludedAddressRangeEntry,
       "snDhcpServerPoolExcludedAddressRangeIndex": snDhcpServerPoolExcludedAddressRangeIndex,
       "snDhcpServerPoolExcludedStartAddress": snDhcpServerPoolExcludedStartAddress,
       "snDhcpServerPoolExcludedEndAddress": snDhcpServerPoolExcludedEndAddress,
       "snDhcpServerPoolExcludedAddressRowStatus": snDhcpServerPoolExcludedAddressRowStatus}
)
