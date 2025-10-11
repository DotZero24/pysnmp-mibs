# SNMP MIB module (QTECH-SECZONE-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SECZONE-CONTEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:29 2025
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

qtechSecZoneVCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68)
)
if mibBuilder.loadTexts:
    qtechSecZoneVCMIB.setRevisions(
        ("2009-12-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSecZoneVCMIBObjects_ObjectIdentity = ObjectIdentity
qtechSecZoneVCMIBObjects = _QtechSecZoneVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1)
)
_QtechSecZoneChainVCTable_Object = MibTable
qtechSecZoneChainVCTable = _QtechSecZoneChainVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1)
)
if mibBuilder.loadTexts:
    qtechSecZoneChainVCTable.setStatus("current")
_QtechSecZoneChainVCEntry_Object = MibTableRow
qtechSecZoneChainVCEntry = _QtechSecZoneChainVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1)
)
qtechSecZoneChainVCEntry.setIndexNames(
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneContextNameVC"),
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneChainNameVC"),
)
if mibBuilder.loadTexts:
    qtechSecZoneChainVCEntry.setStatus("current")


class _QtechSecZoneContextNameVC_Type(DisplayString):
    """Custom type qtechSecZoneContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QtechSecZoneContextNameVC_Type.__name__ = "DisplayString"
_QtechSecZoneContextNameVC_Object = MibTableColumn
qtechSecZoneContextNameVC = _QtechSecZoneContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 1),
    _QtechSecZoneContextNameVC_Type()
)
qtechSecZoneContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSecZoneContextNameVC.setStatus("current")


class _QtechSecZoneChainNameVC_Type(DisplayString):
    """Custom type qtechSecZoneChainNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSecZoneChainNameVC_Type.__name__ = "DisplayString"
_QtechSecZoneChainNameVC_Object = MibTableColumn
qtechSecZoneChainNameVC = _QtechSecZoneChainNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 2),
    _QtechSecZoneChainNameVC_Type()
)
qtechSecZoneChainNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSecZoneChainNameVC.setStatus("current")


class _QtechSecZoneLevelVC_Type(Integer32):
    """Custom type qtechSecZoneLevelVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechSecZoneLevelVC_Type.__name__ = "Integer32"
_QtechSecZoneLevelVC_Object = MibTableColumn
qtechSecZoneLevelVC = _QtechSecZoneLevelVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 3),
    _QtechSecZoneLevelVC_Type()
)
qtechSecZoneLevelVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneLevelVC.setStatus("current")


class _QtechSecZoneAclNameVC_Type(DisplayString):
    """Custom type qtechSecZoneAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechSecZoneAclNameVC_Type.__name__ = "DisplayString"
_QtechSecZoneAclNameVC_Object = MibTableColumn
qtechSecZoneAclNameVC = _QtechSecZoneAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 4),
    _QtechSecZoneAclNameVC_Type()
)
qtechSecZoneAclNameVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneAclNameVC.setStatus("current")


class _QtechSecZoneViolationNotifyThreshVC_Type(Integer32):
    """Custom type qtechSecZoneViolationNotifyThreshVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechSecZoneViolationNotifyThreshVC_Type.__name__ = "Integer32"
_QtechSecZoneViolationNotifyThreshVC_Object = MibTableColumn
qtechSecZoneViolationNotifyThreshVC = _QtechSecZoneViolationNotifyThreshVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 5),
    _QtechSecZoneViolationNotifyThreshVC_Type()
)
qtechSecZoneViolationNotifyThreshVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneViolationNotifyThreshVC.setStatus("current")


class _QtechSecZoneViolationNotifyActionVC_Type(Integer32):
    """Custom type qtechSecZoneViolationNotifyActionVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nologtrap", 0),
          ("log", 1),
          ("trap", 2),
          ("logtrap", 3))
    )


_QtechSecZoneViolationNotifyActionVC_Type.__name__ = "Integer32"
_QtechSecZoneViolationNotifyActionVC_Object = MibTableColumn
qtechSecZoneViolationNotifyActionVC = _QtechSecZoneViolationNotifyActionVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 6),
    _QtechSecZoneViolationNotifyActionVC_Type()
)
qtechSecZoneViolationNotifyActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneViolationNotifyActionVC.setStatus("current")


