# SNMP MIB module (HPN-ICF-VSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-VSI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:04 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hpnicfVsi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105)
)
if mibBuilder.loadTexts:
    hpnicfVsi.setRevisions(
        ("2009-08-08 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVsiObjects_ObjectIdentity = ObjectIdentity
hpnicfVsiObjects = _HpnicfVsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1)
)
_HpnicfVsiScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfVsiScalarGroup = _HpnicfVsiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 1)
)
_HpnicfVsiNextAvailableVsiIndex_Type = Unsigned32
_HpnicfVsiNextAvailableVsiIndex_Object = MibScalar
hpnicfVsiNextAvailableVsiIndex = _HpnicfVsiNextAvailableVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 1, 1),
    _HpnicfVsiNextAvailableVsiIndex_Type()
)
hpnicfVsiNextAvailableVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiNextAvailableVsiIndex.setStatus("current")
_HpnicfVsiL2vpnStatus_Type = TruthValue
_HpnicfVsiL2vpnStatus_Object = MibScalar
hpnicfVsiL2vpnStatus = _HpnicfVsiL2vpnStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 1, 2),
    _HpnicfVsiL2vpnStatus_Type()
)
hpnicfVsiL2vpnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVsiL2vpnStatus.setStatus("current")
_HpnicfVsiTable_Object = MibTable
hpnicfVsiTable = _HpnicfVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfVsiTable.setStatus("current")
_HpnicfVsiEntry_Object = MibTableRow
hpnicfVsiEntry = _HpnicfVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1)
)
hpnicfVsiEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsiEntry.setStatus("current")
_HpnicfVsiIndex_Type = Unsigned32
_HpnicfVsiIndex_Object = MibTableColumn
hpnicfVsiIndex = _HpnicfVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 1),
    _HpnicfVsiIndex_Type()
)
hpnicfVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiIndex.setStatus("current")


class _HpnicfVsiName_Type(OctetString):
    """Custom type hpnicfVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfVsiName_Type.__name__ = "OctetString"
_HpnicfVsiName_Object = MibTableColumn
hpnicfVsiName = _HpnicfVsiName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 2),
    _HpnicfVsiName_Type()
)
hpnicfVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiName.setStatus("current")


class _HpnicfVsiMode_Type(Integer32):
    """Custom type hpnicfVsiMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("martini", 1),
          ("minm", 2),
          ("martiniAndMinm", 3),
          ("kompella", 4),
          ("kompellaAndMinm", 5),
          ("minmpxp", 6),
          ("martiniAndMinmpxp", 7),
          ("kompellaAndMinmpxp", 8))
    )


_HpnicfVsiMode_Type.__name__ = "Integer32"
_HpnicfVsiMode_Object = MibTableColumn
hpnicfVsiMode = _HpnicfVsiMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 3),
    _HpnicfVsiMode_Type()
)
hpnicfVsiMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiMode.setStatus("current")
_HpnicfMinmIsid_Type = Integer32
_HpnicfMinmIsid_Object = MibTableColumn
hpnicfMinmIsid = _HpnicfMinmIsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 4),
    _HpnicfMinmIsid_Type()
)
hpnicfMinmIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMinmIsid.setStatus("current")
_HpnicfVsiId_Type = Unsigned32
_HpnicfVsiId_Object = MibTableColumn
hpnicfVsiId = _HpnicfVsiId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 5),
    _HpnicfVsiId_Type()
)
hpnicfVsiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiId.setStatus("current")


