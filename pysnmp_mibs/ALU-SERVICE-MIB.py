# SNMP MIB module (ALU-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-SERVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:49:02 2025
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

(AluSapSchedulerCir,) = mibBuilder.importSymbols(
    "ALU-QOS-MIB",
    "AluSapSchedulerCir")

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(sapAtmInfoEntry,
 sapBaseInfoEntry,
 sapCemInfoEntry,
 sapCemStatsEntry,
 sapEncapValue,
 sapEthCfmEntry,
 sapEthLoopbackEntry,
 sapEthernetInfoEntry,
 sapIpipeInfoEntry,
 sapPortId,
 sapTlsInfoEntry) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapAtmInfoEntry",
    "sapBaseInfoEntry",
    "sapCemInfoEntry",
    "sapCemStatsEntry",
    "sapEncapValue",
    "sapEthCfmEntry",
    "sapEthLoopbackEntry",
    "sapEthernetInfoEntry",
    "sapIpipeInfoEntry",
    "sapPortId",
    "sapTlsInfoEntry")

(sdpBindBaseStatsEntry,
 sdpBindCpipeEntry) = mibBuilder.importSymbols(
    "TIMETRA-SDP-MIB",
    "sdpBindBaseStatsEntry",
    "sdpBindCpipeEntry")

(ServObjDesc,
 TSapEgrQueueId,
 TSapIngQueueId,
 svcEpipeEntry,
 svcId,
 svcTlsInfoEntry) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "ServObjDesc",
    "TSapEgrQueueId",
    "TSapIngQueueId",
    "svcEpipeEntry",
    "svcId",
    "svcTlsInfoEntry")

(TBWRateType,
 TNamedItem,
 TNamedItemOrEmpty,
 TSapEgressPolicyID,
 TSapIngressPolicyID,
 TmnxActionType,
 TmnxCustId,
 TmnxEnabledDisabled) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TBWRateType",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TSapEgressPolicyID",
    "TSapIngressPolicyID",
    "TmnxActionType",
    "TmnxCustId",
    "TmnxEnabledDisabled")


# MODULE-IDENTITY

aluServiceMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    aluServiceMIBModule.setRevisions(
        ("1908-01-18 00:00",
         "1910-01-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AluSapSchedulerMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("four-priority", 1),
          ("sixteen-priority", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AluServiceMIBConformance_ObjectIdentity = ObjectIdentity
aluServiceMIBConformance = _AluServiceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6)
)
_AluServiceMIBCompliances_ObjectIdentity = ObjectIdentity
aluServiceMIBCompliances = _AluServiceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 1)
)
_AluServiceMIBGroups_ObjectIdentity = ObjectIdentity
aluServiceMIBGroups = _AluServiceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2)
)
_AluServiceObjs_ObjectIdentity = ObjectIdentity
aluServiceObjs = _AluServiceObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6)
)
_AeSapIpipeInfoTable_Object = MibTable
aeSapIpipeInfoTable = _AeSapIpipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1)
)
if mibBuilder.loadTexts:
    aeSapIpipeInfoTable.setStatus("current")
_AeSapIpipeInfoEntry_Object = MibTableRow
aeSapIpipeInfoEntry = _AeSapIpipeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    aeSapIpipeInfoEntry.setStatus("current")


class _AeSapIpipeIpcpAssignCeAddress_Type(TruthValue):
    """Custom type aeSapIpipeIpcpAssignCeAddress based on TruthValue"""
    defaultValue = 2


_AeSapIpipeIpcpAssignCeAddress_Type.__name__ = "TruthValue"
_AeSapIpipeIpcpAssignCeAddress_Object = MibTableColumn
aeSapIpipeIpcpAssignCeAddress = _AeSapIpipeIpcpAssignCeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1, 1, 1),
    _AeSapIpipeIpcpAssignCeAddress_Type()
)
aeSapIpipeIpcpAssignCeAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapIpipeIpcpAssignCeAddress.setStatus("current")


class _AeSapIpipeIpcpPriDnsAddrType_Type(InetAddressType):
    """Custom type aeSapIpipeIpcpPriDnsAddrType based on InetAddressType"""
    defaultValue = 0


_AeSapIpipeIpcpPriDnsAddrType_Type.__name__ = "InetAddressType"
_AeSapIpipeIpcpPriDnsAddrType_Object = MibTableColumn
aeSapIpipeIpcpPriDnsAddrType = _AeSapIpipeIpcpPriDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1, 1, 2),
    _AeSapIpipeIpcpPriDnsAddrType_Type()
)
aeSapIpipeIpcpPriDnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapIpipeIpcpPriDnsAddrType.setStatus("current")


class _AeSapIpipeIpcpPriDnsAddr_Type(InetAddress):
    """Custom type aeSapIpipeIpcpPriDnsAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AeSapIpipeIpcpPriDnsAddr_Type.__name__ = "InetAddress"
_AeSapIpipeIpcpPriDnsAddr_Object = MibTableColumn
aeSapIpipeIpcpPriDnsAddr = _AeSapIpipeIpcpPriDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1, 1, 3),
    _AeSapIpipeIpcpPriDnsAddr_Type()
)
aeSapIpipeIpcpPriDnsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapIpipeIpcpPriDnsAddr.setStatus("current")


class _AeSapIpipeIpcpSecDnsAddrType_Type(InetAddressType):
    """Custom type aeSapIpipeIpcpSecDnsAddrType based on InetAddressType"""
    defaultValue = 0


_AeSapIpipeIpcpSecDnsAddrType_Type.__name__ = "InetAddressType"
_AeSapIpipeIpcpSecDnsAddrType_Object = MibTableColumn
aeSapIpipeIpcpSecDnsAddrType = _AeSapIpipeIpcpSecDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1, 1, 4),
    _AeSapIpipeIpcpSecDnsAddrType_Type()
)
aeSapIpipeIpcpSecDnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapIpipeIpcpSecDnsAddrType.setStatus("current")


class _AeSapIpipeIpcpSecDnsAddr_Type(InetAddress):
    """Custom type aeSapIpipeIpcpSecDnsAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AeSapIpipeIpcpSecDnsAddr_Type.__name__ = "InetAddress"
_AeSapIpipeIpcpSecDnsAddr_Object = MibTableColumn
aeSapIpipeIpcpSecDnsAddr = _AeSapIpipeIpcpSecDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 1, 1, 5),
    _AeSapIpipeIpcpSecDnsAddr_Type()
)
aeSapIpipeIpcpSecDnsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapIpipeIpcpSecDnsAddr.setStatus("current")
_AeSapTlsInfoTable_Object = MibTable
aeSapTlsInfoTable = _AeSapTlsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 2)
)
if mibBuilder.loadTexts:
    aeSapTlsInfoTable.setStatus("current")
_AeSapTlsInfoEntry_Object = MibTableRow
aeSapTlsInfoEntry = _AeSapTlsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    aeSapTlsInfoEntry.setStatus("current")


class _AeSapTlsPPPoEIncludeCircuitId_Type(TruthValue):
    """Custom type aeSapTlsPPPoEIncludeCircuitId based on TruthValue"""
    defaultValue = 2


_AeSapTlsPPPoEIncludeCircuitId_Type.__name__ = "TruthValue"
_AeSapTlsPPPoEIncludeCircuitId_Object = MibTableColumn
aeSapTlsPPPoEIncludeCircuitId = _AeSapTlsPPPoEIncludeCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 2, 1, 1),
    _AeSapTlsPPPoEIncludeCircuitId_Type()
)
aeSapTlsPPPoEIncludeCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapTlsPPPoEIncludeCircuitId.setStatus("current")


class _AeSapTlsPPPoECircuitId_Type(DisplayString):
    """Custom type aeSapTlsPPPoECircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_AeSapTlsPPPoECircuitId_Type.__name__ = "DisplayString"
_AeSapTlsPPPoECircuitId_Object = MibTableColumn
aeSapTlsPPPoECircuitId = _AeSapTlsPPPoECircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 2, 1, 2),
    _AeSapTlsPPPoECircuitId_Type()
)
aeSapTlsPPPoECircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSapTlsPPPoECircuitId.setStatus("current")


class _AeSapTlsForceCVlanForwarding_Type(TruthValue):
    """Custom type aeSapTlsForceCVlanForwarding based on TruthValue"""
    defaultValue = 2


_AeSapTlsForceCVlanForwarding_Type.__name__ = "TruthValue"
_AeSapTlsForceCVlanForwarding_Object = MibTableColumn
aeSapTlsForceCVlanForwarding = _AeSapTlsForceCVlanForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 2, 1, 3),
    _AeSapTlsForceCVlanForwarding_Type()
)
aeSapTlsForceCVlanForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapTlsForceCVlanForwarding.setStatus("current")
_AeSapTlsAtmInfoTable_Object = MibTable
aeSapTlsAtmInfoTable = _AeSapTlsAtmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 3)
)
if mibBuilder.loadTexts:
    aeSapTlsAtmInfoTable.setStatus("current")
_AeSapTlsAtmInfoEntry_Object = MibTableRow
aeSapTlsAtmInfoEntry = _AeSapTlsAtmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    aeSapTlsAtmInfoEntry.setStatus("current")


class _AeSapTlsAtmSubscriberVlanTag_Type(Unsigned32):
    """Custom type aeSapTlsAtmSubscriberVlanTag based on Unsigned32"""
    defaultValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AeSapTlsAtmSubscriberVlanTag_Type.__name__ = "Unsigned32"
_AeSapTlsAtmSubscriberVlanTag_Object = MibTableColumn
aeSapTlsAtmSubscriberVlanTag = _AeSapTlsAtmSubscriberVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 3, 1, 1),
    _AeSapTlsAtmSubscriberVlanTag_Type()
)
aeSapTlsAtmSubscriberVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapTlsAtmSubscriberVlanTag.setStatus("current")
_AeSvcTlsInfoTable_Object = MibTable
aeSvcTlsInfoTable = _AeSvcTlsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 4)
)
if mibBuilder.loadTexts:
    aeSvcTlsInfoTable.setStatus("current")
_AeSvcTlsInfoEntry_Object = MibTableRow
aeSvcTlsInfoEntry = _AeSvcTlsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 4, 1)
)
if mibBuilder.loadTexts:
    aeSvcTlsInfoEntry.setStatus("current")


class _AeSvcTlsPPPoEIncludeCircuitId_Type(TruthValue):
    """Custom type aeSvcTlsPPPoEIncludeCircuitId based on TruthValue"""
    defaultValue = 2


_AeSvcTlsPPPoEIncludeCircuitId_Type.__name__ = "TruthValue"
_AeSvcTlsPPPoEIncludeCircuitId_Object = MibTableColumn
aeSvcTlsPPPoEIncludeCircuitId = _AeSvcTlsPPPoEIncludeCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 4, 1, 1),
    _AeSvcTlsPPPoEIncludeCircuitId_Type()
)
aeSvcTlsPPPoEIncludeCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcTlsPPPoEIncludeCircuitId.setStatus("current")


class _AeSvcTlsL4Hashing_Type(TmnxEnabledDisabled):
    """Custom type aeSvcTlsL4Hashing based on TmnxEnabledDisabled"""
    defaultValue = 2


_AeSvcTlsL4Hashing_Type.__name__ = "TmnxEnabledDisabled"
_AeSvcTlsL4Hashing_Object = MibTableColumn
aeSvcTlsL4Hashing = _AeSvcTlsL4Hashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 4, 1, 2),
    _AeSvcTlsL4Hashing_Type()
)
aeSvcTlsL4Hashing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcTlsL4Hashing.setStatus("current")
_AeSapApipeAtmInfoTable_Object = MibTable
aeSapApipeAtmInfoTable = _AeSapApipeAtmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 6)
)
if mibBuilder.loadTexts:
    aeSapApipeAtmInfoTable.setStatus("current")
_AeSapApipeAtmInfoEntry_Object = MibTableRow
aeSapApipeAtmInfoEntry = _AeSapApipeAtmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 6, 1)
)
if mibBuilder.loadTexts:
    aeSapApipeAtmInfoEntry.setStatus("current")


class _AeSapApipeAtmVcidTranslatedVpi_Type(AtmVpIdentifier):
    """Custom type aeSapApipeAtmVcidTranslatedVpi based on AtmVpIdentifier"""
    defaultValue = 0


_AeSapApipeAtmVcidTranslatedVpi_Type.__name__ = "AtmVpIdentifier"
_AeSapApipeAtmVcidTranslatedVpi_Object = MibTableColumn
aeSapApipeAtmVcidTranslatedVpi = _AeSapApipeAtmVcidTranslatedVpi_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 6, 1, 1),
    _AeSapApipeAtmVcidTranslatedVpi_Type()
)
aeSapApipeAtmVcidTranslatedVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapApipeAtmVcidTranslatedVpi.setStatus("current")


class _AeSapApipeAtmVcidTranslatedVci_Type(AtmVcIdentifier):
    """Custom type aeSapApipeAtmVcidTranslatedVci based on AtmVcIdentifier"""
    defaultValue = 0


_AeSapApipeAtmVcidTranslatedVci_Type.__name__ = "AtmVcIdentifier"
_AeSapApipeAtmVcidTranslatedVci_Object = MibTableColumn
aeSapApipeAtmVcidTranslatedVci = _AeSapApipeAtmVcidTranslatedVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 6, 1, 2),
    _AeSapApipeAtmVcidTranslatedVci_Type()
)
aeSapApipeAtmVcidTranslatedVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSapApipeAtmVcidTranslatedVci.setStatus("current")
_AeSvcSapAGInfoTable_Object = MibTable
aeSvcSapAGInfoTable = _AeSvcSapAGInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7)
)
if mibBuilder.loadTexts:
    aeSvcSapAGInfoTable.setStatus("current")
_AeSvcSapAGInfoEntry_Object = MibTableRow
aeSvcSapAGInfoEntry = _AeSvcSapAGInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1)
)
aeSvcSapAGInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-SERVICE-MIB", "aeSvcSapAGName"),
)
if mibBuilder.loadTexts:
    aeSvcSapAGInfoEntry.setStatus("current")
_AeSvcSapAGName_Type = TNamedItem
_AeSvcSapAGName_Object = MibTableColumn
aeSvcSapAGName = _AeSvcSapAGName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 1),
    _AeSvcSapAGName_Type()
)
aeSvcSapAGName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aeSvcSapAGName.setStatus("current")
_AeSvcSapAGRowStatus_Type = RowStatus
_AeSvcSapAGRowStatus_Object = MibTableColumn
aeSvcSapAGRowStatus = _AeSvcSapAGRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 2),
    _AeSvcSapAGRowStatus_Type()
)
aeSvcSapAGRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcSapAGRowStatus.setStatus("current")


class _AeSvcSapAGDescription_Type(ServObjDesc):
    """Custom type aeSvcSapAGDescription based on ServObjDesc"""
    defaultValue = OctetString("")


_AeSvcSapAGDescription_Type.__name__ = "ServObjDesc"
_AeSvcSapAGDescription_Object = MibTableColumn
aeSvcSapAGDescription = _AeSvcSapAGDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 3),
    _AeSvcSapAGDescription_Type()
)
aeSvcSapAGDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcSapAGDescription.setStatus("current")


class _AeSvcSapAGIngressQosPolicyId_Type(TSapIngressPolicyID):
    """Custom type aeSvcSapAGIngressQosPolicyId based on TSapIngressPolicyID"""
    defaultValue = 1


_AeSvcSapAGIngressQosPolicyId_Type.__name__ = "TSapIngressPolicyID"
_AeSvcSapAGIngressQosPolicyId_Object = MibTableColumn
aeSvcSapAGIngressQosPolicyId = _AeSvcSapAGIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 4),
    _AeSvcSapAGIngressQosPolicyId_Type()
)
aeSvcSapAGIngressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcSapAGIngressQosPolicyId.setStatus("current")


class _AeSvcSapAGEgressQosPolicyId_Type(TSapEgressPolicyID):
    """Custom type aeSvcSapAGEgressQosPolicyId based on TSapEgressPolicyID"""
    defaultValue = 1


_AeSvcSapAGEgressQosPolicyId_Type.__name__ = "TSapEgressPolicyID"
_AeSvcSapAGEgressQosPolicyId_Object = MibTableColumn
aeSvcSapAGEgressQosPolicyId = _AeSvcSapAGEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 5),
    _AeSvcSapAGEgressQosPolicyId_Type()
)
aeSvcSapAGEgressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcSapAGEgressQosPolicyId.setStatus("current")


class _AeSvcSapAGCollectAcctStats_Type(TruthValue):
    """Custom type aeSvcSapAGCollectAcctStats based on TruthValue"""
    defaultValue = 2


_AeSvcSapAGCollectAcctStats_Type.__name__ = "TruthValue"
_AeSvcSapAGCollectAcctStats_Object = MibTableColumn
aeSvcSapAGCollectAcctStats = _AeSvcSapAGCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 6),
    _AeSvcSapAGCollectAcctStats_Type()
)
aeSvcSapAGCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcSapAGCollectAcctStats.setStatus("current")


class _AeSvcSapAGAccountingPolicyId_Type(Unsigned32):
    """Custom type aeSvcSapAGAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_AeSvcSapAGAccountingPolicyId_Type.__name__ = "Unsigned32"
