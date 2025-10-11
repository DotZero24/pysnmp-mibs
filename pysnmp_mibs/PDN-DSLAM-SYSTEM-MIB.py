# SNMP MIB module (PDN-DSLAM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-DSLAM-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:59:46 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(IdslClockMode,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "IdslClockMode",
    "SwitchState")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

pdn_dslam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24)
)
if mibBuilder.loadTexts:
    pdn_dslam.setRevisions(
        ("1902-06-20 00:00",
         "1902-06-05 00:00",
         "1902-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysDevDslamMIBObjects_ObjectIdentity = ObjectIdentity
sysDevDslamMIBObjects = _SysDevDslamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1)
)
_SysDevStats_ObjectIdentity = ObjectIdentity
sysDevStats = _SysDevStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1)
)
_LoginHistTable_Object = MibTable
loginHistTable = _LoginHistTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    loginHistTable.setStatus("current")
_LoginHistTableEntry_Object = MibTableRow
loginHistTableEntry = _LoginHistTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1)
)
loginHistTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "loginUserId"),
    (0, "PDN-DSLAM-SYSTEM-MIB", "loginTime"),
)
if mibBuilder.loadTexts:
    loginHistTableEntry.setStatus("current")
_LoginUserId_Type = DisplayString
_LoginUserId_Object = MibTableColumn
loginUserId = _LoginUserId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 1),
    _LoginUserId_Type()
)
loginUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserId.setStatus("current")
_LoginTime_Type = TimeTicks
_LoginTime_Object = MibTableColumn
loginTime = _LoginTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 2),
    _LoginTime_Type()
)
loginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginTime.setStatus("current")


class _LoginAccessApp_Type(Integer32):
    """Custom type loginAccessApp based on Integer32"""
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
        *(("console", 1),
          ("telnet", 2),
          ("ftp", 3),
          ("web", 4),
          ("modem", 5))
    )


_LoginAccessApp_Type.__name__ = "Integer32"
_LoginAccessApp_Object = MibTableColumn
loginAccessApp = _LoginAccessApp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 3),
    _LoginAccessApp_Type()
)
loginAccessApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginAccessApp.setStatus("current")
_LoginAccessHost_Type = IpAddress
_LoginAccessHost_Object = MibTableColumn
loginAccessHost = _LoginAccessHost_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 4),
    _LoginAccessHost_Type()
)
loginAccessHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginAccessHost.setStatus("current")


class _LoginUserPriv_Type(Integer32):
    """Custom type loginUserPriv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 1),
          ("operator", 2))
    )


_LoginUserPriv_Type.__name__ = "Integer32"
_LoginUserPriv_Object = MibTableColumn
loginUserPriv = _LoginUserPriv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 5),
    _LoginUserPriv_Type()
)
loginUserPriv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginUserPriv.setStatus("current")


class _LoginStatus_Type(Integer32):
    """Custom type loginStatus based on Integer32"""
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


_LoginStatus_Type.__name__ = "Integer32"
_LoginStatus_Object = MibTableColumn
loginStatus = _LoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 1, 1, 6),
    _LoginStatus_Type()
)
loginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginStatus.setStatus("current")
_LoginFailureCountTable_Object = MibTable
loginFailureCountTable = _LoginFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2)
)
if mibBuilder.loadTexts:
    loginFailureCountTable.setStatus("current")
_LoginFailureCountTableEntry_Object = MibTableRow
loginFailureCountTableEntry = _LoginFailureCountTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1)
)
loginFailureCountTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "loginFailureAccessApp"),
)
if mibBuilder.loadTexts:
    loginFailureCountTableEntry.setStatus("current")


class _LoginFailureAccessApp_Type(Integer32):
    """Custom type loginFailureAccessApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("telnet", 2),
          ("ftp", 3))
    )


