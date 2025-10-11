# SNMP MIB module (SYSLOG-R-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/SYSLOG-R-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:31 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(radExperimental,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radExperimental")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

syslogMIBR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogRoles(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("sender", 0),
          ("receiver", 1),
          ("relay", 2))
    )


class SyslogService(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class SyslogEncapsulation(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("none", 2),
          ("tls", 3),
          ("beep", 4))
    )



# MIB Managed Objects in the order of their OIDs

_SyslogNotifications_ObjectIdentity = ObjectIdentity
syslogNotifications = _SyslogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 0)
)
_SyslogObjects_ObjectIdentity = ObjectIdentity
syslogObjects = _SyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1)
)
_SyslogSystem_ObjectIdentity = ObjectIdentity
syslogSystem = _SyslogSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 1)
)


class _SyslogDefaultService_Type(SyslogService):
    """Custom type syslogDefaultService based on SyslogService"""
    defaultValue = OctetString("514")


_SyslogDefaultService_Type.__name__ = "SyslogService"
_SyslogDefaultService_Object = MibScalar
syslogDefaultService = _SyslogDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 1, 1),
    _SyslogDefaultService_Type()
)
syslogDefaultService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogDefaultService.setStatus("current")


class _SyslogDefaultEncapsulation_Type(SyslogEncapsulation):
    """Custom type syslogDefaultEncapsulation based on SyslogEncapsulation"""
    defaultValue = 2


_SyslogDefaultEncapsulation_Type.__name__ = "SyslogEncapsulation"
_SyslogDefaultEncapsulation_Object = MibScalar
syslogDefaultEncapsulation = _SyslogDefaultEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 1, 2),
    _SyslogDefaultEncapsulation_Type()
)
syslogDefaultEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogDefaultEncapsulation.setStatus("current")
_SyslogControlTable_Object = MibTable
syslogControlTable = _SyslogControlTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2)
)
if mibBuilder.loadTexts:
    syslogControlTable.setStatus("current")
_SyslogControlEntry_Object = MibTableRow
syslogControlEntry = _SyslogControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1)
)
syslogControlEntry.setIndexNames(
    (0, "SYSLOG-R-MIB", "syslogControlIndex"),
)
if mibBuilder.loadTexts:
    syslogControlEntry.setStatus("current")


