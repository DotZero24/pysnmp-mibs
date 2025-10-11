# SNMP MIB module (ADTRAN-GENPORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENPORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:40 2025
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

(adGenericShelves,) = mibBuilder.importSymbols(
    "ADTRAN-GENCHASSIS-MIB",
    "adGenericShelves")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(AdAlarmSeverity,
 AdPresence,
 AdProductIdentifier) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "AdAlarmSeverity",
    "AdPresence",
    "AdProductIdentifier")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenPort = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPortInfoTable_Object = MibTable
adGenPortInfoTable = _AdGenPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3)
)
if mibBuilder.loadTexts:
    adGenPortInfoTable.setStatus("current")
_AdGenPortInfoEntry_Object = MibTableRow
adGenPortInfoEntry = _AdGenPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1)
)
adGenPortInfoEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenPortInfoEntry.setStatus("current")


class _AdGenPortInfoIndex_Type(Integer32):
    """Custom type adGenPortInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenPortInfoIndex_Type.__name__ = "Integer32"
_AdGenPortInfoIndex_Object = MibTableColumn
adGenPortInfoIndex = _AdGenPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 1),
    _AdGenPortInfoIndex_Type()
)
adGenPortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortInfoIndex.setStatus("current")
_AdGenPortInfoState_Type = AdPresence
_AdGenPortInfoState_Object = MibTableColumn
adGenPortInfoState = _AdGenPortInfoState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 3),
    _AdGenPortInfoState_Type()
)
adGenPortInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortInfoState.setStatus("current")
_AdGenPortIfIndex_Type = Integer32
_AdGenPortIfIndex_Object = MibTableColumn
adGenPortIfIndex = _AdGenPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 4),
    _AdGenPortIfIndex_Type()
)
adGenPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortIfIndex.setStatus("current")
_AdGenPortDataRate_Type = Integer32
_AdGenPortDataRate_Object = MibTableColumn
adGenPortDataRate = _AdGenPortDataRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 6),
    _AdGenPortDataRate_Type()
)
adGenPortDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPortDataRate.setStatus("current")
_AdGenPortFarEndIP_Type = IpAddress
_AdGenPortFarEndIP_Object = MibTableColumn
adGenPortFarEndIP = _AdGenPortFarEndIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 8),
    _AdGenPortFarEndIP_Type()
)
adGenPortFarEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPortFarEndIP.setStatus("current")
_AdGenPortAlarmStatus_Type = OctetString
_AdGenPortAlarmStatus_Object = MibTableColumn
adGenPortAlarmStatus = _AdGenPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 9),
    _AdGenPortAlarmStatus_Type()
)
adGenPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortAlarmStatus.setStatus("current")
_AdGenPortCustomerUse_Type = DisplayString
_AdGenPortCustomerUse_Object = MibTableColumn
adGenPortCustomerUse = _AdGenPortCustomerUse_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 10),
    _AdGenPortCustomerUse_Type()
)
adGenPortCustomerUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPortCustomerUse.setStatus("current")
_AdGenPortTrapIdentifier_Type = DisplayString
_AdGenPortTrapIdentifier_Object = MibTableColumn
adGenPortTrapIdentifier = _AdGenPortTrapIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 11),
    _AdGenPortTrapIdentifier_Type()
)
adGenPortTrapIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPortTrapIdentifier.setStatus("current")
_AdGenPortTrapSeverity_Type = AdAlarmSeverity
_AdGenPortTrapSeverity_Object = MibTableColumn
adGenPortTrapSeverity = _AdGenPortTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 12),
    _AdGenPortTrapSeverity_Type()
)
adGenPortTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortTrapSeverity.setStatus("current")
_AdGenPortFarEndID_Type = AdProductIdentifier
_AdGenPortFarEndID_Object = MibTableColumn
adGenPortFarEndID = _AdGenPortFarEndID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 3, 1, 14),
    _AdGenPortFarEndID_Type()
)
adGenPortFarEndID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortFarEndID.setStatus("current")
_AdGenPortSlotMapTable_Object = MibTable
adGenPortSlotMapTable = _AdGenPortSlotMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 4)
)
if mibBuilder.loadTexts:
    adGenPortSlotMapTable.setStatus("current")
_AdGenPortSlotMapEntry_Object = MibTableRow
adGenPortSlotMapEntry = _AdGenPortSlotMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 4, 1)
)
adGenPortSlotMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPortSlotMapEntry.setStatus("current")


class _AdGenSlotAddress_Type(Integer32):
    """Custom type adGenSlotAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenSlotAddress_Type.__name__ = "Integer32"
_AdGenSlotAddress_Object = MibTableColumn
adGenSlotAddress = _AdGenSlotAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 4, 1, 2),
    _AdGenSlotAddress_Type()
)
adGenSlotAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSlotAddress.setStatus("current")


