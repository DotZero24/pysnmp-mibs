# SNMP MIB module (H3C-VSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-VSI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:24 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cVsi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105)
)
if mibBuilder.loadTexts:
    h3cVsi.setRevisions(
        ("2016-10-29 16:50",
         "2015-05-26 15:55",
         "2009-08-08 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVsiObjects_ObjectIdentity = ObjectIdentity
h3cVsiObjects = _H3cVsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1)
)
_H3cVsiScalarGroup_ObjectIdentity = ObjectIdentity
h3cVsiScalarGroup = _H3cVsiScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 1)
)
_H3cVsiNextAvailableVsiIndex_Type = Unsigned32
_H3cVsiNextAvailableVsiIndex_Object = MibScalar
h3cVsiNextAvailableVsiIndex = _H3cVsiNextAvailableVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 1, 1),
    _H3cVsiNextAvailableVsiIndex_Type()
)
h3cVsiNextAvailableVsiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiNextAvailableVsiIndex.setStatus("current")
_H3cVsiL2vpnStatus_Type = TruthValue
_H3cVsiL2vpnStatus_Object = MibScalar
h3cVsiL2vpnStatus = _H3cVsiL2vpnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 1, 2),
    _H3cVsiL2vpnStatus_Type()
)
h3cVsiL2vpnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVsiL2vpnStatus.setStatus("current")
_H3cVsiTable_Object = MibTable
h3cVsiTable = _H3cVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2)
)
if mibBuilder.loadTexts:
    h3cVsiTable.setStatus("current")
_H3cVsiEntry_Object = MibTableRow
h3cVsiEntry = _H3cVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1)
)
h3cVsiEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIndex"),
)
if mibBuilder.loadTexts:
    h3cVsiEntry.setStatus("current")
_H3cVsiIndex_Type = Unsigned32
_H3cVsiIndex_Object = MibTableColumn
h3cVsiIndex = _H3cVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 1),
    _H3cVsiIndex_Type()
)
h3cVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiIndex.setStatus("current")