class _QtechSecZoneViolationBlockThreshVC_Type(Integer32):
    """Custom type qtechSecZoneViolationBlockThreshVC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_QtechSecZoneViolationBlockThreshVC_Type.__name__ = "Integer32"
_QtechSecZoneViolationBlockThreshVC_Object = MibTableColumn
qtechSecZoneViolationBlockThreshVC = _QtechSecZoneViolationBlockThreshVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 7),
    _QtechSecZoneViolationBlockThreshVC_Type()
)
qtechSecZoneViolationBlockThreshVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneViolationBlockThreshVC.setStatus("current")


class _QtechSecZoneViolationBlockActionVC_Type(Integer32):
    """Custom type qtechSecZoneViolationBlockActionVC based on Integer32"""
    defaultValue = 1

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


_QtechSecZoneViolationBlockActionVC_Type.__name__ = "Integer32"
_QtechSecZoneViolationBlockActionVC_Object = MibTableColumn
qtechSecZoneViolationBlockActionVC = _QtechSecZoneViolationBlockActionVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 8),
    _QtechSecZoneViolationBlockActionVC_Type()
)
qtechSecZoneViolationBlockActionVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneViolationBlockActionVC.setStatus("current")


class _QtechSecZoneViolationBlockTimeoutVC_Type(Integer32):
    """Custom type qtechSecZoneViolationBlockTimeoutVC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_QtechSecZoneViolationBlockTimeoutVC_Type.__name__ = "Integer32"
_QtechSecZoneViolationBlockTimeoutVC_Object = MibTableColumn
qtechSecZoneViolationBlockTimeoutVC = _QtechSecZoneViolationBlockTimeoutVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 9),
    _QtechSecZoneViolationBlockTimeoutVC_Type()
)
qtechSecZoneViolationBlockTimeoutVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneViolationBlockTimeoutVC.setStatus("current")
_QtechSecZoneChainEntryStatusVC_Type = RowStatus
_QtechSecZoneChainEntryStatusVC_Object = MibTableColumn
qtechSecZoneChainEntryStatusVC = _QtechSecZoneChainEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 1, 1, 10),
    _QtechSecZoneChainEntryStatusVC_Type()
)
qtechSecZoneChainEntryStatusVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecZoneChainEntryStatusVC.setStatus("current")
_QtechSecZone2ZoneVCTable_Object = MibTable
qtechSecZone2ZoneVCTable = _QtechSecZone2ZoneVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2)
)
if mibBuilder.loadTexts:
    qtechSecZone2ZoneVCTable.setStatus("current")
_QtechSecZone2ZoneVCEntry_Object = MibTableRow
qtechSecZone2ZoneVCEntry = _QtechSecZone2ZoneVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2, 1)
)
qtechSecZone2ZoneVCEntry.setIndexNames(
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechZone2ZoneContextNameVC"),
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechZoneFirstNameVC"),
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechZoneSecondNameVC"),
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechZone2ZoneAclNameVC"),
)
if mibBuilder.loadTexts:
    qtechSecZone2ZoneVCEntry.setStatus("current")


class _QtechZone2ZoneContextNameVC_Type(DisplayString):
    """Custom type qtechZone2ZoneContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QtechZone2ZoneContextNameVC_Type.__name__ = "DisplayString"
_QtechZone2ZoneContextNameVC_Object = MibTableColumn
qtechZone2ZoneContextNameVC = _QtechZone2ZoneContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2, 1, 1),
    _QtechZone2ZoneContextNameVC_Type()
)
qtechZone2ZoneContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZone2ZoneContextNameVC.setStatus("current")


class _QtechZoneFirstNameVC_Type(DisplayString):
    """Custom type qtechZoneFirstNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechZoneFirstNameVC_Type.__name__ = "DisplayString"
_QtechZoneFirstNameVC_Object = MibTableColumn
qtechZoneFirstNameVC = _QtechZoneFirstNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2, 1, 2),
    _QtechZoneFirstNameVC_Type()
)
qtechZoneFirstNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZoneFirstNameVC.setStatus("current")


class _QtechZoneSecondNameVC_Type(DisplayString):
    """Custom type qtechZoneSecondNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechZoneSecondNameVC_Type.__name__ = "DisplayString"
_QtechZoneSecondNameVC_Object = MibTableColumn
qtechZoneSecondNameVC = _QtechZoneSecondNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2, 1, 3),
    _QtechZoneSecondNameVC_Type()
)
qtechZoneSecondNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZoneSecondNameVC.setStatus("current")


class _QtechZone2ZoneAclNameVC_Type(DisplayString):
    """Custom type qtechZone2ZoneAclNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechZone2ZoneAclNameVC_Type.__name__ = "DisplayString"
