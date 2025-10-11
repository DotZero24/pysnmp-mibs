# SNMP MIB module (MELLANOX-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:42 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(mellanoxQoS,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxQoS")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mellanoxQoSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1)
)
if mibBuilder.loadTexts:
    mellanoxQoSMib.setRevisions(
        ("2017-07-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MellanoxQoSPrioTable_Object = MibTable
mellanoxQoSPrioTable = _MellanoxQoSPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1)
)
if mibBuilder.loadTexts:
    mellanoxQoSPrioTable.setStatus("current")
_MellanoxQoSPrioEntry_Object = MibTableRow
mellanoxQoSPrioEntry = _MellanoxQoSPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1)
)
mellanoxQoSPrioEntry.setIndexNames(
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPrioIfIndex"),
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPrioIndex"),
)
if mibBuilder.loadTexts:
    mellanoxQoSPrioEntry.setStatus("current")
_MellanoxQoSPrioIfIndex_Type = InterfaceIndex
_MellanoxQoSPrioIfIndex_Object = MibTableColumn
mellanoxQoSPrioIfIndex = _MellanoxQoSPrioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 1),
    _MellanoxQoSPrioIfIndex_Type()
)
mellanoxQoSPrioIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioIfIndex.setStatus("current")
_MellanoxQoSPrioIndex_Type = Integer32
_MellanoxQoSPrioIndex_Object = MibTableColumn
mellanoxQoSPrioIndex = _MellanoxQoSPrioIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 2),
    _MellanoxQoSPrioIndex_Type()
)
mellanoxQoSPrioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioIndex.setStatus("current")
_MellanoxQoSPrioRxPkts_Type = Counter64
_MellanoxQoSPrioRxPkts_Object = MibTableColumn
mellanoxQoSPrioRxPkts = _MellanoxQoSPrioRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 3),
    _MellanoxQoSPrioRxPkts_Type()
)
mellanoxQoSPrioRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxPkts.setStatus("current")
_MellanoxQoSPrioRxUcastPkts_Type = Counter64
_MellanoxQoSPrioRxUcastPkts_Object = MibTableColumn
mellanoxQoSPrioRxUcastPkts = _MellanoxQoSPrioRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 4),
    _MellanoxQoSPrioRxUcastPkts_Type()
)
mellanoxQoSPrioRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxUcastPkts.setStatus("current")
_MellanoxQoSPrioRxMcastPkts_Type = Counter64
_MellanoxQoSPrioRxMcastPkts_Object = MibTableColumn
mellanoxQoSPrioRxMcastPkts = _MellanoxQoSPrioRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 5),
    _MellanoxQoSPrioRxMcastPkts_Type()
)
mellanoxQoSPrioRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxMcastPkts.setStatus("current")
_MellanoxQoSPrioRxBcastPkts_Type = Counter64
_MellanoxQoSPrioRxBcastPkts_Object = MibTableColumn
mellanoxQoSPrioRxBcastPkts = _MellanoxQoSPrioRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 6),
    _MellanoxQoSPrioRxBcastPkts_Type()
)
mellanoxQoSPrioRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxBcastPkts.setStatus("current")
_MellanoxQoSPrioRxBytes_Type = Counter64
_MellanoxQoSPrioRxBytes_Object = MibTableColumn
mellanoxQoSPrioRxBytes = _MellanoxQoSPrioRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 7),
    _MellanoxQoSPrioRxBytes_Type()
)
mellanoxQoSPrioRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxBytes.setStatus("current")
_MellanoxQoSPrioRxPausePkts_Type = Counter64
_MellanoxQoSPrioRxPausePkts_Object = MibTableColumn
mellanoxQoSPrioRxPausePkts = _MellanoxQoSPrioRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 8),
    _MellanoxQoSPrioRxPausePkts_Type()
)
mellanoxQoSPrioRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxPausePkts.setStatus("current")
_MellanoxQoSPrioRxPauseDuration_Type = Counter64
_MellanoxQoSPrioRxPauseDuration_Object = MibTableColumn
mellanoxQoSPrioRxPauseDuration = _MellanoxQoSPrioRxPauseDuration_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 9),
    _MellanoxQoSPrioRxPauseDuration_Type()
)
mellanoxQoSPrioRxPauseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioRxPauseDuration.setStatus("current")
_MellanoxQoSPrioTxPkts_Type = Counter64
_MellanoxQoSPrioTxPkts_Object = MibTableColumn
mellanoxQoSPrioTxPkts = _MellanoxQoSPrioTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 10),
    _MellanoxQoSPrioTxPkts_Type()
)
mellanoxQoSPrioTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioTxPkts.setStatus("current")
_MellanoxQoSPrioTxUcastPkts_Type = Counter64
_MellanoxQoSPrioTxUcastPkts_Object = MibTableColumn
mellanoxQoSPrioTxUcastPkts = _MellanoxQoSPrioTxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 11),
    _MellanoxQoSPrioTxUcastPkts_Type()
)
mellanoxQoSPrioTxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioTxUcastPkts.setStatus("current")
_MellanoxQoSPrioTxMcastPkts_Type = Counter64
_MellanoxQoSPrioTxMcastPkts_Object = MibTableColumn
mellanoxQoSPrioTxMcastPkts = _MellanoxQoSPrioTxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 12),
    _MellanoxQoSPrioTxMcastPkts_Type()
)
mellanoxQoSPrioTxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioTxMcastPkts.setStatus("current")
_MellanoxQoSPrioTxBcastPkts_Type = Counter64
_MellanoxQoSPrioTxBcastPkts_Object = MibTableColumn
mellanoxQoSPrioTxBcastPkts = _MellanoxQoSPrioTxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 13),
    _MellanoxQoSPrioTxBcastPkts_Type()
)
mellanoxQoSPrioTxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioTxBcastPkts.setStatus("current")
_MellanoxQoSPrioTxBytes_Type = Counter64
_MellanoxQoSPrioTxBytes_Object = MibTableColumn
mellanoxQoSPrioTxBytes = _MellanoxQoSPrioTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 14),
    _MellanoxQoSPrioTxBytes_Type()
)
mellanoxQoSPrioTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioTxBytes.setStatus("current")
_MellanoxQoSPrioTxPausePkts_Type = Counter64
_MellanoxQoSPrioTxPausePkts_Object = MibTableColumn
mellanoxQoSPrioTxPausePkts = _MellanoxQoSPrioTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 1, 1, 15),
    _MellanoxQoSPrioTxPausePkts_Type()
)
mellanoxQoSPrioTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPrioTxPausePkts.setStatus("current")
_MellanoxQoSPFCTable_Object = MibTable
mellanoxQoSPFCTable = _MellanoxQoSPFCTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2)
)
if mibBuilder.loadTexts:
    mellanoxQoSPFCTable.setStatus("current")
