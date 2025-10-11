# SNMP MIB module (LUM-WDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-WDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:46 2025
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

(lumModules,
 lumWdmMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumWdmMIB")

(AdminStatusWithNA,
 BerLevel,
 BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 EnabledDisabledWithNA,
 FaultStatus,
 LambdaFrequency,
 LambdaType,
 MgmtNameString,
 ObjectProperty,
 OperStatusWithNA,
 PortNumber,
 PortType,
 ResetWithNA,
 SignalFormat,
 Signed32WithNA,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatusWithNA",
    "BerLevel",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "EnabledDisabledWithNA",
    "FaultStatus",
    "LambdaFrequency",
    "LambdaType",
    "MgmtNameString",
    "ObjectProperty",
    "OperStatusWithNA",
    "PortNumber",
    "PortType",
    "ResetWithNA",
    "SignalFormat",
    "Signed32WithNA",
    "SlotNumber",
    "SubrackNumber")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

lumWdmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lumWdmMIBModule.setRevisions(
        ("2018-04-24 00:00",
         "2017-12-15 00:00",
         "2017-06-22 00:00",
         "2017-04-17 00:00",
         "2016-11-30 00:00",
         "2016-07-29 00:00",
         "2016-01-11 00:00",
         "2015-11-30 00:00",
         "2014-08-15 00:00",
         "2014-05-16 00:00",
         "2013-09-26 00:00",
         "2013-05-01 00:00",
         "2012-12-20 00:00",
         "2012-09-21 00:00",
         "2012-03-30 00:00",
         "2011-12-20 00:00",
         "2011-04-12 00:00",
         "2006-01-27 00:00",
         "2005-09-26 00:00",
         "2005-07-07 00:00",
         "2002-12-04 00:00",
         "2002-05-31 00:00",
         "2002-05-16 00:00",
         "2002-05-15 00:00",
         "2002-02-20 00:00",
         "2002-02-01 00:00",
         "2002-01-24 00:00",
         "2002-01-17 00:00",
         "2002-01-16 00:00",
         "2002-01-09 00:00",
         "2001-12-03 00:00",
         "2001-11-22 00:00",
         "2001-11-09 00:00",
         "2001-10-30 00:00",
         "2001-10-23 00:00",
         "2001-10-10 00:00",
         "2001-09-05 00:00",
         "2001-09-04 00:00",
         "2001-08-24 00:00",
         "2001-08-14 00:00",
         "2001-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumWdmConfs_ObjectIdentity = ObjectIdentity
lumWdmConfs = _LumWdmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1)
)
_LumWdmGroups_ObjectIdentity = ObjectIdentity
lumWdmGroups = _LumWdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1)
)
_LumWdmCompl_ObjectIdentity = ObjectIdentity
lumWdmCompl = _LumWdmCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2)
)
_LumWdmMinimalGroups_ObjectIdentity = ObjectIdentity
lumWdmMinimalGroups = _LumWdmMinimalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 3)
)
_LumWdmMinimalCompl_ObjectIdentity = ObjectIdentity
lumWdmMinimalCompl = _LumWdmMinimalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 4)
)
_LumWdmMIBObjects_ObjectIdentity = ObjectIdentity
lumWdmMIBObjects = _LumWdmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2)
)
_WdmGeneral_ObjectIdentity = ObjectIdentity
wdmGeneral = _WdmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1)
)
_WdmGeneralTestAndIncr_Type = TestAndIncr
_WdmGeneralTestAndIncr_Object = MibScalar
wdmGeneralTestAndIncr = _WdmGeneralTestAndIncr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 1),
    _WdmGeneralTestAndIncr_Type()
)
wdmGeneralTestAndIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmGeneralTestAndIncr.setStatus("current")


class _WdmGeneralMibSpecVersion_Type(DisplayString):
    """Custom type wdmGeneralMibSpecVersion based on DisplayString"""
    defaultValue = OctetString("")


_WdmGeneralMibSpecVersion_Type.__name__ = "DisplayString"
_WdmGeneralMibSpecVersion_Object = MibScalar
wdmGeneralMibSpecVersion = _WdmGeneralMibSpecVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 2),
    _WdmGeneralMibSpecVersion_Type()
)
wdmGeneralMibSpecVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmGeneralMibSpecVersion.setStatus("current")


class _WdmGeneralMibImplVersion_Type(DisplayString):
    """Custom type wdmGeneralMibImplVersion based on DisplayString"""
    defaultValue = OctetString("")


_WdmGeneralMibImplVersion_Type.__name__ = "DisplayString"
_WdmGeneralMibImplVersion_Object = MibScalar
wdmGeneralMibImplVersion = _WdmGeneralMibImplVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 3),
    _WdmGeneralMibImplVersion_Type()
)
wdmGeneralMibImplVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmGeneralMibImplVersion.setStatus("current")
_WdmGeneralLastChangeTime_Type = DateAndTime
_WdmGeneralLastChangeTime_Object = MibScalar
wdmGeneralLastChangeTime = _WdmGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 4),
    _WdmGeneralLastChangeTime_Type()
)
wdmGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralLastChangeTime.setStatus("current")
_WdmGeneralStateLastChangeTime_Type = DateAndTime
_WdmGeneralStateLastChangeTime_Object = MibScalar
wdmGeneralStateLastChangeTime = _WdmGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 5),
    _WdmGeneralStateLastChangeTime_Type()
)
wdmGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralStateLastChangeTime.setStatus("current")
_WdmGeneralWdmIfTableSize_Type = Unsigned32
_WdmGeneralWdmIfTableSize_Object = MibScalar
wdmGeneralWdmIfTableSize = _WdmGeneralWdmIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 6),
    _WdmGeneralWdmIfTableSize_Type()
)
wdmGeneralWdmIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmIfTableSize.setStatus("current")
_WdmGeneralWdmPassiveIfTableSize_Type = Unsigned32
_WdmGeneralWdmPassiveIfTableSize_Object = MibScalar
wdmGeneralWdmPassiveIfTableSize = _WdmGeneralWdmPassiveIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 7),
    _WdmGeneralWdmPassiveIfTableSize_Type()
)
wdmGeneralWdmPassiveIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmPassiveIfTableSize.setStatus("current")
_WdmGeneralWdmProtTableSize_Type = Unsigned32
_WdmGeneralWdmProtTableSize_Object = MibScalar
wdmGeneralWdmProtTableSize = _WdmGeneralWdmProtTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 8),
    _WdmGeneralWdmProtTableSize_Type()
)
wdmGeneralWdmProtTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmProtTableSize.setStatus("current")
_WdmGeneralWdmVc4TableSize_Type = Unsigned32
_WdmGeneralWdmVc4TableSize_Object = MibScalar
wdmGeneralWdmVc4TableSize = _WdmGeneralWdmVc4TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 9),
    _WdmGeneralWdmVc4TableSize_Type()
)
wdmGeneralWdmVc4TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmVc4TableSize.setStatus("current")
_WdmGeneralWdmRemoteProtTableSize_Type = Unsigned32
_WdmGeneralWdmRemoteProtTableSize_Object = MibScalar
wdmGeneralWdmRemoteProtTableSize = _WdmGeneralWdmRemoteProtTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 10),
    _WdmGeneralWdmRemoteProtTableSize_Type()
)
wdmGeneralWdmRemoteProtTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmRemoteProtTableSize.setStatus("current")
_WdmGeneralWdmCtrlChannelTableSize_Type = Unsigned32
_WdmGeneralWdmCtrlChannelTableSize_Object = MibScalar
wdmGeneralWdmCtrlChannelTableSize = _WdmGeneralWdmCtrlChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 11),
    _WdmGeneralWdmCtrlChannelTableSize_Type()
)
wdmGeneralWdmCtrlChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmCtrlChannelTableSize.setStatus("current")
_WdmGeneralWdmCtrlGroupTableSize_Type = Unsigned32
_WdmGeneralWdmCtrlGroupTableSize_Object = MibScalar
wdmGeneralWdmCtrlGroupTableSize = _WdmGeneralWdmCtrlGroupTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 12),
    _WdmGeneralWdmCtrlGroupTableSize_Type()
)
wdmGeneralWdmCtrlGroupTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmCtrlGroupTableSize.setStatus("current")
_WdmGeneralWdmSubChannelTableSize_Type = Unsigned32
_WdmGeneralWdmSubChannelTableSize_Object = MibScalar
wdmGeneralWdmSubChannelTableSize = _WdmGeneralWdmSubChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 13),
    _WdmGeneralWdmSubChannelTableSize_Type()
)
wdmGeneralWdmSubChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmSubChannelTableSize.setStatus("current")
_WdmGeneralWdmDelayCompPGTableSize_Type = Unsigned32
_WdmGeneralWdmDelayCompPGTableSize_Object = MibScalar
wdmGeneralWdmDelayCompPGTableSize = _WdmGeneralWdmDelayCompPGTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 14),
    _WdmGeneralWdmDelayCompPGTableSize_Type()
)
wdmGeneralWdmDelayCompPGTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmDelayCompPGTableSize.setStatus("current")
_WdmGeneralWdmDelayCompLinkTableSize_Type = Unsigned32
_WdmGeneralWdmDelayCompLinkTableSize_Object = MibScalar
wdmGeneralWdmDelayCompLinkTableSize = _WdmGeneralWdmDelayCompLinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 15),
    _WdmGeneralWdmDelayCompLinkTableSize_Type()
)
wdmGeneralWdmDelayCompLinkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmDelayCompLinkTableSize.setStatus("current")
_WdmGeneralWdmMeanChannelPowerControlTableSize_Type = Unsigned32
_WdmGeneralWdmMeanChannelPowerControlTableSize_Object = MibScalar
wdmGeneralWdmMeanChannelPowerControlTableSize = _WdmGeneralWdmMeanChannelPowerControlTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 16),
    _WdmGeneralWdmMeanChannelPowerControlTableSize_Type()
)
wdmGeneralWdmMeanChannelPowerControlTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmMeanChannelPowerControlTableSize.setStatus("current")
_WdmGeneralWdmMeanChannelPowerControlGlobalTableSize_Type = Unsigned32
_WdmGeneralWdmMeanChannelPowerControlGlobalTableSize_Object = MibScalar
wdmGeneralWdmMeanChannelPowerControlGlobalTableSize = _WdmGeneralWdmMeanChannelPowerControlGlobalTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 1, 17),
    _WdmGeneralWdmMeanChannelPowerControlGlobalTableSize_Type()
)
wdmGeneralWdmMeanChannelPowerControlGlobalTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmGeneralWdmMeanChannelPowerControlGlobalTableSize.setStatus("current")
_WdmIfList_ObjectIdentity = ObjectIdentity
wdmIfList = _WdmIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2)
)
_WdmIfTable_Object = MibTable
wdmIfTable = _WdmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wdmIfTable.setStatus("current")
_WdmIfEntry_Object = MibTableRow
wdmIfEntry = _WdmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1)
)
wdmIfEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmIfIndex"),
)
if mibBuilder.loadTexts:
    wdmIfEntry.setStatus("current")


class _WdmIfIndex_Type(Unsigned32):
    """Custom type wdmIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmIfIndex_Type.__name__ = "Unsigned32"
_WdmIfIndex_Object = MibTableColumn
wdmIfIndex = _WdmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 1),
    _WdmIfIndex_Type()
)
wdmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfIndex.setStatus("current")
_WdmIfName_Type = MgmtNameString
_WdmIfName_Object = MibTableColumn
wdmIfName = _WdmIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 2),
    _WdmIfName_Type()
)
wdmIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfName.setStatus("current")


class _WdmIfDescr_Type(DisplayString):
    """Custom type wdmIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmIfDescr_Type.__name__ = "DisplayString"
_WdmIfDescr_Object = MibTableColumn
wdmIfDescr = _WdmIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 3),
    _WdmIfDescr_Type()
)
wdmIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfDescr.setStatus("current")
_WdmIfSubrack_Type = SubrackNumber
_WdmIfSubrack_Object = MibTableColumn
wdmIfSubrack = _WdmIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 4),
    _WdmIfSubrack_Type()
)
wdmIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSubrack.setStatus("current")
_WdmIfSlot_Type = SlotNumber
_WdmIfSlot_Object = MibTableColumn
wdmIfSlot = _WdmIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 5),
    _WdmIfSlot_Type()
)
wdmIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSlot.setStatus("current")
_WdmIfTxPort_Type = PortNumber
_WdmIfTxPort_Object = MibTableColumn
wdmIfTxPort = _WdmIfTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 6),
    _WdmIfTxPort_Type()
)
wdmIfTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTxPort.setStatus("current")


class _WdmIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type wdmIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WdmIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_WdmIfInvPhysIndexOrZero_Object = MibTableColumn
wdmIfInvPhysIndexOrZero = _WdmIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 7),
    _WdmIfInvPhysIndexOrZero_Type()
)
wdmIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfInvPhysIndexOrZero.setStatus("current")
_WdmIfTxLambda_Type = LambdaFrequency
_WdmIfTxLambda_Object = MibTableColumn
wdmIfTxLambda = _WdmIfTxLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 8),
    _WdmIfTxLambda_Type()
)
wdmIfTxLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTxLambda.setStatus("current")
_WdmIfHighSpeedMin_Type = Gauge32
_WdmIfHighSpeedMin_Object = MibTableColumn
wdmIfHighSpeedMin = _WdmIfHighSpeedMin_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 9),
    _WdmIfHighSpeedMin_Type()
)
wdmIfHighSpeedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfHighSpeedMin.setStatus("current")
_WdmIfHighSpeedMax_Type = Gauge32
_WdmIfHighSpeedMax_Object = MibTableColumn
wdmIfHighSpeedMax = _WdmIfHighSpeedMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 10),
    _WdmIfHighSpeedMax_Type()
)
wdmIfHighSpeedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfHighSpeedMax.setStatus("current")
_WdmIfPowerLevel_Type = Integer32
_WdmIfPowerLevel_Object = MibTableColumn
wdmIfPowerLevel = _WdmIfPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 11),
    _WdmIfPowerLevel_Type()
)
wdmIfPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfPowerLevel.setStatus("current")


class _WdmIfPowerLevelHighThreshold_Type(Integer32):
    """Custom type wdmIfPowerLevelHighThreshold based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-380, -60),
    )


_WdmIfPowerLevelHighThreshold_Type.__name__ = "Integer32"
_WdmIfPowerLevelHighThreshold_Object = MibTableColumn
wdmIfPowerLevelHighThreshold = _WdmIfPowerLevelHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 12),
    _WdmIfPowerLevelHighThreshold_Type()
)
wdmIfPowerLevelHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfPowerLevelHighThreshold.setStatus("current")


class _WdmIfPowerLevelLowThreshold_Type(Integer32):
    """Custom type wdmIfPowerLevelLowThreshold based on Integer32"""
    defaultValue = -270

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-380, -60),
    )


_WdmIfPowerLevelLowThreshold_Type.__name__ = "Integer32"
_WdmIfPowerLevelLowThreshold_Object = MibTableColumn
wdmIfPowerLevelLowThreshold = _WdmIfPowerLevelLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 13),
    _WdmIfPowerLevelLowThreshold_Type()
)
wdmIfPowerLevelLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfPowerLevelLowThreshold.setStatus("current")
_WdmIfLaserTemp_Type = Unsigned32
_WdmIfLaserTemp_Object = MibTableColumn
wdmIfLaserTemp = _WdmIfLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 14),
    _WdmIfLaserTemp_Type()
)
wdmIfLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserTemp.setStatus("current")
_WdmIfLaserTempOffset_Type = Integer32
_WdmIfLaserTempOffset_Object = MibTableColumn
wdmIfLaserTempOffset = _WdmIfLaserTempOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 15),
    _WdmIfLaserTempOffset_Type()
)
wdmIfLaserTempOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserTempOffset.setStatus("current")


class _WdmIfLaserTempOffsetThreshold_Type(Unsigned32):
    """Custom type wdmIfLaserTempOffsetThreshold based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WdmIfLaserTempOffsetThreshold_Type.__name__ = "Unsigned32"
_WdmIfLaserTempOffsetThreshold_Object = MibTableColumn
wdmIfLaserTempOffsetThreshold = _WdmIfLaserTempOffsetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 16),
    _WdmIfLaserTempOffsetThreshold_Type()
)
wdmIfLaserTempOffsetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLaserTempOffsetThreshold.setStatus("current")


class _WdmIfLaserMode_Type(Integer32):
    """Custom type wdmIfLaserMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("als", 2))
    )


_WdmIfLaserMode_Type.__name__ = "Integer32"
_WdmIfLaserMode_Object = MibTableColumn
wdmIfLaserMode = _WdmIfLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 17),
    _WdmIfLaserMode_Type()
)
wdmIfLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLaserMode.setStatus("current")


class _WdmIfLaserStatus_Type(Integer32):
    """Custom type wdmIfLaserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WdmIfLaserStatus_Type.__name__ = "Integer32"
_WdmIfLaserStatus_Object = MibTableColumn
wdmIfLaserStatus = _WdmIfLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 18),
    _WdmIfLaserStatus_Type()
)
wdmIfLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserStatus.setStatus("current")


class _WdmIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type wdmIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_WdmIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_WdmIfAdminStatus_Object = MibTableColumn
wdmIfAdminStatus = _WdmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 19),
    _WdmIfAdminStatus_Type()
)
wdmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfAdminStatus.setStatus("current")


class _WdmIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type wdmIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_WdmIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_WdmIfOperStatus_Object = MibTableColumn
wdmIfOperStatus = _WdmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 20),
    _WdmIfOperStatus_Type()
)
wdmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfOperStatus.setStatus("current")
_WdmIfLossOfSignal_Type = FaultStatus
_WdmIfLossOfSignal_Object = MibTableColumn
wdmIfLossOfSignal = _WdmIfLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 21),
    _WdmIfLossOfSignal_Type()
)
wdmIfLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLossOfSignal.setStatus("current")
_WdmIfReceivedPowerHigh_Type = FaultStatus
_WdmIfReceivedPowerHigh_Object = MibTableColumn
wdmIfReceivedPowerHigh = _WdmIfReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 22),
    _WdmIfReceivedPowerHigh_Type()
)
wdmIfReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfReceivedPowerHigh.setStatus("current")
_WdmIfReceivedPowerLow_Type = FaultStatus
_WdmIfReceivedPowerLow_Object = MibTableColumn
wdmIfReceivedPowerLow = _WdmIfReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 23),
    _WdmIfReceivedPowerLow_Type()
)
wdmIfReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfReceivedPowerLow.setStatus("current")
_WdmIfLaserBiasHigh_Type = FaultStatus
_WdmIfLaserBiasHigh_Object = MibTableColumn
wdmIfLaserBiasHigh = _WdmIfLaserBiasHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 24),
    _WdmIfLaserBiasHigh_Type()
)
wdmIfLaserBiasHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserBiasHigh.setStatus("current")
_WdmIfErroredSeconds_Type = FaultStatus
_WdmIfErroredSeconds_Object = MibTableColumn
wdmIfErroredSeconds = _WdmIfErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 25),
    _WdmIfErroredSeconds_Type()
)
wdmIfErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfErroredSeconds.setStatus("deprecated")
_WdmIfSeverelyErroredSeconds_Type = FaultStatus
_WdmIfSeverelyErroredSeconds_Object = MibTableColumn
wdmIfSeverelyErroredSeconds = _WdmIfSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 26),
    _WdmIfSeverelyErroredSeconds_Type()
)
wdmIfSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSeverelyErroredSeconds.setStatus("deprecated")
_WdmIfBackgroundBlockErrors_Type = FaultStatus
_WdmIfBackgroundBlockErrors_Object = MibTableColumn
wdmIfBackgroundBlockErrors = _WdmIfBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 27),
    _WdmIfBackgroundBlockErrors_Type()
)
wdmIfBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfBackgroundBlockErrors.setStatus("deprecated")
_WdmIfUnavailableSeconds_Type = FaultStatus
_WdmIfUnavailableSeconds_Object = MibTableColumn
wdmIfUnavailableSeconds = _WdmIfUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 28),
    _WdmIfUnavailableSeconds_Type()
)
wdmIfUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfUnavailableSeconds.setStatus("deprecated")
_WdmIfForwardDefectIndication_Type = FaultStatus
_WdmIfForwardDefectIndication_Object = MibTableColumn
wdmIfForwardDefectIndication = _WdmIfForwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 29),
    _WdmIfForwardDefectIndication_Type()
)
wdmIfForwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfForwardDefectIndication.setStatus("current")
_WdmIfBackwardDefectIndication_Type = FaultStatus
_WdmIfBackwardDefectIndication_Object = MibTableColumn
wdmIfBackwardDefectIndication = _WdmIfBackwardDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 30),
    _WdmIfBackwardDefectIndication_Type()
)
wdmIfBackwardDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfBackwardDefectIndication.setStatus("current")
_WdmIfLossOfFrame_Type = FaultStatus
_WdmIfLossOfFrame_Object = MibTableColumn
wdmIfLossOfFrame = _WdmIfLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 31),
    _WdmIfLossOfFrame_Type()
)
wdmIfLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLossOfFrame.setStatus("current")
_WdmIfAlarmIndicationSignal_Type = FaultStatus
_WdmIfAlarmIndicationSignal_Object = MibTableColumn
wdmIfAlarmIndicationSignal = _WdmIfAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 32),
    _WdmIfAlarmIndicationSignal_Type()
)
wdmIfAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfAlarmIndicationSignal.setStatus("current")
_WdmIfRemoteDefectIndication_Type = FaultStatus
_WdmIfRemoteDefectIndication_Object = MibTableColumn
wdmIfRemoteDefectIndication = _WdmIfRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 33),
    _WdmIfRemoteDefectIndication_Type()
)
wdmIfRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfRemoteDefectIndication.setStatus("current")
_WdmIfLossOfSync_Type = FaultStatus
_WdmIfLossOfSync_Object = MibTableColumn
wdmIfLossOfSync = _WdmIfLossOfSync_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 34),
    _WdmIfLossOfSync_Type()
)
wdmIfLossOfSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLossOfSync.setStatus("current")
_WdmIfLossOfForwardingErrorCorrection_Type = FaultStatus
_WdmIfLossOfForwardingErrorCorrection_Object = MibTableColumn
wdmIfLossOfForwardingErrorCorrection = _WdmIfLossOfForwardingErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 35),
    _WdmIfLossOfForwardingErrorCorrection_Type()
)
wdmIfLossOfForwardingErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLossOfForwardingErrorCorrection.setStatus("current")
_WdmIfLaserTempHigh_Type = FaultStatus
_WdmIfLaserTempHigh_Object = MibTableColumn
wdmIfLaserTempHigh = _WdmIfLaserTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 36),
    _WdmIfLaserTempHigh_Type()
)
wdmIfLaserTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserTempHigh.setStatus("current")
_WdmIfLaserTempLow_Type = FaultStatus
_WdmIfLaserTempLow_Object = MibTableColumn
wdmIfLaserTempLow = _WdmIfLaserTempLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 37),
    _WdmIfLaserTempLow_Type()
)
wdmIfLaserTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserTempLow.setStatus("current")
_WdmIfRxPort_Type = PortNumber
_WdmIfRxPort_Object = MibTableColumn
wdmIfRxPort = _WdmIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 38),
    _WdmIfRxPort_Type()
)
wdmIfRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfRxPort.setStatus("current")
_WdmIfBitrateMismatch_Type = FaultStatus
_WdmIfBitrateMismatch_Object = MibTableColumn
wdmIfBitrateMismatch = _WdmIfBitrateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 39),
    _WdmIfBitrateMismatch_Type()
)
wdmIfBitrateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfBitrateMismatch.setStatus("current")
_WdmIfLaserBias_Type = Unsigned32
_WdmIfLaserBias_Object = MibTableColumn
wdmIfLaserBias = _WdmIfLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 40),
    _WdmIfLaserBias_Type()
)
wdmIfLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserBias.setStatus("current")


class _WdmIfLaserBiasThreshold_Type(Unsigned32):
    """Custom type wdmIfLaserBiasThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_WdmIfLaserBiasThreshold_Type.__name__ = "Unsigned32"
_WdmIfLaserBiasThreshold_Object = MibTableColumn
wdmIfLaserBiasThreshold = _WdmIfLaserBiasThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 41),
    _WdmIfLaserBiasThreshold_Type()
)
wdmIfLaserBiasThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLaserBiasThreshold.setStatus("current")


class _WdmIfLossOfSignalThreshold_Type(Integer32):
    """Custom type wdmIfLossOfSignalThreshold based on Integer32"""
    defaultValue = -350

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-380, -220),
    )


_WdmIfLossOfSignalThreshold_Type.__name__ = "Integer32"
_WdmIfLossOfSignalThreshold_Object = MibTableColumn
wdmIfLossOfSignalThreshold = _WdmIfLossOfSignalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 42),
    _WdmIfLossOfSignalThreshold_Type()
)
wdmIfLossOfSignalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLossOfSignalThreshold.setStatus("current")


class _WdmIfJ0PathTrace_Type(OctetString):
    """Custom type wdmIfJ0PathTrace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(16, 16),
    )


_WdmIfJ0PathTrace_Type.__name__ = "OctetString"
_WdmIfJ0PathTrace_Object = MibTableColumn
wdmIfJ0PathTrace = _WdmIfJ0PathTrace_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 44),
    _WdmIfJ0PathTrace_Type()
)
wdmIfJ0PathTrace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfJ0PathTrace.setStatus("deprecated")


class _WdmIfInbandMode_Type(Integer32):
    """Custom type wdmIfInbandMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WdmIfInbandMode_Type.__name__ = "Integer32"
_WdmIfInbandMode_Object = MibTableColumn
wdmIfInbandMode = _WdmIfInbandMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 45),
    _WdmIfInbandMode_Type()
)
wdmIfInbandMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfInbandMode.setStatus("deprecated")


class _WdmIfInbandStatus_Type(Integer32):
    """Custom type wdmIfInbandStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WdmIfInbandStatus_Type.__name__ = "Integer32"
_WdmIfInbandStatus_Object = MibTableColumn
wdmIfInbandStatus = _WdmIfInbandStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 46),
    _WdmIfInbandStatus_Type()
)
wdmIfInbandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfInbandStatus.setStatus("deprecated")


class _WdmIfExpectedTxLambda_Type(LambdaFrequency):
    """Custom type wdmIfExpectedTxLambda based on LambdaFrequency"""
    defaultValue = 0


_WdmIfExpectedTxLambda_Type.__name__ = "LambdaFrequency"
_WdmIfExpectedTxLambda_Object = MibTableColumn
wdmIfExpectedTxLambda = _WdmIfExpectedTxLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 47),
    _WdmIfExpectedTxLambda_Type()
)
wdmIfExpectedTxLambda.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfExpectedTxLambda.setStatus("current")


class _WdmIfForwardingErrorCorrectionMode_Type(Integer32):
    """Custom type wdmIfForwardingErrorCorrectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("auto", 3))
    )


_WdmIfForwardingErrorCorrectionMode_Type.__name__ = "Integer32"
_WdmIfForwardingErrorCorrectionMode_Object = MibTableColumn
wdmIfForwardingErrorCorrectionMode = _WdmIfForwardingErrorCorrectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 48),
    _WdmIfForwardingErrorCorrectionMode_Type()
)
wdmIfForwardingErrorCorrectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfForwardingErrorCorrectionMode.setStatus("current")
_WdmIfUnexpectedTxLambda_Type = FaultStatus
_WdmIfUnexpectedTxLambda_Object = MibTableColumn
wdmIfUnexpectedTxLambda = _WdmIfUnexpectedTxLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 49),
    _WdmIfUnexpectedTxLambda_Type()
)
wdmIfUnexpectedTxLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfUnexpectedTxLambda.setStatus("current")


class _WdmIfTraceIntrusionMode_Type(Integer32):
    """Custom type wdmIfTraceIntrusionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfTraceIntrusionMode_Type.__name__ = "Integer32"
_WdmIfTraceIntrusionMode_Object = MibTableColumn
wdmIfTraceIntrusionMode = _WdmIfTraceIntrusionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 50),
    _WdmIfTraceIntrusionMode_Type()
)
wdmIfTraceIntrusionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfTraceIntrusionMode.setStatus("current")


class _WdmIfTraceTransmitted_Type(DisplayString):
    """Custom type wdmIfTraceTransmitted based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_WdmIfTraceTransmitted_Type.__name__ = "DisplayString"
_WdmIfTraceTransmitted_Object = MibTableColumn
wdmIfTraceTransmitted = _WdmIfTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 51),
    _WdmIfTraceTransmitted_Type()
)
wdmIfTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfTraceTransmitted.setStatus("current")


class _WdmIfTraceReceived_Type(DisplayString):
    """Custom type wdmIfTraceReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_WdmIfTraceReceived_Type.__name__ = "DisplayString"
_WdmIfTraceReceived_Object = MibTableColumn
wdmIfTraceReceived = _WdmIfTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 52),
    _WdmIfTraceReceived_Type()
)
wdmIfTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTraceReceived.setStatus("current")


class _WdmIfTraceExpected_Type(DisplayString):
    """Custom type wdmIfTraceExpected based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 62),
    )


_WdmIfTraceExpected_Type.__name__ = "DisplayString"
_WdmIfTraceExpected_Object = MibTableColumn
wdmIfTraceExpected = _WdmIfTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 53),
    _WdmIfTraceExpected_Type()
)
wdmIfTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfTraceExpected.setStatus("current")


class _WdmIfTraceAlarmMode_Type(Integer32):
    """Custom type wdmIfTraceAlarmMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfTraceAlarmMode_Type.__name__ = "Integer32"
_WdmIfTraceAlarmMode_Object = MibTableColumn
wdmIfTraceAlarmMode = _WdmIfTraceAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 54),
    _WdmIfTraceAlarmMode_Type()
)
wdmIfTraceAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfTraceAlarmMode.setStatus("current")
_WdmIfTraceMismatch_Type = FaultStatus
_WdmIfTraceMismatch_Object = MibTableColumn
wdmIfTraceMismatch = _WdmIfTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 55),
    _WdmIfTraceMismatch_Type()
)
wdmIfTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTraceMismatch.setStatus("current")
_WdmIfLaserStatusLastChangeTime_Type = DateAndTime
_WdmIfLaserStatusLastChangeTime_Object = MibTableColumn
wdmIfLaserStatusLastChangeTime = _WdmIfLaserStatusLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 56),
    _WdmIfLaserStatusLastChangeTime_Type()
)
wdmIfLaserStatusLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserStatusLastChangeTime.setStatus("current")


class _WdmIfSuppressRemoteAlarms_Type(Integer32):
    """Custom type wdmIfSuppressRemoteAlarms based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfSuppressRemoteAlarms_Type.__name__ = "Integer32"
_WdmIfSuppressRemoteAlarms_Object = MibTableColumn
wdmIfSuppressRemoteAlarms = _WdmIfSuppressRemoteAlarms_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 57),
    _WdmIfSuppressRemoteAlarms_Type()
)
wdmIfSuppressRemoteAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfSuppressRemoteAlarms.setStatus("current")
_WdmIfSerialNumberMismatch_Type = FaultStatus
_WdmIfSerialNumberMismatch_Object = MibTableColumn
wdmIfSerialNumberMismatch = _WdmIfSerialNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 58),
    _WdmIfSerialNumberMismatch_Type()
)
wdmIfSerialNumberMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSerialNumberMismatch.setStatus("current")


class _WdmIfOptimizeDecisionThreshold_Type(CommandString):
    """Custom type wdmIfOptimizeDecisionThreshold based on CommandString"""
    defaultValue = OctetString("normal")


_WdmIfOptimizeDecisionThreshold_Type.__name__ = "CommandString"
_WdmIfOptimizeDecisionThreshold_Object = MibTableColumn
wdmIfOptimizeDecisionThreshold = _WdmIfOptimizeDecisionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 59),
    _WdmIfOptimizeDecisionThreshold_Type()
)
wdmIfOptimizeDecisionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfOptimizeDecisionThreshold.setStatus("current")


class _WdmIfThresholdOptimizationState_Type(Integer32):
    """Custom type wdmIfThresholdOptimizationState based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("started", 2),
          ("searchingFirstLow", 3),
          ("searchingSecondLow", 4),
          ("searchingThirdLow", 5),
          ("searchingFirstHigh", 6),
          ("searchingSecondHigh", 7),
          ("searchingThirdHigh", 8),
          ("finishedFailed", 9),
          ("finishedOk", 10),
          ("searchingFrameLow", 11),
          ("searchingFrameHigh", 12),
          ("foundFrame", 13),
          ("waitOptimize", 14))
    )


_WdmIfThresholdOptimizationState_Type.__name__ = "Integer32"
_WdmIfThresholdOptimizationState_Object = MibTableColumn
wdmIfThresholdOptimizationState = _WdmIfThresholdOptimizationState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 60),
    _WdmIfThresholdOptimizationState_Type()
)
wdmIfThresholdOptimizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfThresholdOptimizationState.setStatus("current")


