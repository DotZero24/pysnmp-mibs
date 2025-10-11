# SNMP MIB module (ADTRAN-TA5K-TREE-NETWORKING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-TREE-NETWORKING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:53 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTa5kTreeNetworking,
 adTa5kTreeNetworkingID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adTa5kTreeNetworking",
    "adTa5kTreeNetworkingID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adTa5kTreeNetworkingModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 32, 1)
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingModuleIdentity.setRevisions(
        ("2014-02-17 00:00",
         "2011-11-01 23:00",
         "2011-10-26 18:00",
         "2011-10-12 00:00",
         "2011-04-12 21:12")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kTreeNetworkingAlarmPrefix_ObjectIdentity = ObjectIdentity
adTa5kTreeNetworkingAlarmPrefix = _AdTa5kTreeNetworkingAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1)
)
_AdTa5kTreeNetworkingAlarms_ObjectIdentity = ObjectIdentity
adTa5kTreeNetworkingAlarms = _AdTa5kTreeNetworkingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0)
)
_AdTa5kTreeNetworkingProvisioning_ObjectIdentity = ObjectIdentity
adTa5kTreeNetworkingProvisioning = _AdTa5kTreeNetworkingProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2)
)
_AdTa5kTreeNetworkingProvTable_Object = MibTable
adTa5kTreeNetworkingProvTable = _AdTa5kTreeNetworkingProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 1)
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingProvTable.setStatus("current")
_AdTa5kTreeNetworkingProvEntry_Object = MibTableRow
adTa5kTreeNetworkingProvEntry = _AdTa5kTreeNetworkingProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 1, 1)
)
adTa5kTreeNetworkingProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingProvEntry.setStatus("current")


class _AdTa5kTreeNetworkingPortMode_Type(Integer32):
    """Custom type adTa5kTreeNetworkingPortMode based on Integer32"""
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
        *(("unused", 1),
          ("networkInterface", 2),
          ("uplink", 3),
          ("downlink", 4),
          ("erps", 5),
          ("subtendedHost", 6),
          ("uni", 7))
    )


_AdTa5kTreeNetworkingPortMode_Type.__name__ = "Integer32"
_AdTa5kTreeNetworkingPortMode_Object = MibTableColumn
adTa5kTreeNetworkingPortMode = _AdTa5kTreeNetworkingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 1, 1, 1),
    _AdTa5kTreeNetworkingPortMode_Type()
)
adTa5kTreeNetworkingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingPortMode.setStatus("current")
_AdTa5kTreeNetworkingAlarmProvTable_Object = MibTable
adTa5kTreeNetworkingAlarmProvTable = _AdTa5kTreeNetworkingAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2)
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingAlarmProvTable.setStatus("current")
_AdTa5kTreeNetworkingAlarmProvEntry_Object = MibTableRow
adTa5kTreeNetworkingAlarmProvEntry = _AdTa5kTreeNetworkingAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2, 1)
)
adTa5kTreeNetworkingAlarmProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingAlarmProvEntry.setStatus("current")


class _AdTa5kSmPortModeMismatchAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmPortModeMismatchAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmPortModeMismatchAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmPortModeMismatchAlarmEnable_Object = MibTableColumn
adTa5kSmPortModeMismatchAlarmEnable = _AdTa5kSmPortModeMismatchAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2, 1, 1),
    _AdTa5kSmPortModeMismatchAlarmEnable_Type()
)
adTa5kSmPortModeMismatchAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmPortModeMismatchAlarmEnable.setStatus("current")


class _AdTa5kSmUpstreamShelfNotReadyAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmUpstreamShelfNotReadyAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmUpstreamShelfNotReadyAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmUpstreamShelfNotReadyAlarmEnable_Object = MibTableColumn
adTa5kSmUpstreamShelfNotReadyAlarmEnable = _AdTa5kSmUpstreamShelfNotReadyAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2, 1, 2),
    _AdTa5kSmUpstreamShelfNotReadyAlarmEnable_Type()
)
adTa5kSmUpstreamShelfNotReadyAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmUpstreamShelfNotReadyAlarmEnable.setStatus("current")


