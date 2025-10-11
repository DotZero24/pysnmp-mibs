# SNMP MIB module (PowerNet-Discovery-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/apc/PowerNet-Discovery-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:55 2025
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

_Apc_ObjectIdentity = ObjectIdentity
apc = _Apc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 1)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 3)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 4)
)
_ApcDiscovery_ObjectIdentity = ObjectIdentity
apcDiscovery = _ApcDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2)
)
_ApcDiscoveryInfoTableSize_Type = Integer32
_ApcDiscoveryInfoTableSize_Object = MibScalar
apcDiscoveryInfoTableSize = _ApcDiscoveryInfoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 1),
    _ApcDiscoveryInfoTableSize_Type()
)
apcDiscoveryInfoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryInfoTableSize.setStatus("mandatory")
_ApcDiscoveryInfoTable_Object = MibTable
apcDiscoveryInfoTable = _ApcDiscoveryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    apcDiscoveryInfoTable.setStatus("mandatory")
_ApcDiscoveryInfoEntry_Object = MibTableRow
apcDiscoveryInfoEntry = _ApcDiscoveryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1)
)
apcDiscoveryInfoEntry.setIndexNames(
    (0, "PowerNet-Discovery-MIB", "apcDiscoveryInfoTableIndex"),
)
if mibBuilder.loadTexts:
    apcDiscoveryInfoEntry.setStatus("mandatory")
_ApcDiscoveryInfoTableIndex_Type = Integer32
_ApcDiscoveryInfoTableIndex_Object = MibTableColumn
apcDiscoveryInfoTableIndex = _ApcDiscoveryInfoTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 1),
    _ApcDiscoveryInfoTableIndex_Type()
)
apcDiscoveryInfoTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryInfoTableIndex.setStatus("mandatory")
_ApcDiscoveryModel_Type = DisplayString
_ApcDiscoveryModel_Object = MibTableColumn
apcDiscoveryModel = _ApcDiscoveryModel_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 2),
    _ApcDiscoveryModel_Type()
)
apcDiscoveryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryModel.setStatus("mandatory")
_ApcDiscoverySerialNumber_Type = DisplayString
_ApcDiscoverySerialNumber_Object = MibTableColumn
apcDiscoverySerialNumber = _ApcDiscoverySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 3),
    _ApcDiscoverySerialNumber_Type()
)
apcDiscoverySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoverySerialNumber.setStatus("mandatory")