class _WdmIfUseHwDefaultDecisionThreshold_Type(Integer32):
    """Custom type wdmIfUseHwDefaultDecisionThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_WdmIfUseHwDefaultDecisionThreshold_Type.__name__ = "Integer32"
_WdmIfUseHwDefaultDecisionThreshold_Object = MibTableColumn
wdmIfUseHwDefaultDecisionThreshold = _WdmIfUseHwDefaultDecisionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 61),
    _WdmIfUseHwDefaultDecisionThreshold_Type()
)
wdmIfUseHwDefaultDecisionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfUseHwDefaultDecisionThreshold.setStatus("current")
_WdmIfFecCorrectedZeros_Type = Unsigned32
_WdmIfFecCorrectedZeros_Object = MibTableColumn
wdmIfFecCorrectedZeros = _WdmIfFecCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 62),
    _WdmIfFecCorrectedZeros_Type()
)
wdmIfFecCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfFecCorrectedZeros.setStatus("current")
_WdmIfFecCorrectedOnes_Type = Unsigned32
_WdmIfFecCorrectedOnes_Object = MibTableColumn
wdmIfFecCorrectedOnes = _WdmIfFecCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 63),
    _WdmIfFecCorrectedOnes_Type()
)
wdmIfFecCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfFecCorrectedOnes.setStatus("current")


class _WdmIfOptimizedForSerialNumber_Type(DisplayString):
    """Custom type wdmIfOptimizedForSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_WdmIfOptimizedForSerialNumber_Type.__name__ = "DisplayString"
_WdmIfOptimizedForSerialNumber_Object = MibTableColumn
wdmIfOptimizedForSerialNumber = _WdmIfOptimizedForSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 64),
    _WdmIfOptimizedForSerialNumber_Type()
)
wdmIfOptimizedForSerialNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfOptimizedForSerialNumber.setStatus("current")


class _WdmIfRelativeDecisionThreshold_Type(Integer32):
    """Custom type wdmIfRelativeDecisionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000, 1000000),
    )


_WdmIfRelativeDecisionThreshold_Type.__name__ = "Integer32"
_WdmIfRelativeDecisionThreshold_Object = MibTableColumn
wdmIfRelativeDecisionThreshold = _WdmIfRelativeDecisionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 65),
    _WdmIfRelativeDecisionThreshold_Type()
)
wdmIfRelativeDecisionThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfRelativeDecisionThreshold.setStatus("current")
_WdmIfTrxCodeMismatch_Type = FaultStatus
_WdmIfTrxCodeMismatch_Object = MibTableColumn
wdmIfTrxCodeMismatch = _WdmIfTrxCodeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 66),
    _WdmIfTrxCodeMismatch_Type()
)
wdmIfTrxCodeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxCodeMismatch.setStatus("current")
_WdmIfTrxBitrateUnavailable_Type = FaultStatus
_WdmIfTrxBitrateUnavailable_Object = MibTableColumn
wdmIfTrxBitrateUnavailable = _WdmIfTrxBitrateUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 67),
    _WdmIfTrxBitrateUnavailable_Type()
)
wdmIfTrxBitrateUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxBitrateUnavailable.setStatus("current")
_WdmIfTrxMissing_Type = FaultStatus
_WdmIfTrxMissing_Object = MibTableColumn
wdmIfTrxMissing = _WdmIfTrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 68),
    _WdmIfTrxMissing_Type()
)
wdmIfTrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxMissing.setStatus("current")


class _WdmIfTrxClass_Type(DisplayString):
    """Custom type wdmIfTrxClass based on DisplayString"""
    defaultValue = OctetString("")


_WdmIfTrxClass_Type.__name__ = "DisplayString"
_WdmIfTrxClass_Object = MibTableColumn
wdmIfTrxClass = _WdmIfTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 69),
    _WdmIfTrxClass_Type()
)
wdmIfTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxClass.setStatus("current")


class _WdmIfLaserTempHighRelativeThreshold_Type(Integer32):
    """Custom type wdmIfLaserTempHighRelativeThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_WdmIfLaserTempHighRelativeThreshold_Type.__name__ = "Integer32"
_WdmIfLaserTempHighRelativeThreshold_Object = MibTableColumn
wdmIfLaserTempHighRelativeThreshold = _WdmIfLaserTempHighRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 70),
    _WdmIfLaserTempHighRelativeThreshold_Type()
)
wdmIfLaserTempHighRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLaserTempHighRelativeThreshold.setStatus("current")


class _WdmIfLaserTempLowRelativeThreshold_Type(Integer32):
    """Custom type wdmIfLaserTempLowRelativeThreshold based on Integer32"""
    defaultValue = -10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_WdmIfLaserTempLowRelativeThreshold_Type.__name__ = "Integer32"
_WdmIfLaserTempLowRelativeThreshold_Object = MibTableColumn
wdmIfLaserTempLowRelativeThreshold = _WdmIfLaserTempLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 71),
    _WdmIfLaserTempLowRelativeThreshold_Type()
)
wdmIfLaserTempLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLaserTempLowRelativeThreshold.setStatus("current")
_WdmIfTransmitterFailed_Type = FaultStatus
_WdmIfTransmitterFailed_Object = MibTableColumn
wdmIfTransmitterFailed = _WdmIfTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 72),
    _WdmIfTransmitterFailed_Type()
)
wdmIfTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTransmitterFailed.setStatus("current")
_WdmIfReceiverSensitivity_Type = Integer32
_WdmIfReceiverSensitivity_Object = MibTableColumn
wdmIfReceiverSensitivity = _WdmIfReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 73),
    _WdmIfReceiverSensitivity_Type()
)
wdmIfReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfReceiverSensitivity.setStatus("current")


class _WdmIfPowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type wdmIfPowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_WdmIfPowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_WdmIfPowerLevelLowRelativeThreshold_Object = MibTableColumn
wdmIfPowerLevelLowRelativeThreshold = _WdmIfPowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 74),
    _WdmIfPowerLevelLowRelativeThreshold_Type()
)
wdmIfPowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfPowerLevelLowRelativeThreshold.setStatus("current")
_WdmIfIllegalFrequency_Type = FaultStatus
_WdmIfIllegalFrequency_Object = MibTableColumn
wdmIfIllegalFrequency = _WdmIfIllegalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 75),
    _WdmIfIllegalFrequency_Type()
)
wdmIfIllegalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfIllegalFrequency.setStatus("current")


class _WdmIfLaserForcedOn_Type(Integer32):
    """Custom type wdmIfLaserForcedOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfLaserForcedOn_Type.__name__ = "Integer32"
_WdmIfLaserForcedOn_Object = MibTableColumn
wdmIfLaserForcedOn = _WdmIfLaserForcedOn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 76),
    _WdmIfLaserForcedOn_Type()
)
wdmIfLaserForcedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfLaserForcedOn.setStatus("current")


class _WdmIfTrafficCombination_Type(Integer32):
    """Custom type wdmIfTrafficCombination based on Integer32"""
    defaultValue = 0

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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("fcGbEx2", 1),
          ("fc2G", 2),
          ("dvbEsconx8", 3),
          ("esconx10", 4),
          ("framedGbEx10", 5),
          ("esconx6FcGbE", 6),
          ("dvbEsconx4FcGbE", 7),
          ("mixed", 8),
          ("framedGbEx10Vc4", 9),
          ("fcx2VcatVc4", 10),
          ("fc2GVcatVc4", 11),
          ("dvbEsconx8VcatVc4", 12),
          ("mixedVcatVc4", 13),
          ("fcGbEx2VcatVc4", 14),
          ("gbEx3Stm1x5", 15),
          ("gbEx2Stm4x2Stm1x4", 16),
          ("gbEx3Stm4Oc12x1Stm1Oc3x3", 17),
          ("gbEx1Stm16Oc48x1Stm1Oc3x3", 18),
          ("gbEx4x2", 19),
          ("gbEx4Stm16Oc48x2", 20),
          ("stm16Oc48x4", 21),
          ("gbEx2Fcx2x2", 22),
          ("gbESyncEx3Stm4Oc12Stm1Oc3x1", 23),
          ("gbEStm16Oc48Stm4Oc12Stm1Oc3", 24),
          ("gbEStm16Oc48", 25),
          ("syncEx14GLinex2", 26),
          ("syncEx10", 27),
          ("gbEx3Stm4Oc12x1Stm1Oc3x3Basic", 28),
          ("gbESyncEx3Stm4Oc12Stm1Oc3x1Basic", 29),
          ("cpri3x3syncEx2", 30),
          ("syncEx1Cpri4x3", 31))
    )


_WdmIfTrafficCombination_Type.__name__ = "Integer32"
_WdmIfTrafficCombination_Object = MibTableColumn
wdmIfTrafficCombination = _WdmIfTrafficCombination_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 77),
    _WdmIfTrafficCombination_Type()
)
wdmIfTrafficCombination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfTrafficCombination.setStatus("current")


class _WdmIfSelectTrafficCombination_Type(CommandString):
    """Custom type wdmIfSelectTrafficCombination based on CommandString"""
    defaultValue = OctetString("normal")


_WdmIfSelectTrafficCombination_Type.__name__ = "CommandString"
_WdmIfSelectTrafficCombination_Object = MibTableColumn
wdmIfSelectTrafficCombination = _WdmIfSelectTrafficCombination_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 78),
    _WdmIfSelectTrafficCombination_Type()
)
wdmIfSelectTrafficCombination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSelectTrafficCombination.setStatus("current")
_WdmIfObjectProperty_Type = ObjectProperty
_WdmIfObjectProperty_Object = MibTableColumn
wdmIfObjectProperty = _WdmIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 79),
    _WdmIfObjectProperty_Type()
)
wdmIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfObjectProperty.setStatus("current")
_WdmIfTxPowerLevel_Type = Integer32
_WdmIfTxPowerLevel_Object = MibTableColumn
wdmIfTxPowerLevel = _WdmIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 80),
    _WdmIfTxPowerLevel_Type()
)
wdmIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTxPowerLevel.setStatus("current")
_WdmIfLaserTempActual_Type = Integer32
_WdmIfLaserTempActual_Object = MibTableColumn
wdmIfLaserTempActual = _WdmIfLaserTempActual_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 81),
    _WdmIfLaserTempActual_Type()
)
wdmIfLaserTempActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLaserTempActual.setStatus("current")
_WdmIfTrxFailed_Type = FaultStatus
_WdmIfTrxFailed_Object = MibTableColumn
wdmIfTrxFailed = _WdmIfTrxFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 82),
    _WdmIfTrxFailed_Type()
)
wdmIfTrxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxFailed.setStatus("current")
_WdmIfDisabled_Type = FaultStatus
_WdmIfDisabled_Object = MibTableColumn
wdmIfDisabled = _WdmIfDisabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 83),
    _WdmIfDisabled_Type()
)
wdmIfDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfDisabled.setStatus("current")
_WdmIfLoopback_Type = FaultStatus
_WdmIfLoopback_Object = MibTableColumn
wdmIfLoopback = _WdmIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 84),
    _WdmIfLoopback_Type()
)
wdmIfLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLoopback.setStatus("current")


class _WdmIfContinousOptimization_Type(Integer32):
    """Custom type wdmIfContinousOptimization based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfContinousOptimization_Type.__name__ = "Integer32"
_WdmIfContinousOptimization_Object = MibTableColumn
wdmIfContinousOptimization = _WdmIfContinousOptimization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 85),
    _WdmIfContinousOptimization_Type()
)
wdmIfContinousOptimization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfContinousOptimization.setStatus("current")
_WdmIfThresholdOptimizationResultCause_Type = DisplayString
_WdmIfThresholdOptimizationResultCause_Object = MibTableColumn
wdmIfThresholdOptimizationResultCause = _WdmIfThresholdOptimizationResultCause_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 86),
    _WdmIfThresholdOptimizationResultCause_Type()
)
wdmIfThresholdOptimizationResultCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfThresholdOptimizationResultCause.setStatus("current")


class _WdmIfDistributionRole_Type(Integer32):
    """Custom type wdmIfDistributionRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("terminalMultiplexor", 1),
          ("broadcastHub", 2),
          ("broadcastSatellite", 3))
    )


_WdmIfDistributionRole_Type.__name__ = "Integer32"
_WdmIfDistributionRole_Object = MibTableColumn
wdmIfDistributionRole = _WdmIfDistributionRole_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 87),
    _WdmIfDistributionRole_Type()
)
wdmIfDistributionRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfDistributionRole.setStatus("current")
_WdmIfConfigurationCommand_Type = CommandString
_WdmIfConfigurationCommand_Object = MibTableColumn
wdmIfConfigurationCommand = _WdmIfConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 88),
    _WdmIfConfigurationCommand_Type()
)
wdmIfConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfConfigurationCommand.setStatus("current")
_WdmIfNoFrequencySet_Type = FaultStatus
_WdmIfNoFrequencySet_Object = MibTableColumn
wdmIfNoFrequencySet = _WdmIfNoFrequencySet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 89),
    _WdmIfNoFrequencySet_Type()
)
wdmIfNoFrequencySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfNoFrequencySet.setStatus("current")


class _WdmIfFormat_Type(SignalFormat):
    """Custom type wdmIfFormat based on SignalFormat"""
    defaultValue = 5


_WdmIfFormat_Type.__name__ = "SignalFormat"
_WdmIfFormat_Object = MibTableColumn
wdmIfFormat = _WdmIfFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 90),
    _WdmIfFormat_Type()
)
wdmIfFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfFormat.setStatus("current")
_WdmIfConfigurationFormatCommand_Type = CommandString
_WdmIfConfigurationFormatCommand_Object = MibTableColumn
wdmIfConfigurationFormatCommand = _WdmIfConfigurationFormatCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 91),
    _WdmIfConfigurationFormatCommand_Type()
)
wdmIfConfigurationFormatCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfConfigurationFormatCommand.setStatus("current")


class _WdmIfOHTransparency_Type(Integer32):
    """Custom type wdmIfOHTransparency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WdmIfOHTransparency_Type.__name__ = "Integer32"
_WdmIfOHTransparency_Object = MibTableColumn
wdmIfOHTransparency = _WdmIfOHTransparency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 92),
    _WdmIfOHTransparency_Type()
)
wdmIfOHTransparency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfOHTransparency.setStatus("deprecated")
_WdmIfLinkDown_Type = FaultStatus
_WdmIfLinkDown_Object = MibTableColumn
wdmIfLinkDown = _WdmIfLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 93),
    _WdmIfLinkDown_Type()
)
wdmIfLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLinkDown.setStatus("deprecated")


class _WdmIfAutoNegotiationMode_Type(Integer32):
    """Custom type wdmIfAutoNegotiationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WdmIfAutoNegotiationMode_Type.__name__ = "Integer32"
_WdmIfAutoNegotiationMode_Object = MibTableColumn
wdmIfAutoNegotiationMode = _WdmIfAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 94),
    _WdmIfAutoNegotiationMode_Type()
)
wdmIfAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfAutoNegotiationMode.setStatus("deprecated")


class _WdmIfAutoNegotiationStatus_Type(Integer32):
    """Custom type wdmIfAutoNegotiationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incomplete", 1),
          ("half", 2),
          ("full", 3))
    )


_WdmIfAutoNegotiationStatus_Type.__name__ = "Integer32"
_WdmIfAutoNegotiationStatus_Object = MibTableColumn
wdmIfAutoNegotiationStatus = _WdmIfAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 95),
    _WdmIfAutoNegotiationStatus_Type()
)
wdmIfAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfAutoNegotiationStatus.setStatus("deprecated")


class _WdmIfFlowControlMode_Type(Integer32):
    """Custom type wdmIfFlowControlMode based on Integer32"""
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
        *(("noPause", 1),
          ("rxPause", 2),
          ("txPause", 3),
          ("bothPause", 4))
    )


_WdmIfFlowControlMode_Type.__name__ = "Integer32"
_WdmIfFlowControlMode_Object = MibTableColumn
wdmIfFlowControlMode = _WdmIfFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 96),
    _WdmIfFlowControlMode_Type()
)
wdmIfFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfFlowControlMode.setStatus("deprecated")


class _WdmIfGroupLineMode_Type(Integer32):
    """Custom type wdmIfGroupLineMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfGroupLineMode_Type.__name__ = "Integer32"
_WdmIfGroupLineMode_Object = MibTableColumn
wdmIfGroupLineMode = _WdmIfGroupLineMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 97),
    _WdmIfGroupLineMode_Type()
)
wdmIfGroupLineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfGroupLineMode.setStatus("current")


class _WdmIfFecType_Type(Integer32):
    """Custom type wdmIfFecType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enhancedFec", 1),
          ("g709Fec", 2))
    )


_WdmIfFecType_Type.__name__ = "Integer32"
_WdmIfFecType_Object = MibTableColumn
wdmIfFecType = _WdmIfFecType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 98),
    _WdmIfFecType_Type()
)
wdmIfFecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfFecType.setStatus("current")


class _WdmIfFarEndLoopback_Type(Integer32):
    """Custom type wdmIfFarEndLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfFarEndLoopback_Type.__name__ = "Integer32"
_WdmIfFarEndLoopback_Object = MibTableColumn
wdmIfFarEndLoopback = _WdmIfFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 99),
    _WdmIfFarEndLoopback_Type()
)
wdmIfFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfFarEndLoopback.setStatus("current")


class _WdmIfFarEndLoopbackTimeout_Type(Integer32):
    """Custom type wdmIfFarEndLoopbackTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_WdmIfFarEndLoopbackTimeout_Type.__name__ = "Integer32"
_WdmIfFarEndLoopbackTimeout_Object = MibTableColumn
wdmIfFarEndLoopbackTimeout = _WdmIfFarEndLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 100),
    _WdmIfFarEndLoopbackTimeout_Type()
)
wdmIfFarEndLoopbackTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfFarEndLoopbackTimeout.setStatus("current")
_WdmIfFarEndLoopbackEnabled_Type = FaultStatus
_WdmIfFarEndLoopbackEnabled_Object = MibTableColumn
wdmIfFarEndLoopbackEnabled = _WdmIfFarEndLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 101),
    _WdmIfFarEndLoopbackEnabled_Type()
)
wdmIfFarEndLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfFarEndLoopbackEnabled.setStatus("current")
_WdmIfChangeLoopbackCommand_Type = CommandString
_WdmIfChangeLoopbackCommand_Object = MibTableColumn
wdmIfChangeLoopbackCommand = _WdmIfChangeLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 102),
    _WdmIfChangeLoopbackCommand_Type()
)
wdmIfChangeLoopbackCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfChangeLoopbackCommand.setStatus("current")
_WdmIfFecFailure_Type = FaultStatus
_WdmIfFecFailure_Object = MibTableColumn
wdmIfFecFailure = _WdmIfFecFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 103),
    _WdmIfFecFailure_Type()
)
wdmIfFecFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfFecFailure.setStatus("current")


class _WdmIfTxSignalStatus_Type(Integer32):
    """Custom type wdmIfTxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3),
          ("notApplicable", 2147483647))
    )


_WdmIfTxSignalStatus_Type.__name__ = "Integer32"
_WdmIfTxSignalStatus_Object = MibTableColumn
wdmIfTxSignalStatus = _WdmIfTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 104),
    _WdmIfTxSignalStatus_Type()
)
wdmIfTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTxSignalStatus.setStatus("current")


class _WdmIfRxSignalStatus_Type(Integer32):
    """Custom type wdmIfRxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3),
          ("notApplicable", 2147483647))
    )


_WdmIfRxSignalStatus_Type.__name__ = "Integer32"
_WdmIfRxSignalStatus_Object = MibTableColumn
wdmIfRxSignalStatus = _WdmIfRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 105),
    _WdmIfRxSignalStatus_Type()
)
wdmIfRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfRxSignalStatus.setStatus("current")


class _WdmIfNearEndLoopback_Type(Integer32):
    """Custom type wdmIfNearEndLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfNearEndLoopback_Type.__name__ = "Integer32"
_WdmIfNearEndLoopback_Object = MibTableColumn
wdmIfNearEndLoopback = _WdmIfNearEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 106),
    _WdmIfNearEndLoopback_Type()
)
wdmIfNearEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfNearEndLoopback.setStatus("current")


class _WdmIfNearEndLoopbackTimeout_Type(Integer32):
    """Custom type wdmIfNearEndLoopbackTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_WdmIfNearEndLoopbackTimeout_Type.__name__ = "Integer32"
_WdmIfNearEndLoopbackTimeout_Object = MibTableColumn
wdmIfNearEndLoopbackTimeout = _WdmIfNearEndLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 107),
    _WdmIfNearEndLoopbackTimeout_Type()
)
wdmIfNearEndLoopbackTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfNearEndLoopbackTimeout.setStatus("current")
_WdmIfNearEndLoopbackEnabled_Type = FaultStatus
_WdmIfNearEndLoopbackEnabled_Object = MibTableColumn
wdmIfNearEndLoopbackEnabled = _WdmIfNearEndLoopbackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 108),
    _WdmIfNearEndLoopbackEnabled_Type()
)
wdmIfNearEndLoopbackEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfNearEndLoopbackEnabled.setStatus("current")
_WdmIfChangeNearEndLoopbackCommand_Type = CommandString
_WdmIfChangeNearEndLoopbackCommand_Object = MibTableColumn
wdmIfChangeNearEndLoopbackCommand = _WdmIfChangeNearEndLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 109),
    _WdmIfChangeNearEndLoopbackCommand_Type()
)
wdmIfChangeNearEndLoopbackCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfChangeNearEndLoopbackCommand.setStatus("current")
_WdmIfSignalDegraded_Type = FaultStatus
_WdmIfSignalDegraded_Object = MibTableColumn
wdmIfSignalDegraded = _WdmIfSignalDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 110),
    _WdmIfSignalDegraded_Type()
)
wdmIfSignalDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSignalDegraded.setStatus("current")


class _WdmIfHubProtectionMode_Type(Integer32):
    """Custom type wdmIfHubProtectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfHubProtectionMode_Type.__name__ = "Integer32"
_WdmIfHubProtectionMode_Object = MibTableColumn
wdmIfHubProtectionMode = _WdmIfHubProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 111),
    _WdmIfHubProtectionMode_Type()
)
wdmIfHubProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfHubProtectionMode.setStatus("current")


class _WdmIfActualFormat_Type(SignalFormat):
    """Custom type wdmIfActualFormat based on SignalFormat"""
    defaultValue = 10


_WdmIfActualFormat_Type.__name__ = "SignalFormat"
_WdmIfActualFormat_Object = MibTableColumn
wdmIfActualFormat = _WdmIfActualFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 112),
    _WdmIfActualFormat_Type()
)
wdmIfActualFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfActualFormat.setStatus("current")


class _WdmIfTdcDispersion_Type(Integer32):
    """Custom type wdmIfTdcDispersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-800, 800),
    )


_WdmIfTdcDispersion_Type.__name__ = "Integer32"
_WdmIfTdcDispersion_Object = MibTableColumn
wdmIfTdcDispersion = _WdmIfTdcDispersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 113),
    _WdmIfTdcDispersion_Type()
)
wdmIfTdcDispersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfTdcDispersion.setStatus("current")
_WdmIfTdcDispersionCommand_Type = CommandString
_WdmIfTdcDispersionCommand_Object = MibTableColumn
wdmIfTdcDispersionCommand = _WdmIfTdcDispersionCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 114),
    _WdmIfTdcDispersionCommand_Type()
)
wdmIfTdcDispersionCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTdcDispersionCommand.setStatus("current")


class _WdmIfTdcDispersionMode_Type(Integer32):
    """Custom type wdmIfTdcDispersionMode based on Integer32"""
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
        *(("auto", 0),
          ("startValue", 1),
          ("manual", 2))
    )


_WdmIfTdcDispersionMode_Type.__name__ = "Integer32"
_WdmIfTdcDispersionMode_Object = MibTableColumn
wdmIfTdcDispersionMode = _WdmIfTdcDispersionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 115),
    _WdmIfTdcDispersionMode_Type()
)
wdmIfTdcDispersionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmIfTdcDispersionMode.setStatus("current")


class _WdmIfLineControlLoopCurrentState_Type(DisplayString):
    """Custom type wdmIfLineControlLoopCurrentState based on DisplayString"""
    defaultValue = OctetString("")


_WdmIfLineControlLoopCurrentState_Type.__name__ = "DisplayString"
_WdmIfLineControlLoopCurrentState_Object = MibTableColumn
wdmIfLineControlLoopCurrentState = _WdmIfLineControlLoopCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 116),
    _WdmIfLineControlLoopCurrentState_Type()
)
wdmIfLineControlLoopCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfLineControlLoopCurrentState.setStatus("current")


class _WdmIfSignalDegradeThreshold_Type(BerLevel):
    """Custom type wdmIfSignalDegradeThreshold based on BerLevel"""
    defaultValue = 13


_WdmIfSignalDegradeThreshold_Type.__name__ = "BerLevel"
_WdmIfSignalDegradeThreshold_Object = MibTableColumn
wdmIfSignalDegradeThreshold = _WdmIfSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 117),
    _WdmIfSignalDegradeThreshold_Type()
)
wdmIfSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmIfSignalDegradeThreshold.setStatus("current")


class _WdmIfTrxThresholdOptimizationState_Type(Integer32):
    """Custom type wdmIfTrxThresholdOptimizationState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("searching", 2),
          ("optimizing", 3),
          ("steadyState", 4),
          ("failedTrafficLoss", 5),
          ("failedLOS", 6))
    )


_WdmIfTrxThresholdOptimizationState_Type.__name__ = "Integer32"
_WdmIfTrxThresholdOptimizationState_Object = MibTableColumn
wdmIfTrxThresholdOptimizationState = _WdmIfTrxThresholdOptimizationState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 118),
    _WdmIfTrxThresholdOptimizationState_Type()
)
wdmIfTrxThresholdOptimizationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxThresholdOptimizationState.setStatus("current")


class _WdmIfTrxDecisionThreshold_Type(Integer32):
    """Custom type wdmIfTrxDecisionThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WdmIfTrxDecisionThreshold_Type.__name__ = "Integer32"
_WdmIfTrxDecisionThreshold_Object = MibTableColumn
wdmIfTrxDecisionThreshold = _WdmIfTrxDecisionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 119),
    _WdmIfTrxDecisionThreshold_Type()
)
wdmIfTrxDecisionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfTrxDecisionThreshold.setStatus("current")


class _WdmIfSwControlledLaserShutdown_Type(Integer32):
    """Custom type wdmIfSwControlledLaserShutdown based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WdmIfSwControlledLaserShutdown_Type.__name__ = "Integer32"
_WdmIfSwControlledLaserShutdown_Object = MibTableColumn
wdmIfSwControlledLaserShutdown = _WdmIfSwControlledLaserShutdown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 120),
    _WdmIfSwControlledLaserShutdown_Type()
)
wdmIfSwControlledLaserShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfSwControlledLaserShutdown.setStatus("current")
_WdmIfChangeSwControlledLaserShutdownCommand_Type = CommandString
_WdmIfChangeSwControlledLaserShutdownCommand_Object = MibTableColumn
wdmIfChangeSwControlledLaserShutdownCommand = _WdmIfChangeSwControlledLaserShutdownCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 121),
    _WdmIfChangeSwControlledLaserShutdownCommand_Type()
)
wdmIfChangeSwControlledLaserShutdownCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfChangeSwControlledLaserShutdownCommand.setStatus("current")
_WdmIfControlledLaserShutdownEnabled_Type = FaultStatus
_WdmIfControlledLaserShutdownEnabled_Object = MibTableColumn
wdmIfControlledLaserShutdownEnabled = _WdmIfControlledLaserShutdownEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 122),
    _WdmIfControlledLaserShutdownEnabled_Type()
)
wdmIfControlledLaserShutdownEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfControlledLaserShutdownEnabled.setStatus("current")
_WdmIfAid_Type = DisplayString
_WdmIfAid_Object = MibTableColumn
wdmIfAid = _WdmIfAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 123),
    _WdmIfAid_Type()
)
wdmIfAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfAid.setStatus("current")
_WdmIfPhysicalLocation_Type = DisplayString
_WdmIfPhysicalLocation_Object = MibTableColumn
wdmIfPhysicalLocation = _WdmIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 2, 1, 1, 124),
    _WdmIfPhysicalLocation_Type()
)
wdmIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmIfPhysicalLocation.setStatus("current")
_WdmProtList_ObjectIdentity = ObjectIdentity
wdmProtList = _WdmProtList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3)
)
_WdmProtTable_Object = MibTable
wdmProtTable = _WdmProtTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wdmProtTable.setStatus("current")
_WdmProtEntry_Object = MibTableRow
wdmProtEntry = _WdmProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1)
)
wdmProtEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmProtIndex"),
)
if mibBuilder.loadTexts:
    wdmProtEntry.setStatus("current")


class _WdmProtIndex_Type(Unsigned32):
    """Custom type wdmProtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmProtIndex_Type.__name__ = "Unsigned32"
_WdmProtIndex_Object = MibTableColumn
wdmProtIndex = _WdmProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 1),
    _WdmProtIndex_Type()
)
wdmProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtIndex.setStatus("current")


class _WdmProtName_Type(MgmtNameString):
    """Custom type wdmProtName based on MgmtNameString"""
    defaultValue = OctetString("")


_WdmProtName_Type.__name__ = "MgmtNameString"
_WdmProtName_Object = MibTableColumn
wdmProtName = _WdmProtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 2),
    _WdmProtName_Type()
)
wdmProtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtName.setStatus("current")


class _WdmProtDescr_Type(DisplayString):
    """Custom type wdmProtDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmProtDescr_Type.__name__ = "DisplayString"
_WdmProtDescr_Object = MibTableColumn
wdmProtDescr = _WdmProtDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 3),
    _WdmProtDescr_Type()
)
wdmProtDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtDescr.setStatus("current")


class _WdmProtRightSubrack_Type(SubrackNumber):
    """Custom type wdmProtRightSubrack based on SubrackNumber"""
    defaultValue = 0


_WdmProtRightSubrack_Type.__name__ = "SubrackNumber"
_WdmProtRightSubrack_Object = MibTableColumn
wdmProtRightSubrack = _WdmProtRightSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 4),
    _WdmProtRightSubrack_Type()
)
wdmProtRightSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRightSubrack.setStatus("current")


class _WdmProtRightSlot_Type(SlotNumber):
    """Custom type wdmProtRightSlot based on SlotNumber"""
    defaultValue = 0


_WdmProtRightSlot_Type.__name__ = "SlotNumber"
_WdmProtRightSlot_Object = MibTableColumn
wdmProtRightSlot = _WdmProtRightSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 5),
    _WdmProtRightSlot_Type()
)
wdmProtRightSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRightSlot.setStatus("current")


class _WdmProtRightPort_Type(PortNumber):
    """Custom type wdmProtRightPort based on PortNumber"""
    defaultValue = 0


_WdmProtRightPort_Type.__name__ = "PortNumber"
_WdmProtRightPort_Object = MibTableColumn
wdmProtRightPort = _WdmProtRightPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 6),
    _WdmProtRightPort_Type()
)
wdmProtRightPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRightPort.setStatus("current")


class _WdmProtLeftSubrack_Type(SubrackNumber):
    """Custom type wdmProtLeftSubrack based on SubrackNumber"""
    defaultValue = 0


_WdmProtLeftSubrack_Type.__name__ = "SubrackNumber"
_WdmProtLeftSubrack_Object = MibTableColumn
wdmProtLeftSubrack = _WdmProtLeftSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 7),
    _WdmProtLeftSubrack_Type()
)
wdmProtLeftSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtLeftSubrack.setStatus("current")


class _WdmProtLeftSlot_Type(SlotNumber):
    """Custom type wdmProtLeftSlot based on SlotNumber"""
    defaultValue = 0


_WdmProtLeftSlot_Type.__name__ = "SlotNumber"
_WdmProtLeftSlot_Object = MibTableColumn
wdmProtLeftSlot = _WdmProtLeftSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 8),
    _WdmProtLeftSlot_Type()
)
wdmProtLeftSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtLeftSlot.setStatus("current")


class _WdmProtLeftPort_Type(PortNumber):
    """Custom type wdmProtLeftPort based on PortNumber"""
    defaultValue = 0


_WdmProtLeftPort_Type.__name__ = "PortNumber"
_WdmProtLeftPort_Object = MibTableColumn
wdmProtLeftPort = _WdmProtLeftPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 9),
    _WdmProtLeftPort_Type()
)
wdmProtLeftPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtLeftPort.setStatus("current")
_WdmProtLastChangeTime_Type = DateAndTime
_WdmProtLastChangeTime_Object = MibTableColumn
wdmProtLastChangeTime = _WdmProtLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 10),
    _WdmProtLastChangeTime_Type()
)
wdmProtLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtLastChangeTime.setStatus("current")


class _WdmProtAdminStatus_Type(Integer32):
    """Custom type wdmProtAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("leftForced", 2),
          ("rightForced", 3),
          ("auto", 4),
          ("toggle", 5))
    )


_WdmProtAdminStatus_Type.__name__ = "Integer32"
_WdmProtAdminStatus_Object = MibTableColumn
wdmProtAdminStatus = _WdmProtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 11),
    _WdmProtAdminStatus_Type()
)
wdmProtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtAdminStatus.setStatus("current")


