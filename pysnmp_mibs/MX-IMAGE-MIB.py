# SNMP MIB module (MX-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-IMAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:27 2025
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

(ipAddressConfig,
 ipAddressStatus,
 mediatrixConfig,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "ipAddressConfig",
    "ipAddressStatus",
    "mediatrixConfig",
    "mediatrixMgmt")

(sysAdminLastDownloadSoftware,) = mibBuilder.importSymbols(
    "MX-SYSTEM-ADMIN-MIB",
    "sysAdminLastDownloadSoftware")

(MxEnableState,
 MxIpConfigSource,
 MxIpDhcpSiteSpecificCode,
 MxIpHostName,
 MxIpPort,
 MxIpSelectConfigSource) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState",
    "MxIpConfigSource",
    "MxIpDhcpSiteSpecificCode",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSelectConfigSource")

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

imageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6)
)
if mibBuilder.loadTexts:
    imageMIB.setRevisions(
        ("2010-12-15 00:00",
         "2006-03-06 00:00",
         "2005-04-25 00:00",
         "2004-03-27 00:00",
         "2004-02-10 00:00",
         "2001-09-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpAddressStatusImage_ObjectIdentity = ObjectIdentity
ipAddressStatusImage = _IpAddressStatusImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 8)
)


class _ImageConfigSource_Type(MxIpConfigSource):
    """Custom type imageConfigSource based on MxIpConfigSource"""
    defaultValue = 1


_ImageConfigSource_Type.__name__ = "MxIpConfigSource"
_ImageConfigSource_Object = MibScalar
imageConfigSource = _ImageConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 8, 1),
    _ImageConfigSource_Type()
)
imageConfigSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageConfigSource.setStatus("current")


class _ImagePrimaryHost_Type(MxIpHostName):
    """Custom type imagePrimaryHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_ImagePrimaryHost_Type.__name__ = "MxIpHostName"
_ImagePrimaryHost_Object = MibScalar
imagePrimaryHost = _ImagePrimaryHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 8, 2),
    _ImagePrimaryHost_Type()
)
imagePrimaryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagePrimaryHost.setStatus("current")


class _ImagePrimaryPort_Type(MxIpPort):
    """Custom type imagePrimaryPort based on MxIpPort"""
    defaultValue = 69


_ImagePrimaryPort_Type.__name__ = "MxIpPort"
_ImagePrimaryPort_Object = MibScalar
imagePrimaryPort = _ImagePrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 8, 3),
    _ImagePrimaryPort_Type()
)
imagePrimaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imagePrimaryPort.setStatus("current")


class _ImageSecondaryHost_Type(MxIpHostName):
    """Custom type imageSecondaryHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_ImageSecondaryHost_Type.__name__ = "MxIpHostName"
_ImageSecondaryHost_Object = MibScalar
imageSecondaryHost = _ImageSecondaryHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 8, 4),
    _ImageSecondaryHost_Type()
)
imageSecondaryHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageSecondaryHost.setStatus("current")


class _ImageSecondaryPort_Type(MxIpPort):
    """Custom type imageSecondaryPort based on MxIpPort"""
    defaultValue = 69


_ImageSecondaryPort_Type.__name__ = "MxIpPort"
_ImageSecondaryPort_Object = MibScalar
imageSecondaryPort = _ImageSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 1, 8, 5),
    _ImageSecondaryPort_Type()
)
imageSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageSecondaryPort.setStatus("current")
_ImageStatus_ObjectIdentity = ObjectIdentity
imageStatus = _ImageStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 75)
)


