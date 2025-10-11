# SNMP MIB module (ZTE-AN-IPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-IPOA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:00 2025
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnIpoaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnIpoaMibObjects_ObjectIdentity = ObjectIdentity
zxAnIpoaMibObjects = _ZxAnIpoaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1)
)
_ZxAnIpoaDefGateway_Type = IpAddress
_ZxAnIpoaDefGateway_Object = MibScalar
zxAnIpoaDefGateway = _ZxAnIpoaDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 1),
    _ZxAnIpoaDefGateway_Type()
)
zxAnIpoaDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIpoaDefGateway.setStatus("current")
_ZxAnIpoaQueryInterval_Type = Integer32
_ZxAnIpoaQueryInterval_Object = MibScalar
zxAnIpoaQueryInterval = _ZxAnIpoaQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 2),
    _ZxAnIpoaQueryInterval_Type()
)
zxAnIpoaQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIpoaQueryInterval.setStatus("current")
_ZxAnIpoaGatewayARPInterval_Type = Integer32
_ZxAnIpoaGatewayARPInterval_Object = MibScalar
zxAnIpoaGatewayARPInterval = _ZxAnIpoaGatewayARPInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 3),
    _ZxAnIpoaGatewayARPInterval_Type()
)
zxAnIpoaGatewayARPInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnIpoaGatewayARPInterval.setStatus("current")
_ZxAnIpoaUserConfTable_Object = MibTable
zxAnIpoaUserConfTable = _ZxAnIpoaUserConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10)
)
if mibBuilder.loadTexts:
    zxAnIpoaUserConfTable.setStatus("current")
_ZxAnIpoaUserConfEntry_Object = MibTableRow
zxAnIpoaUserConfEntry = _ZxAnIpoaUserConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1)
)
zxAnIpoaUserConfEntry.setIndexNames(
    (0, "ZTE-AN-IPOA-MIB", "zxAnIpoaIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnIpoaUserConfEntry.setStatus("current")
_ZxAnIpoaIfIndex_Type = ZxAnIfindex
_ZxAnIpoaIfIndex_Object = MibTableColumn
zxAnIpoaIfIndex = _ZxAnIpoaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 1),
    _ZxAnIpoaIfIndex_Type()
)
zxAnIpoaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnIpoaIfIndex.setStatus("current")
_ZxAnIpoaUserConfIp_Type = IpAddress
_ZxAnIpoaUserConfIp_Object = MibTableColumn
zxAnIpoaUserConfIp = _ZxAnIpoaUserConfIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 2),
    _ZxAnIpoaUserConfIp_Type()
)
zxAnIpoaUserConfIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpoaUserConfIp.setStatus("current")


class _ZxAnIpoaUserConfInAtmArp_Type(Integer32):
    """Custom type zxAnIpoaUserConfInAtmArp based on Integer32"""
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


_ZxAnIpoaUserConfInAtmArp_Type.__name__ = "Integer32"
_ZxAnIpoaUserConfInAtmArp_Object = MibTableColumn
zxAnIpoaUserConfInAtmArp = _ZxAnIpoaUserConfInAtmArp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 3),
    _ZxAnIpoaUserConfInAtmArp_Type()
)
zxAnIpoaUserConfInAtmArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpoaUserConfInAtmArp.setStatus("current")


class _ZxAnIpoaUserConfLayer_Type(Integer32):
    """Custom type zxAnIpoaUserConfLayer based on Integer32"""
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


