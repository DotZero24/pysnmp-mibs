# SNMP MIB module (ZTE-DSL-IPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-IPOA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:23 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxDsl,) = mibBuilder.importSymbols(
    "ZTE-DSL-MIB",
    "zxDsl")


# MODULE-IDENTITY

zxDslIpoaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxDslIpoaMibObjects_ObjectIdentity = ObjectIdentity
zxDslIpoaMibObjects = _ZxDslIpoaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1)
)
_ZxDslIpoaGlobalObjects_ObjectIdentity = ObjectIdentity
zxDslIpoaGlobalObjects = _ZxDslIpoaGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 1)
)
_ZxDslIpoaDefGateway_Type = IpAddress
_ZxDslIpoaDefGateway_Object = MibScalar
zxDslIpoaDefGateway = _ZxDslIpoaDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 1, 1),
    _ZxDslIpoaDefGateway_Type()
)
zxDslIpoaDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslIpoaDefGateway.setStatus("current")


class _ZxDslIpoaQueryInterval_Type(Integer32):
    """Custom type zxDslIpoaQueryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxDslIpoaQueryInterval_Type.__name__ = "Integer32"
_ZxDslIpoaQueryInterval_Object = MibScalar
zxDslIpoaQueryInterval = _ZxDslIpoaQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 1, 2),
    _ZxDslIpoaQueryInterval_Type()
)
zxDslIpoaQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslIpoaQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxDslIpoaQueryInterval.setUnits("minutes")


class _ZxDslIpoaGatewayARPInterval_Type(Integer32):
    """Custom type zxDslIpoaGatewayARPInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxDslIpoaGatewayARPInterval_Type.__name__ = "Integer32"
_ZxDslIpoaGatewayARPInterval_Object = MibScalar
zxDslIpoaGatewayARPInterval = _ZxDslIpoaGatewayARPInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 1, 3),
    _ZxDslIpoaGatewayARPInterval_Type()
)
zxDslIpoaGatewayARPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslIpoaGatewayARPInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxDslIpoaGatewayARPInterval.setUnits("minutes")
_ZxDslIpoaUser_ObjectIdentity = ObjectIdentity
zxDslIpoaUser = _ZxDslIpoaUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2)
)
_ZxDslIpoaUserConfTable_Object = MibTable
zxDslIpoaUserConfTable = _ZxDslIpoaUserConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxDslIpoaUserConfTable.setStatus("current")
_ZxDslIpoaUserConfEntry_Object = MibTableRow
zxDslIpoaUserConfEntry = _ZxDslIpoaUserConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1)
)
zxDslIpoaUserConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-IPOA-MIB", "zxDslIpoaUserConfBrgPortId"),
)
if mibBuilder.loadTexts:
    zxDslIpoaUserConfEntry.setStatus("current")
_ZxDslIpoaUserConfBrgPortId_Type = Integer32
_ZxDslIpoaUserConfBrgPortId_Object = MibTableColumn
zxDslIpoaUserConfBrgPortId = _ZxDslIpoaUserConfBrgPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 1),
    _ZxDslIpoaUserConfBrgPortId_Type()
)
zxDslIpoaUserConfBrgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfBrgPortId.setStatus("current")
_ZxDslIpoaUserConfIp_Type = IpAddress
_ZxDslIpoaUserConfIp_Object = MibTableColumn
zxDslIpoaUserConfIp = _ZxDslIpoaUserConfIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 2),
    _ZxDslIpoaUserConfIp_Type()
)
zxDslIpoaUserConfIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfIp.setStatus("current")


class _ZxDslIpoaUserConfInAtmArp_Type(Integer32):
    """Custom type zxDslIpoaUserConfInAtmArp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxDslIpoaUserConfInAtmArp_Type.__name__ = "Integer32"
_ZxDslIpoaUserConfInAtmArp_Object = MibTableColumn
zxDslIpoaUserConfInAtmArp = _ZxDslIpoaUserConfInAtmArp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 3),
    _ZxDslIpoaUserConfInAtmArp_Type()
)
zxDslIpoaUserConfInAtmArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfInAtmArp.setStatus("current")


class _ZxDslIpoaUserConfLayer_Type(Integer32):
    """Custom type zxDslIpoaUserConfLayer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("layer2", 1),
          ("layer3", 2))
    )


