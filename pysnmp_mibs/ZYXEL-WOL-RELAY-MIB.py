# SNMP MIB module (ZYXEL-WOL-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-WOL-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:10 2025
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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelWolRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelWolRelaySetup_ObjectIdentity = ObjectIdentity
zyxelWolRelaySetup = _ZyxelWolRelaySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1)
)
_ZyMaxNumberOfWolRelayEntry_Type = Integer32
_ZyMaxNumberOfWolRelayEntry_Object = MibScalar
zyMaxNumberOfWolRelayEntry = _ZyMaxNumberOfWolRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 1),
    _ZyMaxNumberOfWolRelayEntry_Type()
)
zyMaxNumberOfWolRelayEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMaxNumberOfWolRelayEntry.setStatus("current")
_ZyxelWolRelayTable_Object = MibTable
zyxelWolRelayTable = _ZyxelWolRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelWolRelayTable.setStatus("current")
_ZyxelWolRelayEntry_Object = MibTableRow
zyxelWolRelayEntry = _ZyxelWolRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1)
)
zyxelWolRelayEntry.setIndexNames(
    (0, "ZYXEL-WOL-RELAY-MIB", "zyWolRelayUdpPort"),
)
if mibBuilder.loadTexts:
    zyxelWolRelayEntry.setStatus("current")


class _ZyWolRelayUdpPort_Type(Integer32):
    """Custom type zyWolRelayUdpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZyWolRelayUdpPort_Type.__name__ = "Integer32"
_ZyWolRelayUdpPort_Object = MibTableColumn
zyWolRelayUdpPort = _ZyWolRelayUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 1),
    _ZyWolRelayUdpPort_Type()
)
zyWolRelayUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyWolRelayUdpPort.setStatus("current")


class _ZyWolRelaySourceVlanMap1k_Type(OctetString):
    """Custom type zyWolRelaySourceVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelaySourceVlanMap1k_Type.__name__ = "OctetString"
_ZyWolRelaySourceVlanMap1k_Object = MibTableColumn
zyWolRelaySourceVlanMap1k = _ZyWolRelaySourceVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 2),
    _ZyWolRelaySourceVlanMap1k_Type()
)
zyWolRelaySourceVlanMap1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelaySourceVlanMap1k.setStatus("current")


class _ZyWolRelaySourceVlanMap2k_Type(OctetString):
    """Custom type zyWolRelaySourceVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelaySourceVlanMap2k_Type.__name__ = "OctetString"
_ZyWolRelaySourceVlanMap2k_Object = MibTableColumn
zyWolRelaySourceVlanMap2k = _ZyWolRelaySourceVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 3),
    _ZyWolRelaySourceVlanMap2k_Type()
)
zyWolRelaySourceVlanMap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelaySourceVlanMap2k.setStatus("current")


class _ZyWolRelaySourceVlanMap3k_Type(OctetString):
    """Custom type zyWolRelaySourceVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelaySourceVlanMap3k_Type.__name__ = "OctetString"
_ZyWolRelaySourceVlanMap3k_Object = MibTableColumn
zyWolRelaySourceVlanMap3k = _ZyWolRelaySourceVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 4),
    _ZyWolRelaySourceVlanMap3k_Type()
)
zyWolRelaySourceVlanMap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelaySourceVlanMap3k.setStatus("current")


class _ZyWolRelaySourceVlanMap4k_Type(OctetString):
    """Custom type zyWolRelaySourceVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelaySourceVlanMap4k_Type.__name__ = "OctetString"
_ZyWolRelaySourceVlanMap4k_Object = MibTableColumn
zyWolRelaySourceVlanMap4k = _ZyWolRelaySourceVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 5),
    _ZyWolRelaySourceVlanMap4k_Type()
)
zyWolRelaySourceVlanMap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelaySourceVlanMap4k.setStatus("current")


class _ZyWolRelayDestinationVlanMap1k_Type(OctetString):
    """Custom type zyWolRelayDestinationVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelayDestinationVlanMap1k_Type.__name__ = "OctetString"
_ZyWolRelayDestinationVlanMap1k_Object = MibTableColumn
zyWolRelayDestinationVlanMap1k = _ZyWolRelayDestinationVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 6),
    _ZyWolRelayDestinationVlanMap1k_Type()
)
zyWolRelayDestinationVlanMap1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelayDestinationVlanMap1k.setStatus("current")


class _ZyWolRelayDestinationVlanMap2k_Type(OctetString):
    """Custom type zyWolRelayDestinationVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelayDestinationVlanMap2k_Type.__name__ = "OctetString"
_ZyWolRelayDestinationVlanMap2k_Object = MibTableColumn
zyWolRelayDestinationVlanMap2k = _ZyWolRelayDestinationVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 7),
    _ZyWolRelayDestinationVlanMap2k_Type()
)
zyWolRelayDestinationVlanMap2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelayDestinationVlanMap2k.setStatus("current")


class _ZyWolRelayDestinationVlanMap3k_Type(OctetString):
    """Custom type zyWolRelayDestinationVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelayDestinationVlanMap3k_Type.__name__ = "OctetString"
_ZyWolRelayDestinationVlanMap3k_Object = MibTableColumn
zyWolRelayDestinationVlanMap3k = _ZyWolRelayDestinationVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 8),
    _ZyWolRelayDestinationVlanMap3k_Type()
)
zyWolRelayDestinationVlanMap3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelayDestinationVlanMap3k.setStatus("current")


class _ZyWolRelayDestinationVlanMap4k_Type(OctetString):
    """Custom type zyWolRelayDestinationVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyWolRelayDestinationVlanMap4k_Type.__name__ = "OctetString"
_ZyWolRelayDestinationVlanMap4k_Object = MibTableColumn
zyWolRelayDestinationVlanMap4k = _ZyWolRelayDestinationVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 9),
    _ZyWolRelayDestinationVlanMap4k_Type()
)
zyWolRelayDestinationVlanMap4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyWolRelayDestinationVlanMap4k.setStatus("current")
_ZyWolRelayRowStatus_Type = RowStatus
_ZyWolRelayRowStatus_Object = MibTableColumn
zyWolRelayRowStatus = _ZyWolRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 116, 1, 2, 1, 10),
    _ZyWolRelayRowStatus_Type()
)
zyWolRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyWolRelayRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-WOL-RELAY-MIB",
    **{"zyxelWolRelay": zyxelWolRelay,
       "zyxelWolRelaySetup": zyxelWolRelaySetup,
       "zyMaxNumberOfWolRelayEntry": zyMaxNumberOfWolRelayEntry,
       "zyxelWolRelayTable": zyxelWolRelayTable,
       "zyxelWolRelayEntry": zyxelWolRelayEntry,
       "zyWolRelayUdpPort": zyWolRelayUdpPort,
       "zyWolRelaySourceVlanMap1k": zyWolRelaySourceVlanMap1k,
       "zyWolRelaySourceVlanMap2k": zyWolRelaySourceVlanMap2k,
       "zyWolRelaySourceVlanMap3k": zyWolRelaySourceVlanMap3k,
       "zyWolRelaySourceVlanMap4k": zyWolRelaySourceVlanMap4k,
       "zyWolRelayDestinationVlanMap1k": zyWolRelayDestinationVlanMap1k,
       "zyWolRelayDestinationVlanMap2k": zyWolRelayDestinationVlanMap2k,
       "zyWolRelayDestinationVlanMap3k": zyWolRelayDestinationVlanMap3k,
       "zyWolRelayDestinationVlanMap4k": zyWolRelayDestinationVlanMap4k,
       "zyWolRelayRowStatus": zyWolRelayRowStatus}
)