class _ImageLocationStatus_Type(OctetString):
    """Custom type imageLocationStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageLocationStatus_Type.__name__ = "OctetString"
_ImageLocationStatus_Object = MibScalar
imageLocationStatus = _ImageLocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 75, 10),
    _ImageLocationStatus_Type()
)
imageLocationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imageLocationStatus.setStatus("current")
_IpAddressConfigImage_ObjectIdentity = ObjectIdentity
ipAddressConfigImage = _IpAddressConfigImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8)
)


class _ImageSelectConfigSource_Type(MxIpSelectConfigSource):
    """Custom type imageSelectConfigSource based on MxIpSelectConfigSource"""
    defaultValue = 1


_ImageSelectConfigSource_Type.__name__ = "MxIpSelectConfigSource"
_ImageSelectConfigSource_Object = MibScalar
imageSelectConfigSource = _ImageSelectConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 1),
    _ImageSelectConfigSource_Type()
)
imageSelectConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageSelectConfigSource.setStatus("current")
_IpAddressConfigImageStatic_ObjectIdentity = ObjectIdentity
ipAddressConfigImageStatic = _IpAddressConfigImageStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 5)
)


class _ImageStaticPrimaryHost_Type(MxIpHostName):
    """Custom type imageStaticPrimaryHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_ImageStaticPrimaryHost_Type.__name__ = "MxIpHostName"
_ImageStaticPrimaryHost_Object = MibScalar
imageStaticPrimaryHost = _ImageStaticPrimaryHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 5, 1),
    _ImageStaticPrimaryHost_Type()
)
imageStaticPrimaryHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageStaticPrimaryHost.setStatus("current")


class _ImageStaticPrimaryPort_Type(MxIpPort):
    """Custom type imageStaticPrimaryPort based on MxIpPort"""
    defaultValue = 69


_ImageStaticPrimaryPort_Type.__name__ = "MxIpPort"
_ImageStaticPrimaryPort_Object = MibScalar
imageStaticPrimaryPort = _ImageStaticPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 5, 2),
    _ImageStaticPrimaryPort_Type()
)
imageStaticPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageStaticPrimaryPort.setStatus("current")


class _ImageStaticSecondaryHost_Type(MxIpHostName):
    """Custom type imageStaticSecondaryHost based on MxIpHostName"""
    defaultValue = OctetString("192.168.0.10")


_ImageStaticSecondaryHost_Type.__name__ = "MxIpHostName"
_ImageStaticSecondaryHost_Object = MibScalar
imageStaticSecondaryHost = _ImageStaticSecondaryHost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 5, 3),
    _ImageStaticSecondaryHost_Type()
)
imageStaticSecondaryHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageStaticSecondaryHost.setStatus("current")


class _ImageStaticSecondaryPort_Type(MxIpPort):
    """Custom type imageStaticSecondaryPort based on MxIpPort"""
    defaultValue = 69


_ImageStaticSecondaryPort_Type.__name__ = "MxIpPort"
_ImageStaticSecondaryPort_Object = MibScalar
imageStaticSecondaryPort = _ImageStaticSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 5, 4),
    _ImageStaticSecondaryPort_Type()
)
imageStaticSecondaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageStaticSecondaryPort.setStatus("current")
_IpAddressConfigImageDhcp_ObjectIdentity = ObjectIdentity
ipAddressConfigImageDhcp = _IpAddressConfigImageDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 6)
)


class _ImageDhcpPrimarySiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type imageDhcpPrimarySiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_ImageDhcpPrimarySiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_ImageDhcpPrimarySiteSpecificCode_Object = MibScalar
imageDhcpPrimarySiteSpecificCode = _ImageDhcpPrimarySiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 6, 1),
    _ImageDhcpPrimarySiteSpecificCode_Type()
)
imageDhcpPrimarySiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageDhcpPrimarySiteSpecificCode.setStatus("current")


class _ImageDhcpSecondarySiteSpecificCode_Type(MxIpDhcpSiteSpecificCode):
    """Custom type imageDhcpSecondarySiteSpecificCode based on MxIpDhcpSiteSpecificCode"""
    defaultValue = 0


_ImageDhcpSecondarySiteSpecificCode_Type.__name__ = "MxIpDhcpSiteSpecificCode"
_ImageDhcpSecondarySiteSpecificCode_Object = MibScalar
imageDhcpSecondarySiteSpecificCode = _ImageDhcpSecondarySiteSpecificCode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 1, 8, 6, 2),
    _ImageDhcpSecondarySiteSpecificCode_Type()
)
imageDhcpSecondarySiteSpecificCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageDhcpSecondarySiteSpecificCode.setStatus("current")
_ImageMIBObjects_ObjectIdentity = ObjectIdentity
imageMIBObjects = _ImageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1)
)


