# SNMP MIB module (SWITCH-SLOTCARDMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-SLOTCARDMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:59 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomSlotCardmgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23)
)
if mibBuilder.loadTexts:
    raisecomSlotCardmgmt.setRevisions(
        ("2011-01-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomSlotCardNotification_ObjectIdentity = ObjectIdentity
raisecomSlotCardNotification = _RaisecomSlotCardNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 1)
)
_RaisecomSlotCardMibObjects_ObjectIdentity = ObjectIdentity
raisecomSlotCardMibObjects = _RaisecomSlotCardMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2)
)
_RaisecomSlotCardGlobalGroup_ObjectIdentity = ObjectIdentity
raisecomSlotCardGlobalGroup = _RaisecomSlotCardGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 1)
)
_RaisecomSlotCardNum_Type = Unsigned32
_RaisecomSlotCardNum_Object = MibScalar
raisecomSlotCardNum = _RaisecomSlotCardNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 1, 1),
    _RaisecomSlotCardNum_Type()
)
raisecomSlotCardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomSlotCardNum.setStatus("current")
_RaisecomSlotCardTrapEnable_Type = EnableVar
_RaisecomSlotCardTrapEnable_Object = MibScalar
raisecomSlotCardTrapEnable = _RaisecomSlotCardTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 1, 2),
    _RaisecomSlotCardTrapEnable_Type()
)
raisecomSlotCardTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomSlotCardTrapEnable.setStatus("current")
_RaisecomSlotCardTable_Object = MibTable
raisecomSlotCardTable = _RaisecomSlotCardTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2)
)
if mibBuilder.loadTexts:
    raisecomSlotCardTable.setStatus("current")
_RaisecomSlotCardEntry_Object = MibTableRow
raisecomSlotCardEntry = _RaisecomSlotCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2, 1)
)
raisecomSlotCardEntry.setIndexNames(
    (0, "SWITCH-SLOTCARDMGMT-MIB", "raisecomSlotCardIndex"),
)
if mibBuilder.loadTexts:
    raisecomSlotCardEntry.setStatus("current")
_RaisecomSlotCardIndex_Type = Unsigned32
_RaisecomSlotCardIndex_Object = MibTableColumn
raisecomSlotCardIndex = _RaisecomSlotCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2, 1, 1),
    _RaisecomSlotCardIndex_Type()
)
raisecomSlotCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomSlotCardIndex.setStatus("current")


class _RaisecomSlotCardSerialNumber_Type(OctetString):
    """Custom type raisecomSlotCardSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_RaisecomSlotCardSerialNumber_Type.__name__ = "OctetString"
_RaisecomSlotCardSerialNumber_Object = MibTableColumn
raisecomSlotCardSerialNumber = _RaisecomSlotCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2, 1, 2),
    _RaisecomSlotCardSerialNumber_Type()
)
raisecomSlotCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomSlotCardSerialNumber.setStatus("current")


class _RaisecomSlotCardState_Type(Integer32):
    """Custom type raisecomSlotCardState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RaisecomSlotCardState_Type.__name__ = "Integer32"
_RaisecomSlotCardState_Object = MibTableColumn
raisecomSlotCardState = _RaisecomSlotCardState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2, 1, 3),
    _RaisecomSlotCardState_Type()
)
raisecomSlotCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomSlotCardState.setStatus("current")


class _RaisecomSlotCardType_Type(Integer32):
    """Custom type raisecomSlotCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("card-ptp-synce", 1),
          ("card-tdmop", 2),
          ("null", 255))
    )


_RaisecomSlotCardType_Type.__name__ = "Integer32"
_RaisecomSlotCardType_Object = MibTableColumn
raisecomSlotCardType = _RaisecomSlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2, 1, 4),
    _RaisecomSlotCardType_Type()
)
raisecomSlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomSlotCardType.setStatus("current")


class _RaisecomSlotCardDescr_Type(OctetString):
    """Custom type raisecomSlotCardDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(240, 240),
    )
    fixed_length = 240


_RaisecomSlotCardDescr_Type.__name__ = "OctetString"
_RaisecomSlotCardDescr_Object = MibTableColumn
raisecomSlotCardDescr = _RaisecomSlotCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 2, 2, 1, 5),
    _RaisecomSlotCardDescr_Type()
)
raisecomSlotCardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomSlotCardDescr.setStatus("current")

# Managed Objects groups


# Notification objects

raisecomSlotCardStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 23, 1, 1)
)
raisecomSlotCardStateChange.setObjects(
    ("SWITCH-SLOTCARDMGMT-MIB", "raisecomSlotCardState")
)
if mibBuilder.loadTexts:
    raisecomSlotCardStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-SLOTCARDMGMT-MIB",
    **{"raisecomSlotCardmgmt": raisecomSlotCardmgmt,
       "raisecomSlotCardNotification": raisecomSlotCardNotification,
       "raisecomSlotCardStateChange": raisecomSlotCardStateChange,
       "raisecomSlotCardMibObjects": raisecomSlotCardMibObjects,
       "raisecomSlotCardGlobalGroup": raisecomSlotCardGlobalGroup,
       "raisecomSlotCardNum": raisecomSlotCardNum,
       "raisecomSlotCardTrapEnable": raisecomSlotCardTrapEnable,
       "raisecomSlotCardTable": raisecomSlotCardTable,
       "raisecomSlotCardEntry": raisecomSlotCardEntry,
       "raisecomSlotCardIndex": raisecomSlotCardIndex,
       "raisecomSlotCardSerialNumber": raisecomSlotCardSerialNumber,
       "raisecomSlotCardState": raisecomSlotCardState,
       "raisecomSlotCardType": raisecomSlotCardType,
       "raisecomSlotCardDescr": raisecomSlotCardDescr}
)