class _HpnicfVsiTransMode_Type(Integer32):
    """Custom type hpnicfVsiTransMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_HpnicfVsiTransMode_Type.__name__ = "Integer32"
_HpnicfVsiTransMode_Object = MibTableColumn
hpnicfVsiTransMode = _HpnicfVsiTransMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 6),
    _HpnicfVsiTransMode_Type()
)
hpnicfVsiTransMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiTransMode.setStatus("current")


class _HpnicfVsiEnableHubSpoke_Type(Integer32):
    """Custom type hpnicfVsiEnableHubSpoke based on Integer32"""
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


_HpnicfVsiEnableHubSpoke_Type.__name__ = "Integer32"
_HpnicfVsiEnableHubSpoke_Object = MibTableColumn
hpnicfVsiEnableHubSpoke = _HpnicfVsiEnableHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 7),
    _HpnicfVsiEnableHubSpoke_Type()
)
hpnicfVsiEnableHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiEnableHubSpoke.setStatus("current")


class _HpnicfVsiAdminState_Type(Integer32):
    """Custom type hpnicfVsiAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminUp", 1),
          ("adminDown", 2))
    )


_HpnicfVsiAdminState_Type.__name__ = "Integer32"
_HpnicfVsiAdminState_Object = MibTableColumn
hpnicfVsiAdminState = _HpnicfVsiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 8),
    _HpnicfVsiAdminState_Type()
)
hpnicfVsiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiAdminState.setStatus("current")
_HpnicfVsiRowStatus_Type = RowStatus
_HpnicfVsiRowStatus_Object = MibTableColumn
hpnicfVsiRowStatus = _HpnicfVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 9),
    _HpnicfVsiRowStatus_Type()
)
hpnicfVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiRowStatus.setStatus("current")
_HpnicfVsiSpbIsid_Type = Integer32
_HpnicfVsiSpbIsid_Object = MibTableColumn
hpnicfVsiSpbIsid = _HpnicfVsiSpbIsid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 10),
    _HpnicfVsiSpbIsid_Type()
)
hpnicfVsiSpbIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiSpbIsid.setStatus("current")
_HpnicfVsiVxlanID_Type = Unsigned32
_HpnicfVsiVxlanID_Object = MibTableColumn
hpnicfVsiVxlanID = _HpnicfVsiVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 11),
    _HpnicfVsiVxlanID_Type()
)
hpnicfVsiVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiVxlanID.setStatus("current")


class _HpnicfVsiArpSuppression_Type(TruthValue):
    """Custom type hpnicfVsiArpSuppression based on TruthValue"""
    defaultValue = 2


_HpnicfVsiArpSuppression_Type.__name__ = "TruthValue"
_HpnicfVsiArpSuppression_Object = MibTableColumn
hpnicfVsiArpSuppression = _HpnicfVsiArpSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 12),
    _HpnicfVsiArpSuppression_Type()
)
hpnicfVsiArpSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiArpSuppression.setStatus("current")


class _HpnicfVsiFlooding_Type(TruthValue):
    """Custom type hpnicfVsiFlooding based on TruthValue"""
    defaultValue = 1


_HpnicfVsiFlooding_Type.__name__ = "TruthValue"
_HpnicfVsiFlooding_Object = MibTableColumn
hpnicfVsiFlooding = _HpnicfVsiFlooding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 13),
    _HpnicfVsiFlooding_Type()
)
hpnicfVsiFlooding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiFlooding.setStatus("current")
_HpnicfVsiLocalMacCount_Type = Unsigned32
_HpnicfVsiLocalMacCount_Object = MibTableColumn
hpnicfVsiLocalMacCount = _HpnicfVsiLocalMacCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 14),
    _HpnicfVsiLocalMacCount_Type()
)
hpnicfVsiLocalMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiLocalMacCount.setStatus("current")
_HpnicfVsiInterfaceID_Type = Unsigned32
_HpnicfVsiInterfaceID_Object = MibTableColumn
hpnicfVsiInterfaceID = _HpnicfVsiInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 15),
    _HpnicfVsiInterfaceID_Type()
)
hpnicfVsiInterfaceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiInterfaceID.setStatus("current")


class _HpnicfVsiStatistics_Type(TruthValue):
    """Custom type hpnicfVsiStatistics based on TruthValue"""
    defaultValue = 2


