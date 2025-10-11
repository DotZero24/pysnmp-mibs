# SNMP MIB module (H3C-LBV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-LBV2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:35 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cLBv2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148)
)
if mibBuilder.loadTexts:
    h3cLBv2.setRevisions(
        ("2013-11-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cLBv2GlobalObjects_ObjectIdentity = ObjectIdentity
h3cLBv2GlobalObjects = _H3cLBv2GlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 1)
)


class _H3cLBv2TrapEnable_Type(Integer32):
    """Custom type h3cLBv2TrapEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_H3cLBv2TrapEnable_Type.__name__ = "Integer32"
_H3cLBv2TrapEnable_Object = MibScalar
h3cLBv2TrapEnable = _H3cLBv2TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 1, 1),
    _H3cLBv2TrapEnable_Type()
)
h3cLBv2TrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cLBv2TrapEnable.setStatus("current")
_H3cLBv2ActionTables_ObjectIdentity = ObjectIdentity
h3cLBv2ActionTables = _H3cLBv2ActionTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2)
)
_H3cLBv2ActionTable_Object = MibTable
h3cLBv2ActionTable = _H3cLBv2ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1)
)
if mibBuilder.loadTexts:
    h3cLBv2ActionTable.setStatus("current")
_H3cLBv2ActionEntry_Object = MibTableRow
h3cLBv2ActionEntry = _H3cLBv2ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1, 1)
)
h3cLBv2ActionEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2ActionName"),
)
if mibBuilder.loadTexts:
    h3cLBv2ActionEntry.setStatus("current")


class _H3cLBv2ActionName_Type(DisplayString):
    """Custom type h3cLBv2ActionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cLBv2ActionName_Type.__name__ = "DisplayString"
_H3cLBv2ActionName_Object = MibTableColumn
h3cLBv2ActionName = _H3cLBv2ActionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1, 1, 1),
    _H3cLBv2ActionName_Type()
)
h3cLBv2ActionName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2ActionName.setStatus("current")


class _H3cLBv2ActionDefaultSF_Type(DisplayString):
    """Custom type h3cLBv2ActionDefaultSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cLBv2ActionDefaultSF_Type.__name__ = "DisplayString"
_H3cLBv2ActionDefaultSF_Object = MibTableColumn
h3cLBv2ActionDefaultSF = _H3cLBv2ActionDefaultSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1, 1, 2),
    _H3cLBv2ActionDefaultSF_Type()
)
h3cLBv2ActionDefaultSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2ActionDefaultSF.setStatus("current")


class _H3cLBv2ActionBackupSF_Type(DisplayString):
    """Custom type h3cLBv2ActionBackupSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cLBv2ActionBackupSF_Type.__name__ = "DisplayString"
_H3cLBv2ActionBackupSF_Object = MibTableColumn
h3cLBv2ActionBackupSF = _H3cLBv2ActionBackupSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1, 1, 3),
    _H3cLBv2ActionBackupSF_Type()
)
h3cLBv2ActionBackupSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2ActionBackupSF.setStatus("current")


class _H3cLBv2ActionInUseSF_Type(DisplayString):
    """Custom type h3cLBv2ActionInUseSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cLBv2ActionInUseSF_Type.__name__ = "DisplayString"
_H3cLBv2ActionInUseSF_Object = MibTableColumn
h3cLBv2ActionInUseSF = _H3cLBv2ActionInUseSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1, 1, 4),
    _H3cLBv2ActionInUseSF_Type()
)
h3cLBv2ActionInUseSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2ActionInUseSF.setStatus("current")
_H3cLBv2ActionRowStatus_Type = RowStatus
_H3cLBv2ActionRowStatus_Object = MibTableColumn
h3cLBv2ActionRowStatus = _H3cLBv2ActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 2, 1, 1, 5),
    _H3cLBv2ActionRowStatus_Type()
)
h3cLBv2ActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2ActionRowStatus.setStatus("current")
_H3cLBv2VSTables_ObjectIdentity = ObjectIdentity
h3cLBv2VSTables = _H3cLBv2VSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3)
)
_H3cLBv2VSTable_Object = MibTable
h3cLBv2VSTable = _H3cLBv2VSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1)
)
if mibBuilder.loadTexts:
    h3cLBv2VSTable.setStatus("current")
_H3cLBv2VSEntry_Object = MibTableRow
h3cLBv2VSEntry = _H3cLBv2VSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1)
)
h3cLBv2VSEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2VSName"),
)
if mibBuilder.loadTexts:
    h3cLBv2VSEntry.setStatus("current")


class _H3cLBv2VSName_Type(DisplayString):
    """Custom type h3cLBv2VSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cLBv2VSName_Type.__name__ = "DisplayString"
_H3cLBv2VSName_Object = MibTableColumn
h3cLBv2VSName = _H3cLBv2VSName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 1),
    _H3cLBv2VSName_Type()
)
h3cLBv2VSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2VSName.setStatus("current")


class _H3cLBv2VSConnectionsLimit_Type(Unsigned32):
    """Custom type h3cLBv2VSConnectionsLimit based on Unsigned32"""
    defaultValue = 0


_H3cLBv2VSConnectionsLimit_Type.__name__ = "Unsigned32"
_H3cLBv2VSConnectionsLimit_Object = MibTableColumn
h3cLBv2VSConnectionsLimit = _H3cLBv2VSConnectionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 2),
    _H3cLBv2VSConnectionsLimit_Type()
)
h3cLBv2VSConnectionsLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2VSConnectionsLimit.setStatus("current")


class _H3cLBv2VSConnectionsRateLimit_Type(Unsigned32):
    """Custom type h3cLBv2VSConnectionsRateLimit based on Unsigned32"""
    defaultValue = 0


