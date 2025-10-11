# SNMP MIB module (AdaptecArrayController-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adaptec/AdaptecArrayController-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:44 2025
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

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3)
)
_AdaptecArrayController_ObjectIdentity = ObjectIdentity
adaptecArrayController = _AdaptecArrayController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 3, 5)
)
_AdaptecArrayControllerSoftwareVersion_Type = DisplayString
_AdaptecArrayControllerSoftwareVersion_Object = MibScalar
adaptecArrayControllerSoftwareVersion = _AdaptecArrayControllerSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 1),
    _AdaptecArrayControllerSoftwareVersion_Type()
)
adaptecArrayControllerSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerSoftwareVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterNumber_Type = Integer32
_AdaptecArrayControllerAdapterNumber_Object = MibScalar
adaptecArrayControllerAdapterNumber = _AdaptecArrayControllerAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 2),
    _AdaptecArrayControllerAdapterNumber_Type()
)
adaptecArrayControllerAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterNumber.setStatus("mandatory")
_AdaptecArrayControllerAdapterTable_Object = MibTable
adaptecArrayControllerAdapterTable = _AdaptecArrayControllerAdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterTable.setStatus("mandatory")
_AdaptecArrayControllerAdapterEntry_Object = MibTableRow
adaptecArrayControllerAdapterEntry = _AdaptecArrayControllerAdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1)
)
adaptecArrayControllerAdapterEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerAdapterIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterEntry.setStatus("mandatory")
_AdaptecArrayControllerAdapterIndex_Type = Integer32
_AdaptecArrayControllerAdapterIndex_Object = MibTableColumn
adaptecArrayControllerAdapterIndex = _AdaptecArrayControllerAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 1),
    _AdaptecArrayControllerAdapterIndex_Type()
)
adaptecArrayControllerAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerAdapterDescription_Type = DisplayString
_AdaptecArrayControllerAdapterDescription_Object = MibTableColumn
adaptecArrayControllerAdapterDescription = _AdaptecArrayControllerAdapterDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 2),
    _AdaptecArrayControllerAdapterDescription_Type()
)
adaptecArrayControllerAdapterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterDescription.setStatus("mandatory")
_AdaptecArrayControllerAdapterType_Type = DisplayString
_AdaptecArrayControllerAdapterType_Object = MibTableColumn
adaptecArrayControllerAdapterType = _AdaptecArrayControllerAdapterType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 3),
    _AdaptecArrayControllerAdapterType_Type()
)
adaptecArrayControllerAdapterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterType.setStatus("mandatory")
_AdaptecArrayControllerAdapterVersion_Type = DisplayString
_AdaptecArrayControllerAdapterVersion_Object = MibTableColumn
adaptecArrayControllerAdapterVersion = _AdaptecArrayControllerAdapterVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 4),
    _AdaptecArrayControllerAdapterVersion_Type()
)
adaptecArrayControllerAdapterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterVersion.setStatus("mandatory")
_AdaptecArrayControllerAdapterChannelCount_Type = Integer32
_AdaptecArrayControllerAdapterChannelCount_Object = MibTableColumn
adaptecArrayControllerAdapterChannelCount = _AdaptecArrayControllerAdapterChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 5),
    _AdaptecArrayControllerAdapterChannelCount_Type()
)
adaptecArrayControllerAdapterChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterChannelCount.setStatus("mandatory")


