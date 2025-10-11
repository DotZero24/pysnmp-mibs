# SNMP MIB module (ADTRAN-GENATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENATM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:12 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenAtm,
 adGenAtmID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenAtm",
    "adGenAtmID")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenAtmIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 48, 1)
)
if mibBuilder.loadTexts:
    adGenAtmIdentity.setRevisions(
        ("2011-12-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenAtmStatus_ObjectIdentity = ObjectIdentity
adGenAtmStatus = _AdGenAtmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1)
)
_AdGenAtmTotalCountStatusTable_Object = MibTable
adGenAtmTotalCountStatusTable = _AdGenAtmTotalCountStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1)
)
if mibBuilder.loadTexts:
    adGenAtmTotalCountStatusTable.setStatus("current")
_AdGenAtmTotalCountStatusEntry_Object = MibTableRow
adGenAtmTotalCountStatusEntry = _AdGenAtmTotalCountStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1)
)
adGenAtmTotalCountStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenAtmTotalCountStatusEntry.setStatus("current")
_AdGenAtmTotalCountVcl_Type = Integer32
_AdGenAtmTotalCountVcl_Object = MibTableColumn
adGenAtmTotalCountVcl = _AdGenAtmTotalCountVcl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1, 1),
    _AdGenAtmTotalCountVcl_Type()
)
adGenAtmTotalCountVcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmTotalCountVcl.setStatus("current")
_AdGenAtmTotalCountVpl_Type = Integer32
_AdGenAtmTotalCountVpl_Object = MibTableColumn
adGenAtmTotalCountVpl = _AdGenAtmTotalCountVpl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1, 2),
    _AdGenAtmTotalCountVpl_Type()
)
adGenAtmTotalCountVpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmTotalCountVpl.setStatus("current")
_AdGenAtmTotalCountVccc_Type = Integer32
_AdGenAtmTotalCountVccc_Object = MibTableColumn
adGenAtmTotalCountVccc = _AdGenAtmTotalCountVccc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1, 3),
    _AdGenAtmTotalCountVccc_Type()
)
adGenAtmTotalCountVccc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmTotalCountVccc.setStatus("current")
_AdGenAtmTotalCountVpcc_Type = Integer32
_AdGenAtmTotalCountVpcc_Object = MibTableColumn
adGenAtmTotalCountVpcc = _AdGenAtmTotalCountVpcc_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1, 4),
    _AdGenAtmTotalCountVpcc_Type()
)
adGenAtmTotalCountVpcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmTotalCountVpcc.setStatus("current")
_AdGenAtmTotalCountVcIntwk_Type = Integer32
_AdGenAtmTotalCountVcIntwk_Object = MibTableColumn
adGenAtmTotalCountVcIntwk = _AdGenAtmTotalCountVcIntwk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1, 5),
    _AdGenAtmTotalCountVcIntwk_Type()
)
adGenAtmTotalCountVcIntwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmTotalCountVcIntwk.setStatus("current")
_AdGenAtmTotalCountVpIntwk_Type = Integer32
_AdGenAtmTotalCountVpIntwk_Object = MibTableColumn
adGenAtmTotalCountVpIntwk = _AdGenAtmTotalCountVpIntwk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 1, 1, 1, 6),
    _AdGenAtmTotalCountVpIntwk_Type()
)
adGenAtmTotalCountVpIntwk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmTotalCountVpIntwk.setStatus("current")
_AdGenAtmBulkATM_ObjectIdentity = ObjectIdentity
adGenAtmBulkATM = _AdGenAtmBulkATM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2)
)
_AdGenAtmReserveInstanceBulkATMSlotTable_Object = MibTable
adGenAtmReserveInstanceBulkATMSlotTable = _AdGenAtmReserveInstanceBulkATMSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAtmReserveInstanceBulkATMSlotTable.setStatus("current")
_AdGenAtmReserveInstanceBulkATMSlotEntry_Object = MibTableRow
adGenAtmReserveInstanceBulkATMSlotEntry = _AdGenAtmReserveInstanceBulkATMSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 1, 1)
)
adGenAtmReserveInstanceBulkATMSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenAtmReserveInstanceBulkATMSlotEntry.setStatus("current")
_AdGenAtmReserveInstanceBulkATMSlotInstance_Type = Integer32
_AdGenAtmReserveInstanceBulkATMSlotInstance_Object = MibTableColumn
adGenAtmReserveInstanceBulkATMSlotInstance = _AdGenAtmReserveInstanceBulkATMSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 1, 1, 1),
    _AdGenAtmReserveInstanceBulkATMSlotInstance_Type()
)
adGenAtmReserveInstanceBulkATMSlotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAtmReserveInstanceBulkATMSlotInstance.setStatus("current")
_AdGenAtmBulkATMFilterTable_Object = MibTable
adGenAtmBulkATMFilterTable = _AdGenAtmBulkATMFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2)
)
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterTable.setStatus("current")
_AdGenAtmBulkATMFilterEntry_Object = MibTableRow
adGenAtmBulkATMFilterEntry = _AdGenAtmBulkATMFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1)
)
adGenAtmBulkATMFilterEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENATM-MIB", "adGenAtmBulkATMFilterInstance"),
)
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterEntry.setStatus("current")
_AdGenAtmBulkATMFilterInstance_Type = Integer32
_AdGenAtmBulkATMFilterInstance_Object = MibTableColumn
adGenAtmBulkATMFilterInstance = _AdGenAtmBulkATMFilterInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 1),
    _AdGenAtmBulkATMFilterInstance_Type()
)
adGenAtmBulkATMFilterInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterInstance.setStatus("current")


