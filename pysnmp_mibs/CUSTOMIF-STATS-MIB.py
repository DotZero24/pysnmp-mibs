# SNMP MIB module (CUSTOMIF-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ipinfusion/CUSTOMIF-STATS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:21 2025
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

(ipi,) = mibBuilder.importSymbols(
    "OCNOS-IPI-MODULE-MIB",
    "ipi")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

customIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 103)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CustomIfTable_ObjectIdentity = ObjectIdentity
customIfTable = _CustomIfTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1)
)
_IfDropStatsTable_Object = MibTable
ifDropStatsTable = _IfDropStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1)
)
if mibBuilder.loadTexts:
    ifDropStatsTable.setStatus("current")
_IfDropStatsEntry_Object = MibTableRow
ifDropStatsEntry = _IfDropStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1)
)
ifDropStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifDropStatsEntry.setStatus("current")
_IfRxBadCrcErrors_Type = Counter64
_IfRxBadCrcErrors_Object = MibTableColumn
ifRxBadCrcErrors = _IfRxBadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 1),
    _IfRxBadCrcErrors_Type()
)
ifRxBadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxBadCrcErrors.setStatus("current")
_IfRxBadCrcLastIncrement_Type = Counter64
_IfRxBadCrcLastIncrement_Object = MibTableColumn
ifRxBadCrcLastIncrement = _IfRxBadCrcLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 2),
    _IfRxBadCrcLastIncrement_Type()
)
ifRxBadCrcLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxBadCrcLastIncrement.setStatus("current")
_IfRxBadCrcLastIncrementTime_Type = DateAndTime
_IfRxBadCrcLastIncrementTime_Object = MibTableColumn
ifRxBadCrcLastIncrementTime = _IfRxBadCrcLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 3),
    _IfRxBadCrcLastIncrementTime_Type()
)
ifRxBadCrcLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxBadCrcLastIncrementTime.setStatus("current")
_IfRxUndersizeErrors_Type = Counter64
_IfRxUndersizeErrors_Object = MibTableColumn
ifRxUndersizeErrors = _IfRxUndersizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 4),
    _IfRxUndersizeErrors_Type()
)
ifRxUndersizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxUndersizeErrors.setStatus("current")
_IfRxUndersizeLastIncrement_Type = Counter64
_IfRxUndersizeLastIncrement_Object = MibTableColumn
ifRxUndersizeLastIncrement = _IfRxUndersizeLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 5),
    _IfRxUndersizeLastIncrement_Type()
)
ifRxUndersizeLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxUndersizeLastIncrement.setStatus("current")
_IfRxUndersizeLastIncrementTime_Type = DateAndTime
_IfRxUndersizeLastIncrementTime_Object = MibTableColumn
ifRxUndersizeLastIncrementTime = _IfRxUndersizeLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 6),
    _IfRxUndersizeLastIncrementTime_Type()
)
ifRxUndersizeLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxUndersizeLastIncrementTime.setStatus("current")
_IfRxOversizeErrors_Type = Counter64
_IfRxOversizeErrors_Object = MibTableColumn
ifRxOversizeErrors = _IfRxOversizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 7),
    _IfRxOversizeErrors_Type()
)
ifRxOversizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxOversizeErrors.setStatus("current")
_IfRxOversizeLastIncrement_Type = Counter64
_IfRxOversizeLastIncrement_Object = MibTableColumn
ifRxOversizeLastIncrement = _IfRxOversizeLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 8),
    _IfRxOversizeLastIncrement_Type()
)
ifRxOversizeLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxOversizeLastIncrement.setStatus("current")
_IfRxOversizeLastIncrementTime_Type = DateAndTime
_IfRxOversizeLastIncrementTime_Object = MibTableColumn
ifRxOversizeLastIncrementTime = _IfRxOversizeLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 9),
    _IfRxOversizeLastIncrementTime_Type()
)
ifRxOversizeLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxOversizeLastIncrementTime.setStatus("current")
_IfRxFragmentErrors_Type = Counter64
_IfRxFragmentErrors_Object = MibTableColumn
ifRxFragmentErrors = _IfRxFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 10),
    _IfRxFragmentErrors_Type()
)
ifRxFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxFragmentErrors.setStatus("current")
_IfRxFragmentLastIncrement_Type = Counter64
_IfRxFragmentLastIncrement_Object = MibTableColumn
ifRxFragmentLastIncrement = _IfRxFragmentLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 11),
    _IfRxFragmentLastIncrement_Type()
)
ifRxFragmentLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxFragmentLastIncrement.setStatus("current")
_IfRxFragmentLastIncrementTime_Type = DateAndTime
_IfRxFragmentLastIncrementTime_Object = MibTableColumn
ifRxFragmentLastIncrementTime = _IfRxFragmentLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 12),
    _IfRxFragmentLastIncrementTime_Type()
)
ifRxFragmentLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxFragmentLastIncrementTime.setStatus("current")
_IfRxJabberErrors_Type = Counter64
_IfRxJabberErrors_Object = MibTableColumn
ifRxJabberErrors = _IfRxJabberErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 13),
    _IfRxJabberErrors_Type()
)
ifRxJabberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxJabberErrors.setStatus("current")
_IfRxJabberLastIncrement_Type = Counter64
_IfRxJabberLastIncrement_Object = MibTableColumn
ifRxJabberLastIncrement = _IfRxJabberLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 14),
    _IfRxJabberLastIncrement_Type()
)
ifRxJabberLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxJabberLastIncrement.setStatus("current")
_IfRxJabberLastIncrementTime_Type = DateAndTime
_IfRxJabberLastIncrementTime_Object = MibTableColumn
ifRxJabberLastIncrementTime = _IfRxJabberLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 15),
    _IfRxJabberLastIncrementTime_Type()
)
ifRxJabberLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxJabberLastIncrementTime.setStatus("current")
_IfRxPortBlockDrops_Type = Counter64
_IfRxPortBlockDrops_Object = MibTableColumn
ifRxPortBlockDrops = _IfRxPortBlockDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 16),
    _IfRxPortBlockDrops_Type()
)
ifRxPortBlockDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxPortBlockDrops.setStatus("current")
_IfRxPortBlockLastIncrement_Type = Counter64
_IfRxPortBlockLastIncrement_Object = MibTableColumn
ifRxPortBlockLastIncrement = _IfRxPortBlockLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 17),
    _IfRxPortBlockLastIncrement_Type()
)
ifRxPortBlockLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxPortBlockLastIncrement.setStatus("current")
_IfRxPortBlockLastIncrementTime_Type = DateAndTime
_IfRxPortBlockLastIncrementTime_Object = MibTableColumn
ifRxPortBlockLastIncrementTime = _IfRxPortBlockLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 18),
    _IfRxPortBlockLastIncrementTime_Type()
)
ifRxPortBlockLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxPortBlockLastIncrementTime.setStatus("current")
_IfRxVlanDiscards_Type = Counter64
_IfRxVlanDiscards_Object = MibTableColumn
ifRxVlanDiscards = _IfRxVlanDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 19),
    _IfRxVlanDiscards_Type()
)
ifRxVlanDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxVlanDiscards.setStatus("current")
_IfRxVlanDiscardsLastIncrement_Type = Counter64
_IfRxVlanDiscardsLastIncrement_Object = MibTableColumn
ifRxVlanDiscardsLastIncrement = _IfRxVlanDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 20),
    _IfRxVlanDiscardsLastIncrement_Type()
)
ifRxVlanDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxVlanDiscardsLastIncrement.setStatus("current")
_IfRxVlanDiscardsLastIncrementTime_Type = DateAndTime
_IfRxVlanDiscardsLastIncrementTime_Object = MibTableColumn
ifRxVlanDiscardsLastIncrementTime = _IfRxVlanDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 21),
    _IfRxVlanDiscardsLastIncrementTime_Type()
)
ifRxVlanDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxVlanDiscardsLastIncrementTime.setStatus("current")
_IfRxAclOrQosDrops_Type = Counter64
_IfRxAclOrQosDrops_Object = MibTableColumn
ifRxAclOrQosDrops = _IfRxAclOrQosDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 22),
    _IfRxAclOrQosDrops_Type()
)
ifRxAclOrQosDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxAclOrQosDrops.setStatus("current")
_IfRxAclOrQosDropsLastIncrement_Type = Counter64
_IfRxAclOrQosDropsLastIncrement_Object = MibTableColumn
ifRxAclOrQosDropsLastIncrement = _IfRxAclOrQosDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 23),
    _IfRxAclOrQosDropsLastIncrement_Type()
)
ifRxAclOrQosDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxAclOrQosDropsLastIncrement.setStatus("current")
_IfRxAclOrQosDropsLastIncrementTime_Type = DateAndTime
_IfRxAclOrQosDropsLastIncrementTime_Object = MibTableColumn
ifRxAclOrQosDropsLastIncrementTime = _IfRxAclOrQosDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 24),
    _IfRxAclOrQosDropsLastIncrementTime_Type()
)
ifRxAclOrQosDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxAclOrQosDropsLastIncrementTime.setStatus("current")
_IfRxPolicyDiscards_Type = Counter64
_IfRxPolicyDiscards_Object = MibTableColumn
ifRxPolicyDiscards = _IfRxPolicyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 25),
    _IfRxPolicyDiscards_Type()
)
ifRxPolicyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxPolicyDiscards.setStatus("current")
_IfRxPolicyDiscardsLastIncrement_Type = Counter64
_IfRxPolicyDiscardsLastIncrement_Object = MibTableColumn
ifRxPolicyDiscardsLastIncrement = _IfRxPolicyDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 26),
    _IfRxPolicyDiscardsLastIncrement_Type()
)
ifRxPolicyDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxPolicyDiscardsLastIncrement.setStatus("current")
_IfRxPolicyDiscardsLastIncrementTime_Type = DateAndTime
_IfRxPolicyDiscardsLastIncrementTime_Object = MibTableColumn
ifRxPolicyDiscardsLastIncrementTime = _IfRxPolicyDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 27),
    _IfRxPolicyDiscardsLastIncrementTime_Type()
)
ifRxPolicyDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxPolicyDiscardsLastIncrementTime.setStatus("current")
_IfRxEgrPortUnavail_Type = Counter64
_IfRxEgrPortUnavail_Object = MibTableColumn
ifRxEgrPortUnavail = _IfRxEgrPortUnavail_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 28),
    _IfRxEgrPortUnavail_Type()
)
ifRxEgrPortUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxEgrPortUnavail.setStatus("current")
_IfRxEgrPortUnavailLastIncrement_Type = Counter64
_IfRxEgrPortUnavailLastIncrement_Object = MibTableColumn
ifRxEgrPortUnavailLastIncrement = _IfRxEgrPortUnavailLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 29),
    _IfRxEgrPortUnavailLastIncrement_Type()
)
ifRxEgrPortUnavailLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxEgrPortUnavailLastIncrement.setStatus("current")
_IfRxEgrPortUnavailLastIncrementTime_Type = DateAndTime
_IfRxEgrPortUnavailLastIncrementTime_Object = MibTableColumn
ifRxEgrPortUnavailLastIncrementTime = _IfRxEgrPortUnavailLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 30),
    _IfRxEgrPortUnavailLastIncrementTime_Type()
)
ifRxEgrPortUnavailLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxEgrPortUnavailLastIncrementTime.setStatus("current")
_IfRxIBPDiscards_Type = Counter64
_IfRxIBPDiscards_Object = MibTableColumn
ifRxIBPDiscards = _IfRxIBPDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 31),
    _IfRxIBPDiscards_Type()
)
ifRxIBPDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxIBPDiscards.setStatus("current")
_IfRxIBPDiscardsLastIncrement_Type = Counter64
_IfRxIBPDiscardsLastIncrement_Object = MibTableColumn
ifRxIBPDiscardsLastIncrement = _IfRxIBPDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 32),
    _IfRxIBPDiscardsLastIncrement_Type()
)
ifRxIBPDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxIBPDiscardsLastIncrement.setStatus("current")
_IfRxIBPDiscardsLastIncrementTime_Type = DateAndTime
_IfRxIBPDiscardsLastIncrementTime_Object = MibTableColumn
ifRxIBPDiscardsLastIncrementTime = _IfRxIBPDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 33),
    _IfRxIBPDiscardsLastIncrementTime_Type()
)
ifRxIBPDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxIBPDiscardsLastIncrementTime.setStatus("current")
_IfTxPortBlockDrops_Type = Counter64
_IfTxPortBlockDrops_Object = MibTableColumn
ifTxPortBlockDrops = _IfTxPortBlockDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 34),
    _IfTxPortBlockDrops_Type()
)
ifTxPortBlockDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxPortBlockDrops.setStatus("current")
_IfTxPortBlockDropsLastIncrement_Type = Counter64
_IfTxPortBlockDropsLastIncrement_Object = MibTableColumn
ifTxPortBlockDropsLastIncrement = _IfTxPortBlockDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 35),
    _IfTxPortBlockDropsLastIncrement_Type()
)
ifTxPortBlockDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxPortBlockDropsLastIncrement.setStatus("current")
_IfTxPortBlockDropsLastIncrementTime_Type = DateAndTime
_IfTxPortBlockDropsLastIncrementTime_Object = MibTableColumn
ifTxPortBlockDropsLastIncrementTime = _IfTxPortBlockDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 36),
    _IfTxPortBlockDropsLastIncrementTime_Type()
)
ifTxPortBlockDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxPortBlockDropsLastIncrementTime.setStatus("current")
_IfTxVlanDiscards_Type = Counter64
_IfTxVlanDiscards_Object = MibTableColumn
ifTxVlanDiscards = _IfTxVlanDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 37),
    _IfTxVlanDiscards_Type()
)
ifTxVlanDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxVlanDiscards.setStatus("current")
_IfTxVlanDiscardsLastIncrement_Type = Counter64
_IfTxVlanDiscardsLastIncrement_Object = MibTableColumn
ifTxVlanDiscardsLastIncrement = _IfTxVlanDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 38),
    _IfTxVlanDiscardsLastIncrement_Type()
)
ifTxVlanDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxVlanDiscardsLastIncrement.setStatus("current")
_IfTxVlanDiscardsLastIncrementTime_Type = DateAndTime
_IfTxVlanDiscardsLastIncrementTime_Object = MibTableColumn
ifTxVlanDiscardsLastIncrementTime = _IfTxVlanDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 39),
    _IfTxVlanDiscardsLastIncrementTime_Type()
)
ifTxVlanDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxVlanDiscardsLastIncrementTime.setStatus("current")
_IfTxTtlDiscards_Type = Counter64
_IfTxTtlDiscards_Object = MibTableColumn
ifTxTtlDiscards = _IfTxTtlDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 40),
    _IfTxTtlDiscards_Type()
)
ifTxTtlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxTtlDiscards.setStatus("current")
_IfTxTtlDiscardsLastIncrement_Type = Counter64
_IfTxTtlDiscardsLastIncrement_Object = MibTableColumn
ifTxTtlDiscardsLastIncrement = _IfTxTtlDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 41),
    _IfTxTtlDiscardsLastIncrement_Type()
)
ifTxTtlDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxTtlDiscardsLastIncrement.setStatus("current")
_IfTxTtlDiscardsLastIncrementTime_Type = DateAndTime
_IfTxTtlDiscardsLastIncrementTime_Object = MibTableColumn
ifTxTtlDiscardsLastIncrementTime = _IfTxTtlDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 42),
    _IfTxTtlDiscardsLastIncrementTime_Type()
)
ifTxTtlDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxTtlDiscardsLastIncrementTime.setStatus("current")
_IfTxUnknownDiscards_Type = Counter64
_IfTxUnknownDiscards_Object = MibTableColumn
ifTxUnknownDiscards = _IfTxUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 43),
    _IfTxUnknownDiscards_Type()
)
ifTxUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxUnknownDiscards.setStatus("current")
_IfTxUnknownDiscardsLastIncrement_Type = Counter64
_IfTxUnknownDiscardsLastIncrement_Object = MibTableColumn
ifTxUnknownDiscardsLastIncrement = _IfTxUnknownDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 44),
    _IfTxUnknownDiscardsLastIncrement_Type()
)
ifTxUnknownDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxUnknownDiscardsLastIncrement.setStatus("current")
_IfTxUnknownDiscardsLastIncrementTime_Type = DateAndTime
_IfTxUnknownDiscardsLastIncrementTime_Object = MibTableColumn
ifTxUnknownDiscardsLastIncrementTime = _IfTxUnknownDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 45),
    _IfTxUnknownDiscardsLastIncrementTime_Type()
)
ifTxUnknownDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxUnknownDiscardsLastIncrementTime.setStatus("current")
_IfTxUcastQDrops_Type = Counter64
_IfTxUcastQDrops_Object = MibTableColumn
ifTxUcastQDrops = _IfTxUcastQDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 46),
    _IfTxUcastQDrops_Type()
)
ifTxUcastQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxUcastQDrops.setStatus("current")
_IfTxUcastQDropsLastIncrement_Type = Counter64
_IfTxUcastQDropsLastIncrement_Object = MibTableColumn
ifTxUcastQDropsLastIncrement = _IfTxUcastQDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 47),
    _IfTxUcastQDropsLastIncrement_Type()
)
ifTxUcastQDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxUcastQDropsLastIncrement.setStatus("current")
_IfTxUcastQDropsLastIncrementTime_Type = DateAndTime
_IfTxUcastQDropsLastIncrementTime_Object = MibTableColumn
ifTxUcastQDropsLastIncrementTime = _IfTxUcastQDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 48),
    _IfTxUcastQDropsLastIncrementTime_Type()
)
ifTxUcastQDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxUcastQDropsLastIncrementTime.setStatus("current")
_IfTxMcastQDrops_Type = Counter64
_IfTxMcastQDrops_Object = MibTableColumn
ifTxMcastQDrops = _IfTxMcastQDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 49),
    _IfTxMcastQDrops_Type()
)
ifTxMcastQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxMcastQDrops.setStatus("current")
_IfTxMcastQDropsLastIncrement_Type = Counter64
_IfTxMcastQDropsLastIncrement_Object = MibTableColumn
ifTxMcastQDropsLastIncrement = _IfTxMcastQDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 50),
    _IfTxMcastQDropsLastIncrement_Type()
)
ifTxMcastQDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxMcastQDropsLastIncrement.setStatus("current")
_IfTxMcastQDropsLastIncrementTime_Type = DateAndTime
_IfTxMcastQDropsLastIncrementTime_Object = MibTableColumn
ifTxMcastQDropsLastIncrementTime = _IfTxMcastQDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 51),
    _IfTxMcastQDropsLastIncrementTime_Type()
)
ifTxMcastQDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxMcastQDropsLastIncrementTime.setStatus("current")
_IfObmDrops_Type = Counter64
_IfObmDrops_Object = MibTableColumn
ifObmDrops = _IfObmDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 52),
    _IfObmDrops_Type()
)
ifObmDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifObmDrops.setStatus("current")
_IfObmDropsLastIncrement_Type = Counter64
_IfObmDropsLastIncrement_Object = MibTableColumn
ifObmDropsLastIncrement = _IfObmDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 53),
    _IfObmDropsLastIncrement_Type()
)
ifObmDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifObmDropsLastIncrement.setStatus("current")
_IfObmDropsLastIncrementTime_Type = DateAndTime
_IfObmDropsLastIncrementTime_Object = MibTableColumn
ifObmDropsLastIncrementTime = _IfObmDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 54),
    _IfObmDropsLastIncrementTime_Type()
)
ifObmDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifObmDropsLastIncrementTime.setStatus("current")
_IfObmDropsCntrSize_Type = Integer32
_IfObmDropsCntrSize_Object = MibTableColumn
ifObmDropsCntrSize = _IfObmDropsCntrSize_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 1, 1, 55),
    _IfObmDropsCntrSize_Type()
)
ifObmDropsCntrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifObmDropsCntrSize.setStatus("current")
_IfQueueStatsTable_Object = MibTable
ifQueueStatsTable = _IfQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2)
)
if mibBuilder.loadTexts:
    ifQueueStatsTable.setStatus("current")
