# SNMP MIB module (ELTEX-MES-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:11 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(rldot1dStpTrapVrblVID,
 rldot1dStpTrapVrblifIndex) = mibBuilder.importSymbols(
    "RADLAN-BRIDGEMIBOBJECTS-MIB",
    "rldot1dStpTrapVrblVID",
    "rldot1dStpTrapVrblifIndex")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

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

eltMesNotifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0)
)
if mibBuilder.loadTexts:
    eltMesNotifications.setRevisions(
        ("2012-07-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

eltdot1dStpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 7)
)
eltdot1dStpTopologyChange.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    eltdot1dStpTopologyChange.setStatus(
        "current"
    )

eltdot1dStpRootBridgeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 8)
)
eltdot1dStpRootBridgeChange.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    eltdot1dStpRootBridgeChange.setStatus(
        "current"
    )

eltdot1dStpTcProtectionThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 9)
)
eltdot1dStpTcProtectionThresholdReached.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    eltdot1dStpTcProtectionThresholdReached.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-TRAPS-MIB",
    **{"eltMesNotifications": eltMesNotifications,
       "eltdot1dStpTopologyChange": eltdot1dStpTopologyChange,
       "eltdot1dStpRootBridgeChange": eltdot1dStpRootBridgeChange,
       "eltdot1dStpTcProtectionThresholdReached": eltdot1dStpTcProtectionThresholdReached}
)