class _ImageLocation_Type(OctetString):
    """Custom type imageLocation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageLocation_Type.__name__ = "OctetString"
_ImageLocation_Object = MibScalar
imageLocation = _ImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 1),
    _ImageLocation_Type()
)
imageLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageLocation.setStatus("current")


class _ImageSelectionFileLocation_Type(OctetString):
    """Custom type imageSelectionFileLocation based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageSelectionFileLocation_Type.__name__ = "OctetString"
_ImageSelectionFileLocation_Object = MibScalar
imageSelectionFileLocation = _ImageSelectionFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 50),
    _ImageSelectionFileLocation_Type()
)
imageSelectionFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageSelectionFileLocation.setStatus("current")


class _ImageLocationProvisionSource_Type(Integer32):
    """Custom type imageLocationProvisionSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("remoteFile", 1))
    )


_ImageLocationProvisionSource_Type.__name__ = "Integer32"
_ImageLocationProvisionSource_Object = MibScalar
imageLocationProvisionSource = _ImageLocationProvisionSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 100),
    _ImageLocationProvisionSource_Type()
)
imageLocationProvisionSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageLocationProvisionSource.setStatus("current")
_ImageTransfer_ObjectIdentity = ObjectIdentity
imageTransfer = _ImageTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 150)
)


class _ImageTransferProtocol_Type(Integer32):
    """Custom type imageTransferProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 0),
          ("http", 1),
          ("https", 2))
    )


_ImageTransferProtocol_Type.__name__ = "Integer32"
_ImageTransferProtocol_Object = MibScalar
imageTransferProtocol = _ImageTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 150, 50),
    _ImageTransferProtocol_Type()
)
imageTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferProtocol.setStatus("current")


class _ImageTransferUsername_Type(OctetString):
    """Custom type imageTransferUsername based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageTransferUsername_Type.__name__ = "OctetString"
_ImageTransferUsername_Object = MibScalar
imageTransferUsername = _ImageTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 150, 100),
    _ImageTransferUsername_Type()
)
imageTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferUsername.setStatus("current")


class _ImageTransferPassword_Type(OctetString):
    """Custom type imageTransferPassword based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageTransferPassword_Type.__name__ = "OctetString"
_ImageTransferPassword_Object = MibScalar
imageTransferPassword = _ImageTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 150, 150),
    _ImageTransferPassword_Type()
)
imageTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageTransferPassword.setStatus("current")
_ImageAutomaticUpdate_ObjectIdentity = ObjectIdentity
imageAutomaticUpdate = _ImageAutomaticUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200)
)


class _ImageAutoUpdateOnRestartEnable_Type(MxEnableState):
    """Custom type imageAutoUpdateOnRestartEnable based on MxEnableState"""
    defaultValue = 0


_ImageAutoUpdateOnRestartEnable_Type.__name__ = "MxEnableState"
_ImageAutoUpdateOnRestartEnable_Object = MibScalar
imageAutoUpdateOnRestartEnable = _ImageAutoUpdateOnRestartEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200, 50),
    _ImageAutoUpdateOnRestartEnable_Type()
)
imageAutoUpdateOnRestartEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageAutoUpdateOnRestartEnable.setStatus("current")


class _ImageAutoUpdatePeriodicEnable_Type(MxEnableState):
    """Custom type imageAutoUpdatePeriodicEnable based on MxEnableState"""
    defaultValue = 0


_ImageAutoUpdatePeriodicEnable_Type.__name__ = "MxEnableState"
_ImageAutoUpdatePeriodicEnable_Object = MibScalar
imageAutoUpdatePeriodicEnable = _ImageAutoUpdatePeriodicEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200, 100),
    _ImageAutoUpdatePeriodicEnable_Type()
)
imageAutoUpdatePeriodicEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageAutoUpdatePeriodicEnable.setStatus("current")


