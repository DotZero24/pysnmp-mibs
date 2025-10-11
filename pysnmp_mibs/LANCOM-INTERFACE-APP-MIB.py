# SNMP MIB module (LANCOM-INTERFACE-APP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-INTERFACE-APP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:20:32 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

fastPathInterfaceApp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 70)
)
if mibBuilder.loadTexts:
    fastPathInterfaceApp.setRevisions(
        ("2016-08-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentLinkFlapMIBObjects_ObjectIdentity = ObjectIdentity
agentLinkFlapMIBObjects = _AgentLinkFlapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 70, 1)
)
_AgentLinkFlapGlobal_ObjectIdentity = ObjectIdentity
agentLinkFlapGlobal = _AgentLinkFlapGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 70, 1, 1)
)


class _AgentLinkFlapAdminMode_Type(Integer32):
    """Custom type agentLinkFlapAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentLinkFlapAdminMode_Type.__name__ = "Integer32"
_AgentLinkFlapAdminMode_Object = MibScalar
agentLinkFlapAdminMode = _AgentLinkFlapAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 70, 1, 1, 1),
    _AgentLinkFlapAdminMode_Type()
)
agentLinkFlapAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkFlapAdminMode.setStatus("current")


class _AgentLinkFlapDuration_Type(Unsigned32):
    """Custom type agentLinkFlapDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 200),
    )


_AgentLinkFlapDuration_Type.__name__ = "Unsigned32"
_AgentLinkFlapDuration_Object = MibScalar
agentLinkFlapDuration = _AgentLinkFlapDuration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 70, 1, 1, 2),
    _AgentLinkFlapDuration_Type()
)
agentLinkFlapDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkFlapDuration.setStatus("current")
if mibBuilder.loadTexts:
    agentLinkFlapDuration.setUnits("seconds")


class _AgentLinkFlapMaxCount_Type(Unsigned32):
    """Custom type agentLinkFlapMaxCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 100),
    )


_AgentLinkFlapMaxCount_Type.__name__ = "Unsigned32"
_AgentLinkFlapMaxCount_Object = MibScalar
agentLinkFlapMaxCount = _AgentLinkFlapMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 70, 1, 1, 3),
    _AgentLinkFlapMaxCount_Type()
)
agentLinkFlapMaxCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkFlapMaxCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-INTERFACE-APP-MIB",
    **{"fastPathInterfaceApp": fastPathInterfaceApp,
       "agentLinkFlapMIBObjects": agentLinkFlapMIBObjects,
       "agentLinkFlapGlobal": agentLinkFlapGlobal,
       "agentLinkFlapAdminMode": agentLinkFlapAdminMode,
       "agentLinkFlapDuration": agentLinkFlapDuration,
       "agentLinkFlapMaxCount": agentLinkFlapMaxCount}
)