_H3cLBv2VSConnectionsRateLimit_Type.__name__ = "Unsigned32"
_H3cLBv2VSConnectionsRateLimit_Object = MibTableColumn
h3cLBv2VSConnectionsRateLimit = _H3cLBv2VSConnectionsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 3),
    _H3cLBv2VSConnectionsRateLimit_Type()
)
h3cLBv2VSConnectionsRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2VSConnectionsRateLimit.setStatus("current")


class _H3cLBv2VSDefaultSF_Type(DisplayString):
    """Custom type h3cLBv2VSDefaultSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cLBv2VSDefaultSF_Type.__name__ = "DisplayString"
_H3cLBv2VSDefaultSF_Object = MibTableColumn
h3cLBv2VSDefaultSF = _H3cLBv2VSDefaultSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 4),
    _H3cLBv2VSDefaultSF_Type()
)
h3cLBv2VSDefaultSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2VSDefaultSF.setStatus("current")


class _H3cLBv2VSBackupSF_Type(DisplayString):
    """Custom type h3cLBv2VSBackupSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cLBv2VSBackupSF_Type.__name__ = "DisplayString"
_H3cLBv2VSBackupSF_Object = MibTableColumn
h3cLBv2VSBackupSF = _H3cLBv2VSBackupSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 5),
    _H3cLBv2VSBackupSF_Type()
)
h3cLBv2VSBackupSF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2VSBackupSF.setStatus("current")


class _H3cLBv2VSInUseSF_Type(DisplayString):
    """Custom type h3cLBv2VSInUseSF based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_H3cLBv2VSInUseSF_Type.__name__ = "DisplayString"
_H3cLBv2VSInUseSF_Object = MibTableColumn
h3cLBv2VSInUseSF = _H3cLBv2VSInUseSF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 6),
    _H3cLBv2VSInUseSF_Type()
)
h3cLBv2VSInUseSF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSInUseSF.setStatus("current")
_H3cLBv2VSRowStatus_Type = RowStatus
_H3cLBv2VSRowStatus_Object = MibTableColumn
h3cLBv2VSRowStatus = _H3cLBv2VSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 1, 1, 7),
    _H3cLBv2VSRowStatus_Type()
)
h3cLBv2VSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2VSRowStatus.setStatus("current")
_H3cLBv2VSStatsTable_Object = MibTable
h3cLBv2VSStatsTable = _H3cLBv2VSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2)
)
if mibBuilder.loadTexts:
    h3cLBv2VSStatsTable.setStatus("current")
_H3cLBv2VSStatsEntry_Object = MibTableRow
h3cLBv2VSStatsEntry = _H3cLBv2VSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1)
)
h3cLBv2VSStatsEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2VSName"),
    (0, "H3C-LBV2-MIB", "h3cLBv2VSStatChassis"),
    (0, "H3C-LBV2-MIB", "h3cLBv2VSStatSlot"),
    (0, "H3C-LBV2-MIB", "h3cLBv2VSStatCpuid"),
)
if mibBuilder.loadTexts:
    h3cLBv2VSStatsEntry.setStatus("current")


class _H3cLBv2VSStatChassis_Type(Unsigned32):
    """Custom type h3cLBv2VSStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2VSStatChassis_Type.__name__ = "Unsigned32"
_H3cLBv2VSStatChassis_Object = MibTableColumn
h3cLBv2VSStatChassis = _H3cLBv2VSStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 1),
    _H3cLBv2VSStatChassis_Type()
)
h3cLBv2VSStatChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2VSStatChassis.setStatus("current")


class _H3cLBv2VSStatSlot_Type(Unsigned32):
    """Custom type h3cLBv2VSStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2VSStatSlot_Type.__name__ = "Unsigned32"
_H3cLBv2VSStatSlot_Object = MibTableColumn
h3cLBv2VSStatSlot = _H3cLBv2VSStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 2),
    _H3cLBv2VSStatSlot_Type()
)
h3cLBv2VSStatSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2VSStatSlot.setStatus("current")


class _H3cLBv2VSStatCpuid_Type(Unsigned32):
    """Custom type h3cLBv2VSStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2VSStatCpuid_Type.__name__ = "Unsigned32"
