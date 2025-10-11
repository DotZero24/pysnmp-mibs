# SNMP MIB module (CRESTRON-IO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/crestron/CRESTRON-IO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:47 2025
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

(Digital,
 crestronControl) = mibBuilder.importSymbols(
    "CRESTRON-ROOT-MIB",
    "Digital",
    "crestronControl")

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

crestronIo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IoId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class Comparator(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("equals", 1),
          ("greaterThan", 2),
          ("lessThan", 3),
          ("greaterThanOrEqualTo", 4),
          ("lessThanOrEqualTo", 5),
          ("notEqualTo", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CrestronIoAdmin_ObjectIdentity = ObjectIdentity
crestronIoAdmin = _CrestronIoAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 1)
)
_CrestronIoNotifications_ObjectIdentity = ObjectIdentity
crestronIoNotifications = _CrestronIoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 2)
)
_CrestronIoDigitalTrapData_Type = Digital
_CrestronIoDigitalTrapData_Object = MibScalar
crestronIoDigitalTrapData = _CrestronIoDigitalTrapData_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 2, 2),
    _CrestronIoDigitalTrapData_Type()
)
crestronIoDigitalTrapData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crestronIoDigitalTrapData.setStatus("current")
_CrestronIoAnalogTrapData_Type = Integer32
_CrestronIoAnalogTrapData_Object = MibScalar
crestronIoAnalogTrapData = _CrestronIoAnalogTrapData_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 2, 3),
    _CrestronIoAnalogTrapData_Type()
)
crestronIoAnalogTrapData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crestronIoAnalogTrapData.setStatus("current")
_CrestronIoSerialTrapData_Type = OctetString
_CrestronIoSerialTrapData_Object = MibScalar
crestronIoSerialTrapData = _CrestronIoSerialTrapData_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 2, 4),
    _CrestronIoSerialTrapData_Type()
)
crestronIoSerialTrapData.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    crestronIoSerialTrapData.setStatus("current")
_CrestronIoObjects_ObjectIdentity = ObjectIdentity
crestronIoObjects = _CrestronIoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3)
)
_CrestronIoVersion_Type = Integer32
_CrestronIoVersion_Object = MibScalar
crestronIoVersion = _CrestronIoVersion_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 1),
    _CrestronIoVersion_Type()
)
crestronIoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoVersion.setStatus("current")
_CrestronIoDigital_ObjectIdentity = ObjectIdentity
crestronIoDigital = _CrestronIoDigital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2)
)
_CrestronIoDigitalReadWrite_ObjectIdentity = ObjectIdentity
crestronIoDigitalReadWrite = _CrestronIoDigitalReadWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1)
)
_CrestronIoDigitalReadWriteTable_Object = MibTable
crestronIoDigitalReadWriteTable = _CrestronIoDigitalReadWriteTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    crestronIoDigitalReadWriteTable.setStatus("current")
_CrestronIoDigitalReadWriteEntry_Object = MibTableRow
crestronIoDigitalReadWriteEntry = _CrestronIoDigitalReadWriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1, 1)
)
crestronIoDigitalReadWriteEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronIoDigitalReadWriteIoId"),
)
if mibBuilder.loadTexts:
    crestronIoDigitalReadWriteEntry.setStatus("current")
_CrestronIoDigitalReadWriteIoId_Type = IoId
_CrestronIoDigitalReadWriteIoId_Object = MibTableColumn
crestronIoDigitalReadWriteIoId = _CrestronIoDigitalReadWriteIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1, 1, 1),
    _CrestronIoDigitalReadWriteIoId_Type()
)
crestronIoDigitalReadWriteIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadWriteIoId.setStatus("current")
_CrestronIoDigitalReadWriteIoText_Type = DisplayString
_CrestronIoDigitalReadWriteIoText_Object = MibTableColumn
crestronIoDigitalReadWriteIoText = _CrestronIoDigitalReadWriteIoText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1, 1, 2),
    _CrestronIoDigitalReadWriteIoText_Type()
)
crestronIoDigitalReadWriteIoText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadWriteIoText.setStatus("current")


