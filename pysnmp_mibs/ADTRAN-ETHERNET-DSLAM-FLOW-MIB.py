# SNMP MIB module (ADTRAN-ETHERNET-DSLAM-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-ETHERNET-DSLAM-FLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:30 2025
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

(adGenPortInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenEthernetDslamFlow,
 adGenEthernetDslamFlowID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenEthernetDslamFlow",
    "adGenEthernetDslamFlowID")

(GenSystemInterfaceType,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "GenSystemInterfaceType")

(adGenMiniDslam3gMacAddress,) = mibBuilder.importSymbols(
    "ADTRAN-TAMINIDSLAM3G-MIB",
    "adGenMiniDslam3gMacAddress")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenEthernetDslamFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 2, 2)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMIB.setRevisions(
        ("2021-03-03 00:00",
         "2016-01-21 00:00",
         "2014-09-12 00:00",
         "2014-05-13 00:00",
         "2013-11-08 00:00",
         "2013-09-12 00:00",
         "2013-02-19 00:00",
         "2013-01-03 00:00",
         "2012-11-06 00:00",
         "2012-09-13 00:00",
         "2012-07-30 00:00",
         "2012-07-17 00:00",
         "2012-06-27 11:50",
         "2012-04-20 11:50",
         "2012-04-09 11:50",
         "2011-12-21 00:00",
         "2011-11-28 00:00",
         "2011-09-19 00:00",
         "2011-08-22 00:00",
         "2011-08-03 00:00",
         "2011-06-01 00:00",
         "2011-03-24 00:00",
         "2007-09-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEthernetInterfaceTable_Object = MibTable
adGenEthernetInterfaceTable = _AdGenEthernetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEthernetInterfaceTable.setStatus("current")
_AdGenEthernetInterfaceEntry_Object = MibTableRow
adGenEthernetInterfaceEntry = _AdGenEthernetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1)
)
adGenEthernetInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetInterfaceLogicalIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetInterfaceEntry.setStatus("current")
_AdGenEthernetInterfaceLogicalIndex_Type = Integer32
_AdGenEthernetInterfaceLogicalIndex_Object = MibTableColumn
adGenEthernetInterfaceLogicalIndex = _AdGenEthernetInterfaceLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1, 1),
    _AdGenEthernetInterfaceLogicalIndex_Type()
)
adGenEthernetInterfaceLogicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceLogicalIndex.setStatus("current")
_AdGenEthernetInterfaceMaxMACAddresses_Type = Integer32
_AdGenEthernetInterfaceMaxMACAddresses_Object = MibTableColumn
adGenEthernetInterfaceMaxMACAddresses = _AdGenEthernetInterfaceMaxMACAddresses_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1, 2),
    _AdGenEthernetInterfaceMaxMACAddresses_Type()
)
adGenEthernetInterfaceMaxMACAddresses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceMaxMACAddresses.setStatus("current")
_AdGenEthernetInterfaceFlowList_Type = DisplayString
_AdGenEthernetInterfaceFlowList_Object = MibTableColumn
adGenEthernetInterfaceFlowList = _AdGenEthernetInterfaceFlowList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1, 3),
    _AdGenEthernetInterfaceFlowList_Type()
)
adGenEthernetInterfaceFlowList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceFlowList.setStatus("current")


class _AdGenEthernetInterfaceSourceAuthentication_Type(Integer32):
    """Custom type adGenEthernetInterfaceSourceAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenEthernetInterfaceSourceAuthentication_Type.__name__ = "Integer32"
_AdGenEthernetInterfaceSourceAuthentication_Object = MibTableColumn
adGenEthernetInterfaceSourceAuthentication = _AdGenEthernetInterfaceSourceAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1, 4),
    _AdGenEthernetInterfaceSourceAuthentication_Type()
)
adGenEthernetInterfaceSourceAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceSourceAuthentication.setStatus("current")
_AdGenEthernetInterfaceType_Type = GenSystemInterfaceType
_AdGenEthernetInterfaceType_Object = MibTableColumn
adGenEthernetInterfaceType = _AdGenEthernetInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1, 5),
    _AdGenEthernetInterfaceType_Type()
)
adGenEthernetInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceType.setStatus("current")
_AdGenEthernetInterfaceTypeSpecific_Type = OctetString
_AdGenEthernetInterfaceTypeSpecific_Object = MibTableColumn
adGenEthernetInterfaceTypeSpecific = _AdGenEthernetInterfaceTypeSpecific_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 1, 1, 6),
    _AdGenEthernetInterfaceTypeSpecific_Type()
)
adGenEthernetInterfaceTypeSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceTypeSpecific.setStatus("current")
_AdGenEthernetDslamFlowTable_Object = MibTable
adGenEthernetDslamFlowTable = _AdGenEthernetDslamFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowTable.setStatus("current")
_AdGenEthernetDslamFlowEntry_Object = MibTableRow
adGenEthernetDslamFlowEntry = _AdGenEthernetDslamFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1)
)
adGenEthernetDslamFlowEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowEntry.setStatus("current")
_AdGenEthernetDslamFlowIndex_Type = Integer32
_AdGenEthernetDslamFlowIndex_Object = MibTableColumn
adGenEthernetDslamFlowIndex = _AdGenEthernetDslamFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 1),
    _AdGenEthernetDslamFlowIndex_Type()
)
adGenEthernetDslamFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIndex.setStatus("current")


class _AdGenEthernetDslamFlowName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowName_Object = MibTableColumn
adGenEthernetDslamFlowName = _AdGenEthernetDslamFlowName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 2),
    _AdGenEthernetDslamFlowName_Type()
)
adGenEthernetDslamFlowName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowName.setStatus("current")


class _AdGenEthernetDslamFlowTrafficDirection_Type(Integer32):
    """Custom type adGenEthernetDslamFlowTrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2),
          ("bidirectional", 3))
    )


_AdGenEthernetDslamFlowTrafficDirection_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowTrafficDirection_Object = MibTableColumn
adGenEthernetDslamFlowTrafficDirection = _AdGenEthernetDslamFlowTrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 3),
    _AdGenEthernetDslamFlowTrafficDirection_Type()
)
adGenEthernetDslamFlowTrafficDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowTrafficDirection.setStatus("current")


class _AdGenEthernetDslamFlowNetworkSTag_Type(Integer32):
    """Custom type adGenEthernetDslamFlowNetworkSTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AdGenEthernetDslamFlowNetworkSTag_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowNetworkSTag_Object = MibTableColumn
adGenEthernetDslamFlowNetworkSTag = _AdGenEthernetDslamFlowNetworkSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 4),
    _AdGenEthernetDslamFlowNetworkSTag_Type()
)
adGenEthernetDslamFlowNetworkSTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkSTag.setStatus("current")


class _AdGenEthernetDslamFlowNetworkCTag_Type(Integer32):
    """Custom type adGenEthernetDslamFlowNetworkCTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_AdGenEthernetDslamFlowNetworkCTag_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowNetworkCTag_Object = MibTableColumn
adGenEthernetDslamFlowNetworkCTag = _AdGenEthernetDslamFlowNetworkCTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 5),
    _AdGenEthernetDslamFlowNetworkCTag_Type()
)
adGenEthernetDslamFlowNetworkCTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkCTag.setStatus("current")


class _AdGenEthernetDslamFlowCEVlan_Type(Integer32):
    """Custom type adGenEthernetDslamFlowCEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4098),
    )


_AdGenEthernetDslamFlowCEVlan_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowCEVlan_Object = MibTableColumn
adGenEthernetDslamFlowCEVlan = _AdGenEthernetDslamFlowCEVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 6),
    _AdGenEthernetDslamFlowCEVlan_Type()
)
adGenEthernetDslamFlowCEVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCEVlan.setStatus("current")
_AdGenEthernetDslamFlowDownstreamForwardingMode_Type = Integer32
_AdGenEthernetDslamFlowDownstreamForwardingMode_Object = MibTableColumn
adGenEthernetDslamFlowDownstreamForwardingMode = _AdGenEthernetDslamFlowDownstreamForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 7),
    _AdGenEthernetDslamFlowDownstreamForwardingMode_Type()
)
adGenEthernetDslamFlowDownstreamForwardingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDownstreamForwardingMode.setStatus("current")


class _AdGenEthernetDslamFlowDownstreamPbitMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDownstreamPbitMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 1),
          ("marked", 2),
          ("mapped", 3))
    )


_AdGenEthernetDslamFlowDownstreamPbitMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDownstreamPbitMethod_Object = MibTableColumn
adGenEthernetDslamFlowDownstreamPbitMethod = _AdGenEthernetDslamFlowDownstreamPbitMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 8),
    _AdGenEthernetDslamFlowDownstreamPbitMethod_Type()
)
adGenEthernetDslamFlowDownstreamPbitMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDownstreamPbitMethod.setStatus("current")


class _AdGenEthernetDslamFlowDownstreamPbitMarking_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDownstreamPbitMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthernetDslamFlowDownstreamPbitMarking_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDownstreamPbitMarking_Object = MibTableColumn
adGenEthernetDslamFlowDownstreamPbitMarking = _AdGenEthernetDslamFlowDownstreamPbitMarking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 9),
    _AdGenEthernetDslamFlowDownstreamPbitMarking_Type()
)
adGenEthernetDslamFlowDownstreamPbitMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDownstreamPbitMarking.setStatus("current")
_AdGenEthernetDslamFlowDownstreamPbitMapping_Type = Integer32
_AdGenEthernetDslamFlowDownstreamPbitMapping_Object = MibTableColumn
adGenEthernetDslamFlowDownstreamPbitMapping = _AdGenEthernetDslamFlowDownstreamPbitMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 10),
    _AdGenEthernetDslamFlowDownstreamPbitMapping_Type()
)
adGenEthernetDslamFlowDownstreamPbitMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDownstreamPbitMapping.setStatus("current")


class _AdGenEthernetDslamFlowNetworkIngressPbit_Type(Integer32):
    """Custom type adGenEthernetDslamFlowNetworkIngressPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenEthernetDslamFlowNetworkIngressPbit_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowNetworkIngressPbit_Object = MibTableColumn
adGenEthernetDslamFlowNetworkIngressPbit = _AdGenEthernetDslamFlowNetworkIngressPbit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 11),
    _AdGenEthernetDslamFlowNetworkIngressPbit_Type()
)
adGenEthernetDslamFlowNetworkIngressPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkIngressPbit.setStatus("current")
_AdGenEthernetDslamFlowNetworkIngressEtherType_Type = Integer32
_AdGenEthernetDslamFlowNetworkIngressEtherType_Object = MibTableColumn
adGenEthernetDslamFlowNetworkIngressEtherType = _AdGenEthernetDslamFlowNetworkIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 12),
    _AdGenEthernetDslamFlowNetworkIngressEtherType_Type()
)
adGenEthernetDslamFlowNetworkIngressEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkIngressEtherType.setStatus("current")


class _AdGenEthernetDslamFlowNetworkIngressDSCP_Type(Integer32):
    """Custom type adGenEthernetDslamFlowNetworkIngressDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AdGenEthernetDslamFlowNetworkIngressDSCP_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowNetworkIngressDSCP_Object = MibTableColumn
adGenEthernetDslamFlowNetworkIngressDSCP = _AdGenEthernetDslamFlowNetworkIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 13),
    _AdGenEthernetDslamFlowNetworkIngressDSCP_Type()
)
adGenEthernetDslamFlowNetworkIngressDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkIngressDSCP.setStatus("current")
_AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Type = Integer32
_AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Object = MibTableColumn
adGenEthernetDslamFlowNetworkIngressIPProtocolID = _AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 14),
    _AdGenEthernetDslamFlowNetworkIngressIPProtocolID_Type()
)
adGenEthernetDslamFlowNetworkIngressIPProtocolID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkIngressIPProtocolID.setStatus("current")
_AdGenEthernetDslamFlowUpstreamForwardingMode_Type = Integer32
_AdGenEthernetDslamFlowUpstreamForwardingMode_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamForwardingMode = _AdGenEthernetDslamFlowUpstreamForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 15),
    _AdGenEthernetDslamFlowUpstreamForwardingMode_Type()
)
adGenEthernetDslamFlowUpstreamForwardingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamForwardingMode.setStatus("current")


class _AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowUpstreamSTagPbitMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 1),
          ("marked", 2),
          ("mapped", 3))
    )


_AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamSTagPbitMethod = _AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 16),
    _AdGenEthernetDslamFlowUpstreamSTagPbitMethod_Type()
)
adGenEthernetDslamFlowUpstreamSTagPbitMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamSTagPbitMethod.setStatus("current")


class _AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Type(Integer32):
    """Custom type adGenEthernetDslamFlowUpstreamSTagPbitMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamSTagPbitMarking = _AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 17),
    _AdGenEthernetDslamFlowUpstreamSTagPbitMarking_Type()
)
adGenEthernetDslamFlowUpstreamSTagPbitMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamSTagPbitMarking.setStatus("current")
_AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Type = Integer32
_AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamSTagPbitMapping = _AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 18),
    _AdGenEthernetDslamFlowUpstreamSTagPbitMapping_Type()
)
adGenEthernetDslamFlowUpstreamSTagPbitMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamSTagPbitMapping.setStatus("current")


class _AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowUpstreamCTagPbitMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 1),
          ("marked", 2),
          ("mapped", 3))
    )


_AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamCTagPbitMethod = _AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 19),
    _AdGenEthernetDslamFlowUpstreamCTagPbitMethod_Type()
)
adGenEthernetDslamFlowUpstreamCTagPbitMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamCTagPbitMethod.setStatus("current")


class _AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Type(Integer32):
    """Custom type adGenEthernetDslamFlowUpstreamCTagPbitMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamCTagPbitMarking = _AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 20),
    _AdGenEthernetDslamFlowUpstreamCTagPbitMarking_Type()
)
adGenEthernetDslamFlowUpstreamCTagPbitMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamCTagPbitMarking.setStatus("current")
_AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Type = Integer32
_AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamCTagPbitMapping = _AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 21),
    _AdGenEthernetDslamFlowUpstreamCTagPbitMapping_Type()
)
adGenEthernetDslamFlowUpstreamCTagPbitMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamCTagPbitMapping.setStatus("current")


class _AdGenEthernetDslamFlowCustomerIngressPbit_Type(Integer32):
    """Custom type adGenEthernetDslamFlowCustomerIngressPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenEthernetDslamFlowCustomerIngressPbit_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowCustomerIngressPbit_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressPbit = _AdGenEthernetDslamFlowCustomerIngressPbit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 22),
    _AdGenEthernetDslamFlowCustomerIngressPbit_Type()
)
adGenEthernetDslamFlowCustomerIngressPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressPbit.setStatus("current")
_AdGenEthernetDslamFlowCustomerIngressEtherType_Type = Integer32
_AdGenEthernetDslamFlowCustomerIngressEtherType_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressEtherType = _AdGenEthernetDslamFlowCustomerIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 23),
    _AdGenEthernetDslamFlowCustomerIngressEtherType_Type()
)
adGenEthernetDslamFlowCustomerIngressEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressEtherType.setStatus("current")


class _AdGenEthernetDslamFlowCustomerIngressDSCP_Type(Integer32):
    """Custom type adGenEthernetDslamFlowCustomerIngressDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AdGenEthernetDslamFlowCustomerIngressDSCP_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowCustomerIngressDSCP_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressDSCP = _AdGenEthernetDslamFlowCustomerIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 24),
    _AdGenEthernetDslamFlowCustomerIngressDSCP_Type()
)
adGenEthernetDslamFlowCustomerIngressDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressDSCP.setStatus("current")
_AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Type = Integer32
_AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressIPProtocolID = _AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 25),
    _AdGenEthernetDslamFlowCustomerIngressIPProtocolID_Type()
)
adGenEthernetDslamFlowCustomerIngressIPProtocolID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressIPProtocolID.setStatus("current")


class _AdGenEthernetDslamFlowCustomerIngressBroadcast_Type(Integer32):
    """Custom type adGenEthernetDslamFlowCustomerIngressBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowCustomerIngressBroadcast_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowCustomerIngressBroadcast_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressBroadcast = _AdGenEthernetDslamFlowCustomerIngressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 26),
    _AdGenEthernetDslamFlowCustomerIngressBroadcast_Type()
)
adGenEthernetDslamFlowCustomerIngressBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressBroadcast.setStatus("current")