_H3cLBv2VSStatCpuid_Object = MibTableColumn
h3cLBv2VSStatCpuid = _H3cLBv2VSStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 3),
    _H3cLBv2VSStatCpuid_Type()
)
h3cLBv2VSStatCpuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2VSStatCpuid.setStatus("current")
_H3cLBv2VSStatTotalConnections_Type = Counter64
_H3cLBv2VSStatTotalConnections_Object = MibTableColumn
h3cLBv2VSStatTotalConnections = _H3cLBv2VSStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 4),
    _H3cLBv2VSStatTotalConnections_Type()
)
h3cLBv2VSStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatTotalConnections.setStatus("current")
_H3cLBv2VSStatActiveConnections_Type = Unsigned32
_H3cLBv2VSStatActiveConnections_Object = MibTableColumn
h3cLBv2VSStatActiveConnections = _H3cLBv2VSStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 5),
    _H3cLBv2VSStatActiveConnections_Type()
)
h3cLBv2VSStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatActiveConnections.setStatus("current")
_H3cLBv2VSStatClientSidePKTsIn_Type = Counter64
_H3cLBv2VSStatClientSidePKTsIn_Object = MibTableColumn
h3cLBv2VSStatClientSidePKTsIn = _H3cLBv2VSStatClientSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 6),
    _H3cLBv2VSStatClientSidePKTsIn_Type()
)
h3cLBv2VSStatClientSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatClientSidePKTsIn.setStatus("current")
_H3cLBv2VSStatClientSidePKTsOut_Type = Counter64
_H3cLBv2VSStatClientSidePKTsOut_Object = MibTableColumn
h3cLBv2VSStatClientSidePKTsOut = _H3cLBv2VSStatClientSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 7),
    _H3cLBv2VSStatClientSidePKTsOut_Type()
)
h3cLBv2VSStatClientSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatClientSidePKTsOut.setStatus("current")
_H3cLBv2VSStatDroppedPackets_Type = Counter64
_H3cLBv2VSStatDroppedPackets_Object = MibTableColumn
h3cLBv2VSStatDroppedPackets = _H3cLBv2VSStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 8),
    _H3cLBv2VSStatDroppedPackets_Type()
)
h3cLBv2VSStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatDroppedPackets.setStatus("current")
_H3cLBv2VSStatClientSideBytesIn_Type = Counter64
_H3cLBv2VSStatClientSideBytesIn_Object = MibTableColumn
h3cLBv2VSStatClientSideBytesIn = _H3cLBv2VSStatClientSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 9),
    _H3cLBv2VSStatClientSideBytesIn_Type()
)
h3cLBv2VSStatClientSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatClientSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2VSStatClientSideBytesIn.setUnits("byte")
_H3cLBv2VSStatClientSideBytesOut_Type = Counter64
_H3cLBv2VSStatClientSideBytesOut_Object = MibTableColumn
h3cLBv2VSStatClientSideBytesOut = _H3cLBv2VSStatClientSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 10),
    _H3cLBv2VSStatClientSideBytesOut_Type()
)
h3cLBv2VSStatClientSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatClientSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2VSStatClientSideBytesOut.setUnits("byte")
_H3cLBv2VSStatReceivedRequests_Type = Counter64
_H3cLBv2VSStatReceivedRequests_Object = MibTableColumn
h3cLBv2VSStatReceivedRequests = _H3cLBv2VSStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 11),
    _H3cLBv2VSStatReceivedRequests_Type()
)
h3cLBv2VSStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatReceivedRequests.setStatus("current")
_H3cLBv2VSStatSentResponses_Type = Counter64
_H3cLBv2VSStatSentResponses_Object = MibTableColumn
h3cLBv2VSStatSentResponses = _H3cLBv2VSStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 12),
    _H3cLBv2VSStatSentResponses_Type()
)
h3cLBv2VSStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatSentResponses.setStatus("current")
_H3cLBv2VSStatConnectionsRate_Type = Unsigned32
_H3cLBv2VSStatConnectionsRate_Object = MibTableColumn
h3cLBv2VSStatConnectionsRate = _H3cLBv2VSStatConnectionsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 3, 2, 1, 13),
    _H3cLBv2VSStatConnectionsRate_Type()
)
h3cLBv2VSStatConnectionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2VSStatConnectionsRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2VSStatConnectionsRate.setUnits("cps")
_H3cLBv2RSTables_ObjectIdentity = ObjectIdentity
h3cLBv2RSTables = _H3cLBv2RSTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4)
)
_H3cLBv2RSTable_Object = MibTable
h3cLBv2RSTable = _H3cLBv2RSTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 1)
)
if mibBuilder.loadTexts:
    h3cLBv2RSTable.setStatus("current")
_H3cLBv2RSEntry_Object = MibTableRow
h3cLBv2RSEntry = _H3cLBv2RSEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 1, 1)
)
h3cLBv2RSEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2RSName"),
)
if mibBuilder.loadTexts:
    h3cLBv2RSEntry.setStatus("current")


class _H3cLBv2RSName_Type(DisplayString):
    """Custom type h3cLBv2RSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cLBv2RSName_Type.__name__ = "DisplayString"
_H3cLBv2RSName_Object = MibTableColumn
h3cLBv2RSName = _H3cLBv2RSName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 1, 1, 1),
    _H3cLBv2RSName_Type()
)
h3cLBv2RSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2RSName.setStatus("current")
_H3cLBv2RSRowStatus_Type = RowStatus
_H3cLBv2RSRowStatus_Object = MibTableColumn
h3cLBv2RSRowStatus = _H3cLBv2RSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 1, 1, 2),
    _H3cLBv2RSRowStatus_Type()
)
h3cLBv2RSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2RSRowStatus.setStatus("current")


class _H3cLBv2RSConnectionsLimit_Type(Unsigned32):
    """Custom type h3cLBv2RSConnectionsLimit based on Unsigned32"""
    defaultValue = 0


_H3cLBv2RSConnectionsLimit_Type.__name__ = "Unsigned32"
_H3cLBv2RSConnectionsLimit_Object = MibTableColumn
h3cLBv2RSConnectionsLimit = _H3cLBv2RSConnectionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 1, 1, 3),
    _H3cLBv2RSConnectionsLimit_Type()
)
h3cLBv2RSConnectionsLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2RSConnectionsLimit.setStatus("current")


class _H3cLBv2RSConnectionsRateLimit_Type(Unsigned32):
    """Custom type h3cLBv2RSConnectionsRateLimit based on Unsigned32"""
    defaultValue = 0


_H3cLBv2RSConnectionsRateLimit_Type.__name__ = "Unsigned32"
_H3cLBv2RSConnectionsRateLimit_Object = MibTableColumn
h3cLBv2RSConnectionsRateLimit = _H3cLBv2RSConnectionsRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 1, 1, 4),
    _H3cLBv2RSConnectionsRateLimit_Type()
)
h3cLBv2RSConnectionsRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2RSConnectionsRateLimit.setStatus("current")
_H3cLBv2RSStatsTable_Object = MibTable
h3cLBv2RSStatsTable = _H3cLBv2RSStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2)
)
if mibBuilder.loadTexts:
    h3cLBv2RSStatsTable.setStatus("current")
_H3cLBv2RSStatsEntry_Object = MibTableRow
h3cLBv2RSStatsEntry = _H3cLBv2RSStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1)
)
h3cLBv2RSStatsEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2RSName"),
    (0, "H3C-LBV2-MIB", "h3cLBv2RSStatChassis"),
    (0, "H3C-LBV2-MIB", "h3cLBv2RSStatSlot"),
    (0, "H3C-LBV2-MIB", "h3cLBv2RSStatCpuid"),
)
if mibBuilder.loadTexts:
    h3cLBv2RSStatsEntry.setStatus("current")


class _H3cLBv2RSStatChassis_Type(Unsigned32):
    """Custom type h3cLBv2RSStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2RSStatChassis_Type.__name__ = "Unsigned32"
