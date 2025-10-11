# SNMP MIB module (ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:37 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenPseudowireCEMMgmt,
 adGenPseudowireCEMMgmtID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPseudowireCEMMgmt",
    "adGenPseudowireCEMMgmtID")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPseudowireCEMMgmtModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMMgmtModuleIdentity.setRevisions(
        ("2014-12-17 11:15",
         "2012-05-18 11:15")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPseudowireCEMProv_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMProv = _AdGenPseudowireCEMProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1)
)
_AdGenPseudowireCEMProvTable_Object = MibTable
adGenPseudowireCEMProvTable = _AdGenPseudowireCEMProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMProvTable.setStatus("current")
_AdGenPseudowireCEMProvTableEntry_Object = MibTableRow
adGenPseudowireCEMProvTableEntry = _AdGenPseudowireCEMProvTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1)
)
adGenPseudowireCEMProvTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMProvTableEntry.setStatus("current")


class _AdGenPseudowireCEMType_Type(Integer32):
    """Custom type adGenPseudowireCEMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("satop", 1),
          ("cesopBasic", 2),
          ("cesopCas", 3))
    )


_AdGenPseudowireCEMType_Type.__name__ = "Integer32"
_AdGenPseudowireCEMType_Object = MibTableColumn
adGenPseudowireCEMType = _AdGenPseudowireCEMType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 1),
    _AdGenPseudowireCEMType_Type()
)
adGenPseudowireCEMType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMType.setStatus("current")
_AdGenPseudowireCEMPhysicalPortIfIndex_Type = InterfaceIndexOrZero
_AdGenPseudowireCEMPhysicalPortIfIndex_Object = MibTableColumn
adGenPseudowireCEMPhysicalPortIfIndex = _AdGenPseudowireCEMPhysicalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 2),
    _AdGenPseudowireCEMPhysicalPortIfIndex_Type()
)
adGenPseudowireCEMPhysicalPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPhysicalPortIfIndex.setStatus("current")
_AdGenPseudowireCEMDestinationNode_Type = Integer32
_AdGenPseudowireCEMDestinationNode_Object = MibTableColumn
adGenPseudowireCEMDestinationNode = _AdGenPseudowireCEMDestinationNode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 3),
    _AdGenPseudowireCEMDestinationNode_Type()
)
adGenPseudowireCEMDestinationNode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationNode.setStatus("current")
_AdGenPseudowireCEMDestinationShelf_Type = Integer32
_AdGenPseudowireCEMDestinationShelf_Object = MibTableColumn
adGenPseudowireCEMDestinationShelf = _AdGenPseudowireCEMDestinationShelf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 4),
    _AdGenPseudowireCEMDestinationShelf_Type()
)
adGenPseudowireCEMDestinationShelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationShelf.setStatus("current")
_AdGenPseudowireCEMDestinationSlot_Type = InterfaceIndex
_AdGenPseudowireCEMDestinationSlot_Object = MibTableColumn
adGenPseudowireCEMDestinationSlot = _AdGenPseudowireCEMDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 5),
    _AdGenPseudowireCEMDestinationSlot_Type()
)
adGenPseudowireCEMDestinationSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationSlot.setStatus("current")
_AdGenPseudowireCEMDestinationChannel_Type = InterfaceIndex
_AdGenPseudowireCEMDestinationChannel_Object = MibTableColumn
adGenPseudowireCEMDestinationChannel = _AdGenPseudowireCEMDestinationChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 6),
    _AdGenPseudowireCEMDestinationChannel_Type()
)
adGenPseudowireCEMDestinationChannel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationChannel.setStatus("current")
_AdGenPseudowireCEMDestinationONTNumber_Type = InterfaceIndex
_AdGenPseudowireCEMDestinationONTNumber_Object = MibTableColumn
adGenPseudowireCEMDestinationONTNumber = _AdGenPseudowireCEMDestinationONTNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 7),
    _AdGenPseudowireCEMDestinationONTNumber_Type()
)
adGenPseudowireCEMDestinationONTNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationONTNumber.setStatus("current")
_AdGenPseudowireCEMDestinationONTSlot_Type = InterfaceIndex
_AdGenPseudowireCEMDestinationONTSlot_Object = MibTableColumn
adGenPseudowireCEMDestinationONTSlot = _AdGenPseudowireCEMDestinationONTSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 8),
    _AdGenPseudowireCEMDestinationONTSlot_Type()
)
adGenPseudowireCEMDestinationONTSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationONTSlot.setStatus("current")
_AdGenPseudowireCEMDestinationONTPort_Type = InterfaceIndex
_AdGenPseudowireCEMDestinationONTPort_Object = MibTableColumn
adGenPseudowireCEMDestinationONTPort = _AdGenPseudowireCEMDestinationONTPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 9),
    _AdGenPseudowireCEMDestinationONTPort_Type()
)
adGenPseudowireCEMDestinationONTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDestinationONTPort.setStatus("current")
_AdGenPseudowireCEMRowStatus_Type = RowStatus
_AdGenPseudowireCEMRowStatus_Object = MibTableColumn
adGenPseudowireCEMRowStatus = _AdGenPseudowireCEMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 10),
    _AdGenPseudowireCEMRowStatus_Type()
)
adGenPseudowireCEMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMRowStatus.setStatus("current")
_AdGenPseudowireCEMErrorStr_Type = DisplayString
_AdGenPseudowireCEMErrorStr_Object = MibTableColumn
adGenPseudowireCEMErrorStr = _AdGenPseudowireCEMErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 11),
    _AdGenPseudowireCEMErrorStr_Type()
)
adGenPseudowireCEMErrorStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMErrorStr.setStatus("current")
_AdGenPseudowireCEMCircuitIdentifierStr_Type = DisplayString
_AdGenPseudowireCEMCircuitIdentifierStr_Object = MibTableColumn
adGenPseudowireCEMCircuitIdentifierStr = _AdGenPseudowireCEMCircuitIdentifierStr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 12),
    _AdGenPseudowireCEMCircuitIdentifierStr_Type()
)
adGenPseudowireCEMCircuitIdentifierStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCircuitIdentifierStr.setStatus("current")


class _AdGenPseudowireCEMPktJitterBufferDepth_Type(Integer32):
    """Custom type adGenPseudowireCEMPktJitterBufferDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AdGenPseudowireCEMPktJitterBufferDepth_Type.__name__ = "Integer32"