_QtechZone2ZoneAclNameVC_Object = MibTableColumn
qtechZone2ZoneAclNameVC = _QtechZone2ZoneAclNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2, 1, 4),
    _QtechZone2ZoneAclNameVC_Type()
)
qtechZone2ZoneAclNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechZone2ZoneAclNameVC.setStatus("current")
_QtechZone2ZoneEntryStautsVC_Type = RowStatus
_QtechZone2ZoneEntryStautsVC_Object = MibTableColumn
qtechZone2ZoneEntryStautsVC = _QtechZone2ZoneEntryStautsVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 2, 1, 5),
    _QtechZone2ZoneEntryStautsVC_Type()
)
qtechZone2ZoneEntryStautsVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechZone2ZoneEntryStautsVC.setStatus("current")
_QtechSecZoneBlockingVCTable_Object = MibTable
qtechSecZoneBlockingVCTable = _QtechSecZoneBlockingVCTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3)
)
if mibBuilder.loadTexts:
    qtechSecZoneBlockingVCTable.setStatus("current")
_QtechSecZoneBlockingVCEntry_Object = MibTableRow
qtechSecZoneBlockingVCEntry = _QtechSecZoneBlockingVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3, 1)
)
qtechSecZoneBlockingVCEntry.setIndexNames(
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechBockingContextNameVC"),
    (0, "QTECH-SECZONE-CONTEXT-MIB", "qtechBockingIPVC"),
)
if mibBuilder.loadTexts:
    qtechSecZoneBlockingVCEntry.setStatus("current")


class _QtechBockingContextNameVC_Type(DisplayString):
    """Custom type qtechBockingContextNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_QtechBockingContextNameVC_Type.__name__ = "DisplayString"
_QtechBockingContextNameVC_Object = MibTableColumn
qtechBockingContextNameVC = _QtechBockingContextNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3, 1, 1),
    _QtechBockingContextNameVC_Type()
)
qtechBockingContextNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingContextNameVC.setStatus("current")
_QtechBockingIPVC_Type = IpAddress
_QtechBockingIPVC_Object = MibTableColumn
qtechBockingIPVC = _QtechBockingIPVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3, 1, 2),
    _QtechBockingIPVC_Type()
)
qtechBockingIPVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingIPVC.setStatus("current")


class _QtechBockingCurrentStatusVC_Type(Integer32):
    """Custom type qtechBockingCurrentStatusVC based on Integer32"""
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


_QtechBockingCurrentStatusVC_Type.__name__ = "Integer32"
_QtechBockingCurrentStatusVC_Object = MibTableColumn
qtechBockingCurrentStatusVC = _QtechBockingCurrentStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3, 1, 3),
    _QtechBockingCurrentStatusVC_Type()
)
qtechBockingCurrentStatusVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingCurrentStatusVC.setStatus("current")


class _QtechBockingTryAccessZoneNameVC_Type(DisplayString):
    """Custom type qtechBockingTryAccessZoneNameVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechBockingTryAccessZoneNameVC_Type.__name__ = "DisplayString"
_QtechBockingTryAccessZoneNameVC_Object = MibTableColumn
qtechBockingTryAccessZoneNameVC = _QtechBockingTryAccessZoneNameVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3, 1, 4),
    _QtechBockingTryAccessZoneNameVC_Type()
)
qtechBockingTryAccessZoneNameVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechBockingTryAccessZoneNameVC.setStatus("current")
_QtechBockingEntryStatusVC_Type = ConfigStatus
_QtechBockingEntryStatusVC_Object = MibTableColumn
qtechBockingEntryStatusVC = _QtechBockingEntryStatusVC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 1, 3, 1, 5),
    _QtechBockingEntryStatusVC_Type()
)
qtechBockingEntryStatusVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechBockingEntryStatusVC.setStatus("current")
_QtechSecZoneVCMIBConformance_ObjectIdentity = ObjectIdentity
qtechSecZoneVCMIBConformance = _QtechSecZoneVCMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 3)
)
_QtechSecZoneVCMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSecZoneVCMIBCompliances = _QtechSecZoneVCMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 3, 1)
)
_QtechSecZoneVCMIBGroups_ObjectIdentity = ObjectIdentity
qtechSecZoneVCMIBGroups = _QtechSecZoneVCMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 3, 2)
)

