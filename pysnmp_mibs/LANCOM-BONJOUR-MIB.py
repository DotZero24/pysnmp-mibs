# SNMP MIB module (LANCOM-BONJOUR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-BONJOUR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:30 2025
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

(fastPath,) = mibBuilder.importSymbols(
    "LANCOM-REF-MIB",
    "fastPath")

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

fastPathBonjour = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 71)
)
if mibBuilder.loadTexts:
    fastPathBonjour.setRevisions(
        ("2017-06-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentBonjourObjects_ObjectIdentity = ObjectIdentity
agentBonjourObjects = _AgentBonjourObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1)
)
_AgentBonjourGlobal_ObjectIdentity = ObjectIdentity
agentBonjourGlobal = _AgentBonjourGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1, 1)
)


class _AgentBonjourAdminMode_Type(Integer32):
    """Custom type agentBonjourAdminMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentBonjourAdminMode_Type.__name__ = "Integer32"
_AgentBonjourAdminMode_Object = MibScalar
agentBonjourAdminMode = _AgentBonjourAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 71, 1, 1, 1),
    _AgentBonjourAdminMode_Type()
)
agentBonjourAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBonjourAdminMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-BONJOUR-MIB",
    **{"fastPathBonjour": fastPathBonjour,
       "agentBonjourObjects": agentBonjourObjects,
       "agentBonjourGlobal": agentBonjourGlobal,
       "agentBonjourAdminMode": agentBonjourAdminMode}
)
