# SNMP MIB module (IPE-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-LAG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:46 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class IpeEnableDisableValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )



class SeverityValue(TextualConvention, Integer32):
    status = "current"
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
        *(("cleared", 1),
          ("indetermine", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsLinkAggrGroup_ObjectIdentity = ObjectIdentity
asLinkAggrGroup = _AsLinkAggrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38)
)
_AsLinkAggrGroupTable_Object = MibTable
asLinkAggrGroupTable = _AsLinkAggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1)
)
if mibBuilder.loadTexts:
    asLinkAggrGroupTable.setStatus("current")
_AsLinkAggrGroupEntry_Object = MibTableRow
asLinkAggrGroupEntry = _AsLinkAggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1, 1)
)
asLinkAggrGroupEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "asLinkAggrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    asLinkAggrGroupEntry.setStatus("current")
_AsLinkAggrGroupIfIndex_Type = InterfaceIndex
_AsLinkAggrGroupIfIndex_Object = MibTableColumn
asLinkAggrGroupIfIndex = _AsLinkAggrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1, 1, 1),
    _AsLinkAggrGroupIfIndex_Type()
)
asLinkAggrGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrGroupIfIndex.setStatus("current")
_AsLinkAggrGroupNEAddress_Type = IpAddress
_AsLinkAggrGroupNEAddress_Object = MibTableColumn
asLinkAggrGroupNEAddress = _AsLinkAggrGroupNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1, 1, 2),
    _AsLinkAggrGroupNEAddress_Type()
)
asLinkAggrGroupNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrGroupNEAddress.setStatus("current")
_AsLinkAggrGroupLinkStatus_Type = SeverityValue
_AsLinkAggrGroupLinkStatus_Object = MibTableColumn
asLinkAggrGroupLinkStatus = _AsLinkAggrGroupLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1, 1, 3),
    _AsLinkAggrGroupLinkStatus_Type()
)
asLinkAggrGroupLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrGroupLinkStatus.setStatus("current")


class _AsLinkAggrGroupLLFStatus_Type(Integer32):
    """Custom type asLinkAggrGroupLLFStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("force", 2))
    )


_AsLinkAggrGroupLLFStatus_Type.__name__ = "Integer32"
_AsLinkAggrGroupLLFStatus_Object = MibTableColumn
asLinkAggrGroupLLFStatus = _AsLinkAggrGroupLLFStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1, 1, 4),
    _AsLinkAggrGroupLLFStatus_Type()
)
asLinkAggrGroupLLFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrGroupLLFStatus.setStatus("current")


class _AsLinkAggrGroupOperStatus_Type(Integer32):
    """Custom type asLinkAggrGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("linkDown", 1),
          ("linkUp", 2))
    )


_AsLinkAggrGroupOperStatus_Type.__name__ = "Integer32"
_AsLinkAggrGroupOperStatus_Object = MibTableColumn
asLinkAggrGroupOperStatus = _AsLinkAggrGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 1, 1, 5),
    _AsLinkAggrGroupOperStatus_Type()
)
asLinkAggrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrGroupOperStatus.setStatus("current")
_AsLinkAggrPortTable_Object = MibTable
asLinkAggrPortTable = _AsLinkAggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2)
)
if mibBuilder.loadTexts:
    asLinkAggrPortTable.setStatus("current")
_AsLinkAggrPortEntry_Object = MibTableRow
asLinkAggrPortEntry = _AsLinkAggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1)
)
asLinkAggrPortEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "asLinkAggrPortGroupIfIndex"),
    (0, "IPE-LAG-MIB", "asLinkAggrPortIfIndex"),
)
if mibBuilder.loadTexts:
    asLinkAggrPortEntry.setStatus("current")
_AsLinkAggrPortGroupIfIndex_Type = InterfaceIndex
_AsLinkAggrPortGroupIfIndex_Object = MibTableColumn
asLinkAggrPortGroupIfIndex = _AsLinkAggrPortGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 1),
    _AsLinkAggrPortGroupIfIndex_Type()
)
asLinkAggrPortGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrPortGroupIfIndex.setStatus("current")
_AsLinkAggrPortIfIndex_Type = InterfaceIndex
_AsLinkAggrPortIfIndex_Object = MibTableColumn
asLinkAggrPortIfIndex = _AsLinkAggrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 2),
    _AsLinkAggrPortIfIndex_Type()
)
asLinkAggrPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrPortIfIndex.setStatus("current")
_AsLinkAggrPortNEAddress_Type = IpAddress
_AsLinkAggrPortNEAddress_Object = MibTableColumn
asLinkAggrPortNEAddress = _AsLinkAggrPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 3),
    _AsLinkAggrPortNEAddress_Type()
)
asLinkAggrPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrPortNEAddress.setStatus("current")