_H3cLBv2RSStatChassis_Object = MibTableColumn
h3cLBv2RSStatChassis = _H3cLBv2RSStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 1),
    _H3cLBv2RSStatChassis_Type()
)
h3cLBv2RSStatChassis.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2RSStatChassis.setStatus("current")


class _H3cLBv2RSStatSlot_Type(Unsigned32):
    """Custom type h3cLBv2RSStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2RSStatSlot_Type.__name__ = "Unsigned32"
_H3cLBv2RSStatSlot_Object = MibTableColumn
h3cLBv2RSStatSlot = _H3cLBv2RSStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 2),
    _H3cLBv2RSStatSlot_Type()
)
h3cLBv2RSStatSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2RSStatSlot.setStatus("current")


class _H3cLBv2RSStatCpuid_Type(Unsigned32):
    """Custom type h3cLBv2RSStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2RSStatCpuid_Type.__name__ = "Unsigned32"
_H3cLBv2RSStatCpuid_Object = MibTableColumn
h3cLBv2RSStatCpuid = _H3cLBv2RSStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 3),
    _H3cLBv2RSStatCpuid_Type()
)
h3cLBv2RSStatCpuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2RSStatCpuid.setStatus("current")
_H3cLBv2RSStatTotalConnections_Type = Counter64
_H3cLBv2RSStatTotalConnections_Object = MibTableColumn
h3cLBv2RSStatTotalConnections = _H3cLBv2RSStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 4),
    _H3cLBv2RSStatTotalConnections_Type()
)
h3cLBv2RSStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatTotalConnections.setStatus("current")
_H3cLBv2RSStatActiveConnections_Type = Unsigned32
_H3cLBv2RSStatActiveConnections_Object = MibTableColumn
h3cLBv2RSStatActiveConnections = _H3cLBv2RSStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 5),
    _H3cLBv2RSStatActiveConnections_Type()
)
h3cLBv2RSStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatActiveConnections.setStatus("current")
_H3cLBv2RSStatServerSidePKTsIn_Type = Counter64
_H3cLBv2RSStatServerSidePKTsIn_Object = MibTableColumn
h3cLBv2RSStatServerSidePKTsIn = _H3cLBv2RSStatServerSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 6),
    _H3cLBv2RSStatServerSidePKTsIn_Type()
)
h3cLBv2RSStatServerSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatServerSidePKTsIn.setStatus("current")
_H3cLBv2RSStatServerSidePKTsOut_Type = Counter64
_H3cLBv2RSStatServerSidePKTsOut_Object = MibTableColumn
h3cLBv2RSStatServerSidePKTsOut = _H3cLBv2RSStatServerSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 7),
    _H3cLBv2RSStatServerSidePKTsOut_Type()
)
h3cLBv2RSStatServerSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatServerSidePKTsOut.setStatus("current")
_H3cLBv2RSStatDroppedPackets_Type = Counter64
_H3cLBv2RSStatDroppedPackets_Object = MibTableColumn
h3cLBv2RSStatDroppedPackets = _H3cLBv2RSStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 8),
    _H3cLBv2RSStatDroppedPackets_Type()
)
h3cLBv2RSStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatDroppedPackets.setStatus("current")
_H3cLBv2RSStatServerSideBytesIn_Type = Counter64
_H3cLBv2RSStatServerSideBytesIn_Object = MibTableColumn
h3cLBv2RSStatServerSideBytesIn = _H3cLBv2RSStatServerSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 9),
    _H3cLBv2RSStatServerSideBytesIn_Type()
)
h3cLBv2RSStatServerSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatServerSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2RSStatServerSideBytesIn.setUnits("byte")
_H3cLBv2RSStatServerSideBytesOut_Type = Counter64
_H3cLBv2RSStatServerSideBytesOut_Object = MibTableColumn
h3cLBv2RSStatServerSideBytesOut = _H3cLBv2RSStatServerSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 10),
    _H3cLBv2RSStatServerSideBytesOut_Type()
)
h3cLBv2RSStatServerSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatServerSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2RSStatServerSideBytesOut.setUnits("byte")
_H3cLBv2RSStatReceivedRequests_Type = Counter64
_H3cLBv2RSStatReceivedRequests_Object = MibTableColumn
h3cLBv2RSStatReceivedRequests = _H3cLBv2RSStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 11),
    _H3cLBv2RSStatReceivedRequests_Type()
)
h3cLBv2RSStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatReceivedRequests.setStatus("current")
_H3cLBv2RSStatSentResponses_Type = Counter64
_H3cLBv2RSStatSentResponses_Object = MibTableColumn
h3cLBv2RSStatSentResponses = _H3cLBv2RSStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 12),
    _H3cLBv2RSStatSentResponses_Type()
)
h3cLBv2RSStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatSentResponses.setStatus("current")
_H3cLBv2RSStatConnectionsRate_Type = Unsigned32
_H3cLBv2RSStatConnectionsRate_Object = MibTableColumn
h3cLBv2RSStatConnectionsRate = _H3cLBv2RSStatConnectionsRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 4, 2, 1, 13),
    _H3cLBv2RSStatConnectionsRate_Type()
)
h3cLBv2RSStatConnectionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2RSStatConnectionsRate.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2RSStatConnectionsRate.setUnits("cps")
_H3cLBv2SFTables_ObjectIdentity = ObjectIdentity
h3cLBv2SFTables = _H3cLBv2SFTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5)
)
_H3cLBv2SFTable_Object = MibTable
h3cLBv2SFTable = _H3cLBv2SFTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 1)
)
if mibBuilder.loadTexts:
    h3cLBv2SFTable.setStatus("current")
