# SNMP MIB module (QTECH-SECZONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SECZONE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:12 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechSecZoneMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54)
)
if mibBuilder.loadTexts:
    qtechSecZoneMIB.setRevisions(
        ("2009-08-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSecZoneMIBObjects_ObjectIdentity = ObjectIdentity
qtechSecZoneMIBObjects = _QtechSecZoneMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1)
)
_QtechSecZoneChainTable_Object = MibTable
qtechSecZoneChainTable = _QtechSecZoneChainTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1)
)
if mibBuilder.loadTexts:
    qtechSecZoneChainTable.setStatus("current")
_QtechSecZoneChainEntry_Object = MibTableRow
qtechSecZoneChainEntry = _QtechSecZoneChainEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1)
)
qtechSecZoneChainEntry.setIndexNames(
    (0, "QTECH-SECZONE-MIB", "qtechSecZoneChainName"),
)
if mibBuilder.loadTexts:
    qtechSecZoneChainEntry.setStatus("current")


class _QtechSecZoneChainName_Type(DisplayString):
    """Custom type qtechSecZoneChainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSecZoneChainName_Type.__name__ = "DisplayString"
_QtechSecZoneChainName_Object = MibTableColumn
qtechSecZoneChainName = _QtechSecZoneChainName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 1),
    _QtechSecZoneChainName_Type()
)
qtechSecZoneChainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSecZoneChainName.setStatus("current")


class _QtechSecZoneLevel_Type(Integer32):
    """Custom type qtechSecZoneLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechSecZoneLevel_Type.__name__ = "Integer32"
_QtechSecZoneLevel_Object = MibTableColumn
qtechSecZoneLevel = _QtechSecZoneLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 2),
    _QtechSecZoneLevel_Type()
)
qtechSecZoneLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneLevel.setStatus("current")


class _QtechSecZoneAclName_Type(DisplayString):
    """Custom type qtechSecZoneAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSecZoneAclName_Type.__name__ = "DisplayString"
_QtechSecZoneAclName_Object = MibTableColumn
qtechSecZoneAclName = _QtechSecZoneAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 3),
    _QtechSecZoneAclName_Type()
)
qtechSecZoneAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneAclName.setStatus("current")


class _QtechSecZoneViolationNotifyThresh_Type(Integer32):
    """Custom type qtechSecZoneViolationNotifyThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechSecZoneViolationNotifyThresh_Type.__name__ = "Integer32"
_QtechSecZoneViolationNotifyThresh_Object = MibTableColumn
qtechSecZoneViolationNotifyThresh = _QtechSecZoneViolationNotifyThresh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 4),
    _QtechSecZoneViolationNotifyThresh_Type()
)
qtechSecZoneViolationNotifyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneViolationNotifyThresh.setStatus("current")


class _QtechSecZoneViolationNotifyAction_Type(Integer32):
    """Custom type qtechSecZoneViolationNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_QtechSecZoneViolationNotifyAction_Type.__name__ = "Integer32"
_QtechSecZoneViolationNotifyAction_Object = MibTableColumn
qtechSecZoneViolationNotifyAction = _QtechSecZoneViolationNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 5),
    _QtechSecZoneViolationNotifyAction_Type()
)
qtechSecZoneViolationNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneViolationNotifyAction.setStatus("current")


class _QtechSecZoneViolationBlockThresh_Type(Integer32):
    """Custom type qtechSecZoneViolationBlockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechSecZoneViolationBlockThresh_Type.__name__ = "Integer32"
_QtechSecZoneViolationBlockThresh_Object = MibTableColumn
qtechSecZoneViolationBlockThresh = _QtechSecZoneViolationBlockThresh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 6),
    _QtechSecZoneViolationBlockThresh_Type()
)
qtechSecZoneViolationBlockThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneViolationBlockThresh.setStatus("current")


class _QtechSecZoneViolationBlockAction_Type(Integer32):
    """Custom type qtechSecZoneViolationBlockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_QtechSecZoneViolationBlockAction_Type.__name__ = "Integer32"
_QtechSecZoneViolationBlockAction_Object = MibTableColumn
qtechSecZoneViolationBlockAction = _QtechSecZoneViolationBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 7),
    _QtechSecZoneViolationBlockAction_Type()
)
qtechSecZoneViolationBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneViolationBlockAction.setStatus("current")


class _QtechSecZoneViolationBlockTimeout_Type(Integer32):
    """Custom type qtechSecZoneViolationBlockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_QtechSecZoneViolationBlockTimeout_Type.__name__ = "Integer32"