class _AdGenAtmBulkATMFilterType_Type(Integer32):
    """Custom type adGenAtmBulkATMFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notspecified", 0),
          ("vccc", 1),
          ("vpcc", 2),
          ("vcl", 3),
          ("vpl", 4),
          ("vpintwk", 5),
          ("vcintwk", 6))
    )


_AdGenAtmBulkATMFilterType_Type.__name__ = "Integer32"
_AdGenAtmBulkATMFilterType_Object = MibTableColumn
adGenAtmBulkATMFilterType = _AdGenAtmBulkATMFilterType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 2),
    _AdGenAtmBulkATMFilterType_Type()
)
adGenAtmBulkATMFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterType.setStatus("current")
_AdGenAtmBulkATMFilterSlot1_Type = Unsigned32
_AdGenAtmBulkATMFilterSlot1_Object = MibTableColumn
adGenAtmBulkATMFilterSlot1 = _AdGenAtmBulkATMFilterSlot1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 3),
    _AdGenAtmBulkATMFilterSlot1_Type()
)
adGenAtmBulkATMFilterSlot1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterSlot1.setStatus("current")
_AdGenAtmBulkATMFilterPort1_Type = Unsigned32
_AdGenAtmBulkATMFilterPort1_Object = MibTableColumn
adGenAtmBulkATMFilterPort1 = _AdGenAtmBulkATMFilterPort1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 4),
    _AdGenAtmBulkATMFilterPort1_Type()
)
adGenAtmBulkATMFilterPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterPort1.setStatus("current")
_AdGenAtmBulkATMFilterVpi1_Type = Unsigned32
_AdGenAtmBulkATMFilterVpi1_Object = MibTableColumn
adGenAtmBulkATMFilterVpi1 = _AdGenAtmBulkATMFilterVpi1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 5),
    _AdGenAtmBulkATMFilterVpi1_Type()
)
adGenAtmBulkATMFilterVpi1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterVpi1.setStatus("current")
_AdGenAtmBulkATMFilterVci1_Type = Unsigned32
_AdGenAtmBulkATMFilterVci1_Object = MibTableColumn
adGenAtmBulkATMFilterVci1 = _AdGenAtmBulkATMFilterVci1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 6),
    _AdGenAtmBulkATMFilterVci1_Type()
)
adGenAtmBulkATMFilterVci1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterVci1.setStatus("current")
_AdGenAtmBulkATMFilterNode_Type = Unsigned32
_AdGenAtmBulkATMFilterNode_Object = MibTableColumn
adGenAtmBulkATMFilterNode = _AdGenAtmBulkATMFilterNode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 7),
    _AdGenAtmBulkATMFilterNode_Type()
)
adGenAtmBulkATMFilterNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterNode.setStatus("current")
_AdGenAtmBulkATMFilterSlot2_Type = Unsigned32
_AdGenAtmBulkATMFilterSlot2_Object = MibTableColumn
adGenAtmBulkATMFilterSlot2 = _AdGenAtmBulkATMFilterSlot2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 8),
    _AdGenAtmBulkATMFilterSlot2_Type()
)
adGenAtmBulkATMFilterSlot2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterSlot2.setStatus("current")
_AdGenAtmBulkATMFilterPort2_Type = Unsigned32
_AdGenAtmBulkATMFilterPort2_Object = MibTableColumn
adGenAtmBulkATMFilterPort2 = _AdGenAtmBulkATMFilterPort2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 9),
    _AdGenAtmBulkATMFilterPort2_Type()
)
adGenAtmBulkATMFilterPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterPort2.setStatus("current")
_AdGenAtmBulkATMFilterVpi2_Type = Unsigned32
_AdGenAtmBulkATMFilterVpi2_Object = MibTableColumn
adGenAtmBulkATMFilterVpi2 = _AdGenAtmBulkATMFilterVpi2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 10),
    _AdGenAtmBulkATMFilterVpi2_Type()
)
adGenAtmBulkATMFilterVpi2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterVpi2.setStatus("current")
_AdGenAtmBulkATMFilterVci2_Type = Unsigned32
_AdGenAtmBulkATMFilterVci2_Object = MibTableColumn
adGenAtmBulkATMFilterVci2 = _AdGenAtmBulkATMFilterVci2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 11),
    _AdGenAtmBulkATMFilterVci2_Type()
)
adGenAtmBulkATMFilterVci2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterVci2.setStatus("current")
_AdGenAtmBulkATMFilterStag_Type = Unsigned32
_AdGenAtmBulkATMFilterStag_Object = MibTableColumn
adGenAtmBulkATMFilterStag = _AdGenAtmBulkATMFilterStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 12),
    _AdGenAtmBulkATMFilterStag_Type()
)
adGenAtmBulkATMFilterStag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterStag.setStatus("current")
_AdGenAtmBulkATMFilterCtag_Type = Unsigned32
_AdGenAtmBulkATMFilterCtag_Object = MibTableColumn
adGenAtmBulkATMFilterCtag = _AdGenAtmBulkATMFilterCtag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 13),
    _AdGenAtmBulkATMFilterCtag_Type()
)
adGenAtmBulkATMFilterCtag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMFilterCtag.setStatus("current")


class _AdGenAtmBulkATMSlotInstance_Type(Integer32):
    """Custom type adGenAtmBulkATMSlotInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("updateinstance", 1)
    )


