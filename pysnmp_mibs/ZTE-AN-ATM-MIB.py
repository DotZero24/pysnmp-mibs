# SNMP MIB module (ZTE-AN-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ATM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:09 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 experimental,
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
    "experimental",
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

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnAtmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnAtmVcxObjects_ObjectIdentity = ObjectIdentity
zxAnAtmVcxObjects = _ZxAnAtmVcxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1)
)
_ZxAnAtmVcxTable_Object = MibTable
zxAnAtmVcxTable = _ZxAnAtmVcxTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnAtmVcxTable.setStatus("current")
_ZxAnAtmVcxEntry_Object = MibTableRow
zxAnAtmVcxEntry = _ZxAnAtmVcxEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1)
)
zxAnAtmVcxEntry.setIndexNames(
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmVcxUserSideIfIndex"),
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmVcxUserSidePvcId"),
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmVcxWanSideIfIndex"),
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmVcxWanSidePvcId"),
)
if mibBuilder.loadTexts:
    zxAnAtmVcxEntry.setStatus("current")
_ZxAnAtmVcxUserSideIfIndex_Type = ZxAnIfindex
_ZxAnAtmVcxUserSideIfIndex_Object = MibTableColumn
zxAnAtmVcxUserSideIfIndex = _ZxAnAtmVcxUserSideIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 1),
    _ZxAnAtmVcxUserSideIfIndex_Type()
)
zxAnAtmVcxUserSideIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmVcxUserSideIfIndex.setStatus("current")
_ZxAnAtmVcxUserSidePvcId_Type = Integer32
_ZxAnAtmVcxUserSidePvcId_Object = MibTableColumn
zxAnAtmVcxUserSidePvcId = _ZxAnAtmVcxUserSidePvcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 2),
    _ZxAnAtmVcxUserSidePvcId_Type()
)
zxAnAtmVcxUserSidePvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmVcxUserSidePvcId.setStatus("current")
_ZxAnAtmVcxWanSideIfIndex_Type = ZxAnIfindex
_ZxAnAtmVcxWanSideIfIndex_Object = MibTableColumn
zxAnAtmVcxWanSideIfIndex = _ZxAnAtmVcxWanSideIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 3),
    _ZxAnAtmVcxWanSideIfIndex_Type()
)
zxAnAtmVcxWanSideIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmVcxWanSideIfIndex.setStatus("current")
_ZxAnAtmVcxWanSidePvcId_Type = Integer32
_ZxAnAtmVcxWanSidePvcId_Object = MibTableColumn
zxAnAtmVcxWanSidePvcId = _ZxAnAtmVcxWanSidePvcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 4),
    _ZxAnAtmVcxWanSidePvcId_Type()
)
zxAnAtmVcxWanSidePvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmVcxWanSidePvcId.setStatus("current")
_ZxAnAtmVcxUserSideVpi_Type = Integer32
_ZxAnAtmVcxUserSideVpi_Object = MibTableColumn
zxAnAtmVcxUserSideVpi = _ZxAnAtmVcxUserSideVpi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 5),
    _ZxAnAtmVcxUserSideVpi_Type()
)
zxAnAtmVcxUserSideVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmVcxUserSideVpi.setStatus("current")
_ZxAnAtmVcxUserSideVci_Type = Integer32
_ZxAnAtmVcxUserSideVci_Object = MibTableColumn
zxAnAtmVcxUserSideVci = _ZxAnAtmVcxUserSideVci_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 6),
    _ZxAnAtmVcxUserSideVci_Type()
)
zxAnAtmVcxUserSideVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmVcxUserSideVci.setStatus("current")
_ZxAnAtmVcxWanSideVpi_Type = Integer32
_ZxAnAtmVcxWanSideVpi_Object = MibTableColumn
zxAnAtmVcxWanSideVpi = _ZxAnAtmVcxWanSideVpi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 7),
    _ZxAnAtmVcxWanSideVpi_Type()
)
zxAnAtmVcxWanSideVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmVcxWanSideVpi.setStatus("current")
_ZxAnAtmVcxWanSideVci_Type = Integer32
_ZxAnAtmVcxWanSideVci_Object = MibTableColumn
zxAnAtmVcxWanSideVci = _ZxAnAtmVcxWanSideVci_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 8),
    _ZxAnAtmVcxWanSideVci_Type()
)
zxAnAtmVcxWanSideVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmVcxWanSideVci.setStatus("current")