class _AdGenEthernetDslamFlowCustomerIngressMulticast_Type(Integer32):
    """Custom type adGenEthernetDslamFlowCustomerIngressMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowCustomerIngressMulticast_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowCustomerIngressMulticast_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressMulticast = _AdGenEthernetDslamFlowCustomerIngressMulticast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 27),
    _AdGenEthernetDslamFlowCustomerIngressMulticast_Type()
)
adGenEthernetDslamFlowCustomerIngressMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressMulticast.setStatus("current")


class _AdGenEthernetDslamFlowCustomerIngressUnicast_Type(Integer32):
    """Custom type adGenEthernetDslamFlowCustomerIngressUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowCustomerIngressUnicast_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowCustomerIngressUnicast_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressUnicast = _AdGenEthernetDslamFlowCustomerIngressUnicast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 28),
    _AdGenEthernetDslamFlowCustomerIngressUnicast_Type()
)
adGenEthernetDslamFlowCustomerIngressUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressUnicast.setStatus("current")
_AdGenEthernetDslamFlowCustomerIngressPolicer_Type = Integer32
_AdGenEthernetDslamFlowCustomerIngressPolicer_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressPolicer = _AdGenEthernetDslamFlowCustomerIngressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 29),
    _AdGenEthernetDslamFlowCustomerIngressPolicer_Type()
)
adGenEthernetDslamFlowCustomerIngressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressPolicer.setStatus("current")


class _AdGenEthernetDslamFlowEncapsMode_Type(Integer32):
    """Custom type adGenEthernetDslamFlowEncapsMode based on Integer32"""
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
        *(("ipoe", 1),
          ("pppoe", 2),
          ("pppoa", 3),
          ("notApplicable", 4),
          ("atmoe", 5),
          ("pppoaVcMux", 6),
          ("autoDetect", 7),
          ("ethernet", 8))
    )


_AdGenEthernetDslamFlowEncapsMode_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowEncapsMode_Object = MibTableColumn
adGenEthernetDslamFlowEncapsMode = _AdGenEthernetDslamFlowEncapsMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 30),
    _AdGenEthernetDslamFlowEncapsMode_Type()
)
adGenEthernetDslamFlowEncapsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowEncapsMode.setStatus("current")


class _AdGenEthernetDslamFlowManualAddrAging_Type(Integer32):
    """Custom type adGenEthernetDslamFlowManualAddrAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AdGenEthernetDslamFlowManualAddrAging_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowManualAddrAging_Object = MibTableColumn
adGenEthernetDslamFlowManualAddrAging = _AdGenEthernetDslamFlowManualAddrAging_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 31),
    _AdGenEthernetDslamFlowManualAddrAging_Type()
)
adGenEthernetDslamFlowManualAddrAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowManualAddrAging.setStatus("current")


class _AdGenEthernetDslamFlowIntermedAgent_Type(Integer32):
    """Custom type adGenEthernetDslamFlowIntermedAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowIntermedAgent_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowIntermedAgent_Object = MibTableColumn
adGenEthernetDslamFlowIntermedAgent = _AdGenEthernetDslamFlowIntermedAgent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 32),
    _AdGenEthernetDslamFlowIntermedAgent_Type()
)
adGenEthernetDslamFlowIntermedAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIntermedAgent.setStatus("current")


class _AdGenEthernetDslamFlowDhcpRelay_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpRelay based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3),
          ("transparent", 4),
          ("snoop", 5))
    )


_AdGenEthernetDslamFlowDhcpRelay_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpRelay_Object = MibTableColumn
adGenEthernetDslamFlowDhcpRelay = _AdGenEthernetDslamFlowDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 33),
    _AdGenEthernetDslamFlowDhcpRelay_Type()
)
adGenEthernetDslamFlowDhcpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpRelay.setStatus("current")


class _AdGenEthernetDslamFlowOption82Insert_Type(Integer32):
    """Custom type adGenEthernetDslamFlowOption82Insert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowOption82Insert_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowOption82Insert_Object = MibTableColumn
adGenEthernetDslamFlowOption82Insert = _AdGenEthernetDslamFlowOption82Insert_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 34),
    _AdGenEthernetDslamFlowOption82Insert_Type()
)
adGenEthernetDslamFlowOption82Insert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowOption82Insert.setStatus("current")


class _AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowLearnedIpAddrAgingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lease", 1),
          ("fixed", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Object = MibTableColumn
adGenEthernetDslamFlowLearnedIpAddrAgingMethod = _AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 35),
    _AdGenEthernetDslamFlowLearnedIpAddrAgingMethod_Type()
)
adGenEthernetDslamFlowLearnedIpAddrAgingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowLearnedIpAddrAgingMethod.setStatus("current")


class _AdGenEthernetDslamFlowIgmpProcessing_Type(Integer32):
    """Custom type adGenEthernetDslamFlowIgmpProcessing based on Integer32"""
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
        *(("block", 1),
          ("forward", 2),
          ("snooping", 3),
          ("proxy", 4),
          ("notApplicable", 5),
          ("transparent", 6),
          ("forking", 7))
    )


_AdGenEthernetDslamFlowIgmpProcessing_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowIgmpProcessing_Object = MibTableColumn
adGenEthernetDslamFlowIgmpProcessing = _AdGenEthernetDslamFlowIgmpProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 36),
    _AdGenEthernetDslamFlowIgmpProcessing_Type()
)
adGenEthernetDslamFlowIgmpProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIgmpProcessing.setStatus("current")


class _AdGenEthernetDslamFlowIgmpVersion_Type(Integer32):
    """Custom type adGenEthernetDslamFlowIgmpVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3),
          ("notApplicable", 4))
    )


_AdGenEthernetDslamFlowIgmpVersion_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowIgmpVersion_Object = MibTableColumn
adGenEthernetDslamFlowIgmpVersion = _AdGenEthernetDslamFlowIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 37),
    _AdGenEthernetDslamFlowIgmpVersion_Type()
)
adGenEthernetDslamFlowIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIgmpVersion.setStatus("current")


class _AdGenEthernetDslamFlowLastMemberQueryInterval_Type(Integer32):
    """Custom type adGenEthernetDslamFlowLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_AdGenEthernetDslamFlowLastMemberQueryInterval_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowLastMemberQueryInterval_Object = MibTableColumn
adGenEthernetDslamFlowLastMemberQueryInterval = _AdGenEthernetDslamFlowLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 38),
    _AdGenEthernetDslamFlowLastMemberQueryInterval_Type()
)
adGenEthernetDslamFlowLastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowLastMemberQueryInterval.setStatus("current")


class _AdGenEthernetDslamFlowLastMemberQueryCount_Type(Integer32):
    """Custom type adGenEthernetDslamFlowLastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenEthernetDslamFlowLastMemberQueryCount_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowLastMemberQueryCount_Object = MibTableColumn
adGenEthernetDslamFlowLastMemberQueryCount = _AdGenEthernetDslamFlowLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 39),
    _AdGenEthernetDslamFlowLastMemberQueryCount_Type()
)
adGenEthernetDslamFlowLastMemberQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowLastMemberQueryCount.setStatus("current")


class _AdGenEthernetDslamFlowImmediateLeave_Type(Integer32):
    """Custom type adGenEthernetDslamFlowImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowImmediateLeave_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowImmediateLeave_Object = MibTableColumn
adGenEthernetDslamFlowImmediateLeave = _AdGenEthernetDslamFlowImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 40),
    _AdGenEthernetDslamFlowImmediateLeave_Type()
)
adGenEthernetDslamFlowImmediateLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowImmediateLeave.setStatus("current")
_AdGenEthernetDslamFlowMaxAllowedMcastGroups_Type = Integer32
_AdGenEthernetDslamFlowMaxAllowedMcastGroups_Object = MibTableColumn
adGenEthernetDslamFlowMaxAllowedMcastGroups = _AdGenEthernetDslamFlowMaxAllowedMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 41),
    _AdGenEthernetDslamFlowMaxAllowedMcastGroups_Type()
)
adGenEthernetDslamFlowMaxAllowedMcastGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMaxAllowedMcastGroups.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPPPoERemoteId_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpPPPoERemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowDhcpPPPoERemoteId_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpPPPoERemoteId_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoERemoteId = _AdGenEthernetDslamFlowDhcpPPPoERemoteId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 42),
    _AdGenEthernetDslamFlowDhcpPPPoERemoteId_Type()
)
adGenEthernetDslamFlowDhcpPPPoERemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoERemoteId.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics = _AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 43),
    _AdGenEthernetDslamFlowDhcpPPPoELoopCharacteristics_Type()
)
adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat = _AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 44),
    _AdGenEthernetDslamFlowDhcpPPPoECircuitIdFormat_Type()
)
adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat.setStatus("current")
_AdGenEthernetDslamFlowPPPoASessionTimeout_Type = Integer32
_AdGenEthernetDslamFlowPPPoASessionTimeout_Object = MibTableColumn
adGenEthernetDslamFlowPPPoASessionTimeout = _AdGenEthernetDslamFlowPPPoASessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 45),
    _AdGenEthernetDslamFlowPPPoASessionTimeout_Type()
)
adGenEthernetDslamFlowPPPoASessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowPPPoASessionTimeout.setStatus("current")
_AdGenEthernetDslamFlowInterfaceIfIndex_Type = Integer32
_AdGenEthernetDslamFlowInterfaceIfIndex_Object = MibTableColumn
adGenEthernetDslamFlowInterfaceIfIndex = _AdGenEthernetDslamFlowInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 46),
    _AdGenEthernetDslamFlowInterfaceIfIndex_Type()
)
adGenEthernetDslamFlowInterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowInterfaceIfIndex.setStatus("current")
_AdGenEthernetDslamFlowInterfaceLogicalIndex_Type = Integer32
_AdGenEthernetDslamFlowInterfaceLogicalIndex_Object = MibTableColumn
adGenEthernetDslamFlowInterfaceLogicalIndex = _AdGenEthernetDslamFlowInterfaceLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 47),
    _AdGenEthernetDslamFlowInterfaceLogicalIndex_Type()
)
adGenEthernetDslamFlowInterfaceLogicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowInterfaceLogicalIndex.setStatus("current")
_AdGenEthernetDslamFlowLastErrorString_Type = DisplayString
_AdGenEthernetDslamFlowLastErrorString_Object = MibTableColumn
adGenEthernetDslamFlowLastErrorString = _AdGenEthernetDslamFlowLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 48),
    _AdGenEthernetDslamFlowLastErrorString_Type()
)
adGenEthernetDslamFlowLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowLastErrorString.setStatus("current")
_AdGenEthernetDslamFlowRowStatus_Type = RowStatus
_AdGenEthernetDslamFlowRowStatus_Object = MibTableColumn
adGenEthernetDslamFlowRowStatus = _AdGenEthernetDslamFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 49),
    _AdGenEthernetDslamFlowRowStatus_Type()
)
adGenEthernetDslamFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRowStatus.setStatus("current")
_AdGenEthernetDslamFlowNetworkIngressPolicer_Type = Integer32
_AdGenEthernetDslamFlowNetworkIngressPolicer_Object = MibTableColumn
adGenEthernetDslamFlowNetworkIngressPolicer = _AdGenEthernetDslamFlowNetworkIngressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 50),
    _AdGenEthernetDslamFlowNetworkIngressPolicer_Type()
)
adGenEthernetDslamFlowNetworkIngressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkIngressPolicer.setStatus("current")


class _AdGenEthernetDslamFlowUpstreamDiscard_Type(Integer32):
    """Custom type adGenEthernetDslamFlowUpstreamDiscard based on Integer32"""
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


_AdGenEthernetDslamFlowUpstreamDiscard_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowUpstreamDiscard_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamDiscard = _AdGenEthernetDslamFlowUpstreamDiscard_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 51),
    _AdGenEthernetDslamFlowUpstreamDiscard_Type()
)
adGenEthernetDslamFlowUpstreamDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamDiscard.setStatus("current")
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Type = Integer32
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Object = MibTableColumn
adGenEthernetDslamFlowMaxAllowedMulticastBandwidth = _AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 53),
    _AdGenEthernetDslamFlowMaxAllowedMulticastBandwidth_Type()
)
adGenEthernetDslamFlowMaxAllowedMulticastBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMaxAllowedMulticastBandwidth.setStatus("current")


class _AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Type(Integer32):
    """Custom type adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable based on Integer32"""
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


_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Object = MibTableColumn
adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable = _AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 54),
    _AdGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable_Type()
)
adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable.setStatus("current")


class _AdGenEthernetDslamFlowProfileName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowProfileName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowProfileName_Object = MibTableColumn
adGenEthernetDslamFlowProfileName = _AdGenEthernetDslamFlowProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 55),
    _AdGenEthernetDslamFlowProfileName_Type()
)
adGenEthernetDslamFlowProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileName.setStatus("current")


class _AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Type(Integer32):
    """Custom type adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable based on Integer32"""
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


_AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Object = MibTableColumn
adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable = _AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 56),
    _AdGenEthernetDslamFlowMaxAllowedMcastGroupsEnable_Type()
)
adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable.setStatus("current")
_AdGenEthernetDslamFlowNetworkIngressDSCPList_Type = DisplayString
_AdGenEthernetDslamFlowNetworkIngressDSCPList_Object = MibTableColumn
adGenEthernetDslamFlowNetworkIngressDSCPList = _AdGenEthernetDslamFlowNetworkIngressDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 57),
    _AdGenEthernetDslamFlowNetworkIngressDSCPList_Type()
)
adGenEthernetDslamFlowNetworkIngressDSCPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNetworkIngressDSCPList.setStatus("current")
_AdGenEthernetDslamFlowCustomerIngressDSCPList_Type = DisplayString
_AdGenEthernetDslamFlowCustomerIngressDSCPList_Object = MibTableColumn
adGenEthernetDslamFlowCustomerIngressDSCPList = _AdGenEthernetDslamFlowCustomerIngressDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 58),
    _AdGenEthernetDslamFlowCustomerIngressDSCPList_Type()
)
adGenEthernetDslamFlowCustomerIngressDSCPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowCustomerIngressDSCPList.setStatus("current")
_AdGenEthernetDslamFlowIgmpRouterIP_Type = IpAddress
_AdGenEthernetDslamFlowIgmpRouterIP_Object = MibTableColumn
adGenEthernetDslamFlowIgmpRouterIP = _AdGenEthernetDslamFlowIgmpRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 59),
    _AdGenEthernetDslamFlowIgmpRouterIP_Type()
)
adGenEthernetDslamFlowIgmpRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIgmpRouterIP.setStatus("current")


class _AdGenEthernetDslamFlowActivationStatus_Type(Integer32):
    """Custom type adGenEthernetDslamFlowActivationStatus based on Integer32"""
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
        *(("notActivated", 1),
          ("inProgress", 2),
          ("active", 3),
          ("error", 4))
    )


_AdGenEthernetDslamFlowActivationStatus_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowActivationStatus_Object = MibTableColumn
adGenEthernetDslamFlowActivationStatus = _AdGenEthernetDslamFlowActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 60),
    _AdGenEthernetDslamFlowActivationStatus_Type()
)
adGenEthernetDslamFlowActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowActivationStatus.setStatus("current")


class _AdGenEthernetDslamFlowARPProcessing_Type(Integer32):
    """Custom type adGenEthernetDslamFlowARPProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("proxy", 2),
          ("transparent", 3))
    )