_AdGenPseudowireCEMPktJitterBufferDepth_Object = MibTableColumn
adGenPseudowireCEMPktJitterBufferDepth = _AdGenPseudowireCEMPktJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 13),
    _AdGenPseudowireCEMPktJitterBufferDepth_Type()
)
adGenPseudowireCEMPktJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPktJitterBufferDepth.setStatus("current")


class _AdGenPseudowireCEMPktPayloadSize_Type(Integer32):
    """Custom type adGenPseudowireCEMPktPayloadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 958),
    )


_AdGenPseudowireCEMPktPayloadSize_Type.__name__ = "Integer32"
_AdGenPseudowireCEMPktPayloadSize_Object = MibTableColumn
adGenPseudowireCEMPktPayloadSize = _AdGenPseudowireCEMPktPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 14),
    _AdGenPseudowireCEMPktPayloadSize_Type()
)
adGenPseudowireCEMPktPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPktPayloadSize.setStatus("current")


class _AdGenPseudowireCEMPktRTPPayloadType_Type(Integer32):
    """Custom type adGenPseudowireCEMPktRTPPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_AdGenPseudowireCEMPktRTPPayloadType_Type.__name__ = "Integer32"
_AdGenPseudowireCEMPktRTPPayloadType_Object = MibTableColumn
adGenPseudowireCEMPktRTPPayloadType = _AdGenPseudowireCEMPktRTPPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 15),
    _AdGenPseudowireCEMPktRTPPayloadType_Type()
)
adGenPseudowireCEMPktRTPPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPktRTPPayloadType.setStatus("current")


class _AdGenPseudowireCEMPktRTPFrequency_Type(Integer32):
    """Custom type adGenPseudowireCEMPktRTPFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 13200),
    )


_AdGenPseudowireCEMPktRTPFrequency_Type.__name__ = "Integer32"
_AdGenPseudowireCEMPktRTPFrequency_Object = MibTableColumn
adGenPseudowireCEMPktRTPFrequency = _AdGenPseudowireCEMPktRTPFrequency_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 16),
    _AdGenPseudowireCEMPktRTPFrequency_Type()
)
adGenPseudowireCEMPktRTPFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMPktRTPFrequency.setStatus("current")


class _AdGenPseudowireCEMDscp_Type(Integer32):
    """Custom type adGenPseudowireCEMDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenPseudowireCEMDscp_Type.__name__ = "Integer32"
_AdGenPseudowireCEMDscp_Object = MibTableColumn
adGenPseudowireCEMDscp = _AdGenPseudowireCEMDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 17),
    _AdGenPseudowireCEMDscp_Type()
)
adGenPseudowireCEMDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDscp.setStatus("current")


class _AdGenPseudowireCEMServiceState_Type(Integer32):
    """Custom type adGenPseudowireCEMServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("oosUnassigned", 2),
          ("oosMaintenance", 3))
    )


_AdGenPseudowireCEMServiceState_Type.__name__ = "Integer32"
_AdGenPseudowireCEMServiceState_Object = MibTableColumn
adGenPseudowireCEMServiceState = _AdGenPseudowireCEMServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 18),
    _AdGenPseudowireCEMServiceState_Type()
)
adGenPseudowireCEMServiceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPseudowireCEMServiceState.setStatus("current")


class _AdGenPseudowireCEMDetailedOperStatus_Type(DisplayString):
    """Custom type adGenPseudowireCEMDetailedOperStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenPseudowireCEMDetailedOperStatus_Type.__name__ = "DisplayString"