_ZxAnIpoaUserConfLayer_Type.__name__ = "Integer32"
_ZxAnIpoaUserConfLayer_Object = MibTableColumn
zxAnIpoaUserConfLayer = _ZxAnIpoaUserConfLayer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 4),
    _ZxAnIpoaUserConfLayer_Type()
)
zxAnIpoaUserConfLayer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpoaUserConfLayer.setStatus("current")
_ZxAnIpoaUserConfL2gatewayIp_Type = IpAddress
_ZxAnIpoaUserConfL2gatewayIp_Object = MibTableColumn
zxAnIpoaUserConfL2gatewayIp = _ZxAnIpoaUserConfL2gatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 5),
    _ZxAnIpoaUserConfL2gatewayIp_Type()
)
zxAnIpoaUserConfL2gatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpoaUserConfL2gatewayIp.setStatus("current")
_ZxAnIpoaUserConfL2gatewayMac_Type = MacAddress
_ZxAnIpoaUserConfL2gatewayMac_Object = MibTableColumn
zxAnIpoaUserConfL2gatewayMac = _ZxAnIpoaUserConfL2gatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 6),
    _ZxAnIpoaUserConfL2gatewayMac_Type()
)
zxAnIpoaUserConfL2gatewayMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpoaUserConfL2gatewayMac.setStatus("current")
_ZxAnIpoaUserConfRowStatus_Type = RowStatus
_ZxAnIpoaUserConfRowStatus_Object = MibTableColumn
zxAnIpoaUserConfRowStatus = _ZxAnIpoaUserConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 10, 1, 7),
    _ZxAnIpoaUserConfRowStatus_Type()
)
zxAnIpoaUserConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnIpoaUserConfRowStatus.setStatus("current")
_ZxAnIpoaUserInfoTable_Object = MibTable
zxAnIpoaUserInfoTable = _ZxAnIpoaUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11)
)
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoTable.setStatus("current")
_ZxAnIpoaUserInfoEntry_Object = MibTableRow
zxAnIpoaUserInfoEntry = _ZxAnIpoaUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11, 1)
)
zxAnIpoaUserInfoEntry.setIndexNames(
    (0, "ZTE-AN-IPOA-MIB", "zxAnIpoaIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoEntry.setStatus("current")
_ZxAnIpoaUserInfoVlan_Type = Integer32
_ZxAnIpoaUserInfoVlan_Object = MibTableColumn
zxAnIpoaUserInfoVlan = _ZxAnIpoaUserInfoVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11, 1, 1),
    _ZxAnIpoaUserInfoVlan_Type()
)
zxAnIpoaUserInfoVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoVlan.setStatus("current")
_ZxAnIpoaUserInfoIp_Type = IpAddress
_ZxAnIpoaUserInfoIp_Object = MibTableColumn
zxAnIpoaUserInfoIp = _ZxAnIpoaUserInfoIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11, 1, 2),
    _ZxAnIpoaUserInfoIp_Type()
)
zxAnIpoaUserInfoIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoIp.setStatus("current")
_ZxAnIpoaUserInfoMac_Type = MacAddress
_ZxAnIpoaUserInfoMac_Object = MibTableColumn
zxAnIpoaUserInfoMac = _ZxAnIpoaUserInfoMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11, 1, 3),
    _ZxAnIpoaUserInfoMac_Type()
)
zxAnIpoaUserInfoMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoMac.setStatus("current")
_ZxAnIpoaUserInfoGatewayIp_Type = IpAddress
_ZxAnIpoaUserInfoGatewayIp_Object = MibTableColumn
zxAnIpoaUserInfoGatewayIp = _ZxAnIpoaUserInfoGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11, 1, 4),
    _ZxAnIpoaUserInfoGatewayIp_Type()
)
zxAnIpoaUserInfoGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoGatewayIp.setStatus("current")
_ZxAnIpoaUserInfoGatewayMac_Type = MacAddress
_ZxAnIpoaUserInfoGatewayMac_Object = MibTableColumn
zxAnIpoaUserInfoGatewayMac = _ZxAnIpoaUserInfoGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 33, 1, 11, 1, 5),
    _ZxAnIpoaUserInfoGatewayMac_Type()
)
zxAnIpoaUserInfoGatewayMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnIpoaUserInfoGatewayMac.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-IPOA-MIB",
    **{"zxAnIpoaMib": zxAnIpoaMib,
       "zxAnIpoaMibObjects": zxAnIpoaMibObjects,
       "zxAnIpoaDefGateway": zxAnIpoaDefGateway,
       "zxAnIpoaQueryInterval": zxAnIpoaQueryInterval,
       "zxAnIpoaGatewayARPInterval": zxAnIpoaGatewayARPInterval,
       "zxAnIpoaUserConfTable": zxAnIpoaUserConfTable,
       "zxAnIpoaUserConfEntry": zxAnIpoaUserConfEntry,
       "zxAnIpoaIfIndex": zxAnIpoaIfIndex,
       "zxAnIpoaUserConfIp": zxAnIpoaUserConfIp,
       "zxAnIpoaUserConfInAtmArp": zxAnIpoaUserConfInAtmArp,
       "zxAnIpoaUserConfLayer": zxAnIpoaUserConfLayer,
       "zxAnIpoaUserConfL2gatewayIp": zxAnIpoaUserConfL2gatewayIp,
       "zxAnIpoaUserConfL2gatewayMac": zxAnIpoaUserConfL2gatewayMac,
       "zxAnIpoaUserConfRowStatus": zxAnIpoaUserConfRowStatus,
       "zxAnIpoaUserInfoTable": zxAnIpoaUserInfoTable,
       "zxAnIpoaUserInfoEntry": zxAnIpoaUserInfoEntry,
       "zxAnIpoaUserInfoVlan": zxAnIpoaUserInfoVlan,
       "zxAnIpoaUserInfoIp": zxAnIpoaUserInfoIp,
       "zxAnIpoaUserInfoMac": zxAnIpoaUserInfoMac,
       "zxAnIpoaUserInfoGatewayIp": zxAnIpoaUserInfoGatewayIp,
       "zxAnIpoaUserInfoGatewayMac": zxAnIpoaUserInfoGatewayMac}
)
