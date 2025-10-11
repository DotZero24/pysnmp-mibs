# SNMP MIB module (NEWTEC-REFERENCECLOCK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-REFERENCECLOCK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:54 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState")

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

ntcReferenceClock = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300)
)
if mibBuilder.loadTexts:
    ntcReferenceClock.setRevisions(
        ("2013-09-20 08:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcRefClkObjects_ObjectIdentity = ObjectIdentity
ntcRefClkObjects = _NtcRefClkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1)
)
if mibBuilder.loadTexts:
    ntcRefClkObjects.setStatus("current")


class _NtcRefClkRefSelection_Type(Integer32):
    """Custom type ntcRefClkRefSelection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("external", 1))
    )


_NtcRefClkRefSelection_Type.__name__ = "Integer32"
_NtcRefClkRefSelection_Object = MibScalar
ntcRefClkRefSelection = _NtcRefClkRefSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 1),
    _NtcRefClkRefSelection_Type()
)
ntcRefClkRefSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcRefClkRefSelection.setStatus("current")


class _NtcRefClkExtRefFrequency_Type(Integer32):
    """Custom type ntcRefClkExtRefFrequency based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1Mhz", 0),
          ("e2Mhz", 1),
          ("e5Mhz", 3),
          ("e10Mhz", 4),
          ("e20Mhz", 5))
    )


_NtcRefClkExtRefFrequency_Type.__name__ = "Integer32"
_NtcRefClkExtRefFrequency_Object = MibScalar
ntcRefClkExtRefFrequency = _NtcRefClkExtRefFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 2),
    _NtcRefClkExtRefFrequency_Type()
)
ntcRefClkExtRefFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcRefClkExtRefFrequency.setStatus("current")
_NtcRefClkAlarm_ObjectIdentity = ObjectIdentity
ntcRefClkAlarm = _NtcRefClkAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 3)
)
if mibBuilder.loadTexts:
    ntcRefClkAlarm.setStatus("current")
_NtcRefClkAlmRefClockNoSignal_Type = NtcAlarmState
_NtcRefClkAlmRefClockNoSignal_Object = MibScalar
ntcRefClkAlmRefClockNoSignal = _NtcRefClkAlmRefClockNoSignal_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 3, 1),
    _NtcRefClkAlmRefClockNoSignal_Type()
)
ntcRefClkAlmRefClockNoSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRefClkAlmRefClockNoSignal.setStatus("current")
_NtcRefClkAlmRefClockNoLock_Type = NtcAlarmState
_NtcRefClkAlmRefClockNoLock_Object = MibScalar
ntcRefClkAlmRefClockNoLock = _NtcRefClkAlmRefClockNoLock_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 3, 2),
    _NtcRefClkAlmRefClockNoLock_Type()
)
ntcRefClkAlmRefClockNoLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRefClkAlmRefClockNoLock.setStatus("current")


class _NtcRefClkActiveRef_Type(Integer32):
    """Custom type ntcRefClkActiveRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("external", 1))
    )


_NtcRefClkActiveRef_Type.__name__ = "Integer32"
_NtcRefClkActiveRef_Object = MibScalar
ntcRefClkActiveRef = _NtcRefClkActiveRef_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 1, 4),
    _NtcRefClkActiveRef_Type()
)
ntcRefClkActiveRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcRefClkActiveRef.setStatus("current")
_NtcRefClkConformance_ObjectIdentity = ObjectIdentity
ntcRefClkConformance = _NtcRefClkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2)
)
if mibBuilder.loadTexts:
    ntcRefClkConformance.setStatus("current")
_NtcRefClkConfCompliance_ObjectIdentity = ObjectIdentity
ntcRefClkConfCompliance = _NtcRefClkConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 1)
)
if mibBuilder.loadTexts:
    ntcRefClkConfCompliance.setStatus("current")
_NtcRefClkConfGroup_ObjectIdentity = ObjectIdentity
ntcRefClkConfGroup = _NtcRefClkConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 2)
)
if mibBuilder.loadTexts:
    ntcRefClkConfGroup.setStatus("current")

# Managed Objects groups

ntcRefClkConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 2, 1)
)
ntcRefClkConfGrpV1Standard.setObjects(
      *(("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkRefSelection"),
        ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkExtRefFrequency"),
        ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkAlmRefClockNoSignal"),
        ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkAlmRefClockNoLock"),
        ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkActiveRef"))
)
if mibBuilder.loadTexts:
    ntcRefClkConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcRefClkConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 300, 2, 1, 1)
)
ntcRefClkConfCompV1Standard.setObjects(
    ("NEWTEC-REFERENCECLOCK-MIB", "ntcRefClkConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcRefClkConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-REFERENCECLOCK-MIB",
    **{"ntcReferenceClock": ntcReferenceClock,
       "ntcRefClkObjects": ntcRefClkObjects,
       "ntcRefClkRefSelection": ntcRefClkRefSelection,
       "ntcRefClkExtRefFrequency": ntcRefClkExtRefFrequency,
       "ntcRefClkAlarm": ntcRefClkAlarm,
       "ntcRefClkAlmRefClockNoSignal": ntcRefClkAlmRefClockNoSignal,
       "ntcRefClkAlmRefClockNoLock": ntcRefClkAlmRefClockNoLock,
       "ntcRefClkActiveRef": ntcRefClkActiveRef,
       "ntcRefClkConformance": ntcRefClkConformance,
       "ntcRefClkConfCompliance": ntcRefClkConfCompliance,
       "ntcRefClkConfCompV1Standard": ntcRefClkConfCompV1Standard,
       "ntcRefClkConfGroup": ntcRefClkConfGroup,
       "ntcRefClkConfGrpV1Standard": ntcRefClkConfGrpV1Standard}
)