class _SyslogControlIndex_Type(Unsigned32):
    """Custom type syslogControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SyslogControlIndex_Type.__name__ = "Unsigned32"
_SyslogControlIndex_Object = MibTableColumn
syslogControlIndex = _SyslogControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 1),
    _SyslogControlIndex_Type()
)
syslogControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogControlIndex.setStatus("current")
_SyslogControlDescr_Type = SnmpAdminString
_SyslogControlDescr_Object = MibTableColumn
syslogControlDescr = _SyslogControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 2),
    _SyslogControlDescr_Type()
)
syslogControlDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlDescr.setStatus("current")
_SyslogControlRoles_Type = SyslogRoles
_SyslogControlRoles_Object = MibTableColumn
syslogControlRoles = _SyslogControlRoles_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 3),
    _SyslogControlRoles_Type()
)
syslogControlRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlRoles.setStatus("current")
_SyslogControlBindAddrType_Type = InetAddressType
_SyslogControlBindAddrType_Object = MibTableColumn
syslogControlBindAddrType = _SyslogControlBindAddrType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 4),
    _SyslogControlBindAddrType_Type()
)
syslogControlBindAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlBindAddrType.setStatus("current")
_SyslogControlBindAddr_Type = InetAddress
_SyslogControlBindAddr_Object = MibTableColumn
syslogControlBindAddr = _SyslogControlBindAddr_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 5),
    _SyslogControlBindAddr_Type()
)
syslogControlBindAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlBindAddr.setStatus("current")
_SyslogControlService_Type = SyslogService
_SyslogControlService_Object = MibTableColumn
syslogControlService = _SyslogControlService_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 6),
    _SyslogControlService_Type()
)
syslogControlService.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlService.setStatus("current")
_SyslogControlEncapsulation_Type = SyslogEncapsulation
_SyslogControlEncapsulation_Object = MibTableColumn
syslogControlEncapsulation = _SyslogControlEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 7),
    _SyslogControlEncapsulation_Type()
)
syslogControlEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlEncapsulation.setStatus("current")
_SyslogControlMaxMessageSize_Type = Unsigned32
_SyslogControlMaxMessageSize_Object = MibTableColumn
syslogControlMaxMessageSize = _SyslogControlMaxMessageSize_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 8),
    _SyslogControlMaxMessageSize_Type()
)
syslogControlMaxMessageSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlMaxMessageSize.setStatus("current")


class _SyslogControlConfFileName_Type(SnmpAdminString):
    """Custom type syslogControlConfFileName based on SnmpAdminString"""
    defaultValue = OctetString("/etc/syslog.conf")


_SyslogControlConfFileName_Type.__name__ = "SnmpAdminString"
_SyslogControlConfFileName_Object = MibTableColumn
syslogControlConfFileName = _SyslogControlConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 9),
    _SyslogControlConfFileName_Type()
)
syslogControlConfFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlConfFileName.setStatus("current")


class _SyslogControlStorageType_Type(StorageType):
    """Custom type syslogControlStorageType based on StorageType"""
    defaultValue = 3


_SyslogControlStorageType_Type.__name__ = "StorageType"
_SyslogControlStorageType_Object = MibTableColumn
syslogControlStorageType = _SyslogControlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 11),
    _SyslogControlStorageType_Type()
)
syslogControlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlStorageType.setStatus("current")
_SyslogControlRowStatus_Type = RowStatus
_SyslogControlRowStatus_Object = MibTableColumn
syslogControlRowStatus = _SyslogControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 12),
    _SyslogControlRowStatus_Type()
)
syslogControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlRowStatus.setStatus("current")


class _SyslogControlAccountingType_Type(Bits):
    """Custom type syslogControlAccountingType based on Bits"""
    namedValues = NamedValues(
        *(("shell", 0),
          ("system", 1),
          ("commands", 2))
    )

_SyslogControlAccountingType_Type.__name__ = "Bits"
_SyslogControlAccountingType_Object = MibTableColumn
syslogControlAccountingType = _SyslogControlAccountingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 2, 1, 13),
    _SyslogControlAccountingType_Type()
)
syslogControlAccountingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogControlAccountingType.setStatus("current")
_SyslogOperationsTable_Object = MibTable
syslogOperationsTable = _SyslogOperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3)
)
if mibBuilder.loadTexts:
    syslogOperationsTable.setStatus("current")
_SyslogOperationsEntry_Object = MibTableRow
syslogOperationsEntry = _SyslogOperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1)
)
if mibBuilder.loadTexts:
    syslogOperationsEntry.setStatus("current")
_SyslogOperationsMsgsReceived_Type = Counter32
_SyslogOperationsMsgsReceived_Object = MibTableColumn
syslogOperationsMsgsReceived = _SyslogOperationsMsgsReceived_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 1),
    _SyslogOperationsMsgsReceived_Type()
)
syslogOperationsMsgsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsMsgsReceived.setStatus("current")
_SyslogOperationsMsgsTransmitted_Type = Counter32
_SyslogOperationsMsgsTransmitted_Object = MibTableColumn
syslogOperationsMsgsTransmitted = _SyslogOperationsMsgsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 2),
    _SyslogOperationsMsgsTransmitted_Type()
)
syslogOperationsMsgsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsMsgsTransmitted.setStatus("current")
_SyslogOperationsMsgsRelayed_Type = Counter32
_SyslogOperationsMsgsRelayed_Object = MibTableColumn
syslogOperationsMsgsRelayed = _SyslogOperationsMsgsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 3),
    _SyslogOperationsMsgsRelayed_Type()
)
syslogOperationsMsgsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsMsgsRelayed.setStatus("current")
_SyslogOperationsMsgsDropped_Type = Counter32
_SyslogOperationsMsgsDropped_Object = MibTableColumn
syslogOperationsMsgsDropped = _SyslogOperationsMsgsDropped_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 4),
    _SyslogOperationsMsgsDropped_Type()
)
syslogOperationsMsgsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsMsgsDropped.setStatus("current")
_SyslogOperationsMsgsMalFormed_Type = Counter32
_SyslogOperationsMsgsMalFormed_Object = MibTableColumn
syslogOperationsMsgsMalFormed = _SyslogOperationsMsgsMalFormed_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 5),
    _SyslogOperationsMsgsMalFormed_Type()
)
syslogOperationsMsgsMalFormed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsMsgsMalFormed.setStatus("current")
_SyslogOperationsMsgsDiscarded_Type = Counter32
_SyslogOperationsMsgsDiscarded_Object = MibTableColumn
syslogOperationsMsgsDiscarded = _SyslogOperationsMsgsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 6),
    _SyslogOperationsMsgsDiscarded_Type()
)
syslogOperationsMsgsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsMsgsDiscarded.setStatus("current")
_SyslogOperationsLastMsgRecdTime_Type = TimeStamp
_SyslogOperationsLastMsgRecdTime_Object = MibTableColumn
syslogOperationsLastMsgRecdTime = _SyslogOperationsLastMsgRecdTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 7),
    _SyslogOperationsLastMsgRecdTime_Type()
)
syslogOperationsLastMsgRecdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsLastMsgRecdTime.setStatus("current")
_SyslogOperationsLastMsgTransmittedTime_Type = TimeStamp
_SyslogOperationsLastMsgTransmittedTime_Object = MibTableColumn
syslogOperationsLastMsgTransmittedTime = _SyslogOperationsLastMsgTransmittedTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 8),
    _SyslogOperationsLastMsgTransmittedTime_Type()
)
syslogOperationsLastMsgTransmittedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsLastMsgTransmittedTime.setStatus("current")
_SyslogOperationsStartTime_Type = TimeStamp
_SyslogOperationsStartTime_Object = MibTableColumn
syslogOperationsStartTime = _SyslogOperationsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 9),
    _SyslogOperationsStartTime_Type()
)
syslogOperationsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsStartTime.setStatus("current")
_SyslogOperationsLastError_Type = SnmpAdminString
_SyslogOperationsLastError_Object = MibTableColumn
syslogOperationsLastError = _SyslogOperationsLastError_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 10),
    _SyslogOperationsLastError_Type()
)
syslogOperationsLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsLastError.setStatus("current")
_SyslogOperationsLastErrorTime_Type = TimeStamp
_SyslogOperationsLastErrorTime_Object = MibTableColumn
syslogOperationsLastErrorTime = _SyslogOperationsLastErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 11),
    _SyslogOperationsLastErrorTime_Type()
)
syslogOperationsLastErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsLastErrorTime.setStatus("current")


class _SyslogOperationsRunIndex_Type(Integer32):
    """Custom type syslogOperationsRunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SyslogOperationsRunIndex_Type.__name__ = "Integer32"
