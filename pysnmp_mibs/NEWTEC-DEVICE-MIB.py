# SNMP MIB module (NEWTEC-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-DEVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:01 2025
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

(Float32TC,) = mibBuilder.importSymbols(
    "FLOAT-TC-MIB",
    "Float32TC")

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable")

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

ntcDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100)
)
if mibBuilder.loadTexts:
    ntcDevice.setRevisions(
        ("2017-10-23 12:00",
         "2017-07-10 12:00",
         "2016-08-05 08:00",
         "2016-05-17 09:00",
         "2015-10-19 11:00",
         "2015-09-25 11:00",
         "2015-04-13 07:00",
         "2014-09-09 09:00",
         "2014-07-08 09:00",
         "2014-03-18 12:00",
         "2013-05-22 06:00",
         "2013-01-08 12:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcDevObjects_ObjectIdentity = ObjectIdentity
ntcDevObjects = _NtcDevObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1)
)
if mibBuilder.loadTexts:
    ntcDevObjects.setStatus("current")
_NtcDevIdentification_ObjectIdentity = ObjectIdentity
ntcDevIdentification = _NtcDevIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1)
)
if mibBuilder.loadTexts:
    ntcDevIdentification.setStatus("current")


class _NtcDevIdLabel_Type(DisplayString):
    """Custom type ntcDevIdLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NtcDevIdLabel_Type.__name__ = "DisplayString"
_NtcDevIdLabel_Object = MibScalar
ntcDevIdLabel = _NtcDevIdLabel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 1),
    _NtcDevIdLabel_Type()
)
ntcDevIdLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevIdLabel.setStatus("current")


class _NtcDevIdSerialNumber_Type(DisplayString):
    """Custom type ntcDevIdSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevIdSerialNumber_Type.__name__ = "DisplayString"
_NtcDevIdSerialNumber_Object = MibScalar
ntcDevIdSerialNumber = _NtcDevIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 2),
    _NtcDevIdSerialNumber_Type()
)
ntcDevIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdSerialNumber.setStatus("current")


class _NtcDevIdUniqueId_Type(DisplayString):
    """Custom type ntcDevIdUniqueId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevIdUniqueId_Type.__name__ = "DisplayString"
_NtcDevIdUniqueId_Object = MibScalar
ntcDevIdUniqueId = _NtcDevIdUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 3),
    _NtcDevIdUniqueId_Type()
)
ntcDevIdUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdUniqueId.setStatus("current")


class _NtcDevIdProduct_Type(DisplayString):
    """Custom type ntcDevIdProduct based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcDevIdProduct_Type.__name__ = "DisplayString"
_NtcDevIdProduct_Object = MibScalar
ntcDevIdProduct = _NtcDevIdProduct_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 4),
    _NtcDevIdProduct_Type()
)
ntcDevIdProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdProduct.setStatus("current")


class _NtcDevIdDeviceDescription_Type(DisplayString):
    """Custom type ntcDevIdDeviceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevIdDeviceDescription_Type.__name__ = "DisplayString"
_NtcDevIdDeviceDescription_Object = MibScalar
ntcDevIdDeviceDescription = _NtcDevIdDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 5),
    _NtcDevIdDeviceDescription_Type()
)
ntcDevIdDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdDeviceDescription.setStatus("current")


class _NtcDevIdTypeId_Type(DisplayString):
    """Custom type ntcDevIdTypeId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevIdTypeId_Type.__name__ = "DisplayString"
_NtcDevIdTypeId_Object = MibScalar
ntcDevIdTypeId = _NtcDevIdTypeId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 6),
    _NtcDevIdTypeId_Type()
)
ntcDevIdTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdTypeId.setStatus("current")


class _NtcDevIdHardwareRevision_Type(DisplayString):
    """Custom type ntcDevIdHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevIdHardwareRevision_Type.__name__ = "DisplayString"
_NtcDevIdHardwareRevision_Object = MibScalar
ntcDevIdHardwareRevision = _NtcDevIdHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 7),
    _NtcDevIdHardwareRevision_Type()
)
ntcDevIdHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdHardwareRevision.setStatus("current")


class _NtcDevIdSoftwareId_Type(DisplayString):
    """Custom type ntcDevIdSoftwareId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NtcDevIdSoftwareId_Type.__name__ = "DisplayString"
_NtcDevIdSoftwareId_Object = MibScalar
ntcDevIdSoftwareId = _NtcDevIdSoftwareId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 8),
    _NtcDevIdSoftwareId_Type()
)
ntcDevIdSoftwareId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdSoftwareId.setStatus("current")


class _NtcDevIdSoftwareVersion_Type(DisplayString):
    """Custom type ntcDevIdSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevIdSoftwareVersion_Type.__name__ = "DisplayString"
_NtcDevIdSoftwareVersion_Object = MibScalar
ntcDevIdSoftwareVersion = _NtcDevIdSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 9),
    _NtcDevIdSoftwareVersion_Type()
)
ntcDevIdSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdSoftwareVersion.setStatus("current")
_NtcDevIdDeviceOptionsTable_Object = MibTable
ntcDevIdDeviceOptionsTable = _NtcDevIdDeviceOptionsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 10)
)
if mibBuilder.loadTexts:
    ntcDevIdDeviceOptionsTable.setStatus("current")
_NtcDevIdDeviceOptionsEntry_Object = MibTableRow
ntcDevIdDeviceOptionsEntry = _NtcDevIdDeviceOptionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 10, 1)
)
ntcDevIdDeviceOptionsEntry.setIndexNames(
    (0, "NEWTEC-DEVICE-MIB", "ntcDevIdDeviceOptionsSalesCode"),
)
if mibBuilder.loadTexts:
    ntcDevIdDeviceOptionsEntry.setStatus("current")


class _NtcDevIdDeviceOptionsSalesCode_Type(DisplayString):
    """Custom type ntcDevIdDeviceOptionsSalesCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_NtcDevIdDeviceOptionsSalesCode_Type.__name__ = "DisplayString"
_NtcDevIdDeviceOptionsSalesCode_Object = MibTableColumn
ntcDevIdDeviceOptionsSalesCode = _NtcDevIdDeviceOptionsSalesCode_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 10, 1, 1),
    _NtcDevIdDeviceOptionsSalesCode_Type()
)
ntcDevIdDeviceOptionsSalesCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDevIdDeviceOptionsSalesCode.setStatus("current")