_HpnicfVsiStatistics_Type.__name__ = "TruthValue"
_HpnicfVsiStatistics_Object = MibTableColumn
hpnicfVsiStatistics = _HpnicfVsiStatistics_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 16),
    _HpnicfVsiStatistics_Type()
)
hpnicfVsiStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiStatistics.setStatus("current")
_HpnicfVsiNvgreID_Type = Unsigned32
_HpnicfVsiNvgreID_Object = MibTableColumn
hpnicfVsiNvgreID = _HpnicfVsiNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 2, 1, 17),
    _HpnicfVsiNvgreID_Type()
)
hpnicfVsiNvgreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiNvgreID.setStatus("current")
_HpnicfVsiXconnectTable_Object = MibTable
hpnicfVsiXconnectTable = _HpnicfVsiXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfVsiXconnectTable.setStatus("current")
_HpnicfVsiXconnectEntry_Object = MibTableRow
hpnicfVsiXconnectEntry = _HpnicfVsiXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1)
)
hpnicfVsiXconnectEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiXconnectIfIndex"),
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiXconnectEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    hpnicfVsiXconnectEntry.setStatus("current")
_HpnicfVsiXconnectIfIndex_Type = Unsigned32
_HpnicfVsiXconnectIfIndex_Object = MibTableColumn
hpnicfVsiXconnectIfIndex = _HpnicfVsiXconnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 1),
    _HpnicfVsiXconnectIfIndex_Type()
)
hpnicfVsiXconnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiXconnectIfIndex.setStatus("current")
_HpnicfVsiXconnectEvcSrvInstId_Type = Unsigned32
_HpnicfVsiXconnectEvcSrvInstId_Object = MibTableColumn
hpnicfVsiXconnectEvcSrvInstId = _HpnicfVsiXconnectEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 2),
    _HpnicfVsiXconnectEvcSrvInstId_Type()
)
hpnicfVsiXconnectEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiXconnectEvcSrvInstId.setStatus("current")


class _HpnicfVsiXconnectVsiName_Type(OctetString):
    """Custom type hpnicfVsiXconnectVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HpnicfVsiXconnectVsiName_Type.__name__ = "OctetString"
_HpnicfVsiXconnectVsiName_Object = MibTableColumn
hpnicfVsiXconnectVsiName = _HpnicfVsiXconnectVsiName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 3),
    _HpnicfVsiXconnectVsiName_Type()
)
hpnicfVsiXconnectVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiXconnectVsiName.setStatus("current")


class _HpnicfVsiXconnectAccessMode_Type(Integer32):
    """Custom type hpnicfVsiXconnectAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_HpnicfVsiXconnectAccessMode_Type.__name__ = "Integer32"
_HpnicfVsiXconnectAccessMode_Object = MibTableColumn
hpnicfVsiXconnectAccessMode = _HpnicfVsiXconnectAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 4),
    _HpnicfVsiXconnectAccessMode_Type()
)
hpnicfVsiXconnectAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiXconnectAccessMode.setStatus("current")


class _HpnicfVsiXconnectHubSpoke_Type(Integer32):
    """Custom type hpnicfVsiXconnectHubSpoke based on Integer32"""
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
          ("hub", 2),
          ("spoke", 3))
    )


