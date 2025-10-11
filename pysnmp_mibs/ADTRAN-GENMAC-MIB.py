# SNMP MIB module (ADTRAN-GENMAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:26 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenMac,
 adGenMacID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMac",
    "adGenMacID")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenMacIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 8, 1)
)
if mibBuilder.loadTexts:
    adGenMacIdentity.setRevisions(
        ("2008-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMacEvents_ObjectIdentity = ObjectIdentity
adGenMacEvents = _AdGenMacEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 0)
)
_AdGenMacProvisioning_ObjectIdentity = ObjectIdentity
adGenMacProvisioning = _AdGenMacProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1)
)
_AdGenMacProvTable_Object = MibTable
adGenMacProvTable = _AdGenMacProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMacProvTable.setStatus("current")
_AdGenMacProvEntry_Object = MibTableRow
adGenMacProvEntry = _AdGenMacProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 1, 1)
)
adGenMacProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacProvEntry.setStatus("current")
_AdGenMacProvLimit_Type = Integer32
_AdGenMacProvLimit_Object = MibTableColumn
adGenMacProvLimit = _AdGenMacProvLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 1, 1, 1),
    _AdGenMacProvLimit_Type()
)
adGenMacProvLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacProvLimit.setStatus("current")
_AdGenMacProvAgingTime_Type = Integer32
_AdGenMacProvAgingTime_Object = MibTableColumn
adGenMacProvAgingTime = _AdGenMacProvAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 1, 1, 2),
    _AdGenMacProvAgingTime_Type()
)
adGenMacProvAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacProvAgingTime.setStatus("current")
_AdGenClearMACAddressSlotTable_Object = MibTable
adGenClearMACAddressSlotTable = _AdGenClearMACAddressSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 2)
)
if mibBuilder.loadTexts:
    adGenClearMACAddressSlotTable.setStatus("current")
_AdGenClearMACAddressSlotEntry_Object = MibTableRow
adGenClearMACAddressSlotEntry = _AdGenClearMACAddressSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 2, 1)
)
adGenClearMACAddressSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenClearMACAddressSlotEntry.setStatus("current")
_AdGenClearSingleMAC_Type = MacAddress
_AdGenClearSingleMAC_Object = MibTableColumn
adGenClearSingleMAC = _AdGenClearSingleMAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 2, 1, 1),
    _AdGenClearSingleMAC_Type()
)
adGenClearSingleMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenClearSingleMAC.setStatus("current")


class _AdGenClearAllDynamicMAC_Type(Integer32):
    """Custom type adGenClearAllDynamicMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenClearAllDynamicMAC_Type.__name__ = "Integer32"
_AdGenClearAllDynamicMAC_Object = MibTableColumn
adGenClearAllDynamicMAC = _AdGenClearAllDynamicMAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 2, 1, 2),
    _AdGenClearAllDynamicMAC_Type()
)
adGenClearAllDynamicMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenClearAllDynamicMAC.setStatus("current")
_AdGenClearMACAddressTable_Object = MibTable
adGenClearMACAddressTable = _AdGenClearMACAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 3)
)
if mibBuilder.loadTexts:
    adGenClearMACAddressTable.setStatus("current")
_AdGenClearMACAddressEntry_Object = MibTableRow
adGenClearMACAddressEntry = _AdGenClearMACAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 3, 1)
)
adGenClearMACAddressEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMAC-MIB", "adGenClearMACAddressStag"),
    (0, "ADTRAN-GENMAC-MIB", "adGenClearMACAddressStatus"),
)
if mibBuilder.loadTexts:
    adGenClearMACAddressEntry.setStatus("current")


class _AdGenClearMACAddressStag_Type(Integer32):
    """Custom type adGenClearMACAddressStag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AdGenClearMACAddressStag_Type.__name__ = "Integer32"
_AdGenClearMACAddressStag_Object = MibTableColumn
adGenClearMACAddressStag = _AdGenClearMACAddressStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 3, 1, 1),
    _AdGenClearMACAddressStag_Type()
)
adGenClearMACAddressStag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenClearMACAddressStag.setStatus("current")


