# SNMP MIB module (RBTWS-REGISTRATION-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cabletron/RBTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:55:27 2025
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

(rbtwsRegistration,) = mibBuilder.importSymbols(
    "RBTWS-ROOT-MIB",
    "rbtwsRegistration")

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

rbtwsRegistrationDevicesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 6)
)
if mibBuilder.loadTexts:
    rbtwsRegistrationDevicesMib.setRevisions(
        ("2007-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbtwsWirelessSwitch_ObjectIdentity = ObjectIdentity
rbtwsWirelessSwitch = _RbtwsWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1)
)
_RbtwsSwitch8100_ObjectIdentity = ObjectIdentity
rbtwsSwitch8100 = _RbtwsSwitch8100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 1)
)
_RbtwsSwitch8200_ObjectIdentity = ObjectIdentity
rbtwsSwitch8200 = _RbtwsSwitch8200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 2)
)
_RbtwsSwitch8400_ObjectIdentity = ObjectIdentity
rbtwsSwitch8400 = _RbtwsSwitch8400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 3)
)
_RbtwsSwitch8110_ObjectIdentity = ObjectIdentity
rbtwsSwitch8110 = _RbtwsSwitch8110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 4)
)
_RbtwsSwitch8500_ObjectIdentity = ObjectIdentity
rbtwsSwitch8500 = _RbtwsSwitch8500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-REGISTRATION-DEVICES-MIB",
    **{"rbtwsWirelessSwitch": rbtwsWirelessSwitch,
       "rbtwsSwitch8100": rbtwsSwitch8100,
       "rbtwsSwitch8200": rbtwsSwitch8200,
       "rbtwsSwitch8400": rbtwsSwitch8400,
       "rbtwsSwitch8110": rbtwsSwitch8110,
       "rbtwsSwitch8500": rbtwsSwitch8500,
       "rbtwsRegistrationDevicesMib": rbtwsRegistrationDevicesMib}
)
