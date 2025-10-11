# SNMP MIB module (BROCADE-STACK-ISSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/brocade/BROCADE-STACK-ISSU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:02:33 2025
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

(DisplayString,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

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

brcdStackISSUMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41)
)
if mibBuilder.loadTexts:
    brcdStackISSUMIB.setRevisions(
        ("2016-03-15 00:00",
         "2017-08-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdStackISSUGlobalObjects_ObjectIdentity = ObjectIdentity
brcdStackISSUGlobalObjects = _BrcdStackISSUGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 1)
)


class _BrcdStackISSUGlobalUpgradeOption_Type(Integer32):
    """Custom type brcdStackISSUGlobalUpgradeOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("primary", 1),
          ("secondary", 2),
          ("primaryOnErrorReloadPrimary", 3),
          ("primaryOnErrorReloadSecondary", 4),
          ("secondaryOnErrorReloadPrimary", 5),
          ("secondaryOnErrorReloadSecondary", 6),
          ("abort", 7))
    )


_BrcdStackISSUGlobalUpgradeOption_Type.__name__ = "Integer32"
_BrcdStackISSUGlobalUpgradeOption_Object = MibScalar
brcdStackISSUGlobalUpgradeOption = _BrcdStackISSUGlobalUpgradeOption_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 1, 1),
    _BrcdStackISSUGlobalUpgradeOption_Type()
)
brcdStackISSUGlobalUpgradeOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcdStackISSUGlobalUpgradeOption.setStatus("current")


class _BrcdStackISSUGlobalUpgradeStatus_Type(Integer32):
    """Custom type brcdStackISSUGlobalUpgradeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("notUpgrading", 0),
          ("unitToBeUpgraded", 1),
          ("unitJoin", 2),
          ("unitVersionSync", 3),
          ("unitReady", 4),
          ("peUnitJoin", 5),
          ("peUnitVersionSync", 6),
          ("peUnitReady", 7),
          ("standbyAssignment", 8),
          ("standbySyncCompleted", 9),
          ("stackSwitchover", 10),
          ("stackSwitchoverCompleted", 11),
          ("upgradeAbort", 12),
          ("waitingForReload", 13))
    )


_BrcdStackISSUGlobalUpgradeStatus_Type.__name__ = "Integer32"
_BrcdStackISSUGlobalUpgradeStatus_Object = MibScalar
brcdStackISSUGlobalUpgradeStatus = _BrcdStackISSUGlobalUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 1, 2),
    _BrcdStackISSUGlobalUpgradeStatus_Type()
)
brcdStackISSUGlobalUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUGlobalUpgradeStatus.setStatus("current")


