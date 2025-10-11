# SNMP MIB module (DSR-TRAP-OBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/vertiv/DSR-TRAP-OBJECTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:44 2025
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



class UTF8String(OctetString):
    """Custom type UTF8String based on OctetString"""




class ImageFileUpgradeResultsEnum(Integer32):
    """Custom type ImageFileUpgradeResultsEnum based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("imageUpgradeTftpNoSocket", 1),
          ("imageUpgradeTftpConnectFailure", 2),
          ("imageUpgradeTftpRequestDenied", 3),
          ("imageUpgradeTftpBadPacket", 4),
          ("imageUpgradeTftpOOS", 5),
          ("imageUpgradeTftpTooBig", 6),
          ("imageUpgradeTftpTimeout", 7),
          ("imageUpgradeAlreadyInProgress", 8),
          ("imageUpgradeCannotStart", 9),
          ("imageUpgradeMemoryError", 10),
          ("imageUpgradeTftpProtocolError", 11),
          ("imageUpgradeBadType", 12),
          ("imageUpgradeInvalidAppDowngrade", 13),
          ("imageUpgradeChecksumError", 14),
          ("imageUpgradeFlashError", 15),
          ("imageUpgradeInternalError", 16),
          ("imageUpgradeFileNotFound", 17),
          ("imageUpgradeBadHeader", 18),
          ("imageUpgradeIncompatibleHeader", 19),
          ("imageUpgradeTftpXferFail", 20),
          ("imageUpgradeTftpSvrNoResponse", 21),
          ("imageUpgradeNetworkUnreachable", 22),
          ("imageUpgradeSuccess", 9999))
    )





class IqAdaptorUpgradeResultsEnum(Integer32):
    """Custom type IqAdaptorUpgradeResultsEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("iqaUpgradeNoFirmwareImage", 1),
          ("iqaUpgradeLostContact", 2),
          ("iqaUpgradeFailedRestart", 3),
          ("iqaUpgradeSuccess", 9999))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avocent_ObjectIdentity = ObjectIdentity
avocent = _Avocent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418)
)
_Dsr_ObjectIdentity = ObjectIdentity
dsr = _Dsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 7)
)
_DsrProducts_ObjectIdentity = ObjectIdentity
dsrProducts = _DsrProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 7, 1)
)
_DsrManagement_ObjectIdentity = ObjectIdentity
dsrManagement = _DsrManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2)
)
_DsrTrapObject_ObjectIdentity = ObjectIdentity
dsrTrapObject = _DsrTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6)
)


class _AvctDsrTrapObjectUserName_Type(UTF8String):
    """Custom type avctDsrTrapObjectUserName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectUserName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectUserName_Object = MibScalar
avctDsrTrapObjectUserName = _AvctDsrTrapObjectUserName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 1),
    _AvctDsrTrapObjectUserName_Type()
)
avctDsrTrapObjectUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectUserName.setStatus("mandatory")


class _AvctDsrTrapObjectTargetUserName_Type(UTF8String):
    """Custom type avctDsrTrapObjectTargetUserName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectTargetUserName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectTargetUserName_Object = MibScalar
avctDsrTrapObjectTargetUserName = _AvctDsrTrapObjectTargetUserName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 2),
    _AvctDsrTrapObjectTargetUserName_Type()
)
avctDsrTrapObjectTargetUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectTargetUserName.setStatus("mandatory")


class _AvctDsrTrapObjectImageNewVersion_Type(DisplayString):
    """Custom type avctDsrTrapObjectImageNewVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectImageNewVersion_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectImageNewVersion_Object = MibScalar
avctDsrTrapObjectImageNewVersion = _AvctDsrTrapObjectImageNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 4),
    _AvctDsrTrapObjectImageNewVersion_Type()
)
avctDsrTrapObjectImageNewVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectImageNewVersion.setStatus("mandatory")


class _AvctDsrTrapObjectImageCurrentVersion_Type(DisplayString):
    """Custom type avctDsrTrapObjectImageCurrentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectImageCurrentVersion_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectImageCurrentVersion_Object = MibScalar
avctDsrTrapObjectImageCurrentVersion = _AvctDsrTrapObjectImageCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 5),
    _AvctDsrTrapObjectImageCurrentVersion_Type()
)
avctDsrTrapObjectImageCurrentVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectImageCurrentVersion.setStatus("mandatory")


