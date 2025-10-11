# SNMP MIB module (TIMETRA-PXC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-PXC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:54:47 2025
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(SdpId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "SdpId")

(LAGInterfaceNumberOrZero,
 TItemDescription,
 TmnxAdminState,
 TmnxFpeId,
 TmnxOperState,
 TmnxPortID,
 TmnxVRtrID) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "LAGInterfaceNumberOrZero",
    "TItemDescription",
    "TmnxAdminState",
    "TmnxFpeId",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxVRtrID")


# MODULE-IDENTITY

timetraPxcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 105)
)
if mibBuilder.loadTexts:
    timetraPxcMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2015-04-09 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxPxcConformance_ObjectIdentity = ObjectIdentity
tmnxPxcConformance = _TmnxPxcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105)
)
_TmnxPxcCompliances_ObjectIdentity = ObjectIdentity
tmnxPxcCompliances = _TmnxPxcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 1)
)
_TmnxPxcGroups_ObjectIdentity = ObjectIdentity
tmnxPxcGroups = _TmnxPxcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2)
)
_TmnxPxcV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxPxcV14v0Groups = _TmnxPxcV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 1)
)
_TmnxPxcV15v0Groups_ObjectIdentity = ObjectIdentity
tmnxPxcV15v0Groups = _TmnxPxcV15v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 2)
)
_TmnxPxcObjs_ObjectIdentity = ObjectIdentity
tmnxPxcObjs = _TmnxPxcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105)
)
_TmnxPxcConfigTimestamps_ObjectIdentity = ObjectIdentity
tmnxPxcConfigTimestamps = _TmnxPxcConfigTimestamps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 1)
)
_TmnxPxcTableLastChanged_Type = TimeStamp
_TmnxPxcTableLastChanged_Object = MibScalar
tmnxPxcTableLastChanged = _TmnxPxcTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 1, 1),
    _TmnxPxcTableLastChanged_Type()
)
tmnxPxcTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPxcTableLastChanged.setStatus("current")
_TmnxFpeTableLastChanged_Type = TimeStamp
_TmnxFpeTableLastChanged_Object = MibScalar
tmnxFpeTableLastChanged = _TmnxFpeTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 1, 2),
    _TmnxFpeTableLastChanged_Type()
)
tmnxFpeTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFpeTableLastChanged.setStatus("current")
_TmnxPxcConfigurations_ObjectIdentity = ObjectIdentity
tmnxPxcConfigurations = _TmnxPxcConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2)
)
_TmnxPxcTable_Object = MibTable
tmnxPxcTable = _TmnxPxcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxPxcTable.setStatus("current")
_TmnxPxcEntry_Object = MibTableRow
tmnxPxcEntry = _TmnxPxcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1)
)
tmnxPxcEntry.setIndexNames(
    (0, "TIMETRA-PXC-MIB", "tmnxPxcId"),
)
if mibBuilder.loadTexts:
    tmnxPxcEntry.setStatus("current")


class _TmnxPxcId_Type(Unsigned32):
    """Custom type tmnxPxcId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_TmnxPxcId_Type.__name__ = "Unsigned32"
_TmnxPxcId_Object = MibTableColumn
tmnxPxcId = _TmnxPxcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 1),
    _TmnxPxcId_Type()
)
tmnxPxcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxPxcId.setStatus("current")
_TmnxPxcRowStatus_Type = RowStatus
_TmnxPxcRowStatus_Object = MibTableColumn
tmnxPxcRowStatus = _TmnxPxcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 2),
    _TmnxPxcRowStatus_Type()
)
tmnxPxcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPxcRowStatus.setStatus("current")
_TmnxPxcLastChanged_Type = TimeStamp
_TmnxPxcLastChanged_Object = MibTableColumn
tmnxPxcLastChanged = _TmnxPxcLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 3),
    _TmnxPxcLastChanged_Type()
)
tmnxPxcLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPxcLastChanged.setStatus("current")


class _TmnxPxcAdminState_Type(TmnxAdminState):
    """Custom type tmnxPxcAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxPxcAdminState_Type.__name__ = "TmnxAdminState"
_TmnxPxcAdminState_Object = MibTableColumn
tmnxPxcAdminState = _TmnxPxcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 4),
    _TmnxPxcAdminState_Type()
)
tmnxPxcAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPxcAdminState.setStatus("current")
_TmnxPxcOperState_Type = TmnxOperState
_TmnxPxcOperState_Object = MibTableColumn
tmnxPxcOperState = _TmnxPxcOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 5),
    _TmnxPxcOperState_Type()
)
tmnxPxcOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxPxcOperState.setStatus("current")


