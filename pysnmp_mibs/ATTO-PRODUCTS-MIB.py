# SNMP MIB module (ATTO-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/atto/ATTO-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:14:22 2025
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

attoProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 3, 2)
)
if mibBuilder.loadTexts:
    attoProductsMIB.setRevisions(
        ("2013-04-19 13:45",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Attotech_ObjectIdentity = ObjectIdentity
attotech = _Attotech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547)
)
_AttoProducts_ObjectIdentity = ObjectIdentity
attoProducts = _AttoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1)
)
_AttoGenericDevice_ObjectIdentity = ObjectIdentity
attoGenericDevice = _AttoGenericDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 1)
)
_AttoHba_ObjectIdentity = ObjectIdentity
attoHba = _AttoHba_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 3)
)
_AttoFB6500_ObjectIdentity = ObjectIdentity
attoFB6500 = _AttoFB6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 4)
)
_AttoFB6500N_ObjectIdentity = ObjectIdentity
attoFB6500N = _AttoFB6500N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 1, 5)
)
_AttoMgmt_ObjectIdentity = ObjectIdentity
attoMgmt = _AttoMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 2)
)
_AttoModules_ObjectIdentity = ObjectIdentity
attoModules = _AttoModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 3)
)
_AttoAgentCapability_ObjectIdentity = ObjectIdentity
attoAgentCapability = _AttoAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4547, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATTO-PRODUCTS-MIB",
    **{"attotech": attotech,
       "attoProducts": attoProducts,
       "attoGenericDevice": attoGenericDevice,
       "attoHba": attoHba,
       "attoFB6500": attoFB6500,
       "attoFB6500N": attoFB6500N,
       "attoMgmt": attoMgmt,
       "attoModules": attoModules,
       "attoProductsMIB": attoProductsMIB,
       "attoAgentCapability": attoAgentCapability}
)
