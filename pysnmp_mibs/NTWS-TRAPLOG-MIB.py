# SNMP MIB module (NTWS-TRAPLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NTWS-TRAPLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:05 2025
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

(ntwsMibs,) = mibBuilder.importSymbols(
    "NTWS-ROOT-MIB",
    "ntwsMibs")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ntwsTraplogMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13)
)
if mibBuilder.loadTexts:
    ntwsTraplogMib.setRevisions(
        ("2009-03-22 00:09",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtwsTraplogTrapOccurrenceIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class NtwsTraplogTrapOccurrenceIndexOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs

_NtwsTraplogMibObjects_ObjectIdentity = ObjectIdentity
ntwsTraplogMibObjects = _NtwsTraplogMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1)
)
_NtwsTraplogGuideObjects_ObjectIdentity = ObjectIdentity
ntwsTraplogGuideObjects = _NtwsTraplogGuideObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2)
)
_NtwsTraplogOldestTrapIndex_Type = NtwsTraplogTrapOccurrenceIndexOrZero
_NtwsTraplogOldestTrapIndex_Object = MibScalar
ntwsTraplogOldestTrapIndex = _NtwsTraplogOldestTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 1),
    _NtwsTraplogOldestTrapIndex_Type()
)
ntwsTraplogOldestTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogOldestTrapIndex.setStatus("current")
_NtwsTraplogNewestTrapIndex_Type = NtwsTraplogTrapOccurrenceIndexOrZero
_NtwsTraplogNewestTrapIndex_Object = MibScalar
ntwsTraplogNewestTrapIndex = _NtwsTraplogNewestTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 2),
    _NtwsTraplogNewestTrapIndex_Type()
)
ntwsTraplogNewestTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogNewestTrapIndex.setStatus("current")
_NtwsTraplogNewestTrapTime_Type = TimeStamp
_NtwsTraplogNewestTrapTime_Object = MibScalar
ntwsTraplogNewestTrapTime = _NtwsTraplogNewestTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 3),
    _NtwsTraplogNewestTrapTime_Type()
)
ntwsTraplogNewestTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogNewestTrapTime.setStatus("current")


class _NtwsTraplogNewestTrapDateAndTime_Type(DateAndTime):
    """Custom type ntwsTraplogNewestTrapDateAndTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_NtwsTraplogNewestTrapDateAndTime_Type.__name__ = "DateAndTime"
_NtwsTraplogNewestTrapDateAndTime_Object = MibScalar
ntwsTraplogNewestTrapDateAndTime = _NtwsTraplogNewestTrapDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 2, 4),
    _NtwsTraplogNewestTrapDateAndTime_Type()
)
ntwsTraplogNewestTrapDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogNewestTrapDateAndTime.setStatus("current")
_NtwsTraplogTrapTable_Object = MibTable
ntwsTraplogTrapTable = _NtwsTraplogTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3)
)
if mibBuilder.loadTexts:
    ntwsTraplogTrapTable.setStatus("current")
_NtwsTraplogTrapEntry_Object = MibTableRow
ntwsTraplogTrapEntry = _NtwsTraplogTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1)
)
ntwsTraplogTrapEntry.setIndexNames(
    (0, "NTWS-TRAPLOG-MIB", "ntwsTraplogTrapIndex"),
)
if mibBuilder.loadTexts:
    ntwsTraplogTrapEntry.setStatus("current")
_NtwsTraplogTrapIndex_Type = NtwsTraplogTrapOccurrenceIndex
_NtwsTraplogTrapIndex_Object = MibTableColumn
ntwsTraplogTrapIndex = _NtwsTraplogTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 1),
    _NtwsTraplogTrapIndex_Type()
)
ntwsTraplogTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsTraplogTrapIndex.setStatus("current")
_NtwsTraplogTrapTime_Type = TimeStamp
_NtwsTraplogTrapTime_Object = MibTableColumn
ntwsTraplogTrapTime = _NtwsTraplogTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 2),
    _NtwsTraplogTrapTime_Type()
)
ntwsTraplogTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogTrapTime.setStatus("current")
_NtwsTraplogTrapDateAndTime_Type = DateAndTime
_NtwsTraplogTrapDateAndTime_Object = MibTableColumn
ntwsTraplogTrapDateAndTime = _NtwsTraplogTrapDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 3),
    _NtwsTraplogTrapDateAndTime_Type()
)
ntwsTraplogTrapDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogTrapDateAndTime.setStatus("current")
_NtwsTraplogTrapNotificationID_Type = ObjectIdentifier
_NtwsTraplogTrapNotificationID_Object = MibTableColumn
ntwsTraplogTrapNotificationID = _NtwsTraplogTrapNotificationID_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 4),
    _NtwsTraplogTrapNotificationID_Type()
)
ntwsTraplogTrapNotificationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogTrapNotificationID.setStatus("current")


class _NtwsTraplogTrapNumVars_Type(Unsigned32):
    """Custom type ntwsTraplogTrapNumVars based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NtwsTraplogTrapNumVars_Type.__name__ = "Unsigned32"
