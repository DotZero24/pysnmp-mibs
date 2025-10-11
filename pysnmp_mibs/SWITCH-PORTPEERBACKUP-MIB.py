# SNMP MIB module (SWITCH-PORTPEERBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-PORTPEERBACKUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:51 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(Vlanset,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "Vlanset")


# MODULE-IDENTITY

rcPortPeerBackup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcPortPeerBackupObjects_ObjectIdentity = ObjectIdentity
rcPortPeerBackupObjects = _RcPortPeerBackupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1)
)
_RcPortPeerBackupCfgTable_Object = MibTable
rcPortPeerBackupCfgTable = _RcPortPeerBackupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1)
)
if mibBuilder.loadTexts:
    rcPortPeerBackupCfgTable.setStatus("current")
_RcPortPeerBackupCfgEntry_Object = MibTableRow
rcPortPeerBackupCfgEntry = _RcPortPeerBackupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1)
)
rcPortPeerBackupCfgEntry.setIndexNames(
    (0, "SWITCH-PORTPEERBACKUP-MIB", "rcPortPeerBackupPortIndex"),
)
if mibBuilder.loadTexts:
    rcPortPeerBackupCfgEntry.setStatus("current")
_RcPortPeerBackupPortIndex_Type = Integer32
_RcPortPeerBackupPortIndex_Object = MibTableColumn
rcPortPeerBackupPortIndex = _RcPortPeerBackupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 1),
    _RcPortPeerBackupPortIndex_Type()
)
rcPortPeerBackupPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupPortIndex.setStatus("current")
_RcPortPeerBackupVlanlist_Type = Vlanset
_RcPortPeerBackupVlanlist_Object = MibTableColumn
rcPortPeerBackupVlanlist = _RcPortPeerBackupVlanlist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 2),
    _RcPortPeerBackupVlanlist_Type()
)
rcPortPeerBackupVlanlist.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupVlanlist.setStatus("current")


class _RcPortPeerBackupMdName_Type(OctetString):
    """Custom type rcPortPeerBackupMdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RcPortPeerBackupMdName_Type.__name__ = "OctetString"
_RcPortPeerBackupMdName_Object = MibTableColumn
rcPortPeerBackupMdName = _RcPortPeerBackupMdName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 3),
    _RcPortPeerBackupMdName_Type()
)
rcPortPeerBackupMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupMdName.setStatus("current")


class _RcPortPeerBackupMdLevel_Type(Integer32):
    """Custom type rcPortPeerBackupMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcPortPeerBackupMdLevel_Type.__name__ = "Integer32"
_RcPortPeerBackupMdLevel_Object = MibTableColumn
rcPortPeerBackupMdLevel = _RcPortPeerBackupMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 4),
    _RcPortPeerBackupMdLevel_Type()
)
rcPortPeerBackupMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupMdLevel.setStatus("current")


class _RcPortPeerBackupMaName_Type(OctetString):
    """Custom type rcPortPeerBackupMaName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 13),
    )


_RcPortPeerBackupMaName_Type.__name__ = "OctetString"
_RcPortPeerBackupMaName_Object = MibTableColumn
rcPortPeerBackupMaName = _RcPortPeerBackupMaName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 5),
    _RcPortPeerBackupMaName_Type()
)
rcPortPeerBackupMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupMaName.setStatus("current")


class _RcPortPeerBackupRemoteMep_Type(Integer32):
    """Custom type rcPortPeerBackupRemoteMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_RcPortPeerBackupRemoteMep_Type.__name__ = "Integer32"
_RcPortPeerBackupRemoteMep_Object = MibTableColumn
rcPortPeerBackupRemoteMep = _RcPortPeerBackupRemoteMep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 6),
    _RcPortPeerBackupRemoteMep_Type()
)
rcPortPeerBackupRemoteMep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupRemoteMep.setStatus("current")
_RcPortPeerBackupRowStatus_Type = RowStatus
_RcPortPeerBackupRowStatus_Object = MibTableColumn
rcPortPeerBackupRowStatus = _RcPortPeerBackupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 1, 1, 7),
    _RcPortPeerBackupRowStatus_Type()
)
rcPortPeerBackupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcPortPeerBackupRowStatus.setStatus("current")
_RcPortPeerBackupStatusTable_Object = MibTable
rcPortPeerBackupStatusTable = _RcPortPeerBackupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 2)
)
if mibBuilder.loadTexts:
    rcPortPeerBackupStatusTable.setStatus("current")
_RcPortPeerBackupStatusEntry_Object = MibTableRow
rcPortPeerBackupStatusEntry = _RcPortPeerBackupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 2, 1)
)
rcPortPeerBackupStatusEntry.setIndexNames(
    (0, "SWITCH-PORTPEERBACKUP-MIB", "rcPortPeerBackupPortIndex"),
)
if mibBuilder.loadTexts:
    rcPortPeerBackupStatusEntry.setStatus("current")


