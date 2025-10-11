# SNMP MIB module (SUPERMICRO-WSS-RRM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-WSS-RRM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:01:53 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsRrm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84)
)
if mibBuilder.loadTexts:
    fsRrm.setRevisions(
        ("2013-02-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsRrmManagment_ObjectIdentity = ObjectIdentity
fsRrmManagment = _FsRrmManagment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1)
)
_FsRrmConfigTable_Object = MibTable
fsRrmConfigTable = _FsRrmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1)
)
if mibBuilder.loadTexts:
    fsRrmConfigTable.setStatus("current")
_FsRrmConfigEntry_Object = MibTableRow
fsRrmConfigEntry = _FsRrmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1)
)
fsRrmConfigEntry.setIndexNames(
    (0, "SUPERMICRO-WSS-RRM-MIB", "fsRrmRadioType"),
)
if mibBuilder.loadTexts:
    fsRrmConfigEntry.setStatus("current")


class _FsRrmRadioType_Type(Integer32):
    """Custom type fsRrmRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2))
    )


_FsRrmRadioType_Type.__name__ = "Integer32"
_FsRrmRadioType_Object = MibTableColumn
fsRrmRadioType = _FsRrmRadioType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1, 1),
    _FsRrmRadioType_Type()
)
fsRrmRadioType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsRrmRadioType.setStatus("current")


class _FsRrmDcaMode_Type(Integer32):
    """Custom type fsRrmDcaMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("perAP", 2),
          ("disable", 3))
    )


_FsRrmDcaMode_Type.__name__ = "Integer32"
_FsRrmDcaMode_Object = MibTableColumn
fsRrmDcaMode = _FsRrmDcaMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1, 2),
    _FsRrmDcaMode_Type()
)
fsRrmDcaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDcaMode.setStatus("current")


class _FsRrmDcaChannelSelectionMode_Type(Integer32):
    """Custom type fsRrmDcaChannelSelectionMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("once", 2),
          ("off", 3))
    )


_FsRrmDcaChannelSelectionMode_Type.__name__ = "Integer32"
_FsRrmDcaChannelSelectionMode_Object = MibTableColumn
fsRrmDcaChannelSelectionMode = _FsRrmDcaChannelSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1, 3),
    _FsRrmDcaChannelSelectionMode_Type()
)
fsRrmDcaChannelSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmDcaChannelSelectionMode.setStatus("current")


class _FsRrmTpcMode_Type(Integer32):
    """Custom type fsRrmTpcMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("perAP", 2),
          ("disable", 3))
    )


_FsRrmTpcMode_Type.__name__ = "Integer32"
_FsRrmTpcMode_Object = MibTableColumn
fsRrmTpcMode = _FsRrmTpcMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1, 4),
    _FsRrmTpcMode_Type()
)
fsRrmTpcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmTpcMode.setStatus("current")


class _FsRrmTpcSelectionMode_Type(Integer32):
    """Custom type fsRrmTpcSelectionMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("once", 2),
          ("off", 3))
    )


_FsRrmTpcSelectionMode_Type.__name__ = "Integer32"
_FsRrmTpcSelectionMode_Object = MibTableColumn
fsRrmTpcSelectionMode = _FsRrmTpcSelectionMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1, 5),
    _FsRrmTpcSelectionMode_Type()
)
fsRrmTpcSelectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRrmTpcSelectionMode.setStatus("current")
_FsRrmRowStatus_Type = RowStatus
_FsRrmRowStatus_Object = MibTableColumn
fsRrmRowStatus = _FsRrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 84, 1, 1, 1, 6),
    _FsRrmRowStatus_Type()
)
fsRrmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRrmRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-WSS-RRM-MIB",
    **{"fsRrm": fsRrm,
       "fsRrmManagment": fsRrmManagment,
       "fsRrmConfigTable": fsRrmConfigTable,
       "fsRrmConfigEntry": fsRrmConfigEntry,
       "fsRrmRadioType": fsRrmRadioType,
       "fsRrmDcaMode": fsRrmDcaMode,
       "fsRrmDcaChannelSelectionMode": fsRrmDcaChannelSelectionMode,
       "fsRrmTpcMode": fsRrmTpcMode,
       "fsRrmTpcSelectionMode": fsRrmTpcSelectionMode,
       "fsRrmRowStatus": fsRrmRowStatus}
)
