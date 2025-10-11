# SNMP MIB module (ALVARION-DEVICE-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/ALVARION-DEVICE-EVENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:02 2025
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

(coDevDisIndex,) = mibBuilder.importSymbols(
    "ALVARION-DEVICE-MIB",
    "coDevDisIndex")

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionNotificationEnable,
 AlvarionSSIDOrNone) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionNotificationEnable",
    "AlvarionSSIDOrNone")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

alvarionDeviceEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionDeviceEventMIBObjects_ObjectIdentity = ObjectIdentity
alvarionDeviceEventMIBObjects = _AlvarionDeviceEventMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1)
)
_CoDeviceEventConfigGroup_ObjectIdentity = ObjectIdentity
coDeviceEventConfigGroup = _CoDeviceEventConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1)
)


class _CoDevEvSuccessfulAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvSuccessfulAssociationNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvSuccessfulAssociationNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvSuccessfulAssociationNotificationEnabled_Object = MibScalar
coDevEvSuccessfulAssociationNotificationEnabled = _CoDevEvSuccessfulAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 1),
    _CoDevEvSuccessfulAssociationNotificationEnabled_Type()
)
coDevEvSuccessfulAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvSuccessfulAssociationNotificationEnabled.setStatus("current")


class _CoDevEvAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvAssociationFailureNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvAssociationFailureNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvAssociationFailureNotificationEnabled_Object = MibScalar
coDevEvAssociationFailureNotificationEnabled = _CoDevEvAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 2),
    _CoDevEvAssociationFailureNotificationEnabled_Type()
)
coDevEvAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvAssociationFailureNotificationEnabled.setStatus("current")


class _CoDevEvSuccessfulReAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvSuccessfulReAssociationNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvSuccessfulReAssociationNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvSuccessfulReAssociationNotificationEnabled_Object = MibScalar
coDevEvSuccessfulReAssociationNotificationEnabled = _CoDevEvSuccessfulReAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 3),
    _CoDevEvSuccessfulReAssociationNotificationEnabled_Type()
)
coDevEvSuccessfulReAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvSuccessfulReAssociationNotificationEnabled.setStatus("current")


class _CoDevEvReAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvReAssociationFailureNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvReAssociationFailureNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvReAssociationFailureNotificationEnabled_Object = MibScalar
coDevEvReAssociationFailureNotificationEnabled = _CoDevEvReAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 4),
    _CoDevEvReAssociationFailureNotificationEnabled_Type()
)
coDevEvReAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvReAssociationFailureNotificationEnabled.setStatus("current")


class _CoDevEvSuccessfulAuthenticationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvSuccessfulAuthenticationNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvSuccessfulAuthenticationNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvSuccessfulAuthenticationNotificationEnabled_Object = MibScalar
coDevEvSuccessfulAuthenticationNotificationEnabled = _CoDevEvSuccessfulAuthenticationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 5),
    _CoDevEvSuccessfulAuthenticationNotificationEnabled_Type()
)
coDevEvSuccessfulAuthenticationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvSuccessfulAuthenticationNotificationEnabled.setStatus("current")


class _CoDevEvAuthenticationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvAuthenticationFailureNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvAuthenticationFailureNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvAuthenticationFailureNotificationEnabled_Object = MibScalar
coDevEvAuthenticationFailureNotificationEnabled = _CoDevEvAuthenticationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 6),
    _CoDevEvAuthenticationFailureNotificationEnabled_Type()
)
coDevEvAuthenticationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvAuthenticationFailureNotificationEnabled.setStatus("current")


class _CoDevEvSuccessfulDisAssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvSuccessfulDisAssociationNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvSuccessfulDisAssociationNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvSuccessfulDisAssociationNotificationEnabled_Object = MibScalar
coDevEvSuccessfulDisAssociationNotificationEnabled = _CoDevEvSuccessfulDisAssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 7),
    _CoDevEvSuccessfulDisAssociationNotificationEnabled_Type()
)
coDevEvSuccessfulDisAssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvSuccessfulDisAssociationNotificationEnabled.setStatus("current")


