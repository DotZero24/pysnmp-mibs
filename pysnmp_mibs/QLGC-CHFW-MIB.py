# SNMP MIB module (QLGC-CHFW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/marvell/QLGC-CHFW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:47:51 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(qlogicMgmt,) = mibBuilder.importSymbols(
    "QLOGIC-SMI",
    "qlogicMgmt")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qlgcChangeFirmwareModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1)
)
if mibBuilder.loadTexts:
    qlgcChangeFirmwareModule.setRevisions(
        ("2006-01-26 00:00",
         "2005-08-24 00:00",
         "2005-06-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QlgcChFwNotifications_ObjectIdentity = ObjectIdentity
qlgcChFwNotifications = _QlgcChFwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 0)
)
_QlgcChFwObjects_ObjectIdentity = ObjectIdentity
qlgcChFwObjects = _QlgcChFwObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1)
)
_QlgcChFwOpTypes_ObjectIdentity = ObjectIdentity
qlgcChFwOpTypes = _QlgcChFwOpTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1)
)
_QlgcChFwOperDownload_ObjectIdentity = ObjectIdentity
qlgcChFwOperDownload = _QlgcChFwOperDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qlgcChFwOperDownload.setStatus("current")
_QlgcChFwDwldNoErr_ObjectIdentity = ObjectIdentity
qlgcChFwDwldNoErr = _QlgcChFwDwldNoErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qlgcChFwDwldNoErr.setStatus("current")
_QlgcChFwDwldHostErr_ObjectIdentity = ObjectIdentity
qlgcChFwDwldHostErr = _QlgcChFwDwldHostErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qlgcChFwDwldHostErr.setStatus("obsolete")
_QlgcChFwDwldFileErr_ObjectIdentity = ObjectIdentity
qlgcChFwDwldFileErr = _QlgcChFwDwldFileErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qlgcChFwDwldFileErr.setStatus("obsolete")
_QlgcChFwDwldTftpErr_ObjectIdentity = ObjectIdentity
qlgcChFwDwldTftpErr = _QlgcChFwDwldTftpErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qlgcChFwDwldTftpErr.setStatus("current")
_QlgcChFwOperInstall_ObjectIdentity = ObjectIdentity
qlgcChFwOperInstall = _QlgcChFwOperInstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qlgcChFwOperInstall.setStatus("current")
_QlgcChFwInstallNoErr_ObjectIdentity = ObjectIdentity
qlgcChFwInstallNoErr = _QlgcChFwInstallNoErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qlgcChFwInstallNoErr.setStatus("current")
_QlgcChFwInstallFileErr_ObjectIdentity = ObjectIdentity
qlgcChFwInstallFileErr = _QlgcChFwInstallFileErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qlgcChFwInstallFileErr.setStatus("current")
_QlgcChFwInstallFileNoAdminErr_ObjectIdentity = ObjectIdentity
qlgcChFwInstallFileNoAdminErr = _QlgcChFwInstallFileNoAdminErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qlgcChFwInstallFileNoAdminErr.setStatus("current")
_QlgcChFwOperReset_ObjectIdentity = ObjectIdentity
qlgcChFwOperReset = _QlgcChFwOperReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qlgcChFwOperReset.setStatus("current")
_QlgcChFwResetNoErr_ObjectIdentity = ObjectIdentity
qlgcChFwResetNoErr = _QlgcChFwResetNoErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qlgcChFwResetNoErr.setStatus("current")
_QlgcChFwResetErr_ObjectIdentity = ObjectIdentity
qlgcChFwResetErr = _QlgcChFwResetErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    qlgcChFwResetErr.setStatus("current")
_QlgcChFwResetNoAdminErr_ObjectIdentity = ObjectIdentity
qlgcChFwResetNoAdminErr = _QlgcChFwResetNoAdminErr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    qlgcChFwResetNoAdminErr.setStatus("current")
_QlgcChFwOpControl_ObjectIdentity = ObjectIdentity
qlgcChFwOpControl = _QlgcChFwOpControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2)
)


