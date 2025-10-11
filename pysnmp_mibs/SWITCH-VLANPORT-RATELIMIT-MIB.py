# SNMP MIB module (SWITCH-VLANPORT-RATELIMIT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-VLANPORT-RATELIMIT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:01 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcRateLimit = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcVlanPortRateLimitTable_Object = MibTable
rcVlanPortRateLimitTable = _RcVlanPortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rcVlanPortRateLimitTable.setStatus("current")
_RcVlanPortRateLimitEntry_Object = MibTableRow
rcVlanPortRateLimitEntry = _RcVlanPortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1)
)
rcVlanPortRateLimitEntry.setIndexNames(
    (0, "SWITCH-VLANPORT-RATELIMIT-MIB", "rcVlanPortRateLimitPortIndex"),
    (0, "SWITCH-VLANPORT-RATELIMIT-MIB", "rcVlanPortRateLimitPortRule"),
    (0, "SWITCH-VLANPORT-RATELIMIT-MIB", "rcVlanPortRateLimitVlanIndex"),
)
if mibBuilder.loadTexts:
    rcVlanPortRateLimitEntry.setStatus("current")
_RcVlanPortRateLimitPortIndex_Type = Integer32
_RcVlanPortRateLimitPortIndex_Object = MibTableColumn
rcVlanPortRateLimitPortIndex = _RcVlanPortRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1, 1),
    _RcVlanPortRateLimitPortIndex_Type()
)
rcVlanPortRateLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitPortIndex.setStatus("current")


class _RcVlanPortRateLimitPortRule_Type(Integer32):
    """Custom type rcVlanPortRateLimitPortRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_RcVlanPortRateLimitPortRule_Type.__name__ = "Integer32"
_RcVlanPortRateLimitPortRule_Object = MibTableColumn
rcVlanPortRateLimitPortRule = _RcVlanPortRateLimitPortRule_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1, 2),
    _RcVlanPortRateLimitPortRule_Type()
)
rcVlanPortRateLimitPortRule.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitPortRule.setStatus("current")


class _RcVlanPortRateLimitVlanIndex_Type(Integer32):
    """Custom type rcVlanPortRateLimitVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcVlanPortRateLimitVlanIndex_Type.__name__ = "Integer32"
_RcVlanPortRateLimitVlanIndex_Object = MibTableColumn
rcVlanPortRateLimitVlanIndex = _RcVlanPortRateLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1, 3),
    _RcVlanPortRateLimitVlanIndex_Type()
)
rcVlanPortRateLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitVlanIndex.setStatus("current")
_RcVlanPortRateLimitRate_Type = Integer32
_RcVlanPortRateLimitRate_Object = MibTableColumn
rcVlanPortRateLimitRate = _RcVlanPortRateLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1, 4),
    _RcVlanPortRateLimitRate_Type()
)
rcVlanPortRateLimitRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitRate.setStatus("current")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitRate.setUnits("kbps")
_RcVlanPortRateLimitBurst_Type = Integer32
_RcVlanPortRateLimitBurst_Object = MibTableColumn
rcVlanPortRateLimitBurst = _RcVlanPortRateLimitBurst_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1, 5),
    _RcVlanPortRateLimitBurst_Type()
)
rcVlanPortRateLimitBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitBurst.setStatus("current")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitBurst.setUnits("kB")
_RcVlanPortRateLimitRowStatus_Type = RowStatus
_RcVlanPortRateLimitRowStatus_Object = MibTableColumn
rcVlanPortRateLimitRowStatus = _RcVlanPortRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 2, 5, 1, 6),
    _RcVlanPortRateLimitRowStatus_Type()
)
rcVlanPortRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcVlanPortRateLimitRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-VLANPORT-RATELIMIT-MIB",
    **{"rcRateLimit": rcRateLimit,
       "rcVlanPortRateLimitTable": rcVlanPortRateLimitTable,
       "rcVlanPortRateLimitEntry": rcVlanPortRateLimitEntry,
       "rcVlanPortRateLimitPortIndex": rcVlanPortRateLimitPortIndex,
       "rcVlanPortRateLimitPortRule": rcVlanPortRateLimitPortRule,
       "rcVlanPortRateLimitVlanIndex": rcVlanPortRateLimitVlanIndex,
       "rcVlanPortRateLimitRate": rcVlanPortRateLimitRate,
       "rcVlanPortRateLimitBurst": rcVlanPortRateLimitBurst,
       "rcVlanPortRateLimitRowStatus": rcVlanPortRateLimitRowStatus}
)