_LoginFailureAccessApp_Type.__name__ = "Integer32"
_LoginFailureAccessApp_Object = MibTableColumn
loginFailureAccessApp = _LoginFailureAccessApp_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1, 1),
    _LoginFailureAccessApp_Type()
)
loginFailureAccessApp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginFailureAccessApp.setStatus("current")
_LoginFailureCount_Type = Counter32
_LoginFailureCount_Object = MibTableColumn
loginFailureCount = _LoginFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 1, 2, 1, 2),
    _LoginFailureCount_Type()
)
loginFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loginFailureCount.setStatus("current")
_SysDevConfig_ObjectIdentity = ObjectIdentity
sysDevConfig = _SysDevConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2)
)


class _EnablePowerSourceFailureAlarm_Type(Integer32):
    """Custom type enablePowerSourceFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_EnablePowerSourceFailureAlarm_Type.__name__ = "Integer32"
_EnablePowerSourceFailureAlarm_Object = MibScalar
enablePowerSourceFailureAlarm = _EnablePowerSourceFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 1),
    _EnablePowerSourceFailureAlarm_Type()
)
enablePowerSourceFailureAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePowerSourceFailureAlarm.setStatus("current")
_DevIfTable_Object = MibTable
devIfTable = _DevIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    devIfTable.setStatus("current")
_DevIfTableEntry_Object = MibTableRow
devIfTableEntry = _DevIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1)
)
devIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    devIfTableEntry.setStatus("current")


class _DevPacketDiscardPolicy_Type(Integer32):
    """Custom type devPacketDiscardPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("mrrp", 2),
          ("lrrp", 3))
    )


_DevPacketDiscardPolicy_Type.__name__ = "Integer32"
_DevPacketDiscardPolicy_Object = MibTableColumn
devPacketDiscardPolicy = _DevPacketDiscardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1, 1),
    _DevPacketDiscardPolicy_Type()
)
devPacketDiscardPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devPacketDiscardPolicy.setStatus("current")


class _DevLinkIntegrity_Type(Integer32):
    """Custom type devLinkIntegrity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("none", 3))
    )


_DevLinkIntegrity_Type.__name__ = "Integer32"
_DevLinkIntegrity_Object = MibTableColumn
devLinkIntegrity = _DevLinkIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 2, 1, 2),
    _DevLinkIntegrity_Type()
)
devLinkIntegrity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devLinkIntegrity.setStatus("current")
_CommunityTrapAddressInfoTable_Object = MibTable
communityTrapAddressInfoTable = _CommunityTrapAddressInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3)
)
if mibBuilder.loadTexts:
    communityTrapAddressInfoTable.setStatus("current")
_CommunityTrapAddressInfoTableEntry_Object = MibTableRow
communityTrapAddressInfoTableEntry = _CommunityTrapAddressInfoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1)
)
communityTrapAddressInfoTableEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "trapCommunityName"),
    (0, "PDN-DSLAM-SYSTEM-MIB", "trapDestAndPort"),
)
if mibBuilder.loadTexts:
    communityTrapAddressInfoTableEntry.setStatus("current")


class _TrapCommunityName_Type(DisplayString):
    """Custom type trapCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrapCommunityName_Type.__name__ = "DisplayString"
_TrapCommunityName_Object = MibTableColumn
trapCommunityName = _TrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 1),
    _TrapCommunityName_Type()
)
trapCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapCommunityName.setStatus("current")
_TrapDestAndPort_Type = TAddress
_TrapDestAndPort_Object = MibTableColumn
trapDestAndPort = _TrapDestAndPort_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 2),
    _TrapDestAndPort_Type()
)
trapDestAndPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestAndPort.setStatus("current")


class _TrapsEnable_Type(Integer32):
    """Custom type trapsEnable based on Integer32"""
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