class _NtcDevIdDeviceOptionsDescription_Type(DisplayString):
    """Custom type ntcDevIdDeviceOptionsDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtcDevIdDeviceOptionsDescription_Type.__name__ = "DisplayString"
_NtcDevIdDeviceOptionsDescription_Object = MibTableColumn
ntcDevIdDeviceOptionsDescription = _NtcDevIdDeviceOptionsDescription_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 10, 1, 2),
    _NtcDevIdDeviceOptionsDescription_Type()
)
ntcDevIdDeviceOptionsDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdDeviceOptionsDescription.setStatus("current")


class _NtcDevIdLicenseType_Type(Integer32):
    """Custom type ntcDevIdLicenseType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permanent", 0),
          ("temporaryEndDate", 1),
          ("temporaryCredits", 2),
          ("temporaryCreditsUnderRedundancy", 3))
    )


_NtcDevIdLicenseType_Type.__name__ = "Integer32"
_NtcDevIdLicenseType_Object = MibScalar
ntcDevIdLicenseType = _NtcDevIdLicenseType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 11),
    _NtcDevIdLicenseType_Type()
)
ntcDevIdLicenseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdLicenseType.setStatus("current")


class _NtcDevIdLicenseTimeRemain_Type(DisplayString):
    """Custom type ntcDevIdLicenseTimeRemain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NtcDevIdLicenseTimeRemain_Type.__name__ = "DisplayString"
_NtcDevIdLicenseTimeRemain_Object = MibScalar
ntcDevIdLicenseTimeRemain = _NtcDevIdLicenseTimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 1, 12),
    _NtcDevIdLicenseTimeRemain_Type()
)
ntcDevIdLicenseTimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevIdLicenseTimeRemain.setStatus("current")
_NtcDevFrontPanel_ObjectIdentity = ObjectIdentity
ntcDevFrontPanel = _NtcDevFrontPanel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 2)
)
if mibBuilder.loadTexts:
    ntcDevFrontPanel.setStatus("current")


class _NtcDevFpEnable_Type(NtcEnable):
    """Custom type ntcDevFpEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevFpEnable_Type.__name__ = "NtcEnable"
_NtcDevFpEnable_Object = MibScalar
ntcDevFpEnable = _NtcDevFpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 2, 1),
    _NtcDevFpEnable_Type()
)
ntcDevFpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevFpEnable.setStatus("current")


class _NtcDevFpiAccessLevel_Type(Integer32):
    """Custom type ntcDevFpiAccessLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 0),
          ("operator", 1),
          ("expert", 2))
    )


_NtcDevFpiAccessLevel_Type.__name__ = "Integer32"
_NtcDevFpiAccessLevel_Object = MibScalar
ntcDevFpiAccessLevel = _NtcDevFpiAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 2, 2),
    _NtcDevFpiAccessLevel_Type()
)
ntcDevFpiAccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevFpiAccessLevel.setStatus("current")
_NtcDevSnmp_ObjectIdentity = ObjectIdentity
ntcDevSnmp = _NtcDevSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3)
)
if mibBuilder.loadTexts:
    ntcDevSnmp.setStatus("current")
_NtcDevSnmpNotification_ObjectIdentity = ObjectIdentity
ntcDevSnmpNotification = _NtcDevSnmpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ntcDevSnmpNotification.setStatus("current")
_NtcDevSnmpNotifDestTable_Object = MibTable
ntcDevSnmpNotifDestTable = _NtcDevSnmpNotifDestTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ntcDevSnmpNotifDestTable.setStatus("current")
_NtcDevSnmpNotifDestEntry_Object = MibTableRow
ntcDevSnmpNotifDestEntry = _NtcDevSnmpNotifDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1, 1, 1)
)
ntcDevSnmpNotifDestEntry.setIndexNames(
    (0, "NEWTEC-DEVICE-MIB", "ntcDevSnmpNotifDestDestination"),
)
if mibBuilder.loadTexts:
    ntcDevSnmpNotifDestEntry.setStatus("current")


class _NtcDevSnmpNotifDestDestination_Type(Unsigned32):
    """Custom type ntcDevSnmpNotifDestDestination based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NtcDevSnmpNotifDestDestination_Type.__name__ = "Unsigned32"
_NtcDevSnmpNotifDestDestination_Object = MibTableColumn
ntcDevSnmpNotifDestDestination = _NtcDevSnmpNotifDestDestination_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1, 1, 1, 1),
    _NtcDevSnmpNotifDestDestination_Type()
)
ntcDevSnmpNotifDestDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDevSnmpNotifDestDestination.setStatus("current")


class _NtcDevSnmpNotifDestIpAddress_Type(IpAddress):
    """Custom type ntcDevSnmpNotifDestIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NtcDevSnmpNotifDestIpAddress_Type.__name__ = "IpAddress"
_NtcDevSnmpNotifDestIpAddress_Object = MibTableColumn
ntcDevSnmpNotifDestIpAddress = _NtcDevSnmpNotifDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1, 1, 1, 2),
    _NtcDevSnmpNotifDestIpAddress_Type()
)
ntcDevSnmpNotifDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevSnmpNotifDestIpAddress.setStatus("current")


class _NtcDevSnmpNotifDestType_Type(Integer32):
    """Custom type ntcDevSnmpNotifDestType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trapV1", 0),
          ("trapV2", 1),
          ("inform", 2))
    )


_NtcDevSnmpNotifDestType_Type.__name__ = "Integer32"
_NtcDevSnmpNotifDestType_Object = MibTableColumn
ntcDevSnmpNotifDestType = _NtcDevSnmpNotifDestType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1, 1, 1, 3),
    _NtcDevSnmpNotifDestType_Type()
)
ntcDevSnmpNotifDestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevSnmpNotifDestType.setStatus("current")


class _NtcDevSnmpNotifDestCommunity_Type(DisplayString):
    """Custom type ntcDevSnmpNotifDestCommunity based on DisplayString"""
    defaultValue = OctetString("trapcom")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_NtcDevSnmpNotifDestCommunity_Type.__name__ = "DisplayString"
_NtcDevSnmpNotifDestCommunity_Object = MibTableColumn
ntcDevSnmpNotifDestCommunity = _NtcDevSnmpNotifDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 3, 1, 1, 1, 4),
    _NtcDevSnmpNotifDestCommunity_Type()
)
ntcDevSnmpNotifDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevSnmpNotifDestCommunity.setStatus("current")
_NtcDevCli_ObjectIdentity = ObjectIdentity
ntcDevCli = _NtcDevCli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 4)
)
if mibBuilder.loadTexts:
    ntcDevCli.setStatus("current")