class _AdTa5kSmDownstreamShelfFaultAlarmEnable_Type(TruthValue):
    """Custom type adTa5kSmDownstreamShelfFaultAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kSmDownstreamShelfFaultAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kSmDownstreamShelfFaultAlarmEnable_Object = MibTableColumn
adTa5kSmDownstreamShelfFaultAlarmEnable = _AdTa5kSmDownstreamShelfFaultAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2, 1, 3),
    _AdTa5kSmDownstreamShelfFaultAlarmEnable_Type()
)
adTa5kSmDownstreamShelfFaultAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSmDownstreamShelfFaultAlarmEnable.setStatus("current")


class _AdTa5kTreeNetworkingLossOfHeartbeatAlarmEnable_Type(TruthValue):
    """Custom type adTa5kTreeNetworkingLossOfHeartbeatAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kTreeNetworkingLossOfHeartbeatAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kTreeNetworkingLossOfHeartbeatAlarmEnable_Object = MibTableColumn
adTa5kTreeNetworkingLossOfHeartbeatAlarmEnable = _AdTa5kTreeNetworkingLossOfHeartbeatAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2, 1, 4),
    _AdTa5kTreeNetworkingLossOfHeartbeatAlarmEnable_Type()
)
adTa5kTreeNetworkingLossOfHeartbeatAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingLossOfHeartbeatAlarmEnable.setStatus("current")


class _AdTa5kTreeNetworkingPortModeMismatchAlarmEnable_Type(TruthValue):
    """Custom type adTa5kTreeNetworkingPortModeMismatchAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kTreeNetworkingPortModeMismatchAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kTreeNetworkingPortModeMismatchAlarmEnable_Object = MibTableColumn
adTa5kTreeNetworkingPortModeMismatchAlarmEnable = _AdTa5kTreeNetworkingPortModeMismatchAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 2, 1, 5),
    _AdTa5kTreeNetworkingPortModeMismatchAlarmEnable_Type()
)
adTa5kTreeNetworkingPortModeMismatchAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingPortModeMismatchAlarmEnable.setStatus("current")


class _AdTa5kTreeNetworkingNodeAlarmLevelEnable_Type(TruthValue):
    """Custom type adTa5kTreeNetworkingNodeAlarmLevelEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kTreeNetworkingNodeAlarmLevelEnable_Type.__name__ = "TruthValue"