_IfQueueStatsEntry_Object = MibTableRow
ifQueueStatsEntry = _IfQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1)
)
ifQueueStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CUSTOMIF-STATS-MIB", "queuetype"),
    (0, "CUSTOMIF-STATS-MIB", "queueId"),
)
if mibBuilder.loadTexts:
    ifQueueStatsEntry.setStatus("current")
_Queuetype_Type = Integer32
_Queuetype_Object = MibTableColumn
queuetype = _Queuetype_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 1),
    _Queuetype_Type()
)
queuetype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queuetype.setStatus("current")


class _QueueId_Type(Integer32):
    """Custom type queueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_QueueId_Type.__name__ = "Integer32"
_QueueId_Object = MibTableColumn
queueId = _QueueId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 2),
    _QueueId_Type()
)
queueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    queueId.setStatus("current")
_QueueName_Type = DisplayString
_QueueName_Object = MibTableColumn
queueName = _QueueName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 3),
    _QueueName_Type()
)
queueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueName.setStatus("current")
_QueueSize_Type = Counter64
_QueueSize_Object = MibTableColumn
queueSize = _QueueSize_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 4),
    _QueueSize_Type()
)
queueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueSize.setStatus("current")
_IfQueueTxPkts_Type = Counter64
_IfQueueTxPkts_Object = MibTableColumn
ifQueueTxPkts = _IfQueueTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 5),
    _IfQueueTxPkts_Type()
)
ifQueueTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQueueTxPkts.setStatus("current")
_IfQueueTxBytes_Type = Counter64
_IfQueueTxBytes_Object = MibTableColumn
ifQueueTxBytes = _IfQueueTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 6),
    _IfQueueTxBytes_Type()
)
ifQueueTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQueueTxBytes.setStatus("current")
_IfQueueDropPkts_Type = Counter64
_IfQueueDropPkts_Object = MibTableColumn
ifQueueDropPkts = _IfQueueDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 7),
    _IfQueueDropPkts_Type()
)
ifQueueDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQueueDropPkts.setStatus("current")
_IfQueueDropBytes_Type = Counter64
_IfQueueDropBytes_Object = MibTableColumn
ifQueueDropBytes = _IfQueueDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 2, 1, 8),
    _IfQueueDropBytes_Type()
)
ifQueueDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifQueueDropBytes.setStatus("current")
_IfProtocolStatsTable_Object = MibTable
ifProtocolStatsTable = _IfProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3)
)
if mibBuilder.loadTexts:
    ifProtocolStatsTable.setStatus("current")
_IfProtocolStatsEntry_Object = MibTableRow
ifProtocolStatsEntry = _IfProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1)
)
ifProtocolStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifProtocolStatsEntry.setStatus("current")
_IfLacpProtocolPkts_Type = Counter32
_IfLacpProtocolPkts_Object = MibTableColumn
ifLacpProtocolPkts = _IfLacpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 1),
    _IfLacpProtocolPkts_Type()
)
ifLacpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLacpProtocolPkts.setStatus("current")
_IfStpProtocolPkts_Type = Counter32
_IfStpProtocolPkts_Object = MibTableColumn
ifStpProtocolPkts = _IfStpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 2),
    _IfStpProtocolPkts_Type()
)
ifStpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifStpProtocolPkts.setStatus("current")
_IfLldpProtocolPkts_Type = Counter32
_IfLldpProtocolPkts_Object = MibTableColumn
ifLldpProtocolPkts = _IfLldpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 3),
    _IfLldpProtocolPkts_Type()
)
ifLldpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLldpProtocolPkts.setStatus("current")
_IfBgpProtocolPkts_Type = Counter32
_IfBgpProtocolPkts_Object = MibTableColumn
ifBgpProtocolPkts = _IfBgpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 4),
    _IfBgpProtocolPkts_Type()
)
ifBgpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBgpProtocolPkts.setStatus("current")
_IfRipProtocolPkts_Type = Counter32
_IfRipProtocolPkts_Object = MibTableColumn
ifRipProtocolPkts = _IfRipProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 5),
    _IfRipProtocolPkts_Type()
)
ifRipProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRipProtocolPkts.setStatus("current")
_IfOspfProtocolPkts_Type = Counter32
_IfOspfProtocolPkts_Object = MibTableColumn
ifOspfProtocolPkts = _IfOspfProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 6),
    _IfOspfProtocolPkts_Type()
)
ifOspfProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOspfProtocolPkts.setStatus("current")
_IfIsisProtocolPkts_Type = Counter32
_IfIsisProtocolPkts_Object = MibTableColumn
ifIsisProtocolPkts = _IfIsisProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 7),
    _IfIsisProtocolPkts_Type()
)
ifIsisProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIsisProtocolPkts.setStatus("current")
_IfEfmProtocolPkts_Type = Counter32
_IfEfmProtocolPkts_Object = MibTableColumn
ifEfmProtocolPkts = _IfEfmProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 8),
    _IfEfmProtocolPkts_Type()
)
ifEfmProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEfmProtocolPkts.setStatus("current")
_IfSlowProtocolPkts_Type = Counter32
_IfSlowProtocolPkts_Object = MibTableColumn
ifSlowProtocolPkts = _IfSlowProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 9),
    _IfSlowProtocolPkts_Type()
)
ifSlowProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSlowProtocolPkts.setStatus("current")
_IfElmiProtocolPkts_Type = Counter32
_IfElmiProtocolPkts_Object = MibTableColumn
ifElmiProtocolPkts = _IfElmiProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 10),
    _IfElmiProtocolPkts_Type()
)
ifElmiProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifElmiProtocolPkts.setStatus("current")
_IfLdpOrRsvpProtocolPkts_Type = Counter32
_IfLdpOrRsvpProtocolPkts_Object = MibTableColumn
ifLdpOrRsvpProtocolPkts = _IfLdpOrRsvpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 11),
    _IfLdpOrRsvpProtocolPkts_Type()
)
ifLdpOrRsvpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLdpOrRsvpProtocolPkts.setStatus("current")
_IfTrillProtocolPkts_Type = Counter32
_IfTrillProtocolPkts_Object = MibTableColumn
ifTrillProtocolPkts = _IfTrillProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 12),
    _IfTrillProtocolPkts_Type()
)
ifTrillProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTrillProtocolPkts.setStatus("current")
_IfIcmp6ProtocolPkts_Type = Counter32
_IfIcmp6ProtocolPkts_Object = MibTableColumn
ifIcmp6ProtocolPkts = _IfIcmp6ProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 13),
    _IfIcmp6ProtocolPkts_Type()
)
ifIcmp6ProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIcmp6ProtocolPkts.setStatus("current")
_IfArpProtocolPkts_Type = Counter32
_IfArpProtocolPkts_Object = MibTableColumn
ifArpProtocolPkts = _IfArpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 14),
    _IfArpProtocolPkts_Type()
)
ifArpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifArpProtocolPkts.setStatus("current")
_IfDhcpProtocolPkts_Type = Counter32
_IfDhcpProtocolPkts_Object = MibTableColumn
ifDhcpProtocolPkts = _IfDhcpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 15),
    _IfDhcpProtocolPkts_Type()
)
ifDhcpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDhcpProtocolPkts.setStatus("current")
_IfVxLanProtocolPkts_Type = Counter32
_IfVxLanProtocolPkts_Object = MibTableColumn
ifVxLanProtocolPkts = _IfVxLanProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 16),
    _IfVxLanProtocolPkts_Type()
)
ifVxLanProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifVxLanProtocolPkts.setStatus("current")
_IfIgmpProtocolPkts_Type = Counter32
_IfIgmpProtocolPkts_Object = MibTableColumn
ifIgmpProtocolPkts = _IfIgmpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 17),
    _IfIgmpProtocolPkts_Type()
)
ifIgmpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIgmpProtocolPkts.setStatus("current")
_IfVrrpProtocolPkts_Type = Counter32
_IfVrrpProtocolPkts_Object = MibTableColumn
ifVrrpProtocolPkts = _IfVrrpProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 18),
    _IfVrrpProtocolPkts_Type()
)
ifVrrpProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifVrrpProtocolPkts.setStatus("current")
_IfPimProtocolPkts_Type = Counter32
_IfPimProtocolPkts_Object = MibTableColumn
ifPimProtocolPkts = _IfPimProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 19),
    _IfPimProtocolPkts_Type()
)
ifPimProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPimProtocolPkts.setStatus("current")
_IfEapolProtocolPkts_Type = Counter32
_IfEapolProtocolPkts_Object = MibTableColumn
ifEapolProtocolPkts = _IfEapolProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 3, 1, 20),
    _IfEapolProtocolPkts_Type()
)
ifEapolProtocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifEapolProtocolPkts.setStatus("current")
_IfRateStatsTable_Object = MibTable
ifRateStatsTable = _IfRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 4)
)
if mibBuilder.loadTexts:
    ifRateStatsTable.setStatus("current")
_IfRateStatsEntry_Object = MibTableRow
ifRateStatsEntry = _IfRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 4, 1)
)
ifRateStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifRateStatsEntry.setStatus("current")
_IfRxRateBps_Type = Counter64
_IfRxRateBps_Object = MibTableColumn
ifRxRateBps = _IfRxRateBps_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 4, 1, 1),
    _IfRxRateBps_Type()
)
ifRxRateBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxRateBps.setStatus("current")
_IfRxRatePps_Type = Counter64
_IfRxRatePps_Object = MibTableColumn
ifRxRatePps = _IfRxRatePps_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 4, 1, 2),
    _IfRxRatePps_Type()
)
ifRxRatePps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifRxRatePps.setStatus("current")
_IfTxRateBps_Type = Counter64
_IfTxRateBps_Object = MibTableColumn
ifTxRateBps = _IfTxRateBps_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 4, 1, 3),
    _IfTxRateBps_Type()
)
ifTxRateBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxRateBps.setStatus("current")
_IfTxRatePps_Type = Counter64
_IfTxRatePps_Object = MibTableColumn
ifTxRatePps = _IfTxRatePps_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 4, 1, 4),
    _IfTxRatePps_Type()
)
ifTxRatePps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTxRatePps.setStatus("current")
_IfFecStatsTable_Object = MibTable
ifFecStatsTable = _IfFecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 5)
)
if mibBuilder.loadTexts:
    ifFecStatsTable.setStatus("current")
_IfFecStatsEntry_Object = MibTableRow
ifFecStatsEntry = _IfFecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 5, 1)
)
ifFecStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifFecStatsEntry.setStatus("current")


class _IfFecMode_Type(Integer32):
    """Custom type ifFecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("auto", 2),
          ("unsupported", 3))
    )