class _H3cVsiName_Type(OctetString):
    """Custom type h3cVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cVsiName_Type.__name__ = "OctetString"
_H3cVsiName_Object = MibTableColumn
h3cVsiName = _H3cVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 2),
    _H3cVsiName_Type()
)
h3cVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiName.setStatus("current")


class _H3cVsiMode_Type(Integer32):
    """Custom type h3cVsiMode based on Integer32"""
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
              9)
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
          ("kompellaAndMinmpxp", 8),
          ("vxlan", 9))
    )


_H3cVsiMode_Type.__name__ = "Integer32"
_H3cVsiMode_Object = MibTableColumn
h3cVsiMode = _H3cVsiMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 3),
    _H3cVsiMode_Type()
)
h3cVsiMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiMode.setStatus("current")
_H3cMinmIsid_Type = Integer32
_H3cMinmIsid_Object = MibTableColumn
h3cMinmIsid = _H3cMinmIsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 4),
    _H3cMinmIsid_Type()
)
h3cMinmIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMinmIsid.setStatus("current")
_H3cVsiId_Type = Unsigned32
_H3cVsiId_Object = MibTableColumn
h3cVsiId = _H3cVsiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 5),
    _H3cVsiId_Type()
)
h3cVsiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiId.setStatus("current")


class _H3cVsiTransMode_Type(Integer32):
    """Custom type h3cVsiTransMode based on Integer32"""
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


_H3cVsiTransMode_Type.__name__ = "Integer32"
_H3cVsiTransMode_Object = MibTableColumn
h3cVsiTransMode = _H3cVsiTransMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 6),
    _H3cVsiTransMode_Type()
)
h3cVsiTransMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiTransMode.setStatus("current")


class _H3cVsiEnableHubSpoke_Type(Integer32):
    """Custom type h3cVsiEnableHubSpoke based on Integer32"""
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


_H3cVsiEnableHubSpoke_Type.__name__ = "Integer32"
_H3cVsiEnableHubSpoke_Object = MibTableColumn
h3cVsiEnableHubSpoke = _H3cVsiEnableHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 7),
    _H3cVsiEnableHubSpoke_Type()
)
h3cVsiEnableHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiEnableHubSpoke.setStatus("current")


class _H3cVsiAdminState_Type(Integer32):
    """Custom type h3cVsiAdminState based on Integer32"""
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


_H3cVsiAdminState_Type.__name__ = "Integer32"
_H3cVsiAdminState_Object = MibTableColumn
h3cVsiAdminState = _H3cVsiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 8),
    _H3cVsiAdminState_Type()
)
h3cVsiAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiAdminState.setStatus("current")
_H3cVsiRowStatus_Type = RowStatus
_H3cVsiRowStatus_Object = MibTableColumn
h3cVsiRowStatus = _H3cVsiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 9),
    _H3cVsiRowStatus_Type()
)
h3cVsiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiRowStatus.setStatus("current")
_H3cVsiSpbIsid_Type = Integer32
_H3cVsiSpbIsid_Object = MibTableColumn
h3cVsiSpbIsid = _H3cVsiSpbIsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 10),
    _H3cVsiSpbIsid_Type()
)
h3cVsiSpbIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiSpbIsid.setStatus("current")
_H3cVsiVxlanID_Type = Unsigned32
_H3cVsiVxlanID_Object = MibTableColumn
h3cVsiVxlanID = _H3cVsiVxlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 11),
    _H3cVsiVxlanID_Type()
)
h3cVsiVxlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiVxlanID.setStatus("current")


class _H3cVsiArpSuppression_Type(TruthValue):
    """Custom type h3cVsiArpSuppression based on TruthValue"""
    defaultValue = 2


_H3cVsiArpSuppression_Type.__name__ = "TruthValue"
_H3cVsiArpSuppression_Object = MibTableColumn
h3cVsiArpSuppression = _H3cVsiArpSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 12),
    _H3cVsiArpSuppression_Type()
)
h3cVsiArpSuppression.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiArpSuppression.setStatus("current")


class _H3cVsiFlooding_Type(TruthValue):
    """Custom type h3cVsiFlooding based on TruthValue"""
    defaultValue = 1


_H3cVsiFlooding_Type.__name__ = "TruthValue"
_H3cVsiFlooding_Object = MibTableColumn
h3cVsiFlooding = _H3cVsiFlooding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 13),
    _H3cVsiFlooding_Type()
)
h3cVsiFlooding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiFlooding.setStatus("current")
_H3cVsiLocalMacCount_Type = Unsigned32
_H3cVsiLocalMacCount_Object = MibTableColumn
h3cVsiLocalMacCount = _H3cVsiLocalMacCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 14),
    _H3cVsiLocalMacCount_Type()
)
h3cVsiLocalMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiLocalMacCount.setStatus("current")
_H3cVsiInterfaceID_Type = Unsigned32
_H3cVsiInterfaceID_Object = MibTableColumn
h3cVsiInterfaceID = _H3cVsiInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 15),
    _H3cVsiInterfaceID_Type()
)
h3cVsiInterfaceID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiInterfaceID.setStatus("current")


class _H3cVsiStatistics_Type(TruthValue):
    """Custom type h3cVsiStatistics based on TruthValue"""
    defaultValue = 2


_H3cVsiStatistics_Type.__name__ = "TruthValue"
_H3cVsiStatistics_Object = MibTableColumn
h3cVsiStatistics = _H3cVsiStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 16),
    _H3cVsiStatistics_Type()
)
h3cVsiStatistics.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiStatistics.setStatus("current")
_H3cVsiNvgreID_Type = Unsigned32
_H3cVsiNvgreID_Object = MibTableColumn
h3cVsiNvgreID = _H3cVsiNvgreID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 2, 1, 17),
    _H3cVsiNvgreID_Type()
)
h3cVsiNvgreID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiNvgreID.setStatus("current")
_H3cVsiXconnectTable_Object = MibTable
h3cVsiXconnectTable = _H3cVsiXconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3)
)
if mibBuilder.loadTexts:
    h3cVsiXconnectTable.setStatus("current")
_H3cVsiXconnectEntry_Object = MibTableRow
h3cVsiXconnectEntry = _H3cVsiXconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1)
)
h3cVsiXconnectEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiXconnectIfIndex"),
    (0, "H3C-VSI-MIB", "h3cVsiXconnectEvcSrvInstId"),
)
if mibBuilder.loadTexts:
    h3cVsiXconnectEntry.setStatus("current")
_H3cVsiXconnectIfIndex_Type = Unsigned32
_H3cVsiXconnectIfIndex_Object = MibTableColumn
h3cVsiXconnectIfIndex = _H3cVsiXconnectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 1),
    _H3cVsiXconnectIfIndex_Type()
)
h3cVsiXconnectIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiXconnectIfIndex.setStatus("current")
_H3cVsiXconnectEvcSrvInstId_Type = Unsigned32
_H3cVsiXconnectEvcSrvInstId_Object = MibTableColumn
h3cVsiXconnectEvcSrvInstId = _H3cVsiXconnectEvcSrvInstId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 2),
    _H3cVsiXconnectEvcSrvInstId_Type()
)
h3cVsiXconnectEvcSrvInstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiXconnectEvcSrvInstId.setStatus("current")


class _H3cVsiXconnectVsiName_Type(OctetString):
    """Custom type h3cVsiXconnectVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_H3cVsiXconnectVsiName_Type.__name__ = "OctetString"
