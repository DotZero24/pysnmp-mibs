# SNMP MIB module (RAISECOM-RCMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RCMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:30 2025
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

(raisecomCluster,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomCluster")

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

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomRcmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1)
)
if mibBuilder.loadTexts:
    raisecomRcmp.setRevisions(
        ("1904-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RaisecomRcmpClusterEnable_Type(EnableVar):
    """Custom type raisecomRcmpClusterEnable based on EnableVar"""
    defaultValue = 2


_RaisecomRcmpClusterEnable_Type.__name__ = "EnableVar"
_RaisecomRcmpClusterEnable_Object = MibScalar
raisecomRcmpClusterEnable = _RaisecomRcmpClusterEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 1),
    _RaisecomRcmpClusterEnable_Type()
)
raisecomRcmpClusterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpClusterEnable.setStatus("current")


class _RaisecomRcmpIdentity_Type(Integer32):
    """Custom type raisecomRcmpIdentity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("member", 1),
          ("candidate", 2),
          ("commander", 3))
    )


_RaisecomRcmpIdentity_Type.__name__ = "Integer32"
_RaisecomRcmpIdentity_Object = MibScalar
raisecomRcmpIdentity = _RaisecomRcmpIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 2),
    _RaisecomRcmpIdentity_Type()
)
raisecomRcmpIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpIdentity.setStatus("current")
_RaisecomRcmpCommanderMac_Type = MacAddress
_RaisecomRcmpCommanderMac_Object = MibScalar
raisecomRcmpCommanderMac = _RaisecomRcmpCommanderMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 3),
    _RaisecomRcmpCommanderMac_Type()
)
raisecomRcmpCommanderMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpCommanderMac.setStatus("current")


class _RaisecomRcmpAutoActiveEnable_Type(EnableVar):
    """Custom type raisecomRcmpAutoActiveEnable based on EnableVar"""
    defaultValue = 2


_RaisecomRcmpAutoActiveEnable_Type.__name__ = "EnableVar"
_RaisecomRcmpAutoActiveEnable_Object = MibScalar
raisecomRcmpAutoActiveEnable = _RaisecomRcmpAutoActiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 4),
    _RaisecomRcmpAutoActiveEnable_Type()
)
raisecomRcmpAutoActiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpAutoActiveEnable.setStatus("current")
_RaisecomRcmpAutoActiveCommanderMac_Type = MacAddress
_RaisecomRcmpAutoActiveCommanderMac_Object = MibScalar
raisecomRcmpAutoActiveCommanderMac = _RaisecomRcmpAutoActiveCommanderMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 5),
    _RaisecomRcmpAutoActiveCommanderMac_Type()
)
raisecomRcmpAutoActiveCommanderMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpAutoActiveCommanderMac.setStatus("current")
_RaisecomRcmpMemberTable_Object = MibTable
raisecomRcmpMemberTable = _RaisecomRcmpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    raisecomRcmpMemberTable.setStatus("current")
_RaisecomRcmpMemberEntry_Object = MibTableRow
raisecomRcmpMemberEntry = _RaisecomRcmpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1)
)
raisecomRcmpMemberEntry.setIndexNames(
    (0, "RAISECOM-RCMP-MIB", "raisecomRcmpMacAddress"),
)
if mibBuilder.loadTexts:
    raisecomRcmpMemberEntry.setStatus("current")
_RaisecomRcmpMacAddress_Type = MacAddress
_RaisecomRcmpMacAddress_Object = MibTableColumn
raisecomRcmpMacAddress = _RaisecomRcmpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 1),
    _RaisecomRcmpMacAddress_Type()
)
raisecomRcmpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpMacAddress.setStatus("current")
_RaisecomRcmpHostName_Type = OctetString
_RaisecomRcmpHostName_Object = MibTableColumn
raisecomRcmpHostName = _RaisecomRcmpHostName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 2),
    _RaisecomRcmpHostName_Type()
)
raisecomRcmpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpHostName.setStatus("current")
_RaisecomRcmpActiveEnable_Type = EnableVar
_RaisecomRcmpActiveEnable_Object = MibTableColumn
raisecomRcmpActiveEnable = _RaisecomRcmpActiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 3),
    _RaisecomRcmpActiveEnable_Type()
)
raisecomRcmpActiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpActiveEnable.setStatus("current")


class _RaisecomRcmpOperationState_Type(Integer32):
    """Custom type raisecomRcmpOperationState based on Integer32"""
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


_RaisecomRcmpOperationState_Type.__name__ = "Integer32"
_RaisecomRcmpOperationState_Object = MibTableColumn
raisecomRcmpOperationState = _RaisecomRcmpOperationState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 4),
    _RaisecomRcmpOperationState_Type()
)
raisecomRcmpOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpOperationState.setStatus("current")
_RaisecomRcmpUdpPortNumber_Type = Integer32
_RaisecomRcmpUdpPortNumber_Object = MibTableColumn
raisecomRcmpUdpPortNumber = _RaisecomRcmpUdpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 5),
    _RaisecomRcmpUdpPortNumber_Type()
)
raisecomRcmpUdpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpUdpPortNumber.setStatus("current")


class _RaisecomRcmpUserName_Type(OctetString):
    """Custom type raisecomRcmpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RaisecomRcmpUserName_Type.__name__ = "OctetString"
