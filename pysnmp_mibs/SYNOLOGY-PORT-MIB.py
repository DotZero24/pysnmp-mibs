# SNMP MIB module (SYNOLOGY-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:20 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

synoEthPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 109)
)
if mibBuilder.loadTexts:
    synoEthPort.setRevisions(
        ("2020-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_EthPortTable_Object = MibTable
ethPortTable = _EthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 109, 1)
)
if mibBuilder.loadTexts:
    ethPortTable.setStatus("current")
_EthPortEntry_Object = MibTableRow
ethPortEntry = _EthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 109, 1, 1)
)
ethPortEntry.setIndexNames(
    (0, "SYNOLOGY-PORT-MIB", "ethPortIndex"),
)
if mibBuilder.loadTexts:
    ethPortEntry.setStatus("current")


class _EthPortIndex_Type(Integer32):
    """Custom type ethPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EthPortIndex_Type.__name__ = "Integer32"
_EthPortIndex_Object = MibTableColumn
ethPortIndex = _EthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 1),
    _EthPortIndex_Type()
)
ethPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethPortIndex.setStatus("current")


class _EthPortStatus_Type(Integer32):
    """Custom type ethPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("up", 2),
          ("down", 3))
    )


_EthPortStatus_Type.__name__ = "Integer32"
_EthPortStatus_Object = MibTableColumn
ethPortStatus = _EthPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 2),
    _EthPortStatus_Type()
)
ethPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortStatus.setStatus("current")
_EthPortSpeed_Type = Gauge32
_EthPortSpeed_Object = MibTableColumn
ethPortSpeed = _EthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6574, 109, 1, 1, 3),
    _EthPortSpeed_Type()
)
ethPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethPortSpeed.setStatus("current")
_EthPortConformance_ObjectIdentity = ObjectIdentity
ethPortConformance = _EthPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 109, 2)
)
_EthPortCompliances_ObjectIdentity = ObjectIdentity
ethPortCompliances = _EthPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 109, 2, 1)
)
_EthPortGroups_ObjectIdentity = ObjectIdentity
ethPortGroups = _EthPortGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 109, 2, 2)
)

# Managed Objects groups

ethPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 109, 2, 2, 1)
)
ethPortGroup.setObjects(
      *(("SYNOLOGY-PORT-MIB", "ethPortStatus"),
        ("SYNOLOGY-PORT-MIB", "ethPortSpeed"))
)
if mibBuilder.loadTexts:
    ethPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ethPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 109, 2, 1, 1)
)
ethPortCompliance.setObjects(
    ("SYNOLOGY-PORT-MIB", "ethPortGroup")
)
if mibBuilder.loadTexts:
    ethPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-PORT-MIB",
    **{"synology": synology,
       "synoEthPort": synoEthPort,
       "ethPortTable": ethPortTable,
       "ethPortEntry": ethPortEntry,
       "ethPortIndex": ethPortIndex,
       "ethPortStatus": ethPortStatus,
       "ethPortSpeed": ethPortSpeed,
       "ethPortConformance": ethPortConformance,
       "ethPortCompliances": ethPortCompliances,
       "ethPortCompliance": ethPortCompliance,
       "ethPortGroups": ethPortGroups,
       "ethPortGroup": ethPortGroup}
)