_AdGenAtmBulkATMSlotInstance_Type.__name__ = "Integer32"
_AdGenAtmBulkATMSlotInstance_Object = MibTableColumn
adGenAtmBulkATMSlotInstance = _AdGenAtmBulkATMSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 48, 2, 2, 1, 14),
    _AdGenAtmBulkATMSlotInstance_Type()
)
adGenAtmBulkATMSlotInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenAtmBulkATMSlotInstance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENATM-MIB",
    **{"adGenAtmStatus": adGenAtmStatus,
       "adGenAtmTotalCountStatusTable": adGenAtmTotalCountStatusTable,
       "adGenAtmTotalCountStatusEntry": adGenAtmTotalCountStatusEntry,
       "adGenAtmTotalCountVcl": adGenAtmTotalCountVcl,
       "adGenAtmTotalCountVpl": adGenAtmTotalCountVpl,
       "adGenAtmTotalCountVccc": adGenAtmTotalCountVccc,
       "adGenAtmTotalCountVpcc": adGenAtmTotalCountVpcc,
       "adGenAtmTotalCountVcIntwk": adGenAtmTotalCountVcIntwk,
       "adGenAtmTotalCountVpIntwk": adGenAtmTotalCountVpIntwk,
       "adGenAtmBulkATM": adGenAtmBulkATM,
       "adGenAtmReserveInstanceBulkATMSlotTable": adGenAtmReserveInstanceBulkATMSlotTable,
       "adGenAtmReserveInstanceBulkATMSlotEntry": adGenAtmReserveInstanceBulkATMSlotEntry,
       "adGenAtmReserveInstanceBulkATMSlotInstance": adGenAtmReserveInstanceBulkATMSlotInstance,
       "adGenAtmBulkATMFilterTable": adGenAtmBulkATMFilterTable,
       "adGenAtmBulkATMFilterEntry": adGenAtmBulkATMFilterEntry,
       "adGenAtmBulkATMFilterInstance": adGenAtmBulkATMFilterInstance,
       "adGenAtmBulkATMFilterType": adGenAtmBulkATMFilterType,
       "adGenAtmBulkATMFilterSlot1": adGenAtmBulkATMFilterSlot1,
       "adGenAtmBulkATMFilterPort1": adGenAtmBulkATMFilterPort1,
       "adGenAtmBulkATMFilterVpi1": adGenAtmBulkATMFilterVpi1,
       "adGenAtmBulkATMFilterVci1": adGenAtmBulkATMFilterVci1,
       "adGenAtmBulkATMFilterNode": adGenAtmBulkATMFilterNode,
       "adGenAtmBulkATMFilterSlot2": adGenAtmBulkATMFilterSlot2,
       "adGenAtmBulkATMFilterPort2": adGenAtmBulkATMFilterPort2,
       "adGenAtmBulkATMFilterVpi2": adGenAtmBulkATMFilterVpi2,
       "adGenAtmBulkATMFilterVci2": adGenAtmBulkATMFilterVci2,
       "adGenAtmBulkATMFilterStag": adGenAtmBulkATMFilterStag,
       "adGenAtmBulkATMFilterCtag": adGenAtmBulkATMFilterCtag,
       "adGenAtmBulkATMSlotInstance": adGenAtmBulkATMSlotInstance,
       "adGenAtmIdentity": adGenAtmIdentity}
)
