# SNMP MIB module (RUGGEDCOM-MC30-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-MC30-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:43 2025
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

ruggedcomMC30Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 2, 3)
)
if mibBuilder.loadTexts:
    ruggedcomMC30Module.setRevisions(
        ("2011-05-01 17:00",
         "2009-05-15 17:00",
         "2008-03-07 11:00",
         "2006-11-02 11:00",
         "2006-09-09 09:00",
         "2004-06-28 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

ruggedcomMC30Agents = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 3)
)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents.setProductRelease("""\
Rugged Media Converter RMC30 Agent capabilities version
                     1.0.0. """)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents.setStatus(
        "obsolete"
    )

ruggedcomMC30Agents03 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 6)
)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents03.setProductRelease("""\
Rugged Media Converter RMC30 Agent capabilities version
                     3.0.0. """)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents03.setStatus(
        "obsolete"
    )

ruggedcomMC30Agents04 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 11)
)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents04.setProductRelease("""\
Rugged Media Converter RMC30 Agent capabilities version
                     4.0.0. """)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents04.setStatus(
        "obsolete"
    )

ruggedcomMC30Agents041 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 15004, 6, 11, 1)
)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents041.setProductRelease("""\
Rugged Media Converter RMC30 Agent capabilities version
                     4.1.0. """)
if mibBuilder.loadTexts:
    ruggedcomMC30Agents041.setStatus(
        "obsolete"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-MC30-MIB",
    **{"ruggedcomMC30Module": ruggedcomMC30Module,
       "ruggedcomMC30Agents": ruggedcomMC30Agents,
       "ruggedcomMC30Agents03": ruggedcomMC30Agents03,
       "ruggedcomMC30Agents04": ruggedcomMC30Agents04,
       "ruggedcomMC30Agents041": ruggedcomMC30Agents041}
)