class _WdmProtOperStatus_Type(Integer32):
    """Custom type wdmProtOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bothDown", 1),
          ("leftDownRightUp", 2),
          ("leftDownRightStandby", 3),
          ("leftStandbyRightDown", 4),
          ("leftStandbyRightUp", 5),
          ("leftUpRightDown", 6),
          ("leftUpRightStandby", 7))
    )


_WdmProtOperStatus_Type.__name__ = "Integer32"
_WdmProtOperStatus_Object = MibTableColumn
wdmProtOperStatus = _WdmProtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 12),
    _WdmProtOperStatus_Type()
)
wdmProtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtOperStatus.setStatus("deprecated")
_WdmProtRowStatus_Type = RowStatus
_WdmProtRowStatus_Object = MibTableColumn
wdmProtRowStatus = _WdmProtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 13),
    _WdmProtRowStatus_Type()
)
wdmProtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRowStatus.setStatus("current")
_WdmProtServiceDegraded_Type = FaultStatus
_WdmProtServiceDegraded_Object = MibTableColumn
wdmProtServiceDegraded = _WdmProtServiceDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 14),
    _WdmProtServiceDegraded_Type()
)
wdmProtServiceDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtServiceDegraded.setStatus("current")
_WdmProtServiceFailure_Type = FaultStatus
_WdmProtServiceFailure_Object = MibTableColumn
wdmProtServiceFailure = _WdmProtServiceFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 15),
    _WdmProtServiceFailure_Type()
)
wdmProtServiceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtServiceFailure.setStatus("current")


class _WdmProtActiveSide_Type(Integer32):
    """Custom type wdmProtActiveSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("left", 2),
          ("right", 3))
    )


_WdmProtActiveSide_Type.__name__ = "Integer32"
_WdmProtActiveSide_Object = MibTableColumn
wdmProtActiveSide = _WdmProtActiveSide_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 16),
    _WdmProtActiveSide_Type()
)
wdmProtActiveSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtActiveSide.setStatus("current")


class _WdmProtLeftStatus_Type(Integer32):
    """Custom type wdmProtLeftStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WdmProtLeftStatus_Type.__name__ = "Integer32"
_WdmProtLeftStatus_Object = MibTableColumn
wdmProtLeftStatus = _WdmProtLeftStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 17),
    _WdmProtLeftStatus_Type()
)
wdmProtLeftStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtLeftStatus.setStatus("current")


class _WdmProtRightStatus_Type(Integer32):
    """Custom type wdmProtRightStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WdmProtRightStatus_Type.__name__ = "Integer32"
_WdmProtRightStatus_Object = MibTableColumn
wdmProtRightStatus = _WdmProtRightStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 18),
    _WdmProtRightStatus_Type()
)
wdmProtRightStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtRightStatus.setStatus("current")


class _WdmProtProtectionType_Type(Integer32):
    """Custom type wdmProtProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eqAndFiberProtection", 0),
          ("fiberProtectionI", 1),
          ("fiberProtectionII", 2),
          ("fiberProtectionIII", 3),
          ("fiberProtectionIIII", 4),
          ("singleEndedBiDirLineProtection", 5))
    )


_WdmProtProtectionType_Type.__name__ = "Integer32"
_WdmProtProtectionType_Object = MibTableColumn
wdmProtProtectionType = _WdmProtProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 19),
    _WdmProtProtectionType_Type()
)
wdmProtProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtProtectionType.setStatus("current")
_WdmProtObjectProperty_Type = ObjectProperty
_WdmProtObjectProperty_Object = MibTableColumn
wdmProtObjectProperty = _WdmProtObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 20),
    _WdmProtObjectProperty_Type()
)
wdmProtObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtObjectProperty.setStatus("current")


class _WdmProtWrapperMode_Type(Integer32):
    """Custom type wdmProtWrapperMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followTraffic", 1),
          ("fixedToDefault", 2))
    )


_WdmProtWrapperMode_Type.__name__ = "Integer32"
_WdmProtWrapperMode_Object = MibTableColumn
wdmProtWrapperMode = _WdmProtWrapperMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 21),
    _WdmProtWrapperMode_Type()
)
wdmProtWrapperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtWrapperMode.setStatus("current")


class _WdmProtWrapperState_Type(Integer32):
    """Custom type wdmProtWrapperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("left", 2),
          ("right", 3))
    )


_WdmProtWrapperState_Type.__name__ = "Integer32"
_WdmProtWrapperState_Object = MibTableColumn
wdmProtWrapperState = _WdmProtWrapperState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 22),
    _WdmProtWrapperState_Type()
)
wdmProtWrapperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtWrapperState.setStatus("current")


class _WdmProtLeftCommSubrack_Type(SubrackNumber):
    """Custom type wdmProtLeftCommSubrack based on SubrackNumber"""
    defaultValue = 0


_WdmProtLeftCommSubrack_Type.__name__ = "SubrackNumber"
_WdmProtLeftCommSubrack_Object = MibTableColumn
wdmProtLeftCommSubrack = _WdmProtLeftCommSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 23),
    _WdmProtLeftCommSubrack_Type()
)
wdmProtLeftCommSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtLeftCommSubrack.setStatus("current")


class _WdmProtLeftCommSlot_Type(SlotNumber):
    """Custom type wdmProtLeftCommSlot based on SlotNumber"""
    defaultValue = 0


_WdmProtLeftCommSlot_Type.__name__ = "SlotNumber"
_WdmProtLeftCommSlot_Object = MibTableColumn
wdmProtLeftCommSlot = _WdmProtLeftCommSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 24),
    _WdmProtLeftCommSlot_Type()
)
wdmProtLeftCommSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtLeftCommSlot.setStatus("current")


class _WdmProtLeftCommPort_Type(PortNumber):
    """Custom type wdmProtLeftCommPort based on PortNumber"""
    defaultValue = 0


_WdmProtLeftCommPort_Type.__name__ = "PortNumber"
_WdmProtLeftCommPort_Object = MibTableColumn
wdmProtLeftCommPort = _WdmProtLeftCommPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 25),
    _WdmProtLeftCommPort_Type()
)
wdmProtLeftCommPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtLeftCommPort.setStatus("current")


class _WdmProtRightCommSubrack_Type(SubrackNumber):
    """Custom type wdmProtRightCommSubrack based on SubrackNumber"""
    defaultValue = 0


_WdmProtRightCommSubrack_Type.__name__ = "SubrackNumber"
_WdmProtRightCommSubrack_Object = MibTableColumn
wdmProtRightCommSubrack = _WdmProtRightCommSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 26),
    _WdmProtRightCommSubrack_Type()
)
wdmProtRightCommSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRightCommSubrack.setStatus("current")


class _WdmProtRightCommSlot_Type(SlotNumber):
    """Custom type wdmProtRightCommSlot based on SlotNumber"""
    defaultValue = 0


_WdmProtRightCommSlot_Type.__name__ = "SlotNumber"
_WdmProtRightCommSlot_Object = MibTableColumn
wdmProtRightCommSlot = _WdmProtRightCommSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 27),
    _WdmProtRightCommSlot_Type()
)
wdmProtRightCommSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRightCommSlot.setStatus("current")


class _WdmProtRightCommPort_Type(PortNumber):
    """Custom type wdmProtRightCommPort based on PortNumber"""
    defaultValue = 0


_WdmProtRightCommPort_Type.__name__ = "PortNumber"
_WdmProtRightCommPort_Object = MibTableColumn
wdmProtRightCommPort = _WdmProtRightCommPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 28),
    _WdmProtRightCommPort_Type()
)
wdmProtRightCommPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmProtRightCommPort.setStatus("current")
_WdmProtLeftCommInterface_Type = DisplayString
_WdmProtLeftCommInterface_Object = MibTableColumn
wdmProtLeftCommInterface = _WdmProtLeftCommInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 29),
    _WdmProtLeftCommInterface_Type()
)
wdmProtLeftCommInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtLeftCommInterface.setStatus("current")
_WdmProtRightCommInterface_Type = DisplayString
_WdmProtRightCommInterface_Object = MibTableColumn
wdmProtRightCommInterface = _WdmProtRightCommInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 30),
    _WdmProtRightCommInterface_Type()
)
wdmProtRightCommInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtRightCommInterface.setStatus("current")
_WdmProtCommunicationFailure_Type = FaultStatus
_WdmProtCommunicationFailure_Object = MibTableColumn
wdmProtCommunicationFailure = _WdmProtCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 31),
    _WdmProtCommunicationFailure_Type()
)
wdmProtCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtCommunicationFailure.setStatus("current")
_WdmProtHubTrafficConfigMismatch_Type = FaultStatus
_WdmProtHubTrafficConfigMismatch_Object = MibTableColumn
wdmProtHubTrafficConfigMismatch = _WdmProtHubTrafficConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 32),
    _WdmProtHubTrafficConfigMismatch_Type()
)
wdmProtHubTrafficConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtHubTrafficConfigMismatch.setStatus("current")


class _WdmProtSignalDegradeProtection_Type(Integer32):
    """Custom type wdmProtSignalDegradeProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WdmProtSignalDegradeProtection_Type.__name__ = "Integer32"
_WdmProtSignalDegradeProtection_Object = MibTableColumn
wdmProtSignalDegradeProtection = _WdmProtSignalDegradeProtection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 33),
    _WdmProtSignalDegradeProtection_Type()
)
wdmProtSignalDegradeProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtSignalDegradeProtection.setStatus("current")


class _WdmProtRevertiveSwitchWtrTimer_Type(Unsigned32):
    """Custom type wdmProtRevertiveSwitchWtrTimer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_WdmProtRevertiveSwitchWtrTimer_Type.__name__ = "Unsigned32"
_WdmProtRevertiveSwitchWtrTimer_Object = MibTableColumn
wdmProtRevertiveSwitchWtrTimer = _WdmProtRevertiveSwitchWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 34),
    _WdmProtRevertiveSwitchWtrTimer_Type()
)
wdmProtRevertiveSwitchWtrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtRevertiveSwitchWtrTimer.setStatus("current")


class _WdmProtRevertiveSwitch_Type(Integer32):
    """Custom type wdmProtRevertiveSwitch based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WdmProtRevertiveSwitch_Type.__name__ = "Integer32"
_WdmProtRevertiveSwitch_Object = MibTableColumn
wdmProtRevertiveSwitch = _WdmProtRevertiveSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 35),
    _WdmProtRevertiveSwitch_Type()
)
wdmProtRevertiveSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtRevertiveSwitch.setStatus("current")


class _WdmProtRevertiveSwitchPrimaryPath_Type(Integer32):
    """Custom type wdmProtRevertiveSwitchPrimaryPath based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("left", 2),
          ("right", 3))
    )


_WdmProtRevertiveSwitchPrimaryPath_Type.__name__ = "Integer32"
_WdmProtRevertiveSwitchPrimaryPath_Object = MibTableColumn
wdmProtRevertiveSwitchPrimaryPath = _WdmProtRevertiveSwitchPrimaryPath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 36),
    _WdmProtRevertiveSwitchPrimaryPath_Type()
)
wdmProtRevertiveSwitchPrimaryPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmProtRevertiveSwitchPrimaryPath.setStatus("current")


class _WdmProtRevertiveSwitchSecondaryPath_Type(Integer32):
    """Custom type wdmProtRevertiveSwitchSecondaryPath based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("left", 2),
          ("right", 3))
    )


_WdmProtRevertiveSwitchSecondaryPath_Type.__name__ = "Integer32"
_WdmProtRevertiveSwitchSecondaryPath_Object = MibTableColumn
wdmProtRevertiveSwitchSecondaryPath = _WdmProtRevertiveSwitchSecondaryPath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 37),
    _WdmProtRevertiveSwitchSecondaryPath_Type()
)
wdmProtRevertiveSwitchSecondaryPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtRevertiveSwitchSecondaryPath.setStatus("current")
_WdmProtSecondaryPathUsed_Type = FaultStatus
_WdmProtSecondaryPathUsed_Object = MibTableColumn
wdmProtSecondaryPathUsed = _WdmProtSecondaryPathUsed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 3, 1, 1, 38),
    _WdmProtSecondaryPathUsed_Type()
)
wdmProtSecondaryPathUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmProtSecondaryPathUsed.setStatus("current")
_LumentisWdmNotifications_ObjectIdentity = ObjectIdentity
lumentisWdmNotifications = _LumentisWdmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4)
)
_WdmNotifyPrefix_ObjectIdentity = ObjectIdentity
wdmNotifyPrefix = _WdmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0)
)
_WdmPassiveIfList_ObjectIdentity = ObjectIdentity
wdmPassiveIfList = _WdmPassiveIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5)
)
_WdmPassiveIfTable_Object = MibTable
wdmPassiveIfTable = _WdmPassiveIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    wdmPassiveIfTable.setStatus("current")
_WdmPassiveIfEntry_Object = MibTableRow
wdmPassiveIfEntry = _WdmPassiveIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1)
)
wdmPassiveIfEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmPassiveIfIndex"),
)
if mibBuilder.loadTexts:
    wdmPassiveIfEntry.setStatus("current")


class _WdmPassiveIfIndex_Type(Unsigned32):
    """Custom type wdmPassiveIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmPassiveIfIndex_Type.__name__ = "Unsigned32"
_WdmPassiveIfIndex_Object = MibTableColumn
wdmPassiveIfIndex = _WdmPassiveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 1),
    _WdmPassiveIfIndex_Type()
)
wdmPassiveIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfIndex.setStatus("current")
_WdmPassiveIfName_Type = MgmtNameString
_WdmPassiveIfName_Object = MibTableColumn
wdmPassiveIfName = _WdmPassiveIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 2),
    _WdmPassiveIfName_Type()
)
wdmPassiveIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfName.setStatus("current")


class _WdmPassiveIfDescr_Type(DisplayString):
    """Custom type wdmPassiveIfDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmPassiveIfDescr_Type.__name__ = "DisplayString"
_WdmPassiveIfDescr_Object = MibTableColumn
wdmPassiveIfDescr = _WdmPassiveIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 3),
    _WdmPassiveIfDescr_Type()
)
wdmPassiveIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmPassiveIfDescr.setStatus("current")
_WdmPassiveIfSubrack_Type = SubrackNumber
_WdmPassiveIfSubrack_Object = MibTableColumn
wdmPassiveIfSubrack = _WdmPassiveIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 5),
    _WdmPassiveIfSubrack_Type()
)
wdmPassiveIfSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfSubrack.setStatus("current")
_WdmPassiveIfSlot_Type = SlotNumber
_WdmPassiveIfSlot_Object = MibTableColumn
wdmPassiveIfSlot = _WdmPassiveIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 6),
    _WdmPassiveIfSlot_Type()
)
wdmPassiveIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfSlot.setStatus("current")
_WdmPassiveIfPort_Type = PortNumber
_WdmPassiveIfPort_Object = MibTableColumn
wdmPassiveIfPort = _WdmPassiveIfPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 7),
    _WdmPassiveIfPort_Type()
)
wdmPassiveIfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfPort.setStatus("current")


class _WdmPassiveIfInvPhysIndexOrZero_Type(Unsigned32):
    """Custom type wdmPassiveIfInvPhysIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WdmPassiveIfInvPhysIndexOrZero_Type.__name__ = "Unsigned32"
_WdmPassiveIfInvPhysIndexOrZero_Object = MibTableColumn
wdmPassiveIfInvPhysIndexOrZero = _WdmPassiveIfInvPhysIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 8),
    _WdmPassiveIfInvPhysIndexOrZero_Type()
)
wdmPassiveIfInvPhysIndexOrZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfInvPhysIndexOrZero.setStatus("current")
_WdmPassiveIfDirection_Type = PortType
_WdmPassiveIfDirection_Object = MibTableColumn
wdmPassiveIfDirection = _WdmPassiveIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 9),
    _WdmPassiveIfDirection_Type()
)
wdmPassiveIfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfDirection.setStatus("current")
_WdmPassiveIfLambdaType_Type = LambdaType
_WdmPassiveIfLambdaType_Object = MibTableColumn
wdmPassiveIfLambdaType = _WdmPassiveIfLambdaType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 10),
    _WdmPassiveIfLambdaType_Type()
)
wdmPassiveIfLambdaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfLambdaType.setStatus("current")
_WdmPassiveIfLambda_Type = LambdaFrequency
_WdmPassiveIfLambda_Object = MibTableColumn
wdmPassiveIfLambda = _WdmPassiveIfLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 11),
    _WdmPassiveIfLambda_Type()
)
wdmPassiveIfLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfLambda.setStatus("current")
_WdmPassiveIfLambdaMax_Type = LambdaFrequency
_WdmPassiveIfLambdaMax_Object = MibTableColumn
wdmPassiveIfLambdaMax = _WdmPassiveIfLambdaMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 12),
    _WdmPassiveIfLambdaMax_Type()
)
wdmPassiveIfLambdaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfLambdaMax.setStatus("current")
_WdmPassiveIfLastChangeTime_Type = DateAndTime
_WdmPassiveIfLastChangeTime_Object = MibTableColumn
wdmPassiveIfLastChangeTime = _WdmPassiveIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 13),
    _WdmPassiveIfLastChangeTime_Type()
)
wdmPassiveIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfLastChangeTime.setStatus("deprecated")


class _WdmPassiveIfExpectedLambda_Type(LambdaFrequency):
    """Custom type wdmPassiveIfExpectedLambda based on LambdaFrequency"""
    defaultValue = 0


_WdmPassiveIfExpectedLambda_Type.__name__ = "LambdaFrequency"
_WdmPassiveIfExpectedLambda_Object = MibTableColumn
wdmPassiveIfExpectedLambda = _WdmPassiveIfExpectedLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 14),
    _WdmPassiveIfExpectedLambda_Type()
)
wdmPassiveIfExpectedLambda.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmPassiveIfExpectedLambda.setStatus("current")
_WdmPassiveIfUnexpectedLambda_Type = FaultStatus
_WdmPassiveIfUnexpectedLambda_Object = MibTableColumn
wdmPassiveIfUnexpectedLambda = _WdmPassiveIfUnexpectedLambda_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 15),
    _WdmPassiveIfUnexpectedLambda_Type()
)
wdmPassiveIfUnexpectedLambda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfUnexpectedLambda.setStatus("current")


class _WdmPassiveIfAdminStatus_Type(Integer32):
    """Custom type wdmPassiveIfAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WdmPassiveIfAdminStatus_Type.__name__ = "Integer32"
_WdmPassiveIfAdminStatus_Object = MibTableColumn
wdmPassiveIfAdminStatus = _WdmPassiveIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 16),
    _WdmPassiveIfAdminStatus_Type()
)
wdmPassiveIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmPassiveIfAdminStatus.setStatus("current")


class _WdmPassiveIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type wdmPassiveIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_WdmPassiveIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_WdmPassiveIfOperStatus_Object = MibTableColumn
wdmPassiveIfOperStatus = _WdmPassiveIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 17),
    _WdmPassiveIfOperStatus_Type()
)
wdmPassiveIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfOperStatus.setStatus("current")
_WdmPassiveIfObjectProperty_Type = ObjectProperty
_WdmPassiveIfObjectProperty_Object = MibTableColumn
wdmPassiveIfObjectProperty = _WdmPassiveIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 18),
    _WdmPassiveIfObjectProperty_Type()
)
wdmPassiveIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfObjectProperty.setStatus("current")


class _WdmPassiveIfExpectedLambdaMax_Type(LambdaFrequency):
    """Custom type wdmPassiveIfExpectedLambdaMax based on LambdaFrequency"""
    defaultValue = 0


_WdmPassiveIfExpectedLambdaMax_Type.__name__ = "LambdaFrequency"
_WdmPassiveIfExpectedLambdaMax_Object = MibTableColumn
wdmPassiveIfExpectedLambdaMax = _WdmPassiveIfExpectedLambdaMax_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 19),
    _WdmPassiveIfExpectedLambdaMax_Type()
)
wdmPassiveIfExpectedLambdaMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmPassiveIfExpectedLambdaMax.setStatus("current")
_WdmPassiveIfAid_Type = DisplayString
_WdmPassiveIfAid_Object = MibTableColumn
wdmPassiveIfAid = _WdmPassiveIfAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 20),
    _WdmPassiveIfAid_Type()
)
wdmPassiveIfAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfAid.setStatus("current")
_WdmPassiveIfPhysicalLocation_Type = DisplayString
_WdmPassiveIfPhysicalLocation_Object = MibTableColumn
wdmPassiveIfPhysicalLocation = _WdmPassiveIfPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 21),
    _WdmPassiveIfPhysicalLocation_Type()
)
wdmPassiveIfPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfPhysicalLocation.setStatus("current")
_WdmPassiveIfIfNo_Type = PortNumber
_WdmPassiveIfIfNo_Object = MibTableColumn
wdmPassiveIfIfNo = _WdmPassiveIfIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 5, 1, 1, 22),
    _WdmPassiveIfIfNo_Type()
)
wdmPassiveIfIfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmPassiveIfIfNo.setStatus("current")
_WdmVc4List_ObjectIdentity = ObjectIdentity
wdmVc4List = _WdmVc4List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6)
)
_WdmVc4Table_Object = MibTable
wdmVc4Table = _WdmVc4Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    wdmVc4Table.setStatus("current")
_WdmVc4Entry_Object = MibTableRow
wdmVc4Entry = _WdmVc4Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1)
)
wdmVc4Entry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmVc4Index"),
)
if mibBuilder.loadTexts:
    wdmVc4Entry.setStatus("current")


class _WdmVc4Index_Type(Unsigned32):
    """Custom type wdmVc4Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmVc4Index_Type.__name__ = "Unsigned32"
_WdmVc4Index_Object = MibTableColumn
wdmVc4Index = _WdmVc4Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 1),
    _WdmVc4Index_Type()
)
wdmVc4Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4Index.setStatus("current")
_WdmVc4Name_Type = MgmtNameString
_WdmVc4Name_Object = MibTableColumn
wdmVc4Name = _WdmVc4Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 2),
    _WdmVc4Name_Type()
)
wdmVc4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4Name.setStatus("current")


class _WdmVc4Descr_Type(DisplayString):
    """Custom type wdmVc4Descr based on DisplayString"""
    defaultValue = OctetString("")


_WdmVc4Descr_Type.__name__ = "DisplayString"
_WdmVc4Descr_Object = MibTableColumn
wdmVc4Descr = _WdmVc4Descr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 3),
    _WdmVc4Descr_Type()
)
wdmVc4Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmVc4Descr.setStatus("current")
_WdmVc4Subrack_Type = SubrackNumber
_WdmVc4Subrack_Object = MibTableColumn
wdmVc4Subrack = _WdmVc4Subrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 4),
    _WdmVc4Subrack_Type()
)
wdmVc4Subrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4Subrack.setStatus("current")
_WdmVc4Slot_Type = SlotNumber
_WdmVc4Slot_Object = MibTableColumn
wdmVc4Slot = _WdmVc4Slot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 5),
    _WdmVc4Slot_Type()
)
wdmVc4Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4Slot.setStatus("current")
_WdmVc4TxPort_Type = PortNumber
_WdmVc4TxPort_Object = MibTableColumn
wdmVc4TxPort = _WdmVc4TxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 6),
    _WdmVc4TxPort_Type()
)
wdmVc4TxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4TxPort.setStatus("current")
_WdmVc4RxPort_Type = PortNumber
_WdmVc4RxPort_Object = MibTableColumn
wdmVc4RxPort = _WdmVc4RxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 7),
    _WdmVc4RxPort_Type()
)
wdmVc4RxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4RxPort.setStatus("current")


class _WdmVc4Vc4_Type(Unsigned32):
    """Custom type wdmVc4Vc4 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WdmVc4Vc4_Type.__name__ = "Unsigned32"
_WdmVc4Vc4_Object = MibTableColumn
wdmVc4Vc4 = _WdmVc4Vc4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 8),
    _WdmVc4Vc4_Type()
)
wdmVc4Vc4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4Vc4.setStatus("current")
_WdmVc4ObjectProperty_Type = ObjectProperty
_WdmVc4ObjectProperty_Object = MibTableColumn
wdmVc4ObjectProperty = _WdmVc4ObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 9),
    _WdmVc4ObjectProperty_Type()
)
wdmVc4ObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4ObjectProperty.setStatus("current")


class _WdmVc4AuAlarmIndicationSignal_Type(Integer32):
    """Custom type wdmVc4AuAlarmIndicationSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_WdmVc4AuAlarmIndicationSignal_Type.__name__ = "Integer32"
_WdmVc4AuAlarmIndicationSignal_Object = MibTableColumn
wdmVc4AuAlarmIndicationSignal = _WdmVc4AuAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 10),
    _WdmVc4AuAlarmIndicationSignal_Type()
)
wdmVc4AuAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4AuAlarmIndicationSignal.setStatus("current")


class _WdmVc4AuLossOfPointer_Type(Integer32):
    """Custom type wdmVc4AuLossOfPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("alarm", 2))
    )


_WdmVc4AuLossOfPointer_Type.__name__ = "Integer32"
_WdmVc4AuLossOfPointer_Object = MibTableColumn
wdmVc4AuLossOfPointer = _WdmVc4AuLossOfPointer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 11),
    _WdmVc4AuLossOfPointer_Type()
)
wdmVc4AuLossOfPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4AuLossOfPointer.setStatus("current")


class _WdmVc4RxSignalStatus_Type(Integer32):
    """Custom type wdmVc4RxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_WdmVc4RxSignalStatus_Type.__name__ = "Integer32"
_WdmVc4RxSignalStatus_Object = MibTableColumn
wdmVc4RxSignalStatus = _WdmVc4RxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 12),
    _WdmVc4RxSignalStatus_Type()
)
wdmVc4RxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4RxSignalStatus.setStatus("current")


class _WdmVc4ConcatenationStatus_Type(Integer32):
    """Custom type wdmVc4ConcatenationStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("vc3", 3),
          ("vc4", 4),
          ("vc4x4c", 5),
          ("vc4x16c", 6),
          ("vc4x64c", 7),
          ("sts1", 8),
          ("sts3c", 9),
          ("sts12c", 10),
          ("unknown", 11))
    )


_WdmVc4ConcatenationStatus_Type.__name__ = "Integer32"
_WdmVc4ConcatenationStatus_Object = MibTableColumn
wdmVc4ConcatenationStatus = _WdmVc4ConcatenationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 13),
    _WdmVc4ConcatenationStatus_Type()
)
wdmVc4ConcatenationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4ConcatenationStatus.setStatus("current")


class _WdmVc4PayloadStatus_Type(Integer32):
    """Custom type wdmVc4PayloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 1),
          ("unequipped", 2))
    )


_WdmVc4PayloadStatus_Type.__name__ = "Integer32"
_WdmVc4PayloadStatus_Object = MibTableColumn
wdmVc4PayloadStatus = _WdmVc4PayloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 14),
    _WdmVc4PayloadStatus_Type()
)
wdmVc4PayloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4PayloadStatus.setStatus("current")


class _WdmVc4ConnectionStatus_Type(DisplayString):
    """Custom type wdmVc4ConnectionStatus based on DisplayString"""
    defaultValue = OctetString("Not connected")


_WdmVc4ConnectionStatus_Type.__name__ = "DisplayString"
_WdmVc4ConnectionStatus_Object = MibTableColumn
wdmVc4ConnectionStatus = _WdmVc4ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 15),
    _WdmVc4ConnectionStatus_Type()
)
wdmVc4ConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmVc4ConnectionStatus.setStatus("current")


class _WdmVc4ConnectedForeignIndex_Type(Unsigned32):
    """Custom type wdmVc4ConnectedForeignIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WdmVc4ConnectedForeignIndex_Type.__name__ = "Unsigned32"
_WdmVc4ConnectedForeignIndex_Object = MibTableColumn
wdmVc4ConnectedForeignIndex = _WdmVc4ConnectedForeignIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 16),
    _WdmVc4ConnectedForeignIndex_Type()
)
wdmVc4ConnectedForeignIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmVc4ConnectedForeignIndex.setStatus("current")


class _WdmVc4AdminStatus_Type(Integer32):
    """Custom type wdmVc4AdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_WdmVc4AdminStatus_Type.__name__ = "Integer32"
_WdmVc4AdminStatus_Object = MibTableColumn
wdmVc4AdminStatus = _WdmVc4AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 6, 1, 1, 17),
    _WdmVc4AdminStatus_Type()
)
wdmVc4AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmVc4AdminStatus.setStatus("current")
_WdmRemoteProtList_ObjectIdentity = ObjectIdentity
wdmRemoteProtList = _WdmRemoteProtList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7)
)
_WdmRemoteProtTable_Object = MibTable
wdmRemoteProtTable = _WdmRemoteProtTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1)
)
if mibBuilder.loadTexts:
    wdmRemoteProtTable.setStatus("current")
_WdmRemoteProtEntry_Object = MibTableRow
wdmRemoteProtEntry = _WdmRemoteProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1)
)
wdmRemoteProtEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmRemoteProtIndex"),
)
if mibBuilder.loadTexts:
    wdmRemoteProtEntry.setStatus("current")


class _WdmRemoteProtIndex_Type(Unsigned32):
    """Custom type wdmRemoteProtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmRemoteProtIndex_Type.__name__ = "Unsigned32"
_WdmRemoteProtIndex_Object = MibTableColumn
wdmRemoteProtIndex = _WdmRemoteProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 1),
    _WdmRemoteProtIndex_Type()
)
wdmRemoteProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtIndex.setStatus("current")


class _WdmRemoteProtName_Type(MgmtNameString):
    """Custom type wdmRemoteProtName based on MgmtNameString"""
    defaultValue = OctetString("")


_WdmRemoteProtName_Type.__name__ = "MgmtNameString"
_WdmRemoteProtName_Object = MibTableColumn
wdmRemoteProtName = _WdmRemoteProtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 2),
    _WdmRemoteProtName_Type()
)
wdmRemoteProtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtName.setStatus("current")


class _WdmRemoteProtDescr_Type(DisplayString):
    """Custom type wdmRemoteProtDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmRemoteProtDescr_Type.__name__ = "DisplayString"
_WdmRemoteProtDescr_Object = MibTableColumn
wdmRemoteProtDescr = _WdmRemoteProtDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 3),
    _WdmRemoteProtDescr_Type()
)
wdmRemoteProtDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmRemoteProtDescr.setStatus("current")


class _WdmRemoteProtLocalSubrack_Type(SubrackNumber):
    """Custom type wdmRemoteProtLocalSubrack based on SubrackNumber"""
    defaultValue = 0


_WdmRemoteProtLocalSubrack_Type.__name__ = "SubrackNumber"
_WdmRemoteProtLocalSubrack_Object = MibTableColumn
wdmRemoteProtLocalSubrack = _WdmRemoteProtLocalSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 4),
    _WdmRemoteProtLocalSubrack_Type()
)
wdmRemoteProtLocalSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtLocalSubrack.setStatus("current")


class _WdmRemoteProtLocalSlot_Type(SlotNumber):
    """Custom type wdmRemoteProtLocalSlot based on SlotNumber"""
    defaultValue = 0


_WdmRemoteProtLocalSlot_Type.__name__ = "SlotNumber"
_WdmRemoteProtLocalSlot_Object = MibTableColumn
wdmRemoteProtLocalSlot = _WdmRemoteProtLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 5),
    _WdmRemoteProtLocalSlot_Type()
)
wdmRemoteProtLocalSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtLocalSlot.setStatus("current")


class _WdmRemoteProtLocalPort_Type(PortNumber):
    """Custom type wdmRemoteProtLocalPort based on PortNumber"""
    defaultValue = 0


_WdmRemoteProtLocalPort_Type.__name__ = "PortNumber"
_WdmRemoteProtLocalPort_Object = MibTableColumn
wdmRemoteProtLocalPort = _WdmRemoteProtLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 6),
    _WdmRemoteProtLocalPort_Type()
)
wdmRemoteProtLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtLocalPort.setStatus("current")


class _WdmRemoteProtCommSubrack_Type(SubrackNumber):
    """Custom type wdmRemoteProtCommSubrack based on SubrackNumber"""
    defaultValue = 0


_WdmRemoteProtCommSubrack_Type.__name__ = "SubrackNumber"
_WdmRemoteProtCommSubrack_Object = MibTableColumn
wdmRemoteProtCommSubrack = _WdmRemoteProtCommSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 7),
    _WdmRemoteProtCommSubrack_Type()
)
wdmRemoteProtCommSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtCommSubrack.setStatus("current")


class _WdmRemoteProtCommSlot_Type(SlotNumber):
    """Custom type wdmRemoteProtCommSlot based on SlotNumber"""
    defaultValue = 0


_WdmRemoteProtCommSlot_Type.__name__ = "SlotNumber"
_WdmRemoteProtCommSlot_Object = MibTableColumn
wdmRemoteProtCommSlot = _WdmRemoteProtCommSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 8),
    _WdmRemoteProtCommSlot_Type()
)
wdmRemoteProtCommSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtCommSlot.setStatus("current")


class _WdmRemoteProtCommPort_Type(PortNumber):
    """Custom type wdmRemoteProtCommPort based on PortNumber"""
    defaultValue = 0


_WdmRemoteProtCommPort_Type.__name__ = "PortNumber"
_WdmRemoteProtCommPort_Object = MibTableColumn
wdmRemoteProtCommPort = _WdmRemoteProtCommPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 9),
    _WdmRemoteProtCommPort_Type()
)
wdmRemoteProtCommPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtCommPort.setStatus("current")
_WdmRemoteProtCommInterface_Type = DisplayString
_WdmRemoteProtCommInterface_Object = MibTableColumn
wdmRemoteProtCommInterface = _WdmRemoteProtCommInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 10),
    _WdmRemoteProtCommInterface_Type()
)
wdmRemoteProtCommInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtCommInterface.setStatus("current")
_WdmRemoteProtLastChangeTime_Type = DateAndTime
_WdmRemoteProtLastChangeTime_Object = MibTableColumn
wdmRemoteProtLastChangeTime = _WdmRemoteProtLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 11),
    _WdmRemoteProtLastChangeTime_Type()
)
wdmRemoteProtLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtLastChangeTime.setStatus("current")


class _WdmRemoteProtIpAddress_Type(IpAddress):
    """Custom type wdmRemoteProtIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_WdmRemoteProtIpAddress_Type.__name__ = "IpAddress"
