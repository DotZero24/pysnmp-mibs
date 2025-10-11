# SNMP MIB module (ZYXEL-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-MULTICAST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:01:47 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMulticastSetup_ObjectIdentity = ObjectIdentity
zyxelMulticastSetup = _ZyxelMulticastSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1)
)


class _ZyMulticastUnknownMulticastFrameForwarding_Type(Integer32):
    """Custom type zyMulticastUnknownMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2),
          ("drop-vlan", 3))
    )


_ZyMulticastUnknownMulticastFrameForwarding_Type.__name__ = "Integer32"
_ZyMulticastUnknownMulticastFrameForwarding_Object = MibScalar
zyMulticastUnknownMulticastFrameForwarding = _ZyMulticastUnknownMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 1),
    _ZyMulticastUnknownMulticastFrameForwarding_Type()
)
zyMulticastUnknownMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameForwarding.setStatus("current")


class _ZyMulticastReservedMulticastFrameForwarding_Type(Integer32):
    """Custom type zyMulticastReservedMulticastFrameForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flooding", 1),
          ("drop", 2))
    )


_ZyMulticastReservedMulticastFrameForwarding_Type.__name__ = "Integer32"
_ZyMulticastReservedMulticastFrameForwarding_Object = MibScalar
zyMulticastReservedMulticastFrameForwarding = _ZyMulticastReservedMulticastFrameForwarding_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 2),
    _ZyMulticastReservedMulticastFrameForwarding_Type()
)
zyMulticastReservedMulticastFrameForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastReservedMulticastFrameForwarding.setStatus("current")


class _ZyMulticastUnknownMulticastFrameDropVlan1k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameDropVlan1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameDropVlan1k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameDropVlan1k_Object = MibScalar
zyMulticastUnknownMulticastFrameDropVlan1k = _ZyMulticastUnknownMulticastFrameDropVlan1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 3),
    _ZyMulticastUnknownMulticastFrameDropVlan1k_Type()
)
zyMulticastUnknownMulticastFrameDropVlan1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameDropVlan1k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameDropVlan2k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameDropVlan2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameDropVlan2k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameDropVlan2k_Object = MibScalar
zyMulticastUnknownMulticastFrameDropVlan2k = _ZyMulticastUnknownMulticastFrameDropVlan2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 4),
    _ZyMulticastUnknownMulticastFrameDropVlan2k_Type()
)
zyMulticastUnknownMulticastFrameDropVlan2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameDropVlan2k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameDropVlan3k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameDropVlan3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameDropVlan3k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameDropVlan3k_Object = MibScalar
zyMulticastUnknownMulticastFrameDropVlan3k = _ZyMulticastUnknownMulticastFrameDropVlan3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 5),
    _ZyMulticastUnknownMulticastFrameDropVlan3k_Type()
)
zyMulticastUnknownMulticastFrameDropVlan3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameDropVlan3k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameDropVlan4k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameDropVlan4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameDropVlan4k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameDropVlan4k_Object = MibScalar
zyMulticastUnknownMulticastFrameDropVlan4k = _ZyMulticastUnknownMulticastFrameDropVlan4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 6),
    _ZyMulticastUnknownMulticastFrameDropVlan4k_Type()
)
zyMulticastUnknownMulticastFrameDropVlan4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameDropVlan4k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameToQuerierPort_Type(Integer32):
    """Custom type zyMulticastUnknownMulticastFrameToQuerierPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forwarding", 2),
          ("forwarding-vlan", 3))
    )


_ZyMulticastUnknownMulticastFrameToQuerierPort_Type.__name__ = "Integer32"
_ZyMulticastUnknownMulticastFrameToQuerierPort_Object = MibScalar
zyMulticastUnknownMulticastFrameToQuerierPort = _ZyMulticastUnknownMulticastFrameToQuerierPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 7),
    _ZyMulticastUnknownMulticastFrameToQuerierPort_Type()
)
zyMulticastUnknownMulticastFrameToQuerierPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameToQuerierPort.setStatus("current")


class _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k_Object = MibScalar
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k = _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 8),
    _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k_Type()
)
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k_Object = MibScalar
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k = _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 9),
    _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k_Type()
)
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k_Object = MibScalar
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k = _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 10),
    _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k_Type()
)
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k.setStatus("current")


class _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k_Type(OctetString):
    """Custom type zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k_Type.__name__ = "OctetString"
_ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k_Object = MibScalar
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k = _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 54, 1, 11),
    _ZyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k_Type()
)
zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MULTICAST-MIB",
    **{"zyxelMulticast": zyxelMulticast,
       "zyxelMulticastSetup": zyxelMulticastSetup,
       "zyMulticastUnknownMulticastFrameForwarding": zyMulticastUnknownMulticastFrameForwarding,
       "zyMulticastReservedMulticastFrameForwarding": zyMulticastReservedMulticastFrameForwarding,
       "zyMulticastUnknownMulticastFrameDropVlan1k": zyMulticastUnknownMulticastFrameDropVlan1k,
       "zyMulticastUnknownMulticastFrameDropVlan2k": zyMulticastUnknownMulticastFrameDropVlan2k,
       "zyMulticastUnknownMulticastFrameDropVlan3k": zyMulticastUnknownMulticastFrameDropVlan3k,
       "zyMulticastUnknownMulticastFrameDropVlan4k": zyMulticastUnknownMulticastFrameDropVlan4k,
       "zyMulticastUnknownMulticastFrameToQuerierPort": zyMulticastUnknownMulticastFrameToQuerierPort,
       "zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k": zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan1k,
       "zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k": zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan2k,
       "zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k": zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan3k,
       "zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k": zyMulticastUnknownMulticastFrameToQuerierPortForwardingVlan4k}
)
