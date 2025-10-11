# SNMP MIB module (ALCATEL-ENT1-LBD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-LBD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:41 2025
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

(softentIND1Lbd,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1Lbd")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alcatelIND1LBDMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIB.setRevisions(
        ("2008-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaLbdPortConfigLbdOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("inactive", 0),
          ("normal", 1),
          ("shutdown", 2),
          ("remoteShutdown", 3))
    )



class AlaLbdCurrentStateCVAorAR(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("normal", 1))
    )



# MIB Managed Objects in the order of their OIDs

_AlaLbdTraps_ObjectIdentity = ObjectIdentity
alaLbdTraps = _AlaLbdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 0)
)
if mibBuilder.loadTexts:
    alaLbdTraps.setStatus("current")
_AlcatelIND1LBDMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBObjects = _AlcatelIND1LBDMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBObjects.setStatus("current")


class _AlaLbdGlobalConfigStatus_Type(Integer32):
    """Custom type alaLbdGlobalConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaLbdGlobalConfigStatus_Type.__name__ = "Integer32"
_AlaLbdGlobalConfigStatus_Object = MibScalar
alaLbdGlobalConfigStatus = _AlaLbdGlobalConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 1),
    _AlaLbdGlobalConfigStatus_Type()
)
alaLbdGlobalConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigStatus.setStatus("current")


class _AlaLbdGlobalConfigTransmissionTimer_Type(Unsigned32):
    """Custom type alaLbdGlobalConfigTransmissionTimer based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_AlaLbdGlobalConfigTransmissionTimer_Type.__name__ = "Unsigned32"
_AlaLbdGlobalConfigTransmissionTimer_Object = MibScalar
alaLbdGlobalConfigTransmissionTimer = _AlaLbdGlobalConfigTransmissionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 2),
    _AlaLbdGlobalConfigTransmissionTimer_Type()
)
alaLbdGlobalConfigTransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigTransmissionTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigTransmissionTimer.setUnits("seconds")


class _AlaLbdGlobalClearPortStat_Type(Integer32):
    """Custom type alaLbdGlobalClearPortStat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaLbdGlobalClearPortStat_Type.__name__ = "Integer32"
_AlaLbdGlobalClearPortStat_Object = MibScalar
alaLbdGlobalClearPortStat = _AlaLbdGlobalClearPortStat_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 3),
    _AlaLbdGlobalClearPortStat_Type()
)
alaLbdGlobalClearPortStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalClearPortStat.setStatus("current")


class _AlaLbdGlobalConfigAutorecoveryTimer_Type(Unsigned32):
    """Custom type alaLbdGlobalConfigAutorecoveryTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AlaLbdGlobalConfigAutorecoveryTimer_Type.__name__ = "Unsigned32"
_AlaLbdGlobalConfigAutorecoveryTimer_Object = MibScalar
alaLbdGlobalConfigAutorecoveryTimer = _AlaLbdGlobalConfigAutorecoveryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 4),
    _AlaLbdGlobalConfigAutorecoveryTimer_Type()
)
alaLbdGlobalConfigAutorecoveryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigAutorecoveryTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaLbdGlobalConfigAutorecoveryTimer.setUnits("seconds")
_AlaLbdPortConfig_ObjectIdentity = ObjectIdentity
alaLbdPortConfig = _AlaLbdPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5)
)
_AlaLbdPortConfigTable_Object = MibTable
alaLbdPortConfigTable = _AlaLbdPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alaLbdPortConfigTable.setStatus("current")
_AlaLbdPortConfigEntry_Object = MibTableRow
alaLbdPortConfigEntry = _AlaLbdPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1)
)
alaLbdPortConfigEntry.setIndexNames(
    (0, "ALCATEL-ENT1-LBD-MIB", "alaLbdPortConfigIfIndex"),
)
if mibBuilder.loadTexts:
    alaLbdPortConfigEntry.setStatus("current")