_WdmRemoteProtIpAddress_Object = MibTableColumn
wdmRemoteProtIpAddress = _WdmRemoteProtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 12),
    _WdmRemoteProtIpAddress_Type()
)
wdmRemoteProtIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtIpAddress.setStatus("current")


class _WdmRemoteProtIdentifier_Type(DisplayString):
    """Custom type wdmRemoteProtIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_WdmRemoteProtIdentifier_Type.__name__ = "DisplayString"
_WdmRemoteProtIdentifier_Object = MibTableColumn
wdmRemoteProtIdentifier = _WdmRemoteProtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 13),
    _WdmRemoteProtIdentifier_Type()
)
wdmRemoteProtIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtIdentifier.setStatus("current")


class _WdmRemoteProtRole_Type(Integer32):
    """Custom type wdmRemoteProtRole based on Integer32"""
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
        *(("undefined", 0),
          ("master", 1),
          ("slave", 2))
    )


_WdmRemoteProtRole_Type.__name__ = "Integer32"
_WdmRemoteProtRole_Object = MibTableColumn
wdmRemoteProtRole = _WdmRemoteProtRole_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 14),
    _WdmRemoteProtRole_Type()
)
wdmRemoteProtRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtRole.setStatus("current")


class _WdmRemoteProtAdminStatus_Type(Integer32):
    """Custom type wdmRemoteProtAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("localForced", 2),
          ("remoteForced", 3),
          ("auto", 4),
          ("toggle", 5))
    )


_WdmRemoteProtAdminStatus_Type.__name__ = "Integer32"
_WdmRemoteProtAdminStatus_Object = MibTableColumn
wdmRemoteProtAdminStatus = _WdmRemoteProtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 15),
    _WdmRemoteProtAdminStatus_Type()
)
wdmRemoteProtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmRemoteProtAdminStatus.setStatus("current")
_WdmRemoteProtRowStatus_Type = RowStatus
_WdmRemoteProtRowStatus_Object = MibTableColumn
wdmRemoteProtRowStatus = _WdmRemoteProtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 16),
    _WdmRemoteProtRowStatus_Type()
)
wdmRemoteProtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmRemoteProtRowStatus.setStatus("current")


class _WdmRemoteProtActiveSide_Type(Integer32):
    """Custom type wdmRemoteProtActiveSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("local", 2),
          ("remote", 3))
    )


_WdmRemoteProtActiveSide_Type.__name__ = "Integer32"
_WdmRemoteProtActiveSide_Object = MibTableColumn
wdmRemoteProtActiveSide = _WdmRemoteProtActiveSide_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 17),
    _WdmRemoteProtActiveSide_Type()
)
wdmRemoteProtActiveSide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtActiveSide.setStatus("current")


class _WdmRemoteProtLocalStatus_Type(Integer32):
    """Custom type wdmRemoteProtLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("down", 1),
          ("up", 2))
    )


_WdmRemoteProtLocalStatus_Type.__name__ = "Integer32"
_WdmRemoteProtLocalStatus_Object = MibTableColumn
wdmRemoteProtLocalStatus = _WdmRemoteProtLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 18),
    _WdmRemoteProtLocalStatus_Type()
)
wdmRemoteProtLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtLocalStatus.setStatus("current")


class _WdmRemoteProtRemoteStatus_Type(Integer32):
    """Custom type wdmRemoteProtRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("down", 1),
          ("up", 2))
    )


_WdmRemoteProtRemoteStatus_Type.__name__ = "Integer32"
_WdmRemoteProtRemoteStatus_Object = MibTableColumn
wdmRemoteProtRemoteStatus = _WdmRemoteProtRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 19),
    _WdmRemoteProtRemoteStatus_Type()
)
wdmRemoteProtRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtRemoteStatus.setStatus("current")
_WdmRemoteProtObjectProperty_Type = ObjectProperty
_WdmRemoteProtObjectProperty_Object = MibTableColumn
wdmRemoteProtObjectProperty = _WdmRemoteProtObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 20),
    _WdmRemoteProtObjectProperty_Type()
)
wdmRemoteProtObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtObjectProperty.setStatus("current")
_WdmRemoteProtServiceDegraded_Type = FaultStatus
_WdmRemoteProtServiceDegraded_Object = MibTableColumn
wdmRemoteProtServiceDegraded = _WdmRemoteProtServiceDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 21),
    _WdmRemoteProtServiceDegraded_Type()
)
wdmRemoteProtServiceDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtServiceDegraded.setStatus("current")
_WdmRemoteProtServiceFailure_Type = FaultStatus
_WdmRemoteProtServiceFailure_Object = MibTableColumn
wdmRemoteProtServiceFailure = _WdmRemoteProtServiceFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 22),
    _WdmRemoteProtServiceFailure_Type()
)
wdmRemoteProtServiceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtServiceFailure.setStatus("current")
_WdmRemoteProtSetup_Type = CommandString
_WdmRemoteProtSetup_Object = MibTableColumn
wdmRemoteProtSetup = _WdmRemoteProtSetup_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 23),
    _WdmRemoteProtSetup_Type()
)
wdmRemoteProtSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtSetup.setStatus("current")
_WdmRemoteProtSetupFailure_Type = FaultStatus
_WdmRemoteProtSetupFailure_Object = MibTableColumn
wdmRemoteProtSetupFailure = _WdmRemoteProtSetupFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 24),
    _WdmRemoteProtSetupFailure_Type()
)
wdmRemoteProtSetupFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtSetupFailure.setStatus("current")
_WdmRemoteProtRoleConflict_Type = FaultStatus
_WdmRemoteProtRoleConflict_Object = MibTableColumn
wdmRemoteProtRoleConflict = _WdmRemoteProtRoleConflict_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 25),
    _WdmRemoteProtRoleConflict_Type()
)
wdmRemoteProtRoleConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtRoleConflict.setStatus("current")
_WdmRemoteProtCommunicationFailure_Type = FaultStatus
_WdmRemoteProtCommunicationFailure_Object = MibTableColumn
wdmRemoteProtCommunicationFailure = _WdmRemoteProtCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 7, 1, 1, 26),
    _WdmRemoteProtCommunicationFailure_Type()
)
wdmRemoteProtCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmRemoteProtCommunicationFailure.setStatus("current")
_WdmCtrlChannelList_ObjectIdentity = ObjectIdentity
wdmCtrlChannelList = _WdmCtrlChannelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8)
)
_WdmCtrlChannelTable_Object = MibTable
wdmCtrlChannelTable = _WdmCtrlChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1)
)
if mibBuilder.loadTexts:
    wdmCtrlChannelTable.setStatus("current")
_WdmCtrlChannelEntry_Object = MibTableRow
wdmCtrlChannelEntry = _WdmCtrlChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1)
)
wdmCtrlChannelEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmCtrlChannelIndex"),
)
if mibBuilder.loadTexts:
    wdmCtrlChannelEntry.setStatus("current")


class _WdmCtrlChannelIndex_Type(Unsigned32):
    """Custom type wdmCtrlChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmCtrlChannelIndex_Type.__name__ = "Unsigned32"
_WdmCtrlChannelIndex_Object = MibTableColumn
wdmCtrlChannelIndex = _WdmCtrlChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 1),
    _WdmCtrlChannelIndex_Type()
)
wdmCtrlChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelIndex.setStatus("current")
_WdmCtrlChannelName_Type = MgmtNameString
_WdmCtrlChannelName_Object = MibTableColumn
wdmCtrlChannelName = _WdmCtrlChannelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 2),
    _WdmCtrlChannelName_Type()
)
wdmCtrlChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelName.setStatus("current")
_WdmCtrlChannelSubrack_Type = SubrackNumber
_WdmCtrlChannelSubrack_Object = MibTableColumn
wdmCtrlChannelSubrack = _WdmCtrlChannelSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 3),
    _WdmCtrlChannelSubrack_Type()
)
wdmCtrlChannelSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlChannelSubrack.setStatus("current")
_WdmCtrlChannelSlot_Type = SlotNumber
_WdmCtrlChannelSlot_Object = MibTableColumn
wdmCtrlChannelSlot = _WdmCtrlChannelSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 4),
    _WdmCtrlChannelSlot_Type()
)
wdmCtrlChannelSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlChannelSlot.setStatus("current")
_WdmCtrlChannelTxPort_Type = PortNumber
_WdmCtrlChannelTxPort_Object = MibTableColumn
wdmCtrlChannelTxPort = _WdmCtrlChannelTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 5),
    _WdmCtrlChannelTxPort_Type()
)
wdmCtrlChannelTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelTxPort.setStatus("current")


class _WdmCtrlChannelChannel_Type(LambdaFrequency):
    """Custom type wdmCtrlChannelChannel based on LambdaFrequency"""
    defaultValue = 0


_WdmCtrlChannelChannel_Type.__name__ = "LambdaFrequency"
_WdmCtrlChannelChannel_Object = MibTableColumn
wdmCtrlChannelChannel = _WdmCtrlChannelChannel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 6),
    _WdmCtrlChannelChannel_Type()
)
wdmCtrlChannelChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlChannelChannel.setStatus("current")


class _WdmCtrlChannelGroupNumber_Type(Unsigned32):
    """Custom type wdmCtrlChannelGroupNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WdmCtrlChannelGroupNumber_Type.__name__ = "Unsigned32"
_WdmCtrlChannelGroupNumber_Object = MibTableColumn
wdmCtrlChannelGroupNumber = _WdmCtrlChannelGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 7),
    _WdmCtrlChannelGroupNumber_Type()
)
wdmCtrlChannelGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlChannelGroupNumber.setStatus("current")


class _WdmCtrlChannelAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type wdmCtrlChannelAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_WdmCtrlChannelAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_WdmCtrlChannelAdminStatus_Object = MibTableColumn
wdmCtrlChannelAdminStatus = _WdmCtrlChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 8),
    _WdmCtrlChannelAdminStatus_Type()
)
wdmCtrlChannelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlChannelAdminStatus.setStatus("current")


class _WdmCtrlChannelWantedOutputPower_Type(Integer32):
    """Custom type wdmCtrlChannelWantedOutputPower based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-260, 120),
    )


_WdmCtrlChannelWantedOutputPower_Type.__name__ = "Integer32"
_WdmCtrlChannelWantedOutputPower_Object = MibTableColumn
wdmCtrlChannelWantedOutputPower = _WdmCtrlChannelWantedOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 9),
    _WdmCtrlChannelWantedOutputPower_Type()
)
wdmCtrlChannelWantedOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlChannelWantedOutputPower.setStatus("current")
_WdmCtrlChannelCurrentOutputPower_Type = Integer32
_WdmCtrlChannelCurrentOutputPower_Object = MibTableColumn
wdmCtrlChannelCurrentOutputPower = _WdmCtrlChannelCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 10),
    _WdmCtrlChannelCurrentOutputPower_Type()
)
wdmCtrlChannelCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelCurrentOutputPower.setStatus("current")
_WdmCtrlChannelCurrentAttenuation_Type = Unsigned32
_WdmCtrlChannelCurrentAttenuation_Object = MibTableColumn
wdmCtrlChannelCurrentAttenuation = _WdmCtrlChannelCurrentAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 11),
    _WdmCtrlChannelCurrentAttenuation_Type()
)
wdmCtrlChannelCurrentAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelCurrentAttenuation.setStatus("current")
_WdmCtrlChannelForceRegulationCommand_Type = CommandString
_WdmCtrlChannelForceRegulationCommand_Object = MibTableColumn
wdmCtrlChannelForceRegulationCommand = _WdmCtrlChannelForceRegulationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 12),
    _WdmCtrlChannelForceRegulationCommand_Type()
)
wdmCtrlChannelForceRegulationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelForceRegulationCommand.setStatus("current")
_WdmCtrlChannelOuputPowerControlFailure_Type = FaultStatus
_WdmCtrlChannelOuputPowerControlFailure_Object = MibTableColumn
wdmCtrlChannelOuputPowerControlFailure = _WdmCtrlChannelOuputPowerControlFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 13),
    _WdmCtrlChannelOuputPowerControlFailure_Type()
)
wdmCtrlChannelOuputPowerControlFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelOuputPowerControlFailure.setStatus("current")
_WdmCtrlChannelCurrentPowerOutOfRange_Type = FaultStatus
_WdmCtrlChannelCurrentPowerOutOfRange_Object = MibTableColumn
wdmCtrlChannelCurrentPowerOutOfRange = _WdmCtrlChannelCurrentPowerOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 14),
    _WdmCtrlChannelCurrentPowerOutOfRange_Type()
)
wdmCtrlChannelCurrentPowerOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelCurrentPowerOutOfRange.setStatus("current")
_WdmCtrlChannelAttenuationOutOfRange_Type = FaultStatus
_WdmCtrlChannelAttenuationOutOfRange_Object = MibTableColumn
wdmCtrlChannelAttenuationOutOfRange = _WdmCtrlChannelAttenuationOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 15),
    _WdmCtrlChannelAttenuationOutOfRange_Type()
)
wdmCtrlChannelAttenuationOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelAttenuationOutOfRange.setStatus("current")


class _WdmCtrlChannelStatus_Type(Integer32):
    """Custom type wdmCtrlChannelStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("searching", 2),
          ("regulating", 3),
          ("ok", 4),
          ("notFound", 5),
          ("error", 6),
          ("waiting", 7))
    )


_WdmCtrlChannelStatus_Type.__name__ = "Integer32"
_WdmCtrlChannelStatus_Object = MibTableColumn
wdmCtrlChannelStatus = _WdmCtrlChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 16),
    _WdmCtrlChannelStatus_Type()
)
wdmCtrlChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelStatus.setStatus("current")


class _WdmCtrlChannelStartupChannel_Type(Integer32):
    """Custom type wdmCtrlChannelStartupChannel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("start", 2),
          ("blocked", 3))
    )


_WdmCtrlChannelStartupChannel_Type.__name__ = "Integer32"
_WdmCtrlChannelStartupChannel_Object = MibTableColumn
wdmCtrlChannelStartupChannel = _WdmCtrlChannelStartupChannel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 17),
    _WdmCtrlChannelStartupChannel_Type()
)
wdmCtrlChannelStartupChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlChannelStartupChannel.setStatus("current")


class _WdmCtrlChannelMonitorIndex_Type(Unsigned32):
    """Custom type wdmCtrlChannelMonitorIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WdmCtrlChannelMonitorIndex_Type.__name__ = "Unsigned32"
_WdmCtrlChannelMonitorIndex_Object = MibTableColumn
wdmCtrlChannelMonitorIndex = _WdmCtrlChannelMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 18),
    _WdmCtrlChannelMonitorIndex_Type()
)
wdmCtrlChannelMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelMonitorIndex.setStatus("current")
_WdmCtrlChannelStartupCommand_Type = CommandString
_WdmCtrlChannelStartupCommand_Object = MibTableColumn
wdmCtrlChannelStartupCommand = _WdmCtrlChannelStartupCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 19),
    _WdmCtrlChannelStartupCommand_Type()
)
wdmCtrlChannelStartupCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelStartupCommand.setStatus("current")
_WdmCtrlChannelSfpMissing_Type = FaultStatus
_WdmCtrlChannelSfpMissing_Object = MibTableColumn
wdmCtrlChannelSfpMissing = _WdmCtrlChannelSfpMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 20),
    _WdmCtrlChannelSfpMissing_Type()
)
wdmCtrlChannelSfpMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelSfpMissing.setStatus("current")
_WdmCtrlChannelSfpMediaMismatch_Type = FaultStatus
_WdmCtrlChannelSfpMediaMismatch_Object = MibTableColumn
wdmCtrlChannelSfpMediaMismatch = _WdmCtrlChannelSfpMediaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 21),
    _WdmCtrlChannelSfpMediaMismatch_Type()
)
wdmCtrlChannelSfpMediaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelSfpMediaMismatch.setStatus("current")
_WdmCtrlChannelLossOfSignal_Type = FaultStatus
_WdmCtrlChannelLossOfSignal_Object = MibTableColumn
wdmCtrlChannelLossOfSignal = _WdmCtrlChannelLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 22),
    _WdmCtrlChannelLossOfSignal_Type()
)
wdmCtrlChannelLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelLossOfSignal.setStatus("current")


class _WdmCtrlChannelDescr_Type(DisplayString):
    """Custom type wdmCtrlChannelDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmCtrlChannelDescr_Type.__name__ = "DisplayString"
_WdmCtrlChannelDescr_Object = MibTableColumn
wdmCtrlChannelDescr = _WdmCtrlChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 23),
    _WdmCtrlChannelDescr_Type()
)
wdmCtrlChannelDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlChannelDescr.setStatus("current")
_WdmCtrlChannelMaxAttenuation_Type = Unsigned32
_WdmCtrlChannelMaxAttenuation_Object = MibTableColumn
wdmCtrlChannelMaxAttenuation = _WdmCtrlChannelMaxAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 24),
    _WdmCtrlChannelMaxAttenuation_Type()
)
wdmCtrlChannelMaxAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelMaxAttenuation.setStatus("current")
_WdmCtrlChannelMinAttenuation_Type = Unsigned32
_WdmCtrlChannelMinAttenuation_Object = MibTableColumn
wdmCtrlChannelMinAttenuation = _WdmCtrlChannelMinAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 25),
    _WdmCtrlChannelMinAttenuation_Type()
)
wdmCtrlChannelMinAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelMinAttenuation.setStatus("current")


class _WdmCtrlChannelAttenControlOffset_Type(Unsigned32):
    """Custom type wdmCtrlChannelAttenControlOffset based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WdmCtrlChannelAttenControlOffset_Type.__name__ = "Unsigned32"
_WdmCtrlChannelAttenControlOffset_Object = MibTableColumn
wdmCtrlChannelAttenControlOffset = _WdmCtrlChannelAttenControlOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 26),
    _WdmCtrlChannelAttenControlOffset_Type()
)
wdmCtrlChannelAttenControlOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlChannelAttenControlOffset.setStatus("current")
_WdmCtrlChannelAttenControlDegraded_Type = FaultStatus
_WdmCtrlChannelAttenControlDegraded_Object = MibTableColumn
wdmCtrlChannelAttenControlDegraded = _WdmCtrlChannelAttenControlDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 27),
    _WdmCtrlChannelAttenControlDegraded_Type()
)
wdmCtrlChannelAttenControlDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelAttenControlDegraded.setStatus("current")
_WdmCtrlChannelNotFound_Type = FaultStatus
_WdmCtrlChannelNotFound_Object = MibTableColumn
wdmCtrlChannelNotFound = _WdmCtrlChannelNotFound_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 8, 1, 1, 28),
    _WdmCtrlChannelNotFound_Type()
)
wdmCtrlChannelNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlChannelNotFound.setStatus("current")
_WdmCtrlGroupList_ObjectIdentity = ObjectIdentity
wdmCtrlGroupList = _WdmCtrlGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9)
)
_WdmCtrlGroupTable_Object = MibTable
wdmCtrlGroupTable = _WdmCtrlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1)
)
if mibBuilder.loadTexts:
    wdmCtrlGroupTable.setStatus("current")
_WdmCtrlGroupEntry_Object = MibTableRow
wdmCtrlGroupEntry = _WdmCtrlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1)
)
wdmCtrlGroupEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmCtrlGroupIndex"),
)
if mibBuilder.loadTexts:
    wdmCtrlGroupEntry.setStatus("current")


class _WdmCtrlGroupIndex_Type(Unsigned32):
    """Custom type wdmCtrlGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmCtrlGroupIndex_Type.__name__ = "Unsigned32"
_WdmCtrlGroupIndex_Object = MibTableColumn
wdmCtrlGroupIndex = _WdmCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 1),
    _WdmCtrlGroupIndex_Type()
)
wdmCtrlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupIndex.setStatus("current")
_WdmCtrlGroupName_Type = MgmtNameString
_WdmCtrlGroupName_Object = MibTableColumn
wdmCtrlGroupName = _WdmCtrlGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 2),
    _WdmCtrlGroupName_Type()
)
wdmCtrlGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupName.setStatus("current")


class _WdmCtrlGroupDescr_Type(DisplayString):
    """Custom type wdmCtrlGroupDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmCtrlGroupDescr_Type.__name__ = "DisplayString"
_WdmCtrlGroupDescr_Object = MibTableColumn
wdmCtrlGroupDescr = _WdmCtrlGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 3),
    _WdmCtrlGroupDescr_Type()
)
wdmCtrlGroupDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlGroupDescr.setStatus("current")


class _WdmCtrlGroupGroupNumber_Type(Unsigned32):
    """Custom type wdmCtrlGroupGroupNumber based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_WdmCtrlGroupGroupNumber_Type.__name__ = "Unsigned32"
_WdmCtrlGroupGroupNumber_Object = MibTableColumn
wdmCtrlGroupGroupNumber = _WdmCtrlGroupGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 4),
    _WdmCtrlGroupGroupNumber_Type()
)
wdmCtrlGroupGroupNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlGroupGroupNumber.setStatus("current")
_WdmCtrlGroupSubrack_Type = SubrackNumber
_WdmCtrlGroupSubrack_Object = MibTableColumn
wdmCtrlGroupSubrack = _WdmCtrlGroupSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 5),
    _WdmCtrlGroupSubrack_Type()
)
wdmCtrlGroupSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlGroupSubrack.setStatus("current")
_WdmCtrlGroupSlot_Type = SlotNumber
_WdmCtrlGroupSlot_Object = MibTableColumn
wdmCtrlGroupSlot = _WdmCtrlGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 6),
    _WdmCtrlGroupSlot_Type()
)
wdmCtrlGroupSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlGroupSlot.setStatus("current")


class _WdmCtrlGroupPort_Type(Integer32):
    """Custom type wdmCtrlGroupPort based on Integer32"""
    defaultValue = 1

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
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8))
    )


_WdmCtrlGroupPort_Type.__name__ = "Integer32"
_WdmCtrlGroupPort_Object = MibTableColumn
wdmCtrlGroupPort = _WdmCtrlGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 7),
    _WdmCtrlGroupPort_Type()
)
wdmCtrlGroupPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmCtrlGroupPort.setStatus("current")
_WdmCtrlGroupMonitorName_Type = MgmtNameString
_WdmCtrlGroupMonitorName_Object = MibTableColumn
wdmCtrlGroupMonitorName = _WdmCtrlGroupMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 8),
    _WdmCtrlGroupMonitorName_Type()
)
wdmCtrlGroupMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupMonitorName.setStatus("current")


class _WdmCtrlGroupAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type wdmCtrlGroupAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_WdmCtrlGroupAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_WdmCtrlGroupAdminStatus_Object = MibTableColumn
wdmCtrlGroupAdminStatus = _WdmCtrlGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 9),
    _WdmCtrlGroupAdminStatus_Type()
)
wdmCtrlGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlGroupAdminStatus.setStatus("current")


class _WdmCtrlGroupControlMode_Type(Integer32):
    """Custom type wdmCtrlGroupControlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("commissioning", 2))
    )


_WdmCtrlGroupControlMode_Type.__name__ = "Integer32"
_WdmCtrlGroupControlMode_Object = MibTableColumn
wdmCtrlGroupControlMode = _WdmCtrlGroupControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 10),
    _WdmCtrlGroupControlMode_Type()
)
wdmCtrlGroupControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupControlMode.setStatus("current")
_WdmCtrlGroupConfigurationCommand_Type = CommandString
_WdmCtrlGroupConfigurationCommand_Object = MibTableColumn
wdmCtrlGroupConfigurationCommand = _WdmCtrlGroupConfigurationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 11),
    _WdmCtrlGroupConfigurationCommand_Type()
)
wdmCtrlGroupConfigurationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupConfigurationCommand.setStatus("current")
_WdmCtrlGroupForceRegulationCommand_Type = CommandString
_WdmCtrlGroupForceRegulationCommand_Object = MibTableColumn
wdmCtrlGroupForceRegulationCommand = _WdmCtrlGroupForceRegulationCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 12),
    _WdmCtrlGroupForceRegulationCommand_Type()
)
wdmCtrlGroupForceRegulationCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupForceRegulationCommand.setStatus("current")


class _WdmCtrlGroupLockedRange_Type(Integer32):
    """Custom type wdmCtrlGroupLockedRange based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WdmCtrlGroupLockedRange_Type.__name__ = "Integer32"
_WdmCtrlGroupLockedRange_Object = MibTableColumn
wdmCtrlGroupLockedRange = _WdmCtrlGroupLockedRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 13),
    _WdmCtrlGroupLockedRange_Type()
)
wdmCtrlGroupLockedRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlGroupLockedRange.setStatus("current")


class _WdmCtrlGroupRegulationRange_Type(Unsigned32):
    """Custom type wdmCtrlGroupRegulationRange based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WdmCtrlGroupRegulationRange_Type.__name__ = "Unsigned32"
_WdmCtrlGroupRegulationRange_Object = MibTableColumn
wdmCtrlGroupRegulationRange = _WdmCtrlGroupRegulationRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 14),
    _WdmCtrlGroupRegulationRange_Type()
)
wdmCtrlGroupRegulationRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlGroupRegulationRange.setStatus("current")
_WdmCtrlGroupRegulationLastChangeTime_Type = DateAndTime
_WdmCtrlGroupRegulationLastChangeTime_Object = MibTableColumn
wdmCtrlGroupRegulationLastChangeTime = _WdmCtrlGroupRegulationLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 15),
    _WdmCtrlGroupRegulationLastChangeTime_Type()
)
wdmCtrlGroupRegulationLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupRegulationLastChangeTime.setStatus("current")
_WdmCtrlGroupCommissioningMode_Type = FaultStatus
_WdmCtrlGroupCommissioningMode_Object = MibTableColumn
wdmCtrlGroupCommissioningMode = _WdmCtrlGroupCommissioningMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 16),
    _WdmCtrlGroupCommissioningMode_Type()
)
wdmCtrlGroupCommissioningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupCommissioningMode.setStatus("current")
_WdmCtrlGroupAssociateChannel_Type = CommandString
_WdmCtrlGroupAssociateChannel_Object = MibTableColumn
wdmCtrlGroupAssociateChannel = _WdmCtrlGroupAssociateChannel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 17),
    _WdmCtrlGroupAssociateChannel_Type()
)
wdmCtrlGroupAssociateChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupAssociateChannel.setStatus("current")
_WdmCtrlGroupNoOfChannels_Type = Unsigned32
_WdmCtrlGroupNoOfChannels_Object = MibTableColumn
wdmCtrlGroupNoOfChannels = _WdmCtrlGroupNoOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 18),
    _WdmCtrlGroupNoOfChannels_Type()
)
wdmCtrlGroupNoOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupNoOfChannels.setStatus("current")


class _WdmCtrlGroupStatus_Type(Integer32):
    """Custom type wdmCtrlGroupStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("starting", 1),
          ("noRegulation", 2),
          ("reading", 3),
          ("regulation", 4),
          ("idle", 5))
    )


_WdmCtrlGroupStatus_Type.__name__ = "Integer32"
_WdmCtrlGroupStatus_Object = MibTableColumn
wdmCtrlGroupStatus = _WdmCtrlGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 19),
    _WdmCtrlGroupStatus_Type()
)
wdmCtrlGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupStatus.setStatus("current")


class _WdmCtrlGroupTimeLeft_Type(Unsigned32):
    """Custom type wdmCtrlGroupTimeLeft based on Unsigned32"""
    defaultValue = 1800


_WdmCtrlGroupTimeLeft_Type.__name__ = "Unsigned32"
_WdmCtrlGroupTimeLeft_Object = MibTableColumn
wdmCtrlGroupTimeLeft = _WdmCtrlGroupTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 20),
    _WdmCtrlGroupTimeLeft_Type()
)
wdmCtrlGroupTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupTimeLeft.setStatus("current")
_WdmCtrlGroupOutputPowerMismatch_Type = FaultStatus
_WdmCtrlGroupOutputPowerMismatch_Object = MibTableColumn
wdmCtrlGroupOutputPowerMismatch = _WdmCtrlGroupOutputPowerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 21),
    _WdmCtrlGroupOutputPowerMismatch_Type()
)
wdmCtrlGroupOutputPowerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupOutputPowerMismatch.setStatus("current")
_WdmCtrlGroupTotalPower_Type = Integer32
_WdmCtrlGroupTotalPower_Object = MibTableColumn
wdmCtrlGroupTotalPower = _WdmCtrlGroupTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 22),
    _WdmCtrlGroupTotalPower_Type()
)
wdmCtrlGroupTotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupTotalPower.setStatus("current")
_WdmCtrlGroupChannelStartupCommand_Type = CommandString
_WdmCtrlGroupChannelStartupCommand_Object = MibTableColumn
wdmCtrlGroupChannelStartupCommand = _WdmCtrlGroupChannelStartupCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 9, 1, 1, 23),
    _WdmCtrlGroupChannelStartupCommand_Type()
)
wdmCtrlGroupChannelStartupCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGroupChannelStartupCommand.setStatus("current")
_WdmSubChannelList_ObjectIdentity = ObjectIdentity
wdmSubChannelList = _WdmSubChannelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10)
)
_WdmSubChannelTable_Object = MibTable
wdmSubChannelTable = _WdmSubChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1)
)
if mibBuilder.loadTexts:
    wdmSubChannelTable.setStatus("current")
_WdmSubChannelEntry_Object = MibTableRow
wdmSubChannelEntry = _WdmSubChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1)
)
wdmSubChannelEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmSubChannelIndex"),
)
if mibBuilder.loadTexts:
    wdmSubChannelEntry.setStatus("current")


class _WdmSubChannelIndex_Type(Unsigned32):
    """Custom type wdmSubChannelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmSubChannelIndex_Type.__name__ = "Unsigned32"
_WdmSubChannelIndex_Object = MibTableColumn
wdmSubChannelIndex = _WdmSubChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 1),
    _WdmSubChannelIndex_Type()
)
wdmSubChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelIndex.setStatus("current")
_WdmSubChannelName_Type = MgmtNameString
_WdmSubChannelName_Object = MibTableColumn
wdmSubChannelName = _WdmSubChannelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 2),
    _WdmSubChannelName_Type()
)
wdmSubChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelName.setStatus("current")


class _WdmSubChannelId_Type(Unsigned32):
    """Custom type wdmSubChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WdmSubChannelId_Type.__name__ = "Unsigned32"
_WdmSubChannelId_Object = MibTableColumn
wdmSubChannelId = _WdmSubChannelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 3),
    _WdmSubChannelId_Type()
)
wdmSubChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelId.setStatus("current")


class _WdmSubChannelType_Type(Integer32):
    """Custom type wdmSubChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1t1", 1),
          ("fe", 2),
          ("gbeFe", 3))
    )


_WdmSubChannelType_Type.__name__ = "Integer32"
_WdmSubChannelType_Object = MibTableColumn
wdmSubChannelType = _WdmSubChannelType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 4),
    _WdmSubChannelType_Type()
)
wdmSubChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelType.setStatus("current")
_WdmSubChannelUnequipped_Type = FaultStatus
_WdmSubChannelUnequipped_Object = MibTableColumn
wdmSubChannelUnequipped = _WdmSubChannelUnequipped_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 5),
    _WdmSubChannelUnequipped_Type()
)
wdmSubChannelUnequipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelUnequipped.setStatus("current")


class _WdmSubChannelConnectionStatus_Type(DisplayString):
    """Custom type wdmSubChannelConnectionStatus based on DisplayString"""
    defaultValue = OctetString("Not connected")


_WdmSubChannelConnectionStatus_Type.__name__ = "DisplayString"
_WdmSubChannelConnectionStatus_Object = MibTableColumn
wdmSubChannelConnectionStatus = _WdmSubChannelConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 6),
    _WdmSubChannelConnectionStatus_Type()
)
wdmSubChannelConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelConnectionStatus.setStatus("current")


class _WdmSubChannelConnectedForeignIndex_Type(Unsigned32):
    """Custom type wdmSubChannelConnectedForeignIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WdmSubChannelConnectedForeignIndex_Type.__name__ = "Unsigned32"
