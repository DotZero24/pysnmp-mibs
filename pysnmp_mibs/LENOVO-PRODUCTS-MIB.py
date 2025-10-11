# SNMP MIB module (LENOVO-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ibm/LENOVO-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:12:49 2025
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

(lenovoModules,
 lenovoProducts) = mibBuilder.importSymbols(
    "LENOVO-SMI-MIB",
    "lenovoModules",
    "lenovoProducts")

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

lenovoProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 4, 1)
)
if mibBuilder.loadTexts:
    lenovoProductsMIB.setRevisions(
        ("2016-04-20 00:00",
         "2017-05-01 00:00",
         "2017-05-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tor_ObjectIdentity = ObjectIdentity
tor = _Tor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7)
)
if mibBuilder.loadTexts:
    tor.setStatus("current")
_G8296_ObjectIdentity = ObjectIdentity
g8296 = _G8296_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 22)
)
_G8272_ObjectIdentity = ObjectIdentity
g8272 = _G8272_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 24)
)
_G8296_cnos_ObjectIdentity = ObjectIdentity
g8296_cnos = _G8296_cnos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 29)
)
_G8272_cnos_ObjectIdentity = ObjectIdentity
g8272_cnos = _G8272_cnos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 30)
)
_G8332_cnos_ObjectIdentity = ObjectIdentity
g8332_cnos = _G8332_cnos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 31)
)
_Ne1032_ObjectIdentity = ObjectIdentity
ne1032 = _Ne1032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 32)
)
_Ne1032t_ObjectIdentity = ObjectIdentity
ne1032t = _Ne1032t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 33)
)
_Ne1072t_ObjectIdentity = ObjectIdentity
ne1072t = _Ne1072t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 34)
)
_Ne1072_ObjectIdentity = ObjectIdentity
ne1072 = _Ne1072_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 35)
)
_Ne10032_ObjectIdentity = ObjectIdentity
ne10032 = _Ne10032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 36)
)
_Ce0128t_ObjectIdentity = ObjectIdentity
ce0128t = _Ce0128t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 37)
)
_Ce0128p_ObjectIdentity = ObjectIdentity
ce0128p = _Ce0128p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 38)
)
_Ce0152t_ObjectIdentity = ObjectIdentity
ce0152t = _Ce0152t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 39)
)
_Ne1072tv2_ObjectIdentity = ObjectIdentity
ne1072tv2 = _Ne1072tv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 40)
)
_Ne2572_ObjectIdentity = ObjectIdentity
ne2572 = _Ne2572_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 41)
)
_Ne0152t_ObjectIdentity = ObjectIdentity
ne0152t = _Ne0152t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 7, 42)
)
_LenovoServerProducts_ObjectIdentity = ObjectIdentity
lenovoServerProducts = _LenovoServerProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 11)
)
if mibBuilder.loadTexts:
    lenovoServerProducts.setStatus("current")
_Flex_ObjectIdentity = ObjectIdentity
flex = _Flex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 18)
)
if mibBuilder.loadTexts:
    flex.setStatus("current")
_Si4091_ObjectIdentity = ObjectIdentity
si4091 = _Si4091_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19046, 1, 18, 23)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LENOVO-PRODUCTS-MIB",
    **{"tor": tor,
       "g8296": g8296,
       "g8272": g8272,
       "g8296-cnos": g8296_cnos,
       "g8272-cnos": g8272_cnos,
       "g8332-cnos": g8332_cnos,
       "ne1032": ne1032,
       "ne1032t": ne1032t,
       "ne1072t": ne1072t,
       "ne1072": ne1072,
       "ne10032": ne10032,
       "ce0128t": ce0128t,
       "ce0128p": ce0128p,
       "ce0152t": ce0152t,
       "ne1072tv2": ne1072tv2,
       "ne2572": ne2572,
       "ne0152t": ne0152t,
       "lenovoServerProducts": lenovoServerProducts,
       "flex": flex,
       "si4091": si4091,
       "lenovoProductsMIB": lenovoProductsMIB}
)