class _CrestronIoDigitalReadWriteValue_Type(Integer32):
    """Custom type crestronIoDigitalReadWriteValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CrestronIoDigitalReadWriteValue_Type.__name__ = "Integer32"
_CrestronIoDigitalReadWriteValue_Object = MibTableColumn
crestronIoDigitalReadWriteValue = _CrestronIoDigitalReadWriteValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1, 1, 3),
    _CrestronIoDigitalReadWriteValue_Type()
)
crestronIoDigitalReadWriteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronIoDigitalReadWriteValue.setStatus("current")
_CrestronIoDigitalReadWrite0Text_Type = DisplayString
_CrestronIoDigitalReadWrite0Text_Object = MibTableColumn
crestronIoDigitalReadWrite0Text = _CrestronIoDigitalReadWrite0Text_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1, 1, 4),
    _CrestronIoDigitalReadWrite0Text_Type()
)
crestronIoDigitalReadWrite0Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadWrite0Text.setStatus("current")
_CrestronIoDigitalReadWrite1Text_Type = DisplayString
_CrestronIoDigitalReadWrite1Text_Object = MibTableColumn
crestronIoDigitalReadWrite1Text = _CrestronIoDigitalReadWrite1Text_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 1, 1, 1, 5),
    _CrestronIoDigitalReadWrite1Text_Type()
)
crestronIoDigitalReadWrite1Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadWrite1Text.setStatus("current")
_CrestronIoDigitalReadOnly_ObjectIdentity = ObjectIdentity
crestronIoDigitalReadOnly = _CrestronIoDigitalReadOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2)
)
_CrestronIoDigitalReadOnlyTable_Object = MibTable
crestronIoDigitalReadOnlyTable = _CrestronIoDigitalReadOnlyTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnlyTable.setStatus("current")
_CrestronIoDigitalReadOnlyEntry_Object = MibTableRow
crestronIoDigitalReadOnlyEntry = _CrestronIoDigitalReadOnlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1, 1)
)
crestronIoDigitalReadOnlyEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronIoDigitalReadOnlyIoId"),
)
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnlyEntry.setStatus("current")
_CrestronIoDigitalReadOnlyIoId_Type = IoId
_CrestronIoDigitalReadOnlyIoId_Object = MibTableColumn
crestronIoDigitalReadOnlyIoId = _CrestronIoDigitalReadOnlyIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1, 1, 1),
    _CrestronIoDigitalReadOnlyIoId_Type()
)
crestronIoDigitalReadOnlyIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnlyIoId.setStatus("current")
_CrestronIoDigitalReadOnlyIoText_Type = DisplayString
_CrestronIoDigitalReadOnlyIoText_Object = MibTableColumn
crestronIoDigitalReadOnlyIoText = _CrestronIoDigitalReadOnlyIoText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1, 1, 2),
    _CrestronIoDigitalReadOnlyIoText_Type()
)
crestronIoDigitalReadOnlyIoText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnlyIoText.setStatus("current")


class _CrestronIoDigitalReadOnlyValue_Type(Integer32):
    """Custom type crestronIoDigitalReadOnlyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CrestronIoDigitalReadOnlyValue_Type.__name__ = "Integer32"