class _AsLinkAggrPortStatus_Type(Integer32):
    """Custom type asLinkAggrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("active", 1),
          ("standby", 2))
    )


_AsLinkAggrPortStatus_Type.__name__ = "Integer32"
_AsLinkAggrPortStatus_Object = MibTableColumn
asLinkAggrPortStatus = _AsLinkAggrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 4),
    _AsLinkAggrPortStatus_Type()
)
asLinkAggrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatus.setStatus("current")


class _AsLinkAggrPortActorLacpStatus_Type(Bits):
    """Custom type asLinkAggrPortActorLacpStatus based on Bits"""
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )

_AsLinkAggrPortActorLacpStatus_Type.__name__ = "Bits"
_AsLinkAggrPortActorLacpStatus_Object = MibTableColumn
asLinkAggrPortActorLacpStatus = _AsLinkAggrPortActorLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 5),
    _AsLinkAggrPortActorLacpStatus_Type()
)
asLinkAggrPortActorLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortActorLacpStatus.setStatus("current")


class _AsLinkAggrPortPartnerLacpStatus_Type(Bits):
    """Custom type asLinkAggrPortPartnerLacpStatus based on Bits"""
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )

_AsLinkAggrPortPartnerLacpStatus_Type.__name__ = "Bits"
_AsLinkAggrPortPartnerLacpStatus_Object = MibTableColumn
asLinkAggrPortPartnerLacpStatus = _AsLinkAggrPortPartnerLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 6),
    _AsLinkAggrPortPartnerLacpStatus_Type()
)
asLinkAggrPortPartnerLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortPartnerLacpStatus.setStatus("current")


class _AsLinkAggrPortLoopDetect_Type(Integer32):
    """Custom type asLinkAggrPortLoopDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("detected", 2))
    )


_AsLinkAggrPortLoopDetect_Type.__name__ = "Integer32"
_AsLinkAggrPortLoopDetect_Object = MibTableColumn
asLinkAggrPortLoopDetect = _AsLinkAggrPortLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 2, 1, 7),
    _AsLinkAggrPortLoopDetect_Type()
)
asLinkAggrPortLoopDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortLoopDetect.setStatus("current")
_AsLinkAggrPortStatsTable_Object = MibTable
asLinkAggrPortStatsTable = _AsLinkAggrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3)
)
if mibBuilder.loadTexts:
    asLinkAggrPortStatsTable.setStatus("current")