class _CoDevEvDisAssociationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvDisAssociationFailureNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvDisAssociationFailureNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvDisAssociationFailureNotificationEnabled_Object = MibScalar
coDevEvDisAssociationFailureNotificationEnabled = _CoDevEvDisAssociationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 8),
    _CoDevEvDisAssociationFailureNotificationEnabled_Type()
)
coDevEvDisAssociationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvDisAssociationFailureNotificationEnabled.setStatus("current")


class _CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvSuccessfulDeAuthenticationNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Object = MibScalar
coDevEvSuccessfulDeAuthenticationNotificationEnabled = _CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 9),
    _CoDevEvSuccessfulDeAuthenticationNotificationEnabled_Type()
)
coDevEvSuccessfulDeAuthenticationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvSuccessfulDeAuthenticationNotificationEnabled.setStatus("current")


class _CoDevEvDeAuthenticationFailureNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDevEvDeAuthenticationFailureNotificationEnabled based on AlvarionNotificationEnable"""
    defaultValue = 2


_CoDevEvDeAuthenticationFailureNotificationEnabled_Type.__name__ = "AlvarionNotificationEnable"
_CoDevEvDeAuthenticationFailureNotificationEnabled_Object = MibScalar
coDevEvDeAuthenticationFailureNotificationEnabled = _CoDevEvDeAuthenticationFailureNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 1, 10),
    _CoDevEvDeAuthenticationFailureNotificationEnabled_Type()
)
coDevEvDeAuthenticationFailureNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDevEvDeAuthenticationFailureNotificationEnabled.setStatus("current")
_CoDeviceEventInfoGroup_ObjectIdentity = ObjectIdentity
coDeviceEventInfoGroup = _CoDeviceEventInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2)
)
_CoDeviceEventTable_Object = MibTable
coDeviceEventTable = _CoDeviceEventTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceEventTable.setStatus("current")
_CoDeviceEventEntry_Object = MibTableRow
coDeviceEventEntry = _CoDeviceEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1)
)
coDeviceEventEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvIndex"),
)
if mibBuilder.loadTexts:
    coDeviceEventEntry.setStatus("current")


class _CoDevEvIndex_Type(Integer32):
    """Custom type coDevEvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevEvIndex_Type.__name__ = "Integer32"
_CoDevEvIndex_Object = MibTableColumn
coDevEvIndex = _CoDevEvIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1, 1),
    _CoDevEvIndex_Type()
)
coDevEvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevEvIndex.setStatus("current")
_CoDevEvMacAddress_Type = MacAddress
_CoDevEvMacAddress_Object = MibTableColumn
coDevEvMacAddress = _CoDevEvMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 1, 1, 2),
    _CoDevEvMacAddress_Type()
)
coDevEvMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvMacAddress.setStatus("current")
_CoDeviceEventDetailTable_Object = MibTable
coDeviceEventDetailTable = _CoDeviceEventDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2)
)
if mibBuilder.loadTexts:
    coDeviceEventDetailTable.setStatus("current")
_CoDeviceEventDetailEntry_Object = MibTableRow
coDeviceEventDetailEntry = _CoDeviceEventDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1)
)
coDeviceEventDetailEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvIndex"),
    (0, "ALVARION-DEVICE-EVENT-MIB", "coDevEvLogIndex"),
)
if mibBuilder.loadTexts:
    coDeviceEventDetailEntry.setStatus("current")


