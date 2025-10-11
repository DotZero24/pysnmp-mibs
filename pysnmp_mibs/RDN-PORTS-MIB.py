# SNMP MIB module (RDN-PORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/riverdelta/RDN-PORTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:41 2025
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

(rdnDefinitions,) = mibBuilder.importSymbols(
    "RDN-DEFINITIONS-MIB",
    "rdnDefinitions")

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


# MODULE-IDENTITY

rdnPorts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5)
)
if mibBuilder.loadTexts:
    rdnPorts.setRevisions(
        ("2008-08-08 00:00",
         "2005-10-20 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-05-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnPortsUnknown_ObjectIdentity = ObjectIdentity
rdnPortsUnknown = _RdnPortsUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 0)
)
_RdnPortsGige_ObjectIdentity = ObjectIdentity
rdnPortsGige = _RdnPortsGige_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 1)
)
_RdnPortsEthernet_ObjectIdentity = ObjectIdentity
rdnPortsEthernet = _RdnPortsEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 2)
)
_RdnPortsCableMac_ObjectIdentity = ObjectIdentity
rdnPortsCableMac = _RdnPortsCableMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 3)
)
_RdnPortsCableUpstream_ObjectIdentity = ObjectIdentity
rdnPortsCableUpstream = _RdnPortsCableUpstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 4)
)
_RdnPortsCableDownstream_ObjectIdentity = ObjectIdentity
rdnPortsCableDownstream = _RdnPortsCableDownstream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 5)
)
_RdnPortsCableSubIf_ObjectIdentity = ObjectIdentity
rdnPortsCableSubIf = _RdnPortsCableSubIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 6)
)
_RdnPortsLoopback_ObjectIdentity = ObjectIdentity
rdnPortsLoopback = _RdnPortsLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 7)
)
_RdnPortsT1_ObjectIdentity = ObjectIdentity
rdnPortsT1 = _RdnPortsT1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 8)
)
_RdnPortsNull_ObjectIdentity = ObjectIdentity
rdnPortsNull = _RdnPortsNull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 9)
)
_RdnPortsTunnel_ObjectIdentity = ObjectIdentity
rdnPortsTunnel = _RdnPortsTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 10)
)
_RdnPortsPOS_ObjectIdentity = ObjectIdentity
rdnPortsPOS = _RdnPortsPOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 11)
)
_RdnPortsATM_ObjectIdentity = ObjectIdentity
rdnPortsATM = _RdnPortsATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 5, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-PORTS-MIB",
    **{"rdnPorts": rdnPorts,
       "rdnPortsUnknown": rdnPortsUnknown,
       "rdnPortsGige": rdnPortsGige,
       "rdnPortsEthernet": rdnPortsEthernet,
       "rdnPortsCableMac": rdnPortsCableMac,
       "rdnPortsCableUpstream": rdnPortsCableUpstream,
       "rdnPortsCableDownstream": rdnPortsCableDownstream,
       "rdnPortsCableSubIf": rdnPortsCableSubIf,
       "rdnPortsLoopback": rdnPortsLoopback,
       "rdnPortsT1": rdnPortsT1,
       "rdnPortsNull": rdnPortsNull,
       "rdnPortsTunnel": rdnPortsTunnel,
       "rdnPortsPOS": rdnPortsPOS,
       "rdnPortsATM": rdnPortsATM}
)