class _TmnxPxcPortId_Type(TmnxPortID):
    """Custom type tmnxPxcPortId based on TmnxPortID"""
    defaultValue = 503316480


_TmnxPxcPortId_Type.__name__ = "TmnxPortID"
_TmnxPxcPortId_Object = MibTableColumn
tmnxPxcPortId = _TmnxPxcPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 6),
    _TmnxPxcPortId_Type()
)
tmnxPxcPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPxcPortId.setStatus("current")


class _TmnxPxcDescription_Type(TItemDescription):
    """Custom type tmnxPxcDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxPxcDescription_Type.__name__ = "TItemDescription"
_TmnxPxcDescription_Object = MibTableColumn
tmnxPxcDescription = _TmnxPxcDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 1, 1, 7),
    _TmnxPxcDescription_Type()
)
tmnxPxcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxPxcDescription.setStatus("current")
_TmnxFpeTable_Object = MibTable
tmnxFpeTable = _TmnxFpeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2)
)
if mibBuilder.loadTexts:
    tmnxFpeTable.setStatus("current")
_TmnxFpeEntry_Object = MibTableRow
tmnxFpeEntry = _TmnxFpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1)
)
tmnxFpeEntry.setIndexNames(
    (0, "TIMETRA-PXC-MIB", "tmnxFpeId"),
)
if mibBuilder.loadTexts:
    tmnxFpeEntry.setStatus("current")
_TmnxFpeId_Type = TmnxFpeId
_TmnxFpeId_Object = MibTableColumn
tmnxFpeId = _TmnxFpeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 1),
    _TmnxFpeId_Type()
)
tmnxFpeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxFpeId.setStatus("current")
_TmnxFpeRowStatus_Type = RowStatus
_TmnxFpeRowStatus_Object = MibTableColumn
tmnxFpeRowStatus = _TmnxFpeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 2),
    _TmnxFpeRowStatus_Type()
)
tmnxFpeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeRowStatus.setStatus("current")
_TmnxFpeLastChanged_Type = TimeStamp
_TmnxFpeLastChanged_Object = MibTableColumn
tmnxFpeLastChanged = _TmnxFpeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 3),
    _TmnxFpeLastChanged_Type()
)
tmnxFpeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFpeLastChanged.setStatus("current")


class _TmnxFpeDescription_Type(TItemDescription):
    """Custom type tmnxFpeDescription based on TItemDescription"""
    defaultHexValue = ""


_TmnxFpeDescription_Type.__name__ = "TItemDescription"
_TmnxFpeDescription_Object = MibTableColumn
tmnxFpeDescription = _TmnxFpeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 4),
    _TmnxFpeDescription_Type()
)
tmnxFpeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeDescription.setStatus("current")


class _TmnxFpePxcId_Type(Unsigned32):
    """Custom type tmnxFpePxcId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 64),
    )


_TmnxFpePxcId_Type.__name__ = "Unsigned32"
_TmnxFpePxcId_Object = MibTableColumn
tmnxFpePxcId = _TmnxFpePxcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 5),
    _TmnxFpePxcId_Type()
)
tmnxFpePxcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpePxcId.setStatus("current")


class _TmnxFpeXaLagId_Type(LAGInterfaceNumberOrZero):
    """Custom type tmnxFpeXaLagId based on LAGInterfaceNumberOrZero"""
    defaultValue = 0


_TmnxFpeXaLagId_Type.__name__ = "LAGInterfaceNumberOrZero"
_TmnxFpeXaLagId_Object = MibTableColumn
tmnxFpeXaLagId = _TmnxFpeXaLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 6),
    _TmnxFpeXaLagId_Type()
)
tmnxFpeXaLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeXaLagId.setStatus("current")


class _TmnxFpeXbLagId_Type(LAGInterfaceNumberOrZero):
    """Custom type tmnxFpeXbLagId based on LAGInterfaceNumberOrZero"""
    defaultValue = 0


_TmnxFpeXbLagId_Type.__name__ = "LAGInterfaceNumberOrZero"
_TmnxFpeXbLagId_Object = MibTableColumn
tmnxFpeXbLagId = _TmnxFpeXbLagId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 7),
    _TmnxFpeXbLagId_Type()
)
tmnxFpeXbLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeXbLagId.setStatus("current")


