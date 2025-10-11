# SNMP MIB module (HUAWEI-DEVICE-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-DEVICE-MAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:27:10 2025
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

storage = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_DeviceManager_ObjectIdentity = ObjectIdentity
deviceManager = _DeviceManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22)
)
_HwInfoPortIBTable_Object = MibTable
hwInfoPortIBTable = _HwInfoPortIBTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500)
)
if mibBuilder.loadTexts:
    hwInfoPortIBTable.setStatus("current")
_HwInfoPortIBEntry_Object = MibTableRow
hwInfoPortIBEntry = _HwInfoPortIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1)
)
hwInfoPortIBEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBID"),
)
if mibBuilder.loadTexts:
    hwInfoPortIBEntry.setStatus("current")
_HwInfoPortIBID_Type = OctetString
_HwInfoPortIBID_Object = MibTableColumn
hwInfoPortIBID = _HwInfoPortIBID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 1),
    _HwInfoPortIBID_Type()
)
hwInfoPortIBID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBID.setStatus("current")
_HwInfoPortIBParentType_Type = Unsigned32
_HwInfoPortIBParentType_Object = MibTableColumn
hwInfoPortIBParentType = _HwInfoPortIBParentType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 2),
    _HwInfoPortIBParentType_Type()
)
hwInfoPortIBParentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBParentType.setStatus("current")
_HwInfoPortIBParentID_Type = OctetString
_HwInfoPortIBParentID_Object = MibTableColumn
hwInfoPortIBParentID = _HwInfoPortIBParentID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 3),
    _HwInfoPortIBParentID_Type()
)
hwInfoPortIBParentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBParentID.setStatus("current")
_HwInfoPortIBLocation_Type = OctetString
_HwInfoPortIBLocation_Object = MibTableColumn
hwInfoPortIBLocation = _HwInfoPortIBLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 4),
    _HwInfoPortIBLocation_Type()
)
hwInfoPortIBLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBLocation.setStatus("current")
_HwInfoPortIBHealthStatus_Type = Unsigned32
_HwInfoPortIBHealthStatus_Object = MibTableColumn
hwInfoPortIBHealthStatus = _HwInfoPortIBHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 5),
    _HwInfoPortIBHealthStatus_Type()
)
hwInfoPortIBHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBHealthStatus.setStatus("current")
_HwInfoPortIBRunningStatus_Type = Unsigned32
_HwInfoPortIBRunningStatus_Object = MibTableColumn
hwInfoPortIBRunningStatus = _HwInfoPortIBRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 6),
    _HwInfoPortIBRunningStatus_Type()
)
hwInfoPortIBRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBRunningStatus.setStatus("current")
_HwInfoPortIBType_Type = Unsigned32
_HwInfoPortIBType_Object = MibTableColumn
hwInfoPortIBType = _HwInfoPortIBType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 7),
    _HwInfoPortIBType_Type()
)
hwInfoPortIBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBType.setStatus("current")
_HwInfoPortIBWorkingRate_Type = Unsigned32
_HwInfoPortIBWorkingRate_Object = MibTableColumn
hwInfoPortIBWorkingRate = _HwInfoPortIBWorkingRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 8),
    _HwInfoPortIBWorkingRate_Type()
)
hwInfoPortIBWorkingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBWorkingRate.setStatus("current")
_HwInfoPortIBWWN_Type = OctetString
_HwInfoPortIBWWN_Object = MibTableColumn
hwInfoPortIBWWN = _HwInfoPortIBWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 9),
    _HwInfoPortIBWWN_Type()
)
hwInfoPortIBWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBWWN.setStatus("current")
_HwInfoPortIBRole_Type = Unsigned32
_HwInfoPortIBRole_Object = MibTableColumn
hwInfoPortIBRole = _HwInfoPortIBRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 10),
    _HwInfoPortIBRole_Type()
)
hwInfoPortIBRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBRole.setStatus("current")
_HwInfoPortIBSymbolError_Type = Unsigned32
_HwInfoPortIBSymbolError_Object = MibTableColumn
hwInfoPortIBSymbolError = _HwInfoPortIBSymbolError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 11),
    _HwInfoPortIBSymbolError_Type()
)
hwInfoPortIBSymbolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBSymbolError.setStatus("current")
_HwInfoPortIBLinkErrorRecovery_Type = Unsigned32
_HwInfoPortIBLinkErrorRecovery_Object = MibTableColumn
hwInfoPortIBLinkErrorRecovery = _HwInfoPortIBLinkErrorRecovery_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 12),
    _HwInfoPortIBLinkErrorRecovery_Type()
)
hwInfoPortIBLinkErrorRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBLinkErrorRecovery.setStatus("current")
_HwInfoPortIBReceiveErrors_Type = Unsigned32
_HwInfoPortIBReceiveErrors_Object = MibTableColumn
hwInfoPortIBReceiveErrors = _HwInfoPortIBReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 13),
    _HwInfoPortIBReceiveErrors_Type()
)
hwInfoPortIBReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBReceiveErrors.setStatus("current")
_HwInfoPortIBRemoteReceiveErrors_Type = Unsigned32
_HwInfoPortIBRemoteReceiveErrors_Object = MibTableColumn
hwInfoPortIBRemoteReceiveErrors = _HwInfoPortIBRemoteReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 14),
    _HwInfoPortIBRemoteReceiveErrors_Type()
)
hwInfoPortIBRemoteReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBRemoteReceiveErrors.setStatus("current")
_HwInfoPortIBReceiveTransmitErrors_Type = Unsigned32
_HwInfoPortIBReceiveTransmitErrors_Object = MibTableColumn
hwInfoPortIBReceiveTransmitErrors = _HwInfoPortIBReceiveTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 15),
    _HwInfoPortIBReceiveTransmitErrors_Type()
)
hwInfoPortIBReceiveTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBReceiveTransmitErrors.setStatus("current")
_HwInfoPortIBNotSendPacakges_Type = Unsigned32
_HwInfoPortIBNotSendPacakges_Object = MibTableColumn
hwInfoPortIBNotSendPacakges = _HwInfoPortIBNotSendPacakges_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 16),
    _HwInfoPortIBNotSendPacakges_Type()
)
hwInfoPortIBNotSendPacakges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBNotSendPacakges.setStatus("current")
_HwInfoPortIBReceiveConstraintErrors_Type = Unsigned32
_HwInfoPortIBReceiveConstraintErrors_Object = MibTableColumn
hwInfoPortIBReceiveConstraintErrors = _HwInfoPortIBReceiveConstraintErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 17),
    _HwInfoPortIBReceiveConstraintErrors_Type()
)
hwInfoPortIBReceiveConstraintErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBReceiveConstraintErrors.setStatus("current")
_HwInfoPortIBLinkErrors_Type = Unsigned32
_HwInfoPortIBLinkErrors_Object = MibTableColumn
hwInfoPortIBLinkErrors = _HwInfoPortIBLinkErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 18),
    _HwInfoPortIBLinkErrors_Type()
)
hwInfoPortIBLinkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBLinkErrors.setStatus("current")
_HwInfoPortIBBufferOverrunErrors_Type = Unsigned32
_HwInfoPortIBBufferOverrunErrors_Object = MibTableColumn
hwInfoPortIBBufferOverrunErrors = _HwInfoPortIBBufferOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 19),
    _HwInfoPortIBBufferOverrunErrors_Type()
)
hwInfoPortIBBufferOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBBufferOverrunErrors.setStatus("current")
_HwInfoPortIBStartTime_Type = OctetString
_HwInfoPortIBStartTime_Object = MibTableColumn
hwInfoPortIBStartTime = _HwInfoPortIBStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 20),
    _HwInfoPortIBStartTime_Type()
)
hwInfoPortIBStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBStartTime.setStatus("current")
_HwInfoPortIBMaxSpeed_Type = Unsigned32
_HwInfoPortIBMaxSpeed_Object = MibTableColumn
hwInfoPortIBMaxSpeed = _HwInfoPortIBMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 251, 22, 16500, 1, 21),
    _HwInfoPortIBMaxSpeed_Type()
)
hwInfoPortIBMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInfoPortIBMaxSpeed.setStatus("current")
_IsoConformance_ObjectIdentity = ObjectIdentity
isoConformance = _IsoConformance_ObjectIdentity(
    (1, 6)
)
_IsoGroups_ObjectIdentity = ObjectIdentity
isoGroups = _IsoGroups_ObjectIdentity(
    (1, 6, 1)
)
_IsoCompliances_ObjectIdentity = ObjectIdentity
isoCompliances = _IsoCompliances_ObjectIdentity(
    (1, 6, 2)
)

