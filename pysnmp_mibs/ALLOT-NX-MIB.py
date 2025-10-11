# SNMP MIB module (ALLOT-NX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allot/ALLOT-NX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:57 2025
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

(alRegMIB,) = mibBuilder.importSymbols(
    "ALLOT-MIB",
    "alRegMIB")

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

alNXMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 10)
)
if mibBuilder.loadTexts:
    alNXMIB.setRevisions(
        ("2008-12-10 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlEvents_ObjectIdentity = ObjectIdentity
alEvents = _AlEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 10, 0)
)
_AlObjects_ObjectIdentity = ObjectIdentity
alObjects = _AlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2)
)
_AlAlarmTable_Object = MibTable
alAlarmTable = _AlAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1)
)
if mibBuilder.loadTexts:
    alAlarmTable.setStatus("current")
_AlEntry_Object = MibTableRow
alEntry = _AlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1)
)
alEntry.setIndexNames(
    (0, "ALLOT-NX-MIB", "alDeviceIp"),
    (0, "ALLOT-NX-MIB", "alAlarmType"),
    (0, "ALLOT-NX-MIB", "alCardId"),
    (0, "ALLOT-NX-MIB", "alSourceId"),
    (0, "ALLOT-NX-MIB", "alTcaId"),
)
if mibBuilder.loadTexts:
    alEntry.setStatus("current")
_AlDeviceIp_Type = IpAddress
_AlDeviceIp_Object = MibTableColumn
alDeviceIp = _AlDeviceIp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 1),
    _AlDeviceIp_Type()
)
alDeviceIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alDeviceIp.setStatus("current")
_AlAlarmType_Type = Unsigned32
_AlAlarmType_Object = MibTableColumn
alAlarmType = _AlAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 2),
    _AlAlarmType_Type()
)
alAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alAlarmType.setStatus("current")
_AlCardId_Type = Unsigned32
_AlCardId_Object = MibTableColumn
alCardId = _AlCardId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 3),
    _AlCardId_Type()
)
alCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alCardId.setStatus("current")
_AlSourceId_Type = Unsigned32
_AlSourceId_Object = MibTableColumn
alSourceId = _AlSourceId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 4),
    _AlSourceId_Type()
)
alSourceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alSourceId.setStatus("current")
_AlTcaId_Type = Unsigned32
_AlTcaId_Object = MibTableColumn
alTcaId = _AlTcaId_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 5),
    _AlTcaId_Type()
)
alTcaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alTcaId.setStatus("current")


class _AlSeverity_Type(Integer32):
    """Custom type alSeverity based on Integer32"""
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
        *(("unknown", 0),
          ("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_AlSeverity_Type.__name__ = "Integer32"
_AlSeverity_Object = MibTableColumn
alSeverity = _AlSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 6),
    _AlSeverity_Type()
)
alSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alSeverity.setStatus("current")
_AlDescription_Type = OctetString
_AlDescription_Object = MibTableColumn
alDescription = _AlDescription_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 7),
    _AlDescription_Type()
)
alDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alDescription.setStatus("current")
_AlTimestamp_Type = Counter64
_AlTimestamp_Object = MibTableColumn
alTimestamp = _AlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 8),
    _AlTimestamp_Type()
)
alTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTimestamp.setStatus("current")
_AlIndex_Type = OctetString
_AlIndex_Object = MibTableColumn
alIndex = _AlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 1, 1, 9),
    _AlIndex_Type()
)
alIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alIndex.setStatus("current")
_AlTrapCounter_Type = Counter32
_AlTrapCounter_Object = MibScalar
alTrapCounter = _AlTrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 2603, 10, 2, 2),
    _AlTrapCounter_Type()
)
alTrapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alTrapCounter.setStatus("current")
_AlConf_ObjectIdentity = ObjectIdentity
alConf = _AlConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 10, 3)
)
_AlGroups_ObjectIdentity = ObjectIdentity
alGroups = _AlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 10, 3, 1)
)
_AlCompls_ObjectIdentity = ObjectIdentity
alCompls = _AlCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 10, 3, 2)
)

# Managed Objects groups

alBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 10, 3, 1, 1)
)
alBasicGroup.setObjects(
      *(("ALLOT-NX-MIB", "alSeverity"),
        ("ALLOT-NX-MIB", "alDescription"),
        ("ALLOT-NX-MIB", "alTrapCounter"),
        ("ALLOT-NX-MIB", "alTimestamp"),
        ("ALLOT-NX-MIB", "alIndex"))
)
if mibBuilder.loadTexts:
    alBasicGroup.setStatus("current")


# Notification objects

alAlarmRisingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 10, 0, 1)
)
alAlarmRisingTrap.setObjects(
      *(("ALLOT-NX-MIB", "alSeverity"),
        ("ALLOT-NX-MIB", "alDescription"),
        ("ALLOT-NX-MIB", "alTimestamp"),
        ("ALLOT-NX-MIB", "alIndex"))
)
if mibBuilder.loadTexts:
    alAlarmRisingTrap.setStatus(
        "current"
    )

alAlarmFallingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2603, 10, 0, 2)
)
alAlarmFallingTrap.setObjects(
      *(("ALLOT-NX-MIB", "alSeverity"),
        ("ALLOT-NX-MIB", "alDescription"),
        ("ALLOT-NX-MIB", "alTimestamp"),
        ("ALLOT-NX-MIB", "alIndex"))
)
if mibBuilder.loadTexts:
    alAlarmFallingTrap.setStatus(
        "current"
    )


# Notifications groups

alBasicEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2603, 10, 3, 1, 2)
)
alBasicEvents.setObjects(
      *(("ALLOT-NX-MIB", "alAlarmRisingTrap"),
        ("ALLOT-NX-MIB", "alAlarmFallingTrap"))
)
if mibBuilder.loadTexts:
    alBasicEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALLOT-NX-MIB",
    **{"alNXMIB": alNXMIB,
       "alEvents": alEvents,
       "alAlarmRisingTrap": alAlarmRisingTrap,
       "alAlarmFallingTrap": alAlarmFallingTrap,
       "alObjects": alObjects,
       "alAlarmTable": alAlarmTable,
       "alEntry": alEntry,
       "alDeviceIp": alDeviceIp,
       "alAlarmType": alAlarmType,
       "alCardId": alCardId,
       "alSourceId": alSourceId,
       "alTcaId": alTcaId,
       "alSeverity": alSeverity,
       "alDescription": alDescription,
       "alTimestamp": alTimestamp,
       "alIndex": alIndex,
       "alTrapCounter": alTrapCounter,
       "alConf": alConf,
       "alGroups": alGroups,
       "alBasicGroup": alBasicGroup,
       "alBasicEvents": alBasicEvents,
       "alCompls": alCompls}
)