_H3cLBv2SFEntry_Object = MibTableRow
h3cLBv2SFEntry = _H3cLBv2SFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 1, 1)
)
h3cLBv2SFEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2SFName"),
)
if mibBuilder.loadTexts:
    h3cLBv2SFEntry.setStatus("current")


class _H3cLBv2SFName_Type(DisplayString):
    """Custom type h3cLBv2SFName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_H3cLBv2SFName_Type.__name__ = "DisplayString"
_H3cLBv2SFName_Object = MibTableColumn
h3cLBv2SFName = _H3cLBv2SFName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 1, 1, 1),
    _H3cLBv2SFName_Type()
)
h3cLBv2SFName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cLBv2SFName.setStatus("current")
_H3cLBv2SFRowStatus_Type = RowStatus
_H3cLBv2SFRowStatus_Object = MibTableColumn
h3cLBv2SFRowStatus = _H3cLBv2SFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 1, 1, 2),
    _H3cLBv2SFRowStatus_Type()
)
h3cLBv2SFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cLBv2SFRowStatus.setStatus("current")
_H3cLBv2SFStatsTable_Object = MibTable
h3cLBv2SFStatsTable = _H3cLBv2SFStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2)
)
if mibBuilder.loadTexts:
    h3cLBv2SFStatsTable.setStatus("current")
_H3cLBv2SFStatsEntry_Object = MibTableRow
h3cLBv2SFStatsEntry = _H3cLBv2SFStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1)
)
h3cLBv2SFStatsEntry.setIndexNames(
    (0, "H3C-LBV2-MIB", "h3cLBv2SFName"),
    (0, "H3C-LBV2-MIB", "h3cLBv2SFStatChassis"),
    (0, "H3C-LBV2-MIB", "h3cLBv2SFStatSlot"),
    (0, "H3C-LBV2-MIB", "h3cLBv2SFStatCpuid"),
)
if mibBuilder.loadTexts:
    h3cLBv2SFStatsEntry.setStatus("current")


class _H3cLBv2SFStatChassis_Type(Unsigned32):
    """Custom type h3cLBv2SFStatChassis based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2SFStatChassis_Type.__name__ = "Unsigned32"
_H3cLBv2SFStatChassis_Object = MibTableColumn
h3cLBv2SFStatChassis = _H3cLBv2SFStatChassis_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 1),
    _H3cLBv2SFStatChassis_Type()
)
h3cLBv2SFStatChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLBv2SFStatChassis.setStatus("current")


class _H3cLBv2SFStatSlot_Type(Unsigned32):
    """Custom type h3cLBv2SFStatSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2SFStatSlot_Type.__name__ = "Unsigned32"
_H3cLBv2SFStatSlot_Object = MibTableColumn
h3cLBv2SFStatSlot = _H3cLBv2SFStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 2),
    _H3cLBv2SFStatSlot_Type()
)
h3cLBv2SFStatSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLBv2SFStatSlot.setStatus("current")


class _H3cLBv2SFStatCpuid_Type(Unsigned32):
    """Custom type h3cLBv2SFStatCpuid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cLBv2SFStatCpuid_Type.__name__ = "Unsigned32"
_H3cLBv2SFStatCpuid_Object = MibTableColumn
h3cLBv2SFStatCpuid = _H3cLBv2SFStatCpuid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 3),
    _H3cLBv2SFStatCpuid_Type()
)
h3cLBv2SFStatCpuid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cLBv2SFStatCpuid.setStatus("current")
_H3cLBv2SFStatTotalConnections_Type = Counter64
_H3cLBv2SFStatTotalConnections_Object = MibTableColumn
h3cLBv2SFStatTotalConnections = _H3cLBv2SFStatTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 4),
    _H3cLBv2SFStatTotalConnections_Type()
)
h3cLBv2SFStatTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatTotalConnections.setStatus("current")
_H3cLBv2SFStatActiveConnections_Type = Unsigned32
_H3cLBv2SFStatActiveConnections_Object = MibTableColumn
h3cLBv2SFStatActiveConnections = _H3cLBv2SFStatActiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 5),
    _H3cLBv2SFStatActiveConnections_Type()
)
h3cLBv2SFStatActiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatActiveConnections.setStatus("current")
_H3cLBv2SFStatServerSidePKTsIn_Type = Counter64
_H3cLBv2SFStatServerSidePKTsIn_Object = MibTableColumn
h3cLBv2SFStatServerSidePKTsIn = _H3cLBv2SFStatServerSidePKTsIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 6),
    _H3cLBv2SFStatServerSidePKTsIn_Type()
)
h3cLBv2SFStatServerSidePKTsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatServerSidePKTsIn.setStatus("current")
_H3cLBv2SFStatServerSidePKTsOut_Type = Counter64
_H3cLBv2SFStatServerSidePKTsOut_Object = MibTableColumn
h3cLBv2SFStatServerSidePKTsOut = _H3cLBv2SFStatServerSidePKTsOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 7),
    _H3cLBv2SFStatServerSidePKTsOut_Type()
)
h3cLBv2SFStatServerSidePKTsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatServerSidePKTsOut.setStatus("current")
_H3cLBv2SFStatDroppedPackets_Type = Counter64
_H3cLBv2SFStatDroppedPackets_Object = MibTableColumn
h3cLBv2SFStatDroppedPackets = _H3cLBv2SFStatDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 8),
    _H3cLBv2SFStatDroppedPackets_Type()
)
h3cLBv2SFStatDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatDroppedPackets.setStatus("current")
_H3cLBv2SFStatServerSideBytesIn_Type = Counter64
_H3cLBv2SFStatServerSideBytesIn_Object = MibTableColumn
h3cLBv2SFStatServerSideBytesIn = _H3cLBv2SFStatServerSideBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 9),
    _H3cLBv2SFStatServerSideBytesIn_Type()
)
h3cLBv2SFStatServerSideBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatServerSideBytesIn.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2SFStatServerSideBytesIn.setUnits("byte")
_H3cLBv2SFStatServerSideBytesOut_Type = Counter64
_H3cLBv2SFStatServerSideBytesOut_Object = MibTableColumn
h3cLBv2SFStatServerSideBytesOut = _H3cLBv2SFStatServerSideBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 10),
    _H3cLBv2SFStatServerSideBytesOut_Type()
)
h3cLBv2SFStatServerSideBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatServerSideBytesOut.setStatus("current")
if mibBuilder.loadTexts:
    h3cLBv2SFStatServerSideBytesOut.setUnits("byte")