# Managed Objects groups

qtechSecZoneVCMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 3, 2, 1)
)
qtechSecZoneVCMIBGroup.setObjects(
      *(("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneContextNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneChainNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneLevelVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneAclNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneViolationNotifyThreshVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneViolationNotifyActionVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneViolationBlockThreshVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneViolationBlockActionVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneViolationBlockTimeoutVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneChainEntryStatusVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechZone2ZoneContextNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechZoneFirstNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechZoneSecondNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechZone2ZoneAclNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechZone2ZoneEntryStautsVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechBockingContextNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechBockingIPVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechBockingCurrentStatusVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechBockingTryAccessZoneNameVC"),
        ("QTECH-SECZONE-CONTEXT-MIB", "qtechBockingEntryStatusVC"))
)
if mibBuilder.loadTexts:
    qtechSecZoneVCMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechSecZoneVCMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 68, 3, 1, 1)
)
qtechSecZoneVCMIBCompliance.setObjects(
    ("QTECH-SECZONE-CONTEXT-MIB", "qtechSecZoneVCMIBGroup")
)
if mibBuilder.loadTexts:
    qtechSecZoneVCMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SECZONE-CONTEXT-MIB",
    **{"qtechSecZoneVCMIB": qtechSecZoneVCMIB,
       "qtechSecZoneVCMIBObjects": qtechSecZoneVCMIBObjects,
       "qtechSecZoneChainVCTable": qtechSecZoneChainVCTable,
       "qtechSecZoneChainVCEntry": qtechSecZoneChainVCEntry,
       "qtechSecZoneContextNameVC": qtechSecZoneContextNameVC,
       "qtechSecZoneChainNameVC": qtechSecZoneChainNameVC,
       "qtechSecZoneLevelVC": qtechSecZoneLevelVC,
       "qtechSecZoneAclNameVC": qtechSecZoneAclNameVC,
       "qtechSecZoneViolationNotifyThreshVC": qtechSecZoneViolationNotifyThreshVC,
       "qtechSecZoneViolationNotifyActionVC": qtechSecZoneViolationNotifyActionVC,
       "qtechSecZoneViolationBlockThreshVC": qtechSecZoneViolationBlockThreshVC,
       "qtechSecZoneViolationBlockActionVC": qtechSecZoneViolationBlockActionVC,
       "qtechSecZoneViolationBlockTimeoutVC": qtechSecZoneViolationBlockTimeoutVC,
       "qtechSecZoneChainEntryStatusVC": qtechSecZoneChainEntryStatusVC,
       "qtechSecZone2ZoneVCTable": qtechSecZone2ZoneVCTable,
       "qtechSecZone2ZoneVCEntry": qtechSecZone2ZoneVCEntry,
       "qtechZone2ZoneContextNameVC": qtechZone2ZoneContextNameVC,
       "qtechZoneFirstNameVC": qtechZoneFirstNameVC,
       "qtechZoneSecondNameVC": qtechZoneSecondNameVC,
       "qtechZone2ZoneAclNameVC": qtechZone2ZoneAclNameVC,
       "qtechZone2ZoneEntryStautsVC": qtechZone2ZoneEntryStautsVC,
       "qtechSecZoneBlockingVCTable": qtechSecZoneBlockingVCTable,
       "qtechSecZoneBlockingVCEntry": qtechSecZoneBlockingVCEntry,
       "qtechBockingContextNameVC": qtechBockingContextNameVC,
       "qtechBockingIPVC": qtechBockingIPVC,
       "qtechBockingCurrentStatusVC": qtechBockingCurrentStatusVC,
       "qtechBockingTryAccessZoneNameVC": qtechBockingTryAccessZoneNameVC,
       "qtechBockingEntryStatusVC": qtechBockingEntryStatusVC,
       "qtechSecZoneVCMIBConformance": qtechSecZoneVCMIBConformance,
       "qtechSecZoneVCMIBCompliances": qtechSecZoneVCMIBCompliances,
       "qtechSecZoneVCMIBCompliance": qtechSecZoneVCMIBCompliance,
       "qtechSecZoneVCMIBGroups": qtechSecZoneVCMIBGroups,
       "qtechSecZoneVCMIBGroup": qtechSecZoneVCMIBGroup}
)