_MellanoxQoSPFCEntry_Object = MibTableRow
mellanoxQoSPFCEntry = _MellanoxQoSPFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1)
)
mellanoxQoSPFCEntry.setIndexNames(
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPFCIfIndex"),
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPFCIndex"),
)
if mibBuilder.loadTexts:
    mellanoxQoSPFCEntry.setStatus("current")
_MellanoxQoSPFCIfIndex_Type = InterfaceIndex
_MellanoxQoSPFCIfIndex_Object = MibTableColumn
mellanoxQoSPFCIfIndex = _MellanoxQoSPFCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1, 1),
    _MellanoxQoSPFCIfIndex_Type()
)
mellanoxQoSPFCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPFCIfIndex.setStatus("current")
_MellanoxQoSPFCIndex_Type = Integer32
_MellanoxQoSPFCIndex_Object = MibTableColumn
mellanoxQoSPFCIndex = _MellanoxQoSPFCIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1, 2),
    _MellanoxQoSPFCIndex_Type()
)
mellanoxQoSPFCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPFCIndex.setStatus("current")
_MellanoxQoSPFCRxPausePkts_Type = Counter64
_MellanoxQoSPFCRxPausePkts_Object = MibTableColumn
mellanoxQoSPFCRxPausePkts = _MellanoxQoSPFCRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1, 3),
    _MellanoxQoSPFCRxPausePkts_Type()
)
mellanoxQoSPFCRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPFCRxPausePkts.setStatus("current")
_MellanoxQoSPFCRxPauseDuration_Type = Counter64
_MellanoxQoSPFCRxPauseDuration_Object = MibTableColumn
mellanoxQoSPFCRxPauseDuration = _MellanoxQoSPFCRxPauseDuration_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1, 4),
    _MellanoxQoSPFCRxPauseDuration_Type()
)
mellanoxQoSPFCRxPauseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPFCRxPauseDuration.setStatus("current")
_MellanoxQoSPFCTxPausePkts_Type = Counter64
_MellanoxQoSPFCTxPausePkts_Object = MibTableColumn
mellanoxQoSPFCTxPausePkts = _MellanoxQoSPFCTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1, 5),
    _MellanoxQoSPFCTxPausePkts_Type()
)
mellanoxQoSPFCTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPFCTxPausePkts.setStatus("current")
_MellanoxQoSPFCTxPauseDuration_Type = Counter64
_MellanoxQoSPFCTxPauseDuration_Object = MibTableColumn
mellanoxQoSPFCTxPauseDuration = _MellanoxQoSPFCTxPauseDuration_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 2, 1, 6),
    _MellanoxQoSPFCTxPauseDuration_Type()
)
mellanoxQoSPFCTxPauseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPFCTxPauseDuration.setStatus("current")
_MellanoxQoSPGTable_Object = MibTable
mellanoxQoSPGTable = _MellanoxQoSPGTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3)
)
if mibBuilder.loadTexts:
    mellanoxQoSPGTable.setStatus("current")