_TrapsEnable_Type.__name__ = "Integer32"
_TrapsEnable_Object = MibTableColumn
trapsEnable = _TrapsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 3),
    _TrapsEnable_Type()
)
trapsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapsEnable.setStatus("current")
_TrapRowStatus_Type = RowStatus
_TrapRowStatus_Object = MibTableColumn
trapRowStatus = _TrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 3, 1, 4),
    _TrapRowStatus_Type()
)
trapRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapRowStatus.setStatus("current")
_EntCommunityTable_Object = MibTable
entCommunityTable = _EntCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4)
)
if mibBuilder.loadTexts:
    entCommunityTable.setStatus("current")
_EntCommunityTableEntry_Object = MibTableRow
entCommunityTableEntry = _EntCommunityTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1)
)
entCommunityTableEntry.setIndexNames(
    (1, "PDN-DSLAM-SYSTEM-MIB", "entCommunityName"),
)
if mibBuilder.loadTexts:
    entCommunityTableEntry.setStatus("current")


class _EntCommunityName_Type(DisplayString):
    """Custom type entCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EntCommunityName_Type.__name__ = "DisplayString"
_EntCommunityName_Object = MibTableColumn
entCommunityName = _EntCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 1),
    _EntCommunityName_Type()
)
entCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    entCommunityName.setStatus("current")


class _EntCommunityType_Type(Integer32):
    """Custom type entCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_EntCommunityType_Type.__name__ = "Integer32"
_EntCommunityType_Object = MibTableColumn
entCommunityType = _EntCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 2),
    _EntCommunityType_Type()
)
entCommunityType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    entCommunityType.setStatus("current")
_EntCommunityRowStatus_Type = RowStatus
_EntCommunityRowStatus_Object = MibTableColumn
entCommunityRowStatus = _EntCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 4, 1, 3),
    _EntCommunityRowStatus_Type()
)
entCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    entCommunityRowStatus.setStatus("current")
_SysDevUserAccountTable_Object = MibTable
sysDevUserAccountTable = _SysDevUserAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5)
)
if mibBuilder.loadTexts:
    sysDevUserAccountTable.setStatus("current")
_SysDevUserAccountEntry_Object = MibTableRow
sysDevUserAccountEntry = _SysDevUserAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1)
)
sysDevUserAccountEntry.setIndexNames(
    (1, "PDN-DSLAM-SYSTEM-MIB", "sysDevUserAccountUserId"),
)
if mibBuilder.loadTexts:
    sysDevUserAccountEntry.setStatus("current")


class _SysDevUserAccountUserId_Type(DisplayString):
    """Custom type sysDevUserAccountUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 15),
    )


_SysDevUserAccountUserId_Type.__name__ = "DisplayString"
_SysDevUserAccountUserId_Object = MibTableColumn
sysDevUserAccountUserId = _SysDevUserAccountUserId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 1),
    _SysDevUserAccountUserId_Type()
)
sysDevUserAccountUserId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDevUserAccountUserId.setStatus("current")


class _SysDevUserAccountPrivilege_Type(Integer32):
    """Custom type sysDevUserAccountPrivilege based on Integer32"""
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
        *(("operator", 1),
          ("administrator", 2),
          ("maintenance", 3),
          ("provisioning", 4),
          ("manufacturing", 5))
    )


_SysDevUserAccountPrivilege_Type.__name__ = "Integer32"
_SysDevUserAccountPrivilege_Object = MibTableColumn
sysDevUserAccountPrivilege = _SysDevUserAccountPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 2),
    _SysDevUserAccountPrivilege_Type()
)
sysDevUserAccountPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevUserAccountPrivilege.setStatus("current")


class _SysDevUserAccountUserPassword_Type(DisplayString):
    """Custom type sysDevUserAccountUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 15),
    )


_SysDevUserAccountUserPassword_Type.__name__ = "DisplayString"
_SysDevUserAccountUserPassword_Object = MibTableColumn
sysDevUserAccountUserPassword = _SysDevUserAccountUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 3),
    _SysDevUserAccountUserPassword_Type()
)
sysDevUserAccountUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevUserAccountUserPassword.setStatus("current")


