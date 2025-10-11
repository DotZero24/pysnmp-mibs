# SNMP MIB module (TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trapeze/TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:24 2025
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

(trpzRegistration,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzRegistration")


# MODULE-IDENTITY

trpzRegistrationChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 5)
)
if mibBuilder.loadTexts:
    trpzRegistrationChassisMib.setRevisions(
        ("2007-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrpzChassisComponents_ObjectIdentity = ObjectIdentity
trpzChassisComponents = _TrpzChassisComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4)
)
_TrpzChasCompPowerSupplies_ObjectIdentity = ObjectIdentity
trpzChasCompPowerSupplies = _TrpzChasCompPowerSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 1)
)
_TrpzChasCompPowerSupply1_ObjectIdentity = ObjectIdentity
trpzChasCompPowerSupply1 = _TrpzChasCompPowerSupply1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 1)
)
_TrpzChasCompPowerSupply2_ObjectIdentity = ObjectIdentity
trpzChasCompPowerSupply2 = _TrpzChasCompPowerSupply2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 1, 2)
)
_TrpzChasCompFans_ObjectIdentity = ObjectIdentity
trpzChasCompFans = _TrpzChasCompFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2)
)
_TrpzChasCompFan1_ObjectIdentity = ObjectIdentity
trpzChasCompFan1 = _TrpzChasCompFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 1)
)
_TrpzChasCompFan2_ObjectIdentity = ObjectIdentity
trpzChasCompFan2 = _TrpzChasCompFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 2)
)
_TrpzChasCompFan3_ObjectIdentity = ObjectIdentity
trpzChasCompFan3 = _TrpzChasCompFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 3, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-REGISTRATION-CHASSIS-MIB",
    **{"trpzChassisComponents": trpzChassisComponents,
       "trpzChasCompPowerSupplies": trpzChasCompPowerSupplies,
       "trpzChasCompPowerSupply1": trpzChasCompPowerSupply1,
       "trpzChasCompPowerSupply2": trpzChasCompPowerSupply2,
       "trpzChasCompFans": trpzChasCompFans,
       "trpzChasCompFan1": trpzChasCompFan1,
       "trpzChasCompFan2": trpzChasCompFan2,
       "trpzChasCompFan3": trpzChasCompFan3,
       "trpzRegistrationChassisMib": trpzRegistrationChassisMib}
)