_IfFecMode_Type.__name__ = "Integer32"
_IfFecMode_Object = MibTableColumn
ifFecMode = _IfFecMode_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 5, 1, 1),
    _IfFecMode_Type()
)
ifFecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFecMode.setStatus("current")
_IfFecCorrectedBlocks_Type = Counter32
_IfFecCorrectedBlocks_Object = MibTableColumn
ifFecCorrectedBlocks = _IfFecCorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 5, 1, 2),
    _IfFecCorrectedBlocks_Type()
)
ifFecCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFecCorrectedBlocks.setStatus("current")
_IfFecUncorrectedBlocks_Type = Counter32
_IfFecUncorrectedBlocks_Object = MibTableColumn
ifFecUncorrectedBlocks = _IfFecUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 1, 5, 1, 3),
    _IfFecUncorrectedBlocks_Type()
)
ifFecUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFecUncorrectedBlocks.setStatus("current")
_CpuStatsObjects_ObjectIdentity = ObjectIdentity
cpuStatsObjects = _CpuStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2)
)
_CpuPortDropStatsTable_Object = MibTable
cpuPortDropStatsTable = _CpuPortDropStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1)
)
if mibBuilder.loadTexts:
    cpuPortDropStatsTable.setStatus("current")
_CpuPortDropStatsEntry_Object = MibTableRow
cpuPortDropStatsEntry = _CpuPortDropStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1)
)
cpuPortDropStatsEntry.setIndexNames(
    (0, "CUSTOMIF-STATS-MIB", "cpuId"),
)
if mibBuilder.loadTexts:
    cpuPortDropStatsEntry.setStatus("current")
