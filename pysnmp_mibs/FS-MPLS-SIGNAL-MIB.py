# SNMP MIB module (FS-MPLS-SIGNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-MPLS-SIGNAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:17 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 PositiveInteger,
 RouterID,
 Status) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "PositiveInteger",
    "RouterID",
    "Status")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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


# MODULE-IDENTITY

fsMplsSignalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98)
)
if mibBuilder.loadTexts:
    fsMplsSignalMIB.setRevisions(
        ("2011-05-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsSignalMIBObjects_ObjectIdentity = ObjectIdentity
fsMplsSignalMIBObjects = _FsMplsSignalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1)
)
_FsMplsSignalObjects_ObjectIdentity = ObjectIdentity
fsMplsSignalObjects = _FsMplsSignalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1)
)
_FsMplsSignalmplsGernalMibObjects_ObjectIdentity = ObjectIdentity
fsMplsSignalmplsGernalMibObjects = _FsMplsSignalmplsGernalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 1)
)
_FsMplsVersion_Type = Unsigned32
_FsMplsVersion_Object = MibScalar
fsMplsVersion = _FsMplsVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 1, 1),
    _FsMplsVersion_Type()
)
fsMplsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsVersion.setStatus("current")


class _FsMPLSSignal_Type(Integer32):
    """Custom type fsMPLSSignal based on Integer32"""
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
        *(("ldp", 1),
          ("rsvp-te", 2),
          ("cr-ldp", 3),
          ("other", 4))
    )


_FsMPLSSignal_Type.__name__ = "Integer32"
_FsMPLSSignal_Object = MibScalar
fsMPLSSignal = _FsMPLSSignal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 1, 2),
    _FsMPLSSignal_Type()
)
fsMPLSSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSSignal.setStatus("current")
_FsMPLSTESignal_Type = TruthValue
_FsMPLSTESignal_Object = MibScalar
fsMPLSTESignal = _FsMPLSTESignal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 1, 3),
    _FsMPLSTESignal_Type()
)
fsMPLSTESignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSTESignal.setStatus("current")
_FsMplsSignalConfigMibObjects_ObjectIdentity = ObjectIdentity
fsMplsSignalConfigMibObjects = _FsMplsSignalConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 2)
)
_FsMPLSConfigLspNum_Type = Unsigned32
_FsMPLSConfigLspNum_Object = MibScalar
fsMPLSConfigLspNum = _FsMPLSConfigLspNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 2, 1),
    _FsMPLSConfigLspNum_Type()
)
fsMPLSConfigLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSConfigLspNum.setStatus("current")
_FsMPLSActiveLspNum_Type = Unsigned32
_FsMPLSActiveLspNum_Object = MibScalar
fsMPLSActiveLspNum = _FsMPLSActiveLspNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 2, 2),
    _FsMPLSActiveLspNum_Type()
)
fsMPLSActiveLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSActiveLspNum.setStatus("current")
_FsMPLSAdministrativeGroupTable_Object = MibTable
fsMPLSAdministrativeGroupTable = _FsMPLSAdministrativeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsMPLSAdministrativeGroupTable.setStatus("current")
_FsMPLSAdministrativeGroupEntry_Object = MibTableRow
fsMPLSAdministrativeGroupEntry = _FsMPLSAdministrativeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1)
)
fsMPLSAdministrativeGroupEntry.setIndexNames(
    (0, "FS-MPLS-SIGNAL-MIB", "fsMPLSFecIndex"),
)
if mibBuilder.loadTexts:
    fsMPLSAdministrativeGroupEntry.setStatus("current")
_FsMPLSFecIndex_Type = Integer32
_FsMPLSFecIndex_Object = MibTableColumn
fsMPLSFecIndex = _FsMPLSFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 1),
    _FsMPLSFecIndex_Type()
)
fsMPLSFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMPLSFecIndex.setStatus("current")
_FsMPLSLSPName_Type = DisplayString
_FsMPLSLSPName_Object = MibTableColumn
fsMPLSLSPName = _FsMPLSLSPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 2),
    _FsMPLSLSPName_Type()
)
fsMPLSLSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPName.setStatus("current")


