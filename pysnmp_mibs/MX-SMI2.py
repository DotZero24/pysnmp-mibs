# SNMP MIB module (MX-SMI2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SMI2
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:56 2025
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

(mediatrix,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrix")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MediatrixSystem_ObjectIdentity = ObjectIdentity
mediatrixSystem = _MediatrixSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000)
)
if mibBuilder.loadTexts:
    mediatrixSystem.setStatus("current")
_Gen5_ObjectIdentity = ObjectIdentity
gen5 = _Gen5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100)
)
if mibBuilder.loadTexts:
    gen5.setStatus("current")
_MediatrixProducts_ObjectIdentity = ObjectIdentity
mediatrixProducts = _MediatrixProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 100)
)
if mibBuilder.loadTexts:
    mediatrixProducts.setStatus("current")
_MediatrixCommon_ObjectIdentity = ObjectIdentity
mediatrixCommon = _MediatrixCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200)
)
if mibBuilder.loadTexts:
    mediatrixCommon.setStatus("current")
_MediatrixServices_ObjectIdentity = ObjectIdentity
mediatrixServices = _MediatrixServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100)
)
if mibBuilder.loadTexts:
    mediatrixServices.setStatus("current")
_MediatrixHardware_ObjectIdentity = ObjectIdentity
mediatrixHardware = _MediatrixHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500)
)
if mibBuilder.loadTexts:
    mediatrixHardware.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SMI2",
    **{"mediatrixSystem": mediatrixSystem,
       "gen5": gen5,
       "mediatrixProducts": mediatrixProducts,
       "mediatrixCommon": mediatrixCommon,
       "mediatrixServices": mediatrixServices,
       "mediatrixHardware": mediatrixHardware}
)