class _ApcDiscoveryStatus_Type(Integer32):
    """Custom type apcDiscoveryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("deviceNormal", 2),
          ("deviceWarning", 3),
          ("deviceSevere", 4),
          ("deviceLostCom", 5))
    )


_ApcDiscoveryStatus_Type.__name__ = "Integer32"
_ApcDiscoveryStatus_Object = MibTableColumn
apcDiscoveryStatus = _ApcDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 4),
    _ApcDiscoveryStatus_Type()
)
apcDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryStatus.setStatus("mandatory")
_ApcDiscoveryLabelString_Type = DisplayString
_ApcDiscoveryLabelString_Object = MibTableColumn
apcDiscoveryLabelString = _ApcDiscoveryLabelString_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 5),
    _ApcDiscoveryLabelString_Type()
)
apcDiscoveryLabelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryLabelString.setStatus("mandatory")
_ApcDiscoveryDeviceHierarchy_Type = DisplayString
_ApcDiscoveryDeviceHierarchy_Object = MibTableColumn
apcDiscoveryDeviceHierarchy = _ApcDiscoveryDeviceHierarchy_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 6),
    _ApcDiscoveryDeviceHierarchy_Type()
)
apcDiscoveryDeviceHierarchy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceHierarchy.setStatus("mandatory")
_ApcDiscoveryDeviceLocation_Type = DisplayString
_ApcDiscoveryDeviceLocation_Object = MibTableColumn
apcDiscoveryDeviceLocation = _ApcDiscoveryDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 7),
    _ApcDiscoveryDeviceLocation_Type()
)
apcDiscoveryDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceLocation.setStatus("mandatory")
_ApcDiscoveryDeviceLocationMaxLength_Type = Integer32
_ApcDiscoveryDeviceLocationMaxLength_Object = MibTableColumn
apcDiscoveryDeviceLocationMaxLength = _ApcDiscoveryDeviceLocationMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 8),
    _ApcDiscoveryDeviceLocationMaxLength_Type()
)
apcDiscoveryDeviceLocationMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceLocationMaxLength.setStatus("mandatory")
_ApcDiscoveryDeviceName_Type = DisplayString
_ApcDiscoveryDeviceName_Object = MibTableColumn
apcDiscoveryDeviceName = _ApcDiscoveryDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 9),
    _ApcDiscoveryDeviceName_Type()
)
apcDiscoveryDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceName.setStatus("mandatory")
_ApcDiscoveryDeviceNameMaxLength_Type = Integer32
_ApcDiscoveryDeviceNameMaxLength_Object = MibTableColumn
apcDiscoveryDeviceNameMaxLength = _ApcDiscoveryDeviceNameMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 10),
    _ApcDiscoveryDeviceNameMaxLength_Type()
)
apcDiscoveryDeviceNameMaxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceNameMaxLength.setStatus("mandatory")
_ApcDiscoveryDeviceInstance_Type = Integer32
_ApcDiscoveryDeviceInstance_Object = MibTableColumn
apcDiscoveryDeviceInstance = _ApcDiscoveryDeviceInstance_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 11),
    _ApcDiscoveryDeviceInstance_Type()
)
apcDiscoveryDeviceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceInstance.setStatus("mandatory")
_ApcDiscoveryDeviceParamsIndex_Type = DisplayString
_ApcDiscoveryDeviceParamsIndex_Object = MibTableColumn
apcDiscoveryDeviceParamsIndex = _ApcDiscoveryDeviceParamsIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 12),
    _ApcDiscoveryDeviceParamsIndex_Type()
)
apcDiscoveryDeviceParamsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceParamsIndex.setStatus("mandatory")
_ApcDiscoveryDdfXReference_Type = Integer32
_ApcDiscoveryDdfXReference_Object = MibTableColumn
apcDiscoveryDdfXReference = _ApcDiscoveryDdfXReference_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 13),
    _ApcDiscoveryDdfXReference_Type()
)
apcDiscoveryDdfXReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDdfXReference.setStatus("mandatory")
_ApcDiscoveryDeviceStatusBlockId_Type = DisplayString
_ApcDiscoveryDeviceStatusBlockId_Object = MibTableColumn
apcDiscoveryDeviceStatusBlockId = _ApcDiscoveryDeviceStatusBlockId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 2, 1, 14),
    _ApcDiscoveryDeviceStatusBlockId_Type()
)
apcDiscoveryDeviceStatusBlockId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceStatusBlockId.setStatus("mandatory")
_ApcDiscoveryDeviceFirmwareTableSize_Type = Integer32
_ApcDiscoveryDeviceFirmwareTableSize_Object = MibScalar
apcDiscoveryDeviceFirmwareTableSize = _ApcDiscoveryDeviceFirmwareTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 3),
    _ApcDiscoveryDeviceFirmwareTableSize_Type()
)
apcDiscoveryDeviceFirmwareTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceFirmwareTableSize.setStatus("mandatory")
_ApcDiscoveryDeviceFirmwareTable_Object = MibTable
apcDiscoveryDeviceFirmwareTable = _ApcDiscoveryDeviceFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 4)
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceFirmwareTable.setStatus("mandatory")
_ApcDiscoveryDeviceFirmwareEntry_Object = MibTableRow
apcDiscoveryDeviceFirmwareEntry = _ApcDiscoveryDeviceFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 4, 1)
)
apcDiscoveryDeviceFirmwareEntry.setIndexNames(
    (0, "PowerNet-Discovery-MIB", "apcDiscoveryDeviceFirmwareTableIndex"),
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceFirmwareEntry.setStatus("mandatory")
_ApcDiscoveryDeviceFirmwareTableIndex_Type = Integer32
_ApcDiscoveryDeviceFirmwareTableIndex_Object = MibTableColumn
apcDiscoveryDeviceFirmwareTableIndex = _ApcDiscoveryDeviceFirmwareTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 4, 1, 1),
    _ApcDiscoveryDeviceFirmwareTableIndex_Type()
)
apcDiscoveryDeviceFirmwareTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceFirmwareTableIndex.setStatus("mandatory")
_ApcDiscoveryDeviceSerialNumber_Type = DisplayString
_ApcDiscoveryDeviceSerialNumber_Object = MibTableColumn
apcDiscoveryDeviceSerialNumber = _ApcDiscoveryDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 4, 1, 2),
    _ApcDiscoveryDeviceSerialNumber_Type()
)
apcDiscoveryDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceSerialNumber.setStatus("mandatory")
_ApcDiscoveryFirmwareName_Type = DisplayString
_ApcDiscoveryFirmwareName_Object = MibTableColumn
apcDiscoveryFirmwareName = _ApcDiscoveryFirmwareName_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 4, 1, 3),
    _ApcDiscoveryFirmwareName_Type()
)
apcDiscoveryFirmwareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryFirmwareName.setStatus("mandatory")
_ApcDiscoveryFirmwareRevision_Type = DisplayString
_ApcDiscoveryFirmwareRevision_Object = MibTableColumn
apcDiscoveryFirmwareRevision = _ApcDiscoveryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 4, 1, 4),
    _ApcDiscoveryFirmwareRevision_Type()
)
apcDiscoveryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryFirmwareRevision.setStatus("mandatory")
_ApcDiscoveryDeviceProtocolTableSize_Type = Integer32
_ApcDiscoveryDeviceProtocolTableSize_Object = MibScalar
apcDiscoveryDeviceProtocolTableSize = _ApcDiscoveryDeviceProtocolTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 5),
    _ApcDiscoveryDeviceProtocolTableSize_Type()
)
apcDiscoveryDeviceProtocolTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceProtocolTableSize.setStatus("mandatory")
_ApcDiscoveryDeviceProtocolTable_Object = MibTable
apcDiscoveryDeviceProtocolTable = _ApcDiscoveryDeviceProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6)
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceProtocolTable.setStatus("mandatory")
_ApcDiscoveryDeviceProtocolEntry_Object = MibTableRow
apcDiscoveryDeviceProtocolEntry = _ApcDiscoveryDeviceProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6, 1)
)
apcDiscoveryDeviceProtocolEntry.setIndexNames(
    (0, "PowerNet-Discovery-MIB", "apcDiscoveryDeviceProtocolTableIndex"),
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceProtocolEntry.setStatus("mandatory")
_ApcDiscoveryDeviceProtocolTableIndex_Type = Integer32
_ApcDiscoveryDeviceProtocolTableIndex_Object = MibTableColumn
apcDiscoveryDeviceProtocolTableIndex = _ApcDiscoveryDeviceProtocolTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6, 1, 1),
    _ApcDiscoveryDeviceProtocolTableIndex_Type()
)
apcDiscoveryDeviceProtocolTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceProtocolTableIndex.setStatus("mandatory")
_ApcDiscoveryProtocolNumber_Type = Integer32
_ApcDiscoveryProtocolNumber_Object = MibTableColumn
apcDiscoveryProtocolNumber = _ApcDiscoveryProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6, 1, 2),
    _ApcDiscoveryProtocolNumber_Type()
)
apcDiscoveryProtocolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryProtocolNumber.setStatus("mandatory")
_ApcDiscoveryProtocolVersion_Type = DisplayString
_ApcDiscoveryProtocolVersion_Object = MibTableColumn
apcDiscoveryProtocolVersion = _ApcDiscoveryProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6, 1, 3),
    _ApcDiscoveryProtocolVersion_Type()
)
apcDiscoveryProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryProtocolVersion.setStatus("mandatory")
_ApcDiscoveryProtocolPort_Type = DisplayString
_ApcDiscoveryProtocolPort_Object = MibTableColumn
apcDiscoveryProtocolPort = _ApcDiscoveryProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6, 1, 4),
    _ApcDiscoveryProtocolPort_Type()
)
apcDiscoveryProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryProtocolPort.setStatus("mandatory")


class _ApcDiscoveryProtocolEnabledDisabled_Type(Integer32):
    """Custom type apcDiscoveryProtocolEnabledDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ApcDiscoveryProtocolEnabledDisabled_Type.__name__ = "Integer32"
