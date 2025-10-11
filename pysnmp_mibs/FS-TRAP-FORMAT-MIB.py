# SNMP MIB module (FS-TRAP-FORMAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-TRAP-FORMAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:46 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

fsTrapFormatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97)
)
if mibBuilder.loadTexts:
    fsTrapFormatMIB.setRevisions(
        ("2011-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTrapFormatMIBObjects_ObjectIdentity = ObjectIdentity
fsTrapFormatMIBObjects = _FsTrapFormatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1)
)


class _FsTrapFormatTrapSerialNo_Type(DisplayString):
    """Custom type fsTrapFormatTrapSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsTrapFormatTrapSerialNo_Type.__name__ = "DisplayString"
_FsTrapFormatTrapSerialNo_Object = MibScalar
fsTrapFormatTrapSerialNo = _FsTrapFormatTrapSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 1),
    _FsTrapFormatTrapSerialNo_Type()
)
fsTrapFormatTrapSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapSerialNo.setStatus("current")


class _FsTrapFormatTrapLevel_Type(DisplayString):
    """Custom type fsTrapFormatTrapLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsTrapFormatTrapLevel_Type.__name__ = "DisplayString"
_FsTrapFormatTrapLevel_Object = MibScalar
fsTrapFormatTrapLevel = _FsTrapFormatTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 2),
    _FsTrapFormatTrapLevel_Type()
)
fsTrapFormatTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapLevel.setStatus("current")


class _FsTrapFormatTrapType_Type(DisplayString):
    """Custom type fsTrapFormatTrapType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsTrapFormatTrapType_Type.__name__ = "DisplayString"
_FsTrapFormatTrapType_Object = MibScalar
fsTrapFormatTrapType = _FsTrapFormatTrapType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 3),
    _FsTrapFormatTrapType_Type()
)
fsTrapFormatTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapType.setStatus("current")
_FsTrapFormatTrapReasonNo_Type = Integer32
_FsTrapFormatTrapReasonNo_Object = MibScalar
fsTrapFormatTrapReasonNo = _FsTrapFormatTrapReasonNo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 4),
    _FsTrapFormatTrapReasonNo_Type()
)
fsTrapFormatTrapReasonNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapReasonNo.setStatus("current")


class _FsTrapFormatTrapReasons_Type(DisplayString):
    """Custom type fsTrapFormatTrapReasons based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsTrapFormatTrapReasons_Type.__name__ = "DisplayString"
_FsTrapFormatTrapReasons_Object = MibScalar
fsTrapFormatTrapReasons = _FsTrapFormatTrapReasons_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 5),
    _FsTrapFormatTrapReasons_Type()
)
fsTrapFormatTrapReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapReasons.setStatus("current")
_FsTrapFormatTrapStatus_Type = Integer32
_FsTrapFormatTrapStatus_Object = MibScalar
fsTrapFormatTrapStatus = _FsTrapFormatTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 6),
    _FsTrapFormatTrapStatus_Type()
)
fsTrapFormatTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapStatus.setStatus("current")


class _FsTrapFormatTrapTitle_Type(DisplayString):
    """Custom type fsTrapFormatTrapTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsTrapFormatTrapTitle_Type.__name__ = "DisplayString"
_FsTrapFormatTrapTitle_Object = MibScalar
fsTrapFormatTrapTitle = _FsTrapFormatTrapTitle_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 7),
    _FsTrapFormatTrapTitle_Type()
)
fsTrapFormatTrapTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapTitle.setStatus("current")


class _FsTrapFormatTrapContent_Type(DisplayString):
    """Custom type fsTrapFormatTrapContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsTrapFormatTrapContent_Type.__name__ = "DisplayString"
_FsTrapFormatTrapContent_Object = MibScalar
fsTrapFormatTrapContent = _FsTrapFormatTrapContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 8),
    _FsTrapFormatTrapContent_Type()
)
fsTrapFormatTrapContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapContent.setStatus("current")
_FsTrapFormatTrapTime_Type = Counter32
_FsTrapFormatTrapTime_Object = MibScalar
fsTrapFormatTrapTime = _FsTrapFormatTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 9),
    _FsTrapFormatTrapTime_Type()
)
fsTrapFormatTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapTime.setStatus("current")
_FsTrapFormatTrapSlotInfo_Type = DisplayString
_FsTrapFormatTrapSlotInfo_Object = MibScalar
fsTrapFormatTrapSlotInfo = _FsTrapFormatTrapSlotInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 10),
    _FsTrapFormatTrapSlotInfo_Type()
)
fsTrapFormatTrapSlotInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapSlotInfo.setStatus("current")
_FsTrapFormatTrapVendorId_Type = Integer32
_FsTrapFormatTrapVendorId_Object = MibScalar
fsTrapFormatTrapVendorId = _FsTrapFormatTrapVendorId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 11),
    _FsTrapFormatTrapVendorId_Type()
)
fsTrapFormatTrapVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapVendorId.setStatus("current")