_MellanoxQoSPGEntry_Object = MibTableRow
mellanoxQoSPGEntry = _MellanoxQoSPGEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1)
)
mellanoxQoSPGEntry.setIndexNames(
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPGIfIndex"),
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPGIndex"),
)
if mibBuilder.loadTexts:
    mellanoxQoSPGEntry.setStatus("current")
_MellanoxQoSPGIfIndex_Type = InterfaceIndex
_MellanoxQoSPGIfIndex_Object = MibTableColumn
mellanoxQoSPGIfIndex = _MellanoxQoSPGIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 1),
    _MellanoxQoSPGIfIndex_Type()
)
mellanoxQoSPGIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGIfIndex.setStatus("current")
_MellanoxQoSPGIndex_Type = Integer32
_MellanoxQoSPGIndex_Object = MibTableColumn
mellanoxQoSPGIndex = _MellanoxQoSPGIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 2),
    _MellanoxQoSPGIndex_Type()
)
mellanoxQoSPGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGIndex.setStatus("current")
_MellanoxQoSPGPkts_Type = Counter64
_MellanoxQoSPGPkts_Object = MibTableColumn
mellanoxQoSPGPkts = _MellanoxQoSPGPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 3),
    _MellanoxQoSPGPkts_Type()
)
mellanoxQoSPGPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGPkts.setStatus("current")
_MellanoxQoSPGBytes_Type = Counter64
_MellanoxQoSPGBytes_Object = MibTableColumn
mellanoxQoSPGBytes = _MellanoxQoSPGBytes_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 4),
    _MellanoxQoSPGBytes_Type()
)
mellanoxQoSPGBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGBytes.setStatus("current")
_MellanoxQoSPGQueueDepth_Type = Counter64
_MellanoxQoSPGQueueDepth_Object = MibTableColumn
mellanoxQoSPGQueueDepth = _MellanoxQoSPGQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 5),
    _MellanoxQoSPGQueueDepth_Type()
)
mellanoxQoSPGQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGQueueDepth.setStatus("current")
_MellanoxQoSPGNoBufferDiscard_Type = Counter64
_MellanoxQoSPGNoBufferDiscard_Object = MibTableColumn
mellanoxQoSPGNoBufferDiscard = _MellanoxQoSPGNoBufferDiscard_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 6),
    _MellanoxQoSPGNoBufferDiscard_Type()
)
mellanoxQoSPGNoBufferDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGNoBufferDiscard.setStatus("current")
_MellanoxQoSPGSharedBufferDiscard_Type = Counter64
_MellanoxQoSPGSharedBufferDiscard_Object = MibTableColumn
mellanoxQoSPGSharedBufferDiscard = _MellanoxQoSPGSharedBufferDiscard_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 3, 1, 7),
    _MellanoxQoSPGSharedBufferDiscard_Type()
)
mellanoxQoSPGSharedBufferDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPGSharedBufferDiscard.setStatus("current")
_MellanoxQoSTCTable_Object = MibTable
mellanoxQoSTCTable = _MellanoxQoSTCTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4)
)
if mibBuilder.loadTexts:
    mellanoxQoSTCTable.setStatus("current")
