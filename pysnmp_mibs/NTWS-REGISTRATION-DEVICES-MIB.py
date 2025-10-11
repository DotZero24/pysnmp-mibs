# SNMP MIB module (NTWS-REGISTRATION-DEVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NTWS-REGISTRATION-DEVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:26 2025
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

ntwsRegistrationDevicesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 6)
)
if mibBuilder.loadTexts:
    ntwsRegistrationDevicesMib.setRevisions(
        ("2008-08-08 00:01",
         "2007-08-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsWirelessSwitch_ObjectIdentity = ObjectIdentity
ntwsWirelessSwitch = _NtwsWirelessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1)
)
_NtwsSwitch2360_ObjectIdentity = ObjectIdentity
ntwsSwitch2360 = _NtwsSwitch2360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 2)
)
_NtwsSwitch2380_ObjectIdentity = ObjectIdentity
ntwsSwitch2380 = _NtwsSwitch2380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 3)
)
_NtwsSwitch2350_ObjectIdentity = ObjectIdentity
ntwsSwitch2350 = _NtwsSwitch2350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 4)
)
_NtwsSwitch2372_ObjectIdentity = ObjectIdentity
ntwsSwitch2372 = _NtwsSwitch2372_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 5)
)
_NtwsSwitch2382_ObjectIdentity = ObjectIdentity
ntwsSwitch2382 = _NtwsSwitch2382_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 6)
)
_NtwsSwitch2800_ObjectIdentity = ObjectIdentity
ntwsSwitch2800 = _NtwsSwitch2800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3, 1, 7)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-REGISTRATION-DEVICES-MIB",
    **{"ntwsWirelessSwitch": ntwsWirelessSwitch,
       "ntwsSwitch2360": ntwsSwitch2360,
       "ntwsSwitch2380": ntwsSwitch2380,
       "ntwsSwitch2350": ntwsSwitch2350,
       "ntwsSwitch2372": ntwsSwitch2372,
       "ntwsSwitch2382": ntwsSwitch2382,
       "ntwsSwitch2800": ntwsSwitch2800,
       "ntwsRegistrationDevicesMib": ntwsRegistrationDevicesMib}
)
