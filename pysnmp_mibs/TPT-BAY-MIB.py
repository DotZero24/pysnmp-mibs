# SNMP MIB module (TPT-BAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-BAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:06 2025
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

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_slot_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17)
)
if mibBuilder.loadTexts:
    tpt_slot_objs.setRevisions(
        ("2016-05-25 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SlotStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("empty", 0),
          ("active", 1),
          ("error", 2))
    )



class SlotEvent(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("insert", 0),
          ("remove", 1))
    )



class SlotModuleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("type-12-port-1g-copper", 1),
          ("type-12-port-1g-sfp", 2),
          ("type-8-port-10g-sfp", 3),
          ("type-2-port-40g-sfp", 4),
          ("type-6100", 5),
          ("type-5100", 6),
          ("type-2500", 7),
          ("type-1400", 8),
          ("type-660", 9),
          ("type-330", 10),
          ("type-110", 11),
          ("type-10", 12),
          ("type-empty", 13),
          ("type-8-port-1g-copper-bypass", 14),
          ("type-4-port-1g-sfp-sr-bypass", 15),
          ("type-4-port-1g-sfp-lr-bypass", 16),
          ("type-4-port-10g-sfp-sr-bypass", 17),
          ("type-4-port-10g-sfp-lr-bypass", 18))
    )



# MIB Managed Objects in the order of their OIDs

_SlotTempTable_Object = MibTable
slotTempTable = _SlotTempTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1)
)
if mibBuilder.loadTexts:
    slotTempTable.setStatus("current")
_SlotTempEntry_Object = MibTableRow
slotTempEntry = _SlotTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1)
)
slotTempEntry.setIndexNames(
    (0, "TPT-BAY-MIB", "slotTempIndex"),
)
if mibBuilder.loadTexts:
    slotTempEntry.setStatus("current")
_SlotTempIndex_Type = Unsigned32
_SlotTempIndex_Object = MibTableColumn
slotTempIndex = _SlotTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 1),
    _SlotTempIndex_Type()
)
slotTempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotTempIndex.setStatus("current")


class _SlotName_Type(OctetString):
    """Custom type slotName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotName_Type.__name__ = "OctetString"
_SlotName_Object = MibTableColumn
slotName = _SlotName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 2),
    _SlotName_Type()
)
slotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotName.setStatus("current")


class _SlotModuleName_Type(OctetString):
    """Custom type slotModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotModuleName_Type.__name__ = "OctetString"
_SlotModuleName_Object = MibTableColumn
slotModuleName = _SlotModuleName_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 3),
    _SlotModuleName_Type()
)
slotModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleName.setStatus("current")
_SlotStatus_Type = SlotStatus
_SlotStatus_Object = MibTableColumn
slotStatus = _SlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 4),
    _SlotStatus_Type()
)
slotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatus.setStatus("current")


class _SlotModuleSerialNum_Type(OctetString):
    """Custom type slotModuleSerialNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SlotModuleSerialNum_Type.__name__ = "OctetString"
_SlotModuleSerialNum_Object = MibTableColumn
slotModuleSerialNum = _SlotModuleSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 5),
    _SlotModuleSerialNum_Type()
)
slotModuleSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleSerialNum.setStatus("current")
_SlotModuleType_Type = SlotModuleType
_SlotModuleType_Object = MibTableColumn
slotModuleType = _SlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 17, 1, 1, 6),
    _SlotModuleType_Type()
)
slotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotModuleType.setStatus("current")


class _TptSlotDeviceID_Type(OctetString):
    """Custom type tptSlotDeviceID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TptSlotDeviceID_Type.__name__ = "OctetString"
_TptSlotDeviceID_Object = MibScalar
tptSlotDeviceID = _TptSlotDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 281),
    _TptSlotDeviceID_Type()
)
tptSlotDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSlotDeviceID.setStatus("current")
_TptSlotID_Type = Unsigned32
_TptSlotID_Object = MibScalar
tptSlotID = _TptSlotID_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 282),
    _TptSlotID_Type()
)
tptSlotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSlotID.setStatus("current")
_TptSlotEvent_Type = SlotEvent
_TptSlotEvent_Object = MibScalar
tptSlotEvent = _TptSlotEvent_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 283),
    _TptSlotEvent_Type()
)
tptSlotEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptSlotEvent.setStatus("current")

# Managed Objects groups


# Notification objects

tptSlotChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 54)
)
tptSlotChangeNotify.setObjects(
      *(("TPT-BAY-MIB", "tptSlotDeviceID"),
        ("TPT-BAY-MIB", "tptSlotID"),
        ("TPT-BAY-MIB", "tptSlotEvent"))
)
if mibBuilder.loadTexts:
    tptSlotChangeNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-BAY-MIB",
    **{"SlotStatus": SlotStatus,
       "SlotEvent": SlotEvent,
       "SlotModuleType": SlotModuleType,
       "tpt-slot-objs": tpt_slot_objs,
       "slotTempTable": slotTempTable,
       "slotTempEntry": slotTempEntry,
       "slotTempIndex": slotTempIndex,
       "slotName": slotName,
       "slotModuleName": slotModuleName,
       "slotStatus": slotStatus,
       "slotModuleSerialNum": slotModuleSerialNum,
       "slotModuleType": slotModuleType,
       "tptSlotChangeNotify": tptSlotChangeNotify,
       "tptSlotDeviceID": tptSlotDeviceID,
       "tptSlotID": tptSlotID,
       "tptSlotEvent": tptSlotEvent}
)