_QtechSecZoneViolationBlockTimeout_Object = MibTableColumn
qtechSecZoneViolationBlockTimeout = _QtechSecZoneViolationBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 8),
    _QtechSecZoneViolationBlockTimeout_Type()
)
qtechSecZoneViolationBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneViolationBlockTimeout.setStatus("current")
_QtechSecZoneChainEntryStatus_Type = RowStatus
_QtechSecZoneChainEntryStatus_Object = MibTableColumn
qtechSecZoneChainEntryStatus = _QtechSecZoneChainEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 1, 1, 9),
    _QtechSecZoneChainEntryStatus_Type()
)
qtechSecZoneChainEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSecZoneChainEntryStatus.setStatus("current")
_QtechSecZone2ZoneTable_Object = MibTable
qtechSecZone2ZoneTable = _QtechSecZone2ZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 2)
)
if mibBuilder.loadTexts:
    qtechSecZone2ZoneTable.setStatus("current")
_QtechSecZone2ZoneEntry_Object = MibTableRow
qtechSecZone2ZoneEntry = _QtechSecZone2ZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 2, 1)
)
qtechSecZone2ZoneEntry.setIndexNames(
    (0, "QTECH-SECZONE-MIB", "qtechZoneFirstName"),
    (0, "QTECH-SECZONE-MIB", "qtechZoneSecondName"),
    (0, "QTECH-SECZONE-MIB", "qtechZone2ZoneAclName"),
)
if mibBuilder.loadTexts:
    qtechSecZone2ZoneEntry.setStatus("current")


class _QtechZoneFirstName_Type(DisplayString):
    """Custom type qtechZoneFirstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechZoneFirstName_Type.__name__ = "DisplayString"
_QtechZoneFirstName_Object = MibTableColumn
qtechZoneFirstName = _QtechZoneFirstName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 2, 1, 1),
    _QtechZoneFirstName_Type()
)
qtechZoneFirstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZoneFirstName.setStatus("current")


class _QtechZoneSecondName_Type(DisplayString):
    """Custom type qtechZoneSecondName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechZoneSecondName_Type.__name__ = "DisplayString"
_QtechZoneSecondName_Object = MibTableColumn
qtechZoneSecondName = _QtechZoneSecondName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 2, 1, 2),
    _QtechZoneSecondName_Type()
)
qtechZoneSecondName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZoneSecondName.setStatus("current")


class _QtechZone2ZoneAclName_Type(DisplayString):
    """Custom type qtechZone2ZoneAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechZone2ZoneAclName_Type.__name__ = "DisplayString"
_QtechZone2ZoneAclName_Object = MibTableColumn
qtechZone2ZoneAclName = _QtechZone2ZoneAclName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 2, 1, 3),
    _QtechZone2ZoneAclName_Type()
)
qtechZone2ZoneAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZone2ZoneAclName.setStatus("current")
_QtechZone2ZoneEntryStauts_Type = RowStatus
_QtechZone2ZoneEntryStauts_Object = MibTableColumn
qtechZone2ZoneEntryStauts = _QtechZone2ZoneEntryStauts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 2, 1, 4),
    _QtechZone2ZoneEntryStauts_Type()
)
qtechZone2ZoneEntryStauts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechZone2ZoneEntryStauts.setStatus("current")
_QtechSecZoneBlockingTable_Object = MibTable
qtechSecZoneBlockingTable = _QtechSecZoneBlockingTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 3)
)
if mibBuilder.loadTexts:
    qtechSecZoneBlockingTable.setStatus("current")
_QtechSecZoneBlockingEntry_Object = MibTableRow
qtechSecZoneBlockingEntry = _QtechSecZoneBlockingEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 3, 1)
)
qtechSecZoneBlockingEntry.setIndexNames(
    (0, "QTECH-SECZONE-MIB", "qtechBockingIP"),
)
if mibBuilder.loadTexts:
    qtechSecZoneBlockingEntry.setStatus("current")
_QtechBockingIP_Type = IpAddress
_QtechBockingIP_Object = MibTableColumn
qtechBockingIP = _QtechBockingIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 3, 1, 1),
    _QtechBockingIP_Type()
)
qtechBockingIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingIP.setStatus("current")


class _QtechBockingCurrentStatus_Type(Integer32):
    """Custom type qtechBockingCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_QtechBockingCurrentStatus_Type.__name__ = "Integer32"