_WdmSubChannelConnectedForeignIndex_Object = MibTableColumn
wdmSubChannelConnectedForeignIndex = _WdmSubChannelConnectedForeignIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 7),
    _WdmSubChannelConnectedForeignIndex_Type()
)
wdmSubChannelConnectedForeignIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmSubChannelConnectedForeignIndex.setStatus("current")
_WdmSubChannelCrossConnect_Type = CommandString
_WdmSubChannelCrossConnect_Object = MibTableColumn
wdmSubChannelCrossConnect = _WdmSubChannelCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 8),
    _WdmSubChannelCrossConnect_Type()
)
wdmSubChannelCrossConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelCrossConnect.setStatus("current")
_WdmSubChannelDisconnect_Type = CommandString
_WdmSubChannelDisconnect_Object = MibTableColumn
wdmSubChannelDisconnect = _WdmSubChannelDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 9),
    _WdmSubChannelDisconnect_Type()
)
wdmSubChannelDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelDisconnect.setStatus("current")


class _WdmSubChannelRemoteAccessInterface_Type(DisplayString):
    """Custom type wdmSubChannelRemoteAccessInterface based on DisplayString"""
    defaultValue = OctetString("Not connected")


_WdmSubChannelRemoteAccessInterface_Type.__name__ = "DisplayString"
_WdmSubChannelRemoteAccessInterface_Object = MibTableColumn
wdmSubChannelRemoteAccessInterface = _WdmSubChannelRemoteAccessInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 10),
    _WdmSubChannelRemoteAccessInterface_Type()
)
wdmSubChannelRemoteAccessInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmSubChannelRemoteAccessInterface.setStatus("current")


class _WdmSubChannelProtectedChannelIndex_Type(Unsigned32):
    """Custom type wdmSubChannelProtectedChannelIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WdmSubChannelProtectedChannelIndex_Type.__name__ = "Unsigned32"
_WdmSubChannelProtectedChannelIndex_Object = MibTableColumn
wdmSubChannelProtectedChannelIndex = _WdmSubChannelProtectedChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 10, 1, 1, 11),
    _WdmSubChannelProtectedChannelIndex_Type()
)
wdmSubChannelProtectedChannelIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmSubChannelProtectedChannelIndex.setStatus("current")
_WdmCtrlGlobal_ObjectIdentity = ObjectIdentity
wdmCtrlGlobal = _WdmCtrlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 11)
)


class _WdmCtrlGlobalRegulationInterval_Type(Integer32):
    """Custom type wdmCtrlGlobalRegulationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              30)
        )
    )
    namedValues = NamedValues(
        *(("interval5min", 5),
          ("interval30min", 30))
    )


_WdmCtrlGlobalRegulationInterval_Type.__name__ = "Integer32"
_WdmCtrlGlobalRegulationInterval_Object = MibScalar
wdmCtrlGlobalRegulationInterval = _WdmCtrlGlobalRegulationInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 11, 1),
    _WdmCtrlGlobalRegulationInterval_Type()
)
wdmCtrlGlobalRegulationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmCtrlGlobalRegulationInterval.setStatus("current")


class _WdmCtrlGlobalRegulationStatus_Type(Integer32):
    """Custom type wdmCtrlGlobalRegulationStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("searching", 2),
          ("reading", 3),
          ("regulating", 4),
          ("idle", 5))
    )


_WdmCtrlGlobalRegulationStatus_Type.__name__ = "Integer32"
_WdmCtrlGlobalRegulationStatus_Object = MibScalar
wdmCtrlGlobalRegulationStatus = _WdmCtrlGlobalRegulationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 11, 2),
    _WdmCtrlGlobalRegulationStatus_Type()
)
wdmCtrlGlobalRegulationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGlobalRegulationStatus.setStatus("current")
_WdmCtrlGlobalLastRegulation_Type = DateAndTime
_WdmCtrlGlobalLastRegulation_Object = MibScalar
wdmCtrlGlobalLastRegulation = _WdmCtrlGlobalLastRegulation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 11, 3),
    _WdmCtrlGlobalLastRegulation_Type()
)
wdmCtrlGlobalLastRegulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGlobalLastRegulation.setStatus("current")
_WdmCtrlGlobalTimeLeft_Type = Unsigned32
_WdmCtrlGlobalTimeLeft_Object = MibScalar
wdmCtrlGlobalTimeLeft = _WdmCtrlGlobalTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 11, 4),
    _WdmCtrlGlobalTimeLeft_Type()
)
wdmCtrlGlobalTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmCtrlGlobalTimeLeft.setStatus("current")
_WdmDelayCompPGList_ObjectIdentity = ObjectIdentity
wdmDelayCompPGList = _WdmDelayCompPGList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12)
)
_WdmDelayCompPGTable_Object = MibTable
wdmDelayCompPGTable = _WdmDelayCompPGTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1)
)
if mibBuilder.loadTexts:
    wdmDelayCompPGTable.setStatus("current")
_WdmDelayCompPGEntry_Object = MibTableRow
wdmDelayCompPGEntry = _WdmDelayCompPGEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1)
)
wdmDelayCompPGEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmDelayCompPGIndex"),
)
if mibBuilder.loadTexts:
    wdmDelayCompPGEntry.setStatus("current")


class _WdmDelayCompPGIndex_Type(Unsigned32):
    """Custom type wdmDelayCompPGIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmDelayCompPGIndex_Type.__name__ = "Unsigned32"
_WdmDelayCompPGIndex_Object = MibTableColumn
wdmDelayCompPGIndex = _WdmDelayCompPGIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 1),
    _WdmDelayCompPGIndex_Type()
)
wdmDelayCompPGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGIndex.setStatus("current")
_WdmDelayCompPGName_Type = MgmtNameString
_WdmDelayCompPGName_Object = MibTableColumn
wdmDelayCompPGName = _WdmDelayCompPGName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 2),
    _WdmDelayCompPGName_Type()
)
wdmDelayCompPGName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGName.setStatus("current")


class _WdmDelayCompPGUpId_Type(Unsigned32):
    """Custom type wdmDelayCompPGUpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WdmDelayCompPGUpId_Type.__name__ = "Unsigned32"
_WdmDelayCompPGUpId_Object = MibTableColumn
wdmDelayCompPGUpId = _WdmDelayCompPGUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 3),
    _WdmDelayCompPGUpId_Type()
)
wdmDelayCompPGUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGUpId.setStatus("current")


class _WdmDelayCompPGAdminStatus_Type(AdminStatusWithNA):
    """Custom type wdmDelayCompPGAdminStatus based on AdminStatusWithNA"""
    defaultValue = 3


_WdmDelayCompPGAdminStatus_Type.__name__ = "AdminStatusWithNA"
_WdmDelayCompPGAdminStatus_Object = MibTableColumn
wdmDelayCompPGAdminStatus = _WdmDelayCompPGAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 4),
    _WdmDelayCompPGAdminStatus_Type()
)
wdmDelayCompPGAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmDelayCompPGAdminStatus.setStatus("current")


class _WdmDelayCompPGOperStatus_Type(OperStatusWithNA):
    """Custom type wdmDelayCompPGOperStatus based on OperStatusWithNA"""
    defaultValue = 3


_WdmDelayCompPGOperStatus_Type.__name__ = "OperStatusWithNA"
_WdmDelayCompPGOperStatus_Object = MibTableColumn
wdmDelayCompPGOperStatus = _WdmDelayCompPGOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 5),
    _WdmDelayCompPGOperStatus_Type()
)
wdmDelayCompPGOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGOperStatus.setStatus("current")


class _WdmDelayCompPGAutoCompensationMode_Type(EnabledDisabledWithNA):
    """Custom type wdmDelayCompPGAutoCompensationMode based on EnabledDisabledWithNA"""
    defaultValue = 1


_WdmDelayCompPGAutoCompensationMode_Type.__name__ = "EnabledDisabledWithNA"
_WdmDelayCompPGAutoCompensationMode_Object = MibTableColumn
wdmDelayCompPGAutoCompensationMode = _WdmDelayCompPGAutoCompensationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 6),
    _WdmDelayCompPGAutoCompensationMode_Type()
)
wdmDelayCompPGAutoCompensationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmDelayCompPGAutoCompensationMode.setStatus("current")


class _WdmDelayCompPGAutoCompensationState_Type(Integer32):
    """Custom type wdmDelayCompPGAutoCompensationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("state1", 1),
          ("state2", 2),
          ("notApplicable", 2147483647))
    )


_WdmDelayCompPGAutoCompensationState_Type.__name__ = "Integer32"
_WdmDelayCompPGAutoCompensationState_Object = MibTableColumn
wdmDelayCompPGAutoCompensationState = _WdmDelayCompPGAutoCompensationState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 7),
    _WdmDelayCompPGAutoCompensationState_Type()
)
wdmDelayCompPGAutoCompensationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGAutoCompensationState.setStatus("current")
_WdmDelayCompPGDelayDifference_Type = Signed32WithNA
_WdmDelayCompPGDelayDifference_Object = MibTableColumn
wdmDelayCompPGDelayDifference = _WdmDelayCompPGDelayDifference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 8),
    _WdmDelayCompPGDelayDifference_Type()
)
wdmDelayCompPGDelayDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGDelayDifference.setStatus("current")
_WdmDelayCompPGDelayCompensationOOR_Type = FaultStatus
_WdmDelayCompPGDelayCompensationOOR_Object = MibTableColumn
wdmDelayCompPGDelayCompensationOOR = _WdmDelayCompPGDelayCompensationOOR_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 9),
    _WdmDelayCompPGDelayCompensationOOR_Type()
)
wdmDelayCompPGDelayCompensationOOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGDelayCompensationOOR.setStatus("current")
_WdmDelayCompPGFiberLengthDifferenceOOR_Type = FaultStatus
_WdmDelayCompPGFiberLengthDifferenceOOR_Object = MibTableColumn
wdmDelayCompPGFiberLengthDifferenceOOR = _WdmDelayCompPGFiberLengthDifferenceOOR_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 10),
    _WdmDelayCompPGFiberLengthDifferenceOOR_Type()
)
wdmDelayCompPGFiberLengthDifferenceOOR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGFiberLengthDifferenceOOR.setStatus("current")


class _WdmDelayCompPGDelayCompensationReset_Type(ResetWithNA):
    """Custom type wdmDelayCompPGDelayCompensationReset based on ResetWithNA"""
    defaultValue = 2


_WdmDelayCompPGDelayCompensationReset_Type.__name__ = "ResetWithNA"
_WdmDelayCompPGDelayCompensationReset_Object = MibTableColumn
wdmDelayCompPGDelayCompensationReset = _WdmDelayCompPGDelayCompensationReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 12, 1, 1, 11),
    _WdmDelayCompPGDelayCompensationReset_Type()
)
wdmDelayCompPGDelayCompensationReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompPGDelayCompensationReset.setStatus("current")
_WdmDelayCompLinkList_ObjectIdentity = ObjectIdentity
wdmDelayCompLinkList = _WdmDelayCompLinkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13)
)
_WdmDelayCompLinkTable_Object = MibTable
wdmDelayCompLinkTable = _WdmDelayCompLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1)
)
if mibBuilder.loadTexts:
    wdmDelayCompLinkTable.setStatus("current")
_WdmDelayCompLinkEntry_Object = MibTableRow
wdmDelayCompLinkEntry = _WdmDelayCompLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1, 1)
)
wdmDelayCompLinkEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmDelayCompLinkIndex"),
)
if mibBuilder.loadTexts:
    wdmDelayCompLinkEntry.setStatus("current")


class _WdmDelayCompLinkIndex_Type(Unsigned32):
    """Custom type wdmDelayCompLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmDelayCompLinkIndex_Type.__name__ = "Unsigned32"
_WdmDelayCompLinkIndex_Object = MibTableColumn
wdmDelayCompLinkIndex = _WdmDelayCompLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1, 1, 1),
    _WdmDelayCompLinkIndex_Type()
)
wdmDelayCompLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompLinkIndex.setStatus("current")
_WdmDelayCompLinkName_Type = MgmtNameString
_WdmDelayCompLinkName_Object = MibTableColumn
wdmDelayCompLinkName = _WdmDelayCompLinkName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1, 1, 2),
    _WdmDelayCompLinkName_Type()
)
wdmDelayCompLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompLinkName.setStatus("current")


class _WdmDelayCompLinkUpId_Type(Unsigned32):
    """Custom type wdmDelayCompLinkUpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WdmDelayCompLinkUpId_Type.__name__ = "Unsigned32"
_WdmDelayCompLinkUpId_Object = MibTableColumn
wdmDelayCompLinkUpId = _WdmDelayCompLinkUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1, 1, 3),
    _WdmDelayCompLinkUpId_Type()
)
wdmDelayCompLinkUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompLinkUpId.setStatus("current")


class _WdmDelayCompLinkCurrentDelayCompensation_Type(Signed32WithNA):
    """Custom type wdmDelayCompLinkCurrentDelayCompensation based on Signed32WithNA"""
    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47233),
    )


_WdmDelayCompLinkCurrentDelayCompensation_Type.__name__ = "Signed32WithNA"
_WdmDelayCompLinkCurrentDelayCompensation_Object = MibTableColumn
wdmDelayCompLinkCurrentDelayCompensation = _WdmDelayCompLinkCurrentDelayCompensation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1, 1, 4),
    _WdmDelayCompLinkCurrentDelayCompensation_Type()
)
wdmDelayCompLinkCurrentDelayCompensation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmDelayCompLinkCurrentDelayCompensation.setStatus("current")


class _WdmDelayCompLinkWantedDelayCompensation_Type(Signed32WithNA):
    """Custom type wdmDelayCompLinkWantedDelayCompensation based on Signed32WithNA"""
    defaultValue = 0

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47233),
    )


_WdmDelayCompLinkWantedDelayCompensation_Type.__name__ = "Signed32WithNA"
_WdmDelayCompLinkWantedDelayCompensation_Object = MibTableColumn
wdmDelayCompLinkWantedDelayCompensation = _WdmDelayCompLinkWantedDelayCompensation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 13, 1, 1, 5),
    _WdmDelayCompLinkWantedDelayCompensation_Type()
)
wdmDelayCompLinkWantedDelayCompensation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmDelayCompLinkWantedDelayCompensation.setStatus("current")
_WdmMeanChannelPowerControlGlobalList_ObjectIdentity = ObjectIdentity
wdmMeanChannelPowerControlGlobalList = _WdmMeanChannelPowerControlGlobalList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 14)
)
_WdmMeanChannelPowerControlGlobalTable_Object = MibTable
wdmMeanChannelPowerControlGlobalTable = _WdmMeanChannelPowerControlGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 14, 1)
)
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGlobalTable.setStatus("current")
_WdmMeanChannelPowerControlGlobalEntry_Object = MibTableRow
wdmMeanChannelPowerControlGlobalEntry = _WdmMeanChannelPowerControlGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 14, 1, 1)
)
wdmMeanChannelPowerControlGlobalEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmMeanChannelPowerControlGlobalIndex"),
)
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGlobalEntry.setStatus("current")


class _WdmMeanChannelPowerControlGlobalIndex_Type(Unsigned32):
    """Custom type wdmMeanChannelPowerControlGlobalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmMeanChannelPowerControlGlobalIndex_Type.__name__ = "Unsigned32"
_WdmMeanChannelPowerControlGlobalIndex_Object = MibTableColumn
wdmMeanChannelPowerControlGlobalIndex = _WdmMeanChannelPowerControlGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 14, 1, 1, 1),
    _WdmMeanChannelPowerControlGlobalIndex_Type()
)
wdmMeanChannelPowerControlGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGlobalIndex.setStatus("current")
_WdmMeanChannelPowerControlGlobalName_Type = MgmtNameString
_WdmMeanChannelPowerControlGlobalName_Object = MibTableColumn
wdmMeanChannelPowerControlGlobalName = _WdmMeanChannelPowerControlGlobalName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 14, 1, 1, 2),
    _WdmMeanChannelPowerControlGlobalName_Type()
)
wdmMeanChannelPowerControlGlobalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGlobalName.setStatus("current")
_WdmMeanChannelPowerControlGlobalEntryCreate_Type = CommandString
_WdmMeanChannelPowerControlGlobalEntryCreate_Object = MibTableColumn
wdmMeanChannelPowerControlGlobalEntryCreate = _WdmMeanChannelPowerControlGlobalEntryCreate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 14, 1, 1, 3),
    _WdmMeanChannelPowerControlGlobalEntryCreate_Type()
)
wdmMeanChannelPowerControlGlobalEntryCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGlobalEntryCreate.setStatus("current")
_WdmMeanChannelPowerControlList_ObjectIdentity = ObjectIdentity
wdmMeanChannelPowerControlList = _WdmMeanChannelPowerControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15)
)
_WdmMeanChannelPowerControlTable_Object = MibTable
wdmMeanChannelPowerControlTable = _WdmMeanChannelPowerControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1)
)
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlTable.setStatus("current")
_WdmMeanChannelPowerControlEntry_Object = MibTableRow
wdmMeanChannelPowerControlEntry = _WdmMeanChannelPowerControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1)
)
wdmMeanChannelPowerControlEntry.setIndexNames(
    (0, "LUM-WDM-MIB", "wdmMeanChannelPowerControlIndex"),
)
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlEntry.setStatus("current")


class _WdmMeanChannelPowerControlIndex_Type(Unsigned32):
    """Custom type wdmMeanChannelPowerControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WdmMeanChannelPowerControlIndex_Type.__name__ = "Unsigned32"
_WdmMeanChannelPowerControlIndex_Object = MibTableColumn
wdmMeanChannelPowerControlIndex = _WdmMeanChannelPowerControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 1),
    _WdmMeanChannelPowerControlIndex_Type()
)
wdmMeanChannelPowerControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlIndex.setStatus("current")
_WdmMeanChannelPowerControlName_Type = MgmtNameString
_WdmMeanChannelPowerControlName_Object = MibTableColumn
wdmMeanChannelPowerControlName = _WdmMeanChannelPowerControlName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 2),
    _WdmMeanChannelPowerControlName_Type()
)
wdmMeanChannelPowerControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlName.setStatus("current")


class _WdmMeanChannelPowerControlDescr_Type(DisplayString):
    """Custom type wdmMeanChannelPowerControlDescr based on DisplayString"""
    defaultValue = OctetString("")


_WdmMeanChannelPowerControlDescr_Type.__name__ = "DisplayString"
_WdmMeanChannelPowerControlDescr_Object = MibTableColumn
wdmMeanChannelPowerControlDescr = _WdmMeanChannelPowerControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 3),
    _WdmMeanChannelPowerControlDescr_Type()
)
wdmMeanChannelPowerControlDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlDescr.setStatus("current")
_WdmMeanChannelPowerControlOcmSubrack_Type = SubrackNumber
_WdmMeanChannelPowerControlOcmSubrack_Object = MibTableColumn
wdmMeanChannelPowerControlOcmSubrack = _WdmMeanChannelPowerControlOcmSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 4),
    _WdmMeanChannelPowerControlOcmSubrack_Type()
)
wdmMeanChannelPowerControlOcmSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOcmSubrack.setStatus("current")
_WdmMeanChannelPowerControlOcmSlot_Type = SlotNumber
_WdmMeanChannelPowerControlOcmSlot_Object = MibTableColumn
wdmMeanChannelPowerControlOcmSlot = _WdmMeanChannelPowerControlOcmSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 5),
    _WdmMeanChannelPowerControlOcmSlot_Type()
)
wdmMeanChannelPowerControlOcmSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOcmSlot.setStatus("current")


class _WdmMeanChannelPowerControlOcmPort_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlOcmPort based on Integer32"""
    defaultValue = 1

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
        *(("a", 1),
          ("b", 2),
          ("c", 3),
          ("d", 4),
          ("e", 5),
          ("f", 6),
          ("g", 7),
          ("h", 8))
    )


_WdmMeanChannelPowerControlOcmPort_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlOcmPort_Object = MibTableColumn
wdmMeanChannelPowerControlOcmPort = _WdmMeanChannelPowerControlOcmPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 6),
    _WdmMeanChannelPowerControlOcmPort_Type()
)
wdmMeanChannelPowerControlOcmPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOcmPort.setStatus("current")
_WdmMeanChannelPowerControlOaSubrack_Type = SubrackNumber
_WdmMeanChannelPowerControlOaSubrack_Object = MibTableColumn
wdmMeanChannelPowerControlOaSubrack = _WdmMeanChannelPowerControlOaSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 7),
    _WdmMeanChannelPowerControlOaSubrack_Type()
)
wdmMeanChannelPowerControlOaSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOaSubrack.setStatus("current")
_WdmMeanChannelPowerControlOaSlot_Type = SlotNumber
_WdmMeanChannelPowerControlOaSlot_Object = MibTableColumn
wdmMeanChannelPowerControlOaSlot = _WdmMeanChannelPowerControlOaSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 8),
    _WdmMeanChannelPowerControlOaSlot_Type()
)
wdmMeanChannelPowerControlOaSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOaSlot.setStatus("current")
_WdmMeanChannelPowerControlOaPort_Type = PortNumber
_WdmMeanChannelPowerControlOaPort_Object = MibTableColumn
wdmMeanChannelPowerControlOaPort = _WdmMeanChannelPowerControlOaPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 9),
    _WdmMeanChannelPowerControlOaPort_Type()
)
wdmMeanChannelPowerControlOaPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOaPort.setStatus("current")
_WdmMeanChannelPowerControlMonitorName_Type = MgmtNameString
_WdmMeanChannelPowerControlMonitorName_Object = MibTableColumn
wdmMeanChannelPowerControlMonitorName = _WdmMeanChannelPowerControlMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 10),
    _WdmMeanChannelPowerControlMonitorName_Type()
)
wdmMeanChannelPowerControlMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlMonitorName.setStatus("current")


class _WdmMeanChannelPowerControlAdminStatus_Type(AdminStatusWithNA):
    """Custom type wdmMeanChannelPowerControlAdminStatus based on AdminStatusWithNA"""
    defaultValue = 1


_WdmMeanChannelPowerControlAdminStatus_Type.__name__ = "AdminStatusWithNA"
_WdmMeanChannelPowerControlAdminStatus_Object = MibTableColumn
wdmMeanChannelPowerControlAdminStatus = _WdmMeanChannelPowerControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 11),
    _WdmMeanChannelPowerControlAdminStatus_Type()
)
wdmMeanChannelPowerControlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlAdminStatus.setStatus("current")


class _WdmMeanChannelPowerControlOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type wdmMeanChannelPowerControlOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 3


_WdmMeanChannelPowerControlOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_WdmMeanChannelPowerControlOperStatus_Object = MibTableColumn
wdmMeanChannelPowerControlOperStatus = _WdmMeanChannelPowerControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 12),
    _WdmMeanChannelPowerControlOperStatus_Type()
)
wdmMeanChannelPowerControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlOperStatus.setStatus("current")
_WdmMeanChannelPowerControlStartRegulation_Type = CommandString
_WdmMeanChannelPowerControlStartRegulation_Object = MibTableColumn
wdmMeanChannelPowerControlStartRegulation = _WdmMeanChannelPowerControlStartRegulation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 13),
    _WdmMeanChannelPowerControlStartRegulation_Type()
)
wdmMeanChannelPowerControlStartRegulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlStartRegulation.setStatus("current")


class _WdmMeanChannelPowerControlRegulationRange_Type(Unsigned32):
    """Custom type wdmMeanChannelPowerControlRegulationRange based on Unsigned32"""
    defaultValue = 40

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_WdmMeanChannelPowerControlRegulationRange_Type.__name__ = "Unsigned32"
_WdmMeanChannelPowerControlRegulationRange_Object = MibTableColumn
wdmMeanChannelPowerControlRegulationRange = _WdmMeanChannelPowerControlRegulationRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 14),
    _WdmMeanChannelPowerControlRegulationRange_Type()
)
wdmMeanChannelPowerControlRegulationRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlRegulationRange.setStatus("current")
_WdmMeanChannelPowerControlLatestRegulation_Type = DateAndTime
_WdmMeanChannelPowerControlLatestRegulation_Object = MibTableColumn
wdmMeanChannelPowerControlLatestRegulation = _WdmMeanChannelPowerControlLatestRegulation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 15),
    _WdmMeanChannelPowerControlLatestRegulation_Type()
)
wdmMeanChannelPowerControlLatestRegulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlLatestRegulation.setStatus("current")
_WdmMeanChannelPowerControlLatestChange_Type = DateAndTime
_WdmMeanChannelPowerControlLatestChange_Object = MibTableColumn
wdmMeanChannelPowerControlLatestChange = _WdmMeanChannelPowerControlLatestChange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 16),
    _WdmMeanChannelPowerControlLatestChange_Type()
)
wdmMeanChannelPowerControlLatestChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlLatestChange.setStatus("current")
_WdmMeanChannelPowerControlMonitorOffsetCalibrationFailed_Type = FaultStatus
_WdmMeanChannelPowerControlMonitorOffsetCalibrationFailed_Object = MibTableColumn
wdmMeanChannelPowerControlMonitorOffsetCalibrationFailed = _WdmMeanChannelPowerControlMonitorOffsetCalibrationFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 17),
    _WdmMeanChannelPowerControlMonitorOffsetCalibrationFailed_Type()
)
wdmMeanChannelPowerControlMonitorOffsetCalibrationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlMonitorOffsetCalibrationFailed.setStatus("current")


class _WdmMeanChannelPowerControlRegulationState_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlRegulationState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("starting", 1),
          ("regulating", 2),
          ("idle", 3))
    )


_WdmMeanChannelPowerControlRegulationState_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlRegulationState_Object = MibTableColumn
wdmMeanChannelPowerControlRegulationState = _WdmMeanChannelPowerControlRegulationState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 18),
    _WdmMeanChannelPowerControlRegulationState_Type()
)
wdmMeanChannelPowerControlRegulationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlRegulationState.setStatus("current")


class _WdmMeanChannelPowerControlTimeToNextRegulation_Type(Unsigned32):
    """Custom type wdmMeanChannelPowerControlTimeToNextRegulation based on Unsigned32"""
    defaultValue = 30


_WdmMeanChannelPowerControlTimeToNextRegulation_Type.__name__ = "Unsigned32"
_WdmMeanChannelPowerControlTimeToNextRegulation_Object = MibTableColumn
wdmMeanChannelPowerControlTimeToNextRegulation = _WdmMeanChannelPowerControlTimeToNextRegulation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 19),
    _WdmMeanChannelPowerControlTimeToNextRegulation_Type()
)
wdmMeanChannelPowerControlTimeToNextRegulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlTimeToNextRegulation.setStatus("current")


class _WdmMeanChannelPowerControlWantedChannelPower_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlWantedChannelPower based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-150, 100),
    )


_WdmMeanChannelPowerControlWantedChannelPower_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlWantedChannelPower_Object = MibTableColumn
wdmMeanChannelPowerControlWantedChannelPower = _WdmMeanChannelPowerControlWantedChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 20),
    _WdmMeanChannelPowerControlWantedChannelPower_Type()
)
wdmMeanChannelPowerControlWantedChannelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlWantedChannelPower.setStatus("current")
_WdmMeanChannelPowerControlCurrentChannelPower_Type = Integer32
_WdmMeanChannelPowerControlCurrentChannelPower_Object = MibTableColumn
wdmMeanChannelPowerControlCurrentChannelPower = _WdmMeanChannelPowerControlCurrentChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 21),
    _WdmMeanChannelPowerControlCurrentChannelPower_Type()
)
wdmMeanChannelPowerControlCurrentChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlCurrentChannelPower.setStatus("current")


class _WdmMeanChannelPowerControlCurrentGain_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlCurrentGain based on Integer32"""
    defaultValue = 200


_WdmMeanChannelPowerControlCurrentGain_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlCurrentGain_Object = MibTableColumn
wdmMeanChannelPowerControlCurrentGain = _WdmMeanChannelPowerControlCurrentGain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 22),
    _WdmMeanChannelPowerControlCurrentGain_Type()
)
wdmMeanChannelPowerControlCurrentGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlCurrentGain.setStatus("current")


class _WdmMeanChannelPowerControlTotalChannelOutputPower_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlTotalChannelOutputPower based on Integer32"""
    defaultValue = 0


_WdmMeanChannelPowerControlTotalChannelOutputPower_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlTotalChannelOutputPower_Object = MibTableColumn
wdmMeanChannelPowerControlTotalChannelOutputPower = _WdmMeanChannelPowerControlTotalChannelOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 23),
    _WdmMeanChannelPowerControlTotalChannelOutputPower_Type()
)
wdmMeanChannelPowerControlTotalChannelOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlTotalChannelOutputPower.setStatus("current")


class _WdmMeanChannelPowerControlNumberOfChannels_Type(Unsigned32):
    """Custom type wdmMeanChannelPowerControlNumberOfChannels based on Unsigned32"""
    defaultValue = 0


_WdmMeanChannelPowerControlNumberOfChannels_Type.__name__ = "Unsigned32"
_WdmMeanChannelPowerControlNumberOfChannels_Object = MibTableColumn
wdmMeanChannelPowerControlNumberOfChannels = _WdmMeanChannelPowerControlNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 24),
    _WdmMeanChannelPowerControlNumberOfChannels_Type()
)
wdmMeanChannelPowerControlNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlNumberOfChannels.setStatus("current")


class _WdmMeanChannelPowerControlAbsolutePowerOffset_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlAbsolutePowerOffset based on Integer32"""
    defaultValue = 0


_WdmMeanChannelPowerControlAbsolutePowerOffset_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlAbsolutePowerOffset_Object = MibTableColumn
wdmMeanChannelPowerControlAbsolutePowerOffset = _WdmMeanChannelPowerControlAbsolutePowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 25),
    _WdmMeanChannelPowerControlAbsolutePowerOffset_Type()
)
wdmMeanChannelPowerControlAbsolutePowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlAbsolutePowerOffset.setStatus("current")


class _WdmMeanChannelPowerControlRemainingPowerOffset_Type(Integer32):
    """Custom type wdmMeanChannelPowerControlRemainingPowerOffset based on Integer32"""
    defaultValue = 0


_WdmMeanChannelPowerControlRemainingPowerOffset_Type.__name__ = "Integer32"
_WdmMeanChannelPowerControlRemainingPowerOffset_Object = MibTableColumn
wdmMeanChannelPowerControlRemainingPowerOffset = _WdmMeanChannelPowerControlRemainingPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 26),
    _WdmMeanChannelPowerControlRemainingPowerOffset_Type()
)
wdmMeanChannelPowerControlRemainingPowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlRemainingPowerOffset.setStatus("current")
_WdmMeanChannelPowerControlMonitorOffsetTooLarge_Type = FaultStatus
_WdmMeanChannelPowerControlMonitorOffsetTooLarge_Object = MibTableColumn
wdmMeanChannelPowerControlMonitorOffsetTooLarge = _WdmMeanChannelPowerControlMonitorOffsetTooLarge_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 27),
    _WdmMeanChannelPowerControlMonitorOffsetTooLarge_Type()
)
wdmMeanChannelPowerControlMonitorOffsetTooLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlMonitorOffsetTooLarge.setStatus("current")
_WdmMeanChannelPowerControlChannelPowerOutOfRange_Type = FaultStatus
_WdmMeanChannelPowerControlChannelPowerOutOfRange_Object = MibTableColumn
wdmMeanChannelPowerControlChannelPowerOutOfRange = _WdmMeanChannelPowerControlChannelPowerOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 28),
    _WdmMeanChannelPowerControlChannelPowerOutOfRange_Type()
)
wdmMeanChannelPowerControlChannelPowerOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlChannelPowerOutOfRange.setStatus("current")