class _AvctDsrTrapObjectServerName_Type(UTF8String):
    """Custom type avctDsrTrapObjectServerName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectServerName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectServerName_Object = MibScalar
avctDsrTrapObjectServerName = _AvctDsrTrapObjectServerName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 6),
    _AvctDsrTrapObjectServerName_Type()
)
avctDsrTrapObjectServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectServerName.setStatus("mandatory")


class _AvctDsrTrapObjectIqAdaptorId_Type(DisplayString):
    """Custom type avctDsrTrapObjectIqAdaptorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectIqAdaptorId_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectIqAdaptorId_Object = MibScalar
avctDsrTrapObjectIqAdaptorId = _AvctDsrTrapObjectIqAdaptorId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 7),
    _AvctDsrTrapObjectIqAdaptorId_Type()
)
avctDsrTrapObjectIqAdaptorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectIqAdaptorId.setStatus("mandatory")


class _AvctDsrTrapObjectIpAddress_Type(DisplayString):
    """Custom type avctDsrTrapObjectIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AvctDsrTrapObjectIpAddress_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectIpAddress_Object = MibScalar
avctDsrTrapObjectIpAddress = _AvctDsrTrapObjectIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 9),
    _AvctDsrTrapObjectIpAddress_Type()
)
avctDsrTrapObjectIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectIpAddress.setStatus("mandatory")


class _AvctDsrTrapObjectPreviousScreenResolution_Type(DisplayString):
    """Custom type avctDsrTrapObjectPreviousScreenResolution based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectPreviousScreenResolution_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectPreviousScreenResolution_Object = MibScalar
avctDsrTrapObjectPreviousScreenResolution = _AvctDsrTrapObjectPreviousScreenResolution_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 10),
    _AvctDsrTrapObjectPreviousScreenResolution_Type()
)
avctDsrTrapObjectPreviousScreenResolution.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectPreviousScreenResolution.setStatus("mandatory")


class _AvctDsrTrapObjectCurrentScreenResolution_Type(DisplayString):
    """Custom type avctDsrTrapObjectCurrentScreenResolution based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectCurrentScreenResolution_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectCurrentScreenResolution_Object = MibScalar
avctDsrTrapObjectCurrentScreenResolution = _AvctDsrTrapObjectCurrentScreenResolution_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 11),
    _AvctDsrTrapObjectCurrentScreenResolution_Type()
)
avctDsrTrapObjectCurrentScreenResolution.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectCurrentScreenResolution.setStatus("mandatory")


class _AvctDsrTrapObjectAggregatedServerStatusChanged_Type(OctetString):
    """Custom type avctDsrTrapObjectAggregatedServerStatusChanged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 5122),
    )


_AvctDsrTrapObjectAggregatedServerStatusChanged_Type.__name__ = "OctetString"
_AvctDsrTrapObjectAggregatedServerStatusChanged_Object = MibScalar
avctDsrTrapObjectAggregatedServerStatusChanged = _AvctDsrTrapObjectAggregatedServerStatusChanged_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 12),
    _AvctDsrTrapObjectAggregatedServerStatusChanged_Type()
)
avctDsrTrapObjectAggregatedServerStatusChanged.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectAggregatedServerStatusChanged.setStatus("mandatory")
_AvctDsrTrapObjectImageFileUpgradeResult_Type = ImageFileUpgradeResultsEnum
_AvctDsrTrapObjectImageFileUpgradeResult_Object = MibScalar
avctDsrTrapObjectImageFileUpgradeResult = _AvctDsrTrapObjectImageFileUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 13),
    _AvctDsrTrapObjectImageFileUpgradeResult_Type()
)
avctDsrTrapObjectImageFileUpgradeResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectImageFileUpgradeResult.setStatus("mandatory")
_AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Type = IqAdaptorUpgradeResultsEnum
_AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Object = MibScalar
avctDsrTrapObjectIqAdaptorImageUpgradeResult = _AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 14),
    _AvctDsrTrapObjectIqAdaptorImageUpgradeResult_Type()
)
avctDsrTrapObjectIqAdaptorImageUpgradeResult.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectIqAdaptorImageUpgradeResult.setStatus("mandatory")