_AsLinkAggrPortStatsEntry_Object = MibTableRow
asLinkAggrPortStatsEntry = _AsLinkAggrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1)
)
asLinkAggrPortStatsEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "asLinkAggrPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    asLinkAggrPortStatsEntry.setStatus("current")
_AsLinkAggrPortStatsIfIndex_Type = InterfaceIndex
_AsLinkAggrPortStatsIfIndex_Object = MibTableColumn
asLinkAggrPortStatsIfIndex = _AsLinkAggrPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 1),
    _AsLinkAggrPortStatsIfIndex_Type()
)
asLinkAggrPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsIfIndex.setStatus("current")
_AsLinkAggrPortStatsNEAddress_Type = IpAddress
_AsLinkAggrPortStatsNEAddress_Object = MibTableColumn
asLinkAggrPortStatsNEAddress = _AsLinkAggrPortStatsNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 2),
    _AsLinkAggrPortStatsNEAddress_Type()
)
asLinkAggrPortStatsNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsNEAddress.setStatus("current")
_AsLinkAggrPortStatsLACPDUsRx_Type = Counter32
_AsLinkAggrPortStatsLACPDUsRx_Object = MibTableColumn
asLinkAggrPortStatsLACPDUsRx = _AsLinkAggrPortStatsLACPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 3),
    _AsLinkAggrPortStatsLACPDUsRx_Type()
)
asLinkAggrPortStatsLACPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsLACPDUsRx.setStatus("current")
_AsLinkAggrPortStatsLACPDUsTx_Type = Counter32
_AsLinkAggrPortStatsLACPDUsTx_Object = MibTableColumn
asLinkAggrPortStatsLACPDUsTx = _AsLinkAggrPortStatsLACPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 4),
    _AsLinkAggrPortStatsLACPDUsTx_Type()
)
asLinkAggrPortStatsLACPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsLACPDUsTx.setStatus("current")
_AsLinkAggrPortStatsMarkerPDUsRx_Type = Counter32
_AsLinkAggrPortStatsMarkerPDUsRx_Object = MibTableColumn
asLinkAggrPortStatsMarkerPDUsRx = _AsLinkAggrPortStatsMarkerPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 5),
    _AsLinkAggrPortStatsMarkerPDUsRx_Type()
)
asLinkAggrPortStatsMarkerPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsMarkerPDUsRx.setStatus("current")
_AsLinkAggrPortStatsMarkerRespPDUsRx_Type = Counter32
_AsLinkAggrPortStatsMarkerRespPDUsRx_Object = MibTableColumn
asLinkAggrPortStatsMarkerRespPDUsRx = _AsLinkAggrPortStatsMarkerRespPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 6),
    _AsLinkAggrPortStatsMarkerRespPDUsRx_Type()
)
asLinkAggrPortStatsMarkerRespPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsMarkerRespPDUsRx.setStatus("current")
_AsLinkAggrPortStatsMarkerPDUsTx_Type = Counter32
_AsLinkAggrPortStatsMarkerPDUsTx_Object = MibTableColumn
asLinkAggrPortStatsMarkerPDUsTx = _AsLinkAggrPortStatsMarkerPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 7),
    _AsLinkAggrPortStatsMarkerPDUsTx_Type()
)
asLinkAggrPortStatsMarkerPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsMarkerPDUsTx.setStatus("current")
_AsLinkAggrPortStatsMarkerRespPDUsTx_Type = Counter32
_AsLinkAggrPortStatsMarkerRespPDUsTx_Object = MibTableColumn
asLinkAggrPortStatsMarkerRespPDUsTx = _AsLinkAggrPortStatsMarkerRespPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 38, 3, 1, 8),
    _AsLinkAggrPortStatsMarkerRespPDUsTx_Type()
)
asLinkAggrPortStatsMarkerRespPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLinkAggrPortStatsMarkerRespPDUsTx.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvLinkAggrGroup_ObjectIdentity = ObjectIdentity
provLinkAggrGroup = _ProvLinkAggrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38)
)
_ProvLinkAggrGroupTable_Object = MibTable
provLinkAggrGroupTable = _ProvLinkAggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1)
)
if mibBuilder.loadTexts:
    provLinkAggrGroupTable.setStatus("current")
_ProvLinkAggrGroupEntry_Object = MibTableRow
provLinkAggrGroupEntry = _ProvLinkAggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1)
)
provLinkAggrGroupEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "provLinkAggrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    provLinkAggrGroupEntry.setStatus("current")
_ProvLinkAggrGroupIfIndex_Type = InterfaceIndex
_ProvLinkAggrGroupIfIndex_Object = MibTableColumn
provLinkAggrGroupIfIndex = _ProvLinkAggrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 1),
    _ProvLinkAggrGroupIfIndex_Type()
)
provLinkAggrGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrGroupIfIndex.setStatus("current")
_ProvLinkAggrGroupNEAddress_Type = IpAddress
_ProvLinkAggrGroupNEAddress_Object = MibTableColumn
provLinkAggrGroupNEAddress = _ProvLinkAggrGroupNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 2),
    _ProvLinkAggrGroupNEAddress_Type()
)
provLinkAggrGroupNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrGroupNEAddress.setStatus("current")


class _ProvLinkAggrGroupMode_Type(Integer32):
    """Custom type provLinkAggrGroupMode based on Integer32"""
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
        *(("invalid", 0),
          ("active", 1),
          ("passive", 2),
          ("local", 3))
    )


_ProvLinkAggrGroupMode_Type.__name__ = "Integer32"
_ProvLinkAggrGroupMode_Object = MibTableColumn
provLinkAggrGroupMode = _ProvLinkAggrGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 3),
    _ProvLinkAggrGroupMode_Type()
)
provLinkAggrGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMode.setStatus("current")