_SyslogOperationsRunIndex_Object = MibTableColumn
syslogOperationsRunIndex = _SyslogOperationsRunIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 12),
    _SyslogOperationsRunIndex_Type()
)
syslogOperationsRunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsRunIndex.setStatus("current")
_SyslogOperationsCounterDiscontinuityTime_Type = TimeStamp
_SyslogOperationsCounterDiscontinuityTime_Object = MibTableColumn
syslogOperationsCounterDiscontinuityTime = _SyslogOperationsCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 13),
    _SyslogOperationsCounterDiscontinuityTime_Type()
)
syslogOperationsCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsCounterDiscontinuityTime.setStatus("current")


class _SyslogOperationsStatus_Type(Integer32):
    """Custom type syslogOperationsStatus based on Integer32"""
    defaultValue = 1

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
          ("started", 2),
          ("suspended", 3),
          ("stopped", 4))
    )


_SyslogOperationsStatus_Type.__name__ = "Integer32"
_SyslogOperationsStatus_Object = MibTableColumn
syslogOperationsStatus = _SyslogOperationsStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 1, 3, 1, 14),
    _SyslogOperationsStatus_Type()
)
syslogOperationsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogOperationsStatus.setStatus("current")
_SyslogConformance_ObjectIdentity = ObjectIdentity
syslogConformance = _SyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3)
)
_SyslogGroups_ObjectIdentity = ObjectIdentity
syslogGroups = _SyslogGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1)
)
_SyslogCompliances_ObjectIdentity = ObjectIdentity
syslogCompliances = _SyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2)
)
syslogControlEntry.registerAugmentions(
    ("SYSLOG-R-MIB",
     "syslogOperationsEntry")
)
syslogOperationsEntry.setIndexNames(*syslogControlEntry.getIndexNames())

# Managed Objects groups

syslogDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 1)
)
syslogDefaultGroup.setObjects(
      *(("SYSLOG-R-MIB", "syslogDefaultService"),
        ("SYSLOG-R-MIB", "syslogDefaultEncapsulation"))
)
if mibBuilder.loadTexts:
    syslogDefaultGroup.setStatus("current")

syslogOperationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 2)
)
syslogOperationsGroup.setObjects(
      *(("SYSLOG-R-MIB", "syslogOperationsMsgsReceived"),
        ("SYSLOG-R-MIB", "syslogOperationsMsgsTransmitted"),
        ("SYSLOG-R-MIB", "syslogOperationsMsgsRelayed"),
        ("SYSLOG-R-MIB", "syslogOperationsMsgsDropped"),
        ("SYSLOG-R-MIB", "syslogOperationsMsgsMalFormed"),
        ("SYSLOG-R-MIB", "syslogOperationsMsgsDiscarded"),
        ("SYSLOG-R-MIB", "syslogOperationsLastMsgRecdTime"),
        ("SYSLOG-R-MIB", "syslogOperationsLastMsgTransmittedTime"),
        ("SYSLOG-R-MIB", "syslogOperationsStartTime"),
        ("SYSLOG-R-MIB", "syslogOperationsLastError"),
        ("SYSLOG-R-MIB", "syslogOperationsLastErrorTime"),
        ("SYSLOG-R-MIB", "syslogOperationsRunIndex"),
        ("SYSLOG-R-MIB", "syslogOperationsCounterDiscontinuityTime"),
        ("SYSLOG-R-MIB", "syslogOperationsStatus"))
)
if mibBuilder.loadTexts:
    syslogOperationsGroup.setStatus("current")

syslogControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 3)
)
syslogControlGroup.setObjects(
      *(("SYSLOG-R-MIB", "syslogControlDescr"),
        ("SYSLOG-R-MIB", "syslogControlRoles"),
        ("SYSLOG-R-MIB", "syslogControlBindAddrType"),
        ("SYSLOG-R-MIB", "syslogControlBindAddr"),
        ("SYSLOG-R-MIB", "syslogControlEncapsulation"),
        ("SYSLOG-R-MIB", "syslogControlService"),
        ("SYSLOG-R-MIB", "syslogControlMaxMessageSize"),
        ("SYSLOG-R-MIB", "syslogControlConfFileName"),
        ("SYSLOG-R-MIB", "syslogControlStorageType"),
        ("SYSLOG-R-MIB", "syslogControlRowStatus"))
)
if mibBuilder.loadTexts:
    syslogControlGroup.setStatus("current")


# Notification objects

syslogStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 0, 1)
)
syslogStatusChanged.setObjects(
      *(("SYSLOG-R-MIB", "syslogControlDescr"),
        ("SYSLOG-R-MIB", "syslogControlRoles"),
        ("SYSLOG-R-MIB", "syslogControlBindAddrType"),
        ("SYSLOG-R-MIB", "syslogControlBindAddr"),
        ("SYSLOG-R-MIB", "syslogControlService"),
        ("SYSLOG-R-MIB", "syslogControlEncapsulation"),
        ("SYSLOG-R-MIB", "syslogControlConfFileName"),
        ("SYSLOG-R-MIB", "syslogOperationsStatus"))
)
if mibBuilder.loadTexts:
    syslogStatusChanged.setStatus(
        "current"
    )


# Notifications groups

syslogNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 1, 4)
)
syslogNotificationGroup.setObjects(
    ("SYSLOG-R-MIB", "syslogStatusChanged")
)
if mibBuilder.loadTexts:
    syslogNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

syslogFullCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 1)
)
syslogFullCompliance1.setObjects(
      *(("SYSLOG-R-MIB", "syslogNotificationGroup"),
        ("SYSLOG-R-MIB", "syslogDefaultGroup"),
        ("SYSLOG-R-MIB", "syslogOperationsGroup"),
        ("SYSLOG-R-MIB", "syslogControlGroup"))
)
if mibBuilder.loadTexts:
    syslogFullCompliance1.setStatus(
        "current"
    )

syslogFullCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 2)
)
syslogFullCompliance2.setObjects(
      *(("SYSLOG-R-MIB", "syslogDefaultGroup"),
        ("SYSLOG-R-MIB", "syslogOperationsGroup"),
        ("SYSLOG-R-MIB", "syslogControlGroup"))
)
if mibBuilder.loadTexts:
    syslogFullCompliance2.setStatus(
        "current"
    )

syslogReadOnlyCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 3)
)
syslogReadOnlyCompliance1.setObjects(
      *(("SYSLOG-R-MIB", "syslogNotificationGroup"),
        ("SYSLOG-R-MIB", "syslogDefaultGroup"),
        ("SYSLOG-R-MIB", "syslogOperationsGroup"),
        ("SYSLOG-R-MIB", "syslogControlGroup"))
)
if mibBuilder.loadTexts:
    syslogReadOnlyCompliance1.setStatus(
        "current"
    )

syslogReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 4)
)
syslogReadOnlyCompliance2.setObjects(
      *(("SYSLOG-R-MIB", "syslogDefaultGroup"),
        ("SYSLOG-R-MIB", "syslogOperationsGroup"),
        ("SYSLOG-R-MIB", "syslogControlGroup"))
)
if mibBuilder.loadTexts:
    syslogReadOnlyCompliance2.setStatus(
        "current"
    )

syslogNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 164, 20, 14, 3, 2, 5)
)
syslogNotificationCompliance.setObjects(
    ("SYSLOG-R-MIB", "syslogNotificationGroup")
)
if mibBuilder.loadTexts:
    syslogNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYSLOG-R-MIB",
    **{"SyslogRoles": SyslogRoles,
       "SyslogService": SyslogService,
       "SyslogEncapsulation": SyslogEncapsulation,
       "syslogMIBR": syslogMIBR,
       "syslogNotifications": syslogNotifications,
       "syslogStatusChanged": syslogStatusChanged,
       "syslogObjects": syslogObjects,
       "syslogSystem": syslogSystem,
       "syslogDefaultService": syslogDefaultService,
       "syslogDefaultEncapsulation": syslogDefaultEncapsulation,
       "syslogControlTable": syslogControlTable,
       "syslogControlEntry": syslogControlEntry,
       "syslogControlIndex": syslogControlIndex,
       "syslogControlDescr": syslogControlDescr,
       "syslogControlRoles": syslogControlRoles,
       "syslogControlBindAddrType": syslogControlBindAddrType,
       "syslogControlBindAddr": syslogControlBindAddr,
       "syslogControlService": syslogControlService,
       "syslogControlEncapsulation": syslogControlEncapsulation,
       "syslogControlMaxMessageSize": syslogControlMaxMessageSize,
       "syslogControlConfFileName": syslogControlConfFileName,
       "syslogControlStorageType": syslogControlStorageType,
       "syslogControlRowStatus": syslogControlRowStatus,
       "syslogControlAccountingType": syslogControlAccountingType,
       "syslogOperationsTable": syslogOperationsTable,
       "syslogOperationsEntry": syslogOperationsEntry,
       "syslogOperationsMsgsReceived": syslogOperationsMsgsReceived,
       "syslogOperationsMsgsTransmitted": syslogOperationsMsgsTransmitted,
       "syslogOperationsMsgsRelayed": syslogOperationsMsgsRelayed,
       "syslogOperationsMsgsDropped": syslogOperationsMsgsDropped,
       "syslogOperationsMsgsMalFormed": syslogOperationsMsgsMalFormed,
       "syslogOperationsMsgsDiscarded": syslogOperationsMsgsDiscarded,
       "syslogOperationsLastMsgRecdTime": syslogOperationsLastMsgRecdTime,
       "syslogOperationsLastMsgTransmittedTime": syslogOperationsLastMsgTransmittedTime,
       "syslogOperationsStartTime": syslogOperationsStartTime,
       "syslogOperationsLastError": syslogOperationsLastError,
       "syslogOperationsLastErrorTime": syslogOperationsLastErrorTime,
       "syslogOperationsRunIndex": syslogOperationsRunIndex,
       "syslogOperationsCounterDiscontinuityTime": syslogOperationsCounterDiscontinuityTime,
       "syslogOperationsStatus": syslogOperationsStatus,
       "syslogConformance": syslogConformance,
       "syslogGroups": syslogGroups,
       "syslogDefaultGroup": syslogDefaultGroup,
       "syslogOperationsGroup": syslogOperationsGroup,
       "syslogControlGroup": syslogControlGroup,
       "syslogNotificationGroup": syslogNotificationGroup,
       "syslogCompliances": syslogCompliances,
       "syslogFullCompliance1": syslogFullCompliance1,
       "syslogFullCompliance2": syslogFullCompliance2,
       "syslogReadOnlyCompliance1": syslogReadOnlyCompliance1,
       "syslogReadOnlyCompliance2": syslogReadOnlyCompliance2,
       "syslogNotificationCompliance": syslogNotificationCompliance}
)
