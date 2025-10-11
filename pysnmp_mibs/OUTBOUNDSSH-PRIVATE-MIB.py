# SNMP MIB module (OUTBOUNDSSH-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/quanta/OUTBOUNDSSH-PRIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:14 2025
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

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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

outboundSSHPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentOutboundSSHGroup_ObjectIdentity = ObjectIdentity
agentOutboundSSHGroup = _AgentOutboundSSHGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 21, 1)
)


class _AgentOutboundSSHAdminMode_Type(Integer32):
    """Custom type agentOutboundSSHAdminMode based on Integer32"""
    defaultValue = 1

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


_AgentOutboundSSHAdminMode_Type.__name__ = "Integer32"
_AgentOutboundSSHAdminMode_Object = MibScalar
agentOutboundSSHAdminMode = _AgentOutboundSSHAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 1),
    _AgentOutboundSSHAdminMode_Type()
)
agentOutboundSSHAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundSSHAdminMode.setStatus("current")


class _AgentOutboundSSHMaxNoOfSessions_Type(Integer32):
    """Custom type agentOutboundSSHMaxNoOfSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentOutboundSSHMaxNoOfSessions_Type.__name__ = "Integer32"
_AgentOutboundSSHMaxNoOfSessions_Object = MibScalar
agentOutboundSSHMaxNoOfSessions = _AgentOutboundSSHMaxNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 2),
    _AgentOutboundSSHMaxNoOfSessions_Type()
)
agentOutboundSSHMaxNoOfSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundSSHMaxNoOfSessions.setStatus("current")


class _AgentOutboundSSHTimeout_Type(Integer32):
    """Custom type agentOutboundSSHTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 160),
    )


_AgentOutboundSSHTimeout_Type.__name__ = "Integer32"
_AgentOutboundSSHTimeout_Object = MibScalar
agentOutboundSSHTimeout = _AgentOutboundSSHTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 21, 1, 3),
    _AgentOutboundSSHTimeout_Type()
)
agentOutboundSSHTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundSSHTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OUTBOUNDSSH-PRIVATE-MIB",
    **{"outboundSSHPrivate": outboundSSHPrivate,
       "agentOutboundSSHGroup": agentOutboundSSHGroup,
       "agentOutboundSSHAdminMode": agentOutboundSSHAdminMode,
       "agentOutboundSSHMaxNoOfSessions": agentOutboundSSHMaxNoOfSessions,
       "agentOutboundSSHTimeout": agentOutboundSSHTimeout}
)