_CpuId_Type = Integer32
_CpuId_Object = MibTableColumn
cpuId = _CpuId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 1),
    _CpuId_Type()
)
cpuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuId.setStatus("current")
_CpuRxBadCrcErrors_Type = Counter64
_CpuRxBadCrcErrors_Object = MibTableColumn
cpuRxBadCrcErrors = _CpuRxBadCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 2),
    _CpuRxBadCrcErrors_Type()
)
cpuRxBadCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxBadCrcErrors.setStatus("current")
_CpuRxBadCrcLastIncrement_Type = Counter64
_CpuRxBadCrcLastIncrement_Object = MibTableColumn
cpuRxBadCrcLastIncrement = _CpuRxBadCrcLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 3),
    _CpuRxBadCrcLastIncrement_Type()
)
cpuRxBadCrcLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxBadCrcLastIncrement.setStatus("current")
_CpuRxBadCrcLastIncrementTime_Type = DateAndTime
_CpuRxBadCrcLastIncrementTime_Object = MibTableColumn
cpuRxBadCrcLastIncrementTime = _CpuRxBadCrcLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 4),
    _CpuRxBadCrcLastIncrementTime_Type()
)
cpuRxBadCrcLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxBadCrcLastIncrementTime.setStatus("current")
_CpuRxUndersizeErrors_Type = Counter64
_CpuRxUndersizeErrors_Object = MibTableColumn
cpuRxUndersizeErrors = _CpuRxUndersizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 5),
    _CpuRxUndersizeErrors_Type()
)
cpuRxUndersizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxUndersizeErrors.setStatus("current")
_CpuRxUndersizeLastIncrement_Type = Counter64
_CpuRxUndersizeLastIncrement_Object = MibTableColumn
cpuRxUndersizeLastIncrement = _CpuRxUndersizeLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 6),
    _CpuRxUndersizeLastIncrement_Type()
)
cpuRxUndersizeLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxUndersizeLastIncrement.setStatus("current")
_CpuRxUndersizeLastIncrementTime_Type = DateAndTime
_CpuRxUndersizeLastIncrementTime_Object = MibTableColumn
cpuRxUndersizeLastIncrementTime = _CpuRxUndersizeLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 7),
    _CpuRxUndersizeLastIncrementTime_Type()
)
cpuRxUndersizeLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxUndersizeLastIncrementTime.setStatus("current")
_CpuRxOversizeErrors_Type = Counter64
_CpuRxOversizeErrors_Object = MibTableColumn
cpuRxOversizeErrors = _CpuRxOversizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 8),
    _CpuRxOversizeErrors_Type()
)
cpuRxOversizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxOversizeErrors.setStatus("current")
_CpuRxOversizeLastIncrement_Type = Counter64
_CpuRxOversizeLastIncrement_Object = MibTableColumn
cpuRxOversizeLastIncrement = _CpuRxOversizeLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 9),
    _CpuRxOversizeLastIncrement_Type()
)
cpuRxOversizeLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxOversizeLastIncrement.setStatus("current")
_CpuRxOversizeLastIncrementTime_Type = DateAndTime
_CpuRxOversizeLastIncrementTime_Object = MibTableColumn
cpuRxOversizeLastIncrementTime = _CpuRxOversizeLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 10),
    _CpuRxOversizeLastIncrementTime_Type()
)
cpuRxOversizeLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxOversizeLastIncrementTime.setStatus("current")
_CpuRxFragmentErrors_Type = Counter64
_CpuRxFragmentErrors_Object = MibTableColumn
cpuRxFragmentErrors = _CpuRxFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 11),
    _CpuRxFragmentErrors_Type()
)
cpuRxFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxFragmentErrors.setStatus("current")
_CpuRxFragmentLastIncrement_Type = Counter64
_CpuRxFragmentLastIncrement_Object = MibTableColumn
cpuRxFragmentLastIncrement = _CpuRxFragmentLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 12),
    _CpuRxFragmentLastIncrement_Type()
)
cpuRxFragmentLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxFragmentLastIncrement.setStatus("current")
_CpuRxFragmentLastIncrementTime_Type = DateAndTime
_CpuRxFragmentLastIncrementTime_Object = MibTableColumn
cpuRxFragmentLastIncrementTime = _CpuRxFragmentLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 13),
    _CpuRxFragmentLastIncrementTime_Type()
)
cpuRxFragmentLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxFragmentLastIncrementTime.setStatus("current")
_CpuRxJabberErrors_Type = Counter64
_CpuRxJabberErrors_Object = MibTableColumn
cpuRxJabberErrors = _CpuRxJabberErrors_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 14),
    _CpuRxJabberErrors_Type()
)
cpuRxJabberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxJabberErrors.setStatus("current")
_CpuRxJabberLastIncrement_Type = Counter64
_CpuRxJabberLastIncrement_Object = MibTableColumn
cpuRxJabberLastIncrement = _CpuRxJabberLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 15),
    _CpuRxJabberLastIncrement_Type()
)
cpuRxJabberLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxJabberLastIncrement.setStatus("current")
_CpuRxJabberLastIncrementTime_Type = DateAndTime
_CpuRxJabberLastIncrementTime_Object = MibTableColumn
cpuRxJabberLastIncrementTime = _CpuRxJabberLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 16),
    _CpuRxJabberLastIncrementTime_Type()
)
cpuRxJabberLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxJabberLastIncrementTime.setStatus("current")
_CpuRxPortBlockDrops_Type = Counter64
_CpuRxPortBlockDrops_Object = MibTableColumn
cpuRxPortBlockDrops = _CpuRxPortBlockDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 17),
    _CpuRxPortBlockDrops_Type()
)
cpuRxPortBlockDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxPortBlockDrops.setStatus("current")
_CpuRxPortBlockLastIncrement_Type = Counter64
_CpuRxPortBlockLastIncrement_Object = MibTableColumn
cpuRxPortBlockLastIncrement = _CpuRxPortBlockLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 18),
    _CpuRxPortBlockLastIncrement_Type()
)
cpuRxPortBlockLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxPortBlockLastIncrement.setStatus("current")
_CpuRxPortBlockLastIncrementTime_Type = DateAndTime
_CpuRxPortBlockLastIncrementTime_Object = MibTableColumn
cpuRxPortBlockLastIncrementTime = _CpuRxPortBlockLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 19),
    _CpuRxPortBlockLastIncrementTime_Type()
)
cpuRxPortBlockLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxPortBlockLastIncrementTime.setStatus("current")
_CpuRxVlanDiscards_Type = Counter64
_CpuRxVlanDiscards_Object = MibTableColumn
cpuRxVlanDiscards = _CpuRxVlanDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 20),
    _CpuRxVlanDiscards_Type()
)
cpuRxVlanDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxVlanDiscards.setStatus("current")
_CpuRxVlanDiscardsLastIncrement_Type = Counter64
_CpuRxVlanDiscardsLastIncrement_Object = MibTableColumn
cpuRxVlanDiscardsLastIncrement = _CpuRxVlanDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 21),
    _CpuRxVlanDiscardsLastIncrement_Type()
)
cpuRxVlanDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxVlanDiscardsLastIncrement.setStatus("current")
_CpuRxVlanDiscardsLastIncrementTime_Type = DateAndTime
_CpuRxVlanDiscardsLastIncrementTime_Object = MibTableColumn
cpuRxVlanDiscardsLastIncrementTime = _CpuRxVlanDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 22),
    _CpuRxVlanDiscardsLastIncrementTime_Type()
)
cpuRxVlanDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxVlanDiscardsLastIncrementTime.setStatus("current")
_CpuRxAclOrQosDrops_Type = Counter64
_CpuRxAclOrQosDrops_Object = MibTableColumn
cpuRxAclOrQosDrops = _CpuRxAclOrQosDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 23),
    _CpuRxAclOrQosDrops_Type()
)
cpuRxAclOrQosDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxAclOrQosDrops.setStatus("current")
_CpuRxAclOrQosDropsLastIncrement_Type = Counter64
_CpuRxAclOrQosDropsLastIncrement_Object = MibTableColumn
cpuRxAclOrQosDropsLastIncrement = _CpuRxAclOrQosDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 24),
    _CpuRxAclOrQosDropsLastIncrement_Type()
)
cpuRxAclOrQosDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxAclOrQosDropsLastIncrement.setStatus("current")
_CpuRxAclOrQosDropsLastIncrementTime_Type = DateAndTime
_CpuRxAclOrQosDropsLastIncrementTime_Object = MibTableColumn
cpuRxAclOrQosDropsLastIncrementTime = _CpuRxAclOrQosDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 25),
    _CpuRxAclOrQosDropsLastIncrementTime_Type()
)
cpuRxAclOrQosDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxAclOrQosDropsLastIncrementTime.setStatus("current")
_CpuRxPolicyDiscards_Type = Counter64
_CpuRxPolicyDiscards_Object = MibTableColumn
cpuRxPolicyDiscards = _CpuRxPolicyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 26),
    _CpuRxPolicyDiscards_Type()
)
cpuRxPolicyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxPolicyDiscards.setStatus("current")
_CpuRxPolicyDiscardsLastIncrement_Type = Counter64
_CpuRxPolicyDiscardsLastIncrement_Object = MibTableColumn
cpuRxPolicyDiscardsLastIncrement = _CpuRxPolicyDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 27),
    _CpuRxPolicyDiscardsLastIncrement_Type()
)
cpuRxPolicyDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxPolicyDiscardsLastIncrement.setStatus("current")
_CpuRxPolicyDiscardsLastIncrementTime_Type = DateAndTime
_CpuRxPolicyDiscardsLastIncrementTime_Object = MibTableColumn
cpuRxPolicyDiscardsLastIncrementTime = _CpuRxPolicyDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 28),
    _CpuRxPolicyDiscardsLastIncrementTime_Type()
)
cpuRxPolicyDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxPolicyDiscardsLastIncrementTime.setStatus("current")
_CpuRxEgrPortUnavail_Type = Counter64
_CpuRxEgrPortUnavail_Object = MibTableColumn
cpuRxEgrPortUnavail = _CpuRxEgrPortUnavail_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 29),
    _CpuRxEgrPortUnavail_Type()
)
cpuRxEgrPortUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxEgrPortUnavail.setStatus("current")
_CpuRxEgrPortUnavailLastIncrement_Type = Counter64
_CpuRxEgrPortUnavailLastIncrement_Object = MibTableColumn
cpuRxEgrPortUnavailLastIncrement = _CpuRxEgrPortUnavailLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 30),
    _CpuRxEgrPortUnavailLastIncrement_Type()
)
cpuRxEgrPortUnavailLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxEgrPortUnavailLastIncrement.setStatus("current")
_CpuRxEgrPortUnavailLastIncrementTime_Type = DateAndTime
_CpuRxEgrPortUnavailLastIncrementTime_Object = MibTableColumn
cpuRxEgrPortUnavailLastIncrementTime = _CpuRxEgrPortUnavailLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 31),
    _CpuRxEgrPortUnavailLastIncrementTime_Type()
)
cpuRxEgrPortUnavailLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxEgrPortUnavailLastIncrementTime.setStatus("current")
_CpuRxIBPDiscards_Type = Counter64
_CpuRxIBPDiscards_Object = MibTableColumn
cpuRxIBPDiscards = _CpuRxIBPDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 32),
    _CpuRxIBPDiscards_Type()
)
cpuRxIBPDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxIBPDiscards.setStatus("current")
_CpuRxIBPDiscardsLastIncrement_Type = Counter64
_CpuRxIBPDiscardsLastIncrement_Object = MibTableColumn
cpuRxIBPDiscardsLastIncrement = _CpuRxIBPDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 33),
    _CpuRxIBPDiscardsLastIncrement_Type()
)
cpuRxIBPDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxIBPDiscardsLastIncrement.setStatus("current")
_CpuRxIBPDiscardsLastIncrementTime_Type = DateAndTime
_CpuRxIBPDiscardsLastIncrementTime_Object = MibTableColumn
cpuRxIBPDiscardsLastIncrementTime = _CpuRxIBPDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 34),
    _CpuRxIBPDiscardsLastIncrementTime_Type()
)
cpuRxIBPDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuRxIBPDiscardsLastIncrementTime.setStatus("current")
_CpuTxPortBlockDrops_Type = Counter64
_CpuTxPortBlockDrops_Object = MibTableColumn
cpuTxPortBlockDrops = _CpuTxPortBlockDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 35),
    _CpuTxPortBlockDrops_Type()
)
cpuTxPortBlockDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxPortBlockDrops.setStatus("current")
_CpuTxPortBlockDropsLastIncrement_Type = Counter64
_CpuTxPortBlockDropsLastIncrement_Object = MibTableColumn
cpuTxPortBlockDropsLastIncrement = _CpuTxPortBlockDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 36),
    _CpuTxPortBlockDropsLastIncrement_Type()
)
cpuTxPortBlockDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxPortBlockDropsLastIncrement.setStatus("current")
_CpuTxPortBlockDropsLastIncrementTime_Type = DateAndTime
_CpuTxPortBlockDropsLastIncrementTime_Object = MibTableColumn
cpuTxPortBlockDropsLastIncrementTime = _CpuTxPortBlockDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 37),
    _CpuTxPortBlockDropsLastIncrementTime_Type()
)
cpuTxPortBlockDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxPortBlockDropsLastIncrementTime.setStatus("current")
_CpuTxVlanDiscards_Type = Counter64
_CpuTxVlanDiscards_Object = MibTableColumn
cpuTxVlanDiscards = _CpuTxVlanDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 38),
    _CpuTxVlanDiscards_Type()
)
cpuTxVlanDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxVlanDiscards.setStatus("current")
_CpuTxVlanDiscardsLastIncrement_Type = Counter64
_CpuTxVlanDiscardsLastIncrement_Object = MibTableColumn
cpuTxVlanDiscardsLastIncrement = _CpuTxVlanDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 39),
    _CpuTxVlanDiscardsLastIncrement_Type()
)
cpuTxVlanDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxVlanDiscardsLastIncrement.setStatus("current")
_CpuTxVlanDiscardsLastIncrementTime_Type = DateAndTime
_CpuTxVlanDiscardsLastIncrementTime_Object = MibTableColumn
cpuTxVlanDiscardsLastIncrementTime = _CpuTxVlanDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 40),
    _CpuTxVlanDiscardsLastIncrementTime_Type()
)
cpuTxVlanDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxVlanDiscardsLastIncrementTime.setStatus("current")
_CpuTxTtlDiscards_Type = Counter64
_CpuTxTtlDiscards_Object = MibTableColumn
cpuTxTtlDiscards = _CpuTxTtlDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 41),
    _CpuTxTtlDiscards_Type()
)
cpuTxTtlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxTtlDiscards.setStatus("current")
_CpuTxTtlDiscardsLastIncrement_Type = Counter64
_CpuTxTtlDiscardsLastIncrement_Object = MibTableColumn
cpuTxTtlDiscardsLastIncrement = _CpuTxTtlDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 42),
    _CpuTxTtlDiscardsLastIncrement_Type()
)
cpuTxTtlDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxTtlDiscardsLastIncrement.setStatus("current")
_CpuTxTtlDiscardsLastIncrementTime_Type = DateAndTime
_CpuTxTtlDiscardsLastIncrementTime_Object = MibTableColumn
cpuTxTtlDiscardsLastIncrementTime = _CpuTxTtlDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 43),
    _CpuTxTtlDiscardsLastIncrementTime_Type()
)
cpuTxTtlDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxTtlDiscardsLastIncrementTime.setStatus("current")
_CpuTxUnknownDiscards_Type = Counter64
_CpuTxUnknownDiscards_Object = MibTableColumn
cpuTxUnknownDiscards = _CpuTxUnknownDiscards_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 44),
    _CpuTxUnknownDiscards_Type()
)
cpuTxUnknownDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxUnknownDiscards.setStatus("current")
_CpuTxUnknownDiscardsLastIncrement_Type = Counter64
_CpuTxUnknownDiscardsLastIncrement_Object = MibTableColumn
cpuTxUnknownDiscardsLastIncrement = _CpuTxUnknownDiscardsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 45),
    _CpuTxUnknownDiscardsLastIncrement_Type()
)
cpuTxUnknownDiscardsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxUnknownDiscardsLastIncrement.setStatus("current")
_CpuTxUnknownDiscardsLastIncrementTime_Type = DateAndTime
_CpuTxUnknownDiscardsLastIncrementTime_Object = MibTableColumn
cpuTxUnknownDiscardsLastIncrementTime = _CpuTxUnknownDiscardsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 46),
    _CpuTxUnknownDiscardsLastIncrementTime_Type()
)
cpuTxUnknownDiscardsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxUnknownDiscardsLastIncrementTime.setStatus("current")
_CpuTxUcastQDrops_Type = Counter64
_CpuTxUcastQDrops_Object = MibTableColumn
cpuTxUcastQDrops = _CpuTxUcastQDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 47),
    _CpuTxUcastQDrops_Type()
)
cpuTxUcastQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxUcastQDrops.setStatus("current")
_CpuTxUcastQDropsLastIncrement_Type = Counter64
_CpuTxUcastQDropsLastIncrement_Object = MibTableColumn
cpuTxUcastQDropsLastIncrement = _CpuTxUcastQDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 48),
    _CpuTxUcastQDropsLastIncrement_Type()
)
cpuTxUcastQDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxUcastQDropsLastIncrement.setStatus("current")
_CpuTxUcastQDropsLastIncrementTime_Type = DateAndTime
_CpuTxUcastQDropsLastIncrementTime_Object = MibTableColumn
cpuTxUcastQDropsLastIncrementTime = _CpuTxUcastQDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 49),
    _CpuTxUcastQDropsLastIncrementTime_Type()
)
cpuTxUcastQDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxUcastQDropsLastIncrementTime.setStatus("current")
_CpuTxMcastQDrops_Type = Counter64
_CpuTxMcastQDrops_Object = MibTableColumn
cpuTxMcastQDrops = _CpuTxMcastQDrops_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 50),
    _CpuTxMcastQDrops_Type()
)
cpuTxMcastQDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxMcastQDrops.setStatus("current")
_CpuTxMcastQDropsLastIncrement_Type = Counter64
_CpuTxMcastQDropsLastIncrement_Object = MibTableColumn
cpuTxMcastQDropsLastIncrement = _CpuTxMcastQDropsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 51),
    _CpuTxMcastQDropsLastIncrement_Type()
)
cpuTxMcastQDropsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxMcastQDropsLastIncrement.setStatus("current")
_CpuTxMcastQDropsLastIncrementTime_Type = DateAndTime
_CpuTxMcastQDropsLastIncrementTime_Object = MibTableColumn
cpuTxMcastQDropsLastIncrementTime = _CpuTxMcastQDropsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 1, 1, 52),
    _CpuTxMcastQDropsLastIncrementTime_Type()
)
cpuTxMcastQDropsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxMcastQDropsLastIncrementTime.setStatus("current")
_CpuQStatsTable_Object = MibTable
cpuQStatsTable = _CpuQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2)
)
if mibBuilder.loadTexts:
    cpuQStatsTable.setStatus("current")