_ApcDiscoveryProtocolEnabledDisabled_Object = MibTableColumn
apcDiscoveryProtocolEnabledDisabled = _ApcDiscoveryProtocolEnabledDisabled_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 6, 1, 5),
    _ApcDiscoveryProtocolEnabledDisabled_Type()
)
apcDiscoveryProtocolEnabledDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryProtocolEnabledDisabled.setStatus("mandatory")
_ApcDiscoveryDeviceDefTableSize_Type = Integer32
_ApcDiscoveryDeviceDefTableSize_Object = MibScalar
apcDiscoveryDeviceDefTableSize = _ApcDiscoveryDeviceDefTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 7),
    _ApcDiscoveryDeviceDefTableSize_Type()
)
apcDiscoveryDeviceDefTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefTableSize.setStatus("mandatory")
_ApcDiscoveryDeviceDefTable_Object = MibTable
apcDiscoveryDeviceDefTable = _ApcDiscoveryDeviceDefTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8)
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefTable.setStatus("mandatory")
_ApcDiscoveryDeviceDefEntry_Object = MibTableRow
apcDiscoveryDeviceDefEntry = _ApcDiscoveryDeviceDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1)
)
apcDiscoveryDeviceDefEntry.setIndexNames(
    (0, "PowerNet-Discovery-MIB", "apcDiscoveryDeviceDefTableIndex"),
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefEntry.setStatus("mandatory")
_ApcDiscoveryDeviceDefTableIndex_Type = Integer32
_ApcDiscoveryDeviceDefTableIndex_Object = MibTableColumn
apcDiscoveryDeviceDefTableIndex = _ApcDiscoveryDeviceDefTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1, 1),
    _ApcDiscoveryDeviceDefTableIndex_Type()
)
apcDiscoveryDeviceDefTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefTableIndex.setStatus("mandatory")
_ApcDiscoveryDeviceDefDeviceClass_Type = DisplayString
_ApcDiscoveryDeviceDefDeviceClass_Object = MibTableColumn
apcDiscoveryDeviceDefDeviceClass = _ApcDiscoveryDeviceDefDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1, 2),
    _ApcDiscoveryDeviceDefDeviceClass_Type()
)
apcDiscoveryDeviceDefDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefDeviceClass.setStatus("mandatory")
_ApcDiscoveryDeviceDefDeviceType_Type = DisplayString
_ApcDiscoveryDeviceDefDeviceType_Object = MibTableColumn
apcDiscoveryDeviceDefDeviceType = _ApcDiscoveryDeviceDefDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1, 3),
    _ApcDiscoveryDeviceDefDeviceType_Type()
)
apcDiscoveryDeviceDefDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefDeviceType.setStatus("mandatory")
_ApcDiscoveryDeviceDefDeviceFamily_Type = DisplayString
_ApcDiscoveryDeviceDefDeviceFamily_Object = MibTableColumn
apcDiscoveryDeviceDefDeviceFamily = _ApcDiscoveryDeviceDefDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1, 4),
    _ApcDiscoveryDeviceDefDeviceFamily_Type()
)
apcDiscoveryDeviceDefDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefDeviceFamily.setStatus("mandatory")
_ApcDiscoveryDeviceDefDeviceVersion_Type = DisplayString
_ApcDiscoveryDeviceDefDeviceVersion_Object = MibTableColumn
apcDiscoveryDeviceDefDeviceVersion = _ApcDiscoveryDeviceDefDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1, 5),
    _ApcDiscoveryDeviceDefDeviceVersion_Type()
)
apcDiscoveryDeviceDefDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefDeviceVersion.setStatus("mandatory")
_ApcDiscoveryDeviceDefDdfXReference_Type = Integer32
_ApcDiscoveryDeviceDefDdfXReference_Object = MibTableColumn
apcDiscoveryDeviceDefDdfXReference = _ApcDiscoveryDeviceDefDdfXReference_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 8, 1, 6),
    _ApcDiscoveryDeviceDefDdfXReference_Type()
)
apcDiscoveryDeviceDefDdfXReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceDefDdfXReference.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateChangeCount_Type = Integer32
_ApcDiscoveryDeviceAlarmStateChangeCount_Object = MibScalar
apcDiscoveryDeviceAlarmStateChangeCount = _ApcDiscoveryDeviceAlarmStateChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 9),
    _ApcDiscoveryDeviceAlarmStateChangeCount_Type()
)
apcDiscoveryDeviceAlarmStateChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateChangeCount.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateTableSize_Type = Integer32
_ApcDiscoveryDeviceAlarmStateTableSize_Object = MibScalar
apcDiscoveryDeviceAlarmStateTableSize = _ApcDiscoveryDeviceAlarmStateTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 10),
    _ApcDiscoveryDeviceAlarmStateTableSize_Type()
)
apcDiscoveryDeviceAlarmStateTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateTableSize.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateTable_Object = MibTable
apcDiscoveryDeviceAlarmStateTable = _ApcDiscoveryDeviceAlarmStateTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 11)
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateTable.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateEntry_Object = MibTableRow
apcDiscoveryDeviceAlarmStateEntry = _ApcDiscoveryDeviceAlarmStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 11, 1)
)
apcDiscoveryDeviceAlarmStateEntry.setIndexNames(
    (0, "PowerNet-Discovery-MIB", "apcDiscoveryDeviceAlarmStateTableIndex"),
)
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateEntry.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateTableIndex_Type = Integer32
_ApcDiscoveryDeviceAlarmStateTableIndex_Object = MibTableColumn
apcDiscoveryDeviceAlarmStateTableIndex = _ApcDiscoveryDeviceAlarmStateTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 11, 1, 1),
    _ApcDiscoveryDeviceAlarmStateTableIndex_Type()
)
apcDiscoveryDeviceAlarmStateTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateTableIndex.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateSerialNumber_Type = DisplayString
_ApcDiscoveryDeviceAlarmStateSerialNumber_Object = MibTableColumn
apcDiscoveryDeviceAlarmStateSerialNumber = _ApcDiscoveryDeviceAlarmStateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 11, 1, 2),
    _ApcDiscoveryDeviceAlarmStateSerialNumber_Type()
)
apcDiscoveryDeviceAlarmStateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateSerialNumber.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateCode_Type = OctetString
_ApcDiscoveryDeviceAlarmStateCode_Object = MibTableColumn
apcDiscoveryDeviceAlarmStateCode = _ApcDiscoveryDeviceAlarmStateCode_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 11, 1, 3),
    _ApcDiscoveryDeviceAlarmStateCode_Type()
)
apcDiscoveryDeviceAlarmStateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateCode.setStatus("mandatory")
_ApcDiscoveryDeviceAlarmStateParam_Type = OctetString
_ApcDiscoveryDeviceAlarmStateParam_Object = MibTableColumn
apcDiscoveryDeviceAlarmStateParam = _ApcDiscoveryDeviceAlarmStateParam_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 11, 1, 4),
    _ApcDiscoveryDeviceAlarmStateParam_Type()
)
apcDiscoveryDeviceAlarmStateParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceAlarmStateParam.setStatus("mandatory")
_ApcDiscoveryDeviceInfoChangeCount_Type = Integer32
_ApcDiscoveryDeviceInfoChangeCount_Object = MibScalar
apcDiscoveryDeviceInfoChangeCount = _ApcDiscoveryDeviceInfoChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 2, 12),
    _ApcDiscoveryDeviceInfoChangeCount_Type()
)
apcDiscoveryDeviceInfoChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcDiscoveryDeviceInfoChangeCount.setStatus("mandatory")
_ApcTrapReceiver_ObjectIdentity = ObjectIdentity
apcTrapReceiver = _ApcTrapReceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4)
)
_ApcTrapRecvTableSize_Type = Integer32
_ApcTrapRecvTableSize_Object = MibScalar
apcTrapRecvTableSize = _ApcTrapRecvTableSize_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 1),
    _ApcTrapRecvTableSize_Type()
)
apcTrapRecvTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcTrapRecvTableSize.setStatus("mandatory")
_ApcTrapRecvTable_Object = MibTable
apcTrapRecvTable = _ApcTrapRecvTable_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 2)
)
if mibBuilder.loadTexts:
    apcTrapRecvTable.setStatus("mandatory")