class _BrcdStackISSUGlobalUpgradeSystemReady_Type(Integer32):
    """Custom type brcdStackISSUGlobalUpgradeSystemReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notReadyUpgrade", 0),
          ("ready", 1))
    )


_BrcdStackISSUGlobalUpgradeSystemReady_Type.__name__ = "Integer32"
_BrcdStackISSUGlobalUpgradeSystemReady_Object = MibScalar
brcdStackISSUGlobalUpgradeSystemReady = _BrcdStackISSUGlobalUpgradeSystemReady_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 1, 3),
    _BrcdStackISSUGlobalUpgradeSystemReady_Type()
)
brcdStackISSUGlobalUpgradeSystemReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUGlobalUpgradeSystemReady.setStatus("current")
_BrcdStackISSUGlobalUpgradeError_Type = DisplayString
_BrcdStackISSUGlobalUpgradeError_Object = MibScalar
brcdStackISSUGlobalUpgradeError = _BrcdStackISSUGlobalUpgradeError_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 1, 4),
    _BrcdStackISSUGlobalUpgradeError_Type()
)
brcdStackISSUGlobalUpgradeError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUGlobalUpgradeError.setStatus("current")
_BrcdStackISSUTableObjects_ObjectIdentity = ObjectIdentity
brcdStackISSUTableObjects = _BrcdStackISSUTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2)
)
_BrcdStackISSUStatusUnitTable_Object = MibTable
brcdStackISSUStatusUnitTable = _BrcdStackISSUStatusUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1)
)
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitTable.setStatus("current")
_BrcdStackISSUStatusUnitEntry_Object = MibTableRow
brcdStackISSUStatusUnitEntry = _BrcdStackISSUStatusUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1, 1)
)
brcdStackISSUStatusUnitEntry.setIndexNames(
    (0, "BROCADE-STACK-ISSU-MIB", "brcdStackISSUStatusUnitIndex"),
)
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitEntry.setStatus("current")
_BrcdStackISSUStatusUnitIndex_Type = Integer32
_BrcdStackISSUStatusUnitIndex_Object = MibTableColumn
brcdStackISSUStatusUnitIndex = _BrcdStackISSUStatusUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1, 1, 1),
    _BrcdStackISSUStatusUnitIndex_Type()
)
brcdStackISSUStatusUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitIndex.setStatus("current")
_BrcdStackISSUStatusUnitSequence_Type = Integer32
_BrcdStackISSUStatusUnitSequence_Object = MibTableColumn
brcdStackISSUStatusUnitSequence = _BrcdStackISSUStatusUnitSequence_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1, 1, 2),
    _BrcdStackISSUStatusUnitSequence_Type()
)
brcdStackISSUStatusUnitSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitSequence.setStatus("current")
_BrcdStackISSUStatusUnitType_Type = DisplayString
_BrcdStackISSUStatusUnitType_Object = MibTableColumn
brcdStackISSUStatusUnitType = _BrcdStackISSUStatusUnitType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1, 1, 3),
    _BrcdStackISSUStatusUnitType_Type()
)
brcdStackISSUStatusUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitType.setStatus("current")


class _BrcdStackISSUStatusUnitRole_Type(Integer32):
    """Custom type brcdStackISSUStatusUnitRole based on Integer32"""
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
        *(("other", 1),
          ("active", 2),
          ("standby", 3),
          ("member", 4),
          ("standalone", 5),
          ("spxPe", 6))
    )


_BrcdStackISSUStatusUnitRole_Type.__name__ = "Integer32"
_BrcdStackISSUStatusUnitRole_Object = MibTableColumn
brcdStackISSUStatusUnitRole = _BrcdStackISSUStatusUnitRole_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1, 1, 4),
    _BrcdStackISSUStatusUnitRole_Type()
)
brcdStackISSUStatusUnitRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitRole.setStatus("current")


class _BrcdStackISSUStatusUnitStatus_Type(Integer32):
    """Custom type brcdStackISSUStatusUnitStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("notUpgraded", 0),
          ("upgrading", 1),
          ("joined", 2),
          ("versionSyncStart", 3),
          ("versionSyncComplete", 4),
          ("upgradeComplete", 5),
          ("upgradeAbort", 6),
          ("upgradePending", 7))
    )


_BrcdStackISSUStatusUnitStatus_Type.__name__ = "Integer32"
_BrcdStackISSUStatusUnitStatus_Object = MibTableColumn
brcdStackISSUStatusUnitStatus = _BrcdStackISSUStatusUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 41, 2, 1, 1, 5),
    _BrcdStackISSUStatusUnitStatus_Type()
)
brcdStackISSUStatusUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdStackISSUStatusUnitStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-STACK-ISSU-MIB",
    **{"brcdStackISSUMIB": brcdStackISSUMIB,
       "brcdStackISSUGlobalObjects": brcdStackISSUGlobalObjects,
       "brcdStackISSUGlobalUpgradeOption": brcdStackISSUGlobalUpgradeOption,
       "brcdStackISSUGlobalUpgradeStatus": brcdStackISSUGlobalUpgradeStatus,
       "brcdStackISSUGlobalUpgradeSystemReady": brcdStackISSUGlobalUpgradeSystemReady,
       "brcdStackISSUGlobalUpgradeError": brcdStackISSUGlobalUpgradeError,
       "brcdStackISSUTableObjects": brcdStackISSUTableObjects,
       "brcdStackISSUStatusUnitTable": brcdStackISSUStatusUnitTable,
       "brcdStackISSUStatusUnitEntry": brcdStackISSUStatusUnitEntry,
       "brcdStackISSUStatusUnitIndex": brcdStackISSUStatusUnitIndex,
       "brcdStackISSUStatusUnitSequence": brcdStackISSUStatusUnitSequence,
       "brcdStackISSUStatusUnitType": brcdStackISSUStatusUnitType,
       "brcdStackISSUStatusUnitRole": brcdStackISSUStatusUnitRole,
       "brcdStackISSUStatusUnitStatus": brcdStackISSUStatusUnitStatus}
)