_CrestronIoDigitalReadOnlyValue_Object = MibTableColumn
crestronIoDigitalReadOnlyValue = _CrestronIoDigitalReadOnlyValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1, 1, 3),
    _CrestronIoDigitalReadOnlyValue_Type()
)
crestronIoDigitalReadOnlyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnlyValue.setStatus("current")
_CrestronIoDigitalReadOnly0Text_Type = DisplayString
_CrestronIoDigitalReadOnly0Text_Object = MibTableColumn
crestronIoDigitalReadOnly0Text = _CrestronIoDigitalReadOnly0Text_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1, 1, 4),
    _CrestronIoDigitalReadOnly0Text_Type()
)
crestronIoDigitalReadOnly0Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnly0Text.setStatus("current")
_CrestronIoDigitalReadOnly1Text_Type = DisplayString
_CrestronIoDigitalReadOnly1Text_Object = MibTableColumn
crestronIoDigitalReadOnly1Text = _CrestronIoDigitalReadOnly1Text_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 2, 2, 1, 1, 5),
    _CrestronIoDigitalReadOnly1Text_Type()
)
crestronIoDigitalReadOnly1Text.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoDigitalReadOnly1Text.setStatus("current")
_CrestronIoAnalog_ObjectIdentity = ObjectIdentity
crestronIoAnalog = _CrestronIoAnalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3)
)
_CrestronIoAnalogReadWrite_ObjectIdentity = ObjectIdentity
crestronIoAnalogReadWrite = _CrestronIoAnalogReadWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 1)
)
_CrestronIoAnalogReadWriteTable_Object = MibTable
crestronIoAnalogReadWriteTable = _CrestronIoAnalogReadWriteTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    crestronIoAnalogReadWriteTable.setStatus("current")
_CrestronIoAnalogReadWriteEntry_Object = MibTableRow
crestronIoAnalogReadWriteEntry = _CrestronIoAnalogReadWriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 1, 1, 1)
)
crestronIoAnalogReadWriteEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronIoAnalogReadWriteIoId"),
)
if mibBuilder.loadTexts:
    crestronIoAnalogReadWriteEntry.setStatus("current")
_CrestronIoAnalogReadWriteIoId_Type = IoId
_CrestronIoAnalogReadWriteIoId_Object = MibTableColumn
crestronIoAnalogReadWriteIoId = _CrestronIoAnalogReadWriteIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 1, 1, 1, 1),
    _CrestronIoAnalogReadWriteIoId_Type()
)
crestronIoAnalogReadWriteIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoAnalogReadWriteIoId.setStatus("current")
_CrestronIoAnalogReadWriteText_Type = DisplayString
_CrestronIoAnalogReadWriteText_Object = MibTableColumn
crestronIoAnalogReadWriteText = _CrestronIoAnalogReadWriteText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 1, 1, 1, 2),
    _CrestronIoAnalogReadWriteText_Type()
)
crestronIoAnalogReadWriteText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoAnalogReadWriteText.setStatus("current")
_CrestronIoAnalogReadWriteValue_Type = Integer32
_CrestronIoAnalogReadWriteValue_Object = MibTableColumn
crestronIoAnalogReadWriteValue = _CrestronIoAnalogReadWriteValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 1, 1, 1, 3),
    _CrestronIoAnalogReadWriteValue_Type()
)
crestronIoAnalogReadWriteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronIoAnalogReadWriteValue.setStatus("current")
_CrestronIoAnalogReadOnly_ObjectIdentity = ObjectIdentity
crestronIoAnalogReadOnly = _CrestronIoAnalogReadOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 2)
)
_CrestronIoAnalogReadOnlyTable_Object = MibTable
crestronIoAnalogReadOnlyTable = _CrestronIoAnalogReadOnlyTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    crestronIoAnalogReadOnlyTable.setStatus("current")
_CrestronIoAnalogReadOnlyEntry_Object = MibTableRow
crestronIoAnalogReadOnlyEntry = _CrestronIoAnalogReadOnlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 2, 1, 1)
)
crestronIoAnalogReadOnlyEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronIoAnalogReadOnlyIoId"),
)
if mibBuilder.loadTexts:
    crestronIoAnalogReadOnlyEntry.setStatus("current")