_H3cVsiXconnectVsiName_Object = MibTableColumn
h3cVsiXconnectVsiName = _H3cVsiXconnectVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 3),
    _H3cVsiXconnectVsiName_Type()
)
h3cVsiXconnectVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectVsiName.setStatus("current")


class _H3cVsiXconnectAccessMode_Type(Integer32):
    """Custom type h3cVsiXconnectAccessMode based on Integer32"""
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


_H3cVsiXconnectAccessMode_Type.__name__ = "Integer32"
_H3cVsiXconnectAccessMode_Object = MibTableColumn
h3cVsiXconnectAccessMode = _H3cVsiXconnectAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 4),
    _H3cVsiXconnectAccessMode_Type()
)
h3cVsiXconnectAccessMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectAccessMode.setStatus("current")


class _H3cVsiXconnectHubSpoke_Type(Integer32):
    """Custom type h3cVsiXconnectHubSpoke based on Integer32"""
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


_H3cVsiXconnectHubSpoke_Type.__name__ = "Integer32"
_H3cVsiXconnectHubSpoke_Object = MibTableColumn
h3cVsiXconnectHubSpoke = _H3cVsiXconnectHubSpoke_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 5),
    _H3cVsiXconnectHubSpoke_Type()
)
h3cVsiXconnectHubSpoke.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectHubSpoke.setStatus("current")
_H3cVsiXconnectRowStatus_Type = RowStatus
_H3cVsiXconnectRowStatus_Object = MibTableColumn
h3cVsiXconnectRowStatus = _H3cVsiXconnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 3, 1, 6),
    _H3cVsiXconnectRowStatus_Type()
)
h3cVsiXconnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiXconnectRowStatus.setStatus("current")
_H3cVsiPwBindTable_Object = MibTable
h3cVsiPwBindTable = _H3cVsiPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 4)
)
if mibBuilder.loadTexts:
    h3cVsiPwBindTable.setStatus("current")
_H3cVsiPwBindEntry_Object = MibTableRow
h3cVsiPwBindEntry = _H3cVsiPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 4, 1)
)
h3cVsiPwBindEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIndex"),
    (0, "H3C-VSI-MIB", "h3cVsiPwIndex"),
)
if mibBuilder.loadTexts:
    h3cVsiPwBindEntry.setStatus("current")
_H3cVsiPwIndex_Type = Unsigned32
_H3cVsiPwIndex_Object = MibTableColumn
h3cVsiPwIndex = _H3cVsiPwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 4, 1, 1),
    _H3cVsiPwIndex_Type()
)
h3cVsiPwIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiPwIndex.setStatus("current")


class _H3cVsiPwBindAttributes_Type(Bits):
    """Custom type h3cVsiPwBindAttributes based on Bits"""
    namedValues = NamedValues(
        *(("noSplitHorizon", 0),
          ("hub", 1))
    )

_H3cVsiPwBindAttributes_Type.__name__ = "Bits"
_H3cVsiPwBindAttributes_Object = MibTableColumn
h3cVsiPwBindAttributes = _H3cVsiPwBindAttributes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 4, 1, 2),
    _H3cVsiPwBindAttributes_Type()
)
h3cVsiPwBindAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiPwBindAttributes.setStatus("current")
_H3cVsiPwBindRowStatus_Type = RowStatus
_H3cVsiPwBindRowStatus_Object = MibTableColumn
h3cVsiPwBindRowStatus = _H3cVsiPwBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 4, 1, 3),
    _H3cVsiPwBindRowStatus_Type()
)
h3cVsiPwBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiPwBindRowStatus.setStatus("current")
_H3cVsiFloodMacTable_Object = MibTable
h3cVsiFloodMacTable = _H3cVsiFloodMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 5)
)
if mibBuilder.loadTexts:
    h3cVsiFloodMacTable.setStatus("current")