class _SysDevUserAccountAccessPartition_Type(DisplayString):
    """Custom type sysDevUserAccountAccessPartition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SysDevUserAccountAccessPartition_Type.__name__ = "DisplayString"
_SysDevUserAccountAccessPartition_Object = MibTableColumn
sysDevUserAccountAccessPartition = _SysDevUserAccountAccessPartition_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 4),
    _SysDevUserAccountAccessPartition_Type()
)
sysDevUserAccountAccessPartition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevUserAccountAccessPartition.setStatus("current")
_SysDevUserAccountRowStatus_Type = RowStatus
_SysDevUserAccountRowStatus_Object = MibTableColumn
sysDevUserAccountRowStatus = _SysDevUserAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 5, 1, 5),
    _SysDevUserAccountRowStatus_Type()
)
sysDevUserAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevUserAccountRowStatus.setStatus("current")
_SysDevIDSLConfigTable_Object = MibTable
sysDevIDSLConfigTable = _SysDevIDSLConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sysDevIDSLConfigTable.setStatus("current")
_SysDevIDSLConfigEntry_Object = MibTableRow
sysDevIDSLConfigEntry = _SysDevIDSLConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1)
)
sysDevIDSLConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    sysDevIDSLConfigEntry.setStatus("current")


class _SysDevIDSLConfigPrimaryNetClockMode_Type(IdslClockMode):
    """Custom type sysDevIDSLConfigPrimaryNetClockMode based on IdslClockMode"""
    defaultValue = 1


_SysDevIDSLConfigPrimaryNetClockMode_Type.__name__ = "IdslClockMode"
_SysDevIDSLConfigPrimaryNetClockMode_Object = MibTableColumn
sysDevIDSLConfigPrimaryNetClockMode = _SysDevIDSLConfigPrimaryNetClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1, 1),
    _SysDevIDSLConfigPrimaryNetClockMode_Type()
)
sysDevIDSLConfigPrimaryNetClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevIDSLConfigPrimaryNetClockMode.setStatus("current")


class _SysDevIDSLConfigSecondaryNetClockMode_Type(IdslClockMode):
    """Custom type sysDevIDSLConfigSecondaryNetClockMode based on IdslClockMode"""
    defaultValue = 1


_SysDevIDSLConfigSecondaryNetClockMode_Type.__name__ = "IdslClockMode"
_SysDevIDSLConfigSecondaryNetClockMode_Object = MibTableColumn
sysDevIDSLConfigSecondaryNetClockMode = _SysDevIDSLConfigSecondaryNetClockMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 6, 1, 2),
    _SysDevIDSLConfigSecondaryNetClockMode_Type()
)
sysDevIDSLConfigSecondaryNetClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevIDSLConfigSecondaryNetClockMode.setStatus("current")
_SysDevDslamSyslog_ObjectIdentity = ObjectIdentity
sysDevDslamSyslog = _SysDevDslamSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7)
)


class _SysDevSyslogFtpServerXferStatsEnable_Type(SwitchState):
    """Custom type sysDevSyslogFtpServerXferStatsEnable based on SwitchState"""
    defaultValue = 2


_SysDevSyslogFtpServerXferStatsEnable_Type.__name__ = "SwitchState"
_SysDevSyslogFtpServerXferStatsEnable_Object = MibScalar
sysDevSyslogFtpServerXferStatsEnable = _SysDevSyslogFtpServerXferStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7, 1),
    _SysDevSyslogFtpServerXferStatsEnable_Type()
)
sysDevSyslogFtpServerXferStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevSyslogFtpServerXferStatsEnable.setStatus("current")


class _SysDevSyslogTftpServerXferStatsEnable_Type(SwitchState):
    """Custom type sysDevSyslogTftpServerXferStatsEnable based on SwitchState"""
    defaultValue = 2


_SysDevSyslogTftpServerXferStatsEnable_Type.__name__ = "SwitchState"
_SysDevSyslogTftpServerXferStatsEnable_Object = MibScalar
sysDevSyslogTftpServerXferStatsEnable = _SysDevSyslogTftpServerXferStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 7, 2),
    _SysDevSyslogTftpServerXferStatsEnable_Type()
)
sysDevSyslogTftpServerXferStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDevSyslogTftpServerXferStatsEnable.setStatus("current")
_SysDevConfigUserAccountTable_Object = MibTable
sysDevConfigUserAccountTable = _SysDevConfigUserAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8)
)
if mibBuilder.loadTexts:
    sysDevConfigUserAccountTable.setStatus("current")
_SysDevConfigUserAccountEntry_Object = MibTableRow
sysDevConfigUserAccountEntry = _SysDevConfigUserAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8, 1)
)
sysDevConfigUserAccountEntry.setIndexNames(
    (0, "PDN-DSLAM-SYSTEM-MIB", "sysDevConfigUserAccountIndex"),
)
if mibBuilder.loadTexts:
    sysDevConfigUserAccountEntry.setStatus("current")
_SysDevConfigUserAccountIndex_Type = Integer32
_SysDevConfigUserAccountIndex_Object = MibTableColumn
sysDevConfigUserAccountIndex = _SysDevConfigUserAccountIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8, 1, 1),
    _SysDevConfigUserAccountIndex_Type()
)
sysDevConfigUserAccountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sysDevConfigUserAccountIndex.setStatus("current")


class _SysDevConfigUserAccountUserId_Type(DisplayString):
    """Custom type sysDevConfigUserAccountUserId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SysDevConfigUserAccountUserId_Type.__name__ = "DisplayString"