class _AdGenClearMACAddressStatus_Type(Integer32):
    """Custom type adGenClearMACAddressStatus based on Integer32"""
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
        *(("all", 0),
          ("static", 1),
          ("dynamic", 2),
          ("multicast", 3))
    )


_AdGenClearMACAddressStatus_Type.__name__ = "Integer32"
_AdGenClearMACAddressStatus_Object = MibTableColumn
adGenClearMACAddressStatus = _AdGenClearMACAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 3, 1, 2),
    _AdGenClearMACAddressStatus_Type()
)
adGenClearMACAddressStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenClearMACAddressStatus.setStatus("current")


class _AdGenClearMACAddressClear_Type(Integer32):
    """Custom type adGenClearMACAddressClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenClearMACAddressClear_Type.__name__ = "Integer32"
_AdGenClearMACAddressClear_Object = MibTableColumn
adGenClearMACAddressClear = _AdGenClearMACAddressClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 3, 1, 3),
    _AdGenClearMACAddressClear_Type()
)
adGenClearMACAddressClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenClearMACAddressClear.setStatus("current")
_AdGenClearMACAddressInterfaceIDTable_Object = MibTable
adGenClearMACAddressInterfaceIDTable = _AdGenClearMACAddressInterfaceIDTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 4)
)
if mibBuilder.loadTexts:
    adGenClearMACAddressInterfaceIDTable.setStatus("current")
_AdGenClearMACAddressInterfaceIDEntry_Object = MibTableRow
adGenClearMACAddressInterfaceIDEntry = _AdGenClearMACAddressInterfaceIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 4, 1)
)
adGenClearMACAddressInterfaceIDEntry.setIndexNames(
    (0, "ADTRAN-GENMAC-MIB", "adGenClearMACAddressInterfaceID"),
)
if mibBuilder.loadTexts:
    adGenClearMACAddressInterfaceIDEntry.setStatus("current")
_AdGenClearMACAddressInterfaceID_Type = InterfaceIndexOrZero
_AdGenClearMACAddressInterfaceID_Object = MibTableColumn
adGenClearMACAddressInterfaceID = _AdGenClearMACAddressInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 4, 1, 1),
    _AdGenClearMACAddressInterfaceID_Type()
)
adGenClearMACAddressInterfaceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenClearMACAddressInterfaceID.setStatus("current")


class _AdGenClearMACAddressInterfaceIDClear_Type(Integer32):
    """Custom type adGenClearMACAddressInterfaceIDClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGenClearMACAddressInterfaceIDClear_Type.__name__ = "Integer32"
_AdGenClearMACAddressInterfaceIDClear_Object = MibTableColumn
adGenClearMACAddressInterfaceIDClear = _AdGenClearMACAddressInterfaceIDClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 1, 4, 1, 2),
    _AdGenClearMACAddressInterfaceIDClear_Type()
)
adGenClearMACAddressInterfaceIDClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenClearMACAddressInterfaceIDClear.setStatus("current")
_AdGenMacStatus_ObjectIdentity = ObjectIdentity
adGenMacStatus = _AdGenMacStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2)
)
_AdGenMacStatusTable_Object = MibTable
adGenMacStatusTable = _AdGenMacStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 1)
)
if mibBuilder.loadTexts:
    adGenMacStatusTable.setStatus("current")