class _ProvLinkAggrGrLacpTxInterval_Type(Integer32):
    """Custom type provLinkAggrGrLacpTxInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("short", 1),
          ("long", 2))
    )


_ProvLinkAggrGrLacpTxInterval_Type.__name__ = "Integer32"
_ProvLinkAggrGrLacpTxInterval_Object = MibTableColumn
provLinkAggrGrLacpTxInterval = _ProvLinkAggrGrLacpTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 4),
    _ProvLinkAggrGrLacpTxInterval_Type()
)
provLinkAggrGrLacpTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGrLacpTxInterval.setStatus("current")


class _ProvLinkAggrGroupRevertive_Type(IpeEnableDisableValue):
    """Custom type provLinkAggrGroupRevertive based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvLinkAggrGroupRevertive_Type.__name__ = "IpeEnableDisableValue"
_ProvLinkAggrGroupRevertive_Object = MibTableColumn
provLinkAggrGroupRevertive = _ProvLinkAggrGroupRevertive_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 5),
    _ProvLinkAggrGroupRevertive_Type()
)
provLinkAggrGroupRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupRevertive.setStatus("current")


class _ProvLinkAggrGroupTxType_Type(Integer32):
    """Custom type provLinkAggrGroupTxType based on Integer32"""
    defaultValue = 1

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
        *(("invalid", 0),
          ("macVid", 1),
          ("mplsLabel", 2),
          ("ipVid", 3))
    )


_ProvLinkAggrGroupTxType_Type.__name__ = "Integer32"
_ProvLinkAggrGroupTxType_Object = MibTableColumn
provLinkAggrGroupTxType = _ProvLinkAggrGroupTxType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 6),
    _ProvLinkAggrGroupTxType_Type()
)
provLinkAggrGroupTxType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupTxType.setStatus("current")


