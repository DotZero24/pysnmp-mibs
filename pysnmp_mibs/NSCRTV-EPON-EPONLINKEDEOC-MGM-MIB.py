# SNMP MIB module (NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:36 2025
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

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 eponLinkedEoCManagementObjects) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "eponLinkedEoCManagementObjects")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EocDevInfoTable_Object = MibTable
eocDevInfoTable = _EocDevInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1)
)
if mibBuilder.loadTexts:
    eocDevInfoTable.setStatus("current")
_EocDevInfoEntry_Object = MibTableRow
eocDevInfoEntry = _EocDevInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1)
)
eocDevInfoEntry.setIndexNames(
    (0, "NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB", "eDeviceIndex"),
    (0, "NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB", "eCardIndex"),
    (0, "NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB", "ePortIndex"),
)
if mibBuilder.loadTexts:
    eocDevInfoEntry.setStatus("current")
_EDeviceIndex_Type = EponDeviceIndex
_EDeviceIndex_Object = MibTableColumn
eDeviceIndex = _EDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 1),
    _EDeviceIndex_Type()
)
eDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eDeviceIndex.setStatus("current")
_ECardIndex_Type = EponCardIndex
_ECardIndex_Object = MibTableColumn
eCardIndex = _ECardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 2),
    _ECardIndex_Type()
)
eCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eCardIndex.setStatus("current")
_EPortIndex_Type = EponPortIndex
_EPortIndex_Object = MibTableColumn
ePortIndex = _EPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 3),
    _EPortIndex_Type()
)
ePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ePortIndex.setStatus("current")


class _EocDeviceTechnologyProject_Type(OctetString):
    """Custom type eocDeviceTechnologyProject based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocDeviceTechnologyProject_Type.__name__ = "OctetString"
_EocDeviceTechnologyProject_Object = MibTableColumn
eocDeviceTechnologyProject = _EocDeviceTechnologyProject_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 4),
    _EocDeviceTechnologyProject_Type()
)
eocDeviceTechnologyProject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceTechnologyProject.setStatus("current")


class _EocDeviceVendorName_Type(OctetString):
    """Custom type eocDeviceVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocDeviceVendorName_Type.__name__ = "OctetString"
_EocDeviceVendorName_Object = MibTableColumn
eocDeviceVendorName = _EocDeviceVendorName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 5),
    _EocDeviceVendorName_Type()
)
eocDeviceVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceVendorName.setStatus("current")


class _EocDeviceProductType_Type(OctetString):
    """Custom type eocDeviceProductType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocDeviceProductType_Type.__name__ = "OctetString"
_EocDeviceProductType_Object = MibTableColumn
eocDeviceProductType = _EocDeviceProductType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 6),
    _EocDeviceProductType_Type()
)
eocDeviceProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceProductType.setStatus("current")


class _EocDeviceSoftwareVersion_Type(OctetString):
    """Custom type eocDeviceSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocDeviceSoftwareVersion_Type.__name__ = "OctetString"
_EocDeviceSoftwareVersion_Object = MibTableColumn
eocDeviceSoftwareVersion = _EocDeviceSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 7),
    _EocDeviceSoftwareVersion_Type()
)
eocDeviceSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceSoftwareVersion.setStatus("current")


class _EocDeviceHardwareVersion_Type(OctetString):
    """Custom type eocDeviceHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocDeviceHardwareVersion_Type.__name__ = "OctetString"
_EocDeviceHardwareVersion_Object = MibTableColumn
eocDeviceHardwareVersion = _EocDeviceHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 8),
    _EocDeviceHardwareVersion_Type()
)
eocDeviceHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceHardwareVersion.setStatus("current")


class _EocSeriesNumber_Type(OctetString):
    """Custom type eocSeriesNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_EocSeriesNumber_Type.__name__ = "OctetString"