_SysDevConfigUserAccountUserId_Object = MibTableColumn
sysDevConfigUserAccountUserId = _SysDevConfigUserAccountUserId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8, 1, 2),
    _SysDevConfigUserAccountUserId_Type()
)
sysDevConfigUserAccountUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevConfigUserAccountUserId.setStatus("current")


class _SysDevConfigUserAccountPrivilegedPassword_Type(DisplayString):
    """Custom type sysDevConfigUserAccountPrivilegedPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysDevConfigUserAccountPrivilegedPassword_Type.__name__ = "DisplayString"
_SysDevConfigUserAccountPrivilegedPassword_Object = MibTableColumn
sysDevConfigUserAccountPrivilegedPassword = _SysDevConfigUserAccountPrivilegedPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8, 1, 3),
    _SysDevConfigUserAccountPrivilegedPassword_Type()
)
sysDevConfigUserAccountPrivilegedPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevConfigUserAccountPrivilegedPassword.setStatus("current")


class _SysDevConfigUserAccountUserPassword_Type(DisplayString):
    """Custom type sysDevConfigUserAccountUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysDevConfigUserAccountUserPassword_Type.__name__ = "DisplayString"
_SysDevConfigUserAccountUserPassword_Object = MibTableColumn
sysDevConfigUserAccountUserPassword = _SysDevConfigUserAccountUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8, 1, 4),
    _SysDevConfigUserAccountUserPassword_Type()
)
sysDevConfigUserAccountUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevConfigUserAccountUserPassword.setStatus("current")
_SysDevConfigUserAccountRowStatus_Type = RowStatus
_SysDevConfigUserAccountRowStatus_Object = MibTableColumn
sysDevConfigUserAccountRowStatus = _SysDevConfigUserAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 8, 1, 5),
    _SysDevConfigUserAccountRowStatus_Type()
)
sysDevConfigUserAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sysDevConfigUserAccountRowStatus.setStatus("current")
_SysDevConfigUserAccountIndexNext_Type = Integer32
_SysDevConfigUserAccountIndexNext_Object = MibScalar
sysDevConfigUserAccountIndexNext = _SysDevConfigUserAccountIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 1, 2, 9),
    _SysDevConfigUserAccountIndexNext_Type()
)
sysDevConfigUserAccountIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDevConfigUserAccountIndexNext.setStatus("current")
_SysDevDslamMIBTraps_ObjectIdentity = ObjectIdentity
sysDevDslamMIBTraps = _SysDevDslamMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2)
)