class _ProvLinkAggrGroupName_Type(DisplayString):
    """Custom type provLinkAggrGroupName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvLinkAggrGroupName_Type.__name__ = "DisplayString"
_ProvLinkAggrGroupName_Object = MibTableColumn
provLinkAggrGroupName = _ProvLinkAggrGroupName_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 7),
    _ProvLinkAggrGroupName_Type()
)
provLinkAggrGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupName.setStatus("current")
_ProvLinkAggrGroupRowStatus_Type = RowStatus
_ProvLinkAggrGroupRowStatus_Object = MibTableColumn
provLinkAggrGroupRowStatus = _ProvLinkAggrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 8),
    _ProvLinkAggrGroupRowStatus_Type()
)
provLinkAggrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupRowStatus.setStatus("current")


class _ProvLinkAggrGroupMemberPort1_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort1 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort1_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort1_Object = MibTableColumn
provLinkAggrGroupMemberPort1 = _ProvLinkAggrGroupMemberPort1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 9),
    _ProvLinkAggrGroupMemberPort1_Type()
)
provLinkAggrGroupMemberPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort1.setStatus("current")


class _ProvLinkAggrGroupMemberPort2_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort2 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort2_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort2_Object = MibTableColumn
provLinkAggrGroupMemberPort2 = _ProvLinkAggrGroupMemberPort2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 10),
    _ProvLinkAggrGroupMemberPort2_Type()
)
provLinkAggrGroupMemberPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort2.setStatus("current")


class _ProvLinkAggrGroupMemberPort3_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort3 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort3_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort3_Object = MibTableColumn
provLinkAggrGroupMemberPort3 = _ProvLinkAggrGroupMemberPort3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 11),
    _ProvLinkAggrGroupMemberPort3_Type()
)
provLinkAggrGroupMemberPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort3.setStatus("current")


class _ProvLinkAggrGroupMemberPort4_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort4 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort4_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort4_Object = MibTableColumn
provLinkAggrGroupMemberPort4 = _ProvLinkAggrGroupMemberPort4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 12),
    _ProvLinkAggrGroupMemberPort4_Type()
)
provLinkAggrGroupMemberPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort4.setStatus("current")


class _ProvLinkAggrGroupMemberPort5_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort5 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort5_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort5_Object = MibTableColumn
provLinkAggrGroupMemberPort5 = _ProvLinkAggrGroupMemberPort5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 13),
    _ProvLinkAggrGroupMemberPort5_Type()
)
provLinkAggrGroupMemberPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort5.setStatus("current")


class _ProvLinkAggrGroupMemberPort6_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort6 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort6_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort6_Object = MibTableColumn
provLinkAggrGroupMemberPort6 = _ProvLinkAggrGroupMemberPort6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 14),
    _ProvLinkAggrGroupMemberPort6_Type()
)
provLinkAggrGroupMemberPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort6.setStatus("current")


class _ProvLinkAggrGroupMemberPort7_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort7 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort7_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort7_Object = MibTableColumn
provLinkAggrGroupMemberPort7 = _ProvLinkAggrGroupMemberPort7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 15),
    _ProvLinkAggrGroupMemberPort7_Type()
)
provLinkAggrGroupMemberPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort7.setStatus("current")


class _ProvLinkAggrGroupMemberPort8_Type(InterfaceIndexOrZero):
    """Custom type provLinkAggrGroupMemberPort8 based on InterfaceIndexOrZero"""
    defaultValue = 0


_ProvLinkAggrGroupMemberPort8_Type.__name__ = "InterfaceIndexOrZero"
_ProvLinkAggrGroupMemberPort8_Object = MibTableColumn
provLinkAggrGroupMemberPort8 = _ProvLinkAggrGroupMemberPort8_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 1, 1, 16),
    _ProvLinkAggrGroupMemberPort8_Type()
)
provLinkAggrGroupMemberPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    provLinkAggrGroupMemberPort8.setStatus("current")
_ProvLinkAggrPortTable_Object = MibTable
provLinkAggrPortTable = _ProvLinkAggrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 2)
)
if mibBuilder.loadTexts:
    provLinkAggrPortTable.setStatus("current")
_ProvLinkAggrPortEntry_Object = MibTableRow
provLinkAggrPortEntry = _ProvLinkAggrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 2, 1)
)
provLinkAggrPortEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "provLinkAggrPortGroupIfIndex"),
    (0, "IPE-LAG-MIB", "provLinkAggrPortIfIndex"),
)
if mibBuilder.loadTexts:
    provLinkAggrPortEntry.setStatus("current")
_ProvLinkAggrPortGroupIfIndex_Type = InterfaceIndex
_ProvLinkAggrPortGroupIfIndex_Object = MibTableColumn
provLinkAggrPortGroupIfIndex = _ProvLinkAggrPortGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 2, 1, 1),
    _ProvLinkAggrPortGroupIfIndex_Type()
)
provLinkAggrPortGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrPortGroupIfIndex.setStatus("current")
_ProvLinkAggrPortIfIndex_Type = InterfaceIndex
_ProvLinkAggrPortIfIndex_Object = MibTableColumn
provLinkAggrPortIfIndex = _ProvLinkAggrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 2, 1, 2),
    _ProvLinkAggrPortIfIndex_Type()
)
provLinkAggrPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrPortIfIndex.setStatus("current")
_ProvLinkAggrPortNEAddress_Type = IpAddress
_ProvLinkAggrPortNEAddress_Object = MibTableColumn
provLinkAggrPortNEAddress = _ProvLinkAggrPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 2, 1, 3),
    _ProvLinkAggrPortNEAddress_Type()
)
provLinkAggrPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrPortNEAddress.setStatus("current")


class _ProvLinkAggrPortRole_Type(Integer32):
    """Custom type provLinkAggrPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("active", 1),
          ("standby", 2))
    )


_ProvLinkAggrPortRole_Type.__name__ = "Integer32"
_ProvLinkAggrPortRole_Object = MibTableColumn
provLinkAggrPortRole = _ProvLinkAggrPortRole_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 2, 1, 4),
    _ProvLinkAggrPortRole_Type()
)
provLinkAggrPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provLinkAggrPortRole.setStatus("current")
_ProvLinkAggrPortExtTable_Object = MibTable
provLinkAggrPortExtTable = _ProvLinkAggrPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 3)
)
if mibBuilder.loadTexts:
    provLinkAggrPortExtTable.setStatus("current")