class _NtcDevCliRemoteEnable_Type(NtcEnable):
    """Custom type ntcDevCliRemoteEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevCliRemoteEnable_Type.__name__ = "NtcEnable"
_NtcDevCliRemoteEnable_Object = MibScalar
ntcDevCliRemoteEnable = _NtcDevCliRemoteEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 4, 1),
    _NtcDevCliRemoteEnable_Type()
)
ntcDevCliRemoteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevCliRemoteEnable.setStatus("current")


class _NtcDevCliInactivityTimeout_Type(Unsigned32):
    """Custom type ntcDevCliInactivityTimeout based on Unsigned32"""
    defaultValue = 600


_NtcDevCliInactivityTimeout_Type.__name__ = "Unsigned32"
_NtcDevCliInactivityTimeout_Object = MibScalar
ntcDevCliInactivityTimeout = _NtcDevCliInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 4, 2),
    _NtcDevCliInactivityTimeout_Type()
)
ntcDevCliInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevCliInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ntcDevCliInactivityTimeout.setUnits("s")
_NtcDevGui_ObjectIdentity = ObjectIdentity
ntcDevGui = _NtcDevGui_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 5)
)
if mibBuilder.loadTexts:
    ntcDevGui.setStatus("current")


class _NtcDevGuiEnable_Type(NtcEnable):
    """Custom type ntcDevGuiEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevGuiEnable_Type.__name__ = "NtcEnable"
_NtcDevGuiEnable_Object = MibScalar
ntcDevGuiEnable = _NtcDevGuiEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 5, 1),
    _NtcDevGuiEnable_Type()
)
ntcDevGuiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevGuiEnable.setStatus("current")
_NtcDevFtp_ObjectIdentity = ObjectIdentity
ntcDevFtp = _NtcDevFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 6)
)
if mibBuilder.loadTexts:
    ntcDevFtp.setStatus("current")


class _NtcDevFtpEnable_Type(NtcEnable):
    """Custom type ntcDevFtpEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevFtpEnable_Type.__name__ = "NtcEnable"
_NtcDevFtpEnable_Object = MibScalar
ntcDevFtpEnable = _NtcDevFtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 6, 1),
    _NtcDevFtpEnable_Type()
)
ntcDevFtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevFtpEnable.setStatus("current")


class _NtcDevFtpAnonymousEnable_Type(NtcEnable):
    """Custom type ntcDevFtpAnonymousEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevFtpAnonymousEnable_Type.__name__ = "NtcEnable"
_NtcDevFtpAnonymousEnable_Object = MibScalar
ntcDevFtpAnonymousEnable = _NtcDevFtpAnonymousEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 6, 2),
    _NtcDevFtpAnonymousEnable_Type()
)
ntcDevFtpAnonymousEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevFtpAnonymousEnable.setStatus("current")
_NtcDevLog_ObjectIdentity = ObjectIdentity
ntcDevLog = _NtcDevLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7)
)
if mibBuilder.loadTexts:
    ntcDevLog.setStatus("current")
_NtcDevLogLocal_ObjectIdentity = ObjectIdentity
ntcDevLogLocal = _NtcDevLogLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ntcDevLogLocal.setStatus("current")


class _NtcDevLogLocEnable_Type(NtcEnable):
    """Custom type ntcDevLogLocEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevLogLocEnable_Type.__name__ = "NtcEnable"
_NtcDevLogLocEnable_Object = MibScalar
ntcDevLogLocEnable = _NtcDevLogLocEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 1, 1),
    _NtcDevLogLocEnable_Type()
)
ntcDevLogLocEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevLogLocEnable.setStatus("current")
_NtcDevLogRemote_ObjectIdentity = ObjectIdentity
ntcDevLogRemote = _NtcDevLogRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 2)
)
if mibBuilder.loadTexts:
    ntcDevLogRemote.setStatus("current")


class _NtcDevLogRemEnable_Type(NtcEnable):
    """Custom type ntcDevLogRemEnable based on NtcEnable"""
    defaultValue = 0


_NtcDevLogRemEnable_Type.__name__ = "NtcEnable"
_NtcDevLogRemEnable_Object = MibScalar
ntcDevLogRemEnable = _NtcDevLogRemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 2, 1),
    _NtcDevLogRemEnable_Type()
)
ntcDevLogRemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevLogRemEnable.setStatus("current")


class _NtcDevLogRemIpAddress_Type(IpAddress):
    """Custom type ntcDevLogRemIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NtcDevLogRemIpAddress_Type.__name__ = "IpAddress"
_NtcDevLogRemIpAddress_Object = MibScalar
ntcDevLogRemIpAddress = _NtcDevLogRemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 2, 2),
    _NtcDevLogRemIpAddress_Type()
)
ntcDevLogRemIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevLogRemIpAddress.setStatus("current")


class _NtcDevLogRemUdpPort_Type(Unsigned32):
    """Custom type ntcDevLogRemUdpPort based on Unsigned32"""
    defaultValue = 514

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcDevLogRemUdpPort_Type.__name__ = "Unsigned32"
_NtcDevLogRemUdpPort_Object = MibScalar
ntcDevLogRemUdpPort = _NtcDevLogRemUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 2, 3),
    _NtcDevLogRemUdpPort_Type()
)
ntcDevLogRemUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevLogRemUdpPort.setStatus("current")
_NtcDevLogFilterTable_Object = MibTable
ntcDevLogFilterTable = _NtcDevLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 3)
)
if mibBuilder.loadTexts:
    ntcDevLogFilterTable.setStatus("current")
_NtcDevLogFilterEntry_Object = MibTableRow
ntcDevLogFilterEntry = _NtcDevLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 3, 1)
)
ntcDevLogFilterEntry.setIndexNames(
    (0, "NEWTEC-DEVICE-MIB", "ntcDevLogFilterFacility"),
)
if mibBuilder.loadTexts:
    ntcDevLogFilterEntry.setStatus("current")