_AdGenPseudowireCEMDetailedOperStatus_Object = MibTableColumn
adGenPseudowireCEMDetailedOperStatus = _AdGenPseudowireCEMDetailedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 1, 1, 1, 19),
    _AdGenPseudowireCEMDetailedOperStatus_Type()
)
adGenPseudowireCEMDetailedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMDetailedOperStatus.setStatus("current")
_AdGenAdvancedPseudowireCEMProv_ObjectIdentity = ObjectIdentity
adGenAdvancedPseudowireCEMProv = _AdGenAdvancedPseudowireCEMProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2)
)
_AdGenAdvancedPseudowireCEMProvTable_Object = MibTable
adGenAdvancedPseudowireCEMProvTable = _AdGenAdvancedPseudowireCEMProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1)
)
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMProvTable.setStatus("current")
_AdGenAdvancedPseudowireCEMProvTableEntry_Object = MibTableRow
adGenAdvancedPseudowireCEMProvTableEntry = _AdGenAdvancedPseudowireCEMProvTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1)
)
adGenAdvancedPseudowireCEMProvTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMProvTableEntry.setStatus("current")


class _AdGenAdvancedPseudowireCEMType_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("satop", 1),
          ("cesopBasic", 2),
          ("cesopCas", 3))
    )


_AdGenAdvancedPseudowireCEMType_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMType_Object = MibTableColumn
adGenAdvancedPseudowireCEMType = _AdGenAdvancedPseudowireCEMType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 1),
    _AdGenAdvancedPseudowireCEMType_Type()
)
adGenAdvancedPseudowireCEMType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMType.setStatus("current")
_AdGenAdvancedPseudowireCEMSourceUDP_Type = Integer32
_AdGenAdvancedPseudowireCEMSourceUDP_Object = MibTableColumn
adGenAdvancedPseudowireCEMSourceUDP = _AdGenAdvancedPseudowireCEMSourceUDP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 2),
    _AdGenAdvancedPseudowireCEMSourceUDP_Type()
)
adGenAdvancedPseudowireCEMSourceUDP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMSourceUDP.setStatus("current")
_AdGenAdvancedPseudowireCEMPhysicalPortIfIndex_Type = InterfaceIndexOrZero
_AdGenAdvancedPseudowireCEMPhysicalPortIfIndex_Object = MibTableColumn
adGenAdvancedPseudowireCEMPhysicalPortIfIndex = _AdGenAdvancedPseudowireCEMPhysicalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 3),
    _AdGenAdvancedPseudowireCEMPhysicalPortIfIndex_Type()
)
adGenAdvancedPseudowireCEMPhysicalPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMPhysicalPortIfIndex.setStatus("current")
_AdGenAdvancedPseudowireCEMDestinationUDP_Type = Integer32
_AdGenAdvancedPseudowireCEMDestinationUDP_Object = MibTableColumn
adGenAdvancedPseudowireCEMDestinationUDP = _AdGenAdvancedPseudowireCEMDestinationUDP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 4),
    _AdGenAdvancedPseudowireCEMDestinationUDP_Type()
)
adGenAdvancedPseudowireCEMDestinationUDP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMDestinationUDP.setStatus("current")
_AdGenAdvancedPseudowireCEMDestinationIP_Type = IpAddress
_AdGenAdvancedPseudowireCEMDestinationIP_Object = MibTableColumn
adGenAdvancedPseudowireCEMDestinationIP = _AdGenAdvancedPseudowireCEMDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 5),
    _AdGenAdvancedPseudowireCEMDestinationIP_Type()
)
adGenAdvancedPseudowireCEMDestinationIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMDestinationIP.setStatus("current")
_AdGenAdvancedPseudowireCEMDestinationMac_Type = MacAddress
_AdGenAdvancedPseudowireCEMDestinationMac_Object = MibTableColumn
adGenAdvancedPseudowireCEMDestinationMac = _AdGenAdvancedPseudowireCEMDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 6),
    _AdGenAdvancedPseudowireCEMDestinationMac_Type()
)
adGenAdvancedPseudowireCEMDestinationMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMDestinationMac.setStatus("current")
_AdGenAdvancedPseudowireCEMRowStatus_Type = RowStatus
_AdGenAdvancedPseudowireCEMRowStatus_Object = MibTableColumn
adGenAdvancedPseudowireCEMRowStatus = _AdGenAdvancedPseudowireCEMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 7),
    _AdGenAdvancedPseudowireCEMRowStatus_Type()
)
adGenAdvancedPseudowireCEMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMRowStatus.setStatus("current")
_AdGenAdvancedPseudowireCEMErrorStr_Type = DisplayString
_AdGenAdvancedPseudowireCEMErrorStr_Object = MibTableColumn
adGenAdvancedPseudowireCEMErrorStr = _AdGenAdvancedPseudowireCEMErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 8),
    _AdGenAdvancedPseudowireCEMErrorStr_Type()
)
adGenAdvancedPseudowireCEMErrorStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMErrorStr.setStatus("current")
_AdGenAdvancedPseudowireCEMCircuitIdentifierStr_Type = DisplayString
_AdGenAdvancedPseudowireCEMCircuitIdentifierStr_Object = MibTableColumn
adGenAdvancedPseudowireCEMCircuitIdentifierStr = _AdGenAdvancedPseudowireCEMCircuitIdentifierStr_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 9),
    _AdGenAdvancedPseudowireCEMCircuitIdentifierStr_Type()
)
adGenAdvancedPseudowireCEMCircuitIdentifierStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMCircuitIdentifierStr.setStatus("current")


