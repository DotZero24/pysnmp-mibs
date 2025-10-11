# SNMP MIB module (CAMBIUM-NETWORKS-EEE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-EEE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:45 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnEeeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8)
)
if mibBuilder.loadTexts:
    cnEeeMib.setRevisions(
        ("2021-04-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnEeeObjects_ObjectIdentity = ObjectIdentity
cnEeeObjects = _CnEeeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0)
)
_CnEeePortTable_Object = MibTable
cnEeePortTable = _CnEeePortTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1)
)
if mibBuilder.loadTexts:
    cnEeePortTable.setStatus("current")
_CnEeePortEntry_Object = MibTableRow
cnEeePortEntry = _CnEeePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1)
)
cnEeePortEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-EEE-MIB", "cnEeePortIndex"),
)
if mibBuilder.loadTexts:
    cnEeePortEntry.setStatus("current")


class _CnEeePortIndex_Type(Integer32):
    """Custom type cnEeePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnEeePortIndex_Type.__name__ = "Integer32"
_CnEeePortIndex_Object = MibTableColumn
cnEeePortIndex = _CnEeePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 1),
    _CnEeePortIndex_Type()
)
cnEeePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnEeePortIndex.setStatus("current")


class _CnEeeEnabled_Type(Integer32):
    """Custom type cnEeeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_CnEeeEnabled_Type.__name__ = "Integer32"
_CnEeeEnabled_Object = MibTableColumn
cnEeeEnabled = _CnEeeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 2),
    _CnEeeEnabled_Type()
)
cnEeeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnEeeEnabled.setStatus("current")


class _CnEeeCapabilities_Type(Integer32):
    """Custom type cnEeeCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnEeeCapabilities_Type.__name__ = "Integer32"
_CnEeeCapabilities_Object = MibTableColumn
cnEeeCapabilities = _CnEeeCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 3),
    _CnEeeCapabilities_Type()
)
cnEeeCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnEeeCapabilities.setStatus("current")


class _CnEeeLpAbilities_Type(Integer32):
    """Custom type cnEeeLpAbilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CnEeeLpAbilities_Type.__name__ = "Integer32"
_CnEeeLpAbilities_Object = MibTableColumn
cnEeeLpAbilities = _CnEeeLpAbilities_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 8, 0, 1, 1, 4),
    _CnEeeLpAbilities_Type()
)
cnEeeLpAbilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnEeeLpAbilities.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-EEE-MIB",
    **{"cnEeeMib": cnEeeMib,
       "cnEeeObjects": cnEeeObjects,
       "cnEeePortTable": cnEeePortTable,
       "cnEeePortEntry": cnEeePortEntry,
       "cnEeePortIndex": cnEeePortIndex,
       "cnEeeEnabled": cnEeeEnabled,
       "cnEeeCapabilities": cnEeeCapabilities,
       "cnEeeLpAbilities": cnEeeLpAbilities}
)