_NtwsTraplogTrapNumVars_Object = MibTableColumn
ntwsTraplogTrapNumVars = _NtwsTraplogTrapNumVars_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 3, 1, 5),
    _NtwsTraplogTrapNumVars_Type()
)
ntwsTraplogTrapNumVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogTrapNumVars.setStatus("current")
_NtwsTraplogVarTable_Object = MibTable
ntwsTraplogVarTable = _NtwsTraplogVarTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4)
)
if mibBuilder.loadTexts:
    ntwsTraplogVarTable.setStatus("current")
_NtwsTraplogVarEntry_Object = MibTableRow
ntwsTraplogVarEntry = _NtwsTraplogVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1)
)
ntwsTraplogVarEntry.setIndexNames(
    (0, "NTWS-TRAPLOG-MIB", "ntwsTraplogVarTrapIndex"),
    (0, "NTWS-TRAPLOG-MIB", "ntwsTraplogVarIndex"),
)
if mibBuilder.loadTexts:
    ntwsTraplogVarEntry.setStatus("current")
_NtwsTraplogVarTrapIndex_Type = NtwsTraplogTrapOccurrenceIndex
_NtwsTraplogVarTrapIndex_Object = MibTableColumn
ntwsTraplogVarTrapIndex = _NtwsTraplogVarTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 1),
    _NtwsTraplogVarTrapIndex_Type()
)
ntwsTraplogVarTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsTraplogVarTrapIndex.setStatus("current")


class _NtwsTraplogVarIndex_Type(Unsigned32):
    """Custom type ntwsTraplogVarIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NtwsTraplogVarIndex_Type.__name__ = "Unsigned32"
_NtwsTraplogVarIndex_Object = MibTableColumn
ntwsTraplogVarIndex = _NtwsTraplogVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 2),
    _NtwsTraplogVarIndex_Type()
)
ntwsTraplogVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntwsTraplogVarIndex.setStatus("current")
_NtwsTraplogVarID_Type = ObjectIdentifier
_NtwsTraplogVarID_Object = MibTableColumn
ntwsTraplogVarID = _NtwsTraplogVarID_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 3),
    _NtwsTraplogVarID_Type()
)
ntwsTraplogVarID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarID.setStatus("current")


class _NtwsTraplogVarValueType_Type(Integer32):
    """Custom type ntwsTraplogVarValueType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("counter32", 1),
          ("unsigned32", 2),
          ("timeTicks", 3),
          ("integer32", 4),
          ("ipAddress", 5),
          ("octetString", 6),
          ("objectId", 7),
          ("counter64", 8))
    )