_AlaLbdPortConfigIfIndex_Type = InterfaceIndex
_AlaLbdPortConfigIfIndex_Object = MibTableColumn
alaLbdPortConfigIfIndex = _AlaLbdPortConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 1),
    _AlaLbdPortConfigIfIndex_Type()
)
alaLbdPortConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLbdPortConfigIfIndex.setStatus("current")


class _AlaLbdPortConfigLbdAdminStatus_Type(Integer32):
    """Custom type alaLbdPortConfigLbdAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaLbdPortConfigLbdAdminStatus_Type.__name__ = "Integer32"
_AlaLbdPortConfigLbdAdminStatus_Object = MibTableColumn
alaLbdPortConfigLbdAdminStatus = _AlaLbdPortConfigLbdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 2),
    _AlaLbdPortConfigLbdAdminStatus_Type()
)
alaLbdPortConfigLbdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdPortConfigLbdAdminStatus.setStatus("current")
_AlaLbdPortConfigLbdOperStatus_Type = AlaLbdPortConfigLbdOperStatus
_AlaLbdPortConfigLbdOperStatus_Object = MibTableColumn
alaLbdPortConfigLbdOperStatus = _AlaLbdPortConfigLbdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 3),
    _AlaLbdPortConfigLbdOperStatus_Type()
)
alaLbdPortConfigLbdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortConfigLbdOperStatus.setStatus("current")


class _AlaLbdPortConfigServiceAccessType_Type(Integer32):
    """Custom type alaLbdPortConfigServiceAccessType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normalEdge", 1),
          ("serviceEdge", 2),
          ("noValue", 3))
    )


_AlaLbdPortConfigServiceAccessType_Type.__name__ = "Integer32"
_AlaLbdPortConfigServiceAccessType_Object = MibTableColumn
alaLbdPortConfigServiceAccessType = _AlaLbdPortConfigServiceAccessType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 4),
    _AlaLbdPortConfigServiceAccessType_Type()
)
alaLbdPortConfigServiceAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdPortConfigServiceAccessType.setStatus("current")


class _AlaLbdPortAFDConfig_Type(Integer32):
    """Custom type alaLbdPortAFDConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("autoFarbic", 2))
    )


_AlaLbdPortAFDConfig_Type.__name__ = "Integer32"
_AlaLbdPortAFDConfig_Object = MibTableColumn
alaLbdPortAFDConfig = _AlaLbdPortAFDConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 5),
    _AlaLbdPortAFDConfig_Type()
)
alaLbdPortAFDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortAFDConfig.setStatus("current")


class _AlaLbdPortRemoteConfigAdminStatus_Type(Integer32):
    """Custom type alaLbdPortRemoteConfigAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaLbdPortRemoteConfigAdminStatus_Type.__name__ = "Integer32"