class _NtcDevLogFilterFacility_Type(DisplayString):
    """Custom type ntcDevLogFilterFacility based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcDevLogFilterFacility_Type.__name__ = "DisplayString"
_NtcDevLogFilterFacility_Object = MibTableColumn
ntcDevLogFilterFacility = _NtcDevLogFilterFacility_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 3, 1, 1),
    _NtcDevLogFilterFacility_Type()
)
ntcDevLogFilterFacility.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDevLogFilterFacility.setStatus("current")


class _NtcDevLogFilterLevel_Type(Integer32):
    """Custom type ntcDevLogFilterLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("off", 0),
          ("trace", 1),
          ("debug", 2),
          ("info", 3),
          ("notice", 4),
          ("warn", 5),
          ("error", 6),
          ("alert", 7),
          ("emerg", 8))
    )


_NtcDevLogFilterLevel_Type.__name__ = "Integer32"
_NtcDevLogFilterLevel_Object = MibTableColumn
ntcDevLogFilterLevel = _NtcDevLogFilterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 7, 3, 1, 2),
    _NtcDevLogFilterLevel_Type()
)
ntcDevLogFilterLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevLogFilterLevel.setStatus("current")
_NtcDevDateTime_ObjectIdentity = ObjectIdentity
ntcDevDateTime = _NtcDevDateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8)
)
if mibBuilder.loadTexts:
    ntcDevDateTime.setStatus("current")


class _NtcDevDtDate_Type(DisplayString):
    """Custom type ntcDevDtDate based on DisplayString"""
    defaultValue = OctetString("01/01/2001")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_NtcDevDtDate_Type.__name__ = "DisplayString"
_NtcDevDtDate_Object = MibScalar
ntcDevDtDate = _NtcDevDtDate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 1),
    _NtcDevDtDate_Type()
)
ntcDevDtDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevDtDate.setStatus("current")


class _NtcDevDtTime_Type(DisplayString):
    """Custom type ntcDevDtTime based on DisplayString"""
    defaultValue = OctetString("00:00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_NtcDevDtTime_Type.__name__ = "DisplayString"
_NtcDevDtTime_Object = MibScalar
ntcDevDtTime = _NtcDevDtTime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 2),
    _NtcDevDtTime_Type()
)
ntcDevDtTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevDtTime.setStatus("current")
_NtcDevDtNtp_ObjectIdentity = ObjectIdentity
ntcDevDtNtp = _NtcDevDtNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 3)
)
if mibBuilder.loadTexts:
    ntcDevDtNtp.setStatus("current")


class _NtcDevDtNtpEnable_Type(NtcEnable):
    """Custom type ntcDevDtNtpEnable based on NtcEnable"""
    defaultValue = 0


_NtcDevDtNtpEnable_Type.__name__ = "NtcEnable"
_NtcDevDtNtpEnable_Object = MibScalar
ntcDevDtNtpEnable = _NtcDevDtNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 3, 1),
    _NtcDevDtNtpEnable_Type()
)
ntcDevDtNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevDtNtpEnable.setStatus("current")
_NtcDevDtNtpPeerTable_Object = MibTable
ntcDevDtNtpPeerTable = _NtcDevDtNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 3, 2)
)
if mibBuilder.loadTexts:
    ntcDevDtNtpPeerTable.setStatus("current")
_NtcDevDtNtpPeerEntry_Object = MibTableRow
ntcDevDtNtpPeerEntry = _NtcDevDtNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 3, 2, 1)
)
ntcDevDtNtpPeerEntry.setIndexNames(
    (0, "NEWTEC-DEVICE-MIB", "ntcDevDtNtpPeerPeer"),
)
if mibBuilder.loadTexts:
    ntcDevDtNtpPeerEntry.setStatus("current")
_NtcDevDtNtpPeerPeer_Type = Unsigned32
_NtcDevDtNtpPeerPeer_Object = MibTableColumn
ntcDevDtNtpPeerPeer = _NtcDevDtNtpPeerPeer_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 3, 2, 1, 1),
    _NtcDevDtNtpPeerPeer_Type()
)
ntcDevDtNtpPeerPeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDevDtNtpPeerPeer.setStatus("current")


class _NtcDevDtNtpPeerIpAddress_Type(IpAddress):
    """Custom type ntcDevDtNtpPeerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NtcDevDtNtpPeerIpAddress_Type.__name__ = "IpAddress"
_NtcDevDtNtpPeerIpAddress_Object = MibTableColumn
ntcDevDtNtpPeerIpAddress = _NtcDevDtNtpPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 8, 3, 2, 1, 2),
    _NtcDevDtNtpPeerIpAddress_Type()
)
ntcDevDtNtpPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevDtNtpPeerIpAddress.setStatus("current")
_NtcDevMonitor_ObjectIdentity = ObjectIdentity
ntcDevMonitor = _NtcDevMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9)
)
if mibBuilder.loadTexts:
    ntcDevMonitor.setStatus("current")
_NtcDevMonTemperature_Type = Integer32
_NtcDevMonTemperature_Object = MibScalar
ntcDevMonTemperature = _NtcDevMonTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 1),
    _NtcDevMonTemperature_Type()
)
ntcDevMonTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ntcDevMonTemperature.setUnits("Celsius")
_NtcDevMonPowerSupply_Type = Integer32
_NtcDevMonPowerSupply_Object = MibScalar
ntcDevMonPowerSupply = _NtcDevMonPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 2),
    _NtcDevMonPowerSupply_Type()
)
ntcDevMonPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonPowerSupply.setStatus("current")
if mibBuilder.loadTexts:
    ntcDevMonPowerSupply.setUnits("V")


class _NtcDevMonCpuLoad_Type(DisplayString):
    """Custom type ntcDevMonCpuLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_NtcDevMonCpuLoad_Type.__name__ = "DisplayString"
_NtcDevMonCpuLoad_Object = MibScalar
ntcDevMonCpuLoad = _NtcDevMonCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 3),
    _NtcDevMonCpuLoad_Type()
)
ntcDevMonCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonCpuLoad.setStatus("current")


class _NtcDevMonMemoryUse_Type(Unsigned32):
    """Custom type ntcDevMonMemoryUse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtcDevMonMemoryUse_Type.__name__ = "Unsigned32"
_NtcDevMonMemoryUse_Object = MibScalar
ntcDevMonMemoryUse = _NtcDevMonMemoryUse_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 4),
    _NtcDevMonMemoryUse_Type()
)
ntcDevMonMemoryUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonMemoryUse.setStatus("current")
if mibBuilder.loadTexts:
    ntcDevMonMemoryUse.setUnits("%")


class _NtcDevMonUptime_Type(DisplayString):
    """Custom type ntcDevMonUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NtcDevMonUptime_Type.__name__ = "DisplayString"