_CpuQStatsEntry_Object = MibTableRow
cpuQStatsEntry = _CpuQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1)
)
cpuQStatsEntry.setIndexNames(
    (0, "CUSTOMIF-STATS-MIB", "cpuId"),
    (0, "CUSTOMIF-STATS-MIB", "cpuqueueId"),
)
if mibBuilder.loadTexts:
    cpuQStatsEntry.setStatus("current")
_CpuqueueId_Type = Integer32
_CpuqueueId_Object = MibTableColumn
cpuqueueId = _CpuqueueId_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 1),
    _CpuqueueId_Type()
)
cpuqueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpuqueueId.setStatus("current")
_CpuQueueName_Type = DisplayString
_CpuQueueName_Object = MibTableColumn
cpuQueueName = _CpuQueueName_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 2),
    _CpuQueueName_Type()
)
cpuQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuQueueName.setStatus("current")
_CpuQueueSize_Type = Counter64
_CpuQueueSize_Object = MibTableColumn
cpuQueueSize = _CpuQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 3),
    _CpuQueueSize_Type()
)
cpuQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuQueueSize.setStatus("current")
_CpuTxPkts_Type = Counter64
_CpuTxPkts_Object = MibTableColumn
cpuTxPkts = _CpuTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 4),
    _CpuTxPkts_Type()
)
cpuTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxPkts.setStatus("current")
_CpuTxBytes_Type = Counter64
_CpuTxBytes_Object = MibTableColumn
cpuTxBytes = _CpuTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 5),
    _CpuTxBytes_Type()
)
cpuTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxBytes.setStatus("current")
_CpuTxDroppedPkts_Type = Counter64
_CpuTxDroppedPkts_Object = MibTableColumn
cpuTxDroppedPkts = _CpuTxDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 6),
    _CpuTxDroppedPkts_Type()
)
cpuTxDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxDroppedPkts.setStatus("current")
_CpuTxDroppedBytes_Type = Counter64
_CpuTxDroppedBytes_Object = MibTableColumn
cpuTxDroppedBytes = _CpuTxDroppedBytes_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 7),
    _CpuTxDroppedBytes_Type()
)
cpuTxDroppedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxDroppedBytes.setStatus("current")
_CpuTxDroppedPktsLastIncrement_Type = Counter64
_CpuTxDroppedPktsLastIncrement_Object = MibTableColumn
cpuTxDroppedPktsLastIncrement = _CpuTxDroppedPktsLastIncrement_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 8),
    _CpuTxDroppedPktsLastIncrement_Type()
)
cpuTxDroppedPktsLastIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxDroppedPktsLastIncrement.setStatus("current")
_CpuTxDroppedPktsLastIncrementTime_Type = DateAndTime
_CpuTxDroppedPktsLastIncrementTime_Object = MibTableColumn
cpuTxDroppedPktsLastIncrementTime = _CpuTxDroppedPktsLastIncrementTime_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 9),
    _CpuTxDroppedPktsLastIncrementTime_Type()
)
cpuTxDroppedPktsLastIncrementTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxDroppedPktsLastIncrementTime.setStatus("current")
_CpuTxRatePercent_Type = Integer32
_CpuTxRatePercent_Object = MibTableColumn
cpuTxRatePercent = _CpuTxRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 10),
    _CpuTxRatePercent_Type()
)
cpuTxRatePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxRatePercent.setStatus("current")
_CpuTxBps_Type = Integer32
_CpuTxBps_Object = MibTableColumn
cpuTxBps = _CpuTxBps_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 11),
    _CpuTxBps_Type()
)
cpuTxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxBps.setStatus("current")
_CpuTxPps_Type = Integer32
_CpuTxPps_Object = MibTableColumn
cpuTxPps = _CpuTxPps_Object(
    (1, 3, 6, 1, 4, 1, 36673, 103, 2, 2, 1, 12),
    _CpuTxPps_Type()
)
cpuTxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTxPps.setStatus("current")
_CustomIfAlarmObjects_ObjectIdentity = ObjectIdentity
customIfAlarmObjects = _CustomIfAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3)
)
_CustomIfTraps_ObjectIdentity = ObjectIdentity
customIfTraps = _CustomIfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 1)
)
_CpuQueueNotifications_ObjectIdentity = ObjectIdentity
cpuQueueNotifications = _CpuQueueNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 2)
)

