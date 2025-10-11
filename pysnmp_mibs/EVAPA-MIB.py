# SNMP MIB module (EVAPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/EVAPA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:34 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_Hpevapa_ObjectIdentity = ObjectIdentity
hpevapa = _Hpevapa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 175)
)
_Hpevent_ObjectIdentity = ObjectIdentity
hpevent = _Hpevent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 175, 1)
)
_HpevapaTraps_ObjectIdentity = ObjectIdentity
hpevapaTraps = _HpevapaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1)
)
_HpevapaServer_Type = DisplayString
_HpevapaServer_Object = MibScalar
hpevapaServer = _HpevapaServer_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 1),
    _HpevapaServer_Type()
)
hpevapaServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaServer.setStatus("mandatory")
_HpevapaSequence_Number_Type = OctetString
_HpevapaSequence_Number_Object = MibScalar
hpevapaSequence_Number = _HpevapaSequence_Number_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 2),
    _HpevapaSequence_Number_Type()
)
hpevapaSequence_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaSequence_Number.setStatus("mandatory")
_HpevapaEvent_Code_Type = Integer32
_HpevapaEvent_Code_Object = MibScalar
hpevapaEvent_Code = _HpevapaEvent_Code_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 3),
    _HpevapaEvent_Code_Type()
)
hpevapaEvent_Code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaEvent_Code.setStatus("mandatory")
_HpevapaCategory_Type = OctetString
_HpevapaCategory_Object = MibScalar
hpevapaCategory = _HpevapaCategory_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 4),
    _HpevapaCategory_Type()
)
hpevapaCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaCategory.setStatus("mandatory")
_HpevapaTime_Detect_Type = DisplayString
_HpevapaTime_Detect_Object = MibScalar
hpevapaTime_Detect = _HpevapaTime_Detect_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 5),
    _HpevapaTime_Detect_Type()
)
hpevapaTime_Detect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaTime_Detect.setStatus("mandatory")
_HpevapaSeverity_Type = DisplayString
_HpevapaSeverity_Object = MibScalar
hpevapaSeverity = _HpevapaSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 6),
    _HpevapaSeverity_Type()
)
hpevapaSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaSeverity.setStatus("mandatory")
_HpevapaArray_ID_Type = OctetString
_HpevapaArray_ID_Object = MibScalar
hpevapaArray_ID = _HpevapaArray_ID_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 7),
    _HpevapaArray_ID_Type()
)
hpevapaArray_ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaArray_ID.setStatus("mandatory")
_HpevapaArray_Name_Type = OctetString
_HpevapaArray_Name_Object = MibScalar
hpevapaArray_Name = _HpevapaArray_Name_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 8),
    _HpevapaArray_Name_Type()
)
hpevapaArray_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaArray_Name.setStatus("mandatory")
_HpevapaObject_ID_Type = OctetString
_HpevapaObject_ID_Object = MibScalar
hpevapaObject_ID = _HpevapaObject_ID_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 9),
    _HpevapaObject_ID_Type()
)
hpevapaObject_ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaObject_ID.setStatus("mandatory")
_HpevapaObject_Type_Type = OctetString
_HpevapaObject_Type_Object = MibScalar
hpevapaObject_Type = _HpevapaObject_Type_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 10),
    _HpevapaObject_Type_Type()
)
hpevapaObject_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaObject_Type.setStatus("mandatory")
_HpevapaObject_Name_Type = OctetString
_HpevapaObject_Name_Object = MibScalar
hpevapaObject_Name = _HpevapaObject_Name_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 11),
    _HpevapaObject_Name_Type()
)
hpevapaObject_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaObject_Name.setStatus("mandatory")
_HpevapaCounter_Name_Type = OctetString
_HpevapaCounter_Name_Object = MibScalar
hpevapaCounter_Name = _HpevapaCounter_Name_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 12),
    _HpevapaCounter_Name_Type()
)
hpevapaCounter_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaCounter_Name.setStatus("mandatory")
_HpevapaDetect_Level_Type = OctetString
_HpevapaDetect_Level_Object = MibScalar
hpevapaDetect_Level = _HpevapaDetect_Level_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 13),
    _HpevapaDetect_Level_Type()
)
hpevapaDetect_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaDetect_Level.setStatus("mandatory")
_HpevapaActual_Value_Type = OctetString
_HpevapaActual_Value_Object = MibScalar
hpevapaActual_Value = _HpevapaActual_Value_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 14),
    _HpevapaActual_Value_Type()
)
hpevapaActual_Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaActual_Value.setStatus("mandatory")
_HpevapaThreshold_Value_Type = OctetString
_HpevapaThreshold_Value_Object = MibScalar
hpevapaThreshold_Value = _HpevapaThreshold_Value_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 15),
    _HpevapaThreshold_Value_Type()
)
hpevapaThreshold_Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaThreshold_Value.setStatus("mandatory")
_HpevapaDescription_Type = OctetString
_HpevapaDescription_Object = MibScalar
hpevapaDescription = _HpevapaDescription_Object(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 16),
    _HpevapaDescription_Type()
)
hpevapaDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpevapaDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hpevapaAlarmsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 175, 1, 1, 0, 4)
)
hpevapaAlarmsTrap.setObjects(
      *(("EVAPA-MIB", "hpevapaServer"),
        ("EVAPA-MIB", "hpevapaSequence_Number"),
        ("EVAPA-MIB", "hpevapaEvent_Code"),
        ("EVAPA-MIB", "hpevapaCategory"),
        ("EVAPA-MIB", "hpevapaTime_Detect"),
        ("EVAPA-MIB", "hpevapaSeverity"),
        ("EVAPA-MIB", "hpevapaArray_ID"),
        ("EVAPA-MIB", "hpevapaArray_Name"),
        ("EVAPA-MIB", "hpevapaObject_ID"),
        ("EVAPA-MIB", "hpevapaObject_Type"),
        ("EVAPA-MIB", "hpevapaObject_Name"),
        ("EVAPA-MIB", "hpevapaCounter_Name"),
        ("EVAPA-MIB", "hpevapaDetect_Level"),
        ("EVAPA-MIB", "hpevapaActual_Value"),
        ("EVAPA-MIB", "hpevapaThreshold_Value"),
        ("EVAPA-MIB", "hpevapaDescription"))
)
if mibBuilder.loadTexts:
    hpevapaAlarmsTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EVAPA-MIB",
    **{"hp": hp,
       "hpevapa": hpevapa,
       "hpevent": hpevent,
       "hpevapaTraps": hpevapaTraps,
       "hpevapaAlarmsTrap": hpevapaAlarmsTrap,
       "hpevapaServer": hpevapaServer,
       "hpevapaSequence_Number": hpevapaSequence_Number,
       "hpevapaEvent_Code": hpevapaEvent_Code,
       "hpevapaCategory": hpevapaCategory,
       "hpevapaTime_Detect": hpevapaTime_Detect,
       "hpevapaSeverity": hpevapaSeverity,
       "hpevapaArray_ID": hpevapaArray_ID,
       "hpevapaArray_Name": hpevapaArray_Name,
       "hpevapaObject_ID": hpevapaObject_ID,
       "hpevapaObject_Type": hpevapaObject_Type,
       "hpevapaObject_Name": hpevapaObject_Name,
       "hpevapaCounter_Name": hpevapaCounter_Name,
       "hpevapaDetect_Level": hpevapaDetect_Level,
       "hpevapaActual_Value": hpevapaActual_Value,
       "hpevapaThreshold_Value": hpevapaThreshold_Value,
       "hpevapaDescription": hpevapaDescription}
)