_ApcTrapRecvEntry_Object = MibTableRow
apcTrapRecvEntry = _ApcTrapRecvEntry_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 2, 1)
)
apcTrapRecvEntry.setIndexNames(
    (0, "PowerNet-Discovery-MIB", "apcTrapRecvIndex"),
)
if mibBuilder.loadTexts:
    apcTrapRecvEntry.setStatus("mandatory")
_ApcTrapRecvIndex_Type = Integer32
_ApcTrapRecvIndex_Object = MibTableColumn
apcTrapRecvIndex = _ApcTrapRecvIndex_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 2, 1, 1),
    _ApcTrapRecvIndex_Type()
)
apcTrapRecvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcTrapRecvIndex.setStatus("mandatory")


class _ApcTrapRecvHost_Type(DisplayString):
    """Custom type apcTrapRecvHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ApcTrapRecvHost_Type.__name__ = "DisplayString"
_ApcTrapRecvHost_Object = MibTableColumn
apcTrapRecvHost = _ApcTrapRecvHost_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 2, 1, 2),
    _ApcTrapRecvHost_Type()
)
apcTrapRecvHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcTrapRecvHost.setStatus("mandatory")


class _ApcTrapRecvType_Type(Integer32):
    """Custom type apcTrapRecvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("remove", 2),
          ("pcs", 3),
          ("isxm", 4))
    )


