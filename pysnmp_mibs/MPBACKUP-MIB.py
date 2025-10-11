# SNMP MIB module (MPBACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPBACKUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:02 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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


# MODULE-IDENTITY

mpBackupMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpBackupConf_ObjectIdentity = ObjectIdentity
mpBackupConf = _MpBackupConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1)
)
_MpBackupConfTable_Object = MibTable
mpBackupConfTable = _MpBackupConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1)
)
if mibBuilder.loadTexts:
    mpBackupConfTable.setStatus("current")
_MpBackupConfEntry_Object = MibTableRow
mpBackupConfEntry = _MpBackupConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1)
)
mpBackupConfEntry.setIndexNames(
    (0, "MPBACKUP-MIB", "backupIfIndex"),
)
if mibBuilder.loadTexts:
    mpBackupConfEntry.setStatus("current")
_BackupIfIndex_Type = Integer32
_BackupIfIndex_Object = MibTableColumn
backupIfIndex = _BackupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 1),
    _BackupIfIndex_Type()
)
backupIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupIfIndex.setStatus("current")
_BackupIfName_Type = OctetString
_BackupIfName_Object = MibTableColumn
backupIfName = _BackupIfName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 2),
    _BackupIfName_Type()
)
backupIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupIfName.setStatus("current")


class _BackupFlag_Type(OctetString):
    """Custom type backupFlag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_BackupFlag_Type.__name__ = "OctetString"
_BackupFlag_Object = MibTableColumn
backupFlag = _BackupFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 3),
    _BackupFlag_Type()
)
backupFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupFlag.setStatus("current")
_BackupDelayAct_Type = Unsigned32
_BackupDelayAct_Object = MibTableColumn
backupDelayAct = _BackupDelayAct_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 4),
    _BackupDelayAct_Type()
)
backupDelayAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupDelayAct.setStatus("current")
_BackupDelayDeact_Type = Unsigned32
_BackupDelayDeact_Object = MibTableColumn
backupDelayDeact = _BackupDelayDeact_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 5),
    _BackupDelayDeact_Type()
)
backupDelayDeact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupDelayDeact.setStatus("current")


class _BackupLoadAct_Type(Integer32):
    """Custom type backupLoadAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BackupLoadAct_Type.__name__ = "Integer32"
_BackupLoadAct_Object = MibTableColumn
backupLoadAct = _BackupLoadAct_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 6),
    _BackupLoadAct_Type()
)
backupLoadAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupLoadAct.setStatus("current")


class _BackupLoadDeact_Type(Integer32):
    """Custom type backupLoadDeact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BackupLoadDeact_Type.__name__ = "Integer32"
_BackupLoadDeact_Object = MibTableColumn
backupLoadDeact = _BackupLoadDeact_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 7),
    _BackupLoadDeact_Type()
)
backupLoadDeact.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupLoadDeact.setStatus("current")
_BackupRowStatus_Type = RowStatus
_BackupRowStatus_Object = MibTableColumn
backupRowStatus = _BackupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 29, 1, 1, 1, 8),
    _BackupRowStatus_Type()
)
backupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    backupRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPBACKUP-MIB",
    **{"mpBackupMib": mpBackupMib,
       "mpBackupConf": mpBackupConf,
       "mpBackupConfTable": mpBackupConfTable,
       "mpBackupConfEntry": mpBackupConfEntry,
       "backupIfIndex": backupIfIndex,
       "backupIfName": backupIfName,
       "backupFlag": backupFlag,
       "backupDelayAct": backupDelayAct,
       "backupDelayDeact": backupDelayDeact,
       "backupLoadAct": backupLoadAct,
       "backupLoadDeact": backupLoadDeact,
       "backupRowStatus": backupRowStatus}
)