class _ImageAutoUpdateTimeUnit_Type(Integer32):
    """Custom type imageAutoUpdateTimeUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              20)
        )
    )
    namedValues = NamedValues(
        *(("hours", 0),
          ("days", 1),
          ("minutes", 20))
    )


_ImageAutoUpdateTimeUnit_Type.__name__ = "Integer32"
_ImageAutoUpdateTimeUnit_Object = MibScalar
imageAutoUpdateTimeUnit = _ImageAutoUpdateTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200, 150),
    _ImageAutoUpdateTimeUnit_Type()
)
imageAutoUpdateTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageAutoUpdateTimeUnit.setStatus("current")


class _ImageAutoUpdatePeriod_Type(Unsigned32):
    """Custom type imageAutoUpdatePeriod based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_ImageAutoUpdatePeriod_Type.__name__ = "Unsigned32"
_ImageAutoUpdatePeriod_Object = MibScalar
imageAutoUpdatePeriod = _ImageAutoUpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200, 200),
    _ImageAutoUpdatePeriod_Type()
)
imageAutoUpdatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageAutoUpdatePeriod.setStatus("current")


class _ImageAutoUpdateTimeOfDay_Type(Integer32):
    """Custom type imageAutoUpdateTimeOfDay based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 23),
    )


_ImageAutoUpdateTimeOfDay_Type.__name__ = "Integer32"
_ImageAutoUpdateTimeOfDay_Object = MibScalar
imageAutoUpdateTimeOfDay = _ImageAutoUpdateTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200, 250),
    _ImageAutoUpdateTimeOfDay_Type()
)
imageAutoUpdateTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageAutoUpdateTimeOfDay.setStatus("deprecated")


class _ImageAutoUpdateTimeRange_Type(OctetString):
    """Custom type imageAutoUpdateTimeRange based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ImageAutoUpdateTimeRange_Type.__name__ = "OctetString"
_ImageAutoUpdateTimeRange_Object = MibScalar
imageAutoUpdateTimeRange = _ImageAutoUpdateTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 1, 200, 300),
    _ImageAutoUpdateTimeRange_Type()
)
imageAutoUpdateTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageAutoUpdateTimeRange.setStatus("current")
_ImageConformance_ObjectIdentity = ObjectIdentity
imageConformance = _ImageConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2)
)
_ImageCompliances_ObjectIdentity = ObjectIdentity
imageCompliances = _ImageCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 1)
)
_ImageGroups_ObjectIdentity = ObjectIdentity
imageGroups = _ImageGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2)
)
_ImageEvents_ObjectIdentity = ObjectIdentity
imageEvents = _ImageEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3)
)
_ImageNotificationsControl_ObjectIdentity = ObjectIdentity
imageNotificationsControl = _ImageNotificationsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 1)
)


class _ImageCompletionControl_Type(Integer32):
    """Custom type imageCompletionControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_ImageCompletionControl_Type.__name__ = "Integer32"
_ImageCompletionControl_Object = MibScalar
imageCompletionControl = _ImageCompletionControl_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 1, 1),
    _ImageCompletionControl_Type()
)
imageCompletionControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imageCompletionControl.setStatus("current")
_ImageNotifications_ObjectIdentity = ObjectIdentity
imageNotifications = _ImageNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 2)
)
_ImageNotificationsParams_ObjectIdentity = ObjectIdentity
imageNotificationsParams = _ImageNotificationsParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 4)
)


class _ImageLocationUsed_Type(OctetString):
    """Custom type imageLocationUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ImageLocationUsed_Type.__name__ = "OctetString"
_ImageLocationUsed_Object = MibScalar
imageLocationUsed = _ImageLocationUsed_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 4, 1),
    _ImageLocationUsed_Type()
)
imageLocationUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imageLocationUsed.setStatus("current")
_ImageServerAddress_Type = MxIpHostName
_ImageServerAddress_Object = MibScalar
imageServerAddress = _ImageServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 4, 2),
    _ImageServerAddress_Type()
)
imageServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    imageServerAddress.setStatus("current")