_AlaLbdPortRemoteConfigAdminStatus_Object = MibTableColumn
alaLbdPortRemoteConfigAdminStatus = _AlaLbdPortRemoteConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 6),
    _AlaLbdPortRemoteConfigAdminStatus_Type()
)
alaLbdPortRemoteConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdPortRemoteConfigAdminStatus.setStatus("current")
_AlaLbdPortRemoteSrcMacAddr_Type = MacAddress
_AlaLbdPortRemoteSrcMacAddr_Object = MibTableColumn
alaLbdPortRemoteSrcMacAddr = _AlaLbdPortRemoteSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 7),
    _AlaLbdPortRemoteSrcMacAddr_Type()
)
alaLbdPortRemoteSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortRemoteSrcMacAddr.setStatus("current")
_AlaLbdPortRemoteBridgeID_Type = MacAddress
_AlaLbdPortRemoteBridgeID_Object = MibTableColumn
alaLbdPortRemoteBridgeID = _AlaLbdPortRemoteBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 5, 1, 1, 8),
    _AlaLbdPortRemoteBridgeID_Type()
)
alaLbdPortRemoteBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortRemoteBridgeID.setStatus("current")
_AlaLbdPortStat_ObjectIdentity = ObjectIdentity
alaLbdPortStat = _AlaLbdPortStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6)
)
_AlaLbdPortStatsTable_Object = MibTable
alaLbdPortStatsTable = _AlaLbdPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    alaLbdPortStatsTable.setStatus("current")
_AlaLbdPortStatsEntry_Object = MibTableRow
alaLbdPortStatsEntry = _AlaLbdPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1, 1)
)
alaLbdPortStatsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-LBD-MIB", "alaLbdPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alaLbdPortStatsEntry.setStatus("current")
_AlaLbdPortStatsIfIndex_Type = InterfaceIndex
_AlaLbdPortStatsIfIndex_Object = MibTableColumn
alaLbdPortStatsIfIndex = _AlaLbdPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1, 1, 1),
    _AlaLbdPortStatsIfIndex_Type()
)
alaLbdPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLbdPortStatsIfIndex.setStatus("current")
_AlaLbdPortNumLbdInvalidRcvd_Type = Counter32
_AlaLbdPortNumLbdInvalidRcvd_Object = MibTableColumn
alaLbdPortNumLbdInvalidRcvd = _AlaLbdPortNumLbdInvalidRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1, 1, 2),
    _AlaLbdPortNumLbdInvalidRcvd_Type()
)
alaLbdPortNumLbdInvalidRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortNumLbdInvalidRcvd.setStatus("current")
_AlaLbdPortLbdSent_Type = Counter32
_AlaLbdPortLbdSent_Object = MibTableColumn
alaLbdPortLbdSent = _AlaLbdPortLbdSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1, 1, 3),
    _AlaLbdPortLbdSent_Type()
)
alaLbdPortLbdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortLbdSent.setStatus("current")


class _AlaLbdPortStatsClear_Type(Integer32):
    """Custom type alaLbdPortStatsClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_AlaLbdPortStatsClear_Type.__name__ = "Integer32"
_AlaLbdPortStatsClear_Object = MibTableColumn
alaLbdPortStatsClear = _AlaLbdPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1, 1, 4),
    _AlaLbdPortStatsClear_Type()
)
alaLbdPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdPortStatsClear.setStatus("current")


class _AlaLbdPortLinkAgg_Type(Integer32):
    """Custom type alaLbdPortLinkAgg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AlaLbdPortLinkAgg_Type.__name__ = "Integer32"
_AlaLbdPortLinkAgg_Object = MibTableColumn
alaLbdPortLinkAgg = _AlaLbdPortLinkAgg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 6, 1, 1, 5),
    _AlaLbdPortLinkAgg_Type()
)
alaLbdPortLinkAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdPortLinkAgg.setStatus("current")
_AlaLbdTrapsObj_ObjectIdentity = ObjectIdentity
alaLbdTrapsObj = _AlaLbdTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7)
)
_AlaLbdPortIfIndex_Type = InterfaceIndex
_AlaLbdPortIfIndex_Object = MibScalar
alaLbdPortIfIndex = _AlaLbdPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 1),
    _AlaLbdPortIfIndex_Type()
)
alaLbdPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPortIfIndex.setStatus("current")


class _AlaLbdPreviousState_Type(Integer32):
    """Custom type alaLbdPreviousState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("normal", 1)
    )


_AlaLbdPreviousState_Type.__name__ = "Integer32"
_AlaLbdPreviousState_Object = MibScalar
alaLbdPreviousState = _AlaLbdPreviousState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 2),
    _AlaLbdPreviousState_Type()
)
alaLbdPreviousState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPreviousState.setStatus("current")


class _AlaLbdCurrentState_Type(Integer32):
    """Custom type alaLbdCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 1),
          ("remoteShutdown", 2))
    )


_AlaLbdCurrentState_Type.__name__ = "Integer32"
_AlaLbdCurrentState_Object = MibScalar
alaLbdCurrentState = _AlaLbdCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 3),
    _AlaLbdCurrentState_Type()
)
alaLbdCurrentState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdCurrentState.setStatus("current")