_H3cVsiFloodMacEntry_Object = MibTableRow
h3cVsiFloodMacEntry = _H3cVsiFloodMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 5, 1)
)
h3cVsiFloodMacEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIndex"),
    (0, "H3C-VSI-MIB", "h3cVsiFloodMac"),
)
if mibBuilder.loadTexts:
    h3cVsiFloodMacEntry.setStatus("current")
_H3cVsiFloodMac_Type = MacAddress
_H3cVsiFloodMac_Object = MibTableColumn
h3cVsiFloodMac = _H3cVsiFloodMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 5, 1, 1),
    _H3cVsiFloodMac_Type()
)
h3cVsiFloodMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiFloodMac.setStatus("current")
_H3cVsiFloodMacRowStatus_Type = RowStatus
_H3cVsiFloodMacRowStatus_Object = MibTableColumn
h3cVsiFloodMacRowStatus = _H3cVsiFloodMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 5, 1, 2),
    _H3cVsiFloodMacRowStatus_Type()
)
h3cVsiFloodMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiFloodMacRowStatus.setStatus("current")
_H3cVsiLocalMacTable_Object = MibTable
h3cVsiLocalMacTable = _H3cVsiLocalMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 6)
)
if mibBuilder.loadTexts:
    h3cVsiLocalMacTable.setStatus("current")
_H3cVsiLocalMacEntry_Object = MibTableRow
h3cVsiLocalMacEntry = _H3cVsiLocalMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 6, 1)
)
h3cVsiLocalMacEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIndex"),
    (0, "H3C-VSI-MIB", "h3cVsiLocalMacAddr"),
)
if mibBuilder.loadTexts:
    h3cVsiLocalMacEntry.setStatus("current")
_H3cVsiLocalMacAddr_Type = MacAddress
_H3cVsiLocalMacAddr_Object = MibTableColumn
h3cVsiLocalMacAddr = _H3cVsiLocalMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 6, 1, 1),
    _H3cVsiLocalMacAddr_Type()
)
h3cVsiLocalMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiLocalMacAddr.setStatus("current")
_H3cVsiLocalMacIfIndex_Type = InterfaceIndex
_H3cVsiLocalMacIfIndex_Object = MibTableColumn
h3cVsiLocalMacIfIndex = _H3cVsiLocalMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 6, 1, 2),
    _H3cVsiLocalMacIfIndex_Type()
)
h3cVsiLocalMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiLocalMacIfIndex.setStatus("current")
_H3cVsiLocalMacSrvID_Type = Unsigned32
_H3cVsiLocalMacSrvID_Object = MibTableColumn
h3cVsiLocalMacSrvID = _H3cVsiLocalMacSrvID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 6, 1, 3),
    _H3cVsiLocalMacSrvID_Type()
)
h3cVsiLocalMacSrvID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiLocalMacSrvID.setStatus("current")
_H3cVsiPerfTable_Object = MibTable
h3cVsiPerfTable = _H3cVsiPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7)
)
if mibBuilder.loadTexts:
    h3cVsiPerfTable.setStatus("current")
_H3cVsiPerfEntry_Object = MibTableRow
h3cVsiPerfEntry = _H3cVsiPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1)
)
h3cVsiPerfEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIndex"),
)
if mibBuilder.loadTexts:
    h3cVsiPerfEntry.setStatus("current")
