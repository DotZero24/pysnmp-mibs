# SNMP MIB module (TPLINK-DHCPSNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-DHCPSNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:53 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27)
)
if mibBuilder.loadTexts:
    tplinkDhcpSnoopingMIB.setRevisions(
        ("2012-12-17 10:14",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
tplinkDhcpSnoopingMIBObjects = _TplinkDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1)
)
_DhcpSnoopingGlobalConfig_ObjectIdentity = ObjectIdentity
dhcpSnoopingGlobalConfig = _DhcpSnoopingGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1)
)


class _DhcpSnoopingEnable_Type(Integer32):
    """Custom type dhcpSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpSnoopingEnable_Type.__name__ = "Integer32"
_DhcpSnoopingEnable_Object = MibScalar
dhcpSnoopingEnable = _DhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 1),
    _DhcpSnoopingEnable_Type()
)
dhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingEnable.setStatus("current")
_DhcpSnoopingVlanConfigTable_Object = MibTable
dhcpSnoopingVlanConfigTable = _DhcpSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpSnoopingVlanConfigTable.setStatus("current")
_DhcpSnoopingVlanConfigEntry_Object = MibTableRow
dhcpSnoopingVlanConfigEntry = _DhcpSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2, 1)
)
dhcpSnoopingVlanConfigEntry.setIndexNames(
    (0, "TPLINK-DHCPSNOOPING-MIB", "dhcpSnoopingVlanId"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingVlanConfigEntry.setStatus("current")


class _DhcpSnoopingVlanId_Type(Integer32):
    """Custom type dhcpSnoopingVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DhcpSnoopingVlanId_Type.__name__ = "Integer32"
_DhcpSnoopingVlanId_Object = MibTableColumn
dhcpSnoopingVlanId = _DhcpSnoopingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2, 1, 1),
    _DhcpSnoopingVlanId_Type()
)
dhcpSnoopingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanId.setStatus("current")


class _DhcpSnoopingVlanStatus_Type(Integer32):
    """Custom type dhcpSnoopingVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_DhcpSnoopingVlanStatus_Type.__name__ = "Integer32"
_DhcpSnoopingVlanStatus_Object = MibTableColumn
dhcpSnoopingVlanStatus = _DhcpSnoopingVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 1, 2, 1, 2),
    _DhcpSnoopingVlanStatus_Type()
)
dhcpSnoopingVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingVlanStatus.setStatus("current")
_DhcpSnoopingPortConfig_ObjectIdentity = ObjectIdentity
dhcpSnoopingPortConfig = _DhcpSnoopingPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3)
)
_DhcpSnoopingPortConfigTable_Object = MibTable
dhcpSnoopingPortConfigTable = _DhcpSnoopingPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigTable.setStatus("current")
_DhcpSnoopingPortConfigEntry_Object = MibTableRow
dhcpSnoopingPortConfigEntry = _DhcpSnoopingPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1)
)
dhcpSnoopingPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigEntry.setStatus("current")


class _DhcpSnoopingPort_Type(OctetString):
    """Custom type dhcpSnoopingPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpSnoopingPort_Type.__name__ = "OctetString"
_DhcpSnoopingPort_Object = MibTableColumn
dhcpSnoopingPort = _DhcpSnoopingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 1),
    _DhcpSnoopingPort_Type()
)
dhcpSnoopingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPort.setStatus("current")
_DhcpSnoopingPortConfigMaxEntry_Type = Integer32
_DhcpSnoopingPortConfigMaxEntry_Object = MibTableColumn
dhcpSnoopingPortConfigMaxEntry = _DhcpSnoopingPortConfigMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 2),
    _DhcpSnoopingPortConfigMaxEntry_Type()
)
dhcpSnoopingPortConfigMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigMaxEntry.setStatus("current")


class _DhcpSnoopingPortConfigPortLag_Type(OctetString):
    """Custom type dhcpSnoopingPortConfigPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DhcpSnoopingPortConfigPortLag_Type.__name__ = "OctetString"
_DhcpSnoopingPortConfigPortLag_Object = MibTableColumn
dhcpSnoopingPortConfigPortLag = _DhcpSnoopingPortConfigPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 1, 3, 1, 1, 3),
    _DhcpSnoopingPortConfigPortLag_Type()
)
dhcpSnoopingPortConfigPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopingPortConfigPortLag.setStatus("current")
_TplinkDhcpSnoopingNotifications_ObjectIdentity = ObjectIdentity
tplinkDhcpSnoopingNotifications = _TplinkDhcpSnoopingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 27, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-DHCPSNOOPING-MIB",
    **{"tplinkDhcpSnoopingMIB": tplinkDhcpSnoopingMIB,
       "tplinkDhcpSnoopingMIBObjects": tplinkDhcpSnoopingMIBObjects,
       "dhcpSnoopingGlobalConfig": dhcpSnoopingGlobalConfig,
       "dhcpSnoopingEnable": dhcpSnoopingEnable,
       "dhcpSnoopingVlanConfigTable": dhcpSnoopingVlanConfigTable,
       "dhcpSnoopingVlanConfigEntry": dhcpSnoopingVlanConfigEntry,
       "dhcpSnoopingVlanId": dhcpSnoopingVlanId,
       "dhcpSnoopingVlanStatus": dhcpSnoopingVlanStatus,
       "dhcpSnoopingPortConfig": dhcpSnoopingPortConfig,
       "dhcpSnoopingPortConfigTable": dhcpSnoopingPortConfigTable,
       "dhcpSnoopingPortConfigEntry": dhcpSnoopingPortConfigEntry,
       "dhcpSnoopingPort": dhcpSnoopingPort,
       "dhcpSnoopingPortConfigMaxEntry": dhcpSnoopingPortConfigMaxEntry,
       "dhcpSnoopingPortConfigPortLag": dhcpSnoopingPortConfigPortLag,
       "tplinkDhcpSnoopingNotifications": tplinkDhcpSnoopingNotifications}
)