_QtechBockingCurrentStatus_Object = MibTableColumn
qtechBockingCurrentStatus = _QtechBockingCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 3, 1, 2),
    _QtechBockingCurrentStatus_Type()
)
qtechBockingCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingCurrentStatus.setStatus("current")


class _QtechBockingTryAccessZoneName_Type(DisplayString):
    """Custom type qtechBockingTryAccessZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechBockingTryAccessZoneName_Type.__name__ = "DisplayString"
_QtechBockingTryAccessZoneName_Object = MibTableColumn
qtechBockingTryAccessZoneName = _QtechBockingTryAccessZoneName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 3, 1, 3),
    _QtechBockingTryAccessZoneName_Type()
)
qtechBockingTryAccessZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingTryAccessZoneName.setStatus("current")
_QtechBockingEntryStatus_Type = ConfigStatus
_QtechBockingEntryStatus_Object = MibTableColumn
qtechBockingEntryStatus = _QtechBockingEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 3, 1, 4),
    _QtechBockingEntryStatus_Type()
)
qtechBockingEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechBockingEntryStatus.setStatus("current")


class _QtechGlobalViolationNotifyThresh_Type(Integer32):
    """Custom type qtechGlobalViolationNotifyThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechGlobalViolationNotifyThresh_Type.__name__ = "Integer32"
_QtechGlobalViolationNotifyThresh_Object = MibScalar
qtechGlobalViolationNotifyThresh = _QtechGlobalViolationNotifyThresh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 4),
    _QtechGlobalViolationNotifyThresh_Type()
)
qtechGlobalViolationNotifyThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalViolationNotifyThresh.setStatus("current")


class _QtechGlobalViolationNotifyAction_Type(Integer32):
    """Custom type qtechGlobalViolationNotifyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_QtechGlobalViolationNotifyAction_Type.__name__ = "Integer32"
_QtechGlobalViolationNotifyAction_Object = MibScalar
qtechGlobalViolationNotifyAction = _QtechGlobalViolationNotifyAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 5),
    _QtechGlobalViolationNotifyAction_Type()
)
qtechGlobalViolationNotifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalViolationNotifyAction.setStatus("current")


class _QtechGlobalViolationBlockThresh_Type(Integer32):
    """Custom type qtechGlobalViolationBlockThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechGlobalViolationBlockThresh_Type.__name__ = "Integer32"
_QtechGlobalViolationBlockThresh_Object = MibScalar
qtechGlobalViolationBlockThresh = _QtechGlobalViolationBlockThresh_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 6),
    _QtechGlobalViolationBlockThresh_Type()
)
qtechGlobalViolationBlockThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalViolationBlockThresh.setStatus("current")


class _QtechGlobalViolationBlockAction_Type(Integer32):
    """Custom type qtechGlobalViolationBlockAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("globalblock", 1),
          ("zoneblock", 2))
    )


_QtechGlobalViolationBlockAction_Type.__name__ = "Integer32"
_QtechGlobalViolationBlockAction_Object = MibScalar
qtechGlobalViolationBlockAction = _QtechGlobalViolationBlockAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 7),
    _QtechGlobalViolationBlockAction_Type()
)
qtechGlobalViolationBlockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalViolationBlockAction.setStatus("current")


class _QtechGlobalViolationBlockTimeout_Type(Integer32):
    """Custom type qtechGlobalViolationBlockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_QtechGlobalViolationBlockTimeout_Type.__name__ = "Integer32"
