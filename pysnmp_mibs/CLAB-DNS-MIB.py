# SNMP MIB module (CLAB-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/CLAB-DNS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:22:58 2025
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

(clabCommonMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabCommonMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

clabDNSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5)
)
if mibBuilder.loadTexts:
    clabDNSMib.setRevisions(
        ("2016-02-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClabDNSNotifications_ObjectIdentity = ObjectIdentity
clabDNSNotifications = _ClabDNSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 0)
)
_ClabDNSObjects_ObjectIdentity = ObjectIdentity
clabDNSObjects = _ClabDNSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 1)
)


class _ClabDnsIpv6QueryForDualMode_Type(TruthValue):
    """Custom type clabDnsIpv6QueryForDualMode based on TruthValue"""
    defaultValue = 2


_ClabDnsIpv6QueryForDualMode_Type.__name__ = "TruthValue"
_ClabDnsIpv6QueryForDualMode_Object = MibScalar
clabDnsIpv6QueryForDualMode = _ClabDnsIpv6QueryForDualMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 1, 1),
    _ClabDnsIpv6QueryForDualMode_Type()
)
clabDnsIpv6QueryForDualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clabDnsIpv6QueryForDualMode.setStatus("current")
_ClabDNSMibConformance_ObjectIdentity = ObjectIdentity
clabDNSMibConformance = _ClabDNSMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 2)
)
_ClabDNSMibCompliances_ObjectIdentity = ObjectIdentity
clabDNSMibCompliances = _ClabDNSMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 1)
)
_ClabDNSMibGroups_ObjectIdentity = ObjectIdentity
clabDNSMibGroups = _ClabDNSMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 2)
)

# Managed Objects groups

clabDNSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 2, 1)
)
clabDNSGroup.setObjects(
    ("CLAB-DNS-MIB", "clabDnsIpv6QueryForDualMode")
)
if mibBuilder.loadTexts:
    clabDNSGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

clabDNSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 4, 5, 2, 1, 1)
)
clabDNSCompliance.setObjects(
    ("CLAB-DNS-MIB", "clabDNSGroup")
)
if mibBuilder.loadTexts:
    clabDNSCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAB-DNS-MIB",
    **{"clabDNSMib": clabDNSMib,
       "clabDNSNotifications": clabDNSNotifications,
       "clabDNSObjects": clabDNSObjects,
       "clabDnsIpv6QueryForDualMode": clabDnsIpv6QueryForDualMode,
       "clabDNSMibConformance": clabDNSMibConformance,
       "clabDNSMibCompliances": clabDNSMibCompliances,
       "clabDNSCompliance": clabDNSCompliance,
       "clabDNSMibGroups": clabDNSMibGroups,
       "clabDNSGroup": clabDNSGroup}
)