class _AdGenAdvancedPseudowireCEMPktJitterBufferDepth_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMPktJitterBufferDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AdGenAdvancedPseudowireCEMPktJitterBufferDepth_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMPktJitterBufferDepth_Object = MibTableColumn
adGenAdvancedPseudowireCEMPktJitterBufferDepth = _AdGenAdvancedPseudowireCEMPktJitterBufferDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 10),
    _AdGenAdvancedPseudowireCEMPktJitterBufferDepth_Type()
)
adGenAdvancedPseudowireCEMPktJitterBufferDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMPktJitterBufferDepth.setStatus("current")


class _AdGenAdvancedPseudowireCEMPktPayloadSize_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMPktPayloadSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 958),
    )


_AdGenAdvancedPseudowireCEMPktPayloadSize_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMPktPayloadSize_Object = MibTableColumn
adGenAdvancedPseudowireCEMPktPayloadSize = _AdGenAdvancedPseudowireCEMPktPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 11),
    _AdGenAdvancedPseudowireCEMPktPayloadSize_Type()
)
adGenAdvancedPseudowireCEMPktPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMPktPayloadSize.setStatus("current")


class _AdGenAdvancedPseudowireCEMPktRTPPayloadType_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMPktRTPPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(96, 127),
    )


_AdGenAdvancedPseudowireCEMPktRTPPayloadType_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMPktRTPPayloadType_Object = MibTableColumn
adGenAdvancedPseudowireCEMPktRTPPayloadType = _AdGenAdvancedPseudowireCEMPktRTPPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 12),
    _AdGenAdvancedPseudowireCEMPktRTPPayloadType_Type()
)
adGenAdvancedPseudowireCEMPktRTPPayloadType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMPktRTPPayloadType.setStatus("current")


class _AdGenAdvancedPseudowireCEMPktRTPFrequency_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMPktRTPFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 13200),
    )


_AdGenAdvancedPseudowireCEMPktRTPFrequency_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMPktRTPFrequency_Object = MibTableColumn
adGenAdvancedPseudowireCEMPktRTPFrequency = _AdGenAdvancedPseudowireCEMPktRTPFrequency_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 13),
    _AdGenAdvancedPseudowireCEMPktRTPFrequency_Type()
)
adGenAdvancedPseudowireCEMPktRTPFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMPktRTPFrequency.setStatus("current")


class _AdGenAdvancedPseudowireCEMDscp_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenAdvancedPseudowireCEMDscp_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMDscp_Object = MibTableColumn
adGenAdvancedPseudowireCEMDscp = _AdGenAdvancedPseudowireCEMDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 14),
    _AdGenAdvancedPseudowireCEMDscp_Type()
)
adGenAdvancedPseudowireCEMDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMDscp.setStatus("current")


class _AdGenAdvancedPseudowireCEMServiceState_Type(Integer32):
    """Custom type adGenAdvancedPseudowireCEMServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("oosUnassigned", 2),
          ("oosMaintenance", 3))
    )


_AdGenAdvancedPseudowireCEMServiceState_Type.__name__ = "Integer32"
_AdGenAdvancedPseudowireCEMServiceState_Object = MibTableColumn
adGenAdvancedPseudowireCEMServiceState = _AdGenAdvancedPseudowireCEMServiceState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 15),
    _AdGenAdvancedPseudowireCEMServiceState_Type()
)
adGenAdvancedPseudowireCEMServiceState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMServiceState.setStatus("current")


class _AdGenAdvancedPseudowireCEMDetailedOperStatus_Type(DisplayString):
    """Custom type adGenAdvancedPseudowireCEMDetailedOperStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenAdvancedPseudowireCEMDetailedOperStatus_Type.__name__ = "DisplayString"
