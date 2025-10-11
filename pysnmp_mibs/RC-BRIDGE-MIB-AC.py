# SNMP MIB module (RC-BRIDGE-MIB-AC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RC-BRIDGE-MIB-AC
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:40 2025
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

(ruggedcomAgentCapability,) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomAgentCapability")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

ruggedcomBridgeACModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 3)
)
if mibBuilder.loadTexts:
    ruggedcomBridgeACModule.setRevisions(
        ("2014-02-22 17:00",
         "2011-02-22 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ruggedcomBridgeAC = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 3, 1)
)
if mibBuilder.loadTexts:
    ruggedcomBridgeAC.setProductRelease("ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomBridgeAC.setStatus(
        "current"
    )

ruggedcomBridgeAC01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 3, 2)
)
if mibBuilder.loadTexts:
    ruggedcomBridgeAC01.setProductRelease("Ruggedcom ROX 2.4.1")
if mibBuilder.loadTexts:
    ruggedcomBridgeAC01.setStatus(
        "current"
    )

ruggedcomBridgeAC02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 3, 3)
)
if mibBuilder.loadTexts:
    ruggedcomBridgeAC02.setProductRelease("ROS-MB")
if mibBuilder.loadTexts:
    ruggedcomBridgeAC02.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-BRIDGE-MIB-AC",
    **{"ruggedcomBridgeACModule": ruggedcomBridgeACModule,
       "ruggedcomBridgeAC": ruggedcomBridgeAC,
       "ruggedcomBridgeAC01": ruggedcomBridgeAC01,
       "ruggedcomBridgeAC02": ruggedcomBridgeAC02}
)