# Managed Objects groups


# Notification objects

cCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 7)
)
cCN.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    cCN.setStatus(
        "current"
    )

authenticationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 8)
)
authenticationFailureTrap.setObjects(
      *(("PDN-DSLAM-SYSTEM-MIB", "loginFailureAccessApp"),
        ("PDN-DSLAM-SYSTEM-MIB", "loginFailureCount"))
)
if mibBuilder.loadTexts:
    authenticationFailureTrap.setStatus(
        "current"
    )

fanModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 9)
)
if mibBuilder.loadTexts:
    fanModuleFailure.setStatus(
        "current"
    )

powerSourceAFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 10)
)
if mibBuilder.loadTexts:
    powerSourceAFailure.setStatus(
        "current"
    )

slotPollFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 11)
)
slotPollFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    slotPollFailure.setStatus(
        "current"
    )

ethernetJabber = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 12)
)
ethernetJabber.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetJabber.setStatus(
        "current"
    )

ethernetJumbos = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 13)
)
ethernetJumbos.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetJumbos.setStatus(
        "current"
    )

ethernetRunts = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 14)
)
ethernetRunts.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetRunts.setStatus(
        "current"
    )

powerSourceBFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 17)
)
if mibBuilder.loadTexts:
    powerSourceBFailure.setStatus(
        "current"
    )

nonIpConservativeCardDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 18)
)
nonIpConservativeCardDetected.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    nonIpConservativeCardDetected.setStatus(
        "current"
    )

nonSupportedMCC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 20)
)
nonSupportedMCC.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    nonSupportedMCC.setStatus(
        "current"
    )

nonSupportedChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 21)
)
nonSupportedChassis.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    nonSupportedChassis.setStatus(
        "current"
    )

fanEntityModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 22)
)
fanEntityModuleFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    fanEntityModuleFailure.setStatus(
        "current"
    )

fanModuleOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 109)
)
if mibBuilder.loadTexts:
    fanModuleOperational.setStatus(
        "current"
    )

powerSourceAOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 110)
)
if mibBuilder.loadTexts:
    powerSourceAOperational.setStatus(
        "current"
    )

newCardDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 111)
)
newCardDetected.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    newCardDetected.setStatus(
        "current"
    )

ethernetJabberClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 112)
)
ethernetJabberClear.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    ethernetJabberClear.setStatus(
        "current"
    )

powerSourceBOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 117)
)
if mibBuilder.loadTexts:
    powerSourceBOperational.setStatus(
        "current"
    )

fanEntityModuleOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 24, 2, 122)
)
fanEntityModuleOperational.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    fanEntityModuleOperational.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DSLAM-SYSTEM-MIB",
    **{"pdn-dslam": pdn_dslam,
       "sysDevDslamMIBObjects": sysDevDslamMIBObjects,
       "sysDevStats": sysDevStats,
       "loginHistTable": loginHistTable,
       "loginHistTableEntry": loginHistTableEntry,
       "loginUserId": loginUserId,
       "loginTime": loginTime,
       "loginAccessApp": loginAccessApp,
       "loginAccessHost": loginAccessHost,
       "loginUserPriv": loginUserPriv,
       "loginStatus": loginStatus,
       "loginFailureCountTable": loginFailureCountTable,
       "loginFailureCountTableEntry": loginFailureCountTableEntry,
       "loginFailureAccessApp": loginFailureAccessApp,
       "loginFailureCount": loginFailureCount,
       "sysDevConfig": sysDevConfig,
       "enablePowerSourceFailureAlarm": enablePowerSourceFailureAlarm,
       "devIfTable": devIfTable,
       "devIfTableEntry": devIfTableEntry,
       "devPacketDiscardPolicy": devPacketDiscardPolicy,
       "devLinkIntegrity": devLinkIntegrity,
       "communityTrapAddressInfoTable": communityTrapAddressInfoTable,
       "communityTrapAddressInfoTableEntry": communityTrapAddressInfoTableEntry,
       "trapCommunityName": trapCommunityName,
       "trapDestAndPort": trapDestAndPort,
       "trapsEnable": trapsEnable,
       "trapRowStatus": trapRowStatus,
       "entCommunityTable": entCommunityTable,
       "entCommunityTableEntry": entCommunityTableEntry,
       "entCommunityName": entCommunityName,
       "entCommunityType": entCommunityType,
       "entCommunityRowStatus": entCommunityRowStatus,
       "sysDevUserAccountTable": sysDevUserAccountTable,
       "sysDevUserAccountEntry": sysDevUserAccountEntry,
       "sysDevUserAccountUserId": sysDevUserAccountUserId,
       "sysDevUserAccountPrivilege": sysDevUserAccountPrivilege,
       "sysDevUserAccountUserPassword": sysDevUserAccountUserPassword,
       "sysDevUserAccountAccessPartition": sysDevUserAccountAccessPartition,
       "sysDevUserAccountRowStatus": sysDevUserAccountRowStatus,
       "sysDevIDSLConfigTable": sysDevIDSLConfigTable,
       "sysDevIDSLConfigEntry": sysDevIDSLConfigEntry,
       "sysDevIDSLConfigPrimaryNetClockMode": sysDevIDSLConfigPrimaryNetClockMode,
       "sysDevIDSLConfigSecondaryNetClockMode": sysDevIDSLConfigSecondaryNetClockMode,
       "sysDevDslamSyslog": sysDevDslamSyslog,
       "sysDevSyslogFtpServerXferStatsEnable": sysDevSyslogFtpServerXferStatsEnable,
       "sysDevSyslogTftpServerXferStatsEnable": sysDevSyslogTftpServerXferStatsEnable,
       "sysDevConfigUserAccountTable": sysDevConfigUserAccountTable,
       "sysDevConfigUserAccountEntry": sysDevConfigUserAccountEntry,
       "sysDevConfigUserAccountIndex": sysDevConfigUserAccountIndex,
       "sysDevConfigUserAccountUserId": sysDevConfigUserAccountUserId,
       "sysDevConfigUserAccountPrivilegedPassword": sysDevConfigUserAccountPrivilegedPassword,
       "sysDevConfigUserAccountUserPassword": sysDevConfigUserAccountUserPassword,
       "sysDevConfigUserAccountRowStatus": sysDevConfigUserAccountRowStatus,
       "sysDevConfigUserAccountIndexNext": sysDevConfigUserAccountIndexNext,
       "sysDevDslamMIBTraps": sysDevDslamMIBTraps,
       "cCN": cCN,
       "authenticationFailureTrap": authenticationFailureTrap,
       "fanModuleFailure": fanModuleFailure,
       "powerSourceAFailure": powerSourceAFailure,
       "slotPollFailure": slotPollFailure,
       "ethernetJabber": ethernetJabber,
       "ethernetJumbos": ethernetJumbos,
       "ethernetRunts": ethernetRunts,
       "powerSourceBFailure": powerSourceBFailure,
       "nonIpConservativeCardDetected": nonIpConservativeCardDetected,
       "nonSupportedMCC": nonSupportedMCC,
       "nonSupportedChassis": nonSupportedChassis,
       "fanEntityModuleFailure": fanEntityModuleFailure,
       "fanModuleOperational": fanModuleOperational,
       "powerSourceAOperational": powerSourceAOperational,
       "newCardDetected": newCardDetected,
       "ethernetJabberClear": ethernetJabberClear,
       "powerSourceBOperational": powerSourceBOperational,
       "fanEntityModuleOperational": fanEntityModuleOperational}
)