_NtcDevMonUptime_Object = MibScalar
ntcDevMonUptime = _NtcDevMonUptime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 5),
    _NtcDevMonUptime_Type()
)
ntcDevMonUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonUptime.setStatus("current")
_NtcDevMonSensorsTable_Object = MibTable
ntcDevMonSensorsTable = _NtcDevMonSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 6)
)
if mibBuilder.loadTexts:
    ntcDevMonSensorsTable.setStatus("current")
_NtcDevMonSensorsEntry_Object = MibTableRow
ntcDevMonSensorsEntry = _NtcDevMonSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 6, 1)
)
ntcDevMonSensorsEntry.setIndexNames(
    (0, "NEWTEC-DEVICE-MIB", "ntcDevMonSensorsSensor"),
)
if mibBuilder.loadTexts:
    ntcDevMonSensorsEntry.setStatus("current")


class _NtcDevMonSensorsSensor_Type(DisplayString):
    """Custom type ntcDevMonSensorsSensor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcDevMonSensorsSensor_Type.__name__ = "DisplayString"
_NtcDevMonSensorsSensor_Object = MibTableColumn
ntcDevMonSensorsSensor = _NtcDevMonSensorsSensor_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 6, 1, 1),
    _NtcDevMonSensorsSensor_Type()
)
ntcDevMonSensorsSensor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcDevMonSensorsSensor.setStatus("current")


class _NtcDevMonSensorsValue_Type(DisplayString):
    """Custom type ntcDevMonSensorsValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcDevMonSensorsValue_Type.__name__ = "DisplayString"
_NtcDevMonSensorsValue_Object = MibTableColumn
ntcDevMonSensorsValue = _NtcDevMonSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 6, 1, 2),
    _NtcDevMonSensorsValue_Type()
)
ntcDevMonSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonSensorsValue.setStatus("current")


class _NtcDevMonHwFailureCause_Type(DisplayString):
    """Custom type ntcDevMonHwFailureCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevMonHwFailureCause_Type.__name__ = "DisplayString"
_NtcDevMonHwFailureCause_Object = MibScalar
ntcDevMonHwFailureCause = _NtcDevMonHwFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 7),
    _NtcDevMonHwFailureCause_Type()
)
ntcDevMonHwFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonHwFailureCause.setStatus("current")


class _NtcDevMonInternalErrorCause_Type(DisplayString):
    """Custom type ntcDevMonInternalErrorCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtcDevMonInternalErrorCause_Type.__name__ = "DisplayString"
_NtcDevMonInternalErrorCause_Object = MibScalar
ntcDevMonInternalErrorCause = _NtcDevMonInternalErrorCause_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 8),
    _NtcDevMonInternalErrorCause_Type()
)
ntcDevMonInternalErrorCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonInternalErrorCause.setStatus("current")


class _NtcDevMonGlobalCpuLoad_Type(OctetString):
    """Custom type ntcDevMonGlobalCpuLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_NtcDevMonGlobalCpuLoad_Type.__name__ = "OctetString"
_NtcDevMonGlobalCpuLoad_Object = MibScalar
ntcDevMonGlobalCpuLoad = _NtcDevMonGlobalCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 9, 9),
    _NtcDevMonGlobalCpuLoad_Type()
)
ntcDevMonGlobalCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevMonGlobalCpuLoad.setStatus("current")
_NtcDevAlarm_ObjectIdentity = ObjectIdentity
ntcDevAlarm = _NtcDevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10)
)
if mibBuilder.loadTexts:
    ntcDevAlarm.setStatus("current")
_NtcDevAlmGenDeviceAlarm_Type = NtcAlarmState
_NtcDevAlmGenDeviceAlarm_Object = MibScalar
ntcDevAlmGenDeviceAlarm = _NtcDevAlmGenDeviceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 1),
    _NtcDevAlmGenDeviceAlarm_Type()
)
ntcDevAlmGenDeviceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmGenDeviceAlarm.setStatus("current")
_NtcDevAlmGenBootConfigFailure_Type = NtcAlarmState
_NtcDevAlmGenBootConfigFailure_Object = MibScalar
ntcDevAlmGenBootConfigFailure = _NtcDevAlmGenBootConfigFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 2),
    _NtcDevAlmGenBootConfigFailure_Type()
)
ntcDevAlmGenBootConfigFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmGenBootConfigFailure.setStatus("current")
_NtcDevAlmGenInterfaceAlarm_Type = NtcAlarmState
_NtcDevAlmGenInterfaceAlarm_Object = MibScalar
ntcDevAlmGenInterfaceAlarm = _NtcDevAlmGenInterfaceAlarm_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 3),
    _NtcDevAlmGenInterfaceAlarm_Type()
)
ntcDevAlmGenInterfaceAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmGenInterfaceAlarm.setStatus("current")
_NtcDevAlmTemperature_Type = NtcAlarmState
_NtcDevAlmTemperature_Object = MibScalar
ntcDevAlmTemperature = _NtcDevAlmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 4),
    _NtcDevAlmTemperature_Type()
)
ntcDevAlmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmTemperature.setStatus("current")
_NtcDevAlmInvalidLicenseFile_Type = NtcAlarmState
_NtcDevAlmInvalidLicenseFile_Object = MibScalar
ntcDevAlmInvalidLicenseFile = _NtcDevAlmInvalidLicenseFile_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 5),
    _NtcDevAlmInvalidLicenseFile_Type()
)
ntcDevAlmInvalidLicenseFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmInvalidLicenseFile.setStatus("current")
_NtcDevAlmFrontPanelFailure_Type = NtcAlarmState
_NtcDevAlmFrontPanelFailure_Object = MibScalar
ntcDevAlmFrontPanelFailure = _NtcDevAlmFrontPanelFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 6),
    _NtcDevAlmFrontPanelFailure_Type()
)
ntcDevAlmFrontPanelFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmFrontPanelFailure.setStatus("current")
_NtcDevAlmUpgradeFailure_Type = NtcAlarmState
_NtcDevAlmUpgradeFailure_Object = MibScalar
ntcDevAlmUpgradeFailure = _NtcDevAlmUpgradeFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 7),
    _NtcDevAlmUpgradeFailure_Type()
)
ntcDevAlmUpgradeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmUpgradeFailure.setStatus("current")
_NtcDevAlmNtpNoPeerFailure_Type = NtcAlarmState
_NtcDevAlmNtpNoPeerFailure_Object = MibScalar
ntcDevAlmNtpNoPeerFailure = _NtcDevAlmNtpNoPeerFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 8),
    _NtcDevAlmNtpNoPeerFailure_Type()
)
ntcDevAlmNtpNoPeerFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmNtpNoPeerFailure.setStatus("current")
_NtcDevAlmLicenseExpireFile_Type = NtcAlarmState
_NtcDevAlmLicenseExpireFile_Object = MibScalar
ntcDevAlmLicenseExpireFile = _NtcDevAlmLicenseExpireFile_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 9),
    _NtcDevAlmLicenseExpireFile_Type()
)
ntcDevAlmLicenseExpireFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmLicenseExpireFile.setStatus("current")
_NtcDevAlmHardwareInventory_Type = NtcAlarmState
_NtcDevAlmHardwareInventory_Object = MibScalar
ntcDevAlmHardwareInventory = _NtcDevAlmHardwareInventory_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 10),
    _NtcDevAlmHardwareInventory_Type()
)
ntcDevAlmHardwareInventory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmHardwareInventory.setStatus("current")
_NtcDevAlmHardwareFailure_Type = NtcAlarmState
_NtcDevAlmHardwareFailure_Object = MibScalar
ntcDevAlmHardwareFailure = _NtcDevAlmHardwareFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 11),
    _NtcDevAlmHardwareFailure_Type()
)
ntcDevAlmHardwareFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmHardwareFailure.setStatus("current")
_NtcDevAlmInternalError_Type = NtcAlarmState
_NtcDevAlmInternalError_Object = MibScalar
ntcDevAlmInternalError = _NtcDevAlmInternalError_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 12),
    _NtcDevAlmInternalError_Type()
)
ntcDevAlmInternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmInternalError.setStatus("current")
_NtcDevAlmLicenseUpgradeFailure_Type = NtcAlarmState
_NtcDevAlmLicenseUpgradeFailure_Object = MibScalar
ntcDevAlmLicenseUpgradeFailure = _NtcDevAlmLicenseUpgradeFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 10, 13),
    _NtcDevAlmLicenseUpgradeFailure_Type()
)
ntcDevAlmLicenseUpgradeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevAlmLicenseUpgradeFailure.setStatus("current")


class _NtcDevReset_Type(Integer32):
    """Custom type ntcDevReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("hardware", 1),
          ("software", 2),
          ("configs", 3))
    )