_AeSvcSapAGAccountingPolicyId_Object = MibTableColumn
aeSvcSapAGAccountingPolicyId = _AeSvcSapAGAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 7, 1, 7),
    _AeSvcSapAGAccountingPolicyId_Type()
)
aeSvcSapAGAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aeSvcSapAGAccountingPolicyId.setStatus("current")
_AluSapAGBaseStatsTable_Object = MibTable
aluSapAGBaseStatsTable = _AluSapAGBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8)
)
if mibBuilder.loadTexts:
    aluSapAGBaseStatsTable.setStatus("current")
_AluSapAGBaseStatsEntry_Object = MibTableRow
aluSapAGBaseStatsEntry = _AluSapAGBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1)
)
aluSapAGBaseStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-SERVICE-MIB", "aeSvcSapAGName"),
)
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEntry.setStatus("current")
_AluSapAGBaseStatsIngressDroppedPackets_Type = Counter64
_AluSapAGBaseStatsIngressDroppedPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressDroppedPackets = _AluSapAGBaseStatsIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 1),
    _AluSapAGBaseStatsIngressDroppedPackets_Type()
)
aluSapAGBaseStatsIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressDroppedPackets.setStatus("current")
_AluSapAGBaseStatsIngressDroppedOctets_Type = Counter64
_AluSapAGBaseStatsIngressDroppedOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressDroppedOctets = _AluSapAGBaseStatsIngressDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 2),
    _AluSapAGBaseStatsIngressDroppedOctets_Type()
)
aluSapAGBaseStatsIngressDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressDroppedOctets.setStatus("current")
_AluSapAGBaseStatsIngressOfferedHiPrioPackets_Type = Counter64
_AluSapAGBaseStatsIngressOfferedHiPrioPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressOfferedHiPrioPackets = _AluSapAGBaseStatsIngressOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 3),
    _AluSapAGBaseStatsIngressOfferedHiPrioPackets_Type()
)
aluSapAGBaseStatsIngressOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressOfferedHiPrioPackets.setStatus("current")
_AluSapAGBaseStatsIngressOfferedHiPrioOctets_Type = Counter64
_AluSapAGBaseStatsIngressOfferedHiPrioOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressOfferedHiPrioOctets = _AluSapAGBaseStatsIngressOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 4),
    _AluSapAGBaseStatsIngressOfferedHiPrioOctets_Type()
)
aluSapAGBaseStatsIngressOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressOfferedHiPrioOctets.setStatus("current")
_AluSapAGBaseStatsIngressOfferedLoPrioPackets_Type = Counter64
_AluSapAGBaseStatsIngressOfferedLoPrioPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressOfferedLoPrioPackets = _AluSapAGBaseStatsIngressOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 5),
    _AluSapAGBaseStatsIngressOfferedLoPrioPackets_Type()
)
aluSapAGBaseStatsIngressOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressOfferedLoPrioPackets.setStatus("current")
_AluSapAGBaseStatsIngressOfferedLoPrioOctets_Type = Counter64
_AluSapAGBaseStatsIngressOfferedLoPrioOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressOfferedLoPrioOctets = _AluSapAGBaseStatsIngressOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 6),
    _AluSapAGBaseStatsIngressOfferedLoPrioOctets_Type()
)
aluSapAGBaseStatsIngressOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressOfferedLoPrioOctets.setStatus("current")
_AluSapAGBaseStatsIngressDroppedHiPrioPackets_Type = Counter64
_AluSapAGBaseStatsIngressDroppedHiPrioPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressDroppedHiPrioPackets = _AluSapAGBaseStatsIngressDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 7),
    _AluSapAGBaseStatsIngressDroppedHiPrioPackets_Type()
)
aluSapAGBaseStatsIngressDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressDroppedHiPrioPackets.setStatus("current")
_AluSapAGBaseStatsIngressDroppedHiPrioOctets_Type = Counter64
_AluSapAGBaseStatsIngressDroppedHiPrioOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressDroppedHiPrioOctets = _AluSapAGBaseStatsIngressDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 8),
    _AluSapAGBaseStatsIngressDroppedHiPrioOctets_Type()
)
aluSapAGBaseStatsIngressDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressDroppedHiPrioOctets.setStatus("current")
_AluSapAGBaseStatsIngressDroppedLoPrioPackets_Type = Counter64
_AluSapAGBaseStatsIngressDroppedLoPrioPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressDroppedLoPrioPackets = _AluSapAGBaseStatsIngressDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 9),
    _AluSapAGBaseStatsIngressDroppedLoPrioPackets_Type()
)
aluSapAGBaseStatsIngressDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressDroppedLoPrioPackets.setStatus("current")
_AluSapAGBaseStatsIngressDroppedLoPrioOctets_Type = Counter64
_AluSapAGBaseStatsIngressDroppedLoPrioOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressDroppedLoPrioOctets = _AluSapAGBaseStatsIngressDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 10),
    _AluSapAGBaseStatsIngressDroppedLoPrioOctets_Type()
)
aluSapAGBaseStatsIngressDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressDroppedLoPrioOctets.setStatus("current")
_AluSapAGBaseStatsIngressForwardedInProfPackets_Type = Counter64
_AluSapAGBaseStatsIngressForwardedInProfPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressForwardedInProfPackets = _AluSapAGBaseStatsIngressForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 11),
    _AluSapAGBaseStatsIngressForwardedInProfPackets_Type()
)
aluSapAGBaseStatsIngressForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressForwardedInProfPackets.setStatus("current")
_AluSapAGBaseStatsIngressForwardedInProfOctets_Type = Counter64
_AluSapAGBaseStatsIngressForwardedInProfOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressForwardedInProfOctets = _AluSapAGBaseStatsIngressForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 12),
    _AluSapAGBaseStatsIngressForwardedInProfOctets_Type()
)
aluSapAGBaseStatsIngressForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressForwardedInProfOctets.setStatus("current")
_AluSapAGBaseStatsIngressForwardedOutProfPackets_Type = Counter64
_AluSapAGBaseStatsIngressForwardedOutProfPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressForwardedOutProfPackets = _AluSapAGBaseStatsIngressForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 13),
    _AluSapAGBaseStatsIngressForwardedOutProfPackets_Type()
)
aluSapAGBaseStatsIngressForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressForwardedOutProfPackets.setStatus("current")
_AluSapAGBaseStatsIngressForwardedOutProfOctets_Type = Counter64
_AluSapAGBaseStatsIngressForwardedOutProfOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressForwardedOutProfOctets = _AluSapAGBaseStatsIngressForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 14),
    _AluSapAGBaseStatsIngressForwardedOutProfOctets_Type()
)
aluSapAGBaseStatsIngressForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressForwardedOutProfOctets.setStatus("current")
_AluSapAGBaseStatsEgressDroppedInProfPackets_Type = Counter64
_AluSapAGBaseStatsEgressDroppedInProfPackets_Object = MibTableColumn
aluSapAGBaseStatsEgressDroppedInProfPackets = _AluSapAGBaseStatsEgressDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 15),
    _AluSapAGBaseStatsEgressDroppedInProfPackets_Type()
)
aluSapAGBaseStatsEgressDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressDroppedInProfPackets.setStatus("current")
_AluSapAGBaseStatsEgressDroppedInProfOctets_Type = Counter64
_AluSapAGBaseStatsEgressDroppedInProfOctets_Object = MibTableColumn
aluSapAGBaseStatsEgressDroppedInProfOctets = _AluSapAGBaseStatsEgressDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 16),
    _AluSapAGBaseStatsEgressDroppedInProfOctets_Type()
)
aluSapAGBaseStatsEgressDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressDroppedInProfOctets.setStatus("current")
_AluSapAGBaseStatsEgressDroppedOutProfPackets_Type = Counter64
_AluSapAGBaseStatsEgressDroppedOutProfPackets_Object = MibTableColumn
aluSapAGBaseStatsEgressDroppedOutProfPackets = _AluSapAGBaseStatsEgressDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 17),
    _AluSapAGBaseStatsEgressDroppedOutProfPackets_Type()
)
aluSapAGBaseStatsEgressDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressDroppedOutProfPackets.setStatus("current")
_AluSapAGBaseStatsEgressDroppedOutProfOctets_Type = Counter64
_AluSapAGBaseStatsEgressDroppedOutProfOctets_Object = MibTableColumn
aluSapAGBaseStatsEgressDroppedOutProfOctets = _AluSapAGBaseStatsEgressDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 18),
    _AluSapAGBaseStatsEgressDroppedOutProfOctets_Type()
)
aluSapAGBaseStatsEgressDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressDroppedOutProfOctets.setStatus("current")
_AluSapAGBaseStatsEgressForwardedInProfPackets_Type = Counter64
_AluSapAGBaseStatsEgressForwardedInProfPackets_Object = MibTableColumn
aluSapAGBaseStatsEgressForwardedInProfPackets = _AluSapAGBaseStatsEgressForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 19),
    _AluSapAGBaseStatsEgressForwardedInProfPackets_Type()
)
aluSapAGBaseStatsEgressForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressForwardedInProfPackets.setStatus("current")
_AluSapAGBaseStatsEgressForwardedInProfOctets_Type = Counter64
_AluSapAGBaseStatsEgressForwardedInProfOctets_Object = MibTableColumn
aluSapAGBaseStatsEgressForwardedInProfOctets = _AluSapAGBaseStatsEgressForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 20),
    _AluSapAGBaseStatsEgressForwardedInProfOctets_Type()
)
aluSapAGBaseStatsEgressForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressForwardedInProfOctets.setStatus("current")
_AluSapAGBaseStatsEgressForwardedOutProfPackets_Type = Counter64
_AluSapAGBaseStatsEgressForwardedOutProfPackets_Object = MibTableColumn
aluSapAGBaseStatsEgressForwardedOutProfPackets = _AluSapAGBaseStatsEgressForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 21),
    _AluSapAGBaseStatsEgressForwardedOutProfPackets_Type()
)
aluSapAGBaseStatsEgressForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressForwardedOutProfPackets.setStatus("current")
_AluSapAGBaseStatsEgressForwardedOutProfOctets_Type = Counter64
_AluSapAGBaseStatsEgressForwardedOutProfOctets_Object = MibTableColumn
aluSapAGBaseStatsEgressForwardedOutProfOctets = _AluSapAGBaseStatsEgressForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 22),
    _AluSapAGBaseStatsEgressForwardedOutProfOctets_Type()
)
aluSapAGBaseStatsEgressForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsEgressForwardedOutProfOctets.setStatus("current")
_AluSapAGBaseStatsUnknownVpiVciCellsDropped_Type = Counter64
_AluSapAGBaseStatsUnknownVpiVciCellsDropped_Object = MibTableColumn
aluSapAGBaseStatsUnknownVpiVciCellsDropped = _AluSapAGBaseStatsUnknownVpiVciCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 23),
    _AluSapAGBaseStatsUnknownVpiVciCellsDropped_Type()
)
aluSapAGBaseStatsUnknownVpiVciCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsUnknownVpiVciCellsDropped.setStatus("current")
_AluSapAGBaseStatsCustId_Type = TmnxCustId
_AluSapAGBaseStatsCustId_Object = MibTableColumn
aluSapAGBaseStatsCustId = _AluSapAGBaseStatsCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 24),
    _AluSapAGBaseStatsCustId_Type()
)
aluSapAGBaseStatsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsCustId.setStatus("current")
_AluSapAGBaseStatsIngressOfferedUncoloredPackets_Type = Counter64
_AluSapAGBaseStatsIngressOfferedUncoloredPackets_Object = MibTableColumn
aluSapAGBaseStatsIngressOfferedUncoloredPackets = _AluSapAGBaseStatsIngressOfferedUncoloredPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 25),
    _AluSapAGBaseStatsIngressOfferedUncoloredPackets_Type()
)
aluSapAGBaseStatsIngressOfferedUncoloredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressOfferedUncoloredPackets.setStatus("current")
_AluSapAGBaseStatsIngressOfferedUncoloredOctets_Type = Counter64
_AluSapAGBaseStatsIngressOfferedUncoloredOctets_Object = MibTableColumn
aluSapAGBaseStatsIngressOfferedUncoloredOctets = _AluSapAGBaseStatsIngressOfferedUncoloredOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 26),
    _AluSapAGBaseStatsIngressOfferedUncoloredOctets_Type()
)
aluSapAGBaseStatsIngressOfferedUncoloredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsIngressOfferedUncoloredOctets.setStatus("current")
_AluSapAGBaseStatsAuthenticationPktsDiscarded_Type = Counter32
_AluSapAGBaseStatsAuthenticationPktsDiscarded_Object = MibTableColumn
aluSapAGBaseStatsAuthenticationPktsDiscarded = _AluSapAGBaseStatsAuthenticationPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 27),
    _AluSapAGBaseStatsAuthenticationPktsDiscarded_Type()
)
aluSapAGBaseStatsAuthenticationPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsAuthenticationPktsDiscarded.setStatus("current")
_AluSapAGBaseStatsAuthenticationPktsSuccess_Type = Counter32
_AluSapAGBaseStatsAuthenticationPktsSuccess_Object = MibTableColumn
aluSapAGBaseStatsAuthenticationPktsSuccess = _AluSapAGBaseStatsAuthenticationPktsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 28),
    _AluSapAGBaseStatsAuthenticationPktsSuccess_Type()
)
aluSapAGBaseStatsAuthenticationPktsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsAuthenticationPktsSuccess.setStatus("current")
_AluSapAGBaseStatsLastClearedTime_Type = TimeStamp
_AluSapAGBaseStatsLastClearedTime_Object = MibTableColumn
aluSapAGBaseStatsLastClearedTime = _AluSapAGBaseStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 8, 1, 29),
    _AluSapAGBaseStatsLastClearedTime_Type()
)
aluSapAGBaseStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGBaseStatsLastClearedTime.setStatus("current")
_AluSapAGIngQosQStatsTable_Object = MibTable
aluSapAGIngQosQStatsTable = _AluSapAGIngQosQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9)
)
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsTable.setStatus("current")
_AluSapAGIngQosQStatsEntry_Object = MibTableRow
aluSapAGIngQosQStatsEntry = _AluSapAGIngQosQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1)
)
aluSapAGIngQosQStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-SERVICE-MIB", "aeSvcSapAGName"),
    (0, "ALU-SERVICE-MIB", "aluSapAGIngQosQueueId"),
)
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsEntry.setStatus("current")
_AluSapAGIngQosQueueId_Type = TSapIngQueueId
_AluSapAGIngQosQueueId_Object = MibTableColumn
aluSapAGIngQosQueueId = _AluSapAGIngQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 1),
    _AluSapAGIngQosQueueId_Type()
)
aluSapAGIngQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQueueId.setStatus("current")
_AluSapAGIngQosQStatsOfferedHiPrioPackets_Type = Counter64
_AluSapAGIngQosQStatsOfferedHiPrioPackets_Object = MibTableColumn
aluSapAGIngQosQStatsOfferedHiPrioPackets = _AluSapAGIngQosQStatsOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 2),
    _AluSapAGIngQosQStatsOfferedHiPrioPackets_Type()
)
aluSapAGIngQosQStatsOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsOfferedHiPrioPackets.setStatus("current")
_AluSapAGIngQosQStatsDroppedHiPrioPackets_Type = Counter64
_AluSapAGIngQosQStatsDroppedHiPrioPackets_Object = MibTableColumn
aluSapAGIngQosQStatsDroppedHiPrioPackets = _AluSapAGIngQosQStatsDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 3),
    _AluSapAGIngQosQStatsDroppedHiPrioPackets_Type()
)
aluSapAGIngQosQStatsDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsDroppedHiPrioPackets.setStatus("current")
_AluSapAGIngQosQStatsOfferedLoPrioPackets_Type = Counter64
_AluSapAGIngQosQStatsOfferedLoPrioPackets_Object = MibTableColumn
aluSapAGIngQosQStatsOfferedLoPrioPackets = _AluSapAGIngQosQStatsOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 4),
    _AluSapAGIngQosQStatsOfferedLoPrioPackets_Type()
)
aluSapAGIngQosQStatsOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsOfferedLoPrioPackets.setStatus("current")
_AluSapAGIngQosQStatsDroppedLoPrioPackets_Type = Counter64
_AluSapAGIngQosQStatsDroppedLoPrioPackets_Object = MibTableColumn
aluSapAGIngQosQStatsDroppedLoPrioPackets = _AluSapAGIngQosQStatsDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 5),
    _AluSapAGIngQosQStatsDroppedLoPrioPackets_Type()
)
aluSapAGIngQosQStatsDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsDroppedLoPrioPackets.setStatus("current")
_AluSapAGIngQosQStatsOfferedHiPrioOctets_Type = Counter64
_AluSapAGIngQosQStatsOfferedHiPrioOctets_Object = MibTableColumn
aluSapAGIngQosQStatsOfferedHiPrioOctets = _AluSapAGIngQosQStatsOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 6),
    _AluSapAGIngQosQStatsOfferedHiPrioOctets_Type()
)
aluSapAGIngQosQStatsOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsOfferedHiPrioOctets.setStatus("current")
_AluSapAGIngQosQStatsDroppedHiPrioOctets_Type = Counter64
_AluSapAGIngQosQStatsDroppedHiPrioOctets_Object = MibTableColumn
aluSapAGIngQosQStatsDroppedHiPrioOctets = _AluSapAGIngQosQStatsDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 7),
    _AluSapAGIngQosQStatsDroppedHiPrioOctets_Type()
)
aluSapAGIngQosQStatsDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsDroppedHiPrioOctets.setStatus("current")
_AluSapAGIngQosQStatsOfferedLoPrioOctets_Type = Counter64
_AluSapAGIngQosQStatsOfferedLoPrioOctets_Object = MibTableColumn
aluSapAGIngQosQStatsOfferedLoPrioOctets = _AluSapAGIngQosQStatsOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 8),
    _AluSapAGIngQosQStatsOfferedLoPrioOctets_Type()
)
aluSapAGIngQosQStatsOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsOfferedLoPrioOctets.setStatus("current")
_AluSapAGIngQosQStatsDroppedLoPrioOctets_Type = Counter64
_AluSapAGIngQosQStatsDroppedLoPrioOctets_Object = MibTableColumn
aluSapAGIngQosQStatsDroppedLoPrioOctets = _AluSapAGIngQosQStatsDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 9),
    _AluSapAGIngQosQStatsDroppedLoPrioOctets_Type()
)
aluSapAGIngQosQStatsDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsDroppedLoPrioOctets.setStatus("current")
_AluSapAGIngQosQStatsForwardedInProfPackets_Type = Counter64
_AluSapAGIngQosQStatsForwardedInProfPackets_Object = MibTableColumn
aluSapAGIngQosQStatsForwardedInProfPackets = _AluSapAGIngQosQStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 10),
    _AluSapAGIngQosQStatsForwardedInProfPackets_Type()
)
aluSapAGIngQosQStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsForwardedInProfPackets.setStatus("current")
_AluSapAGIngQosQStatsForwardedOutProfPackets_Type = Counter64
_AluSapAGIngQosQStatsForwardedOutProfPackets_Object = MibTableColumn
aluSapAGIngQosQStatsForwardedOutProfPackets = _AluSapAGIngQosQStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 11),
    _AluSapAGIngQosQStatsForwardedOutProfPackets_Type()
)
aluSapAGIngQosQStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsForwardedOutProfPackets.setStatus("current")
_AluSapAGIngQosQStatsForwardedInProfOctets_Type = Counter64
_AluSapAGIngQosQStatsForwardedInProfOctets_Object = MibTableColumn
aluSapAGIngQosQStatsForwardedInProfOctets = _AluSapAGIngQosQStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 12),
    _AluSapAGIngQosQStatsForwardedInProfOctets_Type()
)
aluSapAGIngQosQStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsForwardedInProfOctets.setStatus("current")
_AluSapAGIngQosQStatsForwardedOutProfOctets_Type = Counter64
_AluSapAGIngQosQStatsForwardedOutProfOctets_Object = MibTableColumn
aluSapAGIngQosQStatsForwardedOutProfOctets = _AluSapAGIngQosQStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 13),
    _AluSapAGIngQosQStatsForwardedOutProfOctets_Type()
)
aluSapAGIngQosQStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsForwardedOutProfOctets.setStatus("current")
_AluSapAGIngQosCustId_Type = TmnxCustId
_AluSapAGIngQosCustId_Object = MibTableColumn
aluSapAGIngQosCustId = _AluSapAGIngQosCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 14),
    _AluSapAGIngQosCustId_Type()
)
aluSapAGIngQosCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosCustId.setStatus("current")
_AluSapAGIngQosQStatsUncoloredPacketsOffered_Type = Counter64
_AluSapAGIngQosQStatsUncoloredPacketsOffered_Object = MibTableColumn
aluSapAGIngQosQStatsUncoloredPacketsOffered = _AluSapAGIngQosQStatsUncoloredPacketsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 15),
    _AluSapAGIngQosQStatsUncoloredPacketsOffered_Type()
)
aluSapAGIngQosQStatsUncoloredPacketsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsUncoloredPacketsOffered.setStatus("current")
_AluSapAGIngQosQStatsUncoloredOctetsOffered_Type = Counter64
_AluSapAGIngQosQStatsUncoloredOctetsOffered_Object = MibTableColumn
aluSapAGIngQosQStatsUncoloredOctetsOffered = _AluSapAGIngQosQStatsUncoloredOctetsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 9, 1, 16),
    _AluSapAGIngQosQStatsUncoloredOctetsOffered_Type()
)
aluSapAGIngQosQStatsUncoloredOctetsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsUncoloredOctetsOffered.setStatus("current")
_AluSapAGEgrQosQStatsTable_Object = MibTable
aluSapAGEgrQosQStatsTable = _AluSapAGEgrQosQStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10)
)
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsTable.setStatus("current")
_AluSapAGEgrQosQStatsEntry_Object = MibTableRow
aluSapAGEgrQosQStatsEntry = _AluSapAGEgrQosQStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1)
)
aluSapAGEgrQosQStatsEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "ALU-SERVICE-MIB", "aeSvcSapAGName"),
    (0, "ALU-SERVICE-MIB", "aluSapAGEgrQosQueueId"),
)
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsEntry.setStatus("current")
_AluSapAGEgrQosQueueId_Type = TSapEgrQueueId
_AluSapAGEgrQosQueueId_Object = MibTableColumn
aluSapAGEgrQosQueueId = _AluSapAGEgrQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 1),
    _AluSapAGEgrQosQueueId_Type()
)
aluSapAGEgrQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQueueId.setStatus("current")
_AluSapAGEgrQosQStatsForwardedInProfPackets_Type = Counter64
_AluSapAGEgrQosQStatsForwardedInProfPackets_Object = MibTableColumn
aluSapAGEgrQosQStatsForwardedInProfPackets = _AluSapAGEgrQosQStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 2),
    _AluSapAGEgrQosQStatsForwardedInProfPackets_Type()
)
aluSapAGEgrQosQStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsForwardedInProfPackets.setStatus("current")
_AluSapAGEgrQosQStatsDroppedInProfPackets_Type = Counter64
_AluSapAGEgrQosQStatsDroppedInProfPackets_Object = MibTableColumn
aluSapAGEgrQosQStatsDroppedInProfPackets = _AluSapAGEgrQosQStatsDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 3),
    _AluSapAGEgrQosQStatsDroppedInProfPackets_Type()
)
aluSapAGEgrQosQStatsDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsDroppedInProfPackets.setStatus("current")
_AluSapAGEgrQosQStatsForwardedOutProfPackets_Type = Counter64
_AluSapAGEgrQosQStatsForwardedOutProfPackets_Object = MibTableColumn
aluSapAGEgrQosQStatsForwardedOutProfPackets = _AluSapAGEgrQosQStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 4),
    _AluSapAGEgrQosQStatsForwardedOutProfPackets_Type()
)
aluSapAGEgrQosQStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsForwardedOutProfPackets.setStatus("current")
_AluSapAGEgrQosQStatsDroppedOutProfPackets_Type = Counter64
_AluSapAGEgrQosQStatsDroppedOutProfPackets_Object = MibTableColumn
aluSapAGEgrQosQStatsDroppedOutProfPackets = _AluSapAGEgrQosQStatsDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 5),
    _AluSapAGEgrQosQStatsDroppedOutProfPackets_Type()
)
aluSapAGEgrQosQStatsDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsDroppedOutProfPackets.setStatus("current")
_AluSapAGEgrQosQStatsForwardedInProfOctets_Type = Counter64
_AluSapAGEgrQosQStatsForwardedInProfOctets_Object = MibTableColumn
aluSapAGEgrQosQStatsForwardedInProfOctets = _AluSapAGEgrQosQStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 6),
    _AluSapAGEgrQosQStatsForwardedInProfOctets_Type()
)
aluSapAGEgrQosQStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsForwardedInProfOctets.setStatus("current")
_AluSapAGEgrQosQStatsDroppedInProfOctets_Type = Counter64
_AluSapAGEgrQosQStatsDroppedInProfOctets_Object = MibTableColumn
aluSapAGEgrQosQStatsDroppedInProfOctets = _AluSapAGEgrQosQStatsDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 7),
    _AluSapAGEgrQosQStatsDroppedInProfOctets_Type()
)
aluSapAGEgrQosQStatsDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsDroppedInProfOctets.setStatus("current")
_AluSapAGEgrQosQStatsForwardedOutProfOctets_Type = Counter64
_AluSapAGEgrQosQStatsForwardedOutProfOctets_Object = MibTableColumn
aluSapAGEgrQosQStatsForwardedOutProfOctets = _AluSapAGEgrQosQStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 8),
    _AluSapAGEgrQosQStatsForwardedOutProfOctets_Type()
)
aluSapAGEgrQosQStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsForwardedOutProfOctets.setStatus("current")
_AluSapAGEgrQosQStatsDroppedOutProfOctets_Type = Counter64
_AluSapAGEgrQosQStatsDroppedOutProfOctets_Object = MibTableColumn
aluSapAGEgrQosQStatsDroppedOutProfOctets = _AluSapAGEgrQosQStatsDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 9),
    _AluSapAGEgrQosQStatsDroppedOutProfOctets_Type()
)
aluSapAGEgrQosQStatsDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsDroppedOutProfOctets.setStatus("current")
_AluSapAGEgrQosCustId_Type = TmnxCustId
_AluSapAGEgrQosCustId_Object = MibTableColumn
aluSapAGEgrQosCustId = _AluSapAGEgrQosCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 10, 1, 10),
    _AluSapAGEgrQosCustId_Type()
)
aluSapAGEgrQosCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapAGEgrQosCustId.setStatus("current")
_AluSapEthCfmTable_Object = MibTable
aluSapEthCfmTable = _AluSapEthCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 11)
)
if mibBuilder.loadTexts:
    aluSapEthCfmTable.setStatus("current")