_CrestronIoAnalogReadOnlyIoId_Type = IoId
_CrestronIoAnalogReadOnlyIoId_Object = MibTableColumn
crestronIoAnalogReadOnlyIoId = _CrestronIoAnalogReadOnlyIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 2, 1, 1, 1),
    _CrestronIoAnalogReadOnlyIoId_Type()
)
crestronIoAnalogReadOnlyIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoAnalogReadOnlyIoId.setStatus("current")
_CrestronIoAnalogReadOnlyText_Type = DisplayString
_CrestronIoAnalogReadOnlyText_Object = MibTableColumn
crestronIoAnalogReadOnlyText = _CrestronIoAnalogReadOnlyText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 2, 1, 1, 2),
    _CrestronIoAnalogReadOnlyText_Type()
)
crestronIoAnalogReadOnlyText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoAnalogReadOnlyText.setStatus("current")
_CrestronIoAnalogReadOnlyValue_Type = Integer32
_CrestronIoAnalogReadOnlyValue_Object = MibTableColumn
crestronIoAnalogReadOnlyValue = _CrestronIoAnalogReadOnlyValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 2, 1, 1, 3),
    _CrestronIoAnalogReadOnlyValue_Type()
)
crestronIoAnalogReadOnlyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoAnalogReadOnlyValue.setStatus("current")
_CrestronValue_ObjectIdentity = ObjectIdentity
crestronValue = _CrestronValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 3)
)
_CrestronValueTable_Object = MibTable
crestronValueTable = _CrestronValueTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    crestronValueTable.setStatus("current")
_CrestronValueEntry_Object = MibTableRow
crestronValueEntry = _CrestronValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 3, 1, 1)
)
crestronValueEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronValueIoId"),
)
if mibBuilder.loadTexts:
    crestronValueEntry.setStatus("current")


