# SNMP MIB module (RUCKUS-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-TUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:36 2025
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

(ruckusCommonTunnelModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonTunnelModule")

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

ruckusTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusTunnelObjects_ObjectIdentity = ObjectIdentity
ruckusTunnelObjects = _RuckusTunnelObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1)
)
_RuckusTunnelInfo_ObjectIdentity = ObjectIdentity
ruckusTunnelInfo = _RuckusTunnelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1)
)
_RuckusTunnelSoftGREConfigInfo_ObjectIdentity = ObjectIdentity
ruckusTunnelSoftGREConfigInfo = _RuckusTunnelSoftGREConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3)
)
_RuckusTunnelSoftGREConfigTable_Object = MibTable
ruckusTunnelSoftGREConfigTable = _RuckusTunnelSoftGREConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREConfigTable.setStatus("current")
_RuckusTunnelSoftGREEntry_Object = MibTableRow
ruckusTunnelSoftGREEntry = _RuckusTunnelSoftGREEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3, 1, 1)
)
ruckusTunnelSoftGREEntry.setIndexNames(
    (0, "RUCKUS-TUNNEL-MIB", "ruckusTunnelSoftGREIndex"),
)
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREEntry.setStatus("current")


class _RuckusTunnelSoftGREAdminEnable_Type(Integer32):
    """Custom type ruckusTunnelSoftGREAdminEnable based on Integer32"""
    defaultValue = 2

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


_RuckusTunnelSoftGREAdminEnable_Type.__name__ = "Integer32"
_RuckusTunnelSoftGREAdminEnable_Object = MibTableColumn
ruckusTunnelSoftGREAdminEnable = _RuckusTunnelSoftGREAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3, 1, 1, 1),
    _RuckusTunnelSoftGREAdminEnable_Type()
)
ruckusTunnelSoftGREAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREAdminEnable.setStatus("current")


class _RuckusTunnelSoftGREPrimaryGatewayAddress_Type(OctetString):
    """Custom type ruckusTunnelSoftGREPrimaryGatewayAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusTunnelSoftGREPrimaryGatewayAddress_Type.__name__ = "OctetString"
_RuckusTunnelSoftGREPrimaryGatewayAddress_Object = MibTableColumn
ruckusTunnelSoftGREPrimaryGatewayAddress = _RuckusTunnelSoftGREPrimaryGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3, 1, 1, 2),
    _RuckusTunnelSoftGREPrimaryGatewayAddress_Type()
)
ruckusTunnelSoftGREPrimaryGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREPrimaryGatewayAddress.setStatus("current")


class _RuckusTunnelSoftGRESecondaryGatewayAddress_Type(OctetString):
    """Custom type ruckusTunnelSoftGRESecondaryGatewayAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusTunnelSoftGRESecondaryGatewayAddress_Type.__name__ = "OctetString"
_RuckusTunnelSoftGRESecondaryGatewayAddress_Object = MibTableColumn
ruckusTunnelSoftGRESecondaryGatewayAddress = _RuckusTunnelSoftGRESecondaryGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3, 1, 1, 3),
    _RuckusTunnelSoftGRESecondaryGatewayAddress_Type()
)
ruckusTunnelSoftGRESecondaryGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGRESecondaryGatewayAddress.setStatus("current")
_RuckusTunnelSoftGREIndex_Type = Unsigned32
_RuckusTunnelSoftGREIndex_Object = MibTableColumn
ruckusTunnelSoftGREIndex = _RuckusTunnelSoftGREIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 3, 1, 1, 200),
    _RuckusTunnelSoftGREIndex_Type()
)
ruckusTunnelSoftGREIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREIndex.setStatus("current")
_RuckusTunnelSoftGREStatusInfo_ObjectIdentity = ObjectIdentity
ruckusTunnelSoftGREStatusInfo = _RuckusTunnelSoftGREStatusInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5)
)
_RuckusTunnelSoftGREStatusTable_Object = MibTable
ruckusTunnelSoftGREStatusTable = _RuckusTunnelSoftGREStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREStatusTable.setStatus("current")
_RuckusTunnelSoftGREStatusEntry_Object = MibTableRow
ruckusTunnelSoftGREStatusEntry = _RuckusTunnelSoftGREStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1, 1)
)
ruckusTunnelSoftGREStatusEntry.setIndexNames(
    (0, "RUCKUS-TUNNEL-MIB", "ruckusTunnelSoftGREStatusIndex"),
)
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREStatusEntry.setStatus("current")