_H3cLBv2SFStatReceivedRequests_Type = Counter64
_H3cLBv2SFStatReceivedRequests_Object = MibTableColumn
h3cLBv2SFStatReceivedRequests = _H3cLBv2SFStatReceivedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 11),
    _H3cLBv2SFStatReceivedRequests_Type()
)
h3cLBv2SFStatReceivedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatReceivedRequests.setStatus("current")
_H3cLBv2SFStatSentResponses_Type = Counter64
_H3cLBv2SFStatSentResponses_Object = MibTableColumn
h3cLBv2SFStatSentResponses = _H3cLBv2SFStatSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 5, 2, 1, 12),
    _H3cLBv2SFStatSentResponses_Type()
)
h3cLBv2SFStatSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cLBv2SFStatSentResponses.setStatus("current")
_H3cLBv2Trap_ObjectIdentity = ObjectIdentity
h3cLBv2Trap = _H3cLBv2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6)
)
_H3cLBv2TrapPrefix_ObjectIdentity = ObjectIdentity
h3cLBv2TrapPrefix = _H3cLBv2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0)
)

# Managed Objects groups


# Notification objects

h3cLBv2VSConnOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 1)
)
h3cLBv2VSConnOverloadTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2VSName"),
        ("H3C-LBV2-MIB", "h3cLBv2VSConnectionsLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    h3cLBv2VSConnOverloadTrap.setStatus(
        "current"
    )

h3cLBv2VSConnRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 2)
)
h3cLBv2VSConnRecoveryTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2VSName"),
        ("H3C-LBV2-MIB", "h3cLBv2VSConnectionsLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    h3cLBv2VSConnRecoveryTrap.setStatus(
        "current"
    )

h3cLBv2VSConnsRateOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 3)
)
h3cLBv2VSConnsRateOverloadTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2VSName"),
        ("H3C-LBV2-MIB", "h3cLBv2VSConnectionsRateLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    h3cLBv2VSConnsRateOverloadTrap.setStatus(
        "current"
    )

h3cLBv2VSConnsRateRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 4)
)
h3cLBv2VSConnsRateRecoveryTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2VSName"),
        ("H3C-LBV2-MIB", "h3cLBv2VSConnectionsRateLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2VSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    h3cLBv2VSConnsRateRecoveryTrap.setStatus(
        "current"
    )

h3cLBv2VSActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 5)
)
h3cLBv2VSActiveTrap.setObjects(
    ("H3C-LBV2-MIB", "h3cLBv2VSName")
)
if mibBuilder.loadTexts:
    h3cLBv2VSActiveTrap.setStatus(
        "current"
    )

h3cLBv2VSInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 6)
)
h3cLBv2VSInactiveTrap.setObjects(
    ("H3C-LBV2-MIB", "h3cLBv2VSName")
)
if mibBuilder.loadTexts:
    h3cLBv2VSInactiveTrap.setStatus(
        "current"
    )

h3cLBv2RSAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 7)
)
h3cLBv2RSAvailableTrap.setObjects(
    ("H3C-LBV2-MIB", "h3cLBv2RSName")
)
if mibBuilder.loadTexts:
    h3cLBv2RSAvailableTrap.setStatus(
        "current"
    )

h3cLBv2RSUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 8)
)
h3cLBv2RSUnavailableTrap.setObjects(
    ("H3C-LBV2-MIB", "h3cLBv2RSName")
)
if mibBuilder.loadTexts:
    h3cLBv2RSUnavailableTrap.setStatus(
        "current"
    )

h3cLBv2SFActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 9)
)
h3cLBv2SFActiveTrap.setObjects(
    ("H3C-LBV2-MIB", "h3cLBv2SFName")
)
if mibBuilder.loadTexts:
    h3cLBv2SFActiveTrap.setStatus(
        "current"
    )

h3cLBv2SFInactiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 10)
)
h3cLBv2SFInactiveTrap.setObjects(
    ("H3C-LBV2-MIB", "h3cLBv2SFName")
)
if mibBuilder.loadTexts:
    h3cLBv2SFInactiveTrap.setStatus(
        "current"
    )