_AdGenEthernetDslamFlowARPProcessing_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowARPProcessing_Object = MibTableColumn
adGenEthernetDslamFlowARPProcessing = _AdGenEthernetDslamFlowARPProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 61),
    _AdGenEthernetDslamFlowARPProcessing_Type()
)
adGenEthernetDslamFlowARPProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowARPProcessing.setStatus("current")


class _AdGenEthernetDslamFlowPPPoEProcessing_Type(Integer32):
    """Custom type adGenEthernetDslamFlowPPPoEProcessing based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3),
          ("transparent", 4))
    )


_AdGenEthernetDslamFlowPPPoEProcessing_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowPPPoEProcessing_Object = MibTableColumn
adGenEthernetDslamFlowPPPoEProcessing = _AdGenEthernetDslamFlowPPPoEProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 62),
    _AdGenEthernetDslamFlowPPPoEProcessing_Type()
)
adGenEthernetDslamFlowPPPoEProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowPPPoEProcessing.setStatus("current")
_AdGenEthernetDslamFlowSubscriberIpRowCreateError_Type = DisplayString
_AdGenEthernetDslamFlowSubscriberIpRowCreateError_Object = MibTableColumn
adGenEthernetDslamFlowSubscriberIpRowCreateError = _AdGenEthernetDslamFlowSubscriberIpRowCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 63),
    _AdGenEthernetDslamFlowSubscriberIpRowCreateError_Type()
)
adGenEthernetDslamFlowSubscriberIpRowCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowSubscriberIpRowCreateError.setStatus("current")
_AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Type = Integer32
_AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoEVendorNumber = _AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 64),
    _AdGenEthernetDslamFlowDhcpPPPoEVendorNumber_Type()
)
adGenEthernetDslamFlowDhcpPPPoEVendorNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoEVendorNumber.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat = _AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 65),
    _AdGenEthernetDslamFlowDhcpPPPoEVendorIdFormat_Type()
)
adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat.setStatus("current")


class _AdGenEthernetDslamFlowEvcName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowEvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEthernetDslamFlowEvcName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowEvcName_Object = MibTableColumn
adGenEthernetDslamFlowEvcName = _AdGenEthernetDslamFlowEvcName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 66),
    _AdGenEthernetDslamFlowEvcName_Type()
)
adGenEthernetDslamFlowEvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowEvcName.setStatus("current")


class _AdGenEthernetDslamFlowEvcRoot_Type(Integer32):
    """Custom type adGenEthernetDslamFlowEvcRoot based on Integer32"""
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


_AdGenEthernetDslamFlowEvcRoot_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowEvcRoot_Object = MibTableColumn
adGenEthernetDslamFlowEvcRoot = _AdGenEthernetDslamFlowEvcRoot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 67),
    _AdGenEthernetDslamFlowEvcRoot_Type()
)
adGenEthernetDslamFlowEvcRoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowEvcRoot.setStatus("current")


class _AdGenEthernetDslamFlowDhcpv6Mode_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpv6Mode based on Integer32"""
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
        *(("authenticate", 1),
          ("block", 2),
          ("transparent", 3),
          ("snoop", 4),
          ("sameAsDhcpv4", 5))
    )


_AdGenEthernetDslamFlowDhcpv6Mode_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpv6Mode_Object = MibTableColumn
adGenEthernetDslamFlowDhcpv6Mode = _AdGenEthernetDslamFlowDhcpv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 68),
    _AdGenEthernetDslamFlowDhcpv6Mode_Type()
)
adGenEthernetDslamFlowDhcpv6Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpv6Mode.setStatus("current")


class _AdGenEthernetDslamFlowDhcpv6RelayAgent_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpv6RelayAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("sameAsDhcpv4", 3))
    )


_AdGenEthernetDslamFlowDhcpv6RelayAgent_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpv6RelayAgent_Object = MibTableColumn
adGenEthernetDslamFlowDhcpv6RelayAgent = _AdGenEthernetDslamFlowDhcpv6RelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 69),
    _AdGenEthernetDslamFlowDhcpv6RelayAgent_Type()
)
adGenEthernetDslamFlowDhcpv6RelayAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpv6RelayAgent.setStatus("current")


class _AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpv6RelayAgentTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Object = MibTableColumn
adGenEthernetDslamFlowDhcpv6RelayAgentTrusted = _AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 70),
    _AdGenEthernetDslamFlowDhcpv6RelayAgentTrusted_Type()
)
adGenEthernetDslamFlowDhcpv6RelayAgentTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpv6RelayAgentTrusted.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat = _AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 71),
    _AdGenEthernetDslamFlowDhcpPPPoERemoteIdFormat_Type()
)
adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat.setStatus("current")


class _AdGenEthernetDslamFlowDownstreamQosMapProfile_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowDownstreamQosMapProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenEthernetDslamFlowDownstreamQosMapProfile_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowDownstreamQosMapProfile_Object = MibTableColumn
adGenEthernetDslamFlowDownstreamQosMapProfile = _AdGenEthernetDslamFlowDownstreamQosMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 72),
    _AdGenEthernetDslamFlowDownstreamQosMapProfile_Type()
)
adGenEthernetDslamFlowDownstreamQosMapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDownstreamQosMapProfile.setStatus("current")


class _AdGenEthernetDslamFlowUpstreamChannel_Type(Integer32):
    """Custom type adGenEthernetDslamFlowUpstreamChannel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AdGenEthernetDslamFlowUpstreamChannel_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowUpstreamChannel_Object = MibTableColumn
adGenEthernetDslamFlowUpstreamChannel = _AdGenEthernetDslamFlowUpstreamChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 73),
    _AdGenEthernetDslamFlowUpstreamChannel_Type()
)
adGenEthernetDslamFlowUpstreamChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowUpstreamChannel.setStatus("current")


class _AdGenEthernetDslamFlowDhcpv6CurrMode_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpv6CurrMode based on Integer32"""
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
        *(("authenticate", 1),
          ("block", 2),
          ("transparent", 3),
          ("snoop", 4))
    )


_AdGenEthernetDslamFlowDhcpv6CurrMode_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpv6CurrMode_Object = MibTableColumn
adGenEthernetDslamFlowDhcpv6CurrMode = _AdGenEthernetDslamFlowDhcpv6CurrMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 74),
    _AdGenEthernetDslamFlowDhcpv6CurrMode_Type()
)
adGenEthernetDslamFlowDhcpv6CurrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpv6CurrMode.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert = _AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 75),
    _AdGenEthernetDslamFlowDhcpPPPoEVendorIdInsert_Type()
)
adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert.setStatus("current")
_AdGenEthernetDslamFlowMatchSourceMacList_Type = OctetString
_AdGenEthernetDslamFlowMatchSourceMacList_Object = MibTableColumn
adGenEthernetDslamFlowMatchSourceMacList = _AdGenEthernetDslamFlowMatchSourceMacList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 76),
    _AdGenEthernetDslamFlowMatchSourceMacList_Type()
)
adGenEthernetDslamFlowMatchSourceMacList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMatchSourceMacList.setStatus("current")
_AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Type = DisplayString
_AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Object = MibTableColumn
adGenEthernetDslamFlowMatchSourceMacLastErrorString = _AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 77),
    _AdGenEthernetDslamFlowMatchSourceMacLastErrorString_Type()
)
adGenEthernetDslamFlowMatchSourceMacLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMatchSourceMacLastErrorString.setStatus("current")


class _AdGenEthernetDslamFlowMatchNonIp_Type(TruthValue):
    """Custom type adGenEthernetDslamFlowMatchNonIp based on TruthValue"""
    defaultValue = 2


_AdGenEthernetDslamFlowMatchNonIp_Type.__name__ = "TruthValue"
_AdGenEthernetDslamFlowMatchNonIp_Object = MibTableColumn
adGenEthernetDslamFlowMatchNonIp = _AdGenEthernetDslamFlowMatchNonIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 2, 1, 78),
    _AdGenEthernetDslamFlowMatchNonIp_Type()
)
adGenEthernetDslamFlowMatchNonIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMatchNonIp.setStatus("current")
_AdGenEthernetDslamFlowIndexNextTable_Object = MibTable
adGenEthernetDslamFlowIndexNextTable = _AdGenEthernetDslamFlowIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 3)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIndexNextTable.setStatus("current")
_AdGenEthernetDslamFlowIndexNextEntry_Object = MibTableRow
adGenEthernetDslamFlowIndexNextEntry = _AdGenEthernetDslamFlowIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 3, 1)
)
adGenEthernetDslamFlowIndexNextEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIndexNextEntry.setStatus("current")
_AdGenEthernetDslamFlowIndexNext_Type = Integer32
_AdGenEthernetDslamFlowIndexNext_Object = MibTableColumn
adGenEthernetDslamFlowIndexNext = _AdGenEthernetDslamFlowIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 3, 1, 1),
    _AdGenEthernetDslamFlowIndexNext_Type()
)
adGenEthernetDslamFlowIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowIndexNext.setStatus("current")
_AdGenEthernetDslamFlowProfilesTable_Object = MibTable
adGenEthernetDslamFlowProfilesTable = _AdGenEthernetDslamFlowProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesTable.setStatus("current")
_AdGenEthernetDslamFlowProfilesEntry_Object = MibTableRow
adGenEthernetDslamFlowProfilesEntry = _AdGenEthernetDslamFlowProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1)
)
adGenEthernetDslamFlowProfilesEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesEntry.setStatus("current")
_AdGenEthernetDslamFlowProfileIndex_Type = Integer32
_AdGenEthernetDslamFlowProfileIndex_Object = MibTableColumn
adGenEthernetDslamFlowProfileIndex = _AdGenEthernetDslamFlowProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 1),
    _AdGenEthernetDslamFlowProfileIndex_Type()
)
adGenEthernetDslamFlowProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileIndex.setStatus("current")


class _AdGenEthernetDslamFlowProfileAlias_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowProfileAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowProfileAlias_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowProfileAlias_Object = MibTableColumn
adGenEthernetDslamFlowProfileAlias = _AdGenEthernetDslamFlowProfileAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 2),
    _AdGenEthernetDslamFlowProfileAlias_Type()
)
adGenEthernetDslamFlowProfileAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileAlias.setStatus("current")


class _AdGenEthernetDslamFlowProfileCIR_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AdGenEthernetDslamFlowProfileCIR_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileCIR_Object = MibTableColumn
adGenEthernetDslamFlowProfileCIR = _AdGenEthernetDslamFlowProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 3),
    _AdGenEthernetDslamFlowProfileCIR_Type()
)
adGenEthernetDslamFlowProfileCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileCIR.setStatus("current")


class _AdGenEthernetDslamFlowProfileCBS_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AdGenEthernetDslamFlowProfileCBS_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileCBS_Object = MibTableColumn
adGenEthernetDslamFlowProfileCBS = _AdGenEthernetDslamFlowProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 4),
    _AdGenEthernetDslamFlowProfileCBS_Type()
)
adGenEthernetDslamFlowProfileCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileCBS.setStatus("current")


class _AdGenEthernetDslamFlowProfileEIR_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileEIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AdGenEthernetDslamFlowProfileEIR_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileEIR_Object = MibTableColumn
adGenEthernetDslamFlowProfileEIR = _AdGenEthernetDslamFlowProfileEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 5),
    _AdGenEthernetDslamFlowProfileEIR_Type()
)
adGenEthernetDslamFlowProfileEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileEIR.setStatus("current")


class _AdGenEthernetDslamFlowProfileEBS_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AdGenEthernetDslamFlowProfileEBS_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileEBS_Object = MibTableColumn
adGenEthernetDslamFlowProfileEBS = _AdGenEthernetDslamFlowProfileEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 6),
    _AdGenEthernetDslamFlowProfileEBS_Type()
)
adGenEthernetDslamFlowProfileEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileEBS.setStatus("current")
_AdGenEthernetDslamFlowProfileLastErrorString_Type = DisplayString
_AdGenEthernetDslamFlowProfileLastErrorString_Object = MibTableColumn
adGenEthernetDslamFlowProfileLastErrorString = _AdGenEthernetDslamFlowProfileLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 7),
    _AdGenEthernetDslamFlowProfileLastErrorString_Type()
)
adGenEthernetDslamFlowProfileLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileLastErrorString.setStatus("current")
_AdGenEthernetDslamFlowProfileRowStatus_Type = RowStatus
_AdGenEthernetDslamFlowProfileRowStatus_Object = MibTableColumn
adGenEthernetDslamFlowProfileRowStatus = _AdGenEthernetDslamFlowProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 8),
    _AdGenEthernetDslamFlowProfileRowStatus_Type()
)
adGenEthernetDslamFlowProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileRowStatus.setStatus("current")


class _AdGenEthernetDslamFlowProfileActualCIR_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileActualCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AdGenEthernetDslamFlowProfileActualCIR_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileActualCIR_Object = MibTableColumn
adGenEthernetDslamFlowProfileActualCIR = _AdGenEthernetDslamFlowProfileActualCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 9),
    _AdGenEthernetDslamFlowProfileActualCIR_Type()
)
adGenEthernetDslamFlowProfileActualCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileActualCIR.setStatus("current")


class _AdGenEthernetDslamFlowProfileActualCBS_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileActualCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AdGenEthernetDslamFlowProfileActualCBS_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileActualCBS_Object = MibTableColumn
adGenEthernetDslamFlowProfileActualCBS = _AdGenEthernetDslamFlowProfileActualCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 10),
    _AdGenEthernetDslamFlowProfileActualCBS_Type()
)
adGenEthernetDslamFlowProfileActualCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileActualCBS.setStatus("current")


class _AdGenEthernetDslamFlowProfileActualEIR_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileActualEIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_AdGenEthernetDslamFlowProfileActualEIR_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileActualEIR_Object = MibTableColumn
adGenEthernetDslamFlowProfileActualEIR = _AdGenEthernetDslamFlowProfileActualEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 11),
    _AdGenEthernetDslamFlowProfileActualEIR_Type()
)
adGenEthernetDslamFlowProfileActualEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileActualEIR.setStatus("current")