_AdGenAdvancedPseudowireCEMDetailedOperStatus_Object = MibTableColumn
adGenAdvancedPseudowireCEMDetailedOperStatus = _AdGenAdvancedPseudowireCEMDetailedOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 2, 1, 1, 16),
    _AdGenAdvancedPseudowireCEMDetailedOperStatus_Type()
)
adGenAdvancedPseudowireCEMDetailedOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenAdvancedPseudowireCEMDetailedOperStatus.setStatus("current")
_AdGenPseudowireCEMCesopTimeslotProv_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMCesopTimeslotProv = _AdGenPseudowireCEMCesopTimeslotProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3)
)
_AdGenPseudowireCEMCesopTimeslotTable_Object = MibTable
adGenPseudowireCEMCesopTimeslotTable = _AdGenPseudowireCEMCesopTimeslotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1)
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopTimeslotTable.setStatus("current")
_AdGenPseudowireCEMCesopTimeslotTableEntry_Object = MibTableRow
adGenPseudowireCEMCesopTimeslotTableEntry = _AdGenPseudowireCEMCesopTimeslotTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1, 1)
)
adGenPseudowireCEMCesopTimeslotTableEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMCesopPweIfIndex"),
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMCesopPweTimeslot"),
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMCesopPhysicalPortIfIndex"),
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenPseudowireCEMCesopPhyTimeslot"),
)
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopTimeslotTableEntry.setStatus("current")
_AdGenPseudowireCEMCesopPweIfIndex_Type = InterfaceIndex
_AdGenPseudowireCEMCesopPweIfIndex_Object = MibTableColumn
adGenPseudowireCEMCesopPweIfIndex = _AdGenPseudowireCEMCesopPweIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1, 1, 1),
    _AdGenPseudowireCEMCesopPweIfIndex_Type()
)
adGenPseudowireCEMCesopPweIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopPweIfIndex.setStatus("current")
_AdGenPseudowireCEMCesopPweTimeslot_Type = Integer32
_AdGenPseudowireCEMCesopPweTimeslot_Object = MibTableColumn
adGenPseudowireCEMCesopPweTimeslot = _AdGenPseudowireCEMCesopPweTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1, 1, 2),
    _AdGenPseudowireCEMCesopPweTimeslot_Type()
)
adGenPseudowireCEMCesopPweTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopPweTimeslot.setStatus("current")
_AdGenPseudowireCEMCesopPhysicalPortIfIndex_Type = InterfaceIndex
_AdGenPseudowireCEMCesopPhysicalPortIfIndex_Object = MibTableColumn
adGenPseudowireCEMCesopPhysicalPortIfIndex = _AdGenPseudowireCEMCesopPhysicalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1, 1, 3),
    _AdGenPseudowireCEMCesopPhysicalPortIfIndex_Type()
)
adGenPseudowireCEMCesopPhysicalPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopPhysicalPortIfIndex.setStatus("current")
_AdGenPseudowireCEMCesopPhyTimeslot_Type = Integer32
_AdGenPseudowireCEMCesopPhyTimeslot_Object = MibTableColumn
adGenPseudowireCEMCesopPhyTimeslot = _AdGenPseudowireCEMCesopPhyTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1, 1, 4),
    _AdGenPseudowireCEMCesopPhyTimeslot_Type()
)
adGenPseudowireCEMCesopPhyTimeslot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopPhyTimeslot.setStatus("current")