_MellanoxQoSTCEntry_Object = MibTableRow
mellanoxQoSTCEntry = _MellanoxQoSTCEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1)
)
mellanoxQoSTCEntry.setIndexNames(
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSTCIfIndex"),
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSTCIndex"),
)
if mibBuilder.loadTexts:
    mellanoxQoSTCEntry.setStatus("current")
_MellanoxQoSTCIfIndex_Type = InterfaceIndex
_MellanoxQoSTCIfIndex_Object = MibTableColumn
mellanoxQoSTCIfIndex = _MellanoxQoSTCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 1),
    _MellanoxQoSTCIfIndex_Type()
)
mellanoxQoSTCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCIfIndex.setStatus("current")
_MellanoxQoSTCIndex_Type = Integer32
_MellanoxQoSTCIndex_Object = MibTableColumn
mellanoxQoSTCIndex = _MellanoxQoSTCIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 2),
    _MellanoxQoSTCIndex_Type()
)
mellanoxQoSTCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCIndex.setStatus("current")
_MellanoxQoSTCPkts_Type = Counter64
_MellanoxQoSTCPkts_Object = MibTableColumn
mellanoxQoSTCPkts = _MellanoxQoSTCPkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 3),
    _MellanoxQoSTCPkts_Type()
)
mellanoxQoSTCPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCPkts.setStatus("current")
_MellanoxQoSTCBytes_Type = Counter64
_MellanoxQoSTCBytes_Object = MibTableColumn
mellanoxQoSTCBytes = _MellanoxQoSTCBytes_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 4),
    _MellanoxQoSTCBytes_Type()
)
mellanoxQoSTCBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCBytes.setStatus("current")
_MellanoxQoSTCSXQueueDepth_Type = Counter64
_MellanoxQoSTCSXQueueDepth_Object = MibTableColumn
mellanoxQoSTCSXQueueDepth = _MellanoxQoSTCSXQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 5),
    _MellanoxQoSTCSXQueueDepth_Type()
)
mellanoxQoSTCSXQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCSXQueueDepth.setStatus("current")
_MellanoxQoSTCUnicastQueueDepth_Type = Counter64
_MellanoxQoSTCUnicastQueueDepth_Object = MibTableColumn
mellanoxQoSTCUnicastQueueDepth = _MellanoxQoSTCUnicastQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 6),
    _MellanoxQoSTCUnicastQueueDepth_Type()
)
mellanoxQoSTCUnicastQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCUnicastQueueDepth.setStatus("current")
_MellanoxQoSTCMulticastQueueDepth_Type = Counter64
_MellanoxQoSTCMulticastQueueDepth_Object = MibTableColumn
mellanoxQoSTCMulticastQueueDepth = _MellanoxQoSTCMulticastQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 7),
    _MellanoxQoSTCMulticastQueueDepth_Type()
)
mellanoxQoSTCMulticastQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCMulticastQueueDepth.setStatus("current")
_MellanoxQoSTCUnicastNoBufferDiscard_Type = Counter64
_MellanoxQoSTCUnicastNoBufferDiscard_Object = MibTableColumn
mellanoxQoSTCUnicastNoBufferDiscard = _MellanoxQoSTCUnicastNoBufferDiscard_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 8),
    _MellanoxQoSTCUnicastNoBufferDiscard_Type()
)
mellanoxQoSTCUnicastNoBufferDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCUnicastNoBufferDiscard.setStatus("current")
_MellanoxQoSTCWREDDiscard_Type = Counter64
_MellanoxQoSTCWREDDiscard_Object = MibTableColumn
mellanoxQoSTCWREDDiscard = _MellanoxQoSTCWREDDiscard_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 4, 1, 9),
    _MellanoxQoSTCWREDDiscard_Type()
)
mellanoxQoSTCWREDDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSTCWREDDiscard.setStatus("current")
_MellanoxQoSPortTable_Object = MibTable
mellanoxQoSPortTable = _MellanoxQoSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5)
)
if mibBuilder.loadTexts:
    mellanoxQoSPortTable.setStatus("current")