_QtechGlobalViolationBlockTimeout_Object = MibScalar
qtechGlobalViolationBlockTimeout = _QtechGlobalViolationBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 8),
    _QtechGlobalViolationBlockTimeout_Type()
)
qtechGlobalViolationBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalViolationBlockTimeout.setStatus("current")
_ViolationTime_Type = DisplayString
_ViolationTime_Object = MibScalar
violationTime = _ViolationTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 9),
    _ViolationTime_Type()
)
violationTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationTime.setStatus("current")
_ViolationSrcIP_Type = IpAddress
_ViolationSrcIP_Object = MibScalar
violationSrcIP = _ViolationSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 10),
    _ViolationSrcIP_Type()
)
violationSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationSrcIP.setStatus("current")
_ViolationDestIP_Type = IpAddress
_ViolationDestIP_Object = MibScalar
violationDestIP = _ViolationDestIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 11),
    _ViolationDestIP_Type()
)
violationDestIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationDestIP.setStatus("current")
_ViolationProtocol_Type = Integer32
_ViolationProtocol_Object = MibScalar
violationProtocol = _ViolationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 12),
    _ViolationProtocol_Type()
)
violationProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationProtocol.setStatus("current")
_ViolationL4Key_Type = Integer32
_ViolationL4Key_Object = MibScalar
violationL4Key = _ViolationL4Key_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 1, 13),
    _ViolationL4Key_Type()
)
violationL4Key.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    violationL4Key.setStatus("current")
_QtechSecZoneMIBTraps_ObjectIdentity = ObjectIdentity
qtechSecZoneMIBTraps = _QtechSecZoneMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 2)
)
_QtechSecZoneMIBConformance_ObjectIdentity = ObjectIdentity
qtechSecZoneMIBConformance = _QtechSecZoneMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3)
)
_QtechSecZoneMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSecZoneMIBCompliances = _QtechSecZoneMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3, 1)
)
_QtechSecZoneMIBGroups_ObjectIdentity = ObjectIdentity
qtechSecZoneMIBGroups = _QtechSecZoneMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3, 2)
)

# Managed Objects groups

qtechSecZoneMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3, 2, 1)
)
qtechSecZoneMIBGroup.setObjects(
      *(("QTECH-SECZONE-MIB", "qtechSecZoneChainName"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneLevel"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneAclName"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneViolationNotifyThresh"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneViolationNotifyAction"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneViolationBlockThresh"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneViolationBlockAction"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneViolationBlockTimeout"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneChainEntryStatus"),
        ("QTECH-SECZONE-MIB", "qtechZoneFirstName"),
        ("QTECH-SECZONE-MIB", "qtechZoneSecondName"),
        ("QTECH-SECZONE-MIB", "qtechZone2ZoneAclName"),
        ("QTECH-SECZONE-MIB", "qtechZone2ZoneEntryStauts"),
        ("QTECH-SECZONE-MIB", "qtechBockingIP"),
        ("QTECH-SECZONE-MIB", "qtechBockingCurrentStatus"),
        ("QTECH-SECZONE-MIB", "qtechBockingTryAccessZoneName"),
        ("QTECH-SECZONE-MIB", "qtechBockingEntryStatus"),
        ("QTECH-SECZONE-MIB", "qtechGlobalViolationNotifyThresh"),
        ("QTECH-SECZONE-MIB", "qtechGlobalViolationNotifyAction"),
        ("QTECH-SECZONE-MIB", "qtechGlobalViolationBlockThresh"),
        ("QTECH-SECZONE-MIB", "qtechGlobalViolationBlockAction"),
        ("QTECH-SECZONE-MIB", "qtechGlobalViolationBlockTimeout"))
)
if mibBuilder.loadTexts:
    qtechSecZoneMIBGroup.setStatus("current")

qtechSecZoneNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3, 2, 2)
)
qtechSecZoneNotifObjectsGroup.setObjects(
      *(("QTECH-SECZONE-MIB", "violationTime"),
        ("QTECH-SECZONE-MIB", "violationSrcIP"),
        ("QTECH-SECZONE-MIB", "violationDestIP"),
        ("QTECH-SECZONE-MIB", "violationProtocol"),
        ("QTECH-SECZONE-MIB", "violationL4Key"))
)
if mibBuilder.loadTexts:
    qtechSecZoneNotifObjectsGroup.setStatus("current")


# Notification objects

qtechSecZoneViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 2, 1)
)
qtechSecZoneViolationTrap.setObjects(
      *(("QTECH-SECZONE-MIB", "violationTime"),
        ("QTECH-SECZONE-MIB", "violationSrcIP"),
        ("QTECH-SECZONE-MIB", "violationDestIP"),
        ("QTECH-SECZONE-MIB", "violationProtocol"),
        ("QTECH-SECZONE-MIB", "violationL4Key"),
        ("QTECH-SECZONE-MIB", "qtechZoneFirstName"),
        ("QTECH-SECZONE-MIB", "qtechZoneSecondName"))
)
if mibBuilder.loadTexts:
    qtechSecZoneViolationTrap.setStatus(
        "current"
    )


