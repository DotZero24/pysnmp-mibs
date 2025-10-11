# SNMP MIB module (HPN-ICF-E1T1VI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-E1T1VI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:16 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
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

hpnicfE1T1VI = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76)
)
if mibBuilder.loadTexts:
    hpnicfE1T1VI.setRevisions(
        ("2010-04-08 18:55",
         "2009-06-08 17:41",
         "2007-04-05 15:42")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfE1T1VITable_Object = MibTable
hpnicfE1T1VITable = _HpnicfE1T1VITable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 1)
)
if mibBuilder.loadTexts:
    hpnicfE1T1VITable.setStatus("current")
_HpnicfE1T1VIEntry_Object = MibTableRow
hpnicfE1T1VIEntry = _HpnicfE1T1VIEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 1, 1)
)
hpnicfE1T1VIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfE1T1VIEntry.setStatus("current")
_HpnicfE1T1VIUsingTimeslots_Type = Integer32
_HpnicfE1T1VIUsingTimeslots_Object = MibTableColumn
hpnicfE1T1VIUsingTimeslots = _HpnicfE1T1VIUsingTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 1, 1, 1),
    _HpnicfE1T1VIUsingTimeslots_Type()
)
hpnicfE1T1VIUsingTimeslots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfE1T1VIUsingTimeslots.setStatus("current")
_HpnicfE1T1VIUsingTimeslotsRatio_Type = Integer32
_HpnicfE1T1VIUsingTimeslotsRatio_Object = MibTableColumn
hpnicfE1T1VIUsingTimeslotsRatio = _HpnicfE1T1VIUsingTimeslotsRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 1, 1, 2),
    _HpnicfE1T1VIUsingTimeslotsRatio_Type()
)
hpnicfE1T1VIUsingTimeslotsRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfE1T1VIUsingTimeslotsRatio.setStatus("current")
_HpnicfE1T1VINotifications_ObjectIdentity = ObjectIdentity
hpnicfE1T1VINotifications = _HpnicfE1T1VINotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 2)
)
_HpnicfE1T1VITrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfE1T1VITrapPrefix = _HpnicfE1T1VITrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 2, 0)
)
_HpnicfE1T1VIGeneral_ObjectIdentity = ObjectIdentity
hpnicfE1T1VIGeneral = _HpnicfE1T1VIGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 3)
)


class _HpnicfE1T1VITrapTimeSlotEnable_Type(Integer32):
    """Custom type hpnicfE1T1VITrapTimeSlotEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_HpnicfE1T1VITrapTimeSlotEnable_Type.__name__ = "Integer32"
_HpnicfE1T1VITrapTimeSlotEnable_Object = MibScalar
hpnicfE1T1VITrapTimeSlotEnable = _HpnicfE1T1VITrapTimeSlotEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 3, 1),
    _HpnicfE1T1VITrapTimeSlotEnable_Type()
)
hpnicfE1T1VITrapTimeSlotEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfE1T1VITrapTimeSlotEnable.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfE1T1VITrapTimeSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 76, 2, 0, 1)
)
hpnicfE1T1VITrapTimeSlot.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfE1T1VITrapTimeSlot.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-E1T1VI-MIB",
    **{"hpnicfE1T1VI": hpnicfE1T1VI,
       "hpnicfE1T1VITable": hpnicfE1T1VITable,
       "hpnicfE1T1VIEntry": hpnicfE1T1VIEntry,
       "hpnicfE1T1VIUsingTimeslots": hpnicfE1T1VIUsingTimeslots,
       "hpnicfE1T1VIUsingTimeslotsRatio": hpnicfE1T1VIUsingTimeslotsRatio,
       "hpnicfE1T1VINotifications": hpnicfE1T1VINotifications,
       "hpnicfE1T1VITrapPrefix": hpnicfE1T1VITrapPrefix,
       "hpnicfE1T1VITrapTimeSlot": hpnicfE1T1VITrapTimeSlot,
       "hpnicfE1T1VIGeneral": hpnicfE1T1VIGeneral,
       "hpnicfE1T1VITrapTimeSlotEnable": hpnicfE1T1VITrapTimeSlotEnable}
)
