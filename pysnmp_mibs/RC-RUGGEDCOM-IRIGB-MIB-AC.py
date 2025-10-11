# SNMP MIB module (RC-RUGGEDCOM-IRIGB-MIB-AC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RC-RUGGEDCOM-IRIGB-MIB-AC
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:45 2025
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

ruggedcomRcIrigbACModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbACModule.setRevisions(
        ("2015-10-30 17:00",
         "2014-12-05 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ruggedcomRcIrigbAC = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 1)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC.setStatus(
        "current"
    )

ruggedcomRcIrigbAC01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 2)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC01.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC01.setStatus(
        "current"
    )

ruggedcomRcIrigbAC02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 3)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC02.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC02.setStatus(
        "current"
    )

ruggedcomRcIrigbAC03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 4)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC03.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC03.setStatus(
        "current"
    )

ruggedcomRcIrigbAC04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 5)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC04.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC04.setStatus(
        "current"
    )

ruggedcomRcIrigbAC05 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 6)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC05.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC05.setStatus(
        "current"
    )

ruggedcomRcIrigbAC06 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 43, 7)
)
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC06.setProductRelease("ROS-MPC83 and ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcIrigbAC06.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-RUGGEDCOM-IRIGB-MIB-AC",
    **{"ruggedcomRcIrigbACModule": ruggedcomRcIrigbACModule,
       "ruggedcomRcIrigbAC": ruggedcomRcIrigbAC,
       "ruggedcomRcIrigbAC01": ruggedcomRcIrigbAC01,
       "ruggedcomRcIrigbAC02": ruggedcomRcIrigbAC02,
       "ruggedcomRcIrigbAC03": ruggedcomRcIrigbAC03,
       "ruggedcomRcIrigbAC04": ruggedcomRcIrigbAC04,
       "ruggedcomRcIrigbAC05": ruggedcomRcIrigbAC05,
       "ruggedcomRcIrigbAC06": ruggedcomRcIrigbAC06}
)
