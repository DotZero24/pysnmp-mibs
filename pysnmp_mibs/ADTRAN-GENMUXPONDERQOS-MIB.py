# SNMP MIB module (ADTRAN-GENMUXPONDERQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMUXPONDERQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:09 2025
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

(adGenMuxponderQoS,
 adGenMuxponderQoSID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMuxponderQoS",
    "adGenMuxponderQoSID")

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

adGenMuxponderQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 34, 1)
)
if mibBuilder.loadTexts:
    adGenMuxponderQoSMIB.setRevisions(
        ("2010-09-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMuxponderQoSEvents_ObjectIdentity = ObjectIdentity
adGenMuxponderQoSEvents = _AdGenMuxponderQoSEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 0)
)
_AdGenMuxponderQoSProvisioning_ObjectIdentity = ObjectIdentity
adGenMuxponderQoSProvisioning = _AdGenMuxponderQoSProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1)
)
_AdGenMuxponderQueueCoSMapTable_Object = MibTable
adGenMuxponderQueueCoSMapTable = _AdGenMuxponderQueueCoSMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapTable.setStatus("current")
_AdGenMuxponderQueueCoSMapEntry_Object = MibTableRow
adGenMuxponderQueueCoSMapEntry = _AdGenMuxponderQueueCoSMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1)
)
adGenMuxponderQueueCoSMapEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapEntry.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri0_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri0_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri0 = _AdGenMuxponderQueueCoSMapForPri0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 1),
    _AdGenMuxponderQueueCoSMapForPri0_Type()
)
adGenMuxponderQueueCoSMapForPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri0.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri1_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri1_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri1 = _AdGenMuxponderQueueCoSMapForPri1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 2),
    _AdGenMuxponderQueueCoSMapForPri1_Type()
)
adGenMuxponderQueueCoSMapForPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri1.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri2_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri2_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri2 = _AdGenMuxponderQueueCoSMapForPri2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 3),
    _AdGenMuxponderQueueCoSMapForPri2_Type()
)
adGenMuxponderQueueCoSMapForPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri2.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri3_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri3_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri3 = _AdGenMuxponderQueueCoSMapForPri3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 4),
    _AdGenMuxponderQueueCoSMapForPri3_Type()
)
adGenMuxponderQueueCoSMapForPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri3.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri4_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri4_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri4 = _AdGenMuxponderQueueCoSMapForPri4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 5),
    _AdGenMuxponderQueueCoSMapForPri4_Type()
)
adGenMuxponderQueueCoSMapForPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri4.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri5_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri5_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri5 = _AdGenMuxponderQueueCoSMapForPri5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 6),
    _AdGenMuxponderQueueCoSMapForPri5_Type()
)
adGenMuxponderQueueCoSMapForPri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri5.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri6_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri6_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri6 = _AdGenMuxponderQueueCoSMapForPri6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 7),
    _AdGenMuxponderQueueCoSMapForPri6_Type()
)
adGenMuxponderQueueCoSMapForPri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri6.setStatus("current")
_AdGenMuxponderQueueCoSMapForPri7_Type = Integer32
_AdGenMuxponderQueueCoSMapForPri7_Object = MibTableColumn
adGenMuxponderQueueCoSMapForPri7 = _AdGenMuxponderQueueCoSMapForPri7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 8),
    _AdGenMuxponderQueueCoSMapForPri7_Type()
)
adGenMuxponderQueueCoSMapForPri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapForPri7.setStatus("current")
_AdGenMuxponderQueueCoSMapUntagged_Type = Integer32
_AdGenMuxponderQueueCoSMapUntagged_Object = MibTableColumn
adGenMuxponderQueueCoSMapUntagged = _AdGenMuxponderQueueCoSMapUntagged_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 34, 1, 1, 1, 9),
    _AdGenMuxponderQueueCoSMapUntagged_Type()
)
adGenMuxponderQueueCoSMapUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxponderQueueCoSMapUntagged.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMUXPONDERQOS-MIB",
    **{"adGenMuxponderQoSEvents": adGenMuxponderQoSEvents,
       "adGenMuxponderQoSProvisioning": adGenMuxponderQoSProvisioning,
       "adGenMuxponderQueueCoSMapTable": adGenMuxponderQueueCoSMapTable,
       "adGenMuxponderQueueCoSMapEntry": adGenMuxponderQueueCoSMapEntry,
       "adGenMuxponderQueueCoSMapForPri0": adGenMuxponderQueueCoSMapForPri0,
       "adGenMuxponderQueueCoSMapForPri1": adGenMuxponderQueueCoSMapForPri1,
       "adGenMuxponderQueueCoSMapForPri2": adGenMuxponderQueueCoSMapForPri2,
       "adGenMuxponderQueueCoSMapForPri3": adGenMuxponderQueueCoSMapForPri3,
       "adGenMuxponderQueueCoSMapForPri4": adGenMuxponderQueueCoSMapForPri4,
       "adGenMuxponderQueueCoSMapForPri5": adGenMuxponderQueueCoSMapForPri5,
       "adGenMuxponderQueueCoSMapForPri6": adGenMuxponderQueueCoSMapForPri6,
       "adGenMuxponderQueueCoSMapForPri7": adGenMuxponderQueueCoSMapForPri7,
       "adGenMuxponderQueueCoSMapUntagged": adGenMuxponderQueueCoSMapUntagged,
       "adGenMuxponderQoSMIB": adGenMuxponderQoSMIB}
)