class _FsMPLSLSPStates_Type(Integer32):
    """Custom type fsMPLSLSPStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_FsMPLSLSPStates_Type.__name__ = "Integer32"
_FsMPLSLSPStates_Object = MibTableColumn
fsMPLSLSPStates = _FsMPLSLSPStates_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 3),
    _FsMPLSLSPStates_Type()
)
fsMPLSLSPStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPStates.setStatus("current")
_FsMPLSLSPForwardBytes_Type = Integer32
_FsMPLSLSPForwardBytes_Object = MibTableColumn
fsMPLSLSPForwardBytes = _FsMPLSLSPForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 4),
    _FsMPLSLSPForwardBytes_Type()
)
fsMPLSLSPForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPForwardBytes.setStatus("current")
_FsMPLSLSPForwardPackets_Type = Integer32
_FsMPLSLSPForwardPackets_Object = MibTableColumn
fsMPLSLSPForwardPackets = _FsMPLSLSPForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 5),
    _FsMPLSLSPForwardPackets_Type()
)
fsMPLSLSPForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPForwardPackets.setStatus("current")
_FsMPLSLSPActiveTime_Type = TimeStamp
_FsMPLSLSPActiveTime_Object = MibTableColumn
fsMPLSLSPActiveTime = _FsMPLSLSPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 6),
    _FsMPLSLSPActiveTime_Type()
)
fsMPLSLSPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPActiveTime.setStatus("current")
_FsMPLSLSPCreationTime_Type = TimeStamp
_FsMPLSLSPCreationTime_Object = MibTableColumn
fsMPLSLSPCreationTime = _FsMPLSLSPCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 7),
    _FsMPLSLSPCreationTime_Type()
)
fsMPLSLSPCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPCreationTime.setStatus("current")
_FsMPLSLSPPrimaryCreationTime_Type = TimeStamp
_FsMPLSLSPPrimaryCreationTime_Object = MibTableColumn
fsMPLSLSPPrimaryCreationTime = _FsMPLSLSPPrimaryCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 8),
    _FsMPLSLSPPrimaryCreationTime_Type()
)
fsMPLSLSPPrimaryCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPPrimaryCreationTime.setStatus("current")
_FsMPLSLSPSwitchTimes_Type = Integer32
_FsMPLSLSPSwitchTimes_Object = MibTableColumn
fsMPLSLSPSwitchTimes = _FsMPLSLSPSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 9),
    _FsMPLSLSPSwitchTimes_Type()
)
fsMPLSLSPSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPSwitchTimes.setStatus("current")
_FsMPLSLSPLatestSwitchTime_Type = TimeStamp
_FsMPLSLSPLatestSwitchTime_Object = MibTableColumn
fsMPLSLSPLatestSwitchTime = _FsMPLSLSPLatestSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 10),
    _FsMPLSLSPLatestSwitchTime_Type()
)
fsMPLSLSPLatestSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPLatestSwitchTime.setStatus("current")
_FsMPLSLSPPathchangeTime_Type = TimeStamp
_FsMPLSLSPPathchangeTime_Object = MibTableColumn
fsMPLSLSPPathchangeTime = _FsMPLSLSPPathchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 11),
    _FsMPLSLSPPathchangeTime_Type()
)
fsMPLSLSPPathchangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPPathchangeTime.setStatus("current")
_FsMPLSLSPConfigChangeTime_Type = TimeStamp
_FsMPLSLSPConfigChangeTime_Object = MibTableColumn
fsMPLSLSPConfigChangeTime = _FsMPLSLSPConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 12),
    _FsMPLSLSPConfigChangeTime_Type()
)
fsMPLSLSPConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPConfigChangeTime.setStatus("current")
_FsMPLSLSPBackupPath_Type = DisplayString
_FsMPLSLSPBackupPath_Object = MibTableColumn
fsMPLSLSPBackupPath = _FsMPLSLSPBackupPath_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 13),
    _FsMPLSLSPBackupPath_Type()
)
fsMPLSLSPBackupPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPBackupPath.setStatus("current")


class _FsMPLSLSPOperationPath_Type(Integer32):
    """Custom type fsMPLSLSPOperationPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2),
          ("none", 3))
    )