_HpnicfVsiXconnectHubSpoke_Type.__name__ = "Integer32"
_HpnicfVsiXconnectHubSpoke_Object = MibTableColumn
hpnicfVsiXconnectHubSpoke = _HpnicfVsiXconnectHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 5),
    _HpnicfVsiXconnectHubSpoke_Type()
)
hpnicfVsiXconnectHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiXconnectHubSpoke.setStatus("current")
_HpnicfVsiXconnectRowStatus_Type = RowStatus
_HpnicfVsiXconnectRowStatus_Object = MibTableColumn
hpnicfVsiXconnectRowStatus = _HpnicfVsiXconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 3, 1, 6),
    _HpnicfVsiXconnectRowStatus_Type()
)
hpnicfVsiXconnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiXconnectRowStatus.setStatus("current")
_HpnicfVsiPwBindTable_Object = MibTable
hpnicfVsiPwBindTable = _HpnicfVsiPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfVsiPwBindTable.setStatus("current")
_HpnicfVsiPwBindEntry_Object = MibTableRow
hpnicfVsiPwBindEntry = _HpnicfVsiPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1)
)
hpnicfVsiPwBindEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiPwIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsiPwBindEntry.setStatus("current")
_HpnicfVsiPwIndex_Type = Unsigned32
_HpnicfVsiPwIndex_Object = MibTableColumn
hpnicfVsiPwIndex = _HpnicfVsiPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1, 1),
    _HpnicfVsiPwIndex_Type()
)
hpnicfVsiPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiPwIndex.setStatus("current")


class _HpnicfVsiPwBindAttributes_Type(Bits):
    """Custom type hpnicfVsiPwBindAttributes based on Bits"""
    namedValues = NamedValues(
        *(("noSplitHorizon", 0),
          ("hub", 1))
    )

_HpnicfVsiPwBindAttributes_Type.__name__ = "Bits"
_HpnicfVsiPwBindAttributes_Object = MibTableColumn
hpnicfVsiPwBindAttributes = _HpnicfVsiPwBindAttributes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1, 2),
    _HpnicfVsiPwBindAttributes_Type()
)
hpnicfVsiPwBindAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiPwBindAttributes.setStatus("current")
_HpnicfVsiPwBindRowStatus_Type = RowStatus
_HpnicfVsiPwBindRowStatus_Object = MibTableColumn
hpnicfVsiPwBindRowStatus = _HpnicfVsiPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 4, 1, 3),
    _HpnicfVsiPwBindRowStatus_Type()
)
hpnicfVsiPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiPwBindRowStatus.setStatus("current")
_HpnicfVsiFloodMacTable_Object = MibTable
hpnicfVsiFloodMacTable = _HpnicfVsiFloodMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfVsiFloodMacTable.setStatus("current")
_HpnicfVsiFloodMacEntry_Object = MibTableRow
hpnicfVsiFloodMacEntry = _HpnicfVsiFloodMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5, 1)
)
hpnicfVsiFloodMacEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiFloodMac"),
)
if mibBuilder.loadTexts:
    hpnicfVsiFloodMacEntry.setStatus("current")
_HpnicfVsiFloodMac_Type = MacAddress
_HpnicfVsiFloodMac_Object = MibTableColumn
hpnicfVsiFloodMac = _HpnicfVsiFloodMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5, 1, 1),
    _HpnicfVsiFloodMac_Type()
)
hpnicfVsiFloodMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiFloodMac.setStatus("current")
_HpnicfVsiFloodMacRowStatus_Type = RowStatus
_HpnicfVsiFloodMacRowStatus_Object = MibTableColumn
hpnicfVsiFloodMacRowStatus = _HpnicfVsiFloodMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 5, 1, 2),
    _HpnicfVsiFloodMacRowStatus_Type()
)
hpnicfVsiFloodMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiFloodMacRowStatus.setStatus("current")
_HpnicfVsiLocalMacTable_Object = MibTable
hpnicfVsiLocalMacTable = _HpnicfVsiLocalMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6)
)
if mibBuilder.loadTexts:
    hpnicfVsiLocalMacTable.setStatus("current")
_HpnicfVsiLocalMacEntry_Object = MibTableRow
hpnicfVsiLocalMacEntry = _HpnicfVsiLocalMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1)
)
hpnicfVsiLocalMacEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiLocalMacAddr"),
)
if mibBuilder.loadTexts:
    hpnicfVsiLocalMacEntry.setStatus("current")