_AdTa5kTreeNetworkingNodeAlarmLevelEnable_Object = MibScalar
adTa5kTreeNetworkingNodeAlarmLevelEnable = _AdTa5kTreeNetworkingNodeAlarmLevelEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 2, 3),
    _AdTa5kTreeNetworkingNodeAlarmLevelEnable_Type()
)
adTa5kTreeNetworkingNodeAlarmLevelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingNodeAlarmLevelEnable.setStatus("current")
_AdTa5kTreeNetworkingStatus_ObjectIdentity = ObjectIdentity
adTa5kTreeNetworkingStatus = _AdTa5kTreeNetworkingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3)
)
_AdTa5kTreeNetworkingStatNodeInformationTable_Object = MibTable
adTa5kTreeNetworkingStatNodeInformationTable = _AdTa5kTreeNetworkingStatNodeInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1)
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingStatNodeInformationTable.setStatus("current")
_AdTa5kTreeNetworkingStatNodeInformationEntry_Object = MibTableRow
adTa5kTreeNetworkingStatNodeInformationEntry = _AdTa5kTreeNetworkingStatNodeInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1)
)
adTa5kTreeNetworkingStatNodeInformationEntry.setIndexNames(
    (0, "ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kNodeInformationNodeNumber"),
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingStatNodeInformationEntry.setStatus("current")
_AdTa5kNodeInformationNodeNumber_Type = Integer32
_AdTa5kNodeInformationNodeNumber_Object = MibTableColumn
adTa5kNodeInformationNodeNumber = _AdTa5kNodeInformationNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1, 1),
    _AdTa5kNodeInformationNodeNumber_Type()
)
adTa5kNodeInformationNodeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kNodeInformationNodeNumber.setStatus("current")
_AdTa5kNodeInformationManagementIP_Type = IpAddress
_AdTa5kNodeInformationManagementIP_Object = MibTableColumn
adTa5kNodeInformationManagementIP = _AdTa5kNodeInformationManagementIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1, 2),
    _AdTa5kNodeInformationManagementIP_Type()
)
adTa5kNodeInformationManagementIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kNodeInformationManagementIP.setStatus("current")
_AdTa5kNodeInformationManagementVLANID_Type = Integer32
_AdTa5kNodeInformationManagementVLANID_Object = MibTableColumn
adTa5kNodeInformationManagementVLANID = _AdTa5kNodeInformationManagementVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1, 3),
    _AdTa5kNodeInformationManagementVLANID_Type()
)
adTa5kNodeInformationManagementVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kNodeInformationManagementVLANID.setStatus("current")
_AdTa5kNodeInformationManagementMAC_Type = MacAddress
_AdTa5kNodeInformationManagementMAC_Object = MibTableColumn
adTa5kNodeInformationManagementMAC = _AdTa5kNodeInformationManagementMAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1, 4),
    _AdTa5kNodeInformationManagementMAC_Type()
)
adTa5kNodeInformationManagementMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kNodeInformationManagementMAC.setStatus("current")
_AdTa5kNodeInformationReceivedMessageCount_Type = Counter32
_AdTa5kNodeInformationReceivedMessageCount_Object = MibTableColumn
adTa5kNodeInformationReceivedMessageCount = _AdTa5kNodeInformationReceivedMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1, 5),
    _AdTa5kNodeInformationReceivedMessageCount_Type()
)
adTa5kNodeInformationReceivedMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kNodeInformationReceivedMessageCount.setStatus("current")
_AdTa5kNodeInformationTargetID_Type = DisplayString
_AdTa5kNodeInformationTargetID_Object = MibTableColumn
adTa5kNodeInformationTargetID = _AdTa5kNodeInformationTargetID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 1, 1, 6),
    _AdTa5kNodeInformationTargetID_Type()
)
adTa5kNodeInformationTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kNodeInformationTargetID.setStatus("current")
_AdTa5kTreeNetworkingStatDuplicateNodeInformationTable_Object = MibTable
adTa5kTreeNetworkingStatDuplicateNodeInformationTable = _AdTa5kTreeNetworkingStatDuplicateNodeInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2)
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingStatDuplicateNodeInformationTable.setStatus("current")
_AdTa5kTreeNetworkingStatDuplicateNodeInformationEntry_Object = MibTableRow
adTa5kTreeNetworkingStatDuplicateNodeInformationEntry = _AdTa5kTreeNetworkingStatDuplicateNodeInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1)
)
adTa5kTreeNetworkingStatDuplicateNodeInformationEntry.setIndexNames(
    (0, "ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kDuplicateNodeInformationNodeNumber"),
    (0, "ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kDuplicateNodeInformationManagementMAC"),
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingStatDuplicateNodeInformationEntry.setStatus("current")
_AdTa5kDuplicateNodeInformationNodeNumber_Type = Integer32
_AdTa5kDuplicateNodeInformationNodeNumber_Object = MibTableColumn
adTa5kDuplicateNodeInformationNodeNumber = _AdTa5kDuplicateNodeInformationNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1, 1),
    _AdTa5kDuplicateNodeInformationNodeNumber_Type()
)
adTa5kDuplicateNodeInformationNodeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kDuplicateNodeInformationNodeNumber.setStatus("current")
_AdTa5kDuplicateNodeInformationManagementIP_Type = IpAddress
_AdTa5kDuplicateNodeInformationManagementIP_Object = MibTableColumn
adTa5kDuplicateNodeInformationManagementIP = _AdTa5kDuplicateNodeInformationManagementIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1, 2),
    _AdTa5kDuplicateNodeInformationManagementIP_Type()
)
adTa5kDuplicateNodeInformationManagementIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDuplicateNodeInformationManagementIP.setStatus("current")
_AdTa5kDuplicateNodeInformationManagementVLANID_Type = Integer32
_AdTa5kDuplicateNodeInformationManagementVLANID_Object = MibTableColumn
adTa5kDuplicateNodeInformationManagementVLANID = _AdTa5kDuplicateNodeInformationManagementVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1, 3),
    _AdTa5kDuplicateNodeInformationManagementVLANID_Type()
)
adTa5kDuplicateNodeInformationManagementVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDuplicateNodeInformationManagementVLANID.setStatus("current")
_AdTa5kDuplicateNodeInformationManagementMAC_Type = MacAddress
_AdTa5kDuplicateNodeInformationManagementMAC_Object = MibTableColumn
adTa5kDuplicateNodeInformationManagementMAC = _AdTa5kDuplicateNodeInformationManagementMAC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1, 4),
    _AdTa5kDuplicateNodeInformationManagementMAC_Type()
)
adTa5kDuplicateNodeInformationManagementMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDuplicateNodeInformationManagementMAC.setStatus("current")
_AdTa5kDuplicateNodeInformationReceivedMessageCount_Type = Counter32
_AdTa5kDuplicateNodeInformationReceivedMessageCount_Object = MibTableColumn
adTa5kDuplicateNodeInformationReceivedMessageCount = _AdTa5kDuplicateNodeInformationReceivedMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1, 5),
    _AdTa5kDuplicateNodeInformationReceivedMessageCount_Type()
)
adTa5kDuplicateNodeInformationReceivedMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDuplicateNodeInformationReceivedMessageCount.setStatus("current")
_AdTa5kDuplicateNodeInformationTargetID_Type = DisplayString
_AdTa5kDuplicateNodeInformationTargetID_Object = MibTableColumn
adTa5kDuplicateNodeInformationTargetID = _AdTa5kDuplicateNodeInformationTargetID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 2, 1, 6),
    _AdTa5kDuplicateNodeInformationTargetID_Type()
)
adTa5kDuplicateNodeInformationTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kDuplicateNodeInformationTargetID.setStatus("current")
_AdTa5kTreeNetworkingNodeInformationStatistics_ObjectIdentity = ObjectIdentity
adTa5kTreeNetworkingNodeInformationStatistics = _AdTa5kTreeNetworkingNodeInformationStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 3)
)
_AdTa5kNodeInformationTotalReceivedCount_Type = Counter32
_AdTa5kNodeInformationTotalReceivedCount_Object = MibScalar
adTa5kNodeInformationTotalReceivedCount = _AdTa5kNodeInformationTotalReceivedCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 3, 1),
    _AdTa5kNodeInformationTotalReceivedCount_Type()
)
adTa5kNodeInformationTotalReceivedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kNodeInformationTotalReceivedCount.setStatus("current")
_AdTa5kInformationTotalTransmitCount_Type = Counter32
_AdTa5kInformationTotalTransmitCount_Object = MibScalar
adTa5kInformationTotalTransmitCount = _AdTa5kInformationTotalTransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 3, 2),
    _AdTa5kInformationTotalTransmitCount_Type()
)
adTa5kInformationTotalTransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kInformationTotalTransmitCount.setStatus("current")
_AdTa5kInformationTotalDiscardCount_Type = Counter32
_AdTa5kInformationTotalDiscardCount_Object = MibScalar
adTa5kInformationTotalDiscardCount = _AdTa5kInformationTotalDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 3, 3),
    _AdTa5kInformationTotalDiscardCount_Type()
)
adTa5kInformationTotalDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kInformationTotalDiscardCount.setStatus("current")
_AdTa5kTreeNetworkingTopologyTable_Object = MibTable
adTa5kTreeNetworkingTopologyTable = _AdTa5kTreeNetworkingTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 4)
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingTopologyTable.setStatus("current")
_AdTa5kTreeNetworkingTopologyEntry_Object = MibTableRow
adTa5kTreeNetworkingTopologyEntry = _AdTa5kTreeNetworkingTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 4, 1)
)
adTa5kTreeNetworkingTopologyEntry.setIndexNames(
    (0, "ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kTopologyNodeNumber"),
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingTopologyEntry.setStatus("current")
_AdTa5kTopologyNodeNumber_Type = Integer32
_AdTa5kTopologyNodeNumber_Object = MibTableColumn
adTa5kTopologyNodeNumber = _AdTa5kTopologyNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 4, 1, 1),
    _AdTa5kTopologyNodeNumber_Type()
)
adTa5kTopologyNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kTopologyNodeNumber.setStatus("current")
_AdTa5kTopologyManagementIP_Type = IpAddress
_AdTa5kTopologyManagementIP_Object = MibTableColumn
adTa5kTopologyManagementIP = _AdTa5kTopologyManagementIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 4, 1, 2),
    _AdTa5kTopologyManagementIP_Type()
)
adTa5kTopologyManagementIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kTopologyManagementIP.setStatus("current")
_AdTa5kTopologyHopCount_Type = Integer32
_AdTa5kTopologyHopCount_Object = MibTableColumn
adTa5kTopologyHopCount = _AdTa5kTopologyHopCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 3, 4, 1, 3),
    _AdTa5kTopologyHopCount_Type()
)
adTa5kTopologyHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kTopologyHopCount.setStatus("current")