class _TmnxFpePwPort_Type(TruthValue):
    """Custom type tmnxFpePwPort based on TruthValue"""
    defaultValue = 2


_TmnxFpePwPort_Type.__name__ = "TruthValue"
_TmnxFpePwPort_Object = MibTableColumn
tmnxFpePwPort = _TmnxFpePwPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 8),
    _TmnxFpePwPort_Type()
)
tmnxFpePwPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpePwPort.setStatus("current")


class _TmnxFpeVxlanTermination_Type(TruthValue):
    """Custom type tmnxFpeVxlanTermination based on TruthValue"""
    defaultValue = 2


_TmnxFpeVxlanTermination_Type.__name__ = "TruthValue"
_TmnxFpeVxlanTermination_Object = MibTableColumn
tmnxFpeVxlanTermination = _TmnxFpeVxlanTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 9),
    _TmnxFpeVxlanTermination_Type()
)
tmnxFpeVxlanTermination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeVxlanTermination.setStatus("current")


class _TmnxFpeVxlanOperStatus_Type(Integer32):
    """Custom type tmnxFpeVxlanOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxFpeVxlanOperStatus_Type.__name__ = "Integer32"
_TmnxFpeVxlanOperStatus_Object = MibTableColumn
tmnxFpeVxlanOperStatus = _TmnxFpeVxlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 10),
    _TmnxFpeVxlanOperStatus_Type()
)
tmnxFpeVxlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFpeVxlanOperStatus.setStatus("current")


class _TmnxFpePwPortOperStatus_Type(Integer32):
    """Custom type tmnxFpePwPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_TmnxFpePwPortOperStatus_Type.__name__ = "Integer32"
_TmnxFpePwPortOperStatus_Object = MibTableColumn
tmnxFpePwPortOperStatus = _TmnxFpePwPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 11),
    _TmnxFpePwPortOperStatus_Type()
)
tmnxFpePwPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxFpePwPortOperStatus.setStatus("current")


class _TmnxFpeSubMgmtExtensions_Type(TruthValue):
    """Custom type tmnxFpeSubMgmtExtensions based on TruthValue"""
    defaultValue = 2


_TmnxFpeSubMgmtExtensions_Type.__name__ = "TruthValue"
_TmnxFpeSubMgmtExtensions_Object = MibTableColumn
tmnxFpeSubMgmtExtensions = _TmnxFpeSubMgmtExtensions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 12),
    _TmnxFpeSubMgmtExtensions_Type()
)
tmnxFpeSubMgmtExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeSubMgmtExtensions.setStatus("current")


class _TmnxFpeVxlanTermRouterId_Type(TmnxVRtrID):
    """Custom type tmnxFpeVxlanTermRouterId based on TmnxVRtrID"""
    defaultValue = 1


_TmnxFpeVxlanTermRouterId_Type.__name__ = "TmnxVRtrID"
_TmnxFpeVxlanTermRouterId_Object = MibTableColumn
tmnxFpeVxlanTermRouterId = _TmnxFpeVxlanTermRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 2, 1, 17),
    _TmnxFpeVxlanTermRouterId_Type()
)
tmnxFpeVxlanTermRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxFpeVxlanTermRouterId.setStatus("current")
_TmnxFpeSdpObjs_ObjectIdentity = ObjectIdentity
tmnxFpeSdpObjs = _TmnxFpeSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 3)
)


class _TmnxFpeSdpIdRngStart_Type(SdpId):
    """Custom type tmnxFpeSdpIdRngStart based on SdpId"""
    defaultValue = 0


_TmnxFpeSdpIdRngStart_Type.__name__ = "SdpId"
_TmnxFpeSdpIdRngStart_Object = MibScalar
tmnxFpeSdpIdRngStart = _TmnxFpeSdpIdRngStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 3, 1),
    _TmnxFpeSdpIdRngStart_Type()
)
tmnxFpeSdpIdRngStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFpeSdpIdRngStart.setStatus("current")


class _TmnxFpeSdpIdRngEnd_Type(SdpId):
    """Custom type tmnxFpeSdpIdRngEnd based on SdpId"""
    defaultValue = 0


