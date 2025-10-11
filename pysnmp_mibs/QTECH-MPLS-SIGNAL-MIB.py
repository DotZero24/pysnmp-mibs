# SNMP MIB module (QTECH-MPLS-SIGNAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-MPLS-SIGNAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:40 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus")

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

qtechMplsSignalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98)
)
if mibBuilder.loadTexts:
    qtechMplsSignalMIB.setRevisions(
        ("2011-05-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechMplsSignalMIBObjects_ObjectIdentity = ObjectIdentity
qtechMplsSignalMIBObjects = _QtechMplsSignalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1)
)
_QtechMplsSignalObjects_ObjectIdentity = ObjectIdentity
qtechMplsSignalObjects = _QtechMplsSignalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1)
)
_QtechMplsSignalmplsGernalMibObjects_ObjectIdentity = ObjectIdentity
qtechMplsSignalmplsGernalMibObjects = _QtechMplsSignalmplsGernalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 1)
)
_QtechMplsVersion_Type = Unsigned32
_QtechMplsVersion_Object = MibScalar
qtechMplsVersion = _QtechMplsVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 1, 1),
    _QtechMplsVersion_Type()
)
qtechMplsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMplsVersion.setStatus("current")


class _QtechMPLSSignal_Type(Integer32):
    """Custom type qtechMPLSSignal based on Integer32"""
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


_QtechMPLSSignal_Type.__name__ = "Integer32"
_QtechMPLSSignal_Object = MibScalar
qtechMPLSSignal = _QtechMPLSSignal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 1, 2),
    _QtechMPLSSignal_Type()
)
qtechMPLSSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSSignal.setStatus("current")
_QtechMPLSTESignal_Type = TruthValue
_QtechMPLSTESignal_Object = MibScalar
qtechMPLSTESignal = _QtechMPLSTESignal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 1, 3),
    _QtechMPLSTESignal_Type()
)
qtechMPLSTESignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSTESignal.setStatus("current")
_QtechMplsSignalConfigMibObjects_ObjectIdentity = ObjectIdentity
qtechMplsSignalConfigMibObjects = _QtechMplsSignalConfigMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 2)
)
_QtechMPLSConfigLspNum_Type = Unsigned32
_QtechMPLSConfigLspNum_Object = MibScalar
qtechMPLSConfigLspNum = _QtechMPLSConfigLspNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 2, 1),
    _QtechMPLSConfigLspNum_Type()
)
qtechMPLSConfigLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSConfigLspNum.setStatus("current")
_QtechMPLSActiveLspNum_Type = Unsigned32
_QtechMPLSActiveLspNum_Object = MibScalar
qtechMPLSActiveLspNum = _QtechMPLSActiveLspNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 2, 2),
    _QtechMPLSActiveLspNum_Type()
)
qtechMPLSActiveLspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSActiveLspNum.setStatus("current")
_QtechMPLSAdministrativeGroupTable_Object = MibTable
qtechMPLSAdministrativeGroupTable = _QtechMPLSAdministrativeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qtechMPLSAdministrativeGroupTable.setStatus("current")
_QtechMPLSAdministrativeGroupEntry_Object = MibTableRow
qtechMPLSAdministrativeGroupEntry = _QtechMPLSAdministrativeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1)
)
qtechMPLSAdministrativeGroupEntry.setIndexNames(
    (0, "QTECH-MPLS-SIGNAL-MIB", "qtechMPLSFecIndex"),
)
if mibBuilder.loadTexts:
    qtechMPLSAdministrativeGroupEntry.setStatus("current")
_QtechMPLSFecIndex_Type = Integer32
_QtechMPLSFecIndex_Object = MibTableColumn
qtechMPLSFecIndex = _QtechMPLSFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 1),
    _QtechMPLSFecIndex_Type()
)
qtechMPLSFecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechMPLSFecIndex.setStatus("current")
_QtechMPLSLSPName_Type = DisplayString
_QtechMPLSLSPName_Object = MibTableColumn
qtechMPLSLSPName = _QtechMPLSLSPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 2),
    _QtechMPLSLSPName_Type()
)
qtechMPLSLSPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPName.setStatus("current")


class _QtechMPLSLSPStates_Type(Integer32):
    """Custom type qtechMPLSLSPStates based on Integer32"""
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