# Managed Objects groups


# Notification objects

adTa5kSmPortModeMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 2)
)
adTa5kSmPortModeMismatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmPortModeMismatchClear.setStatus(
        "current"
    )

adTa5kSmPortModeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 3)
)
adTa5kSmPortModeMismatch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmPortModeMismatch.setStatus(
        "current"
    )

adTa5kSmUpstreamShelfNotReadyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 4)
)
adTa5kSmUpstreamShelfNotReadyClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmUpstreamShelfNotReadyClear.setStatus(
        "current"
    )

adTa5kSmUpstreamShelfNotReadyActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 5)
)
adTa5kSmUpstreamShelfNotReadyActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmUpstreamShelfNotReadyActive.setStatus(
        "current"
    )

adTa5kSmDownstreamShelfFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 6)
)
adTa5kSmDownstreamShelfFaultClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmDownstreamShelfFaultClear.setStatus(
        "current"
    )

adTa5kSmDownstreamShelfFaultActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 7)
)
adTa5kSmDownstreamShelfFaultActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmDownstreamShelfFaultActive.setStatus(
        "current"
    )

adTa5kTreeNetworkingLossOfHeartbeatClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 8)
)
adTa5kTreeNetworkingLossOfHeartbeatClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingLossOfHeartbeatClear.setStatus(
        "current"
    )