# Managed Objects groups


# Notification objects

ifCRCErrorPktsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 1, 1)
)
ifCRCErrorPktsTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CUSTOMIF-STATS-MIB", "ifRxBadCrcLastIncrement"))
)
if mibBuilder.loadTexts:
    ifCRCErrorPktsTrap.setStatus(
        "current"
    )

ifUndersizeErrorPktsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 1, 2)
)
ifUndersizeErrorPktsTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CUSTOMIF-STATS-MIB", "ifRxUndersizeLastIncrement"))
)
if mibBuilder.loadTexts:
    ifUndersizeErrorPktsTrap.setStatus(
        "current"
    )

ifOversizeErrorPktsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 1, 3)
)
ifOversizeErrorPktsTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CUSTOMIF-STATS-MIB", "ifRxOversizeLastIncrement"))
)
if mibBuilder.loadTexts:
    ifOversizeErrorPktsTrap.setStatus(
        "current"
    )

ifFragementErrorPktsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 1, 4)
)
ifFragementErrorPktsTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CUSTOMIF-STATS-MIB", "ifRxFragmentLastIncrement"))
)
if mibBuilder.loadTexts:
    ifFragementErrorPktsTrap.setStatus(
        "current"
    )

ifJabberErrorPktsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 1, 5)
)
ifJabberErrorPktsTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("CUSTOMIF-STATS-MIB", "ifRxJabberLastIncrement"))
)
if mibBuilder.loadTexts:
    ifJabberErrorPktsTrap.setStatus(
        "current"
    )

cpuQueueFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 2, 1)
)
cpuQueueFull.setObjects(
      *(("CUSTOMIF-STATS-MIB", "cpuQueueName"),
        ("CUSTOMIF-STATS-MIB", "cpuTxRatePercent"),
        ("CUSTOMIF-STATS-MIB", "cpuTxPps"),
        ("CUSTOMIF-STATS-MIB", "cpuTxDroppedPktsLastIncrement"),
        ("CUSTOMIF-STATS-MIB", "cpuTxDroppedPktsLastIncrementTime"))
)
if mibBuilder.loadTexts:
    cpuQueueFull.setStatus(
        "current"
    )

cpuQueueHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 2, 2)
)
cpuQueueHigh.setObjects(
      *(("CUSTOMIF-STATS-MIB", "cpuQueueName"),
        ("CUSTOMIF-STATS-MIB", "cpuTxRatePercent"),
        ("CUSTOMIF-STATS-MIB", "cpuTxPps"))
)
if mibBuilder.loadTexts:
    cpuQueueHigh.setStatus(
        "current"
    )

cpuQueueRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 36673, 103, 3, 2, 3)
)
cpuQueueRecovery.setObjects(
      *(("CUSTOMIF-STATS-MIB", "cpuQueueName"),
        ("CUSTOMIF-STATS-MIB", "cpuTxRatePercent"))
)
if mibBuilder.loadTexts:
    cpuQueueRecovery.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUSTOMIF-STATS-MIB",
    **{"customIfMib": customIfMib,
       "customIfTable": customIfTable,
       "ifDropStatsTable": ifDropStatsTable,
       "ifDropStatsEntry": ifDropStatsEntry,
       "ifRxBadCrcErrors": ifRxBadCrcErrors,
       "ifRxBadCrcLastIncrement": ifRxBadCrcLastIncrement,
       "ifRxBadCrcLastIncrementTime": ifRxBadCrcLastIncrementTime,
       "ifRxUndersizeErrors": ifRxUndersizeErrors,
       "ifRxUndersizeLastIncrement": ifRxUndersizeLastIncrement,
       "ifRxUndersizeLastIncrementTime": ifRxUndersizeLastIncrementTime,
       "ifRxOversizeErrors": ifRxOversizeErrors,
       "ifRxOversizeLastIncrement": ifRxOversizeLastIncrement,
       "ifRxOversizeLastIncrementTime": ifRxOversizeLastIncrementTime,
       "ifRxFragmentErrors": ifRxFragmentErrors,
       "ifRxFragmentLastIncrement": ifRxFragmentLastIncrement,
       "ifRxFragmentLastIncrementTime": ifRxFragmentLastIncrementTime,
       "ifRxJabberErrors": ifRxJabberErrors,
       "ifRxJabberLastIncrement": ifRxJabberLastIncrement,
       "ifRxJabberLastIncrementTime": ifRxJabberLastIncrementTime,
       "ifRxPortBlockDrops": ifRxPortBlockDrops,
       "ifRxPortBlockLastIncrement": ifRxPortBlockLastIncrement,
       "ifRxPortBlockLastIncrementTime": ifRxPortBlockLastIncrementTime,
       "ifRxVlanDiscards": ifRxVlanDiscards,
       "ifRxVlanDiscardsLastIncrement": ifRxVlanDiscardsLastIncrement,
       "ifRxVlanDiscardsLastIncrementTime": ifRxVlanDiscardsLastIncrementTime,
       "ifRxAclOrQosDrops": ifRxAclOrQosDrops,
       "ifRxAclOrQosDropsLastIncrement": ifRxAclOrQosDropsLastIncrement,
       "ifRxAclOrQosDropsLastIncrementTime": ifRxAclOrQosDropsLastIncrementTime,
       "ifRxPolicyDiscards": ifRxPolicyDiscards,
       "ifRxPolicyDiscardsLastIncrement": ifRxPolicyDiscardsLastIncrement,
       "ifRxPolicyDiscardsLastIncrementTime": ifRxPolicyDiscardsLastIncrementTime,
       "ifRxEgrPortUnavail": ifRxEgrPortUnavail,
       "ifRxEgrPortUnavailLastIncrement": ifRxEgrPortUnavailLastIncrement,
       "ifRxEgrPortUnavailLastIncrementTime": ifRxEgrPortUnavailLastIncrementTime,
       "ifRxIBPDiscards": ifRxIBPDiscards,
       "ifRxIBPDiscardsLastIncrement": ifRxIBPDiscardsLastIncrement,
       "ifRxIBPDiscardsLastIncrementTime": ifRxIBPDiscardsLastIncrementTime,
       "ifTxPortBlockDrops": ifTxPortBlockDrops,
       "ifTxPortBlockDropsLastIncrement": ifTxPortBlockDropsLastIncrement,
       "ifTxPortBlockDropsLastIncrementTime": ifTxPortBlockDropsLastIncrementTime,
       "ifTxVlanDiscards": ifTxVlanDiscards,
       "ifTxVlanDiscardsLastIncrement": ifTxVlanDiscardsLastIncrement,
       "ifTxVlanDiscardsLastIncrementTime": ifTxVlanDiscardsLastIncrementTime,
       "ifTxTtlDiscards": ifTxTtlDiscards,
       "ifTxTtlDiscardsLastIncrement": ifTxTtlDiscardsLastIncrement,
       "ifTxTtlDiscardsLastIncrementTime": ifTxTtlDiscardsLastIncrementTime,
       "ifTxUnknownDiscards": ifTxUnknownDiscards,
       "ifTxUnknownDiscardsLastIncrement": ifTxUnknownDiscardsLastIncrement,
       "ifTxUnknownDiscardsLastIncrementTime": ifTxUnknownDiscardsLastIncrementTime,
       "ifTxUcastQDrops": ifTxUcastQDrops,
       "ifTxUcastQDropsLastIncrement": ifTxUcastQDropsLastIncrement,
       "ifTxUcastQDropsLastIncrementTime": ifTxUcastQDropsLastIncrementTime,
       "ifTxMcastQDrops": ifTxMcastQDrops,
       "ifTxMcastQDropsLastIncrement": ifTxMcastQDropsLastIncrement,
       "ifTxMcastQDropsLastIncrementTime": ifTxMcastQDropsLastIncrementTime,
       "ifObmDrops": ifObmDrops,
       "ifObmDropsLastIncrement": ifObmDropsLastIncrement,
       "ifObmDropsLastIncrementTime": ifObmDropsLastIncrementTime,
       "ifObmDropsCntrSize": ifObmDropsCntrSize,
       "ifQueueStatsTable": ifQueueStatsTable,
       "ifQueueStatsEntry": ifQueueStatsEntry,
       "queuetype": queuetype,
       "queueId": queueId,
       "queueName": queueName,
       "queueSize": queueSize,
       "ifQueueTxPkts": ifQueueTxPkts,
       "ifQueueTxBytes": ifQueueTxBytes,
       "ifQueueDropPkts": ifQueueDropPkts,
       "ifQueueDropBytes": ifQueueDropBytes,
       "ifProtocolStatsTable": ifProtocolStatsTable,
       "ifProtocolStatsEntry": ifProtocolStatsEntry,
       "ifLacpProtocolPkts": ifLacpProtocolPkts,
       "ifStpProtocolPkts": ifStpProtocolPkts,
       "ifLldpProtocolPkts": ifLldpProtocolPkts,
       "ifBgpProtocolPkts": ifBgpProtocolPkts,
       "ifRipProtocolPkts": ifRipProtocolPkts,
       "ifOspfProtocolPkts": ifOspfProtocolPkts,
       "ifIsisProtocolPkts": ifIsisProtocolPkts,
       "ifEfmProtocolPkts": ifEfmProtocolPkts,
       "ifSlowProtocolPkts": ifSlowProtocolPkts,
       "ifElmiProtocolPkts": ifElmiProtocolPkts,
       "ifLdpOrRsvpProtocolPkts": ifLdpOrRsvpProtocolPkts,
       "ifTrillProtocolPkts": ifTrillProtocolPkts,
       "ifIcmp6ProtocolPkts": ifIcmp6ProtocolPkts,
       "ifArpProtocolPkts": ifArpProtocolPkts,
       "ifDhcpProtocolPkts": ifDhcpProtocolPkts,
       "ifVxLanProtocolPkts": ifVxLanProtocolPkts,
       "ifIgmpProtocolPkts": ifIgmpProtocolPkts,
       "ifVrrpProtocolPkts": ifVrrpProtocolPkts,
       "ifPimProtocolPkts": ifPimProtocolPkts,
       "ifEapolProtocolPkts": ifEapolProtocolPkts,
       "ifRateStatsTable": ifRateStatsTable,
       "ifRateStatsEntry": ifRateStatsEntry,
       "ifRxRateBps": ifRxRateBps,
       "ifRxRatePps": ifRxRatePps,
       "ifTxRateBps": ifTxRateBps,
       "ifTxRatePps": ifTxRatePps,
       "ifFecStatsTable": ifFecStatsTable,
       "ifFecStatsEntry": ifFecStatsEntry,
       "ifFecMode": ifFecMode,
       "ifFecCorrectedBlocks": ifFecCorrectedBlocks,
       "ifFecUncorrectedBlocks": ifFecUncorrectedBlocks,
       "cpuStatsObjects": cpuStatsObjects,
       "cpuPortDropStatsTable": cpuPortDropStatsTable,
       "cpuPortDropStatsEntry": cpuPortDropStatsEntry,
       "cpuId": cpuId,
       "cpuRxBadCrcErrors": cpuRxBadCrcErrors,
       "cpuRxBadCrcLastIncrement": cpuRxBadCrcLastIncrement,
       "cpuRxBadCrcLastIncrementTime": cpuRxBadCrcLastIncrementTime,
       "cpuRxUndersizeErrors": cpuRxUndersizeErrors,
       "cpuRxUndersizeLastIncrement": cpuRxUndersizeLastIncrement,
       "cpuRxUndersizeLastIncrementTime": cpuRxUndersizeLastIncrementTime,
       "cpuRxOversizeErrors": cpuRxOversizeErrors,
       "cpuRxOversizeLastIncrement": cpuRxOversizeLastIncrement,
       "cpuRxOversizeLastIncrementTime": cpuRxOversizeLastIncrementTime,
       "cpuRxFragmentErrors": cpuRxFragmentErrors,
       "cpuRxFragmentLastIncrement": cpuRxFragmentLastIncrement,
       "cpuRxFragmentLastIncrementTime": cpuRxFragmentLastIncrementTime,
       "cpuRxJabberErrors": cpuRxJabberErrors,
       "cpuRxJabberLastIncrement": cpuRxJabberLastIncrement,
       "cpuRxJabberLastIncrementTime": cpuRxJabberLastIncrementTime,
       "cpuRxPortBlockDrops": cpuRxPortBlockDrops,
       "cpuRxPortBlockLastIncrement": cpuRxPortBlockLastIncrement,
       "cpuRxPortBlockLastIncrementTime": cpuRxPortBlockLastIncrementTime,
       "cpuRxVlanDiscards": cpuRxVlanDiscards,
       "cpuRxVlanDiscardsLastIncrement": cpuRxVlanDiscardsLastIncrement,
       "cpuRxVlanDiscardsLastIncrementTime": cpuRxVlanDiscardsLastIncrementTime,
       "cpuRxAclOrQosDrops": cpuRxAclOrQosDrops,
       "cpuRxAclOrQosDropsLastIncrement": cpuRxAclOrQosDropsLastIncrement,
       "cpuRxAclOrQosDropsLastIncrementTime": cpuRxAclOrQosDropsLastIncrementTime,
       "cpuRxPolicyDiscards": cpuRxPolicyDiscards,
       "cpuRxPolicyDiscardsLastIncrement": cpuRxPolicyDiscardsLastIncrement,
       "cpuRxPolicyDiscardsLastIncrementTime": cpuRxPolicyDiscardsLastIncrementTime,
       "cpuRxEgrPortUnavail": cpuRxEgrPortUnavail,
       "cpuRxEgrPortUnavailLastIncrement": cpuRxEgrPortUnavailLastIncrement,
       "cpuRxEgrPortUnavailLastIncrementTime": cpuRxEgrPortUnavailLastIncrementTime,
       "cpuRxIBPDiscards": cpuRxIBPDiscards,
       "cpuRxIBPDiscardsLastIncrement": cpuRxIBPDiscardsLastIncrement,
       "cpuRxIBPDiscardsLastIncrementTime": cpuRxIBPDiscardsLastIncrementTime,
       "cpuTxPortBlockDrops": cpuTxPortBlockDrops,
       "cpuTxPortBlockDropsLastIncrement": cpuTxPortBlockDropsLastIncrement,
       "cpuTxPortBlockDropsLastIncrementTime": cpuTxPortBlockDropsLastIncrementTime,
       "cpuTxVlanDiscards": cpuTxVlanDiscards,
       "cpuTxVlanDiscardsLastIncrement": cpuTxVlanDiscardsLastIncrement,
       "cpuTxVlanDiscardsLastIncrementTime": cpuTxVlanDiscardsLastIncrementTime,
       "cpuTxTtlDiscards": cpuTxTtlDiscards,
       "cpuTxTtlDiscardsLastIncrement": cpuTxTtlDiscardsLastIncrement,
       "cpuTxTtlDiscardsLastIncrementTime": cpuTxTtlDiscardsLastIncrementTime,
       "cpuTxUnknownDiscards": cpuTxUnknownDiscards,
       "cpuTxUnknownDiscardsLastIncrement": cpuTxUnknownDiscardsLastIncrement,
       "cpuTxUnknownDiscardsLastIncrementTime": cpuTxUnknownDiscardsLastIncrementTime,
       "cpuTxUcastQDrops": cpuTxUcastQDrops,
       "cpuTxUcastQDropsLastIncrement": cpuTxUcastQDropsLastIncrement,
       "cpuTxUcastQDropsLastIncrementTime": cpuTxUcastQDropsLastIncrementTime,
       "cpuTxMcastQDrops": cpuTxMcastQDrops,
       "cpuTxMcastQDropsLastIncrement": cpuTxMcastQDropsLastIncrement,
       "cpuTxMcastQDropsLastIncrementTime": cpuTxMcastQDropsLastIncrementTime,
       "cpuQStatsTable": cpuQStatsTable,
       "cpuQStatsEntry": cpuQStatsEntry,
       "cpuqueueId": cpuqueueId,
       "cpuQueueName": cpuQueueName,
       "cpuQueueSize": cpuQueueSize,
       "cpuTxPkts": cpuTxPkts,
       "cpuTxBytes": cpuTxBytes,
       "cpuTxDroppedPkts": cpuTxDroppedPkts,
       "cpuTxDroppedBytes": cpuTxDroppedBytes,
       "cpuTxDroppedPktsLastIncrement": cpuTxDroppedPktsLastIncrement,
       "cpuTxDroppedPktsLastIncrementTime": cpuTxDroppedPktsLastIncrementTime,
       "cpuTxRatePercent": cpuTxRatePercent,
       "cpuTxBps": cpuTxBps,
       "cpuTxPps": cpuTxPps,
       "customIfAlarmObjects": customIfAlarmObjects,
       "customIfTraps": customIfTraps,
       "ifCRCErrorPktsTrap": ifCRCErrorPktsTrap,
       "ifUndersizeErrorPktsTrap": ifUndersizeErrorPktsTrap,
       "ifOversizeErrorPktsTrap": ifOversizeErrorPktsTrap,
       "ifFragementErrorPktsTrap": ifFragementErrorPktsTrap,
       "ifJabberErrorPktsTrap": ifJabberErrorPktsTrap,
       "cpuQueueNotifications": cpuQueueNotifications,
       "cpuQueueFull": cpuQueueFull,
       "cpuQueueHigh": cpuQueueHigh,
       "cpuQueueRecovery": cpuQueueRecovery}
)