class _AvctDsrTrapObjectTypeOfImage_Type(Integer32):
    """Custom type avctDsrTrapObjectTypeOfImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("boot", 1),
          ("app", 2))
    )


_AvctDsrTrapObjectTypeOfImage_Type.__name__ = "Integer32"
_AvctDsrTrapObjectTypeOfImage_Object = MibScalar
avctDsrTrapObjectTypeOfImage = _AvctDsrTrapObjectTypeOfImage_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 15),
    _AvctDsrTrapObjectTypeOfImage_Type()
)
avctDsrTrapObjectTypeOfImage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectTypeOfImage.setStatus("mandatory")
_AvctDsrTrapObjectInputPort_Type = Integer32
_AvctDsrTrapObjectInputPort_Object = MibScalar
avctDsrTrapObjectInputPort = _AvctDsrTrapObjectInputPort_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 16),
    _AvctDsrTrapObjectInputPort_Type()
)
avctDsrTrapObjectInputPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectInputPort.setStatus("mandatory")
_AvctDsrTrapObjectSwitchChannel_Type = Integer32
_AvctDsrTrapObjectSwitchChannel_Object = MibScalar
avctDsrTrapObjectSwitchChannel = _AvctDsrTrapObjectSwitchChannel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 17),
    _AvctDsrTrapObjectSwitchChannel_Type()
)
avctDsrTrapObjectSwitchChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSwitchChannel.setStatus("mandatory")


class _AvctDsrTrapObjectFileName_Type(DisplayString):
    """Custom type avctDsrTrapObjectFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AvctDsrTrapObjectFileName_Type.__name__ = "DisplayString"
_AvctDsrTrapObjectFileName_Object = MibScalar
avctDsrTrapObjectFileName = _AvctDsrTrapObjectFileName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 18),
    _AvctDsrTrapObjectFileName_Type()
)
avctDsrTrapObjectFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectFileName.setStatus("mandatory")
_AvctDsrTrapObjectActiveSessions_Type = Integer32
_AvctDsrTrapObjectActiveSessions_Object = MibScalar
avctDsrTrapObjectActiveSessions = _AvctDsrTrapObjectActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 19),
    _AvctDsrTrapObjectActiveSessions_Type()
)
avctDsrTrapObjectActiveSessions.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectActiveSessions.setStatus("mandatory")


class _AvctDsrTrapObjectCascadeSwitchName_Type(UTF8String):
    """Custom type avctDsrTrapObjectCascadeSwitchName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectCascadeSwitchName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectCascadeSwitchName_Object = MibScalar
avctDsrTrapObjectCascadeSwitchName = _AvctDsrTrapObjectCascadeSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 20),
    _AvctDsrTrapObjectCascadeSwitchName_Type()
)
avctDsrTrapObjectCascadeSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectCascadeSwitchName.setStatus("mandatory")


class _AvctDsrTrapObjectOldCascadeSwitchName_Type(UTF8String):
    """Custom type avctDsrTrapObjectOldCascadeSwitchName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectOldCascadeSwitchName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectOldCascadeSwitchName_Object = MibScalar
avctDsrTrapObjectOldCascadeSwitchName = _AvctDsrTrapObjectOldCascadeSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 21),
    _AvctDsrTrapObjectOldCascadeSwitchName_Type()
)
avctDsrTrapObjectOldCascadeSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectOldCascadeSwitchName.setStatus("mandatory")


class _AvctDsrTrapObjectOldServerName_Type(UTF8String):
    """Custom type avctDsrTrapObjectOldServerName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectOldServerName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectOldServerName_Object = MibScalar
avctDsrTrapObjectOldServerName = _AvctDsrTrapObjectOldServerName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 22),
    _AvctDsrTrapObjectOldServerName_Type()
)
avctDsrTrapObjectOldServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectOldServerName.setStatus("mandatory")


class _AvctDsrTrapObjectSpcDeviceLocation_Type(UTF8String):
    """Custom type avctDsrTrapObjectSpcDeviceLocation based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectSpcDeviceLocation_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectSpcDeviceLocation_Object = MibScalar
avctDsrTrapObjectSpcDeviceLocation = _AvctDsrTrapObjectSpcDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 23),
    _AvctDsrTrapObjectSpcDeviceLocation_Type()
)
avctDsrTrapObjectSpcDeviceLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcDeviceLocation.setStatus("mandatory")


