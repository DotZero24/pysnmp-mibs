# SNMP MIB module (MX-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SNMP-AGENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:37 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150)
)
if mibBuilder.loadTexts:
    snmpAgentMIB.setRevisions(
        ("2005-04-28 00:00",
         "2004-02-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpAgentMIBObjects_ObjectIdentity = ObjectIdentity
snmpAgentMIBObjects = _SnmpAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 1)
)


class _SnmpAgentEnable_Type(MxEnableState):
    """Custom type snmpAgentEnable based on MxEnableState"""
    defaultValue = 1


_SnmpAgentEnable_Type.__name__ = "MxEnableState"
_SnmpAgentEnable_Object = MibScalar
snmpAgentEnable = _SnmpAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 1, 1),
    _SnmpAgentEnable_Type()
)
snmpAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentEnable.setStatus("current")


class _SnmpAgentAccess_Type(Integer32):
    """Custom type snmpAgentAccess based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lanOnly", 0),
          ("wanOnly", 1),
          ("all", 2))
    )


_SnmpAgentAccess_Type.__name__ = "Integer32"
_SnmpAgentAccess_Object = MibScalar
snmpAgentAccess = _SnmpAgentAccess_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 1, 5),
    _SnmpAgentAccess_Type()
)
snmpAgentAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentAccess.setStatus("current")
_SnmpAgentConformance_ObjectIdentity = ObjectIdentity
snmpAgentConformance = _SnmpAgentConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 2)
)
_SnmpAgentCompliances_ObjectIdentity = ObjectIdentity
snmpAgentCompliances = _SnmpAgentCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 1)
)
_SnmpAgentGroups_ObjectIdentity = ObjectIdentity
snmpAgentGroups = _SnmpAgentGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 5)
)

# Managed Objects groups

snmpAgentAccessGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 5, 5)
)
snmpAgentAccessGroupVer1.setObjects(
      *(("MX-SNMP-AGENT-MIB", "snmpAgentEnable"),
        ("MX-SNMP-AGENT-MIB", "snmpAgentAccess"))
)
if mibBuilder.loadTexts:
    snmpAgentAccessGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpAgentAccessComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 150, 2, 1, 1)
)
snmpAgentAccessComplVer1.setObjects(
    ("MX-SNMP-AGENT-MIB", "snmpAgentAccessGroupVer1")
)
if mibBuilder.loadTexts:
    snmpAgentAccessComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SNMP-AGENT-MIB",
    **{"snmpAgentMIB": snmpAgentMIB,
       "snmpAgentMIBObjects": snmpAgentMIBObjects,
       "snmpAgentEnable": snmpAgentEnable,
       "snmpAgentAccess": snmpAgentAccess,
       "snmpAgentConformance": snmpAgentConformance,
       "snmpAgentCompliances": snmpAgentCompliances,
       "snmpAgentAccessComplVer1": snmpAgentAccessComplVer1,
       "snmpAgentGroups": snmpAgentGroups,
       "snmpAgentAccessGroupVer1": snmpAgentAccessGroupVer1}
)