class _AdGenEthernetDslamFlowProfileActualEBS_Type(Integer32):
    """Custom type adGenEthernetDslamFlowProfileActualEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_AdGenEthernetDslamFlowProfileActualEBS_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowProfileActualEBS_Object = MibTableColumn
adGenEthernetDslamFlowProfileActualEBS = _AdGenEthernetDslamFlowProfileActualEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 4, 1, 12),
    _AdGenEthernetDslamFlowProfileActualEBS_Type()
)
adGenEthernetDslamFlowProfileActualEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileActualEBS.setStatus("current")
_AdGenEthernetDslamFlowNameLookupTable_Object = MibTable
adGenEthernetDslamFlowNameLookupTable = _AdGenEthernetDslamFlowNameLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 5)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNameLookupTable.setStatus("current")
_AdGenEthernetDslamFlowNameLookupEntry_Object = MibTableRow
adGenEthernetDslamFlowNameLookupEntry = _AdGenEthernetDslamFlowNameLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 5, 1)
)
adGenEthernetDslamFlowNameLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowNameLookupName"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNameLookupEntry.setStatus("current")


class _AdGenEthernetDslamFlowNameLookupName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowNameLookupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowNameLookupName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowNameLookupName_Object = MibTableColumn
adGenEthernetDslamFlowNameLookupName = _AdGenEthernetDslamFlowNameLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 5, 1, 1),
    _AdGenEthernetDslamFlowNameLookupName_Type()
)
adGenEthernetDslamFlowNameLookupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNameLookupName.setStatus("current")
_AdGenEthernetDslamFlowNameLookupIndex_Type = Integer32
_AdGenEthernetDslamFlowNameLookupIndex_Object = MibTableColumn
adGenEthernetDslamFlowNameLookupIndex = _AdGenEthernetDslamFlowNameLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 5, 1, 2),
    _AdGenEthernetDslamFlowNameLookupIndex_Type()
)
adGenEthernetDslamFlowNameLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowNameLookupIndex.setStatus("current")
_AdGenEthernetDslamFlowShaperTable_Object = MibTable
adGenEthernetDslamFlowShaperTable = _AdGenEthernetDslamFlowShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperTable.setStatus("current")
_AdGenEthernetDslamFlowShaperEntry_Object = MibTableRow
adGenEthernetDslamFlowShaperEntry = _AdGenEthernetDslamFlowShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1)
)
adGenEthernetDslamFlowShaperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowShaperInterfaceLogicalIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowShaperPrioritySet"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperEntry.setStatus("current")
_AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Type = Integer32
_AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Object = MibTableColumn
adGenEthernetDslamFlowShaperInterfaceLogicalIndex = _AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 1),
    _AdGenEthernetDslamFlowShaperInterfaceLogicalIndex_Type()
)
adGenEthernetDslamFlowShaperInterfaceLogicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperInterfaceLogicalIndex.setStatus("current")
_AdGenEthernetDslamFlowShaperPrioritySet_Type = Integer32
_AdGenEthernetDslamFlowShaperPrioritySet_Object = MibTableColumn
adGenEthernetDslamFlowShaperPrioritySet = _AdGenEthernetDslamFlowShaperPrioritySet_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 2),
    _AdGenEthernetDslamFlowShaperPrioritySet_Type()
)
adGenEthernetDslamFlowShaperPrioritySet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperPrioritySet.setStatus("current")
_AdGenEthernetDslamFlowShaperRate_Type = Integer32
_AdGenEthernetDslamFlowShaperRate_Object = MibTableColumn
adGenEthernetDslamFlowShaperRate = _AdGenEthernetDslamFlowShaperRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 3),
    _AdGenEthernetDslamFlowShaperRate_Type()
)
adGenEthernetDslamFlowShaperRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperRate.setStatus("current")
_AdGenEthernetDslamFlowShaperRowStatus_Type = RowStatus
_AdGenEthernetDslamFlowShaperRowStatus_Object = MibTableColumn
adGenEthernetDslamFlowShaperRowStatus = _AdGenEthernetDslamFlowShaperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 4),
    _AdGenEthernetDslamFlowShaperRowStatus_Type()
)
adGenEthernetDslamFlowShaperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperRowStatus.setStatus("current")
_AdGenEthernetDslamFlowShaperLastErrorString_Type = DisplayString
_AdGenEthernetDslamFlowShaperLastErrorString_Object = MibTableColumn
adGenEthernetDslamFlowShaperLastErrorString = _AdGenEthernetDslamFlowShaperLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 5),
    _AdGenEthernetDslamFlowShaperLastErrorString_Type()
)
adGenEthernetDslamFlowShaperLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLastErrorString.setStatus("current")


class _AdGenEthernetDslamFlowShaperAlias_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowShaperAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowShaperAlias_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowShaperAlias_Object = MibTableColumn
adGenEthernetDslamFlowShaperAlias = _AdGenEthernetDslamFlowShaperAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 6),
    _AdGenEthernetDslamFlowShaperAlias_Type()
)
adGenEthernetDslamFlowShaperAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperAlias.setStatus("current")


class _AdGenEthernetDslamFlowShaperOperationalStatus_Type(Integer32):
    """Custom type adGenEthernetDslamFlowShaperOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shaperNotRunning", 1),
          ("shaperRunning", 2))
    )


_AdGenEthernetDslamFlowShaperOperationalStatus_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowShaperOperationalStatus_Object = MibTableColumn
adGenEthernetDslamFlowShaperOperationalStatus = _AdGenEthernetDslamFlowShaperOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 7),
    _AdGenEthernetDslamFlowShaperOperationalStatus_Type()
)
adGenEthernetDslamFlowShaperOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperOperationalStatus.setStatus("current")
_AdGenEthernetDslamFlowShaperBurstSize_Type = Integer32
_AdGenEthernetDslamFlowShaperBurstSize_Object = MibTableColumn
adGenEthernetDslamFlowShaperBurstSize = _AdGenEthernetDslamFlowShaperBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 8),
    _AdGenEthernetDslamFlowShaperBurstSize_Type()
)
adGenEthernetDslamFlowShaperBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperBurstSize.setStatus("current")
_AdGenEthernetDslamFlowShaperFixedRate_Type = Integer32
_AdGenEthernetDslamFlowShaperFixedRate_Object = MibTableColumn
adGenEthernetDslamFlowShaperFixedRate = _AdGenEthernetDslamFlowShaperFixedRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 9),
    _AdGenEthernetDslamFlowShaperFixedRate_Type()
)
adGenEthernetDslamFlowShaperFixedRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperFixedRate.setStatus("current")
_AdGenEthernetDslamFlowShaperAssuredRate_Type = Integer32
_AdGenEthernetDslamFlowShaperAssuredRate_Object = MibTableColumn
adGenEthernetDslamFlowShaperAssuredRate = _AdGenEthernetDslamFlowShaperAssuredRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 10),
    _AdGenEthernetDslamFlowShaperAssuredRate_Type()
)
adGenEthernetDslamFlowShaperAssuredRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperAssuredRate.setStatus("current")


class _AdGenEthernetDslamFlowShaperDownstreamMinRate_Type(Integer32):
    """Custom type adGenEthernetDslamFlowShaperDownstreamMinRate based on Integer32"""
    defaultValue = 0


_AdGenEthernetDslamFlowShaperDownstreamMinRate_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowShaperDownstreamMinRate_Object = MibTableColumn
adGenEthernetDslamFlowShaperDownstreamMinRate = _AdGenEthernetDslamFlowShaperDownstreamMinRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 6, 1, 11),
    _AdGenEthernetDslamFlowShaperDownstreamMinRate_Type()
)
adGenEthernetDslamFlowShaperDownstreamMinRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperDownstreamMinRate.setStatus("current")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperDownstreamMinRate.setUnits("kbps")
_AdGenSubscriberAccessStaticIpTable_Object = MibTable
adGenSubscriberAccessStaticIpTable = _AdGenSubscriberAccessStaticIpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7)
)
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpTable.setStatus("current")
_AdGenSubscriberAccessStaticIpEntry_Object = MibTableRow
adGenSubscriberAccessStaticIpEntry = _AdGenSubscriberAccessStaticIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1)
)
adGenSubscriberAccessStaticIpEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenSubscriberAccessStaticIpAddress"),
)
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpEntry.setStatus("current")
_AdGenSubscriberAccessStaticIpAddress_Type = IpAddress
_AdGenSubscriberAccessStaticIpAddress_Object = MibTableColumn
adGenSubscriberAccessStaticIpAddress = _AdGenSubscriberAccessStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1, 1),
    _AdGenSubscriberAccessStaticIpAddress_Type()
)
adGenSubscriberAccessStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpAddress.setStatus("current")
_AdGenSubscriberAccessStaticIpMacAddress_Type = PhysAddress
_AdGenSubscriberAccessStaticIpMacAddress_Object = MibTableColumn
adGenSubscriberAccessStaticIpMacAddress = _AdGenSubscriberAccessStaticIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1, 2),
    _AdGenSubscriberAccessStaticIpMacAddress_Type()
)
adGenSubscriberAccessStaticIpMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpMacAddress.setStatus("current")
_AdGenSubscriberAccessStaticIpGatewayIp_Type = IpAddress
_AdGenSubscriberAccessStaticIpGatewayIp_Object = MibTableColumn
adGenSubscriberAccessStaticIpGatewayIp = _AdGenSubscriberAccessStaticIpGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1, 3),
    _AdGenSubscriberAccessStaticIpGatewayIp_Type()
)
adGenSubscriberAccessStaticIpGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpGatewayIp.setStatus("current")
_AdGenSubscriberAccessStaticIpGatewayMac_Type = PhysAddress
_AdGenSubscriberAccessStaticIpGatewayMac_Object = MibTableColumn
adGenSubscriberAccessStaticIpGatewayMac = _AdGenSubscriberAccessStaticIpGatewayMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1, 4),
    _AdGenSubscriberAccessStaticIpGatewayMac_Type()
)
adGenSubscriberAccessStaticIpGatewayMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpGatewayMac.setStatus("current")
_AdGenSubscriberAccessStaticIpLastErrorString_Type = DisplayString
_AdGenSubscriberAccessStaticIpLastErrorString_Object = MibTableColumn
adGenSubscriberAccessStaticIpLastErrorString = _AdGenSubscriberAccessStaticIpLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1, 5),
    _AdGenSubscriberAccessStaticIpLastErrorString_Type()
)
adGenSubscriberAccessStaticIpLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpLastErrorString.setStatus("current")
_AdGenSubscriberAccessStaticIpRowStatus_Type = RowStatus
_AdGenSubscriberAccessStaticIpRowStatus_Object = MibTableColumn
adGenSubscriberAccessStaticIpRowStatus = _AdGenSubscriberAccessStaticIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 7, 1, 6),
    _AdGenSubscriberAccessStaticIpRowStatus_Type()
)
adGenSubscriberAccessStaticIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenSubscriberAccessStaticIpRowStatus.setStatus("current")
_AdGenEthernetDslamFlowProfilesIndexNextTable_Object = MibTable
adGenEthernetDslamFlowProfilesIndexNextTable = _AdGenEthernetDslamFlowProfilesIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 8)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesIndexNextTable.setStatus("current")
_AdGenEthernetDslamFlowProfilesIndexNextEntry_Object = MibTableRow
adGenEthernetDslamFlowProfilesIndexNextEntry = _AdGenEthernetDslamFlowProfilesIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 8, 1)
)
adGenEthernetDslamFlowProfilesIndexNextEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesIndexNextEntry.setStatus("current")
_AdGenEthernetDslamFlowProfilesIndexNext_Type = Integer32
_AdGenEthernetDslamFlowProfilesIndexNext_Object = MibTableColumn
adGenEthernetDslamFlowProfilesIndexNext = _AdGenEthernetDslamFlowProfilesIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 8, 1, 1),
    _AdGenEthernetDslamFlowProfilesIndexNext_Type()
)
adGenEthernetDslamFlowProfilesIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesIndexNext.setStatus("current")
_AdGenEthernetDslamFlowProfilesLookupTable_Object = MibTable
adGenEthernetDslamFlowProfilesLookupTable = _AdGenEthernetDslamFlowProfilesLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 9)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesLookupTable.setStatus("current")
_AdGenEthernetDslamFlowProfilesLookupEntry_Object = MibTableRow
adGenEthernetDslamFlowProfilesLookupEntry = _AdGenEthernetDslamFlowProfilesLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 9, 1)
)
adGenEthernetDslamFlowProfilesLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowProfileLookupAlias"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfilesLookupEntry.setStatus("current")


class _AdGenEthernetDslamFlowProfileLookupAlias_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowProfileLookupAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowProfileLookupAlias_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowProfileLookupAlias_Object = MibTableColumn
adGenEthernetDslamFlowProfileLookupAlias = _AdGenEthernetDslamFlowProfileLookupAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 9, 1, 1),
    _AdGenEthernetDslamFlowProfileLookupAlias_Type()
)
adGenEthernetDslamFlowProfileLookupAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileLookupAlias.setStatus("current")
_AdGenEthernetDslamFlowProfileLookupIndex_Type = Integer32
_AdGenEthernetDslamFlowProfileLookupIndex_Object = MibTableColumn
adGenEthernetDslamFlowProfileLookupIndex = _AdGenEthernetDslamFlowProfileLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 9, 1, 2),
    _AdGenEthernetDslamFlowProfileLookupIndex_Type()
)
adGenEthernetDslamFlowProfileLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowProfileLookupIndex.setStatus("current")
_AdGenEthernetDslamFlowShaperLookupTable_Object = MibTable
adGenEthernetDslamFlowShaperLookupTable = _AdGenEthernetDslamFlowShaperLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 10)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLookupTable.setStatus("current")
_AdGenEthernetDslamFlowShaperLookupEntry_Object = MibTableRow
adGenEthernetDslamFlowShaperLookupEntry = _AdGenEthernetDslamFlowShaperLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 10, 1)
)
adGenEthernetDslamFlowShaperLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowShaperLookupAlias"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLookupEntry.setStatus("current")


class _AdGenEthernetDslamFlowShaperLookupAlias_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowShaperLookupAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowShaperLookupAlias_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowShaperLookupAlias_Object = MibTableColumn
adGenEthernetDslamFlowShaperLookupAlias = _AdGenEthernetDslamFlowShaperLookupAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 10, 1, 1),
    _AdGenEthernetDslamFlowShaperLookupAlias_Type()
)
adGenEthernetDslamFlowShaperLookupAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLookupAlias.setStatus("current")
_AdGenEthernetDslamFlowShaperLookupIfIndex_Type = Integer32
_AdGenEthernetDslamFlowShaperLookupIfIndex_Object = MibTableColumn
adGenEthernetDslamFlowShaperLookupIfIndex = _AdGenEthernetDslamFlowShaperLookupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 10, 1, 2),
    _AdGenEthernetDslamFlowShaperLookupIfIndex_Type()
)
adGenEthernetDslamFlowShaperLookupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLookupIfIndex.setStatus("current")
_AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Type = Integer32
_AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Object = MibTableColumn
adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex = _AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 10, 1, 3),
    _AdGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex_Type()
)
adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex.setStatus("current")
_AdGenEthernetDslamFlowShaperLookupPrioritySet_Type = Integer32
_AdGenEthernetDslamFlowShaperLookupPrioritySet_Object = MibTableColumn
adGenEthernetDslamFlowShaperLookupPrioritySet = _AdGenEthernetDslamFlowShaperLookupPrioritySet_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 10, 1, 4),
    _AdGenEthernetDslamFlowShaperLookupPrioritySet_Type()
)
adGenEthernetDslamFlowShaperLookupPrioritySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperLookupPrioritySet.setStatus("current")
_AdGenEthernetDslamFlowRev2Table_Object = MibTable
adGenEthernetDslamFlowRev2Table = _AdGenEthernetDslamFlowRev2Table_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Table.setStatus("current")
_AdGenEthernetDslamFlowRev2Entry_Object = MibTableRow
adGenEthernetDslamFlowRev2Entry = _AdGenEthernetDslamFlowRev2Entry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1)
)
adGenEthernetDslamFlowRev2Entry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowRev2Index"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Entry.setStatus("current")
_AdGenEthernetDslamFlowRev2Index_Type = Integer32
_AdGenEthernetDslamFlowRev2Index_Object = MibTableColumn
adGenEthernetDslamFlowRev2Index = _AdGenEthernetDslamFlowRev2Index_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 1),
    _AdGenEthernetDslamFlowRev2Index_Type()
)
adGenEthernetDslamFlowRev2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Index.setStatus("current")


class _AdGenEthernetDslamFlowRev2Name_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowRev2Name_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2Name_Object = MibTableColumn
adGenEthernetDslamFlowRev2Name = _AdGenEthernetDslamFlowRev2Name_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 2),
    _AdGenEthernetDslamFlowRev2Name_Type()
)
adGenEthernetDslamFlowRev2Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Name.setStatus("current")


class _AdGenEthernetDslamFlowRev2TrafficDirection_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2TrafficDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2),
          ("bidirectional", 3))
    )