class _QlgcChFwOpResult_Type(AutonomousType):
    """Custom type qlgcChFwOpResult based on AutonomousType"""
    defaultValue = (0, 0)


_QlgcChFwOpResult_Type.__name__ = "AutonomousType"
_QlgcChFwOpResult_Object = MibScalar
qlgcChFwOpResult = _QlgcChFwOpResult_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 1),
    _QlgcChFwOpResult_Type()
)
qlgcChFwOpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qlgcChFwOpResult.setStatus("current")


class _QlgcChFwOpRequest_Type(Integer32):
    """Custom type qlgcChFwOpRequest based on Integer32"""
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
        *(("auto", 1),
          ("downloadOnly", 2),
          ("installOnly", 3),
          ("resetOnly", 4))
    )


_QlgcChFwOpRequest_Type.__name__ = "Integer32"
_QlgcChFwOpRequest_Object = MibScalar
qlgcChFwOpRequest = _QlgcChFwOpRequest_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 2),
    _QlgcChFwOpRequest_Type()
)
qlgcChFwOpRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwOpRequest.setStatus("current")


class _QlgcChFwDwldHostAddrType_Type(InetAddressType):
    """Custom type qlgcChFwDwldHostAddrType based on InetAddressType"""
    defaultValue = 1


_QlgcChFwDwldHostAddrType_Type.__name__ = "InetAddressType"
_QlgcChFwDwldHostAddrType_Object = MibScalar
qlgcChFwDwldHostAddrType = _QlgcChFwDwldHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 3),
    _QlgcChFwDwldHostAddrType_Type()
)
qlgcChFwDwldHostAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwDwldHostAddrType.setStatus("current")
_QlgcChFwDwldHostAddr_Type = InetAddress
_QlgcChFwDwldHostAddr_Object = MibScalar
qlgcChFwDwldHostAddr = _QlgcChFwDwldHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 4),
    _QlgcChFwDwldHostAddr_Type()
)
qlgcChFwDwldHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwDwldHostAddr.setStatus("current")


class _QlgcChFwDwldHostPort_Type(InetPortNumber):
    """Custom type qlgcChFwDwldHostPort based on InetPortNumber"""
    defaultValue = 69


_QlgcChFwDwldHostPort_Type.__name__ = "InetPortNumber"
_QlgcChFwDwldHostPort_Object = MibScalar
qlgcChFwDwldHostPort = _QlgcChFwDwldHostPort_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 5),
    _QlgcChFwDwldHostPort_Type()
)
qlgcChFwDwldHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwDwldHostPort.setStatus("current")


class _QlgcChFwDwldPathName_Type(DisplayString):
    """Custom type qlgcChFwDwldPathName based on DisplayString"""
    defaultValue = OctetString("/")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QlgcChFwDwldPathName_Type.__name__ = "DisplayString"
_QlgcChFwDwldPathName_Object = MibScalar
qlgcChFwDwldPathName = _QlgcChFwDwldPathName_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 6),
    _QlgcChFwDwldPathName_Type()
)
qlgcChFwDwldPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwDwldPathName.setStatus("current")


class _QlgcChFwDwldFileName_Type(DisplayString):
    """Custom type qlgcChFwDwldFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QlgcChFwDwldFileName_Type.__name__ = "DisplayString"
_QlgcChFwDwldFileName_Object = MibScalar
qlgcChFwDwldFileName = _QlgcChFwDwldFileName_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 7),
    _QlgcChFwDwldFileName_Type()
)
qlgcChFwDwldFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwDwldFileName.setStatus("current")


class _QlgcChFwResetMethod_Type(Integer32):
    """Custom type qlgcChFwResetMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("ndcla", 2))
    )