class _AlaLbdPreviousStateClearViolationAll_Type(Integer32):
    """Custom type alaLbdPreviousStateClearViolationAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("shutdown", 1)
    )


_AlaLbdPreviousStateClearViolationAll_Type.__name__ = "Integer32"
_AlaLbdPreviousStateClearViolationAll_Object = MibScalar
alaLbdPreviousStateClearViolationAll = _AlaLbdPreviousStateClearViolationAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 4),
    _AlaLbdPreviousStateClearViolationAll_Type()
)
alaLbdPreviousStateClearViolationAll.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPreviousStateClearViolationAll.setStatus("current")
_AlaLbdCurrentStateClearViolationAll_Type = AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateClearViolationAll_Object = MibScalar
alaLbdCurrentStateClearViolationAll = _AlaLbdCurrentStateClearViolationAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 5),
    _AlaLbdCurrentStateClearViolationAll_Type()
)
alaLbdCurrentStateClearViolationAll.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdCurrentStateClearViolationAll.setStatus("current")


class _AlaLbdPreviousStateAutoRecovery_Type(Integer32):
    """Custom type alaLbdPreviousStateAutoRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("shutdown", 1)
    )


_AlaLbdPreviousStateAutoRecovery_Type.__name__ = "Integer32"
_AlaLbdPreviousStateAutoRecovery_Object = MibScalar
alaLbdPreviousStateAutoRecovery = _AlaLbdPreviousStateAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 6),
    _AlaLbdPreviousStateAutoRecovery_Type()
)
alaLbdPreviousStateAutoRecovery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdPreviousStateAutoRecovery.setStatus("current")
_AlaLbdCurrentStateAutoRecovery_Type = AlaLbdCurrentStateCVAorAR
_AlaLbdCurrentStateAutoRecovery_Object = MibScalar
alaLbdCurrentStateAutoRecovery = _AlaLbdCurrentStateAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 7, 7),
    _AlaLbdCurrentStateAutoRecovery_Type()
)
alaLbdCurrentStateAutoRecovery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaLbdCurrentStateAutoRecovery.setStatus("current")


class _AlaLbdGlobalStatusAFDConfig_Type(Integer32):
    """Custom type alaLbdGlobalStatusAFDConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 1),
          ("autoFabric", 2))
    )


_AlaLbdGlobalStatusAFDConfig_Type.__name__ = "Integer32"
_AlaLbdGlobalStatusAFDConfig_Object = MibScalar
alaLbdGlobalStatusAFDConfig = _AlaLbdGlobalStatusAFDConfig_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 8),
    _AlaLbdGlobalStatusAFDConfig_Type()
)
alaLbdGlobalStatusAFDConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdGlobalStatusAFDConfig.setStatus("current")


class _AlaLbdVlanGlobalConfigTransmissionTimer_Type(Unsigned32):
    """Custom type alaLbdVlanGlobalConfigTransmissionTimer based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AlaLbdVlanGlobalConfigTransmissionTimer_Type.__name__ = "Unsigned32"
_AlaLbdVlanGlobalConfigTransmissionTimer_Object = MibScalar
alaLbdVlanGlobalConfigTransmissionTimer = _AlaLbdVlanGlobalConfigTransmissionTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 9),
    _AlaLbdVlanGlobalConfigTransmissionTimer_Type()
)
alaLbdVlanGlobalConfigTransmissionTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdVlanGlobalConfigTransmissionTimer.setStatus("current")
if mibBuilder.loadTexts:
    alaLbdVlanGlobalConfigTransmissionTimer.setUnits("seconds")