_TmnxFpeSdpIdRngEnd_Type.__name__ = "SdpId"
_TmnxFpeSdpIdRngEnd_Object = MibScalar
tmnxFpeSdpIdRngEnd = _TmnxFpeSdpIdRngEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 2, 3, 2),
    _TmnxFpeSdpIdRngEnd_Type()
)
tmnxFpeSdpIdRngEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxFpeSdpIdRngEnd.setStatus("current")
_TmnxPxcStatistics_ObjectIdentity = ObjectIdentity
tmnxPxcStatistics = _TmnxPxcStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 3)
)
_TmnxPxcNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxPxcNotifyObjects = _TmnxPxcNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 105, 4)
)
_TmnxPxcNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxPxcNotifyPrefix = _TmnxPxcNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 105)
)
_TmnxPxcNotification_ObjectIdentity = ObjectIdentity
tmnxPxcNotification = _TmnxPxcNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 105, 0)
)

# Managed Objects groups

tmnxPxcV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 1, 1)
)
tmnxPxcV14v0Group.setObjects(
      *(("TIMETRA-PXC-MIB", "tmnxPxcTableLastChanged"),
        ("TIMETRA-PXC-MIB", "tmnxPxcRowStatus"),
        ("TIMETRA-PXC-MIB", "tmnxPxcLastChanged"),
        ("TIMETRA-PXC-MIB", "tmnxPxcAdminState"),
        ("TIMETRA-PXC-MIB", "tmnxPxcOperState"),
        ("TIMETRA-PXC-MIB", "tmnxPxcPortId"),
        ("TIMETRA-PXC-MIB", "tmnxPxcDescription"))
)
if mibBuilder.loadTexts:
    tmnxPxcV14v0Group.setStatus("current")

tmnxFpeV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 1, 2)
)
tmnxFpeV14v0Group.setObjects(
      *(("TIMETRA-PXC-MIB", "tmnxFpeTableLastChanged"),
        ("TIMETRA-PXC-MIB", "tmnxFpeRowStatus"),
        ("TIMETRA-PXC-MIB", "tmnxFpeLastChanged"),
        ("TIMETRA-PXC-MIB", "tmnxFpeDescription"),
        ("TIMETRA-PXC-MIB", "tmnxFpePxcId"),
        ("TIMETRA-PXC-MIB", "tmnxFpeXaLagId"),
        ("TIMETRA-PXC-MIB", "tmnxFpeXbLagId"),
        ("TIMETRA-PXC-MIB", "tmnxFpeSdpIdRngStart"),
        ("TIMETRA-PXC-MIB", "tmnxFpeSdpIdRngEnd"))
)
if mibBuilder.loadTexts:
    tmnxFpeV14v0Group.setStatus("current")

tmnxFpePwPortV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 1, 3)
)
tmnxFpePwPortV14v0Group.setObjects(
      *(("TIMETRA-PXC-MIB", "tmnxFpePwPort"),
        ("TIMETRA-PXC-MIB", "tmnxFpePwPortOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxFpePwPortV14v0Group.setStatus("current")

tmnxFpeVxlanV14v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 1, 4)
)
tmnxFpeVxlanV14v0Group.setObjects(
      *(("TIMETRA-PXC-MIB", "tmnxFpeVxlanTermination"),
        ("TIMETRA-PXC-MIB", "tmnxFpeVxlanOperStatus"))
)
if mibBuilder.loadTexts:
    tmnxFpeVxlanV14v0Group.setStatus("current")

tmnxFpeVxlanV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 1, 5)
)
tmnxFpeVxlanV15v0Group.setObjects(
    ("TIMETRA-PXC-MIB", "tmnxFpeVxlanTermRouterId")
)
if mibBuilder.loadTexts:
    tmnxFpeVxlanV15v0Group.setStatus("current")

tmnxFpeV15v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 2, 2, 1)
)
tmnxFpeV15v0Group.setObjects(
    ("TIMETRA-PXC-MIB", "tmnxFpeSubMgmtExtensions")
)
if mibBuilder.loadTexts:
    tmnxFpeV15v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxPxcComplianceV14v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 1, 1)
)
tmnxPxcComplianceV14v0.setObjects(
      *(("TIMETRA-PXC-MIB", "tmnxPxcV14v0Group"),
        ("TIMETRA-PXC-MIB", "tmnxFpeV14v0Group"),
        ("TIMETRA-PXC-MIB", "tmnxFpePwPortV14v0Group"),
        ("TIMETRA-PXC-MIB", "tmnxFpeVxlanV14v0Group"),
        ("TIMETRA-PXC-MIB", "tmnxFpeV15v0Group"))
)
if mibBuilder.loadTexts:
    tmnxPxcComplianceV14v0.setStatus(
        "current"
    )