_FsMPLSLSPOperationPath_Type.__name__ = "Integer32"
_FsMPLSLSPOperationPath_Object = MibTableColumn
fsMPLSLSPOperationPath = _FsMPLSLSPOperationPath_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 14),
    _FsMPLSLSPOperationPath_Type()
)
fsMPLSLSPOperationPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPOperationPath.setStatus("current")
_FsMPLSLSPIngress_Type = InetAddressType
_FsMPLSLSPIngress_Object = MibTableColumn
fsMPLSLSPIngress = _FsMPLSLSPIngress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 15),
    _FsMPLSLSPIngress_Type()
)
fsMPLSLSPIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPIngress.setStatus("current")
_FsMPLSLSPDestination_Type = InetAddressType
_FsMPLSLSPDestination_Object = MibTableColumn
fsMPLSLSPDestination = _FsMPLSLSPDestination_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 16),
    _FsMPLSLSPDestination_Type()
)
fsMPLSLSPDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPDestination.setStatus("current")
_FsMPLSLSPAdministrativeGroupName_Type = DisplayString
_FsMPLSLSPAdministrativeGroupName_Object = MibTableColumn
fsMPLSLSPAdministrativeGroupName = _FsMPLSLSPAdministrativeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 1, 3, 1, 17),
    _FsMPLSLSPAdministrativeGroupName_Type()
)
fsMPLSLSPAdministrativeGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMPLSLSPAdministrativeGroupName.setStatus("current")
_FsMplsSignalConformance_ObjectIdentity = ObjectIdentity
fsMplsSignalConformance = _FsMplsSignalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 98, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-MPLS-SIGNAL-MIB",
    **{"fsMplsSignalMIB": fsMplsSignalMIB,
       "fsMplsSignalMIBObjects": fsMplsSignalMIBObjects,
       "fsMplsSignalObjects": fsMplsSignalObjects,
       "fsMplsSignalmplsGernalMibObjects": fsMplsSignalmplsGernalMibObjects,
       "fsMplsVersion": fsMplsVersion,
       "fsMPLSSignal": fsMPLSSignal,
       "fsMPLSTESignal": fsMPLSTESignal,
       "fsMplsSignalConfigMibObjects": fsMplsSignalConfigMibObjects,
       "fsMPLSConfigLspNum": fsMPLSConfigLspNum,
       "fsMPLSActiveLspNum": fsMPLSActiveLspNum,
       "fsMPLSAdministrativeGroupTable": fsMPLSAdministrativeGroupTable,
       "fsMPLSAdministrativeGroupEntry": fsMPLSAdministrativeGroupEntry,
       "fsMPLSFecIndex": fsMPLSFecIndex,
       "fsMPLSLSPName": fsMPLSLSPName,
       "fsMPLSLSPStates": fsMPLSLSPStates,
       "fsMPLSLSPForwardBytes": fsMPLSLSPForwardBytes,
       "fsMPLSLSPForwardPackets": fsMPLSLSPForwardPackets,
       "fsMPLSLSPActiveTime": fsMPLSLSPActiveTime,
       "fsMPLSLSPCreationTime": fsMPLSLSPCreationTime,
       "fsMPLSLSPPrimaryCreationTime": fsMPLSLSPPrimaryCreationTime,
       "fsMPLSLSPSwitchTimes": fsMPLSLSPSwitchTimes,
       "fsMPLSLSPLatestSwitchTime": fsMPLSLSPLatestSwitchTime,
       "fsMPLSLSPPathchangeTime": fsMPLSLSPPathchangeTime,
       "fsMPLSLSPConfigChangeTime": fsMPLSLSPConfigChangeTime,
       "fsMPLSLSPBackupPath": fsMPLSLSPBackupPath,
       "fsMPLSLSPOperationPath": fsMPLSLSPOperationPath,
       "fsMPLSLSPIngress": fsMPLSLSPIngress,
       "fsMPLSLSPDestination": fsMPLSLSPDestination,
       "fsMPLSLSPAdministrativeGroupName": fsMPLSLSPAdministrativeGroupName,
       "fsMplsSignalConformance": fsMplsSignalConformance}
)