_ProvLinkAggrPortExtEntry_Object = MibTableRow
provLinkAggrPortExtEntry = _ProvLinkAggrPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 3, 1)
)
provLinkAggrPortExtEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "provLinkAggrPortExtGroupIfIndex"),
    (0, "IPE-LAG-MIB", "provLinkAggrPortExtIfIndex"),
)
if mibBuilder.loadTexts:
    provLinkAggrPortExtEntry.setStatus("current")
_ProvLinkAggrPortExtGroupIfIndex_Type = InterfaceIndex
_ProvLinkAggrPortExtGroupIfIndex_Object = MibTableColumn
provLinkAggrPortExtGroupIfIndex = _ProvLinkAggrPortExtGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 3, 1, 1),
    _ProvLinkAggrPortExtGroupIfIndex_Type()
)
provLinkAggrPortExtGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrPortExtGroupIfIndex.setStatus("current")
_ProvLinkAggrPortExtIfIndex_Type = InterfaceIndex
_ProvLinkAggrPortExtIfIndex_Object = MibTableColumn
provLinkAggrPortExtIfIndex = _ProvLinkAggrPortExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 3, 1, 2),
    _ProvLinkAggrPortExtIfIndex_Type()
)
provLinkAggrPortExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrPortExtIfIndex.setStatus("current")
_ProvLinkAggrPortExtNEAddress_Type = IpAddress
_ProvLinkAggrPortExtNEAddress_Object = MibTableColumn
provLinkAggrPortExtNEAddress = _ProvLinkAggrPortExtNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 3, 1, 3),
    _ProvLinkAggrPortExtNEAddress_Type()
)
provLinkAggrPortExtNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrPortExtNEAddress.setStatus("current")


class _ProvLinkAggrPortExtPriority_Type(Integer32):
    """Custom type provLinkAggrPortExtPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProvLinkAggrPortExtPriority_Type.__name__ = "Integer32"
_ProvLinkAggrPortExtPriority_Object = MibTableColumn
provLinkAggrPortExtPriority = _ProvLinkAggrPortExtPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 3, 1, 4),
    _ProvLinkAggrPortExtPriority_Type()
)
provLinkAggrPortExtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provLinkAggrPortExtPriority.setStatus("current")
_ProvLinkAggrEquipmentTable_Object = MibTable
provLinkAggrEquipmentTable = _ProvLinkAggrEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 4)
)
if mibBuilder.loadTexts:
    provLinkAggrEquipmentTable.setStatus("current")
_ProvLinkAggrEquipmentEntry_Object = MibTableRow
provLinkAggrEquipmentEntry = _ProvLinkAggrEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 4, 1)
)
provLinkAggrEquipmentEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "provLinkAggrEquipmentIndex"),
)
if mibBuilder.loadTexts:
    provLinkAggrEquipmentEntry.setStatus("current")


class _ProvLinkAggrEquipmentIndex_Type(Integer32):
    """Custom type provLinkAggrEquipmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ProvLinkAggrEquipmentIndex_Type.__name__ = "Integer32"
_ProvLinkAggrEquipmentIndex_Object = MibTableColumn
provLinkAggrEquipmentIndex = _ProvLinkAggrEquipmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 4, 1, 1),
    _ProvLinkAggrEquipmentIndex_Type()
)
provLinkAggrEquipmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrEquipmentIndex.setStatus("current")
_ProvLinkAggrEquipmentNEAddress_Type = IpAddress
_ProvLinkAggrEquipmentNEAddress_Object = MibTableColumn
provLinkAggrEquipmentNEAddress = _ProvLinkAggrEquipmentNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 4, 1, 2),
    _ProvLinkAggrEquipmentNEAddress_Type()
)
provLinkAggrEquipmentNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provLinkAggrEquipmentNEAddress.setStatus("current")