_HpnicfVsiLocalMacAddr_Type = MacAddress
_HpnicfVsiLocalMacAddr_Object = MibTableColumn
hpnicfVsiLocalMacAddr = _HpnicfVsiLocalMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1, 1),
    _HpnicfVsiLocalMacAddr_Type()
)
hpnicfVsiLocalMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiLocalMacAddr.setStatus("current")
_HpnicfVsiLocalMacIfIndex_Type = InterfaceIndex
_HpnicfVsiLocalMacIfIndex_Object = MibTableColumn
hpnicfVsiLocalMacIfIndex = _HpnicfVsiLocalMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1, 2),
    _HpnicfVsiLocalMacIfIndex_Type()
)
hpnicfVsiLocalMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiLocalMacIfIndex.setStatus("current")
_HpnicfVsiLocalMacSrvID_Type = Unsigned32
_HpnicfVsiLocalMacSrvID_Object = MibTableColumn
hpnicfVsiLocalMacSrvID = _HpnicfVsiLocalMacSrvID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 6, 1, 3),
    _HpnicfVsiLocalMacSrvID_Type()
)
hpnicfVsiLocalMacSrvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiLocalMacSrvID.setStatus("current")
_HpnicfVsiPerfTable_Object = MibTable
hpnicfVsiPerfTable = _HpnicfVsiPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7)
)
if mibBuilder.loadTexts:
    hpnicfVsiPerfTable.setStatus("current")
_HpnicfVsiPerfEntry_Object = MibTableRow
hpnicfVsiPerfEntry = _HpnicfVsiPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1)
)
hpnicfVsiPerfEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVsiPerfEntry.setStatus("current")
_HpnicfVsiPerfInOctets_Type = Counter64
_HpnicfVsiPerfInOctets_Object = MibTableColumn
hpnicfVsiPerfInOctets = _HpnicfVsiPerfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 1),
    _HpnicfVsiPerfInOctets_Type()
)
hpnicfVsiPerfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfInOctets.setStatus("current")
_HpnicfVsiPerfInPackets_Type = Counter64
_HpnicfVsiPerfInPackets_Object = MibTableColumn
hpnicfVsiPerfInPackets = _HpnicfVsiPerfInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 2),
    _HpnicfVsiPerfInPackets_Type()
)
hpnicfVsiPerfInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfInPackets.setStatus("current")
_HpnicfVsiPerfInErrors_Type = Counter64
_HpnicfVsiPerfInErrors_Object = MibTableColumn
hpnicfVsiPerfInErrors = _HpnicfVsiPerfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 3),
    _HpnicfVsiPerfInErrors_Type()
)
hpnicfVsiPerfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfInErrors.setStatus("current")
_HpnicfVsiPerfInDiscards_Type = Counter64
_HpnicfVsiPerfInDiscards_Object = MibTableColumn
hpnicfVsiPerfInDiscards = _HpnicfVsiPerfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 4),
    _HpnicfVsiPerfInDiscards_Type()
)
hpnicfVsiPerfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfInDiscards.setStatus("current")
_HpnicfVsiPerfOutOctets_Type = Counter64
_HpnicfVsiPerfOutOctets_Object = MibTableColumn
hpnicfVsiPerfOutOctets = _HpnicfVsiPerfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 5),
    _HpnicfVsiPerfOutOctets_Type()
)
hpnicfVsiPerfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfOutOctets.setStatus("current")
_HpnicfVsiPerfOutPackets_Type = Counter64
_HpnicfVsiPerfOutPackets_Object = MibTableColumn
hpnicfVsiPerfOutPackets = _HpnicfVsiPerfOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 6),
    _HpnicfVsiPerfOutPackets_Type()
)
hpnicfVsiPerfOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfOutPackets.setStatus("current")
_HpnicfVsiPerfOutErrors_Type = Counter64
_HpnicfVsiPerfOutErrors_Object = MibTableColumn
hpnicfVsiPerfOutErrors = _HpnicfVsiPerfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 7),
    _HpnicfVsiPerfOutErrors_Type()
)
hpnicfVsiPerfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfOutErrors.setStatus("current")
_HpnicfVsiPerfOutDiscards_Type = Counter64
_HpnicfVsiPerfOutDiscards_Object = MibTableColumn
hpnicfVsiPerfOutDiscards = _HpnicfVsiPerfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 7, 1, 8),
    _HpnicfVsiPerfOutDiscards_Type()
)
hpnicfVsiPerfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiPerfOutDiscards.setStatus("current")
_HpnicfVsiNextAvailableVsiIfID_Type = Unsigned32
_HpnicfVsiNextAvailableVsiIfID_Object = MibScalar
hpnicfVsiNextAvailableVsiIfID = _HpnicfVsiNextAvailableVsiIfID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 8),
    _HpnicfVsiNextAvailableVsiIfID_Type()
)
hpnicfVsiNextAvailableVsiIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiNextAvailableVsiIfID.setStatus("current")
_HpnicfVsiIfTable_Object = MibTable
hpnicfVsiIfTable = _HpnicfVsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 9)
)
if mibBuilder.loadTexts:
    hpnicfVsiIfTable.setStatus("current")