_AluSapEthCfmEntry_Object = MibTableRow
aluSapEthCfmEntry = _AluSapEthCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 11, 1)
)
if mibBuilder.loadTexts:
    aluSapEthCfmEntry.setStatus("current")


class _AluSapEthCfmHoldMepUp_Type(TruthValue):
    """Custom type aluSapEthCfmHoldMepUp based on TruthValue"""
    defaultValue = 2


_AluSapEthCfmHoldMepUp_Type.__name__ = "TruthValue"
_AluSapEthCfmHoldMepUp_Object = MibTableColumn
aluSapEthCfmHoldMepUp = _AluSapEthCfmHoldMepUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 11, 1, 1),
    _AluSapEthCfmHoldMepUp_Type()
)
aluSapEthCfmHoldMepUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEthCfmHoldMepUp.setStatus("current")
_AluSapEpipeInfoTable_Object = MibTable
aluSapEpipeInfoTable = _AluSapEpipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 12)
)
if mibBuilder.loadTexts:
    aluSapEpipeInfoTable.setStatus("current")
_AluSapEpipeInfoEntry_Object = MibTableRow
aluSapEpipeInfoEntry = _AluSapEpipeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 12, 1)
)
aluSapEpipeInfoEntry.setIndexNames(
    (0, "TIMETRA-SERV-MIB", "svcId"),
    (0, "TIMETRA-SAP-MIB", "sapPortId"),
    (0, "TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    aluSapEpipeInfoEntry.setStatus("current")


class _AluSapEpipeMwCompression_Type(TruthValue):
    """Custom type aluSapEpipeMwCompression based on TruthValue"""
    defaultValue = 2


_AluSapEpipeMwCompression_Type.__name__ = "TruthValue"
_AluSapEpipeMwCompression_Object = MibTableColumn
aluSapEpipeMwCompression = _AluSapEpipeMwCompression_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 12, 1, 1),
    _AluSapEpipeMwCompression_Type()
)
aluSapEpipeMwCompression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSapEpipeMwCompression.setStatus("current")


