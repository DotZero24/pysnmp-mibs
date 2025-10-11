# SNMP MIB module (FS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:45 2025
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

(fsGatewayProducts,) = mibBuilder.importSymbols(
    "FS-GATEWAY-SMI",
    "fsGatewayProducts")

(fsRouterProducts,) = mibBuilder.importSymbols(
    "FS-ROUTER-SMI",
    "fsRouterProducts")

(fsSmartClassProducts,) = mibBuilder.importSymbols(
    "FS-SMARTCLASS-SMI",
    "fsSmartClassProducts")

(fsModules,
 fsSwitchProducts) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsModules",
    "fsSwitchProducts")

(fsSoftwareProducts,) = mibBuilder.importSymbols(
    "FS-SOFTWARE-SMI",
    "fsSoftwareProducts")

(fsWirelessProducts,) = mibBuilder.importSymbols(
    "FS-WIRELESS-SMI",
    "fsWirelessProducts")

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

fsProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 4, 1)
)
if mibBuilder.loadTexts:
    fsProductsMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5860_20SQ_ObjectIdentity = ObjectIdentity
S5860_20SQ = _S5860_20SQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1, 1)
)
_S5860_24XB_U_ObjectIdentity = ObjectIdentity
S5860_24XB_U = _S5860_24XB_U_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-PRODUCTS-MIB",
    **{"S5860-20SQ": S5860_20SQ,
       "S5860-24XB-U": S5860_24XB_U,
       "fsProductsMIB": fsProductsMIB}
)