_AdGenMacStatusEntry_Object = MibTableRow
adGenMacStatusEntry = _AdGenMacStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 1, 1)
)
adGenMacStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacStatusEntry.setStatus("current")
_AdGenMacStatusNumEntries_Type = Unsigned32
_AdGenMacStatusNumEntries_Object = MibTableColumn
adGenMacStatusNumEntries = _AdGenMacStatusNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 1, 1, 1),
    _AdGenMacStatusNumEntries_Type()
)
adGenMacStatusNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacStatusNumEntries.setStatus("current")
_AdGenMacStatusMaxLimit_Type = Unsigned32
_AdGenMacStatusMaxLimit_Object = MibTableColumn
adGenMacStatusMaxLimit = _AdGenMacStatusMaxLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 1, 1, 2),
    _AdGenMacStatusMaxLimit_Type()
)
adGenMacStatusMaxLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacStatusMaxLimit.setStatus("current")
_AdGenMacStatusMinAgingTime_Type = Unsigned32
_AdGenMacStatusMinAgingTime_Object = MibTableColumn
adGenMacStatusMinAgingTime = _AdGenMacStatusMinAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 1, 1, 3),
    _AdGenMacStatusMinAgingTime_Type()
)
adGenMacStatusMinAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacStatusMinAgingTime.setStatus("current")
_AdGenMacStatusMaxAgingTime_Type = Unsigned32
_AdGenMacStatusMaxAgingTime_Object = MibTableColumn
adGenMacStatusMaxAgingTime = _AdGenMacStatusMaxAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 1, 1, 4),
    _AdGenMacStatusMaxAgingTime_Type()
)
adGenMacStatusMaxAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacStatusMaxAgingTime.setStatus("current")
_AdGenMacCountsTable_Object = MibTable
adGenMacCountsTable = _AdGenMacCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 2)
)
if mibBuilder.loadTexts:
    adGenMacCountsTable.setStatus("current")
_AdGenMacCountsEntry_Object = MibTableRow
adGenMacCountsEntry = _AdGenMacCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 2, 1)
)
adGenMacCountsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacCountsEntry.setStatus("current")
_AdGenMacCounts5MinAvgEntries_Type = Gauge32
_AdGenMacCounts5MinAvgEntries_Object = MibTableColumn
adGenMacCounts5MinAvgEntries = _AdGenMacCounts5MinAvgEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 2, 1, 1),
    _AdGenMacCounts5MinAvgEntries_Type()
)
adGenMacCounts5MinAvgEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacCounts5MinAvgEntries.setStatus("current")
_AdGenMacLookUpTable_Object = MibTable
adGenMacLookUpTable = _AdGenMacLookUpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 3)
)
if mibBuilder.loadTexts:
    adGenMacLookUpTable.setStatus("current")
_AdGenMacLookUpEntry_Object = MibTableRow
adGenMacLookUpEntry = _AdGenMacLookUpEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 3, 1)
)
adGenMacLookUpEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMAC-MIB", "adGenMacLookUpVlanIndex"),
    (0, "ADTRAN-GENMAC-MIB", "adGenMacLookUpMacIndex"),
)
if mibBuilder.loadTexts:
    adGenMacLookUpEntry.setStatus("current")
_AdGenMacLookUpVlanIndex_Type = VlanIdOrNone
_AdGenMacLookUpVlanIndex_Object = MibTableColumn
adGenMacLookUpVlanIndex = _AdGenMacLookUpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 3, 1, 1),
    _AdGenMacLookUpVlanIndex_Type()
)
adGenMacLookUpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMacLookUpVlanIndex.setStatus("current")
_AdGenMacLookUpMacIndex_Type = MacAddress
_AdGenMacLookUpMacIndex_Object = MibTableColumn
adGenMacLookUpMacIndex = _AdGenMacLookUpMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 3, 1, 2),
    _AdGenMacLookUpMacIndex_Type()
)
adGenMacLookUpMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMacLookUpMacIndex.setStatus("current")
_AdGenMacLookUp_Type = InterfaceIndexOrZero
_AdGenMacLookUp_Object = MibTableColumn
adGenMacLookUp = _AdGenMacLookUp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 2, 3, 1, 3),
    _AdGenMacLookUp_Type()
)
adGenMacLookUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacLookUp.setStatus("current")
_AdGenMacPerformance_ObjectIdentity = ObjectIdentity
adGenMacPerformance = _AdGenMacPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3)
)
_AdGenMacThresh15MinTable_Object = MibTable
adGenMacThresh15MinTable = _AdGenMacThresh15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 1)
)
if mibBuilder.loadTexts:
    adGenMacThresh15MinTable.setStatus("current")
_AdGenMacThresh15MinEntry_Object = MibTableRow
adGenMacThresh15MinEntry = _AdGenMacThresh15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 1, 1)
)
adGenMacThresh15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacThresh15MinEntry.setStatus("current")
_AdGenMacThresh15MinMaxEntries_Type = Unsigned32
_AdGenMacThresh15MinMaxEntries_Object = MibTableColumn
adGenMacThresh15MinMaxEntries = _AdGenMacThresh15MinMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 1, 1, 1),
    _AdGenMacThresh15MinMaxEntries_Type()
)
adGenMacThresh15MinMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacThresh15MinMaxEntries.setStatus("current")
_AdGenMacThresh24HrTable_Object = MibTable
adGenMacThresh24HrTable = _AdGenMacThresh24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 2)
)
if mibBuilder.loadTexts:
    adGenMacThresh24HrTable.setStatus("current")