_H3cVsiPerfInOctets_Type = Counter64
_H3cVsiPerfInOctets_Object = MibTableColumn
h3cVsiPerfInOctets = _H3cVsiPerfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 1),
    _H3cVsiPerfInOctets_Type()
)
h3cVsiPerfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfInOctets.setStatus("current")
_H3cVsiPerfInPackets_Type = Counter64
_H3cVsiPerfInPackets_Object = MibTableColumn
h3cVsiPerfInPackets = _H3cVsiPerfInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 2),
    _H3cVsiPerfInPackets_Type()
)
h3cVsiPerfInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfInPackets.setStatus("current")
_H3cVsiPerfInErrors_Type = Counter64
_H3cVsiPerfInErrors_Object = MibTableColumn
h3cVsiPerfInErrors = _H3cVsiPerfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 3),
    _H3cVsiPerfInErrors_Type()
)
h3cVsiPerfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfInErrors.setStatus("current")
_H3cVsiPerfInDiscards_Type = Counter64
_H3cVsiPerfInDiscards_Object = MibTableColumn
h3cVsiPerfInDiscards = _H3cVsiPerfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 4),
    _H3cVsiPerfInDiscards_Type()
)
h3cVsiPerfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfInDiscards.setStatus("current")
_H3cVsiPerfOutOctets_Type = Counter64
_H3cVsiPerfOutOctets_Object = MibTableColumn
h3cVsiPerfOutOctets = _H3cVsiPerfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 5),
    _H3cVsiPerfOutOctets_Type()
)
h3cVsiPerfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfOutOctets.setStatus("current")
_H3cVsiPerfOutPackets_Type = Counter64
_H3cVsiPerfOutPackets_Object = MibTableColumn
h3cVsiPerfOutPackets = _H3cVsiPerfOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 6),
    _H3cVsiPerfOutPackets_Type()
)
h3cVsiPerfOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfOutPackets.setStatus("current")
_H3cVsiPerfOutErrors_Type = Counter64
_H3cVsiPerfOutErrors_Object = MibTableColumn
h3cVsiPerfOutErrors = _H3cVsiPerfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 7),
    _H3cVsiPerfOutErrors_Type()
)
h3cVsiPerfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfOutErrors.setStatus("current")
_H3cVsiPerfOutDiscards_Type = Counter64
_H3cVsiPerfOutDiscards_Object = MibTableColumn
h3cVsiPerfOutDiscards = _H3cVsiPerfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 7, 1, 8),
    _H3cVsiPerfOutDiscards_Type()
)
h3cVsiPerfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiPerfOutDiscards.setStatus("current")
_H3cVsiNextAvailableVsiIfID_Type = Unsigned32
_H3cVsiNextAvailableVsiIfID_Object = MibScalar
h3cVsiNextAvailableVsiIfID = _H3cVsiNextAvailableVsiIfID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 8),
    _H3cVsiNextAvailableVsiIfID_Type()
)
h3cVsiNextAvailableVsiIfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiNextAvailableVsiIfID.setStatus("current")
_H3cVsiIfTable_Object = MibTable
h3cVsiIfTable = _H3cVsiIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 9)
)
if mibBuilder.loadTexts:
    h3cVsiIfTable.setStatus("current")
_H3cVsiIfEntry_Object = MibTableRow
h3cVsiIfEntry = _H3cVsiIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 9, 1)
)
h3cVsiIfEntry.setIndexNames(
    (0, "H3C-VSI-MIB", "h3cVsiIfID"),
)
if mibBuilder.loadTexts:
    h3cVsiIfEntry.setStatus("current")