_NtcDevReset_Type.__name__ = "Integer32"
_NtcDevReset_Object = MibScalar
ntcDevReset = _NtcDevReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 11),
    _NtcDevReset_Type()
)
ntcDevReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevReset.setStatus("current")
_NtcDevOperatorIdentification_ObjectIdentity = ObjectIdentity
ntcDevOperatorIdentification = _NtcDevOperatorIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 12)
)
if mibBuilder.loadTexts:
    ntcDevOperatorIdentification.setStatus("current")


class _NtcDevTelephonenbr_Type(DisplayString):
    """Custom type ntcDevTelephonenbr based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtcDevTelephonenbr_Type.__name__ = "DisplayString"
_NtcDevTelephonenbr_Object = MibScalar
ntcDevTelephonenbr = _NtcDevTelephonenbr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 12, 1),
    _NtcDevTelephonenbr_Type()
)
ntcDevTelephonenbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevTelephonenbr.setStatus("current")


class _NtcDevTelephoneext_Type(DisplayString):
    """Custom type ntcDevTelephoneext based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NtcDevTelephoneext_Type.__name__ = "DisplayString"
_NtcDevTelephoneext_Object = MibScalar
ntcDevTelephoneext = _NtcDevTelephoneext_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 12, 2),
    _NtcDevTelephoneext_Type()
)
ntcDevTelephoneext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevTelephoneext.setStatus("current")


class _NtcDevCarrId_Type(DisplayString):
    """Custom type ntcDevCarrId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_NtcDevCarrId_Type.__name__ = "DisplayString"
_NtcDevCarrId_Object = MibScalar
ntcDevCarrId = _NtcDevCarrId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 12, 3),
    _NtcDevCarrId_Type()
)
ntcDevCarrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevCarrId.setStatus("current")
_NtcDevLocation_ObjectIdentity = ObjectIdentity
ntcDevLocation = _NtcDevLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 13)
)
if mibBuilder.loadTexts:
    ntcDevLocation.setStatus("current")


class _NtcDevIdLongitude_Type(Float32TC):
    """Custom type ntcDevIdLongitude based on Float32TC"""
    defaultHexValue = "00000000"


_NtcDevIdLongitude_Type.__name__ = "Float32TC"
_NtcDevIdLongitude_Object = MibScalar
ntcDevIdLongitude = _NtcDevIdLongitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 13, 1),
    _NtcDevIdLongitude_Type()
)
ntcDevIdLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevIdLongitude.setStatus("current")
if mibBuilder.loadTexts:
    ntcDevIdLongitude.setUnits("deg.")


class _NtcDevIdLatitude_Type(Float32TC):
    """Custom type ntcDevIdLatitude based on Float32TC"""
    defaultHexValue = "00000000"


_NtcDevIdLatitude_Type.__name__ = "Float32TC"
_NtcDevIdLatitude_Object = MibScalar
ntcDevIdLatitude = _NtcDevIdLatitude_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 13, 2),
    _NtcDevIdLatitude_Type()
)
ntcDevIdLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevIdLatitude.setStatus("current")
if mibBuilder.loadTexts:
    ntcDevIdLatitude.setUnits("deg.")
_NtcDevConfiguration_ObjectIdentity = ObjectIdentity
ntcDevConfiguration = _NtcDevConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 14)
)
if mibBuilder.loadTexts:
    ntcDevConfiguration.setStatus("current")


class _NtcDevAutoSave_Type(NtcEnable):
    """Custom type ntcDevAutoSave based on NtcEnable"""
    defaultValue = 0


_NtcDevAutoSave_Type.__name__ = "NtcEnable"
_NtcDevAutoSave_Object = MibScalar
ntcDevAutoSave = _NtcDevAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 14, 1),
    _NtcDevAutoSave_Type()
)
ntcDevAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevAutoSave.setStatus("current")


class _NtcDevActCfgState_Type(Integer32):
    """Custom type ntcDevActCfgState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("saved", 0),
          ("updatedNotSaved", 1))
    )