# Managed Objects groups

currentObjectGroup = ObjectGroup(
    (1, 6, 1, 1)
)
currentObjectGroup.setObjects(
      *(("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBID"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBParentType"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBParentID"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBLocation"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBHealthStatus"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBRunningStatus"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBType"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBWorkingRate"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBWWN"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBRole"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBSymbolError"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBLinkErrorRecovery"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBReceiveErrors"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBRemoteReceiveErrors"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBReceiveTransmitErrors"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBNotSendPacakges"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBReceiveConstraintErrors"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBLinkErrors"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBBufferOverrunErrors"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBStartTime"),
        ("HUAWEI-DEVICE-MAN-MIB", "hwInfoPortIBMaxSpeed"))
)
if mibBuilder.loadTexts:
    currentObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

basicCompliance = ModuleCompliance(
    (1, 6, 2, 1)
)
basicCompliance.setObjects(
    ("HUAWEI-DEVICE-MAN-MIB", "currentObjectGroup")
)
if mibBuilder.loadTexts:
    basicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DEVICE-MAN-MIB",
    **{"huawei": huawei,
       "products": products,
       "storage": storage,
       "deviceManager": deviceManager,
       "hwInfoPortIBTable": hwInfoPortIBTable,
       "hwInfoPortIBEntry": hwInfoPortIBEntry,
       "hwInfoPortIBID": hwInfoPortIBID,
       "hwInfoPortIBParentType": hwInfoPortIBParentType,
       "hwInfoPortIBParentID": hwInfoPortIBParentID,
       "hwInfoPortIBLocation": hwInfoPortIBLocation,
       "hwInfoPortIBHealthStatus": hwInfoPortIBHealthStatus,
       "hwInfoPortIBRunningStatus": hwInfoPortIBRunningStatus,
       "hwInfoPortIBType": hwInfoPortIBType,
       "hwInfoPortIBWorkingRate": hwInfoPortIBWorkingRate,
       "hwInfoPortIBWWN": hwInfoPortIBWWN,
       "hwInfoPortIBRole": hwInfoPortIBRole,
       "hwInfoPortIBSymbolError": hwInfoPortIBSymbolError,
       "hwInfoPortIBLinkErrorRecovery": hwInfoPortIBLinkErrorRecovery,
       "hwInfoPortIBReceiveErrors": hwInfoPortIBReceiveErrors,
       "hwInfoPortIBRemoteReceiveErrors": hwInfoPortIBRemoteReceiveErrors,
       "hwInfoPortIBReceiveTransmitErrors": hwInfoPortIBReceiveTransmitErrors,
       "hwInfoPortIBNotSendPacakges": hwInfoPortIBNotSendPacakges,
       "hwInfoPortIBReceiveConstraintErrors": hwInfoPortIBReceiveConstraintErrors,
       "hwInfoPortIBLinkErrors": hwInfoPortIBLinkErrors,
       "hwInfoPortIBBufferOverrunErrors": hwInfoPortIBBufferOverrunErrors,
       "hwInfoPortIBStartTime": hwInfoPortIBStartTime,
       "hwInfoPortIBMaxSpeed": hwInfoPortIBMaxSpeed,
       "isoConformance": isoConformance,
       "isoGroups": isoGroups,
       "currentObjectGroup": currentObjectGroup,
       "isoCompliances": isoCompliances,
       "basicCompliance": basicCompliance}
)