_AdGenEthernetDslamFlowRev2TrafficDirection_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2TrafficDirection_Object = MibTableColumn
adGenEthernetDslamFlowRev2TrafficDirection = _AdGenEthernetDslamFlowRev2TrafficDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 3),
    _AdGenEthernetDslamFlowRev2TrafficDirection_Type()
)
adGenEthernetDslamFlowRev2TrafficDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2TrafficDirection.setStatus("current")


class _AdGenEthernetDslamFlowRev2NetworkSTag_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2NetworkSTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_AdGenEthernetDslamFlowRev2NetworkSTag_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2NetworkSTag_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkSTag = _AdGenEthernetDslamFlowRev2NetworkSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 4),
    _AdGenEthernetDslamFlowRev2NetworkSTag_Type()
)
adGenEthernetDslamFlowRev2NetworkSTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkSTag.setStatus("current")


class _AdGenEthernetDslamFlowRev2NetworkCTag_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2NetworkCTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4096),
    )


_AdGenEthernetDslamFlowRev2NetworkCTag_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2NetworkCTag_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkCTag = _AdGenEthernetDslamFlowRev2NetworkCTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 5),
    _AdGenEthernetDslamFlowRev2NetworkCTag_Type()
)
adGenEthernetDslamFlowRev2NetworkCTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkCTag.setStatus("current")


class _AdGenEthernetDslamFlowRev2CEVlan_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2CEVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4097),
    )


_AdGenEthernetDslamFlowRev2CEVlan_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2CEVlan_Object = MibTableColumn
adGenEthernetDslamFlowRev2CEVlan = _AdGenEthernetDslamFlowRev2CEVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 6),
    _AdGenEthernetDslamFlowRev2CEVlan_Type()
)
adGenEthernetDslamFlowRev2CEVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CEVlan.setStatus("current")
_AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Type = Integer32
_AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Object = MibTableColumn
adGenEthernetDslamFlowRev2DownstreamForwardingMode = _AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 7),
    _AdGenEthernetDslamFlowRev2DownstreamForwardingMode_Type()
)
adGenEthernetDslamFlowRev2DownstreamForwardingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DownstreamForwardingMode.setStatus("current")


class _AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2DownstreamPbitMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 1),
          ("marked", 2),
          ("mapped", 3))
    )


_AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Object = MibTableColumn
adGenEthernetDslamFlowRev2DownstreamPbitMethod = _AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 8),
    _AdGenEthernetDslamFlowRev2DownstreamPbitMethod_Type()
)
adGenEthernetDslamFlowRev2DownstreamPbitMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DownstreamPbitMethod.setStatus("current")


class _AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2DownstreamPbitMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Object = MibTableColumn
adGenEthernetDslamFlowRev2DownstreamPbitMarking = _AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 9),
    _AdGenEthernetDslamFlowRev2DownstreamPbitMarking_Type()
)
adGenEthernetDslamFlowRev2DownstreamPbitMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DownstreamPbitMarking.setStatus("current")
_AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Type = Integer32
_AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Object = MibTableColumn
adGenEthernetDslamFlowRev2DownstreamPbitMapping = _AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 10),
    _AdGenEthernetDslamFlowRev2DownstreamPbitMapping_Type()
)
adGenEthernetDslamFlowRev2DownstreamPbitMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DownstreamPbitMapping.setStatus("current")


class _AdGenEthernetDslamFlowRev2NetworkIngressPbit_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2NetworkIngressPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenEthernetDslamFlowRev2NetworkIngressPbit_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2NetworkIngressPbit_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressPbit = _AdGenEthernetDslamFlowRev2NetworkIngressPbit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 11),
    _AdGenEthernetDslamFlowRev2NetworkIngressPbit_Type()
)
adGenEthernetDslamFlowRev2NetworkIngressPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkIngressPbit.setStatus("current")
_AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Type = Integer32
_AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressEtherType = _AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 12),
    _AdGenEthernetDslamFlowRev2NetworkIngressEtherType_Type()
)
adGenEthernetDslamFlowRev2NetworkIngressEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkIngressEtherType.setStatus("current")


class _AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2NetworkIngressDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressDSCP = _AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 13),
    _AdGenEthernetDslamFlowRev2NetworkIngressDSCP_Type()
)
adGenEthernetDslamFlowRev2NetworkIngressDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkIngressDSCP.setStatus("current")
_AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Type = Integer32
_AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID = _AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 14),
    _AdGenEthernetDslamFlowRev2NetworkIngressIPProtocolID_Type()
)
adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID.setStatus("current")
_AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Type = Integer32
_AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamForwardingMode = _AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 15),
    _AdGenEthernetDslamFlowRev2UpstreamForwardingMode_Type()
)
adGenEthernetDslamFlowRev2UpstreamForwardingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamForwardingMode.setStatus("current")


class _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 1),
          ("marked", 2),
          ("mapped", 3))
    )


_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod = _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 16),
    _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMethod_Type()
)
adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod.setStatus("current")


class _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking = _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 17),
    _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMarking_Type()
)
adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking.setStatus("current")
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Type = Integer32
_AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping = _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 18),
    _AdGenEthernetDslamFlowRev2UpstreamSTagPbitMapping_Type()
)
adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping.setStatus("current")


class _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inherit", 1),
          ("marked", 2),
          ("mapped", 3))
    )


_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod = _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 19),
    _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMethod_Type()
)
adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod.setStatus("current")


class _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking = _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 20),
    _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMarking_Type()
)
adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking.setStatus("current")
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Type = Integer32
_AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping = _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 21),
    _AdGenEthernetDslamFlowRev2UpstreamCTagPbitMapping_Type()
)
adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping.setStatus("current")


class _AdGenEthernetDslamFlowRev2CustomerIngressPbit_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2CustomerIngressPbit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AdGenEthernetDslamFlowRev2CustomerIngressPbit_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2CustomerIngressPbit_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressPbit = _AdGenEthernetDslamFlowRev2CustomerIngressPbit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 22),
    _AdGenEthernetDslamFlowRev2CustomerIngressPbit_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressPbit.setStatus("current")
_AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Type = Integer32
_AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressEtherType = _AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 23),
    _AdGenEthernetDslamFlowRev2CustomerIngressEtherType_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressEtherType.setStatus("current")


class _AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2CustomerIngressDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressDSCP = _AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 24),
    _AdGenEthernetDslamFlowRev2CustomerIngressDSCP_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressDSCP.setStatus("current")
_AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Type = Integer32
_AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID = _AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 25),
    _AdGenEthernetDslamFlowRev2CustomerIngressIPProtocolID_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID.setStatus("current")


class _AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2CustomerIngressBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressBroadcast = _AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 26),
    _AdGenEthernetDslamFlowRev2CustomerIngressBroadcast_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressBroadcast.setStatus("current")


class _AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2CustomerIngressMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressMulticast = _AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 27),
    _AdGenEthernetDslamFlowRev2CustomerIngressMulticast_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressMulticast.setStatus("current")


class _AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2CustomerIngressUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressUnicast = _AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 28),
    _AdGenEthernetDslamFlowRev2CustomerIngressUnicast_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressUnicast.setStatus("current")
_AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Type = Integer32
_AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressPolicer = _AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 29),
    _AdGenEthernetDslamFlowRev2CustomerIngressPolicer_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressPolicer.setStatus("current")


class _AdGenEthernetDslamFlowRev2EncapsMode_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2EncapsMode based on Integer32"""
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
        *(("ipoe", 1),
          ("pppoe", 2),
          ("pppoa", 3),
          ("notApplicable", 4),
          ("atmoe", 5),
          ("pppoaVcMux", 6),
          ("autoDetect", 7),
          ("ethernet", 8))
    )


_AdGenEthernetDslamFlowRev2EncapsMode_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2EncapsMode_Object = MibTableColumn
adGenEthernetDslamFlowRev2EncapsMode = _AdGenEthernetDslamFlowRev2EncapsMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 30),
    _AdGenEthernetDslamFlowRev2EncapsMode_Type()
)
adGenEthernetDslamFlowRev2EncapsMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2EncapsMode.setStatus("current")


class _AdGenEthernetDslamFlowRev2ManualAddrAging_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2ManualAddrAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AdGenEthernetDslamFlowRev2ManualAddrAging_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2ManualAddrAging_Object = MibTableColumn
adGenEthernetDslamFlowRev2ManualAddrAging = _AdGenEthernetDslamFlowRev2ManualAddrAging_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 31),
    _AdGenEthernetDslamFlowRev2ManualAddrAging_Type()
)
adGenEthernetDslamFlowRev2ManualAddrAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2ManualAddrAging.setStatus("current")


class _AdGenEthernetDslamFlowRev2IntermedAgent_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2IntermedAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2IntermedAgent_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2IntermedAgent_Object = MibTableColumn
adGenEthernetDslamFlowRev2IntermedAgent = _AdGenEthernetDslamFlowRev2IntermedAgent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 32),
    _AdGenEthernetDslamFlowRev2IntermedAgent_Type()
)
adGenEthernetDslamFlowRev2IntermedAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IntermedAgent.setStatus("current")


class _AdGenEthernetDslamFlowRev2DhcpRelay_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2DhcpRelay based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3),
          ("transparent", 4),
          ("snoop", 5))
    )


_AdGenEthernetDslamFlowRev2DhcpRelay_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2DhcpRelay_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpRelay = _AdGenEthernetDslamFlowRev2DhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 33),
    _AdGenEthernetDslamFlowRev2DhcpRelay_Type()
)
adGenEthernetDslamFlowRev2DhcpRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpRelay.setStatus("current")


class _AdGenEthernetDslamFlowRev2Option82Insert_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2Option82Insert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2Option82Insert_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2Option82Insert_Object = MibTableColumn
adGenEthernetDslamFlowRev2Option82Insert = _AdGenEthernetDslamFlowRev2Option82Insert_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 34),
    _AdGenEthernetDslamFlowRev2Option82Insert_Type()
)
adGenEthernetDslamFlowRev2Option82Insert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Option82Insert.setStatus("current")


class _AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lease", 1),
          ("fixed", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Object = MibTableColumn
adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod = _AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 35),
    _AdGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod_Type()
)
adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod.setStatus("current")


class _AdGenEthernetDslamFlowRev2IgmpProcessing_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2IgmpProcessing based on Integer32"""
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
        *(("block", 1),
          ("forward", 2),
          ("snooping", 3),
          ("proxy", 4),
          ("notApplicable", 5),
          ("transparent", 6),
          ("forking", 7))
    )


_AdGenEthernetDslamFlowRev2IgmpProcessing_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2IgmpProcessing_Object = MibTableColumn
adGenEthernetDslamFlowRev2IgmpProcessing = _AdGenEthernetDslamFlowRev2IgmpProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 36),
    _AdGenEthernetDslamFlowRev2IgmpProcessing_Type()
)
adGenEthernetDslamFlowRev2IgmpProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IgmpProcessing.setStatus("current")


class _AdGenEthernetDslamFlowRev2IgmpVersion_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2IgmpVersion based on Integer32"""
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
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3),
          ("notApplicable", 4))
    )


_AdGenEthernetDslamFlowRev2IgmpVersion_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2IgmpVersion_Object = MibTableColumn
adGenEthernetDslamFlowRev2IgmpVersion = _AdGenEthernetDslamFlowRev2IgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 37),
    _AdGenEthernetDslamFlowRev2IgmpVersion_Type()
)
adGenEthernetDslamFlowRev2IgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IgmpVersion.setStatus("current")


class _AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2LastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Object = MibTableColumn
adGenEthernetDslamFlowRev2LastMemberQueryInterval = _AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 38),
    _AdGenEthernetDslamFlowRev2LastMemberQueryInterval_Type()
)
adGenEthernetDslamFlowRev2LastMemberQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2LastMemberQueryInterval.setStatus("current")


class _AdGenEthernetDslamFlowRev2LastMemberQueryCount_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2LastMemberQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdGenEthernetDslamFlowRev2LastMemberQueryCount_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2LastMemberQueryCount_Object = MibTableColumn
adGenEthernetDslamFlowRev2LastMemberQueryCount = _AdGenEthernetDslamFlowRev2LastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 39),
    _AdGenEthernetDslamFlowRev2LastMemberQueryCount_Type()
)
adGenEthernetDslamFlowRev2LastMemberQueryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2LastMemberQueryCount.setStatus("current")


class _AdGenEthernetDslamFlowRev2ImmediateLeave_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2ImmediateLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2ImmediateLeave_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2ImmediateLeave_Object = MibTableColumn
adGenEthernetDslamFlowRev2ImmediateLeave = _AdGenEthernetDslamFlowRev2ImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 40),
    _AdGenEthernetDslamFlowRev2ImmediateLeave_Type()
)
adGenEthernetDslamFlowRev2ImmediateLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2ImmediateLeave.setStatus("current")
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Type = Integer32
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Object = MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMcastGroups = _AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 41),
    _AdGenEthernetDslamFlowRev2MaxAllowedMcastGroups_Type()
)
adGenEthernetDslamFlowRev2MaxAllowedMcastGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MaxAllowedMcastGroups.setStatus("current")


class _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2DhcpPPPoERemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoERemoteId = _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 42),
    _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteId_Type()
)
adGenEthernetDslamFlowRev2DhcpPPPoERemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpPPPoERemoteId.setStatus("current")


class _AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3))
    )


_AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics = _AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 43),
    _AdGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics_Type()
)
adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics.setStatus("current")


class _AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat = _AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 44),
    _AdGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat_Type()
)
adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat.setStatus("current")
_AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Type = Integer32
_AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Object = MibTableColumn
adGenEthernetDslamFlowRev2PPPoASessionTimeout = _AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 45),
    _AdGenEthernetDslamFlowRev2PPPoASessionTimeout_Type()
)
adGenEthernetDslamFlowRev2PPPoASessionTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2PPPoASessionTimeout.setStatus("current")
_AdGenEthernetDslamFlowRev2InterfaceIfIndex_Type = Integer32
_AdGenEthernetDslamFlowRev2InterfaceIfIndex_Object = MibTableColumn
adGenEthernetDslamFlowRev2InterfaceIfIndex = _AdGenEthernetDslamFlowRev2InterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 46),
    _AdGenEthernetDslamFlowRev2InterfaceIfIndex_Type()
)
adGenEthernetDslamFlowRev2InterfaceIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2InterfaceIfIndex.setStatus("current")
_AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Type = Integer32
_AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Object = MibTableColumn
adGenEthernetDslamFlowRev2InterfaceLogicalIndex = _AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 47),
    _AdGenEthernetDslamFlowRev2InterfaceLogicalIndex_Type()
)
adGenEthernetDslamFlowRev2InterfaceLogicalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2InterfaceLogicalIndex.setStatus("current")
_AdGenEthernetDslamFlowRev2LastErrorString_Type = DisplayString
_AdGenEthernetDslamFlowRev2LastErrorString_Object = MibTableColumn
adGenEthernetDslamFlowRev2LastErrorString = _AdGenEthernetDslamFlowRev2LastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 48),
    _AdGenEthernetDslamFlowRev2LastErrorString_Type()
)
adGenEthernetDslamFlowRev2LastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2LastErrorString.setStatus("current")
_AdGenEthernetDslamFlowRev2RowStatus_Type = RowStatus
_AdGenEthernetDslamFlowRev2RowStatus_Object = MibTableColumn
adGenEthernetDslamFlowRev2RowStatus = _AdGenEthernetDslamFlowRev2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 49),
    _AdGenEthernetDslamFlowRev2RowStatus_Type()
)
adGenEthernetDslamFlowRev2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2RowStatus.setStatus("current")
_AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Type = Integer32
_AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressPolicer = _AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 50),
    _AdGenEthernetDslamFlowRev2NetworkIngressPolicer_Type()
)
adGenEthernetDslamFlowRev2NetworkIngressPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkIngressPolicer.setStatus("current")


class _AdGenEthernetDslamFlowRev2UpstreamDiscard_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2UpstreamDiscard based on Integer32"""
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