h3cLBv2ActionInUseSFChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 11)
)
h3cLBv2ActionInUseSFChangeTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2ActionName"),
        ("H3C-LBV2-MIB", "h3cLBv2ActionDefaultSF"),
        ("H3C-LBV2-MIB", "h3cLBv2ActionBackupSF"),
        ("H3C-LBV2-MIB", "h3cLBv2ActionInUseSF"))
)
if mibBuilder.loadTexts:
    h3cLBv2ActionInUseSFChangeTrap.setStatus(
        "current"
    )

h3cLBv2VSInUseSFChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 12)
)
h3cLBv2VSInUseSFChangeTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2VSName"),
        ("H3C-LBV2-MIB", "h3cLBv2VSDefaultSF"),
        ("H3C-LBV2-MIB", "h3cLBv2VSBackupSF"),
        ("H3C-LBV2-MIB", "h3cLBv2VSInUseSF"))
)
if mibBuilder.loadTexts:
    h3cLBv2VSInUseSFChangeTrap.setStatus(
        "current"
    )

h3cLBv2RSConnOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 13)
)
h3cLBv2RSConnOverloadTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2RSName"),
        ("H3C-LBV2-MIB", "h3cLBv2RSConnectionsLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    h3cLBv2RSConnOverloadTrap.setStatus(
        "current"
    )

h3cLBv2RSConnRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 14)
)
h3cLBv2RSConnRecoveryTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2RSName"),
        ("H3C-LBV2-MIB", "h3cLBv2RSConnectionsLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatActiveConnections"))
)
if mibBuilder.loadTexts:
    h3cLBv2RSConnRecoveryTrap.setStatus(
        "current"
    )

h3cLBv2RSConnsRateOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 15)
)
h3cLBv2RSConnsRateOverloadTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2RSName"),
        ("H3C-LBV2-MIB", "h3cLBv2RSConnectionsRateLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    h3cLBv2RSConnsRateOverloadTrap.setStatus(
        "current"
    )