_ZxDslIpoaUserConfLayer_Type.__name__ = "Integer32"
_ZxDslIpoaUserConfLayer_Object = MibTableColumn
zxDslIpoaUserConfLayer = _ZxDslIpoaUserConfLayer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 4),
    _ZxDslIpoaUserConfLayer_Type()
)
zxDslIpoaUserConfLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfLayer.setStatus("current")
_ZxDslIpoaUserConfL2gatewayIp_Type = IpAddress
_ZxDslIpoaUserConfL2gatewayIp_Object = MibTableColumn
zxDslIpoaUserConfL2gatewayIp = _ZxDslIpoaUserConfL2gatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 5),
    _ZxDslIpoaUserConfL2gatewayIp_Type()
)
zxDslIpoaUserConfL2gatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfL2gatewayIp.setStatus("current")
_ZxDslIpoaUserConfL2gatewayMac_Type = MacAddress
_ZxDslIpoaUserConfL2gatewayMac_Object = MibTableColumn
zxDslIpoaUserConfL2gatewayMac = _ZxDslIpoaUserConfL2gatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 6),
    _ZxDslIpoaUserConfL2gatewayMac_Type()
)
zxDslIpoaUserConfL2gatewayMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfL2gatewayMac.setStatus("current")
_ZxDslIpoaUserConfRowStatus_Type = RowStatus
_ZxDslIpoaUserConfRowStatus_Object = MibTableColumn
zxDslIpoaUserConfRowStatus = _ZxDslIpoaUserConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 1, 1, 10),
    _ZxDslIpoaUserConfRowStatus_Type()
)
zxDslIpoaUserConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslIpoaUserConfRowStatus.setStatus("current")
_ZxDslIpoaUserInfoTable_Object = MibTable
zxDslIpoaUserInfoTable = _ZxDslIpoaUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoTable.setStatus("current")
_ZxDslIpoaUserInfoEntry_Object = MibTableRow
zxDslIpoaUserInfoEntry = _ZxDslIpoaUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1)
)
zxDslIpoaUserInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZTE-DSL-IPOA-MIB", "zxDslIpoaUserInfoBrgPortId"),
)
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoEntry.setStatus("current")
_ZxDslIpoaUserInfoBrgPortId_Type = Integer32
_ZxDslIpoaUserInfoBrgPortId_Object = MibTableColumn
zxDslIpoaUserInfoBrgPortId = _ZxDslIpoaUserInfoBrgPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1, 1),
    _ZxDslIpoaUserInfoBrgPortId_Type()
)
zxDslIpoaUserInfoBrgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoBrgPortId.setStatus("current")
_ZxDslIpoaUserInfoVlan_Type = Integer32
_ZxDslIpoaUserInfoVlan_Object = MibTableColumn
zxDslIpoaUserInfoVlan = _ZxDslIpoaUserInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1, 2),
    _ZxDslIpoaUserInfoVlan_Type()
)
zxDslIpoaUserInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoVlan.setStatus("current")
_ZxDslIpoaUserInfoIp_Type = IpAddress
_ZxDslIpoaUserInfoIp_Object = MibTableColumn
zxDslIpoaUserInfoIp = _ZxDslIpoaUserInfoIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1, 3),
    _ZxDslIpoaUserInfoIp_Type()
)
zxDslIpoaUserInfoIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoIp.setStatus("current")
_ZxDslIpoaUserInfoMac_Type = MacAddress
_ZxDslIpoaUserInfoMac_Object = MibTableColumn
zxDslIpoaUserInfoMac = _ZxDslIpoaUserInfoMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1, 4),
    _ZxDslIpoaUserInfoMac_Type()
)
zxDslIpoaUserInfoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoMac.setStatus("current")
_ZxDslIpoaUserInfoGatewayIp_Type = IpAddress
_ZxDslIpoaUserInfoGatewayIp_Object = MibTableColumn
zxDslIpoaUserInfoGatewayIp = _ZxDslIpoaUserInfoGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1, 5),
    _ZxDslIpoaUserInfoGatewayIp_Type()
)
zxDslIpoaUserInfoGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoGatewayIp.setStatus("current")
_ZxDslIpoaUserInfoGatewayMac_Type = MacAddress
_ZxDslIpoaUserInfoGatewayMac_Object = MibTableColumn
zxDslIpoaUserInfoGatewayMac = _ZxDslIpoaUserInfoGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 44, 1, 2, 2, 1, 6),
    _ZxDslIpoaUserInfoGatewayMac_Type()
)
zxDslIpoaUserInfoGatewayMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIpoaUserInfoGatewayMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-IPOA-MIB",
    **{"zxDslIpoaMib": zxDslIpoaMib,
       "zxDslIpoaMibObjects": zxDslIpoaMibObjects,
       "zxDslIpoaGlobalObjects": zxDslIpoaGlobalObjects,
       "zxDslIpoaDefGateway": zxDslIpoaDefGateway,
       "zxDslIpoaQueryInterval": zxDslIpoaQueryInterval,
       "zxDslIpoaGatewayARPInterval": zxDslIpoaGatewayARPInterval,
       "zxDslIpoaUser": zxDslIpoaUser,
       "zxDslIpoaUserConfTable": zxDslIpoaUserConfTable,
       "zxDslIpoaUserConfEntry": zxDslIpoaUserConfEntry,
       "zxDslIpoaUserConfBrgPortId": zxDslIpoaUserConfBrgPortId,
       "zxDslIpoaUserConfIp": zxDslIpoaUserConfIp,
       "zxDslIpoaUserConfInAtmArp": zxDslIpoaUserConfInAtmArp,
       "zxDslIpoaUserConfLayer": zxDslIpoaUserConfLayer,
       "zxDslIpoaUserConfL2gatewayIp": zxDslIpoaUserConfL2gatewayIp,
       "zxDslIpoaUserConfL2gatewayMac": zxDslIpoaUserConfL2gatewayMac,
       "zxDslIpoaUserConfRowStatus": zxDslIpoaUserConfRowStatus,
       "zxDslIpoaUserInfoTable": zxDslIpoaUserInfoTable,
       "zxDslIpoaUserInfoEntry": zxDslIpoaUserInfoEntry,
       "zxDslIpoaUserInfoBrgPortId": zxDslIpoaUserInfoBrgPortId,
       "zxDslIpoaUserInfoVlan": zxDslIpoaUserInfoVlan,
       "zxDslIpoaUserInfoIp": zxDslIpoaUserInfoIp,
       "zxDslIpoaUserInfoMac": zxDslIpoaUserInfoMac,
       "zxDslIpoaUserInfoGatewayIp": zxDslIpoaUserInfoGatewayIp,
       "zxDslIpoaUserInfoGatewayMac": zxDslIpoaUserInfoGatewayMac}
)
