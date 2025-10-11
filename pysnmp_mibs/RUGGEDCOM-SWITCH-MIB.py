# SNMP MIB module (RUGGEDCOM-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-SWITCH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:33 2025
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

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

(ruggedcomAgentCapabilities,
 ruggedcomProducts) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomAgentCapabilities",
    "ruggedcomProducts")

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

ruggedcomSwitchModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 1)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchModule.setRevisions(
        ("2011-05-01 17:00",
         "2009-05-15 17:00",
         "2008-11-11 13:00",
         "2008-09-08 15:00",
         "2008-03-07 11:00",
         "2006-11-02 11:00",
         "2006-09-09 09:00",
         "2003-07-22 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ruggedcomSwitchAgents = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 1)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents.setProductRelease("Rugged Switch Agent capabilities version 1.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 4)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents03.setProductRelease("Rugged Switch Agent capabilities version 3.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents03.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 7)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents04.setProductRelease("Rugged Switch Agent capabilities version 4.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents04.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents05 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 8)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents05.setProductRelease("Rugged Switch Agent capabilities version 4.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents05.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents06 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 9)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents06.setProductRelease("Rugged Switch Agent capabilities version 5.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents06.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents07 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 13)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents07.setProductRelease("Rugged Switch Agent capabilities version 6.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents07.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents071 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 13, 1)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents071.setProductRelease("Rugged Switch Agent capabilities version 6.1.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents071.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents08 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 14)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents08.setProductRelease("Rugged Switch Agent capabilities version 7.0.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents08.setStatus(
        "obsolete"
    )

ruggedcomSwitchAgents081 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 14, 1)
)
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents081.setProductRelease("Rugged Switch Agent capabilities version 7.1.0. ")
if mibBuilder.loadTexts:
    ruggedcomSwitchAgents081.setStatus(
        "obsolete"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-SWITCH-MIB",
    **{"ruggedcomSwitchModule": ruggedcomSwitchModule,
       "ruggedcomSwitchAgents": ruggedcomSwitchAgents,
       "ruggedcomSwitchAgents03": ruggedcomSwitchAgents03,
       "ruggedcomSwitchAgents04": ruggedcomSwitchAgents04,
       "ruggedcomSwitchAgents05": ruggedcomSwitchAgents05,
       "ruggedcomSwitchAgents06": ruggedcomSwitchAgents06,
       "ruggedcomSwitchAgents07": ruggedcomSwitchAgents07,
       "ruggedcomSwitchAgents071": ruggedcomSwitchAgents071,
       "ruggedcomSwitchAgents08": ruggedcomSwitchAgents08,
       "ruggedcomSwitchAgents081": ruggedcomSwitchAgents081}
)