class _AdaptecArrayControllerAdapterStatus_Type(Integer32):
    """Custom type adaptecArrayControllerAdapterStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6))
    )


_AdaptecArrayControllerAdapterStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerAdapterStatus_Object = MibTableColumn
adaptecArrayControllerAdapterStatus = _AdaptecArrayControllerAdapterStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 3, 1, 6),
    _AdaptecArrayControllerAdapterStatus_Type()
)
adaptecArrayControllerAdapterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerAdapterStatus.setStatus("mandatory")
_AdaptecArrayControllerContainerTable_Object = MibTable
adaptecArrayControllerContainerTable = _AdaptecArrayControllerContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerTable.setStatus("mandatory")
_AdaptecArrayControllerContainerEntry_Object = MibTableRow
adaptecArrayControllerContainerEntry = _AdaptecArrayControllerContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1)
)
adaptecArrayControllerContainerEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerContIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerContainerEntry.setStatus("mandatory")
_AdaptecArrayControllerContIndex_Type = Integer32
_AdaptecArrayControllerContIndex_Object = MibTableColumn
adaptecArrayControllerContIndex = _AdaptecArrayControllerContIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 1),
    _AdaptecArrayControllerContIndex_Type()
)
adaptecArrayControllerContIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContIndex.setStatus("mandatory")
_AdapterArrayControllerContAdapterIndex_Type = Integer32
_AdapterArrayControllerContAdapterIndex_Object = MibTableColumn
adapterArrayControllerContAdapterIndex = _AdapterArrayControllerContAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 2),
    _AdapterArrayControllerContAdapterIndex_Type()
)
adapterArrayControllerContAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adapterArrayControllerContAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerContNumber_Type = Integer32
_AdaptecArrayControllerContNumber_Object = MibTableColumn
adaptecArrayControllerContNumber = _AdaptecArrayControllerContNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 3),
    _AdaptecArrayControllerContNumber_Type()
)
adaptecArrayControllerContNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContNumber.setStatus("mandatory")
_AdaptecArrayControllerContSize_Type = Integer32
_AdaptecArrayControllerContSize_Object = MibTableColumn
adaptecArrayControllerContSize = _AdaptecArrayControllerContSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 4),
    _AdaptecArrayControllerContSize_Type()
)
adaptecArrayControllerContSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContSize.setStatus("mandatory")
_AdaptecArrayControllerContMountPoint_Type = DisplayString
_AdaptecArrayControllerContMountPoint_Object = MibTableColumn
adaptecArrayControllerContMountPoint = _AdaptecArrayControllerContMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 5),
    _AdaptecArrayControllerContMountPoint_Type()
)
adaptecArrayControllerContMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContMountPoint.setStatus("mandatory")
_AdaptecArrayControllerContType_Type = DisplayString
_AdaptecArrayControllerContType_Object = MibTableColumn
adaptecArrayControllerContType = _AdaptecArrayControllerContType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 6),
    _AdaptecArrayControllerContType_Type()
)
adaptecArrayControllerContType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContType.setStatus("mandatory")
_AdaptecArrayControllerContUsage_Type = DisplayString
_AdaptecArrayControllerContUsage_Object = MibTableColumn
adaptecArrayControllerContUsage = _AdaptecArrayControllerContUsage_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 7),
    _AdaptecArrayControllerContUsage_Type()
)
adaptecArrayControllerContUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContUsage.setStatus("mandatory")


class _AdaptecArrayControllerContStatus_Type(Integer32):
    """Custom type adaptecArrayControllerContStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6))
    )


_AdaptecArrayControllerContStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerContStatus_Object = MibTableColumn
adaptecArrayControllerContStatus = _AdaptecArrayControllerContStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 4, 1, 8),
    _AdaptecArrayControllerContStatus_Type()
)
adaptecArrayControllerContStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerContStatus.setStatus("mandatory")
_AdaptecArrayControllerDeviceTable_Object = MibTable
adaptecArrayControllerDeviceTable = _AdaptecArrayControllerDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5)
)
if mibBuilder.loadTexts:
    adaptecArrayControllerDeviceTable.setStatus("mandatory")
_AdaptecArrayControllerDeviceEntry_Object = MibTableRow
adaptecArrayControllerDeviceEntry = _AdaptecArrayControllerDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1)
)
adaptecArrayControllerDeviceEntry.setIndexNames(
    (0, "AdaptecArrayController-MIB", "adaptecArrayControllerDevIndex"),
)
if mibBuilder.loadTexts:
    adaptecArrayControllerDeviceEntry.setStatus("mandatory")