_AdGenMacThresh24HrEntry_Object = MibTableRow
adGenMacThresh24HrEntry = _AdGenMacThresh24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 2, 1)
)
adGenMacThresh24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacThresh24HrEntry.setStatus("current")
_AdGenMacThresh24HrMaxEntries_Type = Unsigned32
_AdGenMacThresh24HrMaxEntries_Object = MibTableColumn
adGenMacThresh24HrMaxEntries = _AdGenMacThresh24HrMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 2, 1, 1),
    _AdGenMacThresh24HrMaxEntries_Type()
)
adGenMacThresh24HrMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacThresh24HrMaxEntries.setStatus("current")
_AdGenMacPerf15MinTable_Object = MibTable
adGenMacPerf15MinTable = _AdGenMacPerf15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 3)
)
if mibBuilder.loadTexts:
    adGenMacPerf15MinTable.setStatus("current")
_AdGenMacPerf15MinEntry_Object = MibTableRow
adGenMacPerf15MinEntry = _AdGenMacPerf15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 3, 1)
)
adGenMacPerf15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacPerf15MinEntry.setStatus("current")
_AdGenMacPerf15MinMaxEntries_Type = Gauge32
_AdGenMacPerf15MinMaxEntries_Object = MibTableColumn
adGenMacPerf15MinMaxEntries = _AdGenMacPerf15MinMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 3, 1, 1),
    _AdGenMacPerf15MinMaxEntries_Type()
)
adGenMacPerf15MinMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacPerf15MinMaxEntries.setStatus("current")
_AdGenMacPerf15MinIntTable_Object = MibTable
adGenMacPerf15MinIntTable = _AdGenMacPerf15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 4)
)
if mibBuilder.loadTexts:
    adGenMacPerf15MinIntTable.setStatus("current")
_AdGenMacPerf15MinIntEntry_Object = MibTableRow
adGenMacPerf15MinIntEntry = _AdGenMacPerf15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 4, 1)
)
adGenMacPerf15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMAC-MIB", "adGenMacPerf15MinIntNum"),
)
if mibBuilder.loadTexts:
    adGenMacPerf15MinIntEntry.setStatus("current")
_AdGenMacPerf15MinIntNum_Type = Gauge32
_AdGenMacPerf15MinIntNum_Object = MibTableColumn
adGenMacPerf15MinIntNum = _AdGenMacPerf15MinIntNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 4, 1, 1),
    _AdGenMacPerf15MinIntNum_Type()
)
adGenMacPerf15MinIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacPerf15MinIntNum.setStatus("current")
_AdGenMacPerf15MinIntMaxEntries_Type = Gauge32
_AdGenMacPerf15MinIntMaxEntries_Object = MibTableColumn
adGenMacPerf15MinIntMaxEntries = _AdGenMacPerf15MinIntMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 4, 1, 2),
    _AdGenMacPerf15MinIntMaxEntries_Type()
)
adGenMacPerf15MinIntMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacPerf15MinIntMaxEntries.setStatus("current")
_AdGenMacPerf24HrTable_Object = MibTable
adGenMacPerf24HrTable = _AdGenMacPerf24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 5)
)
if mibBuilder.loadTexts:
    adGenMacPerf24HrTable.setStatus("current")
_AdGenMacPerf24HrEntry_Object = MibTableRow
adGenMacPerf24HrEntry = _AdGenMacPerf24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 5, 1)
)
adGenMacPerf24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMacPerf24HrEntry.setStatus("current")
_AdGenMacPerf24HrMaxEntries_Type = Gauge32
_AdGenMacPerf24HrMaxEntries_Object = MibTableColumn
adGenMacPerf24HrMaxEntries = _AdGenMacPerf24HrMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 5, 1, 1),
    _AdGenMacPerf24HrMaxEntries_Type()
)
adGenMacPerf24HrMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacPerf24HrMaxEntries.setStatus("current")
_AdGenMacPerf24HrIntTable_Object = MibTable
adGenMacPerf24HrIntTable = _AdGenMacPerf24HrIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 6)
)
if mibBuilder.loadTexts:
    adGenMacPerf24HrIntTable.setStatus("current")