tmnxPxcComplianceV15v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 105, 1, 2)
)
tmnxPxcComplianceV15v0.setObjects(
    ("TIMETRA-PXC-MIB", "tmnxFpeVxlanV15v0Group")
)
if mibBuilder.loadTexts:
    tmnxPxcComplianceV15v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-PXC-MIB",
    **{"timetraPxcMIBModule": timetraPxcMIBModule,
       "tmnxPxcConformance": tmnxPxcConformance,
       "tmnxPxcCompliances": tmnxPxcCompliances,
       "tmnxPxcComplianceV14v0": tmnxPxcComplianceV14v0,
       "tmnxPxcComplianceV15v0": tmnxPxcComplianceV15v0,
       "tmnxPxcGroups": tmnxPxcGroups,
       "tmnxPxcV14v0Groups": tmnxPxcV14v0Groups,
       "tmnxPxcV14v0Group": tmnxPxcV14v0Group,
       "tmnxFpeV14v0Group": tmnxFpeV14v0Group,
       "tmnxFpePwPortV14v0Group": tmnxFpePwPortV14v0Group,
       "tmnxFpeVxlanV14v0Group": tmnxFpeVxlanV14v0Group,
       "tmnxFpeVxlanV15v0Group": tmnxFpeVxlanV15v0Group,
       "tmnxPxcV15v0Groups": tmnxPxcV15v0Groups,
       "tmnxFpeV15v0Group": tmnxFpeV15v0Group,
       "tmnxPxcObjs": tmnxPxcObjs,
       "tmnxPxcConfigTimestamps": tmnxPxcConfigTimestamps,
       "tmnxPxcTableLastChanged": tmnxPxcTableLastChanged,
       "tmnxFpeTableLastChanged": tmnxFpeTableLastChanged,
       "tmnxPxcConfigurations": tmnxPxcConfigurations,
       "tmnxPxcTable": tmnxPxcTable,
       "tmnxPxcEntry": tmnxPxcEntry,
       "tmnxPxcId": tmnxPxcId,
       "tmnxPxcRowStatus": tmnxPxcRowStatus,
       "tmnxPxcLastChanged": tmnxPxcLastChanged,
       "tmnxPxcAdminState": tmnxPxcAdminState,
       "tmnxPxcOperState": tmnxPxcOperState,
       "tmnxPxcPortId": tmnxPxcPortId,
       "tmnxPxcDescription": tmnxPxcDescription,
       "tmnxFpeTable": tmnxFpeTable,
       "tmnxFpeEntry": tmnxFpeEntry,
       "tmnxFpeId": tmnxFpeId,
       "tmnxFpeRowStatus": tmnxFpeRowStatus,
       "tmnxFpeLastChanged": tmnxFpeLastChanged,
       "tmnxFpeDescription": tmnxFpeDescription,
       "tmnxFpePxcId": tmnxFpePxcId,
       "tmnxFpeXaLagId": tmnxFpeXaLagId,
       "tmnxFpeXbLagId": tmnxFpeXbLagId,
       "tmnxFpePwPort": tmnxFpePwPort,
       "tmnxFpeVxlanTermination": tmnxFpeVxlanTermination,
       "tmnxFpeVxlanOperStatus": tmnxFpeVxlanOperStatus,
       "tmnxFpePwPortOperStatus": tmnxFpePwPortOperStatus,
       "tmnxFpeSubMgmtExtensions": tmnxFpeSubMgmtExtensions,
       "tmnxFpeVxlanTermRouterId": tmnxFpeVxlanTermRouterId,
       "tmnxFpeSdpObjs": tmnxFpeSdpObjs,
       "tmnxFpeSdpIdRngStart": tmnxFpeSdpIdRngStart,
       "tmnxFpeSdpIdRngEnd": tmnxFpeSdpIdRngEnd,
       "tmnxPxcStatistics": tmnxPxcStatistics,
       "tmnxPxcNotifyObjects": tmnxPxcNotifyObjects,
       "tmnxPxcNotifyPrefix": tmnxPxcNotifyPrefix,
       "tmnxPxcNotification": tmnxPxcNotification}
)
