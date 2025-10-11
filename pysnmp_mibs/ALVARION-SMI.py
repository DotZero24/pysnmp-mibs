# SNMP MIB module (ALVARION-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/ALVARION-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:20 2025
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

alvarionWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionProducts_ObjectIdentity = ObjectIdentity
alvarionProducts = _AlvarionProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alvarionProducts.setStatus("current")
_AlvarionExperiment_ObjectIdentity = ObjectIdentity
alvarionExperiment = _AlvarionExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 3)
)
if mibBuilder.loadTexts:
    alvarionExperiment.setStatus("current")
_AlvarionModules_ObjectIdentity = ObjectIdentity
alvarionModules = _AlvarionModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 4)
)
if mibBuilder.loadTexts:
    alvarionModules.setStatus("current")
_AlvarionMgmtV2_ObjectIdentity = ObjectIdentity
alvarionMgmtV2 = _AlvarionMgmtV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5)
)
if mibBuilder.loadTexts:
    alvarionMgmtV2.setStatus("current")
_Variation_ObjectIdentity = ObjectIdentity
variation = _Variation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 7)
)
if mibBuilder.loadTexts:
    variation.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-SMI",
    **{"alvarionWireless": alvarionWireless,
       "alvarionProducts": alvarionProducts,
       "alvarionExperiment": alvarionExperiment,
       "alvarionModules": alvarionModules,
       "alvarionMgmtV2": alvarionMgmtV2,
       "variation": variation}
)