_AdGenMacPerf24HrIntEntry_Object = MibTableRow
adGenMacPerf24HrIntEntry = _AdGenMacPerf24HrIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 6, 1)
)
adGenMacPerf24HrIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMAC-MIB", "adGenMacPerf24HrIntNum"),
)
if mibBuilder.loadTexts:
    adGenMacPerf24HrIntEntry.setStatus("current")
_AdGenMacPerf24HrIntNum_Type = Gauge32
_AdGenMacPerf24HrIntNum_Object = MibTableColumn
adGenMacPerf24HrIntNum = _AdGenMacPerf24HrIntNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 6, 1, 1),
    _AdGenMacPerf24HrIntNum_Type()
)
adGenMacPerf24HrIntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacPerf24HrIntNum.setStatus("current")
_AdGenMacPerf24HrIntMaxEntries_Type = Gauge32
_AdGenMacPerf24HrIntMaxEntries_Object = MibTableColumn
adGenMacPerf24HrIntMaxEntries = _AdGenMacPerf24HrIntMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 3, 6, 1, 2),
    _AdGenMacPerf24HrIntMaxEntries_Type()
)
adGenMacPerf24HrIntMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacPerf24HrIntMaxEntries.setStatus("current")
_AdGenMacBulkMAC_ObjectIdentity = ObjectIdentity
adGenMacBulkMAC = _AdGenMacBulkMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4)
)
_AdGenMacReserveInstanceBulkMACSlotTable_Object = MibTable
adGenMacReserveInstanceBulkMACSlotTable = _AdGenMacReserveInstanceBulkMACSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 1)
)
if mibBuilder.loadTexts:
    adGenMacReserveInstanceBulkMACSlotTable.setStatus("current")
_AdGenMacReserveInstanceBulkMACSlotEntry_Object = MibTableRow
adGenMacReserveInstanceBulkMACSlotEntry = _AdGenMacReserveInstanceBulkMACSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 1, 1)
)
adGenMacReserveInstanceBulkMACSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMacReserveInstanceBulkMACSlotEntry.setStatus("current")
_AdGenMacReserveInstanceBulkMACSlotInstance_Type = Integer32
_AdGenMacReserveInstanceBulkMACSlotInstance_Object = MibTableColumn
adGenMacReserveInstanceBulkMACSlotInstance = _AdGenMacReserveInstanceBulkMACSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 1, 1, 1),
    _AdGenMacReserveInstanceBulkMACSlotInstance_Type()
)
adGenMacReserveInstanceBulkMACSlotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMacReserveInstanceBulkMACSlotInstance.setStatus("current")
_AdGenMacBulkMACFilterTable_Object = MibTable
adGenMacBulkMACFilterTable = _AdGenMacBulkMACFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2)
)
if mibBuilder.loadTexts:
    adGenMacBulkMACFilterTable.setStatus("current")
_AdGenMacBulkMACFilterEntry_Object = MibTableRow
adGenMacBulkMACFilterEntry = _AdGenMacBulkMACFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2, 1)
)
adGenMacBulkMACFilterEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMAC-MIB", "adGenMacBulkMACFilterInstance"),
)
if mibBuilder.loadTexts:
    adGenMacBulkMACFilterEntry.setStatus("current")
_AdGenMacBulkMACFilterInstance_Type = Integer32
_AdGenMacBulkMACFilterInstance_Object = MibTableColumn
adGenMacBulkMACFilterInstance = _AdGenMacBulkMACFilterInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2, 1, 1),
    _AdGenMacBulkMACFilterInstance_Type()
)
adGenMacBulkMACFilterInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMacBulkMACFilterInstance.setStatus("current")