class _AluSapEpipeMwDestMacAddress_Type(MacAddress):
    """Custom type aluSapEpipeMwDestMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AluSapEpipeMwDestMacAddress_Type.__name__ = "MacAddress"
_AluSapEpipeMwDestMacAddress_Object = MibTableColumn
aluSapEpipeMwDestMacAddress = _AluSapEpipeMwDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 12, 1, 2),
    _AluSapEpipeMwDestMacAddress_Type()
)
aluSapEpipeMwDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSapEpipeMwDestMacAddress.setStatus("current")


class _AluSapEpipeMwSrcMacAddress_Type(MacAddress):
    """Custom type aluSapEpipeMwSrcMacAddress based on MacAddress"""
    defaultHexValue = "000000000000"


_AluSapEpipeMwSrcMacAddress_Type.__name__ = "MacAddress"
_AluSapEpipeMwSrcMacAddress_Object = MibTableColumn
aluSapEpipeMwSrcMacAddress = _AluSapEpipeMwSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 12, 1, 3),
    _AluSapEpipeMwSrcMacAddress_Type()
)
aluSapEpipeMwSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSapEpipeMwSrcMacAddress.setStatus("current")


class _AluSapEpipeMwCompressRTP_Type(TruthValue):
    """Custom type aluSapEpipeMwCompressRTP based on TruthValue"""
    defaultValue = 2


_AluSapEpipeMwCompressRTP_Type.__name__ = "TruthValue"
_AluSapEpipeMwCompressRTP_Object = MibTableColumn
aluSapEpipeMwCompressRTP = _AluSapEpipeMwCompressRTP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 12, 1, 4),
    _AluSapEpipeMwCompressRTP_Type()
)
aluSapEpipeMwCompressRTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluSapEpipeMwCompressRTP.setStatus("current")
_AluSapBaseInfoTable_Object = MibTable
aluSapBaseInfoTable = _AluSapBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13)
)
if mibBuilder.loadTexts:
    aluSapBaseInfoTable.setStatus("current")
_AluSapBaseInfoEntry_Object = MibTableRow
aluSapBaseInfoEntry = _AluSapBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1)
)
if mibBuilder.loadTexts:
    aluSapBaseInfoEntry.setStatus("current")


class _AluSapIngressSchedulerMode_Type(AluSapSchedulerMode):
    """Custom type aluSapIngressSchedulerMode based on AluSapSchedulerMode"""
    defaultValue = 1


_AluSapIngressSchedulerMode_Type.__name__ = "AluSapSchedulerMode"
_AluSapIngressSchedulerMode_Object = MibTableColumn
aluSapIngressSchedulerMode = _AluSapIngressSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 1),
    _AluSapIngressSchedulerMode_Type()
)
aluSapIngressSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressSchedulerMode.setStatus("current")


class _AluSapEgressSchedulerMode_Type(AluSapSchedulerMode):
    """Custom type aluSapEgressSchedulerMode based on AluSapSchedulerMode"""
    defaultValue = 1


_AluSapEgressSchedulerMode_Type.__name__ = "AluSapSchedulerMode"
_AluSapEgressSchedulerMode_Object = MibTableColumn
aluSapEgressSchedulerMode = _AluSapEgressSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 2),
    _AluSapEgressSchedulerMode_Type()
)
aluSapEgressSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressSchedulerMode.setStatus("current")


class _AluSapIngressAggCir_Type(AluSapSchedulerCir):
    """Custom type aluSapIngressAggCir based on AluSapSchedulerCir"""
    defaultValue = 0


_AluSapIngressAggCir_Type.__name__ = "AluSapSchedulerCir"
_AluSapIngressAggCir_Object = MibTableColumn
aluSapIngressAggCir = _AluSapIngressAggCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 3),
    _AluSapIngressAggCir_Type()
)
aluSapIngressAggCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressAggCir.setStatus("current")
if mibBuilder.loadTexts:
    aluSapIngressAggCir.setUnits("kbps")


class _AluSapEgressAggCir_Type(AluSapSchedulerCir):
    """Custom type aluSapEgressAggCir based on AluSapSchedulerCir"""
    defaultValue = 0


_AluSapEgressAggCir_Type.__name__ = "AluSapSchedulerCir"
_AluSapEgressAggCir_Object = MibTableColumn
aluSapEgressAggCir = _AluSapEgressAggCir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 4),
    _AluSapEgressAggCir_Type()
)
aluSapEgressAggCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressAggCir.setStatus("current")
if mibBuilder.loadTexts:
    aluSapEgressAggCir.setUnits("kbps")


class _AluSapIngressAggRateLimit_Type(Integer32):
    """Custom type aluSapIngressAggRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_AluSapIngressAggRateLimit_Type.__name__ = "Integer32"
_AluSapIngressAggRateLimit_Object = MibTableColumn
aluSapIngressAggRateLimit = _AluSapIngressAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 5),
    _AluSapIngressAggRateLimit_Type()
)
aluSapIngressAggRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    aluSapIngressAggRateLimit.setUnits("kbps")


class _AluSapEgressAggRateLimit_Type(Integer32):
    """Custom type aluSapEgressAggRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1, 10000000),
    )


_AluSapEgressAggRateLimit_Type.__name__ = "Integer32"
_AluSapEgressAggRateLimit_Object = MibTableColumn
aluSapEgressAggRateLimit = _AluSapEgressAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 6),
    _AluSapEgressAggRateLimit_Type()
)
aluSapEgressAggRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    aluSapEgressAggRateLimit.setUnits("kbps")


class _AluSapIngressShaperGroup_Type(TNamedItemOrEmpty):
    """Custom type aluSapIngressShaperGroup based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSapIngressShaperGroup_Type.__name__ = "TNamedItemOrEmpty"
_AluSapIngressShaperGroup_Object = MibTableColumn
aluSapIngressShaperGroup = _AluSapIngressShaperGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 7),
    _AluSapIngressShaperGroup_Type()
)
aluSapIngressShaperGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressShaperGroup.setStatus("current")


class _AluSapEgressShaperGroup_Type(TNamedItemOrEmpty):
    """Custom type aluSapEgressShaperGroup based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_AluSapEgressShaperGroup_Type.__name__ = "TNamedItemOrEmpty"
_AluSapEgressShaperGroup_Object = MibTableColumn
aluSapEgressShaperGroup = _AluSapEgressShaperGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 8),
    _AluSapEgressShaperGroup_Type()
)
aluSapEgressShaperGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressShaperGroup.setStatus("current")


class _AluSapIngressAggCirPercent_Type(Unsigned32):
    """Custom type aluSapIngressAggCirPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AluSapIngressAggCirPercent_Type.__name__ = "Unsigned32"
_AluSapIngressAggCirPercent_Object = MibTableColumn
aluSapIngressAggCirPercent = _AluSapIngressAggCirPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 9),
    _AluSapIngressAggCirPercent_Type()
)
aluSapIngressAggCirPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressAggCirPercent.setStatus("current")
if mibBuilder.loadTexts:
    aluSapIngressAggCirPercent.setUnits("hundredths of a percent")


