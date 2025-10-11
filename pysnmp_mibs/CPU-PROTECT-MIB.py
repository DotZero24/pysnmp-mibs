# SNMP MIB module (CPU-PROTECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/CPU-PROTECT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:47 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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

swCPUProtectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 106)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwCPUProtectGlobalMgmt_ObjectIdentity = ObjectIdentity
swCPUProtectGlobalMgmt = _SwCPUProtectGlobalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 106, 1)
)


class _SwCPUProtectState_Type(Integer32):
    """Custom type swCPUProtectState based on Integer32"""
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


_SwCPUProtectState_Type.__name__ = "Integer32"
_SwCPUProtectState_Object = MibScalar
swCPUProtectState = _SwCPUProtectState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 106, 1, 1),
    _SwCPUProtectState_Type()
)
swCPUProtectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCPUProtectState.setStatus("current")
_SwCPUProtectProtocolTable_Object = MibTable
swCPUProtectProtocolTable = _SwCPUProtectProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 106, 2)
)
if mibBuilder.loadTexts:
    swCPUProtectProtocolTable.setStatus("current")
_SwCPUProtectProtocolEntry_Object = MibTableRow
swCPUProtectProtocolEntry = _SwCPUProtectProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 106, 2, 1)
)
swCPUProtectProtocolEntry.setIndexNames(
    (0, "CPU-PROTECT-MIB", "swCPUProtectProtocolType"),
)
if mibBuilder.loadTexts:
    swCPUProtectProtocolEntry.setStatus("current")


class _SwCPUProtectProtocolType_Type(Integer32):
    """Custom type swCPUProtectProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("bpdu", 2),
          ("icmp", 3),
          ("igmp", 4),
          ("snmp", 5))
    )


_SwCPUProtectProtocolType_Type.__name__ = "Integer32"
_SwCPUProtectProtocolType_Object = MibTableColumn
swCPUProtectProtocolType = _SwCPUProtectProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 106, 2, 1, 1),
    _SwCPUProtectProtocolType_Type()
)
swCPUProtectProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCPUProtectProtocolType.setStatus("current")
_SwCPUProtectProtocolRate_Type = Integer32
_SwCPUProtectProtocolRate_Object = MibTableColumn
swCPUProtectProtocolRate = _SwCPUProtectProtocolRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 106, 2, 1, 2),
    _SwCPUProtectProtocolRate_Type()
)
swCPUProtectProtocolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCPUProtectProtocolRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPU-PROTECT-MIB",
    **{"swCPUProtectMIB": swCPUProtectMIB,
       "swCPUProtectGlobalMgmt": swCPUProtectGlobalMgmt,
       "swCPUProtectState": swCPUProtectState,
       "swCPUProtectProtocolTable": swCPUProtectProtocolTable,
       "swCPUProtectProtocolEntry": swCPUProtectProtocolEntry,
       "swCPUProtectProtocolType": swCPUProtectProtocolType,
       "swCPUProtectProtocolRate": swCPUProtectProtocolRate}
)