_RaisecomRcmpUserName_Object = MibTableColumn
raisecomRcmpUserName = _RaisecomRcmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 6),
    _RaisecomRcmpUserName_Type()
)
raisecomRcmpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpUserName.setStatus("current")


class _RaisecomRcmpPassword_Type(OctetString):
    """Custom type raisecomRcmpPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_RaisecomRcmpPassword_Type.__name__ = "OctetString"
_RaisecomRcmpPassword_Object = MibTableColumn
raisecomRcmpPassword = _RaisecomRcmpPassword_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 7),
    _RaisecomRcmpPassword_Type()
)
raisecomRcmpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpPassword.setStatus("current")
_RaisecomRcmpRowStatus_Type = RowStatus
_RaisecomRcmpRowStatus_Object = MibTableColumn
raisecomRcmpRowStatus = _RaisecomRcmpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 6, 1, 8),
    _RaisecomRcmpRowStatus_Type()
)
raisecomRcmpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomRcmpRowStatus.setStatus("current")


class _RaisecomRcmpSessionTimeout_Type(Integer32):
    """Custom type raisecomRcmpSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 600),
    )


_RaisecomRcmpSessionTimeout_Type.__name__ = "Integer32"
_RaisecomRcmpSessionTimeout_Object = MibScalar
raisecomRcmpSessionTimeout = _RaisecomRcmpSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 7),
    _RaisecomRcmpSessionTimeout_Type()
)
raisecomRcmpSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpSessionTimeout.setStatus("current")


class _RaisecomRcmpMaxSession_Type(Integer32):
    """Custom type raisecomRcmpMaxSession based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RaisecomRcmpMaxSession_Type.__name__ = "Integer32"
_RaisecomRcmpMaxSession_Object = MibScalar
raisecomRcmpMaxSession = _RaisecomRcmpMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 8),
    _RaisecomRcmpMaxSession_Type()
)
raisecomRcmpMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpMaxSession.setStatus("current")


class _RaisecomRcmpMaxSessionPerMember_Type(Integer32):
    """Custom type raisecomRcmpMaxSessionPerMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_RaisecomRcmpMaxSessionPerMember_Type.__name__ = "Integer32"
_RaisecomRcmpMaxSessionPerMember_Object = MibScalar
raisecomRcmpMaxSessionPerMember = _RaisecomRcmpMaxSessionPerMember_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 9),
    _RaisecomRcmpMaxSessionPerMember_Type()
)
raisecomRcmpMaxSessionPerMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpMaxSessionPerMember.setStatus("current")


class _RaisecomRcmpMaxMember_Type(Integer32):
    """Custom type raisecomRcmpMaxMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RaisecomRcmpMaxMember_Type.__name__ = "Integer32"
_RaisecomRcmpMaxMember_Object = MibScalar
raisecomRcmpMaxMember = _RaisecomRcmpMaxMember_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 10),
    _RaisecomRcmpMaxMember_Type()
)
raisecomRcmpMaxMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpMaxMember.setStatus("current")
_RaisecomRcmpID_Type = MacAddress
_RaisecomRcmpID_Object = MibScalar
raisecomRcmpID = _RaisecomRcmpID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 11),
    _RaisecomRcmpID_Type()
)
raisecomRcmpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpID.setStatus("current")
_RaisecomRcmpStatisticsTotalSession_Type = Counter32
_RaisecomRcmpStatisticsTotalSession_Object = MibScalar
raisecomRcmpStatisticsTotalSession = _RaisecomRcmpStatisticsTotalSession_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 12),
    _RaisecomRcmpStatisticsTotalSession_Type()
)
raisecomRcmpStatisticsTotalSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsTotalSession.setStatus("current")
_RaisecomRcmpStatisticsCurrentSession_Type = Counter32
_RaisecomRcmpStatisticsCurrentSession_Object = MibScalar
raisecomRcmpStatisticsCurrentSession = _RaisecomRcmpStatisticsCurrentSession_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 13),
    _RaisecomRcmpStatisticsCurrentSession_Type()
)
raisecomRcmpStatisticsCurrentSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsCurrentSession.setStatus("current")
_RaisecomRcmpStatisticsMaxSession_Type = Counter32
_RaisecomRcmpStatisticsMaxSession_Object = MibScalar
raisecomRcmpStatisticsMaxSession = _RaisecomRcmpStatisticsMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 14),
    _RaisecomRcmpStatisticsMaxSession_Type()
)
raisecomRcmpStatisticsMaxSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsMaxSession.setStatus("current")
_RaisecomRcmpStatisticsTimeoutSession_Type = Counter32
_RaisecomRcmpStatisticsTimeoutSession_Object = MibScalar
raisecomRcmpStatisticsTimeoutSession = _RaisecomRcmpStatisticsTimeoutSession_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 15),
    _RaisecomRcmpStatisticsTimeoutSession_Type()
)
raisecomRcmpStatisticsTimeoutSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsTimeoutSession.setStatus("current")
_RaisecomRcmpStatisticsInPkts_Type = Counter32
_RaisecomRcmpStatisticsInPkts_Object = MibScalar
raisecomRcmpStatisticsInPkts = _RaisecomRcmpStatisticsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 16),
    _RaisecomRcmpStatisticsInPkts_Type()
)
raisecomRcmpStatisticsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsInPkts.setStatus("current")
_RaisecomRcmpStatisticsOutPkts_Type = Counter32
_RaisecomRcmpStatisticsOutPkts_Object = MibScalar
raisecomRcmpStatisticsOutPkts = _RaisecomRcmpStatisticsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 17),
    _RaisecomRcmpStatisticsOutPkts_Type()
)
raisecomRcmpStatisticsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsOutPkts.setStatus("current")
_RaisecomRcmpStatisticsDiscardPkts_Type = Counter32
_RaisecomRcmpStatisticsDiscardPkts_Object = MibScalar
raisecomRcmpStatisticsDiscardPkts = _RaisecomRcmpStatisticsDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 18),
    _RaisecomRcmpStatisticsDiscardPkts_Type()
)
raisecomRcmpStatisticsDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsDiscardPkts.setStatus("current")
_RaisecomRcmpStatisticsErrorPkts_Type = Counter32
_RaisecomRcmpStatisticsErrorPkts_Object = MibScalar
raisecomRcmpStatisticsErrorPkts = _RaisecomRcmpStatisticsErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 19),
    _RaisecomRcmpStatisticsErrorPkts_Type()
)
raisecomRcmpStatisticsErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpStatisticsErrorPkts.setStatus("current")
_RaisecomRcmpDefaultVlan_Type = Integer32
_RaisecomRcmpDefaultVlan_Object = MibScalar
raisecomRcmpDefaultVlan = _RaisecomRcmpDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 20),
    _RaisecomRcmpDefaultVlan_Type()
)
raisecomRcmpDefaultVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRcmpDefaultVlan.setStatus("current")


class _RaisecomRcmpClearStatistics_Type(Integer32):
    """Custom type raisecomRcmpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_RaisecomRcmpClearStatistics_Type.__name__ = "Integer32"