class _AluSapEgressAggCirPercent_Type(Unsigned32):
    """Custom type aluSapEgressAggCirPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AluSapEgressAggCirPercent_Type.__name__ = "Unsigned32"
_AluSapEgressAggCirPercent_Object = MibTableColumn
aluSapEgressAggCirPercent = _AluSapEgressAggCirPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 10),
    _AluSapEgressAggCirPercent_Type()
)
aluSapEgressAggCirPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressAggCirPercent.setStatus("current")
if mibBuilder.loadTexts:
    aluSapEgressAggCirPercent.setUnits("hundredths of a percent")


class _AluSapIngressAggRatePercent_Type(Unsigned32):
    """Custom type aluSapIngressAggRatePercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AluSapIngressAggRatePercent_Type.__name__ = "Unsigned32"
_AluSapIngressAggRatePercent_Object = MibTableColumn
aluSapIngressAggRatePercent = _AluSapIngressAggRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 11),
    _AluSapIngressAggRatePercent_Type()
)
aluSapIngressAggRatePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressAggRatePercent.setStatus("current")
if mibBuilder.loadTexts:
    aluSapIngressAggRatePercent.setUnits("hundredths of a percent")


class _AluSapEgressAggRatePercent_Type(Unsigned32):
    """Custom type aluSapEgressAggRatePercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AluSapEgressAggRatePercent_Type.__name__ = "Unsigned32"
_AluSapEgressAggRatePercent_Object = MibTableColumn
aluSapEgressAggRatePercent = _AluSapEgressAggRatePercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 12),
    _AluSapEgressAggRatePercent_Type()
)
aluSapEgressAggRatePercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressAggRatePercent.setStatus("current")
if mibBuilder.loadTexts:
    aluSapEgressAggRatePercent.setUnits("hundredths of a percent")


class _AluSapIngressAggRateType_Type(TBWRateType):
    """Custom type aluSapIngressAggRateType based on TBWRateType"""
    defaultValue = 1


_AluSapIngressAggRateType_Type.__name__ = "TBWRateType"
_AluSapIngressAggRateType_Object = MibTableColumn
aluSapIngressAggRateType = _AluSapIngressAggRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 13),
    _AluSapIngressAggRateType_Type()
)
aluSapIngressAggRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapIngressAggRateType.setStatus("current")


class _AluSapEgressAggRateType_Type(TBWRateType):
    """Custom type aluSapEgressAggRateType based on TBWRateType"""
    defaultValue = 1


_AluSapEgressAggRateType_Type.__name__ = "TBWRateType"
_AluSapEgressAggRateType_Object = MibTableColumn
aluSapEgressAggRateType = _AluSapEgressAggRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 13, 1, 14),
    _AluSapEgressAggRateType_Type()
)
aluSapEgressAggRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEgressAggRateType.setStatus("current")
_AluSapEthLoopbackTable_Object = MibTable
aluSapEthLoopbackTable = _AluSapEthLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14)
)
if mibBuilder.loadTexts:
    aluSapEthLoopbackTable.setStatus("current")
_AluSapEthLoopbackEntry_Object = MibTableRow
aluSapEthLoopbackEntry = _AluSapEthLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1)
)
if mibBuilder.loadTexts:
    aluSapEthLoopbackEntry.setStatus("current")


class _AluSapEthLoopback_Type(Integer32):
    """Custom type aluSapEthLoopback based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AluSapEthLoopback_Type.__name__ = "Integer32"
_AluSapEthLoopback_Object = MibTableColumn
aluSapEthLoopback = _AluSapEthLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1, 1),
    _AluSapEthLoopback_Type()
)
aluSapEthLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEthLoopback.setStatus("current")


class _AluSapEthLoopbackDuration_Type(Unsigned32):
    """Custom type aluSapEthLoopbackDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 86400),
    )


_AluSapEthLoopbackDuration_Type.__name__ = "Unsigned32"
_AluSapEthLoopbackDuration_Object = MibTableColumn
aluSapEthLoopbackDuration = _AluSapEthLoopbackDuration_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1, 2),
    _AluSapEthLoopbackDuration_Type()
)
aluSapEthLoopbackDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEthLoopbackDuration.setStatus("current")


class _AluSapEthLoopbackPersistent_Type(Integer32):
    """Custom type aluSapEthLoopbackPersistent based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AluSapEthLoopbackPersistent_Type.__name__ = "Integer32"
_AluSapEthLoopbackPersistent_Object = MibTableColumn
aluSapEthLoopbackPersistent = _AluSapEthLoopbackPersistent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1, 3),
    _AluSapEthLoopbackPersistent_Type()
)
aluSapEthLoopbackPersistent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEthLoopbackPersistent.setStatus("current")


class _AluSapEthLoopbackTimeLeft_Type(Unsigned32):
    """Custom type aluSapEthLoopbackTimeLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AluSapEthLoopbackTimeLeft_Type.__name__ = "Unsigned32"
_AluSapEthLoopbackTimeLeft_Object = MibTableColumn
aluSapEthLoopbackTimeLeft = _AluSapEthLoopbackTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1, 4),
    _AluSapEthLoopbackTimeLeft_Type()
)
aluSapEthLoopbackTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapEthLoopbackTimeLeft.setStatus("current")


class _AluSapEthLoopbackMode_Type(Integer32):
    """Custom type aluSapEthLoopbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("internal", 2))
    )


_AluSapEthLoopbackMode_Type.__name__ = "Integer32"
_AluSapEthLoopbackMode_Object = MibTableColumn
aluSapEthLoopbackMode = _AluSapEthLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1, 5),
    _AluSapEthLoopbackMode_Type()
)
aluSapEthLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEthLoopbackMode.setStatus("current")


class _AluSapEthLoopbackMacSwap_Type(TmnxEnabledDisabled):
    """Custom type aluSapEthLoopbackMacSwap based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluSapEthLoopbackMacSwap_Type.__name__ = "TmnxEnabledDisabled"
_AluSapEthLoopbackMacSwap_Object = MibTableColumn
aluSapEthLoopbackMacSwap = _AluSapEthLoopbackMacSwap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 14, 1, 6),
    _AluSapEthLoopbackMacSwap_Type()
)
aluSapEthLoopbackMacSwap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapEthLoopbackMacSwap.setStatus("current")
_AluSapCemInfoTable_Object = MibTable
aluSapCemInfoTable = _AluSapCemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15)
)
if mibBuilder.loadTexts:
    aluSapCemInfoTable.setStatus("current")
_AluSapCemInfoEntry_Object = MibTableRow
aluSapCemInfoEntry = _AluSapCemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15, 1)
)
if mibBuilder.loadTexts:
    aluSapCemInfoEntry.setStatus("current")


class _AluSapCemAsymDelayEnable_Type(TmnxEnabledDisabled):
    """Custom type aluSapCemAsymDelayEnable based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluSapCemAsymDelayEnable_Type.__name__ = "TmnxEnabledDisabled"
_AluSapCemAsymDelayEnable_Object = MibTableColumn
aluSapCemAsymDelayEnable = _AluSapCemAsymDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15, 1, 1),
    _AluSapCemAsymDelayEnable_Type()
)
aluSapCemAsymDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapCemAsymDelayEnable.setStatus("current")


class _AluSapCemAsymDelaySamples_Type(Integer32):
    """Custom type aluSapCemAsymDelaySamples based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2),
          ("four", 4),
          ("eight", 8),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AluSapCemAsymDelaySamples_Type.__name__ = "Integer32"
_AluSapCemAsymDelaySamples_Object = MibTableColumn
aluSapCemAsymDelaySamples = _AluSapCemAsymDelaySamples_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15, 1, 2),
    _AluSapCemAsymDelaySamples_Type()
)
aluSapCemAsymDelaySamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapCemAsymDelaySamples.setStatus("current")


class _AluSapCemAsymDelayRepeatPeriod_Type(Integer32):
    """Custom type aluSapCemAsymDelayRepeatPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1440),
    )


_AluSapCemAsymDelayRepeatPeriod_Type.__name__ = "Integer32"
_AluSapCemAsymDelayRepeatPeriod_Object = MibTableColumn
aluSapCemAsymDelayRepeatPeriod = _AluSapCemAsymDelayRepeatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15, 1, 3),
    _AluSapCemAsymDelayRepeatPeriod_Type()
)
aluSapCemAsymDelayRepeatPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapCemAsymDelayRepeatPeriod.setStatus("current")
_AluSapCemSerialRate_Type = Unsigned32
_AluSapCemSerialRate_Object = MibTableColumn
aluSapCemSerialRate = _AluSapCemSerialRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15, 1, 4),
    _AluSapCemSerialRate_Type()
)
aluSapCemSerialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapCemSerialRate.setStatus("current")
if mibBuilder.loadTexts:
    aluSapCemSerialRate.setUnits("bits/s")


class _AluSapCemOnDemandADC_Type(TmnxActionType):
    """Custom type aluSapCemOnDemandADC based on TmnxActionType"""
    defaultValue = 2


_AluSapCemOnDemandADC_Type.__name__ = "TmnxActionType"
_AluSapCemOnDemandADC_Object = MibTableColumn
aluSapCemOnDemandADC = _AluSapCemOnDemandADC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 15, 1, 5),
    _AluSapCemOnDemandADC_Type()
)
aluSapCemOnDemandADC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSapCemOnDemandADC.setStatus("current")
_AluSapCemStatsTable_Object = MibTable
aluSapCemStatsTable = _AluSapCemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 16)
)
if mibBuilder.loadTexts:
    aluSapCemStatsTable.setStatus("current")
_AluSapCemStatsEntry_Object = MibTableRow
aluSapCemStatsEntry = _AluSapCemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 16, 1)
)
if mibBuilder.loadTexts:
    aluSapCemStatsEntry.setStatus("current")
_AluSapCemStatsEgressSamplingDoneCnt_Type = Counter32
_AluSapCemStatsEgressSamplingDoneCnt_Object = MibTableColumn
aluSapCemStatsEgressSamplingDoneCnt = _AluSapCemStatsEgressSamplingDoneCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 16, 1, 1),
    _AluSapCemStatsEgressSamplingDoneCnt_Type()
)
aluSapCemStatsEgressSamplingDoneCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapCemStatsEgressSamplingDoneCnt.setStatus("current")
_AluSapCemStatsEgressAdjustDoneCnt_Type = Counter32
_AluSapCemStatsEgressAdjustDoneCnt_Object = MibTableColumn
aluSapCemStatsEgressAdjustDoneCnt = _AluSapCemStatsEgressAdjustDoneCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 16, 1, 2),
    _AluSapCemStatsEgressAdjustDoneCnt_Type()
)
aluSapCemStatsEgressAdjustDoneCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSapCemStatsEgressAdjustDoneCnt.setStatus("current")
_AluSdpBindStatsTable_Object = MibTable
aluSdpBindStatsTable = _AluSdpBindStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 17)
)
if mibBuilder.loadTexts:
    aluSdpBindStatsTable.setStatus("current")
_AluSdpBindStatsEntry_Object = MibTableRow
aluSdpBindStatsEntry = _AluSdpBindStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 17, 1)
)
if mibBuilder.loadTexts:
    aluSdpBindStatsEntry.setStatus("current")
_AluSdpBindBaseStatsEgressDroppedPackets_Type = Counter64
_AluSdpBindBaseStatsEgressDroppedPackets_Object = MibTableColumn
aluSdpBindBaseStatsEgressDroppedPackets = _AluSdpBindBaseStatsEgressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 17, 1, 1),
    _AluSdpBindBaseStatsEgressDroppedPackets_Type()
)
aluSdpBindBaseStatsEgressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluSdpBindBaseStatsEgressDroppedPackets.setStatus("current")
_AluSvcEpipeTable_Object = MibTable
aluSvcEpipeTable = _AluSvcEpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 18)
)
if mibBuilder.loadTexts:
    aluSvcEpipeTable.setStatus("current")
_AluSvcEpipeEntry_Object = MibTableRow
aluSvcEpipeEntry = _AluSvcEpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 18, 1)
)
if mibBuilder.loadTexts:
    aluSvcEpipeEntry.setStatus("current")