class _AvctDsrTrapObjectSpcDevicePort_Type(Integer32):
    """Custom type avctDsrTrapObjectSpcDevicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AvctDsrTrapObjectSpcDevicePort_Type.__name__ = "Integer32"
_AvctDsrTrapObjectSpcDevicePort_Object = MibScalar
avctDsrTrapObjectSpcDevicePort = _AvctDsrTrapObjectSpcDevicePort_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 24),
    _AvctDsrTrapObjectSpcDevicePort_Type()
)
avctDsrTrapObjectSpcDevicePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcDevicePort.setStatus("mandatory")


class _AvctDsrTrapObjectSpcDeviceLogin_Type(UTF8String):
    """Custom type avctDsrTrapObjectSpcDeviceLogin based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvctDsrTrapObjectSpcDeviceLogin_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectSpcDeviceLogin_Object = MibScalar
avctDsrTrapObjectSpcDeviceLogin = _AvctDsrTrapObjectSpcDeviceLogin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 25),
    _AvctDsrTrapObjectSpcDeviceLogin_Type()
)
avctDsrTrapObjectSpcDeviceLogin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcDeviceLogin.setStatus("mandatory")


class _AvctDsrTrapObjectSpcSocket_Type(Integer32):
    """Custom type avctDsrTrapObjectSpcSocket based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AvctDsrTrapObjectSpcSocket_Type.__name__ = "Integer32"
_AvctDsrTrapObjectSpcSocket_Object = MibScalar
avctDsrTrapObjectSpcSocket = _AvctDsrTrapObjectSpcSocket_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 26),
    _AvctDsrTrapObjectSpcSocket_Type()
)
avctDsrTrapObjectSpcSocket.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcSocket.setStatus("mandatory")


class _AvctDsrTrapObjectOldName_Type(UTF8String):
    """Custom type avctDsrTrapObjectOldName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectOldName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectOldName_Object = MibScalar
avctDsrTrapObjectOldName = _AvctDsrTrapObjectOldName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 27),
    _AvctDsrTrapObjectOldName_Type()
)
avctDsrTrapObjectOldName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectOldName.setStatus("mandatory")


class _AvctDsrTrapObjectItemName_Type(UTF8String):
    """Custom type avctDsrTrapObjectItemName based on UTF8String"""
    subtypeSpec = UTF8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvctDsrTrapObjectItemName_Type.__name__ = "UTF8String"