_NtwsTraplogVarValueType_Type.__name__ = "Integer32"
_NtwsTraplogVarValueType_Object = MibTableColumn
ntwsTraplogVarValueType = _NtwsTraplogVarValueType_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 4),
    _NtwsTraplogVarValueType_Type()
)
ntwsTraplogVarValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarValueType.setStatus("current")
_NtwsTraplogVarCounter32Val_Type = Counter32
_NtwsTraplogVarCounter32Val_Object = MibTableColumn
ntwsTraplogVarCounter32Val = _NtwsTraplogVarCounter32Val_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 5),
    _NtwsTraplogVarCounter32Val_Type()
)
ntwsTraplogVarCounter32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarCounter32Val.setStatus("current")
_NtwsTraplogVarUnsigned32Val_Type = Unsigned32
_NtwsTraplogVarUnsigned32Val_Object = MibTableColumn
ntwsTraplogVarUnsigned32Val = _NtwsTraplogVarUnsigned32Val_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 6),
    _NtwsTraplogVarUnsigned32Val_Type()
)
ntwsTraplogVarUnsigned32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarUnsigned32Val.setStatus("current")
_NtwsTraplogVarTimeTicksVal_Type = TimeTicks
_NtwsTraplogVarTimeTicksVal_Object = MibTableColumn
ntwsTraplogVarTimeTicksVal = _NtwsTraplogVarTimeTicksVal_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 7),
    _NtwsTraplogVarTimeTicksVal_Type()
)
ntwsTraplogVarTimeTicksVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarTimeTicksVal.setStatus("current")
_NtwsTraplogVarInteger32Val_Type = Integer32
_NtwsTraplogVarInteger32Val_Object = MibTableColumn
ntwsTraplogVarInteger32Val = _NtwsTraplogVarInteger32Val_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 8),
    _NtwsTraplogVarInteger32Val_Type()
)
ntwsTraplogVarInteger32Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarInteger32Val.setStatus("current")
_NtwsTraplogVarOctetStringVal_Type = OctetString
_NtwsTraplogVarOctetStringVal_Object = MibTableColumn
ntwsTraplogVarOctetStringVal = _NtwsTraplogVarOctetStringVal_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 9),
    _NtwsTraplogVarOctetStringVal_Type()
)
ntwsTraplogVarOctetStringVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarOctetStringVal.setStatus("current")
_NtwsTraplogVarIpAddressVal_Type = IpAddress
_NtwsTraplogVarIpAddressVal_Object = MibTableColumn
ntwsTraplogVarIpAddressVal = _NtwsTraplogVarIpAddressVal_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 10),
    _NtwsTraplogVarIpAddressVal_Type()
)
ntwsTraplogVarIpAddressVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarIpAddressVal.setStatus("current")
_NtwsTraplogVarOidVal_Type = ObjectIdentifier
_NtwsTraplogVarOidVal_Object = MibTableColumn
ntwsTraplogVarOidVal = _NtwsTraplogVarOidVal_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 11),
    _NtwsTraplogVarOidVal_Type()
)
ntwsTraplogVarOidVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarOidVal.setStatus("current")
_NtwsTraplogVarCounter64Val_Type = Counter64
_NtwsTraplogVarCounter64Val_Object = MibTableColumn
ntwsTraplogVarCounter64Val = _NtwsTraplogVarCounter64Val_Object(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 1, 4, 1, 12),
    _NtwsTraplogVarCounter64Val_Type()
)
ntwsTraplogVarCounter64Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntwsTraplogVarCounter64Val.setStatus("current")
_NtwsTraplogConformance_ObjectIdentity = ObjectIdentity
ntwsTraplogConformance = _NtwsTraplogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2)
)
_NtwsTraplogCompliances_ObjectIdentity = ObjectIdentity
ntwsTraplogCompliances = _NtwsTraplogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 1)
)
_NtwsTraplogGroups_ObjectIdentity = ObjectIdentity
ntwsTraplogGroups = _NtwsTraplogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2)
)

# Managed Objects groups

ntwsTraplogGuideGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 1)
)
ntwsTraplogGuideGroup.setObjects(
      *(("NTWS-TRAPLOG-MIB", "ntwsTraplogOldestTrapIndex"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogNewestTrapIndex"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogNewestTrapTime"))
)
if mibBuilder.loadTexts:
    ntwsTraplogGuideGroup.setStatus("current")

ntwsTraplogGuideDateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 2)
)
ntwsTraplogGuideDateGroup.setObjects(
    ("NTWS-TRAPLOG-MIB", "ntwsTraplogNewestTrapDateAndTime")
)
if mibBuilder.loadTexts:
    ntwsTraplogGuideDateGroup.setStatus("current")

ntwsTraplogTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 3)
)
ntwsTraplogTrapGroup.setObjects(
      *(("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapTime"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapNotificationID"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapNumVars"))
)
if mibBuilder.loadTexts:
    ntwsTraplogTrapGroup.setStatus("current")

ntwsTraplogTrapDateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 4)
)
ntwsTraplogTrapDateGroup.setObjects(
    ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapDateAndTime")
)
if mibBuilder.loadTexts:
    ntwsTraplogTrapDateGroup.setStatus("current")

ntwsTraplogVarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 2, 5)
)
ntwsTraplogVarGroup.setObjects(
      *(("NTWS-TRAPLOG-MIB", "ntwsTraplogVarID"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarValueType"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarCounter32Val"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarUnsigned32Val"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarTimeTicksVal"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarInteger32Val"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarOctetStringVal"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarIpAddressVal"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarOidVal"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarCounter64Val"))
)
if mibBuilder.loadTexts:
    ntwsTraplogVarGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntwsTraplogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 13, 2, 1, 1)
)
ntwsTraplogCompliance.setObjects(
      *(("NTWS-TRAPLOG-MIB", "ntwsTraplogGuideGroup"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapGroup"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogVarGroup"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogGuideDateGroup"),
        ("NTWS-TRAPLOG-MIB", "ntwsTraplogTrapDateGroup"))
)
if mibBuilder.loadTexts:
    ntwsTraplogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-TRAPLOG-MIB",
    **{"NtwsTraplogTrapOccurrenceIndex": NtwsTraplogTrapOccurrenceIndex,
       "NtwsTraplogTrapOccurrenceIndexOrZero": NtwsTraplogTrapOccurrenceIndexOrZero,
       "ntwsTraplogMib": ntwsTraplogMib,
       "ntwsTraplogMibObjects": ntwsTraplogMibObjects,
       "ntwsTraplogGuideObjects": ntwsTraplogGuideObjects,
       "ntwsTraplogOldestTrapIndex": ntwsTraplogOldestTrapIndex,
       "ntwsTraplogNewestTrapIndex": ntwsTraplogNewestTrapIndex,
       "ntwsTraplogNewestTrapTime": ntwsTraplogNewestTrapTime,
       "ntwsTraplogNewestTrapDateAndTime": ntwsTraplogNewestTrapDateAndTime,
       "ntwsTraplogTrapTable": ntwsTraplogTrapTable,
       "ntwsTraplogTrapEntry": ntwsTraplogTrapEntry,
       "ntwsTraplogTrapIndex": ntwsTraplogTrapIndex,
       "ntwsTraplogTrapTime": ntwsTraplogTrapTime,
       "ntwsTraplogTrapDateAndTime": ntwsTraplogTrapDateAndTime,
       "ntwsTraplogTrapNotificationID": ntwsTraplogTrapNotificationID,
       "ntwsTraplogTrapNumVars": ntwsTraplogTrapNumVars,
       "ntwsTraplogVarTable": ntwsTraplogVarTable,
       "ntwsTraplogVarEntry": ntwsTraplogVarEntry,
       "ntwsTraplogVarTrapIndex": ntwsTraplogVarTrapIndex,
       "ntwsTraplogVarIndex": ntwsTraplogVarIndex,
       "ntwsTraplogVarID": ntwsTraplogVarID,
       "ntwsTraplogVarValueType": ntwsTraplogVarValueType,
       "ntwsTraplogVarCounter32Val": ntwsTraplogVarCounter32Val,
       "ntwsTraplogVarUnsigned32Val": ntwsTraplogVarUnsigned32Val,
       "ntwsTraplogVarTimeTicksVal": ntwsTraplogVarTimeTicksVal,
       "ntwsTraplogVarInteger32Val": ntwsTraplogVarInteger32Val,
       "ntwsTraplogVarOctetStringVal": ntwsTraplogVarOctetStringVal,
       "ntwsTraplogVarIpAddressVal": ntwsTraplogVarIpAddressVal,
       "ntwsTraplogVarOidVal": ntwsTraplogVarOidVal,
       "ntwsTraplogVarCounter64Val": ntwsTraplogVarCounter64Val,
       "ntwsTraplogConformance": ntwsTraplogConformance,
       "ntwsTraplogCompliances": ntwsTraplogCompliances,
       "ntwsTraplogCompliance": ntwsTraplogCompliance,
       "ntwsTraplogGroups": ntwsTraplogGroups,
       "ntwsTraplogGuideGroup": ntwsTraplogGuideGroup,
       "ntwsTraplogGuideDateGroup": ntwsTraplogGuideDateGroup,
       "ntwsTraplogTrapGroup": ntwsTraplogTrapGroup,
       "ntwsTraplogTrapDateGroup": ntwsTraplogTrapDateGroup,
       "ntwsTraplogVarGroup": ntwsTraplogVarGroup}
)