class _AlaLbdVlanConfigLbdAdminStatus_Type(Integer32):
    """Custom type alaLbdVlanConfigLbdAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaLbdVlanConfigLbdAdminStatus_Type.__name__ = "Integer32"
_AlaLbdVlanConfigLbdAdminStatus_Object = MibScalar
alaLbdVlanConfigLbdAdminStatus = _AlaLbdVlanConfigLbdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 10),
    _AlaLbdVlanConfigLbdAdminStatus_Type()
)
alaLbdVlanConfigLbdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdVlanConfigLbdAdminStatus.setStatus("current")


class _AlaLbdVlanConfigAllVlan_Type(Integer32):
    """Custom type alaLbdVlanConfigAllVlan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaLbdVlanConfigAllVlan_Type.__name__ = "Integer32"
_AlaLbdVlanConfigAllVlan_Object = MibScalar
alaLbdVlanConfigAllVlan = _AlaLbdVlanConfigAllVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 11),
    _AlaLbdVlanConfigAllVlan_Type()
)
alaLbdVlanConfigAllVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdVlanConfigAllVlan.setStatus("current")
_AlaLbdVlanConfig_ObjectIdentity = ObjectIdentity
alaLbdVlanConfig = _AlaLbdVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 12)
)
_AlaLbdVlanTable_Object = MibTable
alaLbdVlanTable = _AlaLbdVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaLbdVlanTable.setStatus("current")
_AlaLbdVlanEntry_Object = MibTableRow
alaLbdVlanEntry = _AlaLbdVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 12, 1, 1)
)
alaLbdVlanEntry.setIndexNames(
    (0, "ALCATEL-ENT1-LBD-MIB", "alaLbdVlanId"),
)
if mibBuilder.loadTexts:
    alaLbdVlanEntry.setStatus("current")


class _AlaLbdVlanId_Type(Unsigned32):
    """Custom type alaLbdVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaLbdVlanId_Type.__name__ = "Unsigned32"
_AlaLbdVlanId_Object = MibTableColumn
alaLbdVlanId = _AlaLbdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 12, 1, 1, 1),
    _AlaLbdVlanId_Type()
)
alaLbdVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLbdVlanId.setStatus("current")
_AlaLbdVlanStatus_Type = RowStatus
_AlaLbdVlanStatus_Object = MibTableColumn
alaLbdVlanStatus = _AlaLbdVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 12, 1, 1, 2),
    _AlaLbdVlanStatus_Type()
)
alaLbdVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaLbdVlanStatus.setStatus("current")
_AlaLbdVlanViolationStatistics_ObjectIdentity = ObjectIdentity
alaLbdVlanViolationStatistics = _AlaLbdVlanViolationStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 13)
)
_AlaLbdVlanViolationStatisticsTable_Object = MibTable
alaLbdVlanViolationStatisticsTable = _AlaLbdVlanViolationStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 13, 1)
)
if mibBuilder.loadTexts:
    alaLbdVlanViolationStatisticsTable.setStatus("current")
_AlaLbdVlanViolationStatisticsEntry_Object = MibTableRow
alaLbdVlanViolationStatisticsEntry = _AlaLbdVlanViolationStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 13, 1, 1)
)
alaLbdVlanViolationStatisticsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-LBD-MIB", "alaLbdVlanIfindex"),
)
if mibBuilder.loadTexts:
    alaLbdVlanViolationStatisticsEntry.setStatus("current")


class _AlaLbdVlanIfindex_Type(Unsigned32):
    """Custom type alaLbdVlanIfindex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_AlaLbdVlanIfindex_Type.__name__ = "Unsigned32"
_AlaLbdVlanIfindex_Object = MibTableColumn
alaLbdVlanIfindex = _AlaLbdVlanIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 13, 1, 1, 1),
    _AlaLbdVlanIfindex_Type()
)
alaLbdVlanIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaLbdVlanIfindex.setStatus("current")