_AdaptecArrayControllerDevIndex_Type = Integer32
_AdaptecArrayControllerDevIndex_Object = MibTableColumn
adaptecArrayControllerDevIndex = _AdaptecArrayControllerDevIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 1),
    _AdaptecArrayControllerDevIndex_Type()
)
adaptecArrayControllerDevIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevIndex.setStatus("mandatory")
_AdaptecArrayControllerDevAdapterIndex_Type = Integer32
_AdaptecArrayControllerDevAdapterIndex_Object = MibTableColumn
adaptecArrayControllerDevAdapterIndex = _AdaptecArrayControllerDevAdapterIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 2),
    _AdaptecArrayControllerDevAdapterIndex_Type()
)
adaptecArrayControllerDevAdapterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevAdapterIndex.setStatus("mandatory")
_AdaptecArrayControllerDevChannelId_Type = Integer32
_AdaptecArrayControllerDevChannelId_Object = MibTableColumn
adaptecArrayControllerDevChannelId = _AdaptecArrayControllerDevChannelId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 3),
    _AdaptecArrayControllerDevChannelId_Type()
)
adaptecArrayControllerDevChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevChannelId.setStatus("mandatory")
_AdaptecArrayControllerDevId_Type = Integer32
_AdaptecArrayControllerDevId_Object = MibTableColumn
adaptecArrayControllerDevId = _AdaptecArrayControllerDevId_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 4),
    _AdaptecArrayControllerDevId_Type()
)
adaptecArrayControllerDevId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevId.setStatus("mandatory")
_AdaptecArrayControllerDevLogicalNumber_Type = Integer32
_AdaptecArrayControllerDevLogicalNumber_Object = MibTableColumn
adaptecArrayControllerDevLogicalNumber = _AdaptecArrayControllerDevLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 5),
    _AdaptecArrayControllerDevLogicalNumber_Type()
)
adaptecArrayControllerDevLogicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevLogicalNumber.setStatus("mandatory")
_AdaptecArrayControllerDevType_Type = Integer32
_AdaptecArrayControllerDevType_Object = MibTableColumn
adaptecArrayControllerDevType = _AdaptecArrayControllerDevType_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 6),
    _AdaptecArrayControllerDevType_Type()
)
adaptecArrayControllerDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevType.setStatus("mandatory")
_AdaptecArrayControllerDevVendor_Type = DisplayString
_AdaptecArrayControllerDevVendor_Object = MibTableColumn
adaptecArrayControllerDevVendor = _AdaptecArrayControllerDevVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 7),
    _AdaptecArrayControllerDevVendor_Type()
)
adaptecArrayControllerDevVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevVendor.setStatus("mandatory")
_AdaptecArrayControllerDevProduct_Type = DisplayString
_AdaptecArrayControllerDevProduct_Object = MibTableColumn
adaptecArrayControllerDevProduct = _AdaptecArrayControllerDevProduct_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 8),
    _AdaptecArrayControllerDevProduct_Type()
)
adaptecArrayControllerDevProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevProduct.setStatus("mandatory")
_AdaptecArrayControllerDevRevision_Type = DisplayString
_AdaptecArrayControllerDevRevision_Object = MibTableColumn
adaptecArrayControllerDevRevision = _AdaptecArrayControllerDevRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 9),
    _AdaptecArrayControllerDevRevision_Type()
)
adaptecArrayControllerDevRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevRevision.setStatus("mandatory")
_AdaptecArrayControllerDevBlocks_Type = Integer32
_AdaptecArrayControllerDevBlocks_Object = MibTableColumn
adaptecArrayControllerDevBlocks = _AdaptecArrayControllerDevBlocks_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 10),
    _AdaptecArrayControllerDevBlocks_Type()
)
adaptecArrayControllerDevBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevBlocks.setStatus("mandatory")
_AdaptecArrayControllerDevBytesPerBlock_Type = Integer32
_AdaptecArrayControllerDevBytesPerBlock_Object = MibTableColumn
adaptecArrayControllerDevBytesPerBlock = _AdaptecArrayControllerDevBytesPerBlock_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 11),
    _AdaptecArrayControllerDevBytesPerBlock_Type()
)
adaptecArrayControllerDevBytesPerBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevBytesPerBlock.setStatus("mandatory")
_AdaptecArrayControllerDevUsage_Type = DisplayString
_AdaptecArrayControllerDevUsage_Object = MibTableColumn
adaptecArrayControllerDevUsage = _AdaptecArrayControllerDevUsage_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 12),
    _AdaptecArrayControllerDevUsage_Type()
)
adaptecArrayControllerDevUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevUsage.setStatus("mandatory")