class _CrestronValueIoId_Type(Integer32):
    """Custom type crestronValueIoId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CrestronValueIoId_Type.__name__ = "Integer32"
_CrestronValueIoId_Object = MibTableColumn
crestronValueIoId = _CrestronValueIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 3, 1, 1, 1),
    _CrestronValueIoId_Type()
)
crestronValueIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronValueIoId.setStatus("current")
_CrestronValueValue_Type = Integer32
_CrestronValueValue_Object = MibTableColumn
crestronValueValue = _CrestronValueValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 3, 1, 1, 2),
    _CrestronValueValue_Type()
)
crestronValueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronValueValue.setStatus("current")
_CrestronValueText_Type = DisplayString
_CrestronValueText_Object = MibTableColumn
crestronValueText = _CrestronValueText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 3, 3, 1, 1, 3),
    _CrestronValueText_Type()
)
crestronValueText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronValueText.setStatus("current")
_CrestronIoSerial_ObjectIdentity = ObjectIdentity
crestronIoSerial = _CrestronIoSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4)
)
_CrestronIoSerialReadWrite_ObjectIdentity = ObjectIdentity
crestronIoSerialReadWrite = _CrestronIoSerialReadWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 1)
)
_CrestronIoSerialReadWriteTable_Object = MibTable
crestronIoSerialReadWriteTable = _CrestronIoSerialReadWriteTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    crestronIoSerialReadWriteTable.setStatus("current")
_CrestronIoSerialReadWriteEntry_Object = MibTableRow
crestronIoSerialReadWriteEntry = _CrestronIoSerialReadWriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 1, 1, 1)
)
crestronIoSerialReadWriteEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronIoSerialReadWriteIoId"),
)
if mibBuilder.loadTexts:
    crestronIoSerialReadWriteEntry.setStatus("current")
_CrestronIoSerialReadWriteIoId_Type = IoId
_CrestronIoSerialReadWriteIoId_Object = MibTableColumn
crestronIoSerialReadWriteIoId = _CrestronIoSerialReadWriteIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 1, 1, 1, 1),
    _CrestronIoSerialReadWriteIoId_Type()
)
crestronIoSerialReadWriteIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoSerialReadWriteIoId.setStatus("current")
_CrestronIoSerialReadWriteIoText_Type = DisplayString
_CrestronIoSerialReadWriteIoText_Object = MibTableColumn
crestronIoSerialReadWriteIoText = _CrestronIoSerialReadWriteIoText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 1, 1, 1, 2),
    _CrestronIoSerialReadWriteIoText_Type()
)
crestronIoSerialReadWriteIoText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoSerialReadWriteIoText.setStatus("current")
_CrestronIoSerialReadWriteValue_Type = OctetString
_CrestronIoSerialReadWriteValue_Object = MibTableColumn
crestronIoSerialReadWriteValue = _CrestronIoSerialReadWriteValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 1, 1, 1, 3),
    _CrestronIoSerialReadWriteValue_Type()
)
crestronIoSerialReadWriteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crestronIoSerialReadWriteValue.setStatus("current")
_CrestronIoSerialReadOnly_ObjectIdentity = ObjectIdentity
crestronIoSerialReadOnly = _CrestronIoSerialReadOnly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 2)
)
_CrestronIoSerialReadOnlyTable_Object = MibTable
crestronIoSerialReadOnlyTable = _CrestronIoSerialReadOnlyTable_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    crestronIoSerialReadOnlyTable.setStatus("current")
_CrestronIoSerialReadOnlyEntry_Object = MibTableRow
crestronIoSerialReadOnlyEntry = _CrestronIoSerialReadOnlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 2, 1, 1)
)
crestronIoSerialReadOnlyEntry.setIndexNames(
    (0, "CRESTRON-IO-MIB", "crestronIoSerialReadOnlyIoId"),
)
if mibBuilder.loadTexts:
    crestronIoSerialReadOnlyEntry.setStatus("current")
_CrestronIoSerialReadOnlyIoId_Type = IoId
_CrestronIoSerialReadOnlyIoId_Object = MibTableColumn
crestronIoSerialReadOnlyIoId = _CrestronIoSerialReadOnlyIoId_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 2, 1, 1, 1),
    _CrestronIoSerialReadOnlyIoId_Type()
)
crestronIoSerialReadOnlyIoId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoSerialReadOnlyIoId.setStatus("current")
_CrestronIoSerialReadOnlyIoText_Type = DisplayString
_CrestronIoSerialReadOnlyIoText_Object = MibTableColumn
crestronIoSerialReadOnlyIoText = _CrestronIoSerialReadOnlyIoText_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 2, 1, 1, 2),
    _CrestronIoSerialReadOnlyIoText_Type()
)
crestronIoSerialReadOnlyIoText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoSerialReadOnlyIoText.setStatus("current")
_CrestronIoSerialReadOnlyValue_Type = OctetString
_CrestronIoSerialReadOnlyValue_Object = MibTableColumn
crestronIoSerialReadOnlyValue = _CrestronIoSerialReadOnlyValue_Object(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 3, 4, 2, 1, 1, 3),
    _CrestronIoSerialReadOnlyValue_Type()
)
crestronIoSerialReadOnlyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crestronIoSerialReadOnlyValue.setStatus("current")
_CrestronIoConformance_ObjectIdentity = ObjectIdentity
crestronIoConformance = _CrestronIoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5)
)
_CrestronIoCompliances_ObjectIdentity = ObjectIdentity
crestronIoCompliances = _CrestronIoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5, 1)
)
_CrestronIoGroups_ObjectIdentity = ObjectIdentity
crestronIoGroups = _CrestronIoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5, 2)
)

# Managed Objects groups

crestronIoInputObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5, 2, 1)
)
crestronIoInputObjects.setObjects(
      *(("CRESTRON-IO-MIB", "crestronIoAnalogReadWriteIoId"),
        ("CRESTRON-IO-MIB", "crestronIoAnalogReadWriteValue"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWriteIoId"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWriteValue"),
        ("CRESTRON-IO-MIB", "crestronIoAnalogReadWriteText"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWriteIoText"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWrite0Text"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWrite1Text"),
        ("CRESTRON-IO-MIB", "crestronIoSerialReadWriteIoId"),
        ("CRESTRON-IO-MIB", "crestronIoSerialReadWriteIoText"),
        ("CRESTRON-IO-MIB", "crestronIoSerialReadWriteValue"))
)
if mibBuilder.loadTexts:
    crestronIoInputObjects.setStatus("current")

crestronIoOutputObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5, 2, 2)
)
crestronIoOutputObjects.setObjects(
      *(("CRESTRON-IO-MIB", "crestronIoAnalogReadOnlyIoId"),
        ("CRESTRON-IO-MIB", "crestronIoAnalogReadOnlyValue"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadOnlyIoId"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadOnlyValue"),
        ("CRESTRON-IO-MIB", "crestronIoAnalogReadOnlyText"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWriteIoText"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWrite0Text"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadWrite1Text"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadOnly1Text"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadOnly0Text"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalReadOnlyIoText"),
        ("CRESTRON-IO-MIB", "crestronIoSerialReadOnlyIoId"),
        ("CRESTRON-IO-MIB", "crestronIoSerialReadOnlyIoText"),
        ("CRESTRON-IO-MIB", "crestronIoSerialReadOnlyValue"))
)
if mibBuilder.loadTexts:
    crestronIoOutputObjects.setStatus("current")

crestronIoMiscObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5, 2, 3)
)
crestronIoMiscObjects.setObjects(
      *(("CRESTRON-IO-MIB", "crestronIoVersion"),
        ("CRESTRON-IO-MIB", "crestronValueIoId"),
        ("CRESTRON-IO-MIB", "crestronValueValue"),
        ("CRESTRON-IO-MIB", "crestronValueText"),
        ("CRESTRON-IO-MIB", "crestronIoDigitalTrapData"),
        ("CRESTRON-IO-MIB", "crestronIoAnalogTrapData"),
        ("CRESTRON-IO-MIB", "crestronIoSerialTrapData"))
)
if mibBuilder.loadTexts:
    crestronIoMiscObjects.setStatus("current")


# Notification objects

crestronIoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    crestronIoTrap.setStatus(
        "current"
    )


# Notifications groups

crestronIoTrapObjects = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3212, 7, 1, 5, 2, 4)
)
crestronIoTrapObjects.setObjects(
    ("CRESTRON-IO-MIB", "crestronIoTrap")
)
if mibBuilder.loadTexts:
    crestronIoTrapObjects.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRESTRON-IO-MIB",
    **{"IoId": IoId,
       "Comparator": Comparator,
       "crestronIo": crestronIo,
       "crestronIoAdmin": crestronIoAdmin,
       "crestronIoNotifications": crestronIoNotifications,
       "crestronIoTrap": crestronIoTrap,
       "crestronIoDigitalTrapData": crestronIoDigitalTrapData,
       "crestronIoAnalogTrapData": crestronIoAnalogTrapData,
       "crestronIoSerialTrapData": crestronIoSerialTrapData,
       "crestronIoObjects": crestronIoObjects,
       "crestronIoVersion": crestronIoVersion,
       "crestronIoDigital": crestronIoDigital,
       "crestronIoDigitalReadWrite": crestronIoDigitalReadWrite,
       "crestronIoDigitalReadWriteTable": crestronIoDigitalReadWriteTable,
       "crestronIoDigitalReadWriteEntry": crestronIoDigitalReadWriteEntry,
       "crestronIoDigitalReadWriteIoId": crestronIoDigitalReadWriteIoId,
       "crestronIoDigitalReadWriteIoText": crestronIoDigitalReadWriteIoText,
       "crestronIoDigitalReadWriteValue": crestronIoDigitalReadWriteValue,
       "crestronIoDigitalReadWrite0Text": crestronIoDigitalReadWrite0Text,
       "crestronIoDigitalReadWrite1Text": crestronIoDigitalReadWrite1Text,
       "crestronIoDigitalReadOnly": crestronIoDigitalReadOnly,
       "crestronIoDigitalReadOnlyTable": crestronIoDigitalReadOnlyTable,
       "crestronIoDigitalReadOnlyEntry": crestronIoDigitalReadOnlyEntry,
       "crestronIoDigitalReadOnlyIoId": crestronIoDigitalReadOnlyIoId,
       "crestronIoDigitalReadOnlyIoText": crestronIoDigitalReadOnlyIoText,
       "crestronIoDigitalReadOnlyValue": crestronIoDigitalReadOnlyValue,
       "crestronIoDigitalReadOnly0Text": crestronIoDigitalReadOnly0Text,
       "crestronIoDigitalReadOnly1Text": crestronIoDigitalReadOnly1Text,
       "crestronIoAnalog": crestronIoAnalog,
       "crestronIoAnalogReadWrite": crestronIoAnalogReadWrite,
       "crestronIoAnalogReadWriteTable": crestronIoAnalogReadWriteTable,
       "crestronIoAnalogReadWriteEntry": crestronIoAnalogReadWriteEntry,
       "crestronIoAnalogReadWriteIoId": crestronIoAnalogReadWriteIoId,
       "crestronIoAnalogReadWriteText": crestronIoAnalogReadWriteText,
       "crestronIoAnalogReadWriteValue": crestronIoAnalogReadWriteValue,
       "crestronIoAnalogReadOnly": crestronIoAnalogReadOnly,
       "crestronIoAnalogReadOnlyTable": crestronIoAnalogReadOnlyTable,
       "crestronIoAnalogReadOnlyEntry": crestronIoAnalogReadOnlyEntry,
       "crestronIoAnalogReadOnlyIoId": crestronIoAnalogReadOnlyIoId,
       "crestronIoAnalogReadOnlyText": crestronIoAnalogReadOnlyText,
       "crestronIoAnalogReadOnlyValue": crestronIoAnalogReadOnlyValue,
       "crestronValue": crestronValue,
       "crestronValueTable": crestronValueTable,
       "crestronValueEntry": crestronValueEntry,
       "crestronValueIoId": crestronValueIoId,
       "crestronValueValue": crestronValueValue,
       "crestronValueText": crestronValueText,
       "crestronIoSerial": crestronIoSerial,
       "crestronIoSerialReadWrite": crestronIoSerialReadWrite,
       "crestronIoSerialReadWriteTable": crestronIoSerialReadWriteTable,
       "crestronIoSerialReadWriteEntry": crestronIoSerialReadWriteEntry,
       "crestronIoSerialReadWriteIoId": crestronIoSerialReadWriteIoId,
       "crestronIoSerialReadWriteIoText": crestronIoSerialReadWriteIoText,
       "crestronIoSerialReadWriteValue": crestronIoSerialReadWriteValue,
       "crestronIoSerialReadOnly": crestronIoSerialReadOnly,
       "crestronIoSerialReadOnlyTable": crestronIoSerialReadOnlyTable,
       "crestronIoSerialReadOnlyEntry": crestronIoSerialReadOnlyEntry,
       "crestronIoSerialReadOnlyIoId": crestronIoSerialReadOnlyIoId,
       "crestronIoSerialReadOnlyIoText": crestronIoSerialReadOnlyIoText,
       "crestronIoSerialReadOnlyValue": crestronIoSerialReadOnlyValue,
       "crestronIoConformance": crestronIoConformance,
       "crestronIoCompliances": crestronIoCompliances,
       "crestronIoGroups": crestronIoGroups,
       "crestronIoInputObjects": crestronIoInputObjects,
       "crestronIoOutputObjects": crestronIoOutputObjects,
       "crestronIoMiscObjects": crestronIoMiscObjects,
       "crestronIoTrapObjects": crestronIoTrapObjects}
)