_RaisecomRcmpClearStatistics_Object = MibScalar
raisecomRcmpClearStatistics = _RaisecomRcmpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 6, 1, 21),
    _RaisecomRcmpClearStatistics_Type()
)
raisecomRcmpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRcmpClearStatistics.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RCMP-MIB",
    **{"raisecomRcmp": raisecomRcmp,
       "raisecomRcmpClusterEnable": raisecomRcmpClusterEnable,
       "raisecomRcmpIdentity": raisecomRcmpIdentity,
       "raisecomRcmpCommanderMac": raisecomRcmpCommanderMac,
       "raisecomRcmpAutoActiveEnable": raisecomRcmpAutoActiveEnable,
       "raisecomRcmpAutoActiveCommanderMac": raisecomRcmpAutoActiveCommanderMac,
       "raisecomRcmpMemberTable": raisecomRcmpMemberTable,
       "raisecomRcmpMemberEntry": raisecomRcmpMemberEntry,
       "raisecomRcmpMacAddress": raisecomRcmpMacAddress,
       "raisecomRcmpHostName": raisecomRcmpHostName,
       "raisecomRcmpActiveEnable": raisecomRcmpActiveEnable,
       "raisecomRcmpOperationState": raisecomRcmpOperationState,
       "raisecomRcmpUdpPortNumber": raisecomRcmpUdpPortNumber,
       "raisecomRcmpUserName": raisecomRcmpUserName,
       "raisecomRcmpPassword": raisecomRcmpPassword,
       "raisecomRcmpRowStatus": raisecomRcmpRowStatus,
       "raisecomRcmpSessionTimeout": raisecomRcmpSessionTimeout,
       "raisecomRcmpMaxSession": raisecomRcmpMaxSession,
       "raisecomRcmpMaxSessionPerMember": raisecomRcmpMaxSessionPerMember,
       "raisecomRcmpMaxMember": raisecomRcmpMaxMember,
       "raisecomRcmpID": raisecomRcmpID,
       "raisecomRcmpStatisticsTotalSession": raisecomRcmpStatisticsTotalSession,
       "raisecomRcmpStatisticsCurrentSession": raisecomRcmpStatisticsCurrentSession,
       "raisecomRcmpStatisticsMaxSession": raisecomRcmpStatisticsMaxSession,
       "raisecomRcmpStatisticsTimeoutSession": raisecomRcmpStatisticsTimeoutSession,
       "raisecomRcmpStatisticsInPkts": raisecomRcmpStatisticsInPkts,
       "raisecomRcmpStatisticsOutPkts": raisecomRcmpStatisticsOutPkts,
       "raisecomRcmpStatisticsDiscardPkts": raisecomRcmpStatisticsDiscardPkts,
       "raisecomRcmpStatisticsErrorPkts": raisecomRcmpStatisticsErrorPkts,
       "raisecomRcmpDefaultVlan": raisecomRcmpDefaultVlan,
       "raisecomRcmpClearStatistics": raisecomRcmpClearStatistics}
)