class _AdaptecArrayControllerDevStatus_Type(Integer32):
    """Custom type adaptecArrayControllerDevStatus based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("nonCritical", 4),
          ("critical", 5),
          ("nonRecoverable", 6))
    )


_AdaptecArrayControllerDevStatus_Type.__name__ = "Integer32"
_AdaptecArrayControllerDevStatus_Object = MibTableColumn
adaptecArrayControllerDevStatus = _AdaptecArrayControllerDevStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 3, 5, 5, 1, 13),
    _AdaptecArrayControllerDevStatus_Type()
)
adaptecArrayControllerDevStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adaptecArrayControllerDevStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AdaptecArrayController-MIB",
    **{"adaptec": adaptec,
       "products": products,
       "adaptecArrayController": adaptecArrayController,
       "adaptecArrayControllerSoftwareVersion": adaptecArrayControllerSoftwareVersion,
       "adaptecArrayControllerAdapterNumber": adaptecArrayControllerAdapterNumber,
       "adaptecArrayControllerAdapterTable": adaptecArrayControllerAdapterTable,
       "adaptecArrayControllerAdapterEntry": adaptecArrayControllerAdapterEntry,
       "adaptecArrayControllerAdapterIndex": adaptecArrayControllerAdapterIndex,
       "adaptecArrayControllerAdapterDescription": adaptecArrayControllerAdapterDescription,
       "adaptecArrayControllerAdapterType": adaptecArrayControllerAdapterType,
       "adaptecArrayControllerAdapterVersion": adaptecArrayControllerAdapterVersion,
       "adaptecArrayControllerAdapterChannelCount": adaptecArrayControllerAdapterChannelCount,
       "adaptecArrayControllerAdapterStatus": adaptecArrayControllerAdapterStatus,
       "adaptecArrayControllerContainerTable": adaptecArrayControllerContainerTable,
       "adaptecArrayControllerContainerEntry": adaptecArrayControllerContainerEntry,
       "adaptecArrayControllerContIndex": adaptecArrayControllerContIndex,
       "adapterArrayControllerContAdapterIndex": adapterArrayControllerContAdapterIndex,
       "adaptecArrayControllerContNumber": adaptecArrayControllerContNumber,
       "adaptecArrayControllerContSize": adaptecArrayControllerContSize,
       "adaptecArrayControllerContMountPoint": adaptecArrayControllerContMountPoint,
       "adaptecArrayControllerContType": adaptecArrayControllerContType,
       "adaptecArrayControllerContUsage": adaptecArrayControllerContUsage,
       "adaptecArrayControllerContStatus": adaptecArrayControllerContStatus,
       "adaptecArrayControllerDeviceTable": adaptecArrayControllerDeviceTable,
       "adaptecArrayControllerDeviceEntry": adaptecArrayControllerDeviceEntry,
       "adaptecArrayControllerDevIndex": adaptecArrayControllerDevIndex,
       "adaptecArrayControllerDevAdapterIndex": adaptecArrayControllerDevAdapterIndex,
       "adaptecArrayControllerDevChannelId": adaptecArrayControllerDevChannelId,
       "adaptecArrayControllerDevId": adaptecArrayControllerDevId,
       "adaptecArrayControllerDevLogicalNumber": adaptecArrayControllerDevLogicalNumber,
       "adaptecArrayControllerDevType": adaptecArrayControllerDevType,
       "adaptecArrayControllerDevVendor": adaptecArrayControllerDevVendor,
       "adaptecArrayControllerDevProduct": adaptecArrayControllerDevProduct,
       "adaptecArrayControllerDevRevision": adaptecArrayControllerDevRevision,
       "adaptecArrayControllerDevBlocks": adaptecArrayControllerDevBlocks,
       "adaptecArrayControllerDevBytesPerBlock": adaptecArrayControllerDevBytesPerBlock,
       "adaptecArrayControllerDevUsage": adaptecArrayControllerDevUsage,
       "adaptecArrayControllerDevStatus": adaptecArrayControllerDevStatus}
)