# Managed Objects groups

imageBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 1)
)
imageBasicGroupVer1.setObjects(
    ("MX-IMAGE-MIB", "imageLocation")
)
if mibBuilder.loadTexts:
    imageBasicGroupVer1.setStatus("current")

imageTFTPGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 2)
)
imageTFTPGroupVer1.setObjects(
      *(("MX-IMAGE-MIB", "imageConfigSource"),
        ("MX-IMAGE-MIB", "imagePrimaryHost"),
        ("MX-IMAGE-MIB", "imagePrimaryPort"),
        ("MX-IMAGE-MIB", "imageSecondaryHost"),
        ("MX-IMAGE-MIB", "imageSecondaryPort"),
        ("MX-IMAGE-MIB", "imageSelectConfigSource"),
        ("MX-IMAGE-MIB", "imageStaticPrimaryHost"),
        ("MX-IMAGE-MIB", "imageStaticPrimaryPort"),
        ("MX-IMAGE-MIB", "imageStaticSecondaryHost"),
        ("MX-IMAGE-MIB", "imageStaticSecondaryPort"),
        ("MX-IMAGE-MIB", "imageDhcpPrimarySiteSpecificCode"),
        ("MX-IMAGE-MIB", "imageDhcpSecondarySiteSpecificCode"))
)
if mibBuilder.loadTexts:
    imageTFTPGroupVer1.setStatus("current")

imageBasicNotificationControlGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 3)
)
imageBasicNotificationControlGroupVer1.setObjects(
    ("MX-IMAGE-MIB", "imageCompletionControl")
)
if mibBuilder.loadTexts:
    imageBasicNotificationControlGroupVer1.setStatus("current")

imageBasicNotificationParamsGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 4)
)
imageBasicNotificationParamsGroupVer1.setObjects(
      *(("MX-IMAGE-MIB", "imageLocationUsed"),
        ("MX-IMAGE-MIB", "imageServerAddress"))
)
if mibBuilder.loadTexts:
    imageBasicNotificationParamsGroupVer1.setStatus("current")

imageTransferGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 50)
)
imageTransferGroupVer1.setObjects(
      *(("MX-IMAGE-MIB", "imageTransferProtocol"),
        ("MX-IMAGE-MIB", "imageTransferUsername"),
        ("MX-IMAGE-MIB", "imageTransferPassword"))
)
if mibBuilder.loadTexts:
    imageTransferGroupVer1.setStatus("current")

imageAutomaticUpdateGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 100)
)
imageAutomaticUpdateGroupVer1.setObjects(
      *(("MX-IMAGE-MIB", "imageAutoUpdateOnRestartEnable"),
        ("MX-IMAGE-MIB", "imageAutoUpdatePeriodicEnable"),
        ("MX-IMAGE-MIB", "imageAutoUpdateTimeUnit"),
        ("MX-IMAGE-MIB", "imageAutoUpdatePeriod"),
        ("MX-IMAGE-MIB", "imageAutoUpdateTimeOfDay"),
        ("MX-IMAGE-MIB", "imageAutoUpdateTimeRange"))
)
if mibBuilder.loadTexts:
    imageAutomaticUpdateGroupVer1.setStatus("current")


# Notification objects

imageCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 3, 2, 1)
)
imageCompletion.setObjects(
      *(("MX-IMAGE-MIB", "imageLocationUsed"),
        ("MX-IMAGE-MIB", "imageServerAddress"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastDownloadSoftware"))
)
if mibBuilder.loadTexts:
    imageCompletion.setStatus(
        "current"
    )


# Notifications groups

imageBasicNotificationGroupVer1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 2, 5)
)
imageBasicNotificationGroupVer1.setObjects(
    ("MX-IMAGE-MIB", "imageCompletion")
)
if mibBuilder.loadTexts:
    imageBasicNotificationGroupVer1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

imageBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 6, 2, 1, 1)
)
imageBasicComplVer1.setObjects(
      *(("MX-IMAGE-MIB", "imageBasicGroupVer1"),
        ("MX-IMAGE-MIB", "imageBasicNotificationControlGroupVer1"),
        ("MX-IMAGE-MIB", "imageBasicNotificationParamsGroupVer1"),
        ("MX-IMAGE-MIB", "imageBasicNotificationGroupVer1"),
        ("MX-IMAGE-MIB", "imageTransferGroupVer1"),
        ("MX-IMAGE-MIB", "imageAutomaticUpdateGroupVer1"))
)
if mibBuilder.loadTexts:
    imageBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-IMAGE-MIB",
    **{"ipAddressStatusImage": ipAddressStatusImage,
       "imageConfigSource": imageConfigSource,
       "imagePrimaryHost": imagePrimaryHost,
       "imagePrimaryPort": imagePrimaryPort,
       "imageSecondaryHost": imageSecondaryHost,
       "imageSecondaryPort": imageSecondaryPort,
       "imageStatus": imageStatus,
       "imageLocationStatus": imageLocationStatus,
       "ipAddressConfigImage": ipAddressConfigImage,
       "imageSelectConfigSource": imageSelectConfigSource,
       "ipAddressConfigImageStatic": ipAddressConfigImageStatic,
       "imageStaticPrimaryHost": imageStaticPrimaryHost,
       "imageStaticPrimaryPort": imageStaticPrimaryPort,
       "imageStaticSecondaryHost": imageStaticSecondaryHost,
       "imageStaticSecondaryPort": imageStaticSecondaryPort,
       "ipAddressConfigImageDhcp": ipAddressConfigImageDhcp,
       "imageDhcpPrimarySiteSpecificCode": imageDhcpPrimarySiteSpecificCode,
       "imageDhcpSecondarySiteSpecificCode": imageDhcpSecondarySiteSpecificCode,
       "imageMIB": imageMIB,
       "imageMIBObjects": imageMIBObjects,
       "imageLocation": imageLocation,
       "imageSelectionFileLocation": imageSelectionFileLocation,
       "imageLocationProvisionSource": imageLocationProvisionSource,
       "imageTransfer": imageTransfer,
       "imageTransferProtocol": imageTransferProtocol,
       "imageTransferUsername": imageTransferUsername,
       "imageTransferPassword": imageTransferPassword,
       "imageAutomaticUpdate": imageAutomaticUpdate,
       "imageAutoUpdateOnRestartEnable": imageAutoUpdateOnRestartEnable,
       "imageAutoUpdatePeriodicEnable": imageAutoUpdatePeriodicEnable,
       "imageAutoUpdateTimeUnit": imageAutoUpdateTimeUnit,
       "imageAutoUpdatePeriod": imageAutoUpdatePeriod,
       "imageAutoUpdateTimeOfDay": imageAutoUpdateTimeOfDay,
       "imageAutoUpdateTimeRange": imageAutoUpdateTimeRange,
       "imageConformance": imageConformance,
       "imageCompliances": imageCompliances,
       "imageBasicComplVer1": imageBasicComplVer1,
       "imageGroups": imageGroups,
       "imageBasicGroupVer1": imageBasicGroupVer1,
       "imageTFTPGroupVer1": imageTFTPGroupVer1,
       "imageBasicNotificationControlGroupVer1": imageBasicNotificationControlGroupVer1,
       "imageBasicNotificationParamsGroupVer1": imageBasicNotificationParamsGroupVer1,
       "imageBasicNotificationGroupVer1": imageBasicNotificationGroupVer1,
       "imageTransferGroupVer1": imageTransferGroupVer1,
       "imageAutomaticUpdateGroupVer1": imageAutomaticUpdateGroupVer1,
       "imageEvents": imageEvents,
       "imageNotificationsControl": imageNotificationsControl,
       "imageCompletionControl": imageCompletionControl,
       "imageNotifications": imageNotifications,
       "imageCompletion": imageCompletion,
       "imageNotificationsParams": imageNotificationsParams,
       "imageLocationUsed": imageLocationUsed,
       "imageServerAddress": imageServerAddress}
)
