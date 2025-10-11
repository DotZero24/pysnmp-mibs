# SNMP MIB module (RADLAN-RLPFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/RADLAN-RLPFC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:10:23 2025
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlPfcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 148)
)
if mibBuilder.loadTexts:
    rlPfcMib.setRevisions(
        ("2010-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlPfcPriority(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



# MIB Managed Objects in the order of their OIDs

_RlPfcGlobalEnable_Type = TruthValue
_RlPfcGlobalEnable_Object = MibScalar
rlPfcGlobalEnable = _RlPfcGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 1),
    _RlPfcGlobalEnable_Type()
)
rlPfcGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPfcGlobalEnable.setStatus("current")
_RlPfcPortTable_Object = MibTable
rlPfcPortTable = _RlPfcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 2)
)
if mibBuilder.loadTexts:
    rlPfcPortTable.setStatus("current")
_RlPfcPortEntry_Object = MibTableRow
rlPfcPortEntry = _RlPfcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 2, 1)
)
rlPfcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlPfcPortEntry.setStatus("current")
_RlPfcPortEnableAdmin_Type = TruthValue
_RlPfcPortEnableAdmin_Object = MibTableColumn
rlPfcPortEnableAdmin = _RlPfcPortEnableAdmin_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 2, 1, 1),
    _RlPfcPortEnableAdmin_Type()
)
rlPfcPortEnableAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPfcPortEnableAdmin.setStatus("current")
_RlPfcPortEnableOper_Type = TruthValue
_RlPfcPortEnableOper_Object = MibTableColumn
rlPfcPortEnableOper = _RlPfcPortEnableOper_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 2, 1, 2),
    _RlPfcPortEnableOper_Type()
)
rlPfcPortEnableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPfcPortEnableOper.setStatus("current")
_RlPfcPriorityTable_Object = MibTable
rlPfcPriorityTable = _RlPfcPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 3)
)
if mibBuilder.loadTexts:
    rlPfcPriorityTable.setStatus("current")
_RlPfcPriorityEntry_Object = MibTableRow
rlPfcPriorityEntry = _RlPfcPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 3, 1)
)
rlPfcPriorityEntry.setIndexNames(
    (0, "RADLAN-RLPFC-MIB", "rlPfcPriority"),
)
if mibBuilder.loadTexts:
    rlPfcPriorityEntry.setStatus("current")
_RlPfcPriority_Type = RlPfcPriority
_RlPfcPriority_Object = MibTableColumn
rlPfcPriority = _RlPfcPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 3, 1, 1),
    _RlPfcPriority_Type()
)
rlPfcPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPfcPriority.setStatus("current")
_RlPfcPriorityEnable_Type = TruthValue
_RlPfcPriorityEnable_Object = MibTableColumn
rlPfcPriorityEnable = _RlPfcPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 3, 1, 2),
    _RlPfcPriorityEnable_Type()
)
rlPfcPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPfcPriorityEnable.setStatus("current")
_RlPfcPriorityEnableOperStatus_Type = TruthValue
_RlPfcPriorityEnableOperStatus_Object = MibTableColumn
rlPfcPriorityEnableOperStatus = _RlPfcPriorityEnableOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 3, 1, 3),
    _RlPfcPriorityEnableOperStatus_Type()
)
rlPfcPriorityEnableOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPfcPriorityEnableOperStatus.setStatus("current")


class _RlPfcPriorityEnableOperStatusReason_Type(Integer32):
    """Custom type rlPfcPriorityEnableOperStatusReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("pfcGlobalDis", 2),
          ("pfcPriorityAdminDis", 3),
          ("queue0", 4),
          ("sharedQueue", 5),
          ("notSameQueue", 6))
    )


_RlPfcPriorityEnableOperStatusReason_Type.__name__ = "Integer32"
_RlPfcPriorityEnableOperStatusReason_Object = MibTableColumn
rlPfcPriorityEnableOperStatusReason = _RlPfcPriorityEnableOperStatusReason_Object(
    (1, 3, 6, 1, 4, 1, 89, 148, 3, 1, 4),
    _RlPfcPriorityEnableOperStatusReason_Type()
)
rlPfcPriorityEnableOperStatusReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPfcPriorityEnableOperStatusReason.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-RLPFC-MIB",
    **{"RlPfcPriority": RlPfcPriority,
       "rlPfcMib": rlPfcMib,
       "rlPfcGlobalEnable": rlPfcGlobalEnable,
       "rlPfcPortTable": rlPfcPortTable,
       "rlPfcPortEntry": rlPfcPortEntry,
       "rlPfcPortEnableAdmin": rlPfcPortEnableAdmin,
       "rlPfcPortEnableOper": rlPfcPortEnableOper,
       "rlPfcPriorityTable": rlPfcPriorityTable,
       "rlPfcPriorityEntry": rlPfcPriorityEntry,
       "rlPfcPriority": rlPfcPriority,
       "rlPfcPriorityEnable": rlPfcPriorityEnable,
       "rlPfcPriorityEnableOperStatus": rlPfcPriorityEnableOperStatus,
       "rlPfcPriorityEnableOperStatusReason": rlPfcPriorityEnableOperStatusReason}
)