_HpnicfVsiIfEntry_Object = MibTableRow
hpnicfVsiIfEntry = _HpnicfVsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 9, 1)
)
hpnicfVsiIfEntry.setIndexNames(
    (0, "HPN-ICF-VSI-MIB", "hpnicfVsiIfID"),
)
if mibBuilder.loadTexts:
    hpnicfVsiIfEntry.setStatus("current")
_HpnicfVsiIfID_Type = Unsigned32
_HpnicfVsiIfID_Object = MibTableColumn
hpnicfVsiIfID = _HpnicfVsiIfID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 9, 1, 1),
    _HpnicfVsiIfID_Type()
)
hpnicfVsiIfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfVsiIfID.setStatus("current")
_HpnicfVsiIfIndex_Type = InterfaceIndex
_HpnicfVsiIfIndex_Object = MibTableColumn
hpnicfVsiIfIndex = _HpnicfVsiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 9, 1, 2),
    _HpnicfVsiIfIndex_Type()
)
hpnicfVsiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVsiIfIndex.setStatus("current")
_HpnicfVsiIfRowStatus_Type = RowStatus
_HpnicfVsiIfRowStatus_Object = MibTableColumn
hpnicfVsiIfRowStatus = _HpnicfVsiIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 105, 1, 9, 1, 3),
    _HpnicfVsiIfRowStatus_Type()
)
hpnicfVsiIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfVsiIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VSI-MIB",
    **{"hpnicfVsi": hpnicfVsi,
       "hpnicfVsiObjects": hpnicfVsiObjects,
       "hpnicfVsiScalarGroup": hpnicfVsiScalarGroup,
       "hpnicfVsiNextAvailableVsiIndex": hpnicfVsiNextAvailableVsiIndex,
       "hpnicfVsiL2vpnStatus": hpnicfVsiL2vpnStatus,
       "hpnicfVsiTable": hpnicfVsiTable,
       "hpnicfVsiEntry": hpnicfVsiEntry,
       "hpnicfVsiIndex": hpnicfVsiIndex,
       "hpnicfVsiName": hpnicfVsiName,
       "hpnicfVsiMode": hpnicfVsiMode,
       "hpnicfMinmIsid": hpnicfMinmIsid,
       "hpnicfVsiId": hpnicfVsiId,
       "hpnicfVsiTransMode": hpnicfVsiTransMode,
       "hpnicfVsiEnableHubSpoke": hpnicfVsiEnableHubSpoke,
       "hpnicfVsiAdminState": hpnicfVsiAdminState,
       "hpnicfVsiRowStatus": hpnicfVsiRowStatus,
       "hpnicfVsiSpbIsid": hpnicfVsiSpbIsid,
       "hpnicfVsiVxlanID": hpnicfVsiVxlanID,
       "hpnicfVsiArpSuppression": hpnicfVsiArpSuppression,
       "hpnicfVsiFlooding": hpnicfVsiFlooding,
       "hpnicfVsiLocalMacCount": hpnicfVsiLocalMacCount,
       "hpnicfVsiInterfaceID": hpnicfVsiInterfaceID,
       "hpnicfVsiStatistics": hpnicfVsiStatistics,
       "hpnicfVsiNvgreID": hpnicfVsiNvgreID,
       "hpnicfVsiXconnectTable": hpnicfVsiXconnectTable,
       "hpnicfVsiXconnectEntry": hpnicfVsiXconnectEntry,
       "hpnicfVsiXconnectIfIndex": hpnicfVsiXconnectIfIndex,
       "hpnicfVsiXconnectEvcSrvInstId": hpnicfVsiXconnectEvcSrvInstId,
       "hpnicfVsiXconnectVsiName": hpnicfVsiXconnectVsiName,
       "hpnicfVsiXconnectAccessMode": hpnicfVsiXconnectAccessMode,
       "hpnicfVsiXconnectHubSpoke": hpnicfVsiXconnectHubSpoke,
       "hpnicfVsiXconnectRowStatus": hpnicfVsiXconnectRowStatus,
       "hpnicfVsiPwBindTable": hpnicfVsiPwBindTable,
       "hpnicfVsiPwBindEntry": hpnicfVsiPwBindEntry,
       "hpnicfVsiPwIndex": hpnicfVsiPwIndex,
       "hpnicfVsiPwBindAttributes": hpnicfVsiPwBindAttributes,
       "hpnicfVsiPwBindRowStatus": hpnicfVsiPwBindRowStatus,
       "hpnicfVsiFloodMacTable": hpnicfVsiFloodMacTable,
       "hpnicfVsiFloodMacEntry": hpnicfVsiFloodMacEntry,
       "hpnicfVsiFloodMac": hpnicfVsiFloodMac,
       "hpnicfVsiFloodMacRowStatus": hpnicfVsiFloodMacRowStatus,
       "hpnicfVsiLocalMacTable": hpnicfVsiLocalMacTable,
       "hpnicfVsiLocalMacEntry": hpnicfVsiLocalMacEntry,
       "hpnicfVsiLocalMacAddr": hpnicfVsiLocalMacAddr,
       "hpnicfVsiLocalMacIfIndex": hpnicfVsiLocalMacIfIndex,
       "hpnicfVsiLocalMacSrvID": hpnicfVsiLocalMacSrvID,
       "hpnicfVsiPerfTable": hpnicfVsiPerfTable,
       "hpnicfVsiPerfEntry": hpnicfVsiPerfEntry,
       "hpnicfVsiPerfInOctets": hpnicfVsiPerfInOctets,
       "hpnicfVsiPerfInPackets": hpnicfVsiPerfInPackets,
       "hpnicfVsiPerfInErrors": hpnicfVsiPerfInErrors,
       "hpnicfVsiPerfInDiscards": hpnicfVsiPerfInDiscards,
       "hpnicfVsiPerfOutOctets": hpnicfVsiPerfOutOctets,
       "hpnicfVsiPerfOutPackets": hpnicfVsiPerfOutPackets,
       "hpnicfVsiPerfOutErrors": hpnicfVsiPerfOutErrors,
       "hpnicfVsiPerfOutDiscards": hpnicfVsiPerfOutDiscards,
       "hpnicfVsiNextAvailableVsiIfID": hpnicfVsiNextAvailableVsiIfID,
       "hpnicfVsiIfTable": hpnicfVsiIfTable,
       "hpnicfVsiIfEntry": hpnicfVsiIfEntry,
       "hpnicfVsiIfID": hpnicfVsiIfID,
       "hpnicfVsiIfIndex": hpnicfVsiIfIndex,
       "hpnicfVsiIfRowStatus": hpnicfVsiIfRowStatus}
)
