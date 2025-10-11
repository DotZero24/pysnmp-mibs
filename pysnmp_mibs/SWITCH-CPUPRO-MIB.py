# SNMP MIB module (SWITCH-CPUPRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-CPUPRO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:57 2025
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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcCpuPro = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60)
)
if mibBuilder.loadTexts:
    rcCpuPro.setRevisions(
        ("2010-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcCpuProGroup_ObjectIdentity = ObjectIdentity
rcCpuProGroup = _RcCpuProGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1)
)
_RcCpuProPortTable_Object = MibTable
rcCpuProPortTable = _RcCpuProPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 1)
)
if mibBuilder.loadTexts:
    rcCpuProPortTable.setStatus("current")
_RcCpuProPortEntry_Object = MibTableRow
rcCpuProPortEntry = _RcCpuProPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 1, 1)
)
rcCpuProPortEntry.setIndexNames(
    (0, "SWITCH-CPUPRO-MIB", "rcCpuProPortIndex"),
    (0, "SWITCH-CPUPRO-MIB", "rcCpuProPacketIndex"),
)
if mibBuilder.loadTexts:
    rcCpuProPortEntry.setStatus("current")
_RcCpuProPortIndex_Type = Integer32
_RcCpuProPortIndex_Object = MibTableColumn
rcCpuProPortIndex = _RcCpuProPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 1, 1, 1),
    _RcCpuProPortIndex_Type()
)
rcCpuProPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcCpuProPortIndex.setStatus("current")


class _RcCpuProPortPacketEnable_Type(EnableVar):
    """Custom type rcCpuProPortPacketEnable based on EnableVar"""
    defaultValue = 2


_RcCpuProPortPacketEnable_Type.__name__ = "EnableVar"
_RcCpuProPortPacketEnable_Object = MibTableColumn
rcCpuProPortPacketEnable = _RcCpuProPortPacketEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 1, 1, 2),
    _RcCpuProPortPacketEnable_Type()
)
rcCpuProPortPacketEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuProPortPacketEnable.setStatus("current")


class _RcCpuProPortPacketAttackStatus_Type(Integer32):
    """Custom type rcCpuProPortPacketAttackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attacking", 1),
          ("not-attacking", 2))
    )


_RcCpuProPortPacketAttackStatus_Type.__name__ = "Integer32"
_RcCpuProPortPacketAttackStatus_Object = MibTableColumn
rcCpuProPortPacketAttackStatus = _RcCpuProPortPacketAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 1, 1, 3),
    _RcCpuProPortPacketAttackStatus_Type()
)
rcCpuProPortPacketAttackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuProPortPacketAttackStatus.setStatus("current")
_RcCpuProPortPacketAttackedCount_Type = Counter32
_RcCpuProPortPacketAttackedCount_Object = MibTableColumn
rcCpuProPortPacketAttackedCount = _RcCpuProPortPacketAttackedCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 1, 1, 4),
    _RcCpuProPortPacketAttackedCount_Type()
)
rcCpuProPortPacketAttackedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuProPortPacketAttackedCount.setStatus("current")
_RcCpuProPacketTable_Object = MibTable
rcCpuProPacketTable = _RcCpuProPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2)
)
if mibBuilder.loadTexts:
    rcCpuProPacketTable.setStatus("current")
_RcCpuProPacketEntry_Object = MibTableRow
rcCpuProPacketEntry = _RcCpuProPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2, 1)
)
rcCpuProPacketEntry.setIndexNames(
    (0, "SWITCH-CPUPRO-MIB", "rcCpuProPacketIndex"),
)
if mibBuilder.loadTexts:
    rcCpuProPacketEntry.setStatus("current")


class _RcCpuProPacketIndex_Type(Integer32):
    """Custom type rcCpuProPacketIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bpdu", 1),
          ("arp", 2),
          ("icmp", 3))
    )


_RcCpuProPacketIndex_Type.__name__ = "Integer32"
_RcCpuProPacketIndex_Object = MibTableColumn
rcCpuProPacketIndex = _RcCpuProPacketIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2, 1, 1),
    _RcCpuProPacketIndex_Type()
)
rcCpuProPacketIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuProPacketIndex.setStatus("current")


class _RcCpuProPacketInterval_Type(Integer32):
    """Custom type rcCpuProPacketInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcCpuProPacketInterval_Type.__name__ = "Integer32"
_RcCpuProPacketInterval_Object = MibTableColumn
rcCpuProPacketInterval = _RcCpuProPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2, 1, 2),
    _RcCpuProPacketInterval_Type()
)
rcCpuProPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuProPacketInterval.setStatus("current")


class _RcCpuProPacketHigh_Type(Integer32):
    """Custom type rcCpuProPacketHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_RcCpuProPacketHigh_Type.__name__ = "Integer32"
_RcCpuProPacketHigh_Object = MibTableColumn
rcCpuProPacketHigh = _RcCpuProPacketHigh_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2, 1, 3),
    _RcCpuProPacketHigh_Type()
)
rcCpuProPacketHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuProPacketHigh.setStatus("current")


class _RcCpuProPacketLow_Type(Integer32):
    """Custom type rcCpuProPacketLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcCpuProPacketLow_Type.__name__ = "Integer32"
_RcCpuProPacketLow_Object = MibTableColumn
rcCpuProPacketLow = _RcCpuProPacketLow_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2, 1, 4),
    _RcCpuProPacketLow_Type()
)
rcCpuProPacketLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCpuProPacketLow.setStatus("current")


class _RcCpuProPacketAction_Type(Integer32):
    """Custom type rcCpuProPacketAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("filter", 2),
          ("deny", 3))
    )


_RcCpuProPacketAction_Type.__name__ = "Integer32"
_RcCpuProPacketAction_Object = MibTableColumn
rcCpuProPacketAction = _RcCpuProPacketAction_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 60, 1, 2, 1, 5),
    _RcCpuProPacketAction_Type()
)
rcCpuProPacketAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcCpuProPacketAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-CPUPRO-MIB",
    **{"rcCpuPro": rcCpuPro,
       "rcCpuProGroup": rcCpuProGroup,
       "rcCpuProPortTable": rcCpuProPortTable,
       "rcCpuProPortEntry": rcCpuProPortEntry,
       "rcCpuProPortIndex": rcCpuProPortIndex,
       "rcCpuProPortPacketEnable": rcCpuProPortPacketEnable,
       "rcCpuProPortPacketAttackStatus": rcCpuProPortPacketAttackStatus,
       "rcCpuProPortPacketAttackedCount": rcCpuProPortPacketAttackedCount,
       "rcCpuProPacketTable": rcCpuProPacketTable,
       "rcCpuProPacketEntry": rcCpuProPacketEntry,
       "rcCpuProPacketIndex": rcCpuProPacketIndex,
       "rcCpuProPacketInterval": rcCpuProPacketInterval,
       "rcCpuProPacketHigh": rcCpuProPacketHigh,
       "rcCpuProPacketLow": rcCpuProPacketLow,
       "rcCpuProPacketAction": rcCpuProPacketAction}
)