class _AdGenMacBulkMACFilterStag_Type(Integer32):
    """Custom type adGenMacBulkMACFilterStag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AdGenMacBulkMACFilterStag_Type.__name__ = "Integer32"
_AdGenMacBulkMACFilterStag_Object = MibTableColumn
adGenMacBulkMACFilterStag = _AdGenMacBulkMACFilterStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2, 1, 2),
    _AdGenMacBulkMACFilterStag_Type()
)
adGenMacBulkMACFilterStag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacBulkMACFilterStag.setStatus("current")


class _AdGenMacBulkMACFilterStatus_Type(Integer32):
    """Custom type adGenMacBulkMACFilterStatus based on Integer32"""
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
        *(("all", 0),
          ("static", 1),
          ("dynamic", 2),
          ("multicast", 3))
    )


_AdGenMacBulkMACFilterStatus_Type.__name__ = "Integer32"
_AdGenMacBulkMACFilterStatus_Object = MibTableColumn
adGenMacBulkMACFilterStatus = _AdGenMacBulkMACFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2, 1, 3),
    _AdGenMacBulkMACFilterStatus_Type()
)
adGenMacBulkMACFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacBulkMACFilterStatus.setStatus("current")
_AdGenMacBulkMACFilterInterface_Type = InterfaceIndexOrZero
_AdGenMacBulkMACFilterInterface_Object = MibTableColumn
adGenMacBulkMACFilterInterface = _AdGenMacBulkMACFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2, 1, 4),
    _AdGenMacBulkMACFilterInterface_Type()
)
adGenMacBulkMACFilterInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacBulkMACFilterInterface.setStatus("current")


class _AdGenMacBulkMACSlotInstance_Type(Integer32):
    """Custom type adGenMacBulkMACSlotInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("updateinstance", 1)
    )


_AdGenMacBulkMACSlotInstance_Type.__name__ = "Integer32"
_AdGenMacBulkMACSlotInstance_Object = MibTableColumn
adGenMacBulkMACSlotInstance = _AdGenMacBulkMACSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 4, 2, 1, 5),
    _AdGenMacBulkMACSlotInstance_Type()
)
adGenMacBulkMACSlotInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMacBulkMACSlotInstance.setStatus("current")

# Managed Objects groups


# Notification objects

adGenMacEvent15MinMaxEntriesTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 0, 1)
)
adGenMacEvent15MinMaxEntriesTCA.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenMacEvent15MinMaxEntriesTCA.setStatus(
        "current"
    )

