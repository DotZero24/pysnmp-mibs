# SNMP MIB module (NTWS-REGISTRATION-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NTWS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:15 2025
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

(ntwsRegistration,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsRegistration")

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

ntwsRegistrationChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 5)
)
if mibBuilder.loadTexts:
    ntwsRegistrationChassisMib.setRevisions(
        ("2007-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsChassisComponents_ObjectIdentity = ObjectIdentity
ntwsChassisComponents = _NtwsChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4)
)
_NtwsChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
ntwsChasCompPowerSupplies = _NtwsChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1)
)
_NtwsChasCompPowerSupply1_ObjectIdentity = ObjectIdentity
ntwsChasCompPowerSupply1 = _NtwsChasCompPowerSupply1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 1)
)
_NtwsChasCompPowerSupply2_ObjectIdentity = ObjectIdentity
ntwsChasCompPowerSupply2 = _NtwsChasCompPowerSupply2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 1, 2)
)
_NtwsChasCompFans_ObjectIdentity = ObjectIdentity
ntwsChasCompFans = _NtwsChasCompFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2)
)
_NtwsChasCompFan1_ObjectIdentity = ObjectIdentity
ntwsChasCompFan1 = _NtwsChasCompFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 1)
)
_NtwsChasCompFan2_ObjectIdentity = ObjectIdentity
ntwsChasCompFan2 = _NtwsChasCompFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 2)
)
_NtwsChasCompFan3_ObjectIdentity = ObjectIdentity
ntwsChasCompFan3 = _NtwsChasCompFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-REGISTRATION-CHASSIS-MIB",
    **{"ntwsChassisComponents": ntwsChassisComponents,
       "ntwsChasCompPowerSupplies": ntwsChasCompPowerSupplies,
       "ntwsChasCompPowerSupply1": ntwsChasCompPowerSupply1,
       "ntwsChasCompPowerSupply2": ntwsChasCompPowerSupply2,
       "ntwsChasCompFans": ntwsChasCompFans,
       "ntwsChasCompFan1": ntwsChasCompFan1,
       "ntwsChasCompFan2": ntwsChasCompFan2,
       "ntwsChasCompFan3": ntwsChasCompFan3,
       "ntwsRegistrationChassisMib": ntwsRegistrationChassisMib}
)