adTa5kTreeNetworkingLossOfHeartbeatActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 9)
)
adTa5kTreeNetworkingLossOfHeartbeatActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingLossOfHeartbeatActive.setStatus(
        "current"
    )

adTa5kTreeNetworkingPortModeMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 10)
)
adTa5kTreeNetworkingPortModeMismatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingPortModeMismatchClear.setStatus(
        "current"
    )

adTa5kTreeNetworkingPortModeMismatchActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 11)
)
adTa5kTreeNetworkingPortModeMismatchActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingPortModeMismatchActive.setStatus(
        "current"
    )

adTa5kTreeNetworkingNodeAlarmLevelClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 12)
)
adTa5kTreeNetworkingNodeAlarmLevelClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kTopologyNodeNumber"),
        ("ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kTopologyManagementIP"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingNodeAlarmLevelClear.setStatus(
        "current"
    )

adTa5kTreeNetworkingNodeAlarmLevelActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 32, 1, 0, 13)
)
adTa5kTreeNetworkingNodeAlarmLevelActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kTopologyNodeNumber"),
        ("ADTRAN-TA5K-TREE-NETWORKING-MIB", "adTa5kTopologyManagementIP"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTa5kTreeNetworkingNodeAlarmLevelActive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-TREE-NETWORKING-MIB",
    **{"adTa5kTreeNetworkingAlarmPrefix": adTa5kTreeNetworkingAlarmPrefix,
       "adTa5kTreeNetworkingAlarms": adTa5kTreeNetworkingAlarms,
       "adTa5kSmPortModeMismatchClear": adTa5kSmPortModeMismatchClear,
       "adTa5kSmPortModeMismatch": adTa5kSmPortModeMismatch,
       "adTa5kSmUpstreamShelfNotReadyClear": adTa5kSmUpstreamShelfNotReadyClear,
       "adTa5kSmUpstreamShelfNotReadyActive": adTa5kSmUpstreamShelfNotReadyActive,
       "adTa5kSmDownstreamShelfFaultClear": adTa5kSmDownstreamShelfFaultClear,
       "adTa5kSmDownstreamShelfFaultActive": adTa5kSmDownstreamShelfFaultActive,
       "adTa5kTreeNetworkingLossOfHeartbeatClear": adTa5kTreeNetworkingLossOfHeartbeatClear,
       "adTa5kTreeNetworkingLossOfHeartbeatActive": adTa5kTreeNetworkingLossOfHeartbeatActive,
       "adTa5kTreeNetworkingPortModeMismatchClear": adTa5kTreeNetworkingPortModeMismatchClear,
       "adTa5kTreeNetworkingPortModeMismatchActive": adTa5kTreeNetworkingPortModeMismatchActive,
       "adTa5kTreeNetworkingNodeAlarmLevelClear": adTa5kTreeNetworkingNodeAlarmLevelClear,
       "adTa5kTreeNetworkingNodeAlarmLevelActive": adTa5kTreeNetworkingNodeAlarmLevelActive,
       "adTa5kTreeNetworkingProvisioning": adTa5kTreeNetworkingProvisioning,
       "adTa5kTreeNetworkingProvTable": adTa5kTreeNetworkingProvTable,
       "adTa5kTreeNetworkingProvEntry": adTa5kTreeNetworkingProvEntry,
       "adTa5kTreeNetworkingPortMode": adTa5kTreeNetworkingPortMode,
       "adTa5kTreeNetworkingAlarmProvTable": adTa5kTreeNetworkingAlarmProvTable,
       "adTa5kTreeNetworkingAlarmProvEntry": adTa5kTreeNetworkingAlarmProvEntry,
       "adTa5kSmPortModeMismatchAlarmEnable": adTa5kSmPortModeMismatchAlarmEnable,
       "adTa5kSmUpstreamShelfNotReadyAlarmEnable": adTa5kSmUpstreamShelfNotReadyAlarmEnable,
       "adTa5kSmDownstreamShelfFaultAlarmEnable": adTa5kSmDownstreamShelfFaultAlarmEnable,
       "adTa5kTreeNetworkingLossOfHeartbeatAlarmEnable": adTa5kTreeNetworkingLossOfHeartbeatAlarmEnable,
       "adTa5kTreeNetworkingPortModeMismatchAlarmEnable": adTa5kTreeNetworkingPortModeMismatchAlarmEnable,
       "adTa5kTreeNetworkingNodeAlarmLevelEnable": adTa5kTreeNetworkingNodeAlarmLevelEnable,
       "adTa5kTreeNetworkingStatus": adTa5kTreeNetworkingStatus,
       "adTa5kTreeNetworkingStatNodeInformationTable": adTa5kTreeNetworkingStatNodeInformationTable,
       "adTa5kTreeNetworkingStatNodeInformationEntry": adTa5kTreeNetworkingStatNodeInformationEntry,
       "adTa5kNodeInformationNodeNumber": adTa5kNodeInformationNodeNumber,
       "adTa5kNodeInformationManagementIP": adTa5kNodeInformationManagementIP,
       "adTa5kNodeInformationManagementVLANID": adTa5kNodeInformationManagementVLANID,
       "adTa5kNodeInformationManagementMAC": adTa5kNodeInformationManagementMAC,
       "adTa5kNodeInformationReceivedMessageCount": adTa5kNodeInformationReceivedMessageCount,
       "adTa5kNodeInformationTargetID": adTa5kNodeInformationTargetID,
       "adTa5kTreeNetworkingStatDuplicateNodeInformationTable": adTa5kTreeNetworkingStatDuplicateNodeInformationTable,
       "adTa5kTreeNetworkingStatDuplicateNodeInformationEntry": adTa5kTreeNetworkingStatDuplicateNodeInformationEntry,
       "adTa5kDuplicateNodeInformationNodeNumber": adTa5kDuplicateNodeInformationNodeNumber,
       "adTa5kDuplicateNodeInformationManagementIP": adTa5kDuplicateNodeInformationManagementIP,
       "adTa5kDuplicateNodeInformationManagementVLANID": adTa5kDuplicateNodeInformationManagementVLANID,
       "adTa5kDuplicateNodeInformationManagementMAC": adTa5kDuplicateNodeInformationManagementMAC,
       "adTa5kDuplicateNodeInformationReceivedMessageCount": adTa5kDuplicateNodeInformationReceivedMessageCount,
       "adTa5kDuplicateNodeInformationTargetID": adTa5kDuplicateNodeInformationTargetID,
       "adTa5kTreeNetworkingNodeInformationStatistics": adTa5kTreeNetworkingNodeInformationStatistics,
       "adTa5kNodeInformationTotalReceivedCount": adTa5kNodeInformationTotalReceivedCount,
       "adTa5kInformationTotalTransmitCount": adTa5kInformationTotalTransmitCount,
       "adTa5kInformationTotalDiscardCount": adTa5kInformationTotalDiscardCount,
       "adTa5kTreeNetworkingTopologyTable": adTa5kTreeNetworkingTopologyTable,
       "adTa5kTreeNetworkingTopologyEntry": adTa5kTreeNetworkingTopologyEntry,
       "adTa5kTopologyNodeNumber": adTa5kTopologyNodeNumber,
       "adTa5kTopologyManagementIP": adTa5kTopologyManagementIP,
       "adTa5kTopologyHopCount": adTa5kTopologyHopCount,
       "adTa5kTreeNetworkingModuleIdentity": adTa5kTreeNetworkingModuleIdentity}
)
