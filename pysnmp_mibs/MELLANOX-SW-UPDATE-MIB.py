# SNMP MIB module (MELLANOX-SW-UPDATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mellanox/MELLANOX-SW-UPDATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:38 2025
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

(mellanoxSWUpdate,) = mibBuilder.importSymbols(
    "MELLANOX-SMI-MIB",
    "mellanoxSWUpdate")

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

mellanoxSWUpdateMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1)
)
if mibBuilder.loadTexts:
    mellanoxSWUpdateMib.setRevisions(
        ("2017-07-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MellanoxSWUpdateMibObjects_ObjectIdentity = ObjectIdentity
mellanoxSWUpdateMibObjects = _MellanoxSWUpdateMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1)
)
_MellanoxSWTable_Object = MibTable
mellanoxSWTable = _MellanoxSWTable_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mellanoxSWTable.setStatus("current")
_MellanoxSWEntry_Object = MibTableRow
mellanoxSWEntry = _MellanoxSWEntry_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 1, 1)
)
mellanoxSWEntry.setIndexNames(
    (0, "MELLANOX-SW-UPDATE-MIB", "mellanoxSWPartitionIndex"),
)
if mibBuilder.loadTexts:
    mellanoxSWEntry.setStatus("current")
_MellanoxSWPartitionIndex_Type = Integer32
_MellanoxSWPartitionIndex_Object = MibTableColumn
mellanoxSWPartitionIndex = _MellanoxSWPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 1, 1, 1),
    _MellanoxSWPartitionIndex_Type()
)
mellanoxSWPartitionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWPartitionIndex.setStatus("current")
_MellanoxSWPartitionName_Type = OctetString
_MellanoxSWPartitionName_Object = MibTableColumn
mellanoxSWPartitionName = _MellanoxSWPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 1, 1, 2),
    _MellanoxSWPartitionName_Type()
)
mellanoxSWPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWPartitionName.setStatus("current")
_MellanoxSWPartitionActive_Type = Integer32
_MellanoxSWPartitionActive_Object = MibTableColumn
mellanoxSWPartitionActive = _MellanoxSWPartitionActive_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 1, 1, 3),
    _MellanoxSWPartitionActive_Type()
)
mellanoxSWPartitionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWPartitionActive.setStatus("current")
_MellanoxSWPartitionBootNext_Type = Integer32
_MellanoxSWPartitionBootNext_Object = MibTableColumn
mellanoxSWPartitionBootNext = _MellanoxSWPartitionBootNext_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 1, 1, 4),
    _MellanoxSWPartitionBootNext_Type()
)
mellanoxSWPartitionBootNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWPartitionBootNext.setStatus("current")
_MellanoxSWUpdateCmd_ObjectIdentity = ObjectIdentity
mellanoxSWUpdateCmd = _MellanoxSWUpdateCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 2)
)
_MellanoxSWUpdateCmdSetNext_Type = Integer32
_MellanoxSWUpdateCmdSetNext_Object = MibScalar
mellanoxSWUpdateCmdSetNext = _MellanoxSWUpdateCmdSetNext_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 2, 1),
    _MellanoxSWUpdateCmdSetNext_Type()
)
mellanoxSWUpdateCmdSetNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxSWUpdateCmdSetNext.setStatus("current")
_MellanoxSWUpdateCmdUri_Type = OctetString
_MellanoxSWUpdateCmdUri_Object = MibScalar
mellanoxSWUpdateCmdUri = _MellanoxSWUpdateCmdUri_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 2, 2),
    _MellanoxSWUpdateCmdUri_Type()
)
mellanoxSWUpdateCmdUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxSWUpdateCmdUri.setStatus("current")


class _MellanoxSWUpdateCmdExecute_Type(Integer32):
    """Custom type mellanoxSWUpdateCmdExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mellanoxSWUpdateCmdExecuteUpdate", 1),
          ("mellanoxSWUpdateCmdExecuteSetNext", 2))
    )


_MellanoxSWUpdateCmdExecute_Type.__name__ = "Integer32"
_MellanoxSWUpdateCmdExecute_Object = MibScalar
mellanoxSWUpdateCmdExecute = _MellanoxSWUpdateCmdExecute_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 2, 3),
    _MellanoxSWUpdateCmdExecute_Type()
)
mellanoxSWUpdateCmdExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mellanoxSWUpdateCmdExecute.setStatus("current")
_MellanoxSWUpdateCmdStatus_Type = Integer32
_MellanoxSWUpdateCmdStatus_Object = MibScalar
mellanoxSWUpdateCmdStatus = _MellanoxSWUpdateCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 2, 4),
    _MellanoxSWUpdateCmdStatus_Type()
)
mellanoxSWUpdateCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWUpdateCmdStatus.setStatus("current")
_MellanoxSWUpdateCmdStatusString_Type = OctetString
_MellanoxSWUpdateCmdStatusString_Object = MibScalar
mellanoxSWUpdateCmdStatusString = _MellanoxSWUpdateCmdStatusString_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 2, 5),
    _MellanoxSWUpdateCmdStatusString_Type()
)
mellanoxSWUpdateCmdStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWUpdateCmdStatusString.setStatus("current")
_MellanoxSWActivePartition_Type = Integer32
_MellanoxSWActivePartition_Object = MibScalar
mellanoxSWActivePartition = _MellanoxSWActivePartition_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 3),
    _MellanoxSWActivePartition_Type()
)
mellanoxSWActivePartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWActivePartition.setStatus("current")
_MellanoxSWNextBootPartition_Type = Integer32
_MellanoxSWNextBootPartition_Object = MibScalar
mellanoxSWNextBootPartition = _MellanoxSWNextBootPartition_Object(
    (1, 3, 6, 1, 4, 1, 33049, 11, 1, 1, 4),
    _MellanoxSWNextBootPartition_Type()
)
mellanoxSWNextBootPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mellanoxSWNextBootPartition.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MELLANOX-SW-UPDATE-MIB",
    **{"mellanoxSWUpdateMib": mellanoxSWUpdateMib,
       "mellanoxSWUpdateMibObjects": mellanoxSWUpdateMibObjects,
       "mellanoxSWTable": mellanoxSWTable,
       "mellanoxSWEntry": mellanoxSWEntry,
       "mellanoxSWPartitionIndex": mellanoxSWPartitionIndex,
       "mellanoxSWPartitionName": mellanoxSWPartitionName,
       "mellanoxSWPartitionActive": mellanoxSWPartitionActive,
       "mellanoxSWPartitionBootNext": mellanoxSWPartitionBootNext,
       "mellanoxSWUpdateCmd": mellanoxSWUpdateCmd,
       "mellanoxSWUpdateCmdSetNext": mellanoxSWUpdateCmdSetNext,
       "mellanoxSWUpdateCmdUri": mellanoxSWUpdateCmdUri,
       "mellanoxSWUpdateCmdExecute": mellanoxSWUpdateCmdExecute,
       "mellanoxSWUpdateCmdStatus": mellanoxSWUpdateCmdStatus,
       "mellanoxSWUpdateCmdStatusString": mellanoxSWUpdateCmdStatusString,
       "mellanoxSWActivePartition": mellanoxSWActivePartition,
       "mellanoxSWNextBootPartition": mellanoxSWNextBootPartition}
)