class _CoDevEvLogIndex_Type(Integer32):
    """Custom type coDevEvLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevEvLogIndex_Type.__name__ = "Integer32"
_CoDevEvLogIndex_Object = MibTableColumn
coDevEvLogIndex = _CoDevEvLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 1),
    _CoDevEvLogIndex_Type()
)
coDevEvLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevEvLogIndex.setStatus("current")
_CoDevEvDetMacAddress_Type = MacAddress
_CoDevEvDetMacAddress_Object = MibTableColumn
coDevEvDetMacAddress = _CoDevEvDetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 2),
    _CoDevEvDetMacAddress_Type()
)
coDevEvDetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvDetMacAddress.setStatus("current")
_CoDevEvTime_Type = DisplayString
_CoDevEvTime_Object = MibTableColumn
coDevEvTime = _CoDevEvTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 3),
    _CoDevEvTime_Type()
)
coDevEvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvTime.setStatus("current")
_CoDevEvSSID_Type = AlvarionSSIDOrNone
_CoDevEvSSID_Object = MibTableColumn
coDevEvSSID = _CoDevEvSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 4),
    _CoDevEvSSID_Type()
)
coDevEvSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvSSID.setStatus("current")


class _CoDevEvRadioIndex_Type(Integer32):
    """Custom type coDevEvRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevEvRadioIndex_Type.__name__ = "Integer32"
_CoDevEvRadioIndex_Object = MibTableColumn
coDevEvRadioIndex = _CoDevEvRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 5),
    _CoDevEvRadioIndex_Type()
)
coDevEvRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvRadioIndex.setStatus("current")
_CoDevEvDuplicateCount_Type = Unsigned32
_CoDevEvDuplicateCount_Object = MibTableColumn
coDevEvDuplicateCount = _CoDevEvDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 6),
    _CoDevEvDuplicateCount_Type()
)
coDevEvDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvDuplicateCount.setStatus("current")


class _CoDevEvCategory_Type(Integer32):
    """Custom type coDevEvCategory based on Integer32"""
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
        *(("wireless", 1),
          ("ieee802dot1x", 2),
          ("wpa", 3),
          ("macAuthentication", 4),
          ("dhcpServer", 5),
          ("pptpL2tp", 6),
          ("ipSec", 7),
          ("unknown", 8))
    )


_CoDevEvCategory_Type.__name__ = "Integer32"
_CoDevEvCategory_Object = MibTableColumn
coDevEvCategory = _CoDevEvCategory_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 7),
    _CoDevEvCategory_Type()
)
coDevEvCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvCategory.setStatus("current")


class _CoDevEvOperation_Type(Integer32):
    """Custom type coDevEvOperation based on Integer32"""
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
        *(("association", 1),
          ("authentication", 2),
          ("authorization", 3),
          ("encryption", 4),
          ("addressAllocation", 5),
          ("vpnAuthentication", 6),
          ("vpnAddressAllocation", 7),
          ("unknown", 8))
    )


_CoDevEvOperation_Type.__name__ = "Integer32"
_CoDevEvOperation_Object = MibTableColumn
coDevEvOperation = _CoDevEvOperation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 8),
    _CoDevEvOperation_Type()
)
coDevEvOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvOperation.setStatus("current")
_CoDevEvStatus_Type = DisplayString
_CoDevEvStatus_Object = MibTableColumn
coDevEvStatus = _CoDevEvStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 9),
    _CoDevEvStatus_Type()
)
coDevEvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvStatus.setStatus("current")
_CoDevEvOptionalData_Type = DisplayString
_CoDevEvOptionalData_Object = MibTableColumn
coDevEvOptionalData = _CoDevEvOptionalData_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 1, 2, 2, 1, 10),
    _CoDevEvOptionalData_Type()
)
coDevEvOptionalData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevEvOptionalData.setStatus("current")
_AlvarionDeviceEventMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionDeviceEventMIBNotificationPrefix = _AlvarionDeviceEventMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2)
)
_AlvarionDeviceEventMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionDeviceEventMIBNotifications = _AlvarionDeviceEventMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0)
)
_AlvarionDeviceEventMIBConformance_ObjectIdentity = ObjectIdentity
alvarionDeviceEventMIBConformance = _AlvarionDeviceEventMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3)
)
_AlvarionDeviceEventMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionDeviceEventMIBCompliances = _AlvarionDeviceEventMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 1)
)
_AlvarionDeviceEventMIBGroups_ObjectIdentity = ObjectIdentity
alvarionDeviceEventMIBGroups = _AlvarionDeviceEventMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2)
)

# Managed Objects groups

alvarionDeviceEventConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 1)
)
alvarionDeviceEventConfigMIBGroup.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulAssociationNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvAssociationFailureNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulReAssociationNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvReAssociationFailureNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulAuthenticationNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvAuthenticationFailureNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulDisAssociationNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDisAssociationFailureNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSuccessfulDeAuthenticationNotificationEnabled"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDeAuthenticationFailureNotificationEnabled"))
)
if mibBuilder.loadTexts:
    alvarionDeviceEventConfigMIBGroup.setStatus("current")

alvarionDeviceEventInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 2)
)
alvarionDeviceEventInfoMIBGroup.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDetMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvTime"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvRadioIndex"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvDuplicateCount"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvCategory"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOperation"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    alvarionDeviceEventInfoMIBGroup.setStatus("current")


# Notification objects

coDeviceEventSuccessfulAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 1)
)
coDeviceEventSuccessfulAssociation.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventSuccessfulAssociation.setStatus(
        "current"
    )

coDeviceEventAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 2)
)
coDeviceEventAssociationFailure.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventAssociationFailure.setStatus(
        "current"
    )

coDeviceEventSuccessfulReAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 3)
)
coDeviceEventSuccessfulReAssociation.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventSuccessfulReAssociation.setStatus(
        "current"
    )

coDeviceEventReAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 4)
)
coDeviceEventReAssociationFailure.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventReAssociationFailure.setStatus(
        "current"
    )

coDeviceEventSuccessfulAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 5)
)
coDeviceEventSuccessfulAuthentication.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventSuccessfulAuthentication.setStatus(
        "current"
    )

coDeviceEventAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 6)
)
coDeviceEventAuthenticationFailure.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventAuthenticationFailure.setStatus(
        "current"
    )

coDeviceEventSuccessfulDisAssociation = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 7)
)
coDeviceEventSuccessfulDisAssociation.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventSuccessfulDisAssociation.setStatus(
        "current"
    )

coDeviceEventDisAssociationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 8)
)
coDeviceEventDisAssociationFailure.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventDisAssociationFailure.setStatus(
        "current"
    )

coDeviceEventSuccessfulDeAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 9)
)
coDeviceEventSuccessfulDeAuthentication.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventSuccessfulDeAuthentication.setStatus(
        "current"
    )

coDeviceEventDeAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 2, 0, 10)
)
coDeviceEventDeAuthenticationFailure.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDevEvMacAddress"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvSSID"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvStatus"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDevEvOptionalData"))
)
if mibBuilder.loadTexts:
    coDeviceEventDeAuthenticationFailure.setStatus(
        "current"
    )


# Notifications groups

alvarionDeviceEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 2, 3)
)
alvarionDeviceEventNotificationGroup.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAssociation"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventAssociationFailure"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulReAssociation"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventReAssociationFailure"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulAuthentication"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventAuthenticationFailure"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDisAssociation"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventDisAssociationFailure"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventSuccessfulDeAuthentication"),
        ("ALVARION-DEVICE-EVENT-MIB", "coDeviceEventDeAuthenticationFailure"))
)
if mibBuilder.loadTexts:
    alvarionDeviceEventNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alvarionDeviceEventMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 26, 3, 1, 1)
)
alvarionDeviceEventMIBCompliance.setObjects(
      *(("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventConfigMIBGroup"),
        ("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventInfoMIBGroup"),
        ("ALVARION-DEVICE-EVENT-MIB", "alvarionDeviceEventNotificationGroup"))
)
if mibBuilder.loadTexts:
    alvarionDeviceEventMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-DEVICE-EVENT-MIB",
    **{"alvarionDeviceEventMIB": alvarionDeviceEventMIB,
       "alvarionDeviceEventMIBObjects": alvarionDeviceEventMIBObjects,
       "coDeviceEventConfigGroup": coDeviceEventConfigGroup,
       "coDevEvSuccessfulAssociationNotificationEnabled": coDevEvSuccessfulAssociationNotificationEnabled,
       "coDevEvAssociationFailureNotificationEnabled": coDevEvAssociationFailureNotificationEnabled,
       "coDevEvSuccessfulReAssociationNotificationEnabled": coDevEvSuccessfulReAssociationNotificationEnabled,
       "coDevEvReAssociationFailureNotificationEnabled": coDevEvReAssociationFailureNotificationEnabled,
       "coDevEvSuccessfulAuthenticationNotificationEnabled": coDevEvSuccessfulAuthenticationNotificationEnabled,
       "coDevEvAuthenticationFailureNotificationEnabled": coDevEvAuthenticationFailureNotificationEnabled,
       "coDevEvSuccessfulDisAssociationNotificationEnabled": coDevEvSuccessfulDisAssociationNotificationEnabled,
       "coDevEvDisAssociationFailureNotificationEnabled": coDevEvDisAssociationFailureNotificationEnabled,
       "coDevEvSuccessfulDeAuthenticationNotificationEnabled": coDevEvSuccessfulDeAuthenticationNotificationEnabled,
       "coDevEvDeAuthenticationFailureNotificationEnabled": coDevEvDeAuthenticationFailureNotificationEnabled,
       "coDeviceEventInfoGroup": coDeviceEventInfoGroup,
       "coDeviceEventTable": coDeviceEventTable,
       "coDeviceEventEntry": coDeviceEventEntry,
       "coDevEvIndex": coDevEvIndex,
       "coDevEvMacAddress": coDevEvMacAddress,
       "coDeviceEventDetailTable": coDeviceEventDetailTable,
       "coDeviceEventDetailEntry": coDeviceEventDetailEntry,
       "coDevEvLogIndex": coDevEvLogIndex,
       "coDevEvDetMacAddress": coDevEvDetMacAddress,
       "coDevEvTime": coDevEvTime,
       "coDevEvSSID": coDevEvSSID,
       "coDevEvRadioIndex": coDevEvRadioIndex,
       "coDevEvDuplicateCount": coDevEvDuplicateCount,
       "coDevEvCategory": coDevEvCategory,
       "coDevEvOperation": coDevEvOperation,
       "coDevEvStatus": coDevEvStatus,
       "coDevEvOptionalData": coDevEvOptionalData,
       "alvarionDeviceEventMIBNotificationPrefix": alvarionDeviceEventMIBNotificationPrefix,
       "alvarionDeviceEventMIBNotifications": alvarionDeviceEventMIBNotifications,
       "coDeviceEventSuccessfulAssociation": coDeviceEventSuccessfulAssociation,
       "coDeviceEventAssociationFailure": coDeviceEventAssociationFailure,
       "coDeviceEventSuccessfulReAssociation": coDeviceEventSuccessfulReAssociation,
       "coDeviceEventReAssociationFailure": coDeviceEventReAssociationFailure,
       "coDeviceEventSuccessfulAuthentication": coDeviceEventSuccessfulAuthentication,
       "coDeviceEventAuthenticationFailure": coDeviceEventAuthenticationFailure,
       "coDeviceEventSuccessfulDisAssociation": coDeviceEventSuccessfulDisAssociation,
       "coDeviceEventDisAssociationFailure": coDeviceEventDisAssociationFailure,
       "coDeviceEventSuccessfulDeAuthentication": coDeviceEventSuccessfulDeAuthentication,
       "coDeviceEventDeAuthenticationFailure": coDeviceEventDeAuthenticationFailure,
       "alvarionDeviceEventMIBConformance": alvarionDeviceEventMIBConformance,
       "alvarionDeviceEventMIBCompliances": alvarionDeviceEventMIBCompliances,
       "alvarionDeviceEventMIBCompliance": alvarionDeviceEventMIBCompliance,
       "alvarionDeviceEventMIBGroups": alvarionDeviceEventMIBGroups,
       "alvarionDeviceEventConfigMIBGroup": alvarionDeviceEventConfigMIBGroup,
       "alvarionDeviceEventInfoMIBGroup": alvarionDeviceEventInfoMIBGroup,
       "alvarionDeviceEventNotificationGroup": alvarionDeviceEventNotificationGroup}
)
