# SNMP MIB module (Accton-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/edgecore/Accton-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:54:05 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Accton_ObjectIdentity = ObjectIdentity
accton = _Accton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259)
)
_Edgecorenetworks_ObjectIdentity = ObjectIdentity
edgecorenetworks = _Edgecorenetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10)
)
_EdgeCoreNetworksMgt_ObjectIdentity = ObjectIdentity
edgeCoreNetworksMgt = _EdgeCoreNetworksMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1)
)
_Ecs5510_48sMIB_ObjectIdentity = ObjectIdentity
ecs5510_48sMIB = _Ecs5510_48sMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14)
)
_Rnd_ObjectIdentity = ObjectIdentity
rnd = _Rnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Accton-MIB",
    **{"accton": accton,
       "edgecorenetworks": edgecorenetworks,
       "edgeCoreNetworksMgt": edgeCoreNetworksMgt,
       "ecs5510-48sMIB": ecs5510_48sMIB,
       "rnd": rnd}
)