class _AlaLbdViolatedVlanId_Type(Integer32):
    """Custom type alaLbdViolatedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaLbdViolatedVlanId_Type.__name__ = "Integer32"
_AlaLbdViolatedVlanId_Object = MibTableColumn
alaLbdViolatedVlanId = _AlaLbdViolatedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 13, 1, 1, 2),
    _AlaLbdViolatedVlanId_Type()
)
alaLbdViolatedVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaLbdViolatedVlanId.setStatus("current")


class _AlaLbdGlobalRemoteConfigStatus_Type(Integer32):
    """Custom type alaLbdGlobalRemoteConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaLbdGlobalRemoteConfigStatus_Type.__name__ = "Integer32"
_AlaLbdGlobalRemoteConfigStatus_Object = MibScalar
alaLbdGlobalRemoteConfigStatus = _AlaLbdGlobalRemoteConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 1, 14),
    _AlaLbdGlobalRemoteConfigStatus_Type()
)
alaLbdGlobalRemoteConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaLbdGlobalRemoteConfigStatus.setStatus("current")
_AlcatelIND1LBDMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBConformance = _AlcatelIND1LBDMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBConformance.setStatus("current")
_AlcatelIND1LBDMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBGroups = _AlcatelIND1LBDMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBGroups.setStatus("current")
_AlcatelIND1LBDMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1LBDMIBCompliances = _AlcatelIND1LBDMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBCompliances.setStatus("current")

# Managed Objects groups

alaLbdGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 1)
)
alaLbdGlobalConfigGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalConfigStatus"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalConfigTransmissionTimer"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalClearPortStat"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalConfigAutorecoveryTimer"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalStatusAFDConfig"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdVlanGlobalConfigTransmissionTimer"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdVlanConfigLbdAdminStatus"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdVlanConfigAllVlan"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalRemoteConfigStatus"))
)
if mibBuilder.loadTexts:
    alaLbdGlobalConfigGroup.setStatus("current")

alaLbdIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 2)
)
alaLbdIntfConfigGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPortConfigLbdAdminStatus"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortConfigLbdOperStatus"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortConfigServiceAccessType"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortAFDConfig"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortRemoteConfigAdminStatus"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortRemoteSrcMacAddr"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortRemoteBridgeID"))
)
if mibBuilder.loadTexts:
    alaLbdIntfConfigGroup.setStatus("current")

alaLbdPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 3)
)
alaLbdPortStatusGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPortNumLbdInvalidRcvd"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortLbdSent"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortStatsClear"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortLinkAgg"))
)
if mibBuilder.loadTexts:
    alaLbdPortStatusGroup.setStatus("current")

alaLbdStateTrapToShutdownGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 4)
)
alaLbdStateTrapToShutdownGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPreviousState"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdCurrentState"))
)
if mibBuilder.loadTexts:
    alaLbdStateTrapToShutdownGroup.setStatus("current")

alaLbdStateTrapForClearViolationAllGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 5)
)
alaLbdStateTrapForClearViolationAllGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPreviousStateClearViolationAll"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdCurrentStateClearViolationAll"))
)
if mibBuilder.loadTexts:
    alaLbdStateTrapForClearViolationAllGroup.setStatus("current")

alaLbdStateTrapForAutoRecoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 6)
)
alaLbdStateTrapForAutoRecoveryGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPreviousStateAutoRecovery"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdCurrentStateAutoRecovery"))
)
if mibBuilder.loadTexts:
    alaLbdStateTrapForAutoRecoveryGroup.setStatus("current")

alaLbdVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 8)
)
alaLbdVlanConfigGroup.setObjects(
    ("ALCATEL-ENT1-LBD-MIB", "alaLbdVlanStatus")
)
if mibBuilder.loadTexts:
    alaLbdVlanConfigGroup.setStatus("current")

alaLbdVlanViolationStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 9)
)
alaLbdVlanViolationStatisticsGroup.setObjects(
    ("ALCATEL-ENT1-LBD-MIB", "alaLbdViolatedVlanId")
)
if mibBuilder.loadTexts:
    alaLbdVlanViolationStatisticsGroup.setStatus("current")