_ApcTrapRecvType_Type.__name__ = "Integer32"
_ApcTrapRecvType_Object = MibTableColumn
apcTrapRecvType = _ApcTrapRecvType_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 2, 1, 3),
    _ApcTrapRecvType_Type()
)
apcTrapRecvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcTrapRecvType.setStatus("mandatory")
_ApcTrapRecvUniqueId_Type = Integer32
_ApcTrapRecvUniqueId_Object = MibTableColumn
apcTrapRecvUniqueId = _ApcTrapRecvUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 2, 1, 4),
    _ApcTrapRecvUniqueId_Type()
)
apcTrapRecvUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcTrapRecvUniqueId.setStatus("mandatory")


class _ApcTrapRecvTableModify_Type(DisplayString):
    """Custom type apcTrapRecvTableModify based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ApcTrapRecvTableModify_Type.__name__ = "DisplayString"
_ApcTrapRecvTableModify_Object = MibScalar
apcTrapRecvTableModify = _ApcTrapRecvTableModify_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 3),
    _ApcTrapRecvTableModify_Type()
)
apcTrapRecvTableModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apcTrapRecvTableModify.setStatus("mandatory")
_ApcTrapReceiverUniqueID_Type = Integer32
_ApcTrapReceiverUniqueID_Object = MibScalar
apcTrapReceiverUniqueID = _ApcTrapReceiverUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 318, 1, 4, 4, 4),
    _ApcTrapReceiverUniqueID_Type()
)
apcTrapReceiverUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apcTrapReceiverUniqueID.setStatus("mandatory")
_Apcmgmt_ObjectIdentity = ObjectIdentity
apcmgmt = _Apcmgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 318, 2)
)

# Managed Objects groups


# Notification objects

apcDiscoveryAlarmStateTableUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 318, 0, 1000)
)
apcDiscoveryAlarmStateTableUpdate.setObjects(
    ("PowerNet-Discovery-MIB", "apcDiscoveryDeviceAlarmStateChangeCount")
)
if mibBuilder.loadTexts:
    apcDiscoveryAlarmStateTableUpdate.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PowerNet-Discovery-MIB",
    **{"apc": apc,
       "apcDiscoveryAlarmStateTableUpdate": apcDiscoveryAlarmStateTableUpdate,
       "products": products,
       "hardware": hardware,
       "software": software,
       "system": system,
       "experimental": experimental,
       "apcDiscovery": apcDiscovery,
       "apcDiscoveryInfoTableSize": apcDiscoveryInfoTableSize,
       "apcDiscoveryInfoTable": apcDiscoveryInfoTable,
       "apcDiscoveryInfoEntry": apcDiscoveryInfoEntry,
       "apcDiscoveryInfoTableIndex": apcDiscoveryInfoTableIndex,
       "apcDiscoveryModel": apcDiscoveryModel,
       "apcDiscoverySerialNumber": apcDiscoverySerialNumber,
       "apcDiscoveryStatus": apcDiscoveryStatus,
       "apcDiscoveryLabelString": apcDiscoveryLabelString,
       "apcDiscoveryDeviceHierarchy": apcDiscoveryDeviceHierarchy,
       "apcDiscoveryDeviceLocation": apcDiscoveryDeviceLocation,
       "apcDiscoveryDeviceLocationMaxLength": apcDiscoveryDeviceLocationMaxLength,
       "apcDiscoveryDeviceName": apcDiscoveryDeviceName,
       "apcDiscoveryDeviceNameMaxLength": apcDiscoveryDeviceNameMaxLength,
       "apcDiscoveryDeviceInstance": apcDiscoveryDeviceInstance,
       "apcDiscoveryDeviceParamsIndex": apcDiscoveryDeviceParamsIndex,
       "apcDiscoveryDdfXReference": apcDiscoveryDdfXReference,
       "apcDiscoveryDeviceStatusBlockId": apcDiscoveryDeviceStatusBlockId,
       "apcDiscoveryDeviceFirmwareTableSize": apcDiscoveryDeviceFirmwareTableSize,
       "apcDiscoveryDeviceFirmwareTable": apcDiscoveryDeviceFirmwareTable,
       "apcDiscoveryDeviceFirmwareEntry": apcDiscoveryDeviceFirmwareEntry,
       "apcDiscoveryDeviceFirmwareTableIndex": apcDiscoveryDeviceFirmwareTableIndex,
       "apcDiscoveryDeviceSerialNumber": apcDiscoveryDeviceSerialNumber,
       "apcDiscoveryFirmwareName": apcDiscoveryFirmwareName,
       "apcDiscoveryFirmwareRevision": apcDiscoveryFirmwareRevision,
       "apcDiscoveryDeviceProtocolTableSize": apcDiscoveryDeviceProtocolTableSize,
       "apcDiscoveryDeviceProtocolTable": apcDiscoveryDeviceProtocolTable,
       "apcDiscoveryDeviceProtocolEntry": apcDiscoveryDeviceProtocolEntry,
       "apcDiscoveryDeviceProtocolTableIndex": apcDiscoveryDeviceProtocolTableIndex,
       "apcDiscoveryProtocolNumber": apcDiscoveryProtocolNumber,
       "apcDiscoveryProtocolVersion": apcDiscoveryProtocolVersion,
       "apcDiscoveryProtocolPort": apcDiscoveryProtocolPort,
       "apcDiscoveryProtocolEnabledDisabled": apcDiscoveryProtocolEnabledDisabled,
       "apcDiscoveryDeviceDefTableSize": apcDiscoveryDeviceDefTableSize,
       "apcDiscoveryDeviceDefTable": apcDiscoveryDeviceDefTable,
       "apcDiscoveryDeviceDefEntry": apcDiscoveryDeviceDefEntry,
       "apcDiscoveryDeviceDefTableIndex": apcDiscoveryDeviceDefTableIndex,
       "apcDiscoveryDeviceDefDeviceClass": apcDiscoveryDeviceDefDeviceClass,
       "apcDiscoveryDeviceDefDeviceType": apcDiscoveryDeviceDefDeviceType,
       "apcDiscoveryDeviceDefDeviceFamily": apcDiscoveryDeviceDefDeviceFamily,
       "apcDiscoveryDeviceDefDeviceVersion": apcDiscoveryDeviceDefDeviceVersion,
       "apcDiscoveryDeviceDefDdfXReference": apcDiscoveryDeviceDefDdfXReference,
       "apcDiscoveryDeviceAlarmStateChangeCount": apcDiscoveryDeviceAlarmStateChangeCount,
       "apcDiscoveryDeviceAlarmStateTableSize": apcDiscoveryDeviceAlarmStateTableSize,
       "apcDiscoveryDeviceAlarmStateTable": apcDiscoveryDeviceAlarmStateTable,
       "apcDiscoveryDeviceAlarmStateEntry": apcDiscoveryDeviceAlarmStateEntry,
       "apcDiscoveryDeviceAlarmStateTableIndex": apcDiscoveryDeviceAlarmStateTableIndex,
       "apcDiscoveryDeviceAlarmStateSerialNumber": apcDiscoveryDeviceAlarmStateSerialNumber,
       "apcDiscoveryDeviceAlarmStateCode": apcDiscoveryDeviceAlarmStateCode,
       "apcDiscoveryDeviceAlarmStateParam": apcDiscoveryDeviceAlarmStateParam,
       "apcDiscoveryDeviceInfoChangeCount": apcDiscoveryDeviceInfoChangeCount,
       "apcTrapReceiver": apcTrapReceiver,
       "apcTrapRecvTableSize": apcTrapRecvTableSize,
       "apcTrapRecvTable": apcTrapRecvTable,
       "apcTrapRecvEntry": apcTrapRecvEntry,
       "apcTrapRecvIndex": apcTrapRecvIndex,
       "apcTrapRecvHost": apcTrapRecvHost,
       "apcTrapRecvType": apcTrapRecvType,
       "apcTrapRecvUniqueId": apcTrapRecvUniqueId,
       "apcTrapRecvTableModify": apcTrapRecvTableModify,
       "apcTrapReceiverUniqueID": apcTrapReceiverUniqueID,
       "apcmgmt": apcmgmt}
)
