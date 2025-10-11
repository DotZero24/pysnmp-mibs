# SNMP MIB module (QTECH-TRAP-FORMAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-TRAP-FORMAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:01 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechTrapFormatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97)
)
if mibBuilder.loadTexts:
    qtechTrapFormatMIB.setRevisions(
        ("2011-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechTrapFormatMIBObjects_ObjectIdentity = ObjectIdentity
qtechTrapFormatMIBObjects = _QtechTrapFormatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1)
)


class _QtechTrapFormatTrapSerialNo_Type(DisplayString):
    """Custom type qtechTrapFormatTrapSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechTrapFormatTrapSerialNo_Type.__name__ = "DisplayString"
_QtechTrapFormatTrapSerialNo_Object = MibScalar
qtechTrapFormatTrapSerialNo = _QtechTrapFormatTrapSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 1),
    _QtechTrapFormatTrapSerialNo_Type()
)
qtechTrapFormatTrapSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapSerialNo.setStatus("current")


class _QtechTrapFormatTrapLevel_Type(DisplayString):
    """Custom type qtechTrapFormatTrapLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechTrapFormatTrapLevel_Type.__name__ = "DisplayString"
_QtechTrapFormatTrapLevel_Object = MibScalar
qtechTrapFormatTrapLevel = _QtechTrapFormatTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 2),
    _QtechTrapFormatTrapLevel_Type()
)
qtechTrapFormatTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapLevel.setStatus("current")


class _QtechTrapFormatTrapType_Type(DisplayString):
    """Custom type qtechTrapFormatTrapType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_QtechTrapFormatTrapType_Type.__name__ = "DisplayString"
_QtechTrapFormatTrapType_Object = MibScalar
qtechTrapFormatTrapType = _QtechTrapFormatTrapType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 3),
    _QtechTrapFormatTrapType_Type()
)
qtechTrapFormatTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapType.setStatus("current")
_QtechTrapFormatTrapReasonNo_Type = Integer32
_QtechTrapFormatTrapReasonNo_Object = MibScalar
qtechTrapFormatTrapReasonNo = _QtechTrapFormatTrapReasonNo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 4),
    _QtechTrapFormatTrapReasonNo_Type()
)
qtechTrapFormatTrapReasonNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapReasonNo.setStatus("current")


class _QtechTrapFormatTrapReasons_Type(DisplayString):
    """Custom type qtechTrapFormatTrapReasons based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechTrapFormatTrapReasons_Type.__name__ = "DisplayString"
_QtechTrapFormatTrapReasons_Object = MibScalar
qtechTrapFormatTrapReasons = _QtechTrapFormatTrapReasons_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 5),
    _QtechTrapFormatTrapReasons_Type()
)
qtechTrapFormatTrapReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapReasons.setStatus("current")
_QtechTrapFormatTrapStatus_Type = Integer32
_QtechTrapFormatTrapStatus_Object = MibScalar
qtechTrapFormatTrapStatus = _QtechTrapFormatTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 6),
    _QtechTrapFormatTrapStatus_Type()
)
qtechTrapFormatTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapStatus.setStatus("current")


class _QtechTrapFormatTrapTitle_Type(DisplayString):
    """Custom type qtechTrapFormatTrapTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechTrapFormatTrapTitle_Type.__name__ = "DisplayString"
_QtechTrapFormatTrapTitle_Object = MibScalar
qtechTrapFormatTrapTitle = _QtechTrapFormatTrapTitle_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 7),
    _QtechTrapFormatTrapTitle_Type()
)
qtechTrapFormatTrapTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapTitle.setStatus("current")


class _QtechTrapFormatTrapContent_Type(DisplayString):
    """Custom type qtechTrapFormatTrapContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechTrapFormatTrapContent_Type.__name__ = "DisplayString"
_QtechTrapFormatTrapContent_Object = MibScalar
qtechTrapFormatTrapContent = _QtechTrapFormatTrapContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 8),
    _QtechTrapFormatTrapContent_Type()
)
qtechTrapFormatTrapContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapContent.setStatus("current")
_QtechTrapFormatTrapTime_Type = Counter32
_QtechTrapFormatTrapTime_Object = MibScalar
qtechTrapFormatTrapTime = _QtechTrapFormatTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 9),
    _QtechTrapFormatTrapTime_Type()
)
qtechTrapFormatTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapTime.setStatus("current")
_QtechTrapFormatTrapSlotInfo_Type = DisplayString
_QtechTrapFormatTrapSlotInfo_Object = MibScalar
qtechTrapFormatTrapSlotInfo = _QtechTrapFormatTrapSlotInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 1, 10),
    _QtechTrapFormatTrapSlotInfo_Type()
)
qtechTrapFormatTrapSlotInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapFormatTrapSlotInfo.setStatus("current")
_QtechTrapFormatMIBConformance_ObjectIdentity = ObjectIdentity
qtechTrapFormatMIBConformance = _QtechTrapFormatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 2)
)
_QtechTrapFormatMIBCompliances_ObjectIdentity = ObjectIdentity
qtechTrapFormatMIBCompliances = _QtechTrapFormatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 2, 1)
)
_QtechTrapFormatMIBGroups_ObjectIdentity = ObjectIdentity
qtechTrapFormatMIBGroups = _QtechTrapFormatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 2, 2)
)

# Managed Objects groups

qtechTrapFormatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 2, 2, 1)
)
qtechTrapFormatMIBGroup.setObjects(
      *(("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapSerialNo"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapLevel"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapType"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapReasonNo"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapReasons"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapStatus"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapTitle"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapContent"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapTime"),
        ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatTrapSlotInfo"))
)
if mibBuilder.loadTexts:
    qtechTrapFormatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechTrapFormatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 97, 2, 1, 1)
)
qtechTrapFormatMIBCompliance.setObjects(
    ("QTECH-TRAP-FORMAT-MIB", "qtechTrapFormatMIBGroup")
)
if mibBuilder.loadTexts:
    qtechTrapFormatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-TRAP-FORMAT-MIB",
    **{"qtechTrapFormatMIB": qtechTrapFormatMIB,
       "qtechTrapFormatMIBObjects": qtechTrapFormatMIBObjects,
       "qtechTrapFormatTrapSerialNo": qtechTrapFormatTrapSerialNo,
       "qtechTrapFormatTrapLevel": qtechTrapFormatTrapLevel,
       "qtechTrapFormatTrapType": qtechTrapFormatTrapType,
       "qtechTrapFormatTrapReasonNo": qtechTrapFormatTrapReasonNo,
       "qtechTrapFormatTrapReasons": qtechTrapFormatTrapReasons,
       "qtechTrapFormatTrapStatus": qtechTrapFormatTrapStatus,
       "qtechTrapFormatTrapTitle": qtechTrapFormatTrapTitle,
       "qtechTrapFormatTrapContent": qtechTrapFormatTrapContent,
       "qtechTrapFormatTrapTime": qtechTrapFormatTrapTime,
       "qtechTrapFormatTrapSlotInfo": qtechTrapFormatTrapSlotInfo,
       "qtechTrapFormatMIBConformance": qtechTrapFormatMIBConformance,
       "qtechTrapFormatMIBCompliances": qtechTrapFormatMIBCompliances,
       "qtechTrapFormatMIBCompliance": qtechTrapFormatMIBCompliance,
       "qtechTrapFormatMIBGroups": qtechTrapFormatMIBGroups,
       "qtechTrapFormatMIBGroup": qtechTrapFormatMIBGroup}
)