_QtechMPLSLSPStates_Type.__name__ = "Integer32"
_QtechMPLSLSPStates_Object = MibTableColumn
qtechMPLSLSPStates = _QtechMPLSLSPStates_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 3),
    _QtechMPLSLSPStates_Type()
)
qtechMPLSLSPStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPStates.setStatus("current")
_QtechMPLSLSPForwardBytes_Type = Integer32
_QtechMPLSLSPForwardBytes_Object = MibTableColumn
qtechMPLSLSPForwardBytes = _QtechMPLSLSPForwardBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 4),
    _QtechMPLSLSPForwardBytes_Type()
)
qtechMPLSLSPForwardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPForwardBytes.setStatus("current")
_QtechMPLSLSPForwardPackets_Type = Integer32
_QtechMPLSLSPForwardPackets_Object = MibTableColumn
qtechMPLSLSPForwardPackets = _QtechMPLSLSPForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 5),
    _QtechMPLSLSPForwardPackets_Type()
)
qtechMPLSLSPForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPForwardPackets.setStatus("current")
_QtechMPLSLSPActiveTime_Type = TimeStamp
_QtechMPLSLSPActiveTime_Object = MibTableColumn
qtechMPLSLSPActiveTime = _QtechMPLSLSPActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 6),
    _QtechMPLSLSPActiveTime_Type()
)
qtechMPLSLSPActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPActiveTime.setStatus("current")
_QtechMPLSLSPCreationTime_Type = TimeStamp
_QtechMPLSLSPCreationTime_Object = MibTableColumn
qtechMPLSLSPCreationTime = _QtechMPLSLSPCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 7),
    _QtechMPLSLSPCreationTime_Type()
)
qtechMPLSLSPCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPCreationTime.setStatus("current")
_QtechMPLSLSPPrimaryCreationTime_Type = TimeStamp
_QtechMPLSLSPPrimaryCreationTime_Object = MibTableColumn
qtechMPLSLSPPrimaryCreationTime = _QtechMPLSLSPPrimaryCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 8),
    _QtechMPLSLSPPrimaryCreationTime_Type()
)
qtechMPLSLSPPrimaryCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPPrimaryCreationTime.setStatus("current")
_QtechMPLSLSPSwitchTimes_Type = Integer32
_QtechMPLSLSPSwitchTimes_Object = MibTableColumn
qtechMPLSLSPSwitchTimes = _QtechMPLSLSPSwitchTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 9),
    _QtechMPLSLSPSwitchTimes_Type()
)
qtechMPLSLSPSwitchTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPSwitchTimes.setStatus("current")
_QtechMPLSLSPLatestSwitchTime_Type = TimeStamp
_QtechMPLSLSPLatestSwitchTime_Object = MibTableColumn
qtechMPLSLSPLatestSwitchTime = _QtechMPLSLSPLatestSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 10),
    _QtechMPLSLSPLatestSwitchTime_Type()
)
qtechMPLSLSPLatestSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPLatestSwitchTime.setStatus("current")
_QtechMPLSLSPPathchangeTime_Type = TimeStamp
_QtechMPLSLSPPathchangeTime_Object = MibTableColumn
qtechMPLSLSPPathchangeTime = _QtechMPLSLSPPathchangeTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 11),
    _QtechMPLSLSPPathchangeTime_Type()
)
qtechMPLSLSPPathchangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPPathchangeTime.setStatus("current")
_QtechMPLSLSPConfigChangeTime_Type = TimeStamp
_QtechMPLSLSPConfigChangeTime_Object = MibTableColumn
qtechMPLSLSPConfigChangeTime = _QtechMPLSLSPConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 12),
    _QtechMPLSLSPConfigChangeTime_Type()
)
qtechMPLSLSPConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPConfigChangeTime.setStatus("current")
_QtechMPLSLSPBackupPath_Type = DisplayString
_QtechMPLSLSPBackupPath_Object = MibTableColumn
qtechMPLSLSPBackupPath = _QtechMPLSLSPBackupPath_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 13),
    _QtechMPLSLSPBackupPath_Type()
)
qtechMPLSLSPBackupPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPBackupPath.setStatus("current")


class _QtechMPLSLSPOperationPath_Type(Integer32):
    """Custom type qtechMPLSLSPOperationPath based on Integer32"""
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