_AdGenEthernetDslamFlowRev2UpstreamDiscard_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2UpstreamDiscard_Object = MibTableColumn
adGenEthernetDslamFlowRev2UpstreamDiscard = _AdGenEthernetDslamFlowRev2UpstreamDiscard_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 51),
    _AdGenEthernetDslamFlowRev2UpstreamDiscard_Type()
)
adGenEthernetDslamFlowRev2UpstreamDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2UpstreamDiscard.setStatus("current")
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Type = Integer32
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Object = MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth = _AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 53),
    _AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth_Type()
)
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth.setStatus("current")


class _AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable based on Integer32"""
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


_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Object = MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable = _AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 54),
    _AdGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable_Type()
)
adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable.setStatus("current")


class _AdGenEthernetDslamFlowRev2ProfileName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2ProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowRev2ProfileName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2ProfileName_Object = MibTableColumn
adGenEthernetDslamFlowRev2ProfileName = _AdGenEthernetDslamFlowRev2ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 55),
    _AdGenEthernetDslamFlowRev2ProfileName_Type()
)
adGenEthernetDslamFlowRev2ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2ProfileName.setStatus("current")


class _AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable based on Integer32"""
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


_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Object = MibTableColumn
adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable = _AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 56),
    _AdGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable_Type()
)
adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable.setStatus("current")
_AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Type = DisplayString
_AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Object = MibTableColumn
adGenEthernetDslamFlowRev2NetworkIngressDSCPList = _AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 57),
    _AdGenEthernetDslamFlowRev2NetworkIngressDSCPList_Type()
)
adGenEthernetDslamFlowRev2NetworkIngressDSCPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NetworkIngressDSCPList.setStatus("current")
_AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Type = DisplayString
_AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Object = MibTableColumn
adGenEthernetDslamFlowRev2CustomerIngressDSCPList = _AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 58),
    _AdGenEthernetDslamFlowRev2CustomerIngressDSCPList_Type()
)
adGenEthernetDslamFlowRev2CustomerIngressDSCPList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2CustomerIngressDSCPList.setStatus("current")
_AdGenEthernetDslamFlowRev2IgmpRouterIP_Type = IpAddress
_AdGenEthernetDslamFlowRev2IgmpRouterIP_Object = MibTableColumn
adGenEthernetDslamFlowRev2IgmpRouterIP = _AdGenEthernetDslamFlowRev2IgmpRouterIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 59),
    _AdGenEthernetDslamFlowRev2IgmpRouterIP_Type()
)
adGenEthernetDslamFlowRev2IgmpRouterIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IgmpRouterIP.setStatus("current")


class _AdGenEthernetDslamFlowRev2ActivationStatus_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2ActivationStatus based on Integer32"""
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
        *(("notActivated", 1),
          ("inProgress", 2),
          ("active", 3),
          ("error", 4))
    )


_AdGenEthernetDslamFlowRev2ActivationStatus_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2ActivationStatus_Object = MibTableColumn
adGenEthernetDslamFlowRev2ActivationStatus = _AdGenEthernetDslamFlowRev2ActivationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 60),
    _AdGenEthernetDslamFlowRev2ActivationStatus_Type()
)
adGenEthernetDslamFlowRev2ActivationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2ActivationStatus.setStatus("current")


class _AdGenEthernetDslamFlowRev2ARPProcessing_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2ARPProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("proxy", 2),
          ("transparent", 3))
    )


_AdGenEthernetDslamFlowRev2ARPProcessing_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2ARPProcessing_Object = MibTableColumn
adGenEthernetDslamFlowRev2ARPProcessing = _AdGenEthernetDslamFlowRev2ARPProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 61),
    _AdGenEthernetDslamFlowRev2ARPProcessing_Type()
)
adGenEthernetDslamFlowRev2ARPProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2ARPProcessing.setStatus("current")


class _AdGenEthernetDslamFlowRev2PPPoEProcessing_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2PPPoEProcessing based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("notApplicable", 3),
          ("transparent", 4))
    )


_AdGenEthernetDslamFlowRev2PPPoEProcessing_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2PPPoEProcessing_Object = MibTableColumn
adGenEthernetDslamFlowRev2PPPoEProcessing = _AdGenEthernetDslamFlowRev2PPPoEProcessing_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 62),
    _AdGenEthernetDslamFlowRev2PPPoEProcessing_Type()
)
adGenEthernetDslamFlowRev2PPPoEProcessing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2PPPoEProcessing.setStatus("current")
_AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Type = DisplayString
_AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Object = MibTableColumn
adGenEthernetDslamFlowRev2SubscriberIpRowCreateError = _AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 63),
    _AdGenEthernetDslamFlowRev2SubscriberIpRowCreateError_Type()
)
adGenEthernetDslamFlowRev2SubscriberIpRowCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2SubscriberIpRowCreateError.setStatus("current")
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Type = Integer32
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber = _AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 64),
    _AdGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber_Type()
)
adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber.setStatus("current")


class _AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat = _AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 65),
    _AdGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat_Type()
)
adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat.setStatus("current")


class _AdGenEthernetDslamFlowRev2EvcName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2EvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEthernetDslamFlowRev2EvcName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2EvcName_Object = MibTableColumn
adGenEthernetDslamFlowRev2EvcName = _AdGenEthernetDslamFlowRev2EvcName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 66),
    _AdGenEthernetDslamFlowRev2EvcName_Type()
)
adGenEthernetDslamFlowRev2EvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2EvcName.setStatus("current")


class _AdGenEthernetDslamFlowRev2EvcRoot_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2EvcRoot based on Integer32"""
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


_AdGenEthernetDslamFlowRev2EvcRoot_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2EvcRoot_Object = MibTableColumn
adGenEthernetDslamFlowRev2EvcRoot = _AdGenEthernetDslamFlowRev2EvcRoot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 67),
    _AdGenEthernetDslamFlowRev2EvcRoot_Type()
)
adGenEthernetDslamFlowRev2EvcRoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2EvcRoot.setStatus("current")


class _AdGenEthernetDslamFlowRev2Dhcpv6Mode_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2Dhcpv6Mode based on Integer32"""
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
        *(("authenticate", 1),
          ("block", 2),
          ("transparent", 3),
          ("snoop", 4),
          ("sameAsDhcpv4", 5))
    )


_AdGenEthernetDslamFlowRev2Dhcpv6Mode_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2Dhcpv6Mode_Object = MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6Mode = _AdGenEthernetDslamFlowRev2Dhcpv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 68),
    _AdGenEthernetDslamFlowRev2Dhcpv6Mode_Type()
)
adGenEthernetDslamFlowRev2Dhcpv6Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Dhcpv6Mode.setStatus("current")


class _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2Dhcpv6RelayAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("sameAsDhcpv4", 3))
    )


_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Object = MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6RelayAgent = _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 69),
    _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgent_Type()
)
adGenEthernetDslamFlowRev2Dhcpv6RelayAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Dhcpv6RelayAgent.setStatus("current")


class _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Object = MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted = _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 70),
    _AdGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted_Type()
)
adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted.setStatus("current")


class _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Object = MibTableColumn
adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat = _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 71),
    _AdGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat_Type()
)
adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat.setStatus("current")


class _AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2DownstreamQosMapProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Object = MibTableColumn
adGenEthernetDslamFlowRev2DownstreamQosMapProfile = _AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 72),
    _AdGenEthernetDslamFlowRev2DownstreamQosMapProfile_Type()
)
adGenEthernetDslamFlowRev2DownstreamQosMapProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2DownstreamQosMapProfile.setStatus("current")


class _AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Type(Integer32):
    """Custom type adGenEthernetDslamFlowRev2Dhcpv6CurrMode based on Integer32"""
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
        *(("authenticate", 1),
          ("block", 2),
          ("transparent", 3),
          ("snoop", 4))
    )


_AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Object = MibTableColumn
adGenEthernetDslamFlowRev2Dhcpv6CurrMode = _AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 73),
    _AdGenEthernetDslamFlowRev2Dhcpv6CurrMode_Type()
)
adGenEthernetDslamFlowRev2Dhcpv6CurrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2Dhcpv6CurrMode.setStatus("current")
_AdGenEthernetDslamFlowRev2MatchSourceMacList_Type = OctetString
_AdGenEthernetDslamFlowRev2MatchSourceMacList_Object = MibTableColumn
adGenEthernetDslamFlowRev2MatchSourceMacList = _AdGenEthernetDslamFlowRev2MatchSourceMacList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 74),
    _AdGenEthernetDslamFlowRev2MatchSourceMacList_Type()
)
adGenEthernetDslamFlowRev2MatchSourceMacList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MatchSourceMacList.setStatus("current")
_AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Type = DisplayString
_AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Object = MibTableColumn
adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString = _AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 75),
    _AdGenEthernetDslamFlowRev2MatchSourceMacLastErrorString_Type()
)
adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString.setStatus("current")


class _AdGenEthernetDslamFlowRev2MatchNonIp_Type(TruthValue):
    """Custom type adGenEthernetDslamFlowRev2MatchNonIp based on TruthValue"""
    defaultValue = 2


_AdGenEthernetDslamFlowRev2MatchNonIp_Type.__name__ = "TruthValue"
_AdGenEthernetDslamFlowRev2MatchNonIp_Object = MibTableColumn
adGenEthernetDslamFlowRev2MatchNonIp = _AdGenEthernetDslamFlowRev2MatchNonIp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 11, 1, 76),
    _AdGenEthernetDslamFlowRev2MatchNonIp_Type()
)
adGenEthernetDslamFlowRev2MatchNonIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2MatchNonIp.setStatus("current")
_AdGenEthernetDslamFlowRev2NameLookupTable_Object = MibTable
adGenEthernetDslamFlowRev2NameLookupTable = _AdGenEthernetDslamFlowRev2NameLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 12)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NameLookupTable.setStatus("current")
_AdGenEthernetDslamFlowRev2NameLookupEntry_Object = MibTableRow
adGenEthernetDslamFlowRev2NameLookupEntry = _AdGenEthernetDslamFlowRev2NameLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 12, 1)
)
adGenEthernetDslamFlowRev2NameLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-ETHERNET-DSLAM-FLOW-MIB", "adGenEthernetDslamFlowRev2NameLookupName"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NameLookupEntry.setStatus("current")


class _AdGenEthernetDslamFlowRev2NameLookupName_Type(DisplayString):
    """Custom type adGenEthernetDslamFlowRev2NameLookupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AdGenEthernetDslamFlowRev2NameLookupName_Type.__name__ = "DisplayString"
_AdGenEthernetDslamFlowRev2NameLookupName_Object = MibTableColumn
adGenEthernetDslamFlowRev2NameLookupName = _AdGenEthernetDslamFlowRev2NameLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 12, 1, 1),
    _AdGenEthernetDslamFlowRev2NameLookupName_Type()
)
adGenEthernetDslamFlowRev2NameLookupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NameLookupName.setStatus("current")
_AdGenEthernetDslamFlowRev2NameLookupIndex_Type = Integer32
_AdGenEthernetDslamFlowRev2NameLookupIndex_Object = MibTableColumn
adGenEthernetDslamFlowRev2NameLookupIndex = _AdGenEthernetDslamFlowRev2NameLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 12, 1, 2),
    _AdGenEthernetDslamFlowRev2NameLookupIndex_Type()
)
adGenEthernetDslamFlowRev2NameLookupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2NameLookupIndex.setStatus("current")
_AdGenEthernetDslamFlowRev2IndexNextTable_Object = MibTable
adGenEthernetDslamFlowRev2IndexNextTable = _AdGenEthernetDslamFlowRev2IndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 13)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IndexNextTable.setStatus("current")
_AdGenEthernetDslamFlowRev2IndexNextEntry_Object = MibTableRow
adGenEthernetDslamFlowRev2IndexNextEntry = _AdGenEthernetDslamFlowRev2IndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 13, 1)
)
adGenEthernetDslamFlowRev2IndexNextEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IndexNextEntry.setStatus("current")
_AdGenEthernetDslamFlowRev2IndexNext_Type = Integer32
_AdGenEthernetDslamFlowRev2IndexNext_Object = MibTableColumn
adGenEthernetDslamFlowRev2IndexNext = _AdGenEthernetDslamFlowRev2IndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 13, 1, 1),
    _AdGenEthernetDslamFlowRev2IndexNext_Type()
)
adGenEthernetDslamFlowRev2IndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowRev2IndexNext.setStatus("current")
_AdGenEthernetDslamFlowQueueTable_Object = MibTable
adGenEthernetDslamFlowQueueTable = _AdGenEthernetDslamFlowQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 14)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowQueueTable.setStatus("current")
_AdGenEthernetDslamFlowQueueTableEntry_Object = MibTableRow
adGenEthernetDslamFlowQueueTableEntry = _AdGenEthernetDslamFlowQueueTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 14, 1)
)
adGenEthernetDslamFlowQueueTableEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowQueueTableEntry.setStatus("current")
_AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Type = TruthValue
_AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Object = MibTableColumn
adGenEthernetDslamFlowHonorsSystemPbitCosMap = _AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 14, 1, 1),
    _AdGenEthernetDslamFlowHonorsSystemPbitCosMap_Type()
)
adGenEthernetDslamFlowHonorsSystemPbitCosMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowHonorsSystemPbitCosMap.setStatus("current")


class _AdGenEthernetDslamFlowShaperQueuePriorityOrder_Type(Integer32):
    """Custom type adGenEthernetDslamFlowShaperQueuePriorityOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rightMostHighest", 1),
          ("leftMostHighest", 2))
    )


_AdGenEthernetDslamFlowShaperQueuePriorityOrder_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowShaperQueuePriorityOrder_Object = MibTableColumn
adGenEthernetDslamFlowShaperQueuePriorityOrder = _AdGenEthernetDslamFlowShaperQueuePriorityOrder_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 14, 1, 2),
    _AdGenEthernetDslamFlowShaperQueuePriorityOrder_Type()
)
adGenEthernetDslamFlowShaperQueuePriorityOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowShaperQueuePriorityOrder.setStatus("current")
_AdGenEthernetDslamFlowAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenEthernetDslamFlowAlarmsPrefix = _AdGenEthernetDslamFlowAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 15)
)
_AdGenEthernetDslamFlowAlarms_ObjectIdentity = ObjectIdentity
adGenEthernetDslamFlowAlarms = _AdGenEthernetDslamFlowAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 15, 0)
)
_AdGenEthernetDslamFlowScalarTable_Object = MibTable
adGenEthernetDslamFlowScalarTable = _AdGenEthernetDslamFlowScalarTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 16)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowScalarTable.setStatus("current")
_AdGenEthernetDslamFlowScalarTableEntry_Object = MibTableRow
adGenEthernetDslamFlowScalarTableEntry = _AdGenEthernetDslamFlowScalarTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 16, 1)
)
adGenEthernetDslamFlowScalarTableEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowScalarTableEntry.setStatus("current")
_AdGenEthernetFlowMatchSourceMacMaxAddresses_Type = Integer32
_AdGenEthernetFlowMatchSourceMacMaxAddresses_Object = MibTableColumn
adGenEthernetFlowMatchSourceMacMaxAddresses = _AdGenEthernetFlowMatchSourceMacMaxAddresses_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 16, 1, 1),
    _AdGenEthernetFlowMatchSourceMacMaxAddresses_Type()
)
adGenEthernetFlowMatchSourceMacMaxAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetFlowMatchSourceMacMaxAddresses.setStatus("current")
_AdGenEthernetDslamFlowLoggingTable_Object = MibTable
adGenEthernetDslamFlowLoggingTable = _AdGenEthernetDslamFlowLoggingTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 17)
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowLoggingTable.setStatus("current")
_AdGenEthernetDslamFlowLoggingEntry_Object = MibTableRow
adGenEthernetDslamFlowLoggingEntry = _AdGenEthernetDslamFlowLoggingEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 17, 1)
)
adGenEthernetDslamFlowLoggingEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowLoggingEntry.setStatus("current")


class _AdGenEthernetDslamFlowDhcpPppoeEventDebug_Type(Integer32):
    """Custom type adGenEthernetDslamFlowDhcpPppoeEventDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenEthernetDslamFlowDhcpPppoeEventDebug_Type.__name__ = "Integer32"