# Notification objects

alaLbdStateChangeToShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 0, 1)
)
alaLbdStateChangeToShutdown.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPreviousState"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdCurrentState"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortRemoteSrcMacAddr"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortRemoteBridgeID"))
)
if mibBuilder.loadTexts:
    alaLbdStateChangeToShutdown.setStatus(
        "current"
    )

alaLbdStateChangeForClearViolationAll = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 0, 2)
)
alaLbdStateChangeForClearViolationAll.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPreviousStateClearViolationAll"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdCurrentStateClearViolationAll"))
)
if mibBuilder.loadTexts:
    alaLbdStateChangeForClearViolationAll.setStatus(
        "current"
    )

alaLbdStateChangeForAutoRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 0, 3)
)
alaLbdStateChangeForAutoRecovery.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdPortIfIndex"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPreviousStateAutoRecovery"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdCurrentStateAutoRecovery"))
)
if mibBuilder.loadTexts:
    alaLbdStateChangeForAutoRecovery.setStatus(
        "current"
    )


# Notifications groups

alaLbdTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 1, 7)
)
alaLbdTrapsGroup.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdStateChangeForAutoRecovery"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdStateChangeForClearViolationAll"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdStateChangeToShutdown"))
)
if mibBuilder.loadTexts:
    alaLbdTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1LBDMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 82, 1, 2, 2, 1)
)
alcatelIND1LBDMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-LBD-MIB", "alaLbdGlobalConfigGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdIntfConfigGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdPortStatusGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdStateTrapToShutdownGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdStateTrapForClearViolationAllGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdStateTrapForAutoRecoveryGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdTrapsGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdVlanConfigGroup"),
        ("ALCATEL-ENT1-LBD-MIB", "alaLbdVlanViolationStatisticsGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1LBDMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-LBD-MIB",
    **{"AlaLbdPortConfigLbdOperStatus": AlaLbdPortConfigLbdOperStatus,
       "AlaLbdCurrentStateCVAorAR": AlaLbdCurrentStateCVAorAR,
       "alcatelIND1LBDMIB": alcatelIND1LBDMIB,
       "alaLbdTraps": alaLbdTraps,
       "alaLbdStateChangeToShutdown": alaLbdStateChangeToShutdown,
       "alaLbdStateChangeForClearViolationAll": alaLbdStateChangeForClearViolationAll,
       "alaLbdStateChangeForAutoRecovery": alaLbdStateChangeForAutoRecovery,
       "alcatelIND1LBDMIBObjects": alcatelIND1LBDMIBObjects,
       "alaLbdGlobalConfigStatus": alaLbdGlobalConfigStatus,
       "alaLbdGlobalConfigTransmissionTimer": alaLbdGlobalConfigTransmissionTimer,
       "alaLbdGlobalClearPortStat": alaLbdGlobalClearPortStat,
       "alaLbdGlobalConfigAutorecoveryTimer": alaLbdGlobalConfigAutorecoveryTimer,
       "alaLbdPortConfig": alaLbdPortConfig,
       "alaLbdPortConfigTable": alaLbdPortConfigTable,
       "alaLbdPortConfigEntry": alaLbdPortConfigEntry,
       "alaLbdPortConfigIfIndex": alaLbdPortConfigIfIndex,
       "alaLbdPortConfigLbdAdminStatus": alaLbdPortConfigLbdAdminStatus,
       "alaLbdPortConfigLbdOperStatus": alaLbdPortConfigLbdOperStatus,
       "alaLbdPortConfigServiceAccessType": alaLbdPortConfigServiceAccessType,
       "alaLbdPortAFDConfig": alaLbdPortAFDConfig,
       "alaLbdPortRemoteConfigAdminStatus": alaLbdPortRemoteConfigAdminStatus,
       "alaLbdPortRemoteSrcMacAddr": alaLbdPortRemoteSrcMacAddr,
       "alaLbdPortRemoteBridgeID": alaLbdPortRemoteBridgeID,
       "alaLbdPortStat": alaLbdPortStat,
       "alaLbdPortStatsTable": alaLbdPortStatsTable,
       "alaLbdPortStatsEntry": alaLbdPortStatsEntry,
       "alaLbdPortStatsIfIndex": alaLbdPortStatsIfIndex,
       "alaLbdPortNumLbdInvalidRcvd": alaLbdPortNumLbdInvalidRcvd,
       "alaLbdPortLbdSent": alaLbdPortLbdSent,
       "alaLbdPortStatsClear": alaLbdPortStatsClear,
       "alaLbdPortLinkAgg": alaLbdPortLinkAgg,
       "alaLbdTrapsObj": alaLbdTrapsObj,
       "alaLbdPortIfIndex": alaLbdPortIfIndex,
       "alaLbdPreviousState": alaLbdPreviousState,
       "alaLbdCurrentState": alaLbdCurrentState,
       "alaLbdPreviousStateClearViolationAll": alaLbdPreviousStateClearViolationAll,
       "alaLbdCurrentStateClearViolationAll": alaLbdCurrentStateClearViolationAll,
       "alaLbdPreviousStateAutoRecovery": alaLbdPreviousStateAutoRecovery,
       "alaLbdCurrentStateAutoRecovery": alaLbdCurrentStateAutoRecovery,
       "alaLbdGlobalStatusAFDConfig": alaLbdGlobalStatusAFDConfig,
       "alaLbdVlanGlobalConfigTransmissionTimer": alaLbdVlanGlobalConfigTransmissionTimer,
       "alaLbdVlanConfigLbdAdminStatus": alaLbdVlanConfigLbdAdminStatus,
       "alaLbdVlanConfigAllVlan": alaLbdVlanConfigAllVlan,
       "alaLbdVlanConfig": alaLbdVlanConfig,
       "alaLbdVlanTable": alaLbdVlanTable,
       "alaLbdVlanEntry": alaLbdVlanEntry,
       "alaLbdVlanId": alaLbdVlanId,
       "alaLbdVlanStatus": alaLbdVlanStatus,
       "alaLbdVlanViolationStatistics": alaLbdVlanViolationStatistics,
       "alaLbdVlanViolationStatisticsTable": alaLbdVlanViolationStatisticsTable,
       "alaLbdVlanViolationStatisticsEntry": alaLbdVlanViolationStatisticsEntry,
       "alaLbdVlanIfindex": alaLbdVlanIfindex,
       "alaLbdViolatedVlanId": alaLbdViolatedVlanId,
       "alaLbdGlobalRemoteConfigStatus": alaLbdGlobalRemoteConfigStatus,
       "alcatelIND1LBDMIBConformance": alcatelIND1LBDMIBConformance,
       "alcatelIND1LBDMIBGroups": alcatelIND1LBDMIBGroups,
       "alaLbdGlobalConfigGroup": alaLbdGlobalConfigGroup,
       "alaLbdIntfConfigGroup": alaLbdIntfConfigGroup,
       "alaLbdPortStatusGroup": alaLbdPortStatusGroup,
       "alaLbdStateTrapToShutdownGroup": alaLbdStateTrapToShutdownGroup,
       "alaLbdStateTrapForClearViolationAllGroup": alaLbdStateTrapForClearViolationAllGroup,
       "alaLbdStateTrapForAutoRecoveryGroup": alaLbdStateTrapForAutoRecoveryGroup,
       "alaLbdTrapsGroup": alaLbdTrapsGroup,
       "alaLbdVlanConfigGroup": alaLbdVlanConfigGroup,
       "alaLbdVlanViolationStatisticsGroup": alaLbdVlanViolationStatisticsGroup,
       "alcatelIND1LBDMIBCompliances": alcatelIND1LBDMIBCompliances,
       "alcatelIND1LBDMIBCompliance": alcatelIND1LBDMIBCompliance}
)