class _RuckusTunnelSoftGRECurrentActivePeerIp_Type(OctetString):
    """Custom type ruckusTunnelSoftGRECurrentActivePeerIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusTunnelSoftGRECurrentActivePeerIp_Type.__name__ = "OctetString"
_RuckusTunnelSoftGRECurrentActivePeerIp_Object = MibTableColumn
ruckusTunnelSoftGRECurrentActivePeerIp = _RuckusTunnelSoftGRECurrentActivePeerIp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1, 1, 1),
    _RuckusTunnelSoftGRECurrentActivePeerIp_Type()
)
ruckusTunnelSoftGRECurrentActivePeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGRECurrentActivePeerIp.setStatus("current")


class _RuckusTunnelSoftGREUptime_Type(DisplayString):
    """Custom type ruckusTunnelSoftGREUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusTunnelSoftGREUptime_Type.__name__ = "DisplayString"
_RuckusTunnelSoftGREUptime_Object = MibTableColumn
ruckusTunnelSoftGREUptime = _RuckusTunnelSoftGREUptime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1, 1, 2),
    _RuckusTunnelSoftGREUptime_Type()
)
ruckusTunnelSoftGREUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREUptime.setStatus("current")
_RuckusTunnelSoftGREKeepAliveDropCounter_Type = Counter32
_RuckusTunnelSoftGREKeepAliveDropCounter_Object = MibTableColumn
ruckusTunnelSoftGREKeepAliveDropCounter = _RuckusTunnelSoftGREKeepAliveDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1, 1, 3),
    _RuckusTunnelSoftGREKeepAliveDropCounter_Type()
)
ruckusTunnelSoftGREKeepAliveDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREKeepAliveDropCounter.setStatus("current")
_RuckusTunnelSoftGRETunnelChangeCounter_Type = Counter32
_RuckusTunnelSoftGRETunnelChangeCounter_Object = MibTableColumn
ruckusTunnelSoftGRETunnelChangeCounter = _RuckusTunnelSoftGRETunnelChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1, 1, 4),
    _RuckusTunnelSoftGRETunnelChangeCounter_Type()
)
ruckusTunnelSoftGRETunnelChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGRETunnelChangeCounter.setStatus("current")
_RuckusTunnelSoftGREStatusIndex_Type = Unsigned32
_RuckusTunnelSoftGREStatusIndex_Object = MibTableColumn
ruckusTunnelSoftGREStatusIndex = _RuckusTunnelSoftGREStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 18, 1, 1, 1, 5, 1, 1, 200),
    _RuckusTunnelSoftGREStatusIndex_Type()
)
ruckusTunnelSoftGREStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusTunnelSoftGREStatusIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-TUNNEL-MIB",
    **{"ruckusTunnelMIB": ruckusTunnelMIB,
       "ruckusTunnelObjects": ruckusTunnelObjects,
       "ruckusTunnelInfo": ruckusTunnelInfo,
       "ruckusTunnelSoftGREConfigInfo": ruckusTunnelSoftGREConfigInfo,
       "ruckusTunnelSoftGREConfigTable": ruckusTunnelSoftGREConfigTable,
       "ruckusTunnelSoftGREEntry": ruckusTunnelSoftGREEntry,
       "ruckusTunnelSoftGREAdminEnable": ruckusTunnelSoftGREAdminEnable,
       "ruckusTunnelSoftGREPrimaryGatewayAddress": ruckusTunnelSoftGREPrimaryGatewayAddress,
       "ruckusTunnelSoftGRESecondaryGatewayAddress": ruckusTunnelSoftGRESecondaryGatewayAddress,
       "ruckusTunnelSoftGREIndex": ruckusTunnelSoftGREIndex,
       "ruckusTunnelSoftGREStatusInfo": ruckusTunnelSoftGREStatusInfo,
       "ruckusTunnelSoftGREStatusTable": ruckusTunnelSoftGREStatusTable,
       "ruckusTunnelSoftGREStatusEntry": ruckusTunnelSoftGREStatusEntry,
       "ruckusTunnelSoftGRECurrentActivePeerIp": ruckusTunnelSoftGRECurrentActivePeerIp,
       "ruckusTunnelSoftGREUptime": ruckusTunnelSoftGREUptime,
       "ruckusTunnelSoftGREKeepAliveDropCounter": ruckusTunnelSoftGREKeepAliveDropCounter,
       "ruckusTunnelSoftGRETunnelChangeCounter": ruckusTunnelSoftGRETunnelChangeCounter,
       "ruckusTunnelSoftGREStatusIndex": ruckusTunnelSoftGREStatusIndex}
)
