# SNMP MIB module (LEFTHAND-NETWORKS-GLOBAL-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-GLOBAL-REG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:10 2025
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

lhnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1)
)
if mibBuilder.loadTexts:
    lhnMIB.setRevisions(
        ("2013-11-21 00:00",
         "2013-06-25 00:00",
         "2012-09-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lefthandnetworks_ObjectIdentity = ObjectIdentity
lefthandnetworks = _Lefthandnetworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804)
)
_LhnMIBNotifications_ObjectIdentity = ObjectIdentity
lhnMIBNotifications = _LhnMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 0)
)
_LhnMIBObjects_ObjectIdentity = ObjectIdentity
lhnMIBObjects = _LhnMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1)
)
_LhnMIBConformance_ObjectIdentity = ObjectIdentity
lhnMIBConformance = _LhnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 2)
)
_LhnMIBCompliances_ObjectIdentity = ObjectIdentity
lhnMIBCompliances = _LhnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 2, 1)
)
_LhnMIBGroups_ObjectIdentity = ObjectIdentity
lhnMIBGroups = _LhnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 2, 2)
)
_LefthandnetworksRegistrations_ObjectIdentity = ObjectIdentity
lefthandnetworksRegistrations = _LefthandnetworksRegistrations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2)
)
_LhnModules_ObjectIdentity = ObjectIdentity
lhnModules = _LhnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1)
)
if mibBuilder.loadTexts:
    lhnModules.setStatus("current")
_LefthandnetworksProducts_ObjectIdentity = ObjectIdentity
lefthandnetworksProducts = _LefthandnetworksProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3)
)
_LhnNsm_ObjectIdentity = ObjectIdentity
lhnNsm = _LhnNsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1)
)
if mibBuilder.loadTexts:
    lhnNsm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    **{"lefthandnetworks": lefthandnetworks,
       "lhnMIB": lhnMIB,
       "lhnMIBNotifications": lhnMIBNotifications,
       "lhnMIBObjects": lhnMIBObjects,
       "lhnMIBConformance": lhnMIBConformance,
       "lhnMIBCompliances": lhnMIBCompliances,
       "lhnMIBGroups": lhnMIBGroups,
       "lefthandnetworksRegistrations": lefthandnetworksRegistrations,
       "lhnModules": lhnModules,
       "lefthandnetworksProducts": lefthandnetworksProducts,
       "lhnNsm": lhnNsm}
)