_QlgcChFwResetMethod_Type.__name__ = "Integer32"
_QlgcChFwResetMethod_Object = MibScalar
qlgcChFwResetMethod = _QlgcChFwResetMethod_Object(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 1, 2, 8),
    _QlgcChFwResetMethod_Type()
)
qlgcChFwResetMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qlgcChFwResetMethod.setStatus("current")
_QlgcChFwConformance_ObjectIdentity = ObjectIdentity
qlgcChFwConformance = _QlgcChFwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 2)
)
_QlgcChFwGroups_ObjectIdentity = ObjectIdentity
qlgcChFwGroups = _QlgcChFwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 2, 1)
)
_QlgcChFwCompliances_ObjectIdentity = ObjectIdentity
qlgcChFwCompliances = _QlgcChFwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 2, 2)
)

# Managed Objects groups

qlgcChFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 2, 1, 1)
)
qlgcChFwGroup.setObjects(
      *(("QLGC-CHFW-MIB", "qlgcChFwOpResult"),
        ("QLGC-CHFW-MIB", "qlgcChFwOpRequest"),
        ("QLGC-CHFW-MIB", "qlgcChFwDwldHostAddrType"),
        ("QLGC-CHFW-MIB", "qlgcChFwDwldHostAddr"),
        ("QLGC-CHFW-MIB", "qlgcChFwDwldHostPort"),
        ("QLGC-CHFW-MIB", "qlgcChFwDwldPathName"),
        ("QLGC-CHFW-MIB", "qlgcChFwDwldFileName"),
        ("QLGC-CHFW-MIB", "qlgcChFwResetMethod"))
)
if mibBuilder.loadTexts:
    qlgcChFwGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qlgcChFwComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3873, 3, 1, 2, 2, 1)
)
qlgcChFwComplianceV1.setObjects(
    ("QLGC-CHFW-MIB", "qlgcChFwGroup")
)
if mibBuilder.loadTexts:
    qlgcChFwComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QLGC-CHFW-MIB",
    **{"qlgcChangeFirmwareModule": qlgcChangeFirmwareModule,
       "qlgcChFwNotifications": qlgcChFwNotifications,
       "qlgcChFwObjects": qlgcChFwObjects,
       "qlgcChFwOpTypes": qlgcChFwOpTypes,
       "qlgcChFwOperDownload": qlgcChFwOperDownload,
       "qlgcChFwDwldNoErr": qlgcChFwDwldNoErr,
       "qlgcChFwDwldHostErr": qlgcChFwDwldHostErr,
       "qlgcChFwDwldFileErr": qlgcChFwDwldFileErr,
       "qlgcChFwDwldTftpErr": qlgcChFwDwldTftpErr,
       "qlgcChFwOperInstall": qlgcChFwOperInstall,
       "qlgcChFwInstallNoErr": qlgcChFwInstallNoErr,
       "qlgcChFwInstallFileErr": qlgcChFwInstallFileErr,
       "qlgcChFwInstallFileNoAdminErr": qlgcChFwInstallFileNoAdminErr,
       "qlgcChFwOperReset": qlgcChFwOperReset,
       "qlgcChFwResetNoErr": qlgcChFwResetNoErr,
       "qlgcChFwResetErr": qlgcChFwResetErr,
       "qlgcChFwResetNoAdminErr": qlgcChFwResetNoAdminErr,
       "qlgcChFwOpControl": qlgcChFwOpControl,
       "qlgcChFwOpResult": qlgcChFwOpResult,
       "qlgcChFwOpRequest": qlgcChFwOpRequest,
       "qlgcChFwDwldHostAddrType": qlgcChFwDwldHostAddrType,
       "qlgcChFwDwldHostAddr": qlgcChFwDwldHostAddr,
       "qlgcChFwDwldHostPort": qlgcChFwDwldHostPort,
       "qlgcChFwDwldPathName": qlgcChFwDwldPathName,
       "qlgcChFwDwldFileName": qlgcChFwDwldFileName,
       "qlgcChFwResetMethod": qlgcChFwResetMethod,
       "qlgcChFwConformance": qlgcChFwConformance,
       "qlgcChFwGroups": qlgcChFwGroups,
       "qlgcChFwGroup": qlgcChFwGroup,
       "qlgcChFwCompliances": qlgcChFwCompliances,
       "qlgcChFwComplianceV1": qlgcChFwComplianceV1}
)