adGenMacEvent24HrMaxEntriesTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 8, 0, 11)
)
adGenMacEvent24HrMaxEntriesTCA.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenMacEvent24HrMaxEntriesTCA.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMAC-MIB",
    **{"adGenMacEvents": adGenMacEvents,
       "adGenMacEvent15MinMaxEntriesTCA": adGenMacEvent15MinMaxEntriesTCA,
       "adGenMacEvent24HrMaxEntriesTCA": adGenMacEvent24HrMaxEntriesTCA,
       "adGenMacProvisioning": adGenMacProvisioning,
       "adGenMacProvTable": adGenMacProvTable,
       "adGenMacProvEntry": adGenMacProvEntry,
       "adGenMacProvLimit": adGenMacProvLimit,
       "adGenMacProvAgingTime": adGenMacProvAgingTime,
       "adGenClearMACAddressSlotTable": adGenClearMACAddressSlotTable,
       "adGenClearMACAddressSlotEntry": adGenClearMACAddressSlotEntry,
       "adGenClearSingleMAC": adGenClearSingleMAC,
       "adGenClearAllDynamicMAC": adGenClearAllDynamicMAC,
       "adGenClearMACAddressTable": adGenClearMACAddressTable,
       "adGenClearMACAddressEntry": adGenClearMACAddressEntry,
       "adGenClearMACAddressStag": adGenClearMACAddressStag,
       "adGenClearMACAddressStatus": adGenClearMACAddressStatus,
       "adGenClearMACAddressClear": adGenClearMACAddressClear,
       "adGenClearMACAddressInterfaceIDTable": adGenClearMACAddressInterfaceIDTable,
       "adGenClearMACAddressInterfaceIDEntry": adGenClearMACAddressInterfaceIDEntry,
       "adGenClearMACAddressInterfaceID": adGenClearMACAddressInterfaceID,
       "adGenClearMACAddressInterfaceIDClear": adGenClearMACAddressInterfaceIDClear,
       "adGenMacStatus": adGenMacStatus,
       "adGenMacStatusTable": adGenMacStatusTable,
       "adGenMacStatusEntry": adGenMacStatusEntry,
       "adGenMacStatusNumEntries": adGenMacStatusNumEntries,
       "adGenMacStatusMaxLimit": adGenMacStatusMaxLimit,
       "adGenMacStatusMinAgingTime": adGenMacStatusMinAgingTime,
       "adGenMacStatusMaxAgingTime": adGenMacStatusMaxAgingTime,
       "adGenMacCountsTable": adGenMacCountsTable,
       "adGenMacCountsEntry": adGenMacCountsEntry,
       "adGenMacCounts5MinAvgEntries": adGenMacCounts5MinAvgEntries,
       "adGenMacLookUpTable": adGenMacLookUpTable,
       "adGenMacLookUpEntry": adGenMacLookUpEntry,
       "adGenMacLookUpVlanIndex": adGenMacLookUpVlanIndex,
       "adGenMacLookUpMacIndex": adGenMacLookUpMacIndex,
       "adGenMacLookUp": adGenMacLookUp,
       "adGenMacPerformance": adGenMacPerformance,
       "adGenMacThresh15MinTable": adGenMacThresh15MinTable,
       "adGenMacThresh15MinEntry": adGenMacThresh15MinEntry,
       "adGenMacThresh15MinMaxEntries": adGenMacThresh15MinMaxEntries,
       "adGenMacThresh24HrTable": adGenMacThresh24HrTable,
       "adGenMacThresh24HrEntry": adGenMacThresh24HrEntry,
       "adGenMacThresh24HrMaxEntries": adGenMacThresh24HrMaxEntries,
       "adGenMacPerf15MinTable": adGenMacPerf15MinTable,
       "adGenMacPerf15MinEntry": adGenMacPerf15MinEntry,
       "adGenMacPerf15MinMaxEntries": adGenMacPerf15MinMaxEntries,
       "adGenMacPerf15MinIntTable": adGenMacPerf15MinIntTable,
       "adGenMacPerf15MinIntEntry": adGenMacPerf15MinIntEntry,
       "adGenMacPerf15MinIntNum": adGenMacPerf15MinIntNum,
       "adGenMacPerf15MinIntMaxEntries": adGenMacPerf15MinIntMaxEntries,
       "adGenMacPerf24HrTable": adGenMacPerf24HrTable,
       "adGenMacPerf24HrEntry": adGenMacPerf24HrEntry,
       "adGenMacPerf24HrMaxEntries": adGenMacPerf24HrMaxEntries,
       "adGenMacPerf24HrIntTable": adGenMacPerf24HrIntTable,
       "adGenMacPerf24HrIntEntry": adGenMacPerf24HrIntEntry,
       "adGenMacPerf24HrIntNum": adGenMacPerf24HrIntNum,
       "adGenMacPerf24HrIntMaxEntries": adGenMacPerf24HrIntMaxEntries,
       "adGenMacBulkMAC": adGenMacBulkMAC,
       "adGenMacReserveInstanceBulkMACSlotTable": adGenMacReserveInstanceBulkMACSlotTable,
       "adGenMacReserveInstanceBulkMACSlotEntry": adGenMacReserveInstanceBulkMACSlotEntry,
       "adGenMacReserveInstanceBulkMACSlotInstance": adGenMacReserveInstanceBulkMACSlotInstance,
       "adGenMacBulkMACFilterTable": adGenMacBulkMACFilterTable,
       "adGenMacBulkMACFilterEntry": adGenMacBulkMACFilterEntry,
       "adGenMacBulkMACFilterInstance": adGenMacBulkMACFilterInstance,
       "adGenMacBulkMACFilterStag": adGenMacBulkMACFilterStag,
       "adGenMacBulkMACFilterStatus": adGenMacBulkMACFilterStatus,
       "adGenMacBulkMACFilterInterface": adGenMacBulkMACFilterInterface,
       "adGenMacBulkMACSlotInstance": adGenMacBulkMACSlotInstance,
       "adGenMacIdentity": adGenMacIdentity}
)