class _AdGenPseudowireCEMCesopConnectionStatus_Type(Integer32):
    """Custom type adGenPseudowireCEMCesopConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("connected", 1)
    )


_AdGenPseudowireCEMCesopConnectionStatus_Type.__name__ = "Integer32"
_AdGenPseudowireCEMCesopConnectionStatus_Object = MibTableColumn
adGenPseudowireCEMCesopConnectionStatus = _AdGenPseudowireCEMCesopConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 3, 1, 1, 5),
    _AdGenPseudowireCEMCesopConnectionStatus_Type()
)
adGenPseudowireCEMCesopConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPseudowireCEMCesopConnectionStatus.setStatus("current")
_AdGenEasyPseudowireCEMProv_ObjectIdentity = ObjectIdentity
adGenEasyPseudowireCEMProv = _AdGenEasyPseudowireCEMProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4)
)
_AdGenEasyPseudowireCEMGetNextTable_Object = MibTable
adGenEasyPseudowireCEMGetNextTable = _AdGenEasyPseudowireCEMGetNextTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 1)
)
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMGetNextTable.setStatus("current")
_AdGenEasyPseudowireCEMGetNextEntry_Object = MibTableRow
adGenEasyPseudowireCEMGetNextEntry = _AdGenEasyPseudowireCEMGetNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 1, 1)
)
adGenEasyPseudowireCEMGetNextEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMGetNextEntry.setStatus("current")
_AdGenEasyPseudowireCEMNextIndex_Type = Integer32
_AdGenEasyPseudowireCEMNextIndex_Object = MibTableColumn
adGenEasyPseudowireCEMNextIndex = _AdGenEasyPseudowireCEMNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 1, 1, 1),
    _AdGenEasyPseudowireCEMNextIndex_Type()
)
adGenEasyPseudowireCEMNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMNextIndex.setStatus("current")
_AdGenEasyPseudowireCEMTimeslotTable_Object = MibTable
adGenEasyPseudowireCEMTimeslotTable = _AdGenEasyPseudowireCEMTimeslotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2)
)
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMTimeslotTable.setStatus("current")
_AdGenEasyPseudowireCEMTimeslotEntry_Object = MibTableRow
adGenEasyPseudowireCEMTimeslotEntry = _AdGenEasyPseudowireCEMTimeslotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1)
)
adGenEasyPseudowireCEMTimeslotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB", "adGenEasyPseudowireCEMIndex"),
)
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMTimeslotEntry.setStatus("current")
_AdGenEasyPseudowireCEMIndex_Type = Integer32
_AdGenEasyPseudowireCEMIndex_Object = MibTableColumn
adGenEasyPseudowireCEMIndex = _AdGenEasyPseudowireCEMIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 1),
    _AdGenEasyPseudowireCEMIndex_Type()
)
adGenEasyPseudowireCEMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMIndex.setStatus("current")
_AdGenEasyPseudowireCEMPweIfIndex_Type = InterfaceIndex
_AdGenEasyPseudowireCEMPweIfIndex_Object = MibTableColumn
adGenEasyPseudowireCEMPweIfIndex = _AdGenEasyPseudowireCEMPweIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 2),
    _AdGenEasyPseudowireCEMPweIfIndex_Type()
)
adGenEasyPseudowireCEMPweIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMPweIfIndex.setStatus("current")
_AdGenEasyPseudowireCEMStartingPweTimeslot_Type = Integer32
_AdGenEasyPseudowireCEMStartingPweTimeslot_Object = MibTableColumn
adGenEasyPseudowireCEMStartingPweTimeslot = _AdGenEasyPseudowireCEMStartingPweTimeslot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 3),
    _AdGenEasyPseudowireCEMStartingPweTimeslot_Type()
)
adGenEasyPseudowireCEMStartingPweTimeslot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMStartingPweTimeslot.setStatus("current")
_AdGenEasyPseudowireCEMPhysicalPortIfIndex_Type = InterfaceIndex
_AdGenEasyPseudowireCEMPhysicalPortIfIndex_Object = MibTableColumn
adGenEasyPseudowireCEMPhysicalPortIfIndex = _AdGenEasyPseudowireCEMPhysicalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 4),
    _AdGenEasyPseudowireCEMPhysicalPortIfIndex_Type()
)
adGenEasyPseudowireCEMPhysicalPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMPhysicalPortIfIndex.setStatus("current")
_AdGenEasyPseudowireCEMPhyTimeslots_Type = OctetString
_AdGenEasyPseudowireCEMPhyTimeslots_Object = MibTableColumn
adGenEasyPseudowireCEMPhyTimeslots = _AdGenEasyPseudowireCEMPhyTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 5),
    _AdGenEasyPseudowireCEMPhyTimeslots_Type()
)
adGenEasyPseudowireCEMPhyTimeslots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMPhyTimeslots.setStatus("current")


class _AdGenEasyPseudowireCEMAction_Type(Integer32):
    """Custom type adGenEasyPseudowireCEMAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("remove", 2))
    )


_AdGenEasyPseudowireCEMAction_Type.__name__ = "Integer32"
_AdGenEasyPseudowireCEMAction_Object = MibTableColumn
adGenEasyPseudowireCEMAction = _AdGenEasyPseudowireCEMAction_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 6),
    _AdGenEasyPseudowireCEMAction_Type()
)
adGenEasyPseudowireCEMAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMAction.setStatus("current")
_AdGenEasyPseudowireCEMErrorString_Type = DisplayString
_AdGenEasyPseudowireCEMErrorString_Object = MibTableColumn
adGenEasyPseudowireCEMErrorString = _AdGenEasyPseudowireCEMErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 7),
    _AdGenEasyPseudowireCEMErrorString_Type()
)
adGenEasyPseudowireCEMErrorString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMErrorString.setStatus("current")