_MellanoxQoSPortEntry_Object = MibTableRow
mellanoxQoSPortEntry = _MellanoxQoSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5, 1)
)
mellanoxQoSPortEntry.setIndexNames(
    (0, "MELLANOX-QOS-MIB", "mellanoxQoSPortIfIndex"),
)
if mibBuilder.loadTexts:
    mellanoxQoSPortEntry.setStatus("current")
_MellanoxQoSPortIfIndex_Type = InterfaceIndex
_MellanoxQoSPortIfIndex_Object = MibTableColumn
mellanoxQoSPortIfIndex = _MellanoxQoSPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5, 1, 1),
    _MellanoxQoSPortIfIndex_Type()
)
mellanoxQoSPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPortIfIndex.setStatus("current")
_MellanoxQoSPortRxPausePkts_Type = Counter64
_MellanoxQoSPortRxPausePkts_Object = MibTableColumn
mellanoxQoSPortRxPausePkts = _MellanoxQoSPortRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5, 1, 2),
    _MellanoxQoSPortRxPausePkts_Type()
)
mellanoxQoSPortRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPortRxPausePkts.setStatus("current")
_MellanoxQoSPortTxPausePkts_Type = Counter64
_MellanoxQoSPortTxPausePkts_Object = MibTableColumn
mellanoxQoSPortTxPausePkts = _MellanoxQoSPortTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5, 1, 3),
    _MellanoxQoSPortTxPausePkts_Type()
)
mellanoxQoSPortTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPortTxPausePkts.setStatus("current")
_MellanoxQoSPortTxPauseDuration_Type = Counter64
_MellanoxQoSPortTxPauseDuration_Object = MibTableColumn
mellanoxQoSPortTxPauseDuration = _MellanoxQoSPortTxPauseDuration_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5, 1, 4),
    _MellanoxQoSPortTxPauseDuration_Type()
)
mellanoxQoSPortTxPauseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPortTxPauseDuration.setStatus("current")
_MellanoxQoSPortTxWaitMicroseconds_Type = Counter64
_MellanoxQoSPortTxWaitMicroseconds_Object = MibTableColumn
mellanoxQoSPortTxWaitMicroseconds = _MellanoxQoSPortTxWaitMicroseconds_Object(
    (1, 3, 6, 1, 4, 1, 33049, 15, 1, 5, 1, 5),
    _MellanoxQoSPortTxWaitMicroseconds_Type()
)
mellanoxQoSPortTxWaitMicroseconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxQoSPortTxWaitMicroseconds.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-QOS-MIB",
    **{"mellanoxQoSMib": mellanoxQoSMib,
       "mellanoxQoSPrioTable": mellanoxQoSPrioTable,
       "mellanoxQoSPrioEntry": mellanoxQoSPrioEntry,
       "mellanoxQoSPrioIfIndex": mellanoxQoSPrioIfIndex,
       "mellanoxQoSPrioIndex": mellanoxQoSPrioIndex,
       "mellanoxQoSPrioRxPkts": mellanoxQoSPrioRxPkts,
       "mellanoxQoSPrioRxUcastPkts": mellanoxQoSPrioRxUcastPkts,
       "mellanoxQoSPrioRxMcastPkts": mellanoxQoSPrioRxMcastPkts,
       "mellanoxQoSPrioRxBcastPkts": mellanoxQoSPrioRxBcastPkts,
       "mellanoxQoSPrioRxBytes": mellanoxQoSPrioRxBytes,
       "mellanoxQoSPrioRxPausePkts": mellanoxQoSPrioRxPausePkts,
       "mellanoxQoSPrioRxPauseDuration": mellanoxQoSPrioRxPauseDuration,
       "mellanoxQoSPrioTxPkts": mellanoxQoSPrioTxPkts,
       "mellanoxQoSPrioTxUcastPkts": mellanoxQoSPrioTxUcastPkts,
       "mellanoxQoSPrioTxMcastPkts": mellanoxQoSPrioTxMcastPkts,
       "mellanoxQoSPrioTxBcastPkts": mellanoxQoSPrioTxBcastPkts,
       "mellanoxQoSPrioTxBytes": mellanoxQoSPrioTxBytes,
       "mellanoxQoSPrioTxPausePkts": mellanoxQoSPrioTxPausePkts,
       "mellanoxQoSPFCTable": mellanoxQoSPFCTable,
       "mellanoxQoSPFCEntry": mellanoxQoSPFCEntry,
       "mellanoxQoSPFCIfIndex": mellanoxQoSPFCIfIndex,
       "mellanoxQoSPFCIndex": mellanoxQoSPFCIndex,
       "mellanoxQoSPFCRxPausePkts": mellanoxQoSPFCRxPausePkts,
       "mellanoxQoSPFCRxPauseDuration": mellanoxQoSPFCRxPauseDuration,
       "mellanoxQoSPFCTxPausePkts": mellanoxQoSPFCTxPausePkts,
       "mellanoxQoSPFCTxPauseDuration": mellanoxQoSPFCTxPauseDuration,
       "mellanoxQoSPGTable": mellanoxQoSPGTable,
       "mellanoxQoSPGEntry": mellanoxQoSPGEntry,
       "mellanoxQoSPGIfIndex": mellanoxQoSPGIfIndex,
       "mellanoxQoSPGIndex": mellanoxQoSPGIndex,
       "mellanoxQoSPGPkts": mellanoxQoSPGPkts,
       "mellanoxQoSPGBytes": mellanoxQoSPGBytes,
       "mellanoxQoSPGQueueDepth": mellanoxQoSPGQueueDepth,
       "mellanoxQoSPGNoBufferDiscard": mellanoxQoSPGNoBufferDiscard,
       "mellanoxQoSPGSharedBufferDiscard": mellanoxQoSPGSharedBufferDiscard,
       "mellanoxQoSTCTable": mellanoxQoSTCTable,
       "mellanoxQoSTCEntry": mellanoxQoSTCEntry,
       "mellanoxQoSTCIfIndex": mellanoxQoSTCIfIndex,
       "mellanoxQoSTCIndex": mellanoxQoSTCIndex,
       "mellanoxQoSTCPkts": mellanoxQoSTCPkts,
       "mellanoxQoSTCBytes": mellanoxQoSTCBytes,
       "mellanoxQoSTCSXQueueDepth": mellanoxQoSTCSXQueueDepth,
       "mellanoxQoSTCUnicastQueueDepth": mellanoxQoSTCUnicastQueueDepth,
       "mellanoxQoSTCMulticastQueueDepth": mellanoxQoSTCMulticastQueueDepth,
       "mellanoxQoSTCUnicastNoBufferDiscard": mellanoxQoSTCUnicastNoBufferDiscard,
       "mellanoxQoSTCWREDDiscard": mellanoxQoSTCWREDDiscard,
       "mellanoxQoSPortTable": mellanoxQoSPortTable,
       "mellanoxQoSPortEntry": mellanoxQoSPortEntry,
       "mellanoxQoSPortIfIndex": mellanoxQoSPortIfIndex,
       "mellanoxQoSPortRxPausePkts": mellanoxQoSPortRxPausePkts,
       "mellanoxQoSPortTxPausePkts": mellanoxQoSPortTxPausePkts,
       "mellanoxQoSPortTxPauseDuration": mellanoxQoSPortTxPauseDuration,
       "mellanoxQoSPortTxWaitMicroseconds": mellanoxQoSPortTxWaitMicroseconds}
)