class _ZxAnAtmVcxRowStatus_Type(RowStatus):
    """Custom type zxAnAtmVcxRowStatus based on RowStatus"""
    defaultValue = 5


_ZxAnAtmVcxRowStatus_Type.__name__ = "RowStatus"
_ZxAnAtmVcxRowStatus_Object = MibTableColumn
zxAnAtmVcxRowStatus = _ZxAnAtmVcxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 1, 1, 50),
    _ZxAnAtmVcxRowStatus_Type()
)
zxAnAtmVcxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAtmVcxRowStatus.setStatus("current")
_ZxAnAtmPvcMappingIdTable_Object = MibTable
zxAnAtmPvcMappingIdTable = _ZxAnAtmPvcMappingIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnAtmPvcMappingIdTable.setStatus("current")
_ZxAnAtmPvcMappingIdEntry_Object = MibTableRow
zxAnAtmPvcMappingIdEntry = _ZxAnAtmPvcMappingIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 3, 1)
)
zxAnAtmPvcMappingIdEntry.setIndexNames(
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmIfIndex"),
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmPvcVpi"),
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmPvcVci"),
)
if mibBuilder.loadTexts:
    zxAnAtmPvcMappingIdEntry.setStatus("current")
_ZxAnAtmIfIndex_Type = ZxAnIfindex
_ZxAnAtmIfIndex_Object = MibTableColumn
zxAnAtmIfIndex = _ZxAnAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 3, 1, 1),
    _ZxAnAtmIfIndex_Type()
)
zxAnAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmIfIndex.setStatus("current")


class _ZxAnAtmPvcVpi_Type(Integer32):
    """Custom type zxAnAtmPvcVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnAtmPvcVpi_Type.__name__ = "Integer32"
_ZxAnAtmPvcVpi_Object = MibTableColumn
zxAnAtmPvcVpi = _ZxAnAtmPvcVpi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 3, 1, 2),
    _ZxAnAtmPvcVpi_Type()
)
zxAnAtmPvcVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmPvcVpi.setStatus("current")


class _ZxAnAtmPvcVci_Type(Integer32):
    """Custom type zxAnAtmPvcVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnAtmPvcVci_Type.__name__ = "Integer32"
_ZxAnAtmPvcVci_Object = MibTableColumn
zxAnAtmPvcVci = _ZxAnAtmPvcVci_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 3, 1, 3),
    _ZxAnAtmPvcVci_Type()
)
zxAnAtmPvcVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmPvcVci.setStatus("current")
_ZxAnAtmPvcId_Type = Integer32
_ZxAnAtmPvcId_Object = MibTableColumn
zxAnAtmPvcId = _ZxAnAtmPvcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 1, 3, 1, 4),
    _ZxAnAtmPvcId_Type()
)
zxAnAtmPvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAtmPvcId.setStatus("current")
_ZxAnAtmPerfObjects_ObjectIdentity = ObjectIdentity
zxAnAtmPerfObjects = _ZxAnAtmPerfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2)
)
_ZxAnAtmPerfTable_Object = MibTable
zxAnAtmPerfTable = _ZxAnAtmPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnAtmPerfTable.setStatus("current")
_ZxAnAtmPerfEntry_Object = MibTableRow
zxAnAtmPerfEntry = _ZxAnAtmPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1)
)
zxAnAtmPerfEntry.setIndexNames(
    (0, "ZTE-AN-ATM-MIB", "zxAnAtmPerfIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnAtmPerfEntry.setStatus("current")
_ZxAnAtmPerfIfIndex_Type = ZxAnIfindex
_ZxAnAtmPerfIfIndex_Object = MibTableColumn
zxAnAtmPerfIfIndex = _ZxAnAtmPerfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1, 1),
    _ZxAnAtmPerfIfIndex_Type()
)
zxAnAtmPerfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnAtmPerfIfIndex.setStatus("current")
_ZxAnAtmReceiveCell_Type = Counter64
_ZxAnAtmReceiveCell_Object = MibTableColumn
zxAnAtmReceiveCell = _ZxAnAtmReceiveCell_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1, 2),
    _ZxAnAtmReceiveCell_Type()
)
zxAnAtmReceiveCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmReceiveCell.setStatus("current")
_ZxAnAtmTransmitCell_Type = Counter64
_ZxAnAtmTransmitCell_Object = MibTableColumn
zxAnAtmTransmitCell = _ZxAnAtmTransmitCell_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1, 3),
    _ZxAnAtmTransmitCell_Type()
)
zxAnAtmTransmitCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmTransmitCell.setStatus("current")
_ZxAnAtmDiscardedCell_Type = Counter64
_ZxAnAtmDiscardedCell_Object = MibTableColumn
zxAnAtmDiscardedCell = _ZxAnAtmDiscardedCell_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1, 4),
    _ZxAnAtmDiscardedCell_Type()
)
zxAnAtmDiscardedCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmDiscardedCell.setStatus("current")
_ZxAnAtmContinuityCell_Type = Counter64
_ZxAnAtmContinuityCell_Object = MibTableColumn
zxAnAtmContinuityCell = _ZxAnAtmContinuityCell_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1, 5),
    _ZxAnAtmContinuityCell_Type()
)
zxAnAtmContinuityCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnAtmContinuityCell.setStatus("current")