_AdGenEthernetDslamFlowDhcpPppoeEventDebug_Object = MibTableColumn
adGenEthernetDslamFlowDhcpPppoeEventDebug = _AdGenEthernetDslamFlowDhcpPppoeEventDebug_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 17, 1, 1),
    _AdGenEthernetDslamFlowDhcpPppoeEventDebug_Type()
)
adGenEthernetDslamFlowDhcpPppoeEventDebug.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDhcpPppoeEventDebug.setStatus("current")

# Managed Objects groups


# Notification objects

adGenEthernetDslamFlowDuplicateMacDetectedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 15, 0, 1)
)
adGenEthernetDslamFlowDuplicateMacDetectedClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gMacAddress"))
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDuplicateMacDetectedClr.setStatus(
        "current"
    )

adGenEthernetDslamFlowDuplicateMacDetectedAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 15, 0, 2)
)
adGenEthernetDslamFlowDuplicateMacDetectedAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-TAMINIDSLAM3G-MIB", "adGenMiniDslam3gMacAddress"))
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowDuplicateMacDetectedAct.setStatus(
        "current"
    )

adGenEthernetDslamFlowMacAllocationAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 15, 0, 3)
)
adGenEthernetDslamFlowMacAllocationAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMacAllocationAlarmClr.setStatus(
        "current"
    )

adGenEthernetDslamFlowMacAllocationAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 2, 15, 0, 4)
)
adGenEthernetDslamFlowMacAllocationAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenEthernetDslamFlowMacAllocationAlarmAct.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ETHERNET-DSLAM-FLOW-MIB",
    **{"adGenEthernetInterfaceTable": adGenEthernetInterfaceTable,
       "adGenEthernetInterfaceEntry": adGenEthernetInterfaceEntry,
       "adGenEthernetInterfaceLogicalIndex": adGenEthernetInterfaceLogicalIndex,
       "adGenEthernetInterfaceMaxMACAddresses": adGenEthernetInterfaceMaxMACAddresses,
       "adGenEthernetInterfaceFlowList": adGenEthernetInterfaceFlowList,
       "adGenEthernetInterfaceSourceAuthentication": adGenEthernetInterfaceSourceAuthentication,
       "adGenEthernetInterfaceType": adGenEthernetInterfaceType,
       "adGenEthernetInterfaceTypeSpecific": adGenEthernetInterfaceTypeSpecific,
       "adGenEthernetDslamFlowTable": adGenEthernetDslamFlowTable,
       "adGenEthernetDslamFlowEntry": adGenEthernetDslamFlowEntry,
       "adGenEthernetDslamFlowIndex": adGenEthernetDslamFlowIndex,
       "adGenEthernetDslamFlowName": adGenEthernetDslamFlowName,
       "adGenEthernetDslamFlowTrafficDirection": adGenEthernetDslamFlowTrafficDirection,
       "adGenEthernetDslamFlowNetworkSTag": adGenEthernetDslamFlowNetworkSTag,
       "adGenEthernetDslamFlowNetworkCTag": adGenEthernetDslamFlowNetworkCTag,
       "adGenEthernetDslamFlowCEVlan": adGenEthernetDslamFlowCEVlan,
       "adGenEthernetDslamFlowDownstreamForwardingMode": adGenEthernetDslamFlowDownstreamForwardingMode,
       "adGenEthernetDslamFlowDownstreamPbitMethod": adGenEthernetDslamFlowDownstreamPbitMethod,
       "adGenEthernetDslamFlowDownstreamPbitMarking": adGenEthernetDslamFlowDownstreamPbitMarking,
       "adGenEthernetDslamFlowDownstreamPbitMapping": adGenEthernetDslamFlowDownstreamPbitMapping,
       "adGenEthernetDslamFlowNetworkIngressPbit": adGenEthernetDslamFlowNetworkIngressPbit,
       "adGenEthernetDslamFlowNetworkIngressEtherType": adGenEthernetDslamFlowNetworkIngressEtherType,
       "adGenEthernetDslamFlowNetworkIngressDSCP": adGenEthernetDslamFlowNetworkIngressDSCP,
       "adGenEthernetDslamFlowNetworkIngressIPProtocolID": adGenEthernetDslamFlowNetworkIngressIPProtocolID,
       "adGenEthernetDslamFlowUpstreamForwardingMode": adGenEthernetDslamFlowUpstreamForwardingMode,
       "adGenEthernetDslamFlowUpstreamSTagPbitMethod": adGenEthernetDslamFlowUpstreamSTagPbitMethod,
       "adGenEthernetDslamFlowUpstreamSTagPbitMarking": adGenEthernetDslamFlowUpstreamSTagPbitMarking,
       "adGenEthernetDslamFlowUpstreamSTagPbitMapping": adGenEthernetDslamFlowUpstreamSTagPbitMapping,
       "adGenEthernetDslamFlowUpstreamCTagPbitMethod": adGenEthernetDslamFlowUpstreamCTagPbitMethod,
       "adGenEthernetDslamFlowUpstreamCTagPbitMarking": adGenEthernetDslamFlowUpstreamCTagPbitMarking,
       "adGenEthernetDslamFlowUpstreamCTagPbitMapping": adGenEthernetDslamFlowUpstreamCTagPbitMapping,
       "adGenEthernetDslamFlowCustomerIngressPbit": adGenEthernetDslamFlowCustomerIngressPbit,
       "adGenEthernetDslamFlowCustomerIngressEtherType": adGenEthernetDslamFlowCustomerIngressEtherType,
       "adGenEthernetDslamFlowCustomerIngressDSCP": adGenEthernetDslamFlowCustomerIngressDSCP,
       "adGenEthernetDslamFlowCustomerIngressIPProtocolID": adGenEthernetDslamFlowCustomerIngressIPProtocolID,
       "adGenEthernetDslamFlowCustomerIngressBroadcast": adGenEthernetDslamFlowCustomerIngressBroadcast,
       "adGenEthernetDslamFlowCustomerIngressMulticast": adGenEthernetDslamFlowCustomerIngressMulticast,
       "adGenEthernetDslamFlowCustomerIngressUnicast": adGenEthernetDslamFlowCustomerIngressUnicast,
       "adGenEthernetDslamFlowCustomerIngressPolicer": adGenEthernetDslamFlowCustomerIngressPolicer,
       "adGenEthernetDslamFlowEncapsMode": adGenEthernetDslamFlowEncapsMode,
       "adGenEthernetDslamFlowManualAddrAging": adGenEthernetDslamFlowManualAddrAging,
       "adGenEthernetDslamFlowIntermedAgent": adGenEthernetDslamFlowIntermedAgent,
       "adGenEthernetDslamFlowDhcpRelay": adGenEthernetDslamFlowDhcpRelay,
       "adGenEthernetDslamFlowOption82Insert": adGenEthernetDslamFlowOption82Insert,
       "adGenEthernetDslamFlowLearnedIpAddrAgingMethod": adGenEthernetDslamFlowLearnedIpAddrAgingMethod,
       "adGenEthernetDslamFlowIgmpProcessing": adGenEthernetDslamFlowIgmpProcessing,
       "adGenEthernetDslamFlowIgmpVersion": adGenEthernetDslamFlowIgmpVersion,
       "adGenEthernetDslamFlowLastMemberQueryInterval": adGenEthernetDslamFlowLastMemberQueryInterval,
       "adGenEthernetDslamFlowLastMemberQueryCount": adGenEthernetDslamFlowLastMemberQueryCount,
       "adGenEthernetDslamFlowImmediateLeave": adGenEthernetDslamFlowImmediateLeave,
       "adGenEthernetDslamFlowMaxAllowedMcastGroups": adGenEthernetDslamFlowMaxAllowedMcastGroups,
       "adGenEthernetDslamFlowDhcpPPPoERemoteId": adGenEthernetDslamFlowDhcpPPPoERemoteId,
       "adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics": adGenEthernetDslamFlowDhcpPPPoELoopCharacteristics,
       "adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat": adGenEthernetDslamFlowDhcpPPPoECircuitIdFormat,
       "adGenEthernetDslamFlowPPPoASessionTimeout": adGenEthernetDslamFlowPPPoASessionTimeout,
       "adGenEthernetDslamFlowInterfaceIfIndex": adGenEthernetDslamFlowInterfaceIfIndex,
       "adGenEthernetDslamFlowInterfaceLogicalIndex": adGenEthernetDslamFlowInterfaceLogicalIndex,
       "adGenEthernetDslamFlowLastErrorString": adGenEthernetDslamFlowLastErrorString,
       "adGenEthernetDslamFlowRowStatus": adGenEthernetDslamFlowRowStatus,
       "adGenEthernetDslamFlowNetworkIngressPolicer": adGenEthernetDslamFlowNetworkIngressPolicer,
       "adGenEthernetDslamFlowUpstreamDiscard": adGenEthernetDslamFlowUpstreamDiscard,
       "adGenEthernetDslamFlowMaxAllowedMulticastBandwidth": adGenEthernetDslamFlowMaxAllowedMulticastBandwidth,
       "adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable": adGenEthernetDslamFlowMaxAllowedMulticastBandwidthEnable,
       "adGenEthernetDslamFlowProfileName": adGenEthernetDslamFlowProfileName,
       "adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable": adGenEthernetDslamFlowMaxAllowedMcastGroupsEnable,
       "adGenEthernetDslamFlowNetworkIngressDSCPList": adGenEthernetDslamFlowNetworkIngressDSCPList,
       "adGenEthernetDslamFlowCustomerIngressDSCPList": adGenEthernetDslamFlowCustomerIngressDSCPList,
       "adGenEthernetDslamFlowIgmpRouterIP": adGenEthernetDslamFlowIgmpRouterIP,
       "adGenEthernetDslamFlowActivationStatus": adGenEthernetDslamFlowActivationStatus,
       "adGenEthernetDslamFlowARPProcessing": adGenEthernetDslamFlowARPProcessing,
       "adGenEthernetDslamFlowPPPoEProcessing": adGenEthernetDslamFlowPPPoEProcessing,
       "adGenEthernetDslamFlowSubscriberIpRowCreateError": adGenEthernetDslamFlowSubscriberIpRowCreateError,
       "adGenEthernetDslamFlowDhcpPPPoEVendorNumber": adGenEthernetDslamFlowDhcpPPPoEVendorNumber,
       "adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat": adGenEthernetDslamFlowDhcpPPPoEVendorIdFormat,
       "adGenEthernetDslamFlowEvcName": adGenEthernetDslamFlowEvcName,
       "adGenEthernetDslamFlowEvcRoot": adGenEthernetDslamFlowEvcRoot,
       "adGenEthernetDslamFlowDhcpv6Mode": adGenEthernetDslamFlowDhcpv6Mode,
       "adGenEthernetDslamFlowDhcpv6RelayAgent": adGenEthernetDslamFlowDhcpv6RelayAgent,
       "adGenEthernetDslamFlowDhcpv6RelayAgentTrusted": adGenEthernetDslamFlowDhcpv6RelayAgentTrusted,
       "adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat": adGenEthernetDslamFlowDhcpPPPoERemoteIdFormat,
       "adGenEthernetDslamFlowDownstreamQosMapProfile": adGenEthernetDslamFlowDownstreamQosMapProfile,
       "adGenEthernetDslamFlowUpstreamChannel": adGenEthernetDslamFlowUpstreamChannel,
       "adGenEthernetDslamFlowDhcpv6CurrMode": adGenEthernetDslamFlowDhcpv6CurrMode,
       "adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert": adGenEthernetDslamFlowDhcpPPPoEVendorIdInsert,
       "adGenEthernetDslamFlowMatchSourceMacList": adGenEthernetDslamFlowMatchSourceMacList,
       "adGenEthernetDslamFlowMatchSourceMacLastErrorString": adGenEthernetDslamFlowMatchSourceMacLastErrorString,
       "adGenEthernetDslamFlowMatchNonIp": adGenEthernetDslamFlowMatchNonIp,
       "adGenEthernetDslamFlowIndexNextTable": adGenEthernetDslamFlowIndexNextTable,
       "adGenEthernetDslamFlowIndexNextEntry": adGenEthernetDslamFlowIndexNextEntry,
       "adGenEthernetDslamFlowIndexNext": adGenEthernetDslamFlowIndexNext,
       "adGenEthernetDslamFlowProfilesTable": adGenEthernetDslamFlowProfilesTable,
       "adGenEthernetDslamFlowProfilesEntry": adGenEthernetDslamFlowProfilesEntry,
       "adGenEthernetDslamFlowProfileIndex": adGenEthernetDslamFlowProfileIndex,
       "adGenEthernetDslamFlowProfileAlias": adGenEthernetDslamFlowProfileAlias,
       "adGenEthernetDslamFlowProfileCIR": adGenEthernetDslamFlowProfileCIR,
       "adGenEthernetDslamFlowProfileCBS": adGenEthernetDslamFlowProfileCBS,
       "adGenEthernetDslamFlowProfileEIR": adGenEthernetDslamFlowProfileEIR,
       "adGenEthernetDslamFlowProfileEBS": adGenEthernetDslamFlowProfileEBS,
       "adGenEthernetDslamFlowProfileLastErrorString": adGenEthernetDslamFlowProfileLastErrorString,
       "adGenEthernetDslamFlowProfileRowStatus": adGenEthernetDslamFlowProfileRowStatus,
       "adGenEthernetDslamFlowProfileActualCIR": adGenEthernetDslamFlowProfileActualCIR,
       "adGenEthernetDslamFlowProfileActualCBS": adGenEthernetDslamFlowProfileActualCBS,
       "adGenEthernetDslamFlowProfileActualEIR": adGenEthernetDslamFlowProfileActualEIR,
       "adGenEthernetDslamFlowProfileActualEBS": adGenEthernetDslamFlowProfileActualEBS,
       "adGenEthernetDslamFlowNameLookupTable": adGenEthernetDslamFlowNameLookupTable,
       "adGenEthernetDslamFlowNameLookupEntry": adGenEthernetDslamFlowNameLookupEntry,
       "adGenEthernetDslamFlowNameLookupName": adGenEthernetDslamFlowNameLookupName,
       "adGenEthernetDslamFlowNameLookupIndex": adGenEthernetDslamFlowNameLookupIndex,
       "adGenEthernetDslamFlowShaperTable": adGenEthernetDslamFlowShaperTable,
       "adGenEthernetDslamFlowShaperEntry": adGenEthernetDslamFlowShaperEntry,
       "adGenEthernetDslamFlowShaperInterfaceLogicalIndex": adGenEthernetDslamFlowShaperInterfaceLogicalIndex,
       "adGenEthernetDslamFlowShaperPrioritySet": adGenEthernetDslamFlowShaperPrioritySet,
       "adGenEthernetDslamFlowShaperRate": adGenEthernetDslamFlowShaperRate,
       "adGenEthernetDslamFlowShaperRowStatus": adGenEthernetDslamFlowShaperRowStatus,
       "adGenEthernetDslamFlowShaperLastErrorString": adGenEthernetDslamFlowShaperLastErrorString,
       "adGenEthernetDslamFlowShaperAlias": adGenEthernetDslamFlowShaperAlias,
       "adGenEthernetDslamFlowShaperOperationalStatus": adGenEthernetDslamFlowShaperOperationalStatus,
       "adGenEthernetDslamFlowShaperBurstSize": adGenEthernetDslamFlowShaperBurstSize,
       "adGenEthernetDslamFlowShaperFixedRate": adGenEthernetDslamFlowShaperFixedRate,
       "adGenEthernetDslamFlowShaperAssuredRate": adGenEthernetDslamFlowShaperAssuredRate,
       "adGenEthernetDslamFlowShaperDownstreamMinRate": adGenEthernetDslamFlowShaperDownstreamMinRate,
       "adGenSubscriberAccessStaticIpTable": adGenSubscriberAccessStaticIpTable,
       "adGenSubscriberAccessStaticIpEntry": adGenSubscriberAccessStaticIpEntry,
       "adGenSubscriberAccessStaticIpAddress": adGenSubscriberAccessStaticIpAddress,
       "adGenSubscriberAccessStaticIpMacAddress": adGenSubscriberAccessStaticIpMacAddress,
       "adGenSubscriberAccessStaticIpGatewayIp": adGenSubscriberAccessStaticIpGatewayIp,
       "adGenSubscriberAccessStaticIpGatewayMac": adGenSubscriberAccessStaticIpGatewayMac,
       "adGenSubscriberAccessStaticIpLastErrorString": adGenSubscriberAccessStaticIpLastErrorString,
       "adGenSubscriberAccessStaticIpRowStatus": adGenSubscriberAccessStaticIpRowStatus,
       "adGenEthernetDslamFlowProfilesIndexNextTable": adGenEthernetDslamFlowProfilesIndexNextTable,
       "adGenEthernetDslamFlowProfilesIndexNextEntry": adGenEthernetDslamFlowProfilesIndexNextEntry,
       "adGenEthernetDslamFlowProfilesIndexNext": adGenEthernetDslamFlowProfilesIndexNext,
       "adGenEthernetDslamFlowProfilesLookupTable": adGenEthernetDslamFlowProfilesLookupTable,
       "adGenEthernetDslamFlowProfilesLookupEntry": adGenEthernetDslamFlowProfilesLookupEntry,
       "adGenEthernetDslamFlowProfileLookupAlias": adGenEthernetDslamFlowProfileLookupAlias,
       "adGenEthernetDslamFlowProfileLookupIndex": adGenEthernetDslamFlowProfileLookupIndex,
       "adGenEthernetDslamFlowShaperLookupTable": adGenEthernetDslamFlowShaperLookupTable,
       "adGenEthernetDslamFlowShaperLookupEntry": adGenEthernetDslamFlowShaperLookupEntry,
       "adGenEthernetDslamFlowShaperLookupAlias": adGenEthernetDslamFlowShaperLookupAlias,
       "adGenEthernetDslamFlowShaperLookupIfIndex": adGenEthernetDslamFlowShaperLookupIfIndex,
       "adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex": adGenEthernetDslamFlowShaperLookupInterfaceLogicalIndex,
       "adGenEthernetDslamFlowShaperLookupPrioritySet": adGenEthernetDslamFlowShaperLookupPrioritySet,
       "adGenEthernetDslamFlowRev2Table": adGenEthernetDslamFlowRev2Table,
       "adGenEthernetDslamFlowRev2Entry": adGenEthernetDslamFlowRev2Entry,
       "adGenEthernetDslamFlowRev2Index": adGenEthernetDslamFlowRev2Index,
       "adGenEthernetDslamFlowRev2Name": adGenEthernetDslamFlowRev2Name,
       "adGenEthernetDslamFlowRev2TrafficDirection": adGenEthernetDslamFlowRev2TrafficDirection,
       "adGenEthernetDslamFlowRev2NetworkSTag": adGenEthernetDslamFlowRev2NetworkSTag,
       "adGenEthernetDslamFlowRev2NetworkCTag": adGenEthernetDslamFlowRev2NetworkCTag,
       "adGenEthernetDslamFlowRev2CEVlan": adGenEthernetDslamFlowRev2CEVlan,
       "adGenEthernetDslamFlowRev2DownstreamForwardingMode": adGenEthernetDslamFlowRev2DownstreamForwardingMode,
       "adGenEthernetDslamFlowRev2DownstreamPbitMethod": adGenEthernetDslamFlowRev2DownstreamPbitMethod,
       "adGenEthernetDslamFlowRev2DownstreamPbitMarking": adGenEthernetDslamFlowRev2DownstreamPbitMarking,
       "adGenEthernetDslamFlowRev2DownstreamPbitMapping": adGenEthernetDslamFlowRev2DownstreamPbitMapping,
       "adGenEthernetDslamFlowRev2NetworkIngressPbit": adGenEthernetDslamFlowRev2NetworkIngressPbit,
       "adGenEthernetDslamFlowRev2NetworkIngressEtherType": adGenEthernetDslamFlowRev2NetworkIngressEtherType,
       "adGenEthernetDslamFlowRev2NetworkIngressDSCP": adGenEthernetDslamFlowRev2NetworkIngressDSCP,
       "adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID": adGenEthernetDslamFlowRev2NetworkIngressIPProtocolID,
       "adGenEthernetDslamFlowRev2UpstreamForwardingMode": adGenEthernetDslamFlowRev2UpstreamForwardingMode,
       "adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod": adGenEthernetDslamFlowRev2UpstreamSTagPbitMethod,
       "adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking": adGenEthernetDslamFlowRev2UpstreamSTagPbitMarking,
       "adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping": adGenEthernetDslamFlowRev2UpstreamSTagPbitMapping,
       "adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod": adGenEthernetDslamFlowRev2UpstreamCTagPbitMethod,
       "adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking": adGenEthernetDslamFlowRev2UpstreamCTagPbitMarking,
       "adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping": adGenEthernetDslamFlowRev2UpstreamCTagPbitMapping,
       "adGenEthernetDslamFlowRev2CustomerIngressPbit": adGenEthernetDslamFlowRev2CustomerIngressPbit,
       "adGenEthernetDslamFlowRev2CustomerIngressEtherType": adGenEthernetDslamFlowRev2CustomerIngressEtherType,
       "adGenEthernetDslamFlowRev2CustomerIngressDSCP": adGenEthernetDslamFlowRev2CustomerIngressDSCP,
       "adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID": adGenEthernetDslamFlowRev2CustomerIngressIPProtocolID,
       "adGenEthernetDslamFlowRev2CustomerIngressBroadcast": adGenEthernetDslamFlowRev2CustomerIngressBroadcast,
       "adGenEthernetDslamFlowRev2CustomerIngressMulticast": adGenEthernetDslamFlowRev2CustomerIngressMulticast,
       "adGenEthernetDslamFlowRev2CustomerIngressUnicast": adGenEthernetDslamFlowRev2CustomerIngressUnicast,
       "adGenEthernetDslamFlowRev2CustomerIngressPolicer": adGenEthernetDslamFlowRev2CustomerIngressPolicer,
       "adGenEthernetDslamFlowRev2EncapsMode": adGenEthernetDslamFlowRev2EncapsMode,
       "adGenEthernetDslamFlowRev2ManualAddrAging": adGenEthernetDslamFlowRev2ManualAddrAging,
       "adGenEthernetDslamFlowRev2IntermedAgent": adGenEthernetDslamFlowRev2IntermedAgent,
       "adGenEthernetDslamFlowRev2DhcpRelay": adGenEthernetDslamFlowRev2DhcpRelay,
       "adGenEthernetDslamFlowRev2Option82Insert": adGenEthernetDslamFlowRev2Option82Insert,
       "adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod": adGenEthernetDslamFlowRev2LearnedIpAddrAgingMethod,
       "adGenEthernetDslamFlowRev2IgmpProcessing": adGenEthernetDslamFlowRev2IgmpProcessing,
       "adGenEthernetDslamFlowRev2IgmpVersion": adGenEthernetDslamFlowRev2IgmpVersion,
       "adGenEthernetDslamFlowRev2LastMemberQueryInterval": adGenEthernetDslamFlowRev2LastMemberQueryInterval,
       "adGenEthernetDslamFlowRev2LastMemberQueryCount": adGenEthernetDslamFlowRev2LastMemberQueryCount,
       "adGenEthernetDslamFlowRev2ImmediateLeave": adGenEthernetDslamFlowRev2ImmediateLeave,
       "adGenEthernetDslamFlowRev2MaxAllowedMcastGroups": adGenEthernetDslamFlowRev2MaxAllowedMcastGroups,
       "adGenEthernetDslamFlowRev2DhcpPPPoERemoteId": adGenEthernetDslamFlowRev2DhcpPPPoERemoteId,
       "adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics": adGenEthernetDslamFlowRev2DhcpPPPoELoopCharacteristics,
       "adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat": adGenEthernetDslamFlowRev2DhcpPPPoECircuitIdFormat,
       "adGenEthernetDslamFlowRev2PPPoASessionTimeout": adGenEthernetDslamFlowRev2PPPoASessionTimeout,
       "adGenEthernetDslamFlowRev2InterfaceIfIndex": adGenEthernetDslamFlowRev2InterfaceIfIndex,
       "adGenEthernetDslamFlowRev2InterfaceLogicalIndex": adGenEthernetDslamFlowRev2InterfaceLogicalIndex,
       "adGenEthernetDslamFlowRev2LastErrorString": adGenEthernetDslamFlowRev2LastErrorString,
       "adGenEthernetDslamFlowRev2RowStatus": adGenEthernetDslamFlowRev2RowStatus,
       "adGenEthernetDslamFlowRev2NetworkIngressPolicer": adGenEthernetDslamFlowRev2NetworkIngressPolicer,
       "adGenEthernetDslamFlowRev2UpstreamDiscard": adGenEthernetDslamFlowRev2UpstreamDiscard,
       "adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth": adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidth,
       "adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable": adGenEthernetDslamFlowRev2MaxAllowedMulticastBandwidthEnable,
       "adGenEthernetDslamFlowRev2ProfileName": adGenEthernetDslamFlowRev2ProfileName,
       "adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable": adGenEthernetDslamFlowRev2MaxAllowedMcastGroupsEnable,
       "adGenEthernetDslamFlowRev2NetworkIngressDSCPList": adGenEthernetDslamFlowRev2NetworkIngressDSCPList,
       "adGenEthernetDslamFlowRev2CustomerIngressDSCPList": adGenEthernetDslamFlowRev2CustomerIngressDSCPList,
       "adGenEthernetDslamFlowRev2IgmpRouterIP": adGenEthernetDslamFlowRev2IgmpRouterIP,
       "adGenEthernetDslamFlowRev2ActivationStatus": adGenEthernetDslamFlowRev2ActivationStatus,
       "adGenEthernetDslamFlowRev2ARPProcessing": adGenEthernetDslamFlowRev2ARPProcessing,
       "adGenEthernetDslamFlowRev2PPPoEProcessing": adGenEthernetDslamFlowRev2PPPoEProcessing,
       "adGenEthernetDslamFlowRev2SubscriberIpRowCreateError": adGenEthernetDslamFlowRev2SubscriberIpRowCreateError,
       "adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber": adGenEthernetDslamFlowRev2DhcpPPPoEVendorNumber,
       "adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat": adGenEthernetDslamFlowRev2DhcpPPPoEVendorIdFormat,
       "adGenEthernetDslamFlowRev2EvcName": adGenEthernetDslamFlowRev2EvcName,
       "adGenEthernetDslamFlowRev2EvcRoot": adGenEthernetDslamFlowRev2EvcRoot,
       "adGenEthernetDslamFlowRev2Dhcpv6Mode": adGenEthernetDslamFlowRev2Dhcpv6Mode,
       "adGenEthernetDslamFlowRev2Dhcpv6RelayAgent": adGenEthernetDslamFlowRev2Dhcpv6RelayAgent,
       "adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted": adGenEthernetDslamFlowRev2Dhcpv6RelayAgentTrusted,
       "adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat": adGenEthernetDslamFlowRev2DhcpPPPoERemoteIdFormat,
       "adGenEthernetDslamFlowRev2DownstreamQosMapProfile": adGenEthernetDslamFlowRev2DownstreamQosMapProfile,
       "adGenEthernetDslamFlowRev2Dhcpv6CurrMode": adGenEthernetDslamFlowRev2Dhcpv6CurrMode,
       "adGenEthernetDslamFlowRev2MatchSourceMacList": adGenEthernetDslamFlowRev2MatchSourceMacList,
       "adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString": adGenEthernetDslamFlowRev2MatchSourceMacLastErrorString,
       "adGenEthernetDslamFlowRev2MatchNonIp": adGenEthernetDslamFlowRev2MatchNonIp,
       "adGenEthernetDslamFlowRev2NameLookupTable": adGenEthernetDslamFlowRev2NameLookupTable,
       "adGenEthernetDslamFlowRev2NameLookupEntry": adGenEthernetDslamFlowRev2NameLookupEntry,
       "adGenEthernetDslamFlowRev2NameLookupName": adGenEthernetDslamFlowRev2NameLookupName,
       "adGenEthernetDslamFlowRev2NameLookupIndex": adGenEthernetDslamFlowRev2NameLookupIndex,
       "adGenEthernetDslamFlowRev2IndexNextTable": adGenEthernetDslamFlowRev2IndexNextTable,
       "adGenEthernetDslamFlowRev2IndexNextEntry": adGenEthernetDslamFlowRev2IndexNextEntry,
       "adGenEthernetDslamFlowRev2IndexNext": adGenEthernetDslamFlowRev2IndexNext,
       "adGenEthernetDslamFlowQueueTable": adGenEthernetDslamFlowQueueTable,
       "adGenEthernetDslamFlowQueueTableEntry": adGenEthernetDslamFlowQueueTableEntry,
       "adGenEthernetDslamFlowHonorsSystemPbitCosMap": adGenEthernetDslamFlowHonorsSystemPbitCosMap,
       "adGenEthernetDslamFlowShaperQueuePriorityOrder": adGenEthernetDslamFlowShaperQueuePriorityOrder,
       "adGenEthernetDslamFlowAlarmsPrefix": adGenEthernetDslamFlowAlarmsPrefix,
       "adGenEthernetDslamFlowAlarms": adGenEthernetDslamFlowAlarms,
       "adGenEthernetDslamFlowDuplicateMacDetectedClr": adGenEthernetDslamFlowDuplicateMacDetectedClr,
       "adGenEthernetDslamFlowDuplicateMacDetectedAct": adGenEthernetDslamFlowDuplicateMacDetectedAct,
       "adGenEthernetDslamFlowMacAllocationAlarmClr": adGenEthernetDslamFlowMacAllocationAlarmClr,
       "adGenEthernetDslamFlowMacAllocationAlarmAct": adGenEthernetDslamFlowMacAllocationAlarmAct,
       "adGenEthernetDslamFlowScalarTable": adGenEthernetDslamFlowScalarTable,
       "adGenEthernetDslamFlowScalarTableEntry": adGenEthernetDslamFlowScalarTableEntry,
       "adGenEthernetFlowMatchSourceMacMaxAddresses": adGenEthernetFlowMatchSourceMacMaxAddresses,
       "adGenEthernetDslamFlowLoggingTable": adGenEthernetDslamFlowLoggingTable,
       "adGenEthernetDslamFlowLoggingEntry": adGenEthernetDslamFlowLoggingEntry,
       "adGenEthernetDslamFlowDhcpPppoeEventDebug": adGenEthernetDslamFlowDhcpPppoeEventDebug,
       "adGenEthernetDslamFlowMIB": adGenEthernetDslamFlowMIB}
)