class _WdmMeanChannelPowerControlRegulationInterval_Type(Unsigned32):
    """Custom type wdmMeanChannelPowerControlRegulationInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_WdmMeanChannelPowerControlRegulationInterval_Type.__name__ = "Unsigned32"
_WdmMeanChannelPowerControlRegulationInterval_Object = MibTableColumn
wdmMeanChannelPowerControlRegulationInterval = _WdmMeanChannelPowerControlRegulationInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 29),
    _WdmMeanChannelPowerControlRegulationInterval_Type()
)
wdmMeanChannelPowerControlRegulationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlRegulationInterval.setStatus("current")
_WdmMeanChannelPowerControlAmplifierOutputPort_Type = MgmtNameString
_WdmMeanChannelPowerControlAmplifierOutputPort_Object = MibTableColumn
wdmMeanChannelPowerControlAmplifierOutputPort = _WdmMeanChannelPowerControlAmplifierOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 30),
    _WdmMeanChannelPowerControlAmplifierOutputPort_Type()
)
wdmMeanChannelPowerControlAmplifierOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlAmplifierOutputPort.setStatus("current")
_WdmMeanChannelPowerControlLatestAmplifierRxPower_Type = Integer32
_WdmMeanChannelPowerControlLatestAmplifierRxPower_Object = MibTableColumn
wdmMeanChannelPowerControlLatestAmplifierRxPower = _WdmMeanChannelPowerControlLatestAmplifierRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 31),
    _WdmMeanChannelPowerControlLatestAmplifierRxPower_Type()
)
wdmMeanChannelPowerControlLatestAmplifierRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlLatestAmplifierRxPower.setStatus("current")
_WdmMeanChannelPowerControlLatestAmplifierTxPower_Type = Integer32
_WdmMeanChannelPowerControlLatestAmplifierTxPower_Object = MibTableColumn
wdmMeanChannelPowerControlLatestAmplifierTxPower = _WdmMeanChannelPowerControlLatestAmplifierTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 32),
    _WdmMeanChannelPowerControlLatestAmplifierTxPower_Type()
)
wdmMeanChannelPowerControlLatestAmplifierTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlLatestAmplifierTxPower.setStatus("current")
_WdmMeanChannelPowerControlLocalId_Type = Integer32
_WdmMeanChannelPowerControlLocalId_Object = MibTableColumn
wdmMeanChannelPowerControlLocalId = _WdmMeanChannelPowerControlLocalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 15, 1, 1, 33),
    _WdmMeanChannelPowerControlLocalId_Type()
)
wdmMeanChannelPowerControlLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlLocalId.setStatus("current")

# Managed Objects groups

wdmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 1)
)
wdmGeneralGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralTestAndIncr"),
        ("LUM-WDM-MIB", "wdmGeneralMibSpecVersion"),
        ("LUM-WDM-MIB", "wdmGeneralMibImplVersion"),
        ("LUM-WDM-MIB", "wdmGeneralLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmGeneralGroup.setStatus("current")

wdmIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 2)
)
wdmIfGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfSeverelyErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfBackgroundBlockErrors"),
        ("LUM-WDM-MIB", "wdmIfUnavailableSeconds"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"))
)
if mibBuilder.loadTexts:
    wdmIfGroup.setStatus("deprecated")

wdmProtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 3)
)
wdmProtGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtOperStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"))
)
if mibBuilder.loadTexts:
    wdmProtGroup.setStatus("deprecated")

wdmPassiveIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 5)
)
wdmPassiveIfGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaMax"),
        ("LUM-WDM-MIB", "wdmPassiveIfLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroup.setStatus("deprecated")

wdmGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 6)
)
wdmGeneralGroupV2.setObjects(
    ("LUM-WDM-MIB", "wdmGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    wdmGeneralGroupV2.setStatus("deprecated")

wdmIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 7)
)
wdmIfGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfSeverelyErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfBackgroundBlockErrors"),
        ("LUM-WDM-MIB", "wdmIfUnavailableSeconds"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfJ0PathTrace"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV2.setStatus("deprecated")

wdmPassiveIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 8)
)
wdmPassiveIfGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaMax"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroupV2.setStatus("deprecated")

wdmIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 9)
)
wdmIfGroupV3.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfSeverelyErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfBackgroundBlockErrors"),
        ("LUM-WDM-MIB", "wdmIfUnavailableSeconds"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfJ0PathTrace"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfInbandStatus"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV3.setStatus("deprecated")

wdmPassiveIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 10)
)
wdmPassiveIfGroupV3.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaMax"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroupV3.setStatus("deprecated")

wdmIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 11)
)
wdmIfGroupV4.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfSeverelyErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfBackgroundBlockErrors"),
        ("LUM-WDM-MIB", "wdmIfUnavailableSeconds"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfJ0PathTrace"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfInbandStatus"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV4.setStatus("deprecated")

wdmPassiveIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 12)
)
wdmPassiveIfGroupV4.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroupV4.setStatus("deprecated")

wdmIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 13)
)
wdmIfGroupV5.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfSeverelyErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfBackgroundBlockErrors"),
        ("LUM-WDM-MIB", "wdmIfUnavailableSeconds"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfJ0PathTrace"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfInbandStatus"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV5.setStatus("deprecated")

wdmProtGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 14)
)
wdmProtGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV2.setStatus("deprecated")

wdmIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 15)
)
wdmIfGroupV6.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfSeverelyErroredSeconds"),
        ("LUM-WDM-MIB", "wdmIfBackgroundBlockErrors"),
        ("LUM-WDM-MIB", "wdmIfUnavailableSeconds"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfJ0PathTrace"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV6.setStatus("deprecated")

wdmIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 17)
)
wdmIfGroupV7.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfJ0PathTrace"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV7.setStatus("deprecated")

wdmGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 18)
)
wdmGeneralGroupV3.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmGeneralGroupV3.setStatus("deprecated")

wdmIfGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 19)
)
wdmIfGroupV8.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV8.setStatus("deprecated")

wdmIfGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 20)
)
wdmIfGroupV9.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfInbandMode"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV9.setStatus("deprecated")

wdmIfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 21)
)
wdmIfGroupV10.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV10.setStatus("deprecated")

wdmIfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 22)
)
wdmIfGroupV11.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV11.setStatus("deprecated")

wdmIfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 23)
)
wdmIfGroupV12.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV12.setStatus("deprecated")

wdmPassiveIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 24)
)
wdmPassiveIfGroupV5.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfUnexpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfOperStatus"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroupV5.setStatus("deprecated")

wdmIfGroupV13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 25)
)
wdmIfGroupV13.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV13.setStatus("deprecated")

wdmGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 26)
)
wdmGeneralGroupV4.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralStateLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralWdmIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmPassiveIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmProtTableSize"))
)
if mibBuilder.loadTexts:
    wdmGeneralGroupV4.setStatus("deprecated")

wdmProtGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 27)
)
wdmProtGroupV3.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV3.setStatus("deprecated")

wdmIfGroupV14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 28)
)
wdmIfGroupV14.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV14.setStatus("deprecated")

wdmPassiveIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 29)
)
wdmPassiveIfGroupV6.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfUnexpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfOperStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfObjectProperty"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroupV6.setStatus("current")

wdmProtGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 30)
)
wdmProtGroupV4.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"),
        ("LUM-WDM-MIB", "wdmProtObjectProperty"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV4.setStatus("deprecated")

wdmProtGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 31)
)
wdmProtGroupV5.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"),
        ("LUM-WDM-MIB", "wdmProtObjectProperty"),
        ("LUM-WDM-MIB", "wdmProtWrapperMode"),
        ("LUM-WDM-MIB", "wdmProtWrapperState"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV5.setStatus("deprecated")

wdmIfGroupV15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 32)
)
wdmIfGroupV15.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV15.setStatus("deprecated")

wdmIfGroupV16 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 33)
)
wdmIfGroupV16.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV16.setStatus("deprecated")

wdmIfGroupV17 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 34)
)
wdmIfGroupV17.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV17.setStatus("deprecated")

wdmIfGroupV18 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 35)
)
wdmIfGroupV18.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV18.setStatus("deprecated")

wdmIfGroupV19 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 36)
)
wdmIfGroupV19.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfOHTransparency"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV19.setStatus("deprecated")

wdmVc4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 38)
)
wdmVc4Group.setObjects(
      *(("LUM-WDM-MIB", "wdmVc4Index"),
        ("LUM-WDM-MIB", "wdmVc4Name"),
        ("LUM-WDM-MIB", "wdmVc4Descr"),
        ("LUM-WDM-MIB", "wdmVc4Subrack"),
        ("LUM-WDM-MIB", "wdmVc4Slot"),
        ("LUM-WDM-MIB", "wdmVc4TxPort"),
        ("LUM-WDM-MIB", "wdmVc4RxPort"),
        ("LUM-WDM-MIB", "wdmVc4Vc4"),
        ("LUM-WDM-MIB", "wdmVc4ObjectProperty"),
        ("LUM-WDM-MIB", "wdmVc4AuAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmVc4AuLossOfPointer"),
        ("LUM-WDM-MIB", "wdmVc4RxSignalStatus"),
        ("LUM-WDM-MIB", "wdmVc4ConcatenationStatus"),
        ("LUM-WDM-MIB", "wdmVc4PayloadStatus"))
)
if mibBuilder.loadTexts:
    wdmVc4Group.setStatus("deprecated")

wdmGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 39)
)
wdmGeneralGroupV5.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralStateLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralWdmIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmPassiveIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmProtTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmVc4TableSize"))
)
if mibBuilder.loadTexts:
    wdmGeneralGroupV5.setStatus("current")

wdmIfGroupV20 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 40)
)
wdmIfGroupV20.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfOHTransparency"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV20.setStatus("deprecated")

wdmIfGroupV21 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 41)
)
wdmIfGroupV21.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfOHTransparency"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV21.setStatus("deprecated")

wdmIfGroupV22 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 42)
)
wdmIfGroupV22.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV22.setStatus("deprecated")

wdmRemoteProtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 43)
)
wdmRemoteProtGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmRemoteProtIndex"),
        ("LUM-WDM-MIB", "wdmRemoteProtName"),
        ("LUM-WDM-MIB", "wdmRemoteProtDescr"),
        ("LUM-WDM-MIB", "wdmRemoteProtLocalSubrack"),
        ("LUM-WDM-MIB", "wdmRemoteProtLocalSlot"),
        ("LUM-WDM-MIB", "wdmRemoteProtLocalPort"),
        ("LUM-WDM-MIB", "wdmRemoteProtCommSubrack"),
        ("LUM-WDM-MIB", "wdmRemoteProtCommSlot"),
        ("LUM-WDM-MIB", "wdmRemoteProtCommPort"),
        ("LUM-WDM-MIB", "wdmRemoteProtCommInterface"),
        ("LUM-WDM-MIB", "wdmRemoteProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmRemoteProtIpAddress"),
        ("LUM-WDM-MIB", "wdmRemoteProtIdentifier"),
        ("LUM-WDM-MIB", "wdmRemoteProtRole"),
        ("LUM-WDM-MIB", "wdmRemoteProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmRemoteProtRowStatus"),
        ("LUM-WDM-MIB", "wdmRemoteProtActiveSide"),
        ("LUM-WDM-MIB", "wdmRemoteProtLocalStatus"),
        ("LUM-WDM-MIB", "wdmRemoteProtRemoteStatus"),
        ("LUM-WDM-MIB", "wdmRemoteProtObjectProperty"),
        ("LUM-WDM-MIB", "wdmRemoteProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmRemoteProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmRemoteProtSetup"),
        ("LUM-WDM-MIB", "wdmRemoteProtSetupFailure"),
        ("LUM-WDM-MIB", "wdmRemoteProtRoleConflict"),
        ("LUM-WDM-MIB", "wdmRemoteProtCommunicationFailure"))
)
if mibBuilder.loadTexts:
    wdmRemoteProtGroup.setStatus("current")

wdmProtGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 44)
)
wdmProtGroupV6.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"),
        ("LUM-WDM-MIB", "wdmProtObjectProperty"),
        ("LUM-WDM-MIB", "wdmProtWrapperMode"),
        ("LUM-WDM-MIB", "wdmProtWrapperState"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftCommPort"),
        ("LUM-WDM-MIB", "wdmProtRightCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightCommSlot"),
        ("LUM-WDM-MIB", "wdmProtRightCommPort"),
        ("LUM-WDM-MIB", "wdmProtLeftCommInterface"),
        ("LUM-WDM-MIB", "wdmProtRightCommInterface"),
        ("LUM-WDM-MIB", "wdmProtCommunicationFailure"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV6.setStatus("current")

wdmCtrlChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 45)
)
wdmCtrlChannelGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlChannelIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelName"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSlot"),
        ("LUM-WDM-MIB", "wdmCtrlChannelTxPort"),
        ("LUM-WDM-MIB", "wdmCtrlChannelChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelWantedOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelOuputPowerControlFailure"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentPowerOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenuationOutOfRange"))
)
if mibBuilder.loadTexts:
    wdmCtrlChannelGroup.setStatus("deprecated")

wdmCtrlGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 46)
)
wdmCtrlGroupGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlGroupIndex"),
        ("LUM-WDM-MIB", "wdmCtrlGroupName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupDescr"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSlot"),
        ("LUM-WDM-MIB", "wdmCtrlGroupPort"),
        ("LUM-WDM-MIB", "wdmCtrlGroupMonitorName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupControlMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupLockedRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationLastChangeTime"),
        ("LUM-WDM-MIB", "wdmCtrlGroupCommissioningMode"))
)
if mibBuilder.loadTexts:
    wdmCtrlGroupGroup.setStatus("deprecated")

wdmCtrlGroupGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 48)
)
wdmCtrlGroupGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlGroupIndex"),
        ("LUM-WDM-MIB", "wdmCtrlGroupName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupDescr"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSlot"),
        ("LUM-WDM-MIB", "wdmCtrlGroupPort"),
        ("LUM-WDM-MIB", "wdmCtrlGroupMonitorName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupControlMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupLockedRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationLastChangeTime"),
        ("LUM-WDM-MIB", "wdmCtrlGroupCommissioningMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAssociateChannel"),
        ("LUM-WDM-MIB", "wdmCtrlGroupNoOfChannels"),
        ("LUM-WDM-MIB", "wdmCtrlGroupStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupTimeLeft"))
)
if mibBuilder.loadTexts:
    wdmCtrlGroupGroupV2.setStatus("deprecated")

wdmSubChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 49)
)
wdmSubChannelGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmSubChannelIndex"),
        ("LUM-WDM-MIB", "wdmSubChannelName"),
        ("LUM-WDM-MIB", "wdmSubChannelId"),
        ("LUM-WDM-MIB", "wdmSubChannelType"),
        ("LUM-WDM-MIB", "wdmSubChannelUnequipped"),
        ("LUM-WDM-MIB", "wdmSubChannelConnectionStatus"),
        ("LUM-WDM-MIB", "wdmSubChannelConnectedForeignIndex"),
        ("LUM-WDM-MIB", "wdmSubChannelCrossConnect"),
        ("LUM-WDM-MIB", "wdmSubChannelDisconnect"),
        ("LUM-WDM-MIB", "wdmSubChannelRemoteAccessInterface"))
)
if mibBuilder.loadTexts:
    wdmSubChannelGroup.setStatus("deprecated")

wdmGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 50)
)
wdmGeneralGroupV6.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralStateLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralWdmIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmPassiveIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmProtTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmVc4TableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmCtrlChannelTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmCtrlGroupTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmSubChannelTableSize"))
)
if mibBuilder.loadTexts:
    wdmGeneralGroupV6.setStatus("deprecated")

wdmIfGroupV23 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 51)
)
wdmIfGroupV23.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV23.setStatus("deprecated")

wdmVc4GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 52)
)
wdmVc4GroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmVc4Index"),
        ("LUM-WDM-MIB", "wdmVc4Name"),
        ("LUM-WDM-MIB", "wdmVc4Descr"),
        ("LUM-WDM-MIB", "wdmVc4Subrack"),
        ("LUM-WDM-MIB", "wdmVc4Slot"),
        ("LUM-WDM-MIB", "wdmVc4TxPort"),
        ("LUM-WDM-MIB", "wdmVc4RxPort"),
        ("LUM-WDM-MIB", "wdmVc4Vc4"),
        ("LUM-WDM-MIB", "wdmVc4ObjectProperty"),
        ("LUM-WDM-MIB", "wdmVc4AuAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmVc4AuLossOfPointer"),
        ("LUM-WDM-MIB", "wdmVc4RxSignalStatus"),
        ("LUM-WDM-MIB", "wdmVc4ConcatenationStatus"),
        ("LUM-WDM-MIB", "wdmVc4PayloadStatus"),
        ("LUM-WDM-MIB", "wdmVc4ConnectionStatus"),
        ("LUM-WDM-MIB", "wdmVc4ConnectedForeignIndex"),
        ("LUM-WDM-MIB", "wdmVc4AdminStatus"))
)
if mibBuilder.loadTexts:
    wdmVc4GroupV2.setStatus("current")

wdmCtrlChannelGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 53)
)
wdmCtrlChannelGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlChannelIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelName"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSlot"),
        ("LUM-WDM-MIB", "wdmCtrlChannelTxPort"),
        ("LUM-WDM-MIB", "wdmCtrlChannelChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelWantedOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelOuputPowerControlFailure"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentPowerOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenuationOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelMonitorIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupCommand"))
)
if mibBuilder.loadTexts:
    wdmCtrlChannelGroupV2.setStatus("deprecated")

wdmCtrlGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 54)
)
wdmCtrlGlobalGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlGlobalRegulationInterval"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalRegulationStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalLastRegulation"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalTimeLeft"))
)
if mibBuilder.loadTexts:
    wdmCtrlGlobalGroup.setStatus("current")

wdmSubChannelGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 55)
)
wdmSubChannelGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmSubChannelIndex"),
        ("LUM-WDM-MIB", "wdmSubChannelName"),
        ("LUM-WDM-MIB", "wdmSubChannelId"),
        ("LUM-WDM-MIB", "wdmSubChannelType"),
        ("LUM-WDM-MIB", "wdmSubChannelUnequipped"),
        ("LUM-WDM-MIB", "wdmSubChannelConnectionStatus"),
        ("LUM-WDM-MIB", "wdmSubChannelConnectedForeignIndex"),
        ("LUM-WDM-MIB", "wdmSubChannelCrossConnect"),
        ("LUM-WDM-MIB", "wdmSubChannelDisconnect"),
        ("LUM-WDM-MIB", "wdmSubChannelRemoteAccessInterface"),
        ("LUM-WDM-MIB", "wdmSubChannelProtectedChannelIndex"))
)
if mibBuilder.loadTexts:
    wdmSubChannelGroupV2.setStatus("current")

wdmProtGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 56)
)
wdmProtGroupV7.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"),
        ("LUM-WDM-MIB", "wdmProtObjectProperty"),
        ("LUM-WDM-MIB", "wdmProtWrapperMode"),
        ("LUM-WDM-MIB", "wdmProtWrapperState"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftCommPort"),
        ("LUM-WDM-MIB", "wdmProtRightCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightCommSlot"),
        ("LUM-WDM-MIB", "wdmProtRightCommPort"),
        ("LUM-WDM-MIB", "wdmProtLeftCommInterface"),
        ("LUM-WDM-MIB", "wdmProtRightCommInterface"),
        ("LUM-WDM-MIB", "wdmProtCommunicationFailure"),
        ("LUM-WDM-MIB", "wdmProtHubTrafficConfigMismatch"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV7.setStatus("deprecated")

wdmIfGroupV24 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 57)
)
wdmIfGroupV24.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV24.setStatus("deprecated")

wdmIfGroupV25 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 58)
)
wdmIfGroupV25.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"),
        ("LUM-WDM-MIB", "wdmIfActualFormat"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV25.setStatus("deprecated")

wdmCtrlChannelGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 59)
)
wdmCtrlChannelGroupV3.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlChannelIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelName"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSlot"),
        ("LUM-WDM-MIB", "wdmCtrlChannelTxPort"),
        ("LUM-WDM-MIB", "wdmCtrlChannelChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelWantedOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelOuputPowerControlFailure"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentPowerOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenuationOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelMonitorIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSfpMissing"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSfpMediaMismatch"),
        ("LUM-WDM-MIB", "wdmCtrlChannelLossOfSignal"))
)
if mibBuilder.loadTexts:
    wdmCtrlChannelGroupV3.setStatus("deprecated")

wdmIfGroupV26 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 60)
)
wdmIfGroupV26.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"),
        ("LUM-WDM-MIB", "wdmIfActualFormat"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersion"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionCommand"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionMode"),
        ("LUM-WDM-MIB", "wdmIfLineControlLoopCurrentState"),
        ("LUM-WDM-MIB", "wdmIfSignalDegradeThreshold"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV26.setStatus("deprecated")

wdmProtGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 61)
)
wdmProtGroupV8.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"),
        ("LUM-WDM-MIB", "wdmProtObjectProperty"),
        ("LUM-WDM-MIB", "wdmProtWrapperMode"),
        ("LUM-WDM-MIB", "wdmProtWrapperState"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftCommPort"),
        ("LUM-WDM-MIB", "wdmProtRightCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightCommSlot"),
        ("LUM-WDM-MIB", "wdmProtRightCommPort"),
        ("LUM-WDM-MIB", "wdmProtLeftCommInterface"),
        ("LUM-WDM-MIB", "wdmProtRightCommInterface"),
        ("LUM-WDM-MIB", "wdmProtCommunicationFailure"),
        ("LUM-WDM-MIB", "wdmProtHubTrafficConfigMismatch"),
        ("LUM-WDM-MIB", "wdmProtSignalDegradeProtection"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV8.setStatus("deprecated")

wdmProtGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 62)
)
wdmProtGroupV9.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtDescr"),
        ("LUM-WDM-MIB", "wdmProtLeftSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftPort"),
        ("LUM-WDM-MIB", "wdmProtRightSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightSlot"),
        ("LUM-WDM-MIB", "wdmProtRightPort"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"),
        ("LUM-WDM-MIB", "wdmProtAdminStatus"),
        ("LUM-WDM-MIB", "wdmProtRowStatus"),
        ("LUM-WDM-MIB", "wdmProtServiceDegraded"),
        ("LUM-WDM-MIB", "wdmProtServiceFailure"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtProtectionType"),
        ("LUM-WDM-MIB", "wdmProtObjectProperty"),
        ("LUM-WDM-MIB", "wdmProtWrapperMode"),
        ("LUM-WDM-MIB", "wdmProtWrapperState"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtLeftCommSlot"),
        ("LUM-WDM-MIB", "wdmProtLeftCommPort"),
        ("LUM-WDM-MIB", "wdmProtRightCommSubrack"),
        ("LUM-WDM-MIB", "wdmProtRightCommSlot"),
        ("LUM-WDM-MIB", "wdmProtRightCommPort"),
        ("LUM-WDM-MIB", "wdmProtLeftCommInterface"),
        ("LUM-WDM-MIB", "wdmProtRightCommInterface"),
        ("LUM-WDM-MIB", "wdmProtCommunicationFailure"),
        ("LUM-WDM-MIB", "wdmProtHubTrafficConfigMismatch"),
        ("LUM-WDM-MIB", "wdmProtSignalDegradeProtection"),
        ("LUM-WDM-MIB", "wdmProtRevertiveSwitch"),
        ("LUM-WDM-MIB", "wdmProtRevertiveSwitchWtrTimer"),
        ("LUM-WDM-MIB", "wdmProtRevertiveSwitchPrimaryPath"),
        ("LUM-WDM-MIB", "wdmProtRevertiveSwitchSecondaryPath"),
        ("LUM-WDM-MIB", "wdmProtSecondaryPathUsed"))
)
if mibBuilder.loadTexts:
    wdmProtGroupV9.setStatus("current")

wdmCtrlGroupGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 63)
)
wdmCtrlGroupGroupV3.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlGroupIndex"),
        ("LUM-WDM-MIB", "wdmCtrlGroupName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupDescr"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSlot"),
        ("LUM-WDM-MIB", "wdmCtrlGroupPort"),
        ("LUM-WDM-MIB", "wdmCtrlGroupMonitorName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupControlMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupLockedRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationLastChangeTime"),
        ("LUM-WDM-MIB", "wdmCtrlGroupCommissioningMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAssociateChannel"),
        ("LUM-WDM-MIB", "wdmCtrlGroupNoOfChannels"),
        ("LUM-WDM-MIB", "wdmCtrlGroupStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupTimeLeft"),
        ("LUM-WDM-MIB", "wdmCtrlGroupOutputPowerMismatch"))
)
if mibBuilder.loadTexts:
    wdmCtrlGroupGroupV3.setStatus("deprecated")

wdmIfGroupV27 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 64)
)
wdmIfGroupV27.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"),
        ("LUM-WDM-MIB", "wdmIfActualFormat"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersion"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionCommand"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionMode"),
        ("LUM-WDM-MIB", "wdmIfLineControlLoopCurrentState"),
        ("LUM-WDM-MIB", "wdmIfSignalDegradeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxThresholdOptimizationState"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV27.setStatus("deprecated")

wdmIfGroupV28 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 65)
)
wdmIfGroupV28.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"),
        ("LUM-WDM-MIB", "wdmIfActualFormat"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersion"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionCommand"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionMode"),
        ("LUM-WDM-MIB", "wdmIfLineControlLoopCurrentState"),
        ("LUM-WDM-MIB", "wdmIfSignalDegradeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfTrxDecisionThreshold"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV28.setStatus("deprecated")

wdmIfGroupV29 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 66)
)
wdmIfGroupV29.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"),
        ("LUM-WDM-MIB", "wdmIfActualFormat"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersion"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionCommand"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionMode"),
        ("LUM-WDM-MIB", "wdmIfLineControlLoopCurrentState"),
        ("LUM-WDM-MIB", "wdmIfSignalDegradeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfTrxDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfSwControlledLaserShutdown"),
        ("LUM-WDM-MIB", "wdmIfChangeSwControlledLaserShutdownCommand"),
        ("LUM-WDM-MIB", "wdmIfControlledLaserShutdownEnabled"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV29.setStatus("deprecated")

wdmDelayCompPGGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 67)
)
wdmDelayCompPGGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmDelayCompPGIndex"),
        ("LUM-WDM-MIB", "wdmDelayCompPGName"),
        ("LUM-WDM-MIB", "wdmDelayCompPGUpId"),
        ("LUM-WDM-MIB", "wdmDelayCompPGAdminStatus"),
        ("LUM-WDM-MIB", "wdmDelayCompPGOperStatus"),
        ("LUM-WDM-MIB", "wdmDelayCompPGAutoCompensationMode"),
        ("LUM-WDM-MIB", "wdmDelayCompPGAutoCompensationState"),
        ("LUM-WDM-MIB", "wdmDelayCompPGDelayDifference"),
        ("LUM-WDM-MIB", "wdmDelayCompPGDelayCompensationOOR"),
        ("LUM-WDM-MIB", "wdmDelayCompPGFiberLengthDifferenceOOR"),
        ("LUM-WDM-MIB", "wdmDelayCompPGDelayCompensationReset"))
)
if mibBuilder.loadTexts:
    wdmDelayCompPGGroup.setStatus("current")

wdmDelayCompLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 68)
)
wdmDelayCompLinkGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmDelayCompLinkIndex"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkName"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkUpId"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkCurrentDelayCompensation"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkWantedDelayCompensation"))
)
if mibBuilder.loadTexts:
    wdmDelayCompLinkGroup.setStatus("current")

wdmCtrlChannelGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 69)
)
wdmCtrlChannelGroupV4.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlChannelIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelName"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSlot"),
        ("LUM-WDM-MIB", "wdmCtrlChannelTxPort"),
        ("LUM-WDM-MIB", "wdmCtrlChannelChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelWantedOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelOuputPowerControlFailure"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentPowerOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenuationOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelMonitorIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSfpMissing"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSfpMediaMismatch"),
        ("LUM-WDM-MIB", "wdmCtrlChannelLossOfSignal"),
        ("LUM-WDM-MIB", "wdmCtrlChannelDescr"))
)
if mibBuilder.loadTexts:
    wdmCtrlChannelGroupV4.setStatus("deprecated")

wdmIfGroupV30 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 70)
)
wdmIfGroupV30.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfContinousOptimization"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationResultCause"),
        ("LUM-WDM-MIB", "wdmIfDistributionRole"),
        ("LUM-WDM-MIB", "wdmIfConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmIfNoFrequencySet"),
        ("LUM-WDM-MIB", "wdmIfFormat"),
        ("LUM-WDM-MIB", "wdmIfConfigurationFormatCommand"),
        ("LUM-WDM-MIB", "wdmIfLinkDown"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationMode"),
        ("LUM-WDM-MIB", "wdmIfAutoNegotiationStatus"),
        ("LUM-WDM-MIB", "wdmIfFlowControlMode"),
        ("LUM-WDM-MIB", "wdmIfGroupLineMode"),
        ("LUM-WDM-MIB", "wdmIfFecType"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfFarEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfFecFailure"),
        ("LUM-WDM-MIB", "wdmIfTxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfRxSignalStatus"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopback"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackTimeout"),
        ("LUM-WDM-MIB", "wdmIfNearEndLoopbackEnabled"),
        ("LUM-WDM-MIB", "wdmIfChangeNearEndLoopbackCommand"),
        ("LUM-WDM-MIB", "wdmIfSignalDegraded"),
        ("LUM-WDM-MIB", "wdmIfHubProtectionMode"),
        ("LUM-WDM-MIB", "wdmIfActualFormat"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersion"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionCommand"),
        ("LUM-WDM-MIB", "wdmIfTdcDispersionMode"),
        ("LUM-WDM-MIB", "wdmIfLineControlLoopCurrentState"),
        ("LUM-WDM-MIB", "wdmIfSignalDegradeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfTrxDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfSwControlledLaserShutdown"),
        ("LUM-WDM-MIB", "wdmIfChangeSwControlledLaserShutdownCommand"),
        ("LUM-WDM-MIB", "wdmIfControlledLaserShutdownEnabled"),
        ("LUM-WDM-MIB", "wdmIfAid"),
        ("LUM-WDM-MIB", "wdmIfPhysicalLocation"))
)
if mibBuilder.loadTexts:
    wdmIfGroupV30.setStatus("current")

wdmPassiveIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 71)
)
wdmPassiveIfGroupV7.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfUnexpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfOperStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmPassiveIfAid"),
        ("LUM-WDM-MIB", "wdmPassiveIfPhysicalLocation"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfGroupV7.setStatus("current")

wdmMeanChannelPowerControlGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 72)
)
wdmMeanChannelPowerControlGroupV1.setObjects(
      *(("LUM-WDM-MIB", "wdmMeanChannelPowerControlIndex"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlName"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlDescr"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOcmSubrack"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOcmSlot"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOcmPort"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOaSubrack"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOaSlot"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOaPort"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlMonitorName"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlAdminStatus"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlOperStatus"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlStartRegulation"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlRegulationRange"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlLatestRegulation"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlLatestChange"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlMonitorOffsetCalibrationFailed"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlRegulationState"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlTimeToNextRegulation"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlWantedChannelPower"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlCurrentChannelPower"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlCurrentGain"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlTotalChannelOutputPower"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlNumberOfChannels"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlAbsolutePowerOffset"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlRemainingPowerOffset"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlMonitorOffsetTooLarge"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlChannelPowerOutOfRange"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlRegulationInterval"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlAmplifierOutputPort"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlLatestAmplifierRxPower"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlLatestAmplifierTxPower"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlLocalId"))
)
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGroupV1.setStatus("current")

wdmMeanChannelPowerControlGlobalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 73)
)
wdmMeanChannelPowerControlGlobalGroupV1.setObjects(
      *(("LUM-WDM-MIB", "wdmMeanChannelPowerControlGlobalIndex"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlGlobalName"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlGlobalEntryCreate"))
)
if mibBuilder.loadTexts:
    wdmMeanChannelPowerControlGlobalGroupV1.setStatus("current")

wdmGeneralGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 74)
)
wdmGeneralGroupV7.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralStateLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralWdmIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmPassiveIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmProtTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmVc4TableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmCtrlChannelTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmCtrlGroupTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmSubChannelTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmMeanChannelPowerControlTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmMeanChannelPowerControlGlobalTableSize"))
)
if mibBuilder.loadTexts:
    wdmGeneralGroupV7.setStatus("current")

wdmCtrlGroupGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 75)
)
wdmCtrlGroupGroupV4.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlGroupIndex"),
        ("LUM-WDM-MIB", "wdmCtrlGroupName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupDescr"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSlot"),
        ("LUM-WDM-MIB", "wdmCtrlGroupPort"),
        ("LUM-WDM-MIB", "wdmCtrlGroupMonitorName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupControlMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupLockedRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationLastChangeTime"),
        ("LUM-WDM-MIB", "wdmCtrlGroupCommissioningMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAssociateChannel"),
        ("LUM-WDM-MIB", "wdmCtrlGroupNoOfChannels"),
        ("LUM-WDM-MIB", "wdmCtrlGroupStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupTimeLeft"),
        ("LUM-WDM-MIB", "wdmCtrlGroupOutputPowerMismatch"),
        ("LUM-WDM-MIB", "wdmCtrlGroupTotalPower"))
)
if mibBuilder.loadTexts:
    wdmCtrlGroupGroupV4.setStatus("deprecated")

wdmCtrlGroupGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 76)
)
wdmCtrlGroupGroupV5.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlGroupIndex"),
        ("LUM-WDM-MIB", "wdmCtrlGroupName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupDescr"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlGroupSlot"),
        ("LUM-WDM-MIB", "wdmCtrlGroupPort"),
        ("LUM-WDM-MIB", "wdmCtrlGroupMonitorName"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupControlMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupConfigurationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlGroupLockedRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationRange"),
        ("LUM-WDM-MIB", "wdmCtrlGroupRegulationLastChangeTime"),
        ("LUM-WDM-MIB", "wdmCtrlGroupCommissioningMode"),
        ("LUM-WDM-MIB", "wdmCtrlGroupAssociateChannel"),
        ("LUM-WDM-MIB", "wdmCtrlGroupNoOfChannels"),
        ("LUM-WDM-MIB", "wdmCtrlGroupStatus"),
        ("LUM-WDM-MIB", "wdmCtrlGroupTimeLeft"),
        ("LUM-WDM-MIB", "wdmCtrlGroupOutputPowerMismatch"),
        ("LUM-WDM-MIB", "wdmCtrlGroupTotalPower"),
        ("LUM-WDM-MIB", "wdmCtrlGroupChannelStartupCommand"))
)
if mibBuilder.loadTexts:
    wdmCtrlGroupGroupV5.setStatus("current")

wdmCtrlChannelGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 77)
)
wdmCtrlChannelGroupV5.setObjects(
      *(("LUM-WDM-MIB", "wdmCtrlChannelIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelName"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSubrack"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSlot"),
        ("LUM-WDM-MIB", "wdmCtrlChannelTxPort"),
        ("LUM-WDM-MIB", "wdmCtrlChannelChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupNumber"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAdminStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelWantedOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentOutputPower"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelForceRegulationCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelOuputPowerControlFailure"),
        ("LUM-WDM-MIB", "wdmCtrlChannelCurrentPowerOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenuationOutOfRange"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStatus"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupChannel"),
        ("LUM-WDM-MIB", "wdmCtrlChannelMonitorIndex"),
        ("LUM-WDM-MIB", "wdmCtrlChannelStartupCommand"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSfpMissing"),
        ("LUM-WDM-MIB", "wdmCtrlChannelSfpMediaMismatch"),
        ("LUM-WDM-MIB", "wdmCtrlChannelLossOfSignal"),
        ("LUM-WDM-MIB", "wdmCtrlChannelDescr"),
        ("LUM-WDM-MIB", "wdmCtrlChannelMaxAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelMinAttenuation"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenControlOffset"),
        ("LUM-WDM-MIB", "wdmCtrlChannelAttenControlDegraded"))
)
if mibBuilder.loadTexts:
    wdmCtrlChannelGroupV5.setStatus("current")

wdmGeneralMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 3, 1)
)
wdmGeneralMinimalGroupV1.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralStateLastChangeTime"),
        ("LUM-WDM-MIB", "wdmGeneralWdmIfTableSize"),
        ("LUM-WDM-MIB", "wdmGeneralWdmPassiveIfTableSize"))
)
if mibBuilder.loadTexts:
    wdmGeneralMinimalGroupV1.setStatus("current")

wdmIfMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 3, 2)
)
wdmIfMinimalGroupV1.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"))
)
if mibBuilder.loadTexts:
    wdmIfMinimalGroupV1.setStatus("deprecated")

wdmPassiveIfMinimalGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 3, 3)
)
wdmPassiveIfMinimalGroupV1.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfUnexpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfOperStatus"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfMinimalGroupV1.setStatus("deprecated")

wdmIfMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 3, 4)
)
wdmIfMinimalGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfDescr"),
        ("LUM-WDM-MIB", "wdmIfSubrack"),
        ("LUM-WDM-MIB", "wdmIfSlot"),
        ("LUM-WDM-MIB", "wdmIfTxPort"),
        ("LUM-WDM-MIB", "wdmIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmIfTxLambda"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMin"),
        ("LUM-WDM-MIB", "wdmIfHighSpeedMax"),
        ("LUM-WDM-MIB", "wdmIfPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelHighThreshold"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTemp"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffset"),
        ("LUM-WDM-MIB", "wdmIfLaserTempOffsetThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserMode"),
        ("LUM-WDM-MIB", "wdmIfLaserStatus"),
        ("LUM-WDM-MIB", "wdmIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmIfOperStatus"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignal"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerHigh"),
        ("LUM-WDM-MIB", "wdmIfReceivedPowerLow"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasHigh"),
        ("LUM-WDM-MIB", "wdmIfForwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfBackwardDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfFrame"),
        ("LUM-WDM-MIB", "wdmIfAlarmIndicationSignal"),
        ("LUM-WDM-MIB", "wdmIfRemoteDefectIndication"),
        ("LUM-WDM-MIB", "wdmIfLossOfSync"),
        ("LUM-WDM-MIB", "wdmIfLossOfForwardingErrorCorrection"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHigh"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLow"),
        ("LUM-WDM-MIB", "wdmIfRxPort"),
        ("LUM-WDM-MIB", "wdmIfBitrateMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserBias"),
        ("LUM-WDM-MIB", "wdmIfLaserBiasThreshold"),
        ("LUM-WDM-MIB", "wdmIfLossOfSignalThreshold"),
        ("LUM-WDM-MIB", "wdmIfExpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfForwardingErrorCorrectionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceIntrusionMode"),
        ("LUM-WDM-MIB", "wdmIfTraceTransmitted"),
        ("LUM-WDM-MIB", "wdmIfTraceReceived"),
        ("LUM-WDM-MIB", "wdmIfTraceExpected"),
        ("LUM-WDM-MIB", "wdmIfTraceAlarmMode"),
        ("LUM-WDM-MIB", "wdmIfTraceMismatch"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"),
        ("LUM-WDM-MIB", "wdmIfSuppressRemoteAlarms"),
        ("LUM-WDM-MIB", "wdmIfSerialNumberMismatch"),
        ("LUM-WDM-MIB", "wdmIfOptimizeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfThresholdOptimizationState"),
        ("LUM-WDM-MIB", "wdmIfUseHwDefaultDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedZeros"),
        ("LUM-WDM-MIB", "wdmIfFecCorrectedOnes"),
        ("LUM-WDM-MIB", "wdmIfOptimizedForSerialNumber"),
        ("LUM-WDM-MIB", "wdmIfRelativeDecisionThreshold"),
        ("LUM-WDM-MIB", "wdmIfTrxCodeMismatch"),
        ("LUM-WDM-MIB", "wdmIfTrxBitrateUnavailable"),
        ("LUM-WDM-MIB", "wdmIfTrxMissing"),
        ("LUM-WDM-MIB", "wdmIfTrxClass"),
        ("LUM-WDM-MIB", "wdmIfLaserTempHighRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfLaserTempLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfTransmitterFailed"),
        ("LUM-WDM-MIB", "wdmIfReceiverSensitivity"),
        ("LUM-WDM-MIB", "wdmIfPowerLevelLowRelativeThreshold"),
        ("LUM-WDM-MIB", "wdmIfUnexpectedTxLambda"),
        ("LUM-WDM-MIB", "wdmIfIllegalFrequency"),
        ("LUM-WDM-MIB", "wdmIfLaserForcedOn"),
        ("LUM-WDM-MIB", "wdmIfTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfSelectTrafficCombination"),
        ("LUM-WDM-MIB", "wdmIfObjectProperty"),
        ("LUM-WDM-MIB", "wdmIfTxPowerLevel"),
        ("LUM-WDM-MIB", "wdmIfLaserTempActual"),
        ("LUM-WDM-MIB", "wdmIfTrxFailed"),
        ("LUM-WDM-MIB", "wdmIfDisabled"),
        ("LUM-WDM-MIB", "wdmIfLoopback"))
)
if mibBuilder.loadTexts:
    wdmIfMinimalGroupV2.setStatus("current")

wdmPassiveIfMinimalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 3, 5)
)
wdmPassiveIfMinimalGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmPassiveIfIndex"),
        ("LUM-WDM-MIB", "wdmPassiveIfName"),
        ("LUM-WDM-MIB", "wdmPassiveIfDescr"),
        ("LUM-WDM-MIB", "wdmPassiveIfInvPhysIndexOrZero"),
        ("LUM-WDM-MIB", "wdmPassiveIfSubrack"),
        ("LUM-WDM-MIB", "wdmPassiveIfSlot"),
        ("LUM-WDM-MIB", "wdmPassiveIfPort"),
        ("LUM-WDM-MIB", "wdmPassiveIfDirection"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambdaType"),
        ("LUM-WDM-MIB", "wdmPassiveIfLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfExpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfUnexpectedLambda"),
        ("LUM-WDM-MIB", "wdmPassiveIfAdminStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfOperStatus"),
        ("LUM-WDM-MIB", "wdmPassiveIfIfNo"))
)
if mibBuilder.loadTexts:
    wdmPassiveIfMinimalGroupV2.setStatus("current")


# Notification objects

wdmProtOperStatusBothDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 1)
)
wdmProtOperStatusBothDown.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusBothDown.setStatus(
        "deprecated"
    )

wdmProtOperStatusLeftDownRightUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 2)
)
wdmProtOperStatusLeftDownRightUp.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusLeftDownRightUp.setStatus(
        "deprecated"
    )

wdmProtOperStatusLeftDownRightStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 3)
)
wdmProtOperStatusLeftDownRightStandby.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusLeftDownRightStandby.setStatus(
        "deprecated"
    )

wdmProtOperStatusLeftStandbyRightDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 4)
)
wdmProtOperStatusLeftStandbyRightDown.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusLeftStandbyRightDown.setStatus(
        "deprecated"
    )

wdmProtOperStatusLeftStandbyRightUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 5)
)
wdmProtOperStatusLeftStandbyRightUp.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusLeftStandbyRightUp.setStatus(
        "deprecated"
    )

wdmProtOperStatusLeftUpRightDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 6)
)
wdmProtOperStatusLeftUpRightDown.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusLeftUpRightDown.setStatus(
        "deprecated"
    )

wdmProtOperStatusLeftUpRightStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 7)
)
wdmProtOperStatusLeftUpRightStandby.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"))
)
if mibBuilder.loadTexts:
    wdmProtOperStatusLeftUpRightStandby.setStatus(
        "deprecated"
    )

wdmIfLaserStatusOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 8)
)
wdmIfLaserStatusOn.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmIfLaserStatusOn.setStatus(
        "current"
    )

wdmIfLaserStatusOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 9)
)
wdmIfLaserStatusOff.setObjects(
      *(("LUM-WDM-MIB", "wdmIfIndex"),
        ("LUM-WDM-MIB", "wdmIfName"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmIfLaserStatusOff.setStatus(
        "current"
    )

wdmProtStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 2, 4, 0, 10)
)
wdmProtStatusChanged.setObjects(
      *(("LUM-WDM-MIB", "wdmProtIndex"),
        ("LUM-WDM-MIB", "wdmProtName"),
        ("LUM-WDM-MIB", "wdmProtActiveSide"),
        ("LUM-WDM-MIB", "wdmProtLeftStatus"),
        ("LUM-WDM-MIB", "wdmProtRightStatus"),
        ("LUM-WDM-MIB", "wdmProtLastChangeTime"))
)
if mibBuilder.loadTexts:
    wdmProtStatusChanged.setStatus(
        "current"
    )


# Notifications groups

wdmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 4)
)
wdmNotificationGroup.setObjects(
      *(("LUM-WDM-MIB", "wdmProtOperStatusBothDown"),
        ("LUM-WDM-MIB", "wdmProtOperStatusLeftDownRightUp"),
        ("LUM-WDM-MIB", "wdmProtOperStatusLeftDownRightStandby"),
        ("LUM-WDM-MIB", "wdmProtOperStatusLeftStandbyRightDown"),
        ("LUM-WDM-MIB", "wdmProtOperStatusLeftStandbyRightUp"),
        ("LUM-WDM-MIB", "wdmProtOperStatusLeftUpRightDown"),
        ("LUM-WDM-MIB", "wdmProtOperStatusLeftUpRightStandby"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusOn"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusOff"))
)
if mibBuilder.loadTexts:
    wdmNotificationGroup.setStatus(
        "deprecated"
    )

wdmNotificationGroupV2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 1, 16)
)
wdmNotificationGroupV2.setObjects(
      *(("LUM-WDM-MIB", "wdmIfLaserStatusOn"),
        ("LUM-WDM-MIB", "wdmIfLaserStatusOff"),
        ("LUM-WDM-MIB", "wdmProtStatusChanged"))
)
if mibBuilder.loadTexts:
    wdmNotificationGroupV2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumWdmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 1)
)
lumWdmBasicComplV1.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroup"),
        ("LUM-WDM-MIB", "wdmIfGroup"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV1.setStatus(
        "deprecated"
    )

lumWdmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 2)
)
lumWdmBasicComplV2.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroup"),
        ("LUM-WDM-MIB", "wdmIfGroup"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV2.setStatus(
        "deprecated"
    )

lumWdmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 3)
)
lumWdmBasicComplV3.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroup"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV3.setStatus(
        "deprecated"
    )

lumWdmBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 4)
)
lumWdmBasicComplV4.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV2"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV4.setStatus(
        "deprecated"
    )

lumWdmBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 5)
)
lumWdmBasicComplV5.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV3"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV2"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV5.setStatus(
        "deprecated"
    )

lumWdmBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 6)
)
lumWdmBasicComplV6.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV4"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV3"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV6.setStatus(
        "deprecated"
    )

lumWdmBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 7)
)
lumWdmBasicComplV7.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV4"),
        ("LUM-WDM-MIB", "wdmProtGroup"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV7.setStatus(
        "deprecated"
    )

lumWdmBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 8)
)
lumWdmBasicComplV8.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV5"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV8.setStatus(
        "deprecated"
    )

lumWdmBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 9)
)
lumWdmBasicComplV9.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV6"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroup"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV9.setStatus(
        "deprecated"
    )

lumWdmBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 10)
)
lumWdmBasicComplV10.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV6"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV10.setStatus(
        "deprecated"
    )

lumWdmBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 11)
)
lumWdmBasicComplV11.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV2"),
        ("LUM-WDM-MIB", "wdmIfGroupV7"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV11.setStatus(
        "deprecated"
    )

lumWdmBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 12)
)
lumWdmBasicComplV12.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV7"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV12.setStatus(
        "deprecated"
    )

lumWdmBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 13)
)
lumWdmBasicComplV13.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV8"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV13.setStatus(
        "deprecated"
    )

lumWdmBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 14)
)
lumWdmBasicComplV14.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV9"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV14.setStatus(
        "deprecated"
    )

lumWdmBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 15)
)
lumWdmBasicComplV15.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV10"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV15.setStatus(
        "deprecated"
    )

lumWdmBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 16)
)
lumWdmBasicComplV16.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV11"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV4"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV16.setStatus(
        "deprecated"
    )

lumWdmBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 17)
)
lumWdmBasicComplV17.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV12"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV5"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV17.setStatus(
        "deprecated"
    )

lumWdmBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 18)
)
lumWdmBasicComplV18.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV3"),
        ("LUM-WDM-MIB", "wdmIfGroupV13"),
        ("LUM-WDM-MIB", "wdmProtGroupV2"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV5"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV18.setStatus(
        "deprecated"
    )

lumWdmBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 19)
)
lumWdmBasicComplV19.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV13"),
        ("LUM-WDM-MIB", "wdmProtGroupV3"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV5"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV19.setStatus(
        "deprecated"
    )

lumWdmBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 20)
)
lumWdmBasicComplV20.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV14"),
        ("LUM-WDM-MIB", "wdmProtGroupV4"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV20.setStatus(
        "deprecated"
    )

lumWdmBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 21)
)
lumWdmBasicComplV21.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV14"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV21.setStatus(
        "deprecated"
    )

lumWdmBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 22)
)
lumWdmBasicComplV22.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV15"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV22.setStatus(
        "deprecated"
    )

lumWdmBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 23)
)
lumWdmBasicComplV23.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV16"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV23.setStatus(
        "deprecated"
    )

lumWdmBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 24)
)
lumWdmBasicComplV24.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV16"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV24.setStatus(
        "deprecated"
    )

lumWdmBasicComplV25 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 25)
)
lumWdmBasicComplV25.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV17"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV25.setStatus(
        "deprecated"
    )

lumWdmBasicComplV26 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 26)
)
lumWdmBasicComplV26.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV4"),
        ("LUM-WDM-MIB", "wdmIfGroupV18"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV26.setStatus(
        "deprecated"
    )

lumWdmBasicComplV27 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 27)
)
lumWdmBasicComplV27.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV5"),
        ("LUM-WDM-MIB", "wdmIfGroupV19"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4Group"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV27.setStatus(
        "deprecated"
    )

lumWdmBasicComplV28 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 28)
)
lumWdmBasicComplV28.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV5"),
        ("LUM-WDM-MIB", "wdmIfGroupV20"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4Group"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV28.setStatus(
        "deprecated"
    )

lumWdmBasicComplV29 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 29)
)
lumWdmBasicComplV29.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV5"),
        ("LUM-WDM-MIB", "wdmIfGroupV21"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4Group"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV29.setStatus(
        "deprecated"
    )

lumWdmBasicComplV30 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 30)
)
lumWdmBasicComplV30.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV5"),
        ("LUM-WDM-MIB", "wdmIfGroupV22"),
        ("LUM-WDM-MIB", "wdmProtGroupV6"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4Group"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroup"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV30.setStatus(
        "deprecated"
    )

lumWdmBasicComplV31 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 31)
)
lumWdmBasicComplV31.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV5"),
        ("LUM-WDM-MIB", "wdmIfGroupV22"),
        ("LUM-WDM-MIB", "wdmProtGroupV6"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4Group"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroup"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV31.setStatus(
        "deprecated"
    )

lumWdmBasicComplV32 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 32)
)
lumWdmBasicComplV32.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV23"),
        ("LUM-WDM-MIB", "wdmProtGroupV6"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4Group"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroup"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV32.setStatus(
        "deprecated"
    )

lumWdmBasicComplV33 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 33)
)
lumWdmBasicComplV33.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV23"),
        ("LUM-WDM-MIB", "wdmProtGroupV6"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV33.setStatus(
        "deprecated"
    )

lumWdmBasicComplV34 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 34)
)
lumWdmBasicComplV34.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV24"),
        ("LUM-WDM-MIB", "wdmProtGroupV7"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV34.setStatus(
        "deprecated"
    )

lumWdmBasicComplV35 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 35)
)
lumWdmBasicComplV35.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV25"),
        ("LUM-WDM-MIB", "wdmProtGroupV7"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV35.setStatus(
        "deprecated"
    )

lumWdmBasicComplV36 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 36)
)
lumWdmBasicComplV36.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV25"),
        ("LUM-WDM-MIB", "wdmProtGroupV7"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV3"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV36.setStatus(
        "deprecated"
    )

lumWdmBasicComplV37 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 37)
)
lumWdmBasicComplV37.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV26"),
        ("LUM-WDM-MIB", "wdmProtGroupV8"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV3"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV37.setStatus(
        "deprecated"
    )

lumWdmBasicComplV38 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 38)
)
lumWdmBasicComplV38.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV26"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV3"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV2"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV38.setStatus(
        "deprecated"
    )

lumWdmBasicComplV39 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 39)
)
lumWdmBasicComplV39.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV27"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV3"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV3"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV39.setStatus(
        "deprecated"
    )

lumWdmBasicComplV40 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 40)
)
lumWdmBasicComplV40.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV28"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV3"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV3"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV40.setStatus(
        "deprecated"
    )

lumWdmBasicComplV41 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 41)
)
lumWdmBasicComplV41.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV29"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV3"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV3"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV41.setStatus(
        "deprecated"
    )

lumWdmBasicComplV42 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 42)
)
lumWdmBasicComplV42.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV7"),
        ("LUM-WDM-MIB", "wdmIfGroupV29"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV6"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV4"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV3"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompPGGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkGroup"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlGroupV1"),
        ("LUM-WDM-MIB", "wdmMeanChannelPowerControlGlobalGroupV1"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV42.setStatus(
        "deprecated"
    )

lumWdmBasicComplV43 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 43)
)
lumWdmBasicComplV43.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV30"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV7"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV4"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV3"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompPGGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV43.setStatus(
        "deprecated"
    )

lumWdmBasicComplV44 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 44)
)
lumWdmBasicComplV44.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV30"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV7"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV4"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV4"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompPGGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV44.setStatus(
        "deprecated"
    )

lumWdmBasicComplV45 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 45)
)
lumWdmBasicComplV45.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV30"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV7"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV5"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV5"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompPGGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV45.setStatus(
        "deprecated"
    )

lumWdmBasicComplV46 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 2, 46)
)
lumWdmBasicComplV46.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralGroupV6"),
        ("LUM-WDM-MIB", "wdmIfGroupV30"),
        ("LUM-WDM-MIB", "wdmProtGroupV9"),
        ("LUM-WDM-MIB", "wdmNotificationGroupV2"),
        ("LUM-WDM-MIB", "wdmPassiveIfGroupV7"),
        ("LUM-WDM-MIB", "wdmVc4GroupV2"),
        ("LUM-WDM-MIB", "wdmRemoteProtGroup"),
        ("LUM-WDM-MIB", "wdmCtrlChannelGroupV5"),
        ("LUM-WDM-MIB", "wdmCtrlGroupGroupV5"),
        ("LUM-WDM-MIB", "wdmSubChannelGroupV2"),
        ("LUM-WDM-MIB", "wdmCtrlGlobalGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompPGGroup"),
        ("LUM-WDM-MIB", "wdmDelayCompLinkGroup"))
)
if mibBuilder.loadTexts:
    lumWdmBasicComplV46.setStatus(
        "current"
    )

lumWdmMinimalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 4, 1)
)
lumWdmMinimalComplV1.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralMinimalGroupV1"),
        ("LUM-WDM-MIB", "wdmIfMinimalGroupV1"),
        ("LUM-WDM-MIB", "wdmPassiveIfMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumWdmMinimalComplV1.setStatus(
        "deprecated"
    )

lumWdmMinimalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 4, 2)
)
lumWdmMinimalComplV2.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralMinimalGroupV1"),
        ("LUM-WDM-MIB", "wdmIfMinimalGroupV2"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmPassiveIfMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumWdmMinimalComplV2.setStatus(
        "deprecated"
    )

lumWdmMinimalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 4, 3)
)
lumWdmMinimalComplV3.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralMinimalGroupV1"),
        ("LUM-WDM-MIB", "wdmIfMinimalGroupV2"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmPassiveIfMinimalGroupV1"))
)
if mibBuilder.loadTexts:
    lumWdmMinimalComplV3.setStatus(
        "deprecated"
    )

lumWdmMinimalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 4, 1, 4, 4)
)
lumWdmMinimalComplV4.setObjects(
      *(("LUM-WDM-MIB", "wdmGeneralMinimalGroupV1"),
        ("LUM-WDM-MIB", "wdmIfMinimalGroupV2"),
        ("LUM-WDM-MIB", "wdmProtGroupV5"),
        ("LUM-WDM-MIB", "wdmPassiveIfMinimalGroupV2"))
)
if mibBuilder.loadTexts:
    lumWdmMinimalComplV4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-WDM-MIB",
    **{"lumWdmMIBModule": lumWdmMIBModule,
       "lumWdmConfs": lumWdmConfs,
       "lumWdmGroups": lumWdmGroups,
       "wdmGeneralGroup": wdmGeneralGroup,
       "wdmIfGroup": wdmIfGroup,
       "wdmProtGroup": wdmProtGroup,
       "wdmNotificationGroup": wdmNotificationGroup,
       "wdmPassiveIfGroup": wdmPassiveIfGroup,
       "wdmGeneralGroupV2": wdmGeneralGroupV2,
       "wdmIfGroupV2": wdmIfGroupV2,
       "wdmPassiveIfGroupV2": wdmPassiveIfGroupV2,
       "wdmIfGroupV3": wdmIfGroupV3,
       "wdmPassiveIfGroupV3": wdmPassiveIfGroupV3,
       "wdmIfGroupV4": wdmIfGroupV4,
       "wdmPassiveIfGroupV4": wdmPassiveIfGroupV4,
       "wdmIfGroupV5": wdmIfGroupV5,
       "wdmProtGroupV2": wdmProtGroupV2,
       "wdmIfGroupV6": wdmIfGroupV6,
       "wdmNotificationGroupV2": wdmNotificationGroupV2,
       "wdmIfGroupV7": wdmIfGroupV7,
       "wdmGeneralGroupV3": wdmGeneralGroupV3,
       "wdmIfGroupV8": wdmIfGroupV8,
       "wdmIfGroupV9": wdmIfGroupV9,
       "wdmIfGroupV10": wdmIfGroupV10,
       "wdmIfGroupV11": wdmIfGroupV11,
       "wdmIfGroupV12": wdmIfGroupV12,
       "wdmPassiveIfGroupV5": wdmPassiveIfGroupV5,
       "wdmIfGroupV13": wdmIfGroupV13,
       "wdmGeneralGroupV4": wdmGeneralGroupV4,
       "wdmProtGroupV3": wdmProtGroupV3,
       "wdmIfGroupV14": wdmIfGroupV14,
       "wdmPassiveIfGroupV6": wdmPassiveIfGroupV6,
       "wdmProtGroupV4": wdmProtGroupV4,
       "wdmProtGroupV5": wdmProtGroupV5,
       "wdmIfGroupV15": wdmIfGroupV15,
       "wdmIfGroupV16": wdmIfGroupV16,
       "wdmIfGroupV17": wdmIfGroupV17,
       "wdmIfGroupV18": wdmIfGroupV18,
       "wdmIfGroupV19": wdmIfGroupV19,
       "wdmVc4Group": wdmVc4Group,
       "wdmGeneralGroupV5": wdmGeneralGroupV5,
       "wdmIfGroupV20": wdmIfGroupV20,
       "wdmIfGroupV21": wdmIfGroupV21,
       "wdmIfGroupV22": wdmIfGroupV22,
       "wdmRemoteProtGroup": wdmRemoteProtGroup,
       "wdmProtGroupV6": wdmProtGroupV6,
       "wdmCtrlChannelGroup": wdmCtrlChannelGroup,
       "wdmCtrlGroupGroup": wdmCtrlGroupGroup,
       "wdmCtrlGroupGroupV2": wdmCtrlGroupGroupV2,
       "wdmSubChannelGroup": wdmSubChannelGroup,
       "wdmGeneralGroupV6": wdmGeneralGroupV6,
       "wdmIfGroupV23": wdmIfGroupV23,
       "wdmVc4GroupV2": wdmVc4GroupV2,
       "wdmCtrlChannelGroupV2": wdmCtrlChannelGroupV2,
       "wdmCtrlGlobalGroup": wdmCtrlGlobalGroup,
       "wdmSubChannelGroupV2": wdmSubChannelGroupV2,
       "wdmProtGroupV7": wdmProtGroupV7,
       "wdmIfGroupV24": wdmIfGroupV24,
       "wdmIfGroupV25": wdmIfGroupV25,
       "wdmCtrlChannelGroupV3": wdmCtrlChannelGroupV3,
       "wdmIfGroupV26": wdmIfGroupV26,
       "wdmProtGroupV8": wdmProtGroupV8,
       "wdmProtGroupV9": wdmProtGroupV9,
       "wdmCtrlGroupGroupV3": wdmCtrlGroupGroupV3,
       "wdmIfGroupV27": wdmIfGroupV27,
       "wdmIfGroupV28": wdmIfGroupV28,
       "wdmIfGroupV29": wdmIfGroupV29,
       "wdmDelayCompPGGroup": wdmDelayCompPGGroup,
       "wdmDelayCompLinkGroup": wdmDelayCompLinkGroup,
       "wdmCtrlChannelGroupV4": wdmCtrlChannelGroupV4,
       "wdmIfGroupV30": wdmIfGroupV30,
       "wdmPassiveIfGroupV7": wdmPassiveIfGroupV7,
       "wdmMeanChannelPowerControlGroupV1": wdmMeanChannelPowerControlGroupV1,
       "wdmMeanChannelPowerControlGlobalGroupV1": wdmMeanChannelPowerControlGlobalGroupV1,
       "wdmGeneralGroupV7": wdmGeneralGroupV7,
       "wdmCtrlGroupGroupV4": wdmCtrlGroupGroupV4,
       "wdmCtrlGroupGroupV5": wdmCtrlGroupGroupV5,
       "wdmCtrlChannelGroupV5": wdmCtrlChannelGroupV5,
       "lumWdmCompl": lumWdmCompl,
       "lumWdmBasicComplV1": lumWdmBasicComplV1,
       "lumWdmBasicComplV2": lumWdmBasicComplV2,
       "lumWdmBasicComplV3": lumWdmBasicComplV3,
       "lumWdmBasicComplV4": lumWdmBasicComplV4,
       "lumWdmBasicComplV5": lumWdmBasicComplV5,
       "lumWdmBasicComplV6": lumWdmBasicComplV6,
       "lumWdmBasicComplV7": lumWdmBasicComplV7,
       "lumWdmBasicComplV8": lumWdmBasicComplV8,
       "lumWdmBasicComplV9": lumWdmBasicComplV9,
       "lumWdmBasicComplV10": lumWdmBasicComplV10,
       "lumWdmBasicComplV11": lumWdmBasicComplV11,
       "lumWdmBasicComplV12": lumWdmBasicComplV12,
       "lumWdmBasicComplV13": lumWdmBasicComplV13,
       "lumWdmBasicComplV14": lumWdmBasicComplV14,
       "lumWdmBasicComplV15": lumWdmBasicComplV15,
       "lumWdmBasicComplV16": lumWdmBasicComplV16,
       "lumWdmBasicComplV17": lumWdmBasicComplV17,
       "lumWdmBasicComplV18": lumWdmBasicComplV18,
       "lumWdmBasicComplV19": lumWdmBasicComplV19,
       "lumWdmBasicComplV20": lumWdmBasicComplV20,
       "lumWdmBasicComplV21": lumWdmBasicComplV21,
       "lumWdmBasicComplV22": lumWdmBasicComplV22,
       "lumWdmBasicComplV23": lumWdmBasicComplV23,
       "lumWdmBasicComplV24": lumWdmBasicComplV24,
       "lumWdmBasicComplV25": lumWdmBasicComplV25,
       "lumWdmBasicComplV26": lumWdmBasicComplV26,
       "lumWdmBasicComplV27": lumWdmBasicComplV27,
       "lumWdmBasicComplV28": lumWdmBasicComplV28,
       "lumWdmBasicComplV29": lumWdmBasicComplV29,
       "lumWdmBasicComplV30": lumWdmBasicComplV30,
       "lumWdmBasicComplV31": lumWdmBasicComplV31,
       "lumWdmBasicComplV32": lumWdmBasicComplV32,
       "lumWdmBasicComplV33": lumWdmBasicComplV33,
       "lumWdmBasicComplV34": lumWdmBasicComplV34,
       "lumWdmBasicComplV35": lumWdmBasicComplV35,
       "lumWdmBasicComplV36": lumWdmBasicComplV36,
       "lumWdmBasicComplV37": lumWdmBasicComplV37,
       "lumWdmBasicComplV38": lumWdmBasicComplV38,
       "lumWdmBasicComplV39": lumWdmBasicComplV39,
       "lumWdmBasicComplV40": lumWdmBasicComplV40,
       "lumWdmBasicComplV41": lumWdmBasicComplV41,
       "lumWdmBasicComplV42": lumWdmBasicComplV42,
       "lumWdmBasicComplV43": lumWdmBasicComplV43,
       "lumWdmBasicComplV44": lumWdmBasicComplV44,
       "lumWdmBasicComplV45": lumWdmBasicComplV45,
       "lumWdmBasicComplV46": lumWdmBasicComplV46,
       "lumWdmMinimalGroups": lumWdmMinimalGroups,
       "wdmGeneralMinimalGroupV1": wdmGeneralMinimalGroupV1,
       "wdmIfMinimalGroupV1": wdmIfMinimalGroupV1,
       "wdmPassiveIfMinimalGroupV1": wdmPassiveIfMinimalGroupV1,
       "wdmIfMinimalGroupV2": wdmIfMinimalGroupV2,
       "wdmPassiveIfMinimalGroupV2": wdmPassiveIfMinimalGroupV2,
       "lumWdmMinimalCompl": lumWdmMinimalCompl,
       "lumWdmMinimalComplV1": lumWdmMinimalComplV1,
       "lumWdmMinimalComplV2": lumWdmMinimalComplV2,
       "lumWdmMinimalComplV3": lumWdmMinimalComplV3,
       "lumWdmMinimalComplV4": lumWdmMinimalComplV4,
       "lumWdmMIBObjects": lumWdmMIBObjects,
       "wdmGeneral": wdmGeneral,
       "wdmGeneralTestAndIncr": wdmGeneralTestAndIncr,
       "wdmGeneralMibSpecVersion": wdmGeneralMibSpecVersion,
       "wdmGeneralMibImplVersion": wdmGeneralMibImplVersion,
       "wdmGeneralLastChangeTime": wdmGeneralLastChangeTime,
       "wdmGeneralStateLastChangeTime": wdmGeneralStateLastChangeTime,
       "wdmGeneralWdmIfTableSize": wdmGeneralWdmIfTableSize,
       "wdmGeneralWdmPassiveIfTableSize": wdmGeneralWdmPassiveIfTableSize,
       "wdmGeneralWdmProtTableSize": wdmGeneralWdmProtTableSize,
       "wdmGeneralWdmVc4TableSize": wdmGeneralWdmVc4TableSize,
       "wdmGeneralWdmRemoteProtTableSize": wdmGeneralWdmRemoteProtTableSize,
       "wdmGeneralWdmCtrlChannelTableSize": wdmGeneralWdmCtrlChannelTableSize,
       "wdmGeneralWdmCtrlGroupTableSize": wdmGeneralWdmCtrlGroupTableSize,
       "wdmGeneralWdmSubChannelTableSize": wdmGeneralWdmSubChannelTableSize,
       "wdmGeneralWdmDelayCompPGTableSize": wdmGeneralWdmDelayCompPGTableSize,
       "wdmGeneralWdmDelayCompLinkTableSize": wdmGeneralWdmDelayCompLinkTableSize,
       "wdmGeneralWdmMeanChannelPowerControlTableSize": wdmGeneralWdmMeanChannelPowerControlTableSize,
       "wdmGeneralWdmMeanChannelPowerControlGlobalTableSize": wdmGeneralWdmMeanChannelPowerControlGlobalTableSize,
       "wdmIfList": wdmIfList,
       "wdmIfTable": wdmIfTable,
       "wdmIfEntry": wdmIfEntry,
       "wdmIfIndex": wdmIfIndex,
       "wdmIfName": wdmIfName,
       "wdmIfDescr": wdmIfDescr,
       "wdmIfSubrack": wdmIfSubrack,
       "wdmIfSlot": wdmIfSlot,
       "wdmIfTxPort": wdmIfTxPort,
       "wdmIfInvPhysIndexOrZero": wdmIfInvPhysIndexOrZero,
       "wdmIfTxLambda": wdmIfTxLambda,
       "wdmIfHighSpeedMin": wdmIfHighSpeedMin,
       "wdmIfHighSpeedMax": wdmIfHighSpeedMax,
       "wdmIfPowerLevel": wdmIfPowerLevel,
       "wdmIfPowerLevelHighThreshold": wdmIfPowerLevelHighThreshold,
       "wdmIfPowerLevelLowThreshold": wdmIfPowerLevelLowThreshold,
       "wdmIfLaserTemp": wdmIfLaserTemp,
       "wdmIfLaserTempOffset": wdmIfLaserTempOffset,
       "wdmIfLaserTempOffsetThreshold": wdmIfLaserTempOffsetThreshold,
       "wdmIfLaserMode": wdmIfLaserMode,
       "wdmIfLaserStatus": wdmIfLaserStatus,
       "wdmIfAdminStatus": wdmIfAdminStatus,
       "wdmIfOperStatus": wdmIfOperStatus,
       "wdmIfLossOfSignal": wdmIfLossOfSignal,
       "wdmIfReceivedPowerHigh": wdmIfReceivedPowerHigh,
       "wdmIfReceivedPowerLow": wdmIfReceivedPowerLow,
       "wdmIfLaserBiasHigh": wdmIfLaserBiasHigh,
       "wdmIfErroredSeconds": wdmIfErroredSeconds,
       "wdmIfSeverelyErroredSeconds": wdmIfSeverelyErroredSeconds,
       "wdmIfBackgroundBlockErrors": wdmIfBackgroundBlockErrors,
       "wdmIfUnavailableSeconds": wdmIfUnavailableSeconds,
       "wdmIfForwardDefectIndication": wdmIfForwardDefectIndication,
       "wdmIfBackwardDefectIndication": wdmIfBackwardDefectIndication,
       "wdmIfLossOfFrame": wdmIfLossOfFrame,
       "wdmIfAlarmIndicationSignal": wdmIfAlarmIndicationSignal,
       "wdmIfRemoteDefectIndication": wdmIfRemoteDefectIndication,
       "wdmIfLossOfSync": wdmIfLossOfSync,
       "wdmIfLossOfForwardingErrorCorrection": wdmIfLossOfForwardingErrorCorrection,
       "wdmIfLaserTempHigh": wdmIfLaserTempHigh,
       "wdmIfLaserTempLow": wdmIfLaserTempLow,
       "wdmIfRxPort": wdmIfRxPort,
       "wdmIfBitrateMismatch": wdmIfBitrateMismatch,
       "wdmIfLaserBias": wdmIfLaserBias,
       "wdmIfLaserBiasThreshold": wdmIfLaserBiasThreshold,
       "wdmIfLossOfSignalThreshold": wdmIfLossOfSignalThreshold,
       "wdmIfJ0PathTrace": wdmIfJ0PathTrace,
       "wdmIfInbandMode": wdmIfInbandMode,
       "wdmIfInbandStatus": wdmIfInbandStatus,
       "wdmIfExpectedTxLambda": wdmIfExpectedTxLambda,
       "wdmIfForwardingErrorCorrectionMode": wdmIfForwardingErrorCorrectionMode,
       "wdmIfUnexpectedTxLambda": wdmIfUnexpectedTxLambda,
       "wdmIfTraceIntrusionMode": wdmIfTraceIntrusionMode,
       "wdmIfTraceTransmitted": wdmIfTraceTransmitted,
       "wdmIfTraceReceived": wdmIfTraceReceived,
       "wdmIfTraceExpected": wdmIfTraceExpected,
       "wdmIfTraceAlarmMode": wdmIfTraceAlarmMode,
       "wdmIfTraceMismatch": wdmIfTraceMismatch,
       "wdmIfLaserStatusLastChangeTime": wdmIfLaserStatusLastChangeTime,
       "wdmIfSuppressRemoteAlarms": wdmIfSuppressRemoteAlarms,
       "wdmIfSerialNumberMismatch": wdmIfSerialNumberMismatch,
       "wdmIfOptimizeDecisionThreshold": wdmIfOptimizeDecisionThreshold,
       "wdmIfThresholdOptimizationState": wdmIfThresholdOptimizationState,
       "wdmIfUseHwDefaultDecisionThreshold": wdmIfUseHwDefaultDecisionThreshold,
       "wdmIfFecCorrectedZeros": wdmIfFecCorrectedZeros,
       "wdmIfFecCorrectedOnes": wdmIfFecCorrectedOnes,
       "wdmIfOptimizedForSerialNumber": wdmIfOptimizedForSerialNumber,
       "wdmIfRelativeDecisionThreshold": wdmIfRelativeDecisionThreshold,
       "wdmIfTrxCodeMismatch": wdmIfTrxCodeMismatch,
       "wdmIfTrxBitrateUnavailable": wdmIfTrxBitrateUnavailable,
       "wdmIfTrxMissing": wdmIfTrxMissing,
       "wdmIfTrxClass": wdmIfTrxClass,
       "wdmIfLaserTempHighRelativeThreshold": wdmIfLaserTempHighRelativeThreshold,
       "wdmIfLaserTempLowRelativeThreshold": wdmIfLaserTempLowRelativeThreshold,
       "wdmIfTransmitterFailed": wdmIfTransmitterFailed,
       "wdmIfReceiverSensitivity": wdmIfReceiverSensitivity,
       "wdmIfPowerLevelLowRelativeThreshold": wdmIfPowerLevelLowRelativeThreshold,
       "wdmIfIllegalFrequency": wdmIfIllegalFrequency,
       "wdmIfLaserForcedOn": wdmIfLaserForcedOn,
       "wdmIfTrafficCombination": wdmIfTrafficCombination,
       "wdmIfSelectTrafficCombination": wdmIfSelectTrafficCombination,
       "wdmIfObjectProperty": wdmIfObjectProperty,
       "wdmIfTxPowerLevel": wdmIfTxPowerLevel,
       "wdmIfLaserTempActual": wdmIfLaserTempActual,
       "wdmIfTrxFailed": wdmIfTrxFailed,
       "wdmIfDisabled": wdmIfDisabled,
       "wdmIfLoopback": wdmIfLoopback,
       "wdmIfContinousOptimization": wdmIfContinousOptimization,
       "wdmIfThresholdOptimizationResultCause": wdmIfThresholdOptimizationResultCause,
       "wdmIfDistributionRole": wdmIfDistributionRole,
       "wdmIfConfigurationCommand": wdmIfConfigurationCommand,
       "wdmIfNoFrequencySet": wdmIfNoFrequencySet,
       "wdmIfFormat": wdmIfFormat,
       "wdmIfConfigurationFormatCommand": wdmIfConfigurationFormatCommand,
       "wdmIfOHTransparency": wdmIfOHTransparency,
       "wdmIfLinkDown": wdmIfLinkDown,
       "wdmIfAutoNegotiationMode": wdmIfAutoNegotiationMode,
       "wdmIfAutoNegotiationStatus": wdmIfAutoNegotiationStatus,
       "wdmIfFlowControlMode": wdmIfFlowControlMode,
       "wdmIfGroupLineMode": wdmIfGroupLineMode,
       "wdmIfFecType": wdmIfFecType,
       "wdmIfFarEndLoopback": wdmIfFarEndLoopback,
       "wdmIfFarEndLoopbackTimeout": wdmIfFarEndLoopbackTimeout,
       "wdmIfFarEndLoopbackEnabled": wdmIfFarEndLoopbackEnabled,
       "wdmIfChangeLoopbackCommand": wdmIfChangeLoopbackCommand,
       "wdmIfFecFailure": wdmIfFecFailure,
       "wdmIfTxSignalStatus": wdmIfTxSignalStatus,
       "wdmIfRxSignalStatus": wdmIfRxSignalStatus,
       "wdmIfNearEndLoopback": wdmIfNearEndLoopback,
       "wdmIfNearEndLoopbackTimeout": wdmIfNearEndLoopbackTimeout,
       "wdmIfNearEndLoopbackEnabled": wdmIfNearEndLoopbackEnabled,
       "wdmIfChangeNearEndLoopbackCommand": wdmIfChangeNearEndLoopbackCommand,
       "wdmIfSignalDegraded": wdmIfSignalDegraded,
       "wdmIfHubProtectionMode": wdmIfHubProtectionMode,
       "wdmIfActualFormat": wdmIfActualFormat,
       "wdmIfTdcDispersion": wdmIfTdcDispersion,
       "wdmIfTdcDispersionCommand": wdmIfTdcDispersionCommand,
       "wdmIfTdcDispersionMode": wdmIfTdcDispersionMode,
       "wdmIfLineControlLoopCurrentState": wdmIfLineControlLoopCurrentState,
       "wdmIfSignalDegradeThreshold": wdmIfSignalDegradeThreshold,
       "wdmIfTrxThresholdOptimizationState": wdmIfTrxThresholdOptimizationState,
       "wdmIfTrxDecisionThreshold": wdmIfTrxDecisionThreshold,
       "wdmIfSwControlledLaserShutdown": wdmIfSwControlledLaserShutdown,
       "wdmIfChangeSwControlledLaserShutdownCommand": wdmIfChangeSwControlledLaserShutdownCommand,
       "wdmIfControlledLaserShutdownEnabled": wdmIfControlledLaserShutdownEnabled,
       "wdmIfAid": wdmIfAid,
       "wdmIfPhysicalLocation": wdmIfPhysicalLocation,
       "wdmProtList": wdmProtList,
       "wdmProtTable": wdmProtTable,
       "wdmProtEntry": wdmProtEntry,
       "wdmProtIndex": wdmProtIndex,
       "wdmProtName": wdmProtName,
       "wdmProtDescr": wdmProtDescr,
       "wdmProtRightSubrack": wdmProtRightSubrack,
       "wdmProtRightSlot": wdmProtRightSlot,
       "wdmProtRightPort": wdmProtRightPort,
       "wdmProtLeftSubrack": wdmProtLeftSubrack,
       "wdmProtLeftSlot": wdmProtLeftSlot,
       "wdmProtLeftPort": wdmProtLeftPort,
       "wdmProtLastChangeTime": wdmProtLastChangeTime,
       "wdmProtAdminStatus": wdmProtAdminStatus,
       "wdmProtOperStatus": wdmProtOperStatus,
       "wdmProtRowStatus": wdmProtRowStatus,
       "wdmProtServiceDegraded": wdmProtServiceDegraded,
       "wdmProtServiceFailure": wdmProtServiceFailure,
       "wdmProtActiveSide": wdmProtActiveSide,
       "wdmProtLeftStatus": wdmProtLeftStatus,
       "wdmProtRightStatus": wdmProtRightStatus,
       "wdmProtProtectionType": wdmProtProtectionType,
       "wdmProtObjectProperty": wdmProtObjectProperty,
       "wdmProtWrapperMode": wdmProtWrapperMode,
       "wdmProtWrapperState": wdmProtWrapperState,
       "wdmProtLeftCommSubrack": wdmProtLeftCommSubrack,
       "wdmProtLeftCommSlot": wdmProtLeftCommSlot,
       "wdmProtLeftCommPort": wdmProtLeftCommPort,
       "wdmProtRightCommSubrack": wdmProtRightCommSubrack,
       "wdmProtRightCommSlot": wdmProtRightCommSlot,
       "wdmProtRightCommPort": wdmProtRightCommPort,
       "wdmProtLeftCommInterface": wdmProtLeftCommInterface,
       "wdmProtRightCommInterface": wdmProtRightCommInterface,
       "wdmProtCommunicationFailure": wdmProtCommunicationFailure,
       "wdmProtHubTrafficConfigMismatch": wdmProtHubTrafficConfigMismatch,
       "wdmProtSignalDegradeProtection": wdmProtSignalDegradeProtection,
       "wdmProtRevertiveSwitchWtrTimer": wdmProtRevertiveSwitchWtrTimer,
       "wdmProtRevertiveSwitch": wdmProtRevertiveSwitch,
       "wdmProtRevertiveSwitchPrimaryPath": wdmProtRevertiveSwitchPrimaryPath,
       "wdmProtRevertiveSwitchSecondaryPath": wdmProtRevertiveSwitchSecondaryPath,
       "wdmProtSecondaryPathUsed": wdmProtSecondaryPathUsed,
       "lumentisWdmNotifications": lumentisWdmNotifications,
       "wdmNotifyPrefix": wdmNotifyPrefix,
       "wdmProtOperStatusBothDown": wdmProtOperStatusBothDown,
       "wdmProtOperStatusLeftDownRightUp": wdmProtOperStatusLeftDownRightUp,
       "wdmProtOperStatusLeftDownRightStandby": wdmProtOperStatusLeftDownRightStandby,
       "wdmProtOperStatusLeftStandbyRightDown": wdmProtOperStatusLeftStandbyRightDown,
       "wdmProtOperStatusLeftStandbyRightUp": wdmProtOperStatusLeftStandbyRightUp,
       "wdmProtOperStatusLeftUpRightDown": wdmProtOperStatusLeftUpRightDown,
       "wdmProtOperStatusLeftUpRightStandby": wdmProtOperStatusLeftUpRightStandby,
       "wdmIfLaserStatusOn": wdmIfLaserStatusOn,
       "wdmIfLaserStatusOff": wdmIfLaserStatusOff,
       "wdmProtStatusChanged": wdmProtStatusChanged,
       "wdmPassiveIfList": wdmPassiveIfList,
       "wdmPassiveIfTable": wdmPassiveIfTable,
       "wdmPassiveIfEntry": wdmPassiveIfEntry,
       "wdmPassiveIfIndex": wdmPassiveIfIndex,
       "wdmPassiveIfName": wdmPassiveIfName,
       "wdmPassiveIfDescr": wdmPassiveIfDescr,
       "wdmPassiveIfSubrack": wdmPassiveIfSubrack,
       "wdmPassiveIfSlot": wdmPassiveIfSlot,
       "wdmPassiveIfPort": wdmPassiveIfPort,
       "wdmPassiveIfInvPhysIndexOrZero": wdmPassiveIfInvPhysIndexOrZero,
       "wdmPassiveIfDirection": wdmPassiveIfDirection,
       "wdmPassiveIfLambdaType": wdmPassiveIfLambdaType,
       "wdmPassiveIfLambda": wdmPassiveIfLambda,
       "wdmPassiveIfLambdaMax": wdmPassiveIfLambdaMax,
       "wdmPassiveIfLastChangeTime": wdmPassiveIfLastChangeTime,
       "wdmPassiveIfExpectedLambda": wdmPassiveIfExpectedLambda,
       "wdmPassiveIfUnexpectedLambda": wdmPassiveIfUnexpectedLambda,
       "wdmPassiveIfAdminStatus": wdmPassiveIfAdminStatus,
       "wdmPassiveIfOperStatus": wdmPassiveIfOperStatus,
       "wdmPassiveIfObjectProperty": wdmPassiveIfObjectProperty,
       "wdmPassiveIfExpectedLambdaMax": wdmPassiveIfExpectedLambdaMax,
       "wdmPassiveIfAid": wdmPassiveIfAid,
       "wdmPassiveIfPhysicalLocation": wdmPassiveIfPhysicalLocation,
       "wdmPassiveIfIfNo": wdmPassiveIfIfNo,
       "wdmVc4List": wdmVc4List,
       "wdmVc4Table": wdmVc4Table,
       "wdmVc4Entry": wdmVc4Entry,
       "wdmVc4Index": wdmVc4Index,
       "wdmVc4Name": wdmVc4Name,
       "wdmVc4Descr": wdmVc4Descr,
       "wdmVc4Subrack": wdmVc4Subrack,
       "wdmVc4Slot": wdmVc4Slot,
       "wdmVc4TxPort": wdmVc4TxPort,
       "wdmVc4RxPort": wdmVc4RxPort,
       "wdmVc4Vc4": wdmVc4Vc4,
       "wdmVc4ObjectProperty": wdmVc4ObjectProperty,
       "wdmVc4AuAlarmIndicationSignal": wdmVc4AuAlarmIndicationSignal,
       "wdmVc4AuLossOfPointer": wdmVc4AuLossOfPointer,
       "wdmVc4RxSignalStatus": wdmVc4RxSignalStatus,
       "wdmVc4ConcatenationStatus": wdmVc4ConcatenationStatus,
       "wdmVc4PayloadStatus": wdmVc4PayloadStatus,
       "wdmVc4ConnectionStatus": wdmVc4ConnectionStatus,
       "wdmVc4ConnectedForeignIndex": wdmVc4ConnectedForeignIndex,
       "wdmVc4AdminStatus": wdmVc4AdminStatus,
       "wdmRemoteProtList": wdmRemoteProtList,
       "wdmRemoteProtTable": wdmRemoteProtTable,
       "wdmRemoteProtEntry": wdmRemoteProtEntry,
       "wdmRemoteProtIndex": wdmRemoteProtIndex,
       "wdmRemoteProtName": wdmRemoteProtName,
       "wdmRemoteProtDescr": wdmRemoteProtDescr,
       "wdmRemoteProtLocalSubrack": wdmRemoteProtLocalSubrack,
       "wdmRemoteProtLocalSlot": wdmRemoteProtLocalSlot,
       "wdmRemoteProtLocalPort": wdmRemoteProtLocalPort,
       "wdmRemoteProtCommSubrack": wdmRemoteProtCommSubrack,
       "wdmRemoteProtCommSlot": wdmRemoteProtCommSlot,
       "wdmRemoteProtCommPort": wdmRemoteProtCommPort,
       "wdmRemoteProtCommInterface": wdmRemoteProtCommInterface,
       "wdmRemoteProtLastChangeTime": wdmRemoteProtLastChangeTime,
       "wdmRemoteProtIpAddress": wdmRemoteProtIpAddress,
       "wdmRemoteProtIdentifier": wdmRemoteProtIdentifier,
       "wdmRemoteProtRole": wdmRemoteProtRole,
       "wdmRemoteProtAdminStatus": wdmRemoteProtAdminStatus,
       "wdmRemoteProtRowStatus": wdmRemoteProtRowStatus,
       "wdmRemoteProtActiveSide": wdmRemoteProtActiveSide,
       "wdmRemoteProtLocalStatus": wdmRemoteProtLocalStatus,
       "wdmRemoteProtRemoteStatus": wdmRemoteProtRemoteStatus,
       "wdmRemoteProtObjectProperty": wdmRemoteProtObjectProperty,
       "wdmRemoteProtServiceDegraded": wdmRemoteProtServiceDegraded,
       "wdmRemoteProtServiceFailure": wdmRemoteProtServiceFailure,
       "wdmRemoteProtSetup": wdmRemoteProtSetup,
       "wdmRemoteProtSetupFailure": wdmRemoteProtSetupFailure,
       "wdmRemoteProtRoleConflict": wdmRemoteProtRoleConflict,
       "wdmRemoteProtCommunicationFailure": wdmRemoteProtCommunicationFailure,
       "wdmCtrlChannelList": wdmCtrlChannelList,
       "wdmCtrlChannelTable": wdmCtrlChannelTable,
       "wdmCtrlChannelEntry": wdmCtrlChannelEntry,
       "wdmCtrlChannelIndex": wdmCtrlChannelIndex,
       "wdmCtrlChannelName": wdmCtrlChannelName,
       "wdmCtrlChannelSubrack": wdmCtrlChannelSubrack,
       "wdmCtrlChannelSlot": wdmCtrlChannelSlot,
       "wdmCtrlChannelTxPort": wdmCtrlChannelTxPort,
       "wdmCtrlChannelChannel": wdmCtrlChannelChannel,
       "wdmCtrlChannelGroupNumber": wdmCtrlChannelGroupNumber,
       "wdmCtrlChannelAdminStatus": wdmCtrlChannelAdminStatus,
       "wdmCtrlChannelWantedOutputPower": wdmCtrlChannelWantedOutputPower,
       "wdmCtrlChannelCurrentOutputPower": wdmCtrlChannelCurrentOutputPower,
       "wdmCtrlChannelCurrentAttenuation": wdmCtrlChannelCurrentAttenuation,
       "wdmCtrlChannelForceRegulationCommand": wdmCtrlChannelForceRegulationCommand,
       "wdmCtrlChannelOuputPowerControlFailure": wdmCtrlChannelOuputPowerControlFailure,
       "wdmCtrlChannelCurrentPowerOutOfRange": wdmCtrlChannelCurrentPowerOutOfRange,
       "wdmCtrlChannelAttenuationOutOfRange": wdmCtrlChannelAttenuationOutOfRange,
       "wdmCtrlChannelStatus": wdmCtrlChannelStatus,
       "wdmCtrlChannelStartupChannel": wdmCtrlChannelStartupChannel,
       "wdmCtrlChannelMonitorIndex": wdmCtrlChannelMonitorIndex,
       "wdmCtrlChannelStartupCommand": wdmCtrlChannelStartupCommand,
       "wdmCtrlChannelSfpMissing": wdmCtrlChannelSfpMissing,
       "wdmCtrlChannelSfpMediaMismatch": wdmCtrlChannelSfpMediaMismatch,
       "wdmCtrlChannelLossOfSignal": wdmCtrlChannelLossOfSignal,
       "wdmCtrlChannelDescr": wdmCtrlChannelDescr,
       "wdmCtrlChannelMaxAttenuation": wdmCtrlChannelMaxAttenuation,
       "wdmCtrlChannelMinAttenuation": wdmCtrlChannelMinAttenuation,
       "wdmCtrlChannelAttenControlOffset": wdmCtrlChannelAttenControlOffset,
       "wdmCtrlChannelAttenControlDegraded": wdmCtrlChannelAttenControlDegraded,
       "wdmCtrlChannelNotFound": wdmCtrlChannelNotFound,
       "wdmCtrlGroupList": wdmCtrlGroupList,
       "wdmCtrlGroupTable": wdmCtrlGroupTable,
       "wdmCtrlGroupEntry": wdmCtrlGroupEntry,
       "wdmCtrlGroupIndex": wdmCtrlGroupIndex,
       "wdmCtrlGroupName": wdmCtrlGroupName,
       "wdmCtrlGroupDescr": wdmCtrlGroupDescr,
       "wdmCtrlGroupGroupNumber": wdmCtrlGroupGroupNumber,
       "wdmCtrlGroupSubrack": wdmCtrlGroupSubrack,
       "wdmCtrlGroupSlot": wdmCtrlGroupSlot,
       "wdmCtrlGroupPort": wdmCtrlGroupPort,
       "wdmCtrlGroupMonitorName": wdmCtrlGroupMonitorName,
       "wdmCtrlGroupAdminStatus": wdmCtrlGroupAdminStatus,
       "wdmCtrlGroupControlMode": wdmCtrlGroupControlMode,
       "wdmCtrlGroupConfigurationCommand": wdmCtrlGroupConfigurationCommand,
       "wdmCtrlGroupForceRegulationCommand": wdmCtrlGroupForceRegulationCommand,
       "wdmCtrlGroupLockedRange": wdmCtrlGroupLockedRange,
       "wdmCtrlGroupRegulationRange": wdmCtrlGroupRegulationRange,
       "wdmCtrlGroupRegulationLastChangeTime": wdmCtrlGroupRegulationLastChangeTime,
       "wdmCtrlGroupCommissioningMode": wdmCtrlGroupCommissioningMode,
       "wdmCtrlGroupAssociateChannel": wdmCtrlGroupAssociateChannel,
       "wdmCtrlGroupNoOfChannels": wdmCtrlGroupNoOfChannels,
       "wdmCtrlGroupStatus": wdmCtrlGroupStatus,
       "wdmCtrlGroupTimeLeft": wdmCtrlGroupTimeLeft,
       "wdmCtrlGroupOutputPowerMismatch": wdmCtrlGroupOutputPowerMismatch,
       "wdmCtrlGroupTotalPower": wdmCtrlGroupTotalPower,
       "wdmCtrlGroupChannelStartupCommand": wdmCtrlGroupChannelStartupCommand,
       "wdmSubChannelList": wdmSubChannelList,
       "wdmSubChannelTable": wdmSubChannelTable,
       "wdmSubChannelEntry": wdmSubChannelEntry,
       "wdmSubChannelIndex": wdmSubChannelIndex,
       "wdmSubChannelName": wdmSubChannelName,
       "wdmSubChannelId": wdmSubChannelId,
       "wdmSubChannelType": wdmSubChannelType,
       "wdmSubChannelUnequipped": wdmSubChannelUnequipped,
       "wdmSubChannelConnectionStatus": wdmSubChannelConnectionStatus,
       "wdmSubChannelConnectedForeignIndex": wdmSubChannelConnectedForeignIndex,
       "wdmSubChannelCrossConnect": wdmSubChannelCrossConnect,
       "wdmSubChannelDisconnect": wdmSubChannelDisconnect,
       "wdmSubChannelRemoteAccessInterface": wdmSubChannelRemoteAccessInterface,
       "wdmSubChannelProtectedChannelIndex": wdmSubChannelProtectedChannelIndex,
       "wdmCtrlGlobal": wdmCtrlGlobal,
       "wdmCtrlGlobalRegulationInterval": wdmCtrlGlobalRegulationInterval,
       "wdmCtrlGlobalRegulationStatus": wdmCtrlGlobalRegulationStatus,
       "wdmCtrlGlobalLastRegulation": wdmCtrlGlobalLastRegulation,
       "wdmCtrlGlobalTimeLeft": wdmCtrlGlobalTimeLeft,
       "wdmDelayCompPGList": wdmDelayCompPGList,
       "wdmDelayCompPGTable": wdmDelayCompPGTable,
       "wdmDelayCompPGEntry": wdmDelayCompPGEntry,
       "wdmDelayCompPGIndex": wdmDelayCompPGIndex,
       "wdmDelayCompPGName": wdmDelayCompPGName,
       "wdmDelayCompPGUpId": wdmDelayCompPGUpId,
       "wdmDelayCompPGAdminStatus": wdmDelayCompPGAdminStatus,
       "wdmDelayCompPGOperStatus": wdmDelayCompPGOperStatus,
       "wdmDelayCompPGAutoCompensationMode": wdmDelayCompPGAutoCompensationMode,
       "wdmDelayCompPGAutoCompensationState": wdmDelayCompPGAutoCompensationState,
       "wdmDelayCompPGDelayDifference": wdmDelayCompPGDelayDifference,
       "wdmDelayCompPGDelayCompensationOOR": wdmDelayCompPGDelayCompensationOOR,
       "wdmDelayCompPGFiberLengthDifferenceOOR": wdmDelayCompPGFiberLengthDifferenceOOR,
       "wdmDelayCompPGDelayCompensationReset": wdmDelayCompPGDelayCompensationReset,
       "wdmDelayCompLinkList": wdmDelayCompLinkList,
       "wdmDelayCompLinkTable": wdmDelayCompLinkTable,
       "wdmDelayCompLinkEntry": wdmDelayCompLinkEntry,
       "wdmDelayCompLinkIndex": wdmDelayCompLinkIndex,
       "wdmDelayCompLinkName": wdmDelayCompLinkName,
       "wdmDelayCompLinkUpId": wdmDelayCompLinkUpId,
       "wdmDelayCompLinkCurrentDelayCompensation": wdmDelayCompLinkCurrentDelayCompensation,
       "wdmDelayCompLinkWantedDelayCompensation": wdmDelayCompLinkWantedDelayCompensation,
       "wdmMeanChannelPowerControlGlobalList": wdmMeanChannelPowerControlGlobalList,
       "wdmMeanChannelPowerControlGlobalTable": wdmMeanChannelPowerControlGlobalTable,
       "wdmMeanChannelPowerControlGlobalEntry": wdmMeanChannelPowerControlGlobalEntry,
       "wdmMeanChannelPowerControlGlobalIndex": wdmMeanChannelPowerControlGlobalIndex,
       "wdmMeanChannelPowerControlGlobalName": wdmMeanChannelPowerControlGlobalName,
       "wdmMeanChannelPowerControlGlobalEntryCreate": wdmMeanChannelPowerControlGlobalEntryCreate,
       "wdmMeanChannelPowerControlList": wdmMeanChannelPowerControlList,
       "wdmMeanChannelPowerControlTable": wdmMeanChannelPowerControlTable,
       "wdmMeanChannelPowerControlEntry": wdmMeanChannelPowerControlEntry,
       "wdmMeanChannelPowerControlIndex": wdmMeanChannelPowerControlIndex,
       "wdmMeanChannelPowerControlName": wdmMeanChannelPowerControlName,
       "wdmMeanChannelPowerControlDescr": wdmMeanChannelPowerControlDescr,
       "wdmMeanChannelPowerControlOcmSubrack": wdmMeanChannelPowerControlOcmSubrack,
       "wdmMeanChannelPowerControlOcmSlot": wdmMeanChannelPowerControlOcmSlot,
       "wdmMeanChannelPowerControlOcmPort": wdmMeanChannelPowerControlOcmPort,
       "wdmMeanChannelPowerControlOaSubrack": wdmMeanChannelPowerControlOaSubrack,
       "wdmMeanChannelPowerControlOaSlot": wdmMeanChannelPowerControlOaSlot,
       "wdmMeanChannelPowerControlOaPort": wdmMeanChannelPowerControlOaPort,
       "wdmMeanChannelPowerControlMonitorName": wdmMeanChannelPowerControlMonitorName,
       "wdmMeanChannelPowerControlAdminStatus": wdmMeanChannelPowerControlAdminStatus,
       "wdmMeanChannelPowerControlOperStatus": wdmMeanChannelPowerControlOperStatus,
       "wdmMeanChannelPowerControlStartRegulation": wdmMeanChannelPowerControlStartRegulation,
       "wdmMeanChannelPowerControlRegulationRange": wdmMeanChannelPowerControlRegulationRange,
       "wdmMeanChannelPowerControlLatestRegulation": wdmMeanChannelPowerControlLatestRegulation,
       "wdmMeanChannelPowerControlLatestChange": wdmMeanChannelPowerControlLatestChange,
       "wdmMeanChannelPowerControlMonitorOffsetCalibrationFailed": wdmMeanChannelPowerControlMonitorOffsetCalibrationFailed,
       "wdmMeanChannelPowerControlRegulationState": wdmMeanChannelPowerControlRegulationState,
       "wdmMeanChannelPowerControlTimeToNextRegulation": wdmMeanChannelPowerControlTimeToNextRegulation,
       "wdmMeanChannelPowerControlWantedChannelPower": wdmMeanChannelPowerControlWantedChannelPower,
       "wdmMeanChannelPowerControlCurrentChannelPower": wdmMeanChannelPowerControlCurrentChannelPower,
       "wdmMeanChannelPowerControlCurrentGain": wdmMeanChannelPowerControlCurrentGain,
       "wdmMeanChannelPowerControlTotalChannelOutputPower": wdmMeanChannelPowerControlTotalChannelOutputPower,
       "wdmMeanChannelPowerControlNumberOfChannels": wdmMeanChannelPowerControlNumberOfChannels,
       "wdmMeanChannelPowerControlAbsolutePowerOffset": wdmMeanChannelPowerControlAbsolutePowerOffset,
       "wdmMeanChannelPowerControlRemainingPowerOffset": wdmMeanChannelPowerControlRemainingPowerOffset,
       "wdmMeanChannelPowerControlMonitorOffsetTooLarge": wdmMeanChannelPowerControlMonitorOffsetTooLarge,
       "wdmMeanChannelPowerControlChannelPowerOutOfRange": wdmMeanChannelPowerControlChannelPowerOutOfRange,
       "wdmMeanChannelPowerControlRegulationInterval": wdmMeanChannelPowerControlRegulationInterval,
       "wdmMeanChannelPowerControlAmplifierOutputPort": wdmMeanChannelPowerControlAmplifierOutputPort,
       "wdmMeanChannelPowerControlLatestAmplifierRxPower": wdmMeanChannelPowerControlLatestAmplifierRxPower,
       "wdmMeanChannelPowerControlLatestAmplifierTxPower": wdmMeanChannelPowerControlLatestAmplifierTxPower,
       "wdmMeanChannelPowerControlLocalId": wdmMeanChannelPowerControlLocalId}
)
