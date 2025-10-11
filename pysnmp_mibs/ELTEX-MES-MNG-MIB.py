# SNMP MIB module (ELTEX-MES-MNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-MNG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:08 2025
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

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

_EltMesFtp_ObjectIdentity = ObjectIdentity
eltMesFtp = _EltMesFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 2)
)
_EltMesAAAStatMIB_ObjectIdentity = ObjectIdentity
eltMesAAAStatMIB = _EltMesAAAStatMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 3)
)
_EltMesSnmpCommExtMIB_ObjectIdentity = ObjectIdentity
eltMesSnmpCommExtMIB = _EltMesSnmpCommExtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 4)
)
_EltMesMacNotificationMIB_ObjectIdentity = ObjectIdentity
eltMesMacNotificationMIB = _EltMesMacNotificationMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 7)
)
_EltMesCountersMIB_ObjectIdentity = ObjectIdentity
eltMesCountersMIB = _EltMesCountersMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 8)
)
_EltMesCpuTasksUtilMIB_ObjectIdentity = ObjectIdentity
eltMesCpuTasksUtilMIB = _EltMesCpuTasksUtilMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 9)
)
_EltMesSystemExtMIB_ObjectIdentity = ObjectIdentity
eltMesSystemExtMIB = _EltMesSystemExtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 10)
)
_EltMesIfExtensionMIB_ObjectIdentity = ObjectIdentity
eltMesIfExtensionMIB = _EltMesIfExtensionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 276)
)
_EltMesBridgeExtMIB_ObjectIdentity = ObjectIdentity
eltMesBridgeExtMIB = _EltMesBridgeExtMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401)
)
_EltMesSwitchRateLimiterMIB_ObjectIdentity = ObjectIdentity
eltMesSwitchRateLimiterMIB = _EltMesSwitchRateLimiterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 773)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-MNG-MIB",
    **{"eltMesFtp": eltMesFtp,
       "eltMesAAAStatMIB": eltMesAAAStatMIB,
       "eltMesSnmpCommExtMIB": eltMesSnmpCommExtMIB,
       "eltMesMacNotificationMIB": eltMesMacNotificationMIB,
       "eltMesCountersMIB": eltMesCountersMIB,
       "eltMesCpuTasksUtilMIB": eltMesCpuTasksUtilMIB,
       "eltMesSystemExtMIB": eltMesSystemExtMIB,
       "eltMesIfExtensionMIB": eltMesIfExtensionMIB,
       "eltMesBridgeExtMIB": eltMesBridgeExtMIB,
       "eltMesSwitchRateLimiterMIB": eltMesSwitchRateLimiterMIB}
)