class _ZxATMStatCounterAdminStatus_Type(Integer32):
    """Custom type zxATMStatCounterAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2),
          ("resetCounter", 3))
    )


_ZxATMStatCounterAdminStatus_Type.__name__ = "Integer32"
_ZxATMStatCounterAdminStatus_Object = MibTableColumn
zxATMStatCounterAdminStatus = _ZxATMStatCounterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 57, 2, 1, 1, 6),
    _ZxATMStatCounterAdminStatus_Type()
)
zxATMStatCounterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxATMStatCounterAdminStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ATM-MIB",
    **{"zxAnAtmMib": zxAnAtmMib,
       "zxAnAtmVcxObjects": zxAnAtmVcxObjects,
       "zxAnAtmVcxTable": zxAnAtmVcxTable,
       "zxAnAtmVcxEntry": zxAnAtmVcxEntry,
       "zxAnAtmVcxUserSideIfIndex": zxAnAtmVcxUserSideIfIndex,
       "zxAnAtmVcxUserSidePvcId": zxAnAtmVcxUserSidePvcId,
       "zxAnAtmVcxWanSideIfIndex": zxAnAtmVcxWanSideIfIndex,
       "zxAnAtmVcxWanSidePvcId": zxAnAtmVcxWanSidePvcId,
       "zxAnAtmVcxUserSideVpi": zxAnAtmVcxUserSideVpi,
       "zxAnAtmVcxUserSideVci": zxAnAtmVcxUserSideVci,
       "zxAnAtmVcxWanSideVpi": zxAnAtmVcxWanSideVpi,
       "zxAnAtmVcxWanSideVci": zxAnAtmVcxWanSideVci,
       "zxAnAtmVcxRowStatus": zxAnAtmVcxRowStatus,
       "zxAnAtmPvcMappingIdTable": zxAnAtmPvcMappingIdTable,
       "zxAnAtmPvcMappingIdEntry": zxAnAtmPvcMappingIdEntry,
       "zxAnAtmIfIndex": zxAnAtmIfIndex,
       "zxAnAtmPvcVpi": zxAnAtmPvcVpi,
       "zxAnAtmPvcVci": zxAnAtmPvcVci,
       "zxAnAtmPvcId": zxAnAtmPvcId,
       "zxAnAtmPerfObjects": zxAnAtmPerfObjects,
       "zxAnAtmPerfTable": zxAnAtmPerfTable,
       "zxAnAtmPerfEntry": zxAnAtmPerfEntry,
       "zxAnAtmPerfIfIndex": zxAnAtmPerfIfIndex,
       "zxAnAtmReceiveCell": zxAnAtmReceiveCell,
       "zxAnAtmTransmitCell": zxAnAtmTransmitCell,
       "zxAnAtmDiscardedCell": zxAnAtmDiscardedCell,
       "zxAnAtmContinuityCell": zxAnAtmContinuityCell,
       "zxATMStatCounterAdminStatus": zxATMStatCounterAdminStatus}
)