# Notifications groups

qtechSecZoneNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3, 2, 3)
)
qtechSecZoneNotificationsGroup.setObjects(
    ("QTECH-SECZONE-MIB", "qtechSecZoneViolationTrap")
)
if mibBuilder.loadTexts:
    qtechSecZoneNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechSecZoneMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 54, 3, 1, 1)
)
qtechSecZoneMIBCompliance.setObjects(
      *(("QTECH-SECZONE-MIB", "qtechSecZoneMIBGroup"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneNotifObjectsGroup"),
        ("QTECH-SECZONE-MIB", "qtechSecZoneNotificationsGroup"))
)
if mibBuilder.loadTexts:
    qtechSecZoneMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SECZONE-MIB",
    **{"qtechSecZoneMIB": qtechSecZoneMIB,
       "qtechSecZoneMIBObjects": qtechSecZoneMIBObjects,
       "qtechSecZoneChainTable": qtechSecZoneChainTable,
       "qtechSecZoneChainEntry": qtechSecZoneChainEntry,
       "qtechSecZoneChainName": qtechSecZoneChainName,
       "qtechSecZoneLevel": qtechSecZoneLevel,
       "qtechSecZoneAclName": qtechSecZoneAclName,
       "qtechSecZoneViolationNotifyThresh": qtechSecZoneViolationNotifyThresh,
       "qtechSecZoneViolationNotifyAction": qtechSecZoneViolationNotifyAction,
       "qtechSecZoneViolationBlockThresh": qtechSecZoneViolationBlockThresh,
       "qtechSecZoneViolationBlockAction": qtechSecZoneViolationBlockAction,
       "qtechSecZoneViolationBlockTimeout": qtechSecZoneViolationBlockTimeout,
       "qtechSecZoneChainEntryStatus": qtechSecZoneChainEntryStatus,
       "qtechSecZone2ZoneTable": qtechSecZone2ZoneTable,
       "qtechSecZone2ZoneEntry": qtechSecZone2ZoneEntry,
       "qtechZoneFirstName": qtechZoneFirstName,
       "qtechZoneSecondName": qtechZoneSecondName,
       "qtechZone2ZoneAclName": qtechZone2ZoneAclName,
       "qtechZone2ZoneEntryStauts": qtechZone2ZoneEntryStauts,
       "qtechSecZoneBlockingTable": qtechSecZoneBlockingTable,
       "qtechSecZoneBlockingEntry": qtechSecZoneBlockingEntry,
       "qtechBockingIP": qtechBockingIP,
       "qtechBockingCurrentStatus": qtechBockingCurrentStatus,
       "qtechBockingTryAccessZoneName": qtechBockingTryAccessZoneName,
       "qtechBockingEntryStatus": qtechBockingEntryStatus,
       "qtechGlobalViolationNotifyThresh": qtechGlobalViolationNotifyThresh,
       "qtechGlobalViolationNotifyAction": qtechGlobalViolationNotifyAction,
       "qtechGlobalViolationBlockThresh": qtechGlobalViolationBlockThresh,
       "qtechGlobalViolationBlockAction": qtechGlobalViolationBlockAction,
       "qtechGlobalViolationBlockTimeout": qtechGlobalViolationBlockTimeout,
       "violationTime": violationTime,
       "violationSrcIP": violationSrcIP,
       "violationDestIP": violationDestIP,
       "violationProtocol": violationProtocol,
       "violationL4Key": violationL4Key,
       "qtechSecZoneMIBTraps": qtechSecZoneMIBTraps,
       "qtechSecZoneViolationTrap": qtechSecZoneViolationTrap,
       "qtechSecZoneMIBConformance": qtechSecZoneMIBConformance,
       "qtechSecZoneMIBCompliances": qtechSecZoneMIBCompliances,
       "qtechSecZoneMIBCompliance": qtechSecZoneMIBCompliance,
       "qtechSecZoneMIBGroups": qtechSecZoneMIBGroups,
       "qtechSecZoneMIBGroup": qtechSecZoneMIBGroup,
       "qtechSecZoneNotifObjectsGroup": qtechSecZoneNotifObjectsGroup,
       "qtechSecZoneNotificationsGroup": qtechSecZoneNotificationsGroup}
)