class _RcPortPeerBackupLocalPortStatus_Type(Integer32):
    """Custom type rcPortPeerBackupLocalPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2))
    )


_RcPortPeerBackupLocalPortStatus_Type.__name__ = "Integer32"
_RcPortPeerBackupLocalPortStatus_Object = MibTableColumn
rcPortPeerBackupLocalPortStatus = _RcPortPeerBackupLocalPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 2, 1, 1),
    _RcPortPeerBackupLocalPortStatus_Type()
)
rcPortPeerBackupLocalPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortPeerBackupLocalPortStatus.setStatus("current")


class _RcPortPeerBackupRemotePortStatus_Type(Integer32):
    """Custom type rcPortPeerBackupRemotePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2),
          ("unknown", 3))
    )


_RcPortPeerBackupRemotePortStatus_Type.__name__ = "Integer32"
_RcPortPeerBackupRemotePortStatus_Object = MibTableColumn
rcPortPeerBackupRemotePortStatus = _RcPortPeerBackupRemotePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 2, 1, 2),
    _RcPortPeerBackupRemotePortStatus_Type()
)
rcPortPeerBackupRemotePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortPeerBackupRemotePortStatus.setStatus("current")
_RcPortPeerBackupStatusDuration_Type = Integer32
_RcPortPeerBackupStatusDuration_Object = MibTableColumn
rcPortPeerBackupStatusDuration = _RcPortPeerBackupStatusDuration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 2, 1, 3),
    _RcPortPeerBackupStatusDuration_Type()
)
rcPortPeerBackupStatusDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortPeerBackupStatusDuration.setStatus("current")
_RcPortPeerBackupSwitchCnt_Type = Integer32
_RcPortPeerBackupSwitchCnt_Object = MibTableColumn
rcPortPeerBackupSwitchCnt = _RcPortPeerBackupSwitchCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 1, 2, 1, 4),
    _RcPortPeerBackupSwitchCnt_Type()
)
rcPortPeerBackupSwitchCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcPortPeerBackupSwitchCnt.setStatus("current")
_RcPortPeerBackupNotifications_ObjectIdentity = ObjectIdentity
rcPortPeerBackupNotifications = _RcPortPeerBackupNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 2)
)

# Managed Objects groups


# Notification objects

rcPortPeerBackupLocalPortForward = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 2, 1)
)
rcPortPeerBackupLocalPortForward.setObjects(
    ("SWITCH-PORTPEERBACKUP-MIB", "rcPortPeerBackupLocalPortStatus")
)
if mibBuilder.loadTexts:
    rcPortPeerBackupLocalPortForward.setStatus(
        "current"
    )

rcPortPeerBackupLocalPortBlock = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 80, 2, 2)
)
rcPortPeerBackupLocalPortBlock.setObjects(
    ("SWITCH-PORTPEERBACKUP-MIB", "rcPortPeerBackupLocalPortStatus")
)
if mibBuilder.loadTexts:
    rcPortPeerBackupLocalPortBlock.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-PORTPEERBACKUP-MIB",
    **{"rcPortPeerBackup": rcPortPeerBackup,
       "rcPortPeerBackupObjects": rcPortPeerBackupObjects,
       "rcPortPeerBackupCfgTable": rcPortPeerBackupCfgTable,
       "rcPortPeerBackupCfgEntry": rcPortPeerBackupCfgEntry,
       "rcPortPeerBackupPortIndex": rcPortPeerBackupPortIndex,
       "rcPortPeerBackupVlanlist": rcPortPeerBackupVlanlist,
       "rcPortPeerBackupMdName": rcPortPeerBackupMdName,
       "rcPortPeerBackupMdLevel": rcPortPeerBackupMdLevel,
       "rcPortPeerBackupMaName": rcPortPeerBackupMaName,
       "rcPortPeerBackupRemoteMep": rcPortPeerBackupRemoteMep,
       "rcPortPeerBackupRowStatus": rcPortPeerBackupRowStatus,
       "rcPortPeerBackupStatusTable": rcPortPeerBackupStatusTable,
       "rcPortPeerBackupStatusEntry": rcPortPeerBackupStatusEntry,
       "rcPortPeerBackupLocalPortStatus": rcPortPeerBackupLocalPortStatus,
       "rcPortPeerBackupRemotePortStatus": rcPortPeerBackupRemotePortStatus,
       "rcPortPeerBackupStatusDuration": rcPortPeerBackupStatusDuration,
       "rcPortPeerBackupSwitchCnt": rcPortPeerBackupSwitchCnt,
       "rcPortPeerBackupNotifications": rcPortPeerBackupNotifications,
       "rcPortPeerBackupLocalPortForward": rcPortPeerBackupLocalPortForward,
       "rcPortPeerBackupLocalPortBlock": rcPortPeerBackupLocalPortBlock}
)
