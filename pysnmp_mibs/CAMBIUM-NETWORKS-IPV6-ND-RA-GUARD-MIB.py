# SNMP MIB module (CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:48 2025
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

(PortList,
 VlanIdOrNone,
 dot1qStaticUnicastEntry,
 dot1qTpFdbEntry,
 dot1qTpFdbPort,
 dot1qVlanStaticEntry) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone",
    "dot1qStaticUnicastEntry",
    "dot1qTpFdbEntry",
    "dot1qTpFdbPort",
    "dot1qVlanStaticEntry")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnRAGuardMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9)
)
if mibBuilder.loadTexts:
    cnRAGuardMib.setRevisions(
        ("2021-11-28 00:00",
         "2021-04-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RAGuardPolicy(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("router", 0),
          ("host", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CnRAGuardIfCfg_ObjectIdentity = ObjectIdentity
cnRAGuardIfCfg = _CnRAGuardIfCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9, 1)
)
_CnRAGuardIfCfgTable_Object = MibTable
cnRAGuardIfCfgTable = _CnRAGuardIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1)
)
if mibBuilder.loadTexts:
    cnRAGuardIfCfgTable.setStatus("current")
_CnRAGuardIfCfgEntry_Object = MibTableRow
cnRAGuardIfCfgEntry = _CnRAGuardIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1)
)
cnRAGuardIfCfgEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB", "cnRAGuardIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    cnRAGuardIfCfgEntry.setStatus("current")


class _CnRAGuardIfCfgIfIndex_Type(Integer32):
    """Custom type cnRAGuardIfCfgIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 52),
    )


_CnRAGuardIfCfgIfIndex_Type.__name__ = "Integer32"
_CnRAGuardIfCfgIfIndex_Object = MibTableColumn
cnRAGuardIfCfgIfIndex = _CnRAGuardIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1, 1),
    _CnRAGuardIfCfgIfIndex_Type()
)
cnRAGuardIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnRAGuardIfCfgIfIndex.setStatus("current")


class _CnRAGuardIfCfgPolicy_Type(RAGuardPolicy):
    """Custom type cnRAGuardIfCfgPolicy based on RAGuardPolicy"""
    defaultValue = 0


_CnRAGuardIfCfgPolicy_Type.__name__ = "RAGuardPolicy"
_CnRAGuardIfCfgPolicy_Object = MibTableColumn
cnRAGuardIfCfgPolicy = _CnRAGuardIfCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1, 2),
    _CnRAGuardIfCfgPolicy_Type()
)
cnRAGuardIfCfgPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnRAGuardIfCfgPolicy.setStatus("current")
_CnRAGuardIfCounter_Type = Gauge32
_CnRAGuardIfCounter_Object = MibTableColumn
cnRAGuardIfCounter = _CnRAGuardIfCounter_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 9, 1, 1, 1, 3),
    _CnRAGuardIfCounter_Type()
)
cnRAGuardIfCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnRAGuardIfCounter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-IPV6-ND-RA-GUARD-MIB",
    **{"RAGuardPolicy": RAGuardPolicy,
       "cnRAGuardMib": cnRAGuardMib,
       "cnRAGuardIfCfg": cnRAGuardIfCfg,
       "cnRAGuardIfCfgTable": cnRAGuardIfCfgTable,
       "cnRAGuardIfCfgEntry": cnRAGuardIfCfgEntry,
       "cnRAGuardIfCfgIfIndex": cnRAGuardIfCfgIfIndex,
       "cnRAGuardIfCfgPolicy": cnRAGuardIfCfgPolicy,
       "cnRAGuardIfCounter": cnRAGuardIfCounter}
)