class _AdGenEasyPseudowireCEMStatusString_Type(Integer32):
    """Custom type adGenEasyPseudowireCEMStatusString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2),
          ("inProgress", 3))
    )


_AdGenEasyPseudowireCEMStatusString_Type.__name__ = "Integer32"
_AdGenEasyPseudowireCEMStatusString_Object = MibTableColumn
adGenEasyPseudowireCEMStatusString = _AdGenEasyPseudowireCEMStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 8),
    _AdGenEasyPseudowireCEMStatusString_Type()
)
adGenEasyPseudowireCEMStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMStatusString.setStatus("current")
_AdGenEasyPseudowireCEMRowStatus_Type = RowStatus
_AdGenEasyPseudowireCEMRowStatus_Object = MibTableColumn
adGenEasyPseudowireCEMRowStatus = _AdGenEasyPseudowireCEMRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 4, 2, 1, 9),
    _AdGenEasyPseudowireCEMRowStatus_Type()
)
adGenEasyPseudowireCEMRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEasyPseudowireCEMRowStatus.setStatus("current")
_AdGenPseudowireCEMPerformance_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMPerformance = _AdGenPseudowireCEMPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5)
)
_AdGenPseudowireCEMPerfInfo_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMPerfInfo = _AdGenPseudowireCEMPerfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 5, 2)
)
_AdGenPseudowireCEMAlarms_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMAlarms = _AdGenPseudowireCEMAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6)
)
_AdGenPseudowireCEMEvents_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMEvents = _AdGenPseudowireCEMEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 6, 0)
)
_AdGenPseudowireCEMAlarmProv_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMAlarmProv = _AdGenPseudowireCEMAlarmProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 30, 7)
)
_AdGenPseudowireCEMPerfID_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMPerfID = _AdGenPseudowireCEMPerfID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 2)
)
_AdGenPseudowireCEMPerfInfoID_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMPerfInfoID = _AdGenPseudowireCEMPerfInfoID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 2, 2)
)
_AdGenPseudowireCEMAlarmsID_ObjectIdentity = ObjectIdentity
adGenPseudowireCEMAlarmsID = _AdGenPseudowireCEMAlarmsID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 30, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PSEUDOWIRE-CEM-MGMT-MIB",
    **{"adGenPseudowireCEMProv": adGenPseudowireCEMProv,
       "adGenPseudowireCEMProvTable": adGenPseudowireCEMProvTable,
       "adGenPseudowireCEMProvTableEntry": adGenPseudowireCEMProvTableEntry,
       "adGenPseudowireCEMType": adGenPseudowireCEMType,
       "adGenPseudowireCEMPhysicalPortIfIndex": adGenPseudowireCEMPhysicalPortIfIndex,
       "adGenPseudowireCEMDestinationNode": adGenPseudowireCEMDestinationNode,
       "adGenPseudowireCEMDestinationShelf": adGenPseudowireCEMDestinationShelf,
       "adGenPseudowireCEMDestinationSlot": adGenPseudowireCEMDestinationSlot,
       "adGenPseudowireCEMDestinationChannel": adGenPseudowireCEMDestinationChannel,
       "adGenPseudowireCEMDestinationONTNumber": adGenPseudowireCEMDestinationONTNumber,
       "adGenPseudowireCEMDestinationONTSlot": adGenPseudowireCEMDestinationONTSlot,
       "adGenPseudowireCEMDestinationONTPort": adGenPseudowireCEMDestinationONTPort,
       "adGenPseudowireCEMRowStatus": adGenPseudowireCEMRowStatus,
       "adGenPseudowireCEMErrorStr": adGenPseudowireCEMErrorStr,
       "adGenPseudowireCEMCircuitIdentifierStr": adGenPseudowireCEMCircuitIdentifierStr,
       "adGenPseudowireCEMPktJitterBufferDepth": adGenPseudowireCEMPktJitterBufferDepth,
       "adGenPseudowireCEMPktPayloadSize": adGenPseudowireCEMPktPayloadSize,
       "adGenPseudowireCEMPktRTPPayloadType": adGenPseudowireCEMPktRTPPayloadType,
       "adGenPseudowireCEMPktRTPFrequency": adGenPseudowireCEMPktRTPFrequency,
       "adGenPseudowireCEMDscp": adGenPseudowireCEMDscp,
       "adGenPseudowireCEMServiceState": adGenPseudowireCEMServiceState,
       "adGenPseudowireCEMDetailedOperStatus": adGenPseudowireCEMDetailedOperStatus,
       "adGenAdvancedPseudowireCEMProv": adGenAdvancedPseudowireCEMProv,
       "adGenAdvancedPseudowireCEMProvTable": adGenAdvancedPseudowireCEMProvTable,
       "adGenAdvancedPseudowireCEMProvTableEntry": adGenAdvancedPseudowireCEMProvTableEntry,
       "adGenAdvancedPseudowireCEMType": adGenAdvancedPseudowireCEMType,
       "adGenAdvancedPseudowireCEMSourceUDP": adGenAdvancedPseudowireCEMSourceUDP,
       "adGenAdvancedPseudowireCEMPhysicalPortIfIndex": adGenAdvancedPseudowireCEMPhysicalPortIfIndex,
       "adGenAdvancedPseudowireCEMDestinationUDP": adGenAdvancedPseudowireCEMDestinationUDP,
       "adGenAdvancedPseudowireCEMDestinationIP": adGenAdvancedPseudowireCEMDestinationIP,
       "adGenAdvancedPseudowireCEMDestinationMac": adGenAdvancedPseudowireCEMDestinationMac,
       "adGenAdvancedPseudowireCEMRowStatus": adGenAdvancedPseudowireCEMRowStatus,
       "adGenAdvancedPseudowireCEMErrorStr": adGenAdvancedPseudowireCEMErrorStr,
       "adGenAdvancedPseudowireCEMCircuitIdentifierStr": adGenAdvancedPseudowireCEMCircuitIdentifierStr,
       "adGenAdvancedPseudowireCEMPktJitterBufferDepth": adGenAdvancedPseudowireCEMPktJitterBufferDepth,
       "adGenAdvancedPseudowireCEMPktPayloadSize": adGenAdvancedPseudowireCEMPktPayloadSize,
       "adGenAdvancedPseudowireCEMPktRTPPayloadType": adGenAdvancedPseudowireCEMPktRTPPayloadType,
       "adGenAdvancedPseudowireCEMPktRTPFrequency": adGenAdvancedPseudowireCEMPktRTPFrequency,
       "adGenAdvancedPseudowireCEMDscp": adGenAdvancedPseudowireCEMDscp,
       "adGenAdvancedPseudowireCEMServiceState": adGenAdvancedPseudowireCEMServiceState,
       "adGenAdvancedPseudowireCEMDetailedOperStatus": adGenAdvancedPseudowireCEMDetailedOperStatus,
       "adGenPseudowireCEMCesopTimeslotProv": adGenPseudowireCEMCesopTimeslotProv,
       "adGenPseudowireCEMCesopTimeslotTable": adGenPseudowireCEMCesopTimeslotTable,
       "adGenPseudowireCEMCesopTimeslotTableEntry": adGenPseudowireCEMCesopTimeslotTableEntry,
       "adGenPseudowireCEMCesopPweIfIndex": adGenPseudowireCEMCesopPweIfIndex,
       "adGenPseudowireCEMCesopPweTimeslot": adGenPseudowireCEMCesopPweTimeslot,
       "adGenPseudowireCEMCesopPhysicalPortIfIndex": adGenPseudowireCEMCesopPhysicalPortIfIndex,
       "adGenPseudowireCEMCesopPhyTimeslot": adGenPseudowireCEMCesopPhyTimeslot,
       "adGenPseudowireCEMCesopConnectionStatus": adGenPseudowireCEMCesopConnectionStatus,
       "adGenEasyPseudowireCEMProv": adGenEasyPseudowireCEMProv,
       "adGenEasyPseudowireCEMGetNextTable": adGenEasyPseudowireCEMGetNextTable,
       "adGenEasyPseudowireCEMGetNextEntry": adGenEasyPseudowireCEMGetNextEntry,
       "adGenEasyPseudowireCEMNextIndex": adGenEasyPseudowireCEMNextIndex,
       "adGenEasyPseudowireCEMTimeslotTable": adGenEasyPseudowireCEMTimeslotTable,
       "adGenEasyPseudowireCEMTimeslotEntry": adGenEasyPseudowireCEMTimeslotEntry,
       "adGenEasyPseudowireCEMIndex": adGenEasyPseudowireCEMIndex,
       "adGenEasyPseudowireCEMPweIfIndex": adGenEasyPseudowireCEMPweIfIndex,
       "adGenEasyPseudowireCEMStartingPweTimeslot": adGenEasyPseudowireCEMStartingPweTimeslot,
       "adGenEasyPseudowireCEMPhysicalPortIfIndex": adGenEasyPseudowireCEMPhysicalPortIfIndex,
       "adGenEasyPseudowireCEMPhyTimeslots": adGenEasyPseudowireCEMPhyTimeslots,
       "adGenEasyPseudowireCEMAction": adGenEasyPseudowireCEMAction,
       "adGenEasyPseudowireCEMErrorString": adGenEasyPseudowireCEMErrorString,
       "adGenEasyPseudowireCEMStatusString": adGenEasyPseudowireCEMStatusString,
       "adGenEasyPseudowireCEMRowStatus": adGenEasyPseudowireCEMRowStatus,
       "adGenPseudowireCEMPerformance": adGenPseudowireCEMPerformance,
       "adGenPseudowireCEMPerfInfo": adGenPseudowireCEMPerfInfo,
       "adGenPseudowireCEMAlarms": adGenPseudowireCEMAlarms,
       "adGenPseudowireCEMEvents": adGenPseudowireCEMEvents,
       "adGenPseudowireCEMAlarmProv": adGenPseudowireCEMAlarmProv,
       "adGenPseudowireCEMMgmtModuleIdentity": adGenPseudowireCEMMgmtModuleIdentity,
       "adGenPseudowireCEMPerfID": adGenPseudowireCEMPerfID,
       "adGenPseudowireCEMPerfInfoID": adGenPseudowireCEMPerfInfoID,
       "adGenPseudowireCEMAlarmsID": adGenPseudowireCEMAlarmsID}
)