_EocSeriesNumber_Object = MibTableColumn
eocSeriesNumber = _EocSeriesNumber_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 9),
    _EocSeriesNumber_Type()
)
eocSeriesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocSeriesNumber.setStatus("current")
_EocDeviceIpAddress_Type = IpAddress
_EocDeviceIpAddress_Object = MibTableColumn
eocDeviceIpAddress = _EocDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 10),
    _EocDeviceIpAddress_Type()
)
eocDeviceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocDeviceIpAddress.setStatus("current")
_EocDeviceMacAddress_Type = MacAddress
_EocDeviceMacAddress_Object = MibTableColumn
eocDeviceMacAddress = _EocDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 11),
    _EocDeviceMacAddress_Type()
)
eocDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceMacAddress.setStatus("current")


class _EocDeviceMibVersion_Type(OctetString):
    """Custom type eocDeviceMibVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_EocDeviceMibVersion_Type.__name__ = "OctetString"
_EocDeviceMibVersion_Object = MibTableColumn
eocDeviceMibVersion = _EocDeviceMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 12),
    _EocDeviceMibVersion_Type()
)
eocDeviceMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceMibVersion.setStatus("current")


class _EocDeviceSnmpVersion_Type(Integer32):
    """Custom type eocDeviceSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2c", 2),
          ("v3", 3))
    )


_EocDeviceSnmpVersion_Type.__name__ = "Integer32"
_EocDeviceSnmpVersion_Object = MibTableColumn
eocDeviceSnmpVersion = _EocDeviceSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 13),
    _EocDeviceSnmpVersion_Type()
)
eocDeviceSnmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eocDeviceSnmpVersion.setStatus("current")
_EocDeviceMngVlan_Type = Integer32
_EocDeviceMngVlan_Object = MibTableColumn
eocDeviceMngVlan = _EocDeviceMngVlan_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 14),
    _EocDeviceMngVlan_Type()
)
eocDeviceMngVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocDeviceMngVlan.setStatus("current")
_EocDeviceGateWay_Type = IpAddress
_EocDeviceGateWay_Object = MibTableColumn
eocDeviceGateWay = _EocDeviceGateWay_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 15),
    _EocDeviceGateWay_Type()
)
eocDeviceGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocDeviceGateWay.setStatus("current")
_EocDeviceSubnetMask_Type = IpAddress
_EocDeviceSubnetMask_Object = MibTableColumn
eocDeviceSubnetMask = _EocDeviceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 16),
    _EocDeviceSubnetMask_Type()
)
eocDeviceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocDeviceSubnetMask.setStatus("current")
_EocDeviceReadCommunity_Type = DisplayString
_EocDeviceReadCommunity_Object = MibTableColumn
eocDeviceReadCommunity = _EocDeviceReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 17),
    _EocDeviceReadCommunity_Type()
)
eocDeviceReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocDeviceReadCommunity.setStatus("current")
_EocDeviceWriteCommunity_Type = DisplayString
_EocDeviceWriteCommunity_Object = MibTableColumn
eocDeviceWriteCommunity = _EocDeviceWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 11, 1, 1, 18),
    _EocDeviceWriteCommunity_Type()
)
eocDeviceWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eocDeviceWriteCommunity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB",
    **{"eocDevInfoTable": eocDevInfoTable,
       "eocDevInfoEntry": eocDevInfoEntry,
       "eDeviceIndex": eDeviceIndex,
       "eCardIndex": eCardIndex,
       "ePortIndex": ePortIndex,
       "eocDeviceTechnologyProject": eocDeviceTechnologyProject,
       "eocDeviceVendorName": eocDeviceVendorName,
       "eocDeviceProductType": eocDeviceProductType,
       "eocDeviceSoftwareVersion": eocDeviceSoftwareVersion,
       "eocDeviceHardwareVersion": eocDeviceHardwareVersion,
       "eocSeriesNumber": eocSeriesNumber,
       "eocDeviceIpAddress": eocDeviceIpAddress,
       "eocDeviceMacAddress": eocDeviceMacAddress,
       "eocDeviceMibVersion": eocDeviceMibVersion,
       "eocDeviceSnmpVersion": eocDeviceSnmpVersion,
       "eocDeviceMngVlan": eocDeviceMngVlan,
       "eocDeviceGateWay": eocDeviceGateWay,
       "eocDeviceSubnetMask": eocDeviceSubnetMask,
       "eocDeviceReadCommunity": eocDeviceReadCommunity,
       "eocDeviceWriteCommunity": eocDeviceWriteCommunity}
)