_H3cVsiIfID_Type = Unsigned32
_H3cVsiIfID_Object = MibTableColumn
h3cVsiIfID = _H3cVsiIfID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 9, 1, 1),
    _H3cVsiIfID_Type()
)
h3cVsiIfID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVsiIfID.setStatus("current")
_H3cVsiIfIndex_Type = InterfaceIndex
_H3cVsiIfIndex_Object = MibTableColumn
h3cVsiIfIndex = _H3cVsiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 9, 1, 2),
    _H3cVsiIfIndex_Type()
)
h3cVsiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVsiIfIndex.setStatus("current")
_H3cVsiIfRowStatus_Type = RowStatus
_H3cVsiIfRowStatus_Object = MibTableColumn
h3cVsiIfRowStatus = _H3cVsiIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 105, 1, 9, 1, 3),
    _H3cVsiIfRowStatus_Type()
)
h3cVsiIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVsiIfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VSI-MIB",
    **{"h3cVsi": h3cVsi,
       "h3cVsiObjects": h3cVsiObjects,
       "h3cVsiScalarGroup": h3cVsiScalarGroup,
       "h3cVsiNextAvailableVsiIndex": h3cVsiNextAvailableVsiIndex,
       "h3cVsiL2vpnStatus": h3cVsiL2vpnStatus,
       "h3cVsiTable": h3cVsiTable,
       "h3cVsiEntry": h3cVsiEntry,
       "h3cVsiIndex": h3cVsiIndex,
       "h3cVsiName": h3cVsiName,
       "h3cVsiMode": h3cVsiMode,
       "h3cMinmIsid": h3cMinmIsid,
       "h3cVsiId": h3cVsiId,
       "h3cVsiTransMode": h3cVsiTransMode,
       "h3cVsiEnableHubSpoke": h3cVsiEnableHubSpoke,
       "h3cVsiAdminState": h3cVsiAdminState,
       "h3cVsiRowStatus": h3cVsiRowStatus,
       "h3cVsiSpbIsid": h3cVsiSpbIsid,
       "h3cVsiVxlanID": h3cVsiVxlanID,
       "h3cVsiArpSuppression": h3cVsiArpSuppression,
       "h3cVsiFlooding": h3cVsiFlooding,
       "h3cVsiLocalMacCount": h3cVsiLocalMacCount,
       "h3cVsiInterfaceID": h3cVsiInterfaceID,
       "h3cVsiStatistics": h3cVsiStatistics,
       "h3cVsiNvgreID": h3cVsiNvgreID,
       "h3cVsiXconnectTable": h3cVsiXconnectTable,
       "h3cVsiXconnectEntry": h3cVsiXconnectEntry,
       "h3cVsiXconnectIfIndex": h3cVsiXconnectIfIndex,
       "h3cVsiXconnectEvcSrvInstId": h3cVsiXconnectEvcSrvInstId,
       "h3cVsiXconnectVsiName": h3cVsiXconnectVsiName,
       "h3cVsiXconnectAccessMode": h3cVsiXconnectAccessMode,
       "h3cVsiXconnectHubSpoke": h3cVsiXconnectHubSpoke,
       "h3cVsiXconnectRowStatus": h3cVsiXconnectRowStatus,
       "h3cVsiPwBindTable": h3cVsiPwBindTable,
       "h3cVsiPwBindEntry": h3cVsiPwBindEntry,
       "h3cVsiPwIndex": h3cVsiPwIndex,
       "h3cVsiPwBindAttributes": h3cVsiPwBindAttributes,
       "h3cVsiPwBindRowStatus": h3cVsiPwBindRowStatus,
       "h3cVsiFloodMacTable": h3cVsiFloodMacTable,
       "h3cVsiFloodMacEntry": h3cVsiFloodMacEntry,
       "h3cVsiFloodMac": h3cVsiFloodMac,
       "h3cVsiFloodMacRowStatus": h3cVsiFloodMacRowStatus,
       "h3cVsiLocalMacTable": h3cVsiLocalMacTable,
       "h3cVsiLocalMacEntry": h3cVsiLocalMacEntry,
       "h3cVsiLocalMacAddr": h3cVsiLocalMacAddr,
       "h3cVsiLocalMacIfIndex": h3cVsiLocalMacIfIndex,
       "h3cVsiLocalMacSrvID": h3cVsiLocalMacSrvID,
       "h3cVsiPerfTable": h3cVsiPerfTable,
       "h3cVsiPerfEntry": h3cVsiPerfEntry,
       "h3cVsiPerfInOctets": h3cVsiPerfInOctets,
       "h3cVsiPerfInPackets": h3cVsiPerfInPackets,
       "h3cVsiPerfInErrors": h3cVsiPerfInErrors,
       "h3cVsiPerfInDiscards": h3cVsiPerfInDiscards,
       "h3cVsiPerfOutOctets": h3cVsiPerfOutOctets,
       "h3cVsiPerfOutPackets": h3cVsiPerfOutPackets,
       "h3cVsiPerfOutErrors": h3cVsiPerfOutErrors,
       "h3cVsiPerfOutDiscards": h3cVsiPerfOutDiscards,
       "h3cVsiNextAvailableVsiIfID": h3cVsiNextAvailableVsiIfID,
       "h3cVsiIfTable": h3cVsiIfTable,
       "h3cVsiIfEntry": h3cVsiIfEntry,
       "h3cVsiIfID": h3cVsiIfID,
       "h3cVsiIfIndex": h3cVsiIfIndex,
       "h3cVsiIfRowStatus": h3cVsiIfRowStatus}
)
