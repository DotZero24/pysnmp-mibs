# SNMP MIB module (JUNIPER-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/junose/JUNIPER-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 21:39:26 2025
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

juniperMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636)
)
if mibBuilder.loadTexts:
    juniperMIB.setRevisions(
        ("2003-04-17 01:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxProducts_ObjectIdentity = ObjectIdentity
jnxProducts = _JnxProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 1)
)
if mibBuilder.loadTexts:
    jnxProducts.setStatus("current")
_JnxServices_ObjectIdentity = ObjectIdentity
jnxServices = _JnxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 2)
)
if mibBuilder.loadTexts:
    jnxServices.setStatus("current")
_JnxMibs_ObjectIdentity = ObjectIdentity
jnxMibs = _JnxMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3)
)
if mibBuilder.loadTexts:
    jnxMibs.setStatus("current")
_JnxTraps_ObjectIdentity = ObjectIdentity
jnxTraps = _JnxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4)
)
if mibBuilder.loadTexts:
    jnxTraps.setStatus("current")
_JnxChassisTraps_ObjectIdentity = ObjectIdentity
jnxChassisTraps = _JnxChassisTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 1)
)
_JnxChassisOKTraps_ObjectIdentity = ObjectIdentity
jnxChassisOKTraps = _JnxChassisOKTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 2)
)
_JnxRmonTraps_ObjectIdentity = ObjectIdentity
jnxRmonTraps = _JnxRmonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 3)
)
_JnxLdpTraps_ObjectIdentity = ObjectIdentity
jnxLdpTraps = _JnxLdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 4)
)
_JnxCmNotifications_ObjectIdentity = ObjectIdentity
jnxCmNotifications = _JnxCmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 5)
)
_JnxSonetNotifications_ObjectIdentity = ObjectIdentity
jnxSonetNotifications = _JnxSonetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 6)
)
_JnxPMonNotifications_ObjectIdentity = ObjectIdentity
jnxPMonNotifications = _JnxPMonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 4, 7)
)
_JnxExperiment_ObjectIdentity = ObjectIdentity
jnxExperiment = _JnxExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SMI",
    **{"juniperMIB": juniperMIB,
       "jnxProducts": jnxProducts,
       "jnxServices": jnxServices,
       "jnxMibs": jnxMibs,
       "jnxTraps": jnxTraps,
       "jnxChassisTraps": jnxChassisTraps,
       "jnxChassisOKTraps": jnxChassisOKTraps,
       "jnxRmonTraps": jnxRmonTraps,
       "jnxLdpTraps": jnxLdpTraps,
       "jnxCmNotifications": jnxCmNotifications,
       "jnxSonetNotifications": jnxSonetNotifications,
       "jnxPMonNotifications": jnxPMonNotifications,
       "jnxExperiment": jnxExperiment}
)