class _AluSvcEpipeTeidHashing_Type(TmnxEnabledDisabled):
    """Custom type aluSvcEpipeTeidHashing based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluSvcEpipeTeidHashing_Type.__name__ = "TmnxEnabledDisabled"
_AluSvcEpipeTeidHashing_Object = MibTableColumn
aluSvcEpipeTeidHashing = _AluSvcEpipeTeidHashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 18, 1, 1),
    _AluSvcEpipeTeidHashing_Type()
)
aluSvcEpipeTeidHashing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSvcEpipeTeidHashing.setStatus("current")


class _AluSvcEpipeL4Hashing_Type(TmnxEnabledDisabled):
    """Custom type aluSvcEpipeL4Hashing based on TmnxEnabledDisabled"""
    defaultValue = 2


_AluSvcEpipeL4Hashing_Type.__name__ = "TmnxEnabledDisabled"
_AluSvcEpipeL4Hashing_Object = MibTableColumn
aluSvcEpipeL4Hashing = _AluSvcEpipeL4Hashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 18, 1, 2),
    _AluSvcEpipeL4Hashing_Type()
)
aluSvcEpipeL4Hashing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluSvcEpipeL4Hashing.setStatus("current")
_AeSdpBindCpipeTable_Object = MibTable
aeSdpBindCpipeTable = _AeSdpBindCpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19)
)
if mibBuilder.loadTexts:
    aeSdpBindCpipeTable.setStatus("current")
_AeSdpBindCpipeEntry_Object = MibTableRow
aeSdpBindCpipeEntry = _AeSdpBindCpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1)
)
if mibBuilder.loadTexts:
    aeSdpBindCpipeEntry.setStatus("current")
_AeSdpBindCpipeLocalAsymDelay_Type = TmnxEnabledDisabled
_AeSdpBindCpipeLocalAsymDelay_Object = MibTableColumn
aeSdpBindCpipeLocalAsymDelay = _AeSdpBindCpipeLocalAsymDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1, 1),
    _AeSdpBindCpipeLocalAsymDelay_Type()
)
aeSdpBindCpipeLocalAsymDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSdpBindCpipeLocalAsymDelay.setStatus("current")
_AeSdpBindCpipePeerAsymDelay_Type = TmnxEnabledDisabled
_AeSdpBindCpipePeerAsymDelay_Object = MibTableColumn
aeSdpBindCpipePeerAsymDelay = _AeSdpBindCpipePeerAsymDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1, 2),
    _AeSdpBindCpipePeerAsymDelay_Type()
)
aeSdpBindCpipePeerAsymDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSdpBindCpipePeerAsymDelay.setStatus("current")
_AeSdpBindCpipeLocalJitterBuffer_Type = Unsigned32
_AeSdpBindCpipeLocalJitterBuffer_Object = MibTableColumn
aeSdpBindCpipeLocalJitterBuffer = _AeSdpBindCpipeLocalJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1, 3),
    _AeSdpBindCpipeLocalJitterBuffer_Type()
)
aeSdpBindCpipeLocalJitterBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSdpBindCpipeLocalJitterBuffer.setStatus("current")
if mibBuilder.loadTexts:
    aeSdpBindCpipeLocalJitterBuffer.setUnits("milliseconds")
_AeSdpBindCpipePeerJitterBuffer_Type = Unsigned32
_AeSdpBindCpipePeerJitterBuffer_Object = MibTableColumn
aeSdpBindCpipePeerJitterBuffer = _AeSdpBindCpipePeerJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1, 4),
    _AeSdpBindCpipePeerJitterBuffer_Type()
)
aeSdpBindCpipePeerJitterBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSdpBindCpipePeerJitterBuffer.setStatus("current")
if mibBuilder.loadTexts:
    aeSdpBindCpipePeerJitterBuffer.setUnits("milliseconds")
_AeSdpBindCpipeLocalSerialRate_Type = Unsigned32
_AeSdpBindCpipeLocalSerialRate_Object = MibTableColumn
aeSdpBindCpipeLocalSerialRate = _AeSdpBindCpipeLocalSerialRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1, 5),
    _AeSdpBindCpipeLocalSerialRate_Type()
)
aeSdpBindCpipeLocalSerialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSdpBindCpipeLocalSerialRate.setStatus("current")
if mibBuilder.loadTexts:
    aeSdpBindCpipeLocalSerialRate.setUnits("bits/s")
_AeSdpBindCpipePeerSerialRate_Type = Unsigned32
_AeSdpBindCpipePeerSerialRate_Object = MibTableColumn
aeSdpBindCpipePeerSerialRate = _AeSdpBindCpipePeerSerialRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 19, 1, 6),
    _AeSdpBindCpipePeerSerialRate_Type()
)
aeSdpBindCpipePeerSerialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aeSdpBindCpipePeerSerialRate.setStatus("current")
if mibBuilder.loadTexts:
    aeSdpBindCpipePeerSerialRate.setUnits("bits/s")
_AluExtSapBaseStatsTable_Object = MibTable
aluExtSapBaseStatsTable = _AluExtSapBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 20)
)
if mibBuilder.loadTexts:
    aluExtSapBaseStatsTable.setStatus("current")
_AluExtSapBaseStatsEntry_Object = MibTableRow
aluExtSapBaseStatsEntry = _AluExtSapBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 20, 1)
)
if mibBuilder.loadTexts:
    aluExtSapBaseStatsEntry.setStatus("current")
_AluExtSapBaseStatsEgressDroppedPackets_Type = Counter64
_AluExtSapBaseStatsEgressDroppedPackets_Object = MibTableColumn
aluExtSapBaseStatsEgressDroppedPackets = _AluExtSapBaseStatsEgressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 20, 1, 1),
    _AluExtSapBaseStatsEgressDroppedPackets_Type()
)
aluExtSapBaseStatsEgressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtSapBaseStatsEgressDroppedPackets.setStatus("current")
_AluExtSapEthCfmTable_Object = MibTable
aluExtSapEthCfmTable = _AluExtSapEthCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 21)
)
if mibBuilder.loadTexts:
    aluExtSapEthCfmTable.setStatus("current")
_AluExtSapEthCfmEntry_Object = MibTableRow
aluExtSapEthCfmEntry = _AluExtSapEthCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 21, 1)
)
if mibBuilder.loadTexts:
    aluExtSapEthCfmEntry.setStatus("current")


class _AluExtSapEthCfmHoldMepUp_Type(TruthValue):
    """Custom type aluExtSapEthCfmHoldMepUp based on TruthValue"""
    defaultValue = 2


_AluExtSapEthCfmHoldMepUp_Type.__name__ = "TruthValue"
_AluExtSapEthCfmHoldMepUp_Object = MibTableColumn
aluExtSapEthCfmHoldMepUp = _AluExtSapEthCfmHoldMepUp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 6, 21, 1, 1),
    _AluExtSapEthCfmHoldMepUp_Type()
)
aluExtSapEthCfmHoldMepUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aluExtSapEthCfmHoldMepUp.setStatus("current")
sapIpipeInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aeSapIpipeInfoEntry")
)
aeSapIpipeInfoEntry.setIndexNames(*sapIpipeInfoEntry.getIndexNames())
sapTlsInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aeSapTlsInfoEntry")
)
aeSapTlsInfoEntry.setIndexNames(*sapTlsInfoEntry.getIndexNames())
sapAtmInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aeSapTlsAtmInfoEntry")
)
aeSapTlsAtmInfoEntry.setIndexNames(*sapAtmInfoEntry.getIndexNames())
svcTlsInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aeSvcTlsInfoEntry")
)
aeSvcTlsInfoEntry.setIndexNames(*svcTlsInfoEntry.getIndexNames())
sapAtmInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aeSapApipeAtmInfoEntry")
)
aeSapApipeAtmInfoEntry.setIndexNames(*sapAtmInfoEntry.getIndexNames())
sapEthernetInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSapEthCfmEntry")
)
aluSapEthCfmEntry.setIndexNames(*sapEthernetInfoEntry.getIndexNames())
sapBaseInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSapBaseInfoEntry")
)
aluSapBaseInfoEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sapEthLoopbackEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSapEthLoopbackEntry")
)
aluSapEthLoopbackEntry.setIndexNames(*sapEthLoopbackEntry.getIndexNames())
sapCemInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSapCemInfoEntry")
)
aluSapCemInfoEntry.setIndexNames(*sapCemInfoEntry.getIndexNames())
sapCemStatsEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSapCemStatsEntry")
)
aluSapCemStatsEntry.setIndexNames(*sapCemStatsEntry.getIndexNames())
sdpBindBaseStatsEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSdpBindStatsEntry")
)
aluSdpBindStatsEntry.setIndexNames(*sdpBindBaseStatsEntry.getIndexNames())
svcEpipeEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluSvcEpipeEntry")
)
aluSvcEpipeEntry.setIndexNames(*svcEpipeEntry.getIndexNames())
sdpBindCpipeEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aeSdpBindCpipeEntry")
)
aeSdpBindCpipeEntry.setIndexNames(*sdpBindCpipeEntry.getIndexNames())
sapBaseInfoEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluExtSapBaseStatsEntry")
)
aluExtSapBaseStatsEntry.setIndexNames(*sapBaseInfoEntry.getIndexNames())
sapEthCfmEntry.registerAugmentions(
    ("ALU-SERVICE-MIB",
     "aluExtSapEthCfmEntry")
)
aluExtSapEthCfmEntry.setIndexNames(*sapEthCfmEntry.getIndexNames())

# Managed Objects groups

aluExtSapIpipeIpcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 1)
)
aluExtSapIpipeIpcpGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSapIpipeIpcpAssignCeAddress"),
        ("ALU-SERVICE-MIB", "aeSapIpipeIpcpPriDnsAddrType"),
        ("ALU-SERVICE-MIB", "aeSapIpipeIpcpPriDnsAddr"),
        ("ALU-SERVICE-MIB", "aeSapIpipeIpcpSecDnsAddrType"),
        ("ALU-SERVICE-MIB", "aeSapIpipeIpcpSecDnsAddr"))
)
if mibBuilder.loadTexts:
    aluExtSapIpipeIpcpGroup.setStatus("current")

aluExtSapTlsPPPoEVsaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 2)
)
aluExtSapTlsPPPoEVsaGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSapTlsPPPoEIncludeCircuitId"),
        ("ALU-SERVICE-MIB", "aeSapTlsPPPoECircuitId"),
        ("ALU-SERVICE-MIB", "aeSvcTlsPPPoEIncludeCircuitId"))
)
if mibBuilder.loadTexts:
    aluExtSapTlsPPPoEVsaGroup.setStatus("current")

aluExtSapTlsVlanManipulationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 3)
)
aluExtSapTlsVlanManipulationGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSapTlsAtmSubscriberVlanTag"),
        ("ALU-SERVICE-MIB", "aeSapTlsForceCVlanForwarding"))
)
if mibBuilder.loadTexts:
    aluExtSapTlsVlanManipulationGroup.setStatus("current")

aluExtSapAtmTranslatedVcIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 4)
)
aluExtSapAtmTranslatedVcIdGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSapApipeAtmVcidTranslatedVpi"),
        ("ALU-SERVICE-MIB", "aeSapApipeAtmVcidTranslatedVci"))
)
if mibBuilder.loadTexts:
    aluExtSapAtmTranslatedVcIdGroup.setStatus("current")

aluExtSapAGBaseInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 5)
)
aluExtSapAGBaseInfoGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSvcSapAGRowStatus"),
        ("ALU-SERVICE-MIB", "aeSvcSapAGDescription"),
        ("ALU-SERVICE-MIB", "aeSvcSapAGIngressQosPolicyId"),
        ("ALU-SERVICE-MIB", "aeSvcSapAGEgressQosPolicyId"),
        ("ALU-SERVICE-MIB", "aeSvcSapAGCollectAcctStats"),
        ("ALU-SERVICE-MIB", "aeSvcSapAGAccountingPolicyId"))
)
if mibBuilder.loadTexts:
    aluExtSapAGBaseInfoGroup.setStatus("current")

aluSapAGBaseStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 6)
)
aluSapAGBaseStatsGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressDroppedPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressDroppedOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressOfferedHiPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressOfferedHiPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressOfferedLoPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressOfferedLoPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressDroppedHiPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressDroppedHiPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressDroppedLoPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressDroppedLoPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressForwardedInProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressForwardedInProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressForwardedOutProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressForwardedOutProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressDroppedInProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressDroppedInProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressDroppedOutProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressDroppedOutProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressForwardedInProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressForwardedInProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressForwardedOutProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsEgressForwardedOutProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsUnknownVpiVciCellsDropped"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsCustId"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressOfferedUncoloredPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsIngressOfferedUncoloredOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsAuthenticationPktsDiscarded"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsAuthenticationPktsSuccess"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsLastClearedTime"))
)
if mibBuilder.loadTexts:
    aluSapAGBaseStatsGroup.setStatus("current")

aluSapAGIngQosQStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 7)
)
aluSapAGIngQosQStatsGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapAGIngQosQueueId"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsOfferedHiPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsDroppedHiPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsOfferedLoPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsDroppedLoPrioPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsOfferedHiPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsDroppedHiPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsOfferedLoPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsDroppedLoPrioOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsForwardedInProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsForwardedOutProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsForwardedInProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsForwardedOutProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosCustId"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsUncoloredPacketsOffered"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsUncoloredOctetsOffered"))
)
if mibBuilder.loadTexts:
    aluSapAGIngQosQStatsGroup.setStatus("current")

aluSapAGEgrQosQStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 8)
)
aluSapAGEgrQosQStatsGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapAGEgrQosQueueId"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsForwardedInProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsDroppedInProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsForwardedOutProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsDroppedOutProfPackets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsForwardedInProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsDroppedInProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsForwardedOutProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsDroppedOutProfOctets"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosCustId"))
)
if mibBuilder.loadTexts:
    aluSapAGEgrQosQStatsGroup.setStatus("current")

aluSapEthCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 9)
)
aluSapEthCfmGroup.setObjects(
    ("ALU-SERVICE-MIB", "aluSapEthCfmHoldMepUp")
)
if mibBuilder.loadTexts:
    aluSapEthCfmGroup.setStatus("current")

aluSapEpipeMwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 10)
)
aluSapEpipeMwGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapEpipeMwCompression"),
        ("ALU-SERVICE-MIB", "aluSapEpipeMwDestMacAddress"),
        ("ALU-SERVICE-MIB", "aluSapEpipeMwSrcMacAddress"),
        ("ALU-SERVICE-MIB", "aluSapEpipeMwCompressRTP"))
)
if mibBuilder.loadTexts:
    aluSapEpipeMwGroup.setStatus("current")

aluSapQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 11)
)
aluSapQosGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapIngressSchedulerMode"),
        ("ALU-SERVICE-MIB", "aluSapIngressAggCir"),
        ("ALU-SERVICE-MIB", "aluSapEgressSchedulerMode"),
        ("ALU-SERVICE-MIB", "aluSapEgressAggCir"),
        ("ALU-SERVICE-MIB", "aluSapIngressAggRateLimit"),
        ("ALU-SERVICE-MIB", "aluSapEgressAggRateLimit"))
)
if mibBuilder.loadTexts:
    aluSapQosGroup.setStatus("current")

aluSapEthLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 12)
)
aluSapEthLoopbackGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapEthLoopback"),
        ("ALU-SERVICE-MIB", "aluSapEthLoopbackDuration"),
        ("ALU-SERVICE-MIB", "aluSapEthLoopbackPersistent"),
        ("ALU-SERVICE-MIB", "aluSapEthLoopbackTimeLeft"),
        ("ALU-SERVICE-MIB", "aluSapEthLoopbackMode"),
        ("ALU-SERVICE-MIB", "aluSapEthLoopbackMacSwap"))
)
if mibBuilder.loadTexts:
    aluSapEthLoopbackGroup.setStatus("current")

aluSapCemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 13)
)
aluSapCemGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapCemAsymDelayEnable"),
        ("ALU-SERVICE-MIB", "aluSapCemAsymDelaySamples"),
        ("ALU-SERVICE-MIB", "aluSapCemAsymDelayRepeatPeriod"),
        ("ALU-SERVICE-MIB", "aluSapCemStatsEgressSamplingDoneCnt"),
        ("ALU-SERVICE-MIB", "aluSapCemStatsEgressAdjustDoneCnt"))
)
if mibBuilder.loadTexts:
    aluSapCemGroup.setStatus("current")

aluSdpBindingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 14)
)
aluSdpBindingGroup.setObjects(
    ("ALU-SERVICE-MIB", "aluSdpBindBaseStatsEgressDroppedPackets")
)
if mibBuilder.loadTexts:
    aluSdpBindingGroup.setStatus("current")

aluSapQosGroupV7v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 15)
)
aluSapQosGroupV7v0.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapIngressShaperGroup"),
        ("ALU-SERVICE-MIB", "aluSapEgressShaperGroup"))
)
if mibBuilder.loadTexts:
    aluSapQosGroupV7v0.setStatus("current")

aluSvcEpipeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 16)
)
aluSvcEpipeGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aluSvcEpipeTeidHashing"),
        ("ALU-SERVICE-MIB", "aluSvcEpipeL4Hashing"),
        ("ALU-SERVICE-MIB", "aeSvcTlsL4Hashing"))
)
if mibBuilder.loadTexts:
    aluSvcEpipeGroup.setStatus("current")

aluSapQosGroupV9v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 17)
)
aluSapQosGroupV9v0.setObjects(
      *(("ALU-SERVICE-MIB", "aluSapIngressAggCirPercent"),
        ("ALU-SERVICE-MIB", "aluSapEgressAggCirPercent"),
        ("ALU-SERVICE-MIB", "aluSapIngressAggRatePercent"),
        ("ALU-SERVICE-MIB", "aluSapEgressAggRatePercent"),
        ("ALU-SERVICE-MIB", "aluSapIngressAggRateType"),
        ("ALU-SERVICE-MIB", "aluSapEgressAggRateType"))
)
if mibBuilder.loadTexts:
    aluSapQosGroupV9v0.setStatus("current")

aluExtSdpBindCpipeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 18)
)
aluExtSdpBindCpipeGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSdpBindCpipeLocalAsymDelay"),
        ("ALU-SERVICE-MIB", "aeSdpBindCpipePeerAsymDelay"),
        ("ALU-SERVICE-MIB", "aeSdpBindCpipeLocalJitterBuffer"),
        ("ALU-SERVICE-MIB", "aeSdpBindCpipePeerJitterBuffer"))
)
if mibBuilder.loadTexts:
    aluExtSdpBindCpipeGroup.setStatus("current")

aluExtSdpBindCpipeSerialGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 19)
)
aluExtSdpBindCpipeSerialGroup.setObjects(
      *(("ALU-SERVICE-MIB", "aeSdpBindCpipeLocalSerialRate"),
        ("ALU-SERVICE-MIB", "aeSdpBindCpipePeerSerialRate"))
)
if mibBuilder.loadTexts:
    aluExtSdpBindCpipeSerialGroup.setStatus("current")

aluSapCemSerialGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 20)
)
aluSapCemSerialGroup.setObjects(
    ("ALU-SERVICE-MIB", "aluSapCemSerialRate")
)
if mibBuilder.loadTexts:
    aluSapCemSerialGroup.setStatus("current")

aluExtSapBaseStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 21)
)
aluExtSapBaseStatsGroup.setObjects(
    ("ALU-SERVICE-MIB", "aluExtSapBaseStatsEgressDroppedPackets")
)
if mibBuilder.loadTexts:
    aluExtSapBaseStatsGroup.setStatus("current")

aluExtSapEthCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 2, 22)
)
aluExtSapEthCfmGroup.setObjects(
    ("ALU-SERVICE-MIB", "aluExtSapEthCfmHoldMepUp")
)
if mibBuilder.loadTexts:
    aluExtSapEthCfmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluServiceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 1, 1)
)
aluServiceMIBCompliance.setObjects(
    ("ALU-SERVICE-MIB", "aluExtSapIpipeIpcpGroup")
)
if mibBuilder.loadTexts:
    aluServiceMIBCompliance.setStatus(
        "obsolete"
    )

aluServiceV3v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 1, 2)
)
aluServiceV3v0MIBCompliance.setObjects(
      *(("ALU-SERVICE-MIB", "aluExtSapIpipeIpcpGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapTlsPPPoEVsaGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapTlsVlanManipulationGroup"))
)
if mibBuilder.loadTexts:
    aluServiceV3v0MIBCompliance.setStatus(
        "obsolete"
    )

aluServiceV9v0MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 6, 1, 8)
)
aluServiceV9v0MIBCompliance.setObjects(
      *(("ALU-SERVICE-MIB", "aluExtSapIpipeIpcpGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapTlsPPPoEVsaGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapTlsVlanManipulationGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapAtmTranslatedVcIdGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapAGBaseInfoGroup"),
        ("ALU-SERVICE-MIB", "aluSapAGBaseStatsGroup"),
        ("ALU-SERVICE-MIB", "aluSapAGIngQosQStatsGroup"),
        ("ALU-SERVICE-MIB", "aluSapAGEgrQosQStatsGroup"),
        ("ALU-SERVICE-MIB", "aluSapEthCfmGroup"),
        ("ALU-SERVICE-MIB", "aluSapEpipeMwGroup"),
        ("ALU-SERVICE-MIB", "aluSapQosGroup"),
        ("ALU-SERVICE-MIB", "aluSapEthLoopbackGroup"),
        ("ALU-SERVICE-MIB", "aluSapCemGroup"),
        ("ALU-SERVICE-MIB", "aluSdpBindingGroup"),
        ("ALU-SERVICE-MIB", "aluSapQosGroupV7v0"),
        ("ALU-SERVICE-MIB", "aluSvcEpipeGroup"),
        ("ALU-SERVICE-MIB", "aluSapQosGroupV9v0"),
        ("ALU-SERVICE-MIB", "aluExtSdpBindCpipeGroup"),
        ("ALU-SERVICE-MIB", "aluExtSdpBindCpipeSerialGroup"),
        ("ALU-SERVICE-MIB", "aluSapCemSerialGroup"),
        ("ALU-SERVICE-MIB", "aluExtSapBaseStatsGroup"))
)
if mibBuilder.loadTexts:
    aluServiceV9v0MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-SERVICE-MIB",
    **{"AluSapSchedulerMode": AluSapSchedulerMode,
       "aluServiceMIBModule": aluServiceMIBModule,
       "aluServiceMIBConformance": aluServiceMIBConformance,
       "aluServiceMIBCompliances": aluServiceMIBCompliances,
       "aluServiceMIBCompliance": aluServiceMIBCompliance,
       "aluServiceV3v0MIBCompliance": aluServiceV3v0MIBCompliance,
       "aluServiceV9v0MIBCompliance": aluServiceV9v0MIBCompliance,
       "aluServiceMIBGroups": aluServiceMIBGroups,
       "aluExtSapIpipeIpcpGroup": aluExtSapIpipeIpcpGroup,
       "aluExtSapTlsPPPoEVsaGroup": aluExtSapTlsPPPoEVsaGroup,
       "aluExtSapTlsVlanManipulationGroup": aluExtSapTlsVlanManipulationGroup,
       "aluExtSapAtmTranslatedVcIdGroup": aluExtSapAtmTranslatedVcIdGroup,
       "aluExtSapAGBaseInfoGroup": aluExtSapAGBaseInfoGroup,
       "aluSapAGBaseStatsGroup": aluSapAGBaseStatsGroup,
       "aluSapAGIngQosQStatsGroup": aluSapAGIngQosQStatsGroup,
       "aluSapAGEgrQosQStatsGroup": aluSapAGEgrQosQStatsGroup,
       "aluSapEthCfmGroup": aluSapEthCfmGroup,
       "aluSapEpipeMwGroup": aluSapEpipeMwGroup,
       "aluSapQosGroup": aluSapQosGroup,
       "aluSapEthLoopbackGroup": aluSapEthLoopbackGroup,
       "aluSapCemGroup": aluSapCemGroup,
       "aluSdpBindingGroup": aluSdpBindingGroup,
       "aluSapQosGroupV7v0": aluSapQosGroupV7v0,
       "aluSvcEpipeGroup": aluSvcEpipeGroup,
       "aluSapQosGroupV9v0": aluSapQosGroupV9v0,
       "aluExtSdpBindCpipeGroup": aluExtSdpBindCpipeGroup,
       "aluExtSdpBindCpipeSerialGroup": aluExtSdpBindCpipeSerialGroup,
       "aluSapCemSerialGroup": aluSapCemSerialGroup,
       "aluExtSapBaseStatsGroup": aluExtSapBaseStatsGroup,
       "aluExtSapEthCfmGroup": aluExtSapEthCfmGroup,
       "aluServiceObjs": aluServiceObjs,
       "aeSapIpipeInfoTable": aeSapIpipeInfoTable,
       "aeSapIpipeInfoEntry": aeSapIpipeInfoEntry,
       "aeSapIpipeIpcpAssignCeAddress": aeSapIpipeIpcpAssignCeAddress,
       "aeSapIpipeIpcpPriDnsAddrType": aeSapIpipeIpcpPriDnsAddrType,
       "aeSapIpipeIpcpPriDnsAddr": aeSapIpipeIpcpPriDnsAddr,
       "aeSapIpipeIpcpSecDnsAddrType": aeSapIpipeIpcpSecDnsAddrType,
       "aeSapIpipeIpcpSecDnsAddr": aeSapIpipeIpcpSecDnsAddr,
       "aeSapTlsInfoTable": aeSapTlsInfoTable,
       "aeSapTlsInfoEntry": aeSapTlsInfoEntry,
       "aeSapTlsPPPoEIncludeCircuitId": aeSapTlsPPPoEIncludeCircuitId,
       "aeSapTlsPPPoECircuitId": aeSapTlsPPPoECircuitId,
       "aeSapTlsForceCVlanForwarding": aeSapTlsForceCVlanForwarding,
       "aeSapTlsAtmInfoTable": aeSapTlsAtmInfoTable,
       "aeSapTlsAtmInfoEntry": aeSapTlsAtmInfoEntry,
       "aeSapTlsAtmSubscriberVlanTag": aeSapTlsAtmSubscriberVlanTag,
       "aeSvcTlsInfoTable": aeSvcTlsInfoTable,
       "aeSvcTlsInfoEntry": aeSvcTlsInfoEntry,
       "aeSvcTlsPPPoEIncludeCircuitId": aeSvcTlsPPPoEIncludeCircuitId,
       "aeSvcTlsL4Hashing": aeSvcTlsL4Hashing,
       "aeSapApipeAtmInfoTable": aeSapApipeAtmInfoTable,
       "aeSapApipeAtmInfoEntry": aeSapApipeAtmInfoEntry,
       "aeSapApipeAtmVcidTranslatedVpi": aeSapApipeAtmVcidTranslatedVpi,
       "aeSapApipeAtmVcidTranslatedVci": aeSapApipeAtmVcidTranslatedVci,
       "aeSvcSapAGInfoTable": aeSvcSapAGInfoTable,
       "aeSvcSapAGInfoEntry": aeSvcSapAGInfoEntry,
       "aeSvcSapAGName": aeSvcSapAGName,
       "aeSvcSapAGRowStatus": aeSvcSapAGRowStatus,
       "aeSvcSapAGDescription": aeSvcSapAGDescription,
       "aeSvcSapAGIngressQosPolicyId": aeSvcSapAGIngressQosPolicyId,
       "aeSvcSapAGEgressQosPolicyId": aeSvcSapAGEgressQosPolicyId,
       "aeSvcSapAGCollectAcctStats": aeSvcSapAGCollectAcctStats,
       "aeSvcSapAGAccountingPolicyId": aeSvcSapAGAccountingPolicyId,
       "aluSapAGBaseStatsTable": aluSapAGBaseStatsTable,
       "aluSapAGBaseStatsEntry": aluSapAGBaseStatsEntry,
       "aluSapAGBaseStatsIngressDroppedPackets": aluSapAGBaseStatsIngressDroppedPackets,
       "aluSapAGBaseStatsIngressDroppedOctets": aluSapAGBaseStatsIngressDroppedOctets,
       "aluSapAGBaseStatsIngressOfferedHiPrioPackets": aluSapAGBaseStatsIngressOfferedHiPrioPackets,
       "aluSapAGBaseStatsIngressOfferedHiPrioOctets": aluSapAGBaseStatsIngressOfferedHiPrioOctets,
       "aluSapAGBaseStatsIngressOfferedLoPrioPackets": aluSapAGBaseStatsIngressOfferedLoPrioPackets,
       "aluSapAGBaseStatsIngressOfferedLoPrioOctets": aluSapAGBaseStatsIngressOfferedLoPrioOctets,
       "aluSapAGBaseStatsIngressDroppedHiPrioPackets": aluSapAGBaseStatsIngressDroppedHiPrioPackets,
       "aluSapAGBaseStatsIngressDroppedHiPrioOctets": aluSapAGBaseStatsIngressDroppedHiPrioOctets,
       "aluSapAGBaseStatsIngressDroppedLoPrioPackets": aluSapAGBaseStatsIngressDroppedLoPrioPackets,
       "aluSapAGBaseStatsIngressDroppedLoPrioOctets": aluSapAGBaseStatsIngressDroppedLoPrioOctets,
       "aluSapAGBaseStatsIngressForwardedInProfPackets": aluSapAGBaseStatsIngressForwardedInProfPackets,
       "aluSapAGBaseStatsIngressForwardedInProfOctets": aluSapAGBaseStatsIngressForwardedInProfOctets,
       "aluSapAGBaseStatsIngressForwardedOutProfPackets": aluSapAGBaseStatsIngressForwardedOutProfPackets,
       "aluSapAGBaseStatsIngressForwardedOutProfOctets": aluSapAGBaseStatsIngressForwardedOutProfOctets,
       "aluSapAGBaseStatsEgressDroppedInProfPackets": aluSapAGBaseStatsEgressDroppedInProfPackets,
       "aluSapAGBaseStatsEgressDroppedInProfOctets": aluSapAGBaseStatsEgressDroppedInProfOctets,
       "aluSapAGBaseStatsEgressDroppedOutProfPackets": aluSapAGBaseStatsEgressDroppedOutProfPackets,
       "aluSapAGBaseStatsEgressDroppedOutProfOctets": aluSapAGBaseStatsEgressDroppedOutProfOctets,
       "aluSapAGBaseStatsEgressForwardedInProfPackets": aluSapAGBaseStatsEgressForwardedInProfPackets,
       "aluSapAGBaseStatsEgressForwardedInProfOctets": aluSapAGBaseStatsEgressForwardedInProfOctets,
       "aluSapAGBaseStatsEgressForwardedOutProfPackets": aluSapAGBaseStatsEgressForwardedOutProfPackets,
       "aluSapAGBaseStatsEgressForwardedOutProfOctets": aluSapAGBaseStatsEgressForwardedOutProfOctets,
       "aluSapAGBaseStatsUnknownVpiVciCellsDropped": aluSapAGBaseStatsUnknownVpiVciCellsDropped,
       "aluSapAGBaseStatsCustId": aluSapAGBaseStatsCustId,
       "aluSapAGBaseStatsIngressOfferedUncoloredPackets": aluSapAGBaseStatsIngressOfferedUncoloredPackets,
       "aluSapAGBaseStatsIngressOfferedUncoloredOctets": aluSapAGBaseStatsIngressOfferedUncoloredOctets,
       "aluSapAGBaseStatsAuthenticationPktsDiscarded": aluSapAGBaseStatsAuthenticationPktsDiscarded,
       "aluSapAGBaseStatsAuthenticationPktsSuccess": aluSapAGBaseStatsAuthenticationPktsSuccess,
       "aluSapAGBaseStatsLastClearedTime": aluSapAGBaseStatsLastClearedTime,
       "aluSapAGIngQosQStatsTable": aluSapAGIngQosQStatsTable,
       "aluSapAGIngQosQStatsEntry": aluSapAGIngQosQStatsEntry,
       "aluSapAGIngQosQueueId": aluSapAGIngQosQueueId,
       "aluSapAGIngQosQStatsOfferedHiPrioPackets": aluSapAGIngQosQStatsOfferedHiPrioPackets,
       "aluSapAGIngQosQStatsDroppedHiPrioPackets": aluSapAGIngQosQStatsDroppedHiPrioPackets,
       "aluSapAGIngQosQStatsOfferedLoPrioPackets": aluSapAGIngQosQStatsOfferedLoPrioPackets,
       "aluSapAGIngQosQStatsDroppedLoPrioPackets": aluSapAGIngQosQStatsDroppedLoPrioPackets,
       "aluSapAGIngQosQStatsOfferedHiPrioOctets": aluSapAGIngQosQStatsOfferedHiPrioOctets,
       "aluSapAGIngQosQStatsDroppedHiPrioOctets": aluSapAGIngQosQStatsDroppedHiPrioOctets,
       "aluSapAGIngQosQStatsOfferedLoPrioOctets": aluSapAGIngQosQStatsOfferedLoPrioOctets,
       "aluSapAGIngQosQStatsDroppedLoPrioOctets": aluSapAGIngQosQStatsDroppedLoPrioOctets,
       "aluSapAGIngQosQStatsForwardedInProfPackets": aluSapAGIngQosQStatsForwardedInProfPackets,
       "aluSapAGIngQosQStatsForwardedOutProfPackets": aluSapAGIngQosQStatsForwardedOutProfPackets,
       "aluSapAGIngQosQStatsForwardedInProfOctets": aluSapAGIngQosQStatsForwardedInProfOctets,
       "aluSapAGIngQosQStatsForwardedOutProfOctets": aluSapAGIngQosQStatsForwardedOutProfOctets,
       "aluSapAGIngQosCustId": aluSapAGIngQosCustId,
       "aluSapAGIngQosQStatsUncoloredPacketsOffered": aluSapAGIngQosQStatsUncoloredPacketsOffered,
       "aluSapAGIngQosQStatsUncoloredOctetsOffered": aluSapAGIngQosQStatsUncoloredOctetsOffered,
       "aluSapAGEgrQosQStatsTable": aluSapAGEgrQosQStatsTable,
       "aluSapAGEgrQosQStatsEntry": aluSapAGEgrQosQStatsEntry,
       "aluSapAGEgrQosQueueId": aluSapAGEgrQosQueueId,
       "aluSapAGEgrQosQStatsForwardedInProfPackets": aluSapAGEgrQosQStatsForwardedInProfPackets,
       "aluSapAGEgrQosQStatsDroppedInProfPackets": aluSapAGEgrQosQStatsDroppedInProfPackets,
       "aluSapAGEgrQosQStatsForwardedOutProfPackets": aluSapAGEgrQosQStatsForwardedOutProfPackets,
       "aluSapAGEgrQosQStatsDroppedOutProfPackets": aluSapAGEgrQosQStatsDroppedOutProfPackets,
       "aluSapAGEgrQosQStatsForwardedInProfOctets": aluSapAGEgrQosQStatsForwardedInProfOctets,
       "aluSapAGEgrQosQStatsDroppedInProfOctets": aluSapAGEgrQosQStatsDroppedInProfOctets,
       "aluSapAGEgrQosQStatsForwardedOutProfOctets": aluSapAGEgrQosQStatsForwardedOutProfOctets,
       "aluSapAGEgrQosQStatsDroppedOutProfOctets": aluSapAGEgrQosQStatsDroppedOutProfOctets,
       "aluSapAGEgrQosCustId": aluSapAGEgrQosCustId,
       "aluSapEthCfmTable": aluSapEthCfmTable,
       "aluSapEthCfmEntry": aluSapEthCfmEntry,
       "aluSapEthCfmHoldMepUp": aluSapEthCfmHoldMepUp,
       "aluSapEpipeInfoTable": aluSapEpipeInfoTable,
       "aluSapEpipeInfoEntry": aluSapEpipeInfoEntry,
       "aluSapEpipeMwCompression": aluSapEpipeMwCompression,
       "aluSapEpipeMwDestMacAddress": aluSapEpipeMwDestMacAddress,
       "aluSapEpipeMwSrcMacAddress": aluSapEpipeMwSrcMacAddress,
       "aluSapEpipeMwCompressRTP": aluSapEpipeMwCompressRTP,
       "aluSapBaseInfoTable": aluSapBaseInfoTable,
       "aluSapBaseInfoEntry": aluSapBaseInfoEntry,
       "aluSapIngressSchedulerMode": aluSapIngressSchedulerMode,
       "aluSapEgressSchedulerMode": aluSapEgressSchedulerMode,
       "aluSapIngressAggCir": aluSapIngressAggCir,
       "aluSapEgressAggCir": aluSapEgressAggCir,
       "aluSapIngressAggRateLimit": aluSapIngressAggRateLimit,
       "aluSapEgressAggRateLimit": aluSapEgressAggRateLimit,
       "aluSapIngressShaperGroup": aluSapIngressShaperGroup,
       "aluSapEgressShaperGroup": aluSapEgressShaperGroup,
       "aluSapIngressAggCirPercent": aluSapIngressAggCirPercent,
       "aluSapEgressAggCirPercent": aluSapEgressAggCirPercent,
       "aluSapIngressAggRatePercent": aluSapIngressAggRatePercent,
       "aluSapEgressAggRatePercent": aluSapEgressAggRatePercent,
       "aluSapIngressAggRateType": aluSapIngressAggRateType,
       "aluSapEgressAggRateType": aluSapEgressAggRateType,
       "aluSapEthLoopbackTable": aluSapEthLoopbackTable,
       "aluSapEthLoopbackEntry": aluSapEthLoopbackEntry,
       "aluSapEthLoopback": aluSapEthLoopback,
       "aluSapEthLoopbackDuration": aluSapEthLoopbackDuration,
       "aluSapEthLoopbackPersistent": aluSapEthLoopbackPersistent,
       "aluSapEthLoopbackTimeLeft": aluSapEthLoopbackTimeLeft,
       "aluSapEthLoopbackMode": aluSapEthLoopbackMode,
       "aluSapEthLoopbackMacSwap": aluSapEthLoopbackMacSwap,
       "aluSapCemInfoTable": aluSapCemInfoTable,
       "aluSapCemInfoEntry": aluSapCemInfoEntry,
       "aluSapCemAsymDelayEnable": aluSapCemAsymDelayEnable,
       "aluSapCemAsymDelaySamples": aluSapCemAsymDelaySamples,
       "aluSapCemAsymDelayRepeatPeriod": aluSapCemAsymDelayRepeatPeriod,
       "aluSapCemSerialRate": aluSapCemSerialRate,
       "aluSapCemOnDemandADC": aluSapCemOnDemandADC,
       "aluSapCemStatsTable": aluSapCemStatsTable,
       "aluSapCemStatsEntry": aluSapCemStatsEntry,
       "aluSapCemStatsEgressSamplingDoneCnt": aluSapCemStatsEgressSamplingDoneCnt,
       "aluSapCemStatsEgressAdjustDoneCnt": aluSapCemStatsEgressAdjustDoneCnt,
       "aluSdpBindStatsTable": aluSdpBindStatsTable,
       "aluSdpBindStatsEntry": aluSdpBindStatsEntry,
       "aluSdpBindBaseStatsEgressDroppedPackets": aluSdpBindBaseStatsEgressDroppedPackets,
       "aluSvcEpipeTable": aluSvcEpipeTable,
       "aluSvcEpipeEntry": aluSvcEpipeEntry,
       "aluSvcEpipeTeidHashing": aluSvcEpipeTeidHashing,
       "aluSvcEpipeL4Hashing": aluSvcEpipeL4Hashing,
       "aeSdpBindCpipeTable": aeSdpBindCpipeTable,
       "aeSdpBindCpipeEntry": aeSdpBindCpipeEntry,
       "aeSdpBindCpipeLocalAsymDelay": aeSdpBindCpipeLocalAsymDelay,
       "aeSdpBindCpipePeerAsymDelay": aeSdpBindCpipePeerAsymDelay,
       "aeSdpBindCpipeLocalJitterBuffer": aeSdpBindCpipeLocalJitterBuffer,
       "aeSdpBindCpipePeerJitterBuffer": aeSdpBindCpipePeerJitterBuffer,
       "aeSdpBindCpipeLocalSerialRate": aeSdpBindCpipeLocalSerialRate,
       "aeSdpBindCpipePeerSerialRate": aeSdpBindCpipePeerSerialRate,
       "aluExtSapBaseStatsTable": aluExtSapBaseStatsTable,
       "aluExtSapBaseStatsEntry": aluExtSapBaseStatsEntry,
       "aluExtSapBaseStatsEgressDroppedPackets": aluExtSapBaseStatsEgressDroppedPackets,
       "aluExtSapEthCfmTable": aluExtSapEthCfmTable,
       "aluExtSapEthCfmEntry": aluExtSapEthCfmEntry,
       "aluExtSapEthCfmHoldMepUp": aluExtSapEthCfmHoldMepUp}
)