class _ProvLinkAggrEquipmentSysPriority_Type(Integer32):
    """Custom type provLinkAggrEquipmentSysPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProvLinkAggrEquipmentSysPriority_Type.__name__ = "Integer32"
_ProvLinkAggrEquipmentSysPriority_Object = MibTableColumn
provLinkAggrEquipmentSysPriority = _ProvLinkAggrEquipmentSysPriority_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 38, 4, 1, 3),
    _ProvLinkAggrEquipmentSysPriority_Type()
)
provLinkAggrEquipmentSysPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provLinkAggrEquipmentSysPriority.setStatus("current")
_MaintenanceGroup_ObjectIdentity = ObjectIdentity
maintenanceGroup = _MaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6)
)
_MaintLinkAggrGroup_ObjectIdentity = ObjectIdentity
maintLinkAggrGroup = _MaintLinkAggrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 38)
)
_MaintLinkAggrGroupTable_Object = MibTable
maintLinkAggrGroupTable = _MaintLinkAggrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 38, 1)
)
if mibBuilder.loadTexts:
    maintLinkAggrGroupTable.setStatus("current")
_MaintLinkAggrGroupEntry_Object = MibTableRow
maintLinkAggrGroupEntry = _MaintLinkAggrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 38, 1, 1)
)
maintLinkAggrGroupEntry.setIndexNames(
    (0, "IPE-LAG-MIB", "maintLinkAggrGroupIfIndex"),
)
if mibBuilder.loadTexts:
    maintLinkAggrGroupEntry.setStatus("current")
_MaintLinkAggrGroupIfIndex_Type = InterfaceIndex
_MaintLinkAggrGroupIfIndex_Object = MibTableColumn
maintLinkAggrGroupIfIndex = _MaintLinkAggrGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 38, 1, 1, 1),
    _MaintLinkAggrGroupIfIndex_Type()
)
maintLinkAggrGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintLinkAggrGroupIfIndex.setStatus("current")
_MaintLinkAggrGroupNEAddress_Type = IpAddress
_MaintLinkAggrGroupNEAddress_Object = MibTableColumn
maintLinkAggrGroupNEAddress = _MaintLinkAggrGroupNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 38, 1, 1, 2),
    _MaintLinkAggrGroupNEAddress_Type()
)
maintLinkAggrGroupNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintLinkAggrGroupNEAddress.setStatus("current")


class _MaintLinkAggrGroupRevert_Type(Integer32):
    """Custom type maintLinkAggrGroupRevert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("revert", 2))
    )