h3cLBv2RSConnsRateRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 148, 6, 0, 16)
)
h3cLBv2RSConnsRateRecoveryTrap.setObjects(
      *(("H3C-LBV2-MIB", "h3cLBv2RSName"),
        ("H3C-LBV2-MIB", "h3cLBv2RSConnectionsRateLimit"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatChassis"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatSlot"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatCpuid"),
        ("H3C-LBV2-MIB", "h3cLBv2RSStatConnectionsRate"))
)
if mibBuilder.loadTexts:
    h3cLBv2RSConnsRateRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-LBV2-MIB",
    **{"h3cLBv2": h3cLBv2,
       "h3cLBv2GlobalObjects": h3cLBv2GlobalObjects,
       "h3cLBv2TrapEnable": h3cLBv2TrapEnable,
       "h3cLBv2ActionTables": h3cLBv2ActionTables,
       "h3cLBv2ActionTable": h3cLBv2ActionTable,
       "h3cLBv2ActionEntry": h3cLBv2ActionEntry,
       "h3cLBv2ActionName": h3cLBv2ActionName,
       "h3cLBv2ActionDefaultSF": h3cLBv2ActionDefaultSF,
       "h3cLBv2ActionBackupSF": h3cLBv2ActionBackupSF,
       "h3cLBv2ActionInUseSF": h3cLBv2ActionInUseSF,
       "h3cLBv2ActionRowStatus": h3cLBv2ActionRowStatus,
       "h3cLBv2VSTables": h3cLBv2VSTables,
       "h3cLBv2VSTable": h3cLBv2VSTable,
       "h3cLBv2VSEntry": h3cLBv2VSEntry,
       "h3cLBv2VSName": h3cLBv2VSName,
       "h3cLBv2VSConnectionsLimit": h3cLBv2VSConnectionsLimit,
       "h3cLBv2VSConnectionsRateLimit": h3cLBv2VSConnectionsRateLimit,
       "h3cLBv2VSDefaultSF": h3cLBv2VSDefaultSF,
       "h3cLBv2VSBackupSF": h3cLBv2VSBackupSF,
       "h3cLBv2VSInUseSF": h3cLBv2VSInUseSF,
       "h3cLBv2VSRowStatus": h3cLBv2VSRowStatus,
       "h3cLBv2VSStatsTable": h3cLBv2VSStatsTable,
       "h3cLBv2VSStatsEntry": h3cLBv2VSStatsEntry,
       "h3cLBv2VSStatChassis": h3cLBv2VSStatChassis,
       "h3cLBv2VSStatSlot": h3cLBv2VSStatSlot,
       "h3cLBv2VSStatCpuid": h3cLBv2VSStatCpuid,
       "h3cLBv2VSStatTotalConnections": h3cLBv2VSStatTotalConnections,
       "h3cLBv2VSStatActiveConnections": h3cLBv2VSStatActiveConnections,
       "h3cLBv2VSStatClientSidePKTsIn": h3cLBv2VSStatClientSidePKTsIn,
       "h3cLBv2VSStatClientSidePKTsOut": h3cLBv2VSStatClientSidePKTsOut,
       "h3cLBv2VSStatDroppedPackets": h3cLBv2VSStatDroppedPackets,
       "h3cLBv2VSStatClientSideBytesIn": h3cLBv2VSStatClientSideBytesIn,
       "h3cLBv2VSStatClientSideBytesOut": h3cLBv2VSStatClientSideBytesOut,
       "h3cLBv2VSStatReceivedRequests": h3cLBv2VSStatReceivedRequests,
       "h3cLBv2VSStatSentResponses": h3cLBv2VSStatSentResponses,
       "h3cLBv2VSStatConnectionsRate": h3cLBv2VSStatConnectionsRate,
       "h3cLBv2RSTables": h3cLBv2RSTables,
       "h3cLBv2RSTable": h3cLBv2RSTable,
       "h3cLBv2RSEntry": h3cLBv2RSEntry,
       "h3cLBv2RSName": h3cLBv2RSName,
       "h3cLBv2RSRowStatus": h3cLBv2RSRowStatus,
       "h3cLBv2RSConnectionsLimit": h3cLBv2RSConnectionsLimit,
       "h3cLBv2RSConnectionsRateLimit": h3cLBv2RSConnectionsRateLimit,
       "h3cLBv2RSStatsTable": h3cLBv2RSStatsTable,
       "h3cLBv2RSStatsEntry": h3cLBv2RSStatsEntry,
       "h3cLBv2RSStatChassis": h3cLBv2RSStatChassis,
       "h3cLBv2RSStatSlot": h3cLBv2RSStatSlot,
       "h3cLBv2RSStatCpuid": h3cLBv2RSStatCpuid,
       "h3cLBv2RSStatTotalConnections": h3cLBv2RSStatTotalConnections,
       "h3cLBv2RSStatActiveConnections": h3cLBv2RSStatActiveConnections,
       "h3cLBv2RSStatServerSidePKTsIn": h3cLBv2RSStatServerSidePKTsIn,
       "h3cLBv2RSStatServerSidePKTsOut": h3cLBv2RSStatServerSidePKTsOut,
       "h3cLBv2RSStatDroppedPackets": h3cLBv2RSStatDroppedPackets,
       "h3cLBv2RSStatServerSideBytesIn": h3cLBv2RSStatServerSideBytesIn,
       "h3cLBv2RSStatServerSideBytesOut": h3cLBv2RSStatServerSideBytesOut,
       "h3cLBv2RSStatReceivedRequests": h3cLBv2RSStatReceivedRequests,
       "h3cLBv2RSStatSentResponses": h3cLBv2RSStatSentResponses,
       "h3cLBv2RSStatConnectionsRate": h3cLBv2RSStatConnectionsRate,
       "h3cLBv2SFTables": h3cLBv2SFTables,
       "h3cLBv2SFTable": h3cLBv2SFTable,
       "h3cLBv2SFEntry": h3cLBv2SFEntry,
       "h3cLBv2SFName": h3cLBv2SFName,
       "h3cLBv2SFRowStatus": h3cLBv2SFRowStatus,
       "h3cLBv2SFStatsTable": h3cLBv2SFStatsTable,
       "h3cLBv2SFStatsEntry": h3cLBv2SFStatsEntry,
       "h3cLBv2SFStatChassis": h3cLBv2SFStatChassis,
       "h3cLBv2SFStatSlot": h3cLBv2SFStatSlot,
       "h3cLBv2SFStatCpuid": h3cLBv2SFStatCpuid,
       "h3cLBv2SFStatTotalConnections": h3cLBv2SFStatTotalConnections,
       "h3cLBv2SFStatActiveConnections": h3cLBv2SFStatActiveConnections,
       "h3cLBv2SFStatServerSidePKTsIn": h3cLBv2SFStatServerSidePKTsIn,
       "h3cLBv2SFStatServerSidePKTsOut": h3cLBv2SFStatServerSidePKTsOut,
       "h3cLBv2SFStatDroppedPackets": h3cLBv2SFStatDroppedPackets,
       "h3cLBv2SFStatServerSideBytesIn": h3cLBv2SFStatServerSideBytesIn,
       "h3cLBv2SFStatServerSideBytesOut": h3cLBv2SFStatServerSideBytesOut,
       "h3cLBv2SFStatReceivedRequests": h3cLBv2SFStatReceivedRequests,
       "h3cLBv2SFStatSentResponses": h3cLBv2SFStatSentResponses,
       "h3cLBv2Trap": h3cLBv2Trap,
       "h3cLBv2TrapPrefix": h3cLBv2TrapPrefix,
       "h3cLBv2VSConnOverloadTrap": h3cLBv2VSConnOverloadTrap,
       "h3cLBv2VSConnRecoveryTrap": h3cLBv2VSConnRecoveryTrap,
       "h3cLBv2VSConnsRateOverloadTrap": h3cLBv2VSConnsRateOverloadTrap,
       "h3cLBv2VSConnsRateRecoveryTrap": h3cLBv2VSConnsRateRecoveryTrap,
       "h3cLBv2VSActiveTrap": h3cLBv2VSActiveTrap,
       "h3cLBv2VSInactiveTrap": h3cLBv2VSInactiveTrap,
       "h3cLBv2RSAvailableTrap": h3cLBv2RSAvailableTrap,
       "h3cLBv2RSUnavailableTrap": h3cLBv2RSUnavailableTrap,
       "h3cLBv2SFActiveTrap": h3cLBv2SFActiveTrap,
       "h3cLBv2SFInactiveTrap": h3cLBv2SFInactiveTrap,
       "h3cLBv2ActionInUseSFChangeTrap": h3cLBv2ActionInUseSFChangeTrap,
       "h3cLBv2VSInUseSFChangeTrap": h3cLBv2VSInUseSFChangeTrap,
       "h3cLBv2RSConnOverloadTrap": h3cLBv2RSConnOverloadTrap,
       "h3cLBv2RSConnRecoveryTrap": h3cLBv2RSConnRecoveryTrap,
       "h3cLBv2RSConnsRateOverloadTrap": h3cLBv2RSConnsRateOverloadTrap,
       "h3cLBv2RSConnsRateRecoveryTrap": h3cLBv2RSConnsRateRecoveryTrap}
)