_NtcDevActCfgState_Type.__name__ = "Integer32"
_NtcDevActCfgState_Object = MibScalar
ntcDevActCfgState = _NtcDevActCfgState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 14, 2),
    _NtcDevActCfgState_Type()
)
ntcDevActCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDevActCfgState.setStatus("current")
_NtcDevRest_ObjectIdentity = ObjectIdentity
ntcDevRest = _NtcDevRest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 15)
)
if mibBuilder.loadTexts:
    ntcDevRest.setStatus("current")


class _NtcDevRestEnable_Type(NtcEnable):
    """Custom type ntcDevRestEnable based on NtcEnable"""
    defaultValue = 1


_NtcDevRestEnable_Type.__name__ = "NtcEnable"
_NtcDevRestEnable_Object = MibScalar
ntcDevRestEnable = _NtcDevRestEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 1, 15, 1),
    _NtcDevRestEnable_Type()
)
ntcDevRestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDevRestEnable.setStatus("current")
_NtcDevConformance_ObjectIdentity = ObjectIdentity
ntcDevConformance = _NtcDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 2)
)
if mibBuilder.loadTexts:
    ntcDevConformance.setStatus("current")
_NtcDevConfCompliance_ObjectIdentity = ObjectIdentity
ntcDevConfCompliance = _NtcDevConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 2, 1)
)
if mibBuilder.loadTexts:
    ntcDevConfCompliance.setStatus("current")
_NtcDevConfGroup_ObjectIdentity = ObjectIdentity
ntcDevConfGroup = _NtcDevConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 2, 2)
)
if mibBuilder.loadTexts:
    ntcDevConfGroup.setStatus("current")

# Managed Objects groups

ntcDevConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 2, 2, 1)
)
ntcDevConfGrpV1Standard.setObjects(
      *(("NEWTEC-DEVICE-MIB", "ntcDevIdLabel"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdSerialNumber"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdUniqueId"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdProduct"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdDeviceDescription"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdTypeId"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdHardwareRevision"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdSoftwareId"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdSoftwareVersion"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdDeviceOptionsDescription"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdLicenseType"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdLicenseTimeRemain"),
        ("NEWTEC-DEVICE-MIB", "ntcDevFpEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevFpiAccessLevel"),
        ("NEWTEC-DEVICE-MIB", "ntcDevSnmpNotifDestIpAddress"),
        ("NEWTEC-DEVICE-MIB", "ntcDevSnmpNotifDestType"),
        ("NEWTEC-DEVICE-MIB", "ntcDevSnmpNotifDestCommunity"),
        ("NEWTEC-DEVICE-MIB", "ntcDevCliRemoteEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevCliInactivityTimeout"),
        ("NEWTEC-DEVICE-MIB", "ntcDevGuiEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevFtpEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevFtpAnonymousEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevLogLocEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevLogRemEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevLogRemIpAddress"),
        ("NEWTEC-DEVICE-MIB", "ntcDevLogRemUdpPort"),
        ("NEWTEC-DEVICE-MIB", "ntcDevLogFilterLevel"),
        ("NEWTEC-DEVICE-MIB", "ntcDevDtDate"),
        ("NEWTEC-DEVICE-MIB", "ntcDevDtTime"),
        ("NEWTEC-DEVICE-MIB", "ntcDevDtNtpEnable"),
        ("NEWTEC-DEVICE-MIB", "ntcDevDtNtpPeerIpAddress"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonTemperature"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonPowerSupply"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonCpuLoad"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonMemoryUse"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonUptime"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonSensorsValue"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonHwFailureCause"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonInternalErrorCause"),
        ("NEWTEC-DEVICE-MIB", "ntcDevMonGlobalCpuLoad"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmGenDeviceAlarm"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmGenBootConfigFailure"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmGenInterfaceAlarm"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmTemperature"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmInvalidLicenseFile"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmFrontPanelFailure"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmUpgradeFailure"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmNtpNoPeerFailure"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmLicenseExpireFile"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmHardwareInventory"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmHardwareFailure"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmInternalError"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAlmLicenseUpgradeFailure"),
        ("NEWTEC-DEVICE-MIB", "ntcDevReset"),
        ("NEWTEC-DEVICE-MIB", "ntcDevTelephonenbr"),
        ("NEWTEC-DEVICE-MIB", "ntcDevTelephoneext"),
        ("NEWTEC-DEVICE-MIB", "ntcDevCarrId"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdLongitude"),
        ("NEWTEC-DEVICE-MIB", "ntcDevIdLatitude"),
        ("NEWTEC-DEVICE-MIB", "ntcDevAutoSave"),
        ("NEWTEC-DEVICE-MIB", "ntcDevActCfgState"),
        ("NEWTEC-DEVICE-MIB", "ntcDevRestEnable"))
)
if mibBuilder.loadTexts:
    ntcDevConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcDevConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 100, 2, 1, 1)
)
ntcDevConfCompV1Standard.setObjects(
    ("NEWTEC-DEVICE-MIB", "ntcDevConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcDevConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-DEVICE-MIB",
    **{"ntcDevice": ntcDevice,
       "ntcDevObjects": ntcDevObjects,
       "ntcDevIdentification": ntcDevIdentification,
       "ntcDevIdLabel": ntcDevIdLabel,
       "ntcDevIdSerialNumber": ntcDevIdSerialNumber,
       "ntcDevIdUniqueId": ntcDevIdUniqueId,
       "ntcDevIdProduct": ntcDevIdProduct,
       "ntcDevIdDeviceDescription": ntcDevIdDeviceDescription,
       "ntcDevIdTypeId": ntcDevIdTypeId,
       "ntcDevIdHardwareRevision": ntcDevIdHardwareRevision,
       "ntcDevIdSoftwareId": ntcDevIdSoftwareId,
       "ntcDevIdSoftwareVersion": ntcDevIdSoftwareVersion,
       "ntcDevIdDeviceOptionsTable": ntcDevIdDeviceOptionsTable,
       "ntcDevIdDeviceOptionsEntry": ntcDevIdDeviceOptionsEntry,
       "ntcDevIdDeviceOptionsSalesCode": ntcDevIdDeviceOptionsSalesCode,
       "ntcDevIdDeviceOptionsDescription": ntcDevIdDeviceOptionsDescription,
       "ntcDevIdLicenseType": ntcDevIdLicenseType,
       "ntcDevIdLicenseTimeRemain": ntcDevIdLicenseTimeRemain,
       "ntcDevFrontPanel": ntcDevFrontPanel,
       "ntcDevFpEnable": ntcDevFpEnable,
       "ntcDevFpiAccessLevel": ntcDevFpiAccessLevel,
       "ntcDevSnmp": ntcDevSnmp,
       "ntcDevSnmpNotification": ntcDevSnmpNotification,
       "ntcDevSnmpNotifDestTable": ntcDevSnmpNotifDestTable,
       "ntcDevSnmpNotifDestEntry": ntcDevSnmpNotifDestEntry,
       "ntcDevSnmpNotifDestDestination": ntcDevSnmpNotifDestDestination,
       "ntcDevSnmpNotifDestIpAddress": ntcDevSnmpNotifDestIpAddress,
       "ntcDevSnmpNotifDestType": ntcDevSnmpNotifDestType,
       "ntcDevSnmpNotifDestCommunity": ntcDevSnmpNotifDestCommunity,
       "ntcDevCli": ntcDevCli,
       "ntcDevCliRemoteEnable": ntcDevCliRemoteEnable,
       "ntcDevCliInactivityTimeout": ntcDevCliInactivityTimeout,
       "ntcDevGui": ntcDevGui,
       "ntcDevGuiEnable": ntcDevGuiEnable,
       "ntcDevFtp": ntcDevFtp,
       "ntcDevFtpEnable": ntcDevFtpEnable,
       "ntcDevFtpAnonymousEnable": ntcDevFtpAnonymousEnable,
       "ntcDevLog": ntcDevLog,
       "ntcDevLogLocal": ntcDevLogLocal,
       "ntcDevLogLocEnable": ntcDevLogLocEnable,
       "ntcDevLogRemote": ntcDevLogRemote,
       "ntcDevLogRemEnable": ntcDevLogRemEnable,
       "ntcDevLogRemIpAddress": ntcDevLogRemIpAddress,
       "ntcDevLogRemUdpPort": ntcDevLogRemUdpPort,
       "ntcDevLogFilterTable": ntcDevLogFilterTable,
       "ntcDevLogFilterEntry": ntcDevLogFilterEntry,
       "ntcDevLogFilterFacility": ntcDevLogFilterFacility,
       "ntcDevLogFilterLevel": ntcDevLogFilterLevel,
       "ntcDevDateTime": ntcDevDateTime,
       "ntcDevDtDate": ntcDevDtDate,
       "ntcDevDtTime": ntcDevDtTime,
       "ntcDevDtNtp": ntcDevDtNtp,
       "ntcDevDtNtpEnable": ntcDevDtNtpEnable,
       "ntcDevDtNtpPeerTable": ntcDevDtNtpPeerTable,
       "ntcDevDtNtpPeerEntry": ntcDevDtNtpPeerEntry,
       "ntcDevDtNtpPeerPeer": ntcDevDtNtpPeerPeer,
       "ntcDevDtNtpPeerIpAddress": ntcDevDtNtpPeerIpAddress,
       "ntcDevMonitor": ntcDevMonitor,
       "ntcDevMonTemperature": ntcDevMonTemperature,
       "ntcDevMonPowerSupply": ntcDevMonPowerSupply,
       "ntcDevMonCpuLoad": ntcDevMonCpuLoad,
       "ntcDevMonMemoryUse": ntcDevMonMemoryUse,
       "ntcDevMonUptime": ntcDevMonUptime,
       "ntcDevMonSensorsTable": ntcDevMonSensorsTable,
       "ntcDevMonSensorsEntry": ntcDevMonSensorsEntry,
       "ntcDevMonSensorsSensor": ntcDevMonSensorsSensor,
       "ntcDevMonSensorsValue": ntcDevMonSensorsValue,
       "ntcDevMonHwFailureCause": ntcDevMonHwFailureCause,
       "ntcDevMonInternalErrorCause": ntcDevMonInternalErrorCause,
       "ntcDevMonGlobalCpuLoad": ntcDevMonGlobalCpuLoad,
       "ntcDevAlarm": ntcDevAlarm,
       "ntcDevAlmGenDeviceAlarm": ntcDevAlmGenDeviceAlarm,
       "ntcDevAlmGenBootConfigFailure": ntcDevAlmGenBootConfigFailure,
       "ntcDevAlmGenInterfaceAlarm": ntcDevAlmGenInterfaceAlarm,
       "ntcDevAlmTemperature": ntcDevAlmTemperature,
       "ntcDevAlmInvalidLicenseFile": ntcDevAlmInvalidLicenseFile,
       "ntcDevAlmFrontPanelFailure": ntcDevAlmFrontPanelFailure,
       "ntcDevAlmUpgradeFailure": ntcDevAlmUpgradeFailure,
       "ntcDevAlmNtpNoPeerFailure": ntcDevAlmNtpNoPeerFailure,
       "ntcDevAlmLicenseExpireFile": ntcDevAlmLicenseExpireFile,
       "ntcDevAlmHardwareInventory": ntcDevAlmHardwareInventory,
       "ntcDevAlmHardwareFailure": ntcDevAlmHardwareFailure,
       "ntcDevAlmInternalError": ntcDevAlmInternalError,
       "ntcDevAlmLicenseUpgradeFailure": ntcDevAlmLicenseUpgradeFailure,
       "ntcDevReset": ntcDevReset,
       "ntcDevOperatorIdentification": ntcDevOperatorIdentification,
       "ntcDevTelephonenbr": ntcDevTelephonenbr,
       "ntcDevTelephoneext": ntcDevTelephoneext,
       "ntcDevCarrId": ntcDevCarrId,
       "ntcDevLocation": ntcDevLocation,
       "ntcDevIdLongitude": ntcDevIdLongitude,
       "ntcDevIdLatitude": ntcDevIdLatitude,
       "ntcDevConfiguration": ntcDevConfiguration,
       "ntcDevAutoSave": ntcDevAutoSave,
       "ntcDevActCfgState": ntcDevActCfgState,
       "ntcDevRest": ntcDevRest,
       "ntcDevRestEnable": ntcDevRestEnable,
       "ntcDevConformance": ntcDevConformance,
       "ntcDevConfCompliance": ntcDevConfCompliance,
       "ntcDevConfCompV1Standard": ntcDevConfCompV1Standard,
       "ntcDevConfGroup": ntcDevConfGroup,
       "ntcDevConfGrpV1Standard": ntcDevConfGrpV1Standard}
)