_QtechMPLSLSPOperationPath_Type.__name__ = "Integer32"
_QtechMPLSLSPOperationPath_Object = MibTableColumn
qtechMPLSLSPOperationPath = _QtechMPLSLSPOperationPath_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 14),
    _QtechMPLSLSPOperationPath_Type()
)
qtechMPLSLSPOperationPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPOperationPath.setStatus("current")
_QtechMPLSLSPIngress_Type = InetAddressType
_QtechMPLSLSPIngress_Object = MibTableColumn
qtechMPLSLSPIngress = _QtechMPLSLSPIngress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 15),
    _QtechMPLSLSPIngress_Type()
)
qtechMPLSLSPIngress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPIngress.setStatus("current")
_QtechMPLSLSPDestination_Type = InetAddressType
_QtechMPLSLSPDestination_Object = MibTableColumn
qtechMPLSLSPDestination = _QtechMPLSLSPDestination_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 16),
    _QtechMPLSLSPDestination_Type()
)
qtechMPLSLSPDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPDestination.setStatus("current")
_QtechMPLSLSPAdministrativeGroupName_Type = DisplayString
_QtechMPLSLSPAdministrativeGroupName_Object = MibTableColumn
qtechMPLSLSPAdministrativeGroupName = _QtechMPLSLSPAdministrativeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 1, 3, 1, 17),
    _QtechMPLSLSPAdministrativeGroupName_Type()
)
qtechMPLSLSPAdministrativeGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMPLSLSPAdministrativeGroupName.setStatus("current")
_QtechMplsSignalConformance_ObjectIdentity = ObjectIdentity
qtechMplsSignalConformance = _QtechMplsSignalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 98, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-MPLS-SIGNAL-MIB",
    **{"qtechMplsSignalMIB": qtechMplsSignalMIB,
       "qtechMplsSignalMIBObjects": qtechMplsSignalMIBObjects,
       "qtechMplsSignalObjects": qtechMplsSignalObjects,
       "qtechMplsSignalmplsGernalMibObjects": qtechMplsSignalmplsGernalMibObjects,
       "qtechMplsVersion": qtechMplsVersion,
       "qtechMPLSSignal": qtechMPLSSignal,
       "qtechMPLSTESignal": qtechMPLSTESignal,
       "qtechMplsSignalConfigMibObjects": qtechMplsSignalConfigMibObjects,
       "qtechMPLSConfigLspNum": qtechMPLSConfigLspNum,
       "qtechMPLSActiveLspNum": qtechMPLSActiveLspNum,
       "qtechMPLSAdministrativeGroupTable": qtechMPLSAdministrativeGroupTable,
       "qtechMPLSAdministrativeGroupEntry": qtechMPLSAdministrativeGroupEntry,
       "qtechMPLSFecIndex": qtechMPLSFecIndex,
       "qtechMPLSLSPName": qtechMPLSLSPName,
       "qtechMPLSLSPStates": qtechMPLSLSPStates,
       "qtechMPLSLSPForwardBytes": qtechMPLSLSPForwardBytes,
       "qtechMPLSLSPForwardPackets": qtechMPLSLSPForwardPackets,
       "qtechMPLSLSPActiveTime": qtechMPLSLSPActiveTime,
       "qtechMPLSLSPCreationTime": qtechMPLSLSPCreationTime,
       "qtechMPLSLSPPrimaryCreationTime": qtechMPLSLSPPrimaryCreationTime,
       "qtechMPLSLSPSwitchTimes": qtechMPLSLSPSwitchTimes,
       "qtechMPLSLSPLatestSwitchTime": qtechMPLSLSPLatestSwitchTime,
       "qtechMPLSLSPPathchangeTime": qtechMPLSLSPPathchangeTime,
       "qtechMPLSLSPConfigChangeTime": qtechMPLSLSPConfigChangeTime,
       "qtechMPLSLSPBackupPath": qtechMPLSLSPBackupPath,
       "qtechMPLSLSPOperationPath": qtechMPLSLSPOperationPath,
       "qtechMPLSLSPIngress": qtechMPLSLSPIngress,
       "qtechMPLSLSPDestination": qtechMPLSLSPDestination,
       "qtechMPLSLSPAdministrativeGroupName": qtechMPLSLSPAdministrativeGroupName,
       "qtechMplsSignalConformance": qtechMplsSignalConformance}
)
