# SNMP MIB module (RC-RUGGEDCOM-SYS-INFO-MIB-AC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RC-RUGGEDCOM-SYS-INFO-MIB-AC
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:27 2025
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

ruggedcomRcSysinfoACModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoACModule.setRevisions(
        ("2017-11-02 11:00",
         "2017-02-15 10:00",
         "2013-11-13 17:00",
         "2012-08-30 17:00",
         "2012-06-01 17:00",
         "2011-02-22 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ruggedcomRcSysinfoAC = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 1)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC.setProductRelease("ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC.setStatus(
        "obsolete"
    )

ruggedcomRcSysinfoAC01 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 2)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC01.setProductRelease("ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC01.setStatus(
        "obsolete"
    )

ruggedcomRcSysinfoAC02 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 3)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC02.setProductRelease("ROS-CF52")
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC02.setStatus(
        "obsolete"
    )

ruggedcomRcSysinfoAC03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 4)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC03.setProductRelease("Ruggedcom ROX 2.4.1")
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC03.setStatus(
        "current"
    )

ruggedcomRcSysinfoAC04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 5)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC04.setProductRelease("Ruggedcom ROX II")
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC04.setStatus(
        "current"
    )

ruggedcomRcSysinfoAC05 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 30, 12, 6)
)
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC05.setProductRelease("ROS-CF52 and ROS-MPC83")
if mibBuilder.loadTexts:
    ruggedcomRcSysinfoAC05.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC-RUGGEDCOM-SYS-INFO-MIB-AC",
    **{"ruggedcomRcSysinfoACModule": ruggedcomRcSysinfoACModule,
       "ruggedcomRcSysinfoAC": ruggedcomRcSysinfoAC,
       "ruggedcomRcSysinfoAC01": ruggedcomRcSysinfoAC01,
       "ruggedcomRcSysinfoAC02": ruggedcomRcSysinfoAC02,
       "ruggedcomRcSysinfoAC03": ruggedcomRcSysinfoAC03,
       "ruggedcomRcSysinfoAC04": ruggedcomRcSysinfoAC04,
       "ruggedcomRcSysinfoAC05": ruggedcomRcSysinfoAC05}
)
