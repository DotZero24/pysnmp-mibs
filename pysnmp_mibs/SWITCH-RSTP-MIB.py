# SNMP MIB module (SWITCH-RSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-RSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:05 2025
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

(dot1dStpPortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPortEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcRstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9)
)
if mibBuilder.loadTexts:
    rcRstp.setRevisions(
        ("1991-03-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRstpConfig_ObjectIdentity = ObjectIdentity
rcRstpConfig = _RcRstpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 1)
)


class _RcRstpEnable_Type(TruthValue):
    """Custom type rcRstpEnable based on TruthValue"""
    defaultValue = 1


_RcRstpEnable_Type.__name__ = "TruthValue"
_RcRstpEnable_Object = MibScalar
rcRstpEnable = _RcRstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 1, 1),
    _RcRstpEnable_Type()
)
rcRstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRstpEnable.setStatus("current")
_RcRstpPortConfigTable_Object = MibTable
rcRstpPortConfigTable = _RcRstpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    rcRstpPortConfigTable.setStatus("current")
_RcRstpPortConfigEntry_Object = MibTableRow
rcRstpPortConfigEntry = _RcRstpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcRstpPortConfigEntry.setStatus("current")
_RcRstpPortRstpEnable_Type = TruthValue
_RcRstpPortRstpEnable_Object = MibTableColumn
rcRstpPortRstpEnable = _RcRstpPortRstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 1, 2, 1, 1),
    _RcRstpPortRstpEnable_Type()
)
rcRstpPortRstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRstpPortRstpEnable.setStatus("current")
_RcRstpPortOperEnable_Type = TruthValue
_RcRstpPortOperEnable_Object = MibTableColumn
rcRstpPortOperEnable = _RcRstpPortOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 1, 2, 1, 2),
    _RcRstpPortOperEnable_Type()
)
rcRstpPortOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortOperEnable.setStatus("current")
_RcRstpStatistics_ObjectIdentity = ObjectIdentity
rcRstpStatistics = _RcRstpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2)
)
_RcRstpPortStatsTable_Object = MibTable
rcRstpPortStatsTable = _RcRstpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    rcRstpPortStatsTable.setStatus("current")
_RcRstpPortStatsEntry_Object = MibTableRow
rcRstpPortStatsEntry = _RcRstpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcRstpPortStatsEntry.setStatus("current")
_RcRstpPortRxStpBPDUs_Type = Counter32
_RcRstpPortRxStpBPDUs_Object = MibTableColumn
rcRstpPortRxStpBPDUs = _RcRstpPortRxStpBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 1),
    _RcRstpPortRxStpBPDUs_Type()
)
rcRstpPortRxStpBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortRxStpBPDUs.setStatus("current")
_RcRstpPortRxTCNs_Type = Counter32
_RcRstpPortRxTCNs_Object = MibTableColumn
rcRstpPortRxTCNs = _RcRstpPortRxTCNs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 2),
    _RcRstpPortRxTCNs_Type()
)
rcRstpPortRxTCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortRxTCNs.setStatus("current")
_RcRstpPortRxRstpBPDUs_Type = Counter32
_RcRstpPortRxRstpBPDUs_Object = MibTableColumn
rcRstpPortRxRstpBPDUs = _RcRstpPortRxRstpBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 3),
    _RcRstpPortRxRstpBPDUs_Type()
)
rcRstpPortRxRstpBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortRxRstpBPDUs.setStatus("current")
_RcRstpPortTxStpBPDUs_Type = Counter32
_RcRstpPortTxStpBPDUs_Object = MibTableColumn
rcRstpPortTxStpBPDUs = _RcRstpPortTxStpBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 4),
    _RcRstpPortTxStpBPDUs_Type()
)
rcRstpPortTxStpBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortTxStpBPDUs.setStatus("current")
_RcRstpPortTxTCNs_Type = Counter32
_RcRstpPortTxTCNs_Object = MibTableColumn
rcRstpPortTxTCNs = _RcRstpPortTxTCNs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 5),
    _RcRstpPortTxTCNs_Type()
)
rcRstpPortTxTCNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortTxTCNs.setStatus("current")
_RcRstpPortTxRstpBPDUs_Type = Counter32
_RcRstpPortTxRstpBPDUs_Object = MibTableColumn
rcRstpPortTxRstpBPDUs = _RcRstpPortTxRstpBPDUs_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 6),
    _RcRstpPortTxRstpBPDUs_Type()
)
rcRstpPortTxRstpBPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpPortTxRstpBPDUs.setStatus("current")
_RcRstpPortStatisticsClear_Type = TruthValue
_RcRstpPortStatisticsClear_Object = MibTableColumn
rcRstpPortStatisticsClear = _RcRstpPortStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 9, 2, 1, 1, 7),
    _RcRstpPortStatisticsClear_Type()
)
rcRstpPortStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRstpPortStatisticsClear.setStatus("current")
dot1dStpPortEntry.registerAugmentions(
    ("SWITCH-RSTP-MIB",
     "rcRstpPortConfigEntry")
)
rcRstpPortConfigEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
dot1dStpPortEntry.registerAugmentions(
    ("SWITCH-RSTP-MIB",
     "rcRstpPortStatsEntry")
)
rcRstpPortStatsEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-RSTP-MIB",
    **{"rcRstp": rcRstp,
       "rcRstpConfig": rcRstpConfig,
       "rcRstpEnable": rcRstpEnable,
       "rcRstpPortConfigTable": rcRstpPortConfigTable,
       "rcRstpPortConfigEntry": rcRstpPortConfigEntry,
       "rcRstpPortRstpEnable": rcRstpPortRstpEnable,
       "rcRstpPortOperEnable": rcRstpPortOperEnable,
       "rcRstpStatistics": rcRstpStatistics,
       "rcRstpPortStatsTable": rcRstpPortStatsTable,
       "rcRstpPortStatsEntry": rcRstpPortStatsEntry,
       "rcRstpPortRxStpBPDUs": rcRstpPortRxStpBPDUs,
       "rcRstpPortRxTCNs": rcRstpPortRxTCNs,
       "rcRstpPortRxRstpBPDUs": rcRstpPortRxRstpBPDUs,
       "rcRstpPortTxStpBPDUs": rcRstpPortTxStpBPDUs,
       "rcRstpPortTxTCNs": rcRstpPortTxTCNs,
       "rcRstpPortTxRstpBPDUs": rcRstpPortTxRstpBPDUs,
       "rcRstpPortStatisticsClear": rcRstpPortStatisticsClear}
)