_MaintLinkAggrGroupRevert_Type.__name__ = "Integer32"
_MaintLinkAggrGroupRevert_Object = MibTableColumn
maintLinkAggrGroupRevert = _MaintLinkAggrGroupRevert_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 38, 1, 1, 3),
    _MaintLinkAggrGroupRevert_Type()
)
maintLinkAggrGroupRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintLinkAggrGroupRevert.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-LAG-MIB",
    **{"IpeEnableDisableValue": IpeEnableDisableValue,
       "SeverityValue": SeverityValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asLinkAggrGroup": asLinkAggrGroup,
       "asLinkAggrGroupTable": asLinkAggrGroupTable,
       "asLinkAggrGroupEntry": asLinkAggrGroupEntry,
       "asLinkAggrGroupIfIndex": asLinkAggrGroupIfIndex,
       "asLinkAggrGroupNEAddress": asLinkAggrGroupNEAddress,
       "asLinkAggrGroupLinkStatus": asLinkAggrGroupLinkStatus,
       "asLinkAggrGroupLLFStatus": asLinkAggrGroupLLFStatus,
       "asLinkAggrGroupOperStatus": asLinkAggrGroupOperStatus,
       "asLinkAggrPortTable": asLinkAggrPortTable,
       "asLinkAggrPortEntry": asLinkAggrPortEntry,
       "asLinkAggrPortGroupIfIndex": asLinkAggrPortGroupIfIndex,
       "asLinkAggrPortIfIndex": asLinkAggrPortIfIndex,
       "asLinkAggrPortNEAddress": asLinkAggrPortNEAddress,
       "asLinkAggrPortStatus": asLinkAggrPortStatus,
       "asLinkAggrPortActorLacpStatus": asLinkAggrPortActorLacpStatus,
       "asLinkAggrPortPartnerLacpStatus": asLinkAggrPortPartnerLacpStatus,
       "asLinkAggrPortLoopDetect": asLinkAggrPortLoopDetect,
       "asLinkAggrPortStatsTable": asLinkAggrPortStatsTable,
       "asLinkAggrPortStatsEntry": asLinkAggrPortStatsEntry,
       "asLinkAggrPortStatsIfIndex": asLinkAggrPortStatsIfIndex,
       "asLinkAggrPortStatsNEAddress": asLinkAggrPortStatsNEAddress,
       "asLinkAggrPortStatsLACPDUsRx": asLinkAggrPortStatsLACPDUsRx,
       "asLinkAggrPortStatsLACPDUsTx": asLinkAggrPortStatsLACPDUsTx,
       "asLinkAggrPortStatsMarkerPDUsRx": asLinkAggrPortStatsMarkerPDUsRx,
       "asLinkAggrPortStatsMarkerRespPDUsRx": asLinkAggrPortStatsMarkerRespPDUsRx,
       "asLinkAggrPortStatsMarkerPDUsTx": asLinkAggrPortStatsMarkerPDUsTx,
       "asLinkAggrPortStatsMarkerRespPDUsTx": asLinkAggrPortStatsMarkerRespPDUsTx,
       "provisioningGroup": provisioningGroup,
       "provLinkAggrGroup": provLinkAggrGroup,
       "provLinkAggrGroupTable": provLinkAggrGroupTable,
       "provLinkAggrGroupEntry": provLinkAggrGroupEntry,
       "provLinkAggrGroupIfIndex": provLinkAggrGroupIfIndex,
       "provLinkAggrGroupNEAddress": provLinkAggrGroupNEAddress,
       "provLinkAggrGroupMode": provLinkAggrGroupMode,
       "provLinkAggrGrLacpTxInterval": provLinkAggrGrLacpTxInterval,
       "provLinkAggrGroupRevertive": provLinkAggrGroupRevertive,
       "provLinkAggrGroupTxType": provLinkAggrGroupTxType,
       "provLinkAggrGroupName": provLinkAggrGroupName,
       "provLinkAggrGroupRowStatus": provLinkAggrGroupRowStatus,
       "provLinkAggrGroupMemberPort1": provLinkAggrGroupMemberPort1,
       "provLinkAggrGroupMemberPort2": provLinkAggrGroupMemberPort2,
       "provLinkAggrGroupMemberPort3": provLinkAggrGroupMemberPort3,
       "provLinkAggrGroupMemberPort4": provLinkAggrGroupMemberPort4,
       "provLinkAggrGroupMemberPort5": provLinkAggrGroupMemberPort5,
       "provLinkAggrGroupMemberPort6": provLinkAggrGroupMemberPort6,
       "provLinkAggrGroupMemberPort7": provLinkAggrGroupMemberPort7,
       "provLinkAggrGroupMemberPort8": provLinkAggrGroupMemberPort8,
       "provLinkAggrPortTable": provLinkAggrPortTable,
       "provLinkAggrPortEntry": provLinkAggrPortEntry,
       "provLinkAggrPortGroupIfIndex": provLinkAggrPortGroupIfIndex,
       "provLinkAggrPortIfIndex": provLinkAggrPortIfIndex,
       "provLinkAggrPortNEAddress": provLinkAggrPortNEAddress,
       "provLinkAggrPortRole": provLinkAggrPortRole,
       "provLinkAggrPortExtTable": provLinkAggrPortExtTable,
       "provLinkAggrPortExtEntry": provLinkAggrPortExtEntry,
       "provLinkAggrPortExtGroupIfIndex": provLinkAggrPortExtGroupIfIndex,
       "provLinkAggrPortExtIfIndex": provLinkAggrPortExtIfIndex,
       "provLinkAggrPortExtNEAddress": provLinkAggrPortExtNEAddress,
       "provLinkAggrPortExtPriority": provLinkAggrPortExtPriority,
       "provLinkAggrEquipmentTable": provLinkAggrEquipmentTable,
       "provLinkAggrEquipmentEntry": provLinkAggrEquipmentEntry,
       "provLinkAggrEquipmentIndex": provLinkAggrEquipmentIndex,
       "provLinkAggrEquipmentNEAddress": provLinkAggrEquipmentNEAddress,
       "provLinkAggrEquipmentSysPriority": provLinkAggrEquipmentSysPriority,
       "maintenanceGroup": maintenanceGroup,
       "maintLinkAggrGroup": maintLinkAggrGroup,
       "maintLinkAggrGroupTable": maintLinkAggrGroupTable,
       "maintLinkAggrGroupEntry": maintLinkAggrGroupEntry,
       "maintLinkAggrGroupIfIndex": maintLinkAggrGroupIfIndex,
       "maintLinkAggrGroupNEAddress": maintLinkAggrGroupNEAddress,
       "maintLinkAggrGroupRevert": maintLinkAggrGroupRevert}
)