class _AdGenPortAddress_Type(Integer32):
    """Custom type adGenPortAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenPortAddress_Type.__name__ = "Integer32"
_AdGenPortAddress_Object = MibTableColumn
adGenPortAddress = _AdGenPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 4, 1, 3),
    _AdGenPortAddress_Type()
)
adGenPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortAddress.setStatus("current")
_AdGenPortIfType_Type = Integer32
_AdGenPortIfType_Object = MibTableColumn
adGenPortIfType = _AdGenPortIfType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 4, 1, 4),
    _AdGenPortIfType_Type()
)
adGenPortIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPortIfType.setStatus("current")
_AdGenPortIfInfoTable_Object = MibTable
adGenPortIfInfoTable = _AdGenPortIfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 5)
)
if mibBuilder.loadTexts:
    adGenPortIfInfoTable.setStatus("current")
_AdGenPortIfInfoEntry_Object = MibTableRow
adGenPortIfInfoEntry = _AdGenPortIfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 5, 1)
)
adGenPortIfInfoEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
    (0, "ADTRAN-GENPORT-MIB", "adGenIfTypeIndex"),
)
if mibBuilder.loadTexts:
    adGenPortIfInfoEntry.setStatus("current")
_AdGenIfTypeIndex_Type = Integer32
_AdGenIfTypeIndex_Object = MibTableColumn
adGenIfTypeIndex = _AdGenIfTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 5, 1, 1),
    _AdGenIfTypeIndex_Type()
)
adGenIfTypeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfTypeIndex.setStatus("current")
_AdGenIfIfIndex_Type = Integer32
_AdGenIfIfIndex_Object = MibTableColumn
adGenIfIfIndex = _AdGenIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 5, 1, 4),
    _AdGenIfIfIndex_Type()
)
adGenIfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfIfIndex.setStatus("current")
_AdGenIfCustomerUse_Type = DisplayString
_AdGenIfCustomerUse_Object = MibTableColumn
adGenIfCustomerUse = _AdGenIfCustomerUse_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 5, 1, 10),
    _AdGenIfCustomerUse_Type()
)
adGenIfCustomerUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfCustomerUse.setStatus("current")
_AdGenPortConformance_ObjectIdentity = ObjectIdentity
adGenPortConformance = _AdGenPortConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 99)
)
_AdGenPortCompliances_ObjectIdentity = ObjectIdentity
adGenPortCompliances = _AdGenPortCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 99, 1)
)
_AdGenPortMIBGroups_ObjectIdentity = ObjectIdentity
adGenPortMIBGroups = _AdGenPortMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 99, 2)
)

# Managed Objects groups

adGenPortBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 99, 2, 1)
)
adGenPortBaseGroup.setObjects(
      *(("ADTRAN-GENPORT-MIB", "adGenPortInfoState"),
        ("ADTRAN-GENPORT-MIB", "adGenPortIfIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortDataRate"),
        ("ADTRAN-GENPORT-MIB", "adGenPortFarEndIP"),
        ("ADTRAN-GENPORT-MIB", "adGenPortAlarmStatus"),
        ("ADTRAN-GENPORT-MIB", "adGenPortCustomerUse"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapSeverity"),
        ("ADTRAN-GENPORT-MIB", "adGenPortFarEndID"),
        ("ADTRAN-GENPORT-MIB", "adGenSlotAddress"),
        ("ADTRAN-GENPORT-MIB", "adGenPortAddress"),
        ("ADTRAN-GENPORT-MIB", "adGenPortIfType"),
        ("ADTRAN-GENPORT-MIB", "adGenIfTypeIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenIfIfIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenIfCustomerUse"))
)
if mibBuilder.loadTexts:
    adGenPortBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenPortCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 5, 13, 3, 99, 1, 1)
)
adGenPortCompliance.setObjects(
    ("ADTRAN-GENPORT-MIB", "adGenPortBaseGroup")
)
if mibBuilder.loadTexts:
    adGenPortCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENPORT-MIB",
    **{"adGenPort": adGenPort,
       "adGenPortInfoTable": adGenPortInfoTable,
       "adGenPortInfoEntry": adGenPortInfoEntry,
       "adGenPortInfoIndex": adGenPortInfoIndex,
       "adGenPortInfoState": adGenPortInfoState,
       "adGenPortIfIndex": adGenPortIfIndex,
       "adGenPortDataRate": adGenPortDataRate,
       "adGenPortFarEndIP": adGenPortFarEndIP,
       "adGenPortAlarmStatus": adGenPortAlarmStatus,
       "adGenPortCustomerUse": adGenPortCustomerUse,
       "adGenPortTrapIdentifier": adGenPortTrapIdentifier,
       "adGenPortTrapSeverity": adGenPortTrapSeverity,
       "adGenPortFarEndID": adGenPortFarEndID,
       "adGenPortSlotMapTable": adGenPortSlotMapTable,
       "adGenPortSlotMapEntry": adGenPortSlotMapEntry,
       "adGenSlotAddress": adGenSlotAddress,
       "adGenPortAddress": adGenPortAddress,
       "adGenPortIfType": adGenPortIfType,
       "adGenPortIfInfoTable": adGenPortIfInfoTable,
       "adGenPortIfInfoEntry": adGenPortIfInfoEntry,
       "adGenIfTypeIndex": adGenIfTypeIndex,
       "adGenIfIfIndex": adGenIfIfIndex,
       "adGenIfCustomerUse": adGenIfCustomerUse,
       "adGenPortConformance": adGenPortConformance,
       "adGenPortCompliances": adGenPortCompliances,
       "adGenPortCompliance": adGenPortCompliance,
       "adGenPortMIBGroups": adGenPortMIBGroups,
       "adGenPortBaseGroup": adGenPortBaseGroup}
)