class _FsTrapFormatTrapSerialNum_Type(DisplayString):
    """Custom type fsTrapFormatTrapSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsTrapFormatTrapSerialNum_Type.__name__ = "DisplayString"
_FsTrapFormatTrapSerialNum_Object = MibScalar
fsTrapFormatTrapSerialNum = _FsTrapFormatTrapSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 12),
    _FsTrapFormatTrapSerialNum_Type()
)
fsTrapFormatTrapSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapSerialNum.setStatus("current")


class _FsTrapFormatTrapDateTime_Type(DisplayString):
    """Custom type fsTrapFormatTrapDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsTrapFormatTrapDateTime_Type.__name__ = "DisplayString"
_FsTrapFormatTrapDateTime_Object = MibScalar
fsTrapFormatTrapDateTime = _FsTrapFormatTrapDateTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 1, 13),
    _FsTrapFormatTrapDateTime_Type()
)
fsTrapFormatTrapDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapFormatTrapDateTime.setStatus("current")
_FsTrapFormatMIBConformance_ObjectIdentity = ObjectIdentity
fsTrapFormatMIBConformance = _FsTrapFormatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 2)
)
_FsTrapFormatMIBCompliances_ObjectIdentity = ObjectIdentity
fsTrapFormatMIBCompliances = _FsTrapFormatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 2, 1)
)
_FsTrapFormatMIBGroups_ObjectIdentity = ObjectIdentity
fsTrapFormatMIBGroups = _FsTrapFormatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 2, 2)
)

# Managed Objects groups

fsTrapFormatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 2, 2, 1)
)
fsTrapFormatMIBGroup.setObjects(
      *(("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapSerialNo"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapLevel"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapType"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapReasonNo"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapReasons"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapStatus"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapTitle"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapContent"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapTime"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapSlotInfo"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapVendorId"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapSerialNum"),
        ("FS-TRAP-FORMAT-MIB", "fsTrapFormatTrapDateTime"))
)
if mibBuilder.loadTexts:
    fsTrapFormatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsTrapFormatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 97, 2, 1, 1)
)
fsTrapFormatMIBCompliance.setObjects(
    ("FS-TRAP-FORMAT-MIB", "fsTrapFormatMIBGroup")
)
if mibBuilder.loadTexts:
    fsTrapFormatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-TRAP-FORMAT-MIB",
    **{"fsTrapFormatMIB": fsTrapFormatMIB,
       "fsTrapFormatMIBObjects": fsTrapFormatMIBObjects,
       "fsTrapFormatTrapSerialNo": fsTrapFormatTrapSerialNo,
       "fsTrapFormatTrapLevel": fsTrapFormatTrapLevel,
       "fsTrapFormatTrapType": fsTrapFormatTrapType,
       "fsTrapFormatTrapReasonNo": fsTrapFormatTrapReasonNo,
       "fsTrapFormatTrapReasons": fsTrapFormatTrapReasons,
       "fsTrapFormatTrapStatus": fsTrapFormatTrapStatus,
       "fsTrapFormatTrapTitle": fsTrapFormatTrapTitle,
       "fsTrapFormatTrapContent": fsTrapFormatTrapContent,
       "fsTrapFormatTrapTime": fsTrapFormatTrapTime,
       "fsTrapFormatTrapSlotInfo": fsTrapFormatTrapSlotInfo,
       "fsTrapFormatTrapVendorId": fsTrapFormatTrapVendorId,
       "fsTrapFormatTrapSerialNum": fsTrapFormatTrapSerialNum,
       "fsTrapFormatTrapDateTime": fsTrapFormatTrapDateTime,
       "fsTrapFormatMIBConformance": fsTrapFormatMIBConformance,
       "fsTrapFormatMIBCompliances": fsTrapFormatMIBCompliances,
       "fsTrapFormatMIBCompliance": fsTrapFormatMIBCompliance,
       "fsTrapFormatMIBGroups": fsTrapFormatMIBGroups,
       "fsTrapFormatMIBGroup": fsTrapFormatMIBGroup}
)