_AvctDsrTrapObjectItemName_Object = MibScalar
avctDsrTrapObjectItemName = _AvctDsrTrapObjectItemName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 28),
    _AvctDsrTrapObjectItemName_Type()
)
avctDsrTrapObjectItemName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectItemName.setStatus("mandatory")
_AvctDsrTrapObjectSpcDeviceInlet_Type = Integer32
_AvctDsrTrapObjectSpcDeviceInlet_Object = MibScalar
avctDsrTrapObjectSpcDeviceInlet = _AvctDsrTrapObjectSpcDeviceInlet_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 29),
    _AvctDsrTrapObjectSpcDeviceInlet_Type()
)
avctDsrTrapObjectSpcDeviceInlet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcDeviceInlet.setStatus("mandatory")
_AvctDsrTrapObjectSpcDeviceNumber_Type = Integer32
_AvctDsrTrapObjectSpcDeviceNumber_Object = MibScalar
avctDsrTrapObjectSpcDeviceNumber = _AvctDsrTrapObjectSpcDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 30),
    _AvctDsrTrapObjectSpcDeviceNumber_Type()
)
avctDsrTrapObjectSpcDeviceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcDeviceNumber.setStatus("mandatory")
_AvctDsrTrapObjectOldInputPort_Type = Integer32
_AvctDsrTrapObjectOldInputPort_Object = MibScalar
avctDsrTrapObjectOldInputPort = _AvctDsrTrapObjectOldInputPort_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 31),
    _AvctDsrTrapObjectOldInputPort_Type()
)
avctDsrTrapObjectOldInputPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectOldInputPort.setStatus("mandatory")
_AvctDsrTrapObjectPowerSupply_Type = Integer32
_AvctDsrTrapObjectPowerSupply_Object = MibScalar
avctDsrTrapObjectPowerSupply = _AvctDsrTrapObjectPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 32),
    _AvctDsrTrapObjectPowerSupply_Type()
)
avctDsrTrapObjectPowerSupply.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectPowerSupply.setStatus("mandatory")
_AvctDsrTrapObjectSpcDeviceCircuit_Type = Integer32
_AvctDsrTrapObjectSpcDeviceCircuit_Object = MibScalar
avctDsrTrapObjectSpcDeviceCircuit = _AvctDsrTrapObjectSpcDeviceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 10418, 7, 2, 6, 33),
    _AvctDsrTrapObjectSpcDeviceCircuit_Type()
)
avctDsrTrapObjectSpcDeviceCircuit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avctDsrTrapObjectSpcDeviceCircuit.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSR-TRAP-OBJECTS-MIB",
    **{"UTF8String": UTF8String,
       "ImageFileUpgradeResultsEnum": ImageFileUpgradeResultsEnum,
       "IqAdaptorUpgradeResultsEnum": IqAdaptorUpgradeResultsEnum,
       "avocent": avocent,
       "dsr": dsr,
       "dsrProducts": dsrProducts,
       "dsrManagement": dsrManagement,
       "dsrTrapObject": dsrTrapObject,
       "avctDsrTrapObjectUserName": avctDsrTrapObjectUserName,
       "avctDsrTrapObjectTargetUserName": avctDsrTrapObjectTargetUserName,
       "avctDsrTrapObjectImageNewVersion": avctDsrTrapObjectImageNewVersion,
       "avctDsrTrapObjectImageCurrentVersion": avctDsrTrapObjectImageCurrentVersion,
       "avctDsrTrapObjectServerName": avctDsrTrapObjectServerName,
       "avctDsrTrapObjectIqAdaptorId": avctDsrTrapObjectIqAdaptorId,
       "avctDsrTrapObjectIpAddress": avctDsrTrapObjectIpAddress,
       "avctDsrTrapObjectPreviousScreenResolution": avctDsrTrapObjectPreviousScreenResolution,
       "avctDsrTrapObjectCurrentScreenResolution": avctDsrTrapObjectCurrentScreenResolution,
       "avctDsrTrapObjectAggregatedServerStatusChanged": avctDsrTrapObjectAggregatedServerStatusChanged,
       "avctDsrTrapObjectImageFileUpgradeResult": avctDsrTrapObjectImageFileUpgradeResult,
       "avctDsrTrapObjectIqAdaptorImageUpgradeResult": avctDsrTrapObjectIqAdaptorImageUpgradeResult,
       "avctDsrTrapObjectTypeOfImage": avctDsrTrapObjectTypeOfImage,
       "avctDsrTrapObjectInputPort": avctDsrTrapObjectInputPort,
       "avctDsrTrapObjectSwitchChannel": avctDsrTrapObjectSwitchChannel,
       "avctDsrTrapObjectFileName": avctDsrTrapObjectFileName,
       "avctDsrTrapObjectActiveSessions": avctDsrTrapObjectActiveSessions,
       "avctDsrTrapObjectCascadeSwitchName": avctDsrTrapObjectCascadeSwitchName,
       "avctDsrTrapObjectOldCascadeSwitchName": avctDsrTrapObjectOldCascadeSwitchName,
       "avctDsrTrapObjectOldServerName": avctDsrTrapObjectOldServerName,
       "avctDsrTrapObjectSpcDeviceLocation": avctDsrTrapObjectSpcDeviceLocation,
       "avctDsrTrapObjectSpcDevicePort": avctDsrTrapObjectSpcDevicePort,
       "avctDsrTrapObjectSpcDeviceLogin": avctDsrTrapObjectSpcDeviceLogin,
       "avctDsrTrapObjectSpcSocket": avctDsrTrapObjectSpcSocket,
       "avctDsrTrapObjectOldName": avctDsrTrapObjectOldName,
       "avctDsrTrapObjectItemName": avctDsrTrapObjectItemName,
       "avctDsrTrapObjectSpcDeviceInlet": avctDsrTrapObjectSpcDeviceInlet,
       "avctDsrTrapObjectSpcDeviceNumber": avctDsrTrapObjectSpcDeviceNumber,
       "avctDsrTrapObjectOldInputPort": avctDsrTrapObjectOldInputPort,
       "avctDsrTrapObjectPowerSupply": avctDsrTrapObjectPowerSupply,
       "avctDsrTrapObjectSpcDeviceCircuit": avctDsrTrapObjectSpcDeviceCircuit}
)
